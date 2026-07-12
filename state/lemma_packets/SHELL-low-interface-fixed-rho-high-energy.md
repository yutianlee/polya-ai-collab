# Lemma Packet: Fixed-Rho High-Energy Low-Interface Tails

Obligation: `SHELL-low-interface-fixed-rho-high-energy`

## Exact statement

For $a>0$, let

$$
G_a(z)=\frac1\pi\left(\sqrt{a^2-z^2}-z\arccos\frac za\right)
\quad(0\le z\le a),
$$

extended by zero for $z\ge a$. Fix $0<\rho<1$ and define

$$
\mu=\rho K,\qquad A_{\rho,K}=G_K-G_\mu,
$$

$$
c_\rho=\frac{\arccos\rho}{\pi},\qquad
d_\rho=1-2c_\rho=\frac{2\arcsin\rho}{\pi},
$$

$$
\eta_\rho=G_1\!\left(\max\left\{\rho,\frac12\right\}\right)>0,\qquad
a_\rho=\frac{2\pi\rho}{1-\rho},
$$

and

$$
C_0=1+\frac{8\sqrt2}{15}.
$$

Set

$$
\boxed{
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2.
}
$$

For an integer $r\ge0$, write $x_0=r+1/2$ and

$$
\mathcal T_r=
\left\lfloor A_{\rho,K}(x_0)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A_{\rho,K}(x_0+j)+\frac14\right\rfloor.
$$

The target is

$$
\boxed{
K\ge K_0(\rho),\quad x_0<\rho K
\quad\Longrightarrow\quad
\mathcal T_r\le2\int_{x_0}^{K}A_{\rho,K}(z)\,dz.
}
$$

Together with `SHELL-high-angular-shifted-tails`, this proves the complete coarse weighted lattice bound for every fixed $\rho$ above an explicit threshold.

## Permitted dependencies

- `SHELL-weighted-lattice-scaffold`
- `SHELL-high-angular-shifted-tails`
- `SRC-annuli`
- `sources/annuli_polya.md`, specifically Definition 1.3, Proposition 3.1, Theorem 1.4, Theorem 3.4, and Lemma 6.2

No numerical experiment, Bessel-root certificate, or separated-spectrum completeness claim is permitted.

## 1. Integer split

For a low-interface tail, set

$$
n=\lfloor\mu-x_0\rfloor,\qquad
q=x_0+n,\qquad
B=\lceil K-x_0\rceil.
$$

Then $q\le\mu<q+1$ and $n<B$. For $n\ge1$, monotonicity of the floor and $A\le G_K$ give

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T\left(A(x_0+\cdot)+\frac14,0,n\right)
+\mathbf T\left(G_K(x_0+\cdot)+\frac14,n,B\right).
\tag{1}
$$

At $j=n$, the two half endpoint weights majorize the original full $A$ sample. For $n=0$, the first term is absent and direct pointwise majorization gives

$$
\frac{\mathcal T_r}{2}
\le\mathbf T\left(G_K(x_0+\cdot)+\frac14,0,B\right).
\tag{2}
$$

## 2. Concave head and first floor drop

Assume $n\ge1$ and put

$$
h(t)=A(x_0+t)+\frac14,\qquad m_j=\lfloor h(j)\rfloor.
$$

The sequence $m_j$ is nonincreasing. If it drops below $m_0$, let $p$ be the last index before its first drop:

$$
m_0=m_p>m_{p+1},\qquad 0\le p<n.
$$

If it does not drop on $0,\ldots,n$, set $p=n$.

On $[0,n]$, $h$ is decreasing, concave, and $\operatorname{Lip}_{c_\rho}$. Indeed,

$$
-A'(z)=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right)
\le\frac{\arccos\rho}{\pi}=c_\rho
\qquad(0\le z\le\mu).
$$

If $p<n$, Theorem 1.4 applies. If $p=n$, Proposition 3.1 applies. Both cases give the unified estimate

$$
\mathbf T(h,0,n)
\le
\int_0^nA(x_0+t)\,dt+\frac n4
-\frac{1-c_\rho}{2}(n-p).
\tag{3}
$$

For $n=0$, take $p=0$ and interpret (3) as the absent identity $0\le0$.

## 3. Quantitative no-shelf bound

Because $m_0=m_p$ and $h$ is decreasing,

$$
0\le A(x_0)-A(x_0+p)<1.
\tag{4}
$$

Let $\sigma=-A'$. For $0<z<\mu$,

$$
\sigma'(z)=
\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}
\ge
\kappa:=\frac{K-\mu}{\pi K\mu}
=\frac{1-\rho}{\pi\rho K}.
$$

For completeness, the lower bound follows by writing the difference as $\kappa$ plus

$$
\frac1\pi\left[
\left(\frac1{\sqrt{\mu^2-z^2}}-\frac1\mu\right)
-\left(\frac1{\sqrt{K^2-z^2}}-\frac1K\right)
\right]\ge0;
$$

for fixed $z$, the bracketed one-parameter function is decreasing in its radius argument. In particular, $\sigma$ is increasing and its endpoint value is $c_\rho$, justifying the Lipschitz constant used in (3).

Since $\sigma(0)=0$, for $0\le x<y\le\mu$,

$$
A(x)-A(y)=\int_x^y\sigma(z)\,dz
\ge\frac\kappa2(y^2-x^2)
\ge\frac\kappa2(y-x)^2.
$$

Applying this to (4) yields

$$
\boxed{p<\sqrt{\frac2\kappa}=\sqrt{a_\rho K}.}
\tag{5}
$$

This shell-specific curvature estimate is the step unavailable for a generic concave-to-convex function.

## 4. Convex tail gain for every fixed rho

Let

$$
s=\max\left\{q,\frac K2\right\},\qquad t_*=s-x_0.
$$

Then $t_*\in[n,B]$. The function $g(t)=G_K(x_0+t)$ is decreasing, convex, $\operatorname{Lip}_{1/2}$ on $[n,B]$, vanishes at $B$, and is $\operatorname{Lip}_{1/3}$ on $[t_*,B]$. Moreover,

$$
g(t_*)=G_K(s)\ge K\eta_\rho.
$$

For $\rho\le1/2$, this is equality at $s=K/2$. For $\rho>1/2$, it follows from $s\le\rho K$ and the monotonicity and scaling of $G_K$.

Theorem 3.4 gives

$$
\mathbf T\left(G_K(x_0+\cdot)+\frac14,n,B\right)
\le
\int_n^B G_K(x_0+t)\,dt
-\frac14\lfloor K\eta_\rho\rfloor.
\tag{6}
$$

## 5. Interface loss and compensation

The integral mismatch in (1)--(3) and (6) is

$$
\delta=\int_q^\mu G_\mu(z)\,dz.
$$

Lemma 6.2 and $0\le\mu-q<1$ give

$$
0\le\delta
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}.
$$

If a low tail exists, then $\mu>1/2$, and consequently

$$
\delta<\frac{2\sqrt2}{15}.
\tag{7}
$$

Combining all blocks gives

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz+\delta-\frac{M}{4},
$$

where

$$
M=\lfloor K\eta_\rho\rfloor
+d_\rho n-(1+d_\rho)p
=\lfloor K\eta_\rho\rfloor+d_\rho(n-p)-p.
$$

Since $0\le p\le n$, $d_\rho>0$, and (5) holds,

$$
M>\lfloor K\eta_\rho\rfloor-\sqrt{a_\rho K}
>K\eta_\rho-1-\sqrt{a_\rho K}.
\tag{8}
$$

The definition of $K_0(\rho)$ is exactly the positive-root solution of

$$
K\eta_\rho-\sqrt{a_\rho K}\ge C_0.
$$

Therefore (7)--(8) imply

$$
M>\frac{8\sqrt2}{15}>4\delta,
$$

which proves the target, strictly whenever a low tail exists.

## 6. Weighted consequence

For $K\ge K_0(\rho)$, the present lemma controls every tail beginning below $\mu$, while `SHELL-high-angular-shifted-tails` controls every tail beginning at or above $\mu$. The weighted scaffold gives

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The strict proxy and optimized transferred phase proxy are no larger. This discharges the fixed-$\rho$ high-energy weighted lattice obligation, but not the finite window or the separated-spectrum completeness obligation.

## Falsification cases

- $n=0$;
- no floor drop on the concave head, so $p=n$;
- an immediate first drop, so $p=0$;
- $q=\mu$ and hence $\delta=0$;
- $q$ immediately below $\mu$ by almost one unit;
- $q$ on either side of $K/2$;
- $\rho=1/2$;
- $K\eta_\rho$ on an integer wall;
- equality $K=K_0(\rho)$;
- $\rho\downarrow0$ and $\rho\uparrow1$;
- the distinction between the ordinary-floor coarse proxy and strict positive-integer counting.

## Promotion rule

Promotion requires a clean-room reconstruction that does not see the incumbent proof and an adversarial audit checking Theorems 1.4 and 3.4, the plateau bound, the algebra defining $M$, the explicit root $K_0(\rho)$, and every endpoint case. Numerical sampling is diagnostic only.
