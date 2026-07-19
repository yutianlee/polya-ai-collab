# Round 18 Derived-State Final Consistency Audit

Date: 2026-07-14

Role: independent post-application audit of the Round 18 judge, accepted proof
and reviews, authoritative obligation graph, and synchronized narrative state.
No pre-existing file was modified by this audit.

## Verdict

**PASS. First issue: none in the final bytes.**

The Round 18 mathematics, authoritative graph, and all synchronized
derived-state summaries agree. The exact nonempty `D18` is the only current
residual routed to Round 19; no live instruction sends analytic or certified
work back to `D17`.

## Audit trail: stale routing caught and fixed

The initial audit correctly stopped the commit after finding two actionable
post-Round-17 strings: the parent certification falsification ledger routed a
future certificate to `D17`, and the Round 17 pilot `next_action` routed any
later certificate to `D_17`. Re-audit also found four accumulated
present-tense falsification cases that described `D17` as the residual or
blocker after it had been replaced by `D18`.

Before this final verdict, the state synthesizer:

- changed the parent certification rule and both pilot `next_action` fields
  so any new certificate is routed only to the exact `D18`;
- explicitly labelled the four retained `D17` blocker/set-arithmetic cases
  as historical Round 17 checkpoints; and
- refreshed the graph hash in the validation report and reading packet.

The final global `D17` sweep leaves only correct history and provenance:
`D18=D17\setminus C18`, `C18\subset D17`, Round 17 coverage facts for
`B0/B1`, explicitly historical checkpoints, and rules forbidding a reversion
from `D18` to `D17`. None is a current or future routing instruction.

## Checks that passed

### Accepted theorem, new set, and exact residual

- The judge, incumbent proof, isolated clean-room proof, independent exact
  audit, cross-comparison, source audit, and fresh adversarial referee agree
  on the complete closed theorem band

  $$
  \rho_c\leq\rho\leq\frac78,
  \qquad z_\rho\leq K\leq k_5(\rho).
  $$

- They agree that the genuinely new set is exactly

  $$
  \mathcal C_{18}
  =\left\{\rho_c\leq\rho<\frac78,
  \quad k_2(\rho)<K\leq k_5(\rho)\right\}.
  $$

  Thus `K=k_2` retains its Round 17 owner, `K=k_5` is newly covered, and
  `rho=7/8` retains its endpoint owner.

- Exact subtraction is reproduced consistently in the graph,
  `current_state.md`, `best_proof_draft.md`, `gap_register.md`,
  `lemma_bank.md`, `next_round_prompts.md`, `last_validation_report.md`, and
  `reading_packet.md`:

  $$
  \mathcal D_{18}
  =\left\{\rho_*<\rho<\rho_c,
  \ \frac1{2\rho}<K<U(\rho)\right\}
  \cup
  \left\{\rho_c\leq\rho<\frac78,
  \ k_5(\rho)<K<U(\rho)\right\}.
  $$

  All four frequency faces are strict. The witness `(rho,K)=(1/2,30)` is
  retained, so no document accidentally closes the theorem.

- `B0` and `B1` are consistently retained as certified regression evidence
  inside `C17` and are not subtracted again from `D18`.

### Proof and source boundary

- The fixed-channel zero-extension/min--max comparison is consistently
  labelled internal. The Lorch dependency is restricted to the three
  first-positive-zero bounds at orders `5/2`, `7/2`, and `9/2`, with scope
  `nu>-1`; DLMF supplies only the spherical-Bessel identity.
- The access-controlled full Lorch proof is not claimed to have been
  reconstructed. No shell cross-product, shell-to-ball comparison, higher
  radial exclusion, multiplicity count, or Weyl payment is attributed to
  Lorch.
- All 18 judge-fixed evidence hashes match the inspected files.

### Obligation graph

- The graph has 53 unique obligations and validates acyclically.
- Its observed SHA-256 is
  `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e`,
  matching the validation report and reading packet.
- `SRC-LORCH` is `proved_external_dependency` and
  `SHELL-next-angular-staircase` is `proved_internal` with the five expected
  dependencies and the analytic-envelope implication.
- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`;
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain `open`; `COMP-certified-bessel` remains
  `diagnostic_only`; both pilot children remain `certified`.
- All new dependency and implication edges are reciprocal and no theorem
  target was promoted.

### Round 19 synchronization

- The canonical prompts require freezing and hashing the exact `D18` mask
  before proof work, then a proof-free candidate freeze before isolated A3
  and A4 review.
- They correctly require a combined radial-entry/angular staircase above
  `k5`, explicit treatment of the `2 z_rho` and `k6` walls, and a separate
  proof for `rho_*<rho<rho_c`.
- They record only the proved local ordering
  `k5(rho_c)<2 z_(rho_c)<k6(rho_c)` and do not assert an unproved Round 19
  crossing threshold.
- The validation report consistently records **132 passed, 10 subtests
  passed**, the 12-check residual self-test, the 40-check exact angular
  ledger, successful bytecode compilation, and graph validation.

## Hash record for synchronized state

| artifact | observed SHA-256 |
|---|---|
| `state/current_state.md` | `1512d399b80580513ec49794144d2de11eea16c74ade8220b82867e5e8b6d0b1` |
| `state/best_proof_draft.md` | `149175968bd314f42583d0f11b668d005c16601d5c887e3e4ef51be4369d6f89` |
| `state/gap_register.md` | `5e8817bdd34dec7b120b522085b2773ece9cbcf1bd340909cd17467ec57218a3` |
| `state/lemma_bank.md` | `fbbb96a70374e785d6b635f545c6c6badb7bf1631bc8b5cebea805d72b6cdd64` |
| `state/next_round_prompts.md` | `7d05055b4b884b052f3970bd7b08335dfe63bca25b5ac5a9db8704f6a88db2f7` |
| `state/last_validation_report.md` | `26da601dc9a382b8650654f9460f6268c2fc8f9cea60e2919ddd5356705095f4` |
| `manifests/reading_packet.md` | `650109d64fa4e9e50f1de1e6d0228ae431c391e0029a3d317e5e17ba3a33bc16` |
| `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` |

`python -m math_collab.validate_state_patch --graph
state/proof_obligations.yml` and `git diff --check` both pass on the final
bytes. The semantic routing sweep also passes after the corrections recorded
in the audit trail.
