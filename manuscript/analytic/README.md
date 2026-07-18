# Purely analytic support volume

## Purpose

This directory contains the detailed low- and middle-ratio argument supporting
the Dirichlet Pólya inequality for three-dimensional spherical shells. The
proof is analytic: programs, numerical experiments, floating-point values,
and interval certificates are optional regression tools and are not premises.

## Live sources

| Role | Source |
|---|---|
| Standalone support module | `ratio-sharp-global-closure.tex` |
| Complete proof body | `ratio-sharp-global-closure-body.tex` |
| Condensed main-paper version | `ratio-sharp-global-closure-summary.tex` |
| Reproducible build | `build.ps1` |
| Release inventory and hashes | `MANIFEST.md` |

The analytic supplement inputs the complete body directly. The main paper
inputs only the summary. The two entry points are separate TeX compilations,
so their shared theorem-label name causes no collision.

## Live proof architecture

The support body proves the exact defect identity
`W - P = D_rad - E_ang` and closes it through four components:

1. ratio-sharp angular blocks using the shell slope cap;
2. a tangent envelope for the retained radial remainder;
3. a universal ball quarter-layer with an explicit turning estimate; and
4. exact scalar convexity from rational inequalities, including a direct
   proof of `333/106 < pi < 22/7`.

The main paper supplies the separated spectrum and phase bridge, the no-mode
region, the complementary optical theorem, assembly, dilation, and the
independent non-tiling appendix.

## Build and verification boundary

Run `./build.ps1` from PowerShell, optionally passing an installed `tectonic`
or `latexmk` executable through `-Compiler`. It builds the standalone module,
the analytic supplement, and the main paper from source. A release also
requires checking the LaTeX logs for unresolved references and visually
inspecting rendered pages; a successful compiler exit alone is not enough.

The PDFs in `compiled/`, `manuscript/`, and `output/pdf/` are generated
artifacts. Rebuild and refresh the hashes in `MANIFEST.md` whenever a live
source changes.

## Historical material

The other `ledger-*`, `compact-*`, and earlier closure modules in this
directory are retained for audit history and regression comparison. They are
not inputs to either live manuscript and do not belong to the theorem's
dependency chain.

## Claim discipline

The result concerns genuine three-dimensional spherical shells. These files
do not establish the general Pólya conjecture and do not by themselves
establish novelty, priority, or publication readiness.
