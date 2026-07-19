# Independent audit: Round 35 lower-\(Q\) hard-sector closure

Date: 19 July 2026  
Audited source: `human/outbox/general-d-round-35-lower-Q-hard-sector-closure.md`  
Replays:

- `computations/general_d_round35_midphase_replay.wl`
- `computations/general_d_round35_largephase_replay.wl`

Verdict: **PASS**

## 1. Scope and theorem boundary

The audited theorem concerns only the lower-\(Q\), high-floor, first-drop
hard sector.  In the normalized notation

\[
 X=z+P,\qquad Q=X+M<1,\qquad
 d=1-\frac{2t}{\pi},
\]

the hard target is

\[
 E_*=\frac{P-dM}{2P}>0.
\]

The note proves that every tuple in this sector satisfies

\[
 \Delta>E_*.
\]

This closes that lower-\(Q\) endpoint family.  It does **not** prove the
remaining \(\alpha\)-faces, higher inverse/count bands, simultaneous
inverse/outer-\(B\) collisions, the complete high-floor CST statement,
pointwise assembly, or the all-dimensional theorem.  The statement and
conclusion of the audited source respect this boundary.

## 2. Round 34 transport and sufficiency of the face proof

Round 34 first gives the strict lower bound

\[
 \Delta>C=\frac{2N}{D},
\]

where

\[
 N=\int_z^X\frac{y\,dy}{b(y)},\qquad
 D=\int_X^Q\left\{\frac{y}{u(y)}+\frac{y}{v(y)}\right\}dy.
\]

At fixed \((t,z,\rho)\), \(\rho=M/P\), increasing \(P\) makes \(C\)
strictly decrease while the hard target \((1-d\rho)/2\) remains fixed.
The action integral \(D\) increases, so the action condition remains
feasible.  Hence any counterexample transports rigorously to the one-sided
face \(Q\to1^-\).

On that face,

\[
 P=X-z,\qquad M=1-X,
\]

and the exact residual is

\[
 \mathcal R(t,z,X)=
 \frac{2\{b(z)-b(X)\}}{a^2D_1(t,X)}
 -\frac{(1+d)X-z-d}{2(X-z)}.
\]

The transported domain is

\[
 z>z_0(t),\qquad
 \frac{z+d}{1+d}<X<X_D(t),\qquad D_1(t,X_D)=D_0(t).
\]

If the root defining \(X_D\) does not exist, the domain is empty.  For
fixed \((t,X)\), Round 34 proves that a possible minimum in \(z\) occurs
only at:

1. the one-sided radius boundary \(z=z_0\);
2. the hard boundary, where the target term vanishes and
   \(\mathcal R>0\) automatically; or
3. the possible second stationary root
   \[
    \frac{z(X-z)^2}{b(z)}
    =\frac{d(1-X)D_1}{4}.
   \]

Thus the Round 35 proof obligations are exactly the ones it treats: the
full face in the middle phase, and the radius boundary plus possible second
stationary root in the large phase.  No unproved implication from the
face back to the original tuple is used.

## 3. Small phase

The cited small-phase theorem covers \(0<t\leq\pi/8\) directly, before the
Round 34 face split.  Its exact adjacent-action ratio

\[
 R(P)=\frac{u(z)-u(X)}{u(X)-u(Q)}
\]

strictly decreases when \(P\) increases at fixed \((t,z,\rho)\), and its
\(Q=1\) value strictly increases with \(z\).  Therefore

\[
 R(P)>J(z,\rho)>J(z_0,\rho).
\]

After reversible squaring, the residual increases in \(z\).  With
\(s=d\rho\in(0,1)\) and \(d\geq3/4\), its exact polynomial reduction is

\[
 \mathcal P(d,s)=4(1+Z)(d+s)^2
 -s\{2d+s(1+Z)\}(3-s)^2,
 \qquad Z=\frac{(1-d)^3}{2}.
\]

The tensor-product Bernstein coefficients of \(\mathcal P_d\) are all
positive, with minimum \(341/128\).  At \(d=3/4\), the remaining quartic
has the exact strong-convexity lower bound

\[
 q(s)\geq
 \frac{53111042695}{11341398016}>0.
\]

This verifies the complete small-phase dependency, including the endpoint
\(t=\pi/8\).

## 4. Middle phase: \(\pi/8\leq t\leq\pi/6\)

### 4.1 Correlated bounds and action cutoff

The exact elementary estimates give

\[
 d\geq\frac23,\qquad z>\frac1{125},\qquad
 a^2>\frac{87}{100}=:A.
\]

Writing \(u=u(X)\), one has

\[
 v+\sin t>\frac38+\frac9{10}u,
\]

and therefore

\[
 D_1<B(u):=\frac{u(15+76u)}{15+36u}.
\]

Both monotonicity directions used for the action cutoff are correct:
\(D_1\) decreases in \(t\) and \(X\), while \(D_0\) increases in \(t\).
The exact endpoint comparisons are

\[
 D_1\left(\frac\pi8,\frac78\right)
 <\frac{3587}{4928}<\frac{73}{100}
 <\frac{37}{50}<D_0\left(\frac\pi8\right).
\]

Consequently feasibility forces \(X<7/8\).

### 4.2 Quadrature implication

The retained binomial moment gives

\[
 N\geq\frac{(X-z)(X+z)}2\,\kappa(X),
 \qquad
 \kappa(X)=1+\frac{AX^2}{4}+\frac{A^2X^4}{8}.
\]

Since \(d\geq2/3\), the hard target satisfies

\[
 E_*\leq\frac{G}{6p},\qquad
 p=X-z,\qquad G=3p-2(1-X)>0.
\]

Thus the displayed implication direction is correct: it is enough to show

\[
 H=6\kappa(X)p^2(X+z)-B(u)G>0.
\]

No factor whose sign is unknown is cleared in this reduction.

### 4.3 Low-\(X\) range

For \(X\leq3/5\),

\[
 H_z=3B(u)-6\kappa(X)p(X+3z).
\]

The sharp elementary bounds used in the note give

\[
 H_z\geq
 \frac{11550045527}{11406250000}>0.
\]

During audit, the source's initial strict comparison with the displayed
rational margin was corrected to \(\geq\): equality in that bounding chain
can occur at \(X=3/5\), \(z=X/3\).  The required conclusion
\(H_z>0\) is unaffected.

Because the actual radius has \(z>1/125=:s\), the adverse value is
\(z=s\).  The retained condition \(G>0\) then gives

\[
 X>\ell=\frac{253}{625}.
\]

The polynomial

\[
 U(X)=1-\frac{X^2}{2}-\frac{X^4}{8}
 -\frac{X^6}{16}-\frac{5X^8}{128}
\]

is a valid upper bound for \(u(X)\) on this range, and \(B\) is increasing.
After clearing the positive denominator of \(B(U)\), the exact polynomial
\(P(X)\) in the source is therefore an adverse lower bound for \(H(s)\).

Its fourth derivative has fourteen strictly negative monomial
coefficients after the shift \(X=2/5+Y\).  Hence \(P'''\) decreases, while

\[
 P'''(3/5)>1900,\qquad P''(\ell)>1300.
\]

It follows that \(P''>1300\) on the whole interval.  The exact data at
\(X_*=5/9\) then give

\[
 P(X)>\frac7{1000}-\frac{(7/25)^2}{2600}
 =\frac{5663}{812500}>0.
\]

### 4.4 High-\(X\) range

For \(3/5\leq X<7/8\), the hard condition gives the positive denominator
in

\[
 R=\frac{p^2(2X-p)}{3p-2(1-X)}.
\]

The derivative in \(p\) has the sign of

\[
 p(1-p)-\frac{4X(1-X)}3.
\]

The hard endpoint has \(R\to+\infty\); the endpoint \(p=X\) gives
\(X^3/(5X-2)\).  At an interior critical point, the substitutions

\[
 y=2X-1,\qquad w=1-2p,qquad 3w^2=4y^2-1
\]

are exact.  The two displayed reductions \(Q_1=A_1+B_1w\) and
\(Q_2=A_2+B_2w\) have the correct sign direction because
\(B_1,B_2<0\).  The upper bounds for \(w\) therefore give

\[
 R\geq\frac{27}{125}
 \quad\left(\frac35\leq X\leq\frac45\right),
\]

and

\[
 R>\frac3{20}
 \quad\left(\frac45\leq X<\frac78\right).
\]

Together with the monotone bounds for \(\kappa\) and \(B\), the two exact
positive margins are

\[
 \frac{1779637}{136875000}>0,
 \qquad
 \frac{6069}{190625}>0.
\]

This proves \(\mathcal R>0\) on the entire middle-phase face, without using
or omitting a stationary alternative.

## 5. Large phase: \(\pi/6\leq t<3\pi/14\)

Put \(e=2t/\pi\), so \(1/3\leq e<3/7\).

### 5.1 Feasible rectangle

The action comparison at \((t,X)=(\pi/6,3/4)\) is correctly oriented:

\[
 D_1\left(\frac\pi6,\frac34\right)
 <\frac{41}{40}<\frac{26}{25}<D_0\left(\frac\pi6\right).
\]

Since \(D_1\) decreases and \(D_0\) increases in the relevant variables,
feasibility forces \(X<3/4\).

The positive tangent series gives \(z_0>Z(e)\).  The polynomial \(Z\) is
strictly convex, so its tangent \(\bar z\) at \(e=3/7\) satisfies
\(z_0>\bar z\).  The affine function

\[
 100\bar z+22-61e
\]

is decreasing and remains larger than one at its adverse endpoint.
Substitution into the hard bound
\(X>(z_0+1-e)/(2-e)\) proves \(X>39/100\).  Hence the exact feasible
rectangle is contained in

\[
 \frac{39}{100}<X<\frac34.
\]

### 5.2 Radius boundary

The rational surrogates satisfy

\[
 \sin t>\bar S,\qquad \cos t>\bar c,
 \qquad a^2>\bar a.
\]

With \(u^2=1-X^2\), rationalization gives

\[
 v-\sin t=\frac{c^2u^2}{v+\sin t}.
\]

Since \(v+\sin t<2\), one also has

\[
 v+\sin t>2\sin t+\frac{c^2u^2}{2}
 >2\bar S+\frac{\bar c^2u^2}{2}=r(e,X).
\]

The polynomial \(U=1-X^2/2-X^4/8\) is an upper bound for \(u\).
Consequently

\[
 D_1<\widehat D=U+\frac{u^2}{r}.
\]

For fixed \(0<z<X\), the function

\[
 A\longmapsto
 \frac{\sqrt{1-Az^2}-\sqrt{1-AX^2}}{A}
 =\int_z^X\frac{y\,dy}{\sqrt{1-Ay^2}}
\]

is increasing.  This verifies every direction in
\(\mathcal R(t,z_0,X)>J(z_0)\).

The exact bounds

\[
 z_0<\frac3{50},\qquad \widehat D>\frac{19}{20},
 \qquad \sqrt{1-\bar a z^2}>\frac{499}{500}
\]

hold for \(\bar z\leq z\leq z_0\).  Together with
\(d>4/7\), \(1-X>1/4\), and \(X-z<3/4\), they give

\[
 J'(z)>-\frac{1200}{9481}+\frac8{63}
 =\frac{248}{597303}>0.
\]

Thus \(J(z_0)>J(\bar z)\).  Rationalizing the square-root difference and
using \(\sqrt{1-y}<1-y/2\) gives the exact polynomial lower bound

\[
 J(\bar z)>
 \frac{P(e,X)}
 {2(X-\bar z)B(e,X)\widehat H(e,X)},
\]

whose denominator is positive on the rectangle.

The exact tensor-product Bernstein expansion proves

\[
 P_{XX}>20.
\]

At \(X_c=27/50\), let

\[
 Q(e)=20P(e,X_c)-P_X(e,X_c)^2.
\]

Every degree-fourteen Bernstein coefficient of \(Q\) is strictly larger
than the displayed positive comparison vector, whose minimum is \(1/50\).
Therefore \(Q>1/50\).  Strong convexity gives, for all \(X\) in the
rectangle,

\[
 \begin{aligned}
 P(e,X)
 &>P(e,X_c)-\frac{P_X(e,X_c)^2}{40}\\
 &=\frac{Q(e)}{20}+\frac{P_X(e,X_c)^2}{40}
 >\frac1{1000}.
 \end{aligned}
\]

This proves the radius-boundary residual strictly positive.

### 5.3 Possible second stationary root

Define

\[
 X_b=\frac{9d}{2+9d}.
\]

At \(X_b\), the exact radical is

\[
 u=\frac{2\sqrt{10-9e}}{11-9e}.
\]

Its convexity and strict endpoint bounds give

\[
 u<\bar u=\frac23+\frac{s}{30},
 \qquad e=\frac{7+2s}{21},\quad 0\leq s\leq1.
\]

Also

\[
 v>\frac7{10}\{u+X_b\sin t\}.
\]

The resulting one-variable upper bound for \(D_1(t,X_b)\) is valid because
the map

\[
 q\longmapsto q+\frac{q^2}{7q/10+C}
\]

is strictly increasing.  Exact clearing gives

\[
 \frac{21}{20}-D_1(t,X_b)>
 \frac{119903-1351s-71590s^2+7344s^3}
 {180(47187+3759s-1084s^2)}>0.
\]

The numerator is at least \(46962\) and the denominator factor is at least
\(46103\).  Independently, the exact Taylor quotient proves
\(D_0>21/20\).  Hence

\[
 D_1(t,X_b)<D_0(t).
\]

Since \(D_1\) decreases in \(X\), every feasible candidate satisfies
\(X<X_b\).

At a stationary root, substituting the stationary equation into
\(\mathcal R_{\rm stat}>0\) gives exactly

\[
 d(1-X)b(z)(X+z)>z\{b(z)+b(X)\}H,
 \qquad H=(X-z)-d(1-X)>0.
\]

Because \(b(X)<b(z)\), it is enough to prove

\[
 T_0=d(1-X)(X+z)-2zH>0.
\]

As a quadratic in \(z\), its global minimum satisfies

\[
 8\min_{z\in\mathbb R}T_0
 =-\{X(2+d)-d\}\{X(2+9d)-9d\}.
\]

Hardness and \(z>0\) give \(X>d/(1+d)>d/(2+d)\), so the first factor is
positive.  The intrinsic cutoff \(X<X_b\) makes the second factor negative.
The global minimum is therefore strictly positive, which proves
\(\mathcal R_{\rm stat}>0\).

### 5.4 Empty transported domain for \(e\geq3/7\)

The Taylor lower bound for \(D_0\), evaluated below
\(t=3\pi/14\) and then propagated by monotonicity, gives

\[
 D_0(t)>\frac32.
\]

The hard lower bound and \(z_0>Z(e)\) give

\[
 X>\frac{Z(e)+1-e}{2-e}>\frac38.
\]

The last inequality is the exact positivity of
\(8Z(e)+2-5e\); the replay verifies its convexity/tangent proof on
\([3/7,1)\).

By monotonicity,

\[
 D_1(t,X)<D_1\left(\frac{3\pi}{14},\frac38\right).
\]

At the reference point, \(u=\sqrt{55}/8\),
\(\sin(3\pi/14)>3/5\), and \(v>u\).  Hence

\[
 D_1\left(\frac{3\pi}{14},\frac38\right)
 <u+\frac{u^2}{u+3/5}<\frac32.
\]

This contradicts the strict action condition \(D_1>D_0\).  The transported
domain is therefore empty at and beyond \(e=3/7\).

## 6. Equality-face audit

- \(Q=1\) is only a one-sided analytic limit.  Literal tuples retain
  \(Q<1\).
- The inherited radius inequality is strict, \(z>z_0\); the value at
  \(z=z_0\) is used only as an adverse limiting boundary.
- The small and middle modules both cover \(t=\pi/8\), while the middle and
  large modules both cover \(t=\pi/6\).
- The transported domain is already empty at \(t=3\pi/14\).
- Hard equality \(P=dM\) has \(E_*=0\) and belongs to the automatic sector.
- Action equality \(D_1=D_0\) is an adverse analytic boundary; every
  candidate satisfies the strict action inequality.
- Round 34 already proves activity automatic on the entire inherited
  high-floor first shelf, including simultaneous endpoints.
- No new ordinary-floor, inverse, interpolation, or turning-wall owner is
  introduced.

These checks leave no unowned equality face inside the theorem's stated
scope.

## 7. Mathematica replay

Mathematica 15 was run independently on all four proof layers:

```powershell
wolframscript -file computations/general_d_round34_activity_and_quadrature_replay.wl
wolframscript -file computations/general_d_small_phase_adjacent_action_replay.wl
wolframscript -file computations/general_d_round35_midphase_replay.wl
wolframscript -file computations/general_d_round35_largephase_replay.wl
```

The final flags were

```text
round34ActivityAndQuadratureReplayOK=True
roundSmallPhaseReplayOK=True
round35MidphaseReplayOK=True
round35LargephaseReplayOK=True
```

The Round 35 replays reproduce the exact rational margins, derivative
identities, Taylor residuals, stationary factorization, and Bernstein
coefficient comparisons.  They perform no interval subdivision, numerical
minimization, or empirical threshold selection.

## 8. Frozen artifact hashes

The PASS verdict applies to the following frozen SHA-256 hashes:

```text
4038d92c526532a407f5711f63539bd168d2e88adf1f64e98dfeb8fdc85b9aa4
  human/outbox/general-d-round-35-lower-Q-hard-sector-closure.md

65d2f4344d930e140138d325c33cf81f9a1e673f8bb80bcc5856e643227f062f
  computations/general_d_round35_midphase_replay.wl

ca175a9713b9662619ee10f0e700bcb1a7420a8911fb4441a944e07bdc7519f9
  computations/general_d_round35_largephase_replay.wl
```

