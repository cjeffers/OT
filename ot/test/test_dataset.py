import unittest
from .. import ordertheory
from .. import dataset
from .. import data

class DataSetTests(unittest.TestCase):

    def setUp(self):
        self.ds = dataset.DataSet()
        self.vowel_set = data.voweldset

    def test_init(self):
        """DatSet intialize ok?"""
        self.assertEqual(self.ds.dset, [])
        self.assertEqual(self.ds.edset, [])

    def test_dset_getter_setter(self):
        """DataSet.dset property, also candidate getting/setting"""
        self.ds.dset = self.vowel_set
        for c, d in zip(self.ds.dset, self.vowel_set):
            self.assertEqual(c.inp, d['input'], "inputs don't match")
            self.assertEqual(c.out, d['output'], "outputs don't match")
            self.assertEqual(c.opt, d['optimal'], "optimality doesn't match")
            self.assertEqual(c.vvec, d['vvector'], "violation vectors don't match")

    def test_edset_getter_setter(self):
        """Entailment dset property, also candidate getting/setting"""
        self.ds.edset = self.vowel_set
        for c, d in zip(self.ds.edset, self.vowel_set):
            self.assertEqual(c.inp, d['input'], "inputs don't match")
            self.assertEqual(c.out, d['output'], "outputs don't match")
            self.assertEqual(c.vvec, d['vvector'], "violation vectors don't match")
            self.assertTrue(c.opt, "non-optimal entailment candidate")


class ComparativeDataSetTests(unittest.TestCase):

    def setUp(self):
        self.cds = dataset.ComparativeDataSet()
        self.vowel_set = data.voweldset

    def test_init(self):
        """ComparativeDataSet initialized ok?"""
        self.assertEqual(self.cds.cdset, {}, "didn't initialize to empty dict")

    def test_cdset_getter_setter(self):
        """Comparative vectors generated ok?"""
        self.cds.dset = self.vowel_set
        self.cds.cdset = self.cds.dset
        for cand0 in self.cds.cdset:
            for cand1 in self.cds.cdset[cand0]:
                compinfo = self.cds.cdset[cand0][cand1]
                for w in compinfo.win:
                    self.assertTrue(cand0.vvec[w] < cand1.vvec[w])
                for l in compinfo.lose:
                    self.assertTrue(cand0.vvec[l] > cand1.vvec[l])


class FunctionalDataSetTests(unittest.TestCase):

    def setUp(self):
        self.fds = dataset.FunctionalDataSet()
        self.vowel_set = data.voweldset

    def test_init(self):
        """FunctionalDataSet intialize ok?"""
        self.assertEqual(self.fds.fdset, {}, "didn't initialize to empty dict")

    def test_fdset_getter_setter(self):
        """Functional space calculated ok?"""
        self.fds.dset = self.vowel_set
        self.fds.cdset = self.fds.dset
        self.fds.fdset = self.fds.cdset
        for cand0 in self.fds.dset:
            for cand1 in self.fds.fdset[cand0]:
                finfo = self.fds.fdset[cand0][cand1]
                fspace = finfo.fspace
                fs = ordertheory.FunctionalSpace()
                r_fspace = fs.funcs(finfo.lose, finfo.win)
                self.assertEqual(fspace, r_fspace, "The functional spaces didn't match")


class COTDataSetTests(unittest.TestCase):

    def setUp(self):
        cotds = dataset.COTDataSet()
        cotds.dset = data.voweldset
        cotds.cdset = cotds.dset
        cotds.fdset = cotds.cdset
        self.cotds = cotds

    def test_cot_dset(self):
        """COTDataSet get correct COT grammars?"""
        lattice = ordertheory.StrictOrders().get_orders([1,2,3,4])
        cots = self.cotds.get_cotdset(self.cotds.fdset, lattice)
        for cand0 in cots:
            for cand1 in cots[cand0]:
                info = cots[cand0][cand1]
                for f in info.fspace:
                    maxset = lattice[frozenset(f)]['max']
                    for s in maxset:
                        msg = "%s in %s's maxset isn't in COT" % (str(s), str(f))
                        self.assertTrue(s in info.cots, msg)


class PoOTDataSetTests(unittest.TestCase):

    def setUp(self):
        pds = dataset.PoOTDataSet()
        pds.dset = data.voweldset
        pds.cdset = pds.dset
        pds.fdset = pds.cdset
        self.lattice = ordertheory.StrictOrders().get_orders([1,2,3,4])
        pds.get_cotdset(pds.fdset, self.lattice)
        self.pds = pds

    def test_poot_dset(self):
        """PoOTDataSet get correct PoOT grammars?"""
        poots = self.pds.get_pootdset(self.pds.fdset, self.lattice)
        for cand0 in poots:
            for cand1 in poots[cand0]:
                info = poots[cand0][cand1]
                for c in info.cots:
                    for p in self.lattice[c]['down']:
                        msg = "%s in %s's downset not in PoOT" % (str(p), str(c))
                        self.assertTrue(p in info.poots, msg)





