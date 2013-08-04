"""Test a PoOT built on a mongoDB lattice"""

import pymongo
import cPickle
from .. import poot
from .. import data
import test_poot

class TestMongoPoOT(test_poot.TestPoOT):

    def setUp(self):
        # development-specific configuration
        db = pymongo.MongoClient().rankomatic
        self.p = poot.PoOT(lat_dir=None, mongo_db=db)
        with open('../lattices/gspace_4cons.p', 'rb') as f:
            self.lattice = cPickle.load(f)

    def test_lattice_setter(self):
        """PoOT lattice setter work?"""
        self.p.lattice = data.voweldset
        # go find privately stored lattice inside Lattice object
        assert self.p._lattice._lattice is None
        test_str = "Database(MongoClient('localhost', 27017), u'rankomatic')"
        assert str(self.p._lattice._mongo_db) == test_str

    def test_dset_setter(self):
        """disregard, simply overrides the parent"""
        pass  # overrides parent method
