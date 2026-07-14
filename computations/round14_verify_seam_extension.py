"""Exact finite ledger for the proposed Round 14 seam extension.

This module checks the rational endpoint comparisons proposed for

    0 < epsilon <= 1/8,   kappa = K epsilon**2 >= 32,

with the candidate loss cap B=14/3, together with the independent central
endpoint and prospective six-zone union.  The analytic shifted-tail
identities, monotonicity arguments, complete synthetic path, and branch
ownership belong to the proof artifacts.  No floating-point value is
decisive, and this ledger is not a Bessel-root certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 8)
RHO_MIN = Q(7, 8)
KAPPA_MIN = Q(32)
D_LOWER = Q(2, 3)
DISPLACEMENT_CAP = Q(17, 40)
LOSS_BOUND = Q(14, 3)
CENTRAL_SQRT_CEILING = 550


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
    """Verify the epsilon=1/8, kappa=32 incumbent constant chain."""

    machin_gap = verify_pi_upper()
    pi_upper = Q(1_571, 500)

    # cos(pi/6)=sqrt(3)/2<7/8, so d>2/3.
    d_cosine_margin = RHO_MIN**2 - Q(3, 4)
    assert d_cosine_margin == Q(1, 64)
    assert d_cosine_margin > 0
    shelf_factor = 1 + 1 / D_LOWER
    assert shelf_factor == Q(5, 2)

    # The shelf bound gives qhat<1/1792+(5/2)sqrt(pi/112).
    displacement_first = EPSILON_MAX**2 / (KAPPA_MIN * RHO_MIN)
    assert displacement_first == Q(1, 1_792)
    radical_upper = Q(67, 400)
    radical_margin = radical_upper**2 - pi_upper / 112
    assert radical_margin == Q(3, 1_120_000)
    assert radical_margin > 0
    displacement_upper = displacement_first + shelf_factor * radical_upper
    assert displacement_upper == Q(3_757, 8_960)
    displacement_margin = DISPLACEMENT_CAP - displacement_upper
    assert displacement_margin == Q(51, 8_960)
    assert displacement_margin > 0

    # Hence x0/K>rho(1-qhat)>161/320=1/2+1/320.
    localization = RHO_MIN * (1 - DISPLACEMENT_CAP)
    assert localization == Q(161, 320)
    localization_margin = localization - Q(1, 2)
    assert localization_margin == Q(1, 320)
    assert localization_margin > 0

    # Complete fixed-r=B synthetic path.
    y_upper = Q(99, 280)
    y_upper_margin = y_upper**2 - EPSILON_MAX
    assert y_upper_margin == Q(1, 78_400)
    assert y_upper_margin > 0
    d_q_d_p = y_upper / KAPPA_MIN * shelf_factor
    assert d_q_d_p == Q(99, 3_584)
    scaled_a = EPSILON_MAX / RHO_MIN
    assert scaled_a == Q(1, 7)
    derivative_cap = (
        2
        * pi_upper**2
        * d_q_d_p
        * (1 + DISPLACEMENT_CAP + 2 * scaled_a)
        / (1 - DISPLACEMENT_CAP) ** 3
    )
    assert derivative_cap == Q(117_036_972_261, 23_847_320_000)
    derivative_margin = Q(5) - derivative_cap
    assert derivative_margin == Q(2_199_627_739, 23_847_320_000)
    assert derivative_margin > 0
    synthetic_slope_margin = 2 * LOSS_BOUND - 5
    assert synthetic_slope_margin == Q(13, 3)
    assert synthetic_slope_margin > 0

    # At P=r=B one has S=B.
    endpoint_q = (
        1
        + EPSILON_MAX / KAPPA_MIN
        + y_upper * LOSS_BOUND / KAPPA_MIN
    )
    assert endpoint_q == Q(1_351, 1_280)
    endpoint_qhat = scaled_a * (endpoint_q - 1)
    assert endpoint_qhat == Q(71, 8_960)
    endpoint_margin = (
        LOSS_BOUND**2
        - 2 * pi_upper**2 * endpoint_q / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(49_714_811_804, 82_306_584_375)
    assert endpoint_margin > 0

    # Action gain and both R branches.
    sqrt2_lower = Q(140, 99)
    sqrt2_margin = 2 - sqrt2_lower**2
    assert sqrt2_margin == Q(2, 9_801)
    assert sqrt2_margin > 0
    gain_coefficient = Q(4_480_000, 466_587)
    assert gain_coefficient == (
        2 * sqrt2_lower * KAPPA_MIN / (3 * pi_upper)
    )
    gain_minus_loss = gain_coefficient - LOSS_BOUND
    assert gain_minus_loss == Q(2_302_594, 466_587)
    assert gain_minus_loss > 0

    inverse_y_lower = Q(280, 99)
    interface_cap = Q(132, 175)
    dangerous_payment = inverse_y_lower * gain_minus_loss - 1
    assert dangerous_payment == Q(598_534_207, 46_192_113)
    payment_margin = dangerous_payment - interface_cap
    assert payment_margin == Q(98_646_127_309, 8_083_619_775)
    assert payment_margin > 0

    safe_payment = inverse_y_lower * gain_coefficient - 1
    assert safe_payment == Q(1_208_207_887, 46_192_113)
    safe_payment_margin = safe_payment - interface_cap
    assert safe_payment_margin == Q(205_339_021_309, 8_083_619_775)
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
        "y_upper_margin": y_upper_margin,
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


def verify_kappa24_route_obstruction() -> dict[str, Q]:
    """Verify only the current kappa=24 localization obstruction.

    A lower bound below one half is not a counterexample to the theorem.
    """

    pi_upper = Q(1_571, 500)
    kappa = Q(24)
    displacement_first = EPSILON_MAX**2 / (kappa * RHO_MIN)
    assert displacement_first == Q(1, 1_344)
    radical_upper = Q(31, 160)
    radical_margin = radical_upper**2 - pi_upper / 84
    assert radical_margin == Q(361, 2_688_000)
    assert radical_margin > 0
    displacement_upper = displacement_first + Q(5, 2) * radical_upper
    assert displacement_upper == Q(163, 336)
    localization = RHO_MIN * (1 - displacement_upper)
    assert localization == Q(173, 384)
    half_shortfall = Q(1, 2) - localization
    assert half_shortfall == Q(19, 384)
    assert half_shortfall > 0
    return {
        "kappa": kappa,
        "radical_margin": radical_margin,
        "displacement_upper": displacement_upper,
        "localization_lower_bound": localization,
        "half_shortfall": half_shortfall,
    }


def verify_clean_room_path() -> dict[str, Q]:
    """Verify the isolated reconstruction's distinct comparison path."""

    # Its direct proxy uses sqrt(22)<47/10 and a coarser rational shelf.
    assert Q(47, 10) ** 2 - 22 == Q(9, 100)
    displacement_upper = Q(47, 112) + Q(1, 1_792)
    assert displacement_upper == Q(753, 1_792)
    displacement_margin = DISPLACEMENT_CAP - displacement_upper
    assert displacement_margin == Q(43, 8_960)
    assert displacement_margin > 0

    # Its preliminary quadratic comparison forces P<9.
    coarse_constant = 2 * Q(484, 49) * Q(40, 23) ** 2
    assert coarse_constant == Q(1_548_800, 25_921)
    g_at_nine = 9**2 - coarse_constant * (
        Q(257, 256) + Q(15, 512) * 9
    )
    assert g_at_nine == Q(136_376, 25_921)
    assert g_at_nine > 0
    g_prime_at_nine = 18 - coarse_constant * Q(15, 512)
    assert g_prime_at_nine == Q(421_203, 25_921)
    assert g_prime_at_nine > 0

    # The alternative path Sbar(P)=5P/2-7 starts positively at B=14/3.
    endpoint_margin = (
        Q(196, 9) * Q(1_777, 1_792) ** 2
        - 2 * Q(484, 49) * Q(271, 256)
    )
    assert endpoint_margin == Q(3_627_793, 7_225_344)
    assert endpoint_margin > 0
    path_derivative_margin = (
        2 * Q(14, 3) * Q(31, 32) * Q(119, 128)
        - 5 * Q(484, 49) * Q(3, 256)
    )
    assert path_derivative_margin == Q(1_178_207, 150_528)
    assert path_derivative_margin > 0

    # Its coarser action payment avoids Machin's sharper constants.
    dangerous_payment_margin = Q(3_449, 275) - Q(4, 5)
    assert dangerous_payment_margin == Q(3_229, 275)
    assert dangerous_payment_margin > 0
    safe_payment_margin = Q(21_127, 825) - Q(4, 5)
    assert safe_payment_margin == Q(20_467, 825)
    assert safe_payment_margin > 0

    return {
        "displacement_upper": displacement_upper,
        "displacement_margin": displacement_margin,
        "coarse_constant": coarse_constant,
        "g_at_nine": g_at_nine,
        "g_prime_at_nine": g_prime_at_nine,
        "endpoint_margin": endpoint_margin,
        "path_derivative_margin": path_derivative_margin,
        "dangerous_payment_margin": dangerous_payment_margin,
        "safe_payment_margin": safe_payment_margin,
    }


def verify_central_endpoint() -> dict[str, Q]:
    """Verify K_0(7/8)<550^2 with exact rational comparisons."""

    verify_pi_upper()

    # a=14*pi<14*(22/7)=44<7^2.
    a_upper = 14 * Q(22, 7)
    assert a_upper == 44
    a_margin = Q(7**2) - a_upper
    assert a_margin == 5
    assert a_margin > 0

    # eta>=1/(24*pi)>1/76.
    action_denominator_upper = 24 * Q(22, 7)
    assert action_denominator_upper == Q(528, 7)
    action_denominator_margin = 76 - action_denominator_upper
    assert action_denominator_margin == Q(4, 7)
    assert action_denominator_margin > 0
    eta_lower = Q(1, 76)

    # C0=1+8sqrt(2)/15<307/175.
    c0_upper = Q(307, 175)
    assert 1 + 8 * Q(99, 70) / 15 == c0_upper

    y = CENTRAL_SQRT_CEILING
    central_margin = eta_lower * y**2 - 7 * y - c0_upper
    assert central_margin == Q(427_292, 3_325)
    assert central_margin > 0
    central_ceiling = Q(y**2)
    assert central_ceiling == 302_500

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
    """Verify the six finite ceilings and Round 13 reduction factor."""

    central_ceiling = Q(CENTRAL_SQRT_CEILING**2)
    new_seam_ceiling = KAPPA_MIN / Q(1, 10) ** 2
    round13_seam_ceiling = Q(24) / Q(1, 20) ** 2
    round12_seam_ceiling = Q(24) / Q(1, 25) ** 2
    round10_seam_ceiling = Q(20) / Q(1, 100) ** 2

    assert new_seam_ceiling == 3_200
    assert round13_seam_ceiling == 9_600
    assert round12_seam_ceiling == 15_000
    assert round10_seam_ceiling == 200_000
    assert 64 < new_seam_ceiling
    assert new_seam_ceiling < round13_seam_ceiling
    assert round13_seam_ceiling < round12_seam_ceiling
    assert round12_seam_ceiling < round10_seam_ceiling
    assert round10_seam_ceiling < central_ceiling

    seam_face_threshold = KAPPA_MIN / Q(1, 8) ** 2
    round13_face_threshold = Q(24) / Q(1, 10) ** 2
    round10_face_threshold = Q(20) / Q(1, 25) ** 2
    assert seam_face_threshold == 2_048
    assert round13_face_threshold == 2_400
    assert round10_face_threshold == 12_500

    central_minus_round10 = central_ceiling - round10_seam_ceiling
    central_minus_round12 = central_ceiling - round12_seam_ceiling
    central_minus_round13 = central_ceiling - round13_seam_ceiling
    central_minus_new = central_ceiling - new_seam_ceiling
    assert central_minus_round10 == 102_500
    assert central_minus_round12 == 287_500
    assert central_minus_round13 == 292_900
    assert central_minus_new == 299_300

    reduction_factor = Q(900**2, CENTRAL_SQRT_CEILING**2)
    assert reduction_factor == Q(324, 121)
    assert reduction_factor > 2

    return {
        "small_hole_residual_ceiling": Q(64),
        "new_seam_ceiling": new_seam_ceiling,
        "round13_seam_ceiling": round13_seam_ceiling,
        "round12_seam_ceiling": round12_seam_ceiling,
        "round10_seam_ceiling": round10_seam_ceiling,
        "seam_face_threshold": seam_face_threshold,
        "round13_face_threshold": round13_face_threshold,
        "round10_face_threshold": round10_face_threshold,
        "central_ceiling": central_ceiling,
        "central_minus_round10": central_minus_round10,
        "central_minus_round12": central_minus_round12,
        "central_minus_round13": central_minus_round13,
        "central_minus_new": central_minus_new,
        "reduction_factor": reduction_factor,
    }


if __name__ == "__main__":
    for label, values in (
        ("local_plateau", verify_local_plateau()),
        ("kappa24_route_obstruction", verify_kappa24_route_obstruction()),
        ("clean_room_path", verify_clean_room_path()),
        ("central_endpoint", verify_central_endpoint()),
        ("closed_union", verify_closed_union()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
