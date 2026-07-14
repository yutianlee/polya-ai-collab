"""Tests for the frozen exact post-Round-19 residual classifier."""

from fractions import Fraction as Q
import hashlib
from pathlib import Path
import subprocess

import pytest

from computations import round20_residual_mask as r20


ROOT = Path(__file__).resolve().parents[2]
MUTABLE_STATE_PATHS = {
    "state/proof_obligations.yml",
    "state/next_round_prompts.md",
}


def _dyadic_midpoint(builder) -> Q:
    """Return a greater-than-4096-bit dyadic approximation to a face."""

    old_precision = r20.r19.r18.r17.ctx.prec
    try:
        r20.r19.r18.r17.ctx.prec = 4096
        midpoint = builder().mid()
        mantissa, exponent = midpoint.man_exp()
        return Q(int(mantissa)) * Q(2) ** int(exponent)
    finally:
        r20.r19.r18.r17.ctx.prec = old_precision


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _git_blob_sha256(commit: str, relative_path: str) -> str:
    """Authenticate mutable state from the frozen baseline, not live HEAD."""

    completed = subprocess.run(
        ["git", "show", f"{commit}:{relative_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return hashlib.sha256(completed.stdout).hexdigest()


class TestManifest:
    def test_derivation_is_exactly_the_round19_union(self) -> None:
        manifest = r20._mask_manifest()
        assert manifest["derivation"] == {
            "base_classifier": "computations/round19_residual_mask.py",
            "base_interpretation": "opaque accepted A18",
            "operation": "A19=A18 union accepted_Round19_cover",
            "residual_operation": "D19=D18 minus genuinely_new_C19",
        }

    def test_exact_three_piece_residual(self) -> None:
        residual = r20._mask_manifest()["analytic_residual"]
        assert residual == {
            "name": "D19",
            "small_hole_piece": "rho_*<rho<=rho0 and L(rho)<K<U(rho)",
            "middle_piece": "rho0<rho<rho_c and d<K<U(rho)",
            "high_piece": "rho_c<=rho<7/8 and k6(rho)<K<U(rho)",
            "all_frequency_faces": "strict",
            "rho0_assignment": "small_hole_piece",
            "rho_c_assignment": "high_piece",
        }

    def test_accepted_cover_and_new_part_are_distinguished(self) -> None:
        manifest = r20._mask_manifest()
        cover = manifest["accepted_round19_cover"]
        assert cover["lower_piece"] == "rho0<rho<rho_c and L(rho)<K<=d"
        assert cover["high_closed_piece"] == (
            "rho_c<=rho<=7/8 and z_rho<=K<=k6(rho)"
        )
        assert cover["included_new_frequency_faces"] == ["K=d", "K=k6(rho)"]
        new = manifest["genuinely_new_C19"]
        assert new["high_piece"] == (
            "rho_c<=rho<7/8 and k5(rho)<K<=k6(rho)"
        )

    def test_theorem_uncovered_and_regression_absorption(self) -> None:
        manifest = r20._mask_manifest()
        assert manifest["theorem_wise_uncovered"]["formula"] == "U19=D19"
        regressions = manifest["certified_regressions"]
        assert regressions["B0"]["relation"].endswith("A18 subset A19")
        assert regressions["B1"]["relation"].endswith("A18 subset A19")
        assert "neither box is subtracted again" in regressions["uncovered_formula"]

    def test_no_round20_candidate_is_encoded(self) -> None:
        scope = r20._mask_manifest()["scope"]
        assert scope["round20_candidate_encoded"] is False
        assert scope["new_spectral_estimate"] is False
        assert scope["residual_nonempty_witness"] == ["1/2", "30"]

    def test_authenticated_inputs_match_frozen_bytes(self) -> None:
        inputs = r20._mask_manifest()["authenticated_inputs"]
        commit = inputs["baseline_commit"]
        assert commit == "658674117632d60990ac9b9046aa0fcff9e91a62"
        for relative_path, expected in inputs.items():
            if relative_path == "baseline_commit":
                continue
            assert len(expected) == 64
            if relative_path in MUTABLE_STATE_PATHS:
                actual = _git_blob_sha256(commit, relative_path)
            else:
                actual = _sha256(relative_path)
            assert actual == expected


class TestC19TruthTable:
    def test_lower_component_strict_ratio_and_l_faces_closed_at_d(self) -> None:
        decide = r20.c19_membership_from_signs
        assert decide(1, -1, 1, 0, -1, -1, rho_le_thin=True) is True
        assert decide(0, -1, 1, 0, -1, -1, rho_le_thin=True) is False
        assert decide(1, 0, 1, 0, -1, -1, rho_le_thin=True) is False
        assert decide(1, -1, 0, 0, -1, -1, rho_le_thin=True) is False
        assert decide(1, -1, 1, -1, -1, -1, rho_le_thin=True) is False

    def test_high_component_includes_every_equality_face(self) -> None:
        decide = r20.c19_membership_from_signs
        assert decide(1, 0, 1, -1, 0, 0, rho_le_thin=True) is True
        assert decide(1, 0, 1, -1, -1, 0, rho_le_thin=True) is False
        assert decide(1, 0, 1, -1, 0, -1, rho_le_thin=True) is False
        assert decide(1, 0, 1, -1, 0, 0, rho_le_thin=False) is False

    def test_union_short_circuits_true_and_false_factors(self) -> None:
        decide = r20.c19_membership_from_signs
        assert decide(1, -1, 1, 1, None, None, rho_le_thin=True) is True
        assert decide(-1, None, 0, -1, None, None, rho_le_thin=False) is False
        assert decide(1, None, 1, 1, 1, 1, rho_le_thin=True) is None


class TestD19TruthTable:
    def test_small_hole_piece_includes_rho0_and_is_strict_at_l(self) -> None:
        decide = r20.d19_membership_from_signs
        assert decide(1, 1, -1, -1, 1, 1, 1, rho_lt_thin=True) is True
        assert decide(1, 1, 0, -1, 1, 0, 1, rho_lt_thin=True) is True
        assert decide(1, 1, 0, -1, 0, 0, 1, rho_lt_thin=True) is False

    def test_middle_piece_is_strict_at_d(self) -> None:
        decide = r20.d19_membership_from_signs
        assert decide(1, 1, 1, -1, 1, -1, 1, rho_lt_thin=True) is True
        assert decide(1, 1, 1, -1, 1, 0, 1, rho_lt_thin=True) is False

    def test_high_piece_includes_rho_c_and_is_strict_at_k6(self) -> None:
        decide = r20.d19_membership_from_signs
        assert decide(1, 1, 1, 0, 1, -1, -1, rho_lt_thin=True) is True
        assert decide(1, 1, 1, 0, 1, -1, 0, rho_lt_thin=True) is False

    def test_all_mandatory_outer_faces_are_excluded(self) -> None:
        decide = r20.d19_membership_from_signs
        assert decide(0, 1, 0, -1, 1, 1, 1, rho_lt_thin=True) is False
        assert decide(1, 0, 0, -1, 1, 1, 1, rho_lt_thin=True) is False
        assert decide(1, 1, 0, -1, 1, 1, 1, rho_lt_thin=False) is False

    def test_mandatory_indeterminacy_is_not_overridden(self) -> None:
        decide = r20.d19_membership_from_signs
        assert decide(None, 1, 0, -1, 1, 1, 1, rho_lt_thin=True) is None
        assert decide(1, None, 0, -1, 1, 1, 1, rho_lt_thin=True) is None

    def test_rho_c_indeterminacy_uses_both_adjacent_thresholds(self) -> None:
        decide = r20.d19_membership_from_signs
        # Above both d and k6: residual whichever side of rho_c is true.
        assert decide(1, 1, 1, None, 1, -1, -1, rho_lt_thin=True) is True
        # At/below both thresholds: covered whichever side is true.
        assert decide(1, 1, 1, None, 1, 0, 0, rho_lt_thin=True) is False
        # Between the adjacent thresholds: rho_c ownership is material.
        assert decide(1, 1, 1, None, 1, 0, -1, rho_lt_thin=True) is None


class TestExactRationalComparisons:
    def test_rho0_side_is_exact_after_positive_squaring(self) -> None:
        assert r20._rho0_sign(Q(1, 19)).sign == -1
        assert r20._rho0_sign(Q(1, 18)).sign == 1
        assert r20._rho0_sign(Q(1, 19)).precision_bits == 0

    def test_l_and_d_sides_are_exact(self) -> None:
        assert r20._l_lower_sign(Q(1, 10), Q(5)).sign == 0
        assert r20._l_lower_sign(Q(1, 10), Q(6)).sign == 1
        assert r20._d_upper_sign(Q(9)).sign == 1
        assert r20._d_upper_sign(Q(10)).sign == -1


class TestClassifierFaces:
    @pytest.mark.parametrize(
        ("rho", "k", "piece"),
        [
            (Q(1, 20), Q(12), "small-hole-through-rho0"),
            (Q(1, 10), Q(10), "middle-above-d"),
            (Q(1, 2), Q(30), "high-above-k6"),
        ],
    )
    def test_exactly_three_residual_pieces(self, rho: Q, k: Q, piece: str) -> None:
        result = r20.classify_point(rho, k)
        assert (result.status, result.residual_piece) == (
            "analytic_residual_uncovered",
            piece,
        )

    def test_promoted_lower_and_high_bands(self) -> None:
        lower = r20.classify_point(Q(1, 10), Q(9))
        high = r20.classify_point(Q(1, 2), Q(9))
        assert lower.status == high.status == "analytic_covered"
        assert any("lower-ratio-round19" in item for item in lower.analytic_reasons)
        assert any("high-ratio-round19" in item for item in high.analytic_reasons)

    def test_old_k5_band_remains_owned_by_a18(self) -> None:
        old = r20.classify_point(Q(1, 2), Q(8))
        assert old.status == "analytic_covered"
        assert "angular-staircase-round18" in old.analytic_reasons

    def test_thin_endpoint_owns_all_sampled_frequencies(self) -> None:
        for k in (Q(0), Q(1), Q(20), Q(1944), Q(87025)):
            result = r20.classify_point(Q(7, 8), k)
            assert result.status == "analytic_covered"
            assert "rho-one-endpoint-round16" in result.analytic_reasons

    @pytest.mark.parametrize(
        ("rho", "k", "certificate"),
        [
            (r20.B0_RHO_LO, r20.B0_K_LO, "round8-certified-pilot-B0"),
            (r20.B0_RHO_HI, r20.B0_K_HI, "round8-certified-pilot-B0"),
            (r20.B1_RHO_LO, r20.B1_K_LO, "round17-certified-pilot-B1"),
            (r20.B1_RHO_HI, r20.B1_K_HI, "round17-certified-pilot-B1"),
        ],
    )
    def test_old_boxes_remain_analytic_regressions(
        self, rho: Q, k: Q, certificate: str
    ) -> None:
        result = r20.classify_point(rho, k)
        assert result.status == "analytic_covered"
        assert certificate in result.certified_regression_reasons

    def test_invalid_and_outside_domains(self) -> None:
        assert r20.classify_point(Q(1, 100), Q(1)).status == "outside_I19"
        with pytest.raises(ValueError):
            r20.classify_point(Q(1, 2), Q(-1))
        with pytest.raises(ValueError):
            r20.classify_point(Q(0), Q(1))


class TestIntervalIndeterminacy:
    def test_mandatory_rho_star_gate_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(lambda: r20.r19.r18.r17.constants()[3])
        result = r20.classify_point(rho, Q(0))
        assert result.status == "indeterminate"
        assert "rho-rho_*" in result.unresolved_comparisons

    def test_material_rho_c_assignment_stays_indeterminate(self) -> None:
        rho = _dyadic_midpoint(
            lambda: 1 / (1 + 2 * r20.r19.r18.r17.arb.pi())
        )
        # Here d>K but k6<K: the adjacent accepted classifications differ.
        result = r20.classify_point(rho, Q(8))
        assert result.status == "indeterminate"
        assert "rho(1+2*pi)-1" in result.unresolved_comparisons

    def test_z_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: 2 * r20.r19.r18.r17.arb.pi())
        result = r20.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert {"pi-(1-rho)K", "(1-rho)K-pi"} & set(
            result.unresolved_comparisons
        )

    def test_old_k5_attribution_is_settled_by_closed_c19_band(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r20.r19.r18.r17.arb.pi()) ** 2 + 30).sqrt()
        )
        result = r20.classify_point(Q(1, 2), k)
        assert result.status == "analytic_covered"
        assert any("high-ratio-round19" in item for item in result.analytic_reasons)

    def test_k6_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(
            lambda: ((2 * r20.r19.r18.r17.arb.pi()) ** 2 + 42).sqrt()
        )
        result = r20.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert "pi^2+(42-K^2)(1-rho)^2" in result.unresolved_comparisons

    def test_k0_upper_face_stays_indeterminate(self) -> None:
        k = _dyadic_midpoint(lambda: r20.r19.r18.r17.k0_ball(Q(1, 2)))
        result = r20.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert {"K-K_0(rho)", "K_0(rho)-K"} & set(
            result.unresolved_comparisons
        )


class TestConsistency:
    @pytest.mark.parametrize(
        ("rho", "k"),
        [
            (Q(1, 20), Q(12)),
            (Q(1, 10), Q(10)),
            (Q(1, 2), Q(30)),
            (Q(3, 4), Q(30)),
            (Q(5, 6), Q(100)),
            (Q(6, 7), Q(100)),
        ],
    )
    def test_complement_and_normalized_form_agree_on_residual_points(
        self, rho: Q, k: Q
    ) -> None:
        result = r20.classify_point(rho, k)
        direct = r20.normalized_d19_decision(rho, k)
        assert result.status == "analytic_residual_uncovered"
        assert direct.membership is True
        assert result.residual_piece == direct.piece

    @pytest.mark.parametrize(
        ("rho", "k"),
        [
            (Q(1, 10), Q(9)),
            (Q(1, 2), Q(8)),
            (Q(1, 2), Q(9)),
            (Q(7, 8), Q(30)),
        ],
    )
    def test_covered_points_do_not_intersect_normalized_residual(
        self, rho: Q, k: Q
    ) -> None:
        assert r20.classify_point(rho, k).status == "analytic_covered"
        assert r20.normalized_d19_decision(rho, k).membership is False

    def test_theorem_uncovered_is_exactly_d19(self) -> None:
        for point in (
            (Q(1, 20), Q(12)),
            (Q(1, 10), Q(10)),
            (Q(1, 2), Q(30)),
        ):
            assert r20.theorem_uncovered_decision(*point) == (
                r20.normalized_d19_decision(*point)
            )

    def test_self_check(self) -> None:
        checks = r20.self_check()
        assert len(checks) == 10
        assert len(checks) == len(set(checks))
