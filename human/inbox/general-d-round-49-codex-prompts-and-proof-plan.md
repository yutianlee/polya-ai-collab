# General-dimensional spherical-shell Pólya project
## Independent Round 48 review, analytic proof plan, and Round 49 Codex reasoning packet

**Date:** 21 July 2026  
**Repository:** `yutianlee/polya-ai-collab`  
**Reviewed branch:** `main`  
**Reviewed commit:** `828799fad8b1bb7965570d708bc842844a674de1`  
**Round 48 content commit:** `ddf92b23fbb313b25a6814467e9cab19faca6617`  
**Suggested Round 49 branch:** `codex/general-d-round-49-interface-to-top-suffix`  
**Selected scoped obligation:** `SHELL-general-d-weighted-aggregate-d4`  
**Authoritative status:** `proposed`

The completed three-dimensional spherical-shell theorem remains frozen as
`proved_internal`. The general-dimensional shell theorem remains unproved. The
all-dimensional weighted aggregate remains a separate `proposed` obligation. No
result in this packet changes a mathematical status.

---

# 0. Source precedence and repository gate

Use the following precedence.

1. `state/proof_obligations.yml`.
2. This human Round 49 packet for workflow selection only.
3. `human/inbox/general-d_simplified_analytic_strategy.md`.
4. `human/inbox/general-d-next-discovery-portfolio.md`.
5. The finalized Round 48 lead, certification, adversarial, and independent-audit artifacts.
6. The finalized Round 47 aggregate reduction and independent audit.
7. Earlier audited lemma packets and exact calculations.
8. The general-dimensional manuscript only where consistent with all higher-precedence sources.

Before mathematical work, verify:

```text
repository: yutianlee/polya-ai-collab
branch: main
required main commit: 828799fad8b1bb7965570d708bc842844a674de1
Round 48 content commit: ddf92b23fbb313b25a6814467e9cab19faca6617
selected obligation:
  SHELL-general-d-weighted-aggregate-d4 : proposed
retained statuses:
  SHELL-general-d-d4-full-outer-action-cell-round48 : proved_internal
  SHELL-general-d-d4-deep-inner-action-cell-round48 : proved_internal
  SHELL-general-d-weighted-aggregate : proposed
  SHELL-general-d-branching-backbone : derived_under_assumptions
  TARGET-shell-general-d : proposed
  TARGET-shell-d3 : proved_internal
```

Record the blob hash and SHA-256 of `state/proof_obligations.yml` at preflight.

## 0.1 Repository narrative conflicts

The authoritative proof graph has been updated to select
`SHELL-general-d-weighted-aggregate-d4`. Some narrative headers still report the
older pointwise high-floor CST selection and the old graph hash, notably the
opening paragraphs of:

```text
state/current_state.md
state/gap_register.md
state/next_round_prompts.md
```

Their later Round 48 sections contain the correct residual. This is a repository
synchronization defect, not a mathematical contradiction. Do not use the stale
headers as a status source and do not repair them in the Round 49 reasoning branch
unless a separate maintenance instruction is issued.

## 0.2 Gate terminology

The pointwise Gate-B campaign was stopped by the Round 46 hard rule after another
unsigned sufficient reduction. The live workflow is now the exact weighted-aggregate
fallback required by the binding strategy. Thus “Gate B remains open” should be read
as: the general-dimensional analytic closure has not passed its final sign gate. Do
not reopen the Round 45--46 pointwise owner unless a later human directive explicitly
does so.

---

# 1. Independent review of Round 48

## 1.1 Verdict

```text
STRUCTURAL PASS — FINAL SIGN OPEN
```

The final Round 48 repository tree passes its independent scope and integrity audit.
Mathematically, Round 48 is incomplete but substantive: it certifies two infinite
cell families analytically and reduces the direct inverse-layer route to a sharply
localized residual.

## 1.2 Exact target

With zero extension, put

\[
G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi},
\qquad
A(z)=G_K(z)-G_\mu(z),
\qquad
\mu=\rho K.
\]

For integers \(a\ge1\), use the strict bracket

\[
q_a=\left[A(a)+\frac14\right]_<,
\qquad
[x]_<:=\max\{0,\lceil x\rceil-1\}.
\]

The literal scoped target is

\[
\boxed{
\mathrm{WT}_4
=
\frac{K^4-\mu^4}{64}
-
\sum_{1\le a<K}a^2q_a
\ge0
}
\]

on

\[
0<\rho<1,
\qquad
K^2>\frac{\pi^2}{(1-\rho)^2}+\frac34.
\]

The equality-inclusive complement remains assigned to the strict no-mode theorem.

## 1.3 Exact inverse-layer ledger

Let

\[
H=A(0)=\frac{K-\mu}{\pi},
\]

let \(\xi:[0,H]\to[0,K]\) be the decreasing inverse of \(A\), and define

\[
F(t)=\frac{\xi(t)^3}{3},
\qquad
t_n=n-\frac14,
\qquad
N_n=\left\lceil \xi(t_n)\right\rceil-1.
\]

Then

\[
\boxed{
W_4=\int_0^H F(t)\,dt,
\qquad
P_4^<=\sum_{t_n<H}S_2(N_n),
}
\]

where

\[
S_2(N)=\frac{N(N+1)(2N+1)}6.
\]

For a complete height cell,

\[
\boxed{
L_n=\int_{n-1}^{n}F(t)\,dt-S_2(N_n).
}
\]

This is exact at every action wall. Cellwise positivity of all \(L_n\), including
the terminal truncation, is sufficient for \(\mathrm{WT}_4\), but is not known to
be necessary.

## 1.4 New proved modules

### Full-outer complete cells

Put

\[
\tau=A(\mu)=G_K(\mu).
\]

Every complete cell satisfying \(n\le\tau\) lies wholly in the outer branch and has

\[
\boxed{
L_n>
\frac{19N_n}{48}+\frac{27}{128}>0.
}
\]

The lead proof uses the exact kernel

\[
J(t)=-F'(t)=\frac{\xi(t)^2}{-A'(\xi(t))}
\]

and a correlated past/future comparison. The independent clean-room proof uses a
convex quantile transport. Both retain literal ceiling arithmetic, including
integer inverse radii.

### Complete deep-inner cells

Put

\[
t_*=A\!\left(\frac{\mu}{\sqrt2}\right).
\]

Every complete cell satisfying

\[
n-1\ge t_*
\]

lies in \(z\le\mu/\sqrt2\) and has

\[
\boxed{L_n>0.}
\]

The lead proof establishes

\[
F''(t)
=
\frac{z\{2\sigma(z)-z\sigma'(z)\}}{\sigma(z)^3}
\ge0,
\qquad
\sigma=-A',
\]

in that region. The clean-room proof independently derives the same convexity from

\[
\phi(u)=2\arcsin u-\frac{u}{\sqrt{1-u^2}},
\qquad
\phi'(u)=\frac{1-2u^2}{(1-u^2)^{3/2}}.
\]

These two obligations are correctly recorded as `proved_internal`. Neither
implies global QCL or \(\mathrm{WT}_4\).

## 1.5 Exact rejected route

The continuous replacement

\[
p\!\left(\xi(n-\tfrac14)\right)
\le
\int_{n-1}^{n}\frac{\xi(t)^3}{3}\,dt,
\qquad
p(x)=\frac{x(x+1)(2x+1)}6,
\]

is false. A directed interval calculation at an exact rational
interface-straddling cell gives a continuous margin below \(-572.69\), while the
literal discrete QCL margin at the same point is above \(956715\).

This rejects only the continuous quarter-node strengthening. It does not reject:

- the discrete QCL cell;
- the suffix/block route below;
- the literal \(\mathrm{WT}_4\);
- the spectral theorem.

The false continuous inequality is now a permanent regression case and may not be
reintroduced in disguised form.

## 1.6 First unrepaired global implication

The repository currently states the residual as:

1. complete shallow-inner cells;
2. the unique possible interface-straddling cell;
3. the terminal truncated cell;
4. compensation with the unused top interval.

That is accurate but still describes four objects separately. The smallest useful
analytic obligation is to combine them into one exact interface-to-top suffix.

---

# 2. The missing analytic theorem

## 2.1 Canonical outer-prefix/suffix split

Let

\[
\tau=A(\mu),
\qquad
b=\lfloor\tau\rfloor.
\]

Every cell \(1\le n\le b\) is complete and full-outer, because

\[
n\le b\le\tau<H.
\]

Therefore Round 48 proves

\[
L_n>
\frac{19N_n}{48}+\frac{27}{128}>0
\qquad(1\le n\le b).
\]

Define the exact residual suffix

\[
\boxed{
\mathcal R_{\mathrm{suf}}
:=
\int_b^H F(t)\,dt
-
\sum_{\substack{n\ge b+1\\ n-\frac14<H}}
S_2(N_n).
}
\tag{SFX}
\]

Then

\[
\boxed{
\mathrm{WT}_4
=
\sum_{n=1}^{b}L_n+\mathcal R_{\mathrm{suf}}.
}
\tag{SPLIT}
\]

The first desired theorem is

\[
\boxed{\mathcal R_{\mathrm{suf}}\ge0.}
\tag{SFX+}
\]

This is sufficient for \(\mathrm{WT}_4\). It is not equivalent to it, because a
negative suffix could in principle be paid by the positive full-outer prefix.

## 2.2 Clipped-action normalization

Define

\[
B(z):=(A(z)-b)_+,
\qquad
\widehat H=H-b,
\qquad
R=\xi(b),
\]

and let

\[
\eta(s)=\xi(b+s),
\qquad
0\le s\le\widehat H.
\]

Then \(\eta\) is the decreasing inverse of \(B\) on \([0,R]\), and

\[
\boxed{
\mathcal R_{\mathrm{suf}}
=
\int_0^{\widehat H}\frac{\eta(s)^3}{3}\,ds
-
\sum_{k-\frac14<\widehat H}
S_2\!\left(\left\lceil\eta(k-\tfrac14)\right\rceil-1\right).
}
\tag{NSFX}
\]

Equivalently,

\[
\boxed{
\mathcal R_{\mathrm{suf}}
=
\int_0^R z^2B(z)\,dz
-
\sum_{1\le a<R}a^2
\left[B(a)+\frac14\right]_<.
}
\tag{SSFX}
\]

The normalization has a decisive structural property:

\[
\boxed{
B(\mu)=\tau-b\in[0,1).
}
\tag{IF}
\]

Hence the inner/outer interface lies in the first normalized height cell. Only
that first cell can straddle the interface. Every complete cell with index
\(k\ge2\) is wholly inner. This removes the need for an interface-indexed family.

## 2.3 Exact terminal decomposition

Write

\[
\widehat H=q+\alpha,
\qquad
q=\lfloor\widehat H\rfloor,
\qquad
0\le\alpha<1.
\]

Then

\[
\mathcal R_{\mathrm{suf}}
=
\sum_{k=1}^{q}
\left[
\int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds
-
S_2(M_k)
\right]
+
\mathcal T_{\mathrm{top}},
\]

where

\[
M_k=\left\lceil\eta(k-\tfrac14)\right\rceil-1
\]

and

\[
\boxed{
\mathcal T_{\mathrm{top}}
=
\int_q^{q+\alpha}\frac{\eta(s)^3}{3}\,ds
-
\mathbf 1_{\{\alpha>3/4\}}
S_2\!\left(
\left\lceil\eta(q+\tfrac34)\right\rceil-1
\right).
}
\tag{TOP}
\]

At \(\alpha=3/4\), the terminal node lies on the strict support wall and is
excluded. This exact top term must never be discarded before the final sign.

## 2.4 Why this is the correct proof obligation

This suffix formulation:

- includes every shallow-inner cell;
- includes the unique possible interface cell;
- includes every already proved deep-inner cell;
- includes terminal truncation;
- retains the unused top interval;
- uses no ratio ladder, count ladder, floor family, or chamber family;
- preserves literal ceilings;
- is one bounded, falsifiable theorem.

It is strictly better organized than four independent residual lemmas.

---

# 3. Analytic proof plan

## 3.1 Exact row-cone representation

For each complete normalized cell \(k\), define the occupancy profile

\[
\omega_k(z)
=
\operatorname{length}
\bigl([k-1,k]\cap[0,B(z)]\bigr)
=
\min\{1,\max\{0,B(z)-k+1\}\}.
\]

Then layer cake gives

\[
\boxed{
\int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds
=
\int_0^R z^2\omega_k(z)\,dz.
}
\tag{ROW1}
\]

For every integer \(M\ge0\),

\[
\boxed{
S_2(M)
=
\int_{1/2}^{M+1/2}z^2\,dz-\frac{M}{12}.
}
\tag{ROW2}
\]

Therefore

\[
\boxed{
L_k
=
\int_0^R z^2
\left(
\omega_k(z)
-
\mathbf 1_{[1/2,M_k+1/2]}(z)
\right)dz
+\frac{M_k}{12}.
}
\tag{ROW3}
\]

This identity is exact. It is the discrete row-cone reserve. Unlike the rejected
continuous quarter-node inequality, it keeps the literal integer \(M_k\) and the
Euler correction \(M_k/12\).

Derive an analogous exact row formula for \(\mathcal T_{\mathrm{top}}\), with the
truncated occupancy

\[
\omega_{\mathrm{top}}(z)
=
\min\{\alpha,\max\{0,B(z)-q\}\}.
\]

## 3.2 Sum the rows before estimating them

Do not attempt to prove \(L_k\ge0\) for every shallow cell. Instead, sum (ROW3)
over the complete suffix rows and add the exact top row. The target becomes one
integral inequality

\[
\boxed{
\mathcal R_{\mathrm{suf}}
=
\int_0^R z^2\mathcal K_B(z)\,dz
+
\frac1{12}\sum_k M_k
+\text{exact terminal correction}
\ge0,
}
\tag{BLOCK}
\]

where \(\mathcal K_B\) is the explicitly printed difference between the continuous
occupancy cone and the union of literal discrete row intervals.

The proof must exploit cancellations in \(\mathcal K_B\). Independent
worst-casing of individual rows is forbidden.

## 3.3 Use the one-interface geometry

On \(0<z<\mu\),

\[
\sigma(z)=-A'(z)
=
\frac{\arcsin(z/\mu)-\arcsin(z/K)}{\pi},
\]

and on \(\mu<z<K\),

\[
\sigma(z)=\frac{\arccos(z/K)}{\pi}.
\]

The normalized interface condition (IF) means:

- the outer cap contributes only to the first normalized row;
- all later complete rows are inner;
- the deep-inner portion \(z\le\mu/\sqrt2\) is already positive;
- any adverse curvature is confined to
  \[
  \frac{\mu}{\sqrt2}<z<\mu.
  \]

Thus the missing sign is a localized shallow-inner/interface correction, not a
global inverse-action problem.

## 3.4 Falsifiable curvature sublemma

Define, on the inner branch,

\[
Q(z)=2\sigma(z)-z\sigma'(z).
\]

Equivalently,

\[
Q(z)
=
\frac1\pi\left[
2\left(
\arcsin\frac z\mu-\arcsin\frac zK
\right)
-
z\left(
\frac1{\sqrt{\mu^2-z^2}}
-
\frac1{\sqrt{K^2-z^2}}
\right)
\right].
\]

Since

\[
F''(t)=\frac{zQ(z)}{\sigma(z)^3},
\]

a natural first sub-obligation is:

> Prove or falsify that \(Q\) has at most one zero on \((0,\mu)\), with the
> nonnegative side containing \(0<z\le\mu/\sqrt2\).

A one-crossing theorem would permit a Peano-kernel or convex–concave transport:
the negative curvature is one terminal interval adjacent to the interface and can
be paired with the first-row outer reserve and the exact top term.

Do not assume this theorem. If it is false, record an exact counterexample and
replace it by the weakest integrated sign-change bound actually needed for
(BLOCK).

## 3.5 Composite Peano-kernel route

Let

\[
J(t)=-F'(t)=\frac{\eta(t)^2}{\sigma(\eta(t))}.
\]

Starting from the exact past/future identity used for the full-outer cell, derive
the composite quadrature error for the entire suffix as

\[
\mathcal R_{\mathrm{suf}}
=
\text{literal ceiling reserve}
+
\int_0^{\widehat H}P_{\widehat H}(s)F''(s)\,ds
+
\text{exact terminal boundary term},
\]

with the Peano kernel \(P_{\widehat H}\) printed explicitly and all support
breaks assigned.

Required sign mechanism:

1. prove the sign or monotonicity of the cumulative Peano kernel;
2. combine it with the one-crossing or integrated curvature theorem;
3. retain the first interface row and terminal row until the final line;
4. use the certified deep-inner cells as positive reserve rather than replacing
   them by zero too early.

The proof may use Abel summation or one integration by parts to move from
pointwise curvature to cumulative curvature. Every boundary term must be printed.

## 3.6 Discrete majorization route

In parallel, seek a direct majorization theorem for the literal rows:

\[
\sum_{k}S_2(M_k)
\le
\int_0^{\widehat H}\frac{\eta(s)^3}{3}\,ds.
\]

The theorem may compare cumulative row counts rather than individual rows. A valid
argument could prove, for every cut height \(y\),

\[
\sum_{k\le y}M_k
\quad\text{or}\quad
\sum_{k\le y}M_k^2
\]

is controlled by the corresponding continuous superlevel moment, with the
\(M_k/12\) reserve accumulated exactly.

This route must retain the uniform shell interval. Generic total positivity for
arbitrary atomic measures is already rejected.

## 3.7 Primary success theorem

Round 49 should aim to prove:

\[
\boxed{
\mathcal R_{\mathrm{suf}}\ge0
\quad
\text{for every strict-active }(\rho,K).
}
\tag{R49}
\]

Together with the full-outer lemma, this proves literal \(\mathrm{WT}_4\).

## 3.8 Quantified fallback if the suffix is false

If a directed exact counterexample to (R49) is found while literal
\(\mathrm{WT}_4\ge0\), retain the exact positive prefix instead of abandoning the
direct-layer route.

Define

\[
\mathcal R_{\mathrm{out}}
=
\sum_{n=1}^{b}
\left(
\frac{19N_n}{48}+\frac{27}{128}
\right).
\]

Then the next weaker sufficient theorem is

\[
\boxed{
\mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}\ge0.
}
\tag{R49-FB}
\]

This is still analytic and correlated. It is stronger than literal WT4 because
the actual outer cells exceed \(\mathcal R_{\mathrm{out}}\), so it must be
classified as sufficient, not equivalent.

Do not create a ratio or floor partition to prove (R49-FB).

## 3.9 Independent fallback routes

Keep these alive only as independent pressure:

1. **Component \(U\):**
   charge maximal negative \(D_A\)-components with disjoint bonus cells and one
   neighboring positive tail.
2. **Row-cone \(\Theta\):**
   use the exact adverse-wall reduction and prove a cumulative row reserve.
3. **Literal falsification:**
   search for \(\mathrm{WT}_4<0\) independently of every sufficient route.

Do not combine three unsigned routes into one purported proof.

---

# 4. Strategy revision

## 4.1 Recommended decision

Continue the direct inverse-layer program for one more sharply scoped round, but
replace “prove four residual cell types” by the single suffix theorem (R49).

This is a refinement, not a strategic reversal.

## 4.2 Why no major route switch is yet warranted

Round 48 established two infinite analytic regions and localized all unresolved
curvature to a one-unit interface height plus a shallow inner band. The direct route
has not failed; only an over-strong continuous relaxation has failed. The discrete
QCL remained strongly positive at the exact counterexample.

## 4.3 Switching criteria

Switch away from direct suffix QCL only if one of the following occurs:

1. an exact counterexample to (R49) is certified and (R49-FB) also fails as a
   viable analytic target;
2. the suffix proof necessarily requires a forbidden count/floor/ratio/chamber
   family;
3. the derivation produces another unsigned scalar with no new invariant,
   localization, or exact compensation identity.

If direct suffix QCL stops, the next preferred route is the Round 47 component
inequality \(U\), not pointwise Gate B.

## 4.4 Next three to five rounds

1. **Round 49:** prove or falsify the interface-to-top suffix theorem.
2. **Round 50:** if Round 49 passes, independently certify the scoped \(d=4\)
   aggregate and audit all activity, action, interface, and terminal walls.
3. **Round 51:** freeze and independently audit the general-dimensional
   branching backbone.
4. **Round 52:** derive a dimension-uniform weighted-aggregate lifting mechanism
   for \(d\ge5\).
5. **Round 53:** whole-cover and theorem assembly, followed by a clean manuscript
   rebuild.

A complete \(d=4\) aggregate does not by itself promote the all-dimensional
aggregate or `TARGET-shell-general-d`.

---

# 5. Round 49 Prompt A — lead interface-to-top suffix proof

## Role

Act as the lead analytic agent. Prove (R49), rigorously falsify it, or produce one
new exact block identity that materially reduces it. Do not return another
cell-by-cell chamber list.

## Mandatory sources

Read at minimum:

```text
state/proof_obligations.yml
human/inbox/general-d_simplified_analytic_strategy.md
human/inbox/general-d-next-discovery-portfolio.md
human/current_directives.md
state/approach_registry.md
state/gap_register.md

human/outbox/general-d-round-47-d4-weighted-aggregate.md
human/outbox/general-d-round-47-clean-room-d4-weighted.md
human/outbox/general-d-round-47-independent-audit.md

human/outbox/general-d-round-48-portfolio-discovery.md
human/outbox/general-d-round-48-independent-audit.md
rounds/polya-main/round_048/discovery/portfolio-wave-ledger.md

state/lemma_packets/SHELL-general-d-d4-full-outer-action-cell-round48.md
rounds/polya-main/round_048/certification/outer-cell-lead.md
rounds/polya-main/round_048/certification/outer-cell-clean-room.md
rounds/polya-main/round_048/certification/outer-cell-adversarial-audit.md

state/lemma_packets/SHELL-general-d-d4-deep-inner-action-cell-round48.md
rounds/polya-main/round_048/certification/deep-inner-cell-lead.md
rounds/polya-main/round_048/certification/deep-inner-cell-clean-room.md
rounds/polya-main/round_048/certification/deep-inner-cell-adversarial-audit.md

rounds/polya-main/round_048/diagnostics/continuous-quarter-node-counterexample.md
computations/general_d_round48_continuous_quarter_node_counterexample.py
computations/general_d_round48_qcl_diagnostic.py
```

Do not use the old opening text of `state/next_round_prompts.md` as authority.

## A1. Re-derive the exact split

Prove (SPLIT), (NSFX), (SSFX), (IF), and (TOP) from the strict bracket, with no
unstated endpoint convention.

Audit:

- \(b=0\);
- \(\tau\in\mathbb Z\);
- \(\widehat H<3/4\);
- \(\alpha=3/4\);
- \(K,\mu,R\in\mathbb Z\);
- the support wall \(R=0\);
- the strict active wall.

## A2. Reproduce the rejected-route regression

Before proposing a new inequality, reproduce the directed Round 48 continuous
quarter-node counterexample and verify that the literal discrete suffix/QCL value
at that record remains positive.

Any proposed theorem that implies the false continuous inequality is immediately
rejected.

## A3. Derive the exact row-cone block

Prove (ROW1)--(ROW3) and the exact terminal-row analogue. Sum them to obtain one
printed formula for \(\mathcal R_{\mathrm{suf}}\).

The formula must identify:

- the continuous occupancy kernel;
- the literal integer row intervals;
- every \(M_k/12\) correction;
- the interface-row contribution;
- the terminal top contribution;
- every discarded term, if any.

## A4. Curvature theorem

Prove or falsify the one-crossing candidate for

\[
Q(z)=2\sigma(z)-z\sigma'(z).
\]

If the literal one-crossing statement is false, determine the weakest integrated
substitute sufficient for the block Peano inequality. A numerical plot is not a
substitute for a theorem.

## A5. Sign the suffix

Attempt, in this order:

1. cumulative row-cone majorization;
2. composite Peano kernel plus the curvature theorem;
3. Abel summation retaining the first interface row and terminal row;
4. the quantified fallback (R49-FB), but only after an exact counterexample to
   (R49) or a proved obstruction to its sign mechanism.

Use the certified deep-inner cells as retained positive reserve. Do not discard
them before measuring the shallow loss.

## A6. Required falsification

Independently test:

- the literal suffix (R49);
- the fallback (R49-FB);
- the exact row-cone block;
- the one-crossing claim;
- the literal \(\mathrm{WT}_4\).

Any named negative must receive rational parameter brackets, exact strict-wall
ownership, and directed Arb arithmetic.

## A7. Output contract

The report must contain:

1. exact notation and hypotheses;
2. line-by-line derivations;
3. dependency ledger;
4. exact loss ledger;
5. no-double-counting ledger;
6. equality-face audit;
7. falsification table;
8. a clear separation of theorem, sufficient reduction, diagnostic, and failure;
9. final verdict;
10. files modified.

## Forbidden approaches

Do not:

- reopen R45.18 or pointwise Gate B;
- use the continuous quarter-node polynomial inequality;
- transfer a \(1/\sigma\) pointwise slab theorem to the
  \(\xi^2/\sigma\) QCL kernel;
- introduce a ratio, floor, count, \(B\), \(Q\), or chamber ladder;
- use a new compact certificate;
- promote a finite positive sweep;
- edit the manuscript, state file, proof graph, or completed \(d=3\) chain.

## Required files

Create only:

```text
human/outbox/general-d-round-49-interface-to-top-suffix.md
computations/general_d_round49_suffix_diagnostic.py
```

An optional symbolic replay may be added:

```text
computations/general_d_round49_suffix_replay.wl
```

---

# 6. Round 49 Prompt B — clean-room block reconstruction

## Independence boundary

Before freezing the clean-room derivation, do not read:

```text
human/outbox/general-d-round-49-interface-to-top-suffix.md
computations/general_d_round49_suffix_diagnostic.py
computations/general_d_round49_suffix_replay.wl
human/outbox/general-d-round-49-adversarial-interface-to-top.md
```

Read the authoritative state, binding strategy, Round 47--48 audits, and the two
certified lemma packets only.

## Role

Derive the suffix theorem independently from the clipped spatial action (SSFX).
Do not begin from the lead's Peano kernel.

## Required tasks

1. Prove the outer-prefix/suffix split and clipped-action normalization.
2. Derive the exact terminal truncation formula with strict ownership at
   \(\alpha=3/4\).
3. Develop an independent route using one of:
   - weighted trapezoidal floor sums;
   - cumulative majorization;
   - Abel summation in the radius variable;
   - monotone transport of the row occupancy cone.
4. Determine whether the interface height \(B(\mu)<1\) yields a universal
   first-row compensation theorem.
5. Use the deep-inner convexity theorem only within its exact scope.
6. Attempt an exact block sign; if it fails, print the first unsupported
   inequality and an extremal parameter pattern.
7. Freeze the pre-comparison text and record its hash.
8. After freeze, compare with Prompt A line by line.

## Required output

```text
human/outbox/general-d-round-49-clean-room-interface-to-top.md
```

The report must distinguish the frozen independent derivation from the
post-comparison audit.

---

# 7. Round 49 Prompt C — independent adversarial falsification

## Independence boundary

Build the evaluator independently. Do not import the Prompt-A evaluator or its
formula implementation.

## Literal quantities

Evaluate independently:

\[
\mathrm{WT}_4
=
\frac{K^4-\mu^4}{64}
-
\sum_{1\le a<K}a^2[A(a)+1/4]_<,
\]

\[
\mathcal R_{\mathrm{suf}},
\qquad
\mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}},
\]

the complete-cell \(L_k\), the exact top term, and every new Prompt-A sufficient
scalar.

Compute each key target in two independent forms whenever possible:

- inverse-height integration;
- spatial clipped-action integration;
- direct finite proxy sum.

## Mandatory stress classes

Search:

1. \(\tau=A(\mu)\) just below, on, and just above an integer;
2. \(B(\mu)\downarrow0\) and \(B(\mu)\uparrow1\);
3. a first normalized cell straddling the interface;
4. the shallow band \(\mu/\sqrt2<z<\mu\);
5. the deep/shallow seam \(z=\mu/\sqrt2\);
6. \(\widehat H\) near \(0,1/4,3/4,1\) modulo integers;
7. terminal nodes appearing and disappearing;
8. integer and near-integer \(K,\mu,R\);
9. activity equality and immediately active parameters;
10. \(\rho\downarrow0\) and \(\rho\uparrow1\);
11. moderate frequency;
12. large \(K\) and large row count;
13. every Round 47--48 route counterexample.

## Classification

Use exactly:

### A. Literal aggregate counterexample

\[
\mathrm{WT}_4<0.
\]

This falsifies the scoped aggregate route, not the spectral theorem.

### B. Suffix-route counterexample

\[
\mathcal R_{\mathrm{suf}}<0,
\qquad
\mathrm{WT}_4\ge0.
\]

This rejects (R49) only.

### C. Fallback counterexample

\[
\mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}<0,
\qquad
\mathrm{WT}_4\ge0.
\]

This rejects (R49-FB) only.

### D. Auxiliary-route counterexample

A Peano, one-crossing, majorization, component-\(U\), or row-cone strengthening
fails while its parent target remains nonnegative.

### E. Positive record

Diagnostic only; never continuum coverage.

## Directed certification

For every negative or near-zero named record:

- use rational \(\rho,K\), or rational brackets with uniqueness;
- certify strict activity;
- certify every action wall and literal ceiling;
- certify interface and terminal ownership;
- use directed Arb at two precisions;
- print the full exact ledger;
- classify the result against the literal and sufficient targets separately.

The final output must contain

```text
positive_coverage_certificate: FALSE
```

unless a separately authorized finite-coverage theorem is actually proved.

## Required files

```text
human/outbox/general-d-round-49-adversarial-interface-to-top.md
computations/general_d_round49_independent_suffix_search.py
```

---

# 8. Round 49 Prompt D — final independent audit

## Role

After Prompts A--C are frozen, audit the mathematics and state implications
adversarially.

## Allowed verdicts

```text
PASS
PASS WITH MINOR REPAIRS
STRUCTURAL PASS — FINAL SIGN OPEN
COMPUTER-ASSISTED CANDIDATE ONLY
INCOMPLETE
FAIL
FALSIFIED
```

## Required determinations

1. What exact theorem or reduction was proved?
2. Was (R49) proved on the complete strict-active domain?
3. If (R49) failed, was (R49-FB) proved?
4. Was literal \(\mathrm{WT}_4\) proved or falsified?
5. Is the outer-prefix/suffix split exact at \(\tau\in\mathbb Z\)?
6. Is the terminal node at \(\alpha=3/4\) assigned correctly?
7. Is every strict ceiling retained?
8. Is the interface confined to the first normalized row exactly?
9. Are the full-outer and deep-inner lemmas used only in scope?
10. Is the continuous quarter-node counterexample respected?
11. Is any sufficient inequality reported as equivalent?
12. Are all computations classified correctly?
13. What is the first unrepaired implication?
14. Which proof-obligation statuses should change?
15. What is the next single obligation?

## Status discipline

- If (R49) is proved, the scoped
  `SHELL-general-d-weighted-aggregate-d4` may be considered for
  `proved_internal` only after an independent whole-domain assembly verifies
  the exact implication to literal \(\mathrm{WT}_4\).
- A proved \(d=4\) aggregate does not promote
  `SHELL-general-d-weighted-aggregate`.
- It does not promote the branching backbone.
- It does not promote `TARGET-shell-general-d`.
- A falsified suffix route does not demote literal \(\mathrm{WT}_4\).
- A falsified literal \(\mathrm{WT}_4\) is a counterexample to this proxy
  sufficient route, not automatically to the shell spectral theorem.
- The completed \(d=3\) theorem remains unchanged.

## Required output

```text
human/outbox/general-d-round-49-independent-audit.md
```

The audit may propose an RFC-6902 state patch but must not edit the state file.

---

# 9. Round 49 success and stop criteria

## Success

One of:

1. a complete analytic proof of (R49);
2. a complete analytic proof of (R49-FB);
3. a complete analytic proof of literal \(\mathrm{WT}_4\) by an independently
   audited registered route;
4. an exact counterexample to literal \(\mathrm{WT}_4\).

## Substantive partial success

One of:

- exact suffix normalization plus a proved one-crossing curvature theorem;
- exact block Peano identity reducing the sign to one intrinsic integral;
- an exact cumulative majorization theorem covering all but one explicit
  boundary term;
- a directed counterexample to (R49) with literal WT4 positive;
- a new bounded residual lemma that passes lead, clean-room, and adversarial
  certification.

## Stop

Stop the round if:

- the route requires a ratio/floor/count/chamber family;
- a second compact certificate is required;
- only another unsigned projection remains after the exact block identities;
- the continuous quarter-node route reappears;
- computation is the only support for an infinite-domain sign.

---

# 10. Expected Round 49 file set

```text
human/outbox/general-d-round-49-interface-to-top-suffix.md
human/outbox/general-d-round-49-clean-room-interface-to-top.md
human/outbox/general-d-round-49-adversarial-interface-to-top.md
human/outbox/general-d-round-49-independent-audit.md

computations/general_d_round49_suffix_diagnostic.py
computations/general_d_round49_independent_suffix_search.py
computations/general_d_round49_suffix_replay.wl  # optional
```

No manuscript, state, proof-graph, or completed three-dimensional file is to be
modified in this reasoning round.
