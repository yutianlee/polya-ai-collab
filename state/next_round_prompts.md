# Next Round Prompts

Generated after Round 5 in run polya-main.

Source synthesis: rounds/polya-main/round_005/judge/judge-005.md.

## For A1

Prepare the reduced packet for SHELL-thin-curvature-intermediate. Write

$$
\varepsilon=1-\rho,\qquad
a=\varepsilon K.
$$

The accepted ranges are

$$
K\le\frac{\pi}{4\varepsilon^2}
$$

for $0<\varepsilon\le1/100$, and

$$
K\ge K_0(1-\varepsilon).
$$

The packet must state one exact intermediate theorem with explicit overlap.
It must reject the replacement $r^{-2}\mapsto1$, whose product majorant has
exact counterexamples. Require every new comparison to recover the mean
cross-section

$$
\frac1\varepsilon\int_{1-\varepsilon}^1r^2\,dr
=1-\varepsilon+\frac{\varepsilon^2}{3}
$$

at the cubic level.

## For A2

Develop a radius-sensitive incumbent. The preferred aggregate phase
coordinates are

$$
y=\varepsilon\nu,
$$

and

$$
\mathcal A_{\varepsilon,a}(y)
=
\frac1\pi\int_0^1
\sqrt{
a^2-\frac{y^2}{(1-\varepsilon s)^2}
}_+\,ds.
$$

This is exactly

$$
G_K(\nu)-G_{\rho K}(\nu)
$$

after scaling. Seek a weighted integer inequality directly for the
half-integer mesh $y_\ell=\varepsilon(\ell+1/2)$. Aggregate floor savings
before applying worst-case bounds; the fixed-$\rho$ proof loses uniformity by
requiring every low-interface shifted tail to close separately.

Acceptable alternative routes include:

- radial sublayer bracketing with angular coefficients that preserve the
  Riemann sum for $r^2$;
- a kinetic-plus-centrifugal lower bound that pays explicitly for
  localization near $r=1$;
- an improved thin-scaled shifted-tail inequality with constants uniform in
  $\varepsilon$.

Every route must give a finite explicit threshold and prove overlap.

## For A3

Receive only the reduced packet and independently reconstruct the proposed
intermediate estimate. Search for failure at:

- $\varepsilon a/\pi$ near $3/4$;
- exact radial and angular walls;
- whispering-gallery modes localized near the outer boundary;
- the inner turning interface $y=(1-\varepsilon)a$;
- the claimed overlap point with $K_0(1-\varepsilon)$.

In parallel, continue the independent small-hole audit. Do not infer a
uniform perturbation theorem from pointwise convergence to the ball.

## For A4

Adversarially check the frozen radius-sensitive proof and build diagnostics
for the exact scaled action, not for the rejected flat product majorant.
Separate:

- symbolic or floating exploration;
- exact algebraic wall certificates;
- interval-certified residual boxes.

Do not certify an unbounded intermediate strip. The Bessel certificate remains
diagnostic_only until the analytic endpoint work gives bounded coverage.

## Promotion constraint

Round 5 proves only the low-optical thin-shell window. Do not promote
SHELL-rho-one-endpoint until:

1. a radius-sensitive theorem covers the intermediate window with explicit
   overlap;
2. the remaining thin residual set, if any, is bounded and certified;
3. a clean-room proof and adversarial audit pass.

The global shell theorem additionally requires the small-hole and compact-rho
components and a final theorem-level audit.
