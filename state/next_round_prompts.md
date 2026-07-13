# Next Round Prompts

Generated after Round 7 in run `polya-main`.

Source synthesis: `rounds/polya-main/round_007/judge/judge-007.md`.

## Accepted boundary

Both singular endpoint neighborhoods are analytically discharged. Define

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*:=\frac{\omega_0}{1+2C_*}.
$$

The shell Pólya inequality is proved for all $K\ge0$ when

$$
0<\rho\le\rho_*
\qquad\text{or}\qquad
1-2^{-18}\le\rho<1.
$$

Neither endpoint requires Bessel-root certification. The sole remaining
parameter region is the explicit compact interval

$$
I_*=[\rho_*,1-2^{-18}].
$$

The next primary obligation is `SHELL-rho-compact`; the accompanying bounded
certificate is `COMP-certified-bessel`.

## For A1

Freeze a compact-closure packet with two exact outputs.

1. Give one explicit finite $K_{\mathrm{hi}}$ such that the shell inequality
   is already proved analytically for every

   $$
   \rho\in I_* ,
   \qquad K\ge K_{\mathrm{hi}}.
   $$

2. Translate the remainder into a closed, bounded certificate domain with
   inclusive overlaps at $\rho=\rho_*$ and
   $\rho=1-2^{-18}$.

Use the best piecewise combination of the existing estimates rather than one
needlessly large global formula:

- the small-hole threshold $C_*/(\omega_0-\rho)$ below a chosen
  $\rho_a<\omega_0$;
- the fixed-$\rho$ threshold $K_0(\rho)$ on a central compact interval;
- the Round 6 high-thin threshold $64/(1-\rho)^2$ near $\rho=1$.

Prove every monotonicity or endpoint maximization used to make these bounds
uniform. Record exact rational/algebraic upper bounds suitable for a checker.
Do not send either analytically discharged endpoint neighborhood to the
certificate.

## For A2

Develop the incumbent compact analytic reduction. Begin with

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
$$

where

$$
a_\rho=\frac{2\pi\rho}{1-\rho},
\qquad
\eta_\rho=G_1(\max\{\rho,1/2\}),
\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

Derive a rigorous piecewise upper envelope on $I_*$. Use the Round 7
small-hole threshold near the left endpoint and the Round 6 local-plateau
threshold near the right endpoint whenever they improve this envelope.

The output must identify:

- the finite $K$ interval still requiring certification in each $\rho$
  subinterval;
- the strict angular cutoff $\ell+1/2<K$;
- all possible phase, determinant, and floor walls;
- a finite subdivision rule with no gap at subinterval boundaries.

Optimization is valuable because the raw endpoint bound can be enormous, but
correct finiteness and exact coverage come before numerical efficiency.

## For A3

Receive only the reduced compact packet and independently reconstruct the
piecewise uniform threshold. Attempt to falsify it at:

- $\rho=\rho_*$ and $\rho=1-2^{-18}$;
- every switch between small-hole, fixed-$\rho$, and high-thin estimates;
- $\rho=1/2$, where the definition of $\eta_\rho$ changes branch;
- equality $K=K_{\mathrm{hi}}(\rho)$;
- any monotonicity claim for $K_0$, $a_\rho$, or $\eta_\rho$;
- uncovered slivers between adjacent certificate boxes;
- strict spectral or floor walls lying on a box boundary.

Recompute all constants independently. A bounded box is not a proof until
its analytic covering and boundary conventions are exact.

## For A4

Turn the compact reduction into a certificate specification and a minimal
validated pilot. The specification must state, for every box:

- how the Bessel cross-product or normalized phase is interval-evaluated
  without cancellation;
- how roots are isolated or excluded and how simplicity is used;
- how the angular cutoff is certified uniformly;
- how strict eigenvalue endpoints and ordinary-floor proxy walls are split;
- how neighboring boxes overlap or share certified boundary faces;
- the exact output format that allows an independent checker to recompute the
  count and Weyl margin.

Floating-point scans remain `diagnostic_only`. Interval or ball arithmetic
must be outward rounded and reproducible. Start with a deliberately small
compact pilot box before scaling; do not claim that a pilot certifies the full
compact interval.

## Promotion constraint

Do not promote `SHELL-rho-compact` until:

1. a finite analytic $K_{\mathrm{hi}}$ covers all of $I_*$;
2. every lower-frequency point belongs to an explicit certified box;
3. an independent reconstruction verifies the piecewise analytic cover;
4. an adversarial audit verifies every strict wall and box interface;
5. the certificate is reproducible and independently checked.

Only after that promotion may `SHELL-rho-uniformity` and
`TARGET-shell-d3` enter their final theorem-level clean-room and adversarial
audit.
