# Lower-\(Q\) small-phase closure by the exact adjacent-action bound

Date: 19 July 2026  
Workflow stage: analytic continuation after Round 34

## 0. Statement and theorem boundary

This note follows
`human/inbox/general-d_simplified_analytic_strategy.md`.  It adds no shell-ratio
owner, chamber decomposition, empirical constant, or interval certificate.
It is one analytic sublemma inside the high-floor first-drop CST argument.

On the lower-\(Q\), high-floor, first-drop hard sector, use the normalized
variables of the Round 34 note:

\[
 0<t<\frac\pi2,\qquad c=\cos t,\qquad
 d=1-\frac{2t}{\pi},
\]

\[
 z=\frac r\mu,\qquad P=\frac p\mu,\qquad
 M=\frac m\mu,\qquad X=z+P,\qquad Q=X+M<1.
\]

The hard excess is

\[
 E_*=\frac{P-dM}{2P}>0.
\tag{0.1}
\]

### Small-phase theorem

Every such tuple with

\[
 \boxed{0<t\leq\frac\pi8}
\tag{0.2}
\]

satisfies

\[
 \boxed{\Delta>E_*.}
\tag{0.3}
\]

Consequently the lower-\(Q\) hard sector is empty throughout (0.2).  The
remaining phase \(t>\pi/8\), the other endpoint families in high-floor CST,
pointwise assembly, and the all-dimensional theorem are not closed here.

## 1. Dependencies

Only the following proved facts are used.

1. The Round 34 adjacent-action lemma:
   \[
   \Delta>(f-1)
   \frac{u(z)-u(X)}{u(X)-u(Q)},
   \qquad u(y)=\sqrt{1-y^2}.
   \tag{1.1}
   \]
2. High-floor ownership \(f\geq2\).
3. The exact hard relation (0.1), equivalently
   \[
   \rho:=\frac MP\in\left(0,\frac1d\right),
   \qquad E_*=\frac{1-d\rho}{2}.
   \tag{1.2}
   \]
4. The Round 34 radius-action consequence
   \[
   z>z_0(t):=\frac{4(\tan t-t)}{3\pi}.
   \tag{1.3}
   \]

No terminal inverse level, floor fraction, activity bound, quadrature scalar,
or branching bonus is used.

## 2. Two exact monotone motions

### 2.1 Transport the adjacent ratio to \(Q\to1^-\)

Fix \((t,z,\rho)\), put

\[
 X=z+P,\qquad Q=z+(1+\rho)P,
\]

and write

\[
 R(P)=\frac{u(z)-u(X)}{u(X)-u(Q)}.
\tag{2.1}
\]

Rationalization gives the exact factorization

\[
 R(P)=
 \frac{2z+P}{\rho\{2z+(2+\rho)P\}}
 \frac{u(X)+u(Q)}{u(z)+u(X)}.
\tag{2.2}
\]

The derivative numerator of the first factor, after clearing its positive
denominator, is

\[
 -2z(1+\rho)<0.
\tag{2.3}
\]

For the second factor \(H(P)\), direct logarithmic differentiation gives

\[
 \frac{H'}H=
 -\frac{X/u(X)+(1+\rho)Q/u(Q)}{u(X)+u(Q)}
 +\frac{X}{u(X)\{u(z)+u(X)\}}.
\tag{2.4}
\]

The first fraction in (2.4) is strictly larger than

\[
 \frac{X}{u(X)\{u(X)+u(Q)\}}
 >
 \frac{X}{u(X)\{u(z)+u(X)\}},
\]

because \(u(z)>u(Q)\).  Hence \(H'<0\), and (2.2) proves

\[
 \boxed{R'(P)<0.}
\tag{2.5}
\]

The maximal one-sided value of \(P\) is

\[
 P\to\frac{1-z}{1+\rho},
\]

where \(Q\to1^-\).  Since (1.2) and therefore \(E_*\) are fixed under this
motion, every original tuple satisfies strictly

\[
 R(P)>J(z,\rho):=
 \frac{u(z)-u(X_1)}{u(X_1)},
 \qquad
 X_1=\frac{1+\rho z}{1+\rho}.
\tag{2.6}
\]

The face in (2.6) is a one-sided analytic limit, not an owned
\(\alpha=0\) spectral point.

### 2.2 Transport the radius to \(z=z_0\)

On the face (2.6), a direct calculation gives

\[
 \{J(z,\rho)+1\}^2=
 \frac{(1+z)(1+\rho)^2}
 {\rho\{2+\rho(1+z)\}}.
\tag{2.7}
\]

The logarithmic derivative of the right side with respect to \(z\) is

\[
 \frac{2}{(1+z)\{2+\rho(1+z)\}}>0.
\tag{2.8}
\]

Thus \(J\) strictly increases with \(z\).  Equation (1.3) yields the second
strict comparison

\[
 \boxed{R(P)>J(z,\rho)>J(z_0(t),\rho).}
\tag{2.9}
\]

## 3. Exact polynomial closure for \(t\leq\pi/8\)

Because \(d\rho<1\), both sides of

\[
 J(z_0,\rho)+1>\frac{3-d\rho}{2}
\]

are positive.  Squaring with (2.7) shows that
\(J(z_0,\rho)>E_*\) is equivalent to

\[
 \Phi(z_0,d,\rho)>0,
\tag{3.1}
\]

where

\[
 \Phi(z,d,\rho)=
 4(1+z)(1+\rho)^2
 -\rho\{2+\rho(1+z)\}(3-d\rho)^2.
\tag{3.2}
\]

First, \(\Phi\) is strictly increasing in \(z\).  Indeed,

\[
 \Phi_z=
 \{2(1+\rho)-\rho(3-d\rho)\}
 \{2(1+\rho)+\rho(3-d\rho)\},
\tag{3.3}
\]

and the first factor equals

\[
 2-\rho+d\rho^2
 =2-\rho(1-d\rho)
 \geq2-\frac1{4d}>0.
\tag{3.4}
\]

For \(t\leq\pi/8\), one has \(d\geq3/4\).  Moreover,

\[
 \tan t-t=\int_0^t\tan^2 y\,dy
 >\int_0^t y^2\,dy=\frac{t^3}{3}.
\]

Since \(\pi>3\),

\[
 z_0(t)>\frac{4t^3}{9\pi}
 >\frac{4t^3}{\pi^3}
 =\frac{(1-d)^3}{2}=:Z(d).
\tag{3.5}
\]

It therefore suffices to prove \(\Phi(Z,d,\rho)>0\).  Put

\[
 s=d\rho\in(0,1).
\]

Multiplying by \(d^2\) gives exactly

\[
 \begin{aligned}
 \mathcal P(d,s)
 :={}&d^2\Phi\left(Z,d,\frac{s}{d}\right)\\
 ={}&4(1+Z)(d+s)^2
 -s\{2d+s(1+Z)\}(3-s)^2.
 \end{aligned}
\tag{3.6}
\]

### 3.1 Monotonicity in \(d\)

Map \(d=(3+x)/4\), \(0\leq x\leq1\), and let

\[
 B_i^4(y)=\binom4i y^i(1-y)^{4-i}.
\]

Exact expansion of \(\mathcal P_d\) is

\[
 \mathcal P_d\left(\frac{3+x}{4},s\right)
 =\sum_{i,j=0}^4m_{ij}B_i^4(x)B_j^4(s),
\tag{3.7}
\]

with coefficient matrix

\[
 (m_{ij})=
 \begin{pmatrix}
 747/128&411/128&341/128&455/128&683/128\\
 51/8&243/64&417/128&67/16&97/16\\
 111/16&141/32&1493/384&311/64&109/16\\
 15/2&5&9/2&11/2&15/2\\
 8&11/2&5&6&8
 \end{pmatrix}.
\tag{3.8}
\]

Every entry is positive, so

\[
 \boxed{\mathcal P_d>0}
 \qquad
 \left(\frac34\leq d\leq1,\ 0\leq s\leq1\right).
\tag{3.9}
\]

This is an exact Bernstein-basis identity printed in full, not a numerical
certificate.

### 3.2 The boundary \(d=3/4\)

At the adverse endpoint,

\[
 \mathcal P\left(\frac34,s\right)=\frac3{512}q(s),
\]

\[
 q(s)=387-1272s+676s^2+776s^3-172s^4.
\tag{3.10}
\]

On \([0,1]\),

\[
 q''(s)=1352+4656s-2064s^2\geq1352.
\tag{3.11}
\]

At \(s_*=17/32\), exact arithmetic gives

\[
 q(s_*)=\frac{1227605}{262144},
 \qquad
 q'(s_*)=\frac{245}{2048}.
\tag{3.12}
\]

Strong convexity therefore yields, for every \(s\in[0,1]\),

\[
 \begin{aligned}
 q(s)
 &\geq q(s_*)+q'(s_*)(s-s_*)+676(s-s_*)^2\\
 &\geq
 q(s_*)-\frac{q'(s_*)^2}{2704}
 =\frac{53111042695}{11341398016}>0.
 \end{aligned}
\tag{3.13}
\]

Equations (3.9)--(3.13) prove \(\mathcal P>0\), hence (3.1).  Finally,
(1.1), \(f-1\geq1\), and (2.9) give

\[
 \Delta>(f-1)R(P)\geq R(P)>J(z_0,\rho)>E_*.
\]

This proves (0.3).

## 4. Equality-face audit

1. **\(Q=1\).**  It is only the one-sided limit in (2.6).  Every original
   tuple has \(Q<1\), so the first comparison in (2.9) is strict.
2. **Radius wall.**  The inherited relation is \(z>z_0\), not equality;
   (2.8) makes the second comparison in (2.9) strict.
3. **Phase endpoint.**  The endpoint \(t=\pi/8\), hence \(d=3/4\), is
   included and is covered by the strict positive rational bound (3.13).
4. **Hard wall.**  The wall \(d\rho=1\) has \(E_*=0\) and belongs to the
   automatic sector.  The proof uses only its strict complement
   \(0<s<1\), while the polynomial audit safely includes the closure.
5. **Ordinary floor walls.**  Equation (1.1) is continuous at the literal
   lower-\(Q\) strict-floor wall and remains strict because its
   radial-parameter average is strict.
6. **Inherited grids and turning walls.**  The only grid input is the already
   proved common radius inequality (1.3).  No interpolation or new turning
   owner is introduced.

## 5. Loss ledger

1. The factor \(f-1\geq1\) in (1.1) is replaced by one; the discarded
   multiple \((f-2)R\) is nonnegative.
2. The exact radius \(z_0\) is replaced in (3.5) by the strictly smaller
   \(Z=(1-d)^3/2\).  Monotonicity (3.3) is proved before this loss.
3. The action constraint \(3(1-c)D>8(\tan t-t)\) is unused.  Discarding it
   enlarges the domain and cannot create a false closure claim.
4. No terminal reserve, floor fraction, actual \(E\), or branching bonus is
   invoked or independently worst-cased.

## 6. Counterexample search and theorem-design diagnostic

Before the proof was promoted, direct high-precision minimization of the
exact limiting adjacent residual found no violation on (0.2).  The smallest
observed value was approximately

\[
 0.00315444
\]

at

\[
 t=\frac\pi8,\qquad
 z=z_0(t),\qquad
 \rho\approx0.712471,\qquad X\approx0.587751.
\]

This search was used only to design the exact proof.  Neither the decimal
location nor the observed margin occurs in the implication chain.

## 7. Exact remaining inequality and gate decision

The small-phase sector (0.2) is closed analytically.  The first unsupported
lower-\(Q\) signs are now restricted to

\[
 t>\frac\pi8,
\]

together with the Round 34 face alternatives

\[
 \mathcal R_{\rm stat}>0
\]

at the possible second stationary root and

\[
 \mathcal R(t,z_0(t),X)>0,
 \qquad X_h(t,z_0)<X<X_D(t).
\]

The next pass should combine the stronger large-phase radial denominator
with the same hard excess, not introduce a new shell-ratio owner.  If that
intrinsic analytic pass fails, the revised strategy sends the branch to the
weighted aggregate \(WT\), not to another pointwise certificate.

## 8. Mathematica replay

The companion symbolic replay

`computations/general_d_small_phase_adjacent_action_replay.wl`

checks the two rationalizations, the squared residual, the exact polynomial
normalization, the Bernstein matrix (3.8), and the rational identities
(3.10)--(3.13).  It is an identity replay, not a sign certificate.
