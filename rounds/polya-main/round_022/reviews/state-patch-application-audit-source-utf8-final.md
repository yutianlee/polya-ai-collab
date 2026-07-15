# Round 22 source-UTF-8 final State-Patch application audit

Date: 2026-07-15

## Verdict

**PASS. First issue: none.**

I audited the applied graph independently and read-only. I wrote only this
report; I did not edit or reapply `state/proof_obligations.yml`.

## Frozen authorities

- committed `HEAD` baseline graph: SHA-256
  `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`
  (241,363 bytes);
- final source-UTF-8 judge: SHA-256
  `8bf97553a3c5bbab3de741a5c8752dc29bd5b9d39ce8289079e744b80b0721a2`
  (29,037 bytes);
- independent pre-application audit: SHA-256
  `3d0952f7a0c3aac820427f90249e9f8d5ece5d6f20e1d0bdcc2e9af11f5adc69`
  (8,523 bytes); and
- applied graph: SHA-256
  `b17b173ef58b24548584a7124d1fb2f087a3d8bc90e2e6445f28903f820dfa29`
  (257,190 bytes).

The baseline bytes were obtained from
`git show HEAD:state/proof_obligations.yml`, not from the changed working-tree
file. All four hashes matched the named bytes.

## Independent one-time reconstruction

I strictly decoded the final judge as UTF-8, independently extracted its
last `State Patch` JSON block, parsed it, and checked the exact operation
cardinalities: one create, twelve updates, zero rejects, and six no-change
records. I then invoked `apply_state_patch` exactly once in memory on the
committed 60-obligation baseline, with `round_index=22` and

`judge_ref=rounds/polya-main/round_022/judge/judge-022-source-utf8-final.md`.

The reconstructed result had 61 unique obligations. Its result ledger was
exactly 1 create / 12 update / 0 reject / 6 no-change. The actual application
gave all thirteen created-or-updated objects the single timestamp
`2026-07-15T14:47:52`. After substituting only that realized common timestamp
for the fresh in-memory timestamp, the entire reconstructed top-level mapping
was exactly equal to the parsed current graph. There was no other tolerated
difference.

The only changed pre-existing objects were the twelve update IDs:

- `POLYA-program-target`;
- `SHELL-exact-d20-closure`;
- `SHELL-fixed-rho-high-energy`;
- `SHELL-lattice-count`;
- `SHELL-phase-enclosures`;
- `SHELL-rho-compact`;
- `SHELL-rho-compact-analytic-envelope`;
- `SHELL-rho-one-endpoint`;
- `SHELL-rho-uniformity`;
- `SHELL-rho-zero-endpoint`;
- `SHELL-sturm-liouville-completeness`; and
- `TARGET-shell-d3`.

The only created object was `SHELL-spherical-shell-nontiling`. Every other
pre-existing obligation and every non-obligation top-level graph field was
exactly equal to the committed baseline.

A second application was not attempted. Prevalidation of the same patch
against the current graph refuses it with the sole issue
`create entry duplicates existing obligation: SHELL-spherical-shell-nontiling`.
Thus the bytes agree with exactly one baseline application and the patch is
not silently second-applicable.

## Status, closure, and graph structure

All five relevant obligations are `proved_internal` with empty blockers:

- `SHELL-spherical-shell-nontiling`;
- `SHELL-rho-compact`;
- `SHELL-rho-uniformity`;
- `TARGET-shell-d3`; and
- `POLYA-program-target`.

For each of these five, `permitted_dependencies` is exactly equal to its
direct `dependencies`; every direct premise has a promoted or certified
status and the reciprocal `implies` edge; the three review roles are distinct;
and `review_independence` is `clean_room`.

The complete edge delta from the committed baseline is exact:

- dependencies added:
  `POLYA-program-target -> SHELL-spherical-shell-nontiling` and
  `TARGET-shell-d3 -> SHELL-sturm-liouville-completeness`;
- implications added:
  `SHELL-phase-enclosures -> SHELL-rho-compact`,
  `SHELL-lattice-count -> SHELL-rho-compact`,
  `SHELL-fixed-rho-high-energy -> SHELL-rho-compact`,
  `SHELL-sturm-liouville-completeness -> TARGET-shell-d3`, and
  `SHELL-spherical-shell-nontiling -> POLYA-program-target`;
- blockers removed:
  `SHELL-rho-uniformity -> SHELL-rho-compact` and
  `TARGET-shell-d3 -> SHELL-rho-uniformity`; and
- eleven permitted-dependency ledger entries added: the four exact premises
  of `SHELL-rho-compact`, the three exact premises of
  `SHELL-rho-uniformity`, the new Sturm-Liouville premise of
  `TARGET-shell-d3`, and the three exact premises of
  `POLYA-program-target`.

There were no other additions or removals in those four relation fields.
Every new dependency/implies pair is reciprocal. All dependency, implication,
blocker, and permitted-dependency references resolve to existing IDs. Both
the dependency graph and the implication graph are acyclic. The spectral and
geometry branches remain separate until their conjunction at
`POLYA-program-target`.

## Provenance and evidence

I resolved every evidence, clean-room-review, and adversarial-review path on
all thirteen created-or-updated objects: 212 distinct referenced paths exist.
I also rehashed all 33 embedded artifact-digest entries in the three objects
that gained `artifact_hashes`; these cover 21 distinct files, and every digest
matched.

On both `SHELL-spherical-shell-nontiling` and `POLYA-program-target`, the
corrected `program-target-scope-audit-replacement.md` is positive evidence.
The superseded scope audit, first judge, first State-Patch audit, failed UTF-8
replacement judge, and failed UTF-8 replacement audit occur only in the
negative bucket. The literature note remains inconclusive. The final judge
reference injected by application occurs only once: in the created geometry
node's inconclusive bucket.

The six declared no-change objects are byte-for-byte equal as parsed objects
to their committed-baseline versions:

- `COMP-certified-bessel`;
- `COMP-certified-bessel-pilot-round8`;
- `COMP-certified-bessel-pilot-round17`;
- `ELLIPSE-near-circular`;
- `CERT-certificate-family`; and
- `SRC-mathieu-ellipse`.

## Source encoding and canonical bytes

The final judge strictly decodes with exactly four `U+00F3` code points and
zero `U+8D38`. Of those four judge sites, the two State-Patch strings persisted
as changed graph fields are exact: the `POLYA-program-target` title and the
`TARGET-shell-d3` next action both contain `P` + `U+00F3` + `lya`. The other
two judge sites are explanatory or round-assessment text and are not graph
fields.

The decoded graph contains zero `U+8D38`. It has ten `U+00F3` occurrences in
total because other Pólya strings already existed in the historical graph.
Canonical `ensure_ascii=True` serialization represents all ten as the raw
escape `\u00f3`; the file contains no literal raw `U+00F3`. The on-disk bytes
are exactly `dump_graph(current_mapping)`: 257,190 bytes, 4,378 LF bytes,
zero CR bytes, and a terminal LF.

## Validator

`python -m math_collab.validate_state_patch --graph state/proof_obligations.yml`
returned:

`Graph OK: ...\state\proof_obligations.yml`

The direct `validate_graph(current, root=workspace)` call also returned an
empty issue list, and `git diff --check -- state/proof_obligations.yml`
reported no whitespace error.

## Final determination

**PASS. First issue: none.** The authoritative graph is the canonical,
one-time realization of the authenticated source-UTF-8 final judge. Its node
count, operation ledger, promotions, blockers, closure, relations, evidence,
negative chronology, encoding, and unchanged parallel tracks all match the
frozen application contract.
