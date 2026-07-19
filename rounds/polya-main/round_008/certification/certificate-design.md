# Round 8 residual-certificate design

## Status and scope

This document specifies a certificate family for the compact packet.  The
closed union

\[
 \mathcal E=\mathcal R_L\cup\mathcal R_C\cup\mathcal R_T
\]

is a planning envelope, while the true target is

\[
 \mathcal D=(I_*\times[0,\infty))\setminus\mathcal A,
\]

where \(\mathcal A\) is the union of all permitted analytic regions.  Thus
\(\mathcal D\subseteq\mathcal E\), and analytically owned faces in
\(\mathcal E\setminus\mathcal D\) are masks rather than numerical work.
This document does **not** assert that \(\mathcal D\) is covered.  The
accompanying implementation certifies one deliberately small closed box in
\(\mathcal D\cap\mathcal R_C\).

The exact shell determinant in angular channel \(\ell\) is represented by

\[
 R_\ell(\rho,k)
 =\psi_\ell(\rho k)\eta_\ell(k)
  -\psi_\ell(k)\eta_\ell(\rho k),
\]

where \(\psi_\ell(z)=zj_\ell(z)\) and \(\eta_\ell(z)=zy_\ell(z)\).  In
dimension three these functions have the elementary recurrence

\[
 \psi_0=\sin z,\quad \eta_0=-\cos z,
 \qquad
 \psi_1=\frac{\sin z}{z}-\cos z,\quad
 \eta_1=-\frac{\cos z}{z}-\sin z,
\]

\[
 f_{\ell+1}(z)=\frac{2\ell+1}{z}f_\ell(z)-f_{\ell-1}(z).
\]

Thus low and moderate half-integer channels can be evaluated directly with
outward-rounded real balls; no nonrigorous Bessel library call is needed.

## Machine-readable cell schema

Every certificate cell should contain the following fields.  Exact rational
or dyadic input is mandatory; binary floating-point input is not accepted.

| Group | Required content |
| --- | --- |
| Identity | Schema version, zone, exact closed coordinate box, claim kind, parent cover identifier, and cell identifier. |
| Provenance | Producer and checker versions, precision, platform, commands, SHA-256 hashes of code, frozen packet, and input manifests. |
| Membership | Interval proof that the complete cell lies in the stated residual zone, including both frequency inequalities. |
| Angular cutoff | Exact resolution of every wall \(K=\ell+1/2\), the largest possibly active channel, and the channels actually examined. |
| Spectral data | Backend, determinant/Prüfer convention, root index, root tube or exclusion enclosure, face signs, monotonicity or simplicity input, and multiplicity \(2\ell+1\). |
| Proxy data | If a phase or floor proxy is used, every phase-integer and ordinary-floor wall, strict-floor convention, and certified pointwise domination of the spectral count. |
| Count | Either `exact_strict` or `certified_upper_nonstrict`.  The latter is required whenever a spectral endpoint cannot be separated; it is safe only if its larger count still fits below the Weyl lower bound. |
| Weyl margin | Outward lower enclosure of \(2(1-\rho^3)K^3/(9\pi)\), count upper bound, and a strictly positive difference. |
| Faces | Six/ four closed-face identifiers as appropriate, plus the neighboring cell that shares or overlaps each face. |
| Checker | Independent recomputation result, artifact hash, and explicit limitations. |

The certificate must be rejected if any serialized interval contains a wall
that the cell claims to avoid.  A point sample on each side of a wall is not a
replacement for a root tube or a monotonicity proof over the entire box.

## Wall manifest

A cover builder must account for every intersection with one of the
following:

1. a zone or analytic-coverage boundary;
2. an angular wall \(K=\ell+1/2\);
3. a determinant zero or Prüfer phase level \(n\pi\);
4. a phase-envelope integer or ordinary-floor wall;
5. a switch between determinant, phase, and analytic backends;
6. a zero of the certified Weyl margin.

There are two valid mechanisms.  A `split_box` subdivides at every listed
wall and assigns every shared face.  A `monotone_box` instead proves, for

\[
 B=[\rho_-,\rho_+]\times[K_-,K_+],
\]

the one-sided corner bounds

\[
 N_D(A_{\rho,1},K^2)
 \le \#\{\lambda_j(A_{\rho_-,1})\le K_+^2\}=:C_B
\]

and

\[
 \frac{2}{9\pi}(1-\rho^3)K^3
 \ge \frac{2}{9\pi}(1-\rho_+^3)K_-^3=:W_B.
\]

Then a certified inequality \(C_B\le W_B\) absorbs every internal wall.
The non-strict corner count is intentional and safely includes a possible
eigenvalue on the upper frequency face.  Literal wall splitting is not
required when this monotone mechanism is proved.

Spectral faces use the project's strict convention.  If a root tube lies on a
face, the adjacent cells must agree on its identity and must either prove the
strict endpoint count or both use the same non-strict upper count.

## Zone-specific coordinates and backends

### Zone L

Use \((\rho,K)\) boxes with exact endpoints and certify

\[
 \rho_*\le\rho\le\frac1{16},\qquad
 \frac1{2\rho}\le K\le H_0(\rho),\qquad K<64.
\]

At this scale direct Arb Riccati recurrence, root tubes, and Sturm bounds are
plausible.  The irrational \(\rho_*\) face should remain analytic; numerical
cells should begin at a rational face strictly to its right or carry a proved
interval comparison with the exact definition of \(\rho_*\).

### Zone C

Use \((\rho,K)\) boxes and certify

\[
 \frac1{16}\le\rho\le\frac{99}{100},\qquad
 \frac\pi{1-\rho}\le K\le K_0(\rho).
\]

Direct determinant cells are appropriate at low energy.  At larger energy,
a normalized Prüfer phase or an already-proved phase-to-floor upper envelope
is preferable to unstable high-order forward recurrence.  Every proxy wall
must still be listed.  The coarse bound \(K<2^{35}\) is a finiteness theorem,
not a practical enumeration plan.

### Zone T

Use \((\varepsilon,a)\) with \(a=\varepsilon K\) when possible.  The residual
conditions become

\[
 2^{-18}\le\varepsilon\le\frac1{100},\qquad
 \frac1{8\varepsilon^{3/2}}\le a\le\frac{64}{\varepsilon}.
\]

This scaling avoids storing \(K\) as large as \(2^{42}\), but it does not
make channel-by-channel enumeration practical.  A viable full certificate
will require an aggregate phase/floor inequality or a further analytic
reduction.  Direct root enumeration over the present coarse \(\mathcal R_T\)
should be rejected as an implementation plan.

## Independent-checker contract

The checker must not call the producer as a library.  It must parse exact
inputs, reconstruct residual membership, resolve the angular cutoff, verify
every root/exclusion record, recompute the weighted count, and recompute a
Weyl lower bound.  A full cover checker must additionally prove, from exact
endpoints and face owners,

\[
 \mathcal E\setminus
 (\mathcal A\cup\text{certified boxes})=\varnothing.
\]

For the pilot, the checker uses only Python's
`fractions.Fraction`: Machin's formula encloses \(\pi\), alternating Taylor
remainders enclose sine and cosine, and explicit formulas reconstruct
\(R_0\) and \(R_1\).

## Promotion boundary

An individually checked cell is a certified local result.  It is not a
certificate of `COMP-certified-bessel` until every point of \(\mathcal D\)
has either a certified box or an explicit analytic owner and the exact
face-connected cover manifest itself passes an independent checker.  The
very large coarse bounds in Zones C and T make further analytic compression
the next prerequisite.
