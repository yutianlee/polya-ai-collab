# General dimension, Round 12: an alpha-endpoint reduction for the one-level first-floor scalar

Date: 18 July 2026

Status: this note removes the continuous interface displacement \(\alpha\)
from the remaining \(B=1\) scalar of Round 11.  It does not prove the sign
of that scalar and makes no claim that the first-floor branch is closed.

## 1. Statement and setup

Use the notation and hypotheses of Round 11.  In particular, this note is
restricted to the new extension grids

\[
 r\in\mathbb N,\quad r\ge1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\quad r\ge\frac32,
 \tag{1.1}
\]

and to the hard one-level phase

\[
 B=1,\qquad 0\le\varepsilon<\frac14.
 \tag{1.2}
\]

Let

\[
 \Phi(\theta)=\sin\theta-\theta\cos\theta,
 \qquad
 \frac K\pi\Phi(\theta)=\frac34,
 \tag{1.3}
\]

and define the outer inverse-level point and its displacement from the
terminal grid point by

\[
 z=K\cos\theta,\qquad y=z-q,\qquad
 \eta=y-[y]_<\in(0,1].
 \tag{1.4}
\]

Thus \(K,q,v=G_K(q),\beta=\arccos(q/K)/\pi,\theta,y,\eta\) are fixed
when the inner interface is varied through

\[
 \mu=q+\alpha,\qquad 0\le\alpha<1.
 \tag{1.5}
\]

Put

\[
 h(\alpha)=G_{q+\alpha}(q),\qquad
 \lambda(\alpha)=\frac{K-q-\alpha}{\pi},
 \tag{1.6}
\]

and

\[
 C_{r,n}:=
 \left(n+\frac{n^2}{3(2r+n)}\right)\frac{2n}{r+2n}>0.
 \tag{1.7}
\]

On the open side \(0<\varepsilon<1/4\), where \((Q,\chi_q)=(1,0)\),
the Round 11 scalar (4.5) is

\[
 \Psi^{\rm op}(\alpha)
 =\max\{0,L^{\rm op}(\alpha)\}
 -\frac n2+C_{r,n}\left(\lambda(\alpha)-\frac34\right),
 \tag{1.8}
\]

with

\[
 L^{\rm op}(\alpha)
 =\frac\pi{2\theta}+2\eta-1-\alpha h(\alpha)
 +\frac{(v-1)_+^2}{\beta}.
 \tag{1.9}
\]

### Proposition 1.1 (alpha-endpoint reduction)

The function \(\Psi^{\rm op}\) is strictly decreasing in \(\alpha\).
Consequently every active open-phase scalar in (1.8) is bounded below by
its open-side value at the first of the following three endpoints:

1. the lower action wall \(\varepsilon=0\);
2. the branch boundary \(\alpha=1\);
3. the strengthened dimensional activity wall.

The lower-noncorner wall \(\varepsilon=0\) has a strictly more favorable
literal value than its open-side limit.  Hence proving the endpoint scalar
defined in Section 3 is sufficient for all \(B=1\) tails in (1.1).

## 2. Proof of monotonicity

For \(\alpha>0\), direct differentiation of the ball action gives

\[
 h'(\alpha)
 =\frac{\sqrt{(q+\alpha)^2-q^2}}{\pi(q+\alpha)}>0.
 \tag{2.1}
\]

The function \(h\) is continuous at \(0\), with \(h(0)=0\), and is
strictly increasing on \([0,\infty)\).  Moreover,

\[
 \lambda'(\alpha)=-\frac1\pi,
 \tag{2.2}
\]

so

\[
 \frac{d}{d\alpha}
 \left[-\frac n2+C_{r,n}
 \left(\lambda(\alpha)-\frac34\right)\right]
 =-\frac{C_{r,n}}\pi<0,
 \tag{2.3}
\]

and

\[
 \frac{d}{d\alpha}L^{\rm op}(\alpha)
 =-h(\alpha)-\alpha h'(\alpha)\le0,
 \tag{2.4}
\]

with strict inequality for \(\alpha>0\).  At \(\alpha=0\) this derivative
vanishes, but the affine term in (2.3) still has strictly negative derivative.

The map \(x\mapsto\max(0,x)\) is nondecreasing.  Therefore its
composition with the decreasing function in (2.4) is nonincreasing, while
the second term in (1.8) is strictly decreasing by (2.3).  This proves that
\(\Psi^{\rm op}\) is strictly decreasing, including across a zero of
\(L^{\rm op}\).  \(\square\)

## 3. The exact endpoint

Because \(B=1\), one has \(v>3/4\).  Let \(\alpha_*>0\) be the unique
solution of

\[
 h(\alpha_*)=v-\frac34.
 \tag{3.1}
\]

It exists uniquely because \(h(0)=0\), \(h\) is strictly increasing, and
\(h(\alpha)\to\infty\).  The terminal phase endpoint is

\[
 \bar\alpha_{\rm ph}:=\min\{1,\alpha_*\}.
 \tag{3.2}
\]

Equivalently, if

\[
 v-\frac34\le G_{q+1}(q),
\]

then \(\bar\alpha_{\rm ph}=\alpha_*\); otherwise
\(\bar\alpha_{\rm ph}=1\).

For a parity-uniform theorem it is enough to retain the owner-dimensional
no-mode wall.  Let \(d_{\rm own}=4\) on the integer grid and
\(d_{\rm own}=5\) on the half-integer grid in (1.1), and put

\[
 \kappa_{d_{\rm own}}
 =\frac{(d_{\rm own}-2)^2-1}{4}.
 \tag{3.3}
\]

After substituting \(\rho=(q+\alpha)/K\), the strict activity condition is
equivalent to

\[
 \alpha<\alpha_{\rm act}:=
 K-q-\frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}}.
 \tag{3.4}
\]

For every nonempty active chamber, \(\alpha_{\rm act}>0\).  Define the
sharp endpoint used in this note by

\[
 \boxed{
 \bar\alpha=\min\{\bar\alpha_{\rm ph},\alpha_{\rm act}\},
 \qquad
 \Psi_{\rm end}:=\Psi^{\rm op}(\bar\alpha).}
 \tag{3.5}
\]

Every active open-phase point has \(\alpha<\bar\alpha\), unless the phase
wall is the first endpoint, in which case it has
\(\alpha<\alpha_*=\bar\alpha\).  Proposition 1.1 therefore gives

\[
 \boxed{\Psi^{\rm op}(\alpha)\ge\Psi_{\rm end}.}
 \tag{3.6}
\]

At a literal lower-noncorner wall, \(\alpha=\alpha_*<1\), activity forces
\(\alpha_*<\alpha_{\rm act}\), so \(\bar\alpha=\alpha_*\).  There
\((Q,\chi_q)=(0,1)\), and the literal Round 11 scalar is

\[
 \max\{0,L^{\rm op}(\alpha_*)+1\}
 -\frac n2+C_{r,n}\left(\lambda(\alpha_*)-\frac34\right)+1,
 \tag{3.7}
\]

which is strictly larger than \(\Psi^{\rm op}(\alpha_*)\).  Thus (3.6)
also owns the lower-noncorner wall.

If one prefers a dimension-free but stronger sufficient target, monotonicity
also gives

\[
 \Psi_{\rm end}
 \ge\Psi^{\rm op}(\bar\alpha_{\rm ph}).
 \tag{3.8}
\]

Hence positivity at the phase endpoint alone is sufficient, though it may
discard activity-wall margin.

### Elimination of the original continuous variables

Equations (1.3)--(1.4) give

\[
 K=\frac{3\pi}{4\Phi(\theta)},
 \qquad
 q=\frac{3\pi\cos\theta}{4\Phi(\theta)}-y,
 \qquad r=q-n,
 \tag{3.9}
\]

and

\[
 \lambda(\alpha)
 =\lambda_0(\theta)+\frac{y-\alpha}{\pi},
 \qquad
 \lambda_0(\theta)=
 \frac{3(1-\cos\theta)}{4\Phi(\theta)}.
 \tag{3.10}
\]

The quantities \(v,\beta,h(\bar\alpha),\alpha_*\), and
\(\alpha_{\rm act}\) are then explicit functions of \((\theta,y)\).
Thus (3.5) leaves only \((\theta,y,n)\), subject to the grid condition in
(1.1), the identity \(q=r+n\), and the original first-floor chamber
constraints.  The remaining analytic target is the single endpoint
inequality

\[
 \boxed{\Psi_{\rm end}(\theta,y,n)\ge0.}
 \tag{3.11}
\]

The artificial movement from the original \(\alpha\) to
\(\bar\alpha\) may cross a shelf wall or even leave the no-drop chamber.
This causes no logical gap: (3.6) is a monotonic comparison of the explicit
algebraic scalar, and the endpoint itself is not asserted to be another
admissible shell tail.

## 4. Equality-face audit

1. At \(\varepsilon=0\), the strict bracket changes from \(Q=1\) to
   \(Q=0\) and \(\chi_q\) changes from \(0\) to \(1\).  Formula (3.7)
   evaluates these jumps literally and is more favorable than the open-side
   endpoint.
2. At \(\alpha=1\), the value in (3.5) is only the limit
   \(\alpha\uparrow1\).  The integer \(n=\lfloor\mu-r\rfloor\) would
   change at the literal wall, so no inadmissible equality is inserted into
   the original branch.
3. The activity wall in (3.4) is strict.  Again, (3.5) uses its limiting
   value only.
4. If \(y\in\mathbb N\), then \(\eta=1\), not zero.  If
   \(v+1/4\in\mathbb N\), \(B\) and the top square are evaluated with the
   literal strict bracket.  The lower wall \(v=3/4\) belongs to \(B=0\),
   already proved in Round 11.
5. At a shelf wall \(A(r+j)+1/4\in\mathbb N\), the ordinary floor is used
   in the original no-drop identity.  At \(r+j=\mu\), the inner action is
   zero; if \(\mu-r\in\mathbb N\), then \(q=\mu\) and the cap vanishes.
   At \(r+j=K\), the sample is absent under the strict bracket.  Crossing
   any such wall during the artificial endpoint movement does not change
   the algebraic comparison (3.6).

## 5. Dependencies and loss ledger

### Dependencies

The only load-bearing inputs are Round 11 Proposition 4.1, the literal wall
table (4.7) there, and the strengthened dimensional activity wall.  All
derivatives and endpoint comparisons are proved explicitly above.  No
numerical computation is a premise.

### Loss ledger

Round 11 already records the losses used to obtain (4.5).  This note adds
only one further loss: it discards

\[
 \Psi^{\rm op}(\alpha)-\Psi^{\rm op}(\bar\alpha)>0
\]

at an interior open-phase point.  At the lower action wall it additionally
uses the open-side values \((Q,\chi_q)=(1,0)\), thereby discarding both
favorable literal jumps displayed in (3.7).  No fractional reserve, top
square, active-width term, or owner-dimensional wall is discarded in the
sharp endpoint (3.5).  The optional phase-only target (3.8) does discard
the interval between the activity wall and the later phase endpoint when
the activity wall occurs first.

## 6. Counterexample search (diagnostic only)

The deterministic high-precision Mathematica replay
`computations/general_d_round12_alpha_endpoint_probe.wl`, built on the
Round 11 record set, contained 3,171 active records satisfying (1.1)--(1.2) with
\(0<\varepsilon<1/4\).  Each record was moved algebraically to the endpoint
(3.5).  No negative endpoint value was found.  The smallest sampled value
was

\[
 \Psi_{\rm end}\approx0.03954098598
\]

near

\[
 r=1,\qquad n=2,\qquad q=3,\qquad
 \rho\approx0.4858684363,\qquad K\approx6.3884642055.
\]

There the phase wall occurred first:

\[
 \alpha_*\approx0.1729452229,\qquad
 \alpha_{\rm act}\approx0.2176014046.
\]

The phase-only endpoint (3.8) had the same minimum in this replay.  These
root solves and evaluations are not interval enclosures and are used only
for falsification and theorem design.

## 7. Failure report

The only unproved assertion suggested by this note is the endpoint sign
(3.11) on the exact extension-grid domain.  The observed hard pattern is

\[
 r=1,\qquad n=2,\qquad q=3,\qquad
 \varepsilon\downarrow0,\qquad \eta\downarrow0,
\]

with a negative pre-shelf head and the lower action wall occurring before
the activity wall.  The next analytic step should attack (3.11) directly in
\((\theta,y,n)\), retaining the relation (3.1); this note introduces no
ratio partition and no new empirical premise.
