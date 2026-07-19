# Independent audit: Round 8D sharp terminal cap

Date: 18 July 2026  
Status: **FINAL PASS**

Audited frozen artifacts:

- `human/outbox/general-d-round-08d-sharp-cap-terminal.md`  
  SHA-256 `C29F8ADF77E6EFE5B21BE0B39CD26D8D63B2881023EE72B5E8C0DB37AB81E30E`;
- `scripts/general_d_high_floor_sharp_cap_verify.py`  
  SHA-256 `8E025183DC6F2AFCE4E51F404F5AC7830185FCA1B22B2DF0184D1204E4D91BF6`.

The verifier imports the frozen Round 8C helper only after checking its
SHA-256 hash

`267900ED39C17C02D1BBDEB17B5F36AB616601DEE8127D98E50A9646BCEDCAB5`.

None of those three frozen files was edited during this audit.

The audited conclusion is

\[
 f\geq2,\qquad p<n,\qquad \frac{93}{100}\leq\rho<1
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Round 8D proves the full closed band
\(93/100\leq\rho\leq477/500\); the already audited Round 8B theorem
owns \(\rho\geq477/500\).  The shared endpoint is covered twice, so
there is no endpoint gap and no need to splice the Round 8C ratio theorem
into the final interval.  Round 8D still uses Round 8C's independently
audited active-width lemma.  The result is a ratio exclusion and compact
reduction, not a certification of the remaining fixed-ratio walls.

## 1. Sharp cap and phase ownership

The cap lemma does not require a prior negativity assumption.  Since
\(p<n\) with \(p,n\) integral, \(n\geq1\).  Since
\(r\in\tfrac12\mathbb N\),

\[
 q=r+n\geq\frac32,
\]

including the face \(p=0\).

If \(q=\mu\), the cap is exactly zero.  Suppose \(q<\mu\).  Strict
convexity of \(G_\mu\), together with
\(G_\mu(\mu)=0\), places its graph strictly below the endpoint chord and
gives

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_\mu(q)(\mu-q).
\]

Here \(0<\mu-q<1\).  Also \(R\mapsto G_R(q)\) is strictly increasing
for \(R>q\), since

\[
 \frac{\partial}{\partial R}G_R(q)
 =\frac{\sqrt{R^2-q^2}}{\pi R}>0.
\]

Consequently

\[
 2\int_q^\mu G_\mu(z)\,dz<G_{q+1}(q).
\]

For \(H(q)=G_{q+1}(q)\), set
\(\cos\theta=q/(q+1)\).  Direct differentiation gives

\[
 H'(q)=\frac{\sin\theta-\theta}{\pi}<0.
\]

Thus \(q\geq3/2\) implies

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_{5/2}(3/2)<\frac15.
\]

The last comparison was independently replayed with directed Arb
arithmetic.  At 512 bits,

\[
 G_{5/2}(3/2)=0.1938689194162815205\ldots,
\]

and the directed lower bound for \(1/5-G_{5/2}(3/2)\) is

\[
 0.00613108058371847945\ldots>0.
\]

This proves the cap on the equality phase \(q=\mu\), on the endpoint
\(q=3/2\), and throughout the open phase \(q<\mu<q+1\), without a
continuity argument.

For the later residual-range conversion, the statement that a negative
candidate has \(p\geq1\) is also direct: if \(p=0\), then \(R_0=0\),
\(d_\rho>0\), \(n\geq1\), and the one-interface theorem gives
\(D_A(q)\geq0\).  Hence

\[
 \mathcal S=D_A(q)+\frac{d_\rho n}{2}>0.
\]

Thus negativity forces \(p\geq1\) and \(n\geq2\), exactly as used in
the cutoff section.

## 2. Ratio endpoint, active width, and the common prefix

At \(\rho=93/100\), independent directed evaluation gives

\[
 (\arccos\rho)^2<\frac{71}{500},\qquad
 \frac{\arccos\rho}{\pi}<\frac{1199}{10000}.
\]

The directed gaps at 512 bits are respectively

\[
 0.0003354742383803494\ldots,
 \qquad
 0.0000934165819851335\ldots.
\]

Both left sides decrease as \(\rho\) increases.  Therefore these bounds
hold on the complete Round 8D band.  In particular

\[
 \gamma=\frac3{25}-c>0,
\]

with the rational endpoint gap
\(3/25-1199/10000=1/10000\).

The Round 8C active-width proof applies unchanged.  The present band
satisfies \(\rho\leq477/500\), so \(1-\rho\geq23/500\).  It gives
\(\lambda_\rho>1/5\), and the strict active inequality then gives

\[
 W>\frac74\lambda_\rho>\frac7{20}.
\]

The present-level prefix coefficient exceeds \(3/25\) by
\(1/200\).  The absent-level degree-32 Bernstein reconstruction has
exact smallest coefficient

\[
 \frac{309}{396800}>0.
\]

Thus both level faces retain the strict common bound

\[
 cP>\left(\frac3{25}-c\right)\delta-\frac{cd}{2}
\]

for \(\delta\geq1\).

## 3. Every \(\delta\geq1\) strict wall

The strict counts

\[
 B_0=[W+1/4]_<,\qquad B=[G_K(q)+1/4]_<,
 \qquad Q=[A(q)+1/4]_<
\]

satisfy \(B\geq B_0\) and \(Q\leq B_0+1\).  Hence the partition into

- \(B_0\geq1\);
- \(B_0=0,Q=0\);
- \(B_0=0,Q=1\)

is exhaustive.  The strict convention assigns \(W=3/4\) to
\(B_0=0\), assigns \(A(q)=3/4\) to \(Q=0\), and the split assigns
\(\delta=1\) to this ledger.

The four endpoint polynomials are decreasing for
\(0<c\leq1199/10000\).  On the zero-count face, the derivative with
respect to \(W\) is

\[
 2W-\left(\frac3{25}-c\right)
 >\frac7{10}-\frac3{25}>0,
\]

so using the unattained lower infimum \(W=7/20\) is conservative.  The
exact endpoint margins are

\[
\begin{array}{c|c}
 B_0\geq1&16676601/100000000\\
 B_0=Q=0&7706601/100000000\\
 B_0=0,Q=1,\ W=3/4&39712601/100000000\\
 B_0=0,Q=1,\ W=3/4-c&38276199/100000000
\end{array}
\]

and are all positive.  Open endpoints are used only as lower infima;
no equality wall is filled by continuity.

## 4. The retuned small-\(\delta\) certificate

For \(0<\delta<1\), strict bracketing gives

\[
 B_0=f-1,\qquad
 y=f-W=\delta+\frac14\in\left(\frac14,\frac54\right).
\]

The previously audited scale reduction takes the worst level distance
to \(f=2\), and the exact concavity reduction leaves

\[
 x=\frac yW\in\left\{\frac17,\frac53\right\}.
\]

With \(t_0=3y/c\) and \(u_0=t_0/\mu\),

\[
 u_0<\frac{71}{279}<\frac{51}{200}<1.
\]

Moreover \(u_0/(1-\rho)>2x\) follows strictly from
\(\Phi>\rho\theta^3/3\) and
\(1-\rho<\theta^2/2\).  Hence retaining \(0\leq v\leq2x\) remains
valid.

On the subtracted series copy,

\[
 z\leq\frac7{30},\qquad
 \frac{3/160}{1-7/30}=\frac9{368},
\]

and termwise integration gives \(9/1288\).  The positive first copy is
used only for

\[
 z\leq\frac{91}{300}<1.
\]

Thus both copies remain strictly inside the power-series domain.  The
Taylor quotient controlling

\[
 C_\rho=\frac{\rho\sqrt2(1-\rho)^{3/2}}
 {\sin\theta-\theta\cos\theta}
\]

is decreasing over \(0\leq\theta^2\leq71/500\), because
\(84+10t-t^2/2>0\) there.  Directed endpoint evaluation gives

\[
 C_\rho>\frac{1389}{1000};
\]

the directed endpoint margin is
\(0.0009493314436526601\ldots\).

The verifier covers \([93/100,477/500]\) by 64 closed rational panels.
Its interval constructor checks that both rational endpoints lie in each
Arb ball.  At both \(x\)-endpoints and on every full panel it separately
certifies

\[
 \mathcal I_\rho^{\mathrm D}(2x)>0,
 \qquad
 \frac{1389}{1000}\mathcal I_\rho^{\mathrm D}(2x)-x>0.
\]

Separate positivity of the retained integral is required before replacing
\(C_\rho\) by its rational lower bound, and the implementation checks it.
The exact concavity argument then fills the entire \(x\)-interval.

The smallest directed lower bounds in independent runs at 384, 512, 768,
and 1024 bits were stable at

\[
 \mathcal I_\rho^{\mathrm D}(2x)>0.203714892723\ldots,
\]

\[
 \frac{1389}{1000}\mathcal I_\rho^{\mathrm D}(2x)-x
 >0.0162868443031\ldots.
\]

This proves \(T<3y/c\).  The endpoint-chord calculation gives

\[
 cP>-c-\frac3{16}-\frac{cd}{2}.
\]

The first \(f-1\) retained ball levels lie strictly below \(W\), so
their angles are strictly smaller than \(\pi c\).  Also \(Q\leq f-1\).
The exact-angle reserve and the cap from Section 1 therefore give

\[
 cD_A(q)>
 \frac{f-1}{2}-c(f-1)-\frac c5
 \geq\frac12-\frac65c.
\]

Adding the two estimates and using \(d=1-2c\) yields

\[
 c\mathcal S>rac5{16}-\frac{27}{10}c+c^2.
\]

This polynomial decreases throughout the certified \(c\)-range, and at
\(c=1199/10000\) it equals

\[
 \frac{314601}{100000000}>0.
\]

This is the smallest exact terminal margin in Round 8D.  The open
small-\(\delta\) face and the closed \(\delta=1\) face therefore meet
without a gap.

## 5. Residual cutoff and integer ranges

For \(0<\rho<93/100\), monotonicity of \(G_1\) and directed endpoint
evaluation give

\[
 \frac1{180}<\eta_\rho<\frac19.
\]

At the lower endpoint comparison,

\[
 G_1(93/100)=0.00557770607665256555\ldots,
\]

whose directed margin above \(1/180\) is
\(0.0000221505210970099955\ldots\).  Also

\[
 a_\rho<\frac{66030}{791},\qquad
 a_\rho+2\eta_\rho C_*
 <\frac{2981633}{35595}<84,
\]

with exact last gap \(8347/35595\).

Write \(X=a_\rho+2\eta_\rho C_*\).  Since \(C_*>1/2\),

\[
 X^2-
 \left(a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2\right)
 =\eta_\rho^2(4C_*^2-1)>0.
\]

The fixed-ratio threshold therefore satisfies

\[
 K_0(\rho)<\frac{X}{\eta_\rho^2}
 <84\cdot180^2=2\,721\,600.
\]

For a negative candidate, \(p\geq1\), hence \(n\geq2\), and
\(r<\mu<K\).  Strict inequalities and integrality give

\[
 \rho>\frac1{5\,443\,200},\qquad
 1\leq2r\leq5\,443\,199,
\]

\[
 2\leq n\leq2\,721\,599,
 \qquad 1\leq p\leq n-1.
\]

Finally \(A(r)\geq7/4\), strict decrease from \(A(0)\), and
\(\pi>3\) give

\[
 K-\mu>\frac{7\pi}{4},\qquad K>\frac{21}{4},
\]

\[
 2\leq f\leq907\,200,
 \qquad 0\leq Q\leq f-1,
 \qquad Q\leq B\leq907\,200.
\]

No real endpoint is lost when these strict bounds are converted to the
displayed integer ranges.

## 6. Verifier audit and replay

The verifier compiles with `python -m py_compile`.  It checks the frozen
Round 8C helper hash before import, reconstructs the exact Bernstein
minimum, certifies the sharp cap endpoint, checks every rational series
and terminal coefficient, encloses every full ratio panel, and verifies
the cutoff arithmetic.

I replayed the exact frozen verifier with python-flint 0.8.0 at 384, 512,
768, and 1024 bits.  All four runs returned exit code zero.  The reported
panel minima and all exact ledgers were identical across precisions.

As a separate coverage check, I reimplemented the retained-integral
formula directly and partitioned the same closed ratio band into 128
rational panels at 768 bits.  All 256 panel/endpoint tests passed; the
directed lower bounds were (0.2037788456147\ldots) for the integral and
(0.0181142470075\ldots) for the level-distance margin.

I found no phase-ownership, strict-wall, cap-direction, active-width,
series-domain, interval-coverage, endpoint, cutoff, integer-range, or
implementation defect.

**Final audit verdict: PASS.**
