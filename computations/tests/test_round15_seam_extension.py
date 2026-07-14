from fractions import Fraction as Q

from computations.round15_verify_seam_extension import (
    verify_action_payments,
    verify_angular_displacement_localization,
    verify_central_endpoint,
    verify_complete_synthetic_path,
    verify_elementary_bounds,
    verify_kappa53_route_obstruction,
    verify_seven_zone_union,
)


def test_round15_elementary_pi_and_radical_bounds_are_exact():
    values = verify_elementary_bounds()
    assert values["pi_upper"] == Q(1_571, 500)
    assert values["pi_upper_gap"] == Q(
        2_736_890_694_763, 6_719_303_882_812_500
    )
    assert values["pi_lower"] == Q(333, 106)
    assert values["pi_lower_gap"] == Q(3_418_213, 41_563_593_750)
    assert values["sqrt2_lower"] == Q(140, 99)
    assert values["sqrt3_upper"] == Q(97, 56)


def test_round15_angular_displacement_and_localization_close():
    values = verify_angular_displacement_localization()
    assert values["angular_first"] == Q(1, 25)
    assert values["angular_second"] == Q(2, 405)
    assert values["d_lower"] == Q(5, 8)
    assert values["displacement_margin"] == Q(497, 4_050_000)
    assert values["localization"] == Q(241, 480)
    assert values["localization_margin"] == Q(1, 480)


def test_round15_complete_synthetic_path_has_strict_reserves():
    values = verify_complete_synthetic_path()
    assert values["d_s_d_p"] == Q(13, 5)
    assert values["d_s_d_r"] == -Q(8, 5)
    assert values["derivative_cap"] == Q(
        2_260_740_364_246, 708_624_500_625
    )
    assert values["derivative_margin"] == Q(
        6_858_037_754, 708_624_500_625
    )
    assert values["synthetic_slope_margin"] == Q(92, 15)
    assert values["endpoint_q"] == Q(10_093, 9_720)
    assert values["endpoint_qhat"] == Q(373, 48_600)
    assert values["endpoint_margin"] == Q(
        2_505_132_463_469, 2_616_573_970_125
    )


def test_round15_dangerous_and_safe_payments_cover_full_floor_loss():
    values = verify_action_payments()
    assert values["gain_coefficient"] == Q(280_000, 17_281)
    assert values["gain_minus_loss"] == Q(598_066, 51_843)
    assert values["interface_cap"] == Q(132, 175)
    assert values["dangerous_reserve"] == Q(80_132_733, 3_024_175)
    assert values["safe_reserve"] == Q(114_694_733, 3_024_175)


def test_round15_central_endpoint_is_strict_but_y294_proxy_fails():
    values = verify_central_endpoint()
    assert values["rho_seam"] == Q(5, 6)
    assert values["eta_lower"] == Q(1, 49)
    assert values["central_margin"] == Q(5_226, 1_225)
    assert values["central_ceiling"] == 295**2
    assert values["selected_294_proxy"] == -Q(307, 175)


def test_round15_kappa53_is_only_a_selected_route_obstruction():
    values = verify_kappa53_route_obstruction()
    assert values["kappa"] == 53
    assert values["radical_square_margin"] == Q(
        10_003_031, 1_123_600_000_000
    )
    assert values["selected_proxy_lower"] == Q(6_374_293, 15_900_000)
    assert values["localization_failure"] == Q(14_293, 15_900_000)


def test_round15_seven_zone_faces_and_reduction_are_exact():
    values = verify_seven_zone_union()
    assert values["zone_1_small_hole"] == 64
    assert values["zone_2_central"] == 87_025
    assert values["zone_3_new_seam"] == 3_456
    assert values["zone_4_round14"] == 3_200
    assert values["zone_5_round13"] == 9_600
    assert values["zone_6_constant24"] == 15_000
    assert values["zone_7_round10"] == 200_000
    assert values["round14_face_7_8"] == 2_048
    assert values["round13_face_9_10"] == 2_400
    assert values["round10_face_24_25"] == 12_500
    assert values["reduction_factor"] == Q(121, 80)
    assert values["reduction_reserve"] == Q(41, 80)
