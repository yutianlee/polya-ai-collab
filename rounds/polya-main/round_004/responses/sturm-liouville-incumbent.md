# Round 4 Incumbent: Separated Shell Spectrum

## Verdict

For every fixed $0<\rho<1$, the Dirichlet Laplacian on the spherical shell is unitarily equivalent to the orthogonal direct sum of regular one-dimensional Dirichlet Schrödinger operators

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
$$

each repeated $2\ell+1$ times. This proves completeness of the cross-product spectrum, radial simplicity, positivity, and the exact strict phase-count identity.

## 1. Spherical-harmonic decomposition

Write $x=r\omega$, with

$$
\rho<r<1,\qquad \omega\in\mathbb S^2,\qquad
dx=r^2\,dr\,d\omega.
$$

Choose an orthonormal basis $(Y_{\ell m})$ satisfying

$$
-\Delta_{\mathbb S^2}Y_{\ell m}
=\ell(\ell+1)Y_{\ell m},
\qquad -\ell\le m\le\ell.
$$

For $f\in L^2(\Omega)$, let

$$
R_{\ell m}(r)
=
\int_{\mathbb S^2}
f(r,\omega)\overline{Y_{\ell m}(\omega)}\,d\omega.
$$

Fubini and Parseval give

$$
\|f\|_{L^2(\Omega)}^2
=
\sum_{\ell,m}
\int_\rho^1|R_{\ell m}(r)|^2r^2\,dr.
$$

The substitution

$$
u_{\ell m}(r)=rR_{\ell m}(r)
$$

is unitary into the unweighted radial space. Since $\rho>0$, multiplication by $r$ and $1/r$ are bounded isomorphisms of $H_0^1(\rho,1)$.

## 2. Exact form decomposition

The Dirichlet form is

$$
\mathfrak q[f]=\int_\Omega|\nabla f|^2\,dx,
\qquad D(\mathfrak q)=H_0^1(\Omega).
$$

For finite smooth harmonic expansions,

$$
\mathfrak q[f]
=
\sum_{\ell,m}
\int_\rho^1
\left(
r^2|R_{\ell m}'|^2
+\ell(\ell+1)|R_{\ell m}|^2
\right)dr.
$$

Because $u=rR$ and both endpoint traces vanish,

$$
\int_\rho^1r^2|R'|^2\,dr
=
\int_\rho^1|u'|^2\,dr.
$$

Hence the closed form becomes

$$
\mathfrak q[f]
=
\sum_{\ell,m}
\mathfrak a_\ell[u_{\ell m}],
$$

where

$$
\mathfrak a_\ell[u]
=
\int_\rho^1
\left(
|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2
\right)dr,
\qquad D(\mathfrak a_\ell)=H_0^1(\rho,1).
$$

Closing finite angular truncations gives the precise global form domain

$$
\left\{
(u_{\ell m}):
u_{\ell m}\in H_0^1(\rho,1),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\mathfrak a_\ell[u_{\ell m}]\bigr)<\infty
\right\}.
$$

The associated block operator is

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad
D(L_\ell)=H^2(\rho,1)\cap H_0^1(\rho,1),
$$

and the full operator is

$$
H_\Omega\simeq
\bigoplus_{\ell=0}^\infty
\bigoplus_{m=-\ell}^{\ell}L_\ell
$$

with domain

$$
\left\{
(u_{\ell m}):
u_{\ell m}\in D(L_\ell),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\|L_\ell u_{\ell m}\|_2^2\bigr)<\infty
\right\}.
$$

## 3. Compactness and completeness

Each $L_\ell$ has compact resolvent because

$$
H_0^1(\rho,1)\hookrightarrow L^2(\rho,1)
$$

is compact. That alone does not prove compactness of the infinite direct sum. The missing uniform estimate is

$$
L_\ell\ge\ell(\ell+1),
$$

because $r\le1$. Therefore

$$
\|(L_\ell+1)^{-1}\|
\le\frac1{1+\ell(\ell+1)}
\longrightarrow0.
$$

The full resolvent is the norm limit of its finite-$\ell$ truncations. Each truncation is a finite direct sum of compact operators, so the full resolvent is compact.

Regular Dirichlet Sturm--Liouville theory now gives, in every channel,

$$
0<\lambda_{\ell,1}<\lambda_{\ell,2}<\cdots\to\infty
$$

and a complete orthonormal radial eigenbasis. Positivity can also be seen directly from

$$
\mathfrak a_\ell[u]
\ge
\int_\rho^1|u'|^2\,dr
\ge
\frac{\pi^2}{(1-\rho)^2}\|u\|_2^2.
$$

In particular, $k=0$ is not an eigenfrequency.

Radial eigenvalues are simple: a nonzero solution vanishing at $\rho$ has nonzero initial derivative, and two such solutions for the same eigenvalue have proportional initial data. ODE uniqueness makes them proportional.

Consequently,

$$
\Phi_{\ell mn}(r,\omega)
=\frac{u_{\ell,n}(r)}rY_{\ell m}(\omega)
$$

is a complete orthonormal eigenbasis of $L^2(\Omega)$.

## 4. Cross-product determinant

Let $\lambda=k^2$ with $k>0$ and $\nu=\ell+1/2$. The original radial equation has general solution

$$
R(r)=r^{-1/2}
\bigl(c_1J_\nu(kr)+c_2Y_\nu(kr)\bigr).
$$

The endpoint conditions give

$$
\begin{pmatrix}
J_\nu(\rho k)&Y_\nu(\rho k)\\
J_\nu(k)&Y_\nu(k)
\end{pmatrix}
\begin{pmatrix}c_1\\c_2\end{pmatrix}=0.
$$

A nonzero coefficient vector exists exactly when

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)
-Y_\nu(\rho k)J_\nu(k)
=0.
$$

Thus the positive cross-product zeros are exactly the radial eigenfrequencies. Neither endpoint pair $J_\nu,Y_\nu$ can vanish simultaneously because their Wronskian is nonzero. Both endpoint values of $J_\nu$ may vanish simultaneously for special $(\rho,k)$; this simply produces the genuine pure-$J_\nu$ eigenfunction and does not break the determinant argument.

For completeness, positive roots of the determinant are simple. Let $s_\ell(r,k)$ be the left-normalized transformed solution

$$
(L_\ell-k^2)s_\ell=0,\qquad
s_\ell(\rho,k)=0,\qquad
\partial_rs_\ell(\rho,k)=1.
$$

The Bessel Wronskian gives the exact representation

$$
s_\ell(r,k)
=
\frac{\pi\sqrt\rho}{2}\sqrt r
\left[
J_\nu(\rho k)Y_\nu(kr)
-Y_\nu(\rho k)J_\nu(kr)
\right],
$$

and therefore

$$
s_\ell(1,k)=\frac{\pi\sqrt\rho}{2}F_{\nu,\rho}(k).
$$

At an eigenfrequency, differentiation in $k$ and Lagrange's identity yield

$$
\partial_rs_\ell(1,k)\,
\partial_ks_\ell(1,k)
=
2k\int_\rho^1s_\ell(r,k)^2\,dr>0.
$$

Thus $\partial_ks_\ell(1,k)\ne0$, and every positive root of $F_{\nu,\rho}$ is simple.

The zero-energy characteristic value is

$$
s_\ell(1,0)
=
\frac{\rho^{-\ell}-\rho^{\ell+1}}{2\ell+1}>0.
$$

Equivalently,

$$
\lim_{k\downarrow0}F_{\nu,\rho}(k)
=
\frac{\rho^{-\nu}-\rho^\nu}{\pi\nu}>0.
$$

The phase level $n=0$ at $k\to0+$ is therefore not a determinant root.

## 5. Multiplicity and cross-channel equality

For fixed $(\ell,n)$, the radial eigenvalue occurs in each of the $2\ell+1$ angular channels. Therefore it contributes multiplicity $2\ell+1$.

No absence of cross-$\ell$ degeneracy is required. If

$$
\lambda_{\ell,n}=\lambda_{\ell',n'}
\qquad(\ell\ne\ell'),
$$

the two eigenspaces lie in orthogonal spherical-harmonic sectors, and the full multiplicity is the sum of their dimensions.

In fact, cross-$\ell$ equality can occur. Compare $\lambda_{0,2}(\rho)$ and $\lambda_{7,1}(\rho)$. Since

$$
\lambda_{0,2}(\rho)=\frac{4\pi^2}{(1-\rho)^2},
$$

at $\rho=1/10$ the lower bound

$$
\lambda_{7,1}
\ge\frac{\pi^2}{(1-\rho)^2}+56
>\lambda_{0,2}
$$

holds. At $\rho=4/5$, the first Dirichlet sine trial function gives

$$
\lambda_{7,1}
\le\frac{\pi^2}{(1-\rho)^2}+\frac{56}{\rho^2}
=25\pi^2+\frac{175}{2}
<100\pi^2
=\lambda_{0,2}.
$$

After an affine change to a fixed interval, the min--max forms depend continuously on $\rho$. Hence an intermediate shell radius has

$$
\lambda_{7,1}(\rho)=\lambda_{0,2}(\rho).
$$

This disproves the old shortcut that different centrifugal potentials forbid accidental equality; the direct-sum count remains correct.

Because

$$
\lambda_{\ell,n}\ge\ell(\ell+1),
$$

only finitely many angular channels contribute below any fixed $K^2$. Hence

$$
N_D(\Omega,K^2)
=
\sum_{\ell=0}^\infty(2\ell+1)
\#\{n\ge1:k_{\ell,n}<K\}.
$$

## 6. Exact strict phase count

The proved phase factorization and monotonicity give

$$
F_{\nu,\rho}(k)=0
\quad\Longleftrightarrow\quad
\Psi_{\nu,\rho}(k)\in\pi\mathbb Z,
$$

with

$$
\Psi_{\nu,\rho}(0+)=0,\qquad
\Psi_{\nu,\rho}'(k)>0,\qquad
\Psi_{\nu,\rho}(k)\to\infty.
$$

Thus the $n$th positive root is characterized by

$$
\Psi_{\ell+1/2,\rho}(k_{\ell,n})=n\pi,
\qquad n\ge1.
$$

For every $K>0$,

$$
k_{\ell,n}<K
\quad\Longleftrightarrow\quad
n\pi<\Psi_{\ell+1/2,\rho}(K).
$$

Therefore

$$
\boxed{
N_D(\Omega,K^2)
=
\sum_{\ell=0}^\infty(2\ell+1)
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
}
$$

If $K$ is itself an eigenfrequency with $\Psi(K)=m\pi$, strict counting excludes that root and the channel contributes $m-1$. Simultaneous equality in several $\ell$ channels is handled independently in every orthogonal summand, and all excluded multiplicities add correctly.

## Scope

This proves the separated spectrum, determinant formula, and strict phase-count bridge. It does not prove a finite-window Pólya inequality, $\rho$-uniformity, or any numerical certificate.
