# Round 21 A4 replacement: scoped exact-constant lifecycle

Date: 2026-07-15

Role: replacement executable-evidence report

## Verdict

**PASS. First issue: none in the replacement cycle.**

The earlier A4 report
`rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md`
(SHA-256
`d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56`)
is superseded because its source comment and success banner stated the false
unrestricted claim `k11(rho)>12 for rho>=rho_c`.  That report remains frozen
as negative scope chronology.  No output from it is treated as the current
A4 verdict.

The replacement cycle authenticates a scoped candidate packet, carries the
guard domain as returned certificate data, rejects the old packet path and
old CLI literal, replays both sealed finite certificates, and reruns the
complete repository suite.

## Authenticated replacement bytes

| role | path | SHA-256 |
| --- | --- | --- |
| scoped candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md` | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| hardened wrapper | `computations/round21_verify_exact_d20_closure.py` | `64854c95004efb622c572f6c00d87bc997b74eec7c5563bb06863764b4c9df11` |
| hardened tests | `computations/tests/test_round21_verify_exact_d20_closure.py` | `c9747c8cfe78d8da153e2c9e8b0ddb81e64296bbaf06ed5ede906595f806850e` |

The wrapper authenticates exactly 18 proof inputs.  Its candidate entry is
the scoped packet above.  The rejected predecessor
`state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md`
(SHA-256
`415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3`)
is absent from `EXPECTED_INPUT_HASHES`.

The compact and aggregate producer bytes and canonical compact digest are
unchanged:

| artifact | SHA-256 |
| --- | --- |
| compact producer | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` |
| compact tests | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` |
| compact canonical digest | `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631` |
| aggregate verifier | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` |
| aggregate tests | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` |

## The rejected scope and exact repair

The missing upper wall is not cosmetic.  The map

\[
z_\rho=\frac{\pi}{1-\rho}
\]

is undefined at `rho=1`; beyond that wall its sign changes.  At `rho=2`,

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144,
\]

so `k11(2)<12`.  Thus the old unrestricted literal is false.

On the exact shell ratio domain `rho_c<=rho<1`, however,

\[
0<1-\rho\leq1-\rho_c,
\]

and hence

\[
z_\rho\geq\frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72.
\]

Therefore

\[
k_{11}(\rho)^2>\frac{49}{4}+132
=\frac{577}{4}>144,
\]

which proves exactly

\[
k_{11}(\rho)>12\qquad(\rho_c\leq\rho<1).
\]

Every point of

\[
\mathcal D_{20}=\{\rho_c\leq\rho<39/50,\;
k_{11}(\rho)<K<U(\rho)\}
\]

lies in this domain.  The repaired quantifier therefore leaves the exact
closure conclusion unchanged.

## Executable lifecycle repair

The wrapper now:

1. defines the canonical domain value `K11_GUARD_DOMAIN` as
   `rho_c<=rho<1`;
2. returns that value in the immutable `ExactConstants` result;
3. states the positive-denominator step explicitly in the source proof
   comment;
4. generates the CLI success banner from the returned domain;
5. authenticates the scoped replacement candidate rather than the rejected
   packet.

The tests now:

1. require the scoped candidate path and reject the predecessor path;
2. assert the returned exact guard domain;
3. prove the exact `rho=2` counterexample from the rational upper enclosure;
4. require the corrected CLI literal;
5. reject the old unrestricted CLI literal;
6. retain every earlier byte-mutation, Machin-branch, partition, strict-wall,
   precision, derivative, and finite-scope mutation.

This is a quantifier and provenance repair.  It changes no compact leaf,
aggregate box, exact face row, outward interval decision, derivative formula,
or residual subtraction owner.

## Replacement reproduction

Python bytecode writes and pytest's cache provider were disabled.  The
following outputs are from the replacement bytes listed above.

~~~text
python -B -m py_compile computations/round21_verify_exact_d20_closure.py computations/tests/test_round21_verify_exact_d20_closure.py
PASS

python -B -m computations.round21_verify_exact_d20_closure --high-precision 384
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

python -B -m pytest -p no:cacheprovider -q computations/tests/test_round21_verify_exact_d20_closure.py
............                                                             [100%]
12 passed in 131.34s (0:02:11)

python -B -m pytest -p no:cacheprovider -q
........................................................................ [ 21%]
...........................................x.................. [ 40%]
........................................................................ [ 61%]
........................................................................ [ 83%]
.......................................................                  [100%]
332 passed, 1 xfailed, 10 subtests passed in 159.69s (0:02:39)
~~~

The designated xfail is unchanged and is not a failure of this audit.

## Scope of the A4 conclusion

The compact result is still exactly the 10,580-leaf certificate on
`[7/51,39/50] x [12,200]`.  The aggregate result is still exactly the 1,286
outward-box base certificate at `K=200`.  The executable still makes no
all-frequency proof decision: the analytic `K>=200` propagation remains an
A3 obligation.

The exact set replay still enumerates all 243 sign rows, assigns `K=200` to
the compact subtraction owner, and finds the proposed `D21` empty.  It does
not promote any compact, uniformity, theorem, program, or legacy diagnostic
obligation.

## Chronology consequence

The old A4 report, judge SHA
`5c59fdb95ec0b24f604448d323031e8182366ff00fc6b3a005741d69abf02fd4`,
and State Patch audit SHA
`20a3e72303592e4a3c9573e0549cb10fc00ba2a54d0580975a4082c118893ce8`
predate this replacement evidence and cannot authorize application.  They
must remain superseded chronology.  A new judge must authenticate this
report and the replacement wrapper/test hashes, followed by a new independent
State Patch audit.

## Final decision

**PASS for the scoped replacement A4 cycle.**  The executable evidence proves
only the corrected guard on `rho_c<=rho<1`, preserves the finite-versus-
analytic boundary, and reproduces every numerical and exact-set invariant
needed for closure of `D20`.
