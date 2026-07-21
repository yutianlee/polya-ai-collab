# Current State

Date: 20 July 2026

The authoritative mathematical state is `state/proof_obligations.yml`.
It contains 124 unique obligations, selects
`SHELL-general-d-high-floor-first-drop-CST`, and has SHA-256
`a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.

## Theorem status

The repository records a project-internal proof of the sharp Dirichlet Pólya
inequality for every genuine three-dimensional spherical shell

\[
A_{r,R}=\{x\in\mathbb R^3:r<|x|<R\},\qquad 0<r<R.
\]

With strict counting

\[
N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\},
\]

the result is

\[
N_D(A_{r,R},\Lambda)
\leq \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
=L_3|A_{r,R}|\Lambda^{3/2},
\qquad L_3=\frac1{6\pi^2}.
\]

This is an internal result for the spherical-shell class. It is not a proof of
the general Pólya conjecture and is not a claim of novelty, priority, external
peer review, or publication readiness.

## Revision 2 reviewed proof

For the unit shell, write \(K=\sqrt\Lambda\). The exact disjoint cover is

\[
\begin{array}{ll}
K\leq\pi/(1-\rho):
  &N_D(A_{\rho,1},K^2)=0,\\[2mm]
K>\pi/(1-\rho),\quad 0<\rho<39/50:
  &N_D\leq P<W,\\[2mm]
K>\pi/(1-\rho),\quad 39/50\leq\rho<1:
  &N_D<W\quad\text{by the optical theorem}.
\end{array}
\]

The low/middle-ratio inequality is the ratio-sharp retained-remainder theorem.
It uses:

1. the strict phase-to-proxy bridge and exact layer cake;
2. the ratio-dependent angular cap
   \(q\leq\arccos(\rho)/\pi\);
3. the tangent minorant \(L_\sharp\leq\mathfrak W\);
4. reduction to the universal ball quarter-layer; and
5. exact base and derivative convexity proving \(W-P>0\).

The seam \(\rho=39/50\) is optical-owned. The face
\(K=\pi/(1-\rho)\) is no-mode-owned. Strict radial and angular walls remain
strict throughout.

## Dependency state

The live theorem chain is

\[
\begin{gathered}
\text{phase/count/Sturm--Liouville}
\longrightarrow
\texttt{SHELL-analytic-retained-remainder-closure},\\
\texttt{SHELL-analytic-retained-remainder-closure}
\quad+\quad
\texttt{SHELL-rho-one-endpoint}
\longrightarrow
\texttt{SHELL-rho-uniformity}
\longrightarrow
\texttt{TARGET-shell-d3}.
\end{gathered}
\]

The completed three-dimensional chain is unchanged. The former \(\rho_*\) owner,
finite staircases, 38-state theorem, residual sets, zero/event registry,
611-row ledger, and interval or executable certificates have no live theorem
implication. They remain in the historical archive and as optional regression
material.

The old d=3 low-interface shifted-tail target remains detached and is not a
premise of the extension.  The general-dimensional track instead has explicit
real-order, easy-tail, one-interface, shelf-identity, retained-sector,
no-mode, residual, and final-assembly nodes.  The double-sawtooth/packing node
remains diagnostic only.

## General-dimensional extension status

The all-dimensional theorem is proposed, not proved.  The real-order phase
proxy and the preserved branching, signed-primitive, and master-defect
backbone are separate `derived_under_assumptions` nodes awaiting a frozen
independent audit.  The easy tails, complete one-interface theorem, shelf
identities, dimension-dependent no-mode theorem, first-floor first-drop
sector, and (f\ge2) no-drop sector are represented as proved modules.

Round 10 proves the fractional terminal reserve in
`human/outbox/general-d-round-10-fractional-terminal-reserve-and-shelf-terminal-compensation.md`.
It restores every strict inverse fraction (2\eta_k), defines the inverse
displacement correctly, and retains the local cap correlation.  The repaired
independent audit passes, so this node is `proved_internal`.

The completed WP2 obligation is `SHELL-general-d-first-floor-no-drop`.  The
remainder-rich and (B\ge2) sectors are closed.  Round 11 proves the (B=0)
endpoint corner analytically, and its independent audit passes with only
nonblocking diagnostic-wording caveats.  Round 12 validly reduces a lossy
(B=1) pre-shelf scalar to an endpoint, but Round 13 supplies an exact rational
counterexample on the new integer extension grid.  At
\(\theta=8899/100000\), \(q=9998\), \(n=50\), \(r=9948\), and
\(\alpha=999/1000\), the proposed lower scalar is below \(-3/2\), while the
exact defect is approximately \(39.2503>0\).  Thus only the surrogate sign is
rejected.

Round 14 restores the exact no-drop head
\(H_n=2\int_r^q(A_\alpha(s)-1)\,ds\) and exact cap \(2\delta\).  It proves
\(D_A(r)\ge\Xi(\alpha)>\Xi(\bar\alpha)\).  Round 15 then proves the exact
count

\[
 T_A(r)=1+2n+2[y]_<,
\]

the lossless identity

\[
 D_A(r)=2J_K(r)-2J_{q+\alpha}(r)
 -(1+2n+2[y]_<),
\]

and its strict move to the first phase, branch, or owner-activity endpoint.
This reduction passed an independent audit.

At the endpoint \(a=q+\bar\alpha\), Round 16 discards only the favorable
\(2\eta\), minimizes the remaining scalar at the unique \(A(x)=1\), and
proves

\[
 D_A(r)>\Omega_{\rm end}
\ge2F(K,a)-1+2\eta,
\qquad
 F=J_K(x)-J_a(x)-(z-x).
\]

It reduces the endpoint sign to \(F\ge1/2\) on
\(a\ge2\), \(K-a>\pi\), \(A(a-1)\ge3/4\), \(z>2\); proves \(F_K>0\);
and gives a positive exact rational reserve on the suspected
\(q=3,r=1,n=2\) double face.  Its independent audit passes.

Round 17 treats the remaining action boundary \(A(a-1)=3/4\).  Its exact
quantile decomposition has a comparison function \(Q\) that is strictly
increasing and concave with \(Q(g)>0\).  Round 18 then proves the literal
simultaneous radial/action wall has

\[
 F-\frac12>\frac{1443}{449440}>0.
\]

Round 19 bypasses the formerly selected chord scalar.  A one-radius Jensen
reduction and two intrinsic inequalities prove \(dF/da>0\) on the full
strict action face.  Its finite \(a=8\) radical/angle certificate and all
symbolic identities replay exactly in Mathematica, and its independent audit
passes.  Together Rounds 16, 18, and 19 close \(F(K,a)>1/2\) and the hard
\(B=1\) endpoint.  A gap-free independent integration audit then checks the
full \(B=0,1,\ge2\) phase union, both new extension grids, the lower action
owner, inverse zero extension, owner-dimensional activity, every strict wall,
and an exact proof that \(z=2\) is redundant.  It reports PASS with no
uncovered phase, so WP2 is `proved_internal`.

This selected extension starts at (r=1) on the integer grid and (r=3/2) on
the half-integer grid.  The Round 13 counterexample shows why the exact head
and cap must remain correlated; it is not a counterexample to the first-floor
theorem.

The selected pointwise target is one high-floor first-drop CST theorem.
Round 20 evaluates the exact correlated scalar \(\mathscr S\), the Round 10
lower surrogate \(\Phi_\delta\), and their loss ledger on 19,619 active
interior, shelf-wall, interface-wall, and one-sided inverse-spatial records.
A fresh independent Mathematica 15 replay passes with no sampled negative;
the smallest sampled values are about \(1.28430\) and \(0.837805\),
respectively, at the corrected \(G_K(7)=3/4\), \(y_1=2\) hard face.  This is
floating-point falsification evidence only.

Round 21 then proves an analytic intrinsic reduction.  On the extension
grids it gives the uniform cap \(J<1/7\), extracts the complete interface
levels and retained top interval as a terminal payment, and combines shell
elasticity with curvature into a simultaneous shelf payment.  With

\[
 \alpha=
 \frac{\pi(f-\frac14-\lambda)\cos\theta}
 {\sin\theta-\theta\cos\theta}-r-p-m\in[0,1),
\]

the lower surrogate satisfies \(\Phi_\delta>\mathcal R\), where
\(\mathcal R\) is the explicit scalar in Round 21 equation (4.4).  The
independent current-hash audit passes after two local strictness/citation
repairs.

Round 22 shows why the exact cap cannot be replaced at the last line.  At the
exact active tuple

\[
 K=261/20,\quad \mu=699/100,\quad \rho=233/435,\quad
 (r,n,p,m,q,f,B_0)=(1,5,3,2,6,2,1),
\]

directed Arb arithmetic and an independent multi-precision replay prove
\(\mathcal R<-1/300\).  This falsifies only the coarse sufficient sign, not
\(\Phi_\delta\), CST, or the exact shifted-tail theorem.  Retaining
\(J=2I_\mu(q)\) defines

\[
 \mathcal R_J=\mathcal R+\frac17-J,
 \qquad \Phi_\delta>\mathcal R_J
\]

throughout the same feasible domain, and the certified tuple has
\(\mathcal R_J>1/20\).  At the end of Round 22 the selected open inequality is
therefore
\(\mathcal R_J\ge0\), with the exact cap retained to the last line.

Round 23 supplies a further audited analytic reduction.  Because
\(p,m\ge1\), it proves \(q\ge3\) and the exact rational cap bound
\(J<2I_4(3)<1/8\).  Substituting only at this final comparison gives

\[
 \mathcal R_J>\mathcal C_8,
\]

where \(\mathcal C_8\) is equation (3.2) of the Round 23 note.  For fixed
\((r,p,m,f,\alpha)\), this scalar is strictly convex on every literal
\(B_0\)/top-payment cell, so a possible failure lies at an exact shelf,
activity, action, or top-payment wall, or at the cell's unique stationary
point.  The one-sided face \(\lambda\downarrow0\) keeps
\(\mathcal E\to1\).  The reported 77,391-cell sweep and limiting value
\(0.01286445\ldots\) at
\((r,p,m,f,B_0)=(1,3,2,2,1)\), \(\alpha\uparrow1\), are diagnostic only.
At the end of Round 23, \(\mathcal C_8\ge0\) was the selected stronger
sufficient inequality.  Its later falsification does not affect the proved
convex-cell reduction or the strict inequality \(\mathcal R_J>\mathcal C_8\).

Round 24 then proves two further exact reductions.  At fixed
\(x=r+p\), the feasible positive integer shelf lengths form a prefix and the
only \(p\)-dependent term has second derivative
\(6k(x-p)=6kr>0\).  Thus at most two adjacent \(p\)-owners remain, computed
at the same \(t\).  On the delicate cell
\(B=B_0=f-1\), \(0<u=W-(f-1)<1/\sqrt2\), the terminal action identity gives

\[
 \mu=\frac{\pi(B+u)}{\tan t-t},
 \qquad q\le\mu<q+1,
\]

eliminating \(\alpha\) exactly in the specialized scalar
\(\widehat{\mathcal C}_8\).  Along the lower shelf wall it also proves
\(t_\mu<0\), \(W_\mu<0\), and \(\lambda_\mu>0\).  The independent audit
required two scope repairs: the \(t\)- and \(p\)-candidate conditions are
coupled, not a precomputed Cartesian product, and
\(\widehat{\mathcal C}_8\) applies only on that delicate cell.  Other cells
were not reduced by this step.  The 40,569-tuple replay found no
negative value but also showed diagnostically that global
\(\alpha\)-monotonicity and bare lower-wall dominance are not valid proof
premises.  At the end of Round 24, the blocker was the coupled
stationary-value inequality.

Round 25 now resolves the algebra of that delicate interior stationary point.
With

\[
 H=\tan t-t,\quad z=\tan(t/2),\quad
 L=\frac{4u(B+u)\tan^2t}{H},\quad
 R=\frac m\pi+\frac{B\pi}{2t^2}-L,\quad
 P=\frac{3\pi^2(B+u)R}{H\sin t},
\]

stationarity implies \(R>0\) and the exact identity

\[
 \mathcal C_8=
 m\left(\frac12-\frac t\pi+\frac z\pi\right)
 +B\left(\frac\pi{2t}-1+\frac{\pi z}{2t^2}\right)
 -\frac p2-\frac18+2u^2-zL.
\]

Let \(\psi(P)\) be the positive root of \(\psi^2(2\psi+3)=P\).  The paired
shelf integrals yield the strict \(m\)-window, while stationarity and the
interface/owner constraints give
\(p\le p_{\max}=\min\{\mu-m-1,\psi(P)\}\).  Hence
\(\mathcal C_8\ge\mathcal F(B,m,t,u)\).  The independent audit verifies every
identity, strict face, and inequality direction.  Directed Arb arithmetic at
the relaxed rational point
\((B,m,t,u)=(1,11,1/5,1/1000)\) proves
\(\mathcal F<-34.18\), showing that the endpoint \(m\)-window alone is
insufficient.  This point is not on the exact shelf image and does not
falsify \(\mathcal C_8\) or CST.  At the end of Round 25, the proposed next
target was \(\mathcal F\ge0\) on the full projection of both paired shelf
integrals, the interface strip, activity, parity grid, stationarity, and
coupled \(p\)-owners.

Round 26 reconstructs that full projection without the endpoint relaxation.
On either parity grid, fixed \((B,m,t,u)\) determines \(\mu,q,\alpha\), and
\(x=q-m\); stationarity permits at most one positive integer \(p\) through

\[
 p^2(3x-p)=P,
\]

because the left side is strictly increasing on \(0<p<x\).  The certified
half-grid tuple

\[
 (B,f,m,r,p,\alpha,\mu)
 =\left(1,2,6,\frac{25}{2},6,\frac9{10},\frac{127}{5}\right)
\]

lies in the full paired-shelf, activity, literal-cell, stationary, parity,
and unique coupled minimizing-owner image, but satisfies

\[
 \mathcal F<-\frac1{50}<0<\frac{77}{50}<\mathcal C_8.
\]

Thus the replacement of the actual owner \(p\) by \(p_{\max}\) is genuinely
lossy even on the exact image, and \(\mathcal F\ge0\) is rejected.

Round 26b separately certifies an exact feasible half-grid point

\[
 r=\frac{57755}{2},\quad p=80,\quad m=15,\quad f=2,
 \quad \alpha=\frac12,
\]

and a nearby unique stationary point with \(\mathcal C_8<-7\).  Hence the
curvature-only sign \(\mathcal C_8\ge0\) is also rejected on the exact
domain.  This is not a CST counterexample.  At the same witness,

\[
 \mathcal R_J
 =\mathcal C_8+(p+a_p)(L_0-L_{\rm curv})+\left(\frac18-J\right)
 >20,
\]

because \(L_0\) is the elasticity branch and the exact cap reserve is
positive.  A combined independent audit replayed all Arb decisions at 128,
256, 512, and 1024 bits and used Mathematica 15 to check the symbolic
residuals.

Round 27 certifies that restoring the literal maximum is still not enough to
create a valid global lower-scalar sign.  At
\[
 (r,p,m,f,\alpha,\mu,t)
 =\left(4036,32,1,2,\frac1{16},\frac{65105}{16},\frac{79}{500}\right),
\]
all exact shelf, activity, parity, interface, literal-cell, and top-payment
conditions hold, while
\[
 \mathcal C_{\max,8}<-\frac43,
 \qquad \mathcal R_J<-\frac65.
\]
The same certified tuple has
\(\mathscr S>47\) and \(\Phi_\delta>40\), with more than 14 units of terminal
reserve and 27 units of shelf reserve discarded before \(\mathcal R_J\).
Thus this is not a counterexample to the exact scalar, CST, or the theorem.

The analytic repair is the intrinsic remainder-rich split required by the
revised strategy.  Put \(d=1-2t/\pi\) and
\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p,
 \qquad E_*=\frac12-\frac{dm}{2p}.
\]
The exact Round 10 lower scalar gives
\[
 D_A(r)\ge
 \Phi_\delta^+
 =\max\{0,L_T\}+a_p\Delta+p(E-E_*).
\]
Therefore every tuple with \(p\le dm\) or \(E\ge E_*\) is closed.  The Round
27 negative witness has \(E>1>E_*\) and lies far inside this automatic
sector.  The sole live pointwise blocker is now
\[
 p>dm,\qquad 0\le E<E_*<\frac12,
\]
with exact residual
\[
 \max\{0,L_T\}+a_p\Delta\ge p(E_*-E).
\]
On this sector the sharpened elasticity relation
\(\Delta\ge (s-1)(E+2\lambda)/(s+1)\) is available.  The conditional sign
\(\mathcal C_{\max,8}\ge0\) is a stronger sufficient target only here; it is
not equivalent to the residual and it does not contain \(J\).  A broad exact-
domain diagnostic found no hard-sector negative, but provides no continuum
coverage.

Round 28 now makes the exact residual strictly less lossy.  Define
\[
 \mathcal K_4=
 \frac{(\mu^{-1}-K^{-1})((r+p)^2-r^2)}{2\pi}
 +\frac{(\mu^{-3}-K^{-3})((r+p)^4-r^4)}{24\pi},
\]
\[
 \tau=\frac{s-1}{s+1},\qquad
 M_4=\max\{\tau(E+2\lambda),\mathcal K_4\}.
\]
The audited analytic chain is
\[
 D_A(r)\ge\Phi_\delta^+
 \ge\Psi^{L_T}_{4,E}
 :=\max\{0,L_T\}+a_pM_4+p(E-E_*)
 \ge\Psi^{\rm rf}_{4,E}.
\]
The strict gain \(\Delta>\mathcal K_4\) follows from the first two positive
terms of the binomial expansion of \(\sigma'\).  The primary scalar retains
the actual \(E\), every inverse fraction, the exact cap, and the top interval.
Its continuum sign remains open.

Independently, Round 28 proves that \(H(t)=E(t)-E_*(t)\) is strictly
increasing wherever \(p>d(t)m\), so the hard set is one initial phase
interval.  It also gives a unique elasticity/curvature switch and a finite
candidate list for conditional \(\mathcal C_{\max,8}\).  Those candidate
signs remain auxiliary.  Fresh audited diagnostics found no negative, but
they are floating experiments only: the smallest sampled
\(\Psi^{L_T}_{4,E}\) is about \(0.879294\) at the curvature-owned bad side
\((r,p,m,f,\alpha)=(1,2,2,2,0)\), \(y_1\downarrow2^+\).

Round 29 now proves three exact reductions.  First,
\(\Psi^{L_T}_{4,E}\) is strictly increasing in \(t\) on every fixed-
\(\alpha\) literal terminal count cell.  Its raw terminal jumps are
\(-2\) at an inverse wall, \(-1\) at a \(Q\)-wall, and
\(-1/(16\beta)\) at an outer \(B\)-wall, with clipping and literal ownership
retained.  Second, on the inherited extension grids it is strictly
decreasing in \(\mu\) on every fixed-\(Q\), constant-\(K\) inverse or
outer-\(B\) wall segment.  Thus neither a cell interior nor such a wall
interior can contain the missing minimum.  Third, throughout the primary
component
\[
 (r,p,m,f)=(1,2,2,2),\qquad B=Q=1,\qquad 2<y_1<3,
\]
the exact estimate is
\[
 \Psi^{L_T}_{4,E}>
 \frac{371}{15840}+2\eta_1+2E>0.
\]
Mathematica returns twelve zero derivative/wall residuals, and the exact
rational replay verifies the displayed margin.  An adaptive diagnostic finds
a smaller positive wall--wall cusp, about \(0.8374553252\), at
\(\alpha\approx0.0384220379\); its opposite one-sided derivatives disprove
global \(\alpha\)-monotonicity but imply no continuum sign.

Round 30 now proves the first nonconstant-\(K\) face package.  Throughout
the \(B=Q=1,\ 2<y_1<3\) band, the strengthened activity condition is
automatic.  On the included lower shelf \(e_p=0\), the complete terminal
term is strictly increasing in \(\mu\) and obeys

\[
 L_T>\frac7{10}.
\]

The full scalar has the retained-\(E\) lower bound

\[
 \Psi^{L_T}_{4,E}>
 \mathfrak F(q,r,p,m)
 =
 T(q)+a_p\mathcal K_{4,\min}
 +p\left(E_{\min}-\frac12\right)
 +\frac{m d_{\min}}2.
\]

Necessary shelf/hard conditions are

\[
 G_{K_3}(q-m)-G_q(q-m)\ge\frac74,\qquad
 p>d_{\min}m,\qquad
 E_{\min}<\frac12-\frac{d_{\min}m}{2p}.
\]

The open lower \(Q\)-wall instead has \(0<y_1<\alpha<1\), no inverse or
outer-\(B\) intersection, and a positive strictly increasing terminal term.
Thus no \(y_1>1\) band has a noncorner lower-\(Q\) endpoint.  On
\(\alpha=0,\ f=2\), all first-band candidates with
\(4/5\le t<13/10\) are positive.  The Mathematica replay returns seventeen
zero identities, and the independent audit passes.

Round 31 proves three further analytic conclusions.  First, the dependent
profile \(p\mapsto\mathfrak F(q,q-m-p,p,m)\) is strictly convex for every
fixed \((q,m)\) on its full continuous domain.  At integration radius \(a\), with
\(u=r/a\), \(v=p/a\), and \(u+v<1\), its second-derivative kernel is

\[
 D(u,v)=\frac{2u}{\sqrt{1-u^2}}+
 v\left(1+\frac{u^2}{2}+\frac{v^2}{3}
 -(1-u^2)^{-3/2}\right)>0.
\]

Second, the exact three necessary shelf/hard conditions have no solution for
any real \(q\ge1000\).  Writing \(s=q^{1/3}\), feasibility forces
\(m>11s/10\).  A retained-\(E\), shell-ratio-free implication bootstrap

\[
 1\to\frac{25}{17}\to\frac53\to2\to\frac{25}{11}
 \to\frac52\to3\to4\to10
\]

for \(p/(d_{min}m)\) then contradicts the hard bound
\(E_{\min}<1/2-d_{\min}m/(2p)\).  Thus the retained shelf is confined to
\(q<1000\).  Separately, \(E_{\min}>\mathcal K_{4,\min}\) and
\(T(q)>7/10\) give a weaker finite lower scalar \(L_q\) with no interior minimum;
its minimum on each full parity-grid triangle reduces to the three strictly
convex edges \(p=1\), \(r=r_0\), and \(m=1\).

Round 32 keeps the necessary shelf feasibility before using that weaker
scalar.  For every real \(q\ge35\), with
\(\psi=\arccos(q/K_3)\), it proves the strict self-bootstrap
\[
 m>\frac65\left(\frac{\pi}{\psi}-3\right).
\]
Thus the finite triangle has
\(m\ge m_0=\lfloor(6/5)(\pi/\psi-3)\rfloor+1\); for \(q<35\), the
untruncated boundary \(m_0=1\) is retained.  The \(p=1\) edge satisfies
\(L_q>1/5\).  One compact 192-bit directed-Arb certificate encloses the
continuous convex minima on \(r=r_0\) and \(m=m_0\) for all 1994 exact
integer and half-integer values \(3\le q<1000\) and proves both edges
larger than \(1/100\).  Together with the Round 31 real \(q\ge1000\)
exclusion, this closes the entire Round 30 included retained-\(E\) shelf.
The false untruncated points at \(q=79/2\) and \(q=40\) are retained as
regressions showing that the \(m\)-truncation is load-bearing.

Round 33 treats the first live wall outside that shelf.  On
\(A(q)=3/4\), \(0<\alpha<1\), exact phase comparison gives \(W<3/4\),
while the high-floor first drop retains
\(A(x)-A(q)=f-1+e_p\ge1\).  With \(H=E-E_*\), the lower-\(Q\) transport
factorization and two elementary trigonometric estimates give
\[
 \frac{dH}{d\mu}<0
\]
throughout every feasible hard segment.  Therefore a hypothetical hard
component cannot terminate in the smooth wall interior; in the increasing-
\(\mu\) direction it reaches \(e_p=0\), the activity wall, or
\(\alpha\to1^-\).  This result does not prove monotonicity of
\(\Psi^{L_T}_{4,E}\) and does not close the signs at those three exits.

Round 34 proves that the activity wall is actually disjoint from every
high-floor first shelf, with exact activity margin \(>1/16\).  It also
expresses the preceding shelf variation and terminal action through the same
radial-parameter integral.  Strict Jensen and trapezoid quadratures, combined
before scale elimination, reduce lower-\(Q\) hard-sector exclusion to the
intrinsic \(Q\to1^-\) face
\[
 \frac{2P(2z+P)}{\{b(z)+b(z+P)\}D}>
 \frac{P-d(t)M}{2P}
\]
and a finite radius/stationary alternative.  The small-phase adjacent-action
theorem closes \(0<t\le\pi/8\).  Round 35 closes
\(\pi/8\le t\le\pi/6\) by a retained quadrature estimate, closes the
large-phase radius boundary with one exact polynomial, closes the possible
stationary root by an action-cutoff discriminant, and proves the transported
domain empty for \(t\ge3\pi/14\).  Hence the lower-\(Q\) hard sector is
closed analytically, with no ratio seam or interval certificate.

Round 36 proves the exact global count gap
\[
 B-Q\in\{0,1\},\qquad 0\le Q\le B\le f.
\]
For \(\alpha>0\), each outer-\(B_N\) wall precedes the matching \(Q_N\)
wall; the strip between them is exactly \(B=Q+1\).  On that strip, including
old inverse bad sides,
\[
 L_T>1-J>\frac67,
 \qquad
 \Psi^{L_T}_{4,E}>\frac67-\frac{p-dm}{2}.
\]
Thus the full selected scalar is positive for \(p-dm\le12/7\), in
particular for every hard \(p=1\) gap face.  At higher \(Q_N\) walls the
newest root obeys \(0<y_N<\alpha<1\) and gives \(L_T>3G_\mu(q)>0\), but
that terminal sign alone does not pay the negative shelf term.

Round 37 synchronizes the residual hard one-level gap:

\[
 B_0=Q=B-1\ge1,
 \qquad j=f-B=\lfloor\lambda\rfloor,
 \qquad j\le\lambda<j+1.
\]

The terminal top interval is exactly zero.  With the exact positive reserve
\(\Omega\) and \(\Xi=E-M_4\ge0\), the selected scalar has an exact form
relative to that selected projection:

\[
 \Gamma_{\rm gap}
 =1-J+\frac{B_0d}{2c}+\Omega
 +(p+a_p)M_4+p\Xi-\frac{p-dm}{2}.
\]

The stronger endpoint scalar also satisfies the count-free strict bound
\(\Phi_\delta^+>\mathcal H_\Delta\), where \(\mathcal H_\Delta\) retains the
maximum of the correlated elasticity, quartic-curvature, and adjacent-action
payments.  This is not lossless relative to \(\Phi_\delta^+\) or \(D_A(r)\).

Round 38 sharpens the gap coordinate.  With \(u=\lambda-j\),
\(S_q=A(q)-W\), and \(\chi=u-S_q\), every literal positive-alpha gap owner
satisfies

\[
 0<S_q\le u<S_q+h<\frac{\alpha}{2},
 \qquad 0\le\chi<h,
 \qquad 0<u<\frac{\alpha}{2}<\frac12.
\]

Thus no finite integer-\(\lambda\) wall lies in the positive-alpha gap.  It
also proves the count--phase compensation

\[
 B_0\zeta>\frac15,\qquad \zeta=\frac{\pi}{2t}-1,
\]

and, after writing
\(\widehat\Xi=\Delta-M_4\ge0\), obtains

\[
 \Gamma_{\rm gap}>
 \frac{37}{35}-\frac{p-dm}{2}.
\]

Consequently every one-level gap with
\(p-dm\le74/35\) is closed, including every residual \(p=2\) gap; \(p=1\)
was already closed in Round 36.  The remaining gap work has \(p\ge3\).
Round 38 also proves one unified \(Q\)-wall/outer-\(B\) compensation bound
that retains \(\chi\), the newest inverse level, \(\Omega_-\), and the actual
adjacent action.  This is a proof-level lower bound for
\(\Phi_\delta^+\), not a new certificate and not yet a sign on every
\(p\ge3\) endpoint.  The obligation graph is intentionally unchanged in
Round 38.

Round 39 sharpens the residual cap.  With \(x=r+p\) and \(q=x+m\), residual
\(p\ge3\) implies \(q\ge5\), and
\[
 J<2I_{q+1}(q)\le2I_6(5)<\frac1{10}.
\]
Consequently
\[
 \Gamma_{\rm gap}>
 \frac{11}{10}-\frac{p-dm}{2},
\]
so every gap with \(p-dm\le11/5\) is closed.  A surviving \(p=3\) gap must
satisfy \(dm<4/5\).

On the gap-side outer-\(B\) wall, put \(x=r+p\),
\(\beta=\pi^{-1}\arccos(q/K)\), \(v=G_K(q)\),
\[
 U_z=(\mu^2-z^2)^{1/2},\qquad
 g=\frac{U_r}{U_x}-1,\qquad
 R_1=\frac{U_r-U_x}{U_x-U_q}.
\]
The selected scalar has the exact outer-face form
\[
 \Gamma_{\rm OB}=
 \frac1{2\beta}-J+\Omega_-+(v-\tfrac34)\zeta
 +p\Delta+a_pM_4+2pe_p-\frac{p-dm}{2},
\]
and satisfies the single intrinsic bound
\[
\begin{aligned}
 \Gamma_{\rm OB}>F_{\rm OB}:={}&
 \frac1{2\beta}-J+\Omega_-+(v-\tfrac34)\zeta\\
 &+pR_1[A(x)-A(q)]+a_pg[A(x)-W]+2pe_p
 -\frac{p-dm}{2}.
\end{aligned}
\]
The loss is exactly the sum of the positive adjacent-action and elasticity
remainders.  The optional root-free projection retains
\[
 \Omega_-\ge
 \frac{\pi^2}{2Kt^3\sin t}
 (v-\tfrac34)(W-\tfrac v2+\tfrac18).
\]
Neither expression is a new certificate or a theorem family indexed by a
count, floor, or shell ratio.

At the simultaneous outer-\(B\)/lower-shelf endpoint, the exact floor geometry
forces \(j\ge1\); Round 39 combines this with one phase-stretch inequality to
prove \(\Gamma_{\rm OB}>0\).  This complete endpoint is therefore closed.
The one-sided upper-\(\alpha\) outer-\(B\) endpoint is the final Gate-A face
addressed below.

Round 40 restores the exact radial shelf drop on this remaining endpoint.
For
\[
 \mathcal D(z)=b_K(z)-b_\mu(z),\qquad y=r+\frac p2,
\]
strict convexity and an angular chord estimate give
\[
 \Delta>p\mathcal D(y)>
 p\frac{y(1-\cos t)}{\pi\sqrt{\mu^2-y^2\cos^2t}},
\]
and hence the exact selected scalar has the strict midpoint payment
\[
 p\Delta>
 p^2\frac{y(1-\cos t)}{\pi\sqrt{\mu^2-y^2\cos^2t}}.
\]
With
\[
 \rho=\frac{p/2+m+1}{\mu},\qquad
 C(\rho,t)=\frac{(1-\rho)(1-\cos t)}
 {\pi\sqrt{\sin^2t+2\rho}},
\]
the fixed count interpolation \(B_0>W/4+9/16\) yields
\[
 \Gamma_{\rm OB}>\mathcal R(\mu,p,m,t)
 =\frac9{10}+\frac9{16}\zeta+\frac14\zeta\mu L_0(t)
 +p^2C(\rho,t)-\frac{p-dm}{2}.
\]
This expression is strictly increasing in \(\mu\).  Every endpoint has
\(\mu\ge p+m+2\) and \(\mu>5/(4L_0)\), so the single remaining sign is
\[
 \mathcal R_*(p,m,t):=
 \mathcal R\!\left(\max\left\{p+m+2,\frac5{4L_0(t)}\right\},p,m,t\right)>0.
\]
Its geometric and phase representations are each strictly convex in one
auxiliary variable and agree at the seam.  Round 40 does not prove this final
continuum sign.  Round 41 supplies global exact rational enclosures and
reduces both branch signs to a fixed Bernstein table.  The clean replay ends
in `round41BernsteinSignReplayOK=True` after checking 4,405 load-bearing
coefficients (4,259 positive and 146 zero).  This is a new finite
computer-assisted certificate rather than the short hand-checkable wall
algebra authorized by the revised strategy.  The independent audit verdict
is NOT PASS as a strategy-authorized analytic closure and PASS only as an
exact structural reduction and computer-assisted candidate.  It therefore does not prove
\(\mathcal R_*>0\), close the endpoint, or alter any obligation status.  The
selected \(\Gamma_{\rm OB}\to\mathcal R_*\) projection is analytically
exhausted.  Round 42 performs the last stronger Gate-A specialization
directly through \(\Phi_\delta^+\).  At
\(\chi=h,\ y_B=0,\ \alpha\uparrow1^-\), define
\[
 H=(p+a_p)R_1,\qquad M=\min\{\zeta,H\},\qquad
 \mathcal T_{42}:=\frac9{10}+B_0M+Hh-\frac{p-dm}{2}.
\]
The exact endpoint identity and adjacent-action inequality give
\[
 \Phi_\delta^+>\mathcal T_{42}.
\]
This is structural only.  With
\[
 \mathcal A_{\rm adj}:=(p+a_p)
 [\Delta-R_1(j+e_p+h)]>0,\qquad
 \mathcal A_{\rm cap}:=\frac1{2\beta}-J-\frac9{10}>0,
\]
the complete loss ledger is exactly
\[
 \Phi_\delta^+-\mathcal T_{42}
 =\mathcal A_{\rm cap}+\Omega_-+\mathcal A_{\rm adj}
  +B_0(\zeta-M)+jH+(H+2p)e_p.
\]
The algebra-only replay ends in
`round42StrongerPhiReplayOK=True`.  The independent verdict is STRUCTURAL PASS
only; final sign open.  Round 43, recorded in
`human/outbox/general-d-round-43-hard-remainder-isolation-and-gate-a-stop.md`,
retains \(E<E_*=(p-dm)/(2p)\) and proves
\[
 H\ge\underline H:=
 \frac{(p+a_p)p(2r+p)}{m(2x+m)}
 \min\!\left\{\frac{U_x}{U_r},\sqrt{\frac{U_q}{U_r}}\right\},
 \qquad h>\frac{U_q^3}{3\pi\mu^2}.
\]
Its exact relaxed asymptotic family satisfies
\(\lim\mathcal T_{42}/N<0\), showing that count--phase and radial data alone
are insufficient.  It is outside the common-shelf owner.  A separate finite
high-precision negative diagnostic satisfies the outer wall, activity, common
shelf, and terminal first drop but fails the exact hard owner precisely at
\(E<E_*\); it is noninterval and noncertifying.  On every fixed-\(f\) chart,
Round 43 proves
\[
 \frac d{dt}(E_f-E_*)=
 \frac1\pi\left[\tan t\left(\sqrt{K^2-r^2}+\sqrt{K^2-x^2}\right)
 -\frac mp\right]>0.
\]
At a shelf jump \(E_{f+1}=E_f-2\), while the outer face lies on separate
integer \(B_0\)-walls.  A global continuation therefore requires the
forbidden \(f/B/j\)-indexed wall family.  The independent Round 43 verdict is
analytic structural PASS and **Gate A STOP**.  Gate B is active and restores
\[
 \mathscr S=D_A(q)+R_p+\frac{dm}{2}.
\]
Using the inherited exact shelf identity, the active Gate-B form and its
unrenamed target are
\[
 \mathscr S=D_A(q)+\mathcal C_p+p(E-E_*),
 \qquad D_A(q)+\mathcal C_p\ge p(E_*-E).
\]
The literal terminal defect \(D_A(q)\) and exact trapezoid
\(\mathcal C_p\) must be retained; do not restart from \(L_T\),
\(a_p\Delta\), or another compressed scalar.
The exact-owner sign \(\mathcal T_{42}\ge0\), the endpoint, CST, and the
theorem remain open.  The rejected floor-free adjacent projections remain
invalid replacements and do not falsify the endpoint or CST.

Round 44 reconstructs Gate B losslessly at the exact one-sided
upper-\(\alpha\), outer-\(B\) endpoint.  At the literal outer wall
\(B_{\rm lit}=B_0=Q\), while \(B=B_0+1\) is retained only as the gap-side
label.  After fixing the same literal or adverse old-inverse side vector in
every term,
\[
 D_A(q)=L_T^++\mathcal R_{\rm tan}^+
       =L_T^0+\mathcal R_{\rm tan}^0,
\]
\[
 L_T^+=\Omega_-+B_0\zeta+\frac1{2\beta}-J,\qquad
 L_T^0=\Omega_-+B_0\zeta+\frac9{16\beta}-J,
\]
and
\[
 \mathcal R_{\rm tan}^+-\mathcal R_{\rm tan}^0=\frac1{16\beta}.
\]
Exact first-shelf integration gives
\[
 R_p=\mathcal C_p+p(E-\tfrac12),\qquad
 \mathcal C_p\ge a_p\Delta,
\]
so the complete restored-loss identity is
\[
 \mathscr S-\Phi_\delta^+
 =\mathcal R_{\rm tan}^++(\mathcal C_p-a_p\Delta)
 =\frac1{16\beta}+\mathcal R_{\rm tan}^0
  +(\mathcal C_p-a_p\Delta).
\]
The intrinsic bounds
\[
 \mathcal R_{\rm tan}^0\ge
 \frac9{64\pi\sqrt{K^2-q^2}\,\beta^3},
\qquad
 \mathcal C_p\ge\frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-\frac1{\sqrt{K^2-r^2}}
 \right)
\]
imply that every hypothetical negative point must satisfy
\[
\begin{aligned}
 p(E_*-E)>{}&\Omega_-+B_0\zeta+\frac9{16\beta}-J\\
 &+\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}
 +\frac{p^3}{6\pi}
 \left(
 \frac1{\sqrt{\mu^2-r^2}}-\frac1{\sqrt{K^2-r^2}}
 \right).
\end{aligned}
\]
This is one necessary negative-support localization, not a positivity proof
or certificate.  The clean-room and final independent verdicts are
**STRUCTURAL PASS — FINAL SIGN OPEN**.  The finite searches found no negative
exact-owner record but do not cover the continuum.  Gate A remains stopped,
Gate B continues on the localized support, and Gate C is inactive.  The
endpoint, high-floor CST, pointwise assembly, and all-dimensional theorem
remain open; the proof graph and manuscript are unchanged.

Round 45 first proves the strict implication
\[
 \mathrm{R45\text{-}CF}\Longrightarrow
 \mathrm{S31\ empty}\Longrightarrow
 \mathrm{S30\ empty}\Longrightarrow\mathscr S\ge0,
\]
but directed exact owners falsify R45-CF while retaining positive exact
\(\mathscr S\).  This is a sufficient-route counterexample only.  Returning
to the exact literal support, Round 45 proves the count-uniform old-level
Bregman theorem
\[
 \mathcal R_k\ge\frac{7\pi^2}{48Kt^3\sin t},\qquad
 \sum_{k=1}^{B_0}\mathcal R_k\ge
 \frac{7\pi^2B_0}{48Kt^3\sin t}.
\]
Through the exact old/top decomposition and the primary \(u\)-retaining
Round 38 bound this gives
\[
 \Omega_-+\mathcal R_{\rm tan}^0\ge
 \frac{\pi^2B_0}{Kt^3\sin t}
 \left(\frac W2-\frac{B_0}{4}+\frac1{48}\right)
 +\frac9{64\pi\sqrt{K^2-q^2}\,\beta^3}.
\]
With the existing S30 margin,
\[
 \mathscr S=-M_{30}
 +(\mathcal R_{\rm tan}^0-T_{\rm top})
 +(\mathcal C_p-\mathcal C_{\rm curv}),
\]
so every S30 point with
\(M_{30}\le7\pi^2B_0/(48Kt^3\sin t)\) is signed.  Every hypothetical
negative point satisfies the strict reverse, which reduces exactly to the
strict reverse of Round 45 equation (R45.18).  The independent verdict is
**STRUCTURAL PASS — FINAL SIGN OPEN** under Step A6(4).  It does not prove
(R45.18), the endpoint, high-floor CST, pointwise assembly, or the
all-dimensional theorem.  Gate B continues under this substantive partial,
Gate C remains inactive, and all proof-obligation statuses remain unchanged.

The Round 30 finite diagnostic still retains 933 necessary-condition records,
none above \(q=33\), and finds minimum \(0.30090314669\ldots\) at
\((q,r,p,m)=(5,1,3,1)\).  The observed sharper cutoff and the unarchived
Round 31 finite-edge experiment remain non-premises; the Round 32 analytic
bootstrap and directed certificate are the proof dependencies.

`SHELL-general-d-pointwise-assembly` is the open
pointwise route; `SHELL-general-d-weighted-aggregate` is the alternative
sufficient route.  Only those assembly-level nodes imply the proposed
all-dimensional theorem.  No new ratio ladder is authorized, and a final
proof may use at most one consolidated compact certificate.  Round 32 now
selects that compact fallback for its finite shelf remainder, so the legacy
 first-floor certificate must be analytically replaced or consolidated before
 final assembly.  Round 41's second finite certificate is not authorized for
 that chain, and Rounds 42--45 introduce no authorized certificate.  Gate A
 is exhausted.  Gate B remains active and is now localized by the exact
 Round 45 strengthened support implication.  The next single pointwise task
 is the complete-owner proof of Round 45 equation (R45.18), equivalently
 exclusion of its strict reverse, with the exact wall/action/phase/cap and
 shelf-curvature correlation retained.  Do not repair the target with a
 count, floor, ratio, chamber, or second-certificate family.  Gate C is
 inactive; if Gate B genuinely fails under the revised stop rule, continue
 to the weighted aggregate, not a new lossy surrogate.

## Evidence and remaining work

The current mathematical audits include
`rounds/polya-main/round_025/reviews/revision1-independent-audit.md`,
`human/inbox/revision_2.md`, and `human/inbox/revision_2_2.md`.
Independent passes reconstructed the angular, radial/ball, and scalar
components and found no mathematical failure. Exact rational and
outward-rounded interval scripts are optional transcription regressions only.
The separate Round 38--45 general-dimensional notes each have an independent
audit and exact Mathematica replay at their stated structural scope.  Round
41 is not an authorized analytic closure; Round 42 has only a structural PASS;
Round 43 has an analytic structural PASS and Gate-A STOP; Rounds 44--45 have
**STRUCTURAL PASS — FINAL SIGN OPEN** verdicts and keep Gate B active on its
localized support.  The Round 44--45 numerical searches are diagnostics, not
coverage or certificates.  None of these changes the authoritative open status of
high-floor CST or the all-dimensional theorem.

Before external dissemination, the remaining work is:

- human line-by-line reconstruction of every bottleneck lemma;
- conventional independent referee review of the assembled manuscript; and
- a current literature and novelty comparison.

The separately reviewed non-tiling theorem concerns the same complete
\(0<r<R\) shell family. The ellipse/Mathieu and certificate-family tracks
remain separate open programs.

These dissemination gates concern the completed (d=3) theorem.  They do not
close, delay, or silently promote the separate all-dimensional research
obligations above.

## General-dimensional Round 48 portfolio result

The updated human workflow activates portfolio discovery on the literal
(d=4) weighted aggregate.  Round 48 derives the exact inverse-layer ledger

\[
 W_4=\int_0^{A(0)}\frac{\xi(t)^3}{3}\,dt,
 \qquad
 P_4^<=\sum_{n-1/4<A(0)}S_2(\lceil\xi(n-1/4)\rceil-1).
\]

Two bounded cell obligations are now `proved_internal`: every complete
full-outer cell has reserve (>19N/48+27/128), and every complete deep-inner
cell below (z=\mu/\sqrt2) has positive reserve.  Both passed distinct lead,
clean-room, and adversarial roles.

The unrestricted continuous quarter-node polynomial strengthening is
interval-falsified at an exact rational interface cell, while the literal
discrete QCL cell remains positive there.  The scoped literal aggregate
`SHELL-general-d-weighted-aggregate-d4` remains `proposed` and has no
theorem-level implication.  The first inverse-layer gap is the complete shallow-inner band,
the interface-straddling cell, terminal truncation, and their exact
compensation with the unused top interval.  The all-dimensional theorem
remains unproved, and the completed (d=3) theorem is unchanged.
