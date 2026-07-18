# General dimension, Round 8C: active width removes the zero-count barrier

Date: 2026-07-18  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: analytic ratio certificate with directed interval replay  
Depends on: Rounds 7, 8A, and 8B

This round strengthens the certified ratio band from

\[
 \rho\geq\frac{477}{500}
 \quad\hbox{to}\quad
 \boxed{\rho\geq\frac{939}{1000}}.
\]

The new input is the active-shell inequality

\[
 (1-\rho)K>\pi\left(f-\frac14\right).
\]

It forces a positive lower bound on the interface height
\(W=G_K(\rho K)\).  That lower bound removes the infeasible minimizer
which limited the zero-count terminal ledger in Round 8B.

This is still not a certificate of the residual compact walls below
\(939/1000\).

## 1. Result

### Theorem 1 (active-width high-floor exclusion)

In the high-floor first-drop branch, suppose

\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{939}{1000}\leq\rho<1.
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
 \frac1{9\,572\,836}<\rho<\frac{939}{1000},
 \qquad
 \frac{21}{4}<K<4\,786\,418,}                       \tag{2}
\]

and the finite integer bounds

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq9\,572\,835,\\
 2\leq n\leq4\,786\,417,\qquad
 1\leq p\leq n-1,\\
 2\leq f\leq1\,595\,472,\\
 0\leq Q\leq f-1,\qquad
 Q\leq B\leq1\,595\,472.
 \end{gathered}}                                      \tag{3}
\]

The chamber conditions remain

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,
 \qquad K-\mu>\frac{7\pi}{4},                       \tag{4}
\]

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.                                \tag{5}
\]

The theorem proves the whole ratio interval in (1).  It does not infer
closure merely from the finite ranges (2)--(3).

## 2. The active-width interface bound

Put

\[
 \epsilon=1-\rho,\qquad a=\epsilon K,\qquad
 h=f-\frac14,
\]

and

\[
 g_\rho=G_1(\rho),\qquad
 W=G_K(\rho K)=K g_\rho,\qquad
 \delta=h-W>0.
\]

Every active high-floor configuration satisfies \(a>\pi h\).  Since

\[
 W=\frac{a g_\rho}{\epsilon},
\]

define

\[
 \lambda_\rho=\frac{\pi g_\rho}{\epsilon}.
\]

The active-width inequality gives

\[
 W>\lambda_\rho(W+\delta).                         \tag{6}
\]

In particular \(\lambda_\rho<1\), and hence

\[
 W>\frac{\lambda_\rho}{1-\lambda_\rho}\,\delta.
                                                               \tag{7}
\]

The ball profile has the exact integral representation

\[
 \pi g_\rho
 =\int_\rho^1\arccos x\,dx
 =\int_0^\epsilon\arccos(1-y)\,dy.                 \tag{8}
\]

Because \(\arccos(1-y)>\sqrt{2y}\) for \(y>0\),

\[
 \lambda_\rho>
 \frac{2\sqrt2}{3}\sqrt\epsilon.                  \tag{9}
\]

It is enough to treat \(\rho\leq477/500\), since Round 8B owns the
larger ratios.  Thus \(\epsilon\geq23/500\), and the exact square
comparison

\[
 \frac89\frac{23}{500}>\left(\frac15\right)^2
\]

gives

\[
 \lambda_\rho>\frac15.                            \tag{10}
\]

In the only terminal face where this new information is needed,
\(f\geq2\) and therefore

\[
 \delta=f-\frac14-W\geq\frac74-W.
\]

Combining this with (7) cancels the \(W\lambda_\rho\) terms and gives

\[
 \boxed{
 W>\frac74\lambda_\rho>
 \frac74\frac15=\frac7{20}.}                      \tag{11}
\]

This is the new ingredient of the round.

## 3. The common first-drop prefix

Retain the Round 8B notation

\[
 c=\frac{\arccos\rho}{\pi},\qquad d=1-2c,
 \qquad \widehat H(t)=A(\mu-t),
\]

and let \(M,T,\zeta\) be the shelf and endpoint-chord data defined
there.  The exact chord bound and the slope bound are

\[
 P:=R_p+\frac d2(n-p)
 \geq-\left(\frac14+\zeta\right)(T-M)
       +\frac d2(M-1),
 \qquad M\geq\frac\delta c.                        \tag{12}
\]

Directed endpoint evaluation at the new ratio gives

\[
 \rho\geq\frac{939}{1000}
 \quad\Longrightarrow\quad
 (\arccos\rho)^2<\frac{31}{250},
 \qquad c<\bar c:=\frac{14}{125}.                 \tag{13}
\]

For \(\delta\geq1\), put

\[
 \gamma=\frac3{25}-c>0.
\]

The present-level elasticity argument and the absent-level degree-\(32\)
Bernstein comparison are unchanged.  The latter still has exact
smallest coefficient \(309/396800\).  Both faces therefore have the
common strict prefix

\[
 \boxed{cP>\gamma\delta-\frac{cd}{2}.}              \tag{14}
\]

## 4. Terminal faces for \(\delta\geq1\)

Define the strict terminal counts

\[
 B_0=\left[W+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.
\]

As in Round 8B, the slope bound over \(q=\mu-\alpha\),
\(0\leq\alpha<1\), gives

\[
 B\geq B_0,\qquad Q\leq B_0+1                     \tag{15}
\]

on every strict wall.

### 4.1. The face \(B_0\geq1\)

The exact-angle terminal reserve and cap bound give

\[
 cD_A(q)>
 B_0\left(\frac12-c\right)-\frac{7c}{5}.
\]

Adding (14), using \(\delta\geq1\) and \(B_0\geq1\), and evaluating
the decreasing polynomial at \(c=14/125\), gives

\[
 \boxed{
 c\mathcal S>
 \frac{31}{50}-\frac{39}{10}c+c^2
 \geq\frac{6117}{31250}>0.}                       \tag{16}
\]

### 4.2. The face \(B_0=Q=0\)

Here \(0<W\leq3/4\), the discrete shell tail is empty, and the outer
tangent triangle gives

\[
 D_A(q)\geq\frac{W^2}{c}.
\]

Equations (14) and (11), together with
\(\delta\geq7/4-W\), imply

\[
 c\mathcal S>
 \left(\frac3{25}-c\right)\left(\frac74-W\right)
 -\frac c2+c^2+W^2.                                \tag{17}
\]

For \(W\geq7/20\), the derivative in \(W\) is

\[
 2W-\gamma>
 \frac7{10}-\frac3{25}
 =\frac{29}{50}>0.
\]

Thus the right side of (17) is minimized at the new active-width
endpoint \(W=7/20\), not at the infeasible Round 8B stationary
point \(W=\gamma/2\).  The resulting polynomial decreases for
\(0<c\leq14/125\), and

\[
 \boxed{
 c\mathcal S>
 \left(\frac3{25}-\bar c\right)
 \left(\frac74-\frac7{20}\right)
 -\frac{\bar c}{2}+\bar c^2
 +\left(\frac7{20}\right)^2
 =\frac{22561}{250000}>0.}                         \tag{18}
\]

This is the face repaired by the active-width input.  The small-\(\delta\)
ledger below is now the limiting exact margin.

### 4.3. The face \(B_0=0,Q=1\)

The Round 8B inner payment and outer tangent triangle are unchanged.
The two endpoint polynomials now give

\[
 \boxed{
 \frac{273}{400}-\frac52\bar c+\bar c^2
 =\frac{103761}{250000}>0,}                        \tag{19}
\]

\[
 \boxed{
 \frac{273}{400}-\frac{119}{50}\bar c-\bar c^2
 =\frac{100849}{250000}>0.}                        \tag{20}
\]

Hence every \(\delta\geq1\) face is positive.

## 5. Retuning the \(0<\delta<1\) certificate

The structural reduction of Round 8B is unchanged.  One has

\[
 B_0=f-1,\qquad
 W=f-\frac14-\delta>f-\frac54\geq\frac34,
 \qquad y=f-W=\delta+\frac14.
\]

It is enough to prove

\[
 \boxed{T<\frac{3y}{c}.}                           \tag{21}
\]

Scale monotonicity reduces to \(f=2\), \(W=2-y\), and concavity reduces
the remaining variable to

\[
 x=\frac yW\in\left\{\frac17,\frac53\right\}.
\]

For \(t_0=3y/c\) and \(u_0=t_0/\mu\), the trigonometric estimates used
in Round 8B now give

\[
 u_0<\frac53\frac{31/250}{939/1000}
 =\frac{620}{2817}<\frac{111}{500}<1,
 \qquad
 \frac{u_0}{1-\rho}>2x.                            \tag{22}
\]

Use

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\geq0}
 \frac{\binom{2j}{j}}{8^j(2j+1)}z^j.
\]

On the subtracted retained range,

\[
 0\leq z\leq
 \frac{61}{1000}\frac{10}{3}=\frac{61}{300}.
\]

The decreasing positive coefficients therefore give

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{45z^2}{1912},                \tag{23}
\]

because

\[
 \frac{3/160}{1-61/300}=\frac{45}{1912}.
\]

The positive first copy is used only for

\[
 z\leq\frac{61}{1000}\frac{13}{3}
 =\frac{793}{3000}<1.                              \tag{24}
\]

Writing \(\theta=\arccos\rho\), the coefficient in the exact
noncancelling identity is

\[
 C_\rho=
 \frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}.
\]

The same decreasing Taylor quotient as in Round 8B, now evaluated at

\[
 \rho=\frac{939}{1000},\qquad
 \theta^2=\frac{31}{250},
\]

has the directed lower bound

\[
 \boxed{C_\rho>\frac75.}                           \tag{25}
\]

Retain \(0\leq v\leq V=2x\).  Equations (23)--(25) reduce (21) to the
positivity of

\[
\begin{aligned}
 \mathcal I^{\mathrm C}_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)
 +\frac{1-\rho}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3(1-\rho)^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)
 -\frac23V^{3/2}-\frac{1-\rho}{30}V^{5/2}
 -\frac{45(1-\rho)^2}{6692}V^{7/2}.
\end{aligned}                                      \tag{26}
\]

The final coefficient is exactly \((45/1912)(2/7)\).  Divide

\[
 \frac{939}{1000}\leq\rho\leq\frac{477}{500}
\]

into \(64\) equal rational panels.  Directed Arb evaluation on every
full panel at \(x=1/7,5/3\) proves

\[
 \mathcal I^{\mathrm C}_\rho(2x)>0,
 \qquad
 \frac75\mathcal I^{\mathrm C}_\rho(2x)-x>0.       \tag{27}
\]

Across runs at \(384,512,768,\) and \(1024\) bits, the smallest lower
bounds are

\[
 \mathcal I^{\mathrm C}_\rho(2x)>0.2037628652,
 \qquad
 \frac75\mathcal I^{\mathrm C}_\rho(2x)-x
 >0.0456615050.                                    \tag{28}
\]

Concavity proves (21) for the whole interval of \(x\).  The remaining
prefix and terminal calculation from Round 8B gives

\[
 \boxed{
 c\mathcal S>
 \frac5{16}-\frac{29}{10}c+c^2
 \geq\frac{61}{250000}>0.}                        \tag{29}
\]

Equations (16), (18)--(20), and (29), together with the Round 8B band
at and above \(477/500\), prove (1).

## 6. Improved residual cutoff

For a residual ratio \(\rho<939/1000\), put

\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.
\]

Monotonicity and directed endpoint evaluation give

\[
 \eta_\rho>\frac1{221},\qquad
 \eta_\rho<\frac19.                               \tag{30}
\]

Also

\[
 a_\rho<2\frac{355}{113}\frac{939}{61}
 =\frac{666690}{6893}.                             \tag{31}
\]

Since \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{666690}{6893}+\frac{13}{45}
 =\frac{30090659}{310185}<98.                     \tag{32}
\]

Because \(C_*>1/2\), the square root in the fixed-ratio threshold is
smaller than the same expression on the left of (32).  Hence

\[
 \boxed{
 K_0(\rho)<98\cdot221^2=4\,786\,418.}             \tag{33}
\]

Negativity excludes \(p=0\), so \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\).  Since \(r\geq1/2\), (33) gives

\[
 \rho>\frac1{2\cdot4\,786\,418}
 =\frac1{9\,572\,836},
\]

\[
 2r\leq9\,572\,835,
 \qquad n\leq4\,786\,417.
\]

Finally \(A(r)\geq7/4\) gives (4) and \(K>21/4\), while \(\pi>3\)
gives

\[
 f,B<\frac K3+\frac14
 <1\,595\,472+\frac{11}{12}.
\]

The exact integer consequences are (2)--(3).

## 7. Reproducibility and remaining obligation

The verifier is

    scripts/general_d_high_floor_active_width_verify.py

It reconstructs the degree-\(32\) Bernstein minimum, the exact
active-width comparison, all five terminal ledgers, the retuned series
coefficients, all \(128\) full-panel endpoint evaluations, the residual
cutoff, and the integer ranges.  Directed runs at \(384,512,768,\) and
\(1024\) bits all pass.

This round strictly reduces the unresolved high-floor compact region to

\[
 \frac1{9\,572\,836}<\rho<\frac{939}{1000},
 \qquad \frac{21}{4}<K<4\,786\,418.
\]

No claim is made here that those remaining walls have been certified.
