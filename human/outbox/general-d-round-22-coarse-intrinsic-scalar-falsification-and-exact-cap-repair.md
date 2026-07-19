# General dimension, Round 22: falsification of the coarse intrinsic scalar and exact-cap repair

Date: 19 July 2026  
Status: rigorous counterexample to Round 21 scalar \(\mathcal R\); repaired reduction proved; CST remains open

## 0. Scope and theorem boundary

Round 21 proved

\[
 \Phi_\delta>\mathcal R,
\]

where \(\mathcal R\) replaces the exact local inner cap

\[
 J=2\int_q^\mu G_\mu(z)\,dz
\]

by the uniform bound \(J<1/7\).  It left the proposed sufficient inequality
\(\mathcal R\geq0\) open.

This note proves that \(\mathcal R\geq0\) is false, even at an exact
rational, dimension-active, high-floor first-drop configuration on the
integer owner grid.  This is **not** a counterexample to
\(\Phi_\delta\), CST-H, the exact scalar \(\mathscr S\), or the shifted-tail
theorem.

The failure is caused by replacing the correlated cap \(J\) by \(1/7\).
Retaining \(J\) gives the repaired intrinsic scalar

\[
 \boxed{\mathcal R_J:=\mathcal R+\frac17-J,}                         \tag{0.1}
\]

and the Round 21 proof immediately strengthens to

\[
 \boxed{\Phi_\delta>\mathcal R_J.}                                  \tag{0.2}
\]

At the counterexample below, directed Arb arithmetic proves
\(\mathcal R_J>1/20\).

Thus the revised strategy's instruction not to replace the local cap by a
universal constant before the last line is load-bearing in the high-floor
branch.

## 1. Exact rational counterexample to \(\mathcal R\)

Take

\[
 K=\frac{261}{20},\qquad
 \mu=\frac{699}{100},\qquad
 \rho=\frac{\mu}{K}=\frac{233}{435},
\]

\[
 r=1,\qquad n=5,\qquad q=6,\qquad
 p=3,\qquad m=n-p=2,\qquad
 \alpha=\mu-q=\frac{99}{100}.
                                                                    \tag{1.1}
\]

This is on the integer owner grid, whose first new dimension is \(d=4\).
The strict activity condition is

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}+\frac34.
                                                                    \tag{1.2}
\]

The left side is \(170.3025\); the right side is approximately
\(46.5195\).  The replay verifies (1.2) with directed Arb intervals.

For orientation, the ordinary-floor inputs \(A(z)+1/4\) at the relevant
integer samples are

\[
\begin{array}{c|cccccc}
 z&1&2&3&4&5&6\\ \hline
 A(z)+1/4&
 2.1683516479&
 2.1361242267&
 2.0809553941&
 2.0002671114&
 1.8893353408&
 1.7386468200 .
\end{array}
\]

The certified strict comparisons are

\[
 2\leq A(z)+\frac14<3\quad(1\leq z\leq4),
 \qquad
 1\leq A(5)+\frac14<2.
                                                                    \tag{1.3}
\]

Hence

\[
 f=2,\qquad p=3<n=5,\qquad m=2
\]

with the first drop exactly where asserted.

Put, as in Round 21,

\[
 c=\frac{\arccos\rho}{\pi},\qquad d=1-2c,\qquad
 W=G_K(\mu),\qquad \lambda=\frac74-W.
\]

Directed arithmetic gives

\[
 \lambda=
 0.4795089742572886423598064045\ldots,
 \qquad
 1<W+\frac14<2.
                                                                    \tag{1.4}
\]

Thus the literal strict interface count is

\[
 B_0=[W+\tfrac14]_< =1,
\]

and \(0<\lambda<3/4\), so the Round 21 top payment is

\[
 \mathcal E(\lambda)=2(3/4-\lambda)^2.
\]

The two lower payments in \(L_0\) are

\[
 (s-1)\lambda
 =0.09918518638669317824721005759\ldots,
\]

\[
 \frac{\kappa}{2}p(2r+p)
 =0.1585974964459713769686474284\ldots.
                                                                    \tag{1.5}
\]

The curvature term is strictly larger, so it is the literal maximum in
\(L_0\).  Substitution in Round 21 equation (4.4) gives

\[
 \boxed{
 \mathcal R=
 -0.003580224605754455300027288358\ldots
 <-\frac1{300}.}                                                     \tag{1.6}
\]

All phase, branch, maximum, strict-count, and sign decisions in
(1.2)--(1.6) are certified by python-flint Arb at 512-bit precision.
Because every phase inequality and branch comparison is strict, (1.6)
persists on an open neighborhood; it is not an isolated wall artifact.

This disproves the proposed Round 21 target

\[
 \mathcal R\geq0.
\]

## 2. Exact-cap repair

Before Lemma 1.1 of Round 21 is used, the interface-level proof gives the
stronger exact-cap inequalities

\[
 L_T>\frac{B_0d}{2c}-J
\]

and, when \(0<\lambda<1\),

\[
 L_T>
 \frac{(f-1)d}{2c}
 +\min\{1,2(3/4-\lambda)_+^2\}-J.
                                                                    \tag{2.1}
\]

Therefore the same shelf-elasticity and curvature argument proves (0.2)
with

\[
\boxed{
\begin{aligned}
 \mathcal R_J={}&
 (p+a_p)L_0-\frac p2+\frac{dm}{2}
 +\frac{B_0d}{2c}-J\\
 &+\mathbf 1_{\{0<\lambda<1\}}
 \min\{1,2(3/4-\lambda)_+^2\}.
\end{aligned}}                                                       \tag{2.2}
\]

This repair introduces no terminal inverse root, fractional inverse
displacement, ratio partition, or certificate.  The cap is elementary:

\[
 J=2I_\mu(q),
\]

\[
 I_a(x)=\frac{a^2}{4\pi}
 \left[
 \left(1+2\frac{x^2}{a^2}\right)\arccos\frac xa
 -3\frac xa\sqrt{1-\frac{x^2}{a^2}}
 \right].
                                                                    \tag{2.3}
\]

Moreover \(q=r+p+m\), while \(\mu\) is already fixed by the Round 21
feasibility relation.  Thus \(J\) is an intrinsic correlated variable,
not a new degree of freedom.

At (1.1), Arb gives

\[
 J=
 0.08901111693545672468110130562\ldots<\frac17,
\]

\[
 \boxed{
 \mathcal R_J=
 0.05026580131593167716172854888\ldots
 >\frac1{20}.}                                                       \tag{2.4}
\]

The loss in the uniform cap substitution is

\[
 \frac17-J=0.053846025921686\ldots,
\]

which is more than enough to reverse the sign in (1.6).  Equation (0.2)
and (2.4) rigorously show that the lower surrogate remains positive at the
counterexample to \(\mathcal R\).

## 3. Grid and wall audit

The diagnostic search that led to (1.1) encoded the two extension owners
separately:

- integer shifts \(r\in\mathbb N\), \(r\geq1\), with the \(d=4\)
  activity correction \(3/4\);
- half-integer shifts \(r\in\mathbb N+1/2\), \(r\geq3/2\), with the
  \(d=5\) activity correction \(2\).

It used the literal strict value

\[
 B_0=[W+\tfrac14]_<
\]

rather than a floating floor surrogate.  The certified counterexample is
on the integer owner.  No counterexample to \(\mathcal R_J\) was found in
a subsequent seeded, non-rigorous stress sweep over both owners, but that
search is theorem-design evidence only.

The counterexample is not caused by an inverse spatial wall: Round 21
already discarded every \(\eta_k\).  It is also not caused by an action
wall: all comparisons in (1.3)--(1.5) are strict.  It isolates the
universal cap replacement as the first sign-changing loss.

## 4. New exact obligation

The corrected intrinsic target is

\[
 \boxed{\mathcal R_J\geq0}
                                                                    \tag{4.1}
\]

on the exact feasible high-floor first-drop domain.  Proving (4.1) would
prove \(\Phi_\delta>0\) and therefore CST-H.  It remains open.

The next analytic attempt should retain (2.3) while exploiting:

1. \(q=r+p+m\geq2\);
2. \(\mu=q+\alpha\) with \(0\leq\alpha<1\);
3. monotonic decrease of \(I_{q+1}(q)\) in \(q\);
4. the exact feasibility equation coupling
   \((f,\lambda,c,r,p,m,\alpha)\);
5. the maximum of the elasticity and curvature payments in \(L_0\).

No conclusion should be drawn from the false inequality
\(\mathcal R\geq0\), and the exact cap should not again be replaced by
\(1/7\) before the final comparison.

## 5. Reproduction

The directed-rounding replay is

`computations/general_d_round22_intrinsic_R_counterexample.py`.

Run

```powershell
python -B computations/general_d_round22_intrinsic_R_counterexample.py
```

The expected terminal lines are

```text
PASS coarse Round 21 R < -1/300
PASS exact-cap replacement R_J > 1/20
counterexampleScope=coarse_R_only
phiOrCSTCounterexample=False
```
