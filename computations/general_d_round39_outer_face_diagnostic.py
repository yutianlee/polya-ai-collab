#!/usr/bin/env python3
"""Round 39 directed diagnostic for the two primary outer-B faces.

This program is theorem-design evidence only.  Its finite searches use
ordinary binary64 arithmetic and SciPy root finding.  The optional fixed
counterexample replay uses high-precision mpmath arithmetic, but it is not
directed interval arithmetic and is not a certificate.

The two exact geometric parameterizations are:

* upper alpha/outer-B: alpha=1 and G_K(q)=B-1/4;
* lower shelf/outer-B: A(x)=f-1/4 and G_K(q)=B-1/4, solved jointly by
  using alpha as the outer-wall root parameter.

All retained records are then checked against the first-shelf, first-drop,
activity, hard-residual, strict-count, and positive-alpha gap constraints.
At an old inverse wall, the outer-gap-side owner is the adverse side
eta_k=0; away from a wall this is simply the ordinary fractional part.

No positive minimum printed here proves a continuum sign.  A negative
``Ccurv`` or ``Lj`` value falsifies only that displayed auxiliary lower
margin, not Gamma_gap, H_Delta, Phi_delta^+, the exact shifted-tail scalar,
CST, or Polya.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

import mpmath as mp
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
ROUND27_PATH = (
    ROOT / "computations" / "general_d_round27_exact_phi_hard_sector_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location("round27_round39_outer", ROUND27_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise SystemExit(f"cannot import {ROUND27_PATH}")
R27 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = R27
SPEC.loader.exec_module(R27)


PI = math.pi
UPPER_TOL = 2.0e-8
LOWER_TOL = 2.0e-7
STRESS_TOL = 2.0e-5
ALPHA_EPS = 1.0e-9


@dataclass(frozen=True)
class FaceValue:
    kind: str
    r: float
    p: int
    m: int
    f: int
    B: int
    alpha: float
    t: float
    e0: float
    ep: float
    u: float
    h: float
    gamma_gap: float
    h_delta: float
    rhs_r3820: float
    phi_delta_plus: float
    ccurv: float
    ccurv_drop_2pep: float
    f_ob: float
    f_ob_drop_2pep: float
    f_ob_rootfree: float
    f_ob_rootfree_drop_2pep: float
    lj: float
    lj_rootfree: float
    omega_minus: float
    omega_rootfree: float

    @property
    def j(self) -> int:
        return self.f - self.B

    @property
    def b0(self) -> int:
        return self.B - 1


def hard_interval(
    r: float, p: int, m: int, f: int, alpha: float
) -> tuple[float, float, float, float] | None:
    """Return the exact-owner first-shelf hard interval in t."""

    try:
        interval = R27.feasible_interval(r, p, m, f, alpha)
    except (ArithmeticError, ValueError, OverflowError, ZeroDivisionError):
        return None
    if interval is None:
        return None
    lo, hi, mu, q = interval
    d_lo = 1 - 2 * lo / PI
    if not (p > d_lo * m and R27.hard_gap(r, p, m, f, alpha, lo) < 0):
        return None
    hard_hi = hi
    if R27.hard_gap(r, p, m, f, alpha, hi) >= 0:
        try:
            hard_hi = brentq(
                lambda t: R27.hard_gap(r, p, m, f, alpha, t),
                lo,
                hi,
                xtol=2.0e-14,
                rtol=2.0e-14,
            )
        except (ValueError, ArithmeticError):
            return None
    return (lo, hard_hi, mu, q) if lo < hard_hi else None


def quartic_payment(mu: float, outer: float, r: float, p: int) -> float:
    x = r + p
    return (
        (mu ** (-1) - outer ** (-1)) * (x * x - r * r) / (2 * PI)
        + (mu ** (-3) - outer ** (-3))
        * (x**4 - r**4)
        / (24 * PI)
    )


def evaluate_outer_face(
    kind: str,
    r: float,
    p: int,
    m: int,
    f: int,
    B: int,
    alpha: float,
    t: float,
    *,
    exact_inverse: bool,
    tol: float,
) -> FaceValue | None:
    """Evaluate one exact gap-side outer-B endpoint."""

    q = r + p + m
    mu = q + alpha
    x = r + p
    outer = mu / math.cos(t)
    d = 1 - 2 * t / PI
    zeta = PI / (2 * t) - 1
    b0 = B - 1
    j = f - B
    if b0 < 1 or j < 0:
        return None

    ar = R27.shell_action(mu, t, r)
    ax = R27.shell_action(mu, t, x)
    ax1 = R27.shell_action(mu, t, x + 1)
    aq = R27.shell_action(mu, t, q)
    v = R27.ball_action(outer, q)
    h = R27.ball_action(mu, q)
    e0 = ar + 0.25 - f
    ep = ax + 0.25 - f
    e_sum = e0 + ep
    delta = e0 - ep
    w = mu / PI * (math.tan(t) - t)
    lam = f - 0.25 - w
    u = lam - j

    if abs(v - (B - 0.25)) > 10 * tol:
        return None
    if min(e0, ep) < -tol or max(e0, ep) >= 1 + tol:
        return None
    if kind == "outer_lower" and abs(ep) > tol:
        return None
    if kind == "outer_lower":
        # These two facts are exact consequences of the defining equation
        # A(x)=f-1/4 and strict action decrease from x to x+1.  Reapplying a
        # floating floor to a value of size f is unreliable in the stress
        # scan and would reject valid roots through cancellation alone.
        if abs(ep) > tol or not (0 - tol <= e0 < 1 + tol):
            return None
    else:
        if R27.ordinary_floor(ar + 0.25) != f:
            return None
        if R27.ordinary_floor(ax + 0.25) != f:
            return None
        if R27.ordinary_floor(ax1 + 0.25) == f:
            return None
    activity_gamma = 0.75 if float(r).is_integer() else 2.0
    if R27.activity_margin(mu, t, activity_gamma) <= -tol:
        return None
    if not (p > d * m and e_sum < 0.5 - d * m / (2 * p) + tol):
        return None
    if not (h - tol < u < alpha / 2 + tol):
        return None
    if not (b0 + 0.25 - tol < w < b0 + 0.75 + tol):
        return None
    # At the outer wall aq=B-1/4-h.  Thus 0<h<1 owns Q=B-1 exactly;
    # checking a large floating action with a floor would only add noise.
    if not (0 < h < 1):
        return None

    beta = math.acos(q / outer) / PI
    if beta <= 0:
        return None

    omega_minus = math.nan
    omega = math.nan
    complete_old_inverse = math.nan
    if exact_inverse:
        omega_minus = 0.0
        complete_old_inverse = 0.0
        for k in range(1, B):
            theta = R27.inverse_angle(outer, k - 0.25)
            y = outer * math.cos(theta) - q
            # Moving from the outer wall into its gap owner increases y.
            # Thus a simultaneous old inverse wall is owned adversely.
            eta = y - math.floor(y)
            omega_minus += PI / (2 * theta) - PI / (2 * t) + 2 * eta
            complete_old_inverse += PI / (2 * theta) - 1 + 2 * eta
        omega = omega_minus + 1 / (2 * beta) - 1

    stretch = math.sqrt((mu * mu - r * r) / (mu * mu - x * x))
    g = stretch - 1
    tau = g / (g + 2)
    elastic = tau * (e_sum + 2 * lam)
    k4 = quartic_payment(mu, outer, r, p)
    m4 = max(elastic, k4)
    xi_hat = delta - m4
    if xi_hat < -tol:
        return None

    a_p = p * p / (3 * (2 * r + p))
    j_cap = 2 * R27.ball_integral(mu, q)
    negative = -(p - d * m) / 2

    ur = math.sqrt(mu * mu - r * r)
    ux = math.sqrt(mu * mu - x * x)
    uq = math.sqrt(mu * mu - q * q)
    r1 = (ur - ux) / (ux - uq)
    a_star = (p + a_p) * g
    h_star = (p + a_p) * r1

    shelf_elastic = (f - 1) * min(zeta, a_star) + a_star * (u + ep)
    shelf_curvature = zeta + (p + a_p) * k4
    shelf_adjacent = (f - 1) * min(zeta, h_star) + h_star * ep
    h_delta = (
        1
        - j_cap
        + max(shelf_elastic, shelf_curvature, shelf_adjacent)
        + 2 * p * ep
        + negative
    )

    omega_rootfree = PI * PI / (2 * outer * t**3 * math.sin(t)) * (
        b0 * (b0 + 1) / 2 - b0 * u
    )

    ccurv = 1 - j_cap + shelf_curvature + 2 * p * ep + negative
    ccurv_drop = ccurv - 2 * p * ep

    # The direct outer-face bound supplied by the Round 39 dependency audit.
    common_f = (
        1 / (2 * beta)
        - j_cap
        + b0 * zeta
        + p * r1 * (ax - aq)
        + a_p * g * (ax - w)
        + 2 * p * ep
        + negative
    )
    f_rootfree = common_f + omega_rootfree
    f_rootfree_drop = f_rootfree - 2 * p * ep
    f_ob = math.nan
    f_ob_drop = math.nan
    gamma_gap = math.nan
    rhs_r3820 = math.nan
    phi_delta_plus = math.nan
    if exact_inverse:
        f_ob = common_f + omega_minus
        f_ob_drop = f_ob - 2 * p * ep
        gamma_gap = (
            1
            - j_cap
            + b0 * zeta
            + omega
            + (p + a_p) * m4
            + 2 * p * ep
            + p * xi_hat
            + negative
        )
        lt_direct = (
            1
            - j_cap
            + complete_old_inverse
            + 1 / (2 * beta)
            - 1
        )
        e_star = (p - d * m) / (2 * p)
        phi_delta_plus = lt_direct + a_p * delta + p * (e_sum - e_star)
        rhs_r3820 = (
            1 / (2 * beta)
            - j_cap
            + omega_minus
            + (f - 1) * min(zeta, h_star)
            + h_star * ep
            + h * min(h_star, 2 / beta)
            + 2 * p * ep
            + negative
        )

    # Coarse j>=1 lower-shelf test requested in Round 39.  It is printed
    # for every face, but has its intended interpretation only when j>=1.
    lj = 37 / 35 + p * r1 + a_p * g + negative
    lj_rootfree = lj + omega_rootfree

    return FaceValue(
        kind=kind,
        r=r,
        p=p,
        m=m,
        f=f,
        B=B,
        alpha=alpha,
        t=t,
        e0=e0,
        ep=ep,
        u=u,
        h=h,
        gamma_gap=gamma_gap,
        h_delta=h_delta,
        rhs_r3820=rhs_r3820,
        phi_delta_plus=phi_delta_plus,
        ccurv=ccurv,
        ccurv_drop_2pep=ccurv_drop,
        f_ob=f_ob,
        f_ob_drop_2pep=f_ob_drop,
        f_ob_rootfree=f_rootfree,
        f_ob_rootfree_drop_2pep=f_rootfree_drop,
        lj=lj,
        lj_rootfree=lj_rootfree,
        omega_minus=omega_minus,
        omega_rootfree=omega_rootfree,
    )


def upper_outer_faces(
    tuples: Iterable[tuple[float, int, int, int]],
    *,
    exact_inverse: bool = True,
    tol: float = UPPER_TOL,
) -> list[FaceValue]:
    values: list[FaceValue] = []
    alpha = 1.0
    for r, p, m, f in tuples:
        interval = hard_interval(r, p, m, f, alpha)
        if interval is None:
            continue
        lo, hi, mu, q = interval
        count = lambda t: R27.ball_action(mu / math.cos(t), q) + 0.25
        c_lo, c_hi = count(lo), count(hi)
        b_lo = max(2, math.ceil(c_lo - 1.0e-10))
        b_hi = min(f, math.floor(c_hi + 1.0e-10))
        for B in range(b_lo, b_hi + 1):
            try:
                t = brentq(
                    lambda value, B=B: count(value) - B,
                    lo,
                    hi,
                    xtol=5.0e-15,
                    rtol=1.0e-14,
                )
            except (ValueError, ArithmeticError):
                continue
            item = evaluate_outer_face(
                "outer_upper",
                r,
                p,
                m,
                f,
                B,
                alpha,
                t,
                exact_inverse=exact_inverse,
                tol=tol,
            )
            if item is not None:
                values.append(item)
    return values


def lower_shelf_t(r: float, p: int, m: int, f: int, alpha: float) -> float | None:
    mu = r + p + m + alpha
    x = r + p
    try:
        return R27.increasing_root(
            lambda t: R27.shell_action(mu, t, x), f - 0.25
        )
    except (ValueError, ArithmeticError, OverflowError, ZeroDivisionError):
        return None


def lower_outer_count(r: float, p: int, m: int, f: int, alpha: float) -> float | None:
    t = lower_shelf_t(r, p, m, f, alpha)
    if t is None:
        return None
    q = r + p + m
    mu = q + alpha
    return R27.ball_action(mu / math.cos(t), q) + 0.25


def lower_roots(
    r: float,
    p: int,
    m: int,
    f: int,
    *,
    stress: bool,
) -> list[tuple[float, int]]:
    if stress:
        alpha_grid = (ALPHA_EPS, 1 - ALPHA_EPS)
    else:
        alpha_grid = (
            1.0e-8,
            0.01,
            0.05,
            0.1,
            0.2,
            0.35,
            0.5,
            0.65,
            0.8,
            0.9,
            0.97,
            0.99999999,
        )
    samples: list[tuple[float, float]] = []
    for alpha in alpha_grid:
        count = lower_outer_count(r, p, m, f, alpha)
        if count is not None and math.isfinite(count):
            samples.append((alpha, count))

    roots: list[tuple[float, int]] = []
    for (a0, v0), (a1, v1) in zip(samples, samples[1:]):
        b_lo = max(2, math.ceil(min(v0, v1) - 1.0e-10))
        b_hi = min(f, math.floor(max(v0, v1) + 1.0e-10))
        for B in range(b_lo, b_hi + 1):
            if (v0 - B) * (v1 - B) > 0:
                continue
            try:
                alpha = brentq(
                    lambda value, B=B: (
                        lower_outer_count(r, p, m, f, value) - B
                    ),
                    a0,
                    a1,
                    xtol=1.0e-12,
                    rtol=1.0e-12,
                )
            except (ValueError, ArithmeticError, TypeError):
                continue
            if all(B != old_B or abs(alpha - old_a) > 1.0e-8 for old_a, old_B in roots):
                roots.append((alpha, B))
    return roots


def lower_outer_faces(
    tuples: Iterable[tuple[float, int, int, int]], *, stress: bool
) -> list[FaceValue]:
    values: list[FaceValue] = []
    for r, p, m, f in tuples:
        for alpha, B in lower_roots(r, p, m, f, stress=stress):
            t = lower_shelf_t(r, p, m, f, alpha)
            if t is None:
                continue
            item = evaluate_outer_face(
                "outer_lower",
                r,
                p,
                m,
                f,
                B,
                alpha,
                t,
                exact_inverse=not stress,
                tol=STRESS_TOL if stress else LOWER_TOL,
            )
            if item is not None:
                values.append(item)
    return values


def bounded_tuples() -> list[tuple[float, int, int, int]]:
    tuples: list[tuple[float, int, int, int]] = []
    radii = (
        [float(value) for value in range(1, 31)]
        + [value + 0.5 for value in range(1, 31)]
        + [100.0, 1000.0, 1.0e6]
    )
    shelf_lengths = list(range(3, 31)) + [40, 60, 100, 300]
    gaps = list(range(1, 16)) + [30, 100]
    floors = list(range(2, 7))
    for r in radii:
        for p in shelf_lengths:
            for m in gaps:
                for f in floors:
                    tuples.append((r, p, m, f))

    random.seed(3902)
    for _ in range(20_000):
        r = float(round(math.exp(random.uniform(0, math.log(1.0e8)))))
        if random.randrange(2):
            r += 0.5
        p = max(3, round(math.exp(random.uniform(math.log(3), math.log(3000)))))
        m = max(1, round(math.exp(random.uniform(0, math.log(1000)))))
        f = random.choice((2, 2, 3, 4, 6, 10, 20))
        tuples.append((r, p, m, f))
    return tuples


def stress_tuples() -> list[tuple[float, int, int, int]]:
    floors = sorted(
        set(
            list(range(20, 201))
            + [
                round(
                    math.exp(
                        math.log(200)
                        + (math.log(200_000) - math.log(200)) * index / 400
                    )
                )
                for index in range(401)
            ]
        )
    )
    tuples: list[tuple[float, int, int, int]] = []
    for r in (1.0, 1.5, 2.0, 2.5):
        for p in (3, 4, 5, 8):
            for m in (5, 7, 10, 12, 15, 20, 30, 50, 80, 120, 200, 400):
                for f in floors:
                    tuples.append((r, p, m, f))

    random.seed(3904)
    for _ in range(40_000):
        r = random.choice((1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 5.0, 10.0))
        p = random.choice((3, 3, 3, 4, 5, 6, 8, 10, 20))
        m = max(1, round(math.exp(random.uniform(math.log(2), math.log(2000)))))
        f = max(
            20,
            round(math.exp(random.uniform(math.log(20), math.log(500_000)))),
        )
        tuples.append((r, p, m, f))
    return tuples


def point_text(item: FaceValue) -> str:
    return (
        f"face={item.kind} r={item.r:g} p={item.p} m={item.m} "
        f"f={item.f} B={item.B} B0={item.b0} j={item.j} "
        f"alpha={item.alpha:.15g} t={item.t:.15g} "
        f"e0={item.e0:.12g} ep={item.ep:.12g} "
        f"u={item.u:.12g} h={item.h:.12g}"
    )


def summarize(
    face_name: str,
    values: list[FaceValue],
    name: str,
    key: Callable[[FaceValue], float],
) -> None:
    finite = [item for item in values if math.isfinite(key(item))]
    if not finite:
        print(f"diagnostic_only {face_name}_min_{name}=unavailable")
        return
    best = min(finite, key=key)
    print(
        f"diagnostic_only {face_name}_min_{name}={key(best):.17g} "
        f"at {point_text(best)}"
    )


def high_precision_ccurv_replay() -> None:
    """Nonrigorous 100-digit replay of one feasible negative Ccurv root."""

    mp.mp.dps = 100
    pi = mp.pi
    r, p, m, f, B = mp.mpf(1), mp.mpf(4), mp.mpf(20), mp.mpf(171), 167
    x, q = r + p, r + p + m

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

    def equations(alpha: mp.mpf, t: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        mu = q + alpha
        outer = mu / mp.cos(t)
        return (
            action(outer, x) - action(mu, x) - (f - mp.mpf("0.25")),
            action(outer, q) - (mp.mpf(B) - mp.mpf("0.25")),
        )

    alpha, t = mp.findroot(
        equations,
        (mp.mpf("0.6819"), mp.mpf("1.52513")),
        tol=mp.mpf("1e-85"),
        maxsteps=100,
    )
    mu = q + alpha
    outer = mu / mp.cos(t)
    shell = lambda z: action(outer, z) - action(mu, z)
    e0 = shell(r) + mp.mpf("0.25") - f
    ep = shell(x) + mp.mpf("0.25") - f
    e_sum = e0 + ep
    d = 1 - 2 * t / pi
    zeta = pi / (2 * t) - 1
    w = mu / pi * (mp.tan(t) - t)
    u = f - mp.mpf("0.25") - w - (f - B)
    h = action(mu, q)
    a_p = p * p / (3 * (2 * r + p))
    j_cap = 2 * cap(mu, q)
    k4 = (
        (1 / mu - 1 / outer) * (x * x - r * r) / (2 * pi)
        + (1 / mu**3 - 1 / outer**3) * (x**4 - r**4) / (24 * pi)
    )
    ccurv = (
        1
        - j_cap
        + zeta
        + (p + a_p) * k4
        + 2 * p * ep
        - (p - d * m) / 2
    )
    beta = mp.acos(q / outer) / pi
    ur = mp.sqrt(mu * mu - r * r)
    ux = mp.sqrt(mu * mu - x * x)
    uq = mp.sqrt(mu * mu - q * q)
    g = ur / ux - 1
    r1 = (ur - ux) / (ux - uq)
    b0 = B - 1
    omega_rootfree = pi * pi / (2 * outer * t**3 * mp.sin(t)) * (
        b0 * (b0 + 1) / 2 - b0 * u
    )
    lj = mp.mpf(37) / 35 + p * r1 + a_p * g - (p - d * m) / 2
    f_ob_rootfree = (
        1 / (2 * beta)
        - j_cap
        + omega_rootfree
        + b0 * zeta
        + p * r1 * (shell(x) - shell(q))
        + a_p * g * (shell(x) - w)
        + 2 * p * ep
        - (p - d * m) / 2
    )
    hard_margin = (mp.mpf("0.5") - d * m / (2 * p)) - e_sum
    first_drop_margin = f - (shell(x + 1) + mp.mpf("0.25"))
    activity = (
        outer * outer - pi * pi / (1 - mp.cos(t)) ** 2 - mp.mpf("0.75")
    )

    print("HIGH-PRECISION FIXED REPLAY")
    print("diagnostic_only=True")
    print("arithmetic=mpmath_100_decimal_nonrigorous")
    print("interval_certificate=False")
    for name, value in (
        ("alpha", alpha),
        ("t", t),
        ("e0", e0),
        ("ep", ep),
        ("first_drop_margin", first_drop_margin),
        ("p_minus_dm", p - d * m),
        ("hard_margin", hard_margin),
        ("alpha_half_minus_u", alpha / 2 - u),
        ("u_minus_h", u - h),
        ("W_lower_margin", w - ((B - 1) + mp.mpf("0.25"))),
        ("W_upper_margin", ((B - 1) + mp.mpf("0.75")) - w),
        ("activity_margin", activity),
        ("Ccurv", ccurv),
        ("Ccurv_drop_2pep", ccurv - 2 * p * ep),
        ("Lj", lj),
        ("Omega_rootfree", omega_rootfree),
        ("Lj_plus_Omega_rootfree", lj + omega_rootfree),
        ("F_OB_rootfree", f_ob_rootfree),
    ):
        print(f"diagnostic_only hp_{name}={mp.nstr(value, 70)}")


def report_bounded() -> None:
    tuples = bounded_tuples()
    upper = upper_outer_faces(tuples)
    lower = lower_outer_faces(tuples, stress=False)
    print("ROUND 39 OUTER-FACE BOUNDED SEARCH")
    print("diagnostic_only=True")
    print("theorem_claim=False")
    print("arithmetic=ordinary_binary64")
    print("continuum_sign_status=not_assessed")
    print("upper_endpoint_owner=alpha_up_to_1_gap_side")
    print(f"tuple_count={len(tuples)}")
    print(f"upper_outer_feasible={len(upper)}")
    print(f"lower_outer_feasible={len(lower)}")
    print(
        "diagnostic_only lower_j_counts="
        + repr({j: sum(item.j == j for item in lower) for j in sorted({x.j for x in lower})})
    )
    print(
        "diagnostic_only lower_min_j="
        + (str(min(item.j for item in lower)) if lower else "unavailable")
        + "; lower_min_B0="
        + (str(min(item.b0 for item in lower)) if lower else "unavailable")
    )

    metrics = (
        ("Gamma_gap", lambda x: x.gamma_gap),
        ("H_Delta", lambda x: x.h_delta),
        ("RHS_R38_20", lambda x: x.rhs_r3820),
        ("Phi_delta_plus", lambda x: x.phi_delta_plus),
        ("Ccurv", lambda x: x.ccurv),
        ("Ccurv_drop_2pep", lambda x: x.ccurv_drop_2pep),
        ("F_OB", lambda x: x.f_ob),
        ("F_OB_drop_2pep", lambda x: x.f_ob_drop_2pep),
        ("F_OB_rootfree", lambda x: x.f_ob_rootfree),
        ("F_OB_rootfree_drop_2pep", lambda x: x.f_ob_rootfree_drop_2pep),
    )
    for face_name, values in (("upper", upper), ("lower", lower)):
        for name, key in metrics:
            summarize(face_name, values, name, key)
    summarize("lower", lower, "Lj", lambda x: x.lj)
    summarize("lower", lower, "Lj_plus_Omega_rootfree", lambda x: x.lj_rootfree)
    print(
        "diagnostic_only lower_negative_counts "
        f"Ccurv={sum(x.ccurv < 0 for x in lower)} "
        f"F_OB={sum(x.f_ob < 0 for x in lower)} "
        f"F_OB_rootfree={sum(x.f_ob_rootfree < 0 for x in lower)} "
        f"Lj={sum(x.lj < 0 for x in lower)} "
        f"Lj_plus_Omega_rootfree={sum(x.lj_rootfree < 0 for x in lower)}"
    )


def report_stress() -> None:
    tuples = stress_tuples()
    upper = upper_outer_faces(tuples, exact_inverse=False, tol=STRESS_TOL)
    lower = lower_outer_faces(tuples, stress=True)
    print("ROUND 39 HIGH-FLOOR LOWER/OUTER STRESS SEARCH")
    print("diagnostic_only=True")
    print("theorem_claim=False")
    print("arithmetic=ordinary_binary64")
    print("continuum_sign_status=not_assessed")
    print(f"stress_tuple_count={len(tuples)}")
    print(f"stress_upper_feasible={len(upper)}")
    print(f"stress_lower_feasible={len(lower)}")
    for name, key in (
        ("Ccurv", lambda x: x.ccurv),
        ("F_OB_rootfree", lambda x: x.f_ob_rootfree),
    ):
        summarize("stress_upper", upper, name, key)
    for name, key in (
        ("Ccurv", lambda x: x.ccurv),
        ("F_OB_rootfree", lambda x: x.f_ob_rootfree),
        ("Lj", lambda x: x.lj),
        ("Lj_plus_Omega_rootfree", lambda x: x.lj_rootfree),
    ):
        summarize("stress_lower", lower, name, key)
    print(
        "diagnostic_only stress_upper_negative_counts "
        f"Ccurv={sum(x.ccurv < 0 for x in upper)} "
        f"F_OB_rootfree={sum(x.f_ob_rootfree < 0 for x in upper)}"
    )
    print(
        "diagnostic_only stress_lower_negative_counts "
        f"Ccurv={sum(x.ccurv < 0 for x in lower)} "
        f"F_OB_rootfree={sum(x.f_ob_rootfree < 0 for x in lower)} "
        f"Lj={sum(x.lj < 0 for x in lower)} "
        f"Lj_plus_Omega_rootfree={sum(x.lj_rootfree < 0 for x in lower)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--high-floor-stress",
        action="store_true",
        help="also run the large-f lower-shelf/outer-B stress scan",
    )
    parser.add_argument(
        "--skip-high-precision",
        action="store_true",
        help="skip the fixed 100-decimal Ccurv replay",
    )
    args = parser.parse_args()
    report_bounded()
    if args.high_floor_stress:
        report_stress()
    if not args.skip_high_precision:
        high_precision_ccurv_replay()
    print("scan_status=diagnostic_only")


if __name__ == "__main__":
    main()
