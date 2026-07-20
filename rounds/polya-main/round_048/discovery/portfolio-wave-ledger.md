# Round 48 portfolio-discovery wave ledger

Target:

\[
 \mathrm{WT}_4=\frac{K^4-\mu^4}{64}
 -\sum_{1\le a<K}a^2[A(a)+1/4]_<\ge0
\]

on (0<\rho<1), \(\mu=\rho K\), and
(K^2>\pi^2/(1-\rho)^2+3/4).

The routes were frozen independently before cross-pollination.  Discovery
agreement was not used as proof evidence.

## Exact common inverse-layer form

Let (H=A(0)), let \(\xi\) be the decreasing inverse of (A), and put

\[
 F(t)=\frac{\xi(t)^3}{3},\qquad t_n=n-\frac14,
 \qquad N_n=\lceil\xi(t_n)\rceil-1.
\]

Then

\[
 W_4=\int_0^H F(t)\,dt,
 \qquad
 P_4^<=\sum_{t_n<H}S_2(N_n),
\]

with literal strict-ceiling arithmetic.  For every complete height cell,

\[
 L_n=\int_{n-1}^nF(t)\,dt-S_2(N_n).
\]

The global QCL assertion that all cell terms, including the possible terminal
truncation, are nonnegative is sufficient for \(\mathrm{WT}_4\), but is not
known to be necessary.

## Frozen route results

| Route | Concrete result | First unsupported implication | Disposition |
|---|---|---|---|
| `WT4-DIRECT-LAYER` | Exact inverse-layer/QCL identity above | Sign shallow-inner, interface, and terminal cells | promising |
| `WT4-POINTWISE-D` | Exact sawtooth representation for (D_A(a)); complete slabs on the increasing branch of (1/\sigma) are positive | Weighted QCL uses the different kernel \(\xi^2/\sigma\); no transfer is valid | active |
| `WT4-COMPONENT-U` | Round 47 component identity and allocation remain valid | Correlated component inequality remains unsigned | active |
| `WT4-BONUS-KERNEL` | Shell mixture gives deep-inner convexity; pure total-positivity/atomic-measure strengthening has a route counterexample | Uniform shallow-inner/interface sign | promoted bounded sublemma; pure TP branch falsified |
| `WT4-DISCRETE-MAJOR` | Exact row-cone reserve and fixed-(K) adverse-face reduction for the stronger \(\Theta\) route | Sign every adverse wall/active face | promising |
| `WT4-GENERATING` | Exact outer kernel comparison | No extension across the inner interface | promoted bounded sublemma |
| `WT4-ALT-SPECTRAL` | Continuous quarter-node strengthening proposed, then interval-falsified on an interface cell | Discrete QCL survives; continuous replacement is invalid | falsified route, redirect to discrete QCL |
| `WT4-ACTION-FLOW` | Action walls are upward jumps in the safer direction; compact (K)-slabs reduce to finitely many adverse faces | Tangential derivative has mixed signs and does not sign the faces | promising |
| `WT4-FALSIFICATION` | No literal, QCL, or \(\Theta\) negative found; exact continuous-route counterexample certified | Numerical positivity is not proof | continue |

## Certified bounded results

Two new claims passed distinct lead, clean-room, and adversarial roles.

1. **Full outer cell.**  If (n\le A(\mu)), then

   \[
   L_n>\frac{19N_n}{48}+\frac{27}{128}>0.
   \]

   The lead uses a past/future kernel comparison; the clean-room proof uses a
   convex quantile transport.

2. **Deep inner cell.**  If the cell is complete and
   (n-1\ge A(\mu/\sqrt2)), then (L_n>0).  The lead uses the shell-mixture
   curvature identity; the clean-room proof uses monotonicity of
   (2\arcsin u-u/\sqrt{1-u^2}).

Neither lemma covers the shallow-inner band

\[
 A(\mu)<t<A(\mu/\sqrt2),
\]

an interface-straddling cell, or the terminal truncated cell.

## Exact negative and diagnostic results

The continuous comparison

\[
 p(\xi(n-1/4))\le\int_{n-1}^{n}F(t)\,dt
\]

is false.  A directed interval replay at one exact rational interface cell
gives a margin below (-572.6942), while the literal discrete QCL margin at
the same point is above (956715.736).  The failure is therefore isolated to
the stronger continuous replacement.

Fixed-(K) and fixed-(\rho) wall reductions were exact.  The finite wall
sweeps that found no negative QCL, \(\Theta\), or literal target are diagnostic
only and supply no coverage certificate.

## First global gap

After removing the two certified regions, the first unsupported implication
is a uniform payment mechanism for:

1. complete shallow-inner cells;
2. the unique possible interface-straddling cell;
3. the terminal truncated cell; and
4. any compensation among those residual cells and the unused top interval.

Thus Round 48 materially localizes the aggregate, but does not prove or
falsify \(\mathrm{WT}_4\).
