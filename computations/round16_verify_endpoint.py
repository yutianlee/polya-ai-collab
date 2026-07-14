"""Exact finite-algebra checks for the frozen Round 16 endpoint packet.

This module deliberately uses only the Python standard library and exact
``Fraction`` arithmetic.  It authenticates the frozen packet and checks the
finite algebra in the N, P, H, S, and C screens.  It does *not* verify the
analytic hypotheses behind min--max comparison, phase transfer, the action
inverse, curvature, or the Stieltjes endpoint limits, and therefore it does
not prove the Round 16 endpoint theorem.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from typing import Sequence


PACKET_SHA256 = "5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09"
ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "state" / "lemma_packets" / "SHELL-rho-one-endpoint-round16.md"


def verify_packet_hash(path: Path = PACKET) -> str:
    """Return the digest after rejecting any packet other than the frozen one."""

    digest = sha256(path.read_bytes()).hexdigest()
    if digest != PACKET_SHA256:
        raise AssertionError(f"frozen packet hash mismatch: {digest}")
    return digest


def ceil_q(value: Q) -> int:
    """Exact ceiling of a rational number."""

    return -((-value.numerator) // value.denominator)


def strict_bracket(value: Q) -> int:
    """The packet's [u]_< = ceil(u)-1 convention."""

    return ceil_q(value) - 1


def phase_layer_count(action: Q) -> int:
    """N1 count of positive n with n-1/4 strictly below ``action``."""

    if action < 0:
        raise ValueError("action must be nonnegative")
    return strict_bracket(action + Q(1, 4))


def half_integer_count(epsilon: Q, x: Q) -> int:
    """H6 count of l >= 0 with epsilon(l+1/2) < x."""

    if epsilon <= 0 or x < 0:
        raise ValueError("require epsilon > 0 and x >= 0")
    return max(0, ceil_q(x / epsilon - Q(1, 2)))


def finite_layer_cake(action_values: Sequence[Q], epsilon: Q) -> tuple[Q, Q]:
    """Finite N1--N2 double-counting identity for sampled action layers.

    ``action_values[l]`` plays the role of A(epsilon(l+1/2)).  No numerical
    action evaluation or inverse is used: this checks only the exact exchange
    of the two finite strict counts.
    """

    if epsilon <= 0 or any(value < 0 for value in action_values):
        raise ValueError("require epsilon > 0 and nonnegative actions")
    if any(action_values[i] < action_values[i + 1] for i in range(len(action_values) - 1)):
        raise ValueError("action layers must be nonincreasing")
    left = epsilon * sum(
        (epsilon * (ell + Q(1, 2))) * phase_layer_count(value)
        for ell, value in enumerate(action_values)
    )
    max_q = max((phase_layer_count(value) for value in action_values), default=0)
    right = Q(0)
    for n in range(1, max_q + 1):
        x_n = Q(n) - Q(1, 4)
        layers = sum(x_n < value for value in action_values)
        right += Q(1, 2) * epsilon * epsilon * layers * layers
    return left, right


def action_unit_moment() -> Q:
    """Integral of s(sqrt(1-s^2)-s arccos(s)) on [0,1]."""

    # The two exact integration-by-parts/Beta pieces are 1/3 and 2/9.
    return Q(1, 3) - Q(2, 9)


def n2_i_pi_coefficient(a: Q, epsilon: Q) -> Q:
    """Coefficient of 1/pi in N2's I."""

    if a < 0 or epsilon <= 0:
        raise ValueError("require a >= 0 and epsilon > 0")
    return a**3 * (Q(1) - epsilon + epsilon**2 / 3) / 3


def n2_i_pi_coefficient_from_shell_moments(a: Q, epsilon: Q) -> Q:
    """Same coefficient obtained as (a^3-(rho a)^3)/(9 epsilon)."""

    rho = Q(1) - epsilon
    return action_unit_moment() * a**3 * (Q(1) - rho**3) / epsilon


def n3_volume_pi_coefficient(a: Q, epsilon: Q) -> Q:
    """Coefficient of 1/pi in the volume side of N3."""

    rho = Q(1) - epsilon
    k = a / epsilon
    return Q(2, 9) * (Q(1) - rho**3) * k**3


def n3_twice_i_pi_coefficient(a: Q, epsilon: Q) -> Q:
    return 2 * n2_i_pi_coefficient(a, epsilon) / epsilon**2


def radial_decomposition(s: Q) -> tuple[int, Q]:
    """P3 strict radial convention for s=a/pi."""

    if s < 0:
        raise ValueError("s must be nonnegative")
    n = max(0, ceil_q(s) - 1)
    return n, s - n


def p4_direct(n: int, t: Q) -> Q:
    """D(a)/pi^2 from P2 before expansion, with a/pi=n+t."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    s = Q(n) + t
    sum_squares = Q(n * (n + 1) * (2 * n + 1), 6)
    s0 = n * s**2 - sum_squares
    return Q(2, 3) * s**3 - s0


def p4_closed(n: int, t: Q) -> Q:
    return Q(n * n, 2) + n * (t**2 + Q(1, 6)) + Q(2, 3) * t**3


def p6_exact(n: int, t: Q) -> Q:
    return p4_closed(n, t) - Q(2, 5) * (n + t) ** 2


def p6_square_form(n: int, t: Q) -> Q:
    return (
        Q(n * n, 10)
        + n * ((t - Q(2, 5)) ** 2 + Q(1, 150))
        + Q(2, 3) * t**3
        - Q(2, 5) * t**2
    )


def p6_tail(t: Q) -> Q:
    return Q(2, 3) * t**3 - Q(2, 5) * t**2


def p6_tail_derivative(t: Q) -> Q:
    return 2 * t * (t - Q(2, 5))


def p6_integer_lower_screen(n: int) -> Q:
    return Q(n * n, 10) + Q(n, 150) - Q(8, 375)


def product_cost_coefficient(epsilon: Q) -> Q:
    """Coefficient on the right of P8."""

    return Q(1, 6) + epsilon / 4 + epsilon**2 / 9


def product_cost_derivative(epsilon: Q) -> Q:
    return Q(1, 4) + 2 * epsilon / 9


def product_reserve(epsilon: Q) -> Q:
    return Q(2, 5) - product_cost_coefficient(epsilon)


def low_volume_factor(epsilon: Q) -> Q:
    """Factor 1-epsilon+epsilon^2/3 multiplying I(a)/epsilon^2."""

    return Q(1) - epsilon + epsilon**2 / 3


def p7_final_strict_margin(i_value: Q, epsilon: Q) -> Q:
    """Gap between I(1-epsilon) and the exact volume normalization."""

    return i_value * (low_volume_factor(epsilon) - (Q(1) - epsilon))


def product_angular_count_from_square(u_squared: Q) -> int:
    """P1 ceiling count, avoiding an inexact square root.

    It is the least m >= 0 for which u^2 <= m(m+1).  Thus an exact angular
    wall u^2=m(m+1) belongs to m, and the jump is strictly after the wall.
    """

    if u_squared < 0:
        raise ValueError("u_squared must be nonnegative")
    m = 0
    while u_squared > m * (m + 1):
        m += 1
    return m


def action_radial_count(t_value: Q) -> int:
    """H7 count of n >= 1 with n-1/4 < T."""

    if t_value < 0:
        raise ValueError("T must be nonnegative")
    return max(0, strict_bracket(t_value + Q(1, 4)))


def h5_psi_error_lower(g_tau: Q, g_terminal: Q) -> Q:
    """Worst endpoint/variation contribution from H4 on [tau,T]."""

    if not (0 <= g_tau <= g_terminal):
        raise ValueError("require 0 <= g(tau) <= g(T)")
    psi_lo, psi_hi = Q(-1, 32), Q(3, 32)
    return (
        g_terminal * psi_lo
        - g_tau * psi_hi
        - psi_hi * (g_terminal - g_tau)
    )


def h5_endpoint_screen(rho: Q, a: Q, pi_value: Q) -> Q:
    """F(tau)/4-g(T)/8 after the H3 endpoint substitutions."""

    f_tau = rho**2 * a**2
    g_terminal = 2 * pi_value * rho * a
    return f_tau / 4 - g_terminal / 8


def h8_layer_count(epsilon: Q, radius: Q) -> int:
    return half_integer_count(epsilon, radius)


def h8_layer_upper(epsilon: Q, radius: Q) -> Q:
    """Strict per-layer upper value r^2+epsilon*r+epsilon^2/4."""

    return radius**2 + epsilon * radius + epsilon**2 / 4


def h8_envelope(epsilon: Q, a: Q, pi_value: Q) -> Q:
    return (a / pi_value + Q(1, 4)) * (epsilon * a + epsilon**2 / 4)


def h9_lower(epsilon: Q) -> Q:
    return (Q(1) - epsilon) * (Q(1) - 5 * epsilon) / 4


def h9_derivative(epsilon: Q) -> Q:
    return (-6 + 10 * epsilon) / 4


def h10_upper(epsilon: Q, pi_lower: Q) -> Q:
    """H10 with pi replaced by a positive rational lower bound."""

    return (
        (epsilon + epsilon**2) / pi_lower
        + (epsilon**3 + epsilon**4) / pi_lower**2
    )


def h10_derivative(epsilon: Q, pi_lower: Q) -> Q:
    return (
        (1 + 2 * epsilon) / pi_lower
        + (3 * epsilon**2 + 4 * epsilon**3) / pi_lower**2
    )


def h_common_face_scaled_error(epsilon: Q, pi_value: Q) -> Q:
    """Direct E/a^2 at a=pi/(4 epsilon), for common-face equality."""

    a = pi_value / (4 * epsilon)
    return h8_envelope(epsilon, a, pi_value) / a**2


def h_common_face_scaled_radial(epsilon: Q, pi_value: Q) -> Q:
    """Direct H9 middle expression at a=pi/(4 epsilon)."""

    rho = Q(1) - epsilon
    a = pi_value / (4 * epsilon)
    return rho**2 / 4 - pi_value * rho / (4 * a)


def complementary_screen(epsilon: Q, pi_lower: Q) -> Q:
    return h9_lower(epsilon) - h10_upper(epsilon, pi_lower)


def conditional_reduction() -> Q:
    return Q(200000, 295**2)


def _require(label: str, condition: bool, passed: list[str]) -> None:
    if not condition:
        raise AssertionError(label)
    passed.append(label)


def verify_all(check_packet: bool = True) -> list[str]:
    """Execute all exact finite checks and return their labels."""

    passed: list[str] = []
    if check_packet:
        _require("packet SHA-256", verify_packet_hash() == PACKET_SHA256, passed)

    # N1--N3, including strict proxy walls and a finite layer-cake exchange.
    _require("N1 proxy wall", phase_layer_count(Q(11, 4)) == 2, passed)
    layers = (Q(11, 4), Q(7, 4), Q(5, 4), Q(3, 4), Q(0))
    left, right = finite_layer_cake(layers, Q(1, 8))
    _require("N1--N2 finite layer cake", left == right, passed)
    _require("N2 action unit moment", action_unit_moment() == Q(1, 9), passed)
    for a, epsilon in ((Q(5), Q(1, 8)), (Q(7, 3), Q(1, 25))):
        _require(
            "N2 shell normalization",
            n2_i_pi_coefficient(a, epsilon)
            == n2_i_pi_coefficient_from_shell_moments(a, epsilon),
            passed,
        )
        _require(
            "N3 volume normalization",
            n3_twice_i_pi_coefficient(a, epsilon)
            == n3_volume_pi_coefficient(a, epsilon),
            passed,
        )

    # P4--P9 and strict radial/angular conventions.
    for n, t in ((1, Q(1, 7)), (2, Q(3, 5)), (7, Q(1))):
        _require("P4 expansion", p4_direct(n, t) == p4_closed(n, t), passed)
        _require("P6 square completion", p6_exact(n, t) == p6_square_form(n, t), passed)
    for m in range(1, 8):
        _require(
            "P4 radial-wall continuity",
            p4_closed(m - 1, Q(1)) == p4_closed(m, Q(0)),
            passed,
        )
        _require(
            "P3 radial-wall convention",
            radial_decomposition(Q(m)) == (m - 1, Q(1)),
            passed,
        )
    _require("P6 critical point", p6_tail_derivative(Q(2, 5)) == 0, passed)
    _require("P6 exact minimum", p6_tail(Q(2, 5)) == Q(-8, 375), passed)
    _require("P6 N=1 positivity", p6_integer_lower_screen(1) == Q(32, 375), passed)
    _require("P9 reserve", product_reserve(Q(1, 8)) == Q(577, 2880), passed)
    _require("P8 monotonicity", product_cost_derivative(Q(1, 8)) > 0, passed)
    _require("P7 strict target gap", p7_final_strict_margin(Q(7), Q(1, 8)) > 0, passed)
    for ell in range(1, 8):
        wall = Q(ell * (ell + 1))
        delta = Q(1, 1000)
        _require(
            "P1 angular wall",
            product_angular_count_from_square(wall) == ell,
            passed,
        )
        _require(
            "P1 angular jump after wall",
            product_angular_count_from_square(wall + delta) == ell + 1,
            passed,
        )

    # H5 dependency arithmetic, H6--H8 strict walls, H9--H12 screens.
    for g_tau, g_terminal in ((Q(0), Q(9)), (Q(7, 3), Q(13, 2))):
        _require(
            "H5 Psi-direction cancellation",
            h5_psi_error_lower(g_tau, g_terminal) == -g_terminal / 8,
            passed,
        )
    _require(
        "H5 endpoint substitution",
        h5_endpoint_screen(Q(7, 8), Q(11), Q(333, 106))
        == Q(7, 8) ** 2 * Q(11) ** 2 / 4
        - Q(333, 106) * Q(7, 8) * Q(11) / 4,
        passed,
    )
    for m in range(0, 8):
        wall = Q(m) + Q(1, 2)
        delta = Q(1, 1000)
        _require("H6 half-integer wall", h8_layer_count(Q(1), wall) == m, passed)
        _require(
            "H6 half-integer jump after wall",
            h8_layer_count(Q(1), wall + delta) == m + 1,
            passed,
        )
        count = h8_layer_count(Q(1), wall)
        _require(
            "H8 strict per-layer ceiling",
            count * count < h8_layer_upper(Q(1), wall),
            passed,
        )
    for n in range(1, 8):
        wall_t = Q(n) - Q(1, 4)
        _require("H7 excluded radial wall", action_radial_count(wall_t) == n - 1, passed)
        _require("H7 strict count", action_radial_count(wall_t) < wall_t + Q(1, 4), passed)
    epsilon = Q(1, 8)
    _require("H9 endpoint", h9_lower(epsilon) == Q(21, 256), passed)
    _require("H9 decreasing", h9_derivative(epsilon) < 0, passed)
    _require("H10 increasing", h10_derivative(epsilon, Q(3)) > 0, passed)
    _require("H10 coarse endpoint", h10_upper(epsilon, Q(3)) == Q(193, 4096), passed)
    _require(
        "H11 reserve",
        h9_lower(epsilon) - h10_upper(epsilon, Q(3)) == Q(143, 4096),
        passed,
    )
    for pi_value in (Q(3), Q(333, 106), Q(22, 7)):
        _require(
            "H9 common-face equality",
            h_common_face_scaled_radial(epsilon, pi_value) == h9_lower(epsilon),
            passed,
        )
        _require(
            "H10 common-face equality",
            h_common_face_scaled_error(epsilon, pi_value)
            == h10_upper(epsilon, pi_value),
            passed,
        )

    # S1--S4 exact selected screens.
    _require("S1 product", product_reserve(Q(1, 7)) == Q(1723, 8820), passed)
    _require(
        "S1 complementary",
        complementary_screen(Q(1, 7), Q(3)) == Q(139, 21609),
        passed,
    )
    _require("S2 product", product_reserve(Q(4, 27)) == Q(12719, 65610), passed)
    _require(
        "S2 complementary",
        complementary_screen(Q(4, 27), Q(333, 106))
        == Q(162570113, 235723844196),
        passed,
    )
    _require(
        "S3 selected obstruction",
        complementary_screen(Q(3, 20), Q(333, 106)) == Q(-44729, 20535000),
        passed,
    )
    _require(
        "S4 selected obstruction",
        complementary_screen(Q(1, 6), Q(333, 106))
        == Q(-3983743, 143712144),
        passed,
    )

    # C1--C2 arithmetic only.
    _require("C1 square", 295**2 == 87025, passed)
    _require("C1 coarse first ceiling", 64 < 87025, passed)
    _require("C1 coarse third ceiling", 54 * 8**2 == 3456 < 87025, passed)
    _require("C2 reduction", conditional_reduction() == Q(8000, 3481), passed)
    _require("C2 greater than two", conditional_reduction() - 2 == Q(1038, 3481), passed)
    return passed


def main() -> int:
    passed = verify_all()
    print(f"PASS: {len(passed)} exact finite checks")
    print(f"packet_sha256={PACKET_SHA256}")
    print("analytic_theorem_verified=false")
    print("These checks verify finite algebra, not the Round 16 analytic theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
