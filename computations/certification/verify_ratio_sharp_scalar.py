"""Independent regression checks for the ratio-sharp scalar closure.

The theorem proof is the exact rational/convexity argument in the LaTeX
module.  This script is deliberately redundant: it verifies every rational
cross-multiplication and uses outward-rounded interval arithmetic on the
entire base-curve range.  Its output is evidence against transcription
errors, not a premise of the proof.
"""

from __future__ import annotations

import json
from fractions import Fraction

from mpmath import iv


Q = Fraction


def exact_rational_checks() -> dict[str, Fraction]:
    pi_lo = Q(157, 50)
    pi_hi = Q(22, 7)

    checks = {
        "A_upper_cube_gap": Q(49, 40) ** 3
        - Q(243, 128_000) * pi_hi**6,
        "B_lower_cube_gap": Q(2187, 343 * 2**20) * pi_lo**6
        - Q(179, 1000) ** 3,
        "B_upper_cube_gap": Q(1, 5) ** 3
        - Q(2187, 343 * 2**20) * pi_hi**6,
        "C1_upper_cube_gap": Q(13, 25) ** 3
        - Q(9, 2000) * pi_hi**3,
        "C2_upper_cube_gap": Q(1, 25) ** 3
        - Q(81, 343 * 2**17) * pi_hi**3,
        "F_at_one_margin": Q(8269, 30_000) - Q(1, 4),
        "F_prime_at_one_margin": -Q(14_437, 6125) + Q(5, 2),
        "F_second_at_one_margin": Q(18_162, 1225) - 14,
        "F_third_margin": Q(676_141, 2450),
        "D_at_one_margin": Q(1, 300),
        "D_prime_at_one_margin": Q(54, 175),
        "D_second_margin": Q(1951, 100),
        "K_convexity_margin": Q(47_447, 443_682),
        "x_range_margin": Q(13, 10) ** 6 - Q(50, 11),
    }
    assert all(value > 0 for value in checks.values())
    return checks


def _interval(lower: Fraction, upper: Fraction):
    return iv.mpf([str(lower), str(upper)])


def interval_base_regression(parts: int = 2000) -> dict[str, float]:
    """Enclose F_0 and D_0 on 1 <= x <= 13/10."""

    iv.dps = 50
    pi = iv.pi
    two_thirds = iv.mpf(2) / 3
    one_third = iv.mpf(1) / 3

    c = (3 * pi) ** two_thirds / 2
    alpha = 6 * c / (5 * iv.mpf(4) ** (iv.mpf(5) / 3))
    beta = 3 * c**2 / (7 * iv.mpf(4) ** (iv.mpf(7) / 3))
    mathsf_a = alpha * pi ** (iv.mpf(4) / 3)
    mathsf_b = beta * pi ** two_thirds
    c1 = iv.mpf(4) / 3 * alpha * pi**one_third
    c2 = iv.mpf(2) / 3 * beta * pi ** (-one_third)

    min_f = float("inf")
    min_d = float("inf")
    width = Q(3, 10)
    for index in range(parts):
        left = Q(1) + width * Q(index, parts)
        right = Q(1) + width * Q(index + 1, parts)
        x = _interval(left, right)
        f0 = (
            pi / 2 * x**9
            - mathsf_a * x**8
            - pi**2 / 12 * x**6
            + mathsf_b * x**4
            + (iv.mpf(3) / 4 - pi / 2) * x**3
            + pi**2 / 6
            - iv.mpf(1) / 4
        )
        d0 = (
            pi / 12 * (3 * x**6 - 5 + 4 * x**-6)
            + iv.mpf(1) / 2 * (x**3 - x**-3)
            - c1 * x**2
            + c2 * x**-2
        )
        min_f = min(min_f, float(f0.a))
        min_d = min(min_d, float(d0.a))

    assert min_f > 0
    assert min_d > 0
    return {
        "parts": parts,
        "minimum_F0_lower_endpoint": min_f,
        "minimum_D0_lower_endpoint": min_d,
    }


def main() -> None:
    exact = exact_rational_checks()
    intervals = interval_base_regression()
    print(
        json.dumps(
            {
                "exact_checks": {
                    key: str(value) for key, value in exact.items()
                },
                "interval_regression": intervals,
                "role": "optional regression; not a proof premise",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
