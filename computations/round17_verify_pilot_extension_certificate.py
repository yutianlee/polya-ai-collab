#!/usr/bin/env python3
"""Independently verify the single Round 17 pilot extension certificate.

This checker imports neither python-flint nor the Round 17 producer.  It uses
the previously audited Round 8 exact-rational interval primitives to rebuild
all determinant signs, Sturm exclusions, residual-membership inequalities,
the complete-face intersection, and the strict Weyl margin.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

try:  # Support both repository imports and direct script execution.
    from computations import round8_verify_compact_box_certificate as qcheck
except ModuleNotFoundError:  # pragma: no cover - direct CLI path
    import round8_verify_compact_box_certificate as qcheck


SCHEMA = "polya-shell-round17-pilot-extension-v0.1"
EXPECTED_PACKET_SHA256 = (
    "eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e"
)

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


class VerificationError(RuntimeError):
    """Raised when the submitted artifact does not prove the fixed box."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def _parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"invalid rational endpoint {text!r}") from exc


def _qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _source_paths() -> dict[str, Path]:
    checker_path = Path(__file__).resolve()
    computations_dir = checker_path.parent
    repository_root = computations_dir.parent
    return {
        "producer": computations_dir / "round17_pilot_extension_certificate.py",
        "independent_checker": checker_path,
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


def _verify_provenance(data: dict[str, Any]) -> dict[str, str]:
    paths = _source_paths()
    missing = [name for name, path in paths.items() if not path.exists()]
    _require(not missing, f"missing provenance source(s): {', '.join(missing)}")
    try:
        recorded = data["provenance"]["sha256"]
        expected_packet = data["provenance"]["frozen_packet_expected_sha256"]
    except (KeyError, TypeError) as exc:
        raise VerificationError("missing provenance record") from exc
    actual = {name: _sha256(path) for name, path in paths.items()}
    _require(set(recorded) == set(actual), "provenance source set mismatch")
    for name, digest in actual.items():
        _require(recorded.get(name) == digest, f"SHA-256 mismatch for {name}")
    _require(
        expected_packet == EXPECTED_PACKET_SHA256,
        "certificate names the wrong frozen-packet hash",
    )
    _require(
        actual["frozen_round17_packet"] == EXPECTED_PACKET_SHA256,
        "immutable Round 17 packet bytes changed",
    )
    return actual


def _serialized_sign(record: dict[str, Any], expected: str, label: str) -> None:
    _require(record.get("sign") == expected, f"{label} producer sign label mismatch")
    try:
        interval = qcheck._arb_serialized_interval(record)
    except qcheck.VerificationError as exc:
        raise VerificationError(f"{label}: {exc}") from exc
    _require(interval.sign == expected, f"{label} serialized Arb sign failed")


def _summary(value: qcheck.QInterval) -> dict[str, str]:
    return qcheck._interval_summary(value)


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    """Reconstruct every decisive assertion for the fixed box B1."""

    _require(data.get("schema") == SCHEMA, "unsupported certificate schema")
    verified_hashes = _verify_provenance(data)

    scope = data.get("scope", {})
    _require(scope.get("closed_faces") is True, "B1 faces must all be closed")
    _require(scope.get("residual") == "D_16", "wrong residual identifier")
    rho_lo, rho_hi = map(_parse_fraction, scope.get("rho", []))
    k_lo, k_hi = map(_parse_fraction, scope.get("K", []))
    _require(
        (rho_lo, rho_hi, k_lo, k_hi) == (RHO_LO, RHO_HI, K_LO, K_HI),
        "scope is not the authorized single Round 17 box B1",
    )

    parent = data.get("parent_box", {})
    parent_rho = tuple(map(_parse_fraction, parent.get("rho", [])))
    parent_k = tuple(map(_parse_fraction, parent.get("K", [])))
    _require(
        parent_rho == (B0_RHO_LO, B0_RHO_HI)
        and parent_k == (B0_K_LO, B0_K_HI),
        "parent B0 coordinates changed",
    )
    _require(
        rho_lo == B0_RHO_LO
        and rho_hi == B0_RHO_HI
        and k_lo == B0_K_HI
        and k_hi > k_lo,
        "B1 does not share exactly the complete upper K-face of B0",
    )
    _require(
        parent.get("assigned_shared_face") == "K=168/25",
        "assigned face label mismatch",
    )

    pi = qcheck.machin_pi_bounds()
    _require(
        Fraction(3) < pi.lower < pi.upper < Fraction(22, 7),
        "independent pi enclosure failed",
    )

    # Exact membership in frozen packet equation (9).  The packet proves
    # rho_*<1/16 and K0(rho)>8*pi*rho/(1-rho) after rho_c.  Here
    # rho_c=1/(1+2*pi)<1/7 because pi>3, so this entire ratio box lies in
    # the K0 branch and strictly inside the two ratio endpoint faces.
    _require(Fraction(1, 16) < rho_lo, "B1 does not lie right of rho_*")
    _require(Fraction(1, 7) < rho_lo, "B1 is not proved right of rho_c")
    _require(rho_hi < Fraction(5, 6) < Fraction(7, 8), "B1 ratio cell failed")
    lower_residual_margin = (1 - rho_hi) * k_lo - pi.upper
    _require(
        lower_residual_margin > 0,
        "B1 meets the analytically covered zero-count lower wall",
    )
    k0_proxy_margin = 8 * pi.lower * rho_lo / (1 - rho_lo) - k_hi
    _require(
        k0_proxy_margin > 0,
        "B1 is not strictly below the accepted K0 upper wall",
    )

    membership = data.get("residual_membership", {})
    _serialized_sign(
        membership.get("strict_lower_margin", {}),
        "positive",
        "residual lower margin",
    )
    _serialized_sign(
        membership.get("strict_upper_proxy_margin", {}),
        "positive",
        "residual upper proxy margin",
    )
    _require(
        membership.get("conclusion")
        == "the complete closed B1 lies strictly inside D_16",
        "residual conclusion mismatch",
    )

    rho = qcheck.QInterval(rho_lo, rho_hi)
    k_box = qcheck.QInterval(k_lo, k_hi)
    width_max = 1 - rho_lo
    ell_two_margin = (pi.lower / width_max) ** 2 + 6 - k_hi**2
    second_radial_margin = (2 * pi.lower / width_max) ** 2 - k_hi**2
    _require(ell_two_margin > 0, "ell>=2 Sturm exclusion failed")
    _require(second_radial_margin > 0, "n>=2 Sturm exclusion failed")

    sturm = data.get("sturm_bounds", {})
    _serialized_sign(
        sturm.get("first_ell_two_minus_K_squared", {}),
        "positive",
        "ell>=2 producer Sturm margin",
    )
    _serialized_sign(
        sturm.get("second_ell_zero_minus_K_squared", {}),
        "positive",
        "n>=2 producer Sturm margin",
    )

    channels = data.get("channels")
    _require(isinstance(channels, list) and len(channels) == 2, "expected ell=0,1")
    weighted_count = 0
    independent_determinants: dict[str, dict[str, str]] = {}
    for expected_ell, channel in enumerate(channels):
        ell = channel.get("ell")
        _require(ell == expected_ell, "channels must be exactly ell=0,1 in order")
        multiplicity = channel.get("multiplicity")
        _require(multiplicity == 2 * ell + 1, f"bad multiplicity for ell={ell}")
        bracket = tuple(map(_parse_fraction, channel.get("uniform_root_bracket", [])))
        _require(bracket == ROOT_BRACKETS[ell], f"ell={ell} root bracket changed")
        root_lower, root_upper = bracket
        _require(root_lower < root_upper < k_lo, f"ell={ell} bracket meets B1")

        lower_det = qcheck._determinant(
            ell, rho, qcheck.QInterval.point(root_lower), pi
        )
        upper_det = qcheck._determinant(
            ell, rho, qcheck.QInterval.point(root_upper), pi
        )
        target_det = qcheck._determinant(ell, rho, k_box, pi)
        _require(lower_det.sign == "positive", f"ell={ell} lower sign failed")
        _require(upper_det.sign == "negative", f"ell={ell} upper sign failed")
        _require(target_det.sign == "negative", f"ell={ell} B1 crosses a root")

        for key, exact_value, expected_sign in (
            ("determinant_lower_face", lower_det, "positive"),
            ("determinant_upper_face", upper_det, "negative"),
            ("determinant_on_target_box", target_det, "negative"),
        ):
            _serialized_sign(
                channel.get(key, {}),
                expected_sign,
                f"ell={ell} {key}",
            )

        _require(
            channel.get("root_count_below_every_K_in_box") == 1,
            f"ell={ell} root count field failed",
        )
        weighted_count += multiplicity
        independent_determinants[f"ell_{ell}_lower_face"] = _summary(lower_det)
        independent_determinants[f"ell_{ell}_upper_face"] = _summary(upper_det)
        independent_determinants[f"ell_{ell}_target_box"] = _summary(target_det)

    strict_count = data.get("strict_count", {})
    _require(weighted_count == 4, "independent weighted count is not 4")
    _require(strict_count.get("weighted_count") == 4, "reported count mismatch")
    _require(
        strict_count.get("spectral_wall_in_target_box") is False,
        "spectral-wall flag mismatch",
    )

    weyl_lower = 2 * (1 - rho_hi**3) * k_lo**3 / (9 * pi.upper)
    weyl_margin = weyl_lower - weighted_count
    _require(weyl_margin > 0, "strict Weyl margin failed")
    weyl = data.get("weyl", {})
    _require(
        weyl.get("true_worst_corner")
        == {"rho": _qtext(rho_hi), "K": _qtext(k_lo)},
        "wrong Weyl worst corner",
    )
    _serialized_sign(
        weyl.get("right_hand_side_minus_strict_count", {}),
        "positive",
        "producer Weyl margin",
    )

    boundary = data.get("boundary_policy", {})
    _require(boundary.get("all_B1_faces_included") is True, "open B1 face")
    _require(
        boundary.get("B0_overlap_is_exactly_assigned_complete_face") is True,
        "face-overlap policy failed",
    )
    _require(boundary.get("one_new_box_only") is True, "one-box policy failed")

    return {
        "schema": "polya-shell-round17-pilot-extension-check-v0.1",
        "status": "PASS",
        "certification_scope": "the single closed box B1 only",
        "scope": scope,
        "assigned_shared_face": "K=168/25",
        "checks": {
            "frozen_packet_hash_verified": True,
            "all_provenance_hashes_verified": True,
            "complete_face_intersection_verified": True,
            "B1_subset_D16_verified": True,
            "strict_lower_and_upper_residual_margins": True,
            "uniform_root_brackets_ell_0_1": True,
            "no_spectral_wall_in_B1": True,
            "all_uncounted_modes_excluded_by_Sturm": True,
            "strict_Weyl_margin_at_true_worst_corner": True,
            "closed_faces_included": True,
        },
        "strict_weighted_count": weighted_count,
        "exact_margin_displays": {
            "lower_residual_margin": qcheck._decimal(lower_residual_margin),
            "K0_proxy_margin": qcheck._decimal(k0_proxy_margin),
            "ell_two_Sturm_margin": qcheck._decimal(ell_two_margin),
            "second_radial_Sturm_margin": qcheck._decimal(second_radial_margin),
            "Weyl_lower": qcheck._decimal(weyl_lower),
            "Weyl_minus_count": qcheck._decimal(weyl_margin),
            "note": "decimal displays are non-decisive; PASS used exact Fractions",
        },
        "independent_determinants": independent_determinants,
        "verified_sha256": verified_hashes,
        "limitations": [
            "PASS applies only to B1 and does not cover D_16 or U_16.",
            "B1 is certified coverage, not a new analytic-mask branch.",
            "No theorem obligation is promoted by this local result.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    report = verify_certificate(data)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("PASS")
    print(f"wrote {args.report}")


if __name__ == "__main__":
    main()
