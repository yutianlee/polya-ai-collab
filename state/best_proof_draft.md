# Best Proof Draft

The submission-facing proof is
`manuscript/spherical-shell-polya-proof.tex`; the complete low/middle-ratio
calculation is
`manuscript/analytic/ratio-sharp-global-closure-body.tex`.
This file records the live logical spine.

## Statement

For every \(0<r<R\) and \(\Lambda\geq0\),

\[
N_D(A_{r,R},\Lambda)
\leq \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}.
\]

It is enough by dilation to prove this on \(A_{\rho,1}\) with
\(K=\sqrt\Lambda\).

## 1. Exact spectral reduction

Spherical harmonics reduce the Dirichlet Laplacian to the one-dimensional
operators

\[
-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad \ell=0,1,\ldots,
\]

with multiplicity \(2\ell+1\). The cross-product phase and strict phase
enclosure imply

\[
N_D(A_{\rho,1},K^2)\leq P(\rho,K),
\]

where, with \(T=(1-\rho)K/\pi\), \(R=A_{\rho,K}^{-1}\), and
\(M(r)=\#\{\ell\geq0:\ell+\tfrac12<r\}\),

\[
P=\sum_{n-1/4<T}M(R(n-1/4))^2.
\]

The Weyl target is

\[
W=\int_0^T R(t)^2\,dt
=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

## 2. Exact defect and ratio-sharp angular payment

The strict layer cake decomposes \(W-P\) into retained radial reserve minus
angular rounding defect. Put \(\theta=\arccos\rho\). The exact shell-action
slope satisfies

\[
0\leq q(z)=-A'(z)\leq\frac{\theta}{\pi}.
\]

On the disjoint left block attached to each active shifted radial level,
this yields

\[
E_{\rm ang}
<\frac{1-\rho^2}{6}K^2
-N\left(\frac{3\pi}{8\theta}-\frac14\right),
\]

with the strict half-integer convention valid even at common walls.

## 3. Retained radial reserve

The shifted-sawtooth primitive is bounded below by the \(C^1\) tangent
envelope

\[
L_\sharp(t)=
\begin{cases}
t^2/2,&0\leq t\leq1/4,\\
t/4-1/32,&t\geq1/4.
\end{cases}
\]

The Stieltjes remainder, including its endpoint signs, then reduces the shell
reserve to a universal ball quarter-layer. The outer-branch change of
variables is used only after \(\tau>1/4\) is established, and the ball-inverse
lower bound is shown nonnegative before squaring.

## 4. Scalar closure

The preceding estimates give an explicit lower bound
\(W-P>\underline{\mathcal G}(\rho,K)\). At
\(K_0=\pi/(1-\rho)\), the substitution
\(x=(1-\rho)^{-1/6}\) reduces the base value and derivative to two elementary
functions \(F_0,D_0\). Exact rational estimates prove

\[
F_0(1)>\frac{8269}{30000},\qquad
F_0'''(x)>\frac{676141}{2450},
\]

\[
D_0(1)>\frac1{300},\qquad
D_0'(1)>\frac{54}{175},\qquad
D_0''(x)>\frac{1951}{100},
\]

and

\[
\partial_K^2\underline{\mathcal G}
>\frac{47447}{443682}>0.
\]

Consequently \(P<W\) for
\(K>\pi/(1-\rho)\) and \(0<\rho<39/50\).

## 5. Final assembly

- If \(K\leq\pi/(1-\rho)\), the phase increment is at most \(\pi\), so
  strict counting gives no eigenvalue below \(K^2\).
- If \(K>\pi/(1-\rho)\) and \(0<\rho<39/50\), use the ratio-sharp theorem.
- If \(K>\pi/(1-\rho)\) and \(39/50\leq\rho<1\), use the existing optical
  theorem.

This cover is disjoint and exhaustive. Dilation gives arbitrary \(r,R\).

No finite staircase, event-state theorem, numerical root isolation, interval
certificate, or executable ledger is a premise of this proof.
