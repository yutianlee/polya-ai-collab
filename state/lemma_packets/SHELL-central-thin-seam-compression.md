# Lemma Packet: Central--Thin Seam Compression

Obligation: `SHELL-central-thin-seam-compression`.

Round: 10.

This packet freezes the Round 10 claim and dependency boundary.  A
clean-room reviewer may use this packet and the listed proved inputs, but
must not inspect the Round 10 incumbent derivation before issuing an
independent proof or failure report.

## Primary target

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{25}.
$$

Prove, including threshold equality,

$$
\boxed{
K\ge\frac{20}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

The constant $20$ is not claimed to be optimal.  The point of (1) is its
larger closed radius domain, not an improvement of the Round 9 constant on
$0<\varepsilon\le1/100$.

## Required piecewise use

Retain the stronger proved Round 9 theorem

$$
K\ge\frac{125}{8\varepsilon^2}
\tag{2}
$$

on $0<\varepsilon\le1/100$.  Use (1) only for the enlarged seam strip

$$
\frac1{100}\le\varepsilon\le\frac1{25}.
\tag{3}
$$

The face $\varepsilon=1/100$ is owned by both closed theorems, with (2)
providing the sharper threshold.  The new central--thin face
$\varepsilon=1/25$, equivalently $\rho=24/25$, is owned by (1) and by the
closed central fixed-ratio interval.

## Permitted proved inputs

1. `CONV-strict-counting` and `SHELL-sturm-liouville-completeness`.
2. `SHELL-phase-enclosures`, the strict-to-ordinary-floor transfer,
   `SHELL-weighted-lattice-scaffold`, and
   `SHELL-high-angular-shifted-tails`.
3. The pre-threshold Round 3 low-interface decomposition: for a low shifted
   tail,

   $$
   \frac{\mathcal T_r}{2}
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   $$

   where

   $$
   M=\lfloor K\eta\rfloor+d(n-p)-p,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   $$

   together with the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   $$

4. The exact action representation

   $$
   \eta=G_1(1-\varepsilon)
   =\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv.
   $$

5. `SHELL-thin-local-plateau-optimized`, but only on its proved domain
   $0<\varepsilon\le1/100$, and the proved aggregate-action range

   $$
   K\le\frac1{8\varepsilon^{5/2}}.
   $$

6. `SHELL-fixed-rho-high-energy`: with

   $$
   a_\rho=\frac{2\pi\rho}{1-\rho},
   \qquad
   \eta_\rho=G_1(\max\{\rho,1/2\}),
   \qquad
   C_0=1+\frac{8\sqrt2}{15},
   $$

   the shell inequality holds for $K\ge K_0(\rho)$, where

   $$
   K_0(\rho)=
   \left(
   \frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
        {2\eta_\rho}
   \right)^2.
   \tag{4}
   $$

   The already-audited monotonicity of $K_0$ on the central interval is
   permitted.

7. For the global seam corollary (5)--(7) only, the already-proved
   `SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`, and
   `SHELL-low-interface-small-hole` results may be combined with the
   high-angular input above to cover the left and endpoint zones.  These are
   not dependencies of the local theorem (1).  The conclusion of
   `SHELL-rho-compact-analytic-envelope` is deliberately not permitted,
   because that is the obligation being strengthened by the corollary.

No conclusion or intermediate estimate whose proof assumes
$\varepsilon\le1/100$ may be extrapolated to (3).  In particular, the
Round 9 bounds for the dangerous-plateau location, scaled loss, derivative,
and payment must be rederived on the enlarged domain.

## Required exact seam consequences

Prove directly from (4) that

$$
\boxed{
K_0\!\left(\frac{24}{25}\right)<6000^2
=36000000
<\frac{125^5}{8}.
}
\tag{5}
$$

Then combine the closed analytic zones to prove

$$
\boxed{
0<\rho<1,
\qquad
K\ge\frac{125^5}{8}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{6}
$$

The exact comparison required for promotion is

$$
\frac{125^5}{8}<2^{32}<2^{35},
\qquad
2^{35}>9\frac{125^5}{8}.
\tag{7}
$$

Thus the dominant compact ceiling moves from the central estimate to the
already-proved thin residual ceiling.  This is a high-frequency theorem,
not a proof of the all-frequency shell conjecture.

## Required proof inventory

An incumbent and an isolated clean-room proof must each rederive, on the
whole interval $0<\varepsilon\le1/25$:

1. a uniform lower bound for
   $d=1-2\arccos(1-\varepsilon)/\pi$;
2. the dangerous-plateau location and a positive lower bound for $x_0/K$;
3. the exact local-slope inequality and its self-consistency denominator;
4. a scaled bound for the actual loss $R=p-dm$, with the no-drop,
   immediate-drop, and $n=0$ branches kept separate;
5. the action-gain payment, including the full possible floor loss and
   interface remainder;
6. all elementary bounds for $\pi$, $\sqrt2$, and any additional radicals;
7. monotonicity in every parameter used to place a worst case at
   $\varepsilon=1/25$ or $K\varepsilon^2=20$;
8. the exact central endpoint estimate (5) and all comparisons in (7).

## Mandatory falsification cases

- $\varepsilon=1/15625$, $1/100$, and $1/25$;
- $K=125/(8\varepsilon^2)$ and $K=20/\varepsilon^2$;
- the face $\rho=24/25$ approached from both central and thin regimes;
- the face $\rho=99/100$ and the switch between (1) and (2);
- the no-drop branch $p=n$, immediate-drop branch $p=0$, and degenerate
  branch $n=0$;
- the sign switch $p-dm=0$;
- every ordinary-floor wall, gain wall, interface wall, and strict spectral
  wall;
- the complete synthetic comparison path used to bound the scaled loss;
- any hidden use of $x_0\ge K/2$ or a stronger localization;
- $K=K_0(24/25)$ and $K=6000^2$;
- exact comparison of $6000^2$, $125^5/8$, $2^{32}$, and $2^{35}$.

## Promotion rule

Promote this lemma only after an incumbent proof, an isolated clean-room
reconstruction, an independent adversarial constants-and-walls audit, and
an executable exact rational ledger all pass.  Promotion lowers the global
analytic high-frequency ceiling but leaves `SHELL-rho-compact`,
`COMP-certified-bessel`, `SHELL-rho-uniformity`, and `TARGET-shell-d3`
open until the entire compact residual below the new ceiling is closed and
the theorem-level audits pass.
