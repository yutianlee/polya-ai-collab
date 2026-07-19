# General dimension, Round 35: analytic closure of the lower-\(Q\) hard sector

Date: 19 July 2026  
Status: the lower-\(Q\), high-floor, first-drop hard sector is closed

## 0. Statement and theorem boundary

This note follows
`human/inbox/general-d_simplified_analytic_strategy.md`.  It introduces no
shell-ratio owner, chamber decomposition, empirical constant, or interval
certificate.  The only subdivisions are the intrinsic phase ranges needed
for three different analytic estimates.

Use the normalized variables of Round 34:

\[
 0<t<\frac\pi2,\qquad c=\cos t,\qquad
 d=1-\frac{2t}{\pi},
\]

\[
 z=\frac r\mu,\qquad P=\frac p\mu,
 \qquad M=\frac m\mu,qquad X=z+P,qquad Q=X+M<1.
\]

On the lower-\(Q\), high-floor, first-drop hard sector,

\[
 f\geq2,qquad P>dM,qquad
 E_*:=\frac{P-dM}{2P}>0.
\tag{0.1}
\]

### Theorem 0.1 (lower-\(Q\) hard-sector closure)

Every admissible tuple in this sector satisfies

\[
 \boxed{\Delta>E_*.}
\tag{0.2}
\]

Consequently the lower-\(Q\) hard sector is empty.

The proof has three analytic phase modules:

\[
 \begin{array}{c|c}
 0<t\leq\pi/8 & \text{exact adjacent-action theorem},\\
 \pi/8\leq t\leq\pi/6 & \text{correlated quadrature estimate},\\
 \pi/6\leq t<3\pi/14 & \text{face boundary and stationary estimate}.
 \end{array}
\tag{0.3}
\]

The transported domain is empty for \(t\geq3\pi/14\).  The overlaps in
(0.3) are intentional and include both phase endpoints.

This closes one genuine endpoint family inside high-floor CST.  It does not
close the remaining \(\alpha\)-faces, higher inverse/count bands, or
simultaneous inverse/outer-\(B\) collisions.  Thus high-floor CST,
pointwise assembly, and the all-dimensional theorem remain open.

## 1. Dependencies and the Round 34 face

Only the following proved inputs are used.

1. Round 34 transports every counterexample to the one-sided face
   \(Q\to1^-\), while preserving \((t,z,\rho)\), where \(\rho=M/P\).
2. On that face,
   \[
    P=X-z,\qquad M=1-X,
   \]
   and
   \[
    D_1(t,X)=u(X)+\frac{v(X)-\sin t}{c^2}
    =u(X)+\frac{u(X)^2}{v(X)+\sin t},
   \tag{1.1}
   \]
   where
   \[
    u(y)=\sqrt{1-y^2},\qquad
    v(y)=\sqrt{1-c^2y^2}.
   \]
3. Put
   \[
    a^2=\frac{1+c+c^2}{3},\qquad
    b(y)=\sqrt{1-a^2y^2}.
   \]
   The face residual is
   \[
    \mathcal R(t,z,X)=
    \frac{2\{b(z)-b(X)\}}{a^2D_1(t,X)}
    -\frac{(1+d)X-z-d}{2(X-z)}.
   \tag{1.2}
   \]
4. The exact face domain is
   \[
    z>z_0(t):=\frac{4(\tan t-t)}{3\pi},
    \qquad X_h(t,z)<X<X_D(t),
   \tag{1.3}
   \]
   where
   \[
    X_h(t,z)=\frac{z+d}{1+d},
   \]
   and \(X_D\) is characterized by
   \[
    D_1(t,X_D)=D_0(t),\qquad
    D_0(t)=\frac{8(\tan t-t)}{3(1-\cos t)}.
   \tag{1.4}
   \]
   If the root-existence condition for \(X_D\) fails, the domain is empty.
5. For fixed \((t,X)\), Round 34 reduces the \(z\)-minimum to
   \(z=z_0\), the automatic hard boundary, or the possible second root of
   \[
    \frac{z(X-z)^2}{b(z)}
    =\frac{d(1-X)D_1}{4}.
   \tag{1.5}
   \]
   At a stationary root the residual is
   \[
    \mathcal R_{\rm stat}=
    \frac2{D_1}
    \left\{
      \frac{b(z)-b(X)}{a^2}
      +\frac{z(X-z)}{b(z)}
    \right\}-\frac12.
   \tag{1.6}
   \]

The small-phase theorem in
`human/outbox/general-d-lower-Q-small-phase-adjacent-action-closure.md`
already proves (0.2) for \(0<t\leq\pi/8\).  It remains to treat the last
two ranges in (0.3).

## 2. Middle phase: \(\pi/8\leq t\leq\pi/6\)

This section proves \(\mathcal R>0\) directly on the full face domain.  It
does not use the stationary split.

### 2.1 Safe correlated bounds

Throughout this range,

\[
 d\geq\frac23,qquad
 z>\frac1{125},qquad
 a^2> A:=\frac{87}{100}.
\tag{2.1}
\]

For the radius bound, monotonicity of \(z_0\) and the elementary estimates
\(\sqrt2>140/99\), \(\pi<22/7\) give

\[
 z_0(t)\geq z_0(\pi/8)
 >\frac{59}{6534}>\frac1{125}.
\tag{2.2}
\]

The last inequality in (2.1) follows from

\[
 a^2\geq\frac7{12}+\frac{\sqrt3}{6}
 >\frac{87}{100}.
\tag{2.3}
\]

Let \(u=u(X)\).  Since \(v\geq u\), \(\sin t>3/8\), and hence
\(v+\sin t>3/8+9u/10\), (1.1) gives

\[
 D_1<B(u):=\frac{u(15+76u)}{15+36u}.
\tag{2.4}
\]

The action constraint also forces

\[
 \boxed{X<\frac78.}
\tag{2.5}
\]

Indeed, \(D_1\) decreases in both \(t\) and \(X\), while \(D_0\)
increases in \(t\).  At \(t=\pi/8\), \(X=7/8\),

\[
 u<\frac{31}{64},\qquad v>\frac{47}{80},
\]

so

\[
 D_1<\frac{3587}{4928}<\frac{73}{100}.
\tag{2.6}
\]

On the other hand, the same rational Taylor bounds give

\[
 D_0(\pi/8)>
 \frac{590000}{792099}>\frac{37}{50}.
\tag{2.7}
\]

Equations (2.6)--(2.7) contradict \(D_1>D_0\) when \(X\geq7/8\).

### 2.2 A retained quadrature lower bound

Put

\[
 p=X-z,qquad M=1-X,qquad
 G=3p-2M=5X-3z-2,
\tag{2.8}
\]

and

\[
 \kappa(X)=1+\frac{AX^2}{4}+\frac{A^2X^4}{8}.
\tag{2.9}
\]

The binomial inequality

\[
 \frac1{\sqrt{1-w}}
 \geq1+\frac w2+\frac{3w^2}{8}
 \qquad(0\leq w<1)
\]

and \(a^2>A\) imply

\[
 \begin{aligned}
 N&:=\int_z^X\frac{y\,dy}{b(y)}\\
 &\geq \Phi(X)-\Phi(z)\\
 &\geq\frac{p(X+z)}2\,\kappa(X),
 \end{aligned}
\tag{2.10}
\]

where

\[
 \Phi(y)=\frac{y^2}{2}+\frac{Ay^4}{8}+\frac{A^2y^6}{16}.
\]

Since the first term in (1.2) is \(2N/D_1\), (2.4) and (2.10) give

\[
 C:=\frac{2N}{D_1}
 >\frac{p(X+z)\kappa(X)}{B(u)}.
\tag{2.11}
\]

Also, \(d\geq2/3\) gives

\[
 E_*=\frac{p-dM}{2p}
 \leq\frac{G}{6p}.
\tag{2.12}
\]

Thus it suffices to prove

\[
 H:=6\kappa(X)p^2(X+z)-B(u)G>0.
\tag{2.13}
\]

The hard sector itself has \(G>0\).  We retain this correlation below.

### 2.3 The range \(X\leq3/5\)

Differentiation gives

\[
 H_z=3B(u)-6\kappa(X)p(X+3z).
\tag{2.14}
\]

For \(0<z<X\),

\[
 p(X+3z)\leq\frac{4X^2}{3}\leq\frac{12}{25}.
\]

Using

\[
 \kappa(3/5)=\frac{54528089}{50000000},
 \qquad
 B(4/5)=\frac{1516}{1095},
\]

we obtain the exact positive margin

\[
 H_z\geq
 \frac{11550045527}{11406250000}>0.
\tag{2.15}
\]

Hence the adverse radius is \(s:=1/125\).  Since \(G>0\), this range also
has

\[
 X>\ell:=\frac{253}{625}.
\tag{2.16}
\]

Use the binomial upper polynomial

\[
 U(X)=1-\frac{X^2}{2}-\frac{X^4}{8}
      -\frac{X^6}{16}-\frac{5X^8}{128}>u(X).
\tag{2.17}
\]

Because \(B\) is increasing, (2.13) follows from positivity of the rational
polynomial

\[
 \begin{aligned}
 P(X)={}&6(X-s)^2(X+s)\kappa(X)\{15+36U(X)\}\\
 &-(5X-3s-2)U(X)\{15+76U(X)\}.
 \end{aligned}
\tag{2.18}
\]

An exact coefficient expansion gives

\[
 P^{(4)}(2/5+Y)<0\qquad(0\leq Y\leq1/5);
\tag{2.19}
\]

all fourteen monomial coefficients are strictly negative.  Therefore
\(P'''\) decreases.  Exact endpoint arithmetic gives

\[
 P'''(3/5)>1900,qquad P''(\ell)>1300.
\tag{2.20}
\]

Thus \(P''>1300\) throughout (2.16).  At \(X_*=5/9\),

\[
 P(X_*)>\frac7{1000},qquad
 -\frac7{25}<P'(X_*)<0.
\tag{2.21}
\]

Strong convexity now gives

\[
 P(X)>
 \frac7{1000}-\frac{(7/25)^2}{2600}
 =\frac{5663}{812500}>0.
\tag{2.22}
\]

The companion replay prints every coefficient sign and all rational margins
in (2.19)--(2.22); it performs no interval subdivision or optimization.

### 2.4 The range \(3/5\leq X<7/8\)

Define

\[
 R=\frac{p^2(2X-p)}{3p-2M}.
\tag{2.23}
\]

Then (2.13) is equivalent to

\[
 6\kappa(X)R>B(u).
\tag{2.24}
\]

Elementary one-variable calculus gives

\[
 R\geq\frac{27}{125}
 \quad\left(\frac35\leq X\leq\frac45\right),
\tag{2.25}
\]

and

\[
 R>\frac3{20}
 \quad\left(\frac45\leq X<\frac78\right).
\tag{2.26}
\]

For completeness, the derivative of \(R\) with respect to \(p\) has the
sign of

\[
 p(1-p)-\frac{4X(1-X)}3.
\tag{2.27}
\]

At an interior critical point put

\[
 y=2X-1,qquad w=1-2p.
\]

Then

\[
 3w^2=4y^2-1,qquad
R=\frac{(1-w)^2(1+2y+w)}{4(1+2y-3w)}.
\tag{2.28}
\]

The lower endpoint \(p\downarrow2M/3\) has \(R\to+\infty\).  At the
enlarged upper endpoint \(p=X\),

\[
 R=\frac{X^3}{5X-2},
\]

which is increasing for \(X\geq3/5\) and already equals \(27/125\) at
\(X=3/5\).  For \(3/5\leq X\leq3/4\), the derivative in (2.27) has no
interior minimum because \(4X(1-X)/3\geq1/4\).  It remains only to check
the stationary values for \(3/4<X<7/8\).

For \(1/2\leq y\leq3/5\), (2.25) reduces to

\[
 Q_1=A_1+B_1w>0,
\]

\[
 A_1=44-37y-125y^2+250y^3,qquad
 B_1=118-375y+125y^2<0.
\]

Since \(w\leq2/5\),

\[
 Q_1\geq A_1+\frac25B_1\geq6.
\tag{2.29}
\]

For \(3/5\leq y\leq3/4\), (2.26) reduces to

\[
 Q_2=A_2+B_2w>0,
\]

\[
 A_2=11+2y-20y^2+40y^3,qquad
 B_2=7-60y+20y^2<0.
\]

Concavity of \(w=\sqrt{(4y^2-1)/3}\) gives

\[
 w\leq\frac32y-\frac{19}{40},
\]

and hence

\[
 Q_2\geq A_2+B_2\left(\frac32y-\frac{19}{40}\right)
 \geq\frac{59}{80}.
\tag{2.30}
\]

Finally,

\[
 6\frac{10783}{10000}\frac{27}{125}
 -\frac{1516}{1095}
 =\frac{1779637}{136875000}>0,
\tag{2.31}
\]

and

\[
 6\frac{712}{625}\frac3{20}
 -\frac{303}{305}
 =\frac{6069}{190625}>0.
\tag{2.32}
\]

Equations (2.22), (2.31), and (2.32) prove

\[
 \boxed{\mathcal R(t,z,X)>0
 \quad\left(\frac\pi8\leq t\leq\frac\pi6\right).}
\tag{2.33}
\]

## 3. Large phase: \(\pi/6\leq t<3\pi/14\)

Put

\[
 e=\frac{2t}{\pi},\qquad d=1-e.
\tag{3.1}
\]

Thus \(1/3\leq e<3/7\).  This section closes the two nonautomatic
alternatives from Round 34 separately.

### 3.1 A safe rectangle

Every feasible candidate satisfies

\[
 \boxed{\frac{39}{100}<X<\frac34.}
\tag{3.2}
\]

For the upper bound, \(D_1\) decreases in \(t\) and \(X\), and

\[
 D_1\left(\frac\pi6,\frac34\right)
 =\frac{\sqrt7}{4}+\frac{\sqrt{37}-4}{6}
 <\frac{41}{40}.
\tag{3.3}
\]

The positive tangent series through degree nine gives, for
\(t\geq\pi/6>157/300\),

\[
 D_0(t)>
 \frac{60733103449058607283}
 {58126359375000000000}
 >\frac{26}{25}>\frac{41}{40}.
\tag{3.4}
\]

Thus \(X\geq3/4\) is impossible.

For the lower bound define

\[
 Z(e)=k_3e^3+k_5e^5+k_7e^7,
\tag{3.5}
\]

where

\[
 k_3=\frac{24649}{45000},\qquad
 k_5=\frac{607573201}{1125000000},
\]

\[
 k_7=\frac{254593221134633}{472500000000000}.
\]

The positive tangent series gives \(z_0>Z(e)\).  Since \(Z\) is strictly
convex, its tangent at \(E=3/7\),

\[
 \bar z(e)=Z(E)+Z'(E)(e-E),
\tag{3.6}
\]

satisfies \(z_0>\bar z\).  The exact endpoint data are

\[
 Z(E)=\frac{754570373701125273}
 {14412002500000000000},
\]

\[
 Z'(E)=\frac{122441368634735091}
 {294122500000000000}.
\]

The affine function \(100\bar z+22-61e\) is decreasing and its value at
\(e=E\) is

\[
 \frac{157501698701125273}
 {144120025000000000}>1.
\tag{3.7}
\]

The hard inequality \(X>(z_0+d)/(1+d)\) now yields \(X>39/100\).

### 3.2 The boundary \(z=z_0\)

Use the exact rational surrogates

\[
 \bar S(e)=\frac{29e}{20},\qquad
 \bar c(e)=\frac{7867}{7000}-\frac45e,
\tag{3.8}
\]

\[
 \bar a(e)=\frac{1+\bar c+\bar c^2}{3}.
\]

Alternating Taylor bounds at \(157e/100<t<11e/7\) prove

\[
 \sin t>\bar S,qquad \cos t>\bar c,qquad a^2>\bar a.
\tag{3.9}
\]

Define

\[
 r(e,X)=2\bar S+\frac{\bar c^2}{2}(1-X^2),
\]

\[
 U(X)=1-\frac{X^2}{2}-\frac{X^4}{8},
\]

\[
 \widehat H(e,X)=U(X)r(e,X)+1-X^2,
 \qquad
 \widehat D=\frac{\widehat H}{r}.
\tag{3.10}
\]

Rationalization of \(v-\sin t\) and the binomial upper bound for \(u\)
give

\[
 D_1(t,X)<\widehat D(e,X).
\tag{3.11}
\]

For fixed \((e,X)\), set

\[
 J(z)=
 \frac{2\{\sqrt{1-\bar a z^2}-\sqrt{1-\bar a X^2}\}}
 {\bar a\widehat D}
 -\frac12+\frac{d(1-X)}{2(X-z)}.
\tag{3.12}
\]

Then

\[
 \mathcal R(t,z_0,X)>J(z_0).
\tag{3.13}
\]

The following safe bounds hold on (3.2):

\[
 z_0<\frac3{50},\qquad
 \widehat D>\frac{19}{20},
 \qquad
 \sqrt{1-\bar a z^2}>\frac{499}{500}.
\tag{3.14}
\]

Here is a direct wall check for the first two bounds.  Since
\(3\pi/14<33/49\), alternating Taylor estimates give

\[
 \tan(33/49)<\frac45;
\]

after clearing the positive cosine lower bound, the exact margin is

\[
 \frac{4471174903}{553651488040}>0.
\]

Using \(\pi>31/10\), monotonicity of \(\tan t-t\) then yields
\(\tan t-t<9\pi/200\), hence \(z_0<3/50\).  Also

\[
 U>\frac{13}{20},qquad
 \frac{1-X^2}{r}>
 \frac{56}{181}>\frac3{10},
\]

which proves \(\widehat D>19/20\).  Finally \(\bar a<1\) and
\(z<3/50\) imply the radical bound in (3.14).

They imply

\[
 J'(z)>
 -\frac{1200}{9481}+\frac8{63}
 =\frac{248}{597303}>0.
\tag{3.15}
\]

Since \(z_0>\bar z\),

\[
 \mathcal R(t,z_0,X)>J(z_0)>J(\bar z).
\tag{3.16}
\]

Put

\[
 B(e,X)=2-\frac{\bar a}{2}(\bar z^2+X^2).
\tag{3.17}
\]

The elementary inequality \(\sqrt{1-y}<1-y/2\) gives

\[
 J(\bar z)>
 \frac{P(e,X)}
 {2(X-\bar z)B(e,X)\widehat H(e,X)},
\tag{3.18}
\]

where the single exact polynomial is

\[
 \begin{aligned}
 P(e,X)={}&4(X-\bar z)^2(X+\bar z)r(e,X)\\
 &+\{(1-e)(1-X)-(X-\bar z)\}B(e,X)\widehat H(e,X).
 \end{aligned}
\tag{3.19}
\]

This polynomial has bidegree \((7,9)\).  Normalize the rectangle by

\[
 e=\frac13+\frac{2s}{21},\qquad
 X=\frac{39}{100}+\frac{9y}{25},
 \qquad 0\leq s,y\leq1.
\tag{3.20}
\]

Its exact Bernstein expansion satisfies

\[
 P_{XX}-20=
 \sum_{i,j=0}^7\beta_{ij}B_i^7(s)B_j^7(y),
\]

with \(\beta_{ij}\) strictly larger than the corresponding entry of

\[
 \begin{pmatrix}
2&6&8&11&12&13&14&13\\
3&6&9&11&13&14&14&14\\
3&6&9&11&13&15&15&15\\
3&6&9&12&14&15&16&16\\
3&7&10&12&14&16&17&17\\
4&7&10&13&15&17&17&18\\
4&7&10&13&15&17&18&19\\
4&8&11&14&16&18&19&19
\end{pmatrix}.
\tag{3.21}
\]

Hence \(P_{XX}>20\).  At \(X_c=27/50\), set

\[
 Q(e)=20P(e,X_c)-P_X(e,X_c)^2.
\]

The degree-fourteen Bernstein coefficients of \(Q\) are strictly larger
than

\[
 \frac1{100}
 (51,51,51,50,48,46,43,40,36,32,27,21,15,9,2).
\tag{3.22}
\]

Thus \(Q>1/50\), and strong convexity gives

\[
 P(e,X)>\frac1{1000}>0.
\tag{3.23}
\]

Equations (3.16)--(3.23) prove

\[
 \boxed{\mathcal R(t,z_0(t),X)>0.}
\tag{3.24}
\]

The coefficient comparisons (3.21)--(3.22) are exact rational identities,
replayed in the companion Mathematica file.  They are one compact
polynomial positivity lemma, not an interval-box certificate.

### 3.3 The possible second stationary root

Define the intrinsic action cutoff

\[
 X_b(e)=\frac{9d}{2+9d}
 =\frac{9(1-e)}{11-9e}.
\tag{3.25}
\]

We first prove that feasibility forces

\[
 \boxed{X<X_b(e).}
\tag{3.26}
\]

At \(X=X_b\),

\[
 u=\frac{2\sqrt{10-9e}}{11-9e}.
\tag{3.27}
\]

Normalize \(e=(7+2s)/21\), \(0\leq s\leq1\).  The function in (3.27) is
strictly convex.  Its endpoint bounds

\[
 u(1/3)=\frac{\sqrt7}{4}<\frac23,
 \qquad
 u(3/7)=\frac{\sqrt{301}}{25}<\frac7{10}
\]

therefore give

\[
 u<\bar u:=\frac23+\frac{s}{30}.
\tag{3.28}
\]

Moreover,

\[
 \sin t>\frac{29e}{20},
\]

and, because \(v^2=u^2+\sin^2t\,X_b^2\),

\[
 v>\frac7{10}\{u+X_b\sin t\}.
\tag{3.29}
\]

The function

\[
 q\longmapsto q+
 \frac{q^2}{7q/10+C}
\]

is strictly increasing for \(q>0\), \(C>0\).  Thus (1.1),
(3.28), and (3.29) yield

\[
 D_1(t,X_b)<
 \bar u+
 \frac{\bar u^2}
 {7\bar u/10+(29e/20)(1+7X_b/10)}.
\tag{3.30}
\]

After clearing the positive denominator, the assertion that the last member
is below \(21/20\) is exactly

\[
\frac{119903-1351s-71590s^2+7344s^3}
 {180(47187+3759s-1084s^2)}>0.
\tag{3.31}
\]

The numerator is at least

\[
 119903-1351-71590=46962>0.
\]

The denominator factor is at least \(47187-1084=46103>0\).

On the other hand, put

\[
 F_L(x)=\frac{x^3}{3}+\frac{2x^5}{15}
 +\frac{17x^7}{315}+\frac{62x^9}{2835},
\]

\[
 C_U(x)=\frac{x^2}{2}-\frac{x^4}{24}+\frac{x^6}{720}.
\]

The positive tangent series and alternating cosine estimate give

\[
 D_0(t)>\frac{8F_L(t)}{3C_U(t)}.
\tag{3.32}
\]

The right side is increasing for \(0<t<1\); its derivative is the positive
factor

\[
 \frac{128}{63(360-30t^2+t^4)^2}
\]

times

\[
 113400+145530t^2+87075t^4+47364t^6
 -3049t^8+62t^{10}>0.
\]

Since \(t\geq\pi/6>157/300\),

\[
 \frac{8F_L(t)}{3C_U(t)}-\frac{21}{20}
 >\frac{17290676303566582153}
 {908989503696543937500}>0.
\tag{3.33}
\]

Thus

\[
 D_1(t,X_b)<\frac{21}{20}<D_0(t).
\tag{3.34}
\]

Since \(D_1\) decreases in \(X\), (3.26) follows.

At a root of (1.5), put

\[
 H=(1+d)X-z-d=(X-z)-d(1-X)>0.
\]

Using (1.5), the inequality \(\mathcal R_{\rm stat}>0\) is equivalent to

\[
 d(1-X)b(z)(X+z)
 >z\{b(z)+b(X)\}H.
\tag{3.35}
\]

Since \(b(X)<b(z)\), it is enough to prove

\[
 T_0:=d(1-X)(X+z)-2zH>0.
\tag{3.36}
\]

As a quadratic in \(z\),

\[
 T_0=2z^2+\{3d-(2+3d)X\}z+dX(1-X).
\]

Its global minimum satisfies the exact factorization

\[
 \begin{aligned}
 8\min_{z\in\mathbb R}T_0
 & =8dX(1-X)-\{(2+3d)X-3d\}^2\\
 &=-\{X(2+d)-d\}\{X(2+9d)-9d\}.
 \end{aligned}
\tag{3.37}
\]

The hard inequality and \(z>0\) imply

\[
 X>\frac{d}{1+d}>\frac{d}{2+d},
\]

so the first factor in (3.37) is positive.  Equation (3.26) makes the
second factor negative.  Therefore the right side of (3.37) is strictly
positive, proving (3.36), (3.35), and

\[
 \boxed{\mathcal R_{\rm stat}>0.}
\tag{3.38}
\]

### 3.4 Empty domain for \(e\geq3/7\)

For \(e\geq3/7\), exact Taylor bounds give

\[
 D_0(t)>\frac32.
\tag{3.39}
\]

One explicit check is as follows.  Put \(t_*=471/700<3\pi/14\), and use
the same \(F_L,C_U\) as in (3.32).  Write

\[
 16F_L(t)-9C_U(t)=t^2K(t).
\]

Direct differentiation gives \(K'(t)>0\) for \(0<t<\pi/2\), while

\[
 16F_L(t_*)-9C_U(t_*)
 =\frac{7448526413453072190883023}
 {353094061250000000000000000}>0.
\]

This proves (3.39).

The hard condition and the lower bound \(z_0>Z(e)\) imply

\[
 X>\frac38.
\tag{3.40}
\]

Indeed, \(h(e)=8Z(e)+2-5e\) is convex.  Its tangent at \(e=1/2\) is
positive already at \(e=3/7\), with exact margin

\[
 \frac{564730015345396183}{3603000625000000000}>0,
\]

and \(h'(1/2)>0\).  Hence \(8z_0+2-5e>0\) for every \(e\geq3/7\),
which is equivalent to (3.40) after the hard inequality is used.

Since \(D_1\) decreases in both \(t\) and \(X\),

\[
 D_1(t,X)<D_1\left(\frac{3\pi}{14},\frac38\right).
\]

At \(X=3/8\), \(u=\sqrt{55}/8\), while

\[
 \sin\frac{3\pi}{14}>\frac35.
\]

As \(v>u\),

\[
 D_1\left(\frac{3\pi}{14},\frac38\right)
 <u+\frac{u^2}{u+3/5}<\frac32.
\tag{3.41}
\]

Equations (3.39)--(3.41) contradict feasibility.  Hence the transported
domain is empty for \(e\geq3/7\).

## 4. Conclusion and equality-face audit

The small-phase adjacent-action theorem, (2.33), (3.24), (3.38), and the
empty-domain result prove Theorem 0.1.

1. **The face \(Q=1\).**  It is a one-sided analytic limit under the exact
   Round 34 transport.  Every spectral tuple has \(Q<1\), so no new
   ownership convention is introduced.
2. **The phase endpoints.**  The small and middle estimates both include
   \(t=\pi/8\); the middle and large estimates both include \(t=\pi/6\).
   At \(t=3\pi/14\), the domain is already empty.
3. **The radius wall.**  The inherited relation is strict, \(z>z_0\).
   The large-phase boundary is a one-sided adverse limit.
4. **The hard wall.**  Equality \(H=0\), equivalently \(P=dM\), belongs to
   the automatic sector.  Every use of \(H>0\) above is on its strict
   complement.
5. **The action wall.**  Equality \(D_1=D_0\) is an adverse analytic
   boundary.  The spectral candidate has the strict inequality
   \(D_1>D_0\).
6. **Activity.**  Round 34 proved the activity wall disjoint from the whole
   high-floor first shelf, including simultaneous endpoints.
7. **Ordinary and inverse walls.**  No rounding or interpolation is applied
   in this note.  Their literal ownership remains the one inherited from
   the CST reduction.

## 5. Loss ledger

1. The small phase discards the nonnegative factor \(f-2\) in the exact
   adjacent-action estimate and moves to the adverse \(Q=1\) and \(z=z_0\)
   limits only after proving the corresponding monotonicities.
2. In the middle phase, \(d,a^2,z\), and \(D_1\) are replaced by adverse
   bounds in a correlated order.  Positive higher binomial terms are
   discarded only after the monotone direction is fixed.
3. In the large boundary proof, \(z_0,\sin t,\cos t,a^2\), and \(D_1\) are
   replaced by explicit one-sided surrogates before the single polynomial
   is formed.
4. At a stationary root, \(b(X)<b(z)\) replaces
   \(b(X)+b(z)\) by the strictly larger adverse value \(2b(z)\).  The
   resulting quadratic is proved positive on all real \(z\), a larger
   domain than needed.
5. No terminal inverse fraction, floor fraction, branching bonus, or actual
   endpoint sum is independently worst-cased in this proof.  They are not
   required because the exact adjacent shelf/action comparison already
   closes this endpoint family.

## 6. Mathematica replay and computation boundary

The companion files

`computations/general_d_round35_midphase_replay.wl`

and

`computations/general_d_round35_largephase_replay.wl`

replay the exact polynomial identities, rational endpoint comparisons,
Taylor residuals, and Bernstein coefficient comparisons used above.
Mathematica is not used to locate a minimum, certify interval boxes, or
choose a phase threshold.  All load-bearing domains and inequalities are
displayed in this note.

The expected final flags are

\[
 \texttt{round35MidphaseReplayOK=True},\qquad
 \texttt{round35LargephaseReplayOK=True}.
\]

## 7. Gate decision and revised workflow

The exact lower-\(Q\) hard-sector inequality is now closed analytically.
The next CST pass should not refine (1.2), add a phase threshold, or create
another pointwise certificate.  It should return to the finite endpoint
list outside the included shelf and lower-\(Q\) family:

\[
 \boxed{
 \text{remaining \(\alpha\)-faces, higher inverse/count bands, and
 simultaneous inverse/outer-\(B\) collisions}.}
\]

These faces should first be attacked through the same exact shelf--terminal
correlation.  If one intrinsic face resists, the revised strategy requires
moving to the weighted aggregate \(WT\) with the branching bonus
\(\mathcal B_d(A)\), not starting a new ratio ladder.
