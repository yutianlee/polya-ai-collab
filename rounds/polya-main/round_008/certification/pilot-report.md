# Certified pilot: one central residual box

## Result

The producer and the independent checker certify the closed box

\[
 B=\left[\frac{999}{2000},\frac{1001}{2000}\right]
 \times
 \left[\frac{67}{10},\frac{168}{25}\right]
 \subset\mathcal R_C.
\]

For every \((\rho,K)\in B\),

\[
 N_D(A_{\rho,1},K^2)=4
 <\frac{2}{9\pi}(1-\rho^3)K^3.
\]

All four faces are included.  No determinant or angular wall intersects the
box, so the displayed count is the exact strict count, not merely a sampled
or non-strict count.

## Why the complete box lies in \(\mathcal R_C\)

Clearly \(1/16<999/2000<1001/2000<99/100\).  Using
\(\pi<22/7\),

\[
 \sup_{\rho\in B}\frac\pi{1-\rho}
 <\frac{22/7}{999/2000}
 =\frac{44000}{6993}<\frac{67}{10}.
\]

For the upper residual boundary, \(\eta_\rho\le G_1(0)=1/\pi<1/2\).
Formula (4) in the frozen packet therefore gives

\[
 K_0(\rho)>4a_\rho=\frac{8\pi\rho}{1-\rho}.
\]

Using \(\pi>333/106\), the last expression is at least

\[
 8\frac{333}{106}\frac{999}{1001}
 =\frac{1330668}{53053}
 >\frac{168}{25}.
\]

Thus every point of \(B\), not only its midpoint, lies in \(\mathcal R_C\).

## Root count

Arb at 256-bit precision evaluates the exact Riccati recurrence on the full
\(\rho\)-interval.  It proves uniform strict sign changes on

\[
 \ell=0:\quad \left[\frac{31}{5},\frac{63}{10}\right],
 \qquad
 \ell=1:\quad \left[\frac{13}{2},\frac{33}{5}\right].
\]

The independent checker reconstructs the low-channel identities

\[
 R_0(\rho,k)=\sin((1-\rho)k),
\]

\[
 R_1(\rho,k)=
 \left(1+\frac1{\rho k^2}\right)\sin((1-\rho)k)
 -\frac{1-\rho}{\rho k}\cos((1-\rho)k)
\]

with exact rational Taylor enclosures.  Its determinant intervals have signs

| Channel | lower root face | upper root face | complete target box |
| ---: | :---: | :---: | :---: |
| \(\ell=0\) | positive | negative | negative |
| \(\ell=1\) | positive | negative | negative |

For width \(w=1-\rho\), the min-max principle and one-dimensional Poincaré
inequality give

\[
 \lambda_{n,\ell}\ge
 \left(\frac{n\pi}{w}\right)^2+\ell(\ell+1).
\]

Since \(w\le1001/2000\), \(K^2\le(168/25)^2\), and
\(\pi>333/106\),

\[
 \left(\frac{\pi}{w}\right)^2+6-K^2
 \ge
 \frac{420595320534}{1759138005625}>0.
\]

Hence every \(\ell\ge2\) channel is empty.  The analogous \(n=2,\ell=0\)
bound is also strictly above the box, so each of \(\ell=0,1\) has at most one
root.  The sign changes give exactly one root in each.  Multiplicity then
gives the strict count \(1+3=4\).

For completeness of the enumeration, the proved angular cutoff
\(\ell+1/2<K\) leaves only \(0\le\ell\le6\) anywhere in the box.  The bound
above excludes \(\ell=2,\ldots,6\), while \(\ell\ge7\) is inactive.  The
proved separated Sturm--Liouville completeness theorem identifies every
remaining shell eigenvalue with one of the radial determinant roots just
counted.  Thus no unexamined angular channel, radial index, or cross-channel
coincidence can add to the count.

## Weyl margin

The independent checker obtains the rigorous lower value

\[
 \inf_B\frac{2}{9\pi}(1-\rho^3)K^3
 >18.60731553544245607556,
\]

so the certified margin above the exact count is greater than
\(14.60731553544245607556\).  Even the elementary substitution
\(\pi<22/7\) gives the exact rational lower bound

\[
 \frac{1636784962096851}{88000000000000}>18.59.
\]

## Reproduction

```powershell
python -m pip install -r computations/requirements-round8-certified.txt
python computations/round8_compact_box_certificate.py --output rounds/polya-main/round_008/certification/pilot-central-box.json
python computations/round8_verify_compact_box_certificate.py --input rounds/polya-main/round_008/certification/pilot-central-box.json --report rounds/polya-main/round_008/certification/pilot-central-box-check.json
python -m pytest computations/tests/test_round8_compact_box_certificate.py -q
```

The producer artifact records python-flint/Arb version, precision, parseable
outward balls, exact rational inputs, commands, and SHA-256 hashes of the
producer, independent checker, and frozen packet.  The checker imports neither
python-flint nor producer code, and it rejects the artifact unless all three
recorded hashes equal the current files.

## Limitations

- This certifies one small box only; it does not cover any residual zone.
- It does not promote `COMP-certified-bessel` or `SHELL-rho-compact`.
- It demonstrates low-channel determinant certification, not a scalable
  strategy for the current \(2^{35}\) and \(2^{42}\) coarse bounds.
- A full result needs more analytic compression, then an exact
  face-connected cell-cover manifest and independent cover checker.
