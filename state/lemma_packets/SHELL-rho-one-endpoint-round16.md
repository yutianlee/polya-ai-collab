# Lemma Packet: Round 16 Thin Endpoint Extension

Parent obligation: `SHELL-rho-one-endpoint`.

The labels `(N1)`--`(N3)`, `(P1)`--`(P9)`, `(H1)`--`(H12)`,
`(S1)`--`(S4)`, and `(C1)`--`(C2)` are packet-local equation labels, not
proof-obligation graph IDs.

Round: 16.

Status: **FROZEN CANDIDATE / UNPROVED**. This is a dependency and
proof-obligation packet, not a proof. No Round 16 target, product estimate,
complementary-action estimate, stretch calculation, or conditional consequence
in this packet is promoted before all review gates pass. The exact permitted
inputs below are the only prior results that may be used.

## 1. Frozen claim -- UNPROVED

For the three-dimensional Dirichlet shell $A_{\rho,1}$, the exact Round 16
target is

$$
\boxed{
\frac78\le\rho<1,
\qquad K\ge0,
}
$$

with

$$
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{1}
$$

Equivalently, set

$$
\rho=1-\varepsilon,
\qquad
a=\varepsilon K.
$$

The frozen target is

$$
\boxed{
0<\varepsilon\le\frac18,
\qquad a\ge0.
}
\tag{2}
$$

At $K=0$, equivalently $a=0$, both sides of (1) are zero. For $K>0$,
the proposed product or phase comparison must be strict before transfer to
(1). None of this paragraph proves (1).

## 2. Frozen two-piece union -- UNPROVED

The proof must be reconstructed on exactly the two inclusive pieces

$$
\boxed{0\le a\le\frac{\pi}{4\varepsilon}}
\tag{3a}
$$

and

$$
\boxed{a\ge\frac{\pi}{4\varepsilon}}.
\tag{3b}
$$

Both pieces must independently own the common optical face

$$
\boxed{a=\frac{\pi}{4\varepsilon}}.
\tag{4}
$$

There is no third piece. In particular, no conclusion, estimate, or
intermediate-range coverage from the Round 6 aggregate theorem may enter this
union.

## 3. Exact permitted-input whitelist

The proof may use only:

1. `CONV-strict-counting` and the exact separated shell spectrum;
2. `SHELL-sturm-liouville-completeness`;
3. the proved radial min--max operator comparison, with its direction
   rechecked in the new product proof;
4. `SHELL-phase-enclosures` together with `SHELL-annulus-phase-transfer`,
   only for the already-proved all-domain strict proxy form encoded in
   (N3); and
5. the domain-free action identities in (N1)--(N2), rederived from the exact
   action below or independently audited before use.

The Round 6 aggregate conclusion, including its

$$
0<\varepsilon\le\frac1{100},
\qquad
\frac{\pi}{4\varepsilon}
\le a\le
\frac1{8\varepsilon^{3/2}},
$$

coverage, is **expressly forbidden** as an input. It may not be extended,
quoted as a bridge, or imported through a later theorem that depended on it.
Only separately identified domain-free identities may be rederived and used.

The old Round 5 product-theorem conclusion and the Round 11 bridge,
all-frequency endpoint, and old $P_{\mathcal A}<I$ conclusions are likewise
**expressly forbidden**: each was proved only on the old
$0<\varepsilon\le1/100$ domain and none may be imported into either Round 16
piece. Only formulas explicitly restated in this packet may be rederived and
independently audited on the new domain. The rejected global semicircle
majorant $\mathcal A\le\mathcal B$ is forbidden and may not be used as a
pointwise comparison.

Define the strict integer bracket by

$$
[u]_<:=\lceil u\rceil-1.
$$

For the high piece, use the exact action and inverse defined in Section 5,
extend $\mathcal A(y)=0$ for $y>a$, and set, for
$\ell\in\mathbb N_0$,

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad
q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_{\ell\ge0}y_\ell q_\ell.
\tag{N1}
$$

For $n\ge1$, put

$$
x_n=n-\frac14,
\qquad
M_\varepsilon(x)
=\#\left\{\ell\in\mathbb N_0:
\varepsilon\left(\ell+\frac12\right)<x\right\}.
$$

The exact strict layer-cake identity and continuous normalization to be
rederived or independently audited are

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{\substack{n\ge1\\x_n<T}}
M_\varepsilon(R(x_n))^2,
\qquad
I:=\frac12\int_0^T F(t)\,dt
=\frac{a^3}{3\pi}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
\tag{N2}
$$

The only permitted phase transfer is

$$
N_D(A_{\rho,1},K^2)
\le\frac{2P_{\mathcal A}}{\varepsilon^2},
\qquad
\frac{2I}{\varepsilon^2}
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{N3}
$$

Thus the high piece must prove $P_{\mathcal A}<I$. Equations
(N1)--(N3) do not grant any domain-sensitive Round 6 conclusion.

## Accepted Round 15 boundary -- context only, not a two-piece input

This section records authoritative prior coverage only for status separation
and a later conditional global integration. **None of it is an input to
either proof piece (3a) or (3b).** Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The accepted all-frequency thin endpoint is exactly
$99/100\le\rho<1$; the accepted small-ratio all-frequency range is
$0<\rho\le\rho_*$. Round 15 also proved, including threshold equality,

$$
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2},
\qquad
\rho=1-\varepsilon.
$$

The sharper accepted thresholds remain authoritative only on their exact
domains:

$$
0<\varepsilon\le\frac18,
\quad K\ge\frac{32}{\varepsilon^2};
\qquad
0<\varepsilon\le\frac1{10},
\quad K\ge\frac{24}{\varepsilon^2};
\qquad
0<\varepsilon\le\frac1{25},
\quad K\ge\frac{20}{\varepsilon^2}.
$$

The accepted central endpoint and all-ratio high-frequency theorem are

$$
K_0(5/6)<295^2=87025,
\qquad
0<\rho<1,\quad K\ge200000.
$$

Set $I_{15}=[\rho_*,99/100]$, and let $\mathcal A_{15}$ be the complete
accepted analytic cover with every owned ratio, energy, and threshold face.
The unresolved set

$$
\mathcal D_{15}
=(I_{15}\times[0,\infty))\setminus\mathcal A_{15}
$$

remains open and nonrectangular; in particular,

$$
\mathcal D_{15}\ne I_{15}\times[0,200000).
$$

## 4. Low product piece -- all new estimates UNPROVED

For the separated product comparison, put

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\},
\qquad
b_n=\sqrt{a^2-n^2\pi^2},
$$

and, for $1\le n\le N$,

$$
M_n=
\left\lceil
\sqrt{\left(\frac{b_n}{\varepsilon}\right)^2+\frac14}
-\frac12
\right\rceil.
$$

The intended exact comparison majorant is

$$
\mathcal P_\varepsilon(a)=\sum_{n=1}^{N}M_n^2.
\tag{P1}
$$

Its min--max direction, multiplicities, and every strict radial and angular
wall must be rederived; (P1) is not a granted Round 16 lemma.

Define

$$
I(a)=\frac{2a^3}{3\pi},
\qquad
S_0(a)=\sum_{n=1}^{N}(a^2-n^2\pi^2),
\qquad
D(a)=I(a)-S_0(a).
\tag{P2}
$$

For $a>\pi$, strict radial counting gives the unique representation

$$
\frac a\pi=N+t,
\qquad
N\ge1,
\qquad
0<t\le1.
\tag{P3}
$$

At $a=m\pi$, the required convention is
$(N,t)=(m-1,1)$, because the radial level on the spectral wall is excluded.
The exact expansion to prove is

$$
\boxed{
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}.
}
\tag{P4}
$$

The new one-piece deficit estimate is the **UNPROVED** target

$$
\boxed{D(a)>\frac25a^2\qquad(a>\pi).}
\tag{P5}
$$

Its exact screen is

$$
\begin{aligned}
\frac{D(a)}{\pi^2}-\frac25\left(\frac a\pi\right)^2
&=
\frac{N^2}{10}
+N\left[\left(t-\frac25\right)^2+\frac1{150}\right]
+\frac{2t^3}{3}-\frac{2t^2}{5} \\
&\ge
\frac{N^2}{10}+\frac{N}{150}-\frac8{375}>0.
\end{aligned}
\tag{P6}
$$

The proof must derive the minimum $-8/375$ on $0<t\le1$ and strict
positivity for every integer $N\ge1$; sampling is inadmissible.

The product algebra must be rederived through the sufficient condition

$$
D(a)
\ge
\varepsilon\left(I(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}.
\tag{P7}
$$

On (3a), for $a\ge\pi$, the proposed uniform cost is

$$
\varepsilon\left(I(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}
\le
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
\tag{P8}
$$

At $\varepsilon=1/8$, the exact screened reserve is

$$
\boxed{
\frac25-
\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
}
\tag{P9}
$$

For $0\le a\le\pi$, the strict radial count must be proved to be exactly
zero, including $a=0$ and the wall $a=\pi$. The low piece is complete
only after the zero range, (P1)--(P9), and the common face (4) all pass.

## 5. High complementary-action piece -- UNPROVED

For $r\in\{\rho,1\}$ and $0\le y\le ar$, set

$$
J_r(y)=
\sqrt{a^2r^2-y^2}
-y\arccos\frac{y}{ar}.
$$

Define the exact action

$$
\mathcal A(y)=
\begin{cases}
\dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
&0\le y\le\rho a,\\[6pt]
\dfrac{J_1(y)}{\pi\varepsilon},
&\rho a\le y\le a.
\end{cases}
\tag{H1}
$$

Let

$$
T=\mathcal A(0)=\frac a\pi,
\qquad
\tau=\mathcal A(\rho a),
$$

let $R:[0,T]\to[0,a]$ be the decreasing inverse of $\mathcal A$, and
put

$$
F=R^2,
\qquad
g=-F'>0
$$

on the appropriate open intervals. The curvature and endpoint audit must
prove

$$
g\text{ decreases on }(0,\tau),
\qquad
g\text{ increases on }(\tau,T),
\tag{H2}
$$

and

$$
F(0)=a^2,
\qquad
F(\tau)=\rho^2a^2,
\qquad
F(T)=0,
\qquad
g(T)=2\pi\rho a.
\tag{H3}
$$

Use the shifted radial count

$$
C(t)=\#\{n\ge1:n-1/4<t\},
\qquad
w(t)=t-C(t),
\qquad
W(t)=\int_0^t w(s)\,ds.
$$

Writing $\Psi(t)=W(t)-t/4$, the exact one-period calculation to audit is

$$
W(t)\ge0,
\qquad
-\frac1{32}\le\Psi(t)\le\frac3{32}.
\tag{H4}
$$

The Stieltjes proof must split at the actual, ungridded $\tau$, without
assuming $\tau>1$. With

$$
D_{\rm rad}
:=\int_0^T F(t)\,dt
-\sum_{\substack{n\ge1\\n-1/4<T}}F(n-1/4),
$$

the required radial screen is

$$
\boxed{
D_{\rm rad}
\ge
\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
}
\tag{H5}
$$

The exact half-integer count in (N2) has the closed form

$$
M_\varepsilon(x)
=\max\left\{0,
\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil
\right\}.
\tag{H6}
$$

If

$$
J_{\rm rad}=\#\{n\ge1:n-1/4<T\},
$$

then strict counting must give

$$
J_{\rm rad}<T+\frac14=\frac a\pi+\frac14.
\tag{H7}
$$

The complete angular error must be bounded strictly by

$$
\boxed{
E=
\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
}
\tag{H8}
$$

On the high piece (3b), the proposed uniform screens are

$$
\frac{D_{\rm rad}}{a^2}
\ge
\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
\ge
\frac{(1-\varepsilon)(1-5\varepsilon)}{4},
\tag{H9}
$$

and, with the common-face equality convention preserved,

$$
\boxed{
\frac{E}{a^2}
\le
\frac\varepsilon\pi
+\frac{\varepsilon^2}{\pi}
+\frac{\varepsilon^3}{\pi^2}
+\frac{\varepsilon^4}{\pi^2}.
}
\tag{H10}
$$

The sign in (H10) is deliberately non-strict: equality in this scaling
step occurs at $a=\pi/(4\varepsilon)$. At $\varepsilon=1/8$, the strict
bound $\pi>3$ is intended to give

$$
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
$$

and hence the exact screened reserve

$$
\boxed{
\frac{21}{256}-\frac{193}{4096}
=\frac{143}{4096}>0.
}
\tag{H11}
$$

The proof must establish that the lower side of (H9) decreases and the
upper side of (H10) increases on $0<\varepsilon\le1/8$. It must then
derive, rather than assume,

$$
\varepsilon^2
\sum_{\substack{n\ge1\\n-1/4<T}}
M_\varepsilon(R(n-1/4))^2
<
\sum_{\substack{n\ge1\\n-1/4<T}}F(n-1/4)+E
<
\int_0^T F(t)\,dt.
\tag{H12}
$$

Together with (N1)--(N3), (H12) is intended to prove the high piece. The
endpoint reserve alone is not a proof.

## 6. Six mandatory dependency replacements

Every proof and review must explicitly execute all six replacements:

1. Remove every use of $\tau>1$ and every special first-cell argument;
   use the globally valid $W\ge0$ Stieltjes split at the actual $\tau$.
2. Remove $a\ge125$ and every shortcut such as a radial count below
   $a/2$; use the exact strict bound
   $J_{\rm rad}<a/\pi+1/4$.
3. Replace $\rho\ge99/100$ by the exact
   $\rho=1-\varepsilon$ lower bound in (H9).
4. Replace the old $61/1400$ power reserve by the exact screened reserve
   $143/4096$ in (H11).
5. Replace the old Round 5 three-slab estimate by the exact zero-count
   range and the uniform deficit $D>(2/5)a^2$.
6. Do not extend or invoke the Round 6 aggregate theorem; the two pieces
   (3a)--(3b) are the proposed complete union.

Any additional hidden use of
$\varepsilon\le1/100$, $\rho\ge99/100$, $a\ge125$, or the old bridge
scale must be listed and rederived.

## 7. Stretch arithmetic -- planning only, not claims

The primary lower face remains exactly $\rho=7/8$. The following values
are navigation screens only and are **UNPROVED / NOT PROMOTABLE IN ROUND
16**.

At

$$
\rho=\frac67,
\qquad
\varepsilon=\frac17,
$$

the coarse screens give

$$
\frac{1723}{8820}
\quad\text{(product)},
\qquad
\frac{139}{21609}
\quad\text{(complementary action)}.
\tag{S1}
$$

At

$$
\rho=\frac{23}{27},
\qquad
\varepsilon=\frac4{27},
$$

using the screened rational bound $\pi>333/106$, they give

$$
\frac{12719}{65610}
\quad\text{(product)},
\qquad
\frac{162570113}{235723844196}
\quad\text{(complementary action)}.
\tag{S2}
$$

Neither positive calculation proves a stretch endpoint.

The first tested obstruction in this selected coarse bridge screen is

$$
\rho=\frac{17}{20},
\qquad
\varepsilon=\frac3{20},
\qquad
-\frac{44729}{20535000}<0.
\tag{S3}
$$

At $\varepsilon=1/6$, the corresponding screened value is

$$
-\frac{3983743}{143712144}<0.
\tag{S4}
$$

Equations (S3)--(S4) obstruct only this selected coarse route. They are not
spectral counterexamples, endpoint impossibility results, or evidence that
(1) fails.

## 8. Conditional global consequence -- unavailable before promotion

For this conditional integration only, retain the accepted definitions and
boundary recorded above. The already accepted all-frequency range
$0<\rho\le\rho_*$ is not an
input to the new endpoint proof; it is used only after that proof passes,
when assembling a conditional global consequence.

Only if the target (1)--(2), both inclusive pieces, and their common face
are independently proved and promoted may the remaining coarse envelope be
reduced to

1. $[\rho_*,1/16]$: $K<64$;
2. $[1/16,5/6]$: $K<K_0(5/6)<295^2$;
3. $[5/6,7/8]$: $K<54/(1-\rho)^2\le3456$; and
4. $[7/8,1)$: all frequencies proved.

Only after a separate conditional-envelope audit would the prospective
theorem be

$$
\boxed{
0<\rho<1,
\qquad
K\ge295^2=87025.
}
\tag{C1}
$$

The exact prospective reduction factor from the accepted Round 15 ceiling
would be

$$
\boxed{
\frac{200000}{295^2}
=\frac{8000}{3481}>2.
}
\tag{C2}
$$

Equations (C1)--(C2) are **CONDITIONAL AND UNAVAILABLE** until promotion.
They do not state or imply that any new Round 16 theorem has been proved.
The bounded residual below the analytic cover would remain open, so
`SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` would
remain open and `COMP-certified-bessel` would remain `diagnostic_only`.

## 9. Mandatory branches, walls, and faces

Every proof, reconstruction, ledger, and review must explicitly own:

- $K=0$ and $K>0$, equivalently $a=0$ and $a>0$;
- the exact zero-count range $0\le a\le\pi$;
- every radial wall $a=m\pi$, with the excluded-threshold convention
  $(N,t)=(m-1,1)$, both one-sided limits, and continuity of (P4);
- every product angular wall
  $b_n^2/\varepsilon^2=\ell(\ell+1)$;
- the first positive radial and angular branches;
- the optical face $a=\pi/(4\varepsilon)$ from both pieces;
- the corner $(\varepsilon,a)=(1/8,2\pi)$, where the common face is also
  a radial wall and $(N,t)=(1,1)$;
- the lower ratio face $\rho=7/8$, the closed
  $\varepsilon=1/8$ face, and the open limit $\rho\uparrow1$ without
  treating $\varepsilon=0$ as part of the domain;
- the test faces $\varepsilon=1/100,1/25,1/10,1/8$;
- the action radial wall $n-1/4=T$, with that layer excluded;
- every half-integer angular wall
  $R(n-1/4)/\varepsilon=m+1/2$;
- every phase-proxy wall
  $\mathcal A(y_\ell)+1/4\in\mathbb Z$, using the strict bracket in (N1);
- the outer cutoff $y=a$, the inner interface $y=\rho a$, and the
  actual ungridded curvature interface $t=\tau$;
- $\tau$ on, below, and above a sawtooth grid point, and both sides of
  every sawtooth jump;
- the improper $t=0$ trace, the terminal $t=T$ trace, and every dropped
  nonnegative Stieltjes term;
- the exact domain of $R$, all denominators, square roots, arccosine
  arguments, squarings, and improper endpoint limits;
- the monotonic reductions in (P8), (H9), and (H10), including the
  non-strict equality in (H10) at the common face;
- the conditional interfaces
  $\rho=\rho_*,1/16,5/6,7/8,99/100$; and
- $K=64,3456,295^2,200000,K_0(5/6)$, and every sharper threshold face
  used in the accepted or conditional union.

## 10. Role-independent required outputs

Every assigned proof or review role must return a self-contained artifact
containing, as applicable:

1. `PASS` or `FAIL`, with the first unsupported implication identified
   before secondary observations;
2. an exact dependency ledger separating the five permitted inputs from
   every domain-sensitive estimate, and certifying that no Round 6
   aggregate conclusion entered;
3. a complete low-piece proof or falsification covering the zero range,
   (P1)--(P9), every strict wall, and the common face;
4. a complete high-piece proof or falsification covering (N1)--(N3),
   (H1)--(H12), the ungridded curvature switch, the improper trace, every
   strict wall, and the common face;
5. a closed-union audit showing that the two independently closed pieces,
   and only those pieces, cover every $a\ge0$ for
   $0<\varepsilon\le1/8$;
6. an exact rational or symbolic ledger reproducing at least (P4), the
   minimum and $N=1$ positivity in (P6), $577/2880$, $21/256$,
   $193/4096$, $143/4096$, (S1)--(S4), and $8000/3481>2$;
7. a branch/wall/face ledger covering every item in Section 9;
8. the strongest exact domain actually proved if any step fails, without
   silently moving the target face; and
9. a separate conditional-envelope audit before using (C1)--(C2).

Sampled numerics, decimal sign checks, bounded certification, or agreement
between agents do not replace any analytic implication or exact ledger.
An isolated reconstruction must be completed before cross-comparison with
an incumbent proof.

## 11. Promotion gates

Promote the Round 16 endpoint only if all of the following pass:

1. this packet is byte-frozen and externally hashed before proof work;
2. the dependency audit distinguishes domain-free identities from every
   estimate that used $\varepsilon\le1/100$;
3. the product proof closes on (3a), including the exact zero range and
   common face;
4. the complementary-action proof closes on (3b), including the actual
   curvature interface, improper trace, and common face;
5. all six replacements are explicit and no Round 6 aggregate result
   enters the proof;
6. every strict wall, branch, denominator, radicand, inverse,
   monotonicity, and shared face is owned;
7. a strictly isolated reconstruction passes before cross-review;
8. a fresh adversarial audit finds no unsupported implication;
9. an independently executed exact ledger reproduces every required
   comparison;
10. the two-piece union proves all $a\ge0$ at the closed face
    $\varepsilon=1/8$;
11. the conditional-envelope audit uses accepted Round 15 theorems only on
    their exact domains and proves the $K=295^2$ equality face; and
12. any accepted state patch is applied exactly once.

## 12. Explicit do-not-claim rules

- Do not call (1)--(2) proved until every promotion gate passes.
- Do not move the primary lower face below $\rho=7/8$ in Round 16.
- Do not promote either positive stretch screen (S1)--(S2).
- Do not call either negative screen (S3)--(S4) a counterexample or an
  impossibility theorem.
- Do not extend, invoke, or conceal the Round 6 aggregate theorem as a
  bridge.
- Do not infer a theorem from the two endpoint reserves without proving the
  complete product and complementary-action paths.
- Do not claim the global ceiling $295^2$ until the endpoint, common-face
  union, and conditional envelope audit are independently accepted.
- Do not replace the true residual by a rectangular sweep.
- Do not treat bounded certification, sampled numerics, or agent consensus
  as proof.
- Do not close `SHELL-rho-compact`, `SHELL-rho-uniformity`, or
  `TARGET-shell-d3`, and do not promote `COMP-certified-bessel` beyond
  `diagnostic_only`, while the true compact residual remains open.
