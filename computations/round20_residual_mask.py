#!/usr/bin/env python3
"""Certified set classifier for the exact post-Round-19 shell residual.

This module imports :mod:`computations.round19_residual_mask` as the opaque
accepted ``A18`` classifier and adds only the promoted Round 19 cover.  It
then evaluates the normalized three-piece residual ``D19`` independently.
It is set bookkeeping: it proves no Round 20 spectral estimate and encodes
no prospective Round 20 candidate.

Rational comparisons at ``rho_0=1/sqrt(337)``, ``L=1/(2 rho)``, and
``d=sqrt(337)/2`` are exact after squaring on their positive domains.
Comparisons involving ``rho_c``, ``z_rho``, ``k_6``, or the inherited upper
floor use the accepted precision-escalated Arb policy.  A material
unresolved sign is reported as ``indeterminate`` rather than guessed.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable

try:
    from computations import round19_residual_mask as r19
except ImportError:  # pragma: no cover - direct script execution
    import round19_residual_mask as r19


SCHEMA = "polya-shell-round20-residual-mask-v0.1"
BASELINE_COMMIT = "658674117632d60990ac9b9046aa0fcff9e91a62"

RHO_HALF = Fraction(1, 2)
RHO_SEAM = Fraction(5, 6)
RHO_THIN = Fraction(7, 8)

B0_RHO_LO = r19.B0_RHO_LO
B0_RHO_HI = r19.B0_RHO_HI
B0_K_LO = r19.B0_K_LO
B0_K_HI = r19.B0_K_HI

B1_RHO_LO = r19.B1_RHO_LO
B1_RHO_HI = r19.B1_RHO_HI
B1_K_LO = r19.B1_K_LO
B1_K_HI = r19.B1_K_HI


@dataclass(frozen=True)
class SetDecision:
    """A certified tri-state set decision and its supporting signs."""

    membership: bool | None
    piece: str | None
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[r19.r18.r17.SignRecord, ...]


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
    sign_records: tuple[r19.r18.r17.SignRecord, ...]


def qtext(value: Fraction) -> str:
    return r19.qtext(value)


def parse_fraction(text: str) -> Fraction:
    return r19.parse_fraction(text)


def _deduplicate(items: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(items))


def _tri_and(*factors: bool | None) -> bool | None:
    if any(value is False for value in factors):
        return False
    if any(value is None for value in factors):
        return None
    return True


def _tri_or(*factors: bool | None) -> bool | None:
    if any(value is True for value in factors):
        return True
    if any(value is None for value in factors):
        return None
    return False


def _exact_sign_record(
    label: str, value: Fraction
) -> r19.r18.r17.SignRecord:
    sign = 1 if value > 0 else (-1 if value < 0 else 0)
    exact = qtext(value)
    return r19.r18.r17.SignRecord(label, sign, 0, f"[{exact}, {exact}]")


def _rho0_sign(rho: Fraction) -> r19.r18.r17.SignRecord:
    """Return the exact sign of ``rho-rho_0`` on ``rho>0``.

    Since both sides are positive, this is the sign of ``337*rho^2-1``.
    """

    return _exact_sign_record("337*rho^2-1", 337 * rho * rho - 1)


def _l_lower_sign(rho: Fraction, k: Fraction) -> r19.r18.r17.SignRecord:
    """Return the exact sign of ``K-L(rho)`` on ``rho>0``."""

    return _exact_sign_record("2*rho*K-1", 2 * rho * k - 1)


def _d_upper_sign(k: Fraction) -> r19.r18.r17.SignRecord:
    """Return the exact sign of ``d^2-K^2`` for ``d=sqrt(337)/2``."""

    return _exact_sign_record("337-4*K^2", 337 - 4 * k * k)


def _rho_c_sign(rho: Fraction) -> r19.r18.r17.SignRecord:
    return r19._rho_c_sign(rho)


def _z_lower_sign(rho: Fraction, k: Fraction) -> r19.r18.r17.SignRecord:
    return r19._z_lower_sign(rho, k)


def _k6_upper_sign(rho: Fraction, k: Fraction) -> r19.r18.r17.SignRecord:
    return r19._k6_upper_sign(rho, k)


def c19_membership_from_signs(
    rho0_sign: int | None,
    rho_c_sign: int | None,
    l_lower_sign: int,
    d_upper_sign: int,
    z_lower_sign: int | None,
    k6_upper_sign: int | None,
    *,
    rho_le_thin: bool,
) -> bool | None:
    """Evaluate exactly the promoted Round 19 cover added to ``A18``.

    The lower component is
    ``rho_0<rho<rho_c, L(rho)<K<=d``.  The closed high component is
    ``rho_c<=rho<=7/8, z_rho<=K<=k_6(rho)``.  Thus ``K=d`` and ``K=k_6``
    are included, while the lower component is strict at both ratio faces
    and at ``K=L``.
    """

    lower = _tri_and(
        None if rho0_sign is None else rho0_sign > 0,
        None if rho_c_sign is None else rho_c_sign < 0,
        l_lower_sign > 0,
        d_upper_sign >= 0,
    )
    high = _tri_and(
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k6_upper_sign is None else k6_upper_sign >= 0,
    )
    return _tri_or(lower, high)


def _c19_piece_from_signs(
    rho0_sign: int | None,
    rho_c_sign: int | None,
    l_lower_sign: int,
    d_upper_sign: int,
    z_lower_sign: int | None,
    k6_upper_sign: int | None,
    *,
    rho_le_thin: bool,
) -> tuple[bool | None, str | None]:
    lower = _tri_and(
        None if rho0_sign is None else rho0_sign > 0,
        None if rho_c_sign is None else rho_c_sign < 0,
        l_lower_sign > 0,
        d_upper_sign >= 0,
    )
    high = _tri_and(
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k6_upper_sign is None else k6_upper_sign >= 0,
    )
    membership = _tri_or(lower, high)
    if lower is True:
        return membership, "lower-ratio-round19"
    if high is True:
        return membership, "high-ratio-round19"
    return membership, None


def accepted_c19_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify the exact accepted Round 19 addition to ``A18``."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    rho0 = _rho0_sign(rho)
    rho_c = _rho_c_sign(rho)
    lower = _l_lower_sign(rho, k)
    d_upper = _d_upper_sign(k)
    z_lower = _z_lower_sign(rho, k)
    k6_upper = _k6_upper_sign(rho, k)
    records = (rho0, rho_c, lower, d_upper, z_lower, k6_upper)
    membership, piece = _c19_piece_from_signs(
        rho0.sign,
        rho_c.sign,
        lower.sign,
        d_upper.sign,
        z_lower.sign,
        k6_upper.sign,
        rho_le_thin=rho <= RHO_THIN,
    )
    unresolved = (
        tuple(record.label for record in records if record.sign is None)
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def d19_membership_from_signs(
    rho_star_sign: int | None,
    upper_floor_sign: int | None,
    rho0_sign: int | None,
    rho_c_sign: int | None,
    l_lower_sign: int,
    d_upper_sign: int,
    k6_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> bool | None:
    """Evaluate the normalized exact three-piece ``D19`` predicate.

    ``upper_floor_sign`` is positive exactly when ``K<U(rho)``;
    ``d_upper_sign<0`` means ``K>d``; and ``k6_upper_sign<0`` means
    ``K>k_6(rho)``.  The first ratio piece includes ``rho=rho_0``.  The
    high piece includes ``rho=rho_c``.  Every displayed frequency face is
    strict.
    """

    mandatory = _tri_and(
        None if rho_star_sign is None else rho_star_sign > 0,
        rho_lt_thin,
        None if upper_floor_sign is None else upper_floor_sign > 0,
    )
    if mandatory is not True:
        return mandatory

    # Use the authenticated order rho_0<rho_c.  This branch form is more
    # informative than a raw disjunction: when rho_c itself is unresolved,
    # equal decisions from the adjacent d and k6 thresholds settle D19.
    if rho0_sign is not None and rho0_sign <= 0:
        return l_lower_sign > 0
    if rho0_sign is not None and rho0_sign > 0:
        if rho_c_sign is not None and rho_c_sign < 0:
            return d_upper_sign < 0
        if rho_c_sign is not None and rho_c_sign >= 0:
            return None if k6_upper_sign is None else k6_upper_sign < 0
        middle_frequency = d_upper_sign < 0
        high_frequency = (
            None if k6_upper_sign is None else k6_upper_sign < 0
        )
        if high_frequency is not None and middle_frequency == high_frequency:
            return middle_frequency
        return None

    low = _tri_and(
        None if rho0_sign is None else rho0_sign <= 0,
        l_lower_sign > 0,
    )
    middle = _tri_and(
        None if rho0_sign is None else rho0_sign > 0,
        None if rho_c_sign is None else rho_c_sign < 0,
        d_upper_sign < 0,
    )
    high = _tri_and(
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if k6_upper_sign is None else k6_upper_sign < 0,
    )
    return _tri_or(low, middle, high)


def _d19_piece_from_signs(
    rho_star_sign: int | None,
    upper_floor_sign: int | None,
    rho0_sign: int | None,
    rho_c_sign: int | None,
    l_lower_sign: int,
    d_upper_sign: int,
    k6_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> tuple[bool | None, str | None]:
    membership = d19_membership_from_signs(
        rho_star_sign,
        upper_floor_sign,
        rho0_sign,
        rho_c_sign,
        l_lower_sign,
        d_upper_sign,
        k6_upper_sign,
        rho_lt_thin=rho_lt_thin,
    )
    if membership is not True:
        return membership, None
    if rho0_sign is not None and rho0_sign <= 0:
        return True, "small-hole-through-rho0"
    if rho_c_sign is not None and rho_c_sign < 0:
        return True, "middle-above-d"
    if rho_c_sign is not None and rho_c_sign >= 0:
        return True, "high-above-k6"
    # Both adjacent lower-frequency tests can certify membership even when
    # the irrational rho_c side itself is unresolved.
    return True, "rho-c-interface-unassigned"


def upper_floor_decision(rho: Fraction, k: Fraction) -> r19.r18.SetDecision:
    """Use the authenticated complete inherited upper-floor classifier."""

    return r19.upper_floor_decision(rho, k)


def normalized_d19_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify the exact strict three-piece formula for ``D19`` directly."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    rho_star = r19.r18.r17.certified_sign(
        "rho-rho_*", lambda: r19.r18.r17.qball(rho) - r19.r18.r17.constants()[3]
    )
    if rho_star.sign is not None and rho_star.sign <= 0:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho >= RHO_THIN:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho_star.sign is None:
        return SetDecision(None, None, (rho_star.label,), (rho_star,))

    upper = upper_floor_decision(rho, k)
    rho0 = _rho0_sign(rho)
    rho_c = _rho_c_sign(rho)
    lower = _l_lower_sign(rho, k)
    d_upper = _d_upper_sign(k)
    k6_upper = _k6_upper_sign(rho, k)
    upper_sign = None if upper.membership is None else (1 if upper.membership else -1)
    membership, piece = _d19_piece_from_signs(
        rho_star.sign,
        upper_sign,
        rho0.sign,
        rho_c.sign,
        lower.sign,
        d_upper.sign,
        k6_upper.sign,
        rho_lt_thin=rho < RHO_THIN,
    )
    records = (
        (rho_star,)
        + upper.sign_records
        + (rho0, rho_c, lower, d_upper, k6_upper)
    )
    unresolved = (
        _deduplicate(
            list(upper.unresolved_comparisons)
            + [record.label for record in (rho_c, k6_upper) if record.sign is None]
        )
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def theorem_uncovered_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Return ``U19``; absorbed B0/B1 make it identical to ``D19``."""

    return normalized_d19_decision(rho, k)


def classify_point(rho: Fraction, k: Fraction) -> PointClassification:
    """Classify a rational point under accepted ``A19`` and exact ``D19``."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    old = r19.classify_point(rho, k)
    added = accepted_c19_decision(rho, k)
    analytic = list(old.analytic_reasons)
    certified = list(old.certified_regression_reasons)
    mandatory_old_unresolved = "rho-rho_*" in old.unresolved_comparisons

    if old.status == "outside_I18":
        status = "outside_I19"
    elif old.status == "analytic_covered":
        status = "analytic_covered"
    elif added.membership is True and not mandatory_old_unresolved:
        analytic.append(f"two-sided-staircase-round19:{added.piece}")
        status = "analytic_covered"
    elif old.status == "analytic_residual_uncovered" and added.membership is False:
        status = "analytic_residual_uncovered"
    else:
        status = "indeterminate"

    direct = normalized_d19_decision(rho, k)
    if status == "analytic_residual_uncovered":
        if direct.membership is None:
            status = "indeterminate"
        elif direct.membership is False:
            raise AssertionError("A19 complement disagrees with normalized D19")
    elif status == "analytic_covered" and direct.membership is True:
        raise AssertionError("A19 intersects normalized D19")
    elif status == "indeterminate" and direct.membership is True:
        # The normalized union can occasionally settle both sides of the
        # rho_c interface even when its side sign alone is unresolved.
        status = "analytic_residual_uncovered"

    residual_piece = direct.piece if status == "analytic_residual_uncovered" else None
    unresolved = _deduplicate(
        list(old.unresolved_comparisons)
        + list(added.unresolved_comparisons)
        + (list(direct.unresolved_comparisons) if status == "indeterminate" else [])
    )
    if status != "indeterminate":
        unresolved = tuple()
    records = old.sign_records + added.sign_records + direct.sign_records

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
            "baseline_commit": BASELINE_COMMIT,
            "state/proof_obligations.yml": (
                "ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187"
            ),
            "state/next_round_prompts.md": (
                "c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159"
            ),
            "state/lemma_packets/SHELL-rho-compact-round19.md": (
                "33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50"
            ),
            "computations/round19_residual_mask.py": (
                "bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6"
            ),
            "computations/tests/test_round19_residual_mask.py": (
                "41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787"
            ),
            "rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md": (
                "9e7dedaab08425166998a5c766bdb32d3787d9f35b6c4bf4b7d6be07009c9b43"
            ),
            "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md": (
                "87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db"
            ),
            "rounds/polya-main/round_019/exploration/candidate-claim-freeze.md": (
                "7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff"
            ),
            "sources/round19_bessel_zero_bounds.md": (
                "7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f"
            ),
            "rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md": (
                "ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718"
            ),
            "rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md": (
                "24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17"
            ),
            "computations/round19_verify_two_sided_staircase.py": (
                "4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23"
            ),
            "computations/tests/test_round19_verify_two_sided_staircase.py": (
                "1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08"
            ),
            "rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md": (
                "fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7"
            ),
            "rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md": (
                "fe46d95718e4e070bdea18ee1c2fbcfc89d5eb3c53b5346d712c72715f667365"
            ),
            "rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md": (
                "6e290b70bf2bdaf9785f67fcef4a284a48b08ccce0c0951e72f0322406e58148"
            ),
            "rounds/polya-main/round_019/judge/judge-019.md": (
                "fdf79fa03f1cd82e5ecf4db89750aa0e5d876be6430a25e488bb1c34bdabc83b"
            ),
            "rounds/polya-main/round_019/reviews/state-patch-final-audit.md": (
                "a4cb244e9b97fb5cceaaf82896e87320c1d828d75da09a4da0bd8c13839ca76a"
            ),
            "rounds/polya-main/round_019/reviews/derived-state-final-audit.md": (
                "c94de1a40cec0650ca1adcd0662f1bc1cb403f503472afab3ef3e27a48e41e93"
            ),
        },
        "derivation": {
            "base_classifier": "computations/round19_residual_mask.py",
            "base_interpretation": "opaque accepted A18",
            "operation": "A19=A18 union accepted_Round19_cover",
            "residual_operation": "D19=D18 minus genuinely_new_C19",
        },
        "accepted_round19_cover": {
            "lower_piece": "rho0<rho<rho_c and L(rho)<K<=d",
            "high_closed_piece": "rho_c<=rho<=7/8 and z_rho<=K<=k6(rho)",
            "rho0": "1/sqrt(337)",
            "L": "1/(2rho)",
            "d": "sqrt(337)/2",
            "z_rho": "pi/(1-rho)",
            "k6_squared": "z_rho^2+42",
            "included_new_frequency_faces": ["K=d", "K=k6(rho)"],
        },
        "genuinely_new_C19": {
            "lower_piece": "rho0<rho<rho_c and L(rho)<K<=d",
            "high_piece": "rho_c<=rho<7/8 and k5(rho)<K<=k6(rho)",
            "old_face_owners": ["K=L(rho)", "K=k5(rho)", "rho=7/8"],
        },
        "analytic_residual": {
            "name": "D19",
            "small_hole_piece": "rho_*<rho<=rho0 and L(rho)<K<U(rho)",
            "middle_piece": "rho0<rho<rho_c and d<K<U(rho)",
            "high_piece": "rho_c<=rho<7/8 and k6(rho)<K<U(rho)",
            "all_frequency_faces": "strict",
            "rho0_assignment": "small_hole_piece",
            "rho_c_assignment": "high_piece",
        },
        "theorem_wise_uncovered": {
            "name": "U19",
            "formula": "U19=D19",
            "reason": "B0 and B1 were already subsets of A18",
        },
        "face_owners": {
            "rho=rho_*": "complete small-hole endpoint; outside D19",
            "rho=rho0": "small-hole residual piece; L=d and added lower fiber empty",
            "rho=rho_c": "high residual piece; accepted high band owns through k6",
            "rho=7/8": "complete thin endpoint; outside D19",
            "K=L(rho), rho<=rho0": "inherited high-angular owner",
            "K=d, rho0<rho<rho_c": "Round 19 lower staircase owner",
            "K=k6(rho), rho>=rho_c": "Round 19 high staircase owner",
            "K=U(rho)": "active inherited H0, K0, or seam-54 owner",
            "K=295^2": "Round 16 all-ratio high-frequency owner",
        },
        "certified_regressions": {
            "B0": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["67/10", "168/25"],
                "relation": "B0 subset C17 subset A18 subset A19",
            },
            "B1": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["168/25", "673/100"],
                "relation": "B1 subset C17 subset A18 subset A19",
            },
            "uncovered_formula": "U19=D19; neither box is subtracted again",
        },
        "ratio_interfaces": [
            "rho=rho_* (complete endpoint outside D19)",
            "rho=rho0 (assigned to first D19 piece; L=d)",
            "rho=rho_HK (shared inherited H0=K0 upper face)",
            "rho=omega0 (H0 eligibility ends; K0 active)",
            "rho=rho_c (assigned to high-above-k6 piece)",
            "rho=1/2 (continuous inherited K0 formula interface)",
            "rho=5/6 (inherited seam begins inclusively)",
            "rho=7/8 (complete endpoint outside D19)",
        ],
        "scope": {
            "round20_candidate_encoded": False,
            "new_spectral_estimate": False,
            "residual_nonempty_witness": ["1/2", "30"],
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
        Fraction(1, 20),
        Fraction(12),
        "analytic_residual_uncovered",
        "small-hole-through-rho0",
    )
    passed.append("first exact D19 piece")

    _require_status(
        Fraction(1, 10),
        Fraction(10),
        "analytic_residual_uncovered",
        "middle-above-d",
    )
    passed.append("middle exact D19 piece")

    _require_status(
        Fraction(1, 2),
        Fraction(30),
        "analytic_residual_uncovered",
        "high-above-k6",
    )
    passed.append("high exact D19 piece and nonempty witness")

    lower = _require_status(Fraction(1, 10), Fraction(9), "analytic_covered")
    assert any("lower-ratio-round19" in item for item in lower.analytic_reasons)
    passed.append("accepted Round 19 lower band")

    high = _require_status(Fraction(1, 2), Fraction(9), "analytic_covered")
    assert any("high-ratio-round19" in item for item in high.analytic_reasons)
    passed.append("accepted Round 19 high band")

    assert c19_membership_from_signs(1, -1, 1, 0, -1, -1, rho_le_thin=True)
    assert c19_membership_from_signs(1, 0, 1, -1, 0, 0, rho_le_thin=True)
    passed.append("included d and k6 faces with rho_c assigned high")

    assert d19_membership_from_signs(1, 1, 0, -1, 1, 0, 1, rho_lt_thin=True)
    assert not d19_membership_from_signs(1, 1, 1, -1, 1, 0, 1, rho_lt_thin=True)
    assert not d19_membership_from_signs(1, 1, 1, 0, 1, -1, 0, rho_lt_thin=True)
    passed.append("rho0 ownership and strict new frequency faces")

    for rho, k, certificate in (
        (B0_RHO_LO, B0_K_LO, "round8-certified-pilot-B0"),
        (B0_RHO_HI, B0_K_HI, "round8-certified-pilot-B0"),
        (B1_RHO_LO, B1_K_LO, "round17-certified-pilot-B1"),
        (B1_RHO_HI, B1_K_HI, "round17-certified-pilot-B1"),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert certificate in result.certified_regression_reasons
    passed.append("B0 and B1 retained and analytically absorbed")

    point = (Fraction(1, 2), Fraction(30))
    assert theorem_uncovered_decision(*point) == normalized_d19_decision(*point)
    passed.append("theorem-wise uncovered set equals D19")

    _require_status(Fraction(1, 100), Fraction(1), "outside_I19")
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
