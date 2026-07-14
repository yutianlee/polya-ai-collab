#!/usr/bin/env python3
"""Independent Round 21 A4 verifier for the exact-D20-closure candidate.

This wrapper has a deliberately narrow conclusion.  It authenticates and
replays the two sealed finite certificates, checks their frozen schemas, and
checks the candidate's exact set bookkeeping.  The aggregate replay proves
only the predicates evaluated by outward Arb boxes at the base frequency
``K=200``.  The universally quantified propagation for every ``K>=200`` is
an A3 analytic obligation and is never promoted by this program.

All proof decisions use exact ``Fraction`` arithmetic or certain python-flint
``arb`` comparisons.  Floats are absent from this wrapper's proof path.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import inspect
import sys
from dataclasses import dataclass, replace
from enum import IntEnum
from fractions import Fraction
from pathlib import Path
from types import ModuleType
from typing import Iterable, Mapping, Sequence

from flint import arb, ctx, fmpq


REPO_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_INPUT_HASHES: Mapping[str, str] = {
    "state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md":
        "415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3",
    "state/certificate_contracts/ROUND21-compact-proxy-contract.md":
        "1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe",
    "state/certificate_contracts/ROUND21-aggregate-tail-contract.md":
        "06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d",
    "state/lemma_packets/SHELL-rho-compact-round21.md":
        "fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5",
    "rounds/polya-main/round_021/exploration/residual-mask-freeze.md":
        "92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5",
    "rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md":
        "0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08",
    "computations/round21_certify_compact_proxy.py":
        "2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856",
    "computations/tests/test_round21_certify_compact_proxy.py":
        "29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36",
    "rounds/polya-main/round_021/certification/compact-proxy-rectangle.md":
        "c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293",
    "rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md":
        "61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0",
    "computations/round21_verify_aggregate_tail.py":
        "fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952",
    "computations/tests/test_round21_verify_aggregate_tail.py":
        "50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91",
    "rounds/polya-main/round_021/certification/aggregate-tail-global.md":
        "0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6",
    "state/lemma_packets/SHELL-sturm-liouville-completeness.md":
        "6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8",
    "state/lemma_packets/SHELL-phase-enclosures.md":
        "96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf",
    "state/lemma_packets/SHELL-weighted-lattice-fractional.md":
        "a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c",
    "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md":
        "0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f",
    "sources/annuli_polya.md":
        "951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57",
}

COMPACT_MODULE_PATH = REPO_ROOT / "computations" / "round21_certify_compact_proxy.py"
AGGREGATE_MODULE_PATH = REPO_ROOT / "computations" / "round21_verify_aggregate_tail.py"

COMPACT_SCHEMA = "round21-compact-proxy-v2-half-open-faces"
COMPACT_ROOT = (
    Fraction(7, 51),
    Fraction(39, 50),
    Fraction(12),
    Fraction(200),
)
COMPACT_FROZEN_PRECISION = 256
COMPACT_MIN_PRECISION = 192
COMPACT_LEAVES = 10_580
COMPACT_MAX_DEPTH = 15
COMPACT_DEPTH_LIMIT = 30
COMPACT_BOX_LIMIT = 100_000
COMPACT_PROXY_CORNERS = 16_020
COMPACT_FLOOR_COMPARISONS = 2_153_076
COMPACT_WALL_STRADDLES = 0
COMPACT_DIGEST = "96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631"

AGGREGATE_FROZEN_PRECISION = 192
AGGREGATE_MIN_PRECISION = 192
AGGREGATE_BASE_K = 200
AGGREGATE_LOWER_RHO = Fraction(7, 51)
AGGREGATE_SPLIT_RHO = Fraction(1, 2)
AGGREGATE_UPPER_RHO = Fraction(39, 50)
AGGREGATE_MAX_WIDTH = Fraction(1, 2000)
AGGREGATE_BOXES = 1_286
AGGREGATE_LOW_BOXES = 726
AGGREGATE_HIGH_BOXES = 560

AGGREGATE_VALUE_KEYS = frozenset(
    {
        "eta",
        "b",
        "mu",
        "R",
        "S",
        "B200",
        "BK200",
        "F",
        "I_KK",
        "I_KK_bound",
        "interface_KK",
        "B_KK",
    }
)
AGGREGATE_PREDICATE_FAMILIES = (
    "1-rho>0",
    "mu-3/2>0",
    "200*eta-1>0",
    "S-R>0",
    "R-200*rho>0",
    "I_KK<3b/800",
    "E_KK>0",
    "B_KK>F",
    "B(rho,200)>0",
    "B_K(rho,200)>0",
    "F(rho)>0",
)
AGGREGATE_ANALYTIC_BOUNDARY = (
    "tau=0 cell in Q reconstruction",
    "every half-integer mu wall in Q reconstruction",
    "every integer K*eta wall in Q reconstruction",
    "strict B>=0 => Q>0 => spectral implication",
    "universal guards for every K>=200",
    "universal I_KK/E_KK/B_KK inequalities for every K>=200",
    "integration of B_KK from 200 to K",
    "integration of B_K from 200 to K",
)

# Exact domain carried by the k_11>12 guard.  The upper wall is essential:
# rho=1 is singular, and the unqualified assertion is false beyond it.
K11_GUARD_DOMAIN = "rho_c<=rho<1"


class AuditError(RuntimeError):
    """The first failed A4 authentication, schema, replay, or set check."""


class AuthenticationError(AuditError):
    """A supplied byte identity or the exact manifest schema failed."""


class SchemaError(AuditError):
    """A frozen finite-certificate schema failed."""


class ReplayError(AuditError):
    """A certain finite proof predicate or exact set invariant failed."""


class MachinBranchCertificateError(ReplayError):
    """The immutable exact principal-branch certificate was incomplete."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_manifest_schema(expected: Mapping[str, str]) -> None:
    if set(expected) != set(EXPECTED_INPUT_HASHES):
        missing = sorted(set(EXPECTED_INPUT_HASHES) - set(expected))
        extra = sorted(set(expected) - set(EXPECTED_INPUT_HASHES))
        raise AuthenticationError(f"wrong authenticated path set: missing={missing}, extra={extra}")
    folded = [path.replace("\\", "/").casefold() for path in expected]
    if len(folded) != len(set(folded)):
        raise AuthenticationError("authenticated paths are not unique under case folding")
    for relative, digest in expected.items():
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts:
            raise AuthenticationError(f"non-repository authenticated path: {relative}")
        if len(digest) != 64 or any(ch not in "0123456789abcdefABCDEF" for ch in digest):
            raise AuthenticationError(f"invalid SHA-256 text for {relative}: {digest}")


def authenticate_inputs(
    root: Path = REPO_ROOT,
    expected: Mapping[str, str] = EXPECTED_INPUT_HASHES,
) -> dict[str, str]:
    validate_manifest_schema(expected)
    root = Path(root).resolve()
    observed: dict[str, str] = {}
    for relative, wanted in expected.items():
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise AuthenticationError(f"authenticated path escapes repository: {relative}") from exc
        if not path.is_file():
            raise AuthenticationError(f"missing authenticated input: {relative}")
        got = sha256_file(path)
        if got.lower() != wanted.lower():
            raise AuthenticationError(
                f"SHA-256 mismatch for {relative}: expected {wanted.lower()}, got {got.lower()}"
            )
        observed[relative] = got.lower()
    return observed


def _load_hash_gated_module(name: str, path: Path, expected_digest: str) -> ModuleType:
    if sha256_file(path) != expected_digest:
        raise AuthenticationError(f"sealed module changed before import: {path.relative_to(REPO_ROOT)}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AuthenticationError(f"cannot load sealed module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_sealed_modules() -> tuple[ModuleType, ModuleType]:
    compact = _load_hash_gated_module(
        "round21_a4_sealed_compact",
        COMPACT_MODULE_PATH,
        EXPECTED_INPUT_HASHES["computations/round21_certify_compact_proxy.py"],
    )
    aggregate = _load_hash_gated_module(
        "round21_a4_sealed_aggregate",
        AGGREGATE_MODULE_PATH,
        EXPECTED_INPUT_HASHES["computations/round21_verify_aggregate_tail.py"],
    )
    return compact, aggregate


@dataclass(frozen=True)
class CompactSchemaSnapshot:
    schema: str
    root: tuple[Fraction, Fraction, Fraction, Fraction]
    minimum_precision: int
    frozen_precision: int
    depth_limit: int
    box_limit: int
    packet_hashes: tuple[tuple[str, str], ...]


def compact_schema_snapshot(module: ModuleType) -> CompactSchemaSnapshot:
    root = module.ROOT_BOX
    return CompactSchemaSnapshot(
        schema=module.SCHEMA,
        root=(root.rho_lo, root.rho_hi, root.k_lo, root.k_hi),
        minimum_precision=module.MIN_PRECISION_BITS,
        frozen_precision=module.DEFAULT_PRECISION_BITS,
        depth_limit=module.DEFAULT_MAX_DEPTH,
        box_limit=module.DEFAULT_MAX_BOXES,
        packet_hashes=tuple(module.PACKETS.items()),
    )


def validate_compact_schema(snapshot: CompactSchemaSnapshot) -> None:
    expected_packets = (
        (
            "SHELL-sturm-liouville-completeness.md",
            EXPECTED_INPUT_HASHES["state/lemma_packets/SHELL-sturm-liouville-completeness.md"],
        ),
        (
            "SHELL-phase-enclosures.md",
            EXPECTED_INPUT_HASHES["state/lemma_packets/SHELL-phase-enclosures.md"],
        ),
        (
            "SHELL-weighted-lattice-fractional.md",
            EXPECTED_INPUT_HASHES["state/lemma_packets/SHELL-weighted-lattice-fractional.md"],
        ),
    )
    wanted = CompactSchemaSnapshot(
        COMPACT_SCHEMA,
        COMPACT_ROOT,
        COMPACT_MIN_PRECISION,
        COMPACT_FROZEN_PRECISION,
        COMPACT_DEPTH_LIMIT,
        COMPACT_BOX_LIMIT,
        expected_packets,
    )
    if snapshot != wanted:
        raise SchemaError(f"compact schema mismatch: expected {wanted}, got {snapshot}")


@dataclass(frozen=True)
class AggregateSchemaSnapshot:
    minimum_precision: int
    base_k: int
    lower_rho: Fraction
    split_rho: Fraction
    upper_rho: Fraction
    max_width: Fraction
    box_count: int
    rational_box_fields: tuple[str, ...]
    evaluate_parameters: tuple[str, ...]
    run_parameters: tuple[str, ...]
    expected_hashes: tuple[tuple[str, str], ...]


def aggregate_schema_snapshot(module: ModuleType) -> AggregateSchemaSnapshot:
    return AggregateSchemaSnapshot(
        minimum_precision=module.MIN_PRECISION_BITS,
        base_k=module.K0,
        lower_rho=module.LOWER_RHO,
        split_rho=module.SPLIT_RHO,
        upper_rho=module.UPPER_RHO,
        max_width=module.MAX_BOX_WIDTH,
        box_count=module.EXPECTED_BOX_COUNT,
        rational_box_fields=tuple(module.RationalBox.__dataclass_fields__),
        evaluate_parameters=tuple(inspect.signature(module.evaluate_at_k0).parameters),
        run_parameters=tuple(inspect.signature(module.run_certificate).parameters),
        expected_hashes=tuple(module.EXPECTED_HASHES.items()),
    )


def validate_aggregate_schema(snapshot: AggregateSchemaSnapshot) -> None:
    expected_hashes = (
        (
            "rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md",
            EXPECTED_INPUT_HASHES[
                "rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md"
            ],
        ),
        (
            "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md",
            EXPECTED_INPUT_HASHES[
                "state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md"
            ],
        ),
        (
            "state/lemma_packets/SHELL-weighted-lattice-fractional.md",
            EXPECTED_INPUT_HASHES["state/lemma_packets/SHELL-weighted-lattice-fractional.md"],
        ),
        (
            "state/lemma_packets/SHELL-sturm-liouville-completeness.md",
            EXPECTED_INPUT_HASHES["state/lemma_packets/SHELL-sturm-liouville-completeness.md"],
        ),
        (
            "sources/annuli_polya.md",
            EXPECTED_INPUT_HASHES["sources/annuli_polya.md"],
        ),
    )
    wanted = AggregateSchemaSnapshot(
        AGGREGATE_MIN_PRECISION,
        AGGREGATE_BASE_K,
        AGGREGATE_LOWER_RHO,
        AGGREGATE_SPLIT_RHO,
        AGGREGATE_UPPER_RHO,
        AGGREGATE_MAX_WIDTH,
        AGGREGATE_BOXES,
        ("lo", "hi", "eta_regime"),
        ("rho", "eta_regime"),
        ("precision_bits", "authenticate", "root"),
        expected_hashes,
    )
    if snapshot != wanted:
        raise SchemaError(f"aggregate base-only schema mismatch: expected {wanted}, got {snapshot}")


def _function_nodes(tree: ast.AST, names: set[str]) -> list[ast.FunctionDef]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name in names]


def _assert_no_float_decisions(path: Path, function_names: set[str]) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    nodes = _function_nodes(tree, function_names)
    found = {node.name for node in nodes}
    if found != function_names:
        raise SchemaError(f"missing proof functions in {path.name}: {sorted(function_names - found)}")
    for function in nodes:
        for node in ast.walk(function):
            if isinstance(node, ast.Constant) and isinstance(node.value, float):
                raise SchemaError(f"binary float literal in proof function {function.name}")
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "float":
                    raise SchemaError(f"float conversion in proof function {function.name}")
                if isinstance(node.func, ast.Attribute) and node.func.attr == "mid":
                    raise SchemaError(f"midpoint call in proof function {function.name}")


def validate_static_proof_paths() -> None:
    _assert_no_float_decisions(
        COMPACT_MODULE_PATH,
        {
            "active_channel_count",
            "g_arb",
            "proxy_argument_arb",
            "strict_count_upper_from_arb",
            "coarse_proxy_upper",
            "weyl_arb",
            "evaluate",
            "coordinate_owned",
            "box_owns",
            "validate_partition",
            "validate_leaves",
        },
    )
    _assert_no_float_decisions(
        AGGREGATE_MODULE_PATH,
        {"arb_box", "g_one", "evaluate_at_k0", "_require_positive", "_require_less"},
    )
    tree = ast.parse(AGGREGATE_MODULE_PATH.read_text(encoding="utf-8"))
    evaluate = _function_nodes(tree, {"evaluate_at_k0"})[0]
    fixed_k = False
    for node in ast.walk(evaluate):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        value = node.value
        if any(isinstance(target, ast.Name) and target.id == "k" for target in targets):
            fixed_k = (
                isinstance(value, ast.Call)
                and isinstance(value.func, ast.Name)
                and value.func.id == "arb"
                and len(value.args) == 1
                and isinstance(value.args[0], ast.Name)
                and value.args[0].id == "K0"
            )
    if not fixed_k:
        raise SchemaError("aggregate evaluator is not syntactically fixed to arb(K0)")


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def independent_compact_digest(certificate: object) -> str:
    rows = [
        COMPACT_SCHEMA,
        f"precision_bits={certificate.precision_bits}",
        "root=" + ",".join(fraction_text(value) for value in COMPACT_ROOT),
    ]
    rows.extend(f"packet={name}:{digest}" for name, digest in certificate.packet_hashes)
    for leaf in sorted(certificate.leaves, key=lambda item: item.box):
        box = leaf.box
        rows.append(
            "leaf="
            + ",".join(
                fraction_text(value)
                for value in (box.rho_lo, box.rho_hi, box.k_lo, box.k_hi)
            )
            + f",depth={leaf.depth},P={leaf.proxy_upper}"
        )
    return hashlib.sha256(("\n".join(rows) + "\n").encode("ascii")).hexdigest()


def _coordinate_owned(value: Fraction, lo: Fraction, hi: Fraction, root_hi: Fraction) -> bool:
    return lo <= value and (value < hi or (value == root_hi and hi == root_hi))


def validate_compact_partition_independent(leaves: Sequence[object]) -> None:
    if len(leaves) != COMPACT_LEAVES:
        raise ReplayError(f"compact leaf count changed: expected {COMPACT_LEAVES}, got {len(leaves)}")
    rho_lo, rho_hi, k_lo, k_hi = COMPACT_ROOT
    area = Fraction(0)
    rho_faces = {rho_lo, rho_hi}
    for index, leaf in enumerate(leaves):
        box = leaf.box
        if not (
            rho_lo <= box.rho_lo < box.rho_hi <= rho_hi
            and k_lo <= box.k_lo < box.k_hi <= k_hi
        ):
            raise ReplayError(f"compact leaf {index} is degenerate or outside the root")
        area += (box.rho_hi - box.rho_lo) * (box.k_hi - box.k_lo)
        rho_faces.update((box.rho_lo, box.rho_hi))
    if area != (rho_hi - rho_lo) * (k_hi - k_lo):
        raise ReplayError("compact exact leaf area does not equal root area")

    ordered_rho = sorted(rho_faces)
    for left, right in zip(ordered_rho, ordered_rho[1:]):
        intervals = sorted(
            (leaf.box.k_lo, leaf.box.k_hi)
            for leaf in leaves
            if leaf.box.rho_lo <= left and right <= leaf.box.rho_hi
        )
        cursor = k_lo
        for lo, hi in intervals:
            if lo != cursor:
                kind = "overlap" if lo < cursor else "gap"
                raise ReplayError(f"compact {kind} in rho slab [{left},{right}] at K={lo}")
            cursor = hi
        if cursor != k_hi:
            raise ReplayError(f"compact rho slab [{left},{right}] misses the upper K face")

    for rho in ordered_rho:
        intervals = sorted(
            (leaf.box.k_lo, leaf.box.k_hi)
            for leaf in leaves
            if _coordinate_owned(rho, leaf.box.rho_lo, leaf.box.rho_hi, rho_hi)
        )
        if not intervals or intervals[0][0] != k_lo or intervals[-1][1] != k_hi:
            raise ReplayError(f"compact vertical face rho={rho} misses an outer K face")
        for (lo1, hi1), (lo2, hi2) in zip(intervals, intervals[1:]):
            if hi1 != lo2:
                raise ReplayError(f"compact vertical-face gap/overlap at rho={rho}, K={hi1}")
            if _coordinate_owned(hi1, lo1, hi1, k_hi):
                raise ReplayError("compact lower interval incorrectly owns a shared upper face")
            if not _coordinate_owned(lo2, lo2, hi2, k_hi):
                raise ReplayError("compact upper interval does not own a shared lower face")
        if not _coordinate_owned(k_lo, *intervals[0], k_hi):
            raise ReplayError("compact lower root face is not owned")
        if not _coordinate_owned(k_hi, *intervals[-1], k_hi):
            raise ReplayError("compact upper root face is not owned")


def validate_corner_policy(policy: tuple[str, str, str, str]) -> None:
    if policy != ("rho_lo", "k_hi", "rho_hi", "k_lo"):
        raise SchemaError(
            "wrong compact monotone corners; required proxy=(rho_lo,k_hi), Weyl=(rho_hi,k_lo)"
        )


def validate_compact_certificate(certificate: object, frozen: bool) -> None:
    if certificate.precision_bits < COMPACT_MIN_PRECISION:
        raise ReplayError("compact replay precision is below 192 bits")
    if len(certificate.leaves) != COMPACT_LEAVES:
        raise ReplayError("compact certificate has the wrong leaf count")
    if certificate.max_depth != COMPACT_MAX_DEPTH:
        raise ReplayError("compact certificate has the wrong actual maximum depth")
    if certificate.generated_proxy_corners != COMPACT_PROXY_CORNERS:
        raise ReplayError("compact generated proxy-corner count changed")
    if certificate.generated_floor_comparisons != COMPACT_FLOOR_COMPARISONS:
        raise ReplayError("compact Arb/integer comparison count changed")
    if certificate.generated_wall_straddles != COMPACT_WALL_STRADDLES:
        raise ReplayError("compact generated integer-wall straddle count changed")
    independent = independent_compact_digest(certificate)
    if independent != certificate.digest:
        raise ReplayError("compact stored digest disagrees with independent canonical digest")
    if frozen and independent != COMPACT_DIGEST:
        raise ReplayError(f"compact frozen digest changed: {independent}")
    validate_compact_partition_independent(certificate.leaves)


def validate_compact_interfaces(module: ModuleType, precision_bits: int) -> None:
    if precision_bits < COMPACT_MIN_PRECISION:
        raise ReplayError("compact interface precision below gate")
    validate_corner_policy(("rho_lo", "k_hi", "rho_hi", "k_lo"))
    with ctx.workprec(precision_bits):
        exact = module.strict_count_upper_from_arb(arb(3))
        if (exact.count, exact.ceiling, exact.wall_straddle) != (2, 3, False):
            raise ReplayError("strict integer-wall rule is not [3]_< = 2")
        straddle = module.strict_count_upper_from_arb(arb("3 +/- 0.01"))
        if (straddle.count, straddle.ceiling, straddle.wall_straddle) != (3, 4, True):
            raise ReplayError("uncertain integer wall did not use the safe upper integer")
        if module.strict_count_upper_from_arb(arb(1) / 4).count != 0:
            raise ReplayError("strict count below 1/4 is not zero")
        rho = Fraction(1, 2)
        k = Fraction(3)
        nu = Fraction(3, 2)
        if module.g_arb(rho * k, nu) != arb(0):
            raise ReplayError("inner zero-extension interface nu=rho*K is not exact zero")
        expected = module.g_arb(k, nu) + arb(1) / 4
        if not (module.proxy_argument_arb(rho, k, nu) - expected).contains(0):
            raise ReplayError("proxy disagrees at the inner zero-extension interface")
        if module.g_arb(Fraction(25, 2), Fraction(25, 2)) != arb(0):
            raise ReplayError("outer zero-extension interface nu=K is not exact zero")
    half_wall = Fraction(25, 2)
    if module.active_channel_count(half_wall) != 12:
        raise ReplayError("strict half-integer active-channel cutoff changed")
    if not Fraction(23, 2) < half_wall or Fraction(25, 2) < half_wall:
        raise ReplayError("active-channel equality face is not excluded")


@dataclass(frozen=True)
class CompactReplay:
    precision_bits: int
    certificate: object


def replay_compact(module: ModuleType, high_precision: int) -> tuple[CompactReplay, CompactReplay]:
    if high_precision < 384:
        raise SchemaError("compact higher-precision replay must use at least 384 bits")
    validate_compact_schema(compact_schema_snapshot(module))
    observed_packets = module.verify_packet_hashes()
    if tuple(observed_packets) != compact_schema_snapshot(module).packet_hashes:
        raise ReplayError("compact dependency packet authentication changed")
    validate_compact_interfaces(module, COMPACT_FROZEN_PRECISION)
    frozen = module.build_certificate(
        precision_bits=COMPACT_FROZEN_PRECISION,
        max_depth=COMPACT_DEPTH_LIMIT,
        max_boxes=COMPACT_BOX_LIMIT,
    )
    validate_compact_certificate(frozen, frozen=True)
    module.validate_partition(module.ROOT_BOX, frozen.leaves)
    module.validate_leaves(module.Certifier(COMPACT_FROZEN_PRECISION), frozen.leaves)

    validate_compact_interfaces(module, high_precision)
    high = module.build_certificate(
        precision_bits=high_precision,
        max_depth=COMPACT_DEPTH_LIMIT,
        max_boxes=COMPACT_BOX_LIMIT,
    )
    validate_compact_certificate(high, frozen=False)
    if high.leaves != frozen.leaves:
        raise ReplayError("higher-precision compact leaf tree differs from the frozen tree")
    module.validate_partition(module.ROOT_BOX, high.leaves)
    module.validate_leaves(module.Certifier(high_precision), high.leaves)
    return CompactReplay(COMPACT_FROZEN_PRECISION, frozen), CompactReplay(high_precision, high)


def arb_of_fraction(value: Fraction) -> arb:
    return arb(fmpq(value.numerator, value.denominator))


def validate_aggregate_predicate_schema(families: Iterable[str]) -> None:
    if tuple(families) != AGGREGATE_PREDICATE_FAMILIES:
        raise SchemaError("aggregate finite predicate family was omitted, reordered, or changed")


def validate_analytic_boundary_schema(boundary: Iterable[str]) -> None:
    if tuple(boundary) != AGGREGATE_ANALYTIC_BOUNDARY:
        raise SchemaError("A3 analytic-boundary obligations were omitted or weakened")


def enforce_aggregate_scope(*, base_frequency: int, universal_frequency_claim: bool) -> None:
    if base_frequency != AGGREGATE_BASE_K:
        raise SchemaError("aggregate finite certificate is not fixed to K=200")
    if universal_frequency_claim:
        raise SchemaError("A4 finite replay cannot claim the universal K>=200 chain")


def validate_aggregate_partition_independent(boxes: Sequence[object]) -> None:
    if len(boxes) != AGGREGATE_BOXES:
        raise ReplayError(f"aggregate box count changed: {len(boxes)}")
    cursor = AGGREGATE_LOWER_RHO
    low = high = 0
    for index, box in enumerate(boxes):
        if box.lo != cursor:
            kind = "overlap" if box.lo < cursor else "gap"
            raise ReplayError(f"aggregate partition {kind} before box {index}")
        if not Fraction(0) < box.hi - box.lo <= AGGREGATE_MAX_WIDTH:
            raise ReplayError(f"aggregate box {index} has invalid exact width")
        if box.eta_regime == "rho_le_half":
            low += 1
            if box.hi > AGGREGATE_SPLIT_RHO:
                raise ReplayError(f"aggregate low branch crosses rho=1/2 at box {index}")
        elif box.eta_regime == "rho_ge_half":
            high += 1
            if box.lo < AGGREGATE_SPLIT_RHO:
                raise ReplayError(f"aggregate high branch crosses rho=1/2 at box {index}")
        else:
            raise ReplayError(f"aggregate box {index} has an unknown eta branch")
        cursor = box.hi
    if cursor != AGGREGATE_UPPER_RHO:
        raise ReplayError("aggregate partition has the wrong upper endpoint")
    if (low, high) != (AGGREGATE_LOW_BOXES, AGGREGATE_HIGH_BOXES):
        raise ReplayError(f"aggregate branch counts changed: {(low, high)}")
    if boxes[AGGREGATE_LOW_BOXES - 1].hi != AGGREGATE_SPLIT_RHO:
        raise ReplayError("aggregate low branch does not end exactly at rho=1/2")
    if boxes[AGGREGATE_LOW_BOXES].lo != AGGREGATE_SPLIT_RHO:
        raise ReplayError("aggregate high branch does not begin exactly at rho=1/2")


def require_outward_box(enclosure: arb, lo: Fraction, hi: Fraction) -> None:
    if not enclosure.contains(arb_of_fraction(lo)):
        raise ReplayError(f"outward ball misses exact lower endpoint {lo}")
    if not enclosure.contains(arb_of_fraction(hi)):
        raise ReplayError(f"outward ball misses exact upper endpoint {hi}")


def _positive(name: str, value: arb, box: object) -> None:
    if not (value > 0):
        raise ReplayError(f"aggregate box [{box.lo},{box.hi}] did not prove {name}>0: {value}")


def _less(name: str, left: arb, right: arb, box: object) -> None:
    if not (left < right):
        raise ReplayError(
            f"aggregate box [{box.lo},{box.hi}] did not prove {name}: left={left}, right={right}"
        )


def verify_aggregate_values(values: Mapping[str, arb], rho: arb, box: object) -> int:
    if set(values) != AGGREGATE_VALUE_KEYS:
        raise SchemaError(
            f"aggregate value family changed: missing={sorted(AGGREGATE_VALUE_KEYS-set(values))}, "
            f"extra={sorted(set(values)-AGGREGATE_VALUE_KEYS)}"
        )
    one = arb(1)
    k = arb(AGGREGATE_BASE_K)
    _positive("1-rho", one - rho, box)
    _positive("mu-3/2", values["mu"] - arb(3) / 2, box)
    _positive("200*eta-1", k * values["eta"] - one, box)
    _positive("S-R", values["S"] - values["R"], box)
    _positive("R-200*rho", values["R"] - rho * k, box)
    exact_bound = arb(3) * values["b"] / arb(800)
    if not (values["I_KK_bound"] - exact_bound).contains(0):
        raise ReplayError("aggregate I_KK bound is not the base-only value 3b/800")
    _less("I_KK<3b/800", values["I_KK"], exact_bound, box)
    _positive("E_KK", values["interface_KK"], box)
    _positive("B_KK-F", values["B_KK"] - values["F"], box)
    _positive("B(rho,200)", values["B200"], box)
    _positive("B_K(rho,200)", values["BK200"], box)
    _positive("F(rho)", values["F"], box)
    return len(AGGREGATE_PREDICATE_FAMILIES)


@dataclass(frozen=True)
class Jet2:
    """Value, first derivative, and second derivative in one variable."""

    value: arb
    first: arb
    second: arb

    @classmethod
    def constant(cls, value: arb | int) -> "Jet2":
        return cls(arb(value), arb(0), arb(0))

    @classmethod
    def variable(cls, value: arb | int) -> "Jet2":
        return cls(arb(value), arb(1), arb(0))

    @staticmethod
    def _coerce(other: "Jet2 | arb | int") -> "Jet2":
        return other if isinstance(other, Jet2) else Jet2.constant(other)

    def __add__(self, other: "Jet2 | arb | int") -> "Jet2":
        rhs = self._coerce(other)
        return Jet2(self.value + rhs.value, self.first + rhs.first, self.second + rhs.second)

    __radd__ = __add__

    def __neg__(self) -> "Jet2":
        return Jet2(-self.value, -self.first, -self.second)

    def __sub__(self, other: "Jet2 | arb | int") -> "Jet2":
        return self + (-self._coerce(other))

    def __rsub__(self, other: "Jet2 | arb | int") -> "Jet2":
        return self._coerce(other) - self

    def __mul__(self, other: "Jet2 | arb | int") -> "Jet2":
        rhs = self._coerce(other)
        return Jet2(
            self.value * rhs.value,
            self.first * rhs.value + self.value * rhs.first,
            self.second * rhs.value
            + arb(2) * self.first * rhs.first
            + self.value * rhs.second,
        )

    __rmul__ = __mul__

    def reciprocal(self) -> "Jet2":
        value = arb(1) / self.value
        first = -self.first / (self.value * self.value)
        second = (
            arb(2) * self.first * self.first / (self.value * self.value * self.value)
            - self.second / (self.value * self.value)
        )
        return Jet2(value, first, second)

    def __truediv__(self, other: "Jet2 | arb | int") -> "Jet2":
        return self * self._coerce(other).reciprocal()

    def __rtruediv__(self, other: "Jet2 | arb | int") -> "Jet2":
        return self._coerce(other) / self

    def sqrt(self) -> "Jet2":
        root = self.value.sqrt()
        first_factor = arb(1) / (arb(2) * root)
        second_factor = -arb(1) / (arb(4) * self.value * root)
        return Jet2(
            root,
            first_factor * self.first,
            second_factor * self.first * self.first + first_factor * self.second,
        )

    def asinh(self) -> "Jet2":
        denominator = (arb(1) + self.value * self.value).sqrt()
        first_factor = arb(1) / denominator
        second_factor = -self.value / (denominator * denominator * denominator)
        return Jet2(
            self.value.asinh(),
            first_factor * self.first,
            second_factor * self.first * self.first + first_factor * self.second,
        )


@dataclass(frozen=True)
class DerivativeCheck:
    expressions: Mapping[str, arb]


def derivative_check_at(
    aggregate: ModuleType,
    rho_fraction: Fraction,
    regime: str,
    k_value: int = AGGREGATE_BASE_K,
) -> DerivativeCheck:
    rho = arb_of_fraction(rho_fraction)
    one = arb(1)
    two = arb(2)
    half = one / two
    pi = arb.pi()
    eta = aggregate.g_one(half if regime == "rho_le_half" else rho, pi)
    d = two * rho.asin() / pi
    b = two * pi * rho / (one - rho)
    k = Jet2.variable(arb(k_value))
    mu = rho * k
    c = b * k
    radius = mu + half
    s = (radius * radius + c).sqrt()
    integral = (radius * s + c * (radius / c.sqrt()).asinh() - radius * radius) / two
    error = -arb(8) * (mu + half) / (arb(15) * mu.sqrt())
    reserve = (
        (mu - half) * (k * eta - one)
        + (d / two) * (mu - arb(3) / two) * (mu - half)
        - (one + d) * integral
        + error
    )

    radius_value = radius.value
    s_value = s.value
    asinh_value = (radius_value / (b * arb(k_value)).sqrt()).asinh()
    i_k = rho * (s_value - radius_value) + (b / two) * asinh_value
    i_kk = (
        rho * rho * (radius_value / s_value - one)
        + rho * b / (two * s_value)
        + b * (two * rho * arb(k_value) - one) / (arb(8) * arb(k_value) * s_value)
    )
    e_kk = (
        rho * rho * (two * mu.value - arb(3))
        / (arb(15) * mu.value * mu.value * mu.value.sqrt())
    )
    b_k = (
        rho * (arb(k_value) * eta - one)
        + (mu.value - half) * eta
        + d * rho * (mu.value - one)
        - (one + d) * i_k
        - two * rho * (two * mu.value - one)
        / (arb(15) * mu.value * mu.value.sqrt())
    )
    b_kk = two * rho * eta + d * rho * rho - (one + d) * i_kk + e_kk
    f = two * rho * eta + d * rho * rho - arb(3) * (one + d) * b / arb(800)
    expressions = {
        "I_K": integral.first - i_k,
        "I_KK": integral.second - i_kk,
        "E_KK": error.second - e_kk,
        "B_K": reserve.first - b_k,
        "B_KK": reserve.second - b_kk,
        "F_definition": f - (two * rho * eta + d * rho * rho - arb(3) * (one + d) * b / arb(800)),
    }
    if k_value == AGGREGATE_BASE_K:
        sealed = aggregate.evaluate_at_k0(rho, regime)
        expressions.update(
            {
                "sealed_B200": reserve.value - sealed["B200"],
                "sealed_BK200": reserve.first - sealed["BK200"],
                "sealed_I_KK": integral.second - sealed["I_KK"],
                "sealed_E_KK": error.second - sealed["interface_KK"],
                "sealed_B_KK": reserve.second - sealed["B_KK"],
                "sealed_F": f - sealed["F"],
            }
        )
    for name, difference in expressions.items():
        if not difference.contains(0):
            raise ReplayError(
                f"independent derivative identity {name} failed at rho={rho_fraction}, "
                f"K={k_value}, regime={regime}: {difference}"
            )
    return DerivativeCheck(expressions)


@dataclass(frozen=True)
class AggregateReplay:
    precision_bits: int
    result: object
    sign_checks: int
    endpoint_containments: int
    derivative_points: int
    base_frequency_only: bool = True


def replay_aggregate(
    module: ModuleType,
    high_precision: int,
) -> tuple[AggregateReplay, AggregateReplay]:
    if high_precision < 384:
        raise SchemaError("aggregate higher-precision replay must use at least 384 bits")
    validate_aggregate_schema(aggregate_schema_snapshot(module))
    validate_aggregate_predicate_schema(AGGREGATE_PREDICATE_FAMILIES)
    validate_analytic_boundary_schema(AGGREGATE_ANALYTIC_BOUNDARY)
    enforce_aggregate_scope(base_frequency=AGGREGATE_BASE_K, universal_frequency_claim=False)
    observed = module.authenticate_inputs(REPO_ROOT)
    if tuple(observed.items()) != aggregate_schema_snapshot(module).expected_hashes:
        raise ReplayError("aggregate sealed dependency authentication changed")
    boxes = module.build_boxes()
    module.validate_partition(boxes)
    validate_aggregate_partition_independent(boxes)

    replays: list[AggregateReplay] = []
    for precision in (AGGREGATE_FROZEN_PRECISION, high_precision):
        result = module.run_certificate(precision, root=REPO_ROOT)
        if (
            result.box_count,
            result.low_regime_boxes,
            result.high_regime_boxes,
        ) != (AGGREGATE_BOXES, AGGREGATE_LOW_BOXES, AGGREGATE_HIGH_BOXES):
            raise ReplayError("aggregate replay returned wrong box or branch counts")
        sign_checks = 0
        endpoint_checks = 0
        with ctx.workprec(precision):
            for box in boxes:
                enclosure = module.arb_box(box)
                require_outward_box(enclosure, box.lo, box.hi)
                endpoint_checks += 2
                values = module.evaluate_at_k0(enclosure, box.eta_regime)
                sign_checks += verify_aggregate_values(values, enclosure, box)
            half = arb_of_fraction(AGGREGATE_SPLIT_RHO)
            low_eta = module.evaluate_at_k0(half, "rho_le_half")["eta"]
            high_eta = module.evaluate_at_k0(half, "rho_ge_half")["eta"]
            if not (low_eta - high_eta).contains(0):
                raise ReplayError("aggregate eta branches disagree at rho=1/2")

        derivative_points = 0
        if precision == high_precision:
            with ctx.workprec(precision):
                for box in boxes:
                    derivative_check_at(module, (box.lo + box.hi) / 2, box.eta_regime)
                    derivative_points += 1
        replays.append(
            AggregateReplay(
                precision,
                result,
                sign_checks,
                endpoint_checks,
                derivative_points,
            )
        )
    return replays[0], replays[1]


def alternating_arctan_bounds(q: int, terms: int) -> tuple[Fraction, Fraction]:
    if q <= 1 or terms < 1:
        raise ValueError("alternating arctangent bound requires q>1 and terms>=1")
    partial = Fraction(0)
    for index in range(terms):
        term = Fraction(1, (2 * index + 1) * q ** (2 * index + 1))
        partial += term if index % 2 == 0 else -term
    next_term = Fraction(1, (2 * terms + 1) * q ** (2 * terms + 1))
    if terms % 2 == 0:
        return partial, partial + next_term
    return partial - next_term, partial


MACHIN_BRANCH_SCHEMA = "round21-exact-machin-principal-branch-v1"
MACHIN_THETA_DEFINITION = "theta=4*atan(1/5)-atan(1/239)"
MACHIN_PRINCIPAL_CONCLUSION = "theta=atan(1)=pi/4"
MACHIN_THETA_LOWER = (
    4 * (Fraction(1, 5) - Fraction(1, 3 * 5**3)) - Fraction(1, 239)
)
MACHIN_THETA_UPPER = Fraction(4, 5)
MACHIN_SHARED_INJECTIVITY_INTERVAL = (Fraction(0), Fraction(1))


@dataclass(frozen=True)
class MachinBranchCertificate:
    """Closed exact schema selecting the principal tangent branch."""

    schema: str
    theta_definition: str
    theta_lower_bound: Fraction | None
    theta_upper_bound: Fraction | None
    theta_bounds_are_strict: bool
    injective_function: str
    shared_injectivity_interval: tuple[Fraction, Fraction]
    shared_interval_is_open: bool
    principal_atan_one_interval: tuple[Fraction, Fraction]
    principal_atan_one_bounds_are_strict: bool
    theta_tangent: Fraction
    principal_atan_one_tangent: Fraction
    conclusion: str | None


MACHIN_BRANCH_CERTIFICATE = MachinBranchCertificate(
    schema=MACHIN_BRANCH_SCHEMA,
    theta_definition=MACHIN_THETA_DEFINITION,
    theta_lower_bound=MACHIN_THETA_LOWER,
    theta_upper_bound=MACHIN_THETA_UPPER,
    theta_bounds_are_strict=True,
    injective_function="tan",
    shared_injectivity_interval=MACHIN_SHARED_INJECTIVITY_INTERVAL,
    shared_interval_is_open=True,
    principal_atan_one_interval=MACHIN_SHARED_INJECTIVITY_INTERVAL,
    principal_atan_one_bounds_are_strict=True,
    theta_tangent=Fraction(1),
    principal_atan_one_tangent=Fraction(1),
    conclusion=MACHIN_PRINCIPAL_CONCLUSION,
)


def validate_machin_branch_certificate(
    certificate: MachinBranchCertificate,
    *,
    observed_theta_tangent: Fraction,
) -> MachinBranchCertificate:
    """Reject any loss of the exact range, injectivity, or conclusion gates."""

    if certificate.schema != MACHIN_BRANCH_SCHEMA:
        raise MachinBranchCertificateError("Machin branch schema missing or changed")
    if certificate.theta_definition != MACHIN_THETA_DEFINITION:
        raise MachinBranchCertificateError("Machin theta definition missing or changed")
    if certificate.theta_lower_bound != MACHIN_THETA_LOWER:
        raise MachinBranchCertificateError("Machin lower range bound missing or changed")
    if certificate.theta_upper_bound != MACHIN_THETA_UPPER:
        raise MachinBranchCertificateError("Machin upper range bound missing or changed")
    if not certificate.theta_bounds_are_strict:
        raise MachinBranchCertificateError("Machin strict range-bound relation was lost")
    if certificate.injective_function != "tan":
        raise MachinBranchCertificateError("Machin injective function is not tangent")
    if (
        certificate.shared_injectivity_interval
        != MACHIN_SHARED_INJECTIVITY_INTERVAL
        or not certificate.shared_interval_is_open
    ):
        raise MachinBranchCertificateError(
            "Machin shared open injectivity interval missing or changed"
        )
    shared_lo, shared_hi = certificate.shared_injectivity_interval
    if not (
        shared_lo
        < certificate.theta_lower_bound
        < certificate.theta_upper_bound
        < shared_hi
    ):
        raise MachinBranchCertificateError(
            "Machin theta bounds do not lie in the shared injectivity interval"
        )
    if (
        certificate.principal_atan_one_interval
        != certificate.shared_injectivity_interval
        or not certificate.principal_atan_one_bounds_are_strict
    ):
        raise MachinBranchCertificateError(
            "principal atan(1) is not certified in the shared open injectivity interval"
        )
    if (
        observed_theta_tangent != Fraction(1)
        or certificate.theta_tangent != observed_theta_tangent
        or certificate.principal_atan_one_tangent != Fraction(1)
    ):
        raise MachinBranchCertificateError("Machin tangent equality missing or changed")
    if certificate.conclusion != MACHIN_PRINCIPAL_CONCLUSION:
        raise MachinBranchCertificateError(
            "Machin principal-branch conclusion missing or changed"
        )
    return certificate


@dataclass(frozen=True)
class ExactConstants:
    pi_lower: Fraction
    pi_upper: Fraction
    branch_certificate: MachinBranchCertificate
    k11_guard_domain: str

    @property
    def machin_angle_lower(self) -> Fraction:
        value = self.branch_certificate.theta_lower_bound
        if value is None:  # pragma: no cover - validator makes this unreachable
            raise MachinBranchCertificateError("validated lower range bound disappeared")
        return value

    @property
    def machin_angle_upper(self) -> Fraction:
        value = self.branch_certificate.theta_upper_bound
        if value is None:  # pragma: no cover - validator makes this unreachable
            raise MachinBranchCertificateError("validated upper range bound disappeared")
        return value


def verify_exact_constants(
    branch_certificate: MachinBranchCertificate = MACHIN_BRANCH_CERTIFICATE,
) -> ExactConstants:
    # Exact tangent arithmetic behind Machin's identity:
    # tan(4 arctan(1/5))=120/119 and
    # tan(4 arctan(1/5)-arctan(1/239))=1.
    tan_double = Fraction(2, 5) / (1 - Fraction(1, 25))
    tan_quadruple = 2 * tan_double / (1 - tan_double * tan_double)
    if tan_double != Fraction(5, 12) or tan_quadruple != Fraction(120, 119):
        raise ReplayError("exact Machin tangent reduction failed")
    machin_tangent = (tan_quadruple - Fraction(1, 239)) / (
        1 + tan_quadruple * Fraction(1, 239)
    )
    # This validator is deliberately before the pi enclosure.  A numerical
    # range assertion is not enough: the immutable schema must also retain
    # the common injectivity interval, both tangent values, and the exact
    # principal-branch conclusion.
    validated_branch = validate_machin_branch_certificate(
        branch_certificate,
        observed_theta_tangent=machin_tangent,
    )

    lower5, upper5 = alternating_arctan_bounds(5, 4)
    lower239, upper239 = alternating_arctan_bounds(239, 4)
    pi_lower = 4 * (4 * lower5 - upper239)
    pi_upper = 4 * (4 * upper5 - lower239)
    if not (Fraction(3) < pi_lower < pi_upper < Fraction(22, 7)):
        raise ReplayError("exact rational Machin enclosure did not prove 3<pi<22/7")

    # 14*pi<44 is exactly 7(1+2*pi)<51, hence 7/51<rho_c.
    if not 14 * pi_upper < 44:
        raise ReplayError("exact upper pi bound did not prove 7/51<rho_c")

    # On rho_c<=rho<1, 0<1-rho<=1-rho_c and therefore
    # z=pi/(1-rho)>=pi/(1-rho_c)=pi+1/2>7/2.  Thus
    # k11^2=z^2+132>49/4+132=577/4>144, so k11>12.
    if not pi_lower + Fraction(1, 2) > Fraction(7, 2):
        raise ReplayError("exact lower pi bound did not prove z>7/2")
    if not Fraction(49, 4) + 132 > 144:
        raise ReplayError("exact rational square comparison for k11>12 failed")
    return ExactConstants(
        pi_lower,
        pi_upper,
        validated_branch,
        K11_GUARD_DOMAIN,
    )


class Relation(IntEnum):
    BELOW = -1
    EQUAL = 0
    ABOVE = 1


@dataclass(frozen=True)
class FaceSigns:
    rho_vs_rho_c: Relation
    rho_vs_39_over_50: Relation
    k_vs_k11: Relation
    k_vs_u: Relation
    k_vs_200: Relation


@dataclass(frozen=True)
class SetClassification:
    in_d20: bool
    compact_theorem_applies: bool
    aggregate_theorem_applies: bool
    compact_owner: bool
    aggregate_owner: bool
    in_proposed_d21: bool


def classify_faces(signs: FaceSigns) -> SetClassification:
    in_d20 = (
        signs.rho_vs_rho_c >= Relation.EQUAL
        and signs.rho_vs_39_over_50 == Relation.BELOW
        and signs.k_vs_k11 == Relation.ABOVE
        and signs.k_vs_u == Relation.BELOW
    )
    compact_theorem = in_d20 and signs.k_vs_200 <= Relation.EQUAL
    aggregate_theorem = in_d20 and signs.k_vs_200 >= Relation.EQUAL
    compact_owner = in_d20 and signs.k_vs_200 <= Relation.EQUAL
    aggregate_owner = in_d20 and signs.k_vs_200 == Relation.ABOVE
    proposed = in_d20 and not (compact_owner or aggregate_owner)
    return SetClassification(
        in_d20,
        compact_theorem,
        aggregate_theorem,
        compact_owner,
        aggregate_owner,
        proposed,
    )


def relation(left: Fraction, right: Fraction) -> Relation:
    return Relation.BELOW if left < right else Relation.ABOVE if left > right else Relation.EQUAL


def classify_live_frequency(k: Fraction, k11: Fraction, upper: Fraction) -> SetClassification:
    return classify_faces(
        FaceSigns(
            Relation.EQUAL,
            Relation.BELOW,
            relation(k, k11),
            relation(k, upper),
            relation(k, Fraction(200)),
        )
    )


@dataclass(frozen=True)
class SetReplay:
    exhaustive_sign_rows: int
    ordering_cases: int


def _validate_classification(signs: FaceSigns, result: SetClassification) -> None:
    if result.compact_owner and result.aggregate_owner:
        raise ReplayError(f"double subtraction owner for signs {signs}")
    if result.in_d20 != (result.compact_owner or result.aggregate_owner):
        raise ReplayError(f"D20 is not the exact disjoint owner union for signs {signs}")
    if result.in_proposed_d21:
        raise ReplayError(f"proposed D21 is nonempty for signs {signs}")
    if result.compact_owner and not result.compact_theorem_applies:
        raise ReplayError(f"compact owner lacks compact theorem guard for signs {signs}")
    if result.aggregate_owner and not result.aggregate_theorem_applies:
        raise ReplayError(f"aggregate owner lacks aggregate theorem guard for signs {signs}")
    if result.in_d20 and signs.k_vs_200 == Relation.EQUAL:
        if not (result.compact_theorem_applies and result.aggregate_theorem_applies):
            raise ReplayError("K=200 theorem overlap was lost")
        if not result.compact_owner or result.aggregate_owner:
            raise ReplayError("K=200 is not uniquely compact-owned")


def verify_exact_set_logic() -> SetReplay:
    rows = 0
    for rho_c_sign in Relation:
        for upper_rho_sign in Relation:
            for k11_sign in Relation:
                for upper_k_sign in Relation:
                    for k200_sign in Relation:
                        signs = FaceSigns(
                            rho_c_sign,
                            upper_rho_sign,
                            k11_sign,
                            upper_k_sign,
                            k200_sign,
                        )
                        _validate_classification(signs, classify_faces(signs))
                        rows += 1

    interior = FaceSigns(
        Relation.EQUAL,
        Relation.BELOW,
        Relation.ABOVE,
        Relation.BELOW,
        Relation.BELOW,
    )
    if not classify_faces(interior).in_d20:
        raise ReplayError("included rho=rho_c face was lost")
    if classify_faces(replace(interior, rho_vs_rho_c=Relation.BELOW)).in_d20:
        raise ReplayError("rho=7/51/below-rho_c guard entered D20")
    if classify_faces(replace(interior, rho_vs_39_over_50=Relation.EQUAL)).in_d20:
        raise ReplayError("excluded rho=39/50 face entered D20")
    if classify_faces(replace(interior, k_vs_k11=Relation.EQUAL)).in_d20:
        raise ReplayError("excluded K=k11 face entered D20")
    if classify_faces(replace(interior, k_vs_u=Relation.EQUAL)).in_d20:
        raise ReplayError("excluded K=U face entered D20")

    cases = (
        (Fraction(150), (Fraction(14), Fraction(149))),
        (Fraction(200), (Fraction(14), Fraction(199))),
        (Fraction(250), (Fraction(14), Fraction(200), Fraction(201), Fraction(249))),
    )
    for upper, interior_points in cases:
        for k in interior_points:
            result = classify_live_frequency(k, Fraction(13), upper)
            if not result.in_d20:
                raise ReplayError(f"U-ordering interior point was lost: U={upper}, K={k}")
            _validate_classification(
                FaceSigns(
                    Relation.EQUAL,
                    Relation.BELOW,
                    relation(k, Fraction(13)),
                    relation(k, upper),
                    relation(k, Fraction(200)),
                ),
                result,
            )
        if classify_live_frequency(upper, Fraction(13), upper).in_d20:
            raise ReplayError(f"strict U face entered D20 when U={upper}")
    if not classify_live_frequency(Fraction(200), Fraction(13), Fraction(250)).compact_owner:
        raise ReplayError("U>200 case did not assign K=200 uniquely to compact owner")
    if classify_live_frequency(Fraction(200), Fraction(13), Fraction(200)).in_d20:
        raise ReplayError("U=200 case did not exclude the strict upper face")
    if classify_live_frequency(Fraction(200), Fraction(13), Fraction(150)).in_d20:
        raise ReplayError("U<200 case incorrectly retained K=200")
    return SetReplay(rows, len(cases))


@dataclass(frozen=True)
class AuditResult:
    authenticated_inputs: Mapping[str, str]
    constants: ExactConstants
    set_replay: SetReplay
    compact_frozen: CompactReplay
    compact_high: CompactReplay
    aggregate_frozen: AggregateReplay
    aggregate_high: AggregateReplay
    analytic_chain_claimed: bool = False


def run_audit(high_precision: int = 384) -> AuditResult:
    if high_precision < 384:
        raise SchemaError("higher-precision replay must use at least 384 bits")
    authenticated = authenticate_inputs()
    compact, aggregate = load_sealed_modules()
    validate_static_proof_paths()
    constants = verify_exact_constants()
    set_replay = verify_exact_set_logic()
    compact_frozen, compact_high = replay_compact(compact, high_precision)
    aggregate_frozen, aggregate_high = replay_aggregate(aggregate, high_precision)
    enforce_aggregate_scope(base_frequency=AGGREGATE_BASE_K, universal_frequency_claim=False)
    return AuditResult(
        authenticated,
        constants,
        set_replay,
        compact_frozen,
        compact_high,
        aggregate_frozen,
        aggregate_high,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--high-precision",
        type=int,
        default=384,
        help="higher replay precision in bits (minimum 384)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = run_audit(args.high_precision)
    except Exception as exc:
        print("ROUND21_EXACT_D20_CLOSURE_A4 FAIL")
        print(f"first_issue={type(exc).__name__}: {exc}")
        return 1
    print("ROUND21_EXACT_D20_CLOSURE_A4 PASS")
    print(f"authenticated_inputs={len(result.authenticated_inputs)}")
    print(
        "exact_constants=PASS "
        f"(7/51<rho_c and k11(rho)>12 for {result.constants.k11_guard_domain})"
    )
    print(
        "exact_set=PASS "
        f"({result.set_replay.exhaustive_sign_rows} sign rows; "
        "D20=C21 disjoint-union T21; proposed D21 empty)"
    )
    for replay in (result.compact_frozen, result.compact_high):
        cert = replay.certificate
        print(
            f"compact[{replay.precision_bits}]=PASS leaves={len(cert.leaves)} "
            f"floor_comparisons={cert.generated_floor_comparisons} digest={cert.digest}"
        )
    for replay in (result.aggregate_frozen, result.aggregate_high):
        print(
            f"aggregate_base_K200[{replay.precision_bits}]=PASS boxes={replay.result.box_count} "
            f"sign_checks={replay.sign_checks} endpoint_checks={replay.endpoint_containments} "
            f"derivative_points={replay.derivative_points}"
        )
    print("aggregate_scope=finite outward predicates at K=200 only")
    print("analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
