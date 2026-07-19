from fractions import Fraction as Q

from computations.round10_verify_seam_constants import (
    verify_local_plateau_extension,
    verify_seam_ceiling,
)


def test_round10_local_plateau_extension_constants() -> None:
    values = verify_local_plateau_extension()
    assert values["epsilon_max"] == Q(1, 25)
    assert values["kappa_min"] == 20
    assert values["loss_bound"] == Q(73, 16)
    assert values["endpoint_margin"] > 0
    assert values["payment_margin"] > 0
    assert values["old_ledger_obstruction"] > 0


def test_round10_seam_ceiling_constants() -> None:
    values = verify_seam_ceiling()
    assert values["central_ceiling"] == 6_000**2
    assert values["thin_ceiling"] == Q(125**5, 8)
    assert values["central_ceiling"] < values["thin_ceiling"] < 2**32
    assert values["factor_nine_margin"] > 0
    assert values["seam_width"] == Q(3, 100)
