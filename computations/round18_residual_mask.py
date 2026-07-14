#!/usr/bin/env python3
"""Certified classifier for the exact post-Round-17 shell residual.

Round 18 does not rewrite the accepted primitive mask.  It imports the
frozen Round 17 classifier, adds the promoted closed first-angular band,
and independently checks the normalized two-piece residual.  Rational
comparisons are exact.  Every comparison involving pi or another accepted
irrational constant uses Arb precision escalation; an unresolved material
comparison produces ``indeterminate`` rather than a guessed side.

This module checks set bookkeeping only.  It proves no spectral estimate,
new analytic band, or finite Bessel certificate.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Iterable

try:
    from computations import round17_residual_mask as r17
except ImportError:  # pragma: no cover - direct script execution
    import round17_residual_mask as r17


SCHEMA = "polya-shell-round18-residual-mask-v0.1"

RHO_HALF = Fraction(1, 2)
RHO_SEAM = Fraction(5, 6)
RHO_THIN = Fraction(7, 8)

B0_RHO_LO = Fraction(999, 2000)
B0_RHO_HI = Fraction(1001, 2000)
B0_K_LO = Fraction(67, 10)
B0_K_HI = Fraction(168, 25)

B1_RHO_LO = Fraction(999, 2000)
B1_RHO_HI = Fraction(1001, 2000)
B1_K_LO = Fraction(168, 25)
B1_K_HI = Fraction(673, 100)


@dataclass(frozen=True)
class SetDecision:
    """A certified tri-state decision with the signs used to make it."""

    membership: bool | None
    piece: str | None
    unresolved_comparisons: tuple[str, ...]
    sign_records: tuple[r17.SignRecord, ...]


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
    sign_records: tuple[r17.SignRecord, ...]


def qtext(value: Fraction) -> str:
    return r17.qtext(value)


def parse_fraction(text: str) -> Fraction:
    return r17.parse_fraction(text)


def _deduplicate(items: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(items))


def _inside_b0(rho: Fraction, k: Fraction) -> bool:
    return B0_RHO_LO <= rho <= B0_RHO_HI and B0_K_LO <= k <= B0_K_HI


def _inside_b1(rho: Fraction, k: Fraction) -> bool:
    return B1_RHO_LO <= rho <= B1_RHO_HI and B1_K_LO <= k <= B1_K_HI


def c17_membership_from_signs(
    rho_c_sign: int | None,
    z_lower_sign: int | None,
    k2_upper_sign: int | None,
    *,
    rho_le_thin: bool,
) -> bool | None:
    """Evaluate the closed C17 band from certified face signs.

    The signs are respectively those of ``rho-rho_c``, ``K-z_rho``, and
    ``k_2(rho)^2-K^2``.  All three zero faces are included.
    """

    factors: tuple[bool | None, ...] = (
        rho_le_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign >= 0,
        None if k2_upper_sign is None else k2_upper_sign >= 0,
    )
    if any(value is False for value in factors):
        return False
    if any(value is None for value in factors):
        return None
    return True


def new_c17_membership_from_signs(
    rho_c_sign: int | None,
    z_lower_sign: int | None,
    k2_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> bool | None:
    """Evaluate the genuinely new part of C17 from certified signs.

    Unlike the closed theorem band, the old lower face ``K=z_rho`` and the
    old endpoint ``rho=7/8`` are excluded from the genuinely new set.
    """

    factors: tuple[bool | None, ...] = (
        rho_lt_thin,
        None if rho_c_sign is None else rho_c_sign >= 0,
        None if z_lower_sign is None else z_lower_sign > 0,
        None if k2_upper_sign is None else k2_upper_sign >= 0,
    )
    if any(value is False for value in factors):
        return False
    if any(value is None for value in factors):
        return None
    return True


def d17_piece_from_signs(
    rho_star_sign: int | None,
    upper_floor_sign: int | None,
    rho_c_sign: int | None,
    high_angular_lower_sign: int,
    k2_upper_sign: int | None,
    *,
    rho_lt_thin: bool,
) -> bool | None:
    """Evaluate the normalized D17 predicate from exact face signs.

    ``upper_floor_sign`` is the sign of ``U(rho)-K`` and
    ``high_angular_lower_sign`` is the exact sign of ``2*rho*K-1``.
    The post-band condition is ``k2_upper_sign < 0``.  Consequently all
    frequency sides of D17 are strict and ``rho=rho_c`` belongs to the
    post-k2 piece.
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
    if k2_upper_sign is None:
        return None
    return k2_upper_sign < 0


def _rho_c_sign(rho: Fraction) -> r17.SignRecord:
    return r17.certified_sign(
        "rho(1+2*pi)-1",
        lambda: r17.qball(rho) * (1 + 2 * r17.arb.pi()) - 1,
    )


def _z_lower_sign(rho: Fraction, k: Fraction) -> r17.SignRecord:
    return r17.certified_sign(
        "(1-rho)K-pi",
        lambda: r17.qball((1 - rho) * k) - r17.arb.pi(),
    )


def _k2_upper_sign(rho: Fraction, k: Fraction) -> r17.SignRecord:
    """Return the sign of k_2(rho)^2-K^2 without taking a square root."""

    return r17.certified_sign(
        "pi^2+(6-K^2)(1-rho)^2",
        lambda: r17.arb.pi() ** 2
        + r17.qball((Fraction(6) - k * k) * (1 - rho) ** 2),
    )


def c17_decision(rho: Fraction, k: Fraction) -> SetDecision:
    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    records = (
        _rho_c_sign(rho),
        _z_lower_sign(rho, k),
        _k2_upper_sign(rho, k),
    )
    membership = c17_membership_from_signs(
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


def upper_floor_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Decide the strict inequality K<U(rho) on the compact interior.

    The unique accepted H0=K0 switch is encoded by the sign of the frozen
    polynomial P.  Negative P selects H0, positive P selects K0, and zero
    is their shared face.  At an unresolved switch comparison, both upper
    values are checked and membership is returned only when their minimum
    has a certified side.  The inclusive Round 15 seam becomes the active
    upper owner at rho=5/6.
    """

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < RHO_THIN):
        raise ValueError("upper floor requires 0<rho<7/8")

    if rho >= RHO_SEAM:
        gap = Fraction(54) - k * (1 - rho) ** 2
        sign = 1 if gap > 0 else (-1 if gap < 0 else 0)
        record = r17.SignRecord(
            "54-K(1-rho)^2",
            sign,
            0,
            qtext(gap),
        )
        return SetDecision(sign > 0, "seam-54", tuple(), (record,))

    switch = r17.certified_sign(
        "P_HK(rho)", lambda: r17.hk_switch_polynomial_ball(rho)
    )
    if switch.sign == -1:
        gap = r17.certified_sign(
            "H_0(rho)-K", lambda: r17.h0_ball(rho) - r17.qball(k)
        )
        membership = None if gap.sign is None else gap.sign > 0
        unresolved = (gap.label,) if membership is None else tuple()
        return SetDecision(membership, "H0", unresolved, (switch, gap))

    if switch.sign in (0, 1):
        gap = r17.certified_sign(
            "K_0(rho)-K", lambda: r17.k0_ball(rho) - r17.qball(k)
        )
        membership = None if gap.sign is None else gap.sign > 0
        unresolved = (gap.label,) if membership is None else tuple()
        branch = "H0=K0" if switch.sign == 0 else "K0"
        return SetDecision(membership, branch, unresolved, (switch, gap))

    h_gap = r17.certified_sign(
        "H_0(rho)-K", lambda: r17.h0_ball(rho) - r17.qball(k)
    )
    k_gap = r17.certified_sign(
        "K_0(rho)-K", lambda: r17.k0_ball(rho) - r17.qball(k)
    )
    signs = (h_gap.sign, k_gap.sign)
    if any(sign is not None and sign <= 0 for sign in signs):
        membership: bool | None = False
    elif all(sign is not None and sign > 0 for sign in signs):
        membership = True
    else:
        membership = None
    unresolved = (
        tuple(record.label for record in (switch, h_gap, k_gap) if record.sign is None)
        if membership is None
        else tuple()
    )
    return SetDecision(
        membership,
        "H0/K0-switch-unresolved",
        unresolved,
        (switch, h_gap, k_gap),
    )


def normalized_d17_decision(rho: Fraction, k: Fraction) -> SetDecision:
    """Classify the exact two-piece normalized D17 formula directly."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    rho_star = r17.certified_sign(
        "rho-rho_*", lambda: r17.qball(rho) - r17.constants()[3]
    )
    if rho_star.sign is not None and rho_star.sign <= 0:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho >= RHO_THIN:
        return SetDecision(False, None, tuple(), (rho_star,))
    if rho_star.sign is None:
        return SetDecision(None, None, (rho_star.label,), (rho_star,))

    upper = upper_floor_decision(rho, k)
    rho_c = _rho_c_sign(rho)
    k2_upper = _k2_upper_sign(rho, k)
    exact_lower = 2 * rho * k - 1
    exact_lower_sign = 1 if exact_lower > 0 else (-1 if exact_lower < 0 else 0)

    membership = d17_piece_from_signs(
        rho_star.sign,
        None if upper.membership is None else (1 if upper.membership else -1),
        rho_c.sign,
        exact_lower_sign,
        k2_upper.sign,
        rho_lt_thin=rho < RHO_THIN,
    )
    if membership is True:
        piece = "lower-ratio" if rho_c.sign == -1 else "post-k2"
    else:
        piece = None
    records = (rho_star,) + upper.sign_records + (rho_c, k2_upper)
    unresolved = (
        _deduplicate(
            list(upper.unresolved_comparisons)
            + [record.label for record in (rho_c, k2_upper) if record.sign is None]
        )
        if membership is None
        else tuple()
    )
    return SetDecision(membership, piece, unresolved, records)


def classify_point(rho: Fraction, k: Fraction) -> PointClassification:
    """Classify a rational point under A17, D17, and the two old boxes."""

    if k < 0:
        raise ValueError("K must be nonnegative")
    if not (0 < rho < 1):
        raise ValueError("rho must satisfy 0 < rho < 1")

    old = r17.classify_point(rho, k)
    c17 = c17_decision(rho, k)
    analytic = list(old.analytic_reasons)
    certified = list(old.certified_reasons)
    if _inside_b0(rho, k) and "round8-certified-pilot-B0" not in certified:
        certified.append("round8-certified-pilot-B0")
    if _inside_b1(rho, k):
        certified.append("round17-certified-pilot-B1")

    mandatory_old_unresolved = "rho-rho_*" in old.unresolved_comparisons
    if old.status == "outside_I16":
        status = "outside_I17"
    elif old.status == "analytic_covered":
        status = "analytic_covered"
    elif c17.membership is True and not mandatory_old_unresolved:
        analytic.append("first-angular-band-round17")
        status = "analytic_covered"
    elif old.status == "indeterminate" or c17.membership is None:
        status = "indeterminate"
    else:
        status = "analytic_residual_uncovered"

    direct = normalized_d17_decision(rho, k)
    if status == "analytic_residual_uncovered":
        if direct.membership is None:
            status = "indeterminate"
        elif direct.membership is False:
            raise AssertionError("A17 complement disagrees with normalized D17")
    elif status == "analytic_covered" and direct.membership is True:
        raise AssertionError("A17 intersects normalized D17")

    residual_piece = direct.piece if status == "analytic_residual_uncovered" else None
    unresolved = _deduplicate(
        list(old.unresolved_comparisons)
        + list(c17.unresolved_comparisons)
        + (list(direct.unresolved_comparisons) if status == "indeterminate" else [])
    )
    records = old.sign_records + c17.sign_records + direct.sign_records

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
        "derivation": {
            "base_classifier": "computations/round17_residual_mask.py",
            "operation": "A17=A16 union closed_C17",
            "residual_operation": "D17=D16 minus C17",
        },
        "closed_C17": {
            "rho": "rho_c<=rho<=7/8",
            "K": "z_rho<=K<=k2(rho)",
            "rho_c": "1/(1+2*pi)",
            "z_rho": "pi/(1-rho)",
            "k2_squared": "z_rho^2+6",
            "faces": "all displayed faces included",
        },
        "new_C17": {
            "rho": "rho_c<=rho<7/8",
            "K": "z_rho<K<=k2(rho)",
            "old_face_owners": ["K=z_rho", "rho=7/8"],
        },
        "analytic_residual": {
            "name": "D17",
            "lower_ratio_piece": (
                "rho_*<rho<rho_c and 1/(2rho)<K<U(rho)"
            ),
            "post_band_piece": (
                "rho_c<=rho<7/8 and k2(rho)<K<U(rho)"
            ),
            "all_frequency_faces": "strict",
            "rho_c_assignment": "post_band_piece",
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
            "upper_faces": "included analytic owners; excluded from D17",
        },
        "certified_regressions": {
            "B0": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["67/10", "168/25"],
                "faces": "closed",
                "relation": "B0 subset C17",
            },
            "B1": {
                "rho": ["999/2000", "1001/2000"],
                "K": ["168/25", "673/100"],
                "faces": "closed",
                "relation": "B1 subset C17",
            },
            "uncovered_formula": "U17=D17; neither box is subtracted again",
        },
        "interfaces": [
            "rho=rho_* (complete old endpoint outside D17)",
            "rho=rho_HK (shared H0=K0 upper face)",
            "rho=omega_0 (small-hole open face; K0 remains active)",
            "rho=rho_c (assigned to post-k2 piece)",
            "rho=1/2 (continuous K0 formula interface)",
            "rho=5/6 (seam begins inclusively)",
            "rho=7/8 (complete old endpoint outside D17)",
            "K=1/(2rho) (old high-angular owner)",
            "K=z_rho (old phase-zero owner)",
            "K=k2(rho) (Round 17 first-angular-band owner)",
            "K=U(rho) (old inclusive upper owner)",
        ],
        "method_fact": {
            "name": "crude-cap-9 obstruction",
            "statement": (
                "immediately above k2 the crude cap rises from 4 to 9, "
                "but W(rho_c,k2(rho_c))<9"
            ),
            "scope": "rules out only that uniform coarse cap-payment continuation",
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

    _require_status(Fraction(7, 51), Fraction(4), "analytic_residual_uncovered", "lower-ratio")
    passed.append("lower-ratio D17 piece")

    _require_status(Fraction(11, 80), Fraction(5), "analytic_residual_uncovered", "post-k2")
    passed.append("post-k2 D17 piece")

    band = _require_status(Fraction(11, 80), Fraction(4), "analytic_covered")
    assert "first-angular-band-round17" in band.analytic_reasons
    passed.append("promoted C17 band")

    face = _require_status(Fraction(1, 16), Fraction(8), "analytic_covered")
    assert "high-angular" in face.analytic_reasons
    passed.append("inherited inclusive high-angular face")

    endpoint = _require_status(RHO_THIN, Fraction(0), "analytic_covered")
    assert "rho-one-endpoint-round16" in endpoint.analytic_reasons
    passed.append("complete thin endpoint")

    for rho, k in (
        (B0_RHO_LO, B0_K_LO),
        (B0_RHO_HI, B0_K_HI),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert "round8-certified-pilot-B0" in result.certified_regression_reasons
        assert "first-angular-band-round17" in result.analytic_reasons
    passed.append("B0 analytically subsumed with certificate retained")

    for rho, k in (
        (B1_RHO_LO, B1_K_LO),
        (B1_RHO_HI, B1_K_HI),
    ):
        result = _require_status(rho, k, "analytic_covered")
        assert "round17-certified-pilot-B1" in result.certified_regression_reasons
        assert "first-angular-band-round17" in result.analytic_reasons
    passed.append("B1 analytically subsumed with certificate retained")

    below_seam = upper_floor_decision(RHO_SEAM, Fraction(1943))
    seam_face = upper_floor_decision(RHO_SEAM, Fraction(1944))
    assert below_seam.membership is True and below_seam.piece == "seam-54"
    assert seam_face.membership is False and seam_face.piece == "seam-54"
    passed.append("strict residual side at inclusive seam face")

    left_switch = upper_floor_decision(Fraction(9, 100), Fraction(1))
    right_switch = upper_floor_decision(Fraction(1, 10), Fraction(1))
    assert left_switch.piece == "H0" and left_switch.membership is True
    assert right_switch.piece == "K0" and right_switch.membership is True
    passed.append("accepted unique H0=K0 branch switch")

    assert c17_membership_from_signs(0, 0, 0, rho_le_thin=True) is True
    assert new_c17_membership_from_signs(0, 0, 0, rho_lt_thin=True) is False
    passed.append("closed C17 faces and strict genuinely-new lower face")

    assert d17_piece_from_signs(1, 1, -1, 0, 1, rho_lt_thin=True) is False
    assert d17_piece_from_signs(1, 1, 0, 1, 0, rho_lt_thin=True) is False
    assert d17_piece_from_signs(1, 0, 1, 1, -1, rho_lt_thin=True) is False
    passed.append("all normalized D17 frequency faces are excluded")

    _require_status(Fraction(1, 100), Fraction(1), "outside_I17")
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
