# Current-hash clean-room audit of the retained-remainder closure

Date: 2026-07-17  
Scope: the current all-frequency analytic closure of the final spherical-shell
residual, not the complete finite staircase or the literature/novelty claim.

## Verdict

**PASS.** I reconstructed the implication from the current sources and found
no domain gap, lost strict wall, or computational premise.  The first defect
is: **none**.

## Frozen source snapshot

| Source | Lines | SHA-256 |
|---|---:|---|
| `manuscript/spherical-shell-polya-proof.tex` | 3660 | `aec5573938b7194a961c192afe5d5fd9a110bf28630f9ba397e25a296d947e73` |
| `manuscript/analytic/compact-structural.tex` | 535 | `1055ba25a6e7f97f2f49ef250ef7589c45d0251b8af50a5e0ff59b36c6bf722c` |
| `manuscript/analytic/compact-angular-block.tex` | 476 | `382df2f006d432902bd68582c3305e5006d701c3d24703e16760e8dca7fb12ce` |
| `manuscript/analytic/compact-scalar-positive.tex` | 675 | `811312fc8433bb89f339100f007694dd91de07ec20e4f4d691e36a1fca33fe07` |
| `manuscript/analytic/final-analytic-closure.tex` | 188 | `c0518cf17f0cbb20f92ba87e94c24bdb8873696ee6c9fa6bf134c4f5e631a7fb` |
| `manuscript/spherical-shell-polya-analytic-supplement.tex` | 245 | `16008399df3893c662f501994e1a50b5d8531f63641b6ae7b7afbc9403c289ee` |

I read these current files directly.  Earlier audit verdicts were not used to
bridge a source-hash change.

## Reconstruction of the implication

### 1. Strict spectral proxy

The current main paper defines

\[
 P(\rho,K)=\sum_{\ell+1/2<K}(2\ell+1)
 \left[A_{\rho,K}(\ell+1/2)+\frac14\right]_<
\]

and proves (N_D(A_{\rho,1},K^2)\leq P(\rho,K)) at
`spherical-shell-polya-proof.tex:1785--1806`.  The outer cutoff is strict,
the action is zero-extended at both interfaces, and the positive-integer
bracket excludes an equality phase wall.  This is exactly the proxy used by
the structural and final-closure modules.

### 2. Global retained-remainder identity

`compact-structural.tex:46--200` defines the action for every
(0<\rho<1, K>0) and proves the exact layer cake.  At an angular equality
(R(n-1/4)=m+1/2), the count is (M=m); at a radial equality
(n-1/4=A(\nu)), that layer is excluded.  Thus the rearrangement preserves
the original strict convention.

The Stieltjes calculation at `compact-structural.tex:245--365` gives

\[
 W-P=\mathcal B+\mathcal R_{\rm dec}+\mathcal R_{\rm osc}
      -\mathcal E_{\rm ang},
\]

with both retained remainders nonnegative.  The decreasing-branch primitive
minorant at lines 368--433 yields the smooth payment \(\mathcal H\), and the
corollary at lines 435--467 proves

\[
 \mathcal E_{\rm ang}<\mathcal H\quad\Longrightarrow\quad P<W.
\]

No ratio or upper-frequency restriction is introduced in this structural
step.

### 3. Strict angular payment

`compact-angular-block.tex:287--386` uses only (q=-A'\leq1/2).  On each
active left block of length (3/4), it proves

\[
 r_n\leq\frac43\int_{n-1}^{n-1/4}R(t)\,dt-\frac34,
 \qquad m_n^2-r_n^2<r_n+\frac14.
\]

The second inequality remains strict at a half-integer wall because the
strict count takes (m_n=m), not (m+1).  Summing the disjoint blocks gives

\[
 \mathcal E_{\rm ang}
 <\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

The common-jump identity at lines 229--278 independently confirms that the
chosen right-continuous representatives sample simultaneous radial/angular
jumps with the required left value (p(t^-)=-3/4); no atom is dropped.

On

\[
 \mathcal R_{\rm c}=
 \{\rho_c\leq\rho\leq39/50, K\geq k_{11}(\rho)\},
\]

lines 388--423 show

\[
 T\geq\frac{(1-\rho)k_{11}(\rho)}\pi
   =\sqrt{1+\frac{132(1-\rho)^2}{\pi^2}}>1.
\]

Hence (N\geq1), and therefore

\[
 \mathcal E_{\rm ang}
 <M_c:=\frac{(1-\rho^2)K^2}{6}-\frac12.
\]

Both ratio endpoints and the base-frequency face are included.

### 4. Scalar positivity on the same unbounded domain

`compact-scalar-positive.tex:45--98` states precisely the same closed domain.
The loss derivative is evaluated exactly at lines 119--205.  Its beta bound,
combined with the displayed rational estimates, gives strict positivity of
\(\partial_K\mathcal S\) for (K>12); the interval proof at lines 208--300
includes every \(\rho\in[\rho_c,39/50]\).

Lines 304--425 prove (k_{11}(\rho)>241/20>12) and a rational secant upper
bound for the loss.  Lines 427--654 reduce the base curve to a degree-nine
polynomial and display ten positive Bernstein coefficients on the rational
interval containing the complete ratio range.  Consequently

\[
 \mathcal H-M_c=\mathcal S(\rho,K)>0
\]

for every finite (K\geq k_{11}(\rho)), with no upper cutoff.

As an independent transcription check, I replayed with exact rational
arithmetic:

- the four cubic Bernstein coefficients in the derivative proof;
- the ten-piece secant sum (Q) and the printed positive
  (17/100-Q) gap;
- the factorized-to-expanded degree-nine polynomial identity;
- all ten degree-nine Bernstein coefficients; and
- the beta-chain rational comparison.

Every value reproduced exactly and every asserted coefficient/gap was
positive.  This replay is diagnostic evidence only; the proof is the printed
convexity argument and exact rational identities.

Combining the strict inequalities gives

\[
 \mathcal E_{\rm ang}<M_c<\mathcal H,
 \qquad N_D\leq P<W
\]

on all of \(\mathcal R_{\rm c}\).

## Exact residual and face ownership

The main paper at `spherical-shell-polya-proof.tex:3182--3197` and the final
closure at `final-analytic-closure.tex:34--59` use the identical residual

\[
 \mathcal D_{20}=
 \{\rho_c\leq\rho<39/50, k_{11}(\rho)<K<U(\rho)\}.
\]

Weakening only the strict upper-ratio and lower-frequency inequalities gives

\[
 \mathcal D_{20}\subset
 \{\rho_c\leq\rho\leq39/50, K\geq k_{11}(\rho)\}
 =\mathcal R_{\rm c}.
\]

This is the complete argument at `final-analytic-closure.tex:147--177` and
in the main proposition at `spherical-shell-polya-proof.tex:3266--3287`.
There is no artificial frequency interface.  The inherited faces remain
consistent:

- \(\rho=\rho_c\) is retained in \(\mathcal D_{20}\) when both frequency
  inequalities are strict;
- \(\rho=39/50\) is optical-owned and absent from \(\mathcal D_{20}\), while
  the stronger retained-remainder theorem also covers it;
- \(K=k_{11}(\rho)\) is staircase-owned and absent from \(\mathcal D_{20}\),
  while the stronger theorem also covers it;
- \(K=U(\rho)\) was excluded from the inherited residual.

Thus every point of \(\mathcal D_{20}\) is covered and no boundary point is
lost or subtracted twice.

## Analytic-versus-computational boundary

The three proof modules contain no (K=200) premise, interval enclosure,
executable classification, floating-point sign, sampled minimum, or
numerical root isolation.  The large rational secant and Bernstein displays
are exact finite algebra whose sign follows from convexity and positive
rational coefficients.

The current supplement wrapper includes the structural, angular, scalar, and
final-closure modules as Parts VII--X and classifies the old (K=200), Arb,
aggregate, executable, and interval material only as optional regression.
The current main paper makes the same separation at lines 3321--3403.
Occurrences of those terms inside `final-analytic-closure.tex` explicitly
deny their use; they are not imported premises.

## Final determination

The current-hash sources prove the all-frequency retained-remainder theorem
on exactly the closed domain needed to contain \(\mathcal D_{20}\).  Strict
radial, angular, simultaneous-jump, ratio-seam, and base-frequency walls are
owned consistently.  The closure is purely analytic in the stated sense.

