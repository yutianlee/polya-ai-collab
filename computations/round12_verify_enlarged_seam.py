"""Exact finite ledger for the proposed Round 12 enlarged seam.

This module checks the endpoint comparisons needed for

    0 < epsilon <= 1/20,   kappa = K epsilon**2 >= 24,

using the loss cap B=23/5.  It reproduces both the incumbent chain and the
distinct independent-inventory chain.  The analytic shifted-tail identities
and monotonicity arguments are documented in the accompanying proof
artifacts.  No floating-point value is decisive here.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 20)
RHO_MIN = Q(19, 20)
KAPPA_MIN = Q(24)
D_LOWER = Q(3, 4)
DISPLACEMENT_CAP = Q(11, 40)
LOSS_BOUND = Q(23, 5)
CENTRAL_SQRT_CEILING = 3_300


def _verify_pi_upper() -> Q:
    """Reproduce a rational proof that pi < 1571/500."""

    arctan_fifth_upper = sum(
        Q((-1) ** j, (2 * j + 1) * 5 ** (2 * j + 1)) for j in range(5)
    )
    arctan_239th_lower = Q(1, 239) - Q(1, 3 * 239**3)
    machin_upper = 16 * arctan_fifth_upper - 4 * arctan_239th_lower
    pi_upper = Q(1_571, 500)
    machin_gap = pi_upper - machin_upper
    assert machin_gap == Q(2_736_890_694_763, 6_719_303_882_812_500)
    assert machin_gap > 0
    assert pi_upper < Q(22, 7)
    return machin_gap


def verify_enlarged_local_plateau() -> dict[str, Q]:
    """Verify the independent epsilon=1/20, kappa=24 local ledger."""

    machin_gap = _verify_pi_upper()
    pi_upper = Q(1_571, 500)

    # cos^2(pi/8)=(2+sqrt(2))/4<7/8<(19/20)^2 proves d>3/4.
    assert Q(3, 2) ** 2 > 2
    cosine_gap = RHO_MIN**2 - Q(7, 8)
    assert cosine_gap == Q(11, 400)
    assert cosine_gap > 0
    shelf_factor = 1 + 1 / D_LOWER
    assert shelf_factor == Q(7, 3)

    # The unconditional shelf bound gives
    # qhat < 1/9120 + (7/3)sqrt(pi/228).
    radical_margin = Q(47, 400) ** 2 - Q(1_571, 114_000)
    assert radical_margin == Q(233, 9_120_000)
    assert radical_margin > 0
    displacement_first = Q(1, 9_120)
    displacement_second = shelf_factor * Q(47, 400)
    assert displacement_second == Q(329, 1_200)
    displacement_upper = displacement_first + displacement_second
    assert displacement_upper == Q(4_169, 15_200)
    displacement_margin = DISPLACEMENT_CAP - displacement_upper
    assert displacement_margin == Q(11, 15_200)
    assert displacement_margin > 0

    # Thus t>29/40 and x0/K=rho*t>551/800>1/2.
    localization = RHO_MIN * (1 - DISPLACEMENT_CAP)
    assert localization == Q(551, 800)
    assert localization > Q(1, 2)

    # y<=1/sqrt(20)<9/40.  This gives the full synthetic-path
    # derivative cap for H(P,r).
    y_rational_upper = Q(9, 40)
    assert y_rational_upper**2 - EPSILON_MAX == Q(1, 1_600)
    d_q_d_p = y_rational_upper / KAPPA_MIN * shelf_factor
    assert d_q_d_p == Q(7, 320)
    scaled_a = EPSILON_MAX / RHO_MIN
    assert scaled_a == Q(1, 19)
    derivative_cap = (
        2
        * pi_upper**2
        * d_q_d_p
        * (1 + DISPLACEMENT_CAP + 2 * scaled_a)
        / (1 - DISPLACEMENT_CAP) ** 3
    )
    assert derivative_cap == Q(18_122_825_063, 11_584_775_000)
    derivative_margin = Q(8, 5) - derivative_cap
    assert derivative_margin == Q(412_814_937, 11_584_775_000)
    assert derivative_margin > 0
    synthetic_slope_margin = 2 * LOSS_BOUND - Q(8, 5)
    assert synthetic_slope_margin == Q(38, 5)
    assert synthetic_slope_margin > 0

    # At P=r=B one has S=B.  Rationally majorize y by 9/40 in Q;
    # a=y^2/rho is at most 1/19.
    endpoint_q = (
        1
        + EPSILON_MAX / KAPPA_MIN
        + y_rational_upper * LOSS_BOUND / KAPPA_MIN
    )
    assert endpoint_q == Q(5_017, 4_800)
    endpoint_qhat = scaled_a * (endpoint_q - 1)
    assert endpoint_qhat == Q(217, 91_200)
    endpoint_margin = (
        LOSS_BOUND**2
        - 2 * pi_upper**2 * endpoint_q / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(
        2_196_261_729_217, 5_173_691_430_625
    )
    assert endpoint_margin > 0

    # Action gain.  The bounds sqrt(2)>140/99 and pi<1571/500 give
    # 2 sqrt(2) kappa/(3 pi)>1120000/155529 at kappa>=24.
    assert 2 - Q(140, 99) ** 2 == Q(2, 9_801)
    assert Q(99, 70) ** 2 - 2 == Q(1, 4_900)
    gain_coefficient = Q(1_120_000, 155_529)
    assert gain_coefficient == (
        2 * Q(140, 99) * KAPPA_MIN / (3 * pi_upper)
    )
    gain_minus_loss = gain_coefficient - LOSS_BOUND
    assert gain_minus_loss == Q(2_022_833, 777_645)
    assert gain_minus_loss > 0

    # At y<=1/sqrt(20), 1/y>=sqrt(20)>40/9.
    inverse_y_lower = Q(40, 9)
    inverse_y_square_margin = Q(20) - inverse_y_lower**2
    assert inverse_y_square_margin == Q(20, 81)
    assert inverse_y_square_margin > 0
    dangerous_payment = inverse_y_lower * gain_minus_loss - 1
    assert dangerous_payment == Q(14_782_903, 1_399_761)
    interface_cap = Q(132, 175)
    payment_margin = dangerous_payment - interface_cap
    assert payment_margin == Q(2_402_239_573, 244_958_175)
    assert payment_margin > 0

    safe_payment = inverse_y_lower * gain_coefficient - 1
    assert safe_payment == Q(43_400_239, 1_399_761)
    safe_payment_margin = safe_payment - interface_cap
    assert safe_payment_margin == Q(7_410_273_373, 244_958_175)
    assert safe_payment_margin > 0

    return {
        "epsilon_max": EPSILON_MAX,
        "rho_min": RHO_MIN,
        "kappa_min": KAPPA_MIN,
        "d_lower": D_LOWER,
        "loss_bound": LOSS_BOUND,
        "machin_gap": machin_gap,
        "cosine_gap": cosine_gap,
        "radical_margin": radical_margin,
        "displacement_upper": displacement_upper,
        "displacement_margin": displacement_margin,
        "localization": localization,
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


def verify_incumbent_local_plateau() -> dict[str, Q]:
    """Verify the incumbent's separate d>39/50 constant chain."""

    # The elementary pi lower bound used to turn 11*pi/100 into 33/100.
    pi_quarter_lower = Q(33_976, 45_045)
    pi_lower_margin = pi_quarter_lower - Q(3, 4)
    assert pi_lower_margin == Q(769, 180_180)
    assert pi_lower_margin > 0

    # At x=33/100, x^2/2-x^4/24>1/20.  Together with the
    # alternating cosine bound this gives d>39/50.
    d_cosine_margin = (
        Q(33, 100) ** 2 / 2
        - Q(33, 100) ** 4 / 24
        - Q(1, 20)
    )
    assert d_cosine_margin == Q(3_164_693, 800_000_000)
    assert d_cosine_margin > 0
    d_lower = Q(39, 50)
    shelf_factor = 1 + 1 / d_lower
    assert shelf_factor == Q(89, 39)

    assert Q(9, 40) ** 2 - EPSILON_MAX == Q(1, 1_600)
    assert Q(20) - Q(22, 5) ** 2 == Q(16, 25)

    # Incumbent displacement cap qhat<27/100.
    radical_margin = Q(47, 400) ** 2 - Q(11, 798)
    assert radical_margin == Q(1_391, 63_840_000)
    assert radical_margin > 0
    displacement_upper = Q(1, 9_120) + shelf_factor * Q(47, 400)
    assert displacement_upper == Q(159_019, 592_800)
    displacement_cap = Q(27, 100)
    displacement_margin = displacement_cap - displacement_upper
    assert displacement_margin == Q(1_037, 592_800)
    assert displacement_margin > 0
    localization = RHO_MIN * (1 - displacement_cap)
    assert localization == Q(1_387, 2_000)
    assert localization - Q(1, 2) == Q(387, 2_000)

    # Full fixed-r=B synthetic path.
    d_q_d_p = Q(89, 4_160)
    derivative_cap = (
        2
        * Q(22, 7) ** 2
        * d_q_d_p
        * (1 + displacement_cap + Q(2, 19))
        / (1 - displacement_cap) ** 3
    )
    assert derivative_cap == Q(541_142_250, 362_174_827)
    derivative_margin = Q(3, 2) - derivative_cap
    assert derivative_margin == Q(4_239_981, 724_349_654)
    assert derivative_margin > 0
    synthetic_slope_margin = 2 * LOSS_BOUND - Q(3, 2)
    assert synthetic_slope_margin == Q(77, 10)

    endpoint_q = Q(5_017, 4_800)
    endpoint_qhat = Q(217, 91_200)
    endpoint_margin = (
        LOSS_BOUND**2
        - 2
        * Q(22, 7) ** 2
        * endpoint_q
        / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(
        4_189_934_997_169, 10_140_435_204_025
    )
    assert endpoint_margin > 0

    # Incumbent gain and branch payments.
    gain_coefficient = Q(392, 55)
    inverse_y_lower = Q(22, 5)
    dangerous_payment = (
        gain_coefficient - LOSS_BOUND
    ) * inverse_y_lower - 1
    assert dangerous_payment == Q(253, 25)
    interface_cap = Q(4, 5)
    payment_margin = dangerous_payment - interface_cap
    assert payment_margin == Q(233, 25)
    safe_payment = gain_coefficient * inverse_y_lower - 1
    assert safe_payment == Q(759, 25)
    safe_payment_margin = safe_payment - interface_cap
    assert safe_payment_margin == Q(739, 25)

    return {
        "d_lower": d_lower,
        "pi_lower_margin": pi_lower_margin,
        "d_cosine_margin": d_cosine_margin,
        "shelf_factor": shelf_factor,
        "displacement_upper": displacement_upper,
        "displacement_margin": displacement_margin,
        "localization": localization,
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


def verify_clean_room_local_plateau() -> dict[str, Q]:
    """Verify the isolated clean-room review's B=5 rectangle chain."""

    # d>3/4 from cos^2(pi/8)<(19/20)^2.
    sqrt_two_upper = Q(161, 100)
    assert sqrt_two_upper**2 - 2 == Q(5_921, 10_000)
    cosine_square_upper = (2 + sqrt_two_upper) / 4
    assert cosine_square_upper == RHO_MIN**2 == Q(361, 400)

    # The coarse localization U/K<1/3+1/9600<9/20 gives x0/K>1/2.
    assert 60 > 7**2
    displacement_upper = Q(1, 3) + Q(1, 9_600)
    localization_margin = Q(9, 20) - displacement_upper
    assert localization_margin == Q(3_357, 28_800)
    assert localization_margin > 0

    # The global self-consistency estimate forces P<10.
    p_cap_margin = Q(10**2) - (Q(481, 6) + Q(35, 18) * 10)
    assert p_cap_margin == Q(7, 18)
    assert p_cap_margin > 0

    # On the full rectangle 5<=r<=P<10, Q-1<4/25 and qhat<4/475.
    q_minus_one_upper = Q(2_533, 15_840)
    q_margin = Q(4, 25) - q_minus_one_upper
    assert q_margin == Q(7, 79_200)
    assert q_margin > 0
    assert 40 * 475**2 < 41 * 471**2
    reciprocal_square_margin = Q(41, 40) - Q(475, 471) ** 2
    assert reciprocal_square_margin == Q(70_481, 8_873_640)
    assert reciprocal_square_margin > 0
    h_upper = 2 * Q(484, 49) * Q(29, 25) * Q(41, 40)
    assert h_upper == Q(1_150_952, 49_000)
    endpoint_margin = Q(5**2) - h_upper
    assert endpoint_margin == Q(74_048, 49_000)
    assert endpoint_margin > 0

    # Dangerous and safe branch compensation.
    gain_minus_loss = 16 * Q(7, 5) / Q(22, 7) - 5
    assert gain_minus_loss == Q(117, 55)
    dangerous_payment = 4 * gain_minus_loss - 1
    assert dangerous_payment == Q(413, 55)
    interface_upper = Q(16, 15)
    payment_margin = dangerous_payment - interface_upper
    assert payment_margin == Q(1_063, 165)
    assert payment_margin > 0
    safe_floor_margin = 1 - Q(4, 5)
    assert safe_floor_margin == Q(1, 5)

    return {
        "loss_bound": Q(5),
        "localization_margin": localization_margin,
        "p_cap_margin": p_cap_margin,
        "q_minus_one_upper": q_minus_one_upper,
        "q_margin": q_margin,
        "reciprocal_square_margin": reciprocal_square_margin,
        "h_upper": h_upper,
        "endpoint_margin": endpoint_margin,
        "gain_minus_loss": gain_minus_loss,
        "dangerous_payment": dangerous_payment,
        "payment_margin": payment_margin,
        "safe_floor_margin": safe_floor_margin,
    }


def verify_central_endpoint() -> dict[str, Q]:
    """Verify K_0(19/20)<3300^2 and the seam comparisons."""

    _verify_pi_upper()

    # At rho=19/20, a_rho=38*pi<38*(22/7)<11^2.
    a_upper = 38 * Q(22, 7)
    assert a_upper == Q(836, 7)
    a_margin = Q(11**2) - a_upper
    assert a_margin == Q(11, 7)
    assert a_margin > 0

    # eta>=2sqrt(2)/(3*pi)*epsilon^(3/2).  Use
    # sqrt(20)<9/2, sqrt(2)>140/99, and pi<1571/500.
    assert Q(9, 2) ** 2 - 20 == Q(1, 4)
    eta_lower = Q(14_000, 4_199_283)
    assert eta_lower == (
        2
        * Q(140, 99)
        / (3 * Q(1_571, 500) * 20 * Q(9, 2))
    )

    # C0=1+8sqrt(2)/15<307/175.
    c0_upper = Q(307, 175)
    assert 1 + 8 * Q(99, 70) / 15 == c0_upper

    y = CENTRAL_SQRT_CEILING
    central_margin = eta_lower * y**2 - 11 * y - c0_upper
    assert central_margin == Q(32_985_481, 7_422_975)
    assert central_margin > 0
    central_ceiling = Q(y**2)
    assert central_ceiling == 10_890_000

    # On 1/100<=epsilon<=1/20 the proposed high curve is no larger
    # than 24/(1/100)^2=240000, well below the central ceiling.
    seam_high_at_left = KAPPA_MIN / EPSILON_MAX**2
    seam_high_at_right = KAPPA_MIN / Q(1, 100) ** 2
    assert seam_high_at_left == 9_600
    assert seam_high_at_right == 240_000
    assert seam_high_at_right < central_ceiling
    seam_width = Q(99, 100) - RHO_MIN
    assert seam_width == Q(1, 25)

    return {
        "rho_seam": RHO_MIN,
        "a_upper": a_upper,
        "a_margin": a_margin,
        "eta_lower": eta_lower,
        "c0_upper": c0_upper,
        "central_sqrt_ceiling": Q(y),
        "central_margin": central_margin,
        "central_ceiling": central_ceiling,
        "seam_high_at_left": seam_high_at_left,
        "seam_high_at_right": seam_high_at_right,
        "seam_width": seam_width,
    }


if __name__ == "__main__":
    for label, values in (
        ("enlarged_local_plateau", verify_enlarged_local_plateau()),
        ("incumbent_local_plateau", verify_incumbent_local_plateau()),
        ("clean_room_local_plateau", verify_clean_room_local_plateau()),
        ("central_endpoint", verify_central_endpoint()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
