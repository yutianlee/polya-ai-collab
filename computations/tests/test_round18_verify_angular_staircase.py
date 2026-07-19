from fractions import Fraction
from pathlib import Path

from computations import round18_verify_angular_staircase as ledger


def _checks() -> dict[str, object]:
    return ledger.run_audit()["checks"]


def test_frozen_candidate_and_whitelist_authenticate() -> None:
    result = ledger.run_audit()
    assert result["status"] == "PASS"
    assert result["first_issue"] is None
    assert result["check_count"] == 40
    assert result["authenticated_sha256"] == ledger.EXPECTED_INPUT_HASHES
    assert set(ledger.input_paths()) == set(ledger.EXPECTED_INPUT_HASHES)


def test_radial_barrier_and_multiplicity_caps_are_exact() -> None:
    checks = _checks()
    assert Fraction(checks["radial_n2_gap_lower"]) == Fraction(27, 4)
    assert Fraction(checks["k6_squared_minus_k5_squared"]) == 12
    assert checks["multiplicity_caps_m1_through_m6"] == [1, 4, 9, 16, 25, 36]
    assert checks["k_squared_successive_gaps_m1_through_m6"] == [
        2,
        4,
        6,
        8,
        10,
        12,
    ]


def test_lorch_specializations_use_positive_exact_margins() -> None:
    checks = _checks()
    assert Fraction(checks["lorch_c2_square_margin"]) == Fraction(6, 25)
    assert Fraction(checks["lorch_c3_radical_square_margin"]) == Fraction(
        1121, 6561
    )
    assert Fraction(checks["lorch_c4_radical_square_margin"]) == Fraction(
        4331, 4356
    )
    assert checks["lorch_orders_in_scope"] is True
    assert checks["spherical_bessel_prefactor_positive_for_x_positive"] is True


def test_all_fixed_split_weyl_payments_match_the_exact_ledger() -> None:
    checks = _checks()
    assert Fraction(checks["split_m2_weyl_lower"]) == Fraction(
        100387329, 11000000
    )
    assert Fraction(checks["split_m2_cap_margin"]) == Fraction(
        1387329, 11000000
    )
    assert Fraction(checks["split_m3_weyl_lower"]) == Fraction(107653, 6336)
    assert Fraction(checks["split_m3_cap_margin"]) == Fraction(6277, 6336)
    assert Fraction(checks["split_m4_weyl_lower"]) == Fraction(18375, 704)
    assert Fraction(checks["split_m4_cap_margin"]) == Fraction(775, 704)


def test_split_walls_lie_strictly_above_the_ball_thresholds() -> None:
    checks = _checks()
    assert Fraction(checks["split_m2_k_square_gap"]) == Fraction(
        1802859, 13764100
    )
    assert Fraction(checks["split_m3_k_square_gap"]) == Fraction(103667, 11236)
    assert Fraction(checks["split_m4_k_square_gap"]) == Fraction(36251, 11236)
    assert Fraction(checks["c3_minus_c2"]) == Fraction(7, 5)
    assert Fraction(checks["c4_minus_c3"]) == 1


def test_base_payment_and_moving_wall_monotonicity_are_strict() -> None:
    checks = _checks()
    assert Fraction(checks["base_cap4_squared_margin"]) == Fraction(
        88584210264668, 53216631070729
    )
    assert Fraction(checks["F_m_monotonicity_bracket_gap_m1_through_m5"]) == (
        Fraction(57, 8)
    )
    assert checks["F_m_log_derivative_numerator_factor"] == 3


def test_candidate_stays_strictly_below_every_upper_face() -> None:
    checks = _checks()
    assert Fraction(checks["k5_below_26_square_margin"]) == Fraction(678, 49)
    assert Fraction(checks["low_K0_lower_minus_26"]) == 38
    assert Fraction(checks["high_K0_lower_minus_26"]) == 70
    assert Fraction(checks["seam_floor_at_five_sixths"]) == 1944
    assert Fraction(checks["seam_floor_minus_26"]) == 1918
    assert checks["global_face"] == 295**2
    assert checks["global_face_minus_26"] == 295**2 - 26


def test_face_ownership_and_subtraction_regressions() -> None:
    checks = _checks()
    assert checks["strict_k5_face_owned_by_C18"] is True
    assert checks["strict_k2_face_retains_C17_owner"] is True
    assert checks["rho_seven_eighths_retains_old_owner"] is True
    assert checks["B0_B1_not_subtracted_again"] is True
    assert checks["D18_second_lower_face_is_strict_k5"] is True


def test_independent_machin_enclosure_proves_both_pi_bounds() -> None:
    lower, upper = ledger.machin_pi_bounds()
    assert Fraction(333, 106) < lower < upper < Fraction(22, 7)


def test_ledger_reads_no_unlisted_round18_proof_or_review() -> None:
    source = Path(ledger.__file__).read_text(encoding="utf-8")
    forbidden = (
        "round_018/responses",
        "angular-staircase-incumbent",
        "lorch-source-audit.md",
        "clean-room",
        "adversarial-referee",
        "judge-018",
    )
    assert all(token not in source for token in forbidden)
    assert len(ledger.input_paths()) == 8


def test_manifest_covers_exactly_the_three_owned_outputs() -> None:
    manifest = ledger.artifact_manifest()
    assert set(manifest) == {"ledger", "tests", "review"}
    assert manifest["ledger"] is not None
    assert manifest["tests"] is not None

