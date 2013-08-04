"""Tests for lattice module"""

import pymongo
from .. import lattice

def check_pickle_opened(n):
    """Lattice opens the pickle"""
    l = lattice.PartialOrderLattice(n, lat_dir='../lattices')
    assert l._lattice

def test_opening_pickles():
    for n in [3,4,5]:
        yield check_pickle_opened, n

def test_pickle_array_access():
    l = lattice.PartialOrderLattice(3, lat_dir='../lattices')
    assert l[frozenset([])]['down'] == set([frozenset([])])

def test_mongo_array_access():
    # development-specific configuration
    db =  pymongo.MongoClient().rankomatic
    l = lattice.PartialOrderLattice(3, lat_dir=None, mongo_db=db)
    assert l[frozenset([])]['down'] == set([frozenset([])])
