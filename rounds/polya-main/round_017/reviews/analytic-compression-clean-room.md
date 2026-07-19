# Round 17 analytic-compression clean-room review

## Initial verdict

**PASS.** Candidate C17 is true exactly as stated.  There is no unsupported
implication in the reconstruction below.

This verdict was reached before consulting any incumbent proof, response,
certification artifact, ledger, review, freeze record, prompt, Git diff, or
other Round 17 file.  The only inputs read were the following three files,
after independently checking their SHA-256 hashes.

| whitelisted input | checked SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `state/lemma_packets/SHELL-rho-compact-round17.md` | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |

## 1. Elementary constants used below

I first reconstruct the rational bounds

\[
\frac{157}{50}<\pi<\frac{22}{7}. \tag{1}
\]

For the lower bound, put $a=\arctan(1/5)$ and
$b=\arctan(1/239)$.  Two applications of the tangent double-angle
formula give

\[
\tan(4a)=\frac{120}{119},\qquad
\tan(4a-b)=
\frac{120\cdot239-119}{119\cdot239+120}=1.
\]

The angles are in the principal branch, so this is Machin's identity
$\pi/4=4a-b$.  The alternating integral/Taylor bounds

\[
x-\frac{x^3}{3}<\arctan x<x\qquad(0<x<1)
\]

then give

\[
\frac\pi4>
4\left(\frac15-\frac{1}{3\cdot5^3}\right)-\frac1{239}
=\frac{70369}{89625}>\frac{157}{200};
\]

the numerator in the last comparison is exactly $2675>0$ after using
the common denominator $89625\cdot200$.

For the upper bound, polynomial division gives the exact positive-integral
identity

\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\int_0^1\left(x^6-4x^5+5x^4-4x^2+4-
\frac4{1+x^2}\right)dx
=\frac{22}{7}-\pi.
\]

This proves (1) without a numerical approximation to any spectral root.
I will also use $\sqrt3<7/4$, which follows by squaring two positive
numbers.

Write throughout

\[
d=1-\rho,\qquad z=\frac\pi d,\qquad
k_1=(z^2+2)^{1/2},\qquad k_2=(z^2+6)^{1/2}.
\tag{2}
\]

On the claimed closed band, $0<d<1$; hence every denominator and every
radicand in (2) is positive.

## 2. Complete spectral reconstruction in the window

The permitted separated-spectrum theorem says that the radial operator in
angular order $\ell$ is

\[
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
\quad\hbox{on }(\rho,1)
\]

with Dirichlet endpoints, and that its $n$-th eigenvalue
$\lambda_{\ell,n}$ has global multiplicity $2\ell+1$.  The Dirichlet
eigenvalues of $-d^2/dr^2$ on this interval are $n^2z^2$.  Since
$r<1$ in the open interval, min--max gives

\[
\lambda_{\ell,n}\ge n^2z^2+\ell(\ell+1),                    \tag{3}
\]

and, for $\ell\ge1$, the first-eigenfunction Rayleigh quotient gives the
strict version

\[
\lambda_{\ell,1}>z^2+\ell(\ell+1).                          \tag{4}
\]

Indeed, the Poincare term is at least $z^2$, while

\[
\ell(\ell+1)\int_\rho^1(1/r^2-1)|u|^2\,dr>0

\]

for every nonzero first eigenfunction.  For $\ell=0$ there is equality:

\[
\lambda_{0,n}=n^2z^2.                                       \tag{5}
\]

Because $z>\pi>3$, one has

\[
4z^2>z^2+6.                                                  \tag{6}
\]

Equations (3)--(6) give the requested low-mode ledger:

| angular order | multiplicity | first radial index | second radial index | consequence for $K^2\le z^2+6$ |
|---|---:|---|---|---|
| $\ell=0$ | $1$ | $\lambda_{0,1}=z^2$ | $\lambda_{0,2}=4z^2>z^2+6$ | only $n=1$ can count |
| $\ell=1$ | $3$ | $\lambda_{1,1}>z^2+2=k_1^2$ | $\lambda_{1,2}\ge4z^2+2>z^2+6$ | only $n=1$, and only above $k_1$, can count |
| $\ell=2$ | $5$ | $\lambda_{2,1}>z^2+6=k_2^2$ | $\lambda_{2,2}\ge4z^2+6>z^2+6$ | neither can count |

All $n\ge2$, in every angular channel, are excluded by (3) and (6).
All $\ell\ge2$, including every remaining first radial mode, are excluded
by (4).  Thus no unlisted radial or angular mode can occur anywhere in the
band.

The strict global counting rule now yields the exact alternatives

\[
N_D(A_{\rho,1},K^2)=
\begin{cases}
0,&K=z,\\
1,&z<K\le k_1,\\
1+3\,\mathbf 1_{\{\lambda_{1,1}<K^2\}},&k_1<K\le k_2.
\end{cases}                                                  \tag{7}
\]

In particular, the last line is at most $4$.  If
$K^2=\lambda_{1,1}$, all three $m$-states are excluded by the strict
endpoint convention.  At $K=k_2$, the five $\ell=2$ states are also
excluded because (4) is strict.  No noncoincidence of different angular
orders has been assumed: if a cross-order numerical coincidence occurs,
the orthogonal multiplicities add, and if it occurs at $K^2$, all states
at that value are excluded.  Within this particular window, (4)--(6) in
fact leave no second active angular order with which the possible
$(1,1)$ value could coincide.

This explicitly tests $K=z,k_1,k_2$, both first radial indices, angular
orders $0,1,2$, all multiplicities, and every remaining mode.

## 3. Uniform Weyl inequality

Set

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

At $K=z$, (7) gives $N_D=0<W$.  If $z<K\le k_1$, then

\[
W(\rho,K)>W(\rho,z)
=\frac{2\pi^2}{9}\frac{1+\rho+\rho^2}{(1-\rho)^2}>2>1=N_D, \tag{8}
\]

where $0<\rho<1$ and $\pi>3$ were used.

It remains to pay for the possible multiplicity $1+3$ above $k_1$.
Define

\[
W_1(\rho)=W(\rho,k_1)
=\frac{2}{9\pi}
(3-3d+d^2)\frac{(\pi^2+2d^2)^{3/2}}{d^2}.                  \tag{9}
\]

Both positive factors after $2/(9\pi)$ are strictly decreasing functions
of $d\in(0,1)$.  For the first this follows from $2d-3<0$.  For the
second, its logarithmic derivative is

\[
\frac{6d}{\pi^2+2d^2}-\frac2d
=\frac{2(d^2-\pi^2)}{d(\pi^2+2d^2)}<0.                    \tag{10}
\]

Every denominator in (10) is positive.  Therefore $W_1$ is strictly
increasing in $\rho=1-d$, and its minimum on the claimed ratio interval
is at

\[
\rho_c=\frac1{1+2\pi}.
\]

At this point

\[
d_c=\frac{2\pi}{1+2\pi},\qquad z_c=\pi+\frac12.
\]

The reconstructed bounds (1) imply

\[
\rho_c<\frac17,\qquad
1-\rho_c^3>\frac{342}{343},\qquad
k_1(\rho_c)^2>
\left(\frac{91}{25}\right)^2+2
=\frac{9531}{625}>\left(\frac{39}{10}\right)^2.           \tag{11}
\]

All quantities being positive, taking the positive square root and then
the cube preserves the last inequality.  Also
$2/(9\pi)>7/99$.  Hence exact rational arithmetic gives

\[
W_1(\rho)\ge W_1(\rho_c)
>\frac7{99}\frac{342}{343}\left(\frac{39}{10}\right)^3
=\frac{20287098}{4851000}>4,                               \tag{12}
\]

since $20287098-4\cdot4851000=883098>0$.

For $k_1<K\le k_2$, (7) and (12) therefore give

\[
N_D(A_{\rho,1},K^2)\le4<W_1(\rho)<W(\rho,K).
\]

Together with (8) and the strict lower spectral face, this proves (3) on
the **complete closed band**

\[
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_2(\rho).
\]

No squaring with an unknown sign was used: all square-root comparisons in
(6), (11), and (12) have positive sides.  The only inverse inequalities
used have explicitly positive denominators.  Equations (9)--(10) prove,
rather than assume, the monotonicity needed for the uniform constant.

## 4. Exact residual-mask inclusion

I now prove

\[
\mathcal C_{17}\subset\mathcal D_{16}                     \tag{13}
\]

directly against every disjunct of the frozen predicate.

First note

\[
0<\omega_0=\frac{\sqrt3}{2\pi}-\frac16<\frac18<\rho_c.    \tag{14}
\]

The upper bound follows from $\sqrt3<7/4$ and $\pi>3$; the lower bound
follows, for example, from $\pi<22/7<3\sqrt3$.  The final inequality in
(14) follows from $\pi<22/7<7/2$.  Since
$C_0=1+8\sqrt2/15>1$,

\[
\rho_*=\frac{\omega_0}{2C_0}<\frac1{16}<\rho_c.            \tag{15}
\]

Thus every point of $\mathcal C_{17}$ has
$\rho_*<\rho<7/8$ and $K>0$.

For $\rho\ge\rho_c$, exact rearrangement through the positive quantity
$2\rho(1-\rho)$ gives

\[
z=\frac\pi{1-\rho}\ge\frac1{2\rho},                       \tag{16}
\]

with equality exactly at $\rho=\rho_c$.  Since $K>z$, both lower-ray
coverage conditions are false:

\[
2\rho K>1,\qquad (1-\rho)K>\pi.                            \tag{17}
\]

The small-hole branch is also false because (14) gives
$\rho\ge\rho_c>\omega_0$.

For all $\rho\le7/8$, (1) gives

\[
z\le8\pi<\frac{176}{7},\qquad
k_2^2<\frac{176^2}{7^2}+6
=\frac{31270}{49}<26^2.                                   \tag{18}
\]

Both sides are positive, so $k_2<26$.

It remains to test the fixed-ratio upper branch, including its formula
interface at $\rho=1/2$.  For $0\le s<1$,

\[
G_1(s)=\frac1\pi\int_s^1\arccos t\,dt>0,\qquad
G_1'(s)=-\frac{\arccos s}{\pi}<0.                          \tag{19}
\]

Consequently $\eta_\rho$ is positive, constant up to $\rho=1/2$,
continuous there, and decreasing afterwards.  Meanwhile
$a_\rho=2\pi\rho/(1-\rho)$ is strictly increasing.  If
$y=\sqrt{K_0}$, then $y$ is the unique positive root of

\[
\eta_\rho y^2-\sqrt{a_\rho}\,y-C_0=0.                    \tag{20}
\]

Increasing $a_\rho$, or decreasing positive $\eta_\rho$, makes the
left side at the old positive root negative; uniqueness of the positive
root then moves it to the right.  Thus $K_0$ is increasing, continuously
through $\rho=1/2$.  There is no zero denominator in its displayed
formula because $\eta_\rho>0$.

At $\rho=\rho_c<1/2$, one has $a_{\rho_c}=1$ and
$\eta_{\rho_c}=\omega_0$.  Since $C_0>0$, the positive-root formula
therefore gives

\[
K_0(\rho_c)>\frac1{\omega_0^2}>64.                         \tag{21}
\]

By monotonicity, (18)--(21) imply, uniformly on $\mathcal C_{17}$,

\[
K\le k_2<26<64<K_0(\rho).                                  \tag{22}
\]

Thus the A5 upper ray never covers a candidate point.  This proves the
needed strict comparison with the active $K_0$ upper branch on both sides
of the $\rho=1/2$ formula change.

At the next mask switch, $\rho=5/6$, the Round 15 seam begins
inclusively.  If its ratio condition $d\le1/6$ holds, then (18) gives

\[
Kd^2<\frac{26}{36}=\frac{13}{18}<54,                       \tag{23}
\]

so its frequency condition is false, including at $\rho=5/6$.  In the
normalized mask language, $K<26<1944\le54/d^2$.  The retained A7 branch
requires $d\le1/8$, which is impossible because
$\rho<7/8$ in $\mathcal C_{17}$; A8 and A9, requiring respectively
$d\le1/10$ and $d\le1/25$, are impossible as well.

Finally, the complete ratio faces A0 and A1 do not apply by (15) and the
strict inequality $\rho<7/8$, and the global A10 face does not apply
because

\[
K<26<87025=295^2.                                          \tag{24}
\]

Thus every primitive analytic-coverage disjunct A0--A10 is false, while
the point lies strictly inside $I_{16}\times[0,\infty)$.  By the frozen
definition
$\mathcal D_{16}=(I_{16}\times[0,\infty))\setminus\mathcal A_{16}$,
this proves (13), with both frequency inequalities strict.  In particular,
the included $K=k_2$ face remains strictly below every applicable old
upper branch.

For clarity, the old-face ownership and all requested switch tests are:

| face or interface | exact result |
|---|---|
| $\rho=\rho_c$ | this is not an old complete vertical face; at $K=z$ only, A2 and A3 share ownership because $2\rho_cz=1$; for $K>z$ through $k_2$, the points are in $\mathcal C_{17}\subset\mathcal D_{16}$ |
| $\rho=7/8$ | A1 owns the complete closed vertical face; this face is proved spectrally above but is excluded from $\mathcal C_{17}$; A3 additionally owns its $K=z$ point |
| $K=z$ | A3 owns the complete lower face and strict counting gives zero; at $\rho_c$, A2 also owns it |
| $K=k_1$ | strict count is exactly $1$, because $\lambda_{1,1}>k_1^2$ |
| $K=k_2$ | count is $1$ or $4$; $\ell=2$ is strictly excluded, and equality of $\lambda_{1,1}$ with the endpoint excludes its multiplicity $3$ |
| $\rho=1/2$ | $\eta_\rho$ changes formula but is continuous; (19)--(22) hold on both sides and on the face |
| $\rho=5/6$ | the A6 ratio condition starts inclusively, but (23) is strict; its old upper face is $K=1944$, far above $k_2<26$ |
| $K=295^2$ | A10 owns the equality face, which is disjoint from the candidate band by (24) |

The $H_0$ upper branch is inapplicable throughout because
$\rho\ge\rho_c>\omega_0$; the applicable $K_0$ and seam branches have
both been tested strictly.

## 5. Complete $B_0$-containment check

The verdict is

\[
\boxed{B_0\subset\mathcal C_{17}}.                         \tag{25}
\]

Indeed, $\rho_c<1/7<999/2000$, and
$1001/2000<7/8$.  Since $z_\rho$ and $k_2(\rho)$ are increasing in
$\rho$, their relevant extrema on the closed ratio interval of $B_0$
are

\[
\max z_\rho=\frac{2000\pi}{999}
<\frac{44000}{6993}<\frac{67}{10},                         \tag{26}
\]

where the final cross-multiplication is
$440000<468531$, and

\[
\min k_2(\rho)^2=\left(\frac{2000\pi}{1001}\right)^2+6
>\left(\frac{6280}{1001}\right)^2+6
>\left(\frac{168}{25}\right)^2.                           \tag{27}
\]

For the last exact comparison in (27), the positive cross-multiplied
difference is

\[
45450406\cdot625-28224\cdot1002001
=126027526>0.
\]

All quantities in (27) are positive, so taking the positive square root is
legitimate.  Equations (26)--(27) imply, simultaneously for every point of
the box,

\[
z_\rho<K\le\frac{168}{25}<k_2(\rho).
\]

The coordinatewise extrema prove the assertion on both closed ratio faces,
both closed frequency faces, and all four corners, not merely in the
interior.  Thus the complete Round 8 box is contained in the proposed new
analytic set (although the frozen bookkeeping correctly continues to regard
it as certified coverage overlaid on the analytic residual before C17 is
promoted).

## Final clean-room conclusion

The strict endpoint convention, all low multiplicities, possible
cross-order coincidences, every remaining mode, the uniform Weyl constant,
all mask branches and switch faces, the global $295^2$ face, and every
closed face of $B_0$ have been accounted for.  Candidate C17 passes, and
there is no first unsupported implication to report.
