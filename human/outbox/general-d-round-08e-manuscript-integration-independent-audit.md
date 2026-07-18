# Independent audit: Round 8E manuscript integration

Date: 18 July 2026  
Status: **FINAL PASS**

I independently audited the Round 8E integration in
manuscript/spherical-shell-polya-general-d.tex.  I did not edit the
manuscript, the frozen proof note or verifier, either original \(d=3\)
artifact, or a shared no-drop script.

The frozen inputs have the required SHA-256 hashes:

- proof note human/outbox/general-d-round-08e-refined-cap-terminal.md:
  38DE6AE72ACE3674096A9231A590ADCA1C2CE958BAFA777370AF65A3C2A9EB66;
- verifier scripts/general_d_high_floor_refined_cap_verify.py:
  3360878C89DB842FD8695C74C211A3562DBFC84C3E1B4D3CA291DC36BCED39C5;
- mathematical proof audit
  human/outbox/general-d-round-08e-refined-cap-terminal-independent-audit.md:
  949AF578860D785428F2003AEBCEC146B4DBB2E827F3FF2F9A37D7911C6F64C0.

The audited manuscript source has the expected SHA-256

4E84E2108BA01F2840182FF345495997A61C4D65BC5294E1E1DAEA5761D80A1B.

## 1. Theorem statement and scope

Theorem 7.26 states exactly the frozen Round 8E result:

\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{927}{1000}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Its residual continuous box is exactly

\[
 \frac1{4\,626\,882}<\rho<\frac{927}{1000},\qquad
 \frac{21}{4}<K<2\,313\,441,
\]

and the discrete bounds are transcribed without endpoint changes:

\[
 1\leq2r\leq4\,626\,881,
 \quad 2\leq n\leq2\,313\,440,
 \quad 1\leq p\leq n-1,
\]

\[
 2\leq f\leq771\,147,
 \qquad 0\leq Q\leq f-1,
 \qquad Q\leq B\leq771\,147.
\]

The exact phase conditions \(q\leq\mu<q+1\),
\(K-\mu>7\pi/4\), the strict floor equalities through \(j=p\), and
the strict first drop at \(p+1\) all agree with the proof note.  The
theorem explicitly says that it certifies the ratio interval and not
the compact walls in the residual box.  No closure is inferred from
finiteness.

## 2. Line-by-line proof comparison

Every Round 8E constant and inequality direction in the manuscript
agrees with the frozen proof ledger.

1. The \(p=0\) face is assigned to the completed one-interface theorem.
   A negative candidate therefore has \(p\geq1\), \(n\geq2\), and
   \(q\geq5/2\).  The equality phase \(q=\mu\) is separated before the
   strict-convexity argument.  The manuscript then has the exact strict
   cap
   \[
    2\int_q^\mu G_\mu<G_{7/2}(5/2)<\frac16.
   \]

2. The absent-level chord uses the exact polynomial
   \[
   \frac{142129}{10^6}-\frac{627}{500}a
   +\frac{2881}{1000}a^2-\frac{123}{500}a^3-a^4>0,
   \]
   the degree-48 Bernstein minimum
   \(7422203/77832000000\), and the sign-safe conclusion
   \(L(a)<377/1000\).  With
   \(\beta=123/1000-c\), both present- and absent-level faces give the
   same strict prefix
   \[
    cP>\beta\delta-\frac{cd}{2}.
   \]
   The use of \(M\geq\delta/c\) occurs only after the proof establishes
   \(\beta>0\), so its direction is correct.

3. The splice interval is exactly
   \(927/1000\leq\rho\leq93/100\), with Round 8D owning the upper
   continuation.  The endpoint data
   \[
    (\arccos\rho)^2<\frac{37}{250},\qquad
    c<\frac{49}{400}<\frac{123}{1000}
   \]
   are unchanged.  The active-width comparison uses
   \(\lambda_\rho>249/1000\), the exact positive square gap
   \(1991/9000000\), and gives the strict lower height
   \(W>1743/4000\).

4. The three exhaustive \(\delta\geq1\) strata retain the exact four
   directed margin values:
   \[
   \frac{90643}{480000},\quad
   \frac{2308663}{16000000},\quad
   \frac{63081}{160000},\quad
   \frac{303449}{800000}>0.
   \]
   (The last two values are the two endpoints of the \(B_0=0,Q=1\)
   stratum.)  The manuscript preserves the strict-count ownership,
   the monotonicity direction on the \(B_0=Q=0\) face, and concavity on
   the \(B_0=0,Q=1\) face.

5. On \(0<\delta<1\), the reductions are exactly to \(f=2\) and
   \(x\in\{1/7,5/3\}\).  The manuscript has
   \(u_0<740/2781<267/1000\), the retained-range bounds
   \(73/300\) and \(949/3000\), the series constants \(45/1816\) and
   \(45/6356\), and \(C_\rho>173/125\).  Its displayed integral matches
   the frozen formula term by term.  It records all 64 ratio panels,
   both endpoint values of \(x\), and the directed lower bounds
   \(0.2040442323\) and \(0.0085053826\).  The final small-
   \(\delta\) polynomial is
   \[
    c\mathcal S>\frac5{16}-\frac83c+c^2
    \geq\frac{403}{480000}>0.
   \]

6. The cutoff argument keeps
   \(1/169<\eta_\rho<1/9\),
   \(a_\rho<658170/8249\),
   \(a_\rho+2\eta_\rho C_*<29724887/371205<81\), and
   \[
    K_0(\rho)<81\cdot169^2=2\,313\,441.
   \]
   The ensuing strict real bounds and integer roundings reproduce the
   theorem statement exactly.

I also replayed the frozen verifier independently at 512-bit Arb
precision.  It returned exit code zero, pinned the expected Round 8D
dependency hash, checked all 128 panel-endpoint evaluations and all five
terminal ledgers, and ended with the explicit statement that residual
walls below \(927/1000\) are not certified.

## 3. Abstract, references, and remaining obligations

The abstract reports the new threshold \(\rho\geq927/1000\), the new
box \(1/4626882<\rho<927/1000\), \(21/4<K<2313441\), and immediately
qualifies it as a compact reduction rather than a proof of the residual
walls.  It still identifies both residual no-drop and high-floor compact
walls as uncertified.

The final status section calls Theorem 7.26 the current sharpest box,
repeats the same strict bounds, and again says that the compact analytic
walls require further certification.  The older Round 8D constants
remain only in the historical Round 8D theorem/proof and in the explicit
description of the progression of ratio thresholds; they are not
presented as the current residual box.  All new theorem, equation, and
cross-reference labels resolve, with no duplicate labels or stale
references.

## 4. Independent compile and visual audit

I compiled the unchanged source into the separate directory

manuscript/build-general-d-round8e-integration-audit/.

The build completed with exit code zero and produced a 70-page,
778,605-byte PDF with SHA-256

427C1BF6E05ED9766BA88814954FA2E335F33E8BDAB4467C4158A9C7635D19D9.

The final LaTeX log contains zero instances of undefined references,
multiply defined labels, LaTeX or package warnings, overfull or
underfull boxes, fatal errors, and emergency stops.  MiKTeX emitted a
distribution-maintenance notice that user and administrator updates are
out of sync; this is outside the document log and did not affect the
successful build.

I rendered and visually inspected pages 1--2, 57--62, and 69--70 at
150 dpi.  These cover the updated abstract, all of Theorem 7.26 and its
proof, both section transitions, the complete remaining-obligations
summary, and the final references.  There is no clipping, overlap,
overflow, broken equation, illegible glyph, damaged link text, or page-
number defect.

## 5. Original \(d=3\) preservation and verdict

The original \(d=3\) artifacts retain their established hashes:

- manuscript/spherical-shell-polya-proof.tex:
  E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4;
- manuscript/spherical-shell-polya-proof.pdf:
  FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F.

I found no transcription error, reversed inequality, endpoint mismatch,
missing phase, stale current bound, cross-reference defect, layout
defect, or overclaim.  The Round 8E manuscript integration therefore
**PASSES**.
