# Round 20 Combined Closure: Final Exact-Constants Re-Audit

Verdict: **PASS (A4 finite arithmetic and final-byte gate)**.

First issue: **none**.

The second repair closes the cap-74, artifact-byte, localization-connection,
wrong-wall, and unauthenticated-output defects recorded by the preserved failed
audit. This verdict remains limited to exact finite arithmetic and artifact
integrity; it does not certify the eight analytic A3 assumptions.

## Authentication

All supplied inputs were authenticated before inspection:

| artifact | required and observed SHA-256 |
|---|---|
| `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95` |
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md` | `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31` |

No supplied artifact was edited.

## Byte and visible-text integrity

All six artifacts decode as strict UTF-8. A raw scan found zero forbidden C0
bytes and zero DEL bytes in every artifact. A separate visible-mojibake scan
found no replacement character or common double-decoding marker. In
particular, the repaired report now contains the literal printable formula

```text
\left(\frac{103}{10}\right)^2+\bigl(4\cdot5-3\cdot4\bigr)
```

with an ordinary backslash before `bigl`; the former `0x08` byte is absent.

## Cap-74 closure

The complete 13-check path for the candidate's `k_9`, `H=6`, `h=4` cell still
proves

$$
\left(\frac{103}{10}\right)^2+8=\frac{11409}{100}>108,
\qquad
z_{7/20}^2>\frac{70}{3},
$$

and uses strict counting to force `rho<7/20` and `K>207/20`. Its exact payment
is bounded by

$$
\mathcal W\left(\frac7{20},\frac{207}{20}\right)
>
\frac{52823261673}{704000000}
=74+\frac{727261673}{704000000}>74.
$$

The full multiplicity identity is `49+25=74`. The equality helper returns the
point interval `[0,0]` at `z^2=70/3`; supplying the wrong wall `71/3` raises at
the defining-equality gate.

## Localization registry and mutation sensitivity

The focused tests now independently hard-code all 17 tuples
`(rho, checkpoint, radial, ell, expected_sign)`. For every row they recompute

$$
m(m+1)-\ell(\ell+1)-(n^2-1)z_\rho^2
$$

without rebuilding the expected tuple from the verifier, compare that interval
with `verify_localization_expectation`, and check its required sign. An
independent input-sensitivity test changes the `k_9,n=2,ell=4` input from
`x=24` to `x=25` and requires the exact change from `-2` to `-5`.

I reran the prior exact survivor entirely in memory, replacing

```python
delta = channel_delta(item.checkpoint, item.radial, item.ell, x)
```

with

```python
delta = Interval.point(item.expected_sign)
```

The mutant verifier alone still reaches `PASS 587 34`, as expected for the
adversarial construction, but both repaired tests kill it with `AssertionError`:

- `test_localization_registry_and_sides_are_hard_coded_and_input_connected`;
- `test_localization_semantics_change_under_perturbed_x`.

I likewise replaced the cap-74 equality condition by the disconnected
predicate `channel_wall > 0`. The mutant verifier alone reaches its ordinary
path, but `test_k9_cap74_wrong_channel_wall_fails_at_equality_gate` kills the
mutation because `71/3` no longer raises. These in-memory mutations created no
workspace file and changed no supplied byte.

## Authentication-mode output

The normal CLI authenticates all 17 permitted paths, reports 34 authentication
checks, and prints the observed candidate/freeze hashes. The test-only skipped
mode is now unambiguous:

```text
UNAUTHENTICATED ARITHMETIC-ONLY RESULT: PASS
hash gates: SKIPPED
```

It reports zero authentication gates and prints no `sha256` label or frozen
hash. Its internal verdict is `UNAUTHENTICATED_ARITHMETIC_PASS`, not `PASS`.

## Commands and results

```text
Get-FileHash -Algorithm SHA256 <the six supplied paths>
086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5
4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf
df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95
e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31
```

```text
python -B computations/round20_verify_combined_closure.py
PASS
first issue: none
exact finite checks: 587
substantive checks: 488
bookkeeping identities: 65
authentication gates: 34
candidate sha256: e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
freeze sha256: aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
analytic assumptions remaining for A3: 8
```

```text
python -B computations/round20_verify_combined_closure.py --skip-hash-gates
UNAUTHENTICATED ARITHMETIC-ONLY RESULT: PASS
hash gates: SKIPPED
exact finite checks: 553
substantive checks: 488
bookkeeping identities: 65
authentication gates: 0
analytic assumptions remaining for A3: 8
```

```text
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round20_verify_combined_closure.py
.................                                                        [100%]
17 passed in 1.24s
```

```text
python -B -m pytest -p no:cacheprovider -q
........................................................................ [ 26%]
...........................................x..................            [ 49%]
........................................................................ [ 75%]
..................................................................       [100%]
271 passed, 1 xfailed, 10 subtests passed in 41.07s
```

```text
in-memory mutation re-audit
prior expected-sign mutant verifier: PASS 587 34
localization registry/input-connection test: KILLED (AssertionError)
localization perturbed-x test: KILLED (AssertionError)
prior expected-sign mutant killed by repaired tests: True
wrong-wall predicate mutant verifier: PASS 587 34
wrong-wall equality-gate test: KILLED (Failed)
wrong-wall predicate mutant killed by repaired test: True
```

No exact-constant, face-direction, authentication, mutation-sensitivity, or
final-byte issue remains in the supplied second-repair bundle.
