# Clean-room adversarial audit of `ledger-packets-AB.tex`

Date: 2026-07-16  
Audited source SHA-256: `B5D21260D757D299ACB22EF3A0FD26D3A95A88AE3B0365988E5CBECD787EB6A6`  
Verdict: **PASS**

I froze the source at the digest above and reconstructed its arguments without
using its conclusions as premises. I independently checked the elementary
proof of the pi enclosure, every printed cap identity, the symbolic product
deficit, the zero-cut/channel-cut monotonicity argument, all radical and
moving-crossing fractions, every checkpoint-table entry, both radial
exclusions, and the two presentations of the 288-row coverage contract.

No mathematical defect, missing checkpoint tail, reversed inequality, or row
overlap was found. The exact verifier independently replays all 611 baseline
rows and still reports PASS with the canonical digest printed in the note.
The note is therefore a valid analytic replacement for the 288 rows it
claims, subject to its stated scope: the ball-zero anchors and their angular
propagation theorem remain analytic inputs from the main paper, while their
finite consequences are eliminated here without a search.

## 1. Sources and frozen baseline

The audit compared the note with:

- `manuscript/spherical-shell-polya-proof.tex`, especially the product bound,
  shell-to-ball comparison, angular propagation, zero registry, high
  checkpoint inventories, cap tables, and optical product deficit;
- `manuscript/spherical-shell-polya-supplement.tex`, Supplement S1; and
- `computations/certification/verify_analytic_ledgers.py`.

The Python verifier embedded in Supplement S1 is exactly identical, line for
line, to the standalone verifier: both have 1,526 lines and `Compare-Object`
reports no difference. Running the standalone verifier produced

```text
PASS
first issue: none
core exact finite checks: 553
core substantive checks: 488
core bookkeeping identities: 65
supplemental exact checks: 58
combined registry rows: 611
canonical registry sha256: afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1
```

This matches the baseline count and digest in the audited note.

## 2. Independent check of the pi enclosure

The four-term alternating lower sum is exactly

\[
 \frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}
 -\frac1{7\cdot5^7}
 =\frac{323852}{1640625}.
\]

The alternating-series remainder has the directions stated in the source.
Together with \(\arctan(1/239)<1/239\), it gives

\[
 16\frac{323852}{1640625}-\frac4{239}
 =\frac{1231847548}{392109375}.
\]

Machin's identity is independently confirmed by

\[
 \tan\!\left(4\arctan\frac15\right)=\frac{120}{119},
 \qquad
 \tan\!\left(4\arctan\frac15-\arctan\frac1{239}\right)=1,
\]

and the angle lies in \((0,\pi/2)\), fixing the branch as \(\pi/4\).
The lower margin printed in the note is exact:

\[
 \frac{1231847548}{392109375}-\frac{333}{106}
 =\frac{3418213}{41563593750}>0.
\]

For the upper bound, direct polynomial division gives

\[
 \frac{x^4(1-x)^4}{1+x^2}
 =x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2}.
\]

Its integral from zero to one is therefore \(22/7-\pi\), and the
integrand is strictly positive in the open interval. Finally,

\[
 \frac{22}{7}-\frac{333}{106}=\frac1{742}>0.
\]

Thus the enclosure, its nonemptiness, and the reciprocal inequality all have
the claimed strict directions. This supplies the four analytic replacements
assigned to `verify_pi`.

## 3. Strict brackets and every cap identity

For all real \(x\), the positive integers strictly below \(x\) are empty
when \(x\leq1\) and otherwise are
\(1,\ldots,\lceil x\rceil-1\). Hence

\[
 [x]_{<}=\max\{0,\lceil x\rceil-1\}.
\]

This proves the 16 integer/half-integer rows and the seven phase-proxy wall
rows in `verify_strict_face_conventions`, as well as the distinct optical
radial equality-owner row. At a product wall
\(x^2=h(h+1)\), strictness excludes \(h\), so the cap is \(h^2\).

The telescoping identity

\[
 \sum_{\ell=0}^{h}(2\ell+1)=(h+1)^2
\]

reproduces every non-dash entry in the two rectangular tables. Their exact
row counts are:

| table | non-dash executable cap rows |
|---|---:|
| \(k_8\) | \(5+3+5+5=18\) |
| \(k_9\) | \(1+4+6+6+6=23\) |

Together with the two \(k_7\) bookkeeping rows, twelve \(k_{10}\) rows,
and six \(k_{11}\) rows, this is exactly 61 cap-table rows. I separately
checked all displayed decompositions; in particular

\[
 49+25=74,\quad 49+16+4=69,\quad 49+25+4=78,
 \quad49+36=85,\quad49+36+4=89,
\]

and the six lower caps are exactly
\((45,46,59,66,69,78)\). The ten lower-\(d\) odd sums are exactly
\((1,4,9,10,16,17,26,29,40,45)\).

There is no executable-row collision hidden by the repeated number 74. The
\(k_9\) rectangular table contains one bookkeeping row for its \(H=6,h=4\)
entry, while `verify_k9_h6_h4_path` contains a second, separately labelled
bookkeeping row asserting \(49+25=74\). The same analytic identity validly
replaces both distinct rows. Likewise, the 12 strict-face angular blocks, the
12 optical angular blocks, and the 10 supplemental lower-\(d\) blocks are
separate registry rows even though they instantiate the same odd-sum lemma.

Consequently the block-cap allocation is exactly

\[
 12+12+(61+1)+1+10=97,
\]

with no double-counted executable row.

## 4. Product-deficit algebra and uniform reserve

Inserting \(\sum_{n=1}^N n^2=N(N+1)(2N+1)/6\) and expanding independently
gives

\[
 \frac23(N+t)^3-N(N+t)^2+\sum_{n=1}^Nn^2
 =\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
\]

With \(C=1382/3125\) and \(A=1/2-C=361/6250\), subtraction of
\(C(N+t)^2\) gives the printed \(G_N(t)\). Its forward difference satisfies

\[
 G_{N+1}-G_N=A(2N+1)+t^2-2Ct+\frac16.
\]

Because \(0<C<1\), the quadratic minimum on \((0,1]\) is
\(1/6-C^2\), and for \(N\geq1\)

\[
 G_{N+1}-G_N\geq3A+\frac16-C^2
 =\frac{4229603}{29296875}>0.
\]

Finally,

\[
 G_1'(t)=2(t-C)(t+1),
 \qquad
 G_1(C)=\frac{1822532}{91552734375}>0.
\]

Thus the minimum is global over every integer \(N\geq1\) and
\(0<t\leq1\), including the strict radial-wall convention \(t=1\). The
symbolic proof replaces the five general product-deficit rows and all 18
sampled expansion rows without relying on the sampled grid.

## 5. Cut monotonicity and sufficiency of the zero anchors

The angular propagation theorem in the main paper states, for \(p\geq j\),

\[
 j_{p+1/2,n}^2\geq j_{j+1/2,n}^2
 +p(p+1)-j(j+1).
\]

Therefore every strict anchor in the note supplies the propagated lower
bound \(\mathfrak B_n(\ell)\). When \(\ell\) is increased by one, every
old candidate in the maximum gains exactly \(2(\ell+1)\), while a newly
eligible anchor cannot reduce the maximum. Hence

\[
 \mathfrak Z_{m,n}(\ell+1)
 \geq\mathfrak Z_{m,n}(\ell)+2(\ell+1),
\]

whereas

\[
 \mathfrak C_{m,n}(\ell+1)
 =\mathfrak C_{m,n}(\ell)-\frac{2(\ell+1)}{n^2-1}.
\]

For a counted channel, the product condition requires
\(z^2<\mathfrak C\), while the strict propagated ball-zero bound requires
\(z^2>\mathfrak Z\). Thus \(\mathfrak Z\geq\mathfrak C\) excludes the
base channel and, by opposite monotonicity, its infinite angular tail. The
argument remains valid when \(\mathfrak C\) becomes nonpositive and does
not rely on checking a finite terminal angular index.

The printed anchors suffice for every first-excluded channel:

- for \(n=2\), the first-excluded indices are \(2,4,5,6,5\); the anchors at
  \(1,2,3,5\) provide a candidate at every one of these indices;
- for \(n=3\), both first-excluded indices equal 2, for which the
  \((61/5)^2\) anchor is direct; and
- no anchor at \(\ell=0\) is needed, because the inventory intentionally
  retains \(\ell=0,1\) for the third radial layer at \(k_{10},k_{11}\).

The note does not purport to reprove these Bessel-zero anchors. Their strict
analytic proofs and the angular-propagation comparison are in the main paper,
consistent with the note's scope statement.

## 6. Radicals, endpoint order, and all moving crossings

All six radical margins were recomputed exactly:

\[
\begin{array}{c|c}
337-(183/10)^2=211/100 &(92/5)^2-337=39/25\\
7073/64-(1051/100)^2=2221/40000 &(1052/100)^2-7073/64=6191/40000\\
114-(1067/100)^2=1511/10000 &(107/10)^2-114=49/100.
\end{array}
\]

The endpoint margins \(119/530\), \(32/1211\), and \(119/530\), the two
middle radical gaps \(17/64\) and \(223/64\), and the propagation identity
\((81/8)^2+8=7073/64\) are also exact.

For a wall enclosure \(w_-<w<w_+\), monotonicity of
\(r_w=1-3\pi/w\) gives

\[
 1-\frac{66/7}{w_-}<r_w<1-\frac{999/106}{w_+}.
\]

Evaluation yields precisely the five pairs printed in the source:

\[
\begin{gathered}
 \frac2{35}<r_{10}<\frac{61}{1060},\qquad
 \frac{13}{189}<r_{81/8}<\frac{11}{159},\\
 \frac5{49}<r_{21/2}<\frac{38}{371},\qquad
 \frac{757}{7357}<r_{\sqrt{7073}/8}<\frac{2903}{27878},\\
 \frac{79}{679}<r_{\sqrt{114}}<\frac{676}{5671}.
\end{gathered}
\]

Subtracting consecutive outer bounds gives, in order,

\[
 \frac{2251}{200340},\quad \frac{256}{7791},\quad
 \frac{183}{389921},\quad \frac{231225}{18929162},
\]

all positive. The endpoint margins are exactly

\[
 \frac2{35}-\frac{10}{183}=\frac{16}{6405},
 \qquad
 \frac7{51}-\frac{676}{5671}=\frac{5221}{289221}.
\]

The inputs \(\rho_0<10/183\) and \(\rho_c>7/51\) follow in the stated
directions from the radical and pi bounds. Hence the five crossings are
strictly inside the ratio strip and strictly ordered. These facts replace
exactly five fixed-wall rows, one propagation row, three endpoint rows, ten
crossing-location rows, and four crossing-order rows: 23 rows total.

## 7. Checkpoint table, radial exclusions, and exhaustive inventories

Every checkpoint entry was reconstructed from the anchor maximum, not merely
checked by decimal approximation. The resulting \((B,Z,C,Z-C)\) quadruples
are

| \((m,n,\ell_0)\) | independently reconstructed \((B,Z,C,Z-C)\) |
|---|---|
| \((7,2,2)\) | \((81,25,50/3,25/3)\) |
| \((8,2,4)\) | \((11409/100,4209/100,52/3,7427/300)\) |
| \((9,2,5)\) | \((16641/100,7641/100,20,5641/100)\) |
| \((10,2,6)\) | \((17841/100,6841/100,68/3,13723/300)\) |
| \((11,2,5)\) | \((16641/100,3441/100,34,41/100)\) |
| \((10,3,2)\) | \((3721/25,971/25,13,646/25)\) |
| \((11,3,2)\) | \((3721/25,421/25,63/4,109/100)\) |

The two non-anchor propagated bases are exactly the values printed in the
source. The smallest incompatibility margin is \(41/100>0\), so equality
ownership is not being used to hide a zero margin.

On \(\rho\geq\rho_c\),

\[
 z>\frac{193}{53},\qquad z^2>\frac{37249}{2809}.
\]

The radial margins independently reduce to

\[
 \frac{37249}{2809}-\frac{90}{8}=\frac{22591}{11236}>0,
 \qquad
 \frac{37249}{2809}-\frac{132}{15}=\frac{62649}{14045}>0.
\]

Thus \(n=3\) is impossible through \(k_9\), and \(n\geq4\) is impossible
through \(k_{11}\). For \(n=1\), strictness of
\(\ell(\ell+1)<m(m+1)\) gives precisely \(0\leq\ell\leq m-1\). For
\(n=2\) and the two surviving \(n=3\) checkpoints, the seven base rows and
cut monotonicity remove the whole tails. These cases exhaust all radial
indices \(n\geq1\) and prove exactly the five printed upper inventories.

The 117 checkpoint rows reconcile exactly as

\[
 32\text{ metadata/tail rows}+7\text{ base covers}
 +2\text{ radial exclusions}+76\text{ repeated monotonicity rows}=117.
\]

The 76 repeated rows are the two strict monotonicity checks at each later
index through 12 in the five executable loops:
\(20+16+14+12+14=76\). The analytic lemma proves the infinite tails, so it
is stronger than those finite replay instances.

## 8. The 288-row allocation and disjointness audit

The exhibit-based allocation is arithmetically exact:

\[
 4+24+97+23+117+23=288.
\]

The independent executable-family allocation is also exact:

| executable family | family rows | rows replaced by A/B |
|---|---:|---:|
| `verify_pi` | 4 | 4 |
| `verify_thresholds` | 34 | 23 |
| `verify_strict_face_conventions` | 35 | 35 |
| `verify_lower_inventories_and_payments` | 44 | 1 |
| `verify_checkpoint_inventories` | 117 | 117 |
| `verify_cap_tables_and_payments` | 98 | 62 |
| `verify_optical_constants` | 50 | 36 |
| supplemental \(k_6\)/lower-\(d\) ledger | 26 | 10 |
| **total** |  | **288** |

The potentially ambiguous splits were checked against individual labels:

- the 35 strict-face rows split as 16 bracket rows, 12 angular-block rows,
  and seven phase-proxy rows;
- the 62 cap rows split as 61 table rows plus the separately labelled
  cap-74 path identity;
- the 36 optical rows split as 12 angular blocks, one radial equality owner,
  five general product facts, and 18 sampled expansions; and
- the ten supplemental lower-\(d\) cap rows are distinct from every core
  row.

Therefore no executable row is counted twice. The unclaimed remainder is
\(611-288=323\) rows, agreeing with the note and preserving the separation
from zero-sign proofs, event/payment implications, seam arithmetic, optical
screens, and exact owner subtraction.

## 9. Scope qualification

The PASS verdict means that Packets A and B correctly replace the stated 288
finite exact-ledger predicates by hand-checkable analytic arguments. It does
not promote the note into a standalone proof of the spherical-shell theorem:
the strict Bessel-zero anchors, angular propagation, event assignments,
payments, seam analysis, optical endpoint screens, and owner subtraction are
supplied by the main paper or the other analytic packets. This is exactly the
scope asserted by the source, not an unreported gap.

## 10. Compilation

After the audit was written, I compiled the frozen source with the bundled
Tectonic 0.16.9 workflow. Tectonic completed successfully after its normal
cross-reference reruns and produced a nine-page PDF. The final pass reported
no unresolved references or compilation error.

Compiled PDF: `manuscript/analytic/ledger-packets-AB.pdf`  
PDF SHA-256: `8FCD69609A46285FC2FB20CCECBBAB4318553DF1D5CAE10C463F6B568849A6C7`
