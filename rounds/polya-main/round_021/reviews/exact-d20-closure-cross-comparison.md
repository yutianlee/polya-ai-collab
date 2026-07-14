# Round 21 Exact-D20 Closure Cross-Comparison

Date: 2026-07-15

## Verdict

**FAIL — evidence/lifecycle gate only.** The mathematical reconstruction is
consistent: the compact bridge, aggregate \(\mathcal Q/\mathcal B\) chain,
all-\(K\) calculus argument, exact guards, face ownership, and repaired
Machin branch proof all recheck. The 384-bit A4 replay also passes.

The first live discrepancy is narrower but binding. The preserved A4
branch-gap record says that a valid repair **must** test mutations that lose
either a Machin range bound or the branch conclusion. The final test file
does neither. It calls `verify_exact_constants()` and positively asserts the
returned bounds, but it never mutates or removes either range bound, and the
wrapper exposes no executable branch-conclusion predicate that a test could
mutate. Consequently the repaired mathematics is correct, but the final A4
cycle does not satisfy its own preserved replacement criterion and cannot yet
serve as positive lifecycle evidence.

No candidate, contract, analytic proof, certificate, residual, or set formula
needs mathematical repair for this verdict.

## Authenticated identities compared

The current bytes reproduce the frozen identities:

| role | SHA-256 |
|---|---|
| accepted residual packet | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| residual freeze | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| residual audit | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |
| frozen exact-D20 candidate | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| compact contract | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| aggregate contract | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| replacement freeze | `75afe7f0ea6ca2da4106510f6e90fb64a13a83fd83f023361d3433493d64558c` |
| replacement isolation audit | `d4aaf2676c9056721b919f5b24341e39e77178b27a49bfaa5b54a8e77eb6c57e` |
| compact verifier / report / adversarial audit | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` / `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` / `aac8cc7349b7531ced93ed5fa244efe2d8210999161868e90fd531943b2fc0ca` |
| aggregate route / verifier / report / adversarial audit | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` / `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` / `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` / `aa12d25d71091cfd01a116bc2777afa8669248a13441be391cf3da0b48c9a894` |
| A3 clean-room review / typography addendum | `0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc` / `d003d105038e78a0b95137b9fecb0ca5758a804dac17cbea1e6eea155f50b257` |
| preserved initial A4 branch-gap record | `3d234405e5776b31dea29fbff8ee2803d0f54052cab851240b81546e9ac1b7f2` |
| final A4 wrapper / tests / report | `85b661401544dac0398251480cadc5736fa7ac3941f47684e61d891da30756a0` / `10940d66a5ec0f0e9d42f9d57205de840bb3ea78c92f13cdd08a66f8e9da5713` / `e49458c1ec592c46f66f3ebf0a6c69682582e2392566230f686eca8fdbd7a0ed` |
| incumbent exploratory synthesis | `e04b8199783188f0d90b6c033abe031d7c9ecd54ee1a5cdfd198f3517e98d039` |

The A3 addendum corrects eight typography-only defects in the immutable A3
report, including its two form-feed bytes. With those exact corrected
readings, no mathematical disagreement remains. The incumbent synthesis is
an earlier exploratory artifact with stale conditional wording and malformed
display bytes; it agrees in substance but is not proof evidence.

## Independent mathematical reconstruction

### Exact residual and compact bridge

The accepted residual is exactly

\[
\mathcal D_{20}=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\]

From \(\pi<22/7\),
\(1+2\pi<51/7\), hence \(7/51<\rho_c\). For
\(\rho\geq\rho_c\),
\(z_\rho\geq\pi+1/2>7/2\), so
\(k_{11}^2=z_\rho^2+132>577/4>12^2\). Thus every residual point with
\(K\leq200\) lies in the certified closed rectangle
\([7/51,39/50]\times[12,200]\).

Analytically, zero extension makes both phase interfaces exact, the strict
separated count gives \(N_D\leq P_{\rm coarse}\), and
\(P_{\rm coarse}\) decreases in \(\rho\) and increases in \(K\), while the
Weyl term decreases in \(\rho\) and increases in \(K\). Therefore the
contract's opposite corners are the correct leaf bounds, including strict
integer walls and shared faces. Executably, the sealed certificate replays
10,580 leaves, 16,020 proxy corners, 2,153,076 floor comparisons, and zero
wall straddles at 256 bits and again at 384 bits. The executable signs do not
by themselves prove the spectral bridge; that implication is the A3
analytic argument.

### Aggregate interface and universal propagation

Write
\(\mu=\rho K\), \(C=2\pi\rho K/(1-\rho)\), and
\(\mu-1/2=J+\tau\), \(0\leq\tau<1\). If \(R\) is the actual number of
low tails, the discrete reserve is

\[
\mathcal Q=
R\lfloor K\eta_\rho\rfloor+
\frac{d_\rho J(J+1)}2-(1+d_\rho)\mathcal I(C,R)
-\frac{8R\tau^{5/2}}{15\sqrt\mu}.
\]

The exact identities \(R=J\) at \(\tau=0\), \(R=J+1\) otherwise,
\(n_r=J-r\), and \(\sum n_r=J(J+1)/2\), together with the strict shelf
bound and midpoint Hermite--Hadamard inequality, give
\(\mathcal Q\geq0\Rightarrow N_D<W\), with strictness surviving both
\(\tau=0\) and integer \(K\eta_\rho\) walls.

For \(\overline R=\mu+1/2\), the continuous reserve is

\[
\mathcal B=(\mu-\tfrac12)(K\eta_\rho-1)
+\frac{d_\rho}{2}(\mu-\tfrac32)(\mu-\tfrac12)
-(1+d_\rho)\mathcal I(C,\overline R)
-\frac{8(\mu+1/2)}{15\sqrt\mu}.
\]

The floor inequality, the exact \(J,R\) comparisons, monotonicity of
\(\mathcal I\), and \(0\leq\tau<1\) give the strict relation
\(\mathcal Q>\mathcal B\). Hence
\(\mathcal B\geq0\Rightarrow\mathcal Q>0\Rightarrow N_D<W\).

For fixed \(\rho\), with
\(b=2\pi\rho/(1-\rho)\),
\(S=\sqrt{\overline R^2+bK}\), direct differentiation gives

\[
I_{KK}=\rho^2\left(\frac{\overline R}{S}-1\right)
+\frac{\rho b}{2S}+\frac{b(2\rho K-1)}{8KS},
\qquad
E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}.
\]

On the rational superset and for every \(K\geq200\),
\(\mu>3/2\), \(K\eta_\rho>1\), and
\(S>\overline R>\rho K\). Therefore

\[
I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}\leq\frac{3b}{800},
\qquad E_{KK}>0,
\]

and
\(\mathcal B_{KK}>F(\rho)\). The finite A4 certificate proves only
\(\mathcal B(\rho,200)>0\),
\(\mathcal B_K(\rho,200)>0\), and \(F(\rho)>0\), plus consistency signs,
on 1,286 exact ratio boxes. A3 then performs the two integrations from
\(K=200\) to obtain \(\mathcal B_K>0\) and \(\mathcal B>0\) for every
\(K\geq200\). There is no finite-versus-universal scope mismatch in the
replacement contract or final wrapper.

### Exact faces and proposed successor

The owners are exactly

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

Both theorem domains include \(K=200\), but only the compact set owns it.
If \(U<200\), every residual point is compact-owned; if \(U=200\), the
strict face \(K<U\) excludes \(K=200\); if \(U>200\), the three frequency
rows split exactly as stated. The faces \(\rho=39/50\), \(K=k_{11}\), and
\(K=U\) remain excluded. The 243 sign rows and the three explicit
\(U\)-ordering cases therefore correctly make the proposed \(\mathcal
D_{21}\) empty as bookkeeping. This executable emptiness does not substitute
for the analytic theorems or authorize promotion by itself.

## Repaired Machin argument and first discrepancy

The repaired analytic argument is valid. Exact arithmetic gives

\[
\tan(4\arctan(1/5))=\frac{120}{119},\qquad
\tan(4\arctan(1/5)-\arctan(1/239))=1,
\]

and alternating-series bounds give

\[
\frac34<\frac{70369}{89625}
<4\arctan(1/5)-\arctan(1/239)<\frac45<1.
\]

The principal \(\arctan(1)=\pi/4\) is also in \((0,1)\), and tangent is
injective there, so the unwanted \(\pi/4+n\pi\) branches are excluded. Four
alternating terms then prove \(3<\pi<22/7\). This is an analytic proof,
supported by exact executable rational checks; the tangent identity alone is
not the proof.

The preserved failure record nevertheless required active mutation tests for
both kinds of loss. In the final tests, the only exact-constant test calls the
function and asserts
`machin_angle_lower == Fraction(70369, 89625)` and the positive chain
`3/4 < lower < upper == 4/5 < 1`. It contains no failing mutation of either
bound. The wrapper's `ExactConstants` object contains only numerical bounds,
not a branch-selection or Machin-identity conclusion, so there is also no
branch-conclusion mutation test. Repository-wide inspection found no other
Round 21 test supplying either missing mutation. A passing positive assertion
is not the required mutation test.

This is the first current discrepancy. It does not refute the proof, but it
does prevent the repaired A4 bytes from meeting the explicitly preserved
acceptance condition.

## Reproduction and chronology

The current command

```text
python -B -m computations.round21_verify_exact_d20_closure --high-precision 384
```

passed in 160.1 seconds with 18 authenticated inputs, exact constants, 243
set rows, both compact replays, and aggregate replays at 192 and 384 bits.
The aggregate replay reported 1,286 boxes, 14,146 finite signs, 2,572 endpoint
containments, and 1,286 high-precision derivative points, followed by the
explicit scope marker `A3_REQUIRED_NOT_CLAIMED`. A targeted positive
exact-constants/set test also passed. These successes confirm the mathematics
and current executable behavior, but cannot supply a mutation test that the
test source does not contain.

The earlier candidate isolation failure over an ambiguous aggregate
frequency quantifier is correctly preserved and repaired by the current
candidate/contract bundle. Separately, the rejected first A4 cycle has
wrapper/test/report hashes `202255...`, `0b4ae6...`, and `8ce515...`; the
intermediate `6d2ae...` / `4360cb...` pair remains non-evidence. The preserved
branch-gap report was committed before the final repaired A4 bytes. The
present failure therefore does not resurrect either old mathematical gap; it
enforces the still-unsatisfied mutation-hardening condition stated in that
negative chronology.

## Required next repair

Add an executable branch-certificate/conclusion predicate and adversarial
tests that fail when either exact range bound is lost and when the branch
conclusion is removed or changed. Then rerun both certificate precisions,
focused tests, and the full suite; freeze new wrapper/test/report hashes; and
repeat this cross-comparison. The candidate, residual, contracts, A3 proof,
and sealed compact/aggregate certificates should remain unchanged.
