# General dimension, Round 8G: the exact correlated prefix

Date: 2026-07-18  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: provisional analytic ratio certificate with directed interval replay  
Depends on: Rounds 7 and 8A--8F

Round 8F bounded the signed-prefix factor \(c\mu/W\) by the constant
\(21\).  That decoupling becomes too expensive below
\(\rho=1847/2000\).  This round instead keeps the exact correlated factor

\[
 R_\rho=\frac{c\mu}{W}
 =\frac{\theta\rho}{\sin\theta-\theta\cos\theta},
 \qquad \theta=\arccos\rho.
\]

It also improves the small-\(\delta\) level distance to
\(T<(29/10)y/c\).  Together these changes give the provisional extension

\[
 \boxed{\rho\geq\frac{23}{25}=0.92.}
\]

This is only a ratio certificate.  It does not certify any remaining
fixed-ratio wall below \(23/25\).

## 1. Result

### Theorem 1 (correlated-prefix high-floor exclusion)

In the high-floor first-drop branch, suppose

\[
 f=F_0\geq2,\qquad p<n,\qquad \frac{23}{25}\leq\rho<1.
\]

Then

\[
 \boxed{\mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.}       \tag{1}
\]

Consequently every remaining negative high-floor first-drop candidate
satisfies

\[
 \boxed{
 \frac1{3\,154\,914}<\rho<\frac{23}{25},\qquad
 \frac{21}{4}<K<1\,577\,457,}                              \tag{2}
\]

and

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq3\,154\,913,\\
 2\leq n\leq1\,577\,456,\qquad
 1\leq p\leq n-1,\\
 2\leq f\leq525\,819,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq525\,819.
 \end{gathered}}                                           \tag{3}
\]

The exact chamber conditions remain

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,\qquad
 K-\mu>\frac{7\pi}{4},                                    \tag{4}
\]

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.                                      \tag{5}
\]

No closure is inferred merely from the finiteness of (2)--(3).

## 2. Inherited cap and common prefix

If \(p=0\), then \(R_0=0\), and the completed one-interface theorem gives

\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0.
\]

Thus a negative candidate has \(p\geq1\), \(n\geq2\), and
\(q=r+n\geq5/2\).  Strict convexity of \(G_\mu\), the chamber
\(q\leq\mu<q+1\), and monotonicity of \(G_{q+1}(q)\) give the inherited
strict cap

\[
 \boxed{2\int_q^\mu G_\mu(z)\,dz< G_{7/2}(5/2)<\frac16.}   \tag{6}
\]

Retain

\[
 c=\frac\theta\pi,\qquad d=1-2c,\qquad
 W=G_K(\mu),\qquad h=f-\frac14,\qquad \delta=h-W,
\]

and put

\[
 P=R_p+\frac d2(n-p),\qquad
 \beta=\frac{123}{1000}-c.
\]

For \(\delta\geq1\), the refined absent-level chord from Round 8E gives

\[
 P>\beta M-\frac d2.                                     \tag{7}
\]

On the present-level face,

\[
 P\geq\left(\frac18-c\right)M-\frac d2
 >\beta M-\frac d2,                                      \tag{8}
\]

because the coefficient gap is \(1/500\) and \(M>0\).  Thus (7) is a
strict common pre-substitution prefix on both faces.

## 3. The exact correlated negative prefix

Round 8F owns \(\rho\geq1847/2000\), so it remains to prove (1) on

\[
 \frac{23}{25}\leq\rho\leq\frac{1847}{2000}.             \tag{9}
\]

Directed endpoint evaluation gives

\[
 \theta^2<\frac{163}{1000},\qquad
 c<\bar c:=\frac{641}{5000}.                              \tag{10}
\]

At the upper ratio endpoint \(c>123/1000\), and \(c\) increases as
\(\rho\) decreases.  Hence \(\beta<0\) throughout (9).

Write

\[
 \Phi=\sin\theta-\theta\cos\theta,\qquad
 R_\rho=\frac{\theta\rho}{\Phi},\qquad
 \gamma(\theta)=\beta R_\rho.                            \tag{11}
\]

Since \(M\leq\mu\), the negative sign reverses the substitution in (7):

\[
 cP>\beta c\mu-\frac{cd}{2}
 =\boxed{\gamma(\theta)W-\frac{cd}{2}.}                  \tag{12}
\]

This keeps the exact correlation that was discarded in Round 8F.

For

\[
 R(\theta)=\frac{\theta\cos\theta}{\Phi},
\]

direct differentiation gives

\[
 R'(\theta)=
 \frac{\sin\theta\cos\theta-\theta}{\Phi^2}<0,          \tag{13}
\]

and therefore

\[
 \gamma'(\theta)=-\frac{R(\theta)}\pi
 +\left(\frac{123}{1000}-\frac\theta\pi\right)R'(\theta).
                                                                    \tag{14}
\]

On 64 complete rational \(\rho\)-panels, directed Arb arithmetic proves

\[
 \boxed{\gamma'(\theta)<-\frac{49}{10}<0.}               \tag{15}
\]

Across all four replay precisions, the union of the directed enclosures
was

\[
 -5.595800902<\gamma'(\theta)<-4.986279971.
\]

Thus \(\gamma\) decreases with \(\theta\), and its minimum is at
\(\rho=23/25\).  Directed endpoint evaluation gives

\[
 \gamma(\arccos(23/25))
 =-0.0897444733642\ldots> -\frac9{100}.                   \tag{16}
\]

Consequently

\[
 \boxed{-\frac9{100}<\gamma<0.}                          \tag{17}
\]

on the full band.

## 4. Active width and every \(\delta\geq1\) terminal stratum

The exact active-width factor is

\[
 \lambda(\theta)=\frac{\Phi}{1-\cos\theta}.
\]

Its derivative is

\[
 \lambda'(\theta)=
 \frac{\sin\theta\,(\theta-\sin\theta)}{(1-\cos\theta)^2}>0.
\]

The minimum is therefore the upper endpoint of (9), where directed
evaluation gives

\[
 \lambda>\frac{229}{875}.
\]

Since \(W>\lambda(W+\delta)\) and
\(W+\delta=f-1/4\geq7/4\),

\[
 \boxed{W>\frac{229}{500}.}                              \tag{18}
\]

Use the strict terminal counts

\[
 B_0=\left[W+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.
\]

As before, \(B\geq B_0\) and \(Q\leq B_0+1\).  Thus the following three
strata are exhaustive.

### 4.1. The stratum \(B_0\geq1\)

Strict bracketing gives \(W\leq B_0+3/4\).  Because \(\gamma<0\), (6),
(12), and the exact-angle reserve yield

\[
 c\mathcal S>
 B_0\left(\frac12-c+\gamma\right)
 +\frac34\gamma-\frac{7c}{6}-\frac{cd}{2}.              \tag{19}
\]

The coefficient of \(B_0\) is positive:

\[
 \frac12-c+\gamma>
 \frac12-\frac{641}{5000}-\frac9{100}
 =\frac{1409}{5000}>0.                                  \tag{20}
\]

Hence \(B_0=1\).  The resulting ledger is

\[
 L_B(c,\gamma)=\frac12-\frac83c+c^2+\frac74\gamma.
\]

It decreases in \(c\) because \(-8/3+2c<0\), and increases in
\(\gamma\).  Equations (10) and (17) therefore give the exact rational
ledger

\[
 \boxed{
 c\mathcal S>
 \frac{1280143}{75000000}>0.}                            \tag{21}
\]

### 4.2. The stratum \(B_0=Q=0\)

The outer tangent triangle and (12) give

\[
 c\mathcal S>F_0(W):=W^2+\gamma W-\frac c2+c^2.          \tag{22}
\]

By (17)--(18),

\[
 F_0'(W)=2W+\gamma>
 2\frac{229}{500}-\frac9{100}=\frac{413}{500}>0.
\]

Thus \(W=229/500\) is the lower endpoint.  At that endpoint the ledger
decreases in \(c\), since \(-1/2+2c<0\), and increases in \(\gamma\).
Therefore

\[
 \boxed{
 c\mathcal S>
 \frac{3021981}{25000000}>0.}                            \tag{23}
\]

### 4.3. The stratum \(B_0=0,Q=1\)

Here

\[
 \frac34-c<W\leq\frac34,
\]

and the inner payment plus outer tangent triangle gives

\[
 c\mathcal S>
 F_1(W):=-W^2+\left(\frac32+\gamma\right)W
 -\frac32c+c^2.                                          \tag{24}
\]

This is concave in \(W\), so it suffices to check the two endpoints.  At
\(W=3/4\), the expression decreases in \(c\) and increases in
\(\gamma\).  At \(W=3/4-c\), it becomes

\[
 \frac9{16}-\frac32c+\gamma\left(\frac34-c\right).
\]

Its partial derivative in \(c\) is \(-3/2-\gamma<0\), and its partial
derivative in \(\gamma\) is \(3/4-c>0\).  Thus (10) and (17) give

\[
 \boxed{
 F_1(3/4)>
 \frac{7978381}{25000000}>0,}                            \tag{25}
\]

\[
 \boxed{
 F_1(3/4-c)>
 \frac{157119}{500000}>0.}                               \tag{26}
\]

For a separate correlated check, the verifier evaluates (19), (22), and
both endpoints of (24) directly on 256 full rational panels, without first
separating \(c\) and \(\gamma\).  This is an outward-rounded interval
replay distinct from the exact rational proof (21), (23), (25)--(26).
The finer subdivision makes even its raw interval lower endpoints exceed
the rational floors.  Conservative lower bounds across all four replay
precisions were, respectively,

\[
 0.017263564377,\qquad
 0.120924743146,\qquad
 0.319220429717,\qquad
 0.314297954935.                                         \tag{27}
\]

The \(B_0\)-coefficient lower bound was \(0.281907873981\), and the
\(Q=0\) \(W\)-derivative lower bound was \(0.826096309901\).  Equations
(21), (23), (25), and (26) close every \(\delta\geq1\) face, including
all strict-count walls.

## 5. Improving the small-\(\delta\) level distance

Suppose \(0<\delta<1\), and put

\[
 y=f-W=\delta+\frac14,\qquad L=\frac{29}{10}.
\]

The inherited scale monotonicity reduces the largest level distance at
fixed \(y\) to \(f=2\), \(W=2-y\).  With \(x=y/W\), the inherited
concavity reduction leaves only

\[
 x\in\left\{\frac17,\frac53\right\}.                    \tag{28}
\]

Let

\[
 t_0=\frac{Ly}{c},\qquad u_0=\frac{t_0}{\mu},\qquad
 \kappa_\rho=\frac{\Phi}{\theta\rho(1-\rho)}.
\]

The bound \(\Phi<\theta^3/3\), together with (10), gives

\[
 u_0<
 \frac{29}{10}\frac59
 \frac{163/1000}{23/25}
 =\frac{4727}{16560}<\frac{143}{500}<1.                 \tag{29}
\]

To retain a sharper lower integration range, differentiate

\[
 \kappa(\theta)=
 \frac{\sin\theta-\theta\cos\theta}
 {\theta\cos\theta(1-\cos\theta)}.
\]

If \(N=\Phi\) and \(D=\theta\cos\theta(1-\cos\theta)\), then

\[
 N'D-ND'=
 \theta\sin\theta\,\theta\rho(1-\rho)
 -\Phi\left(\rho(1-\rho)
 +\theta\sin\theta(2\rho-1)\right).                    \tag{30}
\]

Directed evaluation of (30) on 64 complete rational panels gives the
strict lower bound

\[
 N'D-ND'>0.000190444285561.                              \tag{31}
\]

Hence \(\kappa\) increases with \(\theta\), and its minimum is at
\(\rho=1847/2000\).  At that endpoint,

\[
 \boxed{\kappa_\rho>\frac{18}{25},}                      \tag{32}
\]

with directed lower gap

\[
 \kappa_{1847/2000}-\frac{18}{25}
 >1.6195058963\times10^{-5}.
\]

Consequently

\[
 \frac{u_0}{1-\rho}>L\frac{18}{25}x
 =\frac{261}{125}x.                                     \tag{33}
\]

## 6. The retained arccos integral

Use

\[
 \arccos(1-z)=\sqrt{2z}\,S(z).
\]

The alternating Taylor estimates

\[
 1-\cos\theta>
 \theta^2\left(\frac12-\frac{\theta^2}{24}\right),
\]

\[
 \Phi<\theta^3\left(
 \frac13-\frac{\theta^2}{30}+\frac{\theta^4}{840}
 \right)
\]

and the decreasing coefficient quotient give

\[
 \boxed{
 C_\rho=
 \frac{\rho\sqrt2(1-\rho)^{3/2}}{\Phi}
 >\frac{137}{100}.}                                     \tag{34}
\]

Indeed, the logarithmic derivative test reduces to

\[
 84+10t-\frac{t^2}{2}>0,
 \qquad 0\leq t\leq\frac{163}{1000},
\]

and evaluation at \(\rho=23/25\), \(t=163/1000\) gives the stronger
directed lower value \(1.37424804127\ldots\).

Retain

\[
 0\leq v\leq V:=\frac{261}{125}x\leq\frac{87}{25}.
\]

Since \(1-\rho\leq2/25\),

\[
 (1-\rho)V\leq\frac{174}{625},\qquad
 (1-\rho)(1+V)\leq\frac{224}{625}<1.                   \tag{35}
\]

The positive decreasing coefficients of \(S\) give a sharper tail if the
\(z^3\)-coefficient \(5/896\) is retained before summing geometrically:

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{21z^2}{1000}.                     \tag{36}
\]

Indeed, on \(z\leq174/625\), the required upper coefficient is at most

\[
 \frac3{160}+\frac5{896}\frac{174/625}{1-174/625}
 =\frac{21117}{1010240}<\frac{21}{1000},
\]

and the convenient integrated ceiling is

\[
 \frac{21}{1000}\frac27=\frac3{500}.                    \tag{37}
\]

The resulting retained lower integral is

\[
\begin{aligned}
 \mathcal I^{\mathrm G}_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)
 +\frac{1-\rho}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3(1-\rho)^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)
 -\frac23V^{3/2}-\frac{1-\rho}{30}V^{5/2}\\
&-\frac{3(1-\rho)^2}{500}V^{7/2}.
                                                               \tag{38}
\end{aligned}
\]

Divide (9) into 64 equal rational panels.  Directed Arb evaluation on
each complete panel and both endpoint values in (28) proves

\[
 \mathcal I^{\mathrm G}_\rho(V)>0,
 \qquad
 \frac{137}{100}\mathcal I^{\mathrm G}_\rho(V)-x>0.      \tag{39}
\]

Across 384, 512, 768, and 1024 bits, the smallest directed lower bounds
were

\[
 \mathcal I^{\mathrm G}_\rho(V)>0.211576376293,
\]

\[
 \frac{137}{100}\mathcal I^{\mathrm G}_\rho(V)-x
 >0.0214999332585.                                      \tag{40}
\]

Concavity fills the whole \(x\)-interval.  Therefore level \(f\) is
present and

\[
 \boxed{T<\frac{29}{10}\frac yc.}                       \tag{41}
\]

## 7. Completing \(0<\delta<1\)

The endpoint chord, \(M\geq\delta/c\), and (41) give

\[
 cP>
 \left(\frac{3-L}{4}-c\right)\delta
 -\frac L{16}-\frac{cd}{2}.                             \tag{42}
\]

Here \((3-L)/4-c<0\).  Since \(\delta<1\), its lower endpoint is therefore
obtained at \(\delta=1\).  Also \(B_0=f-1\), \(Q\leq f-1\), and (6) gives

\[
 cD_A(q)>
 \frac{f-1}{2}-c(f-1)-\frac c6
 \geq\frac12-\frac{7c}{6}.                              \tag{43}
\]

Adding (42)--(43), using \(d=1-2c\) and \(L=29/10\), yields

\[
 c\mathcal S>
 \frac54-\frac{5L}{16}-\frac83c+c^2.
\]

This decreases on the certified interval.  At \(c=641/5000\),

\[
 \boxed{
 c\mathcal S>
 \frac{1373893}{75000000}>0.}                            \tag{44}
\]

Together with Section 4 and Round 8F above \(1847/2000\), this proves
(1).

## 8. Improved residual cutoff

For a residual ratio \(\rho<23/25\), put

\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.
\]

Monotonicity and directed endpoint evaluation give

\[
 \eta_\rho>\frac1{147},\qquad \eta_\rho<\frac19.        \tag{45}
\]

Also

\[
 a_\rho<23\pi<23\frac{355}{113}=\frac{8165}{113}.
\]

Since \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{8165}{113}+\frac{13}{45}
 =\frac{368894}{5085}<73.                               \tag{46}
\]

Because \(C_*>1/2\), the square root in the fixed-ratio threshold is
strictly smaller than the same left side.  Therefore

\[
 \boxed{K_0(\rho)<73\cdot147^2=1\,577\,457.}            \tag{47}
\]

Negativity excludes \(p=0\), so \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\).  Since \(r\geq1/2\), (47) gives

\[
 \rho>\frac1{3\,154\,914},\qquad
 2r\leq3\,154\,913,\qquad
 n\leq1\,577\,456.
\]

Finally \(A(r)\geq7/4\) gives \(K-\mu>7\pi/4\) and \(K>21/4\), while
\(\pi>3\) gives

\[
 f,B<\frac K3+\frac14<525\,819+\frac14.
\]

These are exactly (2)--(5).

## 9. Directed-arithmetic convention and reproduction

The verifier is

    scripts/general_d_round_08g_correlated_prefix_verify.py

It pins both frozen Round 8F artifacts before import.  Every panel is an
exact rational interval.  The inherited midpoint-radius constructor
creates an Arb ball and explicitly checks that it contains both rational
endpoints.  Arb then encloses every algebraic and transcendental operation
with outward rounding.  A positive assertion is accepted only when the
directed lower endpoint is strictly positive; a negative assertion such as
(15) is accepted only when the directed upper endpoint is strictly below
the stated rational bound.  All remaining arithmetic is exact `fmpq`
arithmetic.

The certificate checks:

- 64 full panels for \(\gamma'(\theta)\) and 256 finer full panels for
  the exact correlated terminal ledgers;
- 64 full panels for the derivative numerator in (30);
- 64 panels times two \(x\)-endpoints for (39);
- the exact rational terminal ledgers and all monotonicity endpoints;
- the cap, series domains and coefficients, small-\(\delta\) polynomial,
  cutoff, and integer ranges.

The remaining compact high-floor region is

\[
 \boxed{
 \frac1{3\,154\,914}<\rho<\frac{23}{25},\qquad
 \frac{21}{4}<K<1\,577\,457.}
\]

No wall in this residual box is claimed certified by this round.
