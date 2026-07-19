# Source Card: Round 19 Bessel-Zero Bounds

Status: **qualified external first-zero audit plus internal second-zero
proof completed on 2026-07-14**.

This card authorizes exactly

$$
j_{11/2,1}>\frac{17}{2},
\qquad
j_{3/2,2}>\frac{77}{10}.
$$

It does not enlarge the scope of `SRC-LORCH` silently. The first inequality
is a new exact-order specialization of the published Lorch statement. The
second is proved internally from the explicit spherical-Bessel formula and
does not use Lorch.

## Primary sources

1. Lee Lorch, “Some Inequalities for the First Positive Zeros of Bessel
   Functions,” *SIAM Journal on Mathematical Analysis* **24**(3) (1993),
   814–823. Publisher page and abstract:
   [https://epubs.siam.org/doi/10.1137/0524050](https://epubs.siam.org/doi/10.1137/0524050).
2. NIST Digital Library of Mathematical Functions,
   [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3), for

   $$
   \mathsf j_\ell(x)=\sqrt{\frac{\pi}{2x}}J_{\ell+1/2}(x),
   \qquad x>0.
   $$

3. NIST DLMF, [§10.49(i)](https://dlmf.nist.gov/10.49.i), for explicit
   elementary formulas for unmodified spherical Bessel functions. The
   order-one identity used below is also verified directly by substitution,
   so no unexposed theorem hypothesis is needed for the internal argument.

The SIAM abstract identifies $j_{\nu,1}$ as the first positive zero of
$J_\nu$ and states its parameter range as $-1<\nu<\infty$.

## 1. New exact-order Lorch specialization

The publisher abstract states, for $-1<\nu<\infty$,

$$
j_{\nu,1}^2>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}
-2(\nu^2-1).
\tag{L2}
$$

At $\nu=11/2$, the denominator is

$$
1-11+\sqrt{14\cdot22}
=2(\sqrt{77}-5)>0.
$$

The right-hand side of (L2) simplifies exactly to

$$
\frac{1014}{2(\sqrt{77}-5)}-\frac{117}{2}
=\frac{507(\sqrt{77}-1)}{52}.
$$

Comparison with the proposed square is equivalent to

$$
\frac{507(\sqrt{77}-1)}{52}>\frac{289}{4}
\quad\Longleftrightarrow\quad
507\sqrt{77}>4264.
$$

Both sides of the last inequality are positive, and

$$
507^2\cdot77-4264^2=1611077>0.
$$

Therefore

$$
j_{11/2,1}^2>\left(\frac{17}{2}\right)^2.
$$

Because $j_{11/2,1}$ is positive by definition,

$$
\boxed{j_{11/2,1}>\frac{17}{2}}.
\tag{Z1}
$$

This is the only new Lorch specialization authorized by this card.

## 2. Internal proof of the second $J_{3/2}$ zero bound

For $x>0$, the spherical order-one function has the elementary form

$$
\mathsf j_1(x)
=\frac{\sin x-x\cos x}{x^2}.
\tag{E1}
$$

It follows either by specializing the DLMF explicit formula or directly
from $\mathsf j_1=-\frac{d}{dx}(\sin x/x)$. At a zero of the numerator,
$\cos x$ cannot vanish, because then $\sin x=\pm1$. Hence the positive
zeros of $\mathsf j_1$ are exactly the positive solutions of

$$
\tan x=x.
\tag{E2}
$$

Let $f(x)=\tan x-x$. For every integer $n\ge1$, on

$$
I_n=\left(n\pi,n\pi+\frac\pi2\right)
$$

one has

$$
f'(x)=\tan^2x>0,
$$

$f(n\pi)=-n\pi<0$, and $f(x)\to+\infty$ at the right endpoint. Thus
there is exactly one root in each $I_n$. On the complementary half-period
$(n\pi+\pi/2,(n+1)\pi)$, $\tan x<0<x$, so there is no root. On
$(0,\pi/2)$, $\tan x>x$ for $x>0$, so the zero at the origin creates no
positive root there. Consequently the second positive zero is the unique
root in

$$
I_2=\left(2\pi,\frac{5\pi}{2}\right).
$$

Set

$$
x_0=\frac{77}{10},
\qquad
y=\frac{5\pi}{2}-x_0.
$$

The inherited exact enclosure

$$
\frac{333}{106}<\pi<\frac{22}{7}
\tag{P}
$$

gives

$$
2\pi<\frac{44}{7}<\frac{77}{10}<\frac{5\pi}{2},
$$

so $0<y<\pi/2$. Moreover,

$$
y>
\frac{5}{2}\frac{333}{106}-\frac{77}{10}
=\frac{163}{1060}
>\frac{10}{77},
$$

where the final comparison is $163\cdot77=12551>10600$.

For $0<y<\pi/2$, the function $\tan y-y$ has derivative
$\tan^2y>0$ and vanishes at zero. Hence $\tan y>y$, and therefore

$$
\tan x_0
=\cot y
<\frac1y
<\frac{77}{10}=x_0.
$$

Thus $f(x_0)<0$. Since $f$ is strictly increasing on $I_2$, its unique
zero lies strictly to the right of $x_0$. By DLMF 10.47.3, the positive
zeros of $\mathsf j_1$ and $J_{3/2}$ coincide. Therefore

$$
\boxed{j_{3/2,2}>\frac{77}{10}}.
\tag{Z2}
$$

## 3. What transfers to the shell proof

DLMF 10.47.3 has a positive prefactor for $x>0$, so (Z1) is the first
unit-ball Dirichlet frequency bound in angular channel $\ell=5$, and (Z2)
is the second such bound in angular channel $\ell=1$.

The shell application still requires the internal fixed-channel variational
comparison

$$
k^{\mathrm{shell}}_{\ell,n}(\rho)
\ge j_{\ell+1/2,n}.
$$

The accepted proof extends shell radial functions by zero into the inner
ball and applies min–max in the fixed angular subspace. This works for each
min–max index $n$, but it is not supplied by Lorch or DLMF and must remain
labelled internal.

Subject to that already internal comparison, (Z1) excludes the first
$\ell=5$ shell mode through $K=17/2$, and (Z2) excludes the second
$\ell=1$ shell mode through $K=77/10$. Equality is excluded under strict
spectral counting because both zero inequalities are strict.

## 4. Scope exclusions

This card supplies none of the following:

- a shell Bessel cross-product zero bound;
- a global or fixed-channel shell-to-ball domain comparison;
- any zero bound at another new order or radial index;
- an angular or radial multiplicity count;
- a Weyl payment, ratio split, endpoint estimate, or finite certificate;
- a proof of the full Lorch article.

The Lorch article body remains access-controlled in the audited environment.
This is a qualified statement-level use of the formula printed in the
primary publisher abstract, followed by exact algebra at one declared
order. The proof of (Z2) is internal and complete.

## Verdict

**PASS for exactly (Z1) and (Z2); first unsupported implication: none.**
