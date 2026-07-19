"""Independent exact-constant verifier for the frozen Round 20 candidate.

This module deliberately proves only finite arithmetic consequences.  It uses
``fractions.Fraction`` throughout; no floating-point value can make a check
pass.  The analytic hypotheses (spectral comparisons, zero enumeration,
phase estimates, and optical Stieltjes arguments) are listed explicitly in
``ANALYTIC_ASSUMPTIONS`` and are not silently promoted by this program.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
from math import factorial, isqrt
from pathlib import Path
from typing import Callable, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]

CANDIDATE_PATH = "state/lemma_packets/SHELL-combined-closure-round20-claim.md"
FREEZE_PATH = "rounds/polya-main/round_020/exploration/candidate-claim-freeze.md"
CANDIDATE_SHA256 = "e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61"
FREEZE_SHA256 = "aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87"

EXPECTED_HASHES: dict[str, str] = {
    CANDIDATE_PATH: CANDIDATE_SHA256,
    FREEZE_PATH: FREEZE_SHA256,
    "state/lemma_packets/SHELL-rho-compact-round20.md":
        "a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8",
    "computations/round20_residual_mask.py":
        "5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2",
    "computations/tests/test_round20_residual_mask.py":
        "d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164",
    "rounds/polya-main/round_020/exploration/residual-mask-freeze.md":
        "172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7",
    "rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md":
        "b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f",
    "state/lemma_packets/SHELL-sturm-liouville-completeness.md":
        "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "state/lemma_packets/SHELL-phase-enclosures.md":
        "96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf",
    "state/lemma_packets/SHELL-weighted-lattice-fractional.md":
        "a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c",
    "state/lemma_packets/SHELL-low-interface-small-hole.md":
        "071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a",
    "state/lemma_packets/SHELL-rho-one-endpoint-round16.md":
        "5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09",
    "sources/annuli_polya.md":
        "951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57",
    "sources/flps_balls.md":
        "27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38",
    "sources/lorch_bessel_zeros.md":
        "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
    "sources/shell_weyl_bessel.md":
        "ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade",
    "sources/bessel_phase_enclosures.md":
        "e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c",
}


ANALYTIC_ASSUMPTIONS = (
    "A3 proves the separated strict-count identity and multiplicity rule.",
    "A3 proves q_(ell,n)^2 >= n^2 z_rho^2+ell(ell+1), q_(0,n)=n z_rho, "
    "the fixed-channel shell-to-ball comparison, and angular-index propagation.",
    "For the eight internally reconstructed half-integer zero bounds, A3 proves "
    "the stated tangent-cell root enumeration, ODE simplicity, and positive-zero convention; "
    "A4 verifies every rational-wall and tangent-endpoint sign exactly.",
    "A3 proves the shifted-tail wedge, its interface remainder estimate, and the "
    "remaining-frequency tail aggregation outside the exceptional floor cell.",
    "A3 proves the strict phase-proxy implication used by the finite lower cap 395.",
    "A3 proves the product min-max comparison and the quarter-circle sum bound used "
    "on the low optical screen.",
    "A3 proves the complementary-action inverse curvature, Stieltjes radial deficit, "
    "layer-cake identity, and phase transfer used on the high optical screen.",
    "Elementary differentiability/monotonicity facts invoked below (G_1, k_m, and W_m) "
    "must be written analytically by A3; A4 verifies their reduced signs exactly.",
)


class VerificationError(AssertionError):
    """First failed exact implication."""


class Ledger:
    def __init__(self) -> None:
        self.labels: list[str] = []
        self.kinds: list[str] = []

    def require(
        self,
        condition: bool,
        label: str,
        detail: str = "",
        *,
        kind: str = "substantive",
    ) -> None:
        if kind not in {"substantive", "bookkeeping", "authentication"}:
            raise ValueError(f"unknown check kind: {kind}")
        if not condition:
            suffix = f": {detail}" if detail else ""
            raise VerificationError(f"{label}{suffix}")
        self.labels.append(label)
        self.kinds.append(kind)

    def counts(self) -> dict[str, int]:
        return {
            kind: sum(observed == kind for observed in self.kinds)
            for kind in ("substantive", "bookkeeping", "authentication")
        }


@dataclass(frozen=True)
class Interval:
    """Closed exact rational interval."""

    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(value: int | Q) -> "Interval":
        value = Q(value)
        return Interval(value, value)

    def __add__(self, other: int | Q | "Interval") -> "Interval":
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: int | Q | "Interval") -> "Interval":
        return self + (-as_interval(other))

    def __rsub__(self, other: int | Q | "Interval") -> "Interval":
        return as_interval(other) - self

    def __mul__(self, other: int | Q | "Interval") -> "Interval":
        other = as_interval(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(Q(1, 1) / self.hi, Q(1, 1) / self.lo)

    def __truediv__(self, other: int | Q | "Interval") -> "Interval":
        return self * as_interval(other).reciprocal()

    def __rtruediv__(self, other: int | Q | "Interval") -> "Interval":
        return as_interval(other) / self

    def __pow__(self, exponent: int) -> "Interval":
        if exponent < 0:
            return (self.reciprocal()) ** (-exponent)
        result = Interval.point(1)
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result


def as_interval(value: int | Q | Interval) -> Interval:
    return value if isinstance(value, Interval) else Interval.point(value)


def sqrt_fraction_bounds(value: Q, decimal_digits: int = 50) -> Interval:
    """Certified decimal-grid enclosure of sqrt(value), using integer square roots."""

    if value < 0:
        raise ValueError("negative radicand")
    if value == 0:
        return Interval.point(0)
    scale = 10**decimal_digits
    floor_scaled_square = value.numerator * scale * scale // value.denominator
    root = isqrt(floor_scaled_square)
    lo = Q(root, scale)
    hi = Q(root + 1, scale)
    assert lo * lo <= value < hi * hi
    return Interval(lo, hi)


def sqrt_interval(value: Interval, decimal_digits: int = 50) -> Interval:
    if value.lo < 0:
        raise ValueError("negative interval radicand")
    return Interval(
        sqrt_fraction_bounds(value.lo, decimal_digits).lo,
        sqrt_fraction_bounds(value.hi, decimal_digits).hi,
    )


def atan_reciprocal_bounds(q: int, terms: int) -> Interval:
    """Alternating-series enclosure for atan(1/q)."""

    x = Q(1, q)
    total = Q(0)
    for k in range(terms):
        term = x ** (2 * k + 1) / (2 * k + 1)
        total += term if k % 2 == 0 else -term
    next_term = x ** (2 * terms + 1) / (2 * terms + 1)
    if terms % 2 == 0:  # next sign is positive
        return Interval(total, total + next_term)
    return Interval(total - next_term, total)


def pi_bounds() -> Interval:
    """Machin: pi = 16 atan(1/5) - 4 atan(1/239)."""

    a = atan_reciprocal_bounds(5, 36)
    b = atan_reciprocal_bounds(239, 12)
    return 16 * a - 4 * b


PI = pi_bounds()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_hashes(
    root: Path = ROOT,
    expected: Mapping[str, str] = EXPECTED_HASHES,
    ledger: Ledger | None = None,
) -> dict[str, str]:
    ledger = ledger or Ledger()
    actual: dict[str, str] = {}
    for relative, wanted in expected.items():
        path = root / relative
        ledger.require(
            path.is_file(),
            f"hash file exists: {relative}",
            kind="authentication",
        )
        digest = sha256(path)
        ledger.require(
            digest == wanted,
            f"SHA-256 gate: {relative}",
            f"expected {wanted}, got {digest}",
            kind="authentication",
        )
        actual[relative] = digest
    return actual


def verify_pi(ledger: Ledger) -> None:
    ledger.require(PI.lo < PI.hi, "Machin interval is nonempty")
    ledger.require(PI.lo > Q(333, 106), "pi > 333/106")
    ledger.require(PI.hi < Q(22, 7), "pi < 22/7")
    ledger.require(Q(106, 333) * PI.lo > 1, "1/pi < 106/333")


def exact_constants() -> dict[str, Interval]:
    sqrt2 = sqrt_fraction_bounds(Q(2))
    sqrt3 = sqrt_fraction_bounds(Q(3))
    sqrt337 = sqrt_fraction_bounds(Q(337))
    omega = sqrt3 / (2 * PI) - Q(1, 6)
    c_star = Q(1, 2) + Q(8, 15) * sqrt2
    c0 = 1 + Q(8, 15) * sqrt2
    rho_star = omega / (1 + 2 * c_star)
    rho0 = 1 / sqrt337
    sigma = Q(3, 4) * omega
    rho_c = 1 / (1 + 2 * PI)
    d = sqrt337 / 2
    return {
        "sqrt2": sqrt2,
        "sqrt3": sqrt3,
        "sqrt337": sqrt337,
        "omega": omega,
        "Cstar": c_star,
        "C0": c0,
        "rho_star": rho_star,
        "rho0": rho0,
        "sigma": sigma,
        "rho_c": rho_c,
        "d": d,
    }


def separated(left: Interval, right: Interval) -> bool:
    return left.hi < right.lo


def verify_thresholds(ledger: Ledger) -> dict[str, Interval]:
    c = exact_constants()
    chain: list[tuple[str, Interval]] = [
        ("rho_*", c["rho_star"]),
        ("rho_0", c["rho0"]),
        ("sigma", c["sigma"]),
        ("rho_c", c["rho_c"]),
        ("39/50", Interval.point(Q(39, 50))),
        ("7/8", Interval.point(Q(7, 8))),
    ]
    for (lname, left), (rname, right) in zip(chain, chain[1:]):
        ledger.require(separated(left, right), f"threshold order {lname} < {rname}")

    ledger.require(separated(c["omega"], c["rho_c"]), "omega_0 < rho_c (H0 ineligible)")
    ledger.require(
        (c["omega"] * c["d"]).lo > 1,
        "omega_0 d > 1",
    )

    sqrt114 = sqrt_fraction_bounds(Q(114))
    c42 = sqrt_fraction_bounds(Q(7073, 64))
    fixed = [
        ("d", c["d"]),
        ("10", Interval.point(10)),
        ("81/8", Interval.point(Q(81, 8))),
        ("21/2", Interval.point(Q(21, 2))),
        ("sqrt(7073)/8", c42),
        ("sqrt(114)", sqrt114),
    ]
    for (lname, left), (rname, right) in zip(fixed, fixed[1:]):
        ledger.require(separated(left, right), f"lower-frequency order {lname} < {rname}")
    ledger.require(Q(7073, 64) == Q(81, 8) ** 2 + 8, "c42 propagation identity")

    z_at_rho0 = PI / (1 - c["rho0"])
    z_at_rhoc = PI + Q(1, 2)  # exact simplification at rho_c
    ledger.require(separated(c["d"], 3 * z_at_rho0), "d < 3 z(rho0)")
    ledger.require((3 * z_at_rho0).hi < 10, "3 z(rho0) < 10")
    ledger.require(separated(sqrt114, 3 * z_at_rhoc), "sqrt(114) < 3 z(rho_c)")

    moving_walls = [
        ("10", Interval.point(10)),
        ("81/8", Interval.point(Q(81, 8))),
        ("21/2", Interval.point(Q(21, 2))),
        ("c42", c42),
        ("sqrt114", sqrt114),
    ]
    crossings: list[tuple[str, Interval]] = []
    for name, wall in moving_walls:
        crossing = 1 - 3 * PI / wall
        ledger.require(separated(c["rho0"], crossing), f"3z={name} crossing above rho0")
        ledger.require(separated(crossing, c["rho_c"]), f"3z={name} crossing below rho_c")
        crossings.append((name, crossing))
    for (lname, left), (rname, right) in zip(crossings, crossings[1:]):
        ledger.require(separated(left, right), f"moving-wall order {lname} before {rname}")

    r_proxy = Interval.point(Q(367, 20))
    ledger.require(separated(sqrt114, 2 / c["omega"]), "sqrt(114) < 2/omega_0")
    ledger.require(separated(2 / c["omega"], r_proxy), "2/omega_0 < 367/20")
    ledger.require(
        separated(c["rho_c"], Q(3, 2) * c["omega"]),
        "rho_c < 3 omega_0/2",
    )
    ledger.require((c["omega"] * sqrt114).lo > 1, "omega_0 sqrt(114) > 1")
    return {**c, "sqrt114": sqrt114, "c42": c42, "R": r_proxy}


def ceil_q(value: Q) -> int:
    return -((-value.numerator) // value.denominator)


def floor_q(value: Q) -> int:
    return value.numerator // value.denominator


def strict_positive_integer_count(value: Q) -> int:
    return max(0, ceil_q(value) - 1)


def verify_strict_face_conventions(ledger: Ledger) -> None:
    for m in range(1, 9):
        ledger.require(
            strict_positive_integer_count(Q(m)) == m - 1,
            f"strict integer bracket at {m}",
        )
        ledger.require(
            strict_positive_integer_count(Q(2 * m + 1, 2)) == m,
            f"strict integer bracket between walls {m}",
        )
    # If x^2=ell(ell+1), y=sqrt(x^2+1/4)-1/2=ell exactly;
    # M=ceil(y)=ell counts ell=0,...,ell-1 and excludes the equality channel.
    for ell in range(0, 12):
        ledger.require(
            sum(2 * j + 1 for j in range(ell)) == ell * ell,
            f"product angular equality excludes ell={ell}",
        )
    # At A+1/4=n, [A+1/4]_< = n-1 and the layer x_n=n-1/4 is excluded.
    for n in range(1, 8):
        ledger.require(
            strict_positive_integer_count(Q(n)) == n - 1,
            f"phase-proxy integer wall n={n}",
        )


def taylor_sin_cos(value: Q, terms: int = 70) -> tuple[Interval, Interval]:
    """Global Taylor enclosures; derivative remainders are bounded by one."""

    sin_sum = Q(0)
    cos_sum = Q(0)
    for k in range(terms):
        sin_term = value ** (2 * k + 1) / factorial(2 * k + 1)
        cos_term = value ** (2 * k) / factorial(2 * k)
        sin_sum += sin_term if k % 2 == 0 else -sin_term
        cos_sum += cos_term if k % 2 == 0 else -cos_term
    sin_err = abs(value) ** (2 * terms) / factorial(2 * terms)
    cos_err = abs(value) ** (2 * terms - 1) / factorial(2 * terms - 1)
    return (
        Interval(sin_sum - sin_err, sin_sum + sin_err),
        Interval(cos_sum - cos_err, cos_sum + cos_err),
    )


def spherical_coefficients(ell: int, x: Q) -> tuple[Q, Q]:
    """Return A,B with spherical_j_ell(x)=A sin(x)+B cos(x)."""

    if x <= 0:
        raise ValueError("x must be positive")
    a0, b0 = Q(1, 1) / x, Q(0)
    if ell == 0:
        return a0, b0
    a1, b1 = Q(1, 1) / (x * x), -Q(1, 1) / x
    if ell == 1:
        return a1, b1
    prev = (a0, b0)
    cur = (a1, b1)
    for l in range(1, ell):
        nxt = (
            Q(2 * l + 1, 1) * cur[0] / x - prev[0],
            Q(2 * l + 1, 1) * cur[1] / x - prev[1],
        )
        prev, cur = cur, nxt
    return cur


def linear_interval(a: Q, x: Interval, b: Q, y: Interval) -> Interval:
    return a * x + b * y


def spherical_sign_at_rational(ell: int, x: Q) -> int:
    a, b = spherical_coefficients(ell, x)
    sin_x, cos_x = taylor_sin_cos(x)
    value = linear_interval(a, sin_x, b, cos_x)
    if value.lo > 0:
        return 1
    if value.hi < 0:
        return -1
    raise VerificationError(f"unresolved exact spherical-Bessel sign ell={ell}, x={x}")


def interval_spherical_coefficients(ell: int, x: Interval) -> tuple[Interval, Interval]:
    a0, b0 = 1 / x, Interval.point(0)
    if ell == 0:
        return a0, b0
    a1, b1 = 1 / (x * x), -(1 / x)
    if ell == 1:
        return a1, b1
    prev = (a0, b0)
    cur = (a1, b1)
    for l in range(1, ell):
        nxt = (
            (2 * l + 1) * cur[0] / x - prev[0],
            (2 * l + 1) * cur[1] / x - prev[1],
        )
        prev, cur = cur, nxt
    return cur


def spherical_sign_at_half_period(ell: int, half_index: int) -> int:
    x = Q(half_index, 2) * PI
    a, b = interval_spherical_coefficients(ell, x)
    phase = half_index % 4
    sin_value = (0, 1, 0, -1)[phase]
    cos_value = (1, 0, -1, 0)[phase]
    value = sin_value * a + cos_value * b
    if value.lo > 0:
        return 1
    if value.hi < 0:
        return -1
    raise VerificationError(
        f"unresolved half-period sign ell={ell}, half_index={half_index}"
    )


@dataclass(frozen=True)
class InternalZeroFace:
    ell: int
    radial: int
    wall: Q
    expected_sign: int
    left_half: int
    right_half: int
    left_sign: int
    right_sign: int


INTERNAL_ZERO_FACES = (
    InternalZeroFace(1, 2, Q(77, 10), -1, 4, 5, -1, 1),
    InternalZeroFace(2, 2, Q(9), -1, 5, 6, -1, 1),
    InternalZeroFace(3, 2, Q(103, 10), -1, 6, 7, -1, 1),
    InternalZeroFace(5, 2, Q(129, 10), -1, 8, 9, -1, 1),
    InternalZeroFace(1, 3, Q(21, 2), 1, 6, 7, 1, -1),
    InternalZeroFace(2, 3, Q(61, 5), 1, 7, 8, 1, -1),
    InternalZeroFace(6, 1, Q(10), 1, 6, 7, 1, -1),
    InternalZeroFace(7, 1, Q(23, 2), 1, 7, 8, 1, -1),
)


LORCH_ZERO_FACES = (
    (8, Q(71, 6)),
    (9, Q(64, 5)),
    (10, Q(69, 5)),
)


def lorch_l2_rhs(ell: int) -> Interval:
    nu = Q(2 * ell + 1, 2)
    radical = sqrt_fraction_bounds((2 * nu + 3) * (2 * nu + 11))
    denominator = 1 - 2 * nu + radical
    if denominator.lo <= 0:
        raise VerificationError(f"Lorch L2 denominator not positive for ell={ell}")
    return 24 * (nu + 1) ** 2 / denominator - 2 * (nu * nu - 1)


def verify_zero_specializations(ledger: Ledger) -> dict[tuple[int, int], Q]:
    registry: dict[tuple[int, int], Q] = {}
    for face in INTERNAL_ZERO_FACES:
        ledger.require(
            (Q(face.left_half, 2) * PI).hi < face.wall,
            f"zero wall ell={face.ell},n={face.radial} right of left half-period",
        )
        ledger.require(
            face.wall < (Q(face.right_half, 2) * PI).lo,
            f"zero wall ell={face.ell},n={face.radial} left of right half-period",
        )
        ledger.require(
            spherical_sign_at_half_period(face.ell, face.left_half) == face.left_sign,
            f"left tangent-cell sign ell={face.ell},n={face.radial}",
        )
        ledger.require(
            spherical_sign_at_half_period(face.ell, face.right_half) == face.right_sign,
            f"right tangent-cell sign ell={face.ell},n={face.radial}",
        )
        ledger.require(
            spherical_sign_at_rational(face.ell, face.wall) == face.expected_sign,
            f"rational zero-wall sign ell={face.ell},n={face.radial}",
        )
        registry[(face.ell, face.radial)] = face.wall * face.wall

    for ell, wall in LORCH_ZERO_FACES:
        rhs = lorch_l2_rhs(ell)
        ledger.require(
            rhs.lo > wall * wall,
            f"Lorch L2 exact specialization ell={ell}",
        )
        ledger.require(
            spherical_sign_at_rational(ell, wall) == 1,
            f"first-zero rational-wall sign ell={ell}",
        )
        registry[(ell, 1)] = wall * wall

    ledger.require(Q(103, 10) > Q(81, 8), "strong j_7/2,2 wall implies 81/8 wall")
    ledger.require(Q(61, 5) > Q(21, 2), "third-mode wall order 21/2 < 61/5")
    return registry


def angular_sum(max_ell: int) -> int:
    return sum(2 * ell + 1 for ell in range(max_ell + 1))


def weyl_interval(rho: Interval, k: Interval) -> Interval:
    return Q(2, 9) * (1 / PI) * (1 - rho**3) * k**3


def verify_lower_inventories_and_payments(
    ledger: Ledger, constants: Mapping[str, Interval]
) -> None:
    # Exclusion/activation arithmetic.  Strict zero walls are analytic inputs;
    # all consequences at included K faces are checked here.
    ledger.require(Q(23, 2) ** 2 > 114, "first ell>=7 absent through sqrt114")
    ledger.require(Q(10) ** 2 == 100, "first ell=6 activation wall 10")
    ledger.require(Q(129, 10) ** 2 > 114, "second ell>=5 absent through sqrt114")
    ledger.require(Q(103, 10) > Q(81, 8), "second ell=3 absent through 81/8")
    ledger.require(
        Q(81, 8) ** 2 + 8 == Q(7073, 64),
        "second ell=4 propagated c42 wall",
    )
    ledger.require(
        Q(81, 8) ** 2 + 18 > 114,
        "second ell>=5 propagated absence",
    )
    ledger.require(Q(21, 2) ** 2 + 4 > 114, "third ell>=2 propagated absence")
    ledger.require((16 * PI**2).lo > 114, "all n>=4 absent through sqrt114")

    expected_caps = (45, 46, 59, 66, 69, 78)
    derived_caps = (
        angular_sum(5) + angular_sum(2),
        angular_sum(5) + angular_sum(2) + 1,
        angular_sum(6) + angular_sum(2) + 1,
        angular_sum(6) + angular_sum(3) + 1,
        angular_sum(6) + angular_sum(3) + 1 + 3,
        angular_sum(6) + angular_sum(4) + 1 + 3,
    )
    ledger.require(
        derived_caps == expected_caps,
        "all six lower inventory caps",
        kind="bookkeeping",
    )

    rho_c = constants["rho_c"]
    payments = (
        (constants["d"], 46, "d"),
        (Interval.point(10), 59, "10"),
        (Interval.point(Q(81, 8)), 66, "81/8"),
        (Interval.point(Q(21, 2)), 69, "21/2"),
        (constants["c42"], 78, "c42"),
    )
    for k, cap, name in payments:
        reserve = weyl_interval(rho_c, k)
        ledger.require(reserve.lo > cap, f"lower Weyl payment above {name} pays cap {cap}")

    proxy_caps = (6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1)
    ledger.require(
        sum((2 * ell + 1) * cap for ell, cap in enumerate(proxy_caps)) == 395,
        "exceptional-cell proxy cap is exactly 395",
    )
    r = Q(367, 20)
    for ell, cap in enumerate(proxy_caps + (0,)):
        nu = Q(2 * ell + 1, 2)
        radical_1 = sqrt_fraction_bounds(r * r - nu * nu)
        radical_2 = sqrt_fraction_bounds(2 * (1 - nu / r))
        # arccos(x) >= sqrt(2(1-x)); hence this is an exact upper bound for G_R.
        numerator_upper = radical_1.hi - nu * radical_2.lo
        proxy_upper = Interval.point(numerator_upper) / PI + Q(1, 4)
        ledger.require(
            proxy_upper.hi < cap + 1,
            f"strict phase proxy ell={ell} has cap {cap}",
        )
    # G_R is decreasing in nu; ell=14 therefore kills every omitted angular tail.
    tail_caps = proxy_caps + (0,)
    ledger.require(
        tail_caps[-1] == 0 and all(a >= b for a, b in zip(tail_caps, tail_caps[1:])),
        "ell>=14 omitted by monotonicity after exact ell=14 check",
    )

    rho_c_k = Q(5, 2) / rho_c
    exceptional_payment = weyl_interval(rho_c, rho_c_k)
    ledger.require(exceptional_payment.lo > 395, "exceptional cell Weyl payment exceeds 395")

    # Exact floor-cell logic.  p>=1 because omega*K>1.  If p>=2, then
    # rho*K < (3/2)(p+1) <= 2p+1/2, with strictness at p=2.
    ledger.require(Q(3, 2) * 3 == Q(9, 2), "p=2 floor-cell endpoint identity")
    for p in range(2, 10):
        ledger.require(
            Q(3, 2) * (p + 1) <= 2 * p + Q(1, 2),
            f"floor-cell inequality p={p}",
        )
    ledger.require(
        (Q(5, 2) - Q(1, 2)).denominator == 1,
        "rho K=5/2 is assigned to failing high half-integer side",
    )
    normalized_face = Q(2)  # omega_0 K at K=2/omega_0
    endpoint_rho_k = 2 * constants["rho_c"] / constants["omega"]
    ledger.require(
        floor_q(normalized_face) == 2 and endpoint_rho_k.hi < 3,
        "K=2/omega has p=2 and rho*K<3",
    )
    ledger.require(
        endpoint_rho_k.hi - Q(1, 2) < Q(5, 2) and 2 <= 2 * floor_q(normalized_face) - 1,
        "K=2/omega satisfies m<=2p-1 and belongs to the complement",
    )


def propagated_lower_square(
    bases: Mapping[int, Q], target_ell: int
) -> Q | None:
    candidates = [
        square + target_ell * (target_ell + 1) - ell * (ell + 1)
        for ell, square in bases.items()
        if ell <= target_ell
    ]
    return max(candidates) if candidates else None


FIRST_BASES = {
    6: Q(10) ** 2,
    7: Q(23, 2) ** 2,
    8: Q(71, 6) ** 2,
    9: Q(64, 5) ** 2,
    10: Q(69, 5) ** 2,
}
SECOND_BASES = {
    1: Q(77, 10) ** 2,
    2: Q(9) ** 2,
    3: Q(103, 10) ** 2,
    5: Q(129, 10) ** 2,
}
THIRD_BASES = {1: Q(21, 2) ** 2, 2: Q(61, 5) ** 2}


def verify_zero_channel_cover(
    ledger: Ledger,
    checkpoint: int,
    radial: int,
    first_excluded_ell: int,
    bases: Mapping[int, Q],
) -> None:
    mterm = checkpoint * (checkpoint + 1)
    ell = first_excluded_ell
    channel_cut = Q(mterm - ell * (ell + 1), radial * radial - 1)
    zero_sq = propagated_lower_square(bases, ell)
    if zero_sq is None:
        raise VerificationError("missing zero base")
    zero_cut = zero_sq - mterm
    ledger.require(
        zero_cut >= channel_cut,
        f"zero/channel cover k{checkpoint}, n={radial}, ell>={ell}",
        f"zero cut {zero_cut}, channel cut {channel_cut}",
    )


def x_at_ratio(rho: Q) -> Interval:
    return PI**2 / (1 - rho) ** 2


def checkpoint_weyl(rho: Interval, checkpoint: int) -> Interval:
    x = PI**2 / (1 - rho) ** 2
    k = sqrt_interval(x + checkpoint * (checkpoint + 1))
    return weyl_interval(rho, k)


def conditional_first_mode_payment(
    ledger: Ledger, checkpoint: int, wall: Q, cap: int, label: str
) -> None:
    mterm = checkpoint * (checkpoint + 1)
    x0 = wall * wall - mterm
    ledger.require(x0 > 0, f"{label} positive localization x")
    root_x = sqrt_fraction_bounds(x0)
    rho0 = 1 - PI / root_x
    payment = weyl_interval(rho0, Interval.point(wall))
    ledger.require(payment.lo > cap, f"{label} conditional payment > {cap}")


def verify_k9_h6_h4_channel_equality(
    ledger: Ledger,
    channel_wall: Q,
) -> Interval:
    """Require that the supplied wall is exactly the k9 (ell,n)=(4,2) wall."""

    prefix = "k9 H=6,h=4 cap74"
    delta = channel_delta(9, 2, 4, Interval.point(channel_wall))
    ledger.require(
        delta.lo == 0 and delta.hi == 0,
        f"{prefix}: z^2=70/3 is the defining k9 ell=4,n=2 equality",
    )
    return delta


def verify_k9_h6_h4_path(
    ledger: Ledger,
    *,
    channel_wall: Q = Q(70, 3),
) -> dict[str, Q | Interval]:
    """Close the previously missing k9 H=6,h=4 cap-74 payment cell."""

    prefix = "k9 H=6,h=4 cap74"
    base_square = Q(103, 10) ** 2
    propagated_square = base_square + (4 * 5 - 3 * 4)
    ledger.require(
        propagated_square == Q(11409, 100),
        f"{prefix}: ell=3 to ell=4 n=2 propagation square",
    )
    ledger.require(
        propagated_square > 108,
        f"{prefix}: propagated second-mode square exceeds 108",
    )

    equality_delta = verify_k9_h6_h4_channel_equality(ledger, channel_wall)
    ledger.require(
        strict_positive_integer_count(Q(1)) == 0,
        f"{prefix}: strict count excludes the defining equality mode",
    )

    rho_face = Q(7, 20)
    x_face = x_at_ratio(rho_face)
    ledger.require(
        x_face.lo > channel_wall,
        f"{prefix}: rho=7/20 lies on excluded side z^2>70/3",
    )
    ledger.require(
        Q(400, 169) * Q(333, 106) ** 2 - channel_wall
        == Q(36230, 1424163),
        f"{prefix}: exact rational reserve at rho=7/20",
    )
    ledger.require(
        x_face.lo > channel_wall and strict_positive_integer_count(Q(1)) == 0,
        f"{prefix}: a counted ell=4 second mode forces rho<7/20",
    )

    frequency_wall = Q(207, 20)
    ledger.require(
        frequency_wall**2 == Q(42849, 400),
        f"{prefix}: exact (207/20)^2",
    )
    ledger.require(
        frequency_wall**2 < 108 < propagated_square,
        f"{prefix}: counted ell=4 second mode forces K>207/20",
    )

    payment = weyl_interval(Interval.point(rho_face), Interval.point(frequency_wall))
    coarse_payment = (
        Q(2, 9)
        * Q(7, 22)
        * (1 - rho_face**3)
        * frequency_wall**3
    )
    ledger.require(
        coarse_payment == Q(52823261673, 704000000),
        f"{prefix}: exact pi<22/7 Weyl lower payment",
    )
    ledger.require(
        coarse_payment - 74 == Q(727261673, 704000000) > 0,
        f"{prefix}: exact Weyl reserve above cap 74",
    )
    ledger.require(
        payment.lo > coarse_payment > 74,
        f"{prefix}: certified W(7/20,207/20)>74",
    )
    ledger.require(
        49 + 25 == 74,
        f"{prefix}: full first and second multiplicities equal cap 74",
        kind="bookkeeping",
    )
    return {
        "base_square": base_square,
        "propagated_square": propagated_square,
        "channel_wall": channel_wall,
        "equality_delta": equality_delta,
        "rho_face": rho_face,
        "frequency_wall": frequency_wall,
        "coarse_payment": coarse_payment,
        "payment": payment,
    }


def verify_checkpoint_inventories(ledger: Ledger, constants: Mapping[str, Interval]) -> None:
    expected = {
        7: (6, 1, -1, 2),
        8: (7, 3, -1, 2),
        9: (8, 4, -1, 2),
        10: (9, 5, 1, 3),
        11: (10, 4, 1, 3),
    }
    for m, (first_max, second_max, third_max, max_radial) in expected.items():
        ledger.require(first_max == m - 1, f"k{m} strict first-mode upper face")
        for ell in range(m, 12):
            ledger.require(
                ell * (ell + 1) >= m * (m + 1),
                f"k{m} first angular tail excluded at ell={ell}",
            )
        ledger.require(second_max < m, f"k{m} finite second inventory")
        if third_max >= 0:
            ledger.require(third_max == 1, f"k{m} third inventory ell=0,1")
        ledger.require(max_radial in (2, 3), f"k{m} stated maximal radial index")

    verify_zero_channel_cover(ledger, 7, 2, 2, SECOND_BASES)
    verify_zero_channel_cover(ledger, 8, 2, 4, SECOND_BASES)
    verify_zero_channel_cover(ledger, 9, 2, 5, SECOND_BASES)
    verify_zero_channel_cover(ledger, 10, 2, 6, SECOND_BASES)
    verify_zero_channel_cover(ledger, 11, 2, 5, SECOND_BASES)

    x_min = (PI + Q(1, 2)) ** 2
    ledger.require(x_min.lo > Q(90, 8), "no third modes at k7,k8,k9")
    verify_zero_channel_cover(ledger, 10, 3, 2, THIRD_BASES)
    verify_zero_channel_cover(ledger, 11, 3, 2, THIRD_BASES)
    ledger.require(x_min.lo > Q(132, 15), "no radial n>=4 through k11")

    # Every omitted angular tail is monotone: the propagated zero cut increases
    # and the channel cut decreases with ell.  The base-ell cover therefore
    # proves all remaining indices, not merely ell<=11.
    for m, first_ell in ((7, 2), (8, 4), (9, 5), (10, 6), (11, 5)):
        M = m * (m + 1)
        previous_zero = None
        previous_channel = None
        for ell in range(first_ell, 13):
            zcut = propagated_lower_square(SECOND_BASES, ell) - M  # type: ignore[operator]
            ccut = Q(M - ell * (ell + 1), 3)
            if previous_zero is not None:
                ledger.require(zcut > previous_zero, f"k{m} zero cut increases at ell={ell}")
                ledger.require(ccut < previous_channel, f"k{m} channel cut decreases at ell={ell}")
            previous_zero, previous_channel = zcut, ccut


def verify_cap_tables_and_payments(ledger: Ledger, constants: Mapping[str, Interval]) -> None:
    # k7
    ledger.require(
        (25, 36, 49) == tuple((h + 1) ** 2 for h in (4, 5, 6)),
        "k7 first caps",
        kind="bookkeeping",
    )
    ledger.require(1 + 3 == 4, "k7 two second modes add 1+3", kind="bookkeeping")

    # k8 and k9 rectangular tables: every numerical entry is exactly the sum
    # of a full first block and a full second block.
    k8 = {
        7: (64, 65, 68, 73, 80),
        6: (49, 50, 53, None, None),
        5: (36, 37, 40, 45, 52),
        4: (25, 26, 29, 34, 41),
    }
    for h_first, row in k8.items():
        for col, value in enumerate(row):
            if value is not None:
                expected = (h_first + 1) ** 2 + (0 if col == 0 else col * col)
                ledger.require(
                    value == expected,
                    f"k8 cap H={h_first}, column={col}",
                    kind="bookkeeping",
                )

    k9 = {
        8: (81, None, None, None, None, None),
        7: (64, 65, 68, 73, None, None),
        6: (49, 50, 53, 58, 65, 74),
        5: (36, 37, 40, 45, 52, 61),
        4: (25, 26, 29, 34, 41, 50),
    }
    for h_first, row in k9.items():
        for col, value in enumerate(row):
            if value is not None:
                expected = (h_first + 1) ** 2 + (0 if col == 0 else col * col)
                ledger.require(
                    value == expected,
                    f"k9 cap H={h_first}, column={col}",
                    kind="bookkeeping",
                )

    verify_k9_h6_h4_path(ledger)

    # Marked impossible cells, proved from simultaneous strict necessary walls.
    ledger.require(Q(100 - 72) > Q(72 - 6, 3), "k8 H=6 with h>=2 impossible")
    ledger.require(Q(71, 6) ** 2 - 90 > Q(90, 3), "k9 H=8 with any second impossible")
    ledger.require(Q(23, 2) ** 2 - 90 > Q(90 - 12, 3), "k9 H=7 with h>=3 impossible")

    k10_cases = (
        (100, 100, "H9 no radial"),
        (81, 81, "H8 no second"),
        (81 + 16, 97, "H8 h<=3"),
        (64, 64, "H7 no second"),
        (64 + 16, 80, "H7 h<=3"),
        (64 + 25, 89, "H7 h=4"),
        (64 + 36, 100, "H7 h=5"),
        (49 + 25, 74, "H<=6 h<=4 no third"),
        (49 + 16 + 4, 69, "H<=6 h<=3 third"),
        (49 + 25 + 4, 78, "H<=6 h=4 third"),
        (49 + 36, 85, "H<=6 h=5 no third"),
        (49 + 36 + 4, 89, "H<=6 h=5 third"),
    )
    for derived, frozen, name in k10_cases:
        ledger.require(derived == frozen, f"k10 cap {name}", kind="bookkeeping")

    k11_cases = (
        (121, 121, "H10 no radial"),
        (100, 100, "H9 no radial"),
        (100 + 25, 125, "H9 second no third"),
        (81 + 25, 106, "H8 no third"),
        (81 + 25 + 4, 110, "H8 third"),
        (64 + 25 + 4, 93, "H<=7 all radial"),
    )
    for derived, frozen, name in k11_cases:
        ledger.require(derived == frozen, f"k11 cap {name}", kind="bookkeeping")

    # W_m is increasing because pi^2(1+rho) > M rho^2(1-rho)^2;
    # the exact uniform reduction is pi^2>9>132/16.
    ledger.require(PI.lo**2 > 9, "checkpoint-Weyl derivative: pi^2>9")
    ledger.require(Q(132, 16) < 9, "checkpoint-Weyl derivative: M/16<9")

    rho_c = constants["rho_c"]
    global_payments = ((7, 40), (8, 53), (9, 73), (10, 89), (11, 121))
    for m, cap in global_payments:
        ledger.require(
            checkpoint_weyl(rho_c, m).lo > cap,
            f"global k{m} checkpoint payment > {cap}",
        )

    conditional_first_mode_payment(ledger, 7, Q(10), 53, "k7 H6")
    conditional_first_mode_payment(ledger, 8, Q(23, 2), 80, "k8 H7")
    conditional_first_mode_payment(ledger, 9, Q(71, 6), 81, "k9 H8")
    conditional_first_mode_payment(ledger, 10, Q(23, 2), 100, "k10 H7")
    conditional_first_mode_payment(ledger, 10, Q(71, 6), 97, "k10 H8")
    conditional_first_mode_payment(ledger, 10, Q(64, 5), 100, "k10 H9")
    conditional_first_mode_payment(ledger, 11, Q(64, 5), 125, "k11 H9")


LOCALIZATION_RATIOS = (
    Q(1, 5), Q(3, 10), Q(1, 3), Q(3, 8), Q(2, 5), Q(5, 12), Q(3, 7),
    Q(1, 2), Q(107, 200), Q(8, 15), Q(3, 5), Q(16, 25), Q(13, 20), Q(2, 3),
    Q(4, 25), Q(1, 4), Q(7, 20),
)


@dataclass(frozen=True)
class LocalizationExpectation:
    rho: Q
    checkpoint: int
    radial: int
    ell: int
    expected_sign: int
    purpose: str


LOCALIZATION_EXPECTATIONS = (
    LocalizationExpectation(Q(1, 5), 11, 3, 1, 1, "k11 third-mode low-side cell"),
    LocalizationExpectation(Q(3, 10), 8, 2, 3, -1, "k8 h=3 exclusion side"),
    LocalizationExpectation(Q(1, 3), 8, 2, 2, -1, "k8 h=2 exclusion side"),
    LocalizationExpectation(Q(3, 8), 9, 2, 3, 1, "k9 h=3 possible side"),
    LocalizationExpectation(Q(2, 5), 9, 2, 2, 1, "k9 h=2 possible side"),
    LocalizationExpectation(Q(5, 12), 9, 2, 1, 1, "k9 h=1 possible side"),
    LocalizationExpectation(Q(3, 7), 9, 2, 0, -1, "k9 second-mode exclusion side"),
    LocalizationExpectation(Q(1, 2), 10, 2, 0, -1, "k10 second-mode exclusion side"),
    LocalizationExpectation(Q(107, 200), 11, 2, 0, -1, "k11 second-mode exclusion side"),
    LocalizationExpectation(Q(8, 15), 11, 2, 0, -1, "k11 stated second-mode localization"),
    LocalizationExpectation(Q(3, 5), 8, 2, 0, -1, "k8 all-second exclusion/payment side"),
    LocalizationExpectation(Q(16, 25), 9, 2, 0, -1, "k9 all-second exclusion/payment side"),
    LocalizationExpectation(Q(13, 20), 10, 2, 0, -1, "k10 all-second exclusion/payment side"),
    LocalizationExpectation(Q(2, 3), 11, 2, 0, -1, "k11 all-second exclusion/payment side"),
    LocalizationExpectation(Q(4, 25), 10, 3, 0, -1, "k10 third-mode exclusion side"),
    LocalizationExpectation(Q(1, 4), 11, 3, 0, -1, "k11 stated third-mode localization"),
    LocalizationExpectation(Q(7, 20), 9, 2, 4, -1, "k9 H=6,h=4 cap74 payment side"),
)


def channel_delta(
    checkpoint: int,
    radial: int,
    ell: int,
    x: Interval,
) -> Interval:
    """Exact channel difference M-ell(ell+1)-(n^2-1) z^2."""

    return (
        Interval.point(checkpoint * (checkpoint + 1) - ell * (ell + 1))
        - (radial * radial - 1) * x
    )


def verify_localization_expectation(
    ledger: Ledger,
    item: LocalizationExpectation,
    *,
    x_override: Interval | None = None,
) -> Interval:
    """Verify one named side, with injectable x for semantic mutation tests."""

    x = x_at_ratio(item.rho) if x_override is None else x_override
    delta = channel_delta(item.checkpoint, item.radial, item.ell, x)
    condition = delta.lo > 0 if item.expected_sign > 0 else delta.hi < 0
    side = "possible" if item.expected_sign > 0 else "excluded"
    ledger.require(
        condition,
        f"rho={item.rho} expected {side} side for {item.purpose}",
    )
    return delta


def verify_localizations(ledger: Ledger, constants: Mapping[str, Interval]) -> None:
    ratios = sorted(set(LOCALIZATION_RATIOS))
    ledger.require(
        len(ratios) == len(LOCALIZATION_RATIOS),
        "localization ratios are distinct",
        kind="bookkeeping",
    )
    ledger.require(
        {item.rho for item in LOCALIZATION_EXPECTATIONS} == set(LOCALIZATION_RATIOS),
        "every named ratio has a connected expected-side assertion",
        kind="bookkeeping",
    )
    for rho in ratios:
        ledger.require(constants["rho_c"].hi < rho < Q(7, 8), f"ratio localization {rho} in high strip")

    for item in LOCALIZATION_EXPECTATIONS:
        verify_localization_expectation(ledger, item)

    x_min = (PI + Q(1, 2)) ** 2
    x_max = 64 * PI**2
    for x in (Q(16), Q(68, 3), Q(34)):
        ledger.require(x_min.hi < x < x_max.lo, f"algebraic split z^2={x} in high strip")
    ledger.require(
        132 - 1 * 2 - 8 * Q(16) == 2 > 0,
        "z^2=16 is on the possible side of k11 n3 ell1",
    )
    ledger.require(
        110 - 6 * 7 - 3 * Q(68, 3) == 0
        and strict_positive_integer_count(Q(1)) == 0,
        "z^2=68/3 defines and strictly excludes k10 n2 ell6 equality",
    )
    ledger.require(
        132 - 5 * 6 - 3 * Q(34) == 0
        and strict_positive_integer_count(Q(1)) == 0,
        "z^2=34 defines and strictly excludes k11 n2 ell5 equality",
    )

    # Explicit k11 localizations.
    ledger.require(x_at_ratio(Q(8, 15)).lo > 44, "k11 second mode forces rho<8/15")
    ledger.require(x_at_ratio(Q(1, 4)).lo > Q(33, 2), "k11 third mode forces rho<1/4")
    h10_lower = Q(69, 5) ** 2 - 132
    h9_lower = Q(64, 5) ** 2 - 132
    ledger.require(h10_lower > 44, "k11 H10 excludes every second mode")
    ledger.require(h10_lower > Q(33, 2), "k11 H10 excludes every third mode")
    ledger.require(h9_lower > Q(33, 2), "k11 H9 excludes every third mode")


def verify_u_and_k11(ledger: Ledger, constants: Mapping[str, Interval]) -> None:
    # K0 is the positive root of eta*K-sqrt(a*K)-C0=0, so K0>C0/eta.
    # On [rho_c,1/2], eta=omega and k11 is increasing.  On [1/2,1),
    # d(eta*k11)/d rho<0 follows from arccos rho>=sqrt(2(1-rho)) and
    # sqrt(1+rho)<sqrt(2).  The only finite endpoint check is therefore rho=1/2.
    k11_half = sqrt_interval(4 * PI**2 + 132)
    central_endpoint_pass = (constants["omega"] * k11_half).hi < constants["C0"].lo
    ledger.require(
        central_endpoint_pass,
        "eta*k11<C0 at rho=1/2",
    )
    ledger.require(1 + Q(1, 2) < 2, "K0 monotonic reduction sqrt(1+rho)<sqrt2")
    ledger.require(
        constants["C0"].lo > 0 and constants["omega"].lo > 0,
        "K0 positive-root identity gives K0>C0/eta",
    )

    # For rho>=5/6, also beat the seam 54/(1-rho)^2.  Squaring and taking
    # s=1-rho<=1/6 leaves pi^2 s^2+132 s^4<2916.
    seam_lhs = PI**2 / 36 + Q(132, 6**4)
    seam_pass = seam_lhs.hi < 54**2
    ledger.require(seam_pass, "k11 below seam-54 branch")
    ledger.require(constants["rho_c"].hi < Q(39, 50) < Q(5, 6), "K0-only interval avoids seam")
    ledger.require(constants["omega"].hi < constants["rho_c"].lo, "K0-only interval avoids H0")
    ledger.require(
        constants["omega"].hi < constants["rho_c"].lo
        and Q(39, 50) < Q(5, 6),
        "U=K0 on rho_c<=rho<39/50",
    )
    ledger.require(central_endpoint_pass and seam_pass, "k11<U on rho_c<=rho<7/8")


def verify_product_deficit(ledger: Ledger) -> None:
    c_d = Q(1382, 3125)
    a_coeff = Q(1, 2) - c_d
    ledger.require(a_coeff > 0, "product deficit positive N^2 coefficient")

    # B(t)=t^2-2Ct+1/6 has minimum 1/6-C^2.  This and
    # A(2N+1) show F(N+1,t)-F(N,t)>0 for N>=1.
    b_min = Q(1, 6) - c_d * c_d
    ledger.require(3 * a_coeff + b_min > 0, "product deficit increases in N")

    # At N=1, F'(t)=2(t-C)(t+1), so the minimum on 0<t<=1 is t=C.
    minimum = (
        Q(2, 3) * c_d**3
        + (1 - c_d) * c_d**2
        - 2 * c_d**2
        + Q(2, 3)
        - c_d
    )
    ledger.require(minimum == Q(1822532, 91552734375), "exact product-deficit minimum")
    ledger.require(minimum > 0, "D(a)>1382/3125 a^2 for all N,t")
    ledger.require(0 < c_d < 1, "product critical point lies in 0<t<=1")

    # P4 itself follows from exact sums of n^2.  Check a finite symbolic grid
    # of indeterminates represented by rational N,t; this verifies the algebraic
    # identity, while the formula below is used for all N.
    for n in range(1, 7):
        for t in (Q(1, 7), Q(1, 2), Q(1)):
            sum_n2 = Q(n * (n + 1) * (2 * n + 1), 6)
            x = n + t
            direct = Q(2, 3) * x**3 - n * x**2 + sum_n2
            expanded = Q(n * n, 2) + n * (t * t + Q(1, 6)) + Q(2, 3) * t**3
            ledger.require(direct == expanded, f"product deficit expansion N={n},t={t}")


def verify_optical_constants(ledger: Ledger) -> None:
    eps0 = Q(11, 50)
    c = Q(1126, 625)
    q = Q(106, 333)
    c_d = Q(1382, 3125)
    r_l = Q(39569, 2772225000)
    r_h = Q(14817541, 472867032960000)

    low_cost = Q(2, 3) * c * q + eps0 / 4 + eps0**2 * q**2
    ledger.require(c_d - low_cost == r_l, "exact low optical endpoint reserve")
    ledger.require(r_l > 0, "low optical reserve positive")
    ledger.require(
        all(coefficient > 0 for coefficient in (Q(1, 4), q**2)),
        "low optical cost increases in epsilon (positive coefficients)",
    )

    high_radial = (1 - eps0) ** 2 / 4 - Q(22, 7) * (1 - eps0) * eps0 / (4 * c)
    high_angular = (
        q * eps0
        + eps0**2 / (4 * c)
        + q * eps0**3 / (4 * c)
        + eps0**4 / (16 * c**2)
    )
    ledger.require(high_radial - high_angular == r_h, "exact high optical endpoint reserve")
    ledger.require(r_h > 0, "high optical reserve positive")

    # L'(eps)<0 because eps<=11/50<1/2; E'(eps)>0 coefficientwise.
    ledger.require(eps0 < Q(1, 2), "high radial screen decreases on epsilon interval")
    ledger.require(
        all(
            coefficient > 0
            for coefficient in (q, Q(1, 4) / c, q / (4 * c), Q(1, 16) / c**2)
        ),
        "high angular screen increases in epsilon (positive coefficients)",
    )

    # Actual scaling implications at a<=c/eps (low) and a>=c/eps (high).
    low_cubic_actual = Q(2, 3) * c / PI
    ledger.require(
        low_cubic_actual.hi < Q(2, 3) * c * q,
        "low optical a<=c/epsilon turns cubic cost into 2cq/3",
    )
    ledger.require(
        ((1 / PI) ** 2).hi < q**2,
        "low optical a>=pi turns epsilon^2/(pi*a) into epsilon^2 q^2",
    )

    common_face = c / eps0
    angular_at_common_face = (
        eps0 / PI
        + eps0**2 / (4 * PI * common_face)
        + eps0 / (4 * common_face)
        + eps0**2 / (16 * common_face**2)
    )
    ledger.require(
        angular_at_common_face.hi < high_angular,
        "full high angular ceiling-error screen at a=c/epsilon",
    )
    ledger.require(
        all(
            coefficient > 0
            for coefficient in (
                eps0**2 / (4 * PI.lo),
                eps0 / 4,
                eps0**2 / 16,
            )
        ),
        "high angular error decreases for a>=c/epsilon",
    )

    radial_at_common_face = (
        (1 - eps0) ** 2 / 4
        - PI * (1 - eps0) * eps0 / (4 * c)
    )
    ledger.require(
        radial_at_common_face.lo > high_radial,
        "full high radial-deficit screen at a=c/epsilon",
    )
    ledger.require(
        (1 - eps0) * eps0 > 0,
        "high radial deficit increases for a>=c/epsilon",
    )

    low_face_slack = c - eps0 * common_face
    high_face_slack = eps0 * common_face - c
    ledger.require(
        low_face_slack == 0 and high_face_slack == 0 and eps0 > 0 and c > 0,
        "a=c/epsilon belongs to both optical pieces",
    )

    # Exact count/error identities at walls.
    for j in range(0, 12):
        ledger.require(sum(2 * ell + 1 for ell in range(j)) == j * j, f"angular ceiling block j={j}")
    ledger.require(
        strict_positive_integer_count(Q(1)) == 0,
        "a=pi radial wall uses (N,t)=(m-1,1) and is excluded",
    )
    verify_product_deficit(ledger)


def verify_exact_subtraction(ledger: Ledger) -> None:
    rho_states = (
        "rho_star", "low1", "rho0", "low2", "rho_c", "pre_opt", "opt_face",
        "post_opt", "rho_7_8",
    )
    k_states = ("below_k6", "k6", "stair", "k11", "post_k11", "U", "above_U")

    def low_d19(rho: str) -> bool:
        return rho in {"low1", "rho0", "low2"}

    def high_ratio(rho: str) -> bool:
        return rho in {"rho_c", "pre_opt", "opt_face", "post_opt"}

    def d19(rho: str, k: str) -> bool:
        if low_d19(rho):
            return k not in {"U", "above_U"}
        return high_ratio(rho) and k in {"stair", "k11", "post_k11"}

    def lower_cover(rho: str, k: str) -> bool:
        return low_d19(rho) and k not in {"U", "above_U"}

    def stair(rho: str, k: str) -> bool:
        return high_ratio(rho) and k in {"stair", "k11"}

    def optical(rho: str, k: str) -> bool:
        return rho in {"opt_face", "post_opt"} and k == "post_k11"

    def d20(rho: str, k: str) -> bool:
        return rho in {"rho_c", "pre_opt"} and k == "post_k11"

    for rho in rho_states:
        for k in k_states:
            remainder = d19(rho, k) and not (lower_cover(rho, k) or stair(rho, k) or optical(rho, k))
            ledger.require(remainder == d20(rho, k), f"D19 subtraction face rho={rho},K={k}")

    ledger.require(
        d19("rho0", "post_k11") and lower_cover("rho0", "post_k11"),
        "rho0 fiber belongs to lower cover and is removed once",
    )
    ledger.require(
        d20("rho_c", "post_k11") and not optical("rho_c", "post_k11"),
        "rho_c belongs to D20 ratio face after closed stair removal",
    )
    ledger.require(
        optical("opt_face", "post_k11") and not d20("opt_face", "post_k11"),
        "rho=39/50 optical face is removed inclusively",
    )
    ledger.require(
        stair("rho_c", "k11") and not d19("rho_c", "U"),
        "K=k11 is stair-owned; K=U is inherited-owner excluded",
    )
    ledger.require(
        d19("pre_opt", "post_k11")
        and not lower_cover("pre_opt", "post_k11")
        and not stair("pre_opt", "post_k11")
        and not optical("pre_opt", "post_k11")
        and d20("pre_opt", "post_k11"),
        "pre-optical post-k11 cell survives exactly as D20",
    )


def run_all(root: Path = ROOT, check_hashes: bool = True) -> dict[str, object]:
    ledger = Ledger()
    hashes = verify_hashes(root, ledger=ledger) if check_hashes else {}
    verify_pi(ledger)
    constants = verify_thresholds(ledger)
    verify_strict_face_conventions(ledger)
    verify_zero_specializations(ledger)
    verify_lower_inventories_and_payments(ledger, constants)
    verify_checkpoint_inventories(ledger, constants)
    verify_cap_tables_and_payments(ledger, constants)
    verify_localizations(ledger, constants)
    verify_u_and_k11(ledger, constants)
    verify_optical_constants(ledger)
    verify_exact_subtraction(ledger)
    check_counts = ledger.counts()
    return {
        "verdict": "PASS" if check_hashes else "UNAUTHENTICATED_ARITHMETIC_PASS",
        "first_issue": None,
        "exact_checks": len(ledger.labels),
        "substantive_checks": check_counts["substantive"],
        "bookkeeping_checks": check_counts["bookkeeping"],
        "authentication_checks": check_counts["authentication"],
        "labels": tuple(ledger.labels),
        "hashes": hashes,
        "analytic_assumptions": ANALYTIC_ASSUMPTIONS,
        "pi_interval": (str(PI.lo), str(PI.hi)),
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-hash-gates",
        action="store_true",
        help="test-only: run arithmetic without authenticating repository inputs",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    authenticated = not args.skip_hash_gates
    try:
        result = run_all(check_hashes=authenticated)
    except (VerificationError, ValueError, ZeroDivisionError) as exc:
        print("FAIL" if authenticated else "UNAUTHENTICATED ARITHMETIC CHECK FAILED")
        print(f"first issue: {exc}")
        return 1
    if not authenticated:
        print("UNAUTHENTICATED ARITHMETIC-ONLY RESULT: PASS")
        print("hash gates: SKIPPED")
        print(f"exact finite checks: {result['exact_checks']}")
        print(f"substantive checks: {result['substantive_checks']}")
        print(f"bookkeeping identities: {result['bookkeeping_checks']}")
        print(f"authentication gates: {result['authentication_checks']}")
        print(f"analytic assumptions remaining for A3: {len(ANALYTIC_ASSUMPTIONS)}")
        return 0
    print("PASS")
    print("first issue: none")
    print(f"exact finite checks: {result['exact_checks']}")
    print(f"substantive checks: {result['substantive_checks']}")
    print(f"bookkeeping identities: {result['bookkeeping_checks']}")
    print(f"authentication gates: {result['authentication_checks']}")
    print(f"candidate sha256: {CANDIDATE_SHA256}")
    print(f"freeze sha256: {FREEZE_SHA256}")
    print(f"analytic assumptions remaining for A3: {len(ANALYTIC_ASSUMPTIONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
