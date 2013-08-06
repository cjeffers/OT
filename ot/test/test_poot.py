"""Tests for poot module"""

import cPickle
from nose.tools import raises
from .. import poot
from .. import data


class TestPoOT(object):

    def setUp(self):
        self.p = poot.PoOT(lat_dir='../lattices')
        with open('../lattices/gspace_4cons.p', 'rb') as f:
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

    def test_get_optimal_candidates(self):
        """Gets all and only the optimal candidates?"""
        self.p.dset = data.voweldset
        opt_cands = [('ovea', 'o.ve.a'), ('ovea', 'o.vee'), ('idea', 'i.de.a'),
                     ('lasi-a', 'la.si.a'), ('lasi-a', 'la.sii'),
                     ('rasia', 'ra.si.a')]
        assert self.p.get_optimal_candidates() == opt_cands

    def test_get_nonoptimal_candidates(self):
        """Gets all and only nonoptimal candidates?"""
        self.p.dset = data.voweldset
        non_opt_cands = [('idea', 'i.dee'), ('rasia', 'ra.sii')]
        assert self.p.get_nonoptimal_candidates() == non_opt_cands

    def test_get_hbounded_candidates(self):
        """Gets all and only the harmonically bounded candidates?"""
        self.p.dset = data.hbounded
        hbounded = [(('i1', 'o1'), ('i1', 'o2'))]
        assert self.p.get_harmonically_bounded_candidates() == hbounded

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
        min_grams = set([frozenset([(3, 1), (2, 4)]), frozenset([(3, 1), (2, 1)])])
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

    def test_get_entailments(self):
        """Gets entailments?"""
        self.p.dset = data.voweldset
        ents = {
            frozenset([('ovea', 'o.vee')]): {
                'down': set([
                    frozenset([('lasi-a', 'la.sii')]),
                    frozenset([('idea', 'i.dee')]),
                    frozenset([('rasia', 'ra.sii')]),
                    frozenset([('ovea', 'o.vee')])]),
                'up': set([
                    frozenset([('ovea', 'o.vee')])])},
            frozenset([('rasia', 'ra.si.a')]): {
                'down': set([
                    frozenset([('ovea', 'o.ve.a')]),
                    frozenset([('lasi-a', 'la.si.a')]),
                    frozenset([('rasia', 'ra.si.a')]),
                    frozenset([('idea', 'i.de.a')])]),
                'up': set([frozenset([('rasia', 'ra.si.a')])])},
            frozenset([('idea', 'i.de.a')]): {
                'down': set([
                    frozenset([('ovea', 'o.ve.a')]),
                    frozenset([('idea', 'i.de.a')])]),
                'up': set([
                    frozenset([('rasia', 'ra.si.a')]),
                    frozenset([('idea', 'i.de.a')])])},
            frozenset([('lasi-a', 'la.sii')]): {
                'down': set([
                    frozenset([('lasi-a', 'la.sii')]),
                    frozenset([('rasia', 'ra.sii')])]),
                'up': set([
                    frozenset([('lasi-a', 'la.sii')]),
                    frozenset([('ovea', 'o.vee')])])},
            frozenset([('rasia', 'ra.sii')]): {
                'down': set([
                    frozenset([('rasia', 'ra.sii')])]),
                'up': set([
                    frozenset([('lasi-a', 'la.sii')]),
                    frozenset([('idea', 'i.dee')]),
                    frozenset([('rasia', 'ra.sii')]),
                    frozenset([('ovea', 'o.vee')])])},
            frozenset([('lasi-a', 'la.si.a')]): {
                'down': set([
                    frozenset([('lasi-a', 'la.si.a')]),
                    frozenset([('ovea', 'o.ve.a')])]),
                'up': set([
                    frozenset([('lasi-a', 'la.si.a')]),
                    frozenset([('rasia', 'ra.si.a')])])},
            frozenset([('idea', 'i.dee')]): {
                'down': set([
                    frozenset([('rasia', 'ra.sii')]),
                    frozenset([('idea', 'i.dee')])]),
                'up': set([
                    frozenset([('idea', 'i.dee')]),
                    frozenset([('ovea', 'o.vee')])])},
            frozenset([('ovea', 'o.ve.a')]): {
                'down': set([
                    frozenset([('ovea', 'o.ve.a')])]),
                'up': set([
                    frozenset([('ovea', 'o.ve.a')]),
                    frozenset([('lasi-a', 'la.si.a')]),
                    frozenset([('rasia', 'ra.si.a')]),
                    frozenset([('idea', 'i.de.a')])])}
        }
        assert self.p.get_entailments() == ents

    def check_dset_edge_case(self, dset, grammars):
        """Handles edge cases?"""
        self.p.dset = getattr(data, dset)
        assert self.p.get_grammars(False) == grammars

    def test_dset_edge_cases(self):
        self.setUp()
        gspace = self.lattice[frozenset([])]['up']
        tests = {'all_optimal': set([]), 'all_zeros': gspace,
                 'iequal': gspace}
        for k, v in tests.iteritems():
            yield self.check_dset_edge_case, k, v

    @raises(ValueError)
    def test_no_optimal_candidates(self):
        """Raises ValueError on no optimal candidates?"""
        self.p.dset = data.no_optimal
        self.get_grammars(False)





