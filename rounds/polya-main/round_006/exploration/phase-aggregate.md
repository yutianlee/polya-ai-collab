# Round 6 exploration: exact thin-scaled action and a radius-sensitive aggregate range

## Verdict

Put

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le \frac1{100},
\qquad a=\varepsilon K,
\qquad y=\varepsilon\nu .
$$

This report proves the exact analytic identities, curvature statements, and
strict lattice conventions for

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds.
$$

It also proves the following new **radius-sensitive aggregate range**:

$$
\boxed{
\frac{\pi}{4\varepsilon}
\le a\le
\frac1{8\varepsilon^{3/2}}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
<\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3 .
}
\tag{1}
$$

The interval is nonempty: for $\varepsilon\le1/100$,
$2\pi\sqrt\varepsilon\le\pi/5<1$.  It overlaps the Round 5 range at
$a=\pi/(4\varepsilon)$.  Consequently, combining (1) with Round 5 gives the
candidate enlarged thin-shell theorem

$$
\boxed{
0<\varepsilon\le\frac1{100},
\qquad
0\le K\le\frac1{8\varepsilon^{5/2}}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3 .
}
\tag{2}
$$

Everything through (1) is proved below, subject only to the already-audited
strict phase enclosure and exact spectral count.  This is an exploration
report, not an authoritative-state promotion.  It does **not** close the full
thin endpoint: the new upper scale $a\asymp\varepsilon^{-3/2}$ remains far
below the existing high-energy scale $a\asymp\varepsilon^{-3}$.

## 1. Exact rescaling and the permitted phase majorant

For $c>0$, define

$$
Q_c(y)=
\begin{cases}
\sqrt{c^2-y^2}-y\arccos(y/c),&0\le y\le c,\\
0,&y>c.
\end{cases}
$$

Changing variables $r=1-\varepsilon s$ gives the exact identities

$$
\boxed{
\mathcal A_{\varepsilon,a}(y)
=\frac1{\pi\varepsilon}
\int_\rho^1\sqrt{a^2-\frac{y^2}{r^2}}_+\,dr
=\frac{Q_a(y)-Q_{\rho a}(y)}{\pi\varepsilon}.
}
\tag{3}
$$

This is exactly

$$
G_K(\nu)-G_{\rho K}(\nu)
\qquad
(K=a/\varepsilon,\ \nu=y/\varepsilon).
$$

Write

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}
$$

and set, on the strict half-integer mesh

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad
q_\ell=
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<.
\tag{4}
$$

No domination of the true phase by the bare action is assumed.  In fact,
below the inner interface the audited enclosure has the opposite lower
inequality $\mathcal A<\gamma$.  What is already proved and is sufficient is

$$
\gamma_{K,\rho K}(\nu)
<\mathcal A_{\varepsilon,a}(\varepsilon\nu)+\frac14.
\tag{5}
$$

For $\nu\le\rho K$, (5) is the audited two-sided action enclosure.  For
$\nu\ge\rho K$, $G_{\rho K}(\nu)=0$, so the audited global bound becomes
$\gamma<G_K+1/4=\mathcal A+1/4$.  Equality at $\nu=\rho K$ is included.
Therefore exact strict counting gives

$$
N_D(A_{\rho,1},K^2)
\le\sum_{y_\ell<a}\frac{2y_\ell}{\varepsilon}q_\ell.
\tag{6}
$$

Define the scaled proxy and its continuous target by

$$
P_{\mathcal A}
:=\varepsilon\sum_{y_\ell<a}y_\ell q_\ell,
\qquad
I_{\varepsilon,a}
:=\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy.
\tag{7}
$$

Multiplying (6) and the shell Weyl term by $\varepsilon^2/2$ shows that the
required aggregate inequality is exactly

$$
\boxed{P_{\mathcal A}\le I_{\varepsilon,a}.}
\tag{8}
$$

## 2. Proved action calculus

### 2.1. Scaling, support, and exact volume

Equation (3) immediately gives

$$
\mathcal A_{\varepsilon,a}(y)
=a\mathcal A_{\varepsilon,1}(y/a),
\qquad
\mathcal A_{\varepsilon,a}(0)=\frac a\pi,
\qquad
\mathcal A_{\varepsilon,a}(a)=0,
\tag{9}
$$

and the support is $[0,a]$.  Fubini, followed by $y=rz$, gives

$$
\begin{aligned}
\int_0^a2y\mathcal A_{\varepsilon,a}(y)\,dy
&=\frac1{\pi\varepsilon}
\int_\rho^1\int_0^{ar}
2y\sqrt{a^2-y^2/r^2}\,dy\,dr\\
&=\frac{2a^3}{3\pi\varepsilon}
\int_\rho^1r^2\,dr\\
&=\frac{2a^3}{9\pi}(3-3\varepsilon+\varepsilon^2).
\end{aligned}
\tag{10}
$$

Thus, with

$$
m_\varepsilon
:=\frac1\varepsilon\int_\rho^1r^2\,dr
=1-\varepsilon+\frac{\varepsilon^2}{3},
\tag{11}
$$

one has the exact radius-sensitive target

$$
\boxed{
I_{\varepsilon,a}=\frac{m_\varepsilon a^3}{3\pi}.
}
\tag{12}
$$

This recovers the required mean cross-section, rather than the rejected
outer-radius coefficient $1$.

### 2.2. Monotonicity and the turning interface

For $0<y<\rho a$,

$$
\mathcal A'(y)
=\frac1{\pi\varepsilon}
\left(
\arccos\frac{y}{\rho a}
-\arccos\frac ya
\right)<0,
\tag{13}
$$

$$
\mathcal A''(y)
=\frac1{\pi\varepsilon}
\left(
\frac1{\sqrt{a^2-y^2}}
-\frac1{\sqrt{\rho^2a^2-y^2}}
\right)<0.
\tag{14}
$$

For $\rho a<y<a$,

$$
\mathcal A'(y)
=-\frac1{\pi\varepsilon}\arccos\frac ya<0,
\qquad
\mathcal A''(y)
=\frac1{\pi\varepsilon\sqrt{a^2-y^2}}>0.
\tag{15}
$$

The one-sided first derivatives at $y=\rho a$ both equal

$$
-\frac{\arccos\rho}{\pi\varepsilon}.
$$

Hence $\mathcal A$ is $C^1$, strictly decreasing, concave before the inner
turning interface, and convex after it.  The left second derivative tends to
$-\infty$ at the interface, so there is no global $C^2$ or one-curvature
argument.  The interface height is exactly

$$
\boxed{
\tau_{\varepsilon,a}
:=\mathcal A(\rho a)
=\frac a{\pi\varepsilon}
\left(\sqrt{1-\rho^2}-\rho\arccos\rho\right).
}
\tag{16}
$$

The integral representation also gives the endpoint-safe estimate

$$
0<\tau_{\varepsilon,a}
\le\frac{a\sqrt{2\varepsilon}}\pi.
\tag{17}
$$

Indeed, at $y=\rho a$ the integrand in (3) is bounded by
$a\sqrt{1-\rho^2}\le a\sqrt{2\varepsilon}$, and the $r$-interval has
length $\varepsilon$.  This also proves (17) directly at the interface,
without using a turning-point asymptotic.

### 2.3. Inverse-square curvature and exact layer cake

Let $T=a/\pi$, let $R(t)$ be the inverse of $\mathcal A$ on $0<t<T$, and
put $F(t)=R(t)^2$.  Then

$$
R_{\varepsilon,a}(t)
=aR_{\varepsilon,1}(t/a),
\qquad
F_{\varepsilon,a}(t)
=a^2F_{\varepsilon,1}(t/a).
\tag{18}
$$

At $y=R(t)$,

$$
F''(t)
=\frac{2(\mathcal A'(y)-y\mathcal A''(y))}
{\mathcal A'(y)^3}.
\tag{19}
$$

For $y>\rho a$, the numerator in (19) is

$$
-\frac1{\pi\varepsilon}
\left(
\arccos(y/a)+\frac{y}{\sqrt{a^2-y^2}}
\right)<0.
$$

For $y<\rho a$, it is

$$
\frac1{\pi\varepsilon}
\left[h\!\left(\frac{y}{\rho a}\right)
-h\!\left(\frac ya\right)\right]>0,
\qquad
h(x)=\arccos x+\frac{x}{\sqrt{1-x^2}},
$$

because $h'(x)=x^2(1-x^2)^{-3/2}>0$.  Since $\mathcal A'<0$,

$$
\boxed{
F''(t)>0\quad(0<t<\tau_{\varepsilon,a}),
\qquad
F''(t)<0\quad(\tau_{\varepsilon,a}<t<T).
}
\tag{20}
$$

Thus the square inverse is convex at low radial levels and concave at high
radial levels.  This is the exact mixed-curvature obstruction at the inner
turning interface.

For the mesh count

$$
M_\varepsilon(x)
:=\#\left\{\ell\ge0:
\varepsilon\left(\ell+\frac12\right)<x\right\}
=\max\left\{0,
\left\lceil\frac x\varepsilon-\frac12\right\rceil
\right\},
\tag{21}
$$

strict layer cake gives the exact aggregate identities

$$
\boxed{
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\ge1\\n-1/4<T}}
M_\varepsilon(R(n-1/4))^2,
\qquad
I_{\varepsilon,a}
=\frac12\int_0^T R(t)^2\,dt.
}
\tag{22}
$$

At a level wall $\mathcal A(y_\ell)+1/4=n$, the condition in (22) is
strict and that layer is excluded.

## 3. Mean-square-radius comparison

Define the effective semicircle action

$$
\mathcal B_{\varepsilon,a}(y)
:=\frac1\pi
\sqrt{a^2-\frac{y^2}{m_\varepsilon}}_+.
\tag{23}
$$

For fixed $0\le y\le\rho a$, the function

$$
\phi_y(z)=\sqrt{a^2-y^2/z}
$$

is concave on $[\rho^2,1]$, because

$$
\phi_y''(z)
=-\frac{y^2}{z^3\phi_y(z)}
-\frac{y^4}{4z^4\phi_y(z)^3}<0
$$

in the interior; the equality case $y=\rho a$ follows by continuity at the
left endpoint.  More explicitly, one may apply Jensen for
$y=(\rho-\delta)a$ and pass monotonically to the limit
$\delta\downarrow0$; this avoids differentiating at the square-root
endpoint.  Jensen's inequality with normalized measure $dr/\varepsilon$
therefore proves

$$
\boxed{
\mathcal A_{\varepsilon,a}(y)
\le\mathcal B_{\varepsilon,a}(y)
\qquad(0\le y\le\rho a).
}
\tag{24}
$$

Moreover,

$$
\int_0^\infty y\mathcal B_{\varepsilon,a}(y)\,dy
=\frac{m_\varepsilon a^3}{3\pi}
=I_{\varepsilon,a}.
\tag{25}
$$

Thus (23) preserves the exact cubic coefficient.  It is not a global
pointwise majorant: $\mathcal B$ vanishes at $a\sqrt{m_\varepsilon}<a$,
whereas $\mathcal A$ remains positive up to $a$.  The region
$y>\rho a$ must be paid for explicitly.

## 4. Proved lattice margin for the effective semicircle

Set

$$
q_\ell^{\mathcal B}
=\left[\mathcal B_{\varepsilon,a}(y_\ell)+\frac14\right]_<,
\qquad
P_{\mathcal B}
=\varepsilon\sum_{\ell\ge0}y_\ell q_\ell^{\mathcal B}.
\tag{26}
$$

The following estimate is the quantitative source of the extension.

### Lemma 1 (proved)

If

$$
0<\varepsilon\le\frac1{100},
\qquad
a\ge\frac\pi{4\varepsilon},
$$

then

$$
\boxed{
I_{\varepsilon,a}-P_{\mathcal B}>\frac{a^2}{12}.
}
\tag{27}
$$

### Proof

Write $t=a/\pi$ and use the strict radial levels

$$
x_n=n-\frac14,
\qquad
N=\#\{n\ge1:x_n<t\}
=\left\lceil t+\frac14\right\rceil-1.
$$

Put

$$
b_n=\sqrt{a^2-\pi^2x_n^2},
\qquad
R_n=\sqrt{m_\varepsilon}\,b_n.
$$

Layer cake gives

$$
P_{\mathcal B}
=\frac{\varepsilon^2}{2}\sum_{n=1}^NM_n^2,
\qquad
M_n=M_\varepsilon(R_n).
\tag{28}
$$

From (21), including every angular wall,

$$
M_n<\frac{R_n}{\varepsilon}+\frac12.
$$

Consequently,

$$
\varepsilon^2\sum_{n=1}^NM_n^2
<m_\varepsilon\sum_{n=1}^Nb_n^2
+\varepsilon\sqrt{m_\varepsilon}\sum_{n=1}^Nb_n
+\frac{\varepsilon^2N}{4}.
\tag{29}
$$

Define the shifted radial deficit

$$
D=\frac{2a^3}{3\pi}-\sum_{n=1}^Nb_n^2.
$$

The strict convention is encoded by

$$
u=t-N\in\left(-\frac14,\frac34\right].
$$

Direct summation of $\sum_{n=1}^N(n-1/4)^2$ gives

$$
\boxed{
\frac D{\pi^2}
=\frac{N^2}{4}
+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}.
}
\tag{30}
$$

Since $u\ge-1/4$,

$$
\frac D{\pi^2}
\ge\frac{N^2}{4}-\frac N{48}-\frac1{96}
\ge\frac{N^2}{5}.
\tag{31}
$$

The last inequality follows from
$24N^2-10N-5>0$ for every integer $N\ge1$.

There is also the endpoint-safe quarter-disk bound

$$
\boxed{
\sum_{n=1}^Nb_n\le\frac{a^2}{4}+\frac a4.
}
\tag{32}
$$

Indeed, for
$b(x)=\pi\sqrt{t^2-x^2}_+$, each value $b(n-1/4)$ is at most the
integral over $[n-5/4,n-1/4]$.  For $n=1$ this uses the even extension on
$[-1/4,3/4]$; for $n\ge2$ it uses monotonicity on $[0,t]$.  The intervals
are consecutive, so

$$
\sum b_n
\le\int_{-1/4}^{t}b(x)\,dx
\le\frac{\pi^2t^2}{4}+\frac{\pi t}{4}.
$$

Now $t\ge25$, $m_\varepsilon\ge99/100$, and
$N\ge t-3/4\ge(24/25)t$.  Equations (31)--(32) imply

$$
m_\varepsilon D>\frac9{50}a^2,
\tag{33}
$$

because

$$
\frac{99}{100}\cdot\frac15
\left(\frac{24}{25}\right)^2
=\frac{57024}{312500}>\frac9{50}.
$$

$$
\varepsilon\sqrt{m_\varepsilon}\sum b_n
<\frac1{300}a^2,
\qquad
\frac{\varepsilon^2N}{4}<\frac1{10000}a^2.
\tag{34}
$$

For the first estimate in (34), use $a>75$, so
$a^2/4+a/4<(19/75)a^2$, and $19/7500<1/300$.
For the second, use $N<t+1/4<2t$, $\varepsilon^2\le10^{-4}$,
$a^2=\pi^2t^2>9t^2$, and $t\ge25$.

Finally, (25), (29), and the definition of $D$ give

$$
I_{\varepsilon,a}-P_{\mathcal B}
>\frac12\left(
m_\varepsilon D
-\varepsilon\sqrt{m_\varepsilon}\sum b_n
-\frac{\varepsilon^2N}{4}
\right)
>\frac{a^2}{12},
$$

because $9/50-1/300-1/10000>1/6$.  This proves the lemma. $\square$

## 5. Paying for the whispering-gallery strip

### Lemma 2 (proved)

If

$$
0<\varepsilon\le\frac1{100},
\qquad
\frac\pi{4\varepsilon}\le a\le
\frac1{8\varepsilon^{3/2}},
$$

then

$$
\boxed{P_{\mathcal A}<I_{\varepsilon,a}.}
\tag{35}
$$

### Proof

For $y_\ell\le\rho a$, (24) and monotonicity of the strict integer count
give $q_\ell\le q_\ell^{\mathcal B}$.  For arbitrary $x,z\ge0$,

$$
[x+1/4]_<-[z+1/4]_<\le (x-z)_++1.
\tag{36}
$$

Therefore

$$
P_{\mathcal A}
\le P_{\mathcal B}
+\varepsilon
\sum_{\rho a<y_\ell<a}y_\ell
\bigl(\mathcal A(y_\ell)+1\bigr).
\tag{37}
$$

The number of mesh points in $(\rho a,a)$ is at most $a+1$.  Also
$y_\ell<a$, $\mathcal A$ is decreasing, and (17) gives

$$
\mathcal A(y_\ell)
\le\mathcal A(\rho a)
\le\frac{a\sqrt{2\varepsilon}}\pi.
$$

Thus the correction in (37) is strictly smaller than

$$
E_{\rm out}
:=\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}\pi+1\right).
\tag{38}
$$

Since $a>75$, $\sqrt2/\pi<1/2$, and
$a\varepsilon^{3/2}\le1/8$,

$$
\frac{E_{\rm out}}{a^2}
<\frac{76}{75}
\left(
\frac12a\varepsilon^{3/2}+\varepsilon
\right)
\le\frac{76}{75}
\left(\frac1{16}+\frac1{100}\right)
<\frac1{12}.
\tag{39}
$$

The last comparison is exact:
$\frac{76}{75}(\frac1{16}+\frac1{100})
=2204/30000<2500/30000=1/12$.

Lemma 1 supplies a strictly larger $a^2/12$ margin for
$P_{\mathcal B}$.  Combining (27), (37), and (39) proves (35).
$\square$

Multiplying (35) by $2/\varepsilon^2$ and using (6), (10), and (12) proves
(1).

## 6. Wall and interface audit

All delicate interfaces are covered as follows.

1. **True phase wall.**  The channel count is $[\gamma]_<$.  Since the
   phase inequality (5) is strict, it is bounded by
   $[\mathcal A+1/4]_<$, including when the latter argument is an integer.

2. **Action level wall.**  In (22), the layer condition is
   $n-1/4<\mathcal A(y_\ell)$, not $\le$.  Equality is excluded.

3. **Effective radial wall.**  If $t=n-1/4$, that radial layer is excluded.
   The convention $u=t-N=3/4$ in (30) is exactly the strict wall
   convention.

4. **Angular wall.**  If
   $R_n/\varepsilon=\ell+1/2$, that channel is excluded.
   Formula (21), rather than an ordinary floor, handles this equality.

5. **Inner turning interface.**  Jensen's bound (24) includes
   $y=\rho a$.  The audited phase enclosure also includes equality there.
   The correction sum in (37) begins strictly above the interface, so no
   sampled channel is lost or counted twice.

6. **Outer cutoff.**  The active spectral cutoff is $y_\ell<a$.  At
   $y=a$, the action is zero and no channel is included.

7. **Overlap endpoints.**  Lemma 2 includes both
   $a=\pi/(4\varepsilon)$ and
   $a=1/(8\varepsilon^{3/2})$.  The first is already covered by Round 5,
   so the two arguments genuinely overlap.

## 7. What remains open

The proof above makes quantitative progress but does not bridge to the
existing fixed-$\rho$ theorem.

- The new endpoint is

  $$
  a=\frac1{8\varepsilon^{3/2}},
  $$

  while the current high-energy theorem begins at order
  $a\asymp\varepsilon^{-3}$.

- The effective action $\mathcal B$ has the exact mean-square radius and an
  explicit lattice margin of order $a^2$.  The crude outer-strip payment in
  (38) is of order $a^3\varepsilon^{3/2}$.  Their balance forces the present
  scale $a\varepsilon^{3/2}=O(1)$.

- One cannot simply assert $\mathcal A\le\mathcal B$ globally:
  $\mathcal B$ vanishes before $\mathcal A$.  The positive outer excess is
  compensated by an interior deficit at the continuous level because their
  weighted integrals are exactly equal.  A full proof must preserve that
  signed cancellation through the strict half-integer staircase.

- The exact inverse-square curve has the mixed curvature (20).  Therefore a
  theorem assuming global convexity or global concavity cannot be applied
  across $t=\tau_{\varepsilon,a}$.

### Unproved next lemma

A natural next target is a signed rearrangement inequality of the form

$$
\sum_{n-1/4<T}
M_\varepsilon(R_{\mathcal A}(n-1/4))^2
\le
\sum_{n-1/4<T}
M_\varepsilon(R_{\mathcal B}(n-1/4))^2.
\tag{40}
$$

Equation (40) is **conjectural** here.  If proved, Lemma 1 would remove the
outer-strip restriction and give a uniform action-proxy theorem for every
$a\ge\pi/(4\varepsilon)$, directly overlapping the existing low-optical
range.  Any attempted proof of (40) must control the radial walls
$n-1/4$, angular walls $R/\varepsilon\in\mathbb Z+1/2$, and the curvature
switch at $t=\tau_{\varepsilon,a}$; equality of the continuous integrals
alone is not sufficient.

## Classification

- **Proved:** (3), (9)--(25), Lemma 1, Lemma 2, and the shell range (1)
  using the already-proved phase enclosure and spectral bridge.
- **Proved by combination with Round 5:** the enlarged low-energy statement
  (2), pending the normal independent review and state-promotion process.
- **Conjectural:** the signed discrete rearrangement (40).
- **Obstruction:** the present absolute-value treatment of the outer strip
  cannot pass the scale $a\asymp\varepsilon^{-3/2}$ and therefore cannot by
  itself close `SHELL-thin-curvature-intermediate`.
