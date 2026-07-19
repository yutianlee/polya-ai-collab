# Audit of `ledger-main-visible.tex`

## Verdict

**PASS.** The packet accounts for exactly 103 uniquely allocated predicates:

| family | source rows allocated here | count |
|---|---|---:|
| `verify_thresholds` | 1–7 and 31–34 | 11 |
| `verify_zero_specializations` | 1–48 | 48 |
| `verify_lower_inventories_and_payments` | 1–8 and 10–44 | 43 |
| supplemental cap–74 incompatibility | one row | 1 |
| **total** |  | **103** |

There is no overlap with Packet B's threshold rows 8–30 or Packet A's
single lower-inventory row 9. No executable result is used as a proof
premise.

## Four-source comparison

The following files were compared:

- main paper: `manuscript/spherical-shell-polya-proof.tex`;
- supplement S1: `manuscript/spherical-shell-polya-supplement.tex`;
- canonical verifier: `computations/certification/verify_analytic_ledgers.py`;
- inventory: `manuscript/analytic/exact-ledger-inventory.md`.

The Python listing embedded in S1 was extracted from the first
`"""Standalone exact-rational verifier` through the end of its listing and
compared with the canonical verifier after normalizing only the surrounding
LaTeX listing markers. The source texts are identical.

The inventory gives 34 threshold rows, 48 zero rows, and 44 lower rows. The
allocation removes threshold rows 8–30 (23 rows) and lower row 9 (one row):

```text
34 - 23 = 11
48      = 48
44 -  1 = 43
11 + 48 + 43 + 1 = 103
```

### Hand-proof versus assertion classification

| allocated subfamily | count | status in the main paper before this packet | packet action |
|---|---:|---|---|
| ratio chain | 5 | hand-proved explicitly | records one-to-one IDs T1–T5 |
| `omega_0 < rho_c`, `omega_0 d > 1` | 2 | hand-proved, one implication compressed | prints all rational witnesses |
| four terminal omega comparisons | 4 | hand-proved across the lower-closure argument | consolidates them as T8–T11 |
| eight internal zero faces, five predicates each | 40 | hand-supported by the sign/count table and rational comparisons; recurrence arithmetic compressed | prints 16 exact location margins, 16 half-period signs, and 8 rational-wall sign certificates |
| Lorch specializations | 3 | hand-proved by printed positive-side squaring residuals | reproduces all three residuals |
| signs at the three Lorch walls | 3 | not separately proved as sign computations; logically implied by the strict first-zero bounds | makes the implication explicit |
| two rational wall orders | 2 | hand-proved | prints exact differences |
| lower activation/exclusion rows | 8 | hand-proved in the inventory argument, with arithmetic partly inline | prints every exact residual |
| five lower Weyl payments | 5 | hand-proved by five printed reserves | reproduces the reserve calculation |
| cap 395, fifteen proxies, tail, payment | 18 | hand-proved; all caps and positive numerators printed | supplies the cleared-denominator formula and one-to-one IDs |
| floor and endpoint rows | 12 | generated from a general hand argument, not printed as twelve separate rows | proves the general identity and maps all instances |
| cap–74 incompatibility | 1 | hand-proved exactly in the main paper and reported in S1 | reproduces `227/300` directly |

**Conclusion:** none of the 103 predicates is a logically unsupported
executable-only assertion. The visibility defects were compression and lack
of one-to-one row naming, not missing mathematics. The packet repairs those
presentation defects.

## Exact-arithmetic replay

An independent `fractions.Fraction` replay (separate from the canonical
verifier's interval implementation) checked every displayed residual. Its
result was:

```text
INDEPENDENT EXACT-ARITHMETIC REPLAY: PASS
(103-row census; all displayed residuals exact)
```

The checked threshold witnesses include

```text
3*1101^2*113^2 - 607^2*355^2 = 1998482
25*333^2 - 243*106^2         = 41877
2*32^2 - 45^2                = 23
400*337 - 367^2              = 111
1600*114 - 367^2             = 47711
```

The eight pairs of strict half-period location margins are

```text
(99/70, 163/1060), (8/7, 45/106),
(61/70, 737/1060), (23/70, 1311/1060),
(15/14, 105/212), (6/5, 97/265),
(4/7, 211/212), (1/2, 113/106).
```

The four nontrivial rational-wall comparison gaps are

```text
2583663/93822700
110529450419/2014895406650
415198510/530601061
3837851856583/53355906187500
```

The half-period polynomial endpoint witnesses replay as

```text
C5(144) = -6561
A5(182) = 421365
C6(81)  = -46116
A6(110) = 700645
A7(110) = -5878565
C7(144) = -2492559
```

The Lorch squared residuals replay as

```text
35171, 6939644, 767579.
```

The five Weyl reserves replay exactly as

```text
2908/539, 6199/539, 990435/137984, 555/44, 159/44.
```

All fifteen proxy numerators are positive and equal, in order, to

```text
14697882, 5409422, 11827162, 3611502, 8555642,
1604782, 5267322, 8361062, 2346202, 4446342,
176282, 1474822, 2444562, 3133502, 286642.
```

The weighted proxy cap and exceptional payment replay as

```text
sum_{ell=0}^{13} (2*ell+1)c_ell = 395
160293325/378004 - 395 = 10981745/378004 > 0.
```

Finally,

```text
2409/100 - 70/3 = 227/300 > 0.
```

## Canonical verifier corroboration

The canonical verifier was run only as a consistency check, not as a
mathematical premise. It reported:

```text
PASS
first issue: none
core exact finite checks: 553
core substantive checks: 488
core bookkeeping identities: 65
supplemental exact checks: 58
combined registry rows: 611
canonical registry sha256:
afd7e054f52aa9a3992fc8ef16d3e7551586c76bfb589053714f5f55a36792f1
```

## LaTeX build

`manuscript/analytic/ledger-main-visible.tex` compiled successfully with the
bundled Tectonic engine to a seven-page PDF:
`manuscript/analytic/ledger-main-visible.pdf`. There are no undefined
references and no overfull boxes. The only remaining diagnostics are two
harmless underfull-box warnings inside long table cells.

No edit was made to the main manuscript or S1.
