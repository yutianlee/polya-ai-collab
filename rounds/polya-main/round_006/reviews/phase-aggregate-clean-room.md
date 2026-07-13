# Clean-room review of Component B: aggregate-action range

## Verdict

**PASS.**  Using only the stated phase/count dependencies and elementary
calculus, the aggregate-action argument proves the stronger strict estimate

$$
N_D(A_{1-\varepsilon,1},K^2)
<\frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

whenever

$$
0<\varepsilon\le \frac1{100},\qquad
\frac{\pi}{4\varepsilon}\le a\le
\frac1{8\varepsilon^{3/2}},\qquad K=\frac a\varepsilon.
$$

The first unsupported implication is: **none**.  The normalization, Jensen
step, strict layer cake, shifted-deficit identity, two auxiliary sum bounds,
outer-strip charge, constants, and all listed walls close without an
additional lemma.

## 1. Normalization and the strict spectral bridge

Put

$$
\rho=1-\varepsilon,\qquad K=\frac a\varepsilon,\qquad
\nu=\frac y\varepsilon,\qquad
m=m_\varepsilon=1-\varepsilon+\frac{\varepsilon^2}{3}.
$$

With $G_\lambda$ extended by zero above its support, differentiation in the
radius parameter gives

$$
G_K(\nu)-G_{\rho K}(\nu)
=\frac1\pi\int_\rho^1
\sqrt{K^2-\frac{\nu^2}{r^2}}_+\,dr.
$$

After $r=1-\varepsilon s$ and the displayed scaling of $K,\nu$, this is
exactly

$$
\mathcal A(y):=\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds.
\tag{1}
$$

For the half-integer mesh

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
$$

let

$$
q^A_\ell=
\left[\mathcal A(y_\ell)+\frac14\right]_<,
\qquad
[x]_<:=\#\{n\in\mathbb N:n<x\}.
$$

The strict phase identity and phase enclosure imply

$$
N_D(A_{\rho,1},K^2)
\le \sum_{y_\ell<a}\frac{2y_\ell}{\varepsilon}q^A_\ell.
\tag{2}
$$

Indeed, for $y_\ell\le \rho a$ the inner-region phase estimate is
$\gamma<\mathcal A+1/4$; for $\rho a<y_\ell<a$ one has
$G_{\rho K}(\nu_\ell)=0$, so the global estimate
$\gamma<G_K+1/4$ is the same inequality.  Strictness is preserved at an
integer wall because $\gamma<U$ implies
$[\gamma]_<\le[U]_<$.  No channel with $y_\ell\ge a$ contributes.

Define

$$
P_A=\varepsilon\sum_{y_\ell<a}y_\ell q^A_\ell,
\qquad
I=\int_0^a y\mathcal A(y)\,dy.
$$

Then (2) is

$$
N_D(A_{\rho,1},K^2)\le \frac{2P_A}{\varepsilon^2}.
\tag{3}
$$

Fubini is exact here.  If $r=1-\varepsilon s$, then

$$
\int_0^\infty y\sqrt{a^2-\frac{y^2}{r^2}}_+\,dy
=r^2\int_0^a z\sqrt{a^2-z^2}\,dz
=\frac{r^2a^3}{3}.
$$

Consequently

$$
I=\frac{a^3}{3\pi}\int_0^1(1-\varepsilon s)^2\,ds
=\frac{ma^3}{3\pi}.
\tag{4}
$$

Also

$$
1-\rho^3=3\varepsilon m,
$$

and hence

$$
\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{5}
$$

Thus it remains only to prove $P_A\le I$.

## 2. Jensen comparison on its exact domain

Define

$$
\mathcal B(y)=\frac1\pi
\sqrt{a^2-\frac{y^2}{m}}_+.
$$

For fixed $0<y\le \rho a$, set

$$
f_y(z)=\sqrt{a^2-\frac{y^2}{z}},
\qquad z\ge\rho^2.
$$

The radicand is nonnegative on this whole interval.  In its interior,

$$
f_y''(z)
=-\frac{y^2}{z^3\sqrt{a^2-y^2/z}}
-\frac{y^4}{4z^4(a^2-y^2/z)^{3/2}}<0.
$$

At $y=\rho a$ this concave function extends continuously to the left
endpoint; at $y=0$ it is constant.  Since

$$
\int_0^1(1-\varepsilon s)^2\,ds=m,
$$

Jensen's inequality therefore yields, including the endpoint $y=\rho a$,

$$
\mathcal A(y)
\le\frac1\pi f_y(m)=\mathcal B(y),
\qquad 0\le y\le\rho a.
\tag{6}
$$

No comparison is used for $y>\rho a$.

## 3. Strict layer cake for the effective action

Let

$$
P_B=\varepsilon\sum_{\ell\ge0}y_\ell
\left[\mathcal B(y_\ell)+\frac14\right]_<.
$$

Introduce

$$
t=\frac a\pi,\qquad x_n=n-\frac14,\qquad
b_n=\sqrt{a^2-\pi^2x_n^2},
$$

and

$$
N=\#\{n\ge1:x_n<t\}.
$$

For every mesh point, the strict positive-integer layer cake is

$$
\left[\mathcal B(y_\ell)+\frac14\right]_<
=\sum_{n\ge1}\mathbf 1_{\{x_n<\mathcal B(y_\ell)\}}.
$$

For $1\le n\le N$,

$$
x_n<\mathcal B(y_\ell)
\quad\Longleftrightarrow\quad
y_\ell<\sqrt m\,b_n.
$$

Thus, with

$$
M_n=\#\left\{\ell\ge0:
\varepsilon\left(\ell+\frac12\right)<\sqrt m\,b_n\right\},
$$

one has the endpoint-safe formula

$$
M_n=\max\left\{0,
\left\lceil\frac{\sqrt m\,b_n}{\varepsilon}-\frac12\right\rceil
\right\}.
\tag{7}
$$

This remains exact when $\sqrt m\,b_n/\varepsilon$ is a half-integer.
Moreover, $\lceil z\rceil<z+1$ gives the strict ceiling estimate

$$
M_n<\frac{\sqrt m\,b_n}{\varepsilon}+\frac12.
\tag{8}
$$

Since

$$
\sum_{\ell=0}^{M-1}\left(\ell+\frac12\right)=\frac{M^2}{2},
$$

finite interchange of the two sums gives the exact identity

$$
P_B=\frac{\varepsilon^2}{2}\sum_{n=1}^N M_n^2.
\tag{9}
$$

Using (8),

$$
P_B<\frac m2\sum_{n=1}^N b_n^2
+\frac{\varepsilon\sqrt m}{2}\sum_{n=1}^N b_n
+\frac{\varepsilon^2N}{8}.
\tag{10}
$$

The strict sign in (10) is valid at every angular ceiling wall.

## 4. The shifted deficit and its two auxiliary bounds

Write

$$
u=t-N.
$$

Equivalently,

$$
N=\lceil t+\tfrac14\rceil-1,
$$

so

$$
-\frac14<u\le\frac34.
\tag{11}
$$

In particular, if $x_n=t$ for some $n$, that zero radial layer is excluded,
$N=n-1$, and $u=3/4$.

Set

$$
D=\frac{2a^3}{3\pi}-\sum_{n=1}^N b_n^2.
$$

The finite-square sum is

$$
\sum_{n=1}^N\left(n-\frac14\right)^2
=\frac{N^3}{3}+\frac{N^2}{4}-\frac{N}{48}.
$$

Substitution of $t=N+u$ therefore gives the exact shifted deficit

$$
\frac D{\pi^2}
=\frac{N^2}{4}+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}.
\tag{12}
$$

Here $a\ge\pi/(4\varepsilon)$ and $\varepsilon\le1/100$ imply $t\ge25$,
so $N\ge1$.  From (11),

$$
\begin{aligned}
\frac D{\pi^2}-\frac{N^2}{5}
&=\frac{N^2}{20}+Nu^2-\frac N{48}+\frac{2u^3}{3}\\
&>\frac{N^2}{20}-\frac N{48}-\frac1{96}\\
&=\frac{24N^2-10N-5}{480}>0.
\end{aligned}
$$

Thus, in particular,

$$
D\ge\frac{\pi^2N^2}{5}.
\tag{13}
$$

For the linear sum, let

$$
f(x)=\sqrt{a^2-\pi^2x^2}\quad(0\le x\le t)
$$

and extend $f$ by the constant $a$ on $[-1/4,0]$.  This extension is
nonincreasing.  Since $x_n=n-1/4$ and the intervals
$[x_n-1,x_n]$ are consecutive,

$$
\begin{aligned}
\sum_{n=1}^N b_n
&\le\sum_{n=1}^N\int_{x_n-1}^{x_n}f(x)\,dx\\
&\le\frac a4+\int_0^t\sqrt{a^2-\pi^2x^2}\,dx\\
&=\frac a4+\frac{a^2}{4}.
\end{aligned}
\tag{14}
$$

This proves both auxiliary estimates without a quadrature assertion.

## 5. Aggregate margin with explicit constants

Combining (4) and (10),

$$
I-P_B>
\frac m2D
-\frac{\varepsilon\sqrt m}{2}\sum_{n=1}^N b_n
-\frac{\varepsilon^2N}{8}.
\tag{15}
$$

The following coarse rational estimates leave ample room.  First,

$$
m\ge\frac{99}{100},\qquad \sqrt m<1.
$$

Also $u\le3/4$ and $t\ge1/(4\varepsilon)$ imply

$$
N=t-u\ge t-\frac34\ge(1-3\varepsilon)t
\ge\frac{97}{100}t.
$$

Consequently, by (13),

$$
\frac m2D
>\frac{931491}{10000000}a^2.
\tag{16}
$$

Since $a\ge25\pi>1$, (14) gives

$$
\frac{\varepsilon\sqrt m}{2}\sum_{n=1}^N b_n
\le\frac{a^2}{400}.
\tag{17}
$$

Furthermore $N<t+1/4=a/\pi+1/4<a$, and hence

$$
\frac{\varepsilon^2N}{8}<\frac{a^2}{80000}.
\tag{18}
$$

Substitution into (15) yields

$$
I-P_B>
\left(
\frac{931491}{10000000}-\frac1{400}-\frac1{80000}
\right)a^2
=\frac{906366}{10000000}a^2
>\frac{a^2}{12}.
\tag{19}
$$

The final comparison is exact: $12\cdot906366=10876392>10000000$.
This proves the required aggregate deficit uniformly over the full stated
$\varepsilon$ and lower-$a$ range.

## 6. Paying the outer strip

By (6), the $A$-proxy is bounded by the $B$-proxy on all mesh points with
$y_\ell\le\rho a$.  The remaining mesh points lie in

$$
\rho a<y_\ell<a,
$$

an interval of length $\varepsilon a$ with mesh spacing $\varepsilon$;
there are at most $a+1$ such points.

The action $\mathcal A$ is nonincreasing in $y$.  At the left endpoint of
the strip,

$$
\begin{aligned}
\mathcal A(\rho a)
&=\frac a\pi\int_0^1
\sqrt{1-\frac{\rho^2}{(1-\varepsilon s)^2}}\,ds\\
&\le\frac a\pi\sqrt{1-\rho^2}
\le\frac{a\sqrt{2\varepsilon}}\pi.
\end{aligned}
\tag{20}
$$

For an outer point,

$$
q^A_\ell
=\left[\mathcal A(y_\ell)+\frac14\right]_<
<\mathcal A(y_\ell)+1
\le\mathcal A(\rho a)+1.
$$

It follows that its entire contribution is strictly smaller than

$$
E_{\rm out}
=\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}\pi+1\right).
\tag{21}
$$

The upper and lower bounds on $a$ give

$$
\begin{aligned}
\frac{E_{\rm out}}{a^2}
&=\left(1+\frac1a\right)
\left(\frac{\varepsilon a\sqrt{2\varepsilon}}\pi+\varepsilon\right)\\
&\le
\left(1+\frac{4\varepsilon}{\pi}\right)
\left(\frac{\sqrt2}{8\pi}+\varepsilon\right).
\end{aligned}
\tag{22}
$$

Using only $\pi>3$, $\sqrt2<3/2$, and
$\varepsilon\le1/100$,

$$
\frac{E_{\rm out}}{a^2}
<\frac{76}{75}\cdot\frac{29}{400}
=\frac{551}{7500}<\frac1{12}.
\tag{23}
$$

Thus the outer strip is fully paid, including at both $a$-range endpoints.

## 7. Completion

Splitting $P_A$ at $y=\rho a$, using Jensen on the inner part and (21) on
the outer part, gives

$$
P_A<P_B+E_{\rm out}.
$$

Equations (19) and (23) now imply

$$
I-P_A>I-P_B-E_{\rm out}
>\frac{a^2}{12}-E_{\rm out}>0.
$$

Therefore $P_A<I$.  Combining this with (3)--(5) proves

$$
N_D(A_{1-\varepsilon,1},K^2)
<\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3
$$

throughout

$$
\frac{\pi}{4\varepsilon^2}\le K\le
\frac1{8\varepsilon^{5/2}}.
$$

## 8. Wall audit

- If $\mathcal A(y_\ell)+1/4$ is an integer, the proxy uses
  $[x]_< = \lceil x\rceil-1$, so no endpoint eigenvalue is inserted.
- If $x_n=a/\pi$, that layer is excluded by $x_n<t$; equivalently
  $u=3/4$, which is included in (11)--(13).
- If $\sqrt m\,b_n/\varepsilon$ is a half-integer, (7) gives the exact
  strict angular count and (8) remains strict.
- A mesh point at $y_\ell=\rho a$ is in the Jensen region, where the
  continuous endpoint extension proves (6).
- A mesh point at $y_\ell=a$ has zero phase contribution and is outside the
  active strict sum.
- No global majorization $\mathcal A\le\mathcal B$ was assumed.  Every point
  with $y_\ell>\rho a$ was charged to $E_{\rm out}$.
- The bounds in (19) and (23) are strict with considerable rational margin,
  so $\varepsilon=1/100$ and both inclusive $a$ endpoints cause no loss.
- All sums are finite, so the layer-cake interchange requires no limiting
  argument.
