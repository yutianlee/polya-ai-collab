# Analytic support bundle audit

**Result: PASS**

Audit date: 16 July 2026 (Asia/Shanghai)

Scope:

- master source: `manuscript/spherical-shell-polya-analytic-supplement.tex`
- release candidate: `tmp/analytic-support-build/spherical-shell-polya-analytic-supplement.pdf`
- all 14 PDFs included from `manuscript/analytic/compiled`
- correspondence of every included PDF to the current LaTeX source
- order, page inclusion, table of contents/bookmarks, global 611-row census, compilation, metadata, and rendered-page appearance

The candidate was cleared for exact-byte promotion. The older PDF previously present at
`manuscript/spherical-shell-polya-analytic-supplement.pdf` was not used as the release
candidate; after this audit, the candidate was promoted there and to the output folder.
Both promoted copies have SHA-256
`B055CC4EB52F7C6A4704587300B95A6645B0BD359E3B8EB34A52B15695267E60`.

## Frozen master artifacts

| artifact | bytes | SHA-256 |
|---|---:|---|
| master source | 5,569 | `D9C607269B50AA59CF6F18695B8A0F832ECB64E32F265876C9D02790B2983465` |
| audited release-candidate PDF | 925,400 | `B055CC4EB52F7C6A4704587300B95A6645B0BD359E3B8EB34A52B15695267E60` |

An independent Tectonic build of the frozen source exited with code 0, produced 79
pages, and had no final-pass undefined-reference, missing-file, overfull-box,
underfull-box, or LaTeX/package warnings. The independent build and the release
candidate have identical normalized extracted text on all 79 pages. Their binary
hashes need not agree because PDF creation metadata is regenerated; the independent
build's SHA-256 was
`7D3D194B259286DE895CED5C10552DBD7B15237153138D22AEC9EE522F8FDADF`.

## Included exhibits and source correspondence

Every included file exists. Each of the 14 current sources was compiled independently;
all 14 builds exited successfully. For every exhibit, normalized text in the included
PDF equals normalized text in the independent build from the listed source, page for
page. The master candidate also reproduces every included page exactly in normalized
text. Thus `pages=-` includes 77 exhibit pages, preceded by exactly two master front
matter pages, for a 79-page bundle.

| part | bundle pages | source SHA-256 | included PDF SHA-256 | source/PDF result |
|---:|---:|---|---|---|
| I, `ledger-main-visible`, 7 pp. | 3--9 | `8FFB175AC4E3FFE8F4A8A89BECB3B6A070DA4BABC08757F045DEB758722F45F5` | `086CECB7B6C09B56723F15BBDC318E15FEA7541CB8745B870621075CE8CCA0E4` | PASS |
| II, `ledger-packets-AB`, 9 pp. | 10--18 | `B5D21260D757D299ACB22EF3A0FD26D3A95A88AE3B0365988E5CBECD787EB6A6` | `D8555026D813274C518DD2FFC97299D645775B04FA5162ED1BDDF402E7087CA3` | PASS |
| III, `ledger-packet-C`, 7 pp. | 19--25 | `131A0F84C5CD38881487DC6AA410401B068E824EE855652281A1A61756BFC776` | `60D4D0817A5B74542AF78F85A2D7AC9ECD1B82FC68877D3BECB1C8142B39E21F` | PASS |
| IV, `ledger-packet-D`, 6 pp. | 26--31 | `17A08B124A6AE81B516E235046DB3ACCD4E7EDDC1C2A7CF6828FF87D6F3B7EBC` | `2C9E31053BB2AAD03AC70B3BDA29BA474D5D0F532806C6A6BCC0E1A0ABB65C44` | PASS |
| V, `ledger-packet-E`, 5 pp. | 32--36 | `03259745FBF8D67930045B4F996DDF9F61A2F5A74E72CF7A95064351E59A6123` | `58AAD400B7A4DF7838661AE1B6083D33FF95606F68A3B0D88BFA276D6E99E54C` | PASS |
| VI, `ledger-packet-F`, 3 pp. | 37--39 | `B137FDE7B974F55DD8EFD7D90501611939F291CAC80437C6F707C3CBC483E26E` | `ECACB63655872FCB5490BC6FCA810F24CA6421CDA66EA5B7F2EE095CFEF4AC8B` | PASS |
| VII, `compact-structural`, 6 pp. | 40--45 | `C236816E12266D055F144CF7EC9B2AEB352CB985EE3730D19F4AA850925606A7` | `23DC875354C0C167B30A1EA124A96B91953ACB56A9A561A155CE0C522872EB33` | PASS |
| VIII, `compact-angular-block`, 6 pp. | 46--51 | `8288FE0EAFEB8D8CFE9A10749E6BA470124408E3DC9FBBF1BE24BBB023C6DB49` | `0E3D0FA03942CE76D9D8DCEEA4391D46724F61C9FE482E0842836208F2A5D2B0` | PASS |
| IX, `compact-scalar-positive`, 8 pp. | 52--59 | `10CD0E5D6DDE5ECD7CFA2B2C64E47368E10E44093A407C04F74E29BB71807BA1` | `1216BE3583C810E39D7DFDE170BF0302C7649469158251B4E30C929328D754D4` | PASS |
| X, `F-positive`, 4 pp. | 60--63 | `D2305C221D89D2275A11B02F590A15FCA36EBE78AAD98DDBF5334FF41BDA064A` | `A0849F98466A0591E4DB9E7CCEC229C69DA800E86662581801F397394ED51D1D` | PASS |
| XI, `BK-positive-standalone`, 3 pp. | 64--66 | `FDEB68A341CEA7654658601636E1266884AF4260D6EDB100039D4AD9A776E0CE` | `5F0386378693056FC63AC7121A570C893CE0CC7E6DE94A2D0D0005CADA623C98` | PASS |
| XII, `B-positive`, 6 pp. | 67--72 | `70222FE3523B3F71384ADF22E2751BE1390498AE6554A8875984330DCBF67808` | `CC953C664640770CAE4B5D4867117CE9263FDE3D5817C40C38D01FDFF3D546F7` | PASS |
| XIII, `aggregate-tail-analytic`, 5 pp. | 73--77 | `B59D673E117611C81BABE4F8D7FE34AD0AFDFEF84BF2D8424128DE606F9C0BC9` | `DDEA00FD64AD90EAB12CEA6765F9431C93CBF2EF61B0B77AF10C8D679F8B2DD2` | PASS |
| XIV, `final-analytic-closure`, 2 pp. | 78--79 | `568E123178817DE1814095C719B5D7BCE90CFE3AFC48FEC6F97581D6AFAD6DC4` | `8A20C5B88C76564FC19C9640697D9C72271874DC0100BE40307898E9B91DA833` | PASS |

Part XI's standalone wrapper inputs `BK-positive.tex`; that included source was also
frozen at SHA-256
`F303CD9659789391DAABDF2821B16DE99B04BA47D767996B8ECCFCAA9F4D6F03`.

Two corrections were explicitly checked in the compiled exhibits:

- Part I has the current title “Hand-visible analytic derivations for 103
  finite-ledger predicates” and correctly refers to the “other five ledger packets.”
- Part IV is the corrected packet D: it states `S <= S_*`, permits equality when
  `m=0`, and retains the downstream strict premise `P^2 < H(P,r)`. Its included PDF
  is text-identical to a fresh build of the corrected source hash listed above.

## Architecture and claim audit

The order in the master is logically consistent with the abstract:

1. Parts I--VI discharge the finite exact ledger.
2. Parts VII--IX proceed from the compact retained-remainder identity, through the
   angular-block estimate, to scalar positivity.
3. Parts X--XIII proceed from the aggregate curvature floor, through the base
   derivative and base reserve, to the aggregate-tail theorem.
4. Part XIV uses those retained-remainder and aggregate inputs to close the final
   residual.

The source declares exactly 14 `\includepdf[pages=-]` entries in this order. The
candidate's page-by-page comparison confirms that there are no omitted, duplicated,
or reordered exhibit pages.

## Independent 611-row census check

The family sizes reconstruct the canonical total independently:

`PI 4 + TH 34 + SF 35 + Z 48 + LI 44 + KI 117 + CP 98 + LOC 47 + U 8 + OPT 50 + SUB 68 + SUP 58 = 611`.

The displayed ownership ranges reconstruct the six disjoint part totals:

- Part I: `TH(11) + Z(48) + LI(43) + SUP(1) = 103`.
- Part II: `PI(4) + TH(23) + SF(35) + LI(1) + KI(117) + CP(62) + OPT(36) = 278`.
- Part III: `CP(36) + LOC(47) = 83`.
- Part IV: `SUP(57) = 57`.
- Part V: `U(8) + OPT(14) = 22`.
- Part VI: `SUB(68) = 68`.

Hence `103 + 278 + 83 + 57 + 22 + 68 = 611`. The core families through SUB total
553 and SUP contributes the stated 58 supplemental rows. The three potentially
ambiguous redundancies are resolved consistently in the prose and table: SUP36--SUP45
belong to IV, SUP58 belongs to I, and OPT15--OPT50 belong to II. CP's “remaining
rows” expands to CP44--CP55, CP57--CP59, and CP78--CP98, exactly the 36 rows owned
by III. No gap or overlap remains.

## PDF structure, metadata, and visual inspection

PDF inspection reported:

- 79 pages, A4 (`595.28 x 841.89 pt`), rotation 0
- PDF 1.5, unencrypted, no JavaScript or forms
- title: “Purely Analytic Supplement for the Dirichlet Polya Inequality on
  Three-Dimensional Spherical Shells”
- subject: “Hand-checkable analytic estimates and finite exact tables”
- creator: LaTeX with hyperref; producer: xdvipdfmx

The bookmark destinations are correct: census page 1; Parts I--XIV begin on pages
3, 10, 19, 26, 32, 37, 40, 46, 52, 60, 64, 67, 73, and 78 respectively. These
destinations agree with the visible table of contents and the measured exhibit
boundaries.

Rendered visual checks covered pages 1, 2, 3, 10, 19, 26, 32, 37, 40, 46, 52, 60,
64, 67, 73, 78, and 79: the census, table of contents, every part boundary, and the
final page. No clipping, overlap, malformed table row, missing title, wrong page
orientation, or unreadable formula was observed.

## Conclusion

The audited candidate is internally complete and correctly assembled. All 14
included PDFs correspond to the latest audited sources, the corrected D packet and
current Part I wording are present, the 611-row allocation is exhaustive and
disjoint, compilation is clean, the declared logical order is respected, and the
rendered 79-page PDF has no observed assembly or layout defect. **PASS.**
