# Round 20 exploration: exact high-ratio extension through \(k_{11}\)

Status: **PASS through \(k_{11}\); exploratory only; not frozen or
promoted**.

Date: 2026-07-15.

This note starts from the independently audited exploratory proof through
\(k_{10}\). Two new internal higher-radial zero walls remove the only
prospective cap obstructions, and one narrow qualified Lorch specialization
supplies the new highest first-mode wall. No Round 19 artifact is edited or
enlarged.

## 1. Claim and prospective subtraction

Write

\[
 \rho_c=\frac1{1+2\pi},
 \qquad
 z=z_\rho=\frac{\pi}{1-\rho},
 \qquad
 x=z^2,
\]

\[
 d_\ell=\ell(\ell+1),
 \qquad
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
 \rho_c\leq\rho\leq\frac78,
 \qquad z_\rho\leq K\leq k_{11}(\rho)}
 \quad\Longrightarrow\quad
 \boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
 \tag{2}
\]

The predecessor owns the closed part through \(k_{10}\). The genuinely
new band is

\[
 \boxed{
 \mathcal C_{20}^{\mathrm{H},11}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac78,
 \quad k_{10}(\rho)<K\leq k_{11}(\rho)\right\}.}
 \tag{3}
\]

If independently reconstructed and promoted with the preceding Round 20
steps, the exact high component of the residual becomes

\[
 \boxed{
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac78,
 \quad k_{11}(\rho)<K<U(\rho)\right\}.}
 \tag{4}
\]

No lower-ratio component is changed by this note.

## 2. Dependency and provenance ledger

| input | SHA-256 | exact use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/high-k10-repair.md` | `0e6fdadc57cdf8e173fb1dc1dad5a1403664833ae722a81b66ba59d5b202704a` | predecessor through the included face \(K=k_{10}\), inherited comparison toolkit, and upper floor |
| `rounds/polya-main/round_020/exploration/high-k10-adversarial-audit.md` | `9ec17b81aea3d6b6899dd25dd07f0241963ca8b246544080ecea08857c697bb1` | independent reconstruction and PASS verdict for the predecessor |
| `sources/round20_k11_zero_bounds.md` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` | internal \(j_{5/2,3}>61/5\), internal \(j_{11/2,2}>129/10\), their angular propagation, and qualified \(j_{21/2,1}>69/5\) |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` | strict first-mode wall \(q_{9,1}>64/5\) |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` | strict first-mode wall \(q_{8,1}>71/6\) |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum, multiplicity \(2\ell+1\), and strict count |

The new source card labels its only external theorem-level input: Lorch's
first-zero inequality at order \(21/2\). Both new higher-radial bounds are
internal elementary arguments. No numerical zero table is used.

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

The first-mode walls needed below are

\[
 \boxed{
 q_{8,1}>\frac{71}{6},
 \qquad
 q_{9,1}>\frac{64}{5},
 \qquad
 q_{10,1}>\frac{69}{5}.}
 \tag{8}
\]

The new higher-radial walls are

\[
 \boxed{q_{2,3}>\frac{61}{5},
 \qquad q_{5,2}>\frac{129}{10},}
 \tag{9}
\]

together with

\[
 \boxed{
 q_{p,3}^2>\frac{3571}{25}+d_p\quad(p\geq2),
 \qquad
 q_{p,2}^2>\frac{13641}{100}+d_p\quad(p\geq5).}
 \tag{10}
\]

All displayed zero walls are strict. Equality at a rational wall leaves
the corresponding mode uncounted.

## 4. Exhaustive inventory through \(k_{11}\)

On the high-ratio interval,

\[
 z\geq\pi+\frac12>\frac{193}{53},
 \qquad
 x>13.
 \tag{11}
\]

Assume \(K\leq k_{11}\), so \(K^2\leq x+132\).

Every mode with \(n\geq4\) is absent, because

\[
 q_{\ell,n}^2-K^2
 \geq16x+d_\ell-(x+132)
 >15\cdot13-132=63.
 \tag{12}
\]

For third modes with \(p\geq2\), split at \(x=16\). If \(x\leq16\),
then (10) gives

\[
 q_{p,3}^2>\frac{3571}{25}+d_p
 \geq\frac{3721}{25}>148\geq x+132.
 \tag{13}
\]

If \(x>16\), the moving comparison gives

\[
 q_{p,3}^2-K^2
 \geq9x+6-(x+132)
 =8x-126>2.
 \tag{14}
\]

Thus only third channels zero and one can occur.

For second modes with \(p\geq5\), split at \(x=34\). If \(x\leq34\),
then

\[
 q_{p,2}^2>\frac{13641}{100}+d_p
 \geq\frac{16641}{100}>166\geq x+132.
 \tag{15}
\]

If \(x>34\), then

\[
 q_{p,2}^2-K^2
 \geq4x+30-(x+132)
 =3x-102>0.
 \tag{16}
\]

Thus only second channels zero through four can occur. Finally, every
first mode with \(\ell\geq11\) is absent by (5), since
\(d_\ell\geq132\). At \(\ell=11,K=k_{11}\), equality in the moving
lower bound remains uncounted under the strict count.

The complete possible inventory is therefore

\[
 \boxed{
 (\ell,1),\ 0\leq\ell\leq10;
 \qquad
 (\ell,2),\ 0\leq\ell\leq4;
 \qquad
 (\ell,3),\ \ell=0,1.}
 \tag{17}
\]

No fourth radial mode, omitted second or third channel, or angular
multiplicity can occur below the included upper face.

## 5. Ratio localization and simultaneous restrictions

If any second mode \((h,2)\) is counted, (5) and the upper face imply

\[
 4x+d_h<K^2\leq x+132,
 \qquad
 x<44.
 \tag{18}
\]

At \(r_2=8/15\), the lower enclosure for \(\pi\) gives

\[
 z(r_2)^2-44>\frac{725209}{550564}>0.
 \tag{19}
\]

Hence a counted second mode forces \(\rho<8/15\).

If any third mode is counted, then

\[
 9x<K^2\leq x+132,
 \qquad
 x<\frac{33}{2}.
 \tag{20}
\]

At \(r_3=1/4\),

\[
 z(r_3)^2-\frac{33}{2}>
 \frac{5871}{5618}>0.
 \tag{21}
\]

Thus a counted third mode forces \(\rho<1/4\). Both ratio faces are
empty for the mode that defines them.

Let \(H\) be the largest counted first angular index. If \(H=10\),
then (8) and the upper face give

\[
 x>\left(\frac{69}{5}\right)^2-132
 =\frac{1461}{25}>44.
 \tag{22}
\]

No second or third mode can coexist. If \(H=9\), then

\[
 x>\left(\frac{64}{5}\right)^2-132
 =\frac{796}{25}>\frac{33}{2},
 \tag{23}
\]

so no third mode can coexist.

## 6. Exhaustive cap table

Since

\[
 \sum_{\ell=0}^{H}(2\ell+1)=(H+1)^2,
 \tag{24}
\]

the complete inventory and incompatibilities reduce to five cap rows:

\[
\begin{array}{c|c|c}
\text{first category}&\text{radial category}&\text{cap}\\ \hline
H=10&\text{no second or third}&121\\
H=9&\text{no second or third}&100\\
H=9&\text{second present; no third}&125\\
H=8&\text{no third}&106\\
H=8&\text{third present}&110\\
H\leq7&\text{all allowed radial modes}&93
\end{array}
 \tag{25}
\]

For example, the last three maxima are

\[
 81+25=106,
 \qquad
 81+25+4=110,
 \qquad
 64+25+4=93.
\]

Every cap contains full angular multiplicities. Lower values of \(H\),
the largest second index, or the largest third index only reduce the
corresponding entry.

## 7. Monotonicity and the uniform baseline

At fixed \(c>0\), \(\mathcal W(\rho,c)\) is strictly decreasing in
\(\rho\), and

\[
 \frac{2}{9\pi}>\frac7{99}.
 \tag{26}
\]

Put

\[
 F_{10}(\rho)=\mathcal W(\rho,k_{10}(\rho)).
\]

The sign of \(F_{10}'\) is the sign of

\[
 \pi^2(1+\rho)-110\rho^2(1-\rho)^2
 >9-\frac{110}{16}=\frac{17}{8}>0.
 \tag{27}
\]

Thus \(F_{10}\) is strictly increasing. Since \(\rho_c<1/7\) and
\(z_{\rho_c}=\pi+1/2>18/5\),

\[
 F_{10}(\rho_c)>
 \frac7{99}\frac{342}{343}
 \left(110+\left(\frac{18}{5}\right)^2\right)^{3/2}>96.
 \tag{28}
\]

The last comparison is sign-safe after squaring; the exact reserve is

\[
 \left(\frac7{99}\frac{342}{343}\right)^2
 \left(\frac{3074}{25}\right)^3-96^2
 =\frac{109839239456}{4539390625}>0.
 \tag{29}
\]

Because the new band has \(K>k_{10}\), this uniform baseline pays the
entire \(H\leq7\) cap \(93\), with strict reserve.

## 8. Exact payment of the five high-angular rows

### 8.1 The \(H=10\) cap

Split at \(\rho=13/20\). Exact arithmetic gives

\[
 \frac7{99}
 \left(1-\left(\frac{13}{20}\right)^3\right)
 \left(\frac{69}{5}\right)^3
 =\frac{1482707121}{11000000}
 =121+\frac{151707121}{11000000},
 \tag{30}
\]

and

\[
 k_{10}(13/20)^2-\left(\frac{69}{5}\right)^2
 >\frac{426449}{3441025}>0.
 \tag{31}
\]

For \(\rho\leq13/20\), the strict first-\(\ell=10\) wall and fixed-wall
decrease pay \(121\). For \(\rho\geq13/20\), equations (27),
(30)--(31), and \(K>k_{10}\) pay it. Both estimates own the split face.

### 8.2 The \(H=9\) rows

If a second mode is present, equations (19) and (8) give
\(\rho<8/15\) and \(K>64/5\). Therefore

\[
 \mathcal W(\rho,K)>
 \frac7{99}
 \left(1-\left(\frac8{15}\right)^3\right)
 \left(\frac{64}{5}\right)^3
 =\frac{5253627904}{41765625}
 =125+\frac{32924779}{41765625}.
 \tag{32}
\]

This pays the complete cap \(125\).

If no second mode is present, split at \(\rho=3/5\). One has

\[
 \frac7{99}
 \left(1-\left(\frac35\right)^3\right)
 \left(\frac{64}{5}\right)^3
 =\frac{179830784}{1546875}
 =100+\frac{25143284}{1546875},
 \tag{33}
\]

and

\[
 k_{10}(3/5)^2-\left(\frac{64}{5}\right)^2
 >\frac{8811001}{1123600}>0.
 \tag{34}
\]

The fixed wall pays below the split, and increasing \(F_{10}\) pays
above it. This closes the cap \(100\).

### 8.3 The \(H=8\) rows

If a third mode is present, equations (21) and (8) give
\(\rho<1/4\) and \(K>71/6\). Hence

\[
 \mathcal W(\rho,K)>
 \frac7{99}
 \left(1-\left(\frac14\right)^3\right)
 \left(\frac{71}{6}\right)^3
 =\frac{17537639}{152064}
 =110+\frac{810599}{152064}.
 \tag{35}
\]

This pays the complete cap \(110\).

If no third mode is present, split at \(\rho=3/7\). Exact arithmetic
gives

\[
 \frac7{99}
 \left(1-\left(\frac37\right)^3\right)
 \left(\frac{71}{6}\right)^3
 =\frac{28274969}{261954}
 =106+\frac{507845}{261954},
 \tag{36}
\]

and

\[
 k_{10}(3/7)^2-\left(\frac{71}{6}\right)^2
 >\frac{317585}{1617984}>0.
 \tag{37}
\]

The strict fixed wall pays below the split, while increasing \(F_{10}\)
pays above it. This closes cap \(106\).

Equations (28)--(37) pay every row of the exhaustive cap table. Therefore
the new band (3), and hence the closed exploratory theorem (2), are
proved.

## 9. Containment below the inherited upper floor

For \(\rho\leq7/8\),

\[
 z\leq8\pi<\frac{176}{7}.
\]

Consequently

\[
 28^2-k_{11}(\rho)^2
 >28^2-\left(\frac{176}{7}\right)^2-132
 =\frac{972}{49}>0.
 \tag{38}
\]

Thus \(k_{11}<28\). On \(\rho_c\leq\rho<5/6\), the inherited central
floor is larger than \(64\). On the seam branch,

\[
 U(\rho)=\frac{54}{(1-\rho)^2}\geq1944.
\]

Hence

\[
 \boxed{k_{11}(\rho)<U(\rho)
 \qquad(\rho_c\leq\rho<7/8).}
 \tag{39}
\]

The subtraction (4) remains strictly inside the inherited residual.

## 10. Equality, endpoint, and provenance audit

- **\(K=k_{10}\):** the independently audited predecessor owns this
  closed face. The new band excludes it, and every moving payment uses
  \(K>k_{10}\).
- **\(K=k_{11}\):** included. The moving lower wall for \((11,1)\)
  equals the upper face, so the strict count excludes that channel.
- **Radial split faces:** at \(x=16\), the strict ball wall (13) excludes
  every third channel \(p\geq2\); at \(x=34\), the strict ball wall
  (15) excludes every second channel \(p\geq5\).
- **Ratio faces:** equations (19) and (21) have positive reserves, so the
  mode defining a ratio row is absent at equality.
- **Fixed zero walls:** all three first-mode and both higher-radial walls
  are strict. Immediately above a wall, its full multiplicity is already
  present in the appropriate cap.
- **Bridge faces:** fixed and moving payments both hold at
  \(13/20,3/5,3/7\), with the displayed strict reserves.
- **Endpoints:** \(\rho=\rho_c\) is included and has the uniform strict
  reserve (29). The proof itself remains valid at \(\rho=7/8\); only the
  residual subtraction excludes that already-owned endpoint.
- **Seam and upper face:** the seam at \(5/6\) only changes the inherited
  upper-floor owner. Equation (39) controls both branches, and \(K=U\)
  is not subtracted.
- **Source scope:** Lorch is used only for the first zero at order
  \(21/2\). The third order-\(5/2\) and second order-\(11/2\) zero bounds
  are internal. No shell cross-product zero or uncertified decimal is
  imported.

Coincident entry walls only remove modes under the strict count. Every
cap contains complete multiplicities, and no cap is carried past a
frequency wall without its full update.

## 11. Verdict

The exact analytic route is **PASS through \(k_{11}\)**. The two internal
higher-radial walls reduce the inventory to first channels through ten,
second channels through four, and third channels through one. The new
qualified first wall pays the sole \(H=10\) cap. Every simultaneous-mode
cap, ratio face, moving bridge, endpoint, and seam is owned, and
\(k_{11}<U\) is strict.

The largest closed extension established by this note is

\[
 \boxed{m=11.}
\]

This note remains exploratory. It must not be treated as frozen or
promoted without a proof-free claim freeze, clean-room reconstruction,
independent exact-constant verification, adversarial review, and a State
Patch audit.
