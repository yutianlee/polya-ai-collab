# Round 20 Replacement Candidate Final-Byte Audit

Verdict: **PASS**.

First issue: **none**.

## 1. Replacement identity and exact diff

The replacement byte streams reproduce the requested identities:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |

The failed release is preserved exactly at
`87d30559dcaa90086ce5274f9a264412a912a2d2`. Its three relevant blobs
reproduce their recorded hashes:

| preserved artifact | reproduced SHA-256 |
|---|---|
| failed candidate | `80b7ec55d71b54cd93a821cb27703b399f13d5a0dedf7bcbaaf854235a779002` |
| failed freeze | `71359b3dd0f6d49f496c7c2f5c6630a40f5b879e433a51b47095479cc2897950` |
| failed final-byte audit | `ae7cd1b145e1cd22a2a023c68a35b619d9017c550e7b55d528cadb2e1b8f24a0` |

The direct Git diff from that commit has exactly the intended scope. The
candidate has one hunk: its three-line circular draft condition is replaced
by four lines saying that these exact bytes are frozen as an independent
review target, are neither proved nor promoted, and require new candidate,
freeze, and audit bytes after any correction. No other candidate line
changed.

The freeze has only two metadata hunks: the candidate authentication row is
updated to the replacement hash, and the lifecycle block records the failed
release, its failed audit, the exact replacement scope, and the requirement
for this new audit. Its theorem summary, residual authentication, permitted
input table, excluded-artifact list, and isolation rule are byte-identical to
the preserved release.

## 2. Baseline and authentication tables

The declared baseline resolves exactly to
`56e8d71ad3df2da6ab47ab1fefb8d758e076c69b`. The candidate contains 15
authenticated table rows and the freeze contains 16, for 31 occurrences and
16 unique paths. Every current byte stream matches its displayed hash. Every
one of the 15 pre-existing input blobs at the declared baseline also matches
the displayed hash.

The pre-freeze scope audit reproduces
`819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467`.
The excluded `k_11` gate record was authenticated by path and hash, without
opening its contents; both working and baseline bytes reproduce
`515b57f7ad4c34a277c781770a7b60945fd345558ce5d4f592439e83fbd1a333`.

## 3. Mathematical and face identity

Because the only candidate change occurs after every mathematical statement,
all constants, definitions, zero obligations, inventories, cap tables,
localization splits, optical constants, source qualifications, and mandatory
falsification faces are byte-identical to the failed release and to the
independently audited draft mathematics.

In particular, `C20` still proposes exactly:

1. closure of both components of `D_19^low`, including the complete
   `rho=rho_0` fiber;
2. the new staircase
   `rho_c<=rho<7/8`, `k_6<K<=k_11`;
3. the optical subtraction piece
   `39/50<=rho<7/8`, `k_11<K<U`.

Conditional on the explicitly assigned proofs of `k_11<U` and `U=K_0` on
`rho_c<=rho<39/50`, the proposed residual is unchanged:

$$
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

The `rho=rho_0` face remains lower-owned; `rho=rho_c` high-owned;
`rho=39/50` optical-owned; and `rho=7/8` outside the live residual. The
`k_6` face remains predecessor-owned, `k_11` staircase-owned, and `U`
excluded. The explicit `K_0=U` normalization was already present before the
first release. No face, set, constant, or table entry changed in the
replacement.

## 4. Isolation, leakage, and lifecycle coherence

The permitted input boundary is unchanged: the five residual artifacts,
five foundational packets, five qualified source cards, four labelled DLMF
identity locations, and stated elementary tools. Every Round 20 exploration
proof, all four named Round 20 zero-bound notes, incumbent response, ledger,
script, review, and judge draft remains excluded from the first isolated
reconstruction. The added lifecycle metadata reports only the failed gate
and replacement scope; it supplies no spectral derivation, zero location,
cap proof, Weyl payment, or theorem verdict. I opened no excluded incumbent
or source proof.

The prior circularity is removed. The candidate and freeze now agree that
the exact replacement bytes are immutable independent-review targets, not
proved or promoted claims, and that any correction requires a fresh
replacement cycle. This audit satisfies the freeze's final outstanding
authentication condition without making the candidate a theorem.

## 5. Byte hygiene

Both replacement targets decode as strict UTF-8, use LF-only line endings,
end in a newline, and contain no BOM, forbidden control byte, Unicode control
or replacement character, tab, or trailing whitespace. Display-math
delimiters, `\\left`/`\\right`, raw braces, and every Markdown table row are
balanced. `git diff --check` is clean for both targets.

## Final decision

**PASS; first issue: none.** The replacement fixes exactly the failed
release-coherence paragraph and updates only authentication/lifecycle
metadata in the freeze. All mathematical content, source and isolation
boundaries, tables, faces, and proof-free status are unchanged and
hash-authenticated.
