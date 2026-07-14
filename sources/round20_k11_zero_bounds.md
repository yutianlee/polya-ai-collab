# Source Card: Round 20 \(k_{11}\) Zero Bounds

Status: **mixed qualified-source/internal proof completed on 2026-07-15**.

This card authorizes exactly

\[
 \boxed{j_{5/2,3}>\frac{61}{5}},
 \tag{Z1}
\]

\[
 \boxed{j_{11/2,2}>\frac{129}{10}},
 \tag{Z2}
\]

and the statement-level Lorch specialization

\[
 \boxed{j_{21/2,1}>\frac{69}{5}}.
 \tag{Z3}
\]

The same-index angular comparison also gives

\[
 \boxed{
 j_{p+1/2,3}^{\,2}>
 \frac{3571}{25}+p(p+1)
 \qquad(p\geq2),}
 \tag{Z4}
\]

and

\[
 \boxed{
 j_{p+1/2,2}^{\,2}>
 \frac{13641}{100}+p(p+1)
 \qquad(p\geq5).}
 \tag{Z5}
\]

No numerical root table, decimal zero approximation, or root solver is
used.

## 1. Provenance and exact division of labor

| input | SHA-256 / URL | exact use |
|---|---|---|
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` | authenticated half-integer spherical-Bessel reduction and the derivative chain \(R'=x\sin x\), \(Q'=xR\) |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` | authenticated recurrence for \(P_n=x^{n+1}\mathsf j_n\), same-index angular min--max comparison, and shell zero-extension transfer |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` | exact half-integer reduction of Lorch's strict first-zero inequality |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | authenticated statement and scope of the strict Lorch inequality |

The inherited rational enclosure is

\[
 \frac{333}{106}<\pi<\frac{22}{7}.
 \tag{P}
\]

Everything below except the explicitly labelled Lorch specialization is
internal exact algebra, calculus, elementary ODE uniqueness, or min--max
ordering.

## 2. The third order-\(5/2\) zero

Put

\[
 R(x)=\sin x-x\cos x,
 \qquad
 Q(x)=(3-x^2)\sin x-3x\cos x.
 \tag{1}
\]

Direct differentiation gives

\[
 R'(x)=x\sin x,
 \qquad
 Q'(x)=xR(x).
 \tag{2}
\]

The numerator of \(\mathsf j_2\) is \(Q\). The derivative chain gives a
complete enumeration of its first three positive roots.

On \((0,\pi)\), \(R>0\), so \(Q\) increases from zero. On
\((\pi,2\pi)\), \(R\) decreases through exactly one zero in
\((\pi,3\pi/2)\). Hence \(Q\) first increases and then decreases; since

\[
 Q(\pi)=3\pi>0,
 \qquad
 Q(2\pi)=-6\pi<0,
\]

there is exactly one first root in this cell.

On \((2\pi,3\pi)\), \(R\) increases through exactly one zero in
\((2\pi,5\pi/2)\). Thus \(Q\) first decreases and then increases, and

\[
 Q(2\pi)<0,
 \qquad
 Q(3\pi)=9\pi>0
\]

give exactly one second root. Finally, on \((3\pi,4\pi)\), \(R\)
decreases through exactly one zero in \((3\pi,7\pi/2)\). The function
\(Q\) first increases and then decreases, while

\[
 Q(3\pi)>0,
 \qquad
 Q(4\pi)=-12\pi<0.
\]

Consequently this cell contains exactly the third positive root, and
\(Q\) is strictly decreasing on \((7\pi/2,4\pi)\).

Set \(a=61/5\) and \(\delta=4\pi-a\). The enclosure (P) gives

\[
 \frac{7\pi}{2}<a<4\pi,
 \qquad
 \delta>\frac{97}{265}.
 \tag{3}
\]

Moreover,

\[
 \frac{97}{265}-\frac{3a}{a^2-3}
 =\frac{111187}{966190}>0.
 \tag{4}
\]

Since \(0<\delta<\pi/2\), one has \(\tan\delta>\delta\), and therefore

\[
\begin{aligned}
 Q(a)
 &=\cos\delta\big((a^2-3)\tan\delta-3a\big)>0.
\end{aligned}
\]

The unique third root in this decreasing cell lies strictly to the right
of \(a\). The positive zeros of \(\mathsf j_2\) and \(J_{5/2}\)
coincide, proving (Z1).

## 3. The second order-\(11/2\) zero

For \(P_n=x^{n+1}\mathsf j_n\), the authenticated spherical recurrence
gives

\[
 P_{n+1}=(2n+1)P_n-x^2P_{n-1}.
 \tag{5}
\]

Starting with \(P_0=\sin x\) and
\(P_1=\sin x-x\cos x\), exact recurrence yields

\[
\begin{aligned}
 P_5(x)={}&(945-420x^2+15x^4)\sin x\\
 &+(-945x+105x^3-x^5)\cos x.
 \tag{6}
\end{aligned}
\]

Put \(b=129/10\) and \(\varepsilon=b-4\pi\). Then

\[
 0<\varepsilon<u:=\frac{177}{530}.
 \tag{7}
\]

At \(b\), the two polynomial coefficients in (6) are

\[
 A=\frac{692874243}{2000}>0,
 \qquad
 B=-\frac{14401867149}{100000}<0.
 \tag{8}
\]

For \(0<\varepsilon<u<1\), elementary sine and cosine bounds give

\[
 \tan\varepsilon
 <\frac{u}{1-u^2/2}<\frac38,
 \qquad
 \frac38-\frac{u}{1-u^2/2}
 =\frac{90453}{4243768}>0.
 \tag{9}
\]

The coefficient ratio satisfies

\[
 \frac{|B|}{A}-\frac38
 =\frac{69653091}{1710800600}>0.
 \tag{10}
\]

Since \(\sin b=\sin\varepsilon\) and
\(\cos b=\cos\varepsilon>0\), equations (8)--(10) show

\[
 P_5(b)=\cos\varepsilon\,(A\tan\varepsilon+B)<0.
 \tag{11}
\]

Near the origin, direct expansion gives
\(P_5(x)=x^{11}/10395+O(x^{13})>0\). On the other hand, (Z1) and angular
form ordering at radial index three imply

\[
 j_{11/2,3}^{\,2}
 \geq j_{5/2,3}^{\,2}+30-6
 >\frac{4321}{25}
 =\left(\frac{129}{10}\right)^2+\frac{643}{100}.
 \tag{12}
\]

Positive Bessel zeros are simple by ODE uniqueness. Thus (12) allows at
most two positive zeros of \(P_5\) below \(b\), while the sign change
from the origin to (11) forces an odd number. Exactly one lies below
\(b\), so the second lies strictly above it. This proves (Z2).

## 4. Angular propagation

At fixed radial index, the unit-ball angular potential comparison gives

\[
 j_{p+1/2,n}^{\,2}
 \geq j_{\ell+1/2,n}^{\,2}+p(p+1)-\ell(\ell+1)
 \qquad(p\geq\ell).
 \tag{13}
\]

Applying (13) to (Z1) with \(\ell=2,n=3\) gives

\[
 j_{p+1/2,3}^{\,2}
 >\frac{3721}{25}+p(p+1)-6
 =\frac{3571}{25}+p(p+1),
\]

which is (Z4). Applying it to (Z2) with \(\ell=5,n=2\) gives

\[
 j_{p+1/2,2}^{\,2}
 >\frac{16641}{100}+p(p+1)-30
 =\frac{13641}{100}+p(p+1),
\]

which is (Z5).

## 5. Qualified first-zero specialization at order \(21/2\)

At angular index \(\ell=10\), the authenticated half-integer reduction
of Lorch's published strict first-zero inequality is

\[
 j_{21/2,1}^{\,2}>R_{10}:=138\sqrt3-46.
 \tag{14}
\]

The comparison \(R_{10}>(69/5)^2\) is equivalent to

\[
 3450\sqrt3>5911.
\]

Both sides are positive, and exact squaring gives

\[
 3450^2\cdot3-5911^2=767579>0.
\]

This proves (Z3). It is a statement-level specialization of the formula
printed in the primary publisher abstract; it is not an internal proof
of Lorch's theorem.

## 6. Shell transfer and scope

Zero extension from a shell channel to the corresponding unit-ball form
domain gives

\[
 q_{p,n}^{\rm shell}(\rho)^2\geq j_{p+1/2,n}^{\,2}.
 \tag{15}
\]

Subject to that separately proved min--max lemma, this card authorizes

\[
 q_{2,3}>\frac{61}{5},
 \qquad
 q_{5,2}>\frac{129}{10},
 \qquad
 q_{10,1}>\frac{69}{5},
\]

together with the shell versions of (Z4)--(Z5).

This card supplies no shell cross-product zero, multiplicity count, Weyl
payment, residual subtraction, or theorem-level claim. Lorch is used only
for the first zero at order \(21/2\); both higher-radial bounds are
internal.

**Verdict: PASS for exactly (Z1)--(Z5) and the conditional shell transfer
above. First unsupported implication: none.**
