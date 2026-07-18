# Independent audit: Round 8B high-floor terminal payment

Date: 18 July 2026  
Status: **FINAL PASS**

Audited frozen artifacts:

- `human/outbox/general-d-round-08b-high-floor-absent-terminal.md`  
  SHA-256 `07797739D2EDE8747B73E217517DB22B3A8023CBA92919DF81D984AA2500FAF6`;
- `scripts/general_d_high_floor_absent_terminal_verify.py`  
  SHA-256 `BD97F156E2DF150ABAD501D20527A618A98CD3450D6B683BCF09BBA4F7C8F63D`.

Neither frozen artifact was edited during this audit.

The audited conclusion is exactly

\[
 f\geq2,\qquad p<n,\qquad \frac{477}{500}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Together with the fixed-ratio scalar theorem, every remaining negative
high-floor first-drop candidate is confined to

\[
 \frac1{29\,931\,928}<\rho<\frac{477}{500},\qquad
 \frac{21}{4}<K<14\,965\,964.
\]

This is a rigorous ratio exclusion and compact reduction, not a certificate
of the remaining fixed-ratio walls.

## 1. Endpoint chord and common prefix

I rederived the first-shelf endpoint-chord inequality with ordinary floors:

\[
 P:=R_p+\frac d2m
 \geq-\left(\frac14+\zeta\right)(T-M)+\frac d2(M-1),
 \qquad M\geq\frac\delta c,
\]

where \(m=n-p\), \(d=1-2c\), \(c=\arccos(\rho)/\pi\), and
\(\delta=f-1/4-W\).  The factor of two, chord direction, and
\(m\geq M-1\) all agree with the exact shelf identity.

For \(\delta\geq1\), the shell-increment elasticity gives \(T/M\leq5/2\)
when level \(f\) is present.  Hence

\[
 cP\geq\left(\frac18-c\right)\delta-\frac{cd}{2}.
\]

On the absent-level face, write \(a=1/4-\zeta\).  The elasticity inversion
and the degree-32 Bernstein inequality give

\[
 \left(\frac12-a\right)(T/M-1)<\frac{19}{50},
\]

and therefore

\[
 cP>\left(\frac3{25}-c\right)\delta-\frac{cd}{2}.
\]

The present coefficient is larger by exactly
\(1/8-3/25=1/200\).  Thus both level faces have the common strict bound

\[
 cP>\gamma\delta-\frac{cd}{2},\qquad
 \gamma=\frac3{25}-c>0.
\]

I independently reconstructed all 33 degree-32 Bernstein coefficients of
the polynomial majorant.  They are positive, and the exact minimum is
\(309/396800\), at coefficient 30.  The auxiliary radical bound
\(\sqrt{a(2+a)}\leq3\sqrt a/2\) has the correct direction on
\(0\leq a\leq1/4\).

## 2. Complete audit of the \(\delta\geq1\) terminal split

With strict brackets,

\[
 B_0=[W+1/4]_<,\qquad B=[G_K(q)+1/4]_<,
 \qquad Q=[A(q)+1/4]_<.
\]

Monotonicity gives \(B\geq B_0\).  Since
\(0\leq A(q)-W<c\), strict bracketing gives \(Q\leq B_0+1\), including
on action walls.

If \(B_0\geq1\), every retained ball angle is strictly smaller than
\(\pi c\).  The exact-angle reserve and
\(2\int_q^\mu G_\mu<2/5\) therefore give

\[
 cD_A(q)>
 \frac{B_0}{2}-cQ-\frac{2c}{5}
 \geq B_0\left(\frac12-c\right)-\frac{7c}{5}.
\]

Minimizing at \(B_0=\delta=1\) produces

\[
 c\mathcal S>\frac{31}{50}-\frac{39}{10}c+c^2.
\]

If \(B_0=0\), the strict convention gives exactly
\(0<W\leq3/4\) and \(Q\in\{0,1\}\).  Since \(q+1>\mu\), all samples
after \(q\) equal ball samples strictly below \(W\), so their counts are
zero.  This justifies treating \(Q\) as the only possible discrete term.

For \(Q=0\), the discrete tail is empty.  The outer tangent triangle gives

\[
 D_A(q)\geq\frac{W^2}{c}.
\]

Using \(f\geq2\), and minimizing the resulting convex quadratic at
\(W=\gamma/2\), gives

\[
 c\mathcal S>
 \frac{129}{625}-\frac{219}{100}c+\frac34c^2.
\]

For \(Q=1\), strict bracketing gives \(A(q)>3/4\), hence

\[
 \frac34-c<W\leq\frac34,qquad
 \alpha>\frac{3/4-W}{c}.
\]

The inner continuous payment and the same outer tangent triangle give

\[
 cD_A(q)>\frac32W-W^2-c.
\]

The resulting expression is concave in \(W\), so its minimum is controlled
by the two endpoint values

\[
 L_+(c)=\frac{273}{400}-\frac52c+c^2,qquad
 L_-(c)=\frac{273}{400}-\frac{119}{50}c-c^2.
\]

The lower endpoint is open, but evaluating it is a safe lower-infimum
bound.  The walls \(W=3/4\) and \(A(q)=3/4\) are owned correctly: the
former lies in \(B_0=0\), while equality in the latter has \(Q=0\).

## 3. Enlarged small-\(\delta\) certificate

For \(0<\delta<1\), strict bracketing fixes

\[
 B_0=f-1,qquad W>f-\frac54,qquad
 y=f-W\in\left(\frac14,\frac54\right).
\]

At fixed ratio, the shell increment
\(E_K(t)=K E_1(t/K)\) is nondecreasing in \(K\) at fixed \(t\), because
\(E_1\) is concave and vanishes at zero.  Thus the largest level distance
at fixed \(y\) occurs at \(f=2\), \(W=2-y\).  Writing
\(x=y/W\) gives \(x\in[1/7,5/3]\).

For this reduced scale, the exact normalized increment

\[
 \mathcal F_\rho(x)=
 \frac{e_\rho(3xg_\rho/c)}{g_\rho}-x
\]

is concave in \(x\).  The displayed formula for \(e_\rho''\) is correct:
its sign reduces to \(\rho^2(1-b^2)\leq1-\rho^2b^2\).  Endpoint
certification therefore fills the whole \(x\)-interval.

At \(\rho=477/500\), directed evaluation proves

\[
 \theta^2<\frac{93}{1000},\qquad c<\frac{97}{1000}.
\]

The inequalities

\[
 \Phi<\frac{\theta^3}{3},\qquad
 \Phi>\frac{\rho\theta^3}{3},\qquad
 1-\rho<\frac{\theta^2}{2}
\]

give \(u_0<1/6\) and \(u_0/(1-\rho)>2x\), with the strict directions used
in the note.

I checked the arccos series coefficients independently.  They decrease,
and on \(z\leq23/150\),

\[
 \sum_{j\geq2}a_jz^j
 \leq\frac{3z^2/160}{1-23/150}
 =\frac{45}{2032}z^2.
\]

Integration gives exactly \(45/7112\).  The first, positively truncated
copy has argument at most \(299/1500<1\), so it remains inside its
convergence domain.  Term-by-term integration reproduces every term of
\(\mathcal I_\rho(V)\) in the note.

For the coefficient

\[
 C_\rho=\frac{\rho\sqrt2(1-\rho)^{3/2}}{\Phi},
\]

the Taylor quotient has logarithmic-derivative numerator proportional to

\[
 -84-10t+\frac{t^2}{2},
\]

so it is decreasing throughout \(0\leq t\leq93/1000\).  Directed endpoint
evaluation proves \(C_\rho>7/5\).

The verifier covers every
\(\rho\in[477/500,99/100]\) by 32 closed rational Arb panels.  On each
entire panel it checks both \(x\)-endpoints, both positivity of the retained
integral and positivity of \((7/5)\mathcal I_\rho(2x)-x\).  This is interval
coverage, not point sampling.  Concavity then proves

\[
 T<\frac{3y}{c}
\]

and in particular proves that level \(f\) is present.

The chord prefix becomes

\[
 cP>-c-\frac3{16}-\frac{cd}{2}.
\]

The first drop gives \(Q\leq f-1\), while \(B\geq f-1\); every retained
angle is strictly smaller than \(\pi c\).  The exact-angle reserve yields

\[
 cD_A(q)>\frac12-\frac75c,
\]

and therefore

\[
 c\mathcal S>\frac5{16}-\frac{29}{10}c+c^2.
\]

## 4. Exact ledgers and independent replay

I recomputed the five endpoint ledgers independently in exact rational
arithmetic.  At \(\bar c=97/1000\) they are

\[
\begin{array}{c|c}
 \delta\geq1,\ B_0\geq1&251109/1000000\\
 \delta\geq1,\ B_0=Q=0&4107/4000000\\
 \delta\geq1,\ B_0=0,\ Q=1,\ W=3/4&449409/1000000\\
 \delta\geq1,\ B_0=0,\ Q=1,\ W=3/4-c&442231/1000000\\
 0<\delta<1&40609/1000000
\end{array}
\]

All five polynomials are decreasing on the certified \(c\)-interval.  The
smallest margin is the correctly identified \(Q=0\) value
\(4107/4000000\).

I independently replayed the frozen verifier with python-flint 0.8.0 at
384 and 1024 bits.  Both runs returned exit code zero and identical exact
ledgers.  At both precisions the smallest directed level-distance margin
was

\[
 0.0607609473485\ldots>0,
\]

and the smallest retained-integral lower bound was

\[
 0.203147928332\ldots>0.
\]

The interval constructors explicitly verify containment of every rational
panel endpoint.  I found no gap or overlap issue relevant to coverage, and
all transcendental comparisons are made with directed Arb balls.

## 5. Fixed-ratio cutoff and integer ranges

For \(\rho<477/500\), monotonicity gives
\(1/338<\eta_\rho<1/9\).  Exact rational recomputation gives

\[
 a_\rho<\frac{338670}{2599},\qquad
 \frac{338670}{2599}+\frac{13}{45}
 =\frac{15273937}{116955}<131.
\]

Because \(C_*>1/2\), squaring shows

\[
 \sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}
 <a_\rho+2\eta_\rho C_*.
\]

Substitution in the imported fixed-ratio threshold gives

\[
 K_0(\rho)<131\cdot338^2=14\,965\,964.
\]

Negativity excludes \(p=0\).  The strict inequalities and integrality then
give exactly

\[
 2r\leq29\,931\,927,\qquad
 n\leq14\,965\,963,
\]

\[
 f,B\leq4\,988\,654.
\]

The last bound uses
\(K/3+1/4<4\,988\,654+11/12\).  The lower ratio bound follows from
\(r<\mu\), \(r\geq1/2\), and \(K<14\,965\,964\).  The conditions
\(K-\mu>7\pi/4\), \(K>21/4\), \(Q\leq f-1\), and \(Q\leq B\) have the
same correct strict directions as in Round 8A.

## 6. Dependency and scope audit

The proof uses four previously audited inputs: the first-shelf
endpoint-chord identity and shell-increment elasticity, the exact-angle
terminal reserve with the one-interface cap bound, the Round-07 theorem on
\(\rho>99/100\), and the fixed-ratio threshold theorem.  I rechecked that
all their hypotheses hold here.  The Round-08B interval includes
\(\rho=99/100\), while Round 07 owns the open interval above it, so there
is no endpoint gap.

No proof-direction, strict-wall ownership, face-coverage, interval-coverage,
cutoff-arithmetic, or implementation defect was found.

**Final audit verdict: PASS.**
