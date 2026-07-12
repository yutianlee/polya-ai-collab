# Lemma Packet: Separated Shell Spectrum and Strict Phase Count

Obligations:

- SHELL-sturm-liouville-completeness
- SHELL-cross-product-formula
- SHELL-count-floor-identity

## Exact theorem

Fix

$$
0<\rho<1,\qquad
\Omega=A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\}.
$$

Let $H_\Omega=-\Delta_\Omega^D$ be the Friedrichs operator associated with

$$
\mathfrak q[f]=\int_\Omega|\nabla f|^2\,dx,
\qquad D(\mathfrak q)=H_0^1(\Omega).
$$

For $\ell\in\mathbb N_0$, define

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad
D(L_\ell)=H^2(\rho,1)\cap H_0^1(\rho,1).
$$

The target theorem has four parts.

### A. Unitary direct-sum decomposition

For any orthonormal spherical-harmonic basis

$$
-\Delta_{\mathbb S^2}Y_{\ell m}
=\ell(\ell+1)Y_{\ell m},
\qquad -\ell\le m\le\ell,
$$

the map

$$
f(r,\omega)\longmapsto
u_{\ell m}(r)
:=
r\int_{\mathbb S^2}
f(r,\omega)\overline{Y_{\ell m}(\omega)}\,d\omega
$$

is unitary from $L^2(\Omega)$ onto

$$
\bigoplus_{\ell=0}^\infty
\bigoplus_{m=-\ell}^{\ell}L^2(\rho,1),
$$

and

$$
\boxed{
H_\Omega\simeq
\bigoplus_{\ell=0}^\infty
\bigoplus_{m=-\ell}^{\ell}L_\ell.
}
$$

The exact global form domain is

$$
\left\{
(u_{\ell m}):
u_{\ell m}\in H_0^1(\rho,1),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\mathfrak a_\ell[u_{\ell m}]\bigr)<\infty
\right\},
$$

where

$$
\mathfrak a_\ell[u]
=
\int_\rho^1
\left(
|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2
\right)dr.
$$

The exact global operator domain is

$$
\left\{
(u_{\ell m}):
u_{\ell m}\in D(L_\ell),\
\sum_{\ell,m}
\bigl(\|u_{\ell m}\|_2^2+\|L_\ell u_{\ell m}\|_2^2\bigr)<\infty
\right\}.
$$

### B. Completeness, positivity, and radial simplicity

Each $L_\ell$ has simple eigenvalues

$$
0<\lambda_{\ell,1}<\lambda_{\ell,2}<\cdots\to\infty
$$

and a complete orthonormal eigenbasis $(u_{\ell,n})_{n\ge1}$ of $L^2(\rho,1)$. The functions

$$
\Phi_{\ell mn}(r,\omega)
=\frac{u_{\ell,n}(r)}rY_{\ell m}(\omega)
$$

form a complete orthonormal eigenbasis of $L^2(\Omega)$.

The global resolvent is compact. It is not enough to cite compactness block by block; one must use

$$
L_\ell\ge\ell(\ell+1)
$$

and hence

$$
\|(L_\ell+1)^{-1}\|
\le\frac1{1+\ell(\ell+1)}
\longrightarrow0.
$$

### C. Bessel cross-product characterization

For

$$
\nu=\ell+\frac12,\qquad k>0,
$$

set

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)
-Y_\nu(\rho k)J_\nu(k).
$$

Then

$$
\boxed{
\lambda_{\ell,n}=k_{\ell,n}^2
\quad\Longleftrightarrow\quad
F_{\ell+1/2,\rho}(k_{\ell,n})=0,
\qquad k_{\ell,n}>0.
}
$$

The positive zeros are simple within each fixed $\ell$ channel. The value $k=0$ is not an eigenfrequency and is not included in the determinant statement.

### D. Multiplicity and strict phase count

For every $K\ge0$,

$$
\boxed{
N_D(\Omega,K^2)
=
\sum_{\ell=0}^\infty(2\ell+1)
\#\{n\ge1:k_{\ell,n}<K\}.
}
$$

If

$$
\Psi_{\nu,\rho}(k)
=\theta_\nu(k)-\theta_\nu(\rho k)
$$

is the already-proved increasing phase with

$$
\Psi_{\nu,\rho}(0+)=0,\qquad
\Psi_{\nu,\rho}(k)\to\infty,
$$

then

$$
k_{\ell,n}<K
\quad\Longleftrightarrow\quad
n\pi<\Psi_{\ell+1/2,\rho}(K),
$$

so

$$
\boxed{
N_D(\Omega,K^2)
=
\sum_{\ell=0}^\infty(2\ell+1)
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
}
$$

At a spectral endpoint $\Psi(K)=m\pi$, the channel count is $m-1$, not $m$. The ordinary floor is only an upper bound there.

## Permitted dependencies

- CONV-strict-counting
- SHELL-exact-phase-rep
- SHELL-phase-monotonicity
- SHELL-angular-cutoff
- the standard spherical-harmonic eigenbasis on $\mathbb S^2$
- elementary regular one-dimensional Dirichlet Sturm--Liouville theory
- the Bessel equation and the Wronskian of $J_\nu,Y_\nu$

The proof must reconstruct the operator and form domains rather than cite a separation ansatz as completeness.

## Required reconstruction

### 1. Hilbert-space decomposition

Use

$$
dx=r^2\,dr\,d\omega
$$

and Parseval on $\mathbb S^2$ to obtain

$$
\|f\|_{L^2(\Omega)}^2
=
\sum_{\ell,m}\int_\rho^1
|R_{\ell m}(r)|^2r^2\,dr.
$$

Multiplication by $r$,

$$
u_{\ell m}=rR_{\ell m},
$$

is unitary from $L^2((\rho,1),r^2dr)$ to $L^2(\rho,1)$. Because $\rho>0$, multiplication by $r$ and $1/r$ also preserves $H_0^1(\rho,1)$ and its two endpoint traces.

### 2. Form identity and closure

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

Since $u=rR$ and $u(\rho)=u(1)=0$,

$$
\int_\rho^1r^2|R'|^2\,dr
=
\int_\rho^1|u'|^2\,dr.
$$

Close this identity in the form norm. Do not replace the global form domain by an unrestricted product.

### 3. Operators and compactness

The form $\mathfrak a_\ell$ has associated operator $L_\ell$ with the stated $H^2\cap H_0^1$ domain because the potential is continuous on $[\rho,1]$.

Each block has compact resolvent by the compact embedding

$$
H_0^1(\rho,1)\hookrightarrow L^2(\rho,1).
$$

For the infinite direct sum, truncate to $\ell\le L$. Each truncation is compact, while the resolvent norm of the discarded tail tends to zero by

$$
L_\ell\ge\ell(\ell+1).
$$

Thus the global resolvent is a norm limit of compact operators.

### 4. Radial simplicity and zero energy

Positivity follows from

$$
\mathfrak a_\ell[u]\ge
\int_\rho^1|u'|^2\,dr
\ge\frac{\pi^2}{(1-\rho)^2}\|u\|_2^2.
$$

Hence $\lambda=0$ is not an eigenvalue. Equivalently, multiplying

$$
L_\ell u=0
$$

by $\overline u$ and integrating with Dirichlet endpoints forces $u=0$.

If two solutions of

$$
L_\ell u=\lambda u
$$

vanish at $r=\rho$, their initial derivatives are proportional. ODE uniqueness makes them proportional, so every radial eigenvalue is simple.

### 5. Determinant and simple positive roots

For $k>0$, the radial solutions are

$$
R(r)=r^{-1/2}
\bigl(c_1J_{\ell+1/2}(kr)+c_2Y_{\ell+1/2}(kr)\bigr).
$$

The two Dirichlet conditions have a nonzero coefficient vector exactly when the displayed cross-product vanishes.

For an independent root-simplicity check, let $s_\ell(r,k)$ solve

$$
(L_\ell-k^2)s_\ell=0,\qquad
s_\ell(\rho,k)=0,\qquad
\partial_rs_\ell(\rho,k)=1.
$$

At a root $s_\ell(1,k)=0$, differentiation in $k$ and Lagrange's identity give

$$
\partial_rs_\ell(1,k)\,
\partial_ks_\ell(1,k)
=
2k\int_\rho^1s_\ell(r,k)^2\,dr>0.
$$

The sign-normalized Bessel solution is

$$
s_\ell(r,k)
=
\frac{\pi\sqrt\rho}{2}\sqrt r
\left[
J_\nu(\rho k)Y_\nu(kr)
-Y_\nu(\rho k)J_\nu(kr)
\right],
$$

whose left derivative is one by the Bessel Wronskian. Consequently

$$
s_\ell(1,k)=\frac{\pi\sqrt\rho}{2}F_{\nu,\rho}(k),
$$

so the positive roots of $F_{\nu,\rho}$ are simple.

At zero energy,

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

Thus the phase level $n=0$ at $k\to0+$ is not a determinant root.

### 6. Full multiplicity

For fixed $(\ell,n)$, the radial eigenvalue appears in each of the $2\ell+1$ orthogonal $m$ channels. If the same numerical eigenvalue occurs for distinct $\ell$ values, the corresponding subspaces remain orthogonal and their dimensions add.

Do not claim that distinct centrifugal potentials prevent accidental cross-$\ell$ equality.

### 7. Finiteness of the count

Because $r\le1$,

$$
\lambda_{\ell,n}\ge\ell(\ell+1).
$$

Thus no channel with $\ell(\ell+1)\ge K^2$ contributes to the strict count below $K^2$, and the angular sum is finite.

## Falsification cases

- the infinite direct sum: blockwise compactness alone is insufficient;
- the exact global form and operator summability conditions;
- $\ell=0$;
- $k=0$ and any rescaled determinant that happens to vanish there;
- $K$ equal to one or several shell eigenfrequencies;
- a determinant root where both endpoint values of $J_\nu$, or both endpoint values of $Y_\nu$, vanish;
- the determinant sign convention;
- positive-root simplicity versus radial eigenvalue simplicity;
- accidental equality across distinct $\ell$ values;
- the factor $r^{-1/2}$ in the ordinary-Bessel radial solution;
- the multiplicity $2\ell+1$;
- the endpoint rule $n\pi<\Psi(K)$ rather than $n\pi\le\Psi(K)$.

## Promotion rule

Promotion requires:

1. an incumbent proof with the exact form and operator domains;
2. a clean-room reconstruction that does not read the incumbent;
3. an adversarial audit of compactness, zero energy, determinant equivalence, root simplicity, multiplicity, and strict endpoints.

The lemma does not prove $\rho$-uniformity, the finite-window Pólya inequality, or certified computation.
