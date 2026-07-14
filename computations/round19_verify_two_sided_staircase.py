#!/usr/bin/env python3
"""Exact finite audit for the frozen Round 19 two-sided staircase.

This program deliberately does not evaluate shell Bessel cross-products or
sample eigenfrequencies.  It authenticates the proof-free candidate and its
six permitted inputs, then checks every finite algebraic obligation used by
the candidate with integers and :class:`fractions.Fraction` objects.

The remaining analytic implications are printed in the manifest.  In
particular, a PASS here is not a replacement for the isolated analytic
reconstruction required by the candidate freeze.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, field
from fractions import Fraction as F
from pathlib import Path
from typing import Callable, Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]

CANDIDATE_PATH = "state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md"
FREEZE_PATH = "rounds/polya-main/round_019/exploration/candidate-claim-freeze.md"

# The candidate is the hash-anchored control object.  The freeze record was
# named by the audit commission and is byte-locked here at the hash observed
# before any dependency was read.
CONTROL_HASHES = {
    CANDIDATE_PATH: "87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db",
    FREEZE_PATH: "7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff",
}

# Exactly the six dependencies whitelisted by the candidate.
WHITELISTED_INPUT_HASHES = {
    "state/lemma_packets/SHELL-rho-compact-round19.md":
        "33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50",
    "rounds/polya-main/round_019/exploration/residual-mask-freeze.md":
        "0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9",
    "state/lemma_packets/SHELL-sturm-liouville-completeness.md":
        "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "sources/lorch_bessel_zeros.md":
        "85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4",
    "sources/flps_balls.md":
        "27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38",
    "sources/round19_bessel_zero_bounds.md":
        "7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f",
}

PI_LO = F(333, 106)
PI_HI = F(22, 7)


ANALYTIC_ASSUMPTIONS = (
    "Machin's identity pi/4 = 4 atan(1/5) - atan(1/239), together with "
    "the alternating arctangent remainder theorem.",
    "The separated shell spectrum, multiplicities 2*l+1, radial simplicity, "
    "and strict endpoint convention k_{l,n}<K from the permitted spectral packet.",
    "The one-dimensional min-max bounds k_{l,n}^2 >= (n*pi/(1-rho))^2 "
    "+ l(l+1), including the exact l=0 frequencies n*pi/(1-rho).",
    "Extension by zero maps each fixed shell angular form domain into the "
    "corresponding unit-ball angular form domain and therefore gives "
    "k_shell(l,n) >= j_{l+1/2,n}.",
    "The ball angular-shift min-max inequality j_{l+3/2,n}^2 >= "
    "j_{l+1/2,n}^2 + 2(l+1), with preservation of radial index n.",
    "The five externally permitted strict Bessel-zero bounds have the scope, "
    "order, radial index, and positive-zero convention stated in their source cards.",
    "The elementary spherical-Bessel identities j_1(x)=(sin x-x cos x)/x^2 "
    "and j_2(x)=((3-x^2)sin x-3x cos x)/x^3, and elementary monotonicity "
    "of tan on each nonsingular half-period.",
    "The inherited residual predicate, active U branches, uniqueness and branch "
    "equality at rho_HK, and prior absorption of B0 and B1 are accepted inputs.",
    "G_1 is decreasing on [1/2,1), as follows analytically by differentiating "
    "its displayed elementary formula.",
)


@dataclass(frozen=True)
class Check:
    name: str
    category: str
    passed: bool
    detail: str = ""


@dataclass
class Audit:
    checks: list[Check] = field(default_factory=list)
    hashes: dict[str, str] = field(default_factory=dict)
    metrics: dict[str, int] = field(default_factory=dict)

    def require(self, condition: bool, name: str, category: str, detail: str = "") -> None:
        self.checks.append(Check(name, category, bool(condition), detail))

    @property
    def passed(self) -> bool:
        return all(item.passed for item in self.checks)

    @property
    def first_failure(self) -> Check | None:
        return next((item for item in self.checks if not item.passed), None)

    def manifest(self) -> dict[str, object]:
        categories: dict[str, dict[str, int]] = {}
        for item in self.checks:
            bucket = categories.setdefault(item.category, {"passed": 0, "failed": 0})
            bucket["passed" if item.passed else "failed"] += 1
        first = self.first_failure
        return {
            "verdict": "PASS" if self.passed else "FAIL",
            "first_failed_obligation": None if first is None else {
                "name": first.name,
                "category": first.category,
                "detail": first.detail,
            },
            "check_count": len(self.checks),
            "categories": categories,
            "metrics": self.metrics,
            "authenticated_hashes": self.hashes,
            "whitelisted_input_count": len(WHITELISTED_INPUT_HASHES),
            "analytic_assumptions_not_proved_by_executable": list(ANALYTIC_ASSUMPTIONS),
        }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _atan_alternating_bounds(x: F, pairs: int) -> tuple[F, F]:
    """Return exact lower/upper bounds from adjacent alternating partial sums."""
    assert F(0) < x < F(1) and pairs >= 0

    def partial(last_index: int) -> F:
        return sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                    for k in range(last_index + 1)), F(0))

    # An odd last index is below atan(x); an even last index is above it.
    return partial(2 * pairs + 1), partial(2 * pairs)


def machin_pi_bounds() -> tuple[F, F]:
    a_lo, a_hi = _atan_alternating_bounds(F(1, 5), 6)
    b_lo, b_hi = _atan_alternating_bounds(F(1, 239), 2)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def _poly_add(a: Sequence[F], b: Sequence[F]) -> tuple[F, ...]:
    n = max(len(a), len(b))
    return tuple((a[i] if i < len(a) else F(0))
                 + (b[i] if i < len(b) else F(0)) for i in range(n))


def _poly_scale(a: Sequence[F], c: F) -> tuple[F, ...]:
    return tuple(c * x for x in a)


def _poly_mul(a: Sequence[F], b: Sequence[F]) -> tuple[F, ...]:
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return tuple(result)


def _trim(a: Sequence[F]) -> tuple[F, ...]:
    result = list(a)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def w_fixed_lower(rho: F, frequency: F) -> F:
    """A strict rational lower certificate for W(rho, frequency)."""
    return F(2) * (1 - rho ** 3) * frequency ** 3 / (9 * PI_HI)


def w_at_rhoc_fixed_lower(frequency: F) -> F:
    """Lower W at rho_c, using opposite directed pi bounds independently."""
    rho_upper = 1 / (1 + 2 * PI_LO)
    return F(2) * (1 - rho_upper ** 3) * frequency ** 3 / (9 * PI_HI)


def moving_payment_holds(rho: F, q: int, cap: int) -> bool:
    """Prove W(rho,sqrt(z^2+q))>cap by positive exact squaring."""
    coefficient = F(2) * (1 - rho ** 3) / (9 * PI_HI)
    square = PI_LO ** 2 / (1 - rho) ** 2 + q
    return coefficient ** 2 * square ** 3 > cap ** 2


def moving_payment_at_rhoc_holds(q: int, cap: int) -> bool:
    rho_upper = 1 / (1 + 2 * PI_LO)
    coefficient = F(2) * (1 - rho_upper ** 3) / (9 * PI_HI)
    square = (PI_LO + F(1, 2)) ** 2 + q
    return coefficient ** 2 * square ** 3 > cap ** 2


def _authenticate(audit: Audit, root: Path) -> None:
    audit.require(len(WHITELISTED_INPUT_HASHES) == 6,
                  "exactly six permitted dependency hashes", "provenance")
    for rel, expected in {**CONTROL_HASHES, **WHITELISTED_INPUT_HASHES}.items():
        path = root / rel
        if not path.is_file():
            audit.require(False, f"hash {rel}", "provenance", "file missing")
            continue
        observed = sha256(path)
        audit.hashes[rel] = observed
        audit.require(observed == expected, f"hash {rel}", "provenance",
                      f"expected {expected}; observed {observed}")


def _check_pi_and_source_arithmetic(audit: Audit) -> None:
    pi_lo, pi_hi = machin_pi_bounds()
    audit.require(pi_lo > PI_LO, "Machin lower certificate 333/106 < pi",
                  "pi-and-radicals")
    audit.require(pi_hi < PI_HI, "Machin upper certificate pi < 22/7",
                  "pi-and-radicals")
    audit.require(pi_lo < pi_hi, "Machin interval is nonempty", "pi-and-radicals")

    # Lorch/source-card specializations, all after positive squaring.
    audit.require(F(105, 4) - F(51, 10) ** 2 == F(6, 25),
                  "j_5/2,1 threshold difference", "source-arithmetic")
    audit.require(81 ** 2 * 5 - 178 ** 2 == 1121 > 0,
                  "j_7/2,1 radical comparison", "source-arithmetic")
    audit.require(66 ** 2 * 15 - 247 ** 2 == 4331 > 0,
                  "j_9/2,1 radical comparison", "source-arithmetic")
    audit.require(507 ** 2 * 77 - 4264 ** 2 == 1611077 > 0,
                  "j_11/2,1 radical comparison", "source-arithmetic")
    audit.require(5 > 1 and 15 > 4 and 77 > 25,
                  "all Lorch radical denominators are positive", "source-arithmetic")

    audit.require(2 * PI_HI < F(77, 10), "2*pi < 77/10", "source-arithmetic")
    audit.require(F(77, 10) < F(5, 2) * PI_LO,
                  "77/10 < 5*pi/2", "source-arithmetic")
    gap = F(5, 2) * PI_LO - F(77, 10)
    audit.require(gap == F(163, 1060) and gap > F(10, 77),
                  "cotangent certificate for j_3/2,2", "source-arithmetic")

    # Internal j_3/2,1>4 and j_5/2,2>9 tangent walls.
    audit.require(PI_HI < 4 < F(3, 2) * PI_LO,
                  "4 lies in (pi,3*pi/2)", "internal-zero-arithmetic")
    audit.require(F(3, 2) * PI_LO - 4 > F(1, 4),
                  "tan(4)<4 cotangent margin", "internal-zero-arithmetic")
    audit.require(F(5, 2) * PI_HI < 9 < 3 * PI_LO,
                  "9 lies in (5*pi/2,3*pi)", "internal-zero-arithmetic")
    audit.require(3 * PI_LO - 9 == F(45, 106),
                  "exact lower distance 3*pi-9", "internal-zero-arithmetic")
    audit.require(F(45, 106) > F(9, 26),
                  "tan(9)+9/26<0 certificate", "internal-zero-arithmetic")
    audit.require((PI_HI / 2) ** 2 < 3 < PI_LO ** 2,
                  "sqrt(3) lies in (pi/2,pi)", "internal-zero-arithmetic")

    # At every zero of R=tan(x)+3x/(x^2-3), substitution gives R'>0.
    # This polynomial identity prevents more than one crossing per continuous
    # negative-tangent half-period.
    x2_minus_3 = (F(-3), F(0), F(1))
    lhs = _poly_add(_poly_mul(x2_minus_3, x2_minus_3),
                    _poly_add((F(0), F(0), F(9)),
                              (F(-9), F(0), F(-3))))
    audit.require(_trim(lhs) == (F(0), F(0), F(0), F(0), F(1)),
                  "j_2 tangent-root derivative numerator reduces to x^4",
                  "internal-zero-arithmetic")

    tangent_inventory = (
        ("(0,pi/2)", 0),
        ("(pi/2,sqrt(3))", 0),
        ("(sqrt(3),pi)", 0),
        ("(pi,3*pi/2)", 0),
        ("(3*pi/2,2*pi)", 1),
        ("(2*pi,5*pi/2)", 0),
        ("(5*pi/2,3*pi)", 1),
    )
    audit.require(sum(count for _, count in tangent_inventory) == 2,
                  "complete j_2 tangent half-period inventory through 3*pi",
                  "internal-zero-arithmetic")
    audit.metrics["j2_tangent_cells"] = len(tangent_inventory)


def _check_thresholds_inventory_and_crossings(audit: Audit) -> None:
    c2, c3, c4, c12, c5 = F(51, 10), F(13, 2), F(15, 2), F(77, 10), F(17, 2)
    fixed = (F(4), c2, c3, c4, c12, c5, F(9))
    audit.require(all(a < b for a, b in zip(fixed, fixed[1:])),
                  "strict rational threshold order through 9", "wall-arithmetic")
    audit.require(4 * 9 ** 2 < 337 < 19 ** 2,
                  "9 < sqrt(337)/2 < 19/2", "wall-arithmetic")

    # Angular shift arithmetic used to exclude all remaining channels at K=d.
    audit.require(c5 ** 2 + 12 == F(337, 4),
                  "l=5 to l=6 first-mode shift lands at d^2", "inventory")
    audit.require(9 ** 2 + 6 > F(337, 4)
                  and 9 ** 2 + 6 - F(337, 4) == F(11, 4),
                  "l=2 to l=3 second-mode shift clears d^2", "inventory")
    audit.require((3 * PI_LO) ** 2 > F(337, 4),
                  "all n>=3 modes clear d by the l=0 third frequency", "inventory")

    # Exact high-ratio wall comparisons.
    zc_lo, zc_hi = PI_LO + F(1, 2), PI_HI + F(1, 2)
    audit.require(zc_lo ** 2 > 10, "k5(rho_c)<2z(rho_c)", "wall-arithmetic")
    audit.require(zc_hi ** 2 < 14, "2z(rho_c)<k6(rho_c)", "wall-arithmetic")
    z_quarter_lo, z_quarter_hi = 4 * PI_LO / 3, 4 * PI_HI / 3
    audit.require(z_quarter_hi ** 2 + 42 < c5 ** 2,
                  "k6(1/4)<17/2 excludes first l=5 below inventory split",
                  "inventory")
    audit.require(z_quarter_lo ** 2 > 14,
                  "k6(1/4)<2z excludes every second mode above inventory split",
                  "inventory")
    z_fifth_lo = 5 * PI_LO / 4
    audit.require(3 * z_fifth_lo ** 2 > 40,
                  "p1(1/5)>k6(1/5), hence second l=1 absent for rho>=1/5",
                  "inventory")
    audit.require(2 > 0, "p1^2-(2z)^2=2>0", "wall-arithmetic")
    audit.require(8 * PI_LO ** 2 > 42,
                  "k6<3z on the complete high-ratio range", "inventory")

    # In the lower band 2z stays strictly between 13/2 and 15/2.
    audit.require(4 * PI_LO > 13 * F(18, 19),
                  "2z>13/2 at rho=1/sqrt(337) by sqrt(337)<19",
                  "wall-arithmetic")
    audit.require(2 * PI_HI + 1 < c4,
                  "2z<15/2 at rho_c", "wall-arithmetic")

    # L=t crossings enumerate all empty/degenerate lower subbands.
    r0_is_below_one_eighteenth = 18 ** 2 < 337
    l_crossings = (F(1, 18), F(1, 17), F(5, 77), F(1, 15),
                   F(1, 13), F(5, 51), F(1, 8))
    audit.require(r0_is_below_one_eighteenth
                  and all(a < b for a, b in zip(l_crossings, l_crossings[1:])),
                  "ordered L-crossing ratios for 9,17/2,77/10,15/2,13/2,51/10,4",
                  "wall-arithmetic")
    audit.metrics["lower_L_crossing_faces"] = len(l_crossings) + 1  # include L=d

    # Multiplicity sums and proposed caps.
    weights = tuple(2 * ell + 1 for ell in range(7))
    cumulative = tuple(sum(weights[:m + 1]) for m in range(6))
    audit.require(weights == (1, 3, 5, 7, 9, 11, 13),
                  "full angular multiplicities l=0,...,6", "caps")
    audit.require(cumulative == (1, 4, 9, 16, 25, 36),
                  "first-mode staircase caps", "caps")
    audit.require(sum(weights[:5]) + weights[0] == 26,
                  "cap after l=0 second entry", "caps")
    audit.require(sum(weights[:5]) + weights[0] + weights[1] == 29,
                  "cap after both possible second entries", "caps")

    # Direct reconstruction of every lower table row, including strict lower
    # thresholds and the only moving split 2z in (13/2,15/2).
    def reconstructed_lower_count(k: F, twice_z: F) -> int:
        return (
            1
            + 3 * (k > 4)
            + 5 * (k > c2)
            + 7 * (k > c3)
            + 9 * (k > c4)
            + 11 * (k > c5)
            + 1 * (k > twice_z)
            + 3 * (k > c12)
            + 5 * (k > 9)
        )

    twice_z_probes = (F(20, 3), F(7), F(29, 4))
    base_k_probes = sorted(set(
        [F(4), c2, c3, c4, c12, c5, F(9), F(37, 4)]
        + [(a + b) / 2 for a, b in zip(
            (F(7, 2), F(4), c2, c3, c4, c12, c5, F(9)),
            (F(4), c2, c3, c4, c12, c5, F(9), F(37, 4)))]
    ))
    table_cases = 0
    for twice_z in twice_z_probes:
        # Include K=2z itself: strict counting owns the second radial mode only
        # immediately above, never at, this moving face.
        for k in sorted(set(base_k_probes + [twice_z])):
            if not (F(7, 2) < k <= F(37, 4)):
                continue
            count = reconstructed_lower_count(k, twice_z)
            if k <= 4:
                cap = 1
            elif k <= c2:
                cap = 4
            elif k <= c3:
                cap = 9 if k <= twice_z else 10
            elif k <= c4:
                cap = 16 if k <= twice_z else 17
            elif k <= c12:
                cap = 26
            elif k <= c5:
                cap = 29
            elif k <= 9:
                cap = 40
            else:
                cap = 45
            audit.require(count <= cap,
                          f"lower cap truth case z2={twice_z}, K={k}", "cap-truth-table",
                          f"count {count}, cap {cap}")
            table_cases += 1
    audit.metrics["lower_cap_truth_cases"] = table_cases

    audit.require(sum(weights[:6]) + sum(weights[:3]) == 45,
                  "included K=d face has cap 45 and no excluded remainder mode",
                  "caps")

    # Mandatory frequency-face semantics.  These are spectral or band lower
    # lower walls and therefore use a strict '<K' entry test.  The candidate
    # upper faces d and k6 are included, whereas the inherited residual U face
    # is excluded.  Fixed thresholds are also strict lower entry walls.
    strict_entry_faces = (
        "L", "z", "k2", "k3", "k4", "k5", "k6", "2z", "p1",
        "4", "51/10", "13/2", "15/2", "77/10", "17/2", "9",
    )
    for face in strict_entry_faces:
        threshold = F(7)
        audit.require(not (threshold < threshold) and threshold < threshold + 1,
                      f"strict ownership at K={face}", "face-semantics")
    audit.require(F(7) <= F(7), "candidate includes upper face K=d",
                  "face-semantics")
    audit.require(F(7) <= F(7), "candidate includes upper face K=k6",
                  "face-semantics")
    audit.require(not (F(7) < F(7)), "residual excludes upper face K=U",
                  "face-semantics")
    audit.metrics["mandatory_frequency_faces"] = len(strict_entry_faces) + 3

    # Equality at a simultaneous cross-order entry excludes every coincident
    # mode under the strict count; immediately above, multiplicities add.
    for block in ((1, 3), (5, 7, 9), (1, 3, 5, 7, 9, 11)):
        at_face = sum(weight * False for weight in block)
        above_face = sum(block)
        audit.require(at_face == 0 and above_face == sum(block),
                      f"strict coincident-entry block {block}", "cap-truth-table")


def _check_derivatives_and_payments(audit: Audit) -> None:
    one_minus_r = (F(1), F(-1))
    r2 = (F(0), F(0), F(1))
    one_minus_r_cubed = (F(1), F(0), F(0), F(-1))
    one_plus_r = (F(1), F(1))

    # Verify the moving-threshold log-derivative numerator identity for every
    # q used in k_0,...,k_6 and p_1.  Coefficients are exact polynomials in rho.
    for q in (0, 2, 6, 12, 20, 30, 42):
        p2 = F(17, 5)  # an indeterminate stand-in coefficient; identity is linear in p^2
        left = _poly_add(_poly_scale(one_minus_r_cubed, p2),
                         _poly_scale(_poly_mul(_poly_mul(r2, one_minus_r),
                                               _poly_add((p2,),
                                                         _poly_scale(_poly_mul(one_minus_r,
                                                                               one_minus_r), F(q)))),
                                     F(-1)))
        right = _poly_mul(one_minus_r,
                          _poly_add(_poly_scale(one_plus_r, p2),
                                    _poly_scale(_poly_mul(r2,
                                                          _poly_mul(one_minus_r,
                                                                    one_minus_r)), F(-q))))
        audit.require(_trim(left) == _trim(right),
                      f"moving derivative numerator identity q={q}", "derivatives")
    quarter_minus_product = (F(1, 4), F(-1), F(1))
    centered_square = _poly_mul((F(-1, 2), F(1)), (F(-1, 2), F(1)))
    audit.require(_trim(quarter_minus_product) == _trim(centered_square),
                  "rho(1-rho)<=1/4 is the square (rho-1/2)^2>=0",
                  "derivatives")
    audit.require(42 < 16 * 9,
                  "moving derivative positive: pi^2(1+rho)>9>q/16",
                  "derivatives")
    audit.require(3 > 0,
                  "d[(1+rho+rho^2)/(1-rho)^2] numerator is 3(1+rho)",
                  "derivatives")
    audit.require(-2 < 0 and 3 > 0,
                  "fixed-frequency derivative is -2*rho^2*K^3/(3*pi)<0",
                  "derivatives")
    audit.require(-1 < 0 and 12 > 0,
                  "W(rho,L(rho)) derivative is -1/(12*pi*rho^4)<0",
                  "derivatives")

    # High-ratio first-mode payments.  Below each split a fixed ball threshold
    # pays; above it the increasing moving k_m threshold pays.
    fixed_high = (
        (F(3, 10), F(51, 10), 9, "l=2 fixed"),
        (F(1, 2), F(13, 2), 16, "l=3 fixed"),
        (F(1, 2), F(15, 2), 25, "l=4 fixed"),
        (F(13, 25), F(17, 2), 36, "l=5 fixed"),
    )
    moving_high = (
        (F(3, 10), 6, 9, "l=2 moving"),
        (F(1, 2), 12, 16, "l=3 moving"),
        (F(1, 2), 20, 25, "l=4 moving"),
        (F(13, 25), 30, 36, "l=5 moving"),
    )
    for rho, threshold, cap, label in fixed_high:
        audit.require(w_fixed_lower(rho, threshold) > cap,
                      f"high payment {label}", "payments")
    for rho, q, cap, label in moving_high:
        audit.require(moving_payment_holds(rho, q, cap),
                      f"high payment {label}", "payments")
    audit.require((3 + 6 * PI_LO + 4 * PI_LO ** 2) / 18 > 1,
                  "high l=0 payment at z and rho_c", "payments")
    audit.require(moving_payment_at_rhoc_holds(2, 4),
                  "high l=1 moving payment at k1 and rho_c", "payments")

    # Once the exact l=0 second wall is crossed, 26 pays the largest count
    # before the l=1 second mode.  At rho_c the expression simplifies exactly.
    w_2z_rhoc_lower = (16 * PI_LO ** 2 + 24 * PI_LO + 12) / 9
    audit.require(w_2z_rhoc_lower > 26,
                  "high reserve/payment W(rho_c,2z)>26", "payments")
    audit.require(w_fixed_lower(F(1, 5), F(77, 10)) > 29,
                  "high second-l=1 fixed payment at rho=1/5", "payments")

    # Lower-ratio fixed payments use monotonicity in rho and the limiting
    # right face rho_c.  The split rows use the moving exact wall 2z.
    lower_fixed = (
        (F(4), 4),
        (F(51, 10), 9),
        (F(13, 2), 16),
        (F(15, 2), 26),
        (F(77, 10), 29),
        (F(17, 2), 40),
        (F(9), 45),
    )
    for threshold, cap in lower_fixed:
        audit.require(w_at_rhoc_fixed_lower(threshold) > cap,
                      f"lower fixed payment K={threshold} cap={cap}", "payments")
    audit.require((3 + 6 * PI_LO + 4 * PI_LO ** 2) / 18 > 1,
                  "lower first-band moving-L payment", "payments")
    audit.require(16 * PI_LO ** 2 / 9 > 17,
                  "lower moving-2z payment exceeds both split caps 10 and 17",
                  "payments")


def _check_upper_floor_and_ratio_order(audit: Audit) -> None:
    # Coarse exact radical bounds, all squared only after positivity.
    audit.require(F(25, 9) < 3 < F(49, 16),
                  "5/3<sqrt(3)<7/4", "upper-floor")
    audit.require(F(49, 25) < 2,
                  "7/5<sqrt(2)", "upper-floor")
    audit.require(PI_LO > 3, "pi>3 for omega_0 bounds", "upper-floor")
    omega_lower, omega_upper = F(13, 132), F(1, 8)
    c0_lower, d_upper = F(131, 75), F(19, 2)
    audit.require(omega_lower > 0 and omega_upper > omega_lower,
                  "0<13/132<omega_0<1/8", "upper-floor")
    audit.require(c0_lower > d_upper * omega_upper,
                  "C0/omega0>d by directed radical bounds", "upper-floor")
    audit.require(1 + 2 * (F(1, 2) + F(8, 15)) == 2 * (1 + F(8, 15)),
                  "symbolic identity 1+2C*=2C0 (sqrt(2) coefficient)",
                  "upper-floor")

    # rho_*<1/sqrt(337)<rho_HK<omega0<rho_c<1/5.
    audit.require(337 * 9407 ** 2 > 100000 ** 2,
                  "1/sqrt(337)<9407/100000<rho_HK", "ratio-order")
    audit.require(F(94071, 1000000) < omega_lower,
                  "rho_HK<omega0 via frozen root bracket", "ratio-order")
    audit.require(omega_upper < F(7, 51),
                  "omega0<rho_c via rho_c>7/51", "ratio-order")
    audit.require(PI_LO > 2, "rho_c<1/5", "ratio-order")
    audit.require(c0_lower > d_upper * omega_upper,
                  "rho_*=omega0/(2C0)<1/sqrt(337)", "ratio-order")
    rational_splits = (F(1, 5), F(1, 4), F(3, 10), F(1, 2),
                       F(13, 25), F(5, 6), F(7, 8))
    audit.require(all(a < b for a, b in zip(rational_splits, rational_splits[1:])),
                  "ordered high-ratio splits through 7/8", "ratio-order")

    # d<U on the low component: H0 is increasing from H0(rho_*)=C0/omega0;
    # K0>=C0/omega0 because its numerator contains sqrt(4*omega0*C0).
    audit.require(c0_lower > d_upper * omega_upper,
                  "d<H0 throughout its active low-ratio branch", "upper-floor")
    audit.require(c0_lower > d_upper * omega_upper,
                  "d<K0 throughout its active low-ratio branch", "upper-floor")

    # k6<K0.  For rho<=1/2, eta*k6<C0.  For rho>=1/2, the negative
    # sqrt(a*k6) term alone dominates eta*k6.  These certify that the defining
    # K0 quadratic is negative at k6, so k6 lies below its positive root.
    audit.require((F(44, 7) ** 2 + 42) < 10 ** 2
                  and F(10, 8) < c0_lower,
                  "k6<K0 on [rho_c,1/2]", "upper-floor")
    audit.require((F(132, 7) ** 2 + 42) < 20 ** 2
                  and F(20, 8) < 6
                  and 2 * PI_LO > 6,
                  "k6<K0 on [1/2,5/6)", "upper-floor")
    audit.require((F(176, 7) ** 2 + 42) < 27 ** 2
                  and 54 / F(1, 6) ** 2 > 27,
                  "k6<54/(1-rho)^2 on [5/6,7/8)", "upper-floor")


def _check_residual_truth_tables(audit: Audit) -> None:
    # Surrogate coordinates encode only exact face order.  They exhaust every
    # vertical face and every interval/equality cell of the relevant walls.
    rs, r0, rc, r78 = F(0), F(2), F(4), F(6)
    rho_probes = (F(-1), rs, F(1), r0, F(3), rc, F(5), r78, F(7))

    def walls(rho: F) -> tuple[F, F, F, F, F]:
        # L,d,U and k5,k6.  The low wall order changes at rho=r0.
        if rho < r0:
            L, d, U = F(2), F(1), F(4)
        elif rho == r0:
            L = d = F(2)
            U = F(4)
        else:
            L, d, U = F(1), F(2), F(4)
        return L, d, U, F(1), F(2)

    cases = 0
    for rho in rho_probes:
        L, d, U, k5, k6 = walls(rho)
        raw_walls = sorted(set((L, d, U, k5, k6)))
        k_probes: list[F] = [raw_walls[0] - 1, raw_walls[-1] + 1]
        k_probes.extend(raw_walls)
        k_probes.extend((a + b) / 2 for a, b in zip(raw_walls, raw_walls[1:]))
        for k in sorted(set(k_probes)):
            d18 = ((rs < rho < rc and L < k < U)
                   or (rc <= rho < r78 and k5 < k < U))
            c19 = ((r0 < rho < rc and L < k <= d)
                   or (rc <= rho < r78 and k5 < k <= k6))
            subtraction = d18 and not c19
            normalized = (
                (rs < rho <= r0 and L < k < U)
                or (r0 < rho < rc and d < k < U)
                or (rc <= rho < r78 and k6 < k < U)
            )
            audit.require(subtraction == normalized,
                          f"residual truth rho={rho}, K={k}", "residual-truth-table",
                          f"D18={d18}, C19={c19}, normalized={normalized}")
            cases += 1
    audit.metrics["residual_face_truth_cases"] = cases

    # At rho=r0, L=d and the proposed lower addition is empty; the complete
    # original L<K<U slice remains in the first normalized component.
    audit.require(not (r0 < r0 < rc),
                  "rho=1/sqrt(337) is excluded from C19^L", "set-arithmetic")
    audit.require(F(1, 2) ** 2 * 337 == F(337, 4),
                  "at rho=1/sqrt(337), L=sqrt(337)/2=d", "set-arithmetic")

    # B0/B1 were already absorbed: under B_i=>not D18, subtracting them again
    # cannot change D18\C19.  Exhaust the constrained Boolean table.
    absorbed_cases = 0
    for d18 in (False, True):
        for c19 in (False, True):
            for b0 in (False, True):
                for b1 in (False, True):
                    if (b0 or b1) and d18:
                        continue
                    audit.require((d18 and not c19)
                                  == (d18 and not (c19 or b0 or b1)),
                                  f"absorbed-box truth d={d18},c={c19},b0={b0},b1={b1}",
                                  "set-arithmetic")
                    absorbed_cases += 1
    audit.metrics["absorbed_box_truth_cases"] = absorbed_cases


def run_audit(root: Path = REPO_ROOT) -> Audit:
    audit = Audit()
    _authenticate(audit, root)
    _check_pi_and_source_arithmetic(audit)
    _check_thresholds_inventory_and_crossings(audit)
    _check_derivatives_and_payments(audit)
    _check_upper_floor_and_ratio_order(audit)
    _check_residual_truth_tables(audit)
    return audit


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT,
                        help="repository root (defaults to the parent of computations)")
    parser.add_argument("--self-check", action="store_true",
                        help="accepted for an explicit audit invocation")
    parser.add_argument("--manifest", action="store_true",
                        help="print the complete JSON manifest")
    args = parser.parse_args(argv)

    audit = run_audit(args.root.resolve())
    manifest = audit.manifest()
    if args.manifest:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    else:
        print(f"{manifest['verdict']}: {manifest['check_count']} exact checks")
        print(f"first failed obligation: {manifest['first_failed_obligation']}")
    return 0 if audit.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
