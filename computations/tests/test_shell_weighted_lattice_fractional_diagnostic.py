"""Regression tests for the non-certified weighted shell lattice diagnostic."""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from computations.shell_weighted_lattice_fractional_diagnostic import (  # noqa: E402
    analyze,
    angular_mode_count,
    gamma_exact_float,
    strict_integer_envelope,
)


class ShellWeightedLatticeDiagnosticTests(unittest.TestCase):
    def test_strict_half_integer_cutoff(self) -> None:
        expected = {
            0.49: 0,
            0.5: 0,
            0.500001: 1,
            1.5: 1,
            1.500001: 2,
            20.5: 20,
            20.500001: 21,
        }
        for K, count in expected.items():
            self.assertEqual(angular_mode_count(K), count)

    def test_strict_integer_endpoint(self) -> None:
        self.assertEqual(strict_integer_envelope(1.0), 0)
        self.assertEqual(strict_integer_envelope(1.2), 1)
        self.assertEqual(strict_integer_envelope(2.0), 1)

    def test_half_order_phase_is_shell_width(self) -> None:
        rho = 0.9
        K = 10 * math.pi
        gamma, error = gamma_exact_float(rho, K, ell=0)
        self.assertEqual(error, 0.0)
        self.assertAlmostEqual(gamma, 1.0, places=13)

    def test_thin_width_has_zero_floating_count(self) -> None:
        diagnostic = analyze(0.99, 100.0, compute_actual=True)
        self.assertLess((1 - diagnostic.rho) * diagnostic.K, math.pi)
        self.assertEqual(diagnostic.actual_count, 0)
        self.assertEqual(diagnostic.gf_integer_envelope, 0)

    def test_integerized_and_continuous_surrogates_are_distinct(self) -> None:
        diagnostic = analyze(0.5, 20.0, compute_actual=False)
        self.assertGreater(diagnostic.gf_surrogate_sum, diagnostic.weyl)
        self.assertLess(diagnostic.gf_integer_envelope, diagnostic.weyl)
        self.assertEqual(diagnostic.shifted_tail_violations, 0)
        self.assertIsNotNone(diagnostic.min_inner_tail_margin)

    def test_closed_form_tail_integral_matches_weyl_identity(self) -> None:
        from computations.shell_weighted_lattice_fractional_diagnostic import integral_action_tail

        K = 20.0
        mu = 10.0
        expected = (K * K - mu * mu) / 8.0
        self.assertAlmostEqual(integral_action_tail(K, mu, 0.0), expected, places=12)


if __name__ == "__main__":
    unittest.main()
