# Independent audit: Round 8F manuscript integration

Date: 18 July 2026  
Status: **FINAL PASS**

I independently audited the Round 8F integration in
manuscript/spherical-shell-polya-general-d.tex against the frozen Round 8F
proof note and its independent mathematical audit. I did not edit the
manuscript, the production Round 8F PDF, either reference proof artifact,
either original \(d=3\) artifact, or any shard/core script. The only
source artifact created by this audit is this report; all compilation and
rendering products are confined to the isolated audit build and temporary
render directories.

## 1. Frozen inputs

The required hashes agreed before the comparison and again after the
independent compile, text extraction, and visual inspection:

| artifact | SHA-256 before and after |
|---|---|
| manuscript/spherical-shell-polya-general-d.tex | 257CC50E00EF0A8B3D25A927DA7A2D3357CB82C7F78DCEA3CC690EC0F720A85D |
| manuscript/build-general-d-round8f/spherical-shell-polya-general-d.pdf | 2C02982455820752EAF594B84D5BEBF3E1FAED248302EA75892DBA338D98F3A1 |
| human/outbox/general-d-round-08f-signed-prefix-terminal.md | ABAFE9A9C0B57607CA0945313D0C0A7B1602D6067D84587F14C274898EF7D196 |
| human/outbox/general-d-round-08f-signed-prefix-terminal-independent-audit.md | 87382053EABDDE184F530064FF938BF6B33F4EFA2F12438F47AD542EDBFD268A |

The hash command was:

    Get-FileHash -Algorithm SHA256 -LiteralPath <artifact>

## 2. Theorem statement, ranges, and scope

Theorem 7.27, “Signed-prefix high-floor exclusion,” states exactly the
frozen Round 8F result:

\[
 f=F_0\geq2,\qquad p<n,\qquad
 \frac{1847}{2000}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Its residual continuous box is exactly

\[
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228,
\]

and the discrete bounds have no changed endpoint:

\[
 r\in\tfrac12\mathbb N,\qquad
 1\leq2r\leq3\,844\,455,
\]
\[
 2\leq n\leq1\,922\,227,\qquad
 1\leq p\leq n-1,
\]
\[
 2\leq f\leq640\,742,\qquad
 0\leq Q\leq f-1,\qquad Q\leq B\leq640\,742.
\]

The chamber conditions are also transcribed exactly:

\[
 \mu=\rho K,\qquad q=r+n\leq\mu<q+1,\qquad
 K-\mu>\frac{7\pi}{4},
\]
\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \quad(0\leq j\leq p),\qquad
 A(r+p+1)<f-\frac14.
\]

The theorem immediately says that it certifies the displayed ratio
interval and not the compact walls left by the residual box. No closure
is inferred from the finiteness of the displayed ranges.

## 3. Line-by-line proof comparison

Every Round 8F constant, strictness choice, and inequality direction in
the integrated proof agrees with the frozen proof note and the independent
mathematical audit.

1. The \(p=0\) face is assigned to the completed one-interface theorem.
   Therefore a negative candidate has \(p\geq1\), \(n\geq2\), and
   \(q\geq5/2\). The inherited terminal cap is the strict wall-safe bound
   \[
    2\int_q^\mu G_\mu(z)\,dz<\frac16.
   \]

2. For \(\delta\geq1\), the absent-level and present-level faces have the
   common pre-substitution estimate
   \[
    P>\left(\frac d2-\frac{377}{1000}\right)M-\frac d2
      =\beta M-\frac d2,
    \qquad \beta=\frac{123}{1000}-c.
   \]
   The present-level coefficient is correctly written
   \((1/8-c)\), which exceeds \(\beta\) by \(1/500\).

3. The new splice band is exactly
   \(1847/2000\leq\rho\leq927/1000\). Its directed endpoint bounds are
   \[
    (\arccos\rho)^2<\frac{311}{2000}<\frac4{25},
    \qquad c<\frac{627}{5000}.
   \]
   With \(\epsilon\geq73/1000\), the exact gap
   \[
    \frac89\frac{73}{1000}-\left(\frac14\right)^2
    =\frac{43}{18000}>0
   \]
   gives \(\lambda_\rho>1/4\) and \(W>7/16\). The radial ratio is
   \[
    \frac{c\mu}{W}
    <\frac{(2/5)(927/1000)}{(1/4)(73/1000)}
    =\frac{7416}{365}<21.
   \]

4. Both sign substitutions have the correct direction. When
   \(\beta\geq0\), the proof uses \(M\geq\delta/c\) and obtains
   \[
    cP>\beta\delta-\frac{cd}{2}.
   \]
   When \(\beta<0\), it uses \(M\leq\mu\); multiplication by the negative
   coefficient reverses the comparison, and \(c\mu/W<21\) yields
   \[
    cP>21\beta W-\frac{cd}{2}.
   \]

5. The three terminal strata \(B_0\geq1\), \(B_0=Q=0\), and
   \(B_0=0,Q=1\) are exhaustive. On the \(\beta\geq0\) side, the four
   exact lower ledgers are
   \[
    \frac{187129}{1000000},\qquad
    \frac{580141}{4000000},\qquad
    \frac{393129}{1000000},\qquad
    \frac{189}{500}.
   \]
   The manuscript preserves the increasing \(W\)-direction on the
   \(B_0=Q=0\) face and the two concavity endpoints on the
   \(B_0=0,Q=1\) face.

6. On the \(\beta<0\) side, strict bracketing gives
   \(W\leq B_0+3/4\). Because \(21\beta<0\), this is correctly used as a
   lower bound. The coefficient and derivative checks remain
   \[
    \frac12-c+21\beta\geq\frac{1621}{5000}>0,
   \]
   \[
    2\frac7{16}+21\left(-\frac3{1250}\right)
    =\frac{4123}{5000}>0.
   \]
   Evaluation at \(c=627/5000\) gives the exact four positive ledgers
   \[
    \frac{2328129}{25000000},\qquad
    \frac{12238141}{100000000},\qquad
    \frac{8808129}{25000000},\qquad
    \frac{2143251}{6250000}.
   \]
   Thus all eight directed terminal endpoints match the frozen ledger.

7. For \(0<\delta<1\), the proof keeps
   \[
    y=f-W=\delta+\frac14,\qquad L=\frac{149}{50},
    \qquad T<\frac{Ly}{c}.
   \]
   The reduction to \(f=2\) and
   \(x\in\{1/7,5/3\}\), together with the retained-range calculations,
   has exactly
   \[
    u_0<\frac{46339}{166230}<\frac{279}{1000}<1,
   \]
   \[
    \kappa_\rho>\frac7{10},\qquad
    \frac{u_0}{1-\rho}>\frac{1043}{500}x,
   \]
   with exact quotient gap
   \(25224124159/1464079822630\).

8. The arccos-series data are unchanged:
   \[
    V\leq\frac{1043}{300},\qquad
    z\leq\frac{53193}{200000},
   \]
   \[
    1+\frac z{12}+\frac{3z^2}{160}
    \leq S(z)\leq
    1+\frac z{12}+\frac{3750z^2}{146807},
   \]
   with integrated upper coefficient \(7500/1027649\) and
   \(C_\rho>689/500\). The six-term displayed retained integral agrees
   term for term. The proof records all 64 rational ratio panels, both
   endpoint values of \(x\), and the directed lower bounds
   \(0.2113764065\) and \(0.0357944486\).

9. The small-\(\delta\) endpoint direction is correct because
   \((3-L)/4-c<0\) and \(\delta<1\). Combining the prefix with the
   terminal reserve gives the exact certificate
   \[
    c\mathcal S>
    \frac{51}{160}-\frac83c+c^2
    \geq\frac{1879}{25000000}>0.
   \]

10. The residual cutoff retains
    \[
     \frac1{158}<\eta_\rho<\frac19,\qquad
     a_\rho<\frac{1311370}{17289},
    \]
    \[
     a_\rho+2\eta_\rho C_*
     <\frac{2193941}{28815}<77,
    \]
    and
    \[
     K_0(\rho)<77\cdot158^2=1\,922\,228.
    \]
    The strict real bounds and integer roundings then reproduce every
    theorem endpoint exactly.

The integrated proof identifies
scripts/general_d_high_floor_signed_prefix_verify.py, states that it pins
the Round 8E verifier, and records all 128 panel-endpoint evaluations at
384, 512, 768, and 1024 bits, consistently with the frozen mathematical
audit.

## 4. Abstract, final status, labels, and references

The abstract reports the new threshold \(\rho\geq1847/2000\), the current
residual box

\[
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228,
\]

and immediately calls it a compact reduction rather than a proof of the
residual walls. It still says that the residual no-drop and high-floor
compact walls are uncertified.

The final status section calls Theorem 7.27 the current sharpest
high-floor box, repeats the same strict bounds, and again says that the
fixed-ratio compact analytic walls require further certification. The
Round 8E threshold \(927/1000\) appears only in the historical progression
and as the upper endpoint of the Round 8F splice band; it is not presented
as the current residual threshold.

An independent static scan found:

| item | count |
|---|---:|
| labels | 361 |
| unique labels | 361 |
| reference commands | 402 |
| unique reference targets | 241 |
| duplicate labels | 0 |
| undefined static reference targets | 0 |

All Round 8F theorem and equation labels are unique.

## 5. Independent compilation and final log

I compiled the unchanged source into
manuscript/build-general-d-round8f-integration-audit. The LaTeX compile
skill helper was run from
C:\Users\Lenovo\.codex\plugins\cache\openai-bundled\latex\0.2.4 with the
exact successful command

    $env:PYTHONUTF8='1'; python scripts/compile_latex.py 'D:\BaiduSyncdisk\Codex\Polya conjecture\manuscript\spherical-shell-polya-general-d.tex' --compiler texlive --output-directory 'D:\BaiduSyncdisk\Codex\Polya conjecture\manuscript\build-general-d-round8f-integration-audit' --json

The UTF-8 environment setting was needed only because the first helper
probe, before TeX was invoked, tried to decode a MiKTeX version stream
using the Windows GBK locale. With UTF-8 enabled, the helper selected
the existing MiKTeX latexmk tool and ran

    latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -synctex=1

with the isolated output directory. It exited zero and produced:

| artifact | bytes | SHA-256 |
|---|---:|---|
| audit PDF | 803,930 | F33C05068E9CAC5BA19324E79DA2935F90AD63973293CA26226047A1F2180250 |
| final LaTeX log | 23,902 | A0867F568C52ABD1EFCB7A14AC7D6B843C2B0BEADF9C3049D21A9ABC5145A28F |

Direct pdfinfo inspection reports 74 pages, letter size, no encryption,
and PDF version 1.5. The exact command used the bundled Poppler binary:

    & 'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe' 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.pdf'

The final document log was scanned independently with the following
result:

| log condition | count |
|---|---:|
| undefined references | 0 |
| duplicate or multiply defined labels/destinations | 0 |
| overfull boxes | 0 |
| underfull boxes | 0 |
| LaTeX warnings | 0 |
| package warnings | 0 |
| LaTeX, fatal, emergency-stop, or undefined-control-sequence errors | 0 |

MiKTeX printed its distribution-maintenance notice that user and
administrator updates are out of sync to the outer process stream. It
does not occur in the document log and did not affect the successful
build.

## 6. Extracted text and visual inspection

The audit PDF was text-extracted with

    pdftotext -layout 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.pdf' 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.txt'

The 283,597-byte extracted text has SHA-256
329C0DB9E0DAC383DC8DD466C4501CE90AF0E538E6E5CB090AD542BACEAF6A6F.
Case-insensitive scans give:

| extracted literal | count |
|---|---:|
| qquad | 0 |
| ?? | 0 |
| undefined | 0 |

Using the bundled Poppler pdftoppm binary, I rendered at 144 dpi with
the exact commands:

    & 'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe' -f 1 -l 1 -png -r 144 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.pdf' 'tmp/pdfs/round8f-integration-audit/page1'
    & 'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe' -f 61 -l 66 -png -r 144 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.pdf' 'tmp/pdfs/round8f-integration-audit/page61to66'
    & 'C:\Users\Lenovo\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe' -f 74 -l 74 -png -r 144 'manuscript/build-general-d-round8f-integration-audit/spherical-shell-polya-general-d.pdf' 'tmp/pdfs/round8f-integration-audit/page74'

I visually inspected pages 1, 61, 62, 63, 64, 65, 66, and 74. These
cover the updated abstract; the transition from the historical Round 8E
theorem; the complete Round 8F theorem, proof, ledgers, and cutoff; the
transition to the no-drop subsection; and the final remaining-obligations
summary. There is no clipping, overlap, overflow, broken equation,
illegible glyph, malformed link, damaged theorem box, or page-number
defect.

## 7. Original \(d=3\) preservation

The original \(d=3\) artifacts remain unchanged:

| artifact | SHA-256 |
|---|---|
| manuscript/spherical-shell-polya-proof.tex | E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4 |
| manuscript/spherical-shell-polya-proof.pdf | FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F |

## 8. Residual obligation and verdict

This integration proves only the signed-prefix high-floor exclusion on

\[
 \frac{1847}{2000}\leq\rho<1.
\]

It does **not** certify any fixed-ratio compact wall in

\[
 \boxed{
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228.}
\]

Those residual walls remain a separate obligation. I found no
transcription error, reversed inequality, omitted terminal stratum,
endpoint mismatch, stale current bound, duplicate or unresolved
reference, layout defect, modification of a frozen artifact, or claim of
closure from finiteness. The Round 8F manuscript integration therefore
**PASSES**.
