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
P_{\mathcal A}\le I_{\varepsilon,a},
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

## Enlarged local-plateau seam theorem

Round 10 rederives the local-plateau argument on the larger parameter domain

$$
0<\varepsilon\le\frac1{25}.
$$

With $K\varepsilon^2\ge20$, the incumbent proof obtains

$$
\widehat q<\frac{21}{80},
\qquad
R<\frac{73}{16\sqrt\varepsilon},
$$

and exact no-drop and gain-payment margins close every low-interface shifted
tail. An isolated reconstruction reaches the same theorem with distinct
intermediate constants. Consequently

$$
\boxed{
0<\varepsilon\le\frac1{25},
\quad
K\ge\frac{20}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The threshold face is included. On the common domain
$0<\varepsilon\le1/100$, the Round 9 constant $125/8$ is sharper and remains
the authoritative high threshold.

## Further enlarged local-plateau seam theorem

Round 12 independently rederives the same shifted-tail mechanism on the
larger domain

$$
0<\varepsilon\le\frac1{20},
\qquad K\varepsilon^2\ge24.
$$

In the incumbent route, every dangerous branch satisfies

$$
d>\frac{39}{50},
\qquad
\widehat q<\frac{27}{100},
\qquad
R<\frac{23}{5\sqrt\varepsilon}.
$$

The complete synthetic comparison path, including its no-drop endpoint,
retains the exact margin

$$
\frac{4189934997169}{10140435204025}>0,
$$

and the final gain payment retains the margin $233/25>0$. An independent
constant inventory obtains the same loss cap with
$d>3/4$ and $\widehat q<11/40$, while the strictly isolated reconstruction
uses a distinct rectangle argument: it first proves $P<10$, then excludes
$5\le r\le P<10$, and obtains $R<5/\sqrt\varepsilon$. All three finite
comparison chains are reproduced by the exact executable ledger.

Consequently, including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac1{20},
\quad
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The sharper Round 10 threshold $K\ge20/\varepsilon^2$ remains authoritative
on $0<\varepsilon\le1/25$.

## Complete thin-shell endpoint

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{100},
\qquad
a=\varepsilon K.
$$

The accepted product and aggregate theorems cover the closed low union

$$
0\le a\le\frac1{8\varepsilon^{3/2}}.
$$

Round 11 proves the complementary range directly from the exact action. If
$F=R^2$ is the square of the decreasing inverse action and $g=-F'$, then
$g$ decreases to the ungridded inner-interface time and increases after it.
Shifted-sawtooth Stieltjes integration gives the radial deficit

$$
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a.
$$

After the exact half-integer angular ceiling, the normalized reserve is
$61/1400>0$. An isolated clean-room proof uses the primitive $W$ of the
uncentered shifted sawtooth instead and obtains

$$
D\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4},
$$

with independent normalized margin
$4119252993/17500000000>0$. Thus, including the common face,

$$
a\ge\frac1{8\varepsilon^{3/2}}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The two closed ranges cover every $a\ge0$. Hence

$$
\boxed{
\frac{99}{100}\le\rho<1,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

This endpoint theorem is analytic and requires no Bessel-root certificate.
The Round 9 optimized plateau and the Round 10 and Round 12 enlarged seam
theorems remain valid standalone results, but none is needed for this
endpoint closure.
The direct proof, clean-room reconstruction, adversarial audit, and exact
ledger are recorded in `rounds/polya-main/round_011/` and
`computations/round11_verify_ultrathin_bridge.py`.

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
I_{12}=\left[\rho_*,\frac{99}{100}\right],
$$

use four exact zones.

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

For $1/16\le\rho\le19/20$, the strict count is zero below
$\pi/(1-\rho)$ and the fixed-ratio theorem applies above $K_0(\rho)$. The
positive-root equation

$$
\eta y^2-\sqrt a\,y-C_0=0,
\qquad y=\sqrt{K_0},
$$

shows that $K_0$ increases with $a$ and decreases with $\eta$. Since
$a_\rho$ increases and $\eta_\rho$ does not, $K_0(\rho)$ is increasing.
Exact endpoint estimates at the Round 12 seam give

$$
K_0(19/20)<3300^2.
$$

For $19/20\le\rho\le24/25$, write $\varepsilon=1-\rho$. The Round 12
local-plateau theorem applies above

$$
\frac{24}{\varepsilon^2}\le15000.
$$

For $24/25\le\rho\le99/100$, the sharper retained Round 10 theorem applies
above

$$
\frac{20}{\varepsilon^2}\le200000.
$$

The complete thin endpoint owns the shared face $\rho=99/100$ and every
larger ratio. Since

$$
64<15000<200000<3300^2,
$$

the central fixed-ratio ceiling dominates all four compact zones. Thus

$$
\boxed{
\rho\in I_{12},\quad K\ge3300^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Combining this with the complete small-hole and complete thin endpoint
theorems yields the global analytic high-frequency result

$$
\boxed{
0<\rho<1,\quad K\ge3300^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Relative to the Round 11 ceiling, the exact reduction factor is

$$
\frac{6000^2}{3300^2}=\frac{400}{121}>3.
$$

Thus Round 12 lowers the complete all-ratio high-frequency ceiling by more
than a factor $3$.

The closed union of the four displayed gap envelopes is only a planning set
$\mathcal E$. The actual certificate target is

$$
\mathcal D=(I_{12}\times[0,\infty))\setminus\mathcal A,
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
  followed, where necessary, by an exact face-connected certificate of every
  point of $\mathcal D$ below $3300^2$;
- a fresh derivation of a larger central--thin seam domain. The Round 13
  target is

  $$
  0<\varepsilon\le\frac1{10},
  \qquad
  K\ge\frac{24}{\varepsilon^2},
  $$

  together with a proposed seam $\rho=9/10$ and a separately proved target
  $K_0(9/10)<900^2$. These constants are unproved planning targets, not
  current theorems;
- a fresh final theorem-level clean-room reconstruction and adversarial
  review after the compact residual is closed.
