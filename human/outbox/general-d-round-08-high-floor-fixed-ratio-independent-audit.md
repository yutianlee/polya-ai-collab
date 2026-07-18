# Independent audit: Round 8A high-floor fixed-ratio band

Date: 18 July 2026  
Status: **FINAL PASS**

Audited artifacts:

- `human/outbox/general-d-round-08-high-floor-fixed-ratio.md`  
  SHA-256 `9CCBB8A71C783E0EEABC29ED9F32183A1C80B474ECF2E51D6FC98D215162E159`;
- `scripts/general_d_high_floor_fixed_ratio_verify.py`  
  SHA-256 `DE583B05BB4744CFFC68BB5CD1BB43819205098A05AF6D34AE136FB291284CC9`.

The audited conclusion is exactly

\[
 f\ge2,\quad p<n,\quad \rho\ge\frac{603}{625}
 \quad\Longrightarrow\quad
 \mathcal S=D_A(q)+R_p+\frac{d_\rho}{2}(n-p)>0.
\]

Together with the fixed-ratio high-energy theorem, this leaves only

\[
 \frac1{87\,889\,536}<\rho<\frac{603}{625},\qquad
 \frac{21}{4}<K<43\,944\,768
\]

in the high-floor first-drop branch. This is a finite reduction, not a
certificate of the remaining walls.

## 1. Endpoint-chord ledger

I rederived the wall-safe chord inequality

\[
 P\ge-\left(\frac14+\zeta\right)(T-M)+\frac d2(M-1),
 \qquad M\ge\frac\delta c,
\]

with ordinary floors on the first shelf and strict terminal brackets.
For \(\delta\ge1\), the present-level elasticity bound gives
\(T/M\le5/2\), hence

\[
 P\ge \frac1{8c}-\frac32+c.
\]

On the absent-level face the degree-32 Bernstein inequality gives

\[
 P>\frac3{25c}-\frac32+c.
\]

The verifier independently reconstructs the Bernstein coefficients and
finds their exact minimum \(309/396800\). Directed evaluation at
\(\rho=603/625\) gives \(c<339/4000\), and exact rational arithmetic then
gives the positive margins

\[
 \frac{80921}{1356000},\qquad \frac{307}{452000}.
\]

The second, much smaller number is correctly identified as the limiting
ledger.

## 2. Level-distance certificate

For \(0<\delta<1\), the scale reduction to
\(f=2\), \(W=2-y\), and \(x=y/W\in[1/7,5/3]\) is valid because the shell
increment is concave and increases with the scale at fixed distance.
The exact normalized target is concave in \(x\), so it is sufficient to
certify the two endpoints.

The noncancelling identity uses

\[
 \arccos(1-z)=\sqrt{2z}\,S(z),\qquad
 S(z)=\sum_{j\ge0}\frac{\binom{2j}{j}}{8^j(2j+1)}z^j.
\]

All coefficients are positive. Since their ratio is less than one, on
\(0\le z\le1/8\)

\[
 1+\frac z{12}+\frac{3z^2}{160}
 \le S(z)
 \le1+\frac z{12}+\frac{3z^2}{140}.
\]

The upper coefficient is in the correct direction: the tail beginning
with \(3z^2/160\) is at most
\((3/160)z^2/(1-z)\le(3/140)z^2\). The retained range satisfies
\(z\le44/375<1/8\). The resulting integrated lower enclosure in the
verifier matches equation (33) of the proof note term by term, including
the subtracted \(3\epsilon^2V^{7/2}/490\) term.

The coefficient lower bound \(C_\rho>36/25\) follows from alternating
Taylor bounds and the decreasing rational-algebraic function displayed
in the note. The strict estimate \(u_0/\epsilon>2x\) follows from
\(\Phi>\rho\theta^3/3\) and \(\epsilon<\theta^2/2\), so retaining
\(0\le v\le2x\) loses only a positive contribution.

The code covers every \(\rho\in[603/625,99/100]\) by 16 rational Arb
intervals, rather than point samples. On each interval it evaluates both
endpoint values of \(x\) with directed rounding. Concavity then fills the
entire \(x\)-interval. Round 7 owns \(\rho>99/100\).

Combining the certified distance with the exact terminal-angle reserve
gives

\[
 c\mathcal S>rac5{16}-\frac{29}{10}c+c^2
 \ge\frac{1182521}{16000000}>0.
\]

## 3. Residual cutoff and integer labels

For \(\rho<603/625\), monotonicity gives
\(1/504<\eta_\rho<1/9\). The rational bounds
\(\pi<355/113\), \(C_*<13/10\), and

\[
 a_\rho+2\eta_\rho C_*<173
\]

are checked in the verifier. Since \(C_*>1/2\),

\[
 \sqrt{a_\rho^2+4a_\rho\eta_\rho C_*+\eta_\rho^2}
 <a_\rho+2\eta_\rho C_*,
\]

and therefore \(K_0(\rho)<173\cdot504^2=43\,944\,768\).
The stated integer ranges follow from strict inequalities:

\[
 2r\le87\,889\,535,\quad n\le43\,944\,767,
 \quad f,B\le14\,648\,256.
\]

## 4. Independent replay

I replayed the frozen verifier independently with python-flint 0.8.0 at
384, 768, and 1024 bits. All three executions returned exit code zero and
the same exact rational ledger. The directed level-distance lower margin
was

\[
 0.122748159345\ldots>0,
\]

and the smallest retained-integral lower bound was
\(0.202999800557\ldots\) (the final printed digit varies outwardly at the
lowest precision only). The cutoff and all integer-label checks were
identical.

No proof-direction, endpoint-ownership, interval-coverage, or
implementation defect was found. The note correctly states that the
remaining \(\rho<603/625\) walls are still open.
