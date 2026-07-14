# Round 21 exact-D20-closure certificate and set audit (A4)

Date: 2026-07-15

Verdict: **PASS. First issue: none.**

This is an unconditional A4 PASS for the authenticated finite certificate
bytes, their frozen schemas and outward replays, and the exact candidate set
logic. It is not an A3 verdict. In particular, this audit proves only the
aggregate predicates evaluated at the base frequency \(K=200\); it does not
claim the universally quantified analytic propagation to every \(K\geq200\).

## 1. Scope and independence

I authenticated every allowed input before reading it. I then read only the
candidate, its two proof-free contracts, the three accepted residual
artifacts, the contracts' foundational inputs, and the sealed compact and
aggregate targets. I did not read a Round 21 A3 reconstruction, certificate
audit, synthesis, cross-comparison, referee, judge, State Patch, or Git
history.

The new independent wrapper and its adversarial tests are:

| artifact | SHA-256 |
|---|---|
| `computations/round21_verify_exact_d20_closure.py` | `85b661401544dac0398251480cadc5736fa7ac3941f47684e61d891da30756a0` |
| `computations/tests/test_round21_verify_exact_d20_closure.py` | `10940d66a5ec0f0e9d42f9d57205de840bb3ea78c92f13cdd08a66f8e9da5713` |

No binary float, display decimal, or midpoint sign is used by the wrapper for
an authentication, partition, branch, count, set, or sign decision.

### Preserved negative chronology

An earlier uncommitted A4 cycle printed PASS but is **rejected and is not
evidence for this verdict**. Its exact bytes were:

| rejected initial-cycle artifact | SHA-256 |
|---|---|
| wrapper | `2022552214d30a77075a80f232a5ac76170ff85c8f41ad24a3ef815aa003eeda` |
| tests | `0b4ae62604fae81991ffc2c697a4c0fb0d9b8ac479410dcf29c6b78193b4976d` |
| report | `8ce51560af2801f4bdba6fbef951a4f0968aa49ffefafcbe989362facafff85c` |

First issue in that cycle: the checker proved
\(\tan(4\arctan(1/5)-\arctan(1/239))=1\) and then invoked Machin's identity
without explicitly proving that the angle lies on the principal tangent
branch. Thus the step excluding \(\pi/4+n\pi\) was unsupported in the A4
artifact, even though the intended identity is true. The printed PASS,
focused tests, and full-suite result from that cycle are discarded.

An intermediate mutation-hardening edit had wrapper hash
`6d2ae56b123296efec653bc3d4e2d740ad26d4396e70de9fc57938f11b774de2`
and test hash
`4360cb61767a4ad0e37fc90a9968140bbe33b1244049a9c5ae0876644793a496`;
its report bytes were not frozen. Those are non-verdict bytes and are also
not evidence.

The present replacement adds and tests exact branch bounds
\(3/4<4\arctan(1/5)-\arctan(1/239)<4/5<1\), as detailed in Section 5.
Every execution result in Section 7 was rerun from the replacement bytes
whose hashes appear above.

## 2. Authentication

All 18 exact identities in the wrapper's closed manifest reproduced:

| role | artifact | reproduced SHA-256 |
|---|---|---|
| candidate | `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| compact contract | `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| aggregate contract | `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| accepted residual packet | `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| residual freeze | `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| residual audit | `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |
| compact verifier | `computations/round21_certify_compact_proxy.py` | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` |
| compact tests | `computations/tests/test_round21_certify_compact_proxy.py` | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` |
| compact report | `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md` | `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` |
| aggregate route | `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md` | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` |
| aggregate verifier | `computations/round21_verify_aggregate_tail.py` | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` |
| aggregate tests | `computations/tests/test_round21_verify_aggregate_tail.py` | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` |
| aggregate report | `rounds/polya-main/round_021/certification/aggregate-tail-global.md` | `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` |
| foundation | `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| foundation | `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| foundation | `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| foundation | `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| qualified source | `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

The manifest rejects a missing or extra path, a non-repository path, a
case-folding collision, malformed hash text, a missing file, and a digest
mismatch. The tests copied the closed 18-file bundle to a temporary root,
mutated each artifact independently, and observed rejection in all 18 cases.

## 3. Compact certificate replay

The wrapper independently checked the complete frozen schema:

| field | checked value |
|---|---|
| schema | `round21-compact-proxy-v2-half-open-faces` |
| root | \([7/51,39/50]\times[12,200]\) |
| frozen/minimum precision | 256/192 bits |
| leaf count | 10,580 |
| actual/depth-limit | 15/30 |
| box limit | 100,000 |
| generated proxy corners | 16,020 |
| generated Arb/integer comparisons | 2,153,076 |
| generated wall straddles | 0 |
| frozen canonical SHA-256 | `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631` |

At 256 bits, the sealed builder and a fresh leaf-by-leaf verifier both
accepted all 10,580 leaves. An independent implementation reconstructed the
canonical ASCII rows and reproduced the frozen digest. It also independently
checked that every leaf is nondegenerate and contained in the root, the exact
areas sum to the root area, every elementary rational \(\rho\)-slab tiles the
full \(K\)-interval without a gap or overlap, and every rational vertical
face has the lower-closed/upper-open owner, with only the two root upper faces
closed.

The same operations were rerun at 384 bits. The exact leaf records, tree,
depth, proxy-corner count, floor-comparison count, and zero-straddle count
were identical to the 256-bit certificate. Since precision is a canonical
digest field, the independent 384-bit digest is correctly different:

`c6deaf2c1a7e9df78760d61414c59ee48a16b0ed621266b2de40a29aea1946f6`.

Both precisions replayed the proof corner
\((\rho_-,K_+)\) for the proxy and
\((\rho_+,K_-)\) for the Weyl lower bound on every leaf. The wrapper also
checked separately:

- the exact rule \([3]_< = 2\), not ordinary floor \(3\);
- a ball `3 +/- 0.01` safely uses upper integer 4 and count 3;
- the exact zero extensions at \(\nu=\rho K\) and \(\nu=K\);
- the strict half-integer active cutoff at \(K=25/2\), which has 12 active
  channels and excludes \(\nu=K\);
- rejection below 192 bits;
- rejection of a changed schema, root, corner orientation, leaf endpoint,
  leaf count, leaf depth, proxy value, partition, or digest;
- rejection of the deliberately coarse root because its required leaf sign
  is nonpositive/uncertain, as well as earlier rejection of stored-proxy
  tampering.

Thus the finite compact certificate itself receives an unconditional A4
PASS. The spectral bridge and the analytic monotone-corner implication remain
within the separate A3 reconstruction boundary.

## 4. Aggregate base-face replay

### 4.1 Exact base-only schema

The sealed executable's finite box schema is ratio-only:
`RationalBox` has exactly the fields `lo`, `hi`, and `eta_regime`;
`evaluate_at_k0` has only the parameters `rho` and `eta_regime`; and its
source fixes `k = arb(K0)` with `K0 = 200`. The certificate runner has no
variable-\(K\) box parameter and makes no finite-box decision at \(K>200\).

The exact partition is

\[
[7/51,1/2]:726\text{ boxes},\qquad
[1/2,39/50]:560\text{ boxes},
\]

for 1,286 consecutive rational boxes of width at most \(1/2000\). The low
branch is exactly `rho_le_half`, the high branch is exactly `rho_ge_half`,
neither crosses the split, and the two formulas for \(\eta_\rho\) agree at the
common face \(\rho=1/2\).

### 4.2 Every outward predicate

At both 192 and 384 bits, all 1,286 Arb ratio enclosures contained both exact
rational endpoints: 2,572 endpoint-containment checks per precision. On
every box, the wrapper independently required all 11 frozen finite
predicates:

1. \(1-\rho>0\);
2. \(\mu_{200}>3/2\);
3. \(200\eta_\rho>1\);
4. \(S>\overline R\);
5. \(\overline R>200\rho\);
6. \(I_{KK}(\rho,200)<3b/800\);
7. \(E_{KK}(\rho,200)>0\);
8. \(\mathcal B_{KK}(\rho,200)>F(\rho)\);
9. \(\mathcal B(\rho,200)>0\);
10. \(\mathcal B_K(\rho,200)>0\);
11. \(F(\rho)>0\).

This is exactly \(1{,}286\times11=14{,}146\) certain sign comparisons per
precision. The wrapper also verifies that the executable's stored
`I_KK_bound` is the base value \(3b/800\), not a variable-frequency box
predicate.

### 4.3 Independent derivative consistency

A separate second-order automatic-differentiation implementation (`Jet2`)
evaluated the defining expressions for \(I(K)\), the interface-error term,
and \(\mathcal B(\rho,K)\). At the exact rational midpoint of every one of the
1,286 ratio boxes, at 384 bits, it independently checked the displayed
identities for

\[
I_K,\quad I_{KK},\quad E_{KK},\quad
\mathcal B_K,\quad\mathcal B_{KK},\quad F,
\]

and their agreement with every corresponding sealed \(K=200\) value. Every
outward difference contained zero. This is an independent algebra and
implementation consistency check; it is not a proof of a sign for arbitrary
\(K\).

The mutations changed the base frequency, precision, width, box count,
partition adjacency, branch owner, endpoint enclosure, value-key family,
sign/factor result, and derivative result. Each was rejected. Removing any
finite predicate or any named A3 boundary item was also rejected, including
the \(\tau=0\) cell, half-integer \(\mu\) walls, integer \(K\eta_\rho\)
walls, strict implications, universal guards/curvatures, and either
integration. A request to relabel the finite A4 replay as a
universal-frequency claim was rejected.

The authenticated aggregate report contains a global theorem narrative.
Authentication of those bytes does not make that narrative an A4 result.
This audit adopts only the corrected contract boundary: the outward
certificate supplies the finite premises at \(K=200\), while A3 must supply
the universal guards, inequalities, and two integrations.

## 5. Exact containment constants

No decimal approximation was used. The wrapper used exact alternating-series
bounds in Machin's identity

\[
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}.
\]

The tangent reduction was checked in exact rational arithmetic:

\[
\tan\left(4\arctan\frac15\right)=\frac{120}{119},
\qquad
\tan\left(4\arctan\frac15-\arctan\frac1{239}\right)=1.
\]

The branch is not inferred from that tangent equality alone. With principal
\(a=\arctan(1/5)\), \(b=\arctan(1/239)\), the alternating-series bounds

\[
a>\frac15-\frac{1}{3\cdot5^3},
\qquad 0<b<\frac1{239}
\]

give the exact range

\[
\frac34
<
\frac{70369}{89625}
=4\left(\frac15-\frac{1}{3\cdot5^3}\right)-\frac1{239}
<4a-b<\frac45<1.
\]

The principal value \(\arctan(1)=\pi/4\) also lies in \((0,1)\). On that
interval \(\cos x>0\) (for example, the alternating cosine bound gives
\(\cos x\geq1-x^2/2>0\)), so
\(\tan'(x)=\sec^2x>0\) and tangent is injective. Therefore
\(\tan(4a-b)=1\) forces \(4a-b=\arctan(1)=\pi/4\), excluding every
\(\pi/4+n\pi\) branch.

Four alternating terms give exact rational endpoints proving

\[
3<\pi<\frac{22}{7}.
\]

The upper bound gives \(14\pi<44\), equivalently

\[
7(1+2\pi)<51,
\qquad
\boxed{\frac7{51}<\frac1{1+2\pi}=\rho_c}.
\]

For \(\rho\geq\rho_c\), monotonicity of \(1/(1-\rho)\) gives

\[
z_\rho=\frac{\pi}{1-\rho}
\geq \frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72.
\]

Therefore

\[
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132=\frac{577}{4}>144,
\]

so \(\boxed{k_{11}(\rho)>12}\) on the entire accepted ratio range.

## 6. Exact D20 split and faces

The independent classifier implements exactly

\[
\mathcal D_{20}=
\{\rho\geq\rho_c,\ \rho<39/50,\ K>k_{11}(\rho),\ K<U(\rho)\}.
\]

It exhaustively checked all \(3^5=243\) combinations of below/equal/above
relations to \(\rho_c\), \(39/50\), \(k_{11}\), \(U\), and 200. On every row,

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}
\]

are disjoint and their union is exactly \(\mathcal D_{20}\). Thus the exact
set expression

\[
\mathcal D_{21}^{\rm proposed}
=\mathcal D_{20}\setminus(\mathcal C_{21}\cup\mathcal T_{21})
\]

is empty.

The shared-frequency truth table reproduced exactly:

| live D20 point | compact theorem guard | aggregate theorem guard | unique subtraction owner |
|---|---|---|---|
| \(K<200\) | yes | no | compact |
| \(K=200\) | yes | yes | compact only |
| \(K>200\) | no | yes | aggregate |

The exact constant checks place the compact guard faces \(\rho=7/51\) and
\(K=12\) outside \(\mathcal D_{20}\). The classifier includes the
\(\rho=\rho_c\) face only with both strict frequency inequalities, excludes
\(\rho=39/50\), excludes \(K=k_{11}\), and excludes \(K=U=K_0\). It also
checked all three possible orderings:

- if \(U<200\), every residual point is compact-owned and \(K=200\) is
  outside the residual;
- if \(U=200\), the strict upper face excludes \(K=200\), so every residual
  point is again compact-owned;
- if \(U>200\), points below 200 and the shared face 200 are compact-owned,
  while points strictly between 200 and \(U\) are aggregate-owned.

This empty proposed set is exact bookkeeping. It does not by itself make the
successor residual live or authorize a State Patch; valid theorem subtraction
still requires the separate A3 analytic verdict and later promotion gates.

## 7. Executed verification

~~~text
$env:PYTHONDONTWRITEBYTECODE='1'
python -m py_compile computations/round21_verify_exact_d20_closure.py computations/tests/test_round21_verify_exact_d20_closure.py
PASS

python -m computations.round21_verify_exact_d20_closure --high-precision 384
ROUND21_EXACT_D20_CLOSURE_A4 PASS
authenticated_inputs=18
exact_constants=PASS
exact_set=PASS (243 sign rows; proposed D21 empty)
compact[256]=PASS leaves=10580 floor_comparisons=2153076
compact[384]=PASS leaves=10580 floor_comparisons=2153076
aggregate_base_K200[192]=PASS boxes=1286 sign_checks=14146 endpoint_checks=2572
aggregate_base_K200[384]=PASS boxes=1286 sign_checks=14146 endpoint_checks=2572 derivative_points=1286
aggregate_scope=finite outward predicates at K=200 only
analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED

python -m pytest -q computations/tests/test_round21_verify_exact_d20_closure.py
8 passed in 114.81s

python -m pytest -q
328 passed, 1 xfailed, 10 subtests passed in 151.79s
~~~

The reported xfail is pytest-designated and is not a failure of this audit.

## Final decision

**PASS. First issue: none.** The compact 256/384-bit finite certificate,
aggregate 192/384-bit \(K=200\) base certificate, exact schemas, outward
faces, strict walls, branches, derivative consistency checks, containment
constants, and exact D20 owner split all pass unconditionally within A4's
scope.

The analytic implication from the compact proxy to the spectral theorem and,
especially, the aggregate reconstruction plus the universal chain
(A25)--(A30) for every \(K\geq200\) remain A3 obligations. This A4 PASS does
not claim or substitute for those results.
