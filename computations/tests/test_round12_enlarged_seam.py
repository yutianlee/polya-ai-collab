from fractions import Fraction as Q

from computations.round12_verify_enlarged_seam import (
    verify_central_endpoint,
    verify_clean_room_local_plateau,
    verify_enlarged_local_plateau,
    verify_incumbent_local_plateau,
)


def test_round12_enlarged_local_plateau_constants() -> None:
    values = verify_enlarged_local_plateau()
    assert values["epsilon_max"] == Q(1, 20)
    assert values["rho_min"] == Q(19, 20)
    assert values["kappa_min"] == 24
    assert values["d_lower"] == Q(3, 4)
    assert values["loss_bound"] == Q(23, 5)
    assert values["displacement_margin"] > 0
    assert values["localization"] > Q(1, 2)
    assert values["derivative_margin"] > 0
    assert values["synthetic_slope_margin"] > 0
    assert values["endpoint_margin"] > 0
    assert values["payment_margin"] > 0
    assert values["safe_payment_margin"] > 0


def test_round12_central_endpoint_constants() -> None:
    values = verify_central_endpoint()
    assert values["rho_seam"] == Q(19, 20)
    assert values["eta_lower"] == Q(14_000, 4_199_283)
    assert values["central_margin"] == Q(32_985_481, 7_422_975)
    assert values["central_margin"] > 0
    assert values["central_ceiling"] == 3_300**2
    assert values["seam_high_at_right"] < values["central_ceiling"]
    assert values["seam_width"] == Q(1, 25)


def test_round12_incumbent_local_plateau_constants() -> None:
    values = verify_incumbent_local_plateau()
    assert values["d_lower"] == Q(39, 50)
    assert values["displacement_margin"] > 0
    assert values["localization"] == Q(1_387, 2_000)
    assert values["derivative_margin"] > 0
    assert values["synthetic_slope_margin"] == Q(77, 10)
    assert values["endpoint_margin"] > 0
    assert values["payment_margin"] == Q(233, 25)
    assert values["safe_payment_margin"] == Q(739, 25)


def test_round12_clean_room_local_plateau_constants() -> None:
    values = verify_clean_room_local_plateau()
    assert values["loss_bound"] == 5
    assert values["localization_margin"] > 0
    assert values["p_cap_margin"] == Q(7, 18)
    assert values["q_margin"] > 0
    assert values["reciprocal_square_margin"] > 0
    assert values["endpoint_margin"] > 0
    assert values["payment_margin"] > 0
    assert values["safe_floor_margin"] == Q(1, 5)
