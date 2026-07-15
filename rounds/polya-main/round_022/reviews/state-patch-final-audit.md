# Round 22 Final State-Patch Audit

Date: 2026-07-15

## Verdict

**FAIL — provenance metadata only. First issue:** the authenticated
`program-target-scope-audit.md` says that the fresh spherical-shell
non-tiling adversarial referee has **299 physical lines**, but the exact
hash-matching file has **300 LF-terminated physical lines**.

This is the first and sole issue. The mathematical theorem and non-tiling
arguments, every declared SHA-256 value, the State Patch syntax and
semantics, the one-time in-memory application, all graph invariants, roles,
premise ledgers, statuses, scopes, and no-novelty boundary otherwise pass.
No mathematical or graph-semantic change is required.

This audit does not apply the patch and does not modify the authoritative
graph. It rejects only the currently authenticated provenance cycle.

## 1. Authenticated judge and baseline

The audited judge is
`rounds/polya-main/round_022/judge/judge-022.md`:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| Round 22 judge | `a7cc398e0014f6e42a6ebd2195b744ec2112331370545a1ff02105ad20eff576` | 25,102 | 469 |
| authoritative graph | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 |

The graph is `state/proof_obligations.yml`. Its hash remained the displayed
baseline value before, during, and after the audit. It parses as 60
obligations with 60 unique identifiers, and the repository graph validator
reports `Graph OK`.

The judge's final `## State Patch` fence extracts as one valid JSON mapping.
The operation counts and identifiers are exact:

- create: one, only `SHELL-spherical-shell-nontiling`;
- update: 12 distinct existing obligations;
- reject: zero; and
- no-change bookkeeping: six.

The 12 update ids are:

1. `SHELL-phase-enclosures`;
2. `SHELL-lattice-count`;
3. `SHELL-fixed-rho-high-energy`;
4. `SHELL-sturm-liouville-completeness`;
5. `SHELL-rho-zero-endpoint`;
6. `SHELL-rho-one-endpoint`;
7. `SHELL-rho-compact-analytic-envelope`;
8. `SHELL-exact-d20-closure`;
9. `SHELL-rho-compact`;
10. `SHELL-rho-uniformity`;
11. `TARGET-shell-d3`; and
12. `POLYA-program-target`.

Both repository validation commands passed on the exact bytes:

```text
python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml
Graph OK

python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/polya-main/round_022/judge/judge-022.md
Patch OK
```

## 2. Exactly one in-memory application

I invoked `apply_state_patch` exactly once, on a loaded in-memory graph, with
`round_index=22` and
`judge_ref=rounds/polya-main/round_022/judge/judge-022.md`. I never called the
graph writer and never invoked a second application.

The returned application result and immediate post-application validation
gave:

- 60 obligations before and 61 after;
- 61 unique post-patch identifiers;
- created: only `SHELL-spherical-shell-nontiling`;
- updated: exactly the 12 ids above, in patch order;
- rejected: none;
- no-change: exactly the six declared entries; and
- zero patched-graph validation issues.

A later audit-harness assertion initially tested one implication tuple in
the same rather than reciprocal orientation. That was an auditor-side test
expression, not a patch failure. I corrected the reciprocity calculation by
static comparison of the already parsed baseline and patch, without invoking
the application function again. The corrected edge delta is recorded below.

## 3. Status, blockers, and dependency closure

All five required resulting obligations have status `proved_internal`:

| obligation | resulting status | blockers after patch |
| --- | --- | --- |
| `SHELL-spherical-shell-nontiling` | `proved_internal` | none |
| `SHELL-rho-compact` | `proved_internal` | none |
| `SHELL-rho-uniformity` | `proved_internal` | none |
| `TARGET-shell-d3` | `proved_internal` | none |
| `POLYA-program-target` | `proved_internal` | none |

The four existing status changes are exactly the last four rows. The
geometry theorem is the only created status. The patch removes the sole
compact blocker from `SHELL-rho-uniformity` and the sole uniformity blocker
from `TARGET-shell-d3`; no required blocker survives.

Recursive dependency closure contains no open, blocked, proposed,
source-audit-required, diagnostic-only, or rejected obligation:

| root | dependency closure | `proved_internal` | `proved_external_dependency` | `certified` |
| --- | ---: | ---: | ---: | ---: |
| `TARGET-shell-d3` | 35 | 27 | 6 | 2 |
| `POLYA-program-target` | 37 | 29 | 6 | 2 |

In particular, `COMP-certified-bessel` is absent from both closures.

## 4. Exact edge delta, reciprocity, and acyclicity

The aggregate list-edge counts are:

| field | before | after | net |
| --- | ---: | ---: | ---: |
| `dependencies` | 219 | 221 | +2 |
| `permitted_dependencies` | 150 | 161 | +11 |
| `implies` | 128 | 133 | +5 |
| `blockers` | 8 | 6 | -2 |

The two dependency additions are exactly:

- `TARGET-shell-d3` depends on
  `SHELL-sturm-liouville-completeness`; and
- `POLYA-program-target` depends on
  `SHELL-spherical-shell-nontiling`.

The five implication additions are exactly:

- `SHELL-phase-enclosures` implies `SHELL-rho-compact`;
- `SHELL-lattice-count` implies `SHELL-rho-compact`;
- `SHELL-fixed-rho-high-energy` implies `SHELL-rho-compact`;
- `SHELL-sturm-liouville-completeness` implies `TARGET-shell-d3`; and
- `SHELL-spherical-shell-nontiling` implies `POLYA-program-target`.

The first three implication additions are the missing reverse metadata for
already present compact dependencies. The last two additions are reciprocal
to the two new dependencies. Thus every new or changed
dependency/implies relation is reciprocal, including the direct
Sturm--Liouville premise required for the `K=0` argument.

After the prospective delta:

- the complete dependency graph is acyclic;
- the complete implication graph is acyclic;
- every dependency, permitted dependency, implication, and blocker target
  names an existing obligation; and
- there is no dangling reference.

The dependency and permitted-dependency sets agree exactly for each of the
five promoted obligations. The geometry node has empty premise sets;
`SHELL-rho-compact` has its four direct analytic premises;
`SHELL-rho-uniformity` has its three disjoint ratio owners;
`TARGET-shell-d3` has the existing theorem premises plus the direct
Sturm--Liouville premise; and the program target has exactly strict counting,
the spectral theorem, and the geometry theorem.

## 5. Track separation and unchanged nodes

The geometric and spectral tracks meet only at `POLYA-program-target`:

```text
TARGET-shell-d3 --------------------> POLYA-program-target
SHELL-spherical-shell-nontiling ----> POLYA-program-target
```

The geometry node neither depends on nor implies `TARGET-shell-d3`, and the
spectral target neither depends on nor implies the geometry node.

`COMP-certified-bessel` is excluded from create and update operations. Its
canonical node-object SHA-256 before and after the in-memory application is

`a9b0b137820272d015daa50fe77753fc406ce69e382bc3551ddc1f2f96378b15`.

It remains byte-for-byte node-equal, `diagnostic_only`, with an empty
`implies` list and no dependency, permitted dependency, implication, or
blocker link to the compact theorem, uniformity theorem, spectral target,
program target, exact-D20 closure, or new geometry theorem. Its Round 8 and
Round 17 pilots likewise remain unchanged certified regression nodes.

All obligations in the `ellipse_parallel` and `certificate_family` tracks
are excluded from the update set and remain unchanged. In particular,
`SRC-mathieu-ellipse`, `ELLIPSE-near-circular`, and
`CERT-certificate-family` retain their prior states and play no role in the
shell theorem.

## 6. Roles, review artifacts, and premise discipline

The promoted theorem/bottleneck roles are distinct and complete:

| obligation | criticality | lead | clean room | adversarial |
| --- | --- | --- | --- | --- |
| geometry non-tiling | theorem | `A2` | `A3` | `A4` |
| compact middle | bottleneck | `A1` | `A3` | `A4` |
| all-ratio uniformity | bottleneck | `A1` | `A3` | `A4` |
| shell spectral target | theorem | `A1` | `A3` | `A2` |
| program target | theorem | `A1` | `A3` | `A4` |

Every row has `review_independence: clean_room`, at least one existing
clean-room artifact, at least one existing adversarial artifact, and
disjoint clean-room/adversarial artifact lists. The clean-room and fresh
adversarial reports independently reconstruct the exact theorem and geometry
claims. The assembly and cross-comparison artifacts keep the finite
certificate scopes separate from the analytic propagation.

The permitted-premise ledgers introduce no circularity. In particular:

- `SHELL-rho-compact` uses only the already proved phase, lattice,
  fixed-ratio high-energy, and complete analytic-envelope inputs;
- `SHELL-rho-uniformity` uses only the compact-middle and two endpoint
  theorems;
- `TARGET-shell-d3` uses the reviewed all-ratio theorem and direct positive
  spectrum input for `K=0`; and
- the geometry theorem uses no spectral premise.

## 7. Claim and convention audit

The patched statements preserve the exact class

$$
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R.
$$

The spectral target uses strict counting, includes every
`Lambda>=0`, treats `K=0` by positive spectrum rather than continuity,
retains the exact ratio owners

$$
(0,\rho_*],\qquad(\rho_*,7/8),\qquad[7/8,1),
$$

and preserves the exact finite/analytic boundary: 10,580 compact leaves on
their finite rectangle, 1,286 aggregate base boxes at `K=200`, analytic
tail propagation, and compact ownership of the shared `K=200` subtraction
face. It does not reconnect the legacy diagnostic computation.

The coefficient and scaling are correct:

$$
L_3=\frac1{6\pi^2},\qquad
L_3|A_{r,R}|=\frac{2}{9\pi}(R^3-r^3),
$$

and

$$
N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda).
$$

The geometry statement quantifies over every `0<r<R`, permits all rigid
motions, requires pairwise-disjoint interiors, rules out exact and
almost-everywhere coverage by open shells, and expressly covers the
corresponding closed-copy conventions after removal of the countable null
boundary union. The contained-ball separation, local finiteness,
countability, fixed-neighbor extraction, finite sphere-cover contradiction,
coincident-sphere cases, and scaling are sound.

The spectral and geometric domain classes are literally identical. The
program statement reads `new` only as newly completed in this internal
program. The judge and patch make no literature-novelty, priority, first
proof, or publication-readiness inference. The exploratory literature note
remains inconclusive evidence only.

## 8. Artifact-hash replay

The patch contains 23 `artifact_hashes` occurrences representing 16
distinct lifecycle files. Every occurrence reproduces. The evidence and
review fields contain 62 path occurrences over 17 unique files; every path
exists. The seventeenth file is the unhashed-by-patch exploratory literature
note, whose raw SHA-256 was also independently reproduced.

| artifact | reproduced SHA-256 | bytes | lines |
| --- | --- | ---: | ---: |
| theorem packet | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | 6,568 | 244 |
| theorem freeze | `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d` | 2,157 | 60 |
| theorem scope audit | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` | 8,228 | 205 |
| theorem incumbent | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` | 6,141 | 290 |
| theorem clean room | `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12` | 18,000 | 655 |
| theorem assembly audit | `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56` | 14,726 | 361 |
| theorem cross-comparison | `6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458` | 5,514 | 161 |
| theorem adversarial referee | `a69dc8a45f5a3b132bf7acc7e721e207ec4c61730e2bf4f85ff810a4a5f039d9` | 20,124 | 680 |
| geometry packet | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` | 4,703 | 105 |
| geometry freeze | `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a` | 992 | 30 |
| geometry scope audit | `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7` | 11,679 | 234 |
| geometry incumbent route | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` | 3,199 | 92 |
| geometry clean room | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` | 7,245 | 241 |
| geometry typography addendum | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` | 1,816 | 45 |
| geometry adversarial referee | `bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53` | 13,290 | **300** |
| program-scope audit | `d36b646136f6cfc9729c5f88e6a0051cadd591e9ba94f8fccefa86b503bf49e5` | 15,538 | 381 |
| exploratory literature note | `31a8bbb71c002daf77690591bd67114e943b3cb869484c517e35036042e52c23` | 2,620 | 50 |

All hashes in the judge and all `artifact_hashes` mappings are therefore
correct. The failure is not a hash mismatch: it is the false physical-line
metadata printed inside the correctly hashed program-scope audit.

## 9. First issue and required replacement

At line 80 of
`rounds/polya-main/round_022/reviews/program-target-scope-audit.md`, the
geometry lifecycle table states:

```text
... spherical-shell-nontiling-adversarial-referee.md ... | 13,290 | 299 |
```

For the exact file with SHA-256
`bfbed9e06f407e555c365524eef16a0d186e6745e2099dcbc4abb8af29499d53`,
independent byte inspection gives:

- 13,290 bytes;
- 300 `LF` bytes;
- zero `CR` bytes;
- a terminal `LF`;
- 300 decoded physical lines; and
- final numbered content at line 300.

Thus the scope audit's statement that the geometric lifecycle “reproduces
exactly” is false by one physical line. The SHA-256 and byte length in that
same row are correct, and every substantive conclusion of the scope audit
remains valid. Nevertheless, this project treats an authenticated positive
review artifact as a provenance claim as well as a mathematical claim, so
the false metadata prevents a clean PASS.

The minimal repair is:

1. replace `299` by `300` in the program-scope audit;
2. recompute that audit's SHA-256;
3. replace the old program-scope hash in all three judge occurrences: the
   narrative identity and the geometry/program `artifact_hashes` entries;
4. freeze the resulting judge bytes under a new SHA-256; and
5. run a replacement final State-Patch audit before application.

No statement, status, dependency, implication, blocker, role, evidence path,
or mathematical proof needs to change.

## Final determination

**Final verdict: FAIL — provenance metadata only. First issue:** the bound
program-scope audit reports 299 physical lines for the exact 300-line
spherical-shell non-tiling adversarial referee. All mathematics, graph
semantics, patch operations, hashes, roles, scopes, and no-novelty controls
otherwise pass.
