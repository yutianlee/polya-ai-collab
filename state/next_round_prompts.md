# Next Round Prompts

Generated after Round 9 in run `polya-main`.

## Accepted boundary

Let

$$
\omega_0=\frac{\sqrt{3}}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt{2}}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

Round 9 proved the radius-sensitive local-plateau estimate with the exact
constant

$$
C_{\mathrm{lp}}=\frac{125}{8}.
$$

Together with the low-frequency thin-shell estimate, it gives complete
analytic coverage for

$$
0<\varepsilon=1-\rho\le \frac1{15625}.
$$

Thus the shell Pólya inequality is proved for every $K\ge0$ in both endpoint
neighborhoods

$$
0<\rho\le\rho_*
\qquad\text{and}\qquad
1-\frac1{15625}\le\rho<1.
$$

The remaining thin residual lies below

$$
\frac{125}{8}\,15625^2
=\frac{30517578125}{8}
<2^{32}.
$$

By contrast, the current central threshold $K_0(\rho)$ near
$\rho=99/100$ still supplies the dominant compact ceiling:

$$
K_0\!\left(\frac{99}{100}\right)
<180000^2<2^{35}.
$$

The present compact high ceiling is therefore $2^{35}$, not the thin-shell
ceiling. The parent obligations `SHELL-rho-compact`,
`COMP-certified-bessel`, `SHELL-rho-uniformity`, and `TARGET-shell-d3`
remain open.

## Round 10 primary target

Analytically compress the central-to-thin seam. The preferred route is to
extend the radius-sensitive local-plateau and scaled-loss argument from

$$
0<\varepsilon\le\frac1{100}
$$

to an explicit rational or algebraic endpoint

$$
0<\varepsilon\le\varepsilon_0,
\qquad
\varepsilon_0>\frac1{100}.
$$

The constant $125/8$ may be retained only if every estimate that used
$\varepsilon\le1/100$ is rederived on the enlarged interval. A piecewise
explicit threshold is also acceptable if its branches and switch points are
proved exactly.

If that route does not close, derive a strictly better central high-frequency
threshold on an explicit interval ending at $\rho=99/100$. In either route,
the output must give:

1. an exact new seam point $\rho_s=1-\varepsilon_0<99/100$, or an exact
   replacement central interval;
2. a gap-free analytic union at every switch, including equality;
3. an exact formula for the resulting global compact ceiling;
4. an exact comparison with the old ceiling $2^{35}$ and with the thin bound
   $30517578125/8$;
5. a quantified reduction of the unresolved region.

The strongest useful outcome lowers the dominant central ceiling. A merely
numerical candidate or a reformulation that leaves the same $2^{35}$ bound
does not satisfy the primary target.

Do not brute-force enumerate modes, angular walls, eigenvalues, or boxes up
to $2^{35}$. Round 10 is an analytic-compression round.

## For A1: obligation architect and lead synthesis

Freeze a packet `SHELL-central-thin-seam-compression` containing only the
accepted Round 9 inputs and the exact Round 10 claim.

First write the current analytic cover as closed parameter sets. Identify
which set owns the face $\varepsilon=1/100$, which set owns the proposed new
face $\varepsilon=\varepsilon_0$, and how strict eigenvalue counting is
handled on both faces. Then derive the exact ceiling after moving the seam.

For the preferred route, inventory every use of $\varepsilon\le1/100$ in the
local-plateau proof, including:

- the dangerous-plateau location;
- lower bounds for the scaled phase and local slope;
- the quadratic estimate for the loss parameter $p$;
- the branch condition for $p-dm$;
- the estimate for $K G_1(1-\varepsilon)$;
- the interface-loss payment and all floor endpoints.

Do not extrapolate the Round 9 theorem beyond its proved domain. Reprove each
domain-dependent inequality with exact rational or algebraic constants.

If the extension fails, record the first exact failed inequality and pivot to
the alternative central-threshold route. The final synthesis must select one
claim, one exact switch, and one exact ceiling; it must not average or vote
between agents' arguments.

## For A2: analytic proof developer

Develop the preferred enlarged-domain proof independently from the audited
tail decomposition and scaled-loss argument. Keep

$$
M=\lfloor K\eta\rfloor+dm-p,
\qquad
\eta=G_1(1-\varepsilon),
$$

with the no-drop branch $p=n$, immediate-drop branch $p=0$, and $n=0$
branch separate until the final uniform estimate. Preserve the exact
condition under which $p-dm$ is positive.

Your output must include:

- an exact admissible $\varepsilon_0>1/100$;
- every elementary bound on $\pi$, radicals, and $G_1$ used in the proof;
- a proof of all monotonicity claims on the enlarged interval;
- safe ownership of integer walls and strict floor endpoints;
- the exact central/thin switch and the resulting ceiling;
- an exact comparison showing whether the central threshold still dominates.

If a constant or switch is discovered numerically, replace it by a rational
or algebraic enclosure and prove the required sign symbolically. Floating
point may guide exploration but may not certify the claim.

As a fallback, improve $K_0(\rho)$ on a closed interval
$[\rho_s,99/100]$ by retaining radius dependence that was previously
discarded. State the improved threshold explicitly and prove its match to the
unchanged central and thin estimates on both boundary faces.

## For A3: clean-room reconstruction and adversarial audit

Receive only the frozen claim, definitions, and allowed prior lemmas. First
reconstruct the proof without the incumbent derivation. Then perform a
separate adversarial constants-and-walls audit.

Attempt to falsify the candidate at:

- $\varepsilon=1/100$, $\varepsilon=\varepsilon_0$, and the old endpoint
  $1/15625$;
- $K$ equal to every proposed threshold and at every piecewise switch;
- the exact face $\rho=1-\varepsilon_0$ from both adjacent regimes;
- $K\eta$ on an integer wall and immediately on either side;
- the branches $p=n$, $p=0$, and $n=0$;
- the first point where a proof uses $x_0\ge K/2$ or an analogous localization;
- the maximal interface loss and equality in its payment;
- every inequality inherited from a proof whose domain ended at
  $\varepsilon=1/100$;
- every monotonicity assertion used to place the global ceiling at a corner;
- the proposed exact comparison with $2^{32}$ and $2^{35}$.

Reject circular use of the old local-plateau theorem outside its stated
domain. Reject any cover whose adjacent closed sets omit a face, double-own a
strict counting convention inconsistently, or rely on sampled parameter
values. Report clean-room and adversarial verdicts separately.

## For A4: secondary face-connected certification pilot

Certification remains secondary and must not be presented as a substitute
for analytic compression.

1. Add at most one small rational box sharing a complete face with the
   existing certified manifest, or certify why that face must be split.
2. State exact face ownership and verify the union of the old and new cells.
3. Use outward-rounded Arb for determinant/root enclosures and retain an
   independent checker that shares neither producer code nor Flint code for
   decisive low-channel identities.
4. Test tampering of coordinates, counts, determinant signs, truncation,
   face ownership, manifest coverage, and hashes.
5. Report the added parameter area and spectral range so that this pilot
   cannot be mistaken for coverage of the high-frequency residual.

Do not launch a grid, wall enumeration, or eigenvalue sweep toward $2^{35}$.
The pilot validates only the face-connected certificate format.

## Promotion constraints

Promote a Round 10 seam-compression lemma only after all of the following
hold:

1. the enlarged domain or improved central interval is explicit and nonempty;
2. every domain-dependent Round 9 estimate is rederived rather than assumed;
3. all switches, ceilings, and comparisons are exact;
4. the analytic cover includes every switch face with compatible strict-count
   conventions;
5. an isolated clean-room reconstruction passes;
6. an independent adversarial constants, branches, and walls audit passes;
7. the resulting dominant compact ceiling is strictly smaller than the
   currently justified one, or the judge records the exact first obstruction.

The small certification pilot may be promoted only as a local certified
subobligation. It cannot promote `COMP-certified-bessel` or any theorem-level
parent. Keep all parent obligations open until an exact checked cover of the
entire residual set exists, followed by fresh theorem-level clean-room and
adversarial audits.
