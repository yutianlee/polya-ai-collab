# Exact-ledger decomputerization inventory

Date: 2026-07-16

Sources inventoried:

- manuscript/spherical-shell-polya-proof.tex;
- Supplement S1 in manuscript/spherical-shell-polya-supplement.tex;
- computations/certification/verify_analytic_ledgers.py.

This inventory concerns the **611 exact-ledger checks only**. It does not
cover either Arb interval certificate, and it does not bulk-transcribe the
ledger.

## 1. Exact count reconciliation

| registry | substantive | bookkeeping | total |
|---|---:|---:|---:|
| core | 488 | 65 | 553 |
| supplemental | 48 | 10 | 58 |
| **combined** | **536** | **75** | **611** |

The checks split by executable family and mathematical destination as
follows.

| executable family | count | mathematical lemma or table |
|---|---:|---|
| verify_pi | 4 | rational \(\pi\)-enclosure |
| verify_thresholds | 34 | ratio/frequency ordering; lower closure |
| verify_strict_face_conventions | 35 | strict floors and equality owners |
| verify_zero_specializations | 48 | zero/sign registry and first-zero table |
| verify_lower_inventories_and_payments | 44 | lower-closure lemma and cap-395 cell |
| verify_checkpoint_inventories | 117 | exhaustive \(k_7,\ldots,k_{11}\) inventories |
| verify_cap_tables_and_payments | 98 | high-staircase cap/payment tables |
| verify_localizations | 47 | high-staircase split/event registry |
| verify_u_and_k11 | 8 | \(k_{11}<U\) and the \(K_0\) owner |
| verify_optical_constants | 50 | all-frequency optical theorem |
| verify_exact_subtraction | 68 | \(\mathcal D_{19}\to\mathcal D_{20}\) |
| **core total** | **553** | |
| seam ledger | 22 | primitive seam owner |
| \(k_6\)/lower-\(d\) wall-cap ledger | 26 | two-sided staircase |
| lower-\(d\) payment ledger | 9 | lower side through \(d\) |
| cap-74 incompatibility | 1 | corrected \(k_9\) cap-74 cell |
| **supplemental total** | **58** | |

Every one of the 611 checks belongs to one of these rows.

## 2. Print-status notation

- **P (printed):** the main paper prints the mathematical predicate and its
  exact witness or reserve.
- **C (compressed):** the conclusion is printed, but the exact wall-to-cell
  mapping or decisive arithmetic is only in S1.
- **R (repeated instance):** many ledger rows test one symbolic identity.
  They should be replaced by one general lemma, not transcribed.
- **X (executable-only):** the particular predicate or mapping is not
  exposed in a hand-checkable main-paper table.

## 3. Core registry

### 3.1 Rational \(\pi\) enclosure: 4

| subfamily | count | status |
|---|---:|---|
| Machin interval is nonempty | 1 | R |
| \(\pi>333/106\), \(\pi<22/7\) | 2 | P |
| \(1/\pi<106/333\) | 1 | P |

The two \(\pi\)-bounds are printed as cm:eq-pi, and the reciprocal is
printed in the optical proof. One analytic proof of the two-sided
\(\pi\)-bound replaces all four rows.

### 3.2 Threshold and wall ordering: 34

| subfamily | count | status |
|---|---:|---|
| \(\rho_*<\rho_0<\sigma<\rho_c<39/50<7/8\) | 5 | P |
| \(\omega_0<\rho_c\), \(\omega_0d>1\) | 2 | P/C |
| \(d<10<81/8<21/2<\sqrt{7073}/8<\sqrt{114}\) | 5 | P |
| \((81/8)^2+8=7073/64\) | 1 | P |
| endpoint comparisons for \(3z(\rho_0)\), \(3z(\rho_c)\) | 3 | C |
| five \(3z=\) fixed-wall crossings lie between \(\rho_0,\rho_c\) | 10 | X |
| order of those five moving crossings | 4 | X |
| \(\sqrt{114}<2/\omega_0<367/20\), \(\rho_c<3\omega_0/2\), \(\omega_0\sqrt{114}>1\) | 4 | P/C |

The ratio and fixed-frequency chains are printed. The **14 moving-\(3z\)
crossing predicates are executable-only** and need one exact ordering table.

### 3.3 Strict face conventions: 35

| repeated identity | count | status |
|---|---:|---|
| strict integer and half-integer bracket instances | 16 | R |
| \(\sum_{j<\ell}(2j+1)=\ell^2\), \(\ell=0,\ldots,11\) | 12 | R |
| phase-proxy integer walls \(n=1,\ldots,7\) | 7 | R |

One lemma
\[
[x]_< =\lceil x\rceil-1,\qquad
\sum_{j=0}^{m-1}(2j+1)=m^2
\]
replaces all 35 rows.

### 3.4 Zero specializations: 48

| subfamily | count | status |
|---|---:|---|
| eight internal zero faces, five checks each | 40 | P/C |
| Lorch specializations for \(\ell=8,9,10\) | 3 | P |
| spherical-Bessel sign checks at those three Lorch walls | 3 | R/C |
| \(103/10>81/8\), \(61/5>21/2\) | 2 | P |

The main paper prints the eight-row sign/count table, the nonautomatic
rational comparisons, the internal zero registry, and the Lorch residual
table. The three extra Lorch sign checks are redundant once the strict
first-zero lower bounds are established. The recurrence/Taylor arithmetic
for several signs is compressed, but the necessary rational witnesses are
already substantially present in the main text.

### 3.5 Lower inventory and cap-395 closure: 44

| subfamily | count | status |
|---|---:|---|
| activation/exclusion consequences through \(\sqrt{114}\) | 8 | P |
| six lower inventory caps as one tuple check | 1 | P/R |
| five lower Weyl payments | 5 | P |
| cap 395, fifteen proxy rows, tail monotonicity, exceptional payment | 18 | P |
| finite floor-cell and endpoint instances | 12 | R/C |

The main lower-closure lemma prints the inventories, five reserves, all
proxy caps and integer margins, cap 395, and its exceptional payment. The
last twelve rows instantiate one floor inequality and two boundary-owner
rules; they should be replaced by the general floor argument.

### 3.6 Checkpoint inventory completeness: 117

| subfamily | count | status |
|---|---:|---|
| strict first-mode metadata | 5 | R |
| finite first-angular-tail instances | 15 | R |
| finite second-inventory metadata | 5 | R |
| third-inventory metadata | 2 | R |
| maximal-radial-index metadata | 5 | R |
| first-excluded-index zero/channel comparisons | 7 | X |
| no third mode at \(k_7,k_8,k_9\) | 1 | C |
| no \(n\ge4\) through \(k_{11}\) | 1 | C |
| propagated zero cut increases | 38 | R/X |
| channel cut decreases | 38 | R/X |

The five final checkpoint inventories are printed, but their exhaustive
proof is not. The missing hand object is a seven-row table of the first
excluded zero/channel margins, followed by one symbolic proof that the zero
cut increases and the channel cut decreases. That replaces the 76 repeated
tail checks.

### 3.7 High-staircase cap tables and payments: 98

| subfamily | count | status |
|---|---:|---|
| cap arithmetic at \(k_7,\ldots,k_{11}\) | 61 | P/R |
| complete corrected cap-74 path | 13 | P |
| three impossible cap-table cells | 3 | C/X |
| moving-payment derivative bounds | 2 | C |
| five global checkpoint payments | 5 | C/X |
| seven conditional localizations/payments, two checks each | 14 | X |

The cap tables and cap-74 correction are printed. The **nineteen
global/conditional payment checks and three impossible cells are not printed
as a connected wall-to-cap table**. The main text lists only representative
reserves before asserting that every event is paid.

### 3.8 High-staircase localizations: 47

| subfamily | count | status |
|---|---:|---|
| distinctness/connectedness of ratio registry | 2 | R |
| 17 ratios lie in the high strip | 17 | R |
| expected possible/excluded side at each named channel event | 17 | X |
| \(z^2=16,68/3,34\) lie in the high strip | 3 | R/C |
| exact side/equality at those three algebraic splits | 3 | C |
| five special \(k_{11}\) localization implications | 5 | C/X |

The main paper prints the list of 17 ratios, but not the essential mapping
\[
(\rho,m,n,\ell)\mapsto
\operatorname{sign}\!\left(
m(m+1)-\ell(\ell+1)-(n^2-1)z_\rho^2\right).
\]
A 17-row localization table is therefore proof-critical.

### 3.9 \(k_{11}<U\): 8

These rows verify the endpoint inequality
\(\eta_\rho k_{11}<C_0\), the monotonic reduction, the seam comparison,
and exclusion of the \(H_0\)/seam owners on the surviving compact ratio
interval. The main paper prints the conclusion and a shorter
\(K_0>64>k_{11}\) argument, but not the eight executable predicates.
Most rows are redundant scope checks. A short two-branch analytic lemma is
the smallest replacement.

### 3.10 Optical constants: 50

| subfamily | count | status |
|---|---:|---|
| product-deficit positivity and exact minimum | 5 | P |
| sample evaluations of the symbolic product identity | 18 | R |
| low/high reserves, scaling, common face, monotonicity | 14 | P/C |
| twelve odd-sum block identities | 12 | R |
| radial equality-wall convention | 1 | P/R |

The main optical lemma prints the symbolic product deficit, exact minimum,
both exact reserves, and the monotonic screen argument. The 30 sample/block
rows are verification redundancy. Only a short expansion of the scaling and
common-face implications may be desirable.

### 3.11 Exact subtraction: 68

| subfamily | count | status |
|---|---:|---|
| \(9\times7\) state truth table | 63 | R/X |
| five boundary/ownership assertions | 5 | P |

The paper prints \(\mathcal D_{19}\), \(\mathcal D_{20}\), and the ownership
of \(\rho_0,\rho_c,39/50,k_{11},U\). The 63 grid rows are brute-force set
algebra and should be replaced by one formal set-difference calculation,
not transcribed.

## 4. Supplemental registry

### 4.1 Seam arithmetic: 22

| subfamily | count | status |
|---|---:|---|
| \(\pi,\sqrt2,y\), shelf enclosures | 5 | P/C |
| displacement/localization arithmetic | 5 | P/C |
| derivative cap and synthetic slope | 4 | C |
| endpoint \(Q,\widehat q\), initial reserve | 3 | P/C |
| action gain, loss, interface cap, terminal reserves | 5 | P |

The seam proof prints the decisive inequalities and terminal reserves, but
not a compact derivation table for all intermediate identities. In
particular the exact derivative proxy is only regenerated in S1. A one-page
seam arithmetic table is sufficient.

### 4.2 \(k_6\) and lower-\(d\) wall/cap ledger: 26

| subfamily | count | status |
|---|---:|---|
| two \(\pi\)-bounds | 2 | P |
| six moving \(k_6\) payments | 6 | C |
| five fixed \(k_6\) payments | 5 | P/C |
| ten lower-\(d\) cap identities | 10 | P/R |
| three \(2z\) ordering/empty-cell checks | 3 | P/C |

The main paper prints the six moving numerators but not their positive
denominators. It prints the five fixed margins and the lower-\(d\) cap table.
The missing hand object is an eleven-row \(k_6\) wall/cap/payment table with
the **full rational difference**, not only its numerator.

### 4.3 Lower-\(d\) payments: 9

The seven fixed-wall reserves, initial \(L\)-payment, and moving \(2z\)
payment are all explicitly printed with their wall/cap association. No
additional transcription is needed.

### 4.4 Cap-74 incompatibility: 1

The main paper prints
\[
\frac{2409}{100}-\frac{70}{3}=\frac{227}{300}>0
\]
and the conservative cap-74 payment. No replacement is needed.

## 5. Material already hand-visible in the main paper

The following are already printed at a reconstructible level:

1. the global ratio chain and fixed frequency ordering;
2. the internal-zero sign/count table, zero registry, Lorch table, and
   propagated zero walls;
3. the lower-\(d\) cap table and all nine lower-\(d\) payments;
4. the lower-closure inventory, ordinary payments, cap-395 proxy list,
   integer margins, and exceptional payment;
5. the high cap tables and corrected cap-74 cell;
6. the optical product identity and both optical reserves;
7. \(\mathcal D_{19}\), \(\mathcal D_{20}\), and the five delicate owners;
8. the principal seam constants and terminal reserves.

These need editing or short supporting lemmas, not code transcription.

## 6. Proof-critical content still executable-only or materially compressed

In descending order of importance:

1. **High-event map:** 17 localization signs, seven conditional payments,
   five global payments, and three impossible cells.
2. **Checkpoint exhaustiveness:** seven boundary cuts and the monotonic
   argument replacing 76 repeated rows.
3. **Moving-\(3z\) ordering:** fourteen crossing/location predicates.
4. **Seam derivative arithmetic:** the exact derivative proxy and its
   intermediate rational identities.
5. **\(k_6\) payment mapping:** six moving payments lack full displayed
   rational differences.
6. **Formal subtraction:** the result is printed, but 63 executable state
   rows stand in for a short set-difference proof.

These are the pieces that must be replaced before the exact ledger ceases to
be a logical dependency.

## 7. Smallest hand-checkable replacement packet

The 611 rows should collapse to six exhibits, estimated at roughly 8--12
manuscript pages.

### Packet A: general exact-arithmetic lemmas

Prove the strict-bracket identity, odd-sum/block-cap identity, symbolic
product-deficit identity for all \(N,t\), and monotonicity of the affine
zero/channel cuts. This eliminates the repeated strict-face, cap-bookkeeping,
optical-sample, and checkpoint-tail rows.

### Packet B: ordering and inventory boundary table

Print the five \(3z\)-crossing ratios with their order, the seven checkpoint
first-excluded-index margins, and the two base radial exclusions. Follow the
table by the symbolic cut-monotonicity proof.

### Packet C: connected high-event registry

Print one table with columns
\[
\rho,\quad k_m,\quad(n,\ell),\quad\Delta,\quad
\operatorname{sign}\Delta,\quad\text{cap/payment consequence}.
\]
It must include all 17 localization ratios, three algebraic splits, three
impossible cells, five global payments, and seven conditional payments.
Every payment row should show an exact positive rational reserve.

### Packet D: seam and two-sided payment tables

Print a condensed 22-row seam dependency table, especially the derivative
proxy and its \(16/5\) margin, and an eleven-row \(k_6\) moving/fixed payment
table with full rational differences. Reference the already printed
lower-\(d\) payments.

### Packet E: upper owner and optical cleanup

Give a short two-branch proof of \(k_{11}<U\) and expand the handful of
optical scaling/common-face implications. The existing symbolic optical
argument remains unchanged.

### Packet F: exact owner subtraction

Replace the 63-state truth table by a one-page formal subtraction: partition
the ratio axis at \(\rho_*,\rho_0,\rho_c,39/50,7/8\), subtract the closed
lower/stair/optical owners, and list the five boundary owners.

## 8. Recommendation

Do **not** bulk-transcribe Supplement S1. Its large row count is driven by
instantiations of general identities and monotonic tail facts. The connected
high-staircase localization/payment table is the only sizable genuinely
missing finite object. Once Packets A--F are present and independently
audited, the script can remain as a reproducibility check, but the theorem
will no longer depend on executing its 611 predicates.
