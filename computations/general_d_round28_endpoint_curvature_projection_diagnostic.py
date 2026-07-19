#!/usr/bin/env python3
"""Round 28 diagnostic for the endpoint-preserving hard-sector projection.

This program is theorem-design evidence only.  It imports the exact-domain
owner/wall sampler from the Round 27 diagnostic and tests the proved analytic
inequalities

    Delta >= ((s-1)/(s+1)) (E+2 lambda),
    Delta >= K_N,

where K_N is the positive curvature series through index N.  It then compares
the complete-terminal and root-free projected scalars with Phi_delta^+.

No positive minimum printed here is a certificate or a proof of continuum
coverage.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import random
import sys
from dataclasses import dataclass
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
ROUND27_PATH = ROOT / "computations" / "general_d_round27_exact_phi_hard_sector_diagnostic.py"
SPEC = importlib.util.spec_from_file_location("round27_hard", ROUND27_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND27_PATH}")
R27 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R27
SPEC.loader.exec_module(R27)


@dataclass(frozen=True)
class Projection:
    record: object
    delta: float
    e_p: float
    lam: float
    elastic_exact: float
    elastic_projected: float
    curvature: float
    terminal_rootfree: float
    psi_E_LT: float
    psi_E_rootfree: float
    psi_endpoint_LT: float
    psi_endpoint_rootfree: float
    psi_endpoint_epfree: float
    identity_residual: float


def curvature_series(
    r: float, p: int, mu: float, outer: float, order: int
) -> float:
    """K_N with positive binomial terms j=0,...,order."""

    total = 0.0
    for j in range(order + 1):
        b_j = math.comb(2 * j, j) / (4**j)
        radii = mu ** (-2 * j - 1) - outer ** (-2 * j - 1)
        spatial = (r + p) ** (2 * j + 2) - r ** (2 * j + 2)
        total += (
            b_j
            * radii
            * spatial
            / (math.pi * (2 * j + 1) * (2 * j + 2))
        )
    return total


def project(record: object, order: int) -> Projection:
    r, p, m, f = record.r, record.p, record.m, record.f
    alpha, t = record.alpha, record.t
    q = r + p + m
    mu = q + alpha
    outer = mu / math.cos(t)
    c = t / math.pi
    d = 1 - 2 * c
    x = r + p
    X = m + alpha

    a_r = R27.shell_action(mu, t, r)
    a_p_endpoint = R27.shell_action(mu, t, x)
    e_0 = a_r + 0.25 - f
    e_p = a_p_endpoint + 0.25 - f
    delta = e_0 - e_p
    E = e_0 + e_p

    stretch = math.sqrt(
        1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p))
    )
    g = stretch - 1
    tau = g / (g + 2)
    W = mu / math.pi * (math.tan(t) - t)
    lam = f - 0.25 - W
    elastic_exact = g * (lam + e_p)
    elastic_projected = tau * (E + 2 * lam)

    curvature = curvature_series(r, p, mu, outer, order)
    B0 = R27.strict_floor(W + 0.25)
    J = 2 * R27.ball_integral(mu, q)
    payment = R27.top_payment(lam) if 0 < lam < 1 else 0.0
    terminal_rootfree = B0 * d / (2 * c) - J + payment

    a_coeff = p * p / (3 * (2 * r + p))
    E_star = 0.5 - d * m / (2 * p)
    remainder_owner = max(elastic_projected, curvature)
    psi_E_LT = (
        max(0.0, record.LT) + a_coeff * remainder_owner + p * (E - E_star)
    )
    psi_E_rootfree = (
        max(0.0, terminal_rootfree)
        + a_coeff * remainder_owner
        + p * (E - E_star)
    )
    shelf_owner = max(elastic_exact, curvature)
    psi_endpoint_LT = (
        max(0.0, record.LT)
        + (p + a_coeff) * shelf_owner
        + 2 * p * e_p
        - p * E_star
    )
    psi_endpoint_rootfree = (
        max(0.0, terminal_rootfree)
        + (p + a_coeff) * shelf_owner
        + 2 * p * e_p
        - p * E_star
    )
    psi_endpoint_epfree = (
        max(0.0, terminal_rootfree)
        + (p + a_coeff) * max(g * lam, curvature)
        - p * E_star
    )
    exact_endpoint_form = (
        max(0.0, record.LT)
        + (p + a_coeff) * delta
        + 2 * p * e_p
        - p * E_star
    )
    identity_residual = record.PhiMax - exact_endpoint_form

    tolerance = 2.0e-7 * max(1.0, abs(record.PhiMax))
    if delta + tolerance < elastic_exact:
        raise ArithmeticError("exact endpoint elasticity failed")
    if delta + tolerance < elastic_projected:
        raise ArithmeticError("E-projected elasticity failed")
    if delta + tolerance < curvature:
        raise ArithmeticError("curvature series exceeded Delta")
    if record.LT + tolerance < terminal_rootfree:
        raise ArithmeticError("root-free terminal bound exceeded L_T")
    if abs(identity_residual) > tolerance:
        raise ArithmeticError("endpoint identity did not close")
    if record.PhiMax + tolerance < psi_endpoint_LT:
        raise ArithmeticError("endpoint L_T projection exceeded Phi_delta^+")
    if record.PhiMax + tolerance < psi_E_LT:
        raise ArithmeticError("exact-remainder projection exceeded Phi_delta^+")
    if psi_E_LT + tolerance < psi_E_rootfree:
        raise ArithmeticError("root-free exact-remainder projection exceeded full projection")
    if psi_E_LT + tolerance < psi_endpoint_LT:
        raise ArithmeticError("endpoint L_T projection exceeded E-retaining projection")
    if psi_E_rootfree + tolerance < psi_endpoint_rootfree:
        raise ArithmeticError("endpoint root-free projection exceeded E-retaining projection")
    if psi_endpoint_LT + tolerance < psi_endpoint_rootfree:
        raise ArithmeticError("root-free projection exceeded full projection")

    return Projection(
        record,
        delta,
        e_p,
        lam,
        elastic_exact,
        elastic_projected,
        curvature,
        terminal_rootfree,
        psi_E_LT,
        psi_E_rootfree,
        psi_endpoint_LT,
        psi_endpoint_rootfree,
        psi_endpoint_epfree,
        identity_residual,
    )


def canonical_boundary(order: int) -> None:
    """High-precision alpha-up-to-one lower-shelf limiting face."""

    mp.mp.dps = 90
    r, p, m, f = mp.mpf(1), 3, 2, 2
    mu, q, x = mp.mpf(7), mp.mpf(6), mp.mpf(4)

    def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        if z >= radius:
            return mp.mpf(0)
        theta = mp.acos(z / radius)
        return radius / mp.pi * (mp.sin(theta) - theta * mp.cos(theta))

    def integral(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        if z >= radius:
            return mp.mpf(0)
        theta = mp.acos(z / radius)
        cosine, sine = mp.cos(theta), mp.sin(theta)
        return radius**2 / (4 * mp.pi) * (
            theta * (1 + 2 * cosine**2) - 3 * sine * cosine
        )

    def shell(t: mp.mpf, z: mp.mpf) -> mp.mpf:
        return action(mu / mp.cos(t), z) - action(mu, z)

    t = mp.findroot(lambda value: shell(value, x) - mp.mpf(7) / 4, (1, 1.01))
    outer = mu / mp.cos(t)
    c, d = t / mp.pi, 1 - 2 * t / mp.pi
    W = mu / mp.pi * (mp.tan(t) - t)
    lam = mp.mpf(7) / 4 - W
    J = 2 * integral(mu, q)
    terminal = d / (2 * c) - J + 2 * (mp.mpf(3) / 4 - lam) ** 2
    X = mp.mpf(3)
    g = mp.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p))) - 1
    tau = g / (g + 2)
    a_coeff = p**2 / (3 * (2 * r + p))
    E_star = mp.mpf(1) / 2 - d * m / (2 * p)
    E = shell(t, r) + mp.mpf(1) / 4 - f

    curvature = mp.mpf(0)
    for j in range(order + 1):
        b_j = mp.binomial(2 * j, j) / (4**j)
        curvature += (
            b_j
            * (mu ** (-2 * j - 1) - outer ** (-2 * j - 1))
            * ((r + p) ** (2 * j + 2) - r ** (2 * j + 2))
            / (mp.pi * (2 * j + 1) * (2 * j + 2))
        )
    remainder_scalar = (
        max(0, terminal)
        + a_coeff * max(tau * (E + 2 * lam), curvature)
        + p * (E - E_star)
    )
    endpoint_scalar = (
        max(0, terminal) + (p + a_coeff) * max(g * lam, curvature) - p * E_star
    )

    print("ROUND 28 CANONICAL LIMITING FACE (90-digit mpmath)")
    print("data: r=1 p=3 m=2 f=2 alpha->1-, lower shelf wall")
    for name, value in (
        ("t", t),
        ("rho", mp.cos(t)),
        ("K", outer),
        ("lambda", lam),
        ("J", J),
        ("terminal_rootfree", terminal),
        ("g_lambda", g * lam),
        ("E", E),
        (f"curvature_K{order}", curvature),
        ("E_star", E_star),
        (f"Psi4E_rootfree_K{order}", remainder_scalar),
        (f"Psi_endpoint_epfree_K{order}", endpoint_scalar),
    ):
        print(f"{name}={mp.nstr(value, 50)}")


def inverse_wall_boundary(order: int) -> None:
    """High-precision bad-side y_1-down-to-2 limit for the full scalar."""

    mp.mp.dps = 90
    r, p, m, f = mp.mpf(1), 2, 2, 2
    mu, q, x = mp.mpf(5), mp.mpf(5), mp.mpf(3)

    def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        if z >= radius:
            return mp.mpf(0)
        theta = mp.acos(z / radius)
        return radius / mp.pi * (mp.sin(theta) - theta * mp.cos(theta))

    outer = mp.findroot(lambda radius: action(radius, 7) - mp.mpf(3) / 4, (11, 11.1))
    t = mp.acos(mu / outer)
    c, d = t / mp.pi, 1 - 2 * t / mp.pi
    W = action(outer, mu)
    lam = mp.mpf(7) / 4 - W
    theta_1 = mp.acos(mp.mpf(7) / outer)
    # This is the right-side limit eta_1 -> 0.  At the literal wall eta_1=1.
    terminal_right = mp.pi / (2 * theta_1) - 1 + (W - 1) ** 2 / c
    shell_r = action(outer, r) - action(mu, r)
    shell_x = action(outer, x) - action(mu, x)
    E = shell_r + shell_x + mp.mpf(1) / 2 - 2 * f
    X = mp.mpf(2)
    g = mp.sqrt(1 + p * (2 * r + p) / (X * (X + 2 * r + 2 * p))) - 1
    tau = g / (g + 2)
    a_coeff = p**2 / (3 * (2 * r + p))
    E_star = mp.mpf(1) / 2 - d * m / (2 * p)
    curvature = mp.mpf(0)
    for j in range(order + 1):
        b_j = mp.binomial(2 * j, j) / (4**j)
        curvature += (
            b_j
            * (mu ** (-2 * j - 1) - outer ** (-2 * j - 1))
            * ((r + p) ** (2 * j + 2) - r ** (2 * j + 2))
            / (mp.pi * (2 * j + 1) * (2 * j + 2))
        )
    projected = tau * (E + 2 * lam)
    scalar = terminal_right + a_coeff * max(projected, curvature) + p * (E - E_star)

    print("ROUND 28 COMPLETE-TERMINAL LIMITING FACE (90-digit mpmath)")
    print("data: r=1 p=2 m=2 f=2 alpha=0 y1->2+ (bad side)")
    for name, value in (
        ("K", outer),
        ("t", t),
        ("theta1", theta_1),
        ("lambda", lam),
        ("L_T_right", terminal_right),
        ("E", E),
        ("E_star", E_star),
        ("elastic_projected", projected),
        (f"curvature_K{order}", curvature),
        (f"Psi4E_LT_K{order}", scalar),
    ):
        print(f"{name}={mp.nstr(value, 50)}")


def rejected_scalar_regressions(order: int) -> None:
    """Replay the Round 26b/27 compressed-scalar witnesses."""

    fixtures = (
        ("round27_RJ", 4036.0, 32, 1, 2, 1 / 16, 79 / 500),
        ("round26b_C8", 57755 / 2, 80, 15, 2, 1 / 2, 7801 / 100000),
    )
    print("ROUND 28 REJECTED-SCALAR REGRESSIONS")
    for name, r, p, m, f, alpha, t in fixtures:
        record = R27.evaluate(r, p, m, f, alpha, t)
        item = project(record, order)
        d = 1 - 2 * t / math.pi
        automatic = p <= d * m or record.epsilon_sum >= record.automatic_threshold
        if not automatic:
            raise ArithmeticError(f"{name} left the Round 27 automatic sector")
        print(
            f"{name}: E={record.epsilon_sum:.15g} "
            f"E*={record.automatic_threshold:.15g} automatic={automatic} "
            f"Phi+={record.PhiMax:.15g} "
            f"Psi4E_LT={item.psi_E_LT:.15g} "
            f"Psi4E_rootfree={item.psi_E_rootfree:.15g}"
        )


def summarize(name: str, projections: list[Projection], key) -> None:
    best = min(projections, key=key)
    rec = best.record
    print(
        f"min {name}={key(best):.15g} at "
        f"r={rec.r:g} p={rec.p} m={rec.m} f={rec.f} "
        f"alpha={rec.alpha:g} t={rec.t:.15g} "
        f"E={rec.epsilon_sum:.12g} E*={rec.automatic_threshold:.12g} "
        f"e_p={best.e_p:.12g} lambda={best.lam:.12g} "
        f"K_N={best.curvature:.12g} T0={best.terminal_rootfree:.12g}"
    )


def run_scan(limit: int, random_count: int, wall_limit: int, order: int) -> None:
    random.seed(20260720)
    projections: list[Projection] = []
    feasible_tuples = 0
    alphas = (0.0, 1 / 16, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999999)
    radii = list(range(1, limit + 1)) + [20, 50, 100, 300, 1000, 3000, 10000]
    shelf_lengths = list(range(1, min(limit, 12) + 1)) + [16, 24, 32, 48]
    gaps = (1, 2, 3, 4, 6, 8, 12)
    floors = (2, 3, 4, 6)

    def add_tuple(r: float, p: int, m: int, f: int, alpha: float) -> None:
        nonlocal feasible_tuples
        try:
            records = R27.hard_candidates(r, p, m, f, alpha, wall_limit)
        except (ArithmeticError, OverflowError, ValueError, ZeroDivisionError):
            return
        if records:
            feasible_tuples += 1
        for record in records:
            projections.append(project(record, order))

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
        r = float(max(1, round(math.exp(random.uniform(0, math.log(1.0e6))))))
        if half_grid:
            r += 0.5
        p = max(1, round(math.exp(random.uniform(0, math.log(1000)))))
        m = max(1, round(math.exp(random.uniform(0, math.log(200)))))
        f = random.choice((2, 2, 2, 3, 4, 6, 10, 16))
        alpha = random.choice(alphas + (random.random(),))
        add_tuple(r, p, m, f, alpha)

    if not projections:
        raise RuntimeError("no hard-sector record was retained")

    print("ROUND 28 ENDPOINT/CURVATURE HARD-SECTOR SCAN (NON-CERTIFIED)")
    print(f"curvature order N={order}; terms j=0,...,{order}")
    print(f"feasible tuples={feasible_tuples}; retained evaluations={len(projections)}")
    print("grids=integer+half-integer; owner/activity/wall predicates inherited")
    print("scanArithmetic=ordinary_double_precision")
    summarize("Phi_delta_plus", projections, lambda item: item.record.PhiMax)
    summarize(
        "Psi4E_LT", projections, lambda item: item.psi_E_LT
    )
    summarize(
        "Psi4E_rootfree",
        projections,
        lambda item: item.psi_E_rootfree,
    )
    summarize("Psi_endpoint_LT", projections, lambda item: item.psi_endpoint_LT)
    summarize(
        "Psi_endpoint_rootfree",
        projections,
        lambda item: item.psi_endpoint_rootfree,
    )
    summarize(
        "Psi_endpoint_epfree",
        projections,
        lambda item: item.psi_endpoint_epfree,
    )
    for branch, subset in (
        (
            "curvature",
            [item for item in projections if item.curvature >= item.elastic_projected],
        ),
        (
            "elasticity",
            [item for item in projections if item.elastic_projected > item.curvature],
        ),
    ):
        if subset:
            print(f"branch {branch}: evaluations={len(subset)}")
            summarize(
                f"Psi4E_LT[{branch}]",
                subset,
                lambda item: item.psi_E_LT,
            )
            summarize(
                f"Psi4E_rootfree[{branch}]",
                subset,
                lambda item: item.psi_E_rootfree,
            )
    print(
        "negative counts: "
        f"Phi={sum(item.record.PhiMax < 0 for item in projections)} "
        f"Psi4E_LT={sum(item.psi_E_LT < 0 for item in projections)} "
        f"Psi4E_root={sum(item.psi_E_rootfree < 0 for item in projections)} "
        f"endpointLT={sum(item.psi_endpoint_LT < 0 for item in projections)} "
        f"endpointRoot={sum(item.psi_endpoint_rootfree < 0 for item in projections)} "
        f"endpointEpfree={sum(item.psi_endpoint_epfree < 0 for item in projections)}"
    )
    print(
        "max endpoint identity residual="
        f"{max(abs(item.identity_residual) for item in projections):.6g}"
    )
    print("scanCertification=diagnostic_only")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--random", type=int, default=1000)
    parser.add_argument("--wall-limit", type=int, default=60)
    parser.add_argument(
        "--order",
        type=int,
        default=1,
        help="largest retained curvature-series index (1 includes quartic gain)",
    )
    parser.add_argument("--boundary-only", action="store_true")
    args = parser.parse_args()
    if args.order < 0:
        raise SystemExit("--order must be nonnegative")
    canonical_boundary(args.order)
    inverse_wall_boundary(args.order)
    rejected_scalar_regressions(args.order)
    if not args.boundary_only:
        run_scan(args.limit, args.random, args.wall_limit, args.order)


if __name__ == "__main__":
    main()
