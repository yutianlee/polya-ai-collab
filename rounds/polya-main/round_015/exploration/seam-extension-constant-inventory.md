# Round 15 seam-extension constant inventory

## Verdict and isolation

**PASS.** Independently reconstructing the frozen screen gives no failed
comparison. The local shifted-tail proof closes on

\[
0<\varepsilon\le\frac16,\qquad
\kappa=K\varepsilon^2\ge54,
\]

including both equality faces. Independently,

\[
K_0(5/6)<295^2=87025.
\]

Conditional on the separate proof and review gates, the seven-zone union
then gives the all-ratio high-frequency ceiling \(K\ge200000\).

The frozen packet has SHA-256

\[
\texttt{c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7}.
\]

This inventory used that packet and accepted pre-Round-15 inputs only. It
did not inspect either Round 15 proof artifact. Every finite calculation is
reproduced by the accompanying standard-library exact ledger. The ledger
does not enumerate Bessel roots and is not a spectral certificate.

## 1. Elementary bounds and the angular factor

Machin's identity and alternating arctangent truncations give

\[
\frac{333}{106}<\pi<\frac{1571}{500}<\frac{22}{7}.
\tag{1.1}
\]

For the upper bound, the five-term upper truncation at \(1/5\) and
two-term lower truncation at \(1/239\) give

\[
\pi<
\frac{5277328977275528}{1679825970703125},
\]

and

\[
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=
\frac{2736890694763}{6719303882812500}>0.
\tag{1.2}
\]

For the lower bound, the four-term lower truncation at \(1/5\) and
\(\arctan(1/239)<1/239\) give

\[
\pi>
\frac{1231847548}{392109375},
\]

and

\[
\frac{1231847548}{392109375}-\frac{333}{106}
=\frac{3418213}{41563593750}>0.
\tag{1.3}
\]

Positive squaring also gives

\[
\frac{140}{99}<\sqrt2<\frac{99}{70},
\qquad
\sqrt3<\frac{97}{56},
\tag{1.4}
\]

with exact reserves

\[
2-\left(\frac{140}{99}\right)^2=\frac2{9801},\quad
\left(\frac{99}{70}\right)^2-2=\frac1{4900},\quad
\left(\frac{97}{56}\right)^2-3=\frac1{3136}.
\]

To reconstruct the angular bound, first note

\[
2-\left(\frac75\right)^2=\frac1{25}>0,
\qquad
\left(\frac79\right)^2-\frac35=\frac2{405}>0.
\tag{1.5}
\]

Thus \(\sqrt2>7/5\), so
\(\sqrt{2-\sqrt2}<\sqrt{3/5}<7/9\). Since

\[
\cos^2\frac{3\pi}{16}
=\frac12+\frac14\sqrt{2-\sqrt2}
<\frac12+\frac7{36}
=\frac{25}{36},
\]

one has \(\cos(3\pi/16)<5/6\). Therefore, uniformly at and above
\(\rho=5/6\),

\[
c=\frac{\arccos\rho}{\pi}<\frac3{16},
\qquad
\boxed{d=1-2c>\frac58}.
\tag{1.6}
\]

The endpoint \(\rho=5/6\) is included because the cosine comparison is
strict.

## 2. Dangerous geometry, displacement, and localization

Put \(y=\sqrt\varepsilon\). On the target domain,

\[
0<y\le\frac1{\sqrt6},\qquad
\rho=1-y^2\ge\frac56,\qquad
K=\frac{\kappa}{y^4},\qquad
\kappa\ge54.
\tag{2.1}
\]

Assume \(R>0\), and use

\[
P=py,\qquad r=Ry,\qquad S=(p+m)y.
\]

The exact geometry is

\[
P-r=dmy,\qquad
S=P+\frac{P-r}{d},\qquad
0<r\le P.
\tag{2.2}
\]

Equation (1.6) gives

\[
S\le P+\frac85(P-r)
=:S_*(P,r)
=\frac{13P-8r}{5}
\le\frac{13}{5}P.
\tag{2.3}
\]

The first inequality is strict when \(m>0\); equality is retained for the
no-drop geometry \(m=0\), where \(P=r=S\).

The shelf estimate scales to

\[
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
\tag{2.4}
\]

The coarser factor in the packet is legitimate because

\[
\left(\frac{13}{5}\right)^2-2\frac{1571}{500}
=\frac{119}{250}>0,
\]

so \(\sqrt{2\pi\rho}<13/5\) for \(0<\rho\le1\).

Define

\[
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho},
\qquad
\widehat q=a(Q-1).
\tag{2.5}
\]

Because \(S=ny\) and \(\mu=\rho\kappa/y^4\), there is an exact identity

\[
\widehat q
=\frac{y^4+y^3S}{\rho\kappa}
=\frac{n+1}{\mu}.
\tag{2.6}
\]

If \(t=x_0/\mu\), then
\(\mu-x_0=n+\beta<n+1\), including \(\beta=0\), and hence

\[
1-t<\widehat q.
\tag{2.7}
\]

The two terms in (2.6) increase with \(y\) and decrease with \(\kappa\)
after using (2.3)--(2.4). Their closed proxy maximum is therefore at
\(y^2=1/6,\rho=5/6,\kappa=54\):

\[
\widehat q
<
\frac{y^4}{\rho\kappa}
+\frac{13}{5}y\sqrt{\frac{2\pi}{\rho\kappa}}
\le
\frac1{1620}
+\frac{13}{5}\sqrt{\frac{\pi}{135}}.
\tag{2.8}
\]

The exact radical comparison is

\[
\left(\frac{763}{5000}\right)^2
-\frac{1571}{67500}
=\frac{8563}{675000000}>0,
\tag{2.9}
\]

so

\[
\widehat q
<
\frac1{1620}+\frac{13}{5}\frac{763}{5000}
=\frac{804689}{2025000}
<\frac{159}{400}.
\tag{2.10}
\]

The final displacement reserve is

\[
\boxed{
\frac{159}{400}-\frac{804689}{2025000}
=\frac{497}{4050000}>0.}
\tag{2.11}
\]

In particular, \(1-\widehat q>241/400>0\). Before any outer-region
slope is invoked,

\[
\frac{x_0}{K}
=\rho t
>\rho(1-\widehat q)
>\frac56\frac{241}{400}
=\frac{241}{480}
=\frac12+\frac1{480}.
\tag{2.12}
\]

Thus the dangerous plateau is localized strictly beyond \(K/2\), even
at \(\varepsilon=1/6,\kappa=54\).

## 3. Ordinary-floor implication and strict self-consistency

In the dangerous branch, \(p>0\). The definition of the first plateau
gives

\[
\left\lfloor A(x_0)+\frac14\right\rfloor
=
\left\lfloor A(x_0+p)+\frac14\right\rfloor.
\]

Two real numbers with the same ordinary floor differ by strictly less
than one, including when either lies on an integer wall. Since \(A\) is
decreasing,

\[
1>A(x_0)-A(x_0+p)
=\int_{x_0}^{x_0+p}\sigma(z)\,dz,
\tag{3.1}
\]

where

\[
\sigma(z)=-A'(z)
=\frac1\pi
\left(\arccos\frac zK-\arccos\frac z\mu\right)
\]

is increasing. At \(x_0=\mu t\),

\[
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
\tag{3.2}
\]

Also

\[
1-\rho t
=\varepsilon+\frac{\mu-x_0}{K}
<y^2+\frac{y^4+y^3S}{\kappa}
=y^2Q.
\]

Since \(0<\rho t<1\),

\[
1-\rho^2t^2<2y^2Q.
\tag{3.3}
\]

Using \(p=P/y\), equations (3.1)--(3.3) imply

\[
1>
\frac{Pt}{\pi\sqrt{2Q}}.
\]

Every factor is positive. Equation (2.7) gives
\(t>1-\widehat q>0\), so positive squaring and division yield

\[
\boxed{
P^2<
\frac{2\pi^2Q}{(1-\widehat q)^2}.}
\tag{3.4}
\]

This reconstructs the actual self-consistency inequality before any
synthetic replacement. It also owns every denominator, radicand, and
squaring sign used in the step.

## 4. Actual-to-synthetic implication and complete fixed-\(r=B\) path

Define

\[
Q_*=1+\frac{y^2}{\kappa}+\frac{yS_*}{\kappa},
\qquad
q_*=a(Q_*-1),
\qquad
H(P,r)=\frac{2\pi^2Q_*}{(1-q_*)^2}.
\tag{4.1}
\]

The same shelf calculation as (2.8)--(2.10), now using
\(S_*\le(13/5)P\), gives \(q_*<159/400\). For fixed \(a\), the function

\[
F(Q)=\frac{2\pi^2Q}{[1-a(Q-1)]^2}
\]

has derivative

\[
F'(Q)
=2\pi^2
\frac{1+q+2a}{(1-q)^3}>0
\qquad(q=a(Q-1)<1).
\tag{4.2}
\]

Since \(S\le S_*\), equations (3.4) and (4.2) prove the required genuine
actual-to-synthetic implication

\[
\boxed{P^2<H(P,r).}
\tag{4.3}
\]

Now put \(B=14/3\), and suppose for contradiction that \(r\ge B\).
Because

\[
\frac{\partial S_*}{\partial r}=-\frac85<0,
\]

equation (4.2) shows that \(H\) decreases with \(r\). Thus

\[
H(P,r)\le H(P,B).
\tag{4.4}
\]

The full path \((P',B)\), \(B\le P'\le P\), is controlled, not merely
its endpoints. Indeed \(P'\le P\) preserves the original shelf ceiling,
and

\[
0<S_*(P',B)\le\frac{13}{5}P'
\]

preserves \(q_*<159/400\) at every path point. Also

\[
\left(\frac{49}{120}\right)^2-\frac16
=\frac1{14400}>0,
\qquad
6-\left(\frac{120}{49}\right)^2
=\frac6{2401}>0,
\tag{4.5}
\]

so \(y<49/120\), \(1/y>120/49\), and

\[
a=\frac{y^2}{1-y^2}\le\frac15,
\qquad
\frac{\partial Q_*}{\partial P'}
=\frac{13y}{5\kappa}
<\frac{637}{32400}.
\tag{4.6}
\]

Using (1.1), (2.10), and (4.6), uniformly along the path,

\[
\begin{aligned}
\frac{\partial H}{\partial P'}
&=
2\pi^2\frac{\partial Q_*}{\partial P'}
\frac{1+q_*+2a}{(1-q_*)^3}\\
&<
2\left(\frac{1571}{500}\right)^2
\frac{637}{32400}
\frac{1+159/400+2/5}{(1-159/400)^3}\\
&=
\frac{2260740364246}{708624500625}
<\frac{16}{5}.
\end{aligned}
\tag{4.7}
\]

The exact derivative reserve is

\[
\frac{16}{5}
-\frac{2260740364246}{708624500625}
=\frac{6858037754}{708624500625}>0.
\tag{4.8}
\]

Consequently, on every point of the path,

\[
\frac d{dP'}\{P'^2-H(P',B)\}
>2B-\frac{16}{5}
=\frac{92}{15}>0.
\tag{4.9}
\]

At the initial endpoint \(P'=r=B\), one has \(S_*=B\). Equations
(4.5)--(4.6) give the strict proxies

\[
Q_*(B,B)<\frac{10093}{9720},
\qquad
q_*(B,B)<\frac{373}{48600}.
\tag{4.10}
\]

The initial endpoint reserve is

\[
\begin{aligned}
B^2-H(B,B)
&>
B^2-
2\left(\frac{1571}{500}\right)^2
\frac{10093/9720}{(1-373/48600)^2}\\
&=
\frac{2505132463469}{2616573970125}>0.
\end{aligned}
\tag{4.11}
\]

Equations (4.4), (4.9), and (4.11) imply
\(P^2-H(P,r)>0\), contradicting (4.3). Hence the entire synthetic path,
including its no-drop endpoint geometry, proves

\[
\boxed{r<\frac{14}{3}},
\qquad
\boxed{R<\frac{14}{3\sqrt\varepsilon}}.
\tag{4.12}
\]

## 5. Action gain and both payment branches

The permitted action identity and
\(\arccos(1-v)\ge\sqrt{2v}\) give

\[
\eta\ge\frac{2\sqrt2}{3\pi}y^3,
\qquad
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
\tag{5.1}
\]

Using \(\kappa\ge54\), (1.1), and (1.4),

\[
K\eta>
\frac{280000}{17281}\frac1y.
\tag{5.2}
\]

The gain remaining after the full plateau-loss cap is

\[
\frac{280000}{17281}-\frac{14}{3}
=\frac{598066}{51843}>0.
\tag{5.3}
\]

Moreover,

\[
4\delta<\frac{8\sqrt2}{15}
<\frac{132}{175}.
\tag{5.4}
\]

If \(R>0\), the universally strict floor inequality
\(\lfloor x\rfloor>x-1\), valid also at integer \(x\), and (4.12) give

\[
\begin{aligned}
M
&=\lfloor K\eta\rfloor-R\\
&>
\left(\frac{280000}{17281}-\frac{14}{3}\right)\frac1y-1.
\end{aligned}
\]

Using \(1/y>120/49\), the exact dangerous reserve after paying both the
unit floor loss and the complete interface term is

\[
\boxed{
\left(\frac{598066}{51843}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{80132733}{3024175}>0.}
\tag{5.5}
\]

If \(R\le0\), including \(R=0\), then
\(M\ge\lfloor K\eta\rfloor\). The safe reserve is

\[
\boxed{
\left(\frac{280000}{17281}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{114694733}{3024175}>0.}
\tag{5.6}
\]

Thus \(M>4\delta\) in both branches. Substitution into the permitted
decomposition gives

\[
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^K A(z)\,dz.
\tag{5.7}
\]

The permitted high-interface and high-angular shifted-tail results,
strict-to-ordinary-floor transfer, and weighted lattice scaffold then
give the frozen local claim, including \(K=54/\varepsilon^2\).

## 6. Exceptional branches and strict walls

Every exceptional branch used by the reduction has a direct owner:

- If \(p=n>0\), then \(m=0\), \(R=p>0\), and \(P=r=S\). This is the
  equality geometry retained at the start of the full synthetic path.
- If \(p=0<n\), then \(R=-dm<0\), so the immediate-drop branch is safe.
- If \(n=0\), the stipulated values \(p=m=R=0\) put the degenerate head
  in the safe branch.
- The wall \(R=0\) belongs to the safe estimate (5.6). The first
  \(R>0\) branch uses no positive lower bound on \(R\).
- At \(\mu-x_0\in\mathbb Z\), one has \(\beta=0\), \(q=\mu\), and
  \(\delta=0\). In both adjacent cells only \(0\le\beta<1\) and
  \(n+\beta<n+1\) are used.
- At \(x_0=\mu\), the permitted high-interface theorem owns equality;
  the approach from below is the \(n=0\) safe branch.
- At every ordinary-floor wall, equality of the two floors still implies
  the strict difference (3.1). At \(K\eta\in\mathbb Z\),
  \(\lfloor K\eta\rfloor>K\eta-1\) still pays the full possible unit
  loss.
- Coarse-proxy integer walls only change which already-covered plateau
  branch is selected. The strict phase enclosure remains bounded by the
  ordinary floor at such a wall.
- At the angular cutoff \(\nu=K\), strict spectral counting has no active
  endpoint channel. At a spectral wall, the separated convention
  \(n\pi<\Psi(K)\) excludes the equality mode.
- Equations (2.10), (3.3), and (4.6) prove positivity of every
  denominator and radicand before division or squaring. The whole
  synthetic path, not a finite sample, retains the same signs.
- No step assumes \(\kappa>54\). Strictness at \(\kappa=54\), including
  \((\varepsilon,K)=(1/6,1944)\), comes from the angular, radical,
  displacement, path, endpoint, and payment reserves.

The overlap faces remain assigned to the sharpest accepted theorem.
At \(\varepsilon=1/100\) the complete endpoint begins; at \(1/25\)
the accepted constant \(20\) theorem is sharpest; at \(1/20\) and
\(1/10\) the accepted constant \(24\) theorem applies; at \(1/8\)
the accepted constant \(32\) theorem applies; and at \(1/6\) the new
constant \(54\) theorem applies. Constants \(20,24,32\) are never
extrapolated beyond their accepted domains.

## 7. Independent central endpoint

This argument does not use the local plateau proof. At \(\rho=5/6\),

\[
a_\rho=10\pi<\frac{220}{7}<36,
\qquad
36-\frac{220}{7}=\frac{32}{7}>0,
\]

so

\[
\sqrt{a_\rho}<6.
\tag{7.1}
\]

The action estimate at \(\varepsilon=1/6\) simplifies to

\[
\eta_{5/6}\ge\frac1{9\pi\sqrt3}.
\]

By (1.1) and (1.4),

\[
49-9\left(\frac{1571}{500}\right)\left(\frac{97}{56}\right)
=\frac{517}{28000}>0,
\]

and therefore

\[
\eta_{5/6}>\frac1{49}.
\tag{7.2}
\]

Also

\[
C_0=1+\frac{8\sqrt2}{15}<\frac{307}{175}.
\tag{7.3}
\]

For \(Y=295\), equations (7.1)--(7.3) yield

\[
\begin{aligned}
\eta_{5/6}Y^2-\sqrt{a_{5/6}}Y-C_0
&>
\frac1{49}295^2-6(295)-\frac{307}{175}\\
&=\frac{5226}{1225}>0.
\end{aligned}
\tag{7.4}
\]

The quadratic has negative constant term and positive leading
coefficient, so its two roots have opposite signs. Its unique positive
root is exactly \(\sqrt{K_0(5/6)}\). Equation (7.4) therefore proves

\[
\boxed{K_0(5/6)<295^2=87025.}
\tag{7.5}
\]

The fixed-ratio theorem owns \(K=K_0(5/6)\) itself, while strictness in
(7.5) puts \(K=295^2\) inside the proved range.

## 8. Selected-route obstructions

These checks are failures of selected proxies, not counterexamples.

For \(\kappa=53\), at the endpoint
\(\varepsilon=1/6,\rho=5/6\), equation (1.3) gives

\[
\frac{2\pi}{265}>\frac{333}{14045}.
\]

Furthermore,

\[
\frac{333}{14045}
-\left(\frac{3079}{20000}\right)^2
=\frac{10003031}{1123600000000}>0.
\]

Hence the endpoint envelope produced solely by the current shelf factor
satisfies

\[
\frac1{1590}
+\frac{13}{5}\sqrt{\frac{2\pi}{265}}
>
\frac1{1590}+\frac{13}{5}\frac{3079}{20000}
=\frac25+\frac{14293}{15900000}.
\tag{8.1}
\]

Localization beyond \(K/2\) at \(\rho=5/6\) would require a displacement
cap below \(2/5\). Thus this selected coarse envelope cannot certify
\(\kappa=53\). It says nothing about the actual shell inequality or a
different proof architecture.

For the central endpoint, the selected \(Y=294\) proxy is

\[
\frac1{49}294^2-6(294)-\frac{307}{175}
=-\frac{307}{175}<0.
\tag{8.2}
\]

Because (7.4) used one-sided bounds, (8.2) does not determine the sign of
the true quadratic at \(294\). In particular, it does not prove
\(K_0(5/6)\ge294^2\).

## 9. Seven-zone union and exact faces

Only after both independent targets and the review gates pass may the
accepted envelope be refined to these coarse closed zones:

| zone | ratio interval | possible residual ceiling |
|---|---|---|
| 1 | \([\rho_*,1/16]\) | \(K<64\) |
| 2 | \([1/16,5/6]\) | \(K<K_0(\rho)\le K_0(5/6)<87025\) |
| 3 | \([5/6,7/8]\) | \(K<54/(1-\rho)^2\le3456\) |
| 4 | \([7/8,9/10]\) | \(K<32/(1-\rho)^2\le3200\) |
| 5 | \([9/10,19/20]\) | \(K<24/(1-\rho)^2\le9600\) |
| 6 | \([19/20,24/25]\) | \(K<24/(1-\rho)^2\le15000\) |
| 7 | \([24/25,99/100]\) | \(K<20/(1-\rho)^2\le200000\) |

The unchanged endpoint \([99/100,1)\) owns every frequency. The finite
ceiling list is

\[
64,\quad87025,\quad3456,\quad3200,\quad9600,\quad15000,\quad200000,
\]

whose maximum is exactly \(200000\).

The shared ratio and energy faces have explicit owners:

- \(\rho=\rho_*\) is owned by the complete small-hole theorem, and the
  two accepted central constructions overlap at \(\rho=1/16\).
- At \(\rho=5/6\), the new theorem includes
  \(K=54/(1/6)^2=1944\); the moving face \(K=K_0(5/6)\) is independently
  owned by the fixed-ratio theorem.
- At \(\rho=7/8\), the accepted constant \(32\) theorem owns the sharper
  face \(K=2048\), rather than the new coarse value \(3456\).
- At \(\rho=9/10\), the accepted constant \(24\) theorem owns
  \(K=2400\), rather than the constant \(32\) value \(3200\).
- At \(\rho=19/20\), the constant \(24\) theorem owns \(K=9600\).
- At \(\rho=24/25\), the accepted constant \(20\) theorem owns the
  sharper face \(K=12500\), rather than \(15000\).
- At \(\rho=99/100\), the complete endpoint owns every \(K\), including
  \(K=200000\).

Thus the listed walls \(K=64,1944,2048,2400,3200,3456,9600,12500,
15000,87025,200000\) are all covered wherever they meet adjacent
zones. The strict comparison (7.5) owns \(K=295^2\) throughout the
central fixed-ratio interval by monotonicity. The failed proxy at
\(K=294^2\) is not promoted; at the seam point \(\rho=5/6\), that energy
is nevertheless covered by the independent local theorem.

Consequently the prospective all-ratio statement includes equality:

\[
\boxed{0<\rho<1,\qquad K\ge200000.}
\tag{9.1}
\]

The exact reduction from the accepted Round 14 ceiling is

\[
\frac{550^2}{200000}
=\frac{121}{80}
=1+\frac{41}{80}>1.
\tag{9.2}
\]

This is only a high-frequency analytic cover. The complete all-frequency
endpoint remains exactly \([99/100,1)\), and the true nonrectangular
compact residual remains open.

## 10. Reproducibility conclusion

The accompanying exact verifier checks seven logically separate ledgers:
elementary constants, angular displacement and localization, the complete
synthetic path, both action-payment branches, the central endpoint, the
\(\kappa=53\) obstruction, and all seven union zones and faces. Focused
tests exercise each ledger independently.

The decisive uniform displacement reserve is \(497/4050000\), while the
synthetic endpoint and both payment reserves are also strictly positive.
No screen fails, no sampled sign or optimizer is used, and neither
obstruction is misreported as a theorem-level impossibility.
