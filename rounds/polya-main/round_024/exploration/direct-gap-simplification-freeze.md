# Round 24 direct-gap simplification freeze

Date: 17 July 2026

## Scope

This is a source-level compression of the already-proved all-frequency
retained-remainder closure.  It changes no theorem, domain, constant, seam,
strict convention, or equality-face owner.

For

\[
 N=\#\{n\geq1:n-1/4<T\},
 \qquad T=\frac{(1-\rho)K}{\pi},
\]

the live handoff is

\[
 \boxed{
 W-P>
 \mathcal H(\rho,K)
 -\frac{(1-\rho^2)K^2}{6}+\frac N2.}
\tag{DG}
\]

It follows from the two reviewed estimates

\[
 W-P\geq\mathcal H-\mathcal E_{\rm ang},
 \qquad
 \mathcal E_{\rm ang}
 <\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

The first inequality retains the decreasing-branch radial remainder and the
nonnegative oscillatory remainder.  The second uses only the disjoint left
blocks `[n-1,n-1/4]`, the slope cap `-A'<=1/2`, and the strict pointwise
rounding `M(r)^2<(r+1/2)^2`.

## Deletion audit boundary

The deleted complete-angular-cell estimates and Euler common-jump formula
were not cited by the proof of the global angular bound.  The live proof never
Stieltjes-integrates the discontinuous angular sawtooth.  At a common wall
`R(n-1/4)=m+1/2`, strict counting gives `M=m`, so the pointwise rounding
inequality remains strict without an additional jump term.

## Frozen current source hashes

- `manuscript/spherical-shell-polya-proof.tex`:
  `15fd1c0d82e060028f52dcd24c2ba1e792858da139a7d2103e094eea34ab4690`
- `manuscript/spherical-shell-polya-analytic-supplement.tex`:
  `16008399df3893c662f501994e1a50b5d8531f63641b6ae7b7afbc9403c289ee`
- `manuscript/analytic/compact-structural.tex`:
  `1bc70ef82d0461f5c807632fe4024f9c3eff57232755428ed90a390d42b69e49`
- `manuscript/analytic/compact-angular-block.tex`:
  `f920348f54b95c42d7e80f564e2d08d66fbec2fe372719bdf539195879c68f6b`
- `manuscript/analytic/compact-scalar-positive.tex`:
  `811312fc8433bb89f339100f007694dd91de07ec20e4f4d691e36a1fca33fe07`
- `manuscript/analytic/final-analytic-closure.tex`:
  `c2a370b52be56e735fb2813845cd29d4fb8cb335f8f16a2e87135edbb647fda3`

## Build result

The isolated structural module has 6 pages, the angular module 5 pages, the
main paper 44 pages under the bundled Tectonic build, and the support volume
69 pages.  The former release support volume had 70 pages.  All four builds
completed without undefined or multiply-defined references.  The release
PDFs in `output/pdf/` were synchronized after the rebuild.

## Logical status

`SHELL-analytic-retained-remainder-closure` remains `proved_internal` and is
the live antecedent of `SHELL-rho-compact`.  This freeze is an equivalent
presentation of that node, not a new theorem promotion.
