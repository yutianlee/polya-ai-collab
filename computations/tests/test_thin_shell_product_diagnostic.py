import importlib.util
from pathlib import Path
import sys

import mpmath as mp


MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "thin_shell_product_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location(
    "thin_shell_product_diagnostic", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
diagnostic = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = diagnostic
SPEC.loader.exec_module(diagnostic)


def test_strict_angular_wall():
    mp.mp.dps = 80
    for ell in [1, 2, 10, 100]:
        wall = mp.mpf(ell * (ell + 1))
        assert diagnostic.angular_q_from_x(wall) == ell
        assert diagnostic.angular_q_from_x(wall + mp.mpf("1e-40")) == ell + 1


def test_exact_rational_counterexample_certificate():
    certificate = diagnostic.rational_counterexample_certificate()
    assert certificate["status"] == "exact_fraction_certificate"
    assert certificate["radial_modes_are_1_2_3"]
    assert all(certificate["angular_checks"].values())
    assert certificate["product"] == 3589
    assert certificate["product_exceeds_weyl"]


def test_high_precision_rational_counterexample():
    mp.mp.dps = 80
    epsilon = mp.mpf(1) / 4
    product, qs = diagnostic.product_proxy(epsilon, mp.mpf(11))
    assert qs == [42, 36, 23]
    assert product == 3589
    assert product > diagnostic.weyl_proxy(epsilon, mp.mpf(11))


def test_radial_wall_excludes_new_mode():
    mp.mp.dps = 80
    epsilon = mp.mpf(1) / 4
    product, qs = diagnostic.product_at_radial_wall(epsilon, 4)
    assert len(qs) == 3
    assert product > diagnostic.weyl_proxy(epsilon, 4 * mp.pi)
