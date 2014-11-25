"""Lattice class, for use with order-theoretic applications.

Lattice -- stores information and methods for implementing a lattice

"""

import cPickle
import os
from ordertheory import StrictOrders, StrictTotalOrders


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
        stored in that database. If both lat_dir and mongo_db evaluate
        to False, the _lattice attribute is set to None, and an error
        will be raised if the access is attempted.

        """
        self.num_lat_queries = 0
        self.set_n = set_n
        self._lat_dir = lat_dir
        self._mongo_db = mongo_db
        if self._mongo_db:
            self._mongo_coll = getattr(self._mongo_db, 'lat%d' % self.set_n)
            self._lattice = None
        elif self._lat_dir:
            print 'loading lattice from cPickle...'
            self._lattice = self.__read_from_pickle(self.set_n, self._lat_dir)
            print 'lattice loaded.'
            self._mongo_coll = None
        else:
            self._lattice = None

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
        elif self._lattice is not None:
            self.num_lat_queries += 1
            return self._lattice[key]
        else:
            raise KeyError('Lattice must be initialized from a pickle, '
                           'MongoDB, or generated.')

    def generate_lattice(self, verbose=False):
        """Generates a lattice from scratch.

        Consider this fair warning: lattices of partial orders get
        huge, fast.  In 2013, with a new core i5 and 6GB memory, there
        simply weren't enough resources to generate a 6-constraint
        lattice.  If you try and generate anything with set_n larger
        than 5, you're on your own.

        """
        if not self._lattice:
            lat = StrictOrders().get_orders(xrange(1, self.set_n + 1), verbose)
            self._lattice = lat

    def __read_from_pickle(self, size, dirname):
        """Read a lattice of size 'size' from a pickle in dirname."""
        filename = 'gspace_%scons.p' % size
        with open(os.path.join(dirname, filename), 'rb') as f:
            return cPickle.load(f)

    def _checks_if_writable(fun, *args, **kwargs):
        """Decorator to check if the lattice can be written from"""
        def wrapper(self, *args, **kwargs):
            if not self._lattice:
                raise TypeError('Lattice must be initialized from a pickle '
                                'or generated.')
            else:
                return fun(self, *args, **kwargs)
        return wrapper

    @_checks_if_writable
    def write_to_pickle(self, lat_dir):
        """Write the current lattice to a pickle in lat_dir.

        Only supports lattices that have been explicitly generated or
        loaded from a file themselves.  Attempting to write a lattice
        that has been initialized from a pymongo.  Database instance will
        result in a TypeError.  Writing from a lattice that has not been
        initialized will also result in a TypeError.

        """
        filename = os.path.join(lat_dir, 'gspace_%dcons.p' % self.set_n)
        with open(filename, 'wb') as f:
            cPickle.dump(self._lattice, f)

    @_checks_if_writable
    def write_to_mongo(self, db):
        """Write the lattice to the given instance MongoDB database.

        Stores the currently loaded lattice in a collection within the
        given database.  The collection will be named 'latN', where N is
        equal to self.set_n.  For example, a lattice where set_n = 4
        will be stored in 'db.lat4'.  Any previous collection with that
        name will be dropped, so be sure you are ok with that.  This
        function, like write_to_pickle, only supports lattices that have
        either been loaded from a file or generated explicitly.  Writing
        from a MongoDB-backed lattice will throw a TypeError.

        """
        col_name = 'lat%d' % self.set_n
        mongo_col = getattr(db, col_name)
        mongo_col.drop()
        for k, v in self._lattice.iteritems():
            doc = {'set': str(sorted(k)), 'value': str(v)}
            mongo_col.insert(doc)


class TotalOrderLattice(object):
    """The lattice of total orders."""

    def __init__(self, set_n):
        self.set_n = set_n
        self.torders = list(StrictTotalOrders().orders(
            xrange(1, self.set_n + 1)
        ))
        self.num_lat_queries = 0

    def __getitem__(self, key):
        print "querying lattice"
        if type(key) is not frozenset:
            raise TypeError("keys to lattice must be of type frozenset")
        super_sets = set()
        for total_order in self.torders:
            if total_order >= key:
                super_sets.add(total_order)
        self.num_lat_queries += 1
        return {'max': super_sets}
