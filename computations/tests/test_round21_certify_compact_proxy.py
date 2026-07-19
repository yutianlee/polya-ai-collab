from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest
from flint import arb, ctx


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "computations"))

import round21_certify_compact_proxy as cert  # noqa: E402


EXPECTED_LEAVES = 10_580
EXPECTED_MAX_DEPTH = 15
EXPECTED_DIGEST = "96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631"


@pytest.fixture(scope="session")
def full_certificate() -> cert.Certificate:
    return cert.build_certificate()


def test_dependency_hash_gates_and_tampering(tmp_path: Path) -> None:
    observed = cert.verify_packet_hashes()
    assert dict(observed) == dict(cert.PACKETS)

    packet_dir = tmp_path / "lemma_packets"
    packet_dir.mkdir()
    for name in cert.PACKETS:
        shutil.copyfile(cert.PACKET_DIR / name, packet_dir / name)
    victim = packet_dir / "SHELL-phase-enclosures.md"
    victim.write_bytes(victim.read_bytes() + b"\nTAMPERED\n")
    with pytest.raises(cert.HashGateError, match="hash mismatch"):
        cert.verify_packet_hashes(packet_dir)


def test_exact_strict_walls_and_interfaces() -> None:
    with ctx.workprec(cert.DEFAULT_PRECISION_BITS):
        exact_wall = cert.strict_count_upper_from_arb(arb(3))
        assert exact_wall.count == 2  # [3]_< = 2, not ordinary floor 3.
        assert exact_wall.ceiling == 3
        assert not exact_wall.wall_straddle

        uncertain_wall = cert.strict_count_upper_from_arb(arb("3 +/- 0.01"))
        assert uncertain_wall.count == 3  # safe fallback; never guesses a side.
        assert uncertain_wall.wall_straddle

        assert cert.strict_count_upper_from_arb(arb(1) / 4).count == 0

        rho = cert.Fraction(1, 2)
        k = cert.Fraction(3)
        nu = cert.Fraction(3, 2)  # exactly nu=rho*K
        assert cert.g_arb(rho * k, nu).is_exact()
        assert cert.g_arb(rho * k, nu) == arb(0)
        expected = cert.g_arb(k, nu) + arb(1) / 4
        assert (cert.proxy_argument_arb(rho, k, nu) - expected).contains(0)

        # The outer endpoint is owned exactly and has G_K(K)=0.
        assert cert.g_arb(cert.Fraction(25, 2), cert.Fraction(25, 2)) == arb(0)

    # At K=25/2 the strict channel nu=K is excluded.
    assert cert.active_channel_count(cert.Fraction(25, 2)) == 12
    assert cert.Fraction(23, 2) < cert.Fraction(25, 2)
    assert not (cert.Fraction(25, 2) < cert.Fraction(25, 2))

    # Shared rational faces have one owner, including root upper faces.
    rho_children = cert.Certifier._split_rho(cert.ROOT_BOX)
    shared_rho = rho_children[0].rho_hi
    sample_k = (cert.ROOT_BOX.k_lo + cert.ROOT_BOX.k_hi) / 2
    assert sum(cert.box_owns(cert.ROOT_BOX, box, shared_rho, sample_k) for box in rho_children) == 1
    assert cert.box_owns(cert.ROOT_BOX, rho_children[1], shared_rho, sample_k)

    k_children = cert.Certifier._split_k(cert.ROOT_BOX)
    shared_k = k_children[0].k_hi
    sample_rho = (cert.ROOT_BOX.rho_lo + cert.ROOT_BOX.rho_hi) / 2
    assert sum(cert.box_owns(cert.ROOT_BOX, box, sample_rho, shared_k) for box in k_children) == 1
    assert cert.box_owns(cert.ROOT_BOX, k_children[1], sample_rho, shared_k)


def test_precision_gate_and_deliberately_too_coarse_root() -> None:
    with pytest.raises(cert.CertificateError, match="below the required"):
        cert.Certifier(cert.MIN_PRECISION_BITS - 1)

    prover = cert.Certifier()
    evaluation = prover.evaluate(cert.ROOT_BOX)
    assert not evaluation.passed
    assert not (evaluation.comparison > 0)
    assert evaluation.proxy_upper == 554_407


def test_full_finite_certificate(full_certificate: cert.Certificate) -> None:
    result = full_certificate
    assert result.precision_bits >= cert.MIN_PRECISION_BITS
    assert len(result.leaves) == EXPECTED_LEAVES
    assert result.max_depth == EXPECTED_MAX_DEPTH
    assert result.digest == EXPECTED_DIGEST
    assert result.min_gap_display > 0
    assert result.generated_wall_straddles == 0
    cert.validate_partition(cert.ROOT_BOX, result.leaves)


def test_certificate_count_tampering_is_rejected(
    full_certificate: cert.Certificate,
) -> None:
    changed = cert.tampered_leaf(full_certificate.leaves[0])
    assert cert.certificate_digest(
        cert.ROOT_BOX,
        (changed,) + full_certificate.leaves[1:],
        full_certificate.precision_bits,
        full_certificate.packet_hashes,
    ) != full_certificate.digest

    prover = cert.Certifier(full_certificate.precision_bits)
    with pytest.raises(cert.CertificateError, match="proxy tampering/mismatch"):
        cert.validate_leaves(prover, (changed,))
