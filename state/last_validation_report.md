# Last Validation Report

Date: 2026-07-15

Round: 21 lemma post-application synchronization

## Decision

**PASS. First unsupported implication: none at the Round 21 lemma boundary.**

This is not a full-theorem promotion report. It authenticates the exact
closure of the Round 20 residual and the synchronized state from which the
separate theorem-level lifecycle begins.

The audited State Patch was applied exactly once in commit `13e9534`. The
authoritative graph is `state/proof_obligations.yml`, SHA-256
`a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`.
It contains 60 unique obligations and validates with no dangling reference,
impermissible dependency, duplicate relationship, or graph cycle.

The realized patch operation is exact:

- 57 obligations before and 60 after;
- 3 creates;
- 13 updates;
- 0 rejected operations; and
- no pre-existing status change.

The independent post-application audit is
`rounds/polya-main/round_021/reviews/state-patch-lemma-application-audit.md`,
SHA-256
`c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef`.
It reconstructs the patch in memory from the committed 57-node baseline and
finds exact equality with the applied graph after normalizing only the single
generated application timestamp.

## Promoted lemma boundary

The three created obligations are:

- `CERT-round21-compact-proxy`: `certified`;
- `CERT-round21-aggregate-tail`: `certified`; and
- `SHELL-exact-d20-closure`: `proved_internal`.

Let

$$
\rho_c=\frac1{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_{11}(\rho)=\sqrt{z_\rho^2+132}.
$$

The historical Round 20 residual is

$$
\mathcal D_{20}=
\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
$$

The compact theorem is strict on
$[7/51,39/50]\times[12,200]$. Its deterministic certificate has 10,580
exact rational leaves and was replayed at 256- and 384-bit precision. The
aggregate finite certificate has 1,286 ratio boxes at 192 and 384 bits and
owns only its $K=200$ base signs. A3's independent analytic derivative,
curvature, and two-integration chain owns the universal $K\ge200$
propagation.

The exact guards are

$$
\frac7{51}<\rho_c,\qquad
k_{11}(\rho)>12\quad(\rho_c\le\rho<1).
$$

They give the disjoint residual split into $K\le200$ and $K>200$, with
$K=200$ compact-owned. The faces $\rho=39/50$, $K=k_{11}$, and $K=U$ are
outside $\mathcal D_{20}$ and are not subtracted again. Consequently

$$
\boxed{\mathcal D_{21}=\varnothing.}
$$

## Executable provenance and reproduced gates

The accepted wrapper authenticates 18 input files. It reads the sealed
producer source once, hashes those exact bytes, strict-decodes UTF-8,
compiles with inherited flags disabled and optimization zero, and directly
executes a registered cache-free module. It reproduces 243 exact sign rows,
all 10,580 compact leaves, all 1,286 aggregate base boxes, and the same
canonical digests.

The accepted validation ledger is:

- exact residual classifier: 47 tests passed;
- final focused source-execution gate: 14 tests passed;
- isolated full repository gate before application: 334 passed,
  1 strict expected xfail, and 10 subtests passed;
- fresh cache files before and after both isolated gates: 0; and
- graph and State-Patch validators: PASS.

The post-application derived-state suite is recorded below after regeneration:

- complete post-application suite: 339 passed, 1 strict expected xfail,
  and 10 subtests passed in 195.92 seconds;
- in-memory source compilation: PASS, 66 tracked Python files;
- strict UTF-8 and C0/DEL scan of changed derived artifacts:
  PASS, 8 synchronized/lifecycle files;
- malformed-LaTeX-command scan: PASS, zero findings; and
- `git diff --check`: PASS.

## Preserved failure chronology

The following are negative or superseded evidence, not promotion support:

1. the initial candidate had isolation ambiguity and inconsistent aggregate
   quantification;
2. the initial aggregate route omitted its spectral bridge;
3. the first exact audit left the Machin principal branch implicit;
4. its replacement lacked mandatory mutation and lifecycle tests;
5. the first fresh referee missed that lifecycle defect;
6. a hardened-referee transcription incorrectly described its context as
   proof-free;
7. the candidate and first judge claimed the false or undefined guard
   $k_{11}(\rho)>12$ for every $\rho\ge\rho_c$; at $\rho=1$ the shell formula
   is singular and $\rho=2$ is an exact counterexample;
8. the corrected guard made the earlier judge and State-Patch audit stale;
   and
9. the first scoped loader could hash `.py` while executing a
   timestamp-valid adjacent `.pyc`.

The final source-execution route closes the last defect. Its malicious-cache
test forces timestamp mode even when `SOURCE_DATE_EPOCH` is present, matches
source size and mtime, installs conflicting semantics, requires source
behavior, and removes the sentry. Superseded unscoped, stale-hash, and
cache-vulnerable artifacts remain in their negative or inconclusive evidence
buckets.

## Status and next boundary

No higher target is promoted:

- `SHELL-rho-compact`: `open`;
- `SHELL-rho-uniformity`: `open`;
- `TARGET-shell-d3`: `open`;
- `POLYA-program-target`: `open`; and
- `COMP-certified-bessel`: `diagnostic_only`.

The obsolete diagnostic-parent dependencies, blockers, and implication on
the theorem path are removed, while the parent and its two legacy pilot boxes
remain regression evidence.

The top-level graph `round_selection` prose remains historical orchestration
metadata by design; it is not copied into the next workflow. Current
obligation statuses and `next_action` fields govern the Round 22 boundary.

The next admissible work is a coherent theorem assembly covering $K=0$,
strict counting, every ratio seam, the Weyl-volume normalization, and scaling
to arbitrary shells. It must then pass a fresh clean-room theorem proof, a
separate adversarial theorem referee, an adversarial non-tiling review, and a
program-scope audit before any higher State Patch is proposed.
