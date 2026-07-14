"""Tests for the frozen exact post-Round-18 residual classifier."""

from fractions import Fraction as Q
import hashlib
from pathlib import Path

import pytest

from computations import round19_residual_mask as r19


ROOT = Path(__file__).resolve().parents[2]


def _dyadic_midpoint(builder) -> Q:
    """Return a greater-than-4096-bit dyadic approximation to a face."""

    old_precision = r19.r18.r17.ctx.prec
    try:
        r19.r18.r17.ctx.prec = 4096
        midpoint = builder().mid()
        mantissa, exponent = midpoint.man_exp()
        return Q(int(mantissa)) * Q(2) ** int(exponent)
    finally:
        r19.r18.r17.ctx.prec = old_precision


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


class TestManifest:
    def test_derivation_is_exactly_the_round18_union(self) -> None:
        manifest = r19._mask_manifest()
        assert manifest["derivation"] == {
            "base_classifier": "computations/round18_residual_mask.py",
            "operation": "A18=A17 union closed_round18_staircase",
            "residual_operation": "D18=D17 minus C18",
        }
        assert manifest["analytic_residual"]["rho_c_assignment"] == "post_band_piece"

    def test_exact_residual_and_theorem_uncovered_formula(self) -> None:
        manifest = r19._mask_manifest()
        residual = manifest["analytic_residual"]
        assert residual["lower_ratio_piece"] == (
            "rho_*<rho<rho_c and 1/(2rho)<K<U(rho)"
        )
        assert residual["post_band_piece"] == (
            "rho_c<=rho<7/8 and k5(rho)<K<U(rho)"
        )
        assert residual["all_frequency_faces"] == "strict"
        assert manifest["theorem_wise_uncovered"]["formula"] == "U18=D18"
        assert manifest["face_owners"]["K=295^2"] == (
            "Round 16 all-ratio high-frequency owner"
        )

    def test_upper_floor_and_all_active_interfaces_are_explicit(self) -> None:
        manifest = r19._mask_manifest()
        upper = manifest["upper_floor"]
        assert upper["piecewise"] == [
            "H0 on rho_*<rho<rho_HK",
            "K0 on rho_HK<=rho<5/6",
            "54/(1-rho)^2 on 5/6<=rho<7/8",
        ]
        interfaces = "\n".join(manifest["ratio_interfaces"])
        for token in (
            "rho=rho_*",
            "rho=rho_HK",
            "rho=omega0",
            "rho=rho_c",
            "rho=1/2",
            "rho=5/6",
            "rho=7/8",
        ):
            assert token in interfaces

    def test_certificates_are_regressions_not_subtractions(self) -> None:
        regressions = r19._mask_manifest()["certified_regressions"]
        assert regressions["B0"]["relation"] == "B0 subset C17 subset A18"
        assert regressions["B1"]["relation"] == "B1 subset C17 subset A18"
        assert regressions["uncovered_formula"] == (
            "U18=D18; neither box is subtracted again"
        )

    def test_method_walls_do_not_encode_a_global_order(self) -> None:
        method = r19._mask_manifest()["method_walls"]
        assert method["accepted_local_fact"] == "k5(rho_c)<2z_rho_c<k6(rho_c)"
        assert method["global_ordering_encoded"] is False
        assert method["crossing_threshold_encoded"] is False
        assert "do not change D18 membership" in method["classification_policy"]

    def test_authenticated_inputs_match_the_committed_bytes(self) -> None:
        inputs = r19._mask_manifest()["authenticated_inputs"]
        assert inputs["baseline_commit"] == "15e4d61db885bfff00a674fd7f37e4cffda70d0c"
        for relative_path, expected in inputs.items():
            if relative_path == "baseline_commit":
                continue
            assert len(expected) == 64
            assert _sha256(relative_path) == expected


class TestSymbolicFaceTruthTables:
    def test_closed_staircase_includes_every_equality_face(self) -> None:
        assert r19.closed_c18_membership_from_signs(
            0, 0, 0, rho_le_thin=True
        ) is True
        assert r19.closed_c18_membership_from_signs(
            1, 1, 1, rho_le_thin=False
        ) is False

    def test_genuine_c18_is_strict_at_k2_and_closed_at_k5(self) -> None:
        assert r19.new_c18_membership_from_signs(
            0, 0, 0, rho_lt_thin=True
        ) is False
        assert r19.new_c18_membership_from_signs(
            0, -1, 0, rho_lt_thin=True
        ) is True
        assert r19.new_c18_membership_from_signs(
            0, -1, 0, rho_lt_thin=False
        ) is False

    def test_false_factor_suppresses_irrelevant_unresolved_signs(self) -> None:
        assert r19.closed_c18_membership_from_signs(
            -1, None, None, rho_le_thin=True
        ) is False
        assert r19.d18_piece_from_signs(
            1, 1, -1, 1, None, rho_lt_thin=True
        ) is True

    def test_every_d18_frequency_boundary_is_strict(self) -> None:
        # rho=rho_*, K=U, K=1/(2rho), and K=k5 are all excluded.
        assert r19.d18_piece_from_signs(
            0, 1, -1, 1, 1, rho_lt_thin=True
        ) is False
        assert r19.d18_piece_from_signs(
            1, 0, -1, 1, 1, rho_lt_thin=True
        ) is False
        assert r19.d18_piece_from_signs(
            1, 1, -1, 0, 1, rho_lt_thin=True
        ) is False
        assert r19.d18_piece_from_signs(
            1, 1, 0, 1, 0, rho_lt_thin=True
        ) is False
        assert r19.d18_piece_from_signs(
            1, 1, 1, 1, -1, rho_lt_thin=False
        ) is False

    def test_rho_c_equality_uses_post_k5_piece(self) -> None:
        assert r19.d18_piece_from_signs(
            1, 1, 0, 1, -1, rho_lt_thin=True
        ) is True
        assert r19.d18_piece_from_signs(
            1, 1, 0, 1, 0, rho_lt_thin=True
        ) is False


class TestClassifierFaces:
    def test_exactly_two_residual_pieces(self) -> None:
        lower = r19.classify_point(Q(7, 51), Q(4))
        upper = r19.classify_point(Q(1, 2), Q(30))
        assert (lower.status, lower.residual_piece) == (
            "analytic_residual_uncovered",
            "lower-ratio",
        )
        assert (upper.status, upper.residual_piece) == (
            "analytic_residual_uncovered",
            "post-k5",
        )

    def test_promoted_staircase_and_old_k2_owner(self) -> None:
        staircase = r19.classify_point(Q(1, 2), Q(7))
        old = r19.classify_point(Q(1, 2), Q(67, 10))
        assert staircase.status == "analytic_covered"
        assert "angular-staircase-round18" in staircase.analytic_reasons
        assert old.status == "analytic_covered"
        assert "first-angular-band-round17" in old.analytic_reasons

    def test_thin_endpoint_owns_all_sampled_frequencies(self) -> None:
        for k in (Q(0), Q(1), Q(20), Q(1944), Q(87025)):
            result = r19.classify_point(Q(7, 8), k)
            assert result.status == "analytic_covered"
            assert "rho-one-endpoint-round16" in result.analytic_reasons

    def test_upper_floor_branches_and_inclusive_seam_owner(self) -> None:
        h0 = r19.upper_floor_decision(Q(9, 100), Q(1))
        k0 = r19.upper_floor_decision(Q(1, 10), Q(1))
        below = r19.upper_floor_decision(Q(5, 6), Q(1943))
        face = r19.upper_floor_decision(Q(5, 6), Q(1944))
        assert (h0.piece, h0.membership) == ("H0", True)
        assert (k0.piece, k0.membership) == ("K0", True)
        assert (below.piece, below.membership) == ("seam-54", True)
        assert (face.piece, face.membership) == ("seam-54", False)

    def test_hk_switch_bracket_is_retained(self) -> None:
        left = r19.r18.r17.certified_sign(
            "left",
            lambda: r19.r18.r17.hk_switch_polynomial_ball(Q(9407, 100000)),
        )
        right = r19.r18.r17.certified_sign(
            "right",
            lambda: r19.r18.r17.hk_switch_polynomial_ball(Q(94071, 1000000)),
        )
        assert (left.sign, right.sign) == (-1, 1)

    @pytest.mark.parametrize(
        ("rho", "k", "certificate"),
        [
            (r19.B0_RHO_LO, r19.B0_K_LO, "round8-certified-pilot-B0"),
            (r19.B0_RHO_HI, r19.B0_K_HI, "round8-certified-pilot-B0"),
            (r19.B1_RHO_LO, r19.B1_K_LO, "round17-certified-pilot-B1"),
            (r19.B1_RHO_HI, r19.B1_K_HI, "round17-certified-pilot-B1"),
        ],
    )
    def test_old_boxes_remain_analytic_regressions(
        self, rho: Q, k: Q, certificate: str
    ) -> None:
        result = r19.classify_point(rho, k)
        assert result.status == "analytic_covered"
        assert certificate in result.certified_regression_reasons

    def test_invalid_and_outside_domains(self) -> None:
        assert r19.classify_point(Q(1, 100), Q(1)).status == "outside_I18"
        with pytest.raises(ValueError):
            r19.classify_point(Q(1, 2), Q(-1))
        with pytest.raises(ValueError):
            r19.classify_point(Q(0), Q(1))


class TestIntervalIndeterminacy:
    def test_mandatory_rho_star_gate_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(lambda: r19.r18.r17.constants()[3])
        result = r19.classify_point(rho, Q(0))
        assert result.status == "indeterminate"
        assert "rho-rho_*" in result.unresolved_comparisons

    def test_material_rho_c_assignment_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(
            lambda: 1 / (1 + 2 * r19.r18.r17.arb.pi())
        )
        result = r19.classify_point(rho, Q(7))
        assert result.status == "indeterminate"
        assert "rho(1+2*pi)-1" in result.unresolved_comparisons

    def test_z_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: 2 * r19.r18.r17.arb.pi())
        result = r19.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert {"pi-(1-rho)K", "(1-rho)K-pi"} & set(
            result.unresolved_comparisons
        )

    def test_k5_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r19.r18.r17.arb.pi()) ** 2 + 30).sqrt()
        )
        result = r19.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert "pi^2+(30-K^2)(1-rho)^2" in result.unresolved_comparisons

    def test_k2_attribution_does_not_hide_decisive_band_coverage(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r19.r18.r17.arb.pi()) ** 2 + 6).sqrt()
        )
        attribution = r19.new_c18_decision(Q(1, 2), k)
        result = r19.classify_point(Q(1, 2), k)
        assert attribution.membership is None
        assert "pi^2+(6-K^2)(1-rho)^2" in attribution.unresolved_comparisons
        assert result.status == "analytic_covered"

    def test_k0_upper_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: r19.r18.r17.k0_ball(Q(1, 2)))
        result = r19.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert {"K-K_0(rho)", "K_0(rho)-K"} & set(
            result.unresolved_comparisons
        )

    def test_two_z_method_face_does_not_change_membership(self) -> None:
        k = _dyadic_midpoint(lambda: 4 * r19.r18.r17.arb.pi())
        walls = r19.method_wall_signs(Q(1, 2), k)
        result = r19.classify_point(Q(1, 2), k)
        assert walls[1].sign is None
        assert (result.status, result.residual_piece) == (
            "analytic_residual_uncovered",
            "post-k5",
        )

    def test_k6_method_face_does_not_change_membership(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r19.r18.r17.arb.pi()) ** 2 + 42).sqrt()
        )
        walls = r19.method_wall_signs(Q(1, 2), k)
        result = r19.classify_point(Q(1, 2), k)
        assert walls[2].sign is None
        assert (result.status, result.residual_piece) == (
            "analytic_residual_uncovered",
            "post-k5",
        )


class TestConsistency:
    @pytest.mark.parametrize(
        ("rho", "k"),
        [
            (Q(7, 51), Q(4)),
            (Q(1, 2), Q(9)),
            (Q(1, 2), Q(30)),
            (Q(3, 4), Q(20)),
            (Q(5, 6), Q(100)),
            (Q(6, 7), Q(100)),
        ],
    )
    def test_complement_and_normalized_form_agree(
        self, rho: Q, k: Q
    ) -> None:
        result = r19.classify_point(rho, k)
        direct = r19.normalized_d18_decision(rho, k)
        assert result.status == "analytic_residual_uncovered"
        assert direct.membership is True
        assert result.residual_piece == direct.piece

    def test_theorem_uncovered_is_exactly_d18(self) -> None:
        for point in ((Q(7, 51), Q(4)), (Q(1, 2), Q(30))):
            assert r19.theorem_uncovered_decision(*point) == (
                r19.normalized_d18_decision(*point)
            )

    def test_self_check(self) -> None:
        checks = r19.self_check()
        assert len(checks) == 13
        assert len(checks) == len(set(checks))
