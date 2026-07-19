# Lemma Packet: Round 13 Central--Thin Seam Extension

Obligations: `SHELL-central-thin-seam-compression`,
`SHELL-rho-compact-analytic-envelope`, and `SHELL-rho-compact`.

Round: 13.

Status: frozen candidate. This packet is not authoritative until an
incumbent proof, a strictly isolated clean-room reconstruction, an
adversarial review, an executable exact ledger, and the judge gate all pass.

The clean-room reviewer may inspect only this packet and the proved inputs
listed below before issuing a separate verdict. The reviewer must not inspect
any Round 13 response, exploration, computation, test, review, or other agent
output before that verdict.

## Frozen local claim

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{10}.
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
first exact failed inequality must be frozen and the best rigorously proved
replacement reported instead of weakening a sign numerically.

## Required piecewise use

Retain the proved Round 12 theorem

$$
0<\varepsilon\le\frac1{20},
\qquad
K\ge\frac{24}{\varepsilon^2},
\tag{2}
$$

and the sharper proved Round 10 theorem

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
\tag{3}
$$

Use (1) as new coverage only on

$$
\frac1{20}\le\varepsilon\le\frac1{10}.
\tag{4}
$$

The face $\varepsilon=1/20$ is owned by both closed constant-$24$
theorems. The proposed new seam face is

$$
\varepsilon=\frac1{10},
\qquad
\rho=\frac9{10}.
\tag{5}
$$

The complete all-frequency endpoint remains exactly
$99/100\le\rho<1$. None of (1)--(3) enlarges that endpoint.

## Definitions supplied to the reviewers

For $a>0$, define

$$
G_a(z)=\frac1\pi
\left(
\sqrt{a^2-z^2}-z\arccos\frac za
\right),
\qquad 0\le z\le a,
$$

and extend $G_a$ by zero for $z\ge a$.

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

For $n\ge1$, define

$$
h_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor.
$$

If the first drop occurs after index $p$, define $p$ by

$$
h_0=h_p>h_{p+1},
\qquad 0\le p<n;
$$

if no drop occurs, set $p=n$. Thus $p=0$ means an immediate drop after the
initial value, while $p=n$ is the no-drop branch. Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{6}
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
\tag{7}
$$

The candidate domain is

$$
0<y\le\frac1{\sqrt{10}},
\qquad
\rho=1-y^2\ge\frac9{10},
\qquad
\kappa\ge24.
\tag{8}
$$

## Permitted proved inputs for the local claim

1. `CONV-strict-counting` and the exact separated shell spectrum from
   `SHELL-sturm-liouville-completeness`.
2. `SHELL-phase-enclosures`, the strict-to-ordinary-floor transfer,
   `SHELL-weighted-lattice-scaffold`, and
   `SHELL-high-angular-shifted-tails`.
3. With

   $$
   b_\ell=
   \left\lfloor
   A\!\left(\ell+\frac12\right)+\frac14
   \right\rfloor,
   \qquad
   \mathcal T_{r_0}=b_{r_0}+2\sum_{\ell>r_0}b_\ell,
   $$

   the audited pre-threshold Round 3 low-interface decomposition from
   `SHELL-low-interface-fixed-rho-high-energy`

   $$
   \frac{\mathcal T_{r_0}}2
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   \tag{9}
   $$

   where

   $$
   M=\lfloor K\eta\rfloor+d(n-p)-p
   =\lfloor K\eta\rfloor-R,
   \qquad
   \delta=\int_q^\mu G_\mu(z)\,dz,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   \tag{10}
   $$

   together with the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   \tag{11}
   $$
4. The exact action identity

   $$
   \eta=G_1(1-\varepsilon)
   =\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv,
   \tag{12}
   $$

   and the elementary inequality
   $\arccos(1-v)\ge\sqrt{2v}$, provided its use and constants are
   reconstructed on (8).
The following inputs are permitted only for the endpoint estimate and
closed global union. They are not dependencies of the local claim (1):

5. The promoted Round 10 and Round 12 theorem statements (2)--(3), but only
   on their stated domains. No intermediate estimate from either proof may
   be extrapolated past its proved endpoint.
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
   \tag{13}
   $$

   The already-audited monotonicity of $K_0$ on the central interval is
   permitted.
7. For the all-ratio corollary only, the proved small-hole endpoint,
   fixed-ratio central theorem, Round 10 and Round 12 seam theorems, and
   Round 11 all-frequency endpoint $99/100\le\rho<1$ may be assembled. The
   desired Round 13 compact-envelope conclusion is not an input to (1).

## Preliminary screen, not a permitted lemma

A read-only exact screen suggests

$$
d>\frac23,
\qquad
\widehat q<\frac37,
\qquad
B=\frac{14}{3}.
\tag{14}
$$

It also suggests the following quantities, in order:

$$
\frac{23}{37800}>0
\quad\text{(displacement reserve)},
$$

$$
\frac{x_0}{K}>\frac{18}{35}=\frac12+\frac1{70}
\quad\text{(localization)},
$$

$$
\frac{2376966388822}{5818105805625}>0
\quad\text{(synthetic endpoint reserve)},
$$

$$
\frac{170244091}{27217575}>0
\quad\text{(action-payment reserve)}.
\tag{15}
$$

These values are navigation aids only. Every expression to which a reserve
belongs, every monotonicity used to reach it, and every strictness direction
must be reconstructed. Merely reproducing the displayed positive fractions
does not prove (1).

## Required new analytic work

On the full domain (8), the incumbent and isolated reviewer must each
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
   \tag{16}
   $$

   with every positivity and squaring condition stated;
5. an explicit rational $B$ such that $R<B/\sqrt\varepsilon$, proved on
   the complete synthetic comparison path, including the no-drop endpoint
   $P=r=B$;
6. enough action gain to prove $M>4\delta$ after the full possible floor
   loss, separately for $R>0$ and $R\le0$;
7. the immediate-drop branch $p=0$, degenerate head $n=0$, no-drop branch
   $p=n$, the sign wall $R=0$, and the first branch with $R>0$;
8. ordinary-floor, gain, interface, threshold, and strict spectral walls.

No sampled sign, decimal approximation, or finite parameter sweep proves
any item above.

## Exact central endpoint target

Prove from (13), without decimal evaluation,

$$
\boxed{K_0(9/10)<900^2.}
\tag{17}
$$

A candidate exact route, which must be checked rather than assumed, is

$$
a_{9/10}=18\pi<8^2,
\qquad
\eta_{9/10}>\frac1{107},
\qquad
C_0<\frac{307}{175}.
\tag{18}
$$

The action lower bound in (12), together with
$\pi<22/7$ and $\sqrt5<9/4$, gives the candidate estimate

$$
\eta_{9/10}
\ge\frac1{15\pi\sqrt5}
>\frac1{107}.
\tag{19}
$$

At $Y=900$, the required quadratic comparison is

$$
\frac1{107}Y^2-8Y-\frac{307}{175}
=\frac{6897151}{18725}>0.
\tag{20}
$$

The proof must explain why positivity at $Y$ places the unique positive root
of the defining quadratic below $Y$.

## Required closed global union

If and only if (1) and (17) pass every gate, assemble these closed zones:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,9/10]$ has
   $K<K_0(9/10)<900^2$;
3. on $[9/10,19/20]$, (1) leaves possible residual only below

   $$
   \frac{24}{(1/20)^2}=9600;
   $$
4. on $[19/20,24/25]$, the Round 12 theorem leaves possible residual only
   below $15000$;
5. on $[24/25,99/100]$, the sharper Round 10 theorem leaves possible
   residual only below $200000$;
6. every frequency on $[99/100,1)$ is already proved.

All shared ratio faces and $K=900^2$ itself must be owned. Since

$$
64<9600<15000<200000<900^2,
$$

the desired consequence is

$$
\boxed{
0<\rho<1,
\qquad
K\ge900^2.
}
\tag{21}
$$

The exact reduction from the Round 12 ceiling would be

$$
\frac{3300^2}{900^2}=\frac{121}{9}>13.
\tag{22}
$$

This is not the all-frequency shell theorem. The compact residual below the
new ceiling would remain open.

## Mandatory falsification faces

- $\varepsilon=1/100$, $1/25$, $1/20$, and $1/10$;
- $\kappa=20$ on the retained Round 10 range and $\kappa=24$ on (1)--(2);
- $\rho=99/100$, $24/25$, $19/20$, and $9/10$ from both adjacent regimes;
- $p=n$, $p=0$, $n=0$, $R=0$, and the first branch with $R>0$;
- the wall $\mu-x_0\in\mathbb Z$ and both adjacent values of $\beta$;
- every coarse-proxy integer wall and the gain wall $K\eta\in\mathbb Z$;
- $q=\mu$, where $\delta=0$, and the low/high interface $x_0=\mu$;
- the angular cutoff wall $\nu=K$;
- the complete synthetic $P$-comparison path, not only its endpoint;
- every monotonicity used to place a worst case at
  $y=1/\sqrt{10}$ or $\kappa=24$;
- every ordinary-floor, gain, interface, threshold, and strict spectral
  wall;
- $K=K_0(9/10)$ and $K=900^2$;
- $\rho=\rho_*$, $\rho=1/16$, and $K=64$ in the global union;
- exact ownership of all zones in (21).

## Forbidden shortcuts

- Do not extrapolate an intermediate Round 12 estimate proved only for
  $\varepsilon\le1/20$.
- Do not use the desired enlarged seam or new compact envelope as an input.
- Do not use any Round 13 response, computation, review, or judge artifact as
  an input to an independent reconstruction.
- Do not use the open compact, certification, uniformity, or final-target
  obligations as proved inputs.
- Do not infer an all-frequency endpoint beyond $\varepsilon=1/100$.
- Do not replace strict brackets by ordinary floors at integer walls.
- Do not use decimal signs, floating-point optimization, or sampled
  monotonicity as proof.
- Do not call an exact rational ledger a Bessel-root certificate.

## Promotion boundary

Promotion may strengthen `SHELL-central-thin-seam-compression` and the
compact analytic envelope, and may lower the all-ratio high-frequency
ceiling. It must leave `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` open until the exact compact
residual is closed and fresh theorem-level audits pass.
