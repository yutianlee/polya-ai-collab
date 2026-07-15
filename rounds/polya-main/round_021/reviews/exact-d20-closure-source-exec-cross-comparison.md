# Round 21 Exact-D20 Source-Execution Cross-Comparison

Date: 2026-07-15

Role: independent cross-comparison of the final scoped A4 cycle

## Verdict

**PASS. First issue: none.**

The final A4 cycle closes both defects in its predecessor lineages: the
frequency guard is stated only on \(\rho_c\leq\rho<1\), and every
proof-bearing repository module is executed from the same in-memory source
payload that is authenticated. The compact and aggregate producer bytes,
the \(\mathcal Q/\mathcal B\) chain, finite certificate data, canonical
digest, exact faces, and subtraction owners are unchanged.

This verdict is only the independent cross-comparison gate. It does not
replace the required fresh assume-false referee, judge, or independent State
Patch audit, and it does not itself promote or apply any proof obligation.

## 1. Authenticated comparison inputs

All six supplied identities were reproduced before their contents were used:

| role | path | reproduced SHA-256 | result |
| --- | --- | --- | --- |
| scoped candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md` | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` | exact |
| final wrapper | `computations/round21_verify_exact_d20_closure.py` | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` | exact |
| final tests | `computations/tests/test_round21_verify_exact_d20_closure.py` | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` | exact |
| final A4 report | `rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-source-exec-replacement.md` | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` | exact |
| A3 domain addendum | `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-domain-addendum.md` | `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241` | exact |
| cached-bytecode failure record | `rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-domain-addendum.md` | `d9a8fd94b1e730a324cfc3b0f518fc00cb65113ec1a0f80fc4bc1cb547c6c4d3` | exact |

The wrapper manifest contains exactly 18 inputs, includes the scoped
candidate, and excludes the rejected unscoped candidate
`415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3`.

## 2. Exact domain comparison

The A3 addendum, scoped packet, final wrapper, tests, and final A4 report now
agree on the exact statement

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).
\]

On this domain both denominators are positive and

\[
0<1-\rho\leq1-\rho_c,
\qquad
z_\rho\geq\frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72.
\]

Thus \(k_{11}(\rho)^2>577/4>144\). The upper wall is essential:
\(\rho=1\) is singular, while at \(\rho=2\)

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Every point of

\[
\mathcal D_{20}=\left\{\rho_c\leq\rho<\frac{39}{50},\;
k_{11}(\rho)<K<U(\rho)\right\}
\]

already has \(\rho<39/50<1\). The corrected quantifier therefore changes
no point, face, theorem application, or subtraction owner in
\(\mathcal D_{20}\). The old unrestricted guard remains false chronology
and may not be cited outside the corrected domain.

## 3. Authenticated source-to-execution lifecycle

### Sealed producers

For each sealed producer, `_load_hash_gated_module` performs one payload
`read_bytes()` call. The earlier whole-manifest authentication is a separate
read; the precise claim is that each load re-reads once and binds that one
in-memory payload to execution. The loader then:

1. computes SHA-256 over that byte buffer and checks the manifest digest;
2. strict-decodes those same bytes as UTF-8;
3. compiles the resulting text with the authenticated filename, mode
   `exec`, `dont_inherit=True`, and `optimize=0`;
4. creates and registers a fresh `ModuleType` with `__loader__`, `__spec__`,
   and `__cached__` all set to `None`; and
5. directly executes the code object in that module dictionary.

There is no `importlib`, source-loader, `marshal`, cache-path, or adjacent
`.pyc` lookup on this path. Hash, decode, and compile failures occur before
`sys.modules` is changed. If definition execution raises, the loader exactly
restores all three possible prior states: no entry, a prior module object, or
an existing `None` sentinel. A successful module intentionally remains
registered. The two-module load is not claimed to be transactional if the
second authenticated producer were to fail after the first succeeded.

Focused dynamic probes independently confirmed:

| lifecycle property | result |
| --- | --- |
| one read and execution of the authenticated payload | PASS |
| strict invalid UTF-8 rejected before module registration | PASS |
| absent entry removed after execution failure | PASS |
| prior module object restored after execution failure | PASS |
| prior `None` sentinel restored after execution failure | PASS |
| under `python -O`, loaded `__debug__` remains true because `optimize=0` | PASS |

### Timestamp-valid malicious cache

The final regression explicitly asks `py_compile` for
`PycInvalidationMode.TIMESTAMP` and asserts a zero-flags header. It first
caches `VALUE = 'cached'`, then installs the equal-length authenticated
source `VALUE = 'source'` while restoring the recorded mtime and size. The
hash-gated loader must return `source`, retain `__loader__ is None` and
`__cached__ is None`, and leave the deliberately created cache unconsulted.
The test removes that explicit cache file in `finally`.

This test does not rely on Python's environment-dependent default. In a
focused isolated run with `SOURCE_DATE_EPOCH=1` (where an unspecified
`py_compile` mode would default to checked-hash bytecode), the explicit
timestamp test and the three-state `sys.modules` test returned:

~~~text
fresh_pycache_files_before=0
..                                                                       [100%]
2 passed in 0.10s
fresh_pycache_files_after=0
~~~

`-B` suppresses ordinary import-cache writes, not explicit
`py_compile.compile()` output. The correctness claim rests on the forced
timestamp header, direct source execution, explicit sentinel cleanup, and
the empty disposable cache prefix, not on the false proposition that `-B`
disables `py_compile`.

## 4. Top-level wrapper and pytest provenance

Plain `python -B -m computations.round21_verify_exact_d20_closure` is not a
proof-bearing launch: `-B` does not forbid a timestamp-valid wrapper cache
read. The final A4 replay instead used trusted stdin code under
`python -I -B -`. That bootstrap read the wrapper once, required SHA-256
`31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`,
strict-decoded and compiled the same payload with optimization zero,
registered a uniquely named module before executing its definitions, and
then called `module.main()` with `--high-precision 384`. Registration before
definition execution is material for dataclass metadata. An independent
definition-only replay of that exact bootstrap path returned:

~~~text
isolated_authenticated_wrapper_definition=PASS
wrapper_sha256=31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9
~~~

The accepted pytest invocations used a newly created empty cache prefix and
the command-line option `-X pycache_prefix=...` under isolated mode; `-I`
would ignore an environment-only `PYTHONPYCACHEPREFIX`. Their stdin
bootstrap disabled plugin autoload, imported installed pytest before making
repository code importable, inserted the absolute repository root at the
front of `sys.path`, and passed absolute test paths to `pytest.main()`.
Specifically, it set `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` before pytest
configuration.
Consequently `PYTHONPATH`, user-site code, and current-directory packages
could not shadow the intended repository imports, while neither adjacent
ordinary caches nor pytest assertion-rewrite caches could substitute
bytecode for their source. The prefixes contained zero files before and
after the accepted runs.

The wrapper has a same-buffer hash-to-execution binding. Pytest is
corroborative regression evidence: its final test hash was checked before
the isolated source import in a fixed worktree, and the fresh prefix excludes
stale cache selection; no stronger same-buffer claim is made for pytest's
own later source read. Standard-library, pytest, and python-flint code are
trusted host software, not authenticated repository proof artifacts.

## 5. Unchanged \(\mathcal Q/\mathcal B\), certificates, and ownership

The final aggregate verifier is byte-identical to every accepted predecessor
at SHA-256
`fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952`.
Hence its exact reserve

\[
\mathcal Q=
R\lfloor K\eta_\rho\rfloor+
\frac{d_\rho J(J+1)}2-(1+d_\rho)\mathcal I(C,R)
-\frac{8R\tau^{5/2}}{15\sqrt\mu}
\]

and continuous lower proxy

\[
\mathcal B=(\mu-\tfrac12)(K\eta_\rho-1)
+\frac{d_\rho}{2}(\mu-\tfrac32)(\mu-\tfrac12)
-(1+d_\rho)\mathcal I(C,\mu+\tfrac12)
-\frac{8(\mu+1/2)}{15\sqrt\mu}
\]

are unchanged. So are the exact comparison
\(\mathcal B\geq0\Rightarrow\mathcal Q>0\Rightarrow N_D<W\), the derivative
formulas, and the curvature bound. A4 certifies only the finite base
predicates \(\mathcal B(\rho,200)>0\),
\(\mathcal B_K(\rho,200)>0\), and \(F(\rho)>0\). A3 still owns the universal
derivative estimates and two integrations that propagate those predicates
to every \(K\geq200\).

The compact producer and tests remain byte-identical at
`2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856`
and
`29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36`.
The source-execution commits change only the loader and its adversarial
tests; they do not touch either producer or the wrapper's classifier.

The final A4 output agrees exactly with its predecessors on every finite
invariant:

| invariant | unchanged value |
| --- | --- |
| compact root and ownership rectangle | `[7/51,39/50] x [12,200]` |
| compact leaves / proxy corners / floor comparisons / wall straddles | 10,580 / 16,020 / 2,153,076 / 0 |
| frozen 256-bit compact digest | `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631` |
| independently regenerated 384-bit compact digest | `c6deaf2c1a7e9df78760d61414c59ee48a16b0ed621266b2de40a29aea1946f6` |
| aggregate boxes / finite signs / endpoint checks | 1,286 / 14,146 / 2,572 |
| 384-bit derivative consistency points | 1,286 |
| exact classifier | \(3^5=243\) sign rows and all three \(U(\rho)\) orderings |

The exact subtraction remains

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

At \(K=200\) both theorem domains apply, but compact is the unique
subtraction owner. The face \(\rho=\rho_c\) is included subject to the strict
frequency inequalities; \(\rho=39/50\), \(K=k_{11}(\rho)\), and
\(K=U(\rho)\) are excluded. The cases \(U<200\), \(U=200\), and \(U>200\)
remain exhaustive, and the proposed \(\mathcal D_{21}\) is empty as exact
set bookkeeping.

## 6. Recorded reproduction evidence

The expensive numerical and repository-wide runs were not repeated by this
cross-comparison. Their outputs were verified as recorded facts inside the
authenticated final A4 report `47cd9467...`, not inferred from test-count
deltas.

The report records this authenticated stdin-wrapper output:

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

The recorded wall time is 136.8 seconds. The independently isolated focused
gate is recorded exactly as:

~~~text
14 passed in 149.15s (0:02:29)
~~~

The independently isolated complete repository gate is recorded exactly as:

~~~text
334 passed, 1 xfailed, 10 subtests passed in 184.76s (0:03:04)
~~~

Both runs recorded zero cache files before and after. The designated xfail
is unchanged. This cross-comparison reran only the fast two-test lifecycle
gate reported in Section 3.

## 7. Exact disposition of predecessor evidence

| artifact or cycle | SHA-256 | disposition now |
| --- | --- | --- |
| compact certificate report | `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` | retained positive finite-certificate evidence because its producer, tests, leaves, and digest are unchanged; it is not current wrapper provenance or a State Patch |
| compact adversarial audit | `aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca` | retained positive audit of the unchanged compact bytes; it does not cure or replace a top-level source-execution gate |
| aggregate certificate report / adversarial audit | `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` / `aa12d25d71091cfd01a116bc2777afa8669248a13441be391cf3da0b48c9a894` | retained positive finite \(K=200\) evidence only; A3 still owns all-\(K\) propagation |
| original clean-room review | `0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc` | its unqualified \(\rho\geq\rho_c\) guard sentence is rejected; its reconstruction restricted to \(\mathcal D_{20}\) remains usable only through the domain addendum |
| A3 domain addendum | `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241` | current positive evidence for the domain correction; its statements about the then-current old wrapper/tests are stale and are not source-execution evidence |
| prior replacement cross-comparison | `e923c034e7b64d5a865e85ee6912572c4e3bd10f890414c4c2a351e9c5790a0e` | superseded as a current cross/provenance gate; its Q/B, finite-certificate, and ownership comparison is reusable only after the domain and source-execution repairs |
| prior hardened referee | `c0a5239cae460ba961d911b384a9f2d2afac605865c72b4d2c604c0f4aa54a9c` | superseded PASS tied to the rejected candidate and wrapper/test/report hashes; not positive evidence for this cycle |
| corrected provenance audit of that referee | `48b259a94a0fd91a37ac2b606a22e1e4ca593f45bc2ef4392b7dd61dd359a5ab` | accurate for that historical referee handoff, but superseded as current-cycle provenance |
| unscoped A4 report | `d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56` | negative chronology: false unrestricted guard |
| scoped but cache-vulnerable A4 report | `55f4f574ad5f44f766726c3d8b8346b2a51e2dfda0562fd8df977e678a9429e4` | negative chronology: `SourceFileLoader` could execute unauthenticated timestamp-valid bytecode, and its `-B`/`py_compile` write claim was false |
| cached-bytecode adversarial referee | `d9a8fd94b1e730a324cfc3b0f518fc00cb65113ec1a0f80fc4bc1cb547c6c4d3` | retained authoritative FAIL for the `64854c95...` / `c9747c8c...` / `55f4f574...` cycle; requirements 1--6 and the replay, full-suite, and cross-comparison parts of requirement 7 are now satisfied, while the fresh-referee and State-Patch gates remain pending; its historical verdict is not rewritten |
| final source-execution A4 report | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` | current positive A4 evidence only |

Intermediate repaired snapshots `c501608c...` / `d5dab951...` and
`31130de2...` / `271c2c8d...` are non-final development bytes. Only wrapper
`31130de2...` paired with final tests `4de93001...`, the scoped packet, and
the final report `47cd9467...` is positive current executable evidence.

The old judge `5c59fdb95ec0b24f604448d323031e8182366ff00fc6b3a005741d69abf02fd4`
and State Patch audit
`20a3e72303592e4a3c9573e0549cb10fc00ba2a54d0580975a4082c118893ce8`
predate both repairs. They remain superseded and cannot authorize
application. A fresh referee, judge, and independent State Patch audit must
authenticate the final quartet and this comparison before any one-time
state mutation.

## Final decision and nonclaims

**PASS. First issue: none.** The final scoped cycle proves an authenticated
source-execution path, preserves the exact \(\mathcal Q/\mathcal B\) and
finite-certificate evidence, and leaves every \(\mathcal D_{20}\) face and
owner unchanged. The proposed \(\mathcal D_{21}=\varnothing\) is exact
bookkeeping, not an automatic theorem promotion.

No conclusion here promotes `SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, `POLYA-program-target`, or any legacy diagnostic target.
No claim is made about novelty, tiling, scaling, or a broader theorem beyond
the scoped Round 21 \(\mathcal D_{20}\) closure.
