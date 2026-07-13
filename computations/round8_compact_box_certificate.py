#!/usr/bin/env python3
"""Produce a narrow Arb certificate for one Round 8 central residual box.

This is deliberately not a cover of ``R_L union R_C union R_T``.  It proves
one closed two-parameter box only:

    999/2000 <= rho <= 1001/2000,
    67/10     <= K   <= 168/25.

The box lies in ``R_C``.  Half-integer Bessel functions are evaluated through
the elementary Riccati--spherical recurrence, so every transcendental
operation is performed by Arb ball arithmetic.  A separate checker in
``round8_verify_compact_box_certificate.py`` reconstructs the signs and the
Weyl margin with rational Taylor bounds and does not import this module.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

try:
    import flint
    from flint import arb, ctx
except ImportError as exc:  # pragma: no cover - exercised by the CLI message
    raise SystemExit(
        "python-flint is required; install computations/requirements-round8-certified.txt"
    ) from exc


SCHEMA = "polya-shell-compact-box-certificate-v0.1"
PRECISION_BITS = 256

RHO_LO = Fraction(999, 2000)
RHO_HI = Fraction(1001, 2000)
K_LO = Fraction(67, 10)
K_HI = Fraction(168, 25)

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
    """Return an Arb ball containing the exact rational closed interval."""

    if lower > upper:
        raise ValueError("lower endpoint exceeds upper endpoint")
    return _qball(lower).union(_qball(upper))


def _ball_record(value: arb) -> dict[str, Any]:
    """Serialize a parseable outward ball and Arb's decimal integer triple."""

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


def riccati_spherical_pair(ell: int, z: arb) -> tuple[arb, arb]:
    """Return ``(z*j_ell(z), z*y_ell(z))`` using an Arb recurrence."""

    if ell < 0:
        raise ValueError("ell must be nonnegative")
    if not (z > 0):
        raise ValueError("the complete input ball must be positive")

    sin_z, cos_z = z.sin_cos()
    psi_previous = sin_z
    eta_previous = -cos_z
    if ell == 0:
        return psi_previous, eta_previous

    psi_current = sin_z / z - cos_z
    eta_current = -cos_z / z - sin_z
    if ell == 1:
        return psi_current, eta_current

    for order in range(1, ell):
        coefficient = (2 * order + 1) / z
        psi_next = coefficient * psi_current - psi_previous
        eta_next = coefficient * eta_current - eta_previous
        psi_previous, psi_current = psi_current, psi_next
        eta_previous, eta_current = eta_current, eta_next
    return psi_current, eta_current


def shell_determinant(ell: int, rho: arb, k: arb) -> arb:
    """Evaluate the root-equivalent Riccati shell determinant with Arb."""

    inner_psi, inner_eta = riccati_spherical_pair(ell, rho * k)
    outer_psi, outer_eta = riccati_spherical_pair(ell, k)
    return inner_psi * outer_eta - outer_psi * inner_eta


def _require_sign(value: arb, expected: str, label: str) -> None:
    actual = _signed_record(value)["sign"]
    if actual != expected:
        raise ArithmeticError(f"{label}: expected {expected}, obtained {actual}: {value}")


def build_certificate() -> dict[str, Any]:
    """Build and internally sanity-check the deterministic pilot certificate."""

    ctx.prec = PRECISION_BITS
    rho = _closed_ball(RHO_LO, RHO_HI)
    k_box = _closed_ball(K_LO, K_HI)

    channel_records: list[dict[str, Any]] = []
    expected_face_signs = {
        0: ("positive", "negative"),
        1: ("positive", "negative"),
    }
    for ell, (root_lower, root_upper) in ROOT_BRACKETS.items():
        lower_value = shell_determinant(ell, rho, _qball(root_lower))
        upper_value = shell_determinant(ell, rho, _qball(root_upper))
        box_value = shell_determinant(ell, rho, k_box)
        expected_lower, expected_upper = expected_face_signs[ell]
        _require_sign(lower_value, expected_lower, f"ell={ell} root lower face")
        _require_sign(upper_value, expected_upper, f"ell={ell} root upper face")
        _require_sign(box_value, "negative", f"ell={ell} target box")
        channel_records.append(
            {
                "ell": ell,
                "multiplicity": 2 * ell + 1,
                "root_count_below_every_K_in_box": 1,
                "uniform_root_bracket": [_qtext(root_lower), _qtext(root_upper)],
                "determinant_lower_face": _signed_record(lower_value),
                "determinant_upper_face": _signed_record(upper_value),
                "determinant_on_target_box": _signed_record(box_value),
            }
        )

    width = 1 - rho
    first_ell_two_lower = (arb.pi() / width) ** 2 + 6
    second_ell_zero_lower = (2 * arb.pi() / width) ** 2
    _require_sign(
        first_ell_two_lower - k_box**2,
        "positive",
        "first ell=2 Sturm lower bound minus K^2",
    )
    _require_sign(
        second_ell_zero_lower - k_box**2,
        "positive",
        "second ell=0 Sturm lower bound minus K^2",
    )

    zero_count_boundary = arb.pi() / width
    # Since eta <= 1/pi < 1/2, formula (4) gives K_0 > 4*a_rho,
    # where 4*a_rho = 8*pi*rho/(1-rho).
    coarse_k0_lower = 8 * arb.pi() * rho / width
    _require_sign(k_box - zero_count_boundary, "positive", "R_C lower boundary")
    _require_sign(coarse_k0_lower - k_box, "positive", "R_C upper boundary")

    weyl = 2 * (1 - rho**3) * k_box**3 / (9 * arb.pi())
    weyl_margin = weyl - 4
    _require_sign(weyl_margin, "positive", "Weyl margin")

    producer_path = Path(__file__).resolve()
    checker_path = producer_path.with_name(
        "round8_verify_compact_box_certificate.py"
    )
    repository_root = producer_path.parent.parent
    packet_path = repository_root / "state" / "lemma_packets" / "SHELL-rho-compact.md"
    hashed_inputs = {"producer": _sha256(producer_path)}
    if checker_path.exists():
        hashed_inputs["independent_checker"] = _sha256(checker_path)
    if packet_path.exists():
        hashed_inputs["frozen_packet"] = _sha256(packet_path)

    certificate: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "certified_pilot_when_independent_checker_returns_PASS",
        "claim": (
            "For every rho in [999/2000,1001/2000] and every K in "
            "[67/10,168/25], the strict Dirichlet shell count is 4 and is "
            "strictly smaller than (2/(9*pi))*(1-rho^3)*K^3."
        ),
        "scope": {
            "zone": "R_C",
            "rho": [_qtext(RHO_LO), _qtext(RHO_HI)],
            "K": [_qtext(K_LO), _qtext(K_HI)],
            "closed_faces": True,
        },
        "arithmetic": {
            "producer": "python-flint Arb",
            "python_flint_version": flint.__version__,
            "precision_bits": PRECISION_BITS,
            "input_convention": "exact rational endpoints; closed Arb hull",
            "output_convention": (
                "parseable outward Arb ball plus mid_rad_10exp decimal triple"
            ),
        },
        "reproducibility": {
            "python_version": sys.version.split()[0],
            "sha256": hashed_inputs,
            "commands": [
                "python -m pip install -r computations/requirements-round8-certified.txt",
                "python computations/round8_compact_box_certificate.py --output "
                "rounds/polya-main/round_008/certification/pilot-central-box.json",
                "python computations/round8_verify_compact_box_certificate.py --input "
                "rounds/polya-main/round_008/certification/pilot-central-box.json "
                "--report rounds/polya-main/round_008/certification/"
                "pilot-central-box-check.json",
            ],
        },
        "proof_dependencies": [
            "d=3 shell determinant zero criterion and multiplicity 2*ell+1",
            "positive radial roots are simple and complete",
            "strict spectral counting convention",
            "Dirichlet Poincare-Sturm bound lambda_(n,ell) >= "
            "(n*pi/(1-rho))^2 + ell*(ell+1)",
            "central residual definition R_C and monotonicity of G_1",
        ],
        "residual_membership": {
            "zero_count_boundary_pi_over_1_minus_rho": _ball_record(
                zero_count_boundary
            ),
            "coarse_K0_lower_8pi_rho_over_1_minus_rho": _ball_record(
                coarse_k0_lower
            ),
            "explanation": (
                "K is above pi/(1-rho).  Also eta<=1/pi<1/2 implies "
                "K0>4*a_rho=8*pi*rho/(1-rho), which is above the box."
            ),
        },
        "angular_cutoff": {
            "rule": "ell+1/2 < K",
            "largest_possibly_active_ell": 6,
            "first_excluded_ell": 7,
        },
        "sturm_bounds": {
            "formula": (
                "lambda_(n,ell) >= (n*pi/(1-rho))^2 + ell*(ell+1)"
            ),
            "first_ell_two_minus_K_squared": _signed_record(
                first_ell_two_lower - k_box**2
            ),
            "second_ell_zero_minus_K_squared": _signed_record(
                second_ell_zero_lower - k_box**2
            ),
            "conclusion": (
                "ell>=2 contributes zero roots; ell=0,1 have at most one root."
            ),
        },
        "channels": channel_records,
        "strict_count": {
            "weighted_count": 4,
            "calculation": "1*(ell=0 root) + 3*(ell=1 root) = 4",
            "spectral_wall_in_target_box": False,
        },
        "weyl": {
            "right_hand_side": _ball_record(weyl),
            "right_hand_side_minus_strict_count": _signed_record(weyl_margin),
        },
        "boundary_policy": {
            "target_box_faces_are_included": True,
            "root_brackets_end_strictly_below_K_lower": True,
            "future_neighbors_must_overlap_or_share_each_closed_face": True,
        },
        "limitations": [
            "This artifact certifies one tiny R_C box, not any full residual zone.",
            "It does not promote COMP-certified-bessel or SHELL-rho-compact.",
            "It does not address the enormous channel counts in the coarse R_C/R_T bounds.",
            "The independent checker is required; producer self-checks alone are insufficient.",
        ],
    }
    return certificate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
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
