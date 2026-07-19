# General dimension, Round 8A: the residual high-floor ratio band

Date: 18 July 2026  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: rigorous exclusion of

\[
 \boxed{\frac{603}{625}\leq\rho<1.}
\]

Together with the fixed-ratio scalar estimate, this replaces the Round-07
residual cutoff \(K<7.1\times10^9\) by

\[
 \boxed{K<43\,944\,768.}
\]

This is a further compact reduction, not a certificate of the residual
\(\rho<603/625\) analytic walls. Ordinary floors define the first shelf,
and strict brackets define every terminal count. No equality wall is
filled by continuity.

## 1. Result

### Theorem 1 (extended high-floor ratio exclusion)

Let

\[
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p),
 \qquad
 c=\frac{\arccos\rho}{\pi},\qquad d_\rho=1-2c.
\]

If \(f\geq2\), \(p<n\), and \(\rho\geq603/625\), then

\[
 \boxed{\mathcal S>0.}                              \tag{1}
\]

Consequently every remaining negative high-floor first-drop candidate
satisfies

\[
 \boxed{
 \frac1{87\,889\,536}<\rho<\frac{603}{625},
 \qquad \frac{21}{4}<K<43\,944\,768.}              \tag{2}
\]

Its discrete labels obey the conservative exact ranges

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq87\,889\,535,\\
 2\leq n\leq43\,944\,767,\qquad 1\leq p\leq n-1,\\
 2\leq f\leq14\,648\,256,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq14\,648\,256.
 \end{gathered}}                                    \tag{3}
\]

The chamber also retains

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,
 \qquad K-\mu>\frac{7\pi}{4},                      \tag{4}
\]

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.                               \tag{5}
\]

The theorem closes a real interval of the residual box. It does not
deduce closure from the finiteness of (2)--(3).

## 2. Endpoint-chord prefix with exact ratio constants

Put

\[
 \widehat H(t)=A(\mu-t),\qquad W=\widehat H(0)=G_K(\mu),
 \qquad h=f-\frac14,
\]

and write \(x=r+p\), \(m=n-p\), \(t_x=\mu-x\). The first shelf and its
first drop determine \(M\) by

\[
 \widehat H(M)=h,\qquad M\leq t_x<M+1.             \tag{6}
\]

If level \(f\) exists, let \(\widehat H(T)=f\) and put \(\zeta=0\).
If it is absent, put \(T=\mu\) and

\[
 \zeta=f-\widehat H(T)\in(0,1/4].                  \tag{7}
\]

Thus the present- and absent-level faces remain separate. Since
\(t_x=m+\alpha\), \(0\leq\alpha<1\), one has \(m\geq M-1\). Changing
variables in the exact shelf integral and using the endpoint chord of the
convex function \(f-\widehat H\) gives

\[
 \boxed{
 P:=R_p+\frac d2m
 \geq-\left(\frac14+\zeta\right)(T-M)
       +\frac d2(M-1),}                             \tag{8}
\]

where \(d=d_\rho=1-2c\). This is the Round-07 endpoint-chord estimate
without replacing \(c,d\) by \(1/20,9/10\).

Let \(\delta=h-W>0\). The slope bound
\(0\leq\widehat H'\leq c\) gives

\[
 M\geq\frac\delta c.                               \tag{9}
\]

At the rational endpoint, directed evaluation gives

\[
 \rho\geq\frac{603}{625}
 \quad\Longrightarrow\quad
 \theta^2<\frac{71}{1000},\qquad
 c<\bar c:=\frac{339}{4000},                       \tag{10}
\]

where \(\theta=\arccos\rho=\pi c\).

## 3. The two \(\delta\geq1\) level faces

The shell-increment elasticity gives

\[
 \frac{\widehat H(t_2)-W}{\widehat H(t_1)-W}
 \geq
 \frac{t_2/t_1}{\sqrt{2t_2/t_1-1}}.                \tag{11}
\]

### 3.1. Level \(f\) is present

For \(\delta\geq1\), (11) at \(M,T\) gives \(T/M\leq5/2\). Thus

\[
\begin{aligned}
 P
 &\geq\left(\frac d2-\frac38\right)M-\frac d2\\
 &\geq\frac{1/8-c}{c}-\left(\frac12-c\right)
 =\frac1{8c}-\frac32+c.
\end{aligned}                                      \tag{12}
\]

The last expression decreases on the present range of \(c\). Hence (10)
gives

\[
 \boxed{P>\frac{80921}{1356000}.}                  \tag{13}
\]

### 3.2. Level \(f\) is absent

Put \(a=1/4-\zeta\in[0,1/4]\). The elasticity estimate gives

\[
 \frac{\mu/M}{\sqrt{2\mu/M-1}}
 \leq1+\frac a\delta\leq1+a.                       \tag{14}
\]

If

\[
 r_*(R)=R^2+R\sqrt{R^2-1},
\]

the exact Round-07 Bernstein certificate proves

\[
 \left(\frac12-a\right)(r_*(1+a)-1)<\frac{19}{50}
 \qquad(0\leq a\leq1/4).                           \tag{15}
\]

Its degree-32 minimum is \(309/396800\). Consequently

\[
\begin{aligned}
 P
 &>\left(\frac d2-\frac{19}{50}\right)M-\frac d2\\
 &\geq\frac{3/25-c}{c}-\left(\frac12-c\right)
 =\frac3{25c}-\frac32+c.
\end{aligned}                                      \tag{16}
\]

This expression is decreasing on the relevant interval. At
\(c=\bar c\),

\[
 \boxed{P>\frac{307}{452000}>0.}                   \tag{17}
\]

The small margin in (17) is the limiting ledger in this round.

## 4. Refined level distance for \(0<\delta<1\)

Here strict bracketing gives exactly

\[
 B_0=\left[W+\frac14\right]_< =f-1,\qquad
 W=f-\frac14-\delta>f-\frac54\geq\frac34.          \tag{18}
\]

Set

\[
 y=f-W=\delta+\frac14\in(1/4,5/4).
\]

We prove

\[
 \boxed{T<\frac{3y}{c}.}                            \tag{19}
\]

This also proves that level \(f\) is present.

### 4.1. Scale reduction and concavity

For fixed \(\rho\), the increment

\[
 E_K(t)=\widehat H(t)-W=K E_1(t/K)
\]

is nondecreasing in \(K\) at fixed \(t\), because \(E_1\) is concave and
\(E_1(0)=0\). At fixed \(y\), the distance to \(W+y\) is therefore
largest at the smallest admissible \(W\). Since \(W=f-y\geq2-y\), it
suffices to take

\[
 f=2,\qquad W=2-y,\qquad
 x=\frac yW\in\left[\frac17,\frac53\right].        \tag{20}
\]

Put

\[
 g_\rho=G_1(\rho),\qquad
 e_\rho(s)=G_1(\rho-s)-\rho G_1(1-s/\rho)-g_\rho.
\]

The scaled shell increment \(e_\rho\) is concave in \(s\). Since
\(K=W/g_\rho\),

\[
 \mathscr F_\rho(x)
 :=\frac{E_K(3y/c)}W-x
 =\frac{e_\rho(3xg_\rho/c)}{g_\rho}-x.             \tag{21}
\]

Thus \(\mathscr F_\rho\) is concave in \(x\). It is enough to prove
\(\mathscr F_\rho(x)>0\) at \(x=1/7,5/3\).

### 4.2. A noncancelling positive arccos series

Let

\[
 \theta=\arccos\rho,\qquad \epsilon=1-\rho,\qquad
 \Phi=\sin\theta-\theta\cos\theta,\qquad
 W=K\frac\Phi\pi.
\]

For \(t_0=3y/c\), put \(u_0=t_0/\mu\). Then

\[
 u_0=\frac{3x\Phi}{\theta\rho}.                     \tag{22}
\]

The bounds

\[
 \Phi<\frac{\theta^3}{3},\qquad
 \theta^2<\frac{71}{1000},\qquad
 \rho\geq\frac{603}{625}
\]

give

\[
 u_0<\frac53\frac{71/1000}{603/625}<\frac18.       \tag{23}
\]

There is also the strict lower estimate

\[
 \Phi>\frac{\rho\theta^3}{3}.                       \tag{24}
\]

Indeed, the difference between the two sides vanishes at zero and has
derivative

\[
 \theta\Phi+\frac{\theta^3\sin\theta}{3}>0.
\]

Since \(\epsilon<\theta^2/2\), (22)--(24) imply

\[
 \frac{u_0}{\epsilon}>2x.                           \tag{25}
\]

Use the positive series

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\geq0}
 \frac{\binom{2j}{j}}{8^j(2j+1)}z^j.              \tag{26}
\]

Its first coefficients are \(1,1/12,3/160\), and the coefficient ratio is

\[
 \frac{(2j+1)^2}{4(j+1)(2j+3)}<1.
\]

Therefore, for \(0\leq z\leq1/8\),

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)
 \leq1+\frac z{12}+\frac{3z^2}{140}.               \tag{27}
\]

The upper bound majorizes every coefficient from \(j=2\) onward by
\(3/160\) and sums the geometric tail.

The exact noncancelling increment formula, followed by
\(u=\epsilon v\), is

\[
 \frac{E_K(t_0)}W
 =C_\rho\int_0^{u_0/\epsilon}
 \left[
 \sqrt{1+\rho v}\,S(\epsilon(1+\rho v))
 -\sqrt v\,S(\epsilon v)
 \right]dv,                                        \tag{28}
\]

where

\[
 C_\rho=\frac{\rho\sqrt2\,\epsilon^{3/2}}{\Phi}.
\]

Taylor bounds give

\[
 \epsilon>\theta^2\left(\frac12-\frac{\theta^2}{24}\right),
 \qquad
 \Phi<\theta^3\left(
 \frac13-\frac{\theta^2}{30}+\frac{\theta^4}{840}
 \right).                                          \tag{29}
\]

The function

\[
 t\longmapsto
 \frac{(1/2-t/24)^{3/2}}{1/3-t/30+t^2/840}
\]

is decreasing for \(0\leq t\leq71/1000\). After logarithmic
differentiation this follows from

\[
 84+10t-\frac{t^2}{2}>0.
\]

Directed evaluation at \(t=71/1000\), \(\rho=603/625\), proves

\[
 \boxed{C_\rho>\frac{36}{25}.}                      \tag{30}
\]

### 4.3. Directed endpoint panels

By (25), retain \(0\leq v\leq V:=2x\). On this interval

\[
 \epsilon v\leq
 \frac{22}{625}\frac{10}{3}
 =\frac{44}{375}<\frac18,                           \tag{31}
\]

so (27) applies to the subtracted series. Keeping three positive terms in
the first series and using the upper bound in the second gives

\[
 \frac{E_K(t_0)}W>\frac{36}{25}\,\mathcal I_\rho(V),\tag{32}
\]

where

\[
\begin{aligned}
 \mathcal I_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)\\
&+\frac{\epsilon}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3\epsilon^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)\\
&-\frac23V^{3/2}-\frac\epsilon{30}V^{5/2}
 -\frac{3\epsilon^2}{490}V^{7/2}.
\end{aligned}                                      \tag{33}
\]

Divide

\[
 \frac{603}{625}\leq\rho\leq\frac{99}{100}
\]

into 16 equal rational panels. On each panel, directed Arb evaluation of
(33) at \(x=1/7\) and \(x=5/3\) proves

\[
 \mathcal I_\rho(2x)>0,\qquad
 \frac{36}{25}\mathcal I_\rho(2x)-x>0.             \tag{34}
\]

At 384, 768, and 1024 bits the smallest directed lower margin in (34) is

\[
 0.122748159345\ldots,
\]

and the smallest retained-integral lower bound is

\[
 0.202999800557\ldots.
\]

Concavity in \(x\) proves (34) throughout (20), hence (19), on the whole
certified band. Round 7 already proves \(\rho>99/100\).

## 5. Completing \(0<\delta<1\)

Here level \(f\) exists, so \(\zeta=0\). From (8), (9), and (19),

\[
\begin{aligned}
 cP
 &>-\frac34\left(\delta+\frac14\right)
   +\left(\frac14+\frac d2\right)\delta
   -\frac{cd}{2}\\
 &=-c\delta-\frac3{16}-\frac{cd}{2}\\
 &>-c-\frac3{16}-\frac{cd}{2}.                    \tag{35}
\end{aligned}
\]

At the terminal start, strict bracketing gives

\[
 B=\left[G_K(q)+\frac14\right]_<\geq f-1,\qquad
 Q=\left[A(q)+\frac14\right]_<\leq f-1.            \tag{36}
\]

For every \(1\leq k\leq f-1\),

\[
 k-\frac14\leq f-\frac54<W=G_K(\mu),               \tag{37}
\]

strictly. Thus each retained ball angle satisfies
\(\theta_k<\theta=\pi c\). The wall-safe exact-angle reserve and the cap
bound \(2\int_q^\mu G_\mu<2/5\) give

\[
 cD_A(q)>\frac12-\frac75c.                          \tag{38}
\]

Using \(d=1-2c\), equations (35) and (38) yield

\[
 c\mathcal S>\frac5{16}-\frac{29}{10}c+c^2.        \tag{39}
\]

The right side decreases on the present range. At \(c=\bar c\),

\[
 \boxed{
 c\mathcal S>\frac{1182521}{16000000}>0.}          \tag{40}
\]

Equations (13), (17), and (40), together with Round 7 above \(99/100\),
prove Theorem 1.

## 6. Improved fixed-ratio cutoff

For every residual ratio \(\rho<603/625\), the fixed-ratio scalar estimate
uses

\[
 K_0(\rho)=
 \frac{a_\rho+2\eta_\rho C_*
 +\sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}}
 {2\eta_\rho^2}.                                   \tag{41}
\]

Monotonicity of the ball action and directed evaluation at \(603/625\)
give

\[
 \eta_\rho>\frac1{504},\qquad \eta_\rho<\frac19.   \tag{42}
\]

The second inequality is the already proved bound \(G_1(1/2)<1/9\).
Moreover, using \(\pi<355/113\),

\[
 a_\rho<2\frac{355}{113}\frac{603}{22}
 =\frac{214065}{1243}.                              \tag{43}
\]

Since \(C_*<13/10\), equations (42)--(43) imply

\[
 a_\rho+2\eta_\rho C_*
 <\frac{214065}{1243}+\frac{13}{45}<173.           \tag{44}
\]

Because \(C_*>1/2\), the square root in (41) is strictly smaller than
\(a_\rho+2\eta_\rho C_*\). Hence

\[
 \boxed{
 K_0(\rho)<173\cdot504^2=43\,944\,768.}            \tag{45}
\]

This proves the \(K\)-bound in (2). Negativity excludes \(p=0\), and the
same chamber geometry as in Round 7 gives (2)--(5):

\[
 2r<2K<87\,889\,536,\qquad
 n<K-\frac12<43\,944\,767\frac12,
\]

\[
 f,B<\frac K3+\frac14<14\,648\,256\frac14.
\]

Taking the exact integer consequences gives (3).

## 7. Precise obstruction to pushing this ledger farther

The present-level \(\delta\geq1\) lower bound remains positive until

\[
 c<\frac{3-\sqrt7}{4}=0.08856\ldots.
\]

The small-\(\delta\) bound (39) remains positive farther still. The first
obstruction is the absent-level estimate (16). Its lower bound changes
sign at

\[
 c_{\mathrm{abs}}
 =\frac{\frac32-\sqrt{177/100}}2
 =0.0847932652\ldots,
\]

corresponding to

\[
 \rho_{\mathrm{abs}}
 =\cos(\pi c_{\mathrm{abs}})
 =0.9647285943\ldots.                               \tag{46}
\]

The rational endpoint \(603/625=0.9648\) is only
\(7.14\times10^{-5}\) above this barrier. Thus the refined level-distance
argument is no longer the bottleneck. To move below (46), one must improve
the absent-level elasticity/chord loss \(19/50\) or use additional
positive terminal information on that face. The sign change is an
obstruction to this proof ledger, not a counterexample to the shell scalar.

## 8. Reproducibility

The verifier is

    scripts/general_d_high_floor_fixed_ratio_verify.py

It uses exact rational arithmetic for the Bernstein, scalar-ledger,
cutoff, and integer-range calculations. It uses Arb directed rounding only
for the ratio endpoint, the coefficient lower bound, the two endpoint
values of (33) on 16 rational ratio panels, and the lower bound in (42).

Independent runs at 384, 768, and 1024 bits give the same ledger:

    PASS ratio endpoint: theta^2<71/1000 and c<339/4000
    PASS absent-level Bernstein minimum: 309/396800
    PASS refined arccos constants: coefficient>36/25, u0<1/8
    PASS level-distance band: 32 directed endpoint panels
    PASS exact scalar ledgers:
      delta>=1 present > 80921/1356000
      delta>=1 absent  > 307/452000
      0<delta<1: c*S > 1182521/16000000
    PASS improved fixed-ratio cutoff: K0(rho)<43944768
    PASS conservative exact integer ranges

The certificate proves a ratio interval and a smaller residual box. It
does not sample the original scalar and makes no claim about the remaining
fixed-ratio compact walls.
