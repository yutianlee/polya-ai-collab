# Round 20 exploration: direct-Lorch extension through \(k_8\)

Status: **PASS through \(k_8\); largest supported index \(m=8\);
exploratory only; not frozen or promoted**.

Date: 2026-07-14.

This note starts from the separate Round 20 proof through \(k_7\).  It
tests direct exact-order specializations of Lorch's published first-zero
inequality and proves one further closed high-ratio band.  It does not
edit or enlarge any Round 19 artifact.

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
 z_\rho\leq K\leq k_8(\rho)}
 \quad\Longrightarrow\quad
 \boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K)}.
 \tag{2}
\]

The predecessor owns the closed part through \(k_7\).  The genuinely new
set proved here is therefore

\[
 \boxed{
 \mathcal C_{20}^{\mathrm{H,L}}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_7(\rho)<K\leq k_8(\rho)\right\}.}
 \tag{3}
\]

If both Round 20 high-ratio steps are independently reconstructed and
promoted, the high component of the residual becomes

\[
 \boxed{
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac78,\quad
 k_8(\rho)<K<U(\rho)\right\}.}
 \tag{4}
\]

No lower-ratio component is changed by this note.

## 2. Dependency and provenance ledger

| input | SHA-256 | exact use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/high-next-wall.md` | `d7bb58554cf7505bc18415415b1ab21fa233b1707d9685b0a48bb58bbb2ab8a2` | predecessor through \(k_7\); internal \(j_{5/2,2}>9\) proof |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` | direct Lorch specializations at orders \(13/2,15/2,17/2\) |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` | internal \(j_{3/2,2}>77/10\) proof |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | channel decomposition, multiplicity, strict count |

The Lorch source supplies only unit-ball **first-zero** inequalities.  All
shell comparisons below are separate internal min--max arguments.

After the unitary radial transformation, put \(d_\ell=\ell(\ell+1)\)
and let \(q_{\ell,n}\) be the shell frequency in channel \(\ell\), radial
index \(n\).  The accepted fixed-channel comparisons are

\[
 \boxed{q_{\ell,n}^2\geq n^2z^2+d_\ell,\qquad q_{0,n}=nz,}
 \tag{5}
\]

\[
 \boxed{q_{\ell,n}^2\geq j_{\ell+1/2,n}^2,}
 \tag{6}
\]

and, on the unit ball, for \(p\geq\ell\),

\[
 \boxed{j_{p+1/2,n}^2
 \geq j_{\ell+1/2,n}^2+d_p-d_\ell.}
 \tag{7}
\]

Equations (5)--(7) follow from form ordering and min--max in a fixed
angular subspace.  None is attributed to Lorch.

The exact zero consequences used in the proof are

\[
 \boxed{
 q_{6,1}>c_6:=\frac{39}{4},\qquad
 q_{7,1}>c_7:=\frac{54}{5},}
 \tag{8}
\]

from the new source card, and

\[
 \boxed{
 q_{1,2}>\frac{77}{10},\qquad
 q_{2,2}>9.}
 \tag{9}
\]

The second inequality in (9) is the predecessor's internal
spherical-Bessel argument.  Applying (7) from \(\ell=2\) gives, for
every \(p\geq2\),

\[
 q_{p,2}^2>81+d_p-6=75+d_p.
 \tag{10}
\]

In particular

\[
 q_{3,2}^2>87>\left(\frac{93}{10}\right)^2,
 \tag{11}
\]

where the final squared reserve is \(51/100\).  The inherited first
\(\ell=5\) threshold is

\[
 q_{5,1}>c_5:=\frac{17}{2}.
 \tag{12}
\]

## 3. Exhaustive spectral inventory through \(k_8\)

Put \(x=z^2\).  On the high-ratio interval,

\[
 z\geq z_{\rho_c}=\pi+\frac12>\frac72,
 \qquad x>\frac{49}{4}.
 \tag{13}
\]

Assume \(K\leq k_8\), so \(K^2\leq x+72\).

Every \(n\geq3\) mode is absent, since (5) gives

\[
 q_{\ell,n}^2-K^2
 \geq9x+d_\ell-(x+72)
 >8\frac{49}{4}-72=26.
 \tag{14}
\]

Every first mode with \(\ell\geq8\) is absent because
\(d_\ell\geq72\).  At \(\ell=8\) and \(K=k_8\), equality in the moving
lower bound still leaves the mode uncounted.

For a second mode with \(\ell\geq4\), (5) and (10) give

\[
 q_{\ell,2}^2\geq4x+d_\ell,
 \qquad q_{\ell,2}^2>75+d_\ell.
 \tag{15}
\]

If \(x\leq d_\ell+3\), the second bound is at least \(x+72\).  If
\(x>d_\ell+3\), the first bound exceeds \(x+72\), because

\[
 3x+d_\ell-72
 >4d_\ell-63\geq17.
\]

Thus all such modes are absent, including both crossing faces.  The
complete possible inventory is exactly bounded by

\[
 \boxed{
 (\ell,1),\ 0\leq\ell\leq7;\qquad
 (\ell,2),\ 0\leq\ell\leq3.}
 \tag{16}
\]

No third radial mode or omitted angular multiplicity can occur below the
closed face \(K=k_8\).

## 4. Ratio localization and simultaneous-mode restrictions

If a second mode \((h,2)\) is counted, (5) and the upper face give

\[
 4x+d_h<K^2\leq x+72,
 \qquad 3x<72-d_h.
 \tag{17}
\]

Hence any second mode forces \(x<24\); \((2,2)\) forces \(x<22\); and
\((3,2)\) forces \(x<20\).  The exact lower bound
\(\pi>333/106\) gives

\[
\begin{aligned}
 z_{3/8}^2-24&>\frac{88824}{70225}>0,\\
 z_{1/3}^2-22&>\frac{9233}{44944}>0,\\
 z_{3/10}^2-20&>\frac{19405}{137641}>0.
\end{aligned}
 \tag{18}
\]

Therefore

\[
\begin{array}{c|c}
 \text{counted radial category}&\text{forced ratio range}\\ \hline
 \text{some second mode}&\rho<3/8\\
 (2,2)&\rho<1/3\\
 (3,2)&\rho<3/10.
\end{array}
 \tag{19}
\]

There is one additional incompatibility.  If \((6,1)\) is counted, (8)
and the upper face imply

\[
 x\geq K^2-72>\frac{1521}{16}-72=\frac{369}{16}>23.
 \tag{20}
\]

This contradicts \(x<22\) whenever \((2,2)\) is counted.  Thus a counted
\((6,1)\) can coexist only with the second modes \((0,2)\) and
\((1,2)\), never with \((2,2)\) or \((3,2)\).

## 5. Complete multiplicity caps

Let \(H\) be the largest counted first angular index, grouped as
\(H=7\), \(H=6\), \(H=5\), or \(H\leq4\).  If a second mode is present,
let \(h\) be its largest angular index.  Bounding all lower channels as
present is safe and gives the following complete caps:

| first category | no second mode | \(h=0\) | \(h=1\) | \(h=2\) | \(h=3\) |
|---|---:|---:|---:|---:|---:|
| \(H=7\) | 64 | 65 | 68 | 73 | 80 |
| \(H=6\) | 49 | 50 | 53 | impossible | impossible |
| \(H=5\) | 36 | 37 | 40 | 45 | 52 |
| \(H\leq4\) | 25 | 26 | 29 | 34 | 41 |

The entries use

\[
 \sum_{\ell=0}^{H}(2\ell+1)=(H+1)^2,
 \qquad
 \sum_{\ell=0}^{h}(2\ell+1)=(h+1)^2.
 \tag{21}
\]

Thus every displayed cap already contains each complete multiplicity.
Equation (20) owns the two impossible cells.

## 6. Monotonic payment facts

At a fixed positive wall \(c\), \(\mathcal W(\rho,c)\) is strictly
decreasing in \(\rho\).  Put

\[
 F_7(\rho)=\mathcal W(\rho,k_7(\rho)).
\]

The sign of its derivative is the sign of

\[
 \pi^2(1+\rho)-56\rho^2(1-\rho)^2
 >9-\frac{56}{16}=\frac{11}{2}>0.
 \tag{22}
\]

Hence \(F_7\) is strictly increasing.  We repeatedly use

\[
 \frac{2}{9\pi}>\frac7{99},
 \tag{23}
\]

which follows from \(\pi<22/7\).

There is a uniform base payment in the new band.  Since
\(\rho_c>1/8\), \(F_7\) is increasing, and \(k_7(1/8)>8\),

\[
 \mathcal W(\rho,K)>F_7(\rho)>F_7(1/8)
 >\frac7{99}\frac{511}{512}\,8^3
 =\frac{3577}{99}>26.
 \tag{24}
\]

Here \(\rho_c>1/8\) follows from \(\pi<7/2\), while
\(k_7(1/8)>8\) follows already from \(\pi>3\).

## 7. Exact payment of every cap

### 7.1 Highest first channel \(H=7\)

If a second mode is present, (19) gives \(\rho<3/8\), while (8) gives
\(K>54/5\).  The largest cap is 80, and

\[
 \mathcal W\left(\frac38,\frac{54}{5}\right)
 >\frac{1484973}{17600}
 =80+\frac{76973}{17600}.
 \tag{25}
\]

Thus all four radial columns in the \(H=7\) row are paid.

If no second mode is present, the cap is 64.  Split at \(\rho=3/5\).
The fixed payment is

\[
 \mathcal W\left(\frac35,\frac{54}{5}\right)
 >\frac{12002256}{171875}
 =64+\frac{1002256}{171875}.
 \tag{26}
\]

At the split, \(\pi>333/106\) gives

\[
 k_7(3/5)^2-\left(\frac{54}{5}\right)^2
 >\frac{1170521}{1123600}>0.
 \tag{27}
\]

Fixed-wall decrease controls \(\rho\leq3/5\), while (22), (26)--(27),
and \(K>k_7\) control \(\rho\geq3/5\).

### 7.2 Highest first channel \(H=6\)

With a second mode, only \(h\leq1\) is possible by (20), so the largest
cap is 53.  Equations (8) and (19) give \(K>39/4\) and \(\rho<3/8\), and

\[
 \mathcal W\left(\frac38,\frac{39}{4}\right)
 >\frac{22376445}{360448}
 =53+\frac{3272701}{360448}.
 \tag{28}
\]

With no second mode, the cap is 49.  Split at \(\rho=1/2\).  One has

\[
 \mathcal W\left(\frac12,\frac{39}{4}\right)
 >\frac{322959}{5632}
 =49+\frac{46991}{5632},
 \tag{29}
\]

and

\[
 k_7(1/2)^2-\left(\frac{39}{4}\right)^2
 >\frac{18599}{44944}>0.
 \tag{30}
\]

The same fixed/moving split argument pays 49 on both closed sides.

### 7.3 Highest first channel \(H=5\)

If \(h=3\), then (11) gives \(K>93/10\), (19) gives
\(\rho<3/10\), and

\[
 \mathcal W\left(\frac3{10},\frac{93}{10}\right)
 >\frac{608719503}{11000000}
 =52+\frac{36719503}{11000000}.
 \tag{31}
\]

If \(h=2\), then \(K>9\), \(\rho<1/3\), and

\[
 \mathcal W\left(\frac13,9\right)
 >\frac{546}{11}
 =45+\frac{51}{11}.
 \tag{32}
\]

If \(h\leq1\), the cap is at most 40.  The first \(\ell=5\) mode gives
\(K>17/2\), any second mode gives \(\rho<3/8\), and

\[
 \mathcal W\left(\frac38,\frac{17}{2}\right)
 >\frac{16679635}{405504}
 =40+\frac{459475}{405504}.
 \tag{33}
\]

Finally, with no second mode, the cap is 36.  Split at \(\rho=1/2\):

\[
 \mathcal W\left(\frac12,\frac{17}{2}\right)
 >\frac{240737}{6336}
 =36+\frac{12641}{6336},
 \tag{34}
\]

while \(k_7(1/2)^2>(17/2)^2\) follows already from \(\pi>3\).
Fixed-wall decrease and increasing \(F_7\) again cover the two sides.

### 7.4 Highest first channel \(H\leq4\)

For \(h=3\), (31) pays 52 and hence the smaller cap 41.  For \(h=2\),
(32) pays 45 and hence cap 34.

For \(h=1\), (9) and (19) give \(K>77/10\) and \(\rho<3/8\).  Thus

\[
 \mathcal W\left(\frac38,\frac{77}{10}\right)
 >\frac{28180537}{921600}
 =29+\frac{1454137}{921600}.
 \tag{35}
\]

If only \((0,2)\) is present, then \(K>2z\).  The exact moving payment

\[
 G_0(\rho)=\mathcal W(\rho,2z)
 =\frac{16\pi^2}{9}\frac{1+\rho+\rho^2}{(1-\rho)^2}
\]

is increasing, and at \(\rho_c\)

\[
 G_0(\rho_c)=\frac{16\pi^2+24\pi+12}{9}
 >\frac{153196}{5625}>26.
 \tag{36}
\]

The last inequality uses \(\pi>157/50\), which follows from
\(333/106>157/50\).  If no second mode is present, the cap is at most 25
and the uniform base payment (24) applies.

Sections 7.1--7.4 pay every cell of the exhaustive cap table.  Therefore
the genuinely new band (3) is proved.  Combining it with the predecessor
through \(k_7\) proves (2).

## 8. Exact containment below the inherited upper floor

For \(\rho\leq7/8\), \(z\leq8\pi<176/7\), and hence

\[
 27^2-k_8(\rho)^2
 >27^2-\left(\frac{176}{7}\right)^2-72
 =\frac{1217}{49}>0.
 \tag{37}
\]

Thus \(k_8<27\).  On \(\rho_c\leq\rho<5/6\), the inherited central
floor satisfies \(K_0>64\).  On the seam branch,

\[
 U(\rho)=\frac{54}{(1-\rho)^2}\geq1944.
\]

Consequently

\[
 \boxed{k_8(\rho)<U(\rho)
 \qquad(\rho_c\leq\rho<7/8).}
 \tag{38}
\]

The subtraction (4) therefore stays inside the inherited residual.

## 9. Equality, seam, and wall-order audit

- **\(K=k_7\):** the predecessor owns this complete closed face.  It is
  excluded from (3), and every new-band moving payment uses \(K>k_7\).
- **\(K=k_8\):** included.  The moving lower wall for \((8,1)\) equals
  the upper face, so strict counting excludes that channel.  Equations
  (14)--(16) remain valid at equality.
- **Lorch walls \(39/4,54/5\):** the corresponding shell frequencies are
  strictly larger than these values.  At equality the mode is absent; an
  enlarged cap is used only when \(K\) is strictly above its wall.
- **Second-mode walls:** equality in \(4z^2+d_h=K^2\), \(K=77/10\),
  \(K=9\), or \(K=93/10\) leaves the relevant mode uncounted.  Immediately
  above, its full multiplicity is already present in the table.
- **Inventory crossings in (15):** both alternatives exclude the mode on
  the shared face.  No ordering is assumed outside the exhaustive split.
- **Ratio faces \(3/10,1/3,3/8\):** the corresponding radial branch is
  empty there by the strict localizations (17)--(19).  No boundary point
  is lost.
- **Payment splits \(1/2,3/5\):** fixed and moving estimates both hold on
  the split face, with the positive reserves (27) and (30).
- **\(\rho=\rho_c\):** included.  The uniform reserve (24) is strict.
- **\(\rho=7/8\):** included in the closed theorem (2), but excluded from
  the residual subtraction (3), consistently with its inherited endpoint
  owner.
- **\(\rho=5/6\) and \(K=U\):** only the upper-floor owner changes.  The
  strict separation (38) controls both branches; \(K=U\) is not
  subtracted.

Coincident entry walls can only omit modes under the strict count.  Every
cap contains complete multiplicities, and no cap is carried across a
frequency wall without its full update.

## 10. The exact first obstruction toward \(k_9\)

The new source card also audits the next angular specialization

\[
 j_{17/2,1}>\frac{71}{6}.
 \tag{39}
\]

Thus the first \(\ell=8\) wall is not the obstruction.  For example, in
the no-second-mode branch the cap 81 is paid at the split \(\rho=2/3\).
Indeed, \(\rho\mapsto\mathcal W(\rho,k_8(\rho))\) is increasing because
its derivative test is bounded below by \(9-72/16=9/2>0\), while

\[
 \mathcal W\left(\frac23,\frac{71}{6}\right)
 >\frac{47602163}{577368}
 =81+\frac{835355}{577368},
\]

and

\[
 k_8(2/3)^2-\left(\frac{71}{6}\right)^2
 >\frac{525692}{25281}>0.
 \tag{40}
\]

The continuation instead fails earlier at a combined lower-angular,
second-radial face.  Take the exact witness

\[
 \rho_0=\frac{27}{100},\qquad x_0=z_{\rho_0}^2.
\]

It lies in the high-ratio interval because
\(\rho_c<1/7<27/100<7/8\).

The inherited bounds on \(\pi\) give

\[
 16<x_0<\left(\frac{2200}{511}\right)^2<\frac{75}{4},
 \qquad
 \frac{75}{4}-\left(\frac{2200}{511}\right)^2
 =\frac{224075}{1044484}>0.
 \tag{41}
\]

Use the **full**, rather than rationally weakened, Lorch square at
\(\ell=6\):

\[
 C_6^2=45\sqrt6-15.
\]

The sign-safe bounds

\[
 \frac{22}{9}<\sqrt6<\frac{49}{20}
\]

give

\[
 95<C_6^2<\frac{381}{4},
 \qquad C_6<\frac{49}{5}.
 \tag{42}
\]

Equations (41)--(42) place this strongest available first-\(\ell=6\)
wall strictly inside the prospective band:

\[
 k_7(\rho_0)^2=x_0+56<C_6^2<x_0+90=k_9(\rho_0)^2.
 \tag{43}
\]

At the same witness, every currently certified lower wall for the second
modes \(0\leq\ell\leq4\) lies below \(C_6\).  Indeed, the largest moving
square is

\[
 4x_0+d_4<4\frac{75}{4}+20=95<C_6^2,
\]

and the largest available ball-shift square is

\[
 75+d_4=95<C_6^2.
\]

Therefore the present information must allow, immediately above the
strongest Lorch wall, the complete cap

\[
 \underbrace{\sum_{\ell=0}^{6}(2\ell+1)}_{49}
 +\underbrace{\sum_{\ell=0}^{4}(2\ell+1)}_{25}
 =74.
 \tag{44}
\]

But even the Weyl term at that full wall is below 66.  From
\(\pi>333/106\), (42), and exact arithmetic,

\[
\begin{aligned}
 \mathcal W(\rho_0,C_6)
 &<\frac{212}{2997}
 \left(1-\left(\frac{27}{100}\right)^3\right)
 \left(\frac{49}{5}\right)^3\\
 &=\frac{6112665680849}{93656250000}
 <66<74,
\end{aligned}
 \tag{45}
\]

where

\[
 66-\frac{6112665680849}{93656250000}
 =\frac{68646819151}{93656250000}>0.
\]

This is a method obstruction, not a counterexample: the true second
shell modes can enter later than the lower walls used in (44).  It shows
that direct first-zero Lorch specializations, the present second-zero
facts, and the current individual min--max comparisons cannot by
themselves justify the \(k_9\) continuation.  A sharper second-radial
bound (already by angular channel \(\ell=4\)), a genuinely stronger
shell radial estimate, or a different coupled payment mechanism is
required.  The order-\(17/2\) first-zero bound (39) cannot repair this
earlier cap-74 face.

## 11. Verdict

The direct exact-order Lorch route is **PASS through \(k_8\)**.  The
largest rigorously supported closed extension with the declared toolkit
is

\[
 \boxed{m=8.}
\]

All first, second, and higher radial possibilities have been audited;
every angular multiplicity and combined cap is paid; \(k_8<U\) is
strict; and every frequency, ratio, endpoint, and seam face has an owner.

The first unsupported continuation is the exact cap-74 configuration
(41)--(45) inside the prospective \(k_9\) band.  This note remains
exploratory and must not be treated as frozen or promoted without a
proof-free claim freeze, clean-room reconstruction, independent constant
verification, adversarial review, and a State Patch audit.
