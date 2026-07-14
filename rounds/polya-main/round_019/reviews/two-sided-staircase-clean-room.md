# Round 19 clean-room analytic review: two-sided staircase

## Initial verdict

**PASS. First unsupported implication: none.**

I reached this verdict without reading an incumbent response, a lower-ratio
exploration, a source-audit review, a computation/verifier, a repository
diff, another Round 19 review, or a judge file. The argument below is an
independent reconstruction from the frozen claim and its six whitelisted
dependencies.

## Authentication and isolation record

These are all the files I read and the SHA-256 hashes I computed from the
bytes I used:

| input actually read | computed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `rounds/polya-main/round_019/exploration/residual-mask-freeze.md` | `0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |

The candidate and all six dependency hashes agree with the freeze. The
freeze file itself is the additional second row above.

## 1. Elementary constant certificate

I used

\[
 \frac{333}{106}<\pi<\frac{22}{7}.
\tag{1}
\]

For completeness, this is not a decimal assumption. Put
\(a=\arctan(1/5)\), \(b=\arctan(1/239)\). The tangent addition formula
gives

\[
 \tan(4a)=\frac{120}{119},\qquad \tan(4a-b)=1,
\]

and the angle lies in \((0,\pi/2)\), so \(\pi=4(4a-b)\). Alternating
arctangent sums give

\[
 a>\frac15-\frac1{3\,5^3}+\frac1{5\,5^5}-\frac1{7\,5^7},
 \qquad b<\frac1{239},
\]

and

\[
 a<\frac15-\frac1{3\,5^3}+\frac1{5\,5^5},
 \qquad b>\frac1{239}-\frac1{3\,239^3}.
\]

The resulting rational bounds satisfy

\[
 \frac{1231847548}{392109375}-\frac{333}{106}
 =\frac{3418213}{41563593750}>0,
\]

\[
 \frac{22}{7}-\frac{670143059704}{213311234375}
 =\frac{1845738322}{1493178640625}>0.
\]

Thus (1), and hence every later use of it, has an elementary exact
certificate.

Write \(q_{\ell,n}\) for the shell frequency in angular channel \(\ell\)
and radial index \(n\). I retain

\[
 z=\frac{\pi}{1-\rho},\quad L=\frac1{2\rho},\quad
 k_m=(z^2+m(m+1))^{1/2},\quad
 p_1=(4z^2+2)^{1/2},\quad d=\frac{\sqrt{337}}2.
\]

All denominators below are positive because \(0<\rho<1\). Every square
root is the positive root, and every squaring below is between positive
quantities.

## 2. Form domains and the two comparison principles

In a fixed shell channel the transformed radial form is

\[
 a_\ell[u]=\int_\rho^1\left(|u'|^2+
 \frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
 \qquad D(a_\ell)=H_0^1(\rho,1).
\tag{2}
\]

The one-dimensional Dirichlet eigenvalues on \((\rho,1)\) are
\(n^2z^2\), and \(r^{-2}\ge1\). The min--max principle therefore gives

\[
 \boxed{q_{\ell,n}^2\ge n^2z^2+\ell(\ell+1).}
\tag{3}
\]

For \(\ell=0\) this is an equality:

\[
 q_{0,n}=nz.
\tag{4}
\]

For the unit ball, the transformed fixed-channel form is

\[
 b_\ell[v]=\int_0^1\left(|v'|^2+
 \frac{\ell(\ell+1)}{r^2}|v|^2\right)dr,
 \qquad D(b_\ell)=H_0^1(0,1).
\tag{5}
\]

The domain assertion is important: Hardy's inequality makes the
\(r^{-2}\) term finite on all of \(H_0^1(0,1)\), including at the origin.
If \(u\in H_0^1(\rho,1)\), extension by zero on \((0,\rho)\) lies in
\(H_0^1(0,1)\), preserves the \(L^2\) norm and the form value, and remains
in the same angular harmonic subspace. Thus the ball form domain is the
larger min--max domain and

\[
 \boxed{q_{\ell,n}^2\ge j_{\ell+1/2,n}^2.}
\tag{6}
\]

This proves the required direction, preserves both \(\ell\) and \(n\),
and does not appeal to unlabelled domain monotonicity.

The ball forms for different angular orders have the same domain. If
\(\ell\ge s\), then

\[
 b_\ell[v]
 =b_s[v]+(\ell(\ell+1)-s(s+1))\int_0^1\frac{|v|^2}{r^2}dr
 \ge b_s[v]+(\ell(\ell+1)-s(s+1))\|v\|_2^2.
\]

Consequently

\[
 \boxed{j_{\ell+1/2,n}^2\ge j_{s+1/2,n}^2+
 \ell(\ell+1)-s(s+1).}
\tag{7}
\]

This is the required ball angular-shift comparison, with its form domain
and direction explicit.

The shell operators are positive by (3), so zero is not an
eigenfrequency. The zeros \(j_{\nu,n}\) used below always mean positive
zeros. The removable zeros of elementary spherical-Bessel numerators at
the origin are never counted. The strict global count is

\[
 N_D(A_{\rho,1},K^2)=
 \sum_{\ell\ge0}(2\ell+1)\#\{n:q_{\ell,n}<K\}.
\tag{8}
\]

Coincident frequencies from distinct angular orders contribute the sum
of their full multiplicities. At \(K\) equal to one or several
frequencies, every equal mode is excluded.

## 3. Zero bounds, including the two internal bounds

The five sourced statements have exactly the following scope:

\[
\begin{array}{c|c|c|c}
\nu&\ell&n&\text{strict positive-zero bound}\\ \hline
5/2&2&1&j_{5/2,1}>51/10\\
7/2&3&1&j_{7/2,1}>13/2\\
9/2&4&1&j_{9/2,1}>15/2\\
11/2&5&1&j_{11/2,1}>17/2\\
3/2&1&2&j_{3/2,2}>77/10.
\end{array}
\tag{9}
\]

No statement in (9) is used at a different order or radial index. The
translation to shell modes is (6), not a source claim.

### 3.1 The internal bound \(j_{3/2,1}>4\)

The positive spherical order-one zeros solve \(\tan x=x\). On
\((0,\pi/2)\), \(\tan x-x>0\); on \((\pi/2,\pi)\), the tangent is
negative; and on \((\pi,3\pi/2)\), \(\tan x-x\) is strictly increasing
from a negative value to \(+\infty\). Hence the first positive zero is
the unique root in that last interval. Since \(\pi<4<3\pi/2\), put
\(y=3\pi/2-4\). From \(\pi>3\), \(y>1/2\), while \(0<y<\pi/2\). Thus

\[
 \tan4=\cot y<\frac1y<2<4.
\]

The unique root is therefore greater than \(4\).

### 3.2 Complete enumeration for \(j_{5/2,2}>9\)

For \(x>0\),

\[
 \mathsf j_2(x)=
 \frac{g(x)}{x^3},\qquad
 g(x)=(3-x^2)\sin x-3x\cos x.
\tag{10}
\]

First,

\[
 g'(x)=x(\sin x-x\cos x).
\]

The factor in parentheses has derivative \(x\sin x>0\) on \((0,\pi)\)
and vanishes at zero. Hence \(g>0\) throughout \((0,\pi]\). For
\(x>\sqrt3\) and away from tangent poles, (10) vanishes exactly when

\[
 \tan x=R(x):=\frac{3x}{3-x^2}.
\tag{11}
\]

There is no zero on \((\pi,3\pi/2)\), or on any later positive-tangent
half-period, because there \(\tan x>0>R(x)\). On every negative-tangent
half-period

\[
 ((m+\tfrac12)\pi,(m+1)\pi),\qquad m\ge1,
\]

put \(F=\tan-R\). For \(x>3\),

\[
 R'(x)=\frac{3(x^2+3)}{(x^2-3)^2}<1\le\sec^2x,
\]

so \(F'>0\). It rises from \(-\infty\) at the left tangent pole to
\(-R((m+1)\pi)>0\) at the right endpoint. Thus there is exactly one zero
in each such negative-tangent half-period and none in any intervening
half-period. Tangent poles themselves are not zeros because
\(g=(3-x^2)\sin x\ne0\); multiples of \(\pi\) are not zeros because
\(g=-3x\cos x\ne0\); and \(x=\sqrt3\) is not a zero. This enumerates all
positive zeros: the first lies in \((3\pi/2,2\pi)\), the second in
\((5\pi/2,3\pi)\), and so on.

Now \(5\pi/2<9<3\pi\). With \(y=3\pi-9\), (1) gives

\[
 0<y<\frac\pi2,
 \qquad y>\frac{999}{106}-9=\frac{45}{106}>\frac9{26}.
\]

Since \(\tan y>y\),

\[
 \tan9=-\tan y<-\frac9{26}=R(9).
\]

Thus \(F(9)<0\). The unique root in \((5\pi/2,3\pi)\) lies to the right
of \(9\), proving

\[
 \boxed{j_{5/2,2}>9.}
\tag{12}
\]

By (7), (9), and (12),

\[
 j_{\ell+1/2,1}^2>
 \frac{289}{4}+\ell(\ell+1)-30\ge\frac{337}{4}
 \quad(\ell\ge6),
\tag{13}
\]

and

\[
 j_{\ell+1/2,2}^2>
 81+\ell(\ell+1)-6\ge87>\frac{337}{4}
 \quad(\ell\ge3).
\tag{14}
\]

These are the exact propagations needed below.

## 4. Exhaustive spectral inventories and caps

### 4.1 High-ratio inventory through \(k_6\)

For \(\rho\ge\rho_c\),

\[
 z\ge z_{\rho_c}=\pi+\frac12>\frac72.
\]

Equation (3) gives the following exclusions through \(K=k_6\):

* every \(\ell\ge6,n\ge1\), because its first lower bound is at least
  \(k_6\);
* every \(n\ge3\), because \(9z^2>z^2+42\);
* every \(\ell\ge2,n=2\), because
  \(4z^2+6>z^2+42\), equivalently \(z^2>12\).

At each equality the strict count still excludes the mode.

If \(\rho\le1/4\), then \(z\le4\pi/3<11/2\), so

\[
 k_6^2=z^2+42<\frac{121}{4}+42=\frac{289}{4}.
\]

The \(\ell=5,n=1\) mode is absent by (6) and (9). Thus the only possible
modes are first modes \(0\le\ell\le4\) and second modes
\((\ell,n)=(0,2),(1,2)\).

If \(\rho\ge1/4\), then \(z>4\), whence \(4z^2>z^2+42\). Every second
mode is absent, and the only possible modes are first modes
\(0\le\ell\le5\). Both conclusions hold at \(\rho=1/4\): there
\(k_6<17/2\) and \(k_6<2z\), so neither the \(\ell=5\) first mode nor a
second mode occurs.

The cumulative first-mode multiplicities are

\[
1,\quad 1+3=4,\quad 9,\quad16,\quad25,\quad36.
\tag{15}
\]

The exact \(\ell=0,n=2\) mode adds one, and the possible
\(\ell=1,n=2\) mode adds three, giving the advertised caps \(26,29\).
The first-mode delay thresholds are (3) together with (9):

\[
\begin{array}{c|c|c}
\text{mode}&\text{lower bounds on its frequency}&\text{cap after entry}\\ \hline
(1,1)&k_1&4\\
(2,1)&k_2,\ 51/10&9\\
(3,1)&k_3,\ 13/2&16\\
(4,1)&k_4,\ 15/2&25\\
(5,1)&k_5,\ 17/2&36\\
(0,2)&2z&26\\
(1,2)&p_1,\ 77/10&29.
\end{array}
\tag{16}
\]

No ordering between the two entries in a row of (16) is assumed.

### 4.2 Lower-ratio inventory through \(d\)

For \(\rho>1/\sqrt{337}\), (1) gives \(3z>3\pi>d\) (squaring, one may
check \(4\cdot999^2>337\cdot106^2\)). Hence all \(n\ge3\) modes are
absent. Equations (6), (13), and (14) exclude every first mode
\(\ell\ge6\) and every second mode \(\ell\ge3\). The exhaustive possible
inventory is therefore first modes \(0\le\ell\le5\) and second modes
\(0\le\ell\le2\), exactly as claimed.

The fixed thresholds satisfy

\[
 4<\frac{51}{10}<\frac{13}{2}<\frac{15}{2}<
 \frac{77}{10}<\frac{17}{2}<9<d;
\]

the final inequality is \(324<337\). From the internal \(j_{3/2,1}>4\),
(9), (12), the exact \(q_{0,2}=2z\), and multiplicities
\(1,3,5,7,9,11\), the count caps are

\[
\begin{array}{c|c}
\text{frequency range}&N_D\text{ cap}\\ \hline
L<K\le4&1\\
4<K\le51/10&4\\
51/10<K\le13/2,\ K\le2z&9\\
51/10<K\le13/2,\ K>2z&10\\
13/2<K\le15/2,\ K\le2z&16\\
13/2<K\le15/2,\ K>2z&17\\
15/2<K\le77/10&26\\
77/10<K\le17/2&29\\
17/2<K\le9&40\\
9<K\le d&45.
\end{array}
\tag{17}
\]

In fact, throughout this ratio interval,

\[
 \frac{13}{2}<2z<\frac{15}{2}.
\tag{18}
\]

For the lower bound use \(1/\sqrt{337}>1/19\) and (1):
\(2z>(19/9)(333/106)=703/106>13/2\). For the upper bound use
\(2z<2z_{\rho_c}=2\pi+1<15/2\). Thus the proposed cap-10 subband in
(17) is empty, while the split in the next row is genuine. Keeping the
empty row is harmless and its hypothetical cap is paid below.

Also \(p_1<77/10\) throughout this interval: at \(\rho_c\),
\(z=\pi+1/2<51/14\), so

\[
 p_1^2<\frac{2699}{49}<\frac{5929}{100}.
\]

Thus the sourced second-zero bound is the stronger delay here.

Every lower threshold in (17) is open. At an exact threshold the delayed
mode remains absent; at \(K=2z\), the exact second \(\ell=0\) mode is
also absent by strict counting. The upper face \(K=d\) remains in the
last row.

For clarity, the requested \(n=1,2,3\), \(\ell=0,\ldots,6\) audit is:

| region | \(n=1\) | \(n=2\) | \(n=3\) and above |
|---|---|---|---|
| \(\rho_c\le\rho\le1/4, K\le k_6\) | \(\ell=0,\ldots,4\) possible; \(\ell=5,6\) absent | only \(\ell=0,1\) possible | all absent |
| \(1/4\le\rho\le7/8, K\le k_6\) | \(\ell=0,\ldots,5\) possible; \(\ell=6\) absent | all absent | all absent |
| \(1/\sqrt{337}<\rho<\rho_c, K\le d\) | \(\ell=0,\ldots,5\) possible; \(\ell=6\) absent | \(\ell=0,1,2\) possible; \(\ell=3,\ldots,6\) absent | all absent |

Higher angular orders follow from (3), (7), (13), and (14); higher radial
indices follow from radial eigenvalue ordering and (3).

## 5. Exact Weyl payments

Put

\[
 W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

It is strictly increasing in \(K>0\), and for fixed \(K\) it is strictly
decreasing in \(\rho\). If \(T^2=az^2+b\), then direct differentiation
shows that \(W(\rho,T(\rho))\) is increasing provided

\[
 a\pi^2(1+\rho)>b\rho^2(1-\rho)^2.
\tag{19}
\]

For \(z,2z,k_1,\ldots,k_6,p_1\), one has \(b/a\le42\), while
\(\rho^2(1-\rho)^2\le1/16\) and \(\pi^2>9>42/16\). Hence every moving
payment used below is strictly increasing. This also supplies all
derivative signs and legitimizes the extremal substitutions.

### 5.1 High-ratio fixed payments

From \(1/\pi>7/22\),

\[
 W(r,c)>\frac7{99}(1-r^3)c^3.
\]

At every proposed fixed/moving split, the fixed side has the following
positive rational margin:

| split \(r\) | fixed threshold \(c\) | cap | lower bound minus cap |
|---:|---:|---:|---:|
| \(3/10\) | \(51/10\) | 9 | \(1387329/11000000\) |
| \(1/2\) | \(13/2\) | 16 | \(6277/6336\) |
| \(1/2\) | \(15/2\) | 25 | \(775/704\) |
| \(13/25\) | \(17/2\) | 36 | \(452843/343750\) |
| \(1/5\) | \(77/10\) | 29 | \(849901/281250\) |

Thus these payments hold on the entire side \(\rho\le r\).

### 5.2 High-ratio moving payments

For a split \(r\) and \(T^2=az^2+b\), define the rational lower bounds

\[
 A=\frac{a(333/106)^2}{(1-r)^2}+b,
 \qquad B=\frac7{99}(1-r^3).
\]

Then \(W(r,T)>BA^{3/2}\). All quantities are positive, so the payment
\(W(r,T)>C\) follows from \(\Delta=B^2A^3-C^2>0\). The exact certificates
are:

| moving threshold and split | \(C\) | \(A\) | \(B\) | exact \(\Delta\) |
|---|---:|---:|---:|---:|
| \(k_1,\ r=1/8\) | 4 | \(2049506/137641\) | \(3577/50688\) | \(153864824754340538785/348796101192617852928\) |
| \(k_2,\ r=3/10\) | 9 | \(3598071/137641\) | \(6811/99000\) | \(1399810848073457853053/394237491401523000000\) |
| \(k_3,\ r=1/2\) | 16 | \(144597/2809\) | \(49/792\) | \(137027505353736631/514922437748928\) |
| \(k_4,\ r=1/2\) | 25 | \(167069/2809\) | \(49/792\) | \(2507119282010251109/13902905819221056\) |
| \(k_5,\ r=13/25\) | 36 | \(13093905/179776\) | \(10444/171875\) | \(92672404686738742434741/709259556128000000000\) |
| \(p_1,\ r=1/5\) | 29 | \(2862113/44944\) | \(868/12375\) | \(373255772037478993002833/868931613701316000000\) |

By (19), each payment holds on the entire side \(\rho\ge r\). Both the
fixed and moving certificates hold at each split, so both one-sided traces
are controlled.

Since
\[
 \rho_c>\frac18
 \quad\Longleftrightarrow\quad \pi<\frac72,
\]
which follows from (1), monotonicity also gives

\[
 W(\rho_c,2z)>W(1/8,2z)>
 \frac{3597732}{137641}=26+\frac{19066}{137641}>26,
\tag{20}
\]

and

\[
 W(\rho_c,z)>\frac{899433}{275282}>1.
\tag{21}
\]

The first row of the moving table gives \(W(\rho,k_1)>4\) for all
\(\rho\ge\rho_c\).

The warned-against shortcut really is unavailable. At \(\rho_c\),
\(z=\pi+1/2<51/14\), hence \(k_5<33/5\), and

\[
 W(\rho_c,k_5)<\frac2{27}\left(\frac{33}{5}\right)^3<25.
\tag{22}
\]

No step below uses a uniform \(W(\rho,k_5)>25\). The delayed
\(\ell=4\) threshold and its \(15/2\) payment are exactly what closes
that gap.

### 5.3 Lower-ratio payments

Here \(\rho<\rho_c<7/50\): indeed,
\(14\pi>14(333/106)=2331/53>43\), which is equivalent to the second
inequality. For every fixed \(c\),

\[
 W(\rho,c)>
 \frac7{99}\left(1-\left(\frac7{50}\right)^3\right)c^3.
\]

The exact margins needed for (17) are:

| threshold \(c\) | cap paid | lower bound minus cap |
|---:|---:|---:|
| 4 | 4 | \(793292/1546875\) |
| \(51/10\) | 9 | \(486236661/1375000000\) |
| \(13/2\) | 16 | \(333100003/99000000\) |
| \(15/2\) | 26 | \(329797/88000\) |
| \(77/10\) | 29 | \(3590476297/1125000000\) |
| \(17/2\) | 40 | \(327078887/99000000\) |
| 9 | 45 | \(8805519/1375000\) |

For the initial cap, \(W(\rho,L)\) is decreasing in \(\rho\), and

\[
 W(\rho_c,L(\rho_c))
 =\frac16+\frac\pi3+\frac{2\pi^2}{9}
 >\frac{19}{6}>1.
\tag{23}
\]

Thus \(K>L\) pays cap 1 strictly. Finally,
\(1/\sqrt{337}>1/19\), and (19) gives

\[
 W(\rho,2z)>W(1/19,2z)>
 16\frac{127}{108}=\frac{508}{27}>17.
\tag{24}
\]

This pays cap 17 and also the empty cap-10 row. Every cap in the proposed
tables has now been paid, on both sides of every fixed/moving split.

## 6. Proof of both candidate bands

### 6.1 High-ratio band

At \(K=z\), (3)--(4) give \(N_D=0<W\). For \(K>z\), use the exhaustive
inventory in Section 4.1 and classify by the highest present category:

* if only the \(\ell=0\) first mode is present, \(N_D\le1\) and (21)
  pays it;
* if \((1,1)\) is present but none of the later categories is, then
  \(N_D\le4\), its presence forces \(K>k_1\), and the first moving
  certificate pays it;
* presence of the \(\ell=2,3,4,5\) first mode gives respectively the
  caps \(9,16,25,36\). Each presence forces \(K\) strictly above both
  lower bounds in its row of (16), and the fixed/moving certificates at
  \(3/10,1/2,1/2,13/25\) pay the appropriate cap;
* if \((0,2)\) is present, the low-ratio high-band inventory has total
  cap 26, and its exact entry \(K>2z\) is paid by (20);
* if \((1,2)\) is present, the total cap is 29, its presence forces
  \(K>p_1\) and \(K>77/10\), and the two certificates at \(\rho=1/5\)
  pay it.

For \(\rho\le1/4\), the \(\ell=5\) first mode is absent; for
\(\rho\ge1/4\), all second modes are absent. Thus the categories cannot
combine to exceed the cap attached to the selected case. No ordering of
entries is used. If several channels coincide, the cumulative cap already
contains every full multiplicity, and equality itself excludes all
coincident modes.

It follows independently that

\[
 N_D(A_{\rho,1},K^2)<W(\rho,K)
\]

for every \(\rho_c\le\rho\le7/8\) and \(z\le K\le k_6\). This proves
the complete high-ratio statement, including the accepted old part and
the genuinely new face \(k_5<K\le k_6\).

### 6.2 Lower-ratio band

Use the exhaustive caps (17). If \(L<K\le4\), (23) gives
\(W(\rho,K)>1\). In every later fixed-threshold row, its lower endpoint
is open, so monotonicity in \(K\) and the lower fixed-payment table give
\(W\) strictly greater than the displayed cap. In the branch \(K>2z\),
(24) gives the stronger cap-17 payment. At \(K=2z\), strict counting
keeps the second \(\ell=0\) mode out and assigns the point to the smaller
cap. At \(K=d\), one has \(d>9\), so the strict payment from the last
row still applies.

Therefore

\[
 N_D(A_{\rho,1},K^2)<W(\rho,K)
\]

for every \(1/\sqrt{337}<\rho<\rho_c\) and \(L<K\le d\), proving the
lower-ratio statement with all strict and inclusive faces as claimed.

## 7. Upper-floor containment

First locate the lower endpoint. With

\[
 \omega_0=\frac{\sqrt3}{2\pi}-\frac16,
 \quad C_*=\frac12+\frac{8\sqrt2}{15},
 \quad C_0=1+\frac{8\sqrt2}{15},
\]

one has \(\omega_0<1/8\), \(C_*>5/4\), and \(C_0>3/2\). These follow
from (1), \(4\sqrt3<7\), \(32\sqrt2>45\), and
\(16\sqrt2>15\), respectively. Hence

\[
 \rho_* =\frac{\omega_0}{1+2C_*}<\frac1{28}<\frac1{19}<
 \frac1{\sqrt{337}}.
\tag{25}
\]

On the \(H_0\) branch, \(H_0\) is strictly increasing and

\[
 H_0(\rho_*)=\frac1{2\rho_*}=L(\rho_*)>d.
\]

Thus \(d<H_0(\rho)\) throughout the active branch, including its
one-sided limit at \(\rho_{HK}\).

For \(\rho<1/2\), \(\eta_\rho=G_1(1/2)=\omega_0\). If
\(x=\sqrt{K_0}\), its defining formula is the positive root of

\[
 \eta_\rho x^2-\sqrt{a_\rho}\,x-C_0=0.
\]

Therefore

\[
 K_0=x^2>\frac{C_0}{\eta_\rho}
 =\frac{C_0}{\omega_0}>12>d.
\tag{26}
\]

Equations (25)--(26), together with equality \(H_0=K_0\) at
\(\rho_{HK}\), prove

\[
 \boxed{d<U(\rho)\quad(\rho_*<\rho<\rho_c).}
\tag{27}
\]

For the high-ratio comparison, if \(\rho_c\le\rho\le1/2\), then
\(K_0>12\), while \(z\le2\pi<7\) gives \(k_6^2<91<12^2\). If
\(1/2<\rho<5/6\), then \(a_\rho>2\pi>6\). Direct differentiation gives
\(G_1'(t)=-\arccos(t)/\pi<0\) for \(0<t<1\), while the defining
expression (or its integral from \(t\) to 1) gives \(G_1(t)>0\). Hence
\(0<\eta_\rho\le\omega_0<1/8\). The defining formula gives

\[
 K_0>\frac{a_\rho}{\eta_\rho^2}>384,
\]

whereas \(z<6\pi<132/7\) gives \(k_6<20\). Finally, for
\(5/6\le\rho<7/8\), one has \(z<8\pi<26\), so \(k_6<27\), while

\[
 U(\rho)=\frac{54}{(1-\rho)^2}>54.
\]

Hence

\[
 \boxed{k_6(\rho)<U(\rho)\quad(\rho_c\le\rho<7/8).}
\tag{28}
\]

This checks both sides of the \(\rho=1/2\) formula interface and both
sides of the \(\rho=5/6\) active floor seam. At \(\rho_{HK}\), the
two low-ratio floor values agree and are both above \(d\). At
\(\rho=\omega_0\), the ineligible \(H_0\) term drops out only after
\(K_0\) was already the minimum, and (26) controls both traces.

## 8. Containment and exact residual subtraction

By (27),

\[
 \mathcal C_{19}^{\rm L}\subset
 \{\rho_*<\rho<\rho_c,\ L<K<U\}.
\]

By (28),

\[
 \mathcal C_{19}^{\rm H}\subset
 \{\rho_c\le\rho<7/8,\ k_5<K<U\}.
\]

Thus \(\mathcal C_{19}\subset\mathcal D_{18}\). The two additions are
disjoint because their ratio intervals are disjoint.

Let \(\rho_0=1/\sqrt{337}\). Since \(L(\rho_0)=d\), subtracting the
closed upper face \(K\le d\) only for \(\rho_0<\rho<\rho_c\) from the
low component leaves

\[
 \{\rho_*<\rho\le\rho_0,\ L<K<U\}
 \cup
 \{\rho_0<\rho<\rho_c,\ d<K<U\}.
\]

The equality slice \(\rho=\rho_0\) belongs to the first set: its proposed
new band is empty, because \(L=d\), and nothing is subtracted there.
Subtracting \(k_5<K\le k_6\) from the high component leaves

\[
 \{\rho_c\le\rho<7/8,\ k_6<K<U\}.
\]

Therefore the exact result is

\[
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le1/\sqrt{337},\ L<K<U\}\\
&\cup\{1/\sqrt{337}<\rho<\rho_c,\ d<K<U\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6<K<U\}.
\end{aligned}}
\tag{29}
\]

The inherited input already has \(B_0,B_1\subset\mathcal A_{18}\) and
\(\mathcal U_{18}=\mathcal D_{18}\). Equation (29) subtracts only from
\(\mathcal D_{18}\); neither box is subtracted a second time.

## 9. Mandatory wall and one-sided-trace audit

The following checks collect the boundary cases not already explicit in
the proof.

* **Ratio endpoints.** The face \(\rho=\rho_*\) is inherited covered and
  is outside (29). At \(\rho=1/\sqrt{337}\), \(L=d\), the new lower band
  is empty, and the unsplit residual slice remains. The lower band is open
  at \(\rho_c\), the high band is closed there, and
  \(L(\rho_c)=z(\rho_c)=\pi+1/2\). The high theorem includes
  \(\rho=7/8\), while its genuinely new residual subtraction is open
  there, consistently with the inherited complete endpoint owner.

* **Proposed ratio splits.** At \(1/5,3/10,1/2,13/25\), both the fixed
  and moving payment rows in Section 5 are strictly valid. Thus both
  one-sided traces and the equality slices are paid. At \(1/4\), both
  inventory arguments are valid and in fact both types of extra mode are
  absent. At \(5/6\), (28) holds from the \(K_0\) side and from the seam
  side, with the seam owning equality.

* **Active floor interfaces.** At \(\rho_{HK}\), \(H_0=K_0>d\); at
  \(\omega_0\), \(K_0>d\) on both traces; at \(1/2\),
  \(G_1(1/2)=\omega_0\) and both high containment estimates meet; at
  \(5/6\), the two branch estimates in (28) cover the left trace and the
  inclusive seam value. The face \(K=U\) remains inherited covered and
  is excluded from every component of (29).

* **Frequency faces.** The face \(K=L\) is open in the lower candidate.
  The face \(K=z\) is included in the high theorem and has count zero.
  At \(K=k_2,\ldots,k_6\), the corresponding lower-bound mode remains
  excluded; \(K=k_5\) keeps its inherited owner, and \(K=k_6\) belongs
  to the new theorem. At \(K=2z\), the exact \((0,2)\) mode is excluded.
  At \(K=p_1\), the \((1,2)\) mode is excluded by (3). At \(K=d\), the
  cap 45 and strict \(K>9\) payment apply. Every fixed threshold in
  (16)--(17) has the old, smaller cap at equality and the larger cap only
  above it.

* **Changing wall order in the high band.** The crossings
  \(2z=k_6\) and \(p_1=k_6\) are respectively
  \(z^2=14\) and \(z^2=40/3\), each unique because \(z\) increases.
  At either crossing the relevant second mode is excluded at the upper
  face. For \(\rho\ge1/4\), both radial walls lie above \(k_6\); for
  \(\rho\le1/4\), the presence-based cases in Section 6 do not require
  an ordering among \(2z,p_1,k_6,15/2,77/10\). Likewise, each first mode
  must clear both its moving and fixed bound, so a crossing or coincidence
  of those bounds can only create an empty subband, never an unpaid mode.

* **Changing wall order in the lower band.** The exact crossings of
  \(L\) with
  \(d,9,17/2,77/10,15/2,13/2,51/10,4\) occur at
  \[
  \frac1{\sqrt{337}},\ \frac1{18},\ \frac1{17},\
  \frac5{77},\ \frac1{15},\ \frac1{13},\ \frac5{51},\ \frac18.
  \]
  At each equality, \(L<K\le c\) is empty; below it the corresponding
  fixed-frequency row remains empty. The wall \(L=2z\) occurs at
  \(\rho=1/(1+4\pi)\), strictly between \(1/\sqrt{337}\) and
  \(\rho_c\): the upper inequality is immediate from
  \(1+4\pi>1+2\pi\), while the lower follows from
  \(1+4\pi<95/7<18<\sqrt{337}\). At equality, \(K=2z\) is still
  assigned to the lower cap.
  Equation (18) proves that \(2z\) never enters the earlier
  \((51/10,13/2]\) row or leaves the \((13/2,15/2]\) row. Thus every
  empty and degenerate lower subband is accounted for.

* **Radial and angular completeness.** Section 4 explicitly tests
  \(n=1,2,3\) and \(\ell=0,\ldots,6\), then excludes all remaining
  modes monotonically. Equations (4), (12)--(14) cover the exact radial
  modes and the proposed higher-mode exclusions. Full multiplicities are
  used throughout. Cross-order coincidences do not invalidate any cap.

* **Strictness and inversions.** All threshold implications have the
  form “mode present \(\Rightarrow K\) strictly exceeds its lower
  bound”; therefore monotonicity of \(W\) yields a strict payment even
  when the numerical payment at the lower bound was written non-strictly.
  The only inversion used for the lower-band nonemptiness is
  \(L<d\iff\rho>1/\sqrt{337}\), with both sides positive. All radical
  comparisons in Sections 3, 4, and 7 were squared only after positivity
  was established.

All mandatory falsification walls therefore have consistent ownership,
complete mode accounting, and a strict Weyl payment where a theorem is
claimed.

## Final conclusion

Both boxed candidate bands are proved, their proposed inventories and
caps are exhaustive, all fixed and moving payments are exact, the two
upper-floor comparisons are strict, and the residual subtraction is
exact. My clean-room verdict remains:

**PASS. First unsupported implication: none.**
