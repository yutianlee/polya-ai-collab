# Spherical-Shell Non-Tiling Clean-Room Proof

Date: 2026-07-15

## Verdict

**PASS. First unsupported implication: none.**

For every fixed $0<r<R$, the open spherical shell

$$
S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}
$$

cannot tile $\mathbb R^3$ by congruent copies with pairwise-disjoint
interiors and coverage up to a Lebesgue-null set. Consequently it cannot
tile by exact coverage either, whether exact coverage is phrased for the
open copies or for their closures.

This is a clean-room geometric reconstruction from the stated claim and
elementary Euclidean measure and topology. I did not inspect an incumbent
route, any other Round 21 exploration, review, or judge, Git history or
diffs, or another agent's work before reaching this verdict.

## 1. Normalize and reduce rigid motions to translations

Apply the dilation $D(x)=x/R$ and put $\alpha=r/R\in(0,1)$. A purported
tiling by $S_{r,R}$ would become one by

$$
T=S_{\alpha,1}=\{x\in\mathbb R^3:\alpha<|x|<1\}.
$$

Dilation preserves disjointness, exact coverage, and null-set coverage;
Lebesgue measure is merely multiplied by $R^{-3}$. It therefore suffices to
rule out a tiling by $T$.

Every Euclidean isometry has the form $x\mapsto Qx+a$ with $Q$ orthogonal.
Because $T$ is radial, $Q(T)=T$. Hence every congruent copy is exactly a
translate

$$
T_a=a+T=\{x:\alpha<|x-a|<1\}.
$$

Reflections cause no additional case. If two indexed copies have the same
center, they are the same nonempty open set and their interiors are not
disjoint. Thus duplicate copies may be removed, and a putative family is
represented by a set of distinct centers $A\subset\mathbb R^3$.

## 2. Uniform separation, local finiteness, and countability

Let $e$ be a unit vector and set

$$
c=\frac{1+\alpha}{2}e,
\qquad
\delta=\frac{1-\alpha}{2}.
$$

The open ball $B(c,\delta)$ lies in $T$: for $x$ in this ball,

$$
\alpha=|c|-\delta<|x|<|c|+\delta=1.
$$

Therefore $T_a$ contains $B(a+c,\delta)$. If two distinct centers satisfied
$|a-b|<2\delta=1-\alpha$, these two contained balls would overlap, forcing
$T_a\cap T_b\ne\varnothing$. Pairwise-disjoint interiors consequently imply

$$
|a-b|\geq1-\alpha
\qquad(a\ne b).
\tag{2.1}
$$

A bounded subset of $\mathbb R^3$ contains only finitely many points with
the fixed positive separation (2.1): disjoint balls of radius
$(1-\alpha)/3$ about those points all lie in one bounded enlargement and
have the same positive volume. Thus $A$ is locally finite. Since

$$
A=\bigcup_{m=1}^{\infty}\bigl(A\cap\overline B(0,m)\bigr)
$$

is a countable union of finite sets, $A$ is countable as well. This also
independently rules out an uncountable hidden family of tiles.

Countability handles the closure version of the tiling convention. Each
$\partial T_a$ is the union of two spheres and has three-dimensional
Lebesgue measure zero. Hence $\bigcup_{a\in A}\partial T_a$ is null. If the
closed shells covered exactly, or covered up to a null set, then their open
interiors $T_a$ would still cover up to a null set. It is therefore enough
to contradict

$$
\left|\mathbb R^3\setminus\bigcup_{a\in A}T_a\right|=0.
\tag{2.2}
$$

Exact coverage by the open copies is already a special case of (2.2).

## 3. Every point of one outer sphere is approached from another interior

Choose any tile, translate the whole configuration, and call it $T_0$.
Let

$$
\Sigma=\{x:|x|=1\}
$$

be its outer boundary sphere. Fix an arbitrary $p\in\Sigma$. For every
$n\geq1$, the exterior neighborhood

$$
U_n=B(p,1/n)\cap\{x:|x|>1\}
$$

is a nonempty open set, hence has positive volume. By (2.2), it cannot be
contained in the null uncovered set. We may choose

$$
x_n\in U_n\cap\bigcup_{a\in A}T_a.
$$

Then $x_n\to p$. Since $|x_n|>1$, none of these points lies in $T_0$, so
choose $a_n\ne0$ with $x_n\in T_{a_n}$.

For all sufficiently large $n$, $x_n\in B(p,1)$. Since
$|x_n-a_n|<1$, the corresponding centers lie in the bounded ball
$B(p,2)$. Local finiteness makes the set of possible $a_n$ finite. Passing
to a subsequence gives one fixed center $a\ne0$ such that
$x_{n_j}\in T_a$ for every $j$. Therefore

$$
p\in\overline{T_a}.
\tag{3.1}
$$

The point $p$ cannot be in the interior $T_a$. If it were, some ball
$B(p,\varepsilon)$ would lie in $T_a$. Choose

$$
0<t<\min\{\varepsilon,1-\alpha\}.
$$

Then $(1-t)p$ belongs to $T_0\cap B(p,\varepsilon)$ and hence also to
$T_a$, contradicting the disjointness of the two interiors. Together with
(3.1), this proves

$$
p\in\partial T_a,
\qquad a\ne0.
\tag{3.2}
$$

This explicitly rules out the possible but incorrect inference that the
limit point might lie in the neighboring tile's interior.

## 4. Only finitely many neighboring boundary spheres are available

The boundary of a translated shell is

$$
\partial T_a
=\{x:|x-a|=\alpha\}\cup\{x:|x-a|=1\}.
\tag{4.1}
$$

If $p\in\Sigma\cap\partial T_a$, then $|p-a|$ is either $\alpha$ or $1$,
so $|a|\leq2$. By local finiteness,

$$
F=(A\cap\overline B(0,2))\setminus\{0\}
$$

is finite. Since $p\in\Sigma$ was arbitrary, (3.2)--(4.1) imply the finite
cover

$$
\Sigma\subset
\bigcup_{a\in F}
\left(
\{x:|x-a|=\alpha\}\cup\{x:|x-a|=1\}
\right).
\tag{4.2}
$$

## 5. Distinct spheres cannot give the finite cover (4.2)

Fix $a\in F$ and $s\in\{\alpha,1\}$. A point in the intersection of
$\Sigma$ with the sphere $\{x:|x-a|=s\}$ satisfies

$$
|x|^2=1,
\qquad
|x-a|^2=s^2,
$$

and subtraction gives

$$
2a\mathbin\cdot x=|a|^2+1-s^2.
\tag{5.1}
$$

Because $a\ne0$, (5.1) is a genuine plane equation. Its intersection with
$\Sigma$ is empty, a single tangent point, or a circle. In every case it
has zero two-dimensional surface measure on $\Sigma$. A finite union of
such intersections still has zero surface measure, whereas $\Sigma$ has
surface area $4\pi$. It therefore cannot cover $\Sigma$, contradicting
(4.2).

There is no identical-sphere exception hidden here. Two Euclidean spheres
are identical only when both their centers and radii agree. A neighboring
outer sphere could equal $\Sigma$ only if $a=0$, which would be the original
tile or a forbidden duplicate. A neighboring inner sphere could equal
$\Sigma$ only if both $a=0$ and $\alpha=1$, but $0<\alpha<1$. Repeated
neighboring boundary spheres, if any, only remove terms from the finite
union and cannot help it cover $\Sigma$.

This contradiction proves that $S_{\alpha,1}$ does not tile in the stated
sense.

## 6. Scale back and calibrate the conclusion

If $S_{r,R}$ admitted a tiling, dilation by $1/R$ would produce the
forbidden tiling by $S_{r/R,1}$. Null sets remain null under this invertible
linear scaling, and exact coverage remains exact. Thus the result holds for
every $0<r<R$.

Under the usual Pólya terminology in which a bounded Euclidean domain is a
tiling domain only if congruent rigid-motion copies tile space with
disjoint interiors up to null boundaries, this proves that every genuine
three-dimensional spherical shell is a **non-tiling domain**. The argument
already allows every rigid motion, because radial symmetry reduces them all
to translations.

This report proves geometry only. It does **not** prove the Dirichlet Pólya
spectral inequality for shells, does not promote any spectral theorem or
proof obligation, and does not establish publication novelty or priority.
