"""Regression tests for the revision-1 ratio-sharp analytic closure."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "computations"
    / "certification"
    / "verify_ratio_sharp_scalar.py"
)


def _module():
    spec = importlib.util.spec_from_file_location("ratio_sharp", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_rational_scalar_bounds() -> None:
    checks = _module().exact_rational_checks()
    assert checks
    assert all(value > 0 for value in checks.values())


def test_interval_base_curve_regression() -> None:
    result = _module().interval_base_regression(parts=2000)
    assert result["minimum_F0_lower_endpoint"] > 0.17
    assert result["minimum_D0_lower_endpoint"] > 0.04
