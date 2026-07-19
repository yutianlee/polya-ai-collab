# Round 20 Candidate Final-Byte Audit

Verdict: **FAIL**.

First issue: **the released candidate is internally circular about whether
its bytes are frozen**.

The released packet is authenticated as
`state/lemma_packets/SHELL-combined-closure-round20-claim.md`, SHA-256
`80b7ec55d71b54cd93a821cb27703b399f13d5a0dedf7bcbaaf854235a779002`,
and the external freeze as
`rounds/polya-main/round_020/exploration/candidate-claim-freeze.md`, SHA-256
`71359b3dd0f6d49f496c7c2f5c6630a40f5b879e433a51b47095479cc2897950`.

## 1. Blocking release-coherence defect

The candidate status says **FROZEN CLAIM ONLY**, and the external freeze
says **FROZEN / RELEASED FOR ISOLATED REVIEW** and declares the candidate
bytes immutable. However, candidate lines 728--735 first list the isolated
analytic reconstruction and independent exact-constant audit as the first
two still-required reviews and then say:

> Until the first two release conditions are satisfied and an external
> freeze records this file's exact SHA-256, the bytes are a draft and may be
> corrected without constituting a replacement frozen candidate.

On the ordinary nearest-antecedent reading, those first two conditions are
the isolated analytic reconstruction and exact-constant audit. They have not
yet occurred; this release is what is supposed to authorize them. The
candidate therefore simultaneously says that the same bytes are frozen and
that they remain a mutable draft until after the reviews for which they are
being frozen. If the intended referents were instead the `k_11` source-scope
gate and root byte review, those referents were removed from this paragraph
during the release transition, leaving the condition undefined in the
released packet.

This is not a mathematical change, but it is a blocking proof-gate defect:
an isolated verdict cannot be credited against bytes whose own release rule
still calls them a mutable draft. Correction requires replacement candidate
bytes, an updated freeze with new hashes, and a repeated final-byte audit.

## 2. Exact transition reconstruction

No standalone copies of the two pre-freeze drafts remain in the workspace.
The exact release unified diffs do remain in the local orchestration record.
I reversed those diffs in memory, without writing a reconstruction. The two
reconstructed byte streams reproduce the independently audited draft hashes
exactly:

| reconstructed pre-freeze artifact | reproduced SHA-256 |
|---|---|
| candidate draft | `be5a9f5792495f5ede3a558f1e31e0c428efb3a34f6ef3008423693b90d59949` |
| freeze draft | `dd9d9fdaf47315abf72cbaeaa2e312874972ae7f8dd3eee57a0280f81528e0e3` |

The candidate transition has four release-only hunks: title/status, the
opening draft qualifier, the `k_11` gate/release prose, and the final review
list. The freeze transition changes title/status, opening release prose, the
candidate-hash row, and the release-rule block, and renames the draft freeze.
No formula, mathematical constant, domain, inventory, cap, source scope, or
falsification face changed. In particular, the normalization
`k_11(rho)<K<K_0(rho)=U(rho)` was already present in both independently
audited draft streams; it is not a release-time mathematical edit.

The independently audited pre-freeze report reproduces SHA-256
`819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467`.

## 3. Baseline, tables, and source boundary

The declared baseline resolves exactly to
`56e8d71ad3df2da6ab47ab1fefb8d758e076c69b`. The candidate contains 15
authenticated table rows and the freeze contains 16, for 31 occurrences and
16 unique paths. Every working-tree byte stream matches its displayed hash.
For all 15 pre-existing input paths, the blob at the declared baseline also
matches the displayed hash. The excluded `k_11` gate record was checked by
path and hash only; its working and baseline bytes both reproduce
`515b57f7ad4c34a277c781770a7b60945fd345558ce5d4f592439e83fbd1a333`.

The permitted boundary remains exactly the five residual artifacts, five
foundational packets, five qualified source cards, the four labelled DLMF
identity locations, and the stated elementary tools. The release introduces
no incumbent proof as an input. Round 20 exploration proofs, all four named
Round 20 zero-bound notes, incumbent responses, ledgers, scripts, reviews,
and judge drafts remain excluded. I did not open any excluded incumbent or
source proof.

## 4. Claim and face check

The mathematical transition itself is clean. `C20` still proposes exactly:

1. both components of `D_19^low` with the complete `rho=rho_0` fiber;
2. the genuinely new staircase
   `rho_c<=rho<7/8`, `k_6<K<=k_11`;
3. the optical subtraction piece
   `39/50<=rho<7/8`, `k_11<K<U`.

Consequently, conditional on the candidate's explicitly assigned proofs of
`k_11<U` and `U=K_0` on `rho_c<=rho<39/50`, the exact residual remains

$$
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

The `rho=rho_0` face belongs to the first lower component; `rho=rho_c` to
the high side; `rho=39/50` to the optical side; and `rho=7/8` lies outside
the live residual. The `k_6` face remains predecessor-owned, `k_11` is
staircase-owned, and `U` is excluded. Thus there is neither a face gap nor a
double subtraction. All lower, high, localization, optical, and
falsification tables are byte-identical to the audited draft. Their visible
multiplicity arithmetic is consistent, including the lower caps
`45,46,59,66,69,78`, the high sum-of-squares caps, and the cap-395 proxy.

## 5. Proof leakage and byte hygiene

The candidate still contains proposed statements and reconstruction
obligations only. The release prose adds gate metadata, not a spectral
derivation, root location, executable certificate, or review proof. The
external freeze explicitly excludes the pre-freeze audit and all other
reviews from A3.

Both released targets decode as strict UTF-8, use LF-only line endings, end
in a newline, and contain no BOM, forbidden control byte, Unicode control or
replacement character, tab, or trailing whitespace. Display-math delimiters,
`\\left`/`\\right`, raw braces, and every Markdown table row are balanced;
`git diff --check` is clean for both targets.

## Final decision

**FAIL; first issue: the released candidate's surviving lines 733--735 make
freeze status depend circularly on the first two reviews that the freeze is
intended to authorize.** All requested identity, mathematical-semantic,
source-boundary, face, table, leakage, and byte-hygiene checks otherwise
pass.
