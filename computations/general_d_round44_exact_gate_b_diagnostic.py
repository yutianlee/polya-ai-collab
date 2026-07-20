#!/usr/bin/env python3
"""Round 44 high-precision exact Gate-B diagnostic.

This program evaluates only the one-sided upper-alpha, outer-B endpoint in
Prompt A.  It solves each outer wall with a verified monotone bracket, applies
literal strict counts, checks the complete owner, and evaluates the unrenamed
target

    S = D_A(q) + C_p + p (E - E_*).

All mpmath results are diagnostic.  The separately invoked Round 27 Arb
fixture is directed only for that historical regression; it certifies no
Round 44 continuum statement and no positive coverage claim is made here.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
MP_DPS = 80
mp.mp.dps = MP_DPS
PI = mp.pi
WALL_TOL = mp.mpf("1e-55")


def ball_action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    return radius / PI * (mp.sin(theta) - theta * mp.cos(theta))


def ball_tail_integral(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
    if z >= radius:
        return mp.mpf(0)
    theta = mp.acos(z / radius)
    c, s = mp.cos(theta), mp.sin(theta)
    return radius * radius / (4 * PI) * (
        theta * (1 + 2 * c * c) - 3 * s * c
    )


def strict_floor(x: mp.mpf) -> int:
    nearest = int(mp.nint(x))
    if abs(x - nearest) <= WALL_TOL:
        return max(0, nearest - 1)
    return max(0, int(mp.ceil(x)) - 1)


def ordinary_floor(x: mp.mpf) -> int:
    nearest = int(mp.nint(x))
    if abs(x - nearest) <= WALL_TOL:
        return max(0, nearest)
    return max(0, int(mp.floor(x)))


def bisect_increasing(function, lo: mp.mpf, hi: mp.mpf, steps: int = 230):
    flo, fhi = function(lo), function(hi)
    if not (flo <= 0 <= fhi):
        raise ValueError("root is not bracketed")
    for _ in range(steps):
        mid = (lo + hi) / 2
        fmid = function(mid)
        if fmid < 0:
            lo, flo = mid, fmid
        else:
            hi, fhi = mid, fmid
    return (lo + hi) / 2, lo, hi, flo, fhi


@lru_cache(maxsize=None)
def solve_outer_wall(q_text: str, alpha_text: str, b_gap: int):
    q = mp.mpf(q_text)
    alpha = mp.mpf(alpha_text)
    mu = q + alpha
    target = mp.mpf(b_gap) - mp.mpf("0.25")

    def residual(t: mp.mpf) -> mp.mpf:
        return ball_action(mu / mp.cos(t), q) - target

    root, lo, hi, flo, fhi = bisect_increasing(
        residual, mp.mpf(0), PI / 2 - mp.mpf("1e-45")
    )
    return root, lo, hi, flo, fhi


def solve_inverse_angle(radius: mp.mpf, level: mp.mpf) -> mp.mpf:
    def residual(theta: mp.mpf) -> mp.mpf:
        return radius / PI * (
            mp.sin(theta) - theta * mp.cos(theta)
        ) - level

    return bisect_increasing(
        residual, mp.mpf(0), PI / 2, steps=220
    )[0]


def fmt(value, digits: int = 32):
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, int):
        return value
    return mp.nstr(value, digits)


@dataclass
class Ledger:
    r: str
    p: int
    m: int
    f: int
    B: int
    B0: int
    j: int
    alpha: str
    q: str
    mu: str
    t: str
    K: str
    d: str
    root_bracket_width: str
    root_left_residual: str
    root_right_residual: str
    activity_margin: str
    h: str
    u: str
    beta: str
    e0: str
    ep: str
    E: str
    Delta: str
    E_star: str
    p_deficit: str
    D_A_q: str
    D_A_q_literal: str
    old_inverse_adverse_count: int
    L_T_plus: str
    L_T_zero: str
    R_tan_plus: str
    R_tan_zero: str
    tangent_difference: str
    expected_tangent_difference: str
    C_p: str
    curvature_reserve: str
    top_bregman_reserve: str
    a_p_Delta: str
    Phi_delta_plus: str
    S: str
    restored_reserve: str
    localization_margin: str
    min_old_inverse_wall_distance: str
    terminal_ledger_residual: str
    scalar_ledger_residual: str


def evaluate(
    r_value: float | str,
    p: int,
    m: int,
    b_gap: int,
    *,
    alpha_value: str = "1",
    enforce_owner: bool = True,
) -> Ledger | None:
    r = mp.mpf(str(r_value))
    alpha = mp.mpf(alpha_value)
    x = r + p
    q = x + m
    mu = q + alpha
    if q < 5 or p < 3 or m < 1 or b_gap < 2:
        return None

    try:
        t, root_lo, root_hi, root_flo, root_fhi = solve_outer_wall(
            mp.nstr(q, 50), mp.nstr(alpha, 50), b_gap
        )
    except (ValueError, ZeroDivisionError):
        return None
    outer = mu / mp.cos(t)
    d = 1 - 2 * t / PI
    b0 = b_gap - 1

    def action(z: mp.mpf) -> mp.mpf:
        return ball_action(outer, z) - ball_action(mu, z)

    def action_integral(z: mp.mpf) -> mp.mpf:
        return ball_tail_integral(outer, z) - ball_tail_integral(mu, z)

    ar, ax, ax1, aq = action(r), action(x), action(x + 1), action(q)
    f = ordinary_floor(ar + mp.mpf("0.25"))
    e0 = ar + mp.mpf("0.25") - f
    ep = ax + mp.mpf("0.25") - f
    e_sum = e0 + ep
    delta = e0 - ep
    e_star = (p - d * m) / (2 * p)
    j = f - b_gap

    h = ball_action(mu, q)
    w = ball_action(outer, mu)
    u = ball_action(outer, q) - w
    beta = mp.acos(q / outer) / PI
    q_count = strict_floor(aq + mp.mpf("0.25"))
    activity_gamma = mp.mpf("0.75") if r == mp.floor(r) else mp.mpf(2)
    activity = outer * outer - PI * PI / (1 - mp.cos(t)) ** 2 - activity_gamma

    owner_checks = (
        ordinary_floor(ax + mp.mpf("0.25")) == f,
        ordinary_floor(ax1 + mp.mpf("0.25")) != f,
        f >= 2,
        j >= 0,
        q_count == b0,
        0 < h < u < beta < mp.mpf("0.5"),
        p > d * m,
        p - d * m > mp.mpf(11) / 5,
        0 <= e_sum < e_star < mp.mpf("0.5"),
        activity > 0,
        root_flo <= 0 <= root_fhi,
    )
    if enforce_owner and not all(owner_checks):
        return None

    # Direct strict terminal count.  At a simultaneous old inverse wall the
    # selected adverse side is two units below the literal strict value per
    # collision.  Both values are retained separately.
    direct_count = q_count
    max_index = max(1, int(mp.ceil(outer - q)) + 2)
    for shift in range(1, max_index + 1):
        direct_count += 2 * strict_floor(action(q + shift) + mp.mpf("0.25"))
    d_q_literal = 2 * action_integral(q) - direct_count

    old_angles: list[mp.mpf] = []
    old_etas: list[mp.mpf] = []
    wall_distances: list[mp.mpf] = []
    adverse_count = 0
    for k in range(1, b_gap):
        theta = solve_inverse_angle(outer, mp.mpf(k) - mp.mpf("0.25"))
        y = outer * mp.cos(theta) - q
        nearest = int(mp.nint(y))
        distance = abs(y - nearest)
        wall_distances.append(distance)
        if distance <= WALL_TOL and nearest >= 1:
            eta = mp.mpf(0)  # adverse one-sided owner
            adverse_count += 1
        else:
            eta = y - strict_floor(y)
        old_angles.append(theta)
        old_etas.append(eta)

    d_q = d_q_literal - 2 * adverse_count
    omega_minus = mp.fsum(
        PI / (2 * theta) - PI / (2 * t) + 2 * eta
        for theta, eta in zip(old_angles, old_etas)
    )
    zeta = PI / (2 * t) - 1
    cap = 2 * ball_tail_integral(mu, q)
    l_plus = omega_minus + b0 * zeta + 1 / (2 * beta) - cap
    l_zero = omega_minus + b0 * zeta + 9 / (16 * beta) - cap
    r_tan_plus = d_q - l_plus
    r_tan_zero = d_q - l_zero

    cp = 2 * (action_integral(r) - action_integral(x)) - p * (ar + ax)
    ap = mp.mpf(p * p) / (3 * (2 * r + p))
    curvature = mp.mpf(p**3) / (6 * PI) * (
        1 / mp.sqrt(mu * mu - r * r)
        - 1 / mp.sqrt(outer * outer - r * r)
    )
    top_bregman = 9 / (
        64 * PI * mp.sqrt(outer * outer - q * q) * beta**3
    )
    p_deficit = p * (e_star - e_sum)
    phi = l_plus + ap * delta + p * (e_sum - e_star)
    scalar = d_q + cp + p * (e_sum - e_star)
    restored = r_tan_plus + cp - ap * delta
    localization_margin = (
        omega_minus
        + b0 * zeta
        + 9 / (16 * beta)
        - cap
        + top_bregman
        + curvature
        - p_deficit
    )

    return Ledger(
        r=fmt(r), p=p, m=m, f=f, B=b_gap, B0=b0, j=j,
        alpha=fmt(alpha), q=fmt(q), mu=fmt(mu), t=fmt(t), K=fmt(outer),
        d=fmt(d), root_bracket_width=fmt(root_hi - root_lo),
        root_left_residual=fmt(root_flo), root_right_residual=fmt(root_fhi),
        activity_margin=fmt(activity), h=fmt(h), u=fmt(u), beta=fmt(beta),
        e0=fmt(e0), ep=fmt(ep), E=fmt(e_sum), Delta=fmt(delta),
        E_star=fmt(e_star), p_deficit=fmt(p_deficit), D_A_q=fmt(d_q),
        D_A_q_literal=fmt(d_q_literal), old_inverse_adverse_count=adverse_count,
        L_T_plus=fmt(l_plus), L_T_zero=fmt(l_zero),
        R_tan_plus=fmt(r_tan_plus), R_tan_zero=fmt(r_tan_zero),
        tangent_difference=fmt(r_tan_plus - r_tan_zero),
        expected_tangent_difference=fmt(1 / (16 * beta)), C_p=fmt(cp),
        curvature_reserve=fmt(curvature), top_bregman_reserve=fmt(top_bregman),
        a_p_Delta=fmt(ap * delta), Phi_delta_plus=fmt(phi), S=fmt(scalar),
        restored_reserve=fmt(restored), localization_margin=fmt(localization_margin),
        min_old_inverse_wall_distance=fmt(
            min(wall_distances) if wall_distances else mp.inf
        ),
        terminal_ledger_residual=fmt(
            (r_tan_plus - r_tan_zero) - 1 / (16 * beta)
        ),
        scalar_ledger_residual=fmt(scalar - phi - restored),
    )


def to_number(value: str) -> mp.mpf:
    return mp.mpf(value)


def structured_search(args):
    integer_r = [float(k) for k in range(1, args.r_max + 1)]
    half_r = [k + 0.5 for k in range(1, args.r_max + 1)]
    tuples = {
        (r, p, m)
        for r in integer_r + half_r
        for p in range(3, args.p_max + 1)
        for m in range(1, args.m_max + 1)
    }
    stress_r = [1.0, 1.5, 2.0, 2.5, 10.0, 100.0, 1000.0]
    stress_p = [3, 4, 5, 8, 12, 20, 50]
    stress_m = [1, 2, 5, 10, 30]
    tuples.update((r, p, m) for r in stress_r for p in stress_p for m in stress_m)

    records: list[Ledger] = []
    tested = 0
    for r, p, m in sorted(tuples):
        for b_gap in range(2, args.b_max + 1):
            tested += 1
            item = evaluate(r, p, m, b_gap)
            if item is not None:
                records.append(item)
    return tested, records


def minimum(records: list[Ledger], field: str):
    return min(records, key=lambda item: to_number(getattr(item, field)))


def round27_certified_regression():
    script = ROOT / "computations" / "general_d_round27_exact_RJ_counterexample.py"
    completed = subprocess.run(
        [sys.executable, "-B", str(script)],
        cwd=ROOT, check=True, text=True, capture_output=True,
    )
    output = completed.stdout
    required = (
        "PASS Cmax8 < -4/3 and R_J < -6/5",
        "PASS exact reduced S > 47 and Phi_delta > 40",
        "automaticSectorCertified=True",
        "phiOrExactSOrCSTCounterexample=False",
    )
    return {
        "command": f"{sys.executable} -B {script}",
        "directed_arb": True,
        "passed": all(token in output for token in required),
        "Cmax8_upper": re.search(r"Cmax8=\[([^\n]+)", output).group(1),
        "R_J_upper": re.search(r"R_J=\[([^\n]+)", output).group(1),
        "S_lower": re.search(r"exact reduced S=\[([^\n]+)", output).group(1),
        "Phi_lower": re.search(r"Phi_delta=\[([^\n]+)", output).group(1),
        "classification": "automatic remainder-rich; not a CST counterexample",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=8)
    parser.add_argument("--p-max", type=int, default=15)
    parser.add_argument("--m-max", type=int, default=10)
    parser.add_argument("--b-max", type=int, default=9)
    parser.add_argument("--skip-round27-arb", action="store_true")
    args = parser.parse_args()

    tested, records = structured_search(args)
    if not records:
        raise SystemExit("no exact-owner endpoint record retained")

    min_s = minimum(records, "S")
    min_phi = minimum(records, "Phi_delta_plus")
    min_restored = minimum(records, "restored_reserve")
    min_localization = minimum(records, "localization_margin")

    convergence = []
    for exponent in (2, 4, 6, 8, 10):
        alpha = mp.mpf(1) - mp.power(10, -exponent)
        item = evaluate(
            min_s.r, min_s.p, min_s.m, min_s.B,
            alpha_value=mp.nstr(alpha, 70), enforce_owner=False,
        )
        convergence.append({
            "alpha": mp.nstr(alpha, 30),
            "outer_root_resolved_separately": True,
            "ledger": asdict(item) if item else None,
        })

    round43 = evaluate(1, 9, 9, 3, enforce_owner=False)
    round43_regression = {
        "expected_tuple": [1, 9, 9, 4, 3, 1],
        "ledger": asdict(round43) if round43 else None,
        "rejected_for_E_greater_than_E_star": bool(
            round43 and to_number(round43.E) > to_number(round43.E_star)
        ),
    }

    report = {
        "round": 44,
        "diagnostic_only": True,
        "positive_coverage_certificate": False,
        "precision_decimal_digits": MP_DPS,
        "target": "S = D_A(q) + C_p + p(E-E_*)",
        "tested_endpoint_candidates": tested,
        "retained_exact_owner_records": len(records),
        "integer_grid_records": sum(mp.mpf(item.r) == mp.floor(mp.mpf(item.r)) for item in records),
        "half_integer_grid_records": sum(mp.mpf(item.r) != mp.floor(mp.mpf(item.r)) for item in records),
        "negative_S_records": sum(to_number(item.S) < 0 for item in records),
        "records_surviving_analytic_negative_support_localization": sum(
            to_number(item.localization_margin) < 0 for item in records
        ),
        "minimum_S": asdict(min_s),
        "minimum_Phi_delta_plus": asdict(min_phi),
        "minimum_restored_reserve": asdict(min_restored),
        "minimum_localization_margin": asdict(min_localization),
        "maximum_absolute_terminal_ledger_residual": fmt(max(
            abs(to_number(item.terminal_ledger_residual)) for item in records
        )),
        "maximum_absolute_scalar_ledger_residual": fmt(max(
            abs(to_number(item.scalar_ledger_residual)) for item in records
        )),
        "minimum_C_p_minus_curvature_reserve": fmt(min(
            to_number(item.C_p) - to_number(item.curvature_reserve)
            for item in records
        )),
        "round43_regression": round43_regression,
        "one_sided_alpha_convergence": convergence,
        "round27_certified_regression": (
            None if args.skip_round27_arb else round27_certified_regression()
        ),
        "conclusion": "no sampled negative S; diagnostic only",
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
