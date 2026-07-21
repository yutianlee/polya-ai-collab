# Lemma Packet: Full Outer Inverse-Action Cell in \(d=4\)

Candidate obligation: `SHELL-general-d-d4-full-outer-action-cell-round48`

This packet promotes one bounded Round 48 discovery claim into obligation
certification.  It does not change any mathematical status by itself.

## Exact statement

Let

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi}
 \quad(0\le z\le R),
\]

with zero extension.  Fix \(0<\rho<1\), \(K>0\), put
\(\mu=\rho K\), and define

\[
 A=G_K-G_\mu,
 \qquad H=A(0)=\frac{K-\mu}{\pi}.
\]

Let \(\xi:[0,H]\to[0,K]\) be the decreasing inverse of \(A\), so
\(A(\xi(t))=t\), and put

\[
 F(t)=\frac{\xi(t)^3}{3},
 \qquad t_n=n-\frac14.
\]

For an integer \(n\ge1\), assume that the complete height cell lies in the
outer branch:

\[
 n\le t_\mu:=A(\mu)=G_K(\mu).
\]

Set

\[
 r=\xi(t_n),
 \qquad N=\lceil r\rceil-1,
 \qquad S_2(N)=\frac{N(N+1)(2N+1)}6,
\]

where the ceiling convention is literal also when \(r\in\mathbb Z\).  Prove

\[
 \boxed{
 L_n:=\int_{n-1}^{n}F(t)\,dt-S_2(N)
 >\frac{19N}{48}+\frac{27}{128}>0.}
\]

No strict-active hypothesis is needed beyond the displayed assumptions; in
the Round 48 application it is available globally.

## Permitted dependencies

Only the following elementary facts may be used:

1. \(G_R'(z)=-\arccos(z/R)/\pi\) for \(0<z<R\).
2. \(A\) is continuous and strictly decreasing on \([0,K]\).
3. On the outer branch \(z\ge\mu\),
   \[
   h(z):=-A'(z)=\frac{\arccos(z/K)}\pi,
   \]
   so \(0<h\le1/2\) and \(h\) decreases with \(z\).
4. The exact sum-of-squares formula for \(S_2(N)\).
5. Elementary inverse-function calculus, integration by parts, and monotone
   integral comparison.

Do not use the Round 48 discovery proof, the incumbent component inequality,
pointwise shifted-tail positivity, or a computational sign certificate as a
premise.

## Required boundary and falsification cases

- \(r\in\mathbb Z\): strict counting gives \(N=r-1\).
- \(r\downarrow N\) from the dangerous counted side.
- \(N=0\).
- \(n=t_\mu\): the height cell may end exactly at the inner interface.
- \(\rho\downarrow0\), where the interface collapses.
- Integer and near-integer \(K\) and \(\mu\); these must create no extra
  endpoint term.
- Verify that the claim is not applied to an interface-straddling or
  truncated height cell.

## Expected artifacts

The lead proof and clean-room reconstruction must each give an exact kernel
or integral derivation, every inequality direction, and a loss ledger.  The
adversarial review must identify the first unsupported implication or return
PASS after checking all boundary cases.  No state promotion occurs before
that review and root validation.
