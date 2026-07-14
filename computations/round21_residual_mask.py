#!/usr/bin/env python3
"""Certified set classifier for the exact accepted Round 20 shell residual.

This module imports :mod:`computations.round20_residual_mask` as the opaque
accepted ``A19`` classifier and adds only the promoted Round 20 cover: the
complete lower part of ``D19``, the closed staircase through ``k_11``, and
the all-frequency optical theorem from ``rho=39/50``.  It independently
evaluates the normalized one-piece residual

    D20 = {rho_c <= rho < 39/50, k_11(rho) < K < K_0(rho)=U(rho)}.

This is set bookkeeping.  It contains no Round 21 certificate, candidate
theorem, or proposed successor residual.  Irrational comparisons use the
accepted precision-escalated Arb policy and return ``indeterminate`` when a
material face cannot be decided.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable

try:
    from computations import round20_residual_mask as r20
except ImportError:  # pragma: no cover - direct script execution
    import round20_residual_mask as r20


SCHEMA = "polya-shell-round21-residual-mask-v0.1"
BASELINE_COMMIT = "e739a1cfcc5ce6647d70f2ddbc09598da4f496aa"

RHO_OPTICAL = Fraction(39, 50)
RHO_THIN = Fraction(7, 8)

B0_RHO_LO = r20.B0_RHO_LO
B0_RHO_HI = r20.B0_RHO_HI
B0_K_LO = r20.B0_K_LO
B0_K_HI = r20.B0_K_HI

B1_RHO_LO = r20.B1_RHO_LO
B1_RHO_HI = r20.B1_RHO_HI
B1_K_LO = r20.B1_K_LO
B1_K_HI = r20.B1_K_HI

_LOWER_D19_PIECES = frozenset(
    {"small-hole-through-rho0", "middle-above-d"}
)


@dataclass(frozen=True)
class SetDecision:
    """A certified tri-state set decision and its supporting signs."""

    membership: bool | None
    piece: str | None
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[r20.r19.r18.r17.SignRecord, ...]


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
    sign_records: tuple[r20.r19.r18.r17.SignRecord, ...]


def qtext(value: Fraction) -> str:
    return r20.qtext(value)


def parse_fraction(text: str) -> Fraction:
    return r20.parse_fraction(text)


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
) -> r20.r19.r18.r17.SignRecord:
    sign = 1 if value > 0 else (-1 if value < 0 else 0)
    exact = qtext(value)
    return r20.r19.r18.r17.SignRecord(label, sign, 0, f"[{exact}, {exact}]")


def _rho_c_sign(rho: Fraction) -> r20.r19.r18.r17.SignRecord:
    return r20._rho_c_sign(rho)


def _rho_optical_sign(rho: Fraction) -> r20.r19.r18.r17.SignRecord:
    """Return the exact sign of ``rho-39/50``."""

    return _exact_sign_record("50*rho-39", 50 * rho - 39)


def _z_lower_sign(
    rho: Fraction, k: Fraction
) -> r20.r19.r18.r17.SignRecord:
    return r20._z_lower_sign(rho, k)


def _k11_upper_sign(
    rho: Fraction, k: Fraction
) -> r20.r19.r18.r17.SignRecord:
    """Return the sign of ``k_11(rho)^2-K^2`` without a square root."""

    core = r20.r19.r18.r17
    return core.certified_sign(
        "pi^2+(132-K^2)(1-rho)^2",
        lambda: core.arb.pi() ** 2
        + core.qball((Fraction(132) - k * k) * (1 - rho) ** 2),
    )


def _k0_upper_sign(
    rho: Fraction, k: Fraction
) -> r20.r19.r18.r17.SignRecord:
    """Return the sign of ``K_0(rho)-K`` by outward Arb evaluation."""

    core = r20.r19.r18.r17
    return core.certified_sign(
        "K_0(rho)-K",
        lambda: core.k0_ball(rho) - core.qball(k),
    )


def round20_cover_membership_from_signs(
    lower_d19_membership: bool | None,
    rho_c_sign: int | None,
    z_lower_sign: int | None,
    k11_upper_sign: int | None,
    rho_optical_sign: int,
    *,
    rho_le_thin: bool,
) -> bool | None:
    """Evaluate the three accepted Round 20 theorem domains.

    ``lower_d19_membership`` represents membership in the two accepted
    lower pieces of ``D19``.  The staircase includes all equality faces in
    ``rho_c<=rho<=7/8`` and ``z_rho<=K<=k_11(rho)``.  The optical theorem
    includes ``rho=39/50`` and every ``K>=0``; it is not restricted to the
    historical compact interval.
    """

    staircase = _tri_and(
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k11_upper_sign is None else k11_upper_sign >= 0,
    )
    optical = rho_optical_sign >= 0
    return _tri_or(lower_d19_membership, staircase, optical)


def _round20_cover_piece_from_signs(
    lower_d19_membership: bool | None,
    rho_c_sign: int | None,
    z_lower_sign: int | None,
    k11_upper_sign: int | None,
    rho_optical_sign: int,
    *,
    rho_le_thin: bool,
) -> tuple[bool | None, str | None]:
    staircase = _tri_and(
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k11_upper_sign is None else k11_upper_sign >= 0,
    )
    optical = rho_optical_sign >= 0
    membership = _tri_or(lower_d19_membership, staircase, optical)

    # The accepted bookkeeping assigns the rho=39/50 face to the optical
    # theorem even where the staircase overlaps it.
    if optical:
        return membership, "all-frequency-optical"
    if lower_d19_membership is True:
        return membership, "complete-d19-lower"
    if staircase is True:
        return membership, "closed-k11-staircase"
    return membership, None


def accepted_round20_cover_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify only the accepted Round 20 cover added to opaque ``A19``."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    d19 = r20.normalized_d19_decision(rho, k)
    if d19.membership is None:
        lower_d19: bool | None = None
    elif d19.membership is False:
        lower_d19 = False
    else:
        lower_d19 = d19.piece in _LOWER_D19_PIECES

    rho_c = _rho_c_sign(rho)
    z_lower = _z_lower_sign(rho, k)
    k11_upper = _k11_upper_sign(rho, k)
    optical = _rho_optical_sign(rho)
    membership, piece = _round20_cover_piece_from_signs(
        lower_d19,
        rho_c.sign,
        z_lower.sign,
        k11_upper.sign,
        optical.sign,
        rho_le_thin=rho <= RHO_THIN,
    )
    records = d19.sign_records + (rho_c, z_lower, k11_upper, optical)
    unresolved = (
        _deduplicate(
            list(d19.unresolved_comparisons)
            + [
                record.label
                for record in (rho_c, z_lower, k11_upper)
                if record.sign is None
            ]
        )
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def d20_membership_from_signs(
    rho_c_sign: int | None,
    rho_optical_sign: int,
    k11_upper_sign: int | None,
    k0_upper_sign: int | None,
) -> bool | None:
    """Evaluate the exact one-piece ``D20`` predicate.

    A nonnegative ``rho_c_sign`` includes the left ratio face.  A negative
    ``rho_optical_sign`` excludes ``rho=39/50``.  Negative
    ``k11_upper_sign`` means ``K>k_11`` and positive ``k0_upper_sign`` means
    ``K<K_0=U``.  Thus both frequency equality faces are excluded.
    """

    return _tri_and(
        None if rho_c_sign is None else rho_c_sign >= 0,
        rho_optical_sign < 0,
        None if k11_upper_sign is None else k11_upper_sign < 0,
        None if k0_upper_sign is None else k0_upper_sign > 0,
    )


def normalized_d20_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify the exact strict one-piece formula for ``D20`` directly."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    rho_c = _rho_c_sign(rho)
    optical = _rho_optical_sign(rho)
    k11_upper = _k11_upper_sign(rho, k)
    k0_upper = _k0_upper_sign(rho, k)

    identity_records: tuple[r20.r19.r18.r17.SignRecord, ...] = tuple()
    if rho_c.sign is not None and rho_c.sign >= 0 and optical.sign < 0:
        # On the live interval rho_c<=rho<39/50, accepted exact branch
        # eligibility gives U=K0: rho_c>omega0 excludes H0 and
        # 39/50<5/6 excludes the seam branch.  Replaying the inherited
        # classifier supplies an executable consistency check.
        inherited_upper = r20.upper_floor_decision(rho, k)
        if inherited_upper.piece != "K0":
            raise AssertionError("accepted live upper floor is not K0")
        if k0_upper.sign is not None and inherited_upper.membership is not None:
            if inherited_upper.membership != (k0_upper.sign > 0):
                raise AssertionError("inherited U and direct K0 signs disagree")
        identity_records = inherited_upper.sign_records

    membership = d20_membership_from_signs(
        rho_c.sign,
        optical.sign,
        k11_upper.sign,
        k0_upper.sign,
    )
    piece = "one-piece-d20" if membership is True else None
    records = (rho_c, optical, k11_upper, k0_upper) + identity_records
    unresolved = (
        _deduplicate(
            record.label
            for record in (rho_c, k11_upper, k0_upper)
            if record.sign is None
        )
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def theorem_uncovered_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Return ``U20``; absorbed B0/B1 make it identical to ``D20``."""

    return normalized_d20_decision(rho, k)


def classify_point(rho: Fraction, k: Fraction) -> PointClassification:
    """Classify a rational point under accepted ``A20`` and exact ``D20``."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    old = r20.classify_point(rho, k)
    added = accepted_round20_cover_decision(rho, k)
    analytic = list(old.analytic_reasons)
    certified = list(old.certified_regression_reasons)
    mandatory_old_unresolved = "rho-rho_*" in old.unresolved_comparisons

    if old.status == "analytic_covered":
        status = "analytic_covered"
    elif added.membership is True and not mandatory_old_unresolved:
        analytic.append(f"combined-closure-round20:{added.piece}")
        status = "analytic_covered"
    elif old.status == "outside_I19":
        status = "outside_I20"
    elif old.status == "analytic_residual_uncovered" and added.membership is False:
        status = "analytic_residual_uncovered"
    else:
        status = "indeterminate"

    direct = normalized_d20_decision(rho, k)
    if status == "analytic_residual_uncovered":
        if direct.membership is None:
            status = "indeterminate"
        elif direct.membership is False:
            raise AssertionError("A20 complement disagrees with normalized D20")
    elif status in {"analytic_covered", "outside_I20"} and direct.membership is True:
        raise AssertionError("accepted A20 status intersects normalized D20")
    elif status == "indeterminate" and direct.membership is True:
        # The normalized conjunction can occasionally settle a residual
        # point when the inherited union retains an irrelevant unknown.
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
            "state/proof_obligations.yml": "313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd",
            "state/next_round_prompts.md": "61341748ef07a6e937f752140b407a83576ae69c62061c1c28ae488acf43e4d2",
            "state/lemma_packets/SHELL-rho-compact-round20.md": "a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8",
            "computations/round20_residual_mask.py": "5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2",
            "computations/tests/test_round20_residual_mask.py": "d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164",
            "rounds/polya-main/round_020/exploration/residual-mask-freeze.md": "172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7",
            "rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md": "b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f",
            "state/lemma_packets/SHELL-combined-closure-round20-claim.md": "e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61",
            "rounds/polya-main/round_020/exploration/candidate-claim-freeze.md": "aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87",
            "rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md": "819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467",
            "rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md": "01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room.md": "7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb",
            "rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md": "7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c",
            "rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md": "2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8",
            "computations/round20_verify_combined_closure.py": "086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5",
            "computations/tests/test_round20_verify_combined_closure.py": "4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md": "df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md": "6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae",
            "rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md": "4b7a7810a12177002f24a16ef60a206669e07fa29e80c3018d2b85add5d1099b",
            "rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md": "acea3818e562a8bc27496f1c727835f7a08e70ce60aaa28946fb8999ddf6c9cc",
            "sources/round20_bessel_zero_bounds.md": "2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3",
            "sources/round20_higher_radial_zero_bounds.md": "8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7",
            "sources/round20_k10_zero_bounds.md": "a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926",
            "sources/round20_k11_zero_bounds.md": "eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240",
            "sources/lorch_bessel_zeros.md": "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-adversarial-audit.md": "4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd",
            "rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md": "52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31",
            "rounds/polya-main/round_020/judge/judge-020.md": "3acd0b9aec2aaa52f791bd8656cf6b53327c11eed5f3c4c51fe8352bee9782fa",
            "rounds/polya-main/round_020/reviews/state-patch-final-audit.md": "9a4ef5abbdf06d54a0d3c22fc9ff3c87ab3b6f44830c378b1edc6368a23c677f",
            "rounds/polya-main/round_020/reviews/derived-state-final-audit.md": "9c7a0dc453eea72bc571b99a11743d23ab42d1910f18e2b20c1dd0780eb752f9",
            "rounds/polya-main/round_020/reviews/derived-state-replacement-audit.md": "671cee8be91964efe0294eba01494cf11065ddbafdad1cc8e9885520ff3e353c",
        },
        "derivation": {
            "base_classifier": "computations/round20_residual_mask.py",
            "base_interpretation": "opaque accepted A19",
            "operation": "A20=A19 union accepted_Round20_cover",
            "residual_operation": "D20=D19 minus genuinely_new_C20",
        },
        "accepted_round20_cover": {
            "lower_piece": "complete accepted D19 lower two pieces",
            "high_closed_piece": "rho_c<=rho<=7/8 and z_rho<=K<=k11(rho)",
            "optical_piece": "39/50<=rho<1 and K>=0",
            "included_faces": ["rho=rho_c", "K=k11(rho)", "rho=39/50"],
        },
        "genuinely_new_C20": {
            "lower_piece": "D19^low",
            "staircase_piece": "rho_c<=rho<7/8 and k6(rho)<K<=k11(rho)",
            "optical_piece": "39/50<=rho<7/8 and k11(rho)<K<U(rho)",
        },
        "analytic_residual": {
            "name": "D20",
            "ratio_piece": "rho_c<=rho<39/50",
            "frequency_piece": "k11(rho)<K<K0(rho)=U(rho)",
            "rho_c_assignment": "included in D20 strictly above k11",
            "rho_optical_assignment": "excluded; optical-owned",
            "frequency_faces": "both strict",
        },
        "upper_floor_identity": {
            "formula": "U(rho)=K0(rho) on rho_c<=rho<39/50",
            "H0_ineligible": "rho>=rho_c>omega0",
            "seam_ineligible": "rho<39/50<5/6",
        },
        "theorem_wise_uncovered": {
            "name": "U20",
            "formula": "U20=D20",
            "reason": "B0 and B1 were already subsets of A19 subset A20",
        },
        "face_owners": {
            "rho=rho_c": "D20 only above the closed k11 staircase",
            "rho=39/50": "Round 20 all-frequency optical theorem",
            "K=k11(rho)": "Round 20 closed staircase",
            "K=K0(rho)=U(rho)": "inherited fixed-rho high-energy owner",
            "rho=rho_*": "inherited complete small-hole endpoint",
            "rho=7/8": "inherited complete thin endpoint",
            "K=295^2": "Round 16 all-ratio high-frequency owner",
            "K=0 on optical ratios": "optical equality face",
        },
        "certified_regressions": {
            "B0": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["67/10", "168/25"],
                "relation": "B0 subset C17 subset A19 subset A20",
            },
            "B1": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["168/25", "673/100"],
                "relation": "B1 subset C17 subset A19 subset A20",
            },
            "uncovered_formula": "U20=D20; neither box is subtracted again",
        },
        "scope": {
            "round21_certificate_encoded": False,
            "round21_candidate_encoded": False,
            "successor_residual_proposed": False,
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

    for point in ((Fraction(1, 20), Fraction(12)), (Fraction(1, 10), Fraction(10))):
        result = _require_status(*point, "analytic_covered")
        assert any("complete-d19-lower" in item for item in result.analytic_reasons)
    passed.append("complete accepted D19 lower closure")

    stair = _require_status(Fraction(1, 2), Fraction(13), "analytic_covered")
    assert any("closed-k11-staircase" in item for item in stair.analytic_reasons)
    passed.append("closed staircase through k11")

    _require_status(
        Fraction(1, 2),
        Fraction(30),
        "analytic_residual_uncovered",
        "one-piece-d20",
    )
    passed.append("exact D20 witness")

    optical = _require_status(Fraction(39, 50), Fraction(30), "analytic_covered")
    assert any("all-frequency-optical" in item for item in optical.analytic_reasons)
    passed.append("inclusive optical ratio face")

    assert d20_membership_from_signs(0, -1, -1, 1) is True
    assert d20_membership_from_signs(1, 0, -1, 1) is False
    assert d20_membership_from_signs(1, -1, 0, 1) is False
    assert d20_membership_from_signs(1, -1, -1, 0) is False
    passed.append("all four D20 faces")

    for rho in (Fraction(7, 50), Fraction(1, 2), Fraction(77, 100)):
        inherited = r20.upper_floor_decision(rho, Fraction(30))
        assert inherited.piece == "K0"
    passed.append("U equals K0 on live rational samples")

    for rho, k, certificate in (
        (B0_RHO_LO, B0_K_LO, "round8-certified-pilot-B0"),
        (B0_RHO_HI, B0_K_HI, "round8-certified-pilot-B0"),
        (B1_RHO_LO, B1_K_LO, "round17-certified-pilot-B1"),
        (B1_RHO_HI, B1_K_HI, "round17-certified-pilot-B1"),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert certificate in result.certified_regression_reasons
    passed.append("B0 and B1 retained without subtraction")

    endpoint = _require_status(Fraction(7, 8), Fraction(30), "analytic_covered")
    assert "rho-one-endpoint-round16" in endpoint.analytic_reasons
    high = _require_status(Fraction(1, 2), Fraction(600), "analytic_covered")
    assert "fixed-rho-high-energy" in high.analytic_reasons
    passed.append("inherited endpoint and high-energy owners")

    outside_optical = _require_status(Fraction(9, 10), Fraction(30), "analytic_covered")
    assert any("all-frequency-optical" in item for item in outside_optical.analytic_reasons)
    passed.append("optical theorem beyond historical compact interval")

    point = (Fraction(1, 2), Fraction(30))
    assert theorem_uncovered_decision(*point) == normalized_d20_decision(*point)
    passed.append("theorem-wise uncovered set equals D20")

    _require_status(Fraction(1, 100), Fraction(1), "outside_I20")
    passed.append("outside lower compact interval is not called residual")

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
