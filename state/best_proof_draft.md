# Best Proof Draft

No complete all-$K$, all-$\rho$ shell Pólya proof exists.

## Exact spectral bridge

For every fixed $0<\rho<1$, spherical-harmonic expansion followed by
$u=rR$ gives

$$
-\Delta_{A_{\rho,1}}^D
\simeq
\bigoplus_{\ell=0}^{\infty}
\bigoplus_{m=-\ell}^{\ell}
\left(
-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
\right).
$$

The exact form and operator domains are recorded in
state/lemma_packets/SHELL-sturm-liouville-completeness.md. Compactness of the
full resolvent uses the angular-tail estimate

$$
\|(L_\ell+1)^{-1}\|
\le
\frac1{1+\ell(\ell+1)}
\longrightarrow0,
$$

not merely blockwise compactness.

Each radial block has a positive simple complete spectrum. For
$\nu=\ell+\tfrac12$, its eigenfrequencies are exactly the positive simple
roots of

$$
F_{\nu,\rho}(k)
=
J_\nu(\rho k)Y_\nu(k)
-Y_\nu(\rho k)J_\nu(k).
$$

With the audited phase convention,

$$
\Psi_{\nu,\rho}(k)
=
\theta_\nu(k)-\theta_\nu(\rho k)
$$

is strictly increasing from zero to infinity, and the positive roots satisfy

$$
\Psi_{\nu,\rho}(k_{\ell,n})=n\pi,
\qquad n=1,2,\ldots.
$$

Thus strict counting is exactly

$$
N_D(A_{\rho,1},K^2)
=
\sum_{\ell=0}^{\infty}(2\ell+1)
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
$$

At a phase wall $\Psi(K)=m\pi$, the channel contribution is $m-1$.
Accidental equality across different $\ell$ channels is allowed and the
orthogonal multiplicities add.

## Fixed-rho high-energy theorem

For

$$
A_{\rho,K}=G_K-G_{\rho K},
$$

the multiplicity scaffold reduces the coarse proxy to shifted tails. The
Round 3 high- and low-interface estimates prove

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor A_{\rho,K}(\nu_\ell)+\frac14\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(K\ge K_0(\rho)),
$$

where

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
$$

$$
a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
\eta_\rho=G_1\!\left(\max\{\rho,1/2\}\right),\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

The strict phase proxy is no larger. Combining it with the now-proved exact
spectral bridge gives the unconditional theorem

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\quad\text{for every fixed }0<\rho<1
\text{ and }K\ge K_0(\rho).
}
$$

Also,

$$
(1-\rho)K\le\pi
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)=0.
$$

## Uniform low-optical thin-shell theorem

Put

$$
\varepsilon=1-\rho,\qquad a=\varepsilon K.
$$

Since

$$
L_\ell
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1)
$$

on the interval of length $\varepsilon$, min--max gives

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
$$

Counting the resulting product levels with strict radial and angular walls
and the exact multiplicity sum yields

$$
\boxed{
0<\varepsilon\le\frac1{100},
\quad
0\le K\le\frac{\pi}{4\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The proof and exact lattice margin are recorded in
state/lemma_packets/SHELL-thin-product-low-optical.md.

This product comparison cannot itself be extrapolated. Its majorant exceeds
the shell Weyl target at exact walls of order
$a\asymp\varepsilon^{-1}$, including a family with
$\varepsilon\downarrow0$. Round 6 closes the resulting gap by two different
radius-sensitive arguments.

## Exact scaled-action aggregate theorem

Put $y=\varepsilon\nu$. The exact shell action is

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds
=G_K(\nu)-G_{\rho K}(\nu).
$$

On the strict half-integer mesh
$y_\ell=\varepsilon(\ell+\tfrac12)$, let

$$
q_\ell=
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_{y_\ell<a}y_\ell q_\ell.
$$

The audited phase enclosure and exact spectrum reduce the shell inequality to

$$
P_{\mathcal A}le I_{\varepsilon,a},
\qquad
I_{\varepsilon,a}
=\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy.
$$

Fubini gives the exact coefficient

$$
I_{\varepsilon,a}
=\frac{m_\varepsilon a^3}{3\pi},
\qquad
m_\varepsilon
=1-\varepsilon+\frac{\varepsilon^2}{3}
=\frac1\varepsilon\int_{1-\varepsilon}^1r^2\,dr.
$$

Define the volume-matched semicircle

$$
\mathcal B_{\varepsilon,a}(y)
=\frac1\pi
\sqrt{a^2-\frac{y^2}{m_\varepsilon}}_+.
$$

Jensen's inequality proves
$\mathcal A_{\varepsilon,a}\le\mathcal B_{\varepsilon,a}$ only below the
inner interface $y\le\rho a$. The effective action is deliberately not used
as a global pointwise majorant. Strict layer cake at radial levels
$n-\tfrac14$, the exact half-integer angular count, and the shifted deficit

$$
\frac D{\pi^2}
=\frac{N^2}{4}
+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3},
\qquad -\frac14<u\le\frac34,
$$

give an effective-action lattice margin larger than $a^2/12$. The positive
outer whispering-gallery strip costs less than $a^2/12$ whenever

$$
\frac\pi{4\varepsilon}
\le a\le\frac1{8\varepsilon^{3/2}},
\qquad 0<\varepsilon\le\frac1{100}.
$$

Consequently the shell inequality holds throughout

$$
\frac\pi{4\varepsilon^2}
\le K\le\frac1{8\varepsilon^{5/2}}.
$$

Together with the product theorem, this covers
$0\le K\le1/(8\varepsilon^{5/2})$.

## Round 6 local-plateau high-thin theorem (historical)

The Round 3 shifted-tail decomposition can be sharpened by retaining the
location of its first constant-floor plateau. If $p$ is its length and
$m$ is the remaining number of concave-head cells, the only dangerous loss
is $p-dm$. In that branch the exact local slope

$$
-A_{\rho,K}'(z)
=\frac1\pi
\left(
\arccos\frac zK-
\arccos\frac z{\rho K}
\right)
\ge
\frac{\varepsilon z}{\pi\sqrt{K^2-z^2}}
$$

forces

$$
p<\frac{10}{\sqrt\varepsilon}
\qquad
\left(K\ge\frac{64}{\varepsilon^2}\right).
$$

At the same threshold, the convex-tail gain is paid by

$$
G_1(1-\varepsilon)
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
$$

This proves every low-interface shifted tail; the audited convex theorem
handles starts at or above the interface. Therefore

$$
K\ge\frac{64}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

for $0<\varepsilon\le1/100$. Round 9 supersedes the constant $64$ below.

## Optimized uniform local-plateau high-thin theorem

For the same Round 3 shifted-tail decomposition, retain the actual
uncompensated loss

$$
R=p-dm.
$$

Set $y=\sqrt\varepsilon$ and
$\kappa=K\varepsilon^2$. A self-consistent scaled analysis of the exact
local slope, with no estimate imported from the old $C=64$ proof, shows that
the dangerous branch $R>0$ satisfies

$$
R<\frac{361}{80\sqrt\varepsilon}
\qquad
\left(\kappa\ge\frac{125}{8}\right).
$$

The action gain obeys

$$
K G_1(1-\varepsilon)
\ge\frac{2\sqrt2\,\kappa}{3\pi\sqrt\varepsilon},
$$

and exact rational endpoint comparisons show that its strict floor lower
bound pays for $R$, the full possible floor loss, and the interface
remainder. The branch $R\le0$ closes directly from the same gain. Thus every
low-interface shifted tail is controlled; the audited convex theorem handles
starts at or above the interface. Therefore, for
$0<\varepsilon\le1/100$,

$$
K\ge\frac{125}{8\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
$$

Threshold equality and all ordinary-floor, interface, gain, and strict
spectral walls are included.

## Complete thin-shell endpoint

The low and optimized high thresholds overlap exactly when

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{15625}.
$$

At $\varepsilon=1/15625$ both thresholds equal $125^5/8$, and both
component theorems include equality. Hence

$$
\boxed{
1-\frac1{15625}\le\rho<1,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

This endpoint theorem is analytic and requires no Bessel-root certificate.
The Round 6 artifacts record the earlier $C=64$ theorem; the optimized proof
and independent review are recorded in `rounds/polya-main/round_009/`.

## Complete small-hole endpoint

Set

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The previously audited small-hole tail theorem states that every shifted
tail beginning below the inner interface $\mu=\rho K$ satisfies its target
integral bound when

$$
0<\rho<\omega_0,
\qquad
K(\omega_0-\rho)\ge C_*.
\tag{S1}
$$

Every tail beginning at or above $\mu$ is already controlled by the convex
high-angular theorem.

If $\mu\le1/2$, then every tail start
$x_r=r+1/2$ satisfies $x_r\ge\mu$, so all tails are high-angular. If
$\mu>1/2$ and $0<\rho\le\rho_*$, then

$$
K(\omega_0-\rho)
>\frac{\omega_0-\rho}{2\rho}
\ge
\frac{\omega_0-\rho_*}{2\rho_*}
=C_*.
$$

Thus (S1) controls every remaining low-interface tail. The multiplicity
scaffold and strict spectral bridge prove

$$
\boxed{
0<\rho\le\rho_*,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

At $\rho=\rho_*$ the two ranges meet at
$K_*=1/(2\rho_*)$, and both endpoints are included. This theorem is also
fully analytic; pointwise root convergence to the ball and small-hole
certification are unnecessary.

## Compact-ratio analytic envelope

On the remaining ratio interval

$$
I_9=\left[\rho_*,1-\frac1{15625}\right],
$$

use three exact zones.

For $\rho_*\le\rho\le1/16$, the high-angular theorem proves the target for
$K\le1/(2\rho)$ and the small-hole low-interface theorem proves it for

$$
K\ge H_0(\rho)=\frac{C_*}{\omega_0-\rho}.
$$

The thresholds meet at $\rho_*$, $H_0$ is increasing, and the elementary
bounds $\sqrt3>5/3$, $\sqrt2<3/2$, and $\pi<22/7$ give

$$
H_0(1/16)<64.
$$

For $1/16\le\rho\le99/100$, the strict count is zero below
$\pi/(1-\rho)$ and the fixed-ratio theorem applies above $K_0(\rho)$. The
positive-root equation

$$
\eta y^2-\sqrt a\,y-C_0=0,
\qquad y=\sqrt{K_0},
$$

shows that $K_0$ increases with $a$ and decreases with $\eta$. Since
$a_\rho$ increases and $\eta_\rho$ does not, $K_0(\rho)$ is increasing.
Exact endpoint estimates give

$$
K_0(99/100)<180000^2<2^{35}.
$$

For $99/100\le\rho\le1-1/15625$, write
$\varepsilon=1-\rho$. The aggregate-action and optimized local-plateau
theorems cover

$$
K\le\frac1{8\varepsilon^{5/2}}
\qquad\hbox{and}\qquad
K\ge\frac{125}{8\varepsilon^2}.
$$

Every possible residual in this thin zone satisfies

$$
K<\frac{125^5}{8}<2^{32}.
$$

The unchanged central ceiling $2^{35}$ therefore dominates all three zones,
and

$$
\boxed{
\rho\in I_9,\quad K\ge2^{35}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Combining this with the complete small-hole and enlarged thin endpoint
theorems yields the global analytic high-frequency result

$$
\boxed{
0<\rho<1,\quad K\ge2^{35}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The closed union of the three displayed gap envelopes is only a planning set
$\mathcal E$. The actual certificate target is

$$
\mathcal D=(I_9\times[0,\infty))\setminus\mathcal A,
$$

where $\mathcal A$ contains every analytically covered point and threshold
face.

## First certified residual box

On the closed box

$$
\rho\in\left[\frac{999}{2000},\frac{1001}{2000}\right],
\qquad
K\in\left[\frac{67}{10},\frac{168}{25}\right],
$$

outward-rounded Arb evaluation of the Riccati--spherical determinant gives
one root in each of $\ell=0,1$. The exact Poincare--Sturm lower bound

$$
\lambda_{n,\ell}
\ge\left(\frac{n\pi}{1-\rho}\right)^2+\ell(\ell+1)
$$

excludes the second radial levels and all $\ell\ge2$. Thus the exact strict
count is $1+3=4$. An independent checker using only rational Machin and
Taylor enclosures reconstructs every determinant sign, truncation, and Weyl
corner. It proves

$$
\inf_B\frac{2}{9\pi}(1-\rho^3)K^3
>18.6073155354,
$$

so the certified margin exceeds $14.6073155354$. This is one local box, not
a cover of $\mathcal D$.

## Remaining gates

This file must not be cited as a proof of the full shell theorem. The open
gates are:

- analytic or symbolic compression of the current compact planning envelope,
  followed by an exact face-connected certificate of every point of
  $\mathcal D$ below $2^{35}$. The Round 9 optimization has removed the old
  thin ceiling; further analytic aggregation or exact monotone-corner
  certification is still needed for the remaining compact residual;
- a fresh final theorem-level clean-room reconstruction and adversarial
  review.
