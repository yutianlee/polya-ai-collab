# Round 20 combined-closure zero/source-provenance audit

## Verdict

**PASS for the assigned zero/source-provenance slice.**  Equations (24)--(26), every rational zero inequality in (27), and the lower zero obligations (19) all admit an independent reconstruction within the frozen source boundary.  The stated lower angular-propagation scopes preserve the radial index and are valid through the included endpoint `sqrt(114)`.

**First unsupported implication:** none in this slice.  This is not a verdict on the cap tables, Weyl payments, optical argument, or the full combined-closure claim.

## Isolation and authentication

I authenticated the released candidate before reading it and then authenticated the release freeze.  I did not read a Round 20 exploration proof, zero-bound card, computation/ledger, review, incumbent response, Git history/diff, judge draft, or another agent's work.  The only local substantive inputs read after the candidate and freeze were the following expressly permitted files.

| file | observed SHA-256 | result |
|---|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` | match |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` | match |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | match |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | match |
| `sources/shell_weyl_bessel.md` | `ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade` | match |
| `sources/bessel_phase_enclosures.md` | `e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c` | match |

The online identity sources were exactly [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3), [DLMF 10.49(i)](https://dlmf.nist.gov/10.49.i), [DLMF 10.51.1](https://dlmf.nist.gov/10.51.E1), and [DLMF 10.51.2](https://dlmf.nist.gov/10.51.E2).  For Lorch I checked the primary [SIAM publisher page](https://epubs.siam.org/doi/10.1137/0524050) and its direct [DOI record](https://doi.org/10.1137/0524050).

## 1. Form comparisons, directions, and index preservation

Write `q_(ell,n)^2` for the `n`th eigenvalue of

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
$$

on `(rho,1)` with form domain `H_0^1(rho,1)`.  On that same form domain,

$$
\mathfrak a_\ell[u]
\geq \int_\rho^1|u'|^2\,dr+\ell(\ell+1)\|u\|_2^2,
$$

because `r<=1`.  Min--max against the Dirichlet interval eigenvalues therefore gives

$$
q_{\ell,n}^2\geq \frac{n^2\pi^2}{(1-\rho)^2}+\ell(\ell+1)
=n^2z_\rho^2+\ell(\ell+1).
$$

For `ell=0` the potential vanishes, so `q_(0,n)=nz_rho`.  This proves (24), with the same min--max index `n` on both sides.

For the unit ball, after `u=rR`, the fixed-`ell` form is

$$
\mathfrak b_\ell[u]=\int_0^1\left(|u'|^2+\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak b_\ell)=H_0^1(0,1).
$$

Hardy's inequality controls the singular term.  Extension by zero sends `H_0^1(rho,1)` isometrically into `H_0^1(0,1)` and preserves both the `L^2` norm and the displayed fixed-channel form.  The zero extension remains in the same `(ell,m)` spherical-harmonic subspace; the zero trace at `r=rho` is essential here.  Min--max on this embedded fixed-channel subspace gives, in the correct direction and at the same radial index,

$$
q_{\ell,n}^2\geq j_{\ell+1/2,n}^2.
$$

This proves (25).  Unlabelled global domain monotonicity is not being used as a substitute for the fixed-channel argument.

Finally, for `p>=ell`, the two ball forms have the same domain and

$$
\mathfrak b_p[u]-\mathfrak b_\ell[u]
=\bigl(p(p+1)-\ell(\ell+1)\bigr)\int_0^1\frac{|u|^2}{r^2}\,dr
\geq \bigl(p(p+1)-\ell(\ell+1)\bigr)\|u\|_2^2.
$$

Min--max yields (26), again without changing `n`:

$$
j_{p+1/2,n}^2\geq j_{\ell+1/2,n}^2+p(p+1)-\ell(\ell+1).
$$

For `p>ell` the additive constant is positive, so the corresponding zero is strictly larger.  Thus (24)--(26) have the claimed domains, directions, angular-channel preservation, and radial-index preservation.

## 2. Half-integer identities, simplicity, and exact root enumeration

[DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3) gives

$$
\mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),\qquad x>0.
$$

The prefactor is positive, so positive zeros, their order, and signs agree.  The point `x=0` is not counted.  The explicit formulas in [DLMF 10.49(i)](https://dlmf.nist.gov/10.49.i), together with the recurrence in [DLMF 10.51.1--10.51.2](https://dlmf.nist.gov/10.51.E1), give

$$
x^{\ell+1}\mathsf j_\ell(x)=P_\ell(x)\sin x+Q_\ell(x)\cos x=:F_\ell(x),
$$

where

$$
\begin{array}{c|l|l}
\ell&P_\ell&Q_\ell\\ \hline
0&1&0\\
1&1&-x\\
2&3-x^2&-3x\\
3&15-6x^2&x^3-15x\\
4&x^4-45x^2+105&10x^3-105x\\
5&15x^4-420x^2+945&-x^5+105x^3-945x\\
6&-x^6+210x^4-4725x^2+10395&-21x^5+1260x^3-10395x\\
7&-28x^6+3150x^4-62370x^2+135135&x^7-378x^5+17325x^3-135135x.
\end{array}
$$

These follow from `P_(ell+1)=(2ell+1)P_ell-x^2P_(ell-1)` and the same recurrence for `Q`.  Taylor expansion at zero gives `j_ell(x)=x^ell/(2ell+1)!!+O(x^(ell+2))`, hence positivity just to the right of zero.

Every positive zero is simple: the spherical Bessel ODE has regular coefficients at a positive point, so a solution with both value and derivative zero there would vanish identically by ODE uniqueness, contradicting the preceding positive leading term.  At a zero `alpha` of `j_ell`, DLMF 10.51.2 gives `j_(ell+1)(alpha)=-j_ell'(alpha)`.  Consecutive simple zeros of `j_ell` therefore give opposite signs of `j_(ell+1)`.  Combining this with the strict form ordering

$$
j_{\ell+3/2,n}>j_{\ell+1/2,n}
$$

proves the strict interlacing

$$
j_{\ell+1/2,n}<j_{\ell+3/2,n}<j_{\ell+1/2,n+1}.
$$

Consequently, if `N_ell(x)` counts positive zeros of `j_ell` below a nonzero endpoint `x`, then

$$
N_\ell(x)\in
\{\max(0,N_{\ell-1}(x)-1),N_{\ell-1}(x)\},
\qquad \operatorname{sgn}\mathsf j_\ell(x)=(-1)^{N_\ell(x)}.
$$

This supplies an exact root enumeration; a tangent sign by itself is never used to guess the radial index.

### Rational trigonometric certificates

The elementary enclosure used throughout is

$$
\frac{157}{50}<\pi<\frac{22}{7}.
$$

For the lower bound, Machin's identity and alternating arctangent bounds give

$$
\pi>16\left(\frac15-\frac1{3\cdot5^3}\right)-\frac4{239}
=\frac{281476}{89625}
=\frac{157}{50}+\frac{107}{179250}.
$$

For the upper bound,

$$
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
$$

For `0<s<pi/2`, elementary differentiation and the sine/cosine Taylor bounds give

$$
\tan s>s,\qquad
\tan s>s+\frac{s^3}{3},\qquad
\tan s<\frac{s}{1-s^2/2}\quad(0<s<1).
$$

Substitution in the displayed `P_ell,Q_ell` gives all endpoint signs.  The nonautomatic exact comparisons are:

$$
\begin{array}{c|c}
x&\text{strict certificate}\\ \hline
77/10&5\pi/2-x>3/20>10/77\\
21/2&7\pi/2-x>49/100>2/21\\
9&3\pi-x>21/50>9/26\\
61/5&4\pi-x>9/25>915/3646\\
103/10&7\pi/2-x>69/100>621540/938227\\
129/10&0<x-4\pi<17/50,\quad \tan(x-4\pi)<1700/4711\\
10&4/7<x-3\pi<29/50,\quad \tan(x-3\pi)<2900/4159\\
23/2&53/50<4\pi-x<\pi/2,\quad \tan(4\pi-x)>546377/375000.
\end{array}
$$

Here

$$
\frac{1700}{4711}<\min\left\{\frac{129}{10},\frac{651063}{327820},
\frac{177800829}{427700150}\right\},
$$

$$
\frac{2900}{4159}<\min\left\{10,\frac{170}{117},
\frac{188790}{127579}\right\},
\qquad \frac47>\frac{890}{21789},
$$

and

$$
\frac{546377}{375000}>
\max\left\{\frac{138}{517},\frac{224020}{186301},
\frac{3153151489}{2276518664}\right\}.
$$

All are direct positive-integer cross multiplications.  For example, at `x=103/10`, writing `delta=7pi/2-x`, one has `tan(x-3pi)=cot(delta)<1/delta`, and `69/100>621540/938227` gives the strict negative sign of `F_3`.  At `x=129/10` the three ratios in the first minimum certify respectively the signs of `F_1,F_3,F_5`; the signs of `F_2,F_4` are immediate from their coefficient signs.  The analogous substitutions at `x=10` and `x=23/2` certify every intermediate sign, not only the terminal channel.

The exact tangent half-cells, signs, and zero counts are therefore:

| rational endpoint `x` | half-period cell | signs `sgn(j_0),...,sgn(j_ell)` | exact counts `N_0,...,N_ell` |
|---|---|---|---|
| `77/10` | `(2pi,5pi/2)` | `+,-` | `2,1` |
| `9` | `(5pi/2,3pi)` | `+,+,-` | `2,2,1` |
| `10` | `(3pi,7pi/2)` | `-,+,+,-,-,-,+` | `3,2,2,1,1,1,0` |
| `103/10` | `(3pi,7pi/2)` | `-,+,+,-` | `3,2,2,1` |
| `21/2` | `(3pi,7pi/2)` | `-,+` | `3,2` |
| `23/2` | `(7pi/2,4pi)` | `-,-,+,+,-,-,-,+` | `3,3,2,2,1,1,1,0` |
| `61/5` | `(7pi/2,4pi)` | `-,-,+` | `3,3,2` |
| `129/10` | `(4pi,9pi/2)` | `+,-,-,+,+,-` | `4,3,3,2,2,1` |

The undivided expression `F_ell=P_ell sin+Q_ell cos` is retained at half-period endpoints, so no root is created or lost by division by `cos x` at a tangent pole.  The strict rational certificates also show that none of the proposed rational walls is itself a zero.  Together with ODE simplicity, the table proves

$$
\begin{gathered}
j_{3/2,2}>\frac{77}{10},\quad j_{5/2,2}>9,\quad
j_{7/2,2}>\frac{103}{10},\quad j_{11/2,2}>\frac{129}{10},\\
j_{3/2,3}>\frac{21}{2},\quad j_{5/2,3}>\frac{61}{5},\\
j_{13/2,1}>10,\quad j_{15/2,1}>\frac{23}{2}.
\end{gathered}
$$

## 3. Exact Lorch scope and the remaining first zeros

The SIAM abstract identifies `j=j_(nu,1)` specifically as the **first positive** zero of `J_nu`, states the range `-1<nu<infinity`, and prints the strict inequalities

$$
j_{\nu,1}^2>(\nu+1)(\nu+5)
$$

and

$$
j_{\nu,1}^2>
\frac{24(\nu+1)^2}{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
$$

That verifies exactly the already-qualified statement-level provenance.  The full paper remains access-controlled; nothing here upgrades it to a proof-level source audit.  In particular, Lorch supplies no `n>=2` zero, shell cross-product zero, shell-to-ball comparison, angular propagation, count, or endpoint ownership.

For `nu=ell+1/2`, the second Lorch right-hand side simplifies to

$$
B_\ell=
\frac{3(2\ell+3)\sqrt{(\ell+2)(\ell+6)}-2\ell^2+\ell+6}{4}.
$$

Its denominator before rationalization is positive because `(ell+2)(ell+6)-ell^2=8ell+12>0`.  Exact specialization gives:

| `ell` | `B_ell` | target square | exact strict comparison |
|---:|---:|---:|---|
| 8 | `(57/2)(sqrt(35)-1)` | `(71/6)^2` | `1026^2*35-6067^2=35171>0` |
| 9 | `(63sqrt(165)-147)/4` | `(64/5)^2` | `1575^2*165-20059^2=6939644>0` |
| 10 | `138sqrt(3)-46` | `(69/5)^2` | `3450^2*3-5911^2=767579>0` |

Both sides being squared in the last column are positive.  Lorch's strict inequality and positivity of the first zero therefore prove

$$
j_{17/2,1}>\frac{71}{6},\qquad
j_{19/2,1}>\frac{64}{5},\qquad
j_{21/2,1}>\frac{69}{5}.
$$

As an independent recurrence check, (26) applied to `j_(15/2,1)>23/2` yields

$$
j_{17/2,1}^2>\frac{529}{4}+16=\frac{593}{4}>\frac{5041}{36},
$$

$$
j_{19/2,1}^2>\frac{529}{4}+34=\frac{665}{4}>\frac{4096}{25}.
$$

Thus the first two of these also follow internally by same-index angular propagation.  By contrast, Lorch's printed bounds at `ell=6,7` are too weak by themselves for `10` and `23/2`; those two strengthenings are supplied by the exact half-integer count above, as required.

## 4. Lower obligations (19) and their full propagation scopes

The registry above gives `j_(13/2,1)>10` and `j_(3/2,3)>21/2` directly.  It also gives

$$
j_{7/2,2}>\frac{103}{10}>\frac{81}{8},
$$

so all three obligations in (19) are strict.  Their advertised lower-inventory consequences follow from (26), always at the same radial index:

1. From `ell=6,n=1`, for every `p>=7`,

   $$
   j_{p+1/2,1}^2>100+p(p+1)-42\geq114.
   $$

   Hence all first modes `ell>=7` are absent through `K=sqrt(114)`.

2. From `ell=3,n=2`,

   $$
   j_{9/2,2}^2>\left(\frac{81}{8}\right)^2+8
   =\frac{7073}{64}=c_{42}^2,
   $$

   and, for every `p>=5`,

   $$
   j_{p+1/2,2}^2>\frac{6561}{64}+18
   =\frac{7713}{64}>114.
   $$

   Thus `(ell,n)=(4,2)` is absent at the included face `K=c_42`, and all second modes `ell>=5` are absent through `sqrt(114)`.

3. From `ell=1,n=3`, for every `p>=2`,

   $$
   j_{p+1/2,3}^2>\frac{441}{4}+4
   =\frac{457}{4}>114.
   $$

   Hence all third modes `ell>=2` are absent through `sqrt(114)`.

4. Since `j_(1/2,n)=npi`,

   $$
   j_{1/2,4}^2=16\pi^2>16\left(\frac{157}{50}\right)^2>114.
   $$

   Monotonicity in `n` and (26) exclude every `n>=4` ball mode in every angular channel through `sqrt(114)`.

Finally (25) transfers each of these fixed-channel, fixed-radial-index ball exclusions to the shell in the correct direction.  Strictness at `10`, `81/8`, `21/2`, `c_42`, and `sqrt(114)` is preserved; no endpoint mode is inadvertently counted.

## 5. Compact zero registry

| required bound | establishment |
|---|---|
| `j_(3/2,2)>77/10` | exact `ell=1` sign and count: `N_1(77/10)=1` |
| `j_(5/2,2)>9` | exact interlaced sign count: `N_2(9)=1` |
| `j_(7/2,2)>103/10` | exact interlaced sign count: `N_3(103/10)=1` |
| `j_(11/2,2)>129/10` | exact interlaced sign count: `N_5(129/10)=1` |
| `j_(3/2,3)>21/2` | exact `ell=1` sign and count: `N_1(21/2)=2` |
| `j_(5/2,3)>61/5` | exact interlaced sign count: `N_2(61/5)=2` |
| `j_(13/2,1)>10` | recurrence-polynomial signs through `ell=6`: `N_6(10)=0` |
| `j_(15/2,1)>23/2` | recurrence-polynomial signs through `ell=7`: `N_7(23/2)=0` |
| `j_(17/2,1)>71/6` | Lorch (L2) exact radical comparison; also (26) from `ell=7` |
| `j_(19/2,1)>64/5` | Lorch (L2) exact radical comparison; also (26) from `ell=7` |
| `j_(21/2,1)>69/5` | Lorch (L2) exact radical comparison |
| `j_(7/2,2)>81/8` | immediate strict consequence of `103/10>81/8` |

This exhausts (27) and (19), with the positive-zero convention, radial indices, angular channels, tangent cells, recurrence propagation, ODE simplicity, and strict rational endpoints all explicit.
