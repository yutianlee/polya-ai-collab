from fractions import Fraction as Q

from computations.round14_verify_seam_extension import (
    verify_central_endpoint,
    verify_clean_room_path,
    verify_closed_union,
    verify_kappa24_route_obstruction,
    verify_local_plateau,
)


def test_round14_local_plateau_endpoint_margins_are_exactly_positive():
    values = verify_local_plateau()
    assert values["epsilon_max"] == Q(1, 8)
    assert values["d_lower"] == Q(2, 3)
    assert values["loss_bound"] == Q(14, 3)
    assert values["displacement_margin"] == Q(51, 8_960)
    assert values["localization_margin"] == Q(1, 320)
    assert values["endpoint_margin"] == Q(49_714_811_804, 82_306_584_375)


def test_round14_complete_synthetic_path_and_payment_close():
    values = verify_local_plateau()
    assert values["derivative_margin"] == Q(2_199_627_739, 23_847_320_000)
    assert values["synthetic_slope_margin"] == Q(13, 3)
    assert values["payment_margin"] == Q(98_646_127_309, 8_083_619_775)
    assert values["safe_payment_margin"] == Q(205_339_021_309, 8_083_619_775)


def test_round14_kappa24_result_is_only_a_route_obstruction():
    values = verify_kappa24_route_obstruction()
    assert values["kappa"] == 24
    assert values["localization_lower_bound"] == Q(173, 384)
    assert values["half_shortfall"] == Q(19, 384)


def test_round14_clean_room_path_is_independently_positive():
    values = verify_clean_room_path()
    assert values["displacement_margin"] == Q(43, 8_960)
    assert values["g_at_nine"] == Q(136_376, 25_921)
    assert values["endpoint_margin"] == Q(3_627_793, 7_225_344)
    assert values["path_derivative_margin"] == Q(1_178_207, 150_528)
    assert values["dangerous_payment_margin"] == Q(3_229, 275)


def test_round14_central_endpoint_quadratic_is_strict():
    values = verify_central_endpoint()
    assert values["rho_seam"] == Q(7, 8)
    assert values["eta_lower"] == Q(1, 76)
    assert values["central_margin"] == Q(427_292, 3_325)
    assert values["central_ceiling"] == 550**2


def test_round14_closed_union_is_below_the_new_central_ceiling():
    values = verify_closed_union()
    assert values["new_seam_ceiling"] == 3_200
    assert values["round13_seam_ceiling"] == 9_600
    assert values["round12_seam_ceiling"] == 15_000
    assert values["round10_seam_ceiling"] == 200_000
    assert values["central_ceiling"] == 550**2
    assert values["reduction_factor"] == Q(324, 121)
