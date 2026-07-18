# General-dimensional spherical-shell Pólya project
## Referee evaluation and instructions for a simplified analytic completion

**Audience:** the AI developing `spherical-shell-polya-general-d.tex`.

**Status:** the current manuscript contains a strong exact dimension-lifting backbone and substantial partial tail analysis, but it does **not** prove the all-dimensional theorem. The two explicitly open branches are the first-floor no-drop branch and the residual high-floor first-drop branch. Do not state the general-dimensional Pólya theorem as proved until both are closed or replaced by a sufficient weighted aggregate theorem.

---

# 1. Executive directive

Keep the exact algebraic reduction. Stop extending the ratio ladder and stop adding independent chamber certificates.

The revised critical path is:

\[
\boxed{
\text{phase proxy}
\Longrightarrow
\text{exact branching}
\Longrightarrow
W_d-P_d^{<}
=
\mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m)
\Longrightarrow
\text{one correlated shelf--terminal theorem}
}
\]

Use the following hierarchy.

1. **Primary analytic target:** prove the required shifted-tail inequality on the **spectrally active region** for the integer and half-integer shifts that actually occur. Use the strongest available no-mode wall in dimension \(d\):
   \[
   K^2>\frac{\pi^2}{(1-\rho)^2}+\frac{(d-2)^2-1}{4}.
   \]
2. **First fallback:** prove the weighted aggregate inequality directly, using the positive branching bonus \(\mathcal B_d(A)\).
3. **Second fallback:** prove a quantitative shifted-tail inequality with a rigorously derived, localized error budget and absorb it after convolution.
4. **Last fallback:** one consolidated, low-dimensional, reproducible interval certificate for a compact residual. Do not use a sequence of overlapping certificates and ratio thresholds.

The final paper should be organized around one reusable analytic lemma, not around the chronology of successive computational rounds.

---

# 2. Referee evaluation of the current manuscript

## 2.1 What is mathematically strong and should be preserved

Preserve the following results, subject only to normal editorial compression.

### A. General-dimensional spectral proxy

The real-order Bessel phase estimate applies at

\[
\nu_{\ell,d}=\ell+\frac{d-2}{2},
\]

with the correct spherical-harmonic multiplicity. The strict proxy is wall-safe and is the correct starting point.

### B. Exact branching decomposition

Retain

\[
P_d^{<}
=
\sum_{m\ge0}c_{d,m}T_A(r_m),
\qquad
c_{d,m}=\binom{m+d-3}{d-3},
\qquad
r_m=m+\frac{d-2}{2}.
\]

This is exact on both parity grids and introduces no interpolation error.

### C. Signed branching primitive

Retain the proof that

\[
\Delta_d(z)\le0.
\]

The AM--GM argument at the grid points and the per-cell critical-point argument are clean. Attribute the underlying higher-dimensional primitive comparison accurately to the FLPS ball mechanism; the shell-specific contribution is the retained defect identity below.

### D. Master branching-defect identity

This is the conceptual center of the general-dimensional paper:

\[
\boxed{
W_d-P_d^{<}
=
\mathcal B_d(A)
+
\sum_{m\ge0}c_{d,m}D_A(r_m),
}
\]

where

\[
D_A(r)=2\int_r^K A(z)\,dz-T_A(r),
\qquad
\mathcal B_d(A)=2\int_0^K(-A'(z))(-\Delta_d(z))\,dz\ge0.
\]

Do not discard \(\mathcal B_d(A)\) in the endgame. It exists precisely to absorb a controlled weighted tail deficit if pointwise positivity is awkward.

### E. Proven tail modules

Retain these as modules:

- outer convex tails \(r\ge\mu\);
- the strict turning-zone zero-tail statement;
- the complete one-interface theorem \(0<\mu-r<1\);
- the fixed-ratio and thin high-energy estimates, as fallback owners;
- the wall-safe first-shelf reduction;
- the scale-free shelf-curvature estimate;
- the inverse-action terminal reserve;
- the strengthened dimensional no-mode wall.

These are not disposable. A global margin proof may replace some of them later, but deleting them before a replacement is proved would remove the best existing control of the interface geometry.

## 2.2 What is not acceptable as the final methodology

### A. The proof is incomplete

The current manuscript itself leaves:

- the first-floor no-drop case \(f=1,\ p=n\);
- a residual high-floor first-drop compact region.

Therefore the main all-dimensional theorem is not proved.

### B. The endgame violated the intended gate discipline

After the local bad-cell pairing failed, the strategy required trying, in order:

1. a fractional-interface trapezoidal formulation;
2. a correlated inverse-action/sawtooth formulation;
3. the aggregate identity using \(\mathcal B_d(A)\).

The manuscript instead introduced a first-shelf scalar and then expanded it through a long chain of ratio-specific owners and certificates. That fork produced useful lemmas, but it should not remain the final architecture.

### C. The current estimates destroy real positive correlation

The difficult branches are not numerically close to zero. Independent checks reproduce approximate active-region deficits of about

\[
0.57\quad\text{in the first-floor no-drop branch},
\qquad
1.95\quad\text{in the high-floor first-drop branch}.
\]

Yet some reduced certificate margins are near \(10^{-6}\) or smaller. The loss is in the reduction, not in the original inequality.

The main sources of lost margin are:

- replacing the exact shelf payment by \(R_p\ge-p/2\);
- bounding the shelf remainder and the terminal level surplus independently;
- discarding fractional information in the terminal inverse levels;
- replacing the local inner cap by universal constants;
- repeatedly separating variables that satisfy exact action and floor relations.

### D. The computer-assisted part is fragmented

A rigorous computer-assisted proof is legitimate, but the current architecture is not efficient: multiple certificate families, millions of boxes, ratio ladders, and very small reported margins still leave open branches.

The final proof may use **one** compact certificate after a strong analytic reduction. It should not use computer assistance as the main geometric decomposition of the parameter space.

### E. The verification package is not self-contained in the current upload

The manuscript refers to many scripts, audit files, precision replays, and hashes. Those files are not present with the uploaded TeX/PDF package. Until the complete verification bundle is supplied and independently replayed, the corresponding computer-assisted propositions cannot be fully audited from the manuscript alone.

---

# 3. Adjudication of the two reviewer strategies

The two reviewers agree on the diagnosis but propose different cures.

## 3.1 Useful conclusion from reviewer R2

R2's strongest contribution is the **wall-compensation diagnosis**:

- when the first shelf has a poor local remainder, its samples hug a floor wall;
- wall hugging forces the terminal one-interface action to sit near a definite level;
- this creates additional complete ball levels and fractional inverse-level reserve;
- therefore the shelf loss and the terminal reserve are anticorrelated and must be estimated together.

Adopt this as the first analytic route.

R2's numerical sweep is useful theorem-design evidence, not proof. It supports retaining the bare shifted-tail inequality as a plausible theorem. Do not turn the empirical lower bound \(D_A\gtrsim0.54\) into an asserted universal constant without proof.

In particular, do **not** state \(D_A(r)\ge1/4\) as the formal theorem merely because the sweep suggests it. The formal target remains \(D_A(r)\ge0\); a positive reserve should emerge from the proof.

## 3.2 Useful conclusion from reviewer R3

R3 correctly emphasizes that the spectral theorem needs only a **weighted aggregate**, not pointwise positivity of every shifted tail. The margin-plus-localized-error framework is a legitimate fallback and may ultimately give the cleanest all-dimensional paper.

However, do not adopt R3's quantitative ansatz as already established.

The sample inequality

\[
D_A(r)
\ge
\frac{\pi-2}{2\pi}(K-r)-0.18
\]

is not uniform. For example, at

\[
(\rho,K,r)=(0.53,7.1,1/2),
\]

one finds

\[
D_A(r)\approx1.0019168616,
\]

whereas the proposed right side is approximately

\[
1.0191547512.
\]

Thus the proposed calibration fails. A margin theorem may still be true with a different error function \(\Xi\), but its constants and localization must be proved.

Also correct the scaling claim for the branching bonus. Typically

\[
-\Delta_d(z)=O(z^{d-3}),
\]

so

\[
\mathcal B_d(A)=O(K^{d-2}),
\]

not \(O(K^{d-1})\). It is a valuable lower-order reserve, not a second macroscopic volume term.

Finally, do not delete all of Sections 6--7 before proving a replacement. The one-interface theorem, first-shelf reduction, curvature estimate, and terminal reserve are precisely the tools needed to derive either the pointwise or aggregate theorem.

## 3.3 Final synthesis

Use a **hybrid strategy**:

- first derive one correlated pointwise shelf--terminal theorem on the active region;
- if a face resists, sum the exact correlated defects and use \(\mathcal B_d(A)\);
- pursue a localized-margin theorem in parallel only after its constants and support are derived from an exact identity;
- reserve a single compact certificate for the final fallback.

---

# 4. Definitions and exact identities to use

Fix

\[
\mu=\rho K,
\qquad
A(z)=G_K(z)-G_\mu(z),
\]

and a relevant shift

\[
r\in\mathbb N\cup(\mathbb N_0+1/2),\qquad r\ge1/2.
\]

Define

\[
T_A(r)=
\left[A(r)+\frac14\right]_<
+
2\sum_{j\ge1}
\left[A(r+j)+\frac14\right]_<,
\]

\[
D_A(r)=2\int_r^K A(z)\,dz-T_A(r).
\]

For an inner tail \(r<\mu\), put

\[
n=\lfloor\mu-r\rfloor,
\qquad
q=r+n,
\qquad
q\le\mu<q+1.
\]

Let \(p\) be the last point of the first ordinary-floor shelf and let

\[
d_\rho=\frac{2\arcsin\rho}{\pi}.
\]

Use the wall-safe first-shelf reduction

\[
\boxed{
D_A(r)
\ge
D_A(q)+R_p+\frac{d_\rho}{2}(n-p).
}
\tag{S1}
\]

On the first shelf, with ordinary-floor remainders

\[
\varepsilon_j=A(r+j)+\frac14-F_j\in[0,1),
\]

retain the exact identity

\[
\boxed{
R_p=C_p+p\left(\varepsilon_0+\varepsilon_p-\frac12\right),
}
\tag{S2}
\]

and the curvature estimate

\[
\boxed{
C_p
\ge
\frac{p^2}{3(2r+p)}(\varepsilon_0-\varepsilon_p).
}
\tag{S3}
\]

For the no-drop branch \(p=n\), use the sharper exact identity from the manuscript rather than (S1):

\[
\boxed{
D_A(r)
=
D_A(q)
-
\frac n2
+
2n\varepsilon_q
+
2\int_0^n u\,\sigma(r+u)\,du
+
\chi_q,
}
\tag{S4}
\]

where \(\sigma=-A'\) and \(\chi_q\) is the favorable endpoint-wall term.

---

# 5. Strengthen the terminal reserve before doing any new casework

The manuscript's inverse-action lemma loses the strict fractional part of each inverse level. Restore it.

Let \(g\) be a decreasing convex terminal action, let

\[
v=g(0),
\qquad
B=\left[g(0)+\frac14\right]_<,
\]

and let \(y_k\) satisfy

\[
g(y_k)=k-\frac14,
\qquad 1\le k\le B.
\]

Put

\[
c_k=-g'(y_k),
\qquad
\eta_k=y_k-[y_k]_<\in(0,1].
\]

The exact level contribution is

\[
2\lceil y_k\rceil-1
=
2y_k+1-2\eta_k.
\]

Repeating the tangent proof therefore gives the strengthened lemma

\[
\boxed{
D_g
\ge
\sum_{k=1}^{B}
\left(
\frac1{2c_k}-1+2\eta_k
\right)
+
\frac{(v-B)_+^2}{c_v}.
}
\tag{T1}
\]

For the one-interface shell tail at \(q\), define

\[
v=G_K(q),
\qquad
B=\left[v+\frac14\right]_<,
\qquad
Q=\left[A(q)+\frac14\right]_<,
\]

\[
\beta=\frac{\arccos(q/K)}{\pi},
\]

and let \(\theta_k\) solve

\[
\frac K\pi\bigl(\sin\theta_k-\theta_k\cos\theta_k\bigr)
=k-\frac14.
\]

Then \(c_k=\theta_k/\pi\), and the strengthened shell reserve is

\[
\boxed{
D_A(q)
\ge
\frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
+
2\sum_{k=1}^{B}\eta_k
-
Q
-
2\delta
+
\frac{(v-B)_+^2}{\beta},
}
\tag{T2}
\]

where

\[
\delta=\int_q^\mu G_\mu(z)\,dz.
\]

Also retain the exact local cap. Put

\[
\alpha=\mu-q\in[0,1),
\qquad
h=G_\mu(q).
\]

Convexity gives the endpoint-safe estimate

\[
\boxed{
0\le 2\delta\le\alpha h,
}
\tag{T3}
\]

with strict inequality when \(\alpha>0\). Do not replace (T3) by a universal constant until the final line of an estimate.

The variables satisfy the exact correlation

\[
A(q)=v-h.
\tag{T4}
\]

Preserve (T2)--(T4) simultaneously. This is the terminal source of the margin lost in the current proof.

---

# 6. New central theorem: correlated shelf--terminal compensation

The new analytic target is the following.

## Theorem target CST

For every spectrally active inner shift on either relevant grid,

\[
\boxed{
D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\ge0.
}
\tag{CST}
\]

The proof must estimate the complete expression, not its summands independently.

## Required proof structure

Prove a finite dichotomy or trichotomy based on intrinsic quantities, not on a ladder of ratio endpoints.

### Case I: remainder-rich shelf

If

\[
\varepsilon_0+\varepsilon_p
\]

is sufficiently large, then (S2) pays most or all of \(-p/2\). Use (S3) for the remaining curvature payment. The terminal inequality may then be used only through \(D_A(q)\ge0\).

### Case II: curvature-rich shelf

If

\[
\varepsilon_0-\varepsilon_p
\]

is large, (S3) gives a scale-free payment. Optimize the coefficient without replacing \(2r+p\) by a global worst case too early.

### Case III: wall-hugging shelf

If both preceding payments are small, then the shelf lies close to one ordinary-floor wall. Use the exact floor relations and the shell elasticity inequality to prove a quantitative terminal consequence:

- an increased complete-level surplus \(B-Q\);
- or a lower bound for \(\sum\eta_k\);
- or a positive top interval \((v-B)_+^2/\beta\);
- or a combination of these.

This is the wall-compensation transport mechanism. The proof should explicitly show that the same hypothesis that makes \(R_p\) poor makes (T2) strong.

Do not replace this correlation by separate lower bounds for \(R_p\), \(B-Q\), \(\delta\), and the terminal angles.

## Normalization

Use normalized variables such as

\[
c=\frac{\arccos\rho}{\pi},
\qquad
\alpha=\mu-q,
\qquad
h=G_\mu(q),
\qquad
v=G_K(q),
\]

and discrete level data \((f,Q,B)\). Avoid raw chamber variables whenever they can be eliminated by

\[
A(q)=v-h,
\qquad
q=r+n,
\qquad
0\le\alpha<1.
\]

The final theorem should have at most a small number of intrinsic cases, ideally the four natural branches

\[
(f=1,p=n),\quad
(f=1,p<n),\quad
(f\ge2,p=n),\quad
(f\ge2,p<n).
\]

Do not subdivide the last branch by a sequence of rational \(\rho\)-thresholds.

---

# 7. Order of attack

## WP0. Freeze and reproduce

1. Freeze the current manuscript as an archive.
2. Obtain and replay every referenced certificate.
3. Create a dependency graph distinguishing analytic theorems, computer-assisted theorems, and unproved claims.
4. Build an exact/high-precision evaluator for \(D_A(r)\), (S1)--(S4), and (T2).

**Gate 0:** if a genuine counterexample to pointwise \(D_A(r)\ge0\) is found, switch immediately to the aggregate theorem in Section 9.

## WP1. Prove the strengthened terminal lemma

Prove (T1)--(T3) in a standalone note, including every strict wall.

**Completion criterion:** no later proof may use the weaker terminal lemma unless it explicitly explains why the fractional terms are irrelevant.

## WP2. Close the first-floor no-drop branch

Use the exact no-drop identity (S4), not the general first-shelf lower bound.

Split by the number \(B\) of complete terminal ball levels:

1. \(B=0\): use the zero-level triangle, (T3), curvature, and the favorable endpoint wall;
2. \(B=1\): use the full one-level version of (T2), including \(2\eta_1\);
3. \(B\ge2\): use the complete-level angle sum and prove monotonicity in \(B\), reducing the hard check to the smallest admissible \(B\).

**Completion criterion:** one analytic theorem for all active first-floor no-drop tails. No interval subdivision by \(\rho\) or \(K\).

## WP3. Reprove the high no-drop floors economically

The current certificates for \(f\ge2\) should be replaced, as far as possible, by an analytic lower bound for

\[
\sum_{k=1}^{B}(k-1/4)^{-1/3}.
\]

Use an integral estimate and the shelf constraints to prove automatic positivity for all sufficiently large \(f\). Retain, at most, a very small exact check for the first one or two floors.

## WP4. Prove CST for the high-floor first-drop branch

Start from the single correlated scalar obtained by combining (S1)--(S3) with (T2)--(T4). Use the elasticity inequality already proved in the manuscript to transport a poor shelf reserve into a terminal level reserve.

Do not introduce another ratio ladder.

**Gate 4A:** if CST closes analytically, retire all ratio-round theorems and high-floor certificates.

**Gate 4B:** if one intrinsic face remains, proceed to the aggregate theorem. Do not add more pointwise owners.

## WP5. Compress the already proved first-floor first-drop sector

The current result may be retained, but rewrite it as:

- one analytic reduction;
- one compact theorem;
- one optional verification appendix.

Remove the history of separate certificate rounds from the main text.

## WP6. Extend thin/fixed-ratio owners only as insurance

Improve the thin theorem only if it substantially shrinks the aggregate or certificate residual. Do not optimize thin constants for their own sake.

## WP7. Assemble and rewrite

After closure, rebuild the paper from a clean branch. Do not edit the 82-page research log into the final paper line by line.

---

# 8. Quantitative-margin route: parallel fallback, not an assumption

A useful alternative target is

\[
D_A(r)
\ge
\alpha_0 L(r)-\Xi(r;\rho,K),
\tag{M1}
\]

where \(L(r)\) is a positive length/action scale and \(\Xi\) is localized.

Do not fix \(\alpha_0=(\pi-2)/(2\pi)\) or any additive constant before proving them.

To make (M1) useful, prove all of the following:

1. an exact derivation of the positive term;
2. a precise support theorem for \(\Xi\), preferably a turning band of width \(O(K^{1/3})\) plus an explicitly controlled interface band;
3. a pointwise bound for \(\Xi\);
4. a binomially weighted bound
   \[
   \sum_m c_{d,m}\Xi(r_m);
   \]
5. a complete moderate-frequency audit, since a flat per-tail error creates a threshold growing with \(d\);
6. a separate treatment of the conserved angular rounding; convolution does not average it away.

If these are proved, sum (M1) through the branching identity. The linear margin sum is of order \(K^{d-1}\); a genuinely turning-localized \(O(1)\) error has weighted mass of order \(K^{d-8/3}\). That is a promising asymptotic separation, but it is not a proof until the localization and the moderate-frequency window are explicit.

---

# 9. Aggregate fallback using the branching bonus

If pointwise CST fails or remains too complicated, prove directly

\[
\boxed{
\mathcal B_d(A)
+
\sum_{m\ge0}c_{d,m}D_A(r_m)
\ge0.
}
\tag{WT}
\]

This is sufficient for the spectral theorem.

## Required steps

1. Identify the shifts where the available analytic lower bound for \(D_A(r_m)\) may be negative.
2. Prove that this set is localized in shift/action space.
3. Derive a quantitative cellwise lower bound for \(-\Delta_d(z)\). The natural scale is
   \[
   -\Delta_d(z)\asymp z^{d-3}
   \]
   away from exceptional equality points.
4. Convert the resulting lower bound for \(\mathcal B_d(A)\) into an action moment.
5. Compare the weighted negative tail mass with this moment.
6. Treat \(d=4\) explicitly first; it is likely the hardest new aggregate dimension. Use the completed \(d=3\) theorem as the base case, not as another shifted-tail obligation.

Do not claim that \(\mathcal B_d(A)\) is of order \(K^{d-1}\). Its natural scale is generally \(K^{d-2}\). Use it to absorb localized or lower-order losses.

---

# 10. Optical fallback

Only after CST and WT have been seriously attempted should an optical owner be introduced.

If needed:

1. lift the product count through the same branching coefficients;
2. formulate one shift-uniform planar optical lemma;
3. compare the cumulative multiplicity with the Weyl moment by Euler--Maclaurin or the signed primitive;
4. choose the ratio seam from the estimates, not from the old three-dimensional value \(39/50\);
5. avoid dimension-by-dimension product tables.

The optical theorem should be one regional owner, not a new finite staircase.

---

# 11. Rules for computation

1. Numerical searches are for falsification and theorem design only.
2. Every heuristic margin must be labeled heuristic.
3. A load-bearing certificate must include:
   - the exact compact domain;
   - the exact inequalities certified;
   - directed rounding or rational arithmetic;
   - a finite coverage/termination proof;
   - all source code and data;
   - an independent replay.
4. Use at most one compact certificate in the final implication chain.
5. Do not report millions of boxes, queue depths, hashes, or precision experiments in the main paper. Put them in a verification document.
6. Exact rational wall checks of the type used in the one-interface theorem are acceptable analytic lemmas, not “computer proofs,” provided the inequalities are printed and hand-checkable.

---

# 12. Output contract for the AI

For every new proposed lemma, produce exactly these items.

1. **Statement**, including strict-wall conventions.
2. **Dependencies**, listing only earlier proved lemmas.
3. **Proof**, with no numerical step hidden behind prose.
4. **Equality-face audit** for:
   \[
   A(r+j)+\frac14\in\mathbb N,
   \quad
   r+j=\mu,
   \quad
   r+j=K,
   \quad
   \mu-r\in\mathbb N.
   \]
5. **Loss ledger:** list every positive term discarded and explain why it is harmless.
6. **Counterexample search:** test the lemma numerically before presenting it as a target.
7. **Failure report:** if the proof does not close, state the exact remaining inequality and the extremal parameter pattern. Do not replace it immediately by another ratio partition.

The AI must not:

- claim the full theorem while an explicit branch remains open;
- introduce a new empirical constant as a theorem premise;
- create another sequence of “Round A/B/C” theorems;
- worst-case correlated floor and action variables independently without first testing the resulting loss;
- delete a proved module before its replacement is complete;
- use absent scripts as a proof premise.

---

# 13. Final manuscript architecture

The final paper should be rebuilt with the following structure.

1. **Main theorem and proof map**
2. **General-dimensional phase proxy**
3. **Exact harmonic branching**
4. **Signed primitive and branching-defect identity**
5. **Correlated shifted-tail theorem**
   - outer/turning tails;
   - one-interface theorem;
   - strengthened terminal reserve;
   - shelf--terminal compensation;
6. **Aggregate or optical fallback**, only if used
7. **Completion, dilation, and endpoint conventions**
8. **Optional non-tiling appendix**
9. **Separate verification supplement**, only if a compact certificate remains

Remove from the live paper:

- superseded ratio rounds;
- research-log language;
- SHA hashes and replay statistics;
- duplicated residual boxes;
- obsolete certificate theorems;
- historical failed lemmas, except for a brief explanatory remark if mathematically illuminating.

---

# 14. Acceptance checklist

The all-dimensional proof is ready only when all of the following hold.

- [ ] Sections corresponding to the phase proxy, branching, signed primitive, and master identity are independently checked.
- [ ] Every relevant integer and half-integer shift is covered on the active region.
- [ ] The first-floor no-drop branch is closed.
- [ ] The high-floor first-drop branch is closed, pointwise or in the weighted aggregate.
- [ ] The moderate-frequency window is explicitly empty or owned.
- [ ] Thin shells are covered without a dimension-specific staircase.
- [ ] Every strict equality wall has an owner.
- [ ] No unprovided script is a theorem premise.
- [ ] Any remaining computation is one compact, reproducible certificate.
- [ ] The final proof graph contains no superseded theorem.
- [ ] The abstract accurately states whether computer assistance is used.

---

# 15. Immediate next task

Do **not** prove another ratio theorem.

The next deliverable is a standalone note titled:

> **Fractional terminal reserve and shelf--terminal compensation for shifted shell tails**

It must contain:

1. the proof of (T1)--(T3);
2. the exact combined scalar from (S1)--(S3) and (T2)--(T4);
3. an analytic closure of the first-floor no-drop branch;
4. a precise CST statement for the high-floor first-drop branch;
5. a gate decision: analytic CST, weighted aggregate WT, or one compact certificate.

Only after this note is complete should the general-dimensional manuscript be rewritten.
