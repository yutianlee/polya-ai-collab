# Spherical-shell Pólya proof — Revision 2 review bundle

This bundle contains the submission-facing proof for genuine
three-dimensional spherical shells.

## Files

- `main.tex` and `main.pdf`: the main theorem, optical closure, assembly,
  dilation, independent non-tiling appendix, and exact external-input boundary.
- `supplement.tex` and `supplement.pdf`: the complete ratio-sharp
  low/middle-ratio defect proof.
- `build.ps1`: a pinned `latexmk`/pdfLaTeX build with source-byte and final-log
  gates.
- `SHA256SUMS.txt`: hashes of the release files.

Both TeX files are mechanically flattened from the canonical repository
sources. They contain no local `\input`, `\include`, `\includepdf`, absolute
path, or precompiled-PDF dependency.

## Build

From PowerShell, with a TeX distribution providing `latexmk` and `pdflatex`:

```powershell
./build.ps1
```

The script builds into `build/`, checks the final logs for unresolved
references, citations, duplicate labels, rerun requests, or TeX errors, and
then publishes `main.pdf` and `supplement.pdf` in this directory.

## Mathematical scope

The proof is purely analytic. Numerical experiments and exact-arithmetic
scripts may be used as regression checks in the research repository, but no
computed truth value, floating-point estimate, interval certificate, or
finite parameter search is a premise of these documents.

The theorem is for spherical shells only. This bundle does not claim the
general Pólya conjecture, literature novelty, priority, peer-review acceptance,
or publication readiness.
