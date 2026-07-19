# General dimension, Round 4d: manuscript release audit

Date: 18 July 2026

## Verdict

**PASS as a progress manuscript.**  The separate general-dimensional source
and PDF compile cleanly, render cleanly, and state their conditional status
accurately.  They do not claim that the shifted-tail conjecture or the
general-dimensional Pólya theorem has already been proved.

## Audited artifacts

- source: `manuscript/spherical-shell-polya-general-d.tex`;
- build: `manuscript/build-general-d-round4c/spherical-shell-polya-general-d.pdf`;
- promoted copy: `output/pdf/spherical-shell-polya-general-d.pdf`.

The audited source SHA-256 is

```text
B2A98E96C671CA5EB859AB96AECB44ADDC033A4CF526226FC1C20879FD7BAFDB
```

The build and promoted PDF have the matching SHA-256

```text
FEFBB3F78663D8700DC7E5EF2E0B92D9D5B588578EA25CC28D8C952702C42B2F
```

## Checks

1. The source was built twice with the cached bundled Tectonic runtime.
2. The PDF has 30 pages.  Independent `pypdf` extraction found no undefined
   references, replacement characters, or empty pages.
3. Source scanning found no forbidden ASCII control characters.
4. Pages 20--30 were independently rendered.  The fractional-top reserve,
   critical-ray argument, quantitative transfer, finite-exhaustion theorem,
   and final obligation list show no clipping, overlap, or malformed formula.
5. The quantitative theorem records the independently audited implication
   
   \[
   f\in\{2,3\},\quad n\ge72\,000
   \quad\Longrightarrow\quad
   \sqrt{1-\rho}\,\bigl(D_A(q)+R_n\bigr)>\frac15.
   \]
6. The abstract and final section explicitly retain the unresolved finite
   no-drop walls and the unresolved first-drop branch.
7. The original three-dimensional source
   `manuscript/spherical-shell-polya-proof.tex` was not used as the target of
   these edits; its timestamp predates the Round 4d work.

The release is therefore suitable as the current rigorous progress draft,
not as a completed proof manuscript.
