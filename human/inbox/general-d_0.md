# Strategic objective

The shifted-tail route should reduce the entire higher-dimensional shell theorem to **one new two-dimensional lattice inequality**.

The correct architecture is

[
\boxed{
\text{real-order phase bound}
;\Longrightarrow;
\text{uniform shifted shell-tail theorem}
;\Longrightarrow;
\text{positive dimension lifting}
;\Longrightarrow;
\text{Pólya for every }d\ge3.
}
]

The current paper already supplies the first step: its Bessel estimate is valid for every real order, and it gives the strict shell-action proxy

[
\gamma_{\rho,K}(z)<A_{\rho,K}(z)+\frac14.
]

Thus no new Bessel asymptotics are needed for general (d). 

The genuine research problem is the shifted-tail theorem below. I do not regard that theorem as proved yet. The algebraic dimension lifting after it is comparatively routine and follows the mechanism already used by FLPS for balls. 

---

# 1. The central theorem to target

Fix

[
0<\rho<1,\qquad K>0,\qquad \mu=\rho K.
]

Define the zero-extended ball action

[
G_a(z)
======

\begin{cases}
\dfrac1\pi
\left(
\sqrt{a^2-z^2}
-z\arccos\dfrac za
\right),&0\le z<a,[2mm]
0,&z\ge a,
\end{cases}
]

and the shell action

[
A_{\rho,K}(z)=G_K(z)-G_\mu(z).
]

Retain the strict positive-integer count

[
[u]_<:=#{n\in\mathbb N:n<u}.
]

For a shift (\sigma\ge0), define the strict shifted tail

[
\boxed{
\mathcal T^<_{\rho,K}(\sigma)
=============================

\left[A_{\rho,K}(\sigma)+\frac14\right]*<
+
2\sum*{j\ge1}
\left[A_{\rho,K}(\sigma+j)+\frac14\right]_<.
}
\tag{1.1}
]

The sum is finite because (A_{\rho,K}) vanishes at and beyond (K).

## Uniform Shifted Shell-Tail Theorem

The desired theorem is

[
\boxed{
\mathcal T^<*{\rho,K}(\sigma)
\le
2\int*\sigma^K A_{\rho,K}(z),dz.
}
\tag{ST}
]

There are three useful levels of this theorem.

### Minimum theorem needed for general (d\ge3)

It is enough to prove (ST) for

[
\sigma\in\frac12\mathbb Z,\qquad
\sigma\ge\frac12,
\qquad
K>\frac{\pi}{1-\rho}.
\tag{ST}_{3+}
]

The reasons are:

* every Bessel order occurring in (d\ge3) belongs to the positive half-lattice;
* the lowest possible shift is (1/2), occurring in (d=3);
* below (K=\pi/(1-\rho)), the higher-dimensional shell count is zero by the one-dimensional Dirichlet comparison.

This restricted theorem avoids the singular planar shift (\sigma=0).

### Clean theorem to publish

The preferable statement is (ST) for every

[
\sigma\in\frac12\mathbb Z_{\ge0}
]

and every (K>0). This removes the no-mode qualification from the lattice theorem.

### Strong optional version

One may try to prove the stronger inequality

[
\left\lfloor A_{\rho,K}(\sigma)+\frac14\right\rfloor
+
2\sum_{j\ge1}
\left\lfloor A_{\rho,K}(\sigma+j)+\frac14\right\rfloor
\le
2\int_\sigma^K A_{\rho,K}(z),dz.
\tag{ST}^{+}
]

This is stronger at integral proxy walls. Preliminary numerical stress tests on integer and half-integer shifts found no counterexample to this stronger form, but that is only heuristic evidence. The proof program should target the strict form first; the ordinary-floor strengthening should not be allowed to delay the general-dimensional theorem.

---

# 2. Exact dimension lifting once (ST) is available

Let

[
a_d:=\frac d2-1,
\qquad
\nu_{\ell,d}=\ell+a_d,
]

and let

[
\kappa_{d,\ell}
===============

## \binom{\ell+d-1}{d-1}

\binom{\ell+d-3}{d-1}
]

be the dimension of the spherical harmonics of degree (\ell) on (S^{d-1}).

The separated radial operator is

[
-\frac{d^2}{dr^2}
+
\frac{\nu_{\ell,d}^2-\frac14}{r^2},
]

with multiplicity (\kappa_{d,\ell}).

Because the existing phase estimate is valid for every real order, the same argument as in the current (d=3) paper gives

[
N_D(A_{\rho,1}^{(d)},K^2)
\le
P_d^<(\rho,K),
\tag{2.1}
]

where

[
P_d^<(\rho,K)
=============

\sum_{\ell\ge0}
\kappa_{d,\ell}
\left[
A_{\rho,K}(\ell+a_d)+\frac14
\right]_<.
\tag{2.2}
]

No dimension-specific phase theorem is needed.

## 2.1 Exact multiplicity decomposition

Put

[
q_\ell
======

\left[
A_{\rho,K}(\ell+a_d)+\frac14
\right]_<.
]

For (d\ge3), define

[
c_{d,n}
=======

\binom{n+d-3}{d-3}.
]

The generating functions are

[
\sum_{\ell\ge0}\kappa_{d,\ell}s^\ell
====================================

\frac{1+s}{(1-s)^{d-1}},
]

[
1+2\sum_{j\ge1}s^j
==================

\frac{1+s}{1-s},
]

and

[
\sum_{n\ge0}c_{d,n}s^n
======================

\frac1{(1-s)^{d-2}}.
]

Consequently,

[
\frac{1+s}{(1-s)^{d-1}}
=======================

\left(
1+2\sum_{j\ge1}s^j
\right)
\left(
\sum_{n\ge0}c_{d,n}s^n
\right).
]

Coefficient comparison gives

[
\kappa_{d,\ell}
===============

c_{d,\ell}
+
2\sum_{n=0}^{\ell-1}c_{d,n}.
\tag{2.3}
]

Therefore

[
\boxed{
P_d^<(\rho,K)
=============

\sum_{n\ge0}
c_{d,n},
\mathcal T^<_{\rho,K}(a_d+n).
}
\tag{2.4}
]

This is exactly the shell analogue of FLPS’s dimension-reduction identity for balls. Their proof attaches binomial weights to entire shifted two-dimensional tails rather than to individual angular samples. 

For illustration:

[
\begin{aligned}
d=3:\quad&
c_{3,n}=1,
&
\kappa_{3,\ell}=2\ell+1;\
d=4:\quad&
c_{4,n}=n+1,
&
\kappa_{4,\ell}=(\ell+1)^2;\
d=5:\quad&
c_{5,n}=\frac{(n+1)(n+2)}2.
\end{aligned}
]

## 2.2 Applying the shifted-tail theorem

Assuming (ST),

[
P_d^<
\le
2\sum_{n\ge0}
c_{d,n}
\int_{a_d+n}^{K}A_{\rho,K}(z),dz.
]

Interchanging the finite sum and integral gives

[
P_d^<
\le
2\int_0^K f_d(z)A_{\rho,K}(z),dz,
\tag{2.5}
]

where

[
f_d(z)
======

\sum_{\substack{n\ge0\a_d+n\le z}}c_{d,n}.
]

By the hockey-stick identity,

[
f_d(z)
======

\begin{cases}
0,&z<a_d,[1mm]
\displaystyle
\binom{\lfloor z-a_d\rfloor+d-2}{d-2},
&z\ge a_d.
\end{cases}
\tag{2.6}
]

Let

[
F_d(z)=\int_0^z f_d(t),dt.
]

FLPS prove the polynomial majorization

[
\boxed{
F_d(z)\le\frac{z^{d-1}}{(d-1)!}.
}
\tag{2.7}
]

Their proof uses the exact piecewise-polynomial form of (F_d) and an arithmetic–geometric mean inequality.

Because (A_{\rho,K}) is decreasing and (A_{\rho,K}(K)=0),

[
2\int_0^K f_d A_{\rho,K}
========================

-2\int_0^K F_d(z)A_{\rho,K}'(z),dz.
]

Using (2.7),

[
\begin{aligned}
2\int_0^K f_d A_{\rho,K}
&\le
-\frac{2}{(d-1)!}
\int_0^K
z^{d-1}A_{\rho,K}'(z),dz\
&=
\frac{2}{(d-2)!}
\int_0^K
z^{d-2}A_{\rho,K}(z),dz.
\end{aligned}
\tag{2.8}
]

The final moment is exact:

[
\boxed{
\frac{2}{(d-2)!}
\int_0^K
z^{d-2}A_{\rho,K}(z),dz
=======================

\frac{1-\rho^d}
{2^d\Gamma(\frac d2+1)^2}
K^d.
}
\tag{2.9}
]

Since

[
L_d|A_{\rho,1}^{(d)}|
=====================

\frac{1-\rho^d}
{2^d\Gamma(\frac d2+1)^2},
]

equations (2.1)–(2.9) prove

[
N_D(A_{\rho,1}^{(d)},K^2)
\le
L_d|A_{\rho,1}^{(d)}|K^d.
]

Thus:

[
\boxed{
\text{After (ST), the all-dimensional proof is approximately five pages.}
}
]

---

# 3. What is already known toward (ST)

An earlier version of the shell manuscript already contained the correct (d=3) shifted-tail scaffold:

[
T_r
===

\left\lfloor A(x_r)+\frac14\right\rfloor
+
2\sum_{j\ge1}
\left\lfloor A(x_r+j)+\frac14\right\rfloor,
\qquad x_r=r+\frac12,
]

and proved that individual bounds

[
T_r\le2\int_{x_r}^K A(z),dz
]

would imply the three-dimensional Weyl bound. 

That earlier argument already proves two useful partial facts.

1. **Tails starting at or above the inner interface** are controlled by the FLPS convex shifted-floor theorem.

2. **Tails below the interface** can be controlled in a small-hole parameter range by splitting the action into a concave prefix and a convex ball suffix.

The current project therefore does not start from zero. The missing step is to replace the small-hole restriction by a global, action-specific argument.

---

# 4. Geometry of the difficult tail

Differentiate the shell action. Put

[
q(z):=-A_{\rho,K}'(z).
]

Then

[
q(z)
====

\frac1\pi
\begin{cases}
\displaystyle
\arccos\frac zK-\arccos\frac z\mu,
&0<z<\mu,[2mm]
\displaystyle
\arccos\frac zK,
&\mu\le z<K.
\end{cases}
\tag{4.1}
]

Moreover,

[
q'(z)>0\quad(0<z<\mu),
\qquad
q'(z)<0\quad(\mu<z<K),
]

and

[
0\le q(z)\le q(\mu)=\frac{\arccos\rho}{\pi}\le\frac12.
\tag{4.2}
]

Thus:

* (A) is concave on ((0,\mu));
* (A) is convex on ((\mu,K));
* (A) and (A') match continuously at (\mu);
* the slope magnitude has one maximum.

If the shift satisfies (\sigma\ge\mu), then

[
A(z)=G_K(z)\qquad(z\ge\sigma),
]

and the tail is exactly a shifted ball tail. FLPS’s theorem applies because (G_K(\sigma+t)) is nonnegative, decreasing, convex and (1/2)-Lipschitz. Their theorem gives the shifted floor count directly from the area. 

Therefore the only unresolved region is

[
\boxed{\sigma<\mu.}
]

A generic theorem for every decreasing, (1/2)-Lipschitz, concave-then-convex function should not be pursued: long plateau-and-taper examples violate such a statement. The proof must exploit the exact shell identities (4.1), the matching at (\mu), and the relation

[
A(z)=\int_z^K q(u),du.
]

---

# 5. Primary route: matched concave–convex floor reserves

This is the route closest to existing FLPS and annulus technology.

## 5.1 Exact integer-interface decomposition

Fix a difficult shift (\sigma<\mu), and set

[
n=\lfloor\mu-\sigma\rfloor,
\qquad
q_0=\sigma+n,
\qquad
\eta=\mu-q_0\in[0,1).
]

Thus

[
q_0\le\mu<q_0+1.
]

Let

[
B=\lceil K-\sigma\rceil,
\qquad
g(t)=A_{\rho,K}(\sigma+t),
]

using zero extension after (K).

For the ordinary-floor form,

[
\frac12\mathcal T_{\rho,K}^{\rm fl}(\sigma)
===========================================

\mathbf T!\left(g+\frac14;0,B\right),
\tag{5.1}
]

where (\mathbf T) is the trapezoidal floor sum.

Split at the last grid point before the interface:

[
\mathbf T!\left(g+\frac14;0,B\right)
====================================

\mathbf T!\left(g+\frac14;0,n\right)
+
\mathbf T!\left(g+\frac14;n,B\right).
]

On the suffix, use

[
A_{\rho,K}\le G_K.
]

This gives

[
\frac12\mathcal T_{\rho,K}^{\rm fl}(\sigma)
\le
\mathbf T!\left(A+\frac14;\sigma,q_0\right)
+
\mathbf T!\left(G_K+\frac14;q_0,K\right).
\tag{5.2}
]

Define the exact reserves

[
R_{\rm in}
:=
\int_\sigma^{q_0}A(z),dz
+\frac n4
---------

\mathbf T!\left(A+\frac14;\sigma,q_0\right),
\tag{5.3}
]

and

[
R_{\rm out}
:=
\int_{q_0}^{K}G_K(z),dz
-----------------------

\mathbf T!\left(G_K+\frac14;q_0,K\right).
\tag{5.4}
]

The only integral mismatch is

[
\delta(q_0,\mu)
:=
\int_{q_0}^{\mu}G_\mu(z),dz.
\tag{5.5}
]

Equation (5.2) will imply (ST) once one proves

[
\boxed{
R_{\rm in}+R_{\rm out}
\ge
\frac n4+\delta(q_0,\mu).
}
\tag{5.6}
]

This is the precise scalar target of the split-interface route.

## 5.2 Keep the mismatch exact

Write

[
\vartheta=\arccos\frac{q_0}{\mu}.
]

Direct integration gives

[
\boxed{
\delta(q_0,\mu)
===============

\frac{\mu^2}{\pi}
\left[
\frac{\vartheta(2+\cos2\vartheta)}4
-----------------------------------

\frac{3\sin2\vartheta}{8}
\right].
}
\tag{5.7}
]

The turning estimate also gives

[
0\le
\delta(q_0,\mu)
\le
\frac{2(\mu-q_0)^{5/2}}{15\sqrt\mu}.
\tag{5.8}
]

Since (0\le\mu-q_0<1), the mismatch becomes small when (\mu) is large. The earlier small-hole proof lost too much by replacing this exact local quantity by a uniform constant.

## 5.3 Quantitative concave-prefix theorem

The annulus paper supplies two relevant ingredients:

* the basic trapezoidal bound for concave functions;
* a strict reserve after the first floor shelf, depending on the Lipschitz constant. 

The new lemma should retain the reserve from **every horizontal shelf**, not only the first one.

A suitable target is:

> **Concave shelf-reserve lemma.**
> Let (h) be decreasing and concave on an integer interval, with
> [
> 0\le-h'\le c<1.
> ]
> Decompose the samples according to the ordinary or strict floor levels of (h+1/4). Then
> [
> \int h+\frac{\text{length}}4-\mathbf T(h+1/4)
> ]
> is bounded below by an explicit sum of shelf-length payments.

The proof should follow the inverse-shelf decomposition used in the annulus floor-sum theorem, but preserve every positive term. The existing theorem discards most of this information because it only needed one regional estimate. 

For the shell action, use

[
c=c_\rho:=\frac{\arccos\rho}{\pi}.
]

The required output is a lower bound for (R_{\rm in}) in terms of:

[
n,\qquad c_\rho,\qquad
A(\sigma),\qquad
A(q_0),\qquad
\eta.
]

## 5.4 Quantitative shifted-ball reserve

FLPS proves only

[
R_{\rm out}\ge0,
]

although their proof contains more slack whenever the shifted ball action is nonzero.

The annulus paper already extracts one particular quantitative reserve: if the ball action becomes (1/3)-Lipschitz after a point (z_*), then the trapezoidal sum gains a payment proportional to

[
\left\lfloor G_K(z_*)\right\rfloor.
]

To obtain a global shell theorem, generalize this to a variable slope threshold.

For

[
0<c<\frac12,
]

the condition

[
|G_K'(z)|\le c
]

is equivalent to

[
z\ge K\cos(\pi c).
]

At that point,

[
G_K(K\cos(\pi c))
=================

\frac K\pi
\left(
\sin(\pi c)-\pi c\cos(\pi c)
\right).
\tag{5.9}
]

The desired quantitative theorem has the form

[
R_{\rm out}
\ge
b(c)
\left\lfloor
\frac K\pi
\bigl(
\sin(\pi c)-\pi c\cos(\pi c)
\bigr)
\right\rfloor
+
R_{\rm end},
\tag{5.10}
]

where (b(c)>0) is obtained by re-running the FLPS “bad lattice point” argument. It should satisfy

[
b!\left(\frac12\right)=0,
\qquad
b!\left(\frac13\right)=\frac14
]

at the half-tail scale.

Do not guess (b(c)). Derive the optimal coefficient from the horizontal shelf proof.

## 5.5 Natural ratio split

The interface geometry suggests a non-empirical split at

[
\rho=\frac12.
]

### Region (\rho\ge1/2)

Here

[
c_\rho=\frac{\arccos\rho}{\pi}\le\frac13.
]

The entire shell action is globally (1/3)-Lipschitz. The concave-prefix reserve should be strongest in this region. The first objective is a small-slope mixed-curvature theorem covering all tails when (\rho\ge1/2).

### Region (0<\rho\le1/2)

Here

[
\mu\le\frac K2.
]

Every outer suffix beginning before the interface contains the interval ([K/2,K]), so the already-known (1/3)-slope ball reserve at (K/2) is available. The prefix shelf reserve must pay the remaining (n/4) cost.

This split is more promising than carrying the current empirical seam (39/50) into the new method.

## 5.6 Fractional-interface upgrade

The mismatch (\delta(q_0,\mu)) arises only because the trapezoidal sum was split at the integer point (q_0), rather than at the true interface (\mu).

If (5.6) remains awkward, the conceptual improvement is a **fractional-interface trapezoidal theorem**.

Let

[
\mu=q_0+\eta,\qquad0\le\eta<1.
]

Assign (\eta)-dependent endpoint weights to the sample at (q_0) and the sample at (q_0+1), so that

[
\mathcal S_{\rm in}^{(\eta)}
+
\mathcal S_{\rm out}^{(\eta)}
=============================

\frac12\mathcal T_{\rho,K}(\sigma)
]

exactly, while the corresponding integrals split exactly at (\mu). The desired paired estimates are

[
\mathcal S_{\rm in}^{(\eta)}
\le
\int_\sigma^\mu A(z),dz+\mathcal I_\eta,
]

[
\mathcal S_{\rm out}^{(\eta)}
\le
\int_\mu^K G_K(z),dz-\mathcal I_\eta.
]

The interface payment (\mathcal I_\eta) cancels. This would eliminate the artificial mismatch (5.5) entirely.

The recommended order is:

1. attempt the simpler integer split and exact reserve inequality (5.6);
2. introduce the fractional-interface theorem only if the final scalar inequality remains unnecessarily complicated.

---

# 6. A more local formulation: the cell-deficit recurrence

There is an exact recurrence which may make the preceding reserve argument much cleaner.

For a fixed shift class—integers or half-integers—put

[
Q_m
===

\left[
A(\sigma+m)+\frac14
\right]_<,
]

and define the tail deficit

[
D_m
===

## 2\int_{\sigma+m}^{K}A(z),dz

\left(
Q_m+2\sum_{j\ge1}Q_{m+j}
\right).
\tag{6.1}
]

Then

[
\boxed{
D_m-D_{m+1}
===========

## 2\int_{\sigma+m}^{\sigma+m+1}A(z),dz

Q_m-Q_{m+1}.
}
\tag{6.2}
]

Thus the entire theorem is a statement about cumulative one-cell deficits.

Define the strict remainder

[
e_m
===

A(\sigma+m)+\frac14-Q_m
\in(0,1].
]

Then

[
Q_m
===

A(\sigma+m)+\frac14-e_m,
]

and (6.2) becomes

[
D_m-D_{m+1}
===========

C_m-\frac12+e_m+e_{m+1},
\tag{6.3}
]

where

[
C_m
===

## 2\int_{\sigma+m}^{\sigma+m+1}A(z),dz

A(\sigma+m)-A(\sigma+m+1).
\tag{6.4}
]

On a fully inner cell, (A) is concave and

[
C_m
===

-\int_0^1
u(1-u)A''(\sigma+m+u),du
\ge0.
\tag{6.5}
]

Moreover,

[
-A''(z)
=======

\frac1\pi
\left(
\frac1{\sqrt{\mu^2-z^2}}
------------------------

\frac1{\sqrt{K^2-z^2}}
\right)
\qquad(z<\mu).
\tag{6.6}
]

A cell can be negative only when

[
e_m+e_{m+1}
<
\frac12-C_m.
\tag{6.7}
]

Because the action drops by at most (1/2) per unit interval, a negative cell cannot contain a floor drop. At the next floor drop the strict remainder jumps close to one, producing a positive cell. This suggests a shell-specific **bad-cell pairing lemma**:

> Every negative inner cell can be paired with the next floor-drop cell, and the increasing inner slope together with the curvature reserve (6.6) makes the paired sum nonnegative.

This is the most concrete combinatorial subproblem in the program. It is a refinement of the FLPS “bad point” mechanism, but now applied to one-cell deficits across a single curvature switch.

The cell formulation has several advantages:

* it automatically respects strict proxy walls;
* only the two shift classes (0) and (1/2\pmod1) occur;
* the cell straddling (\mu) is isolated;
* the outer convex tail supplies a known nonnegative terminal reserve;
* there is no need for a global dimension-dependent scalar polynomial.

I would make this the first analytic attack within the primary route.

---

# 7. Independent route: inverse-action two-sawtooth identity

The current (d=3) proof shows that a retained-remainder identity can be substantially stronger than separate floor-sum estimates. Its tangent-envelope treatment of the shifted radial sawtooth is the relevant template. 

For a fixed shift (\sigma<K), set

[
S=A_{\rho,K}(\sigma),
]

and let (R) be the inverse of (A_{\rho,K}). Define

[
y(t)=R(t)-\sigma,\qquad0\le t\le S.
]

Let

[
x_n=n-\frac14.
]

Transposing the radial floors gives the exact identity

[
\boxed{
\mathcal T^<_{\rho,K}(\sigma)
=============================

\sum_{x_n<S}
H(y(x_n)),
}
\tag{7.1}
]

where

[
H(y)=2\lceil y\rceil-1,\qquad y>0.
\tag{7.2}
]

The continuous area is

[
\boxed{
2\int_\sigma^K A(z),dz
======================

2\int_0^S y(t),dt.
}
\tag{7.3}
]

Hence the shifted-tail theorem is equivalent to

[
2\int_0^S y(t),dt
-----------------

\sum_{x_n<S}H(y(x_n))
\ge0.
\tag{7.4}
]

Decompose this as

[
\begin{aligned}
&2\left[
\int_0^S y(t),dt
----------------

\sum_{x_n<S}y(x_n)
\right]\
&\quad-
\sum_{x_n<S}
\left(
H(y(x_n))-2y(x_n)
\right).
\end{aligned}
\tag{7.5}
]

The first line is a radial quadrature error at the shift (n-1/4). The second is an angular centered-sawtooth error.

The objective is to derive a **joint Stieltjes identity** for (7.5), rather than estimating its two terms independently.

The associated density is

[
g_\sigma(t)
===========

# -\frac{d}{dt}\bigl(2y(t)\bigr)

\frac{2}{q(R(t))}.
\tag{7.6}
]

For (\sigma<\mu), it decreases before the action interface and increases after it. Crucially, for the higher-dimensional shifts

[
\sigma\ge\frac12,
]

the terminal value of (g_\sigma) is finite. The singular endpoint occurs only at the optional planar shift (\sigma=0).

This suggests the following modules.

1. Derive the exact two-sawtooth Stieltjes formula for (7.5).

2. Compute the primitive of the combined periodic kernel.

3. Find a tangent envelope analogous to the present

   [
   L_\sharp(t)
   ===========

   \begin{cases}
   t^2/2,&t\le1/4,\
   t/4-1/32,&t\ge1/4,
   \end{cases}
   ]

   but adapted to the combined radial and angular sawteeth.

4. Use the decreasing–increasing structure of (g_\sigma) to obtain a single interface payment.

5. Treat (\sigma=0) separately only after the positive-shift theorem is complete.

This route has greater conceptual potential than the split-floor route. It may produce the cleanest final paper, but deriving the correct combined primitive is the main technical uncertainty.

---

# 8. Backup route: deform the inner radius

There is a third, independent formulation.

For fixed (K) and (\sigma), begin with (\mu\le\sigma). Then the entire shifted tail is a ball tail, already controlled by FLPS.

Increase (\mu). For (z<\mu),

[
\frac{\partial G_\mu(z)}{\partial\mu}
=====================================

\frac1\pi
\sqrt{1-\left(\frac z\mu\right)^2}.
\tag{8.1}
]

Therefore, between discrete floor events,

[
\frac{d}{d\mu}
\left(
2\int_\sigma^K A_{\rho,K}(z),dz
\right)
=======

-\frac2\pi
\int_\sigma^\mu
\sqrt{1-\left(\frac z\mu\right)^2},dz.
\tag{8.2}
]

The shifted floor count remains constant between events and drops by weight (1) or (2) when

[
A_{\rho,K}(\sigma+j)+\frac14
]

crosses an integer.

The target becomes an event-to-event lemma:

> Before the continuous area can lose one unit of the relevant lattice weight, one of the discrete samples must cross its next floor wall.

The derivative kernel

[
z\longmapsto
\sqrt{1-(z/\mu)^2}
]

is explicit, decreasing and concave. The annulus concave floor-sum estimates are therefore directly relevant.

This deformation route is less likely to be the shortest proof, but it is valuable for:

* explaining why the theorem should be true;
* locating the critical event configurations;
* supplying monotonicity lemmas for the primary proof;
* producing an independent audit.

---

# 9. Fallback if individual tails are not always easy

The exact per-tail theorem is the preferred result. However, the algebraic lifting only requires a weighted aggregate.

Suppose one obtains

[
\mathcal T^<*{\rho,K}(a_d+n)
\le
2\int*{a_d+n}^K A(z),dz
+
\varepsilon_n.
\tag{9.1}
]

Then

[
P_d^<
\le
2\int_0^K f_d(z)A(z),dz
+
\sum_{n\ge0}c_{d,n}\varepsilon_n.
]

The FLPS primitive comparison itself has a positive reserve

[
\boxed{
\mathcal R_d
============

2\int_0^K
\left[
\frac{z^{d-1}}{(d-1)!}
----------------------

F_d(z)
\right]
(-A'(z)),dz.
}
\tag{9.2}
]

Therefore it is enough to prove

[
\sum_{n\ge0}
c_{d,n}\varepsilon_n
\le
\mathcal R_d.
\tag{9.3}
]

The old (d=3) shifted-tail scaffold explicitly recognized that an aggregate cancellation theorem is sufficient even if individual tail bounds are unavailable. 

This should remain a fallback, not the first target. A clean per-tail theorem is dimension-free and conceptually stronger; an aggregate theorem risks reintroducing dimension-dependent bookkeeping.

---

# 10. Recommended sequence of work

| Work package                   | Mathematical output                                                        | Completion criterion                                                                        |
| ------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **WP1: algebraic lifting**     | General-(d) separation, exact identity (2.4), primitive lift (2.7)–(2.9)   | A self-contained 5–7 page note with every strict wall checked                               |
| **WP2: exact tail laboratory** | Evaluator for (\mathcal T_\sigma), exact action integral, event surfaces   | Exhaustive stress tests on integer and half-integer shifts; no numerical premise in theorem |
| **WP3: easy tail regions**     | (\sigma\ge\mu); no-mode region; one interface cell (0<\mu-\sigma<1)        | Fully analytic statements including equality faces                                          |
| **WP4: inner-tail theorem**    | Cell-deficit pairing or matched reserve theorem for arbitrary (\mu-\sigma) | (ST) for (\sigma\ge1/2) on both shift grids                                                 |
| **WP5: all-(d) assembly**      | Pólya for every shell in every (d\ge3)                                     | No dimension-specific finite tables                                                         |
| **WP6: planar enhancement**    | Extend (ST) to (\sigma=0)                                                  | New purely analytic proof of planar annulus Pólya                                           |
| **WP7: manuscript rebuild**    | General-dimensional paper centered on shifted tails                        | Current (d=3) machinery removed from the live proof                                         |

## The first nontrivial milestone

Do not begin with arbitrary (\mu-\sigma). First prove

[
0<\mu-\sigma<1.
\tag{10.1}
]

In this regime there is only one cell intersecting the concave branch. The outer convex theorem controls all later cells. A successful one-cell proof should reveal the correct interface payment and determine whether the integer-split or inverse-action route is superior.

## The next milestone

Prove the theorem separately in the two natural ratio regions:

[
\rho\ge\frac12
\quad\text{and}\quad
0<\rho\le\frac12.
]

This uses, respectively:

* the global (1/3)-slope cap;
* the guaranteed outer-ball reserve beyond (K/2).

Only after those two mechanisms are understood should they be compressed into a uniform theorem.

---

# 11. Equality walls that must be built in from the start

The following faces should be explicit theorem clauses, not handled by continuity afterward:

[
A(\sigma+j)+\frac14\in\mathbb N,
]

[
\sigma+j=\mu,
]

[
\sigma+j=K,
]

[
\mu-\sigma\in\mathbb N,
]

[
K=\frac{\pi}{1-\rho}.
]

The strict bracket is advantageous:

[
[m]_< = m-1
\qquad(m\in\mathbb N).
]

It supplies an extra unit at an integral proxy wall and avoids the most delicate floor discontinuity. The ordinary-floor theorem can be added later as a strengthening.

---

# 12. Final paper structure

A successful general-dimensional manuscript should have the following form.

## Section 1: Main theorem and method

State

[
N_D(A_{r,R}^{(d)},\Lambda)
\le
L_d|A_{r,R}^{(d)}|\Lambda^{d/2},
\qquad d\ge3.
]

State the shifted shell-tail theorem as the principal new analytic result.

## Section 2: Dimension-independent spectral reduction

Include:

* spherical-harmonic separation;
* Bessel determinant;
* strict phase enumeration;
* real-order phase enclosure;
* shell-action proxy.

Most of this is already present in the current paper.

## Section 3: The shifted shell-tail theorem

This should be the conceptual center of the paper:

* action geometry;
* convex outer tails;
* interface-cell lemma;
* concave-prefix reserve or inverse-action identity;
* global closure.

## Section 4: Positive dimension lifting

Prove:

* multiplicity generating-function identity;
* shifted-tail decomposition;
* FLPS primitive estimate;
* exact Weyl moment.

## Section 5: Spectral theorem

Combine:

* no-mode region;
* shifted-tail theorem;
* dilation.

## Appendix A: Planar case

Two possibilities:

* cite the existing planar-annulus theorem and explain why (\sigma=0) is exceptional;
* or include the new (\sigma=0) proof if completed.

## Appendix B: Walls and regression checks

Keep symbolic or interval computations only as independent verification.

The existing retained-remainder (d=3) proof should be frozen as a validated fallback. It should not coexist as a second full live proof in the final general-dimensional manuscript. Its main conceptual contribution to the new paper is the idea that periodic rounding errors should be retained and coupled rather than bounded separately.

---

# 13. Decision criteria

Proceed with the all-dimensional paper if the following are achieved:

1. the positive-shift theorem is proved on both grids
   [
   \mathbb N
   \quad\text{and}\quad
   \mathbb N+\frac12;
   ]

2. the proof uses one common interface mechanism;

3. no dimension-dependent event table is needed;

4. (d=4) and (d=5) follow by the same three-page lifting argument;

5. every equality wall is handled directly.

Switch to the aggregate-reserve fallback if only a small, explicitly controlled family of tails remains unresolved.

Return to a direct (d=4) extension only if the shifted-tail theorem requires a large new staircase or many parameter-specific cases. In that event, the strategy would no longer be delivering the conceptual gain that justifies choosing it.

---

# Bottom line

The research program should be centered on the theorem

[
\boxed{
\mathcal T^<*{\rho,K}(\sigma)
\le
2\int*\sigma^K A_{\rho,K}(z),dz,
\qquad
\sigma\in\frac12\mathbb Z,\ \sigma\ge\frac12.
}
]

Everything after this inequality is a positive combinatorial lift modeled on FLPS’s ball argument. The current project strategy already identifies general (d) as the natural next shell milestone; the shifted-tail theorem is the mechanism that can make that extension conceptual rather than dimension-by-dimension. 

The immediate mathematical task is therefore to write a standalone “Shifted Shell Tails” note and attack, in order:

[
\sigma\ge\mu,
\qquad
0<\mu-\sigma<1,
\qquad
\rho\ge\frac12,
\qquad
\rho\le\frac12,
\qquad
\text{arbitrary positive half-lattice shift}.
]
