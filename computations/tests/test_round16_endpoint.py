"""Tamper-sensitive exact tests for computations.round16_verify_endpoint."""

from fractions import Fraction as Q
import unittest

from computations import round16_verify_endpoint as r16


class FrozenPacketTests(unittest.TestCase):
    def test_packet_digest_is_exact(self) -> None:
        self.assertEqual(
            r16.verify_packet_hash(),
            "5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09",
        )


class StrictCountingAndNormalizationTests(unittest.TestCase):
    def test_n1_proxy_wall_and_layer_cake(self) -> None:
        # A+1/4=3 is an exact proxy wall, so n=3 is excluded.
        self.assertEqual(r16.phase_layer_count(Q(11, 4)), 2)
        self.assertEqual(r16.phase_layer_count(Q(11, 4) - Q(1, 1000)), 2)
        self.assertEqual(r16.phase_layer_count(Q(11, 4) + Q(1, 1000)), 3)
        actions = (Q(11, 4), Q(7, 4), Q(5, 4), Q(3, 4), Q(0))
        left, right = r16.finite_layer_cake(actions, Q(1, 8))
        self.assertEqual(left, right)
        self.assertEqual(left, Q(5, 64))
        with self.assertRaises(ValueError):
            r16.finite_layer_cake(tuple(reversed(actions)), Q(1, 8))

    def test_n2_n3_exact_normalization(self) -> None:
        self.assertEqual(r16.action_unit_moment(), Q(1, 9))
        a, epsilon = Q(5), Q(1, 8)
        self.assertEqual(
            r16.n2_i_pi_coefficient(a, epsilon),
            r16.n2_i_pi_coefficient_from_shell_moments(a, epsilon),
        )
        self.assertEqual(
            r16.n3_twice_i_pi_coefficient(a, epsilon),
            r16.n3_volume_pi_coefficient(a, epsilon),
        )


class ProductScreenTests(unittest.TestCase):
    def test_p4_expansion_and_every_tested_radial_wall(self) -> None:
        self.assertEqual(r16.p4_direct(3, Q(7, 11)), r16.p4_closed(3, Q(7, 11)))
        for m in range(1, 12):
            self.assertEqual(r16.radial_decomposition(Q(m)), (m - 1, Q(1)))
            self.assertEqual(r16.p4_closed(m - 1, Q(1)), r16.p4_closed(m, Q(0)))
            delta = Q(1, 1000)
            self.assertEqual(r16.radial_decomposition(Q(m) - delta)[0], max(0, m - 1))
            self.assertEqual(r16.radial_decomposition(Q(m) + delta)[0], m)

    def test_p6_minimum_positivity_and_p9_reserve(self) -> None:
        t0 = Q(2, 5)
        self.assertEqual(r16.p6_tail_derivative(t0), 0)
        self.assertEqual(r16.p6_tail(t0), Q(-8, 375))
        self.assertLess(r16.p6_tail_derivative(Q(1, 5)), 0)
        self.assertGreater(r16.p6_tail_derivative(Q(4, 5)), 0)
        self.assertEqual(r16.p6_integer_lower_screen(1), Q(32, 375))
        self.assertGreater(r16.p6_integer_lower_screen(1), 0)
        self.assertEqual(r16.product_reserve(Q(1, 8)), Q(577, 2880))

    def test_p7_strict_target_gap_and_product_angular_walls(self) -> None:
        self.assertEqual(r16.p7_final_strict_margin(Q(7), Q(1, 8)), Q(7, 192))
        for ell in range(1, 10):
            wall = Q(ell * (ell + 1))
            delta = Q(1, 10_000)
            self.assertEqual(r16.product_angular_count_from_square(wall), ell)
            self.assertEqual(r16.product_angular_count_from_square(wall - delta), ell)
            self.assertEqual(r16.product_angular_count_from_square(wall + delta), ell + 1)


class ComplementaryActionScreenTests(unittest.TestCase):
    def test_h5_dependency_direction_cancels_g_tau(self) -> None:
        for g_tau, g_terminal in ((Q(0), Q(9)), (Q(7, 3), Q(13, 2))):
            self.assertEqual(r16.h5_psi_error_lower(g_tau, g_terminal), -g_terminal / 8)
        self.assertEqual(
            r16.h5_endpoint_screen(Q(7, 8), Q(11), Q(333, 106)),
            Q(7, 8) ** 2 * Q(11) ** 2 / 4
            - Q(333, 106) * Q(7, 8) * Q(11) / 4,
        )

    def test_h6_h7_h8_strict_walls(self) -> None:
        delta = Q(1, 10_000)
        for m in range(0, 10):
            wall = Q(m) + Q(1, 2)
            self.assertEqual(r16.h8_layer_count(Q(1), wall), m)
            self.assertEqual(r16.h8_layer_count(Q(1), wall - delta), m)
            self.assertEqual(r16.h8_layer_count(Q(1), wall + delta), m + 1)
            self.assertLess(m * m, r16.h8_layer_upper(Q(1), wall))
        for n in range(1, 10):
            wall_t = Q(n) - Q(1, 4)
            self.assertEqual(r16.action_radial_count(wall_t), n - 1)
            self.assertLess(r16.action_radial_count(wall_t), wall_t + Q(1, 4))

    def test_h9_h10_monotonicity_common_face_and_h11(self) -> None:
        epsilon = Q(1, 8)
        self.assertEqual(r16.h9_lower(epsilon), Q(21, 256))
        for face in (Q(1, 100), Q(1, 25), Q(1, 10), Q(1, 8)):
            self.assertGreater(r16.product_cost_derivative(face), 0)
            self.assertLess(r16.h9_derivative(face), 0)
            self.assertGreater(r16.h10_derivative(face, Q(3)), 0)
        self.assertEqual(r16.h10_upper(epsilon, Q(3)), Q(193, 4096))
        self.assertEqual(
            r16.h9_lower(epsilon) - r16.h10_upper(epsilon, Q(3)),
            Q(143, 4096),
        )
        for pi_value in (Q(3), Q(333, 106), Q(22, 7)):
            self.assertEqual(
                r16.h_common_face_scaled_radial(epsilon, pi_value),
                r16.h9_lower(epsilon),
            )
            self.assertEqual(
                r16.h_common_face_scaled_error(epsilon, pi_value),
                r16.h10_upper(epsilon, pi_value),
            )


class StretchAndConditionalTests(unittest.TestCase):
    def test_s1_through_s4_exact_fractions(self) -> None:
        self.assertEqual(r16.product_reserve(Q(1, 7)), Q(1723, 8820))
        self.assertEqual(r16.complementary_screen(Q(1, 7), Q(3)), Q(139, 21609))
        self.assertEqual(r16.product_reserve(Q(4, 27)), Q(12719, 65610))
        self.assertEqual(
            r16.complementary_screen(Q(4, 27), Q(333, 106)),
            Q(162570113, 235723844196),
        )
        self.assertEqual(
            r16.complementary_screen(Q(3, 20), Q(333, 106)),
            Q(-44729, 20535000),
        )
        self.assertEqual(
            r16.complementary_screen(Q(1, 6), Q(333, 106)),
            Q(-3983743, 143712144),
        )

    def test_c1_c2_exact_arithmetic(self) -> None:
        self.assertEqual(295**2, 87025)
        self.assertLess(64, 87025)
        self.assertEqual(54 * 8**2, 3456)
        self.assertEqual(r16.conditional_reduction(), Q(8000, 3481))
        self.assertEqual(r16.conditional_reduction() - 2, Q(1038, 3481))
        self.assertGreater(r16.conditional_reduction(), 2)


if __name__ == "__main__":
    unittest.main()
