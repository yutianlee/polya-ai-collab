# Main conclusion

The proof’s conceptual core is substantially shorter than its current owner graph:

[
N_D\le P,\qquad
P=\sum_{n-1/4<T}M(R(n-1/4))^2,\qquad
W=\int_0^T R(t)^2,dt,
]

followed by the exact defect decomposition

[
W-P
===

B(\rho,K)+R_{\mathrm{dec}}+R_{\mathrm{osc}}-E_{\mathrm{ang}}.
]

The complexity enters because the present proof uses relatively weak lower and upper bounds for (R_{\mathrm{dec}}) and (E_{\mathrm{ang}}). It therefore postpones the all-frequency argument until (K\ge k_{11}(\rho)), requiring the finite staircase through (k_{11}), the 38-state post-event theorem, and the associated zero/cap/localization infrastructure.  The exact retained-remainder identity itself is already global in ((\rho,K)). 

I found two sharpenings which, combined, appear to replace the entire small-hole and compact-middle owner machinery by one short analytic argument.

The resulting proposed structure is:

[
\boxed{
\begin{array}{c}
K\le \pi/(1-\rho):\quad N_D=0,[2mm]
K>\pi/(1-\rho),\quad 0<\rho\le 39/50:
\quad\text{one global defect estimate},[2mm]
39/50\le\rho<1:\quad\text{retain the existing optical theorem}.
\end{array}}
]

This would eliminate the (k_6,\ldots,k_{11}) staircase, the 38-state theorem, the residual sets (\mathcal D_{16},\ldots,\mathcal D_{20}), and most of Parts I–VI and IX–X of the supplement.

---

# 1. First sharpening: use the actual ratio-dependent slope cap

Put

[
\theta:=\arccos\rho.
]

The action derivative in the supplement is

[
q(z):=-A'(z)
============

\frac1\pi
\begin{cases}
\arccos(z/K)-\arccos(z/\rho K),&0<z<\rho K,[1mm]
\arccos(z/K),&\rho K\le z<K.
\end{cases}
]

The supplement proves that (q) increases before (z=\rho K) and decreases after it. Consequently, for fixed (\rho),

[
\boxed{
q(z)\le q(\rho K)=\frac{\theta}{\pi}.}
]

The current angular-block argument instead uses the uniform-in-(\rho) bound (q\le1/2). 

Let

[
x_n=n-\frac14,\qquad r_n=R(x_n),\qquad m_n=M(r_n).
]

For (t\in[n-1,x_n]), monotonicity of (R) gives (R(t)\ge r_n), and

[
x_n-t
=====

# A(r_n)-A(R(t))

\int_{r_n}^{R(t)}q(s),ds
\le
\frac{\theta}{\pi}\bigl(R(t)-r_n\bigr).
]

Therefore

[
R(t)\ge r_n+\frac{\pi}{\theta}(x_n-t).
]

Integrating over the left block of length (3/4),

[
\int_{n-1}^{x_n}R(t),dt
\ge
\frac34r_n+\frac{9\pi}{32\theta},
]

and hence

[
r_n
\le
\frac43\int_{n-1}^{x_n}R(t),dt
-\frac{3\pi}{8\theta}.
]

The exact strict angular convention gives

[
m_n<r_n+\frac12,
]

including at a common radial–angular wall. Thus

[
m_n^2-r_n^2
<
r_n+\frac14
\le
\frac43\int_{n-1}^{x_n}R(t),dt
------------------------------

\left(\frac{3\pi}{8\theta}-\frac14\right).
]

Define

[
d(\rho):=\frac{3\pi}{8\arccos\rho}-\frac14.
]

The left blocks are disjoint, so summing gives the strengthened angular theorem

[
\boxed{
E_{\mathrm{ang}}
<
\frac{1-\rho^2}{6}K^2-Nd(\rho),}
]

where

[
N=#\left{n\ge1:n-\frac14<T\right},
\qquad
T=\frac{(1-\rho)K}{\pi}.
]

Since (\arccos\rho<\pi/2) for (\rho>0),

[
d(\rho)>\frac12.
]

The present argument only obtains (N/2), and the final scalar theorem then discards all but (1/2). This loses both the fixed-ratio slope information and the number of active radial layers. 

Even without changing anything else, replacing (N/2) by (Nd(\rho)) should move the analytic handoff far below (k_{11}).

---

# 2. Second sharpening: replace the rational primitive minorant by the tangent envelope

Let (\mathscr W(t)) denote the primitive of the shifted radial sawtooth used in (R_{\mathrm{dec}}). The supplement proves

[
\mathscr W(t)=\frac{t^2}{2}
\qquad
\left(0\le t\le\frac34\right)
]

and, globally,

[
\mathscr W(t)\ge\frac t4-\frac1{32}.
]

These are consequences of the exact formula for (\Psi(t)=\mathscr W(t)-t/4). 

The current proof uses

[
L(t)=\frac{t^2}{2(1+2t)}.
]

A substantially stronger minorant is

[
\boxed{
L_\sharp(t)=
\begin{cases}
\dfrac{t^2}{2},&0\le t\le\dfrac14,[2mm]
\dfrac t4-\dfrac1{32},&t\ge\dfrac14.
\end{cases}}
]

It is (C^1), nonnegative, and satisfies (L_\sharp\le\mathscr W). Indeed, on (1/4\le t\le3/4),

[
\frac{t^2}{2}
-\left(\frac t4-\frac1{32}\right)
=================================

\frac12\left(t-\frac14\right)^2\ge0,
]

while for (t\ge3/4) the global sawtooth lower bound applies.

Moreover,

[
L_\sharp'(t)=\min\left{t,\frac14\right}.
]

Since (-dg) is a positive measure on the decreasing-curvature branch,

[
R_{\mathrm{dec}}
\ge
R_\sharp:=
-\int_{(0,\tau)}L_\sharp(t),dg(t),
\qquad
\tau=KG_1(\rho).
]

Integration by parts gives

[
R_\sharp
========

-L_\sharp(\tau)g(\tau)
+
\int_0^\tau L_\sharp'(t)g(t),dt.
]

Changing variables from (t) to (z=R(t)),

[
\int_0^\tau L_\sharp'(t)g(t),dt
===============================

\int_{\rho K}^{K}
2z\min\left{A(z),\frac14\right},dz.
]

For

[
0<\rho\le\frac{39}{50},
\qquad
K\ge\frac{\pi}{1-\rho},
]

one has (\tau>1/4). Indeed, the elementary turning estimate already used in the supplement gives

[
G_1(\rho)
\ge
\frac{2\sqrt2}{3\pi}(1-\rho)^{3/2},
]

so

[
\tau
\ge
\frac{2\sqrt2}{3}\sqrt{1-\rho}
\ge
\frac{2\sqrt2}{3}\sqrt{\frac{11}{50}}

> \frac14.
> ]

Thus

[
L_\sharp(\tau)=\frac{\tau}{4}-\frac1{32}.
]

In the exact retained identity, the interface contribution in (B(\rho,K)) is

[
g(\tau)\left(\frac{\tau}{4}+\frac3{32}\right).
]

After subtracting (L_\sharp(\tau)g(\tau)), it becomes simply

[
\frac18g(\tau)
==============

\frac{\pi\rho K}{4\arccos\rho}.
]

Therefore the new radial lower payment is

[
\boxed{
H_\sharp(\rho,K)
================

\frac{\rho^2K^2}{4}
-\frac{\pi\rho K}{4(1-\rho)}
+\frac{\pi\rho K}{4\arccos\rho}
+
\int_{\rho K}^{K}
2z\min\left{A(z),\frac14\right},dz.}
]

This is simpler than the present (H): the rational factor
(A(1+A)/(1+2A)^2) disappears.

---

# 3. The remaining integral becomes a universal ball term

On the outer branch (z\ge\rho K),

[
A(z)=G_K(z).
]

Let (R_B(t)) be the inverse of the ball action (G_K). Since
(G_K(\rho K)=\tau\ge1/4), layer cake gives

[
\frac{\rho^2K^2}{4}
+
\int_{\rho K}^{K}
2z\min\left{G_K(z),\frac14\right},dz
====================================

\int_0^{1/4}R_B(t)^2,dt.
]

Define

[
B_0(K):=\int_0^{1/4}R_B(t)^2,dt.
]

Then

[
\boxed{
H_\sharp(\rho,K)
================

B_0(K)
-\frac{\pi\rho K}{4(1-\rho)}
+\frac{\pi\rho K}{4\arccos\rho}.}
]

The shell-dependent integral has disappeared. Only a universal ball boundary-layer term remains.

Using

[
G_1(s)
======

\frac1\pi\int_s^1\arccos u,du
\ge
\frac{2\sqrt2}{3\pi}(1-s)^{3/2},
]

one obtains, for (0\le t\le1/4),

[
R_B(t)
\ge
K-C K^{1/3}t^{2/3},
\qquad
C=\left(\frac{3\pi}{2\sqrt2}\right)^{2/3}
=\frac{(3\pi)^{2/3}}2.
]

Consequently,

[
\boxed{
B_0(K)
\ge
\frac{K^2}{4}
-\alpha K^{4/3}
+\beta K^{2/3},}
]

where

[
\alpha
======

\frac{6C}{5,4^{5/3}},
\qquad
\beta
=====

\frac{3C^2}{7,4^{7/3}}.
]

Combining the radial and angular estimates, and using (N\ge1) whenever
(K\ge\pi/(1-\rho)), gives

[
W-P>
\frac{1+2\rho^2}{12}K^2
-\alpha K^{4/3}
+\beta K^{2/3}
-\frac{\pi\rho K}{4(1-\rho)}
+\frac{\pi\rho K}{4\arccos\rho}
+d(\rho).
]

---

# 4. The scalar closure becomes elementary algebra

The inequality

[
\boxed{
\arccos\rho
\le
\frac{\pi}{2}\sqrt{1-\rho}}
]

follows by writing (\rho=\cos\theta), using
(1-\rho=2\sin^2(\theta/2)), and the monotonicity of
(\sin y/y) on (0\le y\le\pi/4).

Put

[
e=1-\rho.
]

Then

[
\frac{\pi}{4\arccos\rho}\ge\frac1{2\sqrt e},
\qquad
d(\rho)\ge\frac3{4\sqrt e}-\frac14.
]

It is therefore sufficient to prove positivity of

[
\underline{\mathcal G}(\rho,K)
==============================

\frac{1+2\rho^2}{12}K^2
-\alpha K^{4/3}
+\beta K^{2/3}
-\frac{\pi\rho K}{4e}
+\frac{\rho K}{2\sqrt e}
+\frac3{4\sqrt e}
-\frac14.
]

## Positivity on the base curve

Take

[
K_0=\frac{\pi}{e},
\qquad
x=e^{-1/6}\ge1.
]

Set

[
\mathsf A:=\alpha\pi^{4/3},
\qquad
\mathsf B:=\beta\pi^{2/3}.
]

Direct substitution gives

[
\underline{\mathcal G}(\rho,K_0)=F(x),
]

where

[
\begin{aligned}
F(x)
={}&
\frac{\pi}{2}x^9
-\mathsf A x^8
-\frac{\pi^2}{12}x^6
+\mathsf Bx^4\
&+
\left(\frac34-\frac{\pi}{2}\right)x^3
+\frac{\pi^2}{6}
-\frac14.
\end{aligned}
]

Using only

[
\frac{157}{50}<\pi<\frac{22}{7},
]

and positive-side cubing gives

[
\mathsf A<\frac{49}{40},
\qquad
\frac{179}{1000}<\mathsf B<\frac15.
]

These estimates imply

[
F(1)>\frac14,
\qquad
F'(1)>-\frac52,
\qquad
F''(x)>14\quad(x\ge1).
]

For example, (F'''(x)>0) follows from the same coarse rational bounds, and

[
F''(1)

>

33\frac{157}{50}
-\frac52\left(\frac{22}{7}\right)^2
-56\frac{49}{40}
+\frac92

> 14.
> ]

Writing (y=x-1\ge0),

[
F(x)

>

# \frac14-\frac52y+7y^2

7\left(y-\frac5{28}\right)^2+\frac3{112}>0.
]

Thus

[
\underline{\mathcal G}\left(\rho,\frac{\pi}{1-\rho}\right)>0.
]

## Monotonicity above the base curve

One also has

[
\partial_K^2\underline{\mathcal G}>0
\qquad
\left(K\ge\frac{\pi}{1-\rho}\right).
]

To check the first derivative at the base, define

[
C_1=\frac43\alpha\pi^{1/3},
\qquad
C_2=\frac23\beta\pi^{-1/3}.
]

Then

[
\partial_K\underline{\mathcal G}(\rho,K_0)
==========================================

D(x),
]

with

[
D(x)
====

\frac{\pi}{12}
\left(3x^6-5+4x^{-6}\right)
+
\frac12\left(x^3-x^{-3}\right)
-C_1x^2+C_2x^{-2}.
]

Positive-side cubing gives

[
C_1<\frac{13}{25},
\qquad
C_2<\frac1{25}.
]

Consequently,

[
D(1)>
\frac{157}{300}-\frac{13}{25}
=============================

\frac1{300}>0,
]

[
D'(1)>
3-\frac{11}{7}-\frac{28}{25}
============================

\frac{54}{175}>0,
]

and a crude estimate gives (D''(x)>0) for (x\ge1). Hence (D(x)>0).

Therefore

[
\underline{\mathcal G}(\rho,K)>0
\qquad
\left(
0<\rho\le\frac{39}{50},
\quad
K\ge\frac{\pi}{1-\rho}
\right).
]

It follows that

[
P(\rho,K)<W(\rho,K)
]

throughout this region.

---

# 5. Completion of the simplified proof

For

[
K\le\frac{\pi}{1-\rho},
]

the radial channel operator

[
-\frac{d^2}{dr^2}
+
\frac{\ell(\ell+1)}{r^2}
]

on an interval of length (1-\rho) has all eigenvalues at least

[
\frac{\pi^2}{(1-\rho)^2}.
]

Thus, under the strict counting convention,

[
N_D(A_{\rho,1},K^2)=0.
]

For

[
K>\frac{\pi}{1-\rho},
\qquad
0<\rho\le\frac{39}{50},
]

the preceding argument gives

[
N_D(A_{\rho,1},K^2)
\le P(\rho,K)<W(\rho,K).
]

For

[
\frac{39}{50}\le\rho<1,
]

retain the existing all-frequency optical theorem. The original manuscript already proves that theorem independently of the finite middle staircase. 

Hence the proposed proof has only two ratio owners:

[
(0,39/50]\quad\text{and}\quad[39/50,1).
]

The small-hole endpoint, (\rho_c), (k_6,\ldots,k_{11}), (K_0(\rho)), (U(\rho)), and the residual sets are no longer needed.

---

# Structural comparison

| Component             | Current proof                               | Proposed replacement                      |
| --------------------- | ------------------------------------------- | ----------------------------------------- |
| Low frequency         | Several primitive and finite owners         | One Poincaré no-mode bound                |
| Middle high frequency | Handoff at (k_{11})                         | Handoff at (\pi/(1-\rho))                 |
| Angular estimate      | (q\le1/2), payment (N/2)                    | (q\le\arccos\rho/\pi), payment (Nd(\rho)) |
| Radial minorant       | (t^2/[2(1+2t)])                             | Tangent envelope (L_\sharp)               |
| Remaining integral    | Shell-dependent loss (J(\rho,K))            | Universal ball quarter-layer (B_0(K))     |
| Scalar proof          | Secant grid and degree-nine Bernstein table | Convex degree-nine polynomial             |
| Finite high staircase | 38 states through (k_{11})                  | Removed                                   |
| Ledger                | Large proof/audit supplement                | Most rows become archival only            |

The supplement already distinguishes the live implication chain from the historical 611-row provenance census, but substantial finite zero, cap, staircase, and subtraction material remains in Parts I–VI.  Under the proposed route, that entire finite-middle package ceases to be a theorem premise.

---

# Lower-risk alternatives

## A. Make only the angular improvement

The least invasive change is to leave the present radial (H(\rho,K)) untouched and replace

[
\frac N2
\quad\text{by}\quad
N\left(
\frac{3\pi}{8\arccos\rho}-\frac14
\right).
]

This requires changing only Part VIII and the scalar handoff. It should move the all-frequency base substantially below (k_{11}), potentially to (k_6) or (k_7), while retaining most of the current paper. This is the appropriate fallback if the stronger tangent-envelope argument encounters an endpoint issue during audit.

## B. Replace the finite owner graph with a certified compact check

A computer-assisted version would be much shorter still:

1. retain the exact phase bridge and global defect identities;
2. prove monotonicity above an explicit base;
3. certify the remaining one-variable base inequality by rational interval arithmetic.

The project strategy explicitly treats an analytic tail plus a deterministic interval/rational finite certificate as an acceptable proof architecture.  With the reductions above, the certificate would concern one smooth scalar function, not Bessel roots, 38 event states, or hundreds of ledger rows.

## C. Separate theorem proof from audit material

Independently of the mathematical route, the manuscript should have two documents:

* a proof paper containing only the live dependency chain;
* an audit repository containing exact tables, retired seams, executable regressions, hashes, and provenance.

The non-tiling theorem is logically independent and can also be moved to a short appendix or separate note. The current paper itself states that the spectral and non-tiling arguments are independent.

---

# Recommended course

The strongest route is the **ratio-sharp angular estimate plus tangent-envelope radial minorant**. It appears to reduce the entire lower and middle ratio range to a short algebraic theorem and leaves only the existing optical strip.

Before replacing the manuscript, the necessary audit is narrow:

1. independently verify the (L_\sharp\le\mathscr W) Stieltjes calculation;
2. check the common radial–angular wall convention in the strengthened angular lemma;
3. reproduce the rational bounds for (\mathsf A,\mathsf B,C_1,C_2);
4. certify the scalar lower bound independently with interval arithmetic as a regression check;
5. rebuild the dependency graph and remove every now-unused finite row.

This is the most direct path to turning the present proof from a large owner-and-ledger argument into a short retained-remainder proof.
