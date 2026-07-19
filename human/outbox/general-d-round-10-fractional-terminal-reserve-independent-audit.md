# Independent audit of Round 10: fractional terminal reserve and shelf--terminal compensation

Date: 18 July 2026  
Target: `human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md`  
Strategy: `human/inbox/general-d_simplified_analytic_strategy.md`  
Manuscript checked: `manuscript/spherical-shell-polya-general-d.tex`

## Verdict

**PASS after repairs R1--R6.**

The proofs of (T1)--(T4), the exact/lower scalar separation, the
first-floor no-drop reductions, and the stated strict-wall conventions are
mathematically correct.  I found no counterexample and no sign or factor
error in those arguments.

The repaired diagnostic now computes and reports the T1, T2, and T3 slacks
at genuine high-precision inputs, and the quoted counts and extrema reproduce.
The remaining observations below are non-load-bearing editorial or future
diagnostic-hardening suggestions.

## 1. Verification of repairs R1--R6

### R1. Shift grid and no-drop floor: RESOLVED

The repaired note now states \(r\in\tfrac12\mathbb N\), \(r\geq1/2\), and
declares \(F_0=\cdots=F_n=f\) before defining \(\varepsilon_q,\chi_q\).
The paragraph below records the original issue and is retained as audit
provenance.

The pre-repair Section 0 did not state the hypothesis on (r), although
Section 3 uses
(r\geq1/2) to infer (q=r+n\geq3/2).  Add

\[
 r\in\tfrac12\mathbb N,
 \qquad r\geq\frac12.
\]

Equivalently, use the revised strategy's integer/half-integer formulation.
Without this hypothesis, the implication (n\geq1\Rightarrow q\geq3/2)
does not follow from the note as written.

Also, when introducing (S4), explicitly say

\[
 F_0=\cdots=F_n=f.
\]

In the pre-repair version, (f) first appeared inside the definitions of
(\varepsilon_q) and (\chi_q).

### R2. Scope cross-reference: RESOLVED

Section 0 now correctly points to Section 3 for residual inequalities (3.5)
and (3.7).  The pre-repair note incorrectly said Section 4.

### R3. Direct T1--T3 diagnostics: RESOLVED

The script now forms and prints T1Slack, T2Slack, and T3Slack, together with
separate negative-slack counts.  The fresh replay gave

\[
 \min T1Slack=\min T2Slack
 =0.3379957788418643469\ldots,
\]
\[
 \min T3Slack=1.0887836201970084\times10^{-9},
\]

and zero negative sampled slacks.  The remainder of this subsection records
the pre-repair deficiency.

The pre-repair Section 1.6 said that the run “found no violation of
(T1)--(T3).”  The pre-repair script computed terminal data, but did not form
or print any of
the following:

\[
 D_K(q)-\left[
 \sum_{k=1}^{B}
 \left(\frac1{2c_k}-1+2\eta_k\right)
 +\frac{(v-B)_+^2}{c_v}
 \right],
\]

\[
 D_A(q)-L_T,
 \qquad
 \alpha h-2\delta.
\]

It therefore did not detect a T1, T2, or T3 violation.  In
particular, `minNewScalar` is a no-drop scalar after adding
\(R_n+\chi_q\);
it is not the T2 slack.

The implemented repair added the explicit slack fields, minima, and negative
counts from the first alternative.  Deliberate inverse-spatial wall probes
remain optional future hardening, as noted in Section 1.7.

1. Add explicit `T1Slack`, `T2Slack`, and `T3Slack` fields, print their
   minima and the number of negative values, and include the (B=0),
   (v<B), (v=B), top-action-wall, and integral-(y_k) cases; or
2. weaken Section 1.6 to say only that the script evaluates the displayed
   terminal quantities and reproduces the quoted off-active example.

The analytic proofs do not depend on this diagnostic.

### R4. Input and root precision: RESOLVED

Random inputs are now generated directly at 70-digit working precision from
exact rational bounds.  Ball roots use dynamic precision up to 55 digits, and
the corner roots use exact initial-guess bounds.  The previous FindRoot
precision warnings no longer occur.  The text below records the pre-repair
implementation.

The pre-repair script set `wp = 70`, but the random sweep was seeded by
machine-precision
numbers:

```wolfram
rho = SetPrecision[RandomReal[{0.025, 0.975}], wp];
multiplier = Exp[RandomReal[{Log[1.0002], Log[3.5]}]];
k = SetPrecision[wall multiplier, wp];
```

`SetPrecision` pads a machine number; it does not create the missing digits.
Thus “70-digit working precision” is not an accurate description of the
random input accuracy.  Use high-precision random numbers from the outset,
preferably with exact bounds, for example

```wolfram
rho = RandomReal[{1/40, 39/40}, WorkingPrecision -> wp];
u = RandomReal[{Log[5001/5000], Log[7/2]}, WorkingPrecision -> wp];
multiplier = Exp[u];
```

The pre-repair corner enumeration also used machine literals in

```wolfram
guess = Min[1.2, Max[0.05, (9 Pi/(4 q))^(1/3)]];
```

and the supplied replay emitted `FindRoot::precw` warnings.  The repair uses
exact (6/5) and (1/20) and a 55-digit root solve.

### R5. B=0 enumeration and S4 wording: RESOLVED

The note now calls this a deterministic high-precision half-grid evaluation
and explicitly says it is neither exact nor an interval certificate.  It
reports the S4 result as numerical zero with about 64.38 digits rather than
as a certified \(10^{-64}\) bound.  The following paragraph records the
pre-repair wording.

The pre-repair Section 3.6 called the (B=0) computation an “exact half-grid
enumeration.”
The half-grid values (q\in\{3/2,2,\ldots,80\}) are exact, but (K),
(\rho), the active test, the strict floors, and the wall classification are
obtained from non-directed `FindRoot` and floating arithmetic.  The repaired
note now uses the accurate diagnostic description.

Relatedly, the pre-repair statement that the largest S4 residual was below
(10^{-64}) needed to be replaced by the actual numerical-zero output.  The
repaired note now makes that boundary explicit.

### R6. Active-dimension ownership: RESOLVED

The helper is now named extensionOwnerDimensionForShift.  The note and script
both explain that dOwner is the smallest new dimension after the completed
\(d=3\) theorem is taken as the base.  The following paragraph records the
old ambiguity.

The pre-repair helper called `minimalDimensionForShift` returned

- (d=4) for integral shifts;
- (d=5) for half-integral shifts (r\geq3/2);
- (d=3) for (r=1/2).

This was the smallest **new** dimension after treating the completed
three-dimensional theorem as the base case, not literally the smallest
dimension in which a half-integral shift (r\geq3/2) occurs.  Such a shift
also occurs in (d=3).  Rename the helper or explain this convention next
to the phrase “dimension-active.”  The convention is consistent with the
revised strategy only after the (d=3) base-case ownership was made explicit.

### 1.7 Remaining nonblocking cleanup

1. In the target note's displayed formulas near (2.5), the missing theorem,
   and (3.1), several occurrences of `qquad` should be `\qquad`.  This is a
   rendering typo only; the intended formulas and deductions are clear.
2. Mathematica's output `0``64.384...` is more precisely described as a
   numerical zero with about 64.38 digits of **accuracy**, not precision.
3. If the diagnostic is later extended to deliberate inverse-spatial wall
   probes, define `strictFraction[y_] := y - strictFloor[y]` so it uses the
   same wall tolerance as the count.  The diagnostic `chi` threshold could
   likewise reuse `wallTol`.  This does not affect the present random replay,
   the B=0 run, or the analytic strict-wall proof.

## 2. Analytic audit

### 2.1 T1: PASS

For (1\leq k\leq B=[v+1/4]_<), one has
(k-1/4<v), so the inverse level (y_k\in(0,L)) exists and
(c_k>0).  The strict level contribution is exactly

\[
 1+2[y_k]_<
 =2\lceil y_k\rceil-1
 =2y_k+1-2\eta_k.
\]

At an integral wall (y_k=m), the definition
\(\eta_k=y_k-[y_k]_<\) gives \(\eta_k=1\), hence \(2m-1\), correctly
excluding the equality sample.

The inverse derivative is

\[
 y'(t)=\frac1{g'(y(t))}.
\]

As (t) increases, (y(t)) decreases, (g'(y(t))) is nonincreasing,
and its negative reciprocal is nondecreasing.  Thus (y) is convex.  At
(t=v), the left derivative is (-1/c_v) and the right derivative of the
zero extension is (0), an upward jump, so the extension remains convex.

Integrating the tangent at (t_k=k-1/4) over ([k-1,k]) gives

\[
 2\int_{k-1}^{k}y(t)\,dt
 \geq2y_k+\frac1{2c_k}.
\]

Subtracting the exact level contribution gives precisely
\(1/(2c_k)-1+2\eta_k\).  The top tangent contributes
\((v-B)^2/c_v\) exactly as claimed when \(v>B\).

The (B/v) cases are all correctly owned:

- \(B=0\): the sum is empty and the top triangle gives \(v^2/c_v\);
- \(v<B\): the zero extension on \([v,B]\) is essential and valid;
- \(v=B\): the top term is zero;
- \(v>B\): the unused interval \([B,v]\) supplies the top term.

Formula (1.7) is the exact nonnegative tangent-gap loss.  No fractional
term is hidden.

### 2.2 T2, the optional maximum, T3, and T4: PASS

For (g(s)=G_K(q+s)),

\[
 -G_K'(z)=\frac{\arccos(z/K)}{\pi},
 \qquad c_v=\beta,
 \qquad c_k=\frac{\theta_k}{\pi}.
\]

The inverse displacement is correctly defined as

\[
 y_k=K\cos\theta_k-q.
\]

This displacement, rather than the absolute crossing point, is the
load-bearing quantity on the half-integer grid.

Since (q\leq\mu<q+1), all samples after the endpoint agree with the ball
samples.  Therefore

\[
 D_A(q)=D_K(q)+B-Q-2\delta
\]

holds at strict walls as well.  The (-B) in T1 cancels (+B), giving T2
with the correct coefficients and signs.  The optional
(max\{0,L_T\}) correctly imports the separately proved complete
one-interface theorem.

The displayed off-active example was independently recomputed:

\[
 q=\frac32,\quad \mu=\frac{58}{25},\quad K=\frac{232}{99},
\]

\[
 L_T=-0.0113686244414205784\ldots,qquad
 D_A(q)=0.00660026874489273017\ldots.
\]

Thus the warning that raw T2 is not automatically positive is correct.

For T3,

\[
 G_\mu''(z)=\frac1{\pi\sqrt{\mu^2-z^2}}>0
\]

places \(G_\mu\) strictly below its endpoint chord when
\(\alpha=\mu-q>0\).  Hence \(2\delta<\alpha h\); for \(\alpha=0\), both
sides vanish.  T4 is exact by definition.

### 2.3 Strict-wall audit: PASS

- At \(A(q+j)+1/4\in\mathbb N\), the equality level is absent.
- At an integral inverse displacement, \(\eta_k=1\), not \(0\).
- At \(G_K(q)+1/4=N\), \(B=N-1\), and the unused top interval is retained.
- Under \(q\leq\mu<q+1\), \(q+j=\mu\) forces \(j=0\) and \(q=\mu\);
  then \(h=\delta=0\) and \(B=Q\).
- If \(\mu-r\in\mathbb N\), then \(q=\mu\), so the same zero-cap owner
  applies.
- At \(q+j=K\), the action is zero and \([1/4]_< =0\).
- At the shelf endpoint wall \(A(q)+1/4=f\), S4 retains the favorable
  \(\chi_q=1\).

No limiting argument is improperly substituted for a literal strict value.

## 3. Shelf--terminal scalar audit

Equations (2.1)--(2.4) are correct.  Substitution of S2 into S1 gives

\[
 D_A(r)\geq\mathscr S.
\]

Substitution of T2 and S3 gives exactly \(\Phi_\delta\).  Since

\[
 A(r)-A(r+p)=\varepsilon_0-\varepsilon_p,
\]

the curvature coefficient and its sign in (2.3) are correct.  Replacing
(-2\delta) by (-\alpha h) is in the favorable direction.

The note correctly distinguishes the exact reduced scalar \(\mathscr S\)
from the lower surrogate \(\Phi_\delta\).  It also correctly separates the
no-drop identity

\[
 D_A(r)=D_A(q)-\frac n2+2n\varepsilon_q
 +2\int_0^n u\sigma(r+u)\,du+\chi_q
\]

from universal CST.  Omitting \(\chi_q\) at a no-drop endpoint wall would
ask for an unnecessarily stronger statement.

The loss ledger in Section 2.5 is complete: S1 slack, S3 slack, inverse
tangent gaps, and the optional cap slack are the only losses in the displayed
chain.

## 4. First-floor no-drop audit

### 4.1 Remainder-rich and (B\geq2): PASS

With (F_0=\cdots=F_n=1),

\[
 \varepsilon=A(q)-\frac34\in[0,1).
\]

If \(\varepsilon\geq1/4\), then
\(-n/2+2n\varepsilon\geq0\), and the other S4 terms are nonnegative.

With the repaired shift-grid hypothesis, (n\geq1) gives (q\geq3/2).  The
identity

\[
 G_{q+1}(q)=\frac1\pi\int_q^{q+1}
 \sqrt{1-\frac{q^2}{a^2}}\,da
\]

is correct, and (G_{q+1}(q)) decreases with (q).  Independently,

\[
 G_{5/2}(3/2)=0.1938689194162815205\ldots<\frac15.
\]

Thus (h<1/5).  If (B\geq2), strict counting gives (v>7/4), so

\[
 \varepsilon=v-h-\frac34>1-h>\frac45.
\]

Therefore the entire (B\geq2) sector is indeed contained in the already
closed remainder-rich sector.

### 4.2 (B=0): PASS as a reduction, still open as stated

Here (v\leq3/4), while (v-h=A(q)\geq3/4).  Hence

\[
 v=\frac34,\quad h=0,\quad q=\mu,\quad
 \varepsilon=0,\quad Q=0,\quad\chi_q=1.
\]

T1 gives (D_A(q)\geq9/(16\beta)), and substitution into S4 gives
exactly (3.5).  No claim of proving (3.5) is made.

### 4.3 (B=1): PASS as a reduction, still open as stated

The definition of (L_1) is the one-level instance of T2, and (3.7)
follows from S4 and (D_A(q)\geq\max\{0,L_1\}).  The phase table is
correct:

- \(0<\varepsilon<1/4\): \(Q=1,\chi_q=0\);
- \(\varepsilon=0,h>0\): \(Q=0,\chi_q=1,B=1\);
- \(\varepsilon=h=0\): the \(B=0\) corner.

The note accurately reports that (3.5) and (3.7) remain unproved.

## 5. CST-H and theorem scope

The active condition

\[
 K^2>
 \frac{\pi^2}{(1-\rho)^2}
 +\frac{(d-2)^2-1}{4}
\]

is the correct complement of the strengthened no-mode region.  Its equality
face belongs to the no-mode theorem because the spectral count is strict.

CST-H is correctly limited to \(f\geq2\) and \(p<n\); no no-drop
\(\chi_q\) term is then present.  The note labels the proof open and does not
claim the all-dimensional theorem.  This scope is honest and consistent with
the revised strategy.

## 6. Independent numerical replay

The exact command printed in Section 6 ran successfully under Wolfram 15.0
and reproduced the principal output:

- `records=6427`; `dimensionActiveRecords=6409`;
- one (B=2) active random record and 6408 (B=1) records;
- no (B=0) record in the random sweep;
- `B0GridCount=1197`, through (q=80), with `B0MaxN=20`;
- minimum sampled slacks
  \[
  T1Slack=T2Slack=0.337995778841864\ldots,
  \]
  \[
  T3Slack=1.0887836201970084\times10^{-9},
  \]
  and `negativeSlackCounts=<|T1->0,T2->0,T3->0|>`;
- the quoted difficult-point values
  \[
  D_A(r)=0.573831785000637\ldots,qquad
  R_2=-0.378931695103780\ldots,
  \]
  \[
  \Psi_1=0.0673128993850871\ldots;
  \]
- the old/new surrogate values at
  ((\rho,K,r)\approx(0.6056801590,8.0207601251,1)):
  \[
  -0.0375756423479523\ldots,qquad
  0.749037795546438\ldots;
  \]
- the off-active T2 values quoted above.

The difference

\[
 0.573831785000637\ldots-0.0673128993850871\ldots
 =0.506518885615550\ldots
\]

supports the note's statement that the tangent reduction loses about
(0.51) at that diagnostic point.

The previous `FindRoot::precw` warnings are gone.  The final WolframScript
configuration warning did not prevent the kernel output, but using the
installed `math.exe` binary would provide a cleaner reproduction command.

## 7. Final disposition

- **Analytic WP1:** PASS.
- **Exact/lower scalar derivation:** PASS.
- **First-floor (B\geq2) closure:** PASS.
- **(B=0) and (B=1) reductions:** PASS, still open exactly as reported.
- **CST-H scope and open status:** PASS.
- **Strict-wall ownership:** PASS.
- **Numerical values replayed:** PASS as diagnostics.
- **Claims about what the script checks and its precision:** PASS after
  R3--R5.

The Round-10 note is therefore **PASS**.  Its stated WP2 and CST-H residuals
remain open exactly as declared; this verdict does not promote the
all-dimensional theorem.
