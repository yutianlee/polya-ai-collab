# Round 21 Lemma State Patch Audit

Date: 2026-07-15

## Verdict

**FAIL. First discrepancy: the promoted lemma states an overbroad and false
guard.** In the created `SHELL-exact-d20-closure.statement_tex`, the patch
writes

> `k_11(rho)>12 for rho>=rho_c`

without the necessary upper-domain condition \(\rho<1\). The same guard is
displayed without its domain in the judge's decision prose. The proved
statement is

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1),
\]

and the application to the residual uses only the still smaller range
\(\rho_c\leq\rho<39/50\).

The unrestricted version is not a harmless shorthand. At \(\rho=1\),
\(z_\rho=\pi/(1-\rho)\) is undefined. At \(\rho=2\),

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144,
\]

so \(k_{11}(2)<12\). Thus the graph would contain a literally false
`proved_internal` statement if this patch were applied as written.

This is the sole defect found. The exact D20 subtraction itself is unaffected
because D20 has \(\rho<39/50\), and every structural, hash, certificate-scope,
role, chronology, status, and dependency check otherwise passes. The patch
must nevertheless receive replacement bytes before application; an auditor
must not silently narrow a promoted statement while applying it.

## Audited bytes and authentication

The audited judge file
`rounds/polya-main/round_021/judge/judge-021-lemma.md` has 38,222 bytes and
reproduces the required SHA-256:

`a3418d8a711d46c0ca4531f0ff9837c802626318ee9a22b98a0722caafecf40f`.

The embedded State Patch is valid JSON, was extracted from the final
`## State Patch` fence, and parsed as one mapping. I authenticated all 47 raw
file hashes in the three created obligations' `artifact_hashes` maps; every
one matches. The remaining compact `canonical_certificate` value

`96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`

is a canonical certificate-content digest rather than a raw file hash. It
matches the compact contract, certificate report, hardened wrapper constant,
and frozen 256-bit replay. All 90 evidence, clean-room, adversarial-review,
and certification path references in the create/update operations exist.

In particular, the current residual, candidate, two contracts, A3
review/addendum, hardened A4 wrapper/tests/report, replacement
cross-comparison, corrected fresh referee, replacement provenance audit,
residual classifier/tests, incumbent synthesis, and every preserved negative
review digest reproduce exactly. No stale hash is relabelled as a current
positive artifact.

The declared runtime also matches the available environment: Python 3.14.4
and python-flint 0.8.0.

## In-memory validation and application

The repository validator reported:

```text
Graph OK: state/proof_obligations.yml
Patch OK
```

I then applied the parsed patch to a deep in-memory copy with
`round_index=21` and the declared judge reference. The original graph, patch
against the original graph, and resulting graph each returned no validation
issues. No state, judge, or code file was modified.

The exact `PatchResult` is:

- created: `CERT-round21-compact-proxy`,
  `CERT-round21-aggregate-tail`, `SHELL-exact-d20-closure`;
- updated: `CONV-strict-counting`,
  `SHELL-sturm-liouville-completeness`, `SHELL-phase-enclosures`,
  `SHELL-weighted-lattice-fractional`,
  `SHELL-low-interface-fixed-rho-high-energy`, `SRC-annuli`,
  `SHELL-combined-closure`, `SHELL-rho-compact-analytic-envelope`,
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
  `POLYA-program-target`, and `COMP-certified-bessel`;
- rejected: none; and
- no-change bookkeeping: `SHELL-rho-zero-endpoint`,
  `SHELL-rho-one-endpoint`, `SHELL-fixed-rho-high-energy`,
  `SHELL-combined-closure`, both certified-Bessel pilots,
  `COMP-certified-bessel`, `SHELL-rho-compact`,
  `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target`.

An id appearing in both `update` and `no_change` is not contradictory here:
the update changes metadata, evidence, edges, or next action, while the
no-change entry records that the relevant theorem/status decision remains
unchanged.

## Expected application delta

The proof-obligation count would change from 57 to 60. The only status
entries absent from the old graph are the three new nodes:

| created obligation | resulting status |
|---|---|
| `CERT-round21-compact-proxy` | `certified` |
| `CERT-round21-aggregate-tail` | `certified` |
| `SHELL-exact-d20-closure` | `proved_internal` |

No existing status changes. In particular,
`SHELL-rho-compact-analytic-envelope` was already `proved_internal`;
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` remain `open`; and `COMP-certified-bessel` remains
`diagnostic_only`.

The exact aggregate list-edge counts would be:

| field | before | after | net |
|---|---:|---:|---:|
| `dependencies` | 201 | 219 | +18 |
| `permitted_dependencies` | 131 | 150 | +19 |
| `implies` | 109 | 128 | +19 |
| `blockers` | 11 | 8 | -3 |

Those totals decompose as follows:

- the three new nodes contribute 19 dependencies, 19 permitted
  dependencies, and three forward `implies` edges;
- the existing analytic envelope gains the exact-D20 lemma as one dependency
  and one permitted dependency;
- seven existing foundations gain the declared reverse `implies` metadata
  for the new certificates/lemma, contributing 17 edges;
- `SHELL-rho-compact` loses its direct dependency and blocker on
  `COMP-certified-bessel`;
- `TARGET-shell-d3` loses that dependency, permitted dependency, and blocker;
- `POLYA-program-target` loses that blocker; and
- `COMP-certified-bessel` loses its obsolete `implies` edge to
  `TARGET-shell-d3`.

The requested permitted-dependency removal from `SHELL-rho-compact` is a
safe no-op because that list did not contain the diagnostic computation.
No undeclared edge is removed.

Application would also add the declared positive evidence and falsification
cases, refresh next actions, set Round 21/timestamp metadata on the three
created and 13 updated nodes, and add the judge reference to the new nodes'
inconclusive evidence as required by the application mechanism. It does not
alter `round_selection`, reject a claim, or mutate either Bessel pilot.

## Dependency direction, statuses, and cycles

All dependencies of the three new obligations already have acceptable
statuses in the current graph:

- `CONV-strict-counting`, completeness, phase enclosures, the weighted
  lattice lemma, the low-interface lemma, and `SHELL-combined-closure` are
  `proved_internal`;
- `SRC-annuli` is a `proved_external_dependency`; and
- the two new certificate nodes are `certified` before serving as
  dependencies of the new mathematical lemma in the resulting graph.

For every new direct dependency \(X\to Y\), the patched graph contains the
matching reverse `Y.implies -> X` metadata. The certificates imply the new
lemma, and the lemma depends on them. The new lemma implies
`SHELL-rho-compact-analytic-envelope`, and that envelope gains the new lemma
as a dependency. The existing envelope continues to imply
`SHELL-rho-compact`, which continues through `SHELL-rho-uniformity` to the
theorem target. No missing direct or reverse edge affects reachability.

The current and in-memory patched dependency graphs both have no directed
cycle. Their separate `implies` graphs also have no directed cycle. Before
and after the patch there are no dangling `dependencies`, `implies`,
`blockers`, or `permitted_dependencies` references. Detaching the legacy
diagnostic computation creates neither an orphaned proof premise nor a cycle.

## Certified-computation obligations

Both new CERT nodes meet every mandatory certified-computation field:

- type `computation`, status `certified`, track `certified_computation`;
- `evidence_class: interval_certified`;
- software version, reproduction command, coverage statement, and artifact
  hash map;
- nonempty `certification_artifacts`;
- positive, negative, and inconclusive evidence buckets;
- dependencies and matching `permitted_dependencies`;
- falsification cases and next action; and
- explicit independent-review metadata.

Their scopes are honest and do not claim the mathematical bridges:

1. `CERT-round21-compact-proxy` owns exactly the finite leaf, strict-wall,
   interface, corner, and tiling predicates on the closed rectangle
   \([7/51,39/50]\times[12,200]\), with 10,580 exact leaves. Its statement
   explicitly assigns the spectral transfer to the separately proved
   analytic bridge and certifies no point outside the rectangle.
2. `CERT-round21-aggregate-tail` owns exactly 1,286 outward ratio boxes on
   \([7/51,39/50]\) at the single base frequency \(K=200\). It certifies
   \(\mathcal B(\rho,200)>0\),
   \(\mathcal B_K(\rho,200)>0\), \(F(\rho)>0\), base guards, and consistency
   predicates. Its statement, coverage, falsification cases, and next action
   all forbid a finite-box claim at \(K>200\).

The mathematical `SHELL-exact-d20-closure` node—not either CERT node—owns
the compact spectral bridge, the strict
\(\mathcal B\Rightarrow\mathcal Q\Rightarrow N_D<W\) implication, the
universal derivative inequalities, and both integrations from \(K=200\).
This finite-versus-universal separation is exact.

## Mathematical closure and face ownership

Subject only to correcting the written guard domain, the lemma's set
bookkeeping is exact. The authenticated residual is

\[
\mathcal D_{20}={\rho_c\leq\rho<39/50,\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

On this domain, \(7/51<\rho_c\) and the correctly qualified
\(k_{11}(\rho)>12\) put every point with \(K\leq200\) in the compact theorem
domain, while every point with \(K>200\) is in the aggregate theorem domain.
Thus

\[
\mathcal D_{20}
=\bigl(\mathcal D_{20}\cap\{K\leq200\}\bigr)
\mathbin{\dot\cup}
\bigl(\mathcal D_{20}\cap\{K>200\}\bigr).
\]

Both theorems cover \(K=200\), but the patch assigns that subtraction face
only to the compact owner. If \(U<200\), all residual points are compact; if
\(U=200\), strict \(K<U\) excludes the shared frequency; and if \(U>200\),
the exact split above applies. The faces \(\rho=39/50\), \(K=k_{11}\), and
\(K=U=K_0\) remain outside D20 and are not subtracted twice. Hence D21 is
empty as exact residual bookkeeping.

The false unrestricted guard does not invalidate this narrower argument, but
it does invalidate the promoted statement as written.

## Roles and evidence chronology

The bottleneck lemma has distinct roles: lead author `A2`, clean-room
reviewer `A3`, and adversarial reviewer `fresh-hardened-referee`, with
`review_independence: clean_room`. Its promoted status has both clean-room and
adversarial-review artifacts. The two standard certificate nodes have A4 as
their computation lead and a distinct independent cross-checker as
adversarial reviewer. The existing bottleneck envelope retains its separate
A1/A3/A4 roles. No role collision is introduced.

Positive evidence points only to the repaired/current cycles. The initial
candidate ambiguity, initial aggregate-route failure, implicit-branch A4
failure, lifecycle-incomplete cross-comparison, superseded first referee,
first-referee miss, and failed first provenance transcription remain in
negative evidence where applicable. Existing dependency statuses are all
sufficient, and no failed artifact supplies a promoted premise.

## Higher targets and legacy computation

The patch is genuinely lemma-only apart from the two scoped computation
certifications:

- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain open;
- theorem assembly, endpoint seams, \(K=0\), normalization, scaling,
  theorem-level clean-room review, final referee, and program-scope audit
  remain explicit next actions; and
- no shell theorem or program target is promoted merely because D21 is
  empty.

`COMP-certified-bessel` remains `diagnostic_only`. Its B0 and B1 children
remain certified, analytically redundant regression boxes. After the patch,
no higher obligation has the legacy parent as a dependency, permitted
dependency, blocker, or implied target. The legacy parent's own foundation
dependencies and the pilots' reverse edges remain intact. The patch detaches
the obsolete theorem linkage exactly as declared; it neither broadens nor
relabels the Bessel computation.

## Required replacement

Do not apply SHA-256 `a3418d8a...`. Produce replacement judge bytes that:

1. change the lemma statement to
   `k_11(rho)>12 for rho_c<=rho<1` (or to the narrower residual ratio domain);
2. qualify the displayed guard in the decision prose the same way;
3. leave every other create/update/no-change operation unchanged; and
4. rerun patch validation and a fresh independent State Patch audit against
   the replacement hash.

No analytic proof, certificate, residual, review artifact, dependency edge,
status decision, or legacy-computation detachment otherwise needs repair.

**Final verdict: FAIL. First issue: false unrestricted
`k_11(rho)>12 for rho>=rho_c` guard.**
