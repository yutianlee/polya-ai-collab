# Round 21 Lemma State Patch Audit — Replacement

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

The corrected `rounds/polya-main/round_021/judge/judge-021-lemma.md`
passes strict replacement-byte, syntax, in-memory application, graph,
certificate-scope, evidence, role, chronology, face-ownership, and
non-promotion checks. The former unrestricted guard has been repaired at
both sites, and no unrelated byte-level or semantic patch change was made.

This audit authorizes the corrected State Patch at SHA-256

`5c59fdb95ec0b24f604448d323031e8182366ff00fc6b3a005741d69abf02fd4`

subject to the judge's remaining application-gate commands. It does not
itself apply the patch or modify the proof-obligation graph.

## Replacement-byte isolation

The corrected judge has 38,246 bytes and reproduces the required SHA-256
above. I compared it directly with the initial committed judge at
`c57312cdb79a5bad9bd0fe266b9e465e6be0303f`. The complete Git diff contains
exactly two textual edits:

1. the decision prose now displays
   `k_11(rho)>12 (rho_c<=rho<1)`; and
2. the created `SHELL-exact-d20-closure.statement_tex` now says
   `k_11(rho)>12 for rho_c<=rho<1`.

The second edit is the only change inside the embedded JSON. No create,
update, reject, or no-change operation was added or removed. No id, status,
edge, scope, role, evidence path, artifact hash, reason, next action, score,
or application instruction changed.

The initial judge's raw SHA-256 was
`a3418d8a711d46c0ca4531f0ff9837c802626318ee9a22b98a0722caafecf40f`.
That superseded byte sequence remains correctly rejected by
`state-patch-lemma-audit.md`; this report audits only the replacement bytes.

## Guard correction

The replacement fixes the first and sole discrepancy in the initial audit.
With

\[
\rho_c=\frac{1}{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_{11}(\rho)=\sqrt{z_\rho^2+132},
\]

the expression is undefined at \(\rho=1\), and the unrestricted assertion
for every \(\rho\geq\rho_c\) is false. For example, at \(\rho=2\),

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

On the corrected domain \(\rho_c\leq\rho<1\), however,

\[
z_\rho\geq z_{\rho_c}=\pi+\frac12>\frac72,
\qquad
k_{11}(\rho)^2>\frac{49}{4}+132=\frac{577}{4}>144,
\]

so \(k_{11}(\rho)>12\) follows strictly. The residual D20 uses the narrower
range \(\rho_c\leq\rho<39/50<1\), so the repaired guard is sufficient for
the exact compact/aggregate split and introduces no new scope claim.

## Validator and in-memory application results

Both repository validator invocations passed:

```text
python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml
Graph OK

python -B -m math_collab.validate_state_patch --graph state/proof_obligations.yml --patch rounds/polya-main/round_021/judge/judge-021-lemma.md
Patch OK
```

I also extracted the final `## State Patch` JSON, parsed it as one mapping,
and applied it to a deep in-memory copy of the current graph with
`round_index=21` and the declared judge reference. Validation returned no
issues for the original graph, the patch against that graph, or the patched
graph. The exact result is:

- obligations: 57 before, 60 after;
- created: `CERT-round21-compact-proxy`,
  `CERT-round21-aggregate-tail`, and `SHELL-exact-d20-closure`;
- updated: `CONV-strict-counting`,
  `SHELL-sturm-liouville-completeness`, `SHELL-phase-enclosures`,
  `SHELL-weighted-lattice-fractional`,
  `SHELL-low-interface-fixed-rho-high-energy`, `SRC-annuli`,
  `SHELL-combined-closure`, `SHELL-rho-compact-analytic-envelope`,
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
  `POLYA-program-target`, and `COMP-certified-bessel`;
- rejected: none; and
- no-change bookkeeping: 11 entries, exactly those declared in the patch.

An obligation appearing in both `update` and `no_change` receives only the
declared metadata or edge refresh; its theorem/status decision remains
unchanged.

## Exact state delta and graph invariants

The only new statuses are those of the three created obligations:

| obligation | status |
|---|---|
| `CERT-round21-compact-proxy` | `certified` |
| `CERT-round21-aggregate-tail` | `certified` |
| `SHELL-exact-d20-closure` | `proved_internal` |

No existing status changes. In particular,
`SHELL-rho-compact-analytic-envelope` was already `proved_internal`;
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` remain `open`; and `COMP-certified-bessel` remains
`diagnostic_only`.

The exact aggregate list-edge delta is:

| field | before | after | net |
|---|---:|---:|---:|
| `dependencies` | 201 | 219 | +18 |
| `permitted_dependencies` | 131 | 150 | +19 |
| `implies` | 109 | 128 | +19 |
| `blockers` | 11 | 8 | -3 |

This decomposes exactly as declared:

- the three new nodes contribute 19 dependencies, 19 permitted
  dependencies, and three forward `implies` edges;
- the analytic envelope gains the exact-D20 lemma as one dependency and one
  permitted dependency;
- seven existing foundations gain 17 reverse `implies` edges;
- `SHELL-rho-compact` loses the diagnostic parent's dependency and blocker;
- `TARGET-shell-d3` loses that dependency, permitted dependency, and blocker;
- `POLYA-program-target` loses that blocker; and
- `COMP-certified-bessel` loses its obsolete implication to the theorem
  target.

The requested permitted-dependency removal from `SHELL-rho-compact` is a
safe no-op because the diagnostic parent was not present in that list. No
undeclared edge is removed.

Before and after application:

- the dependency graph is acyclic;
- the separate `implies` graph is acyclic;
- no dependency, permitted dependency, implication, or blocker dangles; and
- every new dependency has its matching reverse implication metadata.

The two certificates imply the exact-D20 lemma, which depends on both. The
lemma implies the analytic envelope, which gains the lemma as a dependency.
All remaining direct/reverse reachability toward compact uniformity and the
theorem target is intact. Every dependency of a new node is already
`proved_internal`, `proved_external_dependency`, or one of the two newly
`certified` certificate obligations.

## Certificate scope, dependencies, and evidence

Both new certificate nodes retain all mandatory certified-computation
fields: type `computation`, status `certified`, track
`certified_computation`, `interval_certified` evidence class, software
version, reproduction command, coverage statement, artifact hashes,
certification artifacts, all evidence buckets, dependencies, matching
permitted dependencies, falsification cases, next action, and independent
review metadata.

Their scopes remain exact:

- `CERT-round21-compact-proxy` certifies 10,580 finite leaves and their
  strict-wall, interface, corner, and tiling predicates only on
  \([7/51,39/50]\times[12,200]\). The analytic spectral bridge remains
  separate.
- `CERT-round21-aggregate-tail` certifies 1,286 outward ratio boxes only on
  \([7/51,39/50]\) at the single base frequency \(K=200\): the declared
  \(\mathcal B\), \(\mathcal B_K\), \(F\), guard, and consistency
  predicates. It makes no finite-box claim for \(K>200\).
- `SHELL-exact-d20-closure`, not either certificate, owns the spectral
  bridge, the \(\mathcal B\Rightarrow\mathcal Q\Rightarrow N_D<W\)
  implication, the universal derivative inequalities, and the two
  integrations from \(K=200\).

The replacement did not alter any artifact hash or evidence path. All 47
raw-file entries in the created nodes' 48-entry artifact-hash maps reproduce
their declared SHA-256 values. The remaining compact
`canonical_certificate` digest,

`96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`,

is a canonical certificate-content digest and agrees across the contract,
report, hardened wrapper, and frozen 256-bit replay. All 90 positive,
negative, inconclusive, clean-room, adversarial-review, and certification
path references exist. The declared runtime also matches the environment:
Python 3.14.4 and python-flint 0.8.0.

Positive evidence uses the repaired/current artifacts. The initial ambiguous
candidate isolation, initial aggregate-route failure, implicit-branch A4
failure, lifecycle-incomplete cross-comparison, superseded first referee,
first-referee lifecycle miss, and failed first provenance transcription
remain negative evidence. No failed or superseded artifact is used as a
promoted premise.

## Roles, faces, and ownership

Role separation remains valid:

- the bottleneck lemma has A2 as lead, A3 as clean-room reviewer, and
  `fresh-hardened-referee` as adversarial reviewer, with `clean_room`
  independence;
- both certificates have A4 as computation lead and a distinct
  `independent-cross-checker`; and
- the existing analytic envelope retains its separate A1/A3/A4 roles.

The exact residual and ownership remain

\[
\mathcal D_{20}=\{\rho_c\leq\rho<39/50,\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

The corrected guards place its \(K\leq200\) part in the compact theorem and
its \(K>200\) part in the aggregate theorem. Both theorem domains cover
\(K=200\), but only the compact subtraction owner owns that face. The three
orderings \(U<200\), \(U=200\), and \(U>200\) are all handled; strict
\(K<U\) resolves the middle case. The faces \(\rho=39/50\),
\(K=k_{11}(\rho)\), and \(K=U\) remain outside D20. There is no omission or
double subtraction, and the exact successor D21 is empty.

## Higher targets and legacy diagnostic detachment

No higher target is promoted. The compact assembly, all-ratio uniformity,
shell theorem, and program target remain open. The patch still requires
coherent theorem assembly, endpoint seams, \(K=0\), normalization, scaling,
theorem-level clean-room review, a fresh final referee, non-tiling work, and
a program-scope audit before any higher promotion.

`COMP-certified-bessel` remains `diagnostic_only`, and its B0/B1 pilot nodes
remain unchanged certified regression boxes. After the in-memory patch, no
higher obligation depends on, permits, is blocked by, or is an implied target
of this legacy parent. Its own foundation dependencies and the pilots'
reverse diagnostic edges remain intact. The patch therefore detaches the
obsolete theorem linkage without broadening, relabelling, or promoting the
legacy computation.

## Final determination

The replacement is precisely the requested two-site guard qualification.
It repairs the undefined/false unrestricted claim, preserves every other
authenticated operation and graph invariant, and leaves all higher targets
at their prior status.

**Final verdict: PASS. First issue: none.**
