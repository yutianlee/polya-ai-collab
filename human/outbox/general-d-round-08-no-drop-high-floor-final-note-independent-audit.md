# Independent audit of the Round 8 high-floor no-drop final note

Date: 18 July 2026

Status: **FINAL PASS**.

This verdict applies only to the corrected exposition note

```text
human/outbox/general-d-round-08-no-drop-high-floor-final.md
bytes:   22,171
SHA-256: 3E43416CFEDBD50B9B29DC57E4FC6A786BCAD9CD90E469C785A466262E8DAE63
```

The note accurately states the mathematics, interval directions, exact
eight-shard ledger, accepted-checker behavior, reproduction commands, and
scope of the completed \(f\geq4\) no-drop certificate.  It does not claim
the combined all-floor no-drop theorem or the high-floor first-drop theorem.

No verifier, checker, canonical or replay log, manuscript, proof note, or
original \(d=3\) artifact was edited during this audit.  The only file added
by the auditor is this report.

## 1. Revision history and exact accepted bytes

The first note supplied for audit had 22,217 bytes and SHA-256

```text
7CB35585D9E03DB6652A2D124990DC80664063CFC62D61D5D4109CBF5A8ADE08
```

It had no mathematical defect, but five notation sites were not valid
inline TeX: the two endpoint pairs, the \(Q\) table heading, \(T\), \(K\),
and \(1/2\).  After those sites were repaired, the note had 22,229 bytes
and SHA-256

```text
1945679ED4AC81A88F3F4C21D1A86CB09A93134BA6D08266CB614601BC78F94F
```

Reversing exactly those six token substitutions in memory reproduced the
original 22,217 bytes and the original `7CB35585...` hash.

Two later sentences grouped the direct high-floor wrapper with the
entrypoints that enforce the shared-core hash.  Source inspection shows
that the shard helper and aggregate checker pin `EEF8150...ACCDE`, while
the direct wrapper does not self-pin.  The first provenance correction
produced 22,221 bytes and SHA-256

```text
4E73B69758D6686C607414C7D14BED58808FC42E13AAF576068208BC71538BB5
```

and the second produced the `1CDC2B87...` note.  Reversing each
one-sentence change independently reproduced its exact predecessor hash:
`1945679E...` from `4E73B697...`, then `4E73B697...` from `1CDC2B87...`.
No other byte changed in either step.

The low-floor final audit completed while this review was open, so the
`1CDC2B87...` statement that its audit was pending then became stale.  The
status paragraph and remaining-work list were updated without broadening
this note's theorem.  An intermediate 22,185-byte version had SHA-256
`8F696AC44D21D079063E2FBB0CC395596951B2F77CB63451F5B7FB8CFE461E79`;
it was not accepted because its wording could be read
as declaring the combined no-drop theorem in this high-floor note.  The
final 22,171-byte `3E43416C...` version instead records that the low-floor
audit is frozen while explicitly deferring all-floor combination to the
separate general-dimensional manuscript integration.  Reversing exactly
the final status paragraph and remaining-work list in memory reconstructs
the 22,216-byte `1CDC2B87...` file exactly.

The accepted note says, correctly, that replacing the shared core in
place would make the *pinned shard helper and aggregate checker* refuse
replay, and that those two entrypoints retain the accepted core pin.

## 2. Frozen references

The note's source and audit manifest agrees byte-for-byte with the
workspace:

| artifact | bytes | SHA-256 |
|---|---:|---|
| `scripts/general_d_no_drop_exhaustion_verify.py` | 7,625 | `81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A` |
| `scripts/general_d_no_drop_compact_verify.py` | 33,458 | `EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE` |
| `scripts/general_d_no_drop_high_floor_compact_verify.py` | 19,447 | `5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F` |
| `scripts/_general_d_no_drop_high_floor_shard.py` | 5,370 | `A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092` |
| `scripts/_aggregate_general_d_no_drop_high_floor_shards.py` | 12,184 | `79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996` |
| architecture audit | 13,107 | `FFD118B79A1078C5DE9BF44688501924738E41B3D5A9673BD8A0BF8D354926B8` |
| repaired root-localization note | 9,211 | `752952059FE017BCF988E86A55F871AA9B240A8DE0C0FE26806A53F9656DD5E5` |
| final checker audit | 15,353 | `064BA541D96BF7B07AC60758E17FDE5E455A383B0CFC3E20E392308EF7258242` |
| final low-floor audit | 19,828 | `83ABBE4DB8228B06678CDE41FED4B02281C154A711ABC9D26FF204FCC47B5475` |

The accepted aggregate checker checks all four transitive proof-source
hashes before importing the wrapper.  The shard helper independently pins
the wrapper and shared core.  The direct wrapper's lack of a self-pin is no
longer misstated by the final note.

The certificate verdict and adversarial results in the frozen
`064BA541...` audit remain valid.  Its Section 8 used the same overbroad
wrapper-pin shorthand that appeared in the draft note.  The corrected final
note and this audit supersede only that non-proof provenance sentence; no
mathematical, ledger, parser, or verdict statement is affected, and the
frozen audit file was preserved.

## 3. Exhaustion, strict phases, and theorem boundary

A fresh read-only run of the frozen exhaustion verifier exited zero and
reproduced its Arb PASS.  Its full lists contain 649 central and 60 outer
pairs.  After the exact restrictions \(f\geq4\) and \(n\geq2\), an
independent reconstruction gives

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]

so the exact union contains 610 pairs, from \((4,2)\) through
\((49,48)\).  The exhaustion source also certifies the finite-tail and
limiting comparisons that exclude escape for every \(f\geq4\) outside
this union.  Thus the note is justified in combining the 610-pair replay
with the already completed direct \(n=1\) module to close the
\(f\geq4\) no-drop sector.

The phase table agrees with `phase_Q`, `phase_levels`, and the one-sided
wall reduction in the frozen core:

| phase | strict chamber | \(Q\) | terminal levels |
|---|---|---:|---:|
| corner | \(\alpha=0,\ \varepsilon=0\) | \(f-1\) | \(f-1\) |
| lower | \(0<\alpha<1,\ \varepsilon=0\) | \(f-1\) | \(f\) |
| open | \(0\leq\alpha<1,\ 0<\varepsilon<1/4\) | \(f\) | \(f\) |

The open chamber is reduced at fixed \((\mu,r)\) to \(A(q)=f-1/4\)
while retaining its open-side \(Q=f\) and \(f\) terminal levels.  Closed
\(\alpha\)-hulls are used only as one-sided interval enclosures.  The
corner is separately certified, so there is no equality-face gap.  The
intended and actual ledger therefore has exactly
\(610\cdot3=1{,}830\) chambers.

## 4. Sigma localization and root directions

The coordinate identities in the note are exact:

\[
 \sigma^2=\frac{K-\mu}{K},\qquad
 \kappa=\sigma(K-\mu),\qquad
 K=\frac{\kappa}{\sigma^3},\qquad
 \mu=\frac{\kappa(1-\sigma^2)}{\sigma^3}.
\]

Every residual point obeys \(K<K_{\rm nd}(n,Q)\) and
\(\kappa\geq21/8\), whence

\[
 K_{\rm nd}(n,Q)\sigma^3>\kappa\geq\frac{21}{8}.
\]

The lower bisection advances only when the Arb upper endpoint proves
\(K_{\rm nd}\sigma^3<21/8\).  Its returned \(s_0\) remains on the proved
impossible side and is retained, giving overlap rather than a gap.

At the other endpoint, the strict ceiling

\[
 \kappa<\frac{3\pi f}{2}<\frac{33f}{7}
\]

and \(\mu\geq n+1/2\) imply the note's strict physicality inequality.
The upper function is strictly decreasing on \((0,1)\); the code retains
the first \(s_1\) whose Arb upper endpoint proves physicality impossible.
All three phases of all 610 pairs have nonempty returned intervals.  The
16 rational sigma panels and eight rational alpha panels yield exactly 16
initial roots for a corner and 128 for a lower/open phase.

For lower and open phases, the deterministic seed

\[
 \kappa_*(f)=\frac{13}{6}\left(f-\frac14\right)
\]

is used only after outward arithmetic proves both \(q(\kappa_*)>0\) and
the strict action upper bound below \(T=f-1/4\).  Failure requests a split.
The two 384- and 512-bit seed audits cover exactly 156,160 boxes.  Source
inspection confirms that the exact positive-gap and noncancelling
trapezoid/midpoint enclosures contain the same action and are intersected
by taking the larger lower and smaller upper endpoint.

The root directions in the note are exact: a lower endpoint advances only
under \(\overline A(m)<T\), and an upper endpoint retreats only under
\(\underline A(m)>T\).  An inconclusive common upper test retains
\(33f/7\); an action upper endpoint below \(T\) proves no root.  The corner
uses the stable half-angle identity and eliminates \(\kappa\) directly.

## 5. Necessary prunes and positive scalar

Every inequality listed in Section 6 of the note matches the frozen core
with the correct strictness and directed endpoint.  This includes
physicality, the root-free cutoff, active-floor, universal upper/slope/width
conditions, the \(n>48\) central obstruction, the outer width and slope
conditions, endpoint-floor and endpoint-phase inequalities, and the
shelf-curvature prune

\[
 2\varepsilon+\Delta+\frac{n\Delta}{3(2r+n)}
 \geq\frac{n-1}{2n},\qquad \Delta=A(r)-A(q).
\]

Failure to prove a terminal exclusion yields subdivision, not a prune.
The exact gap-variable head is

\[
 H=J_2(K,r)-J_2(K,q)-J_2(\mu,r)+J_2(\mu,q)-2nf,
\]

and its lower bound is combined with the independent shelf-curvature lower
bound.  The angle equation, terminal-level counts, \(-Q\) term, and upper
enclosure of the inner cap all agree with the implementation.  Thirty-two
directed angle steps evaluate the lower payment at a lower endpoint for
\(K\).  A leaf is positive only after the outward lower endpoint of the
complete head-plus-terminal scalar is strictly positive.

The positive series uses twelve terms and a directed geometric remainder
with ratio below \(1/2\); analytically nonnegative hulls are intersected
with the nonnegative half-line before square roots.  Depth 72 and 500,000
processed boxes per phase are hard failure caps.  The note correctly states
the observed maximum depth 15 and that no phase reached the box cap.

## 6. Assignment, shard ledgers, and forests

A fresh plan-only replay exited zero and reproduced every assignment hash:

| shard | pairs | cases | assignment SHA-256 |
|---:|---:|---:|---|
| 0 | 77 | 231 | `E04792172F4F934D1E8DE823A7724D082C62C6A089092CDED9519AA4822A3D84` |
| 1 | 77 | 231 | `D975D89CCAF00D6EB84A9E401A2A97F26E90D16B6AE7B834A0F832FB9F526907` |
| 2 | 76 | 228 | `2DBBB8A4309429B2C1FE50AC6CE1247A10823DB8EC28A37090DBE8E712AA3F0D` |
| 3 | 76 | 228 | `95CF3BBD857142837A55D20200914CDFC172010B7F912BA6E74B6BC5E8FEE1E8` |
| 4 | 76 | 228 | `0F69BAFFB45C55E468FD3CB3CE3086A7139165420D21D15CDA83DE2851557449` |
| 5 | 76 | 228 | `A29C9D1E1C10550DA95245C2B2908D1DFA4FDDD2AB9BEFDC8CDA67625A870AFA` |
| 6 | 76 | 228 | `1F073B27CEA4819DC8FC25A8698CC77A25D8A3337341C961F1C8E396DF3A71C9` |
| 7 | 76 | 228 | `CA94BDFDA7CDDEE16F8AA8CD253742833D4B08FB95B2CAFA3BF8A31786B93EF9` |

Direct byte hashing and a fresh accepted-checker replay reproduce the
complete per-shard table in the note:

| shard | boxes | positive | pruned | depth | smallest |
|---:|---:|---:|---:|---:|---:|
| 0 | 1,032,534 | 3,506 | 523,233 | 15 | `2.144211613601797e-05` |
| 1 | 1,020,324 | 7,971 | 512,663 | 15 | `3.295220536637341e-05` |
| 2 | 1,030,748 | 3,563 | 522,147 | 15 | `4.803944338325024e-05` |
| 3 | 1,030,862 | 258 | 525,509 | 15 | `0.04178887764990063` |
| 4 | 1,028,332 | 1,201 | 523,301 | 15 | `0.001293689185865621` |
| 5 | 1,036,944 | 123 | 528,685 | 15 | `0.010374015346279027` |
| 6 | 1,013,068 | 3,377 | 513,493 | 15 | `0.0007232961617573032` |
| 7 | 1,039,988 | 2,987 | 527,343 | 15 | `0.00028010088421405915` |

All eight raw stdout hashes and all eight normalized coverage hashes match
the note.  The raw hashes in shard order are

```text
11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011
23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B
BFA5FEB83B620D5BA633066466FE826CB7FBE8D3938FB0484755857D1E5B4874
3EDC9AB31B5D539503A54E21165D4F5DC599BD80DA75C897156D58DE27316868
8800A1407E7C3AC0906D166E7EC7789B4A3C4EC2BAC90E22A6FAA4E0194490DF
4152DF07FCBFA6EFC70B8875085029B9A4A77ED740317B80225FC610B3A40FE4
AAC9DDE7EF38F78AB89AA5F06380CD8ED7733EDA1C94A549188F51A28D190930
AC01F88A2F0C97DDDDA4D1B16008A8344BBC1FEE73D185A9EE41F5E2BF4009E4
```

Shards 0, 1, 2, 4, 5, 6, and 7 have UTF-16 BOMs; shard 3 is UTF-8
without a BOM.  All canonical stderr files are present and empty.  Shard
0 and 1 replay stdout is byte-identical to production at 44,480 and 44,372
bytes, respectively; both replay stderr files are empty.

Every one of the 1,830 nonempty rows satisfies

\[
 \text{boxes}=2(\text{positive}+\text{pruned})-I,
\]

with \(I=16\) for a corner and \(I=128\) otherwise.  The global initial
root count is therefore

\[
 610\cdot16+1{,}220\cdot128=165{,}920,
\]

and the note's global identity recomputes exactly.

## 7. Aggregate, durable transcript, and checker hardening

The accepted aggregate checker was run unmodified in a fresh subprocess.
It exited zero, emitted 2,666 ASCII/UTF-8 stdout bytes with SHA-256

```text
682091821787EC985085DE42C09BD48EEDDD2AB1ABA8FB7B14075CAAD1DD593C
```

and emitted zero stderr bytes.  It certified exactly

\[
 \begin{aligned}
 \text{pairs}&=610,&\text{cases}&=1{,}830,\\
 \text{boxes}&=8{,}232{,}800,&\text{positive}&=22{,}986,\\
 \text{pruned}&=4{,}176{,}374,&\text{max depth}&=15.
 \end{aligned}
\]

The minimum, normalized coverage digest, and raw-log-set digest are

```text
2.144211613601797e-05
B1C4A0B498CEFFBC211C2F1F6A8AC8F4D81164BA4B8C67E83E09B7FADED9AB01
9515F61976AE9D594B3725829AE6C40011199379F41810F8EBFC38470DC32140
```

The durable stdout has 5,334 bytes and SHA-256
`2E11E13CA0C00C39E09171CEDEDD8D31C5D4314DF68D1958AF7A0553F6BD09C6`.
It is UTF-16 LE with a BOM and ten CRLF line endings.  Decoding it gives
2,666 characters exactly equal to the fresh checker stdout.  Durable
stderr is the empty file with SHA-256
`E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`.

Every hardening claim in Section 10 of the note matches the accepted
checker source.  In particular, it uses canonical ASCII unsigned integers,
accepts only literal `inf` or a finite token satisfying
`token == str(float(token))`, enforces the two caps, checks ordered exact
coverage and every row forest, recomputes all footer fields, requires every
stderr file, and requires the two replay byte equalities.  The final
checker audit's 50-mutation matrix did reject all 50 cases, including
nonfinite overflow, Unicode and leading-zero integers, noncanonical
floats, depth 999, 500,002 boxes, ordering/footer/coverage changes, and
missing or nonempty stderr/replay evidence.

## 8. Reproduction commands

The exhaustion, plan-only, seed-audit, production-shard, replay, and final
aggregate commands printed in Section 11 use the exact script paths and
accepted command-line options.  The helper parser requires `--shard-count`,
requires `--shard-index` outside plan-only mode, and has the displayed
precision, box-cap, sigma-panel, and alpha-panel values.  The two seed-audit
commands use the production defaults of 16 sigma and eight alpha panels.

The exhaustion and plan-only commands were rerun during this audit and
passed.  The final aggregate command was rerun without redirecting over the
preserved evidence and passed.  The note's Windows PowerShell statement is
also consistent with the durable aggregate artifact: native stdout
redirection produced its UTF-16 LE BOM/CRLF representation, which the
checker and independent audits decode explicitly.

## 9. Low-floor state and remaining scope

The separately named low-floor source exists at

```text
scripts/general_d_no_drop_low_floor_final_verify.py
bytes:   33,512
SHA-256: 4AD4BAD7CECE561102B84C4983BD4C50D1BC39D59DA4D1ECD3D04BC7ADA9319F
```

A direct no-index diff against the `EEF8150...` core contains exactly the
two documented predicate widenings and no other change.  The completed
low-floor execution note is unchanged at 14,602 bytes and SHA-256

```text
44304F58E3B61FE1B75AEDC0D764800385AC3C0B905E60F1A3792D97DBCE9BE5
```

Its 1,134 cases on each floor, 2,268 total cases, 27,582,331 boxes, 40,244
positive leaves, and diagnostic minimum
\(1.7050400932319067\times10^{-6}\) agree with the final note.

The final independent low-floor audit is now frozen at

```text
human/outbox/general-d-round-05-no-drop-compact-final-independent-audit.md
bytes:   19,828
SHA-256: 83ABBE4DB8228B06678CDE41FED4B02281C154A711ABC9D26FF204FCC47B5475
```

That audit records `FINAL PASS` and repins the current high-floor note at
`3E43416C...E63`.  To avoid a circular hash dependency, the high-floor note
cites the low-floor audit path but not its hash.  It still claims only the
\(f\geq4\) theorem and defers the all-floor combination to the separate
manuscript integration.  It also keeps the high-floor first-drop residual
outside the 610-pair exhaustion and the 1,830-row ledger.  No sentence
erases, weakens, or silently absorbs either scope boundary.

## 10. Markdown, TeX, and preservation checks

The accepted note is ASCII UTF-8, LF-only, and ends with a final LF.  It
has no NUL, carriage return, form-feed, tab, U+FFFD, or other unexpected
control byte.  Its 84 inline-math opener/closer pairs, 28 display-math
opener/closer pairs, and 26 code-fence tokens are balanced.  The corrected
pair, \(Q\), \(T\), \(K\), and \(1/2\) sites are valid inline TeX.  No
remaining malformed or unescaped mathematical token was found.

The original \(d=3\) and manuscript hashes remain exactly those recorded
by the accepted final checker audit:

| artifact | SHA-256 |
|---|---|
| `manuscript/spherical-shell-polya-proof.tex` | `E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4` |
| `manuscript/spherical-shell-polya-proof.pdf` | `FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F` |
| `manuscript/spherical-shell-polya-analytic-supplement.tex` | `58C3D303BFE1B17A21CD31445FD6F8B52A52384817DBFDC2FEC4BA00CA3C3706` |
| `manuscript/spherical-shell-polya-analytic-supplement.pdf` | `CD6974EA1E1FA9E61A7DFF21C664B175BB4CA0321240F5FDB3B22A1BD53BB294` |
| `manuscript/spherical-shell-polya-supplement.tex` | `F6AB06BA835A8799082AE4832CD0B75B7AFE8FA810412FE5AA2170B03D197E4F` |

## 11. Verdict

**FINAL PASS.**  At SHA-256
`3E43416CFEDBD50B9B29DC57E4FC6A786BCAD9CD90E469C785A466262E8DAE63`,
the final note is an exact, conservative exposition of the completed
\(f\geq4\) no-drop certificate.  Its mathematical inequalities and root
directions, strict phase bookkeeping, 610-pair exhaustion, 1,830-row
forest ledger, per-shard and aggregate numbers, hashes, checker-hardening
claims, reproduction commands, low-floor status, and remaining-scope
statements all agree with the frozen source and evidence.

The report's own SHA-256 is recorded in the external handoff after this
file is closed, since embedding it here would change that hash.
