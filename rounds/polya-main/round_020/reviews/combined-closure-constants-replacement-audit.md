# Round 20 Combined Closure: Independent Replacement Audit

Verdict: **FAIL (supplied replacement bundle)**.

First issue: **the authenticated replacement report contains an actual `0x08`
(U+0008 BACKSPACE) control byte in the propagated-square display at byte offset
1729, line 51, column 31.** This is not terminal decoding. The byte occurs where
the TeX command `\bigl` was intended, so the exact authenticated report bytes
contain a malformed formula and cannot be accepted as a clean final report.

No mathematical defect was found in the cap-74 repair, and ordinary constant,
sign, and digest perturbations are killed. A stronger semantic-disconnection
mutation does survive, however, so the anti-tautology/perturbation hardening
also needs a second repair. The first issue remains the earlier byte defect in
the supplied report, which cannot be silently changed without a new SHA-256
and replacement audit.

## Authentication and isolation

All five supplied artifacts were authenticated before inspection:

| artifact | required and observed SHA-256 |
|---|---|
| `computations/round20_verify_combined_closure.py` | `15b61df7ee7035f515bb2fba4afed1b4d2b3db922038367a46995a9d2d43a8cc` |
| `computations/tests/test_round20_verify_combined_closure.py` | `8bfb2c17fb6de69bb5c0804ad9b0ebabbee380ba32c1872fadc818a09c1f17c0` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `6d38ebc24448913ec275cc8c0a1bfbb1db971e5e834ddc5e9cad17228012eb67` |
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |

The bad byte is therefore part of the exact supplied report, rather than a
post-authentication alteration. I did not edit any supplied artifact.

## First issue: byte-integrity failure

A raw-byte scan allowing only TAB, LF, and CR among C0 controls found exactly
one disallowed control byte across all five inputs:

```text
replacement report: 1 disallowed C0 control byte
offset=1729 byte=0x08 line=51 column=31
context=b'eft(\\frac{103}{10}\\right)^2+\x08igl(4\\cdot5-3\\cdot4\\bigr)\n=\\'
verifier: 0
targeted tests: 0
candidate: 0
freeze: 0
```

Thus the actual byte sequence after the plus sign is `2b 08 69 67 6c`, not the
intended `2b 5c 62 69 67 6c` for `+\bigl`. The surrounding prose and executable
verifier make the intended arithmetic unambiguous, but that does not cure the
final-byte defect in the authenticated report.

## Repaired verifier result

### Cap-74 path

The formerly omitted `k_9`, `H=6`, `h=4` cell is now connected to a complete
13-check exact chain. The verifier proves

$$
\left(\frac{103}{10}\right)^2+8=\frac{11409}{100}>108,
\qquad
z_{7/20}^2>\frac{70}{3},
$$

uses strict counting to force `rho<7/20` and `K>207/20`, and proves

$$
\mathcal W\left(\frac7{20},\frac{207}{20}\right)
>
\frac{52823261673}{704000000}
=74+\frac{727261673}{704000000}>74.
$$

The full multiplicity is separately classified as the bookkeeping identity
`49+25=74`. The path is invoked from the high cap/payment verifier; the old
global `k_9` payment of 73 is no longer asked to pay this cell.

An in-memory source mutation changing the payment wall from `207/20` to
`206/20` was killed at the exact-square check. No supplied file was changed.

### Anti-tautology and authentication gates

The actual verifier produces no finding under the targeted AST scanner. Its
synthetic regression detects all four prohibited patterns: literal `True`, a
direct same-expression comparison, the same comparison hidden behind a local
alias, and string-membership evidence. The earlier `2 == 2`, self-comparison
optical screens, and string-only `B0/B1` check are absent.

A deliberately wrong candidate digest was killed at the candidate SHA-256
gate. The normal run performs 34 authentication checks for the 17 permitted
paths, and the targeted test asserts the exact path/digest map.

This hardening is nevertheless incomplete. A single in-memory source mutation
replaced the independently computed localization expression by

```python
delta = Interval.point(item.expected_sign)
```

so that every positive/negative side check was true by construction. The AST
scanner returned no issue, the targeted localization assertions passed, and
the full mutated verifier still returned `PASS` with all 587 checks and all 34
authentication gates. The scanner detects only selected syntactic tautologies;
it does not detect an expected-output-fed predicate. The targeted test checks
the number of ratio labels and the set of ratio keys, but never independently
recomputes the `(checkpoint, radial, ell, sign)` tuples. This is a substantive
test loophole under the requested perturbation audit.

There is also an authentication-output hazard: the documented test-only
`--skip-hash-gates` option returns `PASS`, reports zero authentication gates,
and still prints the hard-coded candidate/freeze hashes. Even if retained for
tests, that mode should identify its result as unauthenticated and must not
present constants as observed digests.

### Expected-side localizations

All 17 candidate rational faces occur exactly in the expected-side registry.
Each entry evaluates the signed channel difference

$$
m(m+1)-\ell(\ell+1)-(n^2-1)z_\rho^2
$$

against its declared positive or negative side. The `7/20` entry is explicitly
tied to the cap-74 purpose. Independently flipping each declared sign killed
all 17 mutations; deleting the `7/20` entry was killed by the completeness
gate. The three algebraic faces are directional, including strict equality
exclusion at `68/3` and `34`.

Those facts establish that the present registry values are arithmetically
correct. They do not cure the surviving expected-output-fed mutation described
above.

### Scope

The executable result remains an A4 finite-arithmetic result only. Its eight
listed analytic assumptions still require the isolated A3 reconstruction;
nothing in this audit promotes them to exact computational conclusions.

## Commands and results

```text
Get-FileHash -Algorithm SHA256 <the five supplied paths>
15b61df7ee7035f515bb2fba4afed1b4d2b3db922038367a46995a9d2d43a8cc
8bfb2c17fb6de69bb5c0804ad9b0ebabbee380ba32c1872fadc818a09c1f17c0
6d38ebc24448913ec275cc8c0a1bfbb1db971e5e834ddc5e9cad17228012eb67
e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
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
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round20_verify_combined_closure.py
............                                                             [100%]
12 passed in 0.62s
```

```text
python -B -m pytest -p no:cacheprovider -q
........................................................................ [ 27%]
...........................................x..................            [ 51%]
........................................................................ [ 78%]
........................................................                 [100%]
261 passed, 1 xfailed, 10 subtests passed in 5.04s
```

```text
in-memory perturbation harness
cap74 constant perturbation: KILLED
first failure: k9 H=6,h=4 cap74: exact (207/20)^2
expected-side sign flips killed: 17/17
missing 7/20 registry entry: KILLED
first failure: every named ratio has a connected expected-side assertion
candidate hash perturbation: KILLED
first failure: SHA-256 gate: state/lemma_packets/SHELL-combined-closure-round20-claim.md
anti-tautology synthetic issues: literal-true, same-AST, alias-disconnected, string-membership
single-site localization-tautology mutant AST issues: []
single-site mutant targeted localization assertions: True
single-site localization-tautology mutant: PASS 587 34
```

```text
python -B computations/round20_verify_combined_closure.py --skip-hash-gates
PASS
first issue: none
exact finite checks: 553
substantive checks: 488
bookkeeping identities: 65
authentication gates: 0
candidate sha256: e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
freeze sha256: aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
analytic assumptions remaining for A3: 8
```

The supplied replacement bundle therefore requires a byte-clean replacement
report and new report hash. The verifier's present cap-74 arithmetic needs no
constant change, but the localization test/anti-tautology guard and unauthenticated
CLI output need hardening before the next replacement audit.
