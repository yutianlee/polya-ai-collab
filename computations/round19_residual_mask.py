#!/usr/bin/env python3
"""Certified classifier for the exact post-Round-18 shell residual.

Round 19 imports the frozen Round 18 classifier and adds only the accepted
closed angular staircase through ``k_5``.  It independently evaluates the
normalized two-piece residual ``D18`` and the identical theorem-wise
uncovered set.  Rational comparisons are exact.  Comparisons involving pi
or another accepted irrational constant use the inherited Arb precision
escalation policy; an unresolved material comparison returns
``indeterminate`` rather than a guessed side.

The ``k_5``, ``2 z_rho``, and ``k_6`` records are an inventory of method
walls.  They are not used to impose an unproved global ordering.  This
module checks set bookkeeping only and proves no new spectral estimate,
analytic band, or finite Bessel certificate.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable

try:
    from computations import round18_residual_mask as r18
except ImportError:  # pragma: no cover - direct script execution
    import round18_residual_mask as r18


SCHEMA = "polya-shell-round19-residual-mask-v0.1"

RHO_HALF = Fraction(1, 2)
RHO_SEAM = Fraction(5, 6)
RHO_THIN = Fraction(7, 8)

B0_RHO_LO = r18.B0_RHO_LO
B0_RHO_HI = r18.B0_RHO_HI
B0_K_LO = r18.B0_K_LO
B0_K_HI = r18.B0_K_HI

B1_RHO_LO = r18.B1_RHO_LO
B1_RHO_HI = r18.B1_RHO_HI
B1_K_LO = r18.B1_K_LO
B1_K_HI = r18.B1_K_HI


@dataclass(frozen=True)
class SetDecision:
    """A certified tri-state decision with the signs used to make it."""

    membership: bool | None
    piece: str | None
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[r18.r17.SignRecord, ...]


@dataclass(frozen=True)
class PointClassification:
    schema: str
    rho: str
    K: str
    status: str
    analytic_reasons: tuple[str, ...]
    certified_regression_reasons: tuple[str, ...]
    residual_piece: str | None
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[r18.r17.SignRecord, ...]


def qtext(value: Fraction) -> str:
    return r18.qtext(value)


def parse_fraction(text: str) -> Fraction:
    return r18.parse_fraction(text)


def _deduplicate(items: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(items))


def closed_c18_membership_from_signs(
    rho_c_sign: int | None,
    z_lower_sign: int | None,
    k5_upper_sign: int | None,
    *,
    rho_le_thin: bool,
) -> bool | None:
    """Evaluate the accepted closed Round 18 staircase from face signs.

    The signs are those of ``rho-rho_c``, ``K-z_rho``, and
    ``k_5(rho)^2-K^2``.  Every equality face is included.
    """

    factors: tuple[bool | None, ...] = (
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k5_upper_sign is None else k5_upper_sign >= 0,
    )
    if any(value is False for value in factors):
        return False
    if any(value is None for value in factors):
        return None
    return True


def new_c18_membership_from_signs(
    rho_c_sign: int | None,
    k2_upper_sign: int | None,
    k5_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> bool | None:
    """Evaluate the genuinely new set ``C18`` from certified signs.

    ``C18`` is strict above ``k_2``, closed at ``k_5``, includes
    ``rho=rho_c``, and excludes the old complete endpoint ``rho=7/8``.
    """

    factors: tuple[bool | None, ...] = (
        rho_lt_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if k2_upper_sign is None else k2_upper_sign < 0,
        None if k5_upper_sign is None else k5_upper_sign >= 0,
    )
    if any(value is False for value in factors):
        return False
    if any(value is None for value in factors):
        return None
    return True


def d18_piece_from_signs(
    rho_star_sign: int | None,
    upper_floor_sign: int | None,
    rho_c_sign: int | None,
    high_angular_lower_sign: int,
    k5_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> bool | None:
    """Evaluate the normalized exact ``D18`` predicate.

    ``upper_floor_sign`` is the sign of ``U(rho)-K`` and
    ``high_angular_lower_sign`` is the exact sign of ``2*rho*K-1``.
    For ``rho>=rho_c``, ``k5_upper_sign<0`` is exactly ``K>k_5``.
    Every displayed frequency side is strict, and ``rho=rho_c`` is
    assigned to the post-``k_5`` piece.
    """

    mandatory: tuple[bool | None, ...] = (
        None if rho_star_sign is None else rho_star_sign > 0,
        rho_lt_thin,
        None if upper_floor_sign is None else upper_floor_sign > 0,
    )
    if any(value is False for value in mandatory):
        return False
    if any(value is None for value in mandatory):
        return None
    if rho_c_sign is None:
        return None
    if rho_c_sign < 0:
        return high_angular_lower_sign > 0
    if k5_upper_sign is None:
        return None
    return k5_upper_sign < 0


def _rho_c_sign(rho: Fraction) -> r18.r17.SignRecord:
    return r18._rho_c_sign(rho)


def _z_lower_sign(rho: Fraction, k: Fraction) -> r18.r17.SignRecord:
    return r18._z_lower_sign(rho, k)


def _k2_upper_sign(rho: Fraction, k: Fraction) -> r18.r17.SignRecord:
    return r18._k2_upper_sign(rho, k)


def _k5_upper_sign(rho: Fraction, k: Fraction) -> r18.r17.SignRecord:
    """Return the sign of ``k_5(rho)^2-K^2`` without a square root."""

    return r18.r17.certified_sign(
        "pi^2+(30-K^2)(1-rho)^2",
        lambda: r18.r17.arb.pi() ** 2
        + r18.r17.qball((Fraction(30) - k * k) * (1 - rho) ** 2),
    )


def _two_z_upper_sign(rho: Fraction, k: Fraction) -> r18.r17.SignRecord:
    """Return the sign of ``(2 z_rho)^2-K^2`` independently."""

    return r18.r17.certified_sign(
        "4*pi^2-K^2(1-rho)^2",
        lambda: 4 * r18.r17.arb.pi() ** 2
        - r18.r17.qball(k * k * (1 - rho) ** 2),
    )


def _k6_upper_sign(rho: Fraction, k: Fraction) -> r18.r17.SignRecord:
    """Return the sign of ``k_6(rho)^2-K^2`` independently."""

    return r18.r17.certified_sign(
        "pi^2+(42-K^2)(1-rho)^2",
        lambda: r18.r17.arb.pi() ** 2
        + r18.r17.qball((Fraction(42) - k * k) * (1 - rho) ** 2),
    )


def method_wall_signs(
    rho: Fraction, k: Fraction
) -> tuple[r18.r17.SignRecord, r18.r17.SignRecord, r18.r17.SignRecord]:
    """Inventory the sides of ``k_5``, ``2z``, and ``k_6`` independently.

    The tuple order is exactly ``(k_5, 2z, k_6)``.  No result from one
    record is used to infer the sign or ordering of another.
    """

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")
    return (
        _k5_upper_sign(rho, k),
        _two_z_upper_sign(rho, k),
        _k6_upper_sign(rho, k),
    )


def rho_c_local_method_order_signs(
) -> tuple[r18.r17.SignRecord, r18.r17.SignRecord]:
    """Recheck only the accepted local fact ``k5(rho_c)<2z<k6(rho_c)``.

    At ``rho_c``, ``z=pi+1/2``.  The returned signs are respectively those
    of ``(2z)^2-k5^2=3z^2-30`` and ``k6^2-(2z)^2=42-3z^2``.
    """

    left = r18.r17.certified_sign(
        "3*(pi+1/2)^2-30",
        lambda: 3
        * (r18.r17.arb.pi() + r18.r17.qball(Fraction(1, 2))) ** 2
        - 30,
    )
    right = r18.r17.certified_sign(
        "42-3*(pi+1/2)^2",
        lambda: 42
        - 3
        * (r18.r17.arb.pi() + r18.r17.qball(Fraction(1, 2))) ** 2,
    )
    return left, right


def closed_c18_decision(rho: Fraction, k: Fraction) -> SetDecision:
    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    records = (
        _rho_c_sign(rho),
        _z_lower_sign(rho, k),
        _k5_upper_sign(rho, k),
    )
    membership = closed_c18_membership_from_signs(
        records[0].sign,
        records[1].sign,
        records[2].sign,
        rho_le_thin=rho <= RHO_THIN,
    )
    unresolved = (
        tuple(record.label for record in records if record.sign is None)
        if membership is None
        else tuple()
    )
    return SetDecision(membership, None, unresolved, records)


def new_c18_decision(rho: Fraction, k: Fraction) -> SetDecision:
    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    records = (
        _rho_c_sign(rho),
        _k2_upper_sign(rho, k),
        _k5_upper_sign(rho, k),
    )
    membership = new_c18_membership_from_signs(
        records[0].sign,
        records[1].sign,
        records[2].sign,
        rho_lt_thin=rho < RHO_THIN,
    )
    unresolved = (
        tuple(record.label for record in records if record.sign is None)
        if membership is None
        else tuple()
    )
    return SetDecision(membership, None, unresolved, records)


def upper_floor_decision(rho: Fraction, k: Fraction) -> r18.SetDecision:
    """Use the authenticated complete Round 18 upper-floor classifier."""

    return r18.upper_floor_decision(rho, k)


def normalized_d18_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify the exact strict two-piece formula for ``D18`` directly."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    rho_star = r18.r17.certified_sign(
        "rho-rho_*", lambda: r18.r17.qball(rho) - r18.r17.constants()[3]
    )
    if rho_star.sign is not None and rho_star.sign <= 0:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho >= RHO_THIN:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho_star.sign is None:
        return SetDecision(None, None, (rho_star.label,), (rho_star,))

    upper = upper_floor_decision(rho, k)
    rho_c = _rho_c_sign(rho)
    k5_upper = _k5_upper_sign(rho, k)
    exact_lower = 2 * rho * k - 1
    exact_lower_sign = 1 if exact_lower > 0 else (-1 if exact_lower < 0 else 0)

    membership = d18_piece_from_signs(
        rho_star.sign,
        None if upper.membership is None else (1 if upper.membership else -1),
        rho_c.sign,
        exact_lower_sign,
        k5_upper.sign,
        rho_lt_thin=rho < RHO_THIN,
    )
    if membership is True:
        piece = "lower-ratio" if rho_c.sign == -1 else "post-k5"
    else:
        piece = None
    records = (rho_star,) + upper.sign_records + (rho_c, k5_upper)
    unresolved = (
        _deduplicate(
            list(upper.unresolved_comparisons)
            + [record.label for record in (rho_c, k5_upper) if record.sign is None]
        )
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def theorem_uncovered_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Return ``U18``; exact B0/B1 absorption makes it identical to D18."""

    return normalized_d18_decision(rho, k)


def classify_point(rho: Fraction, k: Fraction) -> PointClassification:
    """Classify a rational point under A18, D18, and retained regressions."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    old = r18.classify_point(rho, k)
    staircase = closed_c18_decision(rho, k)
    analytic = list(old.analytic_reasons)
    certified = list(old.certified_regression_reasons)

    mandatory_old_unresolved = "rho-rho_*" in old.unresolved_comparisons
    if old.status == "outside_I17":
        status = "outside_I18"
    elif old.status == "analytic_covered":
        status = "analytic_covered"
    elif staircase.membership is True and not mandatory_old_unresolved:
        analytic.append("angular-staircase-round18")
        status = "analytic_covered"
    elif old.status == "indeterminate" or staircase.membership is None:
        status = "indeterminate"
    else:
        status = "analytic_residual_uncovered"

    direct = normalized_d18_decision(rho, k)
    if status == "analytic_residual_uncovered":
        if direct.membership is None:
            status = "indeterminate"
        elif direct.membership is False:
            raise AssertionError("A18 complement disagrees with normalized D18")
    elif status == "analytic_covered" and direct.membership is True:
        raise AssertionError("A18 intersects normalized D18")

    residual_piece = direct.piece if status == "analytic_residual_uncovered" else None
    unresolved = _deduplicate(
        list(old.unresolved_comparisons)
        + list(staircase.unresolved_comparisons)
        + (list(direct.unresolved_comparisons) if status == "indeterminate" else [])
    )
    records = old.sign_records + staircase.sign_records + direct.sign_records

    return PointClassification(
        SCHEMA,
        qtext(rho),
        qtext(k),
        status,
        tuple(analytic),
        tuple(certified),
        residual_piece,
        unresolved,
        records,
    )


def _mask_manifest() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "authenticated_inputs": {
            "baseline_commit": "15e4d61db885bfff00a674fd7f37e4cffda70d0c",
            "state/proof_obligations.yml": (
                "24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e"
            ),
            "state/next_round_prompts.md": (
                "7d05055b4b884b052f3970bd7b08335dfe63bca25b5ac5a9db8704f6a88db2f7"
            ),
            "state/lemma_packets/SHELL-rho-compact-round18.md": (
                "7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9"
            ),
            "computations/round18_residual_mask.py": (
                "75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da"
            ),
            "computations/tests/test_round18_residual_mask.py": (
                "ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103"
            ),
            "rounds/polya-main/round_018/judge/judge-018.md": (
                "73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61"
            ),
            "rounds/polya-main/round_018/exploration/residual-mask-freeze.md": (
                "7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff"
            ),
        },
        "derivation": {
            "base_classifier": "computations/round18_residual_mask.py",
            "operation": "A18=A17 union closed_round18_staircase",
            "residual_operation": "D18=D17 minus C18",
        },
        "closed_round18_staircase": {
            "rho": "rho_c<=rho<=7/8",
            "K": "z_rho<=K<=k5(rho)",
            "rho_c": "1/(1+2*pi)",
            "z_rho": "pi/(1-rho)",
            "k5_squared": "z_rho^2+30",
            "faces": "all displayed faces included",
        },
        "new_C18": {
            "rho": "rho_c<=rho<7/8",
            "K": "k2(rho)<K<=k5(rho)",
            "old_face_owners": ["K=k2(rho)", "rho=7/8"],
            "new_included_face": "K=k5(rho)",
        },
        "analytic_residual": {
            "name": "D18",
            "lower_ratio_piece": "rho_*<rho<rho_c and 1/(2rho)<K<U(rho)",
            "post_band_piece": "rho_c<=rho<7/8 and k5(rho)<K<U(rho)",
            "all_frequency_faces": "strict",
            "rho_c_assignment": "post_band_piece",
        },
        "theorem_wise_uncovered": {
            "name": "U18",
            "formula": "U18=D18",
            "reason": "B0 and B1 are subsets of C17, hence of A18",
        },
        "upper_floor": {
            "definition": (
                "min(K0(rho), H0(rho) when rho<omega0, "
                "54/(1-rho)^2 when rho>=5/6)"
            ),
            "piecewise": [
                "H0 on rho_*<rho<rho_HK",
                "K0 on rho_HK<=rho<5/6",
                "54/(1-rho)^2 on 5/6<=rho<7/8",
            ],
            "rho_HK": (
                "unique P_HK=0 root in "
                "(9407/100000,94071/1000000); H0=K0"
            ),
            "interfaces": [
                "rho=rho_HK: H0=K0, K0 branch assigned",
                "rho=omega0: H0 availability ends; K0 was already active",
                "rho=1/2: eta formula interface inside continuous K0",
                "rho=5/6: seam-54 branch assigned inclusively",
            ],
            "upper_faces": "included analytic owners; excluded from D18",
        },
        "face_owners": {
            "rho=rho_*": "complete small-hole endpoint",
            "rho=rho_c": "included in post-k5 residual piece; no gap or overlap",
            "rho=7/8": "complete thin endpoint",
            "K=1/(2rho), rho<rho_c": "inherited high-angular owner",
            "K=z_rho": "inherited phase-zero owner",
            "K=k2(rho)": "Round 17 first-angular-band owner",
            "K=k5(rho)": "Round 18 angular-staircase owner",
            "K=U(rho)": "active inherited H0, K0, or seam-54 owner",
            "K=295^2": "Round 16 all-ratio high-frequency owner",
            "K=2z_rho": "method wall only; D18 membership is not altered there",
            "K=k6(rho)": "method wall only; D18 membership is not altered there",
        },
        "certified_regressions": {
            "B0": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["67/10", "168/25"],
                "faces": "closed",
                "relation": "B0 subset C17 subset A18",
            },
            "B1": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["168/25", "673/100"],
                "faces": "closed",
                "relation": "B1 subset C17 subset A18",
            },
            "uncovered_formula": "U18=D18; neither box is subtracted again",
        },
        "ratio_interfaces": [
            "rho=rho_* (complete endpoint outside D18)",
            "rho=1/16 (inherited coarse bookkeeping split only)",
            "rho=rho_HK (shared H0=K0 upper face)",
            "rho=omega0 (small-hole open interface; K0 active)",
            "rho=rho_c (assigned to post-k5 piece)",
            "rho=1/2 (continuous K0 formula interface)",
            "rho=5/6 (seam begins inclusively)",
            "rho=7/8 (complete endpoint outside D18)",
        ],
        "method_walls": {
            "inventory": [
                "k5(rho)=sqrt(z_rho^2+30)",
                "2z_rho",
                "k6(rho)=sqrt(z_rho^2+42)",
                "U(rho)",
            ],
            "accepted_local_fact": "k5(rho_c)<2z_rho_c<k6(rho_c)",
            "global_ordering_encoded": False,
            "crossing_threshold_encoded": False,
            "classification_policy": (
                "each wall sign is computed independently; 2z and k6 do not "
                "change D18 membership"
            ),
            "not_a_counterexample": True,
        },
    }


def _require_status(
    rho: Fraction,
    k: Fraction,
    status: str,
    piece: str | None = None,
) -> PointClassification:
    result = classify_point(rho, k)
    if result.status != status or (piece is not None and result.residual_piece != piece):
        raise AssertionError(
            f"({qtext(rho)}, {qtext(k)}): expected {status}/{piece}, "
            f"obtained {result.status}/{result.residual_piece}; "
            f"analytic={result.analytic_reasons}; "
            f"unresolved={result.unresolved_comparisons}"
        )
    return result


def self_check() -> list[str]:
    passed: list[str] = []

    _require_status(
        Fraction(7, 51),
        Fraction(4),
        "analytic_residual_uncovered",
        "lower-ratio",
    )
    passed.append("lower-ratio D18 piece")

    _require_status(
        Fraction(1, 2),
        Fraction(30),
        "analytic_residual_uncovered",
        "post-k5",
    )
    passed.append("post-k5 D18 piece and accepted nonempty witness")

    band = _require_status(Fraction(1, 2), Fraction(7), "analytic_covered")
    assert "angular-staircase-round18" in band.analytic_reasons
    passed.append("promoted closed Round 18 staircase")

    endpoint = _require_status(RHO_THIN, Fraction(0), "analytic_covered")
    assert "rho-one-endpoint-round16" in endpoint.analytic_reasons
    passed.append("complete thin endpoint")

    for rho, k in (
        (B0_RHO_LO, B0_K_LO),
        (B0_RHO_HI, B0_K_HI),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert "round8-certified-pilot-B0" in result.certified_regression_reasons
    passed.append("B0 retained and analytically absorbed")

    for rho, k in (
        (B1_RHO_LO, B1_K_LO),
        (B1_RHO_HI, B1_K_HI),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert "round17-certified-pilot-B1" in result.certified_regression_reasons
    passed.append("B1 retained and analytically absorbed")

    below_seam = upper_floor_decision(RHO_SEAM, Fraction(1943))
    seam_face = upper_floor_decision(RHO_SEAM, Fraction(1944))
    assert below_seam.membership is True and below_seam.piece == "seam-54"
    assert seam_face.membership is False and seam_face.piece == "seam-54"
    passed.append("strict residual side at inclusive seam face")

    left_switch = upper_floor_decision(Fraction(9, 100), Fraction(1))
    right_switch = upper_floor_decision(Fraction(1, 10), Fraction(1))
    assert left_switch.piece == "H0" and left_switch.membership is True
    assert right_switch.piece == "K0" and right_switch.membership is True
    passed.append("complete H0/K0 upper-floor branch switch")

    assert closed_c18_membership_from_signs(0, 0, 0, rho_le_thin=True) is True
    assert new_c18_membership_from_signs(0, 0, 0, rho_lt_thin=True) is False
    assert new_c18_membership_from_signs(0, -1, 0, rho_lt_thin=True) is True
    passed.append("closed staircase and exact genuinely-new C18 faces")

    assert d18_piece_from_signs(1, 1, -1, 0, 1, rho_lt_thin=True) is False
    assert d18_piece_from_signs(1, 1, 0, 1, 0, rho_lt_thin=True) is False
    assert d18_piece_from_signs(1, 0, 1, 1, -1, rho_lt_thin=True) is False
    passed.append("all normalized D18 frequency faces are excluded")

    local_left, local_right = rho_c_local_method_order_signs()
    assert local_left.sign == 1 and local_right.sign == 1
    passed.append("accepted local k5<2z<k6 method fact at rho_c")

    point = (Fraction(1, 2), Fraction(30))
    assert theorem_uncovered_decision(*point) == normalized_d18_decision(*point)
    passed.append("theorem-wise uncovered set equals D18")

    _require_status(Fraction(1, 100), Fraction(1), "outside_I18")
    passed.append("outside compact interval is not called residual")

    return passed


def _point_argument(text: str) -> tuple[Fraction, Fraction]:
    try:
        rho_text, k_text = text.split(",", maxsplit=1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("point must be RHO,K") from exc
    return parse_fraction(rho_text), parse_fraction(k_text)


def _serialize(result: PointClassification) -> dict[str, object]:
    data = asdict(result)
    data["sign_records"] = [asdict(record) for record in result.sign_records]
    return data


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--point", action="append", type=_point_argument, default=[])
    args = parser.parse_args(list(argv) if argv is not None else None)

    payload: dict[str, object] = {"schema": SCHEMA}
    if args.manifest:
        payload["manifest"] = _mask_manifest()
    if args.self_check or (not args.manifest and not args.point):
        payload["self_check"] = {"status": "PASS", "checks": self_check()}
    if args.point:
        payload["points"] = [_serialize(classify_point(rho, k)) for rho, k in args.point]
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
