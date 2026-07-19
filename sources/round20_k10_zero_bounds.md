# Source Card: Round 20 \(k_{10}\) Zero-Bound Repair

Status: **mixed qualified-source/internal proof completed on 2026-07-15**.

This card authorizes exactly

\[
 \boxed{j_{7/2,2}>\frac{103}{10}},
 \tag{Z1}
\]

\[
 \boxed{j_{15/2,1}>\frac{23}{2}},
 \tag{Z2}
\]

and the statement-level Lorch specialization

\[
 \boxed{j_{19/2,1}>\frac{64}{5}}.
 \tag{Z3}
\]

The internal angular comparison at the same radial index also gives

\[
 \boxed{
 j_{p+1/2,2}^{\,2}>
 \frac{9409}{100}+p(p+1)\qquad(p\geq3).}
 \tag{Z4}
\]

In particular,

\[
 j_{9/2,2}>\frac{53}{5},\qquad
 j_{11/2,2}>11,
 \tag{Z5}
\]

and

\[
 j_{13/2,2}^{\,2}>\frac{13609}{100}
 >\left(\frac{23}{2}\right)^2.
 \tag{Z6}
\]

No numerical root table or numerical root solver is used.

## 1. Exact provenance and division of labor

| input | SHA-256 / URL | exact use |
|---|---|---|
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` | authenticated DLMF spherical formula for order \(3\), and the already reconstructed derivative-chain enumeration of the first two roots of its numerator |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` | exact Lorch formula and the qualified specialization \(j_{15/2,1}>54/5\) |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | authenticated statement and scope of Lorch's strict first-zero inequality |
| NIST DLMF 10.51.1 | <https://dlmf.nist.gov/10.51.E1> | spherical-Bessel three-term recurrence |
| NIST DLMF 10.51.2 | <https://dlmf.nist.gov/10.51.E2> | spherical-Bessel derivative recurrence |

The DLMF statements used here are

\[
 \mathsf j_{n-1}(x)+\mathsf j_{n+1}(x)
 =\frac{2n+1}{x}\mathsf j_n(x)
 \tag{D1}
\]

and

\[
 \mathsf j_n'(x)
 =\mathsf j_{n-1}(x)-\frac{n+1}{x}\mathsf j_n(x).
 \tag{D2}
\]

The links above are the direct NIST equation permalinks. Everything after
these labelled identities and Lorch's labelled first-zero inequality is
exact internal algebra, calculus, or min--max ordering. The inherited
arithmetic enclosure is

\[
 \frac{333}{106}<\pi<\frac{22}{7}.
 \tag{P}
\]

## 2. Sharpening the second order-\(7/2\) zero

For spherical order three, put

\[
 P_3(x)=(15-6x^2)\sin x+(x^3-15x)\cos x.
 \tag{1}
\]

The inherited derivative-chain reconstruction proves that \(P_3\) has
exactly one second positive root in \((3\pi,7\pi/2)\), and that \(P_3\)
is strictly increasing throughout this cell. We now locate that root
strictly to the right of

\[
 a=\frac{103}{10}.
\]

The enclosure (P) gives \(3\pi<a<7\pi/2\). Write \(y=a-3\pi\). Then

\[
 0<y<u:=\frac{232}{265}<1.
 \tag{2}
\]

For \(0<y<1\), alternating Taylor bounds give

\[
 \sin y<S(y):=y-\frac{y^3}{6}+\frac{y^5}{120},
 \qquad
 \cos y>C(y):=1-\frac{y^2}{2}+\frac{y^4}{24}-\frac{y^6}{720}>0.
 \tag{3}
\]

Here \(S\) is increasing and \(C\) is decreasing. Exact substitution at
\(u\) gives

\[
 \frac54 C(u)-S(u)
 =\frac{409676235487517}{12467453135062500}>0.
 \tag{4}
\]

Consequently \(\tan y<5/4\). On the other hand,

\[
 \frac{a(a^2-15)}{6a^2-15}-\frac32
 =\frac{5917}{621540}>0.
 \tag{5}
\]

Since \(\sin a=-\sin y\) and \(\cos a=-\cos y\), equations (3)--(5)
give

\[
 P_3(a)
 =\cos y\big((6a^2-15)\tan y-a(a^2-15)\big)<0.
\]

The unique second root lies to the right of \(a\). The positive zeros of
\(\mathsf j_3\) and \(J_{7/2}\) coincide, so

\[
 \boxed{j_{7/2,2}>\frac{103}{10}}.
\]

## 3. Angular propagation of the sharpened second zero

Let \(d_p=p(p+1)\). For \(p\geq3\), the unit-ball fixed-channel forms
have the same min--max domain and potential difference

\[
 \frac{d_p-d_3}{r^2}\geq d_p-d_3
 \qquad(0<r\leq1).
\]

Thus, at radial index two,

\[
 j_{p+1/2,2}^{\,2}
 \geq j_{7/2,2}^{\,2}+d_p-d_3
 >\frac{10609}{100}+d_p-12
 =\frac{9409}{100}+d_p.
 \tag{6}
\]

For \(p=4,5,6\), respectively,

\[
 \frac{11409}{100}>\left(\frac{53}{5}\right)^2,
 \qquad
 \frac{12409}{100}>11^2,
 \qquad
 \frac{13609}{100}>\left(\frac{23}{2}\right)^2.
 \tag{7}
\]

This proves (Z4)--(Z6).

## 4. An internal repair of the first order-\(15/2\) wall

Define

\[
 P_n(x)=x^{n+1}\mathsf j_n(x).
\]

Equations (D1)--(D2) give, by direct algebra,

\[
 P_{n+1}=(2n+1)P_n-x^2P_{n-1},
 \qquad
 P_n'=xP_{n-1}.
 \tag{8}
\]

Starting from \(P_0=\sin x\) and
\(P_1=\sin x-x\cos x\), recurrence (8) yields

\[
\begin{aligned}
 P_6(x)={}&
 (10395-4725x^2+210x^4-x^6)\sin x\\
 &+(-10395x+1260x^3-21x^5)\cos x,
 \tag{9}
\end{aligned}
\]

and

\[
\begin{aligned}
 P_7(x)={}&
 (135135-62370x^2+3150x^4-28x^6)\sin x\\
 &+(-135135x+17325x^3-378x^5+x^7)\cos x.
 \tag{10}
\end{aligned}
\]

Put \(a_0=54/5\), \(b_0=23/2\). At \(a_0\), the two polynomial
coefficients in (9) are

\[
 A_6=\frac{11397242079}{15625}>0,
 \qquad
 B_6=-\frac{5033180754}{3125}<0.
 \tag{11}
\]

Write \(\delta=7\pi/2-a_0\). From (P),
\(0<\delta<1/5\). Hence

\[
 \tan\delta
 <\frac{\delta}{1-\delta^2/2}
 <\frac{10}{49}<\frac14,
 \tag{12}
\]

while \(A_6/|B_6|>1/4\), since

\[
 4(11397242079)-25165903770=20423064546>0.
\]

Using
\(\sin a_0=-\cos\delta\) and
\(\cos a_0=-\sin\delta\), equations (11)--(12) show

\[
 P_6(a_0)=|B_6|\sin\delta-A_6\cos\delta<0.
 \tag{13}
\]

Direct Taylor expansion of (9) gives
\(P_6(x)=x^{13}/135135+O(x^{15})>0\) for sufficiently small positive
\(x\). Together with (13), this places the first positive zero before
\(a_0\). Equation (7) places the second positive zero strictly to the
right of \(b_0\). Therefore \(P_6\) has no zero on \([a_0,b_0]\), and
(13) gives

\[
 P_6(x)<0\qquad(a_0\leq x\leq b_0).
 \tag{14}
\]

By (8), \(P_7'=xP_6<0\) throughout this interval.

At \(b_0\), the two coefficients in (10) are

\[
 A_7=-\frac{284564833}{16},
 \qquad
 B_7=-\frac{3153151489}{128}.
 \tag{15}
\]

Put \(v=4\pi-b_0\). Then \(0<v<\pi/2\), and (P) gives

\[
 v>\frac{113}{106}.
 \tag{16}
\]

Elementary differentiation gives
\(\tan v>v+v^3/3\) on \((0,\pi/2)\). Exact arithmetic yields

\[
 \frac{113}{106}+\frac13\left(\frac{113}{106}\right)^3
 -\frac75
 =\frac{1248169}{17865240}>0,
 \tag{17}
\]

whereas

\[
 \frac75-\frac{|B_7|}{|A_7|}
 =\frac{169873203}{11382593320}>0.
 \tag{18}
\]

Since \(\sin b_0=-\sin v\) and \(\cos b_0=\cos v\), equations
(15)--(18) imply

\[
 P_7(b_0)=|A_7|\sin v-|B_7|\cos v>0.
 \tag{19}
\]

Thus \(P_7>0\) on all of \([a_0,b_0]\). The authenticated Lorch seed
\(j_{15/2,1}>a_0\) excludes every earlier zero. Hence

\[
 \boxed{j_{15/2,1}>\frac{23}{2}}.
\]

This strengthening is internal once the qualified Lorch seed at the same
order and radial index is admitted; it is not attributed to Lorch.

## 5. Qualified Lorch specialization at order \(19/2\)

For angular index \(\ell=9\), the exact half-integer reduction of
Lorch's published strict inequality is

\[
 j_{19/2,1}^{\,2}>
 R_9:=\frac{63\sqrt{165}-147}{4}.
 \tag{20}
\]

The comparison \(R_9>(64/5)^2\) is equivalent to

\[
 1575\sqrt{165}>20059.
\]

Both sides are positive, and

\[
 1575^2\cdot165-20059^2=6939644>0.
\]

Therefore

\[
 \boxed{j_{19/2,1}>\frac{64}{5}}.
\]

This is a statement-level use of the formula printed in the primary SIAM
publisher abstract. The proof of Lorch's theorem remains access-controlled;
only the displayed specialization and its exact algebra are authorized.

## 6. Transfer and scope exclusions

Zero extension from a shell fixed-channel form domain to the corresponding
unit-ball fixed-channel form domain gives, at the same radial index,

\[
 q_{p,n}^{\rm shell}(\rho)^2\geq j_{p+1/2,n}^{\,2}.
 \tag{21}
\]

Subject to that separately proved internal min--max lemma, this card
therefore authorizes the strict shell walls

\[
 q_{3,2}>\frac{103}{10},\quad
 q_{4,2}>\frac{53}{5},\quad
 q_{5,2}>11,\quad
 q_{7,1}>\frac{23}{2},\quad
 q_{9,1}>\frac{64}{5}.
 \tag{22}
\]

This card supplies no shell cross-product zero, multiplicity count, Weyl
payment, residual subtraction, or theorem-level claim. It does not enlarge
Lorch to a second radial zero: (Z1) is an internal tangent-cell proof, and
(Z2) is an internal recurrence argument seeded only by Lorch's already
audited first-zero exclusion at the identical order.

**Verdict: PASS for exactly (Z1)--(Z6) and the conditional shell transfer
(22). First unsupported implication: none.**
