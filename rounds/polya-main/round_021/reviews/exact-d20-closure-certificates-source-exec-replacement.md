# Round 21 A4 final replacement: authenticated source execution

Date: 2026-07-15

Role: replacement executable-evidence report

## Verdict

**PASS. First issue: none in this final replacement cycle.**

This report supersedes two failed A4 lineages:

1. `exact-d20-closure-certificates.md`, SHA-256
   `d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56`,
   omitted the required `rho<1` wall from its exact-constant banner;
2. `exact-d20-closure-certificates-domain-replacement.md`, SHA-256
   `55f4f574ad5f44f766726c3d8b8346b2a51e2dfda0562fd8df977e678a9429e4`,
   corrected that quantifier but loaded sealed producers through a source
   loader that could execute timestamp-valid unauthenticated bytecode.

Both predecessor reports remain negative chronology. The cached-bytecode
failure is recorded independently in
`exact-d20-closure-adversarial-referee-domain-addendum.md`, SHA-256
`d9a8fd94b1e730a324cfc3b0f518fc00cb65113ec1a0f80fc4bc1cb547c6c4d3`.

The final cycle binds the candidate domain, wrapper source, sealed producer
source, and test imports to explicit source-execution paths that do not
consult adjacent repository bytecode.

## Final authenticated bytes

| role | path | SHA-256 |
| --- | --- | --- |
| scoped candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md` | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| hardened wrapper | `computations/round21_verify_exact_d20_closure.py` | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` |
| hardened tests | `computations/tests/test_round21_verify_exact_d20_closure.py` | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` |

The wrapper manifest contains exactly 18 inputs. It includes the scoped
candidate above and excludes the rejected predecessor candidate SHA-256
`415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3`.

The proof-bearing producer hashes and canonical compact digest remain:

| artifact | SHA-256 |
| --- | --- |
| compact producer | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` |
| compact tests | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` |
| compact canonical digest | `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631` |
| aggregate verifier | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` |
| aggregate tests | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` |

## Mathematical domain repair retained

The exact guard is

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).
\]

Indeed, `0<1-rho<=1-rho_c` implies

\[
z_\rho\geq\frac{\pi}{1-\rho_c}=\pi+\frac12>\frac72,
\]

and hence `k_11(rho)^2>577/4>144`. The upper wall is indispensable:
`rho=1` is singular, and at `rho=2`

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Every D20 point satisfies `rho<39/50<1`, so the corrected guard supplies
exactly the lower compact-frequency inclusion required by the residual split.

## Authenticated producer execution

The rejected loader separately hashed a `.py` path and then delegated
execution to `SourceFileLoader`, which was permitted to use a matching cache.
The final `_load_hash_gated_module` instead:

1. reads the sealed source exactly once as bytes;
2. hashes that in-memory byte string and compares it with the manifest;
3. strict-decodes those same bytes as UTF-8;
4. compiles the resulting source in memory with
   `dont_inherit=True, optimize=0` and the authenticated filename;
5. executes that code object in a fresh registered `ModuleType` whose
   loader, spec, and cache fields are `None`;
6. restores every prior `sys.modules` state on execution failure, including
   absence, a prior module object, and a prior `None` sentinel.

No import loader or cache API occurs on the sealed-producer path.

The adversarial regression constructs an explicitly timestamp-mode cache
(header flags zero) containing `VALUE='cached'`, replaces its equal-length
source with authenticated `VALUE='source'` at the same recorded mtime, and
requires the loader to return `source`. It forces timestamp mode even when
`SOURCE_DATE_EPOCH` is present. A companion test checks all three
`sys.modules` restoration states. The deliberately created malicious cache
file is deleted in the test's `finally` block.

## Authenticated top-level launch

Plain `python -B -m ...` is not the final proof command because `-B` forbids
normal cache writes but does not forbid cache reads. The accepted wrapper
replay used a cache-free stdin bootstrap under `python -I -B -`. The
bootstrap:

1. read the wrapper source exactly once;
2. required SHA-256
   `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`;
3. strict-decoded and compiled those exact bytes at optimization zero;
4. registered a uniquely named fresh `ModuleType` before definition
   execution, so dataclass metadata resolved against the correct module;
5. called `module.main()` with `--high-precision 384`.

The accepted pytest gates used an independent fresh empty cache prefix for
each invocation and command-line `-X pycache_prefix=...` under isolated mode.
The stdin bootstrap disabled plugin autoload, imported the installed pytest
before adding the repository to `sys.path`, then inserted the absolute
repository root and called `pytest.main`. Both the wrapper and focused-test
hashes were checked before launch. `-B` suppressed normal writes, while the
malicious-cache regression cleaned its explicit sentinel. The cache prefix
contained zero files before and after each accepted run.

Runtime standard-library, pytest, and python-flint code remain trusted host
software rather than repository proof artifacts. The evidence claim is that
the hashed repository wrapper and producer sources—not adjacent repository
`.pyc` files—made every proof decision.

## Final reproduction results

The authenticated source bootstrap returned:

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

Wall time: 136.8 seconds.

The isolated focused gate returned:

~~~text
fresh_pycache_files_before=0
isolated_pytest_bootstrap=True
..............                                                           [100%]
14 passed in 149.15s (0:02:29)
fresh_pycache_files_after=0
~~~

The isolated complete repository gate returned:

~~~text
fresh_pycache_files_before=0
isolated_pytest_bootstrap=True
........................................................................ [ 21%]
...........................................x.................. [ 40%]
........................................................................ [ 61%]
........................................................................ [ 82%]
.........................................................                [100%]
334 passed, 1 xfailed, 10 subtests passed in 184.76s (0:03:04)
fresh_pycache_files_after=0
~~~

The designated xfail is unchanged and is not a failure of this cycle.

## Certificate and analytic boundary

The source-execution repair changes no mathematical producer algorithm. The
compact result remains exactly the 10,580-leaf certificate on
`[7/51,39/50] x [12,200]`. The aggregate result remains exactly the 1,286-box
base certificate at `K=200`. The executable makes no all-frequency proof
decision: A3 still owns the analytic derivative, curvature, and two-
integration propagation for every `K>=200`.

The exact classifier still enumerates all 243 sign rows, gives `K=200` to the
compact subtraction owner, treats `rho=39/50`, `K=k_11`, and `K=U` as
outside D20, and finds the proposed D21 empty. No compact, uniformity,
theorem, program, or legacy diagnostic obligation is promoted by this
report.

## Chronology consequence

Every judge or audit authenticating wrapper hashes `4868dcc3...` or
`64854c95...`, test hashes `6716ff1b...` or `c9747c8c...`, or either failed
A4 report predates this final execution lifecycle and cannot authorize state
application. Those bytes remain historical evidence only. A replacement
cross-comparison, fresh adversarial referee, provenance audit, judge, and
State Patch audit must authenticate the final hashes in this report.

## Final decision

**PASS for A4 only.** The final source-execution cycle authenticates the
scoped candidate and every proof-bearing repository source on its actual
execution path, reproduces the finite certificates and exact set split, and
preserves the boundary between finite computation and analytic propagation.
