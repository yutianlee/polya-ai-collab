#!/usr/bin/env python3
"""Rigorous certificate for the two ordinary first-floor small starts.

This script proves the finite part

    r in {1/2, 1},  s=n-p-1 in {0,1},
    p >= 0,  x=r+p < 100,  alpha=mu-(r+n) in [0,1]

on the implicit wall A(x)=3/4.  It uses the stronger true-interface
certificate and the correlated wall-panel implementation from the
independently audited finite first-floor verifier.

It also certifies every numerical constant in the elementary analytic
argument for x>=100.  On that ray the wall equation gives K<6x/5, hence

    A(r)/A(x) > 5/3,  so A(r)>5/4.

The already proved weakened wall certificate is then strictly positive.
Thus the finite Arb computation and the analytic ray cover all p>=0.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

try:
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc

import general_d_first_floor_finite_verify as core


AUDITED_CORE_SHA256 = (
    "9F7C35279FD1E3FC47BF53C26A7D8681527703FE092BC3AA0831BD160609598D"
)
RAY_THRESHOLD = 100


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def certify_ray_constants() -> dict[str, object]:
    """Certify the directed-rounding and exact rational ray comparisons."""

    pi = arb.pi()
    c_delta = ((9 * pi * arb(2).sqrt()) / 8).root(3) ** 2
    c_upper = arb(fmpq(731, 250))
    require(c_delta < c_upper, "delta constant C<731/250 unresolved")

    t_star_q = fmpq(53861, 250000)
    t_star = arb(t_star_q)
    require(
        t_star * arb(RAY_THRESHOLD).root(3) > 1,
        "T_*>100^(-1/3) unresolved",
    )

    # For t=x^(-1/3)<=T_* and beta<=3,
    # K/x <= 1+3t^3+(731/250)t^2 < 6/5.
    k_ratio_q = (
        fmpq(1)
        + 3 * t_star_q**3
        + fmpq(731, 250) * t_star_q**2
    )
    require(k_ratio_q < fmpq(6, 5), "K/x<6/5 rational check failed")

    # If the preliminary alternative delta>=x-beta held, the wall integral
    # would be at least x*sqrt(5)/6.  The x=100 endpoint already contradicts
    # 3*pi/4, and the lower bound increases with x.
    require(
        arb(RAY_THRESHOLD) * arb(5).sqrt() / 6 > 3 * pi / 4,
        "preliminary delta<x-beta comparison unresolved",
    )

    # With r<=1, x>=100, and K<6x/5,
    #
    # (f_r(K)/f_x(K))^2
    #   > (36*x^2-25)/(11*x^2)
    #   >= (36-25/10000)/11 > 25/9.
    ratio_sq_q = (
        fmpq(36) - fmpq(25, RAY_THRESHOLD * RAY_THRESHOLD)
    ) / 11
    require(
        ratio_sq_q > fmpq(25, 9),
        "wall action ratio square does not exceed 25/9",
    )

    return {
        "c_delta_mid": float(c_delta.mid()),
        "k_ratio": float(arb(k_ratio_q).mid()),
        "ratio_sq": float(arb(ratio_sq_q).mid()),
    }


def chamber_list() -> list[core.Chamber]:
    chambers: list[core.Chamber] = []
    for s in (0, 1):
        for r in (fmpq(1, 2), fmpq(1)):
            p = 0
            while r + p < RAY_THRESHOLD:
                chambers.append(core.Chamber(r, p, s))
                p += 1
    require(len(chambers) == 398, f"unexpected chamber count {len(chambers)}")
    return chambers


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=384)
    parser.add_argument("--root-steps", type=int, default=110)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    require(args.precision >= 256, "precision must be at least 256 bits")
    require(args.root_steps >= 80, "root isolation needs at least 80 steps")

    core_path = Path(core.__file__).resolve()
    core_hash = file_sha256(core_path)
    require(
        core_hash == AUDITED_CORE_SHA256,
        f"audited core hash mismatch: {core_hash}",
    )

    core.ROOT_STEPS = args.root_steps
    core.set_precision(args.precision)

    script_path = Path(__file__).resolve()
    print("GENERAL-d SMALL-START FIRST-FLOOR CERTIFICATE")
    print(
        f"python-flint={core.flint.__version__}; "
        f"precision={ctx.prec} bits; root_steps={core.ROOT_STEPS}"
    )
    print(f"script_sha256={file_sha256(script_path)}")
    print(f"audited_core_sha256={core_hash}")
    print("All transcendental sign decisions use directed-rounding Arb.\n")

    ray = certify_ray_constants()
    print("PASS analytic ray x>=100")
    print(
        "  C_delta~{c_delta_mid:.12g}<731/250, "
        "K/x<={k_ratio:.12g}<6/5, "
        "ratio^2>={ratio_sq:.12g}>25/9".format(**ray)
    )

    totals = {
        "chambers": 0,
        "processed": 0,
        "leaves": 0,
        "roots": 0,
        "max_depth": 0,
        "min_midpoint": float("inf"),
    }
    by_s: dict[int, dict[str, object]] = {}
    split_chambers: list[str] = []

    for ch in chamber_list():
        result = core.verify_chamber(ch)
        totals["chambers"] += 1
        for key in ("processed", "leaves", "roots"):
            totals[key] += int(result[key])
        totals["max_depth"] = max(
            int(totals["max_depth"]), int(result["max_depth"])
        )
        totals["min_midpoint"] = min(
            float(totals["min_midpoint"]), float(result["min_midpoint"])
        )
        if int(result["max_depth"]) > 0:
            split_chambers.append(ch.label)

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
        row["max_depth"] = max(
            int(row["max_depth"]), int(result["max_depth"])
        )
        row["min_midpoint"] = min(
            float(row["min_midpoint"]), float(result["min_midpoint"])
        )

    require(int(totals["chambers"]) == 398, "finite coverage count changed")

    for s in (0, 1):
        row = by_s[s]
        print(f"\nPASS finite small starts, s={s}")
        print(
            "  chambers={chambers}, processed-panels={processed}, "
            "accepted-leaves={leaves}, isolated-roots={roots}, "
            "max-depth={max_depth}".format(**row)
        )
        print(
            "  smallest accepted interval midpoint "
            f"(diagnostic only) ~{float(row['min_midpoint']):.12g}"
        )

    print("\nSubdivided chambers:")
    for label in split_chambers:
        print(f"  {label}")

    print("\nCERTIFIED: both small starts are closed for all p>=0")
    print("  r in {1/2,1}, s in {0,1}, alpha in [0,1].")
    print(
        "  finite x<100: chambers={chambers}, "
        "processed-panels={processed}, accepted-leaves={leaves}, "
        "isolated-roots={roots}, max-depth={max_depth}".format(**totals)
    )
    print(
        "  smallest accepted interval midpoint "
        f"(diagnostic only) ~{float(totals['min_midpoint']):.12g}"
    )
    print("  analytic x>=100: A(r)>5/4, hence the wall certificate is positive.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ArithmeticError) as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
