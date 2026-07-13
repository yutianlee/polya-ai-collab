# Round 11 Exploration: Aggregate-Loss Inventory and Fallback

## Classification

The Round 6 coefficient $1/8$ is proof slack.  It comes from charging every
outer whispering-gallery mesh point at the maximum interface action.  It is
not forced by the Jensen domain, the curvature switch, or the strict floor
conventions.

The direct inverse-action bridge selected in the Round 11 incumbent is
stronger and closes the entire complementary range.  This report records an
independent, simpler fallback: integrated outer-strip accounting alone raises
the aggregate coefficient from $1/8$ to $25/32$.

## 1. Loss inventory

| Step | Round 6 charge | Status |
|---|---:|---|
| Effective-semicircle shifted radial deficit | lower bounded by $a^2/12$ | genuine positive reserve, but the constant was coarse |
| Jensen comparison | valid only for $y\le\rho a$ | genuine domain restriction |
| Outer action | every channel charged at $\mathcal A(\rho a)$ | dominant avoidable loss |
| Outer strict floor | one extra unit per channel | genuine but lower order |
| Radial and angular walls | exact strict conventions | no asymptotic loss |

The old outer charge has size

$$
\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}\pi+1\right),
$$

whose leading coefficient is obtained by replacing the whole edge profile by
its maximum.  The exact edge profile instead decays like the $3/2$ power of
the distance from the outer boundary.

## 2. Stronger effective-semicircle reserve

Retain the accepted Round 6 notation

$$
t=\frac a\pi,
\quad
N=\#\{n\ge1:n-1/4<t\},
\quad
u=t-N\in(-1/4,3/4].
$$

The exact shifted deficit satisfies

$$
\frac D{\pi^2}
=\frac{N^2}{4}+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}
>
\frac{N^2}{4}-\frac N{48}-\frac1{96}.
$$

On $\varepsilon\le1/100$ and $a\ge\pi/(4\varepsilon)$, one has
$t\ge25$, $N/t\ge97/100$, and $N/t<101/100$.  Hence

$$
\frac D{a^2}>\frac{7031}{30000}.
$$

Using the exact angular ceiling and quarter-disk sum from Round 6 gives

$$
I-P_{\mathcal B}>
\frac{344197}{3000000}a^2
>\frac{57}{500}a^2.
\tag{1}
$$

## 3. Integrated edge charge

For $y=a(1-\varepsilon r)$, $0\le r\le1$, the active radial subinterval and
$1-v\ge\rho$ give

$$
\mathcal A(a(1-\varepsilon r))
\le
\frac{2\sqrt2}{3\pi\sqrt\rho}
a\sqrt\varepsilon\,r^{3/2}.
\tag{2}
$$

The function $y\mapsto y\mathcal A(y)$ is decreasing on
$[\rho a,a]$.  Thus the strict outer mesh sum is bounded by its integral,
one first-cell correction, and one floor unit per mesh point.  This yields

$$
\frac{E_{\rm out}}{a^2}
<
\frac{4\sqrt2}{15\pi\sqrt\rho}a\varepsilon^{3/2}
+\frac{2\sqrt2}{3\pi\sqrt\rho}\varepsilon^{3/2}
+\varepsilon\left(1+\frac1a\right).
\tag{3}
$$

The exact elementary bounds

$$
\frac{\sqrt2}{\pi\sqrt\rho}<\frac{398}{825},
\qquad
a\varepsilon^{3/2}\le\frac{25}{32}
$$

turn (3) into

$$
\frac{E_{\rm out}}{a^2}
<\frac{1387}{12500}
<\frac{57}{500},
$$

with remaining rational margin $19/6250$.  Combining with (1) proves the
fallback aggregate range

$$
\frac{\pi}{4\varepsilon}
\le a\le
\frac{25}{32\varepsilon^{3/2}}.
$$

It overlaps the accepted Round 9 high theorem through
$\varepsilon=1/400$, at the exact joining height $K=2{,}500{,}000$.

## 4. Selection decision

The fallback already meets the Round 11 target and would lower the global
ceiling to $6000^2$.  The selected direct inverse-action proof is stronger:
it begins at the old aggregate face and covers every larger $a$, thereby
proving all frequencies through $\varepsilon=1/100$.  The fallback is kept
as an independent route and as evidence that the old $1/8$ coefficient was
not structural; it is not used as a dependency of the selected theorem.
