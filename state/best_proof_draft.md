# Best Proof Draft

The submission-facing proof is
`manuscript/spherical-shell-polya-proof.tex`; the complete low/middle-ratio
calculation is
`manuscript/analytic/ratio-sharp-global-closure-body.tex`.
This file records the live logical spine.

## Statement

For every \(0<r<R\) and \(\Lambda\geq0\),

\[
N_D(A_{r,R},\Lambda)
\leq \frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}.
\]

It is enough by dilation to prove this on \(A_{\rho,1}\) with
\(K=\sqrt\Lambda\).

## 1. Exact spectral reduction

Spherical harmonics reduce the Dirichlet Laplacian to the one-dimensional
operators

\[
-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad \ell=0,1,\ldots,
\]

with multiplicity \(2\ell+1\). The cross-product phase and strict phase
enclosure imply

\[
N_D(A_{\rho,1},K^2)\leq P(\rho,K),
\]

where, with \(T=(1-\rho)K/\pi\), \(R=A_{\rho,K}^{-1}\), and
\(M(r)=\#\{\ell\geq0:\ell+\tfrac12<r\}\),

\[
P=\sum_{n-1/4<T}M(R(n-1/4))^2.
\]

The Weyl target is

\[
W=\int_0^T R(t)^2\,dt
=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

## 2. Exact defect and ratio-sharp angular payment

The strict layer cake decomposes \(W-P\) into retained radial reserve minus
angular rounding defect. Put \(\theta=\arccos\rho\). The exact shell-action
slope satisfies

\[
0\leq q(z)=-A'(z)\leq\frac{\theta}{\pi}.
\]

On the disjoint left block attached to each active shifted radial level,
this yields

\[
E_{\rm ang}
<\frac{1-\rho^2}{6}K^2
-N\left(\frac{3\pi}{8\theta}-\frac14\right),
\]

with the strict half-integer convention valid even at common walls.

## 3. Retained radial reserve

The shifted-sawtooth primitive is bounded below by the \(C^1\) tangent
envelope

\[
L_\sharp(t)=
\begin{cases}
t^2/2,&0\leq t\leq1/4,\\
t/4-1/32,&t\geq1/4.
\end{cases}
\]

The Stieltjes remainder, including its endpoint signs, then reduces the shell
reserve to a universal ball quarter-layer. The outer-branch change of
variables is used only after \(\tau>1/4\) is established, and the ball-inverse
lower bound is shown nonnegative before squaring.

## 4. Scalar closure

The preceding estimates give an explicit lower bound
\(W-P>\underline{\mathcal G}(\rho,K)\). At
\(K_0=\pi/(1-\rho)\), the substitution
\(x=(1-\rho)^{-1/6}\) reduces the base value and derivative to two elementary
functions \(F_0,D_0\). Exact rational estimates prove

\[
F_0(1)>\frac{8269}{30000},\qquad
F_0'''(x)>\frac{676141}{2450},
\]

\[
D_0(1)>\frac1{300},\qquad
D_0'(1)>\frac{54}{175},\qquad
D_0''(x)>\frac{1951}{100},
\]

and

\[
\partial_K^2\underline{\mathcal G}
>\frac{47447}{443682}>0.
\]

Consequently \(P<W\) for
\(K>\pi/(1-\rho)\) and \(0<\rho<39/50\).

## 5. Final assembly

- If \(K\leq\pi/(1-\rho)\), the phase increment is at most \(\pi\), so
  strict counting gives no eigenvalue below \(K^2\).
- If \(K>\pi/(1-\rho)\) and \(0<\rho<39/50\), use the ratio-sharp theorem.
- If \(K>\pi/(1-\rho)\) and \(39/50\leq\rho<1\), use the existing optical
  theorem.

This cover is disjoint and exhaustive. Dilation gives arbitrary \(r,R\).

No finite staircase, event-state theorem, numerical root isolation, interval
certificate, or executable ledger is a premise of this proof.

## Separate general-dimensional extension (incomplete)

The incumbent research manuscript is
`manuscript/spherical-shell-polya-general-d.tex`.  It is not part of the
proved statement above and must not inherit the (d=3) theorem status.

Its preserved proof spine is

\[
\text{real-order phase proxy}
\longrightarrow
\text{exact harmonic branching}
\longrightarrow
W_d-P_d^{<}=\mathcal B_d(A)+\sum_m c_{d,m}D_A(r_m).
\]

The current replacement endgame is developed in the Round 10 terminal note
and the Round 11--19 first-floor notes.  Round 10 proves and independently
audits the fractional terminal reserve.  Round 11 proves and independently
audits the (B=0) first-floor corner and derives a lossy (B=1) pre-shelf scalar.
Round 12 validly reduces that scalar to an endpoint, but Round 13 gives an
exact rational extension-grid counterexample to both proposed surrogate sign
claims; the exact defect stays positive.  Round 14 restores the exact no-drop
head and exact inner cap.  Round 15 restores the exact terminal count and
proves the audited exact endpoint identity and monotonic move.  Round 16
reduces that endpoint to \(F(K,a)\ge1/2\), proves \(F_K>0\), and closes the
suspected \(q=3\) double face with a rational reserve.  Round 17 exposes the
exact action-face quantile structure.  Round 18 proves a symbolic rational
reserve at the simultaneous wall.  Round 19 bypasses the chord scalar and
proves \(dF/da>0\) on the full action face by a one-radius Jensen inequality.
Thus \(F(K,a)>1/2\) and the hard \(B=1\) endpoint are closed.  The independent
WP2 integration audit then verifies the exhaustive \(B\)-phase union, both
extension grids, owner activity, every strict wall, and the exact redundancy
of \(z=2\).  The first-floor no-drop theorem is therefore proved internally.
The high-floor first-drop CST theorem remains open.
Round 20 gives a wall-aware, independently replayed diagnostic of
\(\mathscr S\) and \(\Phi_\delta\) on 19,619 active records, with no sampled
negative and a smallest sampled surrogate value about \(0.837805\); this is
not a proof.  Round 21 proves the uniform cap bound \(J<1/7\), an
interface-complete-level/top-interval terminal transport, and simultaneous
elasticity/curvature shelf transport.  It first reduces the analytic target to

\[
 \Phi_\delta>\mathcal R,
 \quad\text{under exact feasibility (4.3)}.
\]

The displayed inequality is proved and independently audited.  Round 22 then
certifies an exact active tuple with \(\mathcal R<-1/300\), so the coarse sign
\(\mathcal R\ge0\) is rejected.  Keeping the exact cap
\(J=2I_\mu(q)\) repairs the reduction to

\[
 \Phi_\delta>\mathcal R_J,
 \qquad
 \mathcal R_J=\mathcal R+\frac17-J.
\]

The same certified tuple has \(\mathcal R_J>1/20\).  Round 23 then retains
the exact cap through its final comparison and proves

\[
 J<\frac18,
 \qquad \mathcal R_J>\mathcal C_8.
\]

For fixed intrinsic discrete data and \(\alpha\), the sufficient scalar
\(\mathcal C_8\) is strictly convex on every literal action/top-payment cell.
Its sign reduces to exact intrinsic walls or one stationary point.  This
reduction remains valid, but Round 26 later proves that the universal sign
\(\mathcal C_8\ge0\) is false.  The exact-cap repaired scalar
\(\mathcal R_J\) and the exact reduced scalar \(\mathscr S\) remain distinct
available quantities.

Round 24 makes that scalar problem coordinatewise.  At fixed \(x=r+p\),
strict convexity in \(p\) leaves at most two adjacent shelf owners.  On the
delicate quadratic top cell the terminal action eliminates \(\alpha\) exactly
in favor of \((B,u)\), and the lower shelf wall obeys
\(t_\mu<0\), \(W_\mu<0\), \(\lambda_\mu>0\).  The resulting \(t\)- and
\(p\)-candidate rules are coupled; \(\widehat{\mathcal C}_8\) is used only
when \(B=f-1\) and \(0<u<1/\sqrt2\), while other cells are not reduced by
this step.  At the end of Round 24 the analytic obligation was the coupled
stationary-value sign, not a global monotonicity assertion in \(\alpha\).

Round 25 evaluates that stationary value exactly on the delicate cell.  Put

\[
 H=\tan t-t,\qquad z=\tan(t/2),\qquad
 L=\frac{4u(B+u)\tan^2t}{H},
\]

and

\[
 R=\frac m\pi+\frac{B\pi}{2t^2}-L.
\]

Put

\[
 P=\frac{3\pi^2(B+u)R}{H\sin t},
 \qquad
 p_{\max}=\min\{\mu-m-1,\psi(P)\},
\]

where \(\psi(P)\) is the positive root of
\(\psi^2(2\psi+3)=P\).

At an interior fixed-\(\mu\) stationary point, \(R>0\) and

\[
 \mathcal C_8=
 m\left(\frac12-\frac t\pi+\frac z\pi\right)
 +B\left(\frac\pi{2t}-1+\frac{\pi z}{2t^2}\right)
 -\frac p2-\frac18+2u^2-zL.
\]

The two exact shelf integrals imply a strict \(m\)-window.  Together with
stationarity and the interface/owner bounds they give
\(p\le p_{\max}\) and hence

\[
 \mathcal C_8\ge\mathcal F(B,m,t,u).
\]

This reduction cannot be closed from the endpoint window alone: directed Arb
arithmetic certifies \(\mathcal F<-34.18\) at the relaxed rational point
\((B,m,t,u)=(1,11,1/5,1/1000)\).  That point is not in the exact projected
shelf image, so it is not a counterexample to \(\mathcal C_8\), CST, or the
theorem.  At the end of Round 25, the remaining proposed pointwise obligation
was \(\mathcal F\ge0\) on the full paired-shelf projection.

Round 26 reconstructs that exact projection and shows that this last
relaxation is also too weak.  For fixed \((B,m,t,u)\) and a parity grid, the
values \(\mu,q,\alpha,x\) are determined, and a stationary owner must solve
\(p^2(3x-p)=P\); the left side is strictly increasing on the owner range.
At the certified half-grid tuple

\[
 (B,f,m,r,p,\alpha,\mu)
 =\left(1,2,6,\frac{25}{2},6,\frac9{10},\frac{127}{5}\right),
\]

\(p=6\) is the unique stationary and discrete minimizing owner, all exact
shelf/activity/cell conditions hold, and

\[
 \mathcal F<-\frac1{50}<0<\frac{77}{50}<\mathcal C_8.
\]

Thus the \(p\mapsto p_{\max}\) replacement, not the shelf projection, causes
the failure.  A second certified exact feasible half-grid point

\[
 r=\frac{57755}{2},\qquad p=80,\qquad m=15,\qquad
 f=2,\qquad \alpha=\frac12,
\]

and its nearby unique stationary point satisfy \(\mathcal C_8<-7\).  At the
same point the exact reserve accounting is

\[
 \mathcal R_J
 =\mathcal C_8+(p+a_p)(L_0-L_{\rm curv})
  +\left(\frac18-J\right)>20.
\]

Hence neither \(\mathcal F\ge0\) nor \(\mathcal C_8\ge0\) is a valid global
sufficient target.  Round 27 shows that the next two compressed global signs
also fail.  At the exact integer-grid tuple
\[
 (r,p,m,f,\alpha,\mu,t)
 =\left(4036,32,1,2,\frac1{16},\frac{65105}{16},\frac{79}{500}\right)
\]
directed Arb arithmetic certifies
\[
 \mathcal C_{\max,8}<-\frac43,
 \qquad \mathcal R_J<-\frac65,
 \qquad \mathscr S>47,
 \qquad \Phi_\delta>40.
\]
Thus the failure is in the compression, not in the exact shifted-tail lower
bound.

To recover the strategy's intrinsic remainder-rich case, set \(d=1-2t/\pi\)
and
\[
 E=e_0+e_p,\qquad \Delta=e_0-e_p,
 \qquad E_*=\frac12-\frac{dm}{2p}.
\]
The exact Round 10 inequality is
\[
 D_A(r)\ge
 \max\{0,L_T\}+a_p\Delta+p(E-E_*).
\]
It proves \(D_A(r)\ge0\) whenever \(p\le dm\) or \(E\ge E_*\).  The Round
27 negative \(\mathcal R_J\) witness has \(E>1>E_*\) and therefore belongs to
this closed automatic branch.  Only
\[
 p>dm,\qquad 0\le E<E_*<\frac12
\]
remains, with the exact obligation
\[
 \max\{0,L_T\}+a_p\Delta\ge p(E_*-E).
\]
The available sharpened wall transport is
\[
 \Delta\ge\frac{s-1}{s+1}(E+2\lambda).
\]
A proof of \(\mathcal C_{\max,8}\ge0\) is sufficient only on this residual
sector and is strictly stronger than the exact obligation; it must not be
treated as an equivalent or global target.  If it fails, return to the exact
residual, then to \(\mathscr S\) or the weighted aggregate.  No
manuscript-level all-dimensional conclusion is currently available.

Round 28 returns to the exact residual and retains the actual endpoint sum.
The first two positive curvature-series terms give the strict payment
\[
 \mathcal K_4=
 \frac{(\mu^{-1}-K^{-1})((r+p)^2-r^2)}{2\pi}
 +\frac{(\mu^{-3}-K^{-3})((r+p)^4-r^4)}{24\pi},
\]
while elasticity gives
\[
 \Delta\ge\tau(E+2\lambda),\qquad \tau=\frac{s-1}{s+1}.
\]
Thus, with
\[
 M_4=\max\{\tau(E+2\lambda),\mathcal K_4\},
\]
the audited chain is
\[
 D_A(r)\ge\Phi_\delta^+
 \ge\Psi^{L_T}_{4,E}
 :=\max\{0,L_T\}+a_pM_4+p(E-E_*)
 \ge\Psi^{\rm rf}_{4,E}.
\]
The first projected scalar is the primary target because it keeps every
inverse fraction, the exact cap, the top interval, and \(E\).

For fixed discrete/interface data, activity also gives
\[
 \frac{d}{dt}\{E(t)-E_*(t)\}>0
 \quad\hbox{whenever }p>d(t)m.
\]
Hence the hard set is one initial phase interval.  A separate literal
maximum analysis gives a unique elasticity/curvature switch, strict convexity
on curvature cells, and at most one elasticity stationary minimum on the
quadratic top-payment cell.  These are finite-candidate reductions only.
Round 29 removes the interior-candidate ambiguity for the primary scalar.
On every fixed-\(\alpha\) literal terminal count cell,
\[
 \frac{d}{dt}\Psi^{L_T}_{4,E}>0.
\]
On every fixed-\(Q\), constant-\(K\) inverse or outer-\(B\) wall segment on
the inherited extension grids,
\[
 \frac{d}{d\mu}\Psi^{L_T}_{4,E}<0.
\]
The raw terminal jumps at inverse, \(Q\), and outer-\(B\) walls are
\(-2\), \(-1\), and \(-1/(16\beta)\), respectively; clipping is retained in
the exact one-sided scalar.  Finally, the entire component
\[
 (r,p,m,f)=(1,2,2,2),\qquad B=Q=1,\qquad 2<y_1<3
\]
satisfies the analytic estimate
\[
 \Psi^{L_T}_{4,E}>
 \frac{371}{15840}+2\eta_1+2E>0.
\]
Round 30 treats the first nonconstant-\(K\) faces without restoring a lossy
global scalar.  Activity is automatic throughout
\(B=Q=1,\ 2<y_1<3\).  On its included lower shelf,
\[
 \frac{dL_T}{d\mu}>0,\qquad L_T>\frac7{10},
\]
and the exact retained-\(E\) projection is
\[
 \Psi^{L_T}_{4,E}>
 \mathfrak F(q,r,p,m)
 =
 T(q)+a_p\mathcal K_{4,\min}
 +p\left(E_{\min}-\frac12\right)
 +\frac{m d_{\min}}2.
\]
The exact image must satisfy
\[
 G_{K_3}(q-m)-G_q(q-m)\ge\frac74,\qquad
 p>d_{\min}m,\qquad
 E_{\min}<\frac12-\frac{d_{\min}m}{2p}.
\]
The open lower \(Q\)-wall has \(0<y_1<\alpha<1\), so it has no inverse or
\(B\)-wall intersection and cannot supply a noncorner endpoint to any
\(y_1>1\) band.  On \(\alpha=0,\ f=2\), the complete terminal concavity
bound and normalized curvature give positivity for
\[
 \frac45\le t<\frac{13}{10}.
\]

Round 31 proves that this shelf problem is finite.  For fixed \((q,m)\), the
dependent profile \(p\mapsto\mathfrak F(q,q-m-p,p,m)\) is strictly convex.
At fixed integration
radius \(a\), its normalized second-derivative kernel is
\[
 \frac{2u}{\sqrt{1-u^2}}+
 v\left(1+\frac{u^2}{2}+\frac{v^2}{3}
 -(1-u^2)^{-3/2}\right)>0,\qquad
 u=\frac ra,\quad v=\frac pa,\quad u+v<1.
\]
For \(q\ge1000\), exact phase estimates force
\(m>11q^{1/3}/10\).  The retained-\(E\) lower bound then yields the intrinsic
bootstrap
\[
 1\to\frac{25}{17}\to\frac53\to2\to\frac{25}{11}
 \to\frac52\to3\to4\to10
\]
for \(p/(d_{\min}m)\), ending in a contradiction to the hard bound.  This
excludes every real \(q\ge1000\) without a shell-ratio ladder.  Moreover,
discarding only positive terms gives a finite lower scalar \(L_q\) whose Hessian has
negative determinant at every interior critical point, so its minimum reduces
to the three strictly convex edges \(p=1\), \(r=r_0\), and \(m=1\).

Round 32 closes that finite shelf without asserting the false full
\(m=1\) edge.  With \(\psi=\arccos(q/K_3)\), shelf feasibility self-improves
for every real \(q\ge35\) to
\[
 m>\frac65\left(\frac{\pi}{\psi}-3\right).
\]
The finite triangle is therefore truncated at the corresponding integer
\(m_0\); below \(q=35\), retain \(m_0=1\).  The \(p=1\) edge is \(>1/5\).
One compact directed-Arb certificate encloses the continuous convex minima
on \(r=r_0\) and \(m=m_0\) for every exact integer and half-integer
\(3\le q<1000\), proving the rational margin \(L_q>1/100\).  Together with
the Round 31 real \(q\ge1000\) exclusion,
\[
 \Psi^{L_T}_{4,E}>\mathfrak F>L_q>0
\]
on the entire Round 30 included shelf.  The finite scan with 933 relaxed
records and cutoff \(q=33\) remains diagnostic only.

Round 33 now controls the geometry of the cleanest first face.  On the open
lower-\(Q\) hard arc, \(B=1\), \(0<y_1<\alpha<1\), no inverse or outer-\(B\)
wall intersects, and
\[
 L_Q=\frac{\pi}{2\theta_1}+2y_1-1-J>\frac3{28}+2y_1.
\]
The exact action \(A(x)-A(q)\ge1\) and the lower-\(Q\) wall factorization prove
\[
 \frac{d}{d\mu}(E-E_*)<0.
\]
Thus a hypothetical hard component persists to \(e_p=0\), an activity wall,
or \(\alpha\to1^-\).  This does not make the full projected scalar monotone.
Round 34 removes the activity wall on every high-floor first shelf.  More
importantly, it compares the terminal action and preceding shelf through the
same radial-parameter integral and reduces lower-\(Q\) hard exclusion to the
intrinsic \(Q\to1^-\) face and one possible second stationary root.  The
small-phase adjacent-action theorem closes \(0<t\le\pi/8\).  Round 35 closes
the middle phase by a retained quadrature estimate, the large boundary by one
exact polynomial, the stationary root by an action-cutoff discriminant, and
proves the domain empty for \(t\ge3\pi/14\).  Thus the lower-\(Q\) hard sector
is closed.  Round 36 then gives the exact count topology
\[
 B-Q\in\{0,1\}.
\]
On the one-level-gap branch,
\[
 L_T>1-J>\frac67,
 \qquad
 \Psi^{L_T}_{4,E}>\frac67-\frac{p-dm}{2},
\]
so \(p-dm\le12/7\) is closed, including all hard \(p=1\) gap faces and
old inverse collisions.  The exact wall map transports the residual gap
candidates to general lower shelves or \(\alpha\to1^-\).  Round 37 then
proves on every hard gap point that
\[
 B_0=Q=B-1\ge1,
 \qquad j=f-B=\lfloor\lambda\rfloor,
\]
and that the terminal top interval is zero.  Defining the exact positive
inverse-angle reserve \(\Omega\) and \(\Xi=E-M_4\ge0\), it obtains the
identity that is exact for the selected projected scalar
\[
 \Gamma_{\rm gap}
 =1-J+\frac{B_0d}{2c}+\Omega
 +(p+a_p)M_4+p\Xi-\frac{p-dm}{2}.
\]
It also proves \(\Phi_\delta^+>\mathcal H_\Delta\) for a count-free maximum
of three correlated shelf payments.  Round 38 then puts
\(u=\lambda-j\), \(S_q=A(q)-W\), and \(\chi=u-S_q\), and proves
\[
 0<S_q\le u<S_q+h<\frac{\alpha}{2},
 \qquad 0\le\chi<h,
 \qquad 0<u<\frac{\alpha}{2}<\frac12.
\]
In particular there is no positive-alpha integer-\(\lambda\) wall.  With
\(\widehat\Xi=\Delta-M_4\ge0\), it refines the selected scalar and proves
the intrinsic count--phase bound
\[
 B_0\left(\frac{\pi}{2t}-1\right)>\frac15.
\]
Therefore
\[
 \Gamma_{\rm gap}>
 \frac{37}{35}-\frac{p-dm}{2},
\]
which closes every one-level gap with \(p-dm\le74/35\), including every
residual \(p=2\) gap.  All remaining one-level gap work has \(p\ge3\).
Round 38 also proves a unified \(\chi\)-compensation lower bound for
\(\Phi_\delta^+\) that interpolates between the \(Q\)-wall newest-inverse
payment and the outer-\(B\) adjacent-action payment.  That lower bound is
structural; it is not a new certificate.

Round 39 first sharpens the cap on this residual sector.  Put
\(x=r+p\) and \(q=x+m\).  Since \(p\ge3\), one has \(q\ge5\), and the cap
monotonicity from Round 23 gives
\[
 J<2I_{q+1}(q)\le2I_6(5)<\frac1{10}.
\]
Together with \(B_0\zeta>1/5\), this yields
\[
 \Gamma_{\rm gap}>
 \frac{11}{10}-\frac{p-dm}{2}.
\]
Hence every gap with \(p-dm\le11/5\) is closed.  In particular, any
remaining \(p=3\) gap satisfies \(dm<4/5\).

On the gap-side outer-\(B\) wall, put
\[
 \beta=\frac1\pi\arccos\frac qK,\qquad v=G_K(q),\qquad
 U_z=(\mu^2-z^2)^{1/2},\qquad
 g=\frac{U_r}{U_x}-1,\qquad
 R_1=\frac{U_r-U_x}{U_x-U_q}.
\]
There \(B_0=v-3/4\), \(y_B=0\), and the selected scalar is exactly
\[
 \Gamma_{\rm OB}=
 \frac1{2\beta}-J+\Omega_-+B_0\zeta
 +p\Delta+a_pM_4+2pe_p-\frac{p-dm}{2}.
\]
The exact action coordinates and the adjacent-action and elasticity bounds
give the single intrinsic inequality
\[
\begin{aligned}
 \Gamma_{\rm OB}>F_{\rm OB}:={}&
 \frac1{2\beta}-J+\Omega_-+(v-\tfrac34)\zeta\\
 &+pR_1[A(x)-A(q)]+a_pg[A(x)-W]+2pe_p
 -\frac{p-dm}{2}.
\end{aligned}
\]
Its entire displayed loss is
\[
 p\{\Delta-R_1[A(x)-A(q)]\}
 +a_p\{M_4-g[A(x)-W]\}>0.
\]
If an inverse-root-free projection is needed, retain
\[
 \Omega_-\ge\Omega_{\rm RF}:=
 \frac{\pi^2}{2Kt^3\sin t}
 (v-\tfrac34)(W-\tfrac v2+\tfrac18).
\]
This is a projection of the same inequality, not another global scalar or
compact certificate.

At the simultaneous outer-\(B\)/lower-shelf endpoint, \(e_p=0\).  Round 39
proves from the exact endpoint floor geometry that \(j\ge1\), and then a
single phase-stretch inequality makes the above intrinsic residual strictly
positive.  Thus that complete endpoint is closed.  The one-sided
upper-\(\alpha\) outer-\(B\) endpoint is the final Gate-A face addressed
below.

Round 40 returns on this endpoint to the exact \(p\Delta\) term.  For
\[
 \mathcal D(z)=b_K(z)-b_\mu(z),\qquad y=r+\frac p2,
\]
strict midpoint convexity and a cosine chord yield
\[
 p\Delta>p^2\delta_y,\qquad
 \delta_y=\frac{y(1-\cos t)}
 {\pi\sqrt{\mu^2-y^2\cos^2t}}.
\]
Writing \(N=p/2+m+1\), \(\rho=N/\mu\), and
\[
 C(\rho,t)=\frac{(1-\rho)(1-\cos t)}
 {\pi\sqrt{\sin^2t+2\rho}},
\]
one has \(\delta_y>C\).  The outer count satisfies
\(B_0>W/4+9/16\), hence
\[
 \Gamma_{\rm OB}>\mathcal R(\mu,p,m,t)
 =\frac9{10}+\frac9{16}\zeta+\frac14\zeta\mu L_0(t)
  +p^2C(\rho,t)-\frac{p-dm}{2}.
\]
This lower expression is strictly increasing in \(\mu\), while feasibility
gives \(\mu\ge p+m+2\) and \(\mu>5/(4L_0)\).  Therefore the endpoint would
close once the single sign
\[
 \mathcal R_*(p,m,t):=
 \mathcal R\!\left(\max\left\{p+m+2,\frac5{4L_0(t)}\right\},p,m,t\right)>0
\]
is proved.  The two analytic branches are strictly convex in one auxiliary
variable and agree at their seam.  Round 40 proves this reduction, not the
last continuum sign.  Round 41 proves exact global rational enclosures and
transports both branch signs to fixed rational polynomial problems.  Its
exact replay checks 4,405 Bernstein coefficients (4,259 positive and 146
zero) and ends in `round41BernsteinSignReplayOK=True`.  The independent audit
verdict is NOT PASS as a strategy-authorized analytic closure and PASS only
as an exact structural reduction and computer-assisted candidate.  The
certificate is therefore not a premise of this draft: \(\mathcal R_*>0\) and
the endpoint remain open.  The selected
\(\Gamma_{\rm OB}\to\mathcal R_*\) projection is analytically exhausted; the
last stronger Gate-A specialization is Round 42.  At
\(\chi=h,\ y_B=0,\ \alpha\uparrow1^-\), put
\[
 H=(p+a_p)R_1,\qquad M=\min\{\zeta,H\}.
\]
The exact endpoint identity and the Round 38 adjacent-action bound imply the
strict structural reduction
\[
 \boxed{\Phi_\delta^+>\mathcal T_{42}},\qquad
 \mathcal T_{42}:=\frac9{10}+B_0M+Hh-\frac{p-dm}{2}.
\]
With
\[
 \mathcal A_{\rm adj}:=(p+a_p)
  [\Delta-R_1(j+e_p+h)]>0,\qquad
 \mathcal A_{\rm cap}:=\frac1{2\beta}-J-\frac9{10}>0,
\]
the complete loss ledger is the exact identity
\[
 \boxed{
 \Phi_\delta^+-\mathcal T_{42}
 =\mathcal A_{\rm cap}+\Omega_-+\mathcal A_{\rm adj}
  +B_0(\zeta-M)+jH+(H+2p)e_p.}
\]
The algebra-only replay ends in
`round42StrongerPhiReplayOK=True`.  The independent verdict is STRUCTURAL PASS
only; final sign open.  Round 43 retains the exact hard correlation
\[
 E<E_*:=\frac{p-dm}{2p}
\]
and proves the hand-checkable envelopes
\[
 H\ge\underline H:=
 \frac{(p+a_p)p(2r+p)}{m(2x+m)}
 \min\!\left\{\frac{U_x}{U_r},
 \sqrt{\frac{U_q}{U_r}}\right\},
 \qquad h>\frac{U_q^3}{3\pi\mu^2}.
\]
An exact relaxed family has \(\lim\mathcal T_{42}/N<0\), so the count--phase
and radial data alone cannot sign the target; the family leaves the common
shelf.  A finite high-precision negative diagnostic satisfies the synchronized
outer wall, activity, common shelf, and terminal first drop, but fails the
hard owner precisely at \(E<E_*\).  It is not an interval certificate or a
counterexample on the live owner.  For fixed \((r,p,m,f)\), Round 43 also
proves
\[
 \boxed{\frac d{dt}(E_f-E_*)=
 \frac1\pi\left[\tan t\left(\sqrt{K^2-r^2}+\sqrt{K^2-x^2}\right)
 -\frac mp\right]>0}.
\]
This transport is chart-local: \(E_{f+1}=E_f-2\), while the outer face samples
the separate integer \(B_0\)-walls.  Global continuation therefore requires
the forbidden \(f\)-, \(B\)-, or \(j\)-indexed wall family.  The independently
audited Round 43 decision is analytic structural PASS and **Gate A STOP**.
Gate B is active and restores the exact shifted-tail scalar
\[
 \boxed{\mathscr S=D_A(q)+R_p+\frac{dm}{2}}.
\]
No sign of \(\mathcal T_{42}\) on its exact owner is proved:
\(\mathcal T_{42}\ge0\), this endpoint, CST, and the theorem remain open.

Higher
equal-count \(Q_N\) and inverse faces, generic equal-count inverse faces, the
\(\alpha=0\) combined corners, and lower shelves outside the proved Round 32
and Round 39 scopes remain open.  The backbone audit, high-floor CST, final
assembly, and all-dimensional theorem remain open; no global
\(\alpha\)-monotonicity shortcut is available.
