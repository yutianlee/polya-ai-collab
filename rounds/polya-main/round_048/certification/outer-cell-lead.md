# Round 48 certification lead: full outer inverse-action cell

Candidate: `SHELL-general-d-d4-full-outer-action-cell-round48`
Role: lead author

Use the notation and hypotheses of
`state/lemma_packets/SHELL-general-d-d4-full-outer-action-cell-round48.md`.  Put

\[
t_0=n-\frac14,\quad \alpha=\frac34,\quad \beta=\frac14,
\quad r=\xi(t_0),\quad h_0=h(r),
\]

where \(h=-A'\).  Since \(n\le t_\mu<A(0)\), the cell is complete and
\(\xi(t)\ge\mu\) for \(0\le t\le n\).  Thus it lies wholly in the outer
branch, where \(h(z)=\arccos(z/K)/\pi\) decreases with \(z\).

## Exact kernel identity

Let

\[
F(t)=\frac{\xi(t)^3}{3},\qquad
J(t)=-F'(t)=\frac{\xi(t)^2}{h(\xi(t))}.
\]

Integrating the identities for \(F(t_0-s)-F(t_0)\) and
\(F(t_0+s)-F(t_0)\) over the two triangular kernels gives

\[
L_n=\frac{r^3}{3}-S_2(N)
+\int_0^\alpha(\alpha-v)J(t_0-v)\,dv
-\int_0^\beta(\beta-v)J(t_0+v)\,dv. \tag{1}
\]

For \(x_v=\xi(t_0-v)\ge r\),

\[
v=\int_r^{x_v}h(u)\,du\le h_0(x_v-r),
\]

so

\[
J(t_0-v)\ge\frac{(r+v/h_0)^2}{h_0}. \tag{2}
\]

For \(y_v=\xi(t_0+v)\le r\), the same outer monotonicity gives

\[
J(t_0+v)\le\frac{r^2}{h_0}. \tag{3}
\]

Substitution into (1), with the adverse future term subtracted, yields

\[
L_n\ge \frac{r^3}{3}-S_2(N)
+\frac{r^2}{4h_0}
+\frac{9r}{64h_0^2}
+\frac{27}{1024h_0^3}. \tag{4}
\]

Because \(0<h_0\le1/2\),

\[
 L_n\ge Q_N(r):=\frac{r^3}{3}-S_2(N)
+\frac{r^2}{2}+\frac{9r}{16}+\frac{27}{128}. \tag{5}
\]

The literal ceiling convention gives \(N<r\le N+1\), including at an
integer action wall.  Since

\[
Q_N'(r)=r^2+r+\frac9{16}>0,
\]

and

\[
Q_N(N)=\frac{19N}{48}+\frac{27}{128},
\]

we conclude

\[
\boxed{L_n>\frac{19N}{48}+\frac{27}{128}>0.}
\]

## Exact loss ledger

The kernel identity is exact.  The losses are the four nonnegative terms

\[
\begin{aligned}
E_-&=\int_0^{3/4}(3/4-v)
\left[J(t_0-v)-\frac{(r+v/h_0)^2}{h_0}\right]dv,\\
E_+&=\int_0^{1/4}(1/4-v)
\left[\frac{r^2}{h_0}-J(t_0+v)\right]dv,\\
E_h&=r^2\left(\frac1{4h_0}-\frac12\right)
+\frac{9r}{64}\left(\frac1{h_0^2}-4\right)
+\frac{27}{1024}\left(\frac1{h_0^3}-8\right),\\
E_r&=\int_N^r\left(u^2+u+\frac9{16}\right)du.
\end{aligned}
\]

Thus

\[
L_n=\frac{19N}{48}+\frac{27}{128}+E_-+E_++E_h+E_r.
\]

Here \(E_r>0\).  If \(r\in\mathbb Z\), strictness gives \(N=r-1\).
The case \(N=0\), the endpoint \(n=t_\mu\), and integer/near-integer
\(K,\mu\) introduce no additional term.  The proof does not apply to a
straddling or truncated cell.
