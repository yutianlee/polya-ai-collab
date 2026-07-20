# General-dimensional spherical-shell Pólya project
## Round 42: stronger upper-alpha specialization of \(\Phi_\delta^+\)

**Date:** 20 July 2026  
**Status:** structural Gate-A specialization; final intrinsic sign open

## 0. Theorem boundary

This note makes the one stronger pointwise attempt authorized after the
Round 40--41 selected projection was analytically exhausted.  It treats
only the one-sided gap-side endpoint

\[
 \chi=h,\qquad y_B=0,\qquad \alpha\uparrow1^-
\]

on the outer-\(B\) face.  It does not prove this endpoint, the complete
one-level-gap theorem, high-floor CST, the general-dimensional branching
backbone, or the all-dimensional Pólya theorem.  It makes no change to
`state/proof_obligations.yml`.

The binding methodology remains
`human/inbox/general-d_simplified_analytic_strategy.md` and
`human/inbox/general-d-strategy_r2.md`.  No ratio partition, theorem family
indexed by \(B\) or \(j\), chamber decomposition, or compact certificate is
introduced.

## 1. Exact owner and notation

Put

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}\pi,
 \qquad b_a(z)=\frac1\pi\arccos\frac za,
\]

\[
 x=r+p,\qquad q=x+m,\qquad \mu=q+1,
 \qquad K=\mu\sec t,\qquad 0<t<\frac\pi2,
\]

\[
 d=1-\frac{2t}\pi,\qquad
 \zeta=\frac d{1-d}=\frac\pi{2t}-1,
 \qquad W=G_K(\mu)=\frac\mu\pi(\tan t-t).
\]

The inherited grids are

\[
 r\in\mathbb N,\ r\geq1,
 \quad\hbox{or}\quad
 r\in\mathbb N_0+\frac12,\ r\geq\frac32,
\]

with \(p,m\in\mathbb N\).  The residual considered here has

\[
 p\geq3,\qquad p>dm.
\]

The Round 39 automatic result already owns \(p-dm\leq11/5\); hence a
genuinely live record may additionally be assumed to have
\(p-dm>11/5\), although that strengthening is not used in the algebra
below.

At the gap-side outer wall,

\[
 v=G_K(q)=B-\frac14,\qquad B_0=B-1\geq1.
\tag{R42.1}
\]

Here \(B\) is the one-sided gap label.  The literal strict bracket at the
wall is \(B-1\), not \(B\).  The endpoint keeps its
\(\alpha\uparrow1^-\) label and is not reindexed as the next chart's
literal \(\alpha=0\) point.

Let \(f\) be the first-shelf floor and put

\[
 j=f-B\geq0,\qquad n=f-1.
\]

Then the synchronized counts give the exact identity

\[
 \boxed{n=f-1=B_0+j\geq B_0.}
\tag{R42.2}
\]

Write

\[
 A(x)=f-\frac14+e_p,\qquad e_p\geq0,
\]

\[
 h=G_\mu(q),\qquad
 \beta=b_K(q),\qquad
 a_p=\frac{p^2}{3(2r+p)},
\]

\[
 U_z=\sqrt{\mu^2-z^2},\qquad
 R_1=\frac{U_r-U_x}{U_x-U_q},\qquad
 H=(p+a_p)R_1,
\]

and

\[
 M:=\min\{\zeta,H\}.
\tag{R42.3}
\]

The exact outer-wall coordinates are

\[
 \chi=h,\qquad y_B=0,\qquad
 A(x)-A(q)=j+e_p+h.
\tag{R42.4}
\]

Moreover, with \(u=v-W\),

\[
 0<h<u<\beta<\frac12,
 \qquad W=B_0+\frac34-u,
\tag{R42.5}
\]

Indeed, since \(\mu-q=1\),

\[
 h=\int_q^\mu b_\mu(z)\,dz,
 \qquad
 u=\int_q^\mu b_K(z)\,dz.
\]

Here \(K>\mu\) gives \(0<b_\mu(z)<b_K(z)\) for
\(q\leq z<\mu\), while the strict decrease of \(b_K\) gives
\(u<b_K(q)=\beta\).  Finally \(q>0\) gives \(\beta<1/2\).

The retained upper-alpha cap formulas are

\[
 h=
 \frac{\sqrt{2q+1}-q\arccos(q/(q+1))}\pi,
\tag{R42.6}
\]

\[
 J=
 \frac{\bigl((q+1)^2+2q^2\bigr)\arccos(q/(q+1))
       -3q\sqrt{2q+1}}{2\pi}.
\tag{R42.7}
\]

The old inverse levels remain in

\[
 \Omega_-=
 \sum_{k=1}^{B_0}
 \left(\frac\pi{2\theta_k}-\frac\pi{2t}+2\eta_k\right)\geq0.
\tag{R42.8}
\]

At a literal old inverse wall \(\eta_k=1\); on its adverse gap side
\(\eta_k\downarrow0\).  The newest event \(y_B=0\) is the outer-action
jump and is not counted again as an old inverse wall.

## 2. Exact stronger endpoint specialization

Before any adjacent-action estimate, the exact Round 37 endpoint scalar is

\[
 \boxed{
 \Phi_\delta^+=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +(p+a_p)\Delta+2pe_p-\frac{p-dm}{2},}
\tag{R42.9}
\]

where \(\Delta=A(r)-A(x)\).  This is an identity for
\(\Phi_\delta^+\), not an identity for the shifted defect.

Round 38 proves, at the actual action drop (R42.4),

\[
 \Delta>R_1(j+e_p+h).
\tag{R42.10}
\]

The one-line minimum algebra used in (R38.18), specialized directly at
\(\chi=h\), therefore gives

\[
 B_0\zeta+(p+a_p)\Delta
 >nM+He_p+Hh.
\tag{R42.11}
\]

Substitution in (R42.9) proves the endpoint-specific strengthening

\[
 \boxed{
 \Phi_\delta^+>
 \frac1{2\beta}-J+\Omega_-
 +nM+H(e_p+h)+2pe_p-\frac{p-dm}{2}.}
\tag{R42.12}
\]

This is the specialization one line before Round 38 replaces the
\(Hh\) payment by
\(h\min\{H,2/\beta\}\).  At \(\chi=h\), the newest inverse displacement
is exactly zero and the adjacent action owns the whole \(Hh\) payment.
Thus (R42.12) is genuinely stronger than merely substituting
\(\chi=h\) in the printed right side of (R38.20).

Now use only (R42.2), \(e_p\geq0\), \(\Omega_-\geq0\),
\(\beta<1/2\), and the proved cap bound \(J<1/10\).  This yields the
single clean sufficient target

\[
 \boxed{
 \mathcal T_{42}:=
 \frac9{10}+B_0\min\{\zeta,H\}+Hh
 -\frac{p-dm}{2}.}
\tag{R42.13}
\]

Indeed,

\[
 \boxed{\Phi_\delta^+>\mathcal T_{42}.}
\tag{R42.14}
\]

Consequently \(\mathcal T_{42}\geq0\), including equality, would close
this endpoint through the inherited implication from
\(\Phi_\delta^+\) to the shifted defect.  No sign of
\(\mathcal T_{42}\) is proved in this note.

## 3. Complete loss ledger

The endpoint loss can be printed without hiding any reserve.  Define the
strict adjacent-action residual

\[
 \mathcal A_{\rm adj}:=
 (p+a_p)\left[\Delta-R_1(j+e_p+h)\right]>0
\tag{R42.15}
\]

and the cap/angular residual

\[
 \mathcal A_{\rm cap}:=
 \frac1{2\beta}-J-\frac9{10}
 =\left(\frac1{2\beta}-1\right)
  +\left(\frac1{10}-J\right)>0.
\tag{R42.16}
\]

Direct substitution of \(n=B_0+j\) and \(M=\min\{\zeta,H\}\) into
(R42.9) gives the exact difference identity

\[
 \boxed{
 \begin{aligned}
 \Phi_\delta^+-\mathcal T_{42}
 ={}&\mathcal A_{\rm cap}+\Omega_-+\mathcal A_{\rm adj}\\
 &+B_0(\zeta-M)+jH+(H+2p)e_p.
 \end{aligned}}
\tag{R42.17}
\]

Every term on the right is nonnegative and three displayed sources are
strict.  In particular, (R42.13) does not silently merge the old inverse,
floor, cap, or adjacent-action losses.

The full inherited ledger is therefore

| transition | status | retained or discarded reserve |
|---|---|---|
| \(D_A(r)\to\mathscr S\) | inherited lower bound | first-shelf reduction slack remains outside this note |
| \(\mathscr S\to\Phi_\delta^+\) | inherited sufficient projection | exact terminal tangent and shelf-trapezoid surplus are not claimed lossless |
| (R42.9) | exact endpoint identity | retains \(J,\Omega_-,B_0\zeta,\Delta,e_p\) |
| (R42.9)\(\to\)(R42.12) | strict adjacent-action/minimum bound | loses exactly \(\mathcal A_{\rm adj}+B_0(\zeta-M)+j(H-M)\) before the later \(jM\) deletion |
| (R42.12)\(\to\)(R42.13) | nonnegative deletion and sharp cap bound | discards \(\Omega_-\), \(jM\), \((H+2p)e_p\), \(1/(2\beta)-1\), and \(1/10-J\) |
| total | exact identity | all discarded terms recombine as (R42.17) |

The earlier selected projection \(\Gamma_{\rm OB}\) additionally loses
the reserve \(a_p(\Delta-M_4)\).  Round 42 does not pass through that
projection and therefore restores that reserve before applying
(R42.10).

The algebra-only companion
`computations/general_d_round42_stronger_phi_replay.wl` checks (R42.2),
the minimum decomposition in (R42.11), the two stage losses, and the total
identity (R42.17).  It ends in
`round42StrongerPhiReplayOK=True`.  Mathematica owns none of the strict
owner inequalities or the open sign (R42.18).

## 4. Diagnostic-only check

As theorem-design evidence only, the existing bounded exact-endpoint
dataset generated by
`computations/general_d_round39_outer_face_diagnostic.py` was reevaluated
with (R42.13).  It contains 406 retained one-sided upper-alpha/outer-\(B\)
samples satisfying the literal grid, shelf, activity, hard-sector, count,
and gap-owner checks.

The observed binary64 minimum was approximately

\[
 \min \mathcal T_{42}\approx0.3854774009.
\]

It occurred at the sampled record
\((r,p,m,f,B,j)=(1,5,1,2,2,0)\).  This finite minimum is not an interval
bound, does not prove a continuum sign, and is not used in Sections 1--3.
No computer certificate is proposed.

## 5. Remaining obligation and gate decision

The exact remaining Gate-A question is now:

\[
 \boxed{
 \frac9{10}+B_0\min\!\left\{
 \frac\pi{2t}-1,
 (p+a_p)\frac{U_r-U_x}{U_x-U_q}
 \right\}
 +(p+a_p)\frac{U_r-U_x}{U_x-U_q}\,G_{q+1}(q)
 \geq\frac{p-dm}{2}}
\tag{R42.18}
\]

on the complete exact owner in Section 1, with
\(G_K(q)=B_0+3/4\) and
\(W=B_0+3/4-u\), \(0<h<u<\beta<1/2\).

This is one intrinsic count--phase/radial compensation inequality.  A
proof must use the exact outer-wall coupling; it may not split into a
\(B_0\)-indexed family, a ratio ladder, or fixed verification chambers,
and it may not replace \(J,W,u,e_p,\Omega_-\), and the shelf action by
unrelated worst cases.  Round 42 supplies no such proof, so the endpoint
and all downstream theorems remain open.

This is the last stronger pointwise projection attempt authorized after
Round 41.  If (R42.18) is false, or if completing it requires any forbidden
partition or a new finite/compact certificate, Gate A stops.  The next
authorized step is Gate B: restore

\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}
\]

with the exact shelf trapezoid, terminal surplus, cap, and inverse
fractions.  Failure to sign (R42.18) in this bounded note is not itself a
counterexample to \(\Phi_\delta^+\), \(\mathscr S\), \(D_A(r)\), CST, or
Pólya; it authorizes no theorem-status promotion.
