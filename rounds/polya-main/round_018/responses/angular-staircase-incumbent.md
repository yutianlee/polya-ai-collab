# Round 18 A2 Angular-Staircase Incumbent

Status: **EXACT CANDIDATE DERIVED / NOT PROMOTED**.

Date: 2026-07-14.

Role: A2 analytic incumbent.

Baseline commit: `1caf24a0f0732038e9d162990dd3c2201daad85d`.

The two required frozen inputs were authenticated before this work began:

| artifact | required and observed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `rounds/polya-main/round_018/exploration/residual-mask-freeze.md` | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |

The external first-zero input was subsequently released by the source
auditor:

| artifact | observed SHA-256 | audit status |
|---|---|---|
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | qualified PASS at statement level |
| `rounds/polya-main/round_018/reviews/lorch-source-audit.md` | `0b49af55a253d7ed7646d2c7b70b2225899c2159d5baa10bb719b3cd3ee785e4` | PASS with an internal-comparison condition |

This file does not edit the frozen mask, promote a theorem, or create the
proof-free candidate packet. It derives the strongest complete wall of the
requested one-radial angular staircase and records its provenance boundary.

## 1. Proof-free selectable claim

Retain

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{1}
$$

For integers $m\geq2$, put

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\tag{2}
$$

### Candidate C18

The strongest closed $k_m$-wall reached by the present argument is

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_5(\rho)
}
\tag{3}
$$

and throughout this band

$$
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).
}
\tag{4}
$$

The genuinely new post-Round-17 portion is exactly

$$
\boxed{
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_2(\rho)<K\leq k_5(\rho)
\right\}.
}
\tag{5}
$$

The accepted Round 17 theorem owns the closed subband through $k_2$.
Sections 2--7 prove the new part $k_2<K\leq k_5$, including all internal
walls. Section 8 proves the exact mask containment. If a later judge
promotes (3)--(5), exact subtraction gives

$$
\begin{aligned}
\mathcal D_{18}^{\rm cand}
={}&\left\{\rho_*<\rho<\rho_c,
\ \frac1{2\rho}<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\leq\rho<\frac78,
\ k_5(\rho)<K<U(\rho)\right\}.
\end{aligned}
\tag{6}
$$

No subtraction or promotion is enacted here.

## 2. Channel forms and the product lower bound

Set $z=z_\rho$. After the unitary substitution $u(r)=rR(r)$, the shell
operator in angular channel $\ell$ is

$$
L_\ell^{\rm sh}
=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}
\quad\hbox{on }H^2(\rho,1)\cap H_0^1(\rho,1).
\tag{7}
$$

Write its eigenvalues as $\lambda_{\ell,n}^{\rm sh}$, in increasing radial
order. Since $r^{-2}\geq1$ on $(\rho,1)$, the form inequality and the
Dirichlet min--max principle give

$$
\boxed{
\lambda_{\ell,n}^{\rm sh}
\geq n^2z^2+\ell(\ell+1)
\qquad(\ell\geq0,\ n\geq1).
}
\tag{8}
$$

For $\ell=0$ the potential vanishes, so in fact

$$
\lambda_{0,n}^{\rm sh}=n^2z^2.
\tag{9}
$$

The exact direct-sum multiplicity of channel $\ell$ is $2\ell+1$.
Coincidences between different channels add these multiplicities; no
cross-channel simplicity is assumed.

## 3. Fixed-channel shell-to-ball comparison

This is the internal variational step which the Lorch source does not
supply.

Let $\mathfrak q_\ell^{\rm B}$ be the transformed radial form of the unit
ball in channel $\ell$,

$$
\mathfrak q_\ell^{\rm B}[v]
=\int_0^1\left(|v'|^2+
\frac{\ell(\ell+1)}{r^2}|v|^2\right)dr.
\tag{10}
$$

Its form domain is $H_0^1(0,1)$; finiteness of the inverse-square term
follows from the one-dimensional Hardy inequality. For
$u\in H_0^1(\rho,1)$ define

$$
(E_\rho u)(r)=
\begin{cases}
0,&0<r\leq\rho,\\
u(r),&\rho<r<1.
\end{cases}
\tag{11}
$$

The zero trace of $u$ at $\rho$ implies $E_\rho u\in H_0^1(0,1)$, and

$$
\|E_\rho u\|_{L^2(0,1)}=\|u\|_{L^2(\rho,1)},
\qquad
\mathfrak q_\ell^{\rm B}[E_\rho u]
=\mathfrak q_\ell^{\rm sh}[u].
\tag{12}
$$

Thus zero extension embeds the shell form domain isometrically into the
ball form domain **inside the same angular channel**. Applying min--max to
this smaller class of trial subspaces proves

$$
\boxed{
\lambda_{\ell,n}^{\rm sh}(\rho)
\geq\lambda_{\ell,n}^{\rm B}
=j_{\ell+1/2,n}^{\,2}.
}
\tag{13}
$$

This proves the channel-labelled comparison rather than appealing to
unlabelled domain monotonicity.

## 4. Audited first-zero thresholds

The qualified source audit verifies, from the exact inequalities printed in
the primary SIAM abstract, that for $-1<\nu<\infty$,

$$
j_{\nu,1}^2>(\nu+1)(\nu+5)
\tag{14}
$$

and

$$
j_{\nu,1}^2>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
\tag{15}
$$

The source card's exact specializations are reproduced to make every
rational threshold visible. At $\nu=5/2$, (14) gives

$$
j_{5/2,1}^2>\frac{105}{4}
=\left(\frac{51}{10}\right)^2+\frac6{25}.
\tag{16}
$$

At $\nu=7/2$, (15) gives

$$
j_{7/2,1}^2>\frac{81\sqrt5-9}{4}
>\frac{169}{4},
\tag{17}
$$

where the last strict comparison follows from
$81^2\cdot5-178^2=1121>0$. At $\nu=9/2$, it gives

$$
j_{9/2,1}^2>
\frac{11}{2}(3\sqrt{15}-1)
>\frac{225}{4},
\tag{18}
$$

where $66^2\cdot15-247^2=4331>0$. All denominators rationalized in
(17)--(18) are positive, and the zeros are positive. Hence (13) yields the
strict shell exclusions

$$
\boxed{
\begin{aligned}
\lambda_{2,1}^{\rm sh}&>c_2^2,&c_2&=\frac{51}{10},\\
\lambda_{3,1}^{\rm sh}&>c_3^2,&c_3&=\frac{13}{2},\\
\lambda_{4,1}^{\rm sh}&>c_4^2,&c_4&=\frac{15}{2}.
\end{aligned}
}
\tag{19}
$$

The external source supplies (16)--(18), not the shell comparison (13),
the radial cutoff below, or any shell cross-product estimate.

## 5. Uniform radial cutoff and exact count caps

On the candidate ratio interval, $z$ is increasing and

$$
z\geq z_{\rho_c}=\pi+\frac12>\frac72.
\tag{20}
$$

For $K\leq k_5$, (8) and (20) imply, for every $n\geq2$,

$$
\lambda_{\ell,n}^{\rm sh}-K^2
\geq4z^2-(z^2+30)
=3z^2-30>\frac{27}{4}>0.
\tag{21}
$$

Thus only the first radial mode can occur. Moreover, at $K\leq k_m$,
every $\ell\geq m$ is excluded by

$$
\lambda_{\ell,1}^{\rm sh}
\geq z^2+\ell(\ell+1)
\geq k_m^2\geq K^2.
\tag{22}
$$

Equality in (22) is also excluded because the spectral count is strict
below $K^2$. Since

$$
\sum_{\ell=0}^{q}(2\ell+1)=(q+1)^2,
\tag{23}
$$

the raw caps in the three new wall bands are $9,16,25$. The sharper caps
obtained from (19) are:

| frequency band | threshold subcase | possibly counted channels | strict-count cap |
|---|---|---|---:|
| $k_2<K\leq k_3$ | $K\leq c_2$ | $\ell=0,1$ | $4$ |
|  | $K>c_2$ | $\ell=0,1,2$ | $9$ |
| $k_3<K\leq k_4$ | $K\leq c_2$ | $\ell=0,1$ | $4$ |
|  | $c_2<K\leq c_3$ | $\ell=0,1,2$ | $9$ |
|  | $K>c_3$ | $\ell=0,1,2,3$ | $16$ |
| $k_4<K\leq k_5$ | $K\leq c_2$ | $\ell=0,1$ | $4$ |
|  | $c_2<K\leq c_3$ | $\ell=0,1,2$ | $9$ |
|  | $c_3<K\leq c_4$ | $\ell=0,1,2,3$ | $16$ |
|  | $K>c_4$ | $\ell=0,1,2,3,4$ | $25$ |

At $K=c_j$, the corresponding channel is still absent because (19) is
strict. At $K=k_3,k_4,k_5$, the next angular channel is absent by (22).
Accidental coincidences cannot enlarge any cap because the complete list of
permitted channels and their full multiplicities is already summed.

## 6. Exact Weyl-payment bridges

### 6.1 Monotonic moving walls

Let $e=1-\rho$, $S=1+\rho+\rho^2$, and

$$
F_m(\rho)=\mathcal W(\rho,k_m(\rho)).
\tag{24}
$$

Since $1-\rho^3=eS$, exact simplification gives

$$
F_m(\rho)
=\frac{2}{9\pi}\frac{S}{e^2}
\left(\pi^2+m(m+1)e^2\right)^{3/2}.
\tag{25}
$$

Writing $d=m(m+1)$,

$$
\frac{F_m'}{F_m}
=\frac{1+2\rho}{S}
+\frac{2\pi^2-de^2}
{e(\pi^2+de^2)}.
\tag{26}
$$

For $m=2,3,4$, one has $d\leq20$. Also

$$
e\leq1-\rho_c=\frac{2\pi}{1+2\pi}
\tag{27}
$$

and, because $\pi>3$,

$$
(1+2\pi)^2>49>40.
\tag{28}
$$

Consequently

$$
20e^2
\leq\frac{80\pi^2}{(1+2\pi)^2}
<2\pi^2.
\tag{29}
$$

Every term in (26) is therefore positive, and

$$
\boxed{F_2,F_3,F_4\ \hbox{are strictly increasing on }
[\rho_c,7/8].}
\tag{30}
$$

For a fixed positive frequency $c$, $\mathcal W(\rho,c)$ is strictly
decreasing in $\rho$.

### 6.2 Elementary rational bounds for $\pi$

Only

$$
3<\frac{157}{50}<\pi<\frac{22}{7}
\tag{31}
$$

is used. The upper bound follows from the positive Dalzell integral

$$
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\tag{32}
$$

For the lower bound, Machin's identity and the alternating arctangent
bounds give

$$
\pi
=16\arctan\frac15-4\arctan\frac1{239}
>16\left(\frac15-\frac1{3\cdot5^3}\right)-\frac4{239}
=\frac{281476}{89625}
=\frac{157}{50}+\frac{107}{179250}.
\tag{33}
$$

Thus all later comparisons are exact rational inequalities.

### 6.3 The cap-four baseline

At $\rho_c$, one has $\rho_c<1/7$,
$k_2^2>(7/2)^2+6=73/4$, and
$k_2>17/4$. Using $2/(9\pi)>7/99$ gives

$$
\begin{aligned}
F_2(\rho_c)
&>\frac7{99}\frac{342}{343}
\frac{73}{4}\frac{17}{4}\\
&=\frac{23579}{4312}
=4+\frac{6331}{4312}>4.
\end{aligned}
\tag{34}
$$

By (30), for every $\rho\geq\rho_c$ and $K>k_2(\rho)$,

$$
\boxed{\mathcal W(\rho,K)>4.}
\tag{35}
$$

### 6.4 The three higher payments

Choose the exact split ratios

$$
r_2=\frac3{10},
\qquad r_3=r_4=\frac12.
\tag{36}
$$

The moving wall lies strictly above the relevant Bessel threshold at each
split:

$$
\begin{aligned}
k_2(r_2)^2-c_2^2
&>\left(\frac{157}{35}\right)^2+6
-\left(\frac{51}{10}\right)^2
=\frac{547}{4900}>0,\\
k_3(r_3)^2-c_3^2
&>4\cdot3^2+12-\frac{169}{4}
=\frac{23}{4}>0,\\
k_4(r_4)^2-c_4^2
&>4\left(\frac{157}{50}\right)^2+20
-\frac{225}{4}
=\frac{7971}{2500}>0.
\end{aligned}
\tag{37}
$$

At the same split points, (31) gives the exact Weyl reserves

$$
\begin{aligned}
\mathcal W(r_2,c_2)
&>\frac7{99}\frac{973}{1000}
\left(\frac{51}{10}\right)^3
=\frac{100387329}{11000000}
=9+\frac{1387329}{11000000},\\
\mathcal W(r_3,c_3)
&>\frac7{99}\frac78
\left(\frac{13}{2}\right)^3
=\frac{107653}{6336}
=16+\frac{6277}{6336},\\
\mathcal W(r_4,c_4)
&>\frac7{99}\frac78
\left(\frac{15}{2}\right)^3
=\frac{18375}{704}
=25+\frac{775}{704}.
\end{aligned}
\tag{38}
$$

For $m=2,3,4$, let $Q_m=(m+1)^2$. Equations (30), (37), and (38) give
the bridge implication

$$
\boxed{
K>k_m(\rho),\quad K>c_m
\quad\Longrightarrow\quad
\mathcal W(\rho,K)>Q_m.
}
\tag{39}
$$

Indeed, if $\rho\leq r_m$, then
$1-\rho^3\geq1-r_m^3$ and $K>c_m$, so
$\mathcal W(\rho,K)>\mathcal W(r_m,c_m)>Q_m$. If
$\rho\geq r_m$, then

$$
\mathcal W(\rho,K)>F_m(\rho)
\geq F_m(r_m)
=\mathcal W(r_m,k_m(r_m))
>\mathcal W(r_m,c_m)>Q_m.
\tag{40}
$$

This proof also covers $\rho=r_m$ and uses no sampled crossing point.

## 7. Completion of the spectral comparison

Consider first $k_2<K\leq k_3$. If $K\leq c_2$, the first row of the
count table and (35) give

$$
N_D\leq4<\mathcal W.
\tag{41}
$$

If $K>c_2$, the cap is $9$ and (39) with $m=2$ gives
$N_D\leq9<\mathcal W$.

Next let $k_3<K\leq k_4$. The three cases

$$
K\leq c_2,
\qquad c_2<K\leq c_3,
\qquad K>c_3
\tag{42}
$$

have caps $4,9,16$. They are paid, respectively, by (35), (39) with
$m=2$, and (39) with $m=3$.

Finally let $k_4<K\leq k_5$. The four cases cut at
$c_2<c_3<c_4$ have caps $4,9,16,25$. They are paid by (35) and (39) with
$m=2,3,4$, respectively. Every comparison is strict on the Weyl side.
Together with the accepted Round 17 theorem on $z\leq K\leq k_2$, this
proves (3)--(4).

The equalities $K=c_2,c_3,c_4$ use the smaller cap, while
$K=k_3,k_4,k_5$ use the cap below the next angular entry. Thus no spectral
endpoint is silently converted from a strict to a non-strict count.

## 8. Exact containment below the frozen upper floor

The frozen packet gives $\omega_0<1/8<\rho_c$, so on the candidate ratio
interval the active upper floor is $K_0$ below $\rho=5/6$ and
$54/(1-\rho)^2$ at and above $\rho=5/6$.

For the first branch, the accepted inequalities
$0<\eta_\rho\leq\omega_0<1/8$ and the exact formula for $K_0$ give

$$
K_0(\rho)
>\frac{a_\rho}{\eta_\rho^2}
>64a_\rho
=128\rho z_\rho.
\tag{43}
$$

The function $\rho z_\rho$ is increasing and
$\rho_cz_{\rho_c}=1/2$, hence

$$
K_0(\rho)>64.
\tag{44}
$$

On the other hand, for $\rho\leq7/8$,

$$
z_\rho\leq8\pi<\frac{176}{7}
\tag{45}
$$

and therefore

$$
26^2-k_5(\rho)^2
>26^2-\left(\frac{176}{7}\right)^2-30
=\frac{678}{49}>0.
\tag{46}
$$

Thus $k_5<26<64<K_0$. On the seam branch,

$$
\frac{54}{(1-\rho)^2}\geq1944>26>k_5.
\tag{47}
$$

Consequently

$$
\boxed{k_5(\rho)<U(\rho)
\quad(\rho_c\leq\rho\leq7/8).}
\tag{48}
$$

Combining (48) with the exact normalized residual in the frozen packet
proves

$$
\boxed{\mathcal C_{18}\subset\mathcal D_{17}}
\tag{49}
$$

and the candidate subtraction (6). This uses the exact two-piece residual,
not a rectangular proxy.

## 9. Face ownership and falsification ledger

1. The ratio face $\rho=\rho_c$ belongs to the new post-$k_2$ residual
   piece and is proved here.
2. The face $\rho=7/8$ is included in the closed spectral lemma but excluded
   from $\mathcal C_{18}$ because the accepted endpoint theorem owns the
   complete vertical face.
3. The face $K=k_2$ remains owned by the accepted Round 17 band and is
   excluded from the genuinely new set by the strict lower inequality in
   (5).
4. The faces $K=k_3,k_4,k_5$ are included. Strict counting excludes the
   next angular channel at equality.
5. At $K=c_2,c_3,c_4$, the relevant shell eigenfrequency is strictly larger,
   so the smaller cap applies.
6. The formula interface $\rho=1/2$ changes no spectral statement and is
   included.
7. At $\rho=5/6$, the seam starts inclusively, but (47) leaves a large exact
   gap above the candidate.
8. The upper face $K=U(\rho)$ is never touched because of (48), and remains
   an old analytically covered face.
9. All radial indices $n\geq2$ are excluded uniformly by the strict reserve
   (21).
10. Cross-channel eigenvalue coincidences cannot increase a displayed cap;
    all permitted channel multiplicities have already been added.
11. The first-zero facts are an external, qualified statement-level input.
    The channel-preserving shell comparison is the internal proof (10)--(13)
    and is not attributed to Lorch.

## 10. Why the present wall stops at $k_5$

The stop at $k_5$ is the strongest complete $k_m$ wall for which the simple
uniform assertion "all $n\geq2$ modes are absent" remains available without
a new radial-entry argument. At the worst ratio $\rho_c$, the exact second
$\ell=0$ shell frequency is $2z_{\rho_c}$. It lies strictly between the next
two relevant walls:

$$
k_5(\rho_c)<2z_{\rho_c},
\tag{50}
$$

by $3z_{\rho_c}^2-30>27/4$, whereas $\pi<22/7$ gives

$$
\begin{aligned}
k_6(\rho_c)^2-(2z_{\rho_c})^2
&=42-3z_{\rho_c}^2\\
&>42-3\left(\frac{51}{14}\right)^2
=\frac{429}{196}>0.
\end{aligned}
\tag{51}
$$

Thus the $n=2$, $\ell=0$ mode enters before $k_6$ at the left ratio face.
Carrying the one-radial cap unchanged to $k_6$ would be the first unsupported
implication. This is a method boundary, not a counterexample; an extension
past $k_5$ must add a radial-entry staircase (and audit any further
first-zero threshold it uses).

## 11. Incumbent verdict

**PASS as an exact candidate derivation.** The source dependency is a
qualified statement-level PASS and the missing source-to-shell step has been
proved internally by fixed-channel zero extension and min--max. The closed
band through $k_5$, the exact strict new set (5), the positive Weyl payments,
the containment below $U$, and all face conventions close without a sampled
or floating-point inference.

The candidate is ready for a separately authored proof-free freeze and an
isolated reconstruction. Nothing in this response promotes it.
