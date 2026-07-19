# Round 20 Combined Closure: Replacement Exact-Constant Audit, Second Repair

Verdict: **PASS (A4 finite arithmetic only)**.

First issue: **none after the second repair cycle**.

This replacement supersedes only the A4 verdict in
`combined-closure-constants.md`; it does not edit that immutable report and
does not certify the analytic A3 theorem reconstruction.

## Replacement provenance

The preceding A4 report remains byte-identical:

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/reviews/combined-closure-constants.md` | `4b5429f9e51e55d7a00635a58115fb417441e23eec5ba253346f54bee9aa9afe` |

Its adversarial audit was preserved at commit
`964a421` and returned **FAIL**:

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/reviews/combined-closure-constants-adversarial-audit.md` | `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd` |

The first decisive defect was a missing payment for the candidate's live
`k_9`, `H=6`, `h=4` cap-74 cell. The old global `k_9` check paid only cap 73.
The repaired verifier proves this cell separately and hardens the structural
checks identified by the failure.

That first replacement was itself rejected by the preserved second-cycle
audit:

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement-audit.md` | `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31` |

The second audit remains byte-immutable. It identified four implementation
and artifact-integrity defects without changing the correct cap-74 arithmetic:

1. an actual `0x08` C0 byte at replacement-report offset 1729;
2. localization predicates that mutation could disconnect from their computed
   `x` input;
3. a cap-74 equality predicate lacking a wrong-wall semantic test at that
   exact gate; and
4. skip-hash CLI output that looked authenticated and printed frozen hashes.

This document records the second repair of those four defects.

The released candidate and freeze continue to authenticate as:

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |

All other Section 1/7 hash gates also pass.

## Decisive cap-74 repair

The candidate zero registry gives

$$
j_{7/2,2}>\frac{103}{10}.
$$

Angular propagation from `ell=3` to `ell=4` gives the exact square

$$
\left(\frac{103}{10}\right)^2+\bigl(4\cdot5-3\cdot4\bigr)
=\frac{11409}{100}>108.
$$

Thus a counted `(ell,n)=(4,2)` mode has frequency strictly above every wall
whose square is at most 108.

At `K=k_9`, the channel comparison for that mode is

$$
4z_\rho^2+20<z_\rho^2+90,
$$

so counting it forces

$$
z_\rho^2<\frac{70}{3}.
$$

At equality the channel lower bound equals `k_9`; strict spectral counting
excludes the mode. At the rational ratio face,

$$
z_{7/20}^2
=\frac{400\pi^2}{169}
>\frac{400}{169}\left(\frac{333}{106}\right)^2
>\frac{70}{3},
$$

and the exact reserve in the last comparison is

$$
\frac{400}{169}\left(\frac{333}{106}\right)^2-\frac{70}{3}
=\frac{36230}{1424163}>0.
$$

Since `z_rho^2` increases strictly with `rho`, a counted `ell=4` second mode
therefore forces

$$
\rho<\frac7{20}.
$$

Choose the fixed payment wall `207/20`. Its square satisfies

$$
\left(\frac{207}{20}\right)^2
=\frac{42849}{400}
<108
<\frac{11409}{100}.
$$

Consequently the same counted mode forces `K>207/20`. Monotonicity of the
Weyl payment in the required directions reduces the cell to the rational
endpoint `(rho,K)=(7/20,207/20)`. Using `pi<22/7`,

$$
\begin{aligned}
\mathcal W\left(\frac7{20},\frac{207}{20}\right)
&>\frac{2}{9}\frac7{22}
\left(1-\left(\frac7{20}\right)^3\right)
\left(\frac{207}{20}\right)^3\\
&=\frac{52823261673}{704000000}\\
&=74+\frac{727261673}{704000000}>74.
\end{aligned}
$$

The cap itself is the complete multiplicity sum

$$
49+25=74.
$$

Every executable label in this chain begins with
`k9 H=6,h=4 cap74:`; the targeted test checks all thirteen labels and marks
only the final `49+25` identity as bookkeeping.

## Structural hardening

### Substantive checks versus bookkeeping

The ledger now classifies each successful entry as one of:

- **substantive**: an inequality, strict face implication, localization,
  exclusion, payment, or analytic-sign reduction;
- **bookkeeping**: a candidate table sum or inventory identity;
- **authentication**: a file-existence or SHA-256 gate.

The final exact run contains

$$
\boxed{587=488\text{ substantive}+65\text{ bookkeeping}+34\text{ authentication}}
$$

labelled checks. This lower count than the failed verifier is intentional: a
large matrix of disconnected “not equal to a wall” probes was removed and
replaced by explicit expected-side implications.

### Anti-tautology enforcement

The verifier no longer uses literal-`True`, same-expression comparisons,
string-absence evidence, or aliases whose expansion merely compares an
expression with itself. In particular:

- the `K=2/omega_0` floor face now computes `p=2`, proves `rho K<3`, and
  concludes `m<=2p-1`;
- the optical low screen checks the actual implications from
  `a<=c/epsilon`, `a>=pi`, and `1/pi<q`;
- the high angular and radial screens evaluate the actual common-face
  expressions and their monotonic directions;
- common optical ownership is checked by the two signed face slacks;
- subtraction uses the actual lower/stair/optical predicates and no longer
  treats absence of the strings `B0` and `B1` as evidence.

The targeted suite contains a synthetic AST regression. It demonstrates that
the scanner detects all four prohibited forms: literal `True`, direct
same-AST comparison, alias-disconnected comparison, and string-membership
evidence. The actual verifier has none.

### Named localization faces

Every one of the seventeen named rational faces in the candidate now has an
explicit expected channel side tied to its cap/localization purpose. The
registry covers exactly

$$
\frac15,\frac3{10},\frac13,\frac38,\frac25,\frac5{12},\frac37,
\frac12,\frac{107}{200},\frac8{15},\frac35,\frac{16}{25},
\frac{13}{20},\frac23,\frac4{25},\frac14,\frac7{20}.
$$

The verifier proves the requested positive or negative sign of

$$
m(m+1)-\ell(\ell+1)-(n^2-1)z_\rho^2
$$

at each face; it does not merely prove non-equality. The three algebraic faces
are likewise directional:

- at `z^2=16`, the `k_11`, `n=3`, `ell=1` channel difference is exactly
  `2>0`;
- at `z^2=68/3`, the `k_10`, `n=2`, `ell=6` difference is exactly zero and
  strict counting excludes the mode;
- at `z^2=34`, the `k_11`, `n=2`, `ell=5` difference is exactly zero and
  strict counting excludes the mode.

The `7/20` entry is explicitly connected to the repaired cap-74 payment.

## Second-cycle hardening

### Artifact bytes

The unintended byte sequence around the propagation formula was
`+ 0x08 igl(...)`; it is now the intended printable text `+\\bigl(...)`.
The focused suite scans the verifier, focused tests, and this replacement
report byte-for-byte. It rejects every byte below `0x20` except tab, line feed,
and carriage return, and also rejects `0x7f`. All three scans pass with no
disallowed C0 byte.

### Input-connected localization

The channel calculation is now centralized in the injectable exact function

```text
channel_delta(checkpoint, radial, ell, x)
  = checkpoint(checkpoint+1) - ell(ell+1) - (radial^2-1)x.
```

Each named localization calls `verify_localization_expectation` with its
actual `x_at_ratio(rho)` input. The tests independently hard-code all seventeen
tuples `(rho, checkpoint, radial, ell, expected_sign)` rather than rebuilding
the expected registry from the verifier. They then recompute every interval
from the formula above and compare it with the verifier result.

Two semantic mutation tests specifically reject replacement of the computed
delta by `Interval.point(item.expected_sign)`:

- the independent hard-coded calculation would disagree immediately; and
- for the `k_9`, `n=2`, `ell=4` entry, perturbing `x` from `24` to `25`
  changes delta exactly from `-2` to `-5`, a change of `-3`.

Thus both registry data and input sensitivity are independently exercised.

### Cap-74 equality gate

The defining channel equality is now checked by the injectable helper
`verify_k9_h6_h4_channel_equality`. At the intended wall `70/3` it returns the
point interval `[0,0]`. A targeted test supplies the wrong wall `71/3` and
requires failure at the equality label itself. Replacing that equality with a
disconnected predicate such as `channel_wall>0` therefore makes the focused
suite fail at the intended gate.

### Authenticated versus skipped CLI mode

The normal CLI path still performs all 34 authentication gates and prints the
frozen candidate and freeze SHA-256 values. The test-only skip path now returns
the distinct internal verdict `UNAUTHENTICATED_ARITHMETIC_PASS` and prints:

```text
UNAUTHENTICATED ARITHMETIC-ONLY RESULT: PASS
hash gates: SKIPPED
```

It prints no `sha256` label, candidate hash, freeze hash, or standalone
authenticated-looking `PASS` line. Focused tests enforce all of these negative
conditions.

## Scope of the PASS

All earlier exact threshold, lower-inventory, cap-395, zero-wall sign,
high-inventory, cap-table, payment, optical-reserve, `U/K_0`, `k_11<U`, and
exact-subtraction checks remain passing. No sampled floating-point result can
support PASS.

The following eight analytic inputs still require A3:

1. The separated strict-count identity and angular multiplicity rule.
2. The form-domain and index-preserving proofs of (24)--(26), including
   shell-to-ball comparison and angular propagation.
3. Tangent-cell root enumeration, positive-zero numbering, ODE uniqueness,
   and simplicity for the eight internal half-integer zero bounds.
4. The shifted-tail wedge, interface remainder, and strict tail aggregation
   outside the exceptional floor cell.
5. The strict phase-proxy implication preceding the exact cap-395 sum.
6. The product min--max comparison and quarter-circle sum bound on the low
   optical piece.
7. The complementary-action curvature, Stieltjes radial deficit, layer-cake
   identity, angular-error transfer, and phase transfer on the high optical
   piece.
8. The elementary analytic monotonicity arguments for `G_1`, `k_m`,
   `z_rho^2`, and the Weyl payments whose reduced exact signs are checked here.

## Replacement artifacts

| artifact | SHA-256 |
|---|---|
| `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |

The replacement report's final SHA-256 is recorded after its final bytes are
written.

## Commands and results

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
17 passed
```

```text
python -B -m pytest -p no:cacheprovider -q
........................................................................ [ 26%]
...........................................x..................            [ 49%]
........................................................................ [ 75%]
..................................................................       [100%]
271 passed, 1 xfailed, 10 subtests passed
```
