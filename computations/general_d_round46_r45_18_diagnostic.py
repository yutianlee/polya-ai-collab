#!/usr/bin/env python3
"""Round 46 lead diagnostics for the complete-owner R45.18 attempt.

The exact-owner records are reconstructed by the audited Round-44/45 engine.
This program adds the literal R45.18 margin and the correlated lower scalar
F_strong derived in the companion report.  Finite positive sweeps are
diagnostics only.  Directed classifications belong to the independent
Round-46 Prompt-C program.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

import mpmath as mp

import general_d_round44_independent_gate_b_search as r44
import general_d_round45_support_sign_diagnostic as r45


DEFAULT_DPS = 100
SEED = 4606


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def encode(value: Any, digits: int = 38) -> Any:
    if isinstance(value, mp.mpf):
        return mp.nstr(value, digits)
    if isinstance(value, dict):
        return {str(k): encode(v, digits) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v, digits) for v in value]
    return value


def closed_j(q: mp.mpf) -> mp.mpf:
    a = mp.acos(q / (q + 1))
    return (((q + 1) ** 2 + 2 * q**2) * a - 3 * q * mp.sqrt(2 * q + 1)) / (2 * mp.pi)


def added_metrics(record: r44.HPRecord, dps: int = DEFAULT_DPS) -> dict[str, mp.mpf]:
    """Literal R45.18 and the proved correlated lower reduction."""

    require(record.owner, f"record is not an exact owner: {record.reasons}")
    with mp.workdps(dps):
        d = record.data
        q = mp.mpf(d["q"])
        mu = mp.mpf(d["mu"])
        r = mp.mpf(d["r"])
        x = mp.mpf(d["x"])
        K = mp.mpf(d["K"])
        t = mp.mpf(d["t"])
        beta = mp.mpf(d["beta"])
        B0 = mp.mpf(d["B0"])
        p = mp.mpf(record.p)
        m = mp.mpf(record.m)
        drho = mp.mpf(d["d"])
        zeta = mp.mpf(d["zeta"])
        W = mp.mpf(d["W"])
        drop = mp.mpf(d["j"]) + mp.mpf(d["ep"]) + mp.mpf(d["h"])

        phi = mp.pi * beta
        a = mp.acos(q / mu)
        Ur = mp.sqrt(mu**2 - r**2)
        Ux = mp.sqrt(mu**2 - x**2)
        Uq = mp.sqrt(mu**2 - q**2)
        R1 = (Ur - Ux) / (Ux - Uq)
        quotient_floor = (phi - a) * mp.tan(a) / mp.pi
        action_exact = p * R1 * drop
        action_lower = p * (Ur - Ux) * quotient_floor
        quotient_slack = drop / (Ux - Uq) - quotient_floor

        J = closed_j(q)
        phase_exact = B0 * zeta + 9 / (16 * beta) - J
        phase_wall = q * (mp.tan(phi) - phi) * (mp.pi - 2 * phi) / (2 * mp.pi * phi)
        phase_slack = phase_exact - phase_wall - mp.mpf(41) / 40

        old = mp.pi**2 * B0 / (K * t**3 * mp.sin(t)) * (W / 2 - B0 / 4 + mp.mpf(1) / 48)
        top = 9 / (64 * mp.pi * mp.sqrt(K**2 - q**2) * beta**3)
        curvature = p**3 / (6 * mp.pi) * (
            1 / Ur - 1 / mp.sqrt(K**2 - r**2)
        )
        half_loss = (p - drho * m) / 2
        literal_margin = action_exact + old + phase_exact + top + curvature - half_loss
        f_strong = action_lower + phase_wall + drho * m / 2 - p / 2 + mp.mpf(41) / 40
        decomposition_residual = literal_margin - f_strong - (
            (action_exact - action_lower) + old + phase_slack + top + curvature
        )

        inherited = r45.round45_metrics(record, dps)
        require(
            abs(literal_margin - inherited["remaining_terminal_action_drop_signed"])
            < mp.power(10, -(dps - 20)),
            "literal R45.18 reconstruction disagrees with Round-45 ledger",
        )
        require(quotient_slack > 0, "inverse-action quotient lower bound failed")
        require(phase_slack > 0, "phase/root lower bound failed")
        require(abs(decomposition_residual) < mp.power(10, -(dps - 20)), "F_strong ledger residual")

        return {
            "R45.18_margin": +literal_margin,
            "F_strong": +f_strong,
            "margin_minus_F_strong": +(literal_margin - f_strong),
            "quotient_slack": +quotient_slack,
            "phase_slack": +phase_slack,
            "old_level_payment": +old,
            "top_payment": +top,
            "shelf_curvature": +curvature,
            "decomposition_residual": +decomposition_residual,
            "S": +mp.mpf(record.S),
        }


def exact_fixture(r2: int, p: int, m: int, B: int, label: str, dps: int) -> tuple[r44.HPRecord, dict[str, mp.mpf]]:
    proposal = r45.candidate(r2, p, m, B, label)
    record = r44.evaluate_hp(proposal, dps)
    require(record.owner, f"{label} ceased to be an owner: {record.reasons}")
    return record, added_metrics(record, dps)


def small_owner_sweep(dps: int) -> dict[str, Any]:
    """A deliberately finite lead sweep; Prompt C performs the broad search."""

    proposals = 0
    loose = []
    for r2 in list(range(2, 17, 2)) + list(range(3, 18, 2)):
        for p in range(3, 31):
            for m in range(1, 16):
                for B in range(2, 11):
                    proposals += 1
                    candidate = r44.float_candidate("round46-lead-small", r2, p, m, B)
                    if candidate is not None:
                        loose.append(candidate)

    owners: list[tuple[r44.HPRecord, dict[str, mp.mpf]]] = []
    seen: set[tuple[int, int, int, int]] = set()
    for candidate in loose:
        if candidate.key in seen:
            continue
        seen.add(candidate.key)
        record = r44.evaluate_hp(candidate, dps)
        if record.owner:
            owners.append((record, added_metrics(record, dps)))

    require(owners, "small sweep found no exact owners")
    minimum = min(owners, key=lambda item: item[1]["R45.18_margin"])
    min_f = min(owners, key=lambda item: item[1]["F_strong"])
    negatives = [item for item in owners if item[1]["R45.18_margin"] < 0]
    return {
        "proposals": proposals,
        "binary64_shortlist": len(loose),
        "exact_owners": len(owners),
        "negative_R45.18": len(negatives),
        "minimum": {
            "key": minimum[0].key,
            "grid": minimum[0].grid,
            "metrics": minimum[1],
        },
        "minimum_F_strong": {
            "key": min_f[0].key,
            "grid": min_f[0].grid,
            "metrics": min_f[1],
        },
    }


@lru_cache(maxsize=None)
def phi_float(q: float, B0: int) -> float:
    v = B0 + 0.75
    lo, hi = 0.0, math.pi / 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if q * (math.tan(mid) - mid) < math.pi * v:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def relaxed_f_strong(r: float, p: float, m: float, B0: int) -> tuple[float, float]:
    q = r + p + m
    phi = phi_float(float(q), int(B0))
    a = math.acos(q / (q + 1))
    t = math.acos(math.cos(phi) / math.cos(a))
    drho = 1 - 2 * t / math.pi
    Ur = math.sqrt((q + 1) ** 2 - r**2)
    Ux = math.sqrt((q + 1) ** 2 - (q - m) ** 2)
    action = p * (Ur - Ux) * (phi - a) * math.tan(a) / math.pi
    phase = q * (math.tan(phi) - phi) * (math.pi - 2 * phi) / (2 * math.pi * phi)
    return action + phase + drho * m / 2 - p / 2 + 41 / 40, p - drho * m


def relaxed_scalar_sweep(random_count: int) -> dict[str, Any]:
    """Search the larger radial/hard geometry, not the exact owner."""

    rows: list[tuple[float, tuple[float, float, float, int]]] = []
    proposals = 0
    # A directed-by-formula architectural probe supplied by the independent
    # symbolic audit.  It obeys the basic radial/hard inequalities but fails
    # the common-shelf and hard-E owner conditions.
    for r, p, m, B0 in ((8_886_110.0, 2935.0, 254.0, 1),):
        proposals += 1
        value, hard = relaxed_f_strong(r, p, m, B0)
        if hard > 11 / 5:
            rows.append((value, (r, p, m, B0)))
    for q in range(5, 301):
        for r in (1.0, 1.5, 2.0, 3.0, 5.0, 10.0):
            for m in range(1, min(25, int(q - r - 3)) + 1):
                p = q - r - m
                if p < 3:
                    continue
                for B0 in (1, 2, 5, 20, 100):
                    proposals += 1
                    value, hard = relaxed_f_strong(r, p, float(m), B0)
                    if hard > 11 / 5:
                        rows.append((value, (r, p, float(m), B0)))

    rng = random.Random(SEED)
    for _ in range(random_count):
        r = rng.choice((1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 50.0))
        p = float(rng.randint(3, 500))
        m = float(rng.randint(1, 150))
        B0 = rng.choice((1, 2, 3, 5, 10, 30, 100, 300))
        proposals += 1
        value, hard = relaxed_f_strong(r, p, m, B0)
        if hard > 11 / 5:
            rows.append((value, (r, p, m, B0)))

    require(rows, "relaxed scalar sweep was empty")
    best = min(rows, key=lambda row: row[0])
    return {
        "scope": "radial and hard inequalities only; shelf/activity/inverse ownership not imposed",
        "proposals": proposals,
        "admissible": len(rows),
        "negative_F_strong": sum(value < 0 for value, _ in rows),
        "minimum_F_strong": best[0],
        "minimum_tuple_r_p_m_B0": best[1],
        "negative_examples_are_not_exact_owners": True,
        "classification": "finite diagnostic only",
    }


def wall_geometry_margin(q: mp.mpf, p: int, m: int, B0: int) -> mp.mpf:
    """Literal normalized margin on the continuous wall; owner labels omitted."""

    v = mp.mpf(B0) + mp.mpf(3) / 4
    lo = mp.mpf(0)
    hi = mp.pi / 2 - mp.eps
    for _ in range(max(300, 3 * mp.mp.prec)):
        mid = (lo + hi) / 2
        if q * (mp.tan(mid) - mid) < mp.pi * v:
            lo = mid
        else:
            hi = mid
    phi = (lo + hi) / 2
    mu = q + 1
    r = q - p - m
    x = q - m
    a = mp.acos(q / mu)
    t = mp.acos(mp.cos(phi) / mp.cos(a))
    K = q / mp.cos(phi)
    beta = phi / mp.pi
    drho = 1 - 2 * t / mp.pi
    zeta = mp.pi / (2 * t) - 1
    W = mu / mp.pi * (mp.tan(t) - t)
    Ur, Ux, Uq = (mp.sqrt(mu**2 - z**2) for z in (r, x, q))
    R1 = (Ur - Ux) / (Ux - Uq)

    def action(z: mp.mpf) -> mp.mpf:
        return r44.ball_action(K, z) - r44.ball_action(mu, z)

    drop = action(x) - action(q)
    old = mp.pi**2 * B0 / (K * t**3 * mp.sin(t)) * (W / 2 - mp.mpf(B0) / 4 + mp.mpf(1) / 48)
    phase = B0 * zeta + 9 / (16 * beta) - closed_j(q)
    top = 9 / (64 * mp.pi * mp.sqrt(K**2 - q**2) * beta**3)
    curvature = p**3 / (6 * mp.pi) * (1 / Ur - 1 / mp.sqrt(K**2 - r**2))
    return p * R1 * drop + old + phase + top + curvature - (p - drho * m) / 2


def wall_derivative_diagnostics(dps: int) -> list[dict[str, Any]]:
    """Show that wall geometry alone does not make the full derivative one-signed."""

    with mp.workdps(dps):
        rows = []
        for q, p, m, B0 in ((mp.mpf(5), 3, 1, 1), (mp.mpf(100), 20, 1, 1)):
            derivative = mp.diff(lambda z: wall_geometry_margin(z, p, m, B0), q)
            rows.append({
                "q_p_m_B0": [q, p, m, B0],
                "r": q - p - m,
                "margin": wall_geometry_margin(q, p, m, B0),
                "d_margin_dq": derivative,
                "scope": "continuous exact wall and radial inequalities; not asserted to be a fixed exact owner component",
            })
        require(rows[0]["d_margin_dq"] > 0 and rows[1]["d_margin_dq"] < 0, "expected derivative sign change missing")
        return rows


def fixture_rows(dps: int) -> list[dict[str, Any]]:
    specs = (
        (2, 3, 1, 2, "Round44-minimum"),
        (3, 3, 1, 2, "half-grid-minimum"),
        (2, 6, 11, 19, "Round45-lead-CF"),
        (3, 6, 7, 5, "Round45-clean-room-CF"),
        (33128, 19, 1, 2, "large-radius-CF"),
        (5, 4, 1, 2, "near-E-star"),
        (3, 3, 6, 13, "near-hard-face"),
    )
    rows = []
    for r2, p, m, B, label in specs:
        record, metrics = exact_fixture(r2, p, m, B, label, dps)
        rows.append({
            "label": label,
            "key_r2_p_m_B": record.key,
            "grid": record.grid,
            "f_B_j": [record.data["f"], record.B, record.data["j"]],
            "metrics": metrics,
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--random", type=int, default=20_000)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    fixtures = fixture_rows(args.dps)
    lead_sweep = small_owner_sweep(args.dps)
    relaxed = relaxed_scalar_sweep(args.random)
    derivatives = wall_derivative_diagnostics(args.dps)

    require(all(mp.mpf(row["metrics"]["R45.18_margin"]) > 0 for row in fixtures), "fixture negative")
    require(lead_sweep["negative_R45.18"] == 0, "lead sweep found a negative requiring directed replay")

    payload = {
        "program": "general_d_round46_r45_18_diagnostic.py",
        "logical_strength": "finite high-precision diagnostics only; no positive coverage certificate",
        "exact_owner_fixtures": fixtures,
        "lead_small_owner_sweep": lead_sweep,
        "relaxed_F_strong_sweep": relaxed,
        "wall_derivative_diagnostics": derivatives,
        "coefficient_regressions": {
            "old_7_over_48": "exact in Mathematica replay",
            "top_9_over_64": "exact in Mathematica replay",
            "one_over_16beta": "exact bookkeeping identity in Mathematica replay",
            "Round27_43_44_45_and_directed_classifications": "independent Prompt-C evaluator",
        },
        "classification": "no counterexample found; F_strong remains unsigned analytically",
    }
    output = json.dumps(encode(payload), indent=2, sort_keys=True)
    print(output)
    if args.json is not None:
        args.json.write_text(output + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
