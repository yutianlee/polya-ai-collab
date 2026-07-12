## Selected main route

Continue the 3D spherical shell route as the Round 2 primary route. The target remains exact Dirichlet Polya for

$$
A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\},\qquad 0<\rho<1,
$$

with strict counting

$$
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}.
$$

No theorem-level Polya claim is promoted. The selected route is:

1. lock the strict-counting convention and endpoint rule;
2. complete the Sturm-Liouville/spherical-harmonic audit of the shell cross-product formula;
3. use the exact Bessel modulus-phase representation as the qualitative scaffold;
4. source-card Nicholson monotonicity before using it as a proof dependency;
5. derive the strict phase-count identity;
6. isolate the inner turning regime $\rho k\sim\nu$ as the main special-function blocker;
7. isolate the $2\ell+1$ weighted floor/lattice problem as the main discrete blocker;
8. keep computation diagnostic until a committed root-isolation script, command, root-enclosure report, counting table, and limitations exist.

This follows the uploaded Stage C protocol and validator constraints: the judge synthesis must select a route, record useful fragments, reject risky ideas, identify gaps, propose new lemmas, produce a JSON-compatible state patch, and assign next-round prompts only to A1, A2, A3, and A4.

The strategic basis remains the initial program recommendation: spherical shells are the cleanest first non-tiling Euclidean target, ellipses remain the higher-impact longer-term flagship, and certificate families remain the lower-risk fallback. The FLPS-style machine still requires exact spectral-to-lattice correspondence, uniform phase enclosures, explicit lattice inequalities, and certified finite-window closure; none of those can be skipped.

## Useful fragments by source

A1's useful contribution is the target theorem memo and strict-counting normalization. The sharpened fixed-$\rho$ target is

$$
N_D(A_{\rho,1},K^2)\le \frac{2}{9\pi}(1-\rho^3)K^3,\qquad K\ge0.
$$

A1 also supplied the counting/eigenvalue equivalence: for strict counting, $N(\Lambda)\le C\Lambda^p$ for all $\Lambda\ge0$ is equivalent to $\lambda_j\ge(j/C)^{1/p}$ for all $j$, with eigenvalues repeated by multiplicity. This is directly useful for certified finite-window verification.

A2's useful contribution is the central qualitative phase scaffold. With

$$
J_\nu(z)=M_\nu(z)\cos\theta_\nu(z),\qquad
Y_\nu(z)=M_\nu(z)\sin\theta_\nu(z),
$$

one has

$$
F_{\nu,\rho}(k)
=
M_\nu(\rho k)M_\nu(k)
\sin(\theta_\nu(k)-\theta_\nu(\rho k)).
$$

Thus zeros are phase-difference levels. A2 also identified the candidate monotonicity mechanism:

$$
\Psi_{\nu,\rho}(k)=\theta_\nu(k)-\theta_\nu(\rho k),
$$

$$
\Psi_{\nu,\rho}'(k)
=
\frac{2}{\pi k}
\left(M_\nu(k)^{-2}-M_\nu(\rho k)^{-2}\right),
$$

which is positive if $M_\nu(z)^2=J_\nu(z)^2+Y_\nu(z)^2$ is strictly decreasing. This should become `SHELL-phase-monotonicity`, but only as `derived_under_assumptions` until Nicholson's formula, validity range, and phase convention are source-carded. The cross-review bundle already converged on accepting `SHELL-exact-phase-rep`, `SHELL-phase-monotonicity`, `SHELL-count-floor-identity`, and `SHELL-inner-turning` with conservative statuses.

A3's useful contribution is the correct warning that the annulus lattice count does not automatically transfer to 3D. The factor $2\ell+1$ makes the count genuinely multiplicity-weighted, and any imported floor-sum lemma must be audited for whether it survives this weight. A3 also proposed the spherical-Bessel algebraic route: because $\nu=\ell+1/2$ in $d=3$, one can express the cross-product in finite trigonometric-rational form. This is valuable for certified computation and low-$\ell$ diagnostics, but it is not a replacement for high-energy phase enclosures.

A4's useful contribution is the formula and computation audit. The derivation

$$
R''+\frac{2}{r}R'+\left(k^2-\frac{\ell(\ell+1)}{r^2}\right)R=0
$$

leads to the Bessel order $\nu=\ell+1/2$, the determinant

$$
F_{\ell+1/2,\rho}(k)
=
J_{\ell+1/2}(\rho k)Y_{\ell+1/2}(k)
-
Y_{\ell+1/2}(\rho k)J_{\ell+1/2}(k),
$$

and the multiplicity $2\ell+1$. A4 also correctly emphasized that no computation has been executed yet and that `COMP-certified-bessel` must remain `diagnostic_only`.

The source Strategy confirms that the shell route should proceed by Bessel cross-products, phase construction, a multiplicity-weighted lattice count, fixed-$\rho$ estimates, endpoint handling, and interval arithmetic for the compact low-energy range. It also confirms that certified numerics must use interval/ball arithmetic and produce verifiable finite-window checks rather than floating-point evidence.

## Rejected or risky ideas

Reject A3's proposed `blocked` status for `SHELL-lattice-count`. The problem is not blocked by a known contradiction; it is open and must be split into narrower obligations. The parent obligation remains `open`.

Reject A3's proposed `blocked` status for `ELLIPSE-near-circular`. The ellipse route is hard and source-audit dependent, but the project strategy keeps it as a parallel flagship preparation track, not a blocked route.

Reject A3's proposed `blocked` status for `CERT-certificate-family`. The certificate route is not ready for proof, but it remains a fallback route pending the Jiang-Lin source audit.

Reject exact floor equality without endpoint qualification. With strict counting, the exact channel count should be

$$
N_\ell(K)
=
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
$$

The floor

$$
\left\lfloor \frac{\Psi_{\ell+1/2,\rho}(K)}{\pi}\right\rfloor
$$

is a safe upper bound, but at spectral endpoints it is not the strict-count identity.

Reject the toy weighted fractional-part diagnostic

$$
\sum_\ell(2\ell+1)\{\sqrt{\Lambda-\ell(\ell+1)}\}
$$

as a proxy for the shell. It does not use the shell phase or the cross-product roots. Diagnostics must use the actual phase $\Psi_{\ell+1/2,\rho}(K)$, exact roots, or a stated WKB phase with explicit error. The uploaded review specifically warns against this proxy and recommends tracking the signed defect using the actual phase/count.

Reject raw interval evaluation of

$$
J_\nu(\rho k)Y_\nu(k)-Y_\nu(\rho k)J_\nu(k)
$$

as the only certified-computation route. It may be ill-conditioned in transition or evanescent regimes. A4 should test raw evaluation against phase-based, recurrence-based, scaled-Bessel, or spherical-Bessel algebraic evaluation.

Reject pure domain monotonicity or pure ball bracketing as a proof shortcut. The inequality

$$
N_D(A_{\rho,1},\Lambda)\le N_D(B_1,\Lambda)
$$

has the wrong volume constant, and the sharper bracketing idea

$$
N_D(A_{\rho,1},\Lambda)\le N_D(B_1,\Lambda)-N_D(B_\rho,\Lambda)
$$

would need a reverse Dirichlet Polya lower bound for the inner ball count, which is not available.

Reject a bare two-term Weyl argument as proof. The favorable negative boundary term is a guide, not a theorem-level certificate. Polya is a pointwise staircase inequality, and asymptotics without an explicit threshold and certified compact-window closure do not suffice. The strategy document explicitly states that asymptotics alone do not prove Polya and that the compact interval must be certified.

Reject A4's proposed patch detail `status: " diagnostic_only"` with a leading space. It would fail the allowed-status validator.

Reject overwriting `SHELL-cross-product-formula`'s `statement_tex` with audit prose. The mathematical statement should stay stable; audit conclusions belong in evidence and next actions.

## Known gaps

1. Source cards are incomplete. `SRC-bessel-phase` must record Nicholson's formula, phase/modulus conventions, Wronskian sign, validity ranges, Airy transition constants, and whether differenced phase bounds remain one-sided. `SRC-annuli` must record which floor-sum lemmas survive the $2\ell+1$ weight. `SRC-shell-weyl` must record whether shell Weyl or cross-product zero estimates are explicit and one-sided.

2. `SHELL-cross-product-formula` still lacks a complete internal proof. The algebra is correct, but the state should require the full spherical-harmonic decomposition, regular Sturm-Liouville completeness, positive/simple radial roots, no $k=0$ eigenvalue, and harmless handling of accidental degeneracies across $\ell$.

3. Phase branch normalization remains open. The project must define a continuous branch of $\theta_\nu$ so that $\Psi_{\nu,\rho}(0^+)=0$, $\Psi_{\nu,\rho}$ increases to infinity, and the first positive zero corresponds to the level $\pi$.

4. Nicholson monotonicity is not yet a legal proof dependency. It must be source-carded with exact hypotheses before `SHELL-phase-monotonicity` can move beyond `derived_under_assumptions`.

5. The inner-boundary transition $\rho k\sim\nu$ is the main new Bessel difficulty. It is not inherited from balls and cannot be assumed from annulus estimates without checking differencing losses.

6. The weighted lattice problem remains open. The project needs an explicit theorem that, given one-sided phase enclosures, bounds

$$
\sum_{\ell\ge0}(2\ell+1)\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}
$$

by the Weyl volume in the fixed-$\rho$ high-energy range.

7. Certified finite-window verification has no committed implementation. It must remain diagnostic until scripts, commands, root enclosures, counting tables, and limitations exist.

8. $\rho$-uniformity is deferred. Fixed-$\rho$ is the next theorem subtarget; compact $\rho$ intervals and the endpoint regimes $\rho\to0$ and $\rho\to1$ are separate obligations.

## New lemmas to add

1. `SHELL-sturm-liouville-completeness`: prove the rigorous separated spectral decomposition and show the Bessel cross-product zeros capture the radial spectrum in every angular channel.

2. `SHELL-exact-phase-rep`: define $M_\nu,\theta_\nu$ and record the exact phase factorization of $F_{\nu,\rho}$.

3. `SHELL-phase-monotonicity`: prove monotonicity of $\Psi_{\nu,\rho}$ assuming Nicholson monotonicity of $M_\nu^2$.

4. `SHELL-count-floor-identity`: record the strict-count phase formula using $n\pi<\Psi(K)$ and the floor upper bound with endpoint caveat.

5. `SHELL-inner-turning`: isolate one-sided Airy-scale control of $\theta_\nu(\rho k)$ and $\Psi_{\nu,\rho}(k)$ when $\rho k-\nu=O(\nu^{1/3})$.

6. `SHELL-weighted-lattice-fractional`: formulate the multiplicity-weighted discrete inequality given explicit one-sided phase bounds.

7. `SHELL-fixed-rho-high-energy`: isolate the analytic high-energy theorem for fixed $0<\rho<1$.

8. `SHELL-angular-cutoff`: prove by Rayleigh quotient that $\ell(\ell+1)\ge K^2$ implies no contribution below $K^2$.

9. `SHELL-spherical-bessel-algebraic`: explore the exact finite trigonometric-rational form of the half-integer cross-products for computation and possible low-order enclosures.

## Counterexample checks to run

1. Exact-root defect scan. For $\rho\in\{0.1,0.5,0.9\}$ and increasing $K$, compute

$$
D_\rho(K)
=
N_D(A_{\rho,1},K^2)
-
\frac{2}{9\pi}(1-\rho^3)K^3.
$$

This is diagnostic only. Record the worst $K$, dominant $\ell$ channels, and whether the maximum occurs near $\rho K\sim\ell+1/2$.

2. Inner-turning stress test. For large $\nu$, sample $k$ such that $\rho k-\nu=O(\nu^{1/3})$. Compare phase-difference estimates obtained by independent Bessel phases, spherical-Bessel algebraic form, and direct high-precision root computation.

3. Bracketing overshoot test. Compute

$$
N_D(B_1,K^2)-N_D(B_\rho,K^2)
-
\frac{2}{9\pi}(1-\rho^3)K^3
$$

for representative $\rho$. If positive frequently, the ball-difference route is not viable.

4. Thin-shell diagnostic. Let $\rho=1-h$ with $h$ small. Compare exact roots to the approximate product model

$$
\left(\frac{\pi n}{h}\right)^2+\ell(\ell+1).
$$

Record whether the signed defect worsens near radial band thresholds.

5. Small-hole diagnostic. Let $\rho=10^{-1},10^{-2},10^{-3}$. Compare shell roots to ball roots and track whether the volume loss

$$
\frac{2}{9\pi}\rho^3K^3
$$

is offset by eigenvalue shifts in the relevant $K$ range.

6. Computation-stability test. For $\rho=1/2$, compare root isolation using raw Bessel cross-products, phase representation, recurrence-scaled spherical Bessels, and the finite trigonometric-rational form for $\ell=0,1,2$ and then for a larger stress value such as $\ell=50$.

## Research strategy adjustment

Round 2 should not pivot. The shell route is stronger after Round 1 because the qualitative phase scaffold is now precise. The next round should be narrower than Round 1:

- A1 handles source-card discipline, especially Nicholson and annulus floor-sum statements.
- A2 handles phase structure and inner-turning quantitative formulation.
- A3 handles the weighted lattice theorem as a black-box problem, not broad route comparison.
- A4 handles rigorous spectral-formula completion and a minimal diagnostic root-isolation prototype.

Parallel tracks remain alive but secondary. Ellipses should stay in source-audit/preparation mode. Certificate families should stay as fallback pending the Jiang-Lin audit. The global strategy still supports a balanced portfolio: shell theorem first, certified Mathieu preparation second, certificate family third.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-sturm-liouville-completeness",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Sturm-Liouville completeness for separated shell spectrum",
        "status": "open",
        "statement_tex": "For A_{rho,1} in R^3, the Dirichlet Laplacian decomposes into spherical-harmonic angular momentum channels; in each ell channel the regular radial Sturm-Liouville problem on [rho,1] has positive simple radial eigenvalues exactly given by positive zeros of F_{ell+1/2,rho}(k), and accidental equality of eigenvalues across different ell is harmless because multiplicities are summed over the orthogonal direct-sum decomposition.",
        "dependencies": [
          "CONV-strict-counting"
        ],
        "implies": [
          "SHELL-cross-product-formula",
          "SHELL-count-floor-identity",
          "COMP-certified-bessel"
        ],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A4_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "owner": "A4",
        "next_action": "Write the full separation-of-variables and regular Sturm-Liouville proof, including no k=0 eigenvalue, positivity of roots, radial simplicity, and harmless cross-ell degeneracy."
      },
      {
        "id": "SHELL-exact-phase-rep",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Exact Bessel phase representation for shell cross-products",
        "status": "derived_under_assumptions",
        "statement_tex": "Given a continuous Bessel modulus-phase convention J_nu=M_nu cos(theta_nu), Y_nu=M_nu sin(theta_nu), with M_nu(z)>0 for z>0, the shell cross-product satisfies F_{nu,rho}(k)=M_nu(rho k) M_nu(k) sin(theta_nu(k)-theta_nu(rho k)); hence positive zeros are exactly phase-difference level points Psi_{nu,rho}(k) in pi Z.",
        "dependencies": [
          "SHELL-cross-product-formula",
          "SRC-bessel-phase"
        ],
        "implies": [
          "SHELL-phase-monotonicity",
          "SHELL-count-floor-identity",
          "SHELL-phase-enclosures"
        ],
        "blockers": [
          "SRC-bessel-phase"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "owner": "A2",
        "next_action": "Source-card the phase and modulus definitions, Wronskian sign convention, and positivity of M_nu before using this as a formal dependency."
      },
      {
        "id": "SHELL-phase-monotonicity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Global monotonicity of the shell phase difference",
        "status": "derived_under_assumptions",
        "statement_tex": "For nu>=1/2 and 0<rho<1, the phase difference Psi_{nu,rho}(k)=theta_nu(k)-theta_nu(rho k) is strictly increasing on k>0, assuming Nicholson monotonicity of M_nu(z)^2=J_nu(z)^2+Y_nu(z)^2 and the phase derivative theta_nu'(z)=2/(pi z M_nu(z)^2).",
        "dependencies": [
          "SHELL-exact-phase-rep",
          "SRC-bessel-phase"
        ],
        "implies": [
          "SHELL-count-floor-identity",
          "SHELL-phase-enclosures"
        ],
        "blockers": [
          "SRC-bessel-phase"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "owner": "A2",
        "next_action": "Audit Nicholson's formula, validity range in nu and z, differentiation under the integral, K0 monotonicity, and the sign convention for theta_nu'."
      },
      {
        "id": "SHELL-count-floor-identity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Strict phase-count identity for shell eigenvalues",
        "status": "derived_under_assumptions",
        "statement_tex": "With strict counting and K=sqrt(Lambda), N_D(A_{rho,1},K^2)=sum_{ell>=0}(2ell+1) #{n>=1: n pi < Psi_{ell+1/2,rho}(K)}. The floor expression floor(Psi_{ell+1/2,rho}(K)/pi) is an upper bound but is not exact at spectral endpoints.",
        "dependencies": [
          "CONV-strict-counting",
          "SHELL-cross-product-formula",
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity"
        ],
        "implies": [
          "SHELL-lattice-count",
          "SHELL-weighted-lattice-fractional",
          "SHELL-fixed-rho-high-energy"
        ],
        "blockers": [
          "SHELL-cross-product-formula",
          "SRC-bessel-phase"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "owner": "A2",
        "next_action": "Verify phase branch normalization, Psi_{nu,rho}(0+)=0, Psi_{nu,rho}(k)->infinity, and strict endpoint handling n pi < Psi(K)."
      },
      {
        "id": "SHELL-inner-turning",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Inner-boundary turning regime for shell phase differences",
        "status": "open",
        "statement_tex": "For fixed 0<rho<1, construct explicit one-sided control of theta_nu(rho k) and Psi_{nu,rho}(k) when rho k lies within the Airy scale of nu, for example rho k-nu=O(nu^{1/3}), with constants and error direction strong enough for the shell counting upper bound.",
        "dependencies": [
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity",
          "SRC-bessel-phase",
          "SRC-shell-weyl"
        ],
        "implies": [
          "SHELL-phase-enclosures",
          "SHELL-fixed-rho-high-energy"
        ],
        "blockers": [
          "SRC-bessel-phase",
          "SRC-shell-weyl"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A3_stageA.md"
          ]
        },
        "owner": "A2",
        "next_action": "Formulate the Airy-scale statement precisely and test whether FLPS single-Bessel Airy bounds survive subtraction in theta_nu(k)-theta_nu(rho k)."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Multiplicity-weighted lattice bound for the 3D shell phase count",
        "status": "open",
        "statement_tex": "Given explicit one-sided phase bounds for Psi_{ell+1/2,rho}(K), prove the 2ell+1 weighted floor or phase-sum estimate needed to bound the fixed-rho high-energy shell count by (2/(9pi))(1-rho^3)K^3.",
        "dependencies": [
          "SHELL-count-floor-identity",
          "SHELL-phase-enclosures",
          "SRC-annuli"
        ],
        "implies": [
          "SHELL-lattice-count",
          "SHELL-fixed-rho-high-energy"
        ],
        "blockers": [
          "SHELL-phase-enclosures",
          "SRC-annuli"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A3_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "owner": "A3",
        "next_action": "Audit annulus floor-sum hypotheses, distinguish radial floor lemmas from angular multiplicity lemmas, and formulate the exact weighted inequality with explicit phase-error allowances."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Fixed-rho high-energy shell Polya estimate",
        "status": "open",
        "statement_tex": "For each fixed 0<rho<1, prove an explicit K_0(rho) such that N_D(A_{rho,1},K^2) <= (2/(9pi))(1-rho^3)K^3 for all K>=K_0(rho), using the strict phase-count identity, one-sided shell phase enclosures, and the multiplicity-weighted lattice estimate.",
        "dependencies": [
          "SHELL-count-floor-identity",
          "SHELL-phase-enclosures",
          "SHELL-lattice-count",
          "SHELL-weighted-lattice-fractional"
        ],
        "implies": [
          "TARGET-shell-d3",
          "COMP-certified-bessel"
        ],
        "blockers": [
          "SHELL-inner-turning",
          "SHELL-phase-enclosures",
          "SHELL-weighted-lattice-fractional"
        ],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A1_stageA.md",
            "rounds/round1/A2_stageA.md"
          ]
        },
        "owner": "A2",
        "next_action": "State the first black-box fixed-rho theorem with exact phase hypotheses, lattice hypotheses, and a computable analytic threshold K_0(rho)."
      },
      {
        "id": "SHELL-angular-cutoff",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Angular momentum cutoff below a fixed energy",
        "status": "proved_internal",
        "statement_tex": "In dimension 3, angular momentum ell contributes no Dirichlet eigenvalue below K^2 on A_{rho,1} if ell(ell+1)>=K^2. Hence finite verification below K_0^2 only needs ell satisfying ell(ell+1)<K_0^2.",
        "dependencies": [
          "SHELL-sturm-liouville-completeness"
        ],
        "implies": [
          "COMP-certified-bessel"
        ],
        "blockers": [],
        "evidence": {
          "positive": [
            "rounds/round1/A1_stageA.md",
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A4_stageA.md"
          ],
          "negative": [],
          "inconclusive": []
        },
        "owner": "A4",
        "next_action": "Use this cutoff in the certified-computation smoke test and record slack versus actual first roots."
      },
      {
        "id": "SHELL-spherical-bessel-algebraic",
        "type": "lemma",
        "track": "certified_computation",
        "title": "Finite trigonometric form of half-integer shell cross-products",
        "status": "proposed",
        "statement_tex": "For integer ell in d=3, express the spherical-Bessel shell cross-product as P_ell(k,rho) sin((1-rho)k)+Q_ell(k,rho) cos((1-rho)k), with rational functions or finite polynomials in k and rho, and assess whether this form improves certified root isolation.",
        "dependencies": [
          "SHELL-cross-product-formula"
        ],
        "implies": [
          "COMP-certified-bessel",
          "SHELL-phase-enclosures"
        ],
        "blockers": [],
        "evidence": {
          "positive": [],
          "negative": [],
          "inconclusive": [
            "rounds/round1/A3_stageA.md",
            "rounds/round1/A4_stageA.md"
          ]
        },
        "owner": "A4",
        "next_action": "Derive ell=0,1,2 explicitly; check whether only sin((1-rho)k) and cos((1-rho)k) remain after cancellation; estimate coefficient growth and conditioning."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "status": "proved_internal",
        "statement_tex": "Use N_D(Omega,Lambda)=#{j: lambda_j^D(Omega)<Lambda}. Under this strict convention, N_D(Omega,Lambda)<=C Lambda^{d/2} for all Lambda>=0 is equivalent to lambda_j^D(Omega)>=(j/C)^{2/d} for all j>=1, with eigenvalues repeated according to multiplicity.",
        "evidence_added": {
          "positive": [
            "rounds/round1/A1_stageA.md",
            "rounds/round1/A1_stageB.md"
          ]
        },
        "next_action": "Use this endpoint rule in all imported source statements, phase-count identities, eigenvalue formulations, and certified finite-window checks."
      },
      {
        "id": "TARGET-shell-d3",
        "status": "open",
        "statement_tex": "For A_{rho,1}={x in R^3: rho<|x|<1}, 0<rho<1, prove N_D(A_{rho,1},Lambda) <= (2/(9pi))(1-rho^3)Lambda^{3/2} for all Lambda>=0 using strict counting; equivalently, with K=sqrt(Lambda), prove N_D(A_{rho,1},K^2) <= (2/(9pi))(1-rho^3)K^3 for all K>=0.",
        "dependencies_added": [
          "SHELL-fixed-rho-high-energy"
        ],
        "blockers_added": [
          "SHELL-fixed-rho-high-energy"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/round1/judge_synthesis.md"
          ]
        },
        "next_action": "Keep the theorem open. First prove the fixed-rho high-energy estimate and a certified finite window; defer compact rho-uniformity and endpoint regimes."
      },
      {
        "id": "SHELL-cross-product-formula",
        "status": "open",
        "dependencies_added": [
          "SHELL-sturm-liouville-completeness"
        ],
        "blockers_added": [
          "SHELL-sturm-liouville-completeness"
        ],
        "evidence_added": {
          "positive": [
            "rounds/round1/A2_stageA.md",
            "rounds/round1/A3_stageA.md",
            "rounds/round1/A4_stageA.md"
          ]
        },
        "next_action": "Complete the Sturm-Liouville and spherical-harmonic proof; do not require absence of accidental equality across ell, only correct multiplicity summation."
      },
      {
        "id": "SRC-bessel-phase",
        "status": "source_audit_required",
        "next_action": "Audit Bessel phase definitions, modulus positivity, Wronskian sign, theta_nu'=2/(pi z M_nu^2), Nicholson's formula and strict decrease of M_nu^2, validity for nu>=1/2 and z>0, Airy transition constants, and whether independent phase bounds can be safely differenced for shell cross-products."
      },
      {
        "id": "SRC-annuli",
        "status": "source_audit_required",
        "next_action": "Extract the annulus cross-product setup, phase estimates, trapezoidal and convex/concave floor-sum lemmas, finite verification method, and identify exactly which estimates are dimension-independent and which rely on planar multiplicities."
      },
      {
        "id": "SRC-shell-weyl",
        "status": "source_audit_required",
        "next_action": "Audit shell-specific Bessel cross-product zero counts, Weyl-remainder bounds, dimension and boundary-condition assumptions, and whether any estimates are one-sided and explicit enough for Polya."
      },
      {
        "id": "SRC-FLPS-balls",
        "status": "source_audit_required",
        "next_action": "Create the source card for FLPS balls/disks/sectors: theorem statements, boundary conditions, counting convention, Bessel phase definitions, lattice-counting lemmas, and computer-assisted components to reproduce before shell transfer."
      },
      {
        "id": "SHELL-phase-enclosures",
        "status": "open",
        "dependencies_added": [
          "SHELL-exact-phase-rep",
          "SHELL-phase-monotonicity",
          "SHELL-inner-turning"
        ],
        "blockers_added": [
          "SHELL-inner-turning"
        ],
        "next_action": "For fixed rho, formulate quantitative one-sided enclosures for Psi_{nu,rho}(k) in oscillatory, outer-turning, inner-turning, mixed evanescent/oscillatory, and fully evanescent regimes; explicitly track differencing loss."
      },
      {
        "id": "SHELL-lattice-count",
        "status": "open",
        "dependencies_added": [
          "SHELL-count-floor-identity",
          "SHELL-weighted-lattice-fractional"
        ],
        "blockers_added": [
          "SHELL-weighted-lattice-fractional"
        ],
        "next_action": "Replace the broad lattice target with a precise black-box theorem: assuming explicit one-sided phase bounds, prove the 2ell+1 weighted count is below (2/(9pi))(1-rho^3)K^3 in the fixed-rho high-energy range."
      },
      {
        "id": "COMP-certified-bessel",
        "status": " diagnostic_only",
        "dependencies_added": [
          "SHELL-angular-cutoff",
          "SHELL-spherical-bessel-algebraic"
        ],
        "required_output": [
          "script",
          "exact command",
          "root-enclosure report",
          "counting verification table",
          "limitations"
        ],
        "evidence_added": {
          "inconclusive": [
            "rounds/round1/A4_stageA.md"
          ]
        },
        "next_action": "Implement a minimal diagnostic root-isolation prototype for rho=1/2, ell=0,1,2, 0<k<20. Compare raw Bessel interval evaluation against phase-based, recurrence-based, scaled, or spherical-Bessel algebraic evaluation. Treat all output as diagnostic."
      },
      {
        "id": "SHELL-rho-uniformity",
        "status": "open",
        "next_action": "Keep rho-uniformity deferred. After fixed-rho high-energy and finite-window methods are formulated, separately plan compact rho intervals, rho->0 small-hole behavior, and rho->1 thin-shell behavior."
      },
      {
        "id": "ELLIPSE-near-circular",
        "status": "open",
        "next_action": "Keep as a parallel flagship track. Do not mark blocked. Next useful action is source-auditing Mathieu characteristic values, small-eccentricity perturbation, and certified eigenvalue enclosures after the shell Round 2 core tasks are assigned."
      },
      {
        "id": "CERT-certificate-family",
        "status": "open",
        "next_action": "Keep as a fallback route. Do not mark blocked. First complete SRC-jiang-lin before proposing a concrete family or exact certificate theorem."
      }
    ],
    "reject": [
      {
        "id": "A3-proposed-blocked-statuses",
        "reason": "Reject marking SHELL-lattice-count, ELLIPSE-near-circular, or CERT-certificate-family as blocked. The correct status is open/source-audit-dependent, not blocked by a proved obstruction."
      },
      {
        "id": "toy-weighted-fractional-test",
        "reason": "Reject the proxy sum using sqrt(Lambda-ell(ell+1)) as a proof-relevant diagnostic. It does not use the shell phase, actual roots, or a stated WKB phase with explicit error."
      },
      {
        "id": "raw-floating-point-computation-as-proof",
        "reason": "Reject any use of floating-point root tables as proof. Computation remains diagnostic until certified interval or ball arithmetic outputs all required artifacts."
      },
      {
        "id": "bare-two-term-weyl-proof",
        "reason": "Reject a bare two-term Weyl threshold argument without explicit one-sided constants and certified compact-window closure."
      }
    ],
    "no_change": [
      {
        "id": "POLYA-program-target",
        "reason": "No theorem-level program claim is proved or promoted."
      },
      {
        "id": "FLPS-disk-ball-reproduction",
        "reason": "Still blocked by source-card audits; remains infrastructure."
      },
      {
        "id": "SRC-mathieu-ellipse",
        "reason": "Still source-audit-required for the parallel ellipse track."
      },
      {
        "id": "SRC-jiang-lin",
        "reason": "Still source-audit-required before certificate-family work can be used as a dependency."
      }
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 7,
    "idea_quality_score": 8,
    "state_evidence_score": 6,
    "calibration_score": 8,
    "reason": "Round 1 produced no theorem proof, but it sharpened the target, fixed the convention, audited the spectral formula, identified a strong phase scaffold, isolated the inner-turning and weighted-lattice blockers, and preserved computation as diagnostic only."
  }
}

## Next-round prompts by agent

### For A1

Build the Round 2 source-card foundation. Prioritize `SRC-bessel-phase`, `SRC-annuli`, `SRC-shell-weyl`, and `SRC-FLPS-balls`.

For `SRC-bessel-phase`, record exact statements for the Bessel phase/modulus convention, Wronskian sign, $\theta_\nu'(z)=2/(\pi zM_\nu(z)^2)$, Nicholson's formula, strict decrease of $M_\nu(z)^2=J_\nu(z)^2+Y_\nu(z)^2$, validity ranges in $\nu$ and $z$, and Airy transition enclosures. State whether the paper's individual phase bounds can be differenced in the shell cross-product without losing the needed one-sided direction.

For `SRC-annuli`, extract the annulus theorem, counting convention, cross-product setup, phase estimates, trapezoidal/floor-sum lemmas, finite verification strategy, and exactly which lemmas rely on planar multiplicity rather than a $2\ell+1$ weight.

For `SRC-shell-weyl`, record the shell cross-product zero-counting and Weyl-remainder statements, including explicitness, one-sidedness, boundary conditions, and dimension range.

Do not claim any shell, ellipse, or certificate-family theorem.

### For A2

Formalize the shell phase scaffold. Write a lemma package for:

1. `SHELL-exact-phase-rep`;
2. `SHELL-phase-monotonicity` conditional on Nicholson;
3. `SHELL-count-floor-identity` with strict endpoint rule;
4. `SHELL-inner-turning`.

For the phase-count identity, do not state equality with the floor at endpoints. Use

$$
\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}.
$$

For `SHELL-inner-turning`, state a precise Airy-scale proposition for $\rho k-\nu=O(\nu^{1/3})$ and identify exactly which constants and one-sided errors must be inherited or rebuilt from the Bessel phase source card. End with a fixed-$\rho$ high-energy proposition template that separates phase hypotheses from lattice hypotheses.

Do not claim the high-energy Polya estimate yet.

### For A3

Attack `SHELL-weighted-lattice-fractional` and refine `SHELL-lattice-count`.

Assume a black-box phase-count formula and explicit one-sided bounds for $\Psi_{\ell+1/2,\rho}(K)$. Formulate the exact weighted discrete inequality needed to prove

$$
\sum_{\ell\ge0}(2\ell+1)\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}
\le
\frac{2}{9\pi}(1-\rho^3)K^3
$$

for fixed $\rho$ and large $K$.

Audit which annulus floor-sum lemmas transfer and which fail because of the weight $2\ell+1$. Compare two possible high-energy mechanisms: fractional-part lower bounds versus a floor-free phase-sum bound with an explicit negative boundary margin. Reject toy diagnostics that do not use the shell phase.

Reserve a short section for whether the ellipse or certificate tracks should receive any Round 3 attention, but keep the shell lattice problem primary.

### For A4

Complete the formula/computation audit in executable form.

First, write the proof skeleton for `SHELL-sturm-liouville-completeness`: spherical-harmonic decomposition, radial regular Sturm-Liouville problem on $[\rho,1]$, determinant zeros, positive roots, no $k=0$ eigenvalue, radial simplicity, and harmless cross-$\ell$ degeneracy.

Second, implement a diagnostic root-isolation prototype for $\rho=1/2$, $\ell=0,1,2$, and $0<k<20$. Compare raw Bessel interval evaluation with at least one stabilized method: phase representation, recurrence-scaled spherical Bessel evaluation, or the finite trigonometric-rational form. Output a script path, exact command, root intervals if available, counting table if available, and limitations.

Third, derive the spherical-Bessel algebraic form for $\ell=0,1,2$ and assess coefficient growth and conditioning. Treat all computation as diagnostic unless root-exclusion and root-isolation certificates are rigorous.

## Round Assessment

Round 1 succeeded as a target-formation and blocker-isolation round. It did not prove any Polya theorem and did not justify promoting `TARGET-shell-d3`. It did establish a more coherent shell route:

- the theorem target is now explicit and normalized;
- strict counting is fixed;
- the shell spectral formula has strong audit support but still needs completeness proof;
- the exact phase representation is the most valuable new structural scaffold;
- Nicholson monotonicity is the key source-card item for phase monotonicity;
- the inner turning point and the $2\ell+1$ weighted lattice count are the two central analytic blockers;
- certified computation requirements are clear and remain diagnostic.

The correct next move is not to broaden the search. It is to formalize the phase scaffold and attack the weighted lattice problem under black-box phase hypotheses while A1 closes source-card gaps and A4 starts a minimal diagnostic computation.

## Confidence

High confidence: strict target normalization, Weyl constant, shell volume, endpoint convention, and the need for source-card discipline.

High confidence: the cross-product formula is algebraically correct, pending a formal Sturm-Liouville completeness proof.

Medium-high confidence: the exact phase representation is correct once phase/modulus conventions are recorded.

Medium confidence: Nicholson monotonicity will prove global shell phase monotonicity, but it remains an external dependency until source-carded.

Medium-low confidence: the weighted lattice estimate can be proved with existing annulus methods; new discrete estimates are likely needed.

Low confidence: endpoint uniformity in $\rho$ and any full theorem-level shell Polya claim at this stage.

No Dirichlet Polya theorem for shells, ellipses, or a certificate family is claimed.
