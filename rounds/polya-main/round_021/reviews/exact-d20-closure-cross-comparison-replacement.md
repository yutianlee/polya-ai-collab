# Round 21 Exact-D20 Closure Replacement Cross-Comparison

Date: 2026-07-15

## Verdict

**PASS. First issue: none.** The third A4 cycle closes the binding lifecycle
failure identified by the strict cross-comparison. The hardened wrapper
validates an exact immutable Machin principal-branch schema before it computes
any \(\pi\) enclosure, and independent mutations losing the lower bound,
upper bound, or principal-branch conclusion are rejected through the real
`verify_exact_constants()` entry point.

The repaired branch proof is mathematically noncircular. The compact and
aggregate certificate bytes, A3 analytic reconstruction, exact residual, and
candidate set split are unchanged and still agree. In particular, the A4
aggregate replay remains confined to finite predicates at \(K=200\); the
universal propagation to every \(K\geq200\) remains an A3 calculus argument.

## Byte identities and negative chronology

The current third-cycle artifacts reproduce:

| artifact | SHA-256 |
|---|---|
| hardened A4 wrapper | `4868dcc3251fe30aff4d8ef362cdd8924fe69d95cafa8d597fa9c88560780ff8` |
| hardened A4 tests | `6716ff1beaaf4053092f8e7baa4d77b95acf38f3fc3d467f15ec76e545271da7` |
| hardened A4 report | `d9def12c61006d4851202fe3100397e8d1505998dca84010e2d893a72ffacd56` |

The unchanged governing and proof artifacts reproduce:

| role | SHA-256 |
|---|---|
| exact-D20 candidate | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| compact contract | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| aggregate contract | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| replacement candidate freeze | `75afe7f0ea6ca2da4106510f6e90fb64a13a83fd83f023361d3433493d64558c` |
| replacement isolation audit | `d4aaf2676c9056721b919f5b24341e39e77178b27a49bfaa5b54a8e77eb6c57e` |
| accepted residual packet / freeze / audit | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` / `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` / `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |
| compact verifier / tests / report | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` / `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` / `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` |
| aggregate route / verifier / tests / report | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` / `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` / `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` / `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` |
| A3 clean-room review / typography addendum | `0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc` / `d003d105038e78a0b95137b9fecb0ca5758a804dac17cbea1e6eea155f50b257` |
| incumbent exploratory synthesis | `e04b8199783188f0d90b6c033abe031d7c9ecd54ee1a5cdfd198f3517e98d039` |

The negative chronology is preserved rather than overwritten:

1. The initial A4 cycle's wrapper/test/report hashes `202255...`,
   `0b4ae6...`, and `8ce515...` are non-evidence because tangent equality was
   used without selecting the principal branch. The preserved failure has
   SHA-256 `3d234405e5776b31dea29fbff8ee2803d0f54052cab851240b81546e9ac1b7f2`.
2. The second cycle's wrapper/test/report hashes `85b661...`, `10940d...`,
   and `e49458...` repaired the mathematics but omitted the required active
   lower-bound, upper-bound, and conclusion mutations. The strict FAIL
   cross-comparison has SHA-256
   `11672110bdc1169c40b46247832c19b9187df3112ab67f28324f6784a2f552a6`.
3. The concurrent initial referee PASS missed that lifecycle gate. Its miss
   is preserved at SHA-256
   `af1761a2426ad22f2cf93ea765e3b98af1314f4587730b654ed4eb36e37106ba`.
4. Commit `9c46cc79526291642b52c462284683daa735aea8`, whose parent is the preserved
   negative-cycle commit `cc00361e3670f1bd6b3042393c0764daf1f67cec`, changes only the A4 wrapper,
   A4 tests, and A4 report. It leaves every analytic, residual, candidate,
   contract, and sealed certificate byte unchanged.

Thus no rejected output is silently reused as current positive evidence.

## Hardened principal-branch path

### Exact schema and call order

The frozen `MachinBranchCertificate` contains exact `Fraction`, tuple,
boolean, and literal-string fields for:

- schema `round21-exact-machin-principal-branch-v1`;
- \(\theta=4\arctan(1/5)-\arctan(1/239)\);
- strict exact bounds
  \(70369/89625<\theta<4/5\) inside the open interval \((0,1)\);
- tangent as the injective function on that shared interval;
- principal \(\arctan(1)\) in the same interval;
- both tangent values equal to exactly \(1\); and
- the conclusion `theta=atan(1)=pi/4`.

There is no binary float, decimal display value, midpoint, or sampled
quantity in `alternating_arctan_bounds()`,
`validate_machin_branch_certificate()`, or `verify_exact_constants()`.
The bound constants are exact rational expressions, not decimal assertions.

Source order is decisive. `verify_exact_constants()` first derives
\(\tan\theta=1\) in exact rational arithmetic, then necessarily calls
`validate_machin_branch_certificate(...)`. Only after that call returns does
it invoke `alternating_arctan_bounds(5,4)` and
`alternating_arctan_bounds(239,4)` to form the \(\pi\) enclosure. Therefore a
failed branch schema cannot fall through to a \(\pi\) claim.

### Independent active mutations

I passed four `dataclasses.replace(...)` mutations through the real
`verify_exact_constants()` entry point while temporarily replacing
`alternating_arctan_bounds()` by a sentinel that would fail if any \(\pi\)
enclosure were reached. The observed results were:

| mutation | result before any \(\pi\) enclosure |
|---|---|
| `theta_lower_bound=None` | rejected: `Machin lower range bound missing or changed` |
| `theta_upper_bound=None` | rejected: `Machin upper range bound missing or changed` |
| `conclusion=None` | rejected: `Machin principal-branch conclusion missing or changed` |
| `conclusion="theta=atan(1)+pi"` | rejected by the same conclusion gate |

The sentinel was never reached. The unmodified real entry point then
returned schema `round21-exact-machin-principal-branch-v1`, lower bound
`70369/89625`, upper bound `4/5`, and conclusion
`theta=atan(1)=pi/4`. These are active failing mutations, not positive
assertions about a displayed value, and they exactly close the two preserved
lifecycle requirements.

### Noncircular mathematical branch selection

Let \(a=\arctan(1/5)\), \(b=\arctan(1/239)\), and
\(\theta=4a-b\). Exact tangent arithmetic gives

\[
\tan(4a)=\frac{120}{119},\qquad \tan\theta=1.
\]

Alternating-series bounds give

\[
\frac34<\frac{70369}{89625}
<\theta<\frac45<1.
\]

The placement of principal \(\arctan(1)\) in the same interval does not use
Machin's identity or a previously assumed upper bound for \(\pi\). From the
elementary integral definition,

\[
\arctan(1)=\int_0^1\frac{dt}{1+t^2},
\]

and the integrand is positive and strictly below \(1\) away from \(t=0\).
Hence \(0<\arctan(1)<1\) directly. Also
\(\cos x\geq1-x^2/2>0\) for \(0<x<1\), so tangent is strictly increasing
there. Since both angles lie in \((0,1)\) and both tangents equal \(1\),
\(\theta=\arctan(1)=\pi/4\). This excludes every
\(\pi/4+n\pi\) branch without circularity. The A4 report states the interval
fact; the integral above is its immediate elementary justification, so no
addendum is required.

Four alternating terms may therefore be applied to the established identity
to prove exactly \(3<\pi<22/7\).

## Unchanged mathematical cross-comparison

### Residual, guards, and compact coverage

The accepted residual remains

\[
\mathcal D_{20}=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\]

The exact upper bound \(\pi<22/7\) gives
\(7/51<\rho_c=1/(1+2\pi)\). For \(\rho\geq\rho_c\),
\(z_\rho\geq\pi+1/2>7/2\), so
\(k_{11}^2=z_\rho^2+132>577/4>12^2\). Thus every residual point with
\(K\leq200\) lies in the compact certified rectangle
\([7/51,39/50]\times[12,200]\).

The A3 compact bridge correctly uses zero extension at
\(\nu=\rho K\) and \(\nu=K\), the strict integer count, and the separated
phase inequality to obtain \(N_D\leq P_{\rm coarse}\). The proxy decreases
in \(\rho\) and increases in \(K\), while the Weyl term has the matching
opposite lower corner. The executable certificate supplies the finite leaf
signs: 10,580 leaves, 16,020 proxy corners, 2,153,076 floor comparisons, and
zero wall straddles at 256 bits, with the same leaves reverified at 384 bits.
Those executable signs do not replace the analytic spectral bridge.

### Aggregate \(\mathcal Q/\mathcal B\) chain

With \(\mu=\rho K\), \(C=2\pi\rho K/(1-\rho)\), and
\(\mu-1/2=J+\tau\), \(0\leq\tau<1\), the exact discrete reserve is

\[
\mathcal Q=
R\lfloor K\eta_\rho\rfloor+
\frac{d_\rho J(J+1)}2-(1+d_\rho)\mathcal I(C,R)
-\frac{8R\tau^{5/2}}{15\sqrt\mu}.
\]

The low-tail identities \(R=J\) at \(\tau=0\), \(R=J+1\) otherwise,
\(n_r=J-r\), and \(\sum n_r=J(J+1)/2\), together with the strict shelf
bound, give
\(\mathcal Q\geq0\Rightarrow N_D<W\), including the \(\tau=0\) and integer
\(K\eta_\rho\) walls.

For \(\overline R=\mu+1/2\),

\[
\mathcal B=(\mu-\tfrac12)(K\eta_\rho-1)
+\frac{d_\rho}{2}(\mu-\tfrac32)(\mu-\tfrac12)
-(1+d_\rho)\mathcal I(C,\overline R)
-\frac{8(\mu+1/2)}{15\sqrt\mu}.
\]

The floor inequality, exact \(J,R\) comparisons, monotonicity of
\(\mathcal I\), and \(0\leq\tau<1\) give \(\mathcal Q>\mathcal B\). Hence
\(\mathcal B\geq0\Rightarrow\mathcal Q>0\Rightarrow N_D<W\).

On \([7/51,39/50]\) and for every \(K\geq200\), A3 proves the guards
\(\mu>3/2\), \(K\eta_\rho>1\), and
\(S>\overline R>\rho K\). Its exact derivatives give

\[
I_{KK}=\rho^2\left(\frac{\overline R}{S}-1\right)
+\frac{\rho b}{2S}+\frac{b(2\rho K-1)}{8KS},
\qquad
E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}},
\]

so

\[
I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}\leq\frac{3b}{800},
\qquad E_{KK}>0,
\qquad \mathcal B_{KK}>F(\rho).
\]

The outward aggregate program certifies only the base predicates
\(\mathcal B(\rho,200)>0\),
\(\mathcal B_K(\rho,200)>0\), and \(F(\rho)>0\), with consistency signs, on
1,286 rational boxes. A3—not A4—uses the universal inequalities and performs
the two integrations from \(K=200\) to prove \(\mathcal B_K>0\) and
\(\mathcal B>0\) for every \(K\geq200\). The hardened source and CLI retain
this boundary exactly.

### Exact faces and successor bookkeeping

The subtraction owners remain

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

At \(K=200\), both theorem domains apply but compact is the unique owner. If
\(U<200\), all residual points are compact-owned; if \(U=200\), strict
\(K<U\) excludes the shared frequency; if \(U>200\), the stated split is
exact. The faces \(\rho=39/50\), \(K=k_{11}\), and \(K=U=K_0\) remain
excluded. The wrapper rechecks all \(3^5=243\) sign rows and all three
\(U\)-orderings, so the proposed \(\mathcal D_{21}\) is empty as exact set
bookkeeping. This executable identity does not itself promote a theorem or
authorize a state patch.

## Independent reproduction

The active mutation probe produced the four specific pre-enclosure
rejections listed above. The current focused command

```text
python -B -m pytest -p no:cacheprovider -q \
  computations/tests/test_round21_verify_exact_d20_closure.py
```

passed all **11 tests in 119.34 seconds**. The current wrapper command

```text
python -B -m computations.round21_verify_exact_d20_closure \
  --high-precision 384
```

passed in **111.9 seconds**, reporting:

- 18 authenticated inputs and exact constants;
- 243 exact set rows and empty proposed \(\mathcal D_{21}\);
- 10,580 compact leaves and 2,153,076 comparisons at both 256 and 384 bits;
- 1,286 aggregate boxes, 14,146 finite signs, and 2,572 endpoint checks at
  both 192 and 384 bits;
- 1,286 derivative consistency points at 384 bits; and
- the explicit markers `finite outward predicates at K=200 only` and
  `A3_REQUIRED_NOT_CLAIMED`.

I did not rerun the complete suite. Its recorded result of **331 passed, 1
xfail, and 10 subtests passed** is consistent with the source history: the
previous 328-pass suite gained exactly the three new mutation test functions,
and the hardened commit changes no other test module or live proof input.

## Final decision

**PASS. First issue: none.** The third-cycle exact branch schema, mandatory
pre-enclosure validation, and active range/conclusion mutations repair the
sole live lifecycle defect. The current hashes, successful replays,
noncircular branch selection, compact and aggregate analytic bridges,
finite-versus-universal scope boundary, exact guards, and every residual face
are mutually consistent. A fresh assume-false referee remains a separate
next workflow gate; it is not part of this cross-comparison verdict.
