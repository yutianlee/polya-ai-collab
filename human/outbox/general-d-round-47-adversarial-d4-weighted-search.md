# Round 47 independent adversarial search: the \(d=4\) weighted aggregate

**Date:** 21 July 2026  
**Role:** Prompt C, independent falsification search  
**Target:**

\[
 \mathrm{WT}_4=\mathcal B_4(A)+\sum_{a\geq1}aD_A(a)
 =W_4-P_4^{<}.
\]

## 1. Result and classification

The search found no negative value of the literal aggregate.  It also found
no resolved negative shifted defect \(D_A(a)\).  These positive observations
are finite diagnostics and prove no continuum statement.

It did find and rigorously certify a **class-B sufficient-route
counterexample**.  The tempting cellwise self-charge inequality

\[
 \mathcal B_{4,a}(A)+\frac{a(a+1)}2L_a\geq0
 \tag{C47.1}
\]

is false.  At the exact rational point

\[
 \rho=\frac9{10},\qquad K=40,\qquad \mu=36,
 \qquad a=29,
\]

directed arithmetic gives

\[
 L_{29}=-0.40027816954933858788\ldots,
\]

\[
 0.204<\mathcal B_{4,29}(A)<0.206,
\]

and hence

\[
 \mathcal B_{4,29}(A)+435L_{29}
 \in[-173.917,-173.915].
\]

At the same point the literal aggregate is exactly

\[
 \mathrm{WT}_4=4301>0.
\]

Thus (C47.1) is only a rejected localization.  It is **not** a
counterexample to literal \(\mathrm{WT}_4\), to a maximal-negative-
\(D_A\)-component theorem with neighboring charges, or to the spectral
Pólya theorem.

The required final classification is therefore:

```text
classification A (literal aggregate): NONE FOUND
classification B (sufficient route): CELL-SELF-CHARGE FALSE
classification C (positive witness): DIAGNOSTIC ONLY
```

## 2. Independence boundary and reconstruction

The evaluator
`computations/general_d_round47_independent_d4_weighted_search.py` imports no
Round-47 lead file or evaluator.  It reconstructs the literal quantities from
the shell action and from the master identity by two separate paths.

For \(R>0\), put

\[
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi}
 \quad(0\leq z<R),
\]

with zero extension, and \(A=G_K-G_\mu\), \(\mu=\rho K\).  The independently
used closed cap is

\[
 I_R(z):=\int_z^R G_R(s)\,ds
 =\frac{R^2}{4\pi}
 \left\{
 \theta(1+2\cos^2\theta)-3\sin\theta\cos\theta
 \right\},
 \quad \theta=\arccos\frac zR.
 \tag{C47.2}
\]

The strict count is evaluated literally:

\[
 q_a=[A(a)+1/4]_< =\max\{0,\lceil A(a)+1/4\rceil-1\}.
\]

Only \(1\leq a<K\) is stored.  In particular, if \(K\in\mathbb N\), the
endpoint \(a=K\) is absent and \(A(K)=0\).

### 2.1 Direct-proxy path

The direct path uses

\[
 W_4=\int_0^Kz^2A(z)\,dz
 =\frac{K^4-\mu^4}{64},
 \qquad
 P_4^{<}=\sum_{1\leq a<K}a^2q_a,
\]

and computes \(\mathrm{WT}_4=W_4-P_4^{<}\).

### 2.2 Bonus-plus-defect path

Independently, the code computes

\[
 T_A(a)=q_a+2\sum_{b>a}q_b,
 \qquad
 D_A(a)=2\{I_K(a)-I_\mu(a)\}-T_A(a),
\]

and the bonus in the exact discrete-integral form

\[
 \mathcal B_4(A)
 =W_4-2\sum_{1\leq a<K}a\{I_K(a)-I_\mu(a)\}.
 \tag{C47.3}
\]

It then forms \(\mathcal B_4+\sum aD_A(a)\) without using the direct proxy
value.  It additionally reconstructs

\[
 L_a=2\int_a^{a+1}A-q_a-q_{a+1}
\]

from adjacent caps and checks

\[
 D_A(a)-D_A(a+1)=L_a,
 \qquad
 \sum_{a\geq1}aD_A(a)
 =\sum_{a\geq1}\frac{a(a+1)}2L_a.
\]

The direct and aggregate paths were also rerun at the named points with Arb.

## 3. Search design and mandatory stress classes

The frozen full run used seed `470047`, 20,000 requested pseudorandom
proposals, and 19,778 distinct accepted strict-active parameter pairs.  Tags
overlap, so their counts do not sum to the number of records.

| mandatory class | implementation | accepted records or directed check |
|---|---|---:|
| 1. immediately above no-mode wall | multiplicative offsets \(10^{-11},10^{-8},10^{-5},10^{-2},0.2\), plus random log offsets | 3,378 |
| 2. \(\rho\uparrow1\) | fixed \(\rho\) through \(0.9999\), plus random thin shells, with activity-rescaled \(K\) | 2,937 |
| 3. small \(\rho\) | fixed and log-random values down to \(10^{-6}\) | 3,349 |
| 4. integer/near-integer \(K\) | \(K=N,N\pm10^{-9}\), plus random distances \(10^{-11}\)--\(10^{-2}\) | 3,420 |
| 5. integer/near-integer \(\mu\) | fixed \(\mu\) and random near-integer \(\mu\) | 3,374 |
| 6. action walls | four fixed-\(\mu\) wall designs, both sides, plus one exact directed wall | 8 sides + 1 exact wall |
| 7. inner-interface cells | every integer-\(\mu\) record explicitly includes \(a\approx\mu\) | 3,374 |
| 8. smallest shift \(a=1\) | evaluated in every record | 19,778 |
| 9. inherited high-floor first-drop | five independently rebuilt wall geometries from Rounds 36--46 | 5 |
| 10. large \(a,K\), terminal count | fixed records through \(K=20000\), random records through \(K=5000\) | 4 fixed + random |
| 11. maximal negative-\(D_A\) components | constructed for every record when \(D_A<-2\cdot10^{-11}\) | none found |
| 12. exact cell bonus minimum | directed rational near-minimizer at \(a=100\) | 1 at 1024 and 1536 bits |

The largest sampled terminal count was \(3,029,819\), at

\[
 \rho=0.026388232019755667\ldots,\qquad
 K=4926.589927302107\ldots.
\]

Its literal aggregate was \(9.764416927992188\times10^9>0\).

## 4. Floating-point search outcome

The full run reported:

```text
distinct_proposals=19778
literal_WT4_negative=0
records_with_D_below_minus_2e-11=0
records_with_binary64_near_zero_D=1418
mpmath_near_zero_rechecks=1418
mpmath_near_zero_negative=0
mpmath_near_zero_minimum=4.4955461868261565e-30
```

The 1,418 near-zero \(D_A\) values occur overwhelmingly in a terminal cell
when \(K\) is extremely close to an integer.  A few binary64 values are of
size \(10^{-15}\) with a negative last bit.  They were classified as
roundoff-ambiguous, not as negative components.  Re-evaluation of the
binary64-minimizing shift in all 1,418 records at 80 decimal digits made all
of them positive; the smallest was
\(4.4955461868261565\times10^{-30}\).  These mpmath reruns remain diagnostic.
Section 5.3 separately certifies a rational terminal near-zero case with
directed Arb arithmetic.

The smallest sampled literal aggregate was

\[
 \begin{aligned}
 \rho&=10^{-6},\\
 K&=3.2587764790700455\ldots,\\
 \mathrm{WT}_4&=1.7621315138491156\ldots,\\
 \mathcal B_4&=0.22118245846168927\ldots.
 \end{aligned}
\]

This is immediately above the active wall and has \(q_a=0\) for every shift.
It is a diagnostic minimum, not a lower-bound proof.

The largest binary64 direct-versus-aggregate absolute residual was
\(4.46\times10^{-3}\) on a value of order \(10^{10}\); the largest scaled
residual was \(4.56\times10^{-13}\).  The adjacent recurrence residual was at
most \(1.12\times10^{-16}\), and the largest absolute summation-by-parts
residual was \(9.77\times10^{-4}\) at large scale.  Directed named evaluations
enclosed both identity residuals by intervals containing zero.

### 4.1 Inherited high-floor diagnostics

The five inherited geometries were reconstructed by fixing the old wall
parameters, solving the wall monotonically, and then evaluating the entire
\(d=4\) integer grid.  No earlier evaluator was imported.

| \((\rho,K)\), rounded | \(\mathrm{WT}_4\) | \(\mathcal B_4\) | \(\min_aD_A(a)\) | negative components |
|---|---:|---:|---:|---:|
| \((0.4869053894,12.3227225054)\) | 106.0354312 | 2.4265526 | 0.00405034 | 0 |
| \((0.2228157509,85.2722481326)\) | 45711.46039 | 143.994014 | 0.00100559 | 0 |
| \((0.4477801249,34.6152031706)\) | 3107.134855 | 19.9524460 | 0.0121214 | 0 |
| \((0.9950955580,16666.7410641)\) | \(3.85816926821\times10^{11}\) | 56625.9 | 0.00087918 | 0 |
| \((0.6095456023,32.8113268692)\) | 3119.864436 | 14.0910988 | 0.0248729 | 0 |

These rows do not certify the inherited owner cover and do not prove any
pointwise or aggregate theorem.

## 5. Directed certificates

The evaluator uses `python-flint` Arb enclosures.  Every named certificate is
run twice at higher precision.  Every strict floor used in its payment ledger
is checked by a directed enclosure inside the asserted open integer cell.

### 5.1 Integer-\(K\), integer-\(\mu\) corner and class-B counterexample

For

\[
 [\rho_-,\rho_+]=[9/10,9/10],\qquad [K_-,K_+]=[40,40],
\]

one has \(\mu=36\).  Directed 768- and 1280-bit runs establish

\[
 K^2-\frac{\pi^2}{(1-\rho)^2}-\frac34
 =612.2895598910641\ldots>0.
\]

The interface \(a=\mu=36\) is evaluated with the inner action equal to zero;
\(a=K=40\) belongs to the zero extension and is excluded from the strict
sum.  All 39 action floors are strict.  In fact,

\[
 q_a=
 \begin{cases}
 1,&1\leq a\leq30,\\
 0,&31\leq a\leq39.
 \end{cases}
\]

The complete global payment ledger is

\[
 \begin{array}{rcl}
 W_4&=&13756,\\
 P_4^{<}&=&9455,\\
 W_4-P_4^{<}&=&4301,\\
 \mathcal B_4(A)&=&6.3326609110017108459691\ldots,\\
 \sum aD_A(a)&=&4294.6673390889982891540\ldots,\\
 \mathcal B_4+\sum aD_A(a)&=&4301.0000000000\ldots.
 \end{array}
\]

The identity residual is enclosed by \(0\pm1.20\times10^{-224}\) at 768
bits.  The minimum shifted defect is

\[
 D_A(39)=0.0379946688582178302276\ldots>0.
\]

For the rejected cellwise sufficient route, an interval Riemann enclosure of
the exact integral

\[
 \mathcal B_{4,29}=2\int_{29}^{30}(-A')(-\Delta_4)
\]

uses 4096 rational subintervals and 768-bit Arb evaluation.  Together with
the directed \(L_{29}\) displayed in Section 1, it proves (C47.1) negative.
The 384-bit/2048-piece replay gives the same classification.

### 5.2 Small-\(\rho\), immediately active point

Take exact rational parameters

\[
 [\rho_-,\rho_+]=[1/10000,1/10000],\qquad
 [K_-,K_+]=[163/50,163/50].
\]

The active-wall excess is enclosed around

\[
 0.00602138190280812376218>0.
\]

All strict floors are certified, \(P_4^{<}=0\), and

\[
 \begin{aligned}
 \mathrm{WT}_4&=1.76477940249999982352205975\ldots,\\
 \mathcal B_4&=0.22136297423706860992505819\ldots,\\
 \sum aD_A(a)&=1.54341642826293121359700156\ldots.
 \end{aligned}
\]

The two evaluations agree with residual \(0\pm5.90\times10^{-229}\) at 768
bits.  The least defect is
\(D_A(3)=0.00459659442688590587\ldots>0\).

### 5.3 Directed terminal near-zero point

Take

\[
 [\rho_-,\rho_+]=[1/2,1/2],\qquad
 [K_-,K_+]=[10000001/1000000,10000001/1000000].
\]

Thus \(K=10+10^{-6}\).  The point is strictly active, with active excess
\(59.7716\ldots\), and every strict floor is certified.  Arb gives

\[
 D_A(10)=
 7.5921334439579871022271111598\times10^{-17}>0
\]

with enclosure radius below \(7.5\times10^{-226}\) at 768 bits.  The full
ledger is

\[
 \begin{aligned}
 P_4^{<}&=91,\\
 \mathrm{WT}_4&=55.4844335937587890630859375\ldots,\\
 \mathcal B_4&=1.56047315042694836555608735\ldots,\\
 \sum aD_A(a)&=53.92396044333184069752985017\ldots.
 \end{aligned}
\]

The 1280-bit rerun agrees.  This certifies that the small negative last bits
seen in analogous binary64 terminal records are numerical artifacts, not
literal negative components.

### 5.4 Exact action wall

Fix \(\mu=6\) and define \(K_*\) by

\[
 A(5)+\frac14=1.
\]

For readability, a coarsened rational bracket containing the evaluator's
70-decimal bracket is

\[
 \frac{9203339322718680230068839575926}{10^{30}}
 <K_*<
 \frac{9203339322718680230068839575927}{10^{30}}.
\]

Consequently,

\[
 \frac{6\cdot10^{30}}{9203339322718680230068839575927}
 <\rho_*<
 \frac{6\cdot10^{30}}{9203339322718680230068839575926}.
\]

The 768-bit residual signs on the narrower stored bracket are less than
\(-2.04\times10^{-71}\) and greater than \(6.31\times10^{-72}\).
Uniqueness follows from

\[
 \frac{\partial A(5)}{\partial K}
 =\frac{\sqrt{K^2-25}}{\pi K}>0
 \qquad(\mu\text{ fixed}).
\]

At the exact wall the strict convention gives

\[
 q_5=[1]_< =0.
\]

Every other floor is certified in a strict open cell, the no-mode excess is
\(2.4838917953\ldots>0\), and

\[
 P_4^{<}=30,\qquad
 \mathrm{WT}_4\in
 61.849006663275773275902144764\ldots\pm6.4\times10^{-69}.
\]

This verifies that the wall belongs to the lower-\(P_4^{<}\) side.  It does
not use an ordinary floor.

### 5.5 Exact \(d=4\) cell minimum

On \(z=a+x\), the directed polynomial is

\[
 -\Delta_4(a+x)
 =\frac a6-\frac{ax(1-x)}2+\frac{x^3}{6}.
\]

At \(a=100\), use the exact rational point

\[
 x_0=
 \frac{249378105604451351096324563797880934725117350131886452864141}
 {5\cdot10^{59}},
\]

which lies extremely close to
\(x_*=\sqrt{a(a+1)}-a\).  At 1024 bits,

\[
 (-\Delta_4)(100+x_0)
 -\frac{100\cdot101}
 {12(100+1/2+\sqrt{100\cdot101})}
 =4.7600407796874\ldots\times10^{-119}>0.
\]

The enclosure radius is below \(8.6\times10^{-307}\).  The exact minimum
exceeds \(a/24\) by

\[
 0.0207555966942359514146\ldots>0.
\]

The 1536-bit replay agrees.  This stress test supports the exact cell formula
and its strict coarse consequence; it is not a global bonus proof.

## 6. Proposed bonus and component comparisons

Three stronger sufficient comparisons were tracked separately from literal
\(\mathrm{WT}_4\).

1. **Coarse aggregate.**  The diagnostic scalar
   \[
   \frac1{12}\sum_{1\leq j<K}A(j)+\sum_a aD_A(a)
   \]
   had sampled minimum \(1.6116270059292852\ldots>0\).  This is positive
   search evidence only.

2. **Bonus pays all sampled negative tails.**  The scalar
   \[
   \mathcal B_4(A)+\sum_{D_A(a)<0}aD_A(a)
   \]
   had sampled minimum \(0.22118245846168927\ldots>0\).  Because the sweep
   found no resolved negative \(D_A(a)\), this test did not exercise the
   intended negative-support mechanism and has almost no evidentiary force.

3. **Each \(L_a\) cell pays itself.**  Inequality (C47.1) is rigorously
   false.  Negative local trapezoidal remainders \(L_a\) occur even when all
   shifted tails \(D_A(a)\) are positive.  A valid component theorem must
   therefore retain transport among adjacent \(L\)-cells, positive boundary
   tails, or additional bonus cells.  It cannot sign every summand in the
   weighted summation-by-parts formula separately.

No \(\Xi_a\) theorem was supplied within this independent search, so no
claim about a localized-deficit theorem is made.

## 7. Wall and ownership audit

| face | treatment |
|---|---|
| strict active wall | all search points satisfy \(K^2>\pi^2/(1-\rho)^2+3/4\); the equality face is not silently included |
| \(K\in\mathbb N\) | \(A(K)=0\); the sum is strictly \(a<K\), demonstrated at \(K=40\) |
| \(\mu\in\mathbb N\) | \(a=\mu\) uses zero inner action/cap and the outer branch, demonstrated at \(\mu=36\) |
| action wall | \(q_a=[N]_< =N-1\), demonstrated at \(A(5)+1/4=1\) |
| inner interface | both sides and exact integer interfaces were sampled |
| endpoint | zero-extended terminal cells were included; the near-zero terminal record was directed |
| \(\rho\uparrow1\) | activity-rescaled thin-shell records were sampled through \(\rho=0.9999\), plus inherited \(\rho\approx0.9951\) |
| moderate frequency | the smallest literal values occurred immediately above activity at \(K\approx3.2588\), not in an asymptotic range |

## 8. What this search does and does not establish

Established by directed named computations:

- exact agreement of direct \(W_4-P_4^{<}\) with the independently assembled
  bonus-plus-weighted-defect ledger at the named rational points;
- correct strict ownership at an exact action wall;
- correct \(K\)- and \(\mu\)-integer ownership at the rational corner;
- positivity of a terminal defect of size \(7.59\times10^{-17}\);
- near-equality verification of the exact \(d=4\) cell minimum;
- a class-B counterexample to the cellwise self-charge inequality (C47.1).

Not established:

- global positivity of \(\mathrm{WT}_4\);
- global pointwise positivity of \(D_A(a)\);
- existence or classification of maximal negative-\(D_A\) components;
- a no-double-counting component charge theorem;
- a finite or compact cover of the strict active domain;
- any spectral counterexample or proof.

## 9. Reproduction

Full search and directed certificates:

```powershell
python computations/general_d_round47_independent_d4_weighted_search.py --random 20000
```

Fast smoke test:

```powershell
python computations/general_d_round47_independent_d4_weighted_search.py --quick
```

The executable always ends by printing the required coverage disclaimer.

```text
positive_coverage_certificate: FALSE
```
