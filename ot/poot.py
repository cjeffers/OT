"""Calculate constraint rankings and entailments in Optimality Theory.

PoOT -- object for holding data and calling calculation methods
  dset -- the dataset attribute
  lattice -- the lattice attribute
  get_optimal_candidates -- return the candidates that are optimal
  get_non_optimal_candidates -- return tho other ones
  get_harmonically_bounded_candidates -- read the name of the function
  is_compatible_COT_grammar -- check if a grammar works with COT dset
  is_compatible_PoOT_grammar -- check if a grammar works with PoOT dset
  is_min_grammar -- is PoOT grammar minimally compatible?
  min -- return all minimal grammars
  is_max_grammar -- is PoOT grammar maximally compatible?
  max -- return all maximal grammars
  get_entailments -- get the set of candidate entailments

Grammar -- exports functions for handling grammars
  opt_grams -- all the grammars that are in a candidate's info
  get_grammars -- get grammars compatible with a dataset

Entailments
  get_entails -- get the entailmentes between sets of candidates

"""
import itertools
import dataset
from ordertheory import Powerset
from lattice import PartialOrderLattice, TotalOrderLattice


class TooManyConstraintsForPartialGrammars(Exception):
    pass


def _ensure_grammardset(fun, *args, **kwargs):
    """Wrap a function to make sure the GrammarDataSet exists."""
    def wrapper(self, *args, **kwargs):
        if self._grammardset is None:
            if self.set_n <= PoOT.MAX_POOT_CONSTRAINTS:
                gdset = dataset.GrammarDataSet()
            else:
                gdset = dataset.ClassicalGrammarDataset()
            gdset.dset = self.dset
            gdset.cdset = gdset.dset
            gdset.fdset = gdset.cdset
            self._grammardset = gdset.get_grammardset(gdset.fdset,
                                                      self.lattice)
        return fun(self, *args, **kwargs)
    return wrapper


class PoOT(object):

    MAX_POOT_CONSTRAINTS = 6

    def __init__(self, lat_dir, mongo_db=None):
        self._dset = []
        self._lattice = {}
        self._lat_dir = lat_dir
        self._mongo_db = mongo_db
        self._grammardset = None
        self._compatible_cots = None
        self._compatible_poots = None

    @property
    def dset(self):
        return self._dset

    @dset.setter
    def dset(self, value):
        if type(value) is tuple:
            value = value[0]
        opts = [value[i]['optimal'] for i, cand in enumerate(value)]
        self.set_n = len(value[0]['vvector'])
        if not any(opts):
            raise ValueError('At least one candidate must be optimal.')
        self.lattice = value
        self._dset = self._dset + value
        self._compatible_cots = None
        self._compatible_poots = None

    @property
    def lattice(self):
        return self._lattice

    @property
    def num_constraints(self):
        return len(self.dset[0]['vvector'])

    @lattice.setter
    def lattice(self, value):
        cons = len(value[0]['vvector'])
        if cons <= PoOT.MAX_POOT_CONSTRAINTS:
            self._lattice = PartialOrderLattice(cons,
                                                self._lat_dir,
                                                self._mongo_db)
        else:
            self._lattice = TotalOrderLattice(cons)

    @_ensure_grammardset
    def get_optimal_candidates(self):
        """Get all optimal candidates."""
        opt = [cand.cand for cand in self._grammardset if cand.opt]
        return opt

    @_ensure_grammardset
    def get_nonoptimal_candidates(self):
        """Get all non-optimal candidates."""
        nonopt = [cand.cand for cand in self._grammardset if not cand.opt]
        return nonopt

    @_ensure_grammardset
    def get_harmonically_bounded_candidates(self):
        """Get all harmonically bound candidate pairs"""
        l = []
        for cand0 in self._grammardset:
            cand_keys = (k for k in self._grammardset[cand0] if
                         type(k) is not str)
            for cand1 in cand_keys:
                if self._grammardset[cand0][cand1].hbounded:
                    l.append((cand0.cand, cand1.cand))
        return l

    @_ensure_grammardset
    def get_grammars(self, classical=True):
        """Get all grammars compatible with a dataset."""
        if not classical and self.set_n > PoOT.MAX_POOT_CONSTRAINTS:
            msg = ("Datasets with more than %d constraints can only find"
                   "classical grammars.") % PoOT.MAX_POOT_CONSTRAINTS
            raise TooManyConstraintsForPartialGrammars(msg)
        if classical:
            if not self._compatible_cots:
                self._compatible_cots = Grammars().get_grammars(
                    self._grammardset, classical
                )
            return self._compatible_cots
        else:
            if not self._compatible_poots:
                self._compatible_poots = Grammars().get_grammars(
                    self._grammardset, classical
                )
                cot_len = sum(range(self.set_n))
                compatible_cots = [g for g in self._compatible_poots
                                   if len(g) == cot_len]
                self._compatible_cots = set(compatible_cots)
            return self._compatible_poots

    def is_compatible_COT_grammar(self, grammar):
        """Check whether COT grammar is compatible with the dataset."""
        cots = self.get_grammars(classical=True)
        return grammar in cots

    def is_compatible_PoOT_grammar(self, grammar):
        """Check whether PoOT grammar is compatible with the dataset."""
        poots = self.get_grammars(classical=False)
        return grammar in poots

    def is_min_grammar(self, grammar):
        """Check whether PoOT grammar is minimally compatible."""
        down = set(self.lattice[grammar]['down'])
        grams = self.get_grammars(classical=False)
        return len(down.intersection(grams)) == 1

    def min(self, grammars):
        """Get all minimal grammars."""
        s = set([])
        for grammar in grammars:
            if self.is_min_grammar(grammar):
                s.add(grammar)
        return s

    def is_max_grammar(self, grammar):
        """Check whether PoOT grammar is maximally compatible."""
        up = set(self.lattice[grammar]['up'])
        grams = self.get_grammars(classical=False)
        return len(up.intersection(grams)) == 1

    def max(self, grammars):
        """Get all maximal grammars."""
        s = set([])
        for grammar in grammars:
            if self.is_max_grammar(grammar):
                s.add(grammar)
        return s

    @_ensure_grammardset
    def get_entailments(self, atomic=True):
        """Get candidate entailments.

        If atomic is True, get atomic entailments.  Else, get
        entailments between sets of candidates.

        """
        return Entailments().get_entails(self._grammardset, atomic)


class Grammars(object):

    def opt_grams(self, candinfo, classical=True):
        if classical:
            return candinfo['opt_cots']
        else:
            return candinfo['opt_poots']

    def get_grammars(self, dset, classical=True):
        """Get grammars compatible with dataset.

        Collect the optimal grammars for each comparison into two
        sets of grammars: pos represents the intersection of all the
        grammars that make the optimal candidates win, and neg
        represents the union of all the grammars that make the non-
        optimal candidates win. The set of grammars compatible with
        the entire dataset is pos - neg.

        """
        pos_grammars = []
        for cand in dset:
            if cand.opt:
                pos_grammars.append(self.opt_grams(dset[cand], classical))

        pos = set.intersection(*map(set, pos_grammars))

        neg_grammars = []
        for cand in dset:
            if not cand.opt:
                neg_grammars.append(self.opt_grams(dset[cand], classical))

        if not neg_grammars:
            neg_grammars = [[]]

        neg = set.union(*map(set, neg_grammars))

        return pos.difference(neg)


class Entailments(object):

    def __mapping(self, dset):
        """Map candidates to the PoOT grammars that make it optimal.

        Return a list of tuples pairing the candidate to the set of all
        and only the PoOT grammars that make that candidate optimal.

        """
        grams = Grammars()
        return [(cand, grams.opt_grams(dset[cand])) for cand in dset]

    def get_entails(self, dset, atomic=True):
        """Get entailments between (sets of) candidates.

        If the optimal grammars for a candidate cand0 are a subset of
        the optimal grammars for a candidate cand1, then cand0 entails
        cand1.

        """
        lattice = {}
        mapping = self.__mapping(dset)
        if atomic:
            prod = itertools.product(mapping, mapping)
        else:
            pset = list(Powerset().powerset(mapping))
            prod = itertools.product(pset, pset)
        for x, y in prod:
            if x and y:
                if atomic:
                    s = frozenset([x[0].cand])
                    t = frozenset([y[0].cand])
                    u = x[1]
                    v = y[1]
                else:
                    s = frozenset([pair[0].cand for pair in x])
                    t = frozenset([pair[0].cand for pair in y])
                    u = set.intersection(*map(set, [pair[1] for pair in x]))
                    v = set.intersection(*map(set, [pair[1] for pair in y]))
                try:
                    lattice[s]
                except KeyError:
                    lattice.update({s: {'up': set([]), 'down': set([])}})
                if u.issuperset(v):
                    lattice[s]['down'].add(t)
                    if u.issubset(v):
                        lattice[s]['up'].add(t)
                elif u.issubset(v):
                    lattice[s]['up'].add(t)
        return lattice


class OTStats(PoOT):
    """Exports basic statistics for a PoOT dataset.

    num_compatible_poots, num_compatible_cots -- get the number of
        compatible PoOT and COT grammars
    num_total_poots, num_compatible_cots -- get the total possible
        number of PoOT and COT grammars for the number of constraints
    num_cots_by_cand -- get a dictionary from input-output pairs to
        the number of cots that make that pair optimal
    """

    const_info = {
        2: {'total_poots': 3, 'total_cots': 2, 'cot_len': 1},
        3: {'total_poots': 19, 'total_cots': 6, 'cot_len': 3},
        4: {'total_poots': 219, 'total_cots': 24, 'cot_len': 6},
        5: {'total_poots': 4231, 'total_cots': 120, 'cot_len': 10},
        6: {'total_poots': 130023, 'total_cots': 720, 'cot_len': 15}
    }

    def num_compatible_poots(self):
        """Get the number of compatible PoOT grammars"""
        return len(self.get_grammars(False))

    def num_compatible_cots(self, grammar=frozenset([])):
        """Get the number of compatible COT grammars"""
        grammars = self.get_grammars(True)
        return len([g for g in grammars if g.issuperset(grammar)])

    def num_total_poots(self):
        """Get the number of possible PoOT grammars"""
        return self.const_info[self.num_constraints]['total_poots']

    def num_total_cots(self, grammar=frozenset([])):
        """Get the number of possible COT grammars"""
        cots = self.lattice[frozenset([])]['max']
        return len([cot for cot in cots if cot.issuperset(grammar)])

    @_ensure_grammardset
    def num_cots_by_cand(self, grammar=frozenset([])):
        """Get the number of COTs that make each candidate optimal.

        Return a dictionary from input-output pairs to the number of
        cots that make that pair optimal

        """
        ret = {}
        for cand in self._grammardset:
            opt_cots = self._grammardset[cand]['opt_cots']
            num_cots = len([cot for cot in opt_cots if
                            cot.issuperset(grammar)])
            ret[cand.cand] = num_cots
        return ret
