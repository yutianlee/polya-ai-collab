# General-dimensional spherical-shell Pólya project
## Adjudication of the uploaded A2 report and Round 44 Codex prompt packet

**Date:** 20 July 2026  
**Repository:** `yutianlee/polya-ai-collab`  
**Base branch:** `main`  
**Base commit:** `ce3cf00cdf82f0c9dca94177f359b8a4fbbcaab3`  
**Selected obligation:** `SHELL-general-d-high-floor-first-drop-CST`  
**Authoritative status:** `open`

The completed three-dimensional theorem remains frozen as `proved_internal`. The general-dimensional theorem remains open. The phase/branching/defect backbone is to be preserved, but its authoritative status remains `derived_under_assumptions` pending its separate frozen independent audit.

---

# 1. Adjudication of the A2 report

## 1.1 Overall evaluation

The report is useful as an advisory Gate-B design document, but its proposed Round 44 prompt should **not** be used verbatim.

Its strongest contribution is the insistence that the exact Gate-B scalar be reconstructed and falsified directly before another analytic reduction is developed. Its weakest points are status inflation, incorrect source precedence, a mechanical round budget, and a prompt that combines too many unrelated tasks.

The correct Round 44 objective is:

\[
\boxed{
\text{reconstruct the exact owner-specific Gate-B identity, expose its full loss ledger,
and adversarially test }\mathscr S\ge0
}
\]

on the single resisting one-sided upper-\(\alpha\), outer-\(B\) endpoint.

## 1.2 Useful points retained

The following points are adopted.

1. **Gate A is correctly stopped.**  
   Round 43 proved that the compressed count-phase/radial route cannot be continued globally without a forbidden \(f/B/j\)-indexed wall analysis. Gate B is therefore active.

2. **The unrenamed exact target must be tested directly.**  
   The primary object is
   \[
   \mathscr S
   =
   D_A(q)+R_p+\frac{d_\rho m}{2}
   =
   D_A(q)+\mathcal C_p+p(E-E_*).
   \]
   A negative projected scalar is not a negative \(\mathscr S\).

3. **Falsification should precede another proof campaign.**  
   A directed-arithmetic, exact-owner point with \(\mathscr S<0\) is a valid Gate-B stop trigger. A finite positive sweep is diagnostic only.

4. **The full Round 43 owner must be implemented verbatim.**  
   The common shelf, literal first drop, hard inequality \(E<E_*\), activity, parity grid, one-sided outer wall, and all inverse-wall ownership data must be checked together.

5. **The exact shelf trapezoid should be restored.**  
   The identities
   \[
   \mathcal C_p
   =
   -\int_0^p u(p-u)A''(r+u)\,du
   =
   2\int_r^{r+p}A(z)\,dz
   -p\bigl(A(r)+A(r+p)\bigr)
   \]
   are the correct starting point.

6. **The elementary curvature reserve is worth proving.**  
   On \(r<r+p<q<\mu<K\),
   \[
   -A''(z)
   =
   \frac1\pi
   \left(
   \frac1{\sqrt{\mu^2-z^2}}
   -
   \frac1{\sqrt{K^2-z^2}}
   \right)
   \]
   is increasing, and therefore
   \[
   \mathcal C_p
   \ge
   \frac{p^3}{6\pi}
   \left(
   \frac1{\sqrt{\mu^2-r^2}}
   -
   \frac1{\sqrt{K^2-r^2}}
   \right).
   \]
   This is a candidate lemma until re-derived and audited.

7. **One-sided endpoint bookkeeping is load-bearing.**  
   The gap-side label \(B\) and the literal strict bracket \(B-1\) must not be conflated.

## 1.3 Points retained only after correction

### A. Exact \(\alpha\uparrow1^-\) treatment

The report says never to evaluate at \(\alpha=1\). That is too strong.

For the analytic endpoint, it is legitimate and preferable to use the exact limit geometry

\[
\mu=q+1
\]

together with the one-sided gap labels. What is forbidden is silently replacing the one-sided owner by the next chart’s literal \(\alpha=0\) owner.

For diagnostics approaching the endpoint, solve the outer-wall equation separately at each

\[
\alpha=1-10^{-j}.
\]

Do not hold \(t\) fixed while changing \(\alpha\).

### B. Terminal reserve bookkeeping

The report proposes a generic identity involving \(D_A(q)-\max\{0,L_T\}\). On the resisting outer-\(B\) endpoint this is insufficiently precise because two terminal decompositions coexist:

- the **gap-side limiting decomposition**, with one-sided label \(B\);
- the **literal-wall decomposition**, with strict bracket \(B-1\) and a nonzero top triangle.

Round 44 must derive both and reconcile them exactly before using either.

### C. Gate-B duration

The report proposes a fixed three-round budget. The binding strategy explicitly rejects elapsed-round stop rules. Continue or stop only under the mathematical Gate-B criteria:

1. a certified exact feasible point has \(\mathscr S<0\); or
2. possible negativity cannot be localized by one intrinsic shelf-terminal theorem without forbidden count, ratio, floor, or chamber splitting.

## 1.4 Points rejected

The following points are not adopted.

1. **Status inflation.**  
   The general-dimensional phase/branching/defect backbone is not `proved_internal`; it remains `derived_under_assumptions`.

2. **“Effectively closed” language for Round 41.**  
   Round 41 remains a computer-assisted candidate only. The endpoint is not mathematically closed in the live proof graph.

3. **Automatic certificate consolidation before Gate C.**  
   Consolidation is a separate human governance and verification task. It is not a substitute for the approved Gate-B/Gate-C decision rule and is off the critical Round 44 path.

4. **Hash re-pinning and d=3 release work inside Round 44.**  
   Mounted-export hash drift is not the selected mathematical obligation. Repository hygiene and d=3 external-review work should be handled separately.

5. **Replaying every historical regression in the same round.**  
   Only regressions directly capable of detecting reuse of a rejected scalar or an owner error are mandatory.

6. **A mandatory Gate-C warm start regardless of the Gate-B result.**  
   This broadens the round. Gate C is activated only by the approved stop criteria.

7. **Treating the manuscript as authoritative when it conflicts with state.**  
   `state/proof_obligations.yml` and the binding strategies have precedence. The manuscript is a notation source only where it agrees with the higher-precedence record.

8. **Allowing \(m=0\) in the high-floor first-drop search.**  
   Here \(m=n-p\ge1\).

9. **Making `general-d-strategy_r2.md` override the simplified strategy.**  
   The approved completion instruction refines the simplified strategy; it does not supersede the authoritative source order.

---

# 2. Shared source precedence for all Round 44 prompts

Read and obey sources in this order.

1. `state/proof_obligations.yml`
2. `human/inbox/general-d_simplified_analytic_strategy.md`
3. `human/inbox/general-d-strategy_r2.md`
4. the newest independently audited Round 38–43 artifacts
5. `human/current_directives.md`
6. `state/current_state.md`
7. `state/gap_register.md`
8. exact lemma packets and replay files
9. `manuscript/spherical-shell-polya-general-d.tex`
10. the uploaded A2 report, as advisory material only

Explicitly report every conflict. Do not silently combine incompatible versions.

No Round 44 agent may promote the general-dimensional theorem or the backbone status.

---

# 3. Prompt A — Lead Round 44 reasoning

## Round 44: exact Gate-B terminal/trapezoid reconstruction and falsification gate

### 3.1 Repository and branch

Work from:

```text
repository: yutianlee/polya-ai-collab
base branch: main
base commit: ce3cf00cdf82f0c9dca94177f359b8a4fbbcaab3
working branch: codex/general-d-round-44-exact-gate-b
```

Record the base commit before any derivation. If `main` has moved, stop and report the new SHA before proceeding.

### 3.2 Mandatory files

Read:

```text
state/proof_obligations.yml
human/inbox/general-d_simplified_analytic_strategy.md
human/inbox/general-d-strategy_r2.md
human/current_directives.md
state/current_state.md
state/gap_register.md
state/lemma_bank.md

human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md
human/outbox/general-d-round-27-remainder-rich-automatic-closure-and-hard-sector-reduction.md
human/outbox/general-d-round-36-exact-count-gap-collision-reduction.md
human/outbox/general-d-round-37-gap-interface-synchronization-and-root-free-gate.md
human/outbox/general-d-round-38-gap-position-count-phase-and-face-compensation.md
human/outbox/general-d-round-38-independent-audit.md
human/outbox/general-d-round-39-outer-face-floor-elimination-and-cap-sharpening.md
human/outbox/general-d-round-39-independent-audit.md
human/outbox/general-d-round-42-stronger-upper-alpha-phi-specialization.md
human/outbox/general-d-round-42-independent-audit.md
human/outbox/general-d-round-43-hard-remainder-isolation-and-gate-a-stop.md
human/outbox/general-d-round-43-independent-audit.md

computations/general_d_round42_stronger_phi_replay.wl
computations/general_d_round43_hard_remainder_replay.wl

manuscript/spherical-shell-polya-general-d.tex
```

Use the manuscript only for definitions that agree with the higher-precedence files.

### 3.3 Exact scope

Work only on the resisting one-sided upper-\(\alpha\), outer-\(B\) endpoint of the hard one-level gap.

Put

\[
x=r+p,\qquad
q=x+m,\qquad
\mu=q+1,\qquad
K=\mu\sec t,\qquad
0<t<\frac\pi2,
\]

\[
d_\rho=1-\frac{2t}{\pi},
\qquad
\zeta=\frac{\pi}{2t}-1.
\]

Use

\[
G_a(z)
=
\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
\qquad
A(z)=G_K(z)-G_\mu(z).
\]

The one-sided outer-wall data are

\[
G_K(q)=B-\frac14,
\qquad
B_0=B-1\ge1,
\]

\[
0<h<u<\beta<\frac12,
\qquad
h=G_\mu(q),
\qquad
\beta=\frac1\pi\arccos\frac qK.
\]

Here \(B\) is the gap-side label. The literal strict outer-ball bracket at the wall is

\[
B_{\rm lit}
=
\left[G_K(q)+\frac14\right]_{<}
=
B-1
=
B_0.
\]

The shell terminal count is also

\[
Q
=
\left[A(q)+\frac14\right]_{<}
=
B_0.
\]

Let the common first-shelf floor be \(f\), with

\[
j=f-B\ge0,
\qquad
n=f-1=B_0+j.
\]

Use the literal first-shelf and first-drop conditions

\[
\left\lfloor A(r)+\frac14\right\rfloor
=
\left\lfloor A(x)+\frac14\right\rfloor
=f,
\]

\[
\left\lfloor A(x+1)+\frac14\right\rfloor
\ne f.
\]

Define

\[
e_0=A(r)+\frac14-f,
\qquad
e_p=A(x)+\frac14-f,
\]

\[
E=e_0+e_p,
\qquad
\Delta=e_0-e_p,
\qquad
a_p=\frac{p^2}{3(2r+p)},
\]

\[
E_*=\frac{p-d_\rho m}{2p}.
\]

Retain the exact hard owner

\[
p\ge3,\qquad
m\ge1,\qquad
p>d_\rho m,\qquad
0\le E<E_*<\frac12,
\]

the Round 39 closure

\[
p-d_\rho m>\frac{11}{5},
\qquad q\ge5,
\]

the dimension-labelled activity condition, and both extension grids

\[
r\in\mathbb N,\ r\ge1,
\qquad\text{or}\qquad
r\in\mathbb N_0+\frac12,\ r\ge\frac32.
\]

### 3.4 Primary proof obligation

The only primary sign target is

\[
\boxed{
\mathscr S
=
D_A(q)+R_p+\frac{d_\rho m}{2}
=
D_A(q)+\mathcal C_p+p(E-E_*)
\ge0.
}
\]

Equivalently,

\[
\boxed{
D_A(q)+\mathcal C_p
\ge
p(E_*-E).
}
\]

Do not rename this target.

### 3.5 Required exact reconstruction

#### A. Shelf identity and curvature reserve

Derive from the definitions:

\[
R_p
=
\mathcal C_p+p\left(E-\frac12\right),
\]

\[
\mathcal C_p
=
-\int_0^p u(p-u)A''(r+u)\,du,
\]

\[
\mathcal C_p
=
2\int_r^x A(z)\,dz
-p\bigl(A(r)+A(x)\bigr).
\]

Prove on the exact owner:

\[
A'(z)<0,\qquad A''(z)<0,\qquad (-A'')'(z)>0
\quad(r\le z\le x),
\]

and hence

\[
\boxed{
\mathcal C_p
\ge
\frac{p^3}{6\pi}
\left(
\frac1{\sqrt{\mu^2-r^2}}
-
\frac1{\sqrt{K^2-r^2}}
\right)>0.
}
\]

Reconstruct the inherited proof of

\[
\mathcal C_p\ge a_p\Delta.
\]

Print its complete loss ledger. If the inherited proof does not supply a single exact remainder formula, list each inequality and the exact nonnegative difference introduced at that line.

#### B. Owner-specific terminal decompositions

Start from the exact Round 10 layer-cake proof, not from the final inequality alone.

Let \(\mathcal R_{\rm tan}\) denote the exact sum of tangent/Bregman remainders appearing in the Round 10 loss ledger. Derive two decompositions of the same terminal defect.

Define

\[
\Omega_-
=
\sum_{k=1}^{B_0}
\left(
\frac{\pi}{2\theta_k}
-\frac{\pi}{2t}
+2\eta_k
\right),
\]

and

\[
J=2\int_q^\mu G_\mu(z)\,dz.
\]

1. **Gap-side limiting decomposition.**  
   Retain the one-sided label \(B\), the newest inverse level \(y_B\downarrow0\), and the gap-side count surplus \(B-Q=1\). Prove

   \[
   \boxed{
   L_T^+
   =
   \Omega_-+B_0\zeta+\frac1{2\beta}-J.
   }
   \]

   Derive an exact nonnegative remainder \(\mathcal R_{\rm tan}^+\) such that

   \[
   \boxed{
   D_A(q)=L_T^++\mathcal R_{\rm tan}^+.
   }
   \]

2. **Literal-wall decomposition.**  
   Use the literal strict bracket \(B_{\rm lit}=B_0\), \(Q=B_0\), and the top interval

   \[
   G_K(q)-B_0=\frac34.
   \]

   Prove

   \[
   \boxed{
   L_T^0
   =
   \Omega_-+B_0\zeta+\frac9{16\beta}-J.
   }
   \]

   Derive an exact nonnegative remainder \(\mathcal R_{\rm tan}^0\) such that

   \[
   \boxed{
   D_A(q)=L_T^0+\mathcal R_{\rm tan}^0.
   }
   \]

3. **Reconciliation.**  
   Prove directly that

   \[
   \boxed{
   \mathcal R_{\rm tan}^+
   =
   \mathcal R_{\rm tan}^0+\frac1{16\beta}.
   }
   \]

   This is an ownership reconciliation, not a new reserve manufactured by changing owners.

Every integral defining \(\mathcal R_{\rm tan}^\pm\) must be printed. Do not hide it behind “convexity slack.”

#### C. Exact Gate-B ledger

Prove the two exact identities

\[
\boxed{
\mathscr S
=
L_T^+
+\mathcal R_{\rm tan}^+
+\mathcal C_p
+p(E-E_*),
}
\]

\[
\boxed{
\mathscr S
=
L_T^0
+\mathcal R_{\rm tan}^0
+\mathcal C_p
+p(E-E_*).
}
\]

Then simplify the exact Round 42 endpoint identity to

\[
\Phi_\delta^+
=
L_T^+
+a_p\Delta
+p(E-E_*).
\]

Deduce and verify algebraically

\[
\boxed{
\mathscr S-\Phi_\delta^+
=
\mathcal R_{\rm tan}^+
+\bigl(\mathcal C_p-a_p\Delta\bigr)
}
\]

and equivalently

\[
\boxed{
\mathscr S-\Phi_\delta^+
=
\frac1{16\beta}
+\mathcal R_{\rm tan}^0
+\bigl(\mathcal C_p-a_p\Delta\bigr).
}
\]

This is the required exact loss ledger. If any formula conflicts with the audited Round 42 notation, stop and report the conflict rather than forcing an identification.

#### D. One intrinsic sign attempt

Use the exact identity, with all correlations retained, to attempt

\[
\Omega_-+B_0\zeta+\frac9{16\beta}-J
+\mathcal R_{\rm tan}^0+\mathcal C_p
\ge
p(E_*-E).
\]

Do not replace it by a new named projected scalar.

Allowed outcomes are:

- a complete analytic proof on the entire owner;
- one intrinsic localization theorem for every possible negative point;
- a certified exact negative point;
- a precise failure report identifying why one intrinsic theorem cannot localize possible negativity.

Do not split by \(B_0\), \(j\), \(f\), shell-ratio intervals, or a chamber list.

### 3.6 Allowed techniques

Allowed:

- exact layer cake;
- inverse-action coordinates;
- Stieltjes integration by parts;
- supporting-tangent/Bregman remainders;
- exact integration by parts for \(\mathcal C_p\);
- monotonicity and convexity of \(G_a\), \(A\), and inverse actions;
- exact floor and phase equations;
- one intrinsic continuous normalization;
- symbolic replay of printed algebra;
- high-precision and directed arithmetic for falsification.

### 3.7 Forbidden and exhausted approaches

Do not:

1. repair \(\mathcal T_{42}\);
2. return to \(\mathcal R_*\), \(\Gamma_{\rm OB}\), \(\Gamma_{\rm gap}\), \(Q_0\), or \(Q_{\rm exact}\) as primary targets;
3. use the Round 41 Bernstein table as a proof premise;
4. introduce a theorem family indexed by \(B_0\), \(B\), \(j\), \(f\), \(Q\), or ratio intervals;
5. introduce a new chamber certificate or positive-direction coverage certificate;
6. assume global \(\alpha\)-monotonicity;
7. replace \(D_A(q)\) at the outset by a lower terminal skeleton;
8. replace \(\mathcal C_p\) at the outset by \(a_p\Delta\);
9. discard inverse fractions, the exact cap, the top interval, \(e_p\), or the actual \(E\);
10. identify the upper-\(\alpha\) gap-side endpoint with the next literal \(\alpha=0\) chart;
11. modify `state/proof_obligations.yml` or the manuscript.

### 3.8 Equality and ownership audit

Handle explicitly:

- \(A(r+s)+1/4\in\mathbb Z\);
- \(G_K(q)+1/4=B\in\mathbb Z\);
- \(A(q)+1/4\in(B-1,B)\);
- old inverse spatial walls \(y_k\in\mathbb Z\);
- \(\eta_k=1\) on a literal inverse wall;
- \(\eta_k\downarrow0\) on the adverse side;
- \(e_p=0\);
- \(E=E_*\);
- the curvature/elasticity switch;
- \(B_0=1\);
- both parity grids;
- the dimension-labelled activity equality face;
- the distinction between gap-side and literal outer-wall decompositions.

Do not use continuity across a shelf-floor jump.

### 3.9 Required falsification work

Build an independent high-precision evaluator from the exact definitions of \(D_A(q)\), \(\mathcal C_p\), and the strict counts.

For exact endpoint data:

\[
\mu=q+1,
\]

and solve

\[
G_{\mu\sec t}(q)=B-\frac14
\]

for \(t\) with verified bracketing.

For one-sided convergence checks, use

\[
\alpha=1-10^{-j}
\]

and solve the outer-wall equation separately for each \(\alpha\).

Search both grids with

\[
p\ge3,\qquad m\ge1,\qquad q\ge5,
\qquad p-d_\rho m>\frac{11}{5}.
\]

Every retained point must pass all owner tests.

Mandatory regressions:

1. Reproduce the Round 43 record
   \[
   (r,p,m,f,B,j)=(1,9,9,4,3,1)
   \]
   and reject it because \(E>E_*\).

2. Reproduce the Round 27 automatic-sector witness and verify that negative rejected scalars coexist with large positive \(\mathscr S\).

3. Verify numerically the two terminal decompositions and the relation
   \[
   \mathcal R_{\rm tan}^+
   -
   \mathcal R_{\rm tan}^0
   =
   \frac1{16\beta}.
   \]

4. Verify the curvature reserve against the exact \(\mathcal C_p\).

At every point record separately:

\[
D_A(q),\quad
L_T^+,\quad
L_T^0,\quad
\mathcal R_{\rm tan}^+,\quad
\mathcal R_{\rm tan}^0,
\]

\[
\mathcal C_p,\quad
a_p\Delta,\quad
p(E_*-E),\quad
\Phi_\delta^+,\quad
\mathscr S.
\]

A floating-point negative is diagnostic only. A Gate-B stop requires directed verification of:

- the wall root;
- every strict owner condition;
- the exact count;
- \(\mathscr S<0\).

No positive coverage certificate is authorized.

### 3.10 Success, partial-success, and stop criteria

#### Success

Prove analytically

\[
\mathscr S\ge0
\]

on the entire one-sided upper-\(\alpha\), outer-\(B\) owner, with every wall assigned.

#### Partial success

Prove the exact owner-specific terminal identities and the exact Gate-B loss ledger, and localize every possible negative point by one intrinsic condition that does not introduce a forbidden split.

#### Gate-B stop

Recommend Gate C if either:

1. a directed exact-feasible point has \(\mathscr S<0\); or
2. possible negativity cannot be localized by one intrinsic shelf-terminal theorem without forbidden count, ratio, floor, or chamber splitting.

Do not use elapsed rounds as a stop rule.

### 3.11 Required outputs

Create:

```text
human/outbox/general-d-round-44-exact-gate-b-terminal-trapezoid-reconstruction.md
computations/general_d_round44_exact_gate_b_replay.wl
computations/general_d_round44_exact_gate_b_diagnostic.py
```

The reasoning note must contain:

1. theorem boundary;
2. exact notation and owner;
3. line-by-line derivations;
4. terminal ownership reconciliation;
5. shelf and terminal loss ledgers;
6. equality-face table;
7. falsification report;
8. separation of proved, conditional, diagnostic, and failed statements;
9. explicit Gate-B/Gate-C decision;
10. all modified files;
11. final commit SHA.

Do not edit:

```text
state/proof_obligations.yml
manuscript/spherical-shell-polya-general-d.tex
```

---

# 4. Prompt B — Clean-room reconstruction

## Round 44B: independent owner-specific terminal and shelf reconstruction

Do not read the lead Round 44 note before completing Sections 1–5 of your own report.

Read only:

```text
state/proof_obligations.yml
human/inbox/general-d_simplified_analytic_strategy.md
human/inbox/general-d-strategy_r2.md
human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md
human/outbox/general-d-round-38-gap-position-count-phase-and-face-compensation.md
human/outbox/general-d-round-42-stronger-upper-alpha-phi-specialization.md
human/outbox/general-d-round-43-hard-remainder-isolation-and-gate-a-stop.md
```

Independently reconstruct:

1. the exact strict terminal count at the outer wall;
2. \(B_{\rm lit}=B-1=Q\);
3. the gap-side limiting terminal decomposition;
4. the literal-wall top-triangle decomposition;
5. both tangent-remainder integrals;
6. the relation
   \[
   \mathcal R_{\rm tan}^+
   =
   \mathcal R_{\rm tan}^0+\frac1{16\beta};
   \]
7. the two exact representations of \(\mathscr S\);
8. the exact difference \(\mathscr S-\Phi_\delta^+\);
9. the identities and sign of \(\mathcal C_p\);
10. the elementary curvature reserve.

Audit every strict bracket and endpoint label. In particular, determine whether the exact endpoint may be evaluated at \(\mu=q+1\) while retaining a one-sided owner label.

After the clean-room derivation is complete, compare it with the lead note and list every discrepancy.

Output:

```text
human/outbox/general-d-round-44-clean-room-gate-b-reconstruction.md
```

Allowed verdicts:

- `PASS`;
- `PASS WITH MINOR REPAIRS`;
- `STRUCTURAL PASS — FINAL SIGN OPEN`;
- `INCOMPLETE`;
- `FAIL`;
- `FALSIFIED`.

Do not modify state or manuscript files.

---

# 5. Prompt C — Adversarial exact-scalar falsification

## Round 44C: independent Gate-B counterexample search

Implement the exact definitions independently of the lead evaluator.

The search target is only

\[
\mathscr S
=
D_A(q)+\mathcal C_p+p(E-E_*).
\]

Do not search for a negative projected scalar as a substitute.

Requirements:

1. Solve the outer-wall equation with verified bracketing.
2. Enforce \(m\ge1\).
3. Enforce both parity grids.
4. Enforce the exact common shelf and first drop.
5. Enforce the dimension-labelled activity condition.
6. Enforce \(E<E_*\), \(p>d_\rho m\), \(p-d_\rho m>11/5\), and \(q\ge5\).
7. Distinguish literal and adverse old-inverse sides.
8. Keep the upper-\(\alpha\) endpoint separate from a literal \(\alpha=0\) chart.
9. Evaluate the direct strict count defining \(D_A(q)\), not only a tangent lower bound.
10. Record the complete exact loss ledger.

Search especially near:

\[
B_0=1,
\qquad
e_p\downarrow0,
\qquad
E\uparrow E_*,
\qquad
\eta_k\downarrow0,
\]

small \(m\), large \(p\), and collisions of the hard seam with another literal wall.

If a stable negative is found, produce a directed interval enclosure verifying the entire owner and \(\mathscr S<0\). Classify it as a `gate_trigger_certificate`, not as a proof premise.

If no negative is found, report only diagnostic minima and the observed division of payment between

\[
D_A(q),\qquad
\mathcal C_p,\qquad
\mathcal R_{\rm tan}^{\pm}.
\]

Output:

```text
human/outbox/general-d-round-44-adversarial-exact-scalar-falsification.md
computations/general_d_round44_independent_gate_b_search.py
```

No positive coverage certificate is permitted.

---

# 6. Prompt D — Independent audit after Round 44

## Independent audit of Round 44

Audit the lead note, clean-room reconstruction, symbolic replay, and adversarial search.

The audit must answer:

1. What exact identity was proved?
2. Was the gap-side/literal-wall terminal reconciliation correct?
3. Were strict brackets and one-sided labels assigned correctly?
4. Is every tangent or curvature remainder displayed with a valid sign?
5. Does the identity for \(\mathscr S-\Phi_\delta^+\) follow from the exact definitions?
6. Did any step reuse an exhausted projected scalar?
7. Did the proof separate correlated quantities before justifying the loss?
8. Were diagnostics and directed certificates classified correctly?
9. Was a negative point verified on the full exact owner?
10. Does Gate B continue, close, or stop under the approved mathematical criteria?

Use one verdict:

- `PASS`;
- `PASS WITH MINOR REPAIRS`;
- `STRUCTURAL PASS — FINAL SIGN OPEN`;
- `COMPUTER-ASSISTED CANDIDATE ONLY`;
- `INCOMPLETE`;
- `FAIL`;
- `FALSIFIED`.

State:

- what was actually proved;
- what remains open;
- the first unrepaired logical gap;
- every strictness or ownership error;
- whether computation is diagnostic or certified;
- recommended proof-obligation updates;
- the next single proof obligation.

Unless the endpoint is completely proved and independently audited, keep

```text
SHELL-general-d-high-floor-first-drop-CST: open
TARGET-shell-general-d: proposed/open
```

and do not promote the general-dimensional backbone.

Output:

```text
human/outbox/general-d-round-44-independent-audit.md
```

---

# 7. Conditional next obligation

Do not execute this section until the Round 44 audit is complete.

- If Round 44 proves the endpoint, the next obligation is the exact terminal decomposition on higher \(Q_N\) faces \(N\ge2\), re-derived without importing the one-level-gap formula.

- If Round 44 gives a single intrinsic negative-support localization, the next obligation is to sign \(\mathscr S\) on exactly that localized support.

- If Round 44 triggers a Gate-B stop, the next obligation is Gate C in dimension four:
  localize every possibly negative shift and compare its weighted mass with a quantitative lower bound for the branching bonus.
