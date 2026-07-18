# Clean-room audit of B-positive.tex

Date: 2026-07-16  
Audited file: manuscript/analytic/B-positive.tex  
Verdict: **PASS**

The proof was reconstructed independently from its definitions. The tangent
majorant, the sign of the \(d_\rho\)-coefficient, the order of the
substitutions, both rational lower envelopes, both affine changes of
variable, both Bernstein conversions, every printed Bernstein numerator,
and both common denominators are correct. No numerical or interval
certificate is used.

## 1. Starting definitions

At \(K=200\),
\[
\mu=200\rho,\qquad
b=\frac{2\pi\rho}{1-\rho},\qquad
c=200b=\frac{400\pi\rho}{1-\rho},\qquad
\overline R=\mu+\frac12 .
\]
Substitution in the aggregate reserve gives exactly
\[
\mathcal B
=(\mu-\tfrac12)(200\eta_\rho-1)
+\frac{d_\rho}{2}(\mu-\tfrac32)(\mu-\tfrac12)
-(1+d_\rho)\overline{\mathcal I}
-\frac{8(\mu+\tfrac12)}{15\sqrt\mu}.
\]
Thus no scaling factor is missing from the assertion.

With \(u=\overline R/\sqrt c\),
\[
\overline{\mathcal I}
=\frac c2\left[
u\sqrt{1+u^2}+\operatorname{arsinh}u-u^2
\right]
=cH(u).
\]
The scaled identity is exact.

## 2. Audit of the \(H\)-tangent

Differentiation gives
\[
H'(u)=\sqrt{1+u^2}-u,\qquad
H''(u)=\frac{u}{\sqrt{1+u^2}}-1<0.
\]
Therefore a tangent line is a global upper majorant.

At
\[
u_0=\frac{589}{300}
\]
the claimed radical is exact because
\[
300^2+589^2=436921=661^2.
\]
Consequently
\[
\sqrt{1+u_0^2}=\frac{661}{300},\qquad
H'(u_0)=\frac{661-589}{300}=\frac6{25},
\]
and
\[
u_0+\sqrt{1+u_0^2}=\frac{1250}{300}=\frac{25}{6}.
\]
Direct simplification gives
\[
H(u_0)-\frac6{25}u_0
=\frac12\left(\log\frac{25}{6}-\frac{589}{1250}\right),
\]
as printed.

The logarithmic estimate is also correct. For \(n\ge1\),
\[
\frac{2}{(2n+1)3^{2n+1}}
<\frac{2}{3}3^{-(2n+1)},
\]
and
\[
\sum_{n=1}^\infty3^{-(2n+1)}=\frac1{24}.
\]
Hence
\[
\log2<\frac23+\frac1{36}=\frac{25}{36}.
\]
Using \(\log(1+x)<x\),
\[
\log\frac{25}{6}
=2\log2+\log\frac{25}{24}
<\frac{25}{18}+\frac1{24}
=\frac{103}{72}.
\]
Finally,
\[
\frac{1789}{1250}-\frac{103}{72}
=\frac{29}{45000}>0.
\]
It follows that the tangent intercept is strictly less than \(12/25\),
and therefore
\[
H(u)<\frac6{25}u+\frac{12}{25}
\]
for every \(u>0\). This part passes without qualification.

## 3. Audit of the integral majorant

From the tangent,
\[
\overline{\mathcal I}
<\frac{6\overline R\sqrt c}{25}+\frac{12c}{25}.
\]
Young's inequality
\[
\sqrt c\leq\frac{c}{2a}+\frac a2
\]
then gives
\[
\overline{\mathcal I}
<\frac{3\overline Rc}{25a}
+\frac{3a\overline R}{25}
+\frac{12c}{25}.
\]
Since
\[
c< c_+(\rho)=\frac{8800}{7}\frac{\rho}{1-\rho}
\]
and every coefficient of \(c\) in this expression is positive, replacement
of \(c\) by \(c_+\) preserves the upper-bound direction. The printed
\(Q_a\) is therefore correct for every rational \(a>0\).

## 4. Audit of the \(d_\rho\)-coefficient

Let
\[
\Phi(\rho)=\overline R^2\frac{1-\rho}{\rho}.
\]
Independent differentiation gives
\[
\frac{\Phi'}{\Phi}
=\frac{200\rho-400\rho^2-\tfrac12}
{\rho(1-\rho)\overline R}.
\]
The critical points are
\[
q_\pm=\frac{10\pm7\sqrt2}{40}.
\]
The inequalities
\[
q_-<\frac1{200}<\frac7{51}<q_+
<\frac{41}{80}<\frac{39}{50}
\]
follow from \(7/5<\sqrt2<3/2\). The derivative is positive between
\(q_-\) and \(q_+\), and negative afterward. Thus on the required interval
\(\Phi\) increases and then decreases, and its minimum is indeed attained
at one of the two endpoints.

Using \(\pi<22/7\),
\[
u^2>\frac{7\overline R^2(1-\rho)}{8800\rho}.
\]
The independently recomputed endpoint values are
\[
\frac{8128201}{2080800},\qquad
\frac{685783}{124800}.
\]
Their differences from \(225/64\) are exactly
\[
\frac{1625777}{4161600},\qquad
\frac{247033}{124800},
\]
so \(u>15/8\) throughout.

Consequently
\[
\frac{\overline{\mathcal I}}{\overline R^2}
<\frac6{25u}+\frac{12}{25u^2}
\leq\frac{496}{1875}.
\]
Also \(\overline R\ge2851/102>27\), and
\[
f(R)=\frac{(R-2)(R-1)}{2R^2}
\]
has derivative
\[
f'(R)=\frac{3R-4}{2R^3}>0\qquad(R>4/3).
\]
Thus
\[
\frac{(\mu-\tfrac32)(\mu-\tfrac12)}
{2\overline R^2}
\geq\frac{325}{729}.
\]
The final difference is exactly
\[
\frac{325}{729}-\frac{496}{1875}
=\frac{82597}{455625}>0.
\]
The coefficient
\[
A-\overline{\mathcal I},\qquad
A=\frac12(\mu-\tfrac32)(\mu-\tfrac12),
\]
is therefore strictly positive, as required.

## 5. Logical order of replacing \(d_\rho\) and \(\overline{\mathcal I}\)

This is the point at which an otherwise correct-looking proof could reverse
an inequality. The dependence on \(d=d_\rho\) and
\(I=\overline{\mathcal I}\) is
\[
dA-(1+d)I=-I+d(A-I).
\]
Because the preceding lemma proves \(A-I>0\), a lower bound \(d>d_*\)
first gives
\[
-I+d(A-I)>-I+d_*(A-I)
=d_*A-(1+d_*)I.
\]
Only after fixing \(d_*\) may one use \(I<Q_a\):
\[
d_*A-(1+d_*)I
>d_*A-(1+d_*)Q_a,
\]
because \(1+d_*>0\).

Thus the valid order is:

1. lower \(d_\rho\) while retaining the actual \(I\);
2. then upper-bound \(I\) by \(Q_a\).

That is the logical order invoked after Lemma 2 in the source. Reversing
the two operations would require the unproved sign of \(A-Q_a\), but the
source does not make that reversal.

The coefficient of \(\eta_\rho\) is \(200(\mu-1/2)>0\), so lowering
\(\eta_\rho\) is valid. Likewise, \(E<E_*\) implies \(-E>-E_*\).
Therefore both implications \(\mathcal B>L_<\) and
\(\mathcal B>L_>\) are sound.

## 6. Audit of the lower rational envelope

On \(7/51\leq\rho\leq1/2\),
\[
\eta_\rho
=\frac{\sqrt3}{2\pi}-\frac16
>\frac{5}{3}\frac7{44}-\frac16
=\frac{13}{132}.
\]
Since \(\arcsin\rho>\rho\) and \(2/\pi>7/11\),
\[
d_\rho>\frac7{11}\rho.
\]

The error bound uses
\[
\frac{1400}{51}\leq\mu\leq100,\qquad
\left(\frac{26}{5}\right)^2<\frac{1400}{51}.
\]
Hence
\[
\sqrt\mu\leq10,\qquad
\frac1{2\sqrt\mu}<\frac5{52},
\]
and
\[
\frac8{15}\left(\sqrt\mu+\frac1{2\sqrt\mu}\right)
<\frac{70}{13}.
\]
Thus every constant in \(L_<\), including the choice \(a=18>0\), has the
correct direction.

## 7. Audit of the upper rational envelope

For \(1/2\leq\rho\leq39/50\),
\[
\eta_\rho\geq
\frac{2\sqrt2}{3\pi}(1-\rho)^{3/2}
>\frac{49}{165}(1-\rho)^{3/2}.
\]
Since
\[
1-\rho\geq\frac{11}{50}>
\left(\frac{23}{50}\right)^2,
\]
one has
\[
\sqrt{1-\rho}>\frac{23}{50},
\]
and therefore
\[
\eta_\rho>
\frac{49}{165}\frac{23}{50}(1-\rho)
=\frac{1127}{8250}(1-\rho).
\]

The first four positive terms of the \(\arcsin\) series are
\[
P_7(\rho)=\rho+\frac{\rho^3}{6}
+\frac{3\rho^5}{40}+\frac{5\rho^7}{112}.
\]
The omitted terms are positive for \(0<\rho<1\), so
\[
d_\rho>\frac7{11}P_7(\rho).
\]

Finally,
\[
100\leq\mu\leq156<169
\]
implies
\[
\sqrt\mu<13,\qquad
\frac1{2\sqrt\mu}\leq\frac1{20},
\]
and hence
\[
E<\frac{174}{25}<7.
\]
Every constant in \(L_>\), including \(a=67>0\), is valid.

## 8. Independent exact replay of the lower Bernstein identity

Using only rational polynomial arithmetic, independent expansion gives
\[
\begin{aligned}
(1-\rho)L_<(\rho)
={}&-\frac{339191}{21450}
+\frac{543570899}{200200}\rho
-\frac{266665673}{46200}\rho^2\\
&+\frac{398072}{33}\rho^3
-\frac{140000}{11}\rho^4.
\end{aligned}
\]
The affine coordinate
\[
x_<=\frac{102\rho-14}{37}
\]
maps \(7/51\) to \(0\) and \(1/2\) to \(1\).

Applying the printed Bernstein-conversion formula independently produced
the following reduced coefficients \(b_k\). The final column gives the exact
integer \(D_</\operatorname{den}(b_k)\), proving that the printed common
denominator clears every coefficient.

| \(k\) | independently recomputed \(b_k\) | \(D_</\operatorname{den}(b_k)\) |
|---:|---:|---:|
| 0 | \(241670701639/879476130\) | \(12320\) |
| 1 | \(272289458051147/637361524800\) | \(17\) |
| 2 | \(1169822714393/2205403200\) | \(4913\) |
| 3 | \(15805777553/24504480\) | \(442170\) |
| 4 | \(1468237453/2402400\) | \(4510134\) |

With
\[
D_<=10835145921600,
\]
multiplication \(D_<b_k\) gives, in order,
\[
\begin{gathered}
2977383044192480,\quad
4628920786869499,\quad
5747338995812809,\\
6988840660610010,\quad
6621947656848702.
\end{gathered}
\]
These match all five printed \(N_{<,k}\) exactly. The denominator is
positive, \(N_{<,0}\) is the minimum, and
\[
N_{<,0}-60D_<=2327274288896480>0.
\]
The lower Bernstein closure passes.

## 9. Independent exact replay of the upper Bernstein identity

The affine coordinate
\[
x_>=\frac{25}{7}\left(\rho-\frac12\right)
\]
maps \(1/2\) to \(0\) and \(39/50\) to \(1\). Independent rational
expansion of \(L_>\) has degree ten, as required.

The independently recomputed reduced Bernstein coefficients and exact
denominator-clearing multipliers are:

| \(k\) | independently recomputed \(b_k\) | \(D_>/\operatorname{den}(b_k)\) |
|---:|---:|---:|
| 0 | \(47440856629/135168000\) | \(18402099609375\) |
| 1 | \(133665375845923/377344000000\) | \(6591796875\) |
| 2 | \(3624646313478031/10188288000000\) | \(244140625\) |
| 3 | \(16719737823335577/47168000000000\) | \(52734375\) |
| 4 | \(16451155854950637/47168000000000\) | \(52734375\) |
| 5 | \(267944735006349893929/795960000000000000\) | \(3125\) |
| 6 | \(3487150603851515793551/11055000000000000000\) | \(225\) |
| 7 | \(9351830612403095155121/33165000000000000000\) | \(75\) |
| 8 | \(192612549930910220351033/829125000000000000000\) | \(3\) |
| 9 | \(44655795022274967410993/276375000000000000000\) | \(9\) |
| 10 | \(320583170500935444017/5025000000000000000\) | \(495\) |

With
\[
D_>=2487375000000000000000,
\]
the eleven products \(D_>b_k\) are exactly
\[
\begin{gathered}
873011369240936279296875,\\
881095006796855712890625,\\
884923416376472412109375,\\
881704924277462068359375,\\
867541422038412498046875,\\
837327296894843418528125,\\
784608885866591053548975,\\
701387295930232136634075,\\
577837649792730661053099,\\
401902155200474706698937,\\
158688669397963044788415.
\end{gathered}
\]
They match every printed \(N_{>,k}\). The denominator is positive,
\(N_{>,10}\) is the minimum, and
\[
N_{>,10}-60D_>
=9446169397963044788415>0.
\]
The upper Bernstein closure passes.

## 10. Final inference and dependency boundary

Bernstein basis functions are nonnegative and sum to one. Since every
coefficient exceeds \(60\), both identities imply
\[
(1-\rho)L(\rho)>60.
\]
On the full interval \(0<1-\rho<1\), so division gives
\[
L(\rho)>\frac{60}{1-\rho}>60.
\]
Together with \(\mathcal B>L\), this proves the stated theorem, including
all interval endpoints and the overlap at \(\rho=1/2\).

The replay used exact rational arithmetic only. No decimal estimate,
floating-point sign, interval enclosure, or unprinted case is needed.

**Final result: PASS. No mathematical gap found.**
