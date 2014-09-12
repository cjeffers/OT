"""Perform order and set-theoretic operations.

Powerset -- return the powerset of any iterable
FunctionalSpace -- get the functional space from one iterable to another
StrictTotalOrders -- get the strict total orders for an iterable
StrictOrders -- get the lattices for an iterable

"""
import itertools


class Powerset(object):

    def powerset(self, iterable):
        """Return an iterable of all possible subsets.

        Each subset is represented as a tuple of zero or more elements
        from iterable.

        """
        l = list(iterable)
        return itertools.chain.from_iterable(
            itertools.combinations(l, r) for r in range(len(l)+1)
        )


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
        elif not dom:
            return [[]]
        else:
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
        for permutation in itertools.permutations(l):
            yield frozenset(self.__recurse(permutation))


class StrictOrders(object):
    def __init__(self):
        self.lattice = {}

    def __is_not_transitive(self, relation):
        """Return True if relation is not transitive.

        A relation r is not transitive if there is a pair (x,y) in r
        such that for some z, (x,z) and (z,y) are in r but (x,y) is not.

        """
        relation = list(relation)
        product = itertools.product(relation, relation)
        for x in product:
            if x[0][1] == x[1][0]:
                if (x[0][0], x[1][1]) not in relation:
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
                if not self.__is_not_transitive(relation):  # if transitive
                    yield frozenset(relation)

    def get_orders(self, iterable, verbose=False):
        """Return the lattice of all partial orders of iterable.

        Each partial order is a key into the lattice, and the value
        is a dict containing that order's maxset, upset, and downset.
        """
        if verbose:
            print "getting orders"
        l = list(iterable)
        torders = list(StrictTotalOrders().orders(l))
        all_orders = set(self.__orders(l))
        count = 0
        for s, t in itertools.product(all_orders, all_orders):
            try:
                self.lattice[s]
            except:
                if verbose:
                    count += 1
                    print "inserting #%d (%d total)" % (count, const_info[len(l)]['total_poots'])
                self.lattice.update({s: {'max': set([]),
                                         'up': set([]),
                                         'down': set([])}})
            if s.issuperset(t):
                self.lattice[s]['down'].add(t)
                if s.issubset(t):
                    self.lattice[s]['up'].add(t)
                    if t in torders:
                        self.lattice[s]['max'].add(t)
            if s.issubset(t):
                self.lattice[s]['up'].add(t)
                if t in torders:
                    self.lattice[s]['max'].add(t)
        return self.lattice


const_info = {
    2: {'total_poots': 3, 'total_cots': 2, 'cot_len': 1},
    3: {'total_poots': 19, 'total_cots': 6, 'cot_len': 3},
    4: {'total_poots': 219, 'total_cots': 24, 'cot_len': 6},
    5: {'total_poots': 4231, 'total_cots': 120, 'cot_len': 10},
    6: {'total_poots': 130023, 'total_cots': 720, 'cot_len': 15}
}
