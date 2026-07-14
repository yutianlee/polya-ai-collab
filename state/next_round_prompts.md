# Next Round Prompts

Round: 20

Canonical graph: `state/proof_obligations.yml`, SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.

## Accepted boundary after Round 19

Put

$$
\rho_c=\frac1{1+2\pi},\qquad
\rho_0=\frac1{\sqrt{337}},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},\qquad
d=\frac{\sqrt{337}}2.
$$

Round 19 promotes the two strict analytic bands

$$
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_6(\rho),
$$

and

$$
\rho_0<\rho<\rho_c,\qquad L(\rho)<K\le d.
$$

The only new external payload is the qualified first-zero specialization
$j_{11/2,1}>17/2$ plus the positive spherical/ordinary Bessel identity.
The bounds $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$, fixed-channel
shell-to-ball min--max, ball angular shifts, shell exclusions,
multiplicities, and Weyl payments are internal.

The live cover is $\mathcal A_{19}$. The historical
$\mathcal D_{18}$ has been superseded and must not be used as the current
target.

## Exact live residual to freeze

Before reading, adapting, freezing, or reviewing any candidate proof, freeze
the exact set

$$
\boxed{\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

The freeze must authenticate:

- the authoritative graph hash and every dependency hash;
- the exact classifier for all three components;
- both traces at $\rho=\rho_0$ and $\rho=\rho_c$;
- ownership of $K=L,d,k_6,U$ and the ratio faces
  $\rho=\rho_*,\rho_0,\rho_c,7/8$;
- the empty candidate fiber $L(\rho_0)=d$;
- the inherited ownership of $K=U$, $\rho=\rho_*$, and $\rho=7/8$;
- the covered faces $K=d$ and $K=k_6$;
- nonemptiness via
  $k_6(1/2)<10<30<64<K_0(1/2)=U(1/2)$;
- that $B_0,B_1$ are retained regression evidence and are not subtracted
  again.

The residual-mask freeze and its independent audit must precede any
proof-free candidate freeze.

## Exact Round 20 routing

Route the three components independently, without replacing them by a
rectangle or coarse envelope.

### A1: low-ratio component

Target exactly

$$
\rho_*<\rho\le\rho_0,\qquad L(\rho)<K<U(\rho).
$$

Prospective small-hole shifted-tail work may be used to design the incumbent
only after the residual freeze. Reconstruct every integer/floor gain,
half-integer face, upper-floor branch, and strict payment. Do not infer a
closed component from the existing exploratory notes.

### A2: middle-ratio component

Target exactly

$$
\rho_0<\rho<\rho_c,\qquad d<K<U(\rho).
$$

Prospective lower-staircase work may suggest a finite-wall decomposition,
but all Bessel bounds, propagated angular shifts, radial exclusions, caps,
payments, and both endpoint traces must be restated in the new proof-free
claim and reconstructed independently.

### A2-high: high-ratio component

Target exactly

$$
\rho_c\le\rho<\frac78,\qquad k_6(\rho)<K<U(\rho).
$$

The current high-$k_8$ exploration is only a prospective direction. Audit
any new exact-order Lorch specialization as a separate narrow source
obligation; do not import second zeros, shell cross-product zeros, or
shell-specific comparisons from that source. Inventory every first and
higher radial entry, full multiplicity, moving wall, and upper-floor branch.

Each workstream must return either a complete analytic subclaim with exact
face ownership or the first unsupported implication. Partial PASS labels in
exploration files are not promotion evidence.

## Proof-free candidate gate

After the exact residual and all proposed new dependencies are frozen, A1
must synthesize one proof-free candidate containing only:

- the exact statement and genuinely new set;
- definitions and an explicit dependency whitelist;
- exact parameter domains and all included/excluded faces;
- required constants and source scope;
- an exhaustive falsification list;
- the exact proposed subtraction from $\mathcal D_{19}$;
- a nonemptiness witness for any proposed successor residual.

The candidate must not cite or reveal incumbent proofs. Freeze its bytes and
hash before A3 or A4 begins.

## A3 isolated reconstruction

A3 receives only the frozen claim, residual freeze, and whitelisted
dependencies. A3 must not read Round 20 incumbents or exploratory notes.
It must reconstruct:

- every spectral identity and min--max direction;
- every new zero bound and its internal/external provenance;
- all angular/radial inventories and multiplicity caps;
- all fixed and moving Weyl payments;
- all monotonicity, positivity, squaring, and inverse steps;
- all strict frequency and ratio faces;
- containment in $\mathcal D_{19}$ and exact successor subtraction;
- status calibration and a residual nonemptiness witness.

Return **PASS** or **FAIL** and the first unsupported implication.

## A4 exact audit

A4 independently implements exact rational/integer checks for every finite
constant, threshold ordering, payment, upper-floor comparison, and residual
truth-table face. The verifier and focused tests must be reproducible and
must fail on perturbed constants or face ownership. Executable checks audit
finite arithmetic only; they do not replace the analytic proof.

## Cross-comparison and fresh referee

After A3 and A4:

1. compare the incumbents, isolated proof, source audit, and exact verifier
   line by line;
2. record every discrepancy and whether it is mathematical, provenance,
   face-ownership, or presentation only;
3. give a fresh referee the frozen claim and authenticated evidence;
4. instruct the referee to assume the claim false and reconstruct every
   displayed identity, inequality direction, source scope, uniformity
   assertion, and endpoint/turning face;
5. require **PASS** or **FAIL** with the first unsupported implication.

The fresh referee must have participated in neither incumbent development
nor A3.

## Mandatory promotion gates

No Round 20 claim enters the graph unless all of the following pass:

- exact $\mathcal D_{19}$ residual freeze and independent mask audit;
- source card and dependency audit for every new external input;
- proof-free candidate freeze;
- complete incumbent proof;
- strictly isolated A3 reconstruction;
- independent A4 exact audit and focused tests;
- cross-comparison;
- fresh adversarial referee;
- judge with an exact State Patch and successor residual;
- independent State Patch audit;
- full repository tests, source compilation, graph validation, and
  `git diff --check`.

Apply any accepted State Patch exactly once through the validator. Do not
promote `SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, or `POLYA-program-target` unless the exact successor
residual is empty and a fresh theorem-level audit passes.
`COMP-certified-bessel` remains `diagnostic_only` unless a separate
promotion proves a rigorous bounded certificate family.

## Explicit do-not-claim rules

- Do not treat any current Round 20 exploration file as frozen, independently
  reconstructed, reviewed, or promoted.
- Do not route work to the historical $\mathcal D_{18}$.
- Do not blur strict and inclusive faces at $L,d,k_6,U$ or at ratio splits.
- Do not attribute an internal tangent proof, variational comparison,
  angular shift, shell zero, multiplicity, or Weyl payment to Lorch or FLPS.
- Do not call sampled floating-point roots or plots certified.
- Do not infer proof from agreement among agents.
