# Independent audit: General dimension, Round 38

Date: 20 July 2026

Audited artifacts:

- `human/inbox/general-d-strategy_r2.md`
- `human/outbox/general-d-round-38-gap-position-count-phase-and-face-compensation.md`
- `computations/general_d_round38_gap_position_replay.wl`
- `computations/general_d_round38_gap_face_diagnostic.py`

## Verdict

**PASS.**  The analytic note correctly proves (R38.1)--(R38.23), with
the exact scope required by the revised strategy.  Its endpoint ownership,
loss ledger, diagnostic labels, and Gate A/B/C decision are consistent with
the proved implication chain.  The remaining \(p\geq3\) sign, the selected
high-floor first-drop obligation, the branching-backbone audit, and the
all-dimensional theorem are all correctly left open.

This audit authorizes no edit to `state/proof_obligations.yml`.  The
authoritative file was rehashed during the audit and still has SHA-256

`a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.

## 1. Gap-position and strict-floor audit

The proof of (R38.1)--(R38.5) is complete.

1. Differentiating \(G_a\) gives \(G_a'(z)=-b_a(z)\).  Therefore

   \[
   S_q=\int_q^\mu(b_K-b_\mu)>0,
   \qquad
   S_q+h=\int_q^\mu b_K<\frac\alpha2.
   \]

2. The literal strict owner \(B_0=[f-\lambda]_< =B-1\) gives
   \(j\leq\lambda<j+1\), while the terminal and outer counts give
   \(S_q\leq u\) and \(u<S_q+h\), respectively.  Hence

   \[
   0<S_q\leq u<S_q+h<\frac\alpha2,
   \qquad 0\leq\chi<h,
   \qquad 0<u<\frac\alpha2<\frac12.
   \]

3. Substitution then gives all four displayed coordinate identities.  In
   particular \(j<\lambda<j+1/2\), so the note correctly removes the
   spurious positive-\(\alpha\) integer-\(\lambda\) face.

4. The \(B_0=0\) corollary uses exactly the inherited normalized hypotheses
   \(W<3/4\), \(A(x)-A(q)\geq1\), and \(P>dM\).  It does not substitute the
   unjustified equality \(A(q)=3/4\).

The one-sided endpoint dictionary is also correct: the literal \(Q\)-wall
has \(\chi=0\); the outer wall has literal count \(B-1\) and gap-side label
\(B^+=B\), with \(\chi=h\) and \(y_B=0\); and the lower-alpha endpoint is
only the limit \(\alpha\downarrow0\), whose literal point is equal-count.
The upper endpoint retains its \(\alpha\uparrow1^-\) labels.

## 2. Selected normal form and count--phase audit

Equations (R38.6)--(R38.8) are correct.  From
\(E=\Delta+2e_p\) and \(\widehat\Xi=\Delta-M_4\), one obtains
\(\Xi=2e_p+\widehat\Xi\).  Substitution gives (R38.7).  Also

\[
M_4\geq\tau(M_4+2e_p+2\lambda),
\qquad
\frac{2\tau}{1-\tau}=g,
\]

which proves \(M_4\geq g(\lambda+e_p)\).  The note correctly qualifies
(R38.7) as lossless only for the selected projected scalar and records the
exact discarded reserve

\[
\Phi_\delta^+-\Gamma_{\rm gap}=a_p\widehat\Xi\geq0.
\]

The count--phase lemma (R38.9) is valid on every finite gap-side owner.
When \(\zeta\geq1/5\), equality would force \(B_0=1\) and
\(t=5\pi/12\), but \(\mu\geq3\) and \(2+\sqrt3>\pi\) then give
\(W>7/4\), contradicting (R38.10).  When \(0<\zeta<1/5\), the auxiliary
function

\[
F(x)=x\cos x-(1-x^2)\sin x
\]

has \(F(0)=0\) and \(F'(x)=x^2\cos x+x\sin x>0\).  Thus
\(\cot x>1/x-x\), and the displayed change of variables yields

\[
B_0\zeta>
\frac{6(1+\zeta)}{\pi^2}-\frac{9\zeta}{4}>\frac15.
\]

The final affine comparison is strict and uses only \(\pi^2<10\).
Consequently

\[
\Gamma_{\rm gap}>
\frac{37}{35}-\frac{p-dm}{2},
\]

so \(p-dm\leq74/35\) closes the projected gate.  The stated \(p=2\)
closure follows from \(p-dm<2\); \(p=1\) is correctly cited as an inherited
Round 36 result.  No conclusion is drawn for the residual \(p\geq3\)
faces.

## 3. Unified face compensation and root-free audit

Equations (R38.14)--(R38.20) are proved with the required correlations
intact.

- The newest-root identity follows from
  \(G_K(q)-G_K(q+y_B)=\int_q^{q+y_B}b_K\).  Monotonicity of \(b_K\) gives
  \(y_B\geq(h-\chi)/\beta\) and
  \(\theta_B\leq\pi\beta\), hence (R38.16).
- The Round 34 common-radial-parameter identity applies to the actual drop
  \(A(x)-A(q)=j+e_p+\chi\), giving the strict (R38.17).  With the inherited
  facts \(j\geq0\) and \(B_0=n-j\geq1\), the two branches of the single
  minimum identity prove (R38.18).
- The affine function of \(\chi\in[0,h]\) is bounded by its smaller endpoint
  payment, proving (R38.19).  Substitution into the exact
  \(\Phi_\delta^+\) formula cancels the initial \(1\) with the newest-level
  \(-1\) and gives precisely (R38.20).

The note correctly treats (R38.20) as one proof-level lower bound rather
than a new scalar or certificate.  A nonnegative right-hand side proves
\(\Phi_\delta^+>0\); a negative right-hand side would not disprove
\(\Phi_\delta^+\) or imply any sign for the smaller
\(\mathcal H_\Delta\).

The optional estimate (R38.22) is also correct.  For every old level,

\[
\delta_k=F(t)-F(\theta_k)
\leq\frac K\pi t\sin t\,(t-\theta_k),
\]

while

\[
\frac\pi{2\theta_k}-\frac\pi{2t}
\geq\frac{\pi(t-\theta_k)}{2t^2}.
\]

Summation gives (R38.22), and \(u<1/2\) gives the strict coarse corollary
(R38.23).  The primary statement retains \(u\), as required.

## 4. Ownership and loss ledger

The ownership table passes all strict-wall checks.

- For positive \(\alpha\), old roots satisfy
  \(\theta_k<t<\theta_B\leq\pi\beta\).
- At an old literal inverse wall, \(\eta_k=1\); on its adverse side,
  \(\eta_k\downarrow0\).  The newest \(y_B=0\) event is assigned only to
  the outer-action jump and is not double counted as an old inverse jump.
- The lower-alpha literal point and the next alpha chart are not imported
  into the one-level-gap owner.

The loss ledger keeps the four levels distinct:

\[
D_A(r)\geq\mathscr S\geq\Phi_\delta^+\geq\Gamma_{\rm gap}.
\]

Only the last passage has the exact reserve
\(a_p\widehat\Xi\); the earlier terminal, shelf, and first-shelf losses are
correctly described as inherited nonnegative reductions rather than
identities.  The optional root-free corollary separately records the loss
of \(u\).

## 5. Computational replay

The Mathematica replay was run with Mathematica 15.0 on Windows:

`wolframscript.exe -file computations/general_d_round38_gap_position_replay.wl`

It returned zero for every algebraic, derivative, minimum, sum, gamma,
threshold, and upper-cap residual, including \(Jcheck=0\), and ended with

`round38GapPositionReplayOK=True`.

The file is properly limited to algebra and calculus identities.  It does
not claim ownership of strict brackets, endpoint labels, or continuum sign
proofs.

The documented diagnostic command was also rerun:

`python -B computations/general_d_round38_gap_face_diagnostic.py --limit 5 --random 200 --wall-limit 50`

It reproduced all reported values:

- 626 feasible tuples and 1,354 retained evaluations;
- 703 integer-grid and 651 half-integer-grid evaluations;
- 1,198 records beyond the proved (R38.13) threshold;
- 50 literal and 57 adverse old-inverse samples;
- minima \(1.97221024700173\ldots\),
  \(0.996771560326323\ldots\), and
  \(1.86292572734470\ldots\) for
  \(\Gamma_{\rm gap}\), \(\mathcal H_\Delta\), and the right-hand side of
  (R38.20), respectively;
- minimum \(B_0\zeta-1/5=0.244103179304456\ldots\);
- no sampled negative target.

The sampler enforces both parity grids, the corresponding activity owner,
literal strict counts, positive \(\alpha\), and literal/adverse old-inverse
samples.  Its negative-\(\Gamma\) reporting path reconstructs
\(\mathscr S\), \(\mathscr S-\Phi_\delta^+\),
\(\Phi_\delta^+-\Gamma_{\rm gap}\), and, when the finite sum is within the
declared limit, \(D_A(r)-\mathscr S\).  No negative record occurred in the
reproduced run.  Every output is correctly marked `diagnostic_only`, uses
ordinary binary64 arithmetic, and is excluded from the analytic proof.

## 6. Strategy and theorem-boundary conclusion

The Round 38 decision obeys the revised stop rule.  Gate A remains active
only for one intrinsic continuous \(p\geq3\) endpoint inequality retaining
\(u,\chi,J,W,\Omega_-,e_p,M_4,\widehat\Xi\).  A certified feasible
\(\Gamma_{\rm gap}<0\) would stop that universal target; one exact
\(\mathcal H_\Delta\) or \(\Phi_\delta^+\) attempt is then permitted before
returning to \(\mathscr S\).  Gate B is prepared but not activated, and
Gate C is not active.

No ratio/count ladder, chamber proliferation, new compact certificate, or
all-dimensional theorem claim appears in the audited deliverables.
