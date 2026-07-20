# Independent audit of Round 43
## Hard-remainder isolation and the Gate-A stop

**Date:** 20 July 2026  
**Verdict:** analytic structural PASS; Gate A STOP; no endpoint or theorem promotion

## 1. Scope checked

I audited
`human/outbox/general-d-round-43-hard-remainder-isolation-and-gate-a-stop.md`
against the two binding strategy documents and the Round 42 dependency
chain.  The admissible claims are deliberately narrow:

- a radical lower envelope for \(H\) and an elementary strict lower bound
  for \(h\);
- an analytic obstruction to signing \(\mathcal T_{42}\) from relaxed
  count-phase/radial data;
- identification of the quantitative hard condition \(E<E_*\) as
  indispensable;
- strict fixed-chart monotonicity of \(E_f-E_*\);
- the Gate-A stop forced by the discontinuous floor/count synchronization.

The note does not claim that \(\mathcal T_{42}\) is false on its exact hard
owner.  It does not close the endpoint, the shifted-tail theorem, high-floor
CST, the general-dimensional branching audit, or the all-dimensional Pólya
theorem.  It does not alter `state/proof_obligations.yml`.

## 2. Radical and cap lemmas

The rationalization

\[
 R_1=\frac{p(2r+p)}{m(2x+m)}
     \frac{U_x+U_q}{U_r+U_x}
\]

is exact.  With \(a=U_r/U_x>1\), \(b=U_q/U_x<1\), the two identities

\[
 \frac{1+b}{1+a}-\frac1a
 =\frac{ab-1}{a(1+a)},
\]

\[
 \left(\frac{1+b}{1+a}\right)^2-\frac ba
 =\frac{(a-b)(1-ab)}{a(1+a)^2}
\]

prove the stated minimum lower bound in the two intrinsic signs
\(ab\ge1\) and \(ab\le1\).  This is not a count- or ratio-indexed theorem
family.

For the cap bound, differentiation gives

\[
 \frac d{d\theta}\left(
 \sin\theta-\theta\cos\theta-\frac{\sin^3\theta}{3}
 \right)
 =\sin\theta(\theta-\sin\theta\cos\theta)>0.
\]

Thus \(H\ge\underline H\), \(h>\underline h\), and the strict reduced
lower bound for \(\mathcal T_{42}\) are valid.

## 3. Relaxed-domain obstruction

The family indexed by multiples of four is an analytic asymptotic argument,
not a finite certificate.  The outer wall is exact because

\[
 \frac N\pi(\tan\theta_N-\theta_N)=\frac74,
 \qquad K=N\sec\theta_N=(N+1)\sec t_N.
\]

The displayed limits for \(t_N\), \(R_1\), \(p+a_p\), and \(h_N\) yield

\[
 \frac{\mathcal T_{42}}N\longrightarrow
 \frac{11\sqrt{14}}{252\pi(2-\sqrt2)}-\frac18<0.
\]

The elementary comparison used for the last sign is correct.  The family
eventually satisfies the grid, activity, outer count, gap ordering, and
\(p>dm\), but its same-shelf drop diverges.  It therefore proves only that
the relaxed phase/radial data are insufficient.  It is not a hard-owner
counterexample.

## 4. Finite diagnostic and the exact missing condition

The high-precision replay of

\[
 (r,p,m,f,B,j)=(1,9,9,4,3,1)
\]

reproduces the outer wall, strict gap ordering, activity, common first
shelf, and terminal first drop.  It also gives

\[
 \mathcal T_{42}\approx-0.1052012867,
 \qquad E-E_*\approx0.0366505656>0.
\]

The record fails the true owner precisely at the quantitative hard
inequality \(E<E_*\).  Because the replay is high-precision arithmetic and
not directed interval arithmetic, the note correctly labels it diagnostic.
No theorem claim depends on its decimal signs.

This leaves the single intrinsic contrapositive

\[
 \mathcal T_{42}<0\Longrightarrow E\ge E_*.
\]

The note does not replace that implication by a new empirical scalar.

## 5. Fixed-chart derivative audit

For \(K=\mu\sec t\), direct differentiation gives

\[
 \frac{\partial A_t(z)}{\partial t}
 =\frac{\tan t}{\pi}\sqrt{K^2-z^2}.
\]

Therefore

\[
 (E_f-E_*)'(t)=\frac1\pi\left[
 \tan t\left(\sqrt{K^2-r^2}+\sqrt{K^2-x^2}\right)-\frac mp
 \right].
\]

Since \(r,x<\mu\), the bracket is strictly greater than
\(2\mu\tan^2t-m/p\).  The hard orientation gives \(m/p<1/d\), so it
suffices that \(2\mu d\tan^2t>1\).

The two-range proof is valid.  The phase identity and \(u<1/2\) give
\(W>5/4\).

- If \(t\le\pi/3\), monotonicity of \(\tan s/s\) gives
  \(\tan t-t\le(t/3)\tan^2t\), and hence
  \(2\mu d\tan^2t>15/2\).
- If \(t\ge\pi/3\), with \(y=\pi/2-t\le\pi/6\), one gets
  \(2\mu d\tan^2t>5y\cot y>5\cos y>1\).

Thus the strict fixed-\(f\) derivative is proved without computer
assistance.

## 6. Gate adjudication

The transport is necessarily chart-local.  At a shelf-floor jump,

\[
 E_{f+1}=E_f-2,
\]

while \(E_*\) is continuous.  The outer face is sampled at the separate
integer walls

\[
 G_K(q)-\frac34=B_0\in\mathbb N.
\]

Consequently a global ordering of the hard crossing and the
\(\mathcal T_{42}\) crossing requires tracking the interlacing of the
\(f\)- and \(B\)-walls.  That is an \(f/B/j\)-indexed theorem family or an
equivalent chamber decomposition.  The binding revised strategy forbids
both.  Continuous phase monotonicity supplies no uniform compensation for
the jump.

This is exactly the Gate-A stop criterion: the one authorized intrinsic
hard-remainder attempt has reached a forbidden discrete wall analysis.
Gate B is therefore authorized and should restore

\[
 \boxed{\mathscr S=D_A(q)+R_p+\frac{dm}{2}}.
\]

No further repair of \(\mathcal T_{42}\), projected scalar, ratio split,
or certificate is authorized.  The proof graph and all theorem statuses
remain unchanged.

## 7. Replay verdict

`computations/general_d_round43_hard_remainder_replay.wl` returns

```text
rationalizationResidual=0
qBranchOneResidual=0
qBranchTwoResidual=0
capDerivativeResidual=0
innerDerivativeResidual=0
actionDerivativeResidual={0, 0}
hardDerivativeResidual=0
limitCoefficientNegative=True
finiteDiagnosticChecks=True
round43HardRemainderReplayOK=True
```

This corroborates the algebra and the finite diagnostic.  It is not a
certificate for an open continuum sign.  The printed analytic proofs own
the promoted Round 43 structural claims.
