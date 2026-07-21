# Round 48 interval counterexample to the continuous quarter-node route

Evidence class: `interval_certified`.  Claim type: route counterexample.

This artifact rejects only

\[
 p\!\left(\xi(n-\tfrac14)\right)
 \le \int_{n-1}^n\frac{\xi(t)^3}{3}\,dt,
 \qquad p(x)=\frac{x(x+1)(2x+1)}6.
\]

It does not reject the discrete QCL cell, literal \(\mathrm{WT}_4\), or a
spectral theorem.

Use the exact rational parameters

\[
 K=\frac{2485744973967441}{20000000},\qquad
 \mu=\frac{1412489996090409}{10^{12}},\qquad
 n=39561154.
\]

The cell straddles the interface because directed Arb evaluation gives

\[
 A(\mu)=39561153.7448320909157\ldots\in(n-1,n).
\]

The exact primitive used by the replay is

\[
 \int_0^z\frac{u^3\arccos(u/R)}\pi\,du
 =\frac{3R^4\arcsin(z/R)
 -z\sqrt{R^2-z^2}(3R^2+2z^2)
 +8z^4\arccos(z/R)}{32\pi}.
\]

Mathematica differentiates this expression to the integrand exactly.  The
initial discovery report contained a mistranscribed primitive; the checked
formula above is the one used for certification.

At 1400 Arb bits with rational inverse brackets of radius below \(10^{-32}\),

\[
 \int_{n-1}^n\frac{\xi(t)^3}{3}\,dt
 \in 940342665.736090048\pm8.69\times10^{-10},
\]

whereas

\[
 p(\xi(n-\tfrac14))
 \in 940343238.4303163436900948474333665
 \pm6.06\times10^{-26}.
\]

Consequently the continuous margin is enclosed by

\[
 -572.69422630\pm5.18\times10^{-9}<0.
\]

Literal strict counting instead gives (N=1412),
(S_2(N)=939385950), and

\[
 L_n=956715.736090048\pm8.69\times10^{-10}>0.
\]

Reproduction:

```powershell
python -B computations/general_d_round48_continuous_quarter_node_counterexample.py --bits 1400 --inverse-radius-digits 32
```

Backend: Python 3.14.4 with `python-flint 0.8.0`, Arb precision 1400 bits.
Coverage: this one explicit rational parameter point only.  Root isolation is
rational bisection with directed action signs.  The script records all final
brackets, active slack, both margins, software, precision, and a deterministic
payload hash.  For the command above, the script SHA-256 is
`06054c777b6a77293afa1ea175f94a7c406c85663f3b8930dd19722eb02a0168`
and the output payload SHA-256 is
`31f37776f1f4ec437195bb6c66edb29ee0e38f0226ca5b2f9b19236f5bdf1002`.
