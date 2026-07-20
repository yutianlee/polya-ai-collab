# Round 48 lead proof: deep-inner inverse-action cell

Obligation: `SHELL-general-d-d4-deep-inner-action-cell-round48`

Verdict: **PASS for the packet statement only**.

Put (z=\xi(t)) and

\[
 \sigma(z)=\frac{\arcsin(z/\mu)-\arcsin(z/K)}\pi.
\]

On the inner branch,

\[
 \sigma(z)=\int_\mu^K
 \frac{z}{\pi R\sqrt{R^2-z^2}}\,dR.
\]

For the integrand (s_R), direct differentiation gives

\[
 2s_R(z)-zs_R'(z)=
 \frac{z(R^2-2z^2)}{\pi R(R^2-z^2)^{3/2}}.
\]

Thus (2\sigma-z\sigma'\ge0) whenever (z\le\mu/\sqrt2).
Inverse differentiation gives

\[
 F'(t)=-\frac{z^2}{\sigma(z)},\qquad
 F''(t)=\frac{z(2\sigma(z)-z\sigma'(z))}{\sigma(z)^3}\ge0.
\]

The hypothesis (n-1\ge t_*=A(\mu/\sqrt2)), together with the fact that
(\xi) is decreasing, confines all of ([n-1,n]) to this convexity
region.  At (c=n-1/4), with (r=\xi(c)), the tangent inequality therefore
gives

\[
 \int_{n-1}^nF(t)\,dt
 \ge F(c)-\frac14F'(c)
 =\frac{r^3}{3}+\frac{r^2}{4\sigma(r)}.
\]

Since (r\le\mu/\sqrt2),

\[
 0<\sigma(r)
 \le\frac{\arcsin(1/\sqrt2)}\pi=\frac14,
\]

so the supply is at least (r^3/3+r^2).  Literal strict-ceiling
arithmetic gives (N=\lceil r\rceil-1<r\).  For (N\ge1),

\[
 \frac{r^3}{3}+r^2>
 \frac{N^3}{3}+N^2
 =S_2(N)+\frac{N(3N-1)}6>S_2(N).
\]

For (N=0), the supply is positive while (S_2(0)=0).  Hence (L_n>0).

The proof includes (r\in\mathbb Z), where (N=r-1), the face
(n-1=t_*), and a cell ending at (H_0) by continuous extension at
(F(H_0)=0).  It does not claim a shallower, interface-straddling, or
truncated cell.

Loss ledger: the shell representation and curvature identity are exact;
the tangent replacement, (\sigma\le1/4), and (r>N) are the only
one-sided steps.  No numerical premise is used.  First unsupported
implication: none within the packet.
