"""Targeted tests for the Round 21 aggregate-tail Arb certificate."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VERIFIER_PATH = REPO_ROOT / "computations" / "round21_verify_aggregate_tail.py"
SPEC = importlib.util.spec_from_file_location("round21_verify_aggregate_tail", VERIFIER_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError(f"cannot load verifier from {VERIFIER_PATH}")
verifier = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = verifier
SPEC.loader.exec_module(verifier)


class AggregateTailCertificateTests(unittest.TestCase):
    def test_authenticated_inputs_match(self) -> None:
        observed = verifier.authenticate_inputs(REPO_ROOT)
        self.assertEqual(observed, dict(verifier.EXPECTED_HASHES))

    def test_hash_mismatch_is_rejected(self) -> None:
        bad = dict(verifier.EXPECTED_HASHES)
        route = next(iter(bad))
        bad[route] = "0" * 64
        with self.assertRaises(verifier.VerificationError):
            verifier.authenticate_inputs(REPO_ROOT, bad)

    def test_exact_partition_and_split(self) -> None:
        boxes = verifier.build_boxes()
        self.assertEqual(len(boxes), 1286)
        self.assertEqual(boxes[0].lo, Fraction(7, 51))
        self.assertEqual(boxes[-1].hi, Fraction(39, 50))
        self.assertTrue(all(Fraction(0) < b.width <= Fraction(1, 2000) for b in boxes))
        self.assertTrue(all(a.hi == b.lo for a, b in zip(boxes, boxes[1:])))
        low = [b for b in boxes if b.eta_regime == "rho_le_half"]
        high = [b for b in boxes if b.eta_regime == "rho_ge_half"]
        self.assertEqual((len(low), len(high)), (726, 560))
        self.assertEqual(low[-1].hi, Fraction(1, 2))
        self.assertEqual(high[0].lo, Fraction(1, 2))

    def test_outward_boxes_contain_exact_endpoints(self) -> None:
        verifier.ctx.prec = 192
        boxes = verifier.build_boxes()
        for box in (boxes[0], boxes[725], boxes[726], boxes[-1]):
            enclosure = verifier.arb_box(box)
            self.assertTrue(enclosure.contains(verifier.arb_of_fraction(box.lo)))
            self.assertTrue(enclosure.contains(verifier.arb_of_fraction(box.hi)))

    def test_eta_formulas_agree_at_half(self) -> None:
        verifier.ctx.prec = 192
        rho = verifier.arb_of_fraction(Fraction(1, 2))
        low = verifier.evaluate_at_k0(rho, "rho_le_half")
        high = verifier.evaluate_at_k0(rho, "rho_ge_half")
        self.assertTrue((low["eta"] - high["eta"]).contains(0))

    def test_derivative_reduction_at_both_eta_regimes(self) -> None:
        verifier.ctx.prec = 192
        for value, regime in (
            (Fraction(1, 3), "rho_le_half"),
            (Fraction(2, 3), "rho_ge_half"),
        ):
            quantities = verifier.evaluate_at_k0(
                verifier.arb_of_fraction(value), regime
            )
            self.assertGreater(verifier.arb(200) * quantities["eta"] - 1, 0)
            self.assertLess(quantities["I_KK"], quantities["I_KK_bound"])
            self.assertGreater(quantities["interface_KK"], 0)
            self.assertGreater(quantities["B_KK"], quantities["F"])

    def test_full_192_bit_certificate(self) -> None:
        result = verifier.run_certificate(192, root=REPO_ROOT)
        self.assertEqual(result.box_count, 1286)
        self.assertEqual((result.low_regime_boxes, result.high_regime_boxes), (726, 560))
        # Display-only regression checks; rigorous decisions occurred inside
        # run_certificate through Arb sign comparisons.
        self.assertGreater(result.display_minima["B200"].approximate_lower, 375.4)
        self.assertGreater(result.display_minima["BK200"].approximate_lower, 4.798)
        self.assertGreater(result.display_minima["F"].approximate_lower, 0.02747)

    def test_precision_below_192_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            verifier.run_certificate(191, authenticate=False)


if __name__ == "__main__":
    unittest.main()
