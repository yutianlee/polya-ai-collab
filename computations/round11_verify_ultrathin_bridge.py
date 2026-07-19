"""Exact ledger for the Round 11 ultra-thin complementary-action bridge.

The analytic proof supplies the calculus, monotonicity, and
Riemann--Stieltjes arguments.  This module checks every finite rational or
integer comparison used to turn them into the explicit domain
epsilon <= 1/100, the reserve 61/1400, and the global ceiling 6000^2.
No floating-point value is decisive.
"""

from __future__ import annotations

from fractions import Fraction as Q


EPSILON_MAX = Q(1, 100)
A_MIN = Q(125)
THIN_RHO_MIN = Q(99, 100)
GLOBAL_CEILING = Q(6_000**2)
ROUND10_CEILING = Q(125**5, 8)


def verify_radial_bridge_constants() -> dict[str, Q]:
    """Check the finite constants in the direct shifted-layer proof."""

    # At epsilon=1/100 the threshold 1/(8 epsilon^(3/2)) is 125;
    # monotonicity makes this the smallest possible a in the domain.
    assert 100**3 == 1_000_000
    assert A_MIN == 1_000 // 8

    # Elementary radical and pi bounds used in tau>1.
    assert Q(7, 5) ** 2 < 2
    assert Q(22, 7) ** 2 < 10
    tau_coefficient = Q(7, 5) / (12 * Q(22, 7))
    assert tau_coefficient == Q(49, 1_320)
    tau_at_epsilon_max = tau_coefficient / EPSILON_MAX
    assert tau_at_epsilon_max == Q(245, 66)
    tau_margin = tau_at_epsilon_max - 1
    assert tau_margin == Q(179, 66)
    assert tau_margin > 0

    # The periodic primitive V of the centered radial sawtooth has these
    # exact extrema on a unit cell.
    v_min = Q(1, 2) * Q(1, 4) ** 2 - Q(1, 4) * Q(1, 4)
    v_max = Q(1, 2) * Q(3, 4) ** 2 - Q(1, 4) * Q(3, 4)
    assert v_min == -Q(1, 32)
    assert v_max == Q(3, 32)
    first_cell_negative_area = Q(1, 2) * Q(1, 4) ** 2
    assert first_cell_negative_area == Q(1, 32)
    assert first_cell_negative_area < Q(1, 16)

    # The g(3/4) coefficient is <4: the generic coefficient is <3
    # because its cube is 8*pi^2/3<80/3<27, and
    # (4/3)^(1/3)<4/3.
    assert Q(80, 3) < 27
    assert Q(4, 3) < Q(4, 3) ** 3
    g_three_quarters_coefficient = Q(4)

    # The F(1) loss coefficient is <7 because
    # (3*pi^2/2)^2 < (3*10/2)^2=225<7^3.
    assert 225 < 7**3
    f_one_coefficient = Q(7)

    # g(T)=2*pi*rho*a<44a/7.  Combining the three endpoint charges in
    # D >= F(1)/4 - 3g(3/4)/32 - g(T)/8 gives 17/8 and 11/14.
    g_terminal_coefficient = Q(44, 7)
    radial_fractional_coefficient = (
        f_one_coefficient / 4
        + Q(3, 32) * g_three_quarters_coefficient
    )
    radial_linear_coefficient = g_terminal_coefficient / 8
    assert radial_fractional_coefficient == Q(17, 8)
    assert radial_linear_coefficient == Q(11, 14)

    return {
        "epsilon_max": EPSILON_MAX,
        "a_min": A_MIN,
        "tau_coefficient": tau_coefficient,
        "tau_at_epsilon_max": tau_at_epsilon_max,
        "tau_margin": tau_margin,
        "sawtooth_primitive_min": v_min,
        "sawtooth_primitive_max": v_max,
        "first_cell_negative_area": first_cell_negative_area,
        "g_three_quarters_coefficient": g_three_quarters_coefficient,
        "f_one_coefficient": f_one_coefficient,
        "g_terminal_coefficient": g_terminal_coefficient,
        "radial_fractional_coefficient": radial_fractional_coefficient,
        "radial_linear_coefficient": radial_linear_coefficient,
    }


def verify_positive_reserve() -> dict[str, Q]:
    """Check the exact final reserve after angular ceiling errors."""

    # epsilon^(2/3)<1/20 follows at epsilon<=1/100 by cubing:
    # epsilon^2<=1/10000<1/8000=(1/20)^3.
    assert EPSILON_MAX**2 < Q(1, 20) ** 3

    # sqrt(epsilon)<=1/10 and epsilon^(5/2)<=1/100000 at the same face.
    assert EPSILON_MAX == Q(1, 10) ** 2
    assert EPSILON_MAX**2 * Q(1, 10) == Q(1, 100_000)

    charged_coefficient = (
        Q(17, 80) + Q(11, 35) + Q(1, 4) + Q(1, 200_000)
    )
    assert charged_coefficient == Q(1_087_507, 1_400_000)
    coarse_cap = Q(57, 7)
    coefficient_margin = coarse_cap - charged_coefficient
    assert coefficient_margin == Q(10_312_493, 1_400_000)
    assert coefficient_margin > 0

    reserve = Q(1, 8) - coarse_cap * EPSILON_MAX
    assert reserve == Q(61, 1_400)
    assert reserve > 0

    # At the threshold face the smallest a is 125, which is enough for
    # N<T+1/4<a/2 under pi>3.
    angular_count_margin = A_MIN / 2 - (A_MIN / 3 + Q(1, 4))
    assert angular_count_margin == Q(247, 12)
    assert angular_count_margin > 0

    return {
        "charged_coefficient": charged_coefficient,
        "coarse_cap": coarse_cap,
        "coefficient_margin": coefficient_margin,
        "reserve": reserve,
        "angular_count_margin": angular_count_margin,
    }


def verify_clean_room_reserve() -> dict[str, Q]:
    """Check the independent clean-room radial and angular reserves."""

    radial_lower = Q(99, 100) ** 2 / 4 - Q(11, 1_750)
    assert radial_lower == Q(66_847, 280_000)
    assert radial_lower > 0

    angular_upper = (
        Q(1, 300)
        + Q(1, 50_000)
        + Q(1, 15_000_000)
        + Q(1, 2_500_000_000)
    )
    assert angular_upper == Q(8_383_501, 2_500_000_000)

    independent_margin = radial_lower - angular_upper
    assert independent_margin == Q(4_119_252_993, 17_500_000_000)
    assert independent_margin > 0

    return {
        "radial_lower": radial_lower,
        "angular_upper": angular_upper,
        "independent_margin": independent_margin,
    }


def verify_global_ceiling() -> dict[str, Q]:
    """Check the new endpoint faces and all-ratio ceiling comparisons."""

    old_thin_epsilon = Q(1, 15_625)
    endpoint_expansion_factor = EPSILON_MAX / old_thin_epsilon
    assert endpoint_expansion_factor == Q(625, 4)

    old_thin_rho_min = 1 - old_thin_epsilon
    discharged_radius_width = old_thin_rho_min - THIN_RHO_MIN
    assert discharged_radius_width == Q(621, 62_500)
    assert discharged_radius_width > 0

    seam_threshold_max = Q(20) / EPSILON_MAX**2
    assert seam_threshold_max == 200_000
    assert seam_threshold_max < GLOBAL_CEILING

    round10_drop = ROUND10_CEILING - GLOBAL_CEILING
    assert round10_drop == Q(30_229_578_125, 8)
    round10_ratio = ROUND10_CEILING / GLOBAL_CEILING
    assert round10_ratio == Q(1_953_125, 18_432)
    assert round10_ratio > 105

    old_ceiling = Q(2**35)
    old_drop = old_ceiling - GLOBAL_CEILING
    assert old_drop == 34_323_738_368
    old_ratio = old_ceiling / GLOBAL_CEILING
    assert old_ratio == Q(134_217_728, 140_625)
    assert old_ratio > 954

    return {
        "thin_rho_min": THIN_RHO_MIN,
        "endpoint_expansion_factor": endpoint_expansion_factor,
        "discharged_radius_width": discharged_radius_width,
        "seam_threshold_max": seam_threshold_max,
        "global_ceiling": GLOBAL_CEILING,
        "round10_ceiling": ROUND10_CEILING,
        "round10_drop": round10_drop,
        "round10_ratio": round10_ratio,
        "old_ceiling": old_ceiling,
        "old_drop": old_drop,
        "old_ratio": old_ratio,
    }


if __name__ == "__main__":
    for label, values in (
        ("radial_bridge", verify_radial_bridge_constants()),
        ("positive_reserve", verify_positive_reserve()),
        ("clean_room_reserve", verify_clean_room_reserve()),
        ("global_ceiling", verify_global_ceiling()),
    ):
        print(f"[{label}]")
        for key, value in values.items():
            print(f"{key}={value}")
    print("PASS")
