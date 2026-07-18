# Independent audit: Round 8C active-width terminal extension

Date: 18 July 2026  
Status: **FINAL PASS**

Audited frozen artifacts:

- `human/outbox/general-d-round-08c-active-width-terminal.md`  
  SHA-256 `55078C3D1E1EC060994FD8DD26D2F6D9F602F03C23A79CBB33B25E326ADCDA50`;
- `scripts/general_d_high_floor_active_width_verify.py`  
  SHA-256 `267900ED39C17C02D1BBDEB17B5F36AB616601DEE8127D98E50A9646BCEDCAB5`.

Neither frozen artifact was edited during this audit.

The audited conclusion is exactly

\[
 f\geq2,\qquad p<n,\qquad \frac{939}{1000}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Round 8C proves the closed overlap band
\(939/1000\leq\rho\leq477/500\); the already audited Round 8B theorem
owns \(\rho\geq477/500\).  Thus the shared endpoint is covered twice and
there is no ratio gap.  The result is a ratio exclusion and compact
reduction, not a certificate of the residual fixed-ratio walls.

## 1. Active width and the interface floor

The ordinary first-shelf floor gives

\[
 A(r)\geq h:=f-\frac14,
\]

while strict monotonicity at positive \(r\) gives

\[
 A(0)=\frac{K-\mu}{\pi}>A(r).
\]

Consequently, with \(a=(1-\rho)K\), every configuration in scope obeys
the strict active inequality \(a>\pi h\).  Put

\[
 g_\rho=G_1(\rho),\qquad W=Kg_\rho,
 \qquad \delta=h-W>0,
 \qquad \lambda_\rho=\frac{\pi g_\rho}{1-\rho}.
\]

Since \(W=ag_\rho/(1-\rho)\), active width gives

\[
 W>\lambda_\rho(W+\delta).
\]

This inequality itself proves \(0<\lambda_\rho<1\), so division by
\(1-\lambda_\rho\) is legitimate.  The exact representation

\[
 \pi g_\rho=\int_0^{1-\rho}\arccos(1-y)\,dy
\]

and \(\arccos(1-y)>\sqrt{2y}\) yield

\[
 \lambda_\rho>\frac{2\sqrt2}{3}\sqrt{1-\rho}.
\]

Only \(\rho\leq477/500\) needs the new argument.  Hence
\(1-\rho\geq23/500\), and the exact square margin is

\[
 \frac89\frac{23}{500}-\frac1{25}=\frac1{1125}>0.
\]

Thus \(\lambda_\rho>1/5\).  Since \(f\geq2\),
\(\delta\geq7/4-W\), and therefore

\[
 W>\frac{\lambda_\rho}{1-\lambda_\rho}\delta
 \geq\frac{\lambda_\rho}{1-\lambda_\rho}
       \left(\frac74-W\right)
 \quad\Longrightarrow\quad
 \boxed{W>\frac74\lambda_\rho>\frac7{20}}.
\]

All directions remain strict.  This is stronger than the earlier target
\(W>329/2000\), by the exact amount \(371/2000\).

## 2. Common prefix and endpoint constants

At \(\rho=939/1000\), directed Arb evaluation proves

\[
 (\arccos\rho)^2<\frac{31}{250},\qquad
 c=\frac{\arccos\rho}{\pi}<\bar c:=\frac{14}{125}.
\]

Both left sides decrease with \(\rho\), so these bounds hold on the
whole overlap band.  In particular
\(\gamma=3/25-c>0\) and \(d=1-2c>0\).

I rechecked the two inputs to the common \(\delta\geq1\) prefix.  The
present-level coefficient exceeds the common one by

\[
 \frac18-\frac3{25}=\frac1{200}>0.
\]

The absent-level degree-32 Bernstein reconstruction has exact smallest
coefficient \(309/396800>0\).  The endpoint-chord and elasticity
arguments therefore give, on both faces,

\[
 cP>\left(\frac3{25}-c\right)\delta-\frac{cd}{2}.
\]

The frozen Round 8B dependency still has the previously audited hashes
`07797739D2EDE8747B73E217517DB22B3A8023CBA92919DF81D984AA2500FAF6`
for its note and
`BD97F156E2DF150ABAD501D20527A618A98CD3450D6B683BCF09BBA4F7C8F63D`
for its verifier.

## 3. Strict-wall terminal partition

The strict counts are

\[
 B_0=[W+1/4]_<,\qquad B=[G_K(q)+1/4]_<,
 \qquad Q=[A(q)+1/4]_<.
\]

Monotonicity gives \(B\geq B_0\), while
\(0\leq A(q)-W<c<1\) gives \(Q\leq B_0+1\) with the same strict
convention.  Thus the \(\delta\geq1\) split is exhaustive:

- \(B_0\geq1\);
- \(B_0=0,Q=0\);
- \(B_0=0,Q=1\).

There is no fourth count face.  The equality \(\delta=1\) belongs to
this ledger.  The wall \(W=3/4\) belongs to \(B_0=0\), and the wall
\(A(q)=3/4\) belongs to \(Q=0\).

### 3.1. The face \(B_0\geq1\)

The exact-angle reserve, cap payment, and common prefix give

\[
 c\mathcal S>\frac{31}{50}-\frac{39}{10}c+c^2.
\]

The coefficients of \(B_0\) and \(\delta\) used before this
minimization are positive.  The displayed polynomial is decreasing for
\(0<c\leq14/125\), and its exact endpoint value is

\[
 \frac{6117}{31250}>0.
\]

### 3.2. The face \(B_0=Q=0\)

Here the strict convention gives \(0<W\leq3/4\), the discrete tail is
empty, and the outer tangent triangle gives \(cD_A(q)\geq W^2\).  After
the active floor, the relevant expression is

\[
 L_0(c,W)=
 \left(\frac3{25}-c\right)\left(\frac74-W\right)
 -\frac c2+c^2+W^2,
 \qquad W>\frac7{20}.
\]

On this domain

\[
 \partial_W L_0=2W-\left(\frac3{25}-c\right)
 >\frac7{10}-\frac3{25}=\frac{29}{50}>0.
\]

It is therefore safe to take the unattained lower endpoint
\(W=7/20\).  The resulting polynomial decreases in \(c\), and at
\(c=14/125\) equals

\[
 \frac{22561}{250000}>0.
\]

No continuity assertion fills the open active wall; the endpoint is
used only as a lower infimum.

### 3.3. The face \(B_0=0,Q=1\)

Strict bracketing gives

\[
 \frac34-c<W\leq\frac34.
\]

The active lower bound is redundant here because
\(3/4-c>7/20\).  The terminal expression is concave in \(W\), so its
infimum is controlled by the two endpoints.  Their exact values at
\(c=14/125\) are

\[
 \frac{273}{400}-\frac52c+c^2
 =\frac{103761}{250000}>0,
\]

\[
 \frac{273}{400}-\frac{119}{50}c-c^2
 =\frac{100849}{250000}>0.
\]

The lower \(W\)-endpoint is open, so evaluating it is again a safe
infimum bound.  Both endpoint polynomials decrease throughout the
certified \(c\)-range.

These three cases exhaust every \(\delta\geq1\) strict wall.

## 4. Retuned small-\(\delta\) certificate

For \(0<\delta<1\), strict bracketing fixes

\[
 B_0=f-1,qquad
 y=f-W=\delta+\frac14\in\left(\frac14,\frac54\right).
\]

Scale monotonicity reduces the largest level distance to \(f=2\).
Then \(W=2-y\) and

\[
 x=\frac yW\in\left[\frac17,\frac53\right].
\]

The physical interval is open at the two extreme \(y\)-values, but
checking the closed \(x\)-interval is conservative.  The exact second
derivative of the normalized increment is nonpositive, so its minimum
is controlled by these two \(x\)-endpoints.

With \(t_0=3y/c\) and \(u_0=t_0/\mu\), the retuned constants give

\[
 u_0<\frac53\frac{31/250}{939/1000}
 =\frac{620}{2817}<\frac{111}{500}<1,
 \qquad \frac{u_0}{1-\rho}>2x.
\]

The first inequality keeps \(t_0\) strictly inside the physical radial
domain.  The second permits retention of the whole interval
\(0\leq v\leq2x\).  The omitted part of the exact integral is positive:
its two arccos arguments have ordered gaps while \(u_0<1\).

For

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),
\]

the positive coefficients of \(S\) decrease.  On the subtracted copy,

\[
 z\leq\frac{61}{300},\qquad
 \frac{3/160}{1-61/300}=\frac{45}{1912}.
\]

Termwise integration gives exactly \(45/6692\).  The positive first
copy is used only for

\[
 z\leq\frac{793}{3000}<1.
\]

Thus both series copies stay inside the stated convergence domain.  I
also rederived every coefficient of the lower integral in equation (26)
of the frozen note.

The alternating Taylor bounds for \(1-\cos\theta\) and
\(\sin\theta-\theta\cos\theta\) reduce the coefficient to

\[
 \rho\sqrt2\,
 \frac{(1/2-t/24)^{3/2}}
 {1/3-t/30+t^2/840},
 \qquad t=\theta^2.
\]

Its logarithmic derivative has sign opposite to
\(84+10t-t^2/2\), which is positive on
\(0\leq t\leq31/250\).  Directed endpoint evaluation therefore proves
\(C_\rho>7/5\) throughout the band.

The verifier partitions
\([939/1000,477/500]\) into 64 closed rational panels.  Its interval
constructor explicitly checks containment of both endpoints of every
panel.  On each full panel it proves, at both \(x\)-endpoints,

\[
 \mathcal I_\rho^{\mathrm C}(2x)>0,
 \qquad \frac75\mathcal I_\rho^{\mathrm C}(2x)-x>0.
\]

Separate positivity of the integral is essential before replacing
\(C_\rho\) by \(7/5\), and the code checks it.  Concavity then fills the
entire \(x\)-interval and proves \(T<3y/c\).  The remaining exact
terminal calculation gives the decreasing polynomial

\[
 c\mathcal S>\frac5{16}-\frac{29}{10}c+c^2
 \geq\frac{61}{250000}>0.
\]

Hence the split \(\delta\geq1\) versus \(0<\delta<1\) is complete,
including the strict ownership of \(\delta=1\).

## 5. Residual cutoff and integer ranges

For \(0<\rho<939/1000\),

\[
 \eta_\rho=G_1(\max\{\rho,1/2\})
\]

is decreasing in its argument.  Directed endpoint evaluation and the
known value at \(1/2\) give

\[
 \frac1{221}<\eta_\rho<\frac19.
\]

Monotonicity of \(2\pi\rho/(1-\rho)\), together with
\(\pi<355/113\), gives

\[
 a_\rho<\frac{666690}{6893}.
\]

Using \(1/2<C_*<13/10\), exact arithmetic gives

\[
 a_\rho+2\eta_\rho C_*
 <\frac{666690}{6893}+\frac{13}{45}
 =\frac{30090659}{310185}<98.
\]

Moreover,

\[
 (a_\rho+2\eta_\rho C_*)^2-
 (a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2)
 =\eta_\rho^2(4C_*^2-1)>0.
\]

Substitution into the imported fixed-ratio threshold therefore gives

\[
 K_0(\rho)<98\cdot221^2=4\,786\,418.
\]

For a negative candidate, \(K<K_0(\rho)\) and \(p\neq0\).  Thus
\(p\geq1\), \(n\geq2\), and \(r<\mu<K\).  Strict inequalities plus
integrality give exactly

\[
 \rho>\frac1{9\,572\,836},\qquad
 1\leq2r\leq9\,572\,835,
\]

\[
 2\leq n\leq4\,786\,417,qquad
 1\leq p\leq n-1.
\]

Finally \(A(r)\geq7/4\), \(A(0)>A(r)\), and \(\pi>3\) give
\(K>21/4\) and

\[
 f,B<\frac K3+\frac14
 <1\,595\,472+\frac{11}{12}.
\]

Therefore

\[
 2\leq f\leq1\,595\,472,
 \qquad 0\leq Q\leq f-1,
 \qquad Q\leq B\leq1\,595\,472.
\]

The bounds \(Q\leq f-1\) and \(Q\leq B\) follow respectively from
the first-drop sample after the shelf and from
\(A(q)<G_K(q)\), with the strict bracket retained.  No endpoint is lost
when the strict real inequalities are converted to integer ranges.

## 6. Independent replay and scope

I replayed the frozen verifier with python-flint 0.8.0 at 384, 512, 768,
and 1024 bits.  All four runs returned exit code zero and identical exact
ledgers.  At every precision the smallest directed values were

\[
 \mathcal I_\rho^{\mathrm C}(2x)>0.203762865224\ldots,
\]

\[
 \frac75\mathcal I_\rho^{\mathrm C}(2x)-x
 >0.0456615050931\ldots.
\]

The five exact terminal margins are

\[
\begin{array}{c|c}
 \delta\geq1,\ B_0\geq1&6117/31250\\
 \delta\geq1,\ B_0=Q=0&22561/250000\\
 \delta\geq1,\ B_0=0,\ Q=1,\ W=3/4&103761/250000\\
 \delta\geq1,\ B_0=0,\ Q=1,\ W=3/4-c&100849/250000\\
 0<\delta<1&61/250000
\end{array}
\]

The smallest is positive.  I found no proof-direction, active-width,
strict-wall ownership, series-domain, interval-coverage, cutoff, range,
or implementation defect.

**Final audit verdict: PASS.**
