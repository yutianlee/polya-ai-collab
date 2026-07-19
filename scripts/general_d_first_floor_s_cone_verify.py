#!/usr/bin/env python3
"""Arb certificate for the ordinary first-floor cone s>=2.

This verifier works on the first-shelf wall A(x)=3/4.  It uses the
dimensionless ratios

    rho=mu/K,  xi=x/K=rho*u,

and

    g(z)=(sqrt(1-z^2)-z acos(z))/pi,
    w=g(xi)-rho*g(u).

The wall fixes K=3/(4w).  The active-region and s>=2 conditions become

    3(1-rho) >= 4*pi*w,     rho-xi >= 4*w.

The radius-average ratio and a one-variable algebraic minimization give

    (xi-eta)(3*sqrt((1-eta^2)/(1-xi^2))-5) >= -2(1-xi).

After combining the two inner head trapezoids by concavity, positivity
follows from J_2>0, where

    J_2 = -(2/3)w(1-xi)
          +(rho-xi)w +(rho-xi)g(rho)+g(rho)^2/c -(16/9)w^2,
    c=acos(rho)/pi.

Indeed J_2<=(16w^2/9) C_1, with C_1 a rigorous lower bound for the
true-interface certificate.  The finite Arb box uses
t=(rho-xi)/(1-rho) in [0,4] and stops at rho=49/50; the complementary
cap is discharged by explicit inequalities checked in near_one_checks and
proved in the accompanying note.

All sign decisions use python-flint Arb directed rounding.  Binary floating
point is used only to choose a subdivision coordinate and print diagnostics.
"""

from __future__ import annotations

import argparse
import heapq
import itertools
import sys
from math import comb

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


PI: arb
RHO_MIN = fmpq(39, 50)
RHO_MAX = fmpq(49, 50)
XI_LOCAL = fmpq(9, 10)
U_FLOOR = fmpq(33, 50)
ROOT_BISECTIONS = 36


def set_precision(bits: int) -> None:
    global PI
    ctx.prec = bits
    PI = arb.pi()


def A(q: fmpq | int) -> arb:
    return arb(q)


def interval_ball(lo: fmpq, hi: fmpq) -> arb:
    if hi < lo:
        raise AssertionError("reversed interval")
    if lo == hi:
        return A(lo)
    mid, rad = (lo + hi) / 2, (hi - lo) / 2
    out = arb(str(mid), str(rad))
    if not out.contains(A(lo)) or not out.contains(A(hi)):
        raise AssertionError("interval constructor lost an endpoint")
    return out


def lower(x: arb) -> arb:
    return x.lower()


def upper(x: arb) -> arb:
    return x.upper()


def semipositive_sqrt(x: arb) -> arb:
    if x >= 0:
        return x.sqrt()
    if upper(x) < 0:
        raise ArithmeticError("negative semipositive radicand")
    return arb(0).union(upper(x).sqrt())


def g(z: arb) -> arb:
    return (semipositive_sqrt(1 - z * z) - z * z.acos()) / PI


def w_point_rt(rho: fmpq, t: fmpq) -> arb:
    xi = rho - (1 - rho) * t
    if not (0 <= xi <= rho):
        raise ArithmeticError("invalid ratio endpoint")
    u = xi / rho
    R, U, X = A(rho), A(u), A(xi)
    return g(X) - R * g(U)


def exact_domain_checks() -> None:
    # Write t=(rho-xi)/(1-rho).  Concavity makes w(t)/t decrease.
    # Up to rho=11/20, its value at the physical endpoint xi=0 is still
    # larger than (1-rho)/4, so the beta>=3 condition is impossible.
    r0 = A(fmpq(11, 20))
    endpoint_ratio = 4 * (1 - r0) / (PI * r0)
    if not (endpoint_ratio > 1):
        raise AssertionError("low-rho physical-endpoint exclusion unresolved")

    # For 11/20<=rho<=39/50, t0=3/pi is physical.  If
    # w(t0)>3(1-rho)/(4pi), then t<=t0 violates beta>=3 and t>=t0
    # violates the active condition.  Certify this one-dimensional
    # comparison on exact rational panels.
    subdivisions = 4096
    left_edge, right_edge = fmpq(11, 20), RHO_MIN
    t0 = 3 / PI
    for j in range(subdivisions):
        left = left_edge + (right_edge - left_edge) * fmpq(j, subdivisions)
        right = left_edge + (right_edge - left_edge) * fmpq(j + 1, subdivisions)
        rho = interval_ball(left, right)
        xi = rho - (1 - rho) * t0
        u = xi / rho
        wall = g(xi) - rho * g(u)
        separation = wall - 3 * (1 - rho) / (4 * PI)
        if not (separation > 0):
            raise AssertionError(
                f"low-rho panel unresolved: j={j}, separation={separation}"
            )

    # Active region plus w>=((1-rho)/pi)*sqrt(1-u^2) implies
    # u>=sqrt(7)/4.  The rational initial value 33/50 is smaller.
    if not (A(U_FLOOR) < arb(7).sqrt() / 4):
        raise AssertionError("U_FLOOR does not cover sqrt(7)/4")

    print("PASS exact domain reductions:")
    print("  rho>39/50 in the simultaneous active, beta>=3 wall domain")
    print("  u=x/mu>=sqrt(7)/4>33/50")


def bernstein_coefficients(
    power: list[fmpq], left: fmpq, right: fmpq
) -> list[fmpq]:
    """Exact Bernstein coefficients of a power-basis polynomial."""

    degree = len(power) - 1
    width = right - left
    local: list[fmpq] = []
    for j in range(degree + 1):
        local.append(
            sum(
                (
                    power[k]
                    * comb(k, j)
                    * left ** (k - j)
                    * width ** j
                    for k in range(j, degree + 1)
                ),
                fmpq(0),
            )
        )
    out: list[fmpq] = []
    for k in range(degree + 1):
        out.append(
            sum(
                (
                    local[j] * fmpq(comb(k, j), comb(degree, j))
                    for j in range(k + 1)
                ),
                fmpq(0),
            )
        )
    return out


def ratio_minimum_checks() -> None:
    """Exact checks behind the two eta-minimization lemmas."""

    # For D>=2/5, squaring the global comparison produces P(D)>=0.
    # The coefficients are in increasing power order.
    power = [fmpq(-4), fmpq(12), fmpq(24), fmpq(-32), fmpq(9)]
    panels = (
        (fmpq(2, 5), fmpq(1, 2)),
        (fmpq(1, 2), fmpq(1)),
        (fmpq(1), fmpq(3, 2)),
        (fmpq(3, 2), fmpq(2)),
        (fmpq(2), fmpq(3)),
        (fmpq(3), fmpq(4)),
    )
    for left, right in panels:
        coeffs = bernstein_coefficients(power, left, right)
        if not all(value > 0 for value in coeffs):
            raise AssertionError(
                f"global ratio polynomial unresolved on [{left},{right}]"
            )
    # For D>=4, 9D^4-32D^3 is positive, as is the remainder.
    d = fmpq(4)
    if not (
        9 * d - 32 > 0
        and 24 * d * d + 12 * d - 4 > 0
    ):
        raise AssertionError("global ratio polynomial tail unresolved")

    # If xi>=9/10 and Q<5/3, then eta>2/3 and hence
    # (xi+eta)/(1+xi)>4/5.  With D=(xi-eta)/(1-xi), it remains to
    # prove D(5-3*sqrt(1+4D/5))<=1.  D<=1/5 is immediate; after
    # squaring for D>=1/5 the required cubic is positive.
    xi0 = XI_LOCAL
    eta_square = 1 - fmpq(25, 9) * (1 - xi0 * xi0)
    if not (eta_square > fmpq(2, 3) ** 2):
        raise AssertionError("local eta lower bound unresolved")
    ratio = (xi0 + fmpq(2, 3)) / (1 + xi0)
    if not (ratio > fmpq(4, 5)):
        raise AssertionError("local q-ratio lower bound unresolved")
    local_power = [fmpq(-1), fmpq(10), fmpq(-16), fmpq(36, 5)]
    local_panels = (
        (fmpq(1, 5), fmpq(1, 2)),
        (fmpq(1, 2), fmpq(1)),
        (fmpq(1), fmpq(6, 5)),
        (fmpq(6, 5), fmpq(2)),
        (fmpq(2), fmpq(3)),
    )
    for left, right in local_panels:
        coeffs = bernstein_coefficients(local_power, left, right)
        if not all(value > 0 for value in coeffs):
            raise AssertionError(
                f"local ratio cubic unresolved on [{left},{right}]"
            )
    d = fmpq(3)
    if not (fmpq(36, 5) * d - 16 > 0 and 10 * d - 1 > 0):
        raise AssertionError("local ratio cubic tail unresolved")

    print("PASS exact eta-minimization lemmas:")
    print("  global M(xi)>=-2(1-xi)")
    print("  local xi>=9/10 bound M(xi)>=-(1-xi)")


def near_one_checks() -> None:
    """Directed-rounding constants for the analytic rho-near-one cap."""

    rho0 = A(RHO_MAX)
    g0 = 2 * (2 * rho0).sqrt() / (3 * PI)
    h0 = 2 * rho0 / 3

    # Case e>=4 epsilon after the global M>=-2(1-xi) bound.
    far_margin = A(fmpq(2, 3)) - 4 / (3 * PI)
    if not (far_margin > 0):
        raise AssertionError(f"near-one far-e margin unresolved: {far_margin}")

    # Case e<4 epsilon.  Since rho>49/50, this has xi>9/10, so
    # M>=-(1-xi).  The radius integral gives
    #   w/epsilon^(3/2) <= B*((1+t)^(3/2)-t^(3/2)),
    # B=2sqrt(2)/(3*pi*sqrt(rho0)).
    sqrt_eps0 = (1 - rho0).sqrt()
    b0 = 2 * arb(2).sqrt() / (3 * PI * rho0.sqrt())
    l_half = A(fmpq(3, 2)) ** A(fmpq(3, 2)) - (
        A(fmpq(1, 2)) ** A(fmpq(3, 2))
    )
    w_half = b0 * l_half

    # For 0<=t<=1/2, the product
    # (1-2t)*((1+t)^(3/2)-t^(3/2)) is at most one.
    low_t_margin = (
        g0 * h0
        - b0 / 3
        - A(fmpq(16, 9)) * sqrt_eps0 * w_half * w_half
    )
    if not (low_t_margin > 0):
        raise AssertionError(
            f"near-one low-t margin unresolved: {low_t_margin}"
        )

    # For 1/2<=t<4, the linear w term is nonnegative, t*g contributes
    # at least g0/2, and the displayed radius-integral bound is largest
    # at t=4.
    l_four = A(5) ** A(fmpq(3, 2)) - A(4) ** A(fmpq(3, 2))
    w_four = b0 * l_four
    high_t_margin = (
        g0 * h0
        + g0 / 2
        - A(fmpq(16, 9)) * sqrt_eps0 * w_four * w_four
    )
    if not (high_t_margin > 0):
        raise AssertionError(
            f"near-one high-t margin unresolved: {high_t_margin}"
        )

    print("PASS analytic rho>49/50 cap constants:")
    print(f"  e>=4epsilon margin coefficient ~{float(far_margin.mid()):.12g}")
    print(f"  0<=e/epsilon<=1/2 margin ~{float(low_t_margin.mid()):.12g}")
    print(f"  1/2<=e/epsilon<4 margin ~{float(high_t_margin.mid()):.12g}")


def rt_hulls(
    r0: fmpq, r1: fmpq, t0: fmpq, t1: fmpq
) -> tuple[arb, arb, arb, arb, arb, arb]:
    """Endpoint hulls on a rho,t rectangle."""

    xi_lo = r0 - (1 - r0) * t1
    xi_hi = r1 - (1 - r1) * t0
    if xi_lo < 0 or xi_hi >= 1:
        raise ArithmeticError("nonphysical ratio rectangle")
    xi = interval_ball(xi_lo, xi_hi)
    eps = interval_ball(1 - r1, 1 - r0)
    e = interval_ball((1 - r1) * t0, (1 - r0) * t1)
    w = w_point_rt(r1, t0).union(w_point_rt(r0, t1))
    grho = g(A(r1)).union(g(A(r0)))
    c = (A(r1).acos() / PI).union(A(r0).acos() / PI)
    return xi, eps, e, w, grho, c


def panel_value_at_t(
    r0: fmpq, r1: fmpq, t: fmpq, kind: str
) -> arb:
    _, eps, e, w, _, _ = rt_hulls(r0, r1, t, t)
    if kind == "beta":
        return e - 4 * w
    if kind == "active":
        return 3 * eps - 4 * PI * w
    raise AssertionError(f"unknown panel function {kind}")


def beta_root_enclosure(
    r0: fmpq, r1: fmpq
) -> tuple[fmpq, fmpq] | None:
    """Common enclosure of the unique root e/w=4 on a rho panel."""

    left, right = fmpq(0), fmpq(2)
    if not (upper(panel_value_at_t(r0, r1, left, "beta")) < 0):
        return None
    if not (lower(panel_value_at_t(r0, r1, right, "beta")) > 0):
        return None

    a, b = left, right
    for _ in range(ROOT_BISECTIONS):
        mid = (a + b) / 2
        value = panel_value_at_t(r0, r1, mid, "beta")
        if upper(value) < 0:
            a = mid
        else:
            b = mid
    root_lo = a

    a, b = root_lo, right
    for _ in range(ROOT_BISECTIONS):
        mid = (a + b) / 2
        value = panel_value_at_t(r0, r1, mid, "beta")
        if lower(value) > 0:
            b = mid
        else:
            a = mid
    return root_lo, b


def active_upper_enclosure(
    r0: fmpq, r1: fmpq
) -> fmpq | None:
    """Upper endpoint covering every active t on a rho panel."""

    if r0 < fmpq(4, 5) < r1:
        return None
    if r0 >= fmpq(4, 5):
        return fmpq(4)

    left, right = fmpq(0), fmpq(2)
    if not (lower(panel_value_at_t(r0, r1, left, "active")) > 0):
        return None
    if not (upper(panel_value_at_t(r0, r1, right, "active")) < 0):
        return None
    a, b = left, right
    for _ in range(ROOT_BISECTIONS):
        mid = (a + b) / 2
        value = panel_value_at_t(r0, r1, mid, "active")
        if upper(value) < 0:
            b = mid
        else:
            a = mid
    return b


def boundary_j_lower(
    r0: fmpq, r1: fmpq, t0: fmpq, t1: fmpq
) -> arb:
    """Lower J_2 at the exact beta root e=4w."""

    _, eps, e, _, grho, c = rt_hulls(r0, r1, t0, t1)
    # Substitute the exact boundary identity w=e/4 before interval
    # evaluation.  This removes a dependency copy of w and gives
    #   J_b=g^2/c+eg-epsilon*e/6-e^2/36.
    return (
        lower(grho) * lower(grho) / upper(c)
        + lower(e) * lower(grho)
        - upper(eps * e) / 6
        - upper(e) * upper(e) / 36
    )


def derivative_norm_lower(
    r0: fmpq, r1: fmpq, t0: fmpq, t1: fmpq
) -> arb:
    """Concavity lower bound for (dJ_2/de)/w."""

    _, eps, e, w, grho, _ = rt_hulls(r0, r1, t0, t1)
    if not (lower(e) > 0 and lower(w) > 0):
        return arb("-inf")
    z = grho / w
    a_over_e = (
        A(fmpq(1, 3))
        - A(fmpq(2, 3)) * eps / e
        - A(fmpq(32, 9)) * w / e
    )
    if lower(a_over_e) >= 0:
        return A(fmpq(1, 3)) + lower(z)
    if upper(a_over_e) <= 0:
        negative_part = a_over_e
    else:
        negative_part = lower(a_over_e).union(arb(0))
    return A(fmpq(1, 3)) + z + (1 - z) * negative_part


def derivative_range_check(
    r0: fmpq, r1: fmpq, t0: fmpq, t1: fmpq
) -> tuple[bool, int, int, float]:
    """Adaptive t-only verification of the normalized derivative."""

    stack = [(t0, t1, 0)]
    processed = 0
    max_depth = 0
    smallest = float("inf")
    while stack:
        left, right, depth = stack.pop()
        processed += 1
        max_depth = max(max_depth, depth)
        try:
            value = derivative_norm_lower(r0, r1, left, right)
        except ArithmeticError:
            value = arb("-inf")
        if value > 0:
            smallest = min(smallest, float(lower(value)))
            continue
        if depth >= 24:
            return False, processed, max_depth, smallest
        mid = (left + right) / 2
        stack.append((mid, right, depth + 1))
        stack.append((left, mid, depth + 1))
    return True, processed, max_depth, smallest


def verify() -> dict[str, int | float]:
    counter = itertools.count()
    heap: list[tuple[int, int, fmpq, fmpq]] = [
        (0, next(counter), RHO_MIN, RHO_MAX)
    ]
    counts: dict[str, int | float] = {
        "rho-panels": 0,
        "rho-splits": 0,
        "empty": 0,
        "positive": 0,
        "derivative-boxes": 0,
        "smallest-boundary-margin": float("inf"),
        "smallest-derivative-margin": float("inf"),
        "max-rho-depth": 0,
        "max-t-depth": 0,
    }

    while heap:
        depth, _, r0, r1 = heapq.heappop(heap)
        counts["rho-panels"] = int(counts["rho-panels"]) + 1
        counts["max-rho-depth"] = max(int(counts["max-rho-depth"]), depth)
        if int(counts["rho-panels"]) > 500_000:
            raise AssertionError("exceeded rho-panel cap")

        roots = beta_root_enclosure(r0, r1)
        active_hi = active_upper_enclosure(r0, r1)
        resolved = roots is not None and active_hi is not None
        if resolved:
            beta_lo, beta_hi = roots
            if beta_lo >= active_hi:
                counts["empty"] = int(counts["empty"]) + 1
                continue
            boundary = boundary_j_lower(r0, r1, beta_lo, beta_hi)
            if boundary > 0:
                ok, boxes, tdepth, derivative_margin = derivative_range_check(
                    r0, r1, beta_lo, active_hi
                )
                counts["derivative-boxes"] = (
                    int(counts["derivative-boxes"]) + boxes
                )
                counts["max-t-depth"] = max(
                    int(counts["max-t-depth"]), tdepth
                )
                if ok:
                    counts["positive"] = int(counts["positive"]) + 1
                    counts["smallest-boundary-margin"] = min(
                        float(counts["smallest-boundary-margin"]),
                        float(boundary),
                    )
                    counts["smallest-derivative-margin"] = min(
                        float(counts["smallest-derivative-margin"]),
                        derivative_margin,
                    )
                    continue

        if depth >= 40:
            raise AssertionError(
                f"unresolved rho panel depth={depth}, rho=[{r0},{r1}], "
                f"roots={roots}, active_hi={active_hi}"
            )
        # Make the physical t=4 boundary rho=4/5 an exact panel edge.
        # A perpetual dyadic split would otherwise keep one panel
        # straddling this rational transition.
        transition = fmpq(4, 5)
        mid = transition if r0 < transition < r1 else (r0 + r1) / 2
        counts["rho-splits"] = int(counts["rho-splits"]) + 1
        heapq.heappush(heap, (depth + 1, next(counter), r0, mid))
        heapq.heappush(heap, (depth + 1, next(counter), mid, r1))

    return counts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=384)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.precision < 256:
        raise AssertionError("precision must be at least 256 bits")
    set_precision(args.precision)
    print("GENERAL-d FIRST-FLOOR s>=2 COMPACT-RATIO CERTIFICATE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print(f"rho range=[{RHO_MIN},{RHO_MAX}]")
    print("All sign decisions are directed-rounding Arb decisions.\n")
    exact_domain_checks()
    ratio_minimum_checks()
    near_one_checks()
    counts = verify()
    print("\nPASS compact ratio sector")
    print(
        "  rho-panels={rho-panels}, rho-splits={rho-splits}, "
        "empty={empty}, positive={positive}".format(**counts)
    )
    print(
        "  derivative-boxes={derivative-boxes}, "
        "max-rho-depth={max-rho-depth}, max-t-depth={max-t-depth}".format(
            **counts
        )
    )
    print(
        "  smallest beta-boundary J_2 lower endpoint "
        f"(diagnostic only) ~{counts['smallest-boundary-margin']:.12g}"
    )
    print(
        "  smallest normalized derivative lower endpoint "
        f"(diagnostic only) ~{counts['smallest-derivative-margin']:.12g}"
    )
    print("\nCERTIFIED globally: true-interface C>0 for the continuous")
    print("active first-floor wall cone beta>=3 (equivalently s>=2).")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
