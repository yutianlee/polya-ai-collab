# Round 24 low-interface shifted-tail target freeze

Date: 17 July 2026

## Authoritative open target

Use the existing obligation `SHELL-low-interface-shifted-tails` as the next
proof-changing research target.

Let

\[
 A(z)=G_K(z)-G_{\rho K}(z),
 \qquad \mu=\rho K,
 \qquad x_r=r+\frac12<\mu,
\]

and, for `j>=0`,

\[
 b_j=\left\lfloor A(x_r+j)+\frac14\right\rfloor,
\]

with zero extension of `A` after `K`.  Prove, for every `0<rho<1`, `K>0`,
and integer `r>=0` with `x_r<mu`,

\[
 \boxed{
 \Delta_r:=
 2\int_{x_r}^{K}A(z)\,dz
 -b_0-2\sum_{j\geq1}b_j
 \geq0.}
\tag{LT}
\]

Equivalently,

\[
 \sum_{j\geq0}b_j-\frac12b_0
 \leq\int_{x_r}^{K}A(z)\,dz.
\]

The term `b_0/2` is the exact first-sample endpoint correction.  Ordinary
floor is intentional at action walls.  The equality face `x_r=mu` belongs to
the already-proved high-interface convex-tail lemma, and zero extension owns
the terminal cell.

## Present coverage

- Starts `x_r>=mu`: proved for all parameters by the convex FLPS tail theorem.
- Starts `x_r<mu` with `K>=K_0(rho)`: proved by the fixed-ratio high-energy
  lemma.
- A restricted small-hole sector: proved by the reviewed low-interface split.
- The unrestricted all-parameter low-interface statement (LT): open.

The all-frequency regional Pólya theorems and retained-remainder closure prove
aggregate inequalities; they do not imply every individual `Delta_r>=0`.

## Falsification boundary

Broad grid, random, endpoint-biased, wall, seam, and simultaneous-wall scans
found no violation of (LT), but this is diagnostic evidence only.

Do not replace `A` by an arbitrary decreasing action with a single-peaked
derivative and slope at most `1/2`: exact piecewise-linear counterexamples
have `P>W`.  Do not try to pay the first radial layer only from `[0,3/4]`:
this local payment fails even for exact shell actions.  A proof of (LT) must
retain shell-specific curvature/no-shelf information, concave-head floor
area, no-drop plateaux, the endpoint half-weight, and the terminal convex
reserve.

## Replacement map if proved and reviewed

Together with the existing high-tail lemma and weighted scaffold, (LT) would
prove the global coarse proxy bound directly.  The following would then cease
to be live theorem premises after an explicit retirement audit:

- the low-interface fixed-high and small-hole partial lemmas;
- the thin-shell and small-hole regional owners;
- the finite staircases and 38-state high-event theorem;
- the combined and compact-middle closures;
- the retained-remainder, angular-block, and scalar-positivity modules; and
- the three-ratio uniformity assembly.

The spectral decomposition, phase enclosure, strict count, weighted
scaffold, dilation, and non-tiling proof would remain.  Nothing may be retired
until (LT) has a complete proof plus independent clean-room and adversarial
reconstruction.
