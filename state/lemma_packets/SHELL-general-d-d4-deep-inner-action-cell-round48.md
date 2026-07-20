# Lemma Packet: Deep-Inner Inverse-Action Cell in \(d=4\)

Candidate obligation: `SHELL-general-d-d4-deep-inner-action-cell-round48`

This packet promotes one bounded Round 48 discovery claim into obligation
certification.  It does not change any mathematical status by itself.

## Exact statement

Use the shell action

\[
 A(z)=G_K(z)-G_\mu(z),\qquad
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}\pi,
\]

with zero extension, where \(0<\mu<K\).  Put

\[
 H_0=A(0),\qquad t_*=A(\mu/\sqrt2),
\]

let \(\xi:[0,H_0]\to[0,K]\) be the decreasing inverse of \(A\), and set

\[
 F(t)=\frac{\xi(t)^3}{3}.
\]

Let \(n\ge1\) be an integer such that the height cell is complete and lies
deep in the inner branch:

\[
 n\le H_0,qquad n-1\ge t_*.
\]

With

\[
 r=\xi(n-\tfrac14),qquad N=\lceil r\rceil-1,qquad
 S_2(N)=\frac{N(N+1)(2N+1)}6,
\]

prove

\[
 \boxed{
 L_n:=\int_{n-1}^{n}F(t)\,dt-S_2(N)>0.}
\]

The ceiling convention is literal at integer \(r\).

## Permitted dependencies

Only the definitions above and the following elementary tools may be used:

1. \(A'=-\sigma\), inverse-function calculus, and differentiation under a
   finite integral.
2. The exact inner-branch formula
   \[
   \sigma(z)=\frac{\arcsin(z/\mu)-\arcsin(z/K)}\pi.
   \]
3. Convex tangent inequalities, the exact sum-of-squares formula, and strict
   ceiling arithmetic.

Do not use the Round 48 discovery proof, the outer-cell proof, pointwise
shifted-tail positivity, or numerical sampling as a premise.

## Required boundary and falsification cases

- \(r\in\mathbb Z\), where \(N=r-1\).
- \(r\downarrow N\) from the counted side.
- \(N=0\).
- The boundary \(n-1=t_*\), so \(\xi(n-1)=\mu/\sqrt2\).
- A cell ending at \(H_0\), interpreted by the inverse endpoint.
- Verify that a cell touching the shallower interface region is not claimed.
- Integer and near-integer \(K,\mu\) must introduce no extra term.

## Expected artifacts

Lead, clean-room, and adversarial artifacts must give exact curvature and
tangent calculations, strict-floor arithmetic, a loss ledger, and the first
unsupported implication or PASS.  No claim about shallow-inner,
interface-straddling, truncated, global QCL, or \(\mathrm{WT}_4\) may be
inferred from this packet.
