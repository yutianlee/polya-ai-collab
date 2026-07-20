#!/usr/bin/env python3
"""Diagnostic-only Round 38 search on hard one-level gap faces.

The sampler is imported from the Round 27 exact-domain diagnostic, so the
integer and half-integer grids, dimension-labelled activity condition,
ordinary shelf owners, strict terminal owners, and literal/adverse inverse
wall samples are unchanged.  This file adds the Round 38 gap coordinates
and evaluates

    Gamma_gap, H_Delta, and the right-hand side of (R38.20).

All arithmetic is ordinary binary64.  Every reported minimum is finite-scan
theorem-design evidence only: this program neither proves nor certifies a
continuum sign.  Literal alpha=0 equal-count points are excluded.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
ROUND27_PATH = (
    ROOT / "computations" / "general_d_round27_exact_phi_hard_sector_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location("round27_round38_faces", ROUND27_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND27_PATH}")
R27 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R27
SPEC.loader.exec_module(R27)


CHECK_TOL = 8.0e-7
FACE_TOL = 2.0e-7
ADVERSE_FACE_TOL = 2.0e-3


@dataclass(frozen=True)
class GapFaceValue:
    """One finite diagnostic evaluation on the positive-alpha gap."""

    record: object
    grid: str
    b0: int
    j: int
    lam: float
    u: float
    sq: float
    chi: float
    h: float
    beta: float
    zeta: float
    count_phase: float
    ep: float
    delta: float
    m4: float
    xi_hat: float
    omega_minus: float
    omega_newest: float
    omega: float
    gamma_gap: float
    h_delta: float
    rhs_r3820: float
    phi_delta_plus: float
    exact_reduced_s: float
    max_coordinate_residual: float
    min_old_eta: float
    max_old_eta: float
    newest_y: float
    face_labels: tuple[str, ...]


def close_tolerance(*values: float) -> float:
    return CHECK_TOL * max(1.0, *(abs(value) for value in values))


def grid_label(r: float) -> str:
    doubled = round(2 * r)
    if abs(2 * r - doubled) > 2.0e-10:
        raise ArithmeticError("shift is on neither supported parity grid")
    if doubled % 2 == 0:
        return "integer_d4_activity"
    return "half_integer_d5_activity"


def quartic_payment(mu: float, outer: float, r: float, p: int) -> float:
    """Round 28 quartic shelf payment K_4."""

    x = r + p
    return (
        (mu ** (-1) - outer ** (-1)) * (x * x - r * r) / (2 * math.pi)
        + (mu ** (-3) - outer ** (-3))
        * (x**4 - r**4)
        / (24 * math.pi)
    )


def adjacent_ratio(mu: float, r: float, p: int, q: float) -> float:
    """Stable algebraic form of the Round 34 adjacent-action ratio R_1."""

    x = r + p
    ur = math.sqrt(max(0.0, mu * mu - r * r))
    ux = math.sqrt(max(0.0, mu * mu - x * x))
    uq = math.sqrt(max(0.0, mu * mu - q * q))
    return (
        (x * x - r * r)
        * (ux + uq)
        / ((q * q - x * x) * (ur + ux))
    )


def classify_faces(
    record: object,
    ep: float,
    aq: float,
    newest_y: float,
    old_ys: list[float],
    old_etas: list[float],
) -> tuple[str, ...]:
    labels: list[str] = []
    if ep <= FACE_TOL:
        labels.append("lower_shelf")
    if newest_y <= ADVERSE_FACE_TOL:
        labels.append("outer_B_gap_side_near")
    q_count_argument = aq + 0.25
    if abs(q_count_argument - round(q_count_argument)) <= FACE_TOL:
        labels.append("literal_Q_wall")
    if any(
        abs(y - round(y)) <= FACE_TOL and eta > 0.5
        for y, eta in zip(old_ys, old_etas)
    ):
        labels.append("literal_old_inverse_wall")
    if any(0.0 <= eta <= ADVERSE_FACE_TOL for eta in old_etas):
        labels.append("adverse_old_inverse_side_near")
    if record.alpha <= 1.001e-3:
        labels.append("lower_alpha_gap_side_near")
    if record.alpha >= 1 - 1.0e-5:
        labels.append("upper_alpha_gap_side_near")
    if not labels:
        labels.append("gap_interior")
    return tuple(labels)


def evaluate_gap_face(record: object) -> GapFaceValue:
    """Reconstruct and check one Round 38 positive-alpha gap record."""

    r, p, m, f = record.r, record.p, record.m, record.f
    alpha, t = record.alpha, record.t
    if not (0.0 < alpha < 1.0):
        raise ArithmeticError("alpha=0 equal-count point entered gap data")
    if p < 3:
        raise ArithmeticError("Round 38 residual diagnostic requires p>=3")
    if record.B != record.Q + 1:
        raise ArithmeticError("record is not a hard one-level gap")

    q = r + p + m
    mu = q + alpha
    x = r + p
    outer = mu / math.cos(t)
    c = t / math.pi
    d = 1 - 2 * c
    zeta = d / (2 * c)

    shell_r = R27.shell_action(mu, t, r)
    shell_x = R27.shell_action(mu, t, x)
    aq = R27.shell_action(mu, t, q)
    inner_cap = R27.ball_action(mu, q)
    v = R27.ball_action(outer, q)
    w = mu / math.pi * (math.tan(t) - t)

    e0 = shell_r + 0.25 - f
    ep = shell_x + 0.25 - f
    e_sum = e0 + ep
    delta = e0 - ep
    lam = f - 0.25 - w
    b0 = R27.strict_floor(w + 0.25)
    j = f - record.B
    u = lam - j
    sq = aq - w
    chi = u - sq
    h = inner_cap

    if b0 != record.Q or b0 != record.B - 1 or b0 < 1:
        raise ArithmeticError("B0=Q=B-1>=1 synchronization failed")
    if j < 0:
        raise ArithmeticError("negative intrinsic action deficit")

    tol = close_tolerance(alpha, u, sq, chi, h, w, aq, v)
    if sq <= -tol or sq > u + tol:
        raise ArithmeticError("0<S_q<=u coordinate enclosure failed")
    if u >= sq + h + tol:
        raise ArithmeticError("u<S_q+h coordinate enclosure failed")
    if sq + h >= alpha / 2 + tol:
        raise ArithmeticError("S_q+h<alpha/2 coordinate enclosure failed")
    if chi < -tol or chi >= h + tol:
        raise ArithmeticError("0<=chi<h coordinate enclosure failed")
    if u <= -tol or u >= alpha / 2 + tol:
        raise ArithmeticError("0<u<alpha/2 coordinate enclosure failed")

    coordinate_residuals = (
        w - (record.B - 0.25 - u),
        aq - (record.B - 0.25 - chi),
        v - (record.B - 0.25 + h - chi),
        (aq + 0.25 - record.Q) - (1 - chi),
        (shell_x - aq) - (j + ep + chi),
    )
    max_coordinate_residual = max(abs(value) for value in coordinate_residuals)
    if max_coordinate_residual > tol:
        raise ArithmeticError("Round 38 coordinate identity residual is too large")

    count_phase = b0 * zeta
    if count_phase <= 0.2:
        raise ArithmeticError("sample violates B0*zeta>1/5")

    beta = math.acos(q / outer) / math.pi
    if beta <= 0:
        raise ArithmeticError("nonpositive terminal beta")

    angles: list[float] = []
    ys: list[float] = []
    etas: list[float] = []
    for level_index in range(1, record.B + 1):
        theta = R27.inverse_angle(outer, level_index - 0.25)
        y = outer * math.cos(theta) - q
        eta = y - R27.strict_floor(y)
        angles.append(theta)
        ys.append(y)
        etas.append(eta)

    old_angles = angles[:b0]
    old_ys = ys[:b0]
    old_etas = etas[:b0]
    newest_theta = angles[b0]
    newest_y = ys[b0]
    newest_eta = etas[b0]
    if newest_y < -tol or newest_y >= alpha + tol:
        raise ArithmeticError("newest inverse displacement left (0,alpha)")
    if abs(newest_eta - newest_y) > tol:
        raise ArithmeticError("newest inverse fraction is not y_B")
    if any(eta < -tol or eta > 1 + tol for eta in old_etas):
        raise ArithmeticError("old strict inverse fraction left [0,1]")

    omega_minus = sum(
        math.pi / (2 * theta) - math.pi / (2 * t) + 2 * eta
        for theta, eta in zip(old_angles, old_etas)
    )
    omega_newest = math.pi / (2 * newest_theta) - 1 + 2 * newest_eta
    omega = omega_minus + omega_newest
    if omega_minus <= -tol or omega_newest <= -tol:
        raise ArithmeticError("inverse-angle reserve became negative")

    stretch = math.sqrt(
        1 + p * (2 * r + p) / ((m + alpha) * (m + alpha + 2 * r + 2 * p))
    )
    g = stretch - 1
    tau = g / (g + 2)
    elastic = tau * (e_sum + 2 * lam)
    k4 = quartic_payment(mu, outer, r, p)
    m4 = max(elastic, k4)
    xi_hat = delta - m4
    if xi_hat < -tol:
        raise ArithmeticError("XiHat=Delta-M4 became negative")

    a_p = p * p / (3 * (2 * r + p))
    j_cap = 2 * R27.ball_integral(mu, q)
    e_star = (p - d * m) / (2 * p)
    gamma_gap = (
        1
        - j_cap
        + b0 * zeta
        + omega
        + (p + a_p) * m4
        + 2 * p * ep
        + p * xi_hat
        - (p - d * m) / 2
    )

    complete_inverse = sum(
        math.pi / (2 * theta) - 1 + 2 * eta
        for theta, eta in zip(angles, etas)
    )
    lt_direct = 1 - j_cap + complete_inverse
    projected_direct = lt_direct + a_p * m4 + p * (e_sum - e_star)
    phi_delta_plus = lt_direct + a_p * delta + p * (e_sum - e_star)

    ratio = adjacent_ratio(mu, r, p, q)
    a_star = (p + a_p) * g
    h_star = (p + a_p) * ratio
    shelf_elastic = (f - 1) * min(zeta, a_star) + a_star * (u + ep)
    shelf_curvature = zeta + (p + a_p) * k4
    shelf_adjacent = (f - 1) * min(zeta, h_star) + h_star * ep
    h_delta = (
        1
        - j_cap
        + max(shelf_elastic, shelf_curvature, shelf_adjacent)
        + 2 * p * ep
        - (p - d * m) / 2
    )
    rhs_r3820 = (
        1 / (2 * beta)
        - j_cap
        + omega_minus
        + (f - 1) * min(zeta, h_star)
        + h_star * ep
        + h * min(h_star, 2 / beta)
        + 2 * p * ep
        - (p - d * m) / 2
    )

    compare_tol = close_tolerance(
        gamma_gap, phi_delta_plus, h_delta, rhs_r3820, record.PhiMax
    )
    if abs(gamma_gap - projected_direct) > compare_tol:
        raise ArithmeticError("Gamma normal-form replay failed")
    if abs(phi_delta_plus - record.PhiMax) > compare_tol:
        raise ArithmeticError("Phi_delta_plus replay disagrees with Round 27")
    if abs(record.LT - lt_direct) > compare_tol:
        raise ArithmeticError("terminal gap rewrite disagrees with Round 27")
    if gamma_gap > phi_delta_plus + compare_tol:
        raise ArithmeticError("Gamma exceeded Phi_delta_plus")
    if abs((phi_delta_plus - gamma_gap) - a_p * xi_hat) > compare_tol:
        raise ArithmeticError("Phi-Gamma projection-loss identity failed")
    if h_delta > phi_delta_plus + compare_tol:
        raise ArithmeticError("H_Delta exceeded Phi_delta_plus")
    if rhs_r3820 > phi_delta_plus + compare_tol:
        raise ArithmeticError("R38.20 right-hand side exceeded Phi_delta_plus")
    if abs((record.S - record.Phi) - (record.terminal_loss + record.shelf_loss)) > compare_tol:
        raise ArithmeticError("exact shifted-tail loss ledger failed")

    return GapFaceValue(
        record=record,
        grid=grid_label(r),
        b0=b0,
        j=j,
        lam=lam,
        u=u,
        sq=sq,
        chi=chi,
        h=h,
        beta=beta,
        zeta=zeta,
        count_phase=count_phase,
        ep=ep,
        delta=delta,
        m4=m4,
        xi_hat=xi_hat,
        omega_minus=omega_minus,
        omega_newest=omega_newest,
        omega=omega,
        gamma_gap=gamma_gap,
        h_delta=h_delta,
        rhs_r3820=rhs_r3820,
        phi_delta_plus=phi_delta_plus,
        exact_reduced_s=record.S,
        max_coordinate_residual=max_coordinate_residual,
        min_old_eta=min(old_etas),
        max_old_eta=max(old_etas),
        newest_y=newest_y,
        face_labels=classify_faces(record, ep, aq, newest_y, old_ys, old_etas),
    )


def literal_tail_defect(
    outer: float, mu: float, shift: float, term_limit: int
) -> tuple[float | None, int]:
    """Evaluate the literal strict tail defect when the sum is modest."""

    term_count = max(0, math.ceil(outer - shift) + 1)
    if term_count > term_limit:
        return None, term_count
    t = math.acos(mu / outer)
    endpoint = R27.strict_floor(R27.shell_action(mu, t, shift) + 0.25)
    doubled = 0
    for index in range(1, term_count + 1):
        action = R27.shell_action(mu, t, shift + index)
        doubled += R27.strict_floor(action + 0.25)
    integral = R27.ball_integral(outer, shift) - R27.ball_integral(mu, shift)
    return 2 * integral - endpoint - 2 * doubled, term_count


def point_text(item: GapFaceValue) -> str:
    rec = item.record
    d = 1 - 2 * rec.t / math.pi
    return (
        f"r={rec.r:g} p={rec.p} m={rec.m} f={rec.f} "
        f"alpha={rec.alpha:.9g} t={rec.t:.15g} grid={item.grid} "
        f"B={rec.B} Q={rec.Q} B0={item.b0} j={item.j} "
        f"u={item.u:.12g} chi={item.chi:.12g} h={item.h:.12g} "
        f"B0zeta={item.count_phase:.12g} p-dm={rec.p-d*rec.m:.12g} "
        f"faces={','.join(item.face_labels)}"
    )


def summarize(name: str, values: list[GapFaceValue], key: Callable[[GapFaceValue], float]) -> None:
    best = min(values, key=key)
    print(f"diagnostic_only min_{name}={key(best):.15g} at {point_text(best)}")


def report_negative_gamma(item: GapFaceValue, defect_term_limit: int) -> None:
    rec = item.record
    q = rec.r + rec.p + rec.m
    mu = q + rec.alpha
    outer = mu / math.cos(rec.t)
    d_a_r, term_count = literal_tail_defect(outer, mu, rec.r, defect_term_limit)
    print(f"diagnostic_only negative_Gamma_record {point_text(item)}")
    print(
        "diagnostic_only negative_Gamma_values "
        f"Gamma_gap={item.gamma_gap:.17g} H_Delta={item.h_delta:.17g} "
        f"RHS_R38_20={item.rhs_r3820:.17g} "
        f"exact_reduced_S={item.exact_reduced_s:.17g} "
        f"Phi_delta_plus={item.phi_delta_plus:.17g}"
    )
    print(
        "diagnostic_only negative_Gamma_loss_ledger "
        f"S_minus_Phi={item.exact_reduced_s-item.phi_delta_plus:.17g} "
        f"terminal_loss={rec.terminal_loss:.17g} "
        f"shelf_loss={rec.shelf_loss:.17g} "
        f"Phi_minus_Gamma={item.phi_delta_plus-item.gamma_gap:.17g}"
    )
    if d_a_r is None:
        print(
            "diagnostic_only literal_defect_unavailable "
            f"term_count={term_count} term_limit={defect_term_limit}"
        )
    else:
        print(
            "diagnostic_only literal_defect_ledger "
            f"D_A_r={d_a_r:.17g} "
            f"D_A_r_minus_S={d_a_r-item.exact_reduced_s:.17g} "
            f"term_count={term_count}"
        )


def run(limit: int, random_count: int, wall_limit: int, defect_term_limit: int) -> None:
    random.seed(20260738)
    values: list[GapFaceValue] = []
    feasible_tuples = 0

    # Positive alpha only: the two extreme values represent one-sided gap
    # samples and are never re-labelled as literal alpha=0/1 points.
    alphas = (
        1.0e-6,
        1.0e-4,
        1.0e-3,
        1 / 16,
        0.25,
        0.5,
        0.75,
        0.9,
        0.99,
        0.999999,
    )
    radii = list(range(1, limit + 1)) + [10, 50, 1000, 1.0e6]
    shelf_lengths = list(range(3, max(4, min(limit + 3, 9)))) + [10, 20, 40]
    shelf_lengths = sorted(set(shelf_lengths))
    gaps = (1, 2, 3, 6, 12)
    floors = (2, 3, 4, 6)

    def add_tuple(r: float, p: int, m: int, f: int, alpha: float) -> None:
        nonlocal feasible_tuples
        try:
            candidates = R27.hard_candidates(r, p, m, f, alpha, wall_limit)
        except (ArithmeticError, OverflowError, ValueError, ZeroDivisionError):
            return
        retained_here = False
        for record in candidates:
            if not (0.0 < record.alpha < 1.0):
                continue
            if record.B != record.Q + 1 or record.p < 3:
                continue
            values.append(evaluate_gap_face(record))
            retained_here = True
        if retained_here:
            feasible_tuples += 1

    for offset in (0.0, 0.5):
        for radius in radii:
            r = float(radius) + offset
            if offset and r < 1.5:
                continue
            for p in shelf_lengths:
                for m in gaps:
                    for f in floors:
                        for alpha in alphas:
                            add_tuple(r, p, m, f, alpha)

    for _ in range(random_count):
        half_grid = random.choice((False, True))
        r = float(max(1, round(math.exp(random.uniform(0, math.log(1.0e7))))))
        if half_grid:
            r += 0.5
        p = max(3, round(math.exp(random.uniform(math.log(3), math.log(300)))))
        m = max(1, round(math.exp(random.uniform(0, math.log(100)))))
        f = random.choice((2, 2, 3, 4, 6, 10, 16))
        alpha = random.choice(alphas + (max(1.0e-8, min(1 - 1.0e-8, random.random())),))
        add_tuple(r, p, m, f, alpha)

    if not values:
        raise RuntimeError("no positive-alpha p>=3 hard gap record was retained")

    residual_values = [
        item
        for item in values
        if item.record.p - (1 - 2 * item.record.t / math.pi) * item.record.m
        > 74 / 35
    ]
    grid_counts = {
        name: sum(item.grid == name for item in values)
        for name in ("integer_d4_activity", "half_integer_d5_activity")
    }
    face_names = (
        "lower_shelf",
        "outer_B_gap_side_near",
        "literal_Q_wall",
        "literal_old_inverse_wall",
        "adverse_old_inverse_side_near",
        "lower_alpha_gap_side_near",
        "upper_alpha_gap_side_near",
        "gap_interior",
    )
    face_counts = {
        name: sum(name in item.face_labels for item in values) for name in face_names
    }

    print("ROUND 38 GAP-FACE SEARCH")
    print("diagnostic_only=True")
    print("theorem_claim=False")
    print("arithmetic=ordinary_binary64")
    print("continuum_sign_status=not_assessed")
    print("alpha_domain=0<alpha<1; literal_alpha0_equal_count_excluded=True")
    print("domain=hard_one_level_gap,p>=3")
    print("sampler=Round27_owner_wall_sampler")
    print(f"feasible_tuples={feasible_tuples}; retained_evaluations={len(values)}")
    print(f"post_CP2_residual_evaluations={len(residual_values)}")
    print("diagnostic_only grid_counts=" + repr(grid_counts))
    print("diagnostic_only face_counts=" + repr(face_counts))

    summarize("Gamma_gap", values, lambda item: item.gamma_gap)
    summarize("H_Delta", values, lambda item: item.h_delta)
    summarize("RHS_R38_20", values, lambda item: item.rhs_r3820)
    summarize("Phi_delta_plus", values, lambda item: item.phi_delta_plus)
    summarize("B0_zeta_minus_1_5", values, lambda item: item.count_phase - 0.2)
    if residual_values:
        summarize("residual_Gamma_gap", residual_values, lambda item: item.gamma_gap)
        summarize("residual_H_Delta", residual_values, lambda item: item.h_delta)
        summarize("residual_RHS_R38_20", residual_values, lambda item: item.rhs_r3820)

    negative_gamma = [item for item in values if item.gamma_gap < 0]
    negative_h_delta = [item for item in values if item.h_delta < 0]
    negative_rhs = [item for item in values if item.rhs_r3820 < 0]
    print(
        "diagnostic_only negative_counts "
        f"Gamma_gap={len(negative_gamma)} "
        f"H_Delta={len(negative_h_delta)} "
        f"RHS_R38_20={len(negative_rhs)}"
    )
    print(
        "diagnostic_only coordinate_checks "
        f"max_identity_residual={max(item.max_coordinate_residual for item in values):.6g} "
        f"min_u={min(item.u for item in values):.12g} "
        f"min_chi={min(item.chi for item in values):.12g} "
        f"min_h_minus_chi={min(item.h-item.chi for item in values):.12g} "
        f"min_alpha_half_minus_Sq_h="
        f"{min(item.record.alpha/2-item.sq-item.h for item in values):.12g}"
    )
    print(
        "diagnostic_only ownership_coverage "
        f"both_parity_grids={all(grid_counts.values())} "
        f"literal_old_inverse={face_counts['literal_old_inverse_wall'] > 0} "
        f"adverse_old_inverse={face_counts['adverse_old_inverse_side_near'] > 0}"
    )

    for item in negative_gamma:
        report_negative_gamma(item, defect_term_limit)

    print("scan_status=diagnostic_only")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--random", type=int, default=200)
    parser.add_argument("--wall-limit", type=int, default=50)
    parser.add_argument("--defect-term-limit", type=int, default=200_000)
    args = parser.parse_args()
    run(args.limit, args.random, args.wall_limit, args.defect_term_limit)


if __name__ == "__main__":
    main()
