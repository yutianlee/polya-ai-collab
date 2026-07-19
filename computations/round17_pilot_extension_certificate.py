#!/usr/bin/env python3
"""Produce the single Round 17 face-connected pilot extension certificate.

The target is the closed box

    B1 = [999/2000, 1001/2000] x [168/25, 673/100].

It meets the retained Round 8 box only on the complete face
``K = 168/25``.  This producer uses Arb ball arithmetic through the frozen
Round 8 Riccati--spherical backend.  The separate Round 17 checker uses exact
``Fraction`` arithmetic and imports neither this module nor python-flint.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

try:  # Support both repository imports and direct script execution.
    from computations import round8_compact_box_certificate as round8
except ModuleNotFoundError:  # pragma: no cover - direct CLI path
    import round8_compact_box_certificate as round8


SCHEMA = "polya-shell-round17-pilot-extension-v0.1"
PRECISION_BITS = 256

RHO_LO = Fraction(999, 2000)
RHO_HI = Fraction(1001, 2000)
K_LO = Fraction(168, 25)
K_HI = Fraction(673, 100)

B0_RHO_LO = Fraction(999, 2000)
B0_RHO_HI = Fraction(1001, 2000)
B0_K_LO = Fraction(67, 10)
B0_K_HI = Fraction(168, 25)

ROOT_BRACKETS = {
    0: (Fraction(31, 5), Fraction(63, 10)),
    1: (Fraction(13, 2), Fraction(33, 5)),
}


def _qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _qball(value: Fraction) -> arb:
    return arb(_qtext(value))


def _closed_ball(lower: Fraction, upper: Fraction) -> arb:
    if lower > upper:
        raise ValueError("lower endpoint exceeds upper endpoint")
    return _qball(lower).union(_qball(upper))


def _ball_record(value: arb) -> dict[str, Any]:
    midpoint, radius, exponent = value.mid_rad_10exp()
    return {
        "arb": value.str(90, radius=True, more=True),
        "mid_rad_10exp": {
            "midpoint_integer": str(midpoint),
            "radius_integer": str(radius),
            "decimal_exponent": int(exponent),
        },
    }


def _signed_record(value: arb) -> dict[str, Any]:
    if value > 0:
        sign = "positive"
    elif value < 0:
        sign = "negative"
    else:
        sign = "contains_zero"
    return {"sign": sign, "enclosure": _ball_record(value)}


def _require_sign(value: arb, sign: str, label: str) -> None:
    if sign == "positive" and not value > 0:
        raise RuntimeError(f"{label} is not strictly positive: {value}")
    if sign == "negative" and not value < 0:
        raise RuntimeError(f"{label} is not strictly negative: {value}")


def build_certificate() -> dict[str, Any]:
    """Build and internally sanity-check the unique Round 17 pilot box."""

    ctx.prec = PRECISION_BITS
    rho = _closed_ball(RHO_LO, RHO_HI)
    k_box = _closed_ball(K_LO, K_HI)
    pi = arb.pi()

    channels: list[dict[str, Any]] = []
    for ell, (root_lower, root_upper) in ROOT_BRACKETS.items():
        lower_value = round8.shell_determinant(ell, rho, _qball(root_lower))
        upper_value = round8.shell_determinant(ell, rho, _qball(root_upper))
        target_value = round8.shell_determinant(ell, rho, k_box)
        _require_sign(lower_value, "positive", f"ell={ell} root lower face")
        _require_sign(upper_value, "negative", f"ell={ell} root upper face")
        _require_sign(target_value, "negative", f"ell={ell} target box")
        channels.append(
            {
                "ell": ell,
                "multiplicity": 2 * ell + 1,
                "uniform_root_bracket": [
                    _qtext(root_lower),
                    _qtext(root_upper),
                ],
                "root_count_below_every_K_in_box": 1,
                "determinant_lower_face": _signed_record(lower_value),
                "determinant_upper_face": _signed_record(upper_value),
                "determinant_on_target_box": _signed_record(target_value),
            }
        )

    width_max = _qball(1 - RHO_LO)
    ell_two_margin = (pi / width_max) ** 2 + 6 - _qball(K_HI) ** 2
    second_radial_margin = (2 * pi / width_max) ** 2 - _qball(K_HI) ** 2
    _require_sign(ell_two_margin, "positive", "ell>=2 Sturm exclusion")
    _require_sign(second_radial_margin, "positive", "n>=2 Sturm exclusion")

    lower_residual_margin = _qball((1 - RHO_HI) * K_LO) - pi
    upper_residual_proxy_margin = (
        8 * pi * _qball(RHO_LO) / _qball(1 - RHO_LO) - _qball(K_HI)
    )
    _require_sign(lower_residual_margin, "positive", "strict lower residual margin")
    _require_sign(
        upper_residual_proxy_margin,
        "positive",
        "strict K0 lower-proxy margin",
    )

    weyl_lower = (
        2
        * (1 - _qball(RHO_HI) ** 3)
        * _qball(K_LO) ** 3
        / (9 * pi)
    )
    weyl_margin = weyl_lower - 4
    _require_sign(weyl_margin, "positive", "strict Weyl margin")

    producer_path = Path(__file__).resolve()
    computations_dir = producer_path.parent
    repository_root = computations_dir.parent
    paths = {
        "producer": producer_path,
        "independent_checker": computations_dir
        / "round17_verify_pilot_extension_certificate.py",
        "arb_backend_helper": computations_dir
        / "round8_compact_box_certificate.py",
        "fraction_checker_helper": computations_dir
        / "round8_verify_compact_box_certificate.py",
        "frozen_round17_packet": repository_root
        / "state"
        / "lemma_packets"
        / "SHELL-rho-compact-round17.md",
        "freeze_record": repository_root
        / "rounds"
        / "polya-main"
        / "round_017"
        / "exploration"
        / "residual-mask-freeze.md",
        "parent_B0_certificate": repository_root
        / "rounds"
        / "polya-main"
        / "round_008"
        / "certification"
        / "pilot-central-box.json",
        "parent_B0_check": repository_root
        / "rounds"
        / "polya-main"
        / "round_008"
        / "certification"
        / "pilot-central-box-check.json",
    }
    missing = [name for name, path in paths.items() if not path.exists()]
    if missing:
        raise RuntimeError(f"missing provenance inputs: {', '.join(missing)}")

    return {
        "schema": SCHEMA,
        "status": "certified_extension_when_independent_checker_returns_PASS",
        "claim": (
            "For every rho in [999/2000,1001/2000] and K in "
            "[168/25,673/100], the strict Dirichlet shell count is 4 and is "
            "strictly smaller than (2/(9*pi))*(1-rho^3)*K^3."
        ),
        "scope": {
            "rho": [_qtext(RHO_LO), _qtext(RHO_HI)],
            "K": [_qtext(K_LO), _qtext(K_HI)],
            "closed_faces": True,
            "residual": "D_16",
        },
        "parent_box": {
            "id": "B0",
            "rho": [_qtext(B0_RHO_LO), _qtext(B0_RHO_HI)],
            "K": [_qtext(B0_K_LO), _qtext(B0_K_HI)],
            "assigned_shared_face": "K=168/25",
            "intersection": (
                "[999/2000,1001/2000] x {168/25}; complete closed upper "
                "face of B0 and lower face of B1"
            ),
        },
        "arithmetic": {
            "producer": "python-flint Arb through frozen Round 8 Riccati backend",
            "precision_bits": PRECISION_BITS,
            "input_convention": "exact rational endpoints; closed Arb hull",
            "output_convention": "parseable outward Arb ball plus mid_rad_10exp",
        },
        "provenance": {
            "sha256": {name: _sha256(path) for name, path in paths.items()},
            "frozen_packet_expected_sha256": (
                "eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e"
            ),
        },
        "residual_membership": {
            "analytic_basis": (
                "Frozen packet equation (9): rho_*<rho<7/8 and "
                "pi/(1-rho)<K<K0(rho) on this ratio box"
            ),
            "ratio_cell": "rho_c<rho<5/6, including the K0 formula interface rho=1/2",
            "strict_lower_margin": _signed_record(lower_residual_margin),
            "strict_upper_proxy_margin": _signed_record(
                upper_residual_proxy_margin
            ),
            "upper_proxy_justification": (
                "K0(rho)>8*pi*rho/(1-rho) on rho>rho_c, from eta_rho<1/2"
            ),
            "conclusion": "the complete closed B1 lies strictly inside D_16",
        },
        "sturm_bounds": {
            "formula": (
                "lambda_(n,ell) >= (n*pi/(1-rho))^2 + ell*(ell+1)"
            ),
            "first_ell_two_minus_K_squared": _signed_record(ell_two_margin),
            "second_ell_zero_minus_K_squared": _signed_record(
                second_radial_margin
            ),
            "conclusion": (
                "ell>=2 contributes no roots; ell=0,1 have at most one root"
            ),
        },
        "channels": channels,
        "strict_count": {
            "weighted_count": 4,
            "calculation": "1*(ell=0 root) + 3*(ell=1 root) = 4",
            "spectral_wall_in_target_box": False,
        },
        "weyl": {
            "true_worst_corner": {
                "rho": _qtext(RHO_HI),
                "K": _qtext(K_LO),
            },
            "right_hand_side_lower": _ball_record(weyl_lower),
            "right_hand_side_minus_strict_count": _signed_record(weyl_margin),
        },
        "boundary_policy": {
            "all_B1_faces_included": True,
            "B0_overlap_is_exactly_assigned_complete_face": True,
            "root_brackets_end_strictly_below_B1": True,
            "one_new_box_only": True,
        },
        "proof_dependencies": [
            "frozen Round 17 residual equation (9) and its K0 lower bound",
            "d=3 shell determinant zero criterion and multiplicity 2*ell+1",
            "positive radial roots are simple and complete",
            "strict spectral counting convention",
            "Dirichlet Poincare-Sturm lower bound",
        ],
        "limitations": [
            "This certifies one face-connected box only, not D_16 or U_16.",
            "It does not promote COMP-certified-bessel or any analytic theorem.",
            "The independent checker is required; producer signs alone are insufficient.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
