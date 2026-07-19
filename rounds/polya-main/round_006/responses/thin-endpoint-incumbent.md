# Frozen Incumbent: Uniform Thin-Shell Endpoint

## Theorem

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le2^{-18}=\frac1{262144}.
$$

Then, for every $K\ge0$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

Equivalently, the strict Dirichlet Pólya inequality holds uniformly for

$$
1-2^{-18}\le\rho<1.
$$

This proof is entirely analytic and requires no finite Bessel certificate.

## 1. Low and aggregate-action ranges

Round 5 proves (1) for

$$
0\le K\le\frac{\pi}{4\varepsilon^2}.
\tag{2}
$$

The radius-sensitive action proof in
`rounds/polya-main/round_006/exploration/phase-aggregate.md` proves it for

$$
\frac{\pi}{4\varepsilon^2}
\le K\le
\frac1{8\varepsilon^{5/2}}.
\tag{3}
$$

Its exact scaled action is

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-
\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds,
\qquad a=\varepsilon K,
$$

and its continuous weighted integral is exactly

$$
\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
$$

Thus this component retains the required mean shell cross-section.  A
Jensen comparison with the volume-matched effective semicircle is used only
below the inner interface; the remaining whispering-gallery strip is paid
by an explicit $a^2/12$ lattice margin.  Every radial, angular, phase, and
turning-interface wall is strict.

Combining (2) and (3) proves (1) throughout

$$
0\le K\le L(\varepsilon)
:=\frac1{8\varepsilon^{5/2}}.
\tag{4}
$$

## 2. Uniform high-thin range

The local-plateau proof in
`rounds/polya-main/round_006/exploration/local-plateau-high-thin.md` proves
(1) for

$$
K\ge H(\varepsilon)
:=\frac{64}{\varepsilon^2}.
\tag{5}
$$

The improvement over the old $K_0(1-\varepsilon)=O(\varepsilon^{-4})$
threshold comes from retaining the tail's starting radius.  If $p$ is the
initial constant-floor plateau and $m$ is the remaining number of head
cells, the only possible loss is $R=p-dm$.  In the branch $R>0$, the exact
slope

$$
-A_{\rho,K}'(z)
=\frac1\pi
\left(
\arccos\frac zK-
\arccos\frac z{\rho K}
\right)
$$

forces $p=O(\varepsilon^{-1/2})$.  The convex-tail gain satisfies

$$
K G_1(1-\varepsilon)
\ge
\frac{2\sqrt2}{3\pi}K\varepsilon^{3/2},
$$

which dominates that plateau uniformly at (5).  The no-drop, immediate-drop,
and $n=0$ branches are included.

## 3. Exact overlap

The two thresholds satisfy

$$
H(\varepsilon)\le L(\varepsilon)
\quad\Longleftrightarrow\quad
\frac{64}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
\varepsilon\le2^{-18}.
$$

At $\varepsilon=2^{-18}$,

$$
H=L=2^{42}.
$$

Both component theorems include equality, so the joining frequency is not
lost.  Round 5 and the aggregate theorem cover $0\le K\le L$, while the
local-plateau theorem covers $H\le K<\infty$.  Their union is all
$K\ge0$, proving (1).

## Scope

This incumbent closes only the $\rho\uparrow1$ endpoint.  It does not prove
the compact-$\rho$ certificate, the $\rho\downarrow0$ endpoint, or the
all-$\rho$ shell theorem.
