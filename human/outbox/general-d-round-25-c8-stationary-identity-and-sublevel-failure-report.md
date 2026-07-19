# General dimension, Round 25: stationary identity and sublevel failure report

Date: 19 July 2026  
Status: rigorous stationary reduction; the C8 sign remains open

## 0. Scope and theorem boundary

This note treats only the delicate Round 24 cell

\[
 B=f-1\geq1,\qquad 0<u<1/\sqrt2,
\]

at an interior stationary point of the fixed-\(\mu\) \(t\)-cell.  It proves
an exact identity for that stationary value, two alpha-free necessary shelf
conditions, and one rigorous lower reduction which eliminates \((r,p,\alpha)\).
The resulting scalar is not nonnegative on the relaxed necessary-condition
domain.  Thus this round does not prove \(\mathcal C _8\geq0\), CST-H, or the
general-dimensional Polya theorem.

## 1. Statement

Put

\[
 H=\tan t-t,\quad z=\tan(t/2),\quad
 \mu={\pi(B+u)\over H},\quad \delta={3\over4}-u,
\]

and suppose the exact Round 24 shelf, interface, activity, and strict-wall
conditions hold.  If \(\partial_t\mathcal C _8=0\) in the open quadratic
cell, define

\[
 L={4u(B+u)\tan ^2t\over H},\qquad
 R={m\over\pi}+{B\pi\over2t^2}-L.                         \tag{1.1}
\]

Then

\[
 R>0,
\]

and the stationary value has the exact form

\[
\boxed{
 \begin{aligned}
 \mathcal C _8={}&m\left({1\over2}-{t\over\pi}+{z\over\pi}\right)
 +B\left({\pi\over2t}-1+{\pi z\over2t^2}\right)-{p\over2}-{1\over8}\\
 &+2u^2-zL .
 \end{aligned}}                                           \tag{1.2}
\]

Moreover the two shelf walls imply the strict necessary conditions

\[
 \boxed{
 { (1-\cos t)(m-1)(2\mu-m+1)\over2\pi\mu}
 <\delta<{(m+1)t\over\pi}.}                              \tag{1.3}
\]

Let \(\psi(P)\) denote the positive root of

\[
 \psi^2(2\psi+3)=P,
\]

where

\[
 P={3\pi^2(B+u)R\over H\sin t}.                           \tag{1.4}
\]

Then every such stationary point obeys

\[
 p\leq p_{\max}:=\min\{\mu-m-1,\psi(P)\},                \tag{1.5}
\]

and hence

\[
\boxed{
 \mathcal C _8\geq \mathcal F(B,m,t,u),}                 \tag{1.6}
\]

where

\[
\begin{aligned}
 \mathcal F={}&m\left({1\over2}-{t\over\pi}+{z\over\pi}\right)
 +B\left({\pi\over2t}-1+{\pi z\over2t^2}\right)\\
 &+2u^2-zL-{1\over8}-{p_{\max}\over2}.                  \tag{1.7}
\end{aligned}
\]

Thus \(\mathcal F\geq0\) on the *full projected shelf image* would close
all interior stationary candidates on this cell.  Equations (1.1), (1.3),
\(\mu-m-1\geq1\), and the activity wall are necessary but are not by
themselves a sufficient description of that image.

## 2. Dependencies

Only the audited Round 23 formula for \(\mathcal C _8\), the audited Round
24 elimination \(W=B+u\), and the exact Round 24 shelf inequalities are
used.  No ratio owner, interval certificate, or unproved monotonicity is a
dependency.

## 3. Proof

At fixed \(\mu\), differentiation on the quadratic top-payment cell gives

\[
 {p^2(3r+2p)\sin t\over3\pi\mu}
 -{m\over\pi}-{B\pi\over2t^2}
 +{4u\mu\tan^2t\over\pi}=0.                              \tag{3.1}
\]

The first term is positive.  Substituting
\(\mu=\pi(B+u)/H\) into (3.1) gives (1.1), \(R>0\), and

\[
 {p^2(3r+2p)H\sin t\over3\pi^2(B+u)}=R.                 \tag{3.2}
\]

The curvature *value* in \(\mathcal C _8\) is the left side of (3.2)
multiplied by

\[
 {1-\cos t\over\sin t}=\tan(t/2)=z.
\]

Replacing it by \(zR\) and collecting the \(m\)- and \(B\)-terms proves
the exact identity (1.2).  This step discards nothing.

For the shelf bounds, write

\[
 \sigma(s)={\arccos(s\cos t/\mu)-\arccos(s/\mu)\over\pi}.
\]

Then

\[
 A(x)-W=\int_x^\mu\sigma(s)\,ds\geq\delta,
 \qquad
 A(x+1)-W=\int_{x+1}^\mu\sigma(s)\,ds<\delta.             \tag{3.3}
\]

For \(0<s<\mu\), one has \(0<\sigma(s)<t/\pi\).  Since
\(\mu-x=m+\alpha<m+1\), the first relation in (3.3) gives the
right inequality in (1.3).

For the other side, the function

\[
 y\longmapsto\arccos(y\cos t)-\arccos y
\]

is strictly convex on \((0,1)\), vanishes at zero, and has derivative
\(1-\cos t\) there.  Therefore

\[
 \sigma(s)>{(1-\cos t)s\over\pi\mu}.                    \tag{3.4}
\]

Now \(\mu-(x+1)=m+\alpha-1\geq m-1\), and the integral of the
right side of (3.4) over \([\mu-(m-1),\mu]\) is

\[
 {(1-\cos t)(m-1)(2\mu-m+1)\over2\pi\mu}.
\]

The second strict relation in (3.3) proves the left inequality in (1.3).

Finally, (3.2) is equivalent to

\[
 p^2(3r+2p)=P.
\]

Because every owner has \(r\geq1\),

\[
 P\geq p^2(2p+3),
\]

so monotonicity of \(s^2(2s+3)\) gives \(p\leq\psi(P)\).  The interface
identity gives

\[
 p=\mu-m-\alpha-r\leq\mu-m-1.
\]

This proves (1.5), and replacing only the negative term \(-p/2\) in the
exact identity proves (1.6)--(1.7).

## 4. Equality-face audit

1. The lower shelf equality \(A(x)=B+3/4\) is included; (3.3) uses a weak
   inequality there.
2. The first-drop equality \(A(x+1)=B+3/4\) is excluded; it is the source
   of the strict left inequality in (1.3).
3. The interface face \(\alpha=0\) is included.  The estimate
   \(p\leq\mu-m-1\) remains valid.  The face \(\alpha=1\) is excluded and
   may only be approached.
4. The action walls \(u=0\) and \(u=1/\sqrt2\) are outside this open cell.
5. A stationary point cannot have \(R=0\), since the curvature derivative
   in (3.2) is strictly positive.
6. As in Round 24, all shelf samples lie below \(\mu<K\); no new
   \(r+j=K\) equality occurs.

## 5. Loss ledger

The stationary identity and the two inequalities (1.3) are exact
consequences of the retained shelf relations.  The only loss is in (1.5):
the exact integer \(p\), exact parity lower bound on \(r\), and exact
\(\alpha\) are replaced by the two continuous upper bounds.  This loss is
one-sided and harmless if (1.7) can be proved nonnegative, but it is too
large on the relaxed domain described next.

## 6. Counterexample search and reproducible diagnostic

Run

```text
python -B computations/general_d_round25_c8_stationary_sublevel_diagnostic.py
```

The script recomputes the Round 24 feasible stationary witness

\[
 (r,p,m,B,\alpha)=(1,5,5,1,0.999999),
\]

checks (3.1), and compares the direct value with (1.2).  Ordinary double
precision gives \(\mathcal C _8\approx0.36709\), while the lower scalar
\(\mathcal F\) agrees to the displayed minimization tolerance.  This is
theorem-design evidence, not proof.

The same script evaluates the relaxed point

\[
 (B,m,t,u)=(1,11,1/5,1/1000).
\]

It satisfies \(R>0\), \(\mu-m-1>1\), and both strict necessary
inequalities (1.3), but gives \(\mathcal F\approx-36.7\).  This point is
not asserted to satisfy the full shelf equations.  Its purpose is precise:
the scalar conditions (1.1), (1.3), and (1.5) cannot replace the projected
shelf image.

## 7. Failure report and exact remaining inequality

The stationary branch is reduced to the single inequality

\[
 \boxed{\mathcal F(B,m,t,u)\geq0}                         \tag{7.1}
\]

on the **full projection** of the exact two shelf relations (3.3), the
interface strip, activity, and the at-most-two discrete \(p\)-owners.  A
proof using only the endpoint estimates (1.3) is impossible, as the relaxed
diagnostic above shows.  The missing information is the shape of the entire
integrals in (3.3), not another ratio threshold.

A next analytic attempt should retain

\[
 \int_x^\mu\sigma\geq\delta>
 \int_{x+1}^\mu\sigma
\]

when bounding \(p_{\max}\), or else pass to the strategy-approved weighted
aggregate theorem.  No global monotonicity in \(\alpha\), \(B\), or \(m\)
has been assumed here.  The C8 sign and the general theorem remain open.
