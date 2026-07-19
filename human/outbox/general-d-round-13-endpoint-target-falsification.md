# General dimension, Round 13: falsification of the alpha-endpoint sign target

Date: 18 July 2026

Status: the monotone alpha-endpoint reduction of Round 12 remains valid, but
its proposed endpoint sign target (3.11) is false.  The counterexample below
is an exact integer-grid, open, hard, first-floor no-drop tail.  It also makes
the Round 11 sufficient scalar (4.5) negative.  The exact defect is strongly
positive, so this rejects only the coarse pre-shelf surrogate, not the
first-floor theorem or the shell inequality.

## 1. Exact construction and gate decision

Put

\[
 \theta=\frac{8899}{100000},\qquad
 \Phi(\theta)=\sin\theta-\theta\cos\theta,
 \qquad K=\frac{3\pi}{4\Phi(\theta)},
\]

\[
 q=9998,\qquad n=50,\qquad r=9948,
 \qquad \alpha=\frac{999}{1000},\qquad
 \mu=q+\alpha.
 \tag{1.1}
\]

Let

\[
 z=K\cos\theta,\qquad y=z-q,\qquad \eta=y.
\]

Then \(G_K(z)=3/4\) by construction.  The exact-rational enclosure in
Section 2 gives

\[
 10038<K<10039,qquad
 9998.407<z<9998.408,qquad
 0.407<y=\eta<0.408.
 \tag{1.2}
\]

This is the integer extension grid owned in dimension \(4\).  All original
branch conditions hold, but

\[
 \boxed{\widehat\Psi_1<-\frac32<0.}
 \tag{1.3}
\]

At the Round 12 endpoint \(\bar\alpha=1\), the same scalar is also negative.
Therefore the gate decision is:

1. **PASS:** Round 12 Proposition 1.1 and its monotone implication (3.6);
2. **REJECT:** the universal endpoint sign target (3.11);
3. **REJECT:** any attempt to close the branch by proving the Round 11
   surrogate (4.5) universally on the extension grids.

## 2. Analytic certificate

The following certificate uses only rational arithmetic and alternating
Taylor bounds.  Take the classical rational enclosure

\[
 \frac{103993}{33102}<\pi<\frac{104348}{33215}.
\]

For \(0<\theta<1\), alternation gives

\[
 \frac{\theta^3}{3}-\frac{\theta^5}{30}
 +\frac{\theta^7}{840}-\frac{\theta^9}{45360}
 <\Phi(\theta)
 <\text{the left side}+\frac{\theta^{11}}{3991680},
\]

and

\[
 1-\frac{\theta^2}{2}+\frac{\theta^4}{24}
 -\frac{\theta^6}{720}
 <\cos\theta
 <\text{the left side}+\frac{\theta^8}{40320}.
\]

Substitution proves (1.2) by exact cross multiplication.

Write \(w=v-3/4=G_K(q)-G_K(z)\).  Since
\(-G_K'(s)=\arccos(s/K)/\pi\),

\[
 \frac{y\theta}{\pi}\le w\le y\beta,
 \qquad \beta=\frac{\arccos(q/K)}\pi.
\]

The rational bounds above, together with
\(\arctan u=u-u^3/3+u^5/5-\cdots\), give

\[
 0.011<w<0.012,qquad \beta<0.029.
 \tag{2.1}
\]

The radius-average representation gives

\[
 G_{q+1}(q)
 \le \frac{2}{3\pi}\sqrt{\frac2q}
 <0.0031.
 \tag{2.2}
\]

Thus \(h(\alpha)<G_{q+1}(q)<w\), and hence

\[
 0.007<\varepsilon=v-h(\alpha)-\frac34<0.012<\frac14.
\]

Consequently \(B=Q=1\), \(\chi_q=0\), and \(v<1\), so the top square
vanishes.  Moreover (2.2) shows that the phase wall occurs after
\(\alpha=1\).  From (1.2),

\[
 \alpha_{\rm act}
 =K-q-\frac{\pi K}{\sqrt{K^2-3/4}}>1,
\]

so \(\bar\alpha=1\), while the point \(\alpha=999/1000\) is strictly
dimension-active.

It remains to verify the complete first shelf.  Put \(\sigma=-A'\).  The
same rational arctangent calculation gives

\[
 \sigma(r)<0.012,\qquad \sigma(q)<0.025.
\]

Since \(\sigma\) is convex, its integral lies below its endpoint
trapezoid:

\[
 \Delta=\int_r^q\sigma(s)\,ds
 \le\frac n2\bigl(\sigma(r)+\sigma(q)\bigr)<0.925.
\]

Together with \(3/4<A(q)<0.762\), this yields

\[
 \frac34<A(r+j)<\frac74\qquad(0\le j\le50).
\]

Therefore every ordinary first-shelf floor is exactly \(F_j=1\).

Finally,

\[
 C_{9948,50}=\frac{2339375}{4697283}<\frac12,
 \qquad \lambda<\frac{51}{4},
\]

while

\[
 0<L^{\rm op}(\alpha)
 <\frac{35}{2}.
\]

Hence the maximum in the scalar equals \(L^{\rm op}\), and

\[
 \widehat\Psi_1
 <\frac{35}{2}-25
 +\frac12\left(\frac{51}{4}-\frac34\right)
 =-\frac32.
\]

This proves (1.3) without numerical search.  The focused exact-rational and
100-digit replay is
`computations/general_d_round13_endpoint_counterexample.wl`.

## 3. High-precision replay and exact identity

At the actual open point \(\alpha=999/1000\), the replay gives

\[
\begin{aligned}
 K&=10038.1281741679491984653061207\ldots,\\
 y&=0.4073245282231106880415255\ldots,\\
 \varepsilon&=0.00857086626411767614465889\ldots,\\
 \lambda&=12.4552029758656314143286153\ldots,\\
 \widehat L_1&=17.4630355657041954076786716\ldots,\\
 \mathcal R_0&=-19.1704897891684061850446302\ldots,\\
 \widehat\Psi_1&=-1.70745422346421077736595859\ldots.
\end{aligned}
\]

The 51 sampled actions range from

\[
 0.7585708662641176761\ldots
 \quad\text{to}\quad
 1.4707676500456716710\ldots,
\]

and every ordinary floor is \(1\).  At the endpoint \(\alpha=1\),

\[
 \Psi_{\rm end}=-1.70762024775344877008553861\ldots.
\]

The exact cap and head ledger at the actual point is

\[
\begin{aligned}
 \delta&=0.00119748715935190061890845\ldots,\\
 2\delta&=0.00239497431870380123781690\ldots,\\
 \alpha h&=0.00299372217136206494693138\ldots,\\
 I=2\int_0^n u\sigma(r+u)\,du
 &=39.9487276527016745996221545\ldots,\\
 R_n&=15.8058142791134422140880431\ldots.
\end{aligned}
\]

Thus restoring only the exact head already gives

\[
 \widehat L_1+R_n
 =33.2688498448176376217667146\ldots>0.
\]

Direct evaluation gives

\[
 D_A(q)=23.4444610701803942773291434\ldots,
\]

\[
 \boxed{D_A(r)=39.2502753492938364914171865\ldots>0,}
\]

and

\[
 D_A(r)-D_A(q)-R_n-\chi_q=0
\]

to more than 80 displayed working digits.

## 4. Equality faces, dependencies, and loss ledger

This point is strictly inside every relevant face: \(0<\alpha<1\),
\(0<\varepsilon<1/4\), \(0<\eta<1\), \(B=Q=1\), and
\(\chi_q=0\).  No strict-bracket or ordinary-floor wall is approached.
The endpoint \(\alpha=1\) is used only as the Round 12 limiting comparison.

The only dependencies are the definitions and exact no-drop identity (S4),
the Round 11 scalar, the Round 12 monotonicity reduction, and the elementary
convexity and alternating-series estimates displayed above.  No search or
floating-point sign is a proof premise.

The failure is overwhelmingly the pre-shelf/head relaxation:

\[
 R_n=15.8058142791\ldots,
 \qquad \mathcal R_0=-19.1704897892\ldots.
\]

The cap relaxation loses only

\[
 \alpha h-2\delta=0.0005987478526582637\ldots.
\]

The endpoint movement itself changes the negative scalar by only about
\(1.66\times10^{-4}\).  It is therefore not the cause of failure.

## 5. Failure report and required pivot

The deterministic Round 12 replay stopped before this long, high-\(q\)
regime and cannot support a universal sign conjecture.  The next round must
not introduce another ratio partition or another coarser surrogate.  It
must retain the exact correlated head remainder in (S4), or move to the
weighted aggregate \(\mathcal B_d(A)\).  The exact-head scalar has more than
33 units of margin at this counterexample, while the true defect has more
than 39 units.
