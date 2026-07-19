# Round 8 adversarial review: compact envelope and certificate domain

Role: adversarial reconstruction of constants, endpoints, coverage, and
certificate walls.

I treated `state/lemma_packets/SHELL-rho-compact.md` as a claim to falsify.
The numerical values below are diagnostics only; every verdict is supported
by the exact inequalities displayed here.

## Verdict

- **Analytic envelope (9)--(16): PASS.** The zone decomposition covers the
  whole compact ratio interval, all claimed inequalities are correct, all
  analytic thresholds include equality, and

  $$
  \rho\in[\rho_*,1-2^{-18}],\qquad K\ge2^{42}
  $$

  is indeed completely analytic.
- **Frozen certificate domain and specification: FAIL as written.** The
  displayed union
  $\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T$ is a closed *over-cover* of
  the unproved points, not the exact unproved set. It contains endpoint and
  switch-face points already covered by permitted analytic theorems. The
  packet first says that the endpoint faces must not be sent to a numerical
  certificate, but its promotion rule later requires every point of that
  same closed union to have a reproducible certificate. Those instructions
  are incompatible literally. The seven certificate bullets are also local
  conditions only: they do not certify that the boxes cover the target set,
  and they do not provide exact angular/radial truncation or event counts.

Thus there is **no unsupported mathematical step in (9)--(16)**. The first
unsupported step is the later identification of (17), without subtracting
all analytically covered points, as the domain that must be certified point
by point.

## 1. Ordering of the switch points

Put

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,\qquad
C_*=\frac12+\frac{8\sqrt2}{15},\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The ordering needed by the three zones is strict:

$$
0<\rho_*<\frac1{16}<\frac{99}{100}<1-2^{-18}<1.
\tag{A}
$$

Indeed, the lower estimate in Section 2 below gives
$\omega_0>1/16>0$. Also $C_*>1/2$, while
$\sqrt3<7/4$ and $\pi>3$ give

$$
\omega_0<\frac{7}{24}-\frac16=\frac18.
$$

Consequently

$$
0<\rho_*<\frac{\omega_0}{2}<\frac1{16}.
$$

The middle comparison is elementary, and
$2^{-18}=1/262144<1/100$ proves the last nontrivial comparison in (A).
There is therefore no reversed or empty ratio zone hidden in the packet.

For reference only,

$$
\omega_0=0.108997781044229\ldots,\quad
C_*=1.25424723326565\ldots,\quad
\rho_*=0.0310668242700667\ldots.
$$

## 2. Zone L constants and endpoints

The quoted elementary estimates give

$$
\frac{\sqrt3}{2\pi}>
\frac{5/3}{2(22/7)}=\frac{35}{132}.
$$

Hence

$$
\omega_0-\frac1{16}
>\frac{35}{132}-\frac16-\frac1{16}
=\frac{140-121}{528}
=\frac{19}{528}>0.
\tag{B}
$$

Similarly, $\sqrt2<3/2$ gives

$$
C_*<\frac12+\frac45=\frac{13}{10}.
\tag{C}
$$

Since $H_0(\rho)=C_*/(\omega_0-\rho)$ is strictly increasing on this
zone, (B)--(C) imply

$$
H_0(1/16)
<\frac{13/10}{19/528}
=\frac{3432}{95}<64.
\tag{D}
$$

The exact actual value is $26.97434598\ldots$, but it is not used.

The two analytic frequency ranges meet at $\rho_*$ because

$$
\omega_0-\rho_*
=\omega_0\frac{2C_*}{1+2C_*}
=2C_*\rho_*,
$$

so

$$
H_0(\rho_*)=\frac1{2\rho_*}
=16.0943389531\ldots.
\tag{E}
$$

More generally,

$$
H_0(\rho)\ge\frac1{2\rho}
\quad\Longleftrightarrow\quad
\rho(1+2C_*)\ge\omega_0
\quad\Longleftrightarrow\quad
\rho\ge\rho_*.
\tag{F}
$$

Thus no gap is reversed. The high-angular theorem includes
$K=1/(2\rho)$, the low-interface theorem includes $K=H_0(\rho)$, and
at $\rho=\rho_*$ the already-proved endpoint theorem includes every
$K$. The closed set $\mathcal R_L$ therefore contains all possibly
unproved Zone-L points, but its two frequency faces and its singleton at
$\rho=\rho_*$ are already analytic.

## 3. Zone C monotonicity and constants

Write

$$
a(\rho)=\frac{2\pi\rho}{1-\rho},\qquad
\eta(\rho)=G_1(\max\{\rho,1/2\}),\qquad
C_0=1+\frac{8\sqrt2}{15}.
$$

Then $a$ is strictly increasing. Since

$$
G_1'(z)=-\frac{\arccos z}{\pi}<0\qquad(0\le z<1),
$$

$\eta$ is constant on $(0,1/2]$ and strictly decreasing on $[1/2,1)$;
in particular it is nonincreasing across the join.

Let $y=\sqrt{K_0}$ be the positive root of

$$
F(y;a,\eta)=\eta y^2-\sqrt a\,y-C_0=0.
$$

At that root,

$$
\partial_yF=2\eta y-\sqrt a
=\sqrt{a+4\eta C_0}>0.
$$

Implicit differentiation therefore gives

$$
\frac{\partial y}{\partial a}
=\frac{y}{2\sqrt a(2\eta y-\sqrt a)}>0,
\qquad
\frac{\partial y}{\partial\eta}
=-\frac{y^2}{2\eta y-\sqrt a}<0.
$$

Increasing $a$ and decreasing $\eta$ both increase $y$, so $K_0(\rho)$
is increasing on the whole central interval, including across $\rho=1/2$.

At $\rho=99/100$,

$$
a=198\pi<792.
\tag{G}
$$

Also

$$
G_1(z)=\frac1\pi\int_z^1\arccos t\,dt.
$$

The inequality $\cos u\ge1-u^2/2$ yields
$\arccos t\ge\sqrt{2(1-t)}$, and hence

$$
G_1(z)\ge
\frac{2\sqrt2}{3\pi}(1-z)^{3/2}.
$$

At $z=99/100$, using $4\sqrt2>\pi$,

$$
\eta(99/100)
\ge\frac{2\sqrt2}{3000\pi}
>\frac1{6000}.
\tag{H}
$$

Moreover $0<\eta<1$ and, by $\sqrt2<3/2$,

$$
C_0<1+\frac45=\frac95.
\tag{I}
$$

Equations (G)--(I) give

$$
\sqrt a<30,\qquad
\sqrt{a+4\eta C_0}
<\sqrt{792+\frac{36}{5}}<30,\qquad
2\eta>\frac1{3000}.
$$

Therefore

$$
\sqrt{K_0(99/100)}<180000,
$$

and

$$
K_0(99/100)<180000^2
=32{,}400{,}000{,}000
<34{,}359{,}738{,}368=2^{35}.
\tag{J}
$$

The actual value $K_0(99/100)=6.8997472349\ldots\times10^9$ is only a
diagnostic. The zero-count theorem includes
$K=\pi/(1-\rho)$ and the fixed-ratio theorem includes $K=K_0(\rho)$.
Thus $\mathcal R_C$ is again a safe closed over-cover of the open frequency
gap, with no endpoint convention lost.

## 4. Zone T constants and endpoints

For $\varepsilon\in[2^{-18},1/100]$,

$$
L(\varepsilon)=\frac1{8\varepsilon^{5/2}},
\qquad
U(\varepsilon)=\frac{64}{\varepsilon^2}.
$$

The order of the two thresholds is exact:

$$
L(\varepsilon)\le U(\varepsilon)
\quad\Longleftrightarrow\quad
1\le512\sqrt\varepsilon
\quad\Longleftrightarrow\quad
\varepsilon\ge2^{-18}.
\tag{K}
$$

At the lower endpoint,

$$
L(2^{-18})
=\frac1{8\,2^{-45}}=2^{42},
\qquad
U(2^{-18})=64\,2^{36}=2^{42}.
\tag{L}
$$

Also

$$
U(\varepsilon)\le U(2^{-18})=2^{42}.
\tag{M}
$$

Both thin theorems include their threshold equalities. At
$\varepsilon=2^{-18}$ their ranges meet, and the already-proved endpoint
theorem independently covers every $K$. Thus there is no thin sliver, but
$\mathcal R_T$ still contains the analytically solved singleton
$(2^{-18},2^{42})$.

At the rational switch $\rho=99/100$, hence $\varepsilon=1/100$,

$$
L=12500,\qquad U=640000,
$$

with both endpoints included analytically.

## 5. Global high-energy coverage

The ratio zones

$$
[\rho_*,1/16],\qquad[1/16,99/100],\qquad
[99/100,1-2^{-18}]
$$

cover $I_*$ and overlap at both rational switch points. In Zone L, (D)
makes every $K\ge2^{42}$ low-interface analytic. In Zone C, monotonicity and
(J) make it fixed-ratio analytic. In Zone T, (M) makes it high-thin
analytic. Every comparison is strict before the final weak threshold, so
$K=2^{42}$ is included. This proves (16) exactly.

There is likewise no uncovered point at $\rho=1/16$ or $\rho=99/100$:
each switch belongs to both neighboring closed envelopes. The two outer
ratio endpoints are fully analytic. Therefore

$$
\{
\text{points not covered by any permitted analytic theorem}
\}
\subseteq
\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T.
\tag{N}
$$

This is the correct coverage statement. Equality in (N) is false.

For example, at $\rho=99/100$, $K=1000$ lies on the central envelope:
$100\pi<400<1000$, while $K_0(99/100)>1000$ follows already from
$\eta<1/3$, $a>594$, and
$\sqrt{K_0}>\sqrt a/\eta>72$. But the thin theorem proves this point because
$1000<12500=L(1/100)$. At the two outer endpoints the discrepancy is even
more explicit: $\mathcal R_L$ contains the singleton from (E), and
$\mathcal R_T$ contains the singleton from (L), although the endpoint
theorems prove all frequencies there.

## 6. First unsupported step and corrected domain

The packet's sentence that (17) is the "sharper residual" is valid only if
"residual" means a convenient closed enclosure. It becomes false as an
exact certificate target when combined with the promotion rule requiring
every point of (17) to be numerically certified.

The corrected target is

$$
\boxed{
\mathcal D=
(\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T)
\setminus\mathcal A,
}
\tag{O}
$$

where $\mathcal A$ is the union of **all** points covered by the permitted
analytic inputs: both endpoint theorems, the high-angular range, the
small-hole low-interface range, the zero-count range, the fixed-ratio
high-energy range, and both thin ranges. In particular, threshold equality
faces belong to $\mathcal A$.

$\mathcal D$ need not itself be closed. A finite interval proof may cover
its closure by closed rational boxes, but every face must carry an explicit
owner:

- an analytic theorem and exact threshold comparison; or
- a computational certificate chunk.

The faces at $\rho=\rho_*$ and $\rho=1-2^{-18}$ must be assigned to the
endpoint theorems. At $\rho=1/16$ and $\rho=99/100$, all analytic inputs from
both adjacent zones must be intersected before declaring the remaining
face computational. This removes the contradiction and does not create an
open sliver.

## 7. Certificate requirements are necessary but not sufficient

The seven frozen wall conditions are sound necessary safeguards. In
particular, the strict angular cutoff, strict eigenvalue faces, outward
rounding, phase/determinant isolation, floor walls, Weyl-margin walls, and
shared faces may not be dropped. For fixed $\rho$, checking immediately to
the right of each spectral jump is valid because the count is constant
between jumps while the Weyl term is increasing in $K$.

They do not yet constitute a reproducible certificate for $\mathcal D$.
The certificate format must additionally include:

1. an exact cover manifest with rational box coordinates and a proof that
   their union covers $\mathcal D$;
2. exact ownership for every outer, switch, and shared face, including
   interval enclosures of the curved functions $H_0$, $K_0$, $L$, and $U$;
3. for every box, exact angular and radial truncation bounds, the number of
   determinant/phase events, and an exact multiplicity sum;
4. branch-wall events such as $\rho K=\ell+1/2$ whenever the piecewise action
   or ordinary-floor proxy is used;
5. a checker that verifies global coverage and face ownership, not only the
   local interval inequalities; and
6. hashes of the input manifest, certificate chunks, checker version, and
   exact constants, so the reported computation can be reproduced.

A list of individually valid boxes without items 1--3 can leave an
unnoticed hole or omit angular/radial channels and therefore does not prove
the theorem.

## 8. Severe feasibility obstruction hidden by boundedness

"Bounded" is not remotely the same as "enumerable" here. On the exact
thin-zone slice

$$
\varepsilon=2^{-17},
$$

which lies strictly inside the permitted interval, the frozen residual
envelope is

$$
L=2^{39}\sqrt2,\qquad U=2^{40}.
$$

Its $K$-width is

$$
U-L=2^{39}(2-\sqrt2).
$$

Since $\sqrt2<10/7$,

$$
U-L>\frac47\,2^{39}
=\frac87\,2^{38}>2^{38}+1.
\tag{P}
$$

Half-integer angular walls have unit spacing. Hence this single horizontal
slice crosses strictly more than $2^{38}$ distinct walls
$K=\ell+1/2$. A literal box split at every angular wall already requires
more than $274$ billion wall events before a single determinant zero,
phase-integer wall, or Weyl-margin wall is processed. Near
$\varepsilon=2^{-18}$ the absolute frequencies approach $2^{42}$ even
though the relative width collapses.

This is a severe feasibility blocker for direct root-by-root or
wall-by-wall certification, not a flaw in the analytic bound (16). Closing
`SHELL-rho-compact` will require a further analytic/aggregate reduction or
a certificate format that proves large families of walls symbolically.
A conventional interval scan of (17), even on the sharper zone-wise union,
is not a credible next step.

## Final promotion recommendation

Promote only the **analytic compact-envelope reduction** and the uniform
high-energy statement (16). Do not promote `SHELL-rho-compact` or treat
`COMP-certified-bessel` as advanced by boundedness alone. Before any pilot
certificate is judged relevant to the final gap, replace (17) by (O), add
the exact global manifest and checker obligations above, and show how the
$>2^{38}$ angular-wall family is aggregated rather than enumerated.

## Post-correction re-audit

I re-read the revised certificate section of
state/lemma_packets/SHELL-rho-compact.md and the companion design
rounds/polya-main/round_008/exploration/certificate-cover-design.md.

### Corrected verdict

**PASS.** The revision repairs the frozen certificate-domain and
specification failure identified above. This post-correction verdict
supersedes the earlier **FAIL as written** for the certificate language; the
earlier **PASS** for the analytic envelope is unchanged. It does not certify
the residual domain or promote SHELL-rho-compact.

The repaired set logic is exact. With

$$
\mathcal P=I_*\times[0,\infty),\qquad
\mathcal D=\mathcal P\setminus\mathcal A,\qquad
\mathcal D\subseteq\mathcal E\subseteq\mathcal P,
$$

one has

$$
\mathcal E\setminus\mathcal A=\mathcal D.
$$

Consequently the checker condition

$$
\mathcal E\setminus
\bigl(\mathcal A\cup\text{certified boxes}\bigr)=\varnothing
$$

is equivalent to requiring the certified boxes to cover every point of
$\mathcal D$. It does not require numerical certification of
$\mathcal E\setminus\mathcal D$. The endpoint and threshold faces are now
explicit analytic masks or face owners, and each rational switch face must
have one declared owner. This removes the former contradiction at
$\rho=\rho_*$, $\rho=1/16$, $\rho=99/100$, and
$\rho=1-2^{-18}$.

The revised wall rule is also safe. It permits either exact subdivision or a
proved one-sided monotone majorant. For

$$
B=[\rho_-,\rho_+]\times[K_-,K_+],
$$

domain inclusion and monotonicity give

$$
N_D(A_{\rho,1},K^2)
\le
\#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}=C_B.
$$

The use of $\le K_+^2$ in this corner count is deliberately non-strict, so
an eigenvalue on the upper face is overcounted safely. Simultaneously,

$$
\frac{2}{9\pi}(1-\rho^3)K^3
\ge
\frac{2}{9\pi}(1-\rho_+^3)K_-^3=W_B.
$$

Thus $C_B\le W_B$ proves the whole closed box, including every internal
determinant, phase-integer, angular, ordinary-floor, and strict spectral
wall. No constancy of the count inside the box is assumed.

In particular, the corrected language **does not demand literal
subdivision at the more than $2^{38}$ half-integer angular walls** on the
$\varepsilon=2^{-17}$ slice. Packet item 3 expressly allows the monotone
alternative; equations (19)--(20) state it; the falsification list rejects
literal subdivision when that alternative is used; and the cover-design
document identifies monotone majorization as essential in the
high-frequency region.

The manifest now contains the missing global and reproducibility data:
exact endpoints and inclusivity, analytic masks, face owners, arithmetic
backend and version, precision, angular and radial truncation proofs,
certified count and Weyl bounds, raw-artifact hashes, and an independent
exact cover check. The design also rejects a scan that merely stops and
requires every included or excluded radial index to have a rigorous
root/phase justification.

One feasibility warning remains, correctly acknowledged by the revised
documents. A monotone corner estimate avoids parameter-wall subdivision but
may still be far too coarse or expensive at frequencies near $2^{42}$; it
does not by itself aggregate the corner spectrum. The full compact theorem
therefore still needs a scalable analytic or symbolic count majorant. That
is an open implementation/research obligation, not a defect in the
corrected certificate specification.
