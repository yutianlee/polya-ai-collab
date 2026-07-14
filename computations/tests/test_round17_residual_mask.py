"""Tests for the certified Round 17 analytic-mask point classifier."""

from fractions import Fraction as Q
import unittest

from computations import round17_residual_mask as r17


class ManifestTests(unittest.TestCase):
    def test_manifest_preserves_noncoarse_interfaces(self) -> None:
        manifest = r17._mask_manifest()
        interfaces = set(manifest["interfaces"])
        self.assertIn("rho=omega_0 (small-hole open face)", interfaces)
        self.assertIn(
            "rho=rho_HK, unique H0=K0 switch in (9407/100000,94071/1000000)",
            interfaces,
        )
        self.assertIn("rho=1/(1+2*pi) (lower-wall crossover)", interfaces)
        self.assertIn("rho=1/2 (K0 formula interface)", interfaces)
        self.assertIn("rho=1/16 (coarse only)", interfaces)

    def test_certified_overlay_is_separate(self) -> None:
        manifest = r17._mask_manifest()
        overlay = manifest["certified_overlay"]
        self.assertEqual(overlay["name"], "B0")
        self.assertEqual(overlay["uncovered_formula"], "U16=D16 minus B0")


class ExactFaceTests(unittest.TestCase):
    def test_high_angular_equality_is_covered(self) -> None:
        result = r17.classify_point(Q(1, 16), Q(8))
        self.assertEqual(result.status, "analytic_covered")
        self.assertIn("high-angular", result.analytic_reasons)

    def test_seam_equality_and_below_face(self) -> None:
        below = r17.classify_point(Q(5, 6), Q(1943))
        face = r17.classify_point(Q(5, 6), Q(1944))
        self.assertEqual(below.status, "analytic_residual_uncovered")
        self.assertEqual(face.status, "analytic_covered")
        self.assertIn("central-thin-seam-54", face.analytic_reasons)

    def test_thin_endpoint_owns_every_frequency(self) -> None:
        for k in (Q(0), Q(1), Q(2048), Q(3456), Q(87025)):
            result = r17.classify_point(Q(7, 8), k)
            self.assertEqual(result.status, "analytic_covered")
            self.assertIn("rho-one-endpoint-round16", result.analytic_reasons)

    def test_global_equality_face_is_covered(self) -> None:
        result = r17.classify_point(Q(3, 4), Q(87025))
        self.assertEqual(result.status, "analytic_covered")
        self.assertIn("round16-global-envelope", result.analytic_reasons)


class ExactMaskTests(unittest.TestCase):
    def test_unresolved_lower_interval_gate_is_indeterminate(self) -> None:
        old_precision = r17.ctx.prec
        try:
            r17.ctx.prec = 4096
            omega0 = (
                r17.arb(3).sqrt() / (2 * r17.arb.pi()) - r17.arb("1/6")
            )
            c_star = r17.arb("1/2") + 8 * r17.arb(2).sqrt() / 15
            midpoint = (omega0 / (1 + 2 * c_star)).mid()
            mantissa, exponent = midpoint.man_exp()
            rho = Q(int(mantissa)) * Q(2) ** int(exponent)
        finally:
            r17.ctx.prec = old_precision

        result = r17.classify_point(rho, Q(0))
        self.assertEqual(result.status, "indeterminate")
        self.assertEqual(result.analytic_reasons, ())
        self.assertEqual(result.unresolved_comparisons, ("rho-rho_*",))

    def test_h0_k0_switch_has_certified_rational_bracket(self) -> None:
        left = r17.certified_sign(
            "left", lambda: r17.hk_switch_polynomial_ball(Q(9407, 100000))
        )
        right = r17.certified_sign(
            "right", lambda: r17.hk_switch_polynomial_ball(Q(94071, 1000000))
        )
        left_in_domain = r17.certified_sign(
            "left-rho_*",
            lambda: r17.qball(Q(9407, 100000)) - r17.constants()[3],
        )
        right_in_domain = r17.certified_sign(
            "omega_0-right",
            lambda: r17.constants()[0] - r17.qball(Q(94071, 1000000)),
        )
        self.assertEqual(left.sign, -1)
        self.assertEqual(right.sign, 1)
        self.assertEqual(left_in_domain.sign, 1)
        self.assertEqual(right_in_domain.sign, 1)

    def test_small_hole_branch_continues_above_one_sixteenth(self) -> None:
        # rho=1/10 lies strictly between 1/16 and omega_0.
        result = r17.classify_point(Q(1, 10), Q(140))
        self.assertEqual(result.status, "analytic_covered")
        self.assertIn("small-hole-low-interface", result.analytic_reasons)

    def test_small_hole_fixed_ratio_gap_is_not_overclaimed(self) -> None:
        result = r17.classify_point(Q(1, 10), Q(80))
        self.assertEqual(result.status, "analytic_residual_uncovered")
        self.assertEqual(result.analytic_reasons, ())

    def test_fixed_ratio_branch(self) -> None:
        result = r17.classify_point(Q(1, 10), Q(90))
        self.assertEqual(result.status, "analytic_covered")
        self.assertIn("fixed-rho-high-energy", result.analytic_reasons)

    def test_coarse_switch_is_not_a_mask_cutoff(self) -> None:
        residual = r17.classify_point(Q(1, 16), Q(9))
        covered = r17.classify_point(Q(1, 16), Q(27))
        self.assertEqual(residual.status, "analytic_residual_uncovered")
        self.assertIn("small-hole-low-interface", covered.analytic_reasons)

    def test_round8_box_is_certified_only(self) -> None:
        for rho, k in (
            (Q(999, 2000), Q(67, 10)),
            (Q(1, 2), Q(671, 100)),
            (Q(1001, 2000), Q(168, 25)),
        ):
            result = r17.classify_point(rho, k)
            self.assertEqual(result.status, "certified_only")
            self.assertEqual(result.analytic_reasons, ())
            self.assertEqual(result.certified_reasons, ("round8-certified-pilot-B0",))

    def test_outside_interval_is_not_called_residual(self) -> None:
        result = r17.classify_point(Q(1, 100), Q(1))
        self.assertEqual(result.status, "outside_I16")

    def test_invalid_domain_rejected(self) -> None:
        with self.assertRaises(ValueError):
            r17.classify_point(Q(1, 2), Q(-1))
        with self.assertRaises(ValueError):
            r17.classify_point(Q(0), Q(1))


class SelfCheckTests(unittest.TestCase):
    def test_self_check(self) -> None:
        checks = r17.self_check()
        self.assertEqual(len(checks), 12)


if __name__ == "__main__":
    unittest.main()
