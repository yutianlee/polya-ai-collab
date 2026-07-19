# General dimension, Round 8 no-drop high-floor aggregate: final independent audit

Date: 2026-07-18

Status: **FINAL PASS**.

This audit covers only the completed \(f\geq4\) high-floor no-drop
aggregate certificate. It does not extend any claim outside that scope.
No verifier source, shard source, canonical log, replay log, manuscript,
proof note, or original \(d=3\) artifact was edited during this audit.

The checker initially presented for final review, SHA-256
173EBDB66E00309F79C6F8261593B6B59A3975F5019C9F075B1ECDAECCCF4081,
was rejected during this audit. Adversarial review found that numeric
overflow could masquerade as infinity and that the pinned depth and
per-case box caps were not enforced. The accepted checker is the
subsequently hardened and independently retested artifact:

    scripts/_aggregate_general_d_no_drop_high_floor_shards.py
    SHA-256 79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996
    12,184 bytes

The final verdict applies to that hash only.

## 1. Frozen dependency and prior-audit snapshot

The accepted checker pins all four transitive proof sources before it
imports the wrapper or reconstructs the assignment:

| artifact | bytes | SHA-256 |
|---|---:|---|
| scripts/general_d_no_drop_exhaustion_verify.py | 7,625 | 81A0C025E10E2B6255B07FD71C55D717235ED9165F2320DCB0EAF2627C46C51A |
| scripts/general_d_no_drop_high_floor_compact_verify.py | 19,447 | 5AEB44F264EA152131D2BD956EEDC902007DDC34FA39DE85031B91F1DC75BF5F |
| scripts/_general_d_no_drop_high_floor_shard.py | 5,370 | A9E3DB8E9DB7492C905D62E23666F189DFCAA74EDCB1616CFB1E050C36CA2092 |
| scripts/general_d_no_drop_compact_verify.py | 33,458 | EEF8150E8D4D56DC1F0088E0C1F3C2EAE3D7E93D688AB52F2CF5975416FACCDE |

All five Python sources, including the aggregate checker, compile in
memory.

The earlier architecture audit is unchanged at SHA-256
FFD118B79A1078C5DE9BF44688501924738E41B3D5A9673BD8A0BF8D354926B8
(13,107 bytes). The preliminary checker audit is unchanged at SHA-256
E049CA8F64163549BFC9548F0440821767F532FC7818F3C91D85690FA58F31AF
(12,539 bytes).

## 2. Independent exhaustion and assignment reconstruction

I executed the frozen exhaustion verifier directly and read its exported
central_pairs and outer_pairs; I did not take the aggregate checker's pair
count on trust. The replay emitted its Arb certification line and gave

\[
 \#\mathcal C_{\rm all}=649,\qquad
 \#\mathcal O_{\rm all}=60.
\]

After independently imposing \(f\geq4\) and \(n\geq2\),

\[
 \#\mathcal C=595,\qquad
 \#\mathcal O=60,\qquad
 \#(\mathcal C\cap\mathcal O)=45,
\]

and therefore

\[
 \boxed{\#(\mathcal C\cup\mathcal O)=610.}
\]

The first and last pairs are \((4,2)\) and \((49,48)\).
Enumerating the sorted union by \(j=0,\ldots,609\), assigning pair \(j\)
to shard \(j\bmod8\), and attaching phases in the fixed order

\[
 (\mathrm{corner},\mathrm{lower},\mathrm{open})
\]

gives 77 pairs and 231 phase rows in shards 0 and 1, and 76 pairs and
228 rows in shards 2 through 7. Thus the intended ledger has exactly

\[
 2\cdot231+6\cdot228=1830
\]

phase rows.

An unmodified plan-only replay exited 0, emitted empty stderr, and
reproduced all eight assignment digests:

| shard | assignment SHA-256 |
|---:|---|
| 0 | E04792172F4F934D1E8DE823A7724D082C62C6A089092CDED9519AA4822A3D84 |
| 1 | D975D89CCAF00D6EB84A9E401A2A97F26E90D16B6AE7B834A0F832FB9F526907 |
| 2 | 2DBBB8A4309429B2C1FE50AC6CE1247A10823DB8EC28A37090DBE8E712AA3F0D |
| 3 | 95CF3BBD857142837A55D20200914CDFC172010B7F912BA6E74B6BC5E8FEE1E8 |
| 4 | 0F69BAFFB45C55E468FD3CB3CE3086A7139165420D21D15CDA83DE2851557449 |
| 5 | A29C9D1E1C10550DA95245C2B2908D1DFA4FDDD2AB9BEFDC8CDA67625A870AFA |
| 6 | 1F073B27CEA4819DC8FC25A8698CC77A25D8A3337341C961F1C8E396DF3A71C9 |
| 7 | CA94BDFDA7CDDEE16F8AA8CD253742833D4B08FB95B2CAFA3BF8A31786B93EF9 |

The plan stdout has SHA-256
3241A1DC02571827B797159453E6067E0086A3D965BEBA8439F45DD7E4471013;
its stderr is empty.

## 3. Independent byte-level parse of all shard evidence

I independently decoded and parsed every canonical stdout byte rather
than importing the aggregate parser. Shards 0, 1, 2, 4, 5, 6, and 7 are
UTF-16 LE with a BOM; shard 3 is UTF-8 without a BOM. Every file ends in
a newline, contains its exact ordered CASE ledger followed by one final
PASS footer, and has no missing, duplicated, reordered, or extra key.

The recomputed shard results are:

| shard | pairs | cases | boxes | positive | pruned | depth | smallest |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 77 | 231 | 1,032,534 | 3,506 | 523,233 | 15 | 2.144211613601797e-05 |
| 1 | 77 | 231 | 1,020,324 | 7,971 | 512,663 | 15 | 3.295220536637341e-05 |
| 2 | 76 | 228 | 1,030,748 | 3,563 | 522,147 | 15 | 4.803944338325024e-05 |
| 3 | 76 | 228 | 1,030,862 | 258 | 525,509 | 15 | 0.04178887764990063 |
| 4 | 76 | 228 | 1,028,332 | 1,201 | 523,301 | 15 | 0.001293689185865621 |
| 5 | 76 | 228 | 1,036,944 | 123 | 528,685 | 15 | 0.010374015346279027 |
| 6 | 76 | 228 | 1,013,068 | 3,377 | 513,493 | 15 | 0.0007232961617573032 |
| 7 | 76 | 228 | 1,039,988 | 2,987 | 527,343 | 15 | 0.00028010088421405915 |

The raw stdout and independently recomputed coverage hashes are:

| shard | raw stdout SHA-256 | coverage SHA-256 |
|---:|---|---|
| 0 | 11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011 | AC1CB58FD8388DCE3469D5A58A59B3D5B6345FDCED14CA7F73C97066A22D7455 |
| 1 | 23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B | A1C932944A18A4B86A2B070D85D03115AD2287E78FEC0609EFCC3DFF09E6C570 |
| 2 | BFA5FEB83B620D5BA633066466FE826CB7FBE8D3938FB0484755857D1E5B4874 | AFE1979580158C5608EEB614E237D52A4BDF03B9679D1B18746618936A35789F |
| 3 | 3EDC9AB31B5D539503A54E21165D4F5DC599BD80DA75C897156D58DE27316868 | 6D409D5E044710737420FBCC37422A443D668D651F21524BF0F46AA46DBE72E6 |
| 4 | 8800A1407E7C3AC0906D166E7EC7789B4A3C4EC2BAC90E22A6FAA4E0194490DF | 5C859F80A980BD3D6D56B7EE872C7E174C71CC33640209AE2AB86373AB5959A0 |
| 5 | 4152DF07FCBFA6EFC70B8875085029B9A4A77ED740317B80225FC610B3A40FE4 | 3FBBA194ED75DE5E7357C0CEFE49A4D4077C3D866E2474ACE3A0A08154369067 |
| 6 | AAC9DDE7EF38F78AB89AA5F06380CD8ED7733EDA1C94A549188F51A28D190930 | 1B5E4FC6FF8B6B98CBF3148730229F04B2D42F2BD268800BE0B2D04F3D028404 |
| 7 | AC01F88A2F0C97DDDDA4D1B16008A8344BBC1FEE73D185A9EE41F5E2BF4009E4 | F71DABAC2FF827490A3609937DD2A15C5A9954103C7504830000D37F143AAFF9 |

All eight canonical stderr logs exist, contain zero bytes, and have
SHA-256 E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855.

The shard 0 and shard 1 replay stdout files are byte-for-byte identical
to their corresponding canonical stdout files. Their hashes are,
respectively,

    11487C524D7882A6DB6E631DFD43797E04C9EDE4EF87ED27AD86975189F75011
    23AF11878D1F31AEB68A9CAF7280932D8D3676DB5BA5376ED7609A0C6FB32A3B

Both replay stderr files exist and have the empty-file hash.

## 4. Per-row forests, margins, caps, and global union

Every one of the 1,830 rows independently satisfies

\[
 2(\mathrm{positive}+\mathrm{pruned})-\mathrm{boxes}
 =
 \begin{cases}
 16,&\mathrm{corner},\\
 128,&\mathrm{lower\ or\ open}.
 \end{cases}
\]

There are no zero-processed rows. Exactly 1,668 rows have no positive
leaf and carry the literal positive-infinity margin; all other margins
are finite and strictly positive. The largest per-case box count is
17,228 at shard 2, ordinal 2, \((f,n)=(4,4)\), open phase. The maximum
observed depth is 15. Thus every actual row lies strictly inside the
pinned limits of 500,000 boxes and depth 72.

Summing the row identities gives

\[
 2(22986+4176374)-8232800
 =165920
 =610\cdot16+1220\cdot128.
\]

The eight lists contain exactly 1,830 distinct keys; their sorted union
equals the independently reconstructed expected union, so there is no
cross-shard overlap or gap. Their pair projection contains exactly 610
distinct pairs.

The independently recomputed global result is

\[
 \boxed{
 \begin{aligned}
 \mathrm{pairs}&=610,& \mathrm{cases}&=1830,\\
 \mathrm{boxes}&=8232800,& \mathrm{positive}&=22986,\\
 \mathrm{pruned}&=4176374,& \mathrm{max\ depth}&=15.
 \end{aligned}}
\]

The minimum and global digests are:

    smallest = 2.144211613601797e-05
    coverage SHA-256 =
    B1C4A0B498CEFFBC211C2F1F6A8AC8F4D81164BA4B8C67E83E09B7FADED9AB01
    raw-log-set SHA-256 =
    9515F61976AE9D594B3725829AE6C40011199379F41810F8EBFC38470DC32140

## 5. Fail-closed checker audit

The accepted checker uses canonical ASCII unsigned-integer grammar,
permits only the literal token inf for infinity, rejects every nonfinite
numeric conversion, and requires each finite token to equal Python's
canonical string representation. It enforces depth at most 72, at most
500,000 processed boxes per case, exact positive infinity for a
zero-positive or zero-box disposition, the phase-specific forest roots,
and strict positivity of every accepted finite margin.

The remaining paths are also fail-closed:

- all four frozen hashes are checked before assignment reconstruction;
- missing, invalidly encoded, empty, or unterminated stdout fails;
- malformed, blank, or garbage content fails;
- CASE after PASS, duplicate PASS, missing PASS, and nonfinal PASS fail;
- missing, duplicated, reordered, extra, or changed CASE keys fail the
  exact ordered assignment;
- wrong residue, changed pair, and changed phase fail;
- every footer field and the coverage digest are recomputed;
- every canonical stderr is mandatory and empty;
- shard 0/1 replay stdout is mandatory and byte-identical, and replay
  stderr is mandatory and empty;
- final guards require 1,830 distinct keys, exact equality with the
  expected union, and exactly 610 pair projections before certification.

I exercised 50 independent negative mutations entirely in memory, without
writing over any evidence file. All 50 were rejected. They covered:

- each of the four source-pin mismatches;
- every missing/invalid/empty/unterminated and garbage/blank path;
- every PASS and CASE ordering, duplication, omission, and extra-row path;
- changed ordinal, \(f\), \(n\), phase, and residue;
- every checked footer field and the coverage digest;
- broken forest identity and every invalid margin/zero-box disposition;
- depth 999 and a consistent 500,002-box binary forest;
- both 1e309 and -1e309 overflow tokens;
- Unicode decimal digits, leading-zero integers, and noncanonical floats;
- all missing, mismatched, or nonempty stderr and replay paths.

In particular, the overflow, depth-999, and 500,002-box mutations that
reached the CERTIFIED line under the rejected checker all fail under the
accepted hash. As a positive control, an otherwise identical shard-3
ledger re-encoded with a UTF-16 big-endian BOM still certified.

## 6. Final checker run and durable transcript

I ran the accepted checker unmodified in a fresh subprocess. It exited 0,
emitted 2,666 stdout bytes with SHA-256

    682091821787EC985085DE42C09BD48EEDDD2AB1ABA8FB7B14075CAAD1DD593C

and emitted zero stderr bytes. Its final two lines were:

    PASS exact union: pairs=610; cases=1830; boxes=8232800; positive=22986; pruned=4176374; max-depth=15; smallest=2.144211613601797e-05; coverage-sha256=B1C4A0B498CEFFBC211C2F1F6A8AC8F4D81164BA4B8C67E83E09B7FADED9AB01; log-set-sha256=9515F61976AE9D594B3725829AE6C40011199379F41810F8EBFC38470DC32140
    CERTIFIED: all retained f>=4 no-drop phases form one exact exhaustive ledger

The durable transcript is UTF-16 LE with a BOM and CRLF newlines:

| artifact | bytes | SHA-256 |
|---|---:|---|
| no-drop-high-floor-shards/aggregate-final.log | 5,334 | 2E11E13CA0C00C39E09171CEDEDD8D31C5D4314DF68D1958AF7A0553F6BD09C6 |
| no-drop-high-floor-shards/aggregate-final.stderr.log | 0 | E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855 |

Decoding the durable stdout as UTF-16 reproduces the live checker stdout
character-for-character, including all ten CRLF line endings.

## 7. Resolution of earlier audits

The architecture audit left the following requirements before a global
PASS: eight completed shard footers, exactly 1,830 unique rows with exact
610-pair projection, per-row forest accounting, empty stderr, the
exhaustion-verifier pin, and encoding-aware parsing. Every requirement is
now met.

The preliminary checker audit identified two concrete defects:

1. the exhaustion verifier was not pinned;
2. a missing canonical stderr file was silently accepted.

Both are fixed. The exhaustion hash is checked before wrapper import, and
every canonical stderr path must exist and contain zero bytes. Shards 0
and 1 also have byte-identical pinned-source replay stdout and independent
empty stderr.

This final audit additionally rejected the intermediate checker because
of overflow-infinity, cap, and canonical-number defects. The 50-case
negative replay verifies that those defects are also closed.

## 8. Reproducibility under the planned low-floor core update

The accepted \(f\geq4\) chain deliberately pins the shared core at EEF8150E.
Replacing scripts/general_d_no_drop_compact_verify.py in place by the
planned two-line low-floor variant with hash 4AD4 would make the pinned
high-floor wrapper, helper, and aggregate checker refuse replay, as they
should.

For direct reproducibility of both certificates, the recommended layout is
to leave the EEF8150E core at its present path and check in the 4AD4
low-floor variant under a separately named low-floor path, with its own
wrapper, embedded pins, and audit. This preserves the already audited
import topology and allows the 1,830-row certificate to replay without
rewriting any accepted hash.

If the current core path must instead move to 4AD4, then first preserve an
exact EEF8150E snapshot together with versioned high-floor wrapper/helper/
checker entry points that import that snapshot, and independently replay
that versioned chain. Merely archiving the EEF8150E bytes without a runnable
pinned import path is weaker. The separate-path 4AD4 design is therefore
the cleaner option.

## 9. Original \(d=3\) and manuscript integrity

The original \(d=3\) artifacts remain:

| artifact | SHA-256 |
|---|---|
| manuscript/spherical-shell-polya-proof.tex | E456265C7E0C30A0EA0B56F1F8B9742548D2D6C0296671BD22EC60DF5AD19FD4 |
| manuscript/spherical-shell-polya-proof.pdf | FC5AFA529E7A797E89509C40F6BE05CD7BF4C61462FDDF826476F3CE7EA1C63F |
| manuscript/spherical-shell-polya-analytic-supplement.tex | 58C3D303BFE1B17A21CD31445FD6F8B52A52384817DBFDC2FEC4BA00CA3C3706 |
| manuscript/spherical-shell-polya-analytic-supplement.pdf | CD6974EA1E1FA9E61A7DFF21C664B175BB4CA0321240F5FDB3B22A1BD53BB294 |
| manuscript/spherical-shell-polya-supplement.tex | F6AB06BA835A8799082AE4832CD0B75B7AFE8FA810412FE5AA2170B03D197E4F |

No manuscript or production PDF was changed by this audit.

## 10. Verdict

**FINAL PASS.** For the accepted checker hash
79999E43B6D0CBC7BF29570F720FF5AE2FBFA4A986431D79F9716966426B7996,
the frozen exhaustion, exact 610-pair modulo-eight partition, all 1,830
phase rows, every per-row forest and margin condition, all footer and
digest checks, the global no-gap/no-overlap union, mandatory stderr, and
the shard 0/1 byte-identical replay evidence agree. The live checker and
durable transcript report exactly 8,232,800 boxes, 22,986 positive leaves,
4,176,374 pruned leaves, depth 15, minimum
\(2.144211613601797\times10^{-5}\), coverage digest B1C4...9AB01, and
log-set digest 9515...32140.
