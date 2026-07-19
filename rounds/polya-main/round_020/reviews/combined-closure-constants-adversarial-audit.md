# Round 20 Combined-Closure Constants: Adversarial Audit

Verdict: **FAIL**.

First issue: **the candidate's `k_9`, `H=6`, `h=4` cap-74 cell has no Weyl payment in the verifier, although the constants report says every high cap/payment case passes.**

## Authentication and isolation

Before reading each supplied artifact, I authenticated these exact bytes:

| artifact | required and observed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `computations/round20_verify_combined_closure.py` | `44a5e840d9f60fb58701b506d21688e15403d295fc9111081d08e982c3ca7de7` |
| `computations/tests/test_round20_verify_combined_closure.py` | `61df4f0b8ed18ee24a3d16ae1b3db189ae099abf86fe334f2a0067f12cc09ca2` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants.md` | `4b5429f9e51e55d7a00635a58115fb417441e23eec5ba253346f54bee9aa9afe` |

The released freeze was additionally authenticated at
`aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87`
before inspection. I inspected only the released candidate/freeze and the three
named A4 artifacts. Running the verifier necessarily hashes the 17 gated paths;
I did not open any other Round 20 proof, exploration, zero card, or review.

## Decisive missing cell

The candidate's `k_9` table contains the admissible row `H=6` and column
`h=4`, with cap

$$
49+25=74.
$$

The verifier gives `k_9` only a global payment greater than `73` in
`global_payments = ((7,40),(8,53),(9,73),(10,89),(11,121))`. Its only
conditional `k_9` payment is the distinct `H=8` case, cap `81`, localized by
the `71/6` first-zero wall. There is no conditional payment for `H=6,h=4`,
and no other check links that cap-74 cell to a payment. Consequently the global
`>73` check cannot pay a possible count of `74`.

This directly falsifies the reviewed report's conclusion that all proposed
high cap/payment cases pass. It also exposes a test loophole: the targeted high
test merely looks for some `k9` label and one algebraic-split label; it does not
require a payment label for every cap exceeding the global payment.

The omission appears repairable, but that does not validate the released
artifacts. Using the verifier's own exact interval machinery, angular
propagation gives the `ell=4,n=2` lower square `11409/100>108`, the channel
face gives `z_(7/20)^2>70/3`, and

$$
\mathcal W\left(\frac7{20},\frac{207}{20}\right)>74.
$$

Those exact implications are absent from the verifier and its tests.

## Additional adversarial weaknesses

Several passing labels are backed by tautologies rather than the claimed
objects. In particular, the `K=2/omega_0` floor-face label checks `2 == 2`;
the low optical scaling label compares an expression with itself; the two
"full" high optical screen labels compare variables with the expressions that
defined them immediately above; the common optical face compares `c/eps0`
with itself in both directions; and the `B0/B1` non-resubtraction label merely
checks that the strings `"B0"` and `"B1"` are absent from a tuple of unrelated
owner names. The AST test rejects only a literal `require(True, ...)`, so all
of these label-to-condition disconnects pass. Thus the reported count of 2,082
labels is not a count of 2,082 substantive exact implications.

The localization loop has a similar weakness: at each frozen rational ratio it
only proves that each enumerated channel wall is not exactly equal to that
ratio. It does not assert the expected side of the wall or connect the trace to
the relevant cap/payment case. This is why a large number of passing trace
labels do not close the missing cap-74 cell.

## Commands and results

```text
Get-FileHash -Algorithm SHA256 <the four paths above>
e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
44a5e840d9f60fb58701b506d21688e15403d295fc9111081d08e982c3ca7de7
61df4f0b8ed18ee24a3d16ae1b3db189ae099abf86fe334f2a0067f12cc09ca2
4b5429f9e51e55d7a00635a58115fb417441e23eec5ba253346f54bee9aa9afe
```

```text
python -B computations/round20_verify_combined_closure.py
PASS
first issue: none
exact finite checks: 2082
candidate sha256: e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61
freeze sha256: aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87
analytic assumptions remaining for A3: 8
```

```text
python -B -m pytest -p no:cacheprovider -q computations/tests/test_round20_verify_combined_closure.py
..........                                                               [100%]
10 passed in 0.49s
```

```text
python -B -  # exact omitted-cell probe using the verifier module
propagated ell=4,n=2 square: 11409/100
propagated square > 108: True
z(7/20)^2 > 70/3: True
(207/20)^2 < propagated square: True
exact interval lower bound W(7/20,207/20) > 74: True
```

The verifier and tests therefore reproduce their advertised PASS, but that
PASS is not sound for the complete candidate constant ledger.
