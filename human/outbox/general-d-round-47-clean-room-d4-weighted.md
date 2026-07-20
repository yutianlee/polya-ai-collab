# Round 47 clean-room derivation: the (d=4) weighted aggregate

**Date:** 2026-07-21  
**Role:** Prompt B clean-room derivation  
**Scope:** (d=4), weighted aggregate only  
**Provisional verdict:** **INCOMPLETE — the structural reduction is exact, but the componentwise sign estimate remains open.**

## 1. Independence, preflight, and authority

I performed this derivation without reading the Round 47 lead report, lead diagnostic/replay, or adversarial report. Before the freeze marker below, the only Round 47 artifact read was the controlling prompt
`human/inbox/general-d-round-47-codex-prompts-and-proof-plan.md`.

The preflight was:

- repository: `yutianlee/polya-ai-collab`;
- required base branch: `main`;
- required base commit: `62119aa918b86ddb4e96d03426f5db7685c381d1`;
- observed working branch: `codex/general-d-round-47-d4-weighted-aggregate`;
- observed `HEAD`: `62119aa918b86ddb4e96d03426f5db7685c381d1`;
- Round 46 audit commit checked by the packet: `a72bc4565d6a29a723545e0a5d38c8e8b1cfb79c`;
- proof-obligations hash expected and observed:
  `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`;
- pre-existing untracked input: the Round 47 prompt only.

The current-state `round_selection` and older pointwise workflow text are stale with respect to the workflow switch made by the Round 46 audit and the Round 47 human prompt. I use the latter two only to select the weighted-aggregate route. I do **not** promote any theorem status. The authoritative statuses therefore remain:

| item | status used here |
|---|---|
| high-floor CST | `open` |
| branching backbone | `derived_under_assumptions` |
| weighted aggregate | `proposed` |
| pointwise assembly | `open` |
| full target | `proposed` |

The mandatory earlier sources used were the simplified analytic strategy, current directives/state/gap register/lemma bank, the relevant branching and master-identity sections of the manuscript, the Round 46 lead/clean-room/adversarial/audit packet, and the audited modules cited in the localization ledger in Section 6. Nothing in this report treats a numerical search or a stale manuscript status paragraph as proof.

## 2. Exact (d=4) target and master identity

Write (A=A_K), extend it by zero for (z\ge K), and put

\[
 \sigma(z):=-A'(z)\ge0,\qquad
 q_a:=\bigl[A(a)+\tfrac14\bigr]_{<},\qquad a\in\mathbb Z_{\ge1}.
\]

Here ([x]_<) is the strict bracket: it is the largest integer strictly less than (x). In particular, if (x=N\in\mathbb Z), then ([x]_< =N-1), not (N).

For (d=4), define

\[
 S_4(z):=\sum_{m+1\le z}(m+1),\qquad
 \Delta_4(z):=\int_0^z S_4(t)\,dt-\frac{z^3}{6},
\]

\[
 D_A(a):=2\int_a^\infty A(z)\,dz
          -q_a-2\sum_{j\ge1}q_{a+j},
\]

and

\[
 B_4(A):=2\int_0^K \sigma(z)\bigl(-\Delta_4(z)\bigr)\,dz.
\]

The direct proxy and Weyl term are

\[
 P_4^{\le}=\sum_{a\ge1}a^2q_a,
 \qquad
 W_4=\int_0^K z^2A(z)\,dz.
\]

Finite summation gives

\[
 \sum_{a\ge1}aD_A(a)
 =2\int_0^K A(z)S_4(z)\,dz-P_4^{\le}.
\]

Since (( -\Delta_4)'=z^2/2-S_4(z)), integration by parts gives

\[
 B_4(A)=W_4-2\int_0^K A(z)S_4(z)\,dz.
\]

Consequently the exact master identity is

\[
 \boxed{W_4-P_4^{\le}
 =B_4(A)+\sum_{a\ge1}aD_A(a).}
\]

Round 47 therefore asks for

\[
 \tag{WT4}
 B_4(A)+\sum_{a\ge1}aD_A(a)\ge0
\]

under the strict activity condition

\[
 K^2>\frac{\pi^2}{(1-\rho)^2}+\frac34.
\]

The equality-inclusive complement belongs to the already proved no-mode module and is not silently folded into the active proof.

## 3. L1--L2: exact primitive and quantitative bonus

### 3.1 Primitive on every unit cell

For (0\le z<1), (S_4(z)=0), hence

\[
 \Delta_4(z)=-\frac{z^3}{6}.
\]

Let (a\ge1) be an integer and write (z=a+x), (0\le x<1). At the integer endpoint,

\[
 \Delta_4(a)=-\frac a6,
\]

and on the cell

\[
 \Delta_4'(a+x)
 =\frac{a(a+1)}2-\frac{(a+x)^2}{2}.
\]

Integration from (x=0) yields the exact polynomial

\[
 \boxed{
 \Delta_4(a+x)
 =-\frac a6+\frac a2x(1-x)-\frac{x^3}{6}.}
\]

Thus, with (H_a(x):=-\Delta_4(a+x)),

\[
 H_a(x)=\frac a6-\frac a2x(1-x)+\frac{x^3}{6}.
\]

Its unique interior minimum is at

\[
 x_a=\sqrt{a(a+1)}-a\in(0,\tfrac12),
\]

and direct substitution gives

\[
 \min_{0\le x\le1}H_a(x)
 =\frac{a(a+1)}{12\bigl(a+\tfrac12+\sqrt{a(a+1)}\bigr)}
 >\frac a{24}.
\]

The last strict inequality follows from

\[
 \sqrt{a(a+1)}<a+\frac32.
\]

This proves the required positive cellwise primitive without a numerical surrogate.

### 3.2 Bonus lower bound

Let

\[
 B_{4,a}:=2\int_a^{a+1}\sigma(z)(-\Delta_4(z))\,dz,
\]

with the integrand zero beyond (K). Then (B_4=\sum_{a\ge0}B_{4,a}). The (a=0) cell is nonnegative, and for every (a\ge1),

\[
 B_{4,a}\ge\frac a{12}\int_a^{a+1}\sigma(z)\,dz
 =\frac a{12}\bigl(A(a)-A(a+1)\bigr).
\]

Therefore

\[
 \boxed{
 B_4(A)\ge
 \frac1{12}\sum_{a\ge1}a\bigl(A(a)-A(a+1)\bigr)
 =\frac1{12}\sum_{1\le j<K}A(j).}
\]

The strict endpoint (j<K) is literal. If (K\in\mathbb Z), then (A(K)=0), so no spurious endpoint contribution is introduced.

## 4. L3--L4: adjacent-tail recurrence and weighted summation

Define

\[
 T_A(a):=q_a+2\sum_{j\ge1}q_{a+j}.
\]

The discrete tail satisfies

\[
 T_A(a)-T_A(a+1)=q_a+q_{a+1}.
\]

It follows directly that

\[
 \boxed{
 D_A(a)-D_A(a+1)=L_a,\qquad
 L_a:=2\int_a^{a+1}A(z)\,dz-q_a-q_{a+1}.}
\]

This equality uses the strict brackets exactly as defined; no ordinary-floor replacement is made at an action wall.

Because (A), (q_a), and hence (D_A(a)) vanish for all sufficiently large (a), telescoping gives

\[
 D_A(a)=\sum_{j\ge a}L_j.
\]

All sums are finite, so reversing them is harmless:

\[
 \boxed{
 \sum_{a\ge1}aD_A(a)
 =\sum_{j\ge1}\frac{j(j+1)}2L_j.}
\]

This is the exact weighted summation-by-parts identity requested in the packet.

For later diagnosis, introduce the strict remainder

\[
 \varepsilon_a:=A(a)+\frac14-q_a\in(0,1].
\]

At an exact action wall (arepsilon_a=1), not (0). Then

\[
 \boxed{
 L_a=T_a^{\rm trap}-\frac12+\varepsilon_a+\varepsilon_{a+1},}
\]

where

\[
 T_a^{\rm trap}
 :=2\int_a^{a+1}A(z)\,dz-A(a)-A(a+1).
\]

On a smooth cell,

\[
 T_a^{\rm trap}
 =-\int_0^1x(1-x)A''(a+x)\,dx,
\]

and an interface cell is handled by splitting the integral at (z=\mu). This formula displays the unresolved correlation: the trapezoidal curvature term and the two strict floor remainders cannot be bounded independently without losing the wall information.

## 5. The two direct routes and why neither closes the sign by itself

### 5.1 Direct layer cake

Let

\[
 Y(t):=\bigl|\{z\ge0:A(z)>t\}\bigr|
\]

be the strict superlevel length. Since (A) is decreasing,

\[
 W_4=\frac13\int_0^{A(0)}Y(t)^3\,dt.
\]

Moreover

\[
 q_a=\#\{k\ge1:k-\tfrac14<A(a)\},
\]

so strict layer exchange gives

\[
 \boxed{
 P_4^{\le}
 =\sum_{k\ge1}\ \sum_{1\le a<Y(k-1/4)}a^2.}
\]

The strict inequality (a<Y(k-1/4)) correctly owns equality at the action wall. This identity is useful, but a level-by-level proof would still require a correlated comparison between the integral of (Y^3) over a level cell and the square staircase sampled at (k-1/4). The inverse action does not have a single useful convexity across the inner and outer regimes. Thus layer cake repackages, rather than removes, the same action-wall/interface problem.

### 5.2 Direct trapezoidal route

Inside the turning point, (A) is concave and (T_a^{\rm trap}\ge0) on a wholly inner cell; outside it, (A) is convex and (T_a^{\rm trap}\le0) on a wholly outer cell. A crossing cell has mixed curvature. Even on a one-sign curvature cell, however,

\[
 L_a=T_a^{\rm trap}-\frac12+\varepsilon_a+\varepsilon_{a+1}
\]

need not inherit that sign. Discarding either remainder is precisely the lossy projection that the audited pointwise program found insufficient. The exact recurrence is retained below, but there is no direct cellwise sign proof here.

## 6. L5: localization of every potentially negative tail

Let

\[
 \mathcal N:=\{a\in\mathbb Z_{\ge1}:a<K,\ D_A(a)<0\}.
\]

The following is a support statement, not a new closure theorem. Applying the already audited modules in their literal scopes gives:

| region or shelf class | authoritative disposition |
|---|---|
| activity equality or below | strict no-mode module; outside the present strict-active branch |
| (a\ge K) | zero extension, so (D_A(a)=0) |
| (a\ge\mu) | outer convex-tail nonnegativity |
| (0<\mu-a<1), together with the (a=\mu) boundary ownership | one-interface certificate; nonnegative |
| turning-zone terminal tail with (G_K(a)\le3/4) | zero-tail module, equality included |
| inner multi-cell, first shelf (f=0) | zero-floor automatic case |
| inner multi-cell, (f=1, p<n) | audited first-floor first-drop exhaustion |
| inner multi-cell, (f=1, p=n) | audited first-floor no-drop/WP2 integration |
| inner multi-cell, (f\ge2, p=n) | audited high-floor no-drop integration |

Thus a negative tail, if one exists, must lie in the active inner multi-cell high-floor first-drop class

\[
 \boxed{a<\mu-1,\qquad f\ge2,\qquad p<n.}
\]

Within that class, the later audited rounds already close the explicitly certified remainder-rich/automatic sectors, the lower-(Q) sector, the activity-excision subcases, the retained-(E) lower shelf, the primary inverse component, and the recorded exact gap/endpoint subfamilies. Therefore

\[
 \mathcal N
 \subseteq
 \{\text{active high-floor first-drop faces not contained in any previously closed sub-sector}\}.
\]

This inclusion deliberately does **not** claim that the named sub-sectors exhaust the high-floor CST. That CST remains open.

Evidence for the ownership statements above is the audited chain including:

- `human/outbox/general-d-round-01.md`;
- `human/outbox/general-d-round-02.md` and
  `general-d-round-02-finite-wall-fraction-certificate.md`;
- `human/outbox/general-d-round-02-shelf-reduction.md`;
- the Round 04/05 first-floor large-ray, finite, small-start, s-cone, and global-exhaustion reports and independent audits;
- `human/outbox/general-d-first-floor-no-drop-wp2-integration-audit.md`;
- `human/outbox/general-d-no-drop-fge2-manuscript-integration-independent-audit.md`;
- the Round 27--37 high-floor reports and independent audits;
- the Round 38--46 reports and their independent audits, with the Round 46 audit controlling the present workflow switch.

## 7. Maximal negative components and an exact charge identity

Let (C=[u,v]\subset\mathbb Z_{\ge1}) be a maximal consecutive component of (mathcal N). Then

\[
 D_A(a)<0\quad(u\le a\le v),\qquad
 D_A(v+1)\ge0,
\]

and, if (u>1), (D_A(u-1)\ge0). In particular,

\[
 L_{u-1}=D_A(u-1)-D_A(u)>0\quad(u>1),
 \qquad
 L_v=D_A(v)-D_A(v+1)<0.
\]

For (a\in[u,v]), the recurrence gives

\[
 D_A(a)=D_A(v+1)+\sum_{j=a}^{v}L_j.
\]

Set

\[
 S_{u,v}:=\sum_{a=u}^{v}a,
 \qquad
 \omega_{u,j}:=\sum_{a=u}^{j}a
 =\frac{j(j+1)-(u-1)u}{2}\ge0.
\]

Then the component charge has the exact right-boundary representation

\[
 \boxed{
 \sum_{a=u}^{v}aD_A(a)
 =S_{u,v}D_A(v+1)+\sum_{j=u}^{v}\omega_{u,j}L_j.}
 \tag{C}
\]

There is no discarded boundary term: (S_{u,v}D_A(v+1)\ge0). This is the natural maximal-component formulation requested in the packet.

For completeness, the equivalent left-boundary representation is

\[
 \sum_{a=u}^{v}aD_A(a)
 =S_{u,v}D_A(u-1)
 -\sum_{j=u-1}^{v-1}\left(\sum_{a=j+1}^{v}a\right)L_j
\]

when (u>1). The positive entrance defect (L_{u-1}) and negative exit defect (L_v) are therefore visible from opposite ends, but neither representation alone controls the weighted interior defects.

## 8. One exact component inequality: derivation, attempted proof, and stopping point

### 8.1 A disjoint intrinsic allocation

Allocate to (C=[u,v]) exactly the bonus cells with the same indices:

\[
 B_C:=\sum_{j=u}^{v}B_{4,j}
 =2\sum_{j=u}^{v}\int_j^{j+1}\sigma(z)(-\Delta_4(z))\,dz.
\]

Distinct maximal negative components receive disjoint bonus cells. Every (D_A(a)\ge0) outside the components and every unallocated bonus cell is retained once and is nonnegative. Consequently the componentwise assertion

\[
 \tag{CI}
 B_C+\sum_{a=u}^{v}aD_A(a)\ge0
\]

for every maximal negative component would be sufficient for (WT4). It is intentionally stronger than the global target; a global proof might permit cross-component compensation.

Using (C), (CI) is exactly

\[
 \boxed{
 2\sum_{j=u}^{v}\int_j^{j+1}\sigma(z)(-\Delta_4(z))\,dz
 +S_{u,v}D_A(v+1)
 +\sum_{j=u}^{v}\omega_{u,j}L_j\ge0.}
 \tag{U}
\]

This is the first unrepaired inequality in the clean-room route.

### 8.2 Exact integration by parts on a bonus cell

On ([j,j+1]), let (H_j(z)=-\Delta_4(z)). Then

\[
 H_j(j)=\frac j6,
 \qquad H_j((j+1)^-)=\frac{j+1}{6},
 \qquad H_j'(z)=\frac{z^2}{2}-\frac{j(j+1)}2.
\]

Therefore

\[
 \boxed{
 B_{4,j}
 =\frac j3A(j)-\frac{j+1}{3}A(j+1)
  +2\int_j^{j+1}A(z)
       \left(\frac{z^2}{2}-\frac{j(j+1)}2\right)dz.}
 \tag{BIP}
\]

Substituting (BIP) and

\[
 L_j=2\int_j^{j+1}A-q_j-q_{j+1}
     =T_j^{\rm trap}-\frac12+\varepsilon_j+\varepsilon_{j+1}
\]

into (U) is exact. It leaves a weighted polynomial kernel in the cell integrals plus endpoint action values and strict floor remainders. The kernel changes sign, and the remainders jump at the same action walls that define the unresolved high-floor faces. Hence neither separate trapezoidal bounds nor the coarse primitive bound preserves enough correlation to sign the result.

The quantitative bonus from Section 3 gives the stronger sufficient condition

\[
 \tag{U'}
 \frac1{12}\sum_{j=u}^{v}j\bigl(A(j)-A(j+1)\bigr)
 +S_{u,v}D_A(v+1)
 +\sum_{j=u}^{v}\omega_{u,j}L_j\ge0.
\]

But (U') is not proved and is stronger than (U), because it replaces the exact bonus by a lower bound. The audited pointwise modules localize where a violation could occur; they do not yet provide a quantitative estimate tying the weighted (L_j)-deficit to the (H_j\)-weighted action drop on the same component.

### 8.3 No-double-counting audit

- The sets of tail indices (C) are disjoint by maximality.
- The allocated bonus-index sets (J_C=C) are therefore disjoint.
- Positive tails outside (mathcal N) remain in the global sum once; no such tail is declared spent twice.
- The term (S_{u,v}D_A(v+1)) in (C) is an algebraic part of the exact representation of the component sum, not an additional copy of the positive tail ((v+1)D_A(v+1)).
- Bonus cells outside (igcup_C C), including the (a=0) cell, remain nonnegative surplus.

Thus the architecture would assemble without overlap if (U) were proved.

### 8.4 Wall, endpoint, and thin-regime audit

- **Activity wall:** equality is owned by the no-mode theorem; this report works only on the strict active side.
- **Action wall:** if (A(a)+1/4=N\in\mathbb Z), then (q_a=N-1) and (arepsilon_a=1). All recurrence and layer-cake formulas above retain this convention.
- **Turning wall:** if (mu\in\mathbb Z), cells meeting (z=\mu) are split there. The action and its first derivative match, while the curvature formula changes. The (a=\mu) tail is owned by the outer/one-interface audited modules.
- **Support wall:** (A(K)=q_K=D_A(K)=0) when (K\in\mathbb Z), and zero extension handles the truncated terminal cell without an endpoint atom.
- **Moderate (K):** all identities are exact immediately above activity; no large-(K) asymptotic is invoked.
- **Thin limit (ho\uparrow1):** activity forces (K) to grow, but each fixed parameter pair still has finite support. No nonuniform limiting interchange is used.

### 8.5 Dependency and loss ledger

| step | exact or lossy? | status |
|---|---|---|
| (d=4) primitive | exact | proved here |
| bonus cell minimum | exact, followed by a one-sided lower bound | proved here |
| adjacent recurrence | exact | proved here |
| weighted summation | exact finite telescoping | proved here |
| layer-cake formula | exact, strict-wall aware | proved here |
| localization to unresolved high-floor first-drop faces | exact use of already audited scope ownership | established, but does not close that sector |
| maximal-component identity (C) | exact | proved here |
| component allocation (J_C=C) | sufficient architecture, stronger than the global theorem | valid if (U) is proved |
| replacement (U) (Rightarrow) (U') | lossy lower bound on the bonus | insufficient at present |
| sign of (U) | no licensed estimate found | **open** |

## 9. Provisional verdict before comparison

The clean-room route verifies L1--L5, produces an exact nonnegative-boundary component identity, and gives a disjoint bonus allocation whose success would imply (WT4). It does **not** prove the sign of the resulting component charge.

Accordingly:

\[
 \boxed{\text{PROVISIONAL VERDICT: INCOMPLETE.}}
\]

The first unrepaired statement is (U), equivalently the componentwise inequality (CI), for every maximal negative component contained in the unresolved active high-floor first-drop sector. Proving (U), weakening it to a globally summable charge, or finding a counterexample to this particular component allocation is the next exact task. No theorem status should be promoted on the basis of this report.

<!-- ROUND47 CLEAN-ROOM PRE-COMPARISON FREEZE END -->

## 10. Freeze record

The SHA-256 of the frozen pre-comparison prefix, defined as every byte from the beginning of this file through the freeze-marker line and its terminating LF, is:

`b5ebd7e67b659acdb703410f38a5da55f2ecb7b5e6131c75439ef23a07c807af`

## 11. Post-comparison section

### 11.1 Authorization and integrity

The parent supplied the following frozen Prompt-A hashes and explicitly authorized comparison:

| Prompt-A artifact | supplied and observed SHA-256 |
|---|---|
| `human/outbox/general-d-round-47-d4-weighted-aggregate.md` | `e717ded2d1c8a9dc38bd590613d6614db61cfa4875eeeef10980bff3ad96a586` |
| `computations/general_d_round47_d4_weighted_diagnostic.py` | `bfdfd0b239401ef3b8bddbb163ce4bb542b18c27c2a2d4127879555dc1336087` |
| `computations/general_d_round47_d4_weighted_replay.wl` | `812cb453b75a33276611c0fb2ddedc93ae772472c5333188a05417548413ca2a` |

All three observed hashes agree exactly with the supplied hashes. I then read those Prompt-A artifacts in full. I did **not** read the Prompt-C report or evaluator. The frozen clean-room prefix above remains byte-for-byte unchanged, with SHA-256

`b5ebd7e67b659acdb703410f38a5da55f2ecb7b5e6131c75439ef23a07c807af`.

### 11.2 Line-by-line agreement map

| lead location | frozen clean-room location | comparison |
|---|---|---|
| Section 0, preflight/conflicts/statuses | Sections 1 and 9 | Exact agreement on the base, branch, proof-obligation hash, stale workflow and manuscript narratives, status discipline, and `INCOMPLETE` verdict. |
| Section 1, $A,q_a,D_a,L_a,P_4^<,W_4$ and (WT4) | Sections 2 and 4 | The definitions and master identity agree exactly. The lead additionally prints $A=G_K-G_\mu$ and the closed moment $W_4=(K^4-\mu^4)/64$. |
| Section 2, (L1.1)--(L1.3) | Section 3.1 | Exact agreement on the cell polynomial, critical point, exact minimum, and strict $a/24$ bound. |
| Section 3, (L2.1)--(L2.4) | Section 3.2 | Exact agreement on the bonus decomposition, zero extension, endpoint $K\in\mathbb N$, and coarse bound. The lead explicitly records the intermediate exact-minimum bound $2M_a[A(a)-A(a+1)]$, which is implicit but not printed in the frozen clean-room text. |
| Section 4, (L3), (L4.1)--(L4.2) | Section 4 | Exact agreement on the strict adjacent recurrence and finite weighted summation. Both retain the lower strict value at action walls. |
| Section 5, coarse support conclusion | Section 6 | Agreement that a negative tail can occur only in the unresolved active high-floor first-drop program. The lead gives a materially sharper and safer formulation; the necessary post-comparison repair is recorded below. |
| Section 6, (C-right), (C-left), (C-sign) | Section 7 | Exact formula-by-formula agreement, including every triangular coefficient and the signs of the entrance and exit increments. |
| Section 8, component allocation and (U) | Section 8.1--8.3 | Both give disjoint sufficient component architectures, but they allocate different resources. They are not the same unproved inequality; see Section 11.4. |
| Section 9, cell-self-charge test | Section 8.2 | Consistent with the clean-room warning that independently signing a cell kernel loses the needed correlation. Prompt A supplies a large-margin numerical negative record, but not a directed certificate. |
| Section 10, wall table | Section 8.4 | Exact agreement on the activity, action, turning, support, terminal-cell, moderate-$K$, and thin-shell assignments. The lead adds the important explicit statement that no-mode is spectral and is not a per-shift $D_a$-sign theorem. |
| Sections 11--13, ledgers | Sections 6 and 8.3--8.5 | Agreement on dependency ownership, one-sided losses, and no-double-counting logic. |
| Section 15, final status | Section 9 | Exact agreement that literal (WT4) is neither proved nor falsified and no obligation status changes. |

The Mathematica replay was rerun after hash verification and returned

```text
ROUND47_D4_SYMBOLIC_REPLAY: PASS
```

for the L1 stationary point/minimum, L3 formal identity, L4 coefficient, and component coefficient. A separate quick rerun of the Python evaluator remained explicitly diagnostic, found no negative literal target in that small rerun, and printed `positive_coverage_certificate: false`.

### 11.3 Hidden assumptions and required repairs

#### Repair 1: proxy notation

The frozen clean-room prefix writes $P_4^{\le}$ in Section 2. The formula there uses the strict bracket and is mathematically the same proxy as Prompt A, but the packet's correct symbol is

\[
 P_4^<=\sum_{a\ge1}a^2q_a.
\]

The clean-room superscript is a notation error only; every formula uses the strict proxy.

#### Repair 2: sharpen and reinterpret L5

The frozen clean-room L5 table compresses the shelf notation and therefore hides four ownership details printed correctly by Prompt A:

1. The shelf profile is the ordinary-floor profile
   $F(k)=\lfloor A(k)+1/4\rfloor$, while $q_k=[A(k)+1/4]_<$ remains strict. At an integral action wall the ordinary shelf remainder is $0$, whereas the strict remainder in Section 4 is $1$.
2. Integer inner starts share the terminal $\bar q=\lfloor\mu\rfloor$, with
   $n_a=\bar q-a$ and $D_{\bar q}\ge0$.
3. The empty first shelf $p_a=0<n_a$ is already positive. Hence the sharp residual has
   \[
   f_a\ge2,\qquad 1\le p_a<n_a,\qquad m_a=n_a-p_a\ge1,
   \]
   not merely the broader frozen condition $f\ge2,p<n$.
4. The later endpoint lists are **transported owner-images**. A negative starting tail need not literally lie on one of those endpoint faces. The frozen phrase “faces not contained in a closed sub-sector” must therefore be read as localization to the unresolved owner-image, not literal point membership.

Prompt A further retains the audited remainder-rich constraints

\[
 p_a>d_\rho m_a,
 \qquad
 0\le E<\frac{p_a-d_\rho m_a}{2p_a}<\frac12.
\]

These refinements repair the clean-room support table. They strengthen L5 and do not alter any earlier exact identity.

#### Repair 3: status of the cell-self-charge record

Prompt A calls

\[
 \mathcal B_{4,a}+\frac{a(a+1)}2L_a\ge0
\]

false and prints a large negative numerical value at

$\rho=9/10,K=40,a=29$. The frozen lead Python artifact uses high-precision `mpmath`, reports the probe as
`sufficient_route_counterexample_if_directed_certified`, and explicitly says its wall distances are not directed certificates. No rational/Arb enclosure accompanies Prompt A.

Therefore Prompt A alone rigorously establishes a strong diagnostic rejection, not a certified counterexample. The phrases “it is false” and “rejection ... proved” should be downgraded to “numerically falsified with a large margin, pending directed certification,” unless a separate directed artifact supplies that certification. This qualification does not affect L1--L5, the component identities, or the `INCOMPLETE` verdict.

### 11.4 Different component allocations: no contradiction

The clean-room sufficient charge uses

\[
 J_C^{\rm clean}=\{u,\ldots,v\},\qquad P_C^{\rm clean}=\varnothing,
\]

so its unproved inequality is

\[
 \sum_{a=u}^v aD_a+\sum_{j=u}^v\mathcal B_{4,j}\ge0.
 \tag{U-clean}
\]

Prompt A instead uses

\[
 J_C^{\rm lead}=\{u-1,u,\ldots,v\}\cap\{0\le j<K\},
 \qquad
 P_C^{\rm lead}=\{v+1\}\cap\{b<K\},
\]

and asks for

\[
 \sum_{a=u}^v aD_a
 +\sum_{j\in J_C^{\rm lead}}\mathcal B_{4,j}
 +\mathbf1_{v+1<K}(v+1)D_{v+1}\ge0.
 \tag{U-lead}
\]

Because the extra lead terms are nonnegative, (U-clean) is stronger and would imply (U-lead). Prompt A's allocation is preferable as the next obligation because it uses more of the globally available disjoint resource and is consequently easier to prove. Its $J_C$ sets are disjoint between components, its $P_C$ sets are disjoint, and a tail term and a bonus cell carrying the same integer label are distinct terms of the master identity. There is no contradiction and no double counting.

The algebraic term $S_{u,v}D_{v+1}$ inside (C-right) is part of the exact representation of the negative component; it is not a second external copy of the positive tail added by $P_C^{\rm lead}$.

### 11.5 Stronger or additional lemmas on each side

Prompt A contains two substantive advances absent from the frozen clean-room prefix:

1. the sharpened L5 common-terminal/shelf owner theorem described above;
2. the localized deficit
   \[
   D_a\ge-\Xi_a,
   \qquad
   \Xi_a=\left[
      \frac{p-d_\rho m}{2}
      -2\int_0^p t\sigma(a+t)\,dt
      -D_{\bar q}
   \right]_+,
   \]
   supported only on the hard L5 sector.

The latter keeps the action-drop density and common terminal reserve correlated. Its global comparison (X.5) is sufficient, not equivalent, and remains open.

The clean-room prefix contains three exact tools absent from Prompt A:

1. the strict-remainder/trapezoid identity
   \[
   L_a=T_a^{\rm trap}-\frac12+\varepsilon_a+\varepsilon_{a+1},
   \qquad \varepsilon_a\in(0,1];
   \]
2. the strict layer-cake representation
   \[
   P_4^<=\sum_{k\ge1}\sum_{1\le a<Y(k-1/4)}a^2;
   \]
3. the exact bonus integration-by-parts formula (BIP)
   \[
   \mathcal B_{4,j}
   =\frac j3A(j)-\frac{j+1}{3}A(j+1)
   +2\int_j^{j+1}A(z)
      \left(\frac{z^2}{2}-\frac{j(j+1)}2\right)dz.
   \]

These formulas are consistent with Prompt A and may be useful in a future attempt at (U-lead), but none currently supplies its sign. The clean-room's leaner allocation is also a stronger sufficient proposal, not a proved stronger theorem.

### 11.6 Correlations that must not be lost

The two derivations independently identify the same obstruction. Any continuation must retain together:

- the exact polynomial $-\Delta_4$, rather than only its $a/24$ minimum;
- the strict floor remainders at both endpoints of each $L_a$;
- the maximal ordinary-floor shelf and literal first drop;
- the common terminal reserve $D_{\bar q}$;
- the action-drop density used simultaneously by the curvature payment and branching bonus;
- the right-boundary value and neighboring positive-tail charge of each maximal negative component.

The frozen clean-room inequality (U') loses the first correlation by replacing the exact bonus with its coarse action moment. The lead's cell-self-charge probe loses component and terminal correlations. Independently worst-casing these terms yields another unsigned projection and is not a licensed continuation.

### 11.7 Contradiction audit and final clean-room conclusion

There is no contradiction between the exact Prompt-A statements and the frozen clean-room derivation. The differences are:

- one notation repair ($P_4^{\le}\to P_4^<$);
- a necessary sharpening and owner-image interpretation of clean-room L5;
- a more generous, and therefore preferable, lead component allocation;
- the new lead localized-deficit lemma;
- the exact clean-room layer-cake, trapezoid, and bonus integration-by-parts identities;
- an evidence-classification repair for the non-directed cell-self-charge probe.

The final clean-room verdict remains

\[
 \boxed{\text{INCOMPLETE — SUBSTANTIVE AGGREGATE REDUCTION.}}
\]

Literal (WT4) has not been proved or falsified on the complete active domain. No mathematical status changes. The next single analytic obligation should be (U-lead), using the correlated shelf/action-drop data; the alternative global obligation is the lead's (X.5). No return to pointwise Gate B is justified by these artifacts.

This post-comparison pass modified only this clean-room report and did not alter its frozen prefix.
