# Frozen Incumbent: Uniform Small-Hole Endpoint

## Theorem

Set

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
$$

and

$$
\rho_*=
\frac{\omega_0}{1+2C_*}
=
\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}
=0.0310668242700667\ldots.
\tag{1}
$$

Then, for every $0<\rho\le\rho_*$ and every $K\ge0$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{2}
$$

The proof is analytic. It uses neither convergence to the ball nor a finite
Bessel-root certificate.

## 1. Audited phase and lattice reduction

Let

$$
\mu=\rho K,
\qquad
A_{\rho,K}=G_K-G_\mu,
\qquad
\nu_\ell=\ell+\frac12.
$$

The exact separated spectrum and strict phase enclosure give

$$
N_D(A_{\rho,1},K^2)
\le S_{\rho,K},
\tag{3}
$$

where

$$
S_{\rho,K}
=\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor
A_{\rho,K}(\nu_\ell)+\frac14
\right\rfloor.
\tag{4}
$$

For $x_r=r+1/2$, define the shifted tail

$$
\mathcal T_r
=\left\lfloor A_{\rho,K}(x_r)+\frac14\right\rfloor
+2\sum_{j\ge1}
\left\lfloor A_{\rho,K}(x_r+j)+\frac14\right\rfloor.
\tag{5}
$$

The proved multiplicity scaffold states that

$$
S_{\rho,K}=\sum_{r\ge0}\mathcal T_r,
\tag{6}
$$

and that the inequalities

$$
\mathcal T_r
\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz
\qquad(r\ge0)
\tag{7}
$$

imply

$$
S_{\rho,K}
\le\int_0^K2zA_{\rho,K}(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{8}
$$

It therefore suffices to prove (7) for every start.

Two previously reviewed tail theorems are available.

1. If $x_r\ge\mu$, then (7) holds by the convex high-angular theorem,
   including equality $x_r=\mu$.
2. If

   $$
   0<\rho<\omega_0,
   \qquad
   K(\omega_0-\rho)\ge C_*,
   \qquad
   x_r<\mu,
   \tag{9}
   $$

   then (7) holds by the audited small-hole low-interface theorem.

## 2. Exact split at $\mu=1/2$

The case $K=0$ is immediate, so assume $K>0$.

If

$$
\mu=\rho K\le\frac12,
$$

then every shifted-tail start satisfies

$$
x_r=r+\frac12\ge\frac12\ge\mu.
$$

Thus the high-angular theorem proves (7) for every $r$. This includes the
joining wall $\mu=1/2$, where $x_0=\mu$.

Now suppose

$$
\mu>\frac12.
$$

Then

$$
K>\frac1{2\rho}.
\tag{10}
$$

Because $C_*>0$, equation (1) gives

$$
0<\rho_*<\omega_0
\tag{11}
$$

and the exact identity

$$
\frac{\omega_0-\rho_*}{2\rho_*}=C_*.
\tag{12}
$$

For $0<\rho\le\rho_*$, the function

$$
f(\rho)=\frac{\omega_0-\rho}{2\rho}
=\frac{\omega_0}{2\rho}-\frac12
$$

is decreasing, so (10)--(12) give

$$
K(\omega_0-\rho)
>
\frac{\omega_0-\rho}{2\rho}
\ge
\frac{\omega_0-\rho_*}{2\rho_*}
=C_*.
\tag{13}
$$

For every $r$, a start with $x_r\ge\mu$ is handled by the high-angular
theorem, while a start with $x_r<\mu$ satisfies all hypotheses in (9) by
(11) and (13). Hence (7) holds for every $r$ in the second branch as well.
Equations (3), (6), and (8) prove (2).

## 3. Endpoint and wall audit

- At $\rho=\rho_*$, equation (12) is an equality. In the branch
  $\mu>1/2$, the first inequality in (13) remains strict, so the threshold in
  (9) is satisfied.
- At $\mu=1/2$, there are no low-interface starts; $x_0=\mu$ belongs to the
  inclusive high-angular theorem.
- At $x_r=\mu$, the high branch is used. Immediately below the interface,
  the low theorem uses only the strict condition $x_r<\mu$ and does not need
  a lower bound on $\mu-x_r$.
- If $K(\omega_0-\rho)=C_*$, then

  $$
  \mu=\frac{C_*\rho}{\omega_0-\rho}\le\frac12,
  $$

  so every start is already high-angular.
- The true spectral count remains strict. The proxy in (4) uses the ordinary
  floor exactly as required by the audited phase majorant and both shifted-tail
  theorems. Phase, action, and eigenvalue walls are therefore not interchanged.
- The argument assumes only $\rho>0$ and never evaluates the degenerate
  domain at $\rho=0$.

## Scope

The constant $\rho_*$ is the exact joining value for these two already-proved
tail regimes because

$$
\frac{C_*}{\omega_0-\rho}
\le\frac1{2\rho}
\quad\Longleftrightarrow\quad
\rho\le\rho_*.
$$

No claim of optimality for the shell theorem itself is made. The result closes
only the $\rho\downarrow0$ endpoint; the intervening compact-$\rho$ window and
the global shell theorem remain open.
