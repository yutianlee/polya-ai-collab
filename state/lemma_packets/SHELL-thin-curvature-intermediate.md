# Lemma Packet: Radius-Sensitive Closure of the Thin-Shell Endpoint

Obligation: `SHELL-thin-curvature-intermediate`.

Parent: `SHELL-rho-one-endpoint`.

## Exact combined theorem

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\varepsilon_*:=\frac1{262144},
\qquad
a=\varepsilon K.
$$

Prove, with strict spectral counting, that

$$
\boxed{
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
\qquad(K\ge0).
}
\tag{1}
$$

The proof must be the explicit overlap of the following three ranges:

1. the proved Round 5 product range

   $$
   0\le K\le\frac{\pi}{4\varepsilon^2};
   \tag{2}
   $$

2. the radius-sensitive aggregate-action range

   $$
   \frac{\pi}{4\varepsilon^2}
   \le K\le
   \frac1{8\varepsilon^{5/2}};
   \tag{3}
   $$

3. the radius-sensitive local-plateau range

   $$
   K\ge\frac{64}{\varepsilon^2}.
   \tag{4}
   $$

The endpoint constant is exact for this proof because

$$
\frac1{8\varepsilon^{5/2}}
\ge\frac{64}{\varepsilon^2}
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{512^2}
=\frac1{262144}.
\tag{5}
$$

Equality in (5) is allowed: both analytic component ranges include their
endpoints.

## Component A: exact scaled action

Use

$$
y=\varepsilon\nu,
$$

and

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-
\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds.
\tag{6}
$$

This is exactly

$$
G_K(\nu)-G_{\rho K}(\nu).
\tag{7}
$$

For the strict half-integer mesh

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
$$

define

$$
q_\ell=
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<.
\tag{8}
$$

The audited phase enclosure and exact spectral bridge give

$$
N_D(A_{\rho,1},K^2)
\le
\sum_{y_\ell<a}\frac{2y_\ell}{\varepsilon}q_\ell.
\tag{9}
$$

Set

$$
P_{\mathcal A}
=\varepsilon\sum_{y_\ell<a}y_\ell q_\ell,
\qquad
I_{\varepsilon,a}
=\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy.
\tag{10}
$$

The desired shell inequality is implied exactly by

$$
P_{\mathcal A}\le I_{\varepsilon,a}.
\tag{11}
$$

Fubini must recover the mean shell cross-section without a pointwise-radius
replacement:

$$
\boxed{
I_{\varepsilon,a}
=\frac{m_\varepsilon a^3}{3\pi},
\qquad
m_\varepsilon
=1-\varepsilon+\frac{\varepsilon^2}{3}
=\frac1\varepsilon\int_{1-\varepsilon}^1r^2\,dr.
}
\tag{12}
$$

## Component B: mean-square-radius aggregate range

Define the effective semicircle action

$$
\mathcal B_{\varepsilon,a}(y)
=\frac1\pi
\sqrt{a^2-\frac{y^2}{m_\varepsilon}}_+.
\tag{13}
$$

For $0\le y\le\rho a$, Jensen's inequality applied to the concave function

$$
z\longmapsto\sqrt{a^2-y^2/z}
$$

must give

$$
\mathcal A_{\varepsilon,a}(y)
\le\mathcal B_{\varepsilon,a}(y).
\tag{14}
$$

The comparison is deliberately not asserted for $y>\rho a$; a positive
whispering-gallery strip remains where $\mathcal B$ may already vanish.

Define

$$
P_{\mathcal B}
=\varepsilon\sum_{\ell\ge0}y_\ell
\left[\mathcal B_{\varepsilon,a}(y_\ell)+\frac14\right]_<.
\tag{15}
$$

The aggregate proof must establish, for
$0<\varepsilon\le1/100$ and $a\ge\pi/(4\varepsilon)$,

$$
\boxed{
I_{\varepsilon,a}-P_{\mathcal B}>\frac{a^2}{12}.
}
\tag{16}
$$

One endpoint-safe route uses the radial levels

$$
x_n=n-\frac14,
\qquad
b_n=\sqrt{a^2-\pi^2x_n^2},
$$

and the strict angular count

$$
M_n
=\max\left\{0,
\left\lceil\frac{\sqrt{m_\varepsilon}b_n}{\varepsilon}
-\frac12\right\rceil\right\}.
\tag{17}
$$

If $t=a/\pi$, $N=\#\{n\ge1:n-1/4<t\}$, and $u=t-N$, then

$$
-\frac14<u\le\frac34
$$

and the exact shifted deficit is

$$
\boxed{
\frac1{\pi^2}
\left(
\frac{2a^3}{3\pi}-\sum_{n=1}^{N}b_n^2
\right)
=\frac{N^2}{4}
+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}.
}
\tag{18}
$$

Required auxiliary bounds are

$$
D\ge\frac{\pi^2N^2}{5},
\qquad
\sum_{n=1}^{N}b_n
\le\frac{a^2}{4}+\frac a4,
\tag{19}
$$

together with the exact angular ceiling

$$
M_n<\frac{\sqrt{m_\varepsilon}b_n}{\varepsilon}+\frac12.
\tag{20}
$$

The outer strip must be paid rather than deleted.  It contains at most
$a+1$ mesh points, and

$$
\mathcal A_{\varepsilon,a}(\rho a)
\le\frac{a\sqrt{2\varepsilon}}{\pi}.
\tag{21}
$$

Therefore, for

$$
\frac{\pi}{4\varepsilon}
\le a\le\frac1{8\varepsilon^{3/2}},
$$

the required correction is bounded by

$$
E_{\rm out}
=\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}\pi+1\right)
<\frac{a^2}{12}.
\tag{22}
$$

Equations (14), (16), and (22) prove (11) in the entire range (3).

## Component C: local-plateau high-thin range

For an ordinary-floor shifted tail beginning at
$x_0=r+1/2<\mu=\rho K$, use

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
$$

and let $p$ be the last index in the initial constant-floor plateau of
$A_{\rho,K}(x_0+j)+1/4$.  Put

$$
m=n-p,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
\qquad
\eta=G_1(\rho).
$$

The audited concave-head/convex-tail decomposition gives

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A_{\rho,K}(z)\,dz
+\delta-\frac M4,
\tag{23}
$$

where

$$
0\le\delta<\frac{2\sqrt2}{15},
\qquad
M=\lfloor K\eta\rfloor+dm-p.
\tag{24}
$$

The new estimate must retain the plateau location.  If
$R=p-dm>0$, prove first that $x_0\ge K/2$.  Then use

$$
\sigma(z):=-A_{\rho,K}'(z)
=\frac1\pi
\left(
\arccos\frac zK-
\arccos\frac z{\rho K}
\right)
\ge
\frac{\varepsilon z}{\pi\sqrt{K^2-z^2}}
\tag{25}
$$

and the plateau drop

$$
A(x_0)-A(x_0+p)<1
$$

to prove, for $K\ge64\varepsilon^{-2}$,

$$
\boxed{
p<\frac{10}{\sqrt\varepsilon},
\qquad
R<\frac{10}{\sqrt\varepsilon}.
}
\tag{26}
$$

Finally,

$$
\eta
=\frac1\pi\int_0^\varepsilon
\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}
\tag{27}
$$

must give

$$
M>
K\eta-1-\frac{10}{\sqrt\varepsilon}
>\frac{17}{3}
>4\delta.
\tag{28}
$$

This proves every low-interface tail.  The already-proved convex theorem
handles tails beginning at or above $\mu$, so the multiplicity scaffold
proves (4).

## Permitted dependencies

- `CONV-strict-counting`
- `SHELL-sturm-liouville-completeness`
- `SHELL-phase-enclosures`
- `SHELL-weighted-lattice-scaffold`
- `SHELL-high-angular-shifted-tails`
- `SHELL-low-interface-fixed-rho-high-energy`, only for its unconditional
  concave-head/convex-tail decomposition before the old threshold estimate
- `SHELL-thin-product-low-optical`
- the audited FLPS annulus floor theorems already recorded in
  `sources/annuli_polya.md`
- elementary finite sums, Jensen's inequality, and one-variable calculus

No floating-point scan, Bessel-root table, uncertified quadrature, or
asymptotic expansion is permitted in the proof.

## Falsification cases

- $\varepsilon=1/262144$, where the two new ranges meet exactly;
- $K=\pi/(4\varepsilon^2)$ and
  $K=1/(8\varepsilon^{5/2})$;
- $K=64/\varepsilon^2$;
- $\mathcal A(y_\ell)+1/4\in\mathbb N$;
- $n-1/4=a/\pi$ in the effective radial sum;
- $\sqrt{m_\varepsilon}b_n/\varepsilon\in\mathbb Z+1/2$;
- $y_\ell=\rho a$ and $y_\ell=a$;
- the fact that $\mathcal B$ is not a global pointwise majorant;
- the no-floor-drop branch $p=n$;
- the immediate-drop branch $p=0$;
- the purely convex branch $n=0$;
- accidental replacement of the strict phase count by an ordinary floor;
- confusing diagnostic scans with proof.

## Promotion rule

Promotion requires:

1. a frozen proof of the aggregate-action range;
2. an isolated clean-room reconstruction of that range;
3. a frozen proof and isolated reconstruction of the local-plateau range;
4. an adversarial constants and wall audit of both components;
5. exact verification of the overlap (5).

If all gates pass, promote both `SHELL-thin-curvature-intermediate` and
`SHELL-rho-one-endpoint`.  The thin endpoint then requires no finite Bessel
certificate.  `SHELL-rho-compact`, `SHELL-rho-zero-endpoint`,
`SHELL-rho-uniformity`, `COMP-certified-bessel`, and `TARGET-shell-d3`
remain separate open obligations.
