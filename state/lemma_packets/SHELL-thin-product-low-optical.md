# Lemma Packet: Thin-Shell Product Comparison at Low Optical Width

Obligation to create: SHELL-thin-product-low-optical.

Related parent: SHELL-rho-one-endpoint.

## Exact theorem

Let

$$
\rho=1-\varepsilon,\qquad
0<\varepsilon\le\frac1{100},\qquad
a=\varepsilon K.
$$

For the three-dimensional Dirichlet shell,

$$
\boxed{
0\le a\le\frac{\pi}{4\varepsilon}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

Equivalently, this proves the shell Pólya estimate for

$$
0\le K\le\frac{\pi}{4\varepsilon^2}
$$

whenever $0<\varepsilon\le1/100$.

The proof must use strict spectral counting at every radial and angular wall.

## Exact product majorant

The transformed radial operator is

$$
L_\ell
=
-\frac{d^2}{dr^2}
+\frac{\ell(\ell+1)}{r^2}
\ge
-\frac{d^2}{dr^2}+\ell(\ell+1)
$$

on an interval of length $\varepsilon$. Hence the min--max principle gives

$$
\lambda_{\ell,n}
\ge
\left(\frac{n\pi}{\varepsilon}\right)^2+\ell(\ell+1).
$$

Define

$$
N=\max\left\{0,\left\lceil\frac a\pi\right\rceil-1\right\}.
$$

For $1\le n\le N$, set

$$
b_n=\sqrt{a^2-n^2\pi^2},
\qquad
T_n=\frac{b_n}{\varepsilon},
$$

$$
M_n
=
\#\{\ell\in\mathbb N_0:\ell(\ell+1)<T_n^2\}
=
\left\lceil
\sqrt{T_n^2+\frac14}-\frac12
\right\rceil.
$$

At an angular wall $T_n^2=p(p+1)$, this formula gives $M_n=p$, so the
endpoint channel $\ell=p$ is excluded.

The exact product comparison is

$$
\boxed{
N_D(A_{1-\varepsilon,1},K^2)
\le
\mathcal P_\varepsilon(a)
:=
\sum_{n=1}^{N}M_n^2.
}
$$

The square is the exact angular multiplicity sum

$$
\sum_{\ell=0}^{M_n-1}(2\ell+1)=M_n^2.
$$

## Required analytic bounds

For every $T>0$,

$$
T^2-T\le M(T)^2<T^2+T+1.
$$

Set

$$
S_0(a)=\sum_{n=1}^{N}b_n^2,
\qquad
B(a)=\sum_{n=1}^{N}b_n,
$$

$$
I(a)=\frac{2a^3}{3\pi},
\qquad
D(a)=I(a)-S_0(a).
$$

For $N\ge1$,

$$
\mathcal P_\varepsilon(a)
<
\frac{S_0(a)}{\varepsilon^2}
+\frac{B(a)}{\varepsilon}+N.
$$

For $N=0$, both sides are zero and the non-strict version holds.

For $a>0$, write

$$
\frac a\pi=N+t,\qquad 0<t\le1.
$$

At a radial wall $a=m\pi$, strict counting requires $N=m-1$ and $t=1$.
The exact radial margin is

$$
\boxed{
D(a)
=
\pi^2\left[
\frac{N^2}{2}
+N\left(t^2+\frac16\right)
+\frac{2t^3}{3}
\right].
}
$$

It is continuous and increasing for $a\ge\pi$, and

$$
D(a)\ge\frac{2\pi^2}{3},
\qquad
D(a)\ge\frac{(a-\pi)^2}{2}.
$$

Also,

$$
B(a)\le\frac{a^2}{4},
\qquad
N\le\frac a\pi.
$$

The exact shell Weyl term in $(\varepsilon,a)$ variables is

$$
W_\varepsilon(a)
=
\frac{I(a)}{\varepsilon^2}
\left(1-\varepsilon+\frac{\varepsilon^2}{3}\right).
$$

It is sufficient to prove

$$
\boxed{
D(a)
\ge
\varepsilon\left(
\frac{2a^3}{3\pi}+\frac{a^2}{4}
\right)
+\frac{\varepsilon^2a}{\pi}.
}
$$

Required range split:

1. $0\le a\le\pi$: the strict radial count is zero.
2. $\pi<a\le4\pi$: use $D(a)\ge2\pi^2/3$ and evaluate the increasing
   right side at $a=4\pi$, $\varepsilon=1/100$.
3. $4\pi\le a\le\pi/(4\varepsilon)$: use
   $D(a)\ge(a-\pi)^2/2\ge9a^2/32$.

## Product-method obstruction

The packet must also establish the limitation of this proof route.

For every $0<\varepsilon<1$ and every integer

$$
Q>\frac9{4\varepsilon},
$$

the exact radial wall $a=Q\pi$ satisfies

$$
\boxed{
\mathcal P_\varepsilon(Q\pi)>W_\varepsilon(Q\pi).
}
$$

Thus the product majorant itself fails at infinitely many optical widths for
every fixed positive $\varepsilon$. This is not a counterexample to the true
shell inequality.

At $a=Q\pi$,

$$
N=Q-1,
$$

$$
S_0=I-D_Q,
\qquad
D_Q=\pi^2\left(\frac{Q^2}{2}+\frac Q6\right),
$$

and the lower angular estimate gives

$$
\mathcal P_\varepsilon(Q\pi)
>
\frac{S_0}{\varepsilon^2}
-\frac{B(Q\pi)}{\varepsilon}.
$$

Use the elementary upper bound

$$
B(Q\pi)<\pi Q(Q-1)
$$

to prove the displayed reverse inequality.

For $\rho=1-\varepsilon$, the existing fixed-rho high-energy theorem begins
at optical width

$$
\varepsilon K_0(1-\varepsilon)
\asymp
\frac{9\pi^3}{4}\varepsilon^{-3},
$$

while the product obstruction occurs at order $\varepsilon^{-1}$. Hence this
positive lemma does not overlap the existing high-energy threshold and does
not close SHELL-rho-one-endpoint.

## Permitted dependencies

- CONV-strict-counting
- SHELL-sturm-liouville-completeness
- SHELL-angular-cutoff
- the min--max principle for the proved direct-sum radial operators
- elementary finite sums and one-variable integral comparisons

No Bessel asymptotic, floating scan, or uncertified computation is permitted
in the proof of the positive range or the wall obstruction.

## Falsification cases

- $a=0$;
- $a=\pi$ and every wall $a=m\pi$;
- $a$ immediately above $\pi$;
- $T_n^2=p(p+1)$ at an angular wall;
- $\varepsilon=1/100$;
- $a=4\pi$;
- $a=\pi/(4\varepsilon)$;
- the direction of the radial operator comparison;
- the factor $M_n^2$ from angular multiplicity;
- confusing failure of the upper majorant with failure of the shell theorem;
- any claimed overlap with $\varepsilon K_0(1-\varepsilon)$.

## Promotion rule

Promotion requires:

1. a frozen incumbent proof of the exact range and exact obstruction;
2. an isolated clean-room reconstruction;
3. an adversarial audit of all strict radial/angular walls, constants, and
   the non-overlap conclusion.

Promotion creates only a partial thin-shell lemma. SHELL-rho-one-endpoint and
TARGET-shell-d3 must remain open.
