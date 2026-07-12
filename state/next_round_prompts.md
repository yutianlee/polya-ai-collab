# Next Round Prompts

Generated after Round 4 in run polya-main.

Source synthesis: rounds/polya-main/round_004/judge/judge-004.md.

## For A1

Prepare the reduced packet for SHELL-rho-one-endpoint. Use

$$
\varepsilon=1-\rho,\qquad a=\varepsilon K.
$$

The region $a\le\pi$ already has zero actual strict shell count. For
$a>\pi$, test the exact comparison obtained from

$$
L_\ell
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1),
$$

namely

$$
\lambda_{\ell,n}(\rho)
\ge
\frac{n^2\pi^2}{\varepsilon^2}+\ell(\ell+1).
$$

Reduce the thin-shell endpoint to an explicit weighted integer inequality in
$(\varepsilon,a)$. State every strict wall and the overlap needed with the
fixed-$\rho$ theorem. If the comparison is too coarse, identify its first
counterexample rather than weakening the target silently.

## For A2

Attack the product-cylinder proxy. For each $n\pi<a$, let $L_n$ be the largest
integer satisfying

$$
L_n(L_n+1)
<
\frac{a^2-n^2\pi^2}{\varepsilon^2}.
$$

The comparison count is

$$
\sum_{n\pi<a}(L_n+1)^2.
$$

Seek an explicit $\varepsilon_0>0$ and a rigorously covered range of $a>\pi$
for which this is at most

$$
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)
\frac{a^3}{\varepsilon^3}.
$$

Preserve strict inequalities at $n\pi=a$ and at
$L_n(L_n+1)=(a^2-n^2\pi^2)/\varepsilon^2$. Quantify the discrete margin
against the angular-rounding error and show how large optical widths overlap
the existing $K_0(\rho)$ theorem.

## For A3

Receive only the reduced thin-shell packet and independently reconstruct or
falsify the proposed integer inequality. Search especially near
$a=m\pi$, angular walls, $\varepsilon\downarrow0$, and the first nonzero
radial mode.

As an independent secondary task, audit SHELL-rho-zero-endpoint. Determine
whether a quantitative comparison with the audited ball theorem gives a
uniform small-hole range, and identify the low angular modes or shrinking
volume margin that prevent a direct perturbative argument.

## For A4

Adversarially audit the frozen thin-shell proof, including the direction of
the operator comparison and every strict lattice wall. In parallel, specify
the interval-certificate interface but do not certify an unbounded domain.
The eventual artifact must include:

- the exact compact parameter boxes left by both endpoint arguments;
- interval or ball arithmetic versions and commands;
- determinant or phase-wall isolation with the proved root simplicity;
- angular cutoff and total multiplicity handling;
- strict endpoint decisions;
- coverage tables and artifact hashes.

Existing floating diagnostics remain diagnostic_only.

## Promotion constraint

Round 4 proves the exact spectrum and the fixed-$\rho$ high-energy theorem.
Do not promote the all-$K$ shell theorem until:

1. the thin-shell and small-hole endpoints have explicit uniform coverage;
2. their overlap with compact-$\rho$ bounds leaves a bounded residual set;
3. that set is interval-certified; and
4. a fresh theorem-level clean-room and adversarial review pass.
