# Round 20 exploration: exact high-ratio repair through \(k_{10}\)

Status: **PASS through \(k_{10}\); exploratory only; not frozen or
promoted**.

Date: 2026-07-15.

This note starts from the final exploratory proof through \(k_9\), repairs
its exact cap-\(89\) obstruction with a sharper internal first-zero wall,
and audits every first, second, third, and higher radial possibility in the
next band. No Round 19 artifact is edited or enlarged.

## 1. Claim and exact prospective subtraction

Write

\[
 \rho_c=\frac1{1+2\pi},\qquad
 z=z_\rho=\frac{\pi}{1-\rho},\qquad
 x=z^2,
\]

\[
 d_\ell=\ell(\ell+1),\qquad
 k_m(\rho)=\sqrt{x+d_m},
\]

and

\[
 \mathcal W(\rho,K)
 =\frac{2}{9\pi}(1-\rho^3)K^3.
 \tag{1}
\]

The closed exploratory theorem is

\[
 \boxed{
 \rho_c\leq\rho\leq\frac78,\qquad
 z_\rho\leq K\leq k_{10}(\rho)}
 \quad\Longrightarrow\quad
 \boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K)}.
 \tag{2}
\]

The predecessor owns the closed part through \(k_9\). The genuinely new
band proved here is

\[
 \boxed{
 \mathcal C_{20}^{\mathrm{H},10}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_9(\rho)<K\leq k_{10}(\rho)\right\}.}
 \tag{3}
\]

If independently reconstructed and promoted with the preceding Round 20
steps, the exact high component of the residual becomes

\[
 \boxed{
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_{10}(\rho)<K<U(\rho)\right\}.}
 \tag{4}
\]

No lower-ratio component is changed by this note.

## 2. Dependency and provenance ledger

| input | SHA-256 | exact use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` | predecessor through the included face \(K=k_9\), inherited upper floor, and established shell comparison toolkit |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` | internal \(j_{7/2,2}>103/10\), internal \(j_{15/2,1}>23/2\), angular propagation, and qualified Lorch specialization \(j_{19/2,1}>64/5\) |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` | strict first-\(\ell=8\) wall \(j_{17/2,1}>71/6\) |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated shell spectrum, multiplicity \(2\ell+1\), and strict spectral count |

The new source card labels every external statement. Its second-zero and
order-\(15/2\) improvements are internal exact arguments; only the
order-\(19/2\) first-zero seed is a new qualified Lorch specialization.
No numerical zero table is used.

## 3. Channel comparisons and strict zero walls

Let \(q_{\ell,n}=q_{\ell,n}(\rho)\) be the shell frequency in angular
channel \(\ell\) and radial index \(n\). Fixed-channel min--max gives

\[
 \boxed{
 q_{\ell,n}^2\geq n^2x+d_\ell,
 \qquad q_{0,n}=nz.}
 \tag{5}
\]

Zero extension into the unit ball and angular form ordering give

\[
 \boxed{q_{\ell,n}^2\geq j_{\ell+1/2,n}^{\,2},}
 \tag{6}
\]

\[
 \boxed{
 j_{p+1/2,n}^{\,2}
 \geq j_{\ell+1/2,n}^{\,2}+d_p-d_\ell
 \qquad(p\geq\ell).}
 \tag{7}
\]

The exact first-mode walls needed below are

\[
 \boxed{
 q_{7,1}>\frac{23}{2},\qquad
 q_{8,1}>\frac{71}{6},\qquad
 q_{9,1}>\frac{64}{5}.}
 \tag{8}
\]

The sharpened second-mode walls are

\[
 \boxed{
 q_{3,2}>\frac{103}{10},\qquad
 q_{4,2}>\frac{53}{5},\qquad
 q_{5,2}>11,}
 \tag{9}
\]

and, for \(p\geq3\),

\[
 \boxed{
 q_{p,2}^2>\frac{9409}{100}+d_p.}
 \tag{10}
\]

All these walls are strict. Equality at any displayed rational wall still
leaves the corresponding shell mode uncounted.

## 4. Exhaustive inventory through the closed face \(K=k_{10}\)

On the high-ratio interval,

\[
 z\geq z_{\rho_c}=\pi+\frac12
 >\frac{193}{53},
 \qquad
 x>13,
 \tag{11}
\]

where

\[
 \left(\frac{193}{53}\right)^2-13
 =\frac{732}{2809}>0.
\]

Assume \(K\leq k_{10}\), so \(K^2\leq x+110\).

Every mode with \(n\geq4\) is absent, because

\[
 q_{\ell,n}^2-K^2
 \geq16x+d_\ell-(x+110)
 >15\cdot13-110=85.
 \tag{12}
\]

For \(n=3\) and \(\ell\geq2\),

\[
 q_{\ell,3}^2-K^2
 \geq9x+6-(x+110)
 =8x-104>0.
 \tag{13}
\]

Thus only third modes \(\ell=0,1\) can occur.

For the second mode in channel six, split at \(x=68/3\). If
\(x\leq68/3\), then (10) gives

\[
 q_{6,2}^2>\frac{13609}{100}
 >\frac{398}{3}\geq x+110,
 \qquad
 \frac{13609}{100}-\frac{398}{3}=\frac{1027}{300}>0.
 \tag{14}
\]

If \(x>68/3\), equation (5) gives

\[
 q_{6,2}^2-K^2
 \geq4x+42-(x+110)=3x-68>0.
 \tag{15}
\]

Angular ordering excludes every second mode with \(\ell\geq6\). Finally,
every first mode with \(\ell\geq10\) is absent by (5), since
\(d_\ell\geq110\); on the face \(K=k_{10}\), equality in the moving
lower bound for \(\ell=10\) is uncounted.

The complete possible inventory is therefore

\[
 \boxed{
 (\ell,1),\ 0\leq\ell\leq9;\qquad
 (\ell,2),\ 0\leq\ell\leq5;\qquad
 (\ell,3),\ \ell=0,1.}
 \tag{16}
\]

No fourth radial entry, omitted second or third channel, or omitted angular
multiplicity can occur below the included upper face.

## 5. Exact ratio localizations

If a second mode \((h,2)\) is counted, equations (5) and
\(K^2\leq x+110\) imply

\[
 4x+d_h<K^2\leq x+110,
 \qquad
 3x<110-d_h.
 \tag{17}
\]

If any third mode is counted, then angular ordering makes \((0,3)\)
counted as well. Since \(q_{0,3}=3z\),

\[
 9x<K^2\leq x+110,
 \qquad
 x<\frac{55}{4}.
 \tag{18}
\]

The following exact reserves convert these strict \(x\)-bounds into
simple rational ratio cutoffs:

\[
\begin{array}{c|c|c|c}
\text{condition}&\text{forced }x\text{-bound}&r&z(r)^2-\text{bound}\\ \hline
h=5&x<80/3&2/5&25195/33708\\
h=4&x<30&3/7&40281/179776\\
\text{any second mode}&x<110/3&1/2&23677/8427\\
\text{any third mode}&x<55/4&4/25&65185/275282
\end{array}
 \tag{19}
\]

Each reserve uses only \(\pi>333/106\). Since \(z_\rho\) is strictly
increasing, a counted mode in a row forces \(\rho<r\). The ratio face
itself is empty for that mode.

## 6. Simultaneous-mode restrictions and exhaustive caps

Let \(H\) be the largest counted first angular index and, when a second
mode occurs, let \(h\) be its largest angular index. A third-mode
contribution is at most

\[
 (2\cdot0+1)+(2\cdot1+1)=4.
 \tag{20}
\]

Every lower angular channel can be included conservatively, because

\[
 \sum_{\ell=0}^{H}(2\ell+1)=(H+1)^2.
 \tag{21}
\]

The high first-mode walls force three useful incompatibilities.

If \(H=9\), then (8) and the upper face imply

\[
 x>\left(\frac{64}{5}\right)^2-110
 =\frac{1346}{25}>\frac{110}{3}.
 \tag{22}
\]

Thus no second or third mode can coexist with \(H=9\).

If \(H=8\), then

\[
 x>\left(\frac{71}{6}\right)^2-110
 =\frac{1081}{36}>30.
 \tag{23}
\]

Therefore \(h\leq3\), and no third mode can occur.

If \(H=7\), then

\[
 x>\left(\frac{23}{2}\right)^2-110
 =\frac{89}{4}>\frac{55}{4},
 \tag{24}
\]

so no third mode can occur.

The resulting cap table is exhaustive:

\[
\begin{array}{c|c|c}
\text{first category}&\text{radial category}&\text{cap}\\ \hline
H=9&\text{no second or third}&100\\
H=8&\text{no second}&81\\
H=8&h\leq3&97\\
H=7&\text{no second}&64\\
H=7&h\leq3&80\\
H=7&h=4&89\\
H=7&h=5&100\\
H\leq6&h\leq4,\ \text{no third}&74\\
H\leq6&h\leq3,\ \text{third present}&69\\
H\leq6&h=4,\ \text{third present}&78\\
H\leq6&h=5,\ \text{no third}&85\\
H\leq6&h=5,\ \text{third present}&89
\end{array}
 \tag{25}
\]

For example, the last cap is \(49+36+4=89\). Every entry includes full
angular multiplicities, and equations (22)--(24) own every omitted cell.

## 7. Monotonic payment facts and a uniform baseline

At fixed \(c>0\), \(\mathcal W(\rho,c)\) is strictly decreasing in
\(\rho\). Also

\[
 \frac{2}{9\pi}>\frac7{99}
 \tag{26}
\]

because \(\pi<22/7\).

Put

\[
 F_9(\rho)=\mathcal W(\rho,k_9(\rho)).
\]

The sign of \(F_9'\) is the sign of

\[
 \pi^2(1+\rho)-90\rho^2(1-\rho)^2
 >9-\frac{90}{16}=\frac{27}{8}>0.
 \tag{27}
\]

Thus \(F_9\) is strictly increasing.

At the left endpoint,

\[
 \rho_c<\frac{11}{80},
 \qquad
 z_{\rho_c}=\pi+\frac12>\frac{193}{53}.
\]

The first inequality follows from
\(333/106-69/22=3/583>0\). Hence

\[
\begin{aligned}
 F_9(\rho_c)
 &>\frac7{99}
 \left(1-\left(\frac{11}{80}\right)^3\right)
 \left(90+\left(\frac{193}{53}\right)^2\right)^{3/2}
 >74.
 \tag{28}
\end{aligned}
\]

The last comparison is sign-safe after squaring; its exact reserve is

\[
 \left[\frac7{99}
 \left(1-\left(\frac{11}{80}\right)^3\right)\right]^2
 \left(90+\left(\frac{193}{53}\right)^2\right)^3
 -74^2
 =\frac{376406437293962706531}
 {5810254283800576000000}>0.
 \tag{29}
\]

Since the new band has \(K>k_9\), equations (27)--(29) pay every cap at
most \(74\) in (25), including all equality faces of those cap rows.

## 8. Exact payment of every remaining cap

For the fixed-wall cases, equations (19), (26), and the applicable strict
zero wall give the following complete ledger:

\[
\begin{array}{c|c|c|c|c}
\text{case}&\text{cap}&r&c&
\frac7{99}(1-r^3)c^3\\ \hline
H=8,\ \text{second}&97&1/2&71/6&
17537639/171072=97+943655/171072\\
H=7,\ h\leq3&80&1/2&23/2&
596183/6336=80+89303/6336\\
H=7,\ h=4&89&3/7&23/2&
961193/9702=89+97715/9702\\
H=7,\ h=5&100&2/5&23/2&
1107197/11000=100+7197/11000\\
H\leq6,\ h=4,\ \text{third}&78&4/25&53/5&
1801858331/21484375=78+126077081/21484375\\
H\leq6,\ h=5,\ \text{no third}&85&2/5&11&
11011/125=85+386/125\\
H\leq6,\ h=5,\ \text{third}&89&4/25&11&
1464463/15625=89+73838/15625
\end{array}
 \tag{30}
\]

Every applicable row has \(\rho<r\) and \(K>c\), so the displayed
payment is strict. The \(H=7\), no-second cap \(64\), and both
\(H\leq6\) caps at most \(74\), are already paid by (28)--(29).

Two no-radial high-angular cases require a fixed/moving bridge rather than
a ratio cutoff.

### 8.1 The \(H=9\) cap

Split at \(\rho=16/25\). Exact arithmetic gives

\[
 \frac7{99}
 \left(1-\left(\frac{16}{25}\right)^3\right)
 \left(\frac{64}{5}\right)^3
 =\frac{2350645248}{21484375}
 =100+\frac{202207748}{21484375},
 \tag{31}
\]

and

\[
 k_9(16/25)^2-\left(\frac{64}{5}\right)^2
 >\frac{648969}{280900}>0.
 \tag{32}
\]

For \(\rho\leq16/25\), the strict first-\(\ell=9\) wall and fixed-wall
decrease pay \(100\). For \(\rho\geq16/25\), equations (27), (31)--(32),
and \(K>k_9\) pay \(100\). Both estimates own the split face.

### 8.2 The \(H=8\), no-second cap

Split at \(\rho=3/5\). One has

\[
 \frac7{99}
 \left(1-\left(\frac35\right)^3\right)
 \left(\frac{71}{6}\right)^3
 =\frac{122763473}{1336500}
 =81+\frac{14506973}{1336500},
 \tag{33}
\]

and

\[
 k_9(3/5)^2-\left(\frac{71}{6}\right)^2
 >\frac{4713989}{404496}>0.
 \tag{34}
\]

The fixed first-\(\ell=8\) wall pays the lower-ratio branch, while the
strictly increasing \(F_9\) pays the upper-ratio branch. Again both
estimates hold at the split face.

Equations (28)--(34) pay every row of the exhaustive table (25). Therefore
the new band (3), and hence the closed prospective theorem (2), are proved.

## 9. Exact containment below the inherited upper floor

For \(\rho\leq7/8\),

\[
 z\leq8\pi<\frac{176}{7}.
\]

Consequently

\[
 28^2-k_{10}(\rho)^2
 >28^2-\left(\frac{176}{7}\right)^2-110
 =\frac{2050}{49}>0.
 \tag{35}
\]

Thus \(k_{10}<28\). On \(\rho_c\leq\rho<5/6\), the inherited central
floor is larger than \(64\). On the seam branch,

\[
 U(\rho)=\frac{54}{(1-\rho)^2}\geq1944.
\]

Hence

\[
 \boxed{k_{10}(\rho)<U(\rho)
 \qquad(\rho_c\leq\rho<7/8).}
 \tag{36}
\]

The subtraction (4) remains strictly inside the inherited residual.

## 10. Equality, endpoint, wall-order, and provenance audit

- **\(K=k_9\):** the predecessor owns the complete closed face. The new
  band excludes it, and every new moving payment uses \(K>k_9\).
- **\(K=k_{10}\):** included. The moving lower wall for \((10,1)\)
  equals the upper face, so strict counting excludes that channel.
- **Second-channel cutoff:** at \(x=68/3\), the strict ball bound (14)
  excludes \((6,2)\); on the upper side the moving comparison (15) is
  strict.
- **Ratio faces:** a mode defining a row of (19) is absent at its ratio
  face because the displayed reserve is positive. No payment branch owns
  a mode at a face where its necessary strict inequality fails.
- **Fixed zero walls:** every bound in (8)--(10) is strict. Immediately
  above a wall, its entire angular multiplicity is already included in
  (25).
- **Bridge faces:** fixed and moving payments both hold at \(16/25\) and
  \(3/5\), with the strict reserves (31)--(34).
- **Third modes:** any counted third mode forces the exact radial mode
  \(q_{0,3}=3z\) to be counted. This owns the \(x<55/4\) localization;
  no third angular multiplicity is silently omitted.
- **\(\rho=\rho_c\):** included. The exact baseline reserve (29) is
  strict there. The closed theorem includes \(\rho=7/8\), while the
  genuinely new residual subtraction excludes that already-owned endpoint.
- **The \(5/6\) seam and \(K=U\):** only the inherited upper-floor owner
  changes. Equation (36) controls both branches, and \(K=U\) is not
  subtracted.
- **Source scope:** the order-\(19/2\) Lorch statement is used only at
  radial index one. The sharper order-\(7/2\) second zero and the repaired
  order-\(15/2\) first wall are explicitly internal. No shell cross-product
  zero or uncertified decimal zero is imported.

Coincident entry walls only omit modes under the strict count. Every cap
contains full multiplicities, and no cap is carried past a frequency wall
without its full update.

## 11. Verdict

The exact analytic repair is **PASS through \(k_{10}\)**. The previous
cap-\(89\) obstruction is removed by the internally proved wall
\(q_{7,1}>23/2\); the simultaneously strengthened second-radial walls pay
the only new cap-\(85\), cap-\(89\), and cap-\(100\) configurations.

Every first, second, third, and higher radial possibility is exhausted;
all angular multiplicities and coexistence restrictions are explicit;
every ratio, bridge, endpoint, and equality face has an owner; and
\(k_{10}<U\) is strict. The closed extension established by this note is

\[
 \boxed{m=10.}
\]

This note remains exploratory. It must not be treated as frozen or promoted
without a proof-free claim freeze, clean-room reconstruction, independent
exact-constant verification, adversarial review, and a State Patch audit.
