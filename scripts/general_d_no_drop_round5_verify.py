#!/usr/bin/env python3
"""Arb replay for the Round 5 finite no-drop reductions.

The analytic note ``human/outbox/general-d-round-05-no-drop-finite.md``
uses two small groups of certified constants.

1.  At the unique radius K_* satisfying

        G_{K_*}(3/2) = 7/4,

    the first two exact terminal angles give more than 7/10 of ball
    reserve, the first angle alone gives more than 1/2, and the largest
    possible one-cell inner cap is smaller than 1/5.  These inequalities
    prove D_A(q)>1/2 whenever q>=3/2 and A(q)>=7/4.

2.  Rational comparisons in the direct critical-profile transfer prove
    positivity for s<=1/10.  Together with the f=2,3 no-drop cone, Arb
    checks the convenient common coefficient s<38/n.

All transcendental decisions use outward Arb arithmetic.  Exact rational
comparisons are also replayed here so that a failure in any displayed
constant exits nonzero.
"""

from __future__ import annotations

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this Arb certificate") from exc


ctx.prec = 512
PI = arb.pi()


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(statement: bool, message: str) -> None:
    if not statement:
        raise AssertionError(message)


def g_action(radius: arb | fmpq, position: fmpq) -> arb:
    """G_radius(position), with the whole radius ball above position."""

    rad = radius if isinstance(radius, arb) else A(radius)
    pos = A(position)
    require(rad > pos, "action radius does not lie above the position")
    return (
        (rad * rad - pos * pos).sqrt()
        - pos * (pos / rad).acos()
    ) / PI


def k_ball(lo: fmpq, hi: fmpq) -> arb:
    require(lo < hi, "invalid rational interval")
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2
    out = arb(str(mid), str(rad))
    require(out.contains(A(lo)) and out.contains(A(hi)), "lost an endpoint")
    return out


# Isolate the unique K_* with G_K(3/2)=7/4.  Monotonicity in K is
# analytic; the endpoint signs and the narrow enclosing ball are checked.
q0 = fmpq(3, 2)
level2 = fmpq(7, 4)
lo, hi = fmpq(7), fmpq(8)
require(g_action(lo, q0) < A(level2), "bad lower K_* bracket")
require(g_action(hi, q0) > A(level2), "bad upper K_* bracket")
for _ in range(180):
    mid = (lo + hi) / 2
    if g_action(mid, q0) < A(level2):
        lo = mid
    else:
        hi = mid

require(g_action(lo, q0) < A(level2), "lost lower K_* sign")
require(g_action(hi, q0) > A(level2), "lost upper K_* sign")
KSTAR = k_ball(lo, hi)

# theta_2 is the angle at q0.  For theta_1 it is enough to prove that
# K_* h(503/500)/pi exceeds 3/4; h is strictly increasing.
theta1_upper = A(fmpq(503, 500))
theta2_upper = A(fmpq(11, 8))
theta2 = (A(q0) / KSTAR).acos()
require(theta2 < theta2_upper, "theta_2 < 11/8 was not certified")

h_theta1_upper = theta1_upper.sin() - theta1_upper * theta1_upper.cos()
require(
    KSTAR * h_theta1_upper / PI > A(fmpq(3, 4)),
    "theta_1 < 503/500 was not certified",
)

two_level = PI / 2 * (1 / theta1_upper + 1 / theta2_upper) - 2
one_level = PI / (2 * theta1_upper) - 1
cap_max = g_action(fmpq(5, 2), q0)
require(two_level > A(fmpq(7, 10)), "two-level reserve is not > 7/10")
require(one_level > A(fmpq(1, 2)), "one-level reserve is not > 1/2")
require(cap_max < A(fmpq(1, 5)), "one-cell cap height is not < 1/5")


# Common critical-cone coefficient.  Here
# c_f=(sqrt(1+(f-1/4)^2)-1)/2.  The endpoint action gives
# kappa<3*pi*f/2 and the cone gives delta>=c_f*n/2, hence
# s=kappa/delta<3*pi*f/(c_f*n).  Both f=2 and f=3 coefficients are <38.
c2 = (A(65).sqrt() - 4) / 8
c3 = (A(137).sqrt() - 4) / 8
coef2 = 6 * PI / c2
coef3 = 9 * PI / c3
require(coef2 < 38, "f=2 cone coefficient is not < 38")
require(coef3 < 38, "f=3 cone coefficient is not < 38")


# Rational closure of the s<=1/10 transfer.
c0 = 2 * A(2).sqrt() / (3 * PI)
C = PI / (2 * A(2).sqrt())
require(c0 > A(fmpq(49, 165)), "c0 > 49/165 failed")
require(C > 1, "pi/(2 sqrt(2)) > 1 failed")

F_three_fifths = A(fmpq(163, 125))
ratio_max = A(fmpq(211, 164))
require(F_three_fifths > ratio_max, "critical t>3/5 comparison failed")
require(
    A(fmpq(164, 75)) > A(fmpq(129, 100)) ** 3,
    "terminal cube-root comparison failed",
)

head_upper = A(fmpq(10, 9)) * A(fmpq(47, 100)) ** 2 * A(fmpq(165, 49))
scaled_lower = (
    A(fmpq(129, 100)) * A(fmpq(997, 1000))
    - A(fmpq(17, 50))
    - head_upper
)
require(scaled_lower > A(fmpq(1, 10)), "scaled critical margin is not > 1/10")


print("PASS: Round 5 finite no-drop constants certified with Arb")
print(f"precision: {ctx.prec} bits")
print(f"K_* enclosure: [{lo}, {hi}]")
print(f"two-level lower reserve: {two_level}")
print(f"one-level lower reserve: {one_level}")
print(f"maximum cap height: {cap_max}")
print(f"critical cone coefficients: f=2 {coef2}; f=3 {coef3}")
print(f"scaled s<=1/10 lower margin: {scaled_lower}")
