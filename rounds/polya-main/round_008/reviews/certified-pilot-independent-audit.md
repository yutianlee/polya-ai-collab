# Round 8 certified-pilot independent audit

## Verdict

**PASS, for the single closed pilot box only.**

The producer, certificate, checker, and stored check report were treated as
untrusted.  The decisive mathematics was reconstructed from the exact
rational box and root brackets, the producer and checker were rerun, their
outputs reproduced the stored artifacts byte for byte, and mutations of every
decisive claim tested below were rejected.

This verdict does **not** cover any residual zone and does not promote either
`COMP-certified-bessel` or `SHELL-rho-compact`.

## Scope reconstructed

The certified box is

\[
B=\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right].
\]

Write \(w=1-\rho\), \(a=\rho k\), and \(b=k\).  With

\[
\psi_0(z)=\sin z,\quad \eta_0(z)=-\cos z,
\]

\[
\psi_1(z)=\frac{\sin z}{z}-\cos z,
\qquad
\eta_1(z)=-\frac{\cos z}{z}-\sin z,
\]

the determinant convention used by the producer is

\[
R_\ell(\rho,k)=\psi_\ell(a)\eta_\ell(b)
-\psi_\ell(b)\eta_\ell(a).
\]

Direct expansion gives

\[
R_0(\rho,k)
=\sin b\cos a-\sin a\cos b
=\sin(wk),
\]

and, after grouping the \(1/(ab)\), sine-sine, cosine-cosine, and
Wronskian terms,

\[
R_1(\rho,k)
=\left(1+\frac1{\rho k^2}\right)\sin(wk)
-\frac{w}{\rho k}\cos(wk).
\]

Thus the independent checker's two low-channel identities have the same sign
and normalization as the producer recurrence; they are not merely
root-equivalent formulas with an unchecked sign reversal.

## Exact residual membership

The ratio bounds satisfy

\[
\frac1{16}<\frac{999}{2000}<\frac{1001}{2000}<\frac{99}{100}.
\]

The lower boundary of \(\mathcal R_C\) increases with \(\rho\).  Hence, using
\(\pi<22/7\),

\[
\sup_B\frac{\pi}{1-\rho}
<\frac{22/7}{999/2000}
=\frac{44000}{6993}<\frac{67}{10}.
\]

For the upper boundary, \(\eta_\rho\le 1/\pi<1/2\).  Formula (4) in the
frozen packet therefore implies

\[
K_0(\rho)>\frac{a_\rho}{\eta_\rho^2}
>4a_\rho=\frac{8\pi\rho}{1-\rho}.
\]

The last function is increasing.  Using \(\pi>333/106\) at the lower ratio
face gives

\[
K_0(\rho)>
8\frac{333}{106}\frac{999}{1001}
=\frac{1330668}{53053}>\frac{168}{25}.
\]

Both frequency inequalities therefore hold on the complete closed box, with
strict room to the two residual-zone boundaries.

## Roots, truncation, and strict multiplicity count

The checker's Fraction-only Machin enclosure of \(\pi\), followed by
alternating Taylor enclosures after reduction to a distance at most one from
\(\pi\), reconstructs the following uniform determinant signs:

| channel | lower root face | upper root face | complete target box |
| ---: | :---: | :---: | :---: |
| \(\ell=0\), bracket \([31/5,63/10]\) | positive | negative | negative |
| \(\ell=1\), bracket \([13/2,33/5]\) | positive | negative | negative |

The independently reconstructed rational interval displays have respective
sign margins

- \(\ell=0\): lower face at least \(0.03848\), upper face at most
  \(-0.00525\), and target-box upper endpoint at most \(-0.20362\);
- \(\ell=1\): lower face at least \(0.03587\), upper face at most
  \(-0.01157\), and target-box upper endpoint at most \(-0.06621\).

These decimal values are only displays of exact rational interval endpoints;
the sign decisions use `Fraction` comparisons.

For the separated radial operator,

\[
-u''+\frac{\ell(\ell+1)}{r^2}u=\lambda u,
\qquad u(\rho)=u(1)=0.
\]

Since \(r^{-2}\ge1\) on the shell, the min-max principle and the interval
Dirichlet spectrum give

\[
\lambda_{n,\ell}\ge
\left(\frac{n\pi}{1-\rho}\right)^2+\ell(\ell+1).
\]

With \(w\le1001/2000\), \(K\le168/25\), and \(\pi>333/106\),

\[
\left(\frac{\pi}{w}\right)^2+6-K^2
\ge
\frac{420595320534}{1759138005625}>0,
\]

so every \(\ell\ge2\) channel is empty.  Also

\[
\left(\frac{2\pi}{w}\right)^2-K^2
\ge
\frac{197782642286784}{1759138005625}>0,
\]

so \(\ell=0\), and a fortiori \(\ell=1\), has at most one root below the
target box ceiling.  The uniform sign changes and continuity give one root in
each of the two surviving channels.

The angular rule \(\ell+1/2<K\) has \(\ell=6\) as the largest possibly active
channel because \(13/2<K_+<15/2\).  The Sturm estimate excludes
\(\ell=2,\ldots,6\), while the angular rule excludes \(\ell\ge7\).  Hence no
channel is omitted.

The upper root faces satisfy

\[
\frac{63}{10}<\frac{67}{10},
\qquad
\frac{33}{5}<\frac{67}{10}.
\]

Consequently both roots lie strictly below every \(K\) in the target box.
The determinant is nonzero throughout the target box and the next radial
roots lie above it, so no spectral wall meets any included target face.  With
the spherical multiplicities \(2\ell+1\), the exact strict count is therefore

\[
1\cdot1+1\cdot3=4.
\]

## Weyl corner direction

The Weyl expression

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3
\]

decreases with \(\rho\), increases with \(K\), and decreases when the positive
denominator \(\pi\) is enlarged.  Its safe lower corner is therefore
\((\rho_+,K_-)\), with an upper enclosure for \(\pi\).  Even the coarser
\(\pi<22/7\) gives

\[
W(\rho,K)>
\frac{1636784962096851}{88000000000000}
>18.59>4.
\]

The independent Machin enclosure gives the sharper displayed lower bound
\(18.60731553544245607556\), hence a strict margin greater than
\(14.60731553544245607556\).  The corner direction and the strict inequality
are correct on all four closed faces.

## Checker independence and provenance

The checker imports only Python standard-library modules.  It imports neither
`python-flint` nor the producer, and it reconstructs rather than trusts:

1. the \(\pi\) enclosure;
2. both determinant identities and all six determinant signs;
3. complete-box \(\mathcal R_C\) membership;
4. angular and radial truncation;
5. multiplicities and the strict count; and
6. the Weyl lower corner and positive margin.

The hashes embedded in the current certificate equal the current files:

| input | SHA-256 |
| --- | --- |
| producer | `8902a0fd4ff7db4b1443ca02326151d4d6e4b9b92b697c68220eb85454c4ec7e` |
| independent checker | `2ab1a31d8a22c6f1d5f7def2e33d2e3f0fb710fdb5cae50f8389d82f5b0475d5` |
| frozen packet | `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7` |

The stored report's certificate hash is also the current certificate hash,
`f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00`.

## Tamper probes

Fresh copies of the certificate were mutated one field at a time.  The
checker rejected all of the following:

| mutation | rejection |
| --- | --- |
| weighted count \(4\to3\) | reported count mismatch |
| \(\ell=1\) multiplicity \(3\to2\) | bad multiplicity |
| root bracket extended to the target box | root bracket meets target box |
| determinant face sign relabeled | producer sign-label mismatch |
| serialized determinant interval made to contain zero | enclosure has no required strict sign |
| spectral-wall flag changed to true | spectral-wall flag mismatch |
| producer source hash replaced | SHA-256 mismatch |
| frequency scope enlarged | angular/truncation audit failure |
| ratio scope enlarged beyond \(\mathcal R_C\) | residual-membership failure |
| Weyl sign relabeled | producer-margin label mismatch |
| one channel removed | expected-channel failure |
| schema changed | unsupported schema |
| root count changed | one-root requirement failure |
| angular maximum changed | angular-cutoff failure |

The current checker intentionally does not authenticate free-text prose,
unused producer metadata, or the exact numerical width of a serialized Arb
interval once that record has the independently reconstructed strict sign.
For example, changing only the prose `claim`, the declared precision, or a
positive Arb display to a different positive display does not cause
rejection.  This is a schema-hardening opportunity, not a soundness defect in
this pilot: none of those fields is used as mathematical evidence, and the
checker independently re-proves every determinant sign and every decisive
inequality.  Downstream use must treat the checker's structured PASS report,
not arbitrary unverified certificate prose, as the certified result.

## Reproduction results

The producer and checker were run into a fresh temporary directory.  The
generated certificate and report had exactly the same SHA-256 hashes as the
stored artifacts:

- certificate: `f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00`;
- check report: `02b12e13ad329e77035d8438ec359b6be4dd35571c384543f3890d67c132e6cc`.

Test results:

- focused Round 8 certificate tests: **6 passed**;
- complete `computations/tests` suite: **28 passed**.

The certified conclusion is therefore

\[
(\rho,K)\in B
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)=4
<\frac{2}{9\pi}(1-\rho^3)K^3,
\]

with all four faces included and with the stated local-only limitation.

## LF-portability re-audit

**PASS.**  After the producer and checker output calls were hardened to request
LF newlines explicitly, the mathematical evaluation and verification paths
were unchanged.  A fresh Windows reproduction produced the exact current
certificate and report hashes listed above.  The generated certificate had
217 LF bytes and zero CR bytes; the generated check report had 83 LF bytes and
zero CR bytes.

The refreshed certificate passed the independent checker.  Key tamper probes
again rejected altered count, multiplicity, root bracket, determinant sign,
serialized sign enclosure, frequency scope, and Weyl sign.  Separate
mutations of each recorded producer, checker, and frozen-packet hash were also
rejected.  The focused tests again reported **6 passed**, and the complete
computation suite again reported **28 passed**.  The portability edit therefore
does not change the audit verdict.
