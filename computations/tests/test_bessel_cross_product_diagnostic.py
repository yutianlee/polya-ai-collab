"""Regression tests for the non-certified Bessel diagnostic."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from computations.bessel_cross_product_diagnostic import (  # noqa: E402
    approximate_root_brackets,
    build_report,
    raw_bessel_cross_product,
    scaled_discrepancy,
    small_k_leading_coefficient,
    stabilized_cross_product_as_raw,
    stabilized_riccati_cross_product,
    weighted_count,
)


class BesselCrossProductDiagnosticTests(unittest.TestCase):
    def test_ell_zero_reduces_to_sine_of_shell_width(self) -> None:
        with mp.workdps(80):
            rho = mp.mpf("0.5")
            for k_text in ("0.25", "1", "7", "13.5", "19.9"):
                k = mp.mpf(k_text)
                expected = mp.sin((1 - rho) * k)
                actual = stabilized_riccati_cross_product(0, rho, k)
                self.assertLess(abs(actual - expected), mp.mpf("1e-75"))

    def test_raw_and_recurrence_evaluators_agree(self) -> None:
        with mp.workdps(80):
            rho = mp.mpf("0.5")
            for ell in (0, 1, 2):
                for k_text in ("0.25", "1", "3", "7", "11", "17"):
                    k = mp.mpf(k_text)
                    raw = raw_bessel_cross_product(ell, rho, k)
                    stabilized = stabilized_cross_product_as_raw(ell, rho, k)
                    self.assertLess(scaled_discrepancy(raw, stabilized), mp.mpf("1e-70"))

    def test_small_k_formal_coefficient_matches_numerical_trend(self) -> None:
        with mp.workdps(80):
            rho = mp.mpf("0.5")
            expected = (mp.mpf("0.5"), mp.mpf(7) / 12, mp.mpf(31) / 40)
            k = mp.mpf("1e-8")
            for ell, expected_coefficient in enumerate(expected):
                coefficient = small_k_leading_coefficient(ell, rho)
                self.assertEqual(coefficient, expected_coefficient)
                observed = stabilized_riccati_cross_product(ell, rho, k) / k
                self.assertLess(abs(observed - coefficient), mp.mpf("1e-14"))

    def test_expected_diagnostic_roots_and_weighted_count(self) -> None:
        expected_roots = {
            0: (6.283185307179586, 12.566370614359173, 18.84955592153876),
            1: (6.572013199016351, 12.721356347418017, 18.954392095852507),
            2: (7.111576238144979, 13.026136362650782, 19.162540329609218),
        }
        with mp.workdps(60):
            rho = mp.mpf("0.5")
            brackets_by_ell = {
                ell: approximate_root_brackets(
                    ell,
                    rho=rho,
                    scan_step=mp.mpf("0.05"),
                    target_width=mp.mpf("1e-14"),
                )
                for ell in expected_roots
            }

            self.assertEqual([len(brackets_by_ell[ell]) for ell in expected_roots], [3, 3, 3])
            self.assertEqual(weighted_count(brackets_by_ell), 27)
            for ell, expected_for_ell in expected_roots.items():
                for bracket, expected in zip(brackets_by_ell[ell], expected_for_ell, strict=True):
                    self.assertAlmostEqual(float(bracket.midpoint), expected, places=11)
                    self.assertLessEqual(bracket.width, mp.mpf("1e-14"))
                    left_value = stabilized_riccati_cross_product(ell, rho, bracket.left)
                    right_value = stabilized_riccati_cross_product(ell, rho, bracket.right)
                    self.assertLessEqual(left_value * right_value, 0)

    def test_report_is_explicitly_non_certified(self) -> None:
        report = build_report(scan_step="0.05", target_width="1e-12", dps=50)
        self.assertIn("FLOATING-POINT DIAGNOSTIC — NOT CERTIFIED", report)
        self.assertIn("does not discharge", report)
        self.assertIn("weighted count of `27`", report)
        self.assertIn("not interval or ball values", report)


if __name__ == "__main__":
    unittest.main()
