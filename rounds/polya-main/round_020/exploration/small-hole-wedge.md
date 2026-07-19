# Round 20 Small-Hole Wedge Exploration

Date: 2026-07-14.

Status: **PASS for the assigned wedge; exploratory analytic note only; not
frozen, independently reviewed, judged, or promoted**.

This note treats the prospective post-Round-19 component

$$
\mathcal D_{19}^{\rm sh}
=\left\{(\rho,K):
\rho_*<\rho\leq\frac1{\sqrt{337}},
\quad \frac1{2\rho}<K<U(\rho)\right\}.
\tag{1}
$$

The route below closes all of (1).  It does not use a new Bessel-zero
bound.  Instead, it returns to the promoted multiplicity-to-shifted-tail
scaffold and keeps the integer gain
$\lfloor\omega _0K\rfloor-n$ exactly.  In this small-hole range that gain
is always at least one, while the only interface remainder is strictly
less than $1/4$.

No frozen Round 19 artifact or state file is changed by this note.

## 1. Scoped inputs

The following bytes were read as inputs.

| artifact | SHA-256 | use |
|---|---|---|
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` | exact residual and the active $U$ branch |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` | audited split and pre-threshold master inequality |
| `rounds/polya-main/round_003/judge/judge-003.md` | `33e292530e644896b00470a92848f2763c3c337c874a32c0f7bb79aac3b7aca9` | promoted tail scaffold and high-tail theorem |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | strict phase majorant |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | exact separated spectrum and strict counting |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | convex floor theorem and turning bound |
| `rounds/polya-main/round_009/reviews/thin-plateau-parametric-dependency-audit.md` | `9ea72dddc15a15bae41ecb59416e316a29d6e8d85aeae3c6af20b6c6fd8080a2` | internal audit of $\pi<355/113$ |

The already audited rational enclosure

$$
\frac{333}{106}<\pi<\frac{355}{113}
\tag{2}
$$

is used only for exact elementary comparisons.  The theorem statement of
`SHELL-low-interface-small-hole` is **not** extrapolated below its published
threshold $K\geq H_0(\rho)$.  Only its fully derived master inequality,
before that final sufficient threshold is imposed, is reconstructed below.

## 2. Constants and the stronger local statement

Put

$$
\omega _0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
d=\frac{\sqrt{337}}2,
\qquad
\sigma=\frac{3\omega _0}{4},
\tag{3}
$$

and let

$$
\mu=\rho K,
\qquad
A_{\rho,K}(z)=G_K(z)-G_\mu(z).
\tag{4}
$$

The actual tail lemma proved here is stronger than what is needed for
(1):

$$
\boxed{
0<\rho\leq\sigma,\quad K>d,\quad \rho K>\frac12
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.}
\tag{5}
$$

Here $A_{\rho,1}=\{x\in\mathbb R^3:\rho<|x|<1\}$ is the shell;
the reuse of the letter $A$ in (4) follows the promoted action notation.

The exact constant comparisons needed for (5) are narrow but elementary.
First,

$$
\sqrt3>\frac{265}{153},
\qquad
\sqrt{337}>\frac{257}{14},
\tag{6}
$$

because the positive square margins are respectively

$$
3\cdot153^2-265^2=2,
\qquad
337\cdot14^2-257^2=3.
$$

Together with the upper bound in (2), this gives

$$
\omega _0>
\frac{265/153}{2(355/113)}-\frac16
=\frac{1184}{10863}.
\tag{7}
$$

Consequently

$$
\boxed{
\omega _0d
>\frac{1184}{10863}\frac{257}{28}
=\frac{76072}{76041}>1.}
\tag{8}
$$

For the geometry of the split, it is enough to note that
$\rho\leq\sigma<1/2$.  An exact bound is obtained from
$\sqrt3<26/15$ and the lower bound in (2):

$$
\omega _0<
\frac{26/15}{2(333/106)}-\frac16
=\frac{1091}{9990}<\frac19,
\qquad
\sigma<\frac1{12}.
\tag{9}
$$

The square margin for $\sqrt3<26/15$ is
$26^2-3\cdot15^2=1$.

## 3. Reconstructed low-interface master inequality

For an integer $r\geq0$, set

$$
x_0=r+\frac12,
\qquad
\mathcal T_r=
\left\lfloor A_{\rho,K}(x_0)+\frac14\right\rfloor
+2\sum_{j\geq1}
\left\lfloor A_{\rho,K}(x_0+j)+\frac14\right\rfloor.
\tag{10}
$$

Suppose that this is a low-interface tail, so $x_0<\mu$.  Define

$$
n_r=\lfloor\mu-x_0\rfloor,
\qquad
q_r=x_0+n_r,
\qquad
B=\lceil K-x_0\rceil.
\tag{11}
$$

Then

$$
q_r\leq\mu<q_r+1.
\tag{12}
$$

Because $\rho<1/2$, one has $q_r\leq\mu<K/2$.  Thus the point
$K/2-x_0$ lies in the convex right block $[n_r,B]$.  Splitting the
trapezoidal floor sum at $n_r$, using concavity of $A_{\rho,K}$ on the
head, and applying the audited improved convex theorem to the translated
$G_K$ tail gives

$$
\frac{\mathcal T_r}{2}
\leq
\int_{x_0}^{K}A_{\rho,K}(z)\,dz
+\delta_r
-\frac{\lfloor\omega _0K\rfloor-n_r}{4},
\tag{13}
$$

where the exact interface mismatch is

$$
\delta_r=\int_{q_r}^{\mu}G_\mu(z)\,dz.
\tag{14}
$$

When $n_r=0$, the concave block is absent; (13) follows directly from
the convex block, exactly as in the audited packet.  No degenerate
trapezoidal interval is invoked.

The turning estimate recorded from Lemma 6.2 of the scoped annulus source
is

$$
G_\mu(z)<\frac{(\mu-z)^{3/2}}{3\sqrt\mu}
\qquad(0<z<\mu).
\tag{15}
$$

Since $q_r\geq1/2$, $\mu-q_r<1$, and $\mu>1/2$, integration gives

$$
0\leq\delta_r
\leq\frac{2}{15\sqrt\mu}(\mu-q_r)^{5/2}
<\frac{2\sqrt2}{15}<\frac14.
\tag{16}
$$

The final comparison in (16) is exact: $8\sqrt2<15$ follows by positive
squaring from $128<225$.

## 4. Exact integer-gain lemma

Let

$$
\alpha=\omega _0K,
\qquad
\beta=\rho K=\mu,
\qquad
m=\left\lfloor\beta-\frac12\right\rfloor.
\tag{17}
$$

Under the hypotheses of (5), (8) gives $\alpha>1$, while
$\rho\leq3\omega _0/4$ gives

$$
\beta\leq\frac34\alpha.
\tag{18}
$$

Because $\beta>1/2$, one has $m\geq0$.  If $m=0$, then
$\lfloor\alpha\rfloor\geq1=m+1$.  If $m\geq1$, then
$\beta\geq m+1/2$, and hence

$$
\alpha\geq\frac43\beta
\geq\frac{4m+2}{3}
=m+1+\frac{m-1}{3}
\geq m+1.
\tag{19}
$$

Therefore

$$
\boxed{\lfloor\omega _0K\rfloor\geq m+1.}
\tag{20}
$$

For any low-interface start $x_0=r+1/2$,

$$
n_r=\lfloor\beta-r-1/2\rfloor\leq m,
$$

so (20) yields the uniform exact gain

$$
\boxed{\lfloor\omega _0K\rfloor-n_r\geq1.}
\tag{21}
$$

Substitution of (16) and (21) into (13) proves, strictly,

$$
\boxed{
\mathcal T_r
<2\int_{r+1/2}^{K}A_{\rho,K}(z)\,dz}
\tag{22}
$$

for every low-interface tail.  Every tail starting at or above $\mu$ is
already controlled by the promoted high-angular shifted-tail theorem.

Because $\mu>1/2$, the $r=0$ tail is a low-interface tail, so at least one
of the inequalities summed in the multiplicity-to-tail decomposition is
strict.  With

$$
a_\ell=\left\lfloor
A_{\rho,K}(\ell+1/2)+\frac14\right\rfloor,
$$

the promoted identity and step-function comparison therefore give

$$
\begin{aligned}
\sum_{\ell\geq0}(2\ell+1)a_\ell
&=\sum_{r\geq0}\mathcal T_r\\
&<2\int_0^K f_3(z)A_{\rho,K}(z)\,dz\\
&\leq\int_0^K2zA_{\rho,K}(z)\,dz\\
&=\frac{2}{9\pi}(1-\rho^3)K^3.
\end{aligned}
\tag{23}
$$

The exact spectral bridge and phase enclosure place the strict spectral
count below this ordinary-floor proxy, including at every integer phase
wall.  This proves (5).

## 5. Application to the assigned wedge

Write

$$
\rho_0=\frac1{\sqrt{337}},
\qquad
L(\rho)=\frac1{2\rho}.
\tag{24}
$$

Equation (8) implies

$$
\omega _0\sqrt{337}>2,
\qquad
\sigma=\frac{3\omega _0}{4}
>\frac{3}{2\sqrt{337}}>\rho_0.
\tag{25}
$$

If $\rho_*<\rho\leq\rho_0$ and $K>L(\rho)$, then

$$
K>L(\rho)\geq L(\rho_0)=d,
\qquad
\rho K>\frac12,
\qquad
\rho<\sigma.
\tag{26}
$$

Thus every point in (1) satisfies the hypotheses of (5), and

$$
\boxed{
(\rho,K)\in\mathcal D_{19}^{\rm sh}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.}
\tag{27}
$$

For completeness, the inherited upper face really is the $H_0$ face on
this whole component.  Indeed,

$$
\rho_0<\frac1{18}<\frac{9407}{100000}<\rho_{HK},
$$

so the frozen branch rule gives

$$
U(\rho)=H_0(\rho)
\qquad(\rho_*<\rho\leq\rho_0).
\tag{28}
$$

The proof of (27) does not need the numerical size of $H_0$; (28) is
recorded only to authenticate the residual and its upper-face ownership.

## 6. Bonus face-connected continuation

The ratio $\rho_0$ is not the true wall of this argument.  From (5),

$$
\boxed{
\rho_0\leq\rho\leq\sigma,\quad d<K
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.}
\tag{29}
$$

Here $\rho K>1/2$ follows from $\rho\geq\rho_0$ and $K>d$; at the corner
$(\rho_0,d)$ equality holds, which is why (29) keeps the strict face
$K>d$.

Consequently, if the frozen Round 19 candidate is later independently
approved and promoted through its included $K=d$ face, then its lower
staircase and (29) would make every frequency complete on the larger ratio
interval

$$
0<\rho\leq\sigma=\frac{3\omega _0}{4}.
\tag{30}
$$

Statement (30) is a prospective union only.  This exploratory note does
not itself promote either ingredient.

## 7. Sharp wall of this one-unit-gain route

The constant $\sigma=3\omega _0/4$ is sharp for the ratio-only floor lemma
(20).  If $\rho>\sigma$, then the interval

$$
\max\left\{\frac{3}{2\rho},\frac1{\omega _0}\right\}
<K<\frac2{\omega _0}
\tag{31}
$$

is nonempty.  On it, $\mu>3/2$ while
$\lfloor\omega _0K\rfloor=1$.  Hence $n_0\geq1$ and the integer gain in
(13) is nonpositive; it is zero whenever $\mu<5/2$.

There is an exact point inside the next prospective residual where this
failure is visible:

$$
\rho=\frac1{12},
\qquad
K=\frac{181}{10}.
\tag{32}
$$

The upper bound in (9) gives

$$
\frac1{12}-\sigma
>\frac1{12}-\frac{1091}{13320}
=\frac{19}{13320}>0.
\tag{33}
$$

Also $1/12<9407/100000<\rho_{HK}$ and

$$
K^2-d^2=\frac{6084}{25}>0.
$$

At this ratio $U=H_0$.  The denominator is positive because (7) gives
$\omega _0-1/12>1115/43452>0$, and $K<U$ follows exactly from
$\sqrt2>7/5$, hence $C_*>187/150$, together with (9):

$$
C_*-\frac{181}{10}\left(\omega _0-\frac1{12}\right)
>
\frac{187}{150}
-\frac{181}{10}\frac{517}{19980}
=\frac{155507}{199800}>0.
\tag{34}
$$

Finally, (7) and (9) give

$$
1<\frac{107152}{54315}
<\omega _0K
<\frac{197471}{99900}<2,
\tag{35}
$$

whereas

$$
\mu=\rho K=\frac{181}{120},
\qquad
n_0=\left\lfloor\mu-\frac12\right\rfloor=1,
\qquad
\mu-\frac32=\frac1{120}>0.
\tag{36}
$$

Thus $\lfloor\omega _0K\rfloor-n_0=0$, while
$\delta_0=\int_{3/2}^{181/120}G_\mu(z)\,dz>0$.  The master inequality
(13) then has no discrete term available to pay this positive remainder.
This is the first exact obstruction to extending the **same uniform
one-unit-gain proof** past $\sigma$.  It is not a counterexample to the
shell Polya inequality, nor does it prove that a sharper shifted-tail
analysis fails.

## 8. Face ownership and verdict

- $\rho=\rho_*$ remains the inherited complete small-hole face and is not
  claimed in (1).
- $\rho=1/\sqrt{337}$ is included in (1).  There $L=d$, and the claimed
  fiber begins strictly above $d$.
- $K=L(\rho)$ remains inherited covered and is excluded from (1).
- $K=U(\rho)=H_0(\rho)$ remains inherited covered and is excluded from
  (1), although the tail estimate itself overlaps that face.
- Equality at $\rho=\sigma$ is allowed in the stronger lemma (5); the
  integer proof (19) remains valid at equality.
- Every phase, floor, and split equality is handled by the strict spectral
  count and by the lower-count side of the floor ledger.

**Verdict: PASS.**  The assigned small-hole wedge (1) is completely closed
by the exact shifted-tail argument.  The first unsupported implication of
this route occurs only beyond the larger face $\rho=3\omega _0/4$, as
exhibited by (32)--(36).  Independent reconstruction, constant audit, and
adversarial review are still required before any freeze or promotion.
