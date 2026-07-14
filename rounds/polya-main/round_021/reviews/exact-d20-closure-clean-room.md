# Round 21 Exact-D20 Closure Clean-Room Review

Verdict: **PASS, conditional on A4 validation of both frozen certificate
contracts. First issue: none.**

More precisely, the analytic implications in the candidate and the two
contracts are valid.  For the compact theorem the remaining premise is A4's
authentication and exact replay of every finite leaf, wall, interface,
corner, and coverage predicate.  For the aggregate theorem the remaining
premises include, in particular, A4's outward proofs on the whole rational
ratio superset that

$$
\mathcal B(\rho,200)>0,\qquad
\mathcal B_K(\rho,200)>0,\qquad F(\rho)>0.
$$

I did not infer any of those finite predicates from contract prose or from a
displayed decimal.  Subject to their separate A4 validation, the compact and
aggregate theorems cover the accepted residual exactly and the proposed
successor residual is empty.

## 1. Isolation and byte authentication

Before reaching the verdict I read only the eleven files authorized by the
isolation instruction.  I did not inspect any other Round 21 file, any
executable, test, certificate report or audit, any aggregate route, any
incumbent exact-D20 note, any compact or aggregate theorem report, any Round
20 proof, any Git diff or log, or any other agent's work.  I ran no verifier
or test.  Apart from elementary exact calculations, the only operations were
SHA-256 authentication and reading the eleven authorized byte streams.  This
review is the only file I wrote.

Every supplied SHA-256 identity was reproduced from the bytes before the file
was read:

| authorized artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

The residual used below is therefore the authenticated accepted set

$$
\mathcal D_{20}=
\left\{(\rho,K):\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
\tag{1}
$$

No Round 21 spectral assertion is imported through (1).

## 2. Exact rational guards

I use two elementary, independently checked bounds for $\pi$.  Polynomial
division gives

$$
\frac{x^4(1-x)^4}{1+x^2}
=x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2}.
$$

Consequently,

$$
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\frac{22}{7}-\pi,
$$

so $\pi<22/7$.  For a lower bound, for $x>0$,

$$
\arctan x=\int_0^x\frac{dt}{1+t^2}
>\int_0^x(1-t^2)\,dt=x-\frac{x^3}{3}.
$$

The tangent addition identity gives
$\arctan(1/2)+\arctan(1/3)=\pi/4$, whence

$$
\frac\pi4>
\left(\frac12-\frac1{24}\right)
+\left(\frac13-\frac1{81}\right)
=\frac{505}{648}>\frac34.
$$

Thus $3<\pi<22/7$, with no decimal input.

Since all denominators are positive,

$$
\frac7{51}<\frac1{1+2\pi}
\quad\Longleftrightarrow\quad
7+14\pi<51
\quad\Longleftrightarrow\quad
\pi<\frac{22}{7}.
\tag{2}
$$

This proves $7/51<\rho_c$ exactly.  Also
$z_\rho=\pi/(1-\rho)$ is increasing in $\rho$, and

$$
z_{\rho_c}
=\frac{\pi}{1-1/(1+2\pi)}
=\pi+\frac12>\frac72.
$$

For every $\rho\geq\rho_c$ it follows that

$$
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132=\frac{577}{4}>rac{576}{4}=12^2,
$$

and hence

$$
k_{11}(\rho)>12.
\tag{3}
$$

Equations (2)--(3) establish the two exact containment guards required by
the candidate.

## 3. Compact spectral bridge and finite-contract implication

### 3.1 Zero extension and the strict bridge

For fixed $\nu\geq0$, direct differentiation on $a>\nu$ gives

$$
\frac{\partial}{\partial a}G_a(\nu)
=\frac{\sqrt{a^2-\nu^2}}{\pi a}.
\tag{4}
$$

The displayed branch tends to zero as $a\downarrow\nu$, as does $G_a(\nu)$.
Thus the extension $G_a(\nu)=0$ for $a\leq\nu$ is continuous and has the
correct one-sided derivative at the interface.  In particular, both
$G_{\rho K}(\nu)$ at $\nu=\rho K$ and $G_K(\nu)$ at $\nu=K$ are exactly
zero; neither equality is sent to the wrong formula.

The authenticated separated-spectrum packet gives, with
$\nu_\ell=\ell+1/2$,

$$
N_D(A_{\rho,1},K^2)
=\sum_{\ell\geq0}2\nu_\ell
[\gamma_{\rho,K}(\nu_\ell)]_<.
\tag{5}
$$

There is no radial root when $K\leq\nu_\ell$, so the exact active set is
$\nu_\ell<K$.  Its cardinality is

$$
\#\{\ell\in\mathbb N_0:\ell+1/2<K\}
=\max\{0,\lceil K-1/2\rceil\}.
\tag{6}
$$

For $\nu\leq\rho K$, including equality, the accepted phase enclosure is

$$
\gamma_{\rho,K}(\nu)
<G_K(\nu)-G_{\rho K}(\nu)+\frac14.
$$

For $\rho K<\nu\leq K$, zero extension gives
$G_{\rho K}(\nu)=0$, and the global phase bound gives the same inequality.
Therefore, on the entire active range,

$$
\gamma_{\rho,K}(\nu)
<A_{\rho,K}(\nu)+\frac14.
\tag{7}
$$

If $x<y$, every positive integer strictly below $x$ is strictly below $y$.
Applying this observation term by term to (5)--(7) proves

$$
N_D(A_{\rho,1},K^2)
\leq P_{\rm coarse}(\rho,K).
\tag{8}
$$

At a phase integer, $[\gamma]_< $ is the integer minus one, exactly as
required.  At a proxy integer, the same strict convention is retained; no
ordinary-floor equality has entered (8).

### 3.2 Monotonicity through both interfaces

Equation (4) immediately shows that $A_{\rho,K}(\nu)$ is weakly decreasing
in $\rho$.  Below the interface $\rho K=\nu$ the inner term is identically
zero; above it its $\rho$ derivative is negative, and the derivative starts
at zero at the interface.

For fixed $\rho$ and $\nu$, the $K$ derivative is, in the nontrivial
regions,

$$
\partial_K A_{\rho,K}(\nu)=
\begin{cases}
\dfrac{\sqrt{K^2-\nu^2}}{\pi K},
 &\nu<K\leq\nu/\rho,\\[6pt]
\dfrac{\sqrt{K^2-\nu^2}-
\sqrt{\rho^2K^2-\nu^2}}{\pi K},
 &K>\nu/\rho.
\end{cases}
\tag{9}
$$

Both expressions are positive.  For $K\leq\nu$ the zero-extended function
is zero, and (9) joins continuously at $K=\nu$ and $K=\nu/\rho$.  Hence
$A$ is weakly increasing in $K$ globally.

The map $x\mapsto[x]_< $ is weakly increasing.  When $K$ crosses a
half-integer $\nu_\ell$, the newly active term begins at
$[0+1/4]_< =0$; it creates no adverse jump.  Thus $P_{\rm coarse}$ is
weakly decreasing in $\rho$ and weakly increasing in $K$, including at
$\nu=\rho K$ and $\nu=K$.

On the compact rectangle,

$$
W_\rho=-\frac{2\rho^2K^3}{3\pi}<0,
\qquad
W_K=\frac{2(1-\rho^3)K^2}{3\pi}>0.
\tag{10}
$$

Consequently, on a closed rational leaf
$B=[\rho_-,\rho_+]\times[K_-,K_+]$,

$$
P_{\rm coarse}(\rho,K)
\leq P_{\rm coarse}(\rho_-,K_+),
\qquad
W(\rho,K)\geq W(\rho_+,K_-).
\tag{11}
$$

This proves the proposed corner orientation, including all shared and outer
faces.

### 3.3 Strict integer walls and leaf conclusion

Let

$$
x_\ell=A_{\rho_-,K_+}(\nu_\ell)+\frac14.
$$

If A4's outward enclosure contains $x_\ell$ and certainly satisfies
$X_\ell\leq M_\ell$ for an integer $M_\ell$, then $x_\ell\leq M_\ell$.
Here $x_\ell\geq1/4$, so necessarily $M_\ell\geq1$, and

$$
[x_\ell]_<
=\max\{0,\lceil x_\ell\rceil-1\}
\leq M_\ell-1.
\tag{12}
$$

This remains true when $x_\ell=M_\ell$ exactly; replacing it by an ordinary
floor would be wrong at precisely that wall.  Equations (11)--(12) imply
$P_{\rm coarse}\leq\widehat P_B$ throughout the closed leaf.  If A4 also
validates the certain lower enclosure and strict sign

$$
W_{B,-}-\widehat P_B>0,
$$

then, everywhere on that leaf,

$$
N_D\leq P_{\rm coarse}leq\widehat P_B
<W_{B,-}\leq W.
\tag{13}
$$

Thus exact A4 validation of every leaf and of the exact half-open tiling
implies the compact theorem on the entire closed root rectangle.  Half-open
ownership prevents double ownership, while proving (13) on each closed leaf
prevents a shared face from escaping the analytic estimate.

## 4. Aggregate discrete reconstruction

### 4.1 Low-tail arithmetic

Assume $\mu>1/2$ and write

$$
\mu-\frac12=J+\tau,
\qquad J\in\mathbb N_0,quad0\leq\tau<1.
$$

The low tails are exactly those $x_r=r+1/2<\mu$.  Hence their number is
$R=J$ for $\tau=0$ and $R=J+1$ for $\tau>0$.  For every $0\leq r<R$,

$$
n_r=\lfloor\mu-x_r\rfloor=J-r,
\qquad
q_r=x_r+n_r=J+\frac12.
$$

It follows, including at $\tau=0$, that

$$
\sum_{r=0}^{R-1}n_r=\frac{J(J+1)}2,
\qquad
\mu-q_r=\tau.
\tag{14}
$$

Thus all interface-loss integrals have the same length.  With
$\delta_0=0$ and
$\delta_\tau=\int_{q_r}^{\mu}G_\mu(z)\,dz$ for $\tau>0$, the qualified
source estimate gives

$$
0\leq\delta_\tau
\leq\frac{2\tau^{5/2}}{15\sqrt\mu}.
\tag{15}
$$

For a low tail, the accepted concave-head/convex-tail split gives, before
any all-tail compensation,

$$
\frac{\mathcal T_r}{2}
\leq\int_{x_r}^{K}A_{\rho,K}(z)\,dz
+\delta_\tau-\frac14
\left(\lfloor K\eta_\rho\rfloor+d_\rho n_r
-(1+d_\rho)p_r\right).
\tag{16}
$$

For completeness, the coefficient in (16) follows directly from the head
margin.  Since $d_\rho=1-2c_\rho$,
$1-c_\rho=(1+d_\rho)/2$, and

$$
\frac{n_r}{4}-\frac{1-c_\rho}{2}(n_r-p_r)
=\frac{-d_\rho n_r+(1+d_\rho)p_r}{4}.
$$

The convex part contributes $-\lfloor K\eta_\rho\rfloor/4$, while the
integral mismatch is exactly $\delta_\tau$.  When $n_r=0$, the head is
absent and $p_r=0$, so (16) remains valid.

The shelf condition and the accepted curvature lower bound give, with
$\kappa=(1-\rho)/(\pi\rho K)$,

$$
1>A(x_r)-A(x_r+p_r)
\geq\frac\kappa2\big((x_r+p_r)^2-x_r^2\big).
$$

Since

$$
C=\frac{2\pi\rho K}{1-\rho}=\frac2\kappa,
$$

this proves

$$
p_r<\sqrt{x_r^2+C}-x_r.
\tag{17}
$$

The function $f_C(x)=\sqrt{x^2+C}-x$ is positive and strictly convex, since
$f_C''(x)=C(x^2+C)^{-3/2}>0$.  The midpoint inequality on each interval
$[r,r+1]$, followed by (17), yields

$$
\sum_{r=0}^{R-1}p_r
<\sum_{r=0}^{R-1}f_C(r+1/2)
\leq\int_0^R f_C(x)\,dx
=\mathcal I(C,R).
\tag{18}
$$

The last integral is exactly

$$
\frac12\left[
R\sqrt{R^2+C}
+C\operatorname{arsinh}\!\left(\frac R{\sqrt C}\right)-R^2
\right].
$$

Summing (16), then using (14), (15), and (18), gives the strict aggregate
error estimate

$$
\begin{aligned}
&\sum_{r=0}^{R-1}\frac{\mathcal T_r}{2}
-\sum_{r=0}^{R-1}\int_{x_r}^{K}A_{\rho,K}(z)\,dz\\
&\quad<
\frac{2R\tau^{5/2}}{15\sqrt\mu}
-\frac14\left[
R\lfloor K\eta_\rho\rfloor
+d_\rho\frac{J(J+1)}2
-(1+d_\rho)\mathcal I(C,R)
\right]\\
&\quad=-\frac14\mathcal Q(\rho,K).
\end{aligned}
\tag{19}
$$

Therefore $\mathcal Q\geq0$ makes the sum of all low tails strictly smaller
than the corresponding sum of integrals.  The strictness in (19) is not a
decimal margin and does not disappear when $\tau=0$.

### 4.2 High tails, weighted identity, and strict Weyl conclusion

For $r\geq R$, one has $x_r\geq\mu$, including equality at a half-integer
inner interface.  Zero extension then makes the tail $G_K$ alone.  The
qualified convex trapezoidal-floor theorem supplies

$$
\mathcal T_r\leq2\int_{x_r}^{K}A_{\rho,K}(z)\,dz.
\tag{20}
$$

Tails beginning at or above $K$ vanish on both sides.  Thus no
high-interface tail is omitted.

Let
$h_\ell=[A_{\rho,K}(\nu_\ell)+1/4]_<$.  The exact dimension-reduction
identity is

$$
\sum_{\ell\geq0}(2\ell+1)h_\ell
=\sum_{r\geq0}\left(h_r+2\sum_{\ell>r}h_\ell\right).
\tag{21}
$$

Every parenthesis in (21) is bounded above by $\mathcal T_r$, because
strict positive-integer counting is at most the ordinary floor.  At an exact
integer proxy wall it is smaller by one, so the comparison remains in the
safe direction.  Combining (19)--(21), when $\mathcal Q\geq0$, gives

$$
P_{\rm coarse}(\rho,K)
<2\sum_{r\geq0}\int_{x_r}^{K}A_{\rho,K}(z)\,dz
=2\int_0^K f_3(z)A_{\rho,K}(z)\,dz.
\tag{22}
$$

The authenticated weighted scaffold has
$F_3(z)=\int_0^z f_3(t)\,dt\leq z^2/2$.  Since $A$ is decreasing in $z$ and
vanishes at $K$, integration by parts and the exact Weyl integral give

$$
2\int_0^K f_3A\leq
\int_0^K2zA(z)\,dz
=\frac{2}{9\pi}(1-\rho^3)K^3=W(\rho,K).
\tag{23}
$$

Together with the strict phase bridge (8), equations (22)--(23) prove

$$
\mathcal Q(\rho,K)\geq0
\Longrightarrow N_D(A_{\rho,1},K^2)<W(\rho,K).
\tag{24}
$$

This covers $\tau=0$, all half-integer $\mu$ walls, all integer
$K\eta_\rho$ walls, and all high-interface tails.  In particular,
$\lfloor y\rfloor>y-1$ is strict even when $y$ itself is an integer.

### 4.3 Continuous reserve implies the discrete reserve

Put $y=K\eta_\rho>1$ and $\overline R=\mu+1/2$.  From the two cases in the
definition of $R$ and from $\mu>3/2$,

$$
R\geq\mu-\frac12,qquad R<\overline R,
$$

$$
J>\mu-\frac32,qquad J+1>\mu-\frac12.
\tag{25}
$$

Consequently,

$$
R\lfloor y\rfloor
>R(y-1)
\geq\left(\mu-\frac12\right)(y-1),
\tag{26}
$$

and, because $d_\rho>0$,

$$
d_\rho\frac{J(J+1)}2
>\frac{d_\rho}{2}
\left(\mu-\frac32\right)
\left(\mu-\frac12\right).
\tag{27}
$$

The integrand defining $\mathcal I(C,R)$ is positive, so

$$
\mathcal I(C,R)<\mathcal I(C,\overline R)
=\overline{\mathcal I}.
\tag{28}
$$

Finally, $0\leq\tau<1$ and $R<\overline R$ imply

$$
R\tau^{5/2}<\overline R.
\tag{29}
$$

Substitution of (26)--(29) into the exact definition of $\mathcal Q$ gives
the pointwise strict comparison

$$
\mathcal Q(\rho,K)>\mathcal B(\rho,K).
\tag{30}
$$

This proof works unchanged at $\tau=0$ and at an integer $y$.  Hence

$$
\mathcal B\geq0\Longrightarrow\mathcal Q>0
\Longrightarrow N_D<W.
\tag{31}
$$

## 5. Universal frequency propagation

### 5.1 Standing guards, including $\rho=1/2$

On the rational superset

$$
\frac7{51}\leq\rho\leq\frac{39}{50},qquad K\geq200,
\tag{32}
$$

one has $1-\rho\geq11/50>0$ and

$$
\mu=\rho K\geq\frac{1400}{51}>\frac32.
\tag{33}
$$

It remains to check $K\eta_\rho>1$ without a numerical sample.  The
identity

$$
G_1(z)=\frac1\pi\int_z^1\arccos t\,dt
$$

shows that $G_1$ is decreasing.  Since
$\max\{\rho,1/2\}\leq39/50$, and since
$\arccos t\geq\sqrt{2(1-t)}$ (from
$1-\cos\theta\leq\theta^2/2$),

$$
\begin{aligned}
200\eta_\rho
&\geq200G_1(39/50)\\
&>\frac{400\sqrt2}{3\pi}
\left(\frac{11}{50}\right)^{3/2}\\
&>\frac{1400\sqrt2}{33}
\left(\frac{11}{50}\right)^{3/2}>1.
\end{aligned}
\tag{34}
$$

The last comparison is exact: the square of its left-hand expression is

$$
\frac{784\cdot1331}{25\cdot1089}
=\frac{1{,}043{,}504}{27{,}225}>1.
$$

Thus $K\eta_\rho\geq200\eta_\rho>1$.  Also

$$
b=\frac{2\pi\rho}{1-\rho}>0,qquad
S^2=\overline R^2+bK>\overline R^2,
$$

so

$$
S>\overline R=\rho K+\frac12>\rho K.
\tag{35}
$$

All definitions in the continuous reserve are therefore valid throughout
(32).  At $\rho=1/2$, the two prescribed branches are literally the same
number,

$$
G_1(1/2)=G_1(\rho)\big|_{\rho=1/2}.
$$

For $\rho<1/2$ the constant branch owns the point, and for $\rho>1/2$ the
$G_1(\rho)$ branch owns it.  No $\rho$ derivative is used in the frequency
propagation, so this interface creates no differentiability assumption.

### 5.2 Exact derivatives

For fixed $\rho$, write $I(K)=\overline{\mathcal I}$ and
$P=S-\overline R$.  The useful integral representation is

$$
I(K)=\int_0^{\overline R}
\left(\sqrt{x^2+bK}-x\right)dx.
\tag{36}
$$

Differentiation under the integral and at the moving upper endpoint gives

$$
I_K=\rho P+rac b2
\operatorname{arsinh}\left(\frac{\overline R}{\sqrt{bK}}\right).
\tag{37}
$$

Since

$$
S_K=\frac{\rho\overline R+b/2}{S}
$$

and

$$
\frac d{dK}\operatorname{arsinh}
\left(\frac{\overline R}{\sqrt{bK}}\right)
=\frac{2\rho K-1}{4KS},
$$

another differentiation yields exactly

$$
I_{KK}
=\rho^2\left(\frac{\overline R}{S}-1\right)
+\frac{\rho b}{2S}
+\frac{b(2\rho K-1)}{8KS}.
\tag{38}
$$

Differentiating the continuous reserve term by term gives

$$
\begin{aligned}
\mathcal B_K={}&
\rho(K\eta_\rho-1)
+(\mu-1/2)\eta_\rho
+d_\rho\rho(\mu-1)\\
&-(1+d_\rho)I_K
-\frac{2\rho(2\mu-1)}{15\mu^{3/2}}.
\end{aligned}
\tag{39}
$$

The derivative of the last term in (39) is

$$
E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}},
\tag{40}
$$

and therefore

$$
\mathcal B_{KK}
=2\rho\eta_\rho+d_\rho\rho^2
-(1+d_\rho)I_{KK}+E_{KK}.
\tag{41}
$$

These are precisely (A17)--(A21); no base-frequency replay is used in their
derivation.

### 5.3 All-$K$ curvature chain and conditional integrations

By (35), the first term on the right of (38) is strictly negative.  Also
$2\rho K-1<2\rho K$.  Hence, at every point of (32),

$$
I_{KK}
<\frac{\rho b}{{2S}}+\frac{\rho b}{4S}
=\frac{3\rho b}{4S}
<\frac{3b}{4K}
\leq\frac{3b}{800}.
\tag{42}
$$

Equation (33) gives

$$
E_{KK}>0.
\tag{43}
$$

Because $1+d_\rho>0$, equations (41)--(43) imply

$$
\begin{aligned}
\mathcal B_{KK}
&>2\rho\eta_\rho+d_\rho\rho^2
-\frac{3(1+d_\rho)b}{4K}\\
&\geq2\rho\eta_\rho+d_\rho\rho^2
-\frac{3(1+d_\rho)b}{800}
=F(\rho).
\end{aligned}
\tag{44}
$$

Thus (A25)--(A28) hold universally, not merely at $K=200$.

Now, and only now, assume A4 has validated the three strict base predicates
in (A23) on every ratio in the rational superset.  In particular,
$F(\rho)>0$.  Equation (44) then gives
$\mathcal B_{KK}(\rho,K)>F(\rho)>0$ for every $K\geq200$.  For $K>200$ the
two exact integrations are

$$
\mathcal B_K(\rho,K)
=\mathcal B_K(\rho,200)
+\int_{200}^{K}\mathcal B_{KK}(\rho,s)\,ds>0,
\tag{45}
$$

$$
\mathcal B(\rho,K)
=\mathcal B(\rho,200)
+\int_{200}^{K}\mathcal B_K(\rho,s)\,ds>0.
\tag{46}
$$

At $K=200$ the corresponding strict conclusions are the separately
validated base predicates themselves.  The consistency signs in (A24b)
are not used as substitutes for (42)--(46).  Combining (31), (45), and
(46) proves the aggregate theorem for all $K\geq200$, conditional exactly
on the stated A4 base validation.

## 6. Exact residual split and faces

For every point of the authenticated residual (1), equations (2)--(3) give

$$
\frac7{51}<\rho_c\leq\rho<\frac{39}{50},
\qquad
12<k_{11}(\rho)<K<U(\rho).
\tag{47}
$$

Consequently, a residual point with $K\leq200$ lies in the compact theorem
domain, while one with $K>200$ lies in the aggregate theorem domain.  At
$K=200$ both theorem statements apply, but the proposed subtraction assigns
the point only to the compact owner.  Exact trichotomy gives

$$
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\},
$$

$$
\mathcal C_{21}\cap\mathcal T_{21}=\varnothing,
\qquad
\mathcal C_{21}\cup\mathcal T_{21}=\mathcal D_{20}.
\tag{48}
$$

No ordering of $U(\rho)$ and $200$ is hidden in (48):

- if $U<200$, every residual point is compact-owned;
- if $U=200$, strictness of $K<U$ excludes the shared frequency face and
  every residual point is compact-owned;
- if $U>200$, $K<200$, $K=200$, and $K>200$ have respectively compact,
  compact, and aggregate subtraction ownership whenever the point also
  satisfies (1).

All named faces are therefore consistent:

- $\rho=7/51$ is an included compact guard face but lies below the residual;
- $\rho=\rho_c$ is residual-inclusive subject to both strict frequency
  inequalities;
- $\rho=39/50$ is residual-excluded and is not subtracted again;
- $K=12$ is a compact guard face but is below every residual point;
- $K=k_{11}(\rho)$ is residual-excluded;
- $12<K<200$ is compact-owned when (1) also holds;
- $K=200$ is compact-owned when (1) also holds, despite theorem overlap;
- $200<K<U(\rho)$ is aggregate-owned;
- $K=U(\rho)=K_0(\rho)$ is residual-excluded.

It follows from (48), conditional on the two theorem validations, that

$$
\mathcal D_{21}^{\rm proposed}
=\mathcal D_{20}\setminus
(\mathcal C_{21}\cup\mathcal T_{21})=\varnothing.
\tag{49}
$$

## 7. Final decision and boundary

**PASS, conditional on A4 certificate validation. First issue: none.**  The
compact bridge, strict cutoff and integer-wall rule, zero-extension
interfaces, corner monotonicity, aggregate low-tail identity and reserve,
continuous-reserve implication, exact derivatives, universal curvature
chain, two integrations, rational containment, and all subtraction faces
have independent analytic support.

This verdict does not authenticate or replay any sealed A4 target and does
not itself assert the finite predicates.  In particular, $F>0$ remains an
A4 certificate predicate, as do the compact leaf signs and the two strict
aggregate base signs.  If any required A4 authentication, exact coverage
check, outward comparison, or base sign fails, the corresponding theorem
and hence (49) are not established.  No broader shell or program theorem is
promoted by this review.
