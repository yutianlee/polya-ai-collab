# Integration audit: Round 8D in the general-dimensional manuscript

Date: 18 July 2026  
Status: **FINAL PASS**

Audited manuscript source:

- `manuscript/spherical-shell-polya-general-d.tex`  
  SHA-256 `DD677A3ACB45647572D5F19CA27222322592DE7F753429E2D8674C9923DACB60`.

Frozen Round 8D sources of truth:

- proof note SHA-256
  `C29F8ADF77E6EFE5B21BE0B39CD26D8D63B2881023EE72B5E8C0DB37AB81E30E`;
- verifier SHA-256
  `8E025183DC6F2AFCE4E51F404F5AC7830185FCA1B22B2DF0184D1204E4D91BF6`.

The manuscript source and the frozen Round 8D artifacts were not edited
during this audit.

## 1. Theorem and proof transcription

The new theorem
`thm:high-floor-round-eight-d-scalar` accurately transcribes the frozen
result:

\[
 f\geq2,\quad p<n,\quad \rho\geq\frac{93}{100}
 \quad\Longrightarrow\quad
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Its residual box, integer ranges, and chamber conditions agree exactly
with the frozen note:

\[
 \frac1{5\,443\,200}<\rho<\frac{93}{100},\qquad
 \frac{21}{4}<K<2\,721\,600,
\]

\[
 1\leq2r\leq5\,443\,199,quad
 2\leq n\leq2\,721\,599,quad
 1\leq p\leq n-1,
\]

\[
 2\leq f\leq907\,200,qquad
 0\leq Q\leq f-1,qquad Q\leq B\leq907\,200.
\]

The proof correctly treats the full closed band
\([93/100,477/500]\), with Round 8B owning the shared endpoint and all
larger ratios.  The active-width derivation, common prefix, strict
terminal partition, and all four \(\delta\geq1\) endpoint ledgers match
the frozen proof.  In particular, the manuscript retains the strict
active floor \(W>7/20\) and the exact ledger values

\[
 \frac{16676601}{10^8},\quad
 \frac{7706601}{10^8},\quad
 \frac{39712601}{10^8},\quad
 \frac{38276199}{10^8}.
\]

On \(0<\delta<1\), the endpoint bounds, series coefficients, integral,
and directed margins are transcribed correctly:

\[
 c<\frac{1199}{10000},\quad
 \theta^2<\frac{71}{500},\quad
 C_\rho>\frac{1389}{1000},
\]

\[
 \frac9{368},\qquad \frac9{1288},
\]

with 64 full rational ratio panels and 128 panel/endpoint tests.  The
reported retained-integral and level-distance lower bounds agree with the
frozen verifier:

\[
 0.2037148927\ldots,qquad 0.0162868443\ldots.
\]

The cap proof owns every phase: \(p<n\) gives \(q\geq3/2\), the
\(q=\mu\) cap is zero, and the open phase uses strict convexity followed
by the decreasing function \(G_{q+1}(q)\).  The endpoint comparison
\(G_{5/2}(3/2)<1/5\) and the resulting terminal polynomial

\[
 c\mathcal S>rac5{16}-\frac{27}{10}c+c^2
 \geq\frac{314601}{10^8}>0
\]

are correct.  The cutoff computation also matches the frozen proof:
\(\eta_\rho>1/180\),
\(a_\rho+2\eta_\rho C_*<84\), and
\(K_0(\rho)<84\cdot180^2=2\,721\,600\).

I found no transcription or proof-direction error.

## 2. Abstract and final status

The abstract reports the new ratio threshold and residual box exactly.
It explicitly calls the result a compact reduction rather than a proof of
the residual fixed-ratio walls.  It also states that only the residual
no-drop and high-floor compact walls remain uncertified.

The final `Remaining proof obligations` section identifies the Round 8D
box as the current sharpest high-floor reduction, preserves the same
integer ranges, and explicitly says that the interior fixed-ratio walls
are still uncertified.  It does not infer closure from finiteness and does
not claim the full shifted-tail theorem or the general-dimensional
spectral theorem is complete.

The historical summary is consistent: Round 8B reaches
\(\rho\geq477/500\), while Round 8D uses active width and the sharp cap to
reach \(\rho\geq93/100\).  I found no status overclaim or stale current
cutoff.

## 3. References and independent build

The new theorem label and every new equation label are unique.  A source
scan found 315 labels with zero duplicate groups and 357 `ref`/`eqref`
uses with zero missing targets.  The generated auxiliary file resolves
the theorem as Theorem 7.25.

Using the LaTeX compile workflow, I independently built the frozen source
with `latexmk`/pdfLaTeX into
`manuscript/build-general-d-round8d-integration-audit`.  The build returned
exit code zero and produced a 66-page PDF.  The LaTeX log contains no
undefined references, multiply defined or duplicate labels, overfull or
underfull boxes, package/LaTeX warnings, or fatal errors.

Build PDF SHA-256:

`17084C099613B54C55853FC985FF6921CF2E58F8290A005E4277EC86AA624F55`.

I found no reference, build, transcription, proof, or status defect.

**Final integration verdict: PASS.**
