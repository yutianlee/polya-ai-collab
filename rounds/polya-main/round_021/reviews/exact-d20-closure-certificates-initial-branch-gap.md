# Preserved Round 21 A4 failure: implicit Machin branch

Date: 2026-07-15

Status: **FAIL / SUPERSEDED NEGATIVE CHRONOLOGY**.

The first completed Round 21 exact-D20 A4 cycle reported PASS with these
new-artifact identities:

| artifact | first-cycle SHA-256 |
|---|---|
| computations/round21_verify_exact_d20_closure.py | 2022552214d30a77075a80f232a5ac76170ff85c8f41ad24a3ef815aa003eeda |
| computations/tests/test_round21_verify_exact_d20_closure.py | 0b4ae62604fae81991ffc2c697a4c0fb0d9b8ac479410dcf29c6b78193b4976d |
| rounds/polya-main/round_021/reviews/exact-d20-closure-certificates.md | 8ce51560af2801f4bdba6fbef951a4f0968aa49ffefafcbe989362facafff85c |

Those uncommitted bytes passed the finite certificate replays and tests, but
their exact-constant subcheck established

\[
\tan\!\left(4\arctan(1/5)-\arctan(1/239)\right)=1
\]

without explicitly proving that the angle lies on the principal
\(\pi/4\) branch rather than \(\pi/4+n\pi\).  The displayed tangent identity
alone is insufficient.  Therefore the first A4 PASS is rejected and none of
its three hashes may be used as positive evidence.

This gap does not invalidate the separate A3 analytic review: A3 proved
\(3<\pi<22/7\) independently by integral identities and did not read or use
the A4 verifier.  It also does not affect the compact or aggregate outward
replays themselves.  It is nevertheless material to A4's unconditional
claim that its own exact containment check is complete.

Before the branch repair, a separate mutation-hardening edit produced
intermediate wrapper and test hashes
6d2ae56b123296efec653bc3d4e2d740ad26d4396e70de9fc57938f11b774de2
and
4360cb61767a4ad0e37fc90a9968140bbe33b1244049a9c5ae0876644793a496.
No report hash or verdict was frozen for that intermediate pair, so those
bytes are also non-evidence.

A valid replacement must add exact bounds placing
\(\theta=4\arctan(1/5)-\arctan(1/239)\) in the same injectivity interval as
\(\arctan(1)=\pi/4\), test mutations that lose either range bound or the
branch conclusion, rerun both certificate precisions, and rerun focused and
full tests.  Only the resulting replacement hashes and a later independent
audit may be positive A4 evidence.
