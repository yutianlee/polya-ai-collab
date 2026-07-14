# Round 20 Derived-State Replacement Audit

Date: 2026-07-15

Repaired synchronization commit:
`c53568533f295e152f33e4dbf5f7474b4fcfaf03`

## Verdict

**PASS. First issue: none.**

The repaired post-Round-20 derived state is consistent with the applied
authoritative graph and Round 20 judge. The stale live-$\mathcal D_{19}$
language identified by the first audit is gone, all affected `\qquad`
display lines are repaired, historical Round 19 statements and formulas
remain intact, and no analogous stale boundary, malformed spacing command,
or Round 21 overclaim was found.

The original FAIL report is preserved byte for byte at
`rounds/polya-main/round_020/reviews/derived-state-final-audit.md`, SHA-256
`9c7a0dc453eea72bc571b99a11743d23ab42d1910f18e2b20c1dd0780eb752f9`.
This replacement audit does not rewrite or supersede that chronology.

## Repaired-byte authentication

The requested repaired and unchanged artifacts reproduce exactly:

| artifact | observed SHA-256 | result |
|---|---|---|
| `state/proof_obligations.yml` | `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd` | PASS |
| `state/current_state.md` | `1bf336ca713a155cd710805fef1b97ac3ae6f2a46692562fb6cbbabc48de64be` | PASS |
| `state/gap_register.md` | `987004faa180e2c6cd4914f9f46c2e21bb361aec9bd5bd739581a98bf8392608` | PASS |
| `state/lemma_bank.md` | `e2fd24e117ab57d783c5f70220958c896869edf04cf25abfe5df6b68e76a8730` | PASS |
| `state/best_proof_draft.md` | `3415cd996e8786b7eb37f427f7d855830470a918d3b0109f7da11d62c7ff306e` | PASS |
| `state/last_validation_report.md` | `aa614d7551b4d3524ee22ad055a43833df0f23a9465395c2514919c9351de99e` | PASS |
| `state/next_round_prompts.md` | `61341748ef07a6e937f752140b407a83576ae69c62061c1c28ae488acf43e4d2` | PASS |
| `manifests/reading_packet.md` | `97787e8d2c87d9ab15f2144a47e4999d65e904da65916f5c11d39d06bd932778` | PASS |
| `computations/tests/test_round20_post_promotion_lifecycle.py` | `0120acb5491c0ccaa9ad7401e5ed5f828219b4aa925dc17570c3a781fc2c91bb` | PASS |
| `computations/tests/conftest.py` | `b0f0c36c166d81aed6a2dea5c88bf43869ef92b8805f4585b2932c7866943904` | PASS |

The repair commit changes only the six advertised prose artifacts. The
authoritative graph, gap register, lifecycle test, conftest, judge, evidence,
and original FAIL report remain unchanged.

## Repair-specific audit

The former blocking defect is fully repaired. In `state/current_state.md`:

- the Round 18 discussion now says that $\mathcal D_{19}$ was the Round 19
  successor and is historical now;
- the same passage identifies the authoritative live residual as
  $\mathcal D_{20}$;
- the later Round 18 and Round 19 summaries likewise label
  $\mathcal D_{19}$ historical rather than live;
- the current opening boundary and Round 20 update still give the exact live
  formula

  $$
  \mathcal D_{20}
  =\left\{\rho_c\leq\rho<\frac{39}{50},\quad
  k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
  $$

`state/best_proof_draft.md` now labels $\mathcal A_{19}$ and
$\mathcal D_{19}$ as the historical post-Round-19 cover and residual. It
retains the full three-piece $\mathcal D_{19}$ formula, its face ownership,
nonempty witness, theorem bands, and the subsequent exact subtraction to
$\mathcal D_{20}$. The other synchronized files retain every legitimate
$\mathcal D_{19}^{\rm low}$ and $\mathcal C_{20}$ provenance reference.
Thus the repair removes stale current-state language without erasing or
rewriting mathematical history.

All nine previously identified affected display lines now contain escaped
`\qquad` commands. A fresh scan of all seven synchronized prose files found
zero occurrence of `qquad` without an immediately preceding backslash. The
repair also introduces no malformed control sequence, encoding defect, or
changed inequality.

## Semantic and status audit

The repaired bundle continues to match the authoritative Round 20 result:

- the graph validates with 57 unique obligations;
- `SRC-ROUND20-BESSEL-ZEROS` is the narrowly scoped
  `proved_external_dependency`, and its indispensable new external numerical
  payload is only $j_{21/2,1}>69/5$ together with the labelled DLMF
  identities;
- every higher-radial zero, strengthened lower-order first zero, root
  enumeration, shell comparison, angular propagation, inventory,
  multiplicity, Weyl payment, and residual subtraction remains internal;
- `SHELL-combined-closure` is `proved_internal` on exactly its lower,
  staircase, and optical domains;
- $\rho=\rho_c$ remains in $\mathcal D_{20}$ only strictly above
  $k_{11}$, $\rho=39/50$ is optical-owned, $K=k_{11}$ is staircase-owned,
  and $K=K_0=U$ is excluded;
- $U=K_0$ exactly on the live ratio interval, and
  $k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2)$ still proves nonemptiness;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain `open`, while `COMP-certified-bessel`
  remains `diagnostic_only`;
- the inherited $B_0,B_1$ certificates remain regression evidence and are
  not subtracted again.

The complete Round 20 failure chronology is preserved: the first candidate
release failure and repair, A3's passing proof plus immutable corrective
addendum, both failed A4 bundles, the final repaired A4 bundle, zero audit,
cross-comparison, fresh referee, judge, and State-Patch audit retain their
correct positive, negative, or chronological roles.

No Round 21 result has been promoted. The compact and aggregate routes are
described only as audited incumbent evidence. No empty successor residual,
scoped Round 21 certificate obligation, shell theorem, or program theorem is
asserted as current graph state. The workflow still requires a new exact
$\mathcal D_{20}$ freeze, proof-free certificate contracts, candidate
freeze, isolated A3 reconstruction, candidate-specific A4 audit,
cross-comparison, fresh lemma referee, judge, and independently audited
State Patch. Any later certificate promotion is routed through scoped
`CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail` obligations,
not by broadening the legacy diagnostic parent. The separate theorem-level
and program-scope gates remain mandatory after exact residual closure.

## Evidence, lifecycle, and mechanical reproduction

Independent reproduction returned:

- authoritative graph validation: **PASS**;
- all 26 fixed-evidence rows in the judge: **PASS**;
- 28 embedded artifact-hash entries collapsing to the same 26 distinct
  judge hashes: **PASS**;
- 860 graph evidence/source/review path occurrences, 234 distinct paths,
  zero missing: **PASS**;
- focused Round 19 lifecycle, Round 20 residual, and Round 20 lifecycle
  suite: **51 passed**;
- Round 20 manifest authentication remains a normal running PASS;
- both Round 20 post-promotion lifecycle tests: **PASS**;
- complete suite: **273 passed, 1 strict expected xfail, 10 subtests
  passed**;
- sole xfail: the immutable Round 19 pre-promotion live-path assertion,
  exactly as designed;
- in-memory Python compilation: **PASS, 62 tracked files**;
- strict UTF-8 and C0/DEL scan: **PASS, 9 synchronized/lifecycle files**;
- unescaped-`qquad` scan: **PASS, zero findings**;
- `git diff --check c535685^ c535685`: **PASS**.

## Decision

The replacement derived-state synchronization is accepted. It is safe to
use these repaired bytes as the Round 21 starting state. This verdict changes
no proof-obligation status and does not promote either Round 21 route.
