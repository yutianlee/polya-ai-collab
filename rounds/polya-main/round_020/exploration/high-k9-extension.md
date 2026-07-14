# Round 20 exploration: repaired high-ratio extension through \(k_9\)

Status: **PASS through \(k_9\); largest supported index \(m=9\) with
the declared exact toolkit; exploratory only; not frozen or promoted**.

Date: 2026-07-14.

This note repairs the precise second-radial obstruction left by the
separate proof through \(k_8\). It uses a new internal proof of
\(j_{7/2,2}>10\), reconstructs the complete prospective \(k_9\)
inventory, pays every combined cap, and then identifies the first exact
current-toolkit obstruction toward \(k_{10}\). It does not edit or enlarge
any Round 19 artifact.

## 1. Claim and exact prospective subtraction

Write

\[
 \rho_c=\frac1{1+2\pi},\qquad
 z=z_\rho=\frac{\pi}{1-\rho},\qquad
 k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
\]

and

\[
 \mathcal W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
 \tag{1}
\]

The closed exploratory theorem is

\[
 \boxed{
 \rho_c\leq\rho\leq\frac78,\qquad
 z_\rho\leq K\leq k_9(\rho)}
 \quad\Longrightarrow\quad
 \boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
 \tag{2}
\]

The predecessor owns the closed part through \(k_8\). The genuinely new
set proved here is

\[
 \boxed{
 \mathcal C_{20}^{\mathrm{H},9}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_8(\rho)<K\leq k_9(\rho)\right\}.}
 \tag{3}
\]

If the Round 20 high-ratio chain is independently reconstructed and
promoted, the exact high component of the residual becomes

\[
 \boxed{
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_9(\rho)<K<U(\rho)\right\}.}
 \tag{4}
\]

No lower-ratio component is changed by this note.

## 2. Dependency and provenance ledger

| input | SHA-256 | exact use |
|---|---|---|
| rounds/polya-main/round_020/exploration/high-lorch-extension.md | 30aea82a3278683bdaf0c8d98b24b82276568d5d42435841833d79f4670f811c | predecessor through \(k_8\), fixed-wall payment lemmas, full Lorch squares |
| sources/round20_higher_radial_zero_bounds.md | 8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7 | internal \(j_{7/2,2}>10\) proof and angular propagation |
| sources/round20_bessel_zero_bounds.md | 2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3 | exact first-zero walls in channels \(6,7,8\) |
| sources/round19_bessel_zero_bounds.md | 7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f | \(q_{5,1}>17/2\) and \(q_{1,2}>77/10\) inputs |
| rounds/polya-main/round_020/exploration/high-next-wall.md | d7bb58554cf7505bc18415415b1ab21fa233b1707d9685b0a48bb58bbb2ab8a2 | internal \(q_{2,2}>9\) proof |
| state/lemma_packets/SHELL-sturm-liouville-completeness.md | 6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8 | channel decomposition, multiplicity, strict spectral count |

No numerical zero table is used. The new source card labels the two DLMF
identities it inherits and proves all of its root localization internally.
Lorch supplies only unit-ball first-zero inequalities. Every shell
comparison below is an internal min--max statement.

## 3. Internal channel comparisons and exact zero consequences

Put

\[
 x=z^2,\qquad d_\ell=\ell(\ell+1),
\]

and let \(q_{\ell,n}\) be the shell frequency in channel \(\ell\), radial
index \(n\). Fixed-channel form ordering gives

\[
 \boxed{q_{\ell,n}^2\geq n^2x+d_\ell,\qquad q_{0,n}=nz.}
 \tag{5}
\]

Zero extension into the unit ball and angular form ordering give

\[
 \boxed{q_{\ell,n}^2\geq j_{\ell+1/2,n}^2,}
 \tag{6}
\]

and, for \(p\geq\ell\),

\[
 \boxed{
 j_{p+1/2,n}^2
 \geq j_{\ell+1/2,n}^2+d_p-d_\ell.}
 \tag{7}
\]

The first-mode walls needed for the cap ledger are

\[
 \boxed{
 q_{5,1}>\frac{17}{2},\quad
 q_{6,1}>\frac{39}{4},\quad
 q_{7,1}>\frac{54}{5},\quad
 q_{8,1}>\frac{71}{6}.}
 \tag{8}
\]

The second-mode walls are

\[
 \boxed{
 q_{1,2}>\frac{77}{10},\qquad
 q_{2,2}>9,\qquad
 q_{3,2}>10.}
 \tag{9}
\]

The new internal proof also gives, for every \(p\geq3\),

\[
 \boxed{q_{p,2}^2>88+d_p.}
 \tag{10}
\]

In particular,

\[
 q_{4,2}^2>108,\qquad
 q_{5,2}^2>118,\qquad
 q_{6,2}^2>130.
 \tag{11}
\]

The old obstruction just above the first \(\ell=6\) wall allowed second
channels through \(\ell=4\). Equations (9)--(11) now exclude channels
\(3\) and \(4\) there: the former lies above \(10\), and the latter lies
above \(\sqrt{108}\). This is the exact repair, not a numerical
approximation to the true shell zeros.

## 4. Exhaustive spectral inventory through \(k_9\)

On the high-ratio interval,

\[
 z\geq z_{\rho_c}=\pi+\frac12>\frac72,
 \qquad x>\frac{49}{4}.
 \tag{12}
\]

Assume \(K\leq k_9\), so \(K^2\leq x+90\). Every mode with \(n\geq3\)
is absent, because

\[
 q_{\ell,n}^2-K^2
 \geq9x+d_\ell-(x+90)
 >8\frac{49}{4}-90=8.
 \tag{13}
\]

Every first mode with \(\ell\geq9\) is absent by (5), since
\(d_\ell\geq90\). At \(\ell=9\) and \(K=k_9\), equality in the moving
lower bound still leaves the mode uncounted under the strict count.

It remains to control second modes. For \(\ell\geq5\), equation (10)
and the moving comparison give

\[
 q_{\ell,2}^2\geq4x+d_\ell,
 \qquad
 q_{\ell,2}^2>88+d_\ell.
 \tag{14}
\]

If \(x\leq d_\ell-2\), the second bound is strictly at least \(x+90\).
If \(x>d_\ell-2\), then

\[
 4x+d_\ell-(x+90)
 =3x+d_\ell-90
 >4d_\ell-96\geq24.
\]

Thus every second mode with \(\ell\geq5\) is absent, including the
crossing face \(x=d_\ell-2\). The complete possible inventory is

\[
 \boxed{
 (\ell,1),\ 0\leq\ell\leq8;\qquad
 (\ell,2),\ 0\leq\ell\leq4.}
 \tag{15}
\]

No third radial mode, omitted second mode, or omitted angular
multiplicity can occur below the closed face \(K=k_9\).

## 5. Exact ratio localization

If a second mode \((h,2)\) is counted, (5) and the upper face imply

\[
 4x+d_h<K^2\leq x+90,
 \qquad
 3x<90-d_h.
 \tag{16}
\]

The following table converts each strict \(x\)-bound into a rational
ratio cutoff. At the displayed ratio \(r_h\), the lower enclosure
\(\pi>333/106\) gives the exact positive reserve shown in the last
column.

| \(h\) | forced \(x<(90-d_h)/3\) | \(r_h\) | \(z(r_h)^2-(90-d_h)/3\) |
|---:|---:|---:|---:|
| 0 | \(30\) | \(3/7\) | \(40281/179776\) |
| 1 | \(88/3\) | \(3/7\) | \(480395/539328\) |
| 2 | \(28\) | \(5/12\) | \(138056/137641\) |
| 3 | \(26\) | \(2/5\) | \(15889/11236\) |
| 4 | \(70/3\) | \(7/20\) | \(36230/1424163\) |

Since \(z_\rho\) is strictly increasing, a counted \((h,2)\) therefore
forces

\[
 \boxed{\rho<r_h.}
 \tag{17}
\]

Every ratio face in the table is empty for the corresponding mode; no
boundary point is assigned to the wrong payment branch.

## 6. Simultaneous-mode restrictions and complete cap table

If the first \(\ell=8\) mode is counted, (8) and \(K^2\leq x+90\)
give

\[
 x>\left(\frac{71}{6}\right)^2-90
 =\frac{1801}{36}>30.
 \tag{18}
\]

This contradicts even the weakest second-mode condition in (16).
Hence a counted \((8,1)\) can coexist with no second mode.

If the first \(\ell=7\) mode is counted, then

\[
 x>\left(\frac{54}{5}\right)^2-90
 =\frac{666}{25}.
 \tag{19}
\]

The gaps from the \(h=3\) and \(h=4\) upper bounds are respectively

\[
 \frac{666}{25}-26=\frac{16}{25}>0,
 \qquad
 \frac{666}{25}-\frac{70}{3}=\frac{248}{75}>0.
\]

Thus a counted \((7,1)\) can coexist only with \(h\leq2\).

Let \(H\) be the largest counted first angular index and, when a second
mode is present, let \(h\) be its largest angular index. Bounding every
lower channel as present gives the exhaustive caps

| first category | no second | \(h=0\) | \(h=1\) | \(h=2\) | \(h=3\) | \(h=4\) |
|---|---:|---:|---:|---:|---:|---:|
| \(H=8\) | 81 | impossible | impossible | impossible | impossible | impossible |
| \(H=7\) | 64 | 65 | 68 | 73 | impossible | impossible |
| \(H=6\) | 49 | 50 | 53 | 58 | 65 | 74 |
| \(H=5\) | 36 | 37 | 40 | 45 | 52 | 61 |
| \(H\leq4\) | 25 | 26 | 29 | 34 | 41 | 50 |

Indeed,

\[
 \sum_{\ell=0}^{H}(2\ell+1)=(H+1)^2,\qquad
 \sum_{\ell=0}^{h}(2\ell+1)=(h+1)^2.
 \tag{20}
\]

Every table entry contains full angular multiplicities. Equations
(18)--(19) own every impossible cell.

## 7. Monotonic payment facts

At a fixed positive wall \(c\), \(\mathcal W(\rho,c)\) is strictly
decreasing in \(\rho\). Also

\[
 \frac{2}{9\pi}>\frac7{99},
 \tag{21}
\]

because \(\pi<22/7\).

Put

\[
 F_8(\rho)=\mathcal W(\rho,k_8(\rho)).
\]

The sign of its derivative is the sign of

\[
 \pi^2(1+\rho)-72\rho^2(1-\rho)^2
 >9-\frac{72}{16}=\frac92>0.
 \tag{22}
\]

Hence \(F_8\) is strictly increasing.

## 8. Exact payment with no second mode

The rows \(H\leq7\) are already paid by the predecessor's stronger
no-second-mode estimates, which require only \(K>k_7\). Here
\(K>k_8>k_7\). For completeness, their exact reserves are:

\[
\begin{array}{c|c|c}
\text{category}&\text{cap}&\text{predecessor payment}\\ \hline
H=7&64&
\mathcal W(3/5,54/5)>
12002256/171875=64+1002256/171875\\
H=6&49&
\mathcal W(1/2,39/4)>
322959/5632=49+46991/5632\\
H=5&36&
\mathcal W(1/2,17/2)>
240737/6336=36+12641/6336\\
H\leq4&25&
\mathcal W>3577/99>26.
\end{array}
 \tag{23}
\]

The fixed/moving bridges are respectively at \(3/5,1/2,1/2\); the
predecessor proves the required wall order there with strict reserves.

Only \(H=8\) is new. Its cap is 81 by (18). Split at \(\rho=2/3\).
Exact arithmetic gives

\[
 \mathcal W\left(\frac23,\frac{71}{6}\right)
 >\frac{47602163}{577368}
 =81+\frac{835355}{577368},
 \tag{24}
\]

and

\[
 k_8(2/3)^2-\left(\frac{71}{6}\right)^2
 >\frac{525692}{25281}>0.
 \tag{25}
\]

For \(\rho\leq2/3\), fixed-wall decrease and \(K>71/6\) pay 81. For
\(\rho\geq2/3\), equations (22), (24)--(25), and \(K>k_8\) pay 81.
Both estimates own the split face.

## 9. Exact payment when a second mode is present

The cap table can now be paid from its largest cells downward.

### 9.1 Highest second channel \(h=4\)

Equations (18)--(19) force \(H\leq6\), so the largest cap is 74. From
(10),

\[
 K^2>108>\left(\frac{207}{20}\right)^2,
 \qquad
 108-\left(\frac{207}{20}\right)^2=\frac{351}{400}.
\]

Together with \(\rho<7/20\), fixed-wall decrease gives

\[
 \mathcal W(\rho,K)>
 \mathcal W\left(\frac7{20},\frac{207}{20}\right)
 >\frac{52823261673}{704000000}
 =74+\frac{727261673}{704000000}.
 \tag{26}
\]

Thus all \(h=4\) cells are paid.

### 9.2 Highest second channel \(h=3\)

Again \(H\leq6\), so the largest cap is 65. Equations (9) and (17) give
\(K>10\) and \(\rho<2/5\). Therefore

\[
 \mathcal W(\rho,K)>
 \mathcal W\left(\frac25,10\right)
 >\frac{728}{11}
 =65+\frac{13}{11}.
 \tag{27}
\]

### 9.3 Highest second channel \(h=2\)

Here \(\rho<5/12\). The three possible first-channel categories are paid
as follows:

\[
\begin{array}{c|c|c|c}
\text{first category}&\text{cap}&\text{wall}&\text{payment lower bound}\\ \hline
H=7&73&54/5&
908901/11000=73+105901/11000\\
H=6&58&39/4&
24652537/405504=58+1133305/405504\\
H\leq5&45&9&
33663/704=45+1983/704.
\end{array}
 \tag{28}
\]

Each entry is \((7/99)(1-(5/12)^3)c^3\) at its displayed wall \(c\).

### 9.4 Highest second channel \(h=1\)

Now \(\rho<3/7\). The complete payments are

\[
\begin{array}{c|c|c|c}
\text{first category}&\text{cap}&\text{wall}&\text{payment lower bound}\\ \hline
H=7&68&54/5&
5528736/67375=68+947236/67375\\
H=6&53&39/4&
520689/8624=53+63617/8624\\
H=5&40&17/2&
388127/9702=40+47/9702\\
H\leq4&29&77/10&
66913/2250=29+1663/2250.
\end{array}
 \tag{29}
\]

The smallest reserve, \(47/9702\), is still exact and strictly positive.

### 9.5 Only the radial second mode \(h=0\)

For \(H=7,6,5\), the caps \(65,50,37\) are smaller than the corresponding
already-paid entries \(68,53,40\) in (29), using the same
\(\rho<3/7\) cutoff and the same first-mode wall.

If \(H\leq4\), the cap is 26 and the exact identity \(q_{0,2}=2z\)
applies. The moving payment

\[
 G_0(\rho)=\mathcal W(\rho,2z)
 =\frac{16\pi^2}{9}
 \frac{1+\rho+\rho^2}{(1-\rho)^2}
\]

is increasing, and the predecessor's exact endpoint evaluation gives

\[
 G_0(\rho_c)
 =\frac{16\pi^2+24\pi+12}{9}
 >\frac{153196}{5625}>26.
 \tag{30}
\]

Sections 8--9 pay every possible cell in the exhaustive cap table.
Therefore the genuinely new band (3), and hence the closed theorem (2),
are proved.

## 10. Exact containment below the inherited upper floor

For \(\rho\leq7/8\),

\[
 z\leq8\pi<\frac{176}{7}.
\]

Consequently

\[
 27^2-k_9(\rho)^2
 >27^2-\left(\frac{176}{7}\right)^2-90
 =\frac{335}{49}>0.
 \tag{31}
\]

Thus \(k_9<27\). On \(\rho_c\leq\rho<5/6\), the inherited central
floor is larger than 64. On the seam branch,

\[
 U(\rho)=\frac{54}{(1-\rho)^2}\geq1944.
\]

Hence

\[
 \boxed{k_9(\rho)<U(\rho)
 \qquad(\rho_c\leq\rho<7/8).}
 \tag{32}
\]

The subtraction (4) stays strictly inside the inherited residual.

## 11. Equality, endpoint, and wall-order audit

- **\(K=k_8\):** the predecessor owns this complete closed face. It is
  excluded from (3), and every new-band moving payment uses \(K>k_8\).
- **\(K=k_9\):** included. The moving lower wall for \((9,1)\) equals
  the upper face, so strict counting excludes that channel.
- **First- and second-zero walls:** all zero inequalities are strict.
  At equality the corresponding mode is absent; immediately above a
  declared lower wall, its full multiplicity is already included.
- **The crossing in (14):** at \(x=d_\ell-2\), the strict ball bound
  excludes the mode. On either side one of the two displayed comparisons
  is strict.
- **Ratio faces:** the mode defining a row of the localization table is
  absent at \(\rho=r_h\), because the table reserve is positive.
- **The \(H=8\) split:** fixed and moving payments both hold at \(2/3\),
  with the strict reserves (24)--(25).
- **\(\rho=\rho_c\):** included; every applicable fixed or moving
  payment above remains strict (with (30) owning the lowest moving
  cell). The closed theorem includes \(\rho=7/8\), while (3) excludes
  that already-owned endpoint.
- **The \(5/6\) seam and \(K=U\):** only the upper-floor owner changes.
  Equation (32) controls both branches, and \(K=U\) is not subtracted.

Coincident entry walls only omit modes under the strict count. Every cap
contains complete multiplicities, and no cap is carried past a declared
frequency wall without its full update.

## 12. Exact first current-toolkit obstruction toward \(k_{10}\)

The new second-radial bound proves \(k_9\), but the declared individual
lower-wall toolkit does not prove the next full band. This can be seen
without decimal arithmetic.

Take

\[
 \rho_0=\frac{13}{40},\qquad
 x_0=z_{\rho_0}^2=\left(\frac{40\pi}{27}\right)^2.
\]

This is an admissible high-ratio witness: \(\pi>3\) gives
\(\rho_c<1/7<13/40<7/8\).

The inherited enclosure for \(\pi\) gives

\[
 \left(\frac{740}{159}\right)^2<x_0
 <\left(\frac{880}{189}\right)^2,
\]

and hence

\[
 x_0-21>\frac{16699}{25281}>0,\qquad
 22-x_0>\frac{11462}{35721}>0.
 \tag{33}
\]

Use the full available Lorch square in channel \(7\),

\[
 C_7^2=\frac{153\sqrt{13}-85}{4}.
 \tag{34}
\]

The source audit proves \(C_7>54/5\). Also
\(\sqrt{13}<361/100\), since
\((361/100)^2-13=321/10000\), and therefore

\[
 C_7^2<\frac{46733}{400}
 <\left(\frac{1081}{100}\right)^2,
\]

where the last squared reserve is \(59/2500\). Equations (33)--(34)
place this strongest available first-\(\ell=7\) wall strictly inside the
prospective next band:

\[
 k_9(\rho_0)^2=x_0+90<112<C_7^2,
\]

and

\[
 C_7^2<117<131<x_0+110=k_{10}(\rho_0)^2.
 \tag{35}
\]

Before this wall, the complete conservative cap is 74:

\[
 \underbrace{\sum_{\ell=0}^{6}(2\ell+1)}_{49}
 +\underbrace{\sum_{\ell=0}^{4}(2\ell+1)}_{25}
 =74.
 \tag{36}
\]

Indeed, \(4x_0+d_4<108<C_7^2\), so every currently available moving or
ball lower face for second channels through \(\ell=4\) has already
passed. The new bound \(q_{5,2}^2>118>C_7^2\) excludes the next second
channel, while \(9x_0>189>C_7^2\) excludes every third mode. The first
\(\ell=8\) mode is excluded by \(q_{8,1}>71/6>C_7\).

This preceding cap is paid throughout the interval. From \(x_0>21\),

\[
 k_9(\rho_0)>\frac{21}{2},
\]

and hence

\[
 \mathcal W(\rho_0,K)>
 \frac7{99}\left(1-\left(\frac{13}{40}\right)^3\right)
 \left(\frac{21}{2}\right)^3
 =\frac{445167009}{5632000}
 =74+\frac{28399009}{5632000}.
 \tag{37}
\]

Once the declared first-\(\ell=7\) lower face has passed, a proof using
only the present individual lower bounds must allow its full multiplicity
15. The safe cap becomes

\[
 74+15=89.
 \tag{38}
\]

But even at the strongest available Lorch wall the Weyl payment is below
87. Using \(1/\pi<106/333\) and \(C_7<1081/100\),

\[
\begin{aligned}
 \mathcal W(\rho_0,C_7)
 &<
 \frac{212}{2997}
 \left(1-\left(\frac{13}{40}\right)^3\right)
 \left(\frac{1081}{100}\right)^3\\
 &=\frac{51083128779599}{592000000000}\\
 &=87-\frac{420871220401}{592000000000}
 <87<89.
\end{aligned}
 \tag{39}
\]

By continuity, the cap payment still fails on a right neighborhood of
this declared lower face. The strict inequality
\(q_{7,1}>C_7\) does **not** assert that the actual shell mode enters
immediately above \(C_7\); it supplies no quantified continuation past
that face. Thus (39) is a method obstruction, not a shell counterexample.
A substantially sharper first-\(\ell=7\) wall, a coupled exclusion of its
coexistence with the second channels, or a different counting/payment
mechanism is required for \(k_{10}\).

Along this exact witness, (37) pays the complete cap before \(C_7\), and
(39) is the first unsupported cap update. No earlier displayed wall is
being skipped.

## 13. Verdict

The repaired exact route is **PASS through \(k_9\)**. The largest closed
extension supported by the declared toolkit is

\[
 \boxed{m=9.}
\]

The internal tangent-cell proof of \(j_{7/2,2}>10\) removes the former
\(k_9\) cap-74 obstruction. Every first, second, and higher-radial
possibility through \(k_9\) is exhausted; every full multiplicity cap is
paid; \(k_9<U\) is strict; and each equality, ratio, endpoint, and seam
face has an owner.

The first unsupported continuation toward \(k_{10}\) is the exact cap-89
configuration (33)--(39). This note remains exploratory and must not be
treated as frozen or promoted without a proof-free claim freeze,
clean-room reconstruction, independent exact-constant verification,
adversarial review, and a State Patch audit.
