# Round 9 exact-arithmetic check of the optimized constants

## Verdict

**PASS.**  The finite rational comparisons for both independently derived
candidates were recomputed with fractions.Fraction and no floating-point
arithmetic:

- incumbent fallback: $C=18$;
- promoted candidate: $C=125/8$.

The executable check is
computations/round9_verify_thin_plateau_constants.py.

## Promoted $C=125/8$ ledger

The exact checks include:

1. the Machin upper bound lies below $1571/500$ by

   $$
   \frac{2736890694763}{6719303882812500}>0;
   $$

2. the uniform derivative bound is

   $$
   \frac{\partial H}{\partial P}
   <\frac{673816}{1366875}<\frac12;
   $$

3. the no-drop endpoint margin is

   $$
   \frac{72581986185449}{5925464687161600}>0;
   $$

4. the final payment margin is

   $$
   \frac{2829397}{3732696}-\frac{132}{175}
   =\frac{2428603}{653221800}>0;
   $$

5. the overlap is

   $$
   \varepsilon_{\rm new}=\frac1{15625},
   \qquad
   K_{\rm join}=\frac{125^5}{8}<2^{32}.
   $$

## Fallback $C=18$ ledger

The simpler independent incumbent is also valid.  Its decisive checks are

$$
F_{10}(53)=\frac{203}{320}>0,
\qquad
10\left(\frac{12656}{2343}-\frac{53}{10}\right)
=\frac{2381}{2343}>1,
$$

with overlap $\varepsilon=1/20736$.

The fallback is retained as variance-reducing evidence.  The stronger
$C=125/8$ theorem is promoted because its separate clean-room proof,
dependency audit, and targeted adversarial reconstruction all pass.
