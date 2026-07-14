"""Adversarial tests for the independent Round 21 exact-D20 A4 verifier."""

from __future__ import annotations

import hashlib
import os
import py_compile
import shutil
import sys
from dataclasses import replace
from fractions import Fraction
from pathlib import Path

import pytest
from flint import arb, ctx

from computations import round21_verify_exact_d20_closure as verifier


@pytest.fixture(scope="session")
def sealed_modules():
    verifier.authenticate_inputs()
    return verifier.load_sealed_modules()


@pytest.fixture(scope="session")
def full_audit() -> verifier.AuditResult:
    return verifier.run_audit(384)


def test_exact_manifest_and_every_authenticated_byte_mutation(tmp_path: Path) -> None:
    scoped_packet = "state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md"
    rejected_packet = "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md"
    assert scoped_packet in verifier.EXPECTED_INPUT_HASHES
    assert rejected_packet not in verifier.EXPECTED_INPUT_HASHES

    for relative in verifier.EXPECTED_INPUT_HASHES:
        source = verifier.REPO_ROOT / relative
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    assert verifier.authenticate_inputs(tmp_path) == dict(verifier.EXPECTED_INPUT_HASHES)

    for relative in verifier.EXPECTED_INPUT_HASHES:
        target = tmp_path / relative
        original = target.read_bytes()
        target.write_bytes(original + b"\nROUND21_A4_MUTATION\n")
        with pytest.raises(verifier.AuthenticationError, match="SHA-256 mismatch"):
            verifier.authenticate_inputs(tmp_path)
        target.write_bytes(original)

    missing = dict(verifier.EXPECTED_INPUT_HASHES)
    missing.pop(next(iter(missing)))
    with pytest.raises(verifier.AuthenticationError, match="wrong authenticated path set"):
        verifier.validate_manifest_schema(missing)
    extra = dict(verifier.EXPECTED_INPUT_HASHES)
    extra["unexpected.md"] = "0" * 64
    with pytest.raises(verifier.AuthenticationError, match="wrong authenticated path set"):
        verifier.validate_manifest_schema(extra)


def test_hash_gated_loader_ignores_timestamp_valid_malicious_pyc(
    tmp_path: Path,
) -> None:
    source_path = tmp_path / "sealed_probe.py"
    cached_source = b"VALUE = 'cached'\n"
    authenticated_source = b"VALUE = 'source'\n"
    assert len(cached_source) == len(authenticated_source)

    source_path.write_bytes(cached_source)
    original_stat = source_path.stat()
    pyc_path = Path(py_compile.compile(str(source_path), doraise=True))
    assert pyc_path.is_file()

    # Preserve the timestamp-mode cache header's mtime and size while making
    # the authenticated source semantics disagree with the cached code.
    source_path.write_bytes(authenticated_source)
    os.utime(
        source_path,
        ns=(original_stat.st_atime_ns, original_stat.st_mtime_ns),
    )
    digest = hashlib.sha256(authenticated_source).hexdigest()
    module_name = "round21_a4_malicious_pyc_probe"
    try:
        module = verifier._load_hash_gated_module(module_name, source_path, digest)
        assert module.VALUE == "source"
        assert module.__loader__ is None
        assert module.__cached__ is None
        assert pyc_path.is_file()
    finally:
        sys.modules.pop(module_name, None)


def test_exact_constants_faces_split_and_u_orderings() -> None:
    constants = verifier.verify_exact_constants()
    assert constants.k11_guard_domain == verifier.K11_GUARD_DOMAIN == "rho_c<=rho<1"
    assert Fraction(3) < constants.pi_lower < constants.pi_upper < Fraction(22, 7)
    assert 14 * constants.pi_upper < 44
    # The omitted upper wall would make the assertion false.  At rho=2,
    # z=-pi and the exact upper enclosure proves k11(2)^2<144.
    assert constants.pi_upper**2 + 132 < 144
    assert constants.machin_angle_lower == Fraction(70369, 89625)
    assert (
        Fraction(3, 4)
        < constants.machin_angle_lower
        < constants.machin_angle_upper
        == Fraction(4, 5)
        < 1
    )
    certificate = constants.branch_certificate
    assert certificate.schema == verifier.MACHIN_BRANCH_SCHEMA
    assert certificate.theta_definition == verifier.MACHIN_THETA_DEFINITION
    assert certificate.shared_injectivity_interval == (Fraction(0), Fraction(1))
    assert certificate.principal_atan_one_interval == certificate.shared_injectivity_interval
    assert certificate.theta_tangent == certificate.principal_atan_one_tangent == 1
    assert certificate.conclusion == verifier.MACHIN_PRINCIPAL_CONCLUSION

    replay = verifier.verify_exact_set_logic()
    assert replay.exhaustive_sign_rows == 3**5
    assert replay.ordering_cases == 3

    k200 = verifier.FaceSigns(
        verifier.Relation.EQUAL,
        verifier.Relation.BELOW,
        verifier.Relation.ABOVE,
        verifier.Relation.BELOW,
        verifier.Relation.EQUAL,
    )
    result = verifier.classify_faces(k200)
    assert result.in_d20
    assert result.compact_theorem_applies and result.aggregate_theorem_applies
    assert result.compact_owner and not result.aggregate_owner
    assert not result.in_proposed_d21

    with pytest.raises(verifier.ReplayError, match="double subtraction owner"):
        verifier._validate_classification(k200, replace(result, aggregate_owner=True))

    # Exact outer/shared faces.
    assert not verifier.classify_faces(
        replace(k200, rho_vs_rho_c=verifier.Relation.BELOW)
    ).in_d20  # rho=7/51 lies below rho_c.
    assert not verifier.classify_faces(
        replace(k200, rho_vs_39_over_50=verifier.Relation.EQUAL)
    ).in_d20
    assert not verifier.classify_faces(
        replace(k200, k_vs_k11=verifier.Relation.EQUAL)
    ).in_d20
    assert not verifier.classify_faces(replace(k200, k_vs_u=verifier.Relation.EQUAL)).in_d20


def test_cli_reports_the_exact_k11_guard_domain(
    full_audit: verifier.AuditResult,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(verifier, "run_audit", lambda _precision: full_audit)
    assert verifier.main(["--high-precision", "384"]) == 0
    output = capsys.readouterr().out
    assert "k11(rho)>12 for rho_c<=rho<1" in output
    assert "k11(rho)>12 for rho>=rho_c" not in output


def test_machin_branch_mutation_losing_lower_bound_is_rejected() -> None:
    mutated = replace(verifier.MACHIN_BRANCH_CERTIFICATE, theta_lower_bound=None)
    with pytest.raises(
        verifier.MachinBranchCertificateError,
        match="lower range bound missing or changed",
    ):
        verifier.verify_exact_constants(mutated)


def test_machin_branch_mutation_losing_upper_bound_is_rejected() -> None:
    mutated = replace(verifier.MACHIN_BRANCH_CERTIFICATE, theta_upper_bound=None)
    with pytest.raises(
        verifier.MachinBranchCertificateError,
        match="upper range bound missing or changed",
    ):
        verifier.verify_exact_constants(mutated)


def test_machin_branch_mutation_losing_or_changing_conclusion_is_rejected() -> None:
    for wrong_conclusion in (None, "theta=atan(1)+pi"):
        mutated = replace(
            verifier.MACHIN_BRANCH_CERTIFICATE,
            conclusion=wrong_conclusion,
        )
        with pytest.raises(
            verifier.MachinBranchCertificateError,
            match="principal-branch conclusion missing or changed",
        ):
            verifier.verify_exact_constants(mutated)


def test_compact_schema_interfaces_precision_and_static_decisions(sealed_modules) -> None:
    compact, _ = sealed_modules
    snapshot = verifier.compact_schema_snapshot(compact)
    verifier.validate_compact_schema(snapshot)
    verifier.validate_static_proof_paths()
    verifier.validate_compact_interfaces(compact, 256)

    with pytest.raises(verifier.SchemaError, match="compact schema mismatch"):
        verifier.validate_compact_schema(replace(snapshot, schema="mutated-schema"))
    with pytest.raises(verifier.SchemaError, match="compact schema mismatch"):
        verifier.validate_compact_schema(
            replace(snapshot, root=(Fraction(7, 52),) + snapshot.root[1:])
        )
    with pytest.raises(verifier.SchemaError, match="compact schema mismatch"):
        verifier.validate_compact_schema(replace(snapshot, frozen_precision=257))
    with pytest.raises(compact.CertificateError, match="below the required"):
        compact.Certifier(compact.MIN_PRECISION_BITS - 1)
    with pytest.raises(verifier.SchemaError, match="wrong compact monotone corners"):
        verifier.validate_corner_policy(("rho_hi", "k_hi", "rho_lo", "k_lo"))

    with ctx.workprec(256):
        exact = compact.strict_count_upper_from_arb(arb(3))
        uncertain = compact.strict_count_upper_from_arb(arb("3 +/- 0.01"))
    assert (exact.count, exact.wall_straddle) == (2, False)
    assert (uncertain.count, uncertain.ceiling, uncertain.wall_straddle) == (3, 4, True)
    assert compact.active_channel_count(Fraction(25, 2)) == 12
    coarse_root = compact.Certifier(256).evaluate(compact.ROOT_BOX)
    assert not coarse_root.passed
    assert not (coarse_root.comparison > 0)


def test_compact_leaf_digest_partition_and_sign_mutations(full_audit, sealed_modules) -> None:
    compact, _ = sealed_modules
    certificate = full_audit.compact_frozen.certificate
    verifier.validate_compact_certificate(certificate, frozen=True)

    first = certificate.leaves[0]
    changed_box = replace(first.box, k_lo=(first.box.k_lo + first.box.k_hi) / 2)
    changed_leaf = replace(first, box=changed_box)
    changed_leaves = (changed_leaf,) + certificate.leaves[1:]
    with pytest.raises(verifier.ReplayError):
        verifier.validate_compact_partition_independent(changed_leaves)

    with pytest.raises(verifier.ReplayError, match="leaf count"):
        verifier.validate_compact_partition_independent(certificate.leaves[1:])

    changed_depth = replace(first, depth=first.depth + 1)
    changed_certificate = replace(
        certificate,
        leaves=(changed_depth,) + certificate.leaves[1:],
    )
    with pytest.raises(verifier.ReplayError, match="digest"):
        verifier.validate_compact_certificate(changed_certificate, frozen=True)

    changed_proxy = replace(first, proxy_upper=first.proxy_upper + 1)
    with pytest.raises(compact.CertificateError, match="proxy tampering/mismatch"):
        compact.validate_leaves(compact.Certifier(256), (changed_proxy,))

    # A sufficiently enlarged integer proxy makes the leaf C10 comparison
    # nonpositive/uncertain and must be rejected.
    failed_proxy = replace(first, proxy_upper=first.proxy_upper + 10**9)
    failed_certificate = replace(
        certificate,
        leaves=(failed_proxy,) + certificate.leaves[1:],
    )
    with pytest.raises(verifier.ReplayError, match="digest"):
        verifier.validate_compact_certificate(failed_certificate, frozen=True)


def test_aggregate_schema_partition_branches_and_scope_mutations(sealed_modules) -> None:
    _, aggregate = sealed_modules
    snapshot = verifier.aggregate_schema_snapshot(aggregate)
    verifier.validate_aggregate_schema(snapshot)
    boxes = aggregate.build_boxes()
    verifier.validate_aggregate_partition_independent(boxes)

    with pytest.raises(verifier.SchemaError, match="base-only schema mismatch"):
        verifier.validate_aggregate_schema(replace(snapshot, base_k=201))
    with pytest.raises(verifier.SchemaError, match="base-only schema mismatch"):
        verifier.validate_aggregate_schema(replace(snapshot, max_width=Fraction(1, 1999)))
    with pytest.raises(ValueError, match="at least"):
        aggregate.run_certificate(191, authenticate=False)

    gap = replace(boxes[1], lo=boxes[1].lo + Fraction(1, 10**9))
    with pytest.raises(verifier.ReplayError, match="gap"):
        verifier.validate_aggregate_partition_independent((boxes[0], gap) + boxes[2:])
    overlap = replace(boxes[1], lo=boxes[1].lo - Fraction(1, 10**9))
    with pytest.raises(verifier.ReplayError, match="overlap"):
        verifier.validate_aggregate_partition_independent((boxes[0], overlap) + boxes[2:])
    wrong_branch = replace(boxes[0], eta_regime="rho_ge_half")
    with pytest.raises(verifier.ReplayError, match="high branch crosses"):
        verifier.validate_aggregate_partition_independent((wrong_branch,) + boxes[1:])

    for index in range(len(verifier.AGGREGATE_PREDICATE_FAMILIES)):
        omitted = (
            verifier.AGGREGATE_PREDICATE_FAMILIES[:index]
            + verifier.AGGREGATE_PREDICATE_FAMILIES[index + 1 :]
        )
        with pytest.raises(verifier.SchemaError, match="predicate family"):
            verifier.validate_aggregate_predicate_schema(omitted)
    for index in range(len(verifier.AGGREGATE_ANALYTIC_BOUNDARY)):
        omitted = (
            verifier.AGGREGATE_ANALYTIC_BOUNDARY[:index]
            + verifier.AGGREGATE_ANALYTIC_BOUNDARY[index + 1 :]
        )
        with pytest.raises(verifier.SchemaError, match="analytic-boundary"):
            verifier.validate_analytic_boundary_schema(omitted)
    with pytest.raises(verifier.SchemaError, match="cannot claim"):
        verifier.enforce_aggregate_scope(base_frequency=200, universal_frequency_claim=True)
    with pytest.raises(verifier.SchemaError, match="fixed to K=200"):
        verifier.enforce_aggregate_scope(base_frequency=201, universal_frequency_claim=False)


def test_aggregate_outward_sign_family_eta_and_derivative_mutations(sealed_modules) -> None:
    _, aggregate = sealed_modules
    boxes = aggregate.build_boxes()
    box = boxes[0]
    midpoint = (box.lo + box.hi) / 2
    with ctx.workprec(384):
        enclosure = aggregate.arb_box(box)
        verifier.require_outward_box(enclosure, box.lo, box.hi)
        exact_midpoint_ball = verifier.arb_of_fraction(midpoint)
        with pytest.raises(verifier.ReplayError, match="misses exact"):
            verifier.require_outward_box(exact_midpoint_ball, box.lo, box.hi)

        values = aggregate.evaluate_at_k0(enclosure, box.eta_regime)
        assert verifier.verify_aggregate_values(values, enclosure, box) == 11
        omitted = dict(values)
        omitted.pop("BK200")
        with pytest.raises(verifier.SchemaError, match="value family changed"):
            verifier.verify_aggregate_values(omitted, enclosure, box)
        wrong_sign = dict(values)
        wrong_sign["F"] = -arb(1)
        with pytest.raises(verifier.ReplayError, match=r"F\(rho\)>0"):
            verifier.verify_aggregate_values(wrong_sign, enclosure, box)

        half = verifier.arb_of_fraction(Fraction(1, 2))
        low_eta = aggregate.evaluate_at_k0(half, "rho_le_half")["eta"]
        high_eta = aggregate.evaluate_at_k0(half, "rho_ge_half")["eta"]
        assert (low_eta - high_eta).contains(0)
        assert not (low_eta - (high_eta + arb(1))).contains(0)

        identities = verifier.derivative_check_at(aggregate, midpoint, box.eta_regime)
        assert all(ball.contains(0) for ball in identities.expressions.values())
        for difference in identities.expressions.values():
            assert not (difference + arb(1)).contains(0)


def test_full_frozen_and_higher_precision_replays(full_audit) -> None:
    assert len(full_audit.authenticated_inputs) == len(verifier.EXPECTED_INPUT_HASHES) == 18
    assert full_audit.set_replay.exhaustive_sign_rows == 243
    assert not full_audit.analytic_chain_claimed

    compact256 = full_audit.compact_frozen.certificate
    compact384 = full_audit.compact_high.certificate
    assert (full_audit.compact_frozen.precision_bits, full_audit.compact_high.precision_bits) == (
        256,
        384,
    )
    assert len(compact256.leaves) == len(compact384.leaves) == 10_580
    assert compact256.leaves == compact384.leaves
    assert compact256.digest == verifier.COMPACT_DIGEST
    assert verifier.independent_compact_digest(compact256) == verifier.COMPACT_DIGEST
    assert compact256.generated_proxy_corners == compact384.generated_proxy_corners == 16_020
    assert (
        compact256.generated_floor_comparisons
        == compact384.generated_floor_comparisons
        == 2_153_076
    )
    assert compact256.generated_wall_straddles == compact384.generated_wall_straddles == 0

    aggregate192 = full_audit.aggregate_frozen
    aggregate384 = full_audit.aggregate_high
    assert (aggregate192.precision_bits, aggregate384.precision_bits) == (192, 384)
    assert aggregate192.result.box_count == aggregate384.result.box_count == 1_286
    assert aggregate192.sign_checks == aggregate384.sign_checks == 1_286 * 11
    assert aggregate192.endpoint_containments == aggregate384.endpoint_containments == 1_286 * 2
    assert aggregate192.derivative_points == 0
    assert aggregate384.derivative_points == 1_286
    assert aggregate192.base_frequency_only and aggregate384.base_frequency_only


def test_cli_reports_finite_a4_scope_only(full_audit, monkeypatch, capsys) -> None:
    monkeypatch.setattr(verifier, "run_audit", lambda high_precision: full_audit)
    assert verifier.main(["--high-precision", "384"]) == 0
    output = capsys.readouterr().out
    assert "ROUND21_EXACT_D20_CLOSURE_A4 PASS" in output
    assert "aggregate_scope=finite outward predicates at K=200 only" in output
    assert "analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED" in output
