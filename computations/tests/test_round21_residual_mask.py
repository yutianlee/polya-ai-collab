"""Tests for the frozen exact accepted-Round-20 residual classifier."""

from fractions import Fraction as Q
import hashlib
from itertools import product
from pathlib import Path
import subprocess

import pytest

from computations import round21_residual_mask as r21


ROOT = Path(__file__).resolve().parents[2]
BASELINE_BLOB_PATHS = {
    "state/proof_obligations.yml",
    "state/next_round_prompts.md",
}


def _dyadic_midpoint(builder) -> Q:
    """Return a greater-than-4096-bit dyadic approximation to a face."""

    core = r21.r20.r19.r18.r17
    old_precision = core.ctx.prec
    try:
        core.ctx.prec = 4096
        midpoint = builder().mid()
        mantissa, exponent = midpoint.man_exp()
        return Q(int(mantissa)) * Q(2) ** int(exponent)
    finally:
        core.ctx.prec = old_precision


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _git_blob_sha256(commit: str, relative_path: str) -> str:
    completed = subprocess.run(
        ["git", "show", f"{commit}:{relative_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return hashlib.sha256(completed.stdout).hexdigest()


class TestManifest:
    def test_derivation_is_exactly_the_round20_union(self) -> None:
        assert r21._mask_manifest()["derivation"] == {
            "base_classifier": "computations/round20_residual_mask.py",
            "base_interpretation": "opaque accepted A19",
            "operation": "A20=A19 union accepted_Round20_cover",
            "residual_operation": "D20=D19 minus genuinely_new_C20",
        }

    def test_exact_one_piece_residual(self) -> None:
        residual = r21._mask_manifest()["analytic_residual"]
        assert residual == {
            "name": "D20",
            "ratio_piece": "rho_c<=rho<39/50",
            "frequency_piece": "k11(rho)<K<K0(rho)=U(rho)",
            "rho_c_assignment": "included in D20 strictly above k11",
            "rho_optical_assignment": "excluded; optical-owned",
            "frequency_faces": "both strict",
        }

    def test_accepted_cover_and_genuinely_new_part_are_distinguished(self) -> None:
        manifest = r21._mask_manifest()
        cover = manifest["accepted_round20_cover"]
        assert cover["lower_piece"] == "complete accepted D19 lower two pieces"
        assert cover["high_closed_piece"] == (
            "rho_c<=rho<=7/8 and z_rho<=K<=k11(rho)"
        )
        assert cover["optical_piece"] == "39/50<=rho<1 and K>=0"
        new = manifest["genuinely_new_C20"]
        assert new["staircase_piece"] == (
            "rho_c<=rho<7/8 and k6(rho)<K<=k11(rho)"
        )
        assert new["optical_piece"] == (
            "39/50<=rho<7/8 and k11(rho)<K<U(rho)"
        )

    def test_live_upper_floor_is_exactly_k0(self) -> None:
        identity = r21._mask_manifest()["upper_floor_identity"]
        assert identity == {
            "formula": "U(rho)=K0(rho) on rho_c<=rho<39/50",
            "H0_ineligible": "rho>=rho_c>omega0",
            "seam_ineligible": "rho<39/50<5/6",
        }

    def test_theorem_uncovered_and_regression_absorption(self) -> None:
        manifest = r21._mask_manifest()
        assert manifest["theorem_wise_uncovered"]["formula"] == "U20=D20"
        regressions = manifest["certified_regressions"]
        assert regressions["B0"]["relation"].endswith("A19 subset A20")
        assert regressions["B1"]["relation"].endswith("A19 subset A20")
        assert "neither box is subtracted again" in regressions["uncovered_formula"]

    def test_no_round21_theorem_or_successor_residual_is_encoded(self) -> None:
        scope = r21._mask_manifest()["scope"]
        assert scope == {
            "round21_certificate_encoded": False,
            "round21_candidate_encoded": False,
            "successor_residual_proposed": False,
            "new_spectral_estimate": False,
            "residual_nonempty_witness": ["1/2", "30"],
        }
        source = Path(r21.__file__).read_text(encoding="utf-8")
        for forbidden in (
            "round21_certify_compact_proxy",
            "round21_verify_aggregate_tail",
            "compact-proxy-rectangle.md",
            "aggregate-tail-global.md",
            "exact-d20-closure.md",
        ):
            assert forbidden not in source

    def test_authenticated_inputs_match_frozen_bytes(self) -> None:
        inputs = r21._mask_manifest()["authenticated_inputs"]
        commit = inputs["baseline_commit"]
        assert commit == "e739a1cfcc5ce6647d70f2ddbc09598da4f496aa"
        for relative_path, expected in inputs.items():
            if relative_path == "baseline_commit":
                continue
            assert len(expected) == 64
            actual = (
                _git_blob_sha256(commit, relative_path)
                if relative_path in BASELINE_BLOB_PATHS
                else _sha256(relative_path)
            )
            assert actual == expected


class TestAcceptedRound20CoverTruthTable:
    def test_lower_cover_short_circuits_unresolved_high_signs(self) -> None:
        decide = r21.round20_cover_membership_from_signs
        assert decide(True, None, None, None, -1, rho_le_thin=True) is True
        assert decide(False, -1, 1, 1, -1, rho_le_thin=True) is False

    def test_staircase_includes_every_equality_face(self) -> None:
        decide = r21.round20_cover_membership_from_signs
        assert decide(False, 0, 0, 0, -1, rho_le_thin=True) is True
        assert decide(False, -1, 0, 0, -1, rho_le_thin=True) is False
        assert decide(False, 0, -1, 0, -1, rho_le_thin=True) is False
        assert decide(False, 0, 0, -1, -1, rho_le_thin=True) is False
        assert decide(False, 0, 0, 0, -1, rho_le_thin=False) is False

    def test_optical_face_is_inclusive_and_all_frequency(self) -> None:
        decide = r21.round20_cover_membership_from_signs
        assert decide(False, None, None, None, 0, rho_le_thin=False) is True
        assert decide(None, None, None, None, 1, rho_le_thin=False) is True
        assert decide(False, None, None, None, -1, rho_le_thin=False) is False

    def test_material_unknowns_remain_unknown(self) -> None:
        decide = r21.round20_cover_membership_from_signs
        assert decide(None, None, 1, 1, -1, rho_le_thin=True) is None
        assert decide(False, 1, None, 1, -1, rho_le_thin=True) is None
        assert decide(False, 1, 1, None, -1, rho_le_thin=True) is None


class TestD20TruthTable:
    @staticmethod
    def _independent_expected(
        rho_c: int | None,
        optical: int,
        k11: int | None,
        k0: int | None,
    ) -> bool | None:
        factors = (
            None if rho_c is None else rho_c >= 0,
            optical < 0,
            None if k11 is None else k11 < 0,
            None if k0 is None else k0 > 0,
        )
        if False in factors:
            return False
        if None in factors:
            return None
        return True

    def test_exhaustive_strong_kleene_table(self) -> None:
        for rho_c, optical, k11, k0 in product(
            (-1, 0, 1, None),
            (-1, 0, 1),
            (-1, 0, 1, None),
            (-1, 0, 1, None),
        ):
            assert r21.d20_membership_from_signs(
                rho_c, optical, k11, k0
            ) is self._independent_expected(rho_c, optical, k11, k0)

    def test_rho_c_is_included(self) -> None:
        assert r21.d20_membership_from_signs(0, -1, -1, 1) is True

    def test_optical_ratio_face_is_excluded(self) -> None:
        assert r21.d20_membership_from_signs(1, 0, -1, 1) is False

    def test_both_frequency_faces_are_excluded(self) -> None:
        assert r21.d20_membership_from_signs(1, -1, 0, 1) is False
        assert r21.d20_membership_from_signs(1, -1, -1, 0) is False

    def test_false_faces_suppress_irrelevant_unknowns(self) -> None:
        assert r21.d20_membership_from_signs(None, 0, None, None) is False
        assert r21.d20_membership_from_signs(None, -1, 0, None) is False
        assert r21.d20_membership_from_signs(None, -1, None, 0) is False

    def test_material_unknowns_are_not_guessed(self) -> None:
        assert r21.d20_membership_from_signs(None, -1, -1, 1) is None
        assert r21.d20_membership_from_signs(1, -1, None, 1) is None
        assert r21.d20_membership_from_signs(1, -1, -1, None) is None


class TestExactAndArbComparisons:
    def test_optical_side_is_exact(self) -> None:
        assert r21._rho_optical_sign(Q(77, 100)).sign == -1
        assert r21._rho_optical_sign(Q(39, 50)).sign == 0
        assert r21._rho_optical_sign(Q(4, 5)).sign == 1
        assert r21._rho_optical_sign(Q(39, 50)).precision_bits == 0

    def test_k11_sides_at_rho_half(self) -> None:
        assert r21._k11_upper_sign(Q(1, 2), Q(13)).sign == 1
        assert r21._k11_upper_sign(Q(1, 2), Q(14)).sign == -1

    @pytest.mark.parametrize("rho", [Q(7, 50), Q(1, 2), Q(3, 4), Q(77, 100)])
    def test_inherited_u_and_direct_k0_agree_on_live_interval(self, rho: Q) -> None:
        for k in (Q(13), Q(30), Q(600), Q(20000)):
            inherited = r21.r20.upper_floor_decision(rho, k)
            direct = r21._k0_upper_sign(rho, k)
            assert inherited.piece == "K0"
            assert inherited.membership is (direct.sign > 0)


class TestClassifierFaces:
    @pytest.mark.parametrize(
        ("rho", "k"),
        [(Q(1, 20), Q(12)), (Q(1, 10), Q(10)), (Q(13, 100), Q(20))],
    )
    def test_complete_d19_lower_is_now_covered(self, rho: Q, k: Q) -> None:
        result = r21.classify_point(rho, k)
        assert result.status == "analytic_covered"
        assert any("complete-d19-lower" in item for item in result.analytic_reasons)

    def test_new_k11_staircase_face_owner(self) -> None:
        result = r21.classify_point(Q(1, 2), Q(13))
        assert result.status == "analytic_covered"
        assert any("closed-k11-staircase" in item for item in result.analytic_reasons)

    @pytest.mark.parametrize(
        ("rho", "k"),
        [(Q(7, 50), Q(13)), (Q(1, 2), Q(14)), (Q(1, 2), Q(30)), (Q(77, 100), Q(20))],
    )
    def test_exact_one_piece_residual(self, rho: Q, k: Q) -> None:
        result = r21.classify_point(rho, k)
        assert (result.status, result.residual_piece) == (
            "analytic_residual_uncovered",
            "one-piece-d20",
        )

    def test_optical_face_and_high_ratios_are_covered(self) -> None:
        face = r21.classify_point(Q(39, 50), Q(30))
        high = r21.classify_point(Q(9, 10), Q(30))
        assert face.status == high.status == "analytic_covered"
        assert any("all-frequency-optical" in item for item in face.analytic_reasons)
        assert any("all-frequency-optical" in item for item in high.analytic_reasons)

    def test_inherited_endpoint_and_high_energy_owners_are_preserved(self) -> None:
        endpoint = r21.classify_point(Q(7, 8), Q(30))
        high = r21.classify_point(Q(1, 2), Q(600))
        global_high = r21.classify_point(Q(1, 2), Q(87025))
        assert endpoint.status == high.status == global_high.status == "analytic_covered"
        assert "rho-one-endpoint-round16" in endpoint.analytic_reasons
        assert "fixed-rho-high-energy" in high.analytic_reasons
        assert "round16-global-envelope" in global_high.analytic_reasons

    @pytest.mark.parametrize(
        ("rho", "k", "certificate"),
        [
            (r21.B0_RHO_LO, r21.B0_K_LO, "round8-certified-pilot-B0"),
            (r21.B0_RHO_HI, r21.B0_K_HI, "round8-certified-pilot-B0"),
            (r21.B1_RHO_LO, r21.B1_K_LO, "round17-certified-pilot-B1"),
            (r21.B1_RHO_HI, r21.B1_K_HI, "round17-certified-pilot-B1"),
        ],
    )
    def test_old_boxes_remain_absorbed_regressions(
        self, rho: Q, k: Q, certificate: str
    ) -> None:
        result = r21.classify_point(rho, k)
        assert result.status == "analytic_covered"
        assert certificate in result.certified_regression_reasons

    def test_invalid_and_outside_domains(self) -> None:
        assert r21.classify_point(Q(1, 100), Q(1)).status == "outside_I20"
        with pytest.raises(ValueError):
            r21.classify_point(Q(1, 2), Q(-1))
        with pytest.raises(ValueError):
            r21.classify_point(Q(0), Q(1))


class TestIntervalIndeterminacy:
    def test_mandatory_rho_star_gate_stays_indeterminate(self) -> None:
        core = r21.r20.r19.r18.r17
        rho = _dyadic_midpoint(lambda: core.constants()[3])
        result = r21.classify_point(rho, Q(0))
        assert result.status == "indeterminate"
        assert "rho-rho_*" in result.unresolved_comparisons

    def test_material_rho_c_side_stays_indeterminate(self) -> None:
        core = r21.r20.r19.r18.r17
        rho = _dyadic_midpoint(lambda: 1 / (1 + 2 * core.arb.pi()))
        result = r21.classify_point(rho, Q(30))
        assert result.status == "indeterminate"
        assert "rho(1+2*pi)-1" in result.unresolved_comparisons

    def test_z_face_stays_indeterminate_before_staircase_decision(self) -> None:
        core = r21.r20.r19.r18.r17
        k = _dyadic_midpoint(lambda: 2 * core.arb.pi())
        result = r21.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert "(1-rho)K-pi" in result.unresolved_comparisons

    def test_k11_face_stays_indeterminate(self) -> None:
        core = r21.r20.r19.r18.r17
        k = _dyadic_midpoint(lambda: ((2 * core.arb.pi()) ** 2 + 132).sqrt())
        result = r21.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert "pi^2+(132-K^2)(1-rho)^2" in result.unresolved_comparisons

    def test_k0_upper_face_stays_indeterminate(self) -> None:
        core = r21.r20.r19.r18.r17
        k = _dyadic_midpoint(lambda: core.k0_ball(Q(1, 2)))
        result = r21.classify_point(Q(1, 2), k)
        assert result.status == "indeterminate"
        assert "K_0(rho)-K" in result.unresolved_comparisons

    def test_optical_face_suppresses_frequency_unknowns(self) -> None:
        core = r21.r20.r19.r18.r17
        for k in (
            _dyadic_midpoint(
                lambda: (
                    (core.arb.pi() / (1 - core.qball(Q(39, 50)))) ** 2 + 132
                ).sqrt()
            ),
            _dyadic_midpoint(lambda: core.k0_ball(Q(39, 50))),
        ):
            result = r21.classify_point(Q(39, 50), k)
            assert result.status == "analytic_covered"
            assert result.unresolved_comparisons == tuple()


class TestConsistency:
    def test_complement_and_normalized_form_agree_on_rational_grid(self) -> None:
        rhos = (
            Q(1, 20),
            Q(1, 10),
            Q(13, 100),
            Q(7, 50),
            Q(1, 2),
            Q(3, 4),
            Q(77, 100),
            Q(39, 50),
            Q(7, 8),
            Q(9, 10),
        )
        frequencies = (Q(0), Q(8), Q(10), Q(12), Q(13), Q(14), Q(20), Q(30), Q(64), Q(600), Q(87025))
        for rho, k in product(rhos, frequencies):
            result = r21.classify_point(rho, k)
            direct = r21.normalized_d20_decision(rho, k)
            if result.status == "analytic_residual_uncovered":
                assert direct.membership is True
                assert result.residual_piece == "one-piece-d20"
            elif result.status in {"analytic_covered", "outside_I20"}:
                assert direct.membership is False
            else:
                assert direct.membership is None

    def test_theorem_uncovered_is_exactly_d20(self) -> None:
        for point in (
            (Q(7, 50), Q(13)),
            (Q(1, 2), Q(30)),
            (Q(77, 100), Q(20)),
            (Q(39, 50), Q(30)),
        ):
            assert r21.theorem_uncovered_decision(*point) == (
                r21.normalized_d20_decision(*point)
            )

    def test_self_check(self) -> None:
        checks = r21.self_check()
        assert len(checks) == 11
        assert len(checks) == len(set(checks))
