import unittest
from .. import ordertheory

class OrderTheoryTests(unittest.TestCase):

    def test_powerset(self):
        """Powerset calculate ok?"""
        test_pset = set([(), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4),
                         (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4),
                         (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)])

        pset = list(ordertheory.Powerset().powerset([1,2,3,4]))

        for elem in pset:
            msg = "%s from generated set not in test powerset" % str(elem)
            self.assertTrue(elem in test_pset, msg)

        for elem in test_pset:
            msg = "%s from test powerset not in generated set" % str(elem)
            self.assertTrue(elem in pset, msg)


    def test_functional_space(self):
        """Functional space calculated correctly?"""
        test_fspace = [[(1, 6), (2, 4), (3, 5)], [(1, 6), (2, 5), (3, 4)],
                       [(1, 4), (2, 6), (3, 4)], [(1, 4), (2, 5), (3, 4)],
                       [(1, 4), (2, 4), (3, 4)], [(1, 6), (2, 5), (3, 6)],
                       [(1, 5), (2, 6), (3, 4)], [(1, 4), (2, 6), (3, 5)],
                       [(1, 5), (2, 5), (3, 4)], [(1, 5), (2, 6), (3, 6)],
                       [(1, 5), (2, 4), (3, 6)], [(1, 4), (2, 5), (3, 6)],
                       [(1, 5), (2, 6), (3, 5)], [(1, 5), (2, 5), (3, 5)],
                       [(1, 4), (2, 6), (3, 6)], [(1, 6), (2, 4), (3, 6)],
                       [(1, 6), (2, 5), (3, 5)], [(1, 6), (2, 6), (3, 4)],
                       [(1, 5), (2, 4), (3, 5)], [(1, 4), (2, 5), (3, 5)],
                       [(1, 5), (2, 5), (3, 6)], [(1, 6), (2, 6), (3, 5)],
                       [(1, 5), (2, 4), (3, 4)], [(1, 6), (2, 6), (3, 6)],
                       [(1, 6), (2, 4), (3, 4)], [(1, 4), (2, 4), (3, 5)],
                       [(1, 4), (2, 4), (3, 6)]]

        fspace = ordertheory.FunctionalSpace().funcs([1, 2, 3], [4, 5, 6])
        msg = "functional space from [1,2,3] into [4,5,6] doesn't match"
        self.assertEqual(fspace, test_fspace, msg)


    def test_strict_total_orders(self):
        """Strict total orders calculated ok?"""
        test_orders = [frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (2, 4)]),
                       frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (4, 3), (2, 4)]),
                       frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (3, 4), (2, 4)]),
                       frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 2), (3, 4)]),
                       frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (4, 3), (4, 2)]),
                       frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 3), (4, 2)]),
                       frozenset([(1, 3), (2, 1), (2, 3), (1, 4), (3, 4), (2, 4)]),
                       frozenset([(1, 3), (2, 1), (2, 3), (1, 4), (4, 3), (2, 4)]),
                       frozenset([(3, 1), (2, 1), (2, 3), (1, 4), (3, 4), (2, 4)]),
                       frozenset([(4, 1), (3, 1), (2, 1), (2, 3), (3, 4), (2, 4)]),
                       frozenset([(1, 3), (2, 1), (2, 3), (4, 3), (4, 1), (2, 4)]),
                       frozenset([(3, 1), (2, 1), (2, 3), (4, 3), (4, 1), (2, 4)]),
                       frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (3, 4), (2, 4)]),
                       frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (4, 2), (3, 4)]),
                       frozenset([(3, 2), (3, 1), (2, 1), (1, 4), (3, 4), (2, 4)]),
                       frozenset([(3, 2), (3, 4), (3, 1), (2, 1), (4, 1), (2, 4)]),
                       frozenset([(1, 2), (3, 2), (3, 4), (3, 1), (4, 2), (4, 1)]),
                       frozenset([(3, 2), (3, 4), (3, 1), (2, 1), (4, 2), (4, 1)]),
                       frozenset([(1, 2), (1, 3), (2, 3), (4, 3), (4, 2), (4, 1)]),
                       frozenset([(1, 2), (3, 2), (1, 3), (4, 3), (4, 2), (4, 1)]),
                       frozenset([(1, 3), (2, 1), (2, 3), (4, 3), (4, 2), (4, 1)]),
                       frozenset([(3, 1), (2, 1), (2, 3), (4, 3), (4, 2), (4, 1)]),
                       frozenset([(1, 2), (3, 2), (3, 1), (4, 3), (4, 2), (4, 1)]),
                       frozenset([(3, 2), (3, 1), (2, 1), (4, 3), (4, 2), (4, 1)])]
        orders = list(ordertheory.StrictTotalOrders().orders([1,2,3,4]))
        msg = "strict total orders for [1,2,3,4] don't match"
        self.assertEqual(orders, test_orders, msg)


    def test_strict_orders(self):
        """Lattices generate ok? (3-constraint)"""
        test_lat = {
            frozenset([(1, 3), (2, 3)]): {
                'down': set([frozenset([(1, 3), (2, 3)]), frozenset([(2, 3)]),
                            frozenset([]), frozenset([(1, 3)])]),
                'max': set([frozenset([(1, 3), (2, 3), (2, 1)]),
                            frozenset([(1, 2), (1, 3), (2, 3)])]),
                'up': set([frozenset([(1, 3), (2, 3)]),
                        frozenset([(1, 2), (1, 3), (2, 3)]),
                        frozenset([(1, 3), (2, 3), (2, 1)])])},
            frozenset([(2, 3)]): {
                'down': set([frozenset([(2, 3)]), frozenset([])]),
                'max': set([frozenset([(1, 3), (2, 3), (2, 1)]),
                            frozenset([(1, 2), (1, 3), (2, 3)]),
                            frozenset([(3, 1), (2, 3), (2, 1)])]),
                'up': set([frozenset([(1, 3), (2, 3)]), frozenset([(2, 3)]),
                           frozenset([(1, 3), (2, 3), (2, 1)]),
                           frozenset([(3, 1), (2, 3), (2, 1)]),
                           frozenset([(1, 2), (1, 3), (2, 3)]),
                           frozenset([(2, 3), (2, 1)])])},
            frozenset([(3, 2), (3, 1)]): {
                'down': set([frozenset([(3, 2)]), frozenset([(3, 2), (3, 1)]),
                             frozenset([]), frozenset([(3, 1)])]),
                'max': set([frozenset([(1, 2), (3, 2), (3, 1)]),
                            frozenset([(3, 2), (3, 1), (2, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (3, 1)]),
                           frozenset([(3, 2), (3, 1)]),
                           frozenset([(3, 2), (3, 1), (2, 1)])])},
            frozenset([(1, 3)]): {
                'down': set([frozenset([]), frozenset([(1, 3)])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(1, 2), (1, 3), (2, 3)]),
                            frozenset([(1, 3), (2, 3), (2, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(1, 3)]), frozenset([(1, 3), (2, 3)]),
                           frozenset([(1, 3), (2, 3), (2, 1)]),
                           frozenset([(1, 2), (1, 3), (2, 3)]),
                           frozenset([(1, 2), (1, 3)])])},
            frozenset([(1, 2)]): {
                'down': set([frozenset([]), frozenset([(1, 2)])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(1, 2), (1, 3), (2, 3)]),
                            frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(1, 2)]),
                           frozenset([(1, 2), (1, 3), (2, 3)]),
                           frozenset([(1, 2), (3, 2)]),
                           frozenset([(1, 2), (3, 2), (3, 1)]),
                           frozenset([(1, 2), (1, 3)])])},
            frozenset([(1, 2), (3, 2), (1, 3)]): {
                'down': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                             frozenset([(1, 3)]), frozenset([(1, 2)]),
                             frozenset([]), frozenset([(1, 2), (3, 2)]),
                             frozenset([(3, 2)]), frozenset([(1, 2), (1, 3)])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)])])},
            frozenset([(2, 3), (2, 1)]): {
                'down': set([frozenset([(2, 1)]), frozenset([(2, 3), (2, 1)]),
                             frozenset([(2, 3)]), frozenset([])]),
                'max': set([frozenset([(1, 3), (2, 3), (2, 1)]),
                            frozenset([(3, 1), (2, 3), (2, 1)])]),
                'up': set([frozenset([(1, 3), (2, 3), (2, 1)]),
                           frozenset([(2, 3), (2, 1)]),
                           frozenset([(3, 1), (2, 3), (2, 1)])])},
            frozenset([(3, 1), (2, 1)]): {
                'down': set([frozenset([(2, 1)]), frozenset([]),
                             frozenset([(3, 1)]), frozenset([(3, 1), (2, 1)])]),
                'max': set([frozenset([(3, 1), (2, 3), (2, 1)]),
                            frozenset([(3, 2), (3, 1), (2, 1)])]),
                'up': set([frozenset([(3, 1), (2, 3), (2, 1)]),
                           frozenset([(3, 2), (3, 1), (2, 1)]),
                           frozenset([(3, 1), (2, 1)])])},
            frozenset([]): {
                'down': set([frozenset([])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(3, 2), (3, 1), (2, 1)]),
                            frozenset([(1, 3), (2, 3), (2, 1)]),
                            frozenset([(3, 1), (2, 3), (2, 1)]),
                            frozenset([(1, 2), (1, 3), (2, 3)]),
                            frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(1, 3), (2, 3)]), frozenset([(2, 3)]),
                           frozenset([(3, 2), (3, 1)]), frozenset([(1, 3)]),
                           frozenset([(1, 2)]),
                           frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(2, 3), (2, 1)]),
                           frozenset([(3, 1), (2, 1)]), frozenset([]),
                           frozenset([(3, 1)]), frozenset([(2, 1)]),
                           frozenset([(3, 1), (2, 3), (2, 1)]),
                           frozenset([(1, 2), (1, 3), (2, 3)]),
                           frozenset([(1, 2), (3, 2)]),
                           frozenset([(1, 3), (2, 3), (2, 1)]),
                           frozenset([(1, 2), (3, 2), (3, 1)]),
                           frozenset([(3, 2)]), frozenset([(1, 2), (1, 3)]),
                           frozenset([(3, 2), (3, 1), (2, 1)])])},
            frozenset([(3, 1)]): {
                'down': set([frozenset([]), frozenset([(3, 1)])]),
                'max': set([frozenset([(3, 1), (2, 3), (2, 1)]),
                            frozenset([(3, 2), (3, 1), (2, 1)]),
                            frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(3, 2), (3, 1), (2, 1)]),
                           frozenset([(3, 1), (2, 1)]),
                           frozenset([(3, 2), (3, 1)]), frozenset([(3, 1)]),
                           frozenset([(3, 1), (2, 3), (2, 1)]),
                           frozenset([(1, 2), (3, 2), (3, 1)])])},
            frozenset([(2, 1)]): {
                'down': set([frozenset([(2, 1)]), frozenset([])]),
                'max': set([frozenset([(1, 3), (2, 3), (2, 1)]),
                            frozenset([(3, 2), (3, 1), (2, 1)]),
                            frozenset([(3, 1), (2, 3), (2, 1)])]),
                'up': set([frozenset([(3, 2), (3, 1), (2, 1)]),
                           frozenset([(3, 1), (2, 1)]),
                           frozenset([(1, 3), (2, 3), (2, 1)]),
                           frozenset([(2, 1)]),
                           frozenset([(3, 1), (2, 3), (2, 1)]),
                           frozenset([(2, 3), (2, 1)])])},
            frozenset([(3, 1), (2, 3), (2, 1)]): {
                'down': set([frozenset([(2, 3)]), frozenset([(3, 1), (2, 1)]),
                             frozenset([]), frozenset([(3, 1)]),
                             frozenset([(2, 1)]),
                             frozenset([(3, 1), (2, 3), (2, 1)]),
                             frozenset([(2, 3), (2, 1)])]),
                'max': set([frozenset([(3, 1), (2, 3), (2, 1)])]),
                'up': set([frozenset([(3, 1), (2, 3), (2, 1)])])},
            frozenset([(1, 2), (1, 3), (2, 3)]): {
                'down': set([frozenset([(1, 3), (2, 3)]), frozenset([(2, 3)]),
                             frozenset([(1, 3)]), frozenset([(1, 2)]),
                             frozenset([]),
                             frozenset([(1, 2), (1, 3), (2, 3)]),
                             frozenset([(1, 2), (1, 3)])]),
                'max': set([frozenset([(1, 2), (1, 3), (2, 3)])]),
                'up': set([frozenset([(1, 2), (1, 3), (2, 3)])])},
            frozenset([(1, 2), (3, 2)]): {
                'down': set([frozenset([(3, 2)]), frozenset([(1, 2), (3, 2)]),
                             frozenset([]), frozenset([(1, 2)])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(1, 2), (3, 2)]),
                           frozenset([(1, 2), (3, 2), (3, 1)])])},
            frozenset([(1, 3), (2, 3), (2, 1)]): {
                'down': set([frozenset([(1, 3), (2, 3)]),
                             frozenset([(2, 3)]), frozenset([(1, 3)]),
                             frozenset([(1, 3), (2, 3), (2, 1)]),
                             frozenset([]), frozenset([(2, 1)]),
                             frozenset([(2, 3), (2, 1)])]),
                'max': set([frozenset([(1, 3), (2, 3), (2, 1)])]),
                'up': set([frozenset([(1, 3), (2, 3), (2, 1)])])},
            frozenset([(1, 2), (3, 2), (3, 1)]): {
                'down': set([frozenset([(1, 2)]), frozenset([(3, 2), (3, 1)]),
                             frozenset([]), frozenset([(3, 1)]),
                             frozenset([(1, 2), (3, 2)]),
                             frozenset([(1, 2), (3, 2), (3, 1)]),
                             frozenset([(3, 2)])]),
                'max': set([frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (3, 1)])])},
            frozenset([(3, 2)]): {
                'down': set([frozenset([(3, 2)]), frozenset([])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(3, 2), (3, 1), (2, 1)]),
                            frozenset([(1, 2), (3, 2), (3, 1)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(3, 2), (3, 1), (2, 1)]),
                           frozenset([(3, 2), (3, 1)]),
                           frozenset([(1, 2), (3, 2)]),
                           frozenset([(1, 2), (3, 2), (3, 1)]),
                           frozenset([(3, 2)])])},
            frozenset([(1, 2), (1, 3)]): {
                'down': set([frozenset([]), frozenset([(1, 3)]),
                             frozenset([(1, 2)]), frozenset([(1, 2), (1, 3)])]),
                'max': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                            frozenset([(1, 2), (1, 3), (2, 3)])]),
                'up': set([frozenset([(1, 2), (3, 2), (1, 3)]),
                           frozenset([(1, 2), (1, 3), (2, 3)]),
                           frozenset([(1, 2), (1, 3)])])},
            frozenset([(3, 2), (3, 1), (2, 1)]): {
                'down': set([frozenset([(3, 2), (3, 1), (2, 1)]),
                             frozenset([(3, 1), (2, 1)]),
                             frozenset([(3, 2), (3, 1)]), frozenset([]),
                             frozenset([(3, 1)]), frozenset([(2, 1)]),
                             frozenset([(3, 2)])]),
                'max': set([frozenset([(3, 2), (3, 1), (2, 1)])]),
                'up': set([frozenset([(3, 2), (3, 1), (2, 1)])])}
        }
        lat = ordertheory.StrictOrders().get_orders([1,2,3])
        for k in lat.keys():
            msg = "Sets for %s in 3-constraint lattice don't match" % str(k)
            self.assertEqual(lat[k], test_lat[k], msg)


if __name__ == '__main__':
    unittest.main()
