# Next Round Prompts

Generated after weighted-lattice round 3 in run `polya-main`.

Source synthesis: `rounds/polya-main/round_003/judge/judge-003.md`.

## For A1

Prepare a reduced packet for `SHELL-low-interface-shifted-tails`. State the ordinary-floor tail exactly, the start condition $r+1/2<\mu=\rho K$, the concave-to-convex derivative signs, the integral target, and every lattice-wall convention. Include the optimized $H_\mu$-capped fallback, but keep it separate from the coarse claim.

## For A2

Develop the incumbent proof of

$$
\mathcal T_r\le2\int_{r+1/2}^{K}
\bigl(G_K(z)-G_{\rho K}(z)\bigr)\,dz
$$

for starts below $\rho K$. Work horizontally by integer phase levels or adapt the audited annulus concave/convex trapezoidal lemmas with explicit interface corrections. Do not reuse the already-discharged high-tail proof as though it crossed the interface. Freeze the attempt before review.

## For A3

Receive only the reduced low-tail packet and permitted source cards. Independently prove the tail inequality or produce the first exact counterexample. Stress-test $\rho K$ on a half-integer, starts immediately below the interface, and coarse-proxy integer walls. If the coarse statement fails, test the optimized $\min\{H_\mu,1/4\}$ envelope.

## For A4

After A2 and A3 are frozen, reconstruct every horizontal block, floor endpoint, and nonintegral-interface correction. Separately design interval/ball checks for any finite exceptional parameter region. The current floating grid remains `diagnostic_only`.

## Promotion constraint

Do not promote `SHELL-weighted-lattice-fractional`, the parent lattice count, or the shell theorem unless every low-interface shifted tail is discharged through a complete proof or a rigorously certified finite partition. The thin-width phase-zero lemma and high-angular tails are already closed and should not be reproved.
