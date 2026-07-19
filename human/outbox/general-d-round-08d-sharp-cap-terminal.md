# General dimension, Round 8D: the sharp terminal cap

Date: 2026-07-18  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: analytic ratio certificate with directed interval replay  
Depends on: Rounds 7, 8A, 8B, and 8C

Round 8C used the active-width relation to remove the zero-count
terminal obstruction.  The limiting margin then moved to the
\(0<\delta<1\) face.  This round reuses a sharper cap estimate already
implicit in the terminal geometry:

\[
 2\int_q^\mu G_\mu(z)\,dz<\frac15
 \qquad(q\geq3/2,\ q\leq\mu<q+1).
\]

It extends the certified high-floor ratio band to

\[
 \boxed{\rho\geq\frac{93}{100}}.
\]

The remaining fixed-ratio walls below \(93/100\) are not certified here.

## 1. Result

### Theorem 1 (sharp-cap high-floor exclusion)

In the high-floor first-drop branch, suppose

\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{93}{100}\leq\rho<1.
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
 \frac1{5\,443\,200}<\rho<\frac{93}{100},\qquad
 \frac{21}{4}<K<2\,721\,600,}                         \tag{2}
\]

and

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq5\,443\,199,\\
 2\leq n\leq2\,721\,599,\qquad
 1\leq p\leq n-1,\\
 2\leq f\leq907\,200,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq907\,200.
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
 A(r+p+1)<f-\frac14.                                \tag{5}
\]

The theorem certifies a ratio interval.  It does not infer closure from
the finiteness of (2)--(3).

## 2. A sharp cap at the terminal start

Since \(p<n\), one has \(n\geq1\).  Together with \(r\geq1/2\), this
gives \(q=r+n\geq3/2\), including the face \(p=0\).

### Lemma 2 (sharp terminal cap)

If \(q\geq3/2\) and \(q\leq\mu<q+1\), then

\[
 \boxed{
 2\int_q^\mu G_\mu(z)\,dz<\frac15.}                 \tag{6}
\]

#### Proof

The claim is immediate when \(q=\mu\).  Otherwise, strict convexity of
\(G_\mu\) on \([q,\mu]\), with endpoint value zero at \(\mu\), gives

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_\mu(q)(\mu-q)<G_{q+1}(q).                      \tag{7}
\]

Put \(H(q)=G_{q+1}(q)\), \(u=q/(q+1)=\cos\theta\).  Direct
differentiation in the radius and spatial variables gives

\[
 H'(q)=\frac{\sin\theta-\theta}{\pi}<0.             \tag{8}
\]

Hence

\[
 G_{q+1}(q)\leq G_{5/2}(3/2)<\frac15.              \tag{9}
\]

The final strict inequality is a directed Arb comparison.  This proves
(6), including the endpoint phase \(q=\mu\).  \(\square\)

## 3. The band \(93/100\leq\rho\leq477/500\)

Round 8B owns every larger ratio, so it remains to treat

\[
 \frac{93}{100}\leq\rho\leq\frac{477}{500}.
\]

Retain its notation

\[
 c=\frac{\arccos\rho}{\pi},\qquad d=1-2c,\qquad
 W=G_K(\mu),\qquad h=f-\frac14,\qquad
 \delta=h-W.
\]

Directed evaluation at the new lower endpoint gives

\[
 (\arccos\rho)^2<\frac{71}{500},\qquad
 c<\bar c:=\frac{1199}{10000}<\frac3{25}.          \tag{10}
\]

The active-width lemma from Round 8C applies on this whole interval and
gives

\[
 \boxed{W>\frac7{20}.}                              \tag{11}
\]

For \(\delta\geq1\), the present- and absent-level faces still have the
common endpoint-chord prefix

\[
 \boxed{
 cP>
 \left(\frac3{25}-c\right)\delta-\frac{cd}{2}.}     \tag{12}
\]

The absent face uses exactly the same degree-\(32\) Bernstein comparison,
whose smallest coefficient is \(309/396800\).

### 3.1. Terminal faces when \(\delta\geq1\)

The terminal stratification of Round 8C is unchanged.  Its four endpoint
polynomials decrease on \(0<c\leq\bar c\); the zero-count polynomial is
increasing in \(W\geq7/20\).  At \(c=\bar c\) the exact ledgers are

\[
 \boxed{
 B_0\geq1:\quad
 c\mathcal S>
 \frac{16676601}{100000000}>0,}                    \tag{13}
\]

\[
 \boxed{
 B_0=Q=0:\quad
 c\mathcal S>
 \frac{7706601}{100000000}>0,}                     \tag{14}
\]

\[
 \boxed{
 B_0=0,\ Q=1,\ W=\frac34:\quad
 c\mathcal S>
 \frac{39712601}{100000000}>0,}                    \tag{15}
\]

\[
 \boxed{
 B_0=0,\ Q=1,\ W=\frac34-c:\quad
 c\mathcal S>
 \frac{38276199}{100000000}>0.}                    \tag{16}
\]

These are respectively the Round 8C polynomials

\[
 \frac{31}{50}-\frac{39}{10}c+c^2,
\]

\[
 \left(\frac3{25}-c\right)
 \left(\frac74-\frac7{20}\right)
 -\frac c2+c^2+\left(\frac7{20}\right)^2,
\]

\[
 \frac{273}{400}-\frac52c+c^2,\qquad
 \frac{273}{400}-\frac{119}{50}c-c^2.
\]

Thus every \(\delta\geq1\) face remains strictly positive, including
the walls \(W=3/4\), \(A(q)=3/4\), and \(\delta=1\).

## 4. Retuning the \(0<\delta<1\) level distance

The scale and concavity reductions from Round 8C remain valid.  It is
enough to prove

\[
 \boxed{T<\frac{3y}{c}},
 \qquad y=f-W=\delta+\frac14,                       \tag{17}
\]

at \(f=2\) and at

\[
 x=\frac yW\in\left\{\frac17,\frac53\right\}.
\]

For \(t_0=3y/c\), \(u_0=t_0/\mu\), the endpoint bounds in (10) give

\[
 u_0<
 \frac53\frac{71/500}{93/100}
 =\frac{71}{279}<\frac{51}{200}<1,\qquad
 \frac{u_0}{1-\rho}>2x.                            \tag{18}
\]

Use

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\geq0}
 \frac{\binom{2j}{j}}{8^j(2j+1)}z^j.
\]

On the subtracted retained range,

\[
 0\leq z\leq\frac7{100}\frac{10}{3}=\frac7{30}.
\]

The decreasing positive coefficients give

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{9z^2}{368},                  \tag{19}
\]

because

\[
 \frac{3/160}{1-7/30}=\frac9{368}.
\]

The positive first copy is used only for

\[
 z\leq\frac7{100}\frac{13}{3}=\frac{91}{300}<1.   \tag{20}
\]

The decreasing Taylor quotient in the noncancelling integral identity,
evaluated at

\[
 \rho=\frac{93}{100},\qquad \theta^2=\frac{71}{500},
\]

gives

\[
 \boxed{
 C_\rho=
 \frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}>
 \frac{1389}{1000}.}                               \tag{21}
\]

Retaining \(0\leq v\leq V=2x\) gives

\[
\begin{aligned}
 \mathcal I^{\mathrm D}_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)
 +\frac{1-\rho}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3(1-\rho)^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)
 -\frac23V^{3/2}-\frac{1-\rho}{30}V^{5/2}
 -\frac{9(1-\rho)^2}{1288}V^{7/2}.
\end{aligned}                                      \tag{22}
\]

The last coefficient is exactly \((9/368)(2/7)\).  Divide
\([93/100,477/500]\) into \(64\) equal rational panels.  Directed
evaluation on each full panel at \(x=1/7,5/3\) proves

\[
 \mathcal I^{\mathrm D}_\rho(2x)>0,\qquad
 \frac{1389}{1000}\mathcal I^{\mathrm D}_\rho(2x)-x>0.       \tag{23}
\]

Across runs at \(384,512,768,\) and \(1024\) bits, the smallest lower
bounds are

\[
 \mathcal I^{\mathrm D}_\rho(2x)>0.2037148927,
\]

\[
 \frac{1389}{1000}\mathcal I^{\mathrm D}_\rho(2x)-x
 >0.0162868443.                                    \tag{24}
\]

Concavity proves (17) for the whole interval of \(x\).

## 5. Sharp-cap payment on the small-\(\delta\) face

Level \(f\) is present.  The endpoint-chord calculation and (17) give

\[
 cP>-c-\frac3{16}-\frac{cd}{2}.                    \tag{25}
\]

Here

\[
 B_0=f-1,\qquad Q\leq f-1,
\]

and each of the first \(f-1\) ball angles is smaller than
\(\theta=\pi c\).  The exact-angle reserve and Lemma 2 therefore give

\[
\begin{aligned}
 cD_A(q)
 &>\frac{f-1}{2}-c(f-1)-\frac c5\\
 &\geq\frac12-\frac{6c}{5}.
\end{aligned}                                      \tag{26}
\]

Adding (25), using \(d=1-2c\), gives the improved polynomial

\[
 c\mathcal S>
 \frac5{16}-\frac{27}{10}c+c^2.                  \tag{27}
\]

It decreases on the certified interval.  At \(c=\bar c\),

\[
 \boxed{
 c\mathcal S>
 \frac{314601}{100000000}>0.}                     \tag{28}
\]

Equations (13)--(16) and (28), together with Round 8B at and above
\(477/500\), prove (1).

## 6. Improved residual cutoff

For a residual ratio \(\rho<93/100\), put

\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.
\]

Directed endpoint evaluation and monotonicity give

\[
 \eta_\rho>\frac1{180},\qquad \eta_\rho<\frac19.   \tag{29}
\]

Moreover

\[
 a_\rho<
 2\frac{355}{113}\frac{93}{7}
 =\frac{66030}{791}.                               \tag{30}
\]

Since \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{66030}{791}+\frac{13}{45}
 =\frac{2981633}{35595}<84.                       \tag{31}
\]

As in Rounds 8B--8C, \(C_*>1/2\) makes the square root in the
fixed-ratio threshold smaller than the same left side.  Hence

\[
 \boxed{
 K_0(\rho)<84\cdot180^2=2\,721\,600.}              \tag{32}
\]

Since a negative candidate has \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\), with \(r\geq1/2\), this gives

\[
 \rho>\frac1{5\,443\,200},\qquad
 2r\leq5\,443\,199,\qquad
 n\leq2\,721\,599.
\]

Finally \(A(r)\geq7/4\) gives \(K-\mu>7\pi/4\) and \(K>21/4\), while
\(\pi>3\) gives

\[
 f,B<\frac K3+\frac14<907\,200+\frac14.
\]

These are exactly (2)--(5).

## 7. Reproducibility and remaining obligation

The directed verifier is

    scripts/general_d_high_floor_sharp_cap_verify.py

It checks the frozen Round 8C helper hash, the cap
\(G_{5/2}(3/2)<1/5\), both ratio endpoint bounds, the Bernstein
coefficient, the active-width ledger, the retuned arccos series, all
\(128\) full-panel endpoint evaluations, the five exact terminal
polynomials, the fixed-ratio cutoff, and the integer ranges.

The remaining high-floor compact region is now

\[
 \boxed{
 \frac1{5\,443\,200}<\rho<\frac{93}{100},\qquad
 \frac{21}{4}<K<2\,721\,600.}
\]

No wall in this residual box is claimed certified by this round.
