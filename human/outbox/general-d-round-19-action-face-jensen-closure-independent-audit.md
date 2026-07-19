# Independent audit: Round 19 action-face Jensen closure

Date: 19 July 2026

Audited note:

human/outbox/general-d-round-19-action-face-jensen-closure.md

SHA-256:

796854BE592E9E1836B6634BA12C59709BEDD87928F71A85EACE8A94B1570C2A

Audited replay:

computations/general_d_round19_action_face_jensen_replay.wl

SHA-256:

B31239E6F34726850ED1B7CD559B6EC39EEA0596AC4C49A6859B4D444442D54B

## 1. Verdict

**PASS.**

No load-bearing sign error, domain gap, equality-wall error, exact-arithmetic
discrepancy, or scope overclaim was found.

The note proves

\[
 \frac{dF}{da}>0
\]

on the complete strict action face

\[
 A(a-1)=\frac34,\qquad K-a>\pi.
\]

Together with the imported Round 16 radial monotonicity and Round 18
simultaneous-wall reserve, this proves the enlarged endpoint lemma

\[
 F(K,a)\ge\frac12
\]

and therefore closes the hard open \(B=1\), first-floor endpoint branch
covered by the Round 16 reduction.  The note correctly leaves formal WP2
promotion to an end-to-end integration audit and leaves the high-floor CST
and all-dimensional theorem open.

A fresh Wolfram 15.0 kernel launched with the \(-\mathrm{noinit}\) and
\(-\mathrm{script}\) flags exited with code zero and printed

\[
 \texttt{round19SymbolicChecks=True},
\quad
 \texttt{round19ExactReplayOK=True},
\quad
 \texttt{round19ReplayOK=True}.
\]

## 2. Action-face domain and elementary identities

On the strict action face put

\[
 t=a-1,\qquad
 \gamma=\arccos(t/K),\qquad
 \phi=\arccos(t/a).
\]

The imported endpoint domain has \(a\ge2\) and \(K-a>\pi\), so

\[
 0<\phi<\gamma<\frac\pi2.
\]

Using \(K=t\sec\gamma\) and \(a=t\sec\phi\), direct substitution into
\(G_K(t)-G_a(t)=3/4\) gives

\[
 (\tan\gamma-\gamma)-(\tan\phi-\phi)
 =\frac{3\pi}{4t}.
\]

Implicit differentiation with respect to \(a\) gives

\[
 k:=K'(a)
 =\frac{\gamma+\sin\phi-\phi}{\sin\gamma}.
\]

Consequently

\[
 k-1
 =\frac{(\gamma-\sin\gamma)-(\phi-\sin\phi)}
 {\sin\gamma}>0,
\]

because \(u-\sin u\) is strictly increasing for \(u>0\).  Also
\(s=K/a=\cos\phi/\cos\gamma>1\).  Combining the action equation with the
preceding formulas gives exactly

\[
 s-k=
 \frac{3\pi/4-\gamma+\phi}{a\sin\gamma}>0.
\]

The numerator is positive already from
\(\gamma<\pi/2\) and \(\phi>0\).  Hence the strict global order used later is

\[
 s>k>1.
\]

The current exact replay checks the speed identity symbolically under the
same strict angular assumptions.

## 3. Exact Jensen mass, barycenter, and tangent algebra

Let \(U\) be the radius-\(K\) quantile profile.  The imported quantile
primitive and scaling identity are

\[
 P_K(y)=\int_0^{G_K(y)}U(c)\,dc,
\qquad
 U_a(c)=U_K(sc)=U(sc).
\]

At the critical point \(A(x)=1\), put

\[
 g=G_a(x),\qquad p=g+1,\qquad q=sg.
\]

If

\[
 \beta=\arccos(x/K),\qquad
 \psi=\arccos(x/a),
\]

then the strict face has \(x>0\), hence \(\beta>\psi\).  Since
\(h(u)=\sin u-u\cos u\) is strictly increasing,

\[
 p=\frac K\pi h(\beta),\qquad
 q=\frac K\pi h(\psi),\qquad
 0<q<p.
\]

The exact derivative therefore becomes

\[
 D=
 \left(k-\frac1s\right)\int_0^qU(c)\,dc
 k\int_q^pU(c)\,dc-kU(3/4).
\]

Both density coefficients are strictly positive:

\[
 k-\frac1s>0,\qquad k>0.
\]

The total mass of the positive weighted measure is

\[
 \begin{aligned}
 \mathcal T
 &=
 \left(k-\frac1s\right)q+k(p-q)\\
 &=kp-\frac qs
 =kp-g
 =k+g(k-1)>0.
 \end{aligned}
\]

Its first moment is

\[
 \left(k-\frac1s\right)q\frac q2
 k(p-q)\frac{p+q}{2}.
\]

Using \(q=sg\), twice this moment simplifies to

\[
 kp^2-sg^2.
\]

Thus the exact barycenter is

\[
 m=\frac{kp^2-sg^2}{2\mathcal T}.
\]

The replay checks separately the total-mass identity, the two-interval
weighted-midpoint identity, and the simplified mean identity.

The quantile profile \(U\) is convex.  Jensen's inequality on the positive
measure supported on \([0,p]\) therefore gives

\[
 \left(k-\frac1s\right)\int_0^qU
 k\int_q^pU
 \ge\mathcal T U(m),
\]

and hence

\[
 D\ge\mathcal T U(m)-kU(3/4).
\]

The barycenter lies in the convex hull \([0,p]\), where \(U\) is defined.
Also \(3/4<p=g+1\), so every value and tangent used below is interior to
the quantile domain.

If \(m\le3/4\), monotonicity of \(U\) gives the strict reserve

\[
 D\ge g(k-1)U(3/4)>0.
\]

If \(m>3/4\), put \(f_0=-U'(3/4)>0\).  The convex tangent inequality gives

\[
 U(m)\ge U(3/4)-f_0(m-3/4).
\]

Direct expansion yields

\[
 4\mathcal T(m-3/4)
 =H,
\]

\[
 H=2(k-s)g^2+(k+3)g-k.
\]

At the angle \(\theta\) determined by \(G_K(z)=3/4\),

\[
 f_0=\frac{\pi h(\theta)}
 {K\theta^3\sin\theta}.
\]

The level equation \(Kh(\theta)/\pi=3/4\) gives exactly

\[
 \frac{U(3/4)}{f_0}
 =\frac{3}{4E(\theta)},
\qquad
 E(u)=\left(\frac{h(u)}{u\sin u}\right)^2.
\]

Consequently

\[
 D\ge\frac{f_0}{4}
 \left(
 \frac{3g(k-1)}{E(\theta)}-H
 \right).
\]

All factors divided out in this calculation are strictly positive.  The
replay independently verifies the derivative split, barycenter identity,
\(H\) identity, and slope identity.

## 4. Location and monotonicity on the action face

For fixed \(a\), the action
\(G_K(a-1)-G_a(a-1)\) is strictly increasing in \(K\).  Round 18 proves
that its radial-wall value at \(K=a+\pi\) decreases through \(3/4\) at the
unique \(a_*\).  Hence the strict action face is parameterized exactly by

\[
 a>a_*,
\qquad
 \frac{11}{2}<a_*<\frac{45}{8}.
\]

There is no missing action-face component below \(a_*\): there the radial
value already exceeds \(3/4\), so increasing \(K\) cannot return it to the
action equality.

Since

\[
 \phi'=-\frac1{a^2\sin\phi}<0,
\]

differentiating the action equation gives

\[
 \gamma'
 =
 \frac{\tan^2\phi\,\phi'-(3\pi/4)/(a-1)^2}
 {\tan^2\gamma}<0.
\]

Thus \(\gamma\) decreases strictly along the whole face.

Differentiating \(A(x)=1\) gives

\[
 x'=\frac{k\sin\beta-\sin\psi}{\beta-\psi}.
\]

Then

\[
 g'
 =-\frac{\psi\beta}{\pi(\beta-\psi)}
 \left(
 k\frac{\sin\beta}{\beta}
 -\frac{\sin\psi}{\psi}
 \right).
\]

The factor outside parentheses is strictly negative.  To check the
parenthetical sign, set \(u(v)=\sin v/v\).  The Round 17 comparison says
that \(u(\phi_y)/u(\gamma_y)\) increases strictly with the spatial
variable \(y\).  Since \(x<t\),

\[
 \frac{u(\psi)}{u(\beta)}
 <
 \frac{u(\phi)}{u(\gamma)}.
\]

At \(y=t\),

\[
 ku(\gamma)
 =
 1-\frac{\phi-\sin\phi}{\gamma}
 >
 1-\frac{\phi-\sin\phi}{\phi}
 =u(\phi).
\]

Therefore \(ku(\beta)>u(\psi)\), and

\[
 g'(a)<0
\]

strictly throughout the action face.  The replay now includes the exact
algebraic identity behind this formula for \(g'\).

## 5. Intrinsic inequality (I): angular separation

The function

\[
 E(u)=\left(\frac1u-\cot u\right)^2
\]

is strictly increasing on \((0,\pi/2)\).  Its positive square root has
derivative

\[
 \frac1{\sin^2u}-\frac1{u^2}>0.
\]

The action equality gives

\[
 G_K(t)=\frac34+G_a(t)>\frac34=G_K(z).
\]

Since \(G_K\) decreases strictly in its spatial argument,

\[
 z>t,\qquad \theta<\gamma,
\qquad E(\theta)<E(\gamma).
\]

It remains to compare \(\phi\) and \(\gamma\).  From \(a>a_*>11/2\),

\[
 \cos\phi=1-\frac1a>\frac9{11}.
\]

The upper alternating cosine polynomial at \(613/1000\) lies strictly
below \(9/11\), with exact margin

\[
 \frac{48282245029}{264000000000000}>0.
\]

Therefore

\[
 \phi<\frac{613}{1000}.
\]

Assume for contradiction that \(\gamma\le5\phi/3\).  Since

\[
 a=t\sec\phi,\quad K=t\sec\gamma,\quad
 t=(\sec\phi-1)^{-1},
\]

and

\[
 \frac{5\phi}{3}<\frac{613}{600}<\frac\pi2,
\]

one obtains

\[
 K-a\le
 R(\phi):=
 \frac{\sec(5\phi/3)-\sec\phi}
 {\sec\phi-1}.
\]

To verify the load-bearing monotonicity of \(R\), expand

\[
 \sec v=\sum_{n\ge0}c_nv^{2n},
\qquad c_n>0.
\]

On the required interval, both secant series converge.  The ratio
\(R(v)\) is the weighted mean of

\[
 r_n=(5/3)^{2n}-1,\qquad n\ge1,
\]

under weights proportional to \(c_nv^{2n}\).  Differentiating the
normalized weighted mean gives

\[
 vR'(v)=2\operatorname{Cov}_w(n,r_n)>0,
\]

because both sequences increase strictly and at least two weights are
positive.  Hence \(R\) is strictly increasing on the exact interval used
by the proof.

The cosine brackets imply

\[
 \sec(613/1000)>\frac{11}{9},
\qquad
 \sec(613/600)<\frac{48}{25}.
\]

The second inequality uses the lower alternating cosine polynomial, with
exact margin

\[
 \frac{36367360087918391}
 {33592320000000000000}>0.
\]

Consequently

\[
 R(\phi)
 <
 \frac{48/25-11/9}{11/9-1}
 =\frac{157}{50}
 <\frac{333}{106}<\pi.
\]

The middle rational margin is exactly \(2/1325\).  This contradicts
\(K-a>\pi\), proving

\[
 \frac{\phi}{\gamma}<\frac35.
\]

All secant arguments remain strictly below \(\pi/2\); no pole or
out-of-domain series is used.

## 6. Intrinsic inequality (I): the \(e\)-ratio and Cauchy estimate

Put \(e(u)=u-\sin u\).  The derivative of
\(e(u)/u^{5/2}\) has the sign of

\[
 N(u)=5\sin u-3u-2u\cos u.
\]

Furthermore

\[
 N'(u)
 =2\sin(u/2)
 \left(2u\cos(u/2)-3\sin(u/2)\right).
\]

For \(y=u/2<\pi/4\), the function \(\tan y/y\) increases and satisfies

\[
 \frac{\tan y}{y}<\frac4\pi<\frac43.
\]

This is exactly the strict condition making the second factor in \(N'\)
positive.  Since \(N(0)=0\),

\[
 \frac{e(u)}{u^{5/2}}
\]

increases strictly on \((0,\pi/2)\).  The angular separation therefore
gives

\[
 \frac{e(\phi)}{e(\gamma)}
 <
 \left(\frac35\right)^{5/2}
 <\frac27.
\]

The final comparison is exact after squaring:

\[
 243\cdot49=11907<12500=4\cdot3125.
\]

For the Cauchy step, write

\[
 h(u)=\int_0^u v\sin v\,dv,
\qquad
 e(u)=\int_0^u(1-\cos v)\,dv.
\]

Since

\[
 v\sin v
 =\sqrt{1-\cos v}\,
 v\sqrt{1+\cos v},
\]

Cauchy--Schwarz gives

\[
 h(u)^2\le e(u)I(u),
\qquad
 I(u)=\int_0^u v^2(1+\cos v)\,dv.
\]

The claimed estimate

\[
 I(u)<\frac57u^2\sin u
\]

is equivalent to \(J(u)>0\), where

\[
 J(u)=14h(u)-\frac73u^3-2u^2\sin u.
\]

Direct differentiation gives

\[
 J'(u)=u^2f(u),
\qquad
 f(u)=10\frac{\sin u}{u}-7-2\cos u.
\]

Also

\[
 f'(u)<0
\quad\Longleftrightarrow\quad
 u^2\sin u<5h(u).
\]

The difference on the right starts at zero and has derivative

\[
 \left(5h(u)-u^2\sin u\right)'
 =u(3\sin u-u\cos u)>0.
\]

Thus \(f\) decreases strictly from \(f(0)=1\).  It has at most one zero,
so \(J'\) has at most one sign change, necessarily from positive to
negative.  Finally, using \(\pi<22/7\),

\[
 J(\pi/2)
 >
 14-\frac7{24}\left(\frac{22}{7}\right)^3
 -\frac12\left(\frac{22}{7}\right)^2
 =\frac1{147}>0.
\]

If \(J'\) never changes sign, \(J\) increases from zero.  If it changes
sign once, \(J\) first increases and then decreases to a still-positive
endpoint.  In either case \(J(u)>0\) on the full interval.

It follows that

\[
 E(\gamma)
 <\frac57\frac{e(\gamma)}{\sin\gamma}.
\]

On the other hand,

\[
 k-1
 =\frac{e(\gamma)-e(\phi)}{\sin\gamma}
 >\frac57\frac{e(\gamma)}{\sin\gamma}.
\]

Combining all strict comparisons proves intrinsic inequality (I):

\[
 E(\theta)<E(\gamma)<k-1.
\]

## 7. Exact \(a=8\) checkpoint

The checkpoint uses only exact rational radical brackets, alternating
arctangent bounds, and the Machin enclosure

\[
 p_-=\frac{333}{106}<\pi<
 \frac{355}{113}=p_+.
\]

At

\[
 a_0=8,\qquad t_0=7,\qquad
 K_0=\frac{229}{20},\qquad
 w_0=\frac{73}{20},
\]

independent Fraction arithmetic reproduces all eight radical-square
margins:

\[
 \frac{779}{10^6},\quad
 \frac{271}{15625},\quad
 \frac{119}{15625},\quad
 \frac{129}{10^6},
\]

\[
 \frac{881}{62500},\quad
 \frac{7609}{10^6},\quad
 \frac{1447}{125000},\quad
 \frac{2661}{10^6}.
\]

Every arctangent proxy lies strictly in \((0,1)\).

For the action comparison at \(t_0\), the upper certificate uses:

- the upper outer radical;
- the lower inner radical in the negative term;
- \(p_-\) in the negative \(-t_0\pi/2\) term;
- \(T_7\), an upper arctangent bound, for both angles.

Thus

\[
 \pi\{G_{K_0}(t_0)-G_8(t_0)\}<C_A.
\]

The exact margin is

\[
 \frac{3p_-}{4}-C_A
 =
 \frac{
 34166275022223598095562522971781767471126684906056074079603086688013958331779648636942897437031921456469
 }{
 2620116438842520740256387092700530415649625849669463936735249319791000000000000000000000000000000000000000
 }
 >\frac1{100}.
\]

Therefore the shell action at \(K_0\) is below \(3/4\).  Since it increases
strictly with \(K\), the action-face radius satisfies \(K_8>K_0\).

At \(w_0\), the inner upper certificate uses \(T_5\), while the outer lower
certificate uses \(T_4\).  Their exact margins are

\[
 p_--C_B
 =
 \frac{15989455522339177998637570243643532427}
 {611784270564205335123733641492279642000}
 >\frac1{50},
\]

\[
 C_C-2p_+
 =
 \frac{822970311087710759444706015966277}
 {42086843913568913961403116238401000}
 >\frac1{60}.
\]

Hence

\[
 G_8(w_0)<1,\qquad G_{K_0}(w_0)>2.
\]

Let \(G_8(w)=1\).  The first comparison gives \(w<w_0\).  Since
\(K_8>K_0\), radius monotonicity and spatial monotonicity give the strict
chain

\[
 G_{K_8}(w)>G_{K_0}(w)>G_{K_0}(w_0)>2.
\]

Therefore \(A(w)>1=A(x)\).  Since both \(A\) and \(G_8\) decrease
strictly,

\[
 x>w,\qquad g(8)=G_8(x)<G_8(w)=1.
\]

No decimal approximation to \(K_8,x\), or \(g(8)\) is used.

## 8. Intrinsic inequality (II)

Exact algebra gives

\[
 3g-H
 =2(s-k)g^2+k(1-g).
\]

Three global bounds control this expression.

First, at the simultaneous wall,

\[
 \cos\gamma_*
 =\frac{a_*-1}{a_*+\pi}
 >
 \frac{9/2}{11/2+22/7}
 =\frac{63}{121}>\frac12.
\]

Here \((a-1)/(a+\pi)\) increases in \(a\), while
\(a_*>11/2\) and \(\pi<22/7\).  Since \(\gamma\) decreases on the strict
face,

\[
 \gamma<\frac\pi3.
\]

Second, \(e(u)/\sin u\) increases strictly because its derivative has
positive numerator \(h(u)\).  Therefore

\[
 k-1
 <\frac{e(\gamma)}{\sin\gamma}
 <\frac{2\pi}{3\sqrt3}-1
 <\frac14.
\]

The last inequality is certified by

\[
 8\pi<\frac{176}{7}<15\sqrt3,
\qquad
 675-\left(\frac{176}{7}\right)^2
 =\frac{2099}{49}>0.
\]

Thus

\[
 1<k<\frac54.
\]

Third, at the simultaneous wall \(x=0\), so
\(g_*=a_*/\pi\).  Since \(g\) decreases,
\(a_*<45/8\), and \(p_->25/8\),

\[
 0<g<g_*<\frac95.
\]

If \(g\le1\), the first term in

\[
 2(s-k)g^2+k(1-g)
\]

is strictly positive and the second is nonnegative, proving the claim.

If \(g>1\), monotonicity and the exact checkpoint imply \(a<8\).  Hence

\[
 \cos\phi=1-\frac1a<\frac78<\cos(1/2),
\qquad
 \phi>\frac12.
\]

The middle strict sign follows directly from
\(\cos u>1-u^2/2\) at \(u=1/2\).

Using
\(\gamma<\pi/2\), \(a<8\), \(\sin\gamma<1\), and \(k<5/4\), the exact
speed identity gives

\[
 \frac{s-k}{k}
 >
 \frac{\pi+2}{40}
 >\frac18.
\]

The last margin is

\[
 \frac{p_-+2}{40}-\frac18=\frac3{848}>0.
\]

On \(1<g<9/5<2\), the function

\[
 \frac{g-1}{2g^2}
\]

has derivative \((2-g)/(2g^3)>0\).  Thus

\[
 \frac{g-1}{2g^2}
 <\frac{10}{81}<\frac18,
\qquad
 \frac18-\frac{10}{81}=\frac1{648}.
\]

Therefore

\[
 \frac{s-k}{k}>
 \frac{g-1}{2g^2},
\]

which is equivalent to

\[
 3g-H>0.
\]

This proves intrinsic inequality (II) throughout the strict action face.

## 9. Completion of the derivative proof

For \(m\le3/4\), the reserve in Section 3 is already strict.  For
\(m>3/4\), intrinsic inequality (I) gives

\[
 \frac{3g(k-1)}{E(\theta)}>3g,
\]

while intrinsic inequality (II) gives

\[
 3g>H.
\]

Since \(f_0>0\), the tangent lower bound yields

\[
 D=\frac{dF}{da}>0
\]

at every strict action-face point.

All cases are exhaustive, including the internal equality \(m=3/4\), which
belongs to the first case and still has reserve
\(g(k-1)U(3/4)>0\).

## 10. Round 16 + Round 18 boundary assembly

The closure uses the earlier results in the correct order:

1. Round 16 proves \(F_K>0\).  At fixed \(a\), minimizing \(F\) therefore
   moves \(K\) down to either the radial boundary \(K=a+\pi\) or the action
   boundary \(A(a-1)=3/4\).
2. On the radial boundary, Round 16 proves \(dF/da<0\), so its minimum is
   reached by increasing \(a\) toward the simultaneous wall.
3. On the strict action boundary, Round 19 proves \(dF/da>0\), so its
   minimum is reached by decreasing \(a\) toward the same wall.
4. Round 18 proves at that wall the exact strict reserve

   \[
   F-\frac12>\frac{1443}{449440}>0.
   \]

Thus the simultaneous wall is the unique boundary minimum, and

\[
 F(K,a)>\frac12
\]

throughout the enlarged endpoint domain.  The weaker displayed conclusion
\(F\ge1/2\) is therefore valid.

Round 16's exact endpoint reduction then gives

\[
 D_{A_\alpha}(r)>
 \Omega_{\rm end}
 \ge2F-1+2\eta>0.
\]

This really does close every genuine hard open \(B=1\), first-floor
endpoint covered by the Round 15--16 endpoint workflow.  The continuous
domain is an enlargement of those genuine endpoints, so no grid or owner
case is omitted.

## 11. Equality walls, dependencies, and claim scope

The equality conventions are correct:

1. The Jensen proof is used only for \(K-a>\pi\), where
   \(a>a_*,x>0\), and \(0<q<p\).
2. At the simultaneous wall, \(x=0\) and \(q=p\); Round 18 owns this
   literal equality, so no degenerate two-interval Jensen step is invoked.
3. The internal equality \(m=3/4\) is owned by the monotonicity case.
4. All \(a=8\) radical, action, and inverse comparisons are strict.
5. The inverse \(G_K(z)=3/4\), strict action-face convention, and
   floor/shelf ownership from the earlier endpoint reduction are unchanged.
6. No lower action wall is identified with an open-side endpoint.

The dependency ledger matches the proof.  Round 16 supplies the endpoint
domain, \(F\), the derivative formula, quantile convexity, radial
monotonicity, and endpoint reduction.  Round 17 supplies the quantile
primitive, scaling, speed identity, and sinc comparison.  Round 18 supplies
the simultaneous-wall root bracket, Machin bounds, and exact reserve.

The conclusion is deliberately narrower than WP2:

- it proves the missing hard open \(B=1\) endpoint input;
- it does not itself perform the full first-floor end-to-end integration
  and therefore does not formally promote WP2;
- it makes no high-floor CST claim;
- it does not claim the all-dimensional theorem.

The status and gate language preserve all these distinctions.

## 12. Fresh exact replay

The frozen replay was launched in a fresh Wolfram 15.0 kernel with

math.exe -noinit -script
computations/general_d_round19_action_face_jensen_replay.wl

It exited with code zero and printed

\[
 \texttt{round19StandaloneReplay=True},
\]

\[
 \texttt{round19SymbolicChecks=True},
\qquad
 \texttt{round19ExactReplayOK=True}.
\]

The symbolic checks include:

- total mass, weighted midpoint, and simplified barycenter;
- the derivative split;
- \(4\mathcal T(m-3/4)=H\);
- the intrinsic-II algebra;
- the exact \(g'\) rearrangement;
- the speed identity;
- \(U(3/4)/f_0=3/(4E(\theta))\).

The exact intrinsic-I margins printed as

\[
 \frac{48282245029}{264000000000000},
\quad
 \frac{36367360087918391}
 {33592320000000000000},
\quad
 \frac2{1325},
\quad
 \frac{593}{153125},
\quad
 \frac1{147}.
\]

The exact intrinsic-II margins printed as

\[
 \frac5{242},\qquad
 \frac{2099}{49},\qquad
 \frac3{848},\qquad
 \frac1{648}.
\]

All eight \(a=8\) square margins and all three action/inner/outer
certificate thresholds passed exactly.

The separate high-precision diagnostic at \(a=8\) returned

\[
 K=11.4775215820882072099617688144\ldots,
\]

\[
 x=4.10376800675646796015187193418\ldots,
\qquad
 g=0.837640993412493565305523137344\ldots,
\]

\[
 \frac{dF}{da}
 =0.0513314072811131861479897582973\ldots,
\]

\[
 \text{Jensen bound}
 =0.0449341353931344614259167997183\ldots.
\]

The diagnostic also had positive margins for
\(q<p\), intrinsic inequalities (I) and (II), and the gap between the
exact derivative and Jensen lower bound.  It ended with

\[
 \texttt{round19DiagnosticChecks=True},
\qquad
 \texttt{round19ReplayOK=True}.
\]

The floating diagnostic is correctly separated from the theorem-bearing
exact gates.

## 13. Final disposition

- Exact Jensen mass/barycenter/tangent algebra: **PASS**.
- Action-face location and \(\gamma,g\) monotonicity: **PASS**.
- Secant-ratio monotonicity and angular separation: **PASS**.
- Cauchy--Schwarz and \(J\)-positivity argument: **PASS**.
- Intrinsic inequality (I): **PASS**.
- Exact \(a=8\) checkpoint: **PASS**.
- Intrinsic inequality (II): **PASS**.
- Strict derivative on the whole action face: **PASS**.
- Round 16 + Round 18 boundary assembly: **PASS**.
- Hard open \(B=1\) endpoint conclusion: **PASS**.
- WP2/high-floor/general-theorem scope language: **PASS; these remain
  unpromoted or open exactly as stated**.
- Fresh \(-\mathrm{noinit}\) replay: **PASS**.

No change was made to the audited note or replay.
