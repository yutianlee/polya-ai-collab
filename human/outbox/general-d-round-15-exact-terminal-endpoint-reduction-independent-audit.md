# General dimension, Round 15: independent audit of the exact-terminal endpoint reduction

Date: 18 July 2026

Verdict: **PASS**.  No blocking mathematical, wall-ownership, or diagnostic-reproducibility defect was found.  The endpoint sign \(\Omega_{\rm end}\ge0\) remains an open lemma, exactly as stated in the audited note.

## Frozen artifacts

- Audited note: `human/outbox/general-d-round-15-exact-terminal-endpoint-reduction.md`
- Audited-note SHA-256: `82e13b290ba24c482368544ba9ff1ab03a18d282a297873b0bb8b7ae0ba6cfd0`
- Replayed evaluator: `computations/general_d_round15_exact_terminal_endpoint_probe.wl`
- Evaluator SHA-256: `261afee87abaf64e3d969bdc57ef0b39671a5a4efbc82546a6caae99509b0ee5`

The audited note was not edited during this audit.

## Mathematical checks

1. **Exact terminal count.**  Since \(q+j>q+\alpha=\mu\) for every positive integer \(j\), the inner action vanishes at all positive terminal samples.  With \(B=1\), their strict floors equal one precisely when \(q+j<z\), or \(j<y\).  The number of positive integers satisfying this is \(M=[y]_<\), including \(M=m-1\) at literal integral \(y=m\).  Together with the endpoint contribution \(Q=1\), this gives the claimed
   \[
   T_A(q)=1+2M.
   \]

2. **S4 combination.**  On the original open chamber \(\chi_q=0\).  Substituting the exact terminal defect and
   \(H_n=2\int_r^q(A-1)\) into S4 cancels both intermediate tail integrals and yields
   \[
   D_A(r)=2J_K(r)-2J_{q+\alpha}(r)-(1+2n+2M)=\Omega(\alpha).
   \]
   The equivalent direct count \(T_A(r)=1+2n+2M\) is consistent with the ordinary first-shelf convention; on the original hard chamber no earlier sample can be an ambiguous strict-floor wall while its ordinary floor remains one.

3. **Strict monotonicity.**  Differentiation under the integral is valid because \(q+\alpha>r\) and \(G_a(a)=0\).  The displayed formula
   \[
   \frac{d}{da}J_a(r)=\frac{a}{2\pi}
   \left(\arccos\frac ra-\frac ra\sqrt{1-r^2/a^2}\right)>0
   \]
   is correct.  Hence \(\Omega'(\alpha)<0\), and every original phase-, branch-, and activity-admissible point satisfies \(\alpha<\bar\alpha\).  Crossing an artificial shelf wall does not affect this comparison of the explicit scalar.

4. **Relation to Round 14.**  On the original chamber,
   \(\Omega-\Xi=D_A(q)-L_{\rm ex}\ge0\).  The exact cap and exact head cancel, so the difference is precisely the nonnegative outer inverse-tangent gap.  Thus \(\Omega_{\rm end}\ge0\) is correctly described as weaker than \(\Xi_{\rm end}\ge0\).

## Equality faces and dimensional ownership

- At an inverse wall \(y=m\), strict ownership gives \(M=m-1\) and \(\eta=1\); the right-hand open cell has \(M=m\) and is less favorable by two units.
- At the lower action wall, \((Q,\chi_q)\) changes from \((1,0)\) to \((0,1)\).  The terminal defect gains one unit and S4 gains one unit, so the literal defect is \(\Omega(\alpha_*)+2\).
- \(\alpha=1\) and \(\alpha=\alpha_{\rm act}\) are correctly used only as one-sided limits.  At the literal branch wall the definition of \(n\) changes.
- Interface samples have zero inner action, and a sample at \(K\) is absent under the strict bracket.
- The imported owner calculation uses
  \[
  \kappa_4=\frac34\quad\text{on the integer grid},
  \qquad
  \kappa_5=2\quad\text{on the half-integer grid},
  \]
  exactly as required.  Higher-dimensional activity walls occur no later than the owner wall, so the owner endpoint is the adverse one for the decreasing scalar.

## Diagnostic replay

Wolfram Language 15.0 replay completed successfully and printed `round15ReplayOK=True`.  The independently observed gates agree with the note and evaluator:

- 3,171 hard extension-grid records;
- 0 negative correct endpoints;
- 0 negative outer tangent gaps;
- owner counts \(605\) phase, \(2432\) branch, and \(134\) activity;
- 16 negative deliberately overextended full-phase records;
- sampled correct-owner minima \(0.65614112736\ldots\), \(0.92722743121\ldots\), and \(0.75072180039\ldots\);
- large-\(q\) replay \(45.23919157837\ldots\).

The evaluator's additional floor-free diagnostic has sampled minimum \(0.354703412962\ldots>1/3\).  Its regression gate is consistent with that value in the frozen evaluator.  All numerical claims are explicitly and correctly qualified as seeded high-precision evidence, not interval enclosures or coverage proofs.

## Boundary of the PASS

This audit validates the exact identity, endpoint reduction, owner and wall conventions, and the reproducibility of the stated diagnostics.  It does **not** prove \(\Omega_{\rm end}\ge0\), close the first-floor branch, or prove the all-dimensional theorem.
