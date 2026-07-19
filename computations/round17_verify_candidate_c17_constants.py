#!/usr/bin/env python3
"""Independent exact constant ledger for the frozen Round 17 claim C17.

This script reads only the frozen claim, residual, and permitted spectral
packets in order to authenticate their bytes.  It does not read an incumbent
proof, a clean-room reconstruction, certification artifacts, or reviews.
All decisive finite comparisons use ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_HASHES = {
    "claim": "c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77",
    "residual": "eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e",
    "spectral": "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
}


class AuditError(RuntimeError):
    """Raised when an exact ledger comparison fails."""


def _require(condition: bool, label: str) -> None:
    if not condition:
        raise AuditError(label)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _atan_alternating_bounds(x: Fraction, term_count: int) -> tuple[Fraction, Fraction]:
    """Enclose atan(x) for 0<x<1 by an alternating rational series."""

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
    """Return independent exact rational bounds from Machin's identity."""

    atan_fifth = _atan_alternating_bounds(Fraction(1, 5), 36)
    atan_239 = _atan_alternating_bounds(Fraction(1, 239), 12)
    lower = 16 * atan_fifth[0] - 4 * atan_239[1]
    upper = 16 * atan_fifth[1] - 4 * atan_239[0]
    _require(lower < upper, "Machin enclosure is inverted")
    return lower, upper


def _packet_paths() -> dict[str, Path]:
    repository_root = Path(__file__).resolve().parent.parent
    return {
        "claim": repository_root
        / "state"
        / "lemma_packets"
        / "SHELL-first-angular-bands-round17-claim.md",
        "residual": repository_root
        / "state"
        / "lemma_packets"
        / "SHELL-rho-compact-round17.md",
        "spectral": repository_root
        / "state"
        / "lemma_packets"
        / "SHELL-sturm-liouville-completeness.md",
    }


def _authenticate_packets() -> dict[str, str]:
    paths = _packet_paths()
    actual: dict[str, str] = {}
    for name, path in paths.items():
        _require(path.exists(), f"missing {name} packet")
        actual[name] = _sha256(path)
        _require(actual[name] == EXPECTED_HASHES[name], f"{name} hash mismatch")
    return actual


def run_audit() -> dict[str, Any]:
    """Execute all finite comparisons needed by the C17 reconstruction."""

    authenticated = _authenticate_packets()
    pi_lower, pi_upper = machin_pi_bounds()

    p_lo = Fraction(333, 106)
    p_hi = Fraction(22, 7)
    _require(Fraction(3) < p_lo < pi_lower, "pi lower rational bound failed")
    _require(pi_upper < p_hi, "pi upper rational bound failed")

    checks: dict[str, Fraction | bool | str] = {}

    # Radical bounds used to remove C0 and rho_* from finite comparisons.
    sqrt2_lower_square_margin = Fraction(2) - Fraction(45, 32) ** 2
    sqrt3_upper_square_margin = Fraction(7, 4) ** 2 - Fraction(3)
    _require(sqrt2_lower_square_margin > 0, "45/32 < sqrt(2) failed")
    _require(sqrt3_upper_square_margin > 0, "sqrt(3) < 7/4 failed")
    checks["sqrt2_lower_square_margin"] = sqrt2_lower_square_margin
    checks["sqrt3_upper_square_margin"] = sqrt3_upper_square_margin
    checks["C0_lower"] = Fraction(7, 4)
    checks["omega0_upper"] = Fraction(1, 8)
    checks["rho_star_upper"] = Fraction(1, 16)

    # Exact order relations for the ratio faces.
    _require(Fraction(1, 16) < Fraction(1, 8), "1/16 < 1/8 failed")
    _require(Fraction(1, 8) < Fraction(7, 51), "1/8 < 7/51 failed")
    _require(Fraction(7, 51) < Fraction(1, 7), "7/51 < 1/7 failed")
    _require(Fraction(1, 7) < Fraction(1, 2), "1/7 < 1/2 failed")
    _require(Fraction(1, 2) < Fraction(5, 6), "1/2 < 5/6 failed")
    _require(Fraction(5, 6) < Fraction(7, 8), "5/6 < 7/8 failed")
    _require(
        Fraction(1, 16) < Fraction(9407, 100000),
        "rho_HK lower locator does not lie right of 1/16",
    )
    _require(
        Fraction(9407, 100000) < Fraction(94071, 1000000),
        "rho_HK locator interval is inverted",
    )
    _require(
        Fraction(94071, 1000000) < Fraction(1, 10),
        "rho_HK locator does not lie left of 1/10",
    )
    checks["rho_c_lower_from_pi_upper"] = Fraction(7, 51)
    checks["rho_c_upper_from_pi_lower"] = Fraction(53, 386)
    checks["rho_HK_upper_below_rho_c"] = True
    checks["ratio_order_chain"] = True

    # The mode-threshold order is z^2 < z^2+2 < z^2+6.  For n>=2,
    # 4z^2-(z^2+6)=3z^2-6>21 because z>pi>3.
    radial_n2_coarse_margin = 3 * Fraction(3) ** 2 - 6
    _require(radial_n2_coarse_margin > 0, "n>=2 exclusion margin failed")
    checks["k1_squared_minus_z_squared"] = Fraction(2)
    checks["k2_squared_minus_k1_squared"] = Fraction(4)
    checks["radial_n2_coarse_margin"] = radial_n2_coarse_margin

    # First Weyl margin.  At rho_c, z=pi+1/2 and
    # W(rho_c,z)-1=(4*pi^2+6*pi-15)/18.  The polynomial is increasing
    # for pi>0, so pi>3 gives the following strict rational lower margin.
    weyl_z_margin_lower = (
        4 * Fraction(3) ** 2 + 6 * Fraction(3) - 15
    ) / 18
    _require(weyl_z_margin_lower > 0, "W(rho_c,z)>1 margin failed")
    checks["weyl_z_minus_one_lower"] = weyl_z_margin_lower

    # Second Weyl margin.  Use rho_c<1/7, pi<22/7, and
    # z(rho_c)=pi+1/2>193/53.  Every factor is positive, so squaring the
    # rational lower bound is reversible.
    k1_square_lower = Fraction(193, 53) ** 2 + 2
    weyl_k1_coefficient_lower = (
        Fraction(2, 1) / (9 * p_hi) * Fraction(342, 343)
    )
    weyl_k1_squared_margin = (
        weyl_k1_coefficient_lower**2 * k1_square_lower**3 - 16
    )
    _require(weyl_k1_squared_margin > 0, "W(rho_c,k1)>4 margin failed")
    checks["weyl_k1_squared_margin"] = weyl_k1_squared_margin

    # Monotonicity reductions.  The derivative of
    # (1+r+r^2)/(1-r)^2 has numerator 3+3r.  For W(r,k1(r)), the sign
    # reduces to z^2(1+r)>2r^2; z^2>9 and 0<=r<1 reduce this to 9>2.
    checks["weyl_z_derivative_constant"] = Fraction(3)
    checks["weyl_z_derivative_linear"] = Fraction(3)
    wk1_monotonic_coarse_margin = Fraction(9) - Fraction(2)
    _require(wk1_monotonic_coarse_margin > 0, "W(k1) monotonicity gap failed")
    checks["weyl_k1_monotonic_coarse_margin"] = wk1_monotonic_coarse_margin

    # C17 subset D16: central K0 branch, rho_c<=rho<=1/2.
    # eta=omega0<1/8 and C0>7/4 imply K0>C0/eta>14, whereas k2<7.
    low_branch_k2_square_margin = Fraction(49) - 4 * p_hi**2 - 6
    _require(low_branch_k2_square_margin > 0, "low-branch k2<7 failed")
    checks["low_branch_K0_lower"] = Fraction(14)
    checks["low_branch_k2_square_margin"] = low_branch_k2_square_margin

    # Central K0 branch, 1/2<=rho<5/6.  eta<=w/2 gives
    # K0>2C0/w.  Compare w*k2=sqrt(pi^2+6w^2) with 2C0, using
    # w<=1/2, pi<22/7, and 2C0>7/2.
    middle_branch_square_margin = Fraction(49, 4) - (
        p_hi**2 + Fraction(3, 2)
    )
    _require(middle_branch_square_margin > 0, "middle-branch k2<K0 failed")
    checks["middle_branch_square_margin"] = middle_branch_square_margin

    # Seam branch, 5/6<=rho<7/8.  With w<=1/6,
    # w*k2=sqrt(pi^2+6w^2)<6 and hence w^2*k2<1<54.
    seam_square_margin = Fraction(36) - (p_hi**2 + Fraction(1, 6))
    _require(seam_square_margin > 0, "seam-branch k2 bound failed")
    checks["seam_square_margin"] = seam_square_margin

    # The candidate lies far below the accepted global K=87025 face.
    # On rho<=7/8, w>=1/8 and k2^2<=(8*pi)^2+6<26^2.
    global_face_square_margin = Fraction(26) ** 2 - ((8 * p_hi) ** 2 + 6)
    _require(global_face_square_margin > 0, "k2<26 global-face bound failed")
    _require(Fraction(26) < Fraction(87025), "26<87025 failed")
    checks["global_face_square_margin"] = global_face_square_margin
    checks["global_face_linear_margin"] = Fraction(87025 - 26)

    # Complete B0 containment.  The worst lower face is
    # (rho,K)=(1001/2000,67/10); the worst upper face is
    # (rho,K)=(999/2000,168/25).
    b0_lower_margin = Fraction(67, 10) - p_hi / Fraction(999, 2000)
    b0_upper_square_margin = (
        (p_lo / Fraction(1001, 2000)) ** 2
        + 6
        - Fraction(168, 25) ** 2
    )
    _require(b0_lower_margin > 0, "B0 strict lower containment failed")
    _require(b0_upper_square_margin > 0, "B0 upper containment failed")
    _require(Fraction(1, 7) < Fraction(999, 2000), "B0 left ratio failed")
    _require(Fraction(1001, 2000) < Fraction(7, 8), "B0 right ratio failed")
    checks["B0_lower_margin"] = b0_lower_margin
    checks["B0_upper_square_margin"] = b0_upper_square_margin
    checks["B0_all_closed_faces_contained"] = True

    # Intended first-method obstruction.  Immediately above k2 the crude
    # product/min-max count cap is 1+3+5=9.  At rho_c, use pi>3,
    # pi<22/7, 1-rho_c^3<1, and k2^2<(51/14)^2+6=3777/196.
    obstruction_k2_square_upper = Fraction(3777, 196)
    obstruction_squared_margin = Fraction(81) - (
        Fraction(2, 27) ** 2 * obstruction_k2_square_upper**3
    )
    _require(obstruction_squared_margin > 0, "W(rho_c,k2)<9 obstruction failed")
    checks["next_band_crude_count"] = Fraction(9)
    checks["obstruction_squared_margin"] = obstruction_squared_margin

    serialized_checks = {
        name: (_qtext(value) if isinstance(value, Fraction) else value)
        for name, value in checks.items()
    }
    return {
        "status": "PASS",
        "first_mismatch": None,
        "authenticated_sha256": authenticated,
        "pi_enclosure": {
            "lower": _qtext(pi_lower),
            "upper": _qtext(pi_upper),
            "proves": ["333/106 < pi", "pi < 22/7"],
        },
        "check_count": len(serialized_checks),
        "checks": serialized_checks,
        "analytic_assumptions_not_proved_by_ledger": [
            "The authenticated separated-spectrum theorem, strict multiplicities, and cross-order direct sum.",
            "The one-dimensional Poincare/min-max eigenvalue bound and the exact ell=0 Dirichlet spectrum.",
            "The frozen residual identity D16={rho_*<rho<7/8, L(rho)<K<U(rho)} and its branch ownership.",
            "The K0 positive-root equation, eta=omega0 for rho<=1/2, and eta<=w/2 for rho>=1/2.",
            "The calculus reductions proving that both Weyl threshold functions increase with rho; the ledger checks their final algebraic signs.",
            "Continuity of the Weyl target, used to turn W(rho_c,k2)<9 into a method obstruction immediately above k2.",
            "Machin's identity and the alternating-series remainder theorem; the ledger independently executes their exact rational consequences.",
            "Positivity conditions that justify the displayed square-root comparisons and reversible squaring; these are checked in the written audit.",
        ],
        "scope_limit": (
            "Finite arithmetic PASS only; this ledger does not prove Candidate C17 "
            "or replace an isolated spectral reconstruction."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    result = run_audit()
    if args.compact:
        print(json.dumps(result, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
