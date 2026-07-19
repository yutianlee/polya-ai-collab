# Round 16 thin-endpoint incumbent

## Verdict

**PASS (isolated incumbent proof).** The first unsupported implication is:
**none** in the chain proving the stated endpoint. This is an incumbent
reconstruction, not a state-promotion decision; the independent adversarial
and cross-review gates in the packet still have to be executed before any
state change.

The frozen packet was hashed before proof work. Its SHA-256 was

```text
5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09
```

exactly as prescribed. The exact domain proved below is

$$
0<\varepsilon\le \frac18,\qquad a=\varepsilon K\ge0,
$$

equivalently

$$
\frac78\le\rho<1,\qquad K\ge0,
$$

and, in fact, the comparison with the Weyl expression is strict when
$K>0$ and is equality when $K=0$.

## 1. Exact dependency ledger

### Whitelist

| permitted input | exact use here | domain-sensitive material imported? |
|---|---|---|
| `CONV-strict-counting` and the exact separated shell spectrum | Strict inequalities at every spectral, radial, angular, and phase wall; multiplicity $2\ell+1$. | No. |
| `SHELL-sturm-liouville-completeness` | The unitary decomposition into $L_\ell=-d^2/dr^2+\ell(\ell+1)/r^2$ and the exact strict spectral sum. | No. |
| The proved radial min--max comparison | Its direction is rechecked directly below from the common form domain and $r^{-2}\ge1$. | No old product conclusion is used. |
| `SHELL-phase-enclosures` with `SHELL-annulus-phase-transfer` | Only the already-proved all-domain proxy transfer (N3), with the strict bracket in (N1). | No old endpoint or bridge estimate is used. |
| The domain-free action identities (N1)--(N2) | Both identities, including normalization, are rederived below from (H1). | No old $P_{\mathcal A}<I$ conclusion is used. |

The only imported inequality in the high proof is therefore (N3):

$$
N_D(A_{\rho,1},K^2)\le \frac{2P_{\mathcal A}}{\varepsilon^2},
\qquad
\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

Everything between $P_{\mathcal A}$ and $I$ is proved here.

### Blacklist

The following inputs occur nowhere in the proof:

* the Round 6 aggregate theorem or either endpoint of its old intermediate
  window;
* the Round 5 product theorem, its conclusion, and its three-slab estimate;
* the Round 11 bridge, all-frequency endpoint, or old
  $P_{\mathcal A}<I$ conclusion;
* the rejected pointwise semicircle majorant
  $\mathcal A\le\mathcal B$;
* any hidden assumption $\varepsilon\le1/100$, $\rho\ge99/100$,
  $a\ge125$, or any old bridge scale;
* any Round 15 coverage in either of the two endpoint pieces; Round 15 is
  mentioned only in the separate conditional-envelope audit in Section 8;
* any sampled or bounded numerical certification.

The navigation screens (S1)--(S4) are reproduced only in the exact ledger.
Neither (S1) nor (S2) is promoted as a stretch endpoint, and neither (S3)
nor (S4) is called a spectral counterexample or impossibility result.

### The six replacements

1. The Stieltjes argument splits at the actual $\tau$, with no assertion
   $\tau>1$ and no first-cell exception.
2. No $a\ge125$ or low-radial shortcut is used; the only radial-layer bound
   is the exact $J_{\rm rad}<a/\pi+1/4$.
3. The high lower screen uses exactly $\rho=1-\varepsilon$.
4. The power reserve is exactly $143/4096$.
5. The old three-slab argument is replaced by the exact zero-count interval
   and $D>(2/5)a^2$.
6. The complete union consists only of the two inclusive pieces
   $a\le\pi/(4\varepsilon)$ and $a\ge\pi/(4\varepsilon)$.

## 2. Normalization and the zero-frequency face

Put

$$
m_\varepsilon=1-\varepsilon+\frac{\varepsilon^2}{3}.
$$

Throughout, $\rho=1-\varepsilon$. Since
$1-\rho^3=3\varepsilon m_\varepsilon$ and
$K=a/\varepsilon$, the target right side is

$$
\frac{2}{9\pi}(1-\rho^3)K^3
=\frac1{\varepsilon^2}\frac{2a^3}{3\pi}m_\varepsilon.
\tag{2.1}
$$

At $a=K=0$, positivity of the Dirichlet operator gives a zero strict
count, and (2.1) is zero. Hence equality owns this face. In the rest of the
proof $a>0$ whenever division by $a$ occurs.

## 3. Low product piece: complete proof of (P1)--(P9)

Assume

$$
0<a\le\frac{\pi}{4\varepsilon}.
\tag{3.1}
$$

### 3.1 Min--max direction, multiplicity, and (P1)

For every $\ell\ge0$, on the same domain $H_0^1(\rho,1)$,

$$
\int_\rho^1\left(|u'|^2+
\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr
\ge
\int_\rho^1\left(|u'|^2+\ell(\ell+1)|u|^2\right)dr,
$$

because $r\le1$. Thus

$$
L_\ell\ge -\frac{d^2}{dr^2}+\ell(\ell+1)
$$

in form order. Min--max therefore gives the required upper-count direction

$$
N_{L_\ell}(K^2)
\le \#\left\{n\ge1:
\left(\frac{n\pi}{\varepsilon}\right)^2
+\ell(\ell+1)<K^2\right\}.
\tag{3.2}
$$

The inequality is strict at the comparison threshold, as required by the
counting convention. After multiplying (3.2) by $2\ell+1$ and summing, the
active radial integers are exactly

$$
n\pi<a,
\qquad
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\}.
$$

For $1\le n\le N$, put $b_n=(a^2-n^2\pi^2)^{1/2}$. The active angular
condition is

$$
\ell(\ell+1)<\frac{b_n^2}{\varepsilon^2}.
$$

Writing

$$
M_n=\left\lceil
\sqrt{\left(\frac{b_n}{\varepsilon}\right)^2+\frac14}
-\frac12\right\rceil,
$$

the allowed indices are $\ell=0,\ldots,M_n-1$. Their full spherical
multiplicity is

$$
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2.
$$

Consequently

$$
N_D(A_{\rho,1},K^2)
\le \mathcal P_\varepsilon(a):=\sum_{n=1}^N M_n^2,
\tag{P1}
$$

with the correct min--max direction and multiplicity.

At a product angular wall
$b_n^2/\varepsilon^2=L(L+1)$, strict counting excludes $\ell=L$,
so $M_n=L$ and the wall value is the lower-side value. Immediately above
the wall the count rises by $2L+1$. The first angular branch is $\ell=0$:
it enters for every $b_n>0$ and is absent at $b_n=0$.

### 3.2 Exact zero-count range

If $0\le a\le\pi$, no positive integer satisfies $n\pi<a$. This includes
both $a=0$ and the wall $a=\pi$. Thus $N=0$, (P1) is zero, and the shell
strict count is zero. For $0<a\le\pi$, the right side of (2.1) is positive,
so the desired comparison is strict; at $a=0$ it is equality.

### 3.3 The deficit: (P2)--(P6)

Let

$$
I_0(a)=\frac{2a^3}{3\pi},\qquad
S_0(a)=\sum_{n=1}^N(a^2-n^2\pi^2),\qquad
D(a)=I_0(a)-S_0(a).
\tag{P2}
$$

For $a>\pi$, strict radial counting gives the unique representation

$$
\frac a\pi=N+t,\qquad N\ge1,\qquad0<t\le1.
\tag{P3}
$$

This is the strict representation (P3). At $a=m\pi$ the excluded threshold forces
$(N,t)=(m-1,1)$, not $(m,0)$. Using
$\sum_{n=1}^Nn^2=N(N+1)(2N+1)/6$ gives

$$
\begin{aligned}
\frac{D(a)}{\pi^2}
&=\frac23(N+t)^3-N(N+t)^2
  +\frac{N(N+1)(2N+1)}6\\
&=\frac{N^2}{2}+N\left(t^2+\frac16\right)
  +\frac{2t^3}{3}.
\end{aligned}
\tag{P4}
$$

At a wall $a=m\pi$, the left/exact value from
$(N,t)=(m-1,1)$ and the right limit from $(N,t)\to(m,0+)$ are both

$$
\frac{m^2}{2}+\frac m6.
$$

Thus (P4), and hence $D$, is continuous across every radial wall even
though the newly positive $n=m,\ell=0$ product branch enters immediately
to the right.

Subtracting $(2/5)(N+t)^2$ from (P4) yields

$$
\frac{D(a)}{\pi^2}-\frac25\left(\frac a\pi\right)^2
=\frac{N^2}{10}
+N\left[\left(t-\frac25\right)^2+\frac1{150}\right]
+h(t),
\tag{3.3}
$$

where

$$
h(t)=\frac{2t^3}{3}-\frac{2t^2}{5},\qquad
h'(t)=2t\left(t-\frac25\right).
$$

On $0<t\le1$, the unique interior minimum is at $t=2/5$, and

$$
\min h=-\frac8{375}.
$$

Therefore

$$
\frac{D(a)}{\pi^2}-\frac25\left(\frac a\pi\right)^2
\ge \frac{N^2}{10}+\frac N{150}-\frac8{375}.
\tag{P6}
$$

The right side increases for integral $N\ge1$, and at $N=1$ it is

$$
\frac1{10}+\frac1{150}-\frac8{375}=\frac{32}{375}>0.
$$

This proves, without sampling,

$$
D(a)>\frac25a^2\qquad(a>\pi).
\tag{P5}
$$

### 3.4 Rounding cost and (P7)--(P9)

For $B=b_n/\varepsilon>0$, the strict ceiling inequality gives

$$
M_n<\sqrt{B^2+\frac14}+\frac12.
$$

All quantities are nonnegative, so squaring is legitimate. Since
$\sqrt{B^2+1/4}\le B+1/2$, one obtains

$$
\varepsilon^2M_n^2
<b_n^2+\varepsilon b_n+\varepsilon^2.
\tag{3.4}
$$

The function $x\mapsto(a^2-\pi^2x^2)^{1/2}$ is strictly decreasing on
its positive interval. Hence

$$
\sum_{n=1}^N b_n
<\int_0^N\sqrt{a^2-\pi^2x^2}\,dx
\le\int_0^{a/\pi}\sqrt{a^2-\pi^2x^2}\,dx
=\frac{a^2}{4},
\tag{3.5}
$$

and strict radial counting gives $N<a/\pi$. Summing (3.4),

$$
\varepsilon^2\mathcal P_\varepsilon(a)
<S_0(a)+\frac{\varepsilon a^2}{4}
+\frac{\varepsilon^2a}{\pi}.
\tag{3.6}
$$

It is therefore sufficient that

$$
D(a)\ge
\varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}.
\tag{P7}
$$

Indeed, (3.6) and (P7) imply

$$
\varepsilon^2\mathcal P_\varepsilon(a)
<I_0(a)(1-\varepsilon)
<I_0(a)m_\varepsilon.
\tag{3.7}
$$

For $a\ge\pi$ in (3.1), using $a\le\pi/(4\varepsilon)$,
$a\ge\pi$, and the strict elementary bound $\pi>3$, gives

$$
\begin{aligned}
\frac1{a^2}\left[
\varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}\right]
&=\frac{2\varepsilon a}{3\pi}+\frac\varepsilon4
  +\frac{\varepsilon^2}{\pi a}\\
&\le\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}.
\end{aligned}
\tag{P8}
$$

The last expression increases with $\varepsilon>0$. At the closed face
$\varepsilon=1/8$ its reserve below $2/5$ is

$$
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
\tag{P9}
$$

Thus (P5) is strictly stronger than (P7) throughout this range. Equations
(P1), (3.7), and (2.1) prove the target strictly for every $a>\pi$ in the
low piece.

### 3.5 Low ownership of the common face

The face $a=\pi/(4\varepsilon)$ is included in (3.1) and in (P8). Since
$\varepsilon\le1/8$, it has $a\ge2\pi$. At the corner
$(\varepsilon,a)=(1/8,2\pi)$ it is also the radial wall $m=2$, so the
required convention is $(N,t)=(1,1)$. Formula (P4), the strict ceiling
estimate, and the reserve (P9) all remain valid there. The low proof
therefore owns the entire common face, including the corner.

## 4. High complementary-action piece: complete proof of (N1)--(N3) and (H1)--(H12)

Assume now

$$
a\ge\frac{\pi}{4\varepsilon}.
\tag{4.1}
$$

In particular $a>0$. All action formulas below are on their exact domains.

### 4.1 Action geometry, inverse, curvature, and endpoints

For $0\le y\le ar$,

$$
J_r(y)=\sqrt{a^2r^2-y^2}-y\arccos\frac{y}{ar},
$$

and define, on the two closed subintervals with their common value at
$y=\rho a$,

$$
\mathcal A(y)=
\begin{cases}
\dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
   &0\le y\le\rho a,\\[6pt]
\dfrac{J_1(y)}{\pi\varepsilon},
   &\rho a\le y\le a.
\end{cases}
\tag{H1}
$$

Put

$$
T=\mathcal A(0)=\frac a\pi,
\qquad \tau=\mathcal A(\rho a).
$$

and direct differentiation on the interior gives

$$
J_r'(y)=-\arccos\frac{y}{ar},
\qquad
J_r''(y)=\frac1{\sqrt{a^2r^2-y^2}}.
\tag{4.2}
$$

Thus the piecewise formula (H1) is continuous and strictly decreasing from
$T=a/\pi$ to zero. At $y=\rho a$, $J_\rho=0$, and both one-sided first
derivatives equal $-\arccos\rho/(\pi\varepsilon)$. Consequently
$\mathcal A$ has a unique decreasing inverse

$$
R:[0,T]\longrightarrow[0,a],
$$

including both endpoints, and $F=R^2$ is continuous there.

For $\rho a<y<a$, put $\alpha=\arccos(y/a)$. Then

$$
g=-F'=\frac{2\pi\varepsilon y}{\alpha}.
\tag{4.3}
$$

The function $y/\alpha$ increases strictly with $y$, whereas $y=R(t)$
decreases with $t$. Hence $g$ decreases on $(0,\tau)$. For
$0<y<\rho a$, put

$$
\delta=\arccos\frac ya-\arccos\frac{y}{\rho a}>0.
$$

The identity

$$
\frac{\delta}{y}
=\int_\rho^1\frac{dr}{r\sqrt{a^2r^2-y^2}}
\tag{4.4}
$$

shows that $\delta/y$ increases strictly with $y$. Thus $y/\delta$
decreases with $y$, and

$$
g=\frac{2\pi\varepsilon y}{\delta}
$$

increases with $t$ on $(\tau,T)$. This proves (H2) at the actual,
ungridded $\tau$, without any assertion about whether $\tau$ is less than,
equal to, or greater than one. Formula (4.3) and its inner counterpart have
the same value at $y=\rho a$, so $g$ is continuous at $\tau$.

The endpoint values are

$$
F(0)=a^2,\qquad F(\tau)=\rho^2a^2,
\qquad F(T)=0.
$$

As $y\downarrow0$,

$$
\delta=\frac{\varepsilon y}{\rho a}+O(y^3),
$$

so

$$
g(T)=2\pi\rho a.
\tag{H3}
$$

At the other endpoint write $y=a\cos\theta$. Then

$$
t=\frac{a}{\pi\varepsilon}
(\sin\theta-\theta\cos\theta)
\sim\frac{a\theta^3}{3\pi\varepsilon},
\qquad
g=\frac{2\pi\varepsilon a\cos\theta}{\theta}=O(t^{-1/3}).
\tag{4.5}
$$

Thus $g$ is integrable at $t=0$. In particular, because $w(t)=t$ and
$W(t)=t^2/2$ near zero,

$$
w(t)g(t)=O(t^{2/3}),\qquad W(t)g(t)=O(t^{5/3})\to0.
\tag{4.6}
$$

This is the required improper trace, not a formal endpoint substitution.

All square roots and arccosines above have arguments in their stated closed
ranges. On the open intervals used for division, $\alpha>0$ or
$\delta>0$; $a,\rho,\varepsilon$ are positive. The only vanishing
denominators are handled by the endpoint limits (4.5) and (H3).

### 4.2 Exact layer cake and normalization: (N1)--(N2)

For $\ell\in\mathbb N_0$ and $n\ge1$, set

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad x_n=n-\frac14,
$$

and, extending $\mathcal A$ by zero for $y>a$, define

$$
q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_{\ell\ge0}y_\ell q_\ell.
\tag{N1}
$$

Here and below $[u]_<:=\lceil u\rceil-1$.

For every $y\ge0$, with $\mathcal A(y)=0$ when $y>a$,

$$
q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<
=\#\{n\ge1:n-\tfrac14<\mathcal A(y_\ell)\}.
\tag{4.7}
$$

This includes a phase-proxy wall: if
$\mathcal A(y_\ell)+1/4=m\in\mathbb Z$, then $q_\ell=m-1$, so the
threshold layer is excluded. At $y=a$ and beyond, $q_\ell=[1/4]_< =0$.

The sums are finite, so strict layer-cake interchange gives

$$
\begin{aligned}
P_{\mathcal A}
&=\varepsilon\sum_{\ell\ge0}y_\ell q_\ell\\
&=\varepsilon\sum_{\substack{n\ge1\\x_n<T}}
 \sum_{y_\ell<R(x_n)}y_\ell.
\end{aligned}
$$

If $M=M_\varepsilon(R(x_n))$, then

$$
\sum_{\ell=0}^{M-1}y_\ell
=\varepsilon\sum_{\ell=0}^{M-1}\left(\ell+\frac12\right)
=\frac{\varepsilon M^2}{2}.
$$

Therefore

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\ge1\\x_n<T}}
M_\varepsilon(R(x_n))^2.
\tag{N2a}
$$

This derives the discrete part of (N2) from (N1), including every strict
wall.

Differentiating $J_r$ with respect to $r$ also gives the exact integral
form

$$
\mathcal A(y)=\frac1{\pi\varepsilon}
\int_\rho^1\sqrt{a^2-\frac{y^2}{r^2}}_+\,dr.
\tag{4.8}
$$

The area under a decreasing inverse and Tonelli's theorem yield

$$
\frac12\int_0^T F(t)\,dt
=\int_0^a y\mathcal A(y)\,dy.
$$

Using $y=rz$ inside (4.8),

$$
\begin{aligned}
I:=\int_0^a y\mathcal A(y)\,dy
&=\frac1{\pi\varepsilon}\int_\rho^1r^2\,dr
  \int_0^a z\sqrt{a^2-z^2}\,dz\\
&=\frac{a^3}{3\pi\varepsilon}\int_\rho^1r^2\,dr\\
&=\frac{a^3}{3\pi}
  \left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\end{aligned}
\tag{N2b}
$$

This proves the full identity (N2), including its normalization.

### 4.3 Exact sawtooth calculation: (H4)

Define

$$
C(t)=\#\{n\ge1:n-\tfrac14<t\},\qquad
w(t)=t-C(t),\qquad
W(t)=\int_0^t w(s)\,ds,\qquad
\Psi(t)=W(t)-\frac t4.
$$

Apart from its immaterial point values at jumps,
$C(t)=\lfloor t+1/4\rfloor$. Write $t=k+s$ with
$k\in\mathbb N_0$ and $0\le s\le1$. The sawtooth has period one and mean
$1/4$, so $\Psi(t)=W(t)-t/4=\Psi(s)$. Direct integration on one period gives

$$
\Psi(s)=
\begin{cases}
\dfrac12(s-\frac14)^2-\dfrac1{32},&0\le s\le\frac34,\\[5pt]
\dfrac12(s-\frac54)^2-\dfrac1{32},&\frac34\le s\le1.
\end{cases}
\tag{4.9}
$$

Also $W(s)=s^2/2\ge0$ on the first subcell, and direct integration on the
second subcell keeps $W(s)>0$; adding $k/4$ proves $W(t)\ge0$ globally.
Formula (4.9) proves exactly

$$
W(t)\ge0,
\qquad
-\frac1{32}\le\Psi(t)\le\frac3{32}.
\tag{H4}
$$

At $x_n=n-1/4$, strict $C$ has the wall value $C(x_n)=n-1$;
$w$ has left value $3/4$ and right value $-1/4$. The primitives $W$ and
$\Psi$ are continuous, so (H4) owns both sides and the wall itself.

### 4.4 Stieltjes discrepancy and the ungridded split: (H5)

Distributionally $dw=dt-dC$. Since $F$ is continuous, $F(T)=0$, and
$w(0)=0$, Stieltjes integration by parts (first on $[\eta,T]$ and then
using (4.6)) gives

$$
D_{\rm rad}
=\int_0^TF(t)\,dt-
 \sum_{\substack{n\ge1\\x_n<T}}F(x_n)
=\int_0^T w(t)g(t)\,dt.
\tag{4.10}
$$

Split at the actual $\tau$. On $(0,\tau)$, $g$ decreases and $W\ge0$;
hence

$$
\int_0^\tau wg
=W(\tau)g(\tau)-\int_0^\tau W\,dg
\ge W(\tau)g(\tau).
\tag{4.11}
$$

The omitted lower boundary is exactly zero by (4.6), and the dropped
Stieltjes term $-\int_0^\tau W\,dg$ is nonnegative.

On $(\tau,T)$, $g$ increases and $w=1/4+\Psi'$. Combining its integration
by parts with (4.11) gives

$$
\begin{aligned}
D_{\rm rad}
&\ge \frac{F(\tau)}4+\frac{\tau g(\tau)}4
 +\Psi(T)g(T)-\int_\tau^T\Psi\,dg\\
&\ge \frac{F(\tau)}4-\frac{g(T)}8
 +g(\tau)\left(\frac\tau4+\frac3{32}\right).
\end{aligned}
\tag{4.12}
$$

Here the second line uses $\Psi(T)\ge-1/32$ and
$\Psi\le3/32$ against the positive measure $dg$. The final displayed
$g(\tau)$ term is nonnegative (indeed positive) and is the only further
dropped Stieltjes remainder. Using (H3),

$$
D_{\rm rad}
\ge\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\tag{H5}
$$

Nothing in this calculation depends on $\tau$ being in a special cell. If
$\tau$ is a grid point, below one, or above one, $W,\Psi$, and $g$ are
continuous at the split; the single value of $w$ is irrelevant to the
Lebesgue integral. This also covers both sides of every sawtooth jump.

### 4.5 Exact angular count and error: (H6)--(H8)

For $x\ge0$, strict half-integer counting is exactly

$$
M_\varepsilon(x)
=\max\left\{0,
\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil
\right\}.
\tag{H6}
$$

If $x/\varepsilon=m+1/2$, then $M_\varepsilon(x)=m$; the equality layer
$\ell=m$ is excluded. This includes the first wall $x/\varepsilon=1/2$,
where the count remains zero and the $\ell=0$ branch enters only above it.

For $x>0$, the strict ceiling inequality and nonnegativity permit the
squaring

$$
\varepsilon^2M_\varepsilon(x)^2
<\left(x+\frac\varepsilon2\right)^2
=x^2+\varepsilon x+\frac{\varepsilon^2}{4}.
\tag{4.13}
$$

The number of active radial action layers is

$$
J_{\rm rad}=\#\{n\ge1:n<T+1/4\}
=\lceil T+1/4\rceil-1<T+\frac14
=\frac a\pi+\frac14.
\tag{H7}
$$

At an action radial wall $x_n=T$, the layer is excluded; $F(T)=0$ makes
the Stieltjes identity continuous while preserving the strict count.
Applying (4.13) with $x=R(x_n)\le a$ and then (H7) yields

$$
\varepsilon^2
\sum_{x_n<T}M_\varepsilon(R(x_n))^2
<\sum_{x_n<T}F(x_n)+E,
\tag{4.14}
$$

where the complete angular error is strictly bounded by

$$
E=\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
\tag{H8}
$$

### 4.6 Uniform high screens: (H9)--(H11)

From (H5), (4.1), and $\rho=1-\varepsilon$,

$$
\frac{D_{\rm rad}}{a^2}
\ge\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
\ge\frac{(1-\varepsilon)(1-5\varepsilon)}4.
\tag{H9}
$$

The last function has derivative $(-6+10\varepsilon)/4<0$ on
$0<\varepsilon\le1/8$, so it decreases to

$$
\frac{21}{256}
$$

on the closed endpoint face.

Expanding $E/a^2$ and using $1/a\le4\varepsilon/\pi$ gives

$$
\frac{E}{a^2}
\le\frac\varepsilon\pi+\frac{\varepsilon^2}{\pi}
+\frac{\varepsilon^3}{\pi^2}+\frac{\varepsilon^4}{\pi^2}.
\tag{H10}
$$

Every replacement of $1/a$ is an equality exactly at the common optical
face; hence the sign in (H10) is correctly non-strict. The right side has
strictly positive derivative for $\varepsilon>0$ and therefore increases
to its value at $1/8$. The strict geometric inequality $\pi>3$ gives

$$
\frac1{8\pi}+\frac1{64\pi}
+\frac1{512\pi^2}+\frac1{4096\pi^2}
<\frac{193}{4096}.
$$

Consequently

$$
D_{\rm rad}-E
>a^2\left(\frac{21}{256}-\frac{193}{4096}\right)
=\frac{143}{4096}a^2>0.
\tag{H11}
$$

### 4.7 Strict completion: (H12), then (N3)

Equations (4.14) and (H11) give the complete strict chain

$$
\varepsilon^2
\sum_{x_n<T}M_\varepsilon(R(x_n))^2
<\sum_{x_n<T}F(x_n)+E
<\int_0^TF(t)\,dt.
\tag{H12}
$$

Using (N2a)--(N2b),

$$
P_{\mathcal A}<I.
$$

The permitted all-domain transfer (N3) now yields, strictly because
$a,K>0$ on the high piece,

$$
N_D(A_{\rho,1},K^2)
\le\frac{2P_{\mathcal A}}{\varepsilon^2}
<\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{N3}
$$

This proves the high piece without a pointwise semicircle comparison and
without any old-domain conclusion.

### 4.8 High ownership of the common face

All inequalities in the high proof include (4.1) with equality. At
$a=\pi/(4\varepsilon)$ the scaling steps in (H9)--(H10) have their stated
equalities, but $\pi>3$ still makes the bound on $E$ strict, leaving the
$143/4096$ reserve. At $(\varepsilon,a)=(1/8,2\pi)$ the action proof is
unchanged. Hence the high piece independently owns the entire common face.

## 5. Closed two-piece union

For every $0<\varepsilon\le1/8$ and every $a\ge0$, either

$$
0\le a\le\frac{\pi}{4\varepsilon}
$$

or

$$
a\ge\frac{\pi}{4\varepsilon}.
$$

There is no gap and no third interval. Both pieces include and prove the
common face. Together with the separately owned $a=0$ face, they prove the
entire target domain. No conclusion from Round 6 participates in this
union.

## 6. Complete branch, wall, and face ledger

* **$K=0$ / $K>0$.** At $K=a=0$ both sides are zero. At every $K>0$ the
  relevant product or action comparison is strict before transfer.
* **Zero and first product branches.** The exact interval
  $0\le a\le\pi$ has no radial mode. At $a=\pi$ the $n=1$ layer is
  excluded; immediately above it the first radial branch $n=1$ and first
  angular branch $\ell=0$ enter.
* **Every product radial wall.** At $a=m\pi$ the value is
  $(N,t)=(m-1,1)$. The left limit uses $t\uparrow1$; the right limit uses
  $(N,t)\to(m,0+)$. Both give $m^2/2+m/6$ in (P4). The new zero-width
  term makes $D$ continuous, while strict spectral counting excludes the
  new mode at the wall.
* **Every product angular wall.** At
  $b_n^2/\varepsilon^2=L(L+1)$, $M_n=L$ and $\ell=L$ is excluded. The
  jump above the wall has multiplicity $2L+1$. Formula (3.4) remains
  strict at the wall.
* **Optical face and corner.** Both pieces own
  $a=\pi/(4\varepsilon)$. At $(1/8,2\pi)$ the radial convention is
  $(N,t)=(1,1)$, and both reserves remain strict.
* **Ratio faces.** The lower ratio $\rho=7/8$, equivalently the closed
  $\varepsilon=1/8$ face, is included. The limit $\rho\uparrow1$ means
  $\varepsilon\downarrow0$ through positive values; $\varepsilon=0$ is
  never inserted into a denominator or claimed as part of the domain.
  The test faces $\varepsilon=1/100,1/25,1/10,1/8$ are ordinary included
  slices of the same proof; no estimate changes there.
* **Action radial walls.** A layer with $x_n=T$ is excluded by $x_n<T$.
  Since $F(T)=0$, the Stieltjes trace has no hidden endpoint mass. The
  first positive action radial branch is $n=1$, $x_1=3/4$; on the high
  piece $T\ge2$, so it is present.
* **Half-integer angular walls.** At
  $R(x_n)/\varepsilon=m+1/2$, (H6) gives $M=m$ and excludes $\ell=m$.
  At $m=0$, the $\ell=0$ branch enters only on the strict upper side.
* **Phase-proxy walls.** At
  $\mathcal A(y_\ell)+1/4=m\in\mathbb Z$, the strict bracket gives
  $q_\ell=m-1$; the phase threshold is not counted.
* **Action cutoffs and interfaces.** At $y=a$, $\mathcal A=0$ and
  $q_\ell=0$. At $y=\rho a$, the two formulas in (H1) and their first
  derivatives agree. The curvature changes at the actual
  $t=\tau$, where $g$ is continuous; no grid alignment is assumed.
* **Sawtooth placement of $\tau$.** Whether $\tau$ is on, immediately
  below, or immediately above a point $x_n$, the continuous $W,\Psi,g$
  give the same split. At every sawtooth jump, $w$ changes from $3/4$ to
  $-1/4$, while $W$ and $\Psi$ have matching one-sided values.
* **Improper and terminal traces.** At $t=0$, (4.5)--(4.6) prove
  integrability and $Wg\to0$. At $t=T$, $F(T)=0$ and
  $g(T)=2\pi\rho a$. The only dropped Stieltjes quantities are
  $-\int_0^\tau W\,dg\ge0$ and
  $g(\tau)(\tau/4+3/32)\ge0$; both are displayed explicitly.
* **Domains and legal algebra.** $R$ has exactly domain $[0,T]$ and range
  $[0,a]$. Every square root is taken with nonnegative radicand, every
  arccosine argument lies in $[0,1]$, and every interior denominator is
  positive. The endpoint zeros are treated by limits. The squarings in
  (3.4) and (4.13) have nonnegative sides; the comparison
  $\sqrt{B^2+1/4}\le B+1/2$ follows by squaring nonnegative quantities.
* **Monotonic reductions.** In (P8) the cost increases with
  $\varepsilon$ and with the allowed upper $a$; in (H9) the lower screen
  decreases on $(0,1/8]$; in (H10) the upper screen increases there.
  Equality in the $1/a$ scaling of (H10) occurs exactly at the common
  face and is deliberately retained as non-strict.
* **Conditional faces.** The interfaces
  $\rho=\rho_*,1/16,5/6,7/8,99/100$ and the energy faces
  $K=64,3456,K_0(5/6),295^2,200000$ are audited separately in Section 8.
  None is an input to Sections 3--5.

## 7. Exact symbolic and standard-library ledger

The algebra behind (P4) is the formal identity

$$
\frac23(N+t)^3-N(N+t)^2+\frac{N(N+1)(2N+1)}6
=\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
$$

The following pure-standard-library ledger uses only exact rational
arithmetic. The tiny polynomial dictionary verifies (P4) formally rather
than by sampling. The Machin-line certificate proves the screened bound
$\pi>333/106$ from alternating arctangent bounds; the main proof needs only
the weaker geometric fact $\pi>3$.

```python
from fractions import Fraction as Q

def clean(p):
    return {k: v for k, v in p.items() if v}
def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return clean(out)
def scale(c, p):
    return clean({k: Q(c) * v for k, v in p.items()})
def mul(p, q):
    out = {}
    for (i, j), u in p.items():
        for (k, l), v in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, Q(0)) + u * v
    return clean(out)
def power(p, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = mul(out, p)
    return out

one = {(0, 0): Q(1)}
N = {(1, 0): Q(1)}
t = {(0, 1): Q(1)}
x = add(N, t)
p4_left = add(
    scale(Q(2, 3), power(x, 3)),
    scale(-1, mul(N, power(x, 2))),
    scale(Q(1, 6), mul(mul(N, add(N, one)), add(scale(2, N), one))),
)
p4_right = add(
    scale(Q(1, 2), power(N, 2)),
    mul(N, power(t, 2)),
    scale(Q(1, 6), N),
    scale(Q(2, 3), power(t, 3)),
)
assert p4_left == p4_right

h = lambda z: Q(2, 3) * z**3 - Q(2, 5) * z**2
assert h(Q(2, 5)) == -Q(8, 375)
assert Q(1, 10) + Q(1, 150) - Q(8, 375) == Q(32, 375)

RP = lambda e: Q(2, 5) - (Q(1, 6) + e / 4 + e**2 / 9)
RH = lambda e, p: ((1-e)*(1-5*e)/4
                    - (e/p + e**2/p + e**3/p**2 + e**4/p**2))

assert RP(Q(1, 8)) == Q(577, 2880)
assert (1-Q(1, 8))*(1-5*Q(1, 8))/4 == Q(21, 256)
assert (Q(1, 8)/3 + Q(1, 8)**2/3
        + Q(1, 8)**3/9 + Q(1, 8)**4/9) == Q(193, 4096)
assert Q(21, 256) - Q(193, 4096) == Q(143, 4096)

# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
# S_3 is a strict lower bound for atan(1/5), and 1/239 is
# a strict upper bound for atan(1/239).
S3 = sum((-1)**j * Q(1, (2*j+1)*5**(2*j+1)) for j in range(4))
pi_lower = 16*S3 - 4*Q(1, 239)
assert pi_lower - Q(333, 106) == Q(3418213, 41563593750) > 0

# Navigation screens only.
assert RP(Q(1, 7)) == Q(1723, 8820)
assert RH(Q(1, 7), Q(3)) == Q(139, 21609)
assert RP(Q(4, 27)) == Q(12719, 65610)
assert RH(Q(4, 27), Q(333, 106)) == Q(162570113, 235723844196)
assert RH(Q(3, 20), Q(333, 106)) == -Q(44729, 20535000)
assert RH(Q(1, 6), Q(333, 106)) == -Q(3983743, 143712144)

assert Q(200000, 295**2) == Q(8000, 3481)
assert Q(8000, 3481) > 2
```

Thus the exact ledger reproduces (P4), the minimum $-8/375$, the
$N=1$ positivity $32/375$, $577/2880$, $21/256$, $193/4096$,
$143/4096$, all of (S1)--(S4), and $8000/3481>2$. The two positive stretch
screens and two negative coarse-screen values retain exactly the limited
status assigned to them in the packet.

## 8. Separate conditional-envelope and equality-face audit

This section is conditional on promotion of Sections 2--5 and uses the
accepted Round 15 boundary facts only here. It is not part of either
endpoint proof piece.

First, the interfaces are correctly ordered. Positivity of $\rho_*$ follows
from $\pi<4<3\sqrt3$. Also $\pi>3$ and
$\sqrt3<7/4$ imply

$$
\omega_0
<\frac{\sqrt3-1}{6}<\frac18,
\qquad
1+2C_*>2,
$$

and hence $0<\rho_*<1/16$. Exact cross multiplication then gives

$$
\rho_*<\frac1{16}<\frac56<\frac78<\frac{99}{100}<1.
$$

Assuming promotion, the prospective residual envelope consists of exactly:

1. $[\rho_*,1/16]$ with only $K<64$ left;
2. $[1/16,5/6]$ with only $K<K_0(5/6)<295^2$ left;
3. $[5/6,7/8]$ with only
   $K<54/(1-\rho)^2\le54/(1/8)^2=3456$ left; and
4. $[7/8,1)$ with no frequency left.

The ratio interfaces are owned on both adjoining sides: $\rho=\rho_*$ is
also in the accepted small-ratio all-frequency theorem;
$\rho=1/16$ and $5/6$ are shared envelope faces; $\rho=7/8$ is both the
new closed endpoint and the upper threshold face; and $\rho=99/100$ is
owned by both the new endpoint and the previously accepted thin endpoint.

The residual inequalities are strict in $K$. Therefore $K=64$,
$K=K_0(5/6)$, and $K=3456$ are cover faces, not residual points. In
particular,

$$
295^2=87025>3456>64,
\qquad K_0(5/6)<295^2,
$$

so the equality face $K=295^2$ is covered on all four ratio intervals.
The accepted $K=200000$ face remains valid but is not used to prove the
new equality face.

The accepted sharper threshold faces remain exactly inclusive on their
stated domains:

$$
K=\frac{54}{\varepsilon^2}\quad(0<\varepsilon\le1/6),
$$

and

$$
K=\frac{32}{\varepsilon^2}\quad(0<\varepsilon\le1/8),\qquad
K=\frac{24}{\varepsilon^2}\quad(0<\varepsilon\le1/10),\qquad
K=\frac{20}{\varepsilon^2}\quad(0<\varepsilon\le1/25).
$$

For example their closed outer test faces are respectively
$K=1944,2048,2400,12500$ at
$\varepsilon=1/6,1/8,1/10,1/25$. No sharper threshold is extrapolated
outside its accepted $\varepsilon$ domain. At the additional test face
$\varepsilon=1/100$, the accepted $20/\varepsilon^2$ equality is exactly
$K=200000$, matching the named accepted all-ratio ceiling face.

It follows conditionally, and only conditionally, that

$$
\boxed{0<\rho<1,\qquad K\ge295^2=87025.}
\tag{C1}
$$

is covered. The exact prospective reduction factor is

$$
\boxed{\frac{200000}{295^2}=\frac{8000}{3481}>2.}
\tag{C2}
$$

Thus (C1) has its equality face, while (C2) follows since
$8000>2\cdot3481=6962$. The bounded nonrectangular residual below
the analytic cover remains open. Accordingly this audit does not close
`SHELL-rho-compact`, `SHELL-rho-uniformity`, or `TARGET-shell-d3`, and it
does not promote `COMP-certified-bessel` beyond `diagnostic_only`.

## 9. Strongest exact conclusion

No proof step failed, so no smaller fallback domain is needed and no target
face has been moved. The strongest exact endpoint statement established by
this incumbent is precisely

$$
\boxed{
\frac78\le\rho<1,\quad K\ge0,
\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

It is equality at $K=0$ and strict at $K>0$. Stretch endpoints and the
conditional global ceiling are not claimed as promoted theorems here.
