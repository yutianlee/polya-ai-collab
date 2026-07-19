# General dimension, Round 26: lossless stationary projection and exact-image falsification of the Round 25 lower scalar

Date: 19 July 2026  
Status: rigorous projection reduction and directed-Arb obstruction; independent audit required

## 0. Scope and theorem boundary

This note treats only the delicate Round 24 cell

\[
 B=f-1\geq1,\qquad 0<u<1/\sqrt2,
\]

at an interior fixed-\(\mu\) stationary point of \(\mathcal C _8\).  It has
two results.

1. The full paired-shelf projection has a lossless discrete description.  For
   fixed \((B,m,t,u)\) and a parity grid, the interface relation fixes
   \((q,\alpha,x)\), and stationarity leaves at most one positive integer
   \(p\).
2. Even after the exact paired shelf integrals, activity condition, parity
   grid, and coupled discrete \(p\)-owner are imposed, the Round 25 lower
   scalar \(\mathcal F\) can be negative.  A directed-Arb enclosure below
   proves \(\mathcal F<-1/50\) at one exact-image stationary point, while
   \(\mathcal C _8>77/50\) there.

Thus the target “\(\mathcal F\geq0\) on the full exact projected shelf
image” is false.  This is not a counterexample to \(\mathcal C _8\geq0\),
\(\mathcal R_J\geq0\), CST-H, or the general-dimensional Polya theorem.  The
correct next pointwise target must retain the exact stationary integer
\(p\), rather than replace it by the Round 25 continuous upper bound
\(p_{\max}\).

## 1. Exact cumulative shelf function

Keep the Round 24--25 notation

\[
 H=\tan t-t,\qquad W=\frac{\mu H}{\pi}=B+u,
 \qquad \delta=\frac34-u,
\]

and define

\[
 \sigma_t(s)=
 \frac{\arccos(s\cos t/\mu)-\arccos(s/\mu)}{\pi},
 \qquad
 \mathscr I_t(y)=\int_y^\mu\sigma_t(s)\,ds.
 \tag{1.1}
\]

Then the complete first-shelf conditions on the delicate cell are exactly

\[
 \boxed{
 \mathscr I_t(x)\geq\delta>
 \mathscr I_t(x+1),\qquad
 \mathscr I_t(r)<\delta+1.}
 \tag{1.2}
\]

No endpoint estimate has been substituted here.  If \(y=\mu v\), the
integral also has the closed form

\[
 \mathscr I_t(\mu v)=\frac{\mu}{\pi}
 \{F_t(1)-F_t(v)\},
 \tag{1.3}
\]

where

\[
 F_t(v)=v\{\arccos(v\cos t)-\arccos v\}
 -\frac{\sqrt{1-v^2\cos^2t}}{\cos t}
 +\sqrt{1-v^2},
 \qquad F_t(1)=t-\tan t.
 \tag{1.4}
\]

Equations (1.1)--(1.4) are just the antiderivative of the exact shelf slope.

## 2. Lossless parity projection

Let

\[
 \mathcal G_0=\mathbb Z,
 \qquad
 \mathcal G_{1/2}=\mathbb Z+\frac12
\]

denote the integer and half-integer owner grids.  Their lower owner bounds are
respectively \(r\geq1\) and \(r\geq3/2\).  Given
\(B,m\in\mathbb N\), \(0<t<\pi/2\), and \(0<u<1/\sqrt2\), put

\[
 \mu=\frac{\pi(B+u)}{H}
\]

and, for either chosen grid, define

\[
 q=\max\{s\in\mathcal G_\varepsilon:s\leq\mu\},
 \qquad \alpha=\mu-q\in[0,1),
 \qquad x=q-m.
 \tag{2.1}
\]

Finally retain the Round 25 quantities

\[
 L=\frac{4u(B+u)\tan^2t}{H},\qquad
 R=\frac m\pi+\frac{B\pi}{2t^2}-L,
 \qquad
 P=\frac{3\pi^2(B+u)R}{H\sin t}.
 \tag{2.2}
\]

### Lemma 2.1 (lossless stationary projection)

On the delicate cell, an exact interior stationary candidate on the chosen
parity grid is equivalent to the existence of a positive integer \(p\) such
that, with \(r=x-p\),

\[
 r\in\mathcal G_\varepsilon,
 \qquad r\geq r_{\min},
 \qquad
 \boxed{p^2(3x-p)=P,}
 \tag{2.3}
\]

together with the full shelf conditions (1.2), the Round 23 strict owner
activity inequality, and the literal cell conditions

\[
 B=f-1,\qquad 0<u<1/\sqrt2.
 \tag{2.4}
\]

If the Round 24 discrete minimization is being used, this \(p\) must in
addition be one of the discrete minimizers of

\[
 S_x(j)=k j^2(3x-j)-\frac j2,
 \qquad k=\frac{1-\cos t}{3\pi\mu},
 \tag{2.5}
\]

on the exact feasible prefix.

For fixed \((B,m,t,u)\), grid, and hence fixed \(x\), equation (2.3) has at
most one positive integer solution compatible with \(r>0\).

### Proof

The grid definition (2.1) is exactly the interface identity
\(q\leq\mu<q+1\), so it loses neither \(\alpha\) nor the parity information.
It gives \(q=x+m=r+p+m\).  Round 25 equation (3.2) is equivalent to

\[
 p^2(3r+2p)=P.
\]

Substitution of \(r=x-p\) gives (2.3).  Conversely, reversing this
calculation gives the fixed-\(\mu\) stationary equation.  Equations (1.2),
(2.4), the start wall, and activity are precisely the retained Round 23--24
feasibility conditions, so the characterization is lossless.

For uniqueness, on \(0<p<x\) one has

\[
 \frac{d}{dp}\{p^2(3x-p)\}=3p(2x-p)>0.
\]

Thus (2.3) has at most one positive real solution in the owner range, hence
at most one positive integer solution.  The final owner condition (2.5) is
the audited Round 24 prefix minimization and has not been relaxed.  \(\square\)

This improves the Round 25 continuous projection: at a stationary point the
integer \(p\) is not merely bounded by \(p_{\max}\); it is pinned by one
strictly monotone cubic equation after the parity quantization fixes \(x\).

## 3. A full-image stationary point

Use the half-integer grid and the exact data

\[
 B=1,\quad f=2,\quad m=6,\quad
 r=\frac{25}{2},\quad p=6,\quad
 \alpha=\frac9{10}.
 \tag{3.1}
\]

Then

\[
 x=r+p=\frac{37}{2},\qquad
 q=x+m=\frac{49}{2},\qquad
 \mu=q+\alpha=\frac{127}{5}.
 \tag{3.2}
\]

Consider the rational interval

\[
 I=\left[\frac{33913}{50000},\frac{16957}{25000}\right]
 =[0.67826,0.67828].
 \tag{3.3}
\]

On this cell define the exact derivative

\[
 D(t)=
 \frac{p^2(3r+2p)}{3\pi\mu}\sin t
 -\frac m\pi-\frac{B\pi}{2t^2}
 +\frac{4u(t)\mu\tan^2t}{\pi},
 \qquad
 u(t)=\frac{\mu(\tan t-t)}{\pi}-B.
 \tag{3.4}
\]

Directed Arb arithmetic gives

\[
 D(0.67826)<-10^{-3},
 \qquad
 D(0.67828)>10^{-3}.
 \tag{3.5}
\]

The audited Round 23 curvature formula gives \(D'=\mathcal C _8''>0\) on
the whole open quadratic cell.  Hence there is a unique
\(t_*\in I\) with \(D(t_*)=0\).

The same directed enclosures give, using the monotonicity in \(t\) proved in
Round 23,

\[
 0.031<u(t)<0.032<\frac1{\sqrt2}
 \quad (t\in I),
 \tag{3.6}
\]

and the following strict margins:

\[
\begin{aligned}
 A_{0.67826}(x)-\frac74&>0.008,\\
 \frac74-A_{0.67828}(x+1)&>0.0625,\\
 \frac{11}{4}-A_{0.67828}(r)&>\frac23,\\
 \frac{\mu^2}{\cos^2(0.67826)}
 -\frac{\pi^2}{(1-\cos(0.67826))^2}-2&>860.
\end{aligned}
\tag{3.7}
\]

Therefore \(t_*\) satisfies both full paired shelf integrals (1.2), the
strict start wall, the half-integer owner activity inequality, and the
literal delicate-cell conditions.  In particular
\(W+1/4\in(1,2)\), so the strict bracket is exactly \(B_0=1\).

It remains to check the coupled discrete owner rule.  On the whole interval
\(I\), directed evaluation of (2.5) gives

\[
 S_x(6)-S_x(5)<-0.0195,
 \qquad
 S_x(7)-S_x(6)>0.0495.
 \tag{3.8}
\]

The exact feasible \(p\)-set is a prefix containing \(6\), and \(S_x\) is
strictly convex.  Thus \(p=6\) is its unique discrete minimizer at \(t_*\).
The point is consequently in the full coupled projected shelf image, not
merely in the endpoint relaxation used for the earlier Round 25 obstruction.

## 4. The Round 25 scalar is negative on the exact image

Write the stationary identity as

\[
 \mathcal C _8=V-\frac p2,
\tag{4.1}
\]

where

\[
\begin{aligned}
 V={}&m\left(\frac12-\frac t\pi+\frac{\tan(t/2)}\pi\right)
 +B\left(\frac\pi{2t}-1+
 \frac{\pi\tan(t/2)}{2t^2}\right)\\
 &+2u^2-\tan(t/2)L-\frac18.
\end{aligned}
\tag{4.2}
\]

An interval evaluation of (4.2) over all \(t\in I\) gives

\[
 4.5432443286<V<4.5469281102<\frac{91}{20}.
 \tag{4.3}
\]

At the stationary point, (2.3) gives exactly

\[
 P=p^2(3r+2p)=1782.
 \tag{4.4}
\]

Let \(\psi(P)\) be the Round 25 positive root of
\(s^2(2s+3)=P\).  Since

\[
 \left(\frac{457}{50}\right)^2
 \left(2\frac{457}{50}+3\right)
 =\frac{27776917}{15625}<1782,
 \tag{4.5}
\]

monotonicity gives \(\psi(P)>457/50\).  The other Round 25 bound is

\[
 \mu-m-1=\frac{92}{5}>\frac{457}{50}.
\tag{4.6}
\]

Hence

\[
 p_{\max}=\min\{\mu-m-1,\psi(P)\}>\frac{457}{50}.
\]

Combining this with (4.3) proves

\[
 \boxed{
 \mathcal F=V-\frac{p_{\max}}2
 <\frac{91}{20}-\frac{457}{100}
 =-\frac1{50}<0.}
 \tag{4.7}
\]

On the other hand, the exact stationary value keeps \(p=6\), so (4.3)
also proves

\[
 \boxed{
 \mathcal C _8=V-3>\frac{77}{50}>0.}
 \tag{4.8}
\]

This isolates the failure precisely: replacing the exact discrete owner
\(p=6\) by \(p_{\max}>9.14\) loses more than \(1.57\), while the exact
stationary scalar has a large positive margin.

## 5. Certification ledger

The finite signs in (3.5)--(3.8) and the interval (4.3) were evaluated with
`python-flint 0.8.0`, Arb precision 512 bits, using the exact rational data
(3.1)--(3.3).  The ball used for (4.3) slightly contains the rational interval
\(I\).  Representative raw enclosures were

```text
D(lo)  = -0.0013354736210280584...
D(hi)  =  0.0012401500294162410...
u(lo)  =  0.031069488669877698...
u(hi)  =  0.031174484668307256...
A_lo(x)-7/4        = 0.008321216855233538...
7/4-A_hi(x+1)      = 0.062672348207851018...
11/4-A_hi(r)       = 0.679981553281645966...
activity gap at lo = 860.592123830610599...
S(6)-S(5) subset [-0.01974744655,-0.01958781065]
S(7)-S(6) subset [ 0.04956873327, 0.04978678086]
V(I) subset [4.54324432862,4.54692811012]
```

Every displayed conclusion uses only a substantially weaker rational margin.
No floating-point root value is used in the proof.

## 6. Loss ledger and next exact target

Lemma 2.1 discards no shelf, interface, parity, activity, or owner
information.  The obstruction (4.7) is caused solely by the Round 25
replacement

\[
 p\longmapsto p_{\max}.
\]

Therefore the exact stationary identity should now be attacked in the
lossless form

\[
 \boxed{
 \mathcal C _8=V(B,m,t,u)-\frac12p,\qquad
 p^2(3x-p)=P,}
 \tag{6.1}
\]

with \(q,\alpha,x\) fixed by (2.1), \(p\) the unique stationary integer from
(2.3), the full cumulative shelf inequalities (1.2), and the Round 24
discrete-owner condition (2.5).  A future sublevel argument may exploit that
the exact cubic and the discrete owner inequalities constrain the same
integer \(p\).  It must not return to \(p_{\max}\), the endpoint-only shelf
window, global \(\alpha\)-monotonicity, or bare lower-wall dominance.

Boundary and other payment cells retain the original \(\mathcal C _8\)
obligation.  If the lossless exact-\(p\) route does not close, the revised
strategy requires returning to \(\mathcal R_J\), the exact correlated scalar,
or the weighted aggregate rather than adding a ratio owner.
