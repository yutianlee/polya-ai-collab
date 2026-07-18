# Independent audit: manuscript integration of the completed \(f\geq2\) no-drop theorem

Date: 18 July 2026

Status: **FINAL PASS**.

This audit covers the current general-dimensional manuscript source, its
separate build, the inserted \(f\geq2\) no-drop theorem and evidence ledger,
the surrounding status claims, and preservation of the original \(d=3\)
paper.  No manuscript source or production PDF was modified by this
auditor.

## 1. Final pinned artifacts

| artifact | bytes | SHA-256 |
|---|---:|---|
| manuscript/spherical-shell-polya-general-d.tex | 212,546 | 650D3A356704BE7912BAA165F568704DEAA782731F90DE62F25E3B0EB364D6D0 |
| manuscript/build-general-d-no-drop-fge2/spherical-shell-polya-general-d.pdf | 877,932 | 1FB700D6E1E34F35B0F0C3217F688A8F77B31DE8AE1E6622D58D72F1D632995B |
| manuscript/build-general-d-no-drop-fge2/spherical-shell-polya-general-d.log | 23,937 | 96B6915E338A701C469E67627D00B2B238B9EBF67D95E9AE042C404E3A194053 |

During the audit, one local strictness typo in the first draft was found:
the proof had written \(s<38/n<1/10\) for \(n\geq380\).  At \(n=380\)
the second comparison is equality.  The source was corrected, before the
final hashes above were pinned, to

\[
 s<\frac{38}{n}\leq\frac1{10}.
\]

The proof conclusion was valid even before this repair because the first
comparison is strict.  The corrected source and rebuilt PDF display the
right chain and are the only versions certified by this report.

## 2. Theorem scope and mathematical boundary

The inserted theorem is titled

> Certified closure of the no-drop floors \(f\geq2\)

and assumes exactly

\[
 p=n\geq1,\qquad F_0=\cdots=F_n=f\geq2.
\]

It concludes

\[
 \mathcal S_n=D_A(q)+R_n>0,
\]

and then uses the previously proved exact wall-slack identity to obtain

\[
 D_A(r)=\mathcal S_n+\chi_q>0.
\]

The proof division is complete and has no missing boundary:

1. \(n=1\) is assigned to Corollary 7.31.
2. For \(f=2,3\), the analytic transfer covers \(s\leq1/10\).
   The finite directed-Arb module covers \(2\leq n\leq379\) and
   \(s\geq1/10\), with the equality face deliberately included in both
   modules.  The corrected estimate
   \(s<38/n\leq1/10\) sends every \(n\geq380\) candidate into the analytic
   sector.
3. For \(f\geq4\), the central and outer exhaustion lists have exact union
   \(595+60-45=610\) pairs.  Their three one-sided endpoint phases give
   \(610\cdot3=1830\) cases, covered by the eight-shard certificate.

The theorem therefore covers every no-drop floor \(f\geq2\), and only
those floors.  It does not absorb the distinct \(f=1,p=n\) row.

## 3. Ledger reconciliation

The manuscript ledger is

| floor | phase cases | processed boxes | positive leaves | maximum depth |
|---|---:|---:|---:|---:|
| \(f=2\) | 1,134 | 19,887,149 | 29,323 | 31 |
| \(f=3\) | 1,134 | 7,695,182 | 10,921 | 23 |
| \(f\geq4\) | 1,830 | 8,232,800 | 22,986 | 15 |
| total | 4,098 | 35,815,131 | 63,230 | 31 |

The row sums were independently recomputed:

\[
 1134+1134+1830=4098,
\]

\[
 19{,}887{,}149+7{,}695{,}182+8{,}232{,}800
 =35{,}815{,}131,
\]

and

\[
 29{,}323+10{,}921+22{,}986=63{,}230.
\]

The three diagnostic smallest positive endpoints also agree with the
audited low- and high-floor records:

\[
 1.7050400932319067\times10^{-6},\qquad
 2.4999770759192934\times10^{-4},\qquad
 2.144211613601797\times10^{-5}.
\]

The manuscript correctly says that these decimals are diagnostics only;
the proof decisions use rational or outward interval signs.

## 4. Reproducibility pins

Every source or audit hash printed in the theorem proof matches the
current file on disk:

| pinned artifact | current SHA-256 |
|---|---|
| scripts/general_d_no_drop_low_floor_final_verify.py | 4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F |
| scripts/general_d_no_drop_compact_verify.py | EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE |
| scripts/_aggregate_general_d_no_drop_high_floor_shards.py | 79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996 |
| human/outbox/general-d-round-05-no-drop-compact-final-independent-audit.md | 83ABBE4DB8228B06678CDE41FED4B02281C154A711ABC9D26FF204FCC47B5475 |
| human/outbox/general-d-round-08-no-drop-high-floor-final-note-independent-audit.md | 7DB8123BD3577E0CF9558F8BB10D8D5591821AF3DA0FFA234B35E550982CD747 |

The supporting proof notes are also present at the independently recorded
hashes:

| proof note | current SHA-256 |
|---|---|
| human/outbox/general-d-round-05-no-drop-compact.md | 44304F58E3B61FE1B75AEDC0D764800385AC3C0B905E60F1A3792D97DBCE9BE5 |
| human/outbox/general-d-round-08-no-drop-high-floor-final.md | 3E43416CFEDBD50B9B29DC57E4FC6A786BCAD9CD90E469C785A466262E8DAE63 |

The low-floor audit is FINAL PASS for the \(f=2,3\) module, and the
high-floor audit is FINAL PASS for the \(f\geq4\) module.  Their scopes are
combined in the manuscript only after the separate analytic \(n=1\) result
and the already proved exhaustion/transfer theorems are invoked.

## 5. Status language and first-floor caveat

The abstract now says that the no-drop certificates prove every floor
\(f\geq2\), that the zero floor is automatic, and that the first-floor
no-drop case \(f=1,p=n\) remains uncertified.  The statement-and-status
section repeats the same caveat.

The remaining-obligations section states explicitly:

\[
 F_0=\cdots=F_n=1,\qquad p=n
\]

is still to be proved and is not part of the ordinary first-floor
first-drop certificates, whose hypothesis is \(p<n\).

All closure claims for the previously completed ordinary first-floor
sector now carry the qualifier “first-drop.”  The finite and large-ray
subtheorems use \(s=n-p-1\geq0\), which itself forces \(p<n\), and the
summary statements explicitly say “ordinary first-floor first-drop
branch.”  No surviving sentence claims the entire first-floor branch,
including \(p=n\), has been proved.

The manuscript also continues to identify the residual high-floor
first-drop compact box

\[
 \frac1{3154914}<\rho<\frac{23}{25},\qquad
 \frac{21}{4}<K<1577457
\]

as uncertified.  Thus the new no-drop theorem is not used to overclaim the
full shifted-tail conjecture or the full general-dimensional Pólya theorem.

## 6. Independent build and PDF checks

The corrected source was independently compiled with the LaTeX compile
workflow into

tmp/pdfs/general-d-fge2-integration-audit-build/

using the detected MiKTeX latexmk/pdfLaTeX toolchain.  The independent
build succeeded with 82 pages and 877,932 PDF bytes.  Its hashes are

| independent artifact | SHA-256 |
|---|---|
| spherical-shell-polya-general-d.pdf | 8573E41B658FB8E54BA99C3D7124B5E630BE342034A59C60C4349C0BAE31325D |
| spherical-shell-polya-general-d.log | 2CDD20F94A92561DAD5119BE060FD3296DA55187A246D5FE2A6BCC22573C71B6 |

The independent PDF binary hash differs from the production build only
because the PDF creation and modification timestamps differ.  A page-wise
comparison found identical extracted text and identical PDF content
streams:

| comparison | common SHA-256 |
|---|---|
| extracted text | CBA8186078FA8E0D642F7010B6C9365372EB6CD40306B78D2649AA7503497F31 |
| concatenated page content streams | 02A12D1686FF65E2D40A30A569E98B9062B8D7C0321DC412EC989793CC7BB100 |

Both the production and independent TeX logs have zero instances of:

- LaTeX, package, class, or pdfTeX document warnings;
- overfull or underfull boxes;
- undefined or multiply defined references;
- LaTeX errors, emergency stops, or fatal errors;
- rerun-required cross-reference messages.

MiKTeX printed its external maintenance notice that user and administrator
updates are out of sync.  This occurs outside the TeX document log after a
successful build and does not alter the PDF; it is not a manuscript
diagnostic.

Full-PDF text scans found no literal qquad artifact, unresolved ?? marker,
undefined marker, placeholder, TODO, FIXME, overfull/underfull message, or
tool-token residue.  The corrected
\(s<38/n\leq1/10\) chain is present in the rendered PDF.

## 7. Visual inspection

Using Poppler, pages 1--3 and 78--82 of the corrected independent PDF were
rendered to PNG and inspected at high resolution.

- Pages 1--3 show a clean title, abstract continuation, statement/status
  section, and explicit \(f=1,p=n\) caveat.  No text is clipped or
  overlapped at the page transition.
- Page 79 introduces Theorem 7.35 with the correct \(f\geq2\) hypothesis
  and boxed positive scalar.
- Page 80 displays the corrected \(\leq1/10\) sign, the exact coordinate
  formulas, the full ledger, all hashes, and the transition to Section 8.
  The small reproducibility text remains legible and inside the margins.
- Page 81 states the \(f=1,p=n\) obligation and the residual high-floor
  first-drop box without overclaim.
- Page 82 closes the obligations and references cleanly.

There are no broken glyphs, black boxes, collisions, clipped equations,
illegible table entries, or malformed page numbers on the inspected pages.

## 8. Preservation of the original \(d=3\) paper

The original three-dimensional artifacts retain exactly the required
hashes:

| original artifact | SHA-256 |
|---|---|
| manuscript/spherical-shell-polya-proof.tex | E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4 |
| manuscript/spherical-shell-polya-proof.pdf | FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F |

The general-dimensional theorem is therefore integrated only in the
separate general-\(d\) manuscript and build, as required.

## 9. Final verdict

**FINAL PASS.**  At source SHA-256

650D3A356704BE7912BAA165F568704DEAA782731F90DE62F25E3B0EB364D6D0

the general-dimensional manuscript accurately and reproducibly proves the
no-drop theorem for every \(f\geq2\), keeps \(f=1,p=n\) and the residual
high-floor first-drop walls open, preserves all verifier/audit pins, builds
cleanly, renders cleanly, and leaves the original \(d=3\) paper unchanged.
