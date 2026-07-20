# General dimension, Round 47: exact (d=4) weighted aggregate

Date: 21 July 2026  
Role: Prompt A, lead analytic pass  
Verdict: **INCOMPLETE — SUBSTANTIVE AGGREGATE REDUCTION**

The literal target was not proved and was not falsified.  This round proves
the exact launch lemmas L1--L4, an intrinsic negative-support theorem L5, an
exact maximal-negative-component charge identity, and a localized deficit
bound built from the same action-drop measure as the branching bonus.  The
first unrepaired implication is one correlated component inequality, stated
as (U) below.  The round stops there: replacing (U) by independently
worst-cased cell bounds produces a false sufficient route.

No mathematical status is changed by this report.

## 0. Preflight, authority, and conflicts

The preflight was run before the derivation.

| item | verified value |
|---|---|
| repository | `yutianlee/polya-ai-collab` |
| base HEAD | `62119aa918b86ddb4e96d03426f5db7685c381d1` |
| branch | `codex/general-d-round-47-d4-weighted-aggregate` |
| Round 46 content commit | `a72bc4565d6a29a723545e0a5d38c8e8b1cfb79c`, an ancestor of HEAD |
| `state/proof_obligations.yml` SHA-256 | `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4` |
| high-floor first-drop CST | `open` |
| branching backbone | `derived_under_assumptions` |
| weighted aggregate | `proposed` |
| pointwise assembly | `open` |
| all-dimensional target | `proposed` |

### Conflict A: stale selected workflow

The state file still selects `SHELL-general-d-high-floor-first-drop-CST` and
describes the stopped pointwise campaign.  The finalized Round 46 audit and
the Round 47 human packet select `SHELL-general-d-weighted-aggregate` as the
workflow.  This changes no status field.

### Conflict B: stale manuscript narrative

The abstract and status narrative of
`manuscript/spherical-shell-polya-general-d.tex` predate the completed
first-floor no-drop integration and Rounds 44--46.  The manuscript was used
for definitions and proved lemmas only, not as a status source, and was not
edited.

The completed three-dimensional theorem remains frozen.  The real-order
phase proxy is retained with its recorded external dependency, and the
branching backbone remains `derived_under_assumptions` pending its dedicated
frozen audit.

## 1. Frozen notation and literal target

Let

\[
 G_R(z)=\frac1\pi\left(\sqrt{R^2-z^2}-z\arccos\frac zR\right)
 \quad(0\le z\le R),
\]

with zero extension, let \(\mu=\rho K\), and put

\[
 A(z)=G_K(z)-G_\mu(z).
\]

The strict bracket is always

\[
 [x]_<:=\#\{n\in\mathbb N:n<x\}
       =\max\{0,\lceil x\rceil-1\}.
\]

In particular, \([N]_< =N-1\) at a positive integral wall.  For every
integer \(a\ge1\), define

\[
 q_a=\left[A(a)+\frac14\right]_<,
\]

\[
 D_a:=D_A(a)=2\int_a^K A(z)\,dz
       -q_a-2\sum_{b>a}q_b,
\]

and

\[
 L_a=2\int_a^{a+1}A(z)\,dz-q_a-q_{a+1}.
\]

All integrals use the zero extension.  Thus these expressions remain
literal on a final truncated cell.

For \(d=4\), \(r_m=m+1\) and \(c_{4,m}=m+1\).  Reindexing with
\(a=m+1\) gives

\[
 \begin{aligned}
 P_4^<
 &=\sum_{a\ge1}a\left(q_a+2\sum_{b>a}q_b\right)\\
 &=\sum_{b\ge1}\left(b+2\sum_{a=1}^{b-1}a\right)q_b
 =\sum_{b\ge1}b^2q_b.
 \end{aligned}
\]

The exact ball moment is

\[
 \int_0^R z^2G_R(z)\,dz=\frac{R^4}{64},
\]

so

\[
 W_4=\int_0^Kz^2A(z)\,dz
 =\frac{K^4-\mu^4}{64}.
\]

The literal Round 47 target is

\[
 \boxed{\mathrm{WT}_4=W_4-P_4^<
 =\mathcal B_4(A)+\sum_{a\ge1}aD_a\ge0}
 \tag{WT4}
\]

on

\[
 K^2>\frac{\pi^2}{(1-\rho)^2}+\frac34.
\]

The equality-inclusive complement is assigned to the strict spectral
no-mode theorem.  That theorem says the spectral count is zero there; it is
not a per-shift assertion that \(D_a\ge0\), and no such assertion is used.

## 2. L1: exact (d=4) branching primitive

For \(d=4\),

\[
 S_4(z)=\sum_{1\le j\le z}j.
\]

Consequently \(S_4=0\) on \([0,1)\), and

\[
 \boxed{\Delta_4(z)=-\frac{z^3}{6}\qquad(0\le z<1).}
\]

At an integer \(a\ge1\), the grid formula gives
\(\Delta_4(a)=-a/6\).  On \(z=a+x\), \(0\le x<1\),

\[
 \begin{aligned}
 \Delta_4(a+x)
 &=-\frac a6+\int_0^x
 \left(\frac{a(a+1)}2-\frac{(a+t)^2}{2}\right)dt\\
 &=\boxed{-\frac a6+\frac{ax(1-x)}2-\frac{x^3}{6}}.
 \end{aligned}
 \tag{L1.1}
\]

Write \(h_a(x)=-\Delta_4(a+x)\).  Its only critical point in
\([0,1]\) is

\[
 x_a^*=\sqrt{a(a+1)}-a,
\]

because

\[
 h_a'(x)=\frac{x^2+2ax-a}{2}.
\]

The derivative changes from negative to positive there.  Direct
substitution, using \((x_a^*)^2+2ax_a^*=a\), yields

\[
 \boxed{
 \min_{0\le x\le1}[-\Delta_4(a+x)]
 =\frac{a(a+1)}
 {12\{a+\frac12+\sqrt{a(a+1)}\}}.}
 \tag{L1.2}
\]

Moreover

\[
 \frac{a(a+1)}{12(a+\frac12+\sqrt{a(a+1)})}>\frac a{24},
 \tag{L1.3}
\]

because this is equivalent to
\(a+3/2>\sqrt{a(a+1)}\), whose squared gap is
\(2a+9/4>0\).  The exact value (L1.2), rather than only (L1.3), is kept
in the subsequent exact cell ledger.

## 3. L2: exact cell bonus and coarse action moment

Put

\[
 h(z)=-\Delta_4(z),\qquad \sigma(z)=-A'(z)\ge0.
\]

For an integer \(a\ge0\), let

\[
 \mathcal B_{4,a}(A)
 =2\int_a^{\min(a+1,K)}\sigma(z)h(z)\,dz.
 \tag{L2.1}
\]

The zero extension makes every cell beyond \(K\) vanish and gives the
exact finite decomposition

\[
 \boxed{\mathcal B_4(A)=\sum_{a\ge0}\mathcal B_{4,a}(A).}
 \tag{L2.2}
\]

For \(a\ge1\), define the exact minimum

\[
 M_a=\frac{a(a+1)}
 {12\{a+\frac12+\sqrt{a(a+1)}\}}.
\]

Then the exact-minimum lower form is

\[
 \boxed{
 \mathcal B_{4,a}(A)
 \ge2M_a\{A(a)-A(\min(a+1,K))\}.}
 \tag{L2.3}
\]

Here and below an endpoint at or beyond \(K\) has action zero.  Only now
using \(M_a>a/24\), discarding the nonnegative cell \(a=0\), and summing
by parts gives

\[
 \begin{aligned}
 \mathcal B_4(A)
 &\ge\frac1{12}\sum_{a\ge1}a\{A(a)-A(a+1)\}\\
 &=\boxed{\frac1{12}\sum_{1\le j<K}A(j).}
 \end{aligned}
 \tag{L2.4}
\]

If \(K\in\mathbb N\), then \(A(K)=0\); the last term is \(j=K-1\),
not \(j=K\).  If \(K\notin\mathbb N\), the last cell is truncated at
\(K\), and the same zero-extended Abel sum applies.  Thus the strict
condition \(j<K\) in (L2.4) is exact on both faces.

## 4. L3 and L4: exact recurrence and weighted summation

Subtracting the two literal strict tails gives

\[
 \begin{aligned}
 D_a-D_{a+1}
 &=2\int_a^{a+1}A
 -q_a-2q_{a+1}+q_{a+1}\\
 &=\boxed{2\int_a^{a+1}A-q_a-q_{a+1}=L_a.}
 \end{aligned}
 \tag{L3}
\]

No ordinary floor has been substituted.  At an action wall the strict
bracket takes the lower value on both sides of this algebraic identity, so
(L3) remains exact.

For all sufficiently large \(a\), \(D_a=0\).  Hence

\[
 D_a=\sum_{j\ge a}L_j.
\]

Finite reindexing now gives

\[
 \begin{aligned}
 \sum_{a\ge1}aD_a
 &=\sum_{j\ge1}L_j\sum_{a=1}^j a\\
 &=\boxed{\sum_{j\ge1}\frac{j(j+1)}2L_j.}
 \end{aligned}
 \tag{L4.1}
\]

Therefore the preferred exact coordinate system is

\[
 \boxed{
 \mathrm{WT}_4
 =\mathcal B_4(A)+
 \sum_{a\ge1}\frac{a(a+1)}2
 \left(2\int_a^{a+1}A-q_a-q_{a+1}\right).}
 \tag{L4.2}
\]

## 5. L5: intrinsic localization of every possible negative tail

This section proves a support inclusion.  It does not assert that the
remaining support is nonempty.

### 5.1 Common terminal geometry in (d=4)

Use \(\bar q=\lfloor\mu\rfloor\); this symbol is deliberately distinct
from the strict counts \(q_a\).  If \(a\) is an integer inner start and
\(n_a=\lfloor\mu-a\rfloor\), then

\[
 \boxed{n_a=\bar q-a,\qquad a+n_a=\bar q.}
 \tag{L5.1}
\]

Thus every integer inner start has the same terminal point.  Define the
ordinary-floor profile

\[
 F(k)=\left\lfloor A(k)+\frac14\right\rfloor,
\]

and, for \(a\le\bar q\), let

\[
 b(a)=\max\{k\in[a,\bar q]\cap\mathbb Z:F(k)=F(a)\},
\]

\[
 f_a=F(a),\qquad p_a=b(a)-a,qquad m_a=\bar q-b(a).
 \tag{L5.2}
\]

This is an intrinsic maximal-shelf partition; it introduces no owner family
indexed by the numerical floor value.  On one maximal shelf its endpoint
\(b\), terminal gap \(m\), and ordinary floor are fixed, while
\(p=b-a\) varies with the start.

### 5.2 Exact owner exclusion

Suppose \(D_a<0\).  The following table exhausts the alternatives.

| region or owner | exact consequence | reason it cannot contain (D_a<0) |
|---|---|---|
| (a\ge K) | (A,q,D_a=0) | zero extension |
| (a\ge\mu) | outer convex tail | `SHELL-general-d-easy-tails` gives (D_a\ge0) |
| (G_K(a)\le3/4) | every later strict count is zero, including equality | turning owner gives (D_a=2\int_a^K A\ge0) |
| (0<\mu-a<1) | one inner interface | complete one-interface theorem, including all walls |
| (F(a)=0) | every strict shell count is zero | direct monotonicity and strict bracket |
| (p_a=0<n_a) | empty first shelf | S1 gives (D_a\ge D_{\bar q}+d_\rho n_a/2>0) |
| (f_a=1, p_a<n_a) | first-floor first drop | proved computer-assisted owner |
| (f_a=1, p_a=n_a) | first-floor no drop | completed WP2 integration theorem |
| (f_a\ge2, p_a=n_a) | high-floor no drop | complete incumbent computer-assisted owner |

Here

\[
 d_\rho=\frac{2\arcsin\rho}{\pi}>0.
\]

At \(\mu-a=1\), the point is assigned to the shelf formulation with
\(n_a=1\), not silently imported into the open one-interface interval.
If \(\mu\in\mathbb N\), the common terminal \(\bar q=\mu\) is itself an
outer start.  Otherwise \(0<\mu-\bar q<1\) and the one-interface theorem
owns the terminal.  In both cases

\[
 D_{\bar q}\ge0.
 \tag{L5.3}
\]

It follows already that a negative tail must obey

\[
 \boxed{f_a\ge2,\qquad 1\le p_a<n_a,\qquad m_a=n_a-p_a\ge1.}
 \tag{L5.4}
\]

Write the two ordinary shelf remainders as

\[
 e_0=A(a)+\frac14-f_a,qquad
 e_p=A(a+p_a)+\frac14-f_a,qquad E=e_0+e_p.
\]

Round 27 proves the remainder-rich owner.  Therefore every possible
negative tail also satisfies

\[
 \boxed{
 p_a>d_\rho m_a,qquad
 0\le E<E_*:=\frac{p_a-d_\rho m_a}{2p_a}<\frac12.}
 \tag{L5.5}
\]

The subsequent signed subdomains remove, in their exact scopes:

| audited module | excluded signed subdomain |
|---|---|
| Round 29 | the primary inverse component and all terminal-cell interior stationary points covered there |
| Rounds 30--32 | the retained shelf (e_p=0, B=Q=1, 2<y_1<3), on the inherited grids |
| Rounds 33--35 | every lower-(Q) hard endpoint component |
| Round 36 | the one-level gap (B=Q+1) with (p-d_\rho m\le12/7), including the equality seam |

After the proved monotone transports, the adverse owner-image is the five
overlapping classes in Round 36, Section 8:

1. the one-level gap \(B=Q+1\), \(p-d_\rho m>12/7\), at a general lower
   shelf or \(\alpha\uparrow1\) endpoint;
2. higher \(Q_N\) bad faces, \(N\ge2\), including old inverse collisions;
3. equal-count generic inverse bad faces transported to a shelf or
   \(\alpha\uparrow1\) endpoint;
4. exceptional \(\alpha=0\) simultaneous \(B/Q\) corners;
5. general lower shelves and \(\alpha\)-endpoint closures outside the
   retained Round 30--32 domain.

The original negative point need not literally lie on one of these faces;
the proved complete-terminal lower scalar is transported to such a face.
Round 37 normalizes class 1 but proves no sign.  Rounds 44--46 add no new
signed owner.  This distinction prevents a reduction image from being
misreported as literal set membership.

Combining the preceding facts proves the intrinsic support theorem

\[
 \boxed{
 \mathcal N_4(A)=\{a\in\mathbb N:a<K,\ D_a<0\}
 \subseteq \text{the unresolved hard high-floor first-drop owner-image}.}
 \tag{L5}
\]

The no-mode theorem appears in this cover only as the global
equality-inclusive parameter assignment outside strict activity.  It is not
a theorem about the sign of an individual shifted defect.

## 6. Exact maximal-negative-component charge

Let \(C=[u,v]\cap\mathbb N\) be a maximal consecutive component of
\(\mathcal N_4(A)\), and write

\[
 T_j=\frac{j(j+1)}2,qquad S_{u,v}=T_v-T_{u-1}=\sum_{a=u}^v a.
\]

Iterating L3 from the nonnegative right boundary gives

\[
 D_a=D_{v+1}+\sum_{j=a}^vL_j.
\]

Thus

\[
 \boxed{
 \sum_{a=u}^v aD_a
 =S_{u,v}D_{v+1}
 +\sum_{j=u}^v(T_j-T_{u-1})L_j.}
 \tag{C-right}
\]

Every printed coefficient is nonnegative.  When \(u>1\), the left-oriented
form is also exact:

\[
 \boxed{
 \sum_{a=u}^v aD_a
 =S_{u,v}D_{u-1}
 -\sum_{j=u-1}^{v-1}(T_v-T_j)L_j.}
 \tag{C-left}
\]

Maximality yields

\[
 L_{u-1}=D_{u-1}-D_u>0\quad(u>1),
 \qquad L_v=D_v-D_{v+1}<0.
 \tag{C-sign}
\]

Consequently the positive-weight form (C-right) puts its largest local
weight \(S_{u,v}\) on the necessarily negative exit increment \(L_v\).
The formula is exact, but L3 alone supplies no sign.

Indeed, coefficient matching shows that (C-right) is the unique expression
using the right boundary and the increments \(L_u,\ldots,L_v\): the
coefficient of \(L_j\) must be \(\sum_{a=u}^j a=T_j-T_{u-1}\).
Introducing a positive left-boundary coefficient forces a negative
coefficient on \(L_{u-1}\).  Thus changing orientation cannot manufacture a
positive charge.

## 7. A proved localized deficit built from action drops

This is the quantitative partial result beyond L1--L5.

For a hard first-drop start, put \(p=p_a\), \(m=m_a\), and
\(q=\bar q\).  The wall-safe first-shelf reduction S1 and curvature bound
S3 give

\[
 \begin{aligned}
 D_a
 &\ge D_q+R_p+\frac{d_\rho m}{2}\\
 &\ge D_q-\frac{p-d_\rho m}{2}
 +2\int_0^p t\,\sigma(a+t)\,dt.
 \end{aligned}
 \tag{X.1}
\]

Define

\[
 Y_a=\frac{p-d_\rho m}{2}
 -2\int_0^p t\,\sigma(a+t)\,dt
 \tag{X.2}
\]

and

\[
 \boxed{\Xi_a=\bigl[Y_a-D_q\bigr]_+.}
 \tag{X.3}
\]

Set \(\Xi_a=0\) outside the L5 hard support.  Then (X.1) proves

\[
 \boxed{D_a\ge-\Xi_a.}
 \tag{X.4}
\]

The coarser terminal-free form

\[
 \Xi_a^{(0)}=[Y_a]_+
\]

also works, but (X.3) is strictly preferable because every integer start
shares the exact terminal \(q=\lfloor\mu\rfloor\).  This common terminal is
kept correlated; it is not separately charged once for every start.

The curvature payment in (X.2) uses precisely the action-drop density
\(\sigma=-A'\) that occurs in

\[
 \mathcal B_4(A)=2\int_0^K\sigma(z)(-\Delta_4(z))\,dz.
\]

Thus \(\Xi_a\) is not a flat error ansatz.  It is supported by L5 and is
built from the same action drops as the bonus.  What remains missing is the
correlated weighted comparison

\[
 \boxed{
 \sum_{a\in\mathcal N_4(A)}a\Xi_a
 \le \mathcal B_4(A)
 +\sum_{a\notin\mathcal N_4(A)}aD_a.}
 \tag{X.5}
\]

This is sufficient for (WT4), not equivalent to it, and is not proved here.

## 8. Canonical disjoint component allocation and the first gap

Order the negative components from left to right.  For
\(C=[u,v]\), assign

\[
 J_C=\{u-1,u,\ldots,v\}\cap\{j:0\le j<K\}
\]

and

\[
 P_C=\begin{cases}
 \{v+1\},&v+1<K,\\
 \varnothing,&v+1\ge K.
 \end{cases}
\]

Distinct components are separated by at least one nonnegative tail, so the
sets \(J_C\) are pairwise disjoint and the sets \(P_C\) are pairwise
disjoint.  Every member of \(P_C\) has nonnegative defect.  Bonus cells and
tail charges are different terms in the master identity; their indices may
coincide without double counting a mathematical quantity.

Define the exact allocated charge

\[
 \mathcal U_C=
 \sum_{a=u}^v aD_a
 +\sum_{j\in J_C}\mathcal B_{4,j}(A)
 +\sum_{b\in P_C}bD_b.
 \tag{U.1}
\]

All unallocated bonus cells and all unallocated nonnegative tails remain
nonnegative.  Therefore

\[
 \boxed{\mathcal U_C\ge0\text{ for every maximal }C}
 \tag{U}
\]

would imply (WT4).  Substitution of (C-right) prints every coefficient:

\[
 \begin{aligned}
 \mathcal U_C
 ={}&S_{u,v}D_{v+1}
 +\sum_{j=u}^v(T_j-T_{u-1})L_j\\
 &+\sum_{j\in J_C}\mathcal B_{4,j}(A)
 +\mathbf 1_{v+1<K}(v+1)D_{v+1}.
 \end{aligned}
 \tag{U.2}
\]

This is the first unrepaired inequality.  The exact polynomial bonus, the
floor remainders in \(L_j\), the common terminal reserve, and the shelf
action drop must be estimated together.  No pointwise or integrated kernel
inequality proving (U) was found.

The round stops at (U), as required: after L1--L5, (C-right), and (X.4), a
further independent worst-casing is only another unsigned projection.

## 9. Why a cell-self-charge proof is unavailable

A tempting replacement for (U) is

\[
 \mathcal B_{4,a}(A)+T_aL_a\ge0
 \quad\text{cell by cell}.
 \tag{false-cell}
\]

It is false.  The lead evaluator gives, at

\[
 \rho=\frac9{10},\qquad K=40,qquad \mu=36,qquad a=29,
\]

\[
 L_{29}\approx-0.400278\ldots,
\]

and

\[
 \mathcal B_{4,29}+435L_{29}
 \approx-173.9155989351099489.
\]

At the same point

\[
 W_4=13756,qquad P_4^<=9455,qquad \mathrm{WT}_4=4301>0.
\]

Moreover \(D_{29}\) is not a negative component.  This is a diagnostic
counterexample to the over-local sufficient route only; it is not a
counterexample to (U), (WT4), or the spectral theorem.  It demonstrates
that the maximal-component and terminal correlations are load-bearing.

## 10. Strict-wall, endpoint, and scale audit

| face | exact assignment |
|---|---|
| active equality (K^2=\pi^2/(1-\rho)^2+3/4) | strict spectral no-mode owner; no claim about (D_a) or WT4 |
| (K\in\mathbb N) | (A(K)=q_K=D_K=0); L2 sum is (j<K) |
| \(\mu\in\mathbb N\) | common terminal \(\bar q=\mu\) is outer; no half-cell ambiguity |
| (A(a)+1/4\in\mathbb N) | strict (q_a=N-1), strict remainder equals 1; ordinary shelf remainder equals 0 |
| (a=\mu) | outer owner, since (G_\mu(\mu)=0) |
| (a=K) | zero extension gives (A=q=D=0) |
| final noninteger cell | every integral is truncated at (K); later (q,D,L) vanish |
| \(\rho\uparrow1\) | formulas remain exact but activity forces (K\to\infty); no uniform sign inferred from numerics |
| moderate (K) just above activity | included in L1--L5 and diagnostics; (U) remains unproved there |

No asymptotic argument is used to claim moderate-frequency closure.

## 11. Dependency ledger

| input | status and use |
|---|---|
| strict counting convention | exact definition of every (q_a,D_a,L_a) |
| real-order phase proxy | inherited external analytic input; not reproved |
| branching backbone | retained `derived_under_assumptions`; specialized algebraically to (d=4) |
| easy tails | proved; L5 outer and turning exclusions |
| one-interface theorem | proved; L5 and (D_{\bar q}\ge0) |
| S1--S3 shelf identities | proved; L5 and localized (Xi_a) |
| first-floor first drop | proved computer-assisted owner; L5 only |
| high-floor no drop | proved computer-assisted owner; L5 only |
| first-floor no drop | proved whole-regime integration owner; L5 only |
| Round 27 | proved remainder-rich split; L5.5 |
| Rounds 29--35 | proved signed subdomains and transports; L5 owner-image |
| Rounds 36--37 | exact residual face list and class-1 normal form; no residual sign imported |
| Rounds 44--46 | Gate-B reductions and stop decision only; no aggregate sign imported |

Key frozen hashes rechecked in preflight include:

- Round 46 lead: `1f3719f043616ce9877adb132fa789ab60ac84dd0aa10f27a30c7787aa9d3be1`;
- Round 46 clean room: `f23424027d9494f69692d88036b981f9c61b421484316b370da9f0041493280a`;
- Round 46 adversarial: `a6520f62d2d66bde7751aeaab01bd78a7df653cf9a9f6b54afa4ed23b5032f7c`;
- Round 46 audit: `172c98d012c4ea3535def0f4106c4f503f3a72a0420d26585395e9fbf242ee20`;
- Round 36 lead/audit:
  `6a4f95429c5c875b174b1dab4520201e1d1e1156428ddb963daaa3dbc86bea3e`,
  `9bab4fce12290671c1c29109facb4dc9185c5d0f08409f557640d7c4205bfddb`;
- Round 37 lead/audit:
  `6d45d5b787c422642e3123ecb6ac81d9e41db8f9108d928598f85ffeda3bf9e2`,
  `e2e925bb3587e916f8093d9f69945c57dd3d6208f93d42a4ebdd1b3ecc7bcf43`.

## 12. Exact loss ledger

| step | loss or strengthening | status |
|---|---|---|
| L1.1--L1.2 | none | exact |
| L2.3 | replace cell polynomial by its exact minimum | one-sided, printed |
| L2.4 | replace (M_a) by (a/24) and discard cell 0 | additional one-sided loss |
| L3--L4 | none | exact finite algebra |
| L5 | use only already signed owners in their scopes | exact support exclusion; transported faces are not literal membership |
| X.1 | S1 plus the proved S3 curvature lower bound | one-sided, wall-safe |
| X.3 | positive-part localization | one-sided; proves X.4 |
| (Xi^{(0)}) | discards (D_{\bar q}\) | valid but deliberately not used as the preferred bound |
| C-right/C-left | none | exact |
| U | demands separate component positivity | sufficient and stronger than the literal global target; open |
| false-cell | independently worst-cases the component correlation | rejected by the printed record |

## 13. No-double-counting ledger

1. The master identity contains every \(aD_a\) once and every bonus cell
   once.
2. Negative components partition \(\mathcal N_4(A)\).
3. The canonical \(J_C\) sets are disjoint; the canonical \(P_C\) sets are
   disjoint.
4. A bonus cell and a tail with the same integer label are distinct master
   terms, not duplicate charges.
5. The common terminal \(D_{\bar q}\) in (X.3) is part of each proved
   pointwise lower bound.  This report does not additionally sum copies of
   it as an external positive-tail resource.
6. Equation (X.5) uses the global bonus and the positive-tail complement
   exactly once.  It is not asserted proved.

## 14. Computational replay and falsification table

The lead diagnostic independently evaluates

\[
 W_4-P_4^<
\]

and

\[
 \mathcal B_4(A)+\sum aD_a,
\]

checks L3, L4, and (C-right), and prints the nearest action-wall distance.
The Mathematica replay proves the symbolic L1 critical point/minimum and the
formal L3/L4 coefficient identities.

| attempted falsification | result | classification |
|---|---|---|
| literal (mathrm{WT}_4<0) on named active, thin, integer, near-integer, and deterministic random records | not found | diagnostic only; no coverage certificate |
| direct proxy versus branching master | agreement to the working precision on named cases | replay, not a continuum proof |
| L1 exact minimum | Mathematica `PASS` | exact symbolic replay |
| coarse L2 lower bound | satisfied on named cases | diagnostic only |
| cell-self-charge (false-cell) | negative at ((9/10,40,29)) while WT4 is (4301) | sufficient-route counterexample only |
| component inequality (U) | neither proved nor falsified | first open implication |

Every finite positive sweep ends with

```text
positive_coverage_certificate: FALSE
```

## 15. Final status and next single obligation

### Proved in Round 47 Prompt A

1. the exact \(d=4\) primitive and its exact positive cell minimum;
2. the exact cell bonus decomposition and coarse action moment;
3. the strict adjacent-shift recurrence and weighted summation identity;
4. the intrinsic L5 support theorem, with the no-mode scope corrected;
5. the exact maximal-component charge identities;
6. the localized action-drop deficit \(D_a\ge-\Xi_a\);
7. a canonical no-double-counting reduction of WT4 to (U);
8. rejection of the cell-self-charge sufficient route.

### Not proved

- (U) on every maximal negative component;
- the global comparison (X.5);
- literal WT4 on the complete active domain;
- any all-dimensional aggregate or spectral theorem.

The first unrepaired implication, and therefore the sole next analytic
obligation, is:

\[
 \boxed{
 \sum_{a=u}^v aD_a
 +\sum_{j=u-1}^{v}\mathcal B_{4,j}(A)
 +\mathbf1_{v+1<K}(v+1)D_{v+1}\ge0
 }
\]

for every maximal negative component \([u,v]\), with truncation and the
\(u=1\) cell-zero convention stated above.  It must be proved using the
correlated shelf/action-drop data, or falsified while keeping literal WT4
separate.  No ratio ladder, count ladder, chamber family, or new compact
certificate is authorized.

The correct status statement is therefore

```text
Round 47 Prompt A: INCOMPLETE — SUBSTANTIVE AGGREGATE REDUCTION
SHELL-general-d-weighted-aggregate: remains proposed
SHELL-general-d-high-floor-first-drop-CST: remains open
SHELL-general-d-branching-backbone: remains derived_under_assumptions
TARGET-shell-general-d: remains proposed
```

## 16. Files modified by Prompt A

Created only:

```text
human/outbox/general-d-round-47-d4-weighted-aggregate.md
computations/general_d_round47_d4_weighted_diagnostic.py
computations/general_d_round47_d4_weighted_replay.wl
```
