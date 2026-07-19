# Round 20 exploration: independent high-closure crosscheck

Status: **PASS through \(k_8\); first unsupported implication: none**.

Date: 2026-07-14.

This is an adversarial pre-freeze reconstruction, not a promotion.  I
assumed the proposed union through \(k_8\) false, did not use the incumbents
as authority for any implication, and made no change to an existing
artifact.

## 1. Byte and provenance check

The bytes actually reviewed have the following SHA-256 values.

| artifact | independently recomputed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `rounds/polya-main/round_019/exploration/residual-mask-freeze.md` | `0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9` |
| `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| `rounds/polya-main/round_020/exploration/high-next-wall.md` | `d7bb58554cf7505bc18415415b1ab21fa233b1707d9685b0a48bb58bbb2ab8a2` |
| `rounds/polya-main/round_020/exploration/high-lorch-extension.md` | `30aea82a3278683bdaf0c8d98b24b82276568d5d42435841833d79f4670f811c` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |

In particular, the current proof-note hash is
`30aea82a3278683bdaf0c8d98b24b82276568d5d42435841833d79f4670f811c`.
This is the hash after the presentation-only `\qquad` repair, not a stale
authorship hash.  Every dependency hash printed inside that note agrees
with the current dependency bytes.

The frozen and subsequently accepted Round 19 bookkeeping gives the high
component

\[
 \mathcal D_{19}^{\rm H}
 =\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K<U(\rho)\},
 \qquad \rho_c=\frac1{1+2\pi}.
 \tag{1}
\]

Thus the Round 20 set calculation must start with an open lower frequency
face, an open upper frequency face, an included \(\rho_c\) slice, and an
excluded \(7/8\) slice.  It does.

## 2. Exact source scope and Lorch specializations

The SIAM publisher abstract independently confirms that \(j_{\nu,1}\) is
the first positive zero of \(J_\nu\), that \(-1<\nu<\infty\), and that

\[
 j_{\nu,1}^{\,2}>
 \frac{24(\nu+1)^2}
 {1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}-2(\nu^2-1).
 \tag{2}
\]

The body of the paper is access-controlled, so this is exactly a
statement-level source use.  DLMF 10.47.3 supplies only the positive-factor
identity between \(\mathsf j_\ell\) and \(J_{\ell+1/2}\).  Neither source
supplies a shell zero, a second radial zero, min--max, multiplicity, a Weyl
payment, or set subtraction.

For \(\nu=\ell+1/2\), rationalizing the positive denominator in (2) gives

\[
 R_\ell=
 \frac{3(2\ell+3)\sqrt{(\ell+2)(\ell+6)}
       -2\ell^2+\ell+6}{4},
 \qquad j_{\ell+1/2,1}^2>R_\ell.
 \tag{3}
\]

The three declared specializations and their sign-safe checks are:

| \(\ell\) | exact \(R_\ell\) | authorized rational wall | squared certificate |
|---:|---|---|---:|
| 6 | \(45\sqrt6-15\) | \(j_{13/2,1}>39/4\) | \(240^2\cdot6-587^2=1031\) |
| 7 | \((153\sqrt{13}-85)/4\) | \(j_{15/2,1}>54/5\) | \(3825^2\cdot13-13789^2=61604\) |
| 8 | \(57(\sqrt{35}-1)/2\) | \(j_{17/2,1}>71/6\) | \(1026^2\cdot35-6067^2=35171\) |

All quantities squared in this table are positive.  The first two rows are
used in the proof through \(k_8\); the third is used only in the \(k_9\)
method audit.  There is no implicit authorization of another order or of a
higher radial index.

The predecessor's use of

\[
 B=\frac{507(\sqrt{77}-1)}{52},
 \qquad j_{11/2,1}^2>B,
\]

is the explicit same-order \(\nu=11/2\) specialization printed and reduced
inside the audited Round 19 source card, not a new order inferred from the
older three-order Lorch card.  Its angular shift gives

\[
 j_{13/2,1}^2>B+12>\left(\frac{234}{25}\right)^2,
\]

where

\[
 77-\left(\frac{71133}{8125}\right)^2
 =\frac{23299436}{66015625}>0.
\]

Thus the weaker predecessor wall \(234/25\), as well as the new direct wall
\(39/4\), has valid provenance.

## 3. Form comparisons and strict direction

Put \(d_\ell=\ell(\ell+1)\) and
\(z=\pi/(1-\rho)\).  The transformed shell form is

\[
 a_\ell[u]=\int_\rho^1
 \left(|u'|^2+\frac{d_\ell}{r^2}|u|^2\right)dr,
 \qquad D(a_\ell)=H_0^1(\rho,1).
\]

The three directions used in both proof notes reconstruct as follows.

1. Since \(r^{-2}\geq1\), form ordering against the length-
   \((1-\rho)\) Dirichlet interval gives, at the same radial min--max index,

   \[
   q_{\ell,n}^2\geq n^2z^2+d_\ell,
   \qquad q_{0,n}=nz.
   \tag{4}
   \]

2. Zero extension from \((\rho,1)\) to \((0,1)\) preserves the norm and
   form and preserves the fixed angular channel.  Hardy's inequality makes
   every transformed ball form domain \(H_0^1(0,1)\).  The shell domain is
   therefore a form subspace of the ball domain, so min--max has the
   direction

   \[
   q_{\ell,n}^2\geq j_{\ell+1/2,n}^2.
   \tag{5}
   \]

3. On the common ball domain, for \(p\geq\ell\),

   \[
   a_p-a_\ell=(d_p-d_\ell)\int_0^1\frac{|u|^2}{r^2}dr
   \geq(d_p-d_\ell)\|u\|_2^2.
   \]

   Hence

   \[
   j_{p+1/2,n}^2\geq
   j_{\ell+1/2,n}^2+d_p-d_\ell.
   \tag{6}
   \]

All three comparisons preserve \(n\).  Combining a non-strict form
comparison with a strict sourced zero bound remains strict.  The spectral
count is \(q_{\ell,n}<K\), so equality at any lower wall omits, rather than
adds, the relevant full multiplicity \(2\ell+1\).

## 4. Reconstruction through \(k_7\)

The predecessor's internal spherical-Bessel argument is complete.  For
\(x>\sqrt3\), zeros of

\[
 \mathsf j_2(x)=\frac{(3-x^2)\sin x-3x\cos x}{x^3}
\]

satisfy \(\tan x=-3x/(x^2-3)\).  There is no root on a positive-tangent
half-period.  On every negative-tangent half-period after \(3\),
\(F=\tan+3x/(x^2-3)\) is strictly increasing because

\[
 \frac{3(x^2+3)}{(x^2-3)^2}<1\leq\sec^2x.
\]

The sourced first-zero bound excludes the sole earlier cell.  Thus the
second root is the unique one in \((5\pi/2,3\pi)\).  At \(x=9\), with
\(y=3\pi-9>45/106>9/26\),

\[
 \tan9=-\tan y<-\frac9{26}=-\frac{27}{78},
\]

so \(j_{5/2,2}>9\).  Equation (6) then gives
\(j_{7/2,2}^2>87\).

For \(K^2\leq k_7^2=z^2+56\) and
\(z>7/2\):

- every \(n\geq3\) mode is absent because \(8z^2-56>42\);
- every second mode with \(\ell\geq4\) is absent because
  \(3z^2+d_\ell-56>3/4\);
- \((2,2)\) is excluded by splitting at \(z^2=50/3\), using (4) on
  the upper side and \(j_{5/2,2}^2>81\) on the lower side;
- \((3,2)\) is excluded similarly at \(z^2=44/3\), using the strict
  ball bound \(>87\);
- every first mode with \(\ell\geq7\) is absent by (4), including at
  \(K=k_7\).

Thus the full possible inventory is

\[
 (\ell,1),\ 0\leq\ell\leq6;
 \qquad (0,2),(1,2).
 \tag{7}
\]

Any counted second mode forces \(3z^2<56\), hence \(\rho<3/10\), because

\[
 z_{3/10}^2>
 \left(\frac{10}{7}\frac{333}{106}\right)^2>\frac{56}{3}.
\]

The complete predecessor caps and payments also reproduce exactly:

| situation | cap | exact lower payment or bridge |
|---|---:|---|
| base first modes, with at most \((0,2)\) | 25 or 26 | \(W(1/8,k_6(1/8))>26\); its squared reserve is \(1906662783250496828695/12918374118245105664\) |
| \((1,2)\) present | 29 | \(W(1/5,77/10)>9006151/281250>29\), and \(p_1(1/5)^2-(77/10)^2>4934581/1123600\) |
| highest first mode \(\ell=5\), no second mode | 36 | \(W(3/7,17/2)>388127/9702>36\); the moving-\(k_6\) squared reserve is \(279281008839913330541/922741008446078976\) |
| highest first mode \(\ell=6\), no second mode | 49 | \(W(107/200,234/25)>8439557159943/171875000000>49\); the moving-\(k_6\) squared reserve is \(254061581274155406101913080384629/19814236859680322312000000000000\) |
| \(\ell=5\) plus possible second modes | 40 | \(W(3/10,17/2)>33462443/792000>40\) |
| \(\ell=6\) plus possible second modes | 53 | \(W(3/10,234/25)>1212065127/21484375>53\) |

The moving payments at \(k_6\) and \(p_1\) increase by the derivative
test

\[
 a\pi^2(1+\rho)>b\rho^2(1-\rho)^2
\]

for a wall \(T^2=az^2+b\); fixed-wall payments decrease with \(\rho\).
No cap is carried across a radial or angular entry without its complete
multiplicity.  This independently validates the closed predecessor through
\(k_7\).

## 5. Exhaustive \(k_8\) inventory and incompatibilities

Now suppose \(K^2\leq k_8^2=x+72\), where \(x=z^2>49/4\).

- For \(n\geq3\), (4) gives
  \(q_{\ell,n}^2-K^2\geq8x+d_\ell-72>26\).
- For first modes \(\ell\geq8\), (4) gives
  \(q_{\ell,1}^2\geq x+d_\ell\geq x+72\).
- For a second mode \(\ell\geq4\), (4)--(6) give both

  \[
  q_{\ell,2}^2\geq4x+d_\ell,
  \qquad q_{\ell,2}^2>75+d_\ell.
  \]

  If \(x\leq d_\ell+3\), the second bound is strictly at least the
  upper face.  If \(x>d_\ell+3\), the first bound exceeds it by more than
  \(4d_\ell-63\geq17\).  The crossing face is excluded by both bounds.

Therefore the complete possible inventory is exactly bounded by

\[
 (\ell,1),\ 0\leq\ell\leq7;
 \qquad (\ell,2),\ 0\leq\ell\leq3.
 \tag{8}
\]

If \((h,2)\) is counted, then

\[
 3x<72-d_h.
 \tag{9}
\]

The exact ratio consequences are

\[
 \begin{array}{c|c|c}
 \text{radial category}&\text{ratio restriction}&\text{exact reserve at the excluded face}\\ \hline
 \text{some second mode}&\rho<3/8&88824/70225\\
 (2,2)&\rho<1/3&9233/44944\\
 (3,2)&\rho<3/10&19405/137641
 \end{array}
 \tag{10}
\]

If \((6,1)\) is counted, the direct wall gives
\(x>369/16>23\).  This is incompatible with \(x<22\) for \((2,2)\)
and with \(x<20\) for \((3,2)\).  Hence the \(H=6,h=2,3\) cells are
genuinely impossible.  In fact \(H=7\) is incompatible with every second
mode because it would force \(x>(54/5)^2-72>44\), while (9) gives
\(x<24\); retaining and paying those empty cells is harmless overcounting.

The resulting complete cap table is

| first category | no second | \(h=0\) | \(h=1\) | \(h=2\) | \(h=3\) |
|---|---:|---:|---:|---:|---:|
| \(H=7\) | 64 | 65 | 68 | 73 | 80 |
| \(H=6\) | 49 | 50 | 53 | impossible | impossible |
| \(H=5\) | 36 | 37 | 40 | 45 | 52 |
| \(H\leq4\) | 25 | 26 | 29 | 34 | 41 |

Each entry is \((H+1)^2+(h+1)^2\), so it includes every complete angular
multiplicity even if a lower channel happens not to be counted.

## 6. Independent payment of every \(k_8\) cap

Let \(F_7(\rho)=W(\rho,k_7(\rho))\).  Its derivative is positive because

\[
 \pi^2(1+\rho)-56\rho^2(1-\rho)^2
 >9-\frac{56}{16}=\frac{11}{2}.
\]

Also \(2/(9\pi)>7/99\).  The following table covers every cell above; all
displayed fractions were independently recomputed from exact rational
arithmetic.

| category paid | largest cap | exact strict lower payment |
|---|---:|---|
| uniform new-band base | 26 | \(F_7(1/8)>3577/99>26\) |
| \(H=7\), some second mode | 80 | \(W(3/8,54/5)>1484973/17600>80\) |
| \(H=7\), no second mode | 64 | \(W(3/5,54/5)>12002256/171875>64\), with \(k_7(3/5)^2-(54/5)^2>1170521/1123600\) |
| \(H=6\), some second mode (necessarily \(h\leq1\)) | 53 | \(W(3/8,39/4)>22376445/360448>53\) |
| \(H=6\), no second mode | 49 | \(W(1/2,39/4)>322959/5632>49\), with \(k_7(1/2)^2-(39/4)^2>18599/44944\) |
| \(H=5,h=3\) | 52 | \(W(3/10,93/10)>608719503/11000000>52\) |
| \(H=5,h=2\) | 45 | \(W(1/3,9)>546/11>45\) |
| \(H=5,h\leq1\) | 40 | \(W(3/8,17/2)>16679635/405504>40\) |
| \(H=5\), no second mode | 36 | \(W(1/2,17/2)>240737/6336>36\), and \(k_7(1/2)>17/2\) |
| \(H\leq4,h=3\) | 41 | the stronger cap-52 payment above |
| \(H\leq4,h=2\) | 34 | the stronger cap-45 payment above |
| \(H\leq4,h=1\) | 29 | \(W(3/8,77/10)>28180537/921600>29\) |
| \(H\leq4,h=0\) | 26 | \(W(\rho,2z)\geq W(\rho_c,2z)>153196/5625>26\) |
| \(H\leq4\), no second mode | 25 | the uniform base payment |

For the fixed/moving splits, fixed payments control the lower-\(\rho\)
side and increasing \(F_7\) controls the upper side.  The two wall-order
reserves in the table make both split faces strict.  For \(h=0\),

\[
 W(\rho,2z)=\frac{16\pi^2}{9}
 \frac{1+\rho+\rho^2}{(1-\rho)^2}
\]

is increasing, and its value at \(\rho_c\) is
\((16\pi^2+24\pi+12)/9\).  The lower bound displayed in the table uses
\(\pi>157/50\).  This completes, rather than samples, the cap table.

## 7. Containment, equality ownership, and subtraction

For \(\rho\leq7/8\), \(z\leq8\pi<176/7\), and

\[
 27^2-k_8^2>
 27^2-\left(\frac{176}{7}\right)^2-72
 =\frac{1217}{49}>0.
 \tag{11}
\]

On \(\rho_c\leq\rho<5/6\), the active upper floor is \(K_0\).  With
\(a_\rho=2\rho z\geq a_{\rho_c}=1\) and \(0<\eta_\rho<1/8\), its exact
formula gives

\[
 K_0>\frac{a_\rho}{\eta_\rho^2}>64a_\rho\geq64.
\]

On \(5/6\leq\rho<7/8\), the seam floor is at least \(1944\).  Therefore

\[
 \boxed{k_8(\rho)<U(\rho)\quad(\rho_c\leq\rho<7/8).}
 \tag{12}
\]

The face audit is consistent:

- \(K=k_6\) is owned by Round 19, \(K=k_7\) by the predecessor, and
  \(K=k_8\) by the new band; the next first mode is excluded on each moving
  equality face by strict counting.
- Equality at a Lorch wall, a second-mode moving wall, or one of
  \(77/10,9,93/10\) leaves the corresponding mode uncounted.  Immediately
  above it the table includes its full multiplicity.
- The ratio faces \(3/10,1/3,3/8\) contain no mode from the branch that
  they terminate, by the strict inequalities in (9)--(10).
- Both estimates hold at \(1/2\) and \(3/5\).  The \(5/6\) seam only
  changes the upper-floor owner.
- \(\rho_c\) is included.  The closed theorem includes \(\rho=7/8\),
  while the residual subtraction excludes that already-owned endpoint.
- \(K=U\) is inherited covered territory and is not subtracted.

The two genuinely new high pieces are disjoint at their shared owner and
have union

\[
 \{\rho_c\leq\rho<7/8,\ k_6<K\leq k_7\}
 \cup
 \{\rho_c\leq\rho<7/8,\ k_7<K\leq k_8\}
 =\{\rho_c\leq\rho<7/8,\ k_6<K\leq k_8\}.
\]

Using (12), exact subtraction from (1) is therefore

\[
 \boxed{
 \mathcal D_{20}^{\rm H}
 =\{\rho_c\leq\rho<7/8,\ k_8(\rho)<K<U(\rho)\}.}
 \tag{13}
\]

Every lower-ratio component is unchanged.

## 8. Separate audit of the \(k_9\) method obstruction

The direct \(\ell=8\) first-zero wall is not itself an obstruction.  In the
prospective \(k_9\) band, any second mode would force \(3x<90\), whereas a
counted \((8,1)\) mode would force
\(x>(71/6)^2-90=1801/36>50\).  Thus this row necessarily has no second
mode.  Its cap is \(81\), and

\[
 W(2/3,71/6)>
 \frac{47602163}{577368}>81,
\]

while

\[
 k_8(2/3)^2-(71/6)^2>\frac{525692}{25281}>0.
\]

The increasing moving \(k_8\) payment and the fixed \(71/6\) payment
therefore bridge at \(2/3\).

The lower-angular/radial witness is valid.  At \(\rho_0=27/100\), put
\(x_0=z_{\rho_0}^2\) and use the full Lorch square

\[
 C_6^2=45\sqrt6-15.
\]

The exact directed bounds give

\[
 16<x_0<\left(\frac{2200}{511}\right)^2<\frac{75}{4},
 \qquad
 95<C_6^2<\frac{381}{4},
 \qquad C_6<\frac{49}{5}.
 \tag{14}
\]

The proof note displays \(k_7<C_6<k_9\).  The stronger relation actually
needed for the prospective new band also follows immediately and exactly:

\[
 k_8(\rho_0)^2=x_0+72
 <\frac{363}{4}<95<C_6^2,
 \qquad
 C_6^2<\frac{381}{4}<x_0+90=k_9(\rho_0)^2.
 \tag{15}
\]

Thus the displayed \(k_7\) is a harmless weaker presentation line, not a
gap in the witness.

At this witness, the largest moving second-mode lower square through
\(\ell=4\) is less than \(95\), and the largest available ball-shift lower
square is \(75+d_4=95<C_6^2\).  Immediately above \(C_6\), the current
individual lower bounds must therefore allow

\[
 \sum_{\ell=0}^{6}(2\ell+1)
 +\sum_{\ell=0}^{4}(2\ell+1)=49+25=74.
 \tag{16}
\]

Second modes \(\ell\geq5\) are still excluded there because their
ball-shift lower square is at least \(105>C_6^2\); the \(\ell=7,8\) first
modes are excluded by the direct rational walls.  Hence (16) is the
complete current-method cap, not a stale partial inventory.

Along this witness's wall ordering, the preceding caps are paid: just above
\(k_8\) the cap is at most \(52\), and at the second-\(\ell=4\) wall the
cap is \(61\).  With

\[
 B_0=\frac7{99}\left(1-\left(\frac{27}{100}\right)^3\right)
 =\frac{6862219}{99000000},
\]

the two sign-safe checks

\[
 B_0^2\,88^3-52^2
 =\frac{90209295643571}{158203125000}>0,
 \qquad
 B_0^2\,95^3-61^2
 =\frac{31234482233568499}{78408000000000}>0
\]

pay both preceding caps.  The next certified wall is the first
\(\ell=6\) wall, where the allowed cap jumps to \(74\).

At that full wall, however,

\[
 W(\rho_0,C_6)
 <\frac{6112665680849}{93656250000}
 <66<74.
 \tag{17}
\]

By continuity the same payment failure persists immediately above the
strict wall.  This proves the claimed obstruction for the present
individual-wall/cap method.  It is not a shell counterexample: the actual
second shell modes may enter later than their available lower walls, and a
sharper second-radial estimate or a coupled counting/payment argument could
still prove the \(k_9\) band.

## 9. Verdict

**PASS.**  The Round 19 closed face, the predecessor through \(k_7\), and
the direct-Lorch step through \(k_8\) form a valid closed theorem through
\(k_8\).  Source scope, all form/min--max directions, every first/second/
higher-radial exclusion, simultaneous-mode restriction, cap-table payment,
strict equality owner, upper-floor comparison, and the subtraction (13)
survive independent reconstruction.

**First unsupported implication: none.**  The separate cap-74 statement is
a valid obstruction to the declared \(k_9\) method and is not promoted as a
mathematical counterexample or a theorem about the true shell entries.
