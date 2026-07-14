from copy import deepcopy
from pathlib import Path

import pytest

from computations import round17_pilot_extension_certificate as producer
from computations import round17_verify_pilot_extension_certificate as checker


def test_single_upward_extension_passes_independent_checker() -> None:
    certificate = producer.build_certificate()
    report = checker.verify_certificate(certificate)
    assert report["status"] == "PASS"
    assert report["strict_weighted_count"] == 4
    assert report["assigned_shared_face"] == "K=168/25"
    assert report["checks"]["B1_subset_D16_verified"] is True
    assert report["checks"]["complete_face_intersection_verified"] is True
    assert float(report["exact_margin_displays"]["ell_two_Sturm_margin"]) > 0.1
    assert float(report["exact_margin_displays"]["Weyl_minus_count"]) > 14.7


def test_checker_rejects_a_second_or_larger_scope() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["scope"]["K"][1] = "337/50"
    with pytest.raises(checker.VerificationError, match="authorized single"):
        checker.verify_certificate(certificate)


def test_checker_rejects_broken_complete_face() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["parent_box"]["assigned_shared_face"] = "rho=1001/2000"
    with pytest.raises(checker.VerificationError, match="assigned face"):
        checker.verify_certificate(certificate)


def test_checker_rejects_tampered_count() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["strict_count"]["weighted_count"] = 3
    with pytest.raises(checker.VerificationError, match="reported count"):
        checker.verify_certificate(certificate)


def test_checker_rejects_tampered_provenance() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["provenance"]["sha256"]["frozen_round17_packet"] = "0" * 64
    with pytest.raises(checker.VerificationError, match="SHA-256 mismatch"):
        checker.verify_certificate(certificate)


def test_checker_is_independent_of_flint_and_round17_producer() -> None:
    source = Path(checker.__file__).read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.startswith(("import ", "from "))
    ]
    assert all("flint" not in line for line in import_lines)
    assert all("round17_pilot_extension_certificate" not in line for line in import_lines)
