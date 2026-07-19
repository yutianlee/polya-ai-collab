# Lemma Packet: Ultra-Thin Complementary Action Bridge

Obligations: `SHELL-ultrathin-intermediate-bridge`,
`SHELL-thin-action-aggregate`, `SHELL-thin-curvature-intermediate`, and
`SHELL-rho-one-endpoint`.

Round: 11.

Status: frozen candidate.  This packet is not authoritative until the
clean-room, adversarial, executable-ledger, and judge gates all pass.

## Frozen claim

Let

$$
\rho=1-\varepsilon,
\qquad 0<\varepsilon\le\frac1{100},
\qquad a=\varepsilon K.
$$

Then

$$
\boxed{
a\ge\frac1{8\varepsilon^{3/2}}
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

Threshold equality is included.  Together with the accepted product and
aggregate ranges, (1) is required to prove the all-frequency conclusion

$$
\boxed{
0<\varepsilon\le\frac1{100},\quad K\ge0.
}
\tag{2}
$$

Equivalently, the proposed complete thin endpoint is

$$
\boxed{\frac{99}{100}\le\rho<1.}
\tag{3}
$$

## Definitions supplied to the reviewer

Define the exact scaled action

$$
\mathcal A(y)=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds,
\qquad T=\mathcal A(0)=\frac a\pi.
$$

Let $R$ be its decreasing inverse, let $F=R^2$, and put

$$
y_\ell=\varepsilon\left(\ell+\frac12\right),
\qquad
q_\ell=[\mathcal A(y_\ell)+1/4]_<,
\qquad
P_{\mathcal A}=\varepsilon\sum_\ell y_\ell q_\ell.
$$

For

$$
x_n=n-\frac14,
\qquad
M_\varepsilon(x)=
\#\left\{\ell\ge0:\varepsilon(\ell+1/2)<x\right\},
$$

strict layer cake reads

$$
P_{\mathcal A}
=\frac{\varepsilon^2}{2}
\sum_{x_n<T}M_\varepsilon(R(x_n))^2,
\qquad
I=\int_0^a y\mathcal A(y)\,dy
=\frac12\int_0^T F(t)\,dt.
\tag{4}
$$

## Permitted proved inputs

1. `CONV-strict-counting` and the exact separated shell spectrum.
2. `SHELL-sturm-liouville-completeness`.
3. `SHELL-phase-enclosures`, only in the already-proved form
   $N_D\le2P_{\mathcal A}/\varepsilon^2$.
4. The exact action identities, derivatives, inverse-square curvature switch,
   and strict layer-cake formula from `SHELL-thin-action-aggregate`.
5. `SHELL-thin-product-low-optical`, which covers
   $0\le a\le\pi/(4\varepsilon)$.
6. The accepted Round 6 aggregate theorem, which covers
   $\pi/(4\varepsilon)\le a\le1/(8\varepsilon^{3/2})$.
7. The Round 10 seam theorem and the proved endpoint estimate
   $K_0(24/25)<6000^2$, only for the final all-ratio corollary.

The Round 9 local-plateau theorem is not needed to prove (1) or (2).  It may
be mentioned only as prior coverage that the new bridge supersedes on
$\varepsilon\le1/100$.

## Required new proof obligation

The reviewer must derive directly from (4), without the incumbent response,
that

$$
\boxed{P_{\mathcal A}<I}
\tag{5}
$$

throughout the closed domain in (1).  The intended falsification target is
the shifted radial discrepancy

$$
D=\int_0^T F(t)\,dt-\sum_{x_n<T}F(x_n).
$$

No global comparison with a volume-matched semicircle is permitted.  In
particular, the reviewer must control the curvature switch at
$\tau=\mathcal A(\rho a)$, the radial sawtooth, and the half-integer angular
ceilings explicitly.

## Mandatory faces and walls

- $\varepsilon=1/100$;
- $a=1/(8\varepsilon^{3/2})$;
- $a=\pi/(4\varepsilon)$ in the accepted lower union;
- $\rho=99/100$, approached from the Round 10 seam and the new endpoint;
- every radial wall $x_n=T$;
- every angular wall $R(x_n)/\varepsilon\in\mathbb Z+1/2$;
- every proxy wall $\mathcal A(y_\ell)+1/4\in\mathbb Z$;
- the ungridded curvature interface $t=\tau$;
- strict spectral walls in the final phase transfer;
- $K=6000^2$ in the all-ratio corollary.

## Forbidden shortcuts

- Do not use the false global majorant $\mathcal A\le\mathcal B$.
- Do not infer (5) from equality of continuous integrals.
- Do not replace $[\cdot]_<$ by an ordinary floor at an integer wall.
- Do not assume that $\tau$ lies on an integer or radial grid.
- Do not use sampled signs, floating-point quadrature, or a finite sweep.
- Do not cite the desired all-frequency endpoint as an input to (1).

## Required consequence if promoted

The exact closed analytic union must show

$$
0<\rho<1,\qquad K\ge6000^2
$$

is proved, while `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` remain open below that ceiling.
