# Round 20 exploration: global high-ratio closure by an optimized optical split

Status: **PASS on a face-connected all-frequency ratio band; exploratory
only; not frozen or promoted**.

Date: 2026-07-15.

This note follows a route qualitatively different from adding one more
angular staircase wall.  It reopens the accepted Round 16 two-piece endpoint
argument, proves a stronger exact product deficit, and moves the optical
interface.  The result is the prospective all-frequency theorem

\[
 \boxed{
 \frac{25}{32}\leq\rho<1,\qquad K\geq0
 }
 \quad\Longrightarrow\quad
 \boxed{
 N_D(A_{\rho,1},K^2)
 \leq \frac{2}{9\pi}(1-\rho^3)K^3.}
 \tag{1}
\]

At \(K=0\) both sides vanish.  For \(K>0\), the comparison proved below is
strict.  Relative to the already accepted endpoint \(7/8\leq\rho<1\), the
new ratio band is

\[
 \boxed{\frac{25}{32}\leq\rho<\frac78,\qquad K\geq0.}
 \tag{2}
\]

This is an exploratory proof, not a State Patch.  It requires its own
proof-free freeze, clean-room reconstruction, exact-constant audit, and
adversarial review before promotion.

## 1. Provenance boundary

The route uses no new external source and no numerical zero table.

| input | SHA-256 | use |
|---|---|---|
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` | strict product count, complementary action, layer cake, radial deficit, and angular-error identities |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | all-domain strict phase proxy |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum and multiplicity \(2\ell+1\) |
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` | prospective subtraction through \(k_9\), not an input to the proof of (1) |
| `rounds/polya-main/round_020/exploration/high-k9-adversarial-audit.md` | `b31a7b4d667992a4e02ffe4e5e5999cdfe611a8b67bd58ea57cdb22a4dc7f63d` | records the independent PASS on the prospective \(k_9\) result |

The Round 16 theorem itself was promoted only for
\(0<\varepsilon\leq1/8\).  Nothing below extrapolates that conclusion.
Instead, the domain-free min--max, action, curvature, sawtooth, and layer-cake
identities are reused, while every estimate depending on the enlarged
\(\varepsilon\)-range is rederived here.

## 2. Scaling and the new closed two-piece union

Put

\[
 \rho=1-\varepsilon,\qquad
 0<\varepsilon\leq\varepsilon_0:=\frac7{32},\qquad
 a=\varepsilon K,\qquad
 c:=\frac{34}{19}.
 \tag{3}
\]

Use the two inclusive optical pieces

\[
 \boxed{0\leq a\leq\frac{c}{\varepsilon}}
 \qquad\hbox{and}\qquad
 \boxed{a\geq\frac{c}{\varepsilon}}.
 \tag{4}
\]

At the worst ratio face,

\[
 \frac{c}{\varepsilon_0}=\frac{1088}{133}
 >\frac{44}{7}>2\pi,
 \qquad
 \frac{1088}{133}-\frac{44}{7}=\frac{36}{19}.
 \tag{5}
\]

Thus the common face is safely above the first positive radial branch on
the whole domain.  Both arguments below include it.

The exact Weyl normalization is

\[
 \frac{2}{9\pi}(1-\rho^3)K^3
 =\frac1{\varepsilon^2}\frac{2a^3}{3\pi}
 \left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
 \tag{6}
\]

We use throughout the elementary rational bounds

\[
 \pi<\frac{22}{7},
 \qquad
 \frac1\pi<q:=\frac{106}{333}.
 \tag{7}
\]

## 3. A stronger exact radial deficit

For \(a>\pi\), strict radial counting gives the unique representation

\[
 \frac a\pi=N+t,\qquad N\geq1,\qquad 0<t\leq1,
 \tag{8}
\]

with \((N,t)=(m-1,1)\) at \(a=m\pi\).  The accepted exact deficit identity
is

\[
 \frac{D(a)}{\pi^2}
 =\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
 \tag{9}
\]

The Round 16 proof used \(D>(2/5)a^2\).  Here the exact improvement is

\[
 \boxed{D(a)>\frac{11}{25}a^2\qquad(a>\pi).}
 \tag{10}
\]

Indeed, set

\[
 \Delta_N(t)
 :=\frac{D(a)}{\pi^2}-\frac{11}{25}(N+t)^2.
\]

Direct expansion gives

\[
 \Delta_N(t)
 =\frac{3N^2}{50}
 +N\left(t^2-\frac{22}{25}t+\frac16\right)
 +\frac{2t^3}{3}-\frac{11t^2}{25}.
 \tag{11}
\]

Moreover,

\[
 \begin{aligned}
 \Delta_{N+1}(t)-\Delta_N(t)
 &=\frac{3(2N+1)}{50}
   +\left(t-\frac{11}{25}\right)^2
   -\frac{101}{3750}\\
 &\geq \frac{287}{1875}>0.
 \end{aligned}
 \tag{12}
\]

Hence \(\Delta_N\geq\Delta_1\).  Finally,

\[
 \Delta_1(t)
 =\frac{17}{75}-\frac{22}{25}t
  +\frac{14}{25}t^2+\frac23t^3,
\]

and

\[
 \Delta_1'(t)=\frac{2}{25}(25t-11)(t+1).
\]

Its unique minimum on \((0,1]\) is therefore at \(t=11/25\), where

\[
 \Delta_1\left(\frac{11}{25}\right)
 =\frac{73}{15625}>0.
 \tag{13}
\]

This proves (10) on every radial cell, including the strict convention at
\(a=m\pi\).

## 4. Closure of the low optical piece

For \(0\leq a\leq\pi\), strict radial counting gives exactly zero modes,
including \(a=\pi\).  Assume henceforth that

\[
 \pi<a\leq\frac{c}{\varepsilon}.
\]

The product min--max comparison from the accepted endpoint machinery gives

\[
 \varepsilon^2\mathcal P_\varepsilon(a)
 <S_0(a)+\frac{\varepsilon a^2}{4}
  +\frac{\varepsilon^2a}{\pi}.
 \tag{14}
\]

Writing \(I_0(a)=2a^3/(3\pi)\) and \(D=I_0-S_0\), the stronger sufficient
condition is

\[
 D(a)>
 \varepsilon\left(I_0(a)+\frac{a^2}{4}\right)
 +\frac{\varepsilon^2a}{\pi}.
 \tag{15}
\]

After division by \(a^2\), the right side of (15) is bounded by

\[
 \frac{2\varepsilon a}{3\pi}
 +\frac\varepsilon4+\frac{\varepsilon^2}{\pi a}
 <\frac{2cq}{3}+\frac\varepsilon4+\varepsilon^2q^2.
 \tag{16}
\]

The last expression increases with \(\varepsilon\).  At
\(\varepsilon_0=7/32\), its exact reserve below \(11/25\) is

\[
 \begin{aligned}
 R_{\rm low}
 &:={11\over25}
 -\left(
 {2\over3}{34\over19}{106\over333}
 +{7\over128}
 +{49\over1024}\left({106\over333}\right)^2
 \right)\\
 &=\frac{9650531}{13484102400}>0.
 \end{aligned}
 \tag{17}
\]

Equations (10), (16), and (17) prove (15).  Consequently (14) is strictly
smaller than

\[
 I_0(a)(1-\varepsilon)
 <I_0(a)\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
 \tag{18}
\]

After division by \(\varepsilon^2\), this proves (1) strictly for \(K>0\)
on the complete low piece.  All product angular walls retain the strict
condition \(\ell(\ell+1)<b_n^2/\varepsilon^2\); no equality mode is added.

## 5. Domain-free complementary-action screen

For the high piece, use the accepted exact action

\[
 \mathcal A(y)=
 \begin{cases}
 \dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
 &0\leq y\leq\rho a,\\[6pt]
 \dfrac{J_1(y)}{\pi\varepsilon},
 &\rho a\leq y\leq a,
 \end{cases}
 \tag{19}
\]

where

\[
 J_r(y)=\sqrt{a^2r^2-y^2}
 -y\arccos\frac{y}{ar}.
\]

Let \(R\) be its decreasing inverse, \(F=R^2\), and
\(T=a/\pi\).  With the strict bracket \([u]_<:=\lceil u\rceil-1\), define

\[
 y_\ell=\varepsilon\left(\ell+\frac12\right),
 \qquad
 q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<,
 \qquad
 P_{\mathcal A}=\varepsilon\sum_{\ell\geq0}y_\ell q_\ell.
 \tag{20}
\]

The all-domain phase transfer and exact integral identity are

\[
 N_D(A_{\rho,1},K^2)\leq\frac{2P_{\mathcal A}}{\varepsilon^2},
 \qquad
 I:=\frac12\int_0^T F(t)\,dt
 =\frac{a^3}{3\pi}
 \left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
 \tag{21}
\]

For clarity about the enlarged ratio domain, the ingredients preceding the
uniform Round 16 endpoint screen are parameter-free for every
\(0<\varepsilon<1\):

1. direct differentiation makes \(-F'\) decrease before the actual inner
   interface and increase after it;
2. the shifted strict sawtooth has \(W\geq0\) and
   \(-1/32\leq W-t/4\leq3/32\);
3. the strict layer count is
   \(M_\varepsilon(x)=\max\{0,\lceil x/\varepsilon-1/2\rceil\}\).

Repeating the Stieltjes split at the actual, ungridded interface therefore
gives, without an \(\varepsilon\leq1/8\) assumption,

\[
 D_{\rm rad}
 \geq\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4},
 \tag{22}
\]

while the complete strict angular ceiling loss is less than

\[
 E=\left(\frac a\pi+\frac14\right)
 \left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
 \tag{23}
\]

Exactly as in the accepted endpoint proof,
\(D_{\rm rad}>E\) implies \(P_{\mathcal A}<I\).  Equations (22)--(23),
not the old \(\varepsilon=1/8\) reserve, are the inputs to the new screen.

## 6. Closure of the high optical piece

Assume

\[
 a\geq\frac{c}{\varepsilon}.
\]

Then \(1/a\leq\varepsilon/c=19\varepsilon/34\).  Equation (22) yields

\[
 \frac{D_{\rm rad}}{a^2}
 \geq \frac{(1-\varepsilon)^2}{4}
 -\frac{19\pi}{136}(1-\varepsilon)\varepsilon.
 \tag{24}
\]

Expanding (23) and using the same reciprocal bound gives

\[
 \frac{E}{a^2}
 \leq
 \frac\varepsilon\pi
+\frac{19\varepsilon^3}{136\pi}
+\frac{19\varepsilon^2}{136}
+\frac{361\varepsilon^4}{18496}.
 \tag{25}
\]

The right side of (25) increases with \(\varepsilon\).  The rational lower
screen obtained from (24) by \(\pi<22/7\) decreases on
\(0<\varepsilon<1/2\), since its derivative is a sum of two negative terms.
It is therefore enough to evaluate \(\varepsilon_0=7/32\).  Using (7), the
exact reserve is

\[
 \begin{aligned}
 R_{\rm high}
 &:={1\over4}\left({25\over32}\right)^2
 -{22\over7}{(25/32)(7/32)\over4(34/19)}\\
 &\quad-\left[
 {7\over32}q
 +{(7/32)^3q\over4(34/19)}
 +{(7/32)^2\over4(34/19)}
 +{(7/32)^4\over16(34/19)^2}
 \right]\\
 &=\frac{4669924235}{6458355744768}>0.
 \end{aligned}
 \tag{26}
\]

Thus \(D_{\rm rad}>E\), including both the closed ratio face
\(\varepsilon=7/32\) and the optical equality face
\(a=c/\varepsilon\).  Equations (20)--(21) give the strict Weyl comparison
for every \(K>0\) on the high piece.

## 7. Closed union and equality audit

The two sets in (4) cover every \(a\geq0\), and both own their common face.
The preceding proof also owns all potentially delicate boundaries:

- \(K=a=0\): the strict spectral count and the Weyl term both vanish;
- \(a=m\pi\): use \((N,t)=(m-1,1)\), so the threshold radial mode is
  excluded;
- \(b_n^2/\varepsilon^2=\ell(\ell+1)\): the product angular mode at
  equality is excluded;
- an action radial wall \(n-1/4=T\), a half-integer angular wall, or a
  phase-proxy integer wall: the strict bracket in (20) excludes the
  threshold contribution;
- \(a=c/\varepsilon\): every reciprocal estimate in the high screen may
  be equality, but both exact reserves (17) and (26) remain strictly
  positive;
- \(\rho=25/32\): included; \(\rho=1\) remains the excluded degenerate
  zero-width limit.

No value of the incumbent Round 16 reserve \(143/4096\) was extrapolated.
The new proof uses the fresh reserves (17) and (26).

## 8. Exact effect on the prospective \(k_9\) residual

The independently audited exploratory \(k_9\) result would, if frozen and
promoted, leave the high component

\[
 \mathcal D_{20}^{\rm H,9}
 =\left\{(\rho,K):
 \rho_c\leq\rho<\frac78,
 \quad k_9(\rho)<K<U(\rho)\right\}.
 \tag{27}
\]

The new all-frequency band subtracts exactly

\[
 \boxed{
 \mathcal C_{20}^{\rm global}
 =\left\{(\rho,K):
 \frac{25}{32}\leq\rho<\frac78,
 \quad k_9(\rho)<K<U(\rho)\right\}.}
 \tag{28}
\]

Conditional on both promotions, the normalized high residual becomes

\[
 \boxed{
 \left\{(\rho,K):
 \rho_c\leq\rho<\frac{25}{32},
 \quad k_9(\rho)<K<U(\rho)\right\}.}
 \tag{29}
\]

Every face has an owner: \(\rho=25/32\) belongs to the new theorem,
\(K=k_9\) belongs to the prospective staircase theorem, and \(K=U\)
belongs to the inherited upper analytic cover.

This subtraction crosses both live upper-floor branches.  The declared
\(k_9\) adversarial audit records the inherited central floor \(U=K_0\) on
\(\rho_c\leq\rho<5/6\).  Since \(25/32<5/6\), the only upper floor
remaining in (29) is

\[
 \boxed{U(\rho)=K_0(\rho)
 \qquad\left(\rho_c\leq\rho<\frac{25}{32}\right).}
 \tag{30}
\]

In particular, the seam branch \(54/(1-\rho)^2\) disappears completely
from the prospective high residual.

## 9. Exact frontier of this two-screen mechanism

The proof above deliberately keeps comfortable exact margins.  Its selected
two-screen family can be described for a general positive split constant
\(c\).  With \(C_D=11/25\), define

\[
 R_L(c,\varepsilon)
 =C_D-\frac{2cq}{3}-\frac\varepsilon4-\varepsilon^2q^2,
 \tag{31}
\]

and

\[
 \begin{aligned}
 R_H(c,\varepsilon)
 ={}&\frac{(1-\varepsilon)^2}{4}
 -\frac{(22/7)(1-\varepsilon)\varepsilon}{4c}\\
 &-\left(
 \varepsilon q+\frac{\varepsilon^3q}{4c}
 +\frac{\varepsilon^2}{4c}
 +\frac{\varepsilon^4}{16c^2}
 \right).
 \end{aligned}
 \tag{32}
\]

Both screens are positive at

\[
 \varepsilon=\frac9{41},\qquad c=\frac{206}{115},
\]

with exact reserves

\[
 R_L=\frac{14692831}{142910046900}>0,
 \qquad
 R_H=\frac{13435547837}{496923590290624}>0.
 \tag{33}
\]

Thus the mechanism can be tuned slightly beyond the clean face chosen in
(3).  On the other hand, at \(\varepsilon=11/50\), positivity of the low
screen forces

\[
 c<c_{\max}
 :=\frac{3}{2q}
 \left(\frac{11}{25}-\frac{11}{200}
 -\frac{121}{2500}q^2\right)
 =\frac{210742213}{117660000}.
 \tag{34}
\]

For fixed \(\varepsilon\), \(R_H\) is strictly increasing in \(c\).  Yet

\[
 R_H\left(c_{\max},\frac{11}{50}\right)
 =-\frac{4113718505834613061}
 {8555787229162000590000}<0.
 \tag{35}
\]

Hence **no choice of optical split constant \(c\)** closes both rational
screens at \(\varepsilon=11/50\).  This is a sharp obstruction for the
specific separated estimates (10), (22), and (23), not a shell
counterexample and not an obstruction to a coupled treatment.

A concrete next lemma is now quantified: recover at least
\(a^2/2000\) in the combined high-action deficit/error estimate near
\(\varepsilon=11/50\).  This exceeds the exact shortfall in (35), because

\[
 \frac1{2000}
 -\frac{4113718505834613061}
 {8555787229162000590000}
 =\frac{82087554373193617}
 {4277893614581000295000}>0.
 \tag{36}
\]

By continuity, after such a gain one may choose a rational
\(c<c_{\max}\) sufficiently close to \(c_{\max}\) so that both the low
reserve and the improved high reserve are strict.

Such a gain could come from retaining the exact \(a\)-dependence in the
radial sawtooth deficit, from reducing the layer-count ceiling error before
summation, or from coupling those two terms instead of bounding them
separately.  Merely moving the optical interface cannot cross (35).

## 10. Verdict

The global route is an exact exploratory **PASS** on the face-connected
all-frequency band

\[
 \boxed{\frac{25}{32}\leq\rho<1,\qquad K\geq0.}
\]

It strengthens the radial product deficit from \(2/5\) to \(11/25\), pays
both sides of the reoptimized optical split with exact positive reserves,
preserves every strict counting wall, and crosses the central/seam upper
floor without any special interface argument.  Combined prospectively with
the independently audited \(k_9\) result, it removes the entire seam branch
and leaves only (29), with upper floor \(K_0(\rho)\).

No computation file was needed.  Promotion remains forbidden until the
usual Round 20 freeze and independent proof gates pass.
