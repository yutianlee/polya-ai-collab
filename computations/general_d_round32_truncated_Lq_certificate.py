#!/usr/bin/env python3
"""One compact Arb certificate for the Round 32 truncated L_q triangles.

This is the only load-bearing numerical certificate in the Round 32
implication.  It covers the exact integer and half-integer q grids below
the analytic Round 31 cutoff q=1000.  The p=1 edge is positive
analytically; this program certifies the minima on r=r_0 and m=m_#.

All transcendental quantities are enclosed with python-flint Arb balls.
Every q and every bisection midpoint is an exact integer or dyadic
rational.  The fixed loop bounds are also a finite termination proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import flint
from flint import arb, ctx


PRECISION_BITS = 192
THETA_BISECTIONS = 100
EDGE_BISECTIONS = 70
Q2_MIN = 6       # q=3
Q2_MAX = 1999    # q=999.5; Round 31 owns every real q>=1000
CERTIFIED_MARGIN = Fraction(1, 100)

ctx.prec = PRECISION_BITS
PI = arb.pi()


def as_arb(value: int | Fraction) -> arb:
    """Enclose an exact integer or rational in an Arb ball."""

    if isinstance(value, Fraction):
        return arb(f"{value.numerator}/{value.denominator}")
    return arb(value)


def rational_interval(lo: Fraction, hi: Fraction) -> arb:
    """Return an Arb ball containing the exact interval [lo,hi]."""

    if not lo <= hi:
        raise ValueError("reversed rational interval")
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2
    return arb(
        f"{mid.numerator}/{mid.denominator}",
        f"{rad.numerator}/{rad.denominator}",
    )


def inverse_angle(q2: int, displacement: int) -> arb:
    """Enclose the unique theta in (0,1) solving its inverse-level equation."""

    q = arb(q2) / 2
    rhs = 3 * PI / (4 * (q + displacement))

    def residual(theta: Fraction) -> arb:
        value = as_arb(theta)
        return value.tan() - value - rhs

    lo = Fraction(0)
    hi = Fraction(1)
    if not (residual(lo) < 0 and residual(hi) > 0):
        raise ArithmeticError("initial inverse-angle bracket failed")

    # tan(theta)-theta is strictly increasing on (0,1).  Exact dyadic
    # bisection therefore preserves a bracket for the unique root.
    for _ in range(THETA_BISECTIONS):
        mid = (lo + hi) / 2
        sign = residual(mid)
        if sign < 0:
            lo = mid
        elif sign > 0:
            hi = mid
        else:
            raise ArithmeticError("Arb could not decide an inverse-angle sign")

    if not (residual(lo) < 0 and residual(hi) > 0):
        raise ArithmeticError("final inverse-angle bracket failed")
    return rational_interval(lo, hi)


@dataclass(frozen=True)
class Coefficients:
    q: arb
    A: arb
    B: arb
    d: arb
    psi: arb


def coefficients(q2: int) -> Coefficients:
    q = arb(q2) / 2
    theta2 = inverse_angle(q2, 2)
    theta3 = inverse_angle(q2, 3)
    k2 = (q + 2) / theta2.cos()
    A = (1 / (q + 1) - 1 / k2) / (2 * PI)
    B = (1 / (q + 1) ** 3 - 1 / k2**3) / (24 * PI)
    psi = (q * theta3.cos() / (q + 3)).acos()
    d = 1 - 2 * psi / PI
    if not (A > 0 and B > 0 and d > 0 and psi > 0):
        raise ArithmeticError("coefficient sign enclosure failed")
    return Coefficients(q, A, B, d, psi)


def lower_scalar(p: arb, x: arb, m: arb, data: Coefficients) -> arb:
    """The Round 31 polynomial lower scalar L_q(p,x)."""

    return (
        arb(7) / 10
        + arb(2)
        / 3
        * p**2
        * (3 * x - p)
        * (data.A + data.B * (x**2 + (x - p) ** 2))
        - p / 2
        + data.d * m / 2
    )


def fixed_m_derivative(p: arb, x: arb, data: Coefficients) -> arb:
    v = data.A + data.B * (x**2 + (x - p) ** 2)
    return (
        arb(2)
        / 3
        * (
            2 * p * (3 * x - p) * v
            + p**2 * (-v + (3 * x - p) * 2 * data.B * (p - x))
        )
        - arb(1) / 2
    )


def fixed_r_derivative(p: arb, r: arb, data: Coefficients) -> arb:
    v = data.A + data.B * ((p + r) ** 2 + r**2)
    return (
        arb(2)
        / 3
        * (
            6 * p * (p + r) * v
            + p**2 * (2 * p + 3 * r) * 2 * data.B * (p + r)
        )
        - (1 + data.d) / 2
    )


@dataclass(frozen=True)
class MinimumEnclosure:
    value: arb
    p: arb
    location: str


def convex_minimum(
    p_lo: Fraction,
    p_hi: Fraction,
    derivative,
    value,
) -> MinimumEnclosure:
    """Enclose the minimum of a proved strictly convex edge function."""

    lo = p_lo
    hi = p_hi
    d_lo = derivative(as_arb(lo))
    d_hi = derivative(as_arb(hi))
    if d_lo > 0:
        point = as_arb(lo)
        return MinimumEnclosure(value(point), point, "left")
    if d_hi < 0:
        point = as_arb(hi)
        return MinimumEnclosure(value(point), point, "right")
    if not (d_lo < 0 and d_hi > 0):
        raise ArithmeticError("edge derivative bracket failed")

    # The derivative is strictly increasing by the analytic Round 31
    # edge-convexity proof.  This fixed bisection encloses its unique zero.
    for _ in range(EDGE_BISECTIONS):
        mid = (lo + hi) / 2
        sign = derivative(as_arb(mid))
        if sign < 0:
            lo = mid
        elif sign > 0:
            hi = mid
        else:
            raise ArithmeticError("Arb could not decide an edge-derivative sign")

    if not (derivative(as_arb(lo)) < 0 and derivative(as_arb(hi)) > 0):
        raise ArithmeticError("final edge-derivative bracket failed")
    p_ball = rational_interval(lo, hi)
    return MinimumEnclosure(value(p_ball), p_ball, "interior")


@dataclass(frozen=True)
class EdgeRecord:
    lower: arb
    q2: int
    edge: str
    m_sharp: int
    minimum: MinimumEnclosure


def update_record(current: EdgeRecord | None, candidate: EdgeRecord) -> EdgeRecord:
    if current is None or candidate.lower < current.lower:
        return candidate
    return current


def main() -> None:
    global_record: EdgeRecord | None = None
    edge_records: dict[str, EdgeRecord | None] = {"r": None, "m": None}
    blocks: list[tuple[int, int, int]] = []
    block_start = Q2_MIN
    previous_m: int | None = None
    q_count = 0
    edge_count = 0

    for q2 in range(Q2_MIN, Q2_MAX + 1):
        data = coefficients(q2)
        q_fraction = Fraction(q2, 2)
        r0_fraction = Fraction(1) if q2 % 2 == 0 else Fraction(3, 2)
        r0 = as_arb(r0_fraction)

        if q2 < 70:  # q<35: use the full Round 31 triangle
            m_sharp = 1
        else:
            shelf_bound = arb(6) / 5 * (PI / data.psi - 3)
            # unique_fmpz succeeds only if Arb proves that the ball has one
            # floor, so this also certifies every integer transition.
            m_sharp = int(shelf_bound.floor().unique_fmpz()) + 1

        if previous_m is None:
            previous_m = m_sharp
            block_start = q2
        elif m_sharp != previous_m:
            blocks.append((previous_m, block_start, q2 - 1))
            previous_m = m_sharp
            block_start = q2

        p_hi = q_fraction - r0_fraction - m_sharp
        if p_hi < 1:
            raise ArithmeticError("unexpected empty truncated triangle")

        # Boundary r=r_0; here x=p+r_0 and m=q-p-r_0.
        r_minimum = convex_minimum(
            Fraction(1),
            p_hi,
            lambda p: fixed_r_derivative(p, r0, data),
            lambda p: lower_scalar(
                p,
                p + r0,
                data.q - p - r0,
                data,
            ),
        )
        r_record = EdgeRecord(
            r_minimum.value.lower(), q2, "r=r0", m_sharp, r_minimum
        )
        if not r_minimum.value > as_arb(CERTIFIED_MARGIN):
            raise ArithmeticError(f"r-edge margin failed at q2={q2}")
        edge_records["r"] = update_record(edge_records["r"], r_record)
        global_record = update_record(global_record, r_record)
        edge_count += 1

        # Boundary m=m_#; here x=q-m_# is constant.
        m = arb(m_sharp)
        x = data.q - m
        m_minimum = convex_minimum(
            Fraction(1),
            p_hi,
            lambda p: fixed_m_derivative(p, x, data),
            lambda p: lower_scalar(p, x, m, data),
        )
        m_record = EdgeRecord(
            m_minimum.value.lower(), q2, "m=mSharp", m_sharp, m_minimum
        )
        if not m_minimum.value > as_arb(CERTIFIED_MARGIN):
            raise ArithmeticError(f"m-edge margin failed at q2={q2}")
        edge_records["m"] = update_record(edge_records["m"], m_record)
        global_record = update_record(global_record, m_record)
        edge_count += 1
        q_count += 1

    if previous_m is not None:
        blocks.append((previous_m, block_start, Q2_MAX))

    assert global_record is not None
    assert edge_records["r"] is not None and edge_records["m"] is not None
    if q_count != Q2_MAX - Q2_MIN + 1 or edge_count != 2 * q_count:
        raise ArithmeticError("coverage count mismatch")

    print("ROUND 32 TRUNCATED L_q CERTIFICATE")
    print(f"pythonFlintVersion={flint.__version__}")
    print(f"arbPrecisionBits={PRECISION_BITS}")
    print(f"thetaBisections={THETA_BISECTIONS}")
    print(f"edgeBisections={EDGE_BISECTIONS}")
    print(f"q2Range={Q2_MIN}..{Q2_MAX}")
    print(f"qCount={q_count}")
    print(f"certifiedEdgeCount={edge_count}")
    print("pEqualsOneAnalyticLowerBound=1/5")
    print("certifiedNontrivialEdgeMargin=1/100")
    print("mSharpBlocks=(m,q2Start,q2End)")
    for block in blocks:
        print(block)
    for key in ("r", "m"):
        record = edge_records[key]
        assert record is not None
        print(
            f"{key}EdgeMinimumLower={record.lower.str(30)};"
            f"q={record.q2}/2;mSharp={record.m_sharp};"
            f"p={record.minimum.p.str(20)};"
            f"location={record.minimum.location}"
        )
    print(f"globalMinimumLower={global_record.lower.str(30)}")
    print("round32TruncatedLqCertificateOK=True")


if __name__ == "__main__":
    main()
