# Independent audit: Round 34 activity excision and correlated quadrature reduction

Date: 19 July 2026  
Verdict: PASS for the proved reductions; the final face and stationary signs
remain open

## 1. Audited scope

I independently checked

human/outbox/general-d-round-34-activity-excision-and-correlated-quadrature-reduction.md

and replayed

computations/general_d_round34_activity_and_quadrature_replay.wl

with Mathematica 15.  The promoted claims are only:

1. activity is automatic on every inherited high-floor first shelf;
2. the exact adjacent-action lemma
   \[
   \Delta>(f-1)\frac{U_r-U_x}{U_x-U_q};
   \]
3. reduction of lower-\(Q\) hard-sector exclusion to the intrinsic scalar
   (3.15) on (3.16);
4. strict transport of every counterexample to \(Q\to1^-\), followed by the
   exact \(z\)-stationary alternative (3.33), (3.38).

The source leaves the transported face and stationary signs open.  This audit
proves neither lower-\(Q\) closure, high-floor CST, pointwise assembly, nor the
all-dimensional theorem.

## 2. Activity theorem

Put \(c=\mu/K\) and \(\delta=K-\mu=K(1-c)\).  First-shelf ownership and
the exact radial derivative give

\[
 \frac74\leq A(x)
 =\int_\mu^K\frac{\sqrt{1-x^2/R^2}}{\pi}\,dR
 <\frac{\delta}{\pi}.
\]

Thus \(\delta>7\pi/4\).  For
\(\gamma\in\{3/4,2\}\),

\[
 \begin{aligned}
 K^2-\frac{\pi^2}{(1-c)^2}-\gamma
 &=\frac{\delta^2-\pi^2}{(1-c)^2}-\gamma\\
 &>\frac{33\pi^2}{16(1-c)^2}-\gamma
 >\frac{33}{16}-2=\frac1{16}.
 \end{aligned}
\]

The last strict step correctly uses \(\pi^2>1\) and
\((1-c)^2<1\).  The radial integral stays strict on the included ordinary
shelf.  Hence activity equality is disjoint from the complete high-floor
first-shelf closure on both inherited grids.

## 3. Adjacent-action lemma

For \(B_s(z)=\sqrt{\mu^2-s^2z^2}\), Fubini gives

\[
 \int_a^b\sigma(z)\,dz
 =\frac1\pi\int_c^1
 \frac{B_s(a)-B_s(b)}{s^2}\,ds.
\]

For

\[
 R_s=\frac{B_s(r)-B_s(x)}{B_s(x)-B_s(q)},
\]

direct differentiation gives exactly

\[
 \frac{d}{ds}\log R_s
 =\frac{\mu^2}{sB_s(x)}
 \left(\frac1{B_s(r)}-\frac1{B_s(q)}\right)<0.
\]

Therefore \(\Delta/[A(x)-A(q)]\) is a positive weighted average strictly
larger than \(R_1\).  The retained lower-\(Q\) action
\(A(x)-A(q)=f-1+e_p\geq f-1\) proves the displayed lemma without
independently worst-casing the two action intervals.

## 4. Correlated quadrature reduction

The upper comparison is correct: the radial-parameter kernel is strictly
convex in \(s\), so

\[
 \sigma(z)<
 \frac{1-c}{2\pi}z
 \left(\frac1{U_z}+\frac1{V_z}\right).
\]

Integration over \([x,q]\) gives

\[
 T=\frac{1-c}{2\pi}
 \left\{U_x-U_q+\frac{V_x-V_q}{c^2}\right\}
 >A(x)-A(q)\geq1.
\]

The lower comparison is also correct.  Apply Jensen to

\[
 \phi(y)=\frac{z/\mu}{\sqrt{1-yz^2/\mu^2}},
 \qquad y=s^2.
\]

Here

\[
 \phi''(y)=
 \frac{3z^5}{4(\mu^2-yz^2)^{5/2}}>0,
 \qquad
 \frac1{1-c}\int_c^1s^2\,ds=\frac{1+c+c^2}{3}=a^2.
\]

With \(B_z=\sqrt{\mu^2-a^2z^2}\),

\[
 \Delta>
 \frac{(1-c)p(2r+p)}{\pi(B_r+B_x)}.
\]

The \(a^2\) factor cancels exactly after rationalization.

Under the normalization of the source,

\[
 T=\frac{\mu(1-c)}{2\pi}D.
\]

Combining \(T>1\) with
\(W=\mu(\tan t-t)/\pi<3/4\) gives

\[
 3(1-c)D>8(\tan t-t).
\]

The common grid bound \(r\geq1\), combined with the same strict upper
bound on \(\mu\), gives

\[
 z>\frac{4(\tan t-t)}{3\pi}.
\]

Finally the Jensen lower bound and lower scale from \(T>1\) give exactly

\[
 \Delta>
 C(z,P,M,t)=
 \frac{2P(2z+P)}{\{b(z)+b(X)\}D}.
\]

Thus (3.15)--(3.16) are a valid sufficient reduction with no raw scale,
floor variable, inverse root, parity interpolation, or ratio-owner seam.

## 5. Rigorous interface-face transport and stationary reduction

Put \(\rho=M/P\),

\[
 h(y)=\frac{y}{b(y)},\qquad
 g(y)=\frac y{u(y)}+\frac y{v(y)},
\]

and \(N=\int_z^Xh\), \(D=\int_X^Qg\).  At fixed
\((t,z,\rho)\), direct rationalization gives

\[
 N=\frac{P(X+z)}{b(z)+b(X)},
\]

\[
 D=\rho P(X+Q)
 \left\{\frac1{u(X)+u(Q)}+\frac1{v(X)+v(Q)}\right\}.
\]

Differentiating reproduces (3.24).  Its first two terms have exact positive
difference

\[
 \frac{2z(1+\rho)}{(X+Q)(X+z)}.
\]

For \(k\in\{1,c\}\), the exact derivative is

\[
 \frac{L_k'}{L_k}=k^2
 \frac{X/w_k(X)+(1+\rho)Q/w_k(Q)}{w_k(X)+w_k(Q)}
 >\frac{Xk^2}{2(1-k^2X^2)}.
\]

Weighting the two values, then using convexity of
\(y/(1-X^2y)\) and \((1+c^2)/2\geq a^2\), proves

\[
 \frac{L'}L>
 \frac{a^2X}{2b(X)^2}>
 \frac{a^2X}{b(X)\{b(z)+b(X)\}}.
\]

Hence \(d\log(D/N)/dP>0\) and \(C=2N/D\) strictly decreases.
Also

\[
 D'=(1+\rho)g(Q)-g(X)>0.
\]

The hard target is fixed, while the action constraint strengthens.  Thus
every counterexample transports to \(Q\to1^-\).

On that face, (3.29)--(3.30) are exact.  Since \(D_1'(X)<0\), action gives
\(X<X_D\) whenever the root exists.  Candidate existence itself forces

\[
 D_0<D_1(0)=1+\frac1{1+\sin t}.
\]

This qualification is necessary: the coarse restriction (3.18) alone does
not guarantee a real \(X_D\).  If the displayed inequality fails, the face
domain is empty.  Under it, solving in \(U=\sqrt{1-X^2}\) gives exactly the
positive branch (3.34).

Finally,

\[
 \mathcal R_z=-\frac{2z}{b(z)D_1}
 +\frac{d(1-X)}{2(X-z)^2}.
\]

The derivative of \(z(X-z)^2/b(z)\) has sign
\(X-3z+2a^2z^3\), which crosses once on \((0,X)\).  Therefore the
stationary equation has at most two roots, classified exactly as in the
source, and substitution gives (3.38).  No sign for (3.38) is inferred from
the diagnostic margin.

## 6. Walls, losses, and falsification

- The included \(e_p=0\) wall retains strictness from both quadrature
  comparisons.
- Literal lower-\(Q\) floor ownership does not change the continuous action.
- The source keeps \(0<\alpha<1\).  The \(Q\to1^-\) face is used only as a
  rigorous one-sided counterexample transport, not silently owned as an
  \(\alpha=0\) spectral point.
- The hard seam \(P=dM\) and automatic seam \(E=E_*\) retain their earlier
  owners.
- Using the common \(r\geq1\) safely discards the half-grid reserve
  \(r\geq3/2\).
- The tuple \((r,p,m,\alpha)=(1,21,17,11/100)\) correctly rejects the old
  elasticity-only projections while leaving the new scalar positive.
- The observed minimum near \(0.014074\) is explicitly theorem-design
  evidence, not a promoted universal margin.

The loss ledger is complete for the promoted claims.  In particular, the
upper and lower quadratures are combined before eliminating the scale.

## 7. Mathematica replay

The fresh replay returned:

    activityMarginIdentityResidual=0
    rationalGap=1/16
    safeGapUsingPiGreater1=1/16
    adjacentActionLogDerivativeResidual=0
    quadraturePrimitiveResiduals={0, 0, 0, 0}
    normalizedCorrelationResidual=0
    transportIdentityResiduals={0, 0, 0}
    qOneResiduals={0, 0}
    xDRootPolynomialResidual=0
    round34ActivityAndQuadratureReplayOK=True

The printed convexity derivatives have positive numerators on the stated
domain.  This is an identity audit, not a certificate for (3.33) or (3.38).

## 8. Verdict and next gate

**PASS** for activity excision, the adjacent-action lemma, strict correlated
quadratures, normalization, \(Q\to1^-\) transport, the stationary
alternative, walls, and scope.

The four-variable sign has been reduced rigorously.  The exact unsupported
signs are now

\[
 \mathcal R_{\rm stat}>0
\]

at the possible second stationary root, and

\[
 \mathcal R(t,z_0(t),X)>0,\qquad
 X_h(t,z_0)<X<X_D(t).
\]

The next pass should use the adjacent-action lemma where it is stronger and
retain the action, radius, and hard-excess constraints together.  If the
intrinsic analytic proof fails, the approved next gate is the weighted
aggregate, not another ratio partition or pointwise certificate.
