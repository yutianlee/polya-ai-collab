# Round 19 A2 High-Ratio \(k_6\) Incumbent

Status: **EXACT ANALYTIC CANDIDATE DERIVED / NOT PROMOTED**.

Date: 2026-07-14.

Role: A2 incumbent for the high-ratio component only.

Baseline commit: `b9c40349e0e39b48b8e08fcd66813bf4e3c093a7`.

This response starts from the committed Round 19 residual-mask freeze. It
does not edit that freeze, the obligation graph, or any state file. The two
new unit-ball zero bounds have a separate, scope-limited provenance record:

| artifact | authenticated SHA-256 | verdict |
|---|---|---|
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` | qualified exact-order source plus internal proof |
| `rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md` | `ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718` | PASS; first unsupported implication none |

## 1. Candidate and exact subtraction

Retain

$$
\rho_c=\frac1{1+2\pi},\qquad
z=z_\rho=\frac{\pi}{1-\rho},\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
$$

and

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{1}
$$

The candidate closed extension is

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad z_\rho\leq K\leq k_6(\rho)
}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{2}
$$

Round 18 already owns the closed subband through \(k_5\). Thus the
genuinely new set is exactly

$$
\boxed{
\mathcal C_{19}^{\mathrm H}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_5(\rho)<K\leq k_6(\rho)
\right\}.}
\tag{3}
$$

Sections 2--8 prove (2), including \(K=k_6\) and all ratio and frequency
seams. Section 9 proves \(k_6<U\), so (3) lies inside the frozen
post-\(k_5\) residual component. If promoted, exact subtraction would give

$$
\boxed{
\begin{aligned}
\mathcal D_{19}^{\mathrm H,cand}
={}&\left\{\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup\left\{\rho_c\leq\rho<\frac78,
\quad k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}}
\tag{4}
$$

This leaves the entire lower-ratio component untouched and is not a full
shell theorem.

## 2. Spectral inputs and provenance

After the unitary radial transformation, angular channel \(\ell\) is
governed on \((\rho,1)\) by

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
$$

with Dirichlet endpoints. Write its radial eigenvalues in increasing order
as \(\lambda_{\ell,n}^{\rm sh}\). Since \(r^{-2}\geq1\), fixed-channel
min--max gives

$$
\boxed{
\lambda_{\ell,n}^{\rm sh}
\geq n^2z^2+\ell(\ell+1).}
\tag{5}
$$

For \(\ell=0\) the potential vanishes, so

$$
\boxed{\lambda_{0,n}^{\rm sh}=n^2z^2.}
\tag{6}
$$

Zero extension of a shell radial function across \((0,\rho]\) preserves
its norm and quadratic form and embeds the shell form domain into the unit
ball form domain in the **same angular channel**. Min--max at each radial
index therefore gives the internal comparison

$$
\boxed{
\lambda_{\ell,n}^{\rm sh}(\rho)
\geq j_{\ell+1/2,n}^2.}
\tag{7}
$$

Neither Lorch nor DLMF is cited for (7), a shell cross-product zero, a
multiplicity, or a Weyl payment.

Round 18 supplies the already audited first-zero thresholds

$$
c_2=\frac{51}{10},\qquad
c_3=\frac{13}{2},\qquad
c_4=\frac{15}{2},
\tag{8}
$$

with \(\lambda_{m,1}^{\rm sh}>c_m^2\) for \(m=2,3,4\). The new, separately
audited zero record supplies exactly

$$
\boxed{
j_{11/2,1}>c_5=\frac{17}{2},
\qquad
j_{3/2,2}>c_{1,2}=\frac{77}{10}.}
\tag{9}
$$

For the first inequality, the newly audited specialization of Lorch's
published second bound is

$$
j_{11/2,1}^2>
\frac{507(\sqrt{77}-1)}{52}>\frac{289}{4};
$$

the last comparison is sign-safe because both sides are positive and

$$
507^2\cdot77-4264^2=1611077>0.
\tag{10}
$$

This is a new exact-order dependency, not an extrapolation of the Round 18
three-order source obligation.

The second inequality in (9) is internal. The positive zeros of

$$
\mathsf j_1(x)=\frac{\sin x-x\cos x}{x^2}
$$

solve \(\tan x=x\). On each
\((n\pi,n\pi+\pi/2)\), \(\tan x-x\) increases strictly from a negative
value to \(+\infty\), and it has no root on the complementary half-period.
Thus the second positive root is the unique root in
\((2\pi,5\pi/2)\). At \(x_0=77/10\), put
\(y=5\pi/2-x_0\). The exact enclosure
\(333/106<\pi<22/7\) gives

$$
0<y<\frac\pi2,
\qquad
y>\frac{163}{1060}>\frac{10}{77}.
$$

Since \(\tan y>y\) on \((0,\pi/2)\),

$$
\tan x_0=\cot y<\frac1y<\frac{77}{10}=x_0.
$$

The unique second root is therefore strictly larger than \(77/10\).

Each angular channel has its full multiplicity \(2\ell+1\), and the count
is strict: an eigenvalue equal to \(K^2\) is not counted.

## 3. The inherited first-mode payment mechanism

The proof above \(k_5\) must retain the delayed-entry payments from Round
18. A uniform raw cap of \(25\) is **not** payable near \(\rho_c\).

For \(m\leq5\), let

$$
F_m(\rho)=\mathcal W(\rho,k_m(\rho)),\qquad
e=1-\rho,\qquad S=1+\rho+\rho^2,
\qquad d=m(m+1).
$$

Then

$$
F_m(\rho)
=\frac{2}{9\pi}\frac{S}{e^2}
(\pi^2+de^2)^{3/2}.
\tag{11}
$$

The sign of its logarithmic derivative, after multiplication by its
positive denominator, is the sign of

$$
3\left[\pi^2(1+\rho)-d\rho^2(1-\rho)^2\right].
\tag{12}
$$

For \(d\leq30\), \(\pi>3\), and
\(\rho^2(1-\rho)^2\leq1/16\), the bracket in (12) is strictly larger than

$$
9-\frac{30}{16}=\frac{57}{8}>0.
$$

Hence every \(F_m\) used below is strictly increasing. At fixed positive
\(c\), \(\mathcal W(\rho,c)\) is strictly decreasing in \(\rho\).

The cap-four baseline is also uniform. From the exact Round 18
reconstruction,

$$
F_2(\rho_c)
>\frac{23579}{4312}
=4+\frac{6331}{4312}>4.
\tag{13}
$$

For the higher inherited entries, use

$$
(r_2,r_3,r_4)=\left(\frac3{10},\frac12,\frac12\right).
$$

The moving walls exceed the fixed thresholds at the splits with the exact
positive lower reserves

$$
\begin{aligned}
k_2(r_2)^2-c_2^2&>\frac{547}{4900},\\
k_3(r_3)^2-c_3^2&>\frac{23}{4},\\
k_4(r_4)^2-c_4^2&>\frac{7971}{2500}.
\end{aligned}
\tag{14}
$$

Using \(2/(9\pi)>7/99\), their fixed-threshold payments are

$$
\begin{aligned}
\mathcal W(r_2,c_2)
&>\frac{100387329}{11000000}
=9+\frac{1387329}{11000000},\\
\mathcal W(r_3,c_3)
&>\frac{107653}{6336}
=16+\frac{6277}{6336},\\
\mathcal W(r_4,c_4)
&>\frac{18375}{704}
=25+\frac{775}{704}.
\end{aligned}
\tag{15}
$$

Consequently, if the first mode in channel \(m\in\{2,3,4\}\) is counted,
then (5), (7), and (8) force

$$
K>k_m(\rho),\qquad K>c_m,
$$

and the split argument gives

$$
\boxed{\mathcal W(\rho,K)>(m+1)^2.}
\tag{16}
$$

Indeed, for \(\rho\leq r_m\), the fixed wall in (15) pays; for
\(\rho\geq r_m\), monotonicity of \(F_m\), (14), and (15) pay at the
moving wall. Thus, whenever only first radial modes with \(\ell\leq4\)
are possible, choose the largest contributing \(m\in\{2,3,4\}\). The
complete multiplicity cap is

$$
\sum_{\ell=0}^{m}(2\ell+1)=(m+1)^2,
$$

and (16) pays it. If no such \(m\) contributes, the cap is \(1+3=4\),
and, because the new band has \(K>k_5>k_2\),
\(\mathcal W(\rho,K)>F_2(\rho)\geq F_2(\rho_c)>4\) by (13). This
reconstructs rather than replaces the inherited first-mode staircase.

## 4. Spectral inventory for \(\rho_c\leq\rho\leq1/4\)

The split is nonempty because \(\pi>3\) gives
\(\rho_c<1/7<1/5<1/4\).
Since \(z\geq z_{\rho_c}=\pi+1/2>7/2\), for \(K\leq k_6\) equation (5)
gives, for every \(n\geq3\),

$$
\lambda_{\ell,n}^{\rm sh}-K^2
\geq9z^2-(z^2+42)
>8\left(\frac72\right)^2-42=56.
\tag{17}
$$

For \(n=2\) and \(\ell\geq2\),

$$
\lambda_{\ell,2}^{\rm sh}-K^2
\geq4z^2+6-(z^2+42)
>3\left(\frac72\right)^2-36=\frac34.
\tag{18}
$$

Every first mode with \(\ell\geq6\) is absent because
\(z^2+\ell(\ell+1)\geq z^2+42\geq K^2\), with equality still excluded by
strict counting.

The remaining possible first channel \(\ell=5\) is also absent on this
ratio interval. The function \(k_6\) increases in \(\rho\), and
\(\pi<22/7\) gives the exact squared reserve

$$
\left(\frac{17}{2}\right)^2-k_6\!\left(\frac14\right)^2
>
\left(\frac{17}{2}\right)^2
-\left(\frac{88}{21}\right)^2-42
=\frac{22385}{1764}>0.
\tag{19}
$$

Equations (7), (9), and (19) exclude \(\ell=5,n=1\) through the closed
\(K=k_6\) face. Hence the complete list of possible modes is

$$
(\ell,1),\ 0\leq\ell\leq4;\qquad
(0,2);\qquad(1,2).
\tag{20}
$$

The second \(\ell=0\) mode enters only when \(K>2z\), by (6). The second
\(\ell=1\) mode can enter only when

$$
K>p_1(\rho):=\sqrt{4z^2+2}
\quad\hbox{and}\quad
K>c_{1,2}=\frac{77}{10},
\tag{21}
$$

by (5), (7), and (9). If the latter mode is counted then the exact
\(\ell=0,n=2\) mode is counted too, because its eigenvalue \(4z^2\) is
strictly smaller than the lower bound \(4z^2+2\) in (21).

The exhaustive strict-count alternatives are therefore:

| radial state | possible modes | cap |
|---|---|---:|
| neither second mode counted | first modes \(0\leq\ell\leq4\), with delayed entries | paid by the actual cap \(4,9,16\), or \(25\) from Section 3 |
| \((0,2)\) counted, \((1,2)\) absent | all first modes plus multiplicity \(1\) | \(25+1=26\) |
| \((1,2)\) counted | all first modes plus multiplicities \(1+3\) | \(25+1+3=29\) |

This table already includes full angular multiplicities, so cross-channel
coincidences cannot enlarge a cap.

## 5. Payment of the cap \(26\)

At the exact \((0,2)\) wall,

$$
G_0(\rho):=\mathcal W(\rho,2z)
=\frac{16\pi^2}{9}\frac{1+\rho+\rho^2}{(1-\rho)^2}
\tag{22}
$$

is strictly increasing. At \(\rho_c\), where
\(z_{\rho_c}=\pi+1/2\), exact simplification gives

$$
G_0(\rho_c)
=\frac{16\pi^2+24\pi+12}{9}.
$$

The polynomial is increasing for positive \(\pi\), so \(\pi>157/50\)
gives

$$
G_0(\rho_c)
>\frac{153196}{5625}
=26+\frac{6946}{5625}>26.
\tag{23}
$$

If \((0,2)\) is counted, then \(K>2z\), and (22)--(23) imply
\(\mathcal W(\rho,K)>26\). At \(K=2z\), the mode is absent by strict
counting, so the smaller first-mode alternative from Section 3 applies.

## 6. Payment of the cap \(29\)

Set

$$
H_1(\rho):=\mathcal W(\rho,p_1(\rho)),
\qquad p_1(\rho)=\sqrt{4z^2+2}.
$$

Direct differentiation gives

$$
\frac1{3}\frac{H_1'}{H_1}
=-\frac{\rho^2}{1-\rho^3}
+\frac{2\pi^2}{(1-\rho)(2\pi^2+(1-\rho)^2)}.
\tag{24}
$$

After multiplication by the positive denominator, its sign is that of

$$
2\pi^2(1+\rho)-\rho^2(1-\rho)^2
>18-\frac1{16}>0.
\tag{25}
$$

Thus \(H_1\) is strictly increasing. Split at \(r_{1,2}=1/5\). At the
split, \(\pi>333/106\) gives

$$
p_1\!\left(\frac15\right)^2
-\left(\frac{77}{10}\right)^2
>\frac{4934581}{1123600}>0.
\tag{26}
$$

Using \(2/(9\pi)>7/99\), the fixed payment is

$$
\mathcal W\!\left(\frac15,\frac{77}{10}\right)
>\frac{9006151}{281250}
=29+\frac{849901}{281250}>29.
\tag{27}
$$

If \((1,2)\) is counted, (21) holds. For \(\rho\leq1/5\), monotonicity at
the fixed threshold and (27) give \(\mathcal W(\rho,K)>29\). For
\(\rho\geq1/5\), (24)--(27) give

$$
\mathcal W(\rho,K)>H_1(\rho)
\geq H_1(1/5)
>\mathcal W(1/5,77/10)>29.
$$

The two arguments agree at \(\rho=1/5\). If
\(K=p_1(\rho)\) or \(K=77/10\), the \((1,2)\) mode is absent, so the
cap-\(29\) branch is not invoked.

Sections 3--6 prove (2) for
\(\rho_c\leq\rho\leq1/4\) and \(k_5<K\leq k_6\).

## 7. Spectral inventory for \(1/4\leq\rho\leq7/8\)

Here \(z\geq4\pi/3>4\). For every \(n\geq2\),

$$
\lambda_{\ell,n}^{\rm sh}-K^2
\geq4z^2-(z^2+42)
=3z^2-42>6.
\tag{28}
$$

Thus no second or higher radial mode contributes. As before, every first
mode with \(\ell\geq6\) is absent through \(K=k_6\). Only first modes
\(0\leq\ell\leq5\) remain.

If \(\ell=5\) is absent, Section 3 pays the actual delayed-entry cap among
\(\ell=0,1,2,3,4\). If \(\ell=5\) is counted, the complete cap is

$$
\sum_{\ell=0}^{5}(2\ell+1)=36.
\tag{29}
$$

It remains to pay exactly this new cap.

## 8. Payment of the cap \(36\)

If the \(\ell=5\) first mode is counted, (5), (7), and (9) force both

$$
K>k_5(\rho),\qquad K>c_5=\frac{17}{2}.
\tag{30}
$$

Split at \(r_5=13/25\). The moving wall exceeds the fixed wall there:
using \(\pi>333/106\),

$$
k_5\!\left(\frac{13}{25}\right)^2
-\left(\frac{17}{2}\right)^2
>\frac{105089}{179776}>0.
\tag{31}
$$

The exact fixed payment is

$$
\mathcal W\!\left(\frac{13}{25},\frac{17}{2}\right)
>\frac{12827843}{343750}
=36+\frac{452843}{343750}>36,
\tag{32}
$$

again from \(2/(9\pi)>7/99\). For \(\rho\leq13/25\), (30), (32), and
fixed-wall monotonicity pay \(36\). For \(\rho\geq13/25\), the increasing
function \(F_5\), (31), and (32) give

$$
\mathcal W(\rho,K)>F_5(\rho)
\geq F_5(13/25)
>\mathcal W(13/25,17/2)>36.
$$

The split face is included in both arguments. At \(K=17/2\), the
\(\ell=5\) mode is absent because the zero bound is strict. At \(K=k_5\),
it is absent by (5) and strict counting; that complete face is already
owned by Round 18.

Sections 3, 7, and 8 prove (2) for
\(1/4\leq\rho\leq7/8\) and \(k_5<K\leq k_6\).

## 9. Exact upper-floor containment

For every \(\rho\leq7/8\), \(z\leq8\pi<176/7\). Hence

$$
26^2-k_6(\rho)^2
>26^2-\left(\frac{176}{7}\right)^2-42
=\frac{90}{49}>0.
\tag{33}
$$

Thus \(k_6<26\) on the complete closed ratio band.

On \(\rho_c\leq\rho<5/6\), the frozen upper floor is \(K_0\). Its exact
formula and the accepted bounds \(0<\eta_\rho<1/8\) imply

$$
K_0(\rho)>\frac{a_\rho}{\eta_\rho^2}
>64a_\rho=128\rho z_\rho.
$$

The function \(\rho z_\rho\) is increasing and
\(\rho_cz_{\rho_c}=1/2\), so \(K_0>64\). Therefore

$$
k_6<26<64<K_0
\qquad(\rho_c\leq\rho<5/6).
\tag{34}
$$

On the seam branch,

$$
\frac{54}{(1-\rho)^2}\geq1944>26>k_6
\qquad(5/6\leq\rho\leq7/8).
\tag{35}
$$

Equations (33)--(35) prove

$$
\boxed{k_6(\rho)<U(\rho)
\quad(\rho_c\leq\rho<7/8),}
\tag{36}
$$

and therefore \(\mathcal C_{19}^{\mathrm H}\subset\mathcal D_{18}\).

## 10. Equality and seam audit

- **\(K=k_5\):** owned by Round 18 and excluded from the genuinely new
  set. The \(\ell=5\) product wall is not counted there.
- **\(K=k_6\):** included. The \(\ell=6,n=1\) product lower bound equals
  \(K^2\), so strict counting excludes that channel. All radial exclusions
  above have strict positive margins.
- **\(K=2z\):** the exact \((0,2)\) mode is at equality and is not counted;
  the inherited first-mode staircase applies. Immediately above the wall,
  (23) pays cap \(26\).
- **\(K=p_1\), \(K=77/10\):** the \((1,2)\) mode is absent at either
  equality; cap \(29\) is used only when both inequalities in (21) are
  strict.
- **\(K=17/2\):** the \(\ell=5\) mode is absent because
  \(\lambda_{5,1}^{\rm sh}>(17/2)^2\); cap \(36\) is used only above the
  fixed wall.
- **\(\rho=\rho_c\):** belongs to the low-ratio half of this proof and to
  the post-\(k_5\) residual owner. The cap-\(26\) payment is strict by
  (23).
- **\(\rho=1/5\), \(13/25\):** each fixed/moving bridge agrees on the
  split face, with the positive reserves (26) and (31).
- **\(\rho=1/4\):** both spectral inventories apply. Equation (19)
  excludes \(\ell=5,n=1\), while (28) excludes every \(n\geq2\); neither
  side loses the face.
- **\(\rho=7/8\):** included in the closed theorem (2) and already owned
  theorem-wise at the endpoint. It is excluded from the genuinely new set
  and from both residual formulas.
- **\(\rho=5/6\) and \(K=U(\rho)\):** the upper-floor owner is unchanged;
  the candidate only subtracts points strictly below \(U\).

All count caps use complete multiplicities. Accidental equality between
different entry walls can only omit a channel under strict counting and
cannot enlarge any displayed cap.

## 11. Verdict and first unsupported implication

The proposed high-ratio extension through \(k_6\) is **proved as an exact
analytic candidate**, using the separately authenticated new zero record
and the internal fixed-channel min--max comparison. The proposed split at
\(1/4\), radial split at \(1/5\), and angular split at \(13/25\) are all
valid on their complete closed faces. Exact subtraction is (4).

**First unsupported implication: none.** The result remains unpromoted
until clean-room reconstruction, independent constant verification, and a
judge State Patch are completed. No statement is made for \(K>k_6\), and
no progress on \(\rho_*<\rho<\rho_c\) is claimed here.
