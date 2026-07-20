# Binding instruction for Codex 5.6 Sol
## General-dimensional spherical-shell Pólya project: Round 38 and the completion strategy

**Date:** 19 July 2026  
**Target agent:** Codex 5.6 Sol  
**Status:** research instruction; no theorem-status promotion is authorized by this document

---

# 0. Source precedence and theorem boundary

Read and obey the sources in this order.

1. `proof_obligations.yml` is authoritative. The expected SHA-256 of the supplied copy is
   `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.
2. `general-d_simplified_analytic_strategy(1).md` is binding for methodology.
3. `current_state.md` and `best_proof_draft.md` define the live theorem boundary.
4. The audited Round 28, 34, 35, 36, and 37 notes supply the promoted local results.
5. `general-d-r2.md` is advisory. Use the accepted ideas below, but do not import its overstatements or its proposed near-ball corner without proving feasibility.

The selected obligation remains

\[
\texttt{SHELL-general-d-high-floor-first-drop-CST}.
\]

The all-dimensional theorem is **not proved**. The exact general-dimensional branching backbone is to be preserved, but its authoritative status is `derived_under_assumptions`, not `proved_internal`; its frozen line-by-line audit remains outstanding. Do not upgrade it in prose or in `proof_obligations.yml`.

Round 37 is a structural reduction only. The live gap task is to prove one of

\[
\Gamma_{\rm gap}\ge 0,
\qquad
\mathcal H_\Delta\ge 0,
\]

or to close the exact stronger scalar \(\Phi_\delta^+\) by one intrinsic correlated argument. Strict positivity is not needed when equality already proves \(D_A(r)\ge0\).

No ratio ladder, no theorem family indexed by \(B\), \(j\), or shell-ratio intervals, no chamber proliferation, and no new compact certificate are permitted.

---

# 1. Adjudication of `general-d-r2.md`

## 1.1 Adopt these points

The report is useful in five respects.

1. **Scope discipline.** It correctly keeps high-floor CST and the all-dimensional theorem open.
2. **Negative-knowledge ledger.** It correctly warns against reusing the counterexampled signs
   \(\mathcal R\), \(\mathcal R_J\), \(\mathcal C_8\), \(\mathcal C_{\max,8}\), \(\mathcal F\), global \(\alpha\)-monotonicity, the Round 11--12 pre-shelf sign, and the rejected calibrated margin.
3. **Falsification first.** A directed adversarial search should accompany a new sufficient scalar before several proof rounds are spent on it. Such a search is diagnostic only.
4. **Explicit fallback activation.** The project needs a precise mathematical stop rule for leaving a compressed scalar and restoring the exact shifted-tail scalar \(\mathscr S\), followed by the weighted aggregate.
5. **Aggregate readiness.** The two aggregate blockers are correctly identified: localization of possibly negative shifts and a quantitative lower bound for the branching bonus away from primitive equality cells. The scaling \(\mathcal B_d(A)=O(K^{d-2})\) must be retained.

Repository-hash drift and certificate consolidation are valid state-hygiene tasks, but they are nonblocking for the Round 38 mathematics.

## 1.2 Correct or reject these points

### A. The general-dimensional backbone is not yet frozen as proved

The report calls the phase/branching/defect backbone “proved.” The authoritative obligation state calls it `derived_under_assumptions` pending a frozen independent audit. Preserve the formulas, but do not promote their status.

### B. The report misses the strongest strict-floor consequence

On a literal positive-\(\alpha\) gap, \(j\le\lambda<j+1\) is not the sharp conclusion. Put

\[
u:=\lambda-j=\{\lambda\}.
\]

Round 38 must prove

\[
0<u<\frac\alpha2<\frac12,
\qquad
j<\lambda<j+\frac12.
\]

Thus no finite integer-\(\lambda\) wall lies in the positive-\(\alpha\) gap. The only finite gap-side integer limit is \(\alpha\downarrow0\), where \(\lambda\downarrow j^+\). The Round 37 discussion of a gap-owned \(\lambda\to N^-\) side must be removed or explicitly marked as generic strict-floor arithmetic outside the gap owner.

### C. “Lossless” needs a qualifier

The \(\Omega/\Xi\) form is exact for the selected projected scalar \(\Gamma_{\rm gap}\). It is not lossless relative to \(\Phi_\delta^+\) or \(D_A(r)\). In particular,

\[
\Xi=E-M_4=2e_p+(\Delta-M_4),
\]

so define

\[
\widehat\Xi:=\Delta-M_4\ge0,
\qquad
\Xi=2e_p+\widehat\Xi.
\]

The discarded projection reserve between \(\Phi_\delta^+\) and \(\Gamma_{\rm gap}\) is \(a_p(\Delta-M_4)=a_p\widehat\Xi\), in addition to earlier inherited tangent/shelf losses between \(D_A\) and \(\Phi_\delta^+\).

### D. Outer-\(B\), integer-\(\lambda\), and alpha endpoints require one-sided labels

At an outer wall \(v+\tfrac14=N\), the literal strict bracket is \(N-1\). The gap-side label is a one-sided label \(B^+=N\). Do not write the gap label as the literal bracket at the wall.

At \(\alpha=0\), the literal point has \(h=0\) and \(B=Q\); it is the separate simultaneous equal-count corner. The lower gap endpoint is only the limit \(\alpha\downarrow0\). The upper endpoint is \(\alpha\uparrow1^-\) and must not be identified with the next chart’s literal \(\alpha=0\) point.

### E. The claimed near-ball degenerate corner is not feasible at smallest interface count

The report proposes the simultaneous pattern

\[
B_0=1,
\qquad
\zeta=\frac d{2c}\downarrow0,
\qquad
t\uparrow\frac\pi2.
\]

This is impossible on the gap. Round 38 must make the exact count-phase compensation explicit. Since \(q\ge3\), \(\mu\ge3\), and

\[
W=B_0+\frac34-u,
\qquad 0<u<\frac12,
\]

one has for \(B_0=1\)

\[
W<\frac74,
\qquad
\tan t-t=\frac{\pi W}{\mu}<\frac{7\pi}{12}.
\]

But

\[
\tan\frac{5\pi}{12}-\frac{5\pi}{12}>\frac{7\pi}{12},
\]

because \(\tan(5\pi/12)=2+\sqrt3>\pi\). Hence

\[
t<\frac{5\pi}{12},
\qquad
\zeta=\frac\pi{2t}-1>\frac15.
\]

More generally, \(B_0\zeta\) does not degenerate when \(t\uparrow\pi/2\): the interface count grows as the per-level payment shrinks. The report’s curvature-only “degenerate corner” is therefore not a valid primary theorem reduction.

### F. A fixed number of rounds is not a stop rule

Do not use “two rounds, then \(\mathscr S\)” as a mechanical rule. Stop or continue according to the exact criteria in Section 6 below.

---

# 2. Round 38 primary theorem package

Produce one analytic note, provisionally named

`general-d-round-38-gap-position-count-phase-and-face-compensation.md`.

The note must have a theorem boundary, dependencies, exact wall ownership, a loss ledger, a diagnostic section clearly labelled nonproof, and a decision gate. It must prove as much of the following package as possible in the listed order.

---

## R38.1. Gap-position coordinate and ownership repair

Work on the hard one-level gap

\[
B=Q+1,
\qquad
B_0=Q=B-1\ge1,
\qquad
0<\alpha<1.
\]

Put

\[
j=f-B,
\qquad
u:=\lambda-j,
\qquad
S_q:=A(q)-W,
\qquad
\chi:=u-S_q.
\]

Prove the exact inequalities

\[
\boxed{
0<S_q\le u<S_q+h<\frac\alpha2,
\qquad
0\le\chi<h,
\qquad
0<u<\frac\alpha2<\frac12.}
\tag{R38.1}
\]

Derive the exact normal coordinates

\[
\boxed{
W=B-\frac14-u,}
\tag{R38.2}
\]

\[
\boxed{
A(q)=B-\frac14-\chi,
\qquad
v=B-\frac14+h-\chi,}
\tag{R38.3}
\]

\[
\boxed{
\xi:=A(q)+\frac14-Q=1-\chi,}
\tag{R38.4}
\]

and, with \(x=r+p\),

\[
\boxed{
A(x)-A(q)=j+e_p+\chi.}
\tag{R38.5}
\]

Record the endpoint dictionary without ambiguity:

| owner | exact gap coordinate |
|---|---:|
| literal \(Q\)-wall | \(\chi=0\) |
| gap interior | \(0<\chi<h\) |
| gap-side outer-\(B\) closure | \(\chi=h\), \(y_B=0\), label \(B^+\) |
| lower gap limit \(\alpha\downarrow0\) | \(h,\chi,u\to0\); literal endpoint is equal-count |
| upper alpha endpoint \(\alpha\uparrow1^-\) | retain the one-sided gap labels; do not identify with the next chart |

Promote an explicit sublevel corollary for the exclusion \(B_0=0\): state the exact hypotheses inherited from Rounds 34--35,

\[
W<\frac34,
\qquad
A(x)-A(q)\ge1,
\qquad
P>dM,
\]

and state that these hypotheses, not the literal equality \(A(q)=3/4\), are what place the tuple in the normalized Round 34 domain.

---

## R38.2. Sharpen \(\Xi\), \(M_4\), and the selected normal form

Define

\[
\widehat\Xi:=\Delta-M_4\ge0.
\]

Prove and use

\[
\boxed{
\Xi=2e_p+\widehat\Xi.}
\tag{R38.6}
\]

The exact selected scalar is therefore

\[
\boxed{
\Gamma_{\rm gap}
=1-J+B_0\zeta+\Omega
 +(p+a_p)M_4+2pe_p+p\widehat\Xi
 -\frac{p-dm}{2},}
\tag{R38.7}
\]

where \(\zeta=d/(2c)=\pi/(2t)-1\).

From

\[
M_4\ge\tau(E+2\lambda),
\qquad
E=\Delta+2e_p\ge M_4+2e_p,
\qquad
\tau=\frac g{g+2},
\]

prove

\[
\boxed{
M_4\ge g(\lambda+e_p).}
\tag{R38.8}
\]

Do not call (R38.7) lossless without saying “lossless for the selected projected scalar.”

Correct the sign language:

- \(\Gamma_{\rm gap}\ge0\) is sufficient;
- \(\Gamma_{\rm gap}=0\) already closes the projected gate;
- a genuine selected-scalar obstruction is \(\Gamma_{\rm gap}<0\), in which case the analogue of Round 37 (9.2) is strict;
- \(\Phi_\delta^+>\mathcal H_\Delta\) remains genuinely strict on the gap and its gap-side limits, but not at the separate literal equal-count \(\alpha=0\) corner.

---

## R38.3. Count-phase compensation and an immediate new closure

Prove the following lemma without splitting by \(B_0\).

### Lemma R38-CP

Every hard gap point and every finite gap-side endpoint satisfies

\[
\boxed{B_0\zeta>\frac15.}
\tag{R38.9}
\]

A preferred proof is the following.

From (R38.2),

\[
B_0+\frac14<W\le B_0+\frac34,
\tag{R38.10}
\]

If \(\zeta\ge1/5\), use \(B_0\ge1\), and rule out equality by the \(B_0=1\), \(t=5\pi/12\) contradiction described in Section 1.2E.

If \(0<\zeta<1/5\), put

\[
x=\frac\pi2-t=\frac{\pi\zeta}{2(1+\zeta)}.
\]

Prove the elementary inequality

\[
\cot x>\frac1x-x
\qquad(0<x<\pi/2)
\tag{R38.11}
\]

by differentiating

\[
x\cos x-(1-x^2)\sin x.
\]

Then

\[
\tan t-t>\frac1x-\frac\pi2.
\]

Using \(\mu\ge3\) and \(B_0\ge W-3/4\) (with strictness supplied by (R38.11)), obtain

\[
B_0\zeta>
\frac{6(1+\zeta)}{\pi^2}-\frac{9\zeta}{4}
>\frac15,
\]

where the last inequality follows at \(\zeta=1/5\) from \(\pi^2<10\).

### Corollary R38-CP2

Use (R38.7), \(J<1/7\), and nonnegativity of the remaining terms to prove

\[
\boxed{
\Gamma_{\rm gap}
>\frac{37}{35}-\frac{p-dm}{2}.}
\tag{R38.12}
\]

Therefore the gap is closed whenever

\[
\boxed{p-dm\le\frac{74}{35}.}
\tag{R38.13}
\]

In particular, every residual gap with \(p=2\) is closed, because \(d,m>0\) imply \(p-dm<2\). The \(p=1\) gap was already closed in Round 36. Thus all remaining gap work after this corollary has \(p\ge3\).

This is the first required substantive output of Round 38. Do not proceed to a more elaborate endpoint proof before establishing or decisively rejecting this lemma.

---

## R38.4. Unified \(Q\)-wall/outer-\(B\) compensation

For the residual \(p\ge3\) faces, do not begin with a curvature-only worst case. First preserve the exact position \(\chi\) and the newest inverse level.

Put

\[
b_K(z)=\frac1\pi\arccos\frac zK,
\qquad
\beta=b_K(q),
\]

and split

\[
\Omega=\Omega_-+\omega_B,
\]

where

\[
\Omega_-=
\sum_{k=1}^{B_0}
\left(
\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k
\right),
\]

\[
\omega_B=
\frac\pi{2\theta_B}-1+2y_B.
\]

From (R38.3), prove the exact newest-level identity

\[
\boxed{
h-\chi
=v-\left(B-\frac14\right)
=\int_q^{q+y_B}b_K(z)\,dz.}
\tag{R38.14}
\]

Since \(b_K\) is decreasing and \(\theta_B\le\pi\beta\), derive

\[
\boxed{
y_B\ge\frac{h-\chi}{\beta},}
\tag{R38.15}
\]

\[
\boxed{
\omega_B\ge
\frac1{2\beta}-1+
\frac{2(h-\chi)}{\beta}.}
\tag{R38.16}
\]

Use the actual adjacent action drop (R38.5), not its Round 37 truncation:

\[
\boxed{
\Delta>R_1(j+e_p+\chi).}
\tag{R38.17}
\]

Let

\[
H_*=(p+a_p)R_1,
\qquad
n=f-1,
\qquad
B_0=n-j.
\]

The exact minimum algebra gives

\[
B_0\zeta+(p+a_p)\Delta
>
 n\min\{\zeta,H_*\}+H_*e_p+H_*\chi.
\tag{R38.18}
\]

For \(0\le\chi\le h\), prove

\[
\boxed{
H_*\chi+\frac{2(h-\chi)}{\beta}
\ge
h\min\left\{H_*,\frac2\beta\right\}.}
\tag{R38.19}
\]

Combining (R38.16)--(R38.19) yields the single proof-level lower bound

\[
\boxed{
\begin{aligned}
\Phi_\delta^+>{}&
\frac1{2\beta}-J+\Omega_-\\
&+(f-1)\min\{\zeta,H_*\}
 +H_*e_p\\
&+h\min\left\{H_*,\frac2\beta\right\}
 +2pe_p-\frac{p-dm}{2}.
\end{aligned}}
\tag{R38.20}
\]

This is a lemma inside the proof, not a new permanent certificate and not a claim that \(\mathcal H_\Delta\ge0\). State the conclusion accurately:

- if the right-hand side is nonnegative, then \(\Phi_\delta^+>0\);
- positivity of this sharpened expression does **not** imply that the older, smaller \(\mathcal H_\Delta\) is nonnegative;
- do not rename (R38.20) as another global scalar family.

The mechanism is unified:

- at the \(Q\)-wall, \(\chi=0\) and the newest inverse displacement pays;
- at the outer-\(B\) closure, \(\chi=h\) and the adjacent action pays while \(y_B=0\);
- in the interior, the payment interpolates linearly;
- old inverse bad sides remain inside \(\Omega_-\), with their literal/adverse \(\eta_k\) values retained.

---

## R38.5. Optional root-free lower bound for \(\Omega_-\)

Use this only if the exact \(\Omega_-\) cannot be handled directly on a transported endpoint. Do not discard \(\Omega_-\) earlier.

For \(1\le k\le B_0\),

\[
W-\left(k-\frac14\right)=B_0-k+1-u.
\tag{R38.21}
\]

Since

\[
\frac d{d\theta}
\left[\frac K\pi(\sin\theta-\theta\cos\theta)\right]
=\frac K\pi\theta\sin\theta
\]

and \(\theta\sin\theta\) is increasing on \((0,\pi/2)\), prove

\[
\boxed{
\Omega_-
\ge
\frac{\pi^2}{2Kt^3\sin t}
\left(
\frac{B_0(B_0+1)}2-B_0u
\right).}
\tag{R38.22}
\]

Because \(0<u<1/2\), this implies

\[
\Omega_->
\frac{\pi^2B_0^2}{4Kt^3\sin t}.
\tag{R38.23}
\]

Retain \(u\) in the primary version. Equation (R38.23) is a final coarse corollary only.

---

## R38.6. Endpoint order of attack

After the \(p\le2\) closure, analyze the transported residual in this order.

### 1. Outer-\(B\) plus lower shelf

Use

\[
\chi=h,
\qquad
y_B=0,
\qquad
e_p=0.
\]

Do not claim that \(\eta_B\) is “near \(\alpha\)” on this face; it is exactly zero. Preserve \(u>h\), \(J\), \(W\), \(\Omega_-\), \(M_4\), and \(\widehat\Xi\).

### 2. Outer-\(B\) plus upper alpha endpoint

Set \(\alpha\uparrow1^-\), so \(\mu=q+1\), while retaining the one-sided gap labels. The exact cap formulas are

\[
\boxed{
h=
\frac{
\sqrt{2q+1}-q\arccos\!\left(\frac q{q+1}\right)
}{\pi},}
\tag{R38.24}
\]

\[
\boxed{
J=
\frac{
\bigl((q+1)^2+2q^2\bigr)
\arccos\!\left(\frac q{q+1}\right)
-3q\sqrt{2q+1}
}{2\pi}.}
\tag{R38.25}
\]

Also retain

\[
W=\frac{q+1}{\pi}(\tan t-t).
\]

Prove one intrinsic continuous inequality. Do not subdivide by \(B_0\), \(j\), or ratio intervals.

### 3. \(Q\)-wall endpoints

Use \(\chi=0\), so \(\xi=1\) and the newest inverse displacement is active. Keep the exact strict owner and the old inverse collisions.

### 4. Generic old inverse faces

At a literal inverse wall, \(\eta_k=1\); on the adverse side, \(\eta_k\downarrow0\). The newest level is not an old inverse wall. Use the fixed-\(K\) transport from Round 36 and avoid creating an extra chamber.

### 5. Lower alpha limit

Treat only the gap-side limit \(\alpha\downarrow0\), where \(h,\chi,u\to0\). The literal endpoint is the separate equal-count simultaneous \(B/Q\) corner and is not covered by the gap theorem.

The currently most dangerous **feasible** pattern is therefore not “\(B_0=1\) and \(t\to\pi/2\).” It is the smallest feasible count/phase configuration after the count-phase lemma, with

\[
p\ge3,
\quad e_p=0,
\quad \chi=h,
\quad y_B=0,
\quad \eta_k\downarrow0\text{ on old inverse bad sides},
\]

and with \(u,h,\widehat\Xi,M_4\) as small as exact feasibility permits. Determine the phase from \(W=\mu(\tan t-t)/\pi\); do not prescribe \(t\uparrow\pi/2\) in advance.

---

# 3. Directed falsification work for Round 38

Run a targeted diagnostic in parallel with the proof. It is not a theorem premise.

Concentrate on the exact transported faces above and on \(p\ge3\). Test, with directed interval arithmetic or certified rational/transcendental enclosures where practical,

\[
\Gamma_{\rm gap}<0,
\qquad
\mathcal H_\Delta<0,
\qquad
\text{RHS of (R38.20)}<0.
\]

At every negative selected-scalar record, also evaluate the exact shifted-tail scalar

\[
\mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

and record the loss ledger

\[
D_A(r)-\mathscr S,
\quad
\mathscr S-\Phi_\delta^+,
\quad
\Phi_\delta^+-\Gamma_{\rm gap}.
\]

A certified \(\Gamma_{\rm gap}<0\) point falsifies only the universal sign of the selected projection. It does not falsify \(\Phi_\delta^+\), \(\mathscr S\), \(D_A\), CST, or the theorem.

Search requirements:

- enforce both parity grids and the dimension-labelled activity wall;
- enforce the literal strict brackets, not rounded substitutes;
- sample both literal and adverse one-sided inverse ownership;
- keep \(\alpha=0\) equal-count corners out of the gap dataset;
- report finite minima only as diagnostics;
- do not promote a decimal margin or a scan cutoff into the proof.

---

# 4. Required Round 38 deliverables

Produce all of the following.

1. **Analytic note** `general-d-round-38-gap-position-count-phase-and-face-compensation.md` containing:
   - theorem boundary and dependency list;
   - the Round 37 corrections;
   - proofs of (R38.1)--(R38.13), or a precise proof-level obstruction;
   - the unified compensation lemma (R38.14)--(R38.20);
   - any endpoint sign actually proved;
   - a strict wall/one-sided ownership table;
   - a loss ledger;
   - a diagnostic-only falsification report;
   - the stop/fallback decision from Section 6.
2. **Symbolic replay** `general_d_round38_gap_position_replay.wl` checking algebraic identities only. Strict-floor ownership must remain printed in the note.
3. **Optional diagnostic** for exact/directed endpoint search. Mark every output `diagnostic_only`.
4. **No status edits** to `proof_obligations.yml` and no all-dimensional theorem claim. Promotion requires an independent audit after the note is complete.

The note must distinguish three outcomes:

- `proved`: a displayed analytic sign with a complete implication chain;
- `structural reduction`: exact identities/transport without a final sign;
- `diagnostic`: finite search or theorem-design evidence.

---

# 5. Mathematica replay identities

Use a replay block equivalent to the following. Mathematica is not allowed to own strict brackets or endpoint labels.

```wl
ClearAll["Global`*"];

G[a_, z_] :=
  (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi;

(* Gap-position algebra *)
gapRules = {
  lambda -> j + u,
  f -> B + j,
  W -> B - 1/4 - u,
  Sq -> u - chi,
  Aq -> W + Sq,
  v -> Aq + h,
  Q -> B - 1,
  Ax -> f - 1/4 + ep
};

FullSimplify[
 {
  Aq - (B - 1/4 - chi),
  v - (B - 1/4 + h - chi),
  (Aq + 1/4 - Q) - (1 - chi),
  (Ax - Aq) - (j + ep + chi)
 } /. gapRules
]
(* {0,0,0,0} *)

(* Xi refinement *)
FullSimplify[
 (E - M4) - (2 ep + Delta - M4),
 Assumptions -> E == Delta + 2 ep
]
(* 0 *)

tau = gEl/(gEl + 2);
FullSimplify[2 tau/(1 - tau) - gEl]
(* 0 *)

(* Count-phase change of variables *)
tFromZeta = Pi/(2 (1 + zeta));
xFromZeta = FullSimplify[Pi/2 - tFromZeta];
(* Pi zeta/(2(1+zeta)) *)

FullSimplify[
 zeta (3/(Pi xFromZeta) - 9/4)
]
(* 6(1+zeta)/Pi^2 - 9 zeta/4 *)

(* Cotangent lower-bound proof auxiliary *)
FullSimplify[
 D[x Cos[x] - (1 - x^2) Sin[x], x]
]
(* x^2 Cos[x] + x Sin[x] *)

(* Linear chi compensation *)
compLow = FullSimplify[
 H chi + 2 (h - chi)/beta - h H
];
(* (h-chi) (2/beta-H) *)

compHigh = FullSimplify[
 H chi + 2 (h - chi)/beta - 2 h/beta
];
(* chi (H-2/beta) *)

(* Interface action-gap sum *)
FullSimplify[
 Sum[B0 - k + 1 - u, {k, 1, B0}],
 Assumptions -> Element[B0, Integers] && B0 >= 1
]
(* B0 (B0 + 1 - 2 u)/2 *)

(* Gamma refinement *)
FullSimplify[
 (p + ap) M4 + p Xi -
 ((p + ap) M4 + 2 p ep + p XiHat),
 Assumptions -> Xi == 2 ep + XiHat
]
(* 0 *)

(* Immediate threshold *)
FullSimplify[6/7 + 1/5 - 1]
(* 2/35 *)

(* Upper-alpha exact cap *)
mu = q + 1;
hAlpha1 = FullSimplify[G[mu, q], Assumptions -> q > 0];

Jclosed =
 ((mu^2 + 2 q^2) ArcCos[q/mu]
   - 3 q Sqrt[mu^2 - q^2])/(2 Pi);

Jcheck = FullSimplify[
 2 Integrate[G[mu, z], {z, q, mu}] - Jclosed,
 Assumptions -> q > 0,
 TransformationFunctions -> {Automatic, FunctionExpand}
];
(* 0 *)
```

Add exact replays for any new derivative or convexity claim used to sign a transported endpoint. Do not replace a printed analytic proof by a zero returned from Mathematica.

---

# 6. Explicit stop and fallback criteria

Do not decide by elapsed rounds. Use the following mathematical gates.

## Gate A: selected projection

Continue the \(\Gamma_{\rm gap}\) route only while its exact terms can be controlled by the count-phase lemma, the \(u,\chi\) coordinates, and one intrinsic continuous endpoint inequality.

Stop the universal \(\Gamma_{\rm gap}\ge0\) target immediately if a certified exact feasible point has \(\Gamma_{\rm gap}<0\). Do not repair it by defining another compressed scalar.

If \(\Gamma_{\rm gap}\) is false or analytically exhausted, make one exact attempt through \(\mathcal H_\Delta\) or directly through \(\Phi_\delta^+\) using (R38.20). Stop this pointwise projection route if either:

1. the relevant sufficient sign is certified false on an exact feasible transported face; or
2. proving it would require a ratio partition, a \(B\)- or \(j\)-indexed theorem family, a new chamber certificate, or replacing \(J,W,u,e_p,\Omega,\Xi\) by unrelated worst cases.

A negative value of the proof-level RHS (R38.20) does not itself falsify \(\Phi_\delta^+\); it only exhausts that lower bound.

## Gate B: restore the exact shifted-tail scalar

On the resisting face, return to

\[
\boxed{
\mathscr S=D_A(q)+R_p+\frac{dm}{2}.}
\]

Restore the exact first-shelf trapezoid, the complete terminal surplus, the exact cap, and every inverse fraction. Do not project through \(M_4\) unless the exact identity explicitly retains the discarded difference.

Stop the exact pointwise route and activate the aggregate if either:

1. a certified exact feasible point has \(\mathscr S<0\); or
2. the possible negative support of \(\mathscr S\) cannot be localized by one intrinsic shelf--terminal theorem without forbidden ratio/count/chamber splitting.

## Gate C: weighted aggregate

Activate

\[
\boxed{
\mathcal B_d(A)+
\sum_{m\ge0}c_{d,m}D_A(r_m)\ge0}
\]

with \(d=4\) first. The first two obligations are:

1. localize every shift on which the exact tail can be negative;
2. derive a quantitative cellwise lower bound for \(-\Delta_d\) away from primitive equality cells and compare the branching-bonus moment with the weighted negative-tail mass.

Do not assume an error ansatz before deriving its support and constants from an exact identity. The completed \(d=3\) theorem is the base case. No second compact certificate is authorized during this route.

---

# 7. Whole-strategy sequence after Round 38

## Stage I. Finish the one-level gap

Use the Round 38 count-phase closure first, then the \(u,\chi\) compensation on the remaining \(p\ge3\) transported faces. A proof of \(\Gamma_{\rm gap}\ge0\), \(\mathcal H_\Delta\ge0\), or exact \(\Phi_\delta^+\ge0\) closes this class.

## Stage II. Transfer only proven structural lemmas to the equal-count classes

For every positive-\(\alpha\) face, the elementary enclosure

\[
B-1\le B_0\le B
\]

is useful. Before claiming an interface payment on higher \(Q_N\) or equal-count inverse faces, rederive the exact terminal decomposition there and check that no unit or top interval is double counted. Do not assume the gap formula survives unchanged.

Then treat, in order:

1. higher \(Q_N\) faces \(N\ge2\);
2. equal-count generic inverse faces;
3. the literal \(\alpha=0\) simultaneous \(B/Q\) corners;
4. general lower shelves outside the precise Round 30--32 scope.

## Stage III. Pointwise assembly

Only after every shifted-tail class is closed, audit the disjoint grid cover:

- integer shifts \(r\ge1\);
- half-integer shifts \(r\ge3/2\);
- \(r=1/2\) owned by the completed \(d=3\) theorem;
- the dimension-dependent no-mode equality face;
- moderate-frequency ownership;
- every strict radial, action, inverse, and alpha wall.

The general-dimensional branching backbone must receive its separate frozen line-by-line audit before final theorem promotion.

## Stage IV. Aggregate fallback if pointwise CST resists

Use the exact branching-defect identity and \(\mathcal B_d(A)\), beginning with \(d=4\). Do not return to ratio owners or fragmented certificates.

## Stage V. Final proof architecture

The final paper must be organized around:

\[
\text{phase proxy}
\to
\text{exact branching}
\to
\text{branching-defect identity}
\to
\text{one correlated pointwise theorem or one weighted aggregate theorem}.
\]

Historical ratio ladders, rejected scalar signs, and diagnostic scans belong in an archive, not in the main implication chain. The existing sanctioned compact certificate must eventually be consolidated with the legacy first-floor check; do this off the critical analytic path.

---

# 8. Final instruction to Codex

Begin by proving R38.1--R38.3. The count-phase lemma and the resulting \(p\le2\) closure are the highest-value low-risk advances and correct the main strategic error in `general-d-r2.md`. Then attack the residual \(p\ge3\) endpoints through the exact \(\chi\)-compensation mechanism. Preserve

\[
\Omega,
\quad
\Xi,
\quad
e_p,
\quad
u=\{\lambda\},
\quad
J,
\quad
W
\]

until the last justified inequality. Do not manufacture a new global scalar merely to obtain a simpler expression. End the round with an explicit Gate A/B/C decision and with the all-dimensional theorem still marked open unless the complete dependency chain has actually been proved and independently audited.
