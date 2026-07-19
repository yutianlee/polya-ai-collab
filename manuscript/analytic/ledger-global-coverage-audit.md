# Final disjoint coverage audit for the 611-row exact ledger

**Verdict: PASS.**

Audit date: 2026-07-16

The six global owners form a pairwise-disjoint partition of the canonical
611-row registry:

\[
278+83+57+22+68+103=611.
\]

There is no unallocated row, no multiply allocated row, and no row outside
the canonical universe. The core and supplemental subtotals separately
reconcile as \(553+58=611\).

## Frozen sources

| Artifact | SHA-256 |
|---|---|
| exact-ledger-inventory.md | DD6C9C712C4213CAB5F551C60E395144FA4FB19E048AD5E7CE606B91D4ABC1DD |
| ledger-packets-AB.tex | B5D21260D757D299ACB22EF3A0FD26D3A95A88AE3B0365988E5CBECD787EB6A6 |
| ledger-packets-AB-audit.md | A91F5E74E1129C1D8505CBD337EF0CF46EA778F40C8CBF03E578D58940E6AEEC |
| ledger-packet-C.tex | 131A0F84C5CD38881487DC6AA410401B068E824EE855652281A1A61756BFC776 |
| ledger-packet-C-audit.md | 59BDC4B56826F9FDCD150AED96D7688A9B51F630ACCA7CC7DDB5A09A0EC4223E |
| ledger-packet-D.tex | 17A08B124A6AE81B516E235046DB3ACCD4E7EDDC1C2A7CF6828FF87D6F3B7EBC |
| ledger-packet-D-audit.md | D215C7FEBFFB4053C2638C4B36950BF78C9ABAB2E07A906E6C953EFA1C8FAEF2 |
| ledger-packet-E.tex | 03259745FBF8D67930045B4F996DDF9F61A2F5A74E72CF7A95064351E59A6123 |
| ledger-packet-E-audit.md | 7C45854F3EB6EA192791DDA17B067CD1F2486FBC91C6E3C217E3D340925E61D1 |
| ledger-packet-F.tex | B137FDE7B974F55DD8EFD7D90501611939F291CAC80437C6F707C3CBC483E26E |
| ledger-packet-F-audit.md | 341C0FC8ACC5A1F74D9E969A404AE5020C0D5C9B57B30A143C319424AD96AB3B |
| ledger-main-visible.tex | 63B4100523F99126F38BD7A997A41328189A6E3CB832E276776775886267BF2F |
| ledger-main-visible-audit.md | EA56A1D17C7AD1D798BFC0D7702452E579AE3FBA121C21570F72DA20A3B0D7B9 |
| verify_analytic_ledgers.py | 41691116E0E3E5453B9B209ACB93FF784724C3A95B83C94BBDF7F6760616E716 |

The Supplement S1 Python listing is text-identical to the canonical
standalone checker, as independently recorded in the packet audits.

## Registry notation

Rows are numbered in the execution order inside each canonical function.
The following short names are used only in this audit:

| ID | Canonical family | Rows |
|---|---|---:|
| PI | verify_pi | 4 |
| TH | verify_thresholds | 34 |
| SF | verify_strict_face_conventions | 35 |
| Z | verify_zero_specializations | 48 |
| LI | verify_lower_inventories_and_payments | 44 |
| KI | verify_checkpoint_inventories | 117 |
| CP | verify_cap_tables_and_payments | 98 |
| LOC | verify_localizations | 47 |
| U | verify_u_and_k11 | 8 |
| OPT | verify_optical_constants | 50 |
| SUB | verify_exact_subtraction | 68 |
| SUP | supplemental registry | 58 |

The first eleven families total 553 core rows. SUP1--SUP58 are the
supplemental rows in their canonical execution order.

## Precise one-to-one allocation

| Canonical family | Full universe | AB | C | D | E | F | main-visible |
|---|---:|---|---|---|---|---|---|
| PI | PI1--PI4 (4) | PI1--PI4 (4) | -- | -- | -- | -- | -- |
| TH | TH1--TH34 (34) | TH8--TH30 (23) | -- | -- | -- | -- | TH1--TH7, TH31--TH34 (11) |
| SF | SF1--SF35 (35) | SF1--SF35 (35) | -- | -- | -- | -- | -- |
| Z | Z1--Z48 (48) | -- | -- | -- | -- | -- | Z1--Z48 (48) |
| LI | LI1--LI44 (44) | LI9 (1) | -- | -- | -- | -- | LI1--LI8, LI10--LI44 (43) |
| KI | KI1--KI117 (117) | KI1--KI117 (117) | -- | -- | -- | -- | -- |
| CP | CP1--CP98 (98) | CP1--CP43, CP56, CP60--CP77 (62) | CP44--CP55, CP57--CP59, CP78--CP98 (36) | -- | -- | -- | -- |
| LOC | LOC1--LOC47 (47) | -- | LOC1--LOC47 (47) | -- | -- | -- | -- |
| U | U1--U8 (8) | -- | -- | -- | U1--U8 (8) | -- | -- |
| OPT | OPT1--OPT50 (50) | OPT15--OPT50 (36) | -- | -- | OPT1--OPT14 (14) | -- | -- |
| SUB | SUB1--SUB68 (68) | -- | -- | -- | -- | SUB1--SUB68 (68) | -- |
| SUP | SUP1--SUP58 (58) | -- | -- | SUP1--SUP57 (57) | -- | -- | SUP58 (1) |

Every range is inclusive.

## Owner totals

| Global owner | Core rows | Supplemental rows | Total |
|---|---:|---:|---:|
| AB | \(4+23+35+1+117+62+36=278\) | 0 | 278 |
| C | \(36+47=83\) | 0 | 83 |
| D | 0 | 57 | 57 |
| E | \(8+14=22\) | 0 | 22 |
| F | 68 | 0 | 68 |
| main-visible | \(11+48+43=102\) | 1 | 103 |
| **total** | **553** | **58** | **611** |

This table also proves that the requested owner totals are not merely a
numerical decomposition: each total is the cardinality of explicitly
listed canonical row IDs.

## Special allocation decisions

### 1. AB's ten supplemental lower-\(d\) rows belong globally to D

Within the supplemental registry:

- SUP1--SUP22 are the seam ledger;
- SUP23--SUP24 are the two payment-ledger \(\pi\) rows;
- SUP25--SUP30 are the six moving \(k_6\) payments;
- SUP31--SUP35 are the five fixed \(k_6\) payments;
- SUP36--SUP45 are the ten lower-\(d\) block-cap identities;
- SUP46--SUP48 are the three \(2z\) ordering predicates;
- SUP49--SUP57 are the nine lower-\(d\) payments;
- SUP58 is the cap-74 incompatibility.

Packet AB analytically proves the odd-sum lemma that also implies
SUP36--SUP45, so its local source coverage count is 288. For the global
partition those ten rows are assigned to Packet D, which owns the complete
SUP1--SUP57 sequence. Therefore AB's global count is

\[
288-10=278,
\]

and D's count remains 57. This is proof redundancy, not row overlap.

### 2. The supplemental cap-74 predicate belongs to main-visible

Packet C owns the twelve non-bookkeeping core cap-74 path rows
CP44--CP55. The core bookkeeping identity CP56 belongs to AB.

The distinct supplemental incompatibility predicate

\[
\frac{2409}{100}-\frac{70}{3}=\frac{227}{300}>0
\]

is global row SUP58. It is assigned to main-visible, whose packet-local
name for this predicate is S1. Packet C's 83-row global allocation contains
no supplemental row. Thus the cap-74 mathematics may be displayed in more
than one proof exhibit, but the executable row SUP58 is counted exactly
once.

### 3. Packet E's repeated optical identities belong globally to AB

The fifty optical rows decompose in canonical order as:

- OPT1--OPT14: endpoint reserves, monotonicity, scaling, and common-face
  implications;
- OPT15--OPT26: twelve angular odd-sum blocks;
- OPT27: the radial equality-owner convention;
- OPT28--OPT32: five general product-deficit facts;
- OPT33--OPT50: eighteen sampled product expansions.

Packet E proves consequences of all fifty rows, but OPT15--OPT50 are the
36 repeated/general identities assigned globally to AB. Packet E's unique
global allocation is therefore

\[
U1\text{--}U8\quad\cup\quad OPT1\text{--}OPT14,
\]

which has \(8+14=22\) rows. Again, the broader proof scope does not create
a row-ownership collision.

## Disjointness and exhaustiveness calculation

I represented every canonical row by the pair
\((\text{family ID},\text{row number})\), built the six owner sets from
the ranges above, and compared them with the full universe.

The independent set audit returned:

    PASS: exact global ownership partition
    AB: 278
    C: 83
    D: 57
    E: 22
    F: 68
    main-visible: 103
    pairwise intersections: 0 across 15 owner pairs
    union: 611 unallocated: 0 extra: 0
    core: 553 supplemental: 58
    special: SUP36-SUP45 -> D; SUP58 -> main-visible; OPT15-OPT50 -> AB

In particular:

\[
\left|\bigcup_{\text{owners}}A_{\text{owner}}\right|=611,
\qquad
A_i\cap A_j=\varnothing\quad(i\ne j).
\]

Since the union equals the canonical 611-row universe, both the unallocated
set and the extra/noncanonical set are empty.

## Canonical corroboration

The standalone exact checker was replayed after the packet audits. It
reported:

    PASS
    first issue: none
    core exact finite checks: 553
    core substantive checks: 488
    core bookkeeping identities: 65
    supplemental exact checks: 58
    combined registry rows: 611
    canonical registry sha256: afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1

This replay authenticates the baseline row universe and ordering. It is not
a premise of the analytic packet proofs.

## Final conclusion

**PASS.** The completed analytic packets and main-visible consolidation
cover every one of the 611 exact-ledger predicates. After the three explicit
global ownership choices, the allocation is pairwise disjoint, sums to 611,
and leaves neither an unallocated row nor a multiply counted executable
row. No packet proof required modification during this global audit.
