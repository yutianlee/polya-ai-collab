# General dimension, Round 11: analytic closure of the zero-level corner and a pre-shelf reduction of the one-level first-floor branch

Date: 18 July 2026

Status: the first-floor no-drop sector with no complete terminal ball level
is proved analytically.  On the new \(d\ge4\) extension grids, the sector
with one complete terminal ball level is reduced to the explicit sufficient
scalar (4.5) below.  No sign claim for that remaining scalar is made in this
note.

## 1. Hypotheses and notation

Let

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}
 \quad(0\le z<a),
 \qquad G_a(z)=0\quad(z\ge a),
\]

and put

\[
 \mu=\rho K,
 \qquad A=G_K-G_\mu,
 \qquad \sigma=-A'.
\]

Assume that the shift is spectrally active and belongs to the relevant
integer or half-integer grid.  In particular,

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}
 +\frac{(d-2)^2-1}{4},
 \tag{1.1}
\]

in the dimensions occurring in the branching argument.  Hence

\[
 \lambda:=A(0)=\frac{K-\mu}{\pi}>1.
 \tag{1.2}
\]

For Sections 2--4, the new extension-grid obligations are precisely

\[
 r\in\mathbb N,\quad r\ge1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\quad r\ge\frac32.
 \tag{1.2a}
\]

The integer shifts are first owned in dimension \(4\), and the half-integer
shifts in (1.2a) are first owned in dimension \(5\).  The line \(r=1/2\)
is retained below only as a diagnostic comparison with the already completed
three-dimensional theorem; it is not a new general-dimensional branching
obligation.  Theorem 5.1 is stronger and does not require this exclusion.

Consider the first-floor no-drop branch

\[
 p=n\ge1,
 \qquad q=r+n,
 \qquad q\le\mu<q+1,
 \qquad F_0=\cdots=F_n=1.
 \tag{1.3}
\]

Write

\[
 \varepsilon=A(q)-\frac34\in[0,1),
 \qquad
 \Delta=A(r)-A(q)\ge0,
 \tag{1.4}
\]

and let

\[
 R_n=-\frac n2+2n\varepsilon
 +2\int_0^n u\sigma(r+u)\,du.
 \tag{1.5}
\]

The exact no-drop identity is

\[
 D_A(r)=D_A(q)+R_n+\chi_q,
 \qquad
 \chi_q={\bf1}_{\{A(q)=3/4\}}.
 \tag{1.6}
\]

At the terminal point put

\[
 v=G_K(q),\qquad h=G_\mu(q),\qquad
 B=[v+\tfrac14]_<,\qquad Q=[A(q)+\tfrac14]_<,
 \tag{1.7}
\]

\[
 \alpha=\mu-q\in[0,1),
 \qquad \beta=\frac{\arccos(q/K)}\pi.
 \tag{1.8}
\]

The already proved local cap estimate gives

\[
 2\int_q^\mu G_\mu(z)\,dz\le\alpha h.
 \tag{1.9}
\]

The cases \(\varepsilon\ge1/4\) and \(B\ge2\) are already closed: the
first follows immediately from (1.5) and one-interface nonnegativity; for
the second, \(h<G_{5/2}(3/2)<1/5\) and strict counting give
\(v>7/4\), hence

\[
 \varepsilon=v-h-\frac34>1-h>\frac45.
 \tag{1.10}
\]

Thus only \(0\le\varepsilon<1/4\) and \(B\in\{0,1\}\) need be
considered.

### Dependencies

This note uses only the following earlier proved modules.

1. The exact no-drop identity (S4), written here as (1.6), and the exact
   first-shelf identity (S2) with its scale-free curvature estimate (S3).
2. One-interface nonnegativity \(D_A(q)\ge0\), the strengthened fractional
   terminal reserve (T2), and the local cap estimate (T3), with the literal
   strict-bracket conventions at every wall.
3. The strengthened dimensional no-mode wall (1.1), the local estimate
   \(h<G_{5/2}(3/2)<1/5\), and the zero-level terminal triangle used in
   (5.13).

Lemma 2.1 and Theorem 5.1 are new proofs in this note.  No numerical search,
external script, or absent certificate is a premise of either proof.

## 2. A pre-shelf correlation

The next lemma is the useful new reduction for the one-level branch.

### Lemma 2.1 (active-width pre-shelf bound)

Under (1.1)--(1.4),

\[
 \boxed{
 \Delta\ge
 \Delta_*(\varepsilon):=
 \frac{2n}{r+2n}
 \left(\lambda-\frac34-\varepsilon\right)>0.}
 \tag{2.1}
\]

#### Proof

On \([0,\mu)\),

\[
 \sigma'(z)=\frac1{\pi\sqrt{\mu^2-z^2}}
 -\frac1{\pi\sqrt{K^2-z^2}}\ge0,
\]

and

\[
 \sigma''(z)=\frac z\pi
 \left((\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}\right)\ge0.
\]

Thus \(\sigma\) is increasing and convex, with \(\sigma(0)=0\).
Convexity implies that \(\sigma(z)/z\) is nondecreasing.  Consequently

\[
 A(0)-A(r)=\int_0^r\sigma(z)\,dz
 \le\frac r2\sigma(r),
 \qquad
 \Delta=\int_r^{r+n}\sigma(z)\,dz\ge n\sigma(r).
\]

Therefore

\[
 A(0)-A(r)\le\frac r{2n}\Delta.
 \tag{2.2}
\]

Since \(A(r)=3/4+\varepsilon+\Delta\), (2.2) becomes

\[
 \lambda-\frac34-\varepsilon-\Delta
 \le\frac r{2n}\Delta,
\]

which rearranges to (2.1).  Its right side is strictly positive by
\(\lambda>1\) and \(\varepsilon<1/4\).  \(\square\)

## 3. Monotone elimination of the endpoint remainder

The exact first-shelf identity and the scale-free curvature estimate give

\[
 R_n\ge
 n\left(2\varepsilon+\Delta-\frac12\right)
 +\frac{n^2}{3(2r+n)}\Delta.
 \tag{3.1}
\]

Set

\[
 M_n:=n+\frac{n^2}{3(2r+n)}.
 \tag{3.2}
\]

Substituting (2.1) into (3.1) gives

\[
 R_n\ge \mathcal H(\varepsilon):=
 n\left(2\varepsilon-\frac12\right)
 +M_n\frac{2n}{r+2n}
 \left(\lambda-\frac34-\varepsilon\right).
 \tag{3.3}
\]

This lower bound is strictly increasing in \(\varepsilon\).  Indeed,

\[
 \mathcal H'(\varepsilon)
 =2n\left(1-\frac{M_n}{r+2n}\right)>0,
 \tag{3.4}
\]

because

\[
 M_n<n\left(1+\frac13\right)=\frac{4n}{3}
 <2n\le r+2n.
\]

Hence the full hard remainder interval is bounded by its lower-wall value:

\[
 \boxed{
 R_n\ge\mathcal R_0:=-\frac n2
 +M_n\frac{2n}{r+2n}
 \left(\lambda-\frac34\right).}
 \tag{3.5}
\]

This is a sufficient lower bound, not an identity.  Its point is that the
continuous endpoint remainder \(\varepsilon\) has disappeared without
replacing the active width \(\lambda\) by its worst possible value.

## 4. The one-level sufficient scalar

Assume \(B=1\).  Let \(\theta=\theta_1\) be determined by

\[
 \frac K\pi(\sin\theta-\theta\cos\theta)=\frac34,
 \tag{4.1}
\]

and put

\[
 y_1=K\cos\theta-q,
 \qquad
 \eta=y_1-[y_1]_<\in(0,1].
 \tag{4.2}
\]

The strengthened one-level terminal reserve, the local cap (1.9), and
one-interface nonnegativity imply

\[
 D_A(q)\ge\max\{0,\widehat L_1\},
 \tag{4.3}
\]

where

\[
 \widehat L_1=
 \frac\pi{2\theta}+2\eta-Q-\alpha h
 +\frac{(v-1)_+^2}{\beta}.
 \tag{4.4}
\]

Combining (1.6), (3.5), and (4.3) proves the following reduction.

### Proposition 4.1 (pre-shelf reduction of \(B=1\) on the extension grids)

Every active first-floor no-drop tail on (1.2a) with \(B=1\) is proved if

\[
 \boxed{
 \widehat\Psi_1:=
 \max\{0,\widehat L_1\}
 -\frac n2
 +\left(n+\frac{n^2}{3(2r+n)}\right)
 \frac{2n}{r+2n}
 \left(\lambda-\frac34\right)
 +\chi_q\ge0.}
 \tag{4.5}
\]

The remaining variables in (4.5) retain their exact correlations

\[
 v-h=A(q)=\frac34+\varepsilon,
 \qquad
 \lambda=\frac{K-\mu}{\pi},
 \qquad
 q=r+n,
 \qquad
 \alpha=\mu-q.
 \tag{4.6}
\]

One may omit the nonnegative top square from (4.4) to obtain a weaker
scalar with no explicit occurrence of \(\varepsilon\).  No such omission
is needed in (4.5).

### Equality and wall audit

The literal strict phase data are

\[
\begin{array}{c|c|c}
\text{phase}&(Q,\chi_q)&\text{conditions}\\ \hline
\text{open}&(1,0)&0<\varepsilon<1/4,\\
\text{lower noncorner}&(0,1)&\varepsilon=0,\ h>0,\\
\text{corner}&(0,1)&\varepsilon=h=0\quad(B=0).
\end{array}
\tag{4.7}
\]

The lower noncorner is not obtained by moving the open value of \(Q\)
through the wall.  At a spatial wall \(y_1\in\mathbb N\), the definition
in (4.2) gives \(\eta=1\), not zero; the equality sample is absent.  At a
vertical action wall \(v+1/4\in\mathbb N\), \(B\) and the top square in
(4.4) are evaluated literally.  These conventions make (4.5) valid on
every equality face.

At a shelf wall \(A(r+j)+1/4\in\mathbb N\), \(F_j\) is the ordinary
floor and the corresponding remainder is zero, so (S2) remains exact.  If
\(r+j=\mu\), the inner action is evaluated as zero at that sample.  In
particular, when \(\mu-r\in\mathbb N\), one has \(q=\mu\),
\(\alpha=h=0\), and the cap vanishes.  If \(r+j=K\), the sample is absent
under the strict bracket.  Thus the four equality faces required by the
strategy are all evaluated literally rather than by continuity from an
adjacent chamber.

Equation (4.5) is the precise remaining \(B=1\) inequality.  This note
does not assert its sign.

### Loss ledger for Proposition 4.1

The passage from the exact identity (1.6) to (4.5) makes exactly the
following losses.

1. Equation (3.1) replaces the exact first-shelf curvature term by (S3),
   discarding its nonnegative hinge surplus.
2. Equation (3.3) replaces the exact endpoint drop \(\Delta\) by the
   pre-shelf lower bound \(\Delta_*(\varepsilon)\).
3. Equation (3.5) discards the nonnegative amount
   \(\mathcal H(\varepsilon)-\mathcal H(0)\), which is positive when
   \(\varepsilon>0\) and vanishes on the lower wall.
4. The terminal bound replaces the exact inner cap \(2\delta\) by
   \(\alpha h\), discarding \(\alpha h-2\delta\ge0\), and the tangent proof
   behind (T2) discards its nonnegative inverse-tangent gaps.

The maximum in (4.3) combines two proved lower bounds and causes no loss.
In particular, \(2\eta\), the top square, and \(\chi_q\) are all retained.
The proof of Theorem 5.1 uses the explicit pointwise relaxations
(5.7)--(5.12); each is displayed and leaves a strict final margin.  It has
no hidden numerical step.

## 5. Analytic closure of the \(B=0\) corner

We now prove the other residual phase completely.

### Theorem 5.1 (zero-level first-floor no-drop corner)

Every spectrally active first-floor no-drop tail with \(B=0\) satisfies

\[
 \boxed{D_A(r)>0.}
 \tag{5.1}
\]

#### Proof

The conditions \(B=0\) and \(A(q)\ge3/4\) force

\[
 q=\mu,\qquad G_K(q)=A(q)=\frac34,\qquad
 \varepsilon=0,\qquad Q=0,\qquad\chi_q=1.
 \tag{5.2}
\]

Put

\[
 \theta=\arccos(q/K),
 \qquad c=\cos\theta=\frac qK,
 \qquad \Phi(\theta)=\sin\theta-\theta\cos\theta.
 \tag{5.3}
\]

Then

\[
 \frac K\pi\Phi(\theta)=\frac34,
 \qquad
 q=\frac{3\pi c}{4\Phi(\theta)},
 \qquad
 \lambda=\frac{K-q}{\pi}
 =\frac{3(1-c)}{4\Phi(\theta)}>1.
 \tag{5.4}
\]

The function

\[
 \theta\longmapsto\frac{1-\cos\theta}{\Phi(\theta)}
\]

is strictly decreasing, since the numerator of its derivative is

\[
 \sin\theta\,[\Phi(\theta)-\theta(1-\cos\theta)]
 =\sin\theta\,(\sin\theta-\theta)<0.
\]

At \(\theta_0=2/\sqrt3\), alternating Taylor bounds give

\[
 \sin\theta_0>\frac{6737}{8505}\theta_0,
 \qquad
 \cos\theta_0<\frac{10313}{25515}.
\]

Consequently

\[
 4\Phi(\theta_0)-3(1-\cos\theta_0)
 >-\frac{15202}{8505}+\frac{5656}{3645}\theta_0>0.
\]

The last comparison is exact: after clearing positive denominators and
squaring, its numerator is

\[
 (11312\cdot8505)^2-3(15202\cdot3645)^2
 =44853838881300>0.
\]

Thus \(\lambda(\theta_0)<1\), and (5.4) implies

\[
 0<\theta<\frac2{\sqrt3}.
 \tag{5.5}
\]

In particular, another alternating Taylor bound gives

\[
 c>\cos(2/\sqrt3)>\frac{491}{1215}>\frac25,
 \tag{5.6}
\]

and

\[
 1-c\ge\frac{\theta^2}{2}-\frac{\theta^4}{24}
 >\frac49\theta^2.
 \tag{5.7}
\]

We next estimate the positive head integral in (1.5).  Put

\[
 t=\frac nq\in(0,1),
 \qquad a=1-t.
\]

For \(s\in[a,1]\), the exact corner slope is

\[
 \begin{aligned}
 \pi\sigma(qs)
 &=\arccos(sc)-\arccos s\\
 &=\int_0^\theta
 \frac{s\sin u}{\sqrt{1-s^2\cos^2u}}\,du\\
 &\ge
 \frac{s(1-c)}{\sqrt{1-c^2s^2}}.
 \end{aligned}
 \tag{5.8}
\]

Changing variables \(r+u=qs\) and using that
\(\sqrt{1-c^2s^2}\le D:=\sqrt{1-c^2(1-t)^2}\), one obtains

\[
 \begin{aligned}
 I&:=2\int_0^n u\sigma(r+u)\,du\\
 &\ge\frac{2q^2(1-c)}{\pi D}
 \int_{1-t}^1(s-1+t)s\,ds\\
 &=\frac{n^2(1-c)(3-t)}{3\pi D}.
 \end{aligned}
 \tag{5.9}
\]

Since \(\Phi(\theta)\le\theta^3/3\), (5.4) and (5.6) imply

\[
 \frac1q=\frac{4\Phi(\theta)}{3\pi c}
 <\frac{10}{9\pi}\theta^3.
 \tag{5.10}
\]

Let \(x=n\theta\).  From \(\sin\theta\le\theta\), \(t<1\), and
(5.10),

\[
 D^2=\sin^2\theta+c^2(2t-t^2)
 \le\theta^2+2t
 <\theta^2\left(1+\frac{20x}{9\pi}\right).
 \tag{5.11}
\]

Equations (5.7), (5.9), and \(3-t>2\) therefore give

\[
 I>
 \frac1\theta
 \frac{8x^2}{27\pi\sqrt{1+20x/(9\pi)}}.
 \tag{5.12}
\]

The zero-level terminal triangle and (1.6) now yield

\[
 \begin{aligned}
 D_A(r)
 &\ge \frac{9\pi}{16\theta}+1-\frac n2+I\\
 &>1+\frac1\theta f(x),
 \end{aligned}
 \tag{5.13}
\]

where

\[
 f(x)=\frac{9\pi}{16}-\frac x2
 +\frac{8x^2}{27\pi\sqrt{1+20x/(9\pi)}}.
 \tag{5.14}
\]

It remains only to check a one-variable algebraic inequality.  Set

\[
 u=\sqrt{1+\frac{20x}{9\pi}}\ge1.
\]

Direct simplification gives

\[
 \frac{400u}{\pi}f(x)
 =P(u):=24u^4-90u^3-48u^2+315u+24.
 \tag{5.15}
\]

For \(1\le u\le11/4\), put \(z=4(u-1)/7\in[0,1]\).  The Bernstein
coefficients of \(P(1+7z/4)\) are

\[
 225,\quad\frac{3915}{16},\quad\frac{2809}{16},
 \quad\frac{3285}{128},\quad\frac{225}{8},
\]

all strictly positive.  For \(u=11/4+v\), \(v\ge0\),

\[
 P(u)=\frac{225}{8}+\frac{45}{8}v
 +\frac{597}{2}v^2+174v^3+24v^4>0.
\]

Hence \(f(x)>0\) for every \(x\ge0\).  Equation (5.13) proves (5.1).
\(\square\)

## 6. Counterexample search (diagnostic only)

The Mathematica evaluator
`computations/general_d_fractional_terminal_probe.wl` was replayed at high
precision after adding (4.5).  This is theorem-design and falsification
evidence only, not an interval certificate.  Among the same 6,409
dimension-active records used
in Round 10, 5,911 records belonged to the \(B=1\) extension-grid target
(1.2a).  No negative value of (4.5) was found; the smallest value in this
replay was approximately

\[
 0.08204151519
\]

near \(r=1,n=2,q=3\).  The exact defect and the stronger Round 10 scalar
retaining both the exact head remainder and the exact cap were also positive
in that sample.

The lower boundary in (1.2a) is essential for this particular sufficient
scalar.  At the exact three-dimensional comparison parameters

\[
 (\rho,K,r)=\left(\frac{227}{500},\frac{2877}{500},\frac12\right),
 \qquad n=2,\qquad q=\frac52,
 \tag{6.1}
\]

the point is spectrally active and belongs to the open \(B=1\) phase.  A
60-digit evaluation gives

\[
 \varepsilon\approx0.00031306544,\qquad
 \widehat L_1\approx0.44608686636,\qquad
 \mathcal R_0\approx-0.45672694496,
\]

and therefore

\[
 \widehat\Psi_1\approx-0.01064007860.
 \tag{6.2}
\]

Thus (4.5) is not a valid universal sign target if the already owned line
\(r=1/2\) is put back into its domain.  This does not contradict
Proposition 4.1, which is an implication, and it does not indicate failure
of the original defect: at (6.1), the stronger Round 10 scalar retaining
both the exact head remainder and the exact cap is approximately
\(0.06731289939\), while the scalar restoring the exact head alone is
approximately \(0.06715517126\), and
\(D_A(r)\approx0.57383178500\).  The loss in (6.2) is specifically the
pre-shelf/head relaxation recorded above.

## 7. Failure report and resulting first-floor status

The required split on the new extension grids is now:

1. \(B=0\): proved analytically by Theorem 5.1;
2. \(B=1\): reduced to the explicit sufficient inequality (4.5), with
   every strict wall retained;
3. \(B\ge2\): automatic by (1.10) and the remainder-rich part of (S4).

Thus the sole surviving first-floor no-drop obligation in this note is to
prove (4.5) on the exact domain (1.2a), subject to (1.1), (1.3),
\(B=1\), and the literal phases (4.7).  Diagnostics indicate that its
difficult pattern is the open side with

\[
 \varepsilon\downarrow0,
 \qquad \eta\downarrow0,
 \qquad R_n<0,
\]

and, on the integer grid, the smallest observed reduced margin occurs near
\(q=3,r=1,n=2\).  No other first-floor failure remains in this note.
The excluded \(r=1/2\) line is owned by the completed three-dimensional
theorem, and (6.2) explains why the coarser scalar (4.5) must not be used to
replace that owner.  These observations are theorem-design evidence only
and are not used in any proof above.
