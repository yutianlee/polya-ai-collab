# Clean-room audit of `final-analytic-closure.tex`

Date: 2026-07-16  
Initial and final source SHA-256: `568E123178817DE1814095C719B5D7BCE90CFE3AFC48FEC6F97581D6AFAD6DC4`  
Verdict: **PASS**  
Source edits: **none**

I reconstructed the closure from the proved phase, compact, aggregate, and
owner-subtraction statements rather than accepting the dependency narrative
in the source. Every hypothesis has the required domain, every open or closed
face has an owner, and every inequality composes in the strict direction
claimed. The definitions of the lattice proxy \(P\) and Weyl target \(W\)
match the earlier phase and compact arguments exactly.

No genuine local defect was found, so the TeX source was not modified. The
former interval certificates and executable truth tables are not premises of
this closure once the audited analytic replacement packets are used.

## 1. Audited premise graph

The closure was checked against the following current sources:

| premise source | SHA-256 | fact used here |
|---|---|---|
| `manuscript/spherical-shell-polya-proof.tex` | `013B1D7C05F79FD88529254AD69D5F08805B08438C448DC9CB3C0C352CD68B30` | exact phase enumeration and strict phase-to-lattice reduction |
| `compact-structural.tex` | `C236816E12266D055F144CF7EC9B2AEB352CB985EE3730D19F4AA850925606A7` | \(\mathcal E_{\rm ang}<\mathcal H\Rightarrow P<W\) |
| `compact-angular-block.tex` | `8288FE0EAFEB8D8CFE9A10749E6BA470124408E3DC9FBBF1BE24BBB023C6DB49` | global strict angular-defect bound |
| `compact-scalar-positive.tex` | `10CD0E5D6DDE5ECD7CFA2B2C64E47368E10E44093A407C04F74E29BB71807BA1` | strict scalar positivity on the closed compact region |
| `aggregate-tail-analytic.tex` | `B59D673E117611C81BABE4F8D7FE34AD0AFDFEF84BF2D8424128DE606F9C0BC9` | strict aggregate theorem for \(K\ge200\) |
| `ledger-packet-F.tex` | `B137FDE7B974F55DD8EFD7D90501611939F291CAC80437C6F707C3CBC483E26E` | exact symbolic construction of \(\mathcal D_{20}\) and its compact/tail split |

The three compact notes, aggregate note, and Packet F all have independent
PASS audits. I checked the actual theorem statements and formulas in those
sources, not just their audit summaries.

## 2. Exact identification of the proxy \(P\)

The final closure defines

\[
 P(\rho,K)=
 \sum_{\substack{\nu=\ell+1/2<K\\\ell\in\mathbb N_0}}
 2\nu\,\#\{n\in\mathbb N:n<A_{\rho,K}(\nu)+1/4\}.
\]

This is exactly the compact argument's

\[
 P_{\rm coarse}(\rho,K)
 =\sum_{\ell+1/2<K}(2\ell+1)
 [A_{\rho,K}(\ell+1/2)+1/4]_<,
\]

because \(2\nu=2\ell+1\) and the displayed set cardinality is precisely
the strict positive-integer bracket. The angular cutoff \(\nu<K\) is also
strict in both definitions. Hence no equality wall is changed during the
renaming from \(P_{\rm coarse}\) to \(P\).

The action agrees at both interfaces. The final source sets

\[
 G_a(z)=0\quad(z\ge a),
\]

whereas the main phase formula displays its elementary expression through
\(z=a\); that expression equals zero there. Thus both conventions give
\(G_a(a)=0\), and consequently the same \(A_{\rho,K}=G_K-G_{\rho K}\)
at \(z=\rho K\) and \(z=K\).

## 3. Phase reduction and strict spectral walls

The exact phase enumeration in the main proof is

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\ell\ge0}(2\ell+1)
 [\gamma_{\rho,K}(\ell+1/2)]_<.
\]

The analytic Bessel-phase enclosure gives, for every active order,

\[
 \gamma_{\rho,K}(\nu)
 <U_{\rho,K}(\nu)
 \le A_{\rho,K}(\nu)+\frac14.
\]

If a positive integer is strictly below \(\gamma\), it is therefore
strictly below \(A+1/4\), even when the second comparison is equality.
Termwise multiplication by the positive angular multiplicity proves

\[
 N_D(A_{\rho,1},K^2)\le P(\rho,K).
\]

Orders \(\nu=K\) are inactive in the phase theorem and are excluded by the
same strict cutoff in \(P\). A radial eigenfrequency exactly equal to \(K\)
is likewise excluded because both the exact phase count and \(N_D\) use a
strict spectral threshold. The non-strict bridge \(N_D\le P\) is sufficient
because the compact estimate proves the next inequality strictly.

The external Bessel-phase enclosure used here is an analytic published
theorem; it is not a numerical or executable certificate.

## 4. Exact identification of the Weyl target \(W\)

The final source defines

\[
 W(\rho,K)=\frac{2(1-\rho^3)K^3}{9\pi}.
\]

This is simultaneously:

1. the Dirichlet Weyl term for the unit-outer-radius spherical shell; and
2. the exact action integral in the phase/compact argument,
   \[
   \int_0^\infty2zA_{\rho,K}(z)\,dz
   =\frac{2}{9\pi}(K^3-(\rho K)^3).
   \]

Thus the structural identity \(W-P=\cdots\) and the final theorem use the
same quantity, with no volume, radius, or frequency normalization missing.

## 5. Compact theorem: premise and domain audit

All three compact notes use the same closed region

\[
 \mathcal R_c=
 \{\rho_c\le\rho\le39/50,\quad
   k_{11}(\rho)\le K\le200\}.
\]

The structural note proves

\[
 \mathcal E_{\rm ang}<\mathcal H\Longrightarrow P<W.
\]

The angular-block note proves on this region that the number of radial cells
is at least one and then obtains the strict bound

\[
 \mathcal E_{\rm ang}
 <B_{\rm ang}:=\frac{(1-\rho^2)K^2}{6}-\frac12.
\]

The scalar note proves, on exactly the same closed region,

\[
 \mathcal H-B_{\rm ang}>0.
\]

Consequently

\[
 \mathcal E_{\rm ang}<B_{\rm ang}<\mathcal H,
\]

so the structural implication yields \(P<W\), and the phase bridge yields
\(N_D<W\). Both outer ratio endpoints, the lower frequency face
\(K=k_{11}(\rho)\), and the upper face \(K=200\) are included by the proved
compact statements. Their positive margins are strict on those closed
faces; no limiting argument is being used.

The notation \(\mathcal B,\mathcal R_{\rm dec},\mathcal R_{\rm osc},
\mathcal E_{\rm ang},\mathcal H\) in the recalled proof refers to the
explicitly defined quantities in the three compact notes. The final closure
uses their proved implications, not an unproved sign assertion about those
symbols.

## 6. Aggregate theorem: premise and domain audit

The independently audited aggregate theorem states

\[
 N_D(A_{\rho,1},K^2)<W(\rho,K)
 \quad
 (\rho_c\le\rho\le39/50,\ K\ge200).
\]

Its proof analytically replaces the aggregate interval certificate with
the three exact base inequalities at \(K=200\), a strict positive curvature
bound, and exact integration. In particular, the theorem owns \(K=200\)
through the strict base value, and it owns both ratio endpoints. Therefore
the final closure's stated aggregate input is neither stronger nor broader
than the proved result.

The actual tail owner below uses \(K>200\), so it lies strictly inside the
aggregate frequency domain. The aggregate theorem's additional coverage of
\(K=200\) does not create an ownership overlap; proof domains may overlap
even though the subtraction owners are disjoint.

## 7. Exact residual and all inherited faces

Packet F proves symbolically, without a state enumeration,

\[
 \mathcal D_{20}
 =\{\rho_c\le\rho<39/50,\quad
 k_{11}(\rho)<K<U(\rho)\}.
\]

This matches equation (1) of the final source exactly. The accompanying
upper-owner packet proves \(U=K_0\) on this surviving ratio range, but the
closure never uses the formula for \(U\); only the inherited strict upper
inequality matters.

The face assignments are consistent:

- \(\rho=\rho_c\) remains in \(\mathcal D_{20}\), subject to the two strict
  frequency inequalities;
- \(\rho=39/50\) is optical-owned and is outside \(\mathcal D_{20}\);
- \(K=k_{11}(\rho)\) is staircase-owned and is outside
  \(\mathcal D_{20}\); and
- \(K=U(\rho)\) was excluded by the inherited strict upper inequality.

The compact and aggregate estimates deliberately include some of these
faces. Proving a closed superset does not change the exact subtraction
ownership.

## 8. Compact/tail partition and the \(K=200\) face

Within \(\mathcal D_{20}\), one always has
\(K>k_{11}(\rho)>0\). Therefore

\[
 \mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},\qquad
 \mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}
\]

are disjoint and exhaust \(\mathcal D_{20}\), even if an individual fibre
is empty. This remains true in all three possibilities
\(U(\rho)<200\), \(U(\rho)=200\), and \(U(\rho)>200\).

For a point in \(\mathcal C_{21}\), the inherited inequalities imply

\[
 \rho_c\le\rho<39/50,qquad
 k_{11}(\rho)<K\le200,
\]

which lies inside the compact theorem's closed domain. For a point in
\(\mathcal T_{21}\),

\[
 \rho_c\le\rho<39/50,qquad K>200,
\]

which lies inside the aggregate theorem's domain.

At \(K=200\), only \(\mathcal C_{21}\) can contain the point. The compact
theorem explicitly includes and proves that face strictly. If the inherited
condition \(K<U(\rho)\) or \(K>k_{11}(\rho)\) fails at 200, then there is no
such residual point; no alternative owner is needed. Thus the source's
boundary assignment is exact.

## 9. Strictness of the final conclusion

On the compact part,

\[
 N_D\le P<W
\]

implies \(N_D<W\). On the tail part, the aggregate theorem already gives
\(N_D<W\). Since every point of \(\mathcal D_{20}\) belongs to exactly one
of these sets, subtraction leaves no successor residual:

\[
 \mathcal D_{20}\setminus
 (\mathcal C_{21}\cup\mathcal T_{21})=\varnothing.
\]

All points of \(\mathcal D_{20}\) have \(K>0\), so there is no conflict
with the equality \(N_D=W=0\) at \(K=0\), which lies outside this final
residual.

## 10. Elimination of executable and interval-certificate premises

The two former interval certificates are replaced as follows:

- the 10,580-box compact certificate is replaced by the independently
  audited structural, angular-block, and scalar notes; and
- the 1,286-box aggregate certificate is replaced by the independently
  audited three-base-sign and curvature argument.

The 63-state subtraction table and its five interface rows are replaced by
Packet F's exact set proof. The rest of the 611-row exact ledger is also
covered by printed analytic packets. The unique-row census is

\[
 288+83+(57-10)+(58-36)+68+103=611.
\]

Here:

- Packets A/B cover 288 rows;
- Packet C covers 83 disjoint rows;
- Packet D covers 57 rows, ten of which are the lower-\(d\) cap identities
  already covered by A/B;
- Packet E covers 58 rows, 36 of which are optical identities already
  covered by A/B;
- Packet F covers the 68 exact-subtraction rows; and
- `ledger-main-visible.tex` covers the remaining 103 rows.

The only overlaps are the explicitly identified 10 and 36 general-identity
instances, so the union contains exactly all 611 predicates. Each current
packet has a PASS audit; Packet C and Packet D hashes include their audited
corrections. Executing the legacy verifier can authenticate the old registry,
but no verifier output is used to prove any displayed analytic lemma.

Finite rational tables remain in the proof only as printed exact algebra,
with hand-checking formulas and positive rational witnesses. That is an
analytic finite argument, not an executable or interval-certificate premise.

## 11. Edit log and verdict

No edit was made. The source's definitions, domains, strictness, and owner
assignments are correct as written.

**Final verdict: PASS.**

## 12. Compilation and final hashes

I compiled the unchanged source with the bundled Tectonic 0.16.9 workflow.
Tectonic completed the required reference reruns, and its final pass had no
undefined reference or LaTeX error. The output is a two-page PDF.

- Source SHA-256:
  `568E123178817DE1814095C719B5D7BCE90CFE3AFC48FEC6F97581D6AFAD6DC4`
- Compiled PDF: `manuscript/analytic/final-analytic-closure.pdf`
- PDF SHA-256:
  `250C6D1EFDF5C46FF770D9C427BECD488331EC9866DFFAA11FBCE8C96E190B4C`
