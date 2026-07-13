# Round 6 diagnostic: exact scaled action, walls, and thin overlap scale

## Status and verdict

This report is an adversarial diagnostic of the exact thin-scaled shell
action.  It makes **no authoritative-state change** and supplies **no interval
certificate**.

The main findings are:

1. The exact action retains precisely the required mean cross-section at the
   continuous cubic level.
2. The rejected flat-product transition at
   $\varepsilon a/\pi\simeq3/4$ is not inherited by the exact
   radius-sensitive coarse proxy.  Every sampled exact-action proxy remains
   below the target there.
3. A proof cannot come from an uncorrected midpoint quadrature estimate: for
   every $0<\varepsilon\le1/10$, an exact one-channel example has the raw
   midpoint action sum **above the entire continuous integral**.  Floor
   savings are indispensable.
4. A single effective-radius flat action cannot both match the shell volume
   and dominate the exact action, because it deletes the whispering-gallery
   strip.
5. Sampled shifted-tail inequalities are favorable, including tails starting
   immediately below the inner turning interface.  This supports the
   thin-scaled shifted-tail route, but is not a uniform proof.
6. At the existing overlap scale $a=\varepsilon K_0(1-\varepsilon)$, the
   generic aggregate margin is expected to be extremely small.  Direct
   floating scans cannot reach that scale for genuinely thin shells and would
   not certify it if they could.

The reproducible implementation is
`computations/thin_scaled_action_round6_diagnostic.py`; its regression tests
are in
`computations/tests/test_thin_scaled_action_round6_diagnostic.py`.

## 1. Exact reduction

Put

$$
\rho=1-\varepsilon,
\qquad a=\varepsilon K,
\qquad y=\varepsilon\nu,
$$

and let

$$
G_R(y)=\frac1\pi
\left(\sqrt{R^2-y^2}-y\arccos\frac yR\right)
\quad(0\le y<R),
$$

extended by zero for $y\ge R$.  Changing variables from $s$ to
$r=1-\varepsilon s$ gives

$$
\boxed{
\mathcal A_{\varepsilon,a}(y)
=\frac1{\pi\varepsilon}\int_\rho^1
\sqrt{a^2-\frac{y^2}{r^2}}_+\,dr
=\frac{G_a(y)-G_{\rho a}(y)}{\varepsilon}.
}
\tag{1}
$$

This is exactly $G_K(\nu)-G_{\rho K}(\nu)$ in the unscaled notation.

On the half-integer mesh

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
$$

define the strict coarse proxy

$$
\mathscr Q_{\varepsilon,a}
=\varepsilon\sum_{y_\ell<a}y_\ell
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<.
\tag{2}
$$

Multiplication of the original weighted proxy by $\varepsilon^2/2$ shows
that its desired inequality is exactly

$$
\boxed{
\mathscr Q_{\varepsilon,a}
\le \mathscr W_{\varepsilon,a}
:=\int_0^a y\mathcal A_{\varepsilon,a}(y)\,dy.
}
\tag{3}
$$

Fubini and the substitution $y=aru$ give the exact identity

$$
\boxed{
\mathscr W_{\varepsilon,a}
=\frac{a^3}{3\pi\varepsilon}\int_\rho^1r^2\,dr
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
}
\tag{4}
$$

Thus the exact action recovers the required mean cross-section with no
asymptotic loss.

For comparison, the optimized transferred shift in scaled variables is

$$
s_{\varepsilon,a}(y)=
\begin{cases}
\displaystyle
\min\left\{
\frac{\varepsilon(3\rho^2a^2+2y^2)}
{24\pi(\rho^2a^2-y^2)^{3/2}},\frac14
\right\},&y<\rho a,\\[2mm]
\frac14,&y\ge\rho a.
\end{cases}
\tag{5}
$$

The optimized proxy is no larger than (2).  Consequently, a coarse-proxy
failure would not by itself refute the optimized phase route or the shell
inequality.

## 2. Exact adversarial obstructions to tempting shortcuts

### 2.1 Raw midpoint quadrature is false, even arbitrarily thin

Consider every

$$
0<\varepsilon\le\frac1{10},
\qquad K=1,
\qquad a=\varepsilon.
$$

There is one active half-integer, $\nu_0=1/2$, so $y_0=\varepsilon/2$.
Since $\rho\ge9/10$, the integrand in (1) is active on the whole radial
interval and is minimized at $r=\rho$.  Therefore

$$
\mathcal A_{\varepsilon,\varepsilon}(y_0)
\ge
\frac{\varepsilon}{\pi}
\sqrt{1-\frac1{4\rho^2}}
\ge
\frac{2\sqrt{14}}{9\pi}\varepsilon.
$$

It follows that

$$
\varepsilon y_0\mathcal A_{\varepsilon,\varepsilon}(y_0)
\ge\frac{\sqrt{14}}{9\pi}\varepsilon^3
>\frac1{3\pi}\varepsilon^3
>\mathscr W_{\varepsilon,\varepsilon},
\tag{6}
$$

where $\sqrt{14}>3$ and
$1-\varepsilon+\varepsilon^2/3<1$ were used.  This is an exact
counterexample family to

$$
\varepsilon\sum y_\ell\mathcal A(y_\ell)
\le\int y\mathcal A(y)\,dy.
$$

It is not a counterexample to (3): here every relevant strict floor is zero.
The fractional-part saving is precisely what repairs the bad midpoint sum.

### 2.2 No single volume-matched effective radius is a pointwise majorant

The flat action at radius $R$,

$$
F_R(y)=\frac1\pi\sqrt{a^2-\frac{y^2}{R^2}}_+,
$$

has cubic integral $R^2a^3/(3\pi)$.  Matching (4) forces

$$
R_{\rm eff}^2=1-\varepsilon+\frac{\varepsilon^2}{3}<1.
$$

But for every

$$
R_{\rm eff}a<y<a,
$$

$F_{R_{\rm eff}}(y)=0$ while
$\mathcal A_{\varepsilon,a}(y)>0$, because a positive outer radial sublayer
remains classically allowed.  Hence a one-radius flat proxy cannot
simultaneously match the cubic coefficient and dominate pointwise.  Any
bracketing proof must retain at least a radial partition or an explicit outer
turning layer.

### 2.3 There is no uniform pointwise fractional-part saving

For fixed $\varepsilon$ and a fixed mesh point $y_\ell$, the map

$$
a\longmapsto
\mathcal A_{\varepsilon,a}(y_\ell)+\frac14
$$

is continuous, strictly increasing once active, and unbounded.  It therefore
crosses every sufficiently large positive integer.  At a crossing with value
$m$, strict counting gives $m-1$ and strict remainder $1$; immediately to its
right, the count is $m$ and the remainder can be arbitrarily close to zero.
Thus no proof may assign every channel a fixed positive floor saving.  The
saving must be aggregated across channels or across shifted tails.

## 3. Bulk curvature and the turning interface

For $0\le y\le\rho a$, define

$$
f_y(r)=\sqrt{a^2-y^2/r^2}.
$$

Direct differentiation gives

$$
f_y''(r)
=-\frac{3y^2}{r^4f_y(r)}
-\frac{y^4}{r^6f_y(r)^3}<0.
$$

Therefore the following exact bulk bounds are available:

$$
\frac{f_y(\rho)+f_y(1)}{2\pi}
\le\mathcal A_{\varepsilon,a}(y)
\le\frac1\pi f_y\left(1-\frac\varepsilon2\right),
\tag{7}
$$

and Cauchy--Schwarz gives the sometimes sharper upper bound

$$
\mathcal A_{\varepsilon,a}(y)
\le\frac1\pi\sqrt{a^2-\frac{y^2}{\rho}}.
\tag{8}
$$

Neither (7) nor (8) extends as a global pointwise upper bound after positive
part extension: modes with $\rho a<y<a$ live only in an outer radial
sublayer and are exactly the modes such an extension can erase.

The action is decreasing, concave for $y<\rho a$, convex for
$\rho a<y<a$, and $C^1$ at the interface.  In particular,

$$
\mathcal A_{\varepsilon,a}(\rho a)
=\frac a\varepsilon G_1(\rho),
\qquad
\partial_y\mathcal A_{\varepsilon,a}(\rho a)
=-\frac{\arccos\rho}{\pi\varepsilon}.
\tag{9}
$$

The optimized shift is also continuous at the interface: its inner $H$ term
diverges and is capped at $1/4$ before reaching $y=\rho a$.

## 4. Whispering-gallery edge

Set

$$
y=a(1-\varepsilon t),
\qquad0\le t\le1.
$$

Only $0\le s<t$ is active.  The exact rescaling gives the formal, and
dominated-convergence-compatible, thin limit

$$
\frac{\mathcal A_{\varepsilon,a}(a(1-\varepsilon t))}
{a\sqrt\varepsilon}
\longrightarrow
\frac{2\sqrt2}{3\pi}t^{3/2}.
\tag{10}
$$

Consequently the continuous edge mass satisfies

$$
\frac{
\int_{\rho a}^{a}y\mathcal A_{\varepsilon,a}(y)\,dy
}{\mathscr W_{\varepsilon,a}}
\sim\frac{4\sqrt2}{5}\varepsilon^{3/2}.
\tag{11}
$$

Although lower order in the full cubic integral, this strip is positive and
cannot be deleted by a global effective-radius comparison.  At the
$a\asymp\varepsilon^{-1}$ product-transition scale it contains
$a\asymp\varepsilon^{-1}$ half-integer channels, so it is well resolved by
the scaled mesh.

## 5. Non-certified transition scan

The following values use

$$
c=\frac{\varepsilon a}{\pi},
\qquad c=\frac34,
$$

and ordinary floating/high-precision evaluation.  `action` means strict
floors of $\mathcal A$ alone, `optimized` uses (5), and `coarse` uses the
constant quarter shift in (2).

| $\varepsilon$ | active channels | action / target | optimized / target | coarse / target | coarse edge / target |
|---:|---:|---:|---:|---:|---:|
| $0.10$ | 236 | 0.895961 | 0.904580 | 0.944037 | 0.027693 |
| $0.05$ | 942 | 0.947019 | 0.948959 | 0.973952 | 0.010730 |
| $0.02$ | 5,890 | 0.979781 | 0.980123 | 0.989839 | 0.002799 |
| $0.01$ | 23,562 | 0.989873 | 0.989965 | 0.994951 | 0.001042 |
| $0.005$ | 94,248 | 0.994968 | 0.994991 | 0.997489 | 0.000375 |

No sampled exact-action proxy inherits the flat product proxy's sign change.
Instead, the observed coarse deficit is consistent with

$$
1-\frac{\mathscr Q}{\mathscr W}
\approx\frac{3\pi}{8a}
=\frac{3\varepsilon}{8c};
\tag{12}
$$

at $c=3/4$ this is $\varepsilon/2$.  Formula (12) is only an empirical
fractional-part average, not a bound: radial walls make any local uniform
fractional-saving assertion false.

The new analytic window in `phase-aggregate.md` was separately probed at
five points between

$$
c=\frac14
\quad\text{and}\quad
c=\frac1{8\pi\sqrt\varepsilon}.
$$

At the upper endpoint the coarse ratios were

| $\varepsilon$ | upper-endpoint coarse ratio |
|---:|---:|
| $0.01$ | 0.990366 |
| $0.005$ | 0.996652 |
| $0.002$ | 0.999155 |
| $0.001$ | 0.999702 |

No sampled wall anomaly or shifted-tail violation appeared in that window.
This agrees with, but does not certify, the independent analytic argument.

## 6. Radial and angular walls

The proxy is most exposed immediately to the right of a radial floor wall.
Three high-precision root probes locate

$$
\mathcal A_{\varepsilon,a}(y_\ell)+\frac14=m
$$

near $c=3/4$:

| $\varepsilon$ | $(\ell,m)$ | $c$ at wall | strict-wall ratio | immediate-right ratio | relative jump |
|---:|---:|---:|---:|---:|---:|
| 0.10 | (143, 6) | 0.750067740 | 0.943782 | 0.944926 | $1.1443\times10^{-3}$ |
| 0.05 | (640, 11) | 0.749949182 | 0.973999 | 0.974150 | $1.5170\times10^{-4}$ |
| 0.01 | (6826, 72) | 0.750000009 | 0.994951269 | 0.994951766 | $4.9681\times10^{-7}$ |

These roots are not interval isolated.  The target channel was manually
assigned $m-1$ at equality and $m$ immediately right, so the displayed jump
does respect the strict convention.

At an outer angular wall $y_\ell=a$, the new action is zero and the
quarter-shifted strict count is still zero; the angular wall itself creates
no proxy jump.  At the inner wall $y_\ell=\rho a$, (9) and the capped shift
show continuity.  The discontinuous events that require cellwise control are
the radial floor walls, not the turning-interface classification itself.

## 7. Shifted-tail diagnostic

For coarse counts

$$
q_\ell=
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<,
$$

the scaled shifted-tail inequality is

$$
\frac\varepsilon2
\left(q_r+2\sum_{\ell>r}q_\ell\right)
\le
\int_{y_r}^{a}\mathcal A_{\varepsilon,a}(y)\,dy.
\tag{13}
$$

Every tail was checked at

$$
\varepsilon\in\{0.10,0.05,0.02,0.01\},
\qquad
c\in\{0.25,0.75,2,10\}.
$$

No violation was found.  At $c=3/4$, the smallest margins among starts below
the inner interface were:

| $\varepsilon$ | minimum scaled inner-tail margin | $y_r/(\rho a)$ at minimum |
|---:|---:|---:|
| 0.10 | 0.542411 | 0.997371 |
| 0.05 | 0.547800 | 0.999046 |
| 0.02 | 0.583451 | 0.999969 |
| 0.01 | 0.570254 | 0.999965 |

The smallest all-tail margins occurred above the interface, on the already
audited high-angular side, and were positive but much smaller.  This evidence
points toward a thin-uniform proof of (13), especially for the tails adjacent
to $y=\rho a$.  It does not justify extrapolation to all
$\varepsilon,a$, because the scan is finite and wall decisions are floating.

## 8. Existing high-energy overlap scale

Let

$$
\eta_\rho=G_1(\rho),
\qquad
A_\rho=\frac{2\pi\rho}{\varepsilon},
$$

and use the existing exact formula for $K_0(\rho)$.  Since

$$
\eta_{1-\varepsilon}
=\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}
\left(1+\frac\varepsilon{20}+O(\varepsilon^2)\right),
$$

one obtains

$$
\boxed{
a_{\rm HE}:=\varepsilon K_0(1-\varepsilon)
=\frac{9\pi^3}{4}\varepsilon^{-3}
\left(1-\frac{11}{10}\varepsilon+O(\varepsilon^2)\right),
}
\tag{14}
$$

and hence

$$
c_{\rm HE}
=\frac{\varepsilon a_{\rm HE}}\pi
\sim\frac{9\pi^2}{4}\varepsilon^{-2}.
\tag{15}
$$

High-precision evaluations are:

| $\varepsilon$ | $K_0$ | $a_{\rm HE}=\varepsilon K_0$ | $c_{\rm HE}$ | $3\pi/(8a_{\rm HE})$ |
|---:|---:|---:|---:|---:|
| 0.10 | $6.2191\times10^5$ | $6.2191\times10^4$ | $1.9796\times10^3$ | $1.8943\times10^{-5}$ |
| 0.05 | $1.0552\times10^7$ | $5.2760\times10^5$ | $8.3970\times10^3$ | $2.2329\times10^{-6}$ |
| 0.02 | $4.2645\times10^8$ | $8.5291\times10^6$ | $5.4298\times10^4$ | $1.3813\times10^{-7}$ |
| 0.01 | $6.8997\times10^9$ | $6.8997\times10^7$ | $2.1963\times10^5$ | $1.7074\times10^{-8}$ |

The last column is the heuristic scale from (12), not a certified margin.
It shows why a brute-force floating check near overlap is unsuitable: at
$\varepsilon=0.01$ there are about $K_0\simeq6.9$ billion angular channels,
and the expected relative discrepancy is only about $1.7\times10^{-8}$.

## 9. Recommendation for the incumbent proof

The diagnostics favor the following order of attack:

1. Use the proved aggregate window in `phase-aggregate.md` as the next exact
   extension of Round 5.
2. Seek a uniform scaled proof of the shifted-tail inequality (13), retaining
   the concave bulk, the $C^1$ inner interface, and the convex outer strip.
3. Aggregate floor savings before any worst-case fractional-part bound.  The
   exact family (6) rules out a pure midpoint argument, and radial-wall
   continuity rules out a fixed channelwise saving.
4. If radial bracketing is used, keep an explicit outer layer; a single
   volume-matched radius is impossible as a pointwise majorant.
5. Require an explicit analytic overlap with (14).  Do not ask interval
   arithmetic to certify the unbounded strip between the current aggregate
   window and $a_{\rm HE}$.

## 10. Reproduction and scope

Run

```powershell
python computations/thin_scaled_action_round6_diagnostic.py `
  --epsilons 0.1 0.05 0.02 0.01 `
  --cs 0.25 0.75 2 10 `
  --wall-probe 0.1:143:6 `
  --wall-probe 0.05:640:11 `
  --wall-probe 0.01:6826:72
```

and

```powershell
python -m pytest computations/tests/test_thin_scaled_action_round6_diagnostic.py -q
```

The script labels all floating output `diagnostic_only`, flags channels near
integer walls, and does not call any Bessel-root routine.  Nothing in this
report certifies an unbounded parameter region, promotes
`SHELL-thin-curvature-intermediate`, or changes the authoritative proof
state.
