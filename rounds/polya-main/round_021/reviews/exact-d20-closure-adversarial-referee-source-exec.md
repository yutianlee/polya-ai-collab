# Round 21 Exact-D20 Closure: Fresh Adversarial Source-Execution Referee

Date: 2026-07-15

## Verdict

**PASS. First unsupported implication: none.**

I treated the repaired exact-D20 claim and the final A4 execution claim as
false until independently reconstructed.  The ratio guard is valid exactly
on `rho_c<=rho<1`, every point of D20 lies in that domain, and the exact
compact/aggregate subtraction still empties D20.  The final loader also
closes the cached-bytecode defect: the bytes that pass SHA-256 are the only
repository producer bytes decoded, compiled, and executed.

This verdict is limited to the final Round 21 exact-D20 evidence cycle.  It
does not apply a State Patch or promote a compact, uniformity, shell-theorem,
program, scaling, novelty, or tiling claim.

## Authenticated review corpus

The following identities were reproduced before and after the adversarial
replays:

| role | path | SHA-256 |
| --- | --- | --- |
| scoped candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md` | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| final source-exec wrapper | `computations/round21_verify_exact_d20_closure.py` | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` |
| final source-exec tests | `computations/tests/test_round21_verify_exact_d20_closure.py` | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` |
| final A4 report | `rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-source-exec-replacement.md` | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` |
| A3 domain addendum | `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-domain-addendum.md` | `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241` |
| cached-bytecode FAIL handoff | `rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-domain-addendum.md` | `d9a8fd94b1e730a324cfc3b0f518fc00cb65113ec1a0f80fc4bc1cb547c6c4d3` |

The wrapper authenticates exactly 18 inputs.  Its manifest contains the
scoped candidate and does not contain the rejected unscoped candidate.  The
compact and aggregate producer hashes remain respectively
`2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856`
and
`fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952`.

## Independent reconstruction of the exact guard

Because `pi>0`,

\[
0<\rho_c=\frac1{1+2\pi}<1.
\]

Assume exactly `rho_c<=rho<1`.  Then both denominators are positive and

\[
0<1-\rho\leq 1-\rho_c.
\]

Taking reciprocals reverses that positive order; multiplying by positive
`pi` preserves it.  Hence

\[
z_\rho=\frac{\pi}{1-\rho}
\geq \frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72.
\]

The last strict inequality uses the independently exact lower enclosure
`pi>3`.  Therefore

\[
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132
=\frac{577}{4}>144,
\]

so

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).
\]

The upper wall cannot be dropped.  At `rho=1`, `1-rho=0`, so `z_rho` and
the displayed definition of `k_11` are undefined.  At `rho=2`,

\[
z_2=-\pi,
\qquad
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Thus `k_11(2)<12`, an exact counterexample to the rejected quantifier
`rho>=rho_c`.  The other exact guard is also unchanged: `pi<22/7` gives
`14*pi<44`, hence `7/51<rho_c` after taking positive reciprocals.

Every D20 point obeys

\[
\rho_c\leq\rho<\frac{39}{50}<1.
\]

The repaired guard therefore applies to every point where the exact-D20
argument uses it, including the included face `rho=rho_c`.  It adds no point
to and removes no point from D20.

## Independent reconstruction of the split

For an accepted residual point,

\[
\frac7{51}<\rho_c\leq\rho<\frac{39}{50},
\qquad
12<k_{11}(\rho)<K<U(\rho).
\]

Define

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

These owners are disjoint and exhaustive.  A point in `C21` lies in the
compact rectangle `[7/51,39/50] x [12,200]`; a point in `T21` lies in the
aggregate domain `rho_c<=rho<=39/50, K>=200`.  The shared theorem face
`K=200` is subtracted exactly once by the compact owner.  This remains true
for `U<200`, `U=200`, and `U>200`.

The inherited faces are unchanged: `rho=rho_c` is included subject to the
strict frequency walls, while `rho=39/50`, `K=k_11(rho)`, and `K=U(rho)`
are excluded.  Hence

\[
\mathcal D_{20}=\mathcal C_{21}\mathbin{\dot\cup}\mathcal T_{21},
\qquad
\mathcal D_{21}=\varnothing.
\]

## Source-execution attack

The failed wrapper first hashed a `.py` path and then asked a
`SourceFileLoader` to execute that path.  A timestamp-valid `.pyc` could
therefore be executed even though only the source was authenticated.  The
final `_load_hash_gated_module` does not use an import loader:

1. `Path.read_bytes()` obtains one in-memory payload.
2. SHA-256 is computed over that payload and compared with the manifest.
3. Those same bytes are strict-decoded as UTF-8.  No replacement or fallback
   decoding is allowed.
4. The resulting uniquely determined text is compiled with the authenticated
   filename, `dont_inherit=True`, and `optimize=0`.
5. A fresh `ModuleType` is registered in `sys.modules` before execution; its
   loader, spec, and cache fields are `None`.
6. The compiled code object is executed directly.  No cache path is queried.
7. On any `BaseException` during execution, an absent entry is removed and a
   prior module object or prior `None` sentinel is restored exactly.

The single-read property is substantive: after the byte read, neither the
hash, decoder, compiler, nor executor reopens the source path.  A concurrent
change to that path cannot change the code object made from the authenticated
payload.

I attacked this path independently in addition to running the committed
tests:

| attack | fresh result |
| --- | --- |
| a path object that raises on a second `read_bytes()` call | one read; authenticated source executed |
| valid non-ASCII UTF-8 source | exact Unicode value executed |
| invalid UTF-8 with its own correct SHA-256 | rejected before module registration |
| host interpreter launched with `-OO` | loaded probe still had `__debug__=True`, proving `optimize=0` |
| code that inspects `sys.modules[__name__]` during definition | observed its own registered module |
| execution failure with prior state absent, module object, or `None` | all three states restored |
| equal-length authenticated source plus malicious timestamp cache | source behavior executed; cache ignored |

The malicious-cache regression explicitly requests
`PycInvalidationMode.TIMESTAMP`, verifies header flags zero, changes the
equal-length source while restoring the recorded mtime, and confirms that
the cache still exists while the source value is returned.  It therefore
remains a timestamp attack even when `SOURCE_DATE_EPOCH` is set.  The test
deletes its explicit cache sentinel in `finally`.

The previous `-B` error is not repeated.  `-B` suppresses normal cache
writes, not reads, and explicit `py_compile` can still write.  The repaired
proof rests on direct source compilation, not on treating `-B` as a read
barrier.

## Top-level wrapper and isolated tests

The proof replay did not import the top-level wrapper with `python -m`.  A
`python -I -B -` stdin bootstrap read the wrapper once, required SHA-256
`31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`,
strict-decoded and compiled that payload at optimization zero, registered a
uniquely named module with the authenticated absolute `__file__`, and called
`main(["--high-precision", "384"])`.  Adjacent wrapper bytecode was never on
that execution path.

For pytest, isolated mode initially excluded the repository from `sys.path`.
Plugin autoload was disabled, installed pytest was imported first, and only
then was the absolute repository root inserted.  Each run used a fresh
empty `-X pycache_prefix=...`, `-B`, and `-p no:cacheprovider`.  The wrapper
and test hashes were checked before collection.  The fresh cache prefix held
zero files after both collection and execution; the malicious test's
explicit timestamp cache was also removed.  Standard-library, pytest,
python-flint, and other installed runtime code remain trusted host software,
not repository proof artifacts.

## Independent reproductions

The direct source/encoding/optimization sentinel returned:

~~~text
SOURCE_EXEC_SENTINEL PASS
host_optimize=2 compiled_probe_debug=True
single_read_count=1 utf8_strict=True registered_before_exec=True
invalid_utf8_rejected=True loader_spec_cache_none=True
~~~

With `SOURCE_DATE_EPOCH=1`, the isolated targeted loader/domain selection
returned:

~~~text
isolated_pytest_bootstrap=True
source_date_epoch=1
....                                                                     [100%]
4 passed, 10 deselected in 0.54s
fresh_pycache_files_after=0
~~~

The complete focused file was then run through the same isolated source
path:

~~~text
isolated_pytest_bootstrap=True
..............                                                           [100%]
14 passed in 111.23s (0:01:51)
fresh_pycache_files_after=0
~~~

The authenticated top-level source bootstrap reproduced the proof output in
the final A4 report exactly:

~~~text
ROUND21_EXACT_D20_CLOSURE_A4 PASS
authenticated_inputs=18
exact_constants=PASS (7/51<rho_c and k11(rho)>12 for rho_c<=rho<1)
exact_set=PASS (243 sign rows; D20=C21 disjoint-union T21; proposed D21 empty)
compact[256]=PASS leaves=10580 floor_comparisons=2153076 digest=96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631
compact[384]=PASS leaves=10580 floor_comparisons=2153076 digest=c6deaf2c1a7e9df78760d61414c59ee48a16b0ed621266b2de40a29aea1946f6
aggregate_base_K200[192]=PASS boxes=1286 sign_checks=14146 endpoint_checks=2572 derivative_points=0
aggregate_base_K200[384]=PASS boxes=1286 sign_checks=14146 endpoint_checks=2572 derivative_points=1286
aggregate_scope=finite outward predicates at K=200 only
analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED
~~~

The final A4 report also records the isolated full repository regression as
`334 passed, 1 xfailed, 10 subtests passed`.  I did not duplicate that
repository-wide diagnostic; the proof-bearing wrapper replay and all 14
focused tests were independently rerun here.

## Analytic and certificate boundary

The source-execution diff changes the loader and its regression tests, not a
mathematical producer.  In particular, it changes no `Q` or `B` formula, no
`I_KK`, `E_KK`, `B_K`, or `B_KK` derivative, no compact leaf, no aggregate
box, and no exact face-classifier rule.  The unchanged producer hashes and
the reproduced digests/counts independently confirm that boundary.

The compact executable still owns its 10,580 finite leaves on the closed
rectangle.  The aggregate executable still owns only 1,286 outward boxes and
the finite predicate family at `K=200`.  A3, not A4, owns the derivative,
curvature, and two-integration propagation to every `K>=200`.  The wrapper's
`A3_REQUIRED_NOT_CLAIMED` marker correctly refuses to relabel the finite
certificate as that universal argument.

The A3 domain addendum at SHA-256 `395238c6...` remains valid for the exact
denominator and D20-domain reconstruction.  Its section authenticating old
wrapper/test hashes `64854c95...` and `c9747c8c...` is now stale execution
chronology and is not used as evidence for this verdict.

## Failed-cycle closure and chronology

The cached-bytecode referee handoff at SHA-256 `d9a8fd94...` remains correct
negative evidence against wrapper `64854c95...` and A4 report `55f4f574...`.
Its replacement requirements are met as follows:

1. one source-byte read: met;
2. hash of that exact payload: met;
3. fixed-filename, fixed-optimization compilation of the strict UTF-8 image
   of that payload: met;
4. fresh registered `ModuleType` and direct execution without a loader: met;
5. correction of the false `py_compile -B` claim: met;
6. malicious timestamp-cache regression: met;
7. focused and repository regressions recorded by final A4, followed by this
   fresh referee: met through the present review stage.  State application
   remains a later, separately authenticated action.

Consequently the current replacements are exact:

| role | rejected cycle | final cycle |
| --- | --- | --- |
| wrapper | `64854c95004efb622c572f6c00d87bc997b74eec7c5563bb06863764b4c9df11` | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` |
| tests | `c9747c8cfe78d8da153e2c9e8b0ddb81e64296bbaf06ed5ede906595f806850e` | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` |
| A4 report | `55f4f574ad5f44f766726c3d8b8346b2a51e2dfda0562fd8df977e678a9429e4` | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` |

The scoped candidate `d8cf6427...` is unchanged.  Earlier A4 cycles and any
judge or State Patch audit authenticating their wrapper/test/report hashes
remain superseded chronology; none can authorize the final bytes.

One prose sentence in the final A4 report and one quoted sentence in the A3
addendum contain mojibake in place of typographic dashes or quotation marks.
The surrounding ASCII text states the intended negations explicitly, and no
formula, hash, command, output, scope, or provenance assertion depends on
those glyphs.  This is nonblocking typography, not an unsupported
implication.

## Final decision

**PASS. First unsupported implication: none.**  The final source-execution
cycle proves the corrected guard only on `rho_c<=rho<1`, binds authenticated
repository source to the executed producer code, preserves the finite/A3
ownership boundary, and supports the exact disjoint closure of D20.  No
State Patch or higher promotion is performed by this report.
