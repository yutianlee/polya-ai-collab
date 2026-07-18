# Round 24 adversarial review: simplified direct-gap release

Date: 17 July 2026

Reviewer role: independent dependency, wall, build, and stale-artifact audit

## Verdict

**PASS after repair.**  No mathematical premise was removed.  The initially
stale release PDFs, manifest hashes, main-paper pointer to `H`, and Part X
three-step handoff were identified and corrected before this freeze.

## Adversarial checks

### Inequality directions and strictness

The structural step is non-strict,

\[
 W-P\geq H-E_{\rm ang},
\]

and the angular step is strict,

\[
 E_{\rm ang}<\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

Their composition is therefore the required strict direct gap.  No strictness
is inferred from the discarded nonnegative remainder.

### Deleted material

Searches of the live TeX sources find no consumer of the deleted labels for
weighted complete cells or the common-jump Euler formula.  The surviving
proof handles common walls through the strict value of `M` before summing
continuous left blocks.

### Scope

The base-domain calculation still gives `(1-rho)k_11(rho)/pi>1`, hence
`N>=1`.  Scalar positivity remains upward-closed for every finite
`K>=k_11(rho)`.  Direct containment of `D20` and every inherited face are
unchanged.

### Build and release

Clean isolated builds passed for the structural module, angular module, main
paper, and supplement, with no undefined or multiply-defined references.  The
support volume is 69 pages.  The two README-linked PDFs in `output/pdf/` are
byte-identical to the rebuilt manuscript PDFs.

The current release hashes are:

- main PDF:
  `5bbf9b639dfaddee96ac5b29b0bd5bfade574a1e167cfca70d6897188a4d210f`;
- supplement PDF:
  `3c7560592875bfe97444cc6f33577f4ee5382e6700e8918116d5ac3e37269d31`;
- structural PDF:
  `4469cecf2b30202e2c69e07b5f5c7976903210be1ec74c81f92e62c3d6c5f04d`;
- angular PDF:
  `cde9a33629522fa61c56cbfe3116eff90bc3fe97b3072c1563c4d5b5fa746081`;
- final-closure PDF:
  `df7a2ad062e32a206dc9b62480eadd801339d9eb1643106b38534d91667b7f45`.

### Research-target separation

The generic double-sawtooth/packing shortcut is not imported into the proof.
It is diagnostic only.  The exact shell-action low-interface shifted-tail
inequality remains open and has no edge into the completed theorem.

First unsupported implication: **none in the simplified live theorem path**.
