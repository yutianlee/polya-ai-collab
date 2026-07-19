"""Exact rational ledger for the Round 10 central--thin seam proof.

The analytic proof supplies the elementary trigonometric implications.  This
module checks every rational comparison used to turn those implications into
the explicit constants epsilon_0=1/25, C=20, B=73/16, and the global ceiling
125^5/8.  No floating-point value is decisive.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 25)
RHO_MIN = Q(24, 25)
KAPPA_MIN = Q(20)
LOSS_BOUND = Q(73, 16)
CENTRAL_SQRT_CEILING = 6_000
THIN_CEILING = Q(125**5, 8)


def verify_local_plateau_extension() -> dict[str, Q]:
    """Check the exact constants in the enlarged local-plateau proof."""

    # cos^2(pi/10)=(5+sqrt(5))/8<29/32<(24/25)^2 proves
    # d>4/5 on rho>=24/25.
    assert Q(9, 4) ** 2 > 5
    cosine_gap = RHO_MIN**2 - Q(29, 32)
    assert cosine_gap == Q(307, 20_000)
    assert cosine_gap > 0

    # The unconditional shelf estimate and d>4/5 give S<(9/4)P.
    # With pi<1571/500 and sqrt(1571/120000)<23/200, the
    # self-consistency displacement satisfies qhat<1553/6000<21/80.
    radical_margin = Q(23, 200) ** 2 - Q(1_571, 120_000)
    assert radical_margin == Q(1, 7_500)
    shelf_constant = 1 + 1 / Q(4, 5)
    assert shelf_constant == Q(9, 4)
    displacement_first = Q(1, 12_000)
    displacement_second = Q(207, 800)
    displacement_cap = Q(21, 80)
    displacement_margin = (
        displacement_cap - displacement_first - displacement_second
    )
    assert displacement_margin == Q(11, 3_000)
    assert displacement_margin > 0
    localization = RHO_MIN * (1 - displacement_cap)
    assert localization == Q(177, 250)
    assert localization > Q(1, 2)

    # Uniform derivative bound for H along the synthetic P-comparison path.
    d_q_d_p = Q(1, 5) / KAPPA_MIN * shelf_constant
    assert d_q_d_p == Q(9, 400)
    scaled_a = EPSILON_MAX / RHO_MIN
    assert scaled_a == Q(1, 24)
    derivative_cap = (
        2
        * Q(1_571, 500) ** 2
        * d_q_d_p
        * (1 + displacement_cap + 2 * scaled_a)
        / (1 - displacement_cap) ** 3
    )
    assert derivative_cap == Q(4_783_063_458, 3_209_046_875)
    assert derivative_cap < Q(3, 2)
    assert 2 * LOSS_BOUND > Q(3, 2)

    # Worst no-drop endpoint: y=1/5, kappa=20, P=r=B, hence S=B.
    endpoint_q = 1 + Q(1, 25) / KAPPA_MIN + Q(1, 5) * LOSS_BOUND / KAPPA_MIN
    assert endpoint_q == Q(8_381, 8_000)
    endpoint_qhat = scaled_a * (endpoint_q - 1)
    assert endpoint_qhat == Q(127, 64_000)
    endpoint_margin = (
        LOSS_BOUND**2
        - 2 * Q(1_571, 500) ** 2 * endpoint_q / (1 - endpoint_qhat) ** 2
    )
    assert endpoint_margin == Q(6_451_558_662_413, 130_552_324_128_000)
    assert endpoint_margin > 0

    # Gain payment.  The bounds sqrt(2)>140/99 and pi<1571/500 give
    # 2 sqrt(2) kappa/(3 pi) > 2800000/466587 at kappa>=20.
    assert 2 - Q(140, 99) ** 2 > 0
    assert Q(99, 70) ** 2 - 2 > 0
    gain_coefficient = Q(2_800_000, 466_587)
    assert gain_coefficient == (
        2 * Q(140, 99) * KAPPA_MIN / (3 * Q(1_571, 500))
    )
    dangerous_payment = 5 * (gain_coefficient - LOSS_BOUND) - 1
    assert dangerous_payment == Q(46_230_353, 7_465_392)
    interface_cap = Q(132, 175)
    payment_margin = dangerous_payment - interface_cap
    assert payment_margin == Q(7_104_880_031, 1_306_443_600)
    assert payment_margin > 0
    compensated_payment = 5 * gain_coefficient - 1
    assert compensated_payment == Q(13_533_413, 466_587)
    assert compensated_payment > 1

    # The unchanged Round 9 C=125/8, B=361/80 payment ledger already
    # becomes insufficient at epsilon=1/99.  This is a proof-ledger
    # obstruction, not a counterexample to the shell inequality.
    old_gain_minus_loss = Q(6_562_093, 37_326_960)
    old_ledger_obstruction = (
        Q(307, 175) ** 2 - 99 * old_gain_minus_loss**2
    )
    assert old_ledger_obstruction == Q(
        307_696_871_393_039, 17_240_352_323_040_000
    )
    assert old_ledger_obstruction > 0

    return {
        "epsilon_max": EPSILON_MAX,
        "rho_min": RHO_MIN,
        "kappa_min": KAPPA_MIN,
        "cosine_gap": cosine_gap,
        "displacement_margin": displacement_margin,
        "localization": localization,
        "derivative_cap": derivative_cap,
        "loss_bound": LOSS_BOUND,
        "endpoint_margin": endpoint_margin,
        "gain_coefficient": gain_coefficient,
        "dangerous_payment": dangerous_payment,
        "payment_margin": payment_margin,
        "old_ledger_obstruction": old_ledger_obstruction,
    }


def verify_seam_ceiling() -> dict[str, Q]:
    """Check the exact central endpoint and global-ceiling comparisons."""

    # At rho=24/25, a=48*pi<1056/7<13^2.
    a_upper = 48 * Q(22, 7)
    assert a_upper == Q(1_056, 7)
    assert a_upper < 13**2

    # eta>=2sqrt(2)/(375*pi)>1120/466587>1/420.
    eta_intermediate = 2 * Q(140, 99) / (375 * Q(1_571, 500))
    assert eta_intermediate == Q(1_120, 466_587)
    eta_lower = Q(1, 420)
    eta_margin = eta_intermediate - eta_lower
    assert eta_margin == Q(1_271, 65_322_180)
    assert eta_margin > 0

    # C0<307/175 follows from sqrt(2)<99/70.  Evaluate the defining
    # quadratic at Y=6000; positivity places its positive root below Y.
    assert Q(99, 70) ** 2 > 2
    y = CENTRAL_SQRT_CEILING
    central_margin = Q(y * y, 420) - 13 * y - Q(307, 175)
    assert central_margin == Q(1_349_693, 175)
    assert central_margin > 0
    central_ceiling = Q(y * y)
    assert central_ceiling == 36_000_000

    assert central_ceiling < THIN_CEILING
    central_to_thin_margin = THIN_CEILING - central_ceiling
    assert central_to_thin_margin == Q(30_229_578_125, 8)

    assert THIN_CEILING < 2**32
    thin_to_2_32_margin = Q(2**32) - THIN_CEILING
    assert thin_to_2_32_margin == Q(3_842_160_243, 8)
    assert Q(2**35) > 9 * THIN_CEILING
    factor_nine_margin = Q(2**35) - 9 * THIN_CEILING
    assert factor_nine_margin == Q(219_703_819, 8)
    old_to_new_drop = Q(2**35) - THIN_CEILING
    assert old_to_new_drop == Q(244_360_328_819, 8)

    seam_width = Q(99, 100) - RHO_MIN
    assert seam_width == Q(3, 100)
    seam_high_at_left = KAPPA_MIN / EPSILON_MAX**2
    seam_high_at_right = KAPPA_MIN / Q(1, 100) ** 2
    assert seam_high_at_left == 12_500
    assert seam_high_at_right == 200_000
    assert seam_high_at_right < THIN_CEILING

    return {
        "central_sqrt_ceiling": Q(y),
        "central_ceiling": central_ceiling,
        "eta_margin": eta_margin,
        "central_margin": central_margin,
        "thin_ceiling": THIN_CEILING,
        "central_to_thin_margin": central_to_thin_margin,
        "thin_to_2_32_margin": thin_to_2_32_margin,
        "factor_nine_margin": factor_nine_margin,
        "old_to_new_drop": old_to_new_drop,
        "seam_width": seam_width,
        "seam_high_at_left": seam_high_at_left,
        "seam_high_at_right": seam_high_at_right,
    }


if __name__ == "__main__":
    for label, values in (
        ("local_plateau_extension", verify_local_plateau_extension()),
        ("seam_ceiling", verify_seam_ceiling()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
