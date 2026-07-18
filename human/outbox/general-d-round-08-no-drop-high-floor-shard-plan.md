# General dimension, Round 8: deterministic high-floor no-drop shard plan

Date: 18 July 2026

Status: execution plan for the pending complete $f\ge4$ no-drop chamber
replay.  This plan does not itself certify the scalar in any unrun chamber.

## Frozen inputs

The launcher

```text
scripts/_general_d_no_drop_high_floor_shard.py
```

has SHA-256

```text
A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092
```

and refuses to run unless the two proof inputs have the audited hashes

```text
high-floor wrapper  5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F
shared core         EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE
```

It independently replays the exhaustion certificate and asserts that the
sorted union contains exactly 610 retained pairs.

## Assignment rule

Enumerate the lexicographically sorted retained pairs by ordinals
$j=0,\ldots,609$.  For a requested shard count $N$, assign the complete
pair, with all three phases, to shard

\[
 j\pmod N.
\]

The launcher asserts before execution that the shard union is the exact
610-pair list and that no ordinal is duplicated.  Keeping corner, lower,
and open phases together makes every completed pair easy to audit.

The recommended initial plan has $N=8$.  Shards 0 and 1 contain 77 pairs
and 231 phase cases each; shards 2 through 7 contain 76 pairs and 228 cases
each.  The exact assignment digests are:

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

These counts sum to

\[
 2\cdot231+6\cdot228=1{,}830.
\]

Replay the plan itself with

```text
python scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --plan-only
```

and run one shard, unbuffered for durable case lines, with

```text
python -u scripts/_general_d_no_drop_high_floor_shard.py --shard-count 8 --shard-index 0 --precision 384
```

## Coverage ledger

After each phase finishes, the launcher emits a line containing

```text
ordinal, f, n, phase, processed boxes, positive leaves, pruned leaves,
maximum depth, smallest accepted scalar endpoint
```

At successful completion it hashes the normalized sorted rows

```text
ordinal,f,n,phase\n
```

and prints the shard coverage SHA-256.  Final aggregation must assert exactly
1,830 distinct $(f,n,\text{phase})$ rows and compare their pair projection
with the 610-pair exhaustion list.  A shard log without its final `PASS`
line is partial coverage only.
