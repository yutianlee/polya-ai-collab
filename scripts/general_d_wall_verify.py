#!/usr/bin/env python3
"""Rigorous Arb certificate for the finite walls in Proposition 6.5.

The script verifies the residual one-interface ball inequality

    E_r(K) = 2 int_r^K G_K(z) dz - T_K(r) - e_r(K) >= 0

at every point at which it can attain a minimum.  Here r ranges over the
nine half-integral shifts, K lies in (2r, 1/omega_0), and

    G_K(z) = (sqrt(K^2-z^2) - z*acos(z/K))/pi.

All transcendental evaluations use python-flint's Arb ball arithmetic.
Every root bracket has exact rational (dyadic) endpoints and is accepted
only after Arb proves opposite strict signs.  Every displayed decimal
bound is obtained by an additional rigorous comparison with a decimal
rational; floating point is used only to seed that comparison.

Run from the repository root with

    python scripts/general_d_wall_verify.py

The process exits nonzero if any sign, wall separation, floor value, or
positive margin cannot be certified.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover - environment diagnostic
    raise SystemExit(
        "python-flint is required (the repository runtime provides it)"
    ) from exc


# A large guard precision compared with the 140 bisection steps below.
ctx.prec = 512
PI = arb.pi()
QUARTER = arb(fmpq(1, 4))
OMEGA = arb(3).sqrt() / (2 * PI) - arb(fmpq(1, 6))

ROOT_STEPS = 140
ROOT_PRINT_DIGITS = 16
VALUE_PRINT_DIGITS = 12


def A(q: fmpq | int) -> arb:
    """Embed an exact rational/integer into an enclosing Arb ball."""

    return arb(q)


def g_point(k: fmpq, z: fmpq) -> arb:
    """G_k(z) at exact rational inputs, with rigorous enclosure."""

    if k < z:
        return arb(0)
    K, Z = A(k), A(z)
    return ((K * K - Z * Z).sqrt() - Z * (Z / K).acos()) / PI


def g_ball(k: arb, z: fmpq) -> arb:
    """Natural Arb extension of G_K(z); the whole K-ball must exceed z."""

    Z = A(z)
    if not (k > Z):
        raise AssertionError(f"K-ball is not strictly above z={z}")
    return ((k * k - Z * Z).sqrt() - Z * (Z / k).acos()) / PI


def integral_ball(k: arb, r: fmpq) -> arb:
    r"""Rigorous value of 2 int_r^K G_K via its elementary antiderivative."""

    R = A(r)
    if not (k > R):
        raise AssertionError("integral called outside K>r")
    s = (k * k - R * R).sqrt()
    return ((k * k + 2 * R * R) * (R / k).acos() - 3 * R * s) / (2 * PI)


def wall_function(k: fmpq, z: fmpq, level: int) -> arb:
    """G_k(z) - (level-1/4), evaluated rigorously."""

    return g_point(k, z) - arb(fmpq(4 * level - 1, 4))


def k_ball(lo: fmpq, hi: fmpq) -> arb:
    """An Arb ball containing the exact rational interval [lo, hi]."""

    if not lo < hi:
        raise AssertionError("invalid interval")
    mid = (lo + hi) / 2
    rad = (hi - lo) / 2
    # Rational strings are accepted by Arb and rounded outwards.
    out = arb(str(mid), str(rad))
    if not out.contains(A(lo)) or not out.contains(A(hi)):
        raise AssertionError("Arb constructor lost a rational endpoint")
    return out


def isolate_root(z: fmpq, level: int) -> tuple[fmpq, fmpq] | None:
    """Isolate the unique wall root below 10 by exact dyadic bisection."""

    lo, hi = z, fmpq(10)
    f_lo = wall_function(lo, z, level)
    f_hi = wall_function(hi, z, level)
    if not (f_lo < 0):
        raise AssertionError("wall function should be negative at K=z")
    if f_hi < 0:
        return None
    if not (f_hi > 0):
        raise AssertionError(f"could not decide wall existence for z={z}, n={level}")

    for _ in range(ROOT_STEPS):
        mid = (lo + hi) / 2
        f_mid = wall_function(mid, z, level)
        if f_mid < 0:
            lo = mid
        elif f_mid > 0:
            hi = mid
        else:
            raise AssertionError(
                f"insufficient precision in root isolation for z={z}, n={level}"
            )

    if not (wall_function(lo, z, level) < 0):
        raise AssertionError("left root sign was not retained")
    if not (wall_function(hi, z, level) > 0):
        raise AssertionError("right root sign was not retained")

    # This also certifies uniqueness on the bracket.  Analytically it is
    # positive for every K>z, so there is at most one root globally.
    kb = k_ball(lo, hi)
    Z = A(z)
    derivative = (1 - (Z / kb) ** 2).sqrt() / PI
    if not (derivative > 0):
        raise AssertionError("failed to certify positive wall derivative")
    return lo, hi


@dataclass(frozen=True)
class Wall:
    r: fmpq
    j: int
    level: int
    lo: fmpq
    hi: fmpq

    @property
    def z(self) -> fmpq:
        return self.r + self.j


def classify_nonwall(value: arb, label: str) -> int:
    """Return [value]_< when value is rigorously separated from all walls."""

    for q in range(4):
        if value > q and value < q + 1:
            return q
    raise AssertionError(f"could not classify strict floor at {label}: {value}")


def q_at_wall(kb: arb, wall: Wall, sample_j: int) -> int:
    """Strict bracket immediately to the right of a specified wall."""

    z = wall.r + sample_j
    if sample_j == wall.j:
        target = g_ball(kb, z) + QUARTER
        if not target.contains(wall.level):
            raise AssertionError("isolated root is absent from its Arb image")
        return wall.level

    # Samples to the right of the zero endpoint contribute zero.  If a very
    # narrow root interval happens to straddle z, monotonicity in K plus the
    # upper endpoint still rigorously proves the zero bracket.
    if wall.hi <= z:
        return 0
    if wall.lo <= z:
        upper_value = g_point(wall.hi, z) + QUARTER
        if upper_value < 1:
            return 0
        raise AssertionError("endpoint-straddling sample was not classifiable")

    value = g_ball(kb, z) + QUARTER
    return classify_nonwall(value, f"r={wall.r}, wall j={wall.j}, sample j={sample_j}")


def wall_margin(wall: Wall) -> tuple[arb, int, arb]:
    """Return (right-hand E, right-hand tail integer, right-hand e)."""

    kb = k_ball(wall.lo, wall.hi)
    qs = []
    sample_j = 0
    while wall.r + sample_j < 10:
        qs.append(q_at_wall(kb, wall, sample_j))
        sample_j += 1
    tail = qs[0] + 2 * sum(qs[1:])

    if wall.j == 0:
        # At a first-sample wall e=1 at the wall and e=0 immediately right.
        remainder = arb(0)
    else:
        first_value = g_ball(kb, wall.r) + QUARTER
        remainder = first_value - qs[0]
        if not (remainder > 0 and remainder < 1):
            raise AssertionError("first-sample remainder is not in (0,1)")

    margin = integral_ball(kb, wall.r) - tail - remainder
    if not (margin > 0):
        raise AssertionError(
            f"NONPOSITIVE WALL MARGIN r={wall.r}, j={wall.j}, "
            f"n={wall.level}: {margin}"
        )
    return margin, tail, remainder


def endpoint_data(r: fmpq) -> tuple[arb, int, arb]:
    """Evaluate E at the lower endpoint K=2r (no wall occurs there)."""

    k = 2 * r
    K = A(k)
    qs = []
    sample_j = 0
    while r + sample_j < 10:
        z = r + sample_j
        value = (g_point(k, z) if z <= k else arb(0)) + QUARTER
        qs.append(classify_nonwall(value, f"endpoint r={r}, sample j={sample_j}"))
        sample_j += 1
    tail = qs[0] + 2 * sum(qs[1:])
    remainder = g_point(k, r) + QUARTER - qs[0]
    margin = integral_ball(K, r) - tail - remainder
    if tail > 0 and not (margin > 0):
        raise AssertionError(f"nonpositive required endpoint at r={r}: {margin}")
    return margin, tail, remainder


def scaled_floor(q: fmpq, scale: int) -> int:
    return (int(q.p) * scale) // int(q.q)


def scaled_ceil(q: fmpq, scale: int) -> int:
    return -((-int(q.p) * scale) // int(q.q))


def decimal_from_scaled(value: int, digits: int) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**digits
    return f"{sign}{value // scale}.{value % scale:0{digits}d}"


def rational_interval_text(lo: fmpq, hi: fmpq, digits: int) -> str:
    scale = 10**digits
    left = scaled_floor(lo, scale)
    right = scaled_ceil(hi, scale)
    return (
        "["
        + decimal_from_scaled(left, digits)
        + ", "
        + decimal_from_scaled(right, digits)
        + "]"
    )


def ball_interval_text(value: arb, digits: int) -> str:
    """Produce a rigorously verified enclosing decimal interval."""

    scale = 10**digits
    seed = float(value.mid())
    lower = math.floor(seed * scale) - 2
    while not (value > A(fmpq(lower, scale))):
        lower -= 1
    while value > A(fmpq(lower + 1, scale)):
        lower += 1

    upper = math.ceil(seed * scale) + 2
    while not (value < A(fmpq(upper, scale))):
        upper += 1
    while value < A(fmpq(upper - 1, scale)):
        upper -= 1

    if not (value > A(fmpq(lower, scale)) and value < A(fmpq(upper, scale))):
        raise AssertionError("reported decimal interval was not certified")
    return (
        "["
        + decimal_from_scaled(lower, digits)
        + ", "
        + decimal_from_scaled(upper, digits)
        + "]"
    )


def main() -> None:
    if not (PI > 3):
        raise AssertionError("failed to certify pi>3 for the level cutoff")
    if not (OMEGA > A(fmpq(1, 10)) and OMEGA < A(fmpq(1, 9))):
        raise AssertionError("failed to certify 1/10 < omega_0 < 1/9")

    shifts = [fmpq(k, 2) for k in range(1, 10)]
    walls: list[Wall] = []
    counts = {"candidate": 0, "no-root<10": 0, "below-2r": 0, "above-Kmax": 0}

    for r in shifts:
        if not (OMEGA * A(2 * r) < 1):
            raise AssertionError(f"empty residual interval for r={r}")
        j = 0
        while r + j < 10:
            z = r + j
            for level in (1, 2, 3):
                counts["candidate"] += 1
                bracket = isolate_root(z, level)
                if bracket is None:
                    counts["no-root<10"] += 1
                    continue
                lo, hi = bracket

                if hi < 2 * r:
                    counts["below-2r"] += 1
                    continue
                if not lo > 2 * r:
                    raise AssertionError(
                        f"wall relation to K=2r unresolved: r={r}, j={j}, n={level}"
                    )

                if OMEGA * A(lo) > 1:
                    counts["above-Kmax"] += 1
                    continue
                if not (OMEGA * A(hi) < 1):
                    raise AssertionError(
                        f"wall relation to Kmax unresolved: r={r}, j={j}, n={level}"
                    )
                walls.append(Wall(r, j, level, lo, hi))
            j += 1

    # Disjoint rational root intervals rule out simultaneous sample walls.
    for r in shifts:
        local = sorted((w for w in walls if w.r == r), key=lambda w: w.lo)
        for left, right in zip(local, local[1:]):
            if not left.hi < right.lo:
                raise AssertionError(f"unresolved coincident walls for r={r}")

    if (
        counts["no-root<10"]
        + counts["below-2r"]
        + counts["above-Kmax"]
        + len(walls)
        != counts["candidate"]
    ):
        raise AssertionError("candidate scan did not form an exhaustive partition")

    print("GENERAL-d FINITE WALL CERTIFICATE")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print("All inequalities below are directed-rounding Arb decisions.")
    print("Every K interval has exact dyadic endpoints with H(lo)<0<H(hi).")
    print(
        "omega_0 is certified in (1/10,1/9), hence "
        "1/omega_0 is in (9,10)."
    )
    print(
        "candidate scan: "
        + ", ".join(f"{key}={value}" for key, value in counts.items())
        + f", in-domain={len(walls)}"
    )
    print()

    required_values: list[tuple[str, arb]] = []
    for r in shifts:
        endpoint_margin, endpoint_tail, _ = endpoint_data(r)
        if endpoint_tail:
            endpoint_status = "REQUIRED-PASS"
            required_values.append((f"r={r}, K=2r", endpoint_margin))
        else:
            endpoint_status = "tail-zero/not-required"
        print(
            f"r={r}: K=2r endpoint, T={endpoint_tail}, {endpoint_status}, "
            f"E={ball_interval_text(endpoint_margin, VALUE_PRINT_DIGITS)}"
        )

        local = sorted((w for w in walls if w.r == r), key=lambda w: w.lo)
        if endpoint_tail == 0:
            first = [w for w in local if w.j == 0 and w.level == 1]
            if len(first) != 1:
                raise AssertionError(f"missing unique first positive-count wall for r={r}")
            if not local or local[0] != first[0]:
                raise AssertionError(f"first positive-count wall is not the first wall for r={r}")

        for wall in local:
            margin, tail, _ = wall_margin(wall)
            required_values.append(
                (f"r={r}, j={wall.j}, n={wall.level}", margin)
            )
            kind = "FIRST" if wall.j == 0 else "LATER"
            if endpoint_tail == 0 and wall.j == 0 and wall.level == 1:
                kind += "+FIRST-POSITIVE"
            print(
                f"  {kind:20s} j={wall.j:2d}, z={str(wall.z):>4s}, "
                f"n={wall.level}, K={rational_interval_text(wall.lo, wall.hi, ROOT_PRINT_DIGITS)}, "
                f"T_right={tail:2d}, E_right={ball_interval_text(margin, VALUE_PRINT_DIGITS)}"
            )
        print()

    if not required_values:
        raise AssertionError("no required values were checked")
    minimum_label, overall_lower = required_values[0]
    for label, value in required_values[1:]:
        if value < overall_lower:
            minimum_label, overall_lower = label, value
        elif not (overall_lower < value):
            raise AssertionError(
                f"could not rigorously order candidate minima {minimum_label} and {label}"
            )
    if not (overall_lower > 0):
        raise AssertionError("no positive global margin was certified")
    print(
        "CERTIFIED: every required endpoint and every right-hand wall limit "
        "has E_r(K)>0."
    )
    print(
        f"Unique smallest checked value ({minimum_label}) lies in "
        + ball_interval_text(overall_lower, VALUE_PRINT_DIGITS)
        + "."
    )


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
