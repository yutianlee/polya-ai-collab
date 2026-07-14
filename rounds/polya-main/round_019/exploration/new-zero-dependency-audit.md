# Round 19 New-Zero Dependency Audit

Date: 2026-07-14

Verdict: **PASS**.

First unsupported implication: **none**.

This audit checks exactly the two new frequency bounds proposed for the
Round 19 $k_6$ staircase:

$$
j_{11/2,1}>\frac{17}{2},
\qquad
j_{3/2,2}>\frac{77}{10}.
$$

The full source and algebra record is
`sources/round19_bessel_zero_bounds.md`.

## Provenance separation

- **External, new exact-order source dependency:** the inequality printed
  in the [Lorch SIAM publisher abstract](https://epubs.siam.org/doi/10.1137/0524050),
  specialized only at $\nu=11/2$.
- **External identity:** [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3),
  identifying positive spherical and ordinary Bessel zeros.
- **Internal:** the complete $j_{3/2,2}$ argument from the elementary
  order-one spherical formula and the equation $\tan x=x$.
- **Internal and separate:** zero extension plus fixed-channel min–max from
  the shell to the ball, for the relevant min–max index.

The existing `SRC-LORCH` scope is not silently enlarged. A State Patch may
add a new narrow source obligation or explicitly extend the old obligation
only after preserving this exact-order provenance record.

## Exact first-zero check

At $\nu=11/2$, Lorch's second lower bound is

$$
j_{11/2,1}^2>
\frac{507(\sqrt{77}-1)}{52}.
$$

Its denominator is positive. The desired comparison reduces to
$507\sqrt{77}>4264$, and exact squaring gives

$$
507^2\cdot77-4264^2=1611077>0.
$$

Both sides are positive, so no sign is lost by squaring. This proves the
strict $17/2$ bound.

## Exact second-zero check

The positive order-one spherical zeros solve $\tan x=x$. The function
$f(x)=\tan x-x$ is strictly increasing on each
$(n\pi,n\pi+\pi/2)$, crosses once there for every $n\ge1$, and has no
positive root on the complementary half-period. Thus the second positive
zero is the unique root in $(2\pi,5\pi/2)$.

At $x_0=77/10$, put $y=5\pi/2-x_0$. From
$333/106<\pi<22/7$,

$$
0<y<\frac\pi2,
\qquad
y>\frac{163}{1060}>\frac{10}{77}.
$$

Since $\tan y>y$,

$$
\tan x_0=\cot y<\frac1y<\frac{77}{10}=x_0.
$$

Hence $f(x_0)<0$, and strict monotonicity places the second root to the
right of $77/10$.

## Shell-use boundary

The two zero bounds become shell exclusions only after applying the
internal fixed-channel min–max comparison. Lorch is not cited for shell
cross-products, higher radial exclusions, multiplicities, or Weyl
payments. DLMF is cited only for the spherical/ordinary identity and
explicit spherical formula context.

No other Bessel order, radial index, source statement, or spectral claim is
approved by this audit.
