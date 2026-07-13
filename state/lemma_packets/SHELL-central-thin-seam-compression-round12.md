# Lemma Packet: Round 12 Enlarged Central--Thin Seam

Obligations: `SHELL-central-thin-seam-compression`,
`SHELL-rho-compact-analytic-envelope`, and `SHELL-rho-compact`.

Round: 12.

Status: frozen candidate. This packet is not authoritative until an
incumbent proof, an isolated clean-room reconstruction, an adversarial
review, an executable exact ledger, and the judge gate all pass.

The clean-room reviewer may inspect this packet and the proved inputs listed
below. The reviewer must not inspect any Round 12 response, exploration,
computation, test, review, or other agent output before issuing a separate
verdict.

## Frozen local claim

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{20}.
$$

Prove, including threshold equality,

$$
\boxed{
K\ge\frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

The constant $24$ is a candidate, not an assumed fact. If it fails, the
reviewer must freeze the first exact failed inequality and report the best
rigorously proved replacement rather than weakening a sign numerically.

## Required piecewise use

Retain the stronger proved Round 10 theorem

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
\tag{2}
$$

Use (1) as new coverage only on

$$
\frac1{25}\le\varepsilon\le\frac1{20}.
\tag{3}
$$

The face $\varepsilon=1/25$ is owned by both closed theorems, with (2)
providing the sharper threshold. The proposed new seam face is

$$
\varepsilon=\frac1{20},
\qquad
\rho=\frac{19}{20}.
\tag{4}
$$

The complete all-frequency endpoint remains exactly
$99/100\le\rho<1$. Neither (1) nor (2) enlarges that endpoint.

## Definitions supplied to the reviewer

For a low-interface shifted tail beginning at $x_0=r_0+1/2<\mu$, put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
\qquad
\eta=G_1(\rho).
$$

Write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1),
$$

and let $p$ be the length of the initial constant ordinary-floor plateau.
Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{5}
$$

For the degenerate head $n=0$, the convention is $p=m=0$. Only the branch
$R>0$ requires a new plateau-loss estimate.

Use the scaled variables

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4,
\qquad
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{6}
$$

The candidate domain becomes

$$
0<y\le\frac1{\sqrt{20}},
\qquad
\rho=1-y^2\ge\frac{19}{20},
\qquad
\kappa\ge24.
\tag{7}
$$

## Permitted proved inputs

1. `CONV-strict-counting` and the exact separated shell spectrum from
   `SHELL-sturm-liouville-completeness`.
2. `SHELL-phase-enclosures`, the strict-to-ordinary-floor transfer,
   `SHELL-weighted-lattice-scaffold`, and
   `SHELL-high-angular-shifted-tails`.
3. The audited pre-threshold Round 3 low-interface decomposition

   $$
   \frac{\mathcal T_{r_0}}2
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   \tag{8}
   $$

   where

   $$
   M=\lfloor K\eta\rfloor+d(n-p)-p
   =\lfloor K\eta\rfloor-R,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   \tag{9}
   $$

   together with the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   \tag{10}
   $$
4. The exact action identity

   $$
   \eta=G_1(1-\varepsilon)
   =\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv,
   \tag{11}
   $$

   and the elementary lower bound
   $\arccos(1-v)\ge\sqrt{2v}$, provided its use and constants are
   reconstructed on (7).
5. The already-promoted Round 10 theorem (2), but only on its stated domain.
   No intermediate Round 10 estimate may be extrapolated past
   $\varepsilon=1/25$.
6. `SHELL-fixed-rho-high-energy`: with

   $$
   a_\rho=\frac{2\pi\rho}{1-\rho},
   \qquad
   \eta_\rho=G_1(\max\{\rho,1/2\}),
   \qquad
   C_0=1+\frac{8\sqrt2}{15},
   $$

   the theorem holds for $K\ge K_0(\rho)$, where

   $$
   K_0(\rho)=
   \left(
   \frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
        {2\eta_\rho}
   \right)^2.
   \tag{12}
   $$

   The already-audited monotonicity of $K_0$ on the central interval is
   permitted.
7. For the all-ratio corollary only, the proved small-hole endpoint, the
   fixed-ratio central theorem, the Round 10 seam theorem, and the Round 11
   all-frequency endpoint $99/100\le\rho<1$ may be assembled. The current
   compact-envelope conclusion is not an input to the local theorem (1).

## Required new analytic work

On the full domain (7), the incumbent and isolated reviewer must each
reconstruct:

1. an explicit lower bound for
   $d=1-2\arccos(1-\varepsilon)/\pi$;
2. from $R>0$, an exact relation among $P$, $r$, and $S$ and a uniform
   dangerous-plateau localization $x_0/K>1/2$;
3. the local-slope inequality, including the fact that equal ordinary-floor
   values give the strict difference $A(x_0)-A(x_0+p)<1$ even at integer
   walls;
4. a self-consistency inequality of the form

   $$
   P^2<
   \frac{2\pi^2Q}{(1-\widehat q)^2},
   \qquad
   Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
   \qquad
   \widehat q=\frac{y^2}{\rho}(Q-1),
   \tag{13}
   $$

   with every positivity and squaring condition stated;
5. an explicit rational $B$ such that $R<B/\sqrt\varepsilon$, proved on the
   complete synthetic comparison path, including the no-drop endpoint
   $P=r=B$;
6. enough action gain to prove $M>4\delta$ after the full possible floor
   loss, separately for $R>0$ and $R\le0$;
7. the immediate-drop branch $p=0$, degenerate head $n=0$, no-drop branch
   $p=n$, and sign wall $R=0$;
8. ordinary-floor, gain, interface, threshold, and strict spectral walls.

No sampled sign, decimal approximation, or finite parameter sweep is proof
of any item above.

## Exact central endpoint target

Prove from (12), without decimal evaluation,

$$
\boxed{K_0(19/20)<3300^2.}
\tag{14}
$$

A candidate exact route, which must be checked rather than assumed, is

$$
a_{19/20}=38\pi<11^2,
\qquad
\eta_{19/20}>\frac{14000}{4199283},
\qquad
C_0<\frac{307}{175}.
\tag{15}
$$

At $Y=3300$, the required quadratic comparison is

$$
\frac{14000}{4199283}Y^2
-11Y-\frac{307}{175}
=\frac{32985481}{7422975}>0.
\tag{16}
$$

The proof must explain why positivity at $Y$ places the unique positive root
of the defining quadratic below $Y$.

## Required closed global union

If and only if (1) and (14) pass all gates, assemble the closed zones:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,19/20]$ has
   $K<K_0(19/20)<3300^2$;
3. on $[19/20,24/25]$, use (1), and on $[24/25,99/100]$ use the sharper
   accepted theorem on every overlap; throughout the combined strip the
   candidate high threshold is at most

   $$
   \frac{24}{(1/100)^2}=240000<3300^2;
   $$
4. every frequency on $[99/100,1)$ is already proved.

All shared ratio faces and $K=3300^2$ itself must be owned. The desired
consequence is

$$
\boxed{
0<\rho<1,
\qquad
K\ge3300^2.
}
\tag{17}
$$

This is not the all-frequency shell theorem. The compact residual below the
new ceiling remains open.

## Mandatory falsification faces

- $\varepsilon=1/100$, $1/25$, and $1/20$;
- $\kappa=20$ on the retained Round 10 range and $\kappa=24$ on (1);
- $\rho=99/100$, $24/25$, and $19/20$ from both adjacent regimes;
- $p=n$, $p=0$, $n=0$, and $R=0$;
- the first branch with $R>0$;
- the entire synthetic $P$-comparison path, not only its endpoint;
- every monotonicity used to place a worst case at
  $y=1/\sqrt{20}$ or $\kappa=24$;
- every ordinary-floor, gain, interface, threshold, and strict spectral
  wall;
- $K=K_0(19/20)$ and $K=3300^2$;
- exact ownership of all zones in (17).

## Forbidden shortcuts

- Do not extrapolate a Round 10 estimate proved only for
  $\varepsilon\le1/25$.
- Do not use the desired enlarged seam or new compact envelope as an input.
- Do not infer an all-frequency endpoint beyond $\varepsilon=1/100$.
- Do not replace strict brackets by ordinary floors at integer walls.
- Do not use decimal signs, floating-point optimization, or sampled
  monotonicity as proof.
- Do not call the exact rational ledger a Bessel-root certificate.

## Promotion boundary

Promotion may strengthen `SHELL-central-thin-seam-compression` and the
compact analytic envelope, and may lower the all-ratio high-frequency
ceiling. It must leave `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` open until the exact compact
residual is closed and fresh theorem-level audits pass.
