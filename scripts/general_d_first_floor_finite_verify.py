#!/usr/bin/env python3
"""Rigorous Arb certificate for the finite ordinary first-floor sector.

This script proves positivity at the implicit wall A(r+p)=3/4 for every

    r in (1/2) N,  r >= 3/2,  p >= 0,
    s = n-p-1 in {0,1},  x=r+p < 100,
    alpha=mu-(r+n) in [0,1].

The stronger true-interface certificate is used:

    C = p(a+b) + (n-p)(b+u) + alpha(u+h) + h^2/c - (1+2p),

where b=A(x)=3/4, a=A(r), u=A(q), h=G_K(mu), and
c=acos(mu/K)/pi.  The first drop makes every sample after x vanish.
Concavity gives the first three trapezoidal action terms, and the tangent
triangle under the outer convex ball profile gives h^2/c.

The implicit wall root is never replaced by a floating-point sample.  At
each exact rational alpha endpoint it is isolated by rational bisection
with every sign decided by directed-rounding Arb arithmetic.  Monotonicity
along the wall supplies correlated endpoint bounds, so only four chambers
need one alpha bisection.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


PI: arb
THREE_QUARTERS: arb
ROOT_STEPS = 110
MAX_DEPTH = 12


def set_precision(bits: int) -> None:
    global PI, THREE_QUARTERS
    ctx.prec = bits
    PI = arb.pi()
    THREE_QUARTERS = arb(fmpq(3, 4))


def A(q: fmpq | int) -> arb:
    return arb(q)


def g_point(radius: fmpq, z: fmpq) -> arb:
    """Evaluate G_radius(z), with exact rational inputs, in Arb."""

    if radius < z:
        raise AssertionError(f"radius {radius} is below sample {z}")
    if radius == z:
        return arb(0)
    R, Z = A(radius), A(z)
    return ((R * R - Z * Z).sqrt() - Z * (Z / R).acos()) / PI


def wall_value(k: fmpq, mu: fmpq, x: fmpq) -> arb:
    return g_point(k, x) - g_point(mu, x) - THREE_QUARTERS


def isolate_wall(mu: fmpq, x: fmpq) -> tuple[fmpq, fmpq]:
    """Return a strict rational bracket for A(x)=3/4 at fixed mu."""

    lo = mu
    if not (wall_value(lo, mu, x) < 0):
        raise AssertionError("wall function is not strictly negative at K=mu")
    hi = mu + 1
    while wall_value(hi, mu, x) < 0:
        hi += 1
        if hi > mu + 100:
            raise AssertionError("wall root was not found below mu+100")
    if not (wall_value(hi, mu, x) > 0):
        raise AssertionError("could not decide the upper wall sign")

    for _ in range(ROOT_STEPS):
        mid = (lo + hi) / 2
        value = wall_value(mid, mu, x)
        if value < 0:
            lo = mid
        elif value > 0:
            hi = mid
        else:
            raise AssertionError("insufficient precision in wall isolation")

    if not (wall_value(lo, mu, x) < 0 and wall_value(hi, mu, x) > 0):
        raise AssertionError("wall bracket lost its strict endpoint signs")
    return lo, hi


@dataclass(frozen=True)
class Chamber:
    r: fmpq
    p: int
    s: int

    @property
    def n(self) -> int:
        return self.p + self.s + 1

    @property
    def x(self) -> fmpq:
        return self.r + self.p

    @property
    def q(self) -> fmpq:
        return self.r + self.n

    @property
    def label(self) -> str:
        return f"(r,p,s)=({self.r},{self.p},{self.s})"


def lower_certificate(
    ch: Chamber,
    alpha_lo: fmpq,
    alpha_hi: fmpq,
    root_lo: tuple[fmpq, fmpq],
    root_hi: tuple[fmpq, fmpq],
) -> arb:
    """Lower-bound C on one exact rational alpha interval.

    Along the wall K=K(mu), A(r) decreases, A(q) increases, and h and c
    decrease.  The root brackets are (K_-,K_+) at the two endpoints.
    Consequently the following deliberately one-sided evaluations are all
    rigorous lower/upper bounds in the directions needed by C.
    """

    mu_lo = ch.q + alpha_lo
    mu_hi = ch.q + alpha_hi

    # a=A(r) decreases: evaluate its lower proxy at mu_hi and K_-.
    a_lo = g_point(root_hi[0], ch.r) - g_point(mu_hi, ch.r)

    # u=A(q) increases: evaluate its lower proxy at mu_lo and K_-.
    u_lo = g_point(root_lo[0], ch.q) - g_point(mu_lo, ch.q)

    # h=G_K(mu) decreases: evaluate its lower proxy at mu_hi and K_-.
    h_lo = g_point(root_hi[0], mu_hi)

    # c decreases along the wall.  At mu_lo, K_+ gives an upper proxy.
    c_hi = (A(mu_lo) / A(root_lo[1])).acos() / PI
    if not (a_lo > 0 and u_lo > 0 and h_lo > 0 and c_hi > 0):
        raise AssertionError(
            f"nonpositive endpoint proxy in {ch.label}, "
            f"alpha=[{alpha_lo},{alpha_hi}]"
        )

    b = THREE_QUARTERS
    return (
        ch.p * (a_lo + b)
        + (ch.n - ch.p) * (b + u_lo)
        + A(alpha_lo) * (u_lo + h_lo)
        + h_lo * h_lo / c_hi
        - (1 + 2 * ch.p)
    )


def chamber_list() -> list[Chamber]:
    chambers: list[Chamber] = []
    for s in (0, 1):
        for twice_r in range(3, 200):
            r = fmpq(twice_r, 2)
            p = 0
            while r + p < 100:
                chambers.append(Chamber(r, p, s))
                p += 1
    if len(chambers) != 19_602:
        raise AssertionError(f"unexpected chamber count {len(chambers)}")
    return chambers


def verify_chamber(ch: Chamber) -> dict[str, object]:
    root_cache: dict[fmpq, tuple[fmpq, fmpq]] = {}

    def root(alpha: fmpq) -> tuple[fmpq, fmpq]:
        if alpha not in root_cache:
            root_cache[alpha] = isolate_wall(ch.q + alpha, ch.x)
        return root_cache[alpha]

    stack = [(fmpq(0), fmpq(1), 0)]
    processed = 0
    leaves = 0
    max_depth = 0
    min_midpoint = float("inf")

    while stack:
        alpha_lo, alpha_hi, depth = stack.pop()
        processed += 1
        max_depth = max(max_depth, depth)
        value = lower_certificate(
            ch, alpha_lo, alpha_hi, root(alpha_lo), root(alpha_hi)
        )
        if value > 0:
            leaves += 1
            min_midpoint = min(min_midpoint, float(value.mid()))
            continue
        if depth >= MAX_DEPTH:
            raise AssertionError(
                f"unresolved {ch.label}, alpha=[{alpha_lo},{alpha_hi}], "
                f"depth={depth}, C={value}"
            )
        mid = (alpha_lo + alpha_hi) / 2
        stack.append((mid, alpha_hi, depth + 1))
        stack.append((alpha_lo, mid, depth + 1))

    return {
        "processed": processed,
        "leaves": leaves,
        "roots": len(root_cache),
        "max_depth": max_depth,
        "min_midpoint": min_midpoint,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=384)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.precision < 256:
        raise AssertionError("precision must be at least 256 bits")
    set_precision(args.precision)

    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
    print("GENERAL-d FINITE FIRST-FLOOR WALL CERTIFICATE")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print(f"root bisections per endpoint={ROOT_STEPS}")
    print(f"script_sha256={script_hash}")
    print("All sign decisions are directed-rounding Arb decisions.\n")

    chambers = chamber_list()
    totals = {
        "chambers": 0,
        "processed": 0,
        "leaves": 0,
        "roots": 0,
        "max_depth": 0,
        "min_midpoint": float("inf"),
    }
    by_s: dict[int, dict[str, object]] = {}

    for index, ch in enumerate(chambers, start=1):
        result = verify_chamber(ch)
        totals["chambers"] += 1
        for key in ("processed", "leaves", "roots"):
            totals[key] += int(result[key])
        totals["max_depth"] = max(totals["max_depth"], int(result["max_depth"]))
        totals["min_midpoint"] = min(
            totals["min_midpoint"], float(result["min_midpoint"])
        )

        row = by_s.setdefault(
            ch.s,
            {
                "chambers": 0,
                "processed": 0,
                "leaves": 0,
                "roots": 0,
                "max_depth": 0,
                "min_midpoint": float("inf"),
            },
        )
        row["chambers"] = int(row["chambers"]) + 1
        for key in ("processed", "leaves", "roots"):
            row[key] = int(row[key]) + int(result[key])
        row["max_depth"] = max(int(row["max_depth"]), int(result["max_depth"]))
        row["min_midpoint"] = min(
            float(row["min_midpoint"]), float(result["min_midpoint"])
        )

        if index % 2500 == 0:
            print(f"  progress: chambers={index}/{len(chambers)}")

    for s in (0, 1):
        row = by_s[s]
        print(f"\nPASS s={s}")
        print(
            "  chambers={chambers}, processed-panels={processed}, "
            "accepted-leaves={leaves}, isolated-roots={roots}, "
            "max-depth={max_depth}".format(**row)
        )
        print(
            "  smallest accepted interval midpoint "
            f"(diagnostic only) ~{float(row['min_midpoint']):.12g}"
        )

    print("\nCERTIFIED: C>0 in every finite first-floor wall chamber")
    print("  r>=3/2, s in {0,1}, x=r+p<100, alpha in [0,1].")
    print(
        "  chambers={chambers}, processed-panels={processed}, "
        "accepted-leaves={leaves}, isolated-roots={roots}, "
        "max-depth={max_depth}".format(**totals)
    )
    print(
        "  smallest accepted interval midpoint "
        f"(diagnostic only) ~{float(totals['min_midpoint']):.12g}"
    )


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
