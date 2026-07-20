# Round 48 adversarial audit: full outer inverse-action cell

Candidate: `SHELL-general-d-d4-full-outer-action-cell-round48`
Role: adversarial reviewer
Verdict: **PASS**

The reviewer reconstructed the packet claim from the lead and independent
clean-room artifacts and found no unsupported implication.

## Lead reconstruction

The hypothesis \(n\le t_\mu=A(\mu)<H\) puts the whole complete cell in the
outer branch.  Splitting at \(t_0=n-1/4\) gives exactly

\[
L_n=\frac{r^3}{3}-S_2(N)
+\int_0^{3/4}(3/4-v)J(t_0-v)\,dv
-\int_0^{1/4}(1/4-v)J(t_0+v)\,dv.
\]

Outer monotonicity gives, with \(h_0=h(r)\),

\[
J(t_0-v)\ge\frac{(r+v/h_0)^2}{h_0},
\qquad
J(t_0+v)\le\frac{r^2}{h_0}.
\]

The resulting coefficients and the direction of the adverse future term are
correct:

\[
L_n\ge\frac{r^3}{3}-S_2(N)
+\frac{r^2}{4h_0}
+\frac{9r}{64h_0^2}
+\frac{27}{1024h_0^3}.
\]

Using \(h_0\le1/2\), \(N<r\le N+1\), and monotonicity of the resulting
polynomial proves the packet bound.  The lead loss equality

\[
L_n=\frac{19N}{48}+\frac{27}{128}+E_-+E_++E_h+E_r
\]

is exact, and all four losses have the stated signs.

## Clean-room reconstruction

The independent quantile coordinate \(q=n-A(z)\) gives

\[
3I_n=\int_0^1z(q)^3\,dq,
\qquad z'(q)=1/h(z(q))\ge2.
\]

Since outer \(h\) decreases, \(z\) is convex.  With
\(d=r-\xi(n)\), one has \(r\ge d\ge1/2\).  The two affine lower envelopes
used in the clean proof have the correct direction.  Differentiation of its
polynomial \(E(r,d)\) reproduces

\[
\partial_dE=
\frac{21}{8}r^2+15rd+\frac{231}{16}d^2
-\frac38r+\frac38d-\frac1{16}>0
\]

on \(r\ge d\ge1/2\).  The subsequent \(N\ge1\) and \(N=0\) arithmetic is
correct.

## Adversarial faces

- At integer \(r\), strict counting gives \(N=r-1\), so \(r>N\) remains
  strict.
- At the dangerous counted-side face \(r\downarrow N\), the positive
  polynomial reserve remains.
- The \(N=0\) case is covered independently in both proofs.
- For \(n=1\), the lead kernel at \(t=0\) is an improper but integrable
  limit because it is a difference of the continuous monotone function
  \(F\); the clean proof extends to its endpoint by continuity.
- At \(n=t_\mu\), only the cell endpoint is the interface, so no inner term
  is introduced.
- Integer/near-integer \(K,\mu\), \(\rho\downarrow0\), and the packet's
  nontruncation/non-straddling scope introduce no missing term.

This PASS applies only to the bounded outer-cell lemma.  It says nothing
about inner cells, the interface cell, a truncated top cell, QCL globally,
or \(\mathrm{WT}_4\).
