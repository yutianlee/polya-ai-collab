# Last Validation Report

Date: 2026-07-13

Round: `polya-main` / round 11

## State patch

- Source: `rounds/polya-main/round_011/judge/judge-011.md`.
- The patch creates `SHELL-ultrathin-intermediate-bridge` as
  `proved_internal`, with

  $$
  0<\varepsilon\le\frac1{100},
  \qquad
  a=\varepsilon K\ge\frac1{8\varepsilon^{3/2}}.
  $$

- The accepted product and aggregate ranges own the complementary closed
  range, so the complete all-frequency thin endpoint becomes
  $99/100\le\rho<1$.
- The Round 9 optimized plateau theorem remains valid and
  `proved_internal`, but is no longer an endpoint or compact-envelope
  dependency.
- The compact planning interval becomes
  $I_{11}=[\rho_*,99/100]$ and the all-ratio analytic ceiling becomes
  $K\ge6000^2$.
- `SHELL-rho-compact`, the parent `COMP-certified-bessel`,
  `SHELL-rho-uniformity`, and `TARGET-shell-d3` retain their open or
  diagnostic statuses.
- No route is newly rejected. Round score: 7.

## Analytic review gates

- Frozen dependency packet: PASS.
- Incumbent inverse-action proof: PASS.
- Strictly isolated clean-room proof with a different radial reserve: PASS.
- Adversarial curvature, Stieltjes, constants, dependency, wall, and face
  audit: PASS.
- Exact executable ledger for both proof paths: PASS.

The incumbent controls the shifted radial discrepancy by

$$
D>
\frac{a^2}{4}
-\frac{17}{8}\varepsilon^{2/3}a^{4/3}
-\frac{11}{14}a
$$

and retains the normalized margin

$$
\frac{I-P_{\mathcal A}}{a^2}>\frac{61}{1400}>0.
$$

The independent clean-room reconstruction instead proves

$$
D\ge
\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}
$$

and, after its own angular estimate, the exact margin

$$
\frac{4119252993}{17500000000}>0.
$$

Both paths include threshold equality, radial walls, half-integer angular
walls, proxy integer walls, the ungridded curvature interface, and strict
spectral walls.

## Complete thin endpoint

The three closed optical ranges are

$$
0\le a\le\frac{\pi}{4\varepsilon},
$$

$$
\frac{\pi}{4\varepsilon}
\le a\le\frac1{8\varepsilon^{3/2}},
$$

and

$$
a\ge\frac1{8\varepsilon^{3/2}}.
$$

Their union is every $a\ge0$ for
$0<\varepsilon\le1/100$.  Therefore

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

The endpoint width in $\varepsilon$ expands from $1/15625$ to $1/100$, an
exact factor $625/4$.  The newly discharged radius width is $621/62500$.

## Global analytic ceiling

On the new compact interval:

- $[\rho_*,1/16]$ has possible residual only below $64$;
- $[1/16,24/25]$ has possible residual only below
  $K_0(24/25)<6000^2$;
- $[24/25,99/100]$ has possible residual only below
  $20/(1-\rho)^2\le200000$;
- $[99/100,1)$ is proved for every frequency.

Thus

$$
\boxed{
0<\rho<1,
\qquad K\ge6000^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reductions are

$$
\frac{125^5/8}{6000^2}
=\frac{1953125}{18432}>105,
\qquad
\frac{2^{35}}{6000^2}
=\frac{134217728}{140625}>954.
$$

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad
K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$.  Round 11 changes no producer, checker,
certificate, or protected packet.  The independent checker reproduces the
provenance-locked packet hash
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
This remains evidence for one local box only; the parent compact
certification remains `diagnostic_only`.

## Mechanical validation

- Judge State Patch validation before application: PASS.
- Applied proof-obligation graph validation: PASS.
- Independent post-promotion graph, narrative, evidence-path, face, and
  provenance audits: PASS.
- Exact Round 11 bridge-and-ceiling ledger: PASS.
- Focused Round 11 tests: 4 passed.
- Complete computation suite: 36 passed.
- Round 8 independent certificate and provenance checker: PASS.
- Markdown whitespace and diff checks: PASS.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge6000^2$.  The full
all-frequency theorem remains open on the exact compact residual

$$
\mathcal D=(I_{11}\times[0,\infty))\setminus\mathcal A
$$

below that ceiling.  Round 12 should target a further central--thin seam
compression, with a concrete target $\varepsilon\le1/20$,
$K\ge24/\varepsilon^2$, and $K_0(19/20)<3300^2$.  Any certified computation
must remain a bounded, face-connected extension of the existing pilot.
After the compact residual closes, fresh theorem-level clean-room and
adversarial audits remain mandatory before promotion of the final target.
