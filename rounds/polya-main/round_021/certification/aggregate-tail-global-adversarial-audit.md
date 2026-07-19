# Round 21 aggregate-tail global certificate: adversarial audit

Date: 2026-07-15

## Verdict

**PASS.** First issue: **none found**.

The authenticated verifier rigorously proves

\[
\rho_c\leq\rho\leq\frac{39}{50},\qquad K\geq200
\quad\Longrightarrow\quad \mathcal B(\rho,K)>0.
\]

The analytic frequency reduction, every required sign, the exact ratio
partition, the piecewise definition of \(\eta_\rho\), the outward Arb
construction, strict interval comparisons, precision and input-hash gates,
and proof/display separation all survived adversarial review.

## Authentication before inspection

The four artifacts were hashed as raw bytes before any was read. Every digest
matched the value supplied for this audit:

| artifact | required and observed SHA-256 | result |
|---|---|---|
| `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md` | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` | match |
| `computations/round21_verify_aggregate_tail.py` | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` | match |
| `computations/tests/test_round21_verify_aggregate_tail.py` | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` | match |
| `rounds/polya-main/round_021/certification/aggregate-tail-global.md` | `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` | match |

The verifier then authenticated its five proof inputs, including the route,
and reported all five expected hashes. Perturbing each expected digest in
turn caused `authenticate_inputs` to reject all five cases. The CLI has no
authentication-off flag: its call to `run_certificate` uses the default
`authenticate=True`. The explicit programmatic `authenticate=False` option
does not affect the documented reproduction path and returns no authenticated
hashes when deliberately used.

## Independent analytic re-derivation

Fix \(\rho\) and set

\[
b=\frac{2\pi\rho}{1-\rho},\quad
\mu=\rho K,\quad R=\rho K+\frac12,\quad C=bK,\quad
S=\sqrt{R^2+C},
\]

with \(d=2\arcsin(\rho)/\pi\) and \(\eta=\eta_\rho\). Here \(b,d,\eta\)
are constant when differentiating in \(K\). Write

\[
I(K)=\frac12\left(RS+C\operatorname{arsinh}\frac{R}{\sqrt C}-R^2\right)
=\int_0^R(\sqrt{x^2+C}-x)\,dx.
\]

Leibniz differentiation gives

\[
I_K=\rho(S-R)+\frac b2\operatorname{arsinh}\frac{R}{\sqrt C}.
\]

Since

\[
\frac{d(S-R)}{dK}=\frac{\rho R+b/2}{S}-\rho,
\qquad
\frac d{dK}\operatorname{arsinh}\frac R{\sqrt C}
=\frac{2\rho K-1}{4KS},
\]

the second derivative is exactly

\[
I_{KK}=\rho^2\left(\frac RS-1\right)
+\frac{\rho b}{2S}+\frac{b(2\rho K-1)}{8KS}.
\]

For

\[
E(K)=-\frac8{15}\left(\sqrt\mu+\frac1{2\sqrt\mu}\right),
\]

direct differentiation gives

\[
E_K=-\frac{2\rho(2\mu-1)}{15\mu^{3/2}},
\qquad
E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}.
\]

Substitution in the authenticated reserve yields precisely the verifier's
first derivative

\[
\begin{aligned}
\mathcal B_K={}&\rho(K\eta-1)+(\mu-\tfrac12)\eta
+d\rho(\mu-1)\\
&-(1+d)I_K-\frac{2\rho(2\mu-1)}{15\mu^{3/2}},
\end{aligned}
\]

and second derivative

\[
\mathcal B_{KK}=2\rho\eta+d\rho^2-(1+d)I_{KK}
+\frac{\rho^2(2\mu-3)}{15\mu^{5/2}}.
\]

No term, coefficient, or sign differs between this derivation, the report,
and `evaluate_at_k0`.

### The bound on \(I_{KK}\) and all sign directions

On the certified domain, \(0<\rho<1\), \(K>0\), \(b>0\), \(d>0\),
\(1+d>0\), \(C>0\), and

\[
S>R=\rho K+\frac12>\rho K>0.
\]

Therefore the first term in \(I_{KK}\) is strictly negative. Moreover,

\[
\frac{b(2\rho K-1)}{8KS}<\frac{\rho b}{4S}
\]

is exactly the strict inequality \(2\rho K-1<2\rho K\), multiplied by
the positive factor \(b/(8KS)\). Consequently

\[
I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K},
\]

where the last strict sign is equivalent to \(\rho K<S\). Multiplication by
the negative coefficient \(-(1+d)\) correctly reverses the inequality. Since
the verifier proves \(\mu>3/2\), it also proves \(E_{KK}>0\). Thus, for
\(K\geq200\),

\[
\mathcal B_{KK}
>2\rho\eta+d\rho^2-\frac{3(1+d)b}{4K}
\geq 2\rho\eta+d\rho^2-\frac{3(1+d)b}{800}
=F(\rho).
\]

All three directions are correct: the first inequality is strict, the second
uses \(1/K\leq1/200\) with a negative coefficient, and the certificate proves
\(F>0\). It follows that \(\mathcal B_K\) is strictly increasing on
\([200,\infty)\); its certified positive value at 200 makes \(\mathcal B\)
strictly increasing; and the certified positive base value proves global
positivity. No unproved monotonicity in \(\rho\) is used.

The earlier route implication also has the needed strictness. If
\(R_{\rm tail}\) denotes the actual tail count, then
\(R_{\rm tail}\geq\mu-1/2\), \(J\geq\mu-3/2\),
\(R_{\rm tail}\leq\mu+1/2\), \(0\leq\tau<1\), and
\(\lfloor K\eta\rfloor>K\eta-1\). Because the verifier establishes
\(\mu>3/2\) and \(K\eta>1\), all factors used to multiply these inequalities
are positive. The floor term is strictly larger than its continuous
replacement, while monotonicity of \(I(C,R)\) in \(R\) and
\(R_{\rm tail}\tau^{5/2}\leq\mu+1/2\) give the remaining weak bounds.
Hence \(\mathcal Q>\mathcal B\), so the certified \(\mathcal B>0\) implies
the required \(\mathcal Q>0\).

## Exact partition, \(\rho_c\), and the \(\eta\) branch

The exact segment lengths are

\[
\frac12-\frac7{51}=\frac{37}{102},
\qquad
\frac{39}{50}-\frac12=\frac7{25}.
\]

At intended width at most \(1/2000\), their exact box counts are respectively
726 and 560. The final low-regime width is \(1/4080\); every other box,
including the final high-regime box, has width \(1/2000\). The audited edge
boxes are

| index | exact box | regime |
|---:|---|---|
| 0 | `[7/51, 14051/102000]` | `rho_le_half` |
| 725 | `[2039/4080, 1/2]` | `rho_le_half` |
| 726 | `[1/2, 1001/2000]` | `rho_ge_half` |
| 1285 | `[1559/2000, 39/50]` | `rho_ge_half` |

There is no gap. The shared endpoint \(1/2\) is deliberately covered by both
closed segments. The exact inequality \(\pi<22/7\) gives

\[
\rho_c=\frac1{1+2\pi}>\frac7{51},
\]

so the rational interval is a superset of the desired interval. An independent
192-bit Arb construction also placed \(\rho_c\) inside the first box.

The authenticated definition is
\(\eta_\rho=G_1(\max\{\rho,1/2\})\), with

\[
G_1(z)=\frac{\sqrt{1-z^2}-z\arccos z}{\pi}.
\]

The verifier therefore correctly uses the constant `g_one(1/2)` on the low
segment and `g_one(rho)` on the high segment. Both expressions are identical
at the shared endpoint. Checks immediately below, at, and immediately above
\(1/2\) were continuous to 100-digit diagnostic precision.

Adversarial in-memory mutations of the partition were all rejected: wrong
count, wrong outer endpoint, a gap, an overlap, zero width, excessive width,
a low box crossing \(1/2\), a wrong branch label, and an unknown branch label.

## Outward Arb and proof dataflow audit

Each intended box endpoint, midpoint, and radius is a `Fraction`, transferred
to an exact `fmpq`. `arb(midpoint, radius)` creates an outward ball, after
which the checker requires that ball to contain outward Arb enclosures of both
exact endpoints. An Arb ball is convex, so endpoint containment covers the
entire rational segment. The full audit repeated this check for all 1,286
endpoint pairs, not only the four pairs selected by the unit test.

All proof expressions are then interval extensions of elementary operations
on that same `rho` ball. Dependency can widen an enclosure but cannot make a
false strict sign pass. In particular, the relatively low displayed bound for
\(\mathcal B\) on the last box is a safe dependency loss. Strict comparisons
use Arb ordering: an independently constructed ball overlapping zero returned
false for both `> 0` and `< 0`.

The source contains no floating-point literals. Its only `float(...)` call is
the diagnostic conversion at line 293, after the current box's Arb proof
checks; that value is used solely to choose a displayed minimum. It cannot
reach `_require_positive`, `_require_less`, partition construction, or any
returned proof expression. The report's phrase “only after every strict sign
check passes” is temporally stronger than the loop implementation—the display
conversion occurs after every check for the current box, not after all boxes—
but this is not proof leakage: any later failed box still raises and prevents
`PASS`.

The minimum-precision gate fails closed at 191 bits before certification and
accepts 192 bits. A separate 256-bit run reproduced the same certified signs
and displayed bounds.

## Reproduction and independent probes

The required commands both passed:

```text
python computations/round21_verify_aggregate_tail.py --precision 192
    PASS; 1,286 boxes = 726 low + 560 high
    display-only lower bounds:
      B200  = 375.4372603381510
      BK200 = 4.798498305533769
      F     = 0.02747676406088864

python -m unittest computations.tests.test_round21_verify_aggregate_tail -v
    Ran 8 tests; OK
```

An independent 100-digit `mpmath` implementation, used only as a diagnostic
cross-check, differentiated the closed forms numerically at
\(\rho=7/51,1/2,39/50\) and \(K=200,237.125\). Residuals between numerical
derivatives and the displayed formulas for \(I_K,I_{KK},\mathcal B_K\), and
\(\mathcal B_{KK}\) were between zero and \(10^{-99}\). At the lower rational
face, true \(\rho_c\), the split, and the upper face, the independently
evaluated \(\mathcal B(\rho,200)\), \(\mathcal B_K(\rho,200)\), \(F(\rho)\),
the margin \(3b/(4K)-I_{KK}\), and the margin
\(\mathcal B_{KK}-F\) were all positive. Perturbed frequency samples at
\(200\), \(200.000001\), \(201\), \(1000\), and \(10^6\) agreed with the
proved monotonicity.

The unit tests are useful gate/regression tests, but the derivative-regime
test consumes quantities produced by `evaluate_at_k0` and is not an
independent formula oracle. This is a test-coverage observation, not a
certificate defect: the formulas and signs were independently re-derived
above, and the rigorous conclusion comes from the authenticated Arb proof,
not from display-value assertions.
