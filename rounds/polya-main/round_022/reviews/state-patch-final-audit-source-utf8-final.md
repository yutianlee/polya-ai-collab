# Round 22 source-UTF-8 final State-Patch audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

I independently audited
`rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`
against the unchanged 60-obligation baseline. I wrote neither the judge nor
the graph, and I did not inherit either earlier State-Patch verdict.

## Frozen authority and UTF-8 provenance

- Final judge SHA-256:
  `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2`
  (29,037 bytes, 524 LF bytes, zero CR bytes, terminal LF).
- Baseline graph SHA-256:
  `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`
  (241,363 bytes).

Strict UTF-8 decoding of the judge succeeds. Exact decoded counts are four
`U+00F3`, zero `U+8D38`, one `U+2014`, and zero `U+FFFD`. The four intended
`P` + `U+00F3` + `lya` sites are at decoded line/column 41:74, 401:66,
405:52, and 512:90. The sole em dash is in the document title. The extracted
JSON contains three of the four `U+00F3` sites and no bad or replacement
code point. Parsing preserves the exact program title, the shell-target next
action, and the round-assessment reason; the required in-memory application
preserves those Python strings and returns the exact reason in its result
messages.

## Complete hash and path replay

Every hash asserted by the final judge, together with the final judge and
baseline authority, matched the current file bytes:

| Artifact | SHA-256 |
| --- | --- |
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` |
| `rounds/polya-main/round_022/exploration/theorem-claim-freeze.md` | `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d` |
| `rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md` | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` |
| `rounds/polya-main/round_022/responses/shell-theorem-incumbent.md` | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` |
| `rounds/polya-main/round_022/reviews/shell-theorem-clean-room.md` | `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12` |
| `rounds/polya-main/round_022/reviews/shell-theorem-assembly-audit.md` | `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56` |
| `rounds/polya-main/round_022/reviews/shell-theorem-cross-comparison.md` | `6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458` |
| `rounds/polya-main/round_022/reviews/shell-theorem-adversarial-referee.md` | `a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9` |
| `state/lemma_packets/SHELL-spherical-shell-nontiling-round22.md` | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` |
| `rounds/polya-main/round_022/exploration/nontiling-claim-freeze.md` | `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a` |
| `rounds/polya-main/round_022/reviews/nontiling-claim-scope-audit.md` | `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7` |
| `rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md` | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md` | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` |
| `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md` | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` |
| `rounds/polya-main/round_022/reviews/spherical-shell-nontiling-adversarial-referee.md` | `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53` |
| `rounds/polya-main/round_022/reviews/program-target-scope-audit-replacement.md` | `0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2` |
| `rounds/polya-main/round_022/reviews/program-target-scope-audit.md` | `d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5` |
| `rounds/polya-main/round_022/judge/judge-022.md` | `a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576` |
| `rounds/polya-main/round_022/reviews/state-patch-final-audit.md` | `b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573` |
| `rounds/polya-main/round_022/judge/judge-022-replacement.md` | `c6a440e9b064bf36925b66e6aea188cce1a624a706da76d9bd74daf417f2d415` |
| `rounds/polya-main/round_022/reviews/state-patch-final-audit-replacement.md` | `ce36df00ec78daca0771bb3e29d5281531beec5d41f22ce07dce15747364eb8d` |
| `rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md` | `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2` |
| `state/proof_obligations.yml` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` |

All 22 Markdown artifact paths embedded in the patch exist. The additional
inconclusive literature note exists and has SHA-256
`31a8bbb71c002daf77690591bd67114e943b3cb869484c517e35036042e52c23`.
The geometry referee is exactly 13,290 bytes with 300 LF bytes and a terminal
LF. The original scope report's 299-line statement is therefore retained as
negative chronology; the corrected replacement scope is positive evidence.
The first judge/audit and the failed UTF-8 replacement judge/audit are also
negative evidence only. None appears in a positive bucket.

## Exactly one in-memory realization

I extracted and parsed the final `State Patch`, validated it against the
baseline, and invoked `apply_state_patch` exactly once, in memory, with
`round_index=22` and
`judge_ref=rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`.
The result was:

- 60 to 61 unique obligations;
- 1 create, 12 updates, 0 rejects, and 6 no-change records;
- `SHELL-spherical-shell-nontiling`, `SHELL-rho-compact`,
  `SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target`
  all `proved_internal`, all with empty blockers;
- direct `SHELL-sturm-liouville-completeness` dependency and reciprocal
  implication for `TARGET-shell-d3`;
- exact reciprocity for every new edge and every direct premise of the five
  promoted obligations;
- no dangling references, no open direct premise of a promoted obligation,
  and acyclic dependency and implication graphs;
- exact permitted-dependency ledgers, distinct clean-room roles, and existing
  clean-room/adversarial artifacts for all five obligations;
- geometry and spectral tracks separated until their conjunction at
  `POLYA-program-target`; and
- `COMP-certified-bessel`, both certified pilots, the ellipse track, the
  certificate-family track, and `SRC-mathieu-ellipse` byte-for-byte unchanged
  as in-memory objects.

The only changed pre-existing objects were the 12 named updates. No top-level
graph field drifted. Post-realization graph validation returned no issue. The
on-disk graph was not written and remained at SHA-256 `a7f8c093...` after the
audit.

## Mathematical and scope boundary

The realized statements exactly retain strict counting, `Lambda>=0`, the
positive-spectrum `K=0` step, the disjoint ratio owners, empty `D21`, Weyl
constant `L_3=1/(6 pi^2)`, and the correct `R^2 Lambda` dilation. The result
is only the inequality for all genuine three-dimensional shells `0<r<R`.
The separate geometry statement covers all rigid motions, pairwise-disjoint
interiors, exact and almost-everywhere coverage, and the closed-copy
formulation after removal of the countable null boundary union. The two
results quantify over literally the same shell class.

Neither the judge nor the patch claims the general Pólya conjecture,
literature novelty, priority, or publication readiness. Failed provenance
artifacts remain negative chronology and the literature note remains
inconclusive.

## Checker hygiene

One discarded inline-shell probe produced two harness-only artifacts. First,
PowerShell converted non-ASCII literals embedded in that probe to `?`, so
literal comparisons falsely flagged the four correct `U+00F3` sites and the
title em dash. An ordinal-based read-only replay on the same bytes passed all
locations and counts. Second, an overbroad novelty matcher flagged the
negative phrases `no literature novelty` and `makes no claim`; exact
negative-context checks passed. Neither artifact concerned the judge bytes,
the parsed patch, the in-memory graph delta, or the mathematical claim.

## Final determination

**PASS. First issue: none.** The final source-UTF-8 judge is authenticated,
its patch passes the application gate in one in-memory realization, and the
authoritative graph remains untouched pending the lead's application.
