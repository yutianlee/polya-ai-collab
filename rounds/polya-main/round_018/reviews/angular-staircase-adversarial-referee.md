# Round 18 Fresh Adversarial Referee: Angular Staircase

Date: 2026-07-14

Role: mandatory fresh adversarial referee. I participated in none of A2, A3,
or A4. I first reconstructed the candidate from the frozen claim and permitted
dependencies, assuming the claim false, and only then compared the incumbent,
clean-room, constant-audit, source-audit, and cross-comparison artifacts.

## Verdict

**PASS.** Candidate C18 is proved on its complete closed band. The exact new
set lies inside the frozen Round 17 residual, and subtracting it gives the
stated two-piece residual with strict lower face $K=k_5$.

**First unsupported implication: none.**

The executable ledger also passes, but this verdict rests on the analytic
reconstruction below rather than on executable assertions or agent agreement.

## 1. Byte authentication

Every assigned digest matched the bytes inspected:

| artifact | observed SHA-256 |
|---|---|
| frozen C18 claim | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| candidate freeze | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |
| A2 incumbent | `bbb1be54d3b0861442ca56b87022ef6c616fae45359914141128d871f1c42032` |
| isolated A3 review | `d94ca00eb41e4d1b33635cb8ef6a569bcfa0a70ed81549e8b4e9907483016660` |
| A4 review | `0d6c38c0790fb492d177ea50546d5bcb5fe7aa0017b5544c9a55c89ab54110e5` |
| A4 verifier | `c3d480cb85f65c9038a61aebfe411e18622b4224d7770e1c074f110330e5ea8f` |
| A4 verifier tests | `2a267c01568bbf069dc93efcc2119a75d454e33dc28b59315faf63ac58a41b50` |
| Lorch source card | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| Lorch source audit | `0b49af55a253d7ed7646d2c7b70b2225899c2159d5baa10bb719b3cd3ee785e4` |
| A2/A3 cross-comparison | `f324da8eef7b9754e4478bdd2bc3f8813b0547688d9ab3dff15600b1a7410bd5` |
| frozen residual packet | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| residual freeze | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| residual classifier | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| residual tests | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| spectral packet | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| accepted Round 17 claim statement | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| FLPS ball source card | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |

I also checked the live primary SIAM abstract at
<https://epubs.siam.org/doi/10.1137/0524050>. It identifies
$j_{\nu,1}$ as the first positive zero of $J_\nu$, gives the scope
$-1<\nu<\infty$, and prints both strict inequalities used here. The source
card correctly records that the full paper is access-controlled and makes
only a statement-level provenance claim.

## 2. Separated lower bound and the radial barrier

Put

$$
z=\frac{\pi}{1-\rho}.
$$

In angular channel $\ell$, the transformed shell form is

$$
\mathfrak a_\ell^\rho[u]
=\int_\rho^1\left(|u'|^2+
\frac{\ell(\ell+1)}{r^2}|u|^2\right)dr,
\qquad D(\mathfrak a_\ell^\rho)=H_0^1(\rho,1).
$$

Since $r^{-2}\ge1$, form ordering against the Dirichlet interval operator
and min--max give, for every radial index,

$$
\boxed{\lambda_{\ell,n}^{\rm sh}
\ge n^2z^2+\ell(\ell+1).}
\tag{1}
$$

The direction is correct: replacing $r^{-2}$ by $1$ lowers the form. For
$\ell=0$, equality holds and the frequencies are exactly $nz$.

On $\rho\ge\rho_c$,

$$
z\ge z_{\rho_c}=\pi+\frac12>\frac72.
$$

Therefore, throughout $K\le k_5$,

$$
\lambda_{\ell,n}-K^2
\ge4z^2-(z^2+30)
=3z^2-30>\frac{27}{4}>0
\qquad(n\ge2).
\tag{2}
$$

All second and higher radial modes are absent. Likewise, for $\ell\ge5$,

$$
\lambda_{\ell,1}\ge z^2+\ell(\ell+1)
\ge z^2+30=k_5^2\ge K^2.
\tag{3}
$$

At $K=k_5$, equality in the lower bound still excludes the $\ell=5$
channel because the count is strict below $K^2$. Thus only $n=1$ and
$\ell=0,1,2,3,4$ can contribute.

The attempted radial wall is genuinely outside the claim:

$$
k_5<2z
\quad\Longleftrightarrow\quad
3z^2>30,
$$

and $k_6^2-k_5^2=12>0$. More sharply, at the worst left ratio,

$$
k_6(\rho_c)^2-(2z_{\rho_c})^2
=42-3z_{\rho_c}^2
>42-3\left(\frac{51}{14}\right)^2
=\frac{429}{196}>0.
$$

Hence $k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c)$. Carrying the one-radial-mode
cap unchanged to $k_6$ would be invalid, but C18 stops before that first
unsupported extension.

## 3. Fixed-channel shell-to-ball comparison

This implication is internal; it is not supplied by Lorch.

For the unit ball in a fixed angular channel, the transformed form is

$$
\mathfrak a_\ell^0[v]
=\int_0^1\left(|v'|^2+
\frac{\ell(\ell+1)}{r^2}|v|^2\right)dr.
$$

Its form domain is $H_0^1(0,1)$, with the inverse-square term finite by the
one-dimensional Hardy inequality for $\ell\ge1$; for $\ell=0$ that term
vanishes. If $u\in H_0^1(\rho,1)$, extend it by zero on $(0,\rho]$. The
zero trace at $\rho$ implies

$$
Eu\in H_0^1(0,1),\qquad
\|Eu\|_2=\|u\|_2,\qquad
\mathfrak a_\ell^0[Eu]=\mathfrak a_\ell^\rho[u].
\tag{4}
$$

In physical variables the extension remains
$Eu(r)r^{-1}Y_{\ell m}(\omega)$, so it preserves the fixed angular
subspace. The shell trial class is a smaller class inside the same ball
channel. Min--max therefore gives the non-strict comparison in the needed
direction,

$$
\boxed{\lambda_{\ell,1}^{\rm sh}(\rho)
\ge\lambda_{\ell,1}^{\rm ball}
=j_{\ell+1/2,1}^{\,2}.}
\tag{5}
$$

There is no hidden use of global domain monotonicity and no angular mixing.

## 4. Lorch scope and exact positive-root algebra

Lorch states, for the first positive zero and $-1<\nu<\infty$,

$$
j_{\nu,1}^2>(\nu+1)(\nu+5),
\tag{6}
$$

and

$$
j_{\nu,1}^2>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
\tag{7}
$$

All three orders $5/2,7/2,9/2$ lie in scope. At $5/2$, (6) gives

$$
j_{5/2,1}^2>\frac{105}{4},
\qquad
\frac{105}{4}-\left(\frac{51}{10}\right)^2
=\frac6{25}>0.
$$

At $7/2$, the denominator in (7) is
$6(\sqrt5-1)>0$ and the bound simplifies to

$$
\frac{81\sqrt5-9}{4}>\frac{169}{4},
$$

where $81^2\cdot5-178^2=1121>0$. At $9/2$, the denominator is
$4(\sqrt{15}-2)>0$ and the bound becomes

$$
\frac{363\sqrt{15}-121}{22}
=\frac{11}{2}(3\sqrt{15}-1)>\frac{225}{4},
$$

because $66^2\cdot15-247^2=4331>0$. Since $j_{\nu,1}$ is positive,
taking square roots preserves every strict direction. Combining with (5)
gives

$$
\sqrt{\lambda_{2,1}^{\rm sh}}>\frac{51}{10},\qquad
\sqrt{\lambda_{3,1}^{\rm sh}}>\frac{13}{2},\qquad
\sqrt{\lambda_{4,1}^{\rm sh}}>\frac{15}{2}.
\tag{8}
$$

The DLMF identity
$\mathsf j_\ell(x)=\sqrt{\pi/(2x)}J_{\ell+1/2}(x)$ has a positive
prefactor for $x>0$, so the spherical and ordinary positive zeros agree.
No shell cross-product zero, higher radial mode, multiplicity, or Weyl
estimate is attributed to Lorch.

## 5. Exact caps, coincidences, and equality faces

The cumulative multiplicity is

$$
\sum_{\ell=0}^{m-1}(2\ell+1)=m^2.
\tag{9}
$$

Equations (1)--(3) and (8) produce precisely the caps
$4,9,16,25$. One convenient complete partition is

$$
q_m(\rho)=\max\{k_m(\rho),c_m\},
\qquad m=2,3,4,
$$

with $c_2=51/10,c_3=13/2,c_4=15/2$. Since both $k_m$ and $c_m$ increase
strictly with $m$, $q_2<q_3<q_4$. The count caps are

| frequency condition | possible channels | cap |
|---|---|---:|
| $K\le q_2$ | $\ell=0,1$ | $4$ |
| $q_2<K\le q_3$ | $\ell=0,1,2$ | $9$ |
| $q_3<K\le q_4$ | $\ell=0,1,2,3$ | $16$ |
| $q_4<K\le k_5$ | $\ell=0,1,2,3,4$ | $25$ |

Only the portions intersecting $k_2<K\le k_5$ are used. If a $c_m$ lies
on either side of $k_m$, the max creates the correct empty or delayed-entry
subband. At $K=c_m$, (8) is strict and the channel is absent. At
$K=k_m$, (1) and strict spectral counting exclude the newly indexed
channel. If several cross-order eigenvalues coincide, their orthogonal
multiplicities add; the table already sums every allowed multiplicity, and
all frequencies equal to $K$ are omitted simultaneously.

## 6. Moving-wall monotonicity and Weyl payments

Let

$$
\mathcal W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3,
\qquad
F_m(\rho)=\mathcal W(\rho,k_m(\rho)).
$$

Writing $e=1-\rho$, $S=1+\rho+\rho^2$, and $d=m(m+1)$ gives

$$
F_m=\frac{2}{9\pi}\frac{S}{e^2}
(\pi^2+de^2)^{3/2}
$$

and

$$
\frac{F_m'}{F_m}
=\frac{1+2\rho}{S}
+\frac{2\pi^2-de^2}{e(\pi^2+de^2)}.
\tag{10}
$$

Equivalently, after multiplying by positive factors, the derivative sign is
the sign of

$$
\pi^2(1+\rho)-d\rho^2(1-\rho)^2.
\tag{11}
$$

For $m=2,3,4$, $d\le20$, while
$\rho^2(1-\rho)^2\le1/16$ and $\pi^2>9$. Thus (11) is strictly positive.
Every $F_m$ used below is strictly increasing. For fixed positive $c$,
$\mathcal W(\rho,c)$ is strictly decreasing in $\rho$.

The rational bounds needed here are independently reconstructed from
Machin's identity and the positive Dalzell integral:

$$
\frac{157}{50}<\pi<\frac{22}{7}.
\tag{12}
$$

First, the cap $4$ is paid everywhere above $k_2$. At $\rho_c$,
$\rho_c<1/7$, $k_2^2>73/4$, and $k_2>17/4$, so

$$
F_2(\rho_c)
>\frac7{99}\frac{342}{343}\frac{73}{4}\frac{17}{4}
=\frac{23579}{4312}>4.
\tag{13}
$$

The proposed split points have strict wall ordering:

$$
\begin{aligned}
k_2(3/10)^2-c_2^2&>\frac{547}{4900}>0,\\
k_3(1/2)^2-c_3^2&>\frac{23}{4}>0,\\
k_4(1/2)^2-c_4^2&>\frac{7971}{2500}>0.
\end{aligned}
\tag{14}
$$

The fixed-threshold Weyl reserves are

$$
\begin{aligned}
\mathcal W(3/10,c_2)
&>\frac{100387329}{11000000}
=9+\frac{1387329}{11000000},\\
\mathcal W(1/2,c_3)
&>\frac{107653}{6336}
=16+\frac{6277}{6336},\\
\mathcal W(1/2,c_4)
&>\frac{18375}{704}
=25+\frac{775}{704}.
\end{aligned}
\tag{15}
$$

For $(m,r_m)=(2,3/10),(3,1/2),(4,1/2)$, if channel $m$ can contribute,
then both $K>k_m(\rho)$ and $K>c_m$. If $\rho\le r_m$, fixed-$K$
monotonicity and (15) pay $(m+1)^2$. If $\rho\ge r_m$, (10), (14), and
(15) give

$$
\mathcal W(\rho,K)>F_m(\rho)
\ge F_m(r_m)>\mathcal W(r_m,c_m)>(m+1)^2.
\tag{16}
$$

Both alternatives include equality at the ratio split, so both one-sided
traces are covered. If no channel among $2,3,4$ contributes, (13) pays the
cap $4$; otherwise take the largest contributing order $m$, use cap
$(m+1)^2$, and apply (16). Hence

$$
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K)
$$

for the entire new region $k_2<K\le k_5$. The accepted Round 17 theorem
supplies the closed subband $z\le K\le k_2$, so the complete closed C18 band
is proved.

## 7. Two independent $K_0$ routes and all upper faces

The $H_0$ branch is inactive on the candidate range. Indeed
$\omega_0<1/8<\rho_c$ (from $\sqrt3<7/4$, $3<\pi<22/7$), while $H_0$
is offered only for $\rho<\omega_0$. Equivalently, the frozen locator gives
$\rho_{HK}<94071/10^6<1/10<\rho_c$.

Two independent comparisons close the active $K_0$ branch.

**Route I (positive-root size).** Since $G_1$ decreases and
$\max\{\rho,1/2\}\ge1/2$,

$$
0<\eta_\rho\le G_1(1/2)=\omega_0<\frac18.
$$

Also
$a_\rho=2\pi\rho/(1-\rho)=2\rho z\ge1$ on
$\rho\ge\rho_c$. From the positive-root formula,

$$
K_0
=\left(\frac{\sqrt a+\sqrt{a+4\eta C_0}}{2\eta}\right)^2
>\frac a{\eta^2}>64.
\tag{17}
$$

**Route II (direct $G_1k_5$ comparison).** Put
$x=\max\{\rho,1/2\}=\cos\theta$. Then

$$
\pi G_1(x)=\sin\theta-\theta\cos\theta
=\int_0^\theta t\sin t\,dt
\le\theta(1-x).
$$

Using monotonicity of $k_5$, $\theta\le\pi/3$, $1-x\le1/2$, and
$\sqrt{z^2+30}<z+15/z$ gives

$$
\eta_\rho k_5(\rho)
<\frac\pi3+\frac5{4\pi}
<\frac{41}{28}<\frac{131}{75}<C_0.
\tag{18}
$$

If $S=\sqrt{K_0}$, its defining quadratic says
$\eta S^2-\sqrt aS-C_0=0$, hence
$\eta K_0=C_0+\sqrt{aK_0}>C_0$. Equation (18) again gives $k_5<K_0$.

For every $\rho\le7/8$,

$$
26^2-k_5^2
>26^2-\left(\frac{176}{7}\right)^2-30
=\frac{678}{49}>0.
\tag{19}
$$

Thus Route I yields $k_5<26<64<K_0$, while Route II yields the same
comparison without the coarse constant $64$.

At the inclusive seam and to its right,

$$
\frac{54}{(1-\rho)^2}\ge1944>26>k_5
\qquad(5/6\le\rho<7/8).
\tag{20}
$$

The old global face is also untouched:

$$
k_5<26<295^2=87025.
\tag{21}
$$

Therefore

$$
\boxed{k_5(\rho)<U(\rho)
\quad(\rho_c\le\rho<7/8)}.
\tag{22}
$$

## 8. Exact inclusion and subtraction

The new set has exactly the ratio and lower-frequency conditions of the
second frozen residual component, and (22) supplies its strict upper
condition. Hence

$$
\boxed{\mathcal C_{18}\subset\mathcal D_{17}.}
$$

Subtracting the included interval $(k_2,k_5]$ from the frozen interval
$(k_2,U)$, using $k_5<U$, gives exactly

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}}
$$

The newly covered face $K=k_5$ is therefore excluded from the residual.
The faces $K=k_2$ and $K=U$ retain their old owners. The first ratio piece
is disjoint from C18 and remains unchanged. Since $B_0$ and $B_1$ were
already contained in C17, neither is subtracted again.

## 9. Mandatory wall audit

| wall or mode | adversarial result |
|---|---|
| $\rho=\rho_c$ | included; $z=\pi+1/2$, radial reserve (2), base payment, and all low-ratio bridge branches are strict |
| $\rho=3/10$ | both $m=2$ bridge alternatives apply at equality; (14)--(15) leave strict reserves |
| $\rho=1/2$ | both $m=3,4$ alternatives apply; the two definitions of $\eta$ agree at $G_1(1/2)=\omega_0$ |
| $\rho=5/6$ | spectral proof is unchanged; $K_0$ and seam containment meet with strict gaps |
| $\rho=7/8$ | closed spectral theorem remains valid; the complete vertical face retains its old owner and is excluded from C18 and D18 |
| $K=z$ | $\lambda_{0,1}=z^2$ is omitted by strict counting, so $N_D=0$; Round 17 owns the face |
| $K=k_2$ | closed Round 17 owner; the new set begins strictly above it |
| $K=k_3,k_4,k_5$ | the newly indexed angular channel is excluded by (1) at equality |
| $K=c_2,c_3,c_4$ | the corresponding shell frequency is strictly larger by (5)--(8) |
| reversed/coincident $c_m,k_m$ | the $q_m=\max\{c_m,k_m\}$ partition removes every phantom or degenerate subband |
| $K=2z$ | strictly above $k_5$; exact $\ell=0,n=2$ equality would be excluded at the wall, but no region beyond is claimed |
| $K=k_6$ | strictly above $k_5$; the one-radial cap cannot be carried there at $\rho_c$ |
| $n=1,2$ | $n=1$ is counted by channel caps; every $n\ge2$ is excluded through $k_5$ by (2) |
| $\ell=0,\ldots,5$ | $0$--$4$ are included with full multiplicities; $\ell\ge5$ is excluded through the closed upper face |
| cross-order coincidence | multiplicities add across orthogonal channels and strict endpoint omission is applied in each channel |
| $K=U$ | strictly above $k_5$ and retains old analytic ownership |
| old $K=295^2$ face | strictly above $k_5$ by (19)--(21) |
| $B_0,B_1$ | already absorbed by C17; not subtracted again |

One non-fatal presentation note: A2 does not separately name the old
$295^2$ face in its final face list. Its own bound $k_5<26$ already places
the candidate below it, and A3, A4, and the independent check above make the
comparison explicit. This is not a theorem gap.

## 10. Executable reproduction

The exact finite ledger authenticated all eight whitelisted inputs and
returned **PASS**, 40 checks, `first_issue: null`. Its three output hashes
matched the assigned verifier, test, and A4-review hashes.

Commands run:

~~~powershell
python computations/round18_verify_angular_staircase.py --self-check --manifest --compact
python computations/round18_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round18_verify_angular_staircase.py computations/tests/test_round18_residual_mask.py -q
python -m compileall -q computations/round18_verify_angular_staircase.py computations/tests/test_round18_verify_angular_staircase.py
~~~

Observed results:

- angular ledger: **PASS**, 40 exact checks, first issue `null`;
- residual classifier: **PASS**, 12 self-checks;
- focused suites: **35 passed, 10 subtests passed**;
- bytecode compilation: **PASS**.

The ledger openly labels the functional analysis, external theorem,
calculus, strict-count staircase, and set subtraction as non-executable
analytic obligations. I reconstructed each above; no hard-coded Boolean in
the ledger is used as proof.

## Final decision

**PASS / first unsupported implication: none.** The form domains, Hardy
step, angular-channel preservation, min--max direction, external theorem
scope, strict positive-root algebra, radial and angular exclusions,
multiplicity caps, equality faces, moving-wall signs, ratio bridges, two
independent $K_0$ comparisons, seam/global containment, and exact residual
subtraction all survive adversarial reconstruction.
