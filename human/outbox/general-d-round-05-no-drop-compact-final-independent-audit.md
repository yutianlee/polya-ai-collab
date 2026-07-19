# General dimension, Round 5 low-floor no-drop: final independent audit - FINAL PASS

Date: 18 July 2026

Status: **FINAL PASS**.

This audit covers the final reproducibility-preserving split of the compact
low-floor no-drop certificate. It does not edit or replace the frozen shared
core used by the completed \(f\geq4\) replay. No source, proof note,
manuscript, canonical log, or prior audit was edited.

## 1. Frozen low-floor snapshot

The three principal files have the expected identities:

| artifact | bytes | SHA-256 |
|---|---:|---|
| `scripts/general_d_no_drop_low_floor_final_verify.py` | 33,512 | `4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F` |
| `scripts/general_d_no_drop_compact_verify.py` | 33,458 | `EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE` |
| `human/outbox/general-d-round-05-no-drop-compact.md` | 14,602 | `44304F58E3B61FE1B75AEDC0D764800385AC3C0B905E60F1A3792D97DBCE9BE5` |

Both Python sources compile in memory. Each source has 1,012 lines and
contains no NUL, carriage return, form feed, or U+FFFD replacement
character. The proof note has no such malformed byte either.

## 2. Exact source split and executed-image identity

An independent unified diff has exactly two hunks, two removed lines, and
two added lines. Both hunks replace

```python
f == 2 and n >= 8 and box.phase in {"lower", "open"}
```

by

```python
((f == 2 and n >= 8) or (f == 3 and n >= 7)) and box.phase in {"lower", "open"}
```

The first occurrence selects the exact positive-series endpoint-root
enclosure. The second selects the exact positive-series \(A(r)\)
enclosure. No root equation, phase convention, pruning test, scalar,
precision, panel count, depth limit, or box cap changed.

The byte-level checks are exact:

- the old predicate occurs exactly twice in the shared core and zero times
  in the final low-floor file;
- the new predicate occurs exactly twice in the final low-floor file and
  zero times in the shared core;
- replacing those two old strings in memory adds exactly 54 bytes and
  reproduces the complete 33,512-byte low-floor file byte for byte;
- the transformed bytes hash to `4AD4...9319F`;
- reversing the two replacements reproduces the complete shared core and
  its `EEF8150...ACCDE` hash byte for byte.

The retained \(f=3\) shard driver has SHA-256
`9BF44A486123C4DE1FA029B46B74ED8D0EADEE3ACB76EFEAE170B892612CA1A3`.
It reads the frozen shared core, requires exactly two old predicates,
performs exactly the replacements above, requires the resulting
`4AD4...9319F` hash, compiles that image, and only then executes it. Loading
that runtime module independently succeeded and reported the pinned
settings

\[
 \text{root steps}=12,\quad \text{panels}=4,\quad
 \text{angle steps}=32,\quad \text{depth}=72,\quad
 \text{box cap}=500000.
\]

Because the independently transformed bytes equal the checked-in final
file, the full \(f=3\) replay executed exactly the current low-floor source
image, not merely a mathematically similar patch.

For \(f=2\), the added disjunct \(f=3\land n\ge7\) is identically false.
I evaluated both predicates on every

\[
 (n,\mathrm{phase})\in
 \{2,\ldots,379\}\times\{\mathrm{corner},\mathrm{lower},\mathrm{open}\},
\]

all 1,134 combinations, and found zero truth-value mismatches. Algebraically
the equality holds for every integer \(n\) and every phase, not just the
enumerated range. Since the two predicate lines are the only byte changes,
the old and new files execute the same \(f=2\) arithmetic branches.

Two direct behavioral controls agree byte for byte between the old and new
paths:

- \((f,n)=(2,379)\), all three phases: 3 boxes, depth 0, identical stdout
  SHA-256 `DC7DD40B4DEF04EEFF65362993D5F740F09652D4DF9736635C455B2A384832CC`;
- the exceptional \((f,n,\mathrm{phase})=(2,8,\mathrm{open})\) series path:
  49,909 boxes, zero positive leaves, depth 17, identical stdout SHA-256
  `19085FC38536D974762D25BA4EE01C1FB7DE2AE20FFD11E84E156B13709F3CEF`.

All four processes exited 0 with empty stderr.

## 3. Proof and implementation logic

### Compact coordinates and root domain

The code and note consistently use

\[
 \sigma=\sqrt{\frac{K-\mu}{K}},\qquad
 \kappa=\sigma(K-\mu)=\sigma^3K,
\]

\[
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3},\qquad
 q=\mu-\alpha,\qquad r=q-n.
\]

On an endpoint wall, \(A(q)=f-1/4\). The endpoint-action estimates put
every compatible root inside

\[
 \frac{21}{8}\leq\kappa\leq
 \begin{cases}66/7,&f=2,\\99/7,&f=3.\end{cases}
\]

The lower \(\sigma\)-bisection uses the failed strict root-free cutoff and
keeps its last excluded endpoint in the retained interval. The upper
bisection uses \(\mu\ge n+1/2\) and likewise retains the first impossible
endpoint. For \(n>48\), intersecting with \(\sigma<38/n\) keeps equality in
the interval and therefore cannot introduce a gap.

### Strict phase semantics

The phase functions in the source exactly implement

\[
\begin{array}{c|c|c|c}
\text{phase}&\alpha&Q&\text{retained ball levels}\\ \hline
\text{corner}&0&f-1&f-1\\
\text{lower}&0<\alpha<1&f-1&f\\
\text{open}&0\leq\alpha<1&f&f.
\end{array}
\]

The lower wall has \(A(q)+1/4=f\); the open chamber is reduced to that wall
while retaining its open-side counts. Closed interval endpoints
\(\alpha=0,1\) are one-sided limits, while the corner is a separate call.
Thus no equality level is assigned the combinatorics from the wrong side.

At fixed \((\mu,r)\), lowering \(K\) decreases the full scalar because
\(\partial_K\mathscr S_n>0\). The first shell wall met is the lower wall at
\(q\). If \(\sigma=1/10\) is met first, the analytic transfer applies.
The open-to-wall reduction therefore loses no possible negative point.

### Directed root and action enclosures

For the ordinary path, the scaled action profile is concave. Composite
trapezoids are directed lower bounds and composite midpoint rules are
directed upper bounds. Root bisection advances only after a universal
directed sign; otherwise it returns a split. The corner eliminates
\(\kappa\) exactly through the stable half-angle identity.

For the exceptional path, the positive series for
\(G_R(R-\mathrm{gap})\) has positive decreasing coefficients and
\(x<1/2\). The first omitted term divided by \(1-\overline x\) bounds the
tail. Exact-zero gap hulls are intersected with the analytically known
nonnegative half-line before a square root. The two changed predicates only
route the same exact shell action through this better enclosure.

Every early terminal return negates a strict necessary condition in the
safe direction: physicality, cutoff, active width, upper/slope/width
geometry, central and outer geometry, endpoint floor/phase, or the audited
shelf-curvature criterion. The exact head and independent curvature head
are combined by taking the larger directed lower endpoint. The angle sum is
evaluated in the lower-payment direction at \(\underline K\), while the
inner cap is subtracted using an upper enclosure. A leaf passes only when
the final outward Arb lower endpoint is strictly positive.

An unresolved box is subdivided. More than 500,000 processed boxes or depth
72 raises an assertion and reaches `CERTIFICATE FAILURE`; neither condition
can be printed as a pass.

## 4. Analytic dependencies and complete low-floor scope

The earlier Round 5 dependency files remain:

| artifact | SHA-256 |
|---|---|
| analytic/cutoff note | `E0AC849A4280718EB9CB13C912CA10AA3EB34BC5F9A2EE68C2094B9A09E6A9C8` |
| independent analytic audit | `3208940D7DA40F43C0F80BCDBF8956A1DF159231E4FDC3A9E3F20F7C267F59B3` |
| Arb constants verifier | `E13D2B6EA0B7D11C2BC800DAF55F1E45A599B247BAD19658655F2B9B12F53574` |

A fresh run of the constants verifier exited 0 with empty stderr at 512
bits and certified the strict \(\sigma\le1/10\) margin. Its stdout SHA-256
was `CCCC7A4F9D945ED3F5E09E7FFBCD7ED6824EC786F0366D7A223C3854AE35057D`.

The dependency chain has no uncovered boundary:

- \(n=1\) is closed directly: concavity gives \(R_1\ge-1/2\), while the
  strict terminal reserve gives \(D_A(q)>1/2\), including \(q=\mu\);
- for \(2\le n\le379\), the analytic theorem covers
  \(\sigma\le1/10\) and the interval certificate covers
  \(\sigma\ge1/10\), so equality is covered by both;
- the strict estimate \(\sigma<38/n\) implies
  \(\sigma<1/10\) when \(n\ge380\), so the analytic theorem closes every
  such case.

These facts combine the finite ledger below with the analytic pieces to
cover the complete \(f=2,3\) no-drop sector and no larger claim.

## 5. Independent parse of the retained \(f=3\) evidence

The aggregate parser has SHA-256
`331A4F13B737CF26864841D8F55BA6F6CC64C94DD368014640ACC532642DAF8E`.
I ran it and also wrote an independent in-memory parser rather than relying
on its totals.

The nine selected log slices are:

| log | selected \(n\) | bytes | SHA-256 |
|---|---:|---:|---|
| `f3-002-026.log` | 2-26 | 8,627 | `BAB05861947D218B7BF775980C119D133805758F15446AAD640AD86EC0D0E5C2` |
| `f3-027-101.log` | 27-36 | 3,401 | `657D5C4D9CA02855A7FBA66E6B32161B0F9C360BFCC5DE7ABF091A41F3CCACEF` |
| `f3-037-058.log` | 37-42 | 2,129 | `EDDB93E4B723767F230CA9CBB6BD94626D06A87A581284AFA52521E6063BDCB1` |
| `f3-043-050.log` | 43-50 | 3,170 | `CE9271A1B49FE7E0E3DC9D2C3642339B19EC86FAAAA16302EE98BAEAFA56ABAE` |
| `f3-051-058.log` | 51-58 | 3,162 | `8887E618D8DC55A045A74D11608E0B9169098FA9D026381C7EC72571EB0FF577` |
| `f3-059-080.log` | 59-80 | 7,336 | `459454FA3B608F3928F099C6CA5A11D82CFBA05573DB90A0B2D69BACBEA48CC3` |
| `f3-081-101.log` | 81-101 | 6,850 | `420851AA95B0D810005A05C5F1F4CC627A6610F6BA00B35E7FB0A75A2E4A97E2` |
| `f3-102-240.log` | 102-240 | 42,054 | `82ECD61B50EB60C33A555AB6BD9E532513FBF5247813D96ABA36F1A7A92B61D8` |
| `f3-241-379.log` | 241-379 | 40,712 | `104C8E8A3D7FC8CFF845CC6E76AF63B817DF9A677F5D6A717740F8024030558D` |

Every `START` line pins the `4AD4...9319F` runtime, precision 512, and the
same \(12/4/32/72/500000\) settings. The selected logs contain exactly
1,134 `CASE` lines, zero duplicate keys, zero missing keys, zero extra keys,
and zero `FAIL` or `CERTIFICATE FAILURE` lines. All nine stderr logs exist,
are empty, and have SHA-256
`E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`.

Each row satisfies

\[
 \mathrm{boxes}=2(\mathrm{positive}+\mathrm{pruned})-1.
\]

A positive row has a finite strictly positive minimum; a zero-positive row
has the literal `inf`. The largest individual case has 84,411 boxes, and
the maximum depth is 23, both strictly below the pinned limits. Thus no
selected case hides an unresolved, capped, or depth-exhausted leaf.

The independently reconstructed ledger is:

| phase | cases | boxes | positive | pruned | depth | minimum positive |
|---|---:|---:|---:|---:|---:|---:|
| corner | 378 | 133,152 | 5,374 | 61,391 | 13 | `0.0012020968532512127` |
| lower | 378 | 4,422,822 | 2,521 | 2,209,079 | 23 | `0.00030504252056230637` |
| open | 378 | 3,139,208 | 3,026 | 1,566,767 | 23 | `0.00024999770759192934` |
| total | 1,134 | 7,695,182 | 10,921 | 3,837,237 | 23 | `0.00024999770759192934` |

For additional reproducibility, the audit-defined normalized selected-row
digest is
`15F54D07FCF63BEB116AB1EED763F92CB34EBDFAE06056904D34D432927FEF44`,
and the ordered nine-log hash-list digest is
`0C49067FC9EB521E86871CF9696995FA1A77C0046826EEC9182A985FD7E81A40`.

Two shard files were interrupted after their final selected complete
`CASE` line and therefore have no shard `PASS` footer. This is not a hidden
case failure: the driver emits a `CASE` line only after `verify_case`
returns with an empty queue, the selected coverage is exact, the forest
identity holds, no failure line exists, and stderr is empty. This provenance
is stated rather than silently treating partial job files as full-shard
transcripts.

## 6. Reconstruction of the prior \(f=2\) disjoint ledger

The completed \(f=2\) execution used the frozen `EEF8150...ACCDE` source at
384 bits. As proved in Section 2, every \(f=2\) branch is byte-for-byte
unchanged in the final low-floor image. I independently expanded the eleven
retained checkpoint domains into keys and checked their arithmetic:

| checkpoint | cases | boxes | positive | depth | minimum reported positive |
|---|---:|---:|---:|---:|---:|
| \(n=2\ldots26\) | 75 | 5,700,618 | 20,687 | 31 | `1.7050400932319067e-06` |
| middle prefix | 25 | 1,969,499 | 3,995 | 21 | `6.2878459916e-05` |
| M1 | 50 | 3,658,642 | 3,468 | 23 | `7.4494561070e-04` |
| M2 | 50 | 2,617,260 | 1,157 | 23 | `3.4842773862e-03` |
| M3 | 50 | 1,799,328 | 16 | 23 | `12.1802306815` |
| M4 | 50 | 2,547,464 | 0 | 24 | `inf` |
| high prefix | 25 | 933,321 | 0 | 24 | `inf` |
| R1 | 203 | 405,129 | 0 | 16 | `inf` |
| R2 | 204 | 163,694 | 0 | 11 | `inf` |
| R3 | 201 | 77,125 | 0 | 10 | `inf` |
| R4 | 201 | 15,069 | 0 | 8 | `inf` |
| total | 1,134 | 19,887,149 | 29,323 | 31 | `1.7050400932319067e-06` |

The domains are pairwise disjoint and their union is exactly
\(\{2,\ldots,379\}\times\{\mathrm{corner},\mathrm{lower},\mathrm{open}\}\).
There are no missing or extra keys. The audit-defined key-coverage SHA-256
is `73A0C41ADADE6B2BF1B6466ACF999720350237CDA39F5185A4999D5EC18F66F5`.

The retained checkpoint summaries all completed with pass status; the
source raises rather than returns a result on any cap or unresolved depth.
Their maximum recorded depth is 31, far below 72, and the proof note records
that no case reached 500,000 boxes. Thus the prior completed execution has
no unresolved, cap, depth, or failure disposition.

Unlike \(f=3\), a complete raw per-case \(f=2\) log and phase split were not
retained. This audit therefore verifies the disjoint key partition, every
checkpoint sum, the exact aggregate arithmetic, the executed-source
transfer, and direct representative old/new runs; it does not claim to have
reparsed nonexistent raw \(f=2\) leaf rows. This is the material evidence-
provenance limitation of the final low-floor certificate.

## 7. Exact combined finite ledger

The two floors give

\[
 1134+1134=2268\quad\text{cases},
\]

\[
 19887149+7695182=27582331\quad\text{boxes},
\]

\[
 29323+10921=40244\quad\text{positive leaves}.
\]

The overall maximum depth is 31 and the smallest reported positive
diagnostic is

\[
 1.7050400932319067\times10^{-6}.
\]

Printed decimal minima are diagnostics only. Every proof acceptance was a
strict positive outward Arb lower endpoint.

The final source was not rerun as one monolithic 2,268-case job. Its proof
evidence is deliberately composite: the \(f=2\) completed disjoint
checkpoints transfer through exact Boolean/source equivalence, while the
\(f=3\) logs executed the exact current source image. This split preserves
both reproducibility and the already accepted high-floor pins.

## 8. Direct preservation of the \(f\geq4\) replay

The high-floor import chain still points to
`scripts/general_d_no_drop_compact_verify.py` and pins
`EEF8150...ACCDE`; it does not import the new low-floor path. The accepted
aggregate checker remains

`scripts/_aggregate_general_d_no_drop_high_floor_shards.py`

with SHA-256
`79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996`.

A fresh unmodified checker run exited 0 with empty stderr and stdout SHA-256
`682091821787EC985085DE42C09BD48EEDDD2AB1ABA8FB7B14075CAAD1DD593C`.
It again certified

\[
 \boxed{610\ \text{pairs},\quad1830\ \text{phase rows}},
\]

with 8,232,800 boxes, 22,986 positive leaves, 4,176,374 pruned leaves,
depth 15, coverage digest
`B1C4A0B498CEFFBC211C2F1F6A8AC8F4D81164BA4B8C67E83E09B7FADED9AB01`,
and raw-log-set digest
`9515F61976AE9D594B3725829AE6C40011199379F41810F8EBFC38470DC32140`.

The durable aggregate log remains SHA-256
`2E11E13CA0C00C39E09171CEDEDD8D31C5D4314DF68D1958AF7A0553F6BD09C6`;
its stderr is the empty-file hash. The wrapper, shard launcher, and
exhaustion verifier remain, respectively,

`5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F`,

`A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092`,

`81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A`.

Thus the separate low-floor file preserves direct replay of the accepted
high-floor certificate without a renamed import or changed pin.

## 9. Reproduction commands run in this audit

The principal read-only commands were:

```text
python scripts/_aggregate_no_drop_f3_shards.py
python scripts/general_d_no_drop_round5_verify.py
python scripts/_aggregate_general_d_no_drop_high_floor_shards.py
python scripts/general_d_no_drop_compact_verify.py --f 2 --n 379 --precision 384
python scripts/general_d_no_drop_low_floor_final_verify.py --f 2 --n 379 --precision 384
python scripts/general_d_no_drop_compact_verify.py --f 2 --n 8 --phase open --precision 384
python scripts/general_d_no_drop_low_floor_final_verify.py --f 2 --n 8 --phase open --precision 384
python scripts/general_d_no_drop_low_floor_final_verify.py --f 3 --n 379 --precision 512
python scripts/_general_d_no_drop_f3_runtime_shard.py --n0 379 --n1 379 --precision 512
```

The first three commands produced:

| command | exit | stdout bytes | stdout SHA-256 | stderr bytes |
|---|---:|---:|---|---:|
| \(f=3\) aggregate | 0 | 2,578 | `3E576C85DB695E2A91C7927F761AE9A5D2A704C1B8B4AF57D21B729143ED1D44` | 0 |
| Round 5 analytic verifier | 0 | 1,492 | `CCCC7A4F9D945ED3F5E09E7FFBCD7ED6824EC786F0366D7A223C3854AE35057D` | 0 |
| \(f\ge4\) aggregate checker | 0 | 2,666 | `682091821787EC985085DE42C09BD48EEDDD2AB1ABA8FB7B14075CAAD1DD593C` | 0 |

All empty stderr streams have SHA-256
`E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`.

## 10. Preservation ledger

The Round 8G and general-d manuscript artifacts remain:

| artifact | SHA-256 |
|---|---|
| corrected Round 8G proof | `C45D339383FD4E6921C3C60D058E14628846DF57E7F7808D62B373AB2476DE90` |
| Round 8G verifier | `873D9E4259DC0827C8917EB8CD04C169303B8D973C332CD2A75DA5038FC19F34` |
| Round 8G proof audit | `203BC49B2F4E61B932D3CA6D2483D295729FCBDE830A813D8EC9DD3AB2AD38A7` |
| Round 8G manuscript audit | `834710A1D4F6BBD2DEC2A1CC1CF149F139A75BD952E13BE521CC73E09AF33532` |
| general-d manuscript source | `A525FA9FC2CB4DDB028369AC88701297A273525C11EE4102DB80D5F3A2D12126` |
| production general-d PDF | `AD56B0537542E5704B3A8041BEB93E3D4876F123CA9A41517170D635D9DB6595` |
| production general-d log | `80D59877E50DFA8533A6479EF8BA99A88274ECD36B45A6E304B3B12D2206A12F` |

The final high-floor note remains an \(f\geq4\)-only artifact. It is 22,171
bytes with SHA-256
`3E43416CFEDBD50B9B29DC57E4FC6A786BCAD9CD90E469C785A466262E8DAE63`.
An exact two-block comparison with its preceding 22,216-byte image changes
only the low-floor-audit status paragraph and the remaining-work list; no
high-floor proof or certificate datum changes.
The frozen high-floor final audit remains
`064BA541D96BF7B07AC60758E17FDE5E455A383B0CFC3E20E392308EF7258242`.
The accepted high-floor checker revalidated every canonical shard hash and
mandatory empty stderr file during the fresh 610/1,830 run.

The original dimension-three paper remains:

| artifact | SHA-256 |
|---|---|
| `manuscript/spherical-shell-polya-proof.tex` | `E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4` |
| `manuscript/spherical-shell-polya-proof.pdf` | `FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F` |

## 11. Verdict

**FINAL PASS.** The separate final low-floor source is exactly the
previously executed \(f=3\) image, has exactly the old \(f=2\) behavior,
and differs from the frozen shared core only at the two documented routing
predicates. The analytic dependencies, strict phase semantics, complete
1,134+1,134 finite coverage, exact aggregate arithmetic, termination
conditions, and direct \(f\geq4\) reproducibility all check. The evidence
provenance limitations are explicit and do not leave an uncovered
mathematical or discrete case.
