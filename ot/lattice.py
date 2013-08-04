"""Lattice class, for use with order-theoretic applications.

Lattice -- stores information and methods for implementing a lattice

"""

import cPickle
import os
import ordertheory
import pymongo


class PartialOrderLattice(object):
    """The lattice of partial orders.

    Stores all the partial orders of a set and the relationships
    necessary to represent a lattice. For any partial order in the
    space, stores a dict with keys 'up', 'down', and 'max', which
    represent the upset, downset, and maxset, respectively, of that
    partial order.

    __init__ -- constructor (see its docstring for further info)
    __getitem__ -- array '[]' syntax, returns a node from the lattice


    """

    def __init__(self, set_n, lat_dir, mongo_db=None):
        """Store the lattice, given a size and where to find it.

        Args:
          set_n -- the size of the set to get partial orders from
          lat_dir -- the directory to find the lattice pickles in
          mongo_db -- a pymongo Database instance

        If mongo_db evaluates to False, the lattice is loaded from
        a pickle file in the directory pointed to by lat_dir.  If
        mongo_db evaluates to True, lat_dir is ignored and the
        instance becomes effectively a frontend to the MongoDB
        collection representing the lattice of the desired size,
        stored in that database.

        """
        self.set_n = set_n
        self._lat_dir = lat_dir
        self._mongo_db = mongo_db
        if self._mongo_db:
            self._mongo_coll = self._mongo_db.__getattr__('lat%d' % self.set_n)
            self._lattice = None
        else:
            self._lattice = self.__read_lat_from_pickle(self.set_n, self._lat_dir)
            self._mongo_coll = None

    def __getitem__(self, key):
        """Get a dict with the maxset, upset, and downset for key.

        If key is of type frozenset, will return a dict with three keys
        'up', 'down', and 'max', which represent the upset, downset,
        and maxset, respectively, of the order represented by key.

        """
        if type(key) is not frozenset:
            raise TypeError("keys to lattice must be of type frozenset")
        if self._mongo_db:
            mongo_doc = self._mongo_coll.find_one({'set': str(sorted(key))})
            return eval(mongo_doc['value'])
        else:
            return self._lattice[key]


    def __read_lat_from_pickle(self, size, dirname):
        filename = 'gspace_%scons.p' % size
        with open(os.path.join(dirname, filename), 'rb') as f:
            return cPickle.load(f)




