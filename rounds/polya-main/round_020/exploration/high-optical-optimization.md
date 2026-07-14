# Round 20 exploration: sharpened optical threshold at \(\rho=39/50\)

Status: **PASS for a strictly improved all-frequency ratio threshold;
exploratory only; not frozen or promoted**.

Date: 2026-07-15.

This note optimizes the exact two-screen route in
`high-global-route.md`. It proves

\[
 \boxed{
 \frac{39}{50}\leq\rho<1,\qquad K\geq0}
 \quad\Longrightarrow\quad
 \boxed{
 N_D(A_{\rho,1},K^2)
 \leq\frac{2}{9\pi}(1-\rho^3)K^3.}
 \tag{1}
\]

At \(K=0\), both sides vanish. For \(K>0\), the comparison is strict.
The new threshold is genuinely smaller than both the displayed
\(25/32\) theorem face and the \(32/41\) tuning witness in the predecessor:

\[
 \frac{25}{32}-\frac{39}{50}=\frac1{800}>0,
 \qquad
 \frac{32}{41}-\frac{39}{50}=\frac1{2050}>0.
 \tag{2}
\]

The repair does not assert the hypothetical high-action gain proposed in
the predecessor. Instead, it proves a larger gain in the exact product
deficit and transfers that gain to the high screen by moving the optical
split.

## 1. Exact provenance boundary

No new external source or numerical zero table is used.

| input | SHA-256 | exact use |
|---|---|---|
| `rounds/polya-main/round_020/exploration/high-global-route.md` | `bbfc40bcb7ce748b946a6fdea7728315489d7e2e7842a0ccb6789f3f34fee6c4` | scaling, strict product count, exact deficit identity, complementary-action screen, and equality bookkeeping |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` | product and action identities inherited by the predecessor |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | all-domain strict phase proxy |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum and multiplicity |

The predecessor rederived every estimate whose validity depends on the
enlarged \(\varepsilon\)-range. This note changes only the exact deficit
constant, the rational split, and the endpoint arithmetic.

## 2. Scaling and optimized split

Put

\[
 \rho=1-\varepsilon,\qquad
 0<\varepsilon\leq\varepsilon_0:=\frac{11}{50},
 \qquad
 a=\varepsilon K,
 \tag{3}
\]

and choose

\[
 C_D:=\frac{1382}{3125},
 \qquad
 c:=\frac{1126}{625}.
 \tag{4}
\]

Use the two inclusive pieces

\[
 0\leq a\leq\frac{c}{\varepsilon},
 \qquad
 a\geq\frac{c}{\varepsilon}.
 \tag{5}
\]

Their common face stays above \(2\pi\) throughout the enlarged domain:

\[
 \frac{c}{\varepsilon_0}
 =\frac{2252}{275}
 >\frac{44}{7}>2\pi,
 \qquad
 \frac{2252}{275}-\frac{44}{7}
 =\frac{3664}{1925}>0.
 \tag{6}
\]

As before, write

\[
 q:=\frac{106}{333},
 \qquad
 \pi<\frac{22}{7},
 \qquad
 \frac1\pi<q.
 \tag{7}
\]

## 3. A sharper exact product deficit

For \(a>\pi\), strict radial counting gives

\[
 \frac a\pi=N+t,\qquad N\geq1,\qquad0<t\leq1,
 \tag{8}
\]

using \((N,t)=(m-1,1)\) at \(a=m\pi\). The exact identity is

\[
 \frac{D(a)}{\pi^2}
 =\frac{N^2}{2}
 +N\left(t^2+\frac16\right)
 +\frac{2t^3}{3}.
 \tag{9}
\]

We claim the strict improvement

\[
 \boxed{
 D(a)>C_Da^2
 =\frac{1382}{3125}a^2
 \qquad(a>\pi).}
 \tag{10}
\]

Define

\[
 \Delta_N(t)
 :=\frac{D(a)}{\pi^2}-C_D(N+t)^2,
 \qquad
 A:=\frac12-C_D=\frac{361}{6250}.
\]

Then

\[
 \Delta_{N+1}(t)-\Delta_N(t)
 =A(2N+1)+(t-C_D)^2+\frac16-C_D^2.
 \tag{11}
\]

For \(N\geq1\),

\[
 \Delta_{N+1}(t)-\Delta_N(t)
 \geq3A+\frac16-C_D^2
 =\frac{4229603}{29296875}>0.
 \tag{12}
\]

Thus \(\Delta_N\geq\Delta_1\). Direct differentiation gives

\[
 \Delta_1'(t)=2(t-C_D)(t+1),
 \tag{13}
\]

so the unique minimum on \((0,1]\) occurs at \(t=C_D\). Its exact value is

\[
 \Delta_1(C_D)
 =\frac23-C_D-C_D^2-\frac{C_D^3}{3}
 =\frac{1822532}{91552734375}>0.
 \tag{14}
\]

This proves (10) on every radial cell, including the strict convention at
\(a=m\pi\).

The improvement over the predecessor's \(11/25\) bound is

\[
 C_D-\frac{11}{25}
 =\frac7{3125}
 =\frac1{2000}+\frac{87}{50000}
 >\frac1{2000}.
 \tag{15}
\]

Thus the exact product deficit recovers more than the previously requested
\(a^2/2000\) margin. This is an actual proved gain, not a continuity
ansatz.

## 4. The two rational screens

The predecessor reduces the low optical piece to positivity of

\[
 R_L(C,c,\varepsilon)
 :=C-\frac{2cq}{3}-\frac{\varepsilon}{4}
 -\varepsilon^2q^2.
 \tag{16}
\]

Indeed, for \(\pi<a\leq c/\varepsilon\), after division by \(a^2\), the
right side of the sufficient product inequality is strictly less than

\[
 \frac{2cq}{3}+\frac{\varepsilon}{4}
 +\varepsilon^2q^2.
\]

The high complementary-action piece is reduced to positivity of

\[
\begin{aligned}
 R_H(c,\varepsilon)
 :={}&\frac{(1-\varepsilon)^2}{4}
 -\frac{(22/7)(1-\varepsilon)\varepsilon}{4c}\\
 &-\left(
 \varepsilon q+\frac{\varepsilon^3q}{4c}
 +\frac{\varepsilon^2}{4c}
 +\frac{\varepsilon^4}{16c^2}
 \right).
 \tag{17}
\end{aligned}
\]

These are the same sufficient screens as in the predecessor. For fixed
\(C,c>0\), \(R_L\) decreases with \(\varepsilon\). On
\(0<\varepsilon<1/2\), the positive lower part of \(R_H\) decreases while
its subtracted ceiling bound increases. Hence it is enough to check both
screens at \(\varepsilon_0=11/50\).

## 5. Exact closure of the low optical piece

At the constants (3)--(4), exact substitution gives

\[
\begin{aligned}
 R_L\left(C_D,c,\varepsilon_0\right)
 &=
 \frac{1382}{3125}
 -\frac23\frac{1126}{625}\frac{106}{333}
 -\frac{11}{200}
 -\frac{121}{2500}\left(\frac{106}{333}\right)^2\\
 &=\frac{39569}{2772225000}>0.
 \tag{18}
\end{aligned}
\]

For \(0\leq a\leq\pi\), the strict radial count is zero, including the
face \(a=\pi\). For \(\pi<a\leq c/\varepsilon\), equations (10), (16),
and (18) prove the predecessor's strict sufficient product inequality.
After restoring the factor \(\varepsilon^{-2}\), this is the strict Weyl
comparison on the complete low piece for \(K>0\).

It is useful to record why the old \(\varepsilon=11/50\) obstruction has
disappeared. The old low screen allowed only

\[
 c<c_{\max}^{\rm old}
 =\frac{210742213}{117660000}.
\]

The new split is larger by

\[
 \frac{1126}{625}-c_{\max}^{\rm old}
 =\frac{1234043}{117660000}>0,
 \tag{19}
\]

while the sharpened low screen still has the strict reserve (18).

## 6. Exact closure of the high optical piece

On \(a\geq c/\varepsilon\), one has \(1/a\leq\varepsilon/c\). The
predecessor's exact radial deficit and full angular ceiling therefore give
the screen (17). Exact substitution yields

\[
\begin{aligned}
 R_H\left(c,\varepsilon_0\right)
 ={}&
 \frac14\left(\frac{39}{50}\right)^2
 -\frac{22}{7}
 \frac{(39/50)(11/50)}{4(1126/625)}\\
 &-\left[
 \frac{11}{50}q
 +\frac{(11/50)^3q}{4(1126/625)}
 +\frac{(11/50)^2}{4(1126/625)}
 +\frac{(11/50)^4}{16(1126/625)^2}
 \right]\\
 ={}&\frac{14817541}{472867032960000}>0.
 \tag{20}
\end{aligned}
\]

The reserve is small but exact and strictly positive. Thus the inherited
complementary-action argument gives \(P_{\mathcal A}<I\) on the complete
high piece, including the ratio face \(\varepsilon=11/50\) and optical
face \(a=c/\varepsilon\).

No extra term has been inserted into the action deficit. The proved
product improvement permits the larger split (19), and the larger split
reduces the reciprocal losses enough to make (20) positive.

## 7. Closed union and strict-face audit

The two pieces in (5) cover every \(a\geq0\) and both include their common
face. The strict conventions are unchanged:

- \(K=a=0\): both the spectral count and Weyl term vanish;
- \(a=\pi\): the threshold radial mode is excluded;
- \(a=m\pi\), \(m\geq2\): representation (8) uses
  \((N,t)=(m-1,1)\), and (14) remains strict;
- a product angular equality, action radial equality, half-integer angular
  equality, or phase-proxy integer equality contributes no threshold mode
  under the inherited strict brackets;
- \(a=c/\varepsilon\): both low and high estimates apply, with the positive
  reserves (18) and (20);
- \(\rho=39/50\): included; \(\rho=1\) remains the excluded degenerate
  zero-width limit.

Therefore the union proves (1) with no frequency gap and no extrapolation
of an old endpoint reserve.

## 8. Exact effect and verdict

The newly covered ratio strip beyond the predecessor's displayed theorem is

\[
 \boxed{
 \frac{39}{50}\leq\rho<\frac{25}{32},
 \qquad K\geq0.}
 \tag{21}
\]

Consequently, when combined with any independently promoted finite
staircase below \(7/8\), the all-frequency route leaves no high residual at
or above \(39/50\).

The optimized optical route is an exact exploratory **PASS** with threshold

\[
 \boxed{\rho_{\rm optical}=\frac{39}{50}.}
\]

Its decisive new lemma is the uniform strict deficit
\(D(a)>(1382/3125)a^2\). That lemma supplies more than the predecessor's
noted \(a^2/2000\) target, allows the exact split \(c=1126/625\), and
closes both screens at \(\varepsilon=11/50\) with positive rational
reserves. Promotion remains forbidden until a proof-free freeze and all
independent review gates pass.
