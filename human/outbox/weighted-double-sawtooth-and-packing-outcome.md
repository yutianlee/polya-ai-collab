# Outcome of the weighted double-sawtooth and packing pass

Date: 17 July 2026

## Decision

The proposed double-sawtooth and shifted-packing ideas do not currently give
a new proof of the global sign.  They do give two exact reformulations and
identify the precise obstruction, but a proof based only on monotonicity,
single-peakedness, and the slope cap `-A' <= 1/2` is false.

The live theorem therefore remains the audited retained-remainder proof.  Its
presentation has nevertheless been simplified: the structural and one-layer
angular estimates are now handed off as the single direct inequality

\[
 W(\rho,K)-P(\rho,K)
 >\mathcal H(\rho,K)
  -\frac{(1-\rho^2)K^2}{6}+\frac N2,
 \qquad
 N=\#\{n\geq1:n-1/4<T\}.
\tag{1}
\]

The unused complete-angular-cell and common-jump development has been removed
from the live angular module.  Strict common walls are already covered by the
pointwise inequality

\[
 M(r)^2<(r+1/2)^2
\]

and the disjoint left-block estimate used to prove (1).

## Exact double-sawtooth identity

Let

\[
 e(r)=M(r)^2-r^2,
 \qquad q(r)=-A'(r),
 \qquad
 \sigma(t)=\#\{n\geq1:n-1/4<t\}-t.
\]

At a strict radial wall, `sigma(n-1/4)=-3/4`; away from the walls,
`-3/4<sigma<1/4`.  Angular Stieltjes summation gives the exact global formula

\[
 \boxed{
 P-W=
 \int_0^K e(r)q(r)\,dr
 +\sum_{m+1/2<K}(2m+1)
   \sigma\!\left(A(m+1/2)\right).}
\tag{2}
\]

Formula (2) includes simultaneous radial--angular walls.  It is a useful
research identity, but not a sign proof:

- the weighted integral can be positive on the decreasing side of `q`;
- the atomic term is positive whenever
  `A(m+1/2)` lies just to the right of a radial wall;
- at a common wall the same atom is instead strongly negative.

Thus neither the negative unweighted mean of a complete angular cell nor an
unsigned bounded-variation estimate can establish (2) with a negative sign.

## Exact packing result and its obstruction

For every counted point

\[
 (i+1/2,j+1/2,n-1/4),\qquad n\geq2,
\]

there is a disjoint graph-following unit cell inside

\[
 \mathcal B_A=\{(u,v,t)\in\mathbb R_+^3:
 t<A(\max\{u,v\})\}.
\]

Indeed, over `Q_ij=[i,i+1] x [j,j+1]`, put

\[
 \Delta_{ij}(u,v)
 =A(\max\{u,v\})
  -A(\max\{i+1/2,j+1/2\}),
\]

and take the vertical interval

\[
 n-\frac54+\Delta_{ij}(u,v)
 <t<
 n-\frac14+\Delta_{ij}(u,v).
\]

The slope cap gives `|Delta_ij|<=1/4`, so the bottom is positive for
`n>=2`; the top lies strictly under the graph, and the cells are disjoint.

For `n=1`, the same cell can cross `t=0`.  This is not merely an artifact of
the estimate.  Actual shell actions can have a first-layer angular ring whose
available ring volume is smaller than its lattice multiplicity, so volume
must be pooled across rings and with the terminal region.  The packing
argument therefore reaches exactly the same first-layer correction handled
by the retained-remainder proof.

## Falsification results

No counterexample was found to the exact shell proxy inequality `P<=W` or to
the stronger shifted-tail inequality described below.  This is diagnostic
evidence only.

Three tempting shortcuts were falsified:

1. A universal theorem for all decreasing actions with `0<=-A'<=1/2` and a
   single-peaked derivative is false.  Exact piecewise-linear examples have
   one active layer and `P>W`.
2. The lower interval `[0,3/4]` need not pay the first layer even for an exact
   shell action.  At `rho=1/100`, `K=581/50`, numerical diagnostics give
   `M(R(3/4))^2=64` but
   `integral_0^(3/4) R(t)^2 dt=63.514368...`.
3. Negative unweighted angular-cell means do not force a nonpositive weighted
   angular defect.  At the same shell point the continuous weighted defect
   and the sampled angular defect are both positive, although the full global
   reserve remains comfortably positive.

The numerical values in items 2--3 are falsification diagnostics, not theorem
premises.

## Sharpened next research target

The surviving uniform target should be stated in the older shifted-tail
form, specialized to the exact shell action.  Put

\[
 a_\ell=\left[A(\ell+1/2)+\frac14\right]_<,
 \qquad
 \mathcal T_r=a_r+2\sum_{\ell>r}a_\ell.
\]

The target is

\[
 \boxed{
 \mathcal T_r
 \leq2\int_{r+1/2}^{K}A_{\rho,K}(z)\,dz
 }
\tag{3}
\]

for every `0<rho<1`, `K>0`, and every half-integer start below `K`, with the
strict wall convention included.  The convex tails starting at or above the
inner interface are already proved.  The new content is one uniform
concave--convex splice estimate for starts below `rho K`.

If (3) is proved globally, the exact multiplicity-to-tail identity and the
step-primitive bound imply `P<=W` immediately.  It would replace the regional
finite-owner and retained-remainder closure after the phase reduction.  It
has survived broad grid, random, endpoint-biased, wall, seam, and
simultaneous-wall searches, but it is not yet proved and has no live theorem
edge.

## Files simplified in this pass

- `manuscript/analytic/compact-structural.tex` now ends at the direct
  retained-remainder bound and a short handoff.
- `manuscript/analytic/compact-angular-block.tex` now proves the angular bound
  directly from the one-layer block and states (1); the unused complete-cell
  and Euler common-jump sections are gone.
- `manuscript/spherical-shell-polya-proof.tex` uses (1) directly in the
  all-frequency middle theorem.

The theorem, constants, seams, strict convention, and face owners are
unchanged.
