# General dimension, Round 27: combined independent audit

Date: 19 July 2026  
Status: accepted as a proved analytic reduction, one certified counterexample package, and one diagnostic-only finite scan; high-floor CST remains open

## 0. Scope and verdict

This audit independently checks only the Round 27 analytic note, its directed-Arb counterexample replay, and its hard-sector diagnostic.  It does not modify or promote any shared proof-state or workflow document.

The Round 27 package is internally consistent after one provenance correction made before this audit was finalized: an unarchived exploratory 20,000,000-point sweep claim was removed from the certified report.  The surviving numerical evidence is exactly the frozen and replayable Round 27 diagnostic: 14,106 feasible hard-sector tuples and 118,528 scalar evaluations.

No remaining algebraic, logical, certified-computation, diagnostic-scope, terminology, hash, or source-format defect was found.  The correct theorem boundary is:

1. the remainder-rich sector is closed analytically;
2. the complementary hard sector is reduced to an exact residual inequality;
3. the restricted sign of \(\mathcal C_{\max,8}\) is sufficient but is not equivalent to that exact residual;
4. neither the diagnostic scan nor the certified counterexample closes high-floor CST.

## 1. Frozen inputs and SHA256 values

The final audited inputs have the following SHA256 values:

| artifact | SHA256 |
|---|---|
| `human/outbox/general-d-round-27-remainder-rich-automatic-closure-and-hard-sector-reduction.md` | `927759184256e9f9a4a7be1ec845129e457ec8162cb5f68219bd3e2d6e812a2f` |
| `human/outbox/general-d-round-27-certified-exact-RJ-counterexample-and-loss-audit.md` | `a6cdaf56dc668896f78cd92275a017028aff4e3f6ae3a686a347871cfe5b67d4` |
| `computations/general_d_round27_exact_RJ_counterexample.py` | `35039283a81d7c95964054e319a285d7f9c87ba97689c402eeb6fefa34a3f0b4` |
| `human/outbox/general-d-round-27-hard-sector-diagnostic.md` | `7134041fab360ebb00473b443a8d1a3183708884d3ee016763385b05fa58085d` |
| `computations/general_d_round27_exact_phi_hard_sector_diagnostic.py` | `c4d77c76636c68db73f1a54a8a95a35782ebe2970ef487ee3b5afbee9fd7de90` |

Hash command:

```powershell
$files = @(
  'human/outbox/general-d-round-27-remainder-rich-automatic-closure-and-hard-sector-reduction.md',
  'human/outbox/general-d-round-27-certified-exact-RJ-counterexample-and-loss-audit.md',
  'computations/general_d_round27_exact_RJ_counterexample.py',
  'human/outbox/general-d-round-27-hard-sector-diagnostic.md',
  'computations/general_d_round27_exact_phi_hard_sector_diagnostic.py'
)
Get-FileHash -Algorithm SHA256 $files
```

## 2. Analytic audit

Put

\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p,
 \qquad E_*={1\over2}-{dm\over2p}={p-dm\over2p}.
\]

The ordinary first-drop conditions and monotonicity give
\(0\leq e_p\leq e_0<1\), hence \(E,\Delta\geq0\).  The possibly negative pair in the wall-safe Round 10 lower bound is exactly

\[
 p\left(E-{1\over2}\right)+{dm\over2}=p(E-E_*).
\]

Consequently:

- if \(p\leq dm\), then \(E_*\leq0\) and the lower bound is automatically nonnegative;
- if \(p>dm\) and \(E\geq E_*\), the same conclusion holds;
- the complementary hard sector is exactly
  \[
  p>dm,\qquad 0\leq E<E_*<\frac12.
  \]

On that hard sector, nonnegativity of the wall-safe surrogate is equivalent to the residual

\[
 \max\{0,L_T\}+a_p\Delta\geq p(E_*-E).
\]

Because the established Round 10 implication is
\(D_A(r)\geq\Phi_\delta^+\), this residual is sufficient for CST.  It is an exact sign condition for the displayed lower surrogate, not an equivalence with the actual defect \(D_A(r)\).

The elasticity refinement also checks algebraically.  With \(g=s-1\),

\[
 \Delta\geq g\left(\lambda+e_p\right)
 =g\left(\lambda+{E-\Delta\over2}\right)
\]

implies

\[
 \Delta\geq {s-1\over s+1}(E+2\lambda).
\]

Since \(\Delta\leq E\), this further gives \(E\geq(s-1)\lambda\).  Together with the retained curvature payment, \(L_0\leq\Delta\leq E<E_*\) on the hard sector.  These are valid restrictions, not asserted closures.

The dependencies used here are already recorded as `proved_internal` in `state/proof_obligations.yml`: the complete one-interface tail, shelf identities, intrinsic reduction, exact-cap repair, and curvature-cell reduction.  The live node `SHELL-general-d-high-floor-first-drop-CST` remains `open`, as it must.

## 3. Scalar terminology and implication direction

The four quantities are not interchangeable:

- \(\mathscr S=D_A(q)+R_p+dm/2\) is the exact reduced Round 20 scalar reconstructed from the literal counts and inverse fraction.
- \(\Phi_\delta\), or its wall-safe max-terminal form \(\Phi_\delta^+\), is an earlier lower surrogate for the exact defect.
- \(\mathcal R_J\) is the later exact-cap repaired lower scalar.
- \(\mathcal C_{\max,8}\) is the final \(1/8\)-cap relaxation using the literal maximum \(L_0\); it does not itself contain \(J\).

The established relations used by Round 27 are

\[
 \mathcal R_J=\mathcal C_{\max,8}+\left({1\over8}-J\right),
 \qquad J<{1\over8},
 \qquad \Phi_\delta>\mathcal R_J.
\]

Thus \(\mathcal C_{\max,8}\geq0\) on the complementary hard sector, combined with the automatic-sector proof, would be sufficient for high-floor CST.  It is strictly stronger than, and not equivalent to, the exact residual inequality.  The analytic note and both reports preserve this distinction.

## 4. Certified replay at 256, 512, and 768 bits

Commands:

```powershell
$env:GENERAL_D_ROUND27_ARB_PREC='256'
python -B computations/general_d_round27_exact_RJ_counterexample.py
$env:GENERAL_D_ROUND27_ARB_PREC='512'
python -B computations/general_d_round27_exact_RJ_counterexample.py
$env:GENERAL_D_ROUND27_ARB_PREC='768'
python -B computations/general_d_round27_exact_RJ_counterexample.py
```

All three runs completed successfully with python-flint 0.8.0 and returned the same strict classifications.  The replay verifies the exact tuple

\[
 (r,p,m,f,\alpha,t)=\left(4036,32,1,2,{1\over16},{79\over500}\right),
 \qquad \mu={65105\over16},
\]

including the integer owner, \(d=4\), both complete paired shelves, exact first drop, activity, the literal \(B_0=1\) saturated-payment cell, both members of \(L_0\), the exact cap, complete terminal count, inverse-angle bracket, and loss identity.  The certified signs are

\[
 \mathcal C_{\max,8}=-1.357650017320433\ldots<-{4\over3},
 \qquad
 \mathcal R_J=-1.232653692824895\ldots<-{6\over5},
\]

while

\[
 \mathscr S=47.1391872600721\ldots>47,
 \qquad
 \Phi_\delta=40.7976475182825\ldots>40.
\]

It also verifies \(E=1.00182478066\ldots>E_*=0.485946655063\ldots\), so the witness belongs to the automatic sector, not the complementary hard sector.  The loss ledger reconstructs terminal loss \(14.307\ldots\), shelf loss \(27.723\ldots\), total loss \(42.030\ldots\), and zero residual to directed-Arb accuracy.  Therefore this is a certified counterexample only to the two global sufficient signs, not to \(\mathscr S\), \(\Phi_\delta\), CST, or Polya.

## 5. Hard-sector diagnostic replay

Published command:

```powershell
python -B computations/general_d_round27_exact_phi_hard_sector_diagnostic.py --random 10000 --wall-limit 120
```

The replay completed successfully and matched the report:

- fixed 90-digit tuple replay: feasible and automatic, with \(\mathscr S\), \(\Phi_\delta\), \(\mathcal R_J\), \(\mathcal C_{\max,8}\), and the loss ledger agreeing with the certified package;
- Round 20 hard-edge regression: hard-sector classification retained, with \(\mathscr S=1.28429678026952\ldots\), \(\Phi_\delta=0.837805481696499\ldots\), \(\mathcal R_J=0.327937915\ldots\), and \(\mathcal C_{\max,8}=0.202968874\ldots\);
- scan scope: both owner grids, 14,106 feasible hard-sector tuples, and 118,528 scalar evaluations; the deterministic grid uses radii through \(10^4\), shelf lengths through 64, gap labels through 12, floors \(2,3,4,6\), and eight interface fractions, while 10,000 seeded log-random proposals use \(r\leq10^6\), \(p\leq1000\), \(m\leq200\), and \(f\leq16\); the implemented literal/right wall probes are retained;
- observed minima: \(\min\mathscr S=1.32628737826933\ldots\), \(\min\Phi_\delta=\min\Phi_+=0.879659219889645\ldots\), \(\min\mathcal R_J=0.0466499635531772\ldots\), and \(\min\mathcal C_{\max,8}=0.0128645720672088\ldots\);
- negative-record counts: zero for all five reported scalars.

The script uses high-precision ordinary evaluation, not interval coverage.  The report correctly labels the scan `diagnostic_only`; finite positive minima do not prove a continuum sign.

## 6. Source and formatting checks

Both Python files pass a read-only `ast.parse` check.  All five audited inputs decode as strict UTF-8, contain no NUL, replacement, or unexpected control character, have a final LF, and have balanced Markdown fences and balanced `\\(...\\)` / `\\[...\\]` delimiter counts.  The only trailing spaces are the intentional two-space Markdown line breaks after the three `Date:` lines.

Representative commands:

```powershell
python -B -c "import ast,pathlib; p=pathlib.Path(r'computations/general_d_round27_exact_RJ_counterexample.py'); ast.parse(p.read_text(encoding='utf-8'), filename=str(p)); print('AST parse OK')"
python -B -c "import ast,pathlib; p=pathlib.Path(r'computations/general_d_round27_exact_phi_hard_sector_diagnostic.py'); ast.parse(p.read_text(encoding='utf-8'), filename=str(p)); print('AST parse OK')"
```

## 7. Final classification

The Round 27 analytic note is accepted as a valid automatic-sector closure and hard-sector reduction.  The exact-RJ package is accepted as a directed-Arb certificate at its stated tuple and precision replays.  The finite scan is accepted only as reproducible theorem-design evidence.  No Round 27 result proves the residual hard sector; the next analytic obligation remains the exact residual inequality, with the restricted \(\mathcal C_{\max,8}\) sign available only as a stronger sufficient target.
