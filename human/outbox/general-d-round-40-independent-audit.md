# Independent audit: General dimension, Round 40

Date: 20 July 2026

Audited artifacts:

- `human/inbox/general-d-strategy_r2.md`
- `human/outbox/general-d-round-40-upper-alpha-midpoint-reduction.md`
- `computations/general_d_round40_upper_midpoint_replay.wl`
- `computations/general_d_round40_upper_face_diagnostic.py`
- the inherited Round 39 endpoint identity and cap used by Round 40

## Verdict

**PASS as a structural reduction.** Every sign, inequality direction,
strictness source, endpoint convention, branch formula, and convexity claim
made as proved in the final Round 40 note is supported. The reduction proves

\[
 \Gamma_{\rm OB}>\mathcal R_*(p,m,t)
\]

on the one-sided outer-\(B\), upper-alpha endpoint and reduces the remaining
problem to one intrinsic continuous sign. It does **not** prove
\(\mathcal R_*>0\), close that endpoint, prove the high-floor CST, or prove
the all-dimensional Pólya theorem.

There is no unsupported theorem claim in the final audited version. The first
unproved proposition in the implication chain is precisely (R40.13),
\(\mathcal R_*(p,m,t)>0\), and the note explicitly labels it as an open proof
target. Consequently there is no "first unsupported claim" to report beyond
that intentionally open target.

No edit was made to `state/proof_obligations.yml`. Its SHA-256 remains

`a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.

## 1. Endpoint identity, cap, and theorem boundary

The selected-scalar starting point is the exact inherited identity

\[
 \Gamma_{\rm OB}=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta+p\Delta+a_pM_4+2pe_p
 -\frac{p-dm}{2}.
\]

Round 40 does not call this identity lossless relative to the shifted defect;
it preserves the earlier projection losses as inherited from Rounds 37--39.
At \(\mu=q+1\), the cap is

\[
 J=2I_{q+1}(q)\leq2I_6(5)<\frac1{10}.
\]

The non-strict first comparison correctly allows the case \(q=5\); the final
cap is strict. The endpoint retains the gap-side labels at
\(\alpha\uparrow1^-\), while the next chart's literal \(\alpha=0\) point is
kept separate. Thus no strict bracket is reassigned at the endpoint.

## 2. Midpoint kernel and angular chord

For \(\mathcal D=b_K-b_\mu\), direct differentiation gives

\[
 \mathcal D'(z)=\frac1\pi
 \left((\mu^2-z^2)^{-1/2}-(K^2-z^2)^{-1/2}\right)>0,
\]

\[
 \mathcal D''(z)=\frac z\pi
 \left((\mu^2-z^2)^{-3/2}-(K^2-z^2)^{-3/2}\right)>0.
\]

Both directions are correct because \(0<z<\mu<K\). Since
\(A'=-\mathcal D\),

\[
 \Delta=\int_r^{r+p}\mathcal D(z)\,dz.
\]

The interval has positive length and lies strictly below \(\mu\), so strict
Hermite--Hadamard midpoint convexity gives

\[
 \Delta>p\mathcal D(r+p/2).
\]

For \(y=r+p/2\), set
\(\vartheta=\arccos(y/\mu)\) and
\(\varphi=\arccos(y/K)\). Then
\(0<\vartheta<\varphi<\pi/2\). The cosine mean-value theorem and
\(\sin\xi<\sin\varphi\) give, in the stated direction,

\[
 \mathcal D(y)>
 \frac{y(1-\cos t)}{
 \pi\sqrt{\mu^2-y^2\cos^2t}}=\delta_y.
\]

Therefore \(p\Delta>p^2\delta_y\). The exact loss after deleting only the
proved nonnegative reserves is

\[
 \Gamma_{\rm OB}-\mathcal U_0
 =p(\Delta-p\delta_y)+\Omega_-+a_pM_4+2pe_p>0.
\]

The strictness is already owned by the midpoint/chord chain; it does not rely
on any reserve being positive.

## 3. Normalization and count interpolation

With \(N=p/2+m+1\) and \(\rho=N/\mu\), the denominator comparison is exact:

\[
 \sin^2t+2\rho-\left[1-(1-\rho)^2\cos^2t\right]
 =\rho(2\sin^2t+\rho\cos^2t)>0.
\]

Because the numerator is positive, the larger root-free denominator produces
the strict lower bound \(\delta_y>C(\rho,t)\), as claimed.

On the outer wall, \(W=B_0+3/4-u\) and

\[
 u=\int_q^{q+1}b_K(z)\,dz<b_K(q)=\beta<\frac12.
\]

Thus \(W>B_0+1/4\geq5/4\). Combining \(B_0\geq1\) with
\(B_0>W-3/4\) is legitimate for every \(0<k\leq1\):

\[
 B_0>(1-k)+k(W-3/4).
\]

The restriction \(k>0\) is essential for strictness and is present in the
final note. At \(k=1/4\), this is exactly

\[
 B_0>\frac W4+\frac9{16}.
\]

Together with \(1/(2\beta)>1\), \(J<1/10\), and \(W=\mu L_0\), this yields
the printed \(\mathcal R\) with every inequality in the correct direction.

## 4. Elimination of \(\mu\)

The derivative

\[
 C_\rho=-A_t\frac{\sin^2t+\rho+1}
 {(\sin^2t+2\rho)^{3/2}}<0
\]

is correct. Since \(\rho=N/\mu\) decreases with \(\mu\), both the
\(p^2C\)-term and the positive linear term \(\zeta\mu L_0/4\) increase.
Hence \(\mathcal R\) is strictly increasing in \(\mu\).

The endpoint constraints give

\[
 \mu\geq p+m+2,
 \qquad
 \mu>\frac5{4L_0(t)}.
\]

Evaluating at the maximum of these two lower endpoints is valid even when the
phase endpoint is unattained: monotonicity gives
\(\mathcal R(\mu)\geq\mathcal R(\mu_*)\), with a strict inequality whenever
the phase lower bound is active. Positivity at \(\mu_*\) is therefore a
sufficient, not asserted necessary, condition.

## 5. Branch formulas, domains, and convexity

On branch I, \(\mu_*=p+m+2\) and
\(a=(p/2+1)/(p+m+2)\). The three constraints transform exactly to

\[
 a_h<a\leq a_I^+,
\]

where the strict lower bound comes from \(p>dm\), while the two non-strict
upper bounds come from \(m\geq1\) and the branch-I seam ownership. Substituting
\(m=(p+2)/(2a)-p-2\) gives (R40.16). Its derivatives are

\[
 f_I'(a)=-\frac{X_I}{a^2}
 +p^2A_t\frac{S_t-a}{(S_t-2a)^{3/2}},
\]

\[
 f_I''(a)=\frac{2X_I}{a^3}
 +p^2A_t\frac{2S_t-a}{(S_t-2a)^{5/2}}>0.
\]

Thus the critical point is unique and clamping it to the interval (or its
closure for a lower-bound calculation) is valid.

On branch II, the phase condition is correctly strict:

\[
 (p+m+2)L_0<\frac54,
\]

so branch I owns the equality seam. With
\(a=1-(p/2+m+1)/\mu_0\), both the phase condition and \(p>dm\) yield strict
lower bounds, whereas \(m\geq1\) yields the closed upper bound. Hence the
exact feasible interval is

\[
 a_{II}^-<a\leq a_{II}^+,
\]

and using its closure can only lower the minimum. Feasibility gives
\(0<a\leq a_{II}^+<1\); no unjustified \(a<1/2\) restriction remains.
Substitution gives (R40.18), and

\[
 f_{II}''(a)=p^2A_t
 \frac{2S_t-a}{(S_t-2a)^{5/2}}>0
\]

throughout this full domain. The two branch formulas are substitutions into
the same \(\mathcal R\) and agree when
\((p+m+2)L_0=5/4\), so there is no seam gap.

The denominator replacements in Section 5 also have the correct direction:
the denominator decreases as \(a\) increases. They are explicitly presented
as optional weaker projections, and neither their remaining two-variable
sign nor the proposed Sturm/resultant continuation is claimed as complete.

## 6. Equality faces and loss ownership

The final ownership table covers the equality loci relevant to this
reduction:

- the outer-\(B\) wall uses the one-sided gap label, not the literal strict
  bracket;
- the action-floor equality is retained until \(e_p\geq0\) is deleted, so the
  deletion is wall-safe;
- the midpoint interval lies below the inner turning wall because
  \(x<\mu\), and below the outer turning wall because \(\mu<K\);
- \(\mu-r=p+m+1\in\mathbb Z\) remains owned by
  \(\alpha\uparrow1^-\), rather than being reindexed into the next chart.

The note distinguishes identities, strict lower bounds, nonnegative
deletions, and optional projections. It does not merge the Round 39
\(F_{\rm OB}\) loss ledger with the new midpoint loss.

## 7. Computational reproduction and diagnostic scope

The updated Mathematica replay was rerun on Windows with the installed
Wolfram runtime:

`wolframscript.exe -file computations/general_d_round40_upper_midpoint_replay.wl`

It returned zero for every derivative, denominator, count, branch,
selected-loss, and tangent-majorant residual; every requested pointwise sign
was `True`; and it ended with

`round40UpperMidpointReplayOK=True`.

In particular, the Branch II algebra and convexity are now replayed under
\(0<a<1\), matching the analytic domain. Mathematica is not used to own
Hermite--Hadamard strictness, brackets, one-sided labels, or the open
continuum sign.

The Python companion compiles and its ordinary binary64 run reproduces the
documented diagnostic behavior: 6,347 retained endpoint samples, observed
minimum \(\mathcal U_0\approx1.0298384740\), and seeded relaxed branch minima
approximately \(0.2701\) and \(0.4159\), with no sampled negative branch
value. The high-precision relaxed \(n=100\) replay makes \(Q_0\) and
\(Q_{\rm exact}\) negative while violating the same-floor/hard feasibility
conditions, exactly as described.

Every such output is labelled `diagnostic_only`; the script prints
`theorem_claim=False` and `interval_certificate=False`. The note uses none of
the sampled minima as a theorem premise and correctly limits the asymptotic
rejection to the two auxiliary universal targets.

## 8. Gate A/B/C conclusion

The final Round 40 state satisfies the revised strategy's Gate A condition:
one intrinsic continuous endpoint sign remains, with no \(B\)-, \(j\)-,
floor-, ratio-, or chamber-indexed theorem family. The two convex formulas
are representations of the two arguments of one maximum, not independent
certificates. No exact feasible counterexample to the selected endpoint
scalar has been produced.

Accordingly, **Gate A remains active** for the proposed global enclosure and
single elimination attempt. If that sign is false or its proof requires the
forbidden proliferation listed in the strategy, the stated fallback to Gate
B is mandatory. Gate C is not activated by Round 40. No obligation or theorem
status is promoted by this audit.
