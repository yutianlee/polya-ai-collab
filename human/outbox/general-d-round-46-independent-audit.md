# General-dimensional spherical-shell Pólya project
## Round 46 final independent audit and Gate-B decision

**Date:** 21 July 2026  
**Role:** Prompt D final independent auditor  
**Selected obligation:** `SHELL-general-d-high-floor-first-drop-CST`  
**Authoritative status at audit:** `open`

## 1. Verdict

```text
INCOMPLETE
```

Round 46 proves several exact reductions but does not prove the
complete-owner sign of (R45.18). It also supplies no directed counterexample
to (R45.18) or to the exact unprojected scalar \(\mathscr S\). Under the
explicit Round-46 hard rule, Gate B therefore stops and the next mathematical
round must switch to the weighted aggregate. This is an unfinished proof, not
a falsification and not a proof of architectural impossibility.

No proof-obligation status is promoted or demoted by this audit.

## 2. Frozen-artifact and repository gate

The repository gate passed before the mathematical comparison.

| item | independently observed |
|---|---|
| repository | `https://github.com/yutianlee/polya-ai-collab.git` |
| branch | `codex/general-d-round-46-r45-18-complete-owner` |
| HEAD / required base | `3ad6a78d9cb2b81d316bcf0c171ad7cce9f4fee1` |
| Round-45 support commit | `cdfa6a6770207f29b603e18b34526aec1cc8feab`, ancestral |
| selected obligation | `SHELL-general-d-high-floor-first-drop-CST : open` |
| Round-45 finalized artifacts | present and unchanged from the support commit |

The frozen hashes all match the values supplied to Prompt D:

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4` |
| Prompt-A report | `1f3719f043616ce9877adb132fa789ab60ac84dd0aa10f27a30c7787aa9d3be1` |
| Prompt-A Mathematica replay | `b2b45864e3a9ef8583e2dec96f325d2104f6e9e2ceee0fb0b22a50cbd09b1236` |
| Prompt-A Python diagnostic | `82f3f48b66e5cf73d4f70e73f77e61f69a9f1cac58800aada0b5e9853a309ca4` |
| Prompt-B final report | `f23424027d9494f69692d88036b981f9c61b421484316b370da9f0041493280a` |
| Prompt-C report | `a6520f62d2d66bde7751aeaab01bd78a7df653cf9a9f6b54afa4ed23b5032f7c` |
| Prompt-C search | `79030d5527c0c0aaf8e32463631157b8826f94338edce4390cd0ce32635501fc` |

The frozen clean-room prefix in Sections 1--5 also reconstructs to its
declared pre-comparison hash

```text
af88daa4a96593822c64b36c1d2f0192927870f75142ab41051284b5e444a926
```

after its terminating newline. Thus the post-freeze comparison did not
rewrite the independent derivation.

The one source conflict is the already disclosed narrative lag in the
`next_action` and blocker prose of `state/proof_obligations.yml`. Its statuses
remain authoritative; the audited Round-45 decision and the Round-46 packet
control this local calculation. No incompatible mathematical versions were
combined.

## 3. Independent replays

The frozen Mathematica file was run with Mathematica 15.0. It returned

```text
round46R4518ReplayOK=True
```

including zero symbolic residuals for the action derivatives, the wall
derivatives, the antiderivative and closed cap \(J\), the inverse-action
kernel, the phase algebra, and the exact coefficients \(7/48\), \(9/64\),
and \(1/(16\beta)\). Its `FindRoot` fixtures are high-precision regressions,
not exact coverage.

The frozen lead Python diagnostic exited successfully. It reproduced 30
high-precision exact owners from 60,480 proposals, found no sampled negative
(R45.18) margin, and reproduced the stated diagnostic minima and the two
opposite wall-derivative signs. Its relaxed negative \(F_{\rm strong}\) point
is explicitly outside the exact owner. These results are finite diagnostics
only.

The full frozen Prompt-C program, not merely its quick mode, was replayed at
90 decimal digits and 768 Arb bits. It reproduced

```text
distinct proposals:             886225
mandatory-box proposals:        447640
high-precision exact owners:        833
sampled R45.18 negatives:             0
sampled exact-S negatives:             0
sampled M30 positives:                  0
positive coverage certificate:     false
```

Both parity grids and every reported stress class were present. The directed
rational wall/inverse brackets and Arb enclosures for the diagnostic minimum
and the three Round-45 CF regression records replayed successfully. In
particular, the directed diagnostic minimum has

\[
 \mathcal M_{45.18}=1.7091455068451735356551549621\ldots>0,
 \qquad
 \mathscr S=2.6945652789003550256293329148\ldots>0.
\]

That certifies only the displayed point. It does not certify that the point
is a global minimum or cover the infinite owner.

## 4. Exact mathematical result of Round 46

Let \(\mathcal M\) be the literal right side of (R45.18) minus its left
side. The lead and clean-room derivations agree on the following exact facts.

First, with

\[
 \phi=\arccos(q/K),\qquad
 a=\arccos\frac q{q+1},\qquad v=B_0+\frac34,
\]

the unique outer-wall normalization is

\[
 q(\tan\phi-\phi)=\pi v,
 \qquad K=q\sec\phi=(q+1)\sec t,
 \qquad \cos t=\frac{\cos\phi}{\cos a}.
\]

It gives one \(\phi\in(a,\pi/2)\), hence one \(t\in(0,\phi)\), and the cap
has the closed form

\[
 J=\frac{\{(q+1)^2+2q^2\}a-3q\sqrt{2q+1}}{2\pi}.
\]

Second, at fixed \((p,m,B_0)\) on an open owner component,

\[
 \phi'<0,\qquad t'<0,\qquad K'>0,\qquad
 W'>0,\qquad J'<0,\qquad \mathcal T'>0.
\]

The exact derivative of the full margin is printed, but its correlated
action, old-level, and shelf-curvature portion has no proved sign. The
opposite diagnostic derivative signs confirm that the bare continuous wall
geometry does not itself supply monotonicity.

Third, the strongest completed reduction is the strict inverse-action
quotient theorem. If

\[
 \mathcal D=A(x)-A(q),\qquad
 Q(z)=\frac{\{\arccos(z/K)-\arccos(z/\mu)\}
 \sqrt{\mu^2-z^2}}{\pi z},
\]

then \(\mathcal D/(U_x-U_q)\) is a positive weighted average of \(Q\) on
\([x,q]\). With \(z=\mu\cos y\) and \(\lambda=\mu/K\),

\[
 \frac d{dy}\{\pi Q(\mu\cos y)\}
 =\cos y\int_\lambda^1
 \frac{1-s^2}{(1-s^2\cos^2y)^{3/2}}\,ds>0.
\]

Thus \(Q\) is strictly decreasing in \(z\), and

\[
 \frac{\mathcal D}{U_x-U_q}>
 \frac{(\phi-a)\tan a}{\pi}.
\]

Combining this with \(t<\phi\), the scoped cap estimate \(J<1/10\), the
exact wall equation, and the already proved positivity of the old-level,
top, and elementary shelf-curvature payments yields

\[
 \boxed{\mathcal M>F_{\rm strong}},
\]

where

\[
\begin{aligned}
F_{\rm strong}={}&
 \frac{p(U_r-U_x)(\phi-a)\tan a}{\pi}\\
&+\frac{q(\tan\phi-\phi)(\pi-2\phi)}{2\pi\phi}
 +\frac{d_\rho m}{2}-\frac p2+\frac{41}{40}.
\end{aligned}
\]

This is a strict sufficient reduction only. The complete-owner inequality
\(F_{\rm strong}\ge0\) was not proved. The separate clean-room Jensen route
also remains open at its correlated interior-kernel estimate. Therefore none
of these exact results proves \(\mathcal M\ge0\).

## 5. The twelve required determinations

### 1. What exact theorem or reduction was proved?

The exact theorem is the unique outer-wall normalization, closed cap formula,
the listed signed wall derivatives, and the strict inverse-action quotient
bound. Together with the inherited payment lemmas, these prove

\[
 \mathscr S>\mathcal M>F_{\rm strong}
\]

on the fixed complete owner. The first inequality is the exact loss ledger
with strict adjacent action; the second is the new Round-46 reduction.

### 2. Was (R45.18) proved on the complete exact owner?

No. It would require \(\mathcal M\ge0\). Round 46 proves only the lower
reduction \(\mathcal M>F_{\rm strong}\), and the sign of
\(F_{\rm strong}\) on the complete owner is open.

### 3. Is every inherited hypothesis used within scope?

Yes as a scope audit. The outer-wall, common-shelf, first-drop, fixed inverse
side, hard-\(E\), parity, activity, and upper-\(\alpha\) labels are retained.
The cap bound is used only with its audited \(q\ge5\), \(p\ge3\) hypotheses;
the adjacent-action and action-drop identities are used only on the fixed
owner; and the old/top Bregman and shelf estimates remain on their proved
intervals. Some owner hypotheses do not enter the elementary formula for
\(F_{\rm strong}\); that loss of usable correlation is reported as the
reason its sign remains open. The relaxed negative probe is not represented
as an owner.

### 4. Is any sufficient inequality misreported as equivalent?

No. Both reports explicitly distinguish

\[
 F_{\rm strong}\ge0\Longrightarrow\mathcal M>0
 \Longrightarrow\mathscr S>0
\]

from converses, which are not asserted. Prompt C separately evaluates the
literal (R45.18) margin and exact \(\mathscr S\).

### 5. Is any correlated quantity worst-cased independently without a quantified loss?

No load-bearing step does so. The action quotient preserves the common
\((q,\phi,a,r,p,m)\) geometry. Every subsequent relaxation has a signed
slack: quotient slack, phase slack, or one of the positive
\(\mathcal O,\mathcal T,\mathcal C\) payments. The larger-domain scan does
discard shelf, activity, and inverse correlations, but it is labelled a
non-owner diagnostic and proves no owner statement. The missing use of those
correlations is the open gap, not a hidden estimate.

### 6. Are all payments counted exactly once?

Yes. The exact reconciliation is

\[
\begin{aligned}
\mathscr S-\mathcal M={}&
 (\Omega_--\Omega_{\rm lb})
 +(\mathcal R_{\rm tan}^0-\mathcal T-R_{\rm old})\\
&+(\mathcal C_p-\mathcal C)
 +p\{E-R_1\mathcal D\}.
\end{aligned}
\]

The old Bregman intervals and literal top interval are disjoint. The shelf
hinge is not added to the elementary curvature reserve. Adjacent action is
used only in the last term. The \(1/(16\beta)\) relation reconciles two
terminal ledgers and is not added as a reserve. Hence old Bregman, top
Bregman, shelf curvature, hinge, adjacent action, and reconciliation each
occur once.

### 7. Are the strict brackets and equality faces assigned correctly?

Yes. Ordinary-floor equality stays with its literal owner; the outer wall
has one-sided old-chart label \(B\) but literal strict count \(B_0=B-1\);
the endpoint shell count is \(Q=B_0\). One fixed old-inverse side vector is
retained, and the newest \(y_B=0\) event belongs only to the top/outer event.
The face \(e_p=0\) is allowed and adjacent action remains strict. The face
\(E=E_*\) belongs to the automatic sector. Activity equality belongs to the
no-mode owner. Integer and half-integer grids stay separate, and
\(\alpha\uparrow1^-\) remains the old chart's endpoint rather than being
relabelled as the next chart's \(\alpha=0\). No argument crosses a floor,
inverse, activity, parity, or outer-count wall by continuity.

### 8. How are the computations classified?

- Mathematica's symbolic residuals and the coefficient integrals are exact
  symbolic/rational replays.
- Mathematica's numerical fixtures and the lead Python sweeps are
  high-precision diagnostics.
- Prompt C's binary64 and mpmath extrema are finite diagnostics.
- Prompt C's named 768-bit Arb evaluations, based on rational wall and
  inverse brackets plus uniqueness proofs, are directed certificates for
  those individual records.
- No positive finite result is a continuum or infinite-owner certificate.

These classifications are accurate in the frozen artifacts.

### 9. What is the first unrepaired logical gap?

In the strongest completed implication chain it is

\[
 \boxed{F_{\rm strong}\ge0\quad\text{on every complete exact owner}.}
\]

The direct wall route and the clean-room Jensen route have earlier
route-specific unsigned inequalities, but the quotient theorem bypasses
them only to reach this still-unsigned terminal inequality.

### 10. Which proof-obligation statuses should change?

None. In particular:

| obligation | retained status |
|---|---|
| `SHELL-general-d-high-floor-first-drop-CST` | `open` |
| `SHELL-general-d-branching-backbone` | `derived_under_assumptions` |
| `SHELL-general-d-weighted-aggregate` | `proposed` |
| `SHELL-general-d-pointwise-assembly` | `open` |
| `TARGET-shell-general-d` | `proposed` |

Workflow selection and `next_action` prose should be updated, but that is
not a mathematical status promotion.

### 11. Does Gate B close, stop by falsification, or stop by the hard rule?

Gate B stops by the Round-46 hard rule. It does not close, because the sign
is unproved. It does not stop by falsification, because Prompt C found no
directed exact-owner reverse of (R45.18) and no directed negative exact
\(\mathscr S\).

### 12. What is the next single obligation?

The single next obligation is

\[
 \boxed{\mathcal B_d(A)+\sum_{m\ge0}c_{d,m}D_A(r_m)\ge0,}
\]

starting with \(d=4\), with the exact branching weights and no new ratio
ladder, pointwise owner family, or additional compact certificate.

## 6. Round 47 launch specification: exact weighted aggregate in d=4

### 6.1 Target and exact specialization

For \(d=4\),

\[
 r_m=m+1,\qquad c_{4,m}=m+1.
\]

Round 47 must prove the one exact active-region statement

\[
 \boxed{\mathrm{WT}_4:
 \mathcal B_4(A)+\sum_{m\ge0}(m+1)D_A(m+1)\ge0.}
\]

The equality-inclusive no-mode region

\[
 K^2\le \frac{\pi^2}{(1-\rho)^2}+\frac34
\]

retains its existing owner. Only the strict active complement enters
\(\mathrm{WT}_4\).

### 6.2 First exact bonus lemma

This audit independently checked the following suitable starting lemma. On
the cell \(z=a+x\), with integer \(a\ge1\) and \(0\le x<1\), the exact
signed primitive is

\[
 \Delta_4(z)=-\frac a6+\frac{a x(1-x)}2-\frac{x^3}{6}.
\]

The minimum of \(-\Delta_4\) occurs at

\[
 x_a=\sqrt{a(a+1)}-a\in(0,1/2),
\]

and is

\[
 \min_{0\le x<1}(-\Delta_4(a+x))
 =\frac{a(a+1)}
 {12\{a+1/2+\sqrt{a(a+1)}\}}
 >\frac a{24}.
\]

Since \(-\Delta_4\ge0\) also on \([0,1)\), the exact bonus obeys

\[
\begin{aligned}
 \mathcal B_4(A)
 &=2\int_0^K(-A'(z))(-\Delta_4(z))\,dz\\
 &\ge\frac1{12}\int_1^K\lfloor z\rfloor(-A'(z))\,dz
 =\frac1{12}\sum_{1\le j<K}A(j),
\end{aligned}
\]

where \(A\) is extended by zero beyond \(K\) for the telescoping identity.
This has the correct natural \(K^{d-2}=K^2\) scale. It is a launch lemma,
not a proof of \(\mathrm{WT}_4\) and not a status change.

### 6.3 Required analytic sequence

Round 47 should proceed in this order.

1. Define the actual negative support
   \[
   \mathcal N_4(A)=\{a\in\mathbb N:a<K,\ D_A(a)<0\}
   \]
   and, using only already proved pointwise modules in their exact scopes,
   prove an intrinsic inclusion of \(\mathcal N_4(A)\) in the unresolved
   active high-floor first-drop region. Do not replace this by a ratio or
   count ladder.
2. Derive a quantitative lower defect \(D_A(a)\ge-\Xi_a\) on that support,
   retaining the shell/action variables that also feed the bonus moment.
   Print a loss ledger; do not independently worst-case floor, cap, action,
   shelf, and bonus variables.
3. Prove the exact weighted comparison
   \[
   \sum_{a\in\mathcal N_4(A)}a[-D_A(a)]
   \le \mathcal B_4(A)
      +\sum_{a\notin\mathcal N_4(A)}aD_A(a).
   \]
   This is exactly sufficient for \(\mathrm{WT}_4\). Dropping the retained
   positive-tail sum and comparing only with the bonus is a stronger
   sufficient route, not an equivalent reformulation.
4. Use the cellwise bonus lemma to convert the right side into an exact
   action moment. The first candidate comparison is
   \[
   \sum_{a\in\mathcal N_4(A)}a\Xi_a
   \le\frac1{12}\sum_{1\le j<K}A(j),
   \]
   but it may be asserted only after the support and correlation estimates
   are proved.
5. Audit the complete moderate-\(K\) window and the limits
   \(\rho\uparrow1\). Preserve strict action brackets, integer-\(K\) walls,
   inner-interface walls, activity equality, and every exact branching
   weight. Use the completed \(d=3\) theorem only as the base case, not as an
   extra shifted-tail premise.
6. Falsify the literal \(\mathrm{WT}_4\) target with an evaluator independent
   of the lead derivation. Any named negative must receive rational wall and
   inverse brackets and directed Arb arithmetic. A failure of a sufficient
   route bound is not a failure of \(\mathrm{WT}_4\).

The round succeeds only with a complete analytic weighted comparison on the
whole active \(d=4\) domain, including equality faces and moderate frequency.
A positive finite sweep remains diagnostic.

## 7. Proposed exact state patch

The state file was not edited. The following RFC-6902 patch is proposed
against the verified hash in Section 2. Its `test` operations make the
no-promotion condition explicit.

```json
[
  {"op":"test","path":"/proof_obligations/64/id","value":"SHELL-general-d-branching-backbone"},
  {"op":"test","path":"/proof_obligations/64/status","value":"derived_under_assumptions"},
  {"op":"test","path":"/proof_obligations/99/id","value":"SHELL-general-d-high-floor-first-drop-CST"},
  {"op":"test","path":"/proof_obligations/99/status","value":"open"},
  {"op":"test","path":"/proof_obligations/100/id","value":"SHELL-general-d-weighted-aggregate"},
  {"op":"test","path":"/proof_obligations/100/status","value":"proposed"},
  {"op":"test","path":"/proof_obligations/101/id","value":"SHELL-general-d-pointwise-assembly"},
  {"op":"test","path":"/proof_obligations/101/status","value":"open"},
  {"op":"test","path":"/proof_obligations/123/id","value":"TARGET-shell-general-d"},
  {"op":"test","path":"/proof_obligations/123/status","value":"proposed"},
  {"op":"replace","path":"/round_selection/target_obligations","value":["SHELL-general-d-weighted-aggregate"]},
  {"op":"replace","path":"/round_selection/round_rule","value":"Round 46 proved exact wall normalization, wall calculus, and the strict sufficient reduction M_45.18>F_strong, but did not sign F_strong on the complete owner. Prompt C found no directed R45.18 or exact-S counterexample. By the Round-46 hard rule, pointwise Gate B is stopped and the sole next obligation is the exact weighted aggregate B_d(A)+sum_m c_{d,m}D_A(r_m)>=0, beginning with d=4, preserving exact branching weights and using no ratio ladder or additional pointwise certificate. All proof-obligation statuses remain unchanged."},
  {"op":"add","path":"/proof_obligations/99/blockers/-","value":"Round 46 proved only the strict reduction M_45.18>F_strong; F_strong remains unsigned on the complete exact owner, so the packet's hard rule stops further pointwise rounds."},
  {"op":"add","path":"/proof_obligations/99/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-r45-18-complete-owner.md"},
  {"op":"add","path":"/proof_obligations/99/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-clean-room-r45-18.md"},
  {"op":"add","path":"/proof_obligations/99/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-adversarial-r45-18-search.md"},
  {"op":"add","path":"/proof_obligations/99/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-independent-audit.md"},
  {"op":"replace","path":"/proof_obligations/99/next_action","value":"Pointwise Gate B stopped by the Round-46 hard rule. Retain the Round 36--46 pointwise reductions only as aggregate localization and falsification evidence; do not launch another pointwise owner, ratio ladder, chamber family, or certificate."},
  {"op":"replace","path":"/proof_obligations/100/blockers/0","value":"Round 46 stopped pointwise Gate B; the exact d=4 negative-support localization and weighted negative-mass comparison are not yet proved."},
  {"op":"replace","path":"/proof_obligations/100/blockers/1","value":"The d=4 cellwise branching-bonus lower bound is available as a launch lemma, but no correlated comparison with localized negative shifted tails or complete moderate-frequency audit is proved."},
  {"op":"add","path":"/proof_obligations/100/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-independent-audit.md"},
  {"op":"replace","path":"/proof_obligations/100/next_action","value":"Activated for Round 47: prove the literal d=4 weighted aggregate B_4(A)+sum_{m>=0}(m+1)D_A(m+1)>=0. First prove an intrinsic support theorem and the cellwise bonus action moment, then compare the exact weighted negative tail mass with the bonus plus retained positive tails. Preserve strict walls and exact branching weights; use no ratio ladder or additional pointwise certificate."},
  {"op":"add","path":"/proof_obligations/101/evidence/inconclusive/-","value":"human/outbox/general-d-round-46-independent-audit.md"},
  {"op":"replace","path":"/proof_obligations/101/next_action","value":"Inactive after the Round-46 hard-rule stop. Preserve the proved pointwise sector modules for use in weighted negative-support localization; do not resume pointwise assembly unless a later audited directive explicitly reopens it."}
]
```

The patch intentionally contains no operation on any `status` field.

## 8. Files modified

This audit created only

```text
human/outbox/general-d-round-46-independent-audit.md
```

No frozen Round-46 artifact, state file, proof graph, manuscript, completed
three-dimensional proof, or Round-45 artifact was edited.
