# Next Round Prompts

Generated after Round 15 in run `polya-main`.

## Accepted boundary after Round 15

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

For the three-dimensional Dirichlet shell $A_{\rho,1}$, the target Pólya
bound is

$$
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{1}
$$

The complete all-frequency theorem is accepted on

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1.
\tag{2}
$$

Round 15 proved, including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2},
}
\qquad \rho=1-\varepsilon.
\tag{3}
$$

The following sharper accepted thresholds remain authoritative on their
exact domains:

$$
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2},
\tag{4}
$$

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2},
\tag{5}
$$

and

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
\tag{6}
$$

Use the sharpest accepted theorem on every overlap. No threshold in
(3)--(6) may be extrapolated outside its proved $\varepsilon$ domain.

The accepted central endpoint and Round 15 seam are

$$
\boxed{K_0(5/6)<295^2=87025},
\qquad
\boxed{\rho_s=\frac56}.
\tag{7}
$$

The accepted analytic envelope has seven finite residual zones:

1. $[\rho_*,1/16]$: every possible residual has $K<64$;
2. $[1/16,5/6]$: every possible residual has
   $K<K_0(\rho)\le K_0(5/6)<87025$;
3. $[5/6,7/8]$: every possible residual has
   $K<54/(1-\rho)^2\le3456$;
4. $[7/8,9/10]$: every possible residual has
   $K<32/(1-\rho)^2\le3200$;
5. $[9/10,19/20]$: every possible residual has
   $K<24/(1-\rho)^2\le9600$;
6. $[19/20,24/25]$: every possible residual has
   $K<24/(1-\rho)^2\le15000$;
7. $[24/25,99/100]$: every possible residual has
   $K<20/(1-\rho)^2\le200000$.

Together with the all-frequency endpoint $[99/100,1)$, these zones prove
the accepted all-ratio high-frequency theorem

$$
\boxed{
0<\rho<1,
\qquad
K\ge200000.
}
\tag{8}
$$

The complete all-frequency thin endpoint nevertheless remains exactly
$[99/100,1)$. Round 15 did not enlarge it.

## Exact current residual

Set

$$
I_{15}=[\rho_*,99/100]
$$

and let $\mathcal A_{15}$ denote the complete accepted analytic cover,
including every owned ratio, energy, and spectral threshold face. The true
unresolved compact set is

$$
\boxed{
\mathcal D_{15}
=(I_{15}\times[0,\infty))\setminus\mathcal A_{15}.
}
\tag{9}
$$

It is nonrectangular. In particular,

$$
\mathcal D_{15}\ne I_{15}\times[0,200000).
$$

The seven zones are coarse enclosures of the complement of the analytic
cover, not a license to certify a rectangular sweep. Any bounded
certification remains secondary and must target face-connected cells of
$\mathcal D_{15}$ itself.

## Round 16 primary theorem -- explicitly unproved

Freeze the following exact target and no stronger endpoint:

$$
\boxed{
\frac78\le\rho<1,
\qquad
K\ge0.
}
\tag{10}
$$

Equivalently, with

$$
\rho=1-\varepsilon,
\qquad
a=\varepsilon K,
$$

the target is (1) for

$$
\boxed{
0<\varepsilon\le\frac18,
\qquad
a\ge0.
}
\tag{11}
$$

For $K>0$ the desired comparison is strict at the phase/product level; at
$K=0$ both sides of (1) are zero. Equations (10)--(11) are **UNPROVED
ROUND 16 TARGETS**. Nothing in this file promotes them.

The proof is to be rebuilt as the two-piece closed union

$$
\boxed{
0\le a\le\frac{\pi}{4\varepsilon}
}
\tag{12a}
$$

and

$$
\boxed{
a\ge\frac{\pi}{4\varepsilon}.
}
\tag{12b}
$$

Both pieces must own the common optical face

$$
a=\frac{\pi}{4\varepsilon}.
\tag{13}
$$

There is no third piece. In particular, the Round 6 aggregate theorem is
not a dependency of the proposed Round 16 proof and must not be extended
past its accepted domain. Only the exact inputs whitelisted below may be
used; the old $\varepsilon\le1/100$ conclusion does not prove the new slab.

## Exact permitted inputs and normalization

The frozen packet must permit only:

1. `CONV-strict-counting` and the exact separated shell spectrum;
2. `SHELL-sturm-liouville-completeness`;
3. the proved radial min--max operator comparison, with its direction
   rechecked in the new product proof;
4. `SHELL-phase-enclosures` only in the already-proved all-domain form
   displayed below; and
5. the domain-free action identities displayed below, rederived from (21)
   or independently audited before use.

Define the strict integer bracket by

$$
[u]_<:=\lceil u\rceil-1,
$$

For the high piece, use $\mathcal A,R,F,T$ from (21)--(22), extend
$\mathcal A(y)=0$ for $y>a$, and set

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad
q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_{\ell\ge0}y_\ell q_\ell.
\tag{N1}
$$

For

$$
x_n=n-\frac14,
\qquad
M_\varepsilon(x)
=\#\left\{\ell\ge0:
\varepsilon\left(\ell+\frac12\right)<x\right\},
$$

the exact strict layer-cake identity and continuous normalization are

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{x_n<T}M_\varepsilon(R(x_n))^2,
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

Thus the high piece must prove $P_{\mathcal A}<I$. No estimate, domain
conclusion, or intermediate-range coverage from the Round 6 aggregate
theorem may be imported.

## Low piece: exact product screen

For the separated product comparison, put

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\},
\qquad
b_n=\sqrt{a^2-n^2\pi^2},
$$

and

$$
M_n=
\left\lceil
\sqrt{\left(\frac{b_n}{\varepsilon}\right)^2+\frac14}
-\frac12
\right\rceil.
$$

The exact comparison majorant is

$$
\mathcal P_\varepsilon(a)=\sum_{n=1}^{N}M_n^2.
$$

Define

$$
I(a)=\frac{2a^3}{3\pi},
\qquad
S_0(a)=\sum_{n=1}^{N}(a^2-n^2\pi^2),
\qquad
D(a)=I(a)-S_0(a).
$$

For $a>\pi$, strict radial counting gives the unique representation

$$
\frac a\pi=N+t,
\qquad
N\ge1,
\qquad
0<t\le1.
\tag{14}
$$

At $a=m\pi$, the convention is $(N,t)=(m-1,1)$, because the radial level
on the spectral wall is excluded. Exact expansion gives

$$
\boxed{
\frac{D(a)}{\pi^2}
=\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}.
}
\tag{15}
$$

The new one-piece deficit estimate to prove is

$$
\boxed{D(a)>\frac25a^2\qquad(a>\pi).}
\tag{16}
$$

The exact screen is

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
\tag{17}
$$

The proof must justify the minimum $-8/375$ on $0<t\le1$ and the final
strict positivity for every integer $N\ge1$; a sampled check is not enough.

The accepted product algebra reduces the comparison to the sufficient
condition

$$
D(a)
\ge
\varepsilon\left(I(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}.
\tag{18}
$$

On (12a), using $a\ge\pi$ and $\pi>3$, the proposed uniform cost is

$$
\varepsilon\left(I(a)+\frac{a^2}{4}\right)
+\frac{\varepsilon^2a}{\pi}
\le
\left(\frac16+\frac\varepsilon4+\frac{\varepsilon^2}{9}\right)a^2.
\tag{19}
$$

At the worst ratio face $\varepsilon=1/8$, the exact reserve is

$$
\boxed{
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
}
\tag{20}
$$

For $0\le a\le\pi$, the strict radial count is exactly zero; this includes
$a=0$ and the wall $a=\pi$. Thus the old three-slab Round 5 constants are
to be replaced by the exact zero range plus (16)--(20).

Equations (15)--(20) are planning screens, not accepted lemmas. The proof
must rederive the comparison direction, the angular ceiling, every radial
and angular wall, the strictness of the upper majorant, and the common face
(13).

## High piece: complementary-action screen

For $r\in\{\rho,1\}$ and $0\le y\le ar$, set

$$
J_r(y)=
\sqrt{a^2r^2-y^2}
-y\arccos\frac{y}{ar},
$$

and define the exact action

$$
\mathcal A(y)=
\begin{cases}
\dfrac{J_1(y)-J_\rho(y)}{\pi\varepsilon},
&0\le y\le\rho a,\\[6pt]
\dfrac{J_1(y)}{\pi\varepsilon},
&\rho a\le y\le a.
\end{cases}
\tag{21}
$$

Let

$$
T=\mathcal A(0)=\frac a\pi,
\qquad
\tau=\mathcal A(\rho a),
$$

let $R$ be the decreasing inverse of $\mathcal A$, and put

$$
F=R^2,
\qquad
g=-F'>0.
$$

The required curvature audit must prove that $g$ decreases on
$(0,\tau)$, increases on $(\tau,T)$, and satisfies

$$
F(0)=a^2,
\qquad
F(\tau)=\rho^2a^2,
\qquad
F(T)=0,
\qquad
g(T)=2\pi\rho a.
\tag{22}
$$

Use the shifted radial count

$$
C(t)=\#\{n\ge1:n-1/4<t\},
\qquad
w(t)=t-C(t),
\qquad
W(t)=\int_0^t w(s)\,ds.
$$

Writing $\Psi(t)=W(t)-t/4$, exact one-period calculation gives

$$
W(t)\ge0,
\qquad
-\frac1{32}\le\Psi(t)\le\frac3{32}.
\tag{23}
$$

The proof must split at the actual, ungridded value $\tau$. It must not
assume $\tau>1$. With

$$
D_{\rm rad}
:=\int_0^T F(t)\,dt
-\sum_{n-1/4<T}F(n-1/4),
$$

the $W\ge0$ Stieltjes route is intended to give

$$
\boxed{
D_{\rm rad}
\ge
\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
}
\tag{24}
$$

For the exact half-integer angular ceiling, the count in (N2) has the
closed form

$$
M_\varepsilon(x)
=\max\left\{0,\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil\right\}.
$$

If

$$
J_{\rm rad}=\#\{n\ge1:n-1/4<T\},
$$

then strict counting gives

$$
J_{\rm rad}<T+\frac14=\frac a\pi+\frac14.
\tag{25}
$$

The complete angular error is therefore bounded strictly by

$$
\boxed{
E=
\left(\frac a\pi+\frac14\right)
\left(\varepsilon a+\frac{\varepsilon^2}{4}\right).
}
\tag{26}
$$

On the high piece (12b), (24) is screened by

$$
\frac{D_{\rm rad}}{a^2}
\ge
\frac{\rho^2}{4}-\frac{\pi\rho}{4a}
\ge
\frac{(1-\varepsilon)(1-5\varepsilon)}{4},
\tag{27}
$$

while (26) gives

$$
\frac{E}{a^2}
\le
\frac\varepsilon\pi
+\frac{\varepsilon^2}{\pi}
+\frac{\varepsilon^3}{\pi^2}
+\frac{\varepsilon^4}{\pi^2}.
\tag{28}
$$

At $\varepsilon=1/8$, using only $\pi>3$,

$$
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
$$

and hence the exact normalized reserve is

$$
\boxed{
\frac{21}{256}-\frac{193}{4096}
=\frac{143}{4096}>0.
}
\tag{29}
$$

The proof must justify that the lower side of (27) decreases and the upper
side of (28) increases on $0<\varepsilon\le1/8$, so that the closed ratio
face really is the worst case. It must then derive the strict layer-cake
comparison

$$
\varepsilon^2
\sum_{n-1/4<T}M_\varepsilon(R(n-1/4))^2
<
\sum_{n-1/4<T}F(n-1/4)+E
<
\int_0^T F(t)\,dt,
\tag{30}
$$

and perform the permitted strict phase transfer to (1).

Equations (21)--(30) are planning screens. Reproducing only the endpoint
reserve (29) is not a proof of the high piece.

## Mandatory replacement audit

The Round 16 proof must explicitly locate and replace every place where the
older endpoint architecture used $\varepsilon\le1/100$. At minimum the
audit must record all six replacements below.

1. Remove any use of $\tau>1$ or a special first-cell argument; use the
   globally valid $W\ge0$ Stieltjes split at the actual $\tau$.
2. Remove $a\ge125$ and any shortcut such as a radial count below $a/2$;
   use the exact strict bound $J_{\rm rad}<a/\pi+1/4$.
3. Replace the endpoint substitution $\rho\ge99/100$ by the
   $\rho=1-\varepsilon$ lower bound in (27).
4. Replace the old $61/1400$ power reserve by the exact $143/4096$ reserve
   in (29).
5. Replace the old Round 5 three-slab estimate by the exact zero-count
   range and the uniform deficit $D>(2/5)a^2$.
6. Do not extend or invoke the Round 6 aggregate theorem; the two pieces
   (12a)--(12b) already form the proposed complete union.

Any additional hidden use of $\varepsilon\le1/100$, $\rho\ge99/100$,
$a\ge125$, or the old bridge scale must also be listed and rederived.

## Stretch screens -- navigation only

The primary target is frozen at the exact lower face $\rho=7/8$. The
following arithmetic is retained only to guide a later round; it is not
part of the Round 16 claim and must not be promoted during this round.

At

$$
\rho=\frac67,
\qquad
\varepsilon=\frac17,
$$

the same coarse screens report the exact positive reserves

$$
\frac{1723}{8820}
\qquad\text{(product)},
\qquad
\frac{139}{21609}
\qquad\text{(complementary action)}.
\tag{31}
$$

At

$$
\rho=\frac{23}{27},
\qquad
\varepsilon=\frac4{27},
$$

using the screened rational bound $\pi>333/106$, the reported reserves are

$$
\frac{12719}{65610}
\qquad\text{(product)},
\qquad
\frac{162570113}{235723844196}
\qquad\text{(complementary action)}.
\tag{32}
$$

These positive calculations do not prove either stretch endpoint. They
have not passed a frozen-packet proof, isolated reconstruction, or
adversarial dependency audit.

The first tested obstruction in this selected bridge screen occurs at

$$
\rho=\frac{17}{20},
\qquad
\varepsilon=\frac3{20},
\qquad
\text{bridge screen}=-\frac{44729}{20535000}<0.
\tag{33}
$$

At $\varepsilon=1/6$, the corresponding screened value is

$$
-\frac{3983743}{143712144}<0.
\tag{34}
$$

Equations (33)--(34) are obstructions to this selected coarse route only.
They are neither spectral counterexamples nor proofs that the endpoint
cannot extend farther. Do not infer failure of (1) from either number.

## Conditional consequence -- do not promote in advance

Only if (10) is independently proved and the closed union passes every
promotion gate, all finite residual zones strictly beyond $\rho=7/8$
disappear. The remaining coarse envelope would be:

1. $[\rho_*,1/16]$: $K<64$;
2. $[1/16,5/6]$: $K<K_0(5/6)<295^2$;
3. $[5/6,7/8]$: $K<54/(1-\rho)^2\le3456$;
4. $[7/8,1)$: all frequencies proved.

The central endpoint would then dominate, yielding the prospective theorem

$$
\boxed{
0<\rho<1,
\qquad
K\ge295^2=87025.
}
\tag{35}
$$

Relative to the accepted Round 15 ceiling, the exact prospective reduction
factor is

$$
\boxed{
\frac{200000}{295^2}
=\frac{8000}{3481}>2.
}
\tag{36}
$$

Equations (35)--(36) are conditional integration consequences, not Round
16 inputs. The bounded residual below the analytic cover would remain
open, so `SHELL-rho-compact`, `SHELL-rho-uniformity`, and
`TARGET-shell-d3` would remain open and `COMP-certified-bessel` would
remain `diagnostic_only`.

## For A1: obligation architect and lead synthesis

Freeze one Round 16 lemma packet before proof work. It must contain:

- the exact theorem (10)--(11), including $K=0$ and the closed face
  $\rho=7/8$;
- the two inclusive optical pieces (12a)--(12b), with both owning (13);
- the exact permitted-input whitelist and normalizations (N1)--(N3), with
  every domain-sensitive Round 6 conclusion excluded;
- the exact product definitions and screens (14)--(20);
- the exact action, sawtooth, radial-deficit, angular-error, and reserve
  screens (21)--(30);
- the six mandatory dependency replacements;
- the accepted Round 15 boundary (2)--(9), clearly separated from the new
  target;
- the stretch values (31)--(34), each labeled planning-only or route
  obstruction as appropriate;
- the conditional consequences (35)--(36), labeled unavailable until
  promotion;
- every branch, strict wall, shared face, monotonicity claim, denominator,
  radicand, inverse, and improper endpoint needed by either piece.

Build a proof-obligation graph with separate nodes for the product piece,
the complementary-action piece, their closed union, and the conditional
envelope integration. The union node may depend only on two independently
closed piece nodes and the face audit. Do not include the Round 6 aggregate
theorem in this dependency chain.

Inventory every older proof line that used $\varepsilon\le1/100$ or an
equivalent consequence. Mark domain-free symbolic identities separately
from domain-sensitive estimates. One lead agent must reconcile the
incumbent and isolated proofs; agent agreement is not mathematical
verification.

## For A2: incumbent analytic proof developer

Prove or falsify the exact two-piece target. For the low piece:

1. reconstruct the min--max comparison and its inequality direction;
2. derive the exact radial and angular counts with strict spectral walls;
3. prove (15), continuity across $a=m\pi$, and (16)--(17) for every
   $N\ge1$ and $0<t\le1$;
4. derive the sufficient condition (18), not merely cite it;
5. prove the uniform cost (19) and reserve (20) on the entire closed
   domain;
6. own $a=0$, $0<a<\pi$, $a=\pi$, and the first positive radial branch;
7. prove the low piece including the equality face (13).

For the high piece:

1. reconstruct the action and inverse geometry, including all derivative
   signs and the ungridded curvature switch;
2. prove the endpoint traces in (22), including the improper $t=0$ limit;
3. derive (23)--(24) by exact Stieltjes integration without assuming
   $\tau>1$;
4. derive the exact half-integer angular ceiling and (25)--(26), including
   equality-wall conventions;
5. prove (27)--(29) uniformly, with exact monotonicity in $\varepsilon$;
6. close (30), the strict phase transfer, and the equality face (13);
7. execute the six-item replacement audit line by line.

Return an executable exact rational or symbolic ledger for every finite
comparison. If a step fails, freeze the first unsupported implication and
state the strongest domain actually proved. Do not repair a sign with
decimal sampling or silently move the target face.

## For A3: strictly isolated clean-room reconstruction

Receive only the frozen packet, its explicitly allowed prior lemmas, and
their exact domains. Before issuing a verdict, do not inspect the incumbent
response or ledger, exploration notes, other Round 16 messages, the
adversarial report, or a judge draft.

Attempt to falsify all of the following:

- $\varepsilon=1/100$, $1/25$, $1/10$, and the new closed face $1/8$;
- the limit $\varepsilon\downarrow0$ without treating $\varepsilon=0$ as
  part of the shell domain;
- $a=0$, $0<a<\pi$, $a=\pi$, the first branch above $\pi$, and every
  radial wall $a=m\pi$ from both sides;
- the common face $a=\pi/(4\varepsilon)$ from both pieces;
- the corner $\varepsilon=1/8$, $a=2\pi$, where the common face is also a
  radial wall and the strict convention is $(N,t)=(1,1)$;
- product angular walls $b_n^2/\varepsilon^2=\ell(\ell+1)$;
- action radial walls $n-1/4=T$, angular walls
  $R(n-1/4)/\varepsilon=m+1/2$, and phase-proxy walls;
- $\tau$ on, below, or above a sawtooth grid point, without assuming
  $\tau>1$;
- the improper outer trace, the terminal trace, and every dropped
  nonnegative Stieltjes term;
- the monotonic reductions in (19), (27), and (28);
- every one of the six replacements and the absence of a hidden Round 6
  aggregate dependency;
- the stretch calculations only as labeled arithmetic, without enlarging
  the frozen theorem.

Return `PASS` or `FAIL` and identify the first unsupported implication, if
one exists, before any cross-comparison with the incumbent proof.

## For A4: adversarial referee and exact-ledger auditor

First assume (10) is false. Audit the incumbent and isolated
reconstructions independently before comparing them. Reconstruct every
displayed identity, inequality direction, strictness claim, domain
restriction, monotonic endpoint reduction, and face assignment.

The audit must in particular verify:

- the exact formula (15) and the minimization producing $-8/375$;
- strict positivity in (17) for the smallest admissible $N$;
- the derivation of (18), including all floor/ceiling losses;
- the exact reserves $577/2880$ and $143/4096$;
- the curvature signs and the validity of the Stieltjes identity at every
  strict radial wall;
- $W\ge0$ on all of $[0,\infty)$ and the two-sided periodic primitive
  bounds;
- the exact count $J_{\rm rad}<a/\pi+1/4$ and the half-integer equality
  convention;
- strictness of (30) at the common face and at $\varepsilon=1/8$;
- the complete six-item replacement inventory;
- that (31)--(32) remain unpromoted and (33)--(34) are not called
  counterexamples;
- that (35)--(36) are applied only after the endpoint and union nodes pass.

Run the exact ledger independently. It must reproduce at least:

1. the algebraic expansion (15);
2. the lower bound in (17) and its strict positivity for $N\ge1$;
3. the product reserve $577/2880$;
4. the endpoint values $21/256$ and $193/4096$;
5. the complementary reserve $143/4096$;
6. all four stretch/obstruction fractions (31)--(34), with their signs;
7. the factor $8000/3481>2$.

The ledger checks arithmetic only; it does not replace the analytic proof.
Identify the first unsupported implication if any check fails.

## Mandatory branches, walls, and faces

Every incumbent proof, isolated reconstruction, exact ledger, and
adversarial review must explicitly own:

- $K=0$ and $K>0$, equivalently $a=0$ and $a>0$;
- the exact zero-count range $0\le a\le\pi$;
- every radial wall $a=m\pi$, with the excluded threshold convention
  $(N,t)=(m-1,1)$;
- every product angular wall
  $b_n^2/\varepsilon^2=\ell(\ell+1)$;
- the first positive radial and angular branches;
- the optical face $a=\pi/(4\varepsilon)$ from both pieces;
- the corner $(\varepsilon,a)=(1/8,2\pi)$ from both pieces;
- the lower ratio face $\rho=7/8$ and the open limit $\rho\uparrow1$;
- the action radial wall $n-1/4=T$, the exact half-integer angular wall,
  and every strict phase-proxy wall;
- the actual ungridded curvature interface $\tau$ and either side of every
  sawtooth grid point;
- all denominators, square roots, inverse-function domains, squarings, and
  improper endpoint limits;
- the interfaces $\rho=\rho_*$, $1/16$, $5/6$, $7/8$, and $99/100$ needed
  for conditional envelope integration;
- $K=64$, $3456$, $295^2$, $200000$, $K=K_0(5/6)$, and every sharper
  threshold face used in the accepted or conditional union.

## Promotion gates

Promote the Round 16 endpoint only if all of the following pass:

1. the packet is frozen and hashed before proof work;
2. the dependency audit distinguishes domain-free identities from every
   estimate that used $\varepsilon\le1/100$;
3. the product proof closes on (12a), including the exact zero range and
   the common face;
4. the complementary-action proof closes on (12b), including the actual
   curvature interface, improper trace, and common face;
5. all six mandatory replacements are explicit and no Round 6 aggregate
   result enters the proof;
6. every strict wall, branch, denominator, radicand, inverse, monotonicity,
   and shared face is owned;
7. a strictly isolated clean-room reconstruction passes before
   cross-review;
8. a fresh adversarial audit finds no unsupported implication;
9. an independently executed exact ledger reproduces every required
   comparison;
10. the two-piece union proves all $a\ge0$ at the closed face
    $\varepsilon=1/8$;
11. the conditional envelope audit uses the accepted Round 15 theorems on
    their sharpest domains and proves the $K=295^2$ equality face;
12. the judge applies any accepted State Patch exactly once.

## Explicit do-not-claim rules

- Do not call (10) proved until every promotion gate passes.
- Do not move the primary lower face below $\rho=7/8$ in Round 16.
- Do not promote either positive stretch screen (31)--(32).
- Do not call either negative screen (33)--(34) a counterexample or an
  impossibility theorem.
- Do not extend the Round 6 aggregate theorem or use it as a hidden bridge.
- Do not infer a theorem from the two endpoint reserves without proving the
  complete product and action paths.
- Do not claim the global ceiling $295^2$ until the endpoint, face union,
  and conditional envelope audit are independently accepted.
- Do not replace the true residual by a rectangular sweep.
- Do not treat bounded certification, sampled numerics, or agent consensus
  as proof.
- Do not close `SHELL-rho-compact`, `SHELL-rho-uniformity`, or
  `TARGET-shell-d3`, and do not promote `COMP-certified-bessel` beyond
  `diagnostic_only`, while the true compact residual remains open.
