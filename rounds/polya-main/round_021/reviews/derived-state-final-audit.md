# Round 21 Derived-State Final Audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

The seven regenerated state/manifest files and the new Round 21
post-promotion lifecycle test are consistent with the applied 60-node graph,
the final lemma judge, and the independent post-application audit. They
record the empty successor residual without promoting any higher theorem or
program obligation, preserve the exact certificate/analytic boundary and
failure chronology, and route the next work to a distinct Round 22 theorem
and non-tiling lifecycle.

This audit is bound to the exact file hashes listed below. Several scoped
files changed while the audit was in progress, so I discarded the earlier
snapshot, reread the final bytes, and reran the lifecycle and complete test
suites after the final hashes stabilized.

## Authenticated authority

The applied graph `state/proof_obligations.yml` has SHA-256

`a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`.

It parses as 60 obligations with 60 distinct ids and passes the canonical
graph validator. The following authoritative artifacts also retain the
expected bytes:

- final lemma judge: `a620175fc43591cd80fcc9f50165d7b21596b077d92fbc4450167d21a4eca9aa`;
- pre-application State Patch audit:
  `bcd67c3939892c4014026c0ebc5103033bdd33dc68f67082f7bd32ef8c0d84fa`;
- post-application audit:
  `c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef`;
- scoped closure candidate:
  `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d`;
- source-execution wrapper:
  `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`;
- wrapper tests:
  `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99`;
- domain addendum:
  `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241`;
- final A4 report:
  `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5`;
- cross-comparison:
  `7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a`;
- fresh referee:
  `d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28`;
  and
- provenance/isolation audit:
  `f4670818af3a57a965f0032edd72ea875d4ad618f9cc4a5b1b78cabdc7e481da`.

Commit `13e9534` is the one-time application commit. Revalidating the already
applied judge against the post-application graph correctly rejects its three
create operations as duplicates; the synchronized workflow explicitly says
not to rerun or reapply that patch.

## Exact graph state

The synchronized files reproduce the graph's only three Round 21 creations:

| obligation | status |
| --- | --- |
| `CERT-round21-compact-proxy` | `certified` |
| `CERT-round21-aggregate-tail` | `certified` |
| `SHELL-exact-d20-closure` | `proved_internal` |

No pre-existing status changed. In particular,
`SHELL-rho-compact-analytic-envelope` remains `proved_internal`, while
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` all remain `open`.

`COMP-certified-bessel` remains `diagnostic_only`. It no longer occurs as a
dependency, permitted dependency, or blocker of the compact/theorem/program
path, and it no longer implies `TARGET-shell-d3`. Its foundational and two
pilot regression links remain intact. The derived files accurately describe
this as detachment, not promotion or deletion.

The graph's top-level `round_selection` text still describes the historical
Round 19-to-20 orchestration. The final validation report and reading packet
explicitly identify it as historical metadata and route Round 22 by current
statuses and `next_action` fields instead. No synchronized workflow treats
that stale prose as current authority.

## Residual and face bookkeeping

Every scoped derived file records the accepted empty successor residual. The
mathematical boundary agrees with the graph and judge:

\[
\mathcal D_{20}=
\{\rho_c\leq\rho<39/50,\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.
\]

The exact guards are stated as

\[
\frac7{51}<\rho_c,
\qquad
k_{11}(\rho)>12\quad(\rho_c\leq\rho<1),
\]

with no current positive use of the false unrestricted extension to every
`rho>=rho_c`. The residual is split disjointly into `K<=200` and `K>200`,
with `K=200` assigned to the compact subtraction owner. The synchronized
proof draft additionally checks the exhaustive `U<200`, `U=200`, and
`U>200` cases. It preserves the outside status of `rho=39/50`, `K=k_11`,
and `K=U`, so none is subtracted twice. The resulting statement

\[
\mathcal D_{21}=\varnothing
\]

is therefore represented as an accepted lemma boundary, not as an automatic
full-theorem promotion.

## Certificate versus analytic scope

The synchronized files preserve the exact ownership boundary:

- the compact certificate has 10,580 exact rational leaves on the closed
  rectangle `7/51<=rho<=39/50`, `12<=K<=200`;
- the aggregate finite computation has 1,286 ratio boxes at the single base
  frequency `K=200`; and
- the universal tail for `rho_c<=rho<=39/50`, `K>=200` comes from the
  independent analytic derivative, curvature, and two-integration chain.

No synchronized file calls the aggregate boxes an all-frequency certificate,
uses either scoped certificate as Bessel-root isolation, or broadens the
legacy diagnostic parent. The reading packet also authenticates the final
source-execution route and limits predecessor audits to their unchanged
finite predicates under the final scope overlays.

## Failure chronology and provenance

The final validation report and reading packet retain the complete nine-step
negative chronology: initial isolation/quantification ambiguity; omitted
spectral bridge; implicit Machin branch; missing mutation/lifecycle tests; a
referee that missed that defect; the incorrect proof-free transcription; the
unrestricted `k_11>12` domain error; the resulting stale judge/audit; and the
loader that could hash `.py` while executing a timestamp-valid adjacent
`.pyc`.

The other derived files preserve the two decisive terminal defects and make
clear that superseded unscoped, stale-hash, and cache-vulnerable cycles are
negative chronology. They describe the accepted repair accurately: read and
hash the producer source bytes once, strict-decode and compile those same
bytes, execute without an import loader or cache, and require source
semantics under a deliberately conflicting timestamp-valid `.pyc`.

## Round 22 workflow, theorem scope, and non-tiling

The next workflow is a distinct theorem-level lifecycle. It requires a
frozen proof-free assembly packet, an independent scope/dependency audit, a
fresh clean-room reconstruction, a separate provenance audit, and a
different adversarial referee instructed to assume the theorem false. It
explicitly tests `K=0`, strict counting at eigenvalue walls, every ratio and
moving-frequency seam, `K=200`, and the global high-frequency wall.

The required normalization and scaling are stated correctly:

\[
L_3=\frac1{6\pi^2},\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),\qquad
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3),
\]

followed by `A_{r,R}=R A_{r/R,1}`, Dirichlet eigenvalue scaling by
`R^{-2}`, and volume scaling by `R^3`. These are pending assembly gates, not
claims that arbitrary shells have already been promoted.

The non-tiling scope is likewise calibrated. Existing geometry addresses
every bounded three-dimensional shell `0<r<R` under congruent rigid motions,
pairwise-disjoint interiors, and almost-everywhere coverage. The synchronized
workflow still requires a fresh adversarial geometry review and separate
program-scope audit. It also requires the final graph to represent the
non-tiling premise with a scoped proved obligation and explicit program
dependency instead of relying on prose alone. Ellipse and certificate-family
tracks remain outside the claim, and the limited literature search is never
called a novelty or priority certificate.

## Lifecycle test and reproduced validation

`computations/tests/test_round21_post_promotion_lifecycle.py` is read-only and
authenticates the applied graph and application audit. It verifies 60 unique
obligations, all three created statuses, the corrected guard, empty residual,
compact ownership of `K=200`, all four higher nodes remaining open, diagnostic
detachment, and synchronization markers in all seven derived files.

The final stabilized bytes passed:

- focused lifecycle test: 5 passed;
- complete repository suite: 339 passed, 1 strict expected xfail, and
  10 subtests passed in 154.26 seconds;
- graph validation: PASS;
- strict UTF-8 and C0/DEL scan: PASS for all 8 synchronized/lifecycle files;
- in-memory parsing of all 66 tracked Python files plus the new lifecycle
  test: PASS; and
- `git diff --check`: PASS.

The reproduced full-suite count agrees with
`state/last_validation_report.md`; wall-clock duration differs only because
runtime is non-deterministic.

## Audited final hashes

| file | SHA-256 |
| --- | --- |
| `state/current_state.md` | `9960f2f12faa3a2f240db3c341279376b60540c7eac43506fb551e6ce9db3c03` |
| `state/gap_register.md` | `1bbcf3b9ca8854c359bd1cc9964a686da8665d170991b913fcb40294c321f4b1` |
| `state/lemma_bank.md` | `eb537ddc06902a0a9b64168111fd2c169f38fa81936a6a139927257cec395c42` |
| `state/next_round_prompts.md` | `0fb336ae5aa9d49dba3d23bc5c2da7fe6e1b5c3eefce6d30ab3c486d2f3515b7` |
| `state/best_proof_draft.md` | `4f125df1fa5b698a140d5f573810b56b99db6c2a7e865748bf5afdee2f01bec0` |
| `state/last_validation_report.md` | `2f1a5bd1e8a92717a4a33a4b131c77ef21753828ad931ab7cc2b44317e428d9f` |
| `manifests/reading_packet.md` | `7442dd02bf94f5c61c2f4145551b8b90bddce82464bd06eba62d11b6419b3ea5` |
| `computations/tests/test_round21_post_promotion_lifecycle.py` | `70efa52d4d71cb32b490280e096912f1b723e5cd9cc332e829bc0e80226187e4` |

## Final determination

The regenerated state is an exact and appropriately conservative projection
of the applied Round 21 lemma graph. It neither loses the empty-residual
result nor converts it into an unaudited theorem/program promotion. No stale
domain claim, cached-bytecode route, certificate overreach, face-ownership
error, diagnostic dependency, validation mismatch, or Round 22 workflow gap
was found.

**Final verdict: PASS. First issue: none.**
