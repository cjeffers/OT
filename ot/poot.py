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
from lattice import PartialOrderLattice as POLattice


class PoOT(object):

    def __init__(self, lat_dir, mongo_db=None):
        self._dset = []
        self._lattice = {}
        self._lat_dir = lat_dir
        self._mongo_db = mongo_db
        self._grammardset = None

    def _ensure_grammardset(fun, *args, **kwargs):
        """Make sure a grammar dset exists, generates it if not."""
        def wrapper(self, *args, **kwargs):
            if self._grammardset is None:
                gdset = dataset.GrammarDataSet()
                gdset.dset = self.dset
                gdset.cdset = gdset.dset
                gdset.fdset = gdset.cdset
                self._grammardset = gdset.get_grammardset(gdset.fdset,
                                                          self.lattice)
            return fun(self, *args, **kwargs)
        return wrapper

    @property
    def dset(self):
        return self._dset

    @dset.setter
    def dset(self, value):
        opts = [value[i]['optimal'] for i, cand in enumerate(value)]
        if not any(opts):
            raise ValueError('At least one candidate must be optimal.')
        self.lattice = value
        if type(value) is tuple:
            value = value[0]
        self._dset = self._dset + value

    @property
    def lattice(self):
        return self._lattice

    @lattice.setter
    def lattice(self, value):
        cons = len(value[0]['vvector'])
        self._lattice = POLattice(cons, self._lat_dir, self._mongo_db)

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
            cand_keys = (k for k in self._grammardset[cand0] if type(k) is not str)
            for cand1 in cand_keys:
                if self._grammardset[cand0][cand1].hbounded:
                    l.append((cand0.cand, cand1.cand))
        return l

    @_ensure_grammardset
    def get_grammars(self, classical=True):
        """Get all grammars compatible with a dataset."""
        return Grammars().get_grammars(self._grammardset, classical)

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
        try:
            pos = set.intersection(*map(set, pos_grammars))
        except TypeError:  # case when pos_grammars is empty
            pos = set([])

        neg_grammars = []
        for cand in dset:
            if not cand.opt:
                neg_grammars.append(self.opt_grams(dset[cand], classical))
        try:
            neg = set.union(*map(set, neg_grammars))
        except TypeError:  # case when neg_grammars is empty
            neg = set([])
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
                    lattice.update({s:{'up':set([]), 'down':set([])}})
                if u.issuperset(v):
                    lattice[s]['down'].add(t)
                    if u.issubset(v):
                        lattice[s]['up'].add(t)
                elif u.issubset(v):
                    lattice[s]['up'].add(t)
        return lattice







