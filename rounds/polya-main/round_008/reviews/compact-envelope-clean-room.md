# Clean-room review: compact-ratio analytic envelope

## Verdict

**PASS.** The three analytic zones cover the whole interval

$$
I_*=[\rho_*,1-2^{-18}],
$$

all constants and monotonicity directions in the frozen packet are correct,
and the global threshold

$$
K_{\mathrm{hi}}=2^{42}
$$

is valid with equality included. In particular, the thin-shell identity
$L(2^{-18})=U(2^{-18})=2^{42}$ is exact; it is not a rounded numerical
coincidence.

This reconstruction used only the frozen compact packet and the proved
packets it cites: the small-hole endpoint and low-interface result, the exact
thin-width zero count, the fixed-$\rho$ high-energy result, and the Round
5--6 thin-shell packets. No incumbent Round 8 proof, root scan, or numerical
quadrature was used.

## 1. Ordering of the switch points

The elementary estimates requested in the packet give

$$
\begin{aligned}
\omega_0-\frac1{16}
&=\frac{\sqrt3}{2\pi}-\frac16-\frac1{16}\\
&>\frac{5}{3}\frac7{44}-\frac16-\frac1{16}
=\frac{19}{528}>0.
\end{aligned}
\tag{1}
$$

Thus $1/16<\omega_0$. Also $\rho_*>0$ and $\rho_*<1/16$.
For the latter, using $\sqrt3<2$, $\pi>3$, and $\sqrt2>1$,

$$
16\omega_0
=\frac{8\sqrt3}{\pi}-\frac83
<\frac83
<\frac{46}{15}
<2+\frac{16\sqrt2}{15}
=1+2C_*.
\tag{2}
$$

Finally $2^{-18}<1/100$, so

$$
\frac{99}{100}<1-2^{-18}.
$$

Consequently the inclusive zones

$$
[\rho_*,1/16],\qquad[1/16,99/100],\qquad
[99/100,1-2^{-18}]
$$

cover $I_*$, with no sliver at either rational switch.

## 2. Zone L

If $K\le 1/(2\rho)$, then $\rho K\le1/2$, and every shifted-tail
start $r+1/2$ is at or above the inner interface. Equality is allowed by
the proved high-angular theorem. If

$$
K\ge H_0(\rho)=\frac{C_*}{\omega_0-\rho},
$$

the proved small-hole low-interface theorem applies because
$\rho\le1/16<\omega_0$. Its threshold also includes equality.

The two thresholds have the claimed order. Since all denominators are
positive,

$$
H_0(\rho)\ge\frac1{2\rho}
\quad\Longleftrightarrow\quad
2C_*\rho\ge\omega_0-\rho
\quad\Longleftrightarrow\quad
\rho\ge\frac{\omega_0}{1+2C_*}=\rho_*.
\tag{3}
$$

At $\rho=\rho_*$, equality holds and

$$
\omega_0-\rho_*=2C_*\rho_*,
\qquad
H_0(\rho_*)=\frac1{2\rho_*}.
\tag{4}
$$

Thus the endpoint has no frequency gap.

The remaining constant estimates are exact:

$$
C_*<\frac12+\frac{8(3/2)}{15}=\frac{13}{10},
$$

and (1) implies

$$
H_0(1/16)
<\frac{13/10}{19/528}
=\frac{3432}{95}<64.
\tag{5}
$$

Moreover

$$
H_0'(\rho)=\frac{C_*}{(\omega_0-\rho)^2}>0,
$$

so every point in the Zone L closed residual envelope has $K<64$.

## 3. Zone C and monotonicity of $K_0$

The exact thin-width theorem covers

$$
K\le\frac{\pi}{1-\rho};
$$

at equality the phase can equal $\pi$, but strict spectral counting excludes
that first level. The fixed-$\rho$ theorem covers $K\ge K_0(\rho)$,
including equality. Hence the displayed $\mathcal R_C$ is a valid closed
envelope of the possible gap.

Differentiate $G_1$ directly:

$$
G_1'(z)=-\frac{\arccos z}{\pi}<0
\qquad(0\le z<1).
\tag{6}
$$

It follows that

$$
a_\rho=\frac{2\pi\rho}{1-\rho}
$$

is strictly increasing while
$\eta_\rho=G_1(\max\{\rho,1/2\})$ is positive and nonincreasing. There is
no discontinuity at $\rho=1/2$.

For a direct check of the root monotonicity, let $y=\sqrt{K_0}$ and

$$
F(y,a,\eta)=\eta y^2-\sqrt a\,y-C_0=0.
$$

At the positive root,

$$
F_y=2\eta y-\sqrt a=\sqrt{a+4\eta C_0}>0,
$$

and therefore

$$
\frac{\partial y}{\partial a}
=\frac{y}{2\sqrt a\,F_y}>0,
\qquad
\frac{\partial y}{\partial\eta}
=-\frac{y^2}{F_y}<0.
\tag{7}
$$

Thus increasing $a_\rho$ and nonincreasing $\eta_\rho$ both increase $y$;
$K_0(\rho)=y^2$ is strictly increasing on the central interval.

It remains to check the endpoint bound without decimals. From (6) and
$G_1(1)=0$,

$$
G_1(1-\varepsilon)
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv.
$$

Since $\cos x\ge1-x^2/2$, one has
$\arccos(1-v)\ge\sqrt{2v}$, whence

$$
\eta_{99/100}
\ge\frac{2\sqrt2}{3\pi}\left(\frac1{100}\right)^{3/2}
>\frac1{6000}.
\tag{8}
$$

The last strict inequality is equivalent to $4\sqrt2>\pi$, which follows
from $\sqrt2>1$ and $\pi<4$. Also

$$
a_{99/100}=198\pi<792,
\qquad
C_0<1+\frac{8(3/2)}{15}=\frac95,
$$

and $0<\eta_{99/100}<G_1(0)=1/\pi<1$. Consequently

$$
a+4\eta C_0<792+\frac{36}{5}<900.
$$

Both square roots in the numerator defining $y$ are therefore less than
$30$, while $2\eta>1/3000$. Hence

$$
y<180000,
\qquad
K_0(99/100)<180000^2
=32{,}400{,}000{,}000
<2^{35}.
\tag{9}
$$

Monotonicity now puts all of $\mathcal R_C$ below $2^{35}$.

## 4. Zone T and the exact joining equality

For $\varepsilon\in[2^{-18},1/100]$, the cited thin estimates include both
endpoint directions:

$$
0\le K\le L(\varepsilon),
\qquad
K\ge U(\varepsilon).
$$

Their relative order is transparent from

$$
\frac{L(\varepsilon)}{U(\varepsilon)}
=\frac{1}{512\sqrt\varepsilon}\le1,
\tag{10}
$$

because $\sqrt\varepsilon\ge2^{-9}=1/512$. Equality occurs only at
$\varepsilon=2^{-18}$. At that endpoint,

$$
\begin{aligned}
L(2^{-18})
&=\frac1{2^3(2^{-18})^{5/2}}
=\frac1{2^3 2^{-45}}=2^{42},\\
U(2^{-18})
&=\frac{2^6}{(2^{-18})^2}
=\frac{2^6}{2^{-36}}=2^{42}.
\end{aligned}
\tag{11}
$$

Both component theorems include their endpoints, so the low and high ranges
touch and cover every $K$ on this face. There is no one-point spectral gap
at $K=2^{42}$.

Finally $U(\varepsilon)=64\varepsilon^{-2}$ is decreasing in
$\varepsilon$, and hence

$$
U(\varepsilon)\le U(2^{-18})=2^{42}.
\tag{12}
$$

The inequality is strict when $\varepsilon>2^{-18}$; at equality the cited
high-frequency theorem and the endpoint theorem both include
$K=2^{42}$.

## 5. Global threshold and wall audit

Let $\rho\in I_*$ and $K\ge2^{42}$.

- In Zone L, (5) gives $K>H_0(\rho)$.
- In Zone C, (9) and monotonicity give $K>K_0(\rho)$.
- In Zone T, (12) gives $K\ge U(\varepsilon)$, including the unique equality
  case $\varepsilon=2^{-18}$ and $K=2^{42}$.

Thus the shell Polya inequality holds throughout the stated global
high-energy region.

All requested equality conventions are consistent:

- $\rho=\rho_*$ is analytic and (4) has exact equality;
- $\rho=1-2^{-18}$ is analytic and (11) has exact equality;
- $K=1/(2\rho)$, $K=H_0(\rho)$, and $K=K_0(\rho)$ are included by the
  corresponding proved inputs;
- $(1-\rho)K=\pi$ has zero count because the spectral convention is strict;
- $K=L(\varepsilon)$ and $K=U(\varepsilon)$ are included;
- $\rho=1/16$ and $\rho=99/100$ belong to both neighboring zones;
- $\rho=1/2$ causes only the continuous switch in the definition of
  $\eta_\rho$.

For a fixed $\rho$, checking immediately to the right of each spectral jump
is also the correct orientation: the strict counting function jumps only
after the eigenfrequency, while the Weyl right-hand side is increasing
between jumps. The packet correctly refuses to use this one-dimensional
observation on a two-parameter box until all moving walls have been enclosed.

## 6. Non-blocking precision note on the word "residual"

The displayed sets $\mathcal R_L$, $\mathcal R_C$, and $\mathcal R_T$ use
closed inequalities. They are therefore **closed certificate envelopes**,
not literally the set of points still lacking an analytic proof. For
example, $\mathcal R_L$ contains the single closed-envelope point

$$
(\rho,K)=(\rho_*,1/(2\rho_*)),
$$

and $\mathcal R_T$ contains

$$
(\varepsilon,K)=(2^{-18},2^{42}),
$$

although both are already analytic. Likewise, each frequency-threshold
face included with equality is already discharged. This causes no error in
the covering argument or in the high-energy theorem: every genuinely
unresolved point lies in the displayed union. The certificate driver should
nevertheless mark these analytic faces as masks (especially the two endpoint
ratio faces), in accordance with the packet's instruction that they not be
sent for numerical certification. With that interpretation, there is no
logical conflict and no uncovered boundary sliver.

## Conclusion

No arithmetic, monotonicity, coverage, or equality error was found. The
analytic reduction to a bounded union of three closed envelopes and the
uniform implication for $K\ge2^{42}$ are ready for promotion as a separate
lemma. This review does not promote SHELL-rho-compact: certification of the
bounded envelopes remains a separate obligation.

## Post-audit correction

**PASS.** The corrected certificate section agrees with
certificate-cover-design.md and resolves the precision note in Section 6.
It now distinguishes the true target

$$
\mathcal D=(I_*\times[0,\infty))\setminus\mathcal A
$$

from the closed planning envelope $\mathcal E$, with
$\mathcal D\subseteq\mathcal E$, and assigns
$\mathcal E\setminus\mathcal D$ to analytic masks or explicit face owners.
Thus the endpoint and threshold faces are no longer implicitly numerical
obligations.

The monotone-box alternative is valid. For
$\rho_-\le\rho\le\rho_+$, domain inclusion gives
$A_{\rho,1}\subseteq A_{\rho_-,1}$, so Dirichlet domain monotonicity and
$K\le K_+$ imply

$$
N_D(A_{\rho,1},K^2)
\le\#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}=C_B.
$$

The non-strict corner count safely includes an eigenvalue on the upper
frequency face. Since $1-\rho^3$ decreases with $\rho$ and $K^3$ increases
with $K$, the Weyl term is bounded below by $W_B$ at
$(\rho_+,K_-)$. Hence $C_B\le W_B$ certifies the entire closed box and
legitimately absorbs its internal spectral, angular, and proxy walls without
literal wall-by-wall subdivision.

Finally, the exact manifest requirement matches the design: exact endpoints
and inclusivity, analytic masks, face ownership, backend and precision,
proved angular/radial truncation, certified count and Weyl bounds, and raw
artifact hashes are all required. The checker condition

$$
\mathcal E\setminus
(\mathcal A\cup\text{certified boxes})=\varnothing
$$

is sufficient because every point of $\mathcal D$ already lies in
$\mathcal E$. Requiring exact endpoint set arithmetic and independent hash
and inequality recomputation excludes sampled-grid coverage. No new
arithmetic or logical defect was found.
