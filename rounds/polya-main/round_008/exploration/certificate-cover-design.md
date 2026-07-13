# Round 8 Exploration: Exact Cover Manifest for Compact Certification

## Purpose

The analytic envelope and a computational certificate solve different set
problems.  They must not be conflated.

Let

$$
\mathcal P=I_*\times[0,\infty)
$$

be the remaining parameter plane, and let $\mathcal A\subset\mathcal P$ be
the union of every region covered by a permitted analytic theorem.  The true
certification target is

$$
\boxed{\mathcal D=\mathcal P\setminus\mathcal A.}
\tag{1}
$$

The closed sets $\mathcal R_L$, $\mathcal R_C$, and $\mathcal R_T$ in the
frozen compact packet form a convenient bounded planning envelope

$$
\mathcal D\subseteq
\mathcal E:=\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T.
\tag{2}
$$

They are not equal to $\mathcal D$: their boundary faces deliberately
overlap analytic regions.  A full certificate must cover (1), not every
point of the larger bookkeeping set (2).

## 1. Two valid ways to cross a wall

A parameter box need not be split at every spectral or angular wall.  It
must use one of two auditable mechanisms.

### Mechanism S: explicit splitting

Split the box at every relevant wall, certify a fixed count on each open
cell, and assign each shared face to a stated neighboring cell or analytic
theorem.

This is appropriate for a small root-isolation window.

### Mechanism M: monotone majorization

For a closed box

$$
B=[\rho_-,\rho_+]\times[K_-,K_+],
$$

domain inclusion and spectral monotonicity give

$$
N_D(A_{\rho,1},K^2)
\le
\#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}
=:C_B
\tag{3}
$$

throughout $B$.  The non-strict corner count in (3) is intentionally safe
even when $K_+$ is an eigenfrequency.  The Weyl target satisfies

$$
\frac{2}{9\pi}(1-\rho^3)K^3
\ge
W_B:=
\frac{2}{9\pi}(1-\rho_+^3)K_-^3.
\tag{4}
$$

Therefore

$$
\boxed{C_B\le W_B}
\tag{5}
$$

certifies the complete closed box, including all determinant, angular, and
strict spectral walls inside it.  Those walls are not ignored; they are
absorbed into the one-sided count (3).

Mechanism M is essential in high-frequency regions.  At
$\varepsilon=2^{-17}$, for example, the thin residual reaches frequencies
of order $2^{40}$ and contains more than $2^{38}$ angular half-integer
walls.  Literal wall-by-wall subdivision is not a finite computation in any
practical sense.

## 2. Required manifest records

Every certified or analytic cover record must have the following fields.

```text
record_id
kind                    # analytic | split_box | monotone_box
rho_left, rho_right     # exact rational/algebraic endpoints
k_left, k_right         # exact rational/algebraic endpoints
left/right inclusivity
parent_zone             # L | C | T
coverage_clause         # exact subset claim in D or ownership of a face
method
dependencies
arithmetic_backend
backend_version
working_precision
input_hash
artifact_hash
boundary_owners
```

For a `monotone_box`, also require

```text
upper_corner_rho
upper_corner_k
count_convention        # must be non-strict for (3), or justify strictness
angular_truncation_proof
radial_truncation_proof
root_or_phase_artifact
certified_count_upper
lower_corner_rho
lower_corner_k
weyl_lower_artifact
certified_weyl_lower
integer_margin
```

For a split box, replace the corner fields by the complete ordered wall list,
root enclosures, cell counts, and face ownership map.

## 3. Global cover checker

The independent checker must operate on exact endpoints.  It must:

1. reconstruct the analytic set $\mathcal A$ from named theorem clauses;
2. reconstruct the bounded planning envelope $\mathcal E$;
3. verify that every numerical box lies in $\mathcal E$;
4. compute the exact set difference

   $$
   \mathcal E\setminus
   (\mathcal A\cup\text{certified boxes});
   $$

5. return success only if that difference is empty;
6. check every boundary face and corner against its declared owner;
7. recompute hashes and every count/Weyl inequality from the raw artifact.

A floating grid, midpoint sample, or graphical union is not a coverage
proof.

## 4. Truncation obligations

Every corner count must be finite for a proved reason.

- Angular: the Rayleigh bound gives the strict cutoff

  $$
  \ell+\frac12<K_+.
  $$

  A non-strict upper count may safely include the final equality channel.
- Radial: use the exact increasing shell phase, a Sturm comparison, or a
  proved zero-spacing bound to give a finite radial index ceiling before
  root isolation begins.
- Roots: each admitted radial index must have one isolated root or a phase
  interval proving its position relative to $K_+$; every excluded index must
  have a certified lower bound above $K_+$.

The checker must reject a count obtained merely because a scan stopped.

## 5. Cancellation-safe determinant evaluation

For half-integer order, use the Riccati--spherical pair

$$
\psi_\ell(z)=zj_\ell(z),
\qquad
\chi_\ell(z)=zy_\ell(z),
$$

and the root-equivalent determinant

$$
R_{\ell,\rho}(K)
=\psi_\ell(\rho K)\chi_\ell(K)
-\psi_\ell(K)\chi_\ell(\rho K).
\tag{6}
$$

The three-term recurrence must be evaluated with outward-rounded balls and
rescaled when necessary.  A certificate must monitor enclosure inflation;
an interval containing zero is not a sign decision.  Near cancellation, use
the rigorously monotone phase increment or a validated ODE/Prüfer integrator
instead of subtracting two wide products.

## 6. Minimal residual pilot suggested by monotonicity

Consider

$$
B_0=
\left[\frac5{81},\frac1{16}\right]
\times
\left[\frac{81}{10},9\right].
\tag{7}
$$

Its lower-left edge satisfies $\rho K=1/2$, and its interior reaches the
small-hole residual.  Since every shell in (7) is a subdomain of the unit
ball,

$$
N_D(A_{\rho,1},K^2)
\le N_D(B_1,9^2).
\tag{8}
$$

The strict unit-ball count below $9$ is

$$
2\cdot1+2\cdot3+1\cdot5+1\cdot7+1\cdot9=29.
\tag{9}
$$

This count can be certified with Arb signs of
$\psi_\ell(z)=zj_\ell(z)$ at integer $z=3,\ldots,9$, together with the
Sturm separation bound that consecutive zeros are at least $\pi$ apart.
Orders $\ell\ge5$ have no positive zero below $9$; monotonicity of the first
Bessel zero in the order then terminates the angular tail.

The target is minimized at $(\rho,K)=(1/16,81/10)$.  The elementary bound
$\pi<4$ gives

$$
\frac{2}{9\pi}
\left(1-\frac1{16^3}\right)
\left(\frac{81}{10}\right)^3
>
\frac{4095\,81^3}{4096\cdot18000}
>29,
\tag{10}
$$

because

$$
4095\,81^3-29\cdot4096\cdot18000
=38{,}138{,}895>0.
$$

Thus (7) is a meaningful first certificate target.  It proves an actual
two-parameter residual box, but it does not validate shell cross-product
isolation and does not materially reduce the enormous central or thin
high-frequency families.

## 7. Feasibility verdict

The exact manifest and monotone-box mechanism make a pilot rigorous.  They
do not make the full envelope computationally tractable.  Before attempting
a global certificate, the analytic program should further reduce the
central ceiling near $\rho=99/100$ and the thin gap near
$\varepsilon=2^{-18}$.  Any plan whose basic unit is one angular channel per
half-integer wall is rejected by the scale of the current residual.
