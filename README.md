# Pólya AI Collaboration

This repository is a public-memory workflow for multi-AI research on Pólya's conjecture for new non-tiling Euclidean domains.

The workflow is claim-centered: `state/proof_obligations.yml` is the authoritative mathematical state, while `rounds/` contains audit evidence. Web conversation memory is useful for continuity, but the GitHub repository is the durable record.

## Target

The first theorem target is exact Dirichlet Pólya for spherical shells, starting in dimension 3:

```text
A_{rho,1} = { x in R^3 : rho < |x| < 1 }, 0 < rho < 1.
```

With the strict counting convention,

```text
N_D(Omega, Lambda) = #{ j : lambda_j^D(Omega) < Lambda },
```

the target inequality is

```text
N_D(A_{rho,1}, Lambda) <= L_3 |A_{rho,1}| Lambda^{3/2}
```

for all `Lambda >= 0`.  The full three-dimensional shell family has now been
closed internally by the purely analytic route described below; its active
work is proof reconstruction and external review.  A separate
general-dimensional shell extension is active, but remains unproved in the
residual high-floor first-drop branch; its preserved backbone and final
whole-cover assembly also still require independent audit.

The parallel flagship track is the Dirichlet ellipse / Mathieu-function program. A lower-risk backup track is a Jiang-Lin-style certificate theorem for a smooth non-tiling comparison family.

## Current shell result

As of 17 July 2026, the repository contains a project-internal purely
analytic proof of the three-dimensional spherical-shell target. The
computer-assisted proof is retained as a regression baseline, but no
executable truth value or interval enclosure is a premise of the analytic
argument. The review artifacts are:

- [main paper](manuscript/spherical-shell-polya-proof.tex);
- [analytic support-volume master](manuscript/spherical-shell-polya-analytic-supplement.tex);
- [modular analytic sources and audits](manuscript/analytic/);
- [release main PDF](output/pdf/spherical-shell-polya-proof-analytic.pdf);
- [release analytic supplement](output/pdf/spherical-shell-polya-analytic-supplement.pdf);
- [flattened Revision 2 review bundle](output/submission/spherical-shell-polya-revision2/);
- [response to the two referee reports](human/outbox/response-to-referees.md);
  and
- [evaluation of the three revised strategies](human/outbox/strategy-evaluation-and-revised-approach.md).

This status is restricted to the spherical-shell class and is an internal
proof claim. It is not a claim of literature novelty, priority, or external
publication acceptance.

## General-dimensional extension

The extension is governed by
[`human/inbox/general-d_simplified_analytic_strategy.md`](human/inbox/general-d_simplified_analytic_strategy.md).
Its exact dimension-lifting backbone is retained, but the current
[`general-dimensional manuscript`](manuscript/spherical-shell-polya-general-d.tex)
does not prove the all-dimensional theorem.

The active standalone packet is
[`Fractional terminal reserve and shelf--terminal compensation`](human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md),
its [independent audit](human/outbox/general-d-round-10-fractional-terminal-reserve-independent-audit.md),
the [Round 11 first-floor reduction](human/outbox/general-d-round-11-first-floor-pre-shelf-reduction.md)
with its [independent audit](human/outbox/general-d-round-11-first-floor-pre-shelf-reduction-independent-audit.md),
the [Round 13 exact falsification](human/outbox/general-d-round-13-endpoint-target-falsification.md)
with its [independent audit](human/outbox/general-d-round-13-endpoint-target-falsification-independent-audit.md),
and the [Round 14 exact-head endpoint reduction](human/outbox/general-d-round-14-exact-head-endpoint-reduction.md)
with its [independent audit](human/outbox/general-d-round-14-exact-head-endpoint-reduction-independent-audit.md),
the [Round 15 exact-terminal reduction](human/outbox/general-d-round-15-exact-terminal-endpoint-reduction.md)
with its [independent audit](human/outbox/general-d-round-15-exact-terminal-endpoint-reduction-independent-audit.md),
the [Round 16 geometric reduction](human/outbox/general-d-round-16-continuous-geometric-reduction-and-hard-face.md)
with its [independent audit](human/outbox/general-d-round-16-continuous-geometric-reduction-independent-audit.md),
the [Round 17 action-face reduction](human/outbox/general-d-round-17-action-face-quantile-reduction.md)
with its [independent audit](human/outbox/general-d-round-17-action-face-quantile-reduction-independent-audit.md),
the [Round 18 symbolic simultaneous-wall closure](human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure.md)
with its [independent audit](human/outbox/general-d-round-18-simultaneous-wall-symbolic-closure-independent-audit.md),
and the [Round 19 Jensen action-face closure](human/outbox/general-d-round-19-action-face-jensen-closure.md)
with its [independent audit](human/outbox/general-d-round-19-action-face-jensen-closure-independent-audit.md),
followed on the selected high-floor branch by the
[Round 20 diagnostic](human/outbox/general-d-round-20-high-floor-first-drop-surrogate-probe.md),
the [Round 21 intrinsic reduction](human/outbox/general-d-round-21-high-floor-cst-intrinsic-reduction.md),
the [Round 22 exact-cap repair](human/outbox/general-d-round-22-coarse-intrinsic-scalar-falsification-and-exact-cap-repair.md),
the [Round 23 curvature-cell reduction](human/outbox/general-d-round-23-exact-cap-curvature-reduction-and-failure-report.md),
the [Round 24 two-axis reduction](human/outbox/general-d-round-24-c8-two-axis-reduction-and-failure-report.md),
and the [Round 25 stationary projection](human/outbox/general-d-round-25-c8-stationary-identity-and-sublevel-failure-report.md),
each with its independent audit, followed by the
[Round 26 lossless projection and coupled-owner falsification](human/outbox/general-d-round-26-lossless-stationary-projection-and-F-falsification.md),
the separate [exact stationary-image certificate](human/outbox/general-d-round-26-exact-stationary-image-counterexample-to-F.md),
the [exact-domain \(\mathcal C_8\) certificate](human/outbox/general-d-round-26b-certified-C8-counterexample-with-positive-exact-correlated-scalar.md),
their [combined independent audit](human/outbox/general-d-round-26-lossless-F-and-C8-counterexamples-combined-independent-audit.md),
the [Round 27 automatic-sector reduction](human/outbox/general-d-round-27-remainder-rich-automatic-closure-and-hard-sector-reduction.md),
the [exact global-\(\mathcal R_J\) counterexample and loss audit](human/outbox/general-d-round-27-certified-exact-RJ-counterexample-and-loss-audit.md),
the [residual hard-sector diagnostic](human/outbox/general-d-round-27-hard-sector-diagnostic.md),
their [combined independent audit](human/outbox/general-d-round-27-combined-independent-audit.md),
the [Round 28 exact-E quartic projection](human/outbox/general-d-round-28-exact-remainder-quartic-curvature-projection-and-hard-face.md),
the [hard-phase Cmax branch reduction](human/outbox/general-d-round-28-hard-sector-Cmax-branch-reduction-and-failure-report.md),
their [combined independent audit](human/outbox/general-d-round-28-combined-independent-audit.md),
the [Round 29 complete-terminal phase/wall reduction and primary-cell closure](human/outbox/general-d-round-29-complete-terminal-phase-monotonicity-and-primary-inverse-cell-closure.md),
its [combined independent audit](human/outbox/general-d-round-29-combined-independent-audit.md),
the [Round 30 nonconstant-\(K\) endpoint reductions](human/outbox/general-d-round-30-nonconstant-K-endpoint-reductions-and-retained-E-shelf-scalar.md),
their [independent audit](human/outbox/general-d-round-30-independent-audit.md),
the [Round 31 retained-\(E\) convexity and large-\(q\) exclusion](human/outbox/general-d-round-31-retained-E-convexity-and-large-q-exclusion.md),
its [independent audit](human/outbox/general-d-round-31-independent-audit.md),
the [Round 32 shelf-bootstrap truncation and compact retained-shelf closure](human/outbox/general-d-round-32-shelf-bootstrap-truncation-and-compact-retained-shelf-closure.md),
its [independent audit](human/outbox/general-d-round-32-independent-audit.md),
the [Round 33 lower-\(Q\) hard-arc monotonicity and endpoint reduction](human/outbox/general-d-round-33-lower-Q-hard-arc-monotonicity-and-endpoint-reduction.md),
its [independent audit](human/outbox/general-d-round-33-independent-audit.md),
the [Round 34 activity excision and correlated quadrature reduction](human/outbox/general-d-round-34-activity-excision-and-correlated-quadrature-reduction.md),
its [independent audit](human/outbox/general-d-round-34-independent-audit.md),
the [small-phase adjacent-action closure](human/outbox/general-d-lower-Q-small-phase-adjacent-action-closure.md),
its [independent audit](human/outbox/general-d-lower-Q-small-phase-adjacent-action-independent-audit.md),
the [Round 35 lower-\(Q\) hard-sector closure](human/outbox/general-d-round-35-lower-Q-hard-sector-closure.md),
its [independent audit](human/outbox/general-d-round-35-independent-audit.md),
the [Round 36 exact count-gap and collision reduction](human/outbox/general-d-round-36-exact-count-gap-collision-reduction.md),
its [independent audit](human/outbox/general-d-round-36-independent-audit.md),
the [Round 37 gap-interface synchronization and exact-shelf reduction](human/outbox/general-d-round-37-gap-interface-synchronization-and-root-free-gate.md),
and its [independent audit](human/outbox/general-d-round-37-independent-audit.md).
The terminal reserve and the zero-level first-floor corner are proved.  Round
13 proves that the lossy Round 11--12 pre-shelf sign target is false even on
the new extension grid; it does not falsify the true defect.  Round 14 restores
the exact no-drop head and cap.  Round 15 restores the exact terminal count
and proves the lossless endpoint reduction.  Round 16 reduces that endpoint
to the grid-free geometric inequality \(F(K,a)\ge1/2\), proves \(F_K>0\), and
closes the suspected \(q=3\) double face with a positive rational reserve.
Round 17 proves that the remaining action-face comparison integrand is
increasing and concave.  Round 18 proves the simultaneous-wall reserve
symbolically, and Round 19 bypasses the chord scalar with a one-radius Jensen
argument proving \(dF/da>0\) on the whole action face.  Together they close
\(F(K,a)\ge1/2\) and the hard \(B=1\) endpoint.  The
[independent WP2 integration audit](human/outbox/general-d-first-floor-no-drop-wp2-integration-audit.md)
then verifies every first-floor phase, both new dimension grids, the activity
wall, strict floor/inverse/action walls, and the exact redundancy of the
apparent \(z=2\) boundary.  Thus the first-floor no-drop theorem is proved.
For the selected high-floor branch, the audited
[Round 20 diagnostic](human/outbox/general-d-round-20-high-floor-first-drop-surrogate-probe.md)
finds no sampled failure of either the exact scalar or its lower surrogate,
and the audited
[Round 21 intrinsic reduction](human/outbox/general-d-round-21-high-floor-cst-intrinsic-reduction.md)
proves the cap, interface-level/top-interval, and elasticity/curvature
transport.  Round 22 then gives an exact active counterexample to the coarse
sign \(\mathcal R\ge0\); it is not a counterexample to CST.  Retaining the
exact cap \(J=2I_\mu(q)\) proves
\(\Phi_\delta>\mathcal R_J\), where
\(\mathcal R_J=\mathcal R+1/7-J\).  Round 23 keeps this exact cap through the
final comparison, proves \(J<1/8\) and \(\mathcal R_J>\mathcal C_8\), and
reduces the then-proposed sufficient sign \(\mathcal C_8\ge0\) to intrinsic
walls or one stationary point on each strictly convex action/top-payment
cell.  Round 24 reduces the shelf labels to at most two adjacent
\(p\)-owners at fixed \(x=r+p\), eliminates \(\alpha\) exactly on the delicate
quadratic top cell, and proves the lower-wall transport signs.  Its audit also
confirms that the candidate conditions are coupled: global
\(\alpha\)-monotonicity and bare lower-wall dominance are not premises.  The
Round 25 stationary identity reduces the delicate interior cell further to
\(\mathcal C_8\ge\mathcal F(B,m,t,u)\) on the full projected image of the
two paired shelf integrals, interface strip, activity condition, parity grid,
and coupled \(p\)-owners.  Round 26 certifies that both this lower scalar and
the curvature-only sign lose too much: a full-image, unique coupled-owner
witness has \(\mathcal F<-1/50<0<77/50<\mathcal C_8\), while a separate exact
feasible witness has \(\mathcal C_8<-7<0<20<\mathcal R_J\).  Round 27 then
certifies that even the global signs \(\mathcal C_{\max,8}\ge0\) and
\(\mathcal R_J\ge0\) are false.  At its exact integer-grid witness,
\(\mathcal C_{\max,8}<-4/3\) and \(\mathcal R_J<-6/5\), but the exact reduced
scalar satisfies \(\mathscr S>47\) and \(\Phi_\delta>40\).  The discrepancy is
explained by more than 42 units of discarded shelf and terminal reserve.

Crucially, that witness is not in the residual hard sector.  Writing
\(d=1-2t/\pi\), \(E=e_0+e_p\), and \(E_*=(p-dm)/(2p)\), Round 27 proves directly from the
exact shelf--terminal scalar that every tuple with \(p\le dm\) or
\(E\ge E_*\) already has \(D_A(r)\ge0\).  The only remaining pointwise domain
is
\[
 p>dm,\qquad 0\le E<E_*<\frac12,
\]
where the exact obligation is
\(\max\{0,L_T\}+a_p\Delta\ge p(E_*-E)\).  A proof of
\(\mathcal C_{\max,8}\ge0\) is retained only as a stronger sufficient target
on this hard sector, not globally and not as an equivalent reformulation.
Round 28 strengthens the exact route to
\[
 D_A(r)\ge\Phi_\delta^+\ge
 \Psi^{L_T}_{4,E}
 =\max\{0,L_T\}
  +a_p\max\{\tau(E+2\lambda),\mathcal K_4\}
  +p(E-E_*),
\]
with a strict quartic curvature gain.  It also proves that the hard sector is
one initial phase interval.  The complete-terminal scalar, retaining every
inverse fraction and the actual \(E\), is now primary; root-free and Cmax
signs are auxiliary.  Round 29 proves strict increase on every fixed-\(\alpha\)
terminal count cell and strict decrease on every fixed-\(Q\), constant-\(K\)
inverse/outer-\(B\) wall segment.  It also closes the entire primary
\((r,p,m,f)=(1,2,2,2)\), \(B=Q=1\), \(2<y_1<3\) component with exact margin
\(371/15840+2\eta_1+2E\).  Round 30 then makes activity automatic throughout
that first inverse band, proves \(L_T>7/10\) and strict terminal increase on
the included lower shelf, and reduces the shelf sign to the retained-\(E\)
scalar \(F(q,r,p,m)\) under three exact necessary conditions.  It also removes
noncorner lower-\(Q\) endpoints from every \(y_1>1\) band and closes the
\(\alpha=0\), \(f=2\), \(4/5\le t<13/10\) phase range.  Round 31 proves
dependent-profile convexity, excludes every real \(q\ge1000\), and reduces a
weaker finite scalar \(L_q\) to three convex edges.  Round 32 keeps shelf
feasibility correlated: for \(q\ge35\) it proves
\(m>(6/5)(\pi/\psi-3)\), thereby removing the genuinely false untruncated
\(m=1\) edge.  One compact directed-Arb certificate then proves
\(L_q>1/100\) on both nontrivial edges for all 1994 exact parity-grid values
below \(1000\); the \(p=1\) edge is analytic.  Thus the included retained-\(E\)
lower shelf is closed.  Round 33 proves analytically that, on the exact open
lower-\(Q\) wall, the hard remainder gap \(H=E-E_*\) is strictly decreasing
with \(\mu\).  Hence a hypothetical hard component cannot end in that smooth
wall interior; it must reach the lower shelf, activity wall, or
\(\alpha\to1^-\).  This is not full-\(\Psi\) monotonicity and does not prove
those endpoint signs.  Round 34 removes the activity wall altogether on every
high-floor first shelf, with exact margin \(>1/16\).  It then compares the
terminal action and preceding shelf through the same radial-parameter
integral and reduces lower-\(Q\) hard-sector exclusion to the one normalized
face and a finite stationary alternative.  The small-phase adjacent-action
lemma closes \(0<t\le\pi/8\).  Round 35 closes the complementary phase by
one correlated quadrature estimate for \(\pi/8\le t\le\pi/6\), an exact
boundary polynomial and stationary discriminant for
\(\pi/6\le t<3\pi/14\), and an empty-domain argument above that cutoff.
Thus the lower-\(Q\) hard sector is closed analytically.  Remaining
Round 36 then proves \(B-Q\in\{0,1\}\), fixes the exact outer-\(B\)/\(Q\)
wall order and collision ownership, and obtains
\(L_T>1-J>6/7\) on the one-level-gap branch.  Hence the full selected
scalar is positive whenever \(p-dm\le12/7\), including every \(p=1\)
gap face and all old inverse-wall bad sides.  Higher \(Q_N\) walls have the
exact terminal reserve \(L_T>3G_\mu(q)>0\), but their full scalar is not yet
closed.  Round 37 synchronizes the hard gap interface as
\(B_0=Q=B-1\ge1\), proves the top interval is exactly zero, and rewrites the
selected residual losslessly as

\[
 \Gamma_{\rm gap}
 =1-J+\frac{B_0d}{2c}+\Omega
 +(p+a_p)M_4+p\Xi-\frac{p-dm}{2},
 \qquad \Omega>0,\quad\Xi\ge0.
\]

It also proves the count-free strict reduction
\(\Phi_\delta^+>\mathcal H_\Delta\).  Neither residual expression has yet
been signed on the continuum.  The current task is therefore the exact
Round 37 gap sign on the transported outer, inverse, lower-shelf, and
\(\alpha\)-endpoint faces, followed by higher \(Q_N\) faces, equal-count
inverse faces, simultaneous \(\alpha=0\) \(B/Q\) corners, and lower shelves
outside the precise Round 30--32 retained-shelf theorem.
The adaptive cusp is diagnostic only and shows that global
\(\alpha\)-monotonicity is false.  If the exact endpoint route fails, return
to \(\mathscr S\) and then the weighted aggregate.  At most one consolidated
compact certificate may remain in the final implication chain; the legacy
first-floor check must be replaced or folded into it.  The
historical ratio ladder and certificate families remain frozen evidence, not
the live proof architecture.

## Functional Roles

- `A1`: project lead, proof-obligation mapper, integrator, and State Patch author.
- `A2`: incumbent proof author for the selected analytic bottleneck.
- `A3`: clean-room solver working from a reduced packet without the incumbent proof.
- `A4`: adversarial referee, formula checker, and certified-computation engineer.

A1, A2, and A3 are semi-manual: paste prompts into persistent web conversations and save copied Markdown responses into `handoff/`. A4 is automatic when `DEEPSEEK_API_KEY` is configured.

These are configurable functional roles, not a permanent mathematical hierarchy. For a bottleneck obligation, lead author, clean-room reviewer, and adversarial reviewer must be distinct.

## Obligation Protocol

Each cycle is organized around one primary proof obligation and at most one independent secondary obligation:

1. The project lead prepares an exact obligation packet and assigns only needed roles.
2. The incumbent author and clean-room solver work independently.
3. The adversarial reviewer audits the frozen attempts and identifies the first unsupported implication.
4. Codex-style computation work produces diagnostic or certified artifacts under an explicit evidence class.
5. One lead integrates discharged obligations and writes a machine-readable `State Patch`.
6. The validator applies accepted changes and regenerates the reading packet.
7. A fresh final referee audits an assembled theorem before promotion.

The Revision 2 reviewed release uses the exact layer cake as its explanatory spine and
has no live finite owner graph.  Its disjoint cover is: no mode for
`K <= pi/(1-rho)`; one ratio-sharp analytic defect theorem for larger `K` and
`0 < rho < 39/50`; and the optical theorem for larger `K` and
`39/50 <= rho < 1`.  The `rho = 39/50` face is optical-owned and the threshold
frequency face is no-mode-owned.

The old `rho_*` split, staircases through `k_11`, 38-state theorem, residual
sets, 611-row allocation, and executable certificates are detached historical
or regression evidence.  The live graph edge is
`SHELL-analytic-retained-remainder-closure -> SHELL-rho-uniformity`.

Barriers are enforced only at genuine mathematical dependencies. The configured workflow currently gives A1 an integration review of A2/A3/A4 and gives A4 an adversarial review of the frozen A2/A3 attempts; A2 and A3 do not perform universal cross-reviews.

## Layout

```text
problems/
  polya_conjecture.md
protocol.md
config/
  agents.example.json
  agents.web-polya.json
math_collab/
  orchestrator.py
  proof_obligations.py
  validate_state_patch.py
  validate_round.py
  human.py
  normalize_markdown.py
state/
  proof_obligations.yml
  next_round_prompts.md
  last_validation_report.md
  current_state.md
  lemma_bank.md
  gap_register.md
  best_proof_draft.md
sources/
  seed_reports/
human/
  current_directives.md
  goals.md
  ideas.md
  references.md
  inbox/
manifests/
  reading_packet.md
rounds/
  <run-id>/
handoff/
  <run-id>/
```

`rounds/` is the public archive. `handoff/` is ignored by Git and is used for temporary web prompts and copied web responses. The reading packet is generated from the proof-obligation graph rather than from transcript history.

## Quick Start

Validate the proof-obligation graph:

```powershell
python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
```

Smoke test the file layout without external API calls:

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --rounds 1 --dry-run --run-id smoke --no-state-update
```

Configure DeepSeek for the automatic A4 agent:

```powershell
Copy-Item .env.example .env
notepad .env
```

Then fill in:

```text
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-pro
```

Smoke test A4:

```powershell
python -m math_collab.api_smoke --config config/agents.web-polya.json --agents A4
```

Generate or advance a mixed manual-web/API research round:

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --run-id polya-main --start-round 1 --rounds 1 --skip-missing-api
```

For the guided runner:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId polya-main -StartRound 1 -Rounds 1
```

Add `-SubmitPrompts` if you want the helper to press Enter after pasting prompts. Add `-NoAutoPublish` to apply Stage D locally without committing/pushing to GitHub.

## Current Focus

- Preserve the revised purely analytic theorem and its strict wall ownership.
- Independently reconstruct the ratio-sharp angular, radial/ball, and scalar
  arguments line by line.
- Keep all finite ledgers and numerical programs detached as regression
  evidence.
- Obtain conventional peer review and a current literature/novelty search
  before any publication claim.
- On the separate general-dimensional track, treat the included retained-
  \(E\) shelf and the lower-\(Q\) hard sector as closed.  Attack the exact
  Round 37 residual gap sign: prove the lossless \(\Gamma_{\rm gap}\) form or
  its \(\mathcal H_\Delta\) sufficient gate on \(B=Q+1\) with
  \(p-d_m>12/7\) (including wall endpoints), then the higher
  \(Q_N\) and generic equal-count inverse faces, the exceptional \(\alpha=0\)
  simultaneous \(B/Q\) corners, and the general lower-shelf or alpha-closure
  configurations outside the retained Round32 compact certificate.
- Treat Mathematica and other high-precision sweeps as falsification and
  theorem-design evidence unless a distinct certified finite obligation is
  created.

## Human Steering

Edit these files before the next stage or round:

- `human/current_directives.md`: active steering instructions.
- `human/goals.md`: current research and workflow goals.
- `human/ideas.md`: mathematical ideas to try.
- `human/references.md`: papers, links, theorem names, citations, or notes.
- `human/inbox/`: timestamped human notes.

You can also add a note from the command line:

```powershell
python -m math_collab.human --kind idea --title "Check shell phase" --text "Assign a lead proof, a clean-room reconstruction, and an adversarial audit for the shell phase bottleneck." --activate
```

## Safety Rules

Every agent must separate:

- proved statements,
- plausible claims,
- gaps,
- counterexample attempts,
- dependencies,
- confidence.

External theorems need source cards before they are used as proof dependencies. Computations can provide diagnostics and certification evidence, but they do not by themselves prove an analytic theorem unless the proof obligation explicitly states a certified finite verification target.
