# Revision 1 independent audit

Date: 17 July 2026

Scope:

- human/inbox/revision_1.md;
- manuscript/analytic/ratio-sharp-global-closure-body.tex;
- the disjoint owner assembly in
  manuscript/spherical-shell-polya-proof.tex.

## Verdict

PASS. Three independent reconstructions found no mathematical failure in
the ratio-sharp angular estimate, the tangent-envelope retained-radial
estimate, the ball quarter-layer reduction, or the scalar convexity
closure. A second source-level pass found no lost label, reference, strict
wall, or owner face.

## Corrections incorporated before promotion

1. The disjoint high-frequency owners are
   \(0<\rho<39/50\) and \(39/50\leq\rho<1\); the shared
   \(\rho=39/50\) face is assigned to the optical theorem.
2. The simplified \(g(\tau)/8\) interface payment is stated only after
   proving \(\tau>1/4\).
3. The ball inverse lower bound is proved nonnegative before it is squared.
4. The constants are
   \[
   \alpha=\frac{6C}{5\,4^{5/3}},\qquad
   \beta=\frac{3C^2}{7\,4^{7/3}}.
   \]
5. The previously compressed assertions \(F_0'''>0\), \(D_0''>0\), and
   \(\partial_K^2\underline{\mathcal G}>0\) are displayed with exact
   rational lower bounds.
6. \(R_B\) is defined as the inverse of \(G_K\) restricted to \([0,K]\).

## Independently checked margins

\[
\begin{aligned}
F_0(1)&>\frac{8269}{30000}>\frac14,&
F_0'(1)&>-\frac{14437}{6125}>-\frac52,\\
F_0''(1)&>\frac{18162}{1225}>14,&
F_0'''(x)&>\frac{676141}{2450}>0,\\
D_0(1)&>\frac1{300},&
D_0'(1)&>\frac{54}{175},\\
D_0''(x)&>\frac{1951}{100},&
\partial_K^2\underline{\mathcal G}
&>\frac{47447}{443682}.
\end{aligned}
\]

The exact rational verifier reproduced every cubed constant comparison.
As a non-proof regression check, outward-rounded interval arithmetic on
the full base range \(1\leq x\leq13/10\) returned lower endpoints
\[
F_0>0.1745,\qquad D_0>0.0420.
\]

## Dependency conclusion

The live shell theorem needs only:

1. separation and the strict phase-to-proxy bridge;
2. the no-mode comparison for \(K\leq\pi/(1-\rho)\);
3. the ratio-sharp theorem for
   \(K>\pi/(1-\rho)\), \(0<\rho<39/50\);
4. the optical theorem for
   \(K>\pi/(1-\rho)\), \(39/50\leq\rho<1\);
5. dilation.

The former small-hole owner, finite staircases, 38-state theorem, residual
sets, and ledger rows have no live implication.
