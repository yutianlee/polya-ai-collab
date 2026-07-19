# General dimension, Round 8B: terminal payment on the high-floor obstruction

Date: 18 July 2026  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: rigorous exclusion of

\[
 \boxed{\frac{477}{500}\leq\rho<1.}
\]

The new ingredient is terminal information on the \(\delta\geq1\) faces.
It removes the absent-level obstruction isolated in Round 8A and, because
the present-level chord coefficient is larger by \(1/200\), handles that
face at the same time.  Together with the fixed-ratio scalar theorem, the
new residual cutoff is

\[
 \boxed{K<14\,965\,964.}
\]

This is a real ratio exclusion and a further compact reduction.  It is
not a certificate of the remaining \(\rho<477/500\) analytic walls.
Ordinary floors define the first shelf, strict brackets define terminal
counts, and no equality wall is filled by continuity.

## 1. Result

### Theorem 1 (terminally strengthened high-floor exclusion)

Let

\[
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p),
 \qquad
 c=\frac{\arccos\rho}{\pi},\qquad d_\rho=1-2c.
\]

If \(f\geq2\), \(p<n\), and \(\rho\geq477/500\), then

\[
 \boxed{\mathcal S>0.}                              \tag{1}
\]

Consequently every remaining negative high-floor first-drop candidate
satisfies

\[
 \boxed{
 \frac1{29\,931\,928}<\rho<\frac{477}{500},
 \qquad \frac{21}{4}<K<14\,965\,964.}              \tag{2}
\]

Its discrete labels obey the conservative exact ranges

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq29\,931\,927,\\
 2\leq n\leq14\,965\,963,\qquad 1\leq p\leq n-1,\\
 2\leq f\leq4\,988\,654,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq4\,988\,654.
 \end{gathered}}                                    \tag{3}
\]

The exact chamber conditions remain

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,
 \qquad K-\mu>\frac{7\pi}{4},                      \tag{4}
\]

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.                               \tag{5}
\]

The theorem does not deduce closure from the finiteness of (2)--(3).

## 2. Endpoint chord and a common \(\delta\geq1\) prefix

Put

\[
 \widehat H(t)=A(\mu-t),\qquad
 W=\widehat H(0)=G_K(\mu),\qquad h=f-\frac14,
\]

and write \(\xi=r+p\), \(m=n-p\), and
\(t_\xi=\mu-\xi\).  The first shelf and its first drop determine \(M\)
by

\[
 \widehat H(M)=h,\qquad M\leq t_\xi<M+1.            \tag{6}
\]

If level \(f\) exists, let \(\widehat H(T)=f\) and put \(\zeta=0\).
If it is absent, put \(T=\mu\) and

\[
 \zeta=f-\widehat H(T)\in(0,1/4].                  \tag{7}
\]

Since \(t_\xi=m+\alpha\), where
\(\alpha=\mu-q\in[0,1)\), one has \(m\geq M-1\).
The exact shelf integral and the endpoint chord of the convex function
\(f-\widehat H\) give

\[
 \boxed{
 P:=R_p+\frac d2m
 \geq-\left(\frac14+\zeta\right)(T-M)
       +\frac d2(M-1),}                             \tag{8}
\]

where \(d=d_\rho=1-2c\).  Let

\[
 \delta=h-W>0.
\]

The slope bound \(0\leq\widehat H'\leq c\) gives

\[
 M\geq\frac{\delta}{c}.                             \tag{9}
\]

At the new rational endpoint, directed evaluation proves

\[
 \rho\geq\frac{477}{500}
 \quad\Longrightarrow\quad
 \theta^2<\frac{93}{1000},\qquad
 c<\bar c:=\frac{97}{1000},                         \tag{10}
\]

where \(\theta=\arccos\rho=\pi c\).

Assume in this section that \(\delta\geq1\), and put

\[
 \gamma=\frac3{25}-c>0.                            \tag{11}
\]

The shell-increment elasticity is

\[
 \frac{\widehat H(t_2)-W}{\widehat H(t_1)-W}
 \geq
 \frac{t_2/t_1}{\sqrt{2t_2/t_1-1}}.                \tag{12}
\]

If level \(f\) is present, (12) gives \(T/M\leq5/2\), hence

\[
 cP\geq\left(\frac18-c\right)\delta-\frac{cd}{2}
 >\gamma\delta-\frac{cd}{2},                       \tag{13}
\]

because

\[
 \frac18-\frac3{25}=\frac1{200}.
\]

If level \(f\) is absent, the Round-07 degree-\(32\) Bernstein
certificate gives

\[
 \left(\frac12-a\right)(r_*(1+a)-1)<\frac{19}{50},
 \qquad
 r_*(R)=R^2+R\sqrt{R^2-1},
\]

for \(0\leq a\leq1/4\), with exact smallest Bernstein coefficient
\(309/396800\).  Equations (8)--(9) then give

\[
 cP>\gamma\delta-\frac{cd}{2}.                     \tag{14}
\]

Thus both level faces have the common strict prefix bound

\[
 \boxed{cP>\gamma\delta-\frac{cd}{2}.}              \tag{15}
\]

## 3. Terminal stratification for \(\delta\geq1\)

Define the strict counts

\[
 B_0=\left[W+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.                    \tag{16}
\]

Because \(q=\mu-\alpha\), \(0\leq\alpha<1\), the slope bound gives

\[
 0\leq A(q)-W<c.
\]

The strict-bracket convention therefore implies, including on every
wall,

\[
 \boxed{B\geq B_0,\qquad Q\leq B_0+1.}             \tag{17}
\]

Indeed, the first inequality is monotonicity of \(G_K\), and
\(A(q)+1/4<W+1/4+1\) proves the second.

### 3.1. At least one complete terminal level

Suppose \(B_0\geq1\).  For \(1\leq k\leq B_0\), strict bracketing gives

\[
 k-\frac14<W=G_K(\mu).
\]

Hence the ball angle \(\theta_k\) at level \(k-1/4\) satisfies
\(\theta_k<\theta=\pi c\).  The exact-angle terminal reserve, (17), and
the cap bound

\[
 2\int_q^\mu G_\mu<\frac25
\]

give

\[
\begin{aligned}
 cD_A(q)
 &> \frac{B_0}{2}-cQ-\frac{2c}{5}\\
 &\geq B_0\left(\frac12-c\right)-\frac{7c}{5}.
\end{aligned}                                      \tag{18}
\]

Combining (15), (18), \(\delta\geq1\), and \(B_0\geq1\) yields

\[
 c\mathcal S>
 \frac{31}{50}-\frac{39}{10}c+c^2.                \tag{19}
\]

The right side decreases on \(0<c\leq\bar c\), and at the rational
endpoint

\[
 \boxed{
 c\mathcal S>\frac{251109}{1000000}>0.}            \tag{20}
\]

### 3.2. No complete terminal level

Suppose \(B_0=0\).  The strict convention says exactly

\[
 0<W\leq\frac34,\qquad Q\in\{0,1\}.                \tag{21}
\]

Moreover \(q+1>\mu\).  For every \(j\geq1\),

\[
 A(q+j)=G_K(q+j)<G_K(\mu)=W\leq\frac34.
\]

Thus every terminal sample after \(q\) has strict count zero.  The only
possible discrete contribution to the shell tail is \(Q\) at \(q\).

#### The face \(Q=0\)

The shell discrete tail is empty.  Convexity of \(G_K\) on
\([\mu,K]\), with value \(W\) and slope magnitude \(c\) at \(\mu\),
gives the outer tangent triangle

\[
 D_A(q)=2\int_q^K A(z)\,dz
 \geq2\int_\mu^K G_K(z)\,dz
 \geq\frac{W^2}{c}.                                \tag{22}
\]

Since \(f\geq2\),

\[
 \delta=f-\frac14-W\geq\frac74-W.
\]

Equations (15) and (22) give

\[
 c\mathcal S>
 \gamma\left(\frac74-W\right)-\frac c2+c^2+W^2.
                                                               \tag{23}
\]

The right side is convex in \(W\), and its minimum on
\([0,3/4]\) occurs at \(W=\gamma/2\).  Consequently

\[
 c\mathcal S>
 \frac{129}{625}-\frac{219}{100}c+\frac34c^2.      \tag{24}
\]

This polynomial decreases on the certified interval.  At
\(c=\bar c\),

\[
 \boxed{
 c\mathcal S>\frac{4107}{4000000}>0.}              \tag{25}
\]

This is the limiting exact ledger in Round 8B.

#### The face \(Q=1\)

Here strict bracketing gives \(A(q)>3/4\).  Since

\[
 A(q)-W<c\alpha,
\]

one has

\[
 \alpha>\frac{3/4-W}{c},\qquad
 \frac34-c<W\leq\frac34.                           \tag{26}
\]

On \([q,\mu]\), \(A\geq W\).  The inner continuous payment and the
outer tangent triangle therefore give

\[
\begin{aligned}
 cD_A(q)
 &=c\left(2\int_q^K A-1\right)\\
 &>2W\left(\frac34-W\right)+W^2-c\\
 &=\frac32W-W^2-c.
\end{aligned}                                      \tag{27}
\]

Combining (15), (26), and \(\delta\geq7/4-W\) gives a concave
quadratic in \(W\).  Its minimum on
\((3/4-c,3/4]\) is at an endpoint.  The two endpoint ledgers are

\[
 L_+(c)=\frac{273}{400}-\frac52c+c^2,              \tag{28}
\]

\[
 L_-(c)=\frac{273}{400}-\frac{119}{50}c-c^2.       \tag{29}
\]

Both decrease on the certified interval, and

\[
 \boxed{
 L_+(\bar c)=\frac{449409}{1000000},\qquad
 L_-(\bar c)=\frac{442231}{1000000}.}              \tag{30}
\]

Thus all \(\delta\geq1\) faces are strictly positive.

## 4. Enlarging the \(0<\delta<1\) certificate

For \(0<\delta<1\), strict bracketing gives

\[
 B_0=f-1,\qquad
 W=f-\frac14-\delta>f-\frac54\geq\frac34.          \tag{31}
\]

Set

\[
 y=f-W=\delta+\frac14\in(1/4,5/4).
\]

As in Round 8A, we prove

\[
 \boxed{T<\frac{3y}{c}.}                            \tag{32}
\]

For completeness, the scale and concavity reductions are recalled.
At fixed \(\rho\),

\[
 E_K(t)=\widehat H(t)-W=K E_1(t/K)
\]

is nondecreasing in \(K\) at fixed \(t\), since \(E_1\) is concave and
\(E_1(0)=0\).  The largest level distance therefore occurs at

\[
 f=2,\qquad W=2-y,\qquad
 x=\frac yW\in\left[\frac17,\frac53\right].        \tag{33}
\]

Put

\[
 g_\rho=G_1(\rho),\qquad
 e_\rho(s)=G_1(\rho-s)-\rho G_1(1-s/\rho)-g_\rho.
\]

With \(b=1-s/\rho\),

\[
\begin{aligned}
 e_\rho''(s)
 &=\frac1{\pi\sqrt{1-\rho^2b^2}}
   -\frac1{\pi\rho\sqrt{1-b^2}}\leq0,
\end{aligned}
\]

because \(\rho^2(1-b^2)\leq1-\rho^2b^2\).  Hence

\[
 \mathcal F_\rho(x)
 =\frac{e_\rho(3xg_\rho/c)}{g_\rho}-x              \tag{34}
\]

is concave in \(x\), and it is enough to check the endpoints in (33).

Let

\[
 \epsilon=1-\rho,\qquad
 \Phi=\sin\theta-\theta\cos\theta,\qquad
 W=K\frac{\Phi}{\pi}.
\]

For \(t_0=3y/c\) and \(u_0=t_0/\mu\),

\[
 u_0=\frac{3x\Phi}{\theta\rho}.                    \tag{35}
\]

The bounds \(\Phi<\theta^3/3\) and (10) give

\[
 u_0<
 \frac53\frac{93/1000}{477/500}<\frac16.           \tag{36}
\]

Also

\[
 \Phi>\frac{\rho\theta^3}{3}.                      \tag{37}
\]

The difference in (37) vanishes at zero and has derivative

\[
 \theta\Phi+\frac{\theta^3\sin\theta}{3}>0.
\]

Since \(\epsilon<\theta^2/2\), equations (35)--(37) imply

\[
 \frac{u_0}{\epsilon}>2x.                          \tag{38}
\]

Use the positive normalized series

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\geq0}
 \frac{\binom{2j}{j}}{8^j(2j+1)}z^j.              \tag{39}
\]

Its first coefficients are \(1,1/12,3/160\), and all later
coefficients decrease.  On the enlarged retained range

\[
 0\leq z\leq
 \frac{23}{500}\frac{10}{3}
 =\frac{23}{150},                                  \tag{40}
\]

the exact upper tail is

\[
 \sum_{j\geq2}a_jz^j
 \leq\frac{3z^2/160}{1-23/150}
 =\frac{45}{2032}z^2.                              \tag{41}
\]

Thus

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)
 \leq1+\frac z{12}+\frac{45z^2}{2032}.             \tag{42}
\]

The first, positively truncated series also stays inside its convergence
domain, since on \(0\leq v\leq10/3\),

\[
 \epsilon(1+\rho v)
 \leq\frac{23}{500}\frac{13}{3}
 =\frac{299}{1500}<1.
\]

The exact noncancelling identity is

\[
 \frac{E_K(t_0)}W
 =C_\rho\int_0^{u_0/\epsilon}
 \left[
 \sqrt{1+\rho v}\,S(\epsilon(1+\rho v))
 -\sqrt v\,S(\epsilon v)
 \right]dv,                                        \tag{43}
\]

\[
 C_\rho=\frac{\rho\sqrt2\,\epsilon^{3/2}}{\Phi}.
\]

The Taylor bounds

\[
 \epsilon>\theta^2\left(\frac12-\frac{\theta^2}{24}\right),
 \qquad
 \Phi<\theta^3\left(
 \frac13-\frac{\theta^2}{30}+\frac{\theta^4}{840}
 \right)
\]

and the decreasing quotient

\[
 t\longmapsto
 \frac{(1/2-t/24)^{3/2}}{1/3-t/30+t^2/840}
\]

reduce the coefficient to the rational endpoint.  Its logarithmic
derivative is negative because

\[
 84+10t-\frac{t^2}{2}>0
 \qquad(0\leq t\leq93/1000).
\]

Directed evaluation
at \(t=93/1000\), \(\rho=477/500\), proves

\[
 \boxed{C_\rho>\frac75.}                            \tag{44}
\]

By (38), retain \(0\leq v\leq V=2x\).  Keeping three positive terms in
the first copy of \(S\) and using (42) in the subtracted copy gives

\[
 \frac{E_K(t_0)}W>\frac75\,\mathcal I_\rho(V),      \tag{45}
\]

once the positivity of the retained lower integral is certified, where

\[
\begin{aligned}
 \mathcal I_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)\\
&+\frac{\epsilon}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3\epsilon^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)\\
&-\frac23V^{3/2}-\frac{\epsilon}{30}V^{5/2}
 -\frac{45\epsilon^2}{7112}V^{7/2}.
\end{aligned}                                      \tag{46}
\]

The coefficient \(45/7112\) is exactly
\((45/2032)(2/7)\).

Divide

\[
 \frac{477}{500}\leq\rho\leq\frac{99}{100}
\]

into \(32\) equal rational panels.  On each full Arb interval, directed
evaluation of (46) at \(x=1/7,5/3\) proves

\[
 \mathcal I_\rho(2x)>0,\qquad
 \frac75\mathcal I_\rho(2x)-x>0.                   \tag{47}
\]

Across directed runs at \(384\), \(512\), \(768\), and \(1024\) bits,
the smallest reported lower margin in (47) exceeds

\[
 0.0607609473,
\]

and the smallest retained-integral lower bound is

\[
 >0.2031479283.
\]

Concavity in (34) proves (47) throughout (33), hence (32).

Level \(f\) is present, so \(\zeta=0\).  Equations (8)--(9) and (32)
give

\[
 cP>-c-\frac3{16}-\frac{cd}{2}.                    \tag{48}
\]

Here \(B_0=f-1\), \(Q\leq f-1\), and every retained terminal ball angle
is smaller than \(\theta=\pi c\).  The exact-angle reserve and the cap
bound give

\[
 cD_A(q)>\frac12-\frac75c.                         \tag{49}
\]

Adding these bounds and using \(d=1-2c\) yields

\[
 c\mathcal S>\frac5{16}-\frac{29}{10}c+c^2.        \tag{50}
\]

At \(c=\bar c\),

\[
 \boxed{
 c\mathcal S>\frac{40609}{1000000}>0.}             \tag{51}
\]

Equations (20), (25), (30), and (51), together with the Round-07
exclusion above \(99/100\), prove (1).

## 5. Improved residual cutoff

For a residual ratio \(\rho<477/500\), monotonicity of \(G_1\) and
directed evaluation at the endpoint give

\[
 \eta_\rho>\frac1{338},\qquad \eta_\rho<\frac19.   \tag{52}
\]

Moreover,

\[
 a_\rho<2\frac{355}{113}\frac{477}{23}
 =\frac{338670}{2599}.                             \tag{53}
\]

Since \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{338670}{2599}+\frac{13}{45}<131.           \tag{54}
\]

Since \(C_*>1/2\),

\[
 \sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}
 <a_\rho+2\eta_\rho C_*.
\]

The fixed-ratio threshold therefore satisfies

\[
 \boxed{
 K_0(\rho)<131\cdot338^2=14\,965\,964.}             \tag{55}
\]

Negativity excludes \(p=0\).  As in Round 8A,

\[
 2r<2K<29\,931\,928,\qquad
 n<K-\frac12<14\,965\,963\frac12,
\]

\[
 f,B<\frac K3+\frac14
 <4\,988\,654+\frac{11}{12}.
\]

Taking exact integer consequences proves (2)--(5).

## 6. What now limits this ledger

The terminal stratification removes the old absent-level sign change at
\(\rho=0.964728\ldots\).  With only the outer tangent triangle and no
additional use of the active-width relation, the weakest new polynomial
is (24).  Its first zero is

\[
 c_*=\frac{219-\sqrt{41769}}{150}
 =0.0975022935\ldots,
\qquad
 \cos(\pi c_*)=0.9534519995\ldots.
\]

The rational choice \(\bar c=97/1000\) stays strictly below this zero.
The actual high-floor active-width inequality supplies further positive
information relating \(W\) and \(c\), so this sign change is not a
counterexample and need not be the ultimate barrier.  The present round
stops at the clean rational ratio \(477/500\); pushing farther requires
retuning both the small-\(\delta\) series certificate and the weakest
zero-count terminal ledger.

## 7. Reproducibility

The verifier is

    scripts/general_d_high_floor_absent_terminal_verify.py

It reconstructs the Bernstein coefficients, every rational scalar
ledger, the series-tail coefficients \(45/2032\) and \(45/7112\), the
fixed-ratio cutoff, and the integer ranges exactly.  Arb directed
rounding is used only for the endpoint transcendental inequalities, the
coefficient lower bound, the \(64\) full interval/end-point evaluations
in (47), and the lower bound in (52).

The certificate proves a ratio interval and a smaller residual box.  It
does not sample the original scalar and makes no claim about the
remaining fixed-ratio compact walls.
