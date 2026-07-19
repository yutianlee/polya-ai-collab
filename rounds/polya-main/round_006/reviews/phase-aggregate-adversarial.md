# Adversarial review: thin-scaled phase aggregate

## Verdict

**PASS.**

I independently recomputed the scaled normalization, action identities,
Jensen comparison, layer-cake multiplicity, shifted radial deficit,
angular ceiling, quarter-disk estimate, numerical constants, outer-strip
payment, and all stated strict walls.  I found no unsupported implication
in the proof of

$$
\frac{\pi}{4\varepsilon}
\le a\le\frac{1}{8\varepsilon^{3/2}}
\quad\Longrightarrow\quad
P_{\mathcal A}<I_{\varepsilon,a},
$$

or in its conversion to the shell counting estimate.

The first statement not supported by the proof is (40), the signed
discrete rearrangement inequality.  The report explicitly labels (40)
conjectural and does not use it in Lemma 1, Lemma 2, or the claimed shell
range.  It therefore does not affect this PASS.

This review assumes only the dependencies the report itself declares:
the already-audited strict phase enclosure

$$
\gamma_{K,\rho K}(\nu)
<G_K(\nu)-G_{\rho K}(\nu)+\frac14
$$

for $0\le\nu<K$, and the proved strict spectral count.

## 1. Rescaling and the allegedly missing epsilon

Put

$$
\rho=1-\varepsilon,\qquad
K=\frac a\varepsilon,\qquad
\nu=\frac y\varepsilon.
$$

Starting from the displayed scaled action and setting
$r=1-\varepsilon s$ gives

$$
\begin{aligned}
\mathcal A_{\varepsilon,a}(y)
&=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds\\
&=\frac1{\pi\varepsilon}
\int_\rho^1\sqrt{a^2-\frac{y^2}{r^2}}_+\,dr.
\end{aligned}
$$

If

$$
Q_c(y)=\sqrt{c^2-y^2}-y\arccos(y/c)
$$

on $0\le y\le c$, then

$$
\frac{d}{dr}Q_{ar}(y)
=\sqrt{a^2-\frac{y^2}{r^2}}.
$$

This verifies

$$
\mathcal A_{\varepsilon,a}(y)
=\frac{Q_a(y)-Q_{\rho a}(y)}{\pi\varepsilon}.
$$

On the other hand,

$$
G_K(\nu)
=\frac{Q_{a/\varepsilon}(y/\varepsilon)}{\pi}
=\frac{Q_a(y)}{\pi\varepsilon},
$$

so

$$
\mathcal A_{\varepsilon,a}(y)
=G_K(\nu)-G_{\rho K}(\nu).
$$

There is no missing factor of $\varepsilon$ in (3).

For the count, $2\ell+1=2\nu=2y/\varepsilon$.  Therefore

$$
N_D(A_{\rho,1},K^2)
\le\sum_{y_\ell<a}\frac{2y_\ell}{\varepsilon}q_\ell
$$

implies, after multiplication by $\varepsilon^2/2$,

$$
\frac{\varepsilon^2}{2}N_D
\le\varepsilon\sum_{y_\ell<a}y_\ell q_\ell
=P_{\mathcal A}.
$$

The Weyl term has exactly the same normalization:

$$
\begin{aligned}
\frac{\varepsilon^2}{2}
\frac{2}{9\pi}(1-\rho^3)K^3
&=\frac{a^3}{9\pi\varepsilon}(1-\rho^3)\\
&=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right)\\
&=I_{\varepsilon,a}.
\end{aligned}
$$

Thus (8) is exactly the required scaled inequality, with neither an extra
nor a missing epsilon.

## 2. Continuous action, support, and turning interface

For fixed $r$, the active $y$-range is $0\le y<ar$.  Hence Fubini gives

$$
\begin{aligned}
\int_0^a2y\mathcal A_{\varepsilon,a}(y)\,dy
&=\frac1{\pi\varepsilon}
\int_\rho^1\int_0^{ar}
2y\sqrt{a^2-y^2/r^2}\,dy\,dr\\
&=\frac{2a^3}{3\pi\varepsilon}\int_\rho^1r^2\,dr\\
&=\frac{2m_\varepsilon a^3}{3\pi},
\end{aligned}
$$

where

$$
m_\varepsilon
=\frac1\varepsilon\int_\rho^1r^2\,dr
=1-\varepsilon+\frac{\varepsilon^2}{3}.
$$

Therefore

$$
I_{\varepsilon,a}
=\int_0^ay\mathcal A_{\varepsilon,a}(y)\,dy
=\frac{m_\varepsilon a^3}{3\pi}.
$$

The support is exactly $[0,a]$: for $y<a$ a nonempty outer radial
sublayer has $ar>y$, while for $y\ge a$ every integrand vanishes.

Differentiating $Q_c'(y)=-\arccos(y/c)$ verifies (13)--(15).
The first derivatives agree at $y=\rho a$, so $\mathcal A$ is $C^1$
there.  At the interface,

$$
\tau_{\varepsilon,a}
=\frac{a}{\pi\varepsilon}
\left(\sqrt{1-\rho^2}-\rho\arccos\rho\right).
$$

The integral representation gives

$$
\tau_{\varepsilon,a}
\le\frac{a}{\pi}\sqrt{1-\rho^2}
\le\frac{a\sqrt{2\varepsilon}}{\pi}.
$$

No turning-point asymptotic or omitted epsilon is hidden in this estimate.

For the inverse $R(t)$ and $F(t)=R(t)^2$,

$$
F''(t)
=\frac{2(\mathcal A'(y)-y\mathcal A''(y))}
{\mathcal A'(y)^3},
\qquad y=R(t).
$$

On the outer side $y>\rho a$, the numerator and denominator are both
negative, so $F''>0$.  This corresponds to
$0<t<\tau_{\varepsilon,a}$.  On the inner side $y<\rho a$, the numerator
is positive and the denominator negative, so $F''<0$, corresponding to
$\tau_{\varepsilon,a}<t<a/\pi$.  The curvature switch in (20) has the
correct orientation.

## 3. Jensen comparison and its exact support

For fixed $0\le y\le\rho a$, define

$$
\phi_y(z)=\sqrt{a^2-\frac{y^2}{z}}.
$$

Because $y^2/a^2\le\rho^2$, this is real and continuous on all of
$[\rho^2,1]$.  In the interior,

$$
\phi_y''(z)
=-\frac{y^2}{z^3\phi_y(z)}
-\frac{y^4}{4z^4\phi_y(z)^3}<0.
$$

Jensen with normalized measure $dr/\varepsilon$ therefore gives

$$
\begin{aligned}
\mathcal A_{\varepsilon,a}(y)
&=\frac1\pi\frac1\varepsilon
\int_\rho^1\phi_y(r^2)\,dr\\
&\le\frac1\pi\phi_y\left(
\frac1\varepsilon\int_\rho^1r^2\,dr\right)\\
&=\frac1\pi
\sqrt{a^2-\frac{y^2}{m_\varepsilon}}
=\mathcal B_{\varepsilon,a}(y).
\end{aligned}
$$

At $y=\rho a$, the integrand merely reaches zero at the one endpoint
$r=\rho$; continuity, or approximation from below, proves the same
inequality.  Also $m_\varepsilon>\rho^2$, so $\mathcal B$ is active
throughout this inner comparison region.

The report does not apply Jensen for $y>\rho a$.  This matters because
$\mathcal B$ vanishes at $a\sqrt{m_\varepsilon}<a$, while
$\mathcal A$ remains positive up to $a$.  The support mismatch is handled
only by the explicit outer-strip payment in Lemma 2.  I found no invalid
global comparison of $\mathcal A$ and $\mathcal B$.

Finally,

$$
\int_0^\infty y\mathcal B_{\varepsilon,a}(y)\,dy
=\frac{m_\varepsilon a^3}{3\pi}
=I_{\varepsilon,a},
$$

so the effective semicircle has the required continuous mass.

## 4. Strict layer cake and angular multiplicity

For $x>0$, the number of strict half-integer mesh points below $x$ is

$$
M_\varepsilon(x)
=\#\{\ell\ge0:\varepsilon(\ell+1/2)<x\}
=\max\left\{0,
\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil\right\}.
$$

If the count equals $M$, then

$$
\sum_{\ell=0}^{M-1}y_\ell
=\varepsilon\sum_{\ell=0}^{M-1}\left(\ell+\frac12\right)
=\frac{\varepsilon M^2}{2}.
$$

The extra factor $\varepsilon$ in the definition of $P_{\mathcal A}$
therefore gives

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\ge1\\n-1/4<a/\pi}}
M_\varepsilon(R(n-1/4))^2.
$$

This verifies both the $\varepsilon^2/2$ normalization and the square
multiplicity in (22).  The continuous identity

$$
I_{\varepsilon,a}
=\frac12\int_0^{a/\pi}R(t)^2\,dt
$$

follows from the same layer cake.

At a level wall
$\mathcal A(y_\ell)+1/4=n$, the condition for the $n$th layer is

$$
n-\frac14<\mathcal A(y_\ell),
$$

which fails at equality.  Thus the layer is correctly excluded.

At an angular wall $x/\varepsilon=\ell_0+1/2$, the formula gives
$M_\varepsilon(x)=\ell_0$, so the equality channel $\ell_0$ is also
excluded.  There is no off-by-one error in (21), (22), or (28).

## 5. Shifted deficit formula

For the effective semicircle, let

$$
t=\frac a\pi,\qquad x_n=n-\frac14,\qquad
N=\#\{n\ge1:x_n<t\}.
$$

Strict counting gives

$$
N=\left\lceil t+\frac14\right\rceil-1,\qquad
u=t-N\in\left(-\frac14,\frac34\right].
$$

At the radial wall $t=n-1/4$, one has $N=n-1$ and $u=3/4$, which is the
correct strict convention.

The exact finite sum is

$$
\sum_{n=1}^N\left(n-\frac14\right)^2
=\frac{N^3}{3}+\frac{N^2}{4}-\frac{N}{48}.
$$

Consequently, with

$$
b_n^2=\pi^2\left(t^2-(n-1/4)^2\right),
$$

direct expansion gives

$$
\begin{aligned}
\frac D{\pi^2}
&=\frac{2t^3}{3}
-Nt^2
+\sum_{n=1}^N(n-1/4)^2\\
&=\frac{N^2}{4}
+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}.
\end{aligned}
$$

This confirms (30).  Since $u>-1/4$,

$$
\frac D{\pi^2}
\ge\frac{N^2}{4}-\frac N{48}-\frac1{96}.
$$

Subtracting $N^2/5$ leaves

$$
\frac{24N^2-10N-5}{480}>0
\qquad(N\ge1),
$$

so (31) is valid.

## 6. Angular ceiling and quarter-disk sum

Writing $x=R_n/\varepsilon$, (21) gives

$$
M_n=\max\{0,\lceil x-1/2\rceil\}<x+\frac12
$$

for every $x>0$, including when $x-1/2$ is an integer.  Squaring and
multiplying by $\varepsilon^2$ yields

$$
\varepsilon^2M_n^2
<R_n^2+\varepsilon R_n+\frac{\varepsilon^2}{4}.
$$

Summing this identity with
$R_n=\sqrt{m_\varepsilon}\,b_n$ gives (29), with all three terms and their
coefficients correct.

For (32), extend

$$
b(x)=\pi\sqrt{t^2-x^2}_+
$$

evenly.  For $n=1$, every
$x\in[-1/4,3/4]$ satisfies $|x|\le3/4$, so
$b(x)\ge b(3/4)$.  For $n\ge2$, $b$ is decreasing on the positive axis,
and hence

$$
b(n-1/4)
\le\int_{n-5/4}^{n-1/4}b(x)\,dx.
$$

The intervals are consecutive, and the final endpoint
$N-1/4$ is strictly below $t$.  Therefore

$$
\begin{aligned}
\sum_{n=1}^Nb_n
&\le\int_{-1/4}^tb(x)\,dx\\
&\le\int_0^tb(x)\,dx+\frac14 b(0)\\
&=\frac{a^2}{4}+\frac a4.
\end{aligned}
$$

The first shifted interval and the radial endpoint are both handled
correctly.

## 7. Lemma 1 constants

The hypotheses imply

$$
t\ge25,\qquad a=\pi t>75,\qquad
m_\varepsilon>\frac{99}{100}.
$$

Since $u\le3/4$,

$$
N\ge t-\frac34\ge\frac{24}{25}t.
$$

Thus

$$
m_\varepsilon D
>\frac{99}{100}\frac{\pi^2}{5}
\left(\frac{24t}{25}\right)^2
=\frac{57024}{312500}a^2
>\frac9{50}a^2.
$$

The two ceiling-error terms obey

$$
\begin{aligned}
\varepsilon\sqrt{m_\varepsilon}\sum b_n
&<\frac1{100}\left(\frac{a^2}{4}+\frac a4\right)
<\frac1{300}a^2,\\
\frac{\varepsilon^2N}{4}
&<\frac1{10000}a^2.
\end{aligned}
$$

For the first line, $a>75$ gives
$a^2/4+a/4<(19/75)a^2$, and
$19/7500<1/300$.  For the second,
$N<t+1/4<2t$, while
$a^2=\pi^2t^2>9t^2$ and $t\ge25$.

Combining these estimates in the exact identity following (29) gives

$$
\begin{aligned}
I_{\varepsilon,a}-P_{\mathcal B}
&>\frac12
\left(\frac9{50}-\frac1{300}-\frac1{10000}\right)a^2\\
&>\frac{a^2}{12},
\end{aligned}
$$

because
$9/50-1/300-1/10000>1/6$.  Lemma 1's constant and strict inequality
are valid.

## 8. Outer whispering-gallery payment

On $y_\ell\le\rho a$, Jensen gives
$q_\ell\le q_\ell^{\mathcal B}$.  For nonnegative $x,z$,

$$
[x+1/4]_<-[z+1/4]_<
\le(x-z)_++1.
$$

This follows by counting the integers in the interval between the two
arguments and remains true at either integer wall.

For $\rho a<y_\ell<a$, one may use
$(\mathcal A-\mathcal B)_+\le\mathcal A$.  Hence

$$
P_{\mathcal A}
\le P_{\mathcal B}
+\varepsilon\sum_{\rho a<y_\ell<a}
y_\ell(\mathcal A(y_\ell)+1).
$$

The strip has width

$$
a-\rho a=\varepsilon a
$$

and the mesh spacing is $\varepsilon$, so it contains fewer than $a+1$
mesh points, not $(a+1)/\varepsilon$ points.  This is the place where a
hidden epsilon factor would have destroyed the proof; the report's count
is correct.

Since $y_\ell<a$ and $\mathcal A$ is decreasing,

$$
E_{\rm out}
<\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}{\pi}+1\right).
$$

Now $a>75$, $\sqrt2/\pi<1/2$,
$a\varepsilon^{3/2}\le1/8$, and
$\varepsilon\le1/100$.  Therefore

$$
\begin{aligned}
\frac{E_{\rm out}}{a^2}
&<\frac{76}{75}
\left(\frac12a\varepsilon^{3/2}+\varepsilon\right)\\
&\le\frac{76}{75}\left(\frac1{16}+\frac1{100}\right)\\
&=\frac{2204}{30000}
<\frac1{12}.
\end{aligned}
$$

The bound remains strict at
$a=1/(8\varepsilon^{3/2})$ because the mesh-point, $y_\ell<a$,
and $\sqrt2/\pi<1/2$ estimates are strict.

Lemma 1 supplies a margin strictly larger than $a^2/12$, so Lemma 2
follows.

## 9. Strict-wall audit

1. **Phase wall.**  If $\gamma$ is an integer, the true strict channel
   count excludes that level.  Since
   $\gamma<\mathcal A+1/4$, its positive-integer set is contained in the
   proxy's positive-integer set.

2. **Proxy integer wall.**  If
   $\mathcal A(y_\ell)+1/4=m$, then
   $[\mathcal A(y_\ell)+1/4]_< =m-1$.  The strict phase inequality cannot
   create an omitted $m$th true level.

3. **Layer wall.**  The $n$th layer uses
   $n-1/4<\mathcal A(y_\ell)$, and equality is excluded.

4. **Effective radial wall.**  If $t=n-1/4$, the $n$th radial layer is
   excluded, $N=n-1$, and $u=3/4$.  Formula (30) uses this convention.

5. **Angular wall.**  If
   $R_n/\varepsilon=\ell+1/2$, then
   $M_\varepsilon(R_n)=\ell$, excluding the equality channel.

6. **Turning interface.**  Jensen includes $y=\rho a$, and the audited
   phase enclosure includes $\nu=\rho K$.  The correction strip begins
   strictly above this point, so an interface mesh point is neither lost
   nor double counted.

7. **Outer wall.**  The active sum uses $y_\ell<a$.  A mesh point at
   $y_\ell=a$ is excluded; in any case
   $\mathcal A(a)+1/4=1/4$ has zero strict positive-integer count.

8. **Range endpoints.**  At
   $a=\pi/(4\varepsilon)$, one has $t\ge25$ and every Lemma 1 estimate
   remains valid.  At
   $a=1/(8\varepsilon^{3/2})$, the outer-payment estimate remains strict.
   Both endpoints are therefore included, and the lower endpoint overlaps
   Round 5 exactly.

## 10. Final dependency and scope check

The proof never assumes the false global comparison
$\mathcal A\le\mathcal B$.  It applies Jensen only on
$[0,\rho a]$ and pays the entire complementary strip.  It never replaces
the strict staircase by an ordinary floor at an integer wall.  The
layer-cake weight is exactly $M^2$, arising from
$\sum_{\ell<M}(2\ell+1)=M^2$ after the scaled normalization.

Accordingly, the proved chain through Lemma 2 and the range (1) passes.
The report also correctly states that this range stops at
$a\asymp\varepsilon^{-3/2}$ and does not overlap the existing
$a\asymp\varepsilon^{-3}$ high-energy threshold.
