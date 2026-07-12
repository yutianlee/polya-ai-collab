# Source Card: Pólya's Conjecture for Euclidean Balls

Status: audited on 2026-07-12 for the Dirichlet ball comparison, weighted lattice count, and dimension-reduction components used by the shell project. This card does not transfer the ball theorem to shells.

## Primary source

N. Filonov, M. Levitin, I. Polterovich, and D. A. Sher, “Pólya's conjecture for Euclidean balls,” *Inventiones Mathematicae* **234** (2023), 129–169.

- Published paper: [10.1007/s00222-023-01198-1](https://doi.org/10.1007/s00222-023-01198-1)
- Open preprint: [arXiv:2203.07696v4](https://arxiv.org/abs/2203.07696)
- Version audited: v4, 9 May 2023.

## Theorem and counting convention

The source uses the frequency variable $K$ and

$$
\mathcal N_D(\Omega,K)=\#\{j:\lambda_j^D(\Omega)\le K^2\}.
$$

Theorem 1.2 proves, for the unit ball $\mathbb B^d$ and every $d\ge2$,

$$
\mathcal N_D(\mathbb B^d,K)<W_d(K),\qquad K>0,
$$

where

$$
W_d(K)=\frac{K^d}{2^d\Gamma(\frac d2+1)^2}.
$$

In dimension three,

$$
W_3(K)=\frac{2}{9\pi}K^3.
$$

The paper notes that the results also hold with a strict counting convention. The present repository nevertheless translates phase endpoints explicitly: at a phase level equal to an integer, the strict radial count is one less than the ordinary floor.

## Ball spectrum and multiplicity

The Dirichlet eigenfrequencies of $\mathbb B^d$ are

$$
j_{m+d/2-1,k},\qquad m\in\mathbb N_0,\quad k\in\mathbb N,
$$

with spherical-harmonic multiplicity

$$
\kappa_{d,m}
=\binom{m+d-1}{d-1}-\binom{m+d-3}{d-1}.
$$

For $d=3$ this becomes

$$
\nu_m=m+\frac12,
\qquad
\kappa_{3,m}=2m+1=2\nu_m.
$$

## Model action and uniform zero count

For $0\le z\le K$, define

$$
G_K(z)=\frac1\pi\left(\sqrt{K^2-z^2}-z\arccos\frac zK\right),
$$

and set $G_K(z)=0$ for $z>K$. The paper's Theorem 2.3, via Proposition 3.1, gives the non-asymptotic Dirichlet comparison

$$
\#\{k\in\mathbb N:j_{\nu,k}\le K\}
\le
\left\lfloor G_K(\nu)+\frac14\right\rfloor,
\qquad \nu\ge0.
$$

Consequently the weighted ball lattice proxy is

$$
\mathcal P_d^D(K)
=\sum_m\kappa_{d,m}
\left\lfloor G_K\!\left(m+\frac d2-1\right)+\frac14\right\rfloor,
$$

and

$$
\mathcal N_D(\mathbb B^d,K)\le\mathcal P_d^D(K).
$$

This is a pointwise comparison, not merely a large-$K$ asymptotic.

## Convex shifted floor-sum theorem

Theorem 5.1 states: if $g$ is nonnegative, decreasing, convex, $1/2$-Lipschitz on $[0,b]$, and $g(b)=0$, then

$$
\left\lfloor g(0)+\frac14\right\rfloor
+2\sum_{j=1}^{\lfloor b\rfloor}
\left\lfloor g(j)+\frac14\right\rfloor
\le 2\int_0^b g(t)\,dt.
$$

Equality is possible only for the zero function. The theorem is translation-compatible: it may be applied to $g(t)=G_K(r+t)$ on $0\le t\le K-r$ for every fixed shift $r\in[0,K]$.

## Dimension reduction in dimension three

For a finitely supported nonnegative integer sequence $(a_m)$,

$$
\sum_{m\ge0}(2m+1)a_m
=\sum_{r\ge0}\left(a_r+2\sum_{m>r}a_m\right).
$$

Applied to

$$
a_m=\left\lfloor G_K\!\left(m+\frac12\right)+\frac14\right\rfloor,
$$

this is the $d=3$ specialization of the paper's higher-dimensional dimension-reduction formula. Each parenthesis is a shifted two-dimensional tail count. Theorem 5.1 bounds it by

$$
2\int_{r+1/2}^{K}G_K(z)\,dz.
$$

After summing the tails, introduce

$$
f_3(z)=\#\left\{r\in\mathbb N_0:r+\frac12\le z\right\}
=\left\lfloor z+\frac12\right\rfloor
$$

away from the immaterial half-integer endpoints. Its primitive satisfies

$$
F_3(z):=\int_0^z f_3(t)\,dt\le\frac{z^2}{2}.
$$

Indeed, for $z=m+\tfrac12+s$ with $m\in\mathbb N_0$ and $0\le s<1$,

$$
\frac{z^2}{2}-F_3(z)=\frac12\left(s-\frac12\right)^2\ge0.
$$

Integration by parts against the decreasing function $G_K$ then gives

$$
2\int_0^K f_3(z)G_K(z)\,dz
\le
\int_0^K 2zG_K(z)\,dz
=\frac{2}{9\pi}K^3.
$$

This is the exact mechanism by which the ball proof handles the weight $2m+1$.

## Exact integral identity

The source proves in every dimension that

$$
\frac{2}{(d-2)!}\int_0^K z^{d-2}G_K(z)\,dz=W_d(K).
$$

For $d=3$,

$$
\int_0^K2zG_K(z)\,dz=\frac{2}{9\pi}K^3.
$$

Subtracting the same identity at $\mu=\rho K$ yields the shell action-volume identity

$$
\int_0^K2z\bigl(G_K(z)-G_\mu(z)\bigr)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3,
$$

where $G_\mu(z)=0$ for $z>\mu$.

## What transfers to the shell project

Transfers directly:

- the half-integer multiplicity identity $2\ell+1=2(\ell+\tfrac12)$;
- the purely combinatorial dimension reduction into shifted tail counts;
- the abstract convex $1/2$-Lipschitz floor-sum theorem;
- the step-function primitive bound $F_3(z)\le z^2/2$;
- the exact weighted integral identity.

For the shell action

$$
A_{\rho,K}(z)=G_K(z)-G_{\rho K}(z),
$$

a shifted tail whose actual starting order is $x_0\ge\rho K$ is exactly the convex ball tail $G_K(x_0+t)$, so Theorem 5.1 applies without modification. In the shell dimension-reduction notation $x_0=r+1/2$.

Does not transfer directly:

- a shifted shell tail beginning at an actual order $x_0<\rho K$ crosses a concave part of $A_{\rho,K}$ before its convex part;
- Theorem 5.1 cannot be applied across that concave/convex interface;
- subtracting the two already-proved ball inequalities is not a valid floor-sum argument;
- the ball comparison concerns zeros of $J_\nu$, not zeros of a shell Bessel cross-product;
- the source supplies no finite certificate for shell roots or shell lattice walls.

## Computation status

The Dirichlet ball proof is analytic. The source's computer-assisted component is used only for a residual Neumann disk interval. It cannot be reused as a shell certificate.

## Audit conclusion

The ball source resolves the algebraic treatment of the $2\ell+1$ multiplicity and rigorously controls every shifted shell tail that starts at or above the inner turning interface $\rho K$. The first unsupported step is now precise: prove the corresponding shifted-tail inequality for starts below $\rho K$, where the shell action changes from concave to convex and the optimized phase slack may be needed.
