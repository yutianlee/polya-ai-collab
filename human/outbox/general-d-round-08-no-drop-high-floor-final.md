# General dimension, Round 8: final certificate for the high-floor no-drop sector

Date: 18 July 2026

Status: **FINAL PASS for the \(f\geq4\) no-drop sector.**  The mathematical
and interval-certificate architecture, the complete eight-shard replay, and
the hardened aggregate checker have all passed independent audit.  The final
audit report is
`general-d-round-08-no-drop-high-floor-final-independent-audit.md`, SHA-256

```text
064BA541D96BF7B07AC60758E17FDE5E455A383B0CFC3E20E392308EF7258242
```

This conclusion is deliberately narrow.  It proves positivity on the
no-drop branch for \(f\geq4\); it does not address the distinct high-floor
first-drop residual.  It also does not by itself complete the repository
integration of the already executed \(f=2,3\) low-floor certificate.  No
manuscript, original \(d=3\) artifact, verifier, checker, or canonical log is
changed by this note.

## 1. Certificate theorem and scope

Use the no-drop notation of the preceding rounds.  Thus \(p=n\), \(f\) is
the endpoint floor, \(n\) is the shelf length, and \(\mathscr S_n\) is the
shifted-tail scalar after the exact no-drop reduction.

**Theorem 1.1.**  Every residual no-drop configuration with

\[
 f\geq4,\qquad n\geq2
\]

has

\[
 \boxed{\mathscr S_n>0.}
\]

Together with the already completed direct \(n=1\) module, this closes the
entire \(f\geq4\) no-drop sector.

The proof has two exhaustive parts.  First, the outward-Arb exhaustion
certificate removes every integer pair except a finite set of 610 retained
pairs.  Second, the interval verifier covers all three strict one-sided
phase chambers of each retained pair.  Every terminal interval box either
violates a proved necessary condition or has a strictly positive outward
lower bound for \(\mathscr S_n\).  The exact ledger contains all
\(610\cdot3=1{,}830\) phase chambers, with no gap or duplicate.

## 2. Frozen proof boundary

The accepted proof chain is pinned to the following exact source images.

| artifact | bytes | SHA-256 |
|---|---:|---|
| `scripts/general_d_no_drop_exhaustion_verify.py` | 7,625 | `81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A` |
| `scripts/general_d_no_drop_compact_verify.py` | 33,458 | `EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE` |
| `scripts/general_d_no_drop_high_floor_compact_verify.py` | 19,447 | `5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F` |
| `scripts/_general_d_no_drop_high_floor_shard.py` | 5,370 | `A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092` |
| `scripts/_aggregate_general_d_no_drop_high_floor_shards.py` | 12,184 | `79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996` |

The mathematical architecture audit is frozen at

```text
human/outbox/general-d-round-08-no-drop-high-floor-independent-audit.md
FFD118B79A1078C5DE9BF44688501924738E41B3D5A9673BD8A0BF8D354926B8
```

and the repaired root-localization note is frozen at

```text
human/outbox/general-d-round-08-no-drop-high-floor-root-localization.md
752952059FE017BCF988E86A55F871AA9B240A8DE0C0FE26806A53F9656DD5E5
```

The final independent audit applies only to the accepted aggregate-checker
hash `79999E43...B7996`.  An earlier checker was rejected; none of its
outputs is used here.

## 3. Exact discrete exhaustion and strict phases

The high-floor wrapper replays the pinned exhaustion certificate before it
constructs a parameter box.  After restricting to \(f\geq4\) and \(n\geq2\),
the central and outer necessary lists satisfy

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]

and therefore

\[
 \boxed{\#(\mathcal C\cup\mathcal O)=610.}
\]

The first and last retained pairs are \((4,2)\) and \((49,48)\).  Every pair
outside this union is already excluded by the analytic central/outer
necessary conditions; the interval computation is required only on the
union.

Put

\[
 q=\mu-\alpha,\qquad
 r=q-n,\qquad
 b=f-\frac14,\qquad
 \varepsilon=A(q)+\frac14-f.
\]

The three phase calls retain their strict one-sided combinatorics:

| phase | strict chamber represented | shell count \(Q\) | terminal levels |
|---|---|---:|---:|
| corner | \(\alpha=0,\ \varepsilon=0\) | \(f-1\) | \(f-1\) |
| lower | \(0<\alpha<1,\ \varepsilon=0\) | \(f-1\) | \(f\) |
| open | \(0\leq\alpha<1,\ 0<\varepsilon<1/4\) | \(f\) | \(f\) |

The open chamber is reduced monotonically, at fixed \((\mu,r)\), to the
wall \(A(q)=b\), but it keeps \(Q=f\) and \(f\) strict-wall-safe terminal
levels.  The interval boxes use the closed hull \(0\leq\alpha\leq1\) only
as a one-sided enclosure.  They never replace the lower/open combinatorics
by corner combinatorics at an endpoint.  Thus equality faces cannot create
a missing strict-floor case.

## 4. Full \(\sigma\)-interval localization

Use the exact critical coordinates

\[
 \sigma=\sqrt{\frac{K-\mu}{K}},\qquad
 \kappa=\sigma(K-\mu),\qquad
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3}.
\]

There is no unproved small-\(\sigma\) transfer in this high-floor driver.
Every residual point satisfies the root-free condition

\[
 K<K_{\rm nd}(n,Q)
\]

and the universal lower endpoint bound \(\kappa\geq21/8\).  Since
\(\kappa=K\sigma^3\),

\[
 K_{\rm nd}(n,Q)\sigma^3>\kappa\geq\frac{21}{8}. \tag{4.1}
\]

Forty exact-rational bisections advance the lower endpoint only when the
Arb upper bound proves the strict reverse of (4.1).  The returned endpoint
\(s_0\) is retained on the already excluded cutoff side, so it gives overlap
rather than a gap.

At the upper end, the endpoint action estimate and \(\pi<22/7\) give

\[
 \kappa<\frac{3\pi f}{2}<\frac{33f}{7}=:\kappa_{\max}(f).
\]

Physicality \(r\geq1/2\) implies \(\mu\geq n+1/2\), so every residual point
must satisfy

\[
 \frac{33f}{7}\frac{1-\sigma^2}{\sigma^3}>n+\frac12. \tag{4.2}
\]

The function on the left is strictly decreasing on \(0<\sigma<1\).  Forty
directed rational bisections return the first point \(s_1\) at which the
Arb upper endpoint proves (4.2) impossible.  Retaining \(s_1\) again gives
overlap.  Hence the closed computational interval

\[
 [s_0,s_1]
\]

contains every possible residual point in the strict interval
\(0<\sigma<1\).  All 610 retained pairs have a nonempty interval in each
of the three phases.

The production grid divides this interval into 16 exact rational
\(\sigma\)-panels.  A corner has one \(\alpha=0\) root per panel; a lower or
open phase has eight exact rational \(\alpha\)-panels per \(\sigma\)-panel.
Thus the initial forest has 16 roots on a corner and 128 roots on each
lower/open phase.

## 5. Rigorous high-floor root enclosure

For lower and open phases the wall target is

\[
 T=f-\frac14.
\]

At fixed \((\sigma,\alpha)\), the noncancelling scaled integral proves that
the shell action \(A(q)\) is strictly increasing in \(\kappa\).  No
monotonicity in \(\sigma\) or \(\alpha\) is assumed.

The deterministic seed

\[
 \kappa_*(f)=\frac{13}{6}\left(f-\frac14\right)
\]

is not accepted on faith.  On every parameter box the verifier first
proves, with outward Arb arithmetic,

\[
 q(\kappa_*)>0,\qquad
 \overline A(q;\kappa_*)<T. \tag{5.1}
\]

Failure of (5.1) requests subdivision; it never discards a candidate.  The
full 384- and 512-bit seed audits cover

\[
 610\cdot2\cdot16\cdot8=156{,}160
\]

lower/open seed boxes.

Two independent rigorous enclosures of the same action are intersected:

1. the exact positive gap-series enclosure;
2. the noncancelling concave integral, with composite trapezoids below and
   composite midpoints above.

The verifier takes the larger lower endpoint and smaller upper endpoint.
If both representations fail, the box is split; if the intervals are
disjoint, the certificate fails.

Starting from \(\kappa_*\), twelve directed bisections advance a common lower
root endpoint only under

\[
 \overline A(m)<T.
\]

The reverse bisection retreats an upper endpoint only under

\[
 \underline A(m)>T.
\]

If the upper test at \(33f/7\) is inconclusive, that proved a priori ceiling
is retained.  If its action upper endpoint is below \(T\), monotonicity
proves that no root exists.  Every direction is therefore conservative.

At the corner, \(\alpha=0\) and \(q=\mu\).  The stable half-angle identity
eliminates \(\kappa\) directly, so no numerical root conjecture enters that
phase.

## 6. Necessary-condition prunes and the positive scalar

Write \(\delta=K-\mu=\kappa/\sigma\).  After root enclosure, each terminal
prune negates a strict necessary condition in a directed-safe direction.
Among the tested conditions are

\[
 \begin{gathered}
 r\geq\frac12,\qquad K<K_{\rm nd}(n,Q),\qquad
 \frac{\delta}{\pi}>b,\\
 K<\frac{2\delta^2(\delta+1)}{\pi^2b^2},\qquad
 K^2>b\,n(n+1),\\
 \frac{\delta}{\pi}<f+\frac14+\frac{r}{4n},\\
 A(r)<f+\frac14,\qquad A(r)+A(q)<2f.
 \end{gathered} \tag{6.1}
\]

The central branch \(r\leq K/2\) is excluded for \(n>48\).  On the outer
branch, the certified outer-width and outer-slope inequalities are tested
with the correct directed endpoints.  The shelf-curvature prune proves

\[
 2\varepsilon+\Delta+
 \frac{n\Delta}{3(2r+n)}\geq\frac{n-1}{2n},
 \qquad \Delta=A(r)-A(q),
\]

before discarding a box.  Failure to prove any exclusion returns an
unresolved split status, not a prune.

On a surviving box, let \(J_2(R,z)=2\int_z^R G_R(t)\,dt\).  The exact
gap-variable head is

\[
 H=J_2(K,r)-J_2(K,q)-J_2(\mu,r)+J_2(\mu,q)-2nf.
\]

It is intersected with the independent shelf-curvature lower bound.  If
\(\vartheta_k\) is defined by

\[
 \frac{K(\sin\vartheta_k-\vartheta_k\cos\vartheta_k)}{\pi}
 =k-\frac14,
\]

the terminal payment is bounded below by

\[
 T_{\rm term}=\sum_{k=1}^{L}\frac{\pi}{2\vartheta_k}
 -Q-\operatorname{cap},
\]

where \(L=f-1\) and the cap is zero at the corner, while \(L=f\) and the
inner cap is subtracted by an upper enclosure on lower/open phases.  The
angle calculation uses 32 directed bisections at a lower bound for \(K\).
A leaf is marked `positive` only after the Arb lower endpoint proves

\[
 \underline H+\underline T_{\rm term}>0. \tag{6.2}
\]

The positive gap series uses a directed geometric remainder with ratio
strictly below \(1/2\).  Nonnegative analytic gap variables are intersected
with the nonnegative half-line before square roots.  Printed decimals and
heap priorities have no proof role.

Every unresolved box is split in two.  Depth 72 and 500,000 processed boxes
per phase are hard failure caps, not tolerances.  The observed maximum depth
was 15, and no phase reached the box cap.

## 7. Deterministic shard partition

Order the 610 retained pairs lexicographically by ordinals
\(j=0,\ldots,609\), and assign ordinal \(j\) to shard \(j\bmod8\).  All
three phases of a pair remain together.  Shards 0 and 1 therefore contain
77 pairs and 231 phase rows each; shards 2 through 7 contain 76 pairs and
228 rows each.

The exact assignment hashes are:

| shard | assignment SHA-256 |
|---:|---|
| 0 | `E04792172F4F934D1E8DE823A7724D082C62C6A089092CDED9519AA4822A3D84` |
| 1 | `D975D89CCAF00D6EB84A9E401A2A97F26E90D16B6AE7B834A0F832FB9F526907` |
| 2 | `2DBBB8A4309429B2C1FE50AC6CE1247A10823DB8EC28A37090DBE8E712AA3F0D` |
| 3 | `95CF3BBD857142837A55D20200914CDFC172010B7F912BA6E74B6BC5E8FEE1E8` |
| 4 | `0F69BAFFB45C55E468FD3CB3CE3086A7139165420D21D15CDA83DE2851557449` |
| 5 | `A29C9D1E1C10550DA95245C2B2908D1DFA4FDDD2AB9BEFDC8CDA67625A870AFA` |
| 6 | `1F073B27CEA4819DC8FC25A8698CC77A25D8A3337341C961F1C8E396DF3A71C9` |
| 7 | `CA94BDFDA7CDDEE16F8AA8CD253742833D4B08FB95B2CAFA3BF8A31786B93EF9` |

For a nonempty full binary forest,

\[
 \text{boxes}=2(\text{positive}+\text{pruned})-I,
\]

where \(I=16\) for a corner and \(I=128\) for a lower/open phase.  The
checker verifies this identity separately for every row.  All 1,830 rows
are nonempty.

## 8. Exact eight-shard ledger

The completed shard totals are:

| shard | pairs | cases | boxes | positive | pruned | depth | smallest positive |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 77 | 231 | 1,032,534 | 3,506 | 523,233 | 15 | `2.144211613601797e-05` |
| 1 | 77 | 231 | 1,020,324 | 7,971 | 512,663 | 15 | `3.295220536637341e-05` |
| 2 | 76 | 228 | 1,030,748 | 3,563 | 522,147 | 15 | `4.803944338325024e-05` |
| 3 | 76 | 228 | 1,030,862 | 258 | 525,509 | 15 | `0.04178887764990063` |
| 4 | 76 | 228 | 1,028,332 | 1,201 | 523,301 | 15 | `0.001293689185865621` |
| 5 | 76 | 228 | 1,036,944 | 123 | 528,685 | 15 | `0.010374015346279027` |
| 6 | 76 | 228 | 1,013,068 | 3,377 | 513,493 | 15 | `0.0007232961617573032` |
| 7 | 76 | 228 | 1,039,988 | 2,987 | 527,343 | 15 | `0.00028010088421405915` |

Their exact coverage and raw stdout hashes are:

| shard | coverage SHA-256 | raw stdout SHA-256 |
|---:|---|---|
| 0 | `AC1CB58FD8388DCE3469D5A58A59B3D5B6345FDCED14CA7F73C97066A22D7455` | `11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011` |
| 1 | `A1C932944A18A4B86A2B070D85D03115AD2287E78FEC0609EFCC3DFF09E6C570` | `23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B` |
| 2 | `AFE1979580158C5608EEB614E237D52A4BDF03B9679D1B18746618936A35789F` | `BFA5FEB83B620D5BA633066466FE826CB7FBE8D3938FB0484755857D1E5B4874` |
| 3 | `6D409D5E044710737420FBCC37422A443D668D651F21524BF0F46AA46DBE72E6` | `3EDC9AB31B5D539503A54E21165D4F5DC599BD80DA75C897156D58DE27316868` |
| 4 | `5C859F80A980BD3D6D56B7EE872C7E174C71CC33640209AE2AB86373AB5959A0` | `8800A1407E7C3AC0906D166E7EC7789B4A3C4EC2BAC90E22A6FAA4E0194490DF` |
| 5 | `3FBBA194ED75DE5E7357C0CEFE49A4D4077C3D866E2474ACE3A0A08154369067` | `4152DF07FCBFA6EFC70B8875085029B9A4A77ED740317B80225FC610B3A40FE4` |
| 6 | `1B5E4FC6FF8B6B98CBF3148730229F04B2D42F2BD268800BE0B2D04F3D028404` | `AAC9DDE7EF38F78AB89AA5F06380CD8ED7733EDA1C94A549188F51A28D190930` |
| 7 | `F71DABAC2FF827490A3609937DD2A15C5A9954103C7504830000D37F143AAFF9` | `AC01F88A2F0C97DDDDA4D1B16008A8344BBC1FEE73D185A9EE41F5E2BF4009E4` |

All eight canonical stderr files are present, zero bytes, and have the
empty-file SHA-256

```text
E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855
```

The first two production runs predated explicit stderr capture.  They were
therefore replayed from the pinned source with separate stdout and stderr.
The checker requires byte-for-byte stdout equality and empty replay stderr:

| shard | production bytes | replay bytes | common SHA-256 |
|---:|---:|---:|---|
| 0 | 44,480 | 44,480 | `11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011` |
| 1 | 44,372 | 44,372 | `23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B` |

Both replay stderr files are zero bytes and have the same empty-file hash.

## 9. Exact aggregate and global forest identity

The exact union is

\[
 \boxed{
 \begin{aligned}
 \text{pairs}&=610,\\
 \text{cases}&=1{,}830,\\
 \text{processed boxes}&=8{,}232{,}800,\\
 \text{positive leaves}&=22{,}986,\\
 \text{pruned leaves}&=4{,}176{,}374,\\
 \text{maximum depth}&=15,\\
 \text{smallest positive margin}
 &=2.144211613601797\times10^{-5}.
 \end{aligned}}
\]

The 610 corner forests contribute \(610\cdot16\) roots, and the 1,220
lower/open forests contribute \(1{,}220\cdot128\) roots.  Hence the total
initial-root count is

\[
 I=165{,}920.
\]

The global full-binary-forest identity recomputes exactly:

\[
 \boxed{
 8{,}232{,}800
 =2(22{,}986+4{,}176{,}374)-165{,}920.}
\]

The normalized 1,830-key coverage hash is

```text
B1C4A0B498CEFFBC211C2F1F6A8AC8F4D81164BA4B8C67E83E09B7FADED9AB01
```

and the SHA-256 of the eight raw stdout hashes, in shard order with a final
newline, is

```text
9515F61976AE9D594B3725829AE6C40011199379F41810F8EBFC38470DC32140
```

The durable aggregate evidence is:

| artifact | bytes | SHA-256 |
|---|---:|---|
| `human/outbox/no-drop-high-floor-shards/aggregate-final.log` | 5,334 | `2E11E13CA0C00C39E09171CEDEDD8D31C5D4314DF68D1958AF7A0553F6BD09C6` |
| `human/outbox/no-drop-high-floor-shards/aggregate-final.stderr.log` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |

The durable stdout is UTF-16 LE with a BOM and CRLF newlines.  Decoding it
reproduces the live accepted-checker output character-for-character.

## 10. Hardened aggregate checker

Before it imports the wrapper, the accepted checker pins the exhaustion
verifier, shared core, high-floor wrapper, and shard launcher hashes listed
in Section 2.  It then:

- requires all eight canonical stdout and stderr paths;
- decodes UTF-16 only under a UTF-16 BOM and otherwise uses UTF-8 with an
  optional BOM;
- rejects empty, unterminated, malformed, extra, reordered, duplicated, or
  post-footer content;
- accepts integer fields only in canonical ASCII form
  `0|[1-9][0-9]*`;
- accepts a numeric minimum only if it is `inf` or a finite canonical Python
  float satisfying `token == str(value)`;
- enforces depth at most 72 and at most 500,000 boxes in each phase;
- checks every row's initial-root count, leaf accounting, and positive
  margin;
- recomputes every footer total, minimum, and normalized coverage hash;
- requires exact ordered equality with the exhaustion-derived assignment;
- proves that the global union has exactly 1,830 unique rows and exactly
  610 pair projections;
- requires the shard 0/1 replays to be byte-identical to production and
  their replay stderr to be empty.

The final independent audit ran a 50-case adversarial matrix.  All 50
mutations were rejected, including nonfinite overflow tokens, Unicode and
leading-zero integers, depth 999, 500,002 boxes, malformed ordering,
coverage/footer mutations, missing or nonempty stderr, and replay
mismatches.  The canonical union remained accepted.  The final audit
verdict is **FINAL PASS** at the exact report hash recorded at the start of
this note.

## 11. Exact reproduction commands

The exhaustion and deterministic plan are reproduced by

```text
python scripts/general_d_no_drop_exhaustion_verify.py
python scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --plan-only
```

The full seed-grid checks are

```text
python scripts/general_d_no_drop_high_floor_compact_verify.py --precision 384 --seed-audit
python scripts/general_d_no_drop_high_floor_compact_verify.py --precision 512 --seed-audit
```

For each `<i>` in `0,1,...,7`, the production shard command is

```text
python -u scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --shard-index <i> --precision 384 --max-boxes 500000 --sigma-panels 16 --alpha-panels 8 1> human/outbox/no-drop-high-floor-shards/shard-<i>-of-8.log 2> human/outbox/no-drop-high-floor-shards/shard-<i>-of-8.stderr.log
```

The two pinned-source replay commands are

```text
python -u scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --shard-index 0 --precision 384 --max-boxes 500000 --sigma-panels 16 --alpha-panels 8 1> human/outbox/no-drop-high-floor-shards/shard-0-of-8.replay.log 2> human/outbox/no-drop-high-floor-shards/shard-0-of-8.replay.stderr.log
python -u scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --shard-index 1 --precision 384 --max-boxes 500000 --sigma-panels 16 --alpha-panels 8 1> human/outbox/no-drop-high-floor-shards/shard-1-of-8.replay.log 2> human/outbox/no-drop-high-floor-shards/shard-1-of-8.replay.stderr.log
```

The final aggregate command is

```text
python -u scripts/_aggregate_general_d_no_drop_high_floor_shards.py 1> human/outbox/no-drop-high-floor-shards/aggregate-final.log 2> human/outbox/no-drop-high-floor-shards/aggregate-final.stderr.log
```

On Windows PowerShell these redirections produce UTF-16 LE stdout.  That is
the preserved byte-level artifact; the checker and independent audit both
decode it explicitly.

## 12. Combination with the low-floor and \(n=1\) modules

The direct \(n=1\) no-drop argument is already complete.  The finite
\(f=2,3\) computations are also complete as executions: the proof note

```text
human/outbox/general-d-round-05-no-drop-compact.md
44304F58E3B61FE1B75AEDC0D764800385AC3C0B905E60F1A3792D97DBCE9BE5
```

records 1,134 cases on each floor, 2,268 cases in total, 27,582,331 boxes,
40,244 positive leaves, and a smallest positive diagnostic
\(1.7050400932319067\times10^{-6}\).  Its complete \(f=3\) replay executed
the two-predicate source image now checked in at

```text
scripts/general_d_no_drop_low_floor_final_verify.py
4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F
```

The persisted file is byte-identical to the image used by the completed
low-floor replay.  The accepted high-floor chain deliberately pins the
shared core at `EEF8150...ACCDE`.  Replacing that file in place by the
`4AD4...9319F` image would correctly make the pinned shard helper and
aggregate checker refuse replay.  The final high-floor audit therefore
recommended, and the repository now implements, the following layout:

1. the `EEF8150...ACCDE` source remains at its current shared/high-floor
   path;
2. the executed `4AD4...9319F` bytes live at the distinct low-floor path
   shown above;
3. the shard helper and aggregate checker retain their accepted
   `EEF8150...ACCDE` pins.

Creation of the separately named low-floor source is therefore complete.
Its final independent audit is frozen at
`human/outbox/general-d-round-05-no-drop-compact-final-independent-audit.md`.
This note continues to claim only the \(f\geq4\) sector.  Combining the
direct \(n=1\) module, the separately audited \(f=2,3\) module, and this
certificate into an all-floor theorem is deferred to the separate
general-\(d\) manuscript integration.

## 13. Remaining obligations and scope boundary

The completed result is

\[
 \boxed{
 \text{all no-drop configurations with }f\geq4
 \text{ have }\mathscr S_n>0.}
\]

The remaining work is separate:

1. preserve the frozen `EEF8150...ACCDE` high-floor import topology and the
   distinct checked-in `4AD4...9319F` low-floor source;
2. integrate the combined no-drop theorem into the separate general-\(d\)
   manuscript using the now-frozen pins and audits;
3. continue the high-floor first-drop analysis independently.

The first-drop residual is not part of the 610-pair no-drop exhaustion, the
1,830-row phase ledger, or the theorem proved here.  No conclusion in this
note should be used to erase or weaken that separate remaining obligation.
