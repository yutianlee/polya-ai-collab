#!/usr/bin/env python3
"""Rigorous compact verification for the remaining f=2,3 no-drop rows.

The proof variables are

    sigma = sqrt((K-mu)/K),       kappa = sigma*(K-mu),
    K = kappa/sigma**3,           mu = kappa*(1-sigma**2)/sigma**3,
    q = mu-alpha,                 r = q-n.

Only sigma >= 1/10 is treated here; the complementary sector is the
analytic Round 5 transfer.  The checked-in default mode is an Arb
certificate.  ``--diagnostic`` runs a non-rigorous floating-point scan and
is never used in a proof decision.
"""

from __future__ import annotations

import argparse
import heapq
import itertools
import math
import sys
from dataclasses import dataclass
from functools import lru_cache

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this Arb certificate") from exc


ctx.prec = 384
PI = arb.pi()


def g_float(radius: float, z: float) -> float:
    if radius <= z:
        return 0.0
    root = math.sqrt(max(0.0, radius * radius - z * z))
    return (root - z * math.acos(z / radius)) / math.pi


def j2_float(radius: float, z: float) -> float:
    """2*integral_z^radius G_radius."""

    if radius <= z:
        return 0.0
    root = math.sqrt(max(0.0, radius * radius - z * z))
    return (
        (radius * radius + 2.0 * z * z) * math.acos(z / radius)
        - 3.0 * z * root
    ) / (2.0 * math.pi)


def shell_float(K: float, mu: float, z: float) -> float:
    return g_float(K, z) - g_float(mu, z)


@lru_cache(maxsize=None)
def level_sum_float(K_key: float, levels: int) -> float:
    """Sum pi/(2 theta_k), rounded K key is diagnostic only."""

    from scipy.optimize import brentq

    K = K_key
    total = 0.0
    for k in range(1, levels + 1):
        tau = k - 0.25

        def equation(theta: float) -> float:
            return K * (math.sin(theta) - theta * math.cos(theta)) / math.pi - tau

        theta = brentq(equation, 1.0e-12, math.pi / 2.0)
        total += math.pi / (2.0 * theta)
    return total


def knd_float(n: int, Q: int) -> float:
    cstar = 4.0 * math.sqrt(2.0) / 15.0
    c0 = (math.pi / 12.0) ** (1.0 / 3.0)
    levels = sum((k - 0.25) ** (-1.0 / 3.0) for k in range(1, Q + 1))
    return ((Q + n / 2.0 + cstar) / (c0 * levels)) ** 3


def root_kappa_float(f: int, n: int, sigma: float, alpha: float, eps: float) -> float | None:
    from scipy.optimize import brentq

    target = f - 0.25 + eps
    lo = max(
        21.0 / 8.0,
        (n + alpha + 0.5) * sigma**3 / (1.0 - sigma**2),
    )
    hi = (3.0 * math.pi * f / 2.0) * (1.0 - 1.0e-12)

    def value(kappa: float) -> float:
        K = kappa / sigma**3
        mu = kappa * (1.0 - sigma**2) / sigma**3
        q = mu - alpha
        return shell_float(K, mu, q) - target

    if lo >= hi or value(lo) > 0.0 or value(hi) < 0.0:
        return None
    return brentq(value, lo, hi, xtol=2.0e-13, rtol=2.0e-14)


def diagnostic_candidate(
    f: int,
    n: int,
    sigma: float,
    alpha: float,
    eps: float,
    phase: str,
) -> tuple[float, dict[str, float]] | None:
    if phase not in {"corner", "lower", "open"}:
        raise ValueError(phase)
    if phase == "corner":
        alpha, eps = 0.0, 0.0
    elif phase == "lower":
        eps = 0.0
    kappa = root_kappa_float(f, n, sigma, alpha, eps)
    if kappa is None:
        return None
    K = kappa / sigma**3
    mu = kappa * (1.0 - sigma**2) / sigma**3
    q = mu - alpha
    r = q - n
    delta = kappa / sigma
    b = f - 0.25
    Q = f - 1 if phase in {"corner", "lower"} else f
    if r < 0.5 or K >= knd_float(n, Q):
        return None

    aq = shell_float(K, mu, q)
    ar = shell_float(K, mu, r)
    if not (b - 1.0e-8 <= aq < f + 1.0e-8):
        return None
    if ar >= f + 0.25 or ar + aq >= 2.0 * f:
        return None

    # Necessary central/outer geometry.
    if r <= K / 2.0:
        if n > 48:
            return None
        U = 2.0 * delta * delta * (delta + 1.0) / (math.pi**2 * b**2)
        if K > U:
            return None
    else:
        cf = (math.sqrt(1.0 + b * b) - 1.0) / 2.0
        if delta + 1.0 <= cf * n:
            return None
        outer = delta * delta * n * n / (2.0 * math.pi**2 * (delta + n + 1.0))
        if K <= outer:
            return None

    xi = max(0.0, aq - b)
    Delta = max(0.0, ar - aq)
    discard = 2.0 * xi + Delta + n * Delta / (3.0 * (2.0 * r + n))
    if discard >= 0.5 - 0.5 / n:
        return None

    head = (
        j2_float(K, r)
        - j2_float(K, q)
        - j2_float(mu, r)
        + j2_float(mu, q)
        - 2.0 * n * f
    )
    levels = f - 1 if phase == "corner" else f
    angle = level_sum_float(round(K, 12), levels)
    cap = j2_float(mu, q)
    terminal_lower = angle - Q - cap
    scalar_lower = head + terminal_lower
    return scalar_lower, {
        "K": K,
        "mu": mu,
        "r": r,
        "q": q,
        "kappa": kappa,
        "aq": aq,
        "ar": ar,
        "head": head,
        "terminal": terminal_lower,
        "discard": discard,
    }


# ---------------------------------------------------------------------------
# Rigorous Arb certificate


QZERO = arb(0)
QONE = arb(1)
QUARTER = arb(fmpq(1, 4))
SIGMA_MIN = fmpq(1, 10)
SIGMA_MAX = fmpq(19, 20)
KAPPA_MIN = fmpq(21, 8)
KAPPA_MAX = {2: fmpq(66, 7), 3: fmpq(99, 7)}
PANELS = 4
ROOT_STEPS = 12
ANGLE_STEPS = 32
G_SERIES_TERMS = 12
MAX_DEPTH = 72
MAX_BOXES_PER_CASE = 500_000
REPORT_PROGRESS = False


def A(value: int | fmpq) -> arb:
    return arb(value)


def lower(value: arb) -> arb:
    return value.lower()


def upper(value: arb) -> arb:
    return value.upper()


def interval_ball(lo: fmpq, hi: fmpq) -> arb:
    if hi < lo:
        raise AssertionError("reversed interval")
    if lo == hi:
        return A(lo)
    # Construct the exact rational hull.  The two-string arb midpoint/radius
    # constructor treats strings such as "1/2" as uncertain decimal input,
    # producing a much wider interval than intended.
    out = A(lo).union(A(hi))
    if not out.contains(A(lo)) or not out.contains(A(hi)):
        raise AssertionError("interval constructor lost an endpoint")
    return out


def semipositive_sqrt(value: arb) -> arb:
    """Rigorous square root when the exact expression is nonnegative."""

    if value >= 0:
        return value.sqrt()
    if upper(value) < 0:
        raise ArithmeticError("negative radicand")
    return QZERO.union(upper(value).sqrt())


def nonnegative_hull(value: arb) -> arb:
    """Intersect an interval with the analytically known half-line [0,inf)."""

    if lower(value) >= 0:
        return value
    if upper(value) < 0:
        raise ArithmeticError("analytically nonnegative quantity is negative")
    return QZERO.union(upper(value))


def action_profile(
    sigma: arb,
    kappa: arb,
    shift: arb,
    v: fmpq,
) -> arb:
    """Radius profile in the non-cancelling scaled shell integral.

    Here shift=alpha for A(q), and shift=alpha+n for A(r).  With
    X=sigma*shift and u=kappa*v, the exact action is

        kappa/pi * integral_0^1 profile(v) dv.
    """

    vv = A(v)
    X = sigma * shift
    y = X / kappa
    first = 1 - vv + y
    second = 2 - (1 + vv + y) * sigma * sigma
    denominator = 1 - vv * sigma * sigma
    return semipositive_sqrt(first * second) / denominator


def action_bounds(
    sigma: arb,
    kappa: arb,
    shift: arb,
) -> tuple[arb, arb]:
    """Composite trapezoid/midpoint bounds for one shell action.

    The radius profile is concave.  Reversing its affine parameter does not
    change concavity, so trapezoid is a lower bound and midpoint an upper
    bound on each panel.
    """

    trap = QZERO
    mid = QZERO
    for j in range(PANELS + 1):
        weight = 1 if j in (0, PANELS) else 2
        trap += weight * action_profile(
            sigma, kappa, shift, fmpq(j, PANELS)
        )
    for j in range(PANELS):
        mid += action_profile(
            sigma, kappa, shift, fmpq(2 * j + 1, 2 * PANELS)
        )
    trap *= kappa / (2 * PANELS * PI)
    mid *= kappa / (PANELS * PI)
    return trap, mid


def g_radius_x(radius: arb, x: arb) -> arb:
    """Exact G_radius(radius-gap) from x=gap/(2*radius).

    Put x=gap/(2*radius)<1/2.  Integrating the positive Taylor series
    for asin gives

      G = 8*radius*x^(3/2)/pi * sum_m d_m*x^m,
      d_m = binom(2m,m)/(4^m*(2m+1)*(2m+3)).

    The coefficient ratios are below one, so the omitted tail is bounded
    by its first term divided by 1-upper(x).  This avoids every subtraction
    in the usual square-root/arctangent formula.
    """

    if x == 0:
        return QZERO
    if upper(x) < 0 or not (upper(x) < A(fmpq(1, 2))):
        raise ArithmeticError("nonpositive action abscissa")
    # x is analytically nonnegative.  Arb endpoint hulls can extend by one
    # outward ulp below zero when the box touches alpha=0.
    x = nonnegative_hull(x)
    partial = QZERO
    power = QONE
    coefficient = fmpq(1, 3)
    for m in range(G_SERIES_TERMS):
        partial += A(coefficient) * power
        power *= x
        coefficient *= fmpq((2 * m + 1) ** 2, 2 * (m + 1) * (2 * m + 5))
    first_omitted = A(coefficient) * power
    remainder_hi = upper(first_omitted) / (1 - upper(x))
    series = partial + QZERO.union(remainder_hi)
    return 8 * radius * x * semipositive_sqrt(x) * series / PI


def g_gap(radius: arb, gap: arb) -> arb:
    """Compatibility wrapper for a gap not carrying useful correlation."""

    if gap == 0:
        return QZERO
    if lower(gap) < 0:
        raise ArithmeticError("negative gap")
    return g_radius_x(radius, gap / (2 * radius))


def exact_shell_at_shift(
    sigma: arb,
    kappa: arb,
    shift: arb,
) -> arb:
    """Exact shell action with dimensionless gaps formed algebraically."""

    sigma2 = sigma * sigma
    sigma3 = sigma2 * sigma
    K = kappa / sigma3
    mu = kappa * (1 - sigma2) / sigma3
    x_outer = sigma2 / 2 + shift * sigma3 / (2 * kappa)
    x_inner = shift * sigma3 / (2 * kappa * (1 - sigma2))
    return g_radius_x(K, x_outer) - g_radius_x(mu, x_inner)


def exact_shell_at_q(sigma: arb, kappa: arb, alpha: arb) -> arb:
    """Exact A(q) for q=mu-alpha, with no nearby-radius subtraction."""

    return exact_shell_at_shift(sigma, kappa, alpha)


def exact_shell_at_r(
    sigma: arb,
    kappa: arb,
    alpha: arb,
    n: int,
) -> arb:
    """Exact A(r) for r=mu-alpha-n, using the same positive series."""

    return exact_shell_at_shift(sigma, kappa, alpha + n)


def cutoff_arb(n: int, Q: int) -> arb:
    cstar = 4 * A(2).sqrt() / 15
    c0 = (PI / 12).root(3)
    levels = QZERO
    for k in range(1, Q + 1):
        levels += A(fmpq(4 * k - 1, 4)) ** fmpq(-1, 3)
    return ((A(Q) + A(n) / 2 + cstar) / (c0 * levels)) ** 3


@dataclass(frozen=True)
class Box:
    f: int
    n: int
    phase: str
    s0: fmpq
    s1: fmpq
    a0: fmpq
    a1: fmpq
    # Endpoint excess eps.  It is zero in every certified phase below: the
    # open sector is reduced monotonically to its endpoint wall before the
    # interval computation starts.
    e0: fmpq
    e1: fmpq
    depth: int = 0

    def split(self, coordinate: str) -> tuple["Box", "Box"]:
        lo = getattr(self, coordinate + "0")
        hi = getattr(self, coordinate + "1")
        if lo == hi:
            raise AssertionError(f"cannot split degenerate {coordinate} interval")
        mid = (lo + hi) / 2
        left = self.__dict__.copy()
        right = self.__dict__.copy()
        left[coordinate + "1"] = mid
        right[coordinate + "0"] = mid
        left["depth"] = self.depth + 1
        right["depth"] = self.depth + 1
        return Box(**left), Box(**right)


def phase_Q(f: int, phase: str) -> int:
    return f - 1 if phase in {"corner", "lower"} else f


def phase_levels(f: int, phase: str) -> int:
    return f - 1 if phase == "corner" else f


@lru_cache(maxsize=None)
def root_kappa_enclosure(
    f: int,
    s0: fmpq,
    s1: fmpq,
    a0: fmpq,
    a1: fmpq,
    e0: fmpq,
    e1: fmpq,
    use_series: bool,
) -> tuple[str, fmpq | None, fmpq | None]:
    """Enclose every kappa root A(q)=f-1/4+eps on a parameter box.

    At fixed (sigma,alpha), the noncancelling scaled integral proves strict
    monotonicity in kappa: after u=kappa*v its two radicand factors are
    affine increasing functions of kappa.  The bisection itself uses the
    exact gap primitive, avoiding the persistent width of fixed quadrature.
    """

    sigma = interval_ball(s0, s1)
    alpha = interval_ball(a0, a1)
    target = A(f) - QUARTER + interval_ball(e0, e1)
    lo, hi = KAPPA_MIN, KAPPA_MAX[f]

    if not use_series:
        # Audited ordinary path: monotone trapezoid/midpoint enclosure of
        # the noncancelling scaled action.
        try:
            lo_bounds = action_bounds(sigma, A(lo), alpha)
            hi_bounds = action_bounds(sigma, A(hi), alpha)
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if lower(lo_bounds[0]) > upper(target):
            return "none", None, None
        if upper(hi_bounds[1]) < lower(target):
            return "none", None, None
        a, b = lo, hi
        for _ in range(ROOT_STEPS):
            m = (a + b) / 2
            try:
                value = action_bounds(sigma, A(m), alpha)[1]
            except (ArithmeticError, ZeroDivisionError):
                return "split", None, None
            if upper(value) < lower(target):
                a = m
            else:
                b = m
        root_lo = a
        try:
            endpoint = action_bounds(sigma, A(hi), alpha)[0]
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if not (lower(endpoint) > upper(target)):
            return "split", None, None
        a, b = root_lo, hi
        for _ in range(ROOT_STEPS):
            m = (a + b) / 2
            try:
                value = action_bounds(sigma, A(m), alpha)[0]
            except (ArithmeticError, ZeroDivisionError):
                return "split", None, None
            if lower(value) > upper(target):
                b = m
            else:
                a = m
        return "ok", root_lo, b

    try:
        lo_value = exact_shell_at_q(sigma, A(lo), alpha)
        hi_value = exact_shell_at_q(sigma, A(hi), alpha)
    except (ArithmeticError, ZeroDivisionError):
        return "split", None, None

    if lower(lo_value) > upper(target):
        return "none", None, None
    if upper(hi_value) < lower(target):
        return "none", None, None

    # Largest common lower bound: exact interval wholly below target.
    a, b = lo, hi
    for _ in range(ROOT_STEPS):
        m = (a + b) / 2
        try:
            value = exact_shell_at_q(sigma, A(m), alpha)
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if upper(value) < lower(target):
            a = m
        else:
            b = m
    root_lo = a

    # Smallest common upper bound: exact interval wholly above target.  If
    # the common endpoint test is inconclusive, retain the a priori ceiling
    # instead of tracing the parameter curve on which the root exits the
    # admissible kappa interval.  This is a safe outer enclosure of every
    # root that actually exists in the box.
    try:
        endpoint = exact_shell_at_q(sigma, A(hi), alpha)
    except (ArithmeticError, ZeroDivisionError):
        return "split", None, None
    if not (lower(endpoint) > upper(target)):
        return "ok", root_lo, hi
    a, b = root_lo, hi
    for _ in range(ROOT_STEPS):
        m = (a + b) / 2
        try:
            value = exact_shell_at_q(sigma, A(m), alpha)
        except (ArithmeticError, ZeroDivisionError):
            return "split", None, None
        if lower(value) > upper(target):
            b = m
        else:
            a = m
    return "ok", root_lo, b


def j2_gap(radius: arb, gap: arb) -> arb:
    """Exact 2*integral_{radius-gap}^radius G_radius, without cancellation."""

    z = radius - gap
    if not (lower(z) > 0):
        raise ArithmeticError("nonpositive action abscissa")
    root = semipositive_sqrt(gap * (2 * radius - gap))
    theta = (root / z).atan()
    return ((radius * radius + 2 * z * z) * theta - 3 * z * root) / (2 * PI)


def angle_sum_lower(K_lower: arb, levels: int) -> arb | None:
    """Directed lower bound for sum pi/(2 theta_k) at K>=K_lower."""

    if not (K_lower > 0):
        return None
    total = QZERO
    for k in range(1, levels + 1):
        tau = A(fmpq(4 * k - 1, 4))
        lo, hi = fmpq(0), fmpq(11, 7)

        def level(theta: fmpq) -> arb:
            th = A(theta)
            h = th.sin() - th * th.cos()
            return K_lower * h / PI

        if not (lower(level(hi)) > tau):
            return None
        for _ in range(ANGLE_STEPS):
            mid = (lo + hi) / 2
            if lower(level(mid)) > tau:
                hi = mid
            else:
                lo = mid
        total += lower(PI / (2 * A(hi)))
    return total


def initial_sigma_interval(f: int, n: int, phase: str) -> tuple[fmpq, fmpq] | None:
    """Analytic cutoff/physical localization before subdivision."""

    Q = phase_Q(f, phase)
    cutoff = cutoff_arb(n, Q)

    # K=kappa/sigma^3<K_nd and kappa>=21/8 force a lower sigma bound.
    lo, hi = SIGMA_MIN, SIGMA_MAX
    for _ in range(28):
        mid = (lo + hi) / 2
        if upper(cutoff * A(mid) ** 3) < A(KAPPA_MIN):
            lo = mid
        else:
            hi = mid
    s0 = lo

    # Physicality mu>=n+1/2 and kappa<kappa_max force an upper bound.
    lo, hi = s0, SIGMA_MAX
    endpoint = A(KAPPA_MAX[f]) * (1 - A(hi) ** 2) / A(hi) ** 3
    if not (upper(endpoint) < A(fmpq(2 * n + 1, 2))):
        raise AssertionError("SIGMA_MAX does not dominate the physical boundary")
    for _ in range(28):
        mid = (lo + hi) / 2
        possible_mu = A(KAPPA_MAX[f]) * (1 - A(mid) ** 2) / A(mid) ** 3
        if upper(possible_mu) < A(fmpq(2 * n + 1, 2)):
            hi = mid
        else:
            lo = mid
    s1 = hi

    # For n>48 the central branch is already excluded, hence the outer cone
    # gives sigma<38/n.  The coefficient is strictly smaller than 38.
    if n > 48 and fmpq(38, n) < s1:
        s1 = fmpq(38, n)
    if s1 <= s0:
        return None
    return s0, s1


def choose_split(box: Box, reason: str) -> str:
    widths: dict[str, float] = {}
    if box.s1 > box.s0:
        widths["s"] = float(A(box.s1 - box.s0)) / 0.85
    if box.a1 > box.a0:
        widths["a"] = float(A(box.a1 - box.a0))
    if box.e1 > box.e0:
        widths["e"] = float(A(box.e1 - box.e0)) / 0.25
    if reason == "root":
        if "s" in widths:
            widths["s"] *= 1.5
        if "e" in widths:
            widths["e"] *= 1.5
    elif reason == "scalar" and "a" in widths:
        widths["a"] *= 1.5
    if not widths:
        raise AssertionError(f"unresolved point box: {box}")
    return max(widths, key=widths.get)


def assess(box: Box) -> tuple[str, float]:
    """Return a rigorous disposition or an unresolved split reason."""

    f, n = box.f, box.n
    b = A(f) - QUARTER
    Q = phase_Q(f, box.phase)
    levels = phase_levels(f, box.phase)
    sigma = interval_ball(box.s0, box.s1)
    alpha = interval_ball(box.a0, box.a1)
    eps = interval_ball(box.e0, box.e1)
    target = b + eps

    if box.phase == "corner":
        # Here alpha=0 and q=mu, so A(q)=G_K(mu)=b eliminates
        # kappa exactly.  With cos(theta)=1-sigma^2, use the stable
        # half-angle theta=2 atan(sigma/sqrt(2-sigma^2)).
        companion = semipositive_sqrt(2 - sigma * sigma)
        theta = 2 * (sigma / companion).atan()
        h = sigma * companion - (1 - sigma * sigma) * theta
        if not (lower(h) > 0):
            return "geometry", -1.0
        raw_kappa = b * PI * sigma * sigma * sigma / h
        if upper(raw_kappa) < A(KAPPA_MIN) or lower(raw_kappa) > A(KAPPA_MAX[f]):
            return "root-miss", 1.0
        kappa_lo = max(lower(raw_kappa), A(KAPPA_MIN))
        kappa_hi = min(upper(raw_kappa), A(KAPPA_MAX[f]))
        kappa = kappa_lo.union(kappa_hi)
    else:
        exceptional_series = (
            ((f == 2 and n >= 8) or (f == 3 and n >= 7)) and box.phase in {"lower", "open"}
        )
        root_status, k0, k1 = root_kappa_enclosure(
            box.f,
            box.s0,
            box.s1,
            box.a0,
            box.a1,
            box.e0,
            box.e1,
            exceptional_series,
        )
        if root_status == "none":
            return "root-miss", 1.0
        if root_status != "ok" or k0 is None or k1 is None:
            return "root", -1.0
        kappa = interval_ball(k0, k1)

    K = kappa / (sigma * sigma * sigma)
    delta = kappa / sigma
    mu = kappa * (1 - sigma * sigma) / (sigma * sigma * sigma)
    q = mu - alpha
    r = q - n

    if upper(r) < A(fmpq(1, 2)):
        return "physical", 1.0
    if not (lower(r) > 0):
        return "geometry", -1.0
    cutoff = cutoff_arb(n, Q)
    if lower(K) >= upper(cutoff):
        return "cutoff", 1.0

    # Universal residual geometry from the exact no-drop identities.
    if upper(delta / PI) <= lower(b):
        return "active", 1.0
    U = 2 * delta * delta * (delta + 1) / (PI * PI * b * b)
    if lower(K - U) >= 0:
        return "upper-geometry", 1.0
    if upper(K * K - b * n * (n + 1)) <= 0:
        return "slope-geometry", 1.0
    width_margin = delta / PI - (A(f) + QUARTER + r / (4 * n))
    if lower(width_margin) >= 0:
        return "width-geometry", 1.0

    side = r - K / 2
    if n > 48 and upper(side) <= 0:
        return "central-box", 1.0
    if lower(side) > 0:
        cf = ((1 + b * b).sqrt() - 1) / 2
        if upper(delta + 1 - cf * n) <= 0:
            return "outer-width", 1.0
        outer_lower = delta * delta * n * n / (2 * PI * PI * (delta + n + 1))
        if upper(K - outer_lower) <= 0:
            return "outer-slope", 1.0

    try:
        if box.phase == "corner" or (
            ((f == 2 and n >= 8) or (f == 3 and n >= 7)) and box.phase in {"lower", "open"}
        ):
            ar = exact_shell_at_r(sigma, kappa, alpha, n)
        else:
            ar_lo_raw, ar_hi_raw = action_bounds(sigma, kappa, alpha + n)
            ar = ar_lo_raw.union(ar_hi_raw)
    except (ArithmeticError, ZeroDivisionError):
        return "geometry", -1.0
    if lower(ar) >= A(f) + QUARTER:
        return "endpoint-floor", 1.0
    if lower(ar + target) >= 2 * A(f):
        return "endpoint-phase", 1.0

    try:
        Delta = nonnegative_hull(ar - target)
    except ArithmeticError:
        return "geometry", -1.0

    # Corollary 2.3: every possible failure lies strictly below this sector.
    discard = 2 * eps + Delta + A(n) * Delta / (3 * (2 * r + n))
    threshold = A(fmpq(n - 1, 2 * n))
    if lower(discard) >= threshold:
        return "curvature-prune", 1.0

    # Exact head in gap variables.  This avoids subtracting nearby radii.
    try:
        head_exact = (
            j2_gap(K, delta + alpha + n)
            - j2_gap(K, delta + alpha)
            - j2_gap(mu, alpha + n)
            + j2_gap(mu, alpha)
            - 2 * n * f
        )
    except (ArithmeticError, ZeroDivisionError):
        return "geometry", -1.0

    head_curvature = (
        A(n * n) * Delta / (3 * (2 * r + n))
        + A(n) * (2 * eps + Delta - A(fmpq(1, 2)))
    )
    head_lo = max(lower(head_exact), lower(head_curvature))

    angle = angle_sum_lower(lower(K), levels)
    if angle is None:
        return "scalar", -1.0
    if box.phase == "corner":
        cap_hi = QZERO
    else:
        try:
            cap_hi = upper(j2_gap(mu, alpha))
        except (ArithmeticError, ZeroDivisionError):
            return "geometry", -1.0
    terminal_lo = angle - Q - cap_hi
    scalar = head_lo + terminal_lo
    if scalar > 0:
        return "positive", float(lower(scalar))
    return "scalar", float(lower(scalar))


def verify_case(f: int, n: int, phase: str) -> dict[str, int | float]:
    sigma_range = initial_sigma_interval(f, n, phase)
    if sigma_range is None:
        return {"processed": 0, "positive": 0, "pruned": 1, "max-depth": 0,
                "smallest-margin": float("inf")}
    s0, s1 = sigma_range
    if phase == "corner":
        a0 = a1 = fmpq(0)
        e0 = e1 = fmpq(0)
    elif phase == "lower":
        a0, a1 = fmpq(0), fmpq(1)
        e0 = e1 = fmpq(0)
    else:
        a0, a1 = fmpq(0), fmpq(1)
        # Every off-wall point is dominated by the point obtained by
        # lowering K at fixed (mu,r) until A(q)=f-1/4.  Keep the open
        # combinatorics Q=f and f strict-wall-safe levels on this wall.
        e0 = e1 = fmpq(0)
    counter = itertools.count()
    initial_boxes = [Box(f, n, phase, s0, s1, a0, a1, e0, e1)]
    # The only numerically close cutoff/floor handoff in this compact audit
    # is the f=2,n=8 lower wall.  Seeding its proved overlap point prevents
    # the generic queue from tracking both exclusion boundaries at once.
    handoff = fmpq(43, 200)
    if f == 2 and n == 8 and phase == "lower" and s0 < handoff < s1:
        initial_boxes = [
            Box(f, n, phase, s0, handoff, a0, a1, e0, e1),
            Box(f, n, phase, handoff, s1, a0, a1, e0, e1),
        ]
    heap: list[tuple[float, int, Box]] = [
        (0.0, next(counter), box) for box in initial_boxes
    ]
    out: dict[str, int | float] = {
        "processed": 0,
        "positive": 0,
        "pruned": 0,
        "max-depth": 0,
        "smallest-margin": float("inf"),
    }
    status_counts: dict[str, int] = {}
    terminal_statuses = {
        "root-miss", "physical", "cutoff", "active", "upper-geometry",
        "slope-geometry", "width-geometry", "central-box", "outer-width",
        "outer-slope", "endpoint-floor", "endpoint-phase", "curvature-prune",
        "positive",
    }

    while heap:
        _, _, box = heapq.heappop(heap)
        out["processed"] = int(out["processed"]) + 1
        out["max-depth"] = max(int(out["max-depth"]), box.depth)
        if int(out["processed"]) > MAX_BOXES_PER_CASE:
            raise AssertionError(f"box limit exceeded: f={f}, n={n}, phase={phase}")
        if REPORT_PROGRESS and int(out["processed"]) % 500 == 0:
            print(
                f"  progress f={f}, n={n}, phase={phase}: "
                f"processed={out['processed']}, queued={len(heap)}, "
                f"depth={out['max-depth']}, statuses={status_counts}"
            )
        status, margin = assess(box)
        status_counts[status] = status_counts.get(status, 0) + 1
        if status in terminal_statuses:
            if status == "positive":
                out["positive"] = int(out["positive"]) + 1
                out["smallest-margin"] = min(float(out["smallest-margin"]), margin)
            else:
                out["pruned"] = int(out["pruned"]) + 1
            continue
        if box.depth >= MAX_DEPTH:
            raise AssertionError(
                f"unresolved depth {box.depth}: {box}; status={status}; margin={margin}"
            )
        coordinate = choose_split(box, "root" if status == "root" else "scalar")
        left, right = box.split(coordinate)
        heapq.heappush(heap, (margin, next(counter), left))
        heapq.heappush(heap, (margin, next(counter), right))
    return out


def exact_constant_checks() -> None:
    if not (PI < A(fmpq(22, 7))):
        raise AssertionError("pi<22/7 failed")
    if not (A(KAPPA_MAX[2]) > 3 * PI):
        raise AssertionError("f=2 kappa upper enlargement failed")
    if not (A(KAPPA_MAX[3]) > 9 * PI / 2):
        raise AssertionError("f=3 kappa upper enlargement failed")
    # The common sigma ceiling is physically impossible already for f=3,n=2.
    s = A(SIGMA_MAX)
    mu_upper = A(KAPPA_MAX[3]) * (1 - s * s) / (s * s * s)
    if not (mu_upper < A(fmpq(5, 2))):
        raise AssertionError("sigma ceiling is not physically excluding")


def rigorous_verify(
    selected_f: int | None,
    selected_n: int | None,
    selected_phase: str | None,
) -> None:
    exact_constant_checks()
    total = 0
    positives = 0
    max_depth = 0
    smallest = float("inf")
    case_count = 0
    phase_stats = {
        phase: {"cases": 0, "boxes": 0, "positive": 0, "depth": 0, "smallest": float("inf")}
        for phase in ("corner", "lower", "open")
    }
    for f in (2, 3):
        if selected_f is not None and f != selected_f:
            continue
        for n in range(2, 380):
            if selected_n is not None and n != selected_n:
                continue
            for phase in ("corner", "lower", "open"):
                if selected_phase is not None and phase != selected_phase:
                    continue
                result = verify_case(f, n, phase)
                case_count += 1
                total += int(result["processed"])
                positives += int(result["positive"])
                max_depth = max(max_depth, int(result["max-depth"]))
                smallest = min(smallest, float(result["smallest-margin"]))
                stats = phase_stats[phase]
                stats["cases"] = int(stats["cases"]) + 1
                stats["boxes"] = int(stats["boxes"]) + int(result["processed"])
                stats["positive"] = int(stats["positive"]) + int(result["positive"])
                stats["depth"] = max(int(stats["depth"]), int(result["max-depth"]))
                stats["smallest"] = min(
                    float(stats["smallest"]), float(result["smallest-margin"])
                )
                if REPORT_PROGRESS and int(result["processed"]) > 1000:
                    print(
                        f"case f={f}, n={n}, phase={phase}: "
                        f"processed={result['processed']}, positive={result['positive']}, "
                        f"pruned={result['pruned']}, depth={result['max-depth']}"
                    )
    full = selected_f is None and selected_n is None and selected_phase is None
    if full:
        print("PASS: compact f=2,3 no-drop rows certified for sigma>=1/10")
    else:
        print("PASS: requested compact no-drop certificate scope")
    print(
        f"python-flint={flint.__version__}; precision={ctx.prec} bits; "
        f"panels={PANELS}; root-steps={ROOT_STEPS}; angle-steps={ANGLE_STEPS}"
    )
    print(f"discrete phase cases: {case_count}")
    print(f"processed boxes: {total}; positive leaves: {positives}; max depth: {max_depth}")
    print(f"smallest accepted exact-angle scalar endpoint (diagnostic): {smallest}")
    for phase in ("corner", "lower", "open"):
        stats = phase_stats[phase]
        if int(stats["cases"]) == 0:
            continue
        print(
            f"phase {phase}: cases={stats['cases']}; boxes={stats['boxes']}; "
            f"positive={stats['positive']}; depth={stats['depth']}; "
            f"smallest={stats['smallest']}"
        )


def diagnostic_scan() -> None:
    """Coarse landscape scan; printed decimals have no proof status."""

    import numpy as np

    best: tuple[float, tuple[object, ...], dict[str, float]] | None = None
    feasible = 0
    # The geometric grid is intentionally modest; it only informs the Arb split strategy.
    for f in (2, 3):
        for n in range(2, 380):
            s_hi = min(0.95, 38.0 / n)
            if s_hi <= 0.1:
                continue
            sigmas = np.geomspace(0.1, s_hi, 9)
            for phase in ("corner", "lower", "open"):
                eps_values = (0.0,) if phase != "open" else np.linspace(0.0, 0.249, 5)
                for sigma in sigmas:
                    alpha_values = (0.0,) if phase == "corner" else np.linspace(0.0, 0.999, 5)
                    for alpha in alpha_values:
                        for eps in eps_values:
                            out = diagnostic_candidate(
                                f, n, float(sigma), float(alpha), float(eps), phase
                            )
                            if out is None:
                                continue
                            feasible += 1
                            value, data = out
                            key = (f, n, sigma, alpha, eps, phase)
                            if best is None or value < best[0]:
                                best = (value, key, data)
    print(f"diagnostic feasible points: {feasible}")
    print(f"diagnostic minimum: {best}")


def main() -> None:
    global PI, REPORT_PROGRESS
    parser = argparse.ArgumentParser()
    parser.add_argument("--diagnostic", action="store_true")
    parser.add_argument("--f", type=int, choices=(2, 3))
    parser.add_argument("--n", type=int)
    parser.add_argument("--phase", choices=("corner", "lower", "open"))
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--precision", type=int, default=384)
    args = parser.parse_args()
    if args.precision < 256:
        raise SystemExit("--precision must be at least 256 bits")
    ctx.prec = args.precision
    PI = arb.pi()
    REPORT_PROGRESS = args.verbose
    if args.diagnostic:
        diagnostic_scan()
        return
    if args.n is not None and not (2 <= args.n <= 379):
        raise SystemExit("--n must lie in 2..379")
    rigorous_verify(args.f, args.n, args.phase)


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError, ZeroDivisionError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
