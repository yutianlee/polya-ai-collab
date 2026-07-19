# Preliminary independent audit: high-floor no-drop aggregate checker

Date: 18 July 2026  
Scope: source architecture and completed shard ledgers 0--6  
Final eight-shard replay: **PENDING**

## Verdict

The preliminary verdict has three parts.

1. **PASS -- retained-pair and shard architecture.** The exhaustion replay,
   the 610-pair retained union, the residue-class partition, all three
   phases per pair, and the binary-forest accounting are correct.

2. **PASS -- internal content of completed stdout ledgers 0--6.** The seven
   completed stdout logs contain exactly their 534 assigned pairs and 1,602
   assigned phase rows. Every row, footer total, ordered coverage list, and
   coverage digest recomputes exactly.

3. **NOT YET ACCEPTABLE AS A FINAL AGGREGATE CHECKER.** Two fail-closed
   hardening requirements are missing from the audited checker:

   - it does not pin the exhaustion verifier hash;
   - it checks a shard stderr file only if that file exists.

   Shards 0 and 1 currently have no stderr files. Their stdout ledgers are
   valid evidence, but they do not certify that those two runs emitted no
   stderr. They must be replayed with separately captured stderr after the
   checker is hardened. No complete \(f\geq4\) claim is made here.

## 1. Frozen source snapshot

| artifact | bytes | SHA-256 |
|---|---:|---|
| scripts/_aggregate_general_d_no_drop_high_floor_shards.py | 10,387 | 634CDD861AB3614D1AB0905B589E1FF0F701FA086462E5158B932D955AEAB6B2 |
| scripts/general_d_no_drop_high_floor_compact_verify.py | 19,447 | 5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F |
| scripts/_general_d_no_drop_high_floor_shard.py | 5,370 | A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092 |
| scripts/general_d_no_drop_compact_verify.py | 33,458 | EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE |
| scripts/general_d_no_drop_exhaustion_verify.py | 7,625 | 81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A |
| human/outbox/general-d-round-08-no-drop-high-floor-independent-audit.md | 13,107 | FFD118B79A1078C5DE9BF44688501924738E41B3D5A9673BD8A0BF8D354926B8 |
| human/outbox/general-d-round-08-no-drop-high-floor-shard-plan.md | 3,113 | D179B1043D0A7F061BACB6235800ED602D8036A6C46E9B8FDB4DC5F88FF65D13 |

All five Python sources compile in memory. None contains a NUL, carriage
return, form-feed, or U+FFFD replacement character. No frozen source,
shard log, manuscript, or Round 8F artifact was edited in this pre-audit.

## 2. Independent retained-pair reconstruction

I executed the exhaustion verifier directly:

    python scripts/general_d_no_drop_exhaustion_verify.py

It exited zero at 256 Arb bits and reported:

    central endpoint comparisons: 138184
    central retained necessary pairs: 649
    outer comparisons: 980
    outer retained finite necessary pairs: 60

I then read its exported central_pairs and outer_pairs directly, rather
than taking the aggregate checker's count on trust. After restricting to
\(f\geq4\) and \(n\geq2\), the exact counts are

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]
\[
 \#(\mathcal C\cup\mathcal O)=610.
\]

The lexicographically first and last retained pairs are \((4,2)\) and
\((49,48)\). The wrapper checks the same four counts before returning the
two sets.

For each lexicographic ordinal \(j=0,\ldots,609\), the shard assignment is
exactly \(j\bmod8\), and the three phases are exactly

\[
 \{\mathrm{corner},\mathrm{lower},\mathrm{open}\}.
\]

The partition has 77 pairs in shards 0 and 1 and 76 pairs in shards 2--7,
so the intended total is

\[
 2\cdot231+6\cdot228=1\,830
\]

phase rows. The independent plan replay

    python scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --plan-only

reproduced all eight published assignment hashes:

| shard | pairs | cases | assignment SHA-256 |
|---:|---:|---:|---|
| 0 | 77 | 231 | E04792172F4F934D1E8DE823A7724D082C62C6A089092CDED9519AA4822A3D84 |
| 1 | 77 | 231 | D975D89CCAF00D6EB84A9E401A2A97F26E90D16B6AE7B834A0F832FB9F526907 |
| 2 | 76 | 228 | 2DBBB8A4309429B2C1FE50AC6CE1247A10823DB8EC28A37090DBE8E712AA3F0D |
| 3 | 76 | 228 | 95CF3BBD857142837A55D20200914CDFC172010B7F912BA6E74B6BC5E8FEE1E8 |
| 4 | 76 | 228 | 0F69BAFFB45C55E468FD3CB3CE3086A7139165420D21D15CDA83DE2851557449 |
| 5 | 76 | 228 | A29C9D1E1C10550DA95245C2B2908D1DFA4FDDD2AB9BEFDC8CDA67625A870AFA |
| 6 | 76 | 228 | 1F073B27CEA4819DC8FC25A8698CC77A25D8A3337341C961F1C8E396DF3A71C9 |
| 7 | 76 | 228 | CA94BDFDA7CDDEE16F8AA8CD253742833D4B08FB95B2CAFA3BF8A31786B93EF9 |

The helper also asserts that the flattened assignments have exactly 610
distinct entries and equal the reconstructed retained list.

## 3. Aggregate parser audit

The checker supports the encodings actually present:

- a UTF-16 little- or big-endian BOM selects Python's UTF-16 decoder;
- every other file is decoded as UTF-8 with an optional BOM.

Current completed logs 0, 1, 2, 4, 5, and 6 are UTF-16 LE with a BOM.
Shard 3 is UTF-8 without a BOM. All seven decode correctly, end in a
newline, and contain one final PASS footer.

The canonical stdout parser fails closed on:

- a missing canonical shard log;
- invalid UTF-16 or UTF-8;
- an empty file or unterminated final line;
- a malformed or unrecognized line, including a blank or garbage line;
- a CASE row after PASS;
- a duplicate PASS;
- a PASS that is not the final line;
- a missing, duplicated, reordered, or extra CASE row;
- a changed ordinal, pair, or phase;
- a row assigned to the wrong residue class;
- a footer with a changed shard index/count, pair count, case count,
  processed-box total, positive total, maximum depth, minimum margin, or
  coverage hash.

The comparison with the exact ordered assignment is stronger than a set
comparison: it fixes all ordinals, pairs, and the corner/lower/open order.
The global checks then require exactly 1,830 distinct keys, exact equality
with the reconstructed eight-shard union, and exactly 610 pair projections.
Extra CASE/PASS/garbage content in any canonical log is rejected. Files
with noncanonical names are ignored and cannot contribute to the
certificate; this is harmless to exact canonical coverage, though the
checker does not enforce directory cleanliness.

The CASE grammar permits only nonnegative integers for boxes, positive
leaves, pruned leaves, and depth. It rejects NaN and arbitrary infinity
tokens. For a nonempty phase, the checker reconstructs

\[
 I=2(\mathrm{positive}+\mathrm{pruned})-\mathrm{boxes}
\]

and requires \(I=16\) on a corner and \(I=128\) on a lower/open phase.
If no positive leaf exists, the minimum must be infinity; otherwise it
must be finite and strictly positive. The special zero-processed
disposition is accepted only as

\[
 (\mathrm{boxes},\mathrm{positive},\mathrm{pruned},
   \mathrm{depth},\mathrm{smallest})=(0,0,1,0,\infty).
\]

Thus every full-binary forest identity and accepted margin is checked
exactly.

## 4. Two checker defects

### 4.1 Missing exhaustion-verifier pin

The aggregate checker pins the helper, wrapper, and core hashes, but it
does not define or verify the exhaustion-verifier hash

    81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A.

The wrapper imports and executes the exhaustion verifier by path, so the
exhaustion source is a real transitive proof dependency. Reconstructing
the current 610-pair list catches most accidental list changes, but it
does not prove that the exhaustion mathematics itself is the audited
version. This omission was already identified as essential hardening in
Section 8 of the architecture audit. A final checker must pin this file
before importing the wrapper or reconstructing assignments.

### 4.2 Missing stderr is accepted

The checker currently uses the logic

    if stderr_path.exists():
        require(stderr_path.read_bytes() == b"", ...)

Therefore a nonempty existing stderr fails, but a missing stderr file
passes silently. Shards 0 and 1 currently have no
shard-0-of-8.stderr.log or shard-1-of-8.stderr.log. Their stdout PASS
footers prove that all assigned certificate calls completed, but they do
not prove that stderr was empty. A final checker must require every
canonical stderr file to exist and be exactly zero bytes. Shards 0 and 1
must be replayed with separate stdout and stderr capture; missing files
must not be manufactured.

No other fail-open parser or coverage defect was found.

## 5. Exact completed-shard results

I independently parsed every line of completed logs 0--6, reconstructed
each expected assignment from the exhaustion verifier, checked every
forest identity, and recomputed each footer and digest.

| shard | encoding | pairs | cases | boxes | positive | pruned | depth | smallest |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | UTF-16 LE BOM | 77 | 231 | 1,032,534 | 3,506 | 523,233 | 15 | 2.144211613601797e-05 |
| 1 | UTF-16 LE BOM | 77 | 231 | 1,020,324 | 7,971 | 512,663 | 15 | 3.295220536637341e-05 |
| 2 | UTF-16 LE BOM | 76 | 228 | 1,030,748 | 3,563 | 522,147 | 15 | 4.803944338325024e-05 |
| 3 | UTF-8 | 76 | 228 | 1,030,862 | 258 | 525,509 | 15 | 0.04178887764990063 |
| 4 | UTF-16 LE BOM | 76 | 228 | 1,028,332 | 1,201 | 523,301 | 15 | 0.001293689185865621 |
| 5 | UTF-16 LE BOM | 76 | 228 | 1,036,944 | 123 | 528,685 | 15 | 0.010374015346279027 |
| 6 | UTF-16 LE BOM | 76 | 228 | 1,013,068 | 3,377 | 513,493 | 15 | 0.0007232961617573032 |

Their exact coverage and raw-log hashes are:

| shard | coverage SHA-256 | raw stdout log SHA-256 |
|---:|---|---|
| 0 | AC1CB58FD8388DCE3469D5A58A59B3D5B6345FDCED14CA7F73C97066A22D7455 | 11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011 |
| 1 | A1C932944A18A4B86A2B070D85D03115AD2287E78FEC0609EFCC3DFF09E6C570 | 23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B |
| 2 | AFE1979580158C5608EEB614E237D52A4BDF03B9679D1B18746618936A35789F | BFA5FEB83B620D5BA633066466FE826CB7FBE8D3938FB0484755857D1E5B4874 |
| 3 | 6D409D5E044710737420FBCC37422A443D668D651F21524BF0F46AA46DBE72E6 | 3EDC9AB31B5D539503A54E21165D4F5DC599BD80DA75C897156D58DE27316868 |
| 4 | 5C859F80A980BD3D6D56B7EE872C7E174C71CC33640209AE2AB86373AB5959A0 | 8800A1407E7C3AC0906D166E7EC7789B4A3C4EC2BAC90E22A6FAA4E0194490DF |
| 5 | 3FBBA194ED75DE5E7357C0CEFE49A4D4077C3D866E2474ACE3A0A08154369067 | 4152DF07FCBFA6EFC70B8875085029B9A4A77ED740317B80225FC610B3A40FE4 |
| 6 | 1B5E4FC6FF8B6B98CBF3148730229F04B2D42F2BD268800BE0B2D04F3D028404 | AAC9DDE7EF38F78AB89AA5F06380CD8ED7733EDA1C94A549188F51A28D190930 |

Stderr evidence is:

- shards 2--6: present, zero bytes, SHA-256
  E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855;
- shards 0--1: missing, so emptiness is not certified.

## 6. Exact partial aggregate for shards 0--6

The union of completed stdout ledgers 0--6 is exactly the expected partial
residue-class union:

\[
 \boxed{
 \begin{aligned}
 \text{pairs}&=534,\\
 \text{cases}&=1\,602,\\
 \text{processed boxes}&=7\,192\,812,\\
 \text{positive leaves}&=19\,999,\\
 \text{pruned leaves}&=3\,649\,031,\\
 \text{maximum depth}&=15,\\
 \text{smallest positive margin}
 &=2.144211613601797\times10^{-5}.
 \end{aligned}}
\]

There are no zero-processed cases. The total initial-root count is
145,248, and the aggregate forest identity is

\[
 7\,192\,812
 =2(19\,999+3\,649\,031)-145\,248.
\]

The 1,602-key partial normalized coverage hash is

    D3DD14BE0E0C99487540BF1F493CBBB5278CBC2D6111E8E3F3D8B4AEBBFF118D

and the SHA-256 of the seven raw stdout log hashes, in shard order with a
final newline, is

    6DC44832F5E74662648B81D9D43613C883A830D0D8485EE83520CB45357F6805.

These are partial-ledger identifiers only. They are not the final
eight-shard coverage or log-set hashes.

## 7. Requirements before final replay

Before any global PASS:

1. harden the checker to pin the exhaustion verifier at
   81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A;
2. require all eight canonical stderr files to exist and be zero bytes;
3. replay shards 0 and 1 with durable, separate stdout/stderr capture;
4. wait for shard 7 to emit its complete PASS footer and empty stderr;
5. re-audit the hardened checker hash;
6. run the final aggregate and independently verify all 610 pairs, 1,830
   unique phase rows, per-case and global forest identities, footer totals,
   coverage digest, raw-log-set digest, and post-run frozen hashes.

Until those steps finish, the completed stdout rows are valid partial
evidence, but the full \(f\geq4\) no-drop replay remains **PENDING**.
