import importlib.util
from pathlib import Path
import sys

import mpmath as mp
import numpy as np


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "thin_scaled_action_round6_diagnostic.py"
)
SPEC = importlib.util.spec_from_file_location(
    "thin_scaled_action_round6_diagnostic", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
diagnostic = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = diagnostic
SPEC.loader.exec_module(diagnostic)


def test_closed_form_matches_action_integral():
    mp.mp.dps = 70
    epsilon = mp.mpf("0.07")
    a = mp.mpf("9.25")
    for y in [mp.mpf("0"), mp.mpf("2"), (1 - epsilon) * a, mp.mpf("9")]:
        closed = diagnostic.scaled_action_mp(epsilon, a, y)
        turning_s = min(
            mp.mpf("1"),
            max(mp.mpf("0"), (1 - y / a) / epsilon),
        )
        integral = (
            mp.re(
                mp.quad(
                    lambda s: mp.sqrt(
                        a * a - y * y / (1 - epsilon * s) ** 2
                    )
                    / mp.pi,
                    [0, turning_s],
                )
            )
            if turning_s > 0
            else mp.mpf("0")
        )
        assert abs(closed - integral) < mp.mpf("1e-60")


def test_continuous_cubic_identity_numerically():
    mp.mp.dps = 60
    epsilon = mp.mpf("0.08")
    a = mp.mpf("4.5")
    rho = 1 - epsilon
    numerical = mp.quad(
        lambda y: y * diagnostic.scaled_action_mp(epsilon, a, y),
        [0, rho * a, a],
    )
    exact = a**3 / (3 * mp.pi) * (1 - epsilon + epsilon**2 / 3)
    assert abs(numerical - exact) < mp.mpf("1e-48")


def test_strict_floor_excludes_positive_integer_wall():
    values = np.array([0.0, 0.8, 1.0, 1.2, 2.0, 2.2])
    counts, walls = diagnostic._strict_floor_diagnostic(values, 1.0e-14)
    assert counts.tolist() == [0, 0, 0, 1, 1, 2]
    assert walls.tolist() == [False, False, True, False, True, False]


def test_raw_midpoint_shortcut_has_exact_thin_counterexample():
    # The exact proof uses rho>=9/10 and sqrt(14)>3.  Numerically check a
    # representative member only as a regression test for the formulas.
    epsilon = 0.01
    a = epsilon  # K=1, so only nu=1/2 is active.
    y = np.array([epsilon / 2])
    action = diagnostic.scaled_action_numpy(epsilon, a, y)[0]
    midpoint = epsilon * y[0] * action
    assert midpoint > diagnostic.target_integral(epsilon, a)


def test_transition_case_and_tail_scan_are_reproducible():
    case = diagnostic.analyze_case(0.01, 0.75)
    assert case.active_channels == 23562
    assert abs(case.coarse_proxy_ratio - 0.9949513034793327) < 2.0e-12
    assert case.coarse_proxy_ratio < 1.0
    assert case.shifted_tail_violations == 0
    assert case.minimum_scaled_inner_tail_margin > 0.0
    assert case.edge_channels == 236


def test_selected_radial_wall_uses_strict_jump():
    probe = diagnostic.coarse_radial_wall_probe("0.01", 6826, 72, 70)
    assert abs(float(probe["c_wall_epsilon_a_over_pi"]) - 0.75) < 2.0e-8
    assert probe["strict_wall_proxy_ratio"] < probe["immediate_right_proxy_ratio"]
    assert probe["immediate_right_proxy_ratio"] < 1.0


def test_K0_thin_scale():
    result = diagnostic.K0_diagnostic("0.01", 70)
    assert 0.98 < float(result["a_HE_over_leading_9pi3_over_4epsilon3"]) < 1.0
    assert float(result["a_HE_epsilon_K0"]) > 6.0e7
