from fractions import Fraction as Q

from computations.round11_verify_ultrathin_bridge import (
    verify_clean_room_reserve,
    verify_global_ceiling,
    verify_positive_reserve,
    verify_radial_bridge_constants,
)


def test_round11_radial_bridge_constants() -> None:
    values = verify_radial_bridge_constants()
    assert values["epsilon_max"] == Q(1, 100)
    assert values["a_min"] == 125
    assert values["tau_margin"] > 0
    assert values["sawtooth_primitive_min"] == -Q(1, 32)
    assert values["sawtooth_primitive_max"] == Q(3, 32)
    assert values["radial_fractional_coefficient"] == Q(17, 8)
    assert values["radial_linear_coefficient"] == Q(11, 14)


def test_round11_positive_reserve() -> None:
    values = verify_positive_reserve()
    assert values["charged_coefficient"] == Q(1_087_507, 1_400_000)
    assert values["coefficient_margin"] > 0
    assert values["reserve"] == Q(61, 1_400)
    assert values["angular_count_margin"] > 0


def test_round11_clean_room_reserve() -> None:
    values = verify_clean_room_reserve()
    assert values["radial_lower"] == Q(66_847, 280_000)
    assert values["angular_upper"] == Q(8_383_501, 2_500_000_000)
    assert values["independent_margin"] == Q(
        4_119_252_993, 17_500_000_000
    )
    assert values["independent_margin"] > 0


def test_round11_global_ceiling() -> None:
    values = verify_global_ceiling()
    assert values["thin_rho_min"] == Q(99, 100)
    assert values["endpoint_expansion_factor"] == Q(625, 4)
    assert values["discharged_radius_width"] == Q(621, 62_500)
    assert values["global_ceiling"] == 6_000**2
    assert values["seam_threshold_max"] < values["global_ceiling"]
    assert values["round10_ratio"] > 105
    assert values["old_ratio"] > 954
