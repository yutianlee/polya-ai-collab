# General dimension, Round 15: exact-terminal endpoint reduction

Date: 18 July 2026

Status: Round 14 restores the exact no-drop head and exact inner cap, but its
scalar still uses the inverse-tangent lower bound for the outer one-level ball
tail.  This note removes that last analytic loss.  On the original hard
one-level chamber the new scalar is exactly the shifted defect, and it is
strictly decreasing under the same endpoint motion.  The endpoint sign is not
proved here, so the first-floor branch and the all-dimensional theorem remain
open.

## 1. Statement

Let

\[
 G_a(s)=\frac{\sqrt{a^2-s^2}-s\arccos(s/a)}{\pi}
 \quad(0\le s<a),
 \qquad G_a(s)=0\quad(s\ge a),
\]

and put

\[
 J_a(x):=\int_x^aG_a(s)\,ds.
 \tag{1.1}
\]

Consider a first-floor no-drop tail on one of the new extension grids,

\[
 r\in\mathbb N,\ r\ge1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\ r\ge\frac32,
 \tag{1.2}
\]

with

\[
 q=r+n,\qquad n\ge1,\qquad
 \mu=q+\alpha,\qquad 0\le\alpha<1,
 \tag{1.3}
\]

\[
 A_\alpha=G_K-G_{q+\alpha}.
\]

Assume the hard open one-level phase

\[
 B=Q=1,
 \qquad
 0<A_\alpha(q)-\frac34<\frac14,
 \qquad \chi_q=0.
 \tag{1.4}
\]

Let \(\theta\) be the outer inverse angle

\[
 \frac K\pi(\sin\theta-\theta\cos\theta)=\frac34,
 \qquad z=K\cos\theta,
 \tag{1.5}
\]

and set

\[
 y=z-q>0,
 \qquad M=[y]_<,
 \qquad \eta=y-M\in(0,1].
 \tag{1.6}
\]

Here \([\,\cdot\,]_<\) is the largest integer strictly below its argument.
Let \(\bar\alpha\) be the first phase, branch, or owner-dimensional activity
endpoint from Rounds 12 and 14:

\[
 \bar\alpha=\min\{1,\alpha_*,\alpha_{\rm act}\},
 \qquad
 G_{q+\alpha_*}(q)=G_K(q)-\frac34.
 \tag{1.7}
\]

Define the exact-terminal scalar

\[
 \boxed{
 \Omega(\alpha)
 :=2J_K(r)-2J_{q+\alpha}(r)
   -\bigl(1+2n+2M\bigr).}
 \tag{1.8}
\]

### Proposition 1.1 (exact-terminal endpoint reduction)

At every original point satisfying (1.2)--(1.4),

\[
 \boxed{D_{A_\alpha}(r)=\Omega(\alpha).}
 \tag{1.9}
\]

Moreover \(\Omega\) is strictly decreasing in \(\alpha\), and hence

\[
 \boxed{D_{A_\alpha}(r)=\Omega(\alpha)>\Omega(\bar\alpha).}
 \tag{1.10}
\]

Thus the hard \(B=1\) first-floor no-drop branch is reduced to

\[
 \boxed{
 \Omega_{\rm end}(K,q,r)
 :=\Omega(\bar\alpha)\ge0.}
 \tag{1.11}
\]

This is a weaker sufficient sign condition than the Round 14 target
\(\Xi_{\rm end}\ge0\), because it restores the nonnegative outer-ball tangent
gap that Round 14 still discarded.

## 2. Exact terminal count

Because \(0\le\alpha<1\), every positive terminal sample satisfies

\[
 q+j\ge q+1>\mu\qquad(j\ge1).
 \tag{2.1}
\]

Consequently the inner ball vanishes at all such samples:

\[
 A_\alpha(q+j)=G_K(q+j)\qquad(j\ge1).
 \tag{2.2}
\]

The condition \(B=1\) says that the only complete outer-ball level is
\(3/4\).  Since \(G_K\) is strictly decreasing,

\[
 G_K(q+j)>\frac34
 \quad\Longleftrightarrow\quad
 q+j<z
 \quad\Longleftrightarrow\quad
 j<y.
\]

The number of positive integers \(j<y\) is exactly \(M=[y]_<\), including
the literal convention at integral \(y\).  At the terminal endpoint itself,
\(Q=1\).  Therefore

\[
 T_{A_\alpha}(q)=1+2M.
 \tag{2.3}
\]

Since the inner action is supported on \([q,\mu]\), (2.3) gives the exact
terminal identity

\[
 D_{A_\alpha}(q)
 =2J_K(q)-2J_{q+\alpha}(q)-1-2M.
 \tag{2.4}
\]

No inverse-tangent inequality is used in (2.4).

## 3. Combination with the exact no-drop head

Round 14 identifies the exact S4 head as

\[
 H_n(\alpha)
 =2\int_r^q\bigl(A_\alpha(s)-1\bigr)\,ds.
 \tag{3.1}
\]

On the open side \(\chi_q=0\), so S4, (2.4), and (3.1) yield

\[
\begin{aligned}
 D_{A_\alpha}(r)
 &=D_{A_\alpha}(q)+H_n(\alpha)\\
 &=2J_K(q)-2J_{q+\alpha}(q)-1-2M\\
 &\quad+2\{J_K(r)-J_K(q)\}
       -2\{J_{q+\alpha}(r)-J_{q+\alpha}(q)\}-2n\\
 &=2J_K(r)-2J_{q+\alpha}(r)-(1+2n+2M)\\
 &=\Omega(\alpha).
\end{aligned}
 \tag{3.2}
\]

This proves (1.9).  Equivalently, (3.2) recovers the literal first-floor
count

\[
 T_{A_\alpha}(r)=1+2n+2M
\]

without estimating any of its three pieces separately.

## 4. Strict endpoint monotonicity

For \(a>r\), differentiation under the integral is legitimate and gives

\[
 \frac{\partial G_a(s)}{\partial a}
 =\frac{\sqrt{a^2-s^2}}{\pi a}>0
 \qquad(r\le s<a).
 \tag{4.1}
\]

The moving endpoint contributes nothing because \(G_a(a)=0\).  Hence

\[
\begin{aligned}
 \frac{d}{da}J_a(r)
 &=\int_r^a\frac{\sqrt{a^2-s^2}}{\pi a}\,ds\\
 &=\frac{a}{2\pi}
 \left[
  \arccos\frac ra
  -\frac ra\sqrt{1-\frac{r^2}{a^2}}
 \right]>0.
\end{aligned}
 \tag{4.2}
\]

It follows directly from (1.8) that

\[
 \Omega'(\alpha)
 =-2\left.\frac{d}{da}J_a(r)\right|_{a=q+\alpha}<0.
 \tag{4.3}
\]

Every original active open point has
\(\alpha<\bar\alpha\).  Continuity and (4.3) prove (1.10), including a
one-sided branch or activity endpoint.  As in Rounds 12 and 14, the artificial
motion may cross shelf walls: (4.3) compares the explicit scalar and does not
assert that intermediate points remain in the same discrete chamber.

## 5. Relation to the Round 14 scalar

Let \(\Xi(\alpha)=L_{\rm ex}(\alpha)+H_n(\alpha)\) be the Round 14 scalar.
The exact terminal formula (2.4) and the proved one-level tangent theorem give

\[
 D_{A_\alpha}(q)\ge L_{\rm ex}(\alpha).
\]

Therefore, throughout the original chamber,

\[
 \Omega(\alpha)-\Xi(\alpha)
 =D_{A_\alpha}(q)-L_{\rm ex}(\alpha)\ge0.
 \tag{5.1}
\]

The difference is exactly the outer-ball inverse-tangent gap; the inner cap
and exact head cancel.  Formula (1.8) is thus not a new lower surrogate.  It
is the exact original defect with its discrete count frozen while moving to
the endpoint.

## 6. Equality-face audit

1. **Inverse spatial wall.** If \(y=m\in\mathbb N\), then
   \(M=[y]_< =m-1\) and \(\eta=1\).  The equality sample at \(z\) is absent.
   A one-sided cell with \(y\downarrow m\) from above has \(M=m\) and is a
   separate, less favorable chamber.
2. **Lower action wall.** At \(\alpha=\alpha_*\), the literal pair is
   \((Q,\chi_q)=(0,1)\).  Relative to the open-side scalar, the terminal count
   loses one unit and S4 gains one unit, so the literal defect is
   \(\Omega(\alpha_*)+2\).  Using \(\Omega(\alpha_*)\) discards both favorable
   jumps.
3. **Branch wall.** The value \(\alpha=1\) is used only as the limit from
   below.  At the literal wall, \(n=\lfloor\mu-r\rfloor\) changes.
4. **Owner-dimensional activity wall.** The activity endpoint is strict and
   is likewise used only as a limiting value.
5. **Ordinary-floor wall.** Equation (3.2) is proved in the original no-drop
   chamber with ordinary shelf floors.  A shelf wall crossed during artificial
   endpoint motion does not change (1.8).
6. **Interface and outer samples.** At \(r+j=\mu\), the inner action is
   literally zero.  At \(r+j=K\), the outer sample is absent under the strict
   bracket.  Both conventions are already encoded in (2.1)--(2.3).

## 7. Dependencies

The proof uses only:

1. the exact first-floor no-drop identity S4, including \(\chi_q\);
2. the strict definition of the terminal inverse point and strict floor;
3. the endpoint-domain bookkeeping from Rounds 12 and 14; and
4. the elementary derivative (4.1).

The fractional terminal theorem T2 is used only to compare (1.8) with the
older Round 14 scalar in (5.1); it is not a premise of the exact identity or
endpoint reduction.

## 8. Loss ledger

At the original open point, (1.9) makes no analytic loss: the outer terminal,
inner cap, no-drop head, inverse displacement, and full discrete count are all
exact.  Moving to \(\bar\alpha\) discards the strictly positive quantity

\[
 \Omega(\alpha)-\Omega(\bar\alpha).
\]

At a literal lower action wall it additionally discards the two favorable
unit jumps described above.  No curvature minorant, active-width estimate,
terminal tangent, local-cap upper bound, or pre-shelf head replacement occurs.

## 9. Counterexample search and diagnostic replay

The Mathematica evaluator
`computations/general_d_round15_exact_terminal_endpoint_probe.wl` replayed the
same 3,171 seeded hard extension-grid records used in Rounds 12 and 14.  It
found no negative \(\Omega_{\rm end}\) and no negative exact outer tangent
gap.  The endpoint owners and their sampled minima were:

\[
\begin{array}{c|c|c}
\text{owner}&\text{records}&\min\Omega_{\rm end}\\ \hline
\text{phase}&605&0.65614112736\ldots\\
\text{branch}&2432&0.92722743121\ldots\\
\text{activity}&134&0.75072180039\ldots
\end{array}
\]

The overall sampled minimum occurred near

\[
 r=1,\qquad n=2,\qquad q=3,\qquad
 y=0.03538325239\ldots,
\]

at the phase endpoint.  There

\[
 \Xi_{\rm end}=0.13877007259\ldots,
 \qquad
 \Omega_{\rm end}-\Xi_{\rm end}=0.51737105477\ldots.
\]

The large-\(q\) rejected-surrogate example from Round 14 gives

\[
 \Omega_{\rm end}=45.23919157837\ldots.
\]

As an adversarial overextension test, the evaluator also ignored the branch
and activity endpoints and moved every record all the way to the phase root.
That stronger comparison is false: 16 seeded records became negative.  The
smallest was approximately

\[
 -0.41442768816
\]

at a branch-owned record with

\[
 r=1,\quad n=4,\quad q=5,\quad
 y=1.00626575787\ldots,\quad
 \alpha_*=1.94918354009\ldots.
\]

Its correct first endpoint is \(\bar\alpha=1\), where
\(\Omega_{\rm end}=2.05651552792\ldots>0\).  Thus the `min` in (1.7) is
load-bearing; the proof must not move a branch- or activity-owned record to a
later phase root.

The script prints `round15ReplayOK=True`.  This is a seeded high-precision
replay, not an interval enclosure or a coverage proof.

## 10. Failure report and gate decision

The sole unproved assertion proposed by this note is

\[
 \Omega_{\rm end}(K,q,r)\ge0
\]

on the exact extension-grid endpoint domain.  The hard pattern remains the
small integer grid \(r=1,n=2,q=3\), at a phase endpoint just to the unfavorable
side of the inverse spatial wall \(y=0\).  The next analytic round should
differentiate or compare the explicit ball-integral expression (1.8) on the
three intrinsic endpoint faces.  It should not return to the Round 11--12
surrogate or introduce a ratio partition.  If (1.11) is falsified, activate
the weighted aggregate WT.
