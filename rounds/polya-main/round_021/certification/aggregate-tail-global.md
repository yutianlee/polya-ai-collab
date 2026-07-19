# Round 21 certification: global aggregate-tail positivity

Status: **PASS — OUTWARD ARB CERTIFICATE**.

Date: 2026-07-15.

## Certified theorem

Let

\[
 \rho_c=\frac1{1+2\pi}.
\]

For the reserve \(\mathcal B\) defined in equation (15) of the authenticated
aggregate low-interface route,

\[
 \boxed{
 \rho_c\leq\rho\leq\frac{39}{50},\quad K\geq200
 \quad\Longrightarrow\quad
 \mathcal B(\rho,K)>0.}
\]

The verifier also proves the standing route conditions
\(\mu>3/2>1/2\) and \(K\eta_\rho>1\) throughout this region.  Therefore the
accepted implication (16) gives \(\mathcal Q>0\) and the strict Pólya
comparison throughout the same high-frequency region.

## Authenticated basis

The executable checker authenticates these exact inputs before performing
any interval calculation:

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md` | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

Certificate artifacts:

| artifact | SHA-256 |
|---|---|
| `computations/round21_verify_aggregate_tail.py` | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` |
| `computations/tests/test_round21_verify_aggregate_tail.py` | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` |

## Analytic reduction in the frequency variable

Fix \(\rho\) and abbreviate

\[
 b=\frac{2\pi\rho}{1-\rho},\qquad
 C=bK,\qquad
 R=\rho K+\frac12,\qquad
 S=\sqrt{R^2+C},\qquad
 P_C(R)=S-R.
\]

Write

\[
 I(K)=\mathcal I(bK,\rho K+\tfrac12)
 =\int_0^R\left(\sqrt{x^2+C}-x\right)\,dx.
\]

The two partial derivatives of the integral are

\[
 \frac{\partial\mathcal I}{\partial R}=P_C(R),
 \qquad
 \frac{\partial\mathcal I}{\partial C}
 =\frac12\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right).
\]

Consequently

\[
 \boxed{
 I_K=\rho P_C(R)
 +\frac b2\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right).}
\]

For the second derivative, direct differentiation gives

\[
 \frac{dP_C(R)}{dK}=\frac{\rho R+b/2}{S}-\rho,
\]

and, using \(R=\rho K+1/2\) and \(C=bK\),

\[
 \frac d{dK}\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right)
 =\frac{2\rho K-1}{4KS}.
\]

Thus the exact formula is

\[
 \boxed{
 I_{KK}
 =\rho^2\left(\frac RS-1\right)
 +\frac{\rho b}{2S}
 +\frac{b(2\rho K-1)}{8KS}.}
\]

Because \(C>0\), one has \(S>R>\rho K\).  The first displayed term is
strictly negative, while

\[
 \frac{b(2\rho K-1)}{8KS}<\frac{\rho b}{4S}.
\]

It follows that

\[
 \boxed{I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}.}
\]

The final term of \(\mathcal B\) can be written

\[
 E(K)=-\frac8{15}\left(\sqrt\mu+\frac1{2\sqrt\mu}\right),
 \qquad \mu=\rho K.
\]

Its exact second derivative is

\[
 \boxed{
 E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}>0
 \qquad(\mu>3/2).}
\]

The remaining two terms of \(\mathcal B\) have combined second derivative
\(2\rho\eta_\rho+d_\rho\rho^2\).  Therefore, for \(K\geq200\),

\[
 \begin{aligned}
 \mathcal B_{KK}
 &=2\rho\eta_\rho+d_\rho\rho^2
   -(1+d_\rho)I_{KK}+E_{KK}\\
 &>2\rho\eta_\rho+d_\rho\rho^2
   -\frac{3(1+d_\rho)b}{4K}\\
 &\geq
 \underbrace{2\rho\eta_\rho+d_\rho\rho^2
   -\frac{3(1+d_\rho)b}{800}}_{=:F(\rho)}.
 \end{aligned}
\]

Hence it is enough to prove on the ratio interval that

\[
 \mathcal B(\rho,200)>0,
 \qquad
 \mathcal B_K(\rho,200)>0,
 \qquad
 F(\rho)>0.
\]

Indeed, \(F>0\) makes \(\mathcal B_K\) strictly increasing in \(K\);
its positive value at \(200\) then makes \(\mathcal B\) strictly increasing,
and the positive base value proves the theorem for every \(K\geq200\).

For reference, the exact first derivative evaluated by the verifier is

\[
 \begin{aligned}
 \mathcal B_K={}&
 \rho(K\eta_\rho-1)+(\mu-\tfrac12)\eta_\rho
 +d_\rho\rho(\mu-1)\\
 &-(1+d_\rho)I_K
 -\frac{2\rho(2\mu-1)}{15\mu^{3/2}}.
 \end{aligned}
\]

## Outward interval certificate

The elementary strict inequality \(\pi<22/7\) gives

\[
 \rho_c=\frac1{1+2\pi}>\frac7{51}.
\]

It therefore suffices to certify the larger rational interval
\([7/51,39/50]\).  The verifier splits at \(\rho=1/2\), where the definition
of \(\eta_\rho\) changes:

\[
 \eta_\rho=G_1(1/2)\quad(\rho\leq1/2),
 \qquad
 \eta_\rho=G_1(\rho)\quad(\rho\geq1/2).
\]

The two formulas agree at the shared endpoint.  Each segment is subdivided
using exact rational endpoints and intended width at most \(1/2000\):

\[
 [7/51,1/2]:726\text{ boxes},
 \qquad
 [1/2,39/50]:560\text{ boxes}.
\]

Thus the exact box count is

\[
 \boxed{726+560=1{,}286.}
\]

Every exact rational box is converted to an outward `arb` enclosure, and
the executable checker verifies that the rounded ball contains both exact
rational endpoints.  All elementary evaluations use python-flint Arb at
192-bit midpoint precision.  On every box the checker proves, by strict Arb
comparison with zero,

\[
 \mathcal B(\rho,200)>0,
 \qquad \mathcal B_K(\rho,200)>0,
 \qquad F(\rho)>0.
\]

It additionally checks \(S>R\), \(R>\rho K\),
\(I_{KK}<3b/(4K)\), \(E_{KK}>0\),
\(\mathcal B_{KK}>F\), \(\mu>3/2\), and \(200\eta_\rho>1\) on every box.

### Proof values versus displays

The proof consists of the 1,286 outward balls for each required expression
excluding zero on the positive side.  No decimal conversion, sampled
minimum, or ordering of boxes is used for a proof decision.

Only after every strict sign check passes, the program converts lower
endpoints to decimals to select human-readable diagnostic minima.  These
nonproof displays are:

| expression | display-only lower value | intended rational box |
|---|---:|---:|
| \(\mathcal B(\rho,200)\) | `375.4372603381510` | `[1559/2000,39/50]` |
| \(\mathcal B_K(\rho,200)\) | `4.798498305533769` | `[7/51,14051/102000]` |
| \(F(\rho)\) | `0.02747676406088864` | `[7/51,14051/102000]` |

The relatively low displayed enclosure for \(\mathcal B\) is an interval
dependency effect and is not an estimate of the true pointwise minimum.
Its only proof-relevant property is strict positivity.

## Reproduction

Environment used: Python 3 with `python-flint 0.8.0`.

From the repository root, run:

```powershell
python computations/round21_verify_aggregate_tail.py --precision 192
python -m unittest computations.tests.test_round21_verify_aggregate_tail -v
```

The first command authenticates all five inputs, verifies exactly 1,286
boxes, and exits zero with `PASS`.  The second runs eight targeted tests,
including hash rejection, exact partition coverage, outward endpoint
containment, agreement of the two \(\eta\) formulas at \(1/2\), both
derivative regimes, the full certificate, and rejection below 192 bits.
Both commands passed on 2026-07-15.
