# Next Round Prompts

Generated after the fixed-$\rho$ continuation of round 3 in run `polya-main`.

Source synthesis: `rounds/polya-main/round_003/judge/judge-003-fixed-rho.md`.

## For A1

Prepare a reduced packet for `SHELL-sturm-liouville-completeness`. State the spherical-harmonic orthogonal decomposition, the radial weighted space and unitary one-dimensional transform, Dirichlet endpoint conditions on $[\rho,1]$, the $k=0$ exclusion, radial simplicity, and how accidental equality across distinct $\ell$ channels contributes multiplicity. Keep the strict count convention explicit.

In parallel, map the residual parameter region using

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2
$$

and the exact zero region $(1-\rho)K\le\pi$.

## For A2

Develop the endpoint-uniformity incumbent. Determine whether the fixed-$\rho$ threshold, the zero strip, and compact-$\rho$ subdivision leave a bounded set in variables such as $(\mu,K)$ or optical width $(1-\rho)K$. If not, isolate the precise thin-shell analytic estimate still missing. Do not label a pointwise-in-$\rho$ threshold uniform.

## For A3

Receive only the reduced Sturm--Liouville packet and permitted standard references. Independently reconstruct the separated spectrum and strict count bridge. Check $k=0$, positivity, completeness, radial simplicity, angular multiplicity $2\ell+1$, and cross-channel degeneracy.

For endpoint work, independently audit any proposed compact covering and search for unbounded escape paths as $\rho\to0,1$.

## For A4

Adversarially review the frozen spectral proof. Separately design interval/ball arithmetic only after A1--A2 identify a bounded residual region. The certificate must isolate roots or phase walls rigorously, preserve strict endpoints, state software versions and commands, and produce coverage and artifact hashes. Existing floating diagnostics remain `diagnostic_only`.

## Promotion constraint

`SHELL-weighted-lattice-fractional` is proved only in the stated fixed-$\rho$ high-energy sense. Do not promote the shell theorem until:

1. separated Sturm--Liouville completeness makes the strict count identity unconditional;
2. compact and endpoint regimes cover all $0<\rho<1$;
3. the remaining parameter set is rigorously certified.
