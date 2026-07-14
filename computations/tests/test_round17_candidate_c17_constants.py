from fractions import Fraction
from pathlib import Path

from computations import round17_verify_candidate_c17_constants as ledger


def test_candidate_c17_constant_ledger_passes() -> None:
    result = ledger.run_audit()
    assert result["status"] == "PASS"
    assert result["first_mismatch"] is None
    assert result["check_count"] == 28
    assert result["authenticated_sha256"] == ledger.EXPECTED_HASHES


def test_two_weyl_margins_are_exactly_positive() -> None:
    checks = ledger.run_audit()["checks"]
    assert Fraction(checks["weyl_z_minus_one_lower"]) == Fraction(13, 6)
    assert Fraction(checks["weyl_k1_squared_margin"]) == Fraction(
        88584210264668, 53216631070729
    )
    assert Fraction(checks["weyl_k1_monotonic_coarse_margin"]) == 7


def test_residual_branch_and_B0_margins_are_positive() -> None:
    checks = ledger.run_audit()["checks"]
    names = (
        "low_branch_k2_square_margin",
        "middle_branch_square_margin",
        "seam_square_margin",
        "global_face_square_margin",
        "global_face_linear_margin",
        "B0_lower_margin",
        "B0_upper_square_margin",
    )
    assert all(Fraction(checks[name]) > 0 for name in names)
    assert checks["B0_all_closed_faces_contained"] is True
    assert checks["rho_HK_upper_below_rho_c"] is True


def test_first_method_obstruction_is_exactly_reproduced() -> None:
    checks = ledger.run_audit()["checks"]
    assert Fraction(checks["next_band_crude_count"]) == 9
    assert Fraction(checks["obstruction_squared_margin"]) == Fraction(
        2121156829, 50824368
    )


def test_independent_machin_enclosure_proves_used_pi_bounds() -> None:
    lower, upper = ledger.machin_pi_bounds()
    assert Fraction(333, 106) < lower < upper < Fraction(22, 7)


def test_ledger_source_does_not_open_round17_proofs_or_reviews() -> None:
    source = Path(ledger.__file__).read_text(encoding="utf-8")
    forbidden_paths = (
        "round_017/responses",
        "round_017/reviews",
        "round_017/certification",
        "analytic-incumbent",
        "clean-room.md",
    )
    assert all(path not in source for path in forbidden_paths)
    assert set(ledger._packet_paths()) == {"claim", "residual", "spectral"}
