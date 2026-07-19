# General dimension, Round 8F: signed prefix beyond the chord barrier

Date: 2026-07-18  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: analytic ratio certificate with directed interval replay  
Depends on: Rounds 7 and 8A--8E

Round 8E reached \(\rho=927/1000\), where the common chord coefficient
\[
 \beta=\frac{123}{1000}-c,\qquad
 c=\frac{\arccos\rho}{\pi},
\]
was still positive.  This round crosses the wall \(\beta=0\).  When
\(\beta<0\), the geometric upper bound \(M\leq\mu\), rather than the
lower bound \(M\geq\delta/c\), gives the favorable direction.  The
dimensionless ratio \(c\mu/W\) is smaller than \(21\) on the new band, so
the resulting negative prefix is absorbed by the same terminal
stratification.

On the small-\(\delta\) face, a sharper retained-range lower bound
improves the level distance from \(3y/c\) to \((149/50)y/c\).  Together
these two changes extend the certified ratio range to
\[
 \boxed{\rho\geq\frac{1847}{2000}=0.9235.}
\]

This is a ratio certificate, not a certificate of any remaining wall
below \(1847/2000\).

## 1. Result

### Theorem 1 (signed-prefix high-floor exclusion)

In the high-floor first-drop branch, suppose
\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{1847}{2000}\leq\rho<1.
\]
Then
\[
 \boxed{
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.}       \tag{1}
\]

Consequently every remaining negative high-floor first-drop candidate
satisfies
\[
 \boxed{
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228,}                         \tag{2}
\]
and
\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq3\,844\,455,\\
 2\leq n\leq1\,922\,227,\qquad
 1\leq p\leq n-1,\\
 2\leq f\leq640\,742,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq640\,742.
 \end{gathered}}                                      \tag{3}
\]

The exact chamber conditions remain
\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,\qquad
 K-\mu>\frac{7\pi}{4},                               \tag{4}
\]
\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.                                 \tag{5}
\]

No conclusion is inferred merely from the finiteness of (2)--(3).

## 2. Inherited cap and the common pre-substitution prefix

The case \(p=0\) is automatic:
\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0.
\]
Hence a negative candidate has \(p\geq1\), \(n\geq2\), and
\[
 q=r+n\geq\frac52.
\]
Round 8E therefore gives the wall-safe cap
\[
 \boxed{2\int_q^\mu G_\mu(z)\,dz<\frac16.}           \tag{6}
\]

Retain the notation
\[
 d=1-2c,\qquad W=G_K(\mu),\qquad
 h=f-\frac14,\qquad \delta=h-W,
\]
and
\[
 P=R_p+\frac d2(n-p).
\]

For \(\delta\geq1\), the refined absent-level chord from Round 8E gives
\[
 P>\left(\frac d2-\frac{377}{1000}\right)M-\frac d2
   =\beta M-\frac d2,                                \tag{7}
\]
when level \(f\) is absent.  If the level is present, its stronger
coefficient gives
\[
 P\geq\left(\frac18-c\right)M-\frac d2
 >\beta M-\frac d2.                                  \tag{8}
\]
Thus (7) is a common estimate before either bound on \(M\) is
substituted.

## 3. Crossing the sign wall

Round 8E owns \(\rho\geq927/1000\), so it remains to treat
\[
 \frac{1847}{2000}\leq\rho\leq\frac{927}{1000}.
\]
Directed endpoint evaluation gives
\[
 (\arccos\rho)^2<\frac{311}{2000}<\frac4{25},
 \qquad
 c<\bar c:=\frac{627}{5000}.                         \tag{9}
\]
In particular \(\arccos\rho<2/5\).

Put \(\epsilon=1-\rho\) and
\[
 \lambda_\rho=\frac{\pi G_1(\rho)}{1-\rho}.
\]
On the present band \(\epsilon\geq73/1000\), and
\[
 \frac89\frac{73}{1000}-\left(\frac14\right)^2
 =\frac{43}{18000}>0.
\]
The active-width estimate therefore gives
\[
 \lambda_\rho>\frac14,\qquad
 \boxed{W>\frac7{16}.}                               \tag{10}
\]

The same quantities control the upper endpoint \(M\leq\mu\).  Indeed,
with \(\theta=\arccos\rho\),
\[
 \frac{c\mu}{W}
 =\frac{c\rho K}{K G_1(\rho)}
 =\frac{\theta\rho}{\lambda_\rho\epsilon}
 <\frac{(2/5)(927/1000)}
 {(1/4)(73/1000)}
 =\frac{7416}{365}<21.                               \tag{11}
\]

If \(\beta\geq0\), then \(M\geq\delta/c\), and (7)--(8) give
\[
 \boxed{cP>\beta\delta-\frac{cd}{2}.}                \tag{12}
\]
If \(\beta<0\), use \(M\leq\mu\).  Equations (7)--(8) and (11) give,
with the inequality direction reversed by the negative coefficient,
\[
 cP>\beta c\mu-\frac{cd}{2}
 >\boxed{21\beta W-\frac{cd}{2}.}                    \tag{13}
\]
This is the signed-prefix replacement for (12).

## 4. The faces \(\delta\geq1\)

Use
\[
 B_0=\left[W+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.
\]
As before,
\[
 B\geq B_0,\qquad Q\leq B_0+1.                      \tag{14}
\]

### 4.1. The region \(\beta\geq0\)

Here \(c\leq123/1000\), and (12) applies.  The exact-angle reserve and
(6) give
\[
 cD_A(q)>
 B_0\left(\frac12-c\right)-\frac{7c}{6}
\]
when \(B_0\geq1\).  At the limiting endpoint \(\beta=0\),
\(c=123/1000\), this and the other two terminal strata give the exact
lower ledgers
\[
 \boxed{
 B_0\geq1:\quad c\mathcal S>
 \frac{187129}{1000000},}                            \tag{15}
\]
\[
 \boxed{
 B_0=Q=0:\quad c\mathcal S>
 \frac{580141}{4000000},}                            \tag{16}
\]
\[
 \boxed{
 B_0=0,\ Q=1:\quad c\mathcal S>
 \min\left\{\frac{393129}{1000000},\frac{189}{500}\right\}.}
                                                               \tag{17}
\]
For (16), the outer tangent triangle gives \(cD_A(q)\geq W^2\), and
the expression increases in \(W\geq7/16\).  For (17), the expression
is concave in \(W\in(3/4-c,3/4]\), so the displayed values are its two
endpoint ledgers.  All four expressions decrease up to
\(c=123/1000\).

### 4.2. The region \(\beta<0\)

Now (13) applies.  If \(B_0\geq1\), strict bracketing gives
\[
 W\leq B_0+\frac34.
\]
Since \(21\beta<0\),
\[
 21\beta W\geq21\beta\left(B_0+\frac34\right).
\]
The coefficient of \(B_0\) in the resulting terminal ledger is
\[
 \frac12-c+21\beta
 \geq\frac{1621}{5000}>0.                            \tag{18}
\]
Thus \(B_0=1\) is the lower endpoint.  At \(c=\bar c\),
\[
 \boxed{
 B_0\geq1:\quad c\mathcal S>
 \frac{2328129}{25000000}>0.}                       \tag{19}
\]

If \(B_0=Q=0\), then
\[
 c\mathcal S>
 W^2+21\beta W-\frac{cd}{2}.                        \tag{20}
\]
Its derivative in \(W\geq7/16\) is bounded below at the endpoint by
\[
 2\frac7{16}+21\left(-\frac3{1250}\right)
 =\frac{4123}{5000}>0.
\]
The expression decreases in \(c\), so
\[
 \boxed{
 B_0=Q=0:\quad c\mathcal S>
 \frac{12238141}{100000000}>0.}                     \tag{21}
\]

Finally, if \(B_0=0,Q=1\), then
\[
 \frac34-c<W\leq\frac34,\qquad
 cD_A(q)>\frac32W-W^2-c.
\]
After adding (13), the expression remains concave in \(W\).  Its two
endpoint polynomials decrease in \(c\), and at \(c=\bar c\) give
\[
 \boxed{
 W=\frac34:\quad
 c\mathcal S>
 \frac{9999}{4000}-\frac{69}{4}c+c^2
 \geq\frac{8808129}{25000000}>0,}                   \tag{22}
\]
\[
 \boxed{
 W=\frac34-c:\quad
 c\mathcal S>
 \frac{9999}{4000}-\frac{19833}{1000}c+21c^2
 \geq\frac{2143251}{6250000}>0.}                    \tag{23}
\]
Equations (15)--(17) and (19)--(23) close every
\(\delta\geq1\) face on the new band.

## 5. Improving the small-\(\delta\) level distance

Suppose \(0<\delta<1\).  Put
\[
 y=f-W=\delta+\frac14,\qquad
 L=\frac{149}{50}.
\]
The scale and concavity reductions from Round 8E again reduce
\[
 \boxed{T<\frac{Ly}{c}}                              \tag{24}
\]
to \(f=2\) and
\[
 x=\frac yW\in\left\{\frac17,\frac53\right\}.
\]

Let
\[
 \Phi=\sin\theta-\theta\cos\theta,\qquad
 t_0=\frac{Ly}{c},\qquad u_0=\frac{t_0}{\mu}.
\]
The upper bounds \(\Phi<\theta^3/3\) and (9) give
\[
 u_0<
 \frac{149}{50}\frac59
 \frac{311/2000}{1847/2000}
 =\frac{46339}{166230}<\frac{279}{1000}<1.          \tag{25}
\]

For the retained lower range, define
\[
 \kappa_\rho=\frac{\Phi}{\theta\rho(1-\rho)}.
\]
The alternating Taylor bounds give
\[
 \Phi>\theta^3\left(\frac13-\frac{\theta^2}{30}\right),
\]
\[
 1-\cos\theta<
 \theta^2\left(\frac12-\frac{\theta^2}{24}
 +\frac{\theta^4}{720}\right).
\]
The quotient
\[
 t\longmapsto
 \frac{1/3-t/30}
 {(927/1000)(1/2-t/24+t^2/720)}
\]
is decreasing on the present interval; its derivative has the sign of
\[
 t^2-20t-60<0.
\]
At \(t=311/2000\), its exact value and gap are
\[
 \frac{105008000000}{146407982263}
 -\frac7{10}
 =\frac{25224124159}{1464079822630}>0.
\]
Hence
\[
 \boxed{\kappa_\rho>\frac7{10}},\qquad
 \frac{u_0}{1-\rho}>
 \frac{149}{50}\frac7{10}x
 =\frac{1043}{500}x.                                \tag{26}
\]

Use
\[
 \arccos(1-z)=\sqrt{2z}\,S(z).
\]
On the retained subtracted range,
\[
 V=\frac{1043}{500}x\leq\frac{1043}{300},
\qquad
 z\leq\frac{153}{2000}\frac{1043}{300}
 =\frac{53193}{200000}.
\]
The decreasing positive coefficients of \(S\) give
\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{3750z^2}{146807}.              \tag{27}
\]
The integrated upper coefficient is
\[
 \frac{3750}{146807}\frac27
 =\frac{7500}{1027649},
\]
and the positive first-copy argument is at most
\[
 \frac{68493}{200000}<1.
\]

The decreasing coefficient quotient used in Round 8E, evaluated at
\(\rho=1847/2000\) and \(\theta^2=311/2000\), gives
\[
 \boxed{
 C_\rho=
 \frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}>
 \frac{689}{500}.}                                  \tag{28}
\]
The resulting retained lower integral is
\[
\begin{aligned}
 \mathcal I^{\mathrm F}_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)
 +\frac{1-\rho}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3(1-\rho)^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)
 -\frac23V^{3/2}-\frac{1-\rho}{30}V^{5/2}\\
&-\frac{7500(1-\rho)^2}{1027649}V^{7/2}.
                                                               \tag{29}
\end{aligned}
\]

Divide \([1847/2000,927/1000]\) into \(64\) equal rational panels.
Directed Arb evaluation on each full panel at both endpoint values of
\(x\), with \(V=(1043/500)x\), proves
\[
 \mathcal I^{\mathrm F}_\rho(V)>0,\qquad
 \frac{689}{500}\mathcal I^{\mathrm F}_\rho(V)-x>0.  \tag{30}
\]
Across \(384,512,768,\) and \(1024\) bits, the smallest lower bounds
are
\[
 \mathcal I^{\mathrm F}_\rho(V)>0.2113764065,
\]
\[
 \frac{689}{500}\mathcal I^{\mathrm F}_\rho(V)-x
 >0.0357944486.                                     \tag{31}
\]
Concavity proves (24) throughout the interval of \(x\).

## 6. Completing \(0<\delta<1\)

The endpoint chord, \(M\geq\delta/c\), and (24) give
\[
\begin{aligned}
 cP
 &>-\frac L4\left(\delta+\frac14\right)
   +\left(\frac34-c\right)\delta-\frac{cd}{2}\\
 &=\left(\frac{3-L}{4}-c\right)\delta
   -\frac L{16}-\frac{cd}{2}.
\end{aligned}
\]
Since \((3-L)/4-c<0\) and \(\delta<1\),
\[
 cP>
 \frac{3-L}{4}-c-\frac L{16}-\frac{cd}{2}.          \tag{32}
\]

Here \(B_0=f-1\), \(Q\leq f-1\), and the cap (6) gives
\[
 cD_A(q)>
 \frac{f-1}{2}-c(f-1)-\frac c6
 \geq\frac12-\frac{7c}{6}.                          \tag{33}
\]
Adding (32)--(33), using \(d=1-2c\) and \(L=149/50\), yields
\[
 c\mathcal S>
 \frac54-\frac{5L}{16}-\frac83c+c^2
 =\frac{51}{160}-\frac83c+c^2.
\]
This decreases on the certified interval.  At \(c=\bar c\),
\[
 \boxed{c\mathcal S>\frac{1879}{25000000}>0.}        \tag{34}
\]
Together with Section 4 and Round 8E above \(927/1000\), this proves
(1).

## 7. Improved residual cutoff

For a residual ratio \(\rho<1847/2000\), put
\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.
\]
Directed endpoint evaluation and monotonicity give
\[
 \eta_\rho>\frac1{158},\qquad \eta_\rho<\frac19.    \tag{35}
\]
Also
\[
 a_\rho<
 2\frac{355}{113}\frac{1847}{153}
 =\frac{1311370}{17289}.                            \tag{36}
\]
Since \(C_*<13/10\),
\[
 a_\rho+2\eta_\rho C_*
 <\frac{1311370}{17289}+\frac{13}{45}
 =\frac{2193941}{28815}<77.                         \tag{37}
\]
As \(C_*>1/2\), the square root in the fixed-ratio threshold is smaller
than the same left side.  Hence
\[
 \boxed{
 K_0(\rho)<77\cdot158^2=1\,922\,228.}               \tag{38}
\]

Negativity excludes \(p=0\), so \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\).  Since \(r\geq1/2\), (38) gives
\[
 \rho>\frac1{3\,844\,456},\qquad
 2r\leq3\,844\,455,\qquad
 n\leq1\,922\,227.
\]
Finally \(A(r)\geq7/4\) gives \(K-\mu>7\pi/4\) and \(K>21/4\), while
\(\pi>3\) gives
\[
 f,B<\frac K3+\frac14<640\,742+\frac{11}{12}.
\]
These are exactly (2)--(5).

## 8. Reproducibility and remaining obligation

The directed verifier is

    scripts/general_d_high_floor_signed_prefix_verify.py

It checks the frozen Round 8E verifier hash, the inherited
\(G_{7/2}(5/2)<1/6\) cap, the ratio endpoint, the active-width and
\(c\mu/W\) bounds, both signs of \(\beta\), all eight
\(\delta\geq1\) endpoint ledgers, the improved retained-range quotient,
all \(128\) full-panel endpoint evaluations, the small-\(\delta\)
polynomial, the fixed-ratio cutoff, and the exact integer ranges.

The remaining high-floor compact region is now
\[
 \boxed{
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228.}
\]
No wall in this residual box is claimed certified by this round.
