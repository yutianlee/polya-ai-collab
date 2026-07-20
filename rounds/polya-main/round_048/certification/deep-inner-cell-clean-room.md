# Round 48 clean-room proof: deep-inner inverse-action cell

Obligation: `SHELL-general-d-d4-deep-inner-action-cell-round48`

Independence: the reviewer received only the lemma packet and did not read
the discovery or lead proof.  Verdict: **PASS**.

For (z=\xi(t)), define

\[
 \phi(u)=2\arcsin u-\frac{u}{\sqrt{1-u^2}}.
\]

The permitted inner formula gives

\[
 F''(t)=\frac{z(2\sigma(z)-z\sigma'(z))}{\sigma(z)^3},
 \qquad
 2\sigma-z\sigma'=\frac{\phi(z/\mu)-\phi(z/K)}\pi.
\]

Because

\[
 \phi'(u)=\frac{1-2u^2}{(1-u^2)^{3/2}}\ge0
 \quad(0\le u\le1/\sqrt2),
\]

(F) is convex wherever (z\le\mu/\sqrt2), hence on the whole packet
cell.  Convexity at the midpoint gives

\[
 \int_{n-1}^nF(t)\,dt\ge F(n-1/2)=\frac{s^3}{3},
 \qquad s=\xi(n-1/2).
\]

Let (r=\xi(n-1/4)).  On ([r,s]), (\sigma(z)<1/4); therefore

\[
 \frac14=A(r)-A(s)=\int_r^s\sigma(z)\,dz<\frac{s-r}{4},
\]

so (s>r+1).  With (N=\lceil r\rceil-1<r),

\[
 \int_{n-1}^nF(t)\,dt
 >\frac{(r+1)^3}{3}
 >\frac{(N+1)^3}{3}
 =S_2(N)+\frac{N^2}{2}+\frac{5N}{6}+\frac13.
\]

This independently proves (L_n>0), including (N=0).  The four displayed
differences form an explicit nonnegative loss ledger: midpoint tangent gap,
the strict (s>r+1) gain, the strict (r>N) gain, and the final positive
polynomial reserve.  The endpoint (H_0) is harmless because
(F(t)=O((H_0-t)^{3/2})).  Integer (r), the face (n-1=t_*), and
near-integer (K,\mu) introduce no extra term.  No claim beyond the packet
is made.  First unsupported implication: none.
