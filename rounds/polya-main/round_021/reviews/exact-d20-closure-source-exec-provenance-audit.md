# Round 21 Exact-D20 Final Source-Execution Provenance Audit

Date: 2026-07-15

Role: independent final provenance and isolation audit

## Verdict

**PASS. First issue: none.**

The final scoped candidate, wrapper, tests, A4 report, A3 domain addendum,
cached-bytecode failure record, cross-comparison, and fresh referee all
reproduce their supplied SHA-256 identities. The live manifest authenticates
the scoped packet and excludes its rejected predecessor. The final loader
binds the bytes hashed to the bytes compiled and executed, the current tests
close the timestamp-cache and loader-state attacks, the positive reports
agree on every mathematical and computational boundary, and the failed
cycles remain explicit negative chronology.

This report completes only the final source-execution provenance gate. It
does not apply a State Patch or promote any proof obligation. A replacement
judge and a new independent State Patch audit must still authenticate the
final bytes before one-time application.

## Authenticated corpus

Every supplied identity was independently recomputed from the current raw
file bytes:

| role | path | bytes | reproduced SHA-256 |
| --- | --- | ---: | --- |
| scoped candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md` | 5,714 | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| final wrapper | `computations/round21_verify_exact_d20_closure.py` | 55,831 | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` |
| final tests | `computations/tests/test_round21_verify_exact_d20_closure.py` | 18,933 | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` |
| final A4 report | `rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-source-exec-replacement.md` | 9,185 | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` |
| A3 domain addendum | `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-domain-addendum.md` | 8,008 | `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241` |
| cached-bytecode FAIL | `rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-domain-addendum.md` | 5,085 | `d9a8fd94b1e730a324cfc3b0f518fc00cb65113ec1a0f80fc4bc1cb547c6c4d3` |
| final cross-comparison | `rounds/polya-main/round_021/reviews/exact-d20-closure-source-exec-cross-comparison.md` | 16,939 | `7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a` |
| fresh source-exec referee | `rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-source-exec.md` | 13,741 | `d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28` |

The working tree was clean before this audit report was created.

## Candidate isolation and semantic delta

The 191-line scoped packet is self-contained for the operative Round 21
claim. It supplies the definitions, exact D20 residual, compact and aggregate
theorem domains, corrected guard proof, exact counterexample to the omitted
upper wall, subtraction owners, face rules, evidence-role boundary, and
nonpromotion rule. Its references to the old packet are solely supersession
and negative chronology; it imports no theorem from the rejected
quantifier.

The replacement is a concise rewrite rather than a one-line textual patch,
but comparison with the 333-line predecessor finds only one mathematical
change:

\[
k_{11}(\rho)>12\quad(\rho\geq\rho_c)
\quad\longrightarrow\quad
k_{11}(\rho)>12\quad(\rho_c\leq\rho<1).
\]

All operative definitions, theorem rectangles, residual walls, strict
frequency inequalities, `K=200` ownership, three possible orderings of
`U(rho)` with 200, and proposed empty successor are preserved. The additional
prose makes the scope defect and its evidence disposition explicit; it does
not introduce a second theorem, certificate, face, status, or program claim.

The corrected proof is exact. On `rho_c<=rho<1`, both denominators are
positive and

\[
0<1-\rho\leq1-\rho_c,
\qquad
z_\rho\geq\frac{\pi}{1-\rho_c}=\pi+\frac12>\frac72,
\]

so `k_11(rho)^2>577/4>144`. The wall `rho<1` is necessary: `rho=1` is
singular, while `rho=2` gives

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Every D20 point already has `rho<39/50<1`, so this correction changes no D20
point or implication.

## Manifest and authenticated source execution

An isolated direct-source bootstrap of the final wrapper independently
returned:

```text
manifest_count=18
scoped_in=True
old_in=False
all_exact=True
guard=rho_c<=rho<1
```

The manifest binds the scoped packet at `d8cf6427...`; the old packet at
`41554615...` is absent. All 18 current manifest paths exist and reproduce
their exact declared hashes. The manifest validator also enforces path-set
equality, case-fold uniqueness, repository containment, and SHA-256 syntax.

For each sealed producer, `_load_hash_gated_module` reads one source payload,
hashes that buffer, strict-decodes those bytes as UTF-8, compiles that exact
image with `dont_inherit=True` and `optimize=0`, registers a fresh
`ModuleType`, and executes the resulting in-memory code object. No import
loader or cache lookup occurs. On definition failure it restores all three
prior `sys.modules` states: absence, a module object, or a `None` sentinel.

The exact source delta from the rejected cache-vulnerable wrapper is confined
to replacing `SourceFileLoader` with this direct authenticated-source path.
The mathematical producers, formulas, classifier, finite data, and precision
gates are untouched. The tests add lifecycle and quarantine checks without
changing a proof algorithm.

## Test and replay consistency

The final focused file contains exactly 14 tests. It covers:

- scoped-manifest inclusion, rejected-packet exclusion, all-input mutation,
  and missing/extra manifest entries;
- an explicitly timestamp-mode malicious `.pyc` with equal source size and
  restored mtime, proving that authenticated source behavior is executed;
- exact restoration of every prior module-registration state on failure;
- the corrected guard, the exact `rho=2` counterexample, and rejection of
  the old CLI wording; and
- all inherited compact, aggregate, exact-set, precision, branch, and scope
  mutations.

A secondary independent run of the final focused file returned **14 passed
in 113.36 seconds** and left the working tree clean. The authenticated A4
report records 14 passed in 149.15 seconds, while the fresh referee records
14 passed in 111.23 seconds. These differing wall times are expected; the
test count and outcomes agree exactly.

The A4 report records the complete repository result as **334 passed,
1 xfailed, 10 subtests passed**. The cross-comparison accurately labels that
as authenticated recorded evidence rather than claiming to rerun it, and
the fresh referee likewise does not claim a duplicate full-suite run. No
report inflates a recorded run into an independent reproduction.

The authenticated wrapper output agrees verbatim across the A4 report,
cross-comparison, and fresh referee on:

- 18 authenticated inputs;
- the guard `rho_c<=rho<1`;
- 243 exact sign rows and proposed empty D21;
- 10,580 compact leaves and 2,153,076 floor comparisons at both precisions;
- compact digests `96e527b4...` at 256 bits and `c6deaf2c...` at 384 bits;
- 1,286 aggregate boxes, 14,146 sign checks, and 2,572 endpoint checks; and
- 1,286 high-precision derivative-consistency points.

## Referee provenance, independence, and agreement

The fresh referee was written directly by the distinct child reviewer
`round21_fresh_referee_hardened`. Its completion record reported the exact
path and SHA-256 `d005e8c3...` and stated that only the assigned file was
added. Commit `8546597` subsequently adds exactly that file; no lead
transcription or stalled-write handoff intervenes in this cycle.

The referee's authenticated corpus lists the candidate, wrapper, tests, A4
report, A3 addendum, and negative cached-bytecode record. It neither lists
nor cites the cross-comparison. It independently reconstructs the guard and
D20 split, attacks the one-read loader, UTF-8 failure, optimization level,
module registration/restoration, and malicious timestamp cache, reruns all
14 focused tests, and reproduces the proof-bearing wrapper output. This is
substantive adversarial independence rather than agreement by inheritance.

The cross-comparison was sealed earlier in commit `9d28eaa`. Its PASS and
the later referee PASS agree on the corrected domain, source-to-execution
binding, finite-versus-analytic boundary, exact D20 faces, evidence
quarantine, and absence of higher promotion. The cross-comparison's statement
that the fresh referee was still pending is correct historical tense at its
creation, not a current discrepancy.

## Negative chronology and quarantine

The chronology is explicit and monotone:

1. the first A4 lineage `d9def12c...` is negative because it printed the
   unrestricted guard;
2. the scoped lineage `55f4f574...` is negative because wrapper
   `64854c95...` could execute a timestamp-valid unauthenticated cache and
   its `-B`/`py_compile` claim was false;
3. cached-bytecode report `d9a8fd94...` remains the authoritative FAIL for
   that precise cycle and is not rewritten;
4. the final wrapper/tests/A4 trio is
   `31130de2...` / `4de93001...` / `47cd9467...`;
5. the final cross-comparison and fresh referee authenticate only that final
   trio and the scoped candidate.

The A3 domain addendum remains positive for its independent denominator and
D20-domain proof. Its discussion of then-current wrapper/test hashes
`64854c95...` / `c9747c8c...` is explicitly stale execution chronology and
is not used to authenticate the final loader. Older candidate, A4,
cross-comparison, referee, provenance, judge, and State Patch audit bytes are
likewise quarantined from current application authority.

Two already-identified mojibake glyphs in historical prose do not affect a
formula, hash, command, output, scope, or provenance assertion. They are
nonblocking typography.

## Certificate boundary, faces, and nonpromotion

The compact producer and tests remain fixed at `2a436116...` and
`29b7425c...`; their executable scope is exactly the 10,580-leaf closed
rectangle `[7/51,39/50] x [12,200]`. The aggregate producer and tests remain
fixed at `fc48425c...` and `50f10033...`; their executable scope is exactly
the 1,286 outward base boxes at `K=200`.

A4 certifies only finite base predicates. A3 retains ownership of both
spectral bridges and the universal derivative, curvature, and two-integration
propagation for every `K>=200`. The output marker
`analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED` enforces that boundary.

The exact classifier retains the D20 faces:

- `rho=rho_c` is included subject to both strict frequency inequalities;
- `rho=39/50`, `K=k_11(rho)`, and `K=U(rho)` are excluded;
- `K=200` is covered by both theorem domains but uniquely compact-owned; and
- the cases `U<200`, `U=200`, and `U>200` are exhaustive.

Thus `D20=C21 dot-union T21` and proposed D21 is empty without omission or
double subtraction.

No reviewed artifact performs a State Patch. The live graph still records
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` as `open`, and `COMP-certified-bessel` as
`diagnostic_only`. No scaling, tiling, novelty, or broader theorem claim is
made.

## Final determination

The final source-execution lifecycle is isolated, authenticated, internally
consistent, independently reviewed, and provenance-complete for submission
to a replacement lemma judge. Failed and superseded cycles remain negative
evidence and cannot authorize application.

**Final verdict: PASS. First issue: none.**
