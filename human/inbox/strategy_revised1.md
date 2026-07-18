# Structural assessment

The proof has a relatively short mathematical core and a very long closure mechanism. The length is largely caused by the requirement that every compact-range decision be replaced by hand-checkable analytic or exact-rational reasoning. The supplement explicitly contains a 611-row ledger and replaces earlier compact and aggregate computer certificates by ten analytic modules. 

I have reviewed the proof architecture and the key inequalities, but I have not independently audited every rational entry in that ledger. The recommendations below concern proof strategy and dependency structure rather than certification of all existing arithmetic.

The main conclusion is:

[
\boxed{\text{Do not replace the phase reduction. Replace the regional closure.}}
]

The separation-of-variables and Bessel-phase part is natural and efficient. The substantial opportunity for simplification begins immediately after the phase-to-lattice reduction.

---

## 1. The irreducible core of the present proof

After scaling, write

[
A_{\rho,1}={x\in\mathbb R^3:\rho<|x|<1},
\qquad 0<\rho<1,
\qquad \Lambda=K^2.
]

Separation into spherical harmonics gives the radial operators

[
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2},
\qquad \ell=0,1,2,\ldots ,
]

with multiplicity (2\ell+1). Setting (\nu_\ell=\ell+\tfrac12), the radial frequencies are zeros of the Bessel cross-product. The proof obtains the exact strict phase count

[
N_D(A_{\rho,1},K^2)
===================

\sum_{\ell\ge0}(2\ell+1)
\bigl[\gamma_{\rho,K}(\nu_\ell)\bigr]_< .
]

The imported Bessel-phase estimates then give

[
\gamma_{\rho,K}(z)
<
A_{\rho,K}(z)+\frac14,
\qquad
A_{\rho,K}(z)=G_K(z)-G_{\rho K}(z),
]

where

[
G_a(z)=
\frac1\pi
\left(
\sqrt{a^2-z^2}-z\arccos\frac za
\right)_+ .
]

Consequently,

[
N_D(A_{\rho,1},K^2)\le P(\rho,K),
]

with the strict lattice proxy

[
P(\rho,K)
:=
\sum_{\nu_\ell<K}
2\nu_\ell
\left[A_{\rho,K}(\nu_\ell)+\frac14\right]_< .
]

At the same time,

[
W(\rho,K)
:=
\int_0^K2zA_{\rho,K}(z),dz
==========================

\frac{2}{9\pi}(1-\rho^3)K^3,
]

which is exactly the Weyl term. Thus the spectral theorem has already been reduced to

[
\boxed{P(\rho,K)\le W(\rho,K).}
]

This is the fundamental reduction in Section 2 of the main manuscript. 

Everything after that is a method for proving this one shifted lattice inequality.

---

## 2. Promote the layer-cake identity to the central theorem

The cleanest representation appears later in the proof and supplement, but it should occur immediately after the phase reduction.

Put

[
T=A_{\rho,K}(0)=\frac{(1-\rho)K}{\pi},
]

and let

[
R:[0,T]\longrightarrow[0,K]
]

be the decreasing inverse of (A_{\rho,K}). Define

[
x_n=n-\frac14,
\qquad
M(r)=#\left{\ell\ge0:\ell+\frac12<r\right}.
]

Then the proxy and Weyl term have the exact representations

[
P(\rho,K)
=========

\sum_{\substack{n\ge1\x_n<T}}
M(R(x_n))^2,
]

and

[
W(\rho,K)=\int_0^T R(t)^2,dt.
]

Thus Pólya follows from the single shifted-quadrature inequality

[
\boxed{
\sum_{n-1/4<T}M(R(n-1/4))^2
\le
\int_0^T R(t)^2,dt.
}
\tag{ML}
]

The supplement already derives this formulation and decomposes its error into a radial shifted-quadrature deficit and an angular rounding defect. 

### Recommended expository change

Make (ML) the “master lattice proposition” of the paper. Then all subsequent arguments should be presented as estimates for the two terms in

[
W-P=D_{\mathrm{rad}}-E_{\mathrm{ang}},
]

where

[
D_{\mathrm{rad}}
================

## \int_0^T R(t)^2,dt

\sum_{x_n<T}R(x_n)^2,
]

and

[
E_{\mathrm{ang}}
================

\sum_{x_n<T}
\left(M(R(x_n))^2-R(x_n)^2\right).
]

This immediately gives a single conceptual spine:

[
\text{spectral count}
\longrightarrow
\text{phase proxy}
\longrightarrow
\text{shifted quadrature}
\longrightarrow
D_{\mathrm{rad}}\ge E_{\mathrm{ang}}.
]

The current small-hole tails, complementary-action argument, optical argument, and retained-remainder argument are all different implementations of this same comparison. Presenting them in this common language would remove a substantial amount of duplicated notation and motivation.

---

# 3. Best practical simplification: a constant high-frequency cutoff

The strongest concrete simplification is to extend the supplement’s retained-remainder argument to a **constant cutoff**

[
K\ge K_*,
]

instead of reaching it only after the (k_6)- and (k_{11})-staircases and the owner-region subtraction.

A conservative and analytically convenient choice is

[
\boxed{K_*=20.}
]

This value is not optimized.

## 3.1 Existing global ingredients

The supplement already proves globally, whenever at least one shifted radial layer is active,

[
E_{\mathrm{ang}}
<
\frac{1-\rho^2}{6}K^2-\frac12.
\tag{1}
]

It also constructs a smooth quantity (H(\rho,K)) such that

[
E_{\mathrm{ang}}<H(\rho,K)
\quad\Longrightarrow\quad
P(\rho,K)<W(\rho,K).
\tag{2}
]

Thus it is enough to prove positivity of

[
S(\rho,K)
:=
H(\rho,K)
-\frac{1-\rho^2}{6}K^2
+\frac12.
\tag{3}
]

The present proof establishes this on

[
\rho_c\le\rho\le\frac{39}{50},
\qquad
K\ge k_{11}(\rho),
]

using positivity on the base curve and upward monotonicity in (K). 

The same method can apparently be extended to

[
0<\rho\le\frac{39}{50},
\qquad K\ge20,
]

without any mode staircase.

---

## 3.2 Monotonicity in (K)

The derivative estimate already developed in the supplement gives, for (K>12),

[
\partial_KS(\rho,K)

>

K\left(\frac{13}{1134}+\frac{\rho^2}{3}\right)
+\frac{3\rho}{8}
-\frac{11\rho}{14(1-\rho)}.
]

Using (K>12), it is enough to prove

[
p(\rho):=
(1-\rho)
\left(
\frac{26}{189}+4\rho^2+\frac{3\rho}{8}
\right)
-\frac{11\rho}{14}

> 0.
> \tag{4}
> ]

For (0\le\rho\le 7/51), simply discard the positive quadratic terms:

[
p(\rho)
\ge
\frac{26}{189}(1-\rho)-\frac{11\rho}{14}
\ge
\frac{209}{19278}>0.
]

For (7/51\le\rho\le39/50), the positive Bernstein-coefficient verification already used in the scalar-positivity module applies. Hence

[
\partial_KS(\rho,K)>0
]

throughout

[
0<\rho\le\frac{39}{50},
\qquad K\ge20.
\tag{5}
]

So only the constant base (K=20) remains.

---

## 3.3 A simple base estimate at (K=20)

In the supplement’s notation, the only non-elementary loss in (S) is

[
J(\rho,K)
=========

\frac{K^2}{2}
\int_\rho^1
\frac{s,ds}{(1+2KG_1(s))^2}.
]

The turning-point inequality

[
G_1(s)
\ge
\frac{2\sqrt2}{3\pi}(1-s)^{3/2}
]

and an exact beta integral imply

[
J(\rho,K)
\le
C_\beta K^{4/3},
]

where

[
C_\beta
=======

\frac{2\pi}{9\sqrt3}
\left(\frac{3\pi}{4\sqrt2}\right)^{2/3}.
]

At (K=20), elementary rational bounds such as

[
\pi<\frac{355}{113},
\qquad
\sqrt3>\frac{265}{153}
]

give

[
J(\rho,20)<\frac{3079}{100}.
\tag{6}
]

Retain only the positive (3/32) endpoint contribution in (H), use

[
\pi<\frac{22}{7},
\qquad
\pi>3,
\qquad
\arccos\rho
===========

\frac{\pi}{2}-\arcsin\rho
\le
\frac{11}{7}-\rho-\frac{\rho^3}{6},
]

and obtain

[
S(\rho,20)>L(\rho),
]

where

[
\begin{aligned}
L(\rho)
={}&
\frac{100}{3}(1+2\rho^2)
-\frac{3079}{100}
-\frac{110}{7}\frac{\rho}{1-\rho}
+\frac12\
&+
\frac{45\rho}
{4\left(\frac{11}{7}-\rho-\frac{\rho^3}{6}\right)}.
\end{aligned}
\tag{7}
]

After clearing the positive denominators, positivity reduces to

[
\begin{aligned}
Q(\rho)
={}&
980000\rho^6-980000\rho^5
+6155737\rho^4
-15164737\rho^3\
&+9902172\rho^2
-1875978\rho
+421806

> 0.
> \end{aligned}
> \tag{8}
> ]

On writing

[
\rho=\frac{39}{50}u,
\qquad 0\le u\le1,
]

the degree-six Bernstein coefficients of (Q) are

[
\begin{gathered}
421806,\quad
\frac{8896443}{50},\quad
\frac{1049011926}{3125},\
\frac{1338120138297}{2500000},\quad
\frac{17771939475189}{31250000},\
\frac{520113194841}{1562500},\quad
\frac{17939689779}{6250000}.
\end{gathered}
]

All are positive. Therefore (subject to an independent audit of the displayed reductions)

[
S(\rho,20)>0
\qquad
\left(0<\rho\le\frac{39}{50}\right).
\tag{9}
]

Combining (5) and (9) gives the proposed theorem

[
\boxed{
P(\rho,K)<W(\rho,K)
\quad
\text{for }
0<\rho\le\frac{39}{50},
\ K\ge20.
}
\tag{10}
]

This would replace:

* the complete Bessel-zero registry;
* the two-sided (k_6) staircase;
* the lower-(d) staircase;
* the (k_{11}) high staircase;
* most localization and cap-payment tables;
* the sets (\mathcal D_{16},\mathcal D_{19},\mathcal D_{20});
* the 63-state owner subtraction.

The current manuscript’s all-frequency theorem already demonstrates that the retained-remainder mechanism is capable of closing an unbounded region; the proposal above merely chooses a simpler constant base and enlarges its ratio range. 

---

# 4. The remaining compact problem becomes very small

The existing proof already has:

1. a complete small-hole theorem for (0<\rho\le\rho_*);
2. an all-frequency optical theorem for (39/50\le\rho<1). 

After the constant-cutoff result, the only region left is

[
\boxed{
\rho_*<\rho<\frac{39}{50},
\qquad
0<K<20.
}
\tag{11}
]

This compact range is much simpler than the present regional decomposition.

Indeed,

[
\nu_\ell<K<20
\quad\Longrightarrow\quad
\ell\le19,
]

and

[
n-\frac14<T
===========

\frac{(1-\rho)K}{\pi}
<
\frac{20}{\pi}<6.37
]

implies

[
n\le6.
]

Thus the entire remaining proxy involves at most

[
20\times6=120
]

angular-radial incidence conditions.

More importantly, one need not certify Bessel zeros. The phase theorem has already reduced the problem to the elementary proxy involving only

[
\sqrt{\cdot},\qquad \arccos,\qquad
A_{\rho,K}(\ell+\tfrac12),
\qquad
W(\rho,K).
]

A compact certificate can therefore verify directly that

[
P(\rho,K)\le W(\rho,K)
]

over (11).

## Suitable certificate design

A rigorous verifier would:

1. subdivide the ((\rho,K))-rectangle into rational boxes;
2. interval-evaluate each (A_{\rho,K}(\nu_\ell));
3. determine the strict values of
   [
   \left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<;
   ]
4. subdivide boxes intersecting an integer wall;
5. use an interval lower bound for
   [
   W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3;
   ]
6. emit a deterministic certificate containing only rational endpoints and interval enclosures.

The strategy report originally identifies precisely this analytic-tail plus certified-finite-window structure as the natural FLPS architecture. 

This route is considerably cleaner than converting every finite decision into a printed exact-rational lemma. The supplement itself notes that earlier compact certificates existed but were deliberately removed from the logical dependency chain. 

---

# 5. Best purely analytic simplification: a double-sawtooth theorem

For a completely non-computational proof, the correct target is not another staircase. It is a global theorem proving

[
D_{\mathrm{rad}}\ge E_{\mathrm{ang}}
]

for the shell action.

Define

[
e(r)=M(r)^2-r^2.
]

On every complete angular cell,

[
m-\frac12<r\le m+\frac12,
]

one has (M(r)=m), and hence

[
\int_{m-1/2}^{m+1/2}
e(r),dr
=======

-\frac1{12}.
\tag{12}
]

This negative cell mean is a major source of cancellation. The present pointwise estimate

[
M(r)^2-r^2<r+\frac14
]

throws most of it away.

At the same time,

[
q(r)=-A'_{\rho,K}(r)
]

is nonnegative and single-peaked: it increases up to the inner interface (r=\rho K) and decreases afterward. The supplement already exploits this geometry, but only after several rounds of separate estimates. 

A stronger global lemma should combine:

* the negative mean (-1/12) of each angular cell;
* the single-peaked shape of (q);
* the radial sawtooth generated by the sampling points (n-\tfrac14);
* the exact common-jump convention when a radial sample coincides with an angular wall.

A plausible target is

[
E_{\mathrm{ang}}
\le
\int_0^K e(r)q(r),dr
+
C,\operatorname{Var}(q),
]

followed by a matching lower bound for (D_{\mathrm{rad}}). Better still would be a direct paired inequality

[
E_{\mathrm{ang}}\le D_{\mathrm{rad}}.
]

Relevant tools are:

* Euler–Maclaurin summation with periodic Bernoulli functions;
* Stieltjes integration preserving common atoms;
* rearrangement inequalities for single-peaked weights;
* Fourier expansions of the centered sawtooth;
* pairing of adjacent angular cells across the peak.

A successful result of this type would collapse the entire proof after the phase reduction to one general lattice lemma.

---

# 6. A geometric reformulation: shifted cubic lattice packing

There is also a useful three-dimensional interpretation of the layer cake.

Define

[
\mathcal B_A
============

\left{
(u,v,t)\in\mathbb R_+^3:
t<A_{\rho,K}(\max{u,v})
\right}.
]

The cross-section at height (t) is a square of side (R(t)), so

[
|\mathcal B_A|
==============

# \int_0^TR(t)^2,dt

W(\rho,K).
]

Moreover, (P(\rho,K)) is exactly the number of shifted lattice points

[
\left(i+\frac12,j+\frac12,n-\frac14\right)
]

inside (\mathcal B_A). Indeed,

[
M(R(x_n))^2
]

counts the pairs ((i,j)) satisfying

[
i+\frac12<R(x_n),
\qquad
j+\frac12<R(x_n).
]

Thus the problem becomes

[
\boxed{
#\left(
\mathcal B_A
\cap
\left[
(\mathbb Z_{\ge0}+\tfrac12)^2
\times
(\mathbb Z_{\ge1}-\tfrac14)
\right]
\right)
\le
|\mathcal B_A|.
}
\tag{13}
]

This suggests a Blichfeldt-type or cell-packing proof.

A useful partial observation is that

[
0\le -A'_{\rho,K}(z)\le\frac12.
]

For every shifted lattice point in a radial layer (n\ge2), one can tilt its unit vertical cell over the angular unit square by at most half the angular displacement. The (1/2)-Lipschitz bound keeps the top of that cell below the graph of (A), and (n\ge2) keeps its bottom above (t=0). These cells are disjoint.

Therefore, in this packing formulation, the true obstruction is concentrated in the **first radial layer** (n=1). This is consistent with the retained-remainder calculation: most of the bulk is naturally paid by volume, and the difficulty is a lower-boundary correction.

A theorem saying that the unused lower-boundary volume pays the first layer would give a very short, geometric proof of (ML). This is a research-level route, but it targets the actual obstruction rather than introducing further parameter staircases.

---

# 7. Improve the phase bound rather than the mode inventory

The blanket correction (+1/4) is responsible for much of the integerization cost. The manuscript already has the sharper estimate

[
\gamma_{\rho,K}(z)
<
A_{\rho,K}(z)+s_{\rho K}(z),
]

where below the inner interface

[
s_{\rho K}(z)
=============

\min{H_{\rho K}(z),1/4}.
]

Only later is this frequently replaced by the coarser (+1/4). 

A shell-specific Prüfer or Langer analysis could distinguish:

* (z<\rho K), where both endpoints lie in the oscillatory region and the phase correction should be substantially smaller;
* (\rho K\le z<K), where there is one turning point and the (1/4) Maslov correction is structurally natural.

The realistic objective is not to remove (1/4) everywhere. It is to localize the quarter-shift to the one-turning-point sector and use a quantitatively smaller correction in the two-oscillatory-endpoint sector.

For the compact verification route, this improvement is immediate: certify the sharper proxy

[
\sum_\ell 2\nu_\ell
\bigl[A_{\rho,K}(\nu_\ell)+s_{\rho K}(\nu_\ell)\bigr]_<
]

instead of the coarse (P). This should significantly enlarge the margin near difficult integer walls.

---

# 8. Ball-difference bracketing as a secondary route

Adding a Dirichlet interface at radius (\rho) gives

[
N_D(B_\rho,K^2)
+
N_D(A_{\rho,1},K^2)
\le
N_D(B_1,K^2),
]

and therefore

[
N_D(A_{\rho,1},K^2)
\le
N_D(B_1,K^2)-N_D(B_\rho,K^2).
\tag{14}
]

If one could prove explicit two-sided ball estimates of the form

[
N_D(B_1,K^2)
\le
\frac{2}{9\pi}K^3-\frac14K^2+C K,
]

and

[
N_D(B_\rho,K^2)
\ge
\frac{2}{9\pi}\rho^3K^3-\frac14\rho^2K^2-C\rho K,
]

then (14) would give

[
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3
-\frac14(1-\rho^2)K^2
+C(1+\rho)K.
]

This proves shell Pólya for an explicit high-frequency range, leaving a finite check.

The difficulty is that a lower bound for the ball counting function with the correct second term is required. Obtaining it may reproduce much of the same Bessel lattice analysis. This is therefore a useful backup high-energy route, but it is less promising than the layer-cake simplification.

---

# 9. Approaches unlikely to simplify the exact theorem

Several general methods are unlikely to produce the exact all-energy inequality without recreating the same arithmetic problem:

* Berezin–Li–Yau or Riesz-mean inequalities lose information at the endpoint (\gamma=0).
* A generic two-term Weyl expansion gives eventual Pólya only when its remainder is explicit and smaller than the boundary term.
* Crude comparison with the product ((\rho,1)\times S^2) works well only for thin shells; the present proof already uses essentially the sharp version of that idea.
* Additional mode-by-mode Bessel-zero tables would enlarge, rather than simplify, the present proof.

The next improvement should therefore be global—quadrature, packing, or certified compact closure—not another refinement of the owner graph.

---

# 10. Recommended revised proof structure

A substantially shorter manuscript could have the following architecture.

## Part I. Exact spectral reduction

1. Scaling and strict counting convention.
2. Spherical-harmonic decomposition.
3. Exact Bessel determinant and phase enumeration.
4. Uniform phase majorant.
5. Definition of (P(\rho,K)) and proof that (N_D\le P).
6. Exact action identity (W=\frac{2}{9\pi}(1-\rho^3)K^3).

## Part II. Master lattice formulation

7. Exact layer-cake identities
   [
   P=\sum M(R(n-\tfrac14))^2,
   \qquad
   W=\int R^2.
   ]
8. One lemma containing all strict radial and angular wall conventions.
9. Error decomposition (W-P=D_{\mathrm{rad}}-E_{\mathrm{ang}}).

## Part III. Three owners only

10. Small-hole theorem for (0<\rho\le\rho_*).
11. Optical theorem for (39/50\le\rho<1).
12. Constant-cutoff theorem for
    [
    0<\rho\le39/50,\qquad K\ge20.
    ]

## Part IV. Compact certificate

13. Verify
    [
    \rho_*<\rho<39/50,\qquad 0<K<20
    ]
    directly for the elementary phase proxy.
14. Publish the checker, rational box certificate, and replay instructions.

## Appendix

15. External phase and floor-sum inputs.
16. Optional exact-rational spot checks.
17. Non-tiling theorem, which is logically independent and can also be published separately.

This would likely reduce the logical proof from the present main manuscript plus 62-page supplement to roughly 25–35 pages plus a compact, independently replayable certificate.

---

# Priority ranking

| Approach                                                           | Expected reduction |   Technical risk | Recommendation                       |
| ------------------------------------------------------------------ | -----------------: | ---------------: | ------------------------------------ |
| Move the exact layer cake to the start                             |           Moderate |              Low | Do immediately                       |
| Constant cutoff (K\ge20) plus compact certificate                  |          Very high |       Low–medium | Best practical route                 |
| Use the optimized phase correction (s_{\rho K}) in the certificate |           Moderate |              Low | Do with the compact check            |
| Global double-sawtooth lemma                                       |            Maximal |             High | Best purely analytic research target |
| Shifted cubic-cell packing                                         |            Maximal |             High | Strong conceptual alternative        |
| Ball-difference bracketing                                         |           Moderate |      Medium–high | Secondary route                      |
| More mode staircases and zero registries                           |           Negative | High bookkeeping | Avoid                                |

The most defensible simplification is therefore:

[
\boxed{
\text{phase reduction}
+
\text{global layer cake}
+
\text{constant high-frequency theorem}
+
\text{small compact certificate}.
}
]

The strongest longer-term analytic alternative is a general shifted-lattice theorem proving (D_{\mathrm{rad}}\ge E_{\mathrm{ang}}) directly.
