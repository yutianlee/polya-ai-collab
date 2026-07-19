# Independent audit of General-d Round 8F: signed prefix beyond the chord barrier

Date: 2026-07-18  
Audited proof note: `human/outbox/general-d-round-08f-signed-prefix-terminal.md`  
Audited verifier: `scripts/general_d_high_floor_signed_prefix_verify.py`  
Scope: the high-floor first-drop ratio certificate only

## Verdict

**FINAL PASS.**  I independently reconstructed the analytic inequalities,
read the verifier line by line, and replayed the directed certificate at
384, 512, 768, and 1024 Arb bits.  The theorem

\[
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0
 \qquad\left(\frac{1847}{2000}\leq\rho<1\right)
\]

is supported in the stated high-floor first-drop branch.  This audit does
**not** certify any residual fixed-ratio wall with
\(\rho<1847/2000\).

## 1. Frozen inputs and dependency chain

The two target files were hash-checked before the audit, were not edited,
and were hash-checked again after all analytic and computational work:

| artifact | SHA256 before and after |
|---|---|
| `human/outbox/general-d-round-08f-signed-prefix-terminal.md` | `ABAFE9A9C0B57607CA0945313D0C0A7B1602D6067D84587F14C274898EF7D196` |
| `scripts/general_d_high_floor_signed_prefix_verify.py` | `066A64BE535AFE212B107928D7845E9BC27D210D144A9E99FDE16DCCDF5A866C` |

The verifier pins the Round 8E verifier to

`3360878C89DB842FD8695C74C211A3562DBFC84C3E1B4D3CA291DC36BCED39C5`,

and the on-disk file has that hash.  Its next inherited hashes also agree:
Round 8D is
`8E025183DC6F2AFCE4E51F404F5AC7830185FCA1B22B2DF0184D1204E4D91BF6`
and the Round 8C helper is
`267900ED39C17C02D1BBDEB17B5F36AB616601DEE8127D98E50A9646BCEDCAB5`.

## 2. Removing \(p=0\) and checking the refined cap

If \(p=0\), then \(R_0=0\).  The completed one-interface theorem gives
\(D_A(q)\geq0\), while \(d_\rho>0\) on this ratio band and \(n>0\).
Consequently

\[
 D_A(q)+\frac{d_\rho n}{2}>0.
\]

A negative candidate therefore has \(p\geq1\).  Since \(p<n\), it has
\(n\geq2\); because \(r\geq1/2\),
\(q=r+n\geq5/2\).

For \(q<\mu<q+1\), strict convexity of \(G_\mu\) and
\(G_\mu(\mu)=0\) put the graph strictly below its endpoint chord:

\[
 2\int_q^\mu G_\mu(z)\,dz
 <G_\mu(q)(\mu-q)<G_{q+1}(q).
\]

The case \(q=\mu\) is zero.  Writing
\(q/(q+1)=\cos\vartheta\) gives
\(\frac d{dq}G_{q+1}(q)=(\sin\vartheta-\vartheta)/\pi<0\), so the
largest endpoint is \(q=5/2\).  My independent 768-bit evaluation gave

\[
 \frac16-G_{7/2}(5/2)>0.0038491515051152111790.
\]

Thus the strict cap \(2\int_q^\mu G_\mu<1/6\) is valid, including its
wall phases.

## 3. Common prefix and the sign switch

Put

\[
 c=\frac{\arccos\rho}{\pi},\quad d=1-2c,\quad
 \beta=\frac{123}{1000}-c,\quad
 P=R_p+\frac d2(n-p).
\]

On the absent-level face, the audited Round 8E chord gives strictly

\[
 P>\left(\frac d2-\frac{377}{1000}\right)M-\frac d2
   =\beta M-\frac d2.
\]

On the present-level face, the elasticity bound gives

\[
 P\geq\left(\frac18-c\right)M-\frac d2
    >\beta M-\frac d2,
\]

because \((1/8-c)-\beta=1/500\) and \(M>0\).  Hence the strict common
pre-substitution inequality is valid on both faces.

If \(\beta\geq0\), then \(M\geq\delta/c\) has the favorable direction:

\[
 cP>\beta\delta-\frac{cd}{2}.
\]

If \(\beta<0\), the inequality reverses when the upper bound
\(M\leq\mu\) is inserted.  With
\(R_\rho=c\mu/W\),

\[
 cP>\beta c\mu-\frac{cd}{2}=\beta R_\rho W-\frac{cd}{2}.
\]

On \(1847/2000\leq\rho\leq927/1000\), directed endpoint bounds give
\(\theta=\arccos\rho<2/5\), while \(\epsilon=1-\rho\geq73/1000\).
The active-width estimate

\[
 \lambda_\rho>\frac{2\sqrt2}{3}\sqrt\epsilon
\]

and the exact gap

\[
 \frac89\frac{73}{1000}-\left(\frac14\right)^2
 =\frac{43}{18000}>0
\]

give \(\lambda_\rho>1/4\).  Since
\(W>\lambda_\rho(W+\delta)\) and
\(W+\delta=f-1/4\geq7/4\), this proves the strict bound

\[
 W>\frac7{16}.
\]

Moreover

\[
 R_\rho=\frac{\theta\rho}{\lambda_\rho\epsilon}
 <\frac{(2/5)(927/1000)}{(1/4)(73/1000)}
 =\frac{7416}{365}<21.
\]

Because \(\beta<0\), multiplying the last strict inequality by
\(\beta W\) reverses it, and therefore

\[
 cP>21\beta W-\frac{cd}{2}.
\]

The two sign directions in the proof note are consequently correct.
Independent endpoint evaluation also gave

\[
 (\arccos(1847/2000))^2<0.154991551249596<\frac{311}{2000},
\]

\[
 c(1847/2000)<0.125315312022<\frac{627}{5000},
\]

with respective lower gaps \(0.000508448750404\) and
\(0.0000846879780004\).

## 4. Exhaustion of every \(\delta\geq1\) terminal stratum

The strict counts satisfy \(B\geq B_0\) and \(Q\leq B_0+1\).  Thus the
three cases \(B_0\geq1\), \(B_0=Q=0\), and
\(B_0=0,Q=1\) are exhaustive.  I checked the reserve used in each case:

\[
\begin{array}{ll}
B_0\geq1:&cD_A(q)>B_0(1/2-c)-7c/6,\\
B_0=Q=0:&cD_A(q)\geq W^2,\\
B_0=0,Q=1:&cD_A(q)>3W/2-W^2-c.
\end{array}
\]

For \(\beta\geq0\), \(\delta\geq1\) is used on the first face and
\(\delta\geq7/4-W\) on the two \(B_0=0\) faces.  All expressions
decrease up to \(c=123/1000\).  The \(Q=0\) expression increases in
\(W\geq7/16\), and the \(Q=1\) expression is concave in
\(W\in[3/4-c,3/4]\).  The four resulting strict lower ledgers are

\[
 \frac{187129}{1000000},\quad
 \frac{580141}{4000000},\quad
 \frac{393129}{1000000},\quad
 \frac{189}{500}.
\]

For clarity, the first ledger is
\(623/1000-(11/3)c+c^2\), whose derivative is negative, and the two
\(Q=1\) endpoint polynomials are

\[
 \frac{1371}{2000}-\frac52c+c^2,qquad
 \frac{1371}{2000}-\frac{2377}{1000}c-c^2;
\]

both decrease throughout the relevant interval.

For \(\beta<0\), strict bracketing on \(B_0\geq1\) gives
\(W\leq B_0+3/4\).  Since \(21\beta<0\), this yields a lower bound, not
an upper bound.  The resulting coefficient of \(B_0\) is

\[
 \frac12-c+21\beta\geq\frac{1621}{5000}>0,
\]

so \(B_0=1\) is the correct endpoint.  Its ledger
\(20081/4000-(473/12)c+c^2\) decreases in \(c\).  On \(Q=0\),

\[
 \partial_W\bigl(W^2+21\beta W-cd/2\bigr)
 \geq 2\frac7{16}+21\left(-\frac3{1250}\right)
 =\frac{4123}{5000}>0,
\]

and the endpoint expression decreases in \(c\).  On \(Q=1\), the
ledger is concave in \(W\); its two endpoint polynomials are

\[
 \frac{9999}{4000}-\frac{69}{4}c+c^2,qquad
 \frac{9999}{4000}-\frac{19833}{1000}c+21c^2.
\]

Their derivatives are negative for
\(123/1000<c\leq627/5000\).  At the latter endpoint the four lower
ledgers are

\[
 \frac{2328129}{25000000},\quad
 \frac{12238141}{100000000},\quad
 \frac{8808129}{25000000},\quad
 \frac{2143251}{6250000}.
\]

All are positive.  This checks the count walls, the moving
\(W=3/4-c\) endpoint, every monotonicity direction, and both concavity
endpoints; no \(\delta\geq1\) stratum is omitted.

## 5. The improved level distance for \(0<\delta<1\)

Let \(y=f-W=\delta+1/4\) and \(L=149/50\).  At fixed \(t\),
\(E_K(t)=K E_1(t/K)\) increases with \(K\), by concavity of \(E_1\) and
\(E_1(0)=0\).  Therefore the worst scale at fixed \(y\) is the smallest
allowed \(W=f-y\), namely \(f=2\), \(W=2-y\).  Then

\[
 x=\frac yW\in\left[\frac17,\frac53\right].
\]

For fixed \(\rho\), the normalized increment
\(e_\rho(Lxg_\rho/c)/g_\rho-x\) is concave in \(x\).  It is therefore
enough to check these two endpoint values.

With \(\Phi=\sin\theta-\theta\cos\theta\),
\(t_0=Ly/c\), and \(u_0=t_0/\mu\),

\[
 u_0=\frac{Lx\Phi}{\theta\rho}
 <\frac{149}{50}\frac59\frac{311/2000}{1847/2000}
 =\frac{46339}{166230}<\frac{279}{1000}<1.
\]

Thus both arccos arguments stay ordered and the exact increment
integrand is positive.

For the retained range, alternating Taylor bounds give

\[
 \Phi>\theta^3\left(\frac13-\frac{\theta^2}{30}\right),\qquad
 1-\cos\theta<\theta^2\left(\frac12-\frac{\theta^2}{24}
 +\frac{\theta^4}{720}\right).
\]

Since \(\rho\leq927/1000\), the resulting lower quotient is decreasing
in \(t=\theta^2\): its derivative has the sign of
\(t^2-20t-60<0\).  At \(t=311/2000\),

\[
 \frac{105008000000}{146407982263}-\frac7{10}
 =\frac{25224124159}{1464079822630}>0.
\]

Hence

\[
 \kappa_\rho=\frac{\Phi}{\theta\rho(1-\rho)}>\frac7{10},
 \qquad
 \frac{u_0}{1-\rho}>\frac{1043}{500}x.
\]

The coefficient estimate uses

\[
 C_\rho>
 \rho\sqrt2\,
 \frac{(1/2-t/24)^{3/2}}{1/3-t/30+t^2/840}.
\]

The quotient is decreasing because the inherited logarithmic-derivative
test reduces to \(84+10t-t^2/2>0\), and \(\rho\geq1847/2000\).
At \(t=311/2000\), my independent 768-bit lower value was

\[
 1.3797475428012373588>\frac{689}{500},
\]

with lower margin \(0.0017475428012373588\).

Retain \(0\leq v\leq V=(1043/500)x\).  Then

\[
 V\leq\frac{1043}{300},\qquad
 (1-\rho)V\leq\frac{53193}{200000},
\]

and the positive-copy argument is at most
\(68493/200000<1\).  The arccos-series coefficients are positive and
decrease, so

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \leq S(z)\leq
 1+\frac z{12}+\frac{3750z^2}{146807}.
\]

The upper coefficient is exactly
\((3/160)/(1-53193/200000)\), and integration gives
\((3750/146807)(2/7)=7500/1027649\).  Term-by-term integration produces
exactly the six-term expression implemented in
`series_integral_lower`; every half-power has a positive interval
argument.

The inherited `interval_ball` constructor contains both rational panel
endpoints.  The verifier loops over exactly the two values
\(x=1/7,5/3\) and all 64 panels, with no skipped branch.  It first checks
the retained integral is positive, which makes replacement of
\(C_\rho\) by \(689/500\) direction-safe, and then checks

\[
 \frac{689}{500}\mathcal I^{\mathrm F}_\rho(V)-x>0.
\]

Concavity fills the entire \(x\)-interval.  Therefore
\(E_K(Ly/c)>y\), level \(f\) is present, and

\[
 T<\frac{149}{50}\frac yc.
\]

## 6. Completing the small-\(\delta\) ledger

The endpoint chord, the now-proved level presence, and
\(M\geq\delta/c\) give

\[
 cP>
 \left(\frac{3-L}{4}-c\right)\delta
 -\frac L{16}-\frac{cd}{2}.
\]

Here \((3-L)/4-c<0\), so \(0<\delta<1\) gives the strict lower endpoint
at \(\delta=1\).  Also \(B_0=f-1\), \(Q\leq f-1\), and the refined cap
gives

\[
 cD_A(q)>\frac{f-1}{2}-c(f-1)-\frac c6
 \geq\frac12-\frac{7c}{6}.
\]

Adding and using \(d=1-2c\) yields

\[
 c\mathcal S>rac54-\frac{5L}{16}-\frac83c+c^2
 =\frac{51}{160}-\frac83c+c^2.
\]

Its derivative is negative on the certified interval, and at
\(c=627/5000\) it is exactly

\[
 \frac{1879}{25000000}>0.
\]

The strict directions at \(\delta=1\) and at the directed upper bound on
\(c\) are safe.

## 7. Residual cutoff and integer ranges

For \(\rho<1847/2000\), monotonicity of the ball action gives

\[
 \frac1{158}<\eta_\rho<\frac19.
\]

Independent 768-bit endpoint margins were

\[
 G_1(1847/2000)-\frac1{158}>0.0000453657359011,
\]

\[
 \frac19-G_1(1/2)>0.00211333006688.
\]

Also

\[
 a_\rho<2\frac{355}{113}\frac{1847}{153}
 =\frac{1311370}{17289},
\]

and, using \(C_*<13/10\),

\[
 a_\rho+2\eta_\rho C_*
 <\frac{2193941}{28815}<77.
\]

Because \(C_*>1/2\),

\[
 (a_\rho+2\eta_\rho C_*)^2
 -(a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2)
 =\eta_\rho^2(4C_*^2-1)>0.
\]

Thus the square root in \(K_0\) is strictly smaller than the other
numerator term and

\[
 K_0(\rho)<77\cdot158^2=1\,922\,228.
\]

Since \(2r\) and \(n\) are integers, \(r<\mu<K<1\,922\,228\) gives

\[
 \rho>\frac1{3\,844\,456},\qquad
 2r\leq3\,844\,455,qquad
 n\leq1\,922\,227.
\]

The first-shelf condition gives \(A(r)\geq7/4\), hence
\(K-\mu>7\pi/4\) and \(K>21/4\).  Finally

\[
 f,B<\frac K3+\frac14
 <640\,742+\frac{11}{12},
\]

so the integer bounds are \(f,B\leq640\,742\), with
\(0\leq Q\leq f-1\) and \(Q\leq B\).  These are exactly the ranges in
the proof note.

## 8. Verifier inspection and four-precision replay

I inspected every executable line.  In particular:

- the prior source hash is checked before import;
- Arb precision is read from `GENERAL_D_ARB_PREC` before any Round 8F
  transcendental constants are created;
- all scalar ledger arithmetic is exact `fmpq` arithmetic;
- the inherited interval constructor explicitly checks containment of
  both rational endpoints;
- all half-powers occur on positive interval balls;
- the panel loops are `endpoint in (1/7,5/3)` and
  `panel in range(64)`, exactly 128 full-panel checks;
- both the integral lower bound and the final margin are tested by their
  directed lower endpoints;
- the cutoff and every integer endpoint are checked exactly; and
- the final message explicitly disclaims the residual ratio walls.

The replay command was

```powershell
$python='C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\python.exe'
foreach($bits in 384,512,768,1024){
  $env:GENERAL_D_ARB_PREC=[string]$bits
  & $python scripts/general_d_high_floor_signed_prefix_verify.py
  if($LASTEXITCODE -ne 0){ throw "failed at $bits bits" }
}
```

I also replayed through redirected process streams to measure stderr
separately.  The results were:

| Arb bits | exit | stderr characters | minimum \(\mathcal I^{\mathrm F}\) lower bound | minimum final lower margin |
|---:|---:|---:|---:|---:|
| 384 | 0 | 0 | 0.211376406594 | 0.0357944486166 |
| 512 | 0 | 0 | 0.211376406594 | 0.0357944486166 |
| 768 | 0 | 0 | 0.211376406594 | 0.0357944486166 |
| 1024 | 0 | 0 | 0.211376406594 | 0.0357944486166 |

Each run reported `python-flint=0.8.0`, the requested actual Arb
precision, the pinned Round 8E hash, and all PASS lines.

## 9. Scope boundary

This audit proves only the signed-prefix ratio exclusion on
\(1847/2000\leq\rho<1\) and the consequent finite residual bounds.  It
does not turn the residual box into a proof by finiteness, and it does not
certify any remaining wall with

\[
 \frac1{3\,844\,456}<\rho<\frac{1847}{2000},\qquad
 \frac{21}{4}<K<1\,922\,228.
\]

Those residual walls remain a separate obligation.
