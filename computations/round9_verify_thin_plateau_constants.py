"""Exact rational checks for the Round 9 optimized thin-plateau constant.

The analytic monotonicity and alternating-series arguments are documented in
the Round 9 proof.  This module independently verifies every finite rational
comparison in that constant ledger.  It uses no floating-point arithmetic.
"""

from __future__ import annotations

from fractions import Fraction


Q = Fraction
C_FALLBACK = 18
C_CLEAN_ROOM = Q(125, 8)


def verify_fallback_constants() -> dict[str, Fraction | int]:
    """Verify the exact C=18 ledger and return its decisive margins."""

    # Rational square-root bounds.
    assert 140**2 < 2 * 99**2
    assert 2 * 2**2 < 3**2

    # Machin's identity plus alternating arctangent bounds supplies a rational
    # upper bound for pi which is itself below 355/113.
    arctan_fifth_upper = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(5)
    )
    arctan_239th_lower = Q(1, 239) - Q(1, 3 * 239**3)
    machin_upper = 16 * arctan_fifth_upper - 4 * arctan_239th_lower
    pi_upper = Q(355, 113)
    machin_gap = pi_upper - machin_upper
    assert machin_gap == Q(45_167_474_711, 189_820_334_689_453_125)
    assert machin_gap > 0

    # Under K >= 18 epsilon^-2, epsilon <= 1/100, rho >= 99/100:
    # U/mu < first_term + (9/4) sqrt(pi/891).
    first_term = Q(1, 178_200)
    localization_target = Q(67, 500)
    square_root_majorant = Q(4, 9) * (localization_target - first_term)
    localization_square_margin = square_root_majorant**2 - pi_upper / 891
    assert square_root_majorant == Q(119_389, 2_004_750)
    assert localization_square_margin == Q(
        9_377_802_773, 454_149_549_562_500
    )
    assert localization_square_margin > 0
    assert first_term + Q(9, 4) * square_root_majorant == localization_target
    t_lower = 1 - localization_target
    assert t_lower == Q(433, 500)

    # The exact local-slope coefficient is below 1053/40.
    slope_coefficient_exact_upper = 2 * pi_upper**2 / t_lower**2
    slope_coefficient = Q(1_053, 40)
    slope_margin = slope_coefficient - slope_coefficient_exact_upper
    assert slope_coefficient_exact_upper == Q(63_012_500_000, 2_394_047_041)
    assert slope_margin == Q(431_534_173, 95_761_881_640)
    assert slope_margin > 0

    # For x=epsilon^-1/2 >= 10, the contradiction threshold is p >= Bx.
    shelf_constant = Q(53, 10)

    def shelf_polynomial(x: Q, s: Q) -> Q:
        return (
            s**2
            - Q(1_053, 320) * s
            - slope_coefficient * (x**2 + Q(1, 18))
        )

    assert shelf_polynomial(Q(10), Q(53)) == Q(203, 320)
    shelf_leading_margin = shelf_constant**2 - slope_coefficient
    assert shelf_leading_margin == Q(353, 200)
    derivative_at_ten = (
        2 * shelf_leading_margin * 10 - Q(1_053, 320) * shelf_constant
    )
    assert derivative_at_ten == Q(57_151, 3_200)
    assert derivative_at_ten > 0

    # The action gain exceeds the shelf by more than one at x >= 10.
    gain_coefficient_lower = Q(12) * Q(140, 99) / pi_upper
    assert gain_coefficient_lower == Q(12_656, 2_343)
    gain_minus_shelf = gain_coefficient_lower - shelf_constant
    assert gain_minus_shelf == Q(2_381, 23_430)
    integral_gap_at_endpoint = gain_minus_shelf * 10
    assert integral_gap_at_endpoint == Q(2_381, 2_343)
    assert integral_gap_at_endpoint > 1
    assert integral_gap_at_endpoint - 1 == Q(38, 2_343)
    interface_loss_upper = Q(8, 15) * Q(3, 2)
    assert interface_loss_upper == Q(4, 5)

    # Exact overlap of C epsilon^-2 and (8 epsilon^(5/2))^-1.
    sqrt_epsilon_new = Q(1, 8 * C_FALLBACK)
    epsilon_new = sqrt_epsilon_new**2
    high_at_overlap = Q(C_FALLBACK) / epsilon_new**2
    low_at_overlap = Q(1, 8) / sqrt_epsilon_new**5
    assert epsilon_new == Q(1, 20_736)
    assert high_at_overlap == low_at_overlap == 2**17 * 3**10
    assert epsilon_new > Q(1, 2**18)
    assert epsilon_new / Q(1, 2**18) == Q(1_024, 81)
    assert epsilon_new < Q(1, 100)
    assert high_at_overlap < 2**33

    return {
        "C": C_FALLBACK,
        "machin_gap": machin_gap,
        "localization_square_margin": localization_square_margin,
        "t_lower": t_lower,
        "slope_margin": slope_margin,
        "shelf_polynomial_at_endpoint": shelf_polynomial(Q(10), Q(53)),
        "gain_coefficient_lower": gain_coefficient_lower,
        "integral_gap_at_endpoint": integral_gap_at_endpoint,
        "interface_loss_upper": interface_loss_upper,
        "epsilon_new": epsilon_new,
        "high_at_overlap": high_at_overlap,
    }


def verify_clean_room_constants() -> dict[str, Fraction]:
    """Verify the independent clean-room C=125/8 constant ledger."""

    arctan_fifth_upper = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(5)
    )
    arctan_239th_lower = Q(1, 239) - Q(1, 3 * 239**3)
    machin_upper = 16 * arctan_fifth_upper - 4 * arctan_239th_lower
    pi_upper = Q(1_571, 500)
    assert machin_upper == Q(5_277_328_977_275_528, 1_679_825_970_703_125)
    machin_gap = pi_upper - machin_upper
    assert machin_gap == Q(2_736_890_694_763, 6_719_303_882_812_500)
    assert machin_gap > 0

    # The d>9/10 geometry is reduced to exact sine-series comparisons.
    sine_lower = Q(3, 40) - Q(1, 6_000)
    assert sine_lower == Q(449, 6_000)
    assert sine_lower > Q(71, 1_000)
    assert 2 * Q(71, 1_000) ** 2 > Q(1, 100)

    # Localization under kappa >= 125/8.
    first_term = Q(8, 1_237_500)
    localization_radicand = Q(352, 86_625)
    assert first_term < Q(1, 1_000)
    assert localization_radicand < Q(1, 225)
    q_upper = Q(1, 1_000) + Q(19, 135)
    assert q_upper < Q(1, 7)

    # Uniform derivative bound for H(P,r).
    derivative_upper = (
        2
        * Q(22, 7) ** 2
        * Q(76, 5_625)
        * (1 + Q(1, 7) + Q(2, 99))
        / (1 - Q(1, 7)) ** 3
    )
    assert derivative_upper == Q(673_816, 1_366_875)
    assert derivative_upper < Q(1, 2)

    # The no-drop endpoint is the worst scaled-loss geometry.
    shelf_loss = Q(361, 80)
    y_max = Q(1, 10)
    rho_min = Q(99, 100)
    q_coefficient = Q(125, 8)
    q_star_capital = 1 + (y_max**2 + y_max * shelf_loss) / q_coefficient
    q_star = y_max**2 / rho_min * (q_star_capital - 1)
    assert q_star_capital == Q(12_869, 12_500)
    assert q_star == Q(41, 137_500)
    endpoint_margin = (
        shelf_loss**2
        - 2 * Q(22, 7) ** 2 * q_star_capital / (1 - q_star) ** 2
    )
    assert endpoint_margin == Q(
        72_581_986_185_449, 5_925_464_687_161_600
    )
    assert endpoint_margin > 0

    # Action gain versus the complete uncompensated loss.
    assert 140**2 < 2 * 99**2
    assert 99**2 > 2 * 70**2
    gain_coefficient_lower = Q(2_187_500, 466_587)
    gain_minus_loss = gain_coefficient_lower - shelf_loss
    assert gain_minus_loss == Q(6_562_093, 37_326_960)
    compensation_lower = 10 * gain_minus_loss - 1
    assert compensation_lower == Q(2_829_397, 3_732_696)
    interface_loss_upper = Q(8, 15) * Q(99, 70)
    assert interface_loss_upper == Q(132, 175)
    final_margin = compensation_lower - interface_loss_upper
    assert final_margin == Q(2_428_603, 653_221_800)
    assert final_margin > 0

    # Exact overlap and the resulting thin residual ceiling.
    sqrt_epsilon_new = 1 / (8 * C_CLEAN_ROOM)
    epsilon_new = sqrt_epsilon_new**2
    high_at_overlap = C_CLEAN_ROOM / epsilon_new**2
    low_at_overlap = Q(1, 8) / sqrt_epsilon_new**5
    assert sqrt_epsilon_new == Q(1, 125)
    assert epsilon_new == Q(1, 15_625)
    assert high_at_overlap == low_at_overlap == Q(125**5, 8)
    assert epsilon_new > Q(1, 2**18)
    assert epsilon_new / Q(1, 2**18) == Q(262_144, 15_625)
    assert high_at_overlap < 2**32

    return {
        "C": C_CLEAN_ROOM,
        "machin_gap": machin_gap,
        "q_upper": q_upper,
        "derivative_upper": derivative_upper,
        "endpoint_margin": endpoint_margin,
        "gain_coefficient_lower": gain_coefficient_lower,
        "compensation_lower": compensation_lower,
        "interface_loss_upper": interface_loss_upper,
        "final_margin": final_margin,
        "epsilon_new": epsilon_new,
        "high_at_overlap": high_at_overlap,
    }


if __name__ == "__main__":
    for label, values in (
        ("fallback_c18", verify_fallback_constants()),
        ("clean_room_c125_over_8", verify_clean_room_constants()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
