# Round 9 adversarial audit: parametric thin-plateau dependencies

## Verdict

**PRIMARY PASS for $C=125/8$; fallback PASS for $C=18$, conditional on the
already-promoted Round 3 shifted-tail inputs and spectral bridge.** I found no
circular use of the old hypothesis

$$
K\ge 64\varepsilon^{-2}
$$

in the independent clean-room proof with

$$
K\ge\frac{125}{8\varepsilon^2}.
$$

Its key improvement is to retain the compensated loss
$R=p-dm$ rather than bounding $p$ alone. In scaled variables it proves

$$
R<\frac{361}{80\sqrt\varepsilon}.
$$

Every comparison needed for the $C=125/8$ theorem

$$
0<\varepsilon\le\frac1{100},
\qquad
K\ge\frac{125}{8\varepsilon^2}
$$

is valid at equality. The critical monotonicity reduction to the no-drop
geometry $m=0$, the synthetic comparison path, the no-drop branch $p=n$,
immediate-drop branch $p=0$, degenerate head $n=0$, interface wall,
head-floor wall, gain wall, and $\varepsilon=1/100$ endpoint all survive
adversarial reconstruction.

The tight final clean-room comparison is

$$
M>
\frac{2829397}{3732696}
>
\frac{132}{175}
>4\delta,
\tag{A}
$$

with exact remaining margin
$2428603/653221800>0$. The monotonicity and endpoint calculations supporting
this comparison are checked in Section 4. The separately reconstructed
$C=18$ proof remains a valid, simpler fallback and is audited in Section 5.

The exact overlap with the independently proved low aggregate-action range is

$$
0<\varepsilon\le\frac1{15625};
$$

equality belongs to both ranges. The sharper thin residual ceiling is
$125^5/8<2^{32}$. The existing $C=18$ direct envelope corollary is correct but
non-sharp; after replacing its endpoint by $1/15625$, the unchanged central
ceiling still gives the uniform all-ratio high-energy threshold
$K\ge2^{35}$.

At the time of this audit, the frozen packet and direct corollary still state
the fallback constant $18$. The primary $125/8$ result should not be described
as frozen or promoted until those artifacts are updated consistently; this
review does not edit shared state or judge files.

**Post-audit resolution.**  The frozen packet and direct corollary were
subsequently updated to $C=125/8$, $\varepsilon_{\rm new}=1/15625$, and the
thin ceiling $125^5/8<2^{32}$.  The dimensionless comparison variable was
also renamed $\widehat q$ to avoid collision with the interface mesh point.

## 1. Sources and notation

The Round 6 sources inspected line by line were:

- `rounds/polya-main/round_006/exploration/local-plateau-high-thin.md`;
- `rounds/polya-main/round_006/reviews/local-plateau-high-clean-room.md`;
- `rounds/polya-main/round_006/reviews/thin-endpoint-combined-constants.md`;
- `rounds/polya-main/round_006/responses/thin-endpoint-incumbent.md`.

The primary candidate inspected independently was
`rounds/polya-main/round_009/reviews/thin-plateau-optimized-clean-room.md`.
The verified fallback sources were
`rounds/polya-main/round_009/responses/thin-plateau-optimized-incumbent.md`,
`state/lemma_packets/SHELL-thin-local-plateau-optimized.md` and
`rounds/polya-main/round_009/responses/optimized-thin-envelope-corollary.md`.
The earlier $C=20$ ledger was also checked and is retained below only as a
superseded dependency comparison.

Write

$$
s=\sqrt\varepsilon,
\qquad
\rho=1-\varepsilon,
\qquad
\alpha=\frac{2\sqrt2}{3\pi},
\qquad
B=\frac{8\sqrt2}{15}.
$$

Thus $0<s\le1/10$. The elementary action bound and interface-loss bound are

$$
\eta=G_1(1-\varepsilon)\ge\alpha\varepsilon^{3/2},
\qquad
4\delta<B.
\tag{1}
$$

Under $K\ge C\varepsilon^{-2}$, (1) gives

$$
K\eta\ge\frac{\alpha C}{s}.
\tag{2}
$$

## 2. Inputs that are genuinely independent of $C=64$

The following imported statements were proved in Round 3 before its final
fixed-$\rho$ threshold was imposed:

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz+\delta-\frac M4,
\tag{3}
$$

$$
M=\lfloor K\eta\rfloor+d_\rho m-p,
\qquad
d_\rho=1-\frac{2\arccos\rho}{\pi},
\tag{4}
$$

and the global shelf estimate

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{5}
$$

I checked (5) against the Round 3 packet and both Round 3 reviews. It follows
from the $C$-free curvature estimate and the strict same-floor relation. It is
valid for $p=n$, $p=0$, and $q=\rho K$. Importing (3)--(5) is therefore not an
import of the old Round 6 theorem.

The uniform loss estimate in (1) is also $C$-free. Whenever a low-interface
tail exists, $\mu=\rho K>x_0\ge1/2$; this is exactly the hypothesis used in
Round 3 to obtain $\delta<2\sqrt2/15$. If no such tail exists, the statement
is vacuous.

The high-interface shifted-tail theorem, multiplicity scaffold, phase
enclosure, and strict spectral bridge are likewise upstream of the Round 6
$64$ choice. Only these upstream components may be imported. In particular,
none of the following may be imported into a proof for $C<64$:

- $x_0\ge K/2$ from the Round 6 incumbent;
- $p<10/\sqrt\varepsilon$ from the incumbent or combined review;
- $x_0/(\rho K)>9/10$ from the Round 6 clean-room review;
- $p<8/\sqrt\varepsilon$ from that review;
- $K\eta>14/\sqrt\varepsilon$ from that review;
- the already-combined endpoint $\varepsilon\le2^{-18}$.

Using any of those conclusions without rederivation would be circular.

## 3. Complete map of the old $64$ dependencies

### 3.1 Round 6 incumbent and combined audit

In the dangerous branch $R=p-d_\rho m>0$, the incumbent uses
$d_\rho>2/3$ and obtains

$$
U:=\rho K-x_0<1+\frac52p.
\tag{6}
$$

These facts are $C$-free. The old threshold enters in the following places.

1. **Outer-half localization.** The displayed incumbent proof of
   $x_0\ge K/2$ remains valid provided

   $$
   C\ge\frac{625}{288}.
   \tag{7}
   $$

   Indeed its contradiction is
   $K<125000/(576\varepsilon)$, whereas
   $K\ge C\varepsilon^{-2}\ge100C/\varepsilon$. Condition (7) is exactly
   what makes the two incompatible. It also implies the auxiliary $K>100$.

2. **Local slope.** The identity

   $$
   -A'(z)\ge\frac{\varepsilon z}
   {\pi\sqrt{K^2-z^2}}
   \tag{8}
   $$

   and its integration over $[x_0,x_0+p]$ are $C$-free. The parameter is used
   only after (8), through the localization and through $1/K\le
   \varepsilon^2/C$.

3. **Incumbent quadratic.** The exact $C$-dependent replacement of the
   Round 6 displayed quadratic is

   $$
   p^2<\frac{8\pi^2}{\varepsilon}
   +\frac{20\pi^2}{C}p+\frac{8\pi^2}{C}.
   \tag{9}
   $$

   It implies $p<10/s$ once

   $$
   C\ge
   \frac{502\pi^2}{25(100-8\pi^2)}.
   \tag{10}
   $$

   The proof's rational substitution $\pi^2<10$ gives the slightly larger
   sufficient condition $C\ge251/25$. At equality the strict inequality in
   (9) still rules out $p=10/s$.

4. **Action gain and payment.** Replacing $64$ by $C$ changes the incumbent
   lower bound to

   $$
   M>\frac{\alpha C-10}{s}-1.
   \tag{11}
   $$

   The exact condition needed only for $M>4\delta$ is

   $$
   C\ge
   C_{\rm inc,pay}
   :=\frac{303\pi\sqrt2}{40}+\frac{2\pi}{25}.
   \tag{12}
   $$

   This is the genuine incumbent bottleneck. A simple rationalized choice is
   $C=34$. If one insists on retaining the much stronger displayed
   intermediate claim $M>17/3$, the sufficient condition becomes
   $C\ge8\sqrt2\pi$; that stronger margin is not required for closure.

The Candidate B portion of the combined Round 6 audit repeats exactly these
four uses. It introduces no additional analytic condition. Its only new use
of $64$ is the overlap calculation, which for general $C$ is

$$
\frac{C}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
\varepsilon\le\frac1{64C^2}.
\tag{13}
$$

### 3.2 Round 6 clean-room proof

The clean-room proof improves the dangerous-branch bookkeeping to

$$
d_\rho>\frac45,
\qquad
U<1+\frac94p.
\tag{14}
$$

Again (14) is $C$-free. Its explicit uses of $64$ are as follows.

1. **Surplus action statement.** Retaining the boxed statement
   $K\eta>14/s$ would require

   $$
   C>\frac{21\pi}{\sqrt2}.
   \tag{15}
   $$

   This is an artificial requirement: the final proof needs only enough gain
   to pay $p$ and $4\delta$, not the number $14$.

2. **Localization at $t>9/10$.** If the two terms are bounded separately as
   in the Round 6 text, the larger condition is

   $$
   C\ge\frac{128\pi}{11}.
   \tag{16}
   $$

   If they are aggregated before rounding, put

   $$
   b_9=\frac94\sqrt{\frac{2\pi}{99}}.
   $$

   The exact condition for that same $t>9/10$ conclusion is

   $$
   C\ge C_{9/10}
   :=25\left(
   b_9+\sqrt{b_9^2+\frac1{24750}}
   \right)^2.
   \tag{17}
   $$

   Exact rational bounds $333/106<\pi<22/7$ show
   $32<C_{9/10}<33$.

3. **Clean-room quadratic.** Conditional on $t>9/10$, the correct
   parametric inequality is

   $$
   p^2<\frac{200\pi^2}{81}
   \left(
   \frac1\varepsilon+\frac1C+\frac{9p}{4C}
   \right).
   \tag{18}
   $$

   It implies $p<8/s$ once

   $$
   C\ge
   \frac{181\pi^2}{2592-100\pi^2}.
   \tag{19}
   $$

   Using only $\pi<4$, the rational sufficient condition is $C\ge181/62$.

4. **Clean-room payment.** Once $p<8/s$ has been rederived under the new
   hypothesis, the exact condition for closure is

   $$
   C\ge
   C_{\rm clean,pay}
   :=\frac{243\pi\sqrt2}{40}+\frac{2\pi}{25}.
   \tag{20}
   $$

Thus a blind preservation of every old boxed intermediate bound would be
controlled by (15), not by the theorem's real needs. A logically
reparameterized proof with the fixed $t>9/10$, $p<8/s$ architecture is
instead controlled by (17), and $C=33$ is its smallest integer choice. The
new $C=20$ proof must therefore change the localization target; it cannot
cite the old $p<8/s$ conclusion.

## 4. Primary audit of the clean-room constant $C=125/8$

### 4.1 Scaled variables and dangerous geometry

Put

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2,
\qquad
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{P1}
$$

Then $0<y\le1/10$ and the new threshold is exactly
$\kappa\ge125/8$. The clean-room proof first strengthens the $C$-free bound
on

$$
d=1-\frac{2\arccos\rho}{\pi}.
$$

Its argument is sound. With $u=\pi/40$, the bounds $3<\pi<4$ give
$3/40<u<1/10$, and

$$
\sin u>u-\frac{u^3}{6}
>\frac3{40}-\frac1{6000}
=\frac{449}{6000}>\frac{71}{1000}.
$$

Thus

$$
1-\cos\frac\pi{20}
=2\sin^2\frac\pi{40}
>2\left(\frac{71}{1000}\right)^2
>\frac1{100}.
$$

Since $\rho\ge99/100$, it follows that
$\arccos\rho<\pi/20$ and therefore

$$
\boxed{d>\frac9{10}}.
\tag{P2}
$$

In the dangerous branch $R=p-dm>0$, one has $p>0$ and

$$
m<\frac{10}{9}p,
\qquad
U<1+p+m<1+\frac{19}{9}p.
\tag{P3}
$$

The scaled relations are exact:

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{P4}
$$

No integrality is assumed for $R$ or $r$.

### 4.2 Localization and the exact scaled plateau inequality

Let $t=x_0/\mu$, $w=1-t$, and define

$$
\widehat q:=\frac{y^4+y^3S}{\kappa\rho}.
$$

Because $\beta<1$,

$$
w=\frac U\mu<\widehat q.
\tag{P5}
$$

The global Round 3 shelf bound gives

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Together with $S<19P/9$, this yields

$$
\widehat q<
\frac{y^4}{\kappa\rho}
+\frac{19}{9}y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{P6}
$$

At the simultaneous worst endpoint
$y=1/10$, $\kappa=125/8$, $\rho=99/100$,

$$
\frac{y^4}{\kappa\rho}
\le\frac8{1237500}<\frac1{1000},
$$

and, using $\pi<22/7$,

$$
y^2\frac{2\pi}{\kappa\rho}
\le\frac{352}{86625}
=\frac{32}{7875}
<\frac1{225}.
$$

Consequently

$$
\widehat q<\frac1{1000}+\frac{19}{135}
=\frac{3827}{27000}
<\frac17,
\tag{P7}
$$

where the final exact margin is $211/189000$. Hence
$t>1-\widehat q>6/7$ and, in
particular, $x_0>K/2$. This is a fresh localization under $125/8$, not the
Round 6 outer-half lemma.

Next put

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho}.
\tag{P8}
$$

Then

$$
\widehat q=a(Q-1),
\qquad
\varepsilon+\frac UK<y^2Q.
\tag{P9}
$$

The exact local slope, (P5), (P9), and the strict same-floor relation give

$$
1>p\sigma(x_0)
>
\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
$$

All quantities being squared are positive because $\widehat q<1/7$.
Therefore

$$
\boxed{
P^2<H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{P10}
$$

I find no missing factor of $y$, $\rho$, or $\kappa$ in (P10).

### 4.3 Monotonicity in $r$ and the synthetic $P'$ path

This is the most delicate part of the clean-room proof. At fixed
$y,\kappa,d$, equation (P4) gives

$$
\frac{\partial Q}{\partial r}=-\frac{y}{\kappa d}<0,
\qquad
\frac{\partial Q}{\partial P}
=\frac y\kappa\left(1+\frac1d\right)>0.
$$

Since $\widehat q=a(Q-1)$,

$$
\frac{\partial H}{\partial Q}
=2\pi^2
\frac{1+\widehat q+2a}{(1-\widehat q)^3}>0.
$$

Thus $H$ is indeed decreasing in $r$, and

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q}{\partial P}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
\tag{P11}
$$

The endpoint bounds $d>9/10$, $\widehat q<1/7$, $a\le1/99$ and
$\kappa\ge125/8$ give

$$
\frac{\partial Q}{\partial P}<\frac{76}{5625},
$$

and exact simplification of (P11) gives

$$
\frac{\partial H}{\partial P}
<
\frac{673816}{1366875}
<\frac12,
\tag{P12}
$$

with final margin $19243/2733750$.

Set $B_*=361/80$. Suppose $r\ge B_*$. Since $R\le p$, also
$P\ge r\ge B_*$. Monotonicity in $r$ gives

$$
P^2-H(P,r)\ge P^2-H(P,B_*).
\tag{P13}
$$

The use of a synthetic path $P'\in[B_*,P]$ is legitimate. Along that path,

$$
S(P',B_*)=P'+\frac{P'-B_*}{d}
<\frac{19}{9}P'.
$$

Moreover $P'\le P$, so every $P'$ remains below the actual global shelf
ceiling. Hence the proof of $\widehat q<1/7$ and therefore (P12) remains
valid on the
whole path. It follows that

$$
\frac d{dP'}
\left(P'^2-H(P',B_*)\right)
>2B_*-\frac12
=\frac{341}{40}>0.
\tag{P14}
$$

There is no hidden assumption that the synthetic $P'$ or the associated
$m'$ is integral; only the displayed algebraic bounds are used.

At $P=r=B_*$, (P4) gives $S=B_*$, i.e. the no-drop geometry $m=0$. Here

$$
Q=1+\frac{y^2+yB_*}{\kappa},
\qquad
\widehat q=\frac{y^4+B_*y^3}{\kappa(1-y^2)}.
$$

Both expressions increase with $y$ and decrease with $\kappa$. Their maxima
are therefore at $y=1/10$, $\kappa=125/8$, where direct reduction gives

$$
Q_*=\frac{12869}{12500},
\qquad
\widehat q_*=\frac{41}{137500}.
\tag{P15}
$$

Using $\pi<22/7$, the endpoint margin recomputes exactly as

$$
B_*^2
-2\left(\frac{22}{7}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=\frac{72581986185449}{5925464687161600}>0.
\tag{P16}
$$

Equations (P13)--(P16) imply
$P^2-H(P,r)>0$, contradicting (P10). Therefore

$$
r<B_*,
\qquad
\boxed{R<\frac{361}{80\sqrt\varepsilon}}.
\tag{P17}
$$

The phrase "the worst loss occurs at $m=0$" is justified in this comparison
sense: the boundary case that controls (P16) has $P=r$, hence $m=0$. The
proof does not assert an unjustified pointwise maximization over unrelated
plateaux.

### 4.4 Final payment and its tight margin

The clean-room rational certificate for $\pi<1571/500$ has the correct
alternating-series directions. Independent reduction gives

$$
\frac{1571}{500}
-\left[
16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
\right]
=\frac{2736890694763}{6719303882812500}>0.
\tag{P18}
$$

Together with $140/99<\sqrt2$ and $\kappa\ge125/8$, this gives

$$
\frac{2\sqrt2\,\kappa}{3\pi}
\ge\frac{125\sqrt2}{12\pi}
>\frac{2187500}{466587}.
\tag{P19}
$$

On $R>0$, equations (P17)--(P19) and
$\lfloor x\rfloor>x-1$ yield

$$
M=L-R
>
\left(
\frac{2187500}{466587}-\frac{361}{80}
\right)\frac1y-1
=\frac{6562093}{37326960y}-1.
$$

The worst endpoint $y=1/10$ gives

$$
M>\frac{2829397}{3732696}.
\tag{P20}
$$

Since $\sqrt2<99/70$,

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
$$

and the final margin is exactly

$$
\frac{2829397}{3732696}-\frac{132}{175}
=\frac{2428603}{653221800}>0.
\tag{P21}
$$

Although small, this is a rational strict margin, not a floating-point
observation. If $R\le0$, then $M\ge L>K\eta-1>1>4\delta$, so the easy branch
does not use (P17).

### 4.5 Branches, walls, and threshold equality

All exceptional cases remain valid.

1. For $n=0$, one has $p=m=R=0$ and the easy gain closes directly.
2. For $p=0$, $R=-dm\le0$; the local-slope and scaled-loss argument is not
   invoked.
3. For no drop $p=n>0$, $m=0$, $P=r$, and the case is exactly represented by
   the endpoint geometry in (P15)--(P16).
4. The boundary $R=0$ belongs to the easy branch.
5. At $q=\mu$ in the original Round 3 notation, $\beta=0$ and $\delta=0$;
   the strict inequality $U<1+p+m$ remains valid.
6. Equality of the plateau floors implies a difference strictly below one,
   including when either sample is an integer.
7. At a gain wall $K\eta\in\mathbb Z$, the inequality
   $\lfloor K\eta\rfloor>K\eta-1$ remains strict.
8. At $K=125/(8\varepsilon^2)$, one has $\kappa=125/8$. Strictness comes
   from (P5), the same-floor relation, the rational bounds, and the floor
   inequality; threshold equality is included.
9. At $\varepsilon=1/100$, the exact endpoint margins (P16) and (P21) remain
   positive.
10. The strict spectral proxy is only majorized by the ordinary-floor proxy;
    no spectral wall is converted into an equality.

### 4.6 Overlap and envelope consequence

The optimized high range and the aggregate-action low range overlap exactly
when

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
125\sqrt\varepsilon\le1
\iff
\boxed{\varepsilon\le\frac1{15625}}.
\tag{P22}
$$

At equality, both thresholds are

$$
K=\frac{125^5}{8}.
$$

Both component ranges include equality. Thus the all-frequency endpoint can
be enlarged to

$$
1-\frac1{15625}\le\rho<1.
\tag{P23}
$$

Accordingly the updated compact interval is

$$
I_{\rm cr}=
\left[\rho_*,1-\frac1{15625}\right].
$$

On its complementary thin strip
$1/15625\le\varepsilon\le1/100$, any residual point satisfies

$$
K<\frac{125}{8\varepsilon^2}
\le\frac{125^5}{8}<2^{32}.
\tag{P24}
$$

The last comparison is exact after multiplying by eight:
$125^5=30517578125<34359738368=2^{35}$. The unchanged central residual
$180000^2<2^{35}$ still controls the global three-zone ceiling. Consequently
the all-ratio high-energy corollary remains

$$
0<\rho<1,
\qquad
K\ge2^{35}
\quad\Longrightarrow\quad\text{shell Polya}.
$$

## 5. Verified fallback: reconstruction of the optimized $C=18$ proof

### 5.1 Rational constants and the Machin bound

The square-root comparisons are exact:

$$
140^2=19600<19602=2\cdot99^2,
\qquad
2<\frac94.
$$

Thus $140/99<\sqrt2<3/2$. The stated proof of
$\pi<355/113$ also has the correct truncation directions. Machin's identity
is

$$
\pi=16\arctan\frac15-4\arctan\frac1{239}.
$$

The five-term alternating sum for $\arctan(1/5)$ ends with a positive term
and is an upper bound. The two-term sum
$1/239-1/(3\cdot239^3)$ is a lower bound for $\arctan(1/239)$; multiplying it
by $-4$ therefore gives an upper bound in Machin's identity. Independent
rational reduction gives exactly

$$
\frac{355}{113}
-\left[
16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
\right]
=
\frac{45167474711}{189820334689453125}>0.
\tag{21}
$$

Thus every use of $\pi<355/113$ in the incumbent is certified without a
floating-point appeal.

### 5.2 Dangerous branch and new localization

As in the $C$-free bookkeeping above, put

$$
R=p-dm,
\qquad
U=\rho K-x_0=p+m+\beta.
$$

If $R>0$, then $p>0$, $d>4/5$, $m<5p/4$, and

$$
U<1+\frac94p.
\tag{22}
$$

No high-energy assumption enters (22). Dividing it by $\mu=\rho K$ and using
the unconditional shelf estimate gives

$$
\frac U\mu
<
\frac1{\rho K}
+\frac94\sqrt{\frac{2\pi}{\varepsilon\rho K}}.
\tag{23}
$$

Under $K\ge18\varepsilon^{-2}$, both resulting upper bounds increase with
$\varepsilon$ on $(0,1/100]$. Their worst values are therefore at
$\varepsilon=1/100$, where

$$
\frac1{\rho K}\le\frac1{178200},
\qquad
\frac{2\pi}{\varepsilon\rho K}\le\frac\pi{891}.
\tag{24}
$$

Let

$$
S=\frac49\left(\frac{67}{500}-\frac1{178200}\right)
=\frac{119389}{2004750}.
$$

The decisive square comparison recomputes to

$$
S^2-\frac{355}{113\cdot891}
=\frac{9377802773}{454149549562500}>0.
\tag{25}
$$

Equations (21) and (25) imply $\sqrt{\pi/891}<S$. Hence (23)--(24) give

$$
\frac U\mu<\frac1{178200}+\frac94S=\frac{67}{500},
\qquad
\boxed{t:=\frac{x_0}{\mu}>\frac{433}{500}}.
\tag{26}
$$

Every inequality needed for (26) remains strict at
$\varepsilon=1/100$ and $K=18\varepsilon^{-2}$. This localization is newly
derived; neither $x_0\ge K/2$ nor the old $t>9/10$ statement is imported.

### 5.3 Local slope and shelf polynomial

At $x_0=\mu t$, the exact identity and monotonicity of the integrand give

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
$$

Since $1-\rho^2t^2\le2(\varepsilon+U/K)$, (26) implies

$$
\sigma(x_0)>
\frac{433\varepsilon}
{500\pi\sqrt{2(\varepsilon+U/K)}}.
\tag{27}
$$

For $p>0$, the same-floor relation is strict:

$$
1>A(x_0)-A(x_0+p)
\ge p\sigma(x_0).
\tag{28}
$$

Using (22), $1/K\le\varepsilon^2/18$, and (27)--(28) yields

$$
p^2<A_0\left(
\frac1\varepsilon+\frac1{18}+\frac p8
\right),
\qquad
A_0=\frac{2\pi^2}{(433/500)^2}.
\tag{29}
$$

The coefficient of $p$ is correct because
$(9/4)/18=1/8$. Independent rational reduction gives

$$
2\left(\frac{355}{113}\right)^2
\left(\frac{500}{433}\right)^2
=\frac{63012500000}{2394047041},
$$

and

$$
\frac{1053}{40}
-\frac{63012500000}{2394047041}
=\frac{431534173}{95761881640}>0.
\tag{30}
$$

Thus $A_0<1053/40$ with the required strict direction.

Put $x=\varepsilon^{-1/2}\ge10$, $b=53/10$, and

$$
F_x(y)=y^2-\frac{1053}{320}y
-\frac{1053}{40}\left(x^2+\frac1{18}\right).
$$

The source's three polynomial identities all recompute exactly:

$$
b^2-\frac{1053}{40}=\frac{353}{200}>0,
$$

$$
F_{10}(53)=\frac{203}{320}>0,
$$

and

$$
\left.
\frac d{dx}F_x(bx)
\right|_{x=10}
=\frac{57151}{3200}>0.
\tag{31}
$$

Because the last derivative increases with $x$, $F_x(bx)>0$ for every
$x\ge10$. Also $\partial_yF_x(y)>0$ for $y\ge bx\ge53$. If $p\ge bx$, then
$F_x(p)>0$, contradicting the strict upper quadratic (29)--(30). Therefore

$$
\boxed{p<\frac{53}{10\sqrt\varepsilon}}.
\tag{32}
$$

This is a complete rederivation under $C=18$, not an invocation of either
Round 6 shelf bound.

### 5.4 Action gain, integrality, and all branches

The action estimate under $C=18$ is

$$
K\eta
\ge\frac{12\sqrt2}{\pi\sqrt\varepsilon}.
$$

The rational bounds in (21) give the strict comparison

$$
\frac{12\sqrt2}{\pi}
>
12\frac{140}{99}\frac{113}{355}
=\frac{12656}{2343}.
\tag{33}
$$

Subtracting (32) from (33) gives exactly

$$
K\eta-p
>
\left(\frac{12656}{2343}-\frac{53}{10}\right)
\frac1{\sqrt\varepsilon}
=\frac{2381}{23430\sqrt\varepsilon}
\ge\frac{2381}{2343}
=1+\frac{38}{2343}>1.
\tag{34}
$$

There is no rounding error in the small final margin. Since $p$ is an
integer, (34) implies

$$
L=\lfloor K\eta\rfloor\ge p+1.
\tag{35}
$$

Indeed, if $\lfloor K\eta\rfloor\le p$, then
$K\eta<\lfloor K\eta\rfloor+1\le p+1$, contradicting (34). If $K\eta$ is an
integer, (34) actually forces $K\eta\ge p+2$, so the gain wall is safer, not
more delicate.

The branches now close as follows.

1. If $R>0$, then
   $M=L+dm-p\ge1+dm\ge1$. This includes no drop $p=n>0$, for which $m=0$.
2. If $R\le0$, then $M=L-R\ge L$. Equation (33) and
   $1/\sqrt\varepsilon\ge10$ give $K\eta>50$, hence $L\ge1$.
3. If $p=0$, necessarily $R=-dm\le0$; no local-slope division is used.
4. If $n=0$, then $p=m=0$ by convention and $M=L\ge1$.
5. The boundary $R=0$ belongs to the easy branch and gives $M=L$ exactly.

Finally,

$$
4\delta<\frac{8\sqrt2}{15}<\frac45<1\le M.
\tag{36}
$$

Thus $M>4\delta$ in every branch. The proof's decisive gain is discrete; a
continuous replacement of $L$ by $K\eta-1$ would unnecessarily lose it.

### 5.5 Walls and threshold endpoints

The requested falsification cases all pass.

1. **$\varepsilon=1/100$.** It is simultaneously the worst localization,
   polynomial, and gain endpoint. The exact positive margins in
   (25), (30), (31), and (34) survive there.
2. **$K=18\varepsilon^{-2}$.** All replacements of $1/K$ are non-strict,
   but (22), (26)--(28), (30), (32)--(34), and (36) are strict. Threshold
   equality is included.
3. **No drop $p=n$.** For $p>0$, $m=0$ and $R=p>0$; Proposition 3.1 supplies
   (28). The first-drop theorem is not misapplied.
4. **Immediate drop $p=0$ and head $n=0$.** These are kept in the easy branch
   and never enter a division by $p$.
5. **Interface wall $q=\mu$.** Then $\beta=0$ and $\delta=0$; all estimates
   improve or remain unchanged.
6. **Head floor wall.** Two samples with the same ordinary floor differ by
   strictly less than one. If the larger value is an integer, the possible
   difference only decreases.
7. **Gain wall.** The integer case is covered by the strengthened observation
   following (35).
8. **Outer trapezoid wall.** The prior zero-extension theorem handles a
   nonintegral overshoot, while an integral endpoint has value zero.
9. **Spectral and transferred-phase walls.** The strict phase count is only
   majorized by the ordinary-floor proxy; it is never replaced by an
   ordinary-floor equality.

### 5.6 Exact overlap

The inclusive high and low ranges meet precisely when

$$
\frac{18}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
144\sqrt\varepsilon\le1
\iff
\boxed{\varepsilon\le\frac1{20736}}.
\tag{37}
$$

At equality their common frequency is

$$
18\cdot20736^2
=2^{17}3^{10}
=7739670528
<2^{33},
\tag{38}
$$

and the optical value is
$\varepsilon K=2^9 3^6=373248$. Both component theorems include equality,
so no seam is lost.

## 6. Audit of the $C=18$ fallback envelope corollary

Let

$$
I_9=\left[\rho_*,1-\frac1{20736}\right].
$$

The direct $C=18$ corollary is correct as written, but it is no longer sharp
once the primary $C=125/8$ proof is accepted.

1. For $1-1/20736\le\rho<1$, one has
   $0<\varepsilon\le1/20736$. Equation (37) makes the union of the two
   inclusive $K$ ranges all of $[0,\infty)$. The lower $\rho$ endpoint is
   included and $\rho=1$ remains excluded.
2. On the remaining thin zone
   $1/20736\le\varepsilon\le1/100$, a residual point must satisfy the strict
   inequalities
   $$
   \frac1{8\varepsilon^{5/2}}<K<\frac{18}{\varepsilon^2}.
   $$
   The high endpoint decreases with $\varepsilon$, so (38) is its maximum.
3. The Round 8 left residual remains below $64$. The central residual remains
   below
   $$
   180000^2=32400000000<34359738368=2^{35}.
   $$
   This central ceiling, not the new thin ceiling, controls the three-zone
   maximum.
4. Hence every residual on $I_9$ has $K<2^{35}$, and threshold equality
   $K=2^{35}$ belongs to the analytic high-energy range.
5. The already-proved small-hole endpoint covers
   $0<\rho\le\rho_*$, $I_9$ includes both of its endpoints, and the enlarged
   thin endpoint begins at $1-1/20736$. These three closed/open conventions
   cover every $0<\rho<1$ with no gap. Therefore
   $$
   0<\rho<1,
   \qquad
   K\ge2^{35}
   \quad\Longrightarrow\quad\text{shell Polya}.
   $$

The statement that the old thin band
$2^{-18}\le\varepsilon\le1/20736$ is removed is harmless, but the portion
that is *newly* removed is more precisely
$2^{-18}<\varepsilon\le1/20736$, because the old theorem already covered
$\varepsilon=2^{-18}$. This wording point does not alter the cover or any
endpoint inclusion.

For the recommended primary constant, replace $1/20736$ throughout this
corollary by $1/15625$, replace the thin ceiling $7739670528$ by
$125^5/8<2^{32}$, and replace the thin high threshold $18\varepsilon^{-2}$
by $125/(8\varepsilon^2)$. The central bound remains unchanged, so the final
$2^{35}$ all-ratio high-energy statement and all closed/open endpoint
conventions remain valid.

## 7. Promotion pre-mortem

Promotion of the primary $C=125/8$ result should be rejected if a later
manuscript:

- imports $x_0\ge K/2$, $t>9/10$, $p<8/\sqrt\varepsilon$, or
  $p<10/\sqrt\varepsilon$ from a proof assuming $C=64$;
- asserts that $H$ decreases in $r$ without holding $y,\kappa,d,P$ fixed;
- differentiates $H$ in $P$ while omitting the dependence of
  $\widehat q=(y^2/\rho)(Q-1)$ on $Q$;
- uses the synthetic $P'$ path without checking
  $S(P',B_*)<19P'/9$ and the inherited global shelf ceiling along the entire
  path;
- claims the worst case is $m=0$ without the two monotonicity comparisons
  (P13)--(P16);
- replaces either $Q_*=12869/12500$ or
  $\widehat q_*=41/137500$ by a rounded decimal;
- loses the exact final payment margin $2428603/653221800$;
- applies the dangerous-loss argument when $R\le0$ or assumes that $R$ is an
  integer;
- loses threshold equality at $K=125/(8\varepsilon^2)$ or overlap equality at
  $\varepsilon=1/15625$;
- reverses either alternating-series direction in the Machin bound;
- replaces the strict transferred phase count by an ordinary-floor identity.

If the primary monotonicity argument is later changed rather than copied,
the independently valid $C=18$ fallback must still be rejected if that
replacement:

- quotes its localization or shelf bound without the new $C=18$ polynomial
  calculations;
- changes the strict inequality $K\eta-p>1$ to a non-strict one before
  applying integrality;
- treats $p$ as nonintegral in the implication (34)--(35);
- claims $\lfloor K\eta\rfloor\ge p+1$ from merely
  $K\eta-p\ge1$ at a noninteger wall;
- applies the dangerous-branch estimate (22) when $R\le0$, or divides by
  $p$ when $p=0$;
- loses the threshold equalities at $K=18\varepsilon^{-2}$ or
  $\varepsilon=1/20736$;
- quotes a thin residual ceiling above $7739670528$, or a global analytic
  ceiling below the unchanged central bound $180000^2$ without a new proof.

None of the primary failures occurs in the corrected clean-room report or
frozen packet, and none of the fallback failures occurs in the incumbent or
isolated $C=18$ referee report.

## Appendix A. Superseded reconstruction of the earlier $C=20$ ledger

The following cross-check was completed before the stronger $C=18$ incumbent
and $C=125/8$ clean-room proof arrived. It is retained only to expose the
dependency structure; it is not the recommended Round 9 constant and does not
control the verdict above.

### A.1 Dangerous branch and exceptional branches

Let $R=p-d_\rho m$. For $R>0$, (14) gives

$$
m<\frac54p,
\qquad
U=\beta+p+m<1+\frac94p.
\tag{21}
$$

This is strict because $\beta<1$ and $d_\rho>4/5$.

- If $p=n>0$, then $m=0$ and $R=p>0$, so (21) and the subsequent local-slope
  proof apply without invoking the first-drop theorem.
- If $p=0$, then $R=-d_\rho m\le0$; no division by $p$ and no local-slope
  estimate is used.
- If $n=0$, Round 3 prescribes $p=m=0$, hence $R=0$ and
  $M=\lfloor K\eta\rfloor$.
- More generally, every $R\le0$ branch is already loss-free. The local shelf
  estimate is needed only for $R>0$.

No branch is silently discarded.

### A.2 Localization at $t>4/5$

Equations (5) and (21) give

$$
\frac U{\rho K}
<
F_C(\varepsilon)
:=
\frac{\varepsilon^2}{C(1-\varepsilon)}
+\frac94\sqrt{
\frac{2\pi\varepsilon}{C(1-\varepsilon)}}.
\tag{22}
$$

Both terms increase with $\varepsilon$, so the worst endpoint is exactly
$\varepsilon=1/100$. At $C=20$,

$$
\frac1{\rho K}\le\frac1{198000},
\tag{23}
$$

and, using $\pi<22/7$,

$$
\frac{2\pi}{\varepsilon\rho K}
\le\frac{11}{3465}
=\frac1{315}
<\frac1{17^2}.
\tag{24}
$$

Therefore

$$
\frac U{\rho K}
<\frac1{198000}+\frac9{68}
=\frac{445517}{3366000}
<\frac15.
\tag{25}
$$

The fraction in the source is correct. Thus

$$
t:=\frac{x_0}{\rho K}>\frac45.
\tag{26}
$$

For reference, preserving the particular split (23)--(24) for general $C$
requires only

$$
C\ge\frac{12716}{693},
\tag{27}
$$

where $\pi<22/7$ supplies strictness. Direct aggregation of (22) would require
an even smaller constant. Hence localization is not the $C=20$ bottleneck.

### A.3 Local slope and shelf quadratic

At $x_0=\rho Kt$, the derivative identity is

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}.
\tag{28}
$$

The integrand is increasing, so (26) and
$1-\rho^2t^2\le2(\varepsilon+U/K)$ give

$$
\sigma(x_0)>
\frac{4\varepsilon}
{5\pi\sqrt{2(\varepsilon+U/K)}}.
\tag{29}
$$

There is no $C$ in (28)--(29). It enters only through
$U/K<(1+9p/4)\varepsilon^2/C$.

For $p>0$, equality of the ordinary floors at the first and last plateau
samples implies, including at integer walls,

$$
A(x_0)-A(x_0+p)<1.
\tag{30}
$$

Combining (29)--(30) gives, at $C=20$,

$$
p^2<\frac{25\pi^2}{8}
\left(
\frac1\varepsilon+\frac1{20}+\frac{9p}{80}
\right)
<\frac{125}{4}
\left(
\frac1\varepsilon+\frac1{20}+\frac{9p}{80}
\right).
\tag{31}
$$

Assume $p\ge29/(5s)$. Since $s\le1/10$, also $p\ge58$. The three terms on
the final right side of (31), divided by $p^2$, are at most

$$
\frac{3125}{3364},
\qquad
\frac{25}{53824},
\qquad
\frac{225}{3712}.
$$

Their exact sum is

$$
\frac{3675}{3712}<1,
$$

which contradicts the strict inequality (31). Hence

$$
p<\frac{29}{5s}.
\tag{32}
$$

For general $C$, the same proof with $\pi^2<10$ is already valid when

$$
C\ge\frac{32875}{1912}.
\tag{33}
$$

The associated quadratic is increasing at and above $29/(5s)$ under (33).
At equality in (33), the strict inequality preceding the quadratic still
excludes equality in (32). Thus neither the quadratic nor its monotonicity is
the $C=20$ bottleneck.

### A.4 Gain, maximal interface loss, and the old architecture's bottleneck

In all branches, $R<29/(5s)$: it follows from (32) when $R>0$, while it is
automatic when $R\le0$. Therefore (2), (4), and
$\lfloor x\rfloor>x-1$ give

$$
M>
\left(\alpha C-\frac{29}{5}\right)\frac1s-1.
\tag{34}
$$

To force the right side of (34) to be at least $B$ at the worst endpoint
$s=1/10$, it is enough and, for these bounds, exact to require

$$
C\ge C_{\rm pay}
=\frac{1}{\alpha}
\left(
\frac{29}{5}+\frac{1+B}{10}
\right)
=\frac{177\pi\sqrt2}{40}+\frac{2\pi}{25}.
\tag{35}
$$

This dominates (27) and (33). For example, $\pi>3$ and
$\sqrt2>7/5$ give $C_{\rm pay}>753/40$, while

$$
\frac{12716}{693}<\frac{753}{40},
\qquad
\frac{32875}{1912}<\frac{753}{40}.
$$

The ledger proves $C_{\rm pay}<20$ without decimal arithmetic. Namely,

$$
\sqrt2>\frac{140}{99},
\qquad
\pi<\frac{22}{7}
$$

imply

$$
20\alpha
=\frac{40\sqrt2}{3\pi}
>\frac{19600}{3267}
>\frac{299}{50},
$$

where the last exact margin is $3167/163350$. Hence

$$
20\alpha-\frac{29}{5}>\frac9{50}.
$$

Using $1/s\ge10$ in (34) gives

$$
M>\frac45.
\tag{36}
$$

Meanwhile $\sqrt2<3/2$ gives

$$
4\delta<B<\frac45.
\tag{37}
$$

The equal rational comparison point $4/5$ is safe because both (36) and (37)
are strict. This is the decisive compensation step, and it is the largest
parameter requirement in the proof.

### A.5 Wall, endpoint, and branch audit

1. **Threshold equality $K=20\varepsilon^{-2}$.** All substitutions of
   $1/K$ are non-strict upper bounds, but (21), (22), (29), (30), (31),
   (34), and (37) retain strictness. Equality in the threshold is included.

2. **Endpoint $\varepsilon=1/100$.** This is the worst endpoint in (22),
   the place where $p\ge29/(5s)$ gives $p\ge58$, and the worst endpoint in
   (34). The exact margins $3675/3712<1$ and (36)--(37) remain strict there.

3. **No drop $p=n$.** For $p>0$, $m=0$ and $R=p>0$. The same-floor relation
   (30), not the first-drop theorem, supplies the local-slope input. If
   $p=n=0$, this is the degenerate-head branch.

4. **Immediate drop $p=0$.** Then $R=-d_\rho m\le0$. The proof never divides
   by $p$ and does not invoke (29)--(32).

5. **Degenerate head $n=0$.** Round 3 sets $p=m=0$; (4) becomes
   $M=\lfloor K\eta\rfloor$. The stronger uniform estimate (34) still
   applies because $R=0<29/(5s)$.

6. **Head-floor wall.** If the initial sampled value is an integer, equality
   of the two ordinary floors can only shorten the plateau. Two real numbers
   in the same ordinary-floor cell differ by strictly less than one, so (30)
   is wall-safe.

7. **Gain wall $K\eta\in\mathbb Z$.** Then
   $\lfloor K\eta\rfloor=K\eta$, and the universal inequality
   $\lfloor x\rfloor>x-1$ used in (34) remains strict.

8. **Interface wall $q=\rho K$.** Then $\beta=0$ and $\delta=0$.
   Equations (21)--(32) remain valid; the interface loss only improves.

9. **High-interface boundary.** Low tails have $x_0<\rho K$; tails beginning
   at or above the interface are covered by the independent convex theorem.
   There is no uncovered equality case.

10. **Spectral and proxy walls.** The final ordinary-floor proxy is a coarse
    upper bound for the strict phase proxy even when the proxy value is an
    integer. No ordinary-floor equality is substituted for the strict
    spectral count.

### A.6 Exact overlap

The independent low aggregate-action theorem includes

$$
K\le\frac1{8\varepsilon^{5/2}},
$$

and the optimized high theorem includes $K\ge20\varepsilon^{-2}$. Their
ranges meet exactly when

$$
20\varepsilon^{-2}
\le\frac1{8\varepsilon^{5/2}}
\iff
160\sqrt\varepsilon\le1
\iff
\boxed{\varepsilon\le\frac1{25600}}.
$$

At $\varepsilon=1/25600$, both thresholds equal

$$
20\cdot25600^2=13107200000<2^{34}.
$$

Both component theorems include their threshold equality, so there is no
open seam. Since $1/25600>2^{-18}$, this is a strict enlargement of the
previous thin endpoint.

### A.7 Historical pre-mortem

Promotion should be rejected if a later manuscript does any of the
following:

- cites $p<8/s$, $p<10/s$, $x_0\ge K/2$, or $t>9/10$ without rederiving it
  under the new hypothesis;
- uses $K\eta>14/s$ at $C=20$ (it is false as a consequence of the stated
  lower bound and is unnecessary);
- applies the dangerous-branch estimate $U<1+9p/4$ to $R\le0$ without first
  splitting branches;
- invokes the local-slope argument at $p=0$;
- replaces the strict same-floor inequality by a non-strict or ordinary-floor
  identity;
- loses strictness at $K\eta\in\mathbb Z$, $q=\rho K$, or
  $K=20\varepsilon^{-2}$;
- rounds $C_{\rm pay}$ numerically instead of using the exact rational
  comparisons above;
- recomputes the overlap as anything other than $1/(64C^2)$, hence
  $1/25600$ for $C=20$;
- imports the old all-$K$ endpoint theorem to prove its own enlarged endpoint.

None of these failures occurs in the audited $C=20$ ledger.
