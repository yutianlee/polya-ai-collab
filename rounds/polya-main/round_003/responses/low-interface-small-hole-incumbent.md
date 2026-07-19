# Round 3 Continuation: Small-Hole Low-Interface Tails

Status note: this frozen stepping-stone was subsequently generalized by `low-interface-fixed-rho-incumbent.md` to every fixed $0<\rho<1$.

## Verdict

The full low-interface obligation is still open, but an explicit analytic sector closes:

$$
0<\rho<\omega_0:=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
K\ge
\frac{\frac12+\frac{8\sqrt2}{15}}{\omega_0-\rho}.
$$

In this sector every coarse ordinary-floor shifted tail, including those that cross the inner interface, is bounded by its target integral. The simpler range $0<\rho<1/10$ follows immediately.

## Proof

Fix a low-interface tail and write

$$
x_0=r+\frac12<\mu=\rho K,\qquad
n=\lfloor\mu-x_0\rfloor,\qquad
q=x_0+n,\qquad
B=\lceil K-x_0\rceil.
$$

Let $A=G_K-G_\mu$, with both $G$ functions extended by zero beyond their endpoints. Define

$$
\mathcal T_r=
\left\lfloor A(x_0)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A(x_0+j)+\frac14\right\rfloor.
$$

For $n\ge1$, split the sampled tail at the integer $n$. Use $A\le G_K$ on the right block. At the split point, the half endpoint from the $A$ block and the half endpoint from the $G_K$ block sum to at least the full $A$ sample. Hence

$$
\frac{\mathcal T_r}{2}
\le
\mathbf T(A(x_0+\cdot)+1/4,0,n)
+\mathbf T(G_K(x_0+\cdot)+1/4,n,B).
\tag{1}
$$

If $n=0$, the first block is absent and direct pointwise majorization gives

$$
\frac{\mathcal T_r}{2}
\le\mathbf T(G_K(x_0+\cdot)+1/4,0,B).
\tag{2}
$$

On the head, $A$ is concave because, for $z<\mu$,

$$
A''(z)=
\frac1{\pi\sqrt{K^2-z^2}}
-\frac1{\pi\sqrt{\mu^2-z^2}}<0.
$$

The audited concave trapezoidal-floor estimate therefore gives

$$
\mathbf T(A(x_0+\cdot)+1/4,0,n)
\le\int_0^nA(x_0+t)\,dt+\frac n4.
\tag{3}
$$

On the right block, $g(t)=G_K(x_0+t)$ is decreasing, convex, globally $\operatorname{Lip}_{1/2}$, and zero at $B$. Since $q\le\mu=\rho K<K/2$, the point $t_*=K/2-x_0$ belongs to $[n,B]$. On $[t_*,B]$, $g$ is $\operatorname{Lip}_{1/3}$, and

$$
g(t_*)=G_K(K/2)=
\left(\frac{\sqrt3}{2\pi}-\frac16\right)K
=\omega_0K.
$$

The audited improved convex theorem gives

$$
\mathbf T(G_K(x_0+\cdot)+1/4,n,B)
\le\int_n^BG_K(x_0+t)\,dt
-\frac14\lfloor\omega_0K\rfloor.
\tag{4}
$$

Comparing the integrals in (3)--(4) with the desired integral of $A$ leaves exactly

$$
\delta=\int_q^\mu G_\mu(z)\,dz.
$$

The point $q$ is the largest half-integer below $\mu$, so it must not be replaced by $\lfloor\mu\rfloor$. Lemma 6.2 of the audited annulus source gives the pointwise bound

$$
G_\mu(z)<\frac{(\mu-z)^{3/2}}{3\sqrt\mu}.
$$

Since $\mu-q<1$ and $\mu>1/2$,

$$
0\le\delta
\le\frac{2(\mu-q)^{5/2}}{15\sqrt\mu}
<\frac{2\sqrt2}{15}.
\tag{5}
$$

Equations (1)--(5), with (2) handling $n=0$, yield

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta-\frac{\lfloor\omega_0K\rfloor-n}{4}.
\tag{6}
$$

The discrete gain satisfies

$$
\lfloor\omega_0K\rfloor-n
>\omega_0K-1-(\rho K-1/2)
=K(\omega_0-\rho)-\frac12.
$$

Under the displayed threshold this is at least $8\sqrt2/15$, strictly larger than $4\delta$ by (5). Substitution in (6) proves

$$
\mathcal T_r<2\int_{x_0}^{K}A(z)\,dz.
$$

All tails starting at or above $\mu$ were already proved in the first Round 3 judgment. The weighted scaffold therefore proves the complete coarse weighted lattice inequality in this small-hole high-energy sector. The strict and optimized proxies are smaller still.

## What this does not prove

- It does not prove the low-interface tail inequality for $\rho\ge\omega_0$.
- It does not close the finite window below the explicit threshold.
- It does not certify the floating-point diagnostic.
- It does not remove the separate spectral completeness dependency.
- It does not prove the full three-dimensional shell Pólya theorem.

## Rejected abstract shortcut

Monotonicity, a global slope smaller than $1/2$, and one concave-to-convex transition do not suffice for the tail inequality. A separate construction gives a long shelf near height $3/4$ with those properties whose floor count exceeds twice its area. The successful proof above instead uses the shell-specific split and the quantitative $G_\mu$ turning bound.
