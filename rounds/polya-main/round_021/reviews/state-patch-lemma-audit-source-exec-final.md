# Round 21 Final Source-Execution State Patch Audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

The final judge at
`rounds/polya-main/round_021/judge/judge-021-lemma.md` reproduces SHA-256

`a620175fc43591cd80fcc9f50165d7b21596b077d92fbc4450167d21a4eca9aa`.

Its embedded State Patch passes both repository validators and a fresh
in-memory application from the current 57-obligation graph. Every current
raw artifact hash, evidence path, certificate digest, dependency direction,
status decision, face assignment, source-execution role, and chronology gate
passes. The patch creates only the two scoped certificates and exact-D20
lemma; it promotes no higher obligation.

This audit does not apply the patch or modify the graph. It authorizes only
the authenticated judge bytes above, subject to the remaining application
gate recorded in that judge.

## Judge and State Patch parsing

The judge has 45,241 bytes. Its final `## State Patch` fence extracts as one
valid JSON mapping. The operation counts are exactly:

- create: 3;
- update: 13;
- reject: 0; and
- no-change bookkeeping: 11.

The create ids are:

1. `CERT-round21-compact-proxy`;
2. `CERT-round21-aggregate-tail`; and
3. `SHELL-exact-d20-closure`.

The update ids are exactly `CONV-strict-counting`,
`SHELL-sturm-liouville-completeness`, `SHELL-phase-enclosures`,
`SHELL-weighted-lattice-fractional`,
`SHELL-low-interface-fixed-rho-high-energy`, `SRC-annuli`,
`SHELL-combined-closure`, `SHELL-rho-compact-analytic-envelope`,
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
`POLYA-program-target`, and `COMP-certified-bessel`.

An id appearing in both `update` and `no_change` is not contradictory: the
update changes declared evidence, metadata, edges, or next action, while the
no-change entry records that its theorem/status decision remains unchanged.

## Validators and in-memory application

Both validator commands passed:

```text
python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml
Graph OK

python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/polya-main/round_021/judge/judge-021-lemma.md
Patch OK
```

I then applied the parsed patch to a deep in-memory copy with
`round_index=21` and the declared judge reference. Validation returned no
issues for the original graph, the patch against that graph, or the patched
graph. The exact `PatchResult` was:

- nodes: 57 before, 60 after;
- created: the three ids listed above;
- updated: the 13 ids listed above;
- rejected: none; and
- no-change: all 11 declared entries.

No state, judge, computation, test, or evidence file was changed by this
application check.

## Status and edge delta

The only statuses absent from the old graph are the three created nodes:

| created obligation | resulting status |
| --- | --- |
| `CERT-round21-compact-proxy` | `certified` |
| `CERT-round21-aggregate-tail` | `certified` |
| `SHELL-exact-d20-closure` | `proved_internal` |

No existing status changes. In particular:

- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain `open`;
- `COMP-certified-bessel` remains `diagnostic_only`; and
- its Round 8 and Round 17 pilot nodes remain `certified` regression boxes.

The exact aggregate list-edge delta is:

| field | before | after | net |
| --- | ---: | ---: | ---: |
| `dependencies` | 201 | 219 | +18 |
| `permitted_dependencies` | 131 | 150 | +19 |
| `implies` | 109 | 128 | +19 |
| `blockers` | 11 | 8 | -3 |

This is the intended decomposition:

- the three new nodes contribute 19 dependencies, 19 permitted
  dependencies, and three forward implications;
- the analytic envelope gains the exact-D20 lemma as one dependency and one
  permitted dependency;
- seven existing foundations gain 17 reverse implications;
- `SHELL-rho-compact` loses its diagnostic-parent dependency and blocker;
- `TARGET-shell-d3` loses that dependency, permitted dependency, and
  blocker;
- `POLYA-program-target` loses that blocker; and
- `COMP-certified-bessel` loses its obsolete implication to
  `TARGET-shell-d3`.

The attempted permitted-dependency removal from `SHELL-rho-compact` remains
a safe no-op because that list did not contain the diagnostic parent. No
undeclared edge is removed.

## Graph invariants and reciprocity

Before and after the in-memory application:

- the dependency graph has no directed cycle;
- the separate implication graph has no directed cycle;
- no dependency, permitted dependency, implication, or blocker reference
  dangles; and
- every new dependency has its matching reverse implication metadata.

The compact and aggregate certificates both imply
`SHELL-exact-d20-closure`, which depends on both. The exact-D20 lemma implies
`SHELL-rho-compact-analytic-envelope`, which gains that lemma as a
dependency. All direct and reverse edges through compact uniformity and the
theorem target remain consistent.

Every dependency of a new node already has an accepted status:
foundational obligations are `proved_internal`, `SRC-annuli` is a
`proved_external_dependency`, and the two computation dependencies are the
newly `certified` nodes.

After application, none of `SHELL-rho-compact`, `TARGET-shell-d3`, or
`POLYA-program-target` contains `COMP-certified-bessel` as a dependency,
permitted dependency, blocker, or implication. The diagnostic parent no
longer implies the theorem target. Its own foundational dependencies and
the pilots' reverse diagnostic edges remain intact, so the patch detaches
the obsolete theorem linkage without orphaning, broadening, or promoting the
legacy computation.

## Exact comparison with the prior intended patch

I parsed the previous corrected judge at commit `48a02bc` and compared its
State Patch with the final patch by operation id and structural field.

- create, update, reject, and no-change id sequences are identical;
- every type, track, status, dependency, permitted dependency, implication,
  blocker, and added/removed edge is identical;
- all three created mathematical statements are byte-for-byte identical;
- no updated mathematical statement changes; and
- the in-memory graph-semantic delta is therefore exactly unchanged.

The differences are confined to current evidence paths and hashes,
adversarial/certification/clean-room artifact lists, reproduction wording,
new source-execution and upper-wall falsification cases, promotion reasons,
and the round-assessment explanation. These are the required provenance
repairs, not a new mathematical or graph claim.

## Hash authentication and evidence existence

Across the three create operations there are 63 `artifact_hashes`
occurrences:

- 62 raw-file hash occurrences, representing 41 distinct raw files; and
- one compact canonical certificate-content digest.

All 62 raw occurrences reproduce their declared SHA-256 values. There are
42 distinct declared digest values overall. The current positive cycle is
authenticated exactly as:

- scoped candidate: `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d`;
- wrapper: `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`;
- tests: `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99`;
- final A4 report: `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5`;
- source-execution cross-comparison:
  `7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a`;
- fresh referee: `d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28`;
  and
- final provenance/isolation audit:
  `f4670818af3a57a965f0032edd72ea875d4ad618f9cc4a5b1b78cabdc7e481da`.

The compact canonical digest

`96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`

was independently regenerated by a direct producer replay with 10,580
leaves and 2,153,076 floor comparisons. It also agrees with the current
contract, compact report, final wrapper, and final A4 report.

The patch contains 127 evidence/artifact-path occurrences over 43 unique
paths, with zero missing:

| category | occurrences | unique paths |
| --- | ---: | ---: |
| positive evidence | 68 | 27 |
| negative evidence | 34 | 16 |
| inconclusive evidence | 1 | 1 |
| clean-room artifacts | 3 | 3 |
| adversarial-review artifacts | 11 | 5 |
| certification artifacts | 10 | 8 |

The positive-path union is disjoint from the negative and inconclusive
unions. No rejected candidate, stale wrapper/test pair, superseded A4
report, prior cross-comparison/referee/provenance cycle, stale judge, or
stale State Patch audit occurs as current positive evidence.

## Evidence roles and restricted predecessor use

The computation roles remain separated: A4 is lead for both certificate
nodes, while `independent-cross-checker` is the distinct adversarial role.
The bottleneck lemma retains A2 as lead, A3 as clean-room reviewer, and
`fresh-hardened-referee` as the distinct adversarial reviewer, with
`review_independence: clean_room`. The current fresh referee wrote its own
authenticated report, and the final provenance audit authenticates that
authorship and independence.

Two predecessor files remain usable only through explicit current scope
overlays; neither is stale current-cycle authority:

1. The original A3 clean-room reconstruction is listed together with its
   domain addendum. The addendum explicitly rejects the unrestricted guard
   sentence and retains the earlier Q/B, spectral-bridge, derivative, and
   D20 reconstruction only on the corrected ratio domain. The judge's
   reason for promotion cites the A3 proof **and** domain addendum as one
   corrected chain.
2. The original compact adversarial audit remains positive only for the
   unchanged finite compact-certificate bytes. The final cross-comparison
   explicitly limits that use, while the scoped candidate, final A4 report,
   fresh referee, and provenance audit reject the old unrestricted guard.

Thus neither file supplies an unqualified current guard or source-execution
claim. All genuinely superseded candidate, A4, cross, referee, and loader
cycles occur only as negative chronology. The old unscoped A4 report is also
the single inconclusive item attached to the legacy diagnostic computation;
that use does not promote or certify it.

The chronology preserves the initial candidate ambiguity, aggregate-route
failure, Machin-branch and lifecycle failures, missed referee defect,
incorrect provenance transcription, false unrestricted guard, stale-hash
judge/audit, and cache-vulnerable source-loader cycle. No failed artifact is
used as a promoted premise.

## Certified-computation scope and reproduction warning

Both new certificate nodes retain every mandatory certified-computation
field: computation type, certified status, certified-computation track,
`interval_certified` evidence class, software version, reproduction command,
coverage statement, artifact hashes, certification artifacts, all evidence
buckets, dependencies, matching permitted dependencies, falsification cases,
next action, and independent-review metadata.

Their scopes remain exact:

- the compact node owns only the 10,580 finite leaves and associated strict
  wall, interface, corner, and tiling predicates on
  `[7/51,39/50] x [12,200]`;
- the aggregate node owns only the 1,286 outward boxes and base predicates
  on `[7/51,39/50]` at the single frequency `K=200`; and
- `SHELL-exact-d20-closure`, not either certificate, owns both spectral
  bridges and the universal derivative, curvature, and two-integration
  propagation for every `K>=200`.

The reproduction warning is correct and material. Plain
`python -B -m computations.round21_verify_exact_d20_closure` is not accepted
as a proof gate because `-B` forbids ordinary cache writes but does not
forbid bytecode reads. The judge instead requires the authenticated stdin
wrapper bootstrap and isolated fresh-cache pytest bootstraps recorded in the
final A4 report. The live wrapper executes the source payload whose bytes it
authenticates; the malicious timestamp-cache and module-state regressions
cover the former lifecycle defect.

## Exact D20 closure and face ownership

The accepted residual is

\[
\mathcal D_{20}=\{\rho_c\leq\rho<39/50,\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

The corrected lower-frequency guard is stated exactly as

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).
\]

On that domain, positive denominators give

\[
z_\rho\geq\frac{\pi}{1-\rho_c}=\pi+\frac12>\frac72,
\qquad k_{11}(\rho)^2>\frac{577}{4}>144.
\]

The upper wall is indispensable: `rho=1` is singular, and the exact
`rho=2` counterexample gives `k_11(2)<12`. Every D20 point satisfies
`rho<39/50<1`, so the corrected guard applies to the complete residual
without broadening it.

The exact subtraction is

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

The owners are disjoint and exhaustive. Both theorem domains cover
`K=200`, but compact is its unique subtraction owner. The cases `U<200`,
`U=200`, and `U>200` are all handled. The included face `rho=rho_c` remains
subject to the strict frequency inequalities; `rho=39/50`, `K=k_11(rho)`,
and `K=U(rho)` remain outside D20. Hence there is no omitted or doubly
subtracted face, and exact bookkeeping gives `D21` empty.

## Higher obligations and application boundary

Empty D21 is a lemma conclusion, not an automatic theorem promotion.
The compact assembly, all-ratio uniformity, shell theorem, and program
target remain open. The patch still requires coherent theorem assembly,
endpoint seams, `K=0`, normalization, scaling, theorem-level clean-room
review, a fresh theorem referee, non-tiling work, and a program-scope audit
before any higher status may change.

The judge explicitly does not apply its patch. Application must use these
exact judge bytes and occur once with `--round-index 21` and the declared
judge reference only after its authenticated wrapper, isolated-test, and
remaining application gates pass.

## Final determination

The final State Patch has the same mathematical and graph-semantic delta as
the prior intended patch, but replaces its stale evidence chain with the
scoped candidate and authenticated source-execution lifecycle. All hashes,
paths, graph invariants, statuses, roles, chronology, faces, and nonpromotion
conditions pass.

**Final verdict: PASS. First issue: none.**
