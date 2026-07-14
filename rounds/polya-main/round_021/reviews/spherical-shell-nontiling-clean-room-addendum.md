# Spherical-Shell Non-Tiling Clean-Room Typography Addendum

Date: 2026-07-15

## Authentication

The immutable clean-room report
`rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md`
has SHA-256
`6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6`.
It was not edited.

## Exact typography corrections

Two displayed spellings in Section 6 have one intended correction:

1. On line 232, in the phrase about the usual terminology, the name is
   `P` + `U+00F3` + `lya`.
2. On line 239, in the phrase about the Dirichlet spectral inequality, the
   name is likewise `P` + `U+00F3` + `lya`.

Thus both sites are to be read as `P&oacute;lya`. A rendering that instead
places code point `U+8D38` between `P` and `lya` is code-page mojibake and is
not the intended spelling.

I inspected the immutable report for additional encoding and typography
defects. Strict UTF-8 decoding succeeds. There are no C0 control bytes other
than tab, line feed, or carriage return; no DEL byte; no replacement
character `U+FFFD`; and no stored `U+8D38`, `U+00C3`, or `U+00C2` mojibake
marker. No additional correction is required.

## Corrected scope sentence

Under the usual P&oacute;lya terminology, this proves that every genuine
three-dimensional spherical shell is a non-tiling domain. This proves
geometry only: it does not prove the Dirichlet P&oacute;lya spectral
inequality and does not establish publication novelty or priority.

## Verdict preservation

The clean-room verdict remains **PASS**, with first unsupported implication
**none**. This addendum changes typography only. Every definition,
countability and local-finiteness argument, boundary-limit step,
finite-sphere-cover contradiction, duplicate-tile case, scaling step, and
scope qualification in the proof remains unchanged.
