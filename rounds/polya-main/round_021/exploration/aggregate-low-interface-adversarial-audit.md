# Adversarial audit: aggregate low-interface route

Date: 2026-07-15.

## Scope and authentication

This audit read only the route and its three declared inputs.  All four
SHA-256 digests match:

| artifact | authenticated SHA-256 |
|---|---|
| `exploration/aggregate-low-interface-route.md` | `1ca5accb36065335ad7550b476a3f36c8f9eaf3edcc78170a1c8a66194a6e5d5` |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

No other Round 21 file and no Round 20 proof was inspected.

## Verdict

**FAIL as written.**  The aggregate analytic estimate itself passes, as does
the floor-free implication \(\mathcal B\geq0\Rightarrow\mathcal Q>0\).
The first unsupported implication is the consequent in (13): the route
turns the strict coarse weighted-proxy estimate into a statement about the
actual spectral count \(N_D(A_{\rho,1},K^2)\).  The authenticated weighted
lattice packet expressly says that the spectral completeness/count identity
needed for this step is still conditional.  None of the other two inputs
supplies it.  Calling the note an "exact conditional lemma" in its status
line does not state the missing hypothesis in (13), (16), or the proof.

Thus the inputs prove the strict coarse proxy bound below.  They prove the
displayed \(N_D\) conclusion only **conditional on** the spectral
completeness/count identity stated as conditional in
`SHELL-weighted-lattice-fractional.md`.

The admitted absence of a global certificate for \(\mathcal B>0\) on
\(K\geq200\) is not part of this FAIL verdict.

## Reconstruction of the exact analytic chain

Put \(t=\mu-\tfrac12=J+\tau\).  The condition
\(x_r=r+\tfrac12<\mu\) is exactly \(r<J+\tau\).  Hence

\[
 R=J\quad(\tau=0),\qquad R=J+1\quad(0<\tau<1).
\]

In particular, the often-mishandled wall \(\tau=0\) has \(J\), not
\(J+1\), low tails.  For every allowed \(r\),

\[
 n_r=\lfloor J+\tau-r\rfloor=J-r,
 \qquad q_r=r+\frac12+J-r=J+\frac12=\mu-\tau.
\]

For \(\tau=0\), the indices are \(0\leq r\leq J-1\), so the \(n_r\)'s
are \(J,J-1,\ldots,1\).  For \(\tau>0\), the additional last cell has
\(r=J,n_J=0\).  Both cases give

\[
 \sum_{r<R}n_r=\frac{J(J+1)}2.
\]

All split points are therefore the same, and the source-card bound applies
because \(q_r=J+\tfrac12>0\):

\[
 \delta_\tau=\int_{\mu-\tau}^{\mu}G_\mu(z)\,dz
 \leq \frac{2\tau^{5/2}}{15\sqrt\mu}.
\]

At \(\tau=0\), the integral and its bound both equal zero.

For a first-shelf length \(p_r\), the authenticated one-tail packet gives

\[
 1>A(x_r)-A(x_r+p_r)
 \geq\frac\kappa2\bigl(p_r^2+2x_rp_r\bigr),
 \qquad \kappa=\frac{1-\rho}{\pi\rho K}.
\]

Since \(2/\kappa=C\), this is exactly

\[
 p_r^2+2x_rp_r<C,
 \qquad p_r<\sqrt{x_r^2+C}-x_r=P_C(x_r).
\]

The inequality is strict also when the no-drop convention gives
\(p_r=n_r\), and is harmless for the \(n_r=p_r=0\) cell.

Next,

\[
 P_C''(x)=\frac{C}{(x^2+C)^{3/2}}>0.
\]

The midpoint Hermite--Hadamard inequality for a convex function has the
direction

\[
 P_C\!\left(r+\frac12\right)
 \leq\int_r^{r+1}P_C(x)\,dx.
\]

Consequently

\[
 \sum_{r<R}p_r<\int_0^R P_C(x)\,dx=\mathcal I(C,R).
\]

Here \(R\geq1\) follows from the standing assumption \(\mu>1/2\), so the
strict sum is not an empty-sum artifact.  Direct integration gives

\[
 \mathcal I(C,R)=\frac12\left[
 R\sqrt{R^2+C}+C\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right)-R^2
 \right],
\]

so (7)--(9), including the Hermite--Hadamard direction, are correct.

Let

\[
 S:=\sum_{r<R}M_r,
 \qquad
 U:=\frac{8R\tau^{5/2}}{15\sqrt\mu}.
\]

Summing the authenticated formula for \(M_r\) gives, with no missing
endpoint term,

\[
 S=R\lfloor K\eta_\rho\rfloor
 +d_\rho\frac{J(J+1)}2
 -(1+d_\rho)\sum_{r<R}p_r.
\]

The strict shelf bound gives

\[
 S>
 R\lfloor K\eta_\rho\rfloor
 +d_\rho\frac{J(J+1)}2
 -(1+d_\rho)\mathcal I(C,R)
 =\mathcal Q+U.
\]

Meanwhile \(4R\delta_\tau\leq U\).  Thus

\[
 \mathcal Q\geq0\quad\Longrightarrow\quad
 S>U\geq4R\delta_\tau.
\]

This verifies both factors in the route: the factor \(4\) comes from the
\(-M_r/4\) in the one-tail estimate, and the factor \(8\) in \(U\) is
\(4\) times the factor \(2\) in the interface bound.  Summing (10) gives

\[
 \frac12\sum_{r<R}\mathcal T_r
 \leq\sum_{r<R}\int_{x_r}^K A(z)\,dz
 +R\delta_\tau-\frac S4
 <\sum_{r<R}\int_{x_r}^K A(z)\,dz.
\]

Multiplication by \(2\), followed by the accepted non-strict bounds for
the high tails, gives a strict bound for the sum of all tail majorants.  At
\(\tau=0\), \(U=\delta_0=0\), while
\(S>\mathcal Q\geq0\), so strictness survives that wall exactly as claimed.

For clarity, what the authenticated inputs then prove unconditionally is
the coarse proxy inequality

\[
 \begin{aligned}
 \mathcal P_{\rm coarse}
 &: =\sum_{\nu_\ell<K}2\nu_\ell
       [A_{\rho,K}(\nu_\ell)+\tfrac14]_< \\
 &<2\sum_{r\geq0}\int_{r+1/2}^K A_{\rho,K}(z)\,dz
 =2\int_0^K f_3(z)A_{\rho,K}(z)\,dz \\
 &\leq\int_0^K2zA_{\rho,K}(z)\,dz
 =\frac{2}{9\pi}(1-\rho^3)K^3.
 \end{aligned}
\]

The first inequality uses the exact dimension-reduction identity and the
ordinary-floor tail majorants; the second uses \(F_3(z)\leq z^2/2\), the
sign \(-A'\geq0\), and integration by parts.  These steps and their factor
\(2\) are authorized by the weighted lattice packet.  The subsequent
replacement of \(\mathcal P_{\rm coarse}\) by the actual spectral count is
the first step that is not authorized unconditionally.

## Audit of the floor-free reserve

The reserve comparison is also correct under the standing
\(\mu>1/2\) assumption and the stated \(K\eta_\rho>1\) assumption.  In
detail,

\[
 R\geq\mu-\frac12,
 \qquad R\leq\mu+\frac12,
\]

and, writing \(\mu-\tfrac12=J+\tau\),

\[
 J(J+1)-\left(\mu-\frac32\right)
             \left(\mu-\frac12\right)
 =(1-\tau)(2J+\tau)\geq0.
\]

Also \(\lfloor x\rfloor>x-1\) for every real \(x\), including integer
walls.  Since \(R>0\) and \(K\eta_\rho-1>0\),

\[
 R\lfloor K\eta_\rho\rfloor
 >(\mu-\tfrac12)(K\eta_\rho-1).
\]

The derivative \(\partial_R\mathcal I(C,R)=P_C(R)>0\) gives the stated
monotonicity, while

\[
 R\tau^{5/2}<\mu+\frac12
\]

(a weak inequality would already suffice) gives the floor-free interface
term.  Combining these comparisons yields the stronger relation

\[
 \mathcal Q(\rho,K)>\mathcal B(\rho,K).
\]

Therefore \(\mathcal B\geq0\Rightarrow\mathcal Q>0\) is valid, with the
strictness supplied already by the floor estimate.  What follows is strict
coarse-proxy positivity unconditionally, and strict Pólya only under the
missing spectral completeness/count hypothesis.

## Independent diagnostic reproduction (nonproof)

The following values are direct high-precision numerical evaluations of
the displayed formula (15).  They use no outward interval arithmetic and
make no claim about persistence between sample points or for unbounded
\(K\); they are **diagnostic only**.

| \(\rho\) | threshold printed in the route | \(\mathcal B\) at that printed \(K\) | diagnostic zero of \(\mathcal B\) | first integer after that zero |
|---:|---:|---:|---:|---:|
| \(1/5\) | 63 | -7.8926671362 | 69.6071699348 | 70 |
| \(3/10\) | 74 | -9.3917675099 | 77.9360406932 | 78 |
| \(2/5\) | 79 | -19.2329004605 | 83.8659533780 | 84 |
| \(1/2\) | 83 | -38.8841354067 | 89.3262056579 | 90 |
| \(3/5\) | 115 | -17.5982437374 | 116.6359557523 | 117 |
| \(13/20\) | 127 | -65.6792306045 | 131.8950283694 | 132 |
| \(39/50\) | 184 | -62.5687260156 | 186.2229644177 | 187 |

Thus every reproducible row in the route's table is false as a threshold
for the displayed \(\mathcal B>0\).  For example,
\(\mathcal B(1/5,63)<0\), whereas
\(\mathcal B(1/5,69)\approx-0.8026442748\) and
\(\mathcal B(1/5,70)\approx0.5276784288\).

The symbol \(\rho_c\) is not defined anywhere in the route or its three
authenticated inputs.  Therefore its table row, the rectangle endpoint,
and the claimed minimum near \((\rho_c,200)\) cannot be independently
reproduced from the permitted corpus.  The grid itself is also not
specified.  These are defects in the diagnostic record, not a substitute
for the outward certificate that the route correctly says is still needed.

## Required patch

1. Replace the consequent of (13) by the strict coarse-proxy inequality
   displayed above.  Then add a separate sentence: *assuming the spectral
   completeness/count identity from the weighted lattice packet, this
   implies the stated strict bound for \(N_D\).*  Make the same separation
   in (16), its prose proof, and the current-verdict section.
2. Define \(\rho_c\) exactly before using it.
3. If the diagnostic table is intended to report (15), recompute it.  The
   numerical crossings above give the reproducible rational-row targets,
   but must remain labelled nonproof.  Otherwise rename the quantity that
   was actually evaluated and provide its formula.  Record the diagnostic
   grid if the minimum claim is retained.

No patch is required to (3)--(12), the definition of \(\mathcal Q\), the
implication \(\mathcal Q\geq0\) to strict aggregate tail compensation, the
formula (15), or the implication \(\mathcal B\geq0\Rightarrow\mathcal Q>0\).
