# Round 24 clean-room review: direct retained-remainder gap

Date: 17 July 2026

Reviewer role: independent clean-room reconstruction

## Frozen inputs

- main source:
  `15fd1c0d82e060028f52dcd24c2ba1e792858da139a7d2103e094eea34ab4690`
- structural source:
  `1bc70ef82d0461f5c807632fe4024f9c3eff57232755428ed90a390d42b69e49`
- angular source:
  `f920348f54b95c42d7e80f564e2d08d66fbec2fe372719bdf539195879c68f6b`
- scalar source:
  `811312fc8433bb89f339100f007694dd91de07ec20e4f4d691e36a1fca33fe07`
- final-closure source:
  `c2a370b52be56e735fb2813845cd29d4fb8cb335f8f16a2e87135edbb647fda3`
- supplement master:
  `16008399df3893c662f501994e1a50b5d8531f63641b6ae7b7afbc9403c289ee`

## Verdict

**PASS.**  The compressed implication is valid and preserves strict wall
ownership:

\[
 W-P\geq\mathcal H-\mathcal E_{\rm ang}
 >\mathcal H-\frac{(1-\rho^2)K^2}{6}+\frac N2.
\]

On the all-frequency middle domain, `N>=1`; with

\[
 M_c=\frac{(1-\rho^2)K^2}{6}-\frac12,
 \qquad \mathcal H-M_c>0,
\]

one obtains `W-P>H-M_c>0`, hence `N_D<=P<W`.

## Reconstruction

1. The structural Stieltjes identity is exact.  The decreasing-branch
   remainder dominates its smooth minorant and the oscillatory remainder is
   nonnegative, giving `W-P>=H-E_ang`.
2. For an active layer `x_n=n-1/4`, the shell slope cap gives
   
   \[
   R(t)\geq r_n+2(x_n-t),\qquad n-1\leq t\leq x_n.
   \]
   
   Integration yields
   
   \[
   r_n\leq\frac43\int_{n-1}^{x_n}R(t)\,dt-\frac34.
   \]
3. Strict angular counting gives
   `M(r_n)^2-r_n^2<r_n+1/4`, including a half-integer wall.
4. The left blocks are disjoint, so summation and
   `integral_0^T R=(1-rho^2)K^2/8` give the stated strict angular bound.

## Wall audit

- `x_n=T` is excluded consistently from `P`, `N`, and the layer cake.
- At `R(x_n)=m+1/2`, strict counting assigns `M=m`, so the pointwise angular
  inequality remains strict.
- The live angular proof does not Stieltjes-integrate the discontinuous
  angular staircase.  A simultaneous radial--angular wall therefore needs no
  separate common-jump product term.
- Both ratio faces and `K=k_11(rho)` remain included exactly as before.

## Deletion audit

The removed complete-angular-cell and Euler common-jump sections had no live
consumer.  The global angular proposition used only the one-layer block and
strict pointwise rounding.  Removing the unused exposition changes no premise
or conclusion.

First unsupported implication: **none**.
