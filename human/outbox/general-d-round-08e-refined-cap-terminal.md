# General dimension, Round 8E: refined cap and absent-level chord

Date: 2026-07-18  
Scope: high-floor first-drop configurations \(F_0=f\geq2\), \(p<n\)  
Status: analytic ratio certificate with directed interval replay  
Depends on: Rounds 7, 8A, 8B, 8C, and 8D

Round 8D reached \(\rho=93/100\).  Two small refinements extend the
certified ratio band to

\[
 \boxed{\rho\geq\frac{927}{1000}}.
\]

First, a negative candidate cannot have \(p=0\).  Therefore its terminal
start satisfies \(q\geq5/2\), and the sharp terminal cap improves from
\(1/5\) to \(1/6\).  Second, the absent-level chord coefficient can be
improved from \(19/50\) to \(377/1000\) by an exact polynomial
certificate.  The resulting common first-drop coefficient is
\(123/1000-c\), which stays positive on the new band.

This round certifies a ratio interval.  It does not certify any residual
wall below \(927/1000\).

## 1. Result

### Theorem 1 (refined-cap high-floor exclusion)

In the high-floor first-drop branch, suppose

\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{927}{1000}\leq\rho<1.
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
 \frac1{4\,626\,882}<\rho<\frac{927}{1000},\qquad
 \frac{21}{4}<K<2\,313\,441,}                         \tag{2}
\]

and

\[
 \boxed{
 \begin{gathered}
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq4\,626\,881,\\
 2\leq n\leq2\,313\,440,\qquad
 1\leq p\leq n-1,\\
 2\leq f\leq771\,147,\\
 0\leq Q\leq f-1,\qquad Q\leq B\leq771\,147.
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

The theorem does not infer closure merely from the finite ranges
(2)--(3).

## 2. Removing \(p=0\) and sharpening the terminal cap

If \(p=0\), then \(R_0=0\), and the completed one-interface theorem
gives

\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0.
\]

Thus a negative candidate must have \(p\geq1\).  Since \(p<n\), it has
\(n\geq2\), and therefore

\[
 q=r+n\geq\frac52.                                   \tag{6}
\]

### Lemma 2 (refined terminal cap)

If \(q\geq5/2\) and \(q\leq\mu<q+1\), then

\[
 \boxed{2\int_q^\mu G_\mu(z)\,dz<\frac16.}          \tag{7}
\]

#### Proof

There is nothing to prove when \(q=\mu\).  Otherwise strict convexity
of \(G_\mu\), together with \(G_\mu(\mu)=0\), gives

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_\mu(q)(\mu-q)<G_{q+1}(q).                       \tag{8}
\]

For \(H(q)=G_{q+1}(q)\), put \(q/(q+1)=\cos\vartheta\).  As in Round
8D,

\[
 H'(q)=\frac{\sin\vartheta-\vartheta}{\pi}<0.
\]

Hence

\[
 G_{q+1}(q)\leq G_{7/2}(5/2)<\frac16,               \tag{9}
\]

where the last strict comparison is directed Arb arithmetic.  This
proves (7), including the phase \(q=\mu\).  \(\square\)

## 3. A sharper absent-level chord

Retain the Round 8B notation

\[
 c=\frac{\arccos\rho}{\pi},\qquad d=1-2c,\qquad
 W=G_K(\mu),\qquad h=f-\frac14,\qquad \delta=h-W.
\]

When level \(f\) is absent, write

\[
 a=\frac14-\zeta\in[0,1/4].
\]

The elasticity estimate and \(\delta\geq1\) reduce the endpoint-chord
coefficient to

\[
 L(a)=\left(\frac12-a\right)
 \left(r_*(1+a)-1\right),                            \tag{10}
\]

where

\[
 r_*(1+a)-1=2a+a^2+(1+a)\sqrt{a(2+a)}.
\]

### Lemma 3 (refined absent-level coefficient)

For \(0\leq a\leq1/4\),

\[
 \boxed{L(a)<\frac{377}{1000}.}                     \tag{11}
\]

#### Proof

Put

\[
 b(a)=\frac{377}{1000}
      -\left(\frac12-a\right)(2a+a^2)
 =\frac{377}{1000}-a+\frac32a^2+a^3.
\]

Its derivative is negative on \([0,1/4]\), and

\[
 b(1/4)=\frac{1891}{8000}>0.                         \tag{12}
\]

An exact expansion gives

\[
\begin{aligned}
 &b(a)^2-\left(\frac12-a\right)^2(1+a)^2a(2+a)\\
 &\quad=
 \frac{142129}{10^6}-\frac{627}{500}a
 +\frac{2881}{1000}a^2-\frac{123}{500}a^3-a^4.
                                                               \tag{13}
\end{aligned}
\]

After \(a=y/4\), every coefficient in its degree-\(48\) Bernstein
representation on \(0\leq y\leq1\) is positive.  The exact smallest
coefficient is

\[
 \frac{7422203}{77832000000}>0.                     \tag{14}
\]

Equations (12)--(14) make the squaring step sign-safe and prove (11).
\(\square\)

Define

\[
 \beta=\frac{123}{1000}-c.                          \tag{15}
\]

If level \(f\) is present, the Round 8B elasticity estimate gives

\[
 cP\geq\left(\frac18-c\right)\delta-\frac{cd}{2}
 >\beta\delta-\frac{cd}{2}.                         \tag{16}
\]

If it is absent, Lemma 3 gives

\[
 P>\left(\frac d2-\frac{377}{1000}\right)M-\frac d2
   =\beta M-\frac d2.
\]

Whenever \(\beta>0\), the slope bound \(M\geq\delta/c\) therefore
gives the same strict estimate.  Thus both faces have the common prefix

\[
 \boxed{cP>\beta\delta-\frac{cd}{2}.}                \tag{17}
\]

## 4. Ratio and active-width constants

Round 8D owns \(\rho\geq93/100\), so it remains to treat

\[
 \frac{927}{1000}\leq\rho\leq\frac{93}{100}.
\]

Directed evaluation at the lower endpoint gives

\[
 (\arccos\rho)^2<\frac{37}{250},\qquad
 c<\bar c:=\frac{49}{400}<\frac{123}{1000}.         \tag{18}
\]

In particular \(\beta>0\).  Put \(\epsilon=1-\rho\) and

\[
 \lambda_\rho=\frac{\pi G_1(\rho)}{1-\rho}.
\]

The active-width argument from Round 8C gives

\[
 \lambda_\rho>\frac{2\sqrt2}{3}\sqrt\epsilon.
\]

On the present band \(\epsilon\geq7/100\), and the exact comparison

\[
 \frac89\frac7{100}-\left(\frac{249}{1000}\right)^2
 =\frac{1991}{9000000}>0
\]

therefore gives \(\lambda_\rho>249/1000\).  Since

\[
 W>\lambda_\rho(W+\delta),\qquad
 W+\delta=f-\frac14\geq\frac74,
\]

we obtain the strict interface-height bound

\[
 \boxed{W>\frac74\frac{249}{1000}
       =\frac{1743}{4000}.}                          \tag{19}
\]

## 5. The faces \(\delta\geq1\)

Use the strict terminal counts

\[
 B_0=\left[W+\frac14\right]_<,\qquad
 B=\left[G_K(q)+\frac14\right]_<,\qquad
 Q=\left[A(q)+\frac14\right]_<.
\]

As before,

\[
 B\geq B_0,\qquad Q\leq B_0+1.                     \tag{20}
\]

### 5.1. The face \(B_0\geq1\)

The exact-angle reserve, (20), and Lemma 2 give

\[
 cD_A(q)>
 B_0\left(\frac12-c\right)-\frac{7c}{6}.           \tag{21}
\]

Use \(B_0\geq1\), \(\delta\geq1\), and (17).  The resulting
polynomial decreases on \(0<c\leq\bar c\), and

\[
 \boxed{
 c\mathcal S>
 \frac{623}{1000}-\frac{11}{3}c+c^2
 \geq\frac{90643}{480000}>0.}                      \tag{22}
\]

### 5.2. The face \(B_0=Q=0\)

The shell discrete tail is empty, and the outer tangent triangle gives

\[
 cD_A(q)\geq W^2.
\]

Since \(\delta\geq7/4-W\), equations (17) and (19) give

\[
 c\mathcal S>
 \beta\left(\frac74-W\right)-\frac c2+c^2+W^2.
                                                               \tag{23}
\]

The derivative in \(W\) is \(2W-\beta>0\) throughout the admissible
range.  The right side also decreases in \(c\).  Its lower endpoint is
therefore obtained from \(W=1743/4000\) and \(c=49/400\):

\[
 \boxed{c\mathcal S>\frac{2308663}{16000000}>0.}     \tag{24}
\]

### 5.3. The face \(B_0=0,Q=1\)

Here

\[
 \frac34-c<W\leq\frac34
\]

and the inner payment plus outer tangent triangle gives

\[
 cD_A(q)>\frac32W-W^2-c.
\]

Together with (17) and \(\delta\geq7/4-W\), the resulting expression is
concave in \(W\), so its minimum over the closed endpoint interval is at
one of its endpoints.  The two decreasing endpoint polynomials give

\[
 \boxed{
 W=\frac34:\quad
 c\mathcal S>
 \frac{1371}{2000}-\frac52c+c^2
 \geq\frac{63081}{160000}>0,}                       \tag{25}
\]

\[
 \boxed{
 W=\frac34-c:\quad
 c\mathcal S>
 \frac{1371}{2000}-\frac{2377}{1000}c-c^2
 \geq\frac{303449}{800000}>0.}                     \tag{26}
\]

Thus every \(\delta\geq1\) terminal face is strictly positive,
including all strict-count walls.

## 6. The face \(0<\delta<1\)

The scale and concavity reductions from Round 8D remain valid.  It is
enough to prove

\[
 T<\frac{3y}{c},\qquad y=f-W=\delta+\frac14,         \tag{27}
\]

at \(f=2\) and at

\[
 x=\frac yW\in\left\{\frac17,\frac53\right\}.
\]

For \(t_0=3y/c\), \(u_0=t_0/\mu\), equation (18) gives

\[
 u_0<\frac53\frac{37/250}{927/1000}
     =\frac{740}{2781}<\frac{267}{1000}<1,
 \qquad \frac{u_0}{1-\rho}>2x.                     \tag{28}
\]

Use

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\geq0}
 \frac{\binom{2j}{j}}{8^j(2j+1)}z^j.
\]

On the subtracted retained range,

\[
 0\leq z\leq\frac{73}{1000}\frac{10}{3}
 =\frac{73}{300}.
\]

The decreasing positive coefficients give

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{45z^2}{1816},                 \tag{29}
\]

because

\[
 \frac{3/160}{1-73/300}=\frac{45}{1816}.
\]

The positive first copy is used only for

\[
 z\leq\frac{73}{1000}\frac{13}{3}
 =\frac{949}{3000}<1.                               \tag{30}
\]

The same decreasing Taylor quotient as in Round 8D, evaluated at
\(\rho=927/1000\) and \(\theta^2=37/250\), gives

\[
 \boxed{
 C_\rho=\frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}>\frac{173}{125}.}    \tag{31}
\]

For \(V=2x\), retain \(0\leq v\leq V\).  The directed lower integral is

\[
\begin{aligned}
 \mathcal I^{\mathrm E}_\rho(V)
={}&\frac{2}{3\rho}
 \left((1+\rho V)^{3/2}-1\right)
 +\frac{1-\rho}{30\rho}
 \left((1+\rho V)^{5/2}-1\right)\\
&+\frac{3(1-\rho)^2}{560\rho}
 \left((1+\rho V)^{7/2}-1\right)
 -\frac23V^{3/2}-\frac{1-\rho}{30}V^{5/2}\\
&-\frac{45(1-\rho)^2}{6356}V^{7/2}.
                                                               \tag{32}
\end{aligned}
\]

The last coefficient is exactly \((45/1816)(2/7)\).  Divide
\([927/1000,93/100]\) into \(64\) equal rational panels.  Directed Arb
evaluation on every full panel at both endpoint values of \(x\) proves

\[
 \mathcal I^{\mathrm E}_\rho(2x)>0,
 \qquad
 \frac{173}{125}\mathcal I^{\mathrm E}_\rho(2x)-x>0. \tag{33}
\]

Across runs at \(384,512,768,\) and \(1024\) bits, the smallest lower
bounds are

\[
 \mathcal I^{\mathrm E}_\rho(2x)>0.2040442323,
\]

\[
 \frac{173}{125}\mathcal I^{\mathrm E}_\rho(2x)-x
 >0.0085053826.                                     \tag{34}
\]

Concavity proves (27) throughout the interval of \(x\).  Hence

\[
 cP>-c-\frac3{16}-\frac{cd}{2}.                     \tag{35}
\]

Here \(B_0=f-1\), \(Q\leq f-1\), and Lemma 2 improves the terminal
reserve to

\[
 cD_A(q)>
 \frac{f-1}{2}-c(f-1)-\frac c6
 \geq\frac12-\frac{7c}{6}.                         \tag{36}
\]

Adding (35)--(36) gives

\[
 c\mathcal S>
 \frac5{16}-\frac83c+c^2.
\]

This decreases on the certified interval, and at \(c=\bar c\),

\[
 \boxed{c\mathcal S>\frac{403}{480000}>0.}          \tag{37}
\]

Equations (22), (24)--(26), and (37), together with Round 8D above
\(93/100\), prove (1).

## 7. Improved residual cutoff

For a residual ratio \(\rho<927/1000\), put

\[
 \eta_\rho=G_1(\max\{\rho,1/2\}),\qquad
 a_\rho=\frac{2\pi\rho}{1-\rho}.
\]

Directed endpoint evaluation and monotonicity give

\[
 \eta_\rho>\frac1{169},\qquad \eta_\rho<\frac19.   \tag{38}
\]

Also

\[
 a_\rho<2\frac{355}{113}\frac{927}{73}
 =\frac{658170}{8249}.                              \tag{39}
\]

Since \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{658170}{8249}+\frac{13}{45}
 =\frac{29724887}{371205}<81.                       \tag{40}
\]

The fixed-ratio threshold is

\[
 K_0(\rho)=
 \frac{a_\rho+2\eta_\rho C_*
 +\sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}}
 {2\eta_\rho^2}.
\]

Because \(C_*>1/2\), the square root is smaller than
\(a_\rho+2\eta_\rho C_*\).  Equations (38)--(40) therefore give

\[
 \boxed{K_0(\rho)<81\cdot169^2=2\,313\,441.}        \tag{41}
\]

Negativity excludes \(p=0\), so \(p\geq1\), \(n\geq2\), and
\(r<\mu<K\).  Since \(r\geq1/2\), (41) gives

\[
 \rho>\frac1{4\,626\,882},\qquad
 2r\leq4\,626\,881,\qquad
 n\leq2\,313\,440.
\]

Finally \(A(r)\geq7/4\) gives \(K-\mu>7\pi/4\) and \(K>21/4\), while
\(\pi>3\) gives

\[
 f,B<\frac K3+\frac14<771\,147+\frac14.
\]

These are exactly (2)--(5).

## 8. Reproducibility and remaining obligation

The directed verifier is

    scripts/general_d_high_floor_refined_cap_verify.py

It checks the frozen Round 8D verifier hash, the degree-\(48\) absent
chord certificate, the active-width comparison, the refined cap
\(G_{7/2}(5/2)<1/6\), both ratio endpoint bounds, the retuned arccos
series, all \(128\) full-panel endpoint evaluations, the five terminal
ledgers, the fixed-ratio cutoff, and the integer ranges.

The remaining high-floor compact region is now

\[
 \boxed{
 \frac1{4\,626\,882}<\rho<\frac{927}{1000},\qquad
 \frac{21}{4}<K<2\,313\,441.}
\]

No wall in this residual box is claimed certified by this round.
