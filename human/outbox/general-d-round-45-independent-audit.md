# General-dimensional spherical-shell Pólya project
## Round 45 independent audit

**Date:** 20 July 2026  
**Role:** Prompt D independent auditor  
**Verdict:** **STRUCTURAL PASS — FINAL SIGN OPEN**

Round 45 does not prove the endpoint sign. It does prove a new uniform
old-level Bregman theorem with coefficient \(7/48\), uses it in the exact
literal terminal decomposition, combines it without double counting with the
primary Round 38 \(\Omega_-\) bound and one shelf-curvature bound, and removes
all old inverse roots and side fractions from one remaining floor-free
inequality. The exact first unrepaired implication is the proof of lead
equation (R45.18) on the complete exact owner.

This is a genuine Step A6(4) substantive partial, not another numerical
support narrowing. It does not close Gate B, stop Gate B, activate Gate C, or
change any proof-obligation status.

## 1. Audit freeze and provenance

The mandatory repository gate passes.

| item | independently observed |
|---|---|
| working branch | codex/general-d-round-45-support-sign |
| git rev-parse main | 52738525ab0ee360c54f237a5a4fe314caa51e79 |
| audit-time HEAD | 52738525ab0ee360c54f237a5a4fe314caa51e79 |
| Round 44 artifact | 2a0e51ecbb1534eeea94615ab94717fa126c0c5d is an ancestor |
| proof-obligation SHA-256 | a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4 |
| selected obligation | SHELL-general-d-high-floor-first-drop-CST : open |
| Round 44 lead blob | dd115dd6f9d98bae1eed4c28fd959d2183cf013c |
| Round 44 audit blob | b4b09013b89c51ccefa653445be6b53c5d8a09b6 |
| Round 44 comparison | both blobs agree with main; no working-tree change |

The exact Round 45 artifacts audited here were frozen at the following
SHA-256 values.

| artifact | SHA-256 |
|---|---|
| lead note | a93c10ed13fbbc83e995562fd845cf39242e0a8b987442d756d744dfd8a0c2c0 |
| clean-room report | a07f537ca8e29a8cf7d57ecc108bce7d94fdf3d1ca475e638f2c65c546c60a59 |
| adversarial report | 929b56f1af67ff800a69d9d85e2dab947941ad3ab2ba7422713e166f5309b669 |
| Mathematica replay | e8121ef30deb12b947135a1f414532ba4c86c3fd6315543dfccb65cbf9bbfbab |
| lead diagnostic | 613064686b68cff9250f998a64dc5e95d9a2727481a66e4989e04ee4a96bf258 |
| independent search | 66e52bbb4e52aafd633f656723e896659f5b090392ca950b68f85a2d263afaf2 |

The known source conflicts are narrative only and were handled correctly.

1. The next_action prose in state/proof_obligations.yml still describes the
   older Round 37 route. Its statuses remain authoritative; the later audited
   Round 43--44 gate decisions and the Round 45 packet control this round.
2. general-d-strategy_r2.md predates the Gate-A stop. Its methodology and
   no-partition rules remain binding, but its old gate-state narrative is
   superseded.
3. The one-sided label \(B\) and literal endpoint count
   \(B_{\rm lit}=B_0=B-1\) are not identified. The Round 45 artifacts preserve
   that distinction.

No incompatible mathematical versions were combined. The state files,
proof graph, and manuscript were not edited in this audit.

## 2. Exact theorem actually proved

Let

\[
c_0:=\frac{\pi^2}{Kt^3\sin t},\qquad
T_{\rm top}:=
\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},
\]

and let \(\mathcal R_k\) be the exact old-level Bregman area from the literal
Round 44 decomposition. Round 45 proves, for every actual old level
\(1\le k\le B_0\),

\[
\boxed{\mathcal R_k\ge\frac7{48}c_0},\qquad
\boxed{\sum_{k=1}^{B_0}\mathcal R_k\ge\frac{7B_0}{48}c_0}.
\tag{A45.1}
\]

Because the old unit intervals and the literal top interval are disjoint,

\[
\boxed{
\mathcal R_{\rm tan}^0\ge
\frac{7\pi^2B_0}{48Kt^3\sin t}+T_{\rm top}.}
\tag{A45.2}
\]

Combining (A45.2) with the primary, \(u\)-retaining Round 38 bound gives the
root-free aggregate

\[
\boxed{
\Omega_-+\mathcal R_{\rm tan}^0\ge
\frac{\pi^2B_0}{Kt^3\sin t}
\left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)
+T_{\rm top}.}
\tag{A45.3}
\]

This is one universally quantified theorem, not a \(k\)-, \(B_0\)-, count-,
floor-, ratio-, or chamber-indexed family.

Round 45 also makes the exact support use explicit. With

\[
\begin{aligned}
M_{30}:={}&p(E_*-E)\\
&-\left(\Omega_-+B_0\zeta+\frac9{16\beta}-J
+T_{\rm top}+\mathcal C_{\rm curv}\right),
\end{aligned}
\]

the literal ledger rearranges exactly to

\[
\boxed{
\mathscr S=-M_{30}
+(\mathcal R_{\rm tan}^0-T_{\rm top})
+(\mathcal C_p-\mathcal C_{\rm curv}).}
\tag{A45.4}
\]

Consequently the part of S30 satisfying

\[
M_{30}\le\frac{7\pi^2B_0}{48Kt^3\sin t}
\]

is signed, and every hypothetical negative point must satisfy

\[
\boxed{
M_{30}>\frac{7\pi^2B_0}{48Kt^3\sin t}.}
\tag{A45.5}
\]

Using the exact action drop and the primary \(\Omega_-\) bound turns (A45.5)
into the strict reverse of lead equation (R45.18). Equivalently, (R45.18) is
a sufficient condition for \(\mathscr S>0\). Round 45 does **not** prove that
(R45.18) holds on the complete owner.

## 3. Line-by-line audit of the new \(7/48\) theorem

Write

\[
\ell(\theta)=\frac K\pi(\sin\theta-\theta\cos\theta),\qquad
Y(\ell)=K\cos\theta-q.
\]

Direct differentiation gives

\[
\frac{dY}{d\theta}=-K\sin\theta,\qquad
\frac{d\ell}{d\theta}=\frac K\pi\theta\sin\theta,
\]

\[
Y'(\ell)=-\frac\pi\theta,\qquad
\boxed{Y''(\ell)=\frac{\pi^2}{K\sin\theta\,\theta^3}}.
\tag{A45.6}
\]

The exact wall relation and \(u<1/2\) give

\[
W=B_0+\frac34-u>B_0+\frac14>B_0.
\]

Every old integration interval lies in \(0\le\ell\le B_0<W=\ell(t)\).
Thus \(0<\theta<t\) for \(\ell>0\). Moreover

\[
\frac d{d\theta}(\theta^3\sin\theta)
=\theta^2(3\sin\theta+\theta\cos\theta)>0
\]

on \(0<\theta<\pi/2\), so \(Y''(\ell)>c_0\) on every positive old-layer
point.

The \(k=1,\ell=0\) endpoint is valid. As \(\ell\downarrow0\), one has
\(\theta\downarrow0\), \(Y(\ell)\to K-q\),
\(Y'(\ell)=-\pi/\theta\to-\infty\), and
\(Y''(\ell)\to+\infty\). Apply the strong-convexity inequality first on
\(\ell\ge\varepsilon>0\) and then let \(\varepsilon\downarrow0\). Continuity
of \(Y\) and of the tangent/quadratic comparison passes the inequality to
\(\ell=0\); no endpoint area is lost.

For the tangent point \(\ell_k=k-1/4\), strong convexity therefore gives

\[
Y(\ell)-\Lambda_k(\ell)\ge
\frac{c_0}{2}(\ell-\ell_k)^2.
\]

The factor \(2\) in the definition of \(\mathcal R_k\) cancels the factor
\(1/2\), and

\[
\int_{k-1}^{k}(\ell-k+1/4)^2\,d\ell
=\int_{-3/4}^{1/4}s^2\,ds=\frac7{48}.
\]

This proves (A45.1), including \(B_0=1\). The coefficient is unrelated to
the \(9/64\) top coefficient: \(7/48\) comes from the full old unit interval
\([-3/4,1/4]\), whereas \(9/64\) comes from the separate top interval of
length \(3/4\).

The root elimination is also exact. The primary Round 38 payment is

\[
\Omega_-\ge\frac{c_0}{2}
\left(\frac{B_0(B_0+1)}2-B_0u\right).
\]

Adding only the old Bregman payment in (A45.1) gives

\[
\frac{c_0B_0(12B_0+19-24u)}{48}
=c_0B_0\left(\frac W2-\frac{B_0}{4}+\frac1{48}\right),
\]

because \(u=B_0+3/4-W\). The top reserve is then added once through the
disjoint exact decomposition, proving (A45.3).

## 4. Strict implication chain and exact action drop

The exact endpoint identities are

\[
A(x)=f-\frac14+e_p,\qquad
A(q)=B-\frac14-h.
\]

Hence

\[
\boxed{A(x)-A(q)=j+e_p+h.}
\tag{A45.7}
\]

This is an identity on the fixed owner, not transport across a floor. The
Round 42 adjacent-action theorem therefore gives

\[
\Delta>R_1\{A(x)-A(q)\}.
\]

Since \(E=\Delta+2e_p\) and \(e_p\ge0\),

\[
E>R_1\{A(x)-A(q)\}\ge R_1h.
\tag{A45.8}
\]

The count-free implication is consequently sound, with strictness retained:

\[
\mathrm{R45\text{-}CF}\Longrightarrow
\mathrm{S31\ empty}\Longrightarrow
\mathrm{S30\ empty}\Longrightarrow\mathscr S\ge0.
\]

Equality in R45-CF still excludes the strict S31 support because (A45.8) is
strict. S30 is contained in S31 because

\[
\Omega_-+B_0\zeta+\frac9{16\beta}-J
>0+\frac15+\frac98-\frac1{10}=\frac{49}{40}.
\]

The hypotheses of all four inherited strict inequalities are satisfied:
old roots obey \(\theta_k<t\), \(B_0\ge1\), \(q\ge5\), \(p\ge3\), the point is
the common-shelf literal first-drop outer-\(B\) owner, and the fixed parity-
labelled activity inequality is strict.

## 5. Reserve, double-counting, and ownership audit

| item | audit finding |
|---|---|
| \(\Omega_-\) | The exact sum is retained before applying the primary \(u\)-retaining Round 38 bound. Its hypotheses \(\theta_k<t\), \(\eta_k\ge0\), and fixed owner are met. |
| \(B_0\zeta>1/5\) | Used only in the S30-to-S31 comparison. The audited Round 38 finite gap-side endpoint hypotheses hold, with the stronger \(q\ge5\). |
| \(J<1/10\) | Used only where authorized. The audited Round 39 residual hypotheses \(q\ge5\), \(p\ge3\) hold. |
| adjacent action | Used with the exact common-shelf, first-drop, upper-\(\alpha\), outer-\(B\), strict-activity owner and the exact action drop (A45.7). |
| shelf payment | Only \(\mathcal C_p\ge\mathcal C_{\rm curv}\) is added to the terminal aggregate. The hinge bound \(a_p\Delta\) is not also added. |
| old Bregman areas | Taken from the actual unit intervals in the exact \(\mathcal R_{\rm tan}^0\) decomposition. |
| top Bregman reserve | Taken only from \([B_0,v]\), disjoint from every old interval \([k-1,k]\). |
| \(1/(16\beta)\) | Checked as \(L_T^0-L_T^+=\mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0\); never added as a further reserve. |
| \(\Omega_-\) versus Bregman terms | These are respectively the tangent/sample skeleton and its exact convex remainder, so their addition is the banked exact decomposition, not reuse of one area. |
| adjacent action versus \(\mathcal C_p\) | Adjacent action lowers the separate \(pE\) term. It is not reused as a second curvature payment. |

Thus neither \(\mathcal C_p\) nor \(\mathcal R_{\rm tan}^0\) is double-counted.
Equation (A45.4) independently confirms that the S30 support payment is
subtracted and restored exactly once.

The equality and side ownership also pass.

1. At \(A(r+s)+1/4\in\mathbb Z\), the literal ordinary floor is used; no
   continuation across \(E_{f+1}=E_f-2\) occurs.
2. At \(G_K(q)+1/4=B\), the literal strict count is \(B_0=B-1\), while \(B\)
   remains the old-chart one-sided label.
3. \(A(q)+1/4=B-h\in(B-1,B)\), so the shell endpoint count is \(Q=B_0\).
4. At each old inverse wall, one may fix \(\eta_k=1\) literally or
   \(\eta_k\downarrow0\) adversely. The Bregman theorem is geometric and the
   primary \(\Omega_-\) bound uses only \(\eta_k\ge0\), so it holds for every
   fixed componentwise side vector. No term is independently worst-cased.
5. The newest \(y_B=0\) event is represented once by the literal top owner;
   it is not treated as an old inverse collision or supplemented by the
   \(1/(16\beta)\) reconciliation.
6. The proof remains strict at \(e_p=0\). The face \(E=E_*\) belongs to the
   automatic sector, activity equality to the no-mode owner, and S30/R45.18
   equality to the nonnegative side.
7. \(B_0=1\), both parity grids, the dimension-labelled activity constants
   \(3/4\) and \(2\), and the integer/half-integer starting radii are handled.
8. The endpoint is evaluated at \(\mu=q+1\) with the
   \(\alpha\uparrow1^-\) labels. It is never reindexed as a next-chart
   \(\alpha=0\) owner.

No proof step transports across a shelf-floor, inverse-count, outer-\(B\), or
activity jump. The separately re-solved one-sided numerical sequences are
reported only as diagnostics.

## 6. Replay and adversarial audit

I ran the finalized artifacts from the repository root.

~~~text
wolframscript -file computations/general_d_round45_support_sign_replay.wl
python -B computations/general_d_round45_support_sign_diagnostic.py --dps 120
python -B computations/general_d_round45_independent_support_search.py --dps 90
~~~

All three exited successfully. Mathematica printed zero for the derivative,
\(7/48\) moment, aggregate, wall-position, \(9/64\), reconciliation, action-
drop, shelf-weight, and support-slack residuals, and ended with

~~~text
fixtureChecks=True
round45SupportSignReplayOK=True
~~~

The lead diagnostic independently asserts the exact support-slack residual
below \(10^{-90}\), certifies the wall and every owner inequality with
640-bit Arb arithmetic, and reproduces the focused route counterexample

\[
(r,p,m,f,B,j)=(1,6,11,21,19,2),
\]

\[
\mathrm{R45\text{-}CF\ RHS-LHS}
=-0.46516360323925236\ldots<0,\qquad
\mathscr S=31.7934404877065138\ldots>0.
\]

The clean-room report found a distinct half-integer exact owner

\[
(r,p,m,f,B,j)=\left(\frac32,6,7,6,5,1\right),
\]

for which an independent directed replay gives R45-CF right-minus-left
\(-0.19347860690435906\ldots<0\) and
\(\mathscr S=10.0891031525889278\ldots>0\). Both points are outside S30 and
S31. They are count_free_route_counterexample records only.

The full independent run reproduced exactly:

| diagnostic event | count |
|---|---:|
| distinct proposals | 490,551 |
| mandatory-box proposals | 447,640 |
| rebuilt exact owners | 149 |
| \(\mathscr S<0\) | 0 |
| \(M_{30}>0\) | 0 |
| \(M_{31}>0\) | 0 |
| R45-CF reverse | 81 |

Named integer and half-integer route failures received directed full-owner
certificates. The other finite signs are high-precision diagnostics. The
program and report do not claim continuum coverage, a globally directed
maximizer, or a positive certificate.

All mandatory regressions pass.

1. The Round 44 tuple \((1,3,1,2,2,0)\) gives
   \(\mathscr S=2.69456527890035502562933291475\ldots\) and is outside S30
   and S31.
2. The tuple \((1,9,9,4,3,1)\) is rejected solely because
   \(E=0.32800248609041395\ldots>E_*=0.29135192053582955\ldots\).
3. The Round 27 automatic-sector witness retains both negative rejected
   projections while directed replay gives \(E>E_*\) and
   \(\mathscr S=47.1391872600721\ldots>0\).
4. The \(1/(16\beta)\) reconciliation replays to zero.
5. The literal top coefficient reconstructs exactly as \(9/64\).
6. The primary Round 38 \(\Omega_-\) lower bound has positive diagnostic
   slack and is rechecked directionally at every named certificate.
7. The Round 42 adjacent-action residual is positive, including every named
   certificate.

The classification discipline is correct: \(M_{30}>0\), if found, would be
a support-entry witness; R45-CF failure is only a sufficient-route
counterexample; and only directed \(\mathscr S<0\) would trigger Gate B. No
negative \(\mathscr S\) was certified.

## 7. Prompt-D determinations

| question | determination |
|---:|---|
| 1 | The exact proved result is (A45.1)--(A45.5): the \(7/48\) old-level theorem, its literal old-plus-top aggregate, the root-free \(\Omega_-+\mathcal R_{\rm tan}^0\) bound, and the strengthened exact negative-support localization. |
| 2 | **No.** These results reduce the complete sign to (R45.18); they do not prove (R45.18). |
| 3 | **Yes.** The result is one intrinsic, count-uniform shelf-terminal reduction, not an indexed case family. |
| 4 | **Yes.** The hypotheses of \(\Omega_-\), the old Bregman areas, \(B_0\zeta>1/5\), \(J<1/10\), and adjacent action are respected. |
| 5 | **No double counting.** Only one shelf bound is used, and old/top Bregman payments are added through their disjoint exact decomposition. |
| 6 | **Yes.** \(1/(16\beta)\) is used only as owner reconciliation. |
| 7 | **No.** There is no proof transport across any shelf, inverse-count, outer-count, or activity jump. |
| 8 | **Yes.** Strict brackets, one-sided labels, activity ownership, parity grids, and fixed side vectors are correct. |
| 9 | **Yes.** Falsification of R45-CF is restricted to that sufficient route. |
| 10 | **Yes.** Diagnostics, support witnesses, route counterexamples, and directed certificates are classified correctly. |
| 11 | **No.** No directed negative \(\mathscr S\) exists in the Round 45 record. |
| 12 | No obstruction is claimed. The reports do not assert impossibility of all intrinsic proofs. |
| 13 | The first unrepaired logical gap is the complete-owner proof of (R45.18). |
| 14 | The four authoritative statuses listed below remain unchanged. |
| 15 | Gate B **continues under a substantive partial**; it neither closes nor stops. Gate C remains inactive. |
| 16 | The next single obligation is the complete-owner proof of (R45.18), equivalently exclusion of its strict reverse, without count/floor/ratio/chamber partition or a second compact certificate. |

## 8. Step A6 decision, statuses, and next obligation

Step A6(4) is genuinely met for three independent reasons.

1. The monotonicity of \(\theta^3\sin\theta\) proves a new exact theorem, not a
   sampled margin.
2. That theorem removes every old inverse root and every old side fraction
   from the remaining sufficient inequality and analytically signs a
   nontrivial part of S30 through (A45.4)--(A45.5).
3. It combines with one shelf ledger and leaves the single printed continuous
   wall-correlated inequality (R45.18), with no indexed family, floor
   transport, new projected scalar, or second certificate.

Accordingly, Gate B qualifies to continue under the substantive-partial
standard. The packet still requires human adjudication before launching a
new round; this verdict is not an automatic Round 46 instruction.

The authoritative statuses remain exactly

~~~text
SHELL-general-d-high-floor-first-drop-CST : open
SHELL-general-d-branching-backbone        : derived_under_assumptions
SHELL-general-d-weighted-aggregate        : proposed
TARGET-shell-general-d                    : proposed
~~~

The next single obligation is:

\[
\boxed{
\begin{aligned}
\frac{p-dm}{2}\le{}&
pR_1\{A(x)-A(q)\}\\
&+\frac{\pi^2B_0}{Kt^3\sin t}
\left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)\\
&+B_0\zeta+\frac9{16\beta}-J\\
&+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
\left(\frac1{\sqrt{\mu^2-r^2}}
-\frac1{\sqrt{K^2-r^2}}\right)
\end{aligned}}
\]

on the complete exact owner, derived from the exact outer wall, strict
activity, \(p-dm>11/5\), the literal first drop, and the continuous shelf
geometry. A positive search is not a proof of this obligation.
