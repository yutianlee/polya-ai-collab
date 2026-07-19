# Preserved Round 21 referee failure: mutation-lifecycle miss

Date: 2026-07-15

Status: **FAIL / SUPERSEDED NEGATIVE CHRONOLOGY**.

The first fresh exact-D20 referee report has raw-file SHA-256
`0466a240861de32b60819f9a5cd3b48106b230839c3fae07f4f67cbd59588e74`.
It correctly reconstructed the compact and aggregate mathematics, replayed
the finite certificates, and returned PASS. That PASS is not admissible as
final positive evidence.

The independently produced cross-comparison, SHA-256
`11672110bdc1169c40b46247832c19b9187df3112ab67f28324f6784a2f552a6`,
identified an earlier lifecycle failure that the referee missed: the
preserved A4 branch-gap record required adversarial tests that lose either
exact Machin range bound and the principal-branch conclusion. The then-live
tests only called `verify_exact_constants()` and positively asserted its
returned bounds, while the wrapper exposed no executable branch-conclusion
predicate to mutate.

This is not a mathematical counterexample. It means the authenticated A4
replacement did not satisfy its own mandatory mutation-hardening gate, and
the concurrent referee's PASS depended on that incomplete evidence cycle.
The report is retained byte-for-byte as a failed review cycle and must not be
listed as a positive adversarial-review artifact.

A valid replacement cycle must:

1. expose an executable exact branch-certificate and conclusion predicate;
2. reject independent mutations losing the lower range bound, upper range
   bound, or principal-branch conclusion;
3. rerun both finite-certificate precisions, focused tests, and the complete
   suite;
4. pass a new independent cross-comparison and a new fresh assume-false
   referee review.

The frozen residual, candidate, contracts, A3 proof, and compact/aggregate
certificate inputs do not require mathematical changes.
