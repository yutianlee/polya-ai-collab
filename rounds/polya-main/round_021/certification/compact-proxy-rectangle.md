# Round 21 compact-proxy rectangle certificate

## Result

The deterministic computation in `computations/round21_certify_compact_proxy.py`
certifies the stronger closed-rectangle statement

\[
 \boxed{
 \frac7{51}\le \rho\le\frac{39}{50},\quad 12\le K\le200
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1},K^2)
 <\frac{2}{9\pi}(1-\rho^3)K^3.}
\]

The certificate uses 256-bit Arb (the program refuses fewer than 192 bits),
10,580 exact rational leaf boxes, and maximum subdivision depth 15.  Every leaf
passes by a certain Arb comparison.  The smallest comparison has the
non-rigorous display approximation `0.092025556028085972`; this decimal is not
used in the proof.  Arb's certain positivity predicate is the proof.

## Dependency gates and permitted identities

Before any evaluation the program requires the following exact SHA-256 hashes:

| packet | accepted SHA-256 |
|---|---|
| `SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |

The only transcendental source identity evaluated is the permitted definition

\[
 G_a(\nu)=\frac1\pi\left(\sqrt{a^2-\nu^2}
 -\nu\arccos\frac\nu a\right)\quad(0\le\nu\le a),
 \qquad G_a(\nu)=0\quad(\nu>a).
\]

No Round 20 proof or exploratory solution is a dependency of this certificate.

## Spectral reduction to the coarse proxy

Put \(\nu_\ell=\ell+\tfrac12\), \(\mu=\rho K\), and

\[
 A_{\rho,K}(\nu)=G_K(\nu)-G_{\rho K}(\nu).
\]

The accepted strict phase-count identity and phase enclosure give

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\nu_\ell<K}2\nu_\ell
   [\gamma_{\rho,K}(\nu_\ell)]_<,
 \qquad
 \gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+\frac14.
\]

Here \([x]_<:=\#\{n\in\mathbb N:n<x\}\).  Monotonicity of this set count,
including when either argument is an integer, therefore yields

\[
 N_D(A_{\rho,1},K^2)
 \le P_{\rm coarse}(\rho,K)
 :=\sum_{\nu_\ell<K}2\nu_\ell
 \left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<.
\]

This implication does not turn a strict count into an ordinary floor.  At a
phase endpoint \(\gamma=m\), its contribution remains \(m-1\).

## Monotone corners

For fixed \(\nu<a\), direct differentiation of the displayed source identity
gives

\[
 \partial_aG_a(\nu)=\frac1\pi\sqrt{1-\frac{\nu^2}{a^2}}.
\]

Together with the zero extension, this is nonnegative and tends to zero as
\(a\downarrow\nu\).  Thus, for fixed \(K\),

\[
 \partial_\rho A_{\rho,K}(\nu)
 =-K\,\partial_aG_a(\nu)\big|_{a=\rho K}\le0.
\]

For fixed \(\rho\), in the active range \(\nu<K\), there are two cases:

\[
 \partial_K A_{\rho,K}(\nu)=
 \begin{cases}
 \displaystyle\frac{\sqrt{K^2-\nu^2}}{\pi K}>0,
     &\rho K\le\nu<K,\\[6pt]
 \displaystyle\frac{\sqrt{K^2-\nu^2}-
 \sqrt{\rho^2K^2-\nu^2}}{\pi K}>0,
     &\nu<\rho K.
 \end{cases}
\]

The formulas agree continuously at \(\nu=\rho K\); at \(\nu=K\) the zero
extension is also continuous and nondecreasing.  Consequently
\(A_{\rho,K}(\nu)\), each strict integer count of it, and
\(P_{\rm coarse}\) decrease weakly with \(\rho\) and increase weakly with
\(K\).

For

\[
 W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3,
\]

one has

\[
 \partial_\rho W=-\frac{2\rho^2K^3}{3\pi}<0,
 \qquad
 \partial_KW=\frac{2(1-\rho^3)K^2}{3\pi}>0.
\]

Hence on an exact rational box
\(B=[\rho_-,\rho_+]\times[K_-,K_+]\),

\[
 P_{\rm coarse}(\rho,K)\le P_{\rm coarse}(\rho_-,K_+),
 \qquad
 W(\rho,K)\ge W(\rho_+,K_-).
\]

## What one leaf certifies

At \((\rho_-,K_+)\), Arb encloses every value

\[
 x_\ell=A_{\rho_-,K_+}(\nu_\ell)+\frac14.
\]

From the outward upper endpoint of that ball the program proposes an integer
\(M_\ell\), but it accepts the term only after Arb certifies
\(x_\ell\le M_\ell\).  This comparison proves

\[
 [x_\ell]_<\le M_\ell-1.
\]

It is exact at an integer wall: if \(x_\ell=M_\ell\), the strict count is
\(M_\ell-1\).  If an Arb ball were to straddle a wall, the algorithm would use
the next integer and safely overcount; at 256 bits there were zero such
straddles among all generated corner evaluations.  Thus the weighted sum
produces a certified integer \(\widehat P_B\ge P_{\rm coarse}(\rho_-,K_+)\).

At the other corner Arb evaluates \(W(\rho_+,K_-)\), takes an outward lower
enclosure \(W_{B,-}\), and declares the leaf proved only if the Arb predicate

\[
 \boxed{W_{B,-}-\widehat P_B>0}
\]

is certainly true.  A floating-point midpoint never enters this decision.

The unsplit root is deliberately too coarse and fails: its upper proxy is
`554407`, while its opposite-corner Weyl lower bound is far smaller.  Only a
failed box is subdivided.  Floating-point display values may choose whether to
bisect \(\rho\) or \(K\), but both candidate bisections have exact rational
midpoints and every final PASS is independently replayed with Arb.

## Interfaces, walls, and exact coverage

All parameter endpoints and all subdivisions are `Fraction` values.

- The comparisons \(\nu\mathrel{?}\rho K\) and \(\nu\mathrel{?}K\) are exact
  rational comparisons.  At \(\nu=\rho K\), the inner \(G\)-term is set to
  exact zero; no endpoint `acos` evaluation is attempted.
- The active count is exactly
  \(\max\{0,\lceil K-\tfrac12\rceil\}\).  Thus \(\nu=K\) is excluded at a
  half-integer \(K\).  Even if included formally, its proxy argument is
  \(1/4\) and its strict count is zero.
- Integer proxy walls use the Arb-versus-integer proof above, and spectral
  endpoints retain the strict packet convention.
- The analytic bound is proved on each closed rational box.  For partition
  ownership, every coordinate interval is lower-closed and upper-open, except
  that an interval on the root's upper face includes that face.  Thus a shared
  face belongs to exactly one child.  A separate exact slab sweep checks that every elementary open
  \(\rho\)-slab tiles the full \(K\)-interval with neither a gap nor a
  positive-area overlap.  Exact leaf-area summation independently equals the
  root area, and every rational vertical face is retiled using the half-open
  ownership rule.  Thus every point, including every edge and vertex, has
  exactly one owner.

The recursion limits are 100,000 boxes and depth 30; the actual certificate is
well inside both limits.

## Reproduction record

Command:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python computations\round21_certify_compact_proxy.py
```

Result:

```text
ROUND21_COMPACT_PROXY PASS
precision_bits=256
leaf_boxes=10580
max_depth=15
coverage=PASS (exact rational slab/face sweep and exact area)
nonoverlap=PASS (exact half-open shared-face ownership)
generated_proxy_corners=16020
generated_floor_comparisons=2153076
generated_wall_straddles=0
min_gap_lower_display=0.092025556028085972
certificate_sha256=96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631
```

The certificate digest hashes the schema, precision, root, all three packet
hashes, and every sorted leaf's four exact rational endpoints, depth, and
integer proxy upper bound.

Targeted adversarial tests:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m pytest -q computations\tests\test_round21_certify_compact_proxy.py
```

Result: `5 passed in 36.94s`.  The tests cover packet tampering, stored-count
tampering, exact integer walls, uncertain wall fallback, both interfaces,
strict half-integer cutoff, the 192-bit gate, the deliberately failing coarse
root, exact coverage, and the fixed certificate digest.

## Coverage of the prospective sub-200 residual

Let

\[
 R=\left[\frac7{51},\frac{39}{50}\right]\times[12,200].
\]

The prospective D20 compact part below \(K=200\) supplied to this round has
parameters satisfying

\[
 \frac7{51}\le\rho\le\frac{39}{50},\qquad12\le K<200.
\]

Therefore it is literally the subset

\[
 R_{\mathrm{D20},<200}\subset
 \left[\frac7{51},\frac{39}{50}\right]\times[12,200)
 \subset R.
\]

No limiting argument is needed, and the certificate also includes the face
\(K=200\).  Thus every prospective D20 point below 200 is covered by one or
more certified boxes, and the exact half-open convention gives every shared
face a unique owner.
