# Round 22 derived-state final audit

Date: 2026-07-15

Auditor role: fresh independent post-application reviewer

## Decision

**PASS. First unsupported implication: none.**

The realized graph, the synchronized state and workflow documents, the
reading-packet generator, both lifecycle test files, and the final validation
ledger agree on one bounded conclusion: the project has an internally proved
strict Dirichlet Pólya theorem for every genuine bounded three-dimensional
spherical shell and a separately proved non-tiling theorem for the same
complete shell class. Nothing audited here supports a claim that the general
Pólya conjecture is solved or a claim of literature novelty, priority,
firstness, publication readiness, or correctness beyond the internal review
boundary.

No open finding remains in the audited files.

## Exact realized graph

The authoritative file is `state/proof_obligations.yml`, SHA-256
`b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`,
257,190 bytes, 4,378 LF bytes, no CR bytes, and a terminal LF. It is canonical
under `dump_graph`, contains 61 obligations with 61 unique identifiers, and
passes the graph validator.

The final State Patch was applied exactly once in commit `d8fe505`. Its
realized ledger is 1 create, 12 updates, 0 rejects, and 6 explicit no-change
decisions, with the sole generated application timestamp
`2026-07-15T14:47:52`. Replaying the source-final patch against the realized
graph is correctly refused because its created geometry identifier already
exists.

The five final nodes

- `SHELL-spherical-shell-nontiling`;
- `SHELL-rho-compact`;
- `SHELL-rho-uniformity`;
- `TARGET-shell-d3`; and
- `POLYA-program-target`

are all `proved_internal` and have empty blockers. The exact dependency
closure of `TARGET-shell-d3` has 35 proper premises, or 36 nodes including
the target. The exact dependency closure of `POLYA-program-target` has 37
proper premises, or 38 nodes including the target. Every node in both closed
sets has status `proved_internal`, `proved_external_dependency`, or
`certified`. Dependency and implication relations are acyclic; every final
theorem-path dependency has its reciprocal implication edge.

The geometry and spectral implication descendants intersect exactly at
`POLYA-program-target`. The direct Sturm--Liouville premise is present on
`TARGET-shell-d3` with the reciprocal edge. The compact reverse edges and
the compact-to-uniform-to-target chain are present.

`COMP-certified-bessel` remains `diagnostic_only`, with empty blockers and
implications, and it is absent from the dependency and blocker lists of the
compact, uniform, spectral-target, and program-target nodes. Its legacy
pilots remain regression evidence only. `ELLIPSE-near-circular` and
`CERT-certificate-family` remain open; their source-audit premises and
alternative implication edges are unchanged. Neither parallel track is a
premise or blocker of the completed shell route.

## Exact mathematical scope

The synchronized theorem uses the strict count

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}.
$$

For every

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R,
$$

and every $\Lambda\ge0$, it states exactly

$$
\boxed{
N_D(A_{r,R},\Lambda)
\le \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2}},
\qquad L_3=\frac1{6\pi^2}.
$$

The derived proof text separately retains $K=0$, the exact ratio partition,
strict spectral and phase walls, the empty successor residual
$\mathcal D_{21}=\varnothing$, Weyl-volume normalization, and the scaling
identity

$$
N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda).
$$

The separately reviewed geometry statement covers the same full
$0<r<R$ family and forbids tilings of $\mathbb R^3$ by congruent
rigid-motion copies with pairwise-disjoint interiors and exact or
almost-everywhere coverage. The open-copy and closed-copy conventions are
handled by removing the countable null union of tile boundaries. No spectral
premise is imported into that geometry node.

The finite certificates retain their exact finite scopes. In particular,
the 10,580 compact leaves do not own an analytic tail, the 1,286 aggregate
boxes own only their $K=200$ base predicates, and no diagnostic computation
is promoted to certification.

## Final authority and failure chronology

The successful authority chain was re-hashed as follows:

| Artifact | SHA-256 |
| --- | --- |
| source-final judge | `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2` |
| source-final pre-application audit | `3d0952f7a0c3aac820427f90249e9f8d5ece5d6f20e1d0bdcc2e9af11f5adc69` |
| source-final post-application audit | `79a46f1e6398cb5887a98dc56142470a3b656b4153f969eec8db07df7604df58` |
| accepted replacement program-scope audit | `0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2` |

The source-final judge strict-decodes as UTF-8 and contains exactly four
U+00F3 characters, one U+2014, zero U+8D38, and zero U+FFFD. Its create,
update, reject, and no-change identifiers exactly match the realized ledger.

The graph preserves, but does not use positively, the following failed or
superseded provenance:

| Failed or superseded artifact | SHA-256 |
| --- | --- |
| first program-scope audit | `d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5` |
| first judge | `a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576` |
| first State-Patch audit | `b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573` |
| UTF-8-corrupted replacement judge | `c6a440e9b064bf36925b66e6aea188cce1a624a706da76d9bd74daf417f2d415` |
| audit rejecting that replacement | `ce36df00ec78daca0771bb3e29d5281531beec5d41f22ce07dce15747364eb8d` |

The first scope cycle misstated the geometry adversarial referee as 299
physical lines. The authenticated referee is 13,290 bytes with 300 LF bytes
and a terminal LF. The later replacement judge contains four actual U+8D38
characters and zero U+00F3 characters. The accepted replacement scope audit
is positive evidence; the five failed artifacts are negative evidence on the
geometry and program nodes. The final judge is only the auto-injected
inconclusive provenance pointer on the created geometry node and does not
replace its positive clean-room and adversarial artifacts. The historical
literature note remains inconclusive.

The immutable theorem, geometry, successful-audit, and failed-chronology
artifact hashes asserted by the Round 22 lifecycle regression all matched
their current bytes.

## Reading-packet and derived-state behavior

`generate_reading_packet` now branches from live graph state. Against the
realized graph it selects the completed-state branch, names the completed
shell target, reports `TARGET-shell-d3` as `proved_internal`, renders the
empty blocker list as `none`, preserves the diagnostic and parallel-track
boundaries, and emits the no-general-conjecture and no-novelty rules. A fresh
in-memory generation contains none of the stale `D_16`, “no complete
all-rho,” or “full theorem remains open” text.

The synchronized reading packet, problem statement, current state, gap
register, lemma bank, proof draft, next-work prompts, and validation report
all use the final graph hash and the same bounded theorem. Historical
pre-Round-22 sections remain explicitly historical. The proof draft's
opening now states the Round 22 internal completion and immediately disclaims
the general conjecture and novelty/priority interpretations.

## Validation reproduced or cross-checked

- graph validator: PASS;
- focused Round 21/22 lifecycle gate: 18 passed in 0.05 seconds on the final
  bytes;
- test collection: 353 tests collected in 1.15 seconds;
- recorded complete repository gate: 352 passed, 1 strict expected xfail,
  and 10 subtests passed in 138.83 seconds; the recorded total is consistent
  with the independently recollected 353 tests;
- in-memory compilation: PASS for 68 Git-visible Python sources (67 tracked
  plus the new untracked Round 22 lifecycle file at audit time), with zero
  compile failures;
- strict UTF-8/control scan: PASS for all 11 modified derived, workflow,
  code, test, and report files; zero U+8D38, U+FFFD, BOMs, forbidden C0
  controls, DEL bytes, CR bytes, or decode failures;
- graph Unicode: canonical decoded graph contains ten U+00F3 characters and
  zero U+8D38 or U+FFFD characters; and
- `git diff --check`: PASS on the final audited diff.

The full 138.83-second suite was not repeated by this auditor because it was
already frozen in the supplied final validation ledger. This audit instead
recollected the entire suite, reran the focused final lifecycle gate, and
independently reproduced the graph, provenance, compilation, Unicode, and
diff checks that are most sensitive to the final synchronized edits.

## Exact audited bytes

The table below freezes every modified input file inspected by this audit,
plus the unchanged realized graph. LF is the count of byte `0x0a`; every
listed file has zero CR bytes.

| File | SHA-256 | Bytes | LF |
| --- | --- | ---: | ---: |
| `state/proof_obligations.yml` | `b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29` | 257,190 | 4,378 |
| `computations/tests/test_round21_post_promotion_lifecycle.py` | `c589896f02ed91a9e1889d950e21700cca770bc5b0cb1931638afabefaac99b0` | 3,724 | 107 |
| `computations/tests/test_round22_final_program_lifecycle.py` | `f30175b33cf0c7a9d1eeb4653d6f5b41881bcd70e6f302e0db761855d3bfb0fa` | 21,946 | 538 |
| `manifests/reading_packet.md` | `50019a8540ecd3daef564037dfc71b862046a1ba5bcd0ff23fc89fa84ccc1236` | 6,566 | 159 |
| `math_collab/proof_obligations.py` | `8f07f41dacc038e498e93bcc2b8ff13bfa56634738d9581fcd9d5c55e54c7e4f` | 28,898 | 715 |
| `problems/polya_conjecture.md` | `a4c1de141e87c144c0bb7475755f744ae5cf3c28a6a77d039be3e33a316175f3` | 4,232 | 138 |
| `state/best_proof_draft.md` | `66f841f281eb158a9495bff18f78e57fd82074d4ee54eb9fa0e0235e3e38d27b` | 47,601 | 1,915 |
| `state/current_state.md` | `3aaf04a925053445c2785e45eff54f42e5ae15d9f3203429046ff9ac09379adb` | 44,644 | 1,322 |
| `state/gap_register.md` | `6862f8e6c396a79bc44dc0d8adc3f2bab783adda8933e3dcdc4c0b323eab5b47` | 14,296 | 279 |
| `state/last_validation_report.md` | `bc74a68b0f2897c3f87ae4a29cd7c7ccebb96b86d6ee3e0cd54354d6f734a573` | 6,202 | 155 |
| `state/lemma_bank.md` | `9679453aba063e8804a294891c51c80ad55a848f0eb8f8dc96feaa0bd5d3b3e6` | 20,663 | 643 |
| `state/next_round_prompts.md` | `a0b43d589fceca11fd1912937cd52e95465aff7650957ecc5ae86a8178368fe7` | 5,418 | 127 |

This audit file is deliberately excluded from the table to avoid a
self-referential hash claim.

## Findings and boundary

Two issues were found during the audit and repaired before the final byte
freeze:

1. the proof draft had an unqualified stale opening sentence saying no
   all-$K$, all-$\rho$ shell proof existed; the opening now records the
   Round 22 project-internal completion and its claim limits, and a lifecycle
   regression rejects recurrence of the stale sentence; and
2. `math_collab/proof_obligations.py` temporarily had mixed line endings,
   which would have made its working-tree SHA-256 differ from the normalized
   committed blob; it is now mechanically normalized to LF-only bytes.

Both repairs were re-hashed, recompiled, and rerun through the focused
lifecycle gate. No other contradiction, dangling dependency, widened
certificate, corrupted Unicode, stale authority hash, or unsupported status
promotion was found.

The first remaining boundary is human, not an internal graph dependency:
line-by-line reconstruction of every bottleneck lemma, manuscript-level
refereeing, and a separate current literature comparison are still required
before external dissemination or any novelty/priority language.
