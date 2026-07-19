# Clean-room review: uniform high-thin closure of every low-interface tail

## Verdict

**PASS.**  Let

$$
\varepsilon=1-\rho,
\qquad
0<\varepsilon\le\frac1{100},
\qquad
K\ge\frac{64}{\varepsilon^2}.
$$

Starting only from the proved Round 3 shifted-tail assembly, every tail with
$x_0<\mu=\rho K$ closes.  The apparent obstruction is the first-floor
plateau length $p$: the old global estimate

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}
$$

does not by itself close uniformly as $\varepsilon\downarrow0$.  In the only
case where the plateau can contribute negatively, the exact derivative

$$
\sigma(z)=-A'(z)
=\frac1\pi\left(
\arccos\frac zK-\arccos\frac z{\rho K}
\right)
$$

instead gives

$$
\boxed{p<\frac8{\sqrt\varepsilon}.}
$$

At the same time,

$$
\boxed{K\eta>\frac{14}{\sqrt\varepsilon},
\qquad \eta=G_1(\rho),}
$$

so the Round 3 compensation margin is much larger than the interface loss.
The no-drop case $p=n$, the degenerate head $n=0$, immediate drops, and all
integer walls are included.

**First unsupported implication:** none in the stated low-interface claim.
The final spectral consequence additionally uses the separately proved
high-interface tails, weighted scaffold, phase enclosure, and exact spectral
bridge; it is not a consequence of the low-tail estimate in isolation.

This review did not inspect the Round 6 incumbent named in the review task.

## 1. Proved Round 3 input

Fix a low-interface tail beginning at $x_0=r+1/2<\mu=\rho K$, and write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1).
$$

Let $p$ be the last index on the initial floor plateau, with the convention
$p=n$ if there is no drop, and put

$$
m=n-p.
$$

The proved concave-head/convex-tail decomposition gives

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta-\frac M4,
\tag{1}
$$

where

$$
0\le\delta<\frac{2\sqrt2}{15},
\tag{2}
$$

$$
M=L+d_\rho m-p,
\qquad
L=\lfloor K\eta\rfloor,
\qquad
d_\rho=\frac{2\arcsin\rho}{\pi}=1-2c_\rho,
\tag{3}
$$

$$
c_\rho=\frac{\arccos\rho}{\pi},
\qquad
\eta=G_1(\rho).
$$

For $n=0$, the head is absent and Round 3 prescribes $p=m=0$, so (1)--(3)
remain valid with $M=L$.

Thus it is enough to prove

$$
M>4\delta.
\tag{4}
$$

## 2. Elementary thin estimates

Since $\rho=1-\varepsilon\ge99/100>3/4$, one has

$$
\arccos(1-\varepsilon)
=2\arcsin\sqrt{\varepsilon/2}
\le\pi\sqrt{\varepsilon/2}.
$$

Here $\arcsin u\le(\pi/2)u$ on $[0,1]$.  Consequently,

$$
c_\rho\le\sqrt{\frac\varepsilon2}<\frac1{10},
\qquad
\boxed{d_\rho>\frac45.}
\tag{5}
$$

The action height $\eta$ has the exact integral representation

$$
\eta=G_1(\rho)
=\frac1\pi\int_\rho^1\arccos u\,du
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv.
$$

If $\theta=\arccos(1-v)$, then
$1-v=\cos\theta\ge1-\theta^2/2$, so
$\theta\ge\sqrt{2v}$.  Hence

$$
\eta\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{6}
$$

Using $K\ge64/\varepsilon^2$, $\sqrt2>7/5$, and $\pi<4$ gives the strict
uniform bound

$$
\boxed{
K\eta
\ge\frac{128\sqrt2}{3\pi\sqrt\varepsilon}
>\frac{14}{\sqrt\varepsilon}.
}
\tag{7}
$$

Indeed $128(7/5)>14\cdot12$.

## 3. Reduction to the only dangerous plateau geometry

The cases $n=0$ and $p=0$ already close from (3) and (7), because then
$M\ge L$.  The same is true whenever

$$
d_\rho m\ge p.
\tag{8}
$$

It remains to assume

$$
p>0,
\qquad
d_\rho m<p.
\tag{9}
$$

By (5),

$$
m<\frac p{d_\rho}<\frac54p,
\qquad
n=p+m<\frac94p.
\tag{10}
$$

The distance from the start of the head to the inner interface is

$$
U:=\mu-x_0=\beta+n,
$$

and therefore

$$
\boxed{U<1+\frac94p.}
\tag{11}
$$

This implication includes the no-drop case: if $p=n$, then $m=0$ and
(9)--(11) hold automatically.

## 4. The dangerous plateau begins uniformly near the interface

The global Round 3 shelf estimate is permitted here:

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{12}
$$

Divide (11) by $\mu=\rho K$ and use (12):

$$
\frac U\mu
<\frac1{\rho K}
+\frac94\sqrt{\frac{2\pi}{\varepsilon\rho K}}.
\tag{13}
$$

The assumed lower bound on $K$, together with
$\rho>3/4$, $\varepsilon\le1/100$, and $\pi<4$, gives

$$
\frac1{\rho K}
\le\frac{\varepsilon^2}{64\rho}<\frac1{1000},
$$

and

$$
\sqrt{\frac{2\pi}{\varepsilon\rho K}}
\le\sqrt{\frac{2\pi\varepsilon}{64\rho}}
<\frac1{24}.
$$

Thus

$$
\frac U\mu<\frac1{1000}+\frac3{32}<\frac1{10}.
$$

With

$$
t:=\frac{x_0}{\mu}=1-\frac U\mu,
$$

we have proved

$$
\boxed{t>\frac9{10}.}
\tag{14}
$$

This is the point at which the global $p$ estimate is useful: not as the
final shelf bound, but only to put every genuinely dangerous shelf inside a
fixed relative neighborhood of the interface.

## 5. Exact local slope and the improved shelf bound

At $x_0=\mu t$, the exact slope is

$$
\begin{aligned}
\sigma(x_0)
&=\frac1\pi\bigl(\arccos(\rho t)-\arccos t\bigr)\\
&=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}.
\end{aligned}
\tag{15}
$$

The integrand is increasing, so (14) implies

$$
\sigma(x_0)
\ge\frac{\varepsilon t}
{\pi\sqrt{1-\rho^2t^2}}
>\frac{9\varepsilon}
{10\pi\sqrt{1-\rho^2t^2}}.
\tag{16}
$$

Because $\rho t=\rho-U/K$,

$$
1-\rho^2t^2
=(1-\rho t)(1+\rho t)
\le2\left(\varepsilon+\frac UK\right).
$$

Hence

$$
\boxed{
\sigma(x_0)
>\frac{9\varepsilon}
{10\pi\sqrt{2(\varepsilon+U/K)}}.
}
\tag{17}
$$

The plateau condition, including at every ordinary-floor wall, is

$$
A(x_0)-A(x_0+p)<1.
\tag{18}
$$

Since $\sigma$ is increasing,

$$
A(x_0)-A(x_0+p)
=\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
$$

Combining this with (11), (17), and
$K\ge64/\varepsilon^2$ gives

$$
p^2
<\frac{200\pi^2}{81}
\left(
\frac1\varepsilon+\frac1{64}+\frac{9p}{256}
\right).
\tag{19}
$$

Indeed

$$
\frac UK
<\frac{\varepsilon^2}{64}
\left(1+\frac94p\right).
$$

Using only $\pi<4$, (19) implies

$$
p^2
<\frac{40}{\varepsilon}+\frac58+\frac{45}{32}p.
\tag{20}
$$

Now suppose, for contradiction, that $p\ge8/\sqrt\varepsilon$.  Then
$p\ge80$, and

$$
\frac{40}{\varepsilon}\le\frac58p^2,
\qquad
\frac58\le\frac1{10000}p^2,
\qquad
\frac{45}{32}p\le\frac1{50}p^2.
$$

The right side of (20) would then be at most

$$
\left(\frac58+\frac1{10000}+\frac1{50}\right)p^2<p^2,
$$

a contradiction.  Therefore

$$
\boxed{p<\frac8{\sqrt\varepsilon}.}
\tag{21}
$$

This proof applies unchanged when there is no floor drop and $p=n$.  It
does not invoke the sharper concave theorem in that branch; it uses only the
Round 3 Proposition 3.1 convention and the resulting same-floor relation
(18).

## 6. Compensation and closure

At every real $x$, including integer walls,

$$
\lfloor x\rfloor>x-1.
$$

Thus (7) gives

$$
L=\lfloor K\eta\rfloor
>\frac{14}{\sqrt\varepsilon}-1.
\tag{22}
$$

If $n=0$, $p=0$, or (8) holds, then $M\ge L$.  In the remaining case,
(3), $d_\rho m\ge0$, (21), and (22) give

$$
M\ge L-p
>\frac6{\sqrt\varepsilon}-1
\ge59.
\tag{23}
$$

The easier branches have an even larger margin.  On the other hand,
(2) and $\sqrt2<3/2$ give

$$
4\delta<\frac{8\sqrt2}{15}<1.
$$

Therefore $M>4\delta$ in every branch.  Substitution into (1) proves

$$
\boxed{
\mathcal T_r
<2\int_{x_0}^{K}A(z)\,dz
\qquad(x_0<\rho K).
}
\tag{24}
$$

In particular the desired non-strict low-interface tail inequality holds.

## 7. Endpoint and wall audit

1. **No drop, $p=n$.**  Then $m=0$, so this is in the dangerous branch
   unless $p=0.  Relation (18) still holds, and the proof of (21) applies.
   Proposition 3.1, not the first-drop theorem, is the Round 3 head input.

2. **Degenerate head, $n=0$.**  Round 3 uses only the convex tail.  With
   $p=m=0$, one has $M=L$, which closes directly by (22).

3. **Immediate drop, $p=0$.**  Here $M=L+d_\rho n\ge L$; no division by
   $p$ or local-slope argument is used.

4. **Interface wall, $q=\mu$.**  Then $\beta=0$ and $\delta=0$.
   Equations (11)--(21) remain valid.

5. **Head floor wall.**  Equality of the initial and terminal ordinary
   floors always implies (18) strictly.  If the larger sampled value is an
   integer, the possible plateau difference only becomes smaller.

6. **Gain wall, $K\eta\in\mathbb Z$.**  Then $L=K\eta$ exactly.  The
   universal inequality $L>K\eta-1$ used in (22) remains strict.

7. **Threshold equality.**  The case $K=64/\varepsilon^2$ is included.
   Strictness in (7), (18), and (22) leaves ample margin.

8. **Outer trapezoid wall.**  If $K-x_0$ is integral, the final $G_K$
   endpoint equals zero; otherwise the proved zero extension handles the
   overshoot.  This is already part of the Round 3 decomposition used in
   (1).

## 8. Spectral consequence and scope

The separately proved high-interface shifted-tail theorem covers every
$x_0\ge\rho K$.  Combining it with (24) and the proved multiplicity scaffold
gives

$$
\sum_{\nu_\ell<K}2\nu_\ell
\left\lfloor
G_K(\nu_\ell)-G_{\rho K}(\nu_\ell)+\frac14
\right\rfloor
\le
\frac{2}{9\pi}(1-\rho^3)K^3
\tag{25}
$$

for

$$
0<\varepsilon=1-\rho\le\frac1{100},
\qquad
K\ge\frac{64}{\varepsilon^2}.
$$

The strict phase proxy is no larger than the ordinary-floor proxy in (25),
including at phase and proxy walls.  With the already-proved exact spectral
bridge, (25) therefore implies the actual shell Pólya bound

$$
\boxed{
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
\qquad
\left(K\ge\frac{64}{\varepsilon^2}\right).
}
\tag{26}
$$

This review proves no claim below that threshold and supplies no numerical
certificate.  Its analytic conclusion is conditional only on the already
proved Round 3 shifted-tail inputs and the already-promoted spectral bridge.
