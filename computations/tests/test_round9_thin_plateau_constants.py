from fractions import Fraction

from computations.round9_verify_thin_plateau_constants import (
    verify_clean_room_constants,
    verify_fallback_constants,
)


def test_round9_fallback_constant_ledger() -> None:
    values = verify_fallback_constants()

    assert values["C"] == 18
    assert values["t_lower"] == Fraction(433, 500)
    assert values["shelf_polynomial_at_endpoint"] > 0
    assert values["integral_gap_at_endpoint"] > 1
    assert values["epsilon_new"] == Fraction(1, 20_736)
    assert values["high_at_overlap"] < 2**33


def test_round9_clean_room_constant_ledger() -> None:
    values = verify_clean_room_constants()

    assert values["C"] == Fraction(125, 8)
    assert values["derivative_upper"] < Fraction(1, 2)
    assert values["endpoint_margin"] > 0
    assert values["final_margin"] > 0
    assert values["epsilon_new"] == Fraction(1, 15_625)
    assert values["high_at_overlap"] < 2**32
