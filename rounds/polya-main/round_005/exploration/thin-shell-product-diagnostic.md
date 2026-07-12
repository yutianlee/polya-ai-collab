# Thin-Shell Product Proxy: Exact Falsification and Diagnostic Wall Scan

Status: **the global product-proxy inequality is false**  
Exact components: asymptotic obstruction, one rational counterexample, and an arbitrarily thin counterexample family  
Floating components: wall-location scans only; explicitly diagnostic, not certified

## 1. Conclusion

Let

$$
x_n(\varepsilon,a)
=\frac{a^2-n^2\pi^2}{\varepsilon^2},
\qquad n\pi<a,
$$

and let \(L_n\) be the largest nonnegative integer satisfying

$$
L_n(L_n+1)<x_n.
$$

The proposed comparison is

$$
P(\varepsilon,a)
=\sum_{n\pi<a}(L_n+1)^2
\stackrel{?}{\le}
W(\varepsilon,a)
:=
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)
\frac{a^3}{\varepsilon^3}.
$$

This is not globally true for any fixed positive thinness. More strongly:

1. For every fixed \(0<\varepsilon\le1\), \(P/W\) tends to a limit strictly larger than one as \(a\to\infty\).
2. There is an exact rational counterexample
   $$
   \boxed{(\varepsilon,a)=(1/4,11).}
   $$
3. There is an exact family of counterexamples approaching the thin limit:
   $$
   \boxed{
   \varepsilon=\frac1Q,\qquad a=Q\pi,\qquad Q=4,5,\ldots .
   }
   $$

Consequently there is no \(\varepsilon_0>0\) for which the product proxy proves \(P\le W\) for every \(0<\varepsilon\le\varepsilon_0\) and every \(a>\pi\).

The thin-limit transition occurs on the two-parameter scale

$$
\boxed{
\frac{\varepsilon a}{\pi}\approx\frac34,
}
$$

not at an epsilon-only threshold. Floating wall sweeps locate the first failures near this value for \(\varepsilon\le0.1\). Because the first violation is often created by a single angular jump and can have relative size only \(10^{-6}\), this numerical location must not be treated as a proof threshold.

## 2. Exact strict-wall formula

Let

$$
r_n
=\frac{\sqrt{1+4x_n}-1}{2},
\qquad r_n(r_n+1)=x_n.
$$

The strict angular inequality gives

$$
\boxed{
L_n+1=\lceil r_n\rceil.
}
$$

Indeed, if \(q=L_n+1\), then

$$
(q-1)q<x_n\le q(q+1).
$$

At an angular wall \(x_n=\ell(\ell+1)\), one has

$$
r_n=\ell,\qquad L_n=\ell-1,\qquad L_n+1=\ell.
$$

Immediately to the right of that wall, \(L_n+1\) becomes \(\ell+1\), and the product count jumps by

$$
(\ell+1)^2-\ell^2=2\ell+1.
$$

At a radial wall \(a=m\pi\), the \(n=m\) term is absent. Immediately to the right it enters with \(L_m=0\), producing a jump of one.

For fixed \(\varepsilon\), \(P\) is constant between these radial and angular walls, while \(W\) is strictly increasing in \(a\). Therefore every local maximum of \(P/W\) occurs immediately to the right of a wall. The equality side and immediate-right side must not be conflated.

## 3. Exact rational counterexample

Take

$$
\varepsilon=\frac14,\qquad a=11.
$$

Use the classical rational bounds

$$
\frac{333}{106}<\pi<\frac{22}{7}.
$$

They imply

$$
3\pi<11<4\pi,
$$

so the radial indices are exactly \(n=1,2,3\). Here

$$
x_n=16(121-n^2\pi^2).
$$

The same rational bounds verify the following strict wall cells:

| \(n\) | \(q_n=L_n+1\) | exact cell containing \(x_n\) |
|---:|---:|---:|
| 1 | 42 | \(41\cdot42<x_1\le42\cdot43\) |
| 2 | 36 | \(35\cdot36<x_2\le36\cdot37\) |
| 3 | 23 | \(22\cdot23<x_3\le23\cdot24\) |

For example, replacing \(\pi\) by the two rational endpoints gives rigorous lower and upper enclosures for every \(x_n\); all six displayed comparisons hold with room to spare. Hence

$$
P(1/4,11)
=42^2+36^2+23^2
=3589.
$$

On the other hand,

$$
W(1/4,11)
=\frac{98494}{9\pi}.
$$

Since \(\pi>333/106\),

$$
W(1/4,11)
<
\frac{98494\cdot106}{9\cdot333}
=\frac{282172}{81}
<3589.
$$

Thus

$$
\boxed{
P(1/4,11)>W(1/4,11)
}
$$

is an exact counterexample with both input parameters rational. No floating-point evaluation is used in this conclusion.

## 4. Exact counterexamples with \(\varepsilon\downarrow0\)

Let \(Q\ge4\) be an integer and set

$$
\varepsilon=\frac1Q,\qquad a=Q\pi.
$$

The strict radial range is \(n=1,\ldots,Q-1\), and

$$
x_n
=\pi^2Q^2(Q^2-n^2).
$$

Write \(q_n=L_n+1=\lceil r_n\rceil\). Since

$$
r_n^2=x_n-r_n>x_n-\sqrt{x_n}
$$

and \(q_n\ge r_n\),

$$
q_n^2>x_n-\sqrt{x_n}.
$$

Therefore, with \(S_Q=\sum_{n=1}^{Q-1}x_n\),

$$
\begin{aligned}
P
&>S_Q-\sum_{n=1}^{Q-1}\sqrt{x_n}\\
&>S_Q-\pi Q^2(Q-1).
\end{aligned}
\tag{1}
$$

The last step uses

$$
\sqrt{x_n}
=\pi Q\sqrt{Q^2-n^2}<\pi Q^2.
$$

The polynomial sum is exact:

$$
S_Q
=
\frac{\pi^2Q^3(Q-1)(4Q+1)}6.
$$

The proposed Weyl quantity is

$$
W_Q
=\pi^2
\left(
\frac23Q^5-\frac23Q^4+\frac29Q^3
\right).
$$

A direct subtraction gives

$$
S_Q-W_Q
=\frac{\pi^2Q^3(3Q-7)}{18}.
$$

Combining this with (1),

$$
P-W_Q
>
\pi Q^2
\left(
\frac{\pi Q(3Q-7)}{18}-(Q-1)
\right).
$$

Using only \(\pi>3\), the bracket is strictly larger than

$$
\frac{3Q^2-13Q+6}{6}.
$$

This is positive at \(Q=4\) and strictly increasing for every \(Q\ge4\). Hence

$$
\boxed{
P(1/Q,Q\pi)>W(1/Q,Q\pi)
\quad\text{for every integer }Q\ge4.
}
$$

These failures occur at the radial wall itself, where the \(n=Q\) mode is correctly excluded. The strict radial convention therefore does not rescue the proposed inequality.

## 5. Global asymptotic obstruction

The failure is structural rather than a collection of isolated wall accidents. From

$$
r_n\le q_n<r_n+1,\qquad r_n^2=x_n-r_n,
$$

one obtains the uniform estimate

$$
x_n-\sqrt{x_n}
<q_n^2
<x_n+2\sqrt{x_n}+1.
$$

Let

$$
N=\left\lceil\frac a\pi\right\rceil-1.
$$

Then

$$
\sum_{n=1}^N x_n
=
\frac1{\varepsilon^2}
\left(
Na^2-\frac{\pi^2N(N+1)(2N+1)}6
\right)
=
\frac{2a^3}{3\pi\varepsilon^2}
+O_\varepsilon(a^2).
$$

The accumulated angular-rounding error is also \(O_\varepsilon(a^2)\). Thus, for fixed \(\varepsilon>0\),

$$
P(\varepsilon,a)
=
\frac{2a^3}{3\pi\varepsilon^2}
+O_\varepsilon(a^2).
$$

Meanwhile,

$$
W(\varepsilon,a)
=
\frac{2a^3}{9\pi\varepsilon^2}
(3-3\varepsilon+\varepsilon^2).
$$

Consequently

$$
\boxed{
\lim_{a\to\infty}\frac{P(\varepsilon,a)}{W(\varepsilon,a)}
=
\frac{3}{3-3\varepsilon+\varepsilon^2}>1
\qquad(0<\varepsilon\le1).
}
$$

This proves that no positive epsilon-only global range exists.

The mechanism is clear: the product proxy has the flat-width leading density, while the exact shell volume contains the smaller curvature factor

$$
1-\varepsilon+\frac{\varepsilon^2}{3}.
$$

For any fixed positive \(\varepsilon\), that mismatch is of leading order in \(a^3\); angular rounding is not the primary obstruction at large \(a\).

## 6. Why the transition scale is \(\varepsilon a/\pi\approx3/4\)

At an exact radial wall \(a=m\pi\), define the unrounded quadratic sum

$$
S(\varepsilon,m)
=
\frac{\pi^2}{\varepsilon^2}
\frac{m(m-1)(4m+1)}6.
$$

Its difference from \(W\) is

$$
S-W
=
\frac{\pi^2}{\varepsilon^2}
\left[
\left(\frac{2\varepsilon}{3}
-\frac{2\varepsilon^2}{9}\right)m^3
-\frac{m^2}{2}
-\frac m6
\right].
$$

Writing \(c=\varepsilon m=\varepsilon a/\pi\), the equation \(S=W\) becomes

$$
(12-4\varepsilon)c^2-9c-3\varepsilon=0.
$$

Its positive root is

$$
c_{\mathrm{base}}(\varepsilon)
=
\frac{
9+\sqrt{81+144\varepsilon-48\varepsilon^2}
}{
24-8\varepsilon
}
=\frac34+O(\varepsilon).
$$

The actual integer proxy differs from \(S\) by angular rounding. In the scaling \(m\asymp1/\varepsilon\), that correction is one asymptotic order smaller than the leading sign change, but it is large enough to move the first individual wall by \(O(\varepsilon)\). This explains both the \(3/4\) transition and the small oscillations in the floating scan.

For a bounded optical-width target \(a\le A\), the natural leading-order candidate is therefore

$$
\varepsilon_{\mathrm{crit}}(A)
\sim\frac{3\pi}{4A}.
$$

This is not a proved sharp threshold. A rigorous positive result should retain a strict margin

$$
\frac{\varepsilon A}{\pi}\le\frac34-\delta
$$

and dominate the angular-rounding term explicitly. Based on the diagnostic data below, the conservative region

$$
\frac{\varepsilon A}{\pi}\le0.70,\qquad \varepsilon\le0.1,
$$

is a reasonable next certificate target, but it is diagnostic guidance only.

## 7. Floating wall sweep

**Everything in this section is diagnostic floating-point evidence, not proof.**

The reproducible event sweep enumerates

$$
a_{n,\ell}^2
=n^2\pi^2+\varepsilon^2\ell(\ell+1).
$$

It adds the jump \(1\) for \(\ell=0\) and \(2\ell+1\) for \(\ell\ge1\), then compares the immediate-right limiting count with \(W\) at the wall. Binary64 arithmetic is used for event locations and the displayed ratios.

For thin values, the first detected immediate-right violations were:

| \(\varepsilon\) | first \(\varepsilon a/\pi\) | wall \((n,\ell)\) | immediate-right \(P/W\) | first failing exact radial wall |
|---:|---:|---:|---:|---:|
| 0.10 | 0.7451297 | \((2,225)\) | 1.00000264 | \(m=9\), \(\varepsilon m=0.90\) |
| 0.05 | 0.7598358 | \((13,494)\) | 1.00000344 | \(m=16\), \(\varepsilon m=0.80\) |
| 0.02 | 0.7494458 | \((5,5833)\) | 1.00000438 | \(m=39\), \(\varepsilon m=0.78\) |
| 0.01 | 0.7520860 | \((39,20202)\) | 1.00000079 | \(m=76\), \(\varepsilon m=0.76\) |

The first violations can be extremely narrow and are normally triggered immediately after an angular jump. Exact radial walls detect failure slightly later but much more robustly.

Moderate epsilon values show larger finite-mode oscillations:

| \(\varepsilon\) | first \(\varepsilon a/\pi\) | wall \((n,\ell)\) | immediate-right \(P/W\) |
|---:|---:|---:|---:|
| 1.00 | 1.09665 | \((1,1)\) | 1.38283 |
| 0.75 | 0.86882 | \((1,2)\) | 1.13128 |
| 0.50 | 0.66331 | \((1,5)\) | 1.00434 |
| 0.25 | 0.78675 | \((1,37)\) | 1.00784 |

These moderate values should not be extrapolated to a universal scaled threshold. The convergence toward \(3/4\) is the thin-limit phenomenon.

## 8. Reproducibility

The diagnostic implementation is:

- computations/thin_shell_product_diagnostic.py
- computations/tests/test_thin_shell_product_diagnostic.py

The exact rational certificate uses Fraction arithmetic. The event and radial scans are prominently labeled diagnostic.

Commands used:

    python -m pytest computations/tests/test_thin_shell_product_diagnostic.py -q

    python computations/thin_shell_product_diagnostic.py \
      --epsilons 0.1 0.05 0.02 0.01 \
      --radial-max 100 \
      --c-max 0.80

The tests report:

    4 passed

## 9. Consequence for the proof strategy

The product-cylinder comparison cannot cover an unbounded optical-width range at any fixed \(\varepsilon>0\). It can only be used, if at all, below a two-parameter cutoff of order

$$
a\lesssim\frac{3\pi}{4\varepsilon}.
$$

Therefore the next proof attempt must do at least one of the following:

1. replace the flat product proxy by a curvature-corrected comparison whose cubic leading coefficient matches the shell volume;
2. use the product proxy only in a bounded range with an explicit strict margin below \(3/4\), then provide a genuinely overlapping high-energy argument;
3. retain additional radial information discarded by the coarse operator comparison.

An epsilon-only statement for this proxy should be rejected rather than weakened silently.
