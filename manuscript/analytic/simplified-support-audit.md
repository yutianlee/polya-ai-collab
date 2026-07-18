# Simplified analytic-support audit

**Verdict: PASS**

Audit date: 2026-07-16 (Asia/Shanghai).

The 62-page support volume is internally consistent after removal of the former aggregate Parts X--XIII. The current master contains exactly Parts I--X; Parts VII--IX are the current all-frequency analytic modules, Packet F gives the current exact owner subtraction, and Part X is the current final closure. I found no stale aggregate premise, unowned boundary face, logical cycle, omitted internal dependency, source/PDF mismatch, or assembly defect.

This is an artifact, provenance, and dependency audit. It is not a substitute for an independent line-by-line referee verification of every analytic inequality or for an external novelty review.

## Audited artifacts

Current release candidate:

- PDF: `tmp/final-analytic-20260716/support-v3/spherical-shell-polya-analytic-supplement.pdf`
- SHA-256: `311B078B1BB08BF021E9D5B4721A0448DC3C4419BC457B85916551CF288848CC`
- Size: 719,624 bytes
- Geometry/security: 62 A4 pages, zero rotation, unencrypted, no forms, no JavaScript

Current master source:

- Source: `manuscript/spherical-shell-polya-analytic-supplement.tex`
- SHA-256: `36C07A5B0828A20898C721AA92C8100A7E0104F3ABE3D7D1EFD2BF5181250F09`
- Size: 5,590 bytes

The earlier staging PDF requested in the audit also exists:

- `tmp/simplified-final-support/spherical-shell-polya-analytic-supplement.pdf`
- SHA-256: `6508D56D924008C943C2B4DA791E0F6E35D73C8644374D2406D027D742EF5007`
- Size: 726,056 bytes

It was superseded during the audit by `support-v3`; the verdict and provenance table below are frozen against `support-v3`.

## Inclusion order and source/PDF provenance

For every part, the text extracted from its page interval in the 62-page release is exactly equal, after raw whitespace normalization, to the text extracted from the current standalone compiled PDF. Thus the master embeds the current all-\(K\) sources, not obsolete aggregate or finite-window versions.

| Part | Master pages | Current source | Source SHA-256 | Current standalone PDF SHA-256 | Result |
|---|---:|---|---|---|---|
| I | 3--9 | `ledger-main-visible.tex` | `4A0B1CBEEF5B0CBF4D5317DA9640CF6443A8B735EC1834FACDC513C262C97F92` | `1D200863789694EE359A29903206A743B966127D385DEE45C9EE3AC698D822D3` | PASS |
| II | 10--18 | `ledger-packets-AB.tex` | `B5D21260D757D299ACB22EF3A0FD26D3A95A88AE3B0365988E5CBECD787EB6A6` | `D8555026D813274C518DD2FFC97299D645775B04FA5162ED1BDDF402E7087CA3` | PASS |
| III | 19--25 | `ledger-packet-C.tex` | `131A0F84C5CD38881487DC6AA410401B068E824EE855652281A1A61756BFC776` | `60D4D0817A5B74542AF78F85A2D7AC9ECD1B82FC68877D3BECB1C8142B39E21F` | PASS |
| IV | 26--31 | `ledger-packet-D.tex` | `94EE66A7A1A71BC760433C5B88F9F66060C5B405EB915AB17667D9C7E617C966` | `A7596B0133A99A51B6B93285DB227AA1C78065CECDC220E02BC6C19186E07B62` | PASS |
| V | 32--36 | `ledger-packet-E.tex` | `03259745FBF8D67930045B4F996DDF9F61A2F5A74E72CF7A95064351E59A6123` | `58AAD400B7A4DF7838661AE1B6083D33FF95606F68A3B0D88BFA276D6E99E54C` | PASS |
| VI | 37--39 | `ledger-packet-F.tex` | `393589B89C4F3361B85CDBEC97FAD7AD16E64488ACDA7A4CBEB0DA9FEFD16049` | `3878E441944D6D46349727A2B61245C0C5865B6E9854245B971931892A099913` | PASS |
| VII | 40--45 | `compact-structural.tex` | `1055BA25A6E7F97F2F49EF250EF7589C45D0251B8AF50A5E0FF59B36C6BF722C` | `C5C0CD3C5685B28087A1D78CD2EE5164F89616CB515A37AF27E389DDC27FBB3D` | PASS |
| VIII | 46--51 | `compact-angular-block.tex` | `382DF2F006D432902BD68582C3305E5006D701C3D24703E16760E8DCA7FB12CE` | `0A110E9B4FF4B7CC57E26FDAF2ED0858F8E722140F8ADDAB757EA369CC2E639C` | PASS |
| IX | 52--59 | `compact-scalar-positive.tex` | `0C77FF2C3431269AB2080CE632613F1B21AA061A086C0AE812B8428AC238EDEA` | `F2CD839652C3F9BF5E73D0A14CC2B6ADCD7B3B8906F08572F947203A6104C290` | PASS |
| X | 60--62 | `final-analytic-closure.tex` | `C0518CF17F0CBB20F92BA87E94C24BDB8873696EE6C9FA6BF134C4F5E631A7FB` | `03BF1787BF3A8B15301ACAE7D5F7AA74BBDA63F7112957552163D9D215DB2DB2` | PASS |

The global census occupies page 1 and the table of contents page 2. The contents order and page numbers agree with the physical PDF. Roman labels I--X are clean, and the generated bookmarks consist of the census plus the ten parts in the same order.

## Independent build check

An independent XeLaTeX build of the current master produced:

- `tmp/pdfs/support-v3-master-fresh/spherical-shell-polya-analytic-supplement.pdf`
- SHA-256: `5DB28C5A452BF14F5763A487EDDD02A92FA60B66E0D8B43A2D82789BE243B10B`
- 62 pages
- zero final-pass LaTeX warnings/errors

Its complete extracted text is exactly equal, after raw whitespace normalization, to the release PDF (77,690 characters in each). The binary hash differs as expected because PDF metadata and object layout are regenerated.

Fresh independent builds of the current Packet D, Packet F, structural, angular-block, scalar-positivity, and final-closure sources also succeeded and text-matched their current standalone PDFs. In particular, Parts VII--IX are reproducibly built from the current all-frequency sources.

## Logical dependency audit

The live dependency chain is acyclic:

1. Parts I--V establish the accepted owner regions and ledger obligations.
2. Part VI performs exact set subtraction and obtains
   \[
   D_{20}=\{\rho_c\leq\rho<\rho_{\mathrm{opt}},\ k_{11}(\rho)<K<U(\rho)\}.
   \]
3. Part VII gives the global structural implication \(\mathcal E_{\mathrm{ang}}<\mathcal H\Rightarrow P<W\) for every \(0<\rho<1\), \(K>0\).
4. Part VIII gives the global angular estimate
   \[
   \mathcal E_{\mathrm{ang}}<\frac{(1-\rho^2)K^2}{6}-\frac N2,
   \]
   and on the retained region \(N\geq1\), hence \(\mathcal E_{\mathrm{ang}}<M_c\).
5. Part IX proves \(\mathcal H-M_c>0\) on the closed, upward-closed region
   \[
   \rho_c\leq\rho\leq\frac{39}{50},\qquad K\geq k_{11}(\rho),
   \]
   with no upper cutoff in \(K\).
6. Part X combines \(\mathcal E_{\mathrm{ang}}<M_c<\mathcal H\), Part VII, the earlier main-proof phase bridge \(N_D\leq P\), and the Part VI inclusion of \(D_{20}\) in the retained region.

Parts VII--IX do not use Packet F, \(D_{20}\), or an aggregate branch as a premise. Packet F's exact set subtraction is independent of Parts VII--IX; its reference to their later theorem is a forward use, not a proof dependency. Part X explicitly identifies its two earlier inputs--the main-proof phase bridge and the owner/subtraction result--so neither is silently omitted. The earlier inputs do not depend on Part X. No cycle was found.

## Boundary ownership

Packet F's current decomposition is consistent:

- The high component is already restricted to \(\rho<\rho_{\mathrm{opt}}\); no second optical subtraction is made.
- \(\rho=\rho_c\) remains in \(D_{20}\).
- \(\rho=\rho_{\mathrm{opt}}\) is absent from \(D_{20}\), while Parts VII--IX prove the stronger closed-face statement.
- \(K=k_{11}(\rho)\) is staircase-owned and excluded from \(D_{20}\).
- \(K=U(\rho)\) is excluded from the inherited residual.
- Therefore \(D_{20}\subseteq\{\rho_c\leq\rho\leq39/50,\ K\geq k_{11}(\rho)\}\) exactly as used by Part X.

No live spectral premise \(K\leq200\) or \(K=200\) occurs in Parts VII--X. The only textual appearances of old certificate counts or frequency splits are historical/status statements explicitly saying that those devices are not used.

## Census and removed aggregate material

The global census remains arithmetically consistent:

- family total: \(553+58=611\);
- owner total: \(103+278+83+57+22+68=611\).

The former aggregate Parts X--XIII are not included in the master. The current master abstract correctly describes Parts I--VI as ledger/ownership support, Parts VII--IX as the retained-remainder theorem, and Part X as final closure. Aggregate computation is mentioned only as retired or optional regression evidence, never as a premise.

## PDF render inspection

Rendered boundary and transition pages 1, 2, 26, 31, 37, 39, 40, 45, 46, 51, 52, 59, 60, and 62 were visually inspected. This covers the census/contents, Packet D boundaries, Packet F boundaries, the starts and ends of Parts VII--IX, and the final closure. No clipping, overlap, wrong orientation, malformed table/formula, broken transition, or stale part heading was found.

## Final determination

**PASS.** The current 62-page `support-v3` PDF is the correct simplified analytic supplement for review: current source-to-PDF provenance is intact, Parts VII--IX are the all-frequency analytic route, Packet F and Part X use the same residual geometry, the TOC and physical order agree, and the closure dependency graph has neither a cycle nor a missing internal edge.
