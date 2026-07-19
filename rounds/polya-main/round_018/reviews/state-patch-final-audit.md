# Round 18 State-Patch Final Audit

Date: 2026-07-14

Role: independent final State Patch auditor. I did not author
`rounds/polya-main/round_018/judge/judge-018.md`, and I did not mutate or
apply any change to `state/proof_obligations.yml`.

## Verdict

**PASS. First issue: none.**

The embedded Round 18 patch validates and applies cleanly in memory against
the required frozen graph. Its artifact provenance, source boundary,
dependency topology, exact residual subtraction, status calibration, and
one-time application behavior are consistent. The patch creates and promotes
only the qualified external source obligation `SRC-LORCH` and the internal
lemma `SHELL-next-angular-staircase`. It does not close the compact shell
obligation, the shell theorem, or the program theorem.

Required frozen hashes:

| artifact | required SHA-256 | observed SHA-256 | result |
|---|---|---|---|
| baseline `state/proof_obligations.yml` | `3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c` | `3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c` | PASS |
| `rounds/polya-main/round_018/judge/judge-018.md` | `73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61` | `73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61` | PASS |

## Evidence and artifact authentication

All 18 fixed-evidence rows in the judge matched their files byte for byte.
All 21 `artifact_hashes` entries in the two proposed obligations matched the
corresponding baseline or evidence artifact, including the spectral packet,
the accepted Round 17 claim, and the FLPS source card. The patch contains 50
evidence references, collapsing to 15 distinct Round 18 paths; every one is a
regular file. The clean-room and adversarial-review paths are present and
hash-correct.

The source boundary is adequate and deliberately narrow. The primary SIAM
publisher abstract for Lee Lorch's article identifies the first positive zero
`j_(nu,1)`, gives the scope `-1<nu<infinity`, and prints both strict squared
lower bounds used in the source card. NIST DLMF 10.47.3 supplies the
spherical-Bessel/ordinary-Bessel identity. Exact specialization yields only

$$
j_{5/2,1}>\frac{51}{10},\qquad
j_{7/2,1}>\frac{13}{2},\qquad
j_{9/2,1}>\frac{15}{2}.
$$

The source card and audit explicitly do not import a shell cross-product
claim, a higher-radial-mode exclusion, multiplicity counting, a Weyl payment,
or fixed-channel shell-to-ball monotonicity. The last comparison is proved
internally by zero extension in the same angular form domain and min--max.
Because the publisher exposes the complete statements and scope but the full
article proof is access-controlled, `proved_external_dependency` is justified
as a qualified statement-level dependency; it is not mislabeled as an
internal reconstruction.

No `last_updated_at` or `last_updated_round` field is hard-coded in the
patch, and no `TODO`, `TBD`, placeholder date, or timestamp token occurs.
Repository application will generate a real ISO timestamp and Round 18 index.

## Repository-tool simulation

The public validator command

~~~powershell
python -m math_collab.validate_round rounds/polya-main/round_018/judge/judge-018.md --round-index 18
~~~

returned `Round State Patch OK` against the frozen baseline. I then used the
same repository functions `extract_state_patch`, `parse_structured_text`,
`apply_state_patch`, and `validate_graph` entirely in memory, with round index
18 and the judge path. The authoritative graph remained at its baseline hash.

The simulated result was exactly:

- created: `SRC-LORCH`, `SHELL-next-angular-staircase`;
- updated: `CONV-strict-counting`,
  `SHELL-sturm-liouville-completeness`, `SHELL-first-angular-bands`,
  `SRC-FLPS-balls`, `SHELL-rho-compact-analytic-envelope`,
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
  `POLYA-program-target`, `COMP-certified-bessel`;
- rejected: none;
- no-change records: the 14 IDs printed in the judge patch.

The simulated graph has 53 unique obligation IDs. It passes `validate_graph`,
has no dangling `dependencies`, `implies`, or `blockers` references, and its
combined canonical dependency/implies digraph is acyclic. Every new edge has
the required reciprocal metadata exactly once:

~~~text
CONV-strict-counting --------------------+
SHELL-sturm-liouville-completeness ------+
SHELL-first-angular-bands ---------------+
SRC-LORCH -------------------------------+--> SHELL-next-angular-staircase
SRC-FLPS-balls --------------------------+          |
                                                     v
                              SHELL-rho-compact-analytic-envelope
~~~

`SHELL-rho-compact-analytic-envelope.dependencies` contains the new lemma
exactly once, and the new lemma implies that envelope exactly once. No list
duplicate is introduced in any touched dependency, implication, or permitted
dependency field.

With the exact Windows path behavior of `validate_round`, the judge reference
`rounds\polya-main\round_018\judge\judge-018.md` is appended once to the
`inconclusive` evidence bucket of each created obligation. Existing updates
receive only their explicit patch evidence, as prescribed by
`apply_state_patch`. Revalidating the same patch against the simulated
post-patch graph fails on both duplicate creates, so the patch is naturally
one-time: it cannot silently apply twice.

Seven IDs appear in both `update` and `no_change`. This overlap is
semantically harmless and operationally unambiguous. For each, `no_change`
describes an unchanged theorem or status, while `update` refreshes evidence,
reverse-edge metadata, the recorded residual statement, falsification cases,
or the next action. The tool applies the update and treats `no_change` as a
report-only record.

## Mathematical bookkeeping audit

The proposed new region is

$$
\mathcal C_{18}
=\left\{\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)\right\}.
$$

The proof gives `k_5<26`. On the active fixed-ratio branch,
`K_0>64`; on the seam branch, `54/(1-rho)^2>=1944`. Hence
`k_5<U` throughout the new ratio interval. Therefore every C18 point has
exactly the ratio and strict lower-wall conditions of the second D17
component and lies strictly below its old upper wall. Thus
`C18 subset D17` is exact, not a rectangular approximation.

Subtracting the half-open interval `(k_2,k_5]` from `(k_2,U)` gives
`(k_5,U)` and leaves the disjoint lower-ratio component unchanged. The
post-promotion residual is therefore exactly

$$
\begin{aligned}
\mathcal D_{18}
={}&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup\left\{\rho_c\leq\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}
$$

All four displayed frequency comparisons remain strict. The old owner keeps
`K=k_2`; the new lemma owns `K=k_5`; the old endpoint keeps `rho=7/8`; and
the old analytic owner keeps `K=U`. The two certified boxes B0 and B1 remain
valid but were already absorbed by C17, so they are not subtracted again.

The residual is demonstrably nonempty. At `rho=1/2`, the audited bounds give

~~~text
k_5(1/2) < 26 < 30 < 64 < K_0(1/2)=U(1/2),
~~~

so `(1/2,30)` lies in the second D18 component. This witness prevents any
accidental theorem closure. The recorded boundary
`k_5(rho_c)<2z_(rho_c)<k_6(rho_c)` also correctly stops the one-radial-mode
argument at `k_5`.

## Status audit

The only created promoted statuses are:

| ID | post-patch status | calibration |
|---|---|---|
| `SRC-LORCH` | `proved_external_dependency` | qualified statement-level source dependency |
| `SHELL-next-angular-staircase` | `proved_internal` | independently reconstructed analytic lemma |

There are no status deltas among the ten updated obligations. In particular:

- `SHELL-rho-compact-analytic-envelope` remains `proved_internal` while its
  exact cover advances from A17/D17 to A18/D18;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
  `POLYA-program-target` remain `open`;
- `COMP-certified-bessel` remains `diagnostic_only`;
- both endpoint obligations remain byte-unchanged at `proved_internal`;
- `COMP-certified-bessel-pilot-round8` and
  `COMP-certified-bessel-pilot-round17` remain byte-unchanged at `certified`;
- no Round 18 certified-computation obligation or certified subset is
  created.

## Reproduction results

Observed checks:

- angular-staircase ledger: **PASS**, 40 exact checks, first issue `null`;
- residual-mask self-check: **PASS**, 12 checks;
- complete repository suite: **132 passed, 10 subtests passed**;
- Round 18 bytecode compilation: **PASS**;
- `git diff --check`: **PASS**;
- post-patch in-memory graph validation: **PASS**.

## Application decision

The patch is safe to apply exactly once with `--round-index 18`, provided the
baseline graph, judge, and all fixed evidence hashes are rechecked immediately
before application. After application, Round 18 closes only the angular band
through the inclusive `k_5` face. The exact nonempty D18 remains the next
proof target; no compact, uniform, shell-theorem, or program-theorem closure
is authorized.
