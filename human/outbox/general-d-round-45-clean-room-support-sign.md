# General-dimensional spherical-shell Pólya project
## Round 45B: clean-room support-sign attempt

**Date:** 20 July 2026  
**Role:** independent analytic review under Prompt B  
**Pre-comparison verdict:** **STRUCTURAL PASS — FINAL SIGN OPEN**  
**Final verdict:** pending the post-freeze comparison required by Prompt B

## 1. Frozen boundary, provenance, and exact owner

Sections 1--5 of this report were completed without reading the lead Round 45
note, its replay, its diagnostic, or the adversarial Round 45 report.  Before
the freeze I read only the Round 45 prompt packet and the files allowed by
Prompt B.

The repository checks required by the packet passed:

| item | verified value |
|---|---|
| `git rev-parse main` | `52738525ab0ee360c54f237a5a4fe314caa51e79` |
| working branch | `codex/general-d-round-45-support-sign` |
| Round 44 artifact in `main` | `2a0e51ecbb1534eeea94615ab94717fa126c0c5d` |
| SHA-256 of `state/proof_obligations.yml` | `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4` |
| selected obligation | `SHELL-general-d-high-floor-first-drop-CST : open` |
| Round 44 lead and audit | present and unchanged in the working tree |

The status boundary is unchanged:

```text
SHELL-general-d-high-floor-first-drop-CST : open
SHELL-general-d-branching-backbone        : derived_under_assumptions
SHELL-general-d-weighted-aggregate        : proposed
TARGET-shell-general-d                    : proposed
```

There are two narrative conflicts, neither affecting an identity below.

1. The `next_action` prose in the proof graph still points to the Round 37
   selected projection.  The later audited Round 43 result stops Gate A, and
   the audited Round 44 result continues Gate B on its localized support.
   The statuses in the proof graph remain authoritative; the later audited
   workflow controls this round.
2. `general-d-strategy_r2.md` describes Gate A as live because it predates
   Rounds 43--44.  Its methodology and no-partition rules remain binding, but
   its gate state is superseded by those audited rounds and the direct Round
   45 packet.

The clean-room calculation uses the packet's owner

\[
x=r+p,\quad q=x+m,\quad \mu=q+1,\quad K=\mu\sec t,
\quad 0<t<\frac\pi2,
\]

\[
d=1-\frac{2t}{\pi},\qquad
\zeta=\frac\pi{2t}-1,
\]

\[
G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,
\qquad A=G_K-G_\mu,
\]

with

\[
G_K(q)=B_0+\frac34,\quad B=B_0+1,\quad
0<h<u<\beta<\frac12,
\]

\[
h=G_\mu(q),\quad u=G_K(q)-G_K(\mu),\quad
\beta=\frac1\pi\arccos\frac qK.
\]

The shelf variables are

\[
f=B+j,\quad
e_0=A(r)+\frac14-f,\quad e_p=A(x)+\frac14-f,
\]

\[
E=e_0+e_p,\quad \Delta=e_0-e_p,\quad
E_*=\frac{p-dm}{2p}.
\]

All uses below retain the complete owner: the common literal first shelf and
literal first drop, \(j\ge0\), \(p\ge3\), \(m\ge1\), \(q\ge5\),
\(p-dm>11/5\), \(0\le E<E_*<1/2\), the appropriate parity grid, strict
dimension-labelled activity, and one fixed old-inverse side vector.

## 2. The implication chain, with all strict inequalities

Put

\[
T_{\rm top}:=
\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},
\]

\[
C_{\rm curv}:=
\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}-
\frac1{\sqrt{K^2-r^2}}
\right),
\]

and

\[
C_0:=\frac{49}{40}+T_{\rm top}+C_{\rm curv}.
\tag{2.1}
\]

The Round 42 adjacent-action input, on this exact common-shelf outer-wall
owner, is

\[
\Delta>R_1(j+e_p+h),\qquad
R_1=\frac{U_r-U_x}{U_x-U_q}>0,
\quad U_z=\sqrt{\mu^2-z^2}.
\tag{2.2}
\]

It follows, without deleting \(e_p\), that

\[
E=\Delta+2e_p
>R_1(j+e_p+h)+2e_p
\ge R_1h.
\tag{2.3}
\]

The first inequality is strict even when \(j=e_p=0\).  Hence

\[
p(E_*-E)
<\frac{p-dm}{2}-pR_1h.
\tag{2.4}
\]

If (R45-CF) holds, its rearrangement and (2.4) give

\[
p(E_*-E)<C_0.
\tag{2.5}
\]

Thus the strict support condition (R45-S31), which requires
\(p(E_*-E)>C_0\), is empty.  Equality in (R45-CF) is harmless because
(2.4) remains strict.

Next, the exact difference between the right sides of (R45-S30) and
(R45-S31) is

\[
\Omega_-
+\left(B_0\zeta-\frac15\right)
+\left(\frac9{16\beta}-\frac98\right)
+\left(\frac1{10}-J\right)>0.
\tag{2.6}
\]

Here the four inputs are respectively
\(\Omega_->0\), \(B_0\zeta>1/5\), \(\beta<1/2\), and \(J<1/10\).
Therefore every (R45-S30) support point is an (R45-S31) support point.

Finally, the literal exact ledger

\[
\mathscr S=
\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p-p(E_*-E)
\tag{2.7}
\]

together with
\(\mathcal R_{\rm tan}^0\ge T_{\rm top}\) and
\(\mathcal C_p\ge C_{\rm curv}\) proves

\[
\mathscr S<0\Longrightarrow\text{(R45-S30)}.
\tag{2.8}
\]

Combining (2.3)--(2.8) proves the requested chain

\[
\boxed{
\text{(R45-CF)}
\Longrightarrow
\text{(R45-S31) empty}
\Longrightarrow
\text{(R45-S30) empty}
\Longrightarrow
\mathscr S\ge0.}
\]

The equality boundary of either support condition belongs to the
nonnegative side: negativity implies a *strict* support inequality.

## 3. Independent falsification of (R45-CF)

(R45-CF) is false on the complete exact owner.  The following is a
counterexample to that sufficient route only:

\[
(r,p,m,B_0,B,f,j)=
\left(\frac32,6,7,4,5,6,1\right),
\quad q=\frac{29}{2},\quad \mu=\frac{31}{2}.
\tag{3.1}
\]

I solved the exact outer wall

\[
F(t):=G_{(31/2)\sec t}(29/2)-\frac{19}{4}=0
\tag{3.2}
\]

with 512-bit Arb balls.  The rational decimal interval obtained by taking

```text
t_c = 1.106515218269151524757444637431522087714546732099264172224487517610659
I_t = [t_c-10^-69,t_c+10^-69]
```

has directed endpoint signs

```text
F(t_c-10^-69) < -2.19e-68,
F(t_c+10^-69) >  1.79e-68.
```

The root is unique because

\[
\partial_aG_a(z)=\frac{\sqrt{a^2-z^2}}{\pi a}>0,
\qquad \frac d{dt}(\mu\sec t)>0.
\]

Evaluation on the whole root interval gives, with ample directed clearance,

\[
\begin{aligned}
K&\in(34.61520317056674,34.61520317056676),\\
d&\in(0.29557053362422816,0.29557053362422819),\\
h&\in(0.07647533910766094,0.07647533910766096),\\
u&\in(0.3573299294651981,0.3573299294651983),\\
\beta&\in(0.3624189066362379,0.3624189066362381),\\
R_1&\in(0.2303064932827068,0.2303064932827070).
\end{aligned}
\tag{3.3}
\]

The literal shelf checks are

\[
\begin{aligned}
e_0&\in(0.3217836725654767,0.3217836725654769),\\
e_p&\in(0.0044784897288849,0.0044784897288851),\\
A(x+1)+\tfrac14-(f-1)
&\in(0.9060448572124589,0.9060448572124592).
\end{aligned}
\tag{3.4}
\]

Thus the first two samples have literal floor \(f=6\), the next sample has
literal floor \(5\), and the first drop is genuine.  Moreover

\[
E\in(0.3262621622943616,0.3262621622943619),
\]

\[
E_*\in(0.3275838553858668,0.3275838553858670),
\tag{3.5}
\]

\[
p-dm-\frac{11}{5}>1.7310,
\]

and the exact \(D=5\) activity margin is greater than \(1163\).  Hence
(3.1) is an exact half-integer-grid owner, not a relaxed or rejected point.

For this owner, directed evaluation gives

\[
\frac{p-dm}{2}
\in(1.96550313231520,1.96550313231521),
\]

whereas the complete right side of (R45-CF) satisfies

\[
pR_1h+\frac{49}{40}+T_{\rm top}+C_{\rm curv}
\in(1.77202452541084,1.77202452541085).
\]

Therefore

\[
\boxed{
\frac{p-dm}{2}-
\left(pR_1h+\frac{49}{40}+T_{\rm top}+C_{\rm curv}\right)
>0.19347860690435.}
\tag{3.6}
\]

As a classification check, I also evaluated the unprojected target directly.
All 20 nonzero terminal strict brackets were certified, with minimum distance
from an integer wall greater than \(0.0141\).  The exact antiderivative and
strict sum give

\[
D_A(q)>9.65448,\qquad \mathcal C_p>0.44254,
\qquad \boxed{\mathscr S>10.08910}.
\tag{3.7}
\]

Also \(p(E_*-E)<0.00794\), so this point is outside both Round 44 support
conditions.  It is therefore a
`count_free_route_counterexample`, not a support-entry witness and not a
Gate-B counterexample.

## 4. An independent exact-support aggregate

Because (R45-CF) is false, retain the old inverse geometry.  Let

\[
Y(\ell)=|\{s\ge0:G_K(q+s)>\ell\}|,
\qquad \ell_k=k-\frac14,
\]

and let \(\Lambda_k\) be the supporting tangent at \(\ell_k\).  For
\(1\le k\le B_0\), put

\[
\mathcal R_k=2\int_{k-1}^{k}(Y-\Lambda_k)\,d\ell.
\]

Writing \(z=q+Y(\ell)=K\cos\theta\), direct inverse differentiation gives

\[
Y''(\ell)=\frac{\pi^2}{K\sin\theta\,\theta^3}.
\tag{4.1}
\]

The exact wall relation gives

\[
W=G_K(\mu)=B_0+\frac34-u>B_0+\frac14.
\tag{4.2}
\]

For every old unit layer, \(\ell\le k\le B_0<W\).  Since \(G_K\) is
decreasing, its inverse lies beyond \(\mu=K\cos t\), hence
\(0<\theta<t\).  The function \(\sin\theta\,\theta^3\) is strictly
increasing on \((0,\pi/2)\).  Consequently, on every old unit layer,

\[
Y''(\ell)>
c_t:=\frac{\pi^2}{K\sin t\,t^3}.
\tag{4.3}
\]

Strong convexity relative to the tangent at \(\ell_k\) now yields

\[
Y(\ell)-\Lambda_k(\ell)
\ge\frac{c_t}{2}(\ell-\ell_k)^2.
\]

Because \([k-1,k]-\ell_k=[-3/4,1/4]\),

\[
\boxed{
\mathcal R_k\ge
c_t\int_{-3/4}^{1/4}s^2\,ds
=\frac7{48}\,c_t.}
\tag{4.4}
\]

This coefficient is obtained from the whole asymmetric old unit layer; it
is not the \(9/64\) coefficient from the separate top interval.  Summing
(4.4) inside the exact literal decomposition gives the new aggregate

\[
\boxed{
\mathcal R_{\rm tan}^0\ge
\frac{7\pi^2B_0}{48K t^3\sin t}
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}.}
\tag{4.5}
\]

Therefore every hypothetical negative point must satisfy the strict,
strictly stronger exact-\(\Omega_-\) support condition

\[
\boxed{
\begin{aligned}
p(E_*-E)>{}&
\Omega_-+B_0\zeta+\frac9{16\beta}-J\\
&+\frac{7\pi^2B_0}{48K t^3\sin t}
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}-
\frac1{\sqrt{K^2-r^2}}
\right).
\end{aligned}}
\tag{4.6}
\]

No old level is split off or identified: (4.5) aggregates the actual finite
sum in one formula.  It remains valid for either fixed literal/adverse old
inverse side vector because \(Y\), its tangents, and its Bregman areas are
geometric; the side vector changes only the corresponding \(2\eta_k\) in
\(\Omega_-\).

If a root-free corollary is wanted only at the last line, the primary Round
38 estimate

\[
\Omega_-\ge
\frac{\pi^2}{2Kt^3\sin t}
\left(\frac{B_0(B_0+1)}2-B_0u\right)
\tag{4.7}
\]

combines with (4.5) to give

\[
\boxed{
\Omega_-+\mathcal R_{\rm tan}^0\ge
\frac{\pi^2B_0(12B_0+19-24u)}
     {48Kt^3\sin t}
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}.}
\tag{4.8}
\]

Equation (4.6), rather than (4.8), is the primary support statement because
it retains \(\Omega_-\) term by term.

Combining (2.3) with (4.6) shows that support emptiness would follow from
the one wall-coupled terminal inequality

\[
\boxed{
\begin{aligned}
\frac{p-dm}{2}\le{}&
p\{R_1(j+e_p+h)+2e_p\}
+\Omega_-+B_0\zeta+\frac9{16\beta}-J\\
&+\frac{7\pi^2B_0}{48Kt^3\sin t}
+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
&+\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}-
\frac1{\sqrt{K^2-r^2}}
\right).
\end{aligned}}
\tag{4.9}
\]

This displayed inequality is only the terminal consequence of the exact
support argument; it is not a renamed proof target or a new certificate.

## 5. Frozen audit: double counting, equality faces, and first failure

### 5.1 Double-counting ledger

| payment | use in this report | audit conclusion |
|---|---|---|
| shelf hinge \(a_p\Delta\) | not used in a support sum | never added to \(C_{\rm curv}\) |
| shelf curvature \(C_{\rm curv}\) | used once as a lower bound for \(\mathcal C_p\) | valid alternative shelf ledger |
| adjacent action | used only in the exact \(E=\Delta+2e_p\) term | not reused as a second lower bound for \(\mathcal C_p\) |
| old Bregman areas | summed through (4.4) over \([k-1,k]\) | disjoint from the top interval |
| top Bregman reserve | used on \([B_0,v]\) only | may be added to the old areas through the exact decomposition |
| \(\Omega_-\) | tangent/sample ledger retained term by term in (4.6) | disjoint from all Bregman remainders |
| \(1/(16\beta)\) | not added anywhere | only reconciles the gap-side and literal ledgers |
| \(9/(16\beta)\) | literal top-tangent payment | counted exactly once |

### 5.2 Equality and ownership faces

| face | owner used here |
|---|---|
| \(A(r+s)+1/4\in\mathbb Z\) | literal ordinary floor; fractional remainder is zero; no transport across the jump |
| \(G_K(q)+1/4=B\in\mathbb Z\) | literal ball count is \(B_0=B-1\); \(B\) remains only the old-chart one-sided label |
| \(A(q)+1/4\in(B-1,B)\) | literal shell count is \(Q=B_0\) |
| old inverse wall | choose \(\eta_k=1\) literally or \(\eta_k\downarrow0\) adversely and keep the full side vector fixed; (4.4) is geometric on both sides |
| newest \(y_B=0\) | outer-action jump, counted once; never treated as an old inverse wall |
| \(e_p=0\) | (2.3) stays strict because (2.2) is strict |
| \(E=E_*\) | automatic-sector owner; excluded from the live strict hard owner |
| \(B_0=1\) | (4.4)--(4.8) contain exactly one old layer and remain valid |
| integer grid | \(r\ge1\); exact even-dimensional activity label retained |
| half-integer grid | \(r\ge3/2\); exact odd-dimensional activity label retained |
| activity equality | no-mode owner, not the active Gate-B owner |
| (R45-CF) equality | closes the support because (2.4) remains strict |
| support equality | nonnegative side, because (2.8) is a strict necessary condition for negativity |
| \(\alpha\uparrow1^-\) | evaluate \(\mu=q+1\) but retain old-chart one-sided gap labels; do not reindex as literal \(\alpha=0\) |
| gap-side/literal terminal formulas | use the literal ledger throughout Sections 2 and 4; do not add their \(1/(16\beta)\) difference |

### 5.3 Exact first unrepaired gap

The count-free route fails at the certified owner (3.1).  The old-level
aggregate (4.5) is proved, removes the identities of all old levels, and
leaves the single intrinsic inequality (4.9).  The first unrepaired analytic
step is now exactly

\[
\text{complete exact owner and exact outer wall}
\quad\Longrightarrow\quad (4.9).
\tag{5.1}
\]

I do not have a uniform proof of (5.1).  In particular, a fixed-chart
derivative cannot be transported through the shelf-floor or outer-count
sawtooth, and this report does not replace that discontinuity by a forbidden
\(B_0\)-, \(j\)-, \(f\)-, ratio-, or chamber-indexed family.  Nor does it
claim that every possible intrinsic proof is obstructed.

The provisional clean-room verdict is therefore

```text
STRUCTURAL PASS — FINAL SIGN OPEN
```

under the substantive-partial clause: (4.4)--(4.8) prove one exact
monotonicity/aggregate reduction and collapse the complete old-level
Bregman sum to one printed inequality.  They do not prove \(\mathscr S\ge0\),
close the endpoint, close Gate B, or authorize Gate C.

---

## FROZEN PRE-COMPARISON BOUNDARY

Everything above this boundary was frozen before reading any lead Round 45
artifact or adversarial Round 45 output.  Post-freeze comparison material,
including every discrepancy with the lead note, must be appended below and
must not revise Sections 1--5.

## 6. Post-freeze comparison with the lead Round 45 note

Only after the boundary above was written did I read
`human/outbox/general-d-round-45-localized-support-sign.md`. I also reran
the lead Mathematica replay after making the analytic comparison. It returned
zero for the symbolic residuals used in the new theorem and ended with

```text
fixtureChecks=True
round45SupportSignReplayOK=True
```

The replay emitted non-load-bearing `FindRoot::precw` warnings while
producing some numerical inverse-root fixture rows. They do not affect the
exact symbolic identities or either independent proof of the aggregate
coefficient.

### 6.1 Agreements

| issue | comparison result |
|---|---|
| strict implication chain | Exact agreement. Both proofs use the strict adjacent-action inequality even at equality in (R45-CF), then use the strict \(49/40\) comparison to place S30 inside S31. |
| status of (R45-CF) | Exact agreement: it is false on complete directed exact owners and is only a `count_free_route_counterexample`. |
| old inverse curvature | Exact agreement on \(Y''(\ell)=\pi^2/(K\sin\theta\,\theta^3)\) and on its uniform lower bound \(\pi^2/(Kt^3\sin t)\). |
| asymmetric unit-layer moment | Exact agreement on \(\int_{-3/4}^{1/4}s^2\,ds=7/48\), hence on \(\mathcal R_k\ge7\pi^2/(48Kt^3\sin t)\). |
| summed old-level theorem | Exact agreement on (4.5), including the disjoint \(9/64\) top reserve. |
| root-free aggregate | The lead's \(W\)-form and the frozen report's \(u\)-form are identical because \(W=B_0+3/4-u\): \(W/2-B_0/4+1/48=(12B_0+19-24u)/48\). |
| double counting | Exact agreement. Neither proof adds the hinge and elementary curvature shelf bounds; old and top Bregman intervals are disjoint; \(\Omega_-\) is a tangent/sample ledger; and \(1/(16\beta)\) is reconciliation only. |
| wall ownership | Exact agreement on the literal \(B_0=B-1\) count, one-sided \(B\) label, newest \(y_B=0\) charge, support equality, activity equality, parity grids, and upper-alpha endpoint. |
| first unrepaired mathematical issue | Both reports leave one exact wall-correlated inequality and prove no full endpoint sign, negative \(\mathscr S\), or Gate-B obstruction. |

### 6.2 Lead strengthening relative to the frozen report

The lead makes one useful additional deletion after the exact-support
aggregate. From

\[
A(x)-A(q)=j+e_p+h
\]

and adjacent action it keeps

\[
E>R_1\{A(x)-A(q)\},
\]

whereas frozen (4.9) kept the sharper but floor-labelled quantity

\[
E>R_1\{A(x)-A(q)\}+2e_p.
\]

The lead then applies the primary \(u\)-retaining lower bound to
\(\Omega_-\). These two nonnegative deletions make the lead's remaining
inequality weaker numerically but remove \(j\), \(e_p\), every old inverse
root, and every side fraction. The result, lead equation (R45.18), is one
continuous floor-free wall inequality and is therefore the cleaner terminal
statement for the joint Round 45 outcome. It is a valid consequence of the
same exact ledger and introduces no new proof target.

The frozen primary support statement (4.6) remains useful as a stronger
exact-\(\Omega_-\) localization; the lead's (R45.18) is the better
formulation for the Step A6 reduction. There is no logical conflict between
them.

### 6.3 Discrepancies and repairs

1. **The \(\ell=0\) endpoint.** Frozen Section 4 writes
   \(0<\theta<t\) on every old unit layer. At the left endpoint of the
   \(k=1\) layer, \(\theta=0\). The lead supplies the needed precise repair:
   prove the curvature inequality for \(\ell>0\) and pass to
   \(\ell\downarrow0\); \(Y''\) diverges there, so the integrated lower bound
   loses nothing. This is a minor endpoint wording repair, not a change to
   (4.4) or its coefficient.
2. **Falsifying witness.** The lead uses the integer-grid owner
   \((r,p,m,f,B,j)=(1,6,11,21,19,2)\), with R45-CF right-minus-left
   \(-0.4651636032\ldots\) and \(\mathscr S=31.79344\ldots>0\). The frozen
   report independently uses the half-integer owner (3.1), with strict reverse
   \(0.1934786069\ldots\) and \(\mathscr S>10.08910\). The distinct witnesses
   corroborate falsity; neither is a support entry.
3. **Old-wall side convention.** The lead fixes the adverse side at an old
   collision and audits the literal alternative. The frozen report proves the
   Bregman aggregate for an arbitrary but fixed literal/adverse vector. These
   scopes agree because the geometric Bregman areas do not depend on
   \(\eta_k\), while the literal vector only increases the retained
   \(2\eta_k\) payment.
4. **Presentation-only defect in the comparison snapshot.** The first frozen
   lead snapshot had lost many inline TeX delimiters and contained a literal
   carriage-return byte in the intended string `B_{\rm lit}`. This was
   reported to the lead for a mechanical repair. It does not change a
   mathematical formula or verdict.
5. **Numerical replay warning.** The lead replay's inverse-root fixture uses
   a lower-precision coefficient inside a 100-digit `FindRoot`, producing
   `FindRoot::precw` warnings. All exact derivative, moment, aggregate,
   reconciliation, and loss residuals nevertheless return zero. The
   clean-room proof and directed witness are independent of those fixture
   roots, so this is not load-bearing.

No mathematical discrepancy was found in the implication chain, the
\(7/48\) theorem, the combined aggregate, the payment ledger, or the claimed
scope of the result.

### 6.4 Final clean-room verdict and Step A6 classification

The lead result meets the substantive-partial standard in Step A6(4):

1. it proves the exact inverse-curvature monotonicity and the count-uniform
   old-level theorem;
2. it eliminates the complete old-root/old-side vector from the remaining
   sufficient inequality;
3. it combines that theorem with one, and only one, shelf-curvature ledger;
   and
4. it leaves the single printed, continuous, floor-free inequality
   (R45.18), with a plausible exact-wall closure route.

It does not prove (R45.18), \(\mathscr S\ge0\), the endpoint, high-floor
CST, or the all-dimensional theorem. It supplies no negative-\(\mathscr S\)
certificate and proves no forbidden-wall obstruction. Gate B therefore
neither closes nor stops; Gate C is not activated by this result, and any
further Gate-B round requires the independent audit and human adjudication
specified in the packet.

The final clean-room verdict, superseding the pending header above, is

```text
STRUCTURAL PASS — FINAL SIGN OPEN
```

The exact first unrepaired gap for the joint Round 45 record is the proof of
lead equation (R45.18) on the complete exact owner, without floor, count,
ratio, or chamber casework. All four authoritative statuses in Section 1
remain unchanged.

### 6.5 Post-comparison mechanical repair verification

The two presentation-only observations in items 4--5 of Section 6.3 have now
been repaired in the lead artifacts.

1. The lead note has balanced inline-TeX delimiters (108 opening and 108
   closing delimiters) and no control bytes other than ordinary line endings.
   In particular, the intended \(B_{\rm lit}\) notation is no longer split by
   a carriage return.
2. The inverse-root fixture now uses a precision consistent with its
   FindRoot working precision. A fresh Mathematica run emitted zero warning
   lines and again ended with fixtureChecks=True and
   round45SupportSignReplayOK=True.

These are mechanical repairs only. They do not alter the frozen analysis,
the mathematical comparison, the first unrepaired inequality, or the final
**STRUCTURAL PASS — FINAL SIGN OPEN** verdict.
