# General dimension, Round 24: two-axis reduction for the C8 scalar

Date: 19 July 2026  
Status: rigorous further reduction; the sign of C8 remains open

## 0. Scope and theorem boundary

Round 23 reduced high-floor first-drop CST-H to

\[
 \mathcal C_8\geq0
\]

on the exact shelf, activity, terminal-action, and strict-wall domain.  This
note does **not** prove that sign.  It proves two exact reductions which remove
spurious discrete and interface freedom:

1. at fixed last-shelf position \(x=r+p\), the dependence on the shelf length
   \(p\) is strictly convex, so at most two adjacent integer values need be
   retained;
2. on the only numerically delicate top-payment cell, \(\alpha\) can be
   eliminated exactly in favor of the intrinsic terminal fractional action.

It also proves the exact motion of the lower shelf wall as \(\alpha\) varies.
That motion has competing signs in \(\mathcal C_8\), so a blanket reduction to
\(\alpha\uparrow1\) is not valid.  Neither CST-H nor the general-dimensional
Polya theorem is promoted here.

## 1. Exact domain and notation

Retain the notation of Round 23:

\[
 t=\arccos\rho,\quad d=1-\frac{2t}{\pi},\quad
 q=r+p+m,\quad \mu=q+\alpha,\quad 0\leq\alpha<1,
\]

\[
 W=\frac\mu\pi(\tan t-t),\qquad
 \lambda=f-\frac14-W>0,qquad
 B_0=[W+\tfrac14]_<.
\]

Put

\[
 x=r+p,qquad h=f-\frac14,qquad
 A_t(z)=G_{\mu/\cos t}(z)-G_\mu(z).
\]

The exact shelf conditions are

\[
 h\leq A_t(x),\qquad A_t(x+1)<h,\qquad A_t(r)<h+1.       \tag{1.1}
\]

The integer owner has \(r\in\mathbb N\), \(r\geq1\), and the half-integer
owner has \(r\in\mathbb N_0+1/2\), \(r\geq3/2\).  In both cases \(p,m\) are
positive integers.  The owner activity inequality is exactly the one in
Round 23 and remains strict.

The scalar is

\[
\begin{aligned}
 \mathcal C_8={}&
 \frac{p^2(3r+2p)(1-\cos t)}{3\pi\mu}-\frac p2
 +\frac m2\left(1-\frac{2t}{\pi}\right)\\
 &+B_0\left(\frac\pi{2t}-1\right)
 +\mathcal E(\lambda)-\frac18.                         \tag{1.2}
\end{aligned}
\]

No term in (1.2) is weakened below.

## 2. Strict convexity in the shelf length

### Lemma 2.1 (fixed-\(x\) shelf convexity)

Fix one parity grid and fix \((x,m,\alpha,f,t)\).  Assume that at least one
positive integer \(p\) gives an exact feasible tuple with \(r=x-p\).  Then
the feasible values of \(p\) form an integer prefix

\[
 \{1,2,\ldots,P\}.                                      \tag{2.1}
\]

On this prefix the only \(p\)-dependent part of \(\mathcal C_8\) is

\[
 S(p)=k p^2(3x-p)-\frac p2,qquad
 k=\frac{1-\cos t}{3\pi\mu}>0,                           \tag{2.2}
\]

and

\[
 S'(p)=3kp(2x-p)-\frac12,qquad
 S''(p)=6k(x-p)=6kr>0.                                   \tag{2.3}
\]

Consequently the discrete minimum is owned as follows.

- If \(6kx^2\leq1\), or if \(S'(P)\leq0\), it is at \(p=P\).
- If \(S'(1)\geq0\), it is at \(p=1\).
- Otherwise put
  \[
   p_*=x-\sqrt{x^2-\frac1{6k}}.                          \tag{2.4}
  \]
  The minimum is at one of the two integers adjacent to \(p_*\) which lie
  in \([1,P]\).

Thus the complete \((r,p)\) list at fixed intrinsic data is replaced by at
most two adjacent candidates, without a ratio split.

### Proof

With \(x\) fixed one has

\[
 \mu=x+m+\alpha,qquad 3r+2p=3(x-p)+2p=3x-p.
\]

Therefore the lower shelf wall, first-drop wall, terminal action, cap
normalization, and owner activity are all independent of \(p\).  The only
remaining feasibility condition involving \(p\) is

\[
 A_t(x-p)<h+1                                             \tag{2.5}
\]

together with the lower bound on \(r=x-p\).  Since \(A_t\) is strictly
decreasing in its spatial argument, decreasing \(p\) increases \(r\) and
preserves (2.5).  The grid lower bound on \(r\) is preserved as well.  This
proves the prefix assertion (2.1).

Substitution of \(r=x-p\) in (1.2) gives (2.2); all other terms are fixed.
Differentiation gives (2.3).  Since every feasible point has \(r>0\), the
convexity is strict.  If the derivative has an interior zero, solving
\(S'(p)=0\) gives (2.4).  The standard nearest-integer property of a strictly
convex function proves the final assertion.  The cases with no interior zero
give the stated endpoints.

The derivative and factorization in (2.3) were independently replayed with
the installed Mathematica 15 kernel; no computer algebra output is needed as
a premise of the displayed calculation.

## 3. Exact elimination of alpha on the delicate top cell

The only sampled low-margin cells have

\[
 B_0=f-1,qquad 0<\lambda<1,
\]

and lie in the quadratic part of the top payment.  Write

\[
 B=B_0=f-1,qquad u=W-B=\frac34-\lambda.                  \tag{3.1}
\]

On the open quadratic cell

\[
 0<u<\frac1{\sqrt2},qquad \mathcal E=2u^2.              \tag{3.2}
\]

The terminal action identity eliminates \(\mu\), hence \(\alpha\), exactly:

\[
 \boxed{\mu=\frac{\pi(B+u)}{\tan t-t}},                  \tag{3.3}
\]

and the interface strip becomes

\[
 \boxed{
  r+p+m\leq\frac{\pi(B+u)}{\tan t-t}<r+p+m+1.}           \tag{3.4}
\]

Here the left equality is the allowed face \(\alpha=0\), while the right
equality is excluded.

Substitution in (1.2), followed by \(x=r+p\), gives the alpha-free scalar

\[
\boxed{
\begin{aligned}
 \widehat{\mathcal C}_8={}&
 \frac{p^2(3x-p)(1-\cos t)(\tan t-t)}
      {3\pi^2(B+u)}-\frac p2\\
 &+\frac m2\left(1-\frac{2t}{\pi}\right)
 +B\left(\frac\pi{2t}-1\right)+2u^2-\frac18.
                                                               \tag{3.5}
\end{aligned}}
\]

No relaxation occurs in (3.3)--(3.5).  At the lower shelf wall the two exact
action balances are

\[
 \boxed{
  W=B+u,qquad A_t(x)-W=\frac34-u.}                       \tag{3.6}
\]

Thus the suspected hard face is no longer described by an independent
\(\alpha\): it is a solution of (3.3), (3.4), and (3.6), followed by the
at-most-two \(p\) choices of Lemma 2.1.

## 4. Motion of the lower shelf wall

### Lemma 4.1 (wall transport in the interface radius)

Fix \(x>0\) and \(h>0\).  Along a lower-wall branch

\[
 \mathcal A(\mu,t;x):=G_{\mu/\cos t}(x)-G_\mu(x)=h,qquad \mu>x,
                                                               \tag{4.1}
\]

the angle \(t=t(\mu)\) and the interface action

\[
 W(\mu)=\frac\mu\pi(\tan t(\mu)-t(\mu))
\]

both decrease strictly.  Equivalently, \(\lambda=h-W\) increases strictly.

### Proof

Put

\[
 y=\frac x\mu,\qquad
 U=\sqrt{\sec^2t-y^2},\qquad V=\sqrt{1-y^2}.
\]

Direct differentiation of the ball action gives

\[
 \mathcal A_\mu=\frac{U-V}{\pi}>0,qquad
 \mathcal A_t=\frac{\mu\tan t\,U}{\pi}>0.                \tag{4.2}
\]

Hence

\[
 t_\mu=-\frac{U-V}{\mu\tan t\,U}<0.                     \tag{4.3}
\]

Using (4.3) in the derivative of \(W\) yields the exact simplification

\[
 W_\mu=\frac1\pi\left(
  \frac{\sin t\sqrt{1-y^2}}{\sqrt{1-y^2\cos^2t}}-t
 \right)<0.                                               \tag{4.4}
\]

Indeed, the quotient multiplying \(\sin t\) is strictly below one, and
\(\sin t<t\) for \(0<t<\pi/2\).  This proves all three assertions.

### Why this does not reduce every tuple to alpha equals one

Within a fixed terminal-action cell, differentiating (1.2) along (4.1) gives

\[
\begin{aligned}
 \frac{d\mathcal C_8}{d\mu}={}&
 \frac{p^2(3r+2p)}{3\pi}
 \left(\frac{\sin t}{\mu}t_\mu-
       \frac{1-\cos t}{\mu^2}\right)\\
 &-\frac m\pi t_\mu-\frac{B_0\pi}{2t^2}t_\mu
 +\mathcal E_\lambda\lambda_\mu.                       \tag{4.5}
\end{aligned}
\]

The curvature term and the quadratic top-payment term are negative, whereas
the \(m\)-term is positive and the \(B_0\)-term is nonnegative.  On the quadratic branch
\(\mathcal E_\lambda=-4(3/4-\lambda)\); on constant branches it is zero.
Thus Lemma 4.1 determines the wall motion but does not determine the sign of
(4.5).  Any proof that simply declares \(\alpha\uparrow1\) to be globally
worst would discard a real competition.

## 5. The reduced obligation and failure report

Round 23 already proves convexity in \(t\) on each intrinsic action cell.
Lemma 2.1 now proves strict convexity in \(p\) at fixed \(x\).  Therefore an
exact proof of \(\mathcal C_8\geq0\) may use the coupled candidate conditions

\[
 \boxed{
  t\in\{\text{cell endpoints, the unique cell stationary point}\},
  \quad
  p\in\{\text{the at-most-two owners from Lemma 2.1 at that }t\}.}   \tag{5.1}
\]

This is a coordinatewise reduction, not an independently precomputed
Cartesian product: \(P\) and \(p_*\) depend on \(t\), while the stationary
point in a \(t\)-cell depends on \(p\).  A proof must solve the coupled
conditions or compare them with a controlled common bound.

On the delicate quadratic cells, (3.3)--(3.6) replace \(\alpha\) and \(f\)
by \((B,u)\), with the integer condition \(B=f-1\geq1\) and
\(0<u<1/\sqrt2\).  On precisely those cells, the exact remaining sign is
(3.5) subject to (1.1), (3.3)--(3.4), the strict activity wall, and the
coupled candidate rule (5.1).  The other constant or quadratic action/top
cells remain obligations for the original scalar (1.2), with Lemma 2.1 but
without the specialized elimination (3.3).

The hoped-for direct statement that every convex-cell minimum is at least its
lower-shelf-wall value is not supported.  The diagnostic described below has
a genuine interior cell minimum for

\[
 (r,p,m,f,\alpha)=(1,5,5,2,0.999999),
\]

approximately \(9.3\times10^{-4}\) below its lower-wall value.  Both values
remain strongly positive.  Hence the next proof must control the unique
stationary value itself (or compare it with a lower wall plus an explicit
convexity correction); bare endpoint dominance is not a valid general lemma.

No monotonicity to the single pattern \((r,p,m,f,B)=(1,3,2,2,1)\) has been
proved.  Lemma 2.1 rigorously explains why a smallest-\(r\) endpoint can own a
fixed-\(x\) problem, but only when \(S'(P)\leq0\).  Other intrinsic data have
an interior \(p_*\), so a global assertion of monotonicity in \(r\) or \(p\)
would be false.

## 6. Equality-face audit

1. **Lower shelf wall.**  Equality \(A_t(x)=h\) belongs to the ordinary-floor
   shelf and is included in (3.6) and (4.1).
2. **First-drop wall.**  Equality \(A_t(x+1)=h\) is excluded and occurs only
   as a one-sided upper endpoint.
3. **Start wall.**  Equality \(A_t(r)=h+1\) is excluded.  The prefix endpoint
   \(P\) is bounded jointly by this strict wall and by the grid lower bound on
   \(r=x-p\); either constraint may bind.  The prefix proof never assigns the
   equality face to this branch.
4. **Terminal action wall.**  At \(W+1/4\in\mathbb Z\), the literal bracket
   takes the lower value.  A change of \(B_0\) is not crossed inside the open
   cell (3.2).
5. **Interface wall.**  The face \(\alpha=0\) is the allowed left equality in
   (3.4); \(\alpha=1\) is the excluded right endpoint and only a limit.
6. **The face \(\lambda\downarrow0\).**  It is not in the first-drop branch.
   Its one-sided top payment is \(1\), not the indicator value obtained by
   substituting \(\lambda=0\).
7. **The faces \(r+j=K\).**  As in Round 23, all samples in (1.1) lie at or
   below \(\mu<K\), so no new outer turning equality occurs.

## 7. Loss ledger

The fixed-\(x\) reparametrization, the convexity calculation, the quadratic
cell substitution, and the wall derivatives are exact.  This note discards
no positive term from \(\mathcal C_8\).  The two earlier Round 23 losses --
discarding the elasticity member of \(L_0\) and replacing the exact cap by
\(1/8\) only at the last line -- remain part of the implication
\(\mathcal R_J>\mathcal C_8\); no additional loss is introduced here.

## 8. Reproducible counterexample search

The non-certified script

`computations/general_d_round24_c8_wall_diagnostic.py`

splits every fixed-\(\alpha\) feasible interval at all terminal-action and
top-payment walls, evaluates literal one-sided walls, and minimizes each
smooth convex cell in ordinary double precision.  With

```
python -B computations/general_d_round24_c8_wall_diagnostic.py \
  --limit 8 --floors 6
```

it retained 40,569 feasible fixed-\(\alpha\) tuples on both owner grids for

\[
 1\leq r\leq8\quad\hbox{or}\quad 3/2\leq r\leq17/2,
 \qquad 1\leq p,m\leq8,
\]

\[
 2\leq f\leq6,qquad
 \alpha\in\{0,.1,.25,.5,.75,.9,.99,.999999\}.
\]

No negative value was found.  The smallest sampled value was

\[
 \mathcal C_8\approx0.0128645720672
\]

at the lower shelf wall for

\[
 (r,p,m,f,B_0,\alpha)=(1,3,2,2,1,0.999999).
\]

The smallest sampled minima with owners other than the lower endpoint were
approximately \(0.36709\) at an interior stationary point and \(0.42003\) at
a strict right limit.  These figures are theorem-design evidence only.

The same diagnostic shows that wall values need not be monotone in \(\alpha\):

\[
 \mathcal C_8(1,1,4,2;\alpha=.5)\approx0.760985,
 \qquad
 \mathcal C_8(1,1,4,2;\alpha=.9)\approx0.793791,
\]

whereas the suspected hard family decreases over the same two sampled
values.  This agrees with the competing exact signs in (4.5).

## 9. Next analytic step

The remaining task is not another ratio partition.  On (3.5), one should:

1. use the two exact action balances (3.6) to bound the unique \(t\)-cell
   stationary value, retaining the quadratic \(2u^2\);
2. apply Lemma 2.1 and prove which of its at-most-two candidates can enter a
   small sublevel set;
3. prove monotonicity in \(B\) and the gap label \(m\) only on that sublevel
   set, rather than globally;
4. if that intrinsic comparison does not close, move to the weighted
   aggregate theorem, as required by the simplified strategy.

On the delicate cell the blocker is
\(\widehat{\mathcal C}_8\geq0\) under
\(B=f-1\in\mathbb N\), \(0<u<1/\sqrt2\), (1.1), (3.3)--(3.4), strict
activity, and the coupled rule (5.1).  The remaining payment/action cells
retain the original \(\mathcal C_8\geq0\) obligation with the fixed-\(x\)
candidate reduction.  The general theorem remains open.
