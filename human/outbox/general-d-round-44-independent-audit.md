# General-dimensional spherical-shell Pólya project
## Independent audit of Round 44 exact Gate-B reconstruction

**Date:** 20 July 2026  
**Required base:** `ce3cf00cdf82f0c9dca94177f359b8a4fbbcaab3`  
**Audited branch:** `codex/general-d-round-44-exact-gate-b`  
**Verdict:** **STRUCTURAL PASS — FINAL SIGN OPEN**

## 0. Boundary, independence, and audit basis

The branch head and merge base were both the required base SHA before the
Round 44 files were committed. The authoritative proof-obligation file still
has SHA-256

~~~text
a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4
~~~

and was not edited during this audit.

I audited the Round 44 prompt, lead reconstruction, frozen clean-room
reconstruction and post-freeze comparison, Mathematica replay, primary Python
diagnostic, independent adversarial script and report, and the relevant exact
sources from Rounds 10, 38, 42, and 43 together with their audits. I also
checked the current directives, state summary, gap register, lemma bank, and
the authoritative statuses in `state/proof_obligations.yml`.

The source-order conflicts are resolved correctly:

1. the proof graph's narrative next action still points to the older Round 37
   projection, while the newer audited Round 43 result stops Gate A and
   activates Gate B; the authoritative `open`/`proposed` statuses agree, and
   the direct Round 44 instruction selects Gate B;
2. Round 10's radial count
   \(n_{10}=\lfloor\mu-r\rfloor\) equals \(p+m\) on the gap side
   \(0<\alpha<1\), but its literal value at \(\mu=q+1\) is \(p+m+1\);
   the later synchronized count coordinate
   \(n_{\rm cnt}=f-1=B_0+j\) is a different quantity and is never substituted
   for \(n_{10}\);
3. Round 10's \(B\) is a literal strict bracket, while Round 44's \(B\) is
   the one-sided gap label. Round 44 consistently writes
   \(B_{\rm lit}=B-1=B_0\).

This audit proves no endpoint sign and promotes no theorem. The authoritative
boundary remains

~~~text
SHELL-general-d-high-floor-first-drop-CST: open
SHELL-general-d-branching-backbone: derived_under_assumptions
SHELL-general-d-weighted-aggregate: proposed
TARGET-shell-general-d: proposed
~~~

## 1. Answers to the ten required audit questions

### 1. What exact identity was proved?

The shelf calculation is exact:

\[
 R_p=\mathcal C_p+p\left(E-\frac12\right),
\]

\[
 \mathcal C_p
 =-\int_0^p u(p-u)A''(r+u)\,du
 =2\int_r^{r+p}A(z)\,dz-p\{A(r)+A(r+p)\}.
\]

For a fixed old-inverse side vector, the terminal defect has the two exact
representations

\[
 D_A(q)=L_T^++\mathcal R_{\rm tan}^+
        =L_T^0+\mathcal R_{\rm tan}^0,
\]

where

\[
 L_T^+=\Omega_-+B_0\zeta+\frac1{2\beta}-J,
 \qquad
 L_T^0=\Omega_-+B_0\zeta+\frac9{16\beta}-J.
\]

Consequently the unrenamed Gate-B scalar satisfies both exact identities

\[
 \boxed{
 \mathscr S=L_T^++\mathcal R_{\rm tan}^+
 +\mathcal C_p+p(E-E_*)}
\]

and

\[
 \boxed{
 \mathscr S=L_T^0+\mathcal R_{\rm tan}^0
 +\mathcal C_p+p(E-E_*)}.
\]

The audited Round 42 endpoint scalar simplifies exactly to

\[
 \Phi_\delta^+=L_T^++a_p\Delta+p(E-E_*),
\]

so the complete loss identity is

\[
 \boxed{
 \mathscr S-\Phi_\delta^+
 =\mathcal R_{\rm tan}^++(\mathcal C_p-a_p\Delta)}
\]

and equivalently

\[
 \boxed{
 \mathscr S-\Phi_\delta^+
 =\frac1{16\beta}+\mathcal R_{\rm tan}^0
  +(\mathcal C_p-a_p\Delta)}.
\]

The lead and clean-room derivations agree on every term in these formulas.

### 2. Was the gap-side/literal-wall reconciliation correct?

Yes. Let

\[
 v=G_K(q)=B_0+\frac34,
 \qquad
 Y(\ell)=|\{s\ge0:G_K(q+s)>\ell\}|,
\]

with the convex zero extension \(Y(\ell)=0\) for \(\ell\ge v\). The endpoint
tangent is \(\Lambda_v(\ell)=(v-\ell)/\beta\). The old-level Bregman
integrals are identical in the two owners, while the gap-side remainder has
the additional interval \([v,B_0+1]\). Therefore

\[
 \begin{aligned}
 \mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0
 &=2\int_v^{B_0+1}\frac{\ell-v}{\beta}\,d\ell\\
 &=\frac{(B_0+1-v)^2}{\beta}
 =\frac1{16\beta}.
 \end{aligned}
\]

At the same time
\(L_T^0-L_T^+=1/(16\beta)\), so both sides reconstruct the same defect.
This is a transfer between two owner ledgers, not a new reserve created by
changing owners.

### 3. Were strict brackets and one-sided labels assigned correctly?

Yes, after the final explicit side-vector repair.

- At the outer wall,
  \[
  B_{\rm lit}=[G_K(q)+1/4]_<=[B]_< =B-1=B_0.
  \]
- Since \(A(q)+1/4=B-h\in(B-1,B)\), the shell count is literally
  \(Q=B_0\).
- The gap-side ball owner retains label \(B\), newest displacement
  \(y_B\downarrow0\), and surplus \(B-Q=1\). The literal owner excludes
  that level and retains the \(3/4\)-length top interval.
- At an old inverse wall \(y_k=N\), the literal value is
  \([y_k]_< =N-1\), \(\eta_k^{\rm lit}=1\); the adverse outer-gap limit has
  selected count \(N\), \(\eta_k^-=0\), and lowers \(D_A\) by exactly two.
  The lead now fixes one old-level side vector consistently in \(D_A\),
  \(\Omega_-\), and both terminal decompositions.
- The newest \(y_B=0\) event is counted once as the outer-action jump and is
  not treated as an old inverse collision.
- The endpoint geometry is legitimately evaluated at \(\mu=q+1\) while the
  old chart's one-sided label is retained. It is not reindexed as the next
  literal \(\alpha=0\) chart.

Shelf-floor equality, \(e_p=0\), \(E=E_*\), \(B_0=1\), both parity grids,
the curvature/elasticity switch, and activity equality are all assigned in
the equality tables without continuity across a shelf jump. Activity equality
belongs to the dimension-labelled no-mode owner and is excluded by the strict
Gate-B activity condition.

The exact ambient-dimension activity owner is

\[
 K^2>\frac{\pi^2}{(1-\mu/K)^2}
 +\frac{(D-2)^2-1}{4},
 \qquad r=\ell+\frac{D-2}{2}.
\]

The computational use of \(3/4\) on the integer grid and \(2\) on the
half-integer grid is correctly identified as the weakest \(D=4\) and \(D=5\)
owner. Every higher-dimensional active record lies in this enlarged domain;
conversely, a retained integer or half-integer record is dimension-labelled
at \(D=4\) or \(D=5\). The analytic identities do not depend on this
enlargement.

### 4. Is every tangent or curvature remainder displayed with a valid sign?

Yes.

For every old level \(\ell_k=k-1/4\),

\[
 \Lambda_k(\ell)=y_k-\frac{\ell-\ell_k}{c_k},
 \qquad c_k=\frac{\theta_k}{\pi},
\]

and convexity of the zero-extended inverse gives

\[
 \mathcal R_k
 =2\int_{k-1}^{k}\{Y(\ell)-\Lambda_k(\ell)\}\,d\ell\ge0.
\]

The complete remainders are printed as

\[
 \mathcal R_{\rm tan}^+
 =\sum_{k=1}^{B_0}\mathcal R_k
 +2\int_{B_0}^{B_0+1}
 \left\{Y(\ell)-\frac{v-\ell}{\beta}\right\}d\ell\ge0,
\]

\[
 \mathcal R_{\rm tan}^0
 =\sum_{k=1}^{B_0}\mathcal R_k
 +2\int_{B_0}^{v}
 \left\{Y(\ell)-\frac{v-\ell}{\beta}\right\}d\ell\ge0.
\]

On \([v,B_0+1]\), \(Y=0\) and the tangent is nonpositive, so the gap-side
integrand remains nonnegative.

For the shelf, direct differentiation gives

\[
 A'<0,\qquad A''<0,\qquad(-A'')'>0
 \quad(r\le z\le r+p),
\]

and hence

\[
 \mathcal C_p\ge
 \frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-
 \frac1{\sqrt{K^2-r^2}}
 \right)>0.
\]

The lead's hinge decomposition and the clean-room covariance decomposition
independently prove \(\mathcal C_p-a_p\Delta\ge0\). Expanding the clean-room
double integral reproduces the weight
\((p-u)(u-a_p)\), so its alternative ledger is algebraically consistent
with the lead's generator-by-generator losses.

The new top-Bregman reserve is also correct. With
\(z=q+Y(\ell)\) and \(\theta=\arccos(z/K)\),

\[
 Y''(\ell)=
 \frac{\pi^2}{\sqrt{K^2-z^2}\,\theta^3}
 \ge\frac1{\pi\sqrt{K^2-q^2}\,\beta^3}
 =:c_{\rm top}
\]

on \([B_0,v]\). Taylor's integral remainder about \(v\) gives

\[
 2\int_{B_0}^{v}(Y-\Lambda_v)\,d\ell
 \ge c_{\rm top}\frac{(3/4)^3}{3}
 =\boxed{\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}}.
\]

Thus the coefficient \(9/64\), not a neighboring triangle coefficient, is
correct.

### 5. Does the identity for \(\mathscr S-\Phi_\delta^+\) follow from the exact definitions?

Yes. It uses only

\[
 E=\Delta+2e_p,\qquad pE_*=\frac{p-d_\rho m}{2},
\]

the exact Round 42 identity, and either exact terminal decomposition. No
inequality is used in the subtraction. The Mathematica replay independently
returns zero for the gap-side, literal-side, two-owner, and Round 42 endpoint
residuals.

### 6. Did any step reuse an exhausted projected scalar?

No. The only sign target searched or localized is

\[
 \mathscr S=D_A(q)+\mathcal C_p+p(E-E_*).
\]

The Round 42 scalar \(\Phi_\delta^+\) is used only to expose the exact
restored loss. \(\mathcal T_{42}\), \(\Gamma_{\rm OB}\),
\(\Gamma_{\rm gap}\), \(\mathcal R_*\), \(\mathcal R_J\), and the earlier
rejected projected targets are not substituted for \(\mathscr S\). The
Round 27 negative projected scalars appear only in the mandated regression
showing why such substitution would be invalid.

### 7. Did the proof separate correlated quantities before justifying the loss?

No unjustified separation occurs. The exact shelf, exact terminal defect,
cap \(J\), phase payment, inverse fractions, actual \(E\), and old-level
side vector are retained through the exact ledger. The one intrinsic sign
attempt replaces only two already displayed nonnegative remainders by
pointwise lower bounds that use the same variables \((r,p,q,\mu,K,\beta)\);
it does not optimize shelf and terminal variables independently.

The resulting necessary support theorem is

\[
\begin{aligned}
 \mathscr S<0\Longrightarrow
 p(E_*-E)>{}&
 \Omega_-+B_0\zeta+\frac9{16\beta}-J\\
 &+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}\\
 &+\frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-
 \frac1{\sqrt{K^2-r^2}}
 \right).
\end{aligned}
\]

This is one condition, not a \(B_0\)-, \(j\)-, \(f\)-, ratio-, or
chamber-indexed family. Moreover \(G_K(\mu)=v-u>B_0+1/4\), whereas every old
level is at most \(B_0-1/4\), so \(\theta_k<t\) and \(\Omega_->0\), including
the adverse \(\eta_k=0\) limit. Together with
\(B_0\zeta>1/5\), \(\beta<1/2\), and \(J<1/10\), this justifies the
count-free \(49/40\) corollary. That corollary is a necessary-support
statement, not a replacement sign target.

### 8. Were diagnostics and directed certificates classified correctly?

Yes.

- The Mathematica replay is an exact algebra/calculus replay. It supports
  transcription and polynomial identities but does not own strict brackets
  or the continuum sign.
- Both endpoint sweeps are explicitly high-precision diagnostics. Their
  positive minima are not coverage certificates.
- The selected 512-bit Arb wall brackets certify only the stated wall-root
  signs. They do not certify positive \(\mathscr S\).
- The Round 27 512-bit Arb calculation is a directed historical regression:
  it certifies negative rejected projected scalars together with
  \(\mathscr S>47\) and \(E>E_*\). It is not a Round 44 owner certificate.
- No `gate_trigger_certificate` or positive coverage certificate is claimed.

### 9. Was a negative point verified on the full exact owner?

No. Neither evaluator found even a floating/high-precision negative owner,
so there was no candidate for a directed full-owner negative certificate.
The Round 43 tuple is correctly rejected because
\(E\approx0.3280024861>E_*\approx0.2913519205\). The Round 27 witness is also
outside the hard owner because \(E>E_*\).

### 10. Does Gate B continue, close, or stop?

Gate B continues. It does not close because no analytic proof of
\(\mathscr S\ge0\) on the entire endpoint owner has been supplied. It does
not stop because no directed exact-owner negative point was found and every
possible negative point has been localized by the single intrinsic support
condition above. Gate C is therefore not activated.

## 2. Independent computation audit

The installed Wolfram runtime was used directly:

~~~text
wolframscript.exe -file computations/general_d_round44_exact_gate_b_replay.wl
~~~

Every symbolic residual was zero, the Round 43 fixture was rejected by the
hard \(E\)-owner, and the run ended with

~~~text
round43FixtureChecks=True
round44ExactGateBReplayOK=True
~~~

The widened primary diagnostic was rerun at 80 decimal digits:

~~~text
python -B computations/general_d_round44_exact_gate_b_diagnostic.py \
  --r-max 12 --p-max 25 --m-max 15 --b-max 12 --skip-round27-arb
~~~

It reproduced 92,455 tested candidates, 34 retained owners (21 integer and
13 half-integer), no negative \(\mathscr S\), and no record satisfying the
necessary negative-support condition. The maximum terminal and scalar ledger
residuals were approximately \(1.29\times10^{-80}\) and
\(2.53\times10^{-80}\), respectively.

The complete independent adversarial command was also rerun at 90 decimal
digits. It reproduced

~~~text
binary64_proposals=629288
binary64_owner_candidates=296
high_precision_exact_owner_records=296
high_precision_negative_owner_records=0
~~~

and the same diagnostic minimum

\[
 (r,p,m,f,B,j)=(1,3,1,2,2,0),\qquad
 \mathscr S=2.69456527890035502562933\ldots.
\]

Its built-in 512-bit Arb checks reproduced the selected wall brackets and the
Round 27 directed signs. The two Python files also compile successfully.
None of these finite results is used as a proof premise.

## 3. What is proved, what is open, and the first unrepaired gap

Actually proved in Round 44:

1. the exact shelf trapezoid identities and all derivative signs;
2. the elementary curvature reserve and a complete nonnegative ledger for
   \(\mathcal C_p-a_p\Delta\);
3. both owner-specific terminal decompositions with every tangent integral;
4. the \(1/(16\beta)\) ownership reconciliation;
5. the exact two-owner Gate-B identities and exact restored-loss identity
   relative to \(\Phi_\delta^+\);
6. the \(9/64\) top-Bregman reserve;
7. one intrinsic necessary condition containing every possible negative
   point.

Still open:

- the sign of \(\mathscr S\) on the localized support;
- the resisting one-sided upper-alpha, outer-\(B\) endpoint;
- the full high-floor first-drop theorem;
- the separate frozen audit of the general-dimensional branching backbone;
- the pointwise/aggregate assembly and all-dimensional theorem.

The first unrepaired logical gap is exactly the implication

\[
 \text{complete exact owner plus the strict support condition}
 \quad\Longrightarrow\quad \mathscr S\ge0.
\]

Equivalently, one must prove that the support allowed by the Round 44
necessary condition is empty, or sign the exact literal ledger there. The
finite observation that no sampled point enters this support does not repair
that gap.

## 4. Strictness and ownership error register

No unrepaired strictness or ownership error remains in the audited artifacts.
The audit specifically checked and found repaired or correct:

- the literal \(B-1\) versus one-sided \(B\) distinction;
- the literal/adverse old-inverse side vector;
- the unique ownership of the newest \(y_B=0\) jump;
- the Round 10 radial \(n\) versus Round 42 count-coordinate \(n\) overload;
- the exact ambient-\(D\) activity wall versus the weakest \(D=4/5\)
  computational owner;
- the upper-alpha endpoint versus a literal next-chart \(\alpha=0\) point;
- \(e_p=0\), \(E=E_*\), activity equality, \(B_0=1\), both parity grids,
  and ordinary-floor equality.

The only remaining source inconsistency is workflow metadata: the proof
graph's narrative next action predates the audited Gate-A stop. It does not
affect the authoritative statuses or any Round 44 identity, and the Round 44
prompt forbids editing that file.

## 5. Recommended state updates

Update only the narrative state files to record:

1. the exact terminal/trapezoid and restored-loss identities above;
2. the intrinsic negative-support theorem and its \(49/40\) corollary;
3. the finite searches as `diagnostic_only`, with no Round 44 negative
   certificate;
4. `Gate B: continues on the localized support` and `Gate C: not active`;
5. the first unrepaired gap and next single obligation below.

Do not alter `state/proof_obligations.yml` or the manuscript in this round.
Keep the high-floor obligation `open`, the general target `proposed`, the
weighted aggregate `proposed`, and the backbone `derived_under_assumptions`.

## 6. Next single proof obligation

Prove \(\mathscr S\ge0\) on exactly the support permitted by the Round 44
necessary condition, using the retained old-level Bregman areas and exact
first-shelf geometry. This must remain one intrinsic shelf-terminal theorem;
it may not split by \(B_0\), \(j\), \(f\), shell-ratio intervals, or chambers.

Higher \(Q_N\) faces and Gate C are not yet authorized by the Round 44 gate
decision.

## 7. Audit file scope

This audit created only:

~~~text
human/outbox/general-d-round-44-independent-audit.md
~~~

It did not modify state, manuscript, proof-graph, lead, clean-room,
diagnostic, replay, or adversarial files.
