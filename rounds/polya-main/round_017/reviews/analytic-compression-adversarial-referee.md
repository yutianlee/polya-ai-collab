# Round 17 Candidate C17 adversarial referee

## Verdict

**PASS.** I assumed Candidate C17 was false and searched for the first
unsupported implication. There is none. The spectral reduction, both strict
endpoint payments, the residual-mask inclusion, the box containments, the
exact residual subtraction, and the stated obstruction to extending the same
coarse method all survive independent reconstruction.

This is a verdict on the stated closed-band lemma and its exact bookkeeping.
It is not a claim that the surviving Round 17 residual is empty.

## 1. Authentication and review order

I computed every SHA-256 below before opening any of the seven files. Every
actual digest equalled the supplied digest.

| artifact | authenticated SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `state/lemma_packets/SHELL-rho-compact-round17.md` | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `rounds/polya-main/round_017/responses/analytic-compression-incumbent.md` | `345e76cbc2f7868db0c78d803edb8c1c5eaabdc8a7189a3f8580d36b08514375` |
| `rounds/polya-main/round_017/reviews/analytic-compression-clean-room.md` | `9e75cd74df11ad903b26e5f6ccc367ab86d5d2eec080e0ddda4a4817765e05b7` |
| `rounds/polya-main/round_017/exploration/analytic-constant-audit.md` | `7fb22f516db763cc4f8fce6abf7aaa7b804fc88cd544c44589e41e3b37798be0` |
| `computations/round17_verify_candidate_c17_constants.py` | `b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469` |

The executable ledger returned `PASS`, 28 exact checks, and no first
mismatch. Its focused test suite returned `6 passed`.

## 2. Elementary constants and sign discipline

The proof needs no numerical spectral root. The elementary enclosure

\[
\frac{157}{50}<\pi<\frac{22}{7}
\tag{1}
\]

is independently available as follows. Machin's identity

\[
\pi=16\arctan\frac15-4\arctan\frac1{239}
\]

follows from the tangent addition and doubling formulas, with the resulting
angle in the principal interval. The alternating bounds

\[
x-\frac{x^3}{3}<\arctan x<x \qquad (0<x<1)
\]

then give

\[
\pi>\frac{281476}{89625}
=\frac{157}{50}+\frac{107}{179250}.
\]

The upper bound follows from the exact positive integral

\[
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\]

Throughout the closed claimed band,

\[
e=1-\rho>0,\qquad z=\frac{\pi}{e}>3,
\qquad k_j>0.
\]

Thus all later divisions by $e,\pi,\eta_\rho$, or positive polynomial
expressions have the displayed direction. Every radicand is positive. Every
squaring or square-root comparison used below has two nonnegative sides, so
no inequality direction is lost.

## 3. Complete spectral and min--max reconstruction

The authenticated spectral packet supplies the unitary direct sum and its
full form-domain summability, not merely a separation ansatz. In one angular
channel the form on $H_0^1(\rho,1)$ is

\[
\mathfrak a_\ell[u]
=\int_\rho^1\left(|u'|^2+
\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr.
\]

Because $r^{-2}\geq1$ on the interval, the comparison form has the same
domain. Dirichlet min--max therefore gives, for every $n\geq1$,

\[
\lambda_{\ell,n}\geq n^2z^2+\ell(\ell+1).
\tag{2}
\]

For $\ell=0$ the potential vanishes, so this is exact:

\[
\lambda_{0,n}=n^2z^2.
\tag{3}
\]

Since $z>3$,

\[
4z^2>z^2+6.
\tag{4}
\]

Consequently every $n\geq2$, for every angular order, lies strictly above
the complete window $K^2\leq z^2+6$. For $n=1$ and $\ell\geq2$,

\[
\lambda_{\ell,1}\geq z^2+\ell(\ell+1)
\geq z^2+6\geq K^2.
\tag{5}
\]

The only possible modes are therefore $(\ell,n)=(0,1)$ and $(1,1)$.
Their full angular multiplicities are $1$ and $3$. The authenticated
direct sum says that a numerical coincidence between different angular
orders adds orthogonal multiplicities; it cannot create an unlisted state.
Here all other radial and angular modes have already been excluded.

Using the strict global convention $\lambda<K^2$, the complete count
ledger is

\[
N_D(A_{\rho,1},K^2)=
\begin{cases}
0,&K=z,\\
1,&z<K\leq k_1,\\
1+3\,\mathbf 1_{\{\lambda_{1,1}<K^2\}},
&k_1<K\leq k_2.
\end{cases}
\tag{6}
\]

At $K=k_1$, (2) puts the $\ell=1$ value at or above $K^2$, so it is
not counted. At $K=k_2$, (5) does the same for all five $\ell=2$
states. Equality at either wall is excluded, not rounded upward. In the last
line of (6), an equality $\lambda_{1,1}=K^2$ likewise excludes all three
states. Thus the caps $0,1,4$ include every strict endpoint and every
possible multiplicity.

## 4. Weyl payment, monotonicity, and exact margin

Set

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\]

At the lower frequency wall,

\[
W(\rho,z)=\frac{2\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}>2>1,
\tag{7}
\]

because the rational factor exceeds $1$ by
$3\rho/(1-\rho)^2>0$, and $\pi>3$. The count is zero at $K=z$;
for $z<K\leq k_1$, strict monotonicity in $K>0$ pays the count $1$.
This includes $K=k_1$.

For the second band define $F(\rho)=W(\rho,k_1(\rho))$. With
$S=1+\rho+\rho^2$,

\[
F(\rho)=\frac{2}{9\pi}\,
\frac{S}{e^2}(\pi^2+2e^2)^{3/2}.
\tag{8}
\]

Its logarithmic derivative is

\[
\frac{F'}F
=\frac{1+2\rho}{S}
+\frac{2(\pi^2-e^2)}{e(\pi^2+2e^2)}>0.
\tag{9}
\]

Every denominator in (9) is positive, and $\pi^2-e^2>9-1>0$. Hence
the minimum is at $\rho_c$. From (1),

\[
\rho_c<\frac{1}{7},\qquad
1-\rho_c^3>\frac{342}{343},\qquad
z_{\rho_c}=\pi+\frac12>\frac{91}{25},
\]

and therefore $k_1(\rho_c)>39/10$. Also
$2/(9\pi)>7/99$. All factors are positive, so taking a square root and a
cube preserves direction. The exact reserve is

\[
F(\rho_c)>
\frac7{99}\frac{342}{343}\left(\frac{39}{10}\right)^3
=\frac{1127061}{269500}
=4+\frac{49061}{269500}>4.
\tag{10}
\]

For $k_1<K\leq k_2$, strict monotonicity in $K$ gives
$W(\rho,K)>F(\rho)\geq F(\rho_c)>4$, while (6) gives $N_D\leq4$.
This proves the requested strict inequality on the entire closed band,
including $\rho=\rho_c,7/8$ and $K=z,k_1,k_2$.

## 5. Exact inclusion in the frozen residual

The elementary inequalities

\[
0<\omega_0<\frac18<\rho_c,
\qquad \rho_*<\omega_0<\rho_c
\tag{11}
\]

follow from $\pi<22/7<3\sqrt3$, $\sqrt3<7/4$, $\pi>3$, and
$C_0>1$. Hence every point of

\[
\mathcal C_{17}
=\{\rho_c\leq\rho<7/8,\ z_\rho<K\leq k_2(\rho)\}
\]

lies in the strict ratio interior of $I_{16}$. For $\rho\geq\rho_c$,
cross-multiplication by $2\rho(1-\rho)>0$ gives

\[
z_\rho\geq\frac1{2\rho},
\]

with equality only at $\rho_c$. Thus $K>z_\rho$ excludes both old
lower rays A2 and A3. It also makes clear that the lower face $K=z_\rho$
of the closed lemma is old A3 coverage; at $\rho_c$ A2 shares that one
point.

The small-hole branch A4 is inapplicable by (11). For the fixed-ratio upper
branch, $G_1'(s)=-\arccos(s)/\pi<0$ and its integral representation show

\[
0<\eta_\rho\leq\omega_0<\frac18.
\]

Moreover $a_\rho=2\rho z_\rho\geq1$, with equality at $\rho_c$. The
positive-root formula, with $C_0>0$, gives

\[
K_0(\rho)>
\frac{a_\rho}{\eta_\rho^2}>64a_\rho\geq64.
\tag{12}
\]

On the other hand, $1-\rho\geq1/8$ on the closed lemma band, so

\[
k_2^2\leq(8\pi)^2+6
<(8\cdot22/7)^2+6<26^2,
\tag{13}
\]

where the last exact squared margin is $1854/49>0$. Hence A5 is false on
the candidate, on both sides of the continuous $\rho=1/2$ formula
interface and on that interface itself.

For $\rho\geq5/6$, the inclusive A6 threshold is at least
$54\cdot6^2=1944>26$; below $5/6$ its ratio gate is false. At
$\rho=5/6$ the strict separation remains. A7 can meet this ratio interval
only at $\rho=7/8$, which is excluded from $\mathcal C_{17}$ and owned
completely by A1. A8 and A9 cannot meet the ratio interval. Finally,
$K\leq k_2<26<87025$, so A10, including its equality face, is false.
A0 is left of the candidate.

Thus every A0--A10 disjunct is false on $\mathcal C_{17}$, and

\[
\boxed{\mathcal C_{17}\subset\mathcal D_{16}}.
\tag{14}
\]

More precisely, if $\overline{\mathcal C}_{17}$ is the closed lemma band,
then its only old-covered portions are $K=z_\rho$ and $\rho=7/8$, so

\[
\overline{\mathcal C}_{17}\cap\mathcal D_{16}
=\mathcal C_{17}.
\tag{15}
\]

## 6. Complete closed-box checks

For the retained Round 8 box, the ratio bounds follow from
$\rho_c<1/7<999/2000<1001/2000<7/8$. Since $z_\rho$ and
$k_2(\rho)$ increase with $\rho$,

\[
\max z_\rho<\frac{44000}{6993}
=\frac{67}{10}-\frac{28531}{69930}<\frac{67}{10},
\]

and, at the opposite ratio face,

\[
\min k_2^2-\left(\frac{168}{25}\right)^2
>\left(\frac{6280}{1001}\right)^2+6
-\left(\frac{168}{25}\right)^2
=\frac{126027526}{626250625}>0.
\]

Every quantity compared with a square root is positive. These two
coordinatewise extrema cover all four faces and corners, proving

\[
\boxed{B_0\subset\mathcal C_{17}}.
\tag{16}
\]

The proposed neighboring certified box is

\[
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
\]

Its ratio faces are the same. Its complete lower-frequency separation is

\[
\frac{168}{25}-\frac{44000}{6993}
=\frac{74824}{174825}>0.
\tag{17}
\]

At the worst upper-wall corner, $\rho=999/2000$, (1) gives the exact
squared reserve

\[
\begin{aligned}
\min k_2^2-\left(\frac{673}{100}\right)^2
&>\left(\frac{6280}{1001}\right)^2+6
-\left(\frac{673}{100}\right)^2\\
&=\frac{668749071}{10020010000}>0.
\end{aligned}
\tag{18}
\]

Thus even the full included face $K=673/100$ lies strictly below $k_2$,
and

\[
\boxed{B_1\subset\mathcal C_{17}}.
\tag{19}
\]

This is set bookkeeping only and was not used as a spectral input.

## 7. Exact residual subtraction

If the closed lemma is promoted, set

\[
\mathcal A_{17}=\mathcal A_{16}\cup\overline{\mathcal C}_{17}.
\]

By elementary set algebra and (15),

\[
\begin{aligned}
\mathcal D_{17}
&=(I_{16}\times[0,\infty))\setminus\mathcal A_{17}\\
&=\mathcal D_{16}\setminus\overline{\mathcal C}_{17}\\
&=\boxed{\mathcal D_{16}\setminus\mathcal C_{17}}.
\end{aligned}
\tag{20}
\]

Using the exact frozen upper floor $U(\rho)$, this is equivalently

\[
\boxed{
\begin{aligned}
\mathcal D_{17}
=&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\leq\rho<\frac78,
\ k_2(\rho)<K<U(\rho)\right\}.
\end{aligned}}
\tag{21}
\]

The inclusion of $\rho_c$ in the second piece and the strict inequality
$K>k_2$ are forced by the closed upper face of $\mathcal C_{17}$. This
is not a rectangular replacement of the residual. Since both $B_0$ and
$B_1$ lie inside the removed analytic set, retaining their independent
certificates causes no second subtraction; the theorem-wise uncovered set
after promotion is exactly $\mathcal U_{17}=\mathcal D_{17}$.

## 8. The four-to-nine method obstruction

Immediately above $k_2$, (2) no longer excludes the first $\ell=2$
channel. The same coarse cap must therefore change from

\[
1+3=4\quad\hbox{to}\quad1+3+5=9.
\]

At $\rho_c$, the upper bound in (1) gives

\[
z_{\rho_c}<\frac{51}{14},
\qquad k_2(\rho_c)^2<\frac{3777}{196}.
\]

Using $\pi>3$ and $1-\rho_c^3<1$, all factors being positive,

\[
W(\rho_c,k_2)<
\frac2{27}\left(\frac{3777}{196}\right)^{3/2}<9.
\tag{22}
\]

The last direction can be squared reversibly; its exact margin is

\[
81-\left(\frac2{27}\right)^2
\left(\frac{3777}{196}\right)^3
=\frac{2121156829}{50824368}>0.
\tag{23}
\]

Continuity leaves the coarse payment below $9$ immediately above the
wall. Therefore the same cap-payment mechanism cannot prove a uniform
extension there. This does **not** say that the actual count equals (9),
and it is not a counterexample to the target inequality.

## 9. Cross-proof and ledger audit

A2 and A3 share only stated, permitted mathematical inputs: the
hash-authenticated direct-sum theorem and strict convention, elementary
one-dimensional Sturm--Liouville/min--max theory, the frozen A0--A10
predicate, and elementary bounds on $\pi$. I found no shared hidden
assumption. In particular, neither proof uses a Bessel-root certificate,
sampled phase value, noncoincidence assumption, or desired theorem
conclusion.

The two reconstructions also close the delicate steps differently. A2 uses
the weak comparison (2), strict endpoint counting, the direct global bound
$K_0>64$, and its own rational reserve. A3 derives the strict
$\ell\geq1$ comparison, proves $K_0$ monotonic through $\rho=1/2$, and
uses the distinct reserve (10). Their agreement is therefore not resting on
one unexamined endpoint shortcut.

The executable ledger does not overclaim analytic content. It authenticates
the three permitted packets and checks finite rational consequences only.
Its output explicitly lists the spectral theorem, min--max, residual
identity, positive-root equation, calculus, continuity, Machin identity, and
sign conditions as assumptions it does not prove, and labels its scope a
finite-arithmetic PASS. The analytic arguments above independently discharge
those interfaces.

## 10. Formatting and hygiene

All seven authenticated artifacts decode as UTF-8, end with a newline, have
no trailing whitespace, tabs, or Unicode replacement characters, and have
balanced Markdown fences. The new referee report uses balanced display math
and no decimal or sampled quantity in a proof step.

One non-mathematical integration issue remains in the unmodified draft
`rounds/polya-main/round_017/judge/state-patch-draft.md`: prose at lines 75,
85, and 104 uses ordinary parentheses around LaTeX commands, for example
`(\mathcal D_{17})`, instead of Markdown math delimiters. This does not
alter the set formulas or the PASS verdict, but should be cleaned before the
draft is finalized. I made no change to that draft or to the graph.

## Final disposition

**PASS. First unsupported implication: none.** Candidate C17, the exact
relations $\mathcal C_{17}\subset\mathcal D_{16}$,
$B_0\subset\mathcal C_{17}$, $B_1\subset\mathcal C_{17}$, and the
subtraction (20)--(21) are all justified with strict endpoint ownership and
exact positive margins.
