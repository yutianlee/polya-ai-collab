# Round 3 Continuation: All Fixed-Rho High-Energy Tails

## Verdict

The remaining low-interface tails admit an explicit fixed-$\rho$ high-energy proof for every $0<\rho<1$. The mechanism is a three-part compensation:

1. the first floor plateau on the concave head has length only $O_\rho(\sqrt K)$;
2. the sharpened concave trapezoidal estimate removes the nominal $n/4$ head cost after that plateau;
3. the convex $G_K$ tail supplies a positive gain $K\eta_\rho/4$.

The linear gain dominates the square-root plateau uniformly over every fixed $\rho$.

## Explicit threshold

Define

$$
\eta_\rho=G_1\!\left(\max\left\{\rho,\frac12\right\}\right),\qquad
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

Then it is sufficient that

$$
K\ge K_0(\rho):=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2.
$$

This threshold is intentionally conservative. It is explicit and finite for each fixed $0<\rho<1$, but diverges rapidly as $\rho\to1$.

## Proof

Fix $x_0=r+1/2<\mu=\rho K$ and set

$$
n=\lfloor\mu-x_0\rfloor,\qquad q=x_0+n,\qquad B=\lceil K-x_0\rceil.
$$

As in the audited small-hole split, the shifted tail divided by two is majorized by a concave $A=G_K-G_\mu$ trapezoidal block on $[0,n]$ and a convex $G_K$ block on $[n,B]$. When $n=0$, only the convex block is present.

For $n\ge1$, put

$$
h(t)=A(x_0+t)+\frac14,\qquad m_j=\lfloor h(j)\rfloor.
$$

Let $p$ be the last sample before the first drop from the initial floor level. If no drop occurs, set $p=n$. The audited sharper concave theorem, with Proposition 3.1 in the no-drop case, yields

$$
\mathbf T(h,0,n)
\le\int_0^nA(x_0+t)\,dt+\frac n4
-\frac{1-c_\rho}{2}(n-p),
\tag{1}
$$

where $c_\rho=\arccos(\rho)/\pi<1/2$.

The equality $m_0=m_p$ forces

$$
A(x_0)-A(x_0+p)<1.
\tag{2}
$$

This is where the shell action supplies more structure than an abstract S-shaped curve. If $\sigma=-A'$, then

$$
\sigma'(z)=
\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}
\ge\frac{1-\rho}{\pi\rho K}=:\kappa.
$$

The last inequality follows by subtracting the value at $z=0$: for fixed $z$, the function

$$
a\longmapsto\frac1{\sqrt{a^2-z^2}}-\frac1a
$$

is decreasing. Thus $\sigma$ is increasing from zero to $c_\rho$, which also proves the Lipschitz bound used in (1).

Since $\sigma(0)=0$, (2) gives

$$
p<\sqrt{\frac2\kappa}
=\sqrt{\frac{2\pi\rho}{1-\rho}K}
=\sqrt{a_\rho K}.
\tag{3}
$$

For the convex block choose the beginning of the $1/3$-Lipschitz region at

$$
s=\max\{q,K/2\}.
$$

The improved convex theorem subtracts one quarter of the floor at this point. Scaling and monotonicity give

$$
G_K(s)\ge K\eta_\rho,
$$

so

$$
\mathbf T(G_K(x_0+\cdot)+1/4,n,B)
\le\int_n^BG_K(x_0+t)\,dt
-\frac14\lfloor K\eta_\rho\rfloor.
\tag{4}
$$

The interface mismatch is

$$
\delta=\int_q^\mu G_\mu(z)\,dz
<\frac{2\sqrt2}{15},
\tag{5}
$$

where the first integrated comparison is non-strict if $q=\mu$, but the displayed uniform estimate remains strict.

Combining the split, (1), and (4)--(5) gives

$$
\frac{\mathcal T_r}{2}
\le\int_{x_0}^KA(z)\,dz+\delta-\frac M4,
$$

with

$$
M=\lfloor K\eta_\rho\rfloor
+d_\rho(n-p)-p,
\qquad d_\rho=\frac{2\arcsin\rho}{\pi}>0.
$$

Since $p\le n$, (3) implies

$$
M>K\eta_\rho-1-\sqrt{a_\rho K}.
$$

The stated threshold is precisely the condition that the right side be at least $8\sqrt2/15$. Therefore $M>4\delta$, proving every low-interface shifted tail.

All high-angular tails were already discharged. The exact weighted scaffold now yields

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge K_0(\rho)).
$$

Hence the strict and optimized shell phase proxies also satisfy the Weyl bound in this fixed-$\rho$ high-energy range.

## Boundaries of the result

- The result is a high-energy weighted lattice theorem, not a finite-window certificate.
- It does not prove the separated Sturm--Liouville completeness statement.
- It is not uniform as $\rho\to1$; $K_0(\rho)$ diverges.
- It does not turn floating Bessel calculations into certification.
- No full shell Pólya theorem is claimed.
