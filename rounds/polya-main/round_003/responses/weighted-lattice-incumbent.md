# Incumbent Attempt: Multiplicity-Weighted Shell Lattice Bound

Role: A2 incumbent analytic author
Obligation: `SHELL-weighted-lattice-fractional`
Status: **partial proof; full obligation remains open**

## 1. Exact strict proxy

Fix $0<\rho<1$, $K>0$, $\mu=\rho K$, and $\nu_\ell=\ell+1/2$. Let

$$
A(\nu)=G_K(\nu)-G_\mu(\nu),
$$

with $G_\mu=0$ above $\mu$. Define

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}=\max\{0,\lceil x\rceil-1\}.
$$

The transferred phase enclosure gives

$$
\gamma_\ell:=\frac{\Psi_{\nu_\ell,\rho}(K)}{\pi}
<A(\nu_\ell)+\frac14.
$$

Therefore the strict radial count satisfies

$$
q_\ell=[\gamma_\ell]_<
\le[A(\nu_\ell)+\tfrac14]_<
\le\left\lfloor A(\nu_\ell)+\frac14\right\rfloor.
$$

The optimized envelope in the lemma packet replaces $1/4$ by $\min\{H_\mu,1/4\}$ below $\mu$, but the coarse envelope is sufficient for every reduction proved below.

## 2. The continuum term is exactly Weyl

For $a>0$,

$$
G_a(\nu)=\frac1\pi\left(\sqrt{a^2-\nu^2}-\nu\arccos\frac\nu a\right),
\qquad0\le\nu\le a.
$$

Scaling $\nu=ax$ gives

$$
\int_0^a2\nu G_a(\nu)\,d\nu
=\frac{2a^3}{\pi}
\left(\int_0^1x\sqrt{1-x^2}\,dx
-\int_0^1x^2\arccos x\,dx\right).
$$

The two elementary integrals are $1/3$ and $2/9$, so

$$
\int_0^a2\nu G_a(\nu)\,d\nu=\frac{2a^3}{9\pi}.
$$

Subtracting the identity at $a=\mu$ from the identity at $a=K$ yields

$$
\boxed{
\int_0^K2\nu A(\nu)\,d\nu
=\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

No asymptotic argument is used here.

## 3. Why the continuous phase sum is not the proof

If every $1/4$ were retained before integerization, its weighted contribution would be

$$
\frac14\sum_{\nu_\ell<K}(2\ell+1)=\frac{m_K^2}{4},
\qquad
m_K=\max\{0,\lceil K-\tfrac12\rceil\}.
$$

For fixed optical width $a=(1-\rho)K$,

$$
\frac{m_K^2/4}{\frac{2}{9\pi}(1-\rho^3)K^3}
\longrightarrow\frac{3\pi}{8a}.
$$

Thus the blanket phase slack is not uniformly lower order. The strict remainders

$$
\langle x\rangle_<=x-[x]_<\in(0,1]
$$

are load-bearing. A proof must retain integerization.

## 4. Equivalent square-count problem

The function $A$ is strictly decreasing on $(0,K)$. Let $x(t)$ be its inverse, extended by zero for $t\ge A(0)$. Swapping the angular and radial sums gives

$$
\sum_{\nu_\ell<K}2\nu_\ell[A(\nu_\ell)+\tfrac14]_<
=\sum_{n\ge1}
\left(
\max\left\{0,
\left\lceil x(n-\tfrac14)-\frac12\right\rceil
\right\}
\right)^2.
$$

The layer-cake identity gives

$$
\int_0^K2\nu A(\nu)\,d\nu
=\int_0^{A(0)}x(t)^2\,dt.
$$

Hence the coarse target is precisely a quarter-shifted square-sum quadrature inequality. This reformulation is exact, but no proof of the required quadrature sign is supplied here.

## 5. Dimension reduction into shifted tails

Set

$$
a_\ell=\left\lfloor A(\nu_\ell)+\frac14\right\rfloor.
$$

For every finitely supported sequence,

$$
\boxed{
\sum_{\ell\ge0}(2\ell+1)a_\ell
=\sum_{r\ge0}
\left(a_r+2\sum_{\ell>r}a_\ell\right).
}
$$

Indeed, $a_\ell$ occurs once with coefficient $1$ in the $r=\ell$ summand and $\ell$ times with coefficient $2$ in the summands $0\le r<\ell$.

Define

$$
\mathcal T_r
=a_r+2\sum_{\ell>r}a_\ell.
$$

The missing shifted-tail inequality is

$$
\tag{T_r}
\mathcal T_r
\le2\int_{r+1/2}^K A(z)\,dz.
$$

Assume temporarily that $(T_r)$ holds for every $r$. Summing gives

$$
\sum_\ell(2\ell+1)a_\ell
\le2\int_0^K f_3(z)A(z)\,dz,
$$

where

$$
f_3(z)=\#\{r\in\mathbb N_0:r+\tfrac12\le z\}.
$$

Let $F_3(z)=\int_0^zf_3(t)dt$. If $z=m+1/2+s$ with $m\in\mathbb N_0$ and $0\le s<1$, direct summation gives

$$
\frac{z^2}{2}-F_3(z)=\frac12(s-\tfrac12)^2\ge0.
$$

Since $A$ is decreasing and $A(K)=0$, integration by parts gives

$$
\int_0^K f_3A=-\int_0^KF_3A'
\le-\int_0^K\frac{z^2}{2}A'
=\int_0^KzA(z)\,dz.
$$

Consequently all shifted-tail inequalities together imply

$$
\sum_\ell(2\ell+1)a_\ell
\le\int_0^K2zA(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

This proves the weighted theorem **conditionally on $(T_r)$ for the tails that start below the inner interface**.

## 6. The high-angular shifted tails are proved

Suppose

$$
r+\frac12\ge\mu.
$$

For $0\le t\le b:=K-r-1/2$,

$$
g_r(t):=A(r+\tfrac12+t)=G_K(r+\tfrac12+t).
$$

The function $g_r$ is nonnegative, decreasing, convex, $1/2$-Lipschitz, and $g_r(b)=0$. The audited FLPS ball floor-sum theorem therefore gives

$$
\left\lfloor g_r(0)+\frac14\right\rfloor
+2\sum_{j=1}^{\lfloor b\rfloor}
\left\lfloor g_r(j)+\frac14\right\rfloor
\le2\int_0^bg_r(t)\,dt.
$$

Terms with $j>b$ vanish. This is exactly $(T_r)$. Hence

$$
\boxed{(T_r)\text{ is proved for every }r+\tfrac12\ge\rho K.}
$$

In particular, if $\rho K\le1/2$, all tails are controlled and the coarse weighted lattice inequality follows for that parameter region.

## 7. Exact thin-width zero-count lemma

For $\nu\ge1/2$, Nicholson's formula gives

$$
M_\nu(x)^2
=\frac8{\pi^2}\int_0^\infty
\cosh(2\nu t)K_0(2x\sinh t)\,dt.
$$

Because the integrand is positive and $\cosh(2\nu t)\ge\cosh t$,

$$
M_\nu(x)^2\ge M_{1/2}(x)^2.
$$

The elementary half-order formulas give

$$
M_{1/2}(x)^2=\frac{2}{\pi x}.
$$

Therefore

$$
0<\theta_\nu'(x)=\frac{2}{\pi xM_\nu(x)^2}\le1
$$

and

$$
0<\Psi_{\nu,\rho}(K)
=\int_{\rho K}^K\theta_\nu'(x)\,dx
\le(1-\rho)K.
$$

If $(1-\rho)K\le\pi$, then no positive integer $n$ satisfies $n\pi<\Psi_{\nu,\rho}(K)$. Thus

$$
\boxed{N_D(A_{\rho,1},K^2)=0\quad\text{whenever }(1-\rho)K\le\pi,}
$$

subject only to the already-recorded separated spectral count. At equality, the $\ell=0$ phase equals $\pi$ and strict counting excludes it.

## 8. First unsupported implication

For a tail with

$$
r+\frac12<\mu,
$$

$A$ is decreasing and concave up to $\mu$, then decreasing and convex from $\mu$ to $K$. The FLPS ball theorem requires convexity on the whole tail and therefore does not apply. Splitting at $\mu$ introduces a generally nonintegral lattice interface and can lose exactly the floor margin needed to cancel the $1/4$ shift.

No argument in this attempt proves $(T_r)$ across that interface. This is the first missing implication, not the Weyl integral, the multiplicity algebra, the high-angular tails, or the thin-width regime.

## Verdict

- Exact target and strict error budget: established.
- Dimension-reduction implication: proved.
- Shifted tails starting at or above $\rho K$: proved from the audited ball theorem.
- Thin-width zero-count region: proved.
- Shifted tails starting below $\rho K$: **open**.
- `SHELL-weighted-lattice-fractional`: **not proved**.
