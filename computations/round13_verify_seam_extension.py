"""Exact finite ledger for the proposed Round 13 seam extension.

This module checks the endpoint comparisons needed for

    0 < epsilon <= 1/10,   kappa = K epsilon**2 >= 24,

using the incumbent candidate loss cap B=14/3. The analytic shifted-tail
identities and monotonicity arguments belong to the accompanying proof
artifacts. No floating-point value is decisive, and this ledger is not a
Bessel-root certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 10)
RHO_MIN = Q(9, 10)
KAPPA_MIN = Q(24)
D_LOWER = Q(2, 3)
DISPLACEMENT_CAP = Q(3, 7)
LOSS_BOUND = Q(14, 3)
CENTRAL_SQRT_CEILING = 900


def verify_pi_upper() -> Q:
    """Reproduce an exact Machin proof that pi < 1571/500."""

    arctan_fifth_upper = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(5)
    )
    arctan_239th_lower = Q(1, 239) - Q(1, 3 * 239**3)
    machin_upper = 16 * arctan_fifth_upper - 4 * arctan_239th_lower
    pi_upper = Q(1_571, 500)
    gap = pi_upper - machin_upper
    assert gap == Q(2_736_890_694_763, 6_719_303_882_812_500)
    assert gap > 0
    assert pi_upper < Q(22, 7)
    return gap


def verify_local_plateau() -> dict[str, Q]:
    """Verify the epsilon=1/10, kappa=24 incumbent constant chain."""

    machin_gap = verify_pi_upper()
    pi_upper = Q(1_571, 500)

    # cos(pi/6)=sqrt(3)/2<9/10, so d>2/3.
    d_cosine_margin = RHO_MIN**2 - Q(3, 4)
    assert d_cosine_margin == Q(3, 50)
    assert d_cosine_margin > 0
    shelf_factor = 1 + 1 / D_LOWER
    assert shelf_factor == Q(5, 2)

    # The shelf bound gives qhat<1/2160+(5/2)sqrt(pi/108).
    displacement_first = EPSILON_MAX**2 / (KAPPA_MIN * RHO_MIN)
    assert displacement_first == Q(1, 2_160)
    radical_upper = Q(171, 1_000)
    radical_margin = radical_upper**2 - pi_upper / 108
    assert radical_margin == Q(4_007, 27_000_000)
    assert radical_margin > 0
    displacement_upper = displacement_first + shelf_factor * radical_upper
    assert displacement_upper == Q(2_311, 5_400)
    displacement_margin = DISPLACEMENT_CAP - displacement_upper
    assert displacement_margin == Q(23, 37_800)
    assert displacement_margin > 0

    # Hence x0/K>rho(1-qhat)>18/35=1/2+1/70.
    localization = RHO_MIN * (1 - DISPLACEMENT_CAP)
    assert localization == Q(18, 35)
    localization_margin = localization - Q(1, 2)
    assert localization_margin == Q(1, 70)
    assert localization_margin > 0

    # Complete fixed-r=B synthetic path.
    y_upper = Q(8, 25)
    y_upper_margin = y_upper**2 - EPSILON_MAX
    assert y_upper_margin == Q(3, 1_250)
    assert y_upper_margin > 0
    d_q_d_p = y_upper / KAPPA_MIN * shelf_factor
    assert d_q_d_p == Q(1, 30)
    scaled_a = EPSILON_MAX / RHO_MIN
    assert scaled_a == Q(1, 9)
    derivative_cap = (
        2
        * pi_upper**2
        * d_q_d_p
        * (1 + DISPLACEMENT_CAP + 2 * scaled_a)
        / (1 - DISPLACEMENT_CAP) ** 3
    )
    assert derivative_cap == Q(1_572_142_117, 270_000_000)
    derivative_margin = Q(6) - derivative_cap
    assert derivative_margin == Q(47_857_883, 270_000_000)
    assert derivative_margin > 0
    synthetic_slope_margin = 2 * LOSS_BOUND - 6
    assert synthetic_slope_margin == Q(10, 3)
    assert synthetic_slope_margin > 0

    # At P=r=B one has S=B.
    endpoint_q = (
        1
        + EPSILON_MAX / KAPPA_MIN
        + y_upper * LOSS_BOUND / KAPPA_MIN
    )
    assert endpoint_q == Q(3_839, 3_600)
    endpoint_qhat = scaled_a * (endpoint_q - 1)
    assert endpoint_qhat == Q(239, 32_400)
    endpoint_margin = (
        LOSS_BOUND**2
        - 2 * pi_upper**2 * endpoint_q / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(
        2_376_966_388_822, 5_818_105_805_625
    )
    assert endpoint_margin > 0

    # Action gain and both R branches.
    assert 2 - Q(140, 99) ** 2 == Q(2, 9_801)
    assert Q(99, 70) ** 2 - 2 == Q(1, 4_900)
    gain_coefficient = Q(1_120_000, 155_529)
    assert gain_coefficient == (
        2 * Q(140, 99) * KAPPA_MIN / (3 * pi_upper)
    )
    gain_minus_loss = gain_coefficient - LOSS_BOUND
    assert gain_minus_loss == Q(394_198, 155_529)
    assert gain_minus_loss > 0

    inverse_y_lower = Q(79, 25)
    inverse_y_margin = Q(10) - inverse_y_lower**2
    assert inverse_y_margin == Q(9, 625)
    assert inverse_y_margin > 0
    interface_cap = Q(132, 175)

    dangerous_payment = inverse_y_lower * gain_minus_loss - 1
    assert dangerous_payment == Q(27_253_417, 3_888_225)
    payment_margin = dangerous_payment - interface_cap
    assert payment_margin == Q(170_244_091, 27_217_575)
    assert payment_margin > 0

    safe_payment = inverse_y_lower * gain_coefficient - 1
    assert safe_payment == Q(3_383_671, 155_529)
    safe_payment_margin = safe_payment - interface_cap
    assert safe_payment_margin == Q(571_612_597, 27_217_575)
    assert safe_payment_margin > 0

    return {
        "epsilon_max": EPSILON_MAX,
        "rho_min": RHO_MIN,
        "kappa_min": KAPPA_MIN,
        "d_lower": D_LOWER,
        "loss_bound": LOSS_BOUND,
        "machin_gap": machin_gap,
        "d_cosine_margin": d_cosine_margin,
        "radical_margin": radical_margin,
        "displacement_upper": displacement_upper,
        "displacement_margin": displacement_margin,
        "localization": localization,
        "localization_margin": localization_margin,
        "derivative_cap": derivative_cap,
        "derivative_margin": derivative_margin,
        "synthetic_slope_margin": synthetic_slope_margin,
        "endpoint_q": endpoint_q,
        "endpoint_qhat": endpoint_qhat,
        "endpoint_margin": endpoint_margin,
        "gain_coefficient": gain_coefficient,
        "dangerous_payment": dangerous_payment,
        "payment_margin": payment_margin,
        "safe_payment_margin": safe_payment_margin,
    }


def verify_clean_room_path() -> dict[str, Q]:
    """Verify the isolated reconstruction's distinct synthetic path."""

    # Its direct x0/K localization uses y^2*rho<=9/100.
    localization_radical_margin = Q(43, 280) ** 2 - Q(33, 1_400)
    assert localization_radical_margin == Q(1, 78_400)
    assert localization_radical_margin > 0
    localization = Q(9, 10) - Q(43, 112) - Q(1, 2_400)
    assert localization == Q(8_663, 16_800)
    screened_localization_reserve = localization - Q(18, 35)
    assert screened_localization_reserve == Q(23, 16_800)
    half_radius_reserve = localization - Q(1, 2)
    assert half_radius_reserve == Q(263, 16_800)

    # Its self-consistency displacement uses a different radical bound.
    displacement_radical_margin = Q(43, 252) ** 2 - Q(11, 378)
    assert displacement_radical_margin == Q(1, 63_504)
    assert displacement_radical_margin > 0
    displacement_upper = Q(1, 2_160) + Q(5, 2) * Q(43, 252)
    assert displacement_upper == Q(6_457, 15_120)
    displacement_margin = Q(3, 7) - displacement_upper
    assert displacement_margin == Q(23, 15_120)
    assert displacement_margin > 0

    # At B=14/3, the clean-room path uses L(X)=5X/2-7 and
    # F(X)=X^2(1-h_X)^2-2*pi^2*Q_X.
    endpoint_q_upper = Q(2_309, 2_160)
    endpoint_q_margin = Q(15, 14) - endpoint_q_upper
    assert endpoint_q_margin == Q(37, 15_120)
    assert endpoint_q_margin > 0
    endpoint_h_upper = Q(149, 19_440)
    endpoint_h_margin = Q(1, 125) - endpoint_h_upper
    assert endpoint_h_margin == Q(163, 486_000)
    assert endpoint_h_margin > 0
    endpoint_f_margin = (
        Q(196, 9) * Q(124, 125) ** 2
        - 2 * Q(22, 7) ** 2 * Q(15, 14)
    )
    assert endpoint_f_margin == Q(12_760_228, 48_234_375)
    assert endpoint_f_margin > 0

    x_h_prime_cap = Q(215, 504)
    path_derivative_margin = (
        2
        * Q(14, 3)
        * Q(4, 7)
        * (Q(4, 7) - x_h_prime_cap)
        - 5 * Q(22, 7) ** 2 / 72
    )
    assert path_derivative_margin == Q(229, 2_646)
    assert path_derivative_margin > 0

    # Its coarser branch payment avoids the sharper Machin constants.
    dangerous_payment = 3 * (Q(392, 55) - Q(14, 3)) - 1
    assert dangerous_payment == Q(351, 55)
    payment_margin = dangerous_payment - Q(4, 5)
    assert payment_margin == Q(307, 55)
    assert payment_margin > 0
    safe_floor_margin = 21 - Q(4, 5)
    assert safe_floor_margin == Q(101, 5)

    return {
        "localization_radical_margin": localization_radical_margin,
        "localization": localization,
        "screened_localization_reserve": screened_localization_reserve,
        "half_radius_reserve": half_radius_reserve,
        "displacement_radical_margin": displacement_radical_margin,
        "displacement_upper": displacement_upper,
        "displacement_margin": displacement_margin,
        "endpoint_q_margin": endpoint_q_margin,
        "endpoint_h_margin": endpoint_h_margin,
        "endpoint_f_margin": endpoint_f_margin,
        "x_h_prime_cap": x_h_prime_cap,
        "path_derivative_margin": path_derivative_margin,
        "dangerous_payment": dangerous_payment,
        "payment_margin": payment_margin,
        "safe_floor_margin": safe_floor_margin,
    }


def verify_central_endpoint() -> dict[str, Q]:
    """Verify K_0(9/10)<900^2 with exact rational comparisons."""

    verify_pi_upper()

    # a=18*pi<18*(22/7)<8^2.
    a_upper = 18 * Q(22, 7)
    assert a_upper == Q(396, 7)
    a_margin = Q(8**2) - a_upper
    assert a_margin == Q(52, 7)
    assert a_margin > 0

    # eta>=1/(15*pi*sqrt(5))>1/107.
    assert Q(9, 4) ** 2 - 5 == Q(1, 16)
    action_denominator_upper = 15 * Q(22, 7) * Q(9, 4)
    assert action_denominator_upper == Q(1_485, 14)
    action_denominator_margin = 107 - action_denominator_upper
    assert action_denominator_margin == Q(13, 14)
    assert action_denominator_margin > 0
    eta_lower = Q(1, 107)

    # C0=1+8sqrt(2)/15<307/175.
    c0_upper = Q(307, 175)
    assert 1 + 8 * Q(99, 70) / 15 == c0_upper

    y = CENTRAL_SQRT_CEILING
    central_margin = eta_lower * y**2 - 8 * y - c0_upper
    assert central_margin == Q(6_897_151, 18_725)
    assert central_margin > 0
    central_ceiling = Q(y**2)
    assert central_ceiling == 810_000

    return {
        "rho_seam": RHO_MIN,
        "a_upper": a_upper,
        "a_margin": a_margin,
        "eta_lower": eta_lower,
        "action_denominator_margin": action_denominator_margin,
        "c0_upper": c0_upper,
        "central_sqrt_ceiling": Q(y),
        "central_margin": central_margin,
        "central_ceiling": central_ceiling,
    }


def verify_closed_union() -> dict[str, Q]:
    """Verify the five finite ceilings and the Round 12 reduction factor."""

    central_ceiling = Q(CENTRAL_SQRT_CEILING**2)
    new_seam_ceiling = KAPPA_MIN / Q(1, 20) ** 2
    round12_seam_ceiling = KAPPA_MIN / Q(1, 25) ** 2
    round10_seam_ceiling = Q(20) / Q(1, 100) ** 2

    assert new_seam_ceiling == 9_600
    assert round12_seam_ceiling == 15_000
    assert round10_seam_ceiling == 200_000
    assert 64 < new_seam_ceiling
    assert new_seam_ceiling < round12_seam_ceiling
    assert round12_seam_ceiling < round10_seam_ceiling
    assert round10_seam_ceiling < central_ceiling

    central_minus_round10 = central_ceiling - round10_seam_ceiling
    central_minus_round12 = central_ceiling - round12_seam_ceiling
    central_minus_new = central_ceiling - new_seam_ceiling
    assert central_minus_round10 == 610_000
    assert central_minus_round12 == 795_000
    assert central_minus_new == 800_400

    reduction_factor = Q(3_300**2, CENTRAL_SQRT_CEILING**2)
    assert reduction_factor == Q(121, 9)
    assert reduction_factor > 13

    return {
        "small_hole_residual_ceiling": Q(64),
        "new_seam_ceiling": new_seam_ceiling,
        "round12_seam_ceiling": round12_seam_ceiling,
        "round10_seam_ceiling": round10_seam_ceiling,
        "central_ceiling": central_ceiling,
        "central_minus_round10": central_minus_round10,
        "central_minus_round12": central_minus_round12,
        "central_minus_new": central_minus_new,
        "reduction_factor": reduction_factor,
    }


if __name__ == "__main__":
    for label, values in (
        ("local_plateau", verify_local_plateau()),
        ("clean_room_path", verify_clean_room_path()),
        ("central_endpoint", verify_central_endpoint()),
        ("closed_union", verify_closed_union()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
