"""Exact finite ledger for the proposed Round 15 seam extension.

This module checks the rational comparisons needed for

    0 < epsilon <= 1/6,   kappa = K epsilon**2 >= 54,

the complete fixed-r=B synthetic path with B=14/3, the independent
central endpoint K_0(5/6)<295**2, the selected-route obstructions at
kappa=53 and Y=294, and the prospective seven-zone union.  It uses only
standard-library exact arithmetic.  The symbolic shifted-tail argument
and branch ownership are recorded in the proof inventory; this ledger is
not a Bessel-root certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 6)
RHO_MIN = Q(5, 6)
KAPPA_MIN = Q(54)
D_LOWER = Q(5, 8)
SHELF_FACTOR = Q(13, 5)
DISPLACEMENT_CAP = Q(159, 400)
LOSS_BOUND = Q(14, 3)
CENTRAL_SQRT_CEILING = 295
GLOBAL_CEILING = 200_000


def verify_elementary_bounds() -> dict[str, Q]:
    """Prove the rational pi and radical bounds used by all ledgers."""

    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).  Alternating-series
    # truncations ending with a positive term are upper bounds, while
    # truncations ending with a negative term are lower bounds.
    arctan_fifth_upper = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(5)
    )
    arctan_239th_lower = Q(1, 239) - Q(1, 3 * 239**3)
    machin_upper = 16 * arctan_fifth_upper - 4 * arctan_239th_lower
    pi_upper = Q(1_571, 500)
    pi_upper_gap = pi_upper - machin_upper
    assert pi_upper_gap == Q(
        2_736_890_694_763, 6_719_303_882_812_500
    )
    assert pi_upper_gap > 0
    assert Q(22, 7) - pi_upper == Q(3, 3_500)

    arctan_fifth_lower = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(4)
    )
    arctan_239th_upper = Q(1, 239)
    machin_lower = 16 * arctan_fifth_lower - 4 * arctan_239th_upper
    pi_lower = Q(333, 106)
    pi_lower_gap = machin_lower - pi_lower
    assert pi_lower_gap == Q(3_418_213, 41_563_593_750)
    assert pi_lower_gap > 0

    sqrt2_lower = Q(140, 99)
    sqrt2_upper = Q(99, 70)
    sqrt3_upper = Q(97, 56)
    assert 2 - sqrt2_lower**2 == Q(2, 9_801)
    assert sqrt2_upper**2 - 2 == Q(1, 4_900)
    assert sqrt3_upper**2 - 3 == Q(1, 3_136)

    return {
        "machin_upper": machin_upper,
        "pi_upper": pi_upper,
        "pi_upper_gap": pi_upper_gap,
        "machin_lower": machin_lower,
        "pi_lower": pi_lower,
        "pi_lower_gap": pi_lower_gap,
        "sqrt2_lower": sqrt2_lower,
        "sqrt2_upper": sqrt2_upper,
        "sqrt3_upper": sqrt3_upper,
    }


def verify_angular_displacement_localization() -> dict[str, Q]:
    """Check d>5/8, the shelf proxy, qhat, and x0/K>1/2."""

    elementary = verify_elementary_bounds()
    pi_upper = elementary["pi_upper"]

    # sqrt(2)>7/5 makes 2-sqrt(2)<3/5, and sqrt(3/5)<7/9.
    angular_first = 2 - Q(7, 5) ** 2
    angular_second = Q(7, 9) ** 2 - Q(3, 5)
    assert angular_first == Q(1, 25)
    assert angular_second == Q(2, 405)
    assert angular_first > 0 and angular_second > 0

    # Since rho<=1, sqrt(2*pi*rho)<13/5 follows from this reserve.
    shelf_square_margin = SHELF_FACTOR**2 - 2 * pi_upper
    assert shelf_square_margin == Q(119, 250)
    assert shelf_square_margin > 0
    assert 1 + 1 / D_LOWER == SHELF_FACTOR

    displacement_first = EPSILON_MAX**2 / (KAPPA_MIN * RHO_MIN)
    assert displacement_first == Q(1, 1_620)
    radical_upper = Q(763, 5_000)
    radical_square = pi_upper / 135
    assert radical_square == Q(1_571, 67_500)
    radical_margin = radical_upper**2 - radical_square
    assert radical_margin == Q(8_563, 675_000_000)
    assert radical_margin > 0

    displacement_proxy = displacement_first + SHELF_FACTOR * radical_upper
    assert displacement_proxy == Q(804_689, 2_025_000)
    displacement_margin = DISPLACEMENT_CAP - displacement_proxy
    assert displacement_margin == Q(497, 4_050_000)
    assert displacement_margin > 0
    denominator_margin = 1 - DISPLACEMENT_CAP
    assert denominator_margin == Q(241, 400)
    assert denominator_margin > 0

    localization = RHO_MIN * denominator_margin
    assert localization == Q(241, 480)
    localization_margin = localization - Q(1, 2)
    assert localization_margin == Q(1, 480)
    assert localization_margin > 0

    return {
        "angular_first": angular_first,
        "angular_second": angular_second,
        "d_lower": D_LOWER,
        "shelf_factor": SHELF_FACTOR,
        "shelf_square_margin": shelf_square_margin,
        "displacement_first": displacement_first,
        "radical_upper": radical_upper,
        "radical_margin": radical_margin,
        "displacement_proxy": displacement_proxy,
        "displacement_margin": displacement_margin,
        "denominator_margin": denominator_margin,
        "localization": localization,
        "localization_margin": localization_margin,
    }


def verify_complete_synthetic_path() -> dict[str, Q]:
    """Check every finite cap used on the fixed-r=B path."""

    elementary = verify_elementary_bounds()
    pi_upper = elementary["pi_upper"]

    y_upper = Q(49, 120)
    y_upper_margin = y_upper**2 - EPSILON_MAX
    inverse_y_margin = 6 - Q(120, 49) ** 2
    assert y_upper_margin == Q(1, 14_400)
    assert inverse_y_margin == Q(6, 2_401)
    assert y_upper_margin > 0 and inverse_y_margin > 0

    a_upper = EPSILON_MAX / RHO_MIN
    assert a_upper == Q(1, 5)
    d_s_d_p = SHELF_FACTOR
    d_s_d_r = -Q(8, 5)
    assert d_s_d_p == Q(13, 5)
    assert d_s_d_r == -Q(8, 5)

    d_q_d_p = d_s_d_p * y_upper / KAPPA_MIN
    assert d_q_d_p == Q(637, 32_400)
    derivative_cap = (
        2
        * pi_upper**2
        * d_q_d_p
        * (1 + DISPLACEMENT_CAP + 2 * a_upper)
        / (1 - DISPLACEMENT_CAP) ** 3
    )
    assert derivative_cap == Q(
        2_260_740_364_246, 708_624_500_625
    )
    derivative_margin = Q(16, 5) - derivative_cap
    assert derivative_margin == Q(
        6_858_037_754, 708_624_500_625
    )
    assert derivative_margin > 0

    synthetic_slope_margin = 2 * LOSS_BOUND - Q(16, 5)
    assert synthetic_slope_margin == Q(92, 15)
    assert synthetic_slope_margin > 0

    # Initial point P=r=B: S_*=B.  The y-bound is strict, so these are
    # strict upper proxies even at epsilon=1/6 and kappa=54.
    endpoint_q = Q(10_093, 9_720)
    endpoint_qhat = Q(373, 48_600)
    assert endpoint_q - 1 == Q(373, 9_720)
    assert a_upper * (endpoint_q - 1) == endpoint_qhat
    assert 1 - endpoint_qhat > 0
    endpoint_margin = (
        LOSS_BOUND**2
        - 2 * pi_upper**2 * endpoint_q / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(
        2_505_132_463_469, 2_616_573_970_125
    )
    assert endpoint_margin > 0

    # These signs are the finite counterparts of the symbolic path
    # monotonicities: H increases with Q, Q_* decreases with r, and no
    # denominator can vanish anywhere on the shelf-controlled path.
    h_q_numerator_lower = 1
    h_q_numerator_upper = 1 + DISPLACEMENT_CAP + 2 * a_upper
    assert h_q_numerator_lower > 0
    assert h_q_numerator_upper == Q(719, 400)
    assert 1 - DISPLACEMENT_CAP == Q(241, 400)

    return {
        "y_upper": y_upper,
        "y_upper_margin": y_upper_margin,
        "inverse_y_margin": inverse_y_margin,
        "a_upper": a_upper,
        "d_s_d_p": d_s_d_p,
        "d_s_d_r": d_s_d_r,
        "d_q_d_p": d_q_d_p,
        "derivative_cap": derivative_cap,
        "derivative_margin": derivative_margin,
        "synthetic_slope_margin": synthetic_slope_margin,
        "endpoint_q": endpoint_q,
        "endpoint_qhat": endpoint_qhat,
        "endpoint_margin": endpoint_margin,
        "h_q_numerator_upper": h_q_numerator_upper,
    }


def verify_action_payments() -> dict[str, Q]:
    """Pay the complete floor loss in dangerous and safe R branches."""

    elementary = verify_elementary_bounds()
    pi_upper = elementary["pi_upper"]
    sqrt2_lower = elementary["sqrt2_lower"]
    sqrt2_upper = elementary["sqrt2_upper"]

    gain_coefficient = 2 * sqrt2_lower * KAPPA_MIN / (3 * pi_upper)
    assert gain_coefficient == Q(280_000, 17_281)
    gain_minus_loss = gain_coefficient - LOSS_BOUND
    assert gain_minus_loss == Q(598_066, 51_843)
    assert gain_minus_loss > 0

    inverse_y_lower = Q(120, 49)
    assert 6 - inverse_y_lower**2 == Q(6, 2_401)
    interface_cap = Q(8, 15) * sqrt2_upper
    assert interface_cap == Q(132, 175)

    dangerous_payment = gain_minus_loss * inverse_y_lower - 1
    dangerous_reserve = dangerous_payment - interface_cap
    assert dangerous_reserve == Q(80_132_733, 3_024_175)
    assert dangerous_reserve > 0

    safe_payment = gain_coefficient * inverse_y_lower - 1
    safe_reserve = safe_payment - interface_cap
    assert safe_reserve == Q(114_694_733, 3_024_175)
    assert safe_reserve > 0

    return {
        "gain_coefficient": gain_coefficient,
        "gain_minus_loss": gain_minus_loss,
        "inverse_y_lower": inverse_y_lower,
        "interface_cap": interface_cap,
        "dangerous_payment": dangerous_payment,
        "dangerous_reserve": dangerous_reserve,
        "safe_payment": safe_payment,
        "safe_reserve": safe_reserve,
    }


def verify_central_endpoint() -> dict[str, Q]:
    """Check the independent comparison K_0(5/6)<295**2."""

    elementary = verify_elementary_bounds()
    pi_upper = elementary["pi_upper"]
    sqrt2_upper = elementary["sqrt2_upper"]
    sqrt3_upper = elementary["sqrt3_upper"]

    a_upper = 10 * Q(22, 7)
    assert a_upper == Q(220, 7)
    a_margin = 36 - a_upper
    assert a_margin == Q(32, 7)
    assert a_margin > 0

    action_product_margin = 49 - 9 * pi_upper * sqrt3_upper
    assert action_product_margin == Q(517, 28_000)
    assert action_product_margin > 0
    eta_lower = Q(1, 49)

    c0_upper = 1 + Q(8, 15) * sqrt2_upper
    assert c0_upper == Q(307, 175)

    y = Q(CENTRAL_SQRT_CEILING)
    central_margin = eta_lower * y**2 - 6 * y - c0_upper
    assert central_margin == Q(5_226, 1_225)
    assert central_margin > 0
    central_ceiling = y**2
    assert central_ceiling == 87_025

    y294 = Q(294)
    selected_294_proxy = eta_lower * y294**2 - 6 * y294 - c0_upper
    assert selected_294_proxy == -Q(307, 175)
    assert selected_294_proxy < 0

    return {
        "rho_seam": RHO_MIN,
        "a_upper": a_upper,
        "a_margin": a_margin,
        "sqrt_a_upper": Q(6),
        "action_product_margin": action_product_margin,
        "eta_lower": eta_lower,
        "c0_upper": c0_upper,
        "central_sqrt_ceiling": y,
        "central_margin": central_margin,
        "central_ceiling": central_ceiling,
        "selected_294_proxy": selected_294_proxy,
    }


def verify_kappa53_route_obstruction() -> dict[str, Q]:
    """Verify only the selected kappa=53 localization obstruction."""

    elementary = verify_elementary_bounds()
    pi_lower = elementary["pi_lower"]

    radicand_lower = 2 * pi_lower / 265
    assert radicand_lower == Q(333, 14_045)
    radical_lower = Q(3_079, 20_000)
    radical_square_margin = radicand_lower - radical_lower**2
    assert radical_square_margin == Q(
        10_003_031, 1_123_600_000_000
    )
    assert radical_square_margin > 0

    selected_proxy_lower = Q(1, 1_590) + SHELF_FACTOR * radical_lower
    assert selected_proxy_lower == Q(6_374_293, 15_900_000)
    localization_failure = selected_proxy_lower - Q(2, 5)
    assert localization_failure == Q(14_293, 15_900_000)
    assert localization_failure > 0

    return {
        "kappa": Q(53),
        "pi_lower": pi_lower,
        "radicand_lower": radicand_lower,
        "radical_lower": radical_lower,
        "radical_square_margin": radical_square_margin,
        "selected_proxy_lower": selected_proxy_lower,
        "localization_failure": localization_failure,
    }


def verify_seven_zone_union() -> dict[str, Q]:
    """Check all seven coarse ceilings, shared faces, and reduction."""

    zone_1 = Q(64)
    zone_2 = Q(CENTRAL_SQRT_CEILING**2)
    zone_3 = KAPPA_MIN / Q(1, 8) ** 2
    zone_4 = Q(32) / Q(1, 10) ** 2
    zone_5 = Q(24) / Q(1, 20) ** 2
    zone_6 = Q(24) / Q(1, 25) ** 2
    zone_7 = Q(20) / Q(1, 100) ** 2
    ceilings = (zone_1, zone_2, zone_3, zone_4, zone_5, zone_6, zone_7)

    assert ceilings == (
        Q(64),
        Q(87_025),
        Q(3_456),
        Q(3_200),
        Q(9_600),
        Q(15_000),
        Q(200_000),
    )
    assert max(ceilings) == GLOBAL_CEILING
    assert all(value <= GLOBAL_CEILING for value in ceilings)

    new_face_5_6 = KAPPA_MIN / Q(1, 6) ** 2
    new_face_7_8 = KAPPA_MIN / Q(1, 8) ** 2
    round14_face_7_8 = Q(32) / Q(1, 8) ** 2
    round14_face_9_10 = Q(32) / Q(1, 10) ** 2
    round13_face_9_10 = Q(24) / Q(1, 10) ** 2
    face_19_20 = Q(24) / Q(1, 20) ** 2
    round13_face_24_25 = Q(24) / Q(1, 25) ** 2
    round10_face_24_25 = Q(20) / Q(1, 25) ** 2
    face_99_100 = Q(20) / Q(1, 100) ** 2

    assert new_face_5_6 == 1_944
    assert new_face_7_8 == 3_456
    assert round14_face_7_8 == 2_048
    assert round14_face_9_10 == 3_200
    assert round13_face_9_10 == 2_400
    assert face_19_20 == 9_600
    assert round13_face_24_25 == 15_000
    assert round10_face_24_25 == 12_500
    assert face_99_100 == 200_000
    assert round14_face_7_8 < new_face_7_8
    assert round13_face_9_10 < round14_face_9_10
    assert round10_face_24_25 < round13_face_24_25

    reduction_factor = Q(550**2, GLOBAL_CEILING)
    reduction_reserve = reduction_factor - 1
    assert reduction_factor == Q(121, 80)
    assert reduction_reserve == Q(41, 80)
    assert reduction_reserve > 0

    return {
        "zone_1_small_hole": zone_1,
        "zone_2_central": zone_2,
        "zone_3_new_seam": zone_3,
        "zone_4_round14": zone_4,
        "zone_5_round13": zone_5,
        "zone_6_constant24": zone_6,
        "zone_7_round10": zone_7,
        "global_ceiling": Q(GLOBAL_CEILING),
        "new_face_5_6": new_face_5_6,
        "new_face_7_8": new_face_7_8,
        "round14_face_7_8": round14_face_7_8,
        "round14_face_9_10": round14_face_9_10,
        "round13_face_9_10": round13_face_9_10,
        "face_19_20": face_19_20,
        "round13_face_24_25": round13_face_24_25,
        "round10_face_24_25": round10_face_24_25,
        "face_99_100": face_99_100,
        "reduction_factor": reduction_factor,
        "reduction_reserve": reduction_reserve,
    }


if __name__ == "__main__":
    for label, values in (
        ("elementary_bounds", verify_elementary_bounds()),
        (
            "angular_displacement_localization",
            verify_angular_displacement_localization(),
        ),
        ("complete_synthetic_path", verify_complete_synthetic_path()),
        ("action_payments", verify_action_payments()),
        ("central_endpoint", verify_central_endpoint()),
        ("kappa53_route_obstruction", verify_kappa53_route_obstruction()),
        ("seven_zone_union", verify_seven_zone_union()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
