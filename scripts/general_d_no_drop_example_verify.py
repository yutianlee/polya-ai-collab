#!/usr/bin/env python3
"""Arb replay of the active no-drop obstruction in the Round 4 note.

The exact inputs are

    K = 23/4,  mu = 103/40,  r = 1/2,  n = 2,  q = 5/2.

The script proves, with outward Arb intervals, that the three inner
ordinary floors equal one, the terminal strict count is one, and

    R_2 < -0.34,  D_A(q) > 0.94,  D_A(q) + R_2 > 0.59.

Run from the repository root with

    python scripts/general_d_no_drop_example_verify.py
"""

from __future__ import annotations

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this Arb certificate") from exc


ctx.prec = 256
PI = arb.pi()

K = fmpq(23, 4)
MU = fmpq(103, 40)
R = fmpq(1, 2)
Q = fmpq(5, 2)
N = 2
M = 1


def A(value: fmpq | int) -> arb:
    return arb(value)


def action(radius: fmpq, z: fmpq) -> arb:
    """Rigorous G_radius(z) at exact rational inputs."""

    if radius <= z:
        return arb(0)
    rad, pos = A(radius), A(z)
    return (
        (rad * rad - pos * pos).sqrt()
        - pos * (pos / rad).acos()
    ) / PI


def twice_integral(radius: fmpq, z: fmpq) -> arb:
    """Rigorous value of 2*integral_z^radius G_radius."""

    if radius <= z:
        return arb(0)
    rad, pos = A(radius), A(z)
    root = (rad * rad - pos * pos).sqrt()
    return (
        (rad * rad + 2 * pos * pos) * (pos / rad).acos()
        - 3 * pos * root
    ) / (2 * PI)


def shell_action(z: fmpq) -> arb:
    return action(K, z) - action(MU, z)


def require(statement: bool, message: str) -> None:
    if not statement:
        raise AssertionError(message)


require(A(K - MU) > PI, "the example is not in K-mu>pi")

inner_points = (R, R + 1, Q)
inner_values = tuple(shell_action(z) for z in inner_points)
for z, value in zip(inner_points, inner_values):
    require(value > A(fmpq(3, 4)), f"A({z}) is not above 3/4")
    require(value < A(fmpq(7, 4)), f"A({z}) is not below 7/4")

# A is decreasing.  Once q+1 is below 3/4, every later strict count
# vanishes; at q the strict count is exactly one.
require(shell_action(Q + 1) < A(fmpq(3, 4)), "terminal count is not one")

head = (
    twice_integral(K, R)
    - twice_integral(K, Q)
    - twice_integral(MU, R)
    + twice_integral(MU, Q)
    - 2 * N * M
)
terminal = twice_integral(K, Q) - twice_integral(MU, Q) - 1
scalar = head + terminal

require(head < A(fmpq(-34, 100)), "failed to prove R_2 < -0.34")
require(terminal > A(fmpq(94, 100)), "failed to prove D_A(q) > 0.94")
require(scalar > A(fmpq(59, 100)), "failed to prove scalar > 0.59")

print("PASS: active no-drop obstruction certified at 256-bit Arb precision")
for z, value in zip(inner_points, inner_values):
    print(f"A({z}) = {value}")
print(f"R_2 = {head}")
print(f"D_A(q) = {terminal}")
print(f"D_A(q)+R_2 = {scalar}")
