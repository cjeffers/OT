"""Perform order and set-theoretic operations.

Powerset -- return the powerset of any iterable
FunctionalSpace -- get the functional space from one iterable to another
StrictTotalOrders -- get the strict total orders for an iterable
StrictOrders -- get the lattices for an iterable

"""
import itertools
import pickle

class Powerset(object):

    def powerset(self, iterable):
        """Return an iterable of all possible subsets.

        Each subset is represented as a tuple of zero or more elements
        from iterable.

        """
        l = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(l, r) for r in range(len(l)+1))


class FunctionalSpace(object):

    def __rel(self, list0, list1):
        """Calculate all possible relations from list0 into list1.

        Returns an iterable of dicts, where keys are elements of list0
        and values are elements of list1. Returned iterator may contain
        duplicate dicts.

        """
        prod = itertools.product(list0, list1)
        pset = Powerset().powerset(prod)
        for rel in pset:
            yield dict(list(rel))

    def funcs(self, list0, list1):
        """Get a list of all possible functions from list0 into list1.

        Each function f is represented as a list of tuples (x, y) where
        f(x) = y.

        """
        dom = list(list0)
        codom = list(list1)
        if not codom:
            return []
        elif codom and not dom:
            return [[]]
        elif dom and codom:
            rel = self.__rel(dom, codom)
            # tupleize and uniq the dicts in rel
            functions = set([tuple(item.items()) for item in rel])
            # return the lists (functions) with the right size domain
            return [list(f) for f in functions if len(f) == len(dom)]


class StrictTotalOrders(object):

    def __recurse(self, l, orders=[]):
        """Get a set-based representation of an order.

        Recursively travel through l, creating tuples where the first
        element of l is ordered before each of the following elements,
        and appending those to the orders list.

        """
        if l:
            orders = orders + list(itertools.product([l[0]], list(l[1:])))
            return self.__recurse(list(l[1:]), orders)
        else:
            return orders

    def orders(self, iterable):
        """Return an iterator over all strict total orders.

        Gives one strict total order for each possible permutation.
        Each strict total order is represented as a frozenset of tuples
        (x, y) such that x >> y.

        """
        l = list(iterable)
        permutations = itertools.permutations(l)
        for permutation in permutations:
            yield frozenset(self.__recurse(permutation))


class StrictOrders(object):
    def __init__(self):
        self.lattice = {}

    def __is_not_transitive(self, relation):
        """Return True if relation is not transitive.

        A relation r is not transitive if there is a pair (x,y) in r
        such that for some z, (x,z) and (z,y) are in r but (x,y) is not.

        """
        product = itertools.product(list(relation), list(relation))
        for x in product:
            if x[0][1] == x[1][0]:
                if (x[0][0], x[1][1]) not in list(relation):
                    return True

    def __orders(self, l):
        """Return an iterator over all orders of l.

        An order o in l is calculated as a transitive relation that is a
        subset of a possible strict total order of l.

        """
        torders = list(StrictTotalOrders().orders(l))
        for order in torders:
            pset = Powerset().powerset(list(order))
            for relation in pset:
                if self.__is_not_transitive(relation) != True:
                    yield frozenset(relation)

    def get_orders(self, iterable):
        """Return the lattice of all partial orders of iterable.

        Each partial order is a key into the lattice, and the value
        is a dict containing that order's maxset, upset, and downset.
        """
        l = list(iterable)
        torders = list(StrictTotalOrders().orders(l))
        for s, t in itertools.product(self.__orders(l), self.__orders(l)):
            try:
                self.lattice[s]
            except:
                self.lattice.update({s:{'max':set([]), 'up':set([]), 'down':set([])}})
            if s.issuperset(t):
                self.lattice[s]['down'].add(t)
                if s.issubset(t):
                    self.lattice[s]['up'].add(t)
                    if t in torders:
                        self.lattice[s]['max'].add(t)
            elif s.issubset(t):
                self.lattice[s]['up'].add(t)
                if t in torders:
                    self.lattice[s]['max'].add(t)
        return self.lattice

    def write_to_pickle(self, iterable):
        """Write the lattice of orders of iterable to a pickle."""
        l = list(iterable)
        length = len(l)
        with open('gspace_%scons.p' % length, 'wb') as f:
            pickle.dump(self.get_orders(l), f)
        return 'Orders written.'

