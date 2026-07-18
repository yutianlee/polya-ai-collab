# General dimension, Round 8B: manuscript integration audit

Date: 18 July 2026  
Status: **FINAL PASS for the Round 8B manuscript integration**

The independently audited Round 8B theorem was inserted only into the
separate general-dimensional source

`manuscript/spherical-shell-polya-general-d.tex`.

The original dimension-three manuscript and PDF were not edited.

## Integrated statement

The new theorem proves the high-floor first-drop scalar for

\[
 \rho\geq\frac{477}{500}
\]

and replaces the previous residual box by

\[
 \frac1{29\,931\,928}<\rho<\frac{477}{500},\qquad
 \frac{21}{4}<K<14\,965\,964.
\]

The manuscript explicitly states that this is a compact reduction, not a
certificate of the residual walls.

## Build and visual checks

The LaTeX project was rebuilt in

`manuscript/build-general-d-round8b/`.

The final PDF has 62 pages and 736,701 bytes.  The build log has zero
matches for undefined references, duplicate labels, overfull or underfull
boxes, and fatal errors.  Pages 1, 49--55, and 61--62 were rendered with
Poppler and visually inspected.  The revised abstract, theorem statement,
proof, transition to the no-drop section, and remaining-obligations section
have no clipped, overlapping, malformed, or placeholder text.

## Frozen hashes

```text
B8639FC24703FA9CFA606C6C0195DC6689B135F24FA267C31CCFB1209D2B24DA  manuscript/spherical-shell-polya-general-d.tex
CF3EBFB13B8735801ACD2196EE941AFEC2B9F4EF0B17FA6B2EF54B31752A062F  manuscript/build-general-d-round8b/spherical-shell-polya-general-d.pdf
BD97F156E2DF150ABAD501D20527A618A98CD3450D6B683BCF09BBA4F7C8F63D  scripts/general_d_high_floor_absent_terminal_verify.py
07797739D2EDE8747B73E217517DB22B3A8023CBA92919DF81D984AA2500FAF6  human/outbox/general-d-round-08b-high-floor-absent-terminal.md
15B04C76FD5211CB7FB68C8BB25C427E44ED1CF75DE1004DE965E33252A24674  human/outbox/general-d-round-08b-high-floor-absent-terminal-independent-audit.md
```

The unchanged original dimension-three hashes are

```text
E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4  manuscript/spherical-shell-polya-proof.tex
FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F  manuscript/spherical-shell-polya-proof.pdf
```

