from fractions import Fraction as Q

from computations.round13_verify_seam_extension import (
    verify_central_endpoint,
    verify_clean_room_path,
    verify_closed_union,
    verify_local_plateau,
)


def test_round13_local_plateau_endpoint_margins_are_exactly_positive():
    values = verify_local_plateau()
    assert values["epsilon_max"] == Q(1, 10)
    assert values["d_lower"] == Q(2, 3)
    assert values["loss_bound"] == Q(14, 3)
    assert values["displacement_margin"] == Q(23, 37_800)
    assert values["localization_margin"] == Q(1, 70)
    assert values["endpoint_margin"] == Q(
        2_376_966_388_822, 5_818_105_805_625
    )


def test_round13_complete_synthetic_path_and_payment_close():
    values = verify_local_plateau()
    assert values["derivative_margin"] == Q(47_857_883, 270_000_000)
    assert values["synthetic_slope_margin"] == Q(10, 3)
    assert values["payment_margin"] == Q(170_244_091, 27_217_575)
    assert values["safe_payment_margin"] == Q(571_612_597, 27_217_575)


def test_round13_clean_room_path_is_independently_positive():
    values = verify_clean_room_path()
    assert values["screened_localization_reserve"] == Q(23, 16_800)
    assert values["displacement_margin"] == Q(23, 15_120)
    assert values["endpoint_f_margin"] == Q(12_760_228, 48_234_375)
    assert values["path_derivative_margin"] == Q(229, 2_646)
    assert values["payment_margin"] == Q(307, 55)


def test_round13_central_endpoint_quadratic_is_strict():
    values = verify_central_endpoint()
    assert values["rho_seam"] == Q(9, 10)
    assert values["eta_lower"] == Q(1, 107)
    assert values["central_margin"] == Q(6_897_151, 18_725)
    assert values["central_ceiling"] == 900**2


def test_round13_closed_union_is_below_the_new_central_ceiling():
    values = verify_closed_union()
    assert values["new_seam_ceiling"] == 9_600
    assert values["round12_seam_ceiling"] == 15_000
    assert values["round10_seam_ceiling"] == 200_000
    assert values["central_ceiling"] == 900**2
    assert values["reduction_factor"] == Q(121, 9)
