# General-dimensional Round 36: exact count-gap and collision reduction

Date: 19 July 2026  
Status: analytic topology reduction and a one-level-gap subfamily closure
proved; high-floor CST remains open

## 0. Scope and theorem boundary

This note continues the correlated complete-terminal strategy required by
`human/inbox/general-d_simplified_analytic_strategy.md`.  It does not add a
ratio owner, a count-by-count chamber decomposition, or a computer-assisted
certificate.

The main new structural fact is

\[
 \boxed{B-Q\in\{0,1\}.}
\tag{0.1}
\]

Thus all terminal count geometry in the residual high-floor first-drop hard
sector has only an equal-count branch and a one-level-gap branch.  The wall
order, one-sided ownership, and inverse collisions of these two branches are
determined exactly below.

The one-level-gap branch has the uniform complete-terminal reserve

\[
 L_T>1-J>\frac67.
\tag{0.2}
\]

Consequently its full Round 28 scalar is positive whenever

\[
 \boxed{p-dm\leq\frac{12}{7}.}
\tag{0.3}
\]

In particular, every hard-sector tuple with \(p=1\) on this branch is
closed.  This is a genuine continuum closure, including bad sides of old
inverse walls.

The result does **not** close the residual one-level-gap branch with
\(p-dm>12/7\), the higher equal-count \(Q\)-walls, the general
\(\alpha\)-faces, the exceptional simultaneous \(B/Q\) corners at
\(\alpha=0\), or lower-shelf faces outside the precise Round 30--32
retained-shelf scope.  Therefore high-floor CST, pointwise assembly, and the
all-dimensional theorem remain open.

## 1. Definitions and inherited facts

Retain the exact Round 28--30 hard-sector data

\[
 q=r+p+m,\qquad \mu=q+\alpha,\qquad 0\leq\alpha<1,
 \qquad K=\mu\sec t,
\]

\[
 p>dm,\qquad 0\leq E<E_*:=\frac12-\frac{dm}{2p},
\tag{1.1}
\]

and

\[
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}+a_pM_4+p(E-E_*).
\tag{1.2}
\]

On both inherited extension grids one has \(q\geq3\).  Write

\[
 h=G_\mu(q),\qquad v=G_K(q),\qquad
 s=A(q)+\frac14=v-h+\frac14,
\tag{1.3}
\]

\[
 Q=[s]_<,\qquad B=[s+h]_<,
 \qquad J=2\int_q^\mu G_\mu(z)\,dz.
\tag{1.4}
\]

For \(1\leq k\leq B\), the complete inverse data are

\[
 \frac K\pi(\sin\theta_k-\theta_k\cos\theta_k)=k-\frac14,
 \qquad y_k=K\cos\theta_k-q,
\]

\[
 \eta_k=y_k-[y_k]_<,
 \qquad \beta=\frac1\pi\arccos\frac qK.
\tag{1.5}
\]

The exact Round 10 terminal expression is

\[
 L_T=
 \sum_{k=1}^{B}\frac\pi{2\theta_k}
 +2\sum_{k=1}^{B}\eta_k-Q-J
 +\frac{(v-B)_+^2}{\beta}.
\tag{1.6}
\]

We use the already proved uniform cap estimate

\[
 \boxed{J<\frac17}
\tag{1.7}
\]

from Round 21.  No numerical approximation is used below.

### 1.1 Dependencies

The proof uses only the following promoted inputs.

1. Round 10: the exact complete-terminal formula (1.6).
2. Round 21: the uniform cap bound (1.7) and strict interface-level
   transport.
3. Rounds 27--28: the automatic/hard split (1.1), the selected scalar
   (1.2), and its implication for the exact shifted tail.
4. Round 29: strict phase-cell monotonicity, the exact count jumps, and
   strict fixed-\(K\), fixed-\(Q\) wall monotonicity.
5. Rounds 30--32: the precise retained-shelf reduction and its closure only
   on \(e_p=0,\ B=Q=1,\ 2<y_1<3\).
6. Round 34: global activity excision on the high-floor first shelf.
7. Round 35 and its small-phase companion: full closure of the \(N=1\)
   lower-\(Q\) hard face.

All remaining steps are strict-floor arithmetic, elementary ball-action
calculus, or nonnegative-term retention.  No diagnostic sign is a
dependency.

## 2. Cap geometry and the exact count gap

### 2.1 The local cap is shorter than one quarter

For \(0<\alpha<1\), the derivative

\[
 -\partial_zG_\mu(z)=\frac1\pi\arccos\frac z\mu
\]

gives

\[
 h=\int_q^{q+\alpha}\frac1\pi\arccos\frac z\mu\,dz.
\tag{2.1}
\]

Here

\[
 \frac z\mu\geq\frac q{q+\alpha}>
 \frac q{q+1}\geq\frac34>\cos\frac\pi4.
\]

Therefore

\[
 \boxed{0<h<\frac\alpha4<\frac14.}
\tag{2.2}
\]

The function \(G_\mu\) is convex on \([q,\mu]\), vanishes at \(\mu\),
and has value \(h\) at \(q\).  It lies below its endpoint chord, so

\[
 J=2\int_q^\mu G_\mu(z)\,dz\leq\alpha h<h.
\tag{2.3}
\]

At \(\alpha=0\), one has \(h=J=0\).

### 2.2 Only two count branches

Adding a number in \([0,1/4)\) to the argument of a strict integer bracket
can raise its value by at most one.  Equations (1.3)--(1.4) therefore give

\[
 \boxed{B-Q\in\{0,1\}.}
\tag{2.4}
\]

There is no hidden third count branch at an integer wall: the definition
\([N]_< =N-1\) is used literally.

The hard-sector inequalities also give a finite intrinsic count ceiling.
Since \(0\leq e_p\leq e_0\) and \(E=e_0+e_p<1/2\),

\[
 e_p\leq\frac E2<\frac14.
\]

Thus

\[
 A(r+p)=f-\frac14+e_p<f,
 \qquad A(q)<A(r+p),
\]

and (2.2) yields \(v=A(q)+h<f+1/4\).  Hence

\[
 \boxed{0\leq Q\leq B\leq f.}
\tag{2.5}
\]

This ceiling is bookkeeping only; no separate owner is introduced for each
value of \(B\) or \(Q\).

## 3. Wall order and strict ownership

Fix \(0<\alpha<1\).  Then \(h\) is fixed while \(s=A_t(q)+1/4\)
strictly increases with the phase \(t\).

For each \(N\geq1\), the outer-action wall \(B_N\) is

\[
 s+h=N.
\tag{3.1}
\]

Its literal and bad phase-right labels are respectively

\[
 (B,Q)=(N-1,N-1),
 \qquad (B,Q)^+=(N,N-1).
\tag{3.2}
\]

The terminal shell-action wall \(Q_N\) is

\[
 s=N.
\tag{3.3}
\]

Its literal and bad phase-right labels are

\[
 (B,Q)=(N,N-1),
 \qquad (B,Q)^+=(N,N).
\tag{3.4}
\]

Since \(h>0\), (3.1) occurs before (3.3).  Hence

\[
 \boxed{B_N\ \hbox{wall}\;<\;Q_N\ \hbox{wall in phase order},}
\tag{3.5}
\]

and the open strip between them is exactly \(B=Q+1\).

At \(\alpha=0\), \(h=0\), so the walls coincide.  Literal ownership is
\((N-1,N-1)\), whereas the bad phase-right side is \((N,N)\).  The
one-sided limit along an open \(B_N\) bad face has labels \((N,N-1)\) and
is one complete-terminal unit stronger.  These two limits must not be
identified.

## 4. The one-level-gap terminal reserve

Suppose \(B=N\) and \(Q=N-1\), at an ordinary point or on any selected
bad side of an old inverse wall.  The top interval is nonnegative, every
selected fractional part is nonnegative, and
\(0<\theta_k<\pi/2\).  Rewriting (1.6) gives

\[
 L_T=
 1-J+
 \sum_{k=1}^{N}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 +\frac{(v-N)_+^2}{\beta}.
\tag{4.1}
\]

Every summand in parentheses is strictly positive.  Therefore, including
all one-sided old inverse collisions,

\[
 \boxed{L_T>1-J>\frac67>0.}
\tag{4.2}
\]

The clipping in (1.2) is consequently inactive.  Using

\[
 p(E-E_*)=pE-\frac{p-dm}{2},
\tag{4.3}
\]

and \(a_pM_4,pE\geq0\), one obtains

\[
 \Psi^{L_T}_{4,E}
 >\frac67-\frac{p-dm}{2}.
\tag{4.4}
\]

This proves the advertised exact closure

\[
 \boxed{
 B=Q+1,\quad p-dm\leq\frac{12}{7}
 \quad\Longrightarrow\quad
 \Psi^{L_T}_{4,E}>0.}
\tag{4.5}
\]

If \(p=1\), hardness gives \(0<1-dm<1<12/7\), so every one-level-gap
face with \(p=1\) is included.

## 5. Outer-\(B\) walls and old inverse collisions

On the bad side of \(B_N\), the new level satisfies

\[
 y_N\downarrow0^+,
 \qquad \theta_N\to\pi\beta,
 \qquad \eta_N\downarrow0.
\tag{5.1}
\]

Let \(C\subset\{1,\ldots,N-1\}\) be the set of simultaneous old inverse
walls, and take their bad sides, so the corresponding \(\eta_k^+\) are
zero.  The top interval vanishes at the bad-right limit and (4.1) becomes

\[
 \boxed{
 L_{B_N,C}^+
 =1-J+
 \sum_{k=1}^{N}
 \left(\frac\pi{2\theta_k}-1+2\eta_k^+\right)
 >1-J.}
\tag{5.2}
\]

The raw count jump is

\[
 -\frac1{16\beta}-2|C|.
\tag{5.3}
\]

The new \(y_N=0\) level is already included in the
\(-1/(16\beta)\) outer-action jump and must not receive another inverse
jump.

If an old level \(k<N\) collides at \(y_k=j\in\mathbb N\), then

\[
 N-k
 =G_K(q)-G_K(q+j)
 =\int_q^{q+j}\frac1\pi\arccos\frac zK\,dz
 <\frac j2.
\]

Thus

\[
 \boxed{j\geq2(N-k)+1\geq3.}
\tag{5.4}
\]

Both the \(B_N\) wall and \(y_k=j\) fix \(K\).  Hence such an
inverse/outer-\(B\) collision is either absent or persists along the whole
allowed \(\alpha\)-segment; it is not an isolated extra chamber.

At the exceptional \(\alpha=0\) simultaneous \(B/Q\) corner, the bad
side instead has

\[
 \boxed{
 L_{BQ_N,C}^+
 =\sum_{k=1}^{N}
 \left(\frac\pi{2\theta_k}-1+2\eta_k^+\right)>0,}
\tag{5.5}
\]

and raw jump

\[
 -1-\frac1{16\beta}-2|C|.
\tag{5.6}
\]

The unit in (5.2) is genuinely absent, so (4.5) does not close this
exceptional equal-count corner.

## 6. Higher \(Q\)-wall geometry

On the open bad side of \(Q_N\), with \(0<\alpha<1\),

\[
 A(q)=N-\frac14,
 \qquad B=Q=N.
\tag{6.1}
\]

The newest inverse root is defined by

\[
 G_K(q+y_N)=N-\frac14.
\]

Since \(G_K(q)=N-1/4+h\),

\[
 h=\int_q^{q+y_N}\frac1\pi\arccos\frac zK\,dz
   =\int_q^{q+\alpha}\frac1\pi\arccos\frac z\mu\,dz.
\tag{6.2}
\]

The outer phase is strictly larger than the inner phase wherever both are
defined.  Hence

\[
 \boxed{0<y_N<\alpha<1.}
\tag{6.3}
\]

In particular, \([y_N]_< =0\) and \(\eta_N=y_N\); the newest level never
lies on an inverse spatial wall.  Only old levels \(k<N\) can collide.  On
their selected bad sides,

\[
 L_{Q_N,C}^+
 =\sum_{k=1}^{N}
 \left(\frac\pi{2\theta_k}-1+2\eta_k^+\right)-J.
\tag{6.4}
\]

The outer phase is below \(\pi/2\), so (6.2) also gives \(h<y_N/2\).
Together with \(J<\alpha h<h\), this yields

\[
 \boxed{L_{Q_N,C}^+>2y_N-J>3h>0.}
\tag{6.5}
\]

Thus every higher \(Q\)-wall has a strictly positive exact terminal term,
even at old inverse collisions.  This does not by itself pay the negative
shelf term \(p(E-E_*)\); only \(N=1\) has been closed in full, by Rounds
34--35.

The raw jump at such a collision is \(-1-2|C|\), and every old collision
again obeys (5.4).

## 7. Fixed-\(K\) transport and a disjoint inverse-face map

### 7.1 Outer-\(B\) faces

An outer-\(B_N\) wall fixes \(K\).  For every \(\alpha>0\), its bad-side
labels are \((B,Q)=(N,N-1)\), so there is no interior \(Q\)-crossing.
Round 29 Proposition 1A says that the complete scalar strictly decreases as
\(\mu\) increases along this fixed-label face.

The larger-\(\mu\) adverse endpoints are therefore the included lower
shelf \(e_p=0\) or \(\alpha\uparrow1\).  The activity face is absent by
Round 34, while the \(p=dm\) and \(E=E_*\) seams have their automatic
positive owner.  The ordinary \(\alpha=0\) endpoint lies in the opposite
transport direction; only the discontinuous combined corner (5.5) remains
separately.

This statement is a reduction, not a shelf closure.  Round 32 closed only
the precise Round 30 retained shelf \(B=Q=1,\ 2<y_1<3\).  A general
one-level-gap lower-shelf endpoint is outside that theorem.

### 7.2 Generic inverse walls

Away from outer-\(B\) walls, fix an inverse wall \(K=K_{k,j}\), let
\(B=N\), and write

\[
 \xi=v+\frac14-N\in(0,1).
\tag{7.1}
\]

Since \(h(\alpha)=G_{q+\alpha}(q)\) strictly increases from zero,

\[
 Q=
 \begin{cases}
 N,&h<\xi,\\
 N-1,&h\geq\xi,
 \end{cases}
\tag{7.2}
\]

with literal lower ownership \(Q=N-1\) at \(h=\xi\).  There is at most
one \(Q\)-collision, and none if \(\xi\) exceeds the
\(\alpha\uparrow1\) cap.  At a reached collision the adverse value is the
\(\mu\)-left, equivalently phase-right, one-sided owner \(Q=N\), not the
literal value at equality.

Round 29 fixed-\(K\) monotonicity now gives a disjoint transport map:

1. if the \(Q\)-collision is reached before another feasible endpoint, the
   pre-collision \(Q=N\) segment ends at its bad left side; if it is not
   reached, that segment ends at \(e_p=0\) or \(\alpha\uparrow1\);
2. the post-collision \(Q=N-1\) segment ends at \(e_p=0\) or
   \(\alpha\uparrow1\);
3. a generic \(\alpha=0\) inverse endpoint is not adverse unless it is
   also a shelf or simultaneous \(B/Q\) corner.

No interior inverse-count owner remains.

## 8. Exact remaining face list and next target

After Rounds 29--35 and the reductions above, the unresolved locus is the
following exhaustive face list.  Endpoint intersections are intentionally
retained in every applicable item; the list is not asserted to be a
disjoint stratification.

1. The residual one-level-gap wall candidates—outer-\(B\) bad faces and
   inverse bad faces inside the gap strip—with
   \[
    B=Q+1,\qquad p-dm>\frac{12}{7},
   \]
   transported to general lower-shelf or \(\alpha\uparrow1\) endpoints.
   If a fixed-\(K\) arc reaches \(p-dm=12/7\) first, (4.5) closes that
   point and Round 29 monotonicity closes the earlier arc.  A genuinely
   residual transported endpoint therefore still satisfies the displayed
   strict inequality.
2. Higher \(Q_N\) bad faces \(N\geq2\), including old inverse collisions
   and their \(\alpha\uparrow1^-\) closure.  Their \(\alpha=0\) closure is
   assigned to item 4.
3. Equal-count generic inverse bad faces away from \(Q\)-walls, transported
   to shelf or \(\alpha\uparrow1\) endpoints.  A reached \(Q\)-collision
   is exactly the bad phase-right \(Q_N\) owner: \(N=1\) is closed by
   Rounds 34--35, and \(N\geq2\) belongs to item 2.
4. Exceptional \(\alpha=0\) simultaneous \(B/Q\) corners, with or without
   old inverse collisions.
5. General lower-shelf faces and their \(\alpha\)-endpoint closures outside
   the exact Round 30--32 retained-shelf domain
   \(e_p=0,\ B=Q=1,\ 2<y_1<3\) on the inherited grids.

For completeness, the exhaustion is as follows.  Round 29 phase
monotonicity sends each terminal cell to the lower shelf or to a bad
outer-\(B\), \(Q\), or inverse wall.  An outer-\(B\) bad side is a gap
face and transports at fixed \(K\).  A generic inverse wall has the unique
split (7.2), so it transports either to its bad \(Q\)-collision or to a
shelf/\(\alpha\) endpoint.  The \(N=1\) \(Q\)-wall is closed by Rounds
34--35; the higher walls remain.  At \(\alpha=0\), the only discontinuous
count endpoint is the combined \(B/Q\) corner.  Round 34 removes activity,
and Round 27 owns the \(p=dm\) and \(E=E_*\) automatic seams.

The next pointwise target should be one unified one-level-gap theorem,

\[
 1-J+
 \sum_{k=1}^{B}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 +a_pM_4+p(E-E_*)>0,
\tag{8.1}
\]

on the residual domain \(p-dm>12/7\).  This is one correlated scalar, not
a family indexed by \(B\).  It simultaneously covers outer-\(B\) bad
sides, inverse bad sides inside the gap strip, and persistent
inverse/outer-\(B\) collisions.

The second target is the higher \(Q_N\) family, using the intrinsic action
deficit \(f-N\), the newest-root reserve (6.5), and the Round 34 correlated
quadrature argument.  If either exact face resists, the revised strategy
requires returning to the exact shifted-tail scalar and then the weighted
aggregate; it does not authorize a count ladder or another certificate.

## 9. Equality-face audit

1. At \(\alpha=0\), \(h=J=0\) and \(B=Q\).  At a simultaneous
   \(B/Q\) corner one uses (5.5), not the one-level-gap limit (5.2).
   Generic \(\alpha=0\) points retain the full formula (1.6), including
   any top interval.
2. The endpoint \(\alpha=1\) is excluded.  Every occurrence above means
   the one-sided limit \(\alpha\uparrow1^-\).
3. At \(s+h=N\) or \(s=N\), the literal bracket is
   \([N]_< =N-1\).  Equations (3.2) and (3.4) distinguish that literal
   owner from the adverse phase-right value.
4. If \(s=Q+u\), \(0<u\leq1\), then the equality \(u+h=1\) gives
   \([s+h]_< =Q\); it belongs to the equal-count branch.  The gap branch
   starts only at \(u+h>1\).
5. At an old inverse wall \(y_k=j\in\mathbb N\), literal ownership has
   \(\eta_k=1\); its adverse right side has \(\eta_k\downarrow0\).  At a
   new outer-\(B\) level, \(y_N=0\) is already part of the outer-action
   jump and is not charged a second inverse jump.
6. The endpoint \(q+j=K\) cannot support an inverse level
   \(k\geq1\), because \(G_K(K)=0<k-1/4\).
7. At \(p-dm=12/7\), (4.4) is still strict because \(J<1/7\).  At
   \(p=dm\) or \(E=E_*\), the automatic owner applies.
8. The top-activation and \(L_T=0\) seams are continuous.  On the gap
   branch (4.2) keeps \(L_T>0\), so its clipping is literally inactive.
9. A lower-shelf intersection is not silently declared closed: only the
   exact Round 30--32 retained-shelf domain listed in Section 8 has been
   proved.

## 10. Counterexample search and rejected strengthenings

The proof itself rules out a third count branch and rules out old
inverse/outer-\(B\) collisions in spatial bands \(j=1,2\).  Two tempting
stronger statements are deliberately rejected.

1. The unit in (5.2) does not survive the simultaneous \(\alpha=0\)
   \(B/Q\) corner; the exact formula is (5.5).
2. Strict positivity of the terminal term on a higher \(Q_N\)-wall does
   not imply positivity of the full scalar, because \(p(E-E_*)\) may be
   negative.

The existing endpoint diagnostic

`computations/general_d_round28_endpoint_curvature_projection_diagnostic.py`

was rerun only as a counterexample search for the residual correlated
scalar.  It found no sampled negative complete scalar.  Its grid is not an
exhaustive continuum cover, and neither that observation nor any sampled
margin is used in an implication above.  The unsupported residual remains
exactly (8.1).

## 11. Exact symbolic replay and loss ledger

The Mathematica replay

`computations/general_d_round36_count_gap_replay.wl`

checks the ball-action derivatives and integral identities, the gap/equal
count rewrites (4.1), (5.5), and (6.4), the scalar identity (4.3), and the
threshold arithmetic in (4.4)--(4.5).  It is an exact replay only; no
floating-point sign is used as a premise.

The only losses in the proved subfamily closure are:

1. replacing the positive angle/fraction/top surplus in (4.1) by zero;
2. using the previously proved uniform cap \(J<1/7\);
3. discarding \(a_pM_4\) and \(pE\), both nonnegative.

All exact fractional inverse data remain available in (8.1) for the
residual branch.

## 12. Gate decision

The count-gap lemma, wall-order/collision map, exact terminal formulas, and
the closure (4.5) may be promoted as analytic results.  The high-floor CST
node must remain open because the five overlapping face classes in Section
8 are not yet closed.  No all-dimensional theorem statement may be
promoted.
