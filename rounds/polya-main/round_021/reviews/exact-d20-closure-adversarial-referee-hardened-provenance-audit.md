# Provenance Audit of the Hardened Exact-D20 Adversarial Referee

Date: 2026-07-15

## Verdict

**FAIL — provenance fidelity only.** First issue: the sealed report describes
the fresh reviewer as a **“context-free child task.”** The original reviewer
explicitly confirms that this wording is inaccurate: it was a fresh child
review, but it received an explicit surrounding assignment and artifact
corpus. A fresh child is not thereby context-free. Because this audit was
asked to ensure that the lead transcription adds no unsupported provenance
claim, that false strengthening is sufficient for FAIL.

No mathematical counterexample, certificate-count mismatch, hash mismatch,
scope leak, or concealed authorship was found. The report correctly and
prominently states that the child completed and handed off the review but did
not write the sealed bytes; the lead transcribed them after the child's
file-write turn stalled. The original reviewer independently confirmed that
provenance fact and confirmed that the core PASS mathematics, execution
counts, branch hardening, exact faces, and finite-A4/all-\(K\)-A3 boundary
faithfully reflect its completed findings and spectral/compact subreview.

The current report must nevertheless be replaced, not treated as a clean
fresh-referee artifact, because of the inaccurate `context-free` claim and
the additional handoff omissions catalogued below.

## Audited bytes and authorship

The audited file is
`rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-hardened.md`.
Its observed raw identity is:

| bytes | SHA-256 |
|---:|---|
| 7,770 | `61366c3dd126790b9a80fa21744a939e9e7f4ab098986faf7ffd14d6c28d2747` |

It was created against clean committed baseline
`9942cfed3fc3a80efdee3122e6c348d7d7f22124`, exactly as the report says.
At audit start it was the only untracked file.

The original reviewer at canonical path
`/root/round21_a3_clean_room/round21_fresh_referee_hardened` supplied a direct
provenance comparison. It confirmed all of the following:

- the sealed file was transcribed by the lead and was **not** written by the
  fresh child;
- the child's review had completed with PASS before its artifact-write turn
  stalled;
- a separately delegated spectral/compact subreview was used;
- the report's central mathematics, counts, hashes, branch-before-\(\pi\)
  ordering, active mutations, face logic, and scope boundary match the
  completed handoff; and
- the report adds no unsupported mathematical conclusion.

Thus the report does not conceal its actual byte authorship. Its opening
provenance disclosure is materially honest except for the adjective
`context-free`. The accurate description is: *a fresh child review given an
explicit assignment and artifact corpus, with a separately delegated
spectral/compact subreview; the lead later transcribed the completed handoff.*

## Hash audit

Every full current hash printed in the report matches the corresponding raw
file:

| role | observed and reported SHA-256 |
|---|---|
| residual packet | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| residual freeze | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| residual audit | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |
| exact-D20 candidate | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| compact contract | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| aggregate contract | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| replacement candidate freeze | `75afe7f0ea6ca2da4106510f6e90fb64a13a83fd83f023361d3433493d64558c` |
| replacement isolation audit | `d4aaf2676c9056721b919f5b24341e39e77178b27a49bfaa5b54a8e77eb6c57e` |
| hardened A4 wrapper | `4868dcc3251fe30aff4d8ef362cdd8924fe69d95cafa8d597fa9c88560780ff8` |
| hardened A4 tests | `6716ff1beaaf4053092f8e7baa4d77b95acf38f3fc3d467f15ec76e545271da7` |
| hardened A4 report | `d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56` |
| replacement cross-comparison | `e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e` |

The shortened compact identities expand correctly to:

- verifier `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856`;
- tests `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36`;
- report `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293`;
  and
- adversarial audit `aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca`.

The shortened aggregate identities expand correctly to:

- route `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0`;
- verifier `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952`;
- tests `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91`;
- report `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6`;
  and
- adversarial audit `aa12d25d71091cfd01a116bc2777afa8669248a13441be391cf3da0b48c9a894`.

No printed digest is false. The transcription is incomplete, however: its
authentication section omits the A3 clean-room report and typography
addendum, even though the all-frequency analytic chain is part of the
reviewed proof. Their current hashes are respectively
`0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc`
and
`d003d105038e78a0b95137b9fecb0ca5758a804dac17cbea1e6eea155f50b257`.

The lifecycle section also abbreviates rather than records the full hashes
of the preserved branch-gap, strict lifecycle FAIL, initial referee, and
initial-referee miss:

- `3d234405e5776b31dea29fbff8ee2803d0f54052cab851240b81546e9ac1b7f2`;
- `11672110bdc1169c40b46247832c19b9187df3112ab67f28324f6784a2f552a6`;
- `0466a240861de32b60819f9a5cd3b48106b230839c3fae07f4f67cbd59588e74`;
  and
- `af1761a2426ad22f2cf93ea765e3b98af1314f4587730b654ed4eb36e37106ba`.

These are omissions, not hash contradictions.

## Execution-count fidelity

Every execution count in the sealed report matches the completed handoff and
current certificate schemas:

| item | reported | independent check |
|---|---:|---:|
| compact leaves at each precision | 10,580 | 10,580 |
| compact Arb/integer comparisons | 2,153,076 | 2,153,076 |
| compact focused tests | 5 | exactly five test functions; child confirmed all passed |
| aggregate ratio boxes | 1,286 | 1,286 |
| aggregate finite signs | 14,146 | \(1{,}286\times11\) |
| aggregate endpoint containments | 2,572 | \(1{,}286\times2\) |
| high-precision derivative points | 1,286 | one per ratio box |
| exact set sign rows | 243 | \(3^5\) |

The 256- and 384-bit compact digest statements are also faithful, as are the
four branch mutations and the explicit CLI scope markers. No execution result
from either superseded A4 cycle is presented as current evidence.

## Mathematical and scope fidelity

No unsupported mathematical implication was introduced by the lead
transcription.

### Compact/spectral subreview

The report's derivative

\[
\partial_aG_a(\nu)=\pi^{-1}\sqrt{1-\nu^2/a^2}
\]

is exactly the accepted
\(\sqrt{a^2-\nu^2}/(\pi a)\) formula for \(a>\nu\). The strict separated
count, zero extensions, strict integer-wall convention, monotone corner
orientation, Weyl direction, and half-open tiling give exactly

\[
N_D\leq P_{\rm coarse}\leq\widehat P_B<W_{B,-}\leq W.
\]

The spectral/compact child directly confirmed that this section faithfully
records its subreview.

### Aggregate proof and A3/A4 boundary

The low-tail identities, strict shelf sum, interface loss, and implications

\[
\mathcal Q\geq0\Longrightarrow N_D<W,
\qquad
\mathcal B\geq0\Longrightarrow\mathcal Q>0
\]

are correct at \(\tau=0\), half-integer \(\mu\) walls, integer
\(K\eta_\rho\) walls, and \(\rho=1/2\). The displayed universal curvature
chain is also correct:

\[
I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}\leq\frac{3b}{800},
\qquad E_{KK}>0,
\qquad \mathcal B_{KK}>F(\rho).
\]

Crucially, the report preserves the contract boundary: outward boxes prove
only the finite \(K=200\) base predicates; A3 supplies the universal
derivatives and two integrations for all \(K\geq200\). It does not promote a
finite replay into an all-frequency proof.

For full fidelity to the child's completed reconstruction, however, a
replacement should display rather than merely assert the omitted exact
\(I_K\), \(\mathcal B_K\), and \(\mathcal B_{KK}\) formulas and should give
the full \(\mathcal Q\) and \(\mathcal B\) identities. Their omission does
not make the implications false, but it makes the lead transcription less
self-contained than the handed-off review.

### Branch, guards, and exact faces

The branch-before-\(\pi\) validation, four active mutations, noncircular
\(\arctan(1)\) integral, tangent injectivity, and exact deductions
\(7/51<\rho_c\) and \(k_{11}>12\) are faithful. The exact owner split at
\(K=200\), all three orderings of \(U\) relative to 200, excluded residual
faces, and empty proposed successor likewise match the candidate and the
child's findings. The report appropriately states that the empty successor is
not itself a State Patch or promotion.

## Lifecycle omissions

The report's negative chronology is true but incomplete. The completed
handoff also retained two earlier failure/repair sequences that the lead
transcription omits:

1. The first candidate-isolation audit rejected the ambiguous finite
   \(K=200\)/universal-\(K\) contract, at SHA-256
   `601aa805838a683b5e440de11766eccc09a73b97112fd93d389427c84daaaf73`.
   The current replacement isolation audit is the later PASS already listed
   by the report.
2. The initial aggregate-route audit FAIL and its replacement PASS are
   preserved at
   `089f597cb3dca872073a0fd0b49852b16c1964c80aaadb2615ccc392259ab9fa`
   and
   `2db756ac182429f82263766b83038f39a88c0c1e9463fc095ffd9b56df82218d`,
   respectively.

Those omissions do not revive either repaired defect, but a report claiming
to seal the completed handoff should include them.

## Required replacement

Preserve the current report as a failed transcription cycle. A replacement
should:

1. replace `context-free child task` by the accurate fresh-child provenance;
2. continue to state explicitly that the lead, not the child, wrote the
   report bytes;
3. add the omitted candidate-isolation and aggregate-route failure/repair
   chronology;
4. add the A3 report/addendum identities and full preserved-review hashes;
5. include the exact omitted aggregate derivative and reserve formulas; and
6. obtain direct confirmation from the original child that the replacement
   is a faithful transcription.

The residual, candidate, contracts, A3 proof, hardened A4 implementation,
sealed compact/aggregate certificates, and exact-D20 mathematical verdict do
not require changes.

**Final verdict: FAIL. First issue: unsupported `context-free` provenance
claim. Mathematical fidelity otherwise passes.**
