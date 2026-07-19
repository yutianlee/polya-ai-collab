# General dimension, Round 8G manuscript integration: independent audit - FINAL PASS

Date: 18 July 2026

Status: **FINAL PASS**.

## 1. Scope and pinned inputs

This audit covers the frozen Round 8G integration in
`manuscript/spherical-shell-polya-general-d.tex`, especially Theorem
`thm:high-floor-round-eight-g-scalar`, its proof, the abstract, the
Statement and status section, and the Remaining proof obligations section.
No manuscript, proof note, verifier, canonical no-drop source, canonical
no-drop log, or original dimension-three artifact was edited.

The frozen production inputs match the supplied pins:

| artifact | bytes | SHA-256 |
|---|---:|---|
| general-d manuscript source | 208,615 | `A525FA9FC2CB4DDB028369AC88701297A273525C11EE4102DB80D5F3A2D12126` |
| production Round 8G PDF | 838,362 | `AD56B0537542E5704B3A8041BEB93E3D4876F123CA9A41517170D635D9DB6595` |
| production Round 8G log | 23,846 | `80D59877E50DFA8533A6479EF8BA99A88274ECD36B45A6E304B3B12D2206A12F` |
| corrected Round 8G proof note | 15,781 | `C45D339383FD4E6921C3C60D058E14628846DF57E7F7808D62B373AB2476DE90` |
| Round 8G proof audit | 12,421 | `203BC49B2F4E61B932D3CA6D2483D295729FCBDE830A813D8EC9DD3AB2AD38A7` |

## 2. Theorem and proof comparison

I compared manuscript lines 5386-5904 line by line with the corrected proof
note and its independent audit. The integration preserves the claim,
hypotheses, strictness, and every proof direction.

### Theorem scope and discrete reduction

Manuscript lines 5386-5434 correctly state the exclusion for the high-floor
first-drop branch with

\[
 f=F_0\geq2,\qquad p<n,\qquad \frac{23}{25}\leq\rho<1,
\]

and the strict conclusion

\[
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

The remaining continuous box is exactly

\[
 \frac1{3154914}<\rho<\frac{23}{25},\qquad
 \frac{21}{4}<K<1577457,
\]

and the discrete rounding is exactly

\[
 1\leq2r\leq3154913,\quad
 2\leq n\leq1577456,\quad
 1\leq p\leq n-1,
\]

\[
 2\leq f\leq525819,\qquad
 0\leq Q\leq f-1,\qquad Q\leq B\leq525819.
\]

The chamber conditions \(q=r+n\leq\mu<q+1\),
\(K-\mu>7\pi/4\), the strict shelf floors, and the first-drop inequality
are all retained. The theorem explicitly says that no residual analytic
wall is certified.

### Inherited cap and exact negative prefix

Lines 5437-5545 correctly reduce to

\[
 \frac{23}{25}\leq\rho\leq\frac{1847}{2000},
\]

retain \(p\geq1\), \(n\geq2\), \(q\geq5/2\), and use the strict terminal
cap \(2\int_q^\mu G_\mu< G_{7/2}(5/2)<1/6\). The present- and absent-level
faces give the same strict prefix

\[
 P>\beta M-\frac d2,
 \qquad \beta=\frac{123}{1000}-c,
\]

with the stated coefficient gap \(1/500\).

The endpoint walls

\[
 \theta^2<\frac{163}{1000},\qquad
 c<\frac{641}{5000},\qquad \beta<0
\]

are inserted in the correct directions. Because \(M\leq\mu\) and
\(\beta<0\), the manuscript correctly reverses that comparison and obtains

\[
 cP>\beta c\mu-\frac{cd}{2}
   =\gamma(\theta)W-\frac{cd}{2}.
\]

The derivative formulas for \(R\) and \(\gamma\) match the proof note.
The count of 64 complete rational panels, the strict wall
\(\gamma'<-49/10\), the enclosure union, the endpoint choice
\(\rho=23/25\), and the final range

\[
 -\frac9{100}<\gamma<0
\]

are all unchanged.

### Active width and terminal strata

Lines 5547-5659 preserve

\[
 \lambda'(\theta)>0,\qquad \lambda>\frac{229}{875},
 \qquad W>\frac{229}{500}.
\]

The three cases \(B_0\geq1\), \(B_0=Q=0\), and \(B_0=0,Q=1\) are
correctly declared exhaustive from \(Q\leq B_0+1\). In the first case the
substitution \(W\leq B_0+3/4\) is in the lower-bound direction because
\(\gamma<0\). In the second case the derivative in \(W\) is strictly
positive. In the third case the reduced quadratic is concave, so both
endpoints are required. The exact proof floors are all copied correctly:

\[
 \frac{1409}{5000},\quad
 \frac{1280143}{75000000},\quad
 \frac{413}{500},\quad
 \frac{3021981}{25000000},
\]

\[
 \frac{7978381}{25000000},\qquad
 \frac{157119}{500000}.
\]

The independent correlated replay remains explicitly separate from the
exact floors. Its 256-panel count and all six printed diagnostic minima
match the proof note.

### Small level distance and retained integral

Lines 5661-5812 preserve the inherited concavity reduction to
\(x\in\{1/7,5/3\}\), and correctly derive

\[
 u_0<\frac{4727}{16560}<\frac{143}{500}.
\]

The quotient-rule numerator for \(\kappa\), its 64-panel positivity check,
the endpoint direction, and

\[
 \kappa_\rho>\frac{18}{25}
\]

are unchanged. So are the retained scale \((261/125)x\), the coefficient
wall \(C_\rho>137/100\), and both series domains

\[
 (1-\rho)V\leq\frac{174}{625},\qquad
 (1-\rho)(1+V)\leq\frac{224}{625}<1.
\]

The decreasing-coefficient argument gives the same exact upper coefficient

\[
 \frac{21117}{1010240}<\frac{21}{1000}
\]

and integrated ceiling \(3/500\). Every coefficient and sign in the
retained integral agrees with the note. The manuscript correctly records
64 full \(\rho\)-panels, both \(x\)-endpoints, hence 128 directed endpoint
checks, followed by concavity on the full interval. The two minimum margins
are unchanged:

\[
 \mathcal I^\mathrm{G}_\rho(V)>0.211576376293,
\qquad
 \frac{137}{100}\mathcal I^\mathrm{G}_\rho(V)-x
 >0.0214999332585.
\]

### The open small-\(\delta\) interval

Lines 5814-5841 use the negative coefficient

\[
 \frac{3-L}{4}-c<0,
 \qquad L=\frac{29}{10},
\]

correctly: for \(0<\delta<1\), replacing \(\delta\) by the closure boundary
\(1\) gives a strict lower bound. The remaining polynomial decreases over
the certified \(c\)-interval and gives exactly

\[
 c\mathcal S>\frac{1373893}{75000000}>0.
\]

### Residual cutoff and integer rounding

Lines 5843-5887 keep the two independent fixed-ratio directions distinct:
\(C_*<13/10\) controls the upper sum, while \(C_*>1/2\) controls the
square-root comparison. The manuscript has

\[
 \eta_\rho>\frac1{147},\qquad
 \eta_\rho<\frac19,
\]

\[
 a_\rho+2\eta_\rho C_*
 <\frac{8165}{113}+\frac{13}{45}
 =\frac{368894}{5085}<73,
\]

and therefore the exact cutoff

\[
 K_0(\rho)<73\cdot147^2=1577457.
\]

The strict real bounds are converted conservatively to
\(2r\leq3154913\), \(n\leq1577456\), and
\(f,B\leq525819\). No equality case is introduced by rounding.

### Reproduction statement

Lines 5889-5904 correctly name the Round 8G verifier and state the panel
counts as \(64/256/64/128\). They also state exact rational endpoints,
outward-rounded Arb enclosures, exact rational ledgers and cutoff, and both
frozen Round 8F pins. The final sentence again disclaims certification of
the finite residual walls.

## 3. Global status and scope consistency

The same scope occurs consistently in all four global locations:

| location | source lines | rendered pages | audit result |
|---|---:|---:|---|
| abstract | 70-94 | 1-2 | \(\rho\geq23/25\); exact residual; explicitly not a proof of residual walls |
| Statement and status | 168-174 | 3 | exact exclusion and residual; residual analytic walls uncertified |
| Round 8G theorem and proof | 5386-5904 | 66-72 | exact theorem scope and repeated residual disclaimer |
| Remaining proof obligations | 6522-6566 | 80 | exact residual and explicit warning against closure from finiteness |

Every location gives the residual as

\[
 \frac1{3154914}<\rho<\frac{23}{25},\qquad
 \frac{21}{4}<K<1577457.
\]

No abstract, theorem, status paragraph, conclusion, or remaining-obligations
paragraph claims the full shifted-tail theorem or claims that the residual
high-floor fixed-ratio walls are proved.

## 4. Independent build and log audit

I built the pinned source independently into the requested distinct
directory

`manuscript/build-general-d-round8g-integration-audit/`.

The bundled LaTeX wrapper was run with Python UTF-8 mode to avoid a Windows
console-decoding failure in its TeX-tool probe. The actual build then used
MiKTeX `latexmk`/`pdflatex`, exited 0, and produced 81 letter-size pages.

| independent artifact | bytes | SHA-256 |
|---|---:|---|
| PDF | 838,362 | `8170BBF641850155CD7DBB01A22DB6D26BEF4E42A5FBBFA42959D55F3CAD89A0` |
| TeX log | 23,937 | `2F64F9F513913C968631D9D8A7F6A265B880848B55D9A6FED2AECB38C7B2DD8A` |
| layout-preserving extracted text | 307,752 | `CF13AE940EE8AA78086C6291DDD21A6B7B812F1FF26F14A5C01FB784995753A3` |

The independent PDF hash differs from the production PDF hash because the
two files have different creation/modification timestamps. They have the
same byte count and page count, and their extracted text files are
byte-for-byte identical, with the common text hash shown above.

Both the production log and the independent log have these diagnostic-form
counts:

| diagnostic | production | independent |
|---|---:|---:|
| LaTeX/package/class warnings | 0 | 0 |
| undefined or rerun references/citations | 0 | 0 |
| overfull or underfull boxes | 0 | 0 |
| TeX/LaTeX fatal or ordinary errors | 0 | 0 |

The substring `warning` inside the loaded package name `infwarerr` is not a
diagnostic and was not miscounted as one.

The extracted PDF text contains zero occurrences of literal `qquad`, `??`,
`undefined`, or U+FFFD. A source-level negative-lookbehind scan also finds
zero unescaped `qquad` tokens.

## 5. Rendered-page inspection

Following the PDF inspection workflow, I rendered and visually inspected
pages 1-3, 66-72, and 80-81 at 160 dpi. This covers the complete abstract,
Statement and status, every page of the Round 8G theorem and proof, the
Remaining proof obligations section, and the final references transition.

| page | rendered PNG SHA-256 |
|---:|---|
| 1 | `3E388DCEE741D7A07227252FADA67086586C002818719C724D13032AC06AF5D9` |
| 2 | `365AA91C3A99B153288DD78A95D899E49F8A0BAF1D7F805747FFFCEC324A89DA` |
| 3 | `1DB92C18DC1CC68A44770106C9C5429C20325099AA9B9D5A0D07BB62DCF0FED5` |
| 66 | `B8D68A97C65015D91FFDA10B1829DC78C62F0581F2366CB645DE731D3A146430` |
| 67 | `B1D430B3FF03D28045FF891EDB805B45DA0B37750D3BC8A8516FFA6D2E396E14` |
| 68 | `866FFDB9DBA27CAFC40C0A97EE01BA18DAF31EB36AC4F6E6B806FEF2D68E8293` |
| 69 | `7AD1826055D77A5FB1F442149018CAD5A85AD3DDD016844ACAC6E20933AD9F29` |
| 70 | `5DA8160EDC7D1292287190DB64152146AF5DCB06197A5AC3D767F2A3715367C5` |
| 71 | `7089C818CF2D9E87267F3AB27CA9CBD3993255E2916D84B17F88EC7D9566BAF3` |
| 72 | `97A6F7AA68D4775975F1C37EB2AE01FCE19E5412CD73A61FD5A8353E5DAA7681` |
| 80 | `569B10DC42E96A0A7B2C6DA2534637BEB58F16599449928DA633E0742E964CA6` |
| 81 | `E116CAFE487BBF86DFD615D0F25B93B869F25E4B8613997DFE04E72BC672ACDF` |

All inspected pages are clean: no clipping, overlap, broken glyph, black
box, missing equation number, malformed hyperlink, bad margin, or unreadable
formula was found. Page transitions preserve complete sentences and the
residual disclaimers are plainly legible.

## 6. Preservation hashes

The frozen Round 8F/8G proof chain rehashed as follows:

| artifact | SHA-256 |
|---|---|
| Round 8F proof note | `ABAFE9A9C0B57607CA0945313D0C0A7B1602D6067D84587F14C274898EF7D196` |
| Round 8F verifier | `066A64BE535AFE212B107928D7845E9BC27D210D144A9E99FDE16DCCDF5A866C` |
| Round 8F proof audit | `87382053EABDDE184F530064FF938BF6B33F4EFA2F12438F47AD542EDBFD268A` |
| Round 8F manuscript-integration audit | `F6E31759D3F9706774DE5A873030A12873191949F306D5694C6EE0438B4979EE` |
| Round 8G corrected proof note | `C45D339383FD4E6921C3C60D058E14628846DF57E7F7808D62B373AB2476DE90` |
| Round 8G verifier | `873D9E4259DC0827C8917EB8CD04C169303B8D973C332CD2A75DA5038FC19F34` |
| Round 8G proof audit | `203BC49B2F4E61B932D3CA6D2483D295729FCBDE830A813D8EC9DD3AB2AD38A7` |

The canonical high-floor no-drop sources rehashed as follows:

| source | SHA-256 |
|---|---|
| aggregate checker | `173EBDB66E00309F79C6F8261593B6B59A3975F5019C9F075B1ECDAECCCF4081` |
| high-floor wrapper | `5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F` |
| shard launcher | `A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092` |
| shared compact core | `EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE` |
| exhaustion verifier | `81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A` |

The canonical no-drop stdout hashes are:

| log | bytes | SHA-256 |
|---|---:|---|
| shard 0 | 44,480 | `11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011` |
| shard 1 | 44,372 | `23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B` |
| shard 2 | 43,892 | `BFA5FEB83B620D5BA633066466FE826CB7FBE8D3938FB0484755857D1E5B4874` |
| shard 3 | 21,927 | `3EDC9AB31B5D539503A54E21165D4F5DC599BD80DA75C897156D58DE27316868` |
| shard 4 | 43,876 | `8800A1407E7C3AC0906D166E7EC7789B4A3C4EC2BAC90E22A6FAA4E0194490DF` |
| shard 5 | 43,838 | `4152DF07FCBFA6EFC70B8875085029B9A4A77ED740317B80225FC610B3A40FE4` |
| shard 6 | 43,858 | `AAC9DDE7EF38F78AB89AA5F06380CD8ED7733EDA1C94A549188F51A28D190930` |
| shard 7 | 43,914 | `AC01F88A2F0C97DDDDA4D1B16008A8344BBC1FEE73D185A9EE41F5E2BF4009E4` |
| final aggregate | 5,334 | `2E11E13CA0C00C39E09171CEDEDD8D31C5D4314DF68D1958AF7A0553F6BD09C6` |

All eight canonical shard stderr logs and the canonical final-aggregate
stderr log are present, have zero bytes, and have the empty-file SHA-256
`E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`.
Transient `.replay.*` files were intentionally excluded from this frozen
canonical-log ledger.

Finally, the original dimension-three paper remains:

| artifact | bytes | SHA-256 |
|---|---:|---|
| `manuscript/spherical-shell-polya-proof.tex` | 57,258 | `E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4` |
| `manuscript/spherical-shell-polya-proof.pdf` | 478,750 | `FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F` |

## 7. Verdict

**FINAL PASS.** The Round 8G theorem and proof are faithfully integrated,
all analytic directions and constants agree with the corrected proof note
and its independent audit, the global status language is exact and does not
overclaim closure, the independent 81-page build is clean, the rendered
pages are visually sound, and every requested frozen artifact rehashes to
the recorded value.
