"""Tests for lattice module"""

import pymongo
from .. import lattice

def check_pickle_opened(n):
    """Lattice opens the pickle"""
    l = lattice.PartialOrderLattice(n, lat_dir='../lattices')
    assert l._lattice

def test_opening_pickles():
    """Pickle open ok?"""
    for n in [3,4,5]:
        yield check_pickle_opened, n

def test_pickle_array_access():
    """Array access on pickle-loaded lattice?"""
    l = lattice.PartialOrderLattice(3, lat_dir='../lattices')
    assert l[frozenset([])]['down'] == set([frozenset([])])

def test_mongo_array_access():
    """Array access on MongoDB-based lattice? **Development env specific**"""
    db =  pymongo.MongoClient().rankomatic
    l = lattice.PartialOrderLattice(3, lat_dir=None, mongo_db=db)
    assert l[frozenset([])]['down'] == set([frozenset([])])

def test_write_from_mongo_lattice_fails():
    """Does writing from a MongoDB-backed lattice raise an error?"""
    db = pymongo.MongoClient().rankomatic
    l = lattice.PartialOrderLattice(3, lat_dir=None, mongo_db=db)
    try:
        l.write_to_pickle('lattices')
    except TypeError:
        assert True
    else:
        assert False

def check_generate_lattice(n):
    l_orig = lattice.PartialOrderLattice(n, lat_dir='../lattices')
    l_new = lattice.PartialOrderLattice(n, lat_dir=None, mongo_db=None)
    l_new.generate_lattice()
    assert l_orig._lattice == l_new._lattice

def test_generate_lattice():
    """Generate lattice ok?"""
    for n in [3, 4]:
        yield check_generate_lattice, n

def check_write_lattice_to_pickle(n):
    l_orig = lattice.PartialOrderLattice(n, lat_dir=None)
    l_orig.generate_lattice()
    l_orig.write_to_pickle(lat_dir='lattices')
    l_sec = lattice.PartialOrderLattice(n, lat_dir='lattices')
    assert l_orig._lattice == l_sec._lattice

def test_write_to_pickle():
    """Write lattice to pickle ok?"""
    for n in [3,4]:
        yield check_write_lattice_to_pickle, n

def check_write_lattice_to_mongo(n):
    l_orig = lattice.PartialOrderLattice(n, lat_dir='../lattices/')
    db = pymongo.MongoClient().test_lats
    l_orig.write_to_mongo(db)
    l_new = lattice.PartialOrderLattice(n, lat_dir=None, mongo_db=db)
    assert l_new[frozenset([])]['down'] == set([frozenset([])])

def test_write_to_mongo():
    """Wrtie lattice to MongoDB ok?"""
    for n in [3,4]:
        yield check_write_lattice_to_mongo, n
