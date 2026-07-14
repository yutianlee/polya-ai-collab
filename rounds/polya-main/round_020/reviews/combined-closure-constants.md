# Round 20 Combined Closure: Independent Exact-Constant Audit

Verdict: **PASS (A4 finite arithmetic only)**.

First issue: **none**.

This verdict does not certify the three analytic theorem claims by itself. It
certifies that the frozen candidate's finite arithmetic, conditional on the
analytic premises listed below, is internally consistent and has the stated
strict face ownership. The isolated A3 reconstruction must still prove those
premises.

## Authentication and isolation

Before reading either released file, I authenticated:

| artifact | required and observed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |

I then authenticated all five permitted residual artifacts and all ten
permitted foundational packets/source cards against Section 7 before reading
them. The executable verifier hard-gates all 17 permitted files. No Round 20
exploration proof, zero-bound card, non-permitted calculation/ledger, incumbent
response, judge draft, repository diff/log, or other reviewer's output was
inspected.

Verifier artifacts at the time of this report:

| artifact | SHA-256 |
|---|---|
| `computations/round20_verify_combined_closure.py` | `44a5e840d9f60fb58701b506d21688e15403d295fc9111081d08e982c3ca7de7` |
| `computations/tests/test_round20_verify_combined_closure.py` | `61df4f0b8ed18ee24a3d16ae1b3db189ae099abf86fe334f2a0067f12cc09ca2` |

The review file's final hash is necessarily recorded after its final bytes are
written.

## Exact method

The verifier uses `fractions.Fraction` and integer arithmetic only. It derives
a certified interval for pi from Machin's formula

$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$

with alternating-series remainders, and proves in particular

$$
\frac{333}{106}<\pi<\frac{22}{7},
\qquad \frac1\pi<\frac{106}{333}.
$$

Radicals are enclosed by integer square roots on a rational decimal grid.
Spherical-Bessel signs at rational walls are enclosed by exact rational Taylor
remainders; signs at tangent half-periods use the exact sine/cosine values and
the spherical recurrence. There are no floating-point literals, sampled roots,
or numerical tolerances in any passing condition.

The full run performs 2,082 labelled exact checks, including the 34 source
hash/existence gates.

## Finite results

### Thresholds, branches, and lower faces

The checker proves

$$
\rho_*<\rho_0<\sigma<\rho_c<\frac{39}{50}<\frac78,
\qquad \omega_0d>1,
$$

and the complete fixed-wall order

$$
d<10<\frac{81}{8}<\frac{21}{2}<\frac{\sqrt{7073}}8<\sqrt{114}
<\frac2{\omega_0}<\frac{367}{20}.
$$

It also verifies every ordering change of the moving wall `3 z_rho` against
`10`, `81/8`, `21/2`, `sqrt(7073)/8`, and `sqrt(114)`; each unique crossing is
strictly between `rho_0` and `rho_c` and occurs in the displayed fixed-wall
order.

Because `omega_0<rho_c`, `H_0` is ineligible throughout the high strip. Below
`5/6`, `U=K_0`. The exact endpoint reduction

$$
\omega_0\sqrt{4\pi^2+132}<C_0
$$

passes, and the derivative sign reduction makes
`eta(rho) k_11(rho)` maximal at `rho=1/2`. Hence the positive-root identity for
`K_0` gives `k_11<K_0`. On the seam branch, squaring reduces the remaining
check to

$$
\pi^2s^2+132s^4<54^2,\qquad 0<s\le\frac16,
$$

which also passes. Thus the finite branch reductions give
`k_11<U` on `rho_c<=rho<7/8` and `U=K_0` on
`rho_c<=rho<39/50`, conditional only on A3 writing the stated elementary
monotonicity argument.

### Zero walls and lower inventories

All eleven walls in (27) have the required exact spherical-Bessel sign. For
the eight internally reconstructed walls, the rational point lies strictly in
the stated tangent half-period, its sign agrees with the left endpoint, and
the opposite sign occurs at the right endpoint. For the remaining first-zero
walls at angular indices 8, 9, and 10, the exact Lorch `(L2)` specialization is
strictly stronger than the proposed rational square. These are finite sign and
specialization checks; the assertion that the bracket contains the relevant
numbered positive zero remains an A3 Sturm/ODE enumeration step.

The six lower caps recompute exactly as

$$
45,\ 46,\ 59,\ 66,\ 69,\ 78.
$$

The propagation identity for the `c_42` wall is

$$
\left(\frac{81}{8}\right)^2+8=\frac{7073}{64}.
$$

Every omitted first, second, third, or higher radial/angular tail is excluded
at the included `sqrt(114)` face by a strict zero wall, channel comparison, or
monotone propagation. Each cap has a strict uniform Weyl payment at its open
lower frequency face.

For the exceptional cell, the exact radial proxy list is

$$
(6,5,5,4,4,3,3,3,2,2,1,1,1,1,0,\ldots),
$$

and its multiplicity-weighted sum is exactly

$$
\sum_{\ell=0}^{13}(2\ell+1)c_\ell=395.
$$

The `ell=14` proxy is strictly below one, and monotonicity removes every later
angular tail. The constrained Weyl payment is strictly greater than 395.
The floor analysis proves `p>=1`; for `p>=2`,

$$
\frac32(p+1)\le 2p+\frac12,
$$

with the required strictness from `rho_c<3 omega_0/2`. Therefore failure of
`m<=2p-1` is exactly the `p=1`, `rho K>=5/2` cell. The face `rho K=5/2`
belongs to the high half-integer side, while `K=2/omega_0` has `p=2` and
belongs to the complement.

### High checkpoints

At `k_7,...,k_11`, the program independently combines the channel lower bound
with the strict zero registry and angular propagation. It reproduces the five
nested inventories, proves all omitted radial and angular tails absent, and
checks every full multiplicity.

Every numerical cap in the `k_8` and `k_9` matrices and every row in the
`k_10` and `k_11` tables is exactly the sum of complete square blocks. The
three families of marked impossible cells reduce to incompatible rational
conditions on `z_rho^2` and pass strictly:

- `k_8`, `H=6`, second `h>=2`;
- `k_9`, `H=8`, any second mode;
- `k_9`, `H=7`, second `h>=3`.

The verifier decides both one-sided channel traces at every rational face in
(28), at `4/25`, `1/4`, and `7/20`, and checks the algebraic faces
`z_rho^2=16,68/3,34`. In particular,

$$
110-6\cdot7-3\frac{68}{3}=0,
\qquad
132-5\cdot6-3\cdot34=0,
$$

so strict counting excludes the defining modes at the latter two equality
faces.

The four stated `k_11` localizations pass exactly: a second mode forces
`rho<8/15`, a third mode forces `rho<1/4`, `H=10` excludes all second and
third modes, and `H=9` excludes all third modes.

For payments, differentiation reduces monotonicity of the checkpoint Weyl
quantity to

$$
\pi^2(1+\rho)>m(m+1)\rho^2(1-\rho)^2.
$$

Uniformly for `m<=11`, this follows from
`pi^2>9>132/16`. The global payments cover caps
`40,53,73,89,121`; the larger conditional cells are paid at the exact first-zero
localization. All proposed high cap/payment cases pass.

### Optical constants

Writing `C_D=1382/3125`, the product deficit screen is increasing in integer
`N`, and its `N=1` derivative factors as

$$
2(t-C_D)(t+1).
$$

The exact minimum at `t=C_D` is

$$
\frac{1822532}{91552734375}>0.
$$

Thus the finite polynomial calculation proves

$$
D(a)>\frac{1382}{3125}a^2
$$

for every `N>=1`, `0<t<=1`, with `(N,t)=(m-1,1)` at `a=m pi`.

At `epsilon_0=11/50`, `c=1126/625`, and `q=106/333`, the low screen gives

$$
\frac{1382}{3125}
-\left(\frac{2cq}{3}+\frac{\varepsilon_0}{4}
+\varepsilon_0^2q^2\right)
=\frac{39569}{2772225000}>0.
$$

The high radial screen uses `pi<22/7`, and the full angular ceiling screen
uses `1/pi<q`. Their endpoint difference is exactly

$$
\frac{14817541}{472867032960000}>0.
$$

The lower cost is increasing in epsilon, the high radial reserve is decreasing,
and the angular error is increasing, all by coefficient/sign reductions on
`0<epsilon<=11/50`. Both pieces include `a=c/epsilon`. The exact angular and
phase-proxy equality conventions exclude their defining strict modes.

### Exact subtraction

An exhaustive symbolic truth table covers every ratio owner and every
frequency relation to `k_6`, `k_11`, and `U`. It confirms

$$
\mathcal D_{19}\setminus
(\mathcal D_{19}^{\rm low}\cup\mathcal C_{20}^{\rm stair}
\cup\mathcal C_{20}^{\rm opt})
=\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

The `rho_0` fiber is removed by the lower theorem, `rho_c` remains included,
`rho=39/50` is removed inclusively by the optical piece, `K=k_11` is owned by
the staircase, and `K=U` remains excluded. The already absorbed boxes `B_0`
and `B_1` are not subtracted again.

## Analytic assumptions still requiring A3

1. The separated strict-count identity and angular multiplicity rule.
2. The channel, fixed-radial-index shell-to-ball, and angular propagation
   inequalities (24)--(26), including their form-domain directions.
3. Tangent-cell enumeration, positive-zero numbering, ODE uniqueness, and
   simplicity for the eight internally reconstructed zero bounds.
4. The shifted-tail wedge, interface remainder, and strict aggregation outside
   the exceptional floor cell.
5. The strict phase-proxy implication used before the exact cap-395 sum.
6. The product min--max comparison and quarter-circle sum bound on the low
   optical piece.
7. The complementary-action curvature, Stieltjes radial deficit, exact
   layer-cake identity, angular error transfer, and phase transfer on the high
   optical piece.
8. The elementary differentiability arguments whose signs were reduced and
   checked here for `G_1`, `k_m`, and the checkpoint Weyl payments.

No finite arithmetic issue remains for A3 to repair.

## Commands and results

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
10 passed
```
