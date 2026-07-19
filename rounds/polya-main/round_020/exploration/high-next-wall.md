# Round 20 exploration: the next high-ratio wall

Status: **PASS through \(k_7\); exploratory only; not frozen or promoted**.

Date: 2026-07-14.

This note starts from the frozen Round 19 high-ratio face \(K=k_6\).  It
does not edit or enlarge any Round 19 artifact.  It proves the next closed
band using only the already authenticated zero inputs and internal
min--max or elementary arguments.

## 1. Candidate and exact high-ratio subtraction

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

The proposed closed extension is

\[
 \boxed{\rho_c\leq\rho\leq\frac78,\qquad
 z_\rho\leq K\leq k_7(\rho)}
 \quad\Longrightarrow\quad
 \boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
 \tag{2}
\]

Round 19 owns the closed part through \(k_6\).  The genuinely new set is
therefore exactly

\[
 \boxed{\mathcal C_{20}^{\mathrm H}
 =\left\{(\rho,K):\rho_c\leq\rho<\frac78,
 \quad k_6(\rho)<K\leq k_7(\rho)\right\}.}
 \tag{3}
\]

Once (2) is independently reconstructed and promoted, subtracting only
this high-ratio addition changes the high component of the residual to

\[
 \boxed{\left\{(\rho,K):\rho_c\leq\rho<\frac78,
 \quad k_7(\rho)<K<U(\rho)\right\}.}
 \tag{4}
\]

All lower-ratio Round 19 components are untouched by this note.

## 2. Allowed inputs and two internal comparisons

The already authenticated source inputs used here are:

| input | authenticated SHA-256 | use |
|---|---|---|
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | \(j_{5/2,1}>51/10\) |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` | exact \(j_{11/2,1}\) bound and \(j_{3/2,2}>77/10\) |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | channel decomposition, multiplicity, strict count |

No new external source is used.

After the unitary radial transformation, the shell form in angular
channel \(\ell\) is

\[
 a_\ell[u]=\int_\rho^1\left(|u'|^2+
 \frac{\ell(\ell+1)}{r^2}|u|^2\right)\,dr,
 \qquad D(a_\ell)=H_0^1(\rho,1).
\]

If \(q_{\ell,n}\) is the shell frequency, fixed-channel min--max and
\(r^{-2}\geq1\) give

\[
 \boxed{q_{\ell,n}^2\geq n^2z^2+\ell(\ell+1),}
 \qquad q_{0,n}=nz.
 \tag{5}
\]

Zero extension from \((\rho,1)\) to \((0,1)\) gives the same-index ball
comparison

\[
 \boxed{q_{\ell,n}^2\geq j_{\ell+1/2,n}^2.}
 \tag{6}
\]

On the unit ball, Hardy's inequality makes all transformed fixed-channel
form domains equal to \(H_0^1(0,1)\).  Hence, for \(p\geq\ell\),

\[
 \boxed{j_{p+1/2,n}^2\geq j_{\ell+1/2,n}^2
 +p(p+1)-\ell(\ell+1).}
 \tag{7}
\]

Both (6) and (7) are internal form comparisons, not new Bessel-zero
citations.

## 3. The two new zero consequences

### 3.1 The first \(\ell=6\) mode

The authenticated Round 19 specialization is

\[
 j_{11/2,1}^2>B,
 \qquad B:=\frac{507(\sqrt{77}-1)}{52}.
 \tag{8}
\]

Equation (7), with \(p=6\) and \(\ell=5\), therefore gives

\[
 j_{13/2,1}^2>B+12.
\]

Set

\[
 c_6:=\frac{234}{25}.
\]

This is a strict lower threshold.  Indeed,

\[
 B+12-c_6^2
 =\frac{507}{52}\left(\sqrt{77}-\frac{71133}{8125}\right)>0,
 \tag{9}
\]

because both sides of the radical comparison are positive and

\[
 77-\left(\frac{71133}{8125}\right)^2
 =\frac{23299436}{66015625}>0.
\]

Consequently

\[
 \boxed{q_{6,1}>c_6=\frac{234}{25}.}
 \tag{10}
\]

### 3.2 The second \(\ell=2\) and \(\ell=3\) modes

For completeness, the bound needed below is proved internally.  The
positive zeros of the spherical Bessel function

\[
 \mathsf j_2(x)=
 \frac{(3-x^2)\sin x-3x\cos x}{x^3}
\]

satisfy, for \(x>\sqrt3\),

\[
 \tan x=R(x):=-\frac{3x}{x^2-3}<0.
 \tag{11}
\]

Tangent poles, multiples of \(\pi\), and \(x=\sqrt3\) are not zeros of
the displayed numerator, so this division loses no zero in the range
being enumerated.

There are no roots on positive-tangent half-periods.  On every
negative-tangent half-period after \(x=3\), put \(F=\tan-R\).  Since

\[
 R'(x)=\frac{3(x^2+3)}{(x^2-3)^2}<1\leq\sec^2x
 \qquad(x>3),
\]

\(F\) is strictly increasing from \(-\infty\) to a positive value, so
there is exactly one root.  The authenticated first-zero bound
\(j_{5/2,1}>51/10\) excludes the only earlier negative half-period;
moreover

\[
 \frac{3\pi}{2}<\frac{51}{10}<2\pi
\]

by (12).  Hence the first positive root is the unique root in
\((3\pi/2,2\pi)\), and the second is the unique root in
\((5\pi/2,3\pi)\).

At \(x=9\), let \(y=3\pi-9\).  The exact bounds

\[
 \frac{333}{106}<\pi<\frac{22}{7}
 \tag{12}
\]

give \(0<y<\pi/2\) and

\[
 y>\frac{45}{106}>\frac9{26}.
\]

Therefore

\[
 \tan9=-\tan y<-y<-\frac9{26}=R(9),
\]

so the unique root lies to the right of 9:

\[
 \boxed{j_{5/2,2}>9.}
 \tag{13}
\]

Equation (7) also gives

\[
 \boxed{j_{7/2,2}^2>81+6=87.}
 \tag{14}
\]

## 4. Exhaustive inventory through \(k_7\)

Throughout \(\rho\geq\rho_c\),

\[
 z\geq z_{\rho_c}=\pi+\frac12>\frac72.
 \tag{15}
\]

Assume now that \(K\leq k_7\), so \(K^2\leq z^2+56\).

First, every \(n\geq3\) mode is absent, because

\[
 9z^2-(z^2+56)>8\left(\frac72\right)^2-56=42.
 \tag{16}
\]

Every second mode with \(\ell\geq4\) is absent, because

\[
 4z^2+20-(z^2+56)
 >3\left(\frac72\right)^2-36=\frac34.
 \tag{17}
\]

The second \(\ell=2\) mode is absent as well.  If
\(z^2\geq50/3\), then (5) gives

\[
 4z^2+6\geq z^2+56.
\]

If \(z^2\leq50/3\), then

\[
 K^2\leq z^2+56\leq\frac{218}{3}<81<j_{5/2,2}^2.
\]

At the common equality face, strict counting still excludes the mode.
Likewise, for the second \(\ell=3\) mode, use the two cases

\[
 z^2\geq\frac{44}{3}
 \quad\Longrightarrow\quad 4z^2+12\geq z^2+56,
\]

and

\[
 z^2\leq\frac{44}{3}
 \quad\Longrightarrow\quad
 K^2\leq\frac{212}{3}<87<j_{7/2,2}^2.
\]

Finally, every first mode with \(\ell\geq7\) is absent by (5), since
its moving lower wall is at least \(k_7\).  The complete possible
inventory is therefore

\[
 \boxed{(\ell,1),\ 0\leq\ell\leq6;\qquad
 (0,2),\ (1,2).}
 \tag{18}
\]

The first-mode cumulative caps are

\[
 25\quad(0\leq\ell\leq4),\qquad
 36\quad(0\leq\ell\leq5),\qquad
 49\quad(0\leq\ell\leq6).
 \tag{19}
\]

The two possible second modes add multiplicities \(1+3=4\).  No cap
below is carried through an entry wall without adding its complete
multiplicity.

There is also a useful exact ratio localization.  If any second mode is
counted, then (5), strict counting, and \(K\leq k_7\) imply

\[
 4z^2<K^2\leq z^2+56,
 \qquad 3z^2<56.
 \tag{20}
\]

But \(\rho\geq3/10\) would give

\[
 z^2\geq\left(\frac{10}{7}\frac{333}{106}\right)^2
 =\frac{56}{3}+\frac{608779}{412923}>\frac{56}{3}.
\]

Hence

\[
 \boxed{\hbox{any counted second mode forces }\rho<\frac3{10}.}
 \tag{21}
\]

## 5. Exact Weyl payments

For a moving wall \(T^2=az^2+b\), direct differentiation shows that
\(\mathcal W(\rho,T(\rho))\) is increasing whenever

\[
 a\pi^2(1+\rho)>b\rho^2(1-\rho)^2.
 \tag{22}
\]

This holds for \(k_6\) (\(a=1,b=42\)), because

\[
 \pi^2(1+\rho)-42\rho^2(1-\rho)^2
 >9-\frac{42}{16}=\frac{51}{8}>0,
\]

and for \(p_1=\sqrt{4z^2+2}\).  At fixed positive \(c\),
\(\mathcal W(\rho,c)\) is strictly decreasing in \(\rho\).

We repeatedly use

\[
 \frac{2}{9\pi}>\frac7{99},
 \tag{23}
\]

which follows from \(\pi<22/7\).

### 5.1 Base cap 26 above the old face

The new band has \(K>k_6\).  Since \(\rho_c>1/8\) and the moving
payment at \(k_6\) is increasing, it is enough to evaluate at \(1/8\).
Put

\[
 A_0=\frac{7555146}{137641},\qquad
 B_0=\frac{3577}{50688}.
\]

By (12) and (23),

\[
 \mathcal W\left(\frac18,k_6\left(\frac18\right)\right)
 >B_0A_0^{3/2}>26,
\]

where the last comparison is sign-safe and

\[
 B_0^2A_0^3-26^2
 =\frac{1906662783250496828695}
 {12918374118245105664}>0.
 \tag{24}
\]

Thus the base first-mode cap 25 and the cap 26 obtained by adding only
\((0,2)\) are both paid everywhere in the genuinely new band.

### 5.2 Cap 29 at the second \(\ell=1\) wall

If \((1,2)\) is counted, then

\[
 K>p_1(\rho)=\sqrt{4z^2+2},
 \qquad K>\frac{77}{10}.
 \tag{25}
\]

Split at \(\rho=1/5\).  The exact fixed payment is

\[
 \mathcal W\left(\frac15,\frac{77}{10}\right)
 >\frac{9006151}{281250}
 =29+\frac{849901}{281250}.
 \tag{26}
\]

At the split, (12) gives

\[
 p_1\left(\frac15\right)^2-\left(\frac{77}{10}\right)^2
 >\frac{4934581}{1123600}>0.
 \tag{27}
\]

For \(\rho\leq1/5\), fixed-wall monotonicity and (26) pay 29.  For
\(\rho\geq1/5\), the increasing moving payment at \(p_1\), together
with (26)--(27), pays 29.  Equality at either wall leaves the mode
uncounted.

### 5.3 Cap 36 when the first \(\ell=5\) mode is present

If \((5,1)\) is counted, then \(K>17/2\).  Split at \(\rho=3/7\).
On the fixed side,

\[
 \mathcal W\left(\frac37,\frac{17}{2}\right)
 >\frac{388127}{9702}
 =36+\frac{38855}{9702}.
 \tag{28}
\]

On the moving side, define

\[
 A_5=\frac{12984153}{179776},\qquad
 B_5=\frac{316}{4851}.
\]

Then

\[
 \mathcal W\left(\frac37,k_6\left(\frac37\right)\right)
 >B_5A_5^{3/2}>36,
\]

with exact squared reserve

\[
 B_5^2A_5^3-36^2
 =\frac{279281008839913330541}
 {922741008446078976}>0.
 \tag{29}
\]

Fixed-wall decrease controls \(\rho\leq3/7\); moving-wall increase and
the condition \(K>k_6\) control \(\rho\geq3/7\).  Both arguments are
strict on the split face.

### 5.4 Cap 49 when the first \(\ell=6\) mode is present

If \((6,1)\) is counted, then (10) gives \(K>c_6=234/25\).  Split at

\[
 r_6=\frac{107}{200}.
\]

The fixed payment is

\[
 \mathcal W\left(r_6,\frac{234}{25}\right)
 >\frac{8439557159943}{171875000000}
 =49+\frac{17682159943}{171875000000}.
 \tag{30}
\]

For the moving payment, put

\[
 A_6=\frac{236586858}{2699449},\qquad
 B_6=\frac{5269411}{88000000}.
\]

Then

\[
 \mathcal W(r_6,k_6(r_6))>B_6A_6^{3/2}>49,
\]

because

\[
 B_6^2A_6^3-49^2
 =\frac{254061581274155406101913080384629}
 {19814236859680322312000000000000}>0.
 \tag{31}
\]

Again the fixed wall controls \(\rho\leq r_6\), and the increasing
moving \(k_6\) wall controls \(\rho\geq r_6\).  Notice that (30)--(31)
avoid assuming any global ordering between \(c_6\) and \(k_6\).

### 5.5 Combined angular/radial caps 40 and 53

The previous payments cannot be carried unchanged when a second mode and
a new high angular mode occur together.  Equation (21) localizes every
such case to \(\rho<3/10\).

If \((5,1)\) is present, \((6,1)\) is absent, and at least one second
mode is present, the complete cap is

\[
 36+1+3=40.
\]

It is paid at the fixed \(17/2\) wall:

\[
 \mathcal W\left(\frac3{10},\frac{17}{2}\right)
 >\frac{33462443}{792000}
 =40+\frac{1782443}{792000}.
 \tag{32}
\]

If \((6,1)\) and at least one second mode are both present, the complete
cap is

\[
 49+1+3=53.
\]

It is paid at the fixed \(c_6\) wall:

\[
 \mathcal W\left(\frac3{10},\frac{234}{25}\right)
 >\frac{1212065127}{21484375}
 =53+\frac{73393252}{21484375}.
 \tag{33}
\]

The inequalities are strict because a present angular mode forces
\(K\) strictly above its strict fixed lower threshold.  At
\(\rho=3/10\), (21) excludes every second mode, so no equality case is
lost.

## 6. Proof of the new band

Take \(\rho_c\leq\rho\leq7/8\) and
\(k_6(\rho)<K\leq k_7(\rho)\).  Use the exhaustive inventory (18) and
classify by the highest new category present.

1. If \((6,1)\) is present and a second mode is present, the count is at
   most 53 and (33) pays it.  If no second mode is present, the count is
   at most 49 and (30)--(31) pay it.
2. If \((6,1)\) is absent but \((5,1)\) is present, a simultaneous
   second mode gives cap 40, paid by (32).  With no second mode the cap is
   36, paid by (28)--(29).
3. If both \((5,1)\) and \((6,1)\) are absent, presence of \((1,2)\)
   gives cap \(25+1+3=29\), paid by (26)--(27).  If only \((0,2)\) is
   present, the cap is 26, paid by (24).  If neither is present, the cap
   is 25, also paid by (24).

These cases include every complete multiplicity in (18).  Coincident
entry walls can only remove modes at equality under the strict count;
they cannot increase a cap.  This proves the genuinely new band (3).
Together with the frozen Round 19 theorem through \(k_6\), it proves
(2).

## 7. Exact containment below the inherited upper floor

For \(\rho\leq7/8\), (12) gives \(z<176/7\), and hence

\[
 27^2-k_7(\rho)^2
 >27^2-\left(\frac{176}{7}\right)^2-56
 =\frac{2001}{49}>0.
 \tag{34}
\]

Thus \(k_7<27\).  On \(\rho_c\leq\rho<5/6\), the accepted upper-floor
formula and \(0<\eta_\rho<1/8\) give

\[
 K_0(\rho)>\frac{a_\rho}{\eta_\rho^2}>64a_\rho\geq64,
\]

because \(a_\rho=2\rho z_\rho\) is increasing and
\(a_{\rho_c}=1\).  On the seam branch,

\[
 \frac{54}{(1-\rho)^2}\geq1944.
\]

Consequently

\[
 \boxed{k_7(\rho)<U(\rho)
 \qquad(\rho_c\leq\rho<7/8).}
 \tag{35}
\]

This proves \(\mathcal C_{20}^{\mathrm H}\) lies inside the frozen
high-ratio residual before the exact subtraction (4).

## 8. Equality, seam, and wall-order audit

- **\(K=k_6\):** Round 19 owns this closed face.  It is excluded from
  the genuinely new set, and every new-band payment uses \(K>k_6\).
- **\(K=k_7\):** included.  The \((7,1)\) moving lower bound equals the
  upper face, so strict counting excludes that channel.  Equations
  (16)--(17) and the two-case exclusions for \((2,2)\) and \((3,2)\)
  remain valid at equality.
- **\(K=2z\), \(K=p_1\), and \(K=77/10\):** the relevant second mode
  is absent at its equality wall.  Immediately above it, its full
  multiplicity is included in caps 26 or 29, and also in caps 40 or 53
  when a higher angular mode is present.
- **\(K=17/2\), \(K=c_6\):** the corresponding angular mode is absent
  at equality because the ball lower bounds are strict.  The enlarged
  cap is used only when \(K\) is strictly above the wall.
- **\(z^2=50/3\), \(z^2=44/3\):** both the moving and ball exclusions
  for the second \(\ell=2,3\) modes hold on the crossing face.  No
  ordering is assumed away from the two exhaustive cases.
- **Ratio splits \(1/5,3/10,3/7,107/200\):** both relevant estimates
  hold on each split face.  At \(3/10\), the radial-combination branches
  are empty by (21).
- **\(\rho=\rho_c\):** belongs to the new band.  The base reserve (24)
  is strict; \(\rho_c>1/8\) follows from \(\pi<7/2\).
- **\(\rho=7/8\):** belongs to the closed theorem but not to the new
  residual subtraction, consistently with the inherited endpoint owner.
- **\(\rho=5/6\), \(K=U\):** only the upper-floor owner changes at the
  seam.  Equation (35) controls both sides, and the face \(K=U\) is not
  subtracted.

All radical comparisons above are between positive quantities before
squaring.  All count caps use multiplicity \(2\ell+1\), and no cap is
carried across \(2z\), \(p_1\), \(17/2\), \(c_6\), or \(k_7\) without
the corresponding update.

## 9. Exact first obstruction to continuing through \(k_8\)

The next prospective upper face is

\[
 k_8^2=z^2+72.
\]

The first newly allowed angular channel would be \((7,1)\), which raises
the first-mode cap from 49 to

\[
 \sum_{\ell=0}^7(2\ell+1)=64.
\]

At the witness used below, second modes are still excluded already by
the moving estimate \(4z^2>z^2+72\): indeed (12) gives

\[
 z_{107/200}^2-24>
 \frac{58423224}{2699449}>0.
\]

Thus 64 is the complete relevant cap, not a stale first-radial cap
carried across a radial wall.

The strongest lower threshold obtained from the authenticated bound (8)
using only the internal angular comparison (7) is

\[
 j_{15/2,1}^2>B+26=:C_7^2.
 \tag{36}
\]

At the exact rational witness

\[
 \rho_0=\frac{107}{200},
\]

the moving wall is below this fixed threshold.  Indeed,
\(\sqrt{77}>877/100\), \(\pi<22/7\), and exact arithmetic give

\[
 B-30-z_{\rho_0}^2
 >\frac{12829703}{169520400}>0,
\]

so \(k_7(\rho_0)<C_7\).  The prospective interval above this threshold
is nonempty because \(\sqrt{77}<79/9\), \(\pi>333/106\), and

\[
 k_8(\rho_0)^2-C_7^2
 >\frac{256058629}{16196694}>0.
\]

However the Weyl term at the only currently justified exclusion wall is
still below the required cap.  The same bounds give

\[
 C_7^2<\frac{611}{6},
 \qquad
 \mathcal W(\rho_0,C_7)
 <A\left(\frac{611}{6}\right)^{3/2},
 \quad
 A:=\frac{212}{2997}
 \left(1-\left(\frac{107}{200}\right)^3\right),
\]

and the sign-safe squared certificate is

\[
 64^2-A^2\left(\frac{611}{6}\right)^3
 =\frac{29349032780743847169109}
 {95808096000000000000}>0.
 \tag{37}
\]

Thus, immediately above the available lower wall, the present inventory
must allow the \((7,1)\) multiplicity but cannot pay the resulting cap
64.  This is a proof-method obstruction, not a counterexample: the true
shell entry may occur later than (36).

The first unsupported continuation is therefore precisely:

> extending the cap-49 argument through \(k_8\) without either a sharper
> internal lower bound for \(j_{15/2,1}\) (or the shell cross-product
> itself), or a different payment/counting mechanism.

No new source dependency has been used in the proved \(k_7\) band.  A
new external zero estimate for order \(15/2\), if proposed for the
\(k_8\) step, must be separately authenticated before use.

## 10. Verdict

The prospective closed extension through \(k_7\) is **PASS** as an exact
analytic exploratory candidate.  The inventory includes every first,
second, and higher radial possibility; all angular multiplicities and
combined radial/angular caps are paid; \(k_7<U\) is strict; and every
frequency and ratio equality face has an owner.

The first unsupported continuation is the cap-64 \((7,1)\) step toward
\(k_8\), quantified exactly by (36)--(37).  The note remains exploratory
and must not be treated as frozen or promoted without the usual
proof-free claim freeze, clean-room reconstruction, independent constant
verification, and State Patch audit.
