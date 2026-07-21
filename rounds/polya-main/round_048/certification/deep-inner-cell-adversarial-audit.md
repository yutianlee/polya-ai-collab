# Round 48 adversarial audit: deep-inner inverse-action cell

Obligation: `SHELL-general-d-d4-deep-inner-action-cell-round48`

The adversarial reviewer received the packet after the lead and clean-room
outputs were frozen and did not use either proof as a premise.  Verdict:
**PASS for the bounded statement**.

The reviewer reconstructed

\[
 F''(t)=\frac{z(2\sigma-z\sigma')}{\sigma^3}>0,
 \qquad
 2\sigma-z\sigma'=
 \frac{\phi(z/\mu)-\phi(z/K)}\pi,
\]

where

\[
 \phi'(u)=\frac{1-2u^2}{(1-u^2)^{3/2}}\ge0
 \quad(0\le u\le1/\sqrt2).
\]

It also checked that (n-1\ge t_*) truly confines every point of the cell
to (z\le\mu/\sqrt2).  Integrating the tangent at (n-1/4) yields

\[
 \int_{n-1}^nF\ge\frac{r^3}{3}+\frac{r^2}{4\sigma(r)}
 >\frac{r^3}{3}+r^2.
\]

The strict version is valid because the node is interior to the deep cell,
so (r<\mu/\sqrt2).  Literal (N=\lceil r\rceil-1<r) and

\[
 \frac{N^3}{3}+N^2-S_2(N)=\frac{N(3N-1)}6
\]

finish the (N\ge1) case; (N=0) is separate and immediate.

Falsification faces checked: (r\in\mathbb Z), (r\downarrow N), (N=0),
(n-1=t_*), (n=H_0), and integer or near-integer (K,\mu).  At
(H_0), (F'\to0), so the convex extension is valid.  A shallower or
interface cell violates the confinement hypothesis and is expressly outside
scope.  There is no truncation or rounding loss hidden in the proof.

First unsupported implication: none.  This audit does not sign any other
cell or infer global QCL or \(\mathrm{WT}_4\).
