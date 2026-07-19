# Lemma Packet: Low-Interface Shifted Tails in the Small-Hole Sector

Status note: this proved stepping-stone is superseded by `SHELL-low-interface-fixed-rho-high-energy.md`, which treats every fixed $0<\rho<1$.

Obligation: `SHELL-low-interface-small-hole`

## Exact statement

Let

$$
G_a(z)=\frac1\pi\left(\sqrt{a^2-z^2}-z\arccos\frac za\right)
\quad(0\le z\le a),
$$

extended by zero for $z\ge a$, and put

$$
A_{\rho,K}(z)=G_K(z)-G_{\rho K}(z),\qquad
\mu=\rho K,
$$

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15}.
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
0<\rho<\omega_0,\quad
K(\omega_0-\rho)\ge C_*,\quad
x_0<\rho K
\quad\Longrightarrow\quad
\mathcal T_r\le 2\int_{x_0}^{K}A_{\rho,K}(z)\,dz.
}
$$

The simpler sufficient sector

$$
0<\rho<\frac1{10},\qquad
K\left(\frac1{10}-\rho\right)\ge C_*
$$

follows because $\omega_0>1/10$.

## Permitted dependencies

- `SHELL-weighted-lattice-scaffold`
- `SHELL-high-angular-shifted-tails`
- `SRC-annuli`
- `sources/annuli_polya.md`, specifically Definition 1.3, Proposition 3.1, Theorem 3.4, and Lemma 6.2

No spectral completeness or numerical root computation is used.

## Required endpoint bookkeeping

For a low-interface tail $x_0<\mu$, set

$$
n=\lfloor\mu-x_0\rfloor,
\qquad q=x_0+n,
\qquad B=\lceil K-x_0\rceil.
$$

Then

$$
q\le\mu<q+1,\qquad n<B,\qquad G_K(x_0+B)=0.
$$

The point $q$ is the largest half-integer not exceeding $\mu$; it is not generally $\lfloor\mu\rfloor$. Consequently, the interface estimate must be derived from the pointwise turning bound in Lemma 6.2, not quoted from the paper's last-integer-cell corollary.

For integers $a<b$, use the trapezoidal floor sum

$$
\mathbf T(h,a,b)=
\frac12\lfloor h(a)\rfloor+
\sum_{j=a+1}^{b-1}\lfloor h(j)\rfloor+
\frac12\lfloor h(b)\rfloor.
$$

When $n=0$, the concave-head term below is absent; do not invoke a degenerate trapezoidal interval.

## Proof skeleton to reconstruct

Since $A_{\rho,K}\le G_K$, monotonicity of the floor and the two half-weights at the split point give, for $n\ge1$,

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T\left(A_{\rho,K}(x_0+\cdot)+\frac14,0,n\right)
+\mathbf T\left(G_K(x_0+\cdot)+\frac14,n,B\right).
$$

For $n=0$, directly use

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T\left(G_K(x_0+\cdot)+\frac14,0,B\right).
$$

On $[x_0,q]$, the function $A_{\rho,K}$ is concave. Proposition 3.1 therefore gives

$$
\mathbf T\left(A_{\rho,K}(x_0+\cdot)+\frac14,0,n\right)
\le
\int_0^n A_{\rho,K}(x_0+t)\,dt+\frac n4.
$$

On $[n,B]$, the function $g(t)=G_K(x_0+t)$, extended by zero past $K$, is decreasing, convex, $\operatorname{Lip}_{1/2}$, and satisfies $g(B)=0$. Because $q\le\mu=\rho K<K/2$, the point

$$
t_*=\frac K2-x_0
$$

lies in $[n,B]$. On $[t_*,B]$, $g$ is $\operatorname{Lip}_{1/3}$, and

$$
g(t_*)=G_K(K/2)=\omega_0K.
$$

Theorem 3.4 gives

$$
\mathbf T\left(G_K(x_0+\cdot)+\frac14,n,B\right)
\le
\int_n^B G_K(x_0+t)\,dt
-\frac14\lfloor\omega_0K\rfloor.
$$

The only integral mismatch is

$$
\delta=\int_q^\mu G_\mu(z)\,dz.
$$

Lemma 6.2 states

$$
G_\mu(z)<\frac{(\mu-z)^{3/2}}{3\sqrt\mu}
\qquad(0<z<\mu).
$$

Since $0\le\mu-q<1$ and a low tail implies $\mu>1/2$,

$$
0\le\delta
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}
<\frac{2\sqrt2}{15}.
$$

Thus, in both the $n=0$ and $n\ge1$ cases,

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A_{\rho,K}(z)\,dz
+\delta-\frac{\lfloor\omega_0K\rfloor-n}{4}.
$$

Finally,

$$
n\le\rho K-\frac12,
\qquad
\lfloor\omega_0K\rfloor>\omega_0K-1,
$$

and hence

$$
\lfloor\omega_0K\rfloor-n
>K(\omega_0-\rho)-\frac12
\ge\frac{8\sqrt2}{15}
>4\delta.
$$

This proves the claimed shifted-tail inequality, in fact strictly whenever a low tail exists.

## Consequence through the weighted scaffold

Together with `SHELL-high-angular-shifted-tails`, this controls every shifted tail in the stated sector. Therefore the coarse ordinary-floor proxy satisfies

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The strict proxy and the optimized $H_\mu$-capped proxy are no larger. This is a lattice statement only; it does not discharge spectral completeness, the finite window, or the sectors $\rho\ge\omega_0$.

## Falsification cases

- $n=0$, where there is no concave trapezoidal block;
- $q=\mu$, where the interface loss is exactly zero;
- $\mu$ immediately above a half-integer, where $\mu-q$ is small;
- $\mu$ immediately below the next half-integer, where $\mu-q\to1^-$;
- $K-x_0\in\mathbb Z$, where $B=K-x_0$ and the terminal sample is exactly at $K$;
- $A_{\rho,K}(x_0+j)+1/4\in\mathbb Z$;
- $K(\omega_0-\rho)=C_*$;
- $\rho\uparrow\omega_0$, where the explicit threshold diverges.

## Promotion rule

Promote only after an independent reconstruction verifies the split weights, the $n=0$ case, all hypotheses of Theorem 3.4, and the strict constant chain, followed by an adversarial audit. Do not promote the parent `SHELL-low-interface-shifted-tails`, which remains open for $\rho\ge\omega_0$.
