#!/usr/bin/env python3
"""Arb replay for the Round 9 f=1 no-drop small-s constants.

This script checks only the explicit constant ledger in
``human/outbox/general-d-round-09-no-drop-f1-small-s.md``.  The functional
inequalities in that note are analytic; no sampled decimal is a proof input.
"""

from __future__ import annotations

import argparse

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required for this Arb replay") from exc


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=384)
    args = parser.parse_args()
    if args.precision < 128:
        raise SystemExit("precision must be at least 128 bits")
    ctx.prec = args.precision

    pi = arb.pi()
    root2 = arb(2).sqrt()

    require(pi > arb(3), "pi>3")
    require(pi < arb(fmpq(22, 7)), "pi<22/7")
    require(root2 > arb(fmpq(7, 5)), "sqrt(2)>7/5")
    require(root2 < arb(fmpq(99, 70)), "sqrt(2)<99/70")
    require(root2 < arb(fmpq(3, 2)), "sqrt(2)<3/2")

    c = fmpq(293, 300)
    w_min = fmpq(277, 400)
    y_min = c * w_min
    require(y_min == fmpq(81161, 120000), "exact y_min")
    require(y_min > fmpq(27, 40), "y_min>27/40")

    t = fmpq(81, 160)
    u = (1 - t * t) ** 2 / (4 * t * t)
    require(u == fmpq(362483521, 671846400), "exact u(81/160)")
    require(fmpq(27, 50) - u == fmpq(62707, 134369280), "u gap")

    c0 = 2 * root2 / (3 * pi)
    require(c0 > arb(fmpq(49, 165)), "c0>49/165")
    kappa_cap = fmpq(300, 293) * fmpq(165, 49)
    require(kappa_cap == fmpq(49500, 14357), "kappa cap")
    x_cap = kappa_cap * fmpq(27, 50)
    require(x_cap == fmpq(26730, 14357), "negative-head length cap")
    require(x_cap < 3, "negative-head cap lies below X=3")

    head_cost = x_cap * fmpq(13, 40)
    require(head_cost == fmpq(34749, 57428), "head cost")

    # The cubed 9/10 angle comparison is reduced in the note to this
    # rational chain using pi>3 and sqrt(2)<99/70.
    angle_left = 9 * w_min
    angle_right = fmpq(2187, 500) * fmpq(99, 70)
    require(angle_left == fmpq(2493, 400), "angle left endpoint")
    require(angle_right == fmpq(216513, 35000), "angle right endpoint")
    require(angle_left - angle_right == fmpq(3249, 70000), "angle margin")
    require(
        pi * pi * arb(w_min) > arb(fmpq(2187, 500)) * root2,
        "direct Arb angle comparison",
    )

    terminal_noncorner = fmpq(9, 10) - fmpq(1, 10) - fmpq(1, 25)
    require(terminal_noncorner == fmpq(19, 25), "noncorner terminal")
    noncorner_margin = terminal_noncorner - head_cost
    require(
        noncorner_margin == fmpq(222407, 1435700),
        "noncorner scalar margin",
    )
    require(noncorner_margin > 0, "positive noncorner scalar margin")

    # beta/s < 10/7 at the corner follows after squaring from this exact
    # comparison.
    require(fmpq(400, 199) < fmpq(100, 49), "corner beta comparison")
    terminal_corner = fmpq(189, 160)
    corner_margin = terminal_corner - head_cost
    require(corner_margin == fmpq(1323513, 2297120), "corner scalar margin")
    require(corner_margin > 0, "positive corner scalar margin")

    n = 61
    dbar = (fmpq(3, 2) + fmpq(1, 4 * n)) / (
        fmpq(7, 22) - fmpq(1, 4 * n)
    )
    ubar = fmpq(32, 81) * dbar * dbar * (dbar + 1)
    require(dbar == fmpq(4037, 843), "central Dbar_61")
    require(
        ubar == fmpq(2544997143040, 48525245667),
        "central Ubar_61",
    )
    central_right = fmpq(3, 4) * n * (n + 1)
    require(central_right == fmpq(5673, 2), "central right side")
    require(ubar * ubar < central_right, "central n=61 exclusion")

    require(fmpq(528, 7 * 755) < fmpq(1, 10), "outer n=755 enters small-s")
    require(1500 * fmpq(22, 7) == fmpq(33000, 7), "compact K cap")

    print("PASS: f=1 no-drop small-s constants certified with Arb")
    print(f"python-flint={flint.__version__}; precision={ctx.prec} bits")
    print(f"noncorner margin={noncorner_margin}")
    print(f"corner margin={corner_margin}")
    print("central n<=60; outer n<=754; K<33000/7")


if __name__ == "__main__":
    main()
