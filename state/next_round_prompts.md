# Next Round Prompts

Generated after Round 6 in run `polya-main`.

Source synthesis: `rounds/polya-main/round_006/judge/judge-006.md`.

## Accepted boundary

The exact spectrum, fixed-$\rho$ high-energy theorem, and complete thin-shell
endpoint are proved. In particular,

$$
1-2^{-18}\le\rho<1,
\qquad K\ge0
$$

requires no Bessel-root certification. The next primary obligation is
`SHELL-rho-zero-endpoint`; `SHELL-rho-compact` and
`COMP-certified-bessel` are secondary and must be scoped only after the
small-hole split is explicit.

## For A1

Prepare and freeze the reduced packet for `SHELL-rho-zero-endpoint`. It must
state one quantitative theorem with an explicit constant $\rho_0>0$:

$$
0<\rho\le\rho_0,
\qquad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
$$

Use the scaled inner parameter

$$
\mu=\rho K
$$

and require an explicit case split at least between $\mu<1/2$ and
$\mu\ge1/2$. List the exact spectrum, strict phase convention, audited ball
source, and `state/lemma_packets/SHELL-low-interface-small-hole.md` as the
available evidence, while distinguishing proved inputs from routes that still
need proof. The packet must identify a finite residual $(\rho,K)$ region and
an explicit overlap with the compact-$\rho$ interval.

Do not use pointwise convergence of shell roots to ball roots as a uniform
theorem. State the required constants, low-order exceptions, phase/floor
walls, and volume-margin inequality explicitly.

## For A2

Develop the incumbent small-hole proof. Start from the proved shifted-tail
sector in `state/lemma_packets/SHELL-low-interface-small-hole.md`:

$$
0<\rho<\omega_0,
\qquad
K(\omega_0-\rho)\ge C_*,
$$

where

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15}.
$$

Turn this into an explicit uniform high-$K$ threshold for
$0<\rho\le\rho_0<\omega_0$. Combine it with the exact zero-count region
$(1-\rho)K\le\pi$, then attack only the remaining bounded window. For that
window, seek a quantitative comparison with the Dirichlet ball that controls
the loss of volume $1-\rho^3$ and is uniform in every retained angular order.

Acceptable alternatives include a direct strict phase comparison at fixed
$\mu=\rho K$, a finite low-order analytic enclosure plus an angular-tail
theorem, or an analytic reduction to explicit interval boxes. Every route
must provide a numerical-free proof of boundedness and explicit overlap with
`SHELL-rho-compact`.

## For A3

Receive only the reduced packet and reconstruct the proposed small-hole
theorem independently. Try to falsify it at:

- $\rho K<1/2$, where the inner Bessel argument is below the first
  half-integer angular scale;
- $\ell=0,1,2$ and the first radial roots;
- exact shell eigenvalues and exact phase or floor walls;
- $\rho=\rho_0$ and every joining value of $K$;
- the transition between the zero-count, analytic high-$K$, and finite-window
  pieces;
- any step that replaces pointwise ball convergence by an unstated uniform
  estimate;
- loss of the factor $1-\rho^3$ in the Weyl target.

Report the first unsupported implication if the proof fails. If it passes,
reconstruct all constants without consulting the incumbent proof.

## For A4

Design the bounded certificate only after A1/A2 provide explicit boxes. The
certificate must isolate every relevant Bessel cross-product root or phase
wall with interval/ball arithmetic, preserve strict spectral counting, and
cover parameter-box boundaries without gaps. It must also certify the floor
state on each box or subdivide at every possible floor wall.

Keep floating-point scans and symbolic experiments labeled
`diagnostic_only`. Do not certify an unbounded strip, and do not spend any
certificate budget on $1-2^{-18}\le\rho<1$, which is analytically discharged.

In parallel, formulate a uniform bound for $K_0(\rho)$ on the eventual compact
interval $[\rho_0,1-2^{-18}]$ and translate the low-frequency remainder into
explicit finite boxes.

## Promotion constraint

Do not promote `SHELL-rho-zero-endpoint` until:

1. one explicit $\rho_0$ and all-$K$ covering are proved;
2. a clean-room reconstruction and adversarial wall/constants audit pass;
3. every computational subclaim used in the proof is interval-certified;
4. the result overlaps the compact-$\rho$ sector with inclusive endpoints.

Do not promote `SHELL-rho-uniformity` or `TARGET-shell-d3` until the compact
finite window is also closed and a fresh theorem-level audit passes.
