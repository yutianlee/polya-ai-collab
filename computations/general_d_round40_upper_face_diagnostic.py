#!/usr/bin/env python3
"""Round 40 adversarial diagnostic for the upper-alpha/outer-B face.

This program is theorem-design and falsification evidence only.  It uses
ordinary binary64 arithmetic, SciPy root finding, and (optionally) a fixed
mpmath replay.  It is not interval arithmetic and no positive sampled
minimum is a proof.

At alpha=1 the outer wall has the efficient exact parameterization

    q/pi (tan(theta)-theta) = B-1/4,
    t = acos((q+1) cos(theta)/q).

Thus the search can select the count B directly, derive the first-shelf
label f from the action, and then enforce every retained hard-gap owner.
The deterministic pass covers both dimension grids.  The directed random
pass selects the hard ratio d*m/p first and deliberately targets small,
intermediate, large, and near-pi/2 phases.

Gamma_OB and F_OB require the literal old-inverse fractions.  They are
evaluated in the bulk pass only for B <= ``--exact-b-max``.  The root-free
F_OB bound is evaluated at every retained root.  Since the Round 39 proof
gives Gamma_OB > F_OB >= F_OB_rootfree, a positive root-free value is also
diagnostic evidence against a negative exact value, but remains nonproof.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import random
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Callable, Iterable, Iterator

import mpmath as mp
from scipy.optimize import brentq
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[1]
ROUND39_PATH = ROOT / "computations" / "general_d_round39_outer_face_diagnostic.py"
SPEC = importlib.util.spec_from_file_location("round39_round40_upper", ROUND39_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND39_PATH}")
R39 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R39
SPEC.loader.exec_module(R39)


PI = math.pi
SEARCH_TOL = 3.0e-7


@dataclass(frozen=True)
class UpperSample:
    face: R39.FaceValue
    theta: float
    beta: float
    q: float
    d: float
    zeta: float
    j_cap: float
    g: float
    r1: float
    adjacent: float
    elastic: float
    ep_payment: float
    negative: float
    count_payment: float
    omega_rootfree: float
    f_cap_count: float
    f_cap_count_drop_2pep: float
    f_no_omega: float
    f_no_ap: float
    f_no_adjacent: float
    f_drop_j: float
    f_ep_only: float
    f_drop_all_ep: float
    f_drop_h_u: float
    f_phase_only: float
    f_phase_h_u: float
    f_phase_coordinate_ep: float
    f_phase_explicit_ep: float
    f_phase_h_u_coordinate_ep: float
    f_phase_h_u_explicit_ep: float
    midpoint_payment: float
    u_mid_scalar: float
    r_mid_projected: float
    mu_star: float
    r_star: float
    r_branch: float
    r_branch_kind: str
    r_branch_residual: float

    @property
    def r(self) -> float:
        return self.face.r

    @property
    def p(self) -> int:
        return self.face.p

    @property
    def m(self) -> int:
        return self.face.m

    @property
    def B(self) -> int:
        return self.face.B

    @property
    def f(self) -> int:
        return self.face.f

    @property
    def j(self) -> int:
        return self.face.j

    @property
    def active_residual(self) -> bool:
        return self.p - self.d * self.m > 11 / 5


def _q_key(q: float) -> int:
    """Both authorized grids make 2*q an integer."""

    return int(round(2 * q))


@lru_cache(maxsize=500_000)
def upper_phase(q2: int, B: int) -> tuple[float, float] | None:
    """Return (theta,t) at alpha=1 and the selected outer wall."""

    q = q2 / 2
    mu = q + 1
    theta0 = math.acos(q / mu)
    target = B - 0.25
    try:
        theta = brentq(
            lambda value: q / PI * (math.tan(value) - value) - target,
            theta0,
            PI / 2 - 1.0e-13,
            xtol=8.0e-15,
            rtol=1.0e-14,
            maxiter=120,
        )
    except (ValueError, ArithmeticError, OverflowError):
        return None
    cosine_t = mu * math.cos(theta) / q
    if not 0 < cosine_t < 1:
        return None
    return theta, math.acos(cosine_t)


def build_sample(
    r: float,
    p: int,
    m: int,
    B: int,
    *,
    exact_b_max: int,
) -> UpperSample | None:
    """Construct and fully recheck one upper-alpha outer-wall point."""

    if p < 3 or m < 1 or B < 2:
        return None
    q = r + p + m
    phase = upper_phase(_q_key(q), B)
    if phase is None:
        return None
    theta, t = phase
    d = 1 - 2 * t / PI
    if not (0 < d < 1 and p > d * m):
        return None

    mu = q + 1
    gamma = 0.75 if float(r).is_integer() else 2.0
    if R39.R27.activity_margin(mu, t, gamma) <= -SEARCH_TOL:
        return None

    x = r + p
    f = R39.R27.ordinary_floor(R39.R27.shell_action(mu, t, x) + 0.25)
    if f < 1:
        return None

    # First do the inexpensive root-free evaluation.  Literal old inverse
    # levels are replayed only after this point and only at moderate B.
    face = R39.evaluate_outer_face(
        "outer_upper",
        r,
        p,
        m,
        f,
        B,
        1.0,
        t,
        exact_inverse=False,
        tol=SEARCH_TOL,
    )
    if face is None:
        return None
    if B <= exact_b_max:
        exact_face = R39.evaluate_outer_face(
            "outer_upper",
            r,
            p,
            m,
            f,
            B,
            1.0,
            t,
            exact_inverse=True,
            tol=SEARCH_TOL,
        )
        if exact_face is None:
            return None
        face = exact_face

    outer = mu / math.cos(t)
    zeta = PI / (2 * t) - 1
    beta = theta / PI
    j_cap = 2 * R39.R27.ball_integral(mu, q)
    ur = math.sqrt(mu * mu - r * r)
    ux = math.sqrt(mu * mu - x * x)
    uq = math.sqrt(mu * mu - q * q)
    g = ur / ux - 1
    r1 = (ur - ux) / (ux - uq)
    a_p = p * p / (3 * (2 * r + p))
    aq = R39.R27.shell_action(mu, t, q)
    ax = R39.R27.shell_action(mu, t, x)
    w = mu / PI * (math.tan(t) - t)
    adjacent = p * r1 * (ax - aq)
    elastic = a_p * g * (ax - w)
    ep_payment = 2 * p * face.ep
    negative = -(p - d * m) / 2
    count_payment = (B - 1) * zeta
    rootfree = face.f_ob_rootfree

    # Two proven universal replacements from Round 39 are J<1/10 and
    # B0*zeta>1/5.  The following is therefore a plausible coarsening of
    # F_OB_rootfree, not a theorem established by this scan.
    f_cap_count = rootfree + j_cap - 0.1 - count_payment + 0.2
    f_cap_count_drop = f_cap_count - ep_payment

    # Deliberately aggressive deletions isolate which correlated reserves
    # cannot safely be discarded in a future analytic proof.
    f_no_omega = rootfree - face.omega_rootfree
    f_no_ap = rootfree - elastic
    f_no_adjacent = rootfree - adjacent
    f_drop_j = rootfree - (p * r1 + a_p * g) * face.j
    f_ep_only = (
        1 / (2 * beta)
        - 0.1
        + face.omega_rootfree
        + 0.2
        + (p * r1 + a_p * g) * face.ep
        + ep_payment
        + negative
    )
    f_drop_all_ep = rootfree - (p * r1 + a_p * g + 2 * p) * face.ep
    f_drop_h_u = rootfree - p * r1 * face.h - a_p * g * face.u
    f_phase_only = 1 / (2 * beta) - 0.1 + face.omega_rootfree + 0.2 + negative
    hu_payment = p * r1 * face.h + a_p * g * face.u
    coordinate_ep = (p * r1 + a_p * g) * face.ep
    f_phase_h_u = f_phase_only + hu_payment
    f_phase_coordinate_ep = f_phase_only + coordinate_ep
    f_phase_explicit_ep = f_phase_only + ep_payment
    f_phase_h_u_coordinate_ep = f_phase_only + hu_payment + coordinate_ep
    f_phase_h_u_explicit_ep = f_phase_only + hu_payment + ep_payment

    # Round 40 midpoint package.  ``u_mid_scalar`` is the full sufficient
    # scalar; ``r_mid_projected`` is its floor-free projection R(mu).
    # R_* evaluates R at the proved lower endpoint mu_* and the two branch
    # formulas below are algebraically equal to that endpoint value.
    y_mid = r + p / 2
    n_mid = p / 2 + m + 1
    rho_mid = n_mid / mu
    cosine_t = math.cos(t)
    sine_t = math.sin(t)
    a_mid = (1 - cosine_t) / PI
    s_mid = 2 + sine_t * sine_t
    midpoint_payment = (
        p
        * p
        * y_mid
        * (1 - cosine_t)
        / (PI * math.sqrt(mu * mu - y_mid * y_mid * cosine_t * cosine_t))
    )
    u_mid_scalar = (
        1 / (2 * beta)
        - j_cap
        + count_payment
        + midpoint_payment
        + negative
    )
    l0 = (math.tan(t) - t) / PI
    c_mid = (1 - rho_mid) * a_mid / math.sqrt(s_mid - 2 * (1 - rho_mid))
    r_mid_projected = (
        0.9
        + 9 * zeta / 16
        + zeta * mu * l0 / 4
        + p * p * c_mid
        + negative
    )
    s0 = p + m + 2
    mu0 = 5 / (4 * l0)
    mu_star = max(s0, mu0)
    a_star_mid = 1 - n_mid / mu_star
    c_star = a_star_mid * a_mid / math.sqrt(s_mid - 2 * a_star_mid)
    r_star = (
        0.9
        + 9 * zeta / 16
        + zeta * mu_star * l0 / 4
        + p * p * c_star
        + negative
    )
    if s0 >= mu0:
        r_branch_kind = "I"
        a_branch = (p / 2 + 1) / s0
        x_branch = (p + 2) * (zeta * l0 + 2 * d) / 8
        r_branch = (
            0.9
            + 9 * zeta / 16
            - p * (1 + d) / 2
            - d
            + x_branch / a_branch
            + p * p * a_mid * a_branch / math.sqrt(s_mid - 2 * a_branch)
        )
    else:
        r_branch_kind = "II"
        a_branch = 1 - n_mid / mu0
        r_branch = (
            0.9
            + 7 * zeta / 8
            + d * mu0 / 2
            - p * (2 + d) / 4
            - d / 2
            + p * p * a_mid * a_branch / math.sqrt(s_mid - 2 * a_branch)
            - d * mu0 * a_branch / 2
        )

    # ``outer`` is intentionally evaluated above: it catches overflow in a
    # regime where the binary64 replay is no longer trustworthy.
    if not math.isfinite(outer):
        return None
    return UpperSample(
        face=face,
        theta=theta,
        beta=beta,
        q=q,
        d=d,
        zeta=zeta,
        j_cap=j_cap,
        g=g,
        r1=r1,
        adjacent=adjacent,
        elastic=elastic,
        ep_payment=ep_payment,
        negative=negative,
        count_payment=count_payment,
        omega_rootfree=face.omega_rootfree,
        f_cap_count=f_cap_count,
        f_cap_count_drop_2pep=f_cap_count_drop,
        f_no_omega=f_no_omega,
        f_no_ap=f_no_ap,
        f_no_adjacent=f_no_adjacent,
        f_drop_j=f_drop_j,
        f_ep_only=f_ep_only,
        f_drop_all_ep=f_drop_all_ep,
        f_drop_h_u=f_drop_h_u,
        f_phase_only=f_phase_only,
        f_phase_h_u=f_phase_h_u,
        f_phase_coordinate_ep=f_phase_coordinate_ep,
        f_phase_explicit_ep=f_phase_explicit_ep,
        f_phase_h_u_coordinate_ep=f_phase_h_u_coordinate_ep,
        f_phase_h_u_explicit_ep=f_phase_h_u_explicit_ep,
        midpoint_payment=midpoint_payment,
        u_mid_scalar=u_mid_scalar,
        r_mid_projected=r_mid_projected,
        mu_star=mu_star,
        r_star=r_star,
        r_branch=r_branch,
        r_branch_kind=r_branch_kind,
        r_branch_residual=r_star - r_branch,
    )


def deterministic_candidates(q_max: int, b_max: int) -> Iterator[tuple[float, int, int, int]]:
    """Exhaust all decompositions on both grids in the small-q box."""

    for q2 in range(10, 2 * q_max + 1):
        q = q2 / 2
        integer_grid = q2 % 2 == 0
        r0 = 1.0 if integer_grid else 1.5
        r = r0
        while r <= q - 4:
            p_max = int(math.floor(q - r - 1 + 1.0e-12))
            for p in range(3, p_max + 1):
                m = int(round(q - r - p))
                if m < 1:
                    continue
                for B in range(2, b_max + 1):
                    yield r, p, m, B
            r += 1


def phase_wall_counts(q: float, target_t: float) -> tuple[int, ...]:
    """Integer walls immediately around a desired phase."""

    mu = q + 1
    theta = math.acos(q * math.cos(target_t) / mu)
    real_B = q / PI * (math.tan(theta) - theta) + 0.25
    center = int(round(real_B))
    return tuple(sorted({value for value in range(center - 1, center + 2) if value >= 2}))


def directed_random_candidates(count: int, seed: int) -> Iterator[tuple[float, int, int, int]]:
    """Bias random points toward the hard wall and all phase scales."""

    rng = random.Random(seed)
    phase_atoms = (
        0.25,
        0.5,
        0.75,
        0.95,
        1.05,
        1.15,
        1.25,
        1.35,
        1.43,
        1.49,
        1.53,
        1.555,
        1.565,
    )
    for _ in range(count):
        if rng.random() < 0.72:
            r = rng.randrange(2, 41) / 2
            if r < 1 or (r % 1 == 0.5 and r < 1.5):
                r = 1.0
        else:
            r = max(1.0, round(2 * math.exp(rng.uniform(0, math.log(1.0e8)))) / 2)

        if rng.random() < 0.75:
            p = rng.randint(3, 40)
        else:
            p = max(3, round(math.exp(rng.uniform(math.log(3), math.log(1.0e5)))))

        target_t = rng.choice(phase_atoms) if rng.random() < 0.8 else rng.uniform(0.2, 1.569)
        d_target = 1 - 2 * target_t / PI
        # Select rho=d*m/p across the hard interval, with extra mass near
        # both rho=0 and rho=1.  The exact wall is rechecked after rounding.
        selector = rng.random()
        if selector < 1 / 3:
            rho = rng.random() ** 4
        elif selector < 2 / 3:
            rho = 1 - rng.random() ** 4
        else:
            rho = rng.random()
        m = max(1, round(rho * p / max(d_target, 1.0e-7)))
        m = min(m, 2_000_000)
        q = r + p + m
        for B in phase_wall_counts(q, target_t):
            if B <= 100_000_000:
                yield r, p, m, B


def round39_stress_candidates() -> Iterator[tuple[float, int, int, int]]:
    """Replay the independently parameterized Round 39 high-floor grid."""

    faces = R39.upper_outer_faces(
        R39.stress_tuples(), exact_inverse=False, tol=R39.STRESS_TOL
    )
    for face in faces:
        yield face.r, face.p, face.m, face.B


def sample_text(sample: UpperSample) -> str:
    face = sample.face
    parity = "integer" if float(sample.r).is_integer() else "half_integer"
    return (
        f"r={sample.r:g} p={sample.p} m={sample.m} q={sample.q:g} "
        f"f={sample.f} B={sample.B} B0={sample.B-1} j={sample.j} "
        f"grid={parity} t={face.t:.15g} theta={sample.theta:.15g} "
        f"d={sample.d:.12g} ep={face.ep:.12g} u={face.u:.12g} h={face.h:.12g}"
    )


def summarize(
    values: list[UpperSample],
    name: str,
    key: Callable[[UpperSample], float],
) -> UpperSample | None:
    finite = [sample for sample in values if math.isfinite(key(sample))]
    if not finite:
        print(f"diagnostic_only min_{name}=unavailable")
        return None
    best = min(finite, key=key)
    print(f"diagnostic_only min_{name}={key(best):.17g} at {sample_text(best)}")
    print(f"diagnostic_only negative_count_{name}={sum(key(sample) < 0 for sample in finite)}")
    return best


def grouped_minima(values: list[UpperSample]) -> None:
    groups: tuple[tuple[str, Callable[[UpperSample], bool]], ...] = (
        ("integer_grid", lambda s: float(s.r).is_integer()),
        ("half_integer_grid", lambda s: not float(s.r).is_integer()),
        ("j_zero", lambda s: s.j == 0),
        ("j_positive", lambda s: s.j >= 1),
        ("phase_below_1p2", lambda s: s.face.t < 1.2),
        ("phase_1p2_to_1p5", lambda s: 1.2 <= s.face.t < 1.5),
        ("phase_at_least_1p5", lambda s: s.face.t >= 1.5),
        ("B_at_most_4", lambda s: s.B <= 4),
        ("B_at_least_1000", lambda s: s.B >= 1000),
        ("active_residual", lambda s: s.active_residual),
    )
    for label, predicate in groups:
        subset = [sample for sample in values if predicate(sample)]
        if not subset:
            print(f"diagnostic_only group={label} retained=0")
            continue
        best = min(subset, key=lambda sample: sample.face.f_ob_rootfree)
        print(
            f"diagnostic_only group={label} retained={len(subset)} "
            f"min_F_OB_rootfree={best.face.f_ob_rootfree:.17g} at {sample_text(best)}"
        )


def correlation_report(values: list[UpperSample]) -> None:
    if len(values) < 20:
        print("diagnostic_only correlations=unavailable")
        return
    target = [sample.face.f_ob_rootfree for sample in values]
    features: tuple[tuple[str, Callable[[UpperSample], float]], ...] = (
        ("log_q", lambda s: math.log(s.q)),
        ("log_r", lambda s: math.log(s.r)),
        ("log_p", lambda s: math.log(s.p)),
        ("log_m", lambda s: math.log(s.m)),
        ("log_B", lambda s: math.log(s.B)),
        ("j", lambda s: float(s.j)),
        ("t", lambda s: s.face.t),
        ("d", lambda s: s.d),
        ("ep", lambda s: s.face.ep),
        ("u", lambda s: s.face.u),
        ("h", lambda s: s.face.h),
        ("p_minus_dm", lambda s: s.p - s.d * s.m),
        ("B0_zeta", lambda s: s.count_payment),
        ("Omega_rootfree", lambda s: s.omega_rootfree),
        ("adjacent", lambda s: s.adjacent),
        ("elastic", lambda s: s.elastic),
    )
    ranked: list[tuple[float, str, float]] = []
    for name, function in features:
        feature = [function(sample) for sample in values]
        rho, _ = spearmanr(feature, target)
        if math.isfinite(float(rho)):
            ranked.append((abs(float(rho)), name, float(rho)))
    for _, name, rho in sorted(ranked, reverse=True)[:10]:
        print(f"diagnostic_only spearman_F_OB_rootfree_vs_{name}={rho:.9g}")


@dataclass(frozen=True)
class RelaxedMidpoint:
    r: float
    p: float
    m: float
    v: float
    t: float
    d: float
    u_mid: float
    r_mu: float
    r_star: float
    r_branch: float
    branch: str


def relaxed_midpoint_value(
    r: float, p: float, m: float, d: float
) -> RelaxedMidpoint | None:
    """Evaluate the midpoint package on the floor-free continuous domain."""

    if not (r >= 1 and p >= 3 and m >= 1 and 0 < d < 1):
        return None
    if p - d * m <= 11 / 5:
        return None
    q = r + p + m
    mu = q + 1
    t = PI * (1 - d) / 2
    if d < 1.0e-6:
        delta = PI * d / 2
        cosine_t = math.sin(delta)
        sine_t = math.cos(delta)
        tangent_minus_t = 1 / math.tan(delta) - t
    else:
        cosine_t = math.cos(t)
        sine_t = math.sin(t)
        if t < 0.05:
            t2 = t * t
            tangent_minus_t = t * t2 * (
                1 / 3 + 2 * t2 / 15 + 17 * t2 * t2 / 315 + 62 * t2**3 / 2835
            )
        else:
            tangent_minus_t = math.tan(t) - t
    one_minus_cosine_t = 2 * math.sin(t / 2) ** 2
    cosine_psi = q * cosine_t / mu
    if not 0 < cosine_psi < 1:
        return None
    psi = math.acos(cosine_psi)
    v = q / PI * (math.tan(psi) - psi)
    if v < 7 / 4:
        return None
    outer = mu / cosine_t
    if outer * outer - PI * PI / (one_minus_cosine_t * one_minus_cosine_t) - 2 <= 0:
        return None

    zeta = d / (1 - d)
    l0 = tangent_minus_t / PI
    y = r + p / 2
    n_mid = p / 2 + m + 1
    rho = n_mid / mu
    a_mid = one_minus_cosine_t / PI
    s_mid = 2 + sine_t**2
    radicand = mu * mu - y * y * cosine_t**2
    if radicand <= 0 or s_mid - 2 * (1 - rho) <= 0:
        return None
    j_cap = 2 * R39.R27.ball_integral(mu, q)
    midpoint_payment = p * p * y * one_minus_cosine_t / (PI * math.sqrt(radicand))
    negative = -(p - d * m) / 2
    u_mid = PI / (2 * psi) - j_cap + (v - 0.75) * zeta + midpoint_payment + negative
    c_mid = (1 - rho) * a_mid / math.sqrt(s_mid - 2 * (1 - rho))
    r_mu = 0.9 + 9 * zeta / 16 + zeta * mu * l0 / 4 + p * p * c_mid + negative

    s0 = p + m + 2
    mu0 = 5 / (4 * l0)
    mu_star = max(s0, mu0)
    a_star = 1 - n_mid / mu_star
    r_star = (
        0.9
        + 9 * zeta / 16
        + zeta * mu_star * l0 / 4
        + p * p * a_star * a_mid / math.sqrt(s_mid - 2 * a_star)
        + negative
    )
    if s0 >= mu0:
        branch = "I"
        a_branch = (p / 2 + 1) / s0
        x_branch = (p + 2) * (zeta * l0 + 2 * d) / 8
        r_branch = (
            0.9
            + 9 * zeta / 16
            - p * (1 + d) / 2
            - d
            + x_branch / a_branch
            + p * p * a_mid * a_branch / math.sqrt(s_mid - 2 * a_branch)
        )
    else:
        branch = "II"
        a_branch = 1 - n_mid / mu0
        r_branch = (
            0.9
            + 7 * zeta / 8
            + d * mu0 / 2
            - p * (2 + d) / 4
            - d / 2
            + p * p * a_mid * a_branch / math.sqrt(s_mid - 2 * a_branch)
            - d * mu0 * a_branch / 2
        )
    if not all(math.isfinite(value) for value in (outer, u_mid, r_mu, r_star, r_branch)):
        return None
    return RelaxedMidpoint(r, p, m, v, t, d, u_mid, r_mu, r_star, r_branch, branch)


def relaxed_midpoint_report(count: int, seed: int) -> None:
    """Directed binary64 stress of the continuous midpoint relaxation."""

    rng = random.Random(seed)
    values: list[RelaxedMidpoint] = []
    for _ in range(count):
        if rng.random() < 0.45:
            r = 1 + rng.random() * 20
            p = 3 + rng.random() * 40
            m = 1 + rng.random() * 80
        else:
            r = math.exp(rng.uniform(0, math.log(1.0e12)))
            p = math.exp(rng.uniform(math.log(3), math.log(1.0e8)))
            m = math.exp(rng.uniform(0, math.log(1.0e8)))
        hard_ceiling = (p - 11 / 5) / m
        if hard_ceiling <= 0:
            continue
        selector = rng.random()
        fraction = selector**4 if rng.random() < 0.5 else 1 - selector**4
        d = min(0.999999, hard_ceiling * fraction)
        value = relaxed_midpoint_value(r, p, m, d)
        if value is not None:
            values.append(value)

    print("ROUND 40 RELAXED MIDPOINT STRESS")
    print("diagnostic_only=True")
    print("theorem_claim=False")
    print("arithmetic=ordinary_binary64")
    print(f"diagnostic_only relaxed_attempted={count}")
    print(f"diagnostic_only relaxed_retained={len(values)}")
    if not values:
        return
    # U_mid contains a difference of huge outer actions on the broadest
    # stress scales.  Binary64 cancellation can swamp its projection loss,
    # so this relaxed report prints only the stable R package.  U_mid is
    # still evaluated on exact retained roots and in fixed mp replays.
    for name, function in (
        ("R_mu", lambda value: value.r_mu),
        ("R_star", lambda value: value.r_star),
        ("R_branch", lambda value: value.r_branch),
    ):
        best = min(values, key=function)
        print(
            f"diagnostic_only relaxed_min_{name}={function(best):.17g} "
            f"at r={best.r:.12g} p={best.p:.12g} m={best.m:.12g} "
            f"v={best.v:.12g} t={best.t:.12g} d={best.d:.12g} branch={best.branch}"
        )
        print(
            f"diagnostic_only relaxed_negative_count_{name}="
            f"{sum(function(value) < 0 for value in values)}"
        )
    print(
        "diagnostic_only relaxed_branch_counts="
        + repr({branch: sum(value.branch == branch for value in values) for branch in ("I", "II")})
    )
    for branch in ("I", "II"):
        branch_values = [value for value in values if value.branch == branch]
        if branch_values:
            best = min(branch_values, key=lambda value: value.r_branch)
            print(
                f"diagnostic_only relaxed_min_R_branch_{branch}={best.r_branch:.17g} "
                f"at r={best.r:.12g} p={best.p:.12g} m={best.m:.12g} "
                f"v={best.v:.12g} t={best.t:.12g} d={best.d:.12g}"
            )
            print(
                f"diagnostic_only relaxed_negative_count_R_branch_{branch}="
                f"{sum(value.r_branch < 0 for value in branch_values)}"
            )
    print(
        "diagnostic_only relaxed_max_relative_R_star_minus_branch="
        f"{max(abs(value.r_star - value.r_branch) / (1 + abs(value.r_star) + abs(value.r_branch)) for value in values):.17g}"
    )
    print(
        "diagnostic_only relaxed_min_R_mu_minus_R_star="
        f"{min(value.r_mu - value.r_star for value in values):.17g}"
    )


def high_precision_replay(sample: UpperSample) -> None:
    """Noninterval replay of the sampled F_OB_rootfree minimizer."""

    mp.mp.dps = 90
    pi = mp.pi
    r = mp.mpf(str(sample.r))
    p = mp.mpf(sample.p)
    m = mp.mpf(sample.m)
    B = int(sample.B)
    f = int(sample.f)
    q = r + p + m
    mu = q + 1
    theta0 = mp.acos(q / mu)
    theta = mp.findroot(
        lambda value: q / pi * (mp.tan(value) - value) - (B - mp.mpf("0.25")),
        (mp.mpf(str(sample.theta)) * mp.mpf("0.999"), mp.mpf(str(sample.theta)) * mp.mpf("1.001")),
    )
    t = mp.acos(mu * mp.cos(theta) / q)
    outer = mu / mp.cos(t)

    def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        if z >= radius:
            return mp.mpf(0)
        return (mp.sqrt(radius * radius - z * z) - z * mp.acos(z / radius)) / pi

    def cap(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        cosine = z / radius
        return radius * radius / (4 * pi) * (
            mp.acos(cosine) * (1 + 2 * cosine * cosine)
            - 3 * cosine * mp.sqrt(1 - cosine * cosine)
        )

    shell = lambda z: action(outer, z) - action(mu, z)
    x = r + p
    ar, ax, aq = shell(r), shell(x), shell(q)
    e0 = ar + mp.mpf("0.25") - f
    ep = ax + mp.mpf("0.25") - f
    delta = e0 - ep
    e_sum = e0 + ep
    w = mu / pi * (mp.tan(t) - t)
    lam = f - mp.mpf("0.25") - w
    j = f - B
    u = lam - j
    h = action(mu, q)
    d = 1 - 2 * t / pi
    zeta = pi / (2 * t) - 1
    beta = theta / pi
    ur = mp.sqrt(mu * mu - r * r)
    ux = mp.sqrt(mu * mu - x * x)
    uq = mp.sqrt(mu * mu - q * q)
    g = ur / ux - 1
    r1 = (ur - ux) / (ux - uq)
    a_p = p * p / (3 * (2 * r + p))
    j_cap = 2 * cap(mu, q)
    omega_rf = pi * pi / (2 * outer * t**3 * mp.sin(t)) * (
        (B - 1) * B / 2 - (B - 1) * u
    )
    negative = -(p - d * m) / 2
    f_rf = (
        1 / (2 * beta)
        - j_cap
        + omega_rf
        + (B - 1) * zeta
        + p * r1 * (ax - aq)
        + a_p * g * (ax - w)
        + 2 * p * ep
        + negative
    )

    k4 = (
        (1 / mu - 1 / outer) * (x * x - r * r) / (2 * pi)
        + (1 / mu**3 - 1 / outer**3) * (x**4 - r**4) / (24 * pi)
    )
    tau = g / (g + 2)
    m4 = max(tau * (e_sum + 2 * lam), k4)
    xi_hat = delta - m4
    omega_minus = mp.nan
    f_ob = mp.nan
    gamma = mp.nan
    if B <= 200:
        omega_minus = mp.mpf(0)
        for k in range(1, B):
            level = mp.mpf(k) - mp.mpf("0.25")
            theta_k = mp.findroot(
                lambda value: outer / pi * (mp.sin(value) - value * mp.cos(value)) - level,
                (mp.mpf("1e-20"), theta),
                solver="bisect",
                tol=mp.mpf("1e-70"),
                maxsteps=400,
            )
            y = outer * mp.cos(theta_k) - q
            eta = y - mp.floor(y)
            if abs(eta) < mp.mpf("1e-70") or abs(eta - 1) < mp.mpf("1e-70"):
                eta = mp.mpf(0)
            omega_minus += pi / (2 * theta_k) - pi / (2 * t) + 2 * eta
        f_ob = f_rf - omega_rf + omega_minus
        omega = omega_minus + 1 / (2 * beta) - 1
        gamma = (
            1
            - j_cap
            + (B - 1) * zeta
            + omega
            + (p + a_p) * m4
            + 2 * p * ep
            + p * xi_hat
            + negative
        )

    print("ROUND 40 FIXED HIGH-PRECISION REPLAY")
    print("diagnostic_only=True")
    print("interval_certificate=False")
    print("arithmetic=mpmath_90_decimal_noninterval")
    print(f"diagnostic_only hp_tuple=(r,p,m,f,B)=({sample.r:g},{sample.p},{sample.m},{f},{B})")
    for name, value in (
        ("theta", theta),
        ("t", t),
        ("d", d),
        ("ep", ep),
        ("u", u),
        ("h", h),
        ("J", j_cap),
        ("Omega_rootfree", omega_rf),
        ("F_OB_rootfree", f_rf),
        ("Omega_minus", omega_minus),
        ("F_OB", f_ob),
        ("Gamma_OB", gamma),
    ):
        print(f"diagnostic_only hp_{name}={mp.nstr(value, 70)}")


def high_precision_midpoint_replay(sample: UpperSample) -> None:
    """Noninterval replay of the sampled R_* minimizer."""

    mp.mp.dps = 90
    pi = mp.pi
    r = mp.mpf(str(sample.r))
    p, m = mp.mpf(sample.p), mp.mpf(sample.m)
    B = sample.B
    q, mu = r + p + m, r + p + m + 1
    theta_seed = mp.mpf(str(sample.theta))
    theta = mp.findroot(
        lambda value: q / pi * (mp.tan(value) - value) - (B - mp.mpf("0.25")),
        (theta_seed - mp.mpf("1e-8"), theta_seed + mp.mpf("1e-8")),
        tol=mp.mpf("1e-75"),
    )
    t = mp.acos(mu * mp.cos(theta) / q)
    d = 1 - 2 * t / pi
    zeta = d / (1 - d)
    l0 = (mp.tan(t) - t) / pi
    y = r + p / 2
    n_mid = p / 2 + m + 1
    rho = n_mid / mu
    a_mid = (1 - mp.cos(t)) / pi
    s_mid = 2 + mp.sin(t) ** 2

    a_cap = mp.acos(q / mu)
    c_cap = q / mu
    j_cap = mu * mu / (2 * pi) * (
        a_cap * (1 + 2 * c_cap * c_cap)
        - 3 * c_cap * mp.sin(a_cap)
    )
    midpoint_payment = (
        p
        * p
        * y
        * (1 - mp.cos(t))
        / (pi * mp.sqrt(mu * mu - y * y * mp.cos(t) ** 2))
    )
    negative = -(p - d * m) / 2
    u_mid = pi / (2 * theta) - j_cap + (B - 1) * zeta + midpoint_payment + negative
    c_mid = (1 - rho) * a_mid / mp.sqrt(s_mid - 2 * (1 - rho))
    r_mu = mp.mpf("0.9") + 9 * zeta / 16 + zeta * mu * l0 / 4 + p * p * c_mid + negative
    s0 = p + m + 2
    mu0 = 5 / (4 * l0)
    mu_star = max(s0, mu0)
    a_star = 1 - n_mid / mu_star
    r_star = (
        mp.mpf("0.9")
        + 9 * zeta / 16
        + zeta * mu_star * l0 / 4
        + p * p * a_star * a_mid / mp.sqrt(s_mid - 2 * a_star)
        + negative
    )
    if s0 >= mu0:
        branch = "I"
        a_branch = (p / 2 + 1) / s0
        x_branch = (p + 2) * (zeta * l0 + 2 * d) / 8
        r_branch = (
            mp.mpf("0.9")
            + 9 * zeta / 16
            - p * (1 + d) / 2
            - d
            + x_branch / a_branch
            + p * p * a_mid * a_branch / mp.sqrt(s_mid - 2 * a_branch)
        )
    else:
        branch = "II"
        a_branch = 1 - n_mid / mu0
        r_branch = (
            mp.mpf("0.9")
            + 7 * zeta / 8
            + d * mu0 / 2
            - p * (2 + d) / 4
            - d / 2
            + p * p * a_mid * a_branch / mp.sqrt(s_mid - 2 * a_branch)
            - d * mu0 * a_branch / 2
        )

    print("ROUND 40 MIDPOINT MINIMUM REPLAY")
    print("diagnostic_only=True")
    print("interval_certificate=False")
    print("arithmetic=mpmath_90_decimal_noninterval")
    print(
        f"diagnostic_only midpoint_hp_tuple=(r,p,m,f,B)="
        f"({sample.r:g},{sample.p},{sample.m},{sample.f},{sample.B})"
    )
    print(f"diagnostic_only midpoint_hp_branch={branch}")
    for name, value in (
        ("theta", theta),
        ("t", t),
        ("d", d),
        ("U_mid", u_mid),
        ("R_mu", r_mu),
        ("mu_star", mu_star),
        ("R_star", r_star),
        ("R_branch", r_branch),
        ("R_star_minus_branch", r_star - r_branch),
        ("U_mid_minus_R_mu", u_mid - r_mu),
        ("R_mu_minus_R_star", r_mu - r_star),
    ):
        print(f"diagnostic_only midpoint_hp_{name}={mp.nstr(value, 70)}")


def high_precision_simplification_replays() -> None:
    """Noninterval replays of two deliberately falsified coarsenings."""

    mp.mp.dps = 90
    pi = mp.pi

    def quantities(
        r_text: str, p_int: int, m_int: int, f_int: int, B: int, theta_seed: str
    ) -> dict[str, mp.mpf]:
        r = mp.mpf(r_text)
        p, m = mp.mpf(p_int), mp.mpf(m_int)
        q, mu = r + p + m, r + p + m + 1
        theta = mp.findroot(
            lambda value: q / pi * (mp.tan(value) - value)
            - (B - mp.mpf("0.25")),
            (mp.mpf(theta_seed) - mp.mpf("1e-5"), mp.mpf(theta_seed) + mp.mpf("1e-5")),
            solver="anderson",
            tol=mp.mpf("1e-75"),
        )
        t = mp.acos(mu * mp.cos(theta) / q)
        outer = mu / mp.cos(t)

        def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
            return (
                mp.sqrt(radius * radius - z * z) - z * mp.acos(z / radius)
            ) / pi

        def cap(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
            cosine = z / radius
            return radius * radius / (4 * pi) * (
                mp.acos(cosine) * (1 + 2 * cosine * cosine)
                - 3 * cosine * mp.sqrt(1 - cosine * cosine)
            )

        shell = lambda z: action(outer, z) - action(mu, z)
        x = r + p
        e0 = shell(r) + mp.mpf("0.25") - f_int
        ep = shell(x) + mp.mpf("0.25") - f_int
        d = 1 - 2 * t / pi
        zeta = pi / (2 * t) - 1
        w = mu / pi * (mp.tan(t) - t)
        u = f_int - mp.mpf("0.25") - w - (f_int - B)
        omega_rf = pi * pi / (2 * outer * t**3 * mp.sin(t)) * (
            (B - 1) * B / 2 - (B - 1) * u
        )
        beta = theta / pi
        negative = -(p - d * m) / 2
        phase_only = 1 / (2 * beta) - mp.mpf("0.1") + omega_rf + mp.mpf("0.2") + negative
        a_p = p * p / (3 * (2 * r + p))
        ur = mp.sqrt(mu * mu - r * r)
        ux = mp.sqrt(mu * mu - x * x)
        uq = mp.sqrt(mu * mu - q * q)
        g = ur / ux - 1
        r1 = (ur - ux) / (ux - uq)
        h = action(mu, q)
        coordinate_ep = (p * r1 + a_p * g) * ep
        explicit_ep = 2 * p * ep
        hu_payment = p * r1 * h + a_p * g * u
        k4 = (
            (1 / mu - 1 / outer) * (x * x - r * r) / (2 * pi)
            + (1 / mu**3 - 1 / outer**3) * (x**4 - r**4) / (24 * pi)
        )
        j_cap = 2 * cap(mu, q)
        ccurv = 1 - j_cap + zeta + (p + a_p) * k4 + 2 * p * ep + negative
        return {
            "theta": theta,
            "t": t,
            "d": d,
            "e0": e0,
            "ep": ep,
            "u": u,
            "hard_margin": (mp.mpf("0.5") - d * m / (2 * p)) - (e0 + ep),
            "F_phase_only": phase_only,
            "F_phase_coordinate_ep": phase_only + coordinate_ep,
            "F_phase_explicit_ep": phase_only + explicit_ep,
            "F_phase_h_u": phase_only + hu_payment,
            "Ccurv": ccurv,
        }

    print("ROUND 40 FIXED SIMPLIFICATION REPLAYS")
    print("diagnostic_only=True")
    print("interval_certificate=False")
    phase = quantities("1", 5, 1, 2, 2, "1.078331394248258")
    print("diagnostic_only phase_counterexample_tuple=(r,p,m,f,B)=(1,5,1,2,2)")
    for name, value in phase.items():
        print(f"diagnostic_only phase_hp_{name}={mp.nstr(value, 70)}")
    curvature = quantities("2.5", 20, 1921, 253148, 252796, "1.568358513777853")
    print(
        "diagnostic_only curvature_counterexample_tuple="
        "(r,p,m,f,B)=(2.5,20,1921,253148,252796)"
    )
    for name, value in curvature.items():
        print(f"diagnostic_only curvature_hp_{name}={mp.nstr(value, 70)}")


def high_precision_relaxed_rejection() -> None:
    """Replay the asymptotic rejection of Q0 and Qexact at n=100."""

    mp.mp.dps = 90
    pi = mp.pi
    n = mp.mpf(100)
    r, p, m = n**6, n**3, mp.mpf(1)
    v = mp.mpf(7) / 4
    q, mu = r + p + m, r + p + m + 1
    guess = (3 * pi * v / q) ** (mp.mpf(1) / 3)
    psi = mp.findroot(
        lambda value: q / pi * (mp.tan(value) - value) - v,
        (guess * mp.mpf("0.9"), guess * mp.mpf("1.1")),
        tol=mp.mpf("1e-75"),
    )
    a_cap = mp.acos(q / mu)
    t = mp.acos(mu * mp.cos(psi) / q)
    d = 1 - 2 * t / pi
    zeta = d / (1 - d)
    outer = q / mp.cos(psi)

    def action(radius: mp.mpf, z: mp.mpf) -> mp.mpf:
        return (
            mp.sqrt(radius * radius - z * z) - z * mp.acos(z / radius)
        ) / pi

    shell = lambda z: action(outer, z) - action(mu, z)
    x = r + p
    ur = mp.sqrt(mu * mu - r * r)
    ux = mp.sqrt(mu * mu - x * x)
    uq = mp.sqrt(mu * mu - q * q)
    p_transport = uq / q * (ur - ux)
    r1 = (ur - ux) / (ux - uq)
    adjacent = shell(x) - shell(q)
    c_cap = q / mu
    j_cap = mu * mu / (2 * pi) * (
        a_cap * (1 + 2 * c_cap * c_cap)
        - 3 * c_cap * mp.sin(a_cap)
    )
    base = pi / (2 * psi) - j_cap + (v - mp.mpf("0.75")) * zeta - (p - d * m) / 2
    q0 = base + p * p_transport * (psi - a_cap) / pi
    q_exact = base + p * r1 * adjacent

    l0 = (mp.tan(t) - t) / pi
    y = r + p / 2
    n_mid = p / 2 + m + 1
    rho = n_mid / mu
    a_mid = (1 - mp.cos(t)) / pi
    s_mid = 2 + mp.sin(t) ** 2
    midpoint_payment = (
        p
        * p
        * y
        * (1 - mp.cos(t))
        / (pi * mp.sqrt(mu * mu - y * y * mp.cos(t) ** 2))
    )
    u_mid = base + midpoint_payment
    negative = -(p - d * m) / 2
    c_mid = (1 - rho) * a_mid / mp.sqrt(s_mid - 2 * (1 - rho))
    r_mu = mp.mpf("0.9") + 9 * zeta / 16 + zeta * mu * l0 / 4 + p * p * c_mid + negative
    s0 = p + m + 2
    mu0 = 5 / (4 * l0)
    mu_star = max(s0, mu0)
    a_star = 1 - n_mid / mu_star
    r_star = (
        mp.mpf("0.9")
        + 9 * zeta / 16
        + zeta * mu_star * l0 / 4
        + p * p * a_star * a_mid / mp.sqrt(s_mid - 2 * a_star)
        + negative
    )

    print("ROUND 40 RELAXED Q0/QEXACT REJECTION REPLAY")
    print("diagnostic_only=True")
    print("interval_certificate=False")
    print("arithmetic=mpmath_90_decimal_noninterval")
    print("diagnostic_only relaxed_hp_family=n=100,r=n^6,p=n^3,m=1,v=7/4")
    for name, value in (
        ("psi", psi),
        ("t", t),
        ("d", d),
        ("gap_u", v - action(outer, mu)),
        ("Delta", shell(r) - shell(x)),
        ("Q0", q0),
        ("Qexact", q_exact),
        ("U_mid", u_mid),
        ("R_mu", r_mu),
        ("R_star", r_star),
    ):
        print(f"diagnostic_only relaxed_hp_{name}={mp.nstr(value, 70)}")


def run(args: argparse.Namespace) -> None:
    values: list[UpperSample] = []
    seen: set[tuple[int, int, int, int]] = set()
    attempted = 0

    streams_list: list[Iterable[tuple[float, int, int, int]]] = [
        deterministic_candidates(args.q_max, args.b_max),
        directed_random_candidates(args.random, args.seed),
    ]
    if not args.skip_round39_stress:
        streams_list.append(round39_stress_candidates())
    streams: Iterable[Iterable[tuple[float, int, int, int]]] = streams_list
    for stream in streams:
        for r, p, m, B in stream:
            key = (int(round(2 * r)), p, m, B)
            if key in seen:
                continue
            seen.add(key)
            attempted += 1
            sample = build_sample(r, p, m, B, exact_b_max=args.exact_b_max)
            if sample is not None:
                values.append(sample)

    print("ROUND 40 UPPER-ALPHA OUTER-B ADVERSARIAL SEARCH")
    print("diagnostic_only=True")
    print("theorem_claim=False")
    print("arithmetic=ordinary_binary64")
    print("interval_certificate=False")
    print("continuum_sign_status=not_assessed")
    print("endpoint_owner=alpha_up_to_1_gap_side")
    print(f"attempted_unique={attempted}")
    print(f"retained_feasible={len(values)}")
    print(f"retained_integer_grid={sum(float(v.r).is_integer() for v in values)}")
    print(f"retained_half_integer_grid={sum(not float(v.r).is_integer() for v in values)}")
    print(f"retained_active_p_minus_dm_gt_11_over_5={sum(v.active_residual for v in values)}")
    print(f"exact_old_inverse_retained={sum(math.isfinite(v.face.f_ob) for v in values)}")
    if not values:
        print("scan_status=diagnostic_only_no_feasible_roots")
        return

    metrics: tuple[tuple[str, Callable[[UpperSample], float]], ...] = (
        ("Gamma_OB_exact_subset", lambda s: s.face.gamma_gap),
        ("F_OB_exact_subset", lambda s: s.face.f_ob),
        ("F_OB_rootfree", lambda s: s.face.f_ob_rootfree),
        ("H_Delta", lambda s: s.face.h_delta),
        ("Ccurv", lambda s: s.face.ccurv),
        ("Ccurv_drop_2pep", lambda s: s.face.ccurv_drop_2pep),
        ("RHS_R38_20_exact_subset", lambda s: s.face.rhs_r3820),
        ("F_OB_rootfree_drop_2pep", lambda s: s.face.f_ob_rootfree_drop_2pep),
        ("F_cap_count", lambda s: s.f_cap_count),
        ("F_cap_count_drop_2pep", lambda s: s.f_cap_count_drop_2pep),
        ("F_drop_j", lambda s: s.f_drop_j),
        ("F_no_omega", lambda s: s.f_no_omega),
        ("F_no_ap", lambda s: s.f_no_ap),
        ("F_no_adjacent", lambda s: s.f_no_adjacent),
        ("F_ep_only", lambda s: s.f_ep_only),
        ("F_drop_all_ep", lambda s: s.f_drop_all_ep),
        ("F_drop_h_u", lambda s: s.f_drop_h_u),
        ("F_phase_only", lambda s: s.f_phase_only),
        ("F_phase_h_u", lambda s: s.f_phase_h_u),
        ("F_phase_coordinate_ep", lambda s: s.f_phase_coordinate_ep),
        ("F_phase_explicit_ep", lambda s: s.f_phase_explicit_ep),
        ("F_phase_h_u_coordinate_ep", lambda s: s.f_phase_h_u_coordinate_ep),
        ("F_phase_h_u_explicit_ep", lambda s: s.f_phase_h_u_explicit_ep),
        ("U_mid", lambda s: s.u_mid_scalar),
        ("R_mu", lambda s: s.r_mid_projected),
        ("R_star", lambda s: s.r_star),
        ("R_branch", lambda s: s.r_branch),
    )
    minima: dict[str, UpperSample] = {}
    for name, key in metrics:
        best = summarize(values, name, key)
        if best is not None:
            minima[name] = best

    grouped_minima(values)
    correlation_report(values)
    print(
        "diagnostic_only midpoint_branch_counts="
        + repr(
            {
                branch: sum(sample.r_branch_kind == branch for sample in values)
                for branch in ("I", "II")
            }
        )
    )
    for branch in ("I", "II"):
        branch_values = [sample for sample in values if sample.r_branch_kind == branch]
        if branch_values:
            best_branch = min(branch_values, key=lambda sample: sample.r_branch)
            print(
                f"diagnostic_only min_R_branch_{branch}={best_branch.r_branch:.17g} "
                f"at {sample_text(best_branch)}"
            )
            print(
                f"diagnostic_only negative_count_R_branch_{branch}="
                f"{sum(sample.r_branch < 0 for sample in branch_values)}"
            )
    print(
        "diagnostic_only max_abs_R_star_minus_branch="
        f"{max(abs(sample.r_branch_residual) for sample in values):.17g}"
    )
    print(
        "diagnostic_only min_U_mid_minus_R_mu="
        f"{min(sample.u_mid_scalar - sample.r_mid_projected for sample in values):.17g}"
    )
    print(
        "diagnostic_only min_R_mu_minus_R_star="
        f"{min(sample.r_mid_projected - sample.r_star for sample in values):.17g}"
    )

    active = [sample for sample in values if sample.active_residual]
    if active:
        print(f"diagnostic_only active_subset_retained={len(active)}")
        for name, key in metrics[:9]:
            summarize(active, "active_" + name, key)

    if not args.skip_relaxed_midpoint and args.relaxed_random > 0:
        relaxed_midpoint_report(args.relaxed_random, args.seed + 97)

    if not args.skip_high_precision and "F_OB_rootfree" in minima:
        high_precision_replay(minima["F_OB_rootfree"])
        high_precision_simplification_replays()
        if "R_star" in minima:
            high_precision_midpoint_replay(minima["R_star"])
        high_precision_relaxed_rejection()
    print("scan_status=diagnostic_only")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=75)
    parser.add_argument("--b-max", type=int, default=16)
    parser.add_argument("--random", type=int, default=120_000)
    parser.add_argument("--seed", type=int, default=4001)
    parser.add_argument("--exact-b-max", type=int, default=40)
    parser.add_argument("--skip-round39-stress", action="store_true")
    parser.add_argument("--relaxed-random", type=int, default=80_000)
    parser.add_argument("--skip-relaxed-midpoint", action="store_true")
    parser.add_argument("--skip-high-precision", action="store_true")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
