#!/usr/bin/env python3
"""Directed/exact certificate for the provisional Round-08G extension.

This verifier is intentionally isolated from the frozen Round-08F proof and
verifier.  It pins both artifacts before importing the prior implementation.
It certifies only the high-floor first-drop ratio band
``23/25 <= rho <= 1847/2000``; it does not certify any residual wall below
``rho=23/25``.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

try:
    import flint
    from flint import arb, ctx, fmpq
except ImportError as exc:  # pragma: no cover
    raise SystemExit("python-flint is required") from exc


SCRIPT_DIR = Path(__file__).resolve().parent
PRIOR_VERIFIER = SCRIPT_DIR / "general_d_high_floor_signed_prefix_verify.py"
PRIOR_VERIFIER_SHA256 = (
    "066A64BE535AFE212B107928D7845E9BC27D210D144A9E99FDE16DCCDF5A866C"
)
PRIOR_PROOF = (
    SCRIPT_DIR.parent
    / "human"
    / "outbox"
    / "general-d-round-08f-signed-prefix-terminal.md"
)
PRIOR_PROOF_SHA256 = (
    "ABAFE9A9C0B57607CA0945313D0C0A7B1602D6067D84587F14C274898EF7D196"
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


actual_prior_verifier_hash = file_sha256(PRIOR_VERIFIER)
actual_prior_proof_hash = file_sha256(PRIOR_PROOF)
if actual_prior_verifier_hash != PRIOR_VERIFIER_SHA256:  # pragma: no cover
    raise SystemExit(
        "Round-08F verifier hash mismatch: "
        f"{actual_prior_verifier_hash} != {PRIOR_VERIFIER_SHA256}"
    )
if actual_prior_proof_hash != PRIOR_PROOF_SHA256:  # pragma: no cover
    raise SystemExit(
        "Round-08F proof hash mismatch: "
        f"{actual_prior_proof_hash} != {PRIOR_PROOF_SHA256}"
    )

import general_d_high_floor_signed_prefix_verify as prior  # noqa: E402


base = prior.base
ctx.prec = int(os.environ.get("GENERAL_D_ARB_PREC", "512"))
PI = arb.pi()
SQRT2 = arb(2).sqrt()

RHO_MIN = fmpq(23, 25)
RHO_MAX = fmpq(1847, 2000)
THETA_SQ_BAR = fmpq(163, 1000)
C_BAR = fmpq(641, 5000)
COMMON_PREFIX_CONSTANT = fmpq(123, 1000)
GAMMA_FLOOR = -fmpq(9, 100)
LAMBDA_FLOOR = fmpq(229, 875)
W_FLOOR = fmpq(229, 500)
LEVEL_DISTANCE_FACTOR = fmpq(29, 10)
KAPPA_FLOOR = fmpq(18, 25)
RETAINED_SCALE = fmpq(261, 125)
COEFFICIENT_FLOOR = fmpq(137, 100)
SERIES_Z_BAR = fmpq(174, 625)
SERIES_QUADRATIC_UPPER = fmpq(21, 1000)
SERIES_INTEGRATED_UPPER = fmpq(3, 500)
CAP_UPPER = fmpq(1, 6)
PANELS = 64
TERMINAL_PANELS = 256


def A(value: int | fmpq) -> arb:
    return arb(value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def correlated_quantities(rho: arb) -> tuple[arb, arb, arb, arb, arb, arb]:
    """Return theta, c, Phi, R=theta*rho/Phi, beta*R, and d."""
    theta = rho.acos()
    c = theta / PI
    sine = (1 - rho * rho).sqrt()
    phi = sine - theta * rho
    radial = theta * rho / phi
    gamma = (A(COMMON_PREFIX_CONSTANT) - c) * radial
    d = 1 - 2 * c
    return theta, c, phi, radial, gamma, d


def series_integral_lower(rho: arb, x: fmpq) -> arb:
    """Lower retained integral with V=(29/10)(18/25)x."""
    eps = 1 - rho
    v = A(RETAINED_SCALE * x)
    one_plus = 1 + rho * v

    result = A(fmpq(2, 3)) / rho * (
        base.odd_half_power(one_plus, 3) - 1
    )
    result += eps / (30 * rho) * (
        base.odd_half_power(one_plus, 5) - 1
    )
    result += (
        A(fmpq(3, 560))
        * eps
        * eps
        / rho
        * (base.odd_half_power(one_plus, 7) - 1)
    )
    result -= A(fmpq(2, 3)) * base.odd_half_power(v, 3)
    result -= eps / 30 * base.odd_half_power(v, 5)
    result -= (
        A(SERIES_INTEGRATED_UPPER)
        * eps
        * eps
        * base.odd_half_power(v, 7)
    )
    return result


def main() -> None:
    print("GENERAL-d HIGH-FLOOR CORRELATED-PREFIX CERTIFICATE (ROUND 08G)")
    print(f"python-flint={flint.__version__}; Arb precision={ctx.prec} bits")
    print(f"Round-08F verifier SHA256={actual_prior_verifier_hash}")
    print(f"Round-08F proof SHA256={actual_prior_proof_hash}")
    print("Exact rationals are used except for directed Arb signs.\n")

    rho0 = A(RHO_MIN)
    rho1 = A(RHO_MAX)
    theta0 = rho0.acos()
    theta1 = rho1.acos()
    require(theta0 * theta0 < A(THETA_SQ_BAR), "theta^2 <163/1000 failed")
    require(theta0 / PI < A(C_BAR), "c <641/5000 failed")
    require(
        theta1 / PI > A(COMMON_PREFIX_CONSTANT),
        "beta<0 on the full band failed",
    )
    print("PASS ratio endpoints: theta^2<163/1000, c<641/5000, beta<0")

    # The Round-08E/08F p=0 reduction gives q>=5/2 for a negative
    # candidate, hence the same strict cap.
    cap_endpoint = prior.prior.prior.g_radius(
        A(fmpq(7, 2)), A(fmpq(5, 2))
    )
    require(cap_endpoint < A(CAP_UPPER), "G_(7/2)(5/2)<1/6 failed")
    print("PASS inherited p=0 exclusion and G_(7/2)(5/2)<1/6 cap")

    # The exact lambda=Phi/(1-rho) is increasing with theta because its
    # derivative has numerator sin(theta)*(theta-sin(theta)).  Its minimum
    # is therefore the upper-rho endpoint.
    sine1 = (1 - rho1 * rho1).sqrt()
    phi1 = sine1 - theta1 * rho1
    lambda1 = phi1 / (1 - rho1)
    require(theta1 > sine1, "theta>sin(theta) failed")
    require(lambda1 > A(LAMBDA_FLOOR), "lambda>229/875 failed")
    require(
        fmpq(7, 4) * LAMBDA_FLOOR == W_FLOOR,
        "active W floor changed",
    )
    print("PASS active width: lambda>229/875 and W>229/500")

    # First certify the theta monotonicity of the correlated coefficient
    # gamma=beta*R_rho on 64 complete rational rho panels.
    gamma_prime_minimum = float("inf")
    gamma_prime_maximum = -float("inf")
    for panel in range(PANELS):
        lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, PANELS)
        hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, PANELS)
        rho = base.interval_ball(lo, hi)
        theta, c, phi, radial, _, _ = correlated_quantities(rho)
        sine = (1 - rho * rho).sqrt()
        radial_prime = (sine * rho - theta) / (phi * phi)
        gamma_prime = (
            -radial / PI
            + (A(COMMON_PREFIX_CONSTANT) - c) * radial_prime
        )
        require(gamma_prime < A(-fmpq(49, 10)), "gamma monotonicity failed")
        gamma_prime_minimum = min(
            gamma_prime_minimum, float(base.lower(gamma_prime))
        )
        gamma_prime_maximum = max(
            gamma_prime_maximum, float(gamma_prime.upper())
        )

    # Keep gamma correlated with c on each of 256 finer complete rational
    # rho panels.  The formulas below are the exact terminal ledgers after
    # cP>gamma*W-cd/2.  This replay is separate from the rational ledger
    # proof below.
    terminal_minima = {
        "b0-coefficient": float("inf"),
        "b0-ledger": float("inf"),
        "q0-derivative": float("inf"),
        "q0-ledger": float("inf"),
        "q1-upper": float("inf"),
        "q1-lower": float("inf"),
    }
    for panel in range(TERMINAL_PANELS):
        lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, TERMINAL_PANELS)
        hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, TERMINAL_PANELS)
        rho = base.interval_ball(lo, hi)
        _, c, phi, radial, gamma, d = correlated_quantities(rho)
        require(phi > 0, "Phi was not positive on a terminal panel")
        require(radial > 0, "R_rho was not positive on a terminal panel")
        require(
            A(COMMON_PREFIX_CONSTANT) - c < 0,
            "beta was not negative on a terminal panel",
        )

        b0_coefficient = A(fmpq(1, 2)) - c + gamma
        b0_ledger = (
            b0_coefficient
            + A(fmpq(3, 4)) * gamma
            - A(fmpq(7, 6)) * c
            - c * d / 2
        )
        q0_derivative = 2 * A(W_FLOOR) + gamma
        q0_ledger = A(W_FLOOR) ** 2 + gamma * A(W_FLOOR) - c * d / 2

        upper_width = A(fmpq(3, 4))
        lower_width = upper_width - c

        def q1_ledger(width: arb) -> arb:
            return (
                A(fmpq(3, 2)) * width
                - width * width
                - c
                + gamma * width
                - c * d / 2
            )

        values = {
            "b0-coefficient": b0_coefficient,
            "b0-ledger": b0_ledger,
            "q0-derivative": q0_derivative,
            "q0-ledger": q0_ledger,
            "q1-upper": q1_ledger(upper_width),
            "q1-lower": q1_ledger(lower_width),
        }
        for name, value in values.items():
            require(base.lower(value) > 0, f"terminal panel failed: {name}")
            terminal_minima[name] = min(
                terminal_minima[name], float(base.lower(value))
            )

    _, _, _, _, gamma0, _ = correlated_quantities(rho0)
    require(gamma0 > A(GAMMA_FLOOR), "gamma>-9/100 endpoint failed")

    # Independent exact rational lower ledgers following from
    # c<641/5000, gamma>-9/100, and W>229/500.
    rational_b0_coefficient = fmpq(1, 2) - C_BAR + GAMMA_FLOOR
    rational_q0_derivative = 2 * W_FLOOR + GAMMA_FLOOR
    rational_b0 = (
        fmpq(1, 2)
        - fmpq(8, 3) * C_BAR
        + C_BAR**2
        + fmpq(7, 4) * GAMMA_FLOOR
    )
    rational_q0 = (
        W_FLOOR**2
        + GAMMA_FLOOR * W_FLOOR
        - C_BAR / 2
        + C_BAR**2
    )
    rational_q1_upper = (
        fmpq(9, 16)
        - fmpq(3, 2) * C_BAR
        + C_BAR**2
        + fmpq(3, 4) * GAMMA_FLOOR
    )
    rational_q1_lower = (
        fmpq(9, 16)
        - fmpq(3, 2) * C_BAR
        + GAMMA_FLOOR * (fmpq(3, 4) - C_BAR)
    )
    require(rational_b0_coefficient == fmpq(1409, 5000), "B0 coefficient changed")
    require(rational_q0_derivative == fmpq(413, 500), "Q0 derivative changed")
    require(rational_b0 == fmpq(1280143, 75000000), "rational B0 ledger changed")
    require(rational_q0 == fmpq(3021981, 25000000), "rational Q0 ledger changed")
    require(
        rational_q1_upper == fmpq(7978381, 25000000),
        "rational Q1 upper ledger changed",
    )
    require(
        rational_q1_lower == fmpq(157119, 500000),
        "rational Q1 lower ledger changed",
    )
    require(
        min(rational_b0, rational_q0, rational_q1_upper, rational_q1_lower)
        > 0,
        "rational terminal ledger failed",
    )

    print(
        f"PASS exact correlated terminal ledgers on "
        f"{TERMINAL_PANELS} full panels:"
    )
    print(
        "  gamma-prime enclosure union="
        f"[{gamma_prime_minimum:.12g}, {gamma_prime_maximum:.12g}]"
    )
    print(
        "  endpoint gamma+9/100 lower bound="
        f"{float(base.lower(gamma0 - A(GAMMA_FLOOR))):.12g}"
    )
    for name, value in terminal_minima.items():
        print(f"  {name} minimum lower bound={value:.12g}")
    print(
        "  rational ledger floors: "
        f"{rational_b0}, {rational_q0}, "
        f"{rational_q1_upper}, {rational_q1_lower}"
    )

    # Prove kappa=Phi/(theta*rho*epsilon) is increasing with theta.  If
    # N=Phi and D=theta*rho*(1-rho), the displayed H is N'D-ND'.
    derivative_minimum = float("inf")
    for panel in range(PANELS):
        lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, PANELS)
        hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, PANELS)
        rho = base.interval_ball(lo, hi)
        theta, _, phi, _, _, _ = correlated_quantities(rho)
        sine = (1 - rho * rho).sqrt()
        eps = 1 - rho
        derivative_numerator = (
            theta * sine * theta * rho * eps
            - phi * (rho * eps + theta * sine * (2 * rho - 1))
        )
        require(
            base.lower(derivative_numerator) > 0,
            "kappa theta-monotonicity panel failed",
        )
        derivative_minimum = min(
            derivative_minimum, float(base.lower(derivative_numerator))
        )

    theta1, _, phi1, _, _, _ = correlated_quantities(rho1)
    kappa1 = phi1 / (theta1 * rho1 * (1 - rho1))
    require(kappa1 > A(KAPPA_FLOOR), "kappa>18/25 endpoint failed")
    print("PASS retained ratio: kappa is increasing in theta on 64 panels")
    print(
        "  derivative-numerator minimum lower bound="
        f"{derivative_minimum:.12g}"
    )
    print(
        "  endpoint kappa-18/25 lower bound="
        f"{float(base.lower(kappa1 - A(KAPPA_FLOOR))):.12g}"
    )

    # The Taylor quotient for C_rho is decreasing in t=theta^2.  The
    # exact logarithmic derivative reduction is positive here.
    tbar = THETA_SQ_BAR
    coefficient_monotonicity = 84 + 10 * tbar - tbar**2 / 2
    require(coefficient_monotonicity > 0, "C_rho quotient monotonicity failed")
    coefficient_numerator = A(fmpq(1, 2) - tbar / 24)
    coefficient_denominator = A(
        fmpq(1, 3) - tbar / 30 + tbar**2 / 840
    )
    coefficient_lower = (
        rho0
        * SQRT2
        * base.odd_half_power(coefficient_numerator, 3)
        / coefficient_denominator
    )
    require(
        coefficient_lower > A(COEFFICIENT_FLOOR),
        "C_rho>137/100 failed",
    )

    u_upper = (
        LEVEL_DISTANCE_FACTOR
        * fmpq(5, 9)
        * THETA_SQ_BAR
        / RHO_MIN
    )
    require(u_upper == fmpq(4727, 16560), "u0 upper changed")
    require(u_upper < fmpq(143, 500), "u0<143/500 failed")
    require(
        LEVEL_DISTANCE_FACTOR * KAPPA_FLOOR == RETAINED_SCALE,
        "retained scale changed",
    )

    eps_max = 1 - RHO_MIN
    v_max = RETAINED_SCALE * fmpq(5, 3)
    require(v_max == fmpq(87, 25), "retained V maximum changed")
    z_upper = eps_max * v_max
    require(z_upper == SERIES_Z_BAR, "subtracted series z upper changed")
    tail_upper = (
        fmpq(3, 160)
        + fmpq(5, 896) * SERIES_Z_BAR / (1 - SERIES_Z_BAR)
    )
    require(
        tail_upper == fmpq(21117, 1010240),
        "refined quadratic arccos tail changed",
    )
    require(tail_upper < SERIES_QUADRATIC_UPPER, "21/1000 tail ceiling failed")
    require(
        SERIES_QUADRATIC_UPPER * fmpq(2, 7)
        == SERIES_INTEGRATED_UPPER,
        "integrated arccos tail changed",
    )
    first_copy_z = eps_max * (1 + v_max)
    require(first_copy_z == fmpq(224, 625), "first-copy z changed")
    require(first_copy_z < 1, "positive arccos series left its domain")
    print("PASS improved level-distance constants:")
    print("  u0<4727/16560<143/500; kappa>18/25")
    print("  C_rho>137/100; retained V=(261/125)x")
    print("  z<=174/625; tail<21/1000; integrated=3/500")

    smallest = float("inf")
    smallest_integral = float("inf")
    for endpoint in (fmpq(1, 7), fmpq(5, 3)):
        for panel in range(PANELS):
            lo = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel, PANELS)
            hi = RHO_MIN + (RHO_MAX - RHO_MIN) * fmpq(panel + 1, PANELS)
            rho = base.interval_ball(lo, hi)
            integral = series_integral_lower(rho, endpoint)
            margin = A(COEFFICIENT_FLOOR) * integral - A(endpoint)
            require(base.lower(integral) > 0, "series integral was not positive")
            require(base.lower(margin) > 0, "level-distance endpoint failed")
            smallest_integral = min(
                smallest_integral, float(base.lower(integral))
            )
            smallest = min(smallest, float(base.lower(margin)))
    print(
        "PASS level-distance band: 128 directed endpoint panels; "
        f"minimum lower margin={smallest:.12g}"
    )
    print(f"  minimum retained-integral lower bound={smallest_integral:.12g}")

    require(
        fmpq(3, 1) - LEVEL_DISTANCE_FACTOR > 0,
        "L<3 changed",
    )
    require(
        (fmpq(3, 1) - LEVEL_DISTANCE_FACTOR) / 4
        - COMMON_PREFIX_CONSTANT
        < 0,
        "small-delta delta coefficient was not negative",
    )
    small_delta = (
        fmpq(5, 4)
        - fmpq(5, 16) * LEVEL_DISTANCE_FACTOR
        - fmpq(8, 3) * C_BAR
        + C_BAR**2
    )
    require(
        small_delta == fmpq(1373893, 75000000),
        "small-delta polynomial changed",
    )
    require(small_delta > 0, "small-delta ledger failed")
    print(f"PASS small-delta scalar ledger: c*S>{small_delta}")

    eta0 = base.g(rho0)
    require(eta0 > A(fmpq(1, 147)), "eta(rho0)>1/147 failed")
    require(base.g(A(fmpq(1, 2))) < A(fmpq(1, 9)), "eta upper failed")
    require(PI < A(fmpq(355, 113)), "pi upper bound failed")
    a_upper = fmpq(23) * fmpq(355, 113)
    require(a_upper == fmpq(8165, 113), "a upper changed")
    combined = a_upper + fmpq(13, 45)
    require(combined == fmpq(368894, 5085), "numerator sum changed")
    require(combined < 73, "fixed-ratio numerator bound failed")
    cutoff = 73 * 147**2
    require(cutoff == 1577457, "cutoff arithmetic changed")
    print("PASS improved fixed-ratio cutoff constants:")
    print("  eta>1/147, eta<1/9, a+2*eta*C_*<73")
    print(f"  K0(rho)<{cutoff}")

    require(2 * cutoff - 1 == 3154913, "2r range arithmetic failed")
    require(cutoff - 1 == 1577456, "n range arithmetic failed")
    f_upper = fmpq(cutoff, 3) + fmpq(1, 4)
    require(
        fmpq(525819) < f_upper < fmpq(525820),
        "f,B range arithmetic failed",
    )
    print("PASS conservative exact integer ranges")

    print("\nCERTIFIED: the high-floor first-drop scalar is positive on")
    print("23/25 <= rho <= 1847/2000; Round 08F covers larger rho.")
    print("Residual fixed-ratio walls with rho<23/25 are not certified.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"CERTIFICATE FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
