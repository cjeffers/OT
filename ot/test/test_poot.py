"""Tests for poot module"""

import cPickle
import os.path

from nose.tools import raises, assert_raises, ok_
from ot import poot
from ot import data

LAT_DIR = "lattices"


class TestPoOT(object):

    def setUp(self):
        self.p = poot.PoOT(lat_dir=LAT_DIR)
        with open(os.path.join(LAT_DIR, 'gspace_4cons.p'), 'rb') as f:
            self.lattice = cPickle.load(f)

    def test_lattice_setter(self):
        """PoOT lattice setter work?"""
        self.p.lattice = data.voweldset
        # go find privately stored lattice inside Lattice object
        assert self.p._lattice._lattice == self.lattice

    def test_dset_setter(self):
        """PoOT dset setter work?"""
        self.p.dset = data.voweldset
        assert self.p.dset == data.voweldset
        # go find privately stored lattice inside Lattice object
        assert self.p._lattice._lattice == self.lattice

    def test_lattice_setter_tuple(self):
        """PoOT dset setter work with tuples?"""
        self.p.dset = (data.voweldset, 'poop')
        assert self.p.dset == data.voweldset

    def test_apriori_setter(self):
        self.p.dset = data.voweldset
        self.p.get_grammars(classical=False)
        assert self.p.apriori == frozenset([])
        assert self.p._grammardset is not None
        assert self.p._compatible_cots is not None
        assert self.p._compatible_poots is not None

        self.p.apriori = frozenset([])
        assert self.p.apriori == frozenset([])
        assert self.p._grammardset is not None
        assert self.p._compatible_cots is not None
        assert self.p._compatible_poots is not None

        self.p.apriori = frozenset([(1, 2)])
        assert self.p.apriori == frozenset([(1, 2)])
        assert self.p._grammardset is None
        assert self.p._compatible_cots is None
        assert self.p._compatible_poots is None

    def test_apriori_setter_bad_values(self):
        bad_values = [
            'poop',
            frozenset([(1, 2, 3)]),
            frozenset([(1, 2), 1]),
            frozenset([(1, 2), ('a', 2)]),
            frozenset([(1, 2), (2, 'a')])
        ]
        for value in bad_values:
            yield self.check_apriori_setter_bad_value, value

    def check_apriori_setter_bad_value(self, value):
        with assert_raises(ValueError) as ex:
            self.p.apriori = value
        ok_(ex.exception.message == ("A priori ranking must be a frozenset of "
                                     "length-two tuples"),
            "We get the right exception")

    def test_get_optimal_candidates(self):
        """Gets all and only the optimal candidates?"""
        self.p.dset = data.voweldset
        opt_cands = set([
            ('ovea', 'o-ve-a'), ('ovea', 'o-vee'), ('idea', 'i-de-a'),
            ('lasi-a', 'la-si-a'), ('lasi-a', 'la-sii'),
            ('rasia', 'ra-si-a')
        ])
        assert set(self.p.get_optimal_candidates()) == opt_cands

    def test_get_nonoptimal_candidates(self):
        """Gets all and only nonoptimal candidates?"""
        self.p.dset = data.voweldset
        non_opt_cands = set([('idea', 'i-dee'), ('rasia', 'ra-sii')])
        assert set(self.p.get_nonoptimal_candidates()) == non_opt_cands

    def test_get_hbounded_candidates(self):
        """Gets all and only the harmonically bounded candidates?"""
        self.p.dset = data.hbounded
        hbounded = [('i1', 'o2')]
        assert self.p.get_harmonically_bounded_candidates() == hbounded

    def test_hbounded_optimal_has_no_grammars(self):
        """Hbounded candidates marked optimal --> no grammars?"""
        self.p.dset = data.hbounded_optimal
        grams = self.p.get_grammars(classical=False)
        assert len(grams) == 0

    def test_get_poot_grammars(self):
        """Gets all the right PoOT grammars?"""
        self.p.dset = data.voweldset
        grammars = set([
            frozenset([(3, 1), (2, 1)]),
            frozenset([(3, 1), (2, 4)]),
            frozenset([(3, 2), (3, 1), (2, 1)]),
            frozenset([(3, 1), (2, 4), (2, 1)]),
            frozenset([(3, 1), (4, 1), (2, 1)]),
            frozenset([(3, 1), (2, 3), (2, 1)]),
            frozenset([(3, 1), (2, 3), (2, 4), (2, 1)]),
            frozenset([(4, 1), (3, 1), (2, 3), (2, 1)]),
            frozenset([(3, 1), (4, 1), (2, 4), (2, 1)]),
            frozenset([(3, 2), (3, 1), (4, 1), (2, 1)]),
            frozenset([(4, 1), (3, 1), (2, 3), (2, 4), (2, 1)])
        ])
        assert self.p.get_grammars(classical=False) == grammars

    def test_get_poot_grammars_with_apriori(self):
        """Gets PoOT grammars, filtered by an apriori ranking?"""
        p = poot.PoOT(lat_dir=LAT_DIR, apriori=frozenset([(2, 4)]))
        p.dset = data.voweldset
        grammars = set([
            frozenset([(3, 1), (2, 4)]),
            frozenset([(3, 1), (2, 4), (2, 1)]),
            frozenset([(3, 1), (2, 3), (2, 4), (2, 1)]),
            frozenset([(3, 1), (4, 1), (2, 4), (2, 1)]),
            frozenset([(4, 1), (3, 1), (2, 3), (2, 4), (2, 1)])
        ])
        assert p.get_grammars(classical=False) == grammars

    def check_get_big_cot_grammars(self, set_n):
        p = poot.PoOT(lat_dir=LAT_DIR)
        p.dset = getattr(data, "trivial_cot_%d" % set_n)
        grams = p.get_grammars(classical=True)
        assert len(grams) == 1
        gram = grams.pop()
        assert len(gram) == sum(range(set_n))

    def test_get_big_cot_grammars(self):
        for n in range(7, 9):
            yield self.check_get_big_cot_grammars, n

    @raises(poot.TooManyConstraintsForPartialGrammars)
    def test_big_grammar_fails_poot(self):
        self.p.dset = data.trivial_cot_8
        self.p.get_grammars(classical=False)

    def test_get_cot_grammars(self):
        """Gets all the right COT grammars?"""
        self.p.dset = data.hbounded
        cot_grammars = set([
            frozenset([(3, 1), (2, 1), (2, 3), (4, 3), (4, 2), (4, 1)]),
            frozenset([(3, 2), (3, 1), (2, 1), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 3), (4, 2)]),
            frozenset([(1, 3), (2, 1), (2, 3), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (3, 4), (3, 1), (4, 2), (4, 1)]),
            frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (4, 3), (4, 2)]),
            frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (4, 2), (3, 4)]),
            frozenset([(3, 2), (3, 4), (3, 1), (2, 1), (4, 1), (2, 4)]),
            frozenset([(4, 1), (3, 1), (2, 1), (2, 3), (3, 4), (2, 4)]),
            frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (2, 4)]),
            frozenset([(1, 3), (2, 1), (2, 3), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 2), (3, 2), (3, 1), (4, 3), (4, 2), (4, 1)]),
            frozenset([(3, 1), (2, 1), (2, 3), (4, 3), (4, 1), (2, 4)]),
            frozenset([(3, 2), (3, 4), (3, 1), (2, 1), (4, 2), (4, 1)]),
            frozenset([(1, 2), (1, 3), (1, 4), (2, 3), (4, 3), (2, 4)]),
            frozenset([(1, 2), (1, 3), (2, 3), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 3), (2, 1), (2, 3), (1, 4), (4, 3), (2, 4)]),
            frozenset([(3, 2), (3, 1), (2, 1), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 3), (2, 1), (2, 3), (4, 3), (4, 1), (2, 4)]),
            frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (3, 4), (2, 4)]),
            frozenset([(3, 1), (2, 1), (2, 3), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 2), (3, 2), (1, 3), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 2), (3, 4)])
        ])
        assert cot_grammars == self.p.get_grammars()

    def test_get_cot_grammars_with_apriori(self):
        """Gets COT grammars compatible with apriori?"""
        p = poot.PoOT(lat_dir=LAT_DIR, apriori=frozenset([(1, 2), (3, 2)]))
        p.dset = data.hbounded
        cot_grammars = set([
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 3), (4, 2)]),
            frozenset([(1, 2), (3, 2), (3, 4), (3, 1), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (4, 2), (3, 4)]),
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 2), (3, 2), (3, 1), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (3, 1), (1, 4), (3, 4), (2, 4)]),
            frozenset([(1, 2), (3, 2), (1, 3), (4, 3), (4, 2), (4, 1)]),
            frozenset([(1, 2), (3, 2), (1, 3), (1, 4), (4, 2), (3, 4)])
        ])
        assert cot_grammars == p.get_grammars()

    def test_no_opt_gives_no_grammars(self):
        """No optimal candidates gives no grammars?"""
        self.p.dset = data.no_rankings
        assert self.p.get_grammars() == set([])

    def test_is_compatible_cot_grammar(self):
        """Can check for COT compatibility?"""
        self.p.dset = data.hbounded
        yes = frozenset([(3, 2), (3, 4), (3, 1), (2, 1), (4, 2), (4, 1)])
        no = frozenset([(3, 1), (4, 1), (2, 4), (2, 1)])
        assert self.p.is_compatible_COT_grammar(yes)
        assert not self.p.is_compatible_COT_grammar(no)

    def test_is_compatible_poot_grammar(self):
        """Can check for PoOT compatibility?"""
        self.p.dset = data.voweldset
        yes = frozenset([(3, 2), (3, 1), (2, 1)])
        no = frozenset([(1, 2), (1, 3), (2, 3)])
        assert self.p.is_compatible_PoOT_grammar(yes)
        assert not self.p.is_compatible_PoOT_grammar(no)

    def test_is_min_grammar(self):
        """Can check for a grammars minimality?"""
        self.p.dset = data.voweldset
        yes = frozenset([(3, 1), (2, 1)])
        no = frozenset([(3, 1), (2, 3), (2, 4), (2, 1)])
        assert self.p.is_min_grammar(yes)
        assert not self.p.is_min_grammar(no)

    def test_poot_min(self):
        """Gets min grammars?"""
        self.p.dset = data.voweldset
        min_grams = set([frozenset([(3, 1), (2, 4)]),
                         frozenset([(3, 1), (2, 1)])])
        assert self.p.min(self.p.get_grammars(False)) == min_grams

    def test_is_max_grammar(self):
        """Can check for a grammars maximality?"""
        self.p.dset = data.voweldset
        yes = frozenset([(4, 1), (3, 1), (2, 3), (2, 4), (2, 1)])
        no = frozenset([(3, 1), (2, 1), (2, 4)])
        assert self.p.is_max_grammar(yes)
        assert not self.p.is_max_grammar(no)

    def test_poot_max(self):
        """Gets max grammars?"""
        self.p.dset = data.voweldset
        max_grams = set([frozenset([(4, 1), (3, 1), (2, 3), (2, 4), (2, 1)]),
                         frozenset([(3, 2), (3, 1), (4, 1), (2, 1)])])
        assert self.p.max(self.p.get_grammars(False)) == max_grams

    def test_get_hbounded_entailments(self):
        self.p.dset = data.hbounded
        ents = {
            frozenset([('i1', 'o1')]): {
                'up': set([
                    frozenset([('i1', 'o1')])]),
                'down': set([
                    frozenset([('i1', 'o1')]),
                    frozenset([('i1', 'o2')])])},
            frozenset([('i1', 'o2')]): {
                'up': set([
                    frozenset([('i1', 'o2')]),
                    frozenset([('i1', 'o1')])]),
                'down': set([
                    frozenset([('i1', 'o2')])])
            }
        }
        assert ents == self.p.get_entailments()

    def test_get_entailments(self):
        """Gets entailments?"""
        self.p.dset = data.voweldset
        ents = {
            frozenset([('ovea', 'o-vee')]): {
                'down': set([
                    frozenset([('lasi-a', 'la-sii')]),
                    frozenset([('idea', 'i-dee')]),
                    frozenset([('rasia', 'ra-sii')]),
                    frozenset([('ovea', 'o-vee')])]),
                'up': set([
                    frozenset([('ovea', 'o-vee')])])},
            frozenset([('rasia', 'ra-si-a')]): {
                'down': set([
                    frozenset([('ovea', 'o-ve-a')]),
                    frozenset([('lasi-a', 'la-si-a')]),
                    frozenset([('rasia', 'ra-si-a')]),
                    frozenset([('idea', 'i-de-a')])]),
                'up': set([frozenset([('rasia', 'ra-si-a')])])},
            frozenset([('idea', 'i-de-a')]): {
                'down': set([
                    frozenset([('ovea', 'o-ve-a')]),
                    frozenset([('idea', 'i-de-a')])]),
                'up': set([
                    frozenset([('rasia', 'ra-si-a')]),
                    frozenset([('idea', 'i-de-a')])])},
            frozenset([('lasi-a', 'la-sii')]): {
                'down': set([
                    frozenset([('lasi-a', 'la-sii')]),
                    frozenset([('rasia', 'ra-sii')])]),
                'up': set([
                    frozenset([('lasi-a', 'la-sii')]),
                    frozenset([('ovea', 'o-vee')])])},
            frozenset([('rasia', 'ra-sii')]): {
                'down': set([
                    frozenset([('rasia', 'ra-sii')])]),
                'up': set([
                    frozenset([('lasi-a', 'la-sii')]),
                    frozenset([('idea', 'i-dee')]),
                    frozenset([('rasia', 'ra-sii')]),
                    frozenset([('ovea', 'o-vee')])])},
            frozenset([('lasi-a', 'la-si-a')]): {
                'down': set([
                    frozenset([('lasi-a', 'la-si-a')]),
                    frozenset([('ovea', 'o-ve-a')])]),
                'up': set([
                    frozenset([('lasi-a', 'la-si-a')]),
                    frozenset([('rasia', 'ra-si-a')])])},
            frozenset([('idea', 'i-dee')]): {
                'down': set([
                    frozenset([('rasia', 'ra-sii')]),
                    frozenset([('idea', 'i-dee')])]),
                'up': set([
                    frozenset([('idea', 'i-dee')]),
                    frozenset([('ovea', 'o-vee')])])},
            frozenset([('ovea', 'o-ve-a')]): {
                'down': set([
                    frozenset([('ovea', 'o-ve-a')])]),
                'up': set([
                    frozenset([('ovea', 'o-ve-a')]),
                    frozenset([('lasi-a', 'la-si-a')]),
                    frozenset([('rasia', 'ra-si-a')]),
                    frozenset([('idea', 'i-de-a')])])}
        }
        assert self.p.get_entailments() == ents

    def test_entailments_with_apriori(self):
        self.p.dset = data.apriori_entailments
        p = poot.PoOT(lat_dir=LAT_DIR, apriori=frozenset([(2, 1)]))
        p.dset = data.apriori_entailments
        ents = self.p.get_entailments()
        apriori = frozenset([(2, 1)])
        apriori_ents = {
            frozenset([('i1', 'o2')]): {
                'down': set([frozenset([('i1', 'o2')]),
                             frozenset([('i2', 'o4')]),
                             frozenset([('i2', 'o3')]),
                             frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i1', 'o2')])])
            },
            frozenset([('i2', 'o4')]): {
                'down': set([frozenset([('i2', 'o4')]),
                             frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i1', 'o2')]),
                           frozenset([('i2', 'o4')])])
            },
            frozenset([('i2', 'o3')]): {
                'down': set([frozenset([('i2', 'o3')]),
                             frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i1', 'o2')]),
                           frozenset([('i2', 'o3')])])
            },
            frozenset([('i1', 'o1')]): {
                'down': set([frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i1', 'o2')]),
                           frozenset([('i2', 'o4')]),
                           frozenset([('i2', 'o3')]),
                           frozenset([('i1', 'o1')])])
            }
        }
        ents = {
            frozenset([('i1', 'o2')]): {
                'down': set([frozenset([('i1', 'o2')]),
                             frozenset([('i2', 'o3')])]),
                'up': set([frozenset([('i1', 'o2')])])
            },
            frozenset([('i2', 'o4')]): {
                'down': set([frozenset([('i2', 'o4')]),
                             frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i2', 'o4')])])
            },
            frozenset([('i2', 'o3')]): {
                'down': set([frozenset([('i2', 'o3')])]),
                'up': set([frozenset([('i1', 'o2')]),
                           frozenset([('i2', 'o3')])])
            },
            frozenset([('i1', 'o1')]): {
                'down': set([frozenset([('i1', 'o1')])]),
                'up': set([frozenset([('i2', 'o4')]),
                           frozenset([('i1', 'o1')])])
            }
        }
        assert self.p.get_entailments() == ents
        assert p.get_entailments() == apriori_ents
        assert self.p.get_entailments(apriori=apriori) == apriori_ents

    def test_get_non_atomic_entailments(self):
        with open('non_atomic_vowel_entails.pkl', 'rb') as f:
            ents = cPickle.load(f)
        self.p.dset = data.voweldset
        assert self.p.get_entailments(atomic=False) == ents

    def check_edge_case(self, dset, grammars, classical):
        self.p.dset = getattr(data, dset)
        assert self.p.get_grammars(classical) == grammars

    def get_all_or_none_edge_cases(self, classical):
        if classical:
            gspace = self.lattice[frozenset([])]['max']
        else:
            gspace = self.lattice[frozenset([])]['up']
        return {
            'c0y_c1y_iy_dy': gspace,
            'c0y_c1y_in_dy': gspace,
            'c0y_c1n_iy_dy': set([]),
            'c0n_c1y_iy_dy': set([]),
            'c0y_c1n_in_dy': set([]),
            'c0n_c1y_in_dy': set([]),
            'c0y_c1y_iy_dn': gspace,
            'c0y_c1n_iy_dn': set([]),
            'c0n_c1y_iy_dn': set([])
        }

    def test_poot_edge_cases(self):
        self.setUp()
        assert self.lattice
        for k, v in self.get_all_or_none_edge_cases(False).iteritems():
            yield self.check_edge_case, k, v, False

    def test_cot_edge_cases(self):
        self.setUp()
        for k, v in self.get_all_or_none_edge_cases(True).iteritems():
            yield self.check_edge_case, k, v, True

    @raises(ValueError)
    def check_error_cases(self, dset, classical):
        self.p.dset = getattr(data, dset)
        self.p.get_grammars(classical)

    def test_error_cases(self):
        dsets = ['c0n_c1n_in_dn', 'c0n_c1n_in_dy',
                 'c0n_c1n_iy_dn', 'c0n_c1n_iy_dy']
        types = [True, False]
        cases = [(d, t) for d in dsets for t in types]
        for c in cases:
            yield self.check_error_cases, c[0], c[1]

    def check_single_opt_cand(self, gspace, classical):
        self.p.dset = data.single_opt_cand
        assert self.p.get_grammars(classical) == gspace

    def test_single_optimal_candidates(self):
        self.setUp()
        for b in (True, False):
            if b:
                gspace = self.lattice[frozenset([])]['max']
            else:
                gspace = self.lattice[frozenset([])]['up']
            yield self.check_single_opt_cand, gspace, b

    @raises(ValueError)
    def check_single_non_opt_cand(self, classical):
        self.p.dset = data.single_non_opt_cand
        self.p.get_grammars(classical)

    def test_single_non_opt_cand(self):
        for b in (True, False):
            yield self.check_single_non_opt_cand, b


class TestStats(object):

    def setUp(self):
        ots1 = poot.OTStats(LAT_DIR)
        ots1.dset = data.voweldset
        ots2 = poot.OTStats(LAT_DIR)
        ots2.dset = data.three_const

        self.ots1 = ots1
        self.ots2 = ots2

    def test_num_poots(self):
        assert(self.ots1.num_compatible_poots() == 11)
        assert(self.ots2.num_compatible_poots() == 19)
        assert(self.ots1.num_total_poots() == 219)
        assert(self.ots2.num_total_poots() == 19)

    def test_num_cots(self):
        assert(self.ots1.num_compatible_cots() == 0)
        assert(self.ots2.num_compatible_cots() == 6)
        assert(self.ots1.num_total_cots() == 24)
        assert(self.ots2.num_total_cots() == 6)

    def test_num_cots_by_cand(self):
        num_by_cand = self.ots1.num_cots_by_cand()
        assert(num_by_cand[('ovea', 'o-ve-a')] == 8)
        assert(num_by_cand[('ovea', 'o-vee')] == 16)
        assert(num_by_cand[('rasia', 'ra-sii')] == 8)
        assert(num_by_cand[('lasi-a', 'la-si-a')] == 12)
        assert(num_by_cand[('idea', 'i-de-a')] == 12)
        assert(num_by_cand[('idea', 'i-dee')] == 12)
        assert(num_by_cand[('rasia', 'ra-si-a')] == 16)
        assert(num_by_cand[('lasi-a', 'la-sii')] == 12)

    def test_num_cots_by_cand_hbounded(self):
        self.ots1.dset = data.hbounded
        num_by_cand = self.ots1.num_cots_by_cand()
        assert(num_by_cand[('i1', 'o1')] == 24)
        assert(num_by_cand[('i1', 'o2')] == 0)

    def test_num_cots_by_cand_by_grammar(self):
        grams = sorted(list(self.ots1.get_grammars(False)))
        guess = [self.ots1.num_cots_by_cand(gram) for gram in grams]
        check = [
            {('rasia', 'ra-si-a'): 8, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 5, ('idea', 'i-de-a'): 8,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 3,
             ('ovea', 'o-ve-a'): 4, ('ovea', 'o-vee'): 4},
            {('rasia', 'ra-si-a'): 6, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 5, ('idea', 'i-de-a'): 6,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 5, ('ovea', 'o-vee'): 1},
            {('rasia', 'ra-si-a'): 3, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 2, ('idea', 'i-de-a'): 3,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 2, ('ovea', 'o-vee'): 1},
            {('rasia', 'ra-si-a'): 4, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 3, ('idea', 'i-de-a'): 4,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 2, ('ovea', 'o-vee'): 2},
            {('rasia', 'ra-si-a'): 5, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 4, ('idea', 'i-de-a'): 5,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 4, ('ovea', 'o-vee'): 1},
            {('rasia', 'ra-si-a'): 6, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 3, ('idea', 'i-de-a'): 6,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 3,
             ('ovea', 'o-ve-a'): 2, ('ovea', 'o-vee'): 4},
            {('rasia', 'ra-si-a'): 4, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 2, ('idea', 'i-de-a'): 4,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 2,
             ('ovea', 'o-ve-a'): 2, ('ovea', 'o-vee'): 2},
            {('rasia', 'ra-si-a'): 3, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 1, ('idea', 'i-de-a'): 3,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 2,
             ('ovea', 'o-ve-a'): 1, ('ovea', 'o-vee'): 2},
            {('rasia', 'ra-si-a'): 3, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 2, ('idea', 'i-de-a'): 3,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 2, ('ovea', 'o-vee'): 1},
            {('rasia', 'ra-si-a'): 2, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 1, ('idea', 'i-de-a'): 2,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 1, ('ovea', 'o-vee'): 1},
            {('rasia', 'ra-si-a'): 3, ('rasia', 'ra-sii'): 0,
             ('lasi-a', 'la-si-a'): 2, ('idea', 'i-de-a'): 3,
             ('idea', 'i-dee'): 0, ('lasi-a', 'la-sii'): 1,
             ('ovea', 'o-ve-a'): 1, ('ovea', 'o-vee'): 2}
        ]
        for g, c in zip(guess, check):
            assert(g == c)
