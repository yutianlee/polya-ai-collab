# Round 9 incumbent: an optimized thin local-plateau theorem

## Verdict

Let

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le\frac1{100}.
$$

The audited Round 3 shifted-tail decomposition closes under the strictly
smaller threshold

$$
\boxed{K\ge \frac{18}{\varepsilon^2}.}
\tag{1}
$$

Consequently, subject only to the already-promoted high-interface tail,
weighted scaffold, phase enclosure, and exact spectral bridge,

$$
\boxed{
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
\quad
\left(K\ge\frac{18}{\varepsilon^2}\right).
}
\tag{2}
$$

No estimate proved under the old hypothesis
$K\ge64\varepsilon^{-2}$ is used below.  In particular, the dangerous
plateau is relocated and its length is rederived directly from (1).

Combining (2) with the already-proved range

$$
0\le K\le \frac1{8\varepsilon^{5/2}}
\tag{3}
$$

gives the exact enlarged endpoint

$$
\boxed{
\varepsilon_{\rm new}=\frac1{20736}=\frac1{144^2},
\qquad
1-\frac1{20736}\le\rho<1.
}
\tag{4}
$$

The constant $18$ is a simple self-consistent improvement, not a claim of
optimality.

## 1. Frozen input from Round 3

Put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
\eta=G_1(\rho),
$$

and consider a low-interface shifted tail beginning at the half-integer
$x_0=r+1/2<\mu$.  Define

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1).
$$

For $n\ge1$, let $p$ be the last index in the initial constant ordinary-floor
plateau of

$$
A(x_0+j)+\frac14,
\qquad 0\le j\le n.
$$

If there is no drop, set $p=n$.  Put $m=n-p$.  If $n=0$, the Round 3
convention is $p=m=0$ and the concave block is absent.

The audited concave-head/convex-tail assembly gives

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta-\frac M4,
\tag{5}
$$

where

$$
0\le\delta=\int_q^\mu G_\mu(z)\,dz
<\frac{2\sqrt2}{15},
\tag{6}
$$

$$
M=L+dm-p,
\qquad
L=\lfloor K\eta\rfloor,
\qquad
d=1-\frac{2\arccos\rho}{\pi}.
\tag{7}
$$

The same Round 3 curvature argument, which has no high-energy hypothesis,
gives

$$
\boxed{
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
}
\tag{8}
$$

The no-drop case uses Proposition 3.1 rather than the first-drop theorem;
nevertheless (5)--(8) remain valid with $p=n$.  Thus it is enough to prove
$M>4\delta$ for every branch.

## 2. Exact elementary constants

Only the following rational bounds are used:

$$
\boxed{
\pi<\frac{355}{113},
\qquad
\frac{140}{99}<\sqrt2<\frac32.
}
\tag{9}
$$

The square-root bounds follow by squaring:
$19600<2\cdot9801$ and $2<9/4$.  For a fully rational certificate of the
$\pi$ bound, Machin's identity and alternating arctangent sums give

$$
\pi
<16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
<\frac{355}{113};
$$

the difference between the last rational majorant and $355/113$ in the
required direction is certified by

$$
\frac{355}{113}
-\left[
16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
\right]
=
\frac{45167474711}{189820334689453125}>0.
\tag{10}
$$

Finally,

$$
\eta
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge
\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{11}
$$

Indeed, $\cos\theta\ge1-\theta^2/2$ implies
$\arccos(1-v)\ge\sqrt{2v}$.  Equations (9) and (11) are the only
rationalization of $G_1$ used below.

## 3. The exact dangerous branch

Define the possible interface loss

$$
R=p-dm.
\tag{12}
$$

If $R\le0$, then $M=L-R\ge L$ and there is no plateau loss.  Suppose now
that $R>0$.  Then $p>0$ and $dm<p$.

The identity

$$
\arccos(1-\varepsilon)
=2\arcsin\sqrt{\varepsilon/2}
\le\pi\sqrt{\varepsilon/2}
$$

uses the chord bound $\arcsin u\le(\pi/2)u$.  Hence

$$
\frac{\arccos\rho}{\pi}
\le\sqrt{\frac\varepsilon2}<\frac1{10},
\qquad
\boxed{d>\frac45.}
\tag{13}
$$

It follows in the dangerous branch that

$$
m<\frac p d<\frac54p.
\tag{14}
$$

Writing

$$
U:=\mu-x_0=n+\beta=p+m+\beta,
$$

we therefore obtain the strict geometric bound

$$
\boxed{U<1+\frac94p.}
\tag{15}
$$

This branch includes $p=n>0$ with no floor drop, where $m=0$.  An immediate
drop has $p=0$ and hence $R=-dm\le0$.  The case $n=0$ has $p=m=0$ and is
also in the easy branch.

## 4. Relocating the dangerous plateau under $C=18$

Let

$$
t=\frac{x_0}{\mu}=1-\frac U\mu.
$$

Divide (15) by $\mu=\rho K$ and use the unconditional estimate (8):

$$
\frac U\mu
<
\frac1{\rho K}
+\frac94\sqrt{\frac{2\pi}{\varepsilon\rho K}}.
\tag{16}
$$

Under (1), $\rho\ge99/100$, and $\varepsilon\le1/100$,

$$
\frac1{\rho K}\le\frac1{178200},
\qquad
\frac{2\pi}{\varepsilon\rho K}
\le\frac\pi{891}.
\tag{17}
$$

Set

$$
S=\frac49\left(\frac{67}{500}-\frac1{178200}\right)
=\frac{119389}{2004750}.
$$

The bound in (9) and the exact square comparison

$$
S^2-\frac{355}{113\cdot891}
=
\frac{9377802773}{454149549562500}>0
\tag{18}
$$

show that $\sqrt{\pi/891}<S$.  Substitution in (16)--(17) gives

$$
\frac U\mu<\frac{67}{500},
\qquad
\boxed{t>\frac{433}{500}.}
\tag{19}
$$

This is the first place where the new threshold enters.  It is derived
directly from $18\varepsilon^{-2}$; the old $64\varepsilon^{-2}$
localization is not imported.

## 5. Local slope and the new quadratic shelf bound

For $0<z<\mu$, put $\sigma(z)=-A'(z)$.  At $x_0=\mu t$,

$$
\begin{aligned}
\sigma(x_0)
&=\frac1\pi\bigl(\arccos(\rho t)-\arccos t\bigr)\\
&=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}\\
&\ge\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\end{aligned}
\tag{20}
$$

Since $\rho t=x_0/K=\rho-U/K$,

$$
1-\rho^2t^2
\le2(1-\rho t)
=2\left(\varepsilon+\frac UK\right).
$$

Together with (19), this yields

$$
\sigma(x_0)
>
\frac{433\varepsilon}
{500\pi\sqrt{2(\varepsilon+U/K)}}.
\tag{21}
$$

Constancy of the initial ordinary floor, including at an integer floor
wall, gives

$$
A(x_0)-A(x_0+p)<1.
\tag{22}
$$

The function $\sigma$ is increasing on $[0,\mu]$, so

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
$$

Using (1), (15), and (21), we obtain the entirely new quadratic estimate

$$
p^2
<A_0\left(
\frac1\varepsilon+\frac1{18}+\frac p8
\right),
\qquad
A_0:=\frac{2\pi^2}{(433/500)^2}.
\tag{23}
$$

The rational bounds in (9) give

$$
A_0
<2\left(\frac{355}{113}\right)^2
\left(\frac{500}{433}\right)^2
=\frac{63012500000}{2394047041}
<\frac{1053}{40};
\tag{24}
$$

the last difference is
$431534173/95761881640>0$.

Put $x=\varepsilon^{-1/2}\ge10$, $B=53/10$, and

$$
F_x(s)=s^2-\frac{1053}{320}s
-\frac{1053}{40}\left(x^2+\frac1{18}\right).
$$

At $P=Bx$,

$$
F_{10}(53)=\frac{203}{320}>0,
\tag{25}
$$

and the derivative of $F_x(Bx)$ with respect to $x$ at $x=10$ is

$$
\frac{57151}{3200}>0.
\tag{26}
$$

Indeed,

$$
B^2-\frac{1053}{40}=\frac{353}{200}>0,
$$

so that derivative increases with $x$.  Also
$\partial_sF_x(s)=2s-1053/320>0$ for $s\ge Bx\ge53$.  Therefore
(23)--(26) exclude $p\ge Bx$ and prove

$$
\boxed{p<\frac{53}{10\sqrt\varepsilon}.}
\tag{27}
$$

This replaces, rather than imports, the Round 6 estimate
$p<8/\sqrt\varepsilon$.

## 6. The convex gain pays every branch

From (1), (9), and (11),

$$
K\eta
\ge\frac{36\sqrt2}{3\pi\sqrt\varepsilon}
>
\frac{12656}{2343\sqrt\varepsilon}.
\tag{28}
$$

Combining (27) and (28),

$$
K\eta-p
>
\left(\frac{12656}{2343}-\frac{53}{10}\right)
\frac1{\sqrt\varepsilon}
=\frac{2381}{23430\sqrt\varepsilon}
\ge\frac{2381}{2343}
=1+\frac{38}{2343}>1.
\tag{29}
$$

Because $p$ is an integer, (29) implies

$$
\boxed{L=\lfloor K\eta\rfloor\ge p+1}
\tag{30}
$$

even when $K\eta$ lies on an integer wall.

We now close every branch.

1. If $R>0$, then (7) and (30) give
   $$M=L+dm-p\ge1+dm\ge1.$$
2. If $R\le0$, then $M=L-R\ge L$.  Equation (28) and
   $\varepsilon^{-1/2}\ge10$ give $K\eta>50$, hence $L\ge1$.
3. The no-drop branch $p=n>0$ is included in item 1 with $m=0$, so
   $M=L-p\ge1$.
4. The immediate-drop branch $p=0$ is included in item 2.
5. If $n=0$, then $p=m=0$ and $M=L\ge1$ without invoking a concave
   theorem.

Finally, (6) and $\sqrt2<3/2$ imply

$$
4\delta<\frac{8\sqrt2}{15}<\frac45<1\le M.
\tag{31}
$$

Thus $M>4\delta$ in (5), and every low-interface shifted tail closes
strictly.  Notice that the decisive last step uses the integrality of
$L-p$; replacing the floor by a continuous estimate would discard the
small but sufficient margin in (29).

## 7. Spectral consequence and endpoint audit

The already-proved convex theorem controls tails with $x_0\ge\mu$.
Combining those tails with the result above and the promoted weighted
scaffold gives

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor
G_K(\nu_\ell)-G_{\rho K}(\nu_\ell)+\frac14
\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{32}
$$

The strict phase proxy is no larger than this ordinary-floor proxy, and the
exact separated spectral bridge yields (2).

All relevant endpoints are safe:

- **Threshold equality.**  $K=18\varepsilon^{-2}$ is included.  Strictness
  in (18), (22), (27), and (29) remains at equality.
- **No floor drop.**  $p=n$ uses the Round 3 Proposition 3.1 convention;
  no first-drop theorem is applied outside its hypotheses.
- **Immediate drop and degenerate head.**  These are the separate $p=0$
  and $n=0$ branches above; no division by $p$ occurs.
- **Interface wall.**  If $q=\mu$, then $\beta=0$ and $\delta=0$.
  Equations (15)--(31) remain valid.
- **Head floor wall.**  Two decreasing samples with the same ordinary
  floor differ by strictly less than one, which is exactly (22).
- **Gain wall.**  If $K\eta\in\mathbb Z$, (30) follows directly from the
  strict inequality $K\eta>p+1$.
- **Outer trapezoid wall.**  If $K-x_0$ is integral, the endpoint value is
  zero; otherwise the audited zero extension supplies the same endpoint.
- **Spectral wall.**  The transferred phase count is strict and is
  majorized by the ordinary floor in (32), including when the majorant is
  integral.

## 8. Exact overlap and reduction of the thin residual

Let

$$
H_{18}(\varepsilon)=\frac{18}{\varepsilon^2},
\qquad
L(\varepsilon)=\frac1{8\varepsilon^{5/2}}.
$$

The two inclusive analytic ranges cover every $K\ge0$ exactly when

$$
\frac{18}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
144\sqrt\varepsilon\le1
\iff
\boxed{\varepsilon\le\frac1{20736}}.
\tag{33}
$$

At equality,

$$
H_{18}(1/20736)=L(1/20736)
=2^{17}3^{10}=7739670528,
\tag{34}
$$

so no joining point is lost.  In optical variables the joining value is
$a=\varepsilon K=2^9 3^6=373248$.

Relative to the old $C=64$ theorem:

- the high-frequency ceiling at fixed $\varepsilon$ is multiplied by
  $18/64=9/32$;
- the uniform thin-neighborhood width is enlarged by
  $$
  \frac{1/20736}{2^{-18}}=\frac{1024}{81};
  $$
- the whole former residual band
  $2^{-18}\le\varepsilon\le1/20736$ disappears;
- for $1/20736<\varepsilon\le1/100$, the only remaining thin planning gap
  is
  $$
  \frac1{8\varepsilon^{5/2}}
  <K<
  \frac{18}{\varepsilon^2},
  $$
  whose upper-to-lower ratio is $144\sqrt\varepsilon$, instead of the old
  $512\sqrt\varepsilon$.

## Classification

- **Proved in this incumbent:** the $C=18$ local-plateau theorem and the
  exact overlap endpoint $\varepsilon_{\rm new}=1/20736$, conditional only
  on the already-audited Round 3 tail assembly and promoted spectral
  dependencies explicitly named above.
- **Not imported:** any bound whose proof assumes
  $K\ge64\varepsilon^{-2}$, including the old $p<8/\sqrt\varepsilon$.
- **Not claimed:** optimality of $18$, certification of the remaining thin
  gap, or promotion before isolated clean-room and adversarial review.
