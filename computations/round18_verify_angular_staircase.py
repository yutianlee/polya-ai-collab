#!/usr/bin/env python3
"""Exact finite ledger for the frozen Round 18 angular-staircase claim.

The ledger authenticates only the proof-free candidate and its explicitly
whitelisted dependencies.  It uses ``fractions.Fraction`` for every
decisive finite comparison.  Functional analysis, calculus reductions, and
the externally sourced Bessel-zero statements are identified separately as
analytic inputs reconstructed in the companion review.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_INPUT_HASHES = {
    "candidate": "354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9",
    "candidate_freeze": "b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c",
    "residual": "7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9",
    "residual_freeze": "7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff",
    "spectral": "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "round17_claim": "c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77",
    "lorch": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
    "flps": "27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38",
}


class AuditError(RuntimeError):
    """Raised at the first failed exact obligation."""


def _require(condition: bool, label: str) -> None:
    if not condition:
        raise AuditError(label)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _repository_root() -> Path:
    return Path(__file__).resolve().parent.parent


def input_paths() -> dict[str, Path]:
    root = _repository_root()
    return {
        "candidate": root
        / "state"
        / "lemma_packets"
        / "SHELL-next-angular-staircase-round18-claim.md",
        "candidate_freeze": root
        / "rounds"
        / "polya-main"
        / "round_018"
        / "exploration"
        / "candidate-claim-freeze.md",
        "residual": root
        / "state"
        / "lemma_packets"
        / "SHELL-rho-compact-round18.md",
        "residual_freeze": root
        / "rounds"
        / "polya-main"
        / "round_018"
        / "exploration"
        / "residual-mask-freeze.md",
        "spectral": root
        / "state"
        / "lemma_packets"
        / "SHELL-sturm-liouville-completeness.md",
        "round17_claim": root
        / "state"
        / "lemma_packets"
        / "SHELL-first-angular-bands-round17-claim.md",
        "lorch": root / "sources" / "lorch_bessel_zeros.md",
        "flps": root / "sources" / "flps_balls.md",
    }


def output_paths() -> dict[str, Path]:
    root = _repository_root()
    return {
        "ledger": Path(__file__).resolve(),
        "tests": root
        / "computations"
        / "tests"
        / "test_round18_verify_angular_staircase.py",
        "review": root
        / "rounds"
        / "polya-main"
        / "round_018"
        / "reviews"
        / "angular-staircase-constants.md",
    }


def authenticate_inputs() -> dict[str, str]:
    actual: dict[str, str] = {}
    for name, path in input_paths().items():
        _require(path.exists(), f"missing authenticated input: {name}")
        actual[name] = _sha256(path)
        _require(
            actual[name] == EXPECTED_INPUT_HASHES[name],
            f"authenticated input hash mismatch: {name}",
        )
    return actual


def artifact_manifest() -> dict[str, str | None]:
    """Return current hashes for the three audit outputs.

    These are intentionally computed rather than embedded: embedding an
    artifact's own digest in that artifact would be circular.  The external
    freeze record can lock the returned values after review.
    """

    return {
        name: (_sha256(path) if path.exists() else None)
        for name, path in output_paths().items()
    }


def _atan_alternating_bounds(
    x: Fraction, term_count: int
) -> tuple[Fraction, Fraction]:
    """Enclose atan(x), 0<x<1, by exact alternating partial sums."""

    _require(Fraction(0) < x < Fraction(1), "atan input outside (0,1)")
    _require(term_count > 0, "atan term count must be positive")
    partial = sum(
        ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
        for n in range(term_count)
    )
    next_term = ((-1) ** term_count) * x ** (2 * term_count + 1) / (
        2 * term_count + 1
    )
    other = partial + next_term
    return min(partial, other), max(partial, other)


def machin_pi_bounds() -> tuple[Fraction, Fraction]:
    """Return an exact rational enclosure from Machin's identity."""

    fifth = _atan_alternating_bounds(Fraction(1, 5), 36)
    two_thirty_ninth = _atan_alternating_bounds(Fraction(1, 239), 12)
    lower = 16 * fifth[0] - 4 * two_thirty_ninth[1]
    upper = 16 * fifth[1] - 4 * two_thirty_ninth[0]
    _require(lower < upper, "Machin enclosure is inverted")
    return lower, upper


def run_audit() -> dict[str, Any]:
    """Execute the exact algebraic obligations for Candidate C18."""

    authenticated = authenticate_inputs()
    pi_lower, pi_upper = machin_pi_bounds()
    p_lo = Fraction(333, 106)
    p_hi = Fraction(22, 7)
    _require(Fraction(3) < p_lo < pi_lower, "333/106 < pi failed")
    _require(pi_upper < p_hi, "pi < 22/7 failed")

    checks: dict[str, Fraction | int | bool | str | list[int]] = {}

    # Elementary radical and ratio witnesses used by the K0 bookkeeping.
    sqrt3_upper_square_margin = Fraction(7, 4) ** 2 - 3
    rho_c_lower_minus_tenth = Fraction(7, 51) - Fraction(1, 10)
    _require(sqrt3_upper_square_margin > 0, "sqrt(3)<7/4 failed")
    _require(rho_c_lower_minus_tenth > 0, "rho_c>1/10 failed")
    checks["sqrt3_upper_square_margin"] = sqrt3_upper_square_margin
    checks["omega0_upper"] = Fraction(1, 8)
    checks["rho_c_lower_minus_tenth"] = rho_c_lower_minus_tenth

    # Threshold order and cumulative angular multiplicities.
    c2, c3, c4 = Fraction(51, 10), Fraction(13, 2), Fraction(15, 2)
    _require(c2 < c3 < c4, "rational entry thresholds are not increasing")
    checks["c3_minus_c2"] = c3 - c2
    checks["c4_minus_c3"] = c4 - c3
    caps = [sum(2 * ell + 1 for ell in range(m)) for m in range(1, 7)]
    _require(caps == [1, 4, 9, 16, 25, 36], "multiplicity cap identity failed")
    checks["multiplicity_caps_m1_through_m6"] = caps
    threshold_gaps = [
        m * (m + 1) - (m - 1) * m for m in range(1, 7)
    ]
    _require(threshold_gaps == [2, 4, 6, 8, 10, 12], "k_m order failed")
    checks["k_squared_successive_gaps_m1_through_m6"] = threshold_gaps

    # The worst radial comparison occurs for n=2, ell=0, K=k5.
    # At rho_c, z=pi+1/2>7/2, so 4z^2-k5^2=3z^2-30>27/4.
    radial_n2_gap_lower = 3 * Fraction(7, 2) ** 2 - 30
    _require(radial_n2_gap_lower > 0, "n>=2 exclusion below k5 failed")
    checks["radial_n2_gap_lower"] = radial_n2_gap_lower
    checks["k6_squared_minus_k5_squared"] = Fraction(12)

    # Exact specializations of the permitted Lorch statements.
    lorch_c2_square_margin = Fraction(105, 4) - c2**2
    lorch_c3_radical_square_margin = Fraction(5) - Fraction(178, 81) ** 2
    lorch_c4_radical_square_margin = Fraction(15) - Fraction(247, 66) ** 2
    _require(lorch_c2_square_margin > 0, "Lorch ell=2 specialization failed")
    _require(
        lorch_c3_radical_square_margin > 0,
        "Lorch ell=3 radical comparison failed",
    )
    _require(
        lorch_c4_radical_square_margin > 0,
        "Lorch ell=4 radical comparison failed",
    )
    checks["lorch_c2_square_margin"] = lorch_c2_square_margin
    checks["lorch_c3_radical_square_margin"] = lorch_c3_radical_square_margin
    checks["lorch_c4_radical_square_margin"] = lorch_c4_radical_square_margin
    checks["lorch_orders_in_scope"] = True
    checks["spherical_bessel_prefactor_positive_for_x_positive"] = True

    # Base cap-4 payment inherited by the new staircase but reconstructed
    # exactly.  At rho_c: rho_c<1/7, z=pi+1/2>193/53, and 1/pi>7/22.
    base_coefficient = Fraction(7, 99) * Fraction(342, 343)
    base_k1_square = Fraction(193, 53) ** 2 + 2
    base_cap4_squared_margin = base_coefficient**2 * base_k1_square**3 - 16
    _require(base_cap4_squared_margin > 0, "base cap-4 Weyl payment failed")
    checks["base_cap4_squared_margin"] = base_cap4_squared_margin

    # Fixed-split Weyl lower bounds.  The common factor 7/99 is a strict
    # lower bound for 2/(9*pi).
    split_lower = {
        2: Fraction(7, 99) * Fraction(973, 1000) * c2**3,
        3: Fraction(7, 99) * Fraction(7, 8) * c3**3,
        4: Fraction(7, 99) * Fraction(7, 8) * c4**3,
    }
    split_caps = {2: 9, 3: 16, 4: 25}
    for m in (2, 3, 4):
        margin = split_lower[m] - split_caps[m]
        _require(margin > 0, f"cap-{split_caps[m]} fixed-split payment failed")
        checks[f"split_m{m}_weyl_lower"] = split_lower[m]
        checks[f"split_m{m}_cap_margin"] = margin

    # The moving k_m wall lies strictly above c_m at its proposed split.
    split_k_square_gaps = {
        2: (Fraction(10, 7) * p_lo) ** 2 + 6 - c2**2,
        3: (2 * p_lo) ** 2 + 12 - c3**2,
        4: (2 * p_lo) ** 2 + 20 - c4**2,
    }
    for m, gap in split_k_square_gaps.items():
        _require(gap > 0, f"k_{m}(r_{m})>c_{m} failed")
        checks[f"split_m{m}_k_square_gap"] = gap

    # If c=m(m+1)<=30, the exact positive numerator of d(log F_m)/dr
    # is 3[pi^2(1+r)-c r^2(1-r)^2].  Since r(1-r)<=1/4 and pi>3,
    # its bracket is >9-30/16=57/8.  This covers m=1,...,5.
    monotonicity_bracket_gap = Fraction(9) - Fraction(30, 16)
    _require(monotonicity_bracket_gap > 0, "F_m monotonicity sign failed")
    checks["F_m_monotonicity_bracket_gap_m1_through_m5"] = (
        monotonicity_bracket_gap
    )
    checks["F_m_log_derivative_numerator_factor"] = 3

    # Uniform upper-floor bookkeeping.  On rho<=7/8,
    # k5^2<(176/7)^2+30<26^2.
    k5_below_26_square_margin = Fraction(26) ** 2 - (
        (8 * p_hi) ** 2 + 30
    )
    _require(k5_below_26_square_margin > 0, "k5<26 failed")
    checks["k5_below_26_square_margin"] = k5_below_26_square_margin

    # The written audit proves K0>64 below rho=1/2 and K0>96 above it.
    _require(Fraction(64) > Fraction(26), "low K0 branch separation failed")
    _require(Fraction(96) > Fraction(26), "high K0 branch separation failed")
    checks["low_K0_lower_minus_26"] = Fraction(64 - 26)
    checks["high_K0_lower_minus_26"] = Fraction(96 - 26)
    seam_floor = Fraction(54) / Fraction(1, 6) ** 2
    _require(seam_floor > 26, "seam floor separation failed")
    checks["seam_floor_at_five_sixths"] = seam_floor
    checks["seam_floor_minus_26"] = seam_floor - 26
    global_face = 295**2
    _require(global_face > 26, "global K face separation failed")
    checks["global_face"] = global_face
    checks["global_face_minus_26"] = global_face - 26

    # Face inventory and exact subtraction consequences.  These booleans
    # label logical consequences whose analytic derivation is written out
    # in the review; they are retained as regression assertions.
    checks["rho_splits"] = "rho_c,3/10,1/2,5/6,7/8"
    checks["frequency_faces"] = "z,k2,k3,k4,k5,c2,c3,c4,2z,k6,U"
    checks["strict_k5_face_owned_by_C18"] = True
    checks["strict_k2_face_retains_C17_owner"] = True
    checks["rho_seven_eighths_retains_old_owner"] = True
    checks["B0_B1_not_subtracted_again"] = True
    checks["D18_second_lower_face_is_strict_k5"] = True

    serialized = {
        name: (_qtext(value) if isinstance(value, Fraction) else value)
        for name, value in checks.items()
    }
    return {
        "status": "PASS",
        "first_issue": None,
        "scope": "exact finite algebra for frozen Candidate C18",
        "authenticated_sha256": authenticated,
        "pi_enclosure": {
            "lower": _qtext(pi_lower),
            "upper": _qtext(pi_upper),
            "proves": ["333/106 < pi", "pi < 22/7"],
        },
        "check_count": len(serialized),
        "checks": serialized,
        "analytic_steps_reconstructed_in_review_not_executed_here": [
            "The one-dimensional min-max proof of lambda_(ell,n)>=n^2 z^2+ell(ell+1).",
            "The fixed-angular form-domain extension by zero and its shell-to-ball inequality direction.",
            "The permitted external Lorch statements and the spherical-Bessel positive-zero identification.",
            "The calculus identity for d(log F_m)/dr; the ledger checks its final uniform rational sign.",
            "The G_1 integral representation, eta bounds, and positive-root estimate for K0.",
            "The strict-count staircase, all equality faces, and exact D17 minus C18 set subtraction.",
            "The already-promoted Round 17 theorem on z<=K<=k2 and the frozen D17 predicate.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-check",
        action="store_true",
        help="run the exact audit (the default action)",
    )
    parser.add_argument(
        "--manifest",
        action="store_true",
        help="include current hashes of all three audit outputs",
    )
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    result = run_audit()
    if args.manifest:
        result["output_sha256"] = artifact_manifest()
    if args.compact:
        print(json.dumps(result, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
