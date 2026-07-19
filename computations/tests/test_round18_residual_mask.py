"""Tests for the exact post-Round-17 residual classifier."""

from fractions import Fraction as Q
import unittest

from computations import round18_residual_mask as r18


def _dyadic_midpoint(builder) -> Q:
    """Return a >4096-bit dyadic approximation to an irrational face."""

    old_precision = r18.r17.ctx.prec
    try:
        r18.r17.ctx.prec = 4096
        midpoint = builder().mid()
        mantissa, exponent = midpoint.man_exp()
        return Q(int(mantissa)) * Q(2) ** int(exponent)
    finally:
        r18.r17.ctx.prec = old_precision


class ManifestTests(unittest.TestCase):
    def test_manifest_is_derived_from_round17_union(self) -> None:
        manifest = r18._mask_manifest()
        self.assertEqual(
            manifest["derivation"],
            {
                "base_classifier": "computations/round17_residual_mask.py",
                "operation": "A17=A16 union closed_C17",
                "residual_operation": "D17=D16 minus C17",
            },
        )
        self.assertEqual(manifest["analytic_residual"]["rho_c_assignment"], "post_band_piece")

    def test_upper_floor_and_hk_switch_are_explicit(self) -> None:
        upper = r18._mask_manifest()["upper_floor"]
        self.assertIn("H0 on rho_*<rho<rho_HK", upper["piecewise"])
        self.assertIn("K0 on rho_HK<=rho<5/6", upper["piecewise"])
        self.assertIn("(9407/100000,94071/1000000)", upper["rho_HK"])

    def test_certificates_are_regressions_not_subtractions(self) -> None:
        regressions = r18._mask_manifest()["certified_regressions"]
        self.assertEqual(regressions["B0"]["relation"], "B0 subset C17")
        self.assertEqual(regressions["B1"]["relation"], "B1 subset C17")
        self.assertEqual(
            regressions["uncovered_formula"],
            "U17=D17; neither box is subtracted again",
        )

    def test_cap_nine_fact_has_narrow_scope(self) -> None:
        obstruction = r18._mask_manifest()["method_fact"]
        self.assertTrue(obstruction["not_a_counterexample"])
        self.assertIn("only", obstruction["scope"])
        self.assertIn("W(rho_c,k2(rho_c))<9", obstruction["statement"])


class SymbolicFaceTruthTableTests(unittest.TestCase):
    def test_closed_c17_includes_all_equality_faces(self) -> None:
        self.assertIs(
            r18.c17_membership_from_signs(0, 0, 0, rho_le_thin=True),
            True,
        )
        self.assertIs(
            r18.c17_membership_from_signs(1, 1, 1, rho_le_thin=False),
            False,
        )

    def test_new_c17_excludes_old_lower_and_endpoint_faces(self) -> None:
        self.assertIs(
            r18.new_c17_membership_from_signs(0, 0, 0, rho_lt_thin=True),
            False,
        )
        self.assertIs(
            r18.new_c17_membership_from_signs(0, 1, 0, rho_lt_thin=False),
            False,
        )
        self.assertIs(
            r18.new_c17_membership_from_signs(0, 1, 0, rho_lt_thin=True),
            True,
        )

    def test_false_factor_overrides_irrelevant_unresolved_sign(self) -> None:
        self.assertIs(
            r18.c17_membership_from_signs(-1, None, None, rho_le_thin=True),
            False,
        )
        self.assertIs(
            r18.c17_membership_from_signs(1, None, 1, rho_le_thin=True),
            None,
        )

    def test_every_d17_boundary_is_strict(self) -> None:
        # rho=rho_*, K=U, lower K=1/(2rho), and K=k2 are all excluded.
        self.assertIs(r18.d17_piece_from_signs(0, 1, -1, 1, 1, rho_lt_thin=True), False)
        self.assertIs(r18.d17_piece_from_signs(1, 0, -1, 1, 1, rho_lt_thin=True), False)
        self.assertIs(r18.d17_piece_from_signs(1, 1, -1, 0, 1, rho_lt_thin=True), False)
        self.assertIs(r18.d17_piece_from_signs(1, 1, 0, 1, 0, rho_lt_thin=True), False)
        self.assertIs(r18.d17_piece_from_signs(1, 1, 1, 1, -1, rho_lt_thin=False), False)

    def test_rho_c_equality_uses_post_k2_piece(self) -> None:
        self.assertIs(r18.d17_piece_from_signs(1, 1, 0, 1, -1, rho_lt_thin=True), True)
        self.assertIs(r18.d17_piece_from_signs(1, 1, 0, 1, 0, rho_lt_thin=True), False)


class ClassifierFaceTests(unittest.TestCase):
    def test_two_exact_residual_pieces(self) -> None:
        lower = r18.classify_point(Q(7, 51), Q(4))
        upper = r18.classify_point(Q(11, 80), Q(5))
        self.assertEqual((lower.status, lower.residual_piece), ("analytic_residual_uncovered", "lower-ratio"))
        self.assertEqual((upper.status, upper.residual_piece), ("analytic_residual_uncovered", "post-k2"))

    def test_promoted_band_and_inherited_lower_face(self) -> None:
        band = r18.classify_point(Q(11, 80), Q(4))
        old_face = r18.classify_point(Q(1, 16), Q(8))
        self.assertEqual(band.status, "analytic_covered")
        self.assertIn("first-angular-band-round17", band.analytic_reasons)
        self.assertEqual(old_face.status, "analytic_covered")
        self.assertIn("high-angular", old_face.analytic_reasons)

    def test_thin_endpoint_owns_all_sampled_frequencies(self) -> None:
        for k in (Q(0), Q(1), Q(20), Q(1944), Q(87025)):
            result = r18.classify_point(Q(7, 8), k)
            self.assertEqual(result.status, "analytic_covered")
            self.assertIn("rho-one-endpoint-round16", result.analytic_reasons)

    def test_upper_floor_branches_and_inclusive_seam_owner(self) -> None:
        h0 = r18.upper_floor_decision(Q(9, 100), Q(1))
        k0 = r18.upper_floor_decision(Q(1, 10), Q(1))
        half = r18.upper_floor_decision(Q(1, 2), Q(1))
        below = r18.upper_floor_decision(Q(5, 6), Q(1943))
        face = r18.upper_floor_decision(Q(5, 6), Q(1944))
        self.assertEqual((h0.piece, h0.membership), ("H0", True))
        self.assertEqual((k0.piece, k0.membership), ("K0", True))
        self.assertEqual((half.piece, half.membership), ("K0", True))
        self.assertEqual((below.piece, below.membership), ("seam-54", True))
        self.assertEqual((face.piece, face.membership), ("seam-54", False))

    def test_hk_polynomial_bracket_is_retained(self) -> None:
        left = r18.r17.certified_sign(
            "left", lambda: r18.r17.hk_switch_polynomial_ball(Q(9407, 100000))
        )
        right = r18.r17.certified_sign(
            "right", lambda: r18.r17.hk_switch_polynomial_ball(Q(94071, 1000000))
        )
        self.assertEqual((left.sign, right.sign), (-1, 1))

    def test_B0_every_corner_is_analytic_and_certified(self) -> None:
        for rho in (r18.B0_RHO_LO, r18.B0_RHO_HI):
            for k in (r18.B0_K_LO, r18.B0_K_HI):
                result = r18.classify_point(rho, k)
                self.assertEqual(result.status, "analytic_covered")
                self.assertIn("first-angular-band-round17", result.analytic_reasons)
                self.assertIn("round8-certified-pilot-B0", result.certified_regression_reasons)

    def test_B1_every_corner_is_analytic_and_certified(self) -> None:
        for rho in (r18.B1_RHO_LO, r18.B1_RHO_HI):
            for k in (r18.B1_K_LO, r18.B1_K_HI):
                result = r18.classify_point(rho, k)
                self.assertEqual(result.status, "analytic_covered")
                self.assertIn("first-angular-band-round17", result.analytic_reasons)
                self.assertIn("round17-certified-pilot-B1", result.certified_regression_reasons)

    def test_outside_interval_and_invalid_domains(self) -> None:
        self.assertEqual(r18.classify_point(Q(1, 100), Q(1)).status, "outside_I17")
        with self.assertRaises(ValueError):
            r18.classify_point(Q(1, 2), Q(-1))
        with self.assertRaises(ValueError):
            r18.classify_point(Q(0), Q(1))


class IntervalIndeterminacyTests(unittest.TestCase):
    def test_unresolved_mandatory_rho_star_gate_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(lambda: r18.r17.constants()[3])
        result = r18.classify_point(rho, Q(0))
        self.assertEqual(result.status, "indeterminate")
        self.assertEqual(result.analytic_reasons, ())
        self.assertIn("rho-rho_*", result.unresolved_comparisons)

    def test_unresolved_rho_c_assignment_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(lambda: 1 / (1 + 2 * r18.r17.arb.pi()))
        result = r18.classify_point(rho, Q(5))
        self.assertEqual(result.status, "indeterminate")
        self.assertIn("rho(1+2*pi)-1", result.unresolved_comparisons)

    def test_unresolved_z_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: 2 * r18.r17.arb.pi())
        result = r18.classify_point(Q(1, 2), k)
        self.assertEqual(result.status, "indeterminate")
        self.assertTrue(
            {"pi-(1-rho)K", "(1-rho)K-pi"}
            & set(result.unresolved_comparisons)
        )

    def test_unresolved_k2_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r18.r17.arb.pi()) ** 2 + 6).sqrt()
        )
        result = r18.classify_point(Q(1, 2), k)
        self.assertEqual(result.status, "indeterminate")
        self.assertIn("pi^2+(6-K^2)(1-rho)^2", result.unresolved_comparisons)

    def test_unresolved_k0_upper_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: r18.r17.k0_ball(Q(1, 2)))
        result = r18.classify_point(Q(1, 2), k)
        self.assertEqual(result.status, "indeterminate")
        self.assertTrue(
            {"K-K_0(rho)", "K_0(rho)-K"}
            & set(result.unresolved_comparisons)
        )


class ConsistencyTests(unittest.TestCase):
    def test_complement_and_normalized_form_agree_on_cell_inventory(self) -> None:
        points = (
            (Q(1, 16), Q(9)),
            (Q(9, 100), Q(6)),
            (Q(1, 10), Q(80)),
            (Q(1, 8), Q(5)),
            (Q(7, 51), Q(4)),
            (Q(11, 80), Q(5)),
            (Q(1, 2), Q(7)),
            (Q(3, 4), Q(13)),
            (Q(5, 6), Q(20)),
            (Q(6, 7), Q(23)),
        )
        for rho, k in points:
            with self.subTest(rho=rho, k=k):
                result = r18.classify_point(rho, k)
                direct = r18.normalized_d17_decision(rho, k)
                self.assertEqual(result.status, "analytic_residual_uncovered")
                self.assertIs(direct.membership, True)
                self.assertEqual(result.residual_piece, direct.piece)

    def test_self_check(self) -> None:
        self.assertEqual(len(r18.self_check()), 12)


if __name__ == "__main__":
    unittest.main()
