# Independent audit of General-dimensional Round 31

Date: 19 July 2026

Decision: **PASS for the stated analytic reductions; no promotion of
high-floor CST or the all-dimensional theorem.**

Audited artifacts:

- human/outbox/general-d-round-31-retained-E-convexity-and-large-q-exclusion.md
- computations/general_d_round31_retained_shelf_replay.wl

## 1. Independence

The review was split across three agents so that every load-bearing component
received a check independent of its author:

- the retained-\(E\) \(p\)-convexity kernel was independently reconstructed
  from both the radius integral and the normalized \((u,v)\)-kernel;
- the \(q\ge1000\) phase bounds, feasibility transport, \(B_c\) lower
  bound, endpoint reduction, and nine-step intrinsic implication bootstrap
  were independently reconstructed by an agent that did not derive them;
- the quartic-tail inequality, lower-scalar Hessian, three-edge reduction,
  equality faces, loss ledger, and failure scope were independently checked;
  and
- a final integration pass compared every displayed formula with the
  Mathematica replay and the stated claim boundary.

The first audit found four transcription/precision issues: a missing plus
sign in the printed convexity kernel, a strict/non-strict mismatch at
\(u=0\), an incorrectly stated cube-root bound in the \(\delta\) derivation,
and phase wording at \(z=q\).  All were corrected before the final passes.
The final three read-only passes returned PASS.

## 2. Convexity audit

For fixed \((q,m)\), the auditors verified

\[
 E_{\min}(p)=\int_{x-p}^{x}\sigma(z)\,dz,
\]

\[
 \frac{d^2}{dp^2}\{pE_{\min}(p)\}
 =2\sigma(r)-p\sigma'(r),
\]

and the curvature second derivative

\[
 C''(p)
 =\frac1\pi\int_M^K
 \left\{
  \frac p{a^2}
  +\frac{p(r^2/2+p^2/3)}{a^4}
 \right\}\,da.
\]

After \(u=r/a,\ v=p/a\), the exact kernel is

\[
 D(u,v)
 =
 \frac{2u}{\sqrt{1-u^2}}
 +v\left\{
 1+\frac{u^2}{2}+\frac{v^2}{3}
 -(1-u^2)^{-3/2}
 \right\}.
\]

The inequality direction using \(v<1-u\) is correct, and the
\(t=\sqrt{(1-u)/(1+u)}\) factorization is exact and positive.  The retained
\(v^3/3\) term handles \(u=0\).  Thus

\[
 \mathfrak F_{pp}>0
\]

on the stated continuous interval.  No shelf-feasibility or hard-sector
assumption is hidden in this convexity statement.

## 3. \(q\ge1000\) exclusion audit

Writing \(s=q^{1/3}\ge10\), the auditors independently verified the exact
angle chain

\[
 \frac{93}{50s}<\theta_2<\frac{48}{25s},
\]

\[
 \Delta=K_2-(q+1)>\frac{17}{10}s,\qquad
 \delta=K_2-q<\frac{21}{10}s,\qquad
 K_2<\frac{103}{100}q,
\]

\[
 \psi=\arccos(q/K_3)<\frac{21}{10s},\qquad
 d_{\min}>\frac{43}{50}.
\]

Every replacement direction is adverse.  The exact rational remainders in
the replay are positive.

The phase monotonicity argument from
\(G_{K_3}(q+3)=3/4\) gives

\[
 G_{K_3}(q-m)-G_q(q-m)
 <\frac34+\frac{(m+3)\psi}{\pi}.
\]

Thus shelf feasibility forces

\[
 m>\frac{11}{10}s.
\]

For \(P=cm<x\), the audit reconstructed the exact phase-kernel lower bound

\[
 E_{\min}(P)\ge
 \frac{\Delta c m\{2q-(2+c)m\}}
 {2\pi K\sqrt{2K\{\delta+(1+c)m\}}}.
\]

The \(m\)-factor has one positive critical point, a maximum.  Its infimum on
the closed comparison interval is therefore at an endpoint.  The exact
endpoint-ratio calculation proves that the lower endpoint wins for
\(43/50\le c\le10\).

No monotonicity in \(c\) is assumed.  At \(c=\lambda d_{\min}\), the proof
uses \(c>43\lambda/50\) only in the favorable prefactor and
\(c<\lambda\) separately in both adverse factors.

All nine comparisons

\[
 C_\lambda>
 \frac4{25},\frac15,\frac14,\frac7{25},\frac3{10},
 \frac13,\frac38,\frac9{20},\frac12
\]

were recomputed with exact rational arithmetic.  They force

\[
 \frac{p}{d_{\min}m}>
 1,\frac{25}{17},\frac53,2,\frac{25}{11},
 \frac52,3,4,10,
\]

after which \(E_{\min}>1/2\) contradicts the strict hard upper bound.
Therefore the claimed exclusion for every real \(q\ge1000\) passes.

The proof is shell-ratio-free: the intrinsic implication bootstrap creates
no partition or owner seam in \(\rho,K,q\).  It is not represented as a new
shell-ratio ladder.

## 4. Finite lower-scalar audit

The positive arcsine tail proves strictly

\[
 E_{\min}>\mathcal K_{4,\min}.
\]

The auditors verified the lower scalar \(L_q\), both diagonal Hessian
entries, and

\[
 \det\nabla^2L_q=-\frac{16p^2}{9}\mathcal Q,\qquad
 \mathcal Q>0.
\]

The normalized quartic polynomial is decreasing on \(0\le u\le1\) and has
minimum \(-4\), so the printed bound
\(\mathcal Q>35A^2/4\) is valid.  Hence an interior stationary point is a
saddle.  The full real triangle reduces to

\[
 p=1,\qquad r=r_0,\qquad m=1,
\]

and all three restrictions are strictly convex.  This is an analytic
candidate reduction only.  The note correctly refuses to use an unarchived
finite edge experiment as a theorem premise.

The audit also confirmed the global failure warning: positivity of the
quartic-only lower scalar is not claimed asymptotically.  Retaining the exact
\(E_{\min}\) is load-bearing.

## 5. Equality faces and scope

PASS:

- the proof holds for every real \(q\ge1000\), hence both parity grids;
- equality in shelf feasibility is accepted;
- \(p=d_{\min}m\) remains in the already proved automatic sector;
- every auxiliary length \(P=\lambda d_{\min}m\) lies strictly inside the
  actual shelf;
- \(q=1000\) is included;
- the inherited lower radii remain \(1\) and \(3/2\);
- no inverse-, \(B\)-, \(Q\)-, or ordinary-floor wall owner changes; and
- the open lower-\(Q\), \(\alpha\)-, other-band, and simultaneous-wall
  endpoint families remain explicitly outside the claim.

The exact remaining retained-shelf range is \(q<1000\).  The observed cutoff
near \(q=33\) and every finite positive minimum remain diagnostic only.

## 6. Replay and controls

Command:

    wolframscript.exe -file computations/general_d_round31_retained_shelf_replay.wl

Environment:

- Mathematica 15.0.0 for Microsoft Windows (64-bit);
- WolframScript 1.14.0 for Microsoft Windows (64-bit).

Fresh output:

- curvature/convexity residuals: all zero;
- lower-scalar Hessian residuals: all zero;
- six angle margins: exact and positive;
- two endpoint-ratio margins: exact and positive;
- nine bootstrap margins: exact and positive; and
- round31RetainedShelfReplayOK=True.

Additional controls:

- git diff --check: PASS;
- tab scan: zero;
- nonprinting control-byte scan: zero; and
- source/replay claim-boundary comparison: PASS.

Artifact hashes:

- Round 31 source:
  1b01f45cc08105c6b30bd3f1e6e2d678e18d1b4ec0dd4d013ad09bdb65a946e7
- Round 31 Mathematica replay:
  66ce23dc899bf21dd635b3281f87e9dea1dfc3c0b6d4d2191709e1abca25e541

## 7. Final decision

**PASS** for:

- strict \(p\)-convexity of the full retained-\(E\) scalar;
- analytic exclusion of the Round 30 necessary shelf/hard domain for all
  real \(q\ge1000\); and
- the finite three-edge lower-scalar reduction.

**Not proved**:

- exclusion on \(33.5<q<1000\);
- \(\mathfrak F>0\) on the remaining exact parity-grid candidates;
- any endpoint family outside the Round 30 retained-shelf scope;
- high-floor CST;
- pointwise assembly; or
- the all-dimensional theorem.
