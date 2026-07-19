# General dimension, Round 26: exact stationary-image counterexample to the Round 25 scalar F

Date: 19 July 2026  
Status: certified counterexample to \(\mathcal F\geq0\) on the exact image; the C8 sign remains open

## 0. Scope and theorem boundary

Round 25 proved, at every interior stationary point on the delicate cell,

\[
 \mathcal C _8\geq\mathcal F.
\]

It proposed proving \(\mathcal F\geq0\) on the full projection of the exact
shelf domain. This note shows that proposed sufficient scalar is false even
on the exact projected stationary image. The counterexample satisfies the
complete paired shelf inequalities, the strict start wall, the interface
identity, owner activity, the open quadratic action cell, and the exact
stationarity equation.

This is **not** a counterexample to \(\mathcal C_8\geq0\). At the certified
point, \(\mathcal C_8>1\). It therefore does not falsify CST-H or the
general-dimensional Polya theorem. It only proves that the Round 25
\(p_{\max}\)-relaxation is too lossy to serve as the next scalar target.

## 1. Exact domain reconstructed

Retain the Round 24 notation

\[
 x=r+p,\qquad q=r+p+m,\qquad \mu=q+\alpha,\qquad
 h=B+\frac34,
\]

\[
 A_t(s)=G_{\mu/\cos t}(s)-G_\mu(s),\qquad
 W={\mu\over\pi}(\tan t-t),\qquad u=W-B.
\]

On the delicate \(B=f-1\) cell, the exact domain is

\[
 B\in\mathbb N,\qquad 0<u<{1\over\sqrt2},\qquad
 0\leq\alpha<1,
\]

\[
 h\leq A_t(x),\qquad A_t(x+1)<h,\qquad A_t(r)<h+1,       \tag{1.1}
\]

together with the appropriate strict owner-activity inequality. The
stationary equation is

\[
 D(t):={p^2(3r+2p)\sin t\over3\pi\mu}
 -{m\over\pi}-{B\pi\over2t^2}
 +{4u\mu\tan^2t\over\pi}=0.                              \tag{1.2}
\]

The paired integral relations used in Round 25 are exactly

\[
 A_t(x)-W=\int_x^\mu\sigma(s)\,ds\geq\delta,
\]

\[
 A_t(x+1)-W=\int_{x+1}^\mu\sigma(s)\,ds<\delta,
 \qquad \delta={3\over4}-u.                              \tag{1.3}
\]

Indeed, subtracting \(W+\delta=B+3/4=h\) shows that the two
full-integral margins are precisely

\[
 A_t(x)-h,\qquad h-A_t(x+1).                              \tag{1.4}
\]

Thus certifying (1.1) certifies the full paired integrals, not merely the
endpoint \(m\)-window derived from them.

## 2. Certified exact-image witness

Take the exact data

\[
 \boxed{
 (r,p,m,B,f,\alpha,\mu)
 =\left(12,4,5,1,2,{1\over2},{43\over2}\right).}          \tag{2.1}
\]

This is the integer owner grid, with \(x=16\), \(q=21\), and
\(h=7/4\). Directed-rounding Arb arithmetic certifies a unique stationary
root in the rational interval

\[
 \boxed{
 {7257007\over10^7}<t<{7257008\over10^7}.}                \tag{2.2}
\]

At the two exact endpoints of this interval,

\[
 D(7257007/10^7)<-1.18\times10^{-6},
\]

\[
 D(7257008/10^7)>1.24\times10^{-5}.                       \tag{2.3}
\]

Throughout the interval,

\[
 D'(t)>136.03.                                             \tag{2.4}
\]

Continuity, (2.3), and (2.4) prove existence and uniqueness of the exact
stationary root.

The same interval evaluation gives

\[
 u=0.10528\ldots,
\]

and the following certified positive margins on the entire root interval:

\[
\begin{array}{c|c}
\text{condition}&\text{certified margin}\\ \hline
A_t(16)-7/4&>0.01102\\
7/4-A_t(17)&>0.07286\\
11/4-A_t(12)&>0.73184\\
\text{integer-owner activity}&>669.89
\end{array}                                                \tag{2.5}
\]

Also \(0<u<1/\sqrt2\), \(0<\lambda=3/4-u<1\), and

\[
 1<W+\frac14<2.
\]

Therefore the literal bracket is \(B_0=1\), the quadratic payment is
exactly \(2u^2\), and no action or floor wall is being approximated. Since
\(17<\mu<\mu/\cos t\), no outer turning equality is present.

Equations (1.3)--(1.4) and the first two rows of (2.5) prove explicitly
that this point lies in the full paired-integral shelf image. The third row
supplies the strict start condition that is not visible in those two
integrals.

## 3. The exact failure mechanism

At a stationary point, Round 25 gives

\[
 P=p^2(3r+2p).
\]

For (2.1), this value is exactly

\[
 P=4^2(3\cdot12+2\cdot4)=704.                             \tag{3.1}
\]

Let \(\psi^2(2\psi+3)=704\). Exact rational substitution shows

\[
 {659\over100}<\psi<{33\over5}.                           \tag{3.2}
\]

The other Round 25 upper bound is

\[
 \mu-m-1=15>{33\over5},
\]

so \(p_{\max}=\psi\). Hence

\[
 1.295<{p_{\max}-p\over2}<1.3.                            \tag{3.3}
\]

The exact stationary identity immediately relates the two scalars:

\[
 \boxed{
 \mathcal F=\mathcal C _8-{p_{\max}-p\over2}.}             \tag{3.4}
\]

Directed-rounding evaluation on the whole root interval certifies

\[
 \boxed{
 \mathcal F<-{1\over100},\qquad \mathcal C _8>1.}          \tag{3.5}
\]

Numerically, only for orientation,

\[
 t\approx0.725700708747,\qquad
 \mathcal F\approx-0.0151228915,\qquad
 \mathcal C _8\approx1.2820971435.                        \tag{3.6}
\]

Thus the paired full integrals do not rescue the statement
\(\mathcal F\geq0\): the exact image itself contains a negative value. The
failure is exactly the continuous owner loss (3.3), not a shelf relaxation,
an endpoint convention, or a numerical near-wall effect.

## 4. Reproducible diagnostic and adversarial sweep

Certified artifact:

`computations/general_d_round26_c8_exact_stationary_image_counterexample.py`

Run only the interval certificate with

```text
python -B computations/general_d_round26_c8_exact_stationary_image_counterexample.py
```

The replay passes at 256, 512, and 768 Arb bits. Every transcendental sign
in (2.2)--(3.5) uses directed rounding.

The same artifact contains a separately labelled, non-certified search:

```text
python -B computations/general_d_round26_c8_exact_stationary_image_counterexample.py --scan --limit 16
```

For \(B=1\), both owner grids through \(r=16.5\),
\(1\leq p\leq6\), \(1\leq m\leq7\), and
\(\alpha\in\{0,1/2,0.9,0.99\}\), it retained 588 actual feasible
stationary roots. Sixty-seven had \(\mathcal F<0\). The smallest sampled
value was

\[
 \mathcal F\approx-0.2570894
\]

at

\[
 (r,p,m,B,\alpha)=(16.5,6,6,1,0.99),
\]

while its direct scalar remained positive,

\[
 \mathcal C _8\approx1.67693.
\]

The sweep is theorem-design evidence only. The exact witness (2.1), not the
sweep, proves the counterexample.

## 5. Consequence for the analytic workflow

The Round 25 implication \(\mathcal C_8\geq\mathcal F\) remains correct,
but its proposed sign target is rejected:

\[
 \boxed{
 \mathcal F\geq0\text{ on the full projected stationary shelf image is
 false}.}
\]

No inequality extracted from the full paired shelf integrals can prove that
false statement. A subsequent C8 argument must instead retain enough owner
information to recover the reserve

\[
 {p_{\max}-p\over2},
\]

or avoid the \(p_{\max}\) substitution entirely. The exact stationary
identity from Round 25 remains useful in the owner-dependent form with
\(-p/2\). The strategy-approved alternative is the weighted aggregate
theorem if that exact-owner route does not close; another continuous ratio
partition is not indicated.

The exact C8 sign and the general theorem remain open.
