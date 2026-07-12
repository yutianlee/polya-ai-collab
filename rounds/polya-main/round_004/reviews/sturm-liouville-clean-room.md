# Clean-room review: separated shell spectrum and strict phase count

## Verdict

**PASS.** The four-part theorem in SHELL-sturm-liouville-completeness is supported. The unitary transform, closed form and operator domains, norm-compactness of the infinite direct-sum resolvent, radial completeness and simplicity, Bessel determinant (including its sign normalization), exclusion of zero energy, phase indexing, strict endpoint convention, angular multiplicity, and treatment of cross-\(\ell\) coincidences all reconstruct without a gap.

The phase representation, strict phase monotonicity, and its two endpoint limits are used only as the explicitly permitted prior dependencies. All operator and determinant assertions are independently derived below. I did not read the Round 4 incumbent or another Round 4 review.

## 1. Hilbert-space unitary

For \(f\in L^2(\Omega)\), define its spherical coefficients for almost every \(r\) by

\[
R_{\ell m}(r)
=\int_{\mathbb S^2}f(r,\omega)
\overline{Y_{\ell m}(\omega)}\,d\omega,
\qquad
u_{\ell m}(r)=rR_{\ell m}(r).
\]

Parseval on \(\mathbb S^2\), followed by Tonelli, gives

\[
\begin{aligned}
\|f\|_{L^2(\Omega)}^2
&=\int_\rho^1
\sum_{\ell,m}|R_{\ell m}(r)|^2r^2\,dr\\
&=\sum_{\ell,m}\int_\rho^1|u_{\ell m}(r)|^2\,dr.
\end{aligned}
\]

Thus the displayed transform is an isometry. Conversely, from any square-summable family \((u_{\ell m})\), the partial sums

\[
f_L(r,\omega)
=\frac1r\sum_{\ell\le L}\sum_m
u_{\ell m}(r)Y_{\ell m}(\omega)
\]

are Cauchy in \(L^2(\Omega)\), with norm difference exactly the corresponding direct-sum norm. Their limit maps back to the given family, proving surjectivity. Hence

\[
L^2(\Omega)\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}L^2(\rho,1)
\]

unitarily.

Because \(0<\rho<1\), both \(r\) and \(1/r\) belong to
\(W^{1,\infty}(\rho,1)\). Multiplication by either is bounded on
\(H^1(\rho,1)\), and it preserves both zero endpoint traces. Therefore

\[
R\in H_0^1(\rho,1)
\quad\Longleftrightarrow\quad
u=rR\in H_0^1(\rho,1).
\]

This removes any endpoint ambiguity in the change of radial unknown.

## 2. Exact transformed form and its closure

For a finite smooth spherical-harmonic expansion, polar coordinates and
orthogonality give

\[
\mathfrak q[f]
=\sum_{\ell,m}\int_\rho^1
\left(r^2|R_{\ell m}'|^2
+\ell(\ell+1)|R_{\ell m}|^2\right)dr.
\]

The radial identity in the packet is exact, but it requires the Dirichlet
traces. If \(u=rR\), then

\[
r^2|R'|^2
=\left|u'-\frac ur\right|^2
=|u'|^2-\frac{(|u|^2)'}r+\frac{|u|^2}{r^2}.
\]

Since

\[
\frac{(|u|^2)'}r
=\left(\frac{|u|^2}{r}\right)'
+\frac{|u|^2}{r^2},
\]

integration yields

\[
\int_\rho^1r^2|R'|^2\,dr
=\int_\rho^1|u'|^2\,dr
-\left[\frac{|u|^2}{r}\right]_\rho^1
=\int_\rho^1|u'|^2\,dr.
\]

Also

\[
\ell(\ell+1)|R|^2
=\frac{\ell(\ell+1)}{r^2}|u|^2.
\]

Consequently the form on finite expansions is the orthogonal sum of

\[
\mathfrak a_\ell[u]
=\int_\rho^1
\left(|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak a_\ell)=H_0^1(\rho,1).
\]

Its closure has exactly the domain

\[
\mathcal D_{\mathrm{form}}
=\left\{(u_{\ell m}):
\begin{array}{l}
u_{\ell m}\in H_0^1(\rho,1),\\[2mm]
\displaystyle
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+
\mathfrak a_\ell[u_{\ell m}]\bigr)<\infty
\end{array}
\right\}.
\]

Indeed, a form-Cauchy sequence gives componentwise \(H_0^1\) limits and
the displayed square summability. Conversely, first truncating in
\((\ell,m)\) and then approximating the finitely many radial components
by \(C_c^\infty(\rho,1)\) proves density in this norm. Therefore the
domain is neither missing a summability condition nor enlarged to an
unrestricted Cartesian product.

By uniqueness of the operator associated with a closed semibounded
form, this proves the unitary form decomposition of the Friedrichs
Dirichlet Laplacian.

## 3. Block and global operator domains

For fixed \(\ell\), the potential

\[
V_\ell(r)=\frac{\ell(\ell+1)}{r^2}
\]

is real and bounded (indeed continuous) on \([\rho,1]\). The operator
associated with \(\mathfrak a_\ell\) is therefore

\[
L_\ell=-\frac{d^2}{dr^2}+V_\ell,
\qquad
D(L_\ell)=H^2(\rho,1)\cap H_0^1(\rho,1).
\]

The operator associated with the orthogonal sum form acts componentwise.
A vector belongs to its domain exactly when each component belongs to
\(D(L_\ell)\) and the componentwise image is square summable. Including
the ambient Hilbert norm explicitly, this is

\[
\mathcal D_{\mathrm{op}}
=\left\{(u_{\ell m}):
\begin{array}{l}
u_{\ell m}\in H^2(\rho,1)\cap H_0^1(\rho,1),\\[2mm]
\displaystyle
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+
\|L_\ell u_{\ell m}\|_2^2\bigr)<\infty
\end{array}
\right\}.
\]

Thus, with both domains understood exactly,

\[
H_\Omega\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}L_\ell.
\]

## 4. Infinite-direct-sum compactness

Each block has compact resolvent because

\[
H_0^1(\rho,1)\hookrightarrow L^2(\rho,1)
\]

is compact. This alone would not prove compactness of the infinite
orthogonal sum.

For \(r\le1\),

\[
\mathfrak a_\ell[u]\ge
\ell(\ell+1)\|u\|_2^2,
\]

so

\[
\|(L_\ell+1)^{-1}\|
\le\frac1{1+\ell(\ell+1)}.
\]

Let \(P_L\) project onto all channels with \(\ell\le L\). The operator

\[
P_L(H_\Omega+1)^{-1}
\]

is a finite direct sum of compact block resolvents and hence compact.
For the complement,

\[
\|(I-P_L)(H_\Omega+1)^{-1}\|
\le
\sup_{\ell>L}\frac1{1+\ell(\ell+1)}
\longrightarrow0.
\]

The global resolvent is therefore a norm limit of compact operators and
is compact.

## 5. Radial spectrum, positivity, simplicity, and global completeness

Regular one-dimensional Dirichlet Sturm--Liouville theory gives each
\(L_\ell\) a complete orthonormal eigenbasis and a sequence of real
simple eigenvalues tending to \(+\infty\). Their positivity is strict,
since the interval Poincaré inequality gives

\[
\mathfrak a_\ell[u]\ge
\int_\rho^1|u'|^2\,dr
\ge\frac{\pi^2}{(1-\rho)^2}\|u\|_2^2.
\]

In particular zero is not a radial eigenvalue, including for
\(\ell=0\).

Simplicity can also be seen directly. Two eigenfunctions for the same
\(\lambda\) both vanish at \(r=\rho\); their initial derivative data
are proportional, and uniqueness for the regular second-order ODE makes
the functions proportional.

Let \(u_{\ell,n}\) be normalized radial eigenfunctions. Under the unitary
inverse, the coordinate basis vectors become

\[
\Phi_{\ell mn}(r,\omega)
=\frac{u_{\ell,n}(r)}rY_{\ell m}(\omega).
\]

Their norms and pairwise inner products are exactly those of the
direct-sum coordinate vectors, so they are orthonormal. Completeness in
each radial block, then completeness of the Hilbert direct sum, proves
that all \(\Phi_{\ell mn}\) together form a complete eigenbasis of
\(L^2(\Omega)\).

## 6. Bessel determinant and its sign normalization

Write

\[
\nu=\ell+\frac12,\qquad \lambda=k^2,\qquad k>0.
\]

For the physical radial factor \(R=u/r\), the radial equation is

\[
-R''-\frac2rR'
+\frac{\ell(\ell+1)}{r^2}R=k^2R.
\]

Its general solution is

\[
R(r)=r^{-1/2}
\bigl(c_1J_\nu(kr)+c_2Y_\nu(kr)\bigr),
\]

equivalently

\[
u(r)=\sqrt r\,
\bigl(c_1J_\nu(kr)+c_2Y_\nu(kr)\bigr).
\]

Since \(r\ne0\) at both endpoints, the two Dirichlet equations for
\((c_1,c_2)\) have coefficient matrix

\[
\begin{pmatrix}
J_\nu(\rho k)&Y_\nu(\rho k)\\
J_\nu(k)&Y_\nu(k)
\end{pmatrix}.
\]

Its determinant is precisely

\[
F_{\nu,\rho}(k)
=J_\nu(\rho k)Y_\nu(k)
-Y_\nu(\rho k)J_\nu(k).
\]

Thus a nonzero coefficient vector exists exactly when \(F_{\nu,\rho}(k)=0\).
The Wronskian

\[
J_\nu(x)Y_\nu'(x)-J_\nu'(x)Y_\nu(x)
=\frac2{\pi x}
\]

also shows that \(J_\nu,Y_\nu\) cannot vanish simultaneously at either
positive endpoint. Cases where \(J_\nu\) vanishes at both distinct
endpoints, or \(Y_\nu\) does, are nevertheless included correctly by
the determinant criterion.

For the sign and normalization, define

\[
s_\ell(r,k)
=\frac{\pi\sqrt\rho}{2}\sqrt r\,
\left[
J_\nu(\rho k)Y_\nu(kr)
-Y_\nu(\rho k)J_\nu(kr)
\right].
\]

The bracket vanishes at \(r=\rho\). At that endpoint its \(r\)-derivative
is

\[
k\left[J_\nu(\rho k)Y_\nu'(\rho k)
-Y_\nu(\rho k)J_\nu'(\rho k)\right]
=\frac2{\pi\rho}.
\]

Multiplying by

\[
\frac{\pi\sqrt\rho}{2}\sqrt\rho
\]

gives

\[
s_\ell(\rho,k)=0,\qquad
\partial_rs_\ell(\rho,k)=1.
\]

At the right endpoint,

\[
s_\ell(1,k)=\frac{\pi\sqrt\rho}{2}F_{\nu,\rho}(k),
\]

so the determinant sign and the positive normalization in the packet
are correct.

## 7. Simplicity of every positive determinant zero

Differentiate

\[
(L_\ell-k^2)s_\ell=0
\]

with respect to \(k\). If \(v=\partial_ks_\ell\), then

\[
(L_\ell-k^2)v=2ks_\ell.
\]

The initial normalization is independent of \(k\), so

\[
v(\rho,k)=\partial_rv(\rho,k)=0.
\]

At a determinant root, \(s_\ell(1,k)=0\). Lagrange's identity gives

\[
\begin{aligned}
2k\int_\rho^1s_\ell(r,k)^2\,dr
&=\left[v\,\partial_rs_\ell
-s_\ell\,\partial_rv\right]_\rho^1\\
&=\partial_ks_\ell(1,k)\,
\partial_rs_\ell(1,k).
\end{aligned}
\]

The right side is strictly positive. Hence
\(\partial_ks_\ell(1,k)\ne0\), and because the proportionality factor
between \(s_\ell(1,k)\) and \(F_{\nu,\rho}(k)\) is a fixed positive
constant, every positive zero of \(F_{\nu,\rho}\) is simple.

This is a separate assertion from one-dimensional eigenspace
simplicity, and both have now been justified.

## 8. Zero energy and the \(n=0\) phase level

At \(k=0\), solutions of \(L_\ell s=0\) are linear combinations of
\(r^{\ell+1}\) and \(r^{-\ell}\). Applying

\[
s(\rho,0)=0,\qquad s'(\rho,0)=1
\]

gives

\[
s_\ell(r,0)
=\frac{r^{\ell+1}-\rho^{2\ell+1}r^{-\ell}}
{(2\ell+1)\rho^\ell},
\]

and therefore

\[
s_\ell(1,0)
=\frac{\rho^{-\ell}-\rho^{\ell+1}}{2\ell+1}>0.
\]

This agrees with strict operator positivity and proves directly that
zero energy is not a Dirichlet eigenvalue. Taking the continuous
\(k\downarrow0\) limit in the normalized endpoint formula gives

\[
\lim_{k\downarrow0}F_{\nu,\rho}(k)
=\frac{\rho^{-\nu}-\rho^\nu}{\pi\nu}>0.
\]

Thus \(F_{\nu,\rho}\), although written for \(k>0\), has a nonzero
finite right limit. The phase value \(0\) occurs only as \(k\downarrow0\)
and is not a determinant zero. No rescaling which artificially inserts
a zero at \(k=0\) may be used in the spectral enumeration.

## 9. Phase factorization, indexing, and strict endpoints

Under the permitted exact phase representation, write

\[
J_\nu(x)=M_\nu(x)\cos\theta_\nu(x),\qquad
Y_\nu(x)=M_\nu(x)\sin\theta_\nu(x),
\]

where

\[
M_\nu(x)=\sqrt{J_\nu(x)^2+Y_\nu(x)^2}>0
\]

and the argument is chosen as the continuous real lift. Substitution
into the determinant, with

\[
\Psi_{\nu,\rho}(k)
=\theta_\nu(k)-\theta_\nu(\rho k),
\]

gives the sign-consistent identity

\[
F_{\nu,\rho}(k)
=M_\nu(\rho k)M_\nu(k)
\sin\Psi_{\nu,\rho}(k).
\]

Therefore its positive zeros are exactly the positive solutions of

\[
\Psi_{\nu,\rho}(k)\in\pi\mathbb Z.
\]

The permitted phase results say that \(\Psi_{\nu,\rho}\) is continuous
and strictly increasing on \((0,\infty)\), with

\[
\Psi_{\nu,\rho}(0+)=0,\qquad
\Psi_{\nu,\rho}(k)\longrightarrow\infty.
\]

Consequently, for every \(n\ge1\), there is exactly one
\(k_{\ell,n}>0\) such that

\[
\Psi_{\ell+1/2,\rho}(k_{\ell,n})=n\pi.
\]

There is no \(n=0\) root by the preceding zero-energy calculation. By
strict monotonicity, for \(K>0\),

\[
k_{\ell,n}<K
\quad\Longleftrightarrow\quad
n\pi<\Psi_{\ell+1/2,\rho}(K).
\]

At an endpoint with \(\Psi(K)=m\pi\), the admissible positive integers
are \(1,\ldots,m-1\), so the channel count is \(m-1\), not \(m\). For
\(K=0\), defining \(\Psi(0)=0\) by its right limit makes both channel
counts zero. Thus the strict endpoint convention is valid for every
\(K\ge0\).

## 10. Angular multiplicity, coincidences, and finiteness

For fixed \((\ell,n)\), the same radial eigenvalue occurs in each of the
\(2\ell+1\) mutually orthogonal spherical-harmonic channels
\(m=-\ell,\ldots,\ell\). Radial simplicity makes each such coordinate
one-dimensional.

If a numerical eigenvalue is shared by different \(\ell\)'s (or by
several distinct channel labels), the direct-sum decomposition makes
the associated subspaces orthogonal. Their dimensions add. The proof
does not assert, and does not need, the false general principle that
distinct centrifugal potentials prohibit accidental coincidences.

The angular sum is finite at every \(K\). Indeed,

\[
\lambda_{\ell,n}
=\mathfrak a_\ell[u_{\ell,n}]
\ge\ell(\ell+1),
\]

for normalized \(u_{\ell,n}\). Hence a strict eigenvalue count below
\(K^2\) receives no contribution whenever

\[
\ell(\ell+1)\ge K^2.
\]

Only finitely many \(\ell\)'s remain, and each regular radial block has
only finitely many eigenvalues below \(K^2\).

Counting the complete direct-sum eigenbasis with multiplicity therefore
gives

\[
N_D(\Omega,K^2)
=\sum_{\ell=0}^{\infty}(2\ell+1)
\#\{n\ge1:k_{\ell,n}<K\},
\]

and substitution of the strict phase equivalence gives

\[
N_D(\Omega,K^2)
=\sum_{\ell=0}^{\infty}(2\ell+1)
\#\{n\ge1:n\pi<
\Psi_{\ell+1/2,\rho}(K)\}.
\]

Both sums include accidental cross-\(\ell\) coincidences with their full
added multiplicity and exclude every eigenfrequency equal to \(K\).

## 11. Adversarial endpoint checklist

- **Global domains:** the form domain has componentwise
  \(H_0^1\) regularity plus form-norm summability; the operator domain
  has componentwise \(H^2\cap H_0^1\) regularity plus graph-norm
  summability.
- **Infinite sum:** compactness is obtained from finite angular
  truncations and a resolvent tail converging to zero in norm, not from
  blockwise compactness alone.
- **\(\ell=0\):** Poincaré positivity still excludes zero, while the
  determinant uses \(\nu=1/2\) without modification.
- **\(k=0\):** the normalized zero-energy endpoint and the unscaled
  determinant limit are strictly positive.
- **Determinant sign:** the positive Wronskian gives
  \(s_\ell'( \rho,k)=1\) and
  \(s_\ell(1,k)=(\pi\sqrt\rho/2)F_{\nu,\rho}(k)\).
- **Endpoint Bessel zeros:** the \(2\times2\) determinant criterion
  remains valid if the same Bessel species vanishes at both radii; the
  Wronskian rules out simultaneous \(J_\nu,Y_\nu\) vanishing at one
  radius.
- **Positive-root simplicity:** Lagrange's identity proves a nonzero
  derivative of the unscaled determinant at every positive root.
- **Spectral endpoint:** \(k_{\ell,n}=K\) is excluded in both the
  eigenvalue count and the phase count.
- **Angular multiplicity:** it is exactly
  \(\dim\mathcal H_\ell(\mathbb S^2)=2\ell+1\).
- **Cross-\(\ell\) collisions:** orthogonal eigenspace dimensions add;
  no noncollision claim is used.

No unsupported implication remains in the stated theorem.
