## Selected main route

Continue the **3D spherical shell** as the primary first-theorem route, reorganized around the two-layer decomposition that emerged from Round 1. No pivot; no theorem promotion. Human steering (shell primary, no Round-1 proof claim, repo as durable memory) is respected; no new human intervention appeared between stages.

- **Layer 1 (qualitative structure -- now provable).** All four agents independently derived and cross-checked the spectral formula, and A2 supplied the decisive structural result: the exact phase factorization
$$
F_{\nu,\rho}(k)=M_\nu(\rho k)\,M_\nu(k)\,\sin\!\big(\theta_\nu(k)-\theta_\nu(\rho k)\big),\qquad M_\nu=\sqrt{J_\nu^2+Y_\nu^2}>0,
$$
together with global strict monotonicity of $\Psi_{\nu,\rho}(k)=\theta_\nu(k)-\theta_\nu(\rho k)$ via
$$
\Psi_{\nu,\rho}'(k)=\frac{2}{\pi k}\Big(\tfrac{1}{M_\nu(k)^2}-\tfrac{1}{M_\nu(\rho k)^2}\Big)>0,
$$
using strict decrease of $M_\nu^2$ (Nicholson). This yields the exact strict-count identity
$$
N_D(A_{\rho,1},K^2)=\sum_{\ell\ge0}(2\ell+1)\,\#\{n\ge1:\ n\pi<\Psi_{\ell+1/2,\rho}(K)\}
$$
in **all** spectral regimes, with no Airy analysis needed for existence/indexing. The target constant is confirmed by three independent computations: $L_3|A_{\rho,1}|=\tfrac{2}{9\pi}(1-\rho^3)$.

- **Layer 2 (quantitative -- the two hard blockers, now isolated).** (i) `SHELL-inner-turning`: one-sided control of $\Psi_{\nu,\rho}$ when $\rho k-\nu=O(\nu^{1/3})$, robust under phase differencing. (ii) `SHELL-weighted-lattice-fractional`: the genuinely 2-parameter, $2\ell+1$-weighted floor-sum bound; annulus floor-sum lemmas are 1D in the angular index and do not transfer.

Ellipse and certificate-family tracks remain **open / source-audit**, not blocked.

## Useful fragments by source

- **A2 (Stage A + B):** exact phase factorization; Nicholson monotonicity of $\Psi$; exact strict-count floor identity; a priori angular cutoff via weighted Rayleigh quotient; the observation that $\nu=\ell+\tfrac12$ makes the $\ell$-sum a **midpoint quadrature** (killing the first-order Euler--Maclaurin term); the floor-free high-energy mechanism $T(K)=\sum(2\ell+1)\Psi/\pi\le$ Weyl via the negative Dirichlet boundary term $-\tfrac{1+\rho^2}{4}K^2$; and a diagnostic exact-root defect scan at $\rho=0.5$ whose defect tracks $-\tfrac{1+\rho^2}{4}\Lambda$. Symbolic verification of A3's algebraic form for $\ell\le2$.
- **A1 (Stage A + B):** the strict-counting/eigenvalue equivalence ($N_D\le C\Lambda^{d/2}\ \forall\Lambda\iff\lambda_j\ge(j/C)^{2/d}\ \forall j$); the correct endpoint discipline (exact count uses $n\pi<\Psi$, floor is only an upper bound); sharpened target constant; source-audit prioritization; and the correction that "no accidental cross-$\ell$ degeneracy" must not be required (counting holds because multiplicities add).
- **A3 (Stage A + B):** the $d=3$ **spherical-Bessel elementary form** $F_{\ell+1/2,\rho}(k)=P_\ell\sin((1-\rho)k)+Q_\ell\cos((1-\rho)k)$ (verified $\ell\le2$; $\ell=0$ gives $\sin((1-\rho)k)/(\rho k^2)$) -- a real asset for certified computation; and the sharp risk isolation of the $2\ell+1$ weighted lattice sum as a distinct 2D obligation.
- **A4 (Stage A + B):** rigorous formula/multiplicity/strict-count audit reproduced independently; the **Sturm--Liouville completeness** requirement (no eigenvalue missed by separation); a concrete, appropriately-scoped certified-computation first target with exemplary "not executed" discipline.

## Rejected or risky ideas

- **A3's `blocked` statuses** on `SHELL-lattice-count`, `ELLIPSE-near-circular`, `CERT-certificate-family`: rejected. No impossibility was demonstrated; each has an active next action. Blocking would halt useful parallel work.
- **A3's toy diagnostic** $\sum(2\ell+1)\{\sqrt{\Lambda-\ell(\ell+1)}\}$: rejected as a validity proxy -- it drops $\rho$, is not the shell phase, and a fractional-part sum cannot go "deeply negative." Replace with the exact-root (or specified-WKB) signed-defect scan.
- **A3's capacity route** ($4\pi\rho/(1-\rho)$ is a condenser capacity, not the Newtonian capacity needed for eigenvalue bounds) and **trace-formula route** (produces oscillatory, not one-sided, corrections): retained only as low-priority escape hatches.
- **A4's patch defects**: the malformed status `" diagnostic_only"` (leading space; would fail the validator) and the overwrite of `SHELL-cross-product-formula`'s `statement_tex` with an audit note -- both rejected; the audit note belongs in `evidence`/`next_action`.
- **Naive interval evaluation** of the raw cross-product: risky (catastrophic cancellation at large $\ell$). Certified computation must use the phase/modulus form or the elementary spherical-Bessel form.
- **Two-term Weyl heuristic as a standalone argument**: risky because the shell has a positive-measure family of periodic billiards; recorded only as "two-term Weyl insufficient; exact phase/lattice route primary," not as negative evidence against the theorem.

## Known gaps

1. **Inner-turning quantitative enclosure** (`SHELL-inner-turning`): whether FLPS single-Bessel Airy/Olver phase bounds survive subtraction at $\rho k\approx\nu$, one-sided and explicit. Central special-function blocker.
2. **2D weighted lattice bound** (`SHELL-weighted-lattice-fractional`): the $2\ell+1$ weight makes this a 2-parameter count; annulus 1D-angular floor sums do not transfer.
3. **Phase branch normalization**: prove $\Psi_{\nu,\rho}(0^+)=0$ and that the first zero corresponds to level $\pi$ (off-by-one risk shifts every angular channel).
4. **Sturm--Liouville completeness** for `SHELL-cross-product-formula` (all $L^2$ modes captured; radial simplicity; positivity of roots; multiplicity $2\ell+1$) -- without requiring absence of accidental cross-$\ell$ degeneracy.
5. **Nicholson source card** in `SRC-bessel-phase` (validity range, differentiation-under-integral justification, Wronskian/phase sign) -- blocks promoting `SHELL-phase-monotonicity` to `proved_internal`.
6. **Explicit high-energy enclosure** (`SHELL-fixed-rho-high-energy`): make the phase-shift-to-boundary-term identity quantitative and one-sided, and control the $\ell$-sum (midpoint-quadrature advantage) so $T(K)\le$ Weyl for $K\ge K_0(\rho)$.

## New lemmas to add

- `SHELL-exact-phase-rep` (derived_under_assumptions): the exact factorization and $\Psi\in\pi\mathbb Z$ zero condition.
- `SHELL-phase-monotonicity` (derived_under_assumptions): $\Psi_{\nu,\rho}'>0$ via Nicholson; consequently $\Psi(0^+)=0$, $\Psi\to\infty$.
- `SHELL-count-floor-identity` (derived_under_assumptions): exact strict count $\sum(2\ell+1)\#\{n\ge1:n\pi<\Psi\}$, with floor only as an upper bound.
- `SHELL-angular-cutoff` (proved_internal): $\ell(\ell+1)\ge K^2\Rightarrow$ no contribution; weighted-Rayleigh proof recorded below.
- `SHELL-inner-turning` (open): the inner-transition one-sided phase control.
- `SHELL-fixed-rho-high-energy` (open): the fixed-$\rho$ high-energy counting bound with explicit threshold.
- `SHELL-weighted-lattice-fractional` (open): the 2D weighted floor-sum inequality (owner A3).
- `SHELL-spherical-bessel-algebraic` (open; $\ell\le2$ verified): the elementary $P_\ell\sin+Q_\ell\cos$ form (owner A4).

Recorded proof of `SHELL-angular-cutoff`: for $R\in H^1_0((\rho,1),r^2dr)$, $\frac{\int_\rho^1[(R')^2+\ell(\ell+1)r^{-2}R^2]r^2dr}{\int_\rho^1 R^2 r^2dr}>\ell(\ell+1)\frac{\int R^2dr}{\int R^2r^2dr}\ge\ell(\ell+1)$ since $r^2\le1$ and the kinetic term is positive; hence the lowest radial eigenvalue exceeds $\ell(\ell+1)$.

## Counterexample checks to run

1. **Exact-root signed-defect scan** $D_\rho(K)=\sum(2\ell+1)\#\{n\ge1:n\pi<\Psi_{\ell+1/2,\rho}(K)\}-\tfrac{2}{9\pi}(1-\rho^3)K^3$ for $\rho\in\{0.1,0.5,0.9\}$ over growing $K$ (A2 confirmed $\rho=0.5$: defect stays negative, $\approx-\tfrac{1+\rho^2}{4}\Lambda$). Watch whether the worst defect drifts into the inner-transition band $\rho K\approx\ell+\tfrac12$ or the thin-shell regime.
2. **Interval-arithmetic stability** at high order (e.g. $F_{50.5,0.5}$ near its first root): compare naive cross-product vs phase/elementary evaluation; confirm the latter avoids width explosion (rebuts the cancellation blocker).
3. **Weighted floor-sum vs Weyl** using the *actual* phase (not the toy proxy), to stress-test the 2D lattice obligation before investing in the enclosure.

## Research strategy adjustment

Split the shell route into small, separately-verifiable obligations. Layer 1 is promoted to a tracked scaffold (mostly `derived_under_assumptions`, pending the Nicholson and completeness cards). Layer 2 is attacked on two independent fronts: A2 on the inner-turning enclosure, A3 on the abstract 2D weighted lattice inequality (black-box phase, minimal error hypotheses). A4 discharges completeness and builds a diagnostic (non-proof) interval-arithmetic prototype using the phase/elementary form. A1 builds the source cards, Nicholson first. Defer $\rho$-uniformity and endpoint limits; defer full certified finite-window closure until the high-energy bound and the cancellation behavior are understood. Ellipse/certificate stay parallel and open.

## State Patch

{
  "proof_obligations": {
    "create": [
      {
        "id": "SHELL-exact-phase-rep",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Exact Bessel cross-product phase factorization",
        "status": "derived_under_assumptions",
        "statement_tex": "For a fixed Bessel phase/modulus convention J_nu=M_nu cos(theta_nu), Y_nu=M_nu sin(theta_nu), M_nu(z)=sqrt(J_nu(z)^2+Y_nu(z)^2)>0 for z>0, one has F_{nu,rho}(k)=M_nu(rho k) M_nu(k) sin(theta_nu(k)-theta_nu(rho k)). Hence positive zeros of F_{nu,rho} occur exactly when Psi_{nu,rho}(k):=theta_nu(k)-theta_nu(rho k) is in pi*Z.",
        "dependencies": ["SHELL-cross-product-formula", "SRC-bessel-phase"],
        "implies": ["SHELL-count-floor-identity", "SHELL-phase-monotonicity"],
        "blockers": ["SRC-bessel-phase"],
        "evidence": {"positive": ["rounds/polya-main/round1/A2_stageA.md", "rounds/polya-main/round1/A2_stageB.md"], "negative": [], "inconclusive": []},
        "owner": "A2",
        "next_action": "Source-card the phase/modulus definitions and Wronskian sign convention; then promote to proved_internal."
      },
      {
        "id": "SHELL-phase-monotonicity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Global strict monotonicity of the shell phase difference",
        "status": "derived_under_assumptions",
        "statement_tex": "For nu>=1/2 and 0<rho<1, Psi_{nu,rho} is strictly increasing on (0,infty): Psi'_{nu,rho}(k)=(2/(pi k))(1/M_nu(k)^2 - 1/M_nu(rho k)^2)>0, using strict decrease of z|->M_nu(z)^2=J_nu(z)^2+Y_nu(z)^2 (Nicholson). Consequently Psi_{nu,rho}(0+)=0 and Psi_{nu,rho}(k)->infty as k->infty.",
        "dependencies": ["SHELL-exact-phase-rep", "SRC-bessel-phase"],
        "implies": ["SHELL-count-floor-identity"],
        "blockers": ["SRC-bessel-phase"],
        "evidence": {"positive": ["rounds/polya-main/round1/A2_stageA.md"], "negative": [], "inconclusive": ["rounds/polya-main/round1/A2_stageB.md"]},
        "owner": "A2",
        "next_action": "Card Nicholson's integral (validity nu>=0, z>0; differentiation under the integral; sign), prove the branch normalization Psi(0+)=0; then promote to proved_internal."
      },
      {
        "id": "SHELL-count-floor-identity",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Exact strict-count identity for the shell",
        "status": "derived_under_assumptions",
        "statement_tex": "With strict counting, N_D(A_{rho,1},K^2)=sum_{ell>=0}(2ell+1) #{n>=1 : n*pi < Psi_{ell+1/2,rho}(K)}. In particular N_D(A_{rho,1},K^2) <= sum_{ell>=0}(2ell+1) floor(Psi_{ell+1/2,rho}(K)/pi). Do not assert floor equality at eigenvalue endpoints.",
        "dependencies": ["SHELL-cross-product-formula", "SHELL-exact-phase-rep", "SHELL-phase-monotonicity", "CONV-strict-counting"],
        "implies": ["TARGET-shell-d3"],
        "blockers": ["SHELL-phase-monotonicity"],
        "evidence": {"positive": ["rounds/polya-main/round1/A2_stageA.md"], "negative": [], "inconclusive": []},
        "owner": "A2",
        "next_action": "After monotonicity and completeness are promoted, upgrade; keep the endpoint rule n*pi<Psi(K) rather than a floor equality."
      },
      {
        "id": "SHELL-angular-cutoff",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "A priori angular-momentum cutoff",
        "status": "proved_internal",
        "statement_tex": "For d=3, angular momentum ell contributes no Dirichlet eigenvalue below K^2 whenever ell(ell+1)>=K^2; equivalently the ell-sum is finite with ell < (-1+sqrt(1+4K^2))/2. Proof: the radial Rayleigh quotient on (rho,1) with weight r^2 dr exceeds ell(ell+1), since ell(ell+1)/r^2 >= ell(ell+1) for r<=1 and the kinetic term is positive.",
        "dependencies": ["CONV-strict-counting"],
        "implies": [],
        "blockers": [],
        "evidence": {"positive": ["rounds/polya-main/round1/A2_stageA.md", "rounds/polya-main/round1/A1_stageA.md", "rounds/polya-main/round1/A4_stageA.md"], "negative": [], "inconclusive": []},
        "owner": "A2",
        "next_action": "Record the one-paragraph Rayleigh-quotient proof in state/lemma_bank.md."
      },
      {
        "id": "SHELL-inner-turning",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Inner turning-point one-sided phase control",
        "status": "open",
        "statement_tex": "Establish explicit one-sided control of theta_nu(rho k) and of Psi_{nu,rho}(k)=theta_nu(k)-theta_nu(rho k) in the inner turning regime rho*k - nu = O(nu^{1/3}), robust under phase differencing, with computable error.",
        "dependencies": ["SHELL-phase-enclosures", "SRC-bessel-phase", "SRC-shell-weyl"],
        "implies": ["SHELL-fixed-rho-high-energy"],
        "blockers": ["SRC-bessel-phase", "SRC-shell-weyl"],
        "evidence": {"positive": [], "negative": [], "inconclusive": ["rounds/polya-main/round1/A2_stageA.md"]},
        "owner": "A2",
        "next_action": "Test whether FLPS single-Bessel Airy/Olver phase enclosures survive subtraction at rho*k~nu; produce a one-sided bound with explicit constants."
      },
      {
        "id": "SHELL-fixed-rho-high-energy",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Fixed-rho high-energy counting bound",
        "status": "open",
        "statement_tex": "For each fixed 0<rho<1, exhibit an explicit threshold K_0(rho) and a one-sided phase enclosure such that sum_{ell>=0}(2ell+1) floor(Psi_{ell+1/2,rho}(K)/pi) <= (2/(9pi))(1-rho^3)K^3 for all K>=K_0(rho). Primary mechanism: the floor-free sum T(K)=sum(2ell+1)Psi/pi satisfies T(K) <= Weyl via the negative Dirichlet boundary term -(1+rho^2)/4 * K^2; the half-integer orders nu=ell+1/2 make the ell-sum a midpoint quadrature, removing the first-order Euler-Maclaurin term.",
        "dependencies": ["SHELL-count-floor-identity", "SHELL-phase-enclosures", "SHELL-inner-turning", "SHELL-weighted-lattice-fractional", "SRC-annuli"],
        "implies": ["TARGET-shell-d3"],
        "blockers": ["SHELL-phase-enclosures", "SHELL-weighted-lattice-fractional"],
        "evidence": {"positive": [], "negative": [], "inconclusive": ["rounds/polya-main/round1/A2_stageB.md"]},
        "owner": "A2",
        "next_action": "Make the phase-shift-to-boundary-term identity quantitative and one-sided; control the ell-sum via the midpoint-quadrature bound; determine K_0(rho)."
      },
      {
        "id": "SHELL-weighted-lattice-fractional",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Multiplicity-weighted 2D floor-sum bound",
        "status": "open",
        "statement_tex": "Given explicit one-sided upper bounds on Psi_{ell+1/2,rho}(K) with specified error terms and monotonicity/convexity in ell, prove the 2-parameter multiplicity-weighted inequality sum_{ell>=0}(2ell+1) floor(Psi_{ell+1/2,rho}(K)/pi) <= (2/(9pi))(1-rho^3)K^3 in the fixed-rho high-energy range. Note: annulus floor-sum lemmas are 1D in the angular index and do not transfer directly under the 2ell+1 weight.",
        "dependencies": ["SHELL-count-floor-identity", "SHELL-phase-enclosures", "SRC-annuli"],
        "implies": ["SHELL-fixed-rho-high-energy", "SHELL-lattice-count"],
        "blockers": ["SHELL-phase-enclosures"],
        "evidence": {"positive": [], "negative": [], "inconclusive": ["rounds/polya-main/round1/A3_stageA.md"]},
        "owner": "A3",
        "next_action": "Formulate the weighted inequality abstractly (black-box phase); identify minimal phase-error hypotheses; audit which annulus lemmas are radial-index (transferable) vs planar-multiplicity (not)."
      },
      {
        "id": "SHELL-spherical-bessel-algebraic",
        "type": "lemma",
        "track": "shell_analytic",
        "title": "Elementary spherical-Bessel form of the shell cross-product (d=3)",
        "status": "open",
        "statement_tex": "In d=3, F_{ell+1/2,rho}(k) = P_ell(k,rho) sin((1-rho)k) + Q_ell(k,rho) cos((1-rho)k), with P_ell,Q_ell rational in k (polynomials in 1/k and 1/(rho k) of degree <= ell). Verified for ell=0,1,2: ell=0 gives sin((1-rho)k)/(rho k^2). Open: prove for all ell (no (1+rho)k frequencies survive) and assess numerical conditioning.",
        "dependencies": ["SHELL-cross-product-formula"],
        "implies": [],
        "blockers": [],
        "evidence": {"positive": ["rounds/polya-main/round1/A2_stageB.md"], "negative": [], "inconclusive": ["rounds/polya-main/round1/A3_stageA.md", "rounds/polya-main/round1/A4_stageA.md"]},
        "owner": "A4",
        "next_action": "Prove the all-ell form via spherical-Bessel recurrences; estimate coefficient growth; test interval-arithmetic conditioning against the phase form."
      }
    ],
    "update": [
      {
        "id": "CONV-strict-counting",
        "status": "proved_internal",
        "evidence_added": {"positive": ["rounds/polya-main/round1/A1_stageA.md"]},
        "next_action": "Record the equivalence: with eigenvalues repeated by multiplicity, N_D(Omega,Lambda)<=C*Lambda^{d/2} for all Lambda>=0 iff lambda_j^D>=(j/C)^{2/d} for all j>=1. Endpoint-normalize any imported non-strict or k-parameter counting before use."
      },
      {
        "id": "SHELL-cross-product-formula",
        "status": "open",
        "evidence_added": {"positive": ["rounds/polya-main/round1/A4_stageA.md", "rounds/polya-main/round1/A1_stageA.md"]},
        "next_action": "Prove radial Sturm-Liouville completeness on [rho,1] (all L^2 modes captured), radial simplicity within each ell, positivity of roots and no k=0 eigenvalue, multiplicity 2ell+1, and the R=1 scaling reduction. Do NOT require absence of accidental cross-ell degeneracy (harmless; multiplicities add). Keep the mathematical statement_tex; audit notes go in evidence/next_action."
      },
      {
        "id": "SHELL-phase-enclosures",
        "status": "open",
        "blockers_added": ["SHELL-inner-turning"],
        "evidence_added": {"inconclusive": ["rounds/polya-main/round1/A2_stageA.md"]},
        "next_action": "Split into oscillatory / outer-turning / inner-turning (delegated to SHELL-inner-turning) / evanescent regimes; produce one-sided upper bounds on Psi with explicit error, feeding SHELL-fixed-rho-high-energy."
      },
      {
        "id": "SHELL-lattice-count",
        "status": "open",
        "evidence_added": {"inconclusive": ["rounds/polya-main/round1/A3_stageA.md"]},
        "next_action": "Reduce via SHELL-weighted-lattice-fractional; demand a genuine 2-parameter weighted bound; identify which annulus floor-sum lemmas are radial-index (transferable) vs planar-multiplicity (not)."
      },
      {
        "id": "COMP-certified-bessel",
        "status": " diagnostic_only",
        "evidence_added": {"inconclusive": ["rounds/polya-main/round1/A4_stageA.md"]},
        "next_action": "Implement a validated prototype for rho=1/2, ell=0,1, 0<k<20. Evaluate via the phase/modulus form F=M_nu(rho k)M_nu(k)sin(Psi) or the elementary spherical-Bessel form, NOT the naive cross-product, to avoid catastrophic cancellation. Produce root-isolation/exclusion certificates. Keep required outputs: script, exact command, root-enclosure report, counting verification table, limitations."
      },
      {
        "id": "SRC-bessel-phase",
        "status": "source_audit_required",
        "next_action": "Card: Nicholson's integral for J_nu^2+Y_nu^2 and its strict decrease; Wronskian and phase-derivative convention theta_nu'=2/(pi z M_nu^2); validity for nu>=0, z>0; Airy/Olver transition constants and one-sided error direction; whether independent single-Bessel phase bounds can be safely differenced."
      },
      {
        "id": "SRC-annuli",
        "status": "source_audit_required",
        "next_action": "Card the exact annulus floor-sum / trapezoidal lemma hypotheses; separate radial-index estimates (candidate transfer) from angular-index estimates relying on planar multiplicity; record whether any lemma admits the weight 2ell+1."
      }
    ],
    "reject": [
      {"id": "ELLIPSE-near-circular", "reason": "Reject proposed 'blocked' status: no impossibility demonstrated. Remains open parallel flagship with SRC-mathieu-ellipse as source-audit blocker."},
      {"id": "CERT-certificate-family", "reason": "Reject proposed 'blocked' status: fallback track remains open pending SRC-jiang-lin source audit."}
    ],
    "no_change": [
      {"id": "TARGET-shell-d3", "reason": "No proof-level change. Explicit constant (2/(9pi))(1-rho^3) recorded; theorem remains open pending Layer-2 obligations."},
      {"id": "POLYA-program-target", "reason": "Global target remains open."},
      {"id": "SRC-FLPS-balls", "reason": "Source audit still required; no card produced this round."},
      {"id": "SRC-shell-weyl", "reason": "Source audit still required; needed for inner-turning constants."},
      {"id": "SRC-mathieu-ellipse", "reason": "Parallel track; source audit still required."},
      {"id": "SRC-jiang-lin", "reason": "Fallback track; source audit still required."},
      {"id": "SHELL-rho-uniformity", "reason": "Deferred per Round-1 rule until fixed-rho estimates exist."}
    ]
  },
  "round_assessment": {
    "mathematical_progress_score": 3,
    "idea_quality_score": 8,
    "state_evidence_score": 7,
    "calibration_score": 7,
    "reason": "Structural de-risking only: exact monotone phase scaffold plus a proved angular cutoff and a proved counting convention; no Polya progress and both quantitative blockers (inner-turning enclosure, 2D weighted lattice) untouched. High idea quality and solid promotable evidence; calibration good after correcting A3's premature blocked statuses."
  }
}

## Next-round prompts by agent

### For A1
Build the source cards, Nicholson first. In `SRC-bessel-phase` record Nicholson's integral for $J_\nu^2+Y_\nu^2$, its strict decrease, the phase convention and $\theta_\nu'=2/(\pi zM_\nu^2)$, the Airy/Olver transition constants with one-sided error direction, and whether single-Bessel phase bounds can be safely differenced. In `SRC-annuli` extract the exact floor-sum hypotheses and separate radial-index from planar-multiplicity estimates. Begin `SRC-FLPS-balls` and `SRC-shell-weyl`. No external theorem may be used as a proof dependency before its card exists.

### For A2
Formalize the Layer-1 scaffold: prove `SHELL-exact-phase-rep`, `SHELL-phase-monotonicity` (conditional on the Nicholson card), the branch normalization $\Psi(0^+)=0$, and `SHELL-count-floor-identity` with the strict endpoint rule $n\pi<\Psi$. Then attack `SHELL-inner-turning`: give an explicit one-sided bound on $\Psi_{\nu,\rho}$ for $\rho k-\nu=O(\nu^{1/3})$, testing whether FLPS Airy enclosures survive subtraction. Draft `SHELL-fixed-rho-high-energy` around the floor-free/boundary-term mechanism and the midpoint-quadrature control of the $\ell$-sum.

### For A3
Turn the weighted-lattice risk into a precise theorem: state and attempt `SHELL-weighted-lattice-fractional` assuming a black-box phase with explicit one-sided error and specified convexity/monotonicity in $\ell$; identify the minimal hypotheses under which the $2\ell+1$-weighted floor sum stays below $\tfrac{2}{9\pi}(1-\rho^3)K^3$, and audit which annulus lemmas are 1D-angular. Also run the exact-root signed-defect scan for $\rho\in\{0.1,0.5,0.9\}$ (not the toy proxy) and report whether the worst defect drifts to the inner-transition band. Keep ellipse/certificate parallel, not blocked.

### For A4
Discharge `SHELL-cross-product-formula` as a rigorous Sturm--Liouville completeness lemma (do not require absence of accidental cross-$\ell$ degeneracy). Derive the $\ell=0,1,2$ spherical-Bessel forms explicitly and begin the all-$\ell$ structure for `SHELL-spherical-bessel-algebraic`. Build the diagnostic interval-arithmetic prototype for $\rho=1/2$, $\ell=0,1$, $0<k<20$, evaluating via the phase/modulus or elementary form (not the naive cross-product), and report where cancellation appears. All computation remains diagnostic until the required outputs are committed.

## Round Assessment

Round 1 delivered exactly what the round rule asked for -- a clean, safe proof-obligation graph and a sharpened target -- plus one genuine structural advance. The shell counting function now has an exact, globally monotone phase representation, which converts an infinite spectral problem into a floor-sum whose *existence and indexing* need no turning-point analysis. This is real, checkable progress, but it is foundational; it does not touch the two quantitative blockers, so the proof-graph-safe `mathematical_progress_score` is kept low (3/10).

Split scores in prose:

- **A1 -- idea 8, state evidence 8.5, calibration 9.** Best state-promotable output: the strict-counting equivalence, endpoint discipline, source prioritization, and the correction that cross-$\ell$ degeneracy must not be required. Conservative and precise; minor YAML formatting only.
- **A2 -- idea 9, state evidence 8, calibration 9.** The round's key structural scaffold (exact phase, Nicholson monotonicity, floor identity, angular cutoff), plus the midpoint-quadrature and floor-free high-energy observations and a corrective exact-root diagnostic. Reviewer consensus scored this 9--10; no theorem overclaim.
- **A3 -- idea 8, state evidence 4.5, calibration 5.** The spherical-Bessel elementary form is a real, verified asset ($\ell\le2$) and the 2D-weight risk isolation is correct; but the Stage-A over-use of `blocked`, the underspecified fractional-part lemma, and the flawed diagnostic proxy lowered state-evidence and calibration. A3's Stage-B review was markedly better calibrated.
- **A4 -- idea 8, state evidence 7, calibration 8.5.** Rigorous formula confirmation, the completeness requirement, and a concrete scoped computation target with exemplary discipline; deductions only for the status-string typo and the `statement_tex` overwrite.

No Dirichlet--Polya theorem for shells, ellipses, or a certificate family is claimed or promoted.

## Confidence

- Layer-1 scaffold (exact phase, floor identity, angular cutoff, counting convention): high -- algebraically elementary and numerically corroborated; promotion to `proved_internal` gated only on the Nicholson and completeness cards.
- `SHELL-phase-monotonicity`: high on the mathematics, held at `derived_under_assumptions` until Nicholson is carded.
- High-energy floor-free route: moderately high -- the $\rho=0.5$ defect scan matches the predicted $-\tfrac{1+\rho^2}{4}\Lambda$ margin, but the explicit one-sided enclosure and Euler--Maclaurin control remain open.
- `SHELL-inner-turning` and `SHELL-weighted-lattice-fractional`: genuinely open; these are the decisive Round-2 tests. If the weighted-lattice inequality cannot be established even for a black-box well-behaved phase, the whole shell route must be re-evaluated.
- Route choice: shells remain the best primary first-theorem candidate; ellipse and certificate tracks stay open in parallel.
