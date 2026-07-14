# Round 20 Derived-State Final Audit

Date: 2026-07-15

Frozen synchronization commit: `63fb84bd5c929e5f5a43d0df73d91707df4bceb8`

## Verdict

**FAIL. First issue:** `state/current_state.md` still identifies
`\mathcal D_{19}` as the live residual in two sentences of its historical
Round 18 section. The authoritative applied graph and Round 20 judge instead
make the exact live residual

$$
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

Specifically, lines 313 and 321 of the frozen file say, respectively,
“superseded by the live $\mathcal D_{19}$” and “strictly smaller live
residual $\mathcal D_{19}$.” Those statements were valid after Round 19 but
are obsolete after the applied Round 20 State Patch. They contradict the
correct live boundary at the beginning and end of the same file and violate
the requirement that no stale prompt direct Round 21 work toward a
superseded residual. The two occurrences must describe $\mathcal D_{19}$ as
historical and identify $\mathcal D_{20}$ as live before this derived-state
bundle can pass.

I did not repair any supplied artifact.

## Frozen-byte authentication

The audited commit is the current `HEAD`, its worktree was clean before this
report was written, and the requested hashes all reproduce exactly:

| artifact | observed SHA-256 | result |
|---|---|---|
| `state/proof_obligations.yml` | `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd` | PASS |
| `state/current_state.md` | `dd3bc9ab0f2be76e000c160102e4a4fad9013a8c41ff294d5b170577c33bc916` | PASS |
| `state/gap_register.md` | `987004faa180e2c6cd4914f9f46c2e21bb361aec9bd5bd739581a98bf8392608` | PASS |
| `state/lemma_bank.md` | `560d5d2cd713122fae314ecc2efd1023bcd2d553bfb9741cead741928545f8e9` | PASS |
| `state/best_proof_draft.md` | `7c215ba222d4aa2e15757440a84e3cf0bbea7f2686394adfb9eadbd75cf41a1b` | PASS |
| `state/last_validation_report.md` | `0e5e72358ef6180c69d4e5236f8398af17727cac9431c51602182d7d83d80f06` | PASS |
| `state/next_round_prompts.md` | `4ebaa57ba855eac95dab2e150c571654a98a852afb6fe0b27008aa2d22188981` | PASS |
| `manifests/reading_packet.md` | `9947ba9381664cba6501fd2d198d06df3f3aeb0ceeef686e1caa9ec69610d427` | PASS |
| `computations/tests/test_round20_post_promotion_lifecycle.py` | `0120acb5491c0ccaa9ad7401e5ed5f828219b4aa925dc17570c3a781fc2c91bb` | PASS |

The authoritative Round 20 judge remains byte-identical at SHA-256
`3acd0b9aec2aaa52f791bd8656cf6b53327c11eed5f3c4c51fe8352bee9782fa`.
All 26 rows of its fixed-evidence table were independently replayed. The
baseline graph row was read from commit
`658674117632d60990ac9b9046aa0fcff9e91a62`; every other row was checked
against its current file. All hashes match. The two created obligations have
28 embedded `artifact_hashes` entries collapsing to the same 26 distinct
judge hashes. Across the complete authoritative graph, 860 evidence,
source-card, or review-path occurrences collapse to 234 distinct paths; no
path is missing.

## Mathematical and status consistency

Apart from the stale “live $\mathcal D_{19}$” wording above, the synchronized
material agrees with the graph and judge on the substantive Round 20
boundary:

- the graph has 57 unique obligations and validates;
- `SRC-ROUND20-BESSEL-ZEROS` alone is newly
  `proved_external_dependency`, with indispensable external numerical scope
  restricted to $j_{21/2,1}>69/5$ and the labelled DLMF identities;
- `SHELL-combined-closure` alone is newly `proved_internal`;
- all higher-radial zeros, the strengthened order-$13/2$ and order-$15/2$
  first-zero bounds, shell comparison, angular propagation, inventories,
  multiplicities, payments, and subtraction remain internal;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain `open`;
- `COMP-certified-bessel` remains `diagnostic_only`, and neither inherited
  certified box is subtracted again;
- the correct $\mathcal D_{20}$ faces are otherwise preserved:
  $\rho=\rho_c$ is included only strictly above $k_{11}$,
  $\rho=39/50$ is optical-owned, $K=k_{11}$ is staircase-owned, and
  $K=K_0=U$ is excluded;
- the witness
  $k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2)$ correctly proves that
  $\mathcal D_{20}$ is nonempty;
- the initial candidate-release failure, corrected release, A3 addendum,
  both failed A4 cycles, final repaired A4 bundle, zero audit,
  cross-comparison, referee, judge, and State-Patch audit are retained in
  their correct chronological and evidentiary roles.

The Round 21 compact and aggregate routes are consistently described as
independently audited but unpromoted. No scoped Round 21 certificate
obligation, empty successor residual, shell theorem, or program theorem is
claimed as graph state. The next-round material correctly requires a new
residual freeze, proof-free compact and aggregate certificate contracts,
candidate freeze, isolated A3 reconstruction, candidate-specific A4 audit,
cross-comparison, fresh lemma referee, judge, and State-Patch audit. It also
keeps future evidence on scoped `CERT-round21-compact-proxy` and
`CERT-round21-aggregate-tail` obligations rather than broadening the legacy
diagnostic parent, and reserves theorem-level and program-scope reviews for
after exact residual closure is promoted.

## Secondary presentation defect

Seven new display lines in four supplied files lost the backslash before
`qquad`, so TeX renders the letters `qquad` rather than the spacing command:

- `state/next_round_prompts.md`: lines 24 and 30;
- `manifests/reading_packet.md`: lines 33 and 39;
- `state/last_validation_report.md`: line 75;
- `state/lemma_bank.md`: lines 455 and 461.

This does not change the intended inequalities, but it is a repeated
derived-document defect and should be corrected together with the blocking
live-residual wording.

## Lifecycle and reproduction results

The lifecycle design itself is correct:

- graph validation: **PASS**;
- focused Round 19 lifecycle, Round 20 residual, and Round 20 lifecycle
  suite: **51 passed**;
- the Round 20 manifest authentication test remains a normal running test:
  `TestManifest::test_authenticated_inputs_match_frozen_bytes` passed;
- both new Round 20 post-promotion lifecycle tests passed and authenticate
  the immutable original test bytes plus advancement of both mutable state
  inputs;
- complete suite: **273 passed, 1 strict expected xfail, 10 subtests
  passed**;
- the sole xfail is exactly
  `computations/tests/test_round19_residual_mask.py::TestManifest::test_authenticated_inputs_match_the_committed_bytes`;
- in-memory Python source compilation: **PASS, 62 tracked files**;
- strict UTF-8 and C0/DEL scan of the eight supplied derived artifacts:
  **PASS**;
- path and fixed-hash replay: **PASS**;
- `git diff --check 63fb84b^ 63fb84b`: **PASS**.

## Decision

The frozen synchronization cannot be accepted as final because it contains
two explicit stale live-boundary assertions. After repairing those two
assertions and the secondary TeX escapes, reseal the derived bytes and rerun
this final audit. No mathematical promotion or graph change is required for
that repair.
