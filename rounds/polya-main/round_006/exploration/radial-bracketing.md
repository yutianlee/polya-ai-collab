# Round 6 exploration: radius-sensitive radial bracketing

## Verdict

There is no completed radius-sensitive proof in this note.  There are,
however, four rigorous conclusions.

1. The already accepted flat-product argument has a substantially larger
   provable window than the Round 5 constant records:

   $$
   0<\varepsilon\le \frac1{100},\qquad
   0\le K\le \frac{9}{4\varepsilon^2}
   \quad\Longrightarrow\quad
   N_D(A_{1-\varepsilon,1},K^2)
   \le \frac{2}{9\pi}\bigl(1-(1-\varepsilon)^3\bigr)K^3.
   \tag{1}
   $$

   This is a full proof candidate (subject to the ordinary independent
   review gate), not a diagnostic.  It overlaps the accepted window and
   extends its endpoint from $\pi/(4\varepsilon^2)$ to
   $9/(4\varepsilon^2)$.  It does not close the endpoint and does not undo
   the exact obstruction to the flat product majorant.

2. Coupled radial step potentials give a rigorous radius-sensitive
   majorant without introducing artificial boundary modes.  Their cubic
   coefficient is the right Riemann sum for $r^2$, and its excess over the
   shell mean is explicit.

3. Ordinary Neumann sublayer bracketing is not a viable global proof.  For
   every fixed finite partition, its majorant has a strictly larger cubic
   coefficient than the shell Weyl term.  This is a rigorous obstruction,
   not just an unfavorable estimate.

4. An energy-tuned paired-Robin decomposition can remove the artificial
   interface count exactly at a chosen spectral threshold.  Together with
   the coupled-step comparison, this reduces the missing radius-sensitive
   theorem to an explicit uniform $K^2$ deficit estimate, stated in
   Section 6.  That estimate is conditional here.

Throughout,

$$
\rho=1-\varepsilon,\qquad
q_\ell=\ell(\ell+1),\qquad
L_\ell=-\frac{d^2}{dr^2}+\frac{q_\ell}{r^2}
$$

on $H^2(\rho,1)\cap H_0^1(\rho,1)$, and all counts are strict counts below
$K^2$.

## 1. A full extension of the flat-product range

Round 5 proves that it is sufficient to show

$$
D(a)\ge
\varepsilon\left(\frac{2a^3}{3\pi}+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi},
\qquad a=\varepsilon K,
\tag{2}
$$

and it proves

$$
D(a)\ge\frac{(a-\pi)^2}{2}\qquad(a\ge\pi).
\tag{3}
$$

The ranges $0\le a\le\pi$ and $\pi<a\le4\pi$ are already handled in
Round 5.  Suppose therefore that

$$
4\pi\le a\le\frac{9}{4\varepsilon}.
$$

After division by $a^2$, (2) follows from

$$
f_\varepsilon(a):=
\frac12\left(1-\frac\pi a\right)^2
-\frac{2\varepsilon a}{3\pi}
-\frac\varepsilon4
-\frac{\varepsilon^2}{\pi a}
\ge0.
\tag{4}
$$

Its derivative has the sign of

$$
G_\varepsilon(a)
=\pi a-\pi^2-\frac{2\varepsilon a^3}{3\pi}
+\frac{\varepsilon^2a}{\pi},
\qquad
f_\varepsilon'(a)=\frac{G_\varepsilon(a)}{a^3}.
\tag{5}
$$

Now

$$
G_\varepsilon(4\pi)
=\pi^2\left(3-\frac{128\varepsilon}{3}\right)+4\varepsilon^2>0
\tag{6}
$$

for $0<\varepsilon\le1/100$, while

$$
G_\varepsilon''(a)=-\frac{4\varepsilon a}{\pi}<0.
\tag{7}
$$

Thus the superlevel set $\{a:G_\varepsilon(a)\ge0\}$ is an interval
containing $4\pi$.  Consequently $f_\varepsilon$ first increases and then
possibly decreases; it has no interior minimum on the interval in (4).

At the left endpoint,

$$
f_\varepsilon(4\pi)
=\frac9{32}-\frac{35\varepsilon}{12}
-\frac{\varepsilon^2}{4\pi^2}>0.
\tag{8}
$$

At the right endpoint,

$$
f_\varepsilon\left(\frac9{4\varepsilon}\right)
=\frac12\left(1-\frac{4\pi\varepsilon}{9}\right)^2
-\frac3{2\pi}-\frac\varepsilon4
-\frac{4\varepsilon^3}{9\pi}.
\tag{9}
$$

This is decreasing in $\varepsilon$ on $(0,1/100]$.  Dropping the positive
quadratic term in the first square and using the elementary bounds
$157/50<\pi<22/7$ gives

$$
\begin{aligned}
f_\varepsilon\left(\frac9{4\varepsilon}\right)
&\ge
\frac12-\frac{75}{157}-\frac{22}{1575}
-\frac1{400}-\frac4{27000000}\\
&=\frac{10802069}{1854562500}>0.
\end{aligned}
\tag{10}
$$

Equations (4)--(10) prove (2) throughout the remaining range, and hence
prove (1).  All endpoints are included.  This proof still uses the rejected
flat majorant only in a range where its upper bound closes; it makes no
claim for larger $K$.

## 2. Coupled step comparison: the correct operator direction

Let

$$
\rho=R_0<R_1<\cdots<R_M=1,
\qquad h_j=R_j-R_{j-1}.
$$

Define the right-endpoint step potential

$$
V_{\ell,M}(r)=\frac{q_\ell}{R_j^2}
\quad\text{for }R_{j-1}<r<R_j
\tag{11}
$$

and the **coupled** comparison operator

$$
\widehat L_{\ell,M}=-\frac{d^2}{dr^2}+V_{\ell,M}
$$

on the same domain $H^2$ piecewise intersected with $H_0^1(\rho,1)$,
with continuity of both the function and its weak derivative at every
interface.  No boundary condition is inserted at an internal interface.

Because $r\le R_j$ on the $j$th subinterval,

$$
\frac{q_\ell}{r^2}\ge\frac{q_\ell}{R_j^2}.
$$

The two forms have the same domain and therefore

$$
L_\ell\ge\widehat L_{\ell,M}
\quad\text{in form order},
\qquad
N_{L_\ell}(K^2)\le N_{\widehat L_{\ell,M}}(K^2).
\tag{12}
$$

After summing with multiplicity $2\ell+1$,

$$
N_D(A_{\rho,1},K^2)\le\widehat N_M(K),
\tag{13}
$$

where $\widehat N_M$ is the exact direct-sum count of the coupled step
operators.  This is the useful radius-sensitive bracketing direction.

The step equations can be propagated exactly.  If
$p_j^2=K^2-q_\ell/R_j^2\ge0$, the transfer matrix across the $j$th layer is

$$
T_j=
\begin{pmatrix}
\cos(p_jh_j)&\sin(p_jh_j)/p_j\\
-p_j\sin(p_jh_j)&\cos(p_jh_j)
\end{pmatrix}.
\tag{14}
$$

If $p_j^2=-\kappa_j^2<0$, replace cosine and sine by cosine-hyperbolic and
sine-hyperbolic and replace the lower-left entry by
$\kappa_j\sinh(\kappa_jh_j)$.  Thus this comparison is also suitable for an
exact Pruefer recursion; floating transfer products alone would not be a
certificate.

## 3. Exact recovery of the shell mean, and the unavoidable step excess

The shell mean cross-section is

$$
m_\rho:=\frac1\varepsilon\int_\rho^1r^2\,dr
=\frac{1+\rho+\rho^2}{3}
=1-\varepsilon+\frac{\varepsilon^2}{3}.
\tag{15}
$$

For a uniform partition, $h=\varepsilon/M$ and
$R_j=\rho+jh$.  Direct summation gives the exact right-sum identity

$$
\boxed{
h\sum_{j=1}^M R_j^2
=\int_\rho^1r^2\,dr
+\varepsilon h\left(1-\frac\varepsilon2+\frac h6\right).
}
\tag{16}
$$

For a nonuniform partition with $h_*:=\max_jh_j$,

$$
\begin{aligned}
\sum_jh_jR_j^2-\int_\rho^1r^2\,dr
&=\sum_j\left(R_jh_j^2-\frac{h_j^3}{3}\right)\\
&\le\varepsilon h_*.
\end{aligned}
\tag{17}
$$

The sign in (16) is forced: any pointwise constant lower approximation
$q_\ell/S_j^2\le q_\ell/r^2$ on a whole layer must have
$S_j\ge R_j$, so its cubic angular cross-section is at least the same right
sum.  A fixed piecewise-constant lower potential can never have the exact
shell cubic coefficient.

The same mean appears without approximation in the preferred scaled
action.  With $a=\varepsilon K$, $y=\varepsilon\nu$, and

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds,
$$

Fubini and the substitution $y=ar z$ give

$$
\boxed{
\int_0^\infty2y\mathcal A_{\varepsilon,a}(y)\,dy
=\frac{2a^3}{3\pi}m_\rho.
}
\tag{18}
$$

Thus (16) measures exactly how much radius information a step comparison
loses relative to the action.

## 4. Rigorous obstruction to ordinary Neumann sublayers

Suppose the step form is decoupled by placing Neumann conditions at every
internal $R_j$.  Its form domain is the direct sum of the subinterval
$H^1$ spaces, with Dirichlet conditions only at the two physical shell
boundaries.  This domain contains the continuous $H_0^1(\rho,1)$ domain.
The form agrees on that subspace.  Therefore the min--max direction is

$$
\widehat L^{\,N}_{\ell,M}\le\widehat L_{\ell,M}\le L_\ell
\quad\text{in the eigenvalue sense},
\qquad
N_{L_\ell}(K^2)\le N_{\widehat L^{\,N}_{\ell,M}}(K^2).
\tag{19}
$$

This is a valid upper-count comparison, but it is too large.  Fix any
finite partition.  On a layer of length $h_j$ and outer radius $R_j$, the
radial frequencies form an arithmetic progression of spacing
$\pi/h_j$: mixed Dirichlet--Neumann on the two physical-edge layers and
Neumann--Neumann on every interior layer.  If $C_{j}(K)$ denotes its full
angular-multiplicity count, the exact formula

$$
\#\{\ell\ge0:q_\ell<R_j^2t^2\}
=\left\lceil\sqrt{R_j^2t^2+\frac14}-\frac12\right\rceil
$$

and a Riemann-sum limit imply

$$
\lim_{K\to\infty}\frac{C_j(K)}{K^3}
=\frac{2h_jR_j^2}{3\pi}.
\tag{20}
$$

Indeed, the square of the displayed angular count is
$R_j^2t^2+O(R_jt+1)$, and summing it over an arithmetic radial mesh gives

$$
\frac{h_j}{\pi}\int_0^K R_j^2(K^2-t^2)\,dt
=\frac{2h_jR_j^2}{3\pi}K^3,
$$

with an $O(K^2)$ remainder for fixed $h_j,R_j$.  Summing (20) over a fixed
finite partition and using (17) yields

$$
\lim_{K\to\infty}
\frac{N_{\widehat L^{\,N}_M}(K^2)
-\frac{2}{9\pi}(1-\rho^3)K^3}{K^3}
=\frac{2}{3\pi}
\left(\sum_jh_jR_j^2-\int_\rho^1r^2\,dr\right)>0.
\tag{21}
$$

Consequently the Neumann-sublayer majorant exceeds the desired Weyl term
for all sufficiently large $K$.  Refining a fixed number of Neumann layers
cannot close the thin endpoint.  A $K$-dependent refinement also creates
two artificial Neumann faces per cut and requires a separate quantitative
analysis; (21) alone does not prove impossibility for every such adaptive
scheme.

## 5. Paired Robin interfaces and exact threshold gluing

There is a way to decouple without an unavoidable one-mode interface loss.
Split an interval at $c$.  For a real number $\alpha$, put the boundary
terms

$$
-\alpha|u_-(c)|^2
\quad\text{on the left form},
\qquad
+\alpha|u_+(c)|^2
\quad\text{on the right form}.
\tag{22}
$$

Both separated problems then have the same logarithmic-derivative
condition

$$
u_-'(c)=\alpha u_-(c),
\qquad
u_+'(c)=\alpha u_+(c).
\tag{23}
$$

On the continuous subspace $u_-(c)=u_+(c)$, the two trace terms in (22)
cancel exactly.  Enlarging the domain therefore gives, for every finite
$\alpha$,

$$
N_H(E)\le N_{H_-^\alpha}(E)+N_{H_+^\alpha}(E).
\tag{24}
$$

The signs in (22) are essential.  Giving the same form sign on both sides
does not restrict to the original form.

More is true at one fixed threshold $E$.  Assume first that $E$ is not a
Dirichlet eigenvalue of either subinterval.  Let $\phi_L$ solve

$$
(H-E)\phi_L=0,\qquad \phi_L(a)=0,\qquad\phi_L(c)=1,
$$

and choose

$$
\alpha=\phi_L'(c).
\tag{25}
$$

Then $E$ is an eigenvalue of the left Robin problem and is excluded by the
strict count.  The Dirichlet-to-Neumann inertia decomposition gives

$$
\boxed{
N_H(E)=N_{H_-^\alpha}(E)+N_{H_+^\alpha}(E).
}
\tag{26}
$$

For completeness, if $A_L=\phi_L'(c)$ and
$A_R=-\phi_R'(c)$ for the solution with
$\phi_R(c)=1,\phi_R(b)=0$, the coupled boundary direction has quadratic
coefficient $A_L+A_R$.  Under (25), the left separated coefficient is
$A_L-\alpha=0$, while the right coefficient is
$A_R+\alpha=A_L+A_R$.  The strict negative inertias, including the case
$A_L+A_R=0$ where $E$ is a global eigenvalue, therefore agree exactly.
This equality is restricted to thresholds that are not Dirichlet
eigenvalues of either subinterval. At an internal Dirichlet wall, retain only
the bracketing inequality (24), or move the interface and rederive the
identity at the shifted split; a one-sided limit at the original split need
not preserve the strict count. For example, for
$H=-d^2/dx^2$ on $(0,2)$ with a split at $c=1$ and $E=\pi^2$, the full
strict count is $1$, whereas every finite paired Robin parameter gives a sum
of separated strict counts equal to $2$.

Away from internal Dirichlet walls, this lemma explains what ordinary
Neumann cuts lose.  It does not by itself
give a usable estimate: the tuning parameter (25) is the exact logarithmic
derivative of the incumbent solution.  Bounding its Robin phase uniformly
after replacing $q_\ell/r^2$ by step constants is essentially the remaining
analytic work, not a free consequence of (26).

## 6. An explicit conditional closure criterion

The coupled-step route can be reduced to one concrete estimate with ample
constant room.  For each $(\varepsilon,K)$ set

$$
M=\lceil8\varepsilon K\rceil,
\qquad h=\frac\varepsilon M.
\tag{27}
$$

Then $h\le1/(8K)$ and, by (16) and $h\le\varepsilon$,

$$
0<h\sum_{j=1}^MR_j^2-\int_\rho^1r^2\,dr
\le\frac{\varepsilon}{8K}.
\tag{28}
$$

Consequently the following **unproved uniform surface-deficit lemma** would
close the radius-sensitive intermediate range:

$$
\boxed{
\widehat N_M(K)
\le\frac{2}{3\pi}
\left(h\sum_{j=1}^MR_j^2\right)K^3
-\frac{K^2}{1000}
}
\tag{29}
$$

for

$$
0<\varepsilon\le\frac1{100},
\qquad K\ge\frac9{4\varepsilon^2},
\qquad M=\lceil8\varepsilon K\rceil.
$$

Indeed, the cubic excess in (28) is at most

$$
\frac{2}{3\pi}\frac{\varepsilon}{8K}K^3
=\frac{\varepsilon}{12\pi}K^2
\le\frac{1}{1200\pi}K^2
<\frac{K^2}{1000}.
\tag{30}
$$

Combining (12), (29), and (30) gives the desired shell bound for every
$K\ge9/(4\varepsilon^2)$, while (1) gives the lower range with exact
overlap at the endpoint.  Thus (29), if proved uniformly, would cover the
entire thin endpoint and automatically overlap the existing fixed-$\rho$
high-energy theorem.

The expected two-boundary Weyl correction is much larger than
$K^2/1000$, but an asymptotic expansion is not a proof of (29).  What is
needed is a one-sided, wall-safe estimate uniform in the growing number
$M\asymp\varepsilon K$ of **potential jumps**.  The jumps are not boundary
faces because the step operator remains coupled.  A viable proof could use
the exact transfer recursion (14), or the paired-Robin identity (26) with
correlated phase shifts.  Replacing the coupled operator by Neumann pieces
cannot prove (29), by Section 4.

## 7. An exact averaged-centrifugal inequality and its limitation

There is also a rigorous localization estimate, but it only controls low
angular channels.  Put $x=1-r\in(0,\varepsilon)$ and
$V(x)=(1-x)^{-2}$.  Its interval average is

$$
\overline V=\frac1\varepsilon\int_0^\varepsilon V(x)\,dx
=\frac1\rho.
$$

The zero-endpoint primitive of $V-\overline V$ is

$$
F(x)=\frac{x}{1-x}-\frac{x}{\rho}
=-\frac{x(\varepsilon-x)}{\rho(1-x)},
$$

and an elementary derivative calculation gives

$$
\|F\|_\infty
=:\Gamma_\rho
=\frac{(1-\sqrt\rho)^2}{\rho}.
\tag{31}
$$

For $u\in H_0^1(0,\varepsilon)$, integration by parts has no boundary term
and yields

$$
\left|\int_0^\varepsilon(V-\overline V)|u|^2\,dx\right|
\le2\Gamma_\rho\|u'\|_2\|u\|_2.
\tag{32}
$$

Therefore, for every $q\ge0$ and every $\delta>0$,

$$
\boxed{
\int\left(|u'|^2+qV|u|^2\right)
\ge(1-\delta)\|u'\|_2^2
+\left(\frac q\rho-\frac{q^2\Gamma_\rho^2}{\delta}\right)\|u\|_2^2.
}
\tag{33}
$$

Since $m_\rho=(1+\rho+\rho^2)/3$,

$$
\frac1\rho-\frac1{m_\rho}
=\frac{(1-\rho)^2}{\rho(1+\rho+\rho^2)}.
$$

Thus (33) implies the mean-radius comparison

$$
L_\ell\ge(1-\delta)\left(-\frac{d^2}{dr^2}\right)
+\frac{q_\ell}{m_\rho}
\tag{34}
$$

whenever

$$
q_\ell\le
\delta\,
\frac{\rho(1+\sqrt\rho)^2}
{(1-\sqrt\rho)^2(1+\rho+\rho^2)}.
\tag{35}
$$

The comparison (34) genuinely recovers the desired cross-section
$m_\rho$, but its scope is too small for the intermediate problem.  As
$\varepsilon\downarrow0$, the right side of (35) is

$$
\frac{16\delta}{3\varepsilon^2}(1+O(\varepsilon)),
$$

so it controls only $\ell=O(\varepsilon^{-1})$.  At
$K\asymp\varepsilon^{-2}$, the active angular range extends to
$\ell=O(\varepsilon^{-2})$, and the kinetic loss $1-\delta$ also has a
positive cubic cost.  Hence a channelwise use of (34) cannot supply the
full mean-cross-section correction.  It may still be useful as the
low-angular component of an aggregate proof paired with a turning-point or
Robin-phase estimate for high angular momentum.

## Final classification

- **Full proof candidate:** the enlarged flat-product window (1), with all
  constants and endpoints proved above.
- **Rigorous radius-sensitive ingredients:** the coupled-step comparison
  (12), exact right-sum error (16)--(17), exact action mean (18), paired
  Robin gluing (22)--(26), and averaged form inequality (31)--(35).
- **Rigorous obstruction:** every fixed finite Neumann-sublayer majorant has
  the wrong cubic coefficient, as shown in (21); every pointwise constant
  lower step has a positive right-sum excess.
- **Conditional route:** prove the explicit wall-safe coupled-step deficit
  (29).  It would join (1) at $K=9/(4\varepsilon^2)$ and cover the entire
  remaining thin range.  No such deficit is proved in this exploration.
