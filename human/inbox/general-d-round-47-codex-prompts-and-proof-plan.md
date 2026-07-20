# General-dimensional spherical-shell Pólya project
## Independent review after Round 46 and Round 47 Codex reasoning prompt packet

**Date:** 20 July 2026  
**Repository:** `yutianlee/polya-ai-collab`  
**Reviewed branch:** `main`  
**Reviewed commit:** `62119aa918b86ddb4e96d03426f5db7685c381d1`  
**Suggested Round 47 branch:** `codex/general-d-round-47-d4-weighted-aggregate`  
**Current mathematical bottleneck:** general-dimensional spherical-shell extension  
**Completed theorem retained:** the three-dimensional spherical-shell theorem remains frozen as `proved_internal`

---

# 0. Independent review after Round 46

## 0.1 Source precedence and repository conflicts

Use the following precedence.

1. `state/proof_obligations.yml` for mathematical statuses and dependency ownership.
2. This human prompt packet for the Round 47 workflow decision only.
3. `human/inbox/general-d_simplified_analytic_strategy.md` for the binding methodology.
4. The finalized Round 46 lead, clean-room, adversarial, and independent-audit artifacts.
5. Earlier independently audited general-dimensional lemmas.
6. `manuscript/spherical-shell-polya-general-d.tex` only where consistent with the higher-precedence sources.

Two conflicts must be reported explicitly.

### Conflict A: stale round selection

At the reviewed commit, `state/proof_obligations.yml` still selects

```text
SHELL-general-d-high-floor-first-drop-CST
```

and its narrative rule still describes the older pointwise route. The finalized Round 46 audit instead mandates a switch to

```text
SHELL-general-d-weighted-aggregate
```

without changing any mathematical status. This packet is a human workflow revision that supersedes only the stale `round_selection` prose. It does **not** supersede any status field.

### Conflict B: stale manuscript status narrative

The current general-dimensional manuscript predates the completed first-floor no-drop integration and the Round 44--46 Gate-B work. It is a research log, not the authoritative status record. Do not edit it in Round 47.

No source conflict permits promotion of the all-dimensional theorem.

---

## 0.2 Review verdict

```text
INCOMPLETE
```

Round 46 made exact and useful progress, but it did not close the pointwise Gate-B owner and did not prove the general-dimensional theorem. It also did not falsify the exact Gate-B scalar or the underlying shifted-tail defect.

This is not a failure of the project. It is a clean stopping point for the exhausted pointwise architecture.

---

## 0.3 Progress that should be retained

The following modules are mathematically substantive and should remain frozen.

### A. Completed three-dimensional theorem

The sharp Dirichlet Pólya inequality for every genuine three-dimensional spherical shell remains `proved_internal`. It is separate from the general-dimensional extension.

### B. Exact general-dimensional backbone

Retain the real-order phase proxy, exact harmonic branching, signed primitive, and master identity

\[
W_d-P_d^{<}
=
\mathcal B_d(A)
+
\sum_{m\ge0}c_{d,m}D_A(r_m),
\]

where

\[
r_m=m+\frac{d-2}{2},
\qquad
c_{d,m}=\binom{m+d-3}{d-3},
\qquad
\mathcal B_d(A)\ge0.
\]

The backbone remains `derived_under_assumptions` until its dedicated frozen audit is completed.

### C. Pointwise shifted-tail modules

Retain, in their exact scopes:

- the dimension-dependent strict no-mode owner;
- outer convex tails;
- the turning-zone zero-tail owner;
- the complete one-interface theorem;
- the first-shelf identities and curvature reserve;
- the first-floor first-drop theorem;
- the high-floor no-drop theorem;
- the completed first-floor no-drop theorem;
- the analytically closed remainder-rich and lower-\(Q\) high-floor sectors;
- every exact wall, parity, and activity assignment already audited.

### D. Round 44--46 Gate-B reductions

Round 46 validly proved:

1. the unique outer-wall normalization
   \[
   q(\tan\phi-\phi)=\pi\left(B_0+\frac34\right),
   \qquad
   K=q\sec\phi=(q+1)\sec t;
   \]
2. the closed inner-cap formula;
3. the exact derivative of the full Round-45 margin along a fixed owner wall;
4. several one-signed wall components;
5. the strict inverse-action quotient theorem
   \[
   \frac{A(x)-A(q)}{U_x-U_q}
   >
   \frac{(\phi-a)\tan a}{\pi};
   \]
6. the strict sufficient reduction
   \[
   \mathcal M_{45.18}>F_{\mathrm{strong}};
   \]
7. a complete loss ledger and equality-face audit.

The finite searches found no negative exact Gate-B owner, but they remain diagnostic.

---

## 0.4 What is still missing at Gate B

There are two distinct gaps. They must not be conflated.

### Local implication gap

For the one-sided upper-\(\alpha\), outer-\(B\) endpoint treated in Rounds 44--46, the first unrepaired implication is

\[
\boxed{
F_{\mathrm{strong}}\ge0
\quad\text{on every complete exact owner}.
}
\]

Here

\[
\begin{aligned}
F_{\mathrm{strong}}={}&
\frac{p(U_r-U_x)(\phi-a)\tan a}{\pi}\\
&+
\frac{q(\tan\phi-\phi)(\pi-2\phi)}
     {2\pi\phi}
+\frac{d_\rho m}{2}
-\frac p2
+\frac{41}{40}.
\end{aligned}
\]

This is only a sufficient reduction. It is not equivalent to the literal Round-45 margin \(\mathcal M_{45.18}\), and neither is equivalent to the exact unprojected shifted-tail scalar \(\mathscr S\).

The broader relaxed domain contains negative values of \(F_{\mathrm{strong}}\). Therefore an analytic proof cannot sign this formula from the outer wall and elementary radial geometry alone. It must use the exact common-shelf, first-drop, hard-\(E\), activity, and parity correlations that were discarded in the reduction.

### Theorem-level cover gap

Even a proof of the displayed Gate-B owner would not, by itself, prove high-floor CST. A separate exact cover audit would still have to own:

- the remaining higher \(Q_N\) faces;
- equal-count generic inverse faces;
- exceptional \(\alpha=0\) simultaneous \(B/Q\) corners;
- general lower-shelf and \(\alpha\)-endpoint closures;
- both parity grids;
- the complete moderate-frequency active window;
- every strict equality face.

Thus Gate B was a local endpoint gate, not the final all-dimensional theorem.

---

## 0.5 Contingent analytic plan for reopening Gate B

This is a mathematically plausible salvage plan. It is **not** the recommended Round 47 target, because the Round 46 hard rule has already stopped further pointwise rounds.

### GB1. Return to the full margin

Do not try to prove \(F_{\mathrm{strong}}\ge0\) as a free-standing inequality. Restore

\[
\mathcal M=
pR_1\mathcal D+\mathcal O+
B_0\zeta+\frac9{16\beta}-J+
\mathcal T+\mathcal C
-\frac{p-d_\rho m}{2},
\]

with

\[
\mathcal D=A(x)-A(q),
\]

and retain \(\mathcal O,\mathcal T,\mathcal C\). The negative relaxed examples show that these omitted positive payments, or their correlation with the shelf data, are load-bearing.

### GB2. Prove one integrated action-curvature theorem

Group

\[
\mathcal P(p):=pR_1\mathcal D+\mathcal C.
\]

Round 46 derived the exact second derivative as an integral. The first missing kernel estimate was

\[
C_b\left(
\frac{p\mu^2}{U_r^3}-\frac{2r}{U_r}
\right)
\le
\frac{pbQ_b}{2(b^2-r^2)^{7/2}},
\qquad
\mu\le b\le K,
\]

or a signed integrated replacement.

The target should be the weakest statement sufficient to produce an explicit tangent lower bound for \(\mathcal P\) on the complete owner. Pointwise kernel positivity is stronger than necessary; an integrated inequality is acceptable.

### GB3. Use the exact shelf image, not a chamber family

From the common shelf, literal first drop, and hard-\(E\) condition, derive one intrinsic feasible-set theorem for \(p\) at fixed \((q,m,B_0)\). The theorem must retain

\[
A(r)+\frac14=f+e_0,
\qquad
A(x)+\frac14=f+e_p,
\qquad
0\le e_p\le e_0,
\]

\[
E=e_0+e_p<E_*=\frac{p-d_\rho m}{2p},
\]

and the first-drop wall at \(x+1\).

The required conclusion is not a list of floors. It is a continuous inequality showing that the same wall-hugging condition that makes the shelf payment small forces either:

- a lower tangent for \(\mathcal P\);
- extra old-level payment \(\mathcal O\);
- extra top payment \(\mathcal T\); or
- a direct lower bound for the phase/root reserve.

### GB4. Reduce to one intrinsic boundary or stationary scalar

After GB2--GB3, prove that the complete margin has no negative interior minimum. A valid conclusion would be:

- monotonicity from the least feasible \(p\);
- convexity plus a signed derivative at the least feasible \(p\);
- a unique stationary point with a directly positive value; or
- transport to an already owned exact face.

Convexity alone is insufficient because a convex function may attain its minimum in the interior.

### GB5. Close the smallest intrinsic face

The expected residual is \(p=3\), \(m=1\), \(B_0=1\), or an exact hard-\(E\) boundary. Use the wall equation and the closed formula for \(J\) to reduce this to one printed elementary inequality in \((q,\phi)\). No ratio ladder, count ladder, or certificate family is allowed.

### GB6. Perform a separate cover audit

Only after the local owner is closed may a new audit determine whether the remaining high-floor face classes are already inherited, reducible to the same theorem, or still open.

### Gate-B stop criterion

If GB2 or GB3 produces another unsigned scalar, do not start another pointwise round. Preserve the exact reduction and continue with the weighted aggregate.

---

## 0.6 Recommended strategy revision

The recommended strategy is to accept the Round 46 hard stop and activate the exact weighted aggregate.

The next primary target is

\[
\boxed{
\mathcal B_d(A)+\sum_{m\ge0}c_{d,m}D_A(r_m)\ge0,
}
\]

starting with \(d=4\).

Reasons:

1. It is exactly sufficient for the spectral proxy.
2. It can retain the branching bonus discarded by the pointwise route.
3. It can use already proved pointwise modules to localize possible negative tails.
4. It avoids the unresolved count-, inverse-, and endpoint-owner proliferation.
5. Round 46 supplies useful localization and lower-bound information even though it did not close the pointwise scalar.
6. The \(d=4\) branching primitive has an explicit cell formula and a positive \(K^2\)-scale bonus.

No mathematical status should change merely because the workflow changes.

---

# 1. Round 47 proof plan: exact weighted aggregate in \(d=4\)

## 1.1 Exact target

For \(d=4\),

\[
r_m=m+1,\qquad c_{4,m}=m+1.
\]

Write \(a=m+1\). Round 47 targets

\[
\boxed{
\mathrm{WT}_4:\quad
\mathcal B_4(A)+\sum_{a\ge1}aD_A(a)\ge0
}
\]

on the strict active region

\[
K^2>
\frac{\pi^2}{(1-\rho)^2}+\frac34.
\]

The equality-inclusive complement remains owned by the existing no-mode theorem.

Define

\[
q_a:=\left[A(a)+\frac14\right]_<.
\]

The direct \(d=4\) proxy is

\[
P_4^{<}=\sum_{a\ge1}a^2q_a,
\qquad
W_4=\int_0^K z^2A(z)\,dz.
\]

The master identity gives

\[
W_4-P_4^{<}
=
\mathcal B_4(A)+\sum_{a\ge1}aD_A(a).
\]

A negative value of \(\mathrm{WT}_4\) would falsify this sufficient proxy route, not the spectral Pólya theorem itself.

---

## 1.2 Required exact launch lemmas

### Lemma L1: the \(d=4\) primitive

For \(0\le z<1\),

\[
\Delta_4(z)=-\frac{z^3}{6}.
\]

For integer \(a\ge1\) and \(z=a+x\), \(0\le x<1\),

\[
\boxed{
\Delta_4(a+x)
=
-\frac a6+\frac{ax(1-x)}2-\frac{x^3}{6}.
}
\]

Prove directly that

\[
-\Delta_4(a+x)\ge
\frac{a(a+1)}
{12\{a+\frac12+\sqrt{a(a+1)}\}}
>
\frac a{24}.
\]

Do not replace the exact cell polynomial by \(a/24\) until a loss ledger shows the loss is harmless.

### Lemma L2: exact and coarse bonus forms

Define the cell bonus

\[
\mathcal B_{4,a}(A)
=
2\int_a^{a+1}
(-A'(z))(-\Delta_4(z))\,dz,
\]

with zero extension and the final interval truncated at \(K\).

Then

\[
\mathcal B_4(A)=\sum_{a\ge0}\mathcal B_{4,a}(A).
\]

The coarse consequence is

\[
\boxed{
\mathcal B_4(A)
\ge
\frac1{12}\sum_{1\le j<K}A(j).
}
\]

Audit the face \(K\in\mathbb N\): \(A(K)=0\), and the sum is strictly \(j<K\).

### Lemma L3: exact adjacent-shift recurrence

For every integer \(a\ge1\), define

\[
L_a
:=
2\int_a^{a+1}A(z)\,dz-q_a-q_{a+1}.
\]

Prove the exact identity

\[
\boxed{
D_A(a)-D_A(a+1)=L_a.
}
\]

This identity must use the strict bracket literally. No ordinary floor may be substituted.

### Lemma L4: exact weighted summation by parts

Because \(D_A(a)=0\) for all sufficiently large \(a\),

\[
\boxed{
\sum_{a\ge1}aD_A(a)
=
\sum_{a\ge1}\frac{a(a+1)}2L_a.
}
\]

Therefore

\[
\boxed{
\mathrm{WT}_4
=
\mathcal B_4(A)
+
\sum_{a\ge1}\frac{a(a+1)}2L_a.
}
\]

This is the preferred coordinate system for the aggregate proof.

### Lemma L5: negative-support localization

Define

\[
\mathcal N_4(A)
=
\{a\in\mathbb N:\ a<K,\ D_A(a)<0\}.
\]

Using only already proved pointwise modules in their exact scopes, prove that every \(a\in\mathcal N_4(A)\) lies in the unresolved active high-floor first-drop sector. Explicitly exclude:

- no-mode shifts;
- outer and turning tails;
- one-interface tails;
- first-floor first drops;
- all no-drop tails;
- the completed first-floor no-drop sector;
- every already closed high-floor sub-sector.

The result must be an intrinsic support theorem, not a ratio or floor ladder.

---

## 1.3 Preferred aggregate closure: maximal negative components

Partition \(\mathcal N_4(A)\) into maximal consecutive components

\[
C=[u,v]\cap\mathbb N.
\]

Use L3 to express every \(D_A(a)\) in a component through the local defects \(L_j\) and the nonnegative boundary values \(D_A(u-1)\), \(D_A(v+1)\), when present.

For each component, derive an exact charge identity of the form

\[
\sum_{a\in C}aD_A(a)
=
\sum_{j\in I_C}\omega_{C,j}L_j
+\text{nonnegative boundary terms},
\]

with printed nonnegative weights \(\omega_{C,j}\).

Then prove one component theorem:

\[
\boxed{
\sum_{a\in C}aD_A(a)
+
\sum_{j\in J_C}\mathcal B_{4,j}(A)
+
\sum_{b\in P_C}bD_A(b)
\ge0,
}
\]

where:

- \(J_C\) is an intrinsically defined set of bonus cells;
- \(P_C\) contains retained positive neighboring tails, if needed;
- different components receive disjoint bonus cells and disjoint positive-tail charges;
- every charge is counted exactly once.

The theorem may use maximal ordinary-floor shelves inside the component, but it may not create a theorem family indexed by the floor value, \(B\), \(Q\), a shell-ratio interval, or a certificate chamber.

The expected mechanism is:

- a negative local trapezoidal remainder forces wall hugging;
- wall hugging forces a controlled action drop across the same cells;
- the exact polynomial \(-\Delta_4\) converts that action drop into branching bonus;
- neighboring positive shifted tails provide any residual boundary charge.

---

## 1.4 Fallback aggregate closure: localized deficit function

If the component theorem does not close, derive

\[
D_A(a)\ge-\Xi_a
\qquad(a\in\mathcal N_4(A)),
\]

where \(\Xi_a\) is built from the same action drops that occur in \(\mathcal B_4(A)\).

The minimum acceptable result is a proved inequality

\[
\sum_{a\in\mathcal N_4(A)}a\Xi_a
\le
\mathcal B_4(A)
+
\sum_{a\notin\mathcal N_4(A)}aD_A(a).
\]

A stronger sufficient route is

\[
\sum_{a\in\mathcal N_4(A)}a\Xi_a
\le
\mathcal B_4(A),
\]

but it must not be described as equivalent.

The first coarse candidate

\[
\sum_{a\in\mathcal N_4(A)}a\Xi_a
\le
\frac1{12}\sum_{1\le j<K}A(j)
\]

may be tested, but only after \(\Xi_a\) and its support are rigorously derived.

---

## 1.5 Moderate frequency, thin shells, and walls

A complete proof must explicitly handle:

- the strict active wall
  \[
  K^2=\frac{\pi^2}{(1-\rho)^2}+\frac34;
  \]
- \(K\in\mathbb N\);
- \(\mu=\rho K\in\mathbb N\);
- action walls \(A(a)+1/4\in\mathbb N\);
- the inner interface \(a=\mu\);
- the endpoint \(a=K\);
- \(\rho\uparrow1\);
- moderate \(K\) immediately above activity;
- all zero-extended terminal cells.

Do not infer the moderate-frequency case from an asymptotic argument.

---

## 1.6 Round 47 success, partial-success, and stop criteria

### Success

A complete analytic proof of \(\mathrm{WT}_4\) on the entire strict active domain, including all equality faces and the moderate-frequency window.

### Substantive partial success

Any of the following, with a precise residual:

1. L1--L5 plus a finite list of intrinsic negative-component types;
2. an exact component-charge identity reducing \(\mathrm{WT}_4\) to one correlated scalar;
3. a proved localized \(\Xi_a\) with a rigorous weighted support theorem;
4. a directed counterexample to a proposed component or bonus-only sufficient inequality while the literal \(\mathrm{WT}_4\) remains positive.

No status promotion follows from partial success.

### Stop

Stop the round if:

- a directed negative value of literal \(\mathrm{WT}_4\) is found;
- the proposed aggregate reduction requires a ratio ladder, floor/count ladder, chamber family, or second compact certificate;
- the lead obtains only another unsigned projection after the exact local identities are exhausted.

A negative sufficient bound is not a negative \(\mathrm{WT}_4\), and a negative \(\mathrm{WT}_4\) is not a counterexample to the spectral theorem.

---

# 2. Prompt A — lead analytic proof of \(\mathrm{WT}_4\)

## Role

Act as the lead reasoning agent. Prove the exact \(d=4\) weighted aggregate or produce a mathematically decisive partial result under the stop rules above.

## Mandatory preflight

Before any derivation, verify:

```text
repository: yutianlee/polya-ai-collab
base branch: main
required base commit: 62119aa918b86ddb4e96d03426f5db7685c381d1
Round 46 audit commit: a72bc4565d6a29a723545e0a5d38c8e8b1cfb79c
current status:
  SHELL-general-d-high-floor-first-drop-CST : open
  SHELL-general-d-branching-backbone        : derived_under_assumptions
  SHELL-general-d-weighted-aggregate        : proposed
  SHELL-general-d-pointwise-assembly        : open
  TARGET-shell-general-d                    : proposed
```

Verify the content hash of `state/proof_obligations.yml`. Report the stale `round_selection` conflict. This human packet authorizes the weighted-aggregate workflow only; it does not authorize a status change.

## Mandatory sources

Read at minimum:

```text
state/proof_obligations.yml
human/inbox/general-d_simplified_analytic_strategy.md
human/current_directives.md
state/current_state.md
state/gap_register.md
state/lemma_bank.md

manuscript/spherical-shell-polya-general-d.tex

human/outbox/general-d-round-46-r45-18-complete-owner.md
human/outbox/general-d-round-46-clean-room-r45-18.md
human/outbox/general-d-round-46-adversarial-r45-18-search.md
human/outbox/general-d-round-46-independent-audit.md

human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md
human/outbox/general-d-round-10-fractional-terminal-reserve-independent-audit.md
human/outbox/general-d-first-floor-no-drop-wp2-integration-audit.md
human/outbox/general-d-round-36-exact-count-gap-collision-reduction.md
human/outbox/general-d-round-36-independent-audit.md
human/outbox/general-d-round-37-gap-interface-synchronization-and-root-free-gate.md
human/outbox/general-d-round-37-independent-audit.md
```

Also read the exact files cited by the proof-obligation entries for:

```text
SHELL-general-d-easy-tails
SHELL-general-d-one-interface-tail
SHELL-general-d-shelf-identities
SHELL-general-d-first-floor-first-drop
SHELL-general-d-high-floor-no-drop
SHELL-general-d-first-floor-no-drop
SHELL-general-d-no-mode
```

Do not use the stale manuscript abstract as a status source.

## Exact target

Prove

\[
\mathcal B_4(A)+\sum_{a\ge1}aD_A(a)\ge0
\]

on

\[
K^2>
\frac{\pi^2}{(1-\rho)^2}+\frac34.
\]

## Required order of work

### A1. Freeze notation and derive L1--L4

Print all definitions and prove:

\[
\Delta_4(a+x)
=
-\frac a6+\frac{ax(1-x)}2-\frac{x^3}{6},
\]

\[
\mathcal B_4(A)
\ge
\frac1{12}\sum_{1\le j<K}A(j),
\]

\[
D_A(a)-D_A(a+1)
=
2\int_a^{a+1}A-q_a-q_{a+1},
\]

\[
\sum_{a\ge1}aD_A(a)
=
\sum_{a\ge1}\frac{a(a+1)}2
\left(
2\int_a^{a+1}A-q_a-q_{a+1}
\right).
\]

Audit strict walls before proceeding.

### A2. Prove the support theorem L5

Use the proved modules to localize every possible negative \(D_A(a)\). Produce an exact cover table. Do not merely cite that “all other cases were handled.”

### A3. Work with maximal negative components

Derive an exact component charge formula. Test the formula symbolically and numerically before attempting a global sign.

### A4. Prove the component charge or localized-deficit theorem

Use the exact cell polynomial \(-\Delta_4\) as long as possible. Keep action drops, floor remainders, and bonus cells correlated.

### A5. Close moderate frequency and thin shells

No asymptotic-only conclusion is accepted.

### A6. Produce the ledgers

The report must contain:

1. dependency ledger;
2. exact loss ledger;
3. no-double-counting charge ledger;
4. strict-wall and equality-face ledger;
5. falsification table;
6. final status statement;
7. list of files modified.

## Forbidden approaches

Do not:

- resume the pointwise \(F_{\mathrm{strong}}\) campaign;
- introduce a ratio ladder;
- introduce a floor, count, \(B\), \(Q\), or chamber-indexed theorem family;
- use a new compact certificate;
- independently worst-case action, cap, floor, and bonus quantities without a printed loss;
- call a sufficient comparison equivalent;
- use a finite positive sweep as proof;
- edit the manuscript, state file, proof graph, or completed three-dimensional proof.

## Required output files

Create only:

```text
human/outbox/general-d-round-47-d4-weighted-aggregate.md
computations/general_d_round47_d4_weighted_diagnostic.py
```

An optional exact symbolic replay may be added as:

```text
computations/general_d_round47_d4_weighted_replay.wl
```

---

# 3. Prompt B — clean-room analytic reconstruction

## Independence boundary

Before the freeze, do not read:

```text
human/outbox/general-d-round-47-d4-weighted-aggregate.md
computations/general_d_round47_d4_weighted_diagnostic.py
computations/general_d_round47_d4_weighted_replay.wl
human/outbox/general-d-round-47-adversarial-d4-weighted-search.md
```

Read only the mandatory authoritative sources and earlier audited artifacts.

## Role

Independently reconstruct the \(d=4\) aggregate from the direct proxy

\[
W_4-P_4^{<}
=
\int_0^K z^2A(z)\,dz
-
\sum_{a\ge1}a^2
\left[A(a)+\frac14\right]_<.
\]

## Required clean-room tasks

1. Derive the \(d=4\) primitive and bonus without copying the lead notation.
2. Independently derive
   \[
   D_A(a)-D_A(a+1)=L_a
   \]
   and the weighted summation identity.
3. Determine whether a direct layer-cake or weighted trapezoidal proof is cleaner than the negative-support route.
4. Derive an independent maximal-block or maximal-negative-component formulation.
5. Attempt one exact component inequality.
6. Audit all strict walls.
7. Record the first unrepaired inequality if the proof does not close.
8. Freeze the clean-room derivation before reading Prompt A.
9. After the freeze, compare with Prompt A line by line and report:
   - exact agreements;
   - hidden assumptions;
   - lost correlations;
   - any stronger clean-room lemma;
   - any contradiction.

## Required output

```text
human/outbox/general-d-round-47-clean-room-d4-weighted.md
```

The report must clearly separate pre-comparison and post-comparison sections and record a hash of the frozen pre-comparison prefix.

---

# 4. Prompt C — independent adversarial search

## Independence boundary

Do not import the Prompt-A evaluator. Build the literal \(d=4\) formulas independently from the master identity or direct proxy.

## Role

Falsify the literal target and every proposed sufficient lemma. Computation is diagnostic except for directed certification of named points.

## Literal quantities

Evaluate independently:

\[
q_a=\left[A(a)+\frac14\right]_<,
\]

\[
P_4^{<}=\sum_{a\ge1}a^2q_a,
\qquad
W_4=\int_0^Kz^2A(z)\,dz,
\]

\[
\mathrm{WT}_4=W_4-P_4^{<},
\]

and separately

\[
\mathcal B_4(A)+\sum_{a\ge1}aD_A(a).
\]

The two evaluations must agree to the directed enclosure.

## Mandatory stress classes

Search:

1. \(K\) immediately above the no-mode wall;
2. \(\rho\uparrow1\);
3. small \(\rho\);
4. integer and near-integer \(K\);
5. integer and near-integer \(\mu=\rho K\);
6. action walls \(A(a)+1/4\in\mathbb N\);
7. inner-interface cells \(a\approx\mu\);
8. the smallest active integer shift \(a=1\);
9. high-floor first-drop records inherited from Rounds 36--46;
10. large \(a\), large \(K\), and large terminal count;
11. maximal consecutive components of sampled negative \(D_A(a)\), if any;
12. the exact d=4 bonus bound near its cell minimum.

## Classification

Use exactly these classes.

### A. Literal aggregate route counterexample

\[
\mathrm{WT}_4<0.
\]

Certify with rational parameter brackets, strict-wall ownership, and directed Arb arithmetic. This falsifies \(\mathrm{WT}_4\), not the spectral theorem.

### B. Sufficient-route counterexample

A proposed component, block, bonus-only, or \(\Xi_a\) inequality is negative while

\[
\mathrm{WT}_4\ge0.
\]

This rejects only that sufficient route.

### C. Candidate exact theorem witness

A named positive point is diagnostic only. It cannot establish global coverage.

## Directed certification requirements

For every named negative or near-zero record:

- use rational brackets for \(\rho\) and \(K\);
- certify every strict floor;
- certify the no-mode side;
- certify the \(a=\mu\) and \(a=K\) ownership;
- evaluate with Arb or rational interval arithmetic;
- print the complete payment ledger;
- rerun at higher precision;
- distinguish literal \(\mathrm{WT}_4\) from every surrogate.

## Required output files

```text
human/outbox/general-d-round-47-adversarial-d4-weighted-search.md
computations/general_d_round47_independent_d4_weighted_search.py
```

A positive finite sweep must end with

```text
positive_coverage_certificate: FALSE
```

---

# 5. Prompt D — final independent audit and Round 48 decision

## Role

After Prompts A--C are frozen, perform an adversarial mathematical audit.

## Required determinations

Use one verdict:

```text
PASS
PASS WITH MINOR REPAIRS
STRUCTURAL PASS — FINAL SIGN OPEN
COMPUTER-ASSISTED CANDIDATE ONLY
INCOMPLETE
FAIL
FALSIFIED
```

Answer all of the following.

1. What exact theorem or reduction was proved?
2. Is literal \(\mathrm{WT}_4\) proved on the complete active domain?
3. Is the no-mode equality face assigned correctly?
4. Is the \(d=4\) branching specialization exact?
5. Are L1--L4 correct at integer action walls?
6. Is negative support localized using only proved modules?
7. Are all bonus cells and positive-tail charges counted once?
8. Is any sufficient inequality misreported as equivalent?
9. Are computations diagnostic or certified?
10. What is the first unrepaired logical gap?
11. Which proof-obligation statuses should change?
12. What is the next single obligation?

## Status discipline

- A complete \(d=4\) proof does not prove the all-\(d\) weighted aggregate.
- The existing general `SHELL-general-d-weighted-aggregate` obligation must not be promoted solely from \(d=4\).
- If a complete \(d=4\) theorem is proved, propose a new scoped obligation:
  ```text
  SHELL-general-d-weighted-aggregate-d4
  ```
  with an appropriate status and exact dependencies.
- Do not promote `TARGET-shell-general-d` until the backbone and all dimensions are independently closed.
- If literal \(\mathrm{WT}_4\) is falsified, record the negative route evidence but do not demote the spectral theorem target.
- Workflow and `next_action` prose may change without changing mathematical statuses.

## Round 48 decision

If \(\mathrm{WT}_4\) is proved, recommend one sharply defined next obligation:

- extend the aggregate inequality from \(d=4\) to all \(d\ge5\); or
- first freeze and independently promote the branching backbone, if that is the remaining dependency gate.

If the proof is partial, select only the first unrepaired aggregate inequality. Do not return to pointwise Gate B without a new human directive.

## Required output

```text
human/outbox/general-d-round-47-independent-audit.md
```

The audit may propose an RFC-6902 state patch, but it must not edit the state file.

---

# 6. Expected Round 47 file set

```text
human/outbox/general-d-round-47-d4-weighted-aggregate.md
human/outbox/general-d-round-47-clean-room-d4-weighted.md
human/outbox/general-d-round-47-adversarial-d4-weighted-search.md
human/outbox/general-d-round-47-independent-audit.md

computations/general_d_round47_d4_weighted_diagnostic.py
computations/general_d_round47_independent_d4_weighted_search.py
computations/general_d_round47_d4_weighted_replay.wl   # optional
```

No manuscript, state, proof-graph, or completed three-dimensional file is to be modified in this reasoning round.
