PASS. First unsupported implication: none.

# Round 19 two-sided staircase: fresh adversarial referee

Date: 2026-07-14

Role: fresh referee, independent of the incumbent and clean-room work

Frozen candidate baseline: 5814b335a108d3af25aadde312dcc9581172e9f6

Final review checkpoint inspected: bfb90c524c6cad195c5fc299e24aed25527b9fbc

I began from the contrary hypothesis that the frozen candidate was false. I
looked for a source-scope overreach, a wrong min--max direction, an omitted
mode, a cap continued past a moving wall, a non-strict Weyl payment, a lost
endpoint, and an incorrect set subtraction. None survived reconstruction.
The PASS below is for the frozen claims (3), (5), and (8), not for the full
shell Pólya conjecture and not for any point in the three residual components.

## 1. Byte authentication and provenance

The candidate and every dependency explicitly whitelisted by its freeze match
the recorded hashes. The later artifacts required by the referee commission
were independently hashed again after the final presentation-only cleanup.

| artifact actually read | observed SHA-256 |
|---|---|
| state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md | 87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db |
| rounds/polya-main/round_019/exploration/candidate-claim-freeze.md | 7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff |
| state/lemma_packets/SHELL-rho-compact-round19.md | 33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50 |
| rounds/polya-main/round_019/exploration/residual-mask-freeze.md | 0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9 |
| state/lemma_packets/SHELL-sturm-liouville-completeness.md | 6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8 |
| sources/lorch_bessel_zeros.md | 85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4 |
| sources/flps_balls.md | 27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38 |
| sources/round19_bessel_zero_bounds.md | 7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f |
| rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md | b9a86f1411a8e63c30b6ae5e2b3a65e167426f0b72a4447d15d4e833c5df6983 |
| rounds/polya-main/round_019/exploration/lower-ratio-route.md | 1a4cd1eb93c286816346ead50edef0f151f8b1a287186ba3b20e37336c16b681 |
| rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md | 24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17 |
| computations/round19_verify_two_sided_staircase.py | 4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23 |
| computations/tests/test_round19_verify_two_sided_staircase.py | 1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08 |
| rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md | fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7 |
| rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md | fe46d95718e4e070bdea18ee1c2fbcfc89d5eb3c53b5346d712c72715f667365 |

The auxiliary zero-dependency audit named by the incumbent also matches
ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718.
Both baseline identifiers above resolve to Git commits.

The A4 report contains the former test hash 58c825... under the expressly
historical headings “Results at freeze time” and “Output hashes before this
report was added.” The final test bytes differ only by removal of one terminal
blank line. The current hash is 1eea93..., the cross-comparison records that
current hash, and the same 24 tests pass. This chronology is not a mathematical
or provenance failure.

I also checked the primary statement boundary directly. The
[SIAM publisher abstract](https://epubs.siam.org/doi/10.1137/0524050)
identifies \(j_{\nu,1}\) as the first positive zero, gives the range
\(-1<\nu<\infty\), and prints exactly the two strict Lorch inequalities used
by the source cards. The body remains access-controlled, so this is correctly
labelled statement-level provenance. [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3)
is used only for the positive-factor identity between spherical and ordinary
Bessel functions, and [DLMF 10.49(i)](https://dlmf.nist.gov/10.49.i) only for
the elementary spherical formulas. The FLPS ball source is not used to infer
any shell zero or to subtract two ball inequalities; no shell-specific claim
is imported from it.

## 2. Spectral comparison directions

For a fixed angular channel, after \(u=rR\), the shell form is

\[
a_{\rho,\ell}[u]=\int_\rho^1
\left(|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(a_{\rho,\ell})=H_0^1(\rho,1).
\]

Since \(r^{-2}\ge1\), one-dimensional Dirichlet min--max gives, at the
same radial index \(n\),

\[
\boxed{q_{\ell,n}^2\ge n^2z_\rho^2+\ell(\ell+1)},
\qquad z_\rho=\frac\pi{1-\rho}.
\tag{2.1}
\]

For \(\ell=0\), the potential vanishes, so this is the exact identity
\(q_{0,n}=nz_\rho\).

Zero extension maps \(H_0^1(\rho,1)\) into \(H_0^1(0,1)\), preserves norm
and form, and preserves the spherical harmonic. Hardy's inequality makes the
ball centrifugal term finite on the common transformed ball form domain. The
ball domain is therefore the larger min--max domain, so the direction is

\[
\boxed{q_{\ell,n}^{\rm shell}(\rho)\ge j_{\ell+1/2,n}}.
\tag{2.2}
\]

There is no unlabelled-domain shortcut and neither \(\ell\) nor \(n\) changes.
On the ball, the form domains for different angular orders agree and, for
\(p>\ell\),

\[
b_p[v]-b_\ell[v]
=\bigl(p(p+1)-\ell(\ell+1)\bigr)
\int_0^1\frac{|v|^2}{r^2}dr
\ge\bigl(p(p+1)-\ell(\ell+1)\bigr)\|v\|_2^2.
\]

Thus the second direction is

\[
\boxed{j_{p+1/2,n}^2\ge j_{\ell+1/2,n}^2
+p(p+1)-\ell(\ell+1)}.
\tag{2.3}
\]

Finally, the permitted spectral packet gives the strict global count

\[
N_D(A_{\rho,1},K^2)
=\sum_{\ell\ge0}(2\ell+1)\#\{n:q_{\ell,n}<K\}.
\tag{2.4}
\]

Consequently equality with any frequency excludes that mode; cross-order
coincidences add their full multiplicities immediately above the common
frequency but add nothing at equality.

## 3. Zero inventory and internal zero proofs

The permitted zero statements have exactly this scope; only the four
first-zero Lorch rows are external:

\[
\begin{array}{c|c|c|c}
\nu&\ell&n&\text{bound}\\ \hline
5/2&2&1&j_{5/2,1}>51/10\\
7/2&3&1&j_{7/2,1}>13/2\\
9/2&4&1&j_{9/2,1}>15/2\\
11/2&5&1&j_{11/2,1}>17/2\\
3/2&1&2&j_{3/2,2}>77/10.
\end{array}
\]

The four Lorch specializations reduce respectively to

\[
\frac{105}{4}-\left(\frac{51}{10}\right)^2=\frac6{25}>0,
\]

\[
81^2\cdot5-178^2=1121>0,
\quad 66^2\cdot15-247^2=4331>0,
\quad 507^2\cdot77-4264^2=1611077>0.
\]

All radical denominators and both sides before squaring are positive. No
specialization is reused at a different order or radial index.

The \(J_{3/2}\) second-zero proof is internal. Positive spherical order-one
zeros solve \(\tan x=x\). There is one root in each
\((n\pi,n\pi+\pi/2)\), \(n\ge1\), and none on the complementary
half-period. For \(x_0=77/10\) and \(y=5\pi/2-x_0\),

\[
0<y<\frac\pi2,
\qquad y>\frac{163}{1060}>\frac{10}{77}.
\]

Hence \(\tan x_0=\cot y<1/y<x_0\), placing the second root strictly to the
right. The same enumeration gives the first order-one root in
\((\pi,3\pi/2)\); with \(y=3\pi/2-4>1/2\),
\(\tan4=\cot y<2<4\), so \(j_{3/2,1}>4\).

The unsourced \(j_{5/2,2}>9\) was also reconstructed. Put

\[
g(x)=(3-x^2)\sin x-3x\cos x,
\qquad \mathsf j_2(x)=g(x)/x^3.
\]

On \((0,\pi)\), \(g'(x)=x(\sin x-x\cos x)>0\), so there is no positive
zero. For \(x>3\), zeros on a negative-tangent half-period solve

\[
F(x):=\tan x+\frac{3x}{x^2-3}=0,
\]

and

\[
F'(x)=\sec^2x-\frac{3(x^2+3)}{(x^2-3)^2}>0,
\quad
(x^2-3)^2-3(x^2+3)=x^2(x^2-9)>0.
\]

The complete cells through \(3\pi\) contain \(0,0,0,0,1,0,1\) roots on

\[
(0,\pi/2),\ (\pi/2,\sqrt3),\ (\sqrt3,\pi),\
(\pi,3\pi/2),\ (3\pi/2,2\pi),\
(2\pi,5\pi/2),\ (5\pi/2,3\pi).
\]

At \(x=9\), writing \(y=3\pi-9\),

\[
y>\frac{45}{106}>\frac9{26},
\qquad
F(9)=-\tan y+\frac9{26}<0.
\]

The unique root in the last cell is therefore greater than 9. Tangent poles,
multiples of \(\pi\), \(x=\sqrt3\), and the removable origin are not zeros.
This is the complete required root enumeration, not a sampled assertion.

By (2.2)--(2.3),

\[
j_{13/2,1}^2>\left(\frac{17}{2}\right)^2+12
=\frac{337}{4}=d^2,
\]

and

\[
j_{7/2,2}^2>9^2+6=87>d^2.
\]

These strict inequalities exclude every first mode with \(\ell\ge6\) and
every second mode with \(\ell\ge3\) through \(K=d\).

## 4. Exhaustive mode inventories and moving walls

### High ratio

For \(\rho\ge\rho_c\), \(z\ge\pi+1/2>7/2\). Through \(K=k_6\), (2.1)
gives

\[
q_{\ell,n}^2-K^2\ge8z^2-42>56 \quad(n\ge3),
\]

\[
q_{\ell,2}^2-K^2\ge3z^2-36>\frac34
\quad(\ell\ge2),
\]

and every first mode with \(\ell\ge6\) has lower bound at least \(k_6\).
For \(\rho\le1/4\),

\[
\left(\frac{17}{2}\right)^2-k_6(1/4)^2
>\frac{22385}{1764}>0,
\]

so \((5,1)\) is absent. The exhaustive possible list is then first modes
\(0\le\ell\le4\), plus \((0,2)\) and \((1,2)\). For
\(\rho\ge1/4\), \(z>4\), so \(4z^2>z^2+42\); every second mode is absent
and only first modes \(0\le\ell\le5\) remain. Both arguments hold at
\(\rho=1/4\).

The cumulative first-mode multiplicities are

\[
1,4,9,16,25,36.
\]

The exact \((0,2)\) mode adds one and a possible \((1,2)\) mode adds three,
giving 26 and 29. Presence of \((1,2)\) forces \(K>p_1>2z\), so it also
forces the exact \((0,2)\) mode to be present. No cross-order coincidence can
increase these caps.

The changing upper-wall order is benign and was checked explicitly:
\(p_1=k_6\) exactly at \(z^2=40/3\), and \(2z=k_6\) exactly at \(z^2=14\).
Both crossings are unique because \(z\) increases. At a crossing the equal
mode is excluded. The combined \(p_1\) and \(77/10\) delays actually make the
cap-29 branch conservative; retaining it cannot undercount.

### Lower ratio

For \(1/\sqrt{337}<\rho<\rho_c\), \(3z>3\pi>d\), so all \(n\ge3\) modes
are absent. Together with the strict ball shifts above, the exhaustive list
through the included face \(K=d\) is

\[
(\ell,1),\ 0\le\ell\le5;
\qquad (\ell,2),\ 0\le\ell\le2.
\]

The fixed thresholds obey

\[
4<\frac{51}{10}<\frac{13}{2}<\frac{15}{2}
<\frac{77}{10}<\frac{17}{2}<9<d.
\]

Moreover, throughout the lower band,

\[
\frac{13}{2}<2z<\frac{15}{2},
\qquad p_1<\frac{77}{10}.
\]

Indeed, \(\rho>1/\sqrt{337}>1/19\) gives
\(2z>(19/9)(333/106)=703/106>13/2\), while
\(\rho<\rho_c\) gives \(2z<2\pi+1<51/7<15/2\).
Also \(z<\pi+1/2<51/14\), so
\[
p_1^2<\frac{2699}{49}<\frac{5929}{100}
=\left(\frac{77}{10}\right)^2.
\]

Thus the nominal cap-10 row is empty, the \(2z\) split in the next row is
genuine, and the fixed \(77/10\) wall is the stronger second-\(\ell=1\)
delay. The exact strict-count cap function is bounded by

\[
1+3\mathbf1_{K>4}+5\mathbf1_{K>51/10}
+7\mathbf1_{K>13/2}+9\mathbf1_{K>15/2}
+11\mathbf1_{K>17/2}
+\mathbf1_{K>2z}+3\mathbf1_{K>77/10}+5\mathbf1_{K>9},
\]

which yields exactly

\[
1,4,9,10,16,17,26,29,40,45
\]

in the candidate rows. At every fixed wall and at \(2z\), the corresponding
new indicator is zero.

For the mandatory true-lower-wall test, \(L^2-k_m^2\) has derivative

\[
-\frac1{2\rho^3}-\frac{2\pi^2}{(1-\rho)^3}<0,
\]

so each sign change is unique. Likewise,
\[
\frac d{d\rho}(L^2-p_1^2)
=-\frac1{2\rho^3}-\frac{8\pi^2}{(1-\rho)^3}<0.
\]
The \(2z\) and \(z\) crossings are solved exactly. Directed exact signs give

| moving wall | unique crossing with \(L\) |
|---|---|
| \(k_6\) | \(17/250<\rho_6<69/1000\) |
| \(p_1\) | \(9/125<\rho_{p_1}<73/1000\) |
| \(2z\) | \(\rho_{2z}=1/(1+4\pi)\), with \(73/1000<\rho_{2z}<37/500\) |
| \(k_5\) | \(77/1000<\rho_5<39/500\) |
| \(k_4\) | \(11/125<\rho_4<89/1000\) |
| \(k_3\) | \(101/1000<\rho_3<51/500\) |
| \(k_2\) | \(23/200<\rho_2<117/1000\) |
| \(k_1\) | \(129/1000<\rho_1<13/100\) |
| \(z\) | \(\rho_c=1/(1+2\pi)\) |

For \(k_m\), multiplying by \(4\rho^2(1-\rho)^2\) gives the sign polynomial

\[
Q_m(\rho;p)=(1-\rho)^2-4p^2\rho^2
-4m(m+1)\rho^2(1-\rho)^2.
\]

The left signs remain positive at \(p=355/113>\pi\), and the right signs
remain negative at \(p=333/106<\pi\). Machin's exact interval certifies both
directed bounds; in particular its upper endpoint \(p_{\rm hi}\) satisfies
\[
\frac{355}{113}-p_{\rm hi}
=\frac{242737813388119804033919865163014162469429969277}
{909934029156324999352237144753089569509029388427734375}>0.
\]
For example, the six left/right numerator pairs reproduce
the incumbent ledger, beginning with
\(1092040039511>0,-441813249<0\) for \(m=1\), and ending with
\(140918469867>0,-5078264998669<0\) for \(m=6\). The \(p_1\) bracket has
directed numerators \(21336857728>0\) and
\(-6595279527969<0\). Hence no moving wall is silently crossed by a stale
cap.

The fixed intersections \(L=c\) are exactly

\[
\begin{array}{c|ccccccc}
c&9&17/2&77/10&15/2&13/2&51/10&4\\ \hline
\rho&1/18&1/17&5/77&1/15&1/13&5/51&1/8.
\end{array}
\]

The final face \(L=d\) is exactly \(\rho=1/\sqrt{337}\). Empty and degenerate
subbands created by all these wall changes are therefore accounted for.

## 5. Strict Weyl payments and stale-cap audit

Put

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

It increases strictly with \(K>0\) and decreases strictly with \(\rho\) at
fixed \(K\). If \(T^2=az^2+b\), direct logarithmic differentiation gives the
sign condition

\[
\operatorname{sgn}\frac{d}{d\rho}W(\rho,T(\rho))
=\operatorname{sgn}\bigl(a\pi^2(1+\rho)
-b\rho^2(1-\rho)^2\bigr).
\tag{5.1}
\]

Every denominator cleared here is positive. Since
\(\rho^2(1-\rho)^2\le1/16\), \(\pi^2>9\), and \(b/a\le42\), every moving
payment used below is strictly increasing.

For the high first-mode bridges, presence forces \(K\) above both a fixed
ball wall and a moving product wall. At the proposed split, both sides have
strict certificates. With
\(A=a(333/106)^2/(1-r)^2+b\),
\(B=(7/99)(1-r^3)\), and \(\Delta=B^2A^3-C^2\), the exact audit gives:

| entry/cap | split | fixed payment minus cap | positive numerator of \(\Delta\) |
|---|---:|---:|---:|
| \(\ell=2,\ C=9\) | \(3/10\) | \(1387329/11000000\) | 1399810848073457853053 |
| \(\ell=3,\ C=16\) | \(1/2\) | \(6277/6336\) | 137027505353736631 |
| \(\ell=4,\ C=25\) | \(1/2\) | \(775/704\) | 2507119282010251109 |
| \(\ell=5,\ C=36\) | \(13/25\) | \(452843/343750\) | 92672404686738742434741 |
| \((1,2),\ C=29\) | \(1/5\) | \(849901/281250\) | 373255772037478993002833 |

The positive fixed/moving ordering reserves at those splits are respectively

\[
k_2^2-c_2^2>\frac{547}{4900},\quad
k_3^2-c_3^2>\frac{23}{4},\quad
k_4^2-c_4^2>\frac{7971}{2500},
\]

\[
p_1^2-(77/10)^2>\frac{4934581}{1123600},\qquad
k_5^2-(17/2)^2>\frac{105089}{179776}.
\]

The initial high entries and radial jump are also strict:

\[
W(\rho_c,z_{\rho_c})-1>\frac{40567}{16854}>0,
\]

the positive-squaring certificate for \(W(\rho_c,k_1)>4\) has numerator
122885180711351123434093163, and

\[
W(\rho_c,2z_{\rho_c})-26>\frac{10582}{8427}>0.
\]

At \(K=2z\) the new radial mode is absent; immediately above it the cap-26
payment applies. The proof does not use the false uniform shortcut near the
left face. Indeed \(k_5(\rho_c)<33/5\), so

\[
W(\rho_c,k_5)<\frac2{27}\left(\frac{33}{5}\right)^3<25.
\]

The delayed \(\ell=4\) fixed wall is what pays 25 there.

For the lower band, \(\rho<\rho_c<7/50\) and \(1/\pi>7/22\). The exact
fixed-threshold lower margins are:

| threshold | cap | lower margin |
|---:|---:|---:|
| \(4\) | 4 | \(793292/1546875\) |
| \(51/10\) | 9 | \(486236661/1375000000\) |
| \(13/2\) | 16 | \(333100003/99000000\) |
| \(15/2\) | 26 | \(329797/88000\) |
| \(77/10\) | 29 | \(3590476297/1125000000\) |
| \(17/2\) | 40 | \(327078887/99000000\) |
| \(9\) | 45 | \(8805519/1375000\) |

Also

\[
W(\rho,L)>W(\rho_c,L(\rho_c))
=\frac16+\frac\pi3+\frac{2\pi^2}{9}>\frac{19}{6}>1,
\]

and, because \(\rho>1/\sqrt{337}>1/19\),

\[
W(\rho,2z)>W(1/19,2z)>16\frac{127}{108}
=\frac{508}{27}>17.
\]

Thus every one of the lower caps, including both sides of the moving \(2z\)
split and the included face \(K=d>9\), is paid strictly.

## 6. Upper-floor containment

Let

\[
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\quad C_*=\frac12+\frac{8\sqrt2}{15},
\quad C_0=1+\frac{8\sqrt2}{15}.
\]

The exact identities \(1+2C_*=2C_0\) and
\(\rho_*=\omega_0/(2C_0)\) give

\[
H_0(\rho_*)=\frac1{2\rho_*}=\frac{C_0}{\omega_0}.
\]

Directed elementary bounds give

\[
\frac{13}{132}<\omega_0<\frac18,
\qquad C_0>\frac{131}{75},
\qquad d<\frac{19}{2},
\]

and hence

\[
C_0-d\omega_0>
\frac{131}{75}-\frac{19}{16}
=\frac{671}{1200}>0.
\]

The \(H_0\) branch is increasing from \(H_0(\rho_*)>d\). On the low-ratio
\(K_0\) branch, \(\eta=\omega_0\), and the positive-root formula gives
\(K_0>C_0/\omega_0>d\). Therefore

\[
\boxed{d<U(\rho)\quad(\rho_*<\rho<\rho_c)}.
\]

This covers both sides of \(\rho_{HK}\), where \(H_0=K_0\), and the
\(\rho=\omega_0\) eligibility interface.

For the high band, write
\(f(K)=\eta K-\sqrt{aK}-C_0\); \(K_0\) is its unique positive root. On
\([\rho_c,1/2]\), \(\eta<1/8\), \(k_6<10\), and \(10/8<C_0\), so
\(f(k_6)<0\). On \([1/2,5/6)\), \(\eta<1/8\), \(k_6<20\), while
\(a\ge2\pi>6\) and \(k_6\ge2\pi>6\); hence
\(\sqrt{ak_6}>6>20/8>\eta k_6\), again giving \(f(k_6)<0\). On the seam,

\[
U(\rho)=\frac{54}{(1-\rho)^2}\ge1944>27>k_6
\quad(5/6\le\rho<7/8).
\]

Thus

\[
\boxed{k_6(\rho)<U(\rho)\quad(\rho_c\le\rho<7/8)}.
\]

The \(\rho=1/2\) definition interface and the inclusive \(\rho=5/6\) seam
are controlled from both sides.

## 7. Endpoint ownership and exact subtraction

The endpoint audit is as follows.

- \(\rho=\rho_*\) and \(\rho=7/8\) retain complete inherited owners and are
  outside the residual.
- At \(\rho_0=1/\sqrt{337}\), \(L=d\); the lower candidate fiber
  \(L<K\le d\) is empty, so the whole inherited slice \(L<K<U\) remains.
- The lower band is open at \(\rho_c\); the high band is closed there.
  Also \(L(\rho_c)=z_{\rho_c}=\pi+1/2\).
- The payment splits \(1/5,3/10,1/2,13/25\) have strict certificates on
  both traces. At \(1/4\), both inventory arguments apply. At \(5/6\), the
  seam owns equality. The active \(\rho_{HK}\), \(\omega_0\), and \(1/2\)
  upper-floor interfaces were checked above.
- \(K=L\) is open in the lower candidate. \(K=z\) is included in the high
  theorem and has count zero. At \(k_2,\ldots,k_6\), the corresponding
  lower-bound mode is excluded; \(k_5\) retains its Round 18 owner and
  \(k_6\) is newly included.
- At \(K=2z\), the exact \((0,2)\) mode is excluded. At \(K=p_1\), the
  \((1,2)\) mode is excluded by (2.1). Every fixed zero threshold assigns
  equality to the old, smaller cap. \(K=d\) is included. \(K=U\) remains an
  inherited covered face and is excluded from the residual.

The two proposed additions are disjoint and, by the strict upper-floor
comparisons, both lie inside

\[
\mathcal D_{18}=
\{\rho_*<\rho<\rho_c,\ L<K<U\}
\cup
\{\rho_c\le\rho<7/8,\ k_5<K<U\}.
\]

Subtracting \((L,d]\) only when \(\rho_0<\rho<\rho_c\), and subtracting
\((k_5,k_6]\) on the high piece, gives exactly

\[
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\left\{\rho_*<\rho\le\frac1{\sqrt{337}},\ L(\rho)<K<U(\rho)\right\}\\
&\cup\left\{\frac1{\sqrt{337}}<\rho<\rho_c,\ d<K<U(\rho)\right\}\\
&\cup\left\{\rho_c\le\rho<\frac78,\ k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}}
\]

The inherited input already has \(B_0,B_1\subset\mathcal A_{18}\), hence
\((B_0\cup B_1)\cap\mathcal D_{18}=\varnothing\). Neither box is subtracted
again.

## 8. Independent execution and counterexample search

Commands run from the repository root and their results:

    python computations/round19_verify_two_sided_staircase.py --self-check --manifest
    python -m pytest computations/tests/test_round19_verify_two_sided_staircase.py -q
    python computations/round19_residual_mask.py --self-check --manifest
    python -m pytest computations/tests/test_round19_residual_mask.py -q
    python -m pytest -q
    python -m compileall -q computations
    git diff --check

Results:

- Round 19 two-sided verifier: **PASS**, 245 exact checks, first failure
  null; all eight control/permitted files authenticated.
- Focused two-sided tests: **24 passed**.
- Frozen residual self-check: **PASS**, 13 checks.
- Focused residual tests: **37 passed**.
- Full suite: **193 passed, 10 subtests passed**.
- Compilation and diff hygiene: **PASS**.

I also ran an independent falsification sweep from a PowerShell here-string
piped to Python. It used scipy.special.jv/yv for the shell cross-product,
scipy.optimize.brentq for sign-changing simple roots, exact \(\ell=0\)
frequencies, angular orders through 8, 81 lower-ratio and 127 high-ratio
samples including every named split, and every detected entry and candidate
face. Result: 208 ratio samples, 1,466 entry/face cases, no counterexample;
the smallest sampled right-limit margin was approximately
\(2.40710964033\), at the high left face just above \(K=z_{\rho_c}\).
This numerical sweep is falsification evidence only; no proof step depends on
it.

## 9. Final verdict

The source boundaries, form domains, min--max directions, positive-zero
indices, tangent-cell enumeration, spectral inventories, complete
multiplicities, moving/fixed wall order, strict Weyl payments, upper-floor
containment, endpoint ownership, absorbed-box bookkeeping, and residual set
subtraction all check out.

**PASS. First unsupported implication: none.**
