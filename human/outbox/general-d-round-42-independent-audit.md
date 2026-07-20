# Independent audit: General dimension, Round 42

**Date:** 20 July 2026

Audited artifacts:

- `human/inbox/general-d-strategy_r2.md`
- `human/outbox/general-d-round-38-gap-position-count-phase-and-face-compensation.md`
- `human/outbox/general-d-round-39-outer-face-floor-elimination-and-cap-sharpening.md`
- `human/outbox/general-d-round-42-stronger-upper-alpha-phi-specialization.md`
- `computations/general_d_round42_stronger_phi_replay.wl`

## Verdict

**STRUCTURAL PASS only; final sign open.**

The Round 42 endpoint identity, synchronized count, minimum algebra, loss
identity, strict owner inequalities, and gate boundary are correct. A fresh
Windows Mathematica run returned

```text
countResidual=0
minimumResidual=0
lossResidual=0
stageOneLossResidual=0
stageTwoLossResidual=0
round42StrongerPhiReplayOK=True
```

Round 42 does not prove the sufficient sign
\(\mathcal T_{42}\geq0\), equation (R42.18), the endpoint, the complete
one-level-gap theorem, high-floor CST, the branching aggregate, or the
all-dimensional Pólya theorem. No state or proof-obligation status is
promoted by this audit.

## 1. Endpoint identity (R42.9)

Round 38 gives the exact scalar

\[
 \Phi_\delta^+=1-J+\Omega+B_0\zeta
 +(p+a_p)\Delta+2pe_p-\frac{p-dm}{2}.
\]

At the gap-side outer wall, \(y_B=0\) and
\(\theta_B=\pi\beta\). Hence

\[
 \Omega=\Omega_-+\omega_B,
 \qquad
 \omega_B=\frac{\pi}{2\theta_B}-1
 =\frac1{2\beta}-1.
\]

Substitution cancels the initial \(1\) and gives exactly

\[
 \Phi_\delta^+=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +(p+a_p)\Delta+2pe_p-\frac{p-dm}{2},
\]

which is (R42.9). The formula restores the full
\((p+a_p)\Delta\) term and does not pass through the smaller selected
projection \(\Gamma_{\rm OB}\).

## 2. Count and minimum algebra

The synchronized count is immediate from the definitions:

\[
 B_0+j=(B-1)+(f-B)=f-1=n.
\]

Thus (R42.2), including \(n\geq B_0\) because \(j\geq0\), is exact.

Let \(H=(p+a_p)R_1>0\) and \(M=\min\{\zeta,H\}\). The strict
adjacent-action estimate gives

\[
 B_0\zeta+(p+a_p)\Delta
 >B_0\zeta+H(j+e_p+h).
\]

The exact residual after subtracting the right side of (R42.11) is

\[
 B_0(\zeta-M)+j(H-M)\geq0.
\]

Both terms are nonnegative because \(M\leq\zeta\), \(M\leq H\),
\(B_0\geq1\), and \(j\geq0\). Therefore

\[
 B_0\zeta+(p+a_p)\Delta
 >nM+He_p+Hh
\]

with strictness inherited from the adjacent-action estimate. This verifies
(R42.11) without introducing a new owner split.

## 3. Exact owner chain

At \(\alpha\uparrow1^-\), \(\mu=q+1\). Using
\(G_a'(z)=-b_a(z)\),

\[
 h=G_\mu(q)=\int_q^{q+1}b_\mu(z)\,dz,
\]

whereas the outer-wall coordinate gives

\[
 u=G_K(q)-G_K(\mu)=\int_q^{q+1}b_K(z)\,dz.
\]

Since \(K>\mu\), one has \(b_K(z)>b_\mu(z)\) for
\(q\leq z<\mu\). Hence \(0<h<u\). The function \(b_K\) is strictly
decreasing, and the integration interval has length one, so

\[
 u< b_K(q)=\beta.
\]

Finally \(0<q/K<1\) implies
\(0<\arccos(q/K)<\pi/2\), hence \(\beta<1/2\). Therefore the complete
strict chain

\[
 0<h<u<\beta<\frac12
\]

is valid on the stated one-sided endpoint owner. The literal strict bracket
remains \(B-1\), while \(B\) is retained only as the one-sided gap label.

## 4. Loss identity (R42.17)

Define

\[
 \mathcal A_{\rm adj}=(p+a_p)
 [\Delta-R_1(j+e_p+h)]
\]

and

\[
 \mathcal A_{\rm cap}=
 \frac1{2\beta}-J-\frac9{10}.
\]

Using \(H=(p+a_p)R_1\), direct subtraction of

\[
 \mathcal T_{42}=\frac9{10}+B_0M+Hh-\frac{p-dm}{2}
\]

from (R42.9) gives

\[
 \begin{aligned}
 \Phi_\delta^+-\mathcal T_{42}
 ={}&\mathcal A_{\rm cap}+\Omega_-+\mathcal A_{\rm adj}\\
 &+B_0(\zeta-M)+jH+(H+2p)e_p.
 \end{aligned}
\]

This is exactly (R42.17). Each term is nonnegative. The strict sources are
the adjacent-action residual and the two components
\(1/(2\beta)-1>0\) and \(1/10-J>0\) of the cap residual. Thus equality in
\(\mathcal T_{42}\geq0\) would still imply
\(\Phi_\delta^+>0\).

The two-stage loss ledger is also consistent: before deleting the later
\(jM\) payment, the minimum step loses exactly

\[
 \mathcal A_{\rm adj}+B_0(\zeta-M)+j(H-M),
\]

and the remaining deletions recombine to (R42.17).

## 5. Replay scope and theorem boundary

The Mathematica companion checks only exact substitutions and algebraic
loss identities. It does not own the strict bracket, endpoint label,
adjacent-action inequality, cap inequalities, or the open sign of
\(\mathcal T_{42}\). Its final `True` is therefore consistent with the
note's structural status and is not a continuum sign proof.

The diagnostic binary64 minimum is explicitly non-load-bearing. No compact
certificate, ratio ladder, \(B_0\)- or \(j\)-indexed theorem family, or
verification chamber is introduced.

## 6. Gate decision

Round 42 correctly records the last stronger Gate-A pointwise route after
the Round 40--41 selected projection was exhausted. The remaining intrinsic
question is precisely (R42.18). Gate A remains active while that single sign
is pursued analytically.

If (R42.18) is certified false, or if proving it requires a forbidden
partition or new finite/compact certificate, Gate A stops and Gate B restores

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

with the exact shelf trapezoid, terminal surplus, cap, and inverse fractions.
Merely leaving (R42.18) open in this structural round does not itself trigger
Gate B and does not falsify \(\Phi_\delta^+\), \(\mathscr S\),
\(D_A(r)\), CST, or Pólya.

No edit was made to `state/proof_obligations.yml` or any theorem-status
graph.
