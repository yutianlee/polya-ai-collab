# Adversarial referee report: integrated purely analytic closure

Verdict: **PASS**

I audited the section beginning with “Purely analytic closure of the exact
residual \(\mathcal D_{20}\)” and ending with “Analytic dependency, coverage,
and optional cross-checks” under the hostile assumption that the claimed
Pólya inequality is false.  I reconstructed each implication needed to pass
from the compact and aggregate estimates to Proposition `compact-middle`,
including all endpoint conventions requested in the assignment.

This verdict applies to the following frozen main source:

- `manuscript/spherical-shell-polya-proof.tex`
- SHA-256:
  `84D079A9FD3A6001C7F00A528F7EAF40799D6850E87537BDC3819A98A9F6D982`
- audited main-source lines: 3674--4078

No unsupported mathematical implication remains in this frozen section.  In
particular, the discrete \(\mathcal Q\)-bridge is now proved in the main source
rather than being passed through a circular citation to the aggregate note.

## 1. Audited sources

The integrated statements agree with the following retained analytic sources.

| source | frozen SHA-256 | role |
|---|---|---|
| `compact-structural.tex` | `C236816E12266D055F144CF7EC9B2AEB352CB985EE3730D19F4AA850925606A7` | exact deficit identity and \(\mathcal E_{\rm ang}<\mathcal H\Rightarrow P<W\) |
| `compact-angular-block.tex` | `8288FE0EAFEB8D8CFE9A10749E6BA470124408E3DC9FBBF1BE24BBB023C6DB49` | strict global angular-block bound |
| `compact-scalar-positive.tex` | `10CD0E5D6DDE5ECD7CFA2B2C64E47368E10E44093A407C04F74E29BB71807BA1` | strict scalar positivity on the closed compact domain |
| `F-positive.tex` | `D2305C221D89D2275A11B02F590A15FCA36EBE78AAD98DDBF5334FF41BDA064A` | \(F>1549/84150\) |
| `BK-positive.tex` | `F303CD9659789391DAABDF2821B16DE99B04BA47D767996B8ECCFCAA9F4D6F03` | \(\mathcal B_K(\rho,200)>0\) |
| `B-positive.tex` | `70222FE3523B3F71384ADF22E2751BE1390498AE6554A8875984330DCBF67808` | \(\mathcal B(\rho,200)>60\) |
| `aggregate-tail-analytic.tex` | `B59D673E117611C81BABE4F8D7FE34AD0AFDFEF84BF2D8424128DE606F9C0BC9` | continuous curvature propagation and aggregate theorem |
| `ledger-packet-F.tex` | `B137FDE7B974F55DD8EFD7D90501611939F291CAC80437C6F707C3CBC483E26E` | exact construction and split of \(\mathcal D_{20}\) |

The corresponding individual audit files all record PASS.  I used those
audits as cross-checks, but reconstructed the chains below directly from the
displayed formulas.

## 2. Compact \(\mathcal E_{\rm ang}\)--\(\mathcal H\) chain

Main lines 3695--3737 correctly assemble the following chain.

1. The already established phase reduction at main lines 2031--2037 gives
   \[
   N_D(A_{\rho,1},K^2)\leq P_{\rm coarse}(\rho,K).
   \]

2. `compact-structural.tex`, lines 270--360, proves the exact retained-deficit
   identity.  Its concrete minorant is constructed at lines 367--423, and the
   corollary at lines 428--460 proves
   \[
   \mathcal E_{\rm ang}<\mathcal H\quad\Longrightarrow\quad
   P_{\rm coarse}<W.
   \]
   This is the implication reproduced at main lines 3695--3705.

3. `compact-angular-block.tex`, lines 288--329, proves the strict one-layer
   estimate, including a half-integer rounding wall.  The disjoint-block sum
   at lines 332--380 gives
   \[
   \mathcal E_{\rm ang}
   <\frac{1-\rho^2}{6}K^2-\frac N2.
   \]
   Lines 400--406 of that source show \(N\geq1\) on the exact closed compact
   domain because
   \[
   T\geq\frac{(1-\rho)k_{11}}\pi
     =\sqrt{1+132(1-\rho)^2/\pi^2}>1.
   \]
   Hence the main-source bound at lines 3710--3722 follows with a strict
   \(-1/2\) payment.  The revised wording at main lines 3715--3718 now matches
   the actual disjoint one-layer proof and correctly includes common jump
   faces through the strict rounding convention.

4. `compact-scalar-positive.tex`, lines 86--93, states the required strict
   scalar inequality on the same closed domain.  Its monotonicity reduction is
   proved at lines 197--288, its uniform loss estimates at lines 293--411, and
   strict base-curve positivity by explicit rational/Bernstein calculations at
   lines 527--643.  Thus main lines 3723--3729 correctly give
   \[
   \mathcal H>\frac{1-\rho^2}{6}K^2-\frac12.
   \]

Combining the last two displays yields
\(\mathcal E_{\rm ang}<\mathcal H\), then
\(P_{\rm coarse}<W\), and finally \(N_D<W\).  The strict inequalities survive
\(\rho=\rho_c\), \(\rho=39/50\), \(K=k_{11}(\rho)\), \(K=200\), and all
radial--angular coincidence walls.  I found no boundary at which the compact
chain becomes merely non-strict.

## 3. Reconstruction of the discrete \(\mathcal Q\)-bridge

The definitions and proof at main lines 3768--3894 are arithmetically
consistent.

Write
\[
x:=\mu-\frac12=J+\tau,
\qquad 0\leq\tau<1,
\qquad
R=J\ (\tau=0),\quad R=J+1\ (\tau>0).
\]
For \(0\leq r<R\), main lines 3776--3782 correctly give
\[
n_r=J-r,qquad q_r=J+\frac12,qquad
\sum_{r<R}n_r=\frac{J(J+1)}2,qquad \mu-q_r=\tau.
\]
When \(\tau=0\), the low tails stop at \(r=J-1\) and the interface tail
\(x_J=\mu\) is assigned to the high side.  When \(\tau>0\), the final low tail
has \(n_J=0\).  Thus the two cases neither omit nor duplicate an interface.

For \(C=2\pi\rho K/(1-\rho)\), main lines 3811--3827 use
\[
\vartheta(0)=0,
\qquad
\vartheta'(z)\geq\frac{1-\rho}{\pi\rho K}=\frac2C.
\]
Therefore \(\vartheta(z)\geq2z/C\), and equality of the ordinary floors on a
first shelf of length \(p_r\) implies
\[
1>A(x_r)-A(x_r+p_r)
  \geq\frac{(x_r+p_r)^2-x_r^2}{C}.
\]
Consequently
\[
p_r<f_C(x_r):=\sqrt{x_r^2+C}-x_r.
\]
The function \(f_C\) is positive and strictly convex.  Applying the midpoint
inequality interval by interval gives exactly main lines 3828--3835:
\[
\sum_{r<R}p_r
 <\sum_{r<R}f_C(r+1/2)
 \leq\int_0^Rf_C(x)\,dx=\mathcal I(C,R).
\]

The one-tail inequality at main lines 3836--3850 is the earlier
concave-head/convex-tail formula with
\[
M_r=\lfloor K\eta_\rho\rfloor+d_\rho n_r-(1+d_\rho)p_r
\]
and interface loss
\(0\leq\delta_\tau\leq2\tau^{5/2}/(15\sqrt\mu)\).  Summing it gives
\[
\begin{aligned}
&\sum_{r<R}\frac{\mathcal T_r}{2}
-\sum_{r<R}\int_{x_r}^K A(z)\,dz\\
&\quad<
\frac{2R\tau^{5/2}}{15\sqrt\mu}
-\frac14\left[
R\lfloor K\eta_\rho\rfloor
d_\rho\frac{J(J+1)}2
-(1+d_\rho)\mathcal I(C,R)
\right]
=-\frac{\mathcal Q}{4}.
\end{aligned}
\]
The coefficient \(8\) in the definition of \(\mathcal Q\) at main
lines 3791--3798 is therefore correct.

For \(r\geq R\), main lines 3860--3865 apply the non-strict convex-tail bound,
including \(x_r=\mu\).  The exact multiplicity identity at lines 3867--3876
then converts the low/high tail sum into the weighted lattice proxy.  If
\(\mathcal Q\geq0\), the low-tail inequality is still strict, so
\[
P_{\rm coarse}
<2\sum_r\int_{x_r}^KA(z)\,dz
=2\int_0^K f_3(z)A(z)\,dz.
\]
Finally, the scaffold primitive satisfies
\(\int_0^z f_3\leq z^2/2\); integration by parts gives
\[
2\int_0^K f_3A\leq\int_0^K2zA(z)\,dz=W.
\]
Thus the lemma at main lines 3801--3894 is valid.  At \(\tau=0\), strictness
does not depend on a positive interface remainder: \(R=J\geq1\),
\(\sum p_r<\mathcal I(C,R)\), and the interface belongs to the high side.  An
integer \(K\eta_\rho\) also causes no loss, since the strict floor convention
can only lower the proxy.

## 4. Strict bridge \(\mathcal Q>\mathcal B\), including \(\tau=0\)

Main lines 3896--3911 assume exactly the conditions later established on the
tail domain: \(x=\mu-1/2>1\) and \(y=K\eta_\rho>1\).  The four comparisons are
strict for the following independent reasons.

1. \(R\geq x\), with equality only when \(\tau=0\), and
   \(\lfloor y\rfloor>y-1\).  Since \(R>0\) and \(y-1>0\),
   \[
   R\lfloor y\rfloor>R(y-1)\geq x(y-1).
   \]

2. Direct subtraction gives
   \[
   J(J+1)-x(x-1)=(1-\tau)(2J+\tau)>0.
   \]
   For \(\tau=0\), this difference is \(2J>0\).

3. Since \(R<\overline R=x+1\) in both cases and
   \(f_C(t)=\sqrt{t^2+C}-t>0\),
   \[
   \mathcal I(C,R)<\mathcal I(C,\overline R)
   =\overline{\mathcal I}.
   \]

4. If \(\tau=0\), then \(R\tau^{5/2}=0<\overline R\).  If \(\tau>0\),
   then \(R\tau^{5/2}<R<\overline R\).

The negative signs on the last two terms reverse in the favorable direction,
so termwise substitution proves \(\mathcal Q>\mathcal B\), not merely
\(\mathcal Q\geq\mathcal B\).  Half-interface and integer-floor walls are
therefore covered.

## 5. Analytic base signs and propagation from \(K=200\)

Main lines 3926--3969 correctly import and propagate three analytic signs on
the rational superset \(7/51\leq\rho\leq39/50\):
\[
F(\rho)>\frac{1549}{84150},\qquad
\mathcal B_K(\rho,200)>0,\qquad
\mathcal B(\rho,200)>60.
\]
Their ownership is explicit:

- `F-positive.tex`, lines 173--246;
- `BK-positive.tex`, lines 1--15 and its two analytic interval proofs;
- `B-positive.tex`, lines 81--89 and 381--483.

No sampled or interval-computed sign is used.  The proofs use elementary
integral estimates, rational comparison, positive-side squaring, and exact
Bernstein-basis coefficients.

The derivative identities are printed in `aggregate-tail-analytic.tex`,
lines 187--219.  On \(K\geq200\), its lines 277--303 use
\(S>\overline R>\rho K\) to obtain
\[
\overline{\mathcal I}_{KK}<\frac{3b}{800},
\qquad E_{KK}>0,
\qquad \mathcal B_{KK}>F>\frac{1549}{84150}.
\]
Twice integrating from \(200\), as done at main lines 3958--3966, yields
\[
\mathcal B(\rho,K)>
60+\frac{1549}{168300}(K-200)^2>0.
\]
At \(K=200\), the integral term vanishes, but the separately proved strict
base value supplies the conclusion; main line 3968 states this explicitly.
The chain \(\mathcal Q>\mathcal B>0\) then activates the discrete implication.

The tail validity hypotheses are also owned analytically.  Main lines
3926--3934 (and `aggregate-tail-analytic.tex`, lines 221--260) prove
\(\mu>3/2\) and \(K\eta_\rho>1\) on the rational superset.  The containment
\(7/51<\rho_c\) follows from \(\pi<22/7\), so the entire desired tail domain is
inside that superset.

## 6. Ownership of \(\rho_c\), \(K=200\), and the residual

Main lines 3661--3672 define
\[
\mathcal D_{20}=
\{\rho_c\leq\rho<39/50,\ k_{11}(\rho)<K<U(\rho)\}
\]
and assign its excluded faces.  The split at main lines 3985--4006 is
\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]
It is disjoint and exhaustive.  In particular:

- \(K=200\) is uniquely compact-owned, even though the analytic tail theorem
  is also valid there;
- \(\rho=\rho_c\) is included when the two frequency inequalities defining
  \(\mathcal D_{20}\) are strict;
- \(\rho=39/50\), \(K=k_{11}(\rho)\), and \(K=U(\rho)\) remain outside
  \(\mathcal D_{20}\) and retain their earlier owners.

This agrees with `ledger-packet-F.tex` and its audit, especially audit lines
100--138.  Thus the equality faces are not lost by a complement operation.

## 7. Use in Proposition `compact-middle`

Main lines 4022--4038 correctly use the earlier owner subtraction: primitive
owners cover the complement of \(\mathcal D_{16}\); the listed intermediate
lemmas remove exactly the sets subtracted in constructing \(\mathcal D_{20}\);
and every remaining point lies in exactly one of \(\mathcal C_{21}\) or
\(\mathcal T_{21}\).  The compact and tail lemmas therefore leave no residual
point.  The theorem is stated non-strictly because \(K=0\) has
\(N_D=W=0\); all positive-frequency residual points have been proved with a
strict inequality.

## 8. Dependency census and final finding

Main lines 4044--4078 now describe a **normalized disjoint allocation**.  This
wording is important and is correct.  The raw packet sources contain 10 and 36
repeated general-identity instances, documented at
`final-analytic-closure-audit.md`, lines 290--309.  The subsequent normalized
ownership audit, `ledger-global-coverage-audit.md`, lines 69--92 and 104--181,
assigns the ten supplemental lower-\(d\) identities to Packet D and the 36
optical general identities to Packet A/B.  With those canonical choices, the
unique census is
\[
278+83+57+22+68+103=611,
\]
exactly the table at main lines 4048--4064.  Hence the normalized owner sets
are pairwise disjoint even though an identity may be used in more than one
proof location.

**First unsupported or overstated implication:** none in the frozen source.
The compact chain, the full discrete \(\mathcal Q\) argument, the strict
\(\mathcal Q>\mathcal B\) bridge (including \(\tau=0\)), the analytic base-sign
propagation, and the exact owner split all reconstruct with the stated
strictness.  The integrated analytic section therefore passes this adversarial
referee check.
