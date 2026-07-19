# Lemma Bank

The authoritative statements, dependencies, and evidence are in
`state/proof_obligations.yml`. This short bank lists the lemmas used by the
Revision 2 reviewed proof; earlier valid finite and regional lemmas remain available in
the graph and round archive but are not live premises.

## Live structural lemmas

- **Strict counting.**
  \(N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}\), with strict
  radial and angular wall ownership.
- **Separated shell spectrum.** The Dirichlet shell Laplacian is the orthogonal
  spherical-harmonic sum of complete Sturm--Liouville blocks with multiplicity
  \(2\ell+1\).
- **Cross-product and phase.** Positive radial eigenfrequencies are the simple
  positive zeros of the Bessel cross product, and the audited phase enclosure
  gives the strict proxy count.
- **Exact layer cake.** The multiplicity-weighted proxy is
  \(P=\sum_{n-1/4<T}M(R(n-1/4))^2\), while
  \(W=\int_0^T R(t)^2dt\).
- **No-mode theorem.** If \((1-\rho)K\leq\pi\), then the strict shell count is
  zero.

## Ratio-sharp global closure

For \(0<\rho<39/50\) and \(K>\pi/(1-\rho)\):

- the shell-action slope satisfies
  \(q\leq\arccos(\rho)/\pi\);
- disjoint left blocks give the angular payment
  \[
  E_{\rm ang}
  <\frac{1-\rho^2}{6}K^2
   -N\left(\frac{3\pi}{8\arccos\rho}-\frac14\right);
  \]
- the tangent envelope
  \[
  L_\sharp(t)=t^2/2\quad(t\leq1/4),\qquad
  L_\sharp(t)=t/4-1/32\quad(t\geq1/4)
  \]
  minorizes the exact shifted-sawtooth primitive;
- the retained Stieltjes remainder reduces to the universal ball
  quarter-layer, with \(\tau>1/4\) and the nonnegative squaring condition
  checked explicitly; and
- exact base and derivative convexity proves \(W-P>0\).

Thus \(N_D\leq P<W\) on the entire low/middle-ratio high-frequency region.

## Optical closure and assembly

The all-frequency optical theorem holds for
\(39/50\leq\rho<1\), including the lower seam. Combined with the no-mode and
ratio-sharp lemmas, it proves all \(0<\rho<1\) and \(K\geq0\). Scaling proves
the theorem for every \(0<r<R\).

## Detached results

The small-hole theorem, fixed-ratio high-energy theorem, finite staircases,
38-state exhaustion, exact owner subtraction, and certified compact closure
remain valid historical or alternate results. They have no edge into the
Revision 2 theorem chain. The double-sawtooth and shifted-tail nodes are
diagnostic or proposed only.

## Active general-dimensional lemma bank

This bank is separate from the completed Revision 2 proof.

- **Real-order proxy and exact branching backbone (derived, audit pending).**
  The real-order phase specialization still needs a dedicated frozen audit.
  Conditional on that specialization, for
  (r_m=m+(d-2)/2) and
  (c_{d,m}=\binom{m+d-3}{d-3}), the phase proxy branches exactly and

  \[
  W_d-P_d^{<}=\mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m),
  \qquad \mathcal B_d(A)\ge0.
  \]

- **First-shelf reduction (proved module).** An inner shifted tail is reduced
  to (D_A(q)+R_p+d_\rho(n-p)/2), with the exact shelf identity and the
  scale-free curvature bound retained.

- **Exact no-drop identity (proved module).** For (p=n), use

  \[
  D_A(r)=D_A(q)-\frac n2+2n\varepsilon_q
  +2\int_0^n u\sigma(r+u)\,du+\chi_q.
  \]

  The endpoint term (\chi_q) must not be removed by a stronger universal
  CST statement.

- **Fractional terminal reserve (Round 10, proved and audited).** If (y_k) is the
  strict inverse displacement, then

  \[
  D_g\ge\sum_{k=1}^B
  \left(\frac1{2c_k}-1+2\eta_k\right)
  +\frac{(v-B)_+^2}{c_v},
  \qquad \eta_k=y_k-[y_k]_<.
  \]

  For the shell, (y_k=K\cos\theta_k-q), and the inner cap satisfies
  (0\le2\delta\le\alpha h), strictly for (\alpha>0).

- **First-floor zero-level corner (Round 11).** If (f=1,p=n,B=0), then
  (q=\mu), (G_K(q)=3/4), and the active wall plus a slope-integral lower
  bound reduce the defect to a positive quartic Bernstein polynomial.
  Hence (D_A(r)>0) analytically.

- **First-floor one-level pre-shelf reduction.** For
  (0\le\varepsilon<1/4), convexity gives

  \[
  \Delta\ge\frac{2n}{r+2n}
  \left(\lambda-\frac34-\varepsilon\right),
  \]

  and the resulting shelf lower bound is increasing in (\varepsilon).  This
  implication produces the explicit (B=1) scalar (4.5) of the Round 11 note.
  Round 13 shows that the scalar's universal sign is false even on the new
  integer extension grid; therefore it is no longer a live sufficient target.

- **One-level interface endpoint reduction (Round 12).** Holding the outer
  inverse level fixed and writing (\mu=q+\alpha), the open-side scalar (4.5)
  is strictly decreasing in (\alpha).  Its phase endpoint is determined by
  \(G_{q+\alpha_*}(q)=v-3/4\), and its sharp endpoint also retains the
  owner-dimensional activity wall.  For this surrogate, the reduction would
  make it sufficient to prove

  \[
  \Psi_{\rm end}(\theta,y,n)\ge0.
  \]

  The literal lower action wall has the favorable jumps (Q:1\to0) and
  (\chi_q:0\to1).  Round 13 proves that this endpoint sign is false, so the
  monotonicity lemma is retained but the proposed sign target is rejected.

- **Exact-head endpoint reduction (Round 14, proved and audited).** In the
  hard open (B=1) first-floor no-drop branch on the new extension grids, let

  \[
  L_{\rm ex}=\frac\pi{2\theta}+2\eta-1-2\delta
  +\frac{(v-1)_+^2}{\beta},
  \qquad
  H_n=2\int_r^q(A_\alpha(s)-1)\,ds,
  \]

  and \(\Xi=L_{\rm ex}+H_n\).  Then \(L_{\rm ex}>1/12\), the exact S4
  identity gives \(D_A(r)\ge\Xi(\alpha)\), and \(\Xi\) is strictly decreasing
  in the interface displacement.  Hence

  \[
  D_A(r)\ge\Xi(\alpha)>\Xi(\bar\alpha),
  \]

  where \(\bar\alpha\) is the first phase, branch, or owner-dimensional
  activity endpoint.  This formulation retains the exact head, exact cap,
  inverse fraction, top square, and literal-wall jumps.  Its sign target has
  been superseded by the sharper exact-terminal reduction below.

- **Exact-terminal endpoint reduction (Round 15, proved and audited).**  Let
  \(z\) solve \(G_K(z)=3/4\), put \(y=z-q\) and \(M=[y]_<\).  On the hard open
  one-level chamber the literal count is
  \(T_A(r)=1+2n+2M\), so

  \[
  D_{A_\alpha}(r)
  =\Omega(\alpha)
  :=2J_K(r)-2J_{q+\alpha}(r)-(1+2n+2M).
  \]

  Since \(J_a(r)\) is strictly increasing in \(a\),
  \(\Omega'(\alpha)<0\), and
  \(D_A(r)=\Omega(\alpha)>\Omega(\bar\alpha)\).  This identity restores the
  exact outer terminal and makes no analytic loss at the original point.

- **Continuous geometric reduction (Round 16, proved and audited).**  At
  \(a=q+\bar\alpha\), write \(\eta=y-[y]_<\) and let \(x\) be the unique
  solution of \(G_K(x)-G_a(x)=1\).  The endpoint domain implies
  \(a\ge2\), \(K-a>\pi\), \(A(a-1)\ge3/4\), and \(z>2\).  Convex minimization
  gives

  \[
  \Omega_{\rm end}
  \ge2F(K,a)-1+2\eta,\qquad
  F=J_K(x)-J_a(x)-(z-x).
  \]

  It is therefore enough to prove \(F\ge1/2\).  The radial derivative
  \(F_K>0\) follows from a strict convex-quantile/Jensen argument.  The
  suspected \(q=3,r=1,n=2\) double face has the exact rational reserve

  \[
  \Omega_{\rm wall}>
  \frac{15150166179733}{73320166719360}>\frac15.
  \]

- **Action-face quantile reduction (Round 17, proved and audited).**  On
  \(A(a-1)=3/4\), the exact derivative is

  \[
  \frac{dF}{da}=K'B_K+\int_0^gQ(c)\,dc,
  \]

  where \(B_K>0\), \(Q(c)=K'U_K(c+1)-U_a(c)\), and \(g=G_a(x)\).
  The quantile comparison satisfies \(Q'>0\), \(Q''<0\), and \(Q(g)>0\).
  Concavity makes the endpoint-chord scalar \(\mathcal S\) sufficient, but
  Round 19 bypasses that non-sharp target and works from the exact derivative.

- **Simultaneous-wall closure (Round 18, proved and audited).**  At the unique
  point \(K=a+\pi\), \(A(a-1)=3/4\), exact rational Taylor and Machin bounds
  give

  \[
  \frac{11}{2}<a<\frac{45}{8},\qquad z<\frac{101}{20},
  \qquad F-\frac12>\frac{1443}{449440}>0.
  \]

- **Action-face Jensen closure (Round 19, proved and audited).**  With
  \(s=K/a\), \(k=K'(a)\), \(p=g+1\), and \(q=sg\), the exact derivative is
  the integral of one decreasing convex radius-\(K\) quantile against a
  positive two-piece measure.  Jensen and the tangent at level \(3/4\)
  reduce the sign to

  \[
  E(\theta)<k-1,
  \qquad
  2(s-k)g^2+k(1-g)>0.
  \]

  Both inequalities are proved globally, with one finite exact checkpoint
  \(g(8)<1\).  Hence \(dF/da>0\) on the strict action face.  Combined with
  Rounds 16 and 18, this proves \(F(K,a)>1/2\) throughout the enlarged
  endpoint domain and closes the hard open \(B=1\) endpoint.

- **First-floor no-drop WP2 (proved and independently integrated).**  The
  final audit reconstructs the complete \(B=0,1,\ge2\) phase union, the
  integer grid \(r\ge1\), the half-integer grid \(r\ge3/2\), the lower action
  owner, owner activity, inverse zero extension, and every strict wall.  It
  also proves exactly that the auxiliary \(z=2\) face is redundant.  No
  unproved chord scalar or sampled minimum enters the dependency chain.

- **High-floor wall-aware probe (Round 20, diagnostic and independently
  replayed).**  The exact scalar, \(\Phi_\delta\), two variants, and their
  terminal/shelf loss ledger replay on 19,619 active records with all negative
  counts zero.  The corrected hard wall is \(G_K(7)=3/4\), \(q=5\),
  \(y_1=2\); the bad-side strict fraction tends to zero and both terminal
  quantities jump down by exactly two.  These are floating-point diagnostics,
  not positivity evidence.

- **High-floor intrinsic CST reduction (Round 21, proved and audited).**  Put
  \(W=G_K(\mu)\), \(\lambda=f-1/4-W\), and
  \(B_0=[f-\lambda]_<\).  On the extension grids the local cap obeys
  \(J<1/7\); complete interface levels and the top interval give a terminal
  payment that does not use any \(\eta_k\).  Elasticity and curvature give
  \(\Delta\ge L_0\).  Consequently
  \(\Phi_\delta>\mathcal R\), with \(\mathcal R\) explicit in equation
  (4.4) and constrained by exact feasibility (4.3).  Round 22 proves that the
  optional sign \(\mathcal R\ge0\) is false, but the reduction itself remains
  valid.

- **Exact-cap repair (Round 22, proved, certified at the counterexample, and
  independently audited).**  The exact active tuple
  \((K,\mu,\rho;r,n,p,m,q,f,B_0)=
  (261/20,699/100,233/435;1,5,3,2,6,2,1)\) satisfies
  \(\mathcal R<-1/300\) by directed Arb arithmetic.  Retaining
  \(J=2I_\mu(q)\) repairs the analytic reduction globally to
  \[
    \Phi_\delta>\mathcal R_J,
    \qquad \mathcal R_J=\mathcal R+\frac17-J.
  \]
  At the same tuple, \(\mathcal R_J>1/20\).  This rejects only the coarse
  sufficient sign; \(\mathcal R_J\) remains the repaired scalar passed to
  Round 23.

- **Curvature-only convex-cell reduction (Round 23, proved and independently
  audited).**  On the exact high-floor first-drop domain,
  \(p,m\ge1\) implies \(q\ge3\), and a printed rational chain proves
  \(J<2I_4(3)<1/8\).  Keeping \(J\) to that final comparison gives
  \[
    \mathcal R_J>\mathcal C_8.
  \]
  For fixed \((r,p,m,f,\alpha)\), \(\mathcal C_8\) is strictly convex on
  each literal action/top-payment cell.  Its sign therefore reduces to the
  exact shelf/activity/action/top-payment boundaries or the unique stationary
  point.  The one-sided \(\lambda\downarrow0\) face has
  \(\mathcal E\to1\).  The observed limiting value near
  \(0.01286445\) is diagnostic only.  The reduction remains proved, but
  Round 26 later rejects the universal sign \(\mathcal C_8\ge0\).

- **Coordinatewise two-axis reduction (Round 24, proved and independently
  audited).**  Fix \(x=r+p\).  Feasible positive integer \(p\)-labels form a
  prefix, and their contribution
  \(S(p)=kp^2(3x-p)-p/2\) satisfies \(S''(p)=6k(x-p)>0\), leaving at most two
  adjacent owners at each \(t\).  On the delicate quadratic top-payment cell,
  \(B=f-1\) and \(0<u<1/\sqrt2\), the identity
  \(\mu=\pi(B+u)/(\tan t-t)\) eliminates \(\alpha\) exactly.  Along the lower
  shelf wall, \(t_\mu<0\), \(W_\mu<0\), and \(\lambda_\mu>0\).  The
  candidate conditions are coupled, and other payment cells are not reduced
  by this step; no global \(\alpha\)-monotonicity or lower-wall dominance is
  claimed.

- **Stationary projected-shelf reduction (Round 25, proved and independently
  audited).**  On the delicate cell \(B=f-1\),
  \(0<u<1/\sqrt2\), an interior fixed-\(\mu\) stationary point satisfies
  \(R>0\) and the exact identity
  \[
    \mathcal C_8=
    m\left(\frac12-\frac t\pi+\frac z\pi\right)
    +B\left(\frac\pi{2t}-1+\frac{\pi z}{2t^2}\right)
    -\frac p2-\frac18+2u^2-zL,
  \]
  where \(H=\tan t-t\), \(z=\tan(t/2)\),
  \(L=4u(B+u)\tan^2t/H\), and
  \(R=m/\pi+B\pi/(2t^2)-L\).  Put
  \(P=3\pi^2(B+u)R/(H\sin t)\), and let \(\psi(P)\) be the positive root of
  \(\psi^2(2\psi+3)=P\).  The two full shelf integrals imply a strict
  \(m\)-window, and stationarity plus interface/owner bounds give
  \(p\le\min\{\mu-m-1,\psi(P)\}\), hence
  \(\mathcal C_8\ge\mathcal F(B,m,t,u)\).  The endpoint window is not a
  sufficient description of the projected shelf image: directed Arb
  arithmetic proves \(\mathcal F<-34.18\) at a relaxed rational point outside
  that image.  Thus the promoted lemma is the reduction, not the sign of
  \(\mathcal F\), \(\mathcal C_8\), or CST.

- **Lossless projection and sufficient-sign falsification (Round 26, proved,
  certified, and independently audited).**  The paired shelf inequalities
  have a lossless cumulative-integral form.  On a fixed parity grid,
  \((B,m,t,u)\) fixes \(\mu,q,\alpha,x\), and stationarity pins at most one
  positive integer owner through \(p^2(3x-p)=P\).  At the certified half-grid
  tuple
  \[
    (B,f,m,r,p,\alpha,\mu)
    =\left(1,2,6,\frac{25}{2},6,\frac9{10},\frac{127}{5}\right),
  \]
  \(p=6\) is also the unique discrete minimizing owner, yet
  \[
    \mathcal F<-\frac1{50}<0<\frac{77}{50}<\mathcal C_8.
  \]
  Thus replacing the actual \(p\) by \(p_{\max}\) destroys the sign even on
  the full coupled-owner image.  A separate exact half-grid witness
  \(r=57755/2\), \(p=80\), \(m=15\), \(f=2\), \(\alpha=1/2\), and its nearby
  unique stationary point satisfy \(\mathcal C_8<-7\).  At the same witness,
  however,
  \[
    \mathcal R_J
    =\mathcal C_8+(p+a_p)(L_0-L_{\rm curv})+\left(\frac18-J\right)>20.
  \]
  Therefore both \(\mathcal F\ge0\) and \(\mathcal C_8\ge0\) are rejected
  sufficient targets.  The identities remain valid.  Round 27 later rejects
  global \(\mathcal R_J\ge0\), so this chronology must not be read as a live
  global-sign premise.  The actual owner, exact \(J\), and literal
  \(L_0=\max\{L_{\rm elast},L_{\rm curv}\}\) remain essential accounting
  variables; \(\mathscr S\) denotes the exact reduced scalar and is not
  synonymous with \(\mathcal R_J\).

- **Remainder-rich automatic closure and exact hard-sector reduction (Round
  27, proved and independently audited).**  Put \(d=1-2t/\pi\) and
  \[
   E=e_0+e_p,\qquad \Delta=e_0-e_p,
   \qquad E_*=\frac12-\frac{dm}{2p}.
  \]
  The exact lower scalar satisfies
  \[
   D_A(r)\ge\Phi_\delta^+
   =\max\{0,L_T\}+a_p\Delta+p(E-E_*).
  \]
  Hence \(p\le dm\) or \(E\ge E_*\) implies \(D_A(r)\ge0\).  The only
  residual sector is
  \[
   p>dm,\qquad 0\le E<E_*<\frac12,
  \]
  and its exact remaining inequality is
  \[
   \max\{0,L_T\}+a_p\Delta\ge p(E_*-E).
  \]
  The Round 21 elasticity inequality sharpens there to
  \[
   \Delta\ge\frac{s-1}{s+1}(E+2\lambda).
  \]
  Separately, a directed-Arb exact tuple certifies
  \(\mathcal C_{\max,8}<-4/3\) and \(\mathcal R_J<-6/5\), but also
  \(\mathscr S>47\), \(\Phi_\delta>40\), and \(E>1>E_*\).  Thus it rejects
  only the global compressed signs and lies in the proved automatic branch.
  Conditional \(\mathcal C_{\max,8}\ge0\) is a stronger sufficient target on
  the residual sector, not an equivalent restatement and not a global claim.

- **Exact-E quartic projection and hard-phase reduction (Round 28, proved and
  independently audited).**  On the Round 27 residual sector define
  \[
   \mathcal K_4=
   \frac{(\mu^{-1}-K^{-1})((r+p)^2-r^2)}{2\pi}
   +\frac{(\mu^{-3}-K^{-3})((r+p)^4-r^4)}{24\pi},
  \]
  \[
   \tau=\frac{s-1}{s+1},\qquad
   M_4=\max\{\tau(E+2\lambda),\mathcal K_4\}.
  \]
  Then
  \[
   \Delta>\mathcal K_4,\qquad
   \Delta\ge\tau(E+2\lambda),
  \]
  and
  \[
   D_A(r)\ge\Phi_\delta^+
   \ge\Psi^{L_T}_{4,E}
   :=\max\{0,L_T\}+a_pM_4+p(E-E_*)
   \ge\Psi^{\rm rf}_{4,E}.
  \]
  The complete-terminal scalar is primary; its full sign remained open at
  the end of Round 28 and is narrowed, but not closed, by Round 29 below.
  Independently, \(H(t)=E(t)-E_*(t)\) is strictly increasing on \(p>d(t)m\),
  so the hard set is one initial phase interval.  The conditional Cmax
  maximum has one switch, strictly convex curvature cells, decreasing
  elasticity constant-payment cells, and at most one elasticity stationary
  minimum on the quadratic cell.  This yields a finite auxiliary candidate
  list but no sign theorem.  Fresh diagnostics and Mathematica replays are
  regression evidence only.

- **Complete-terminal phase/wall reduction and primary inverse cell (Round
  29, proved and independently audited).**  On every fixed-\(\alpha\)
  literal terminal count cell in the exact residual sector,
  \(\Psi^{L_T}_{4,E}\) is strictly increasing in \(t\).  The literal raw
  terminal jumps are
  \[
   -2\quad\hbox{(inverse wall)},\qquad
   -1\quad\hbox{(\(Q\)-wall)},\qquad
   -\frac1{16\beta}\quad\hbox{(outer \(B\)-wall)}.
  \]
  On the inherited grids \(r\ge1\) (integer) and \(r\ge3/2\)
  (half-integer), every fixed-\(Q\), constant-\(K\) inverse/outer-\(B\) wall
  segment has \(d\Psi^{L_T}_{4,E}/d\mu<0\).  Thus neither type of interior
  stationary point remains.  On the entire component
  \[
   (r,p,m,f)=(1,2,2,2),\qquad B=Q=1,\qquad 2<y_1<3,
  \]
  exact angle, cap, top-interval, and curvature estimates give
  \[
   \Psi^{L_T}_{4,E}>
   \frac{371}{15840}+2\eta_1+2E>0.
  \]
  At the end of Round 29 the remaining candidates were the nonconstant-\(K\)
  shelf, \(Q\), activity, hard-sector, and \(\alpha\) endpoints and the other
  simultaneous wall intersections; Rounds 30--35 subsequently close the
  included shelf, activity exit, and lower-\(Q\) hard endpoint family.  The
  adaptive cusp is diagnostic only and rules out a
  global \(\alpha\)-monotonicity shortcut.

- **First-inverse nonconstant-\(K\) endpoint reduction (Round 30, proved and
  independently audited).**  On the whole \(B=Q=1,\ 2<y_1<3\) band,
  activity is automatic.  On the included lower shelf,
  \[
   \frac{dL_T}{d\mu}>0,\qquad L_T>\frac7{10}.
  \]
  With \(\theta_j,K_j\) defined by
  \[
   \tan\theta_j-\theta_j=\frac{3\pi}{4(q+j)},\qquad
   K_j=\frac{q+j}{\cos\theta_j},\qquad j=2,3,
  \]
  the projected scalar satisfies
  \[
   \Psi^{L_T}_{4,E}>
   \mathfrak F(q,r,p,m)
   =
   T(q)+a_p\mathcal K_{4,\min}
   +p\left(E_{\min}-\frac12\right)
   +\frac{m d_{\min}}2.
  \]
  Shelf feasibility and hardness imply
  \[
   G_{K_3}(q-m)-G_q(q-m)\ge\frac74,\qquad
   p>d_{\min}m,\qquad
   E_{\min}<\frac12-\frac{d_{\min}m}{2p}.
  \]
  The open lower \(Q\)-wall has \(0<y_1<\alpha<1\), no inverse or
  outer-\(B\) wall, and \(L_Q>3/28+2y_1\) with \(dL_Q/d\mu>0\).
  Hence it cannot terminate a \(y_1>1\) band away from an
  \(\alpha=0\) corner.  On \(\alpha=0,\ f=2\),
  \[
   \Psi^{L_T}_{4,E}>1+2\eta_1-H(t)>0
   \quad\hbox{for}\quad \frac45\le t<\frac{13}{10}.
  \]
  The sign \(\mathfrak F>0\), the lower-\(Q\) hard arc, and endpoint
  families outside this exact scope remain open.  The observed diagnostic
  cutoff \(q\le33\) is not a lemma.

- **Retained-\(E\) convexity and shell-ratio-free large-\(q\) exclusion
  (Round 31, proved and independently audited).**  For fixed \((q,m)\), the
  dependent profile \(p\mapsto\mathfrak F(q,q-m-p,p,m)\) is strictly convex.
  At a fixed
  integration radius \(a\), put \(u=r/a\), \(v=p/a\).  The normalized
  second-derivative kernel is
  \[
   D(u,v)=\frac{2u}{\sqrt{1-u^2}}+
   v\left(1+\frac{u^2}{2}+\frac{v^2}{3}
   -(1-u^2)^{-3/2}\right)>0
  \]
  for \(u,v\ge0\), \(v>0\), and \(u+v<1\).  For every real
  \(q\ge1000\), exact rational phase bounds force \(m>11q^{1/3}/10\), and
  the intrinsic retained-\(E\) bootstrap
  \[
   1\to\frac{25}{17}\to\frac53\to2\to\frac{25}{11}
   \to\frac52\to3\to4\to10
  \]
  for \(p/(d_{\min}m)\) contradicts the hard upper bound.  Hence the exact
  necessary retained-shelf domain is empty for \(q\ge1000\), without a
  shell-ratio partition.  Finally, a weaker finite lower scalar \(L_q\) has no
  interior minimum and reduces on each parity-grid triangle to the three
  strictly convex edges \(p=1\), \(r=r_0\), and \(m=1\).  No edge sign and
  no exclusion for \(q<1000\) is part of this lemma.

- **Intrinsic shelf-bootstrap truncation and compact retained-shelf closure
  (Round 32, proved, certified, and independently audited).**  Put
  \(\psi=\arccos(q/K_3)\).  For every necessary included lower-shelf point
  with real \(q\ge35\),
  \[
   m>\frac65\left(\frac{\pi}{\psi}-3\right).
  \]
  The proof first gets \(m>y=\pi/\psi-3\), then uses the increasing convex
  phase difference
  \(h(z)=\arccos(z/K_3)-\arccos(z/q)\), the exact estimate
  \(h(q-y)<2\psi/3\), and a trapezoidal phase bound to self-improve the shelf
  condition.  Hence integer
  \(m\ge m_0=\lfloor(6/5)y\rfloor+1\) for \(q\ge35\); put \(m_0=1\) below
  \(35\).  On the resulting triangles, \(L_q>1/5\) at \(p=1\).  A single
  directed-Arb certificate proves \(L_q>1/100\) on \(r=r_0\) and \(m=m_0\)
  for all 1994 exact grid values \(3\le q<1000\).  Round 31 owns every real
  \(q\ge1000\).  Therefore \(\mathfrak F>0\) on the whole included
  retained-\(E\) shelf on both grids.  This lemma includes no other
  nonconstant-\(K\) endpoint family.

- **Open lower-\(Q\) hard-arc monotonicity (Round 33, proved and independently
  audited).**  On \(A(q)=3/4\), \(0<\alpha<1\), retain the exact first-drop
  action \(A(x)-A(q)=f-1+e_p\ge1\).  Put \(H=E-E_*\).  Along the wall,
  \(K'=\kappa=\sin\phi/\sin\psi\), and with
  \(D(z)=S_\mu(z)-\kappa S_K(z)\), \(c=\cos t\), and
  \(a=1-\kappa c\),
  \[
   \pi H'=-D(r)-D(x)+\frac mp\frac{a}{\mu\tan t}.
  \]
  Exact factorization at \(x\), the retained action, and \(W<3/4\) imply
  \(D(x)>a/(d\mu\tan t)\).  Since hard orientation gives \(m/p<1/d\),
  \(H'<0\).  Thus a hypothetical hard component reaches the included lower
  shelf, an activity wall, or \(\alpha\to1^-\).  The lemma proves neither
  full-\(\Psi\) monotonicity nor the sign at those exits.

- **High-floor activity excision and lower-\(Q\) correlated quadrature
  reduction (Round 34, proved and independently audited).**  On every
  high-floor first shelf,
  \(A(x)\ge7/4<(K-\mu)/\pi\), so \(K-\mu>7\pi/4\) and
  \[
   K^2-\frac{\pi^2}{(1-\mu/K)^2}-\gamma>\frac1{16},
   \qquad \gamma\in\{3/4,2\}.
  \]
  Thus activity equality is absent globally in this branch.  On the
  lower-\(Q\) wall, Fubini also gives the exact adjacent-action lemma
  \[
   \Delta>(f-1)\frac{U_r-U_x}{U_x-U_q}.
  \]
  Combining a strict action trapezoid with a strict Jensen shelf lower bound,
  before eliminating \(\mu\), reduces hard-sector exclusion to (3.15) on
  (3.16) of the Round 34 note and then to the \(Q\to1^-\) face plus a finite
  radius/stationary alternative.

- **Lower-\(Q\) hard-sector closure (small phase and Round 35, proved and
  independently audited).**  The exact adjacent-action ratio closes
  \(0<t\le\pi/8\).  For \(\pi/8\le t\le\pi/6\), a retained binomial
  quadrature and one rational polynomial prove the full face residual
  positive.  For \(\pi/6\le t<3\pi/14\), the radius boundary reduces to one
  exact bivariate polynomial, while feasibility forces
  \(X<9d/(2+9d)\); at a stationary root this makes the discriminant of the
  adverse quadratic strictly negative.  The transported domain is empty for
  \(t\ge3\pi/14\).  Hence every lower-\(Q\), high-floor, first-drop hard tuple
  has \(\Delta>E_*\).  This closes only the lower-\(Q\) endpoint family, not
  high-floor CST.

- **Exact count-gap and collision reduction (Round 36, proved and
  independently audited).**  On the residual hard sector,
  \(h=G_\mu(q)<1/4\), so \(B-Q\in\{0,1\}\) and \(B\le f\).  For
  \(\alpha>0\), the outer-\(B_N\) wall precedes \(Q_N\).  On the
  one-level-gap branch,
  \[
   L_T>1-J>\frac67,
   \qquad
   \Psi^{L_T}_{4,E}>\frac67-\frac{p-dm}{2},
  \]
  which closes \(p-dm\le12/7\), including \(p=1\) and old inverse bad
  sides.  On a higher \(Q_N\) wall, \(0<y_N<\alpha<1\) and
  \(L_T>3G_\mu(q)>0\); the full scalar remains open there.  Fixed-\(K\)
  transport leaves only the residual gap endpoints, higher equal-count
  faces, \(\alpha=0\) combined corners, and general lower shelves.

- **Gap-interface synchronization and exact-shelf reduction (Round 37,
  proved and independently audited).**  On the hard one-level-gap branch,
  strict-floor synchronization gives
  \[
   B_0=Q=B-1\ge1,
   \qquad j=f-B=\lfloor\lambda\rfloor,
   \qquad j\le\lambda<j+1.
  \]
  The possible \(B_0=0\) sublevel is excluded by the already proved
  Round 34--35 normalized-domain theorem, and the terminal top interval is
  identically zero.  With \(\Omega>0\) and \(\Xi=E-M_4\ge0\),
  \[
   \Gamma_{\rm gap}
   =1-J+\frac{B_0d}{2c}+\Omega
    +(p+a_p)M_4+p\Xi-\frac{p-dm}{2}
  \]
  is lossless relative to the selected Round 28 scalar.  A separate
  correlated shelf argument proves the strict count-free sufficient bound
  \(\Phi_\delta^+>\mathcal H_\Delta\).  Neither residual sign is proved.

No all-dimensional theorem follows until the high-floor first-drop
residual is closed pointwise or by the weighted aggregate and the final
assembly is audited.
