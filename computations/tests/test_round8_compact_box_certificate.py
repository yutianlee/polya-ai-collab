from copy import deepcopy
from pathlib import Path

import pytest
from flint import arb, ctx

from computations import round8_compact_box_certificate as producer
from computations import round8_verify_compact_box_certificate as checker


def test_arb_recurrence_matches_independent_ell_one_identity() -> None:
    ctx.prec = 200
    rho = arb("1/2")
    k = arb("33/5")
    recurrence = producer.shell_determinant(1, rho, k)
    t = (1 - rho) * k
    explicit = (
        (1 + 1 / (rho * k**2)) * t.sin()
        - ((1 - rho) / (rho * k)) * t.cos()
    )
    assert (recurrence - explicit).contains(0)
    assert recurrence < 0


def test_pilot_certificate_passes_independent_fraction_checker() -> None:
    certificate = producer.build_certificate()
    report = checker.verify_certificate(certificate)
    assert report["status"] == "PASS"
    assert report["strict_weighted_count"] == 4
    assert float(report["weyl_margin_lower_display"]) > 14.6
    assert report["checks"]["full_box_inside_R_C"] is True


def test_checker_rejects_tampered_count() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["strict_count"]["weighted_count"] = 3
    with pytest.raises(checker.VerificationError, match="reported count mismatch"):
        checker.verify_certificate(certificate)


def test_checker_rejects_tampered_determinant_sign() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["channels"][0]["determinant_lower_face"]["sign"] = "negative"
    with pytest.raises(checker.VerificationError, match="producer sign label mismatch"):
        checker.verify_certificate(certificate)


def test_checker_rejects_tampered_source_hash() -> None:
    certificate = deepcopy(producer.build_certificate())
    certificate["reproducibility"]["sha256"]["producer"] = "0" * 64
    with pytest.raises(checker.VerificationError, match="SHA-256 mismatch for producer"):
        checker.verify_certificate(certificate)


def test_checker_has_no_flint_or_producer_import() -> None:
    source = Path(checker.__file__).read_text(encoding="utf-8")
    import_lines = [line.strip() for line in source.splitlines() if line.startswith(("import ", "from "))]
    assert all("flint" not in line for line in import_lines)
    assert all("round8_compact_box_certificate" not in line for line in import_lines)
