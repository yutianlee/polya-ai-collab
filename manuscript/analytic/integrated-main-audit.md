# Clean-room audit of the integrated main manuscript

Date: 2026-07-16  
Audited source: `manuscript/spherical-shell-polya-proof.tex`  
Final verdict: **PASS**

The purely analytic compact closure, aggregate tail, exact residual split,
and final spectral-theorem assembly are valid in the final source identified
below.  I found one proof-critical circular dependency in the first integrated
draft: the discrete aggregate implication was asserted in the main paper as
being proved in Part XIII, while Part XIII imported that implication from the
main paper.  During this audit the lead restored the complete discrete proof
and then added the short missing derivation of its first-shelf bound.  I
re-audited the corrected block and compiled the final manuscript.  No defect
remains in the audited source.

## 1. Frozen final artifacts

| artifact | pages | SHA-256 |
|---|---:|---|
| `manuscript/spherical-shell-polya-proof.tex` | -- | `84D079A9FD3A6001C7F00A528F7EAF40799D6850E87537BDC3819A98A9F6D982` |
| `manuscript/spherical-shell-polya-proof.pdf` | 52 | `E4E9E4573050DD42EE63F0B221B9F899686082649C27E14EF0BC7A20582C407F` |
| `manuscript/spherical-shell-polya-analytic-supplement.tex` | -- | `D9C607269B50AA59CF6F18695B8A0F832ECB64E32F265876C9D02790B2983465` |
| `manuscript/spherical-shell-polya-analytic-supplement.pdf` | 79 | `B055CC4EB52F7C6A4704587300B95A6645B0BD359E3B8EB34A52B15695267E60` |

The main paper and support volume were compiled independently with bundled
Tectonic 0.16.9.  The final passes completed without a LaTeX error or an
undefined reference/citation.  The support hash above is the later
page-by-page-audited bundle promoted after this main-paper audit.

## 2. Audited analytic premises

The integrated formulas were compared with the actual audited TeX sources,
not only with their summaries.

| source | SHA-256 | integrated use |
|---|---|---|
| `compact-structural.tex` | `C236816E12266D055F144CF7EC9B2AEB352CB985EE3730D19F4AA850925606A7` | retained-remainder identity and \(\mathcal E_{\rm ang}<\mathcal H\Rightarrow P<W\) |
| `compact-angular-block.tex` | `8288FE0EAFEB8D8CFE9A10749E6BA470124408E3DC9FBBF1BE24BBB023C6DB49` | strict global angular-defect bound |
| `compact-scalar-positive.tex` | `10CD0E5D6DDE5ECD7CFA2B2C64E47368E10E44093A407C04F74E29BB71807BA1` | scalar positivity on the closed compact region |
| `F-positive.tex` | `D2305C221D89D2275A11B02F590A15FCA36EBE78AAD98DDBF5334FF41BDA064A` | positive aggregate curvature floor |
| `BK-positive-standalone.tex` | `FDEB68A341CEA7654658601636E1266884AF4260D6EDB100039D4AD9A776E0CE` | \(\mathcal B_K(\rho,200)>0\) |
| `B-positive.tex` | `70222FE3523B3F71384ADF22E2751BE1390498AE6554A8875984330DCBF67808` | \(\mathcal B(\rho,200)>60\) |
| `aggregate-tail-analytic.tex` | `B59D673E117611C81BABE4F8D7FE34AD0AFDFEF84BF2D8424128DE606F9C0BC9` | continuous reserve, derivatives, validity domain, and propagation |
| `ledger-packet-F.tex` | `B137FDE7B974F55DD8EFD7D90501611939F291CAC80437C6F707C3CBC483E26E` | exact construction and subtraction of \(\mathcal D_{20}\) |
| `final-analytic-closure.tex` | `568E123178817DE1814095C719B5D7BCE90CFE3AFC48FEC6F97581D6AFAD6DC4` | independent compact/tail owner assembly |

The unique-row ledger partition was also checked against
`ledger-global-coverage-audit.md`: the six disjoint owner counts are

\[
103+278+83+57+22+68=611.
\]

The support volume now prints the canonical family ranges that realize this
partition.  The post-audit change to `ledger-main-visible.tex` only changes
the title from “certificate” to “derivations” and corrects “other six” to
“other five”; its mathematics is unchanged.

## 3. Compact closure

The integrated compact lemma at lines 3684--3737 uses exactly the closed
domain

\[
 \rho_c\leq\rho\leq39/50,
 \qquad k_{11}(\rho)\leq K\leq200.
\]

Its `P_coarse` is the proxy in the compact notes: with
\(\nu=\ell+1/2\), one has \(2\nu=2\ell+1\), the same strict positive-integer
count, and the same strict angular cutoff \(\nu<K\).  The Weyl payment is
also identical:

\[
 W=\int_0^K2zA_{\rho,K}(z)\,dz
  =\frac{2(1-\rho^3)K^3}{9\pi}.
\]

On this domain the calculation at lines 3710--3715 proves that at least one
complete radial block is present.  Parts VII--VIII give, strictly,

\[
 \mathcal E_{\rm ang}
 <\frac{(1-\rho^2)K^2}{6}-\frac12,
\]

and Part IX gives

\[
 \mathcal H-\frac{(1-\rho^2)K^2}{6}+\frac12>0.
\]

Thus \(\mathcal E_{\rm ang}<\mathcal H\), the structural implication gives
\(P_{\rm coarse}<W\), and the earlier phase reduction gives
\(N_D\leq P_{\rm coarse}<W\).  All four faces of the displayed compact
domain are included, and the strict margin is retained on them.

## 4. Restored discrete aggregate bridge

The final block at lines 3767--3911 is now self-contained and matches the
original audited analytic argument.

1. Under \(\mu>1/2\), the definitions of \(J,\tau,R\) give exactly
   \(n_r=J-r\), \(q_r=J+1/2\),
   \(\sum_{r<R}n_r=J(J+1)/2\), and \(\mu-q_r=\tau\).  They are correct in
   both cases \(\tau=0\) and \(0<\tau<1\).
2. Lines 3811--3827 now derive, rather than merely assert, the first-shelf
   estimate.  Since \(C=2\pi\rho K/(1-\rho)=2/\vartheta'_{\rm floor}\),
   \(\vartheta(0)=0\), and \(\vartheta'\geq2/C\),
   \[
    1>\int_{x_r}^{x_r+p_r}\vartheta
      \geq\frac{(x_r+p_r)^2-x_r^2}{C},
   \]
   whence \(p_r<\sqrt{x_r^2+C}-x_r\).
3. Strict convexity and the midpoint inequality give
   \(\sum p_r<\mathcal I(C,R)\).  Combining this with the exact
   concave-head/convex-tail estimate and
   \(0\leq\delta_\tau\leq2\tau^{5/2}/(15\sqrt\mu)\) yields the strict summed
   inequality \(\text{low-tail defect}< -\mathcal Q/4\).
4. High tails are controlled non-strictly, while the low-tail sum is strict.
   The exact multiplicity identity and the weighted scaffold therefore give
   \[
    \mathcal Q\geq0
    \Longrightarrow
    P_{\rm coarse}<2\int_0^K f_3A_{\rho,K}\leq W.
   \]
   The proof explicitly preserves strictness at \(\tau=0\), a half-integer
   inner interface, and an integer \(K\eta_\rho\) wall.
5. If \(K\eta_\rho>1\) and \(\mu>3/2\), the four termwise comparisons at
   lines 3895--3907 have the correct directions and give
   \(\mathcal Q>\mathcal B\).  In particular, the strict floor inequality is
   valid even when \(K\eta_\rho\) is an integer.

This restoration removes the circular dependency found in the initial
integration.  Part XIII now correctly begins its continuous propagation from
the discrete bridge proved in the main paper.

## 5. Aggregate propagation

For \(7/51\leq\rho\leq39/50\) and \(K\geq200\), Part XIII proves
\(\mu>3/2\) and \(K\eta_\rho>1\).  The inclusion
\([\rho_c,39/50]\subset[7/51,39/50]\) follows from \(\pi<22/7\).

The reserve \(\mathcal B\), \(\overline{\mathcal I}\), and curvature floor
\(F\) at lines 3740--3765 and 3924--3951 agree term for term with
`aggregate-tail-analytic.tex`.  The audited base signs are

\[
 F(\rho)>\frac{1549}{84150},\qquad
 \mathcal B_K(\rho,200)>0,\qquad
 \mathcal B(\rho,200)>60.
\]

Twice integrating the strict curvature estimate gives, including the base
face \(K=200\),

\[
 \mathcal B(\rho,K)>
 60+\frac{1549}{168300}(K-200)^2>0.
\]

Consequently \(\mathcal Q>\mathcal B>0\), and the restored discrete lemma
proves the strict Pólya bound for every \(K\geq200\) in the stated ratio
interval.  No interval or sampled sign is used.

## 6. Exact owners and final theorem

Packet F gives exactly

\[
 \mathcal D_{20}
 =\{\rho_c\leq\rho<39/50,
       \ k_{11}(\rho)<K<U(\rho)\}.
\]

The split at lines 3972--4007,

\[
 \mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},\qquad
 \mathcal T_{21}=\mathcal D_{20}\cap\{K>200\},
\]

is disjoint and exhaustive.  The face \(K=200\) belongs only to the compact
owner.  The inherited faces \(\rho=39/50\), \(K=k_{11}(\rho)\), and
\(K=U(\rho)\) remain outside \(\mathcal D_{20}\); \(\rho=\rho_c\) remains
inside subject to the two strict frequency inequalities.  Hence the successor
residual is empty.

The final ratio partition is likewise disjoint and exhaustive:

\[
 (0,1)=(0,\rho_*]\mathbin{\dot\cup}
 (\rho_*,7/8)\mathbin{\dot\cup}[7/8,1).
\]

The small-hole theorem, compact-middle proposition, and thin-shell theorem
cover these three owners.  The case \(K=0\) is handled separately by
\(N_D=W=0\).  Finally, the dilation identity

\[
 N_D(A_{r,R},\Lambda)=N_D(A_{r/R,1},R^2\Lambda)
\]

and \(R>0\) give the claimed factor \(R^3\Lambda^{3/2}\).  The final theorem
therefore follows for every \(0<r<R\) and \(\Lambda\geq0\).

## 7. Executable/interval dependency audit

All remaining mentions of interval programs, certificates, executable
classifiers, and hashes at lines 4040--4077 and in the verification-boundary
appendix are explicitly historical or optional regression checks.  None is
an antecedent of a proof implication.  The current dependency chain uses
printed exact identities, rational cross-multiplications, positive-side
squarings, Bernstein positivity, elementary integral estimates, and the
stated published analytic inputs.

Static checks on the final main source found:

- 205 labels, all unique;
- 197 references, with no missing target;
- 13 citations, all resolved by the five bibliography entries; and
- no residual Arb dependency or interval/executable truth premise.

## 8. Correction log

- **Proof-critical issue found and corrected:** the initial integrated main
  paper omitted the proof of
  \(\mathcal Q\geq0\Rightarrow P_{\rm coarse}<W\) while Part XIII imported it
  from the main paper.  The complete derivation was restored at current lines
  3767--3911.
- **Small self-containment issue found and corrected:** the restored proof
  initially quoted the stronger first-shelf bound without displaying its
  derivation.  Lines 3811--3827 now derive it from the already proved curvature
  inequality.
- I made no direct source edit.  Both corrections were applied by the lead
  during the audit and were then independently checked here.
- A final metadata-only edit changed the PDF subject, running header, and
  subtitle to “Purely analytic”; the frozen main PDF was recompiled afterward.

**Final conclusion: PASS for the exact source and PDFs frozen in Section 1.**
