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

## Central--thin seam at $\rho=9/10$ (retained Round 13)

Round 13 rederives the local-plateau argument on

$$
0<\varepsilon\le\frac1{10},
\qquad K\varepsilon^2\ge24.
$$

The incumbent and independent constant inventory prove

$$
d>\frac23,
\qquad
\widehat q<\frac37,
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

The complete fixed-$r=B$ path has exact endpoint reserve

$$
\frac{2376966388822}{5818105805625}>0
$$

and action-payment reserve

$$
\frac{170244091}{27217575}>0.
$$

The strictly isolated reconstruction uses a different direct localization
and the affine comparison

$$
L(X)=\frac52X-7,
\qquad
F(X)=X^2(1-h_X)^2-2\pi^2Q_X,
$$

with $F(B)>12760228/48234375$ and
$F'(X)>229/2646$ on the complete path. Both proofs own every exceptional
branch and strict wall. Consequently, including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac1{10},
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

## Central--thin seam at $\rho=7/8$

Round 14 independently rederives the local-plateau argument on the enlarged
closed domain

$$
0<\varepsilon\le\frac18,
\qquad K\varepsilon^2\ge32.
$$

The incumbent proof and the independent constant inventory obtain

$$
d>\frac23,
\qquad
\widehat q<\frac{17}{40},
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

For the complete fixed-$r=B$ path with $B=14/3$, the derivative estimate has
exact reserve

$$
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0.
$$

The initial endpoint and dangerous-branch payment reserves are, respectively,

$$
\frac{49714811804}{82306584375}>0,
\qquad
\frac{98646127309}{8083619775}>0.
$$

The strictly isolated clean-room proof first derives $P<9$ and then follows
the distinct affine path

$$
\overline S(P)=\frac52P-7.
$$

Its independent endpoint, full-path derivative, and dangerous-payment
reserves are

$$
\frac{3627793}{7225344}>0,
\qquad
\frac{1178207}{150528}>0,
\qquad
\frac{3229}{275}>0.
$$

Both arguments include the no-drop, immediate-drop, degenerate-head, and
$R=0$ branches; the full possible unit floor loss; every interface and
ordinary-floor wall; and threshold equality. Consequently

$$
\boxed{
0<\varepsilon\le\frac18,
\quad
K\ge\frac{32}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The retained Round 13 threshold $K\ge24/\varepsilon^2$ remains sharper on
$0<\varepsilon\le1/10$, and the retained Round 10 threshold
$K\ge20/\varepsilon^2$ remains sharper on $0<\varepsilon\le1/25$. At
$\varepsilon=1/8$ and $\kappa=24$, that route proves only
$x_0/K>173/384$, while $173/384<1/2$; hence its lower bound does not localize
beyond $1/2$. This obstructs that particular constant-$24$ proof route but
does not disprove a stronger theorem.

## Central--thin seam at $\rho=5/6$

Round 15 independently rederives the local-plateau argument on the enlarged
closed domain

$$
0<\varepsilon\le\frac16,
\qquad K\varepsilon^2\ge54.
$$

The incumbent finite comparison proves

$$
d>\frac58,
\qquad
\widehat q<\frac{159}{400},
\qquad
\frac{x_0}{K}>\frac{241}{480}
=\frac12+\frac1{480}.
$$

With $B=14/3$ and the synthetic comparison

$$
S_*(P,r)=\frac{13P-8r}{5},
$$

the complete fixed-$r$ path has derivative cap and reserve

$$
\frac{2260740364246}{708624500625}<\frac{16}{5},
\qquad
\frac{6858037754}{708624500625}>0,
$$

while the comparison slope is $92/15$. The endpoint, dangerous-payment,
and safe-payment reserves are, respectively,

$$
\frac{2505132463469}{2616573970125}>0,
\qquad
\frac{80132733}{3024175}>0,
\qquad
\frac{114694733}{3024175}>0.
$$

The action gain satisfies the exact lower comparison $280000/17281$, and an
independent clean-room reconstruction closes the same enlarged domain by a
distinct cosine-gap self-consistency route. Both proofs own every exceptional
branch, strict wall, threshold face, and possible unit floor loss. Therefore,
including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac16,
\quad
K\ge\frac{54}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

The retained Round 14 threshold $K\ge32/\varepsilon^2$ remains sharper on
$0<\varepsilon\le1/8$, the retained Round 13 threshold
$K\ge24/\varepsilon^2$ remains sharper on $0<\varepsilon\le1/10$, and the
retained Round 10 threshold $K\ge20/\varepsilon^2$ remains sharper on
$0<\varepsilon\le1/25$. The failed $\kappa=53$ localization proxy and the
failed $Y=294$ central proxy are obstructions to those particular comparison
routes, not counterexamples to any stronger theorem.

## Complete thin-shell endpoint (Round 16)

Write

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac18,
\qquad
a=\varepsilon K.
$$

Round 16 proves this endpoint by two independent inclusive pieces. On the
low piece

$$
0\le a\le\frac{\pi}{4\varepsilon},
$$

the radial form comparison has the correct upper-count direction. Strict
radial counting gives

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\}.
$$

The comparison count is zero for $0\le a\le\pi$, including the wall
$a=\pi$. For $a>\pi$, write $a/\pi=N+t$ with $N\ge1$ and $0<t\le1$,
using $(N,t)=(m-1,1)$ at the strict radial wall $a=m\pi$. The exact product
deficit is

$$
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3},
$$

and the complete-square argument proves

$$
D(a)>\frac25a^2.
$$

The cubic remainder has exact minimum $-8/375$, and the $N=1$ lower screen
is $32/375>0$. The complete angular-ceiling and quarter-disk cost is at
most

$$
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
$$

At the closed ratio face, the exact remaining reserve is

$$
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
$$

Thus the low comparison is strict for $a>0$ and includes the optical face
$a=\pi/(4\varepsilon)$.

On the high piece

$$
a\ge\frac{\pi}{4\varepsilon},
$$

let $R:[0,T]\to[0,a]$ be the decreasing inverse of the exact piecewise
shell action, and set $F=R^2$ and $g=-F'$. The curvature audit proves that
$g$ decreases before and increases after the actual ungridded interface
$\tau$. The improper trace at $t=0$, the terminal trace, and the interface
values are included. Exact shifted-sawtooth Stieltjes integration gives

$$
D_{\rm rad}
\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4},
$$

while strict half-integer angular counting gives the complete error

$$
E=\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
$$

The lower screen decreases and the upper screen increases throughout
$0<\varepsilon\le1/8$. At the closed endpoint,

$$
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
$$

so the exact high-piece reserve is

$$
D_{\rm rad}-E>\frac{143}{4096}a^2>0.
$$

This closes the full strict comparison $P_{\mathcal A}<I$ and the permitted
phase transfer. It is not merely an endpoint calculation. The high piece
also includes $a=\pi/(4\varepsilon)$, so both pieces own their common face.
At the corner $(\varepsilon,a)=(1/8,2\pi)$ this is simultaneously the
strict radial wall with $(N,t)=(1,1)$.

The two closed pieces cover every $a\ge0$. At $K=0$ both sides vanish; for
$K>0$ the product or phase-proxy comparison is strict. Therefore

$$
\boxed{
\frac78\le\rho<1,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Every radial, product-angular, action-radial, half-integer, phase-proxy, and
sawtooth wall is owned with the strict convention. The proof uses no
domain-sensitive conclusion from the Round 5 product theorem, Round 6
aggregate theorem, or Round 11 endpoint. The frozen proof, isolated
reconstruction, adversarial audit, and exact ledger are recorded in
`rounds/polya-main/round_016/` and
`computations/round16_verify_endpoint.py`.

### Retained Round 11 endpoint (historical)

The earlier accepted endpoint $99/100\le\rho<1$ remains a valid standalone
theorem. Its low union covered
$0\le a\le1/(8\varepsilon^{3/2})$ by the product and aggregate arguments.
On the complementary range, its direct action proof obtained

$$
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a
$$

with normalized reserve $61/1400>0$, while its isolated reconstruction
proved

$$
D\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}
$$

with margin $4119252993/17500000000>0$. Those accepted arguments and their
ledger remain in `rounds/polya-main/round_011/` and
`computations/round11_verify_ultrathin_bridge.py`; the stronger Round 16
endpoint is now operative.

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
I_{16}=\left[\rho_*,\frac78\right],
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

For $1/16\le\rho\le5/6$, the strict count is zero below
$\pi/(1-\rho)$ and the fixed-ratio theorem applies above $K_0(\rho)$. The
positive-root equation

$$
\eta y^2-\sqrt a\,y-C_0=0,
\qquad y=\sqrt{K_0},
$$

shows that $K_0(\rho)$ is increasing. At $\rho=5/6$, the independent
fixed-ratio calculation at $Y=295$ has exact positive quadratic margin

$$
\frac{5226}{1225}>0.
$$

Its unique positive root therefore lies below $295$, so

$$
K_0(5/6)<295^2=87025.
$$

Write $\varepsilon=1-\rho$. The accepted theorems give the four-zone
envelope

1. on $[\rho_*,1/16]$, a residual point can occur only for $K<64$;
2. on $[1/16,5/6]$, a residual point can occur only for
   $K<K_0(\rho)\le K_0(5/6)<295^2=87025$;
3. on $[5/6,7/8]$, a residual point can occur only for
   $K<54/\varepsilon^2\le3456$;
4. on $[7/8,1)$, the complete Round 16 endpoint covers every $K\ge0$.

The complete thin endpoint owns the shared face $\rho=7/8$. Every other
shared ratio and threshold face is owned by one of the adjacent accepted
theorems. In particular, the residual inequalities are strict, so the faces
$K=64$, $K=K_0(5/6)$, $K=3456$, and $K=295^2$ are covered. The compact
conclusion is

$$
\boxed{
\rho\in I_{16},\quad K\ge295^2=87025
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Combining this with the complete small-hole and complete thin endpoint
theorems yields the global analytic high-frequency result

$$
\boxed{
0<\rho<1,\quad K\ge295^2=87025
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

Let $\mathcal A_{16}$ denote the complete accepted analytic cover, including
every theorem domain and owned threshold face in the four-zone union. The
actual unresolved set is

$$
\mathcal D_{16}
=(I_{16}\times[0,\infty))\setminus\mathcal A_{16}.
$$

This is an exact, nonrectangular complement of the accepted cover. It lies
below the displayed piecewise envelope, but it is not the rectangle
$I_{16}\times[0,87025)$ and must never be replaced by that rectangle.

## First angular bands above the zero-count wall (Round 17)

Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_1(\rho)=\sqrt{z_\rho^2+2},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
$$

Round 17 proves the strict comparison on the complete closed band

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_2(\rho).
}
$$

After the unitary radial transformation, angular channel $\ell$ is governed
on $(\rho,1)$ by

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}.
$$

Because $r^{-2}\ge1$, the Dirichlet min--max principle gives

$$
\lambda_{\ell,n}\ge n^2z_\rho^2+\ell(\ell+1).
\tag{R17.1}
$$

For $\ell=0$ this is exact: $\lambda_{0,n}=n^2z_\rho^2$. Throughout the
band, every $n\ge2$ mode lies above $K^2$, and every $\ell\ge2$ first mode
lies at or above $z_\rho^2+6\ge K^2$. Strict counting therefore yields

$$
N_D(A_{\rho,1},K^2)=
\begin{cases}
0,&K=z_\rho,\\
1,&z_\rho<K\le k_1(\rho),
\end{cases}
$$

and

$$
N_D(A_{\rho,1},K^2)\le1+3=4
\qquad
\bigl(k_1(\rho)<K\le k_2(\rho)\bigr).
\tag{R17.2}
$$

The inclusive $k_1$ and $k_2$ faces are handled by the strict spectral
convention. Accidental cross-order coincidences cannot increase the cap,
because the full angular multiplicities have already been included.

For

$$
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3,
$$

the first band is paid at its lower wall:

$$
W(\rho,z_\rho)
=\frac{2\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}
>2>1.
\tag{R17.3}
$$

For the second band, $F(\rho)=W(\rho,k_1(\rho))$ is strictly increasing,
since, with $e=1-\rho$ and $S=1+\rho+\rho^2$,

$$
\frac{F'(\rho)}{F(\rho)}
=\frac{1+2\rho}{S}
+\frac{2(\pi^2-e^2)}{e(\pi^2+2e^2)}>0.
$$

An exact rational evaluation at the left face gives

$$
F(\rho_c)
>4+\frac{18372917357}{92514296875}>4.
\tag{R17.4}
$$

Equations (R17.2)--(R17.4), together with monotonicity in $K$, prove

$$
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3
$$

on the complete stated band.

Its genuinely new part is

$$
\mathcal C_{17}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad z_\rho<K\le k_2(\rho)
\right\}.
$$

Exact comparison with every frozen lower and upper mask branch proves
$\mathcal C_{17}\subset\mathcal D_{16}$. Thus

$$
\mathcal A_{17}=\mathcal A_{16}\cup\overline{\mathcal C}_{17},
\qquad
\mathcal D_{17}=\mathcal D_{16}\setminus\mathcal C_{17},
$$

where the bar denotes the complete closed theorem band. In explicit form,

$$
\boxed{
\mathcal D_{17}
=\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\le\rho<\frac78,
\ k_2(\rho)<K<U(\rho)\right\}.
}
\tag{R17.5}
$$

Here $U(\rho)$ is the exact Round 17 frozen upper floor: $H_0(\rho)$ below
$\rho_{HK}$, $K_0(\rho)$ from $\rho_{HK}$ to $5/6$, and
$54/(1-\rho)^2$ from $5/6$ to $7/8$. The lower wall $K=z_\rho$ and the
ratio face $\rho=7/8$ remain owned by the earlier zero-count and endpoint
theorems. The residual (R17.5) is nonempty, so this compression does not
prove the full shell theorem.

Immediately above $k_2$, (R17.1) must permit the $\ell=2$ channel and the
coarse multiplicity cap jumps from $4$ to $1+3+5=9$. At the left ratio
face,

$$
W\bigl(\rho_c,k_2(\rho_c)\bigr)<9.
$$

Hence this same all-at-once cap cannot continue uniformly through the third
angular band. This is the historical Round 17 method obstruction, not a
counterexample to the target inequality. Round 18 resolves it through
$k_5$ with delayed fixed-channel entries.

## Delayed angular-entry staircase through $k_5$ (Round 18)

For $m\in\mathbb N_0$, set

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
$$

Round 18 proves

$$
\boxed{
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_5(\rho)
}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<W(\rho,K).
\tag{R18.1}
$$

The Round 17 theorem already owns $z_\rho\le K\le k_2(\rho)$. To treat
$k_2<K\le k_5$, first note that $z_\rho\ge\pi+1/2>7/2$. Hence

$$
4z_\rho^2-k_5(\rho)^2
=3z_\rho^2-30>\frac{27}{4}>0.
\tag{R18.2}
$$

The lower bound (R17.1) therefore excludes every $n\ge2$ mode through the
closed $K=k_5$ face. It also excludes every first mode with $\ell\ge5$,
because $z_\rho^2+\ell(\ell+1)\ge z_\rho^2+30=k_5^2$. Only the first
radial modes in channels $\ell=0,1,2,3,4$ can contribute.

The delayed first entries use a fixed-channel comparison that is proved
inside the project. For

$$
\mathfrak a_\ell^\rho[u]
=\int_\rho^1\left(|u'|^2+
\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak a_\ell^\rho)=H_0^1(\rho,1),
$$

extend $u$ by zero across $(0,\rho]$. Its zero trace gives a member of the
unit-ball fixed-$\ell$ form domain; the extension preserves the norm, the
form, and the angular subspace. Min--max in that same channel gives the
first inequality below; the audited unit-ball separation formula gives the
equality:

$$
\boxed{
\lambda_{\ell,1}^{\rm shell}(\rho)
\ge\lambda_{\ell,1}^{\rm ball}
=j_{\ell+1/2,1}^2.}
\tag{R18.3}
$$

This is an internal variational argument, not an assertion imported from
Lorch. The audited external dependency supplies only

$$
j_{5/2,1}>c_2=\frac{51}{10},\qquad
j_{7/2,1}>c_3=\frac{13}{2},\qquad
j_{9/2,1}>c_4=\frac{15}{2}.
\tag{R18.4}
$$

The SIAM publisher abstract states the strict inequalities used, the
first-positive-zero convention, and the scope $\nu>-1$; DLMF supplies the
spherical-Bessel identity. The full Lorch paper was access-controlled, so
this is a qualified statement-level dependency rather than a reconstruction
of its proof. No shell cross-product bound, shell-to-ball comparison,
higher-radial exclusion, multiplicity count, or Weyl payment is attributed
to Lorch.

Let

$$
F_m(\rho)=W(\rho,k_m(\rho)),qquad
e=1-\rho,qquad S=1+\rho+\rho^2,qquad c=m(m+1).
$$

Then

$$
F_m(\rho)=\frac{2}{9\pi}\frac{S}{e^2}
(\pi^2+ce^2)^{3/2}.
$$

After multiplying its logarithmic derivative by the positive denominator,
its sign is the sign of

$$
3\left[\pi^2(1+\rho)-c\rho^2(1-\rho)^2\right]>0
\qquad(m\le5),
\tag{R18.5}
$$

because $c\le30$, $\rho^2(1-\rho)^2\le1/16$, and $\pi>3$. Thus all
moving-wall payments used below are strictly increasing.

The three delayed-entry bridges use

$$
(r_2,r_3,r_4)=\left(\frac3{10},\frac12,\frac12\right)
$$

and the exact split payments

$$
\begin{aligned}
W\left(\frac3{10},\frac{51}{10}\right)
&>\frac{100387329}{11000000}>9,\\
W\left(\frac12,\frac{13}{2}\right)
&>\frac{107653}{6336}>16,\\
W\left(\frac12,\frac{15}{2}\right)
&>\frac{18375}{704}>25.
\end{aligned}
\tag{R18.6}
$$

At the corresponding splits the moving walls lie above the fixed
thresholds, with exact positive squared reserves

$$
\frac{1802859}{13764100},\qquad
\frac{103667}{11236},\qquad
\frac{36251}{11236}.
\tag{R18.7}
$$

If the first mode in channel $m\in\{2,3,4\}$ contributes, (R17.1),
(R18.3), and (R18.4) force both $K>k_m(\rho)$ and $K>c_m$. For
$\rho\le r_m$, monotonicity of $(1-\rho^3)$ pays at the fixed threshold
$c_m$; for $\rho\ge r_m$, (R18.5) pays at the moving wall $k_m$. Equations
(R18.6)--(R18.7) cover both one-sided traces, coincident thresholds, and
empty subbands. The available cumulative strict-count upper caps are exactly

$$
4,\qquad9,\qquad16,\qquad25,
\tag{R18.8}
$$

the sums of the full multiplicities $2\ell+1$. If none of the
$\ell=2,3,4$ channels contributes, the cap is $4$ and
$K>k_2>k_1$ together with (R17.4) gives $W(\rho,K)>4$. Otherwise choose
the largest contributing $m\in\{2,3,4\}$; all higher channels are absent,
the cap is $(m+1)^2$, and the corresponding bridge pays it strictly.
Strict counting excludes a new channel on each equality wall $K=k_m$ and
$K=c_m$; accidental cross-order coincidences cannot exceed the cumulative
cap. This proves (R18.1), including $K=k_5$ and both ratio faces.

The genuinely new part is

$$
\mathcal C_{18}
=\left\{\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K\le k_5(\rho)\right\}.
\tag{R18.9}
$$

The upper-floor audit first gives $k_5<26$ on the closed ratio band. The
$H_0$ branch ends below $\rho_c$; on the active fixed-ratio branch one has
$26<64<K_0$, while on the seam branch
$26<1944\le54/(1-\rho)^2$. Hence

$$
k_5(\rho)<U(\rho),
\qquad \mathcal C_{18}\subset\mathcal D_{17}.
\tag{R18.10}
$$

Exact subtraction now gives the accepted current residual

$$
\boxed{
\mathcal D_{18}
=\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}
\cup
\left\{\rho_c\le\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.}
\tag{R18.11}
$$

Every displayed frequency inequality in (R18.11) is strict. The old
$K=k_2$ owner is unchanged, $K=k_5$ is newly covered, and $\rho=7/8$
retains its endpoint owner. The residual is nonempty: the exact audited
chain

$$
k_5(1/2)<26<30<64<K_0(1/2)=U(1/2)
$$

puts $(1/2,30)$ in its second component.

The proof stops at a genuine method boundary. At the left ratio face,

$$
k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c),
\tag{R18.12}
$$

and the exact $\ell=0,n=2$ mode enters immediately above $2z_{\rho_c}$.
The one-radial-mode cap therefore cannot simply continue to $k_6$. This is
not a counterexample; the next band requires a combined radial-entry and
angular staircase.

## Certified central regression boxes

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

so the certified margin exceeds $14.6073155354$. This is the retained Round 8
box $B_0$.

Round 17 independently certifies the face-connected extension

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

The complete lower face of $B_1$ is the complete upper face of $B_0$.
Outward Arb determinant signs and an independent exact-rational checker
again give exactly one root in each of $\ell=0,1$, no other contributing
mode, and exact strict count $4$. At the true Weyl worst corner the strict
margin is greater than

$$
\frac{39657181883797}{2685546875000}>0.
$$

Exact set arithmetic gives

$$
B_0\cup B_1\subset\mathcal C_{17}.
$$

Both certificates therefore remain independent regression evidence but are
analytically redundant after promotion of the Round 17 band. They do not
subtract anything further from $\mathcal D_{18}$, do not promote sampled
numerics to proof, and do not make `COMP-certified-bessel` more than
`diagnostic_only`.

## Remaining gates

This file must not be cited as a proof of the full shell theorem. The open
obligations `SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, and `POLYA-program-target` remain open. The gates are:

- analytic or symbolic closure of the exact two-piece residual
  $\mathcal D_{18}$, followed only where necessary by rigorous,
  face-connected certification inside that same residual;
- preservation of the exact accepted mask $\mathcal A_{18}$ and every owned
  face; a coarse envelope or rectangle is not an admissible substitute;
- construction above $k_5$ must resolve the relative $2z_\rho$ and
  $k_6(\rho)$ radial/angular walls, while the unchanged
  $\rho_*<\rho<\rho_c$ component is handled separately;
- a fresh final theorem-level clean-room reconstruction and adversarial
  review after the compact residual is closed. Agent consensus is not a
  proof, and finite ledgers certify only the arithmetic they execute.
