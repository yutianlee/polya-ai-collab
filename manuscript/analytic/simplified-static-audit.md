# Static audit of the simplified analytic manuscript

**Audit date:** 16 July 2026  
**Result:** **PASS.** No unresolved mathematical dependency, reference error,
artifact mismatch, or outstanding publication-cleanup finding remains in the
checked snapshot.

## Frozen snapshot checked

- Main source: `manuscript/spherical-shell-polya-proof.tex`
  - SHA-256: `9F3D86C3777189186F1937F13EB0FA663211D4CCE259A27BFE4B7D8E5D85F9BB`
- Supplement wrapper:
  `manuscript/spherical-shell-polya-analytic-supplement.tex`
  - SHA-256: `36C07A5B0828A20898C721AA92C8100A7E0104F3ABE3D7D1EFD2BF5181250F09`
- Final main PDF:
  `tmp/final-analytic-20260716/main/spherical-shell-polya-proof.pdf`
  - SHA-256: `9058FE198947E51BFC04511B60C3ACCD348EA3D0B845887C4A1C23B2DAB09559`
- Final support PDF:
  `tmp/final-analytic-20260716/support-v3/spherical-shell-polya-analytic-supplement.pdf`
  - SHA-256: `311B078B1BB08BF021E9D5B4721A0448DC3C4419BC457B85916551CF288848CC`

The final PDFs were readable by `pdftotext`; the extracted page boundaries
were 40 pages for the main paper and 62 pages for the support volume.

## Checks that passed

### 1. Labels, references, and citations

- The main source contains 153 labels and 143 internal references.
- Each of the ten included supplement sources has no duplicate label and no
  reference to a missing label when treated as the standalone exhibit that it
  is.
- The main paper's five citation keys (`DLMF`, `FLPSannuli`, `FLPSballs`,
  `FLPSphase`, and `Lorch1993`) all have matching bibliography entries, and
  there is no unused bibliography entry.
- Fresh converged builds of the main paper and assembled supplement produced
  no undefined-reference, undefined-citation, or multiply-defined-label
  warning.
- A few label names repeat *between* standalone exhibits (for example
  `eq:D20` and `eq:pi-bounds`). This is harmless because the wrapper uses
  `\includepdf`, not `\input`; the auxiliary namespaces never meet.

### 2. Retired frequency split and aggregate branch

- No live source in the main/supplement dependency chain contains a `K=200`,
  `K\leq200`, or `K\geq200` premise.
- The stale equality-owner language was repaired. The main paper now assigns
  `K=2/\omega_0` to the complementary branch at main lines 2559--2562, and the
  corresponding ledger proof explicitly names the complementary average-floor
  branch at `ledger-main-visible.tex` lines 477--495.
- Remaining occurrences of “former aggregate” are explicitly historical and
  non-premissory: supplement-wrapper lines 43--49 and main lines 3019--3025.
  The final-closure exhibit likewise says that the aggregate module is not
  used.

### 3. Exact residual and owner domains

The simplified owner graph is now internally aligned:

- Main `\mathcal D_{19}` has high component
  `\rho_c\leq\rho<39/50` at main lines 2333--2340.
- The optical theorem owns `39/50\leq\rho<1`, and the main assembly now states
  this separately before subtracting the lower and staircase owners at main
  lines 2868--2884.
- Packet F uses the same ratio cutoff. Its definitions of `D_{\rm high}` and
  `S_{\rm own}` are at lines 44--64; its exact subtraction is at lines
  73--113. It no longer introduces the historical `\rho<7/8` parent residual
  or subtracts an optical owner a second time.
- The resulting `D_{20}` in Packet F, the main paper, and Part X is the same
  open/closed set:
  `\rho_c\leq\rho<39/50` and
  `k_{11}(\rho)<K<U(\rho)`.
- The all-frequency retained-remainder theorem has the same closed domain in
  all three locations:
  `\rho_c\leq\rho\leq39/50` and
  `K\geq k_{11}(\rho)`.
  Thus the final inclusion `D_{20}\subset\mathcal R_{\rm rr}` has no missing
  boundary face.

### 4. Thin-shell and seam cleanup

- There is no surviving thin-shell theorem or thin-shell ratio owner in the
  main dependency graph. The `thin:` label prefix remains only as an internal
  name for the product/action tools now collected in Section 3; every such
  reference resolves.
- Seam rows still printed in Part IV, and the older upper-owner seam checks in
  Part V, are explicitly retained as independent ledger cross-checks. Main
  lines 3013--3017 state that the retired seam rows are not premises of the
  simplified owner graph.

### 5. Included artifacts

All ten files named by the wrapper exist. The repaired
`ledger-main-visible.pdf` and `ledger-packet-F.pdf` were rebuilt after their
sources (both compiled copies are timestamped 15:41:27). The four components
changed in the publication-cleanup delta were likewise rebuilt after their
sources: `ledger-packet-D.pdf` and Parts VII--IX are timestamped 15:46:48--49.
The final support PDF contains these rebuilt exhibits rather than preceding
stale copies.

## Delta re-audit after publication cleanups

### Standalone `pdflatex` portability: resolved

The following sources now load `lmodern` immediately after T1 font encoding:

- `ledger-packet-D.tex`, lines 3--8;
- `compact-structural.tex`, lines 3--7;
- `compact-angular-block.tex`, lines 3--7;
- `compact-scalar-positive.tex`, lines 3--7.

A fresh, isolated MiKTeX/pdfTeX build of each source completed with exit code
zero and no undefined-reference, multiply-defined-label, package, font, or
`pdfTeX` warning. A repeated static scan found no new missing or duplicate
label in any of the four exhibits.

### Supplement contents numbering: resolved

The wrapper now sets `\thesection` to uppercase Roman numerals and supplies a
wider section-number field before the ten `\includepdf` entries (wrapper lines
101--170). The generated `.toc` contains `\numberline{I}` through
`\numberline{X}` with no Roman numeral duplicated in the title.

Both the independent MiKTeX build and the final `support-v3` artifact render
Roman-only entries `I` through `X`. Automated text extraction found zero
Arabic-plus-Roman entries of the former `1 I.` form. The support volume remains
62 pages, and the converged wrapper build has no LaTeX, overfull, or underfull
warning.

## Conclusion

The simplified proof structure is statically coherent: the `K=200` split and
aggregate dependency are gone, the optical and retained-remainder theorem
domains agree across the main paper and support exhibits, all strict owner
faces have a named branch, and the final residual inclusion is consistent.
The two previous non-blocking publication findings were repaired and passed a
fresh delta build. No mathematical, cross-reference, portability, contents,
or artifact blocker remains in this audit snapshot.
