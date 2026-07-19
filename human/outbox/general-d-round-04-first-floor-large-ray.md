# General dimension, Round 4d: rigorous first-floor large-ray certificate

Date: 18 July 2026  
Scope: the ordinary first-floor branch \(F_0=1,\ p<n\), on the wall
\(A(r+p)=3/4\), in the sector

\[
 r\ge \frac32,\qquad s=n-p-1\in\{0,1\},\qquad x=r+p\ge100.
\]

Status: **proved** by an analytic compactification followed by a
384-bit directed-rounding Arb branch-and-bound.  This note does not claim
the global first-floor exhaustion: the \(s\ge2\) cone and a finite set with
\(s=0,1,\ x<100\) remain.

The verifier is

scripts/general_d_first_floor_ray_verify.py.

## 1. Statement

Let

\[
 A(z)=G_K(z)-G_\mu(z),\qquad
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi},
\]

and put

\[
 x=r+p,\qquad y=x+1,\qquad
 q=x+s+1,\qquad \mu=q+\alpha,\qquad 0\le\alpha\le1.
\]

Thus

\[
 \beta:=\mu-x=s+1+\alpha,\qquad L:=\mu-y=\beta-1=s+\alpha.
\]

At the first-shelf wall \(A(x)=3/4\), write

\[
 v=A(y),\qquad
 \lambda=\frac{K-\mu}{\pi\mu},\qquad
 c=\frac1\pi\arccos\frac\mu K,
\]

and

\[
 \mathcal E
 =2\int_y^\mu
  [v-\lambda(S_y-S_z)]_+\,dz
  +\frac{(v-\lambda S_y)_+^2}{c},
 \qquad S_z=\sqrt{\mu^2-z^2}.
\]

The weakened first-drop certificate is

\[
 W=p\left(A(r)-\frac54\right)+v-\frac14+\mathcal E.
 \tag{1}
\]

The result certified here is

> **Theorem 1.** If \(r\ge3/2\), \(s\in\{0,1\}\), and \(x\ge100\), then
> \(W>0\) at every wall point \(A(x)=3/4\).  The proof covers the continuous
> relaxation of \(r,p,\alpha\); hence it covers the required half-integral
> and integral chamber parameters.

## 2. A rigorous compact cone

Set

\[
 \delta=K-\mu,
 \qquad t=x^{-1/3},
 \qquad \kappa=t\delta,
 \qquad P=tp.
 \tag{2}
\]

Changing variables \(R=x+u\) in the wall equation gives the exact identity

\[
 \frac{3\pi}{4}
 =\int_\beta^{\beta+\delta}
   \frac{\sqrt{u(2x+u)}}{x+u}\,du.
 \tag{3}
\]

Here \(1\le\beta\le3\).

### 2.1 Upper and lower bounds for \(\delta\)

First, \(\delta<x-\beta\).  Otherwise the interval in (3) contains
\([x/2,x]\), and on that interval the integrand is at least
\(\sqrt5/3\).  Since \(x\ge100\), this would give

\[
 \frac{3\pi}{4}\ge\frac{x\sqrt5}{6},
\]

which is impossible.

Consequently \(u<x\) throughout (3), and

\[
 \frac{\sqrt{u(2x+u)}}{x+u}
 \ge \sqrt{\frac{u}{2x}}.
\]

Since
\((\beta+\delta)^{3/2}-\beta^{3/2}\ge\delta^{3/2}\), (3) yields

\[
 \delta\le Cx^{1/3},
 \qquad
 C=\left(\frac{9\pi\sqrt2}{8}\right)^{2/3}
   <\frac{731}{250}=2.924.
 \tag{4}
\]

In the other direction,

\[
 \frac{\sqrt{u(2x+u)}}{x+u}
 \le\sqrt{\frac{2u}{x}},
\]

so monotonicity of the integrand gives

\[
 \frac{3\pi}{4}
 \le \delta\sqrt{\frac{2(\beta+\delta)}x}.
 \tag{5}
\]

The rational number

\[
 T_*:=\frac{53861}{250000}=0.215444
\]

strictly exceeds \(100^{-1/3}\).  Therefore

\[
 \beta+\delta
 \le (C+3T_*)x^{1/3}=:Bx^{1/3},
\]

and (5) gives

\[
 \delta\ge Dx^{1/3},
 \qquad
 D=\frac{3\pi/4}{\sqrt{2B}}
   >\frac{22}{25}=0.88.
 \tag{6}
\]

The Arb preamble certifies, with directed rounding,

\[
 C=2.923332817290\ldots<2.924,
 \qquad
 D=0.881825023935\ldots>0.88.
\]

Thus every wall point in the asserted ray has

\[
 \boxed{\frac{22}{25}<\kappa<\frac{731}{250}.}
 \tag{7}
\]

### 2.2 A rigorous upper bound for \(P\) at a possible failure

Let

\[
 \Delta=A(r)-\frac34.
\]

The already proved wall reduction shows that a failure of (1) must have
\(0<\Delta<1/2\).  For \(R\in[\mu,K]\), put

\[
 f_z(R)=\sqrt{1-z^2/R^2}.
\]

Since \(f_r\ge f_x\),

\[
 f_r-f_x
 =\frac{x^2-r^2}{R^2(f_r+f_x)}
 \ge
 \frac{x^2-r^2}{2K\sqrt{K^2-r^2}}.
\]

After integration,

\[
 \Delta\ge
 \frac{\delta(x^2-r^2)}{2\pi K\sqrt{K^2-r^2}}.
 \tag{8}
\]

Put \(B_0=3571/1000\) and \(C_K=583/500\).  The inequalities above and
the Arb checks give

\[
 \beta+\delta<B_0x^{1/3},
 \qquad K<C_Kx.
\]

Moreover

\[
 x^2-r^2=p(2x-p)\ge px,
\]

and

\[
 K-r\le (B_0+P)x^{1/3},
 \qquad K+r<(C_K+1)x.
\]

Substitution in (8) yields

\[
 \Delta\ge
 \frac{(22/25)P}
 {2\pi C_K\sqrt{(C_K+1)(B_0+P)}}.
 \tag{9}
\]

If \(\Delta<1/2\), then

\[
 \frac{22}{25}P
 <\pi C_K\sqrt{(C_K+1)(B_0+P)}.
 \tag{10}
\]

The left side divided by \(\sqrt{B_0+P}\) is strictly increasing.  At
\(P=41\), Arb proves the strict reverse of (10).  Hence every possible
failure lies in

\[
 \boxed{0\le P<41.}
 \tag{11}
\]

Points with \(P\ge41\) have \(A(r)\ge5/4\) and are automatic in (1).

## 3. Two-panel enclosure of the implicit wall

At the radius node

\[
 R=\mu+\xi\delta,
 \qquad0\le\xi\le1,
 \qquad w_\xi=\beta t+\xi\kappa,
\]

the three scaled radius profiles are

\[
 \Phi_x(t,w)
 =\frac{\sqrt{w(2+t^2w)}}{1+t^2w},
 \tag{12}
\]

\[
 \Phi_r(t,P,w)
 =\frac{\sqrt{(w+P)(2+t^2(w-P))}}{1+t^2w},
 \tag{13}
\]

and

\[
 \Phi_y(t,\beta,\kappa,\xi)
 =\frac{
 \sqrt{((\beta-1)t+\xi\kappa)
       (2+t^2((\beta+1)t+\xi\kappa))}}
 {1+t^2(\beta t+\xi\kappa)}.
 \tag{14}
\]

These formulas are exact: \(f_x=t\Phi_x\), \(f_r=t\Phi_r\), and
\(f_y=t\Phi_y\).  On the compact cone,

\[
 2-Pt^2\ge2-41T_*^2>0,
\]

so every displayed radicand is nonnegative, including at \(t=0\).

For a profile \(F(\xi)\), define

\[
 T_2[F]=\frac{F(0)+2F(1/2)+F(1)}4,
 \qquad
 M_2[F]=\frac{F(1/4)+F(3/4)}2.
 \tag{15}
\]

For fixed \(z\), the radius profile is increasing and strictly concave:

\[
 f_z'(R)=\frac{z^2}{R^3f_z(R)}>0,
\]

\[
 f_z''(R)
 =-\frac{3z^2}{R^4f_z(R)}
  -\frac{z^4}{R^6f_z(R)^3}<0.
 \tag{16}
\]

Therefore the composite two-panel trapezoid and midpoint inequalities give

\[
 \frac\kappa\pi T_2[\Phi_z]
 \le A(z)
 \le\frac\kappa\pi M_2[\Phi_z].
 \tag{17}
\]

In particular, the exact implicit wall satisfies

\[
 \boxed{
 \frac\kappa\pi T_2[\Phi_x]
 \le\frac34
 \le\frac\kappa\pi M_2[\Phi_x].}
 \tag{18}
\]

Both endpoint expressions are increasing in \(\kappa\): increasing
\(\kappa\) lengthens the radius interval and increases every radius node.
The verifier bisects (18), with interval-valued \(t,\beta\), to enclose
every possible wall root.  It never replaces the wall by a sampled root.

The same trapezoid bound supplies

\[
 A(r)\ge \underline A_r
 :=\frac\kappa\pi T_2[\Phi_r],
 \qquad
 v=A(y)\ge \underline v
 :=\frac\kappa\pi T_2[\Phi_y].
 \tag{19}
\]

## 4. The product/transition term is retained

Put

\[
 h=v-\lambda S_y.
\]

The slope envelope anchored at the wall gives

\[
 h\ge H:=\frac34-\lambda S_x.
\]

In compact variables this is

\[
 H
 =\frac34-
 \frac{\kappa\sqrt t\,\sqrt{\beta(2+\beta t^3)}}
 {\pi(1+\beta t^3)}.
 \tag{20}
\]

Thus \(H=0\) is the explicit lower-profile product/transition boundary.
The verifier does not discard it: a box is not accepted by the terminal
certificate unless directed rounding proves \(H>0\) on the entire box.
Every wall-compatible nonautomatic box in this ray is eventually proved to
lie strictly on that positive side.

When \(H>0\), the terminal profile is at least \(H\) throughout
\([y,\mu]\), so

\[
 \mathcal E\ge2LH+\frac{H^2}{c}.
 \tag{21}
\]

Let

\[
 \vartheta=\frac\kappa{1+\beta t^3},
 \qquad
 Q=\frac{\sqrt{\vartheta(2+t^2\vartheta)}}\pi.
 \tag{22}
\]

Since

\[
 \frac ct
 =\frac1{\pi t}
 \arctan\!\left(t\sqrt{2\vartheta+t^2\vartheta^2}\right)
 \le Q,
 \tag{23}
\]

one has

\[
 t\frac{H^2}{c}\ge\frac{H^2}{Q}.
\]

Combining (1), (19), and (21)--(23) gives the stable scaled lower
certificate

\[
 \boxed{
 tW\ge\mathscr C
 :=P\left(\underline A_r-\frac54\right)
 +t\left(\underline v-\frac14+2LH\right)
 +\frac{H^2}{Q}.}
 \tag{24}
\]

Formula (24) has a finite continuous limit at \(t=0\).  It is the scalar
certified by the Arb subdivision.

## 5. Directed-rounding branch-and-bound

For each \(s=0,1\), the verifier covers

\[
 0\le t\le T_*,\qquad
 s+1\le\beta\le s+2,\qquad
 0\le P\le41,
 \tag{25}
\]

and encloses \(\kappa\) from (18) inside (7).  The actual domain condition
\(r\ge3/2\) is

\[
 1-Pt^2-\frac32t^3\ge0.
 \tag{26}
\]

Every accepted box has one of the following rigorous dispositions:

1. (26) is strictly false, so the box misses the asserted ray;
2. \(\underline A_r\ge5/4\), so (1) is automatic;
3. \(H>0\) and the Arb lower endpoint of \(\mathscr C\) is strictly
   positive.

All transcendental and algebraic interval operations use 384-bit Arb
directed rounding.  Floating point is used only to choose which coordinate
to bisect and to print diagnostic margins; it is not used in a sign
decision.

The reproducible output is:

    PASS s=0, beta in [1,2]
      processed=17697, invalid=4, automatic=170, positive=8675,
      max-depth=21

    PASS s=1, beta in [2,3]
      processed=25367, invalid=5, automatic=140, positive=12539,
      max-depth=22

    CERTIFIED: W>0 on the implicit first-floor wall for the continuous
    large-ray relaxation x>=100, r>=3/2, s=0,1.
    Total branch-and-bound boxes processed: 43064

The smallest printed accepted lower endpoints, approximately
\(4.67\times10^{-6}\) and \(1.97\times10^{-6}\), are diagnostics only.  The
proof consists of the strict Arb signs on all accepted boxes.

## 6. Precisely what remains

This certificate removes the previously open compactified large ray

\[
 r\ge\frac32,\qquad s\in\{0,1\},\qquad x\ge100.
\]

It does **not** prove that the ten known weakened-certificate failures are
globally exhaustive.  The remaining first-floor wall domain is:

1. the unbounded cone \(s\ge2\);
2. for \(s=0,1\), the finite half-grid chamber set with
   \(r\ge3/2,\ x<100\);
3. the two small-start rays \(r=1/2\) and \(r=1\), which the prior wall
   bounds reduce to finite \(x\)-ranges.

Thus the large-ray/product-transition obstruction is now a theorem, while
the next useful step is either a global \(s\ge2\) estimate or an exact Arb
enumeration of the finite \(s=0,1,\ x<100\) chamber set.
