"""Datasets for use with ot Optimality Theory module.

DataSet -- vanilla OT dataset, a list of candidate objects
Candidate -- object for input/output pair, violation vector
ComparativeDataSet -- adds comparison of relevant candidate pairs
FunctionalDataSet -- adds functional space to each comparison pair
COTDataSet -- adds COT grammars for each comparison
PoOTDataSet -- adds PoOT grammars for each comparison

Note: each *DataSet on this list is a descendant of the *DataSet above
it.

"""
import itertools
import ordertheory


class DataSet(object):
    """Construct Dataset object.

    The original DataSet object. Converts a dict containing the dataset
    into a proper Python object, or rather a list of them.

    """

    def __init__(self):
        """Empty initialization."""
        self._dset = []
        self._edset = []

    @property
    def dset(self):
        """Dataset getter."""
        return self._dset

    @dset.setter
    def dset(self, value):
        """Dataset setter."""
        self._dset = self.get_dset(value)

    def get_dset(self, dset):
        """Turns list of dictionaries into list of
        'Candidate' objects"""
        return [Candidate(cand) for cand in dset]

    @property
    def edset(self):
        """Entailment dataset getter."""
        return self._edset

    @edset.setter
    def edset(self, value):
        """Entailment dataset setter."""
        self._edset = self.get_edset(value)

    def get_edset(self, dset):
        """Turns list of dictionaries into list of 'Candidate'
        objects, setting their optimal values to True."""
        dset = self.get_dset(dset)
        for cand in dset:
            cand.opt = True
        return dset


class Candidate(object):
    """Store the information for one candidate in a dataset.

    Essentially a bunch of getters and setters, this stores the data
    (input, output, optimality, and violation vector) for one candidate
    in a dataset.

    """

    def __str__(self):
        return str(self.cand)

    def __init__(self, dict0):
        self._inp = dict0['input']
        self._out = dict0['output']
        self._vvec = dict0['violation_vector']
        self._opt = dict0['optimal']
        self.cand = (self._inp, self._out)

    @property
    def inp(self):
        return self._inp

    @inp.setter
    def inp(self, value):
        self._inp = value

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value

    @property
    def vvec(self):
        return self._vvec

    @vvec.setter
    def vvec(self, value):
        self._vvec = value

    @property
    def opt(self):
        return self._opt

    @opt.setter
    def opt(self, value):
        self._opt = value


class ComparativeDataSet(DataSet):
    """Convert a vanilla DataSet into one with comparisons.

    Set the attribute cdset to a list of Candidates, and it will compare
    each of them, setting cdset to a dict of Candidates pointing to
    dicts of Candidates, where the value is the ComparativeInfo between
    the first key and second key.

    """

    def __init__(self):
        DataSet.__init__(self)
        self._cdset = {}

    @property
    def cdset(self):
        return self._cdset

    @cdset.setter
    def cdset(self, value):
        self._cdset = self.get_cdset(value)

    def __comp(self, dict0, dict1):
        """Compare two violation vectors, and return the comparison.

        Return a dict with values that are lists of the constraints
        represented as integers where dict0 strictly beats and
        strictly loses to (respectively keyed by 'win' and 'lose') to
        dict1, and the value keyed by 'hbounded' is true if there are
        no constraints that dict0 loses on.

        """
        win = []
        lose = []
        for n in dict0:
            if dict0[n] < dict1[n]:
                win.append(n)
            elif dict0[n] > dict1[n]:
                lose.append(n)
        if win and not lose:
            hbounded = True
            iequal = False
        elif not win and not lose:
            hbounded = False
            iequal = True
        else:
            hbounded = False
            iequal = False
        return {'win': win, 'lose': lose,
                'hbounded': hbounded, 'iequal': iequal}

    def __init_cdset(self, dset):
        """Create an (empty) comparative dictionary (or dataset).

        Build up a dictionary of dictionaries, where each key is a
        Candidate cand0, and the value is an empty dict of Candidates
        cand1, where cand0 and cand1 have the same input and at least
        one of cand0 or cand1 is optimal.

        """
        cdset = {}
        for cand0, cand1 in itertools.product(dset, dset):
            if cand0.inp == cand1.inp:
                try:
                    cdset[cand0].update({cand1: {}})
                except KeyError:
                    cdset.update({cand0: {cand1: {}}})
        return cdset

    def get_cdset(self, dset):
        cdset = self.__init_cdset(dset)
        self.hbounded = set()
        for cand0 in cdset.keys():
            for cand1 in cdset[cand0].keys():
                compinfo = cdset[cand0][cand1]
                comps = self.__comp(cand0.vvec, cand1.vvec)
                if comps['hbounded']:  # remove hbounded candidates
                    self.hbounded.add(cand1)
                compinfo.update(comps)
                cdset[cand0][cand1] = ComparativeInfo(compinfo)
        self._remove_hbounded_cands(cdset)
        return cdset

    def _remove_hbounded_cands(self, cdset):
        for hbound in self.hbounded:
            cdset.pop(hbound)
        for cand0 in cdset:
            for hbound in self.hbounded:
                try:
                    cdset[cand0].pop(hbound)
                except KeyError:
                    pass
        return cdset


class ComparativeInfo(object):
    """Hold the comparisons between two candidates.

    Given two candidates cand0 and cand1, contains a list of
    constraints cand0 wins on, loses on, and whether or not cand0 is
    harmonically bounded. Also stores the original dict of comparisons.

    """

    def __init__(self, dict0):
        self.info = dict0
        self.win = dict0['win']
        self.lose = dict0['lose']
        self.hbounded = dict0['hbounded']
        self.iequal = dict0['iequal']


class FunctionalDataSet(ComparativeDataSet):
    """Get the functional space from losing to winning candidates.

    For each pair of candidates cand0 and cand1 in the
    ComparativeDataSet, calculate the functional space from the set of
    losing to the set of winning constraints and add it to the info for
    cdset[cand0][cand1]

    """

    def __init__(self):
        ComparativeDataSet.__init__(self)
        self._fdset = {}

    @property
    def fdset(self):
        return self._fdset

    @fdset.setter
    def fdset(self, value):
        value = super(FunctionalDataSet, self).get_cdset(value)
        self._fdset = self.get_fdset(value)

    def get_fdset(self, cdset):
        """Calculate the functional space for each pair of candidates.

        Specifically calculate the functional space from losing to
        winning constraints for each pair of candidates in the dataset.

        """
        fspace = ordertheory.FunctionalSpace()
        for cand0 in cdset:
            for cand1 in cdset[cand0]:
                finfo = cdset[cand0][cand1]
                funcs = fspace.funcs(finfo.lose, finfo.win)
                finfo.info.update({'fspace': funcs})
                cdset[cand0][cand1] = FunctionalInfo(finfo.info)
        return cdset


class FunctionalInfo(ComparativeInfo):

    def __init__(self, dict0):
        ComparativeInfo.__init__(self, dict0)
        self.fspace = dict0['fspace']


class COTDataSet(FunctionalDataSet):
    """Store the Classical OT (COT) grammars that satisfy the dataset"""

    def get_cotdset(self, fdset, lattice, apriori=frozenset([])):
        """Calculate the COT grammars for each pair of candidates.

        For each pair cand0 and cand1, add a set containing the maxsets
        of all the functions from losing to winning.  The maxset of
        each function (considered as a partial order) is one of the
        COT grammars that satisfies that comparison.

        """
        apriori_compatible = lattice[apriori]['max']
        for cand0 in fdset.keys():
            for cand1 in fdset[cand0].keys():
                cots = set([])
                cotinfo = fdset[cand0][cand1]
                if cotinfo.iequal:
                    cots = lattice[frozenset([])]['max']
                else:
                    for f in cotinfo.fspace:
                        cots.update(lattice[frozenset(f)]['max'])
                cots = set.intersection(cots, apriori_compatible)
                cotinfo.info.update({'cots': cots})
                fdset[cand0][cand1] = COTInfo(cotinfo.info)
        return fdset


class COTInfo(FunctionalInfo):

    def __init__(self, dict0):
        FunctionalInfo.__init__(self, dict0)
        self.cots = dict0['cots']


class PoOTDataSet(COTDataSet):
    """Store the Partial order OT (PoOT) grammars for the dataset"""

    def get_pootdset(self, fdset, lattice, apriori=frozenset([])):
        """Calculate the PoOT grammars for each pair of candidates

        For each pair cand0 and cand1, add a set containing the union
        of the downsets of all the COT grammars that satisfy the
        cand0 ~ cand1 comparison. Each element of the downset of a COT
        grammar is a subset of that grammar, and thus also satisfies the
        requirements of the candidate pair.

        """
        cotdset = self.get_cotdset(fdset, lattice, apriori)
        apriori_compatible = lattice[apriori]['up']
        for cand0 in cotdset:
            for cand1 in cotdset[cand0]:
                pootinfo = cotdset[cand0][cand1]
                if pootinfo.iequal:
                    poots = lattice[frozenset([])]['up']
                elif not pootinfo.iequal and not pootinfo.cots:
                    poots = pootinfo.cots
                else:
                    downs = [lattice[frozenset(cot)]['down']
                             for cot in pootinfo.cots]
                    poots = set.union(*map(set, downs))
                poots = set.intersection(poots, apriori_compatible)
                pootinfo.info.update({'poots': poots})
                cotdset[cand0][cand1] = PoOTInfo(pootinfo.info)
        return cotdset


class PoOTInfo(COTInfo):

    def __init__(self, dict0):
        COTInfo.__init__(self, dict0)
        self.poots = dict0['poots']


class GrammarDataSet(PoOTDataSet):
    """Store the optimal grammars for each candidate in the dataset"""

    def get_grammardset(self, fdset, lattice, apriori=frozenset([])):
        pootdset = self.get_pootdset(fdset, lattice, apriori)

        for cand in pootdset:
            opt_cots = self._opt_grams(pootdset[cand])
            opt_poots = self._opt_grams(pootdset[cand], classical=False)
            pootdset[cand].update({'opt_cots': opt_cots,
                                   'opt_poots': opt_poots})
        return pootdset

    def _opt_grams(self, candinfo, classical=True):
        """Get the grammars that make a candidate optimal.

        Return the intersection of the grammars that make the candidate
        more harmonic than each of the candidates it is compared to.  If
        classical is False, return the PoOT grammars that do so,
        otherwise return the COT grammars.

        """
        cand_keys = (k for k in candinfo if type(k) is not str)
        if classical:
            l = [candinfo[cand0].cots for cand0 in cand_keys]
        else:
            l = [candinfo[cand0].poots for cand0 in cand_keys]
        return set.intersection(*map(set, l))


class ClassicalGrammarDataset(GrammarDataSet):

    def get_grammardset(self, fdset, lattice, apriori=frozenset([])):
        cotdset = self.get_cotdset(fdset, lattice, apriori)
        for cand in cotdset:
            opt_cots = self._opt_grams(cotdset[cand])
            cotdset[cand].update({'opt_cots': opt_cots})

        return cotdset
