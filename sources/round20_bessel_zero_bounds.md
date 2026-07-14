# Source Card: Round 20 Exact-Order Lorch Specializations

Status: **qualified statement-level source audit and exact algebra completed
on 2026-07-14**.

This card authorizes exactly

\[
 j_{13/2,1}>\frac{39}{4},\qquad
 j_{15/2,1}>\frac{54}{5},\qquad
 j_{17/2,1}>\frac{71}{6}.
 \tag{Z}
\]

The first two inequalities are used in the Round 20 proof through
\(k_8\).  The third is used only to audit the next prospective angular
wall toward \(k_9\); it does not by itself prove that extension.

## 1. Authenticated primary statement

The source dependency is the already authenticated card
`sources/lorch_bessel_zeros.md`, SHA-256

```
85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4
```

for Lee Lorch, "Some Inequalities for the First Positive Zeros of Bessel
Functions," *SIAM Journal on Mathematical Analysis* **24**(3) (1993),
814--823, DOI 10.1137/0524050.  The publisher abstract identifies
\(j_{\nu,1}\) as the first positive zero of \(J_\nu\), gives the scope
\(-1<\nu<\infty\), and states

\[
 j_{\nu,1}^{\,2}>
 \frac{24(\nu+1)^2}
 {1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
 -2(\nu^2-1).
 \tag{L2}
\]

The body of the article remains access-controlled in the audited
environment.  This is therefore a statement-level use of the formula
printed in the primary publisher abstract, not an independent
reconstruction of Lorch's proof.

## 2. Half-integer reduction

Put \(\nu=\ell+1/2\), where \(\ell\in\mathbb N_0\).  Since

\[
 (\ell+2)(\ell+6)-\ell^2=4(2\ell+3)>0,
\]

the denominator in (L2) is positive.  Rationalizing it gives the exact
lower square

\[
 \boxed{
 R_\ell=
 \frac{3(2\ell+3)\sqrt{(\ell+2)(\ell+6)}
       -2\ell^2+\ell+6}{4}}
 \quad\text{with}\quad
 j_{\ell+1/2,1}^{\,2}>R_\ell.
 \tag{1}
\]

No numerical approximation is used in the following three
specializations.

## 3. Order \(13/2\): angular channel \(\ell=6\)

Equation (1) gives

\[
 R_6=45\sqrt6-15.
\]

The comparison with \((39/4)^2\) is equivalent to

\[
 240\sqrt6>587.
\]

Both sides are positive, and

\[
 240^2\cdot6-587^2=1031>0.
\]

Thus

\[
 \boxed{j_{13/2,1}>\frac{39}{4}}.
 \tag{2}
\]

## 4. Order \(15/2\): angular channel \(\ell=7\)

Equation (1) gives

\[
 R_7=\frac{153\sqrt{13}-85}{4}.
\]

The comparison with \((54/5)^2\) is equivalent to

\[
 3825\sqrt{13}>13789.
\]

Both sides are positive, and

\[
 3825^2\cdot13-13789^2=61604>0.
\]

Consequently

\[
 \boxed{j_{15/2,1}>\frac{54}{5}}.
 \tag{3}
\]

## 5. Order \(17/2\): angular channel \(\ell=8\)

Equation (1) gives

\[
 R_8=\frac{57}{2}(\sqrt{35}-1).
\]

The comparison with \((71/6)^2\) is equivalent to

\[
 1026\sqrt{35}>6067.
\]

Both sides are positive, and

\[
 1026^2\cdot35-6067^2=35171>0.
\]

Therefore

\[
 \boxed{j_{17/2,1}>\frac{71}{6}}.
 \tag{4}
\]

## 6. Exact scope of transfer to the shell argument

The inherited DLMF identity

\[
 \mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
 \qquad x>0,
\]

identifies these as unit-ball first radial zeros.  Applying them to a
shell still requires the project's separate internal, fixed-channel
zero-extension/min--max comparison

\[
 q_{\ell,1}^{\rm shell}(\rho)^2
 \ge j_{\ell+1/2,1}^2.
\]

Subject to that internal lemma, (2)--(4) give strict shell exclusions
through the displayed rational walls.  Equality at a rational wall is
excluded because the Lorch inequalities are strict.

Lorch supplies none of the following:

- a zero bound for a shell Bessel cross-product;
- shell-to-ball domain monotonicity or the fixed-channel min--max map;
- a second or higher radial zero bound;
- angular multiplicities or a spectral counting formula;
- a Weyl payment, endpoint estimate, or residual-mask subtraction.

In particular, the order-\(17/2\) specialization controls only the first
\(\ell=8\) unit-ball zero.  It cannot repair a failure caused by second
radial channels at lower angular orders.

## Verdict

**PASS for exactly (Z).  First unsupported implication: none inside the
three declared exact-order specializations.**  Any further order, radial
index, or shell statement requires a new explicit audit rather than an
implicit enlargement of this card.
