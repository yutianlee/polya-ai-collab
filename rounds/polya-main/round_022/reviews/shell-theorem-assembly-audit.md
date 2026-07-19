# Round 22 theorem assembly and provenance audit

Date: 2026-07-15

Role: independent A4 theorem-assembly/provenance audit

## Verdict

**PASS. First issue: none.**

The incumbent reconstructs exactly the frozen unit-shell theorem, keeps the
strict counting convention at every threshold, closes the middle ratio range
only through the promoted complete Round 21 cover, derives the Weyl
coefficient and arbitrary-radius scaling in the correct direction, and makes
no graph or program-level promotion. The current graph and every final
Round 21 source-execution artifact used by that cover authenticate. Failed,
unscoped, stale-hash, and cache-vulnerable predecessors remain negative
chronology and are not revived.

I formed this verdict without reading the Round 22 clean-room theorem report.

## 1. Frozen inputs and current bytes

The theorem packet still reproduces the identity declared by the freeze:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | 6,568 | 244 |
| `rounds/polya-main/round_022/exploration/theorem-claim-freeze.md` | `6c332d8b2ab388e81a7b190e2674912227271a3425ea3e0ecac99fdaf950f99d` | 2,157 | 60 |
| `rounds/polya-main/round_022/reviews/theorem-claim-scope-audit.md` | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` | 8,228 | 205 |
| `rounds/polya-main/round_022/responses/shell-theorem-incumbent.md` | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` | 6,141 | 290 |
| `state/proof_obligations.yml` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 |

The freeze's baseline
`07df801fe031e55d53a46c25e3ae98d27a8ad8e4` is an ancestor of the audit-time
`HEAD`, `96fc9a1ec25efc45e430ed6e807b509e96cfcf3b`. The intervening commit adds the
Round 22 packet, freeze, and scope audit. The authoritative graph blob at the
baseline, at `HEAD`, and in the working tree is byte-identical and has the
frozen SHA-256 above. Thus the scope audit's statement that the baseline was
the then-current `HEAD` is historical audit-time wording, not a stale-graph
dependency.

All five files above strict-decode as UTF-8 without a BOM. They use LF only,
have exactly one terminal LF, and contain no tab, trailing-whitespace line,
replacement character, or forbidden control byte. `git diff --check` is
clean. The incumbent is an unpromoted working artifact; unrelated Round 22
non-tiling work is outside this theorem audit and is not used below.

## 2. Graph authority, status, and acyclicity

The canonical validator reports `Graph OK`. Independent parsing gives 60
obligations with 60 unique ids, all evidence paths used here exist, the
positive/negative/inconclusive evidence sets are disjoint, and the dependency
digraph has no cycle.

The packet's five direct inputs have exactly the required statuses:

| permitted input | status |
| --- | --- |
| `CONV-strict-counting` | `proved_internal` |
| `SHELL-sturm-liouville-completeness` | `proved_internal` |
| `SHELL-rho-zero-endpoint` | `proved_internal` |
| `SHELL-rho-compact-analytic-envelope` | `proved_internal` |
| `SHELL-rho-one-endpoint` | `proved_internal` |

Every dependency of `SHELL-rho-compact-analytic-envelope`, including
`SHELL-exact-d20-closure`, is itself `proved_internal`. The envelope points
forward to `SHELL-rho-compact`; it does not depend on that open output, so the
incumbent's middle-range invocation is not circular.

The nonpremise outputs remain unchanged:

| output or legacy node | status |
| --- | --- |
| `SHELL-rho-compact` | `open` |
| `SHELL-rho-uniformity` | `open` |
| `TARGET-shell-d3` | `open` |
| `POLYA-program-target` | `open` |
| `COMP-certified-bessel` | `diagnostic_only` |

The two Round 21 finite obligations alone are `certified`. The obsolete
diagnostic parent is neither a theorem premise nor a transitive route to the
incumbent conclusion.

## 3. Exact theorem union and seam audit

The constant proof in incumbent lines 46--76 is exact. From

\[
3\sqrt3>5>\pi
\]

one gets \(\omega_0>0\). The bounds \(\sqrt3<2\) and \(\pi>3\) give
\(\omega_0<1/6\). Since \(1+2C_*>1\),

\[
0<\rho_*<\omega_0<\frac16<\frac78.
\]

Consequently the incumbent's union

\[
(0,1)=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}[7/8,1)
\]

is disjoint and exhaustive. The outer seam owners are exact:

- \(\rho=\rho_*\) is included only in the small-hole outer branch;
- \(\rho=7/8\) is included only in the thin-shell outer branch; and
- neither \(\rho=0\) nor \(\rho=1\) is asserted to be a shell in the theorem.

For \(K>0\), the small-hole and thin-shell branches invoke their promoted
inputs on exactly their declared domains. For the open middle interval, the
incumbent defines \(\mathcal A_{21}\) as the complete accepted cover retained
by the promoted analytic-envelope obligation and uses its exact complement
\(\mathcal D_{21}=\varnothing\). This is a legitimate use of the fourth
whitelisted input, not an assumption of `SHELL-rho-compact`: the promoted
envelope statement itself retains the complete predecessor cover and exact
successor subtraction.

Although the incumbent does not reprint every historical mask formula, it
does not replace them by a rectangular proxy. The authenticated Round 17--21
chain gives the following exact ownership ledger:

- the original lower and upper walls \(1/(2\rho)\), \(H_0(\rho)\),
  \(z_\rho=\pi/(1-\rho)\), \(K_0(\rho)\), and the seam upper floor retain
  their accepted owners, including the \(H_0=K_0\) switch;
- the ratio interfaces \(1/16\), \(\rho_{HK}\), \(\omega_0\),
  \(\rho_c\), \(1/2\), \(5/6\), and the historical thin interfaces retain
  their exact one-sided or shared-face conventions;
- Round 17 owns through \(k_2(\rho)\), Round 18 through
  \(k_5(\rho)\), Round 19 through \(d=\sqrt{337}/2\) below \(\rho_c\)
  and \(k_6(\rho)\) at and above \(\rho_c\), and Round 20 through
  \(k_{11}(\rho)\);
- \(\rho_0=1/\sqrt{337}\) remains in the first Round 19 residual piece
  because its candidate lower fiber is empty, and that whole lower residual
  is then removed by the Round 20 lower closure;
- \(\rho=\rho_c\) is retained on the high-side ratio cell and, in the final
  residual, only strictly above \(k_{11}(\rho)\);
- \(\rho=39/50\) is owned by the Round 20 all-frequency optical theorem;
- \(K=U(\rho)=K_0(\rho)\), the global high-frequency face, and every
  staircase lower face remain covered and outside the later residual; and
- the old closed boxes \(B_0,B_1\) lie inside the already analytic Round 17
  band and remain regression evidence only, so neither is subtracted again.

Thus the abstract \(\mathcal A_{21}\) invocation in incumbent lines 130--149
has an authenticated exact union behind it. Lines 151--171 correctly unpack
the only live successor seam rather than substituting an older
\(\mathcal D_{17}\), \(\mathcal D_{18}\), or \(\mathcal D_{19}\).

## 4. Strict count and the zero-frequency face

The incumbent uses

\[
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}
\]

with multiplicity throughout. The Sturm--Liouville input gives

\[
\lambda_{\ell,n}\geq \frac{\pi^2}{(1-\rho)^2}>0,
\]

so the separate calculation

\[
N_D(A_{\rho,1},0)=0=W(\rho,0)
\]

is valid and uses no continuity from positive frequency.

No floor is recomputed in the assembly. At an eigenfrequency the threshold
root is excluded. In the inherited exact phase identity, if
\(\Psi_{\ell+1/2,\rho}(K)=m\pi\), the channel count is \(m-1\), not the
ordinary floor \(m\). If several angular channels share that eigenvalue, the
orthogonal multiplicities add while the root is excluded in every channel.
The first positive eigenfrequency, integer phase walls, and cross-channel
coincidences therefore retain the frozen strict convention.

## 5. Exact D20 closure, K=200, and evidence roles

The accepted live residual is exactly

\[
\mathcal D_{20}=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\]

The source-execution chain proves the exact guards

\[
\frac7{51}<\rho_c,
\qquad
k_{11}(\rho)>12\quad(\rho_c\leq\rho<1).
\]

The upper ratio wall is indispensable: \(z_\rho\) is undefined at
\(\rho=1\), and at \(\rho=2\),

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Every D20 point satisfies \(\rho<39/50<1\), so the scoped guard applies
exactly where used. It gives \(K>k_{11}(\rho)>12\), while
\(7/51<\rho_c\) puts the ratio inside the compact rectangle.

Define

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

Then every compact-owner point is in
\([7/51,39/50]\times[12,200]\), and every aggregate-owner point is in
\([\rho_c,39/50]\times[200,\infty)\). At \(K=200\) both theorem domains
apply, but only \(\mathcal C_{21}\) subtracts the face. The definitions work
unchanged for \(U<200\), \(U=200\), and \(U>200\). The faces
\(\rho=39/50\), \(K=k_{11}(\rho)\), and \(K=U(\rho)\) were already outside
D20 and are not subtracted again. Hence

\[
\mathcal D_{20}=\mathcal C_{21}\mathbin{\dot\cup}\mathcal T_{21},
\qquad \mathcal D_{21}=\varnothing.
\]

The incumbent preserves the finite/analytic boundary exactly:

- 10,580 compact leaves certify finite proxy predicates only on the closed
  rectangle \([7/51,39/50]\times[12,200]\); the promoted analytic bridge
  owns the spectral transfer;
- 1,286 aggregate boxes certify only the outward base predicates at
  \(K=200\); and
- the derivative, curvature, and two-integration argument, not finite boxes,
  owns the universal aggregate conclusion for every \(K\geq200\).

## 6. Reproduced final Round 21 source-execution chain

The current final-cycle identities reproduce exactly:

| role | SHA-256 |
| --- | --- |
| scoped candidate | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| final wrapper | `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9` |
| final tests | `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99` |
| final A4 report | `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5` |
| final cross-comparison | `7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a` |
| fresh source-exec referee | `d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28` |
| final provenance/isolation audit | `f4670818af3a57a965f0032edd72ea875d4ad618f9cc4a5b1b78cabdc7e481da` |
| lemma judge | `a620175fc43591cd80fcc9f50165d7b21596b077d92fbc4450167d21a4eca9aa` |
| final pre-application State-Patch audit | `bcd67c3939892c4014026c0ebc5103033bdd33dc68f67082f7bd32ef8c0d84fa` |
| post-application audit | `c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef` |

I launched the final wrapper from its authenticated in-memory source bytes
under isolated `python -I -B -`, with optimization zero and no import loader.
The 384-bit replay returned:

~~~text
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
~~~

Three independently selected focused regressions also passed from
authenticated wrapper/test bytes under an isolated fresh cache prefix: the
timestamp-valid malicious-`.pyc` attack, restoration of all prior
`sys.modules` states after execution failure, and the exact constants,
243 face rows, three \(U\)-orderings, and unique \(K=200\) owner.

The current positive producer identities also reproduce:

- compact producer/tests/canonical digest:
  `2a436116...`, `29b7425c...`, `96e527b4...`;
- aggregate producer/tests: `fc48425c...`, `50f10033...`.

The graph's 18 positive exact-D20 paths all exist at their recorded bytes.
The rejected packet `415546156e...`, the unscoped A4 report `d9def12c...`,
the cache-vulnerable report `55f4f574...`, its authoritative FAIL
`d9a8fd94...`, the old wrapper/test cycles `4868dcc3.../6716ff1b...` and
`64854c95.../c9747c8c...`, the intermediate repair snapshots
`c501608c.../d5dab951...`, the prior cross/referee/provenance reports
`e923c034...`, `c0a5239c...`, and `48b259a9...`, and the earlier branch,
lifecycle, and provenance failures remain superseded or negative. None is
used to authenticate the final source semantics.

## 7. Weyl normalization, Lambda substitution, and dilation

The incumbent correctly derives

\[
L_3=\frac{\omega_3}{(2\pi)^3}
=\frac{4\pi/3}{8\pi^3}=\frac1{6\pi^2},
\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\]

and therefore

\[
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3).
\]

For every \(\Lambda\geq0\), \(K=\sqrt\Lambda\) is nonnegative and
\(K^3=\Lambda^{3/2}\). The already separate \(K=0\) proof covers
\(\Lambda=0\), so no endpoint is lost in the substitution.

For \(0<r<R\), with \(\rho=r/R\), the map

\[
(D_Ru)(x)=R^{-3/2}u(x/R)
\]

is unitary from \(L^2(A_{\rho,1})\) to \(L^2(A_{r,R})\), and its quadratic
form scales by \(R^{-2}\). Hence

\[
A_{r,R}=R A_{\rho,1},\qquad
\lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}),
\]

so strict threshold comparison gives the correct direction

\[
N_D(A_{r,R},\Lambda)=N_D(A_{\rho,1},R^2\Lambda),
\]

not an argument \(R^{-2}\Lambda\). Substitution yields

\[
\frac{2}{9\pi}(1-\rho^3)(R^2\Lambda)^{3/2}
=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2}.
\]

This is valid for every \(R>0\), including \(R<1\) and \(R>1\). The theorem
keeps \(r=0\) and \(r=R\) outside its class at equality.

## 8. Scope and final determination

The incumbent proves only the three-dimensional spherical-shell spectral
inequality and its dilation corollary. It does not claim a Weyl remainder,
tiling or non-tiling theorem, novelty, publication priority, ellipse result,
certificate-family result, or program-target completion. Its status line and
closing scope paragraph explicitly leave promotion to later theorem-level
review and a separately audited State Patch.

**Final verdict: PASS. First issue: none.** The incumbent is a sound,
noncircular assembly of the exact frozen theorem from authenticated promoted
inputs, with every endpoint and evidence-role boundary preserved.
