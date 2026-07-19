# Round 22 replacement State-Patch final audit

Date: 2026-07-15

Role: independent replacement-judge and one-time State-Patch auditor

## Verdict

**FAIL — encoding/provenance only. First issue:** the exact replacement judge
contains the Chinese code point `U+8D38` in place of `U+00F3` in all four
intended occurrences of `Pólya`. The resulting token is `P\u8d38lya`, not
`Pólya`.

This is the sole issue found. The patch syntax, one-time in-memory
realization, mathematical statements apart from that spelling corruption,
dependency closures, statuses, blockers, reciprocal edges, acyclicity,
review roles, premise ledgers, artifact hashes, evidence classifications,
scaling, non-tiling scope, and no-novelty boundary otherwise pass.

The patch is not authorized for application on these bytes. I did not write
the authoritative graph, and its SHA-256 remained unchanged before and after
the audit.

## 1. Frozen authentication

The requested artifacts reproduce exactly:

| artifact | SHA-256 | bytes | raw LF | terminal LF |
| --- | --- | ---: | ---: | :---: |
| replacement judge | `c6a440e9b064bf36925b66e6aea188cce1a624a706da76d9bd74daf417f2d415` | 27,500 | 504 | yes |
| baseline graph | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 | yes |
| replacement scope audit | `0ff8940a09adae1b510fcaa43bcd9d1eefeba903a3d20dd0d3997dd0a44960b2` | 15,147 | 347 | yes |
| superseded scope audit | `d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5` | 15,538 | 381 | yes |
| failed first judge | `a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576` | 25,102 | 469 | yes |
| failed first audit | `b0a8e35d2a1adf291886b5f44215a2086687ab642d9358cdf994480acbf10573` | 15,072 | 352 | yes |
| geometry adversarial referee | `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53` | 13,290 | 300 | yes |

The geometry referee has zero CR bytes, 300 entries under
`.NET File.ReadAllLines`, and last numbered line
`300:of this verdict.` under `rg -n '^'`. The replacement scope audit therefore
correctly repairs the former 299-line metadata error.

The baseline graph parses as 60 obligations with 60 unique identifiers.
Repository graph validation and pre-application patch validation both return
no issues.

## 2. First issue: exact encoding corruption

UTF-8 decoding of the replacement judge gives four `U+8D38` occurrences and
zero `U+00F3` occurrences. They are:

| line | location | exact defective token |
| ---: | --- | --- |
| 32 | general-conjecture disclaimer | `P\u8d38lya` |
| 386 | `TARGET-shell-d3.next_action` | `P\u8d38lya` |
| 390 | `POLYA-program-target.title` | `P\u8d38lya` |
| 492 | `round_assessment.reason` | `P\u8d38lya` |

The defective character is encoded by the bytes `e8 b4 b8`. By contrast, the
failed first judge and the replacement program-scope audit each contain four
correct `U+00F3` occurrences and zero `U+8D38` occurrences.

This is not merely invisible prose damage. Applying the patch would replace
the authoritative program title with
`Program target: exact Dirichlet P\u8d38lya for non-tiling three-dimensional
spherical shells`, and would store the same corruption in the spectral
target's next action. The judge also no longer literally says that it does
not close the general **Pólya** conjecture, because the theorem name in that
sentence is corrupted.

The formulas and quantified theorem statements remain mathematically
unambiguous, and no positive global-conjecture assertion appears. Nonetheless,
an audited State Patch must not introduce a known encoding corruption into
authoritative state, so this exact judge cannot receive a PASS.

## 3. Exactly one in-memory realization

I extracted the final `## State Patch` fence as one valid JSON mapping and
called `apply_state_patch` exactly once on an in-memory copy, with
`round_index=22` and
`judge_ref=rounds/polya-main/round_022/judge/judge-022-replacement.md`.
No graph writer was imported or called.

The result was exact:

- 60 obligations became 61 obligations with 61 unique identifiers;
- create: one, only `SHELL-spherical-shell-nontiling`;
- update: 12 distinct existing obligations;
- reject: zero; and
- no-change bookkeeping: six exact entries.

The 12 update ids are
`SHELL-phase-enclosures`, `SHELL-lattice-count`,
`SHELL-fixed-rho-high-energy`, `SHELL-sturm-liouville-completeness`,
`SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`,
`SHELL-rho-compact-analytic-envelope`, `SHELL-exact-d20-closure`,
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target`.

Post-realization graph validation reports zero issues. The five relevant
nodes all become `proved_internal` with empty blockers:

- `SHELL-spherical-shell-nontiling`;
- `SHELL-rho-compact`;
- `SHELL-rho-uniformity`;
- `TARGET-shell-d3`; and
- `POLYA-program-target`.

The only existing status changes are the last four nodes, each from `open` to
`proved_internal`. Recursive premise closure has no `proposed`, `open`,
`blocked`, `source_audit_required`, `diagnostic_only`, or `rejected` node:

| root | premises excluding root | status composition |
| --- | ---: | --- |
| `TARGET-shell-d3` | 35 | 27 `proved_internal`, 6 `proved_external_dependency`, 2 `certified` |
| `POLYA-program-target` | 37 | 29 `proved_internal`, 6 `proved_external_dependency`, 2 `certified` |

Including each root gives 36 and 38 nodes respectively. The legacy
`COMP-certified-bessel` node is absent from both closures.

## 4. Graph invariants and unchanged scope

The exact edge totals change as follows:

| field | before | after | delta |
| --- | ---: | ---: | ---: |
| dependencies | 219 | 221 | +2 |
| implies | 128 | 133 | +5 |
| blockers | 8 | 6 | -2 |
| permitted dependencies | 150 | 161 | +11 |

The dependency additions are exactly the direct
`SHELL-sturm-liouville-completeness -> TARGET-shell-d3` premise and the
`SHELL-spherical-shell-nontiling -> POLYA-program-target` premise. Their
reciprocal `implies` entries are present. The three further `implies`
additions supply the previously missing reverse metadata from
`SHELL-phase-enclosures`, `SHELL-lattice-count`, and
`SHELL-fixed-rho-high-energy` to `SHELL-rho-compact`.

Every premise of the five promoted nodes is reciprocated, including the
direct Sturm edge used at `K=0`. The complete dependency graph and complete
implication graph are both acyclic. Every dependency, implication, blocker,
and permitted-dependency target exists; there are no dangling or duplicate
edge entries. For each of the five promoted nodes, dependencies and permitted
dependencies agree exactly.

The geometry node has no premise and neither depends on nor implies
`TARGET-shell-d3`. The spectral and geometry theorems meet only at
`POLYA-program-target`.

All six no-change entries remain exact-equal, as do every node in the
`ellipse_parallel` and `certificate_family` tracks. In particular,
`COMP-certified-bessel` retains canonical node SHA-256
`a9b0b137820272d015daa50fe77753fc406ce69e382bc3551ddc1f2f96378b15`,
status `diagnostic_only`, empty `implies`, and no link into the completed
theorem path. Its Round 8 and Round 17 pilots also remain exact-equal.

## 5. Evidence, roles, and mathematical scope

All 49 SHA-256 occurrences in the replacement judge reduce to 19 distinct
authenticated files, and every occurrence reproduces. The three
`artifact_hashes` mappings contain 29 occurrences; every key is associated
with the correct file and hash. All 65 patch evidence/review path occurrences,
covering 19 unique files, exist.

The replacement program-scope audit is positive evidence. The superseded
scope report and first failed State-Patch audit are negative evidence at the
program node, and the limited literature note remains inconclusive. The
failed judge and failed audit hashes are preserved as negative chronology.

All five promoted theorem/bottleneck nodes have distinct lead, clean-room,
and adversarial roles; `review_independence` is `clean_room`; their exact
clean-room and adversarial artifact lists are nonempty, disjoint, and exist.
Their premise ledgers contain only the reviewed analytic, endpoint,
positivity, strict-counting, spectral-target, and geometry-target premises
appropriate to each node.

Apart from the four corrupted theorem-name tokens, the exact statements retain:

- strict counting and every `Lambda>=0`, including the direct positive-spectrum
  treatment of `K=0`;
- the disjoint ratio partition with endpoint ownership and empty `D21`;
- the finite/analytic certificate boundary and compact ownership of `K=200`;
- `L_3=1/(6 pi^2)` and coefficient
  `(2/(9 pi))(R^3-r^3)`;
- the correct scaling identity
  `N_D(A_{r,R},Lambda)=N_D(A_{r/R,1},R^2 Lambda)` for every `R>0`;
- every genuine shell `0<r<R`, with neither degenerate endpoint included;
- non-tiling by all rigid motions with pairwise-disjoint interiors, exact or
  almost-everywhere coverage, and the corresponding closed-copy convention;
  and
- an explicit program-internal, no-literature-novelty-or-priority boundary.

No statement claims the general conjecture, publication novelty, priority,
or readiness for publication. The only problem is that the intended theorem
name in four places is not encoded correctly.

## Required replacement

Replace exactly the four `U+8D38` characters by `U+00F3` using a UTF-8-safe
edit, recompute the judge SHA-256, preserve the current failed judge and this
audit as negative chronology, and run a new independent final State-Patch
audit before application. No mathematical formula, graph edge, status,
evidence classification, role, premise ledger, or proof artifact requires a
substantive change.

## Final determination

**FAIL — encoding/provenance only. First issue:** the replacement judge would
write `P\u8d38lya` into authoritative state and uses that corrupted token in
its general-conjecture disclaimer. All other audited conditions pass. The
authoritative graph remains at the exact 60-node baseline SHA-256
`a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`.
