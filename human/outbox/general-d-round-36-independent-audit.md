# General-dimensional Round 36: independent audit

Date: 19 July 2026  
Verdict: **PASS for the stated analytic reduction and subfamily closure**

## 0. Audited scope and theorem boundary

This audit independently checks

- `human/outbox/general-d-round-36-exact-count-gap-collision-reduction.md`;
- `computations/general_d_round36_count_gap_replay.wl`;
- the promoted inputs used from Rounds 21, 28--30, 32, and 34--35; and
- compliance with
  `human/inbox/general-d_simplified_analytic_strategy.md`.

The PASS verdict covers only the following new claims:

1. the exact terminal count gap \(B-Q\in\{0,1\}\);
2. the wall order and literal/adverse ownership of the \(B_N\) and \(Q_N\)
   walls;
3. the exact one-level-gap reserve \(L_T>1-J>6/7\);
4. the full-scalar closure
   \[
    B=Q+1,\qquad p-dm\leq\frac{12}{7}
    \quad\Longrightarrow\quad
    \Psi^{L_T}_{4,E}>0;
   \]
5. the outer-\(B\), \(Q\), and inverse-wall collision formulas; and
6. the fixed-\(K\) transport map and resulting exhaustive residual face list.

It does **not** promote high-floor CST, pointwise shifted-tail positivity,
the weighted aggregate, or the all-dimensional theorem.  The residual face
classes printed in source Section 8 remain open.

## 1. Dependency audit

The source uses the earlier results within their proved scopes.

1. Round 21 supplies the analytic cap bound \(J<1/7\).  Its proof applies
   already for \(q\geq2\), while the Round 28 extension grids used here have
   \(q\geq3\).
2. Round 28 supplies the exact hard-sector scalar
   \[
    \Psi^{L_T}_{4,E}
    =\max\{0,L_T\}+a_pM_4+p(E-E_*),
    \qquad E_*=\frac12-\frac{dm}{2p},
   \]
   with \(a_pM_4\geq0\).
3. Round 29 supplies phase-cell monotonicity, the three raw count jumps,
   and strict decrease of the complete scalar along fixed-\(K\), fixed-\(Q\)
   inverse or outer-\(B\) wall segments.
4. Rounds 30--32 are invoked only for their narrow retained lower shelf
   \(e_p=0,\ B=Q=1,\ 2<y_1<3\); the source explicitly leaves all other
   lower shelves open.
5. Round 34 supplies global activity excision in the inherited high-floor
   first-shelf sector.
6. Round 35 and its small-phase companion close only the \(N=1\) lower-\(Q\)
   hard face.  Higher \(Q_N\) faces are not silently assigned to that result.

No diagnostic or floating-point margin is used as a dependency.

## 2. Exact analytic audit

### 2.1 Cap and count gap

For \(0<\alpha<1\), \(q\geq3\), and \(\mu=q+\alpha\),

\[
 h=G_\mu(q)
  =\int_q^{q+\alpha}\frac1\pi\arccos\frac z\mu\,dz.
\]

Since

\[
 \frac z\mu\geq\frac q{q+\alpha}
 >\frac q{q+1}\geq\frac34>\cos\frac\pi4,
\]

the integrand is strictly below \(1/4\), giving

\[
 0<h<\frac\alpha4<\frac14.
\]

Convexity of \(G_\mu\), together with its endpoint values \(h\) and \(0\),
gives \(J\leq\alpha h<h\).  At \(\alpha=0\), \(h=J=0\).

Writing \(s=A(q)+1/4\), one has \(Q=[s]_<\) and \(B=[s+h]_<\).  Adding
\(h\in[0,1/4)\) to a strict-bracket argument changes it by zero or one,
including at the literal integer wall.  Hence

\[
 \boxed{B-Q\in\{0,1\}}.
\]

The ceiling \(0\leq Q\leq B\leq f\) is also correct: hard-sector shelf
ordering gives \(e_p\leq E/2<1/4\), hence \(A(r+p)<f\), \(A(q)<A(r+p)\),
and \(v=A(q)+h<f+1/4\).

### 2.2 Wall ownership and collision jumps

For fixed \(0<\alpha<1\), \(h\) is fixed and \(s\) increases with phase.
At \(s+h=N\), literal ownership is \((B,Q)=(N-1,N-1)\) and the adverse
phase-right owner is \((N,N-1)\).  At \(s=N\), literal ownership is
\((N,N-1)\) and the adverse phase-right owner is \((N,N)\).  Thus the
outer-\(B_N\) wall precedes the \(Q_N\) wall and their intervening strip is
exactly \(B=Q+1\).

The three raw jumps agree with Round 29:

\[
 \Delta L_T=-2
 \quad\hbox{at each old inverse wall},
\]

\[
 \Delta L_T=-\frac1{16\beta}
 \quad\hbox{at an outer-}B\hbox{ wall},
\]

and

\[
 \Delta L_T=-1
 \quad\hbox{at a }Q\hbox{ wall}.
\]

The outer-\(B\) jump follows exactly from the new contribution
\(1/(2\beta)\) and the disappearing old top triangle \(9/(16\beta)\).
Consequently simultaneous old inverse collisions contribute
\(-2|C|\), while the new \(y_N=0\) level is not charged twice.  At
\(\alpha=0\), the simultaneous \(B/Q\) jump is therefore

\[
 -1-\frac1{16\beta}-2|C|.
\]

For an old collision on an outer-\(B_N\) wall,

\[
 N-k
 =\int_q^{q+j}\frac1\pi\arccos\frac zK\,dz
 <\frac j2,
\]

so integer arithmetic gives \(j\geq2(N-k)+1\geq3\).  On a \(Q_N\) wall
the exact action gap is \(N-k+h\), which implies the same displayed lower
bound for \(j\).

### 2.3 One-level-gap full-scalar closure

When \(B=N\) and \(Q=N-1\), including selected bad sides of old inverse
walls,

\[
 L_T=1-J+
 \sum_{k=1}^{N}
 \left(\frac\pi{2\theta_k}-1+2\eta_k\right)
 +\frac{(v-N)_+^2}{\beta}.
\]

Every selected \(\eta_k\) is nonnegative and \(0<\theta_k<\pi/2\), so
each parenthesized term is strictly positive.  Therefore

\[
 L_T>1-J>\frac67>0.
\]

The clipping is inactive.  Since

\[
 p(E-E_*)=pE-\frac{p-dm}{2}
\]

and \(pE,a_pM_4\geq0\),

\[
 \Psi^{L_T}_{4,E}>
 \frac67-\frac{p-dm}{2}.
\]

This is still strict at \(p-dm=12/7\), proving the source's full-scalar
closure exactly.  In particular \(p=1\) gives
\(0<1-dm<1<12/7\).

### 2.4 Higher \(Q_N\) reserve

On the adverse side of a \(Q_N\) wall with \(0<\alpha<1\), the newest root
satisfies

\[
 h=\int_q^{q+y_N}\frac1\pi\arccos\frac zK\,dz
  =\int_q^{q+\alpha}\frac1\pi\arccos\frac z\mu\,dz.
\]

The outer phase is strictly larger on the common interval, so
\(0<y_N<\alpha<1\).  Hence \([y_N]_< =0\) and \(\eta_N=y_N\).  The
normalized outer-phase integrand is below \(1/2\), giving \(h<y_N/2\),
while \(J<h\).  All old-level
summands are positive even on their selected bad sides, and therefore

\[
 L^+_{Q_N,C}>2y_N-J>3h>0.
\]

The source correctly does not infer full-scalar positivity from this
terminal positivity.

### 2.5 Fixed-\(K\) transport and exhaustion

An outer-\(B_N\) wall fixes \(K\) and has \(Q=N-1\) for every
\(\alpha>0\), so Round 29 fixed-label monotonicity transports its adverse
candidate to the larger-\(\mu\) lower shelf or \(\alpha\uparrow1^-\).

Away from an outer-\(B\) wall, a fixed inverse wall has fixed \(B=N\).  With
\(\xi=v+1/4-N\in(0,1)\), strict bracket arithmetic gives

\[
 Q=N\quad(h<\xi),
 \qquad
 Q=N-1\quad(h\geq\xi),
\]

with literal lower ownership at equality.  Since \(h(\alpha)\) is strictly
increasing, at most one \(Q\)-collision occurs.  If reached, the adverse
candidate is its \(\mu\)-left/phase-right owner; if not reached, transport
continues to the shelf or \(\alpha\uparrow1^-\).  The expanded Section 8
correctly lists all resulting faces and explicitly allows endpoint classes
to overlap.

## 3. Equality-face audit

All equality conventions needed by the new claims are owned.

1. **Ordinary action walls.**  The convention \([N]_< =N-1\) is applied
   literally.  At \(u+h=1\), the count remains on the equal-count branch;
   the gap begins only for \(u+h>1\).
2. **Interface wall and integral \(\mu-r\).**  These are exactly
   \(\alpha=0\).  Then \(h=J=0\) and \(B=Q\).  A simultaneous \(B/Q\)
   corner uses (5.5), not the open-gap limit; a generic \(\alpha=0\) point
   retains the full formula (1.6), including any top interval.
3. **Excluded adjacent interface.**  \(\alpha=1\) is never substituted;
   every occurrence is the one-sided limit \(\alpha\uparrow1^-\).
4. **Inverse spatial walls.**  Literal ownership has \(\eta_k=1\); the
   adverse phase-right side has \(\eta_k\downarrow0\).
5. **Outer support.**  \(q+j=K\) cannot support \(k\geq1\), since
   \(G_K(K)=0<k-1/4\).
6. **Hard and automatic seams.**  The threshold \(p-dm=12/7\) remains
   strictly positive.  The seams \(p=dm\) and \(E=E_*\) retain their
   automatic owners.
7. **Continuous seams.**  Top activation and \(L_T=0\) are continuous;
   on the gap branch \(L_T>0\), so clipping introduces no ambiguity.
8. **Lower shelves.**  Only the exact Round 30--32 retained shelf is
   declared closed.  Other shelf intersections remain in the residual
   face list.

## 4. Revised-strategy compliance

The source complies with the revised analytic workflow for this partial
round.

- It retains the exact correlated terminal scalar and its fractional
  inverse data.
- It introduces neither a shell-ratio ladder nor count-indexed owners.
- The split \(B-Q\in\{0,1\}\) is an exact intrinsic dichotomy, not an
  empirical chamber decomposition.
- The threshold \(12/7\) follows analytically from the promoted cap bound;
  it is not a fitted numerical constant.
- The Mathematica file replays exact identities only and is not a compact
  certificate.
- The Round 28 diagnostic is explicitly labeled a falsification search and
  is not a proof premise.
- The precise unresolved scalar (8.1), loss ledger, equality audit, and gate
  decision are printed.
- The source instructs the next round to return to the exact shifted-tail
  scalar and then the weighted aggregate if an intrinsic face resists.

The note is therefore suitable as an analytic proof-graph node, but not as
a replacement for the still-open CST or weighted aggregate node.

## 5. Exact Mathematica replay

The replay was run locally with Mathematica 15.0 through WolframScript:

```powershell
& 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' `
  -file 'computations/general_d_round36_count_gap_replay.wl'
```

It exited with code zero and printed:

```text
zDerivative=True
radiusDerivative=True
zConvexityIdentity=True
capIntegral=True
outerInverseIntegral=True
outerWallLiteralOwnership=True
outerWallBadOwnership=True
qWallLiteralOwnership=True
qWallBadOwnership=True
countGapNoJumpBranch=True
countGapOneJumpBranch=True
alphaZeroLiteralOwnership=True
alphaZeroBadOwnership=True
inverseMapPreCollision=True
inverseMapLiteralCollision=True
inverseMapPostCollision=True
gapRewrite=True
equalRewrite=True
outerBJump=True
combinedBQJump=True
isolatedQJump=True
inverseJump=True
outerBCollisionActionGap=True
qCollisionActionGap=True
hardShelfIdentity=True
capMargin=True
gapThreshold=True
qWallReserve=True
capQuarterInputs=True
collisionBandArithmetic=True
collisionIntegerImplication=True
round36CountGapReplayOK=True
```

No floating-point value is used in any replay check.

## 6. Frozen artifact hashes

SHA-256 values at the time of this audit:

```text
6a4f95429c5c875b174b1dab4520201e1d1e1156428ddb963daaa3dbc86bea3e  human/outbox/general-d-round-36-exact-count-gap-collision-reduction.md
06b02c53ad564f771381a6ff3c557c30eb95f5d58f919c195b476e77f48db218  computations/general_d_round36_count_gap_replay.wl
```

## 7. Final verdict

**PASS.**  The exact count-gap reduction, wall/collision topology, and
one-level-gap closure for \(p-dm\leq12/7\) are valid and may be promoted as
an analytic internal node.  The source correctly leaves high-floor CST and
the all-dimensional theorem open.
