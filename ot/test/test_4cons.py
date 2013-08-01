from poot import PoOT as poot
from data import sample0, voweldset

p = poot()
p.dset = voweldset

if str(p.get_grammars(classical=False)) == 'set([frozenset([(3, 1), (2, 3), (2, 4), (2, 1)]), frozenset([(3, 2), (3, 1), (2, 1)]), frozenset([(3, 1), (2, 4), (2, 1)]), frozenset([(4, 1), (3, 1), (2, 3), (2, 1)]), frozenset([(3, 1), (2, 1)]), frozenset([(3, 1), (4, 1), (2, 1)]), frozenset([(3, 1), (2, 4)]), frozenset([(3, 1), (2, 3), (2, 1)]), frozenset([(3, 1), (4, 1), (2, 4), (2, 1)]), frozenset([(4, 1), (3, 1), (2, 3), (2, 4), (2, 1)]), frozenset([(3, 2), (3, 1), (4, 1), (2, 1)])])':
    print "works for 4 constraints"
