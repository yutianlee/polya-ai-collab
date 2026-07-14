# Round 20 Combined-Closure Cross-Comparison

Date: 2026-07-15.

Verdict: **PASS / RELEASE FOR FRESH ADVERSARIAL REVIEW**.

First discrepancy affecting the frozen candidate after the completed repair
cycle: **none**.

This comparison was performed only after the isolated A3 verdict, its
preserved corrective addendum, the independent zero-provenance audit, and the
final repaired A4 bundle with its independent PASS re-audit were complete. It
compares those reconstructions line by line with the authenticated incumbent
lower, staircase, and optical workstreams and with the frozen candidate. It
does not promote the candidate and does not replace the required fresh-referee
gate.

## 1. Authenticated release objects

The frozen review target and its bookkeeping boundary reproduce exactly:

| role | artifact | SHA-256 |
|---|---|---|
| frozen candidate | `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| candidate freeze | `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| residual packet | `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| residual classifier | `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| residual tests | `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| residual freeze | `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| residual independent audit | `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |
| proof-free scope audit | `rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md` | `819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467` |
| replacement final-byte audit | `rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md` | `01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c` |

Every one of the candidate's fifteen permitted local input paths exists and
its current SHA-256 equals the displayed value. The replacement final-byte
audit also verifies that the only change from the failed first release was the
release-coherence paragraph and matching freeze metadata; no theorem,
constant, inventory, face, source boundary, or falsification obligation
changed.

## 2. Authenticated comparison evidence

### 2.1 Incumbent lower chain

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/exploration/small-hole-wedge.md` | `f1e5ab1c3671e82257a78cd2855581f326e4df98385539a69dc4b1a295a7f43b` |
| `rounds/polya-main/round_020/exploration/lower-next-wall.md` | `94099e852274ac697fa8c60563fbcdb0c4bb91a40c3de2c0af7556cbf7754e0a` |
| `rounds/polya-main/round_020/exploration/lower-remaining-gap.md` | `0baea820115061f3dbd5d46c0ca48271dce2df50885c83d5cd3a83c176f6e9c6` |
| `rounds/polya-main/round_020/exploration/lower-closure-crosscheck.md` | `ffde9721e1b0f238ea74e1af069041498deb15481f950618a85c6b5f236624b7` |
| `rounds/polya-main/round_020/exploration/integrity-audit.md` | `d44e05b422709a4913ec2bc376567b3beda2a31c4975ca535900f6d6781f10a6` |

### 2.2 Incumbent staircase and zero chain

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/exploration/high-next-wall.md` | `d7bb58554cf7505bc18415415b1ab21fa233b1707d9685b0a48bb58bbb2ab8a2` |
| `rounds/polya-main/round_020/exploration/high-lorch-extension.md` | `30aea82a3278683bdaf0c8d98b24b82276568d5d42435841833d79f4670f811c` |
| `rounds/polya-main/round_020/exploration/high-closure-crosscheck.md` | `9ad5b481ec147896a2861e3e55441e4a4114b3517a8fdbabb00451016eaf0403` |
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` |
| `rounds/polya-main/round_020/exploration/high-k9-adversarial-audit.md` | `b31a7b4d667992a4e02ffe4e5e5999cdfe611a8b67bd58ea57cdb22a4dc7f63d` |
| `rounds/polya-main/round_020/exploration/high-k10-repair.md` | `0e6fdadc57cdf8e173fb1dc1dad5a1403664833ae722a81b66ba59d5b202704a` |
| `rounds/polya-main/round_020/exploration/high-k10-adversarial-audit.md` | `9ec17b81aea3d6b6899dd25dd07f0241963ca8b246544080ecea08857c697bb1` |
| `rounds/polya-main/round_020/exploration/high-k11-extension.md` | `9faa7b75bb5b55cde24f63c613d03eb625457c9f99df03ad9a8bb563c9c22be1` |
| `rounds/polya-main/round_020/exploration/high-k11-adversarial-audit.md` | `515b57f7ad4c34a277c781770a7b60945fd345558ce5d4f592439e83fbd1a333` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` |
| `sources/round20_k11_zero_bounds.md` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` |

### 2.3 Incumbent optical chain

| artifact | SHA-256 |
|---|---|
| `rounds/polya-main/round_020/exploration/high-global-route.md` | `bbfc40bcb7ce748b946a6fdea7728315489d7e2e7842a0ccb6789f3f34fee6c4` |
| `rounds/polya-main/round_020/exploration/high-global-adversarial-audit.md` | `06f3b9efcc81c7d9bb51b2cb3ec6f0993ab6557e49438629215127557a690af8` |
| `rounds/polya-main/round_020/exploration/high-optical-optimization.md` | `6e6eb668cb284ede7ab6662b772af9004158d8d7098a83d549786823804ddc16` |
| `rounds/polya-main/round_020/exploration/high-optical-adversarial-audit.md` | `d7a92ae46d9e64cc9834e630f2db2dad16785552e66535c81b1ef7b5fd1c8b2a` |

### 2.4 Independent reconstructions and final A4 bundle

| role | artifact | SHA-256 |
|---|---|---|
| isolated A3 | `rounds/polya-main/round_020/reviews/combined-closure-clean-room.md` | `7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb` |
| preserved A3 correction | `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md` | `7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c` |
| independent zero/source audit | `rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md` | `2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8` |
| final A4 verifier | `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| final A4 focused tests | `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |
| final A4 report | `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95` |
| independent final A4 audit | `rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md` | `6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae` |

A3 authenticated the candidate and permitted boundary before reading it and
returned its initial verdict without an incumbent, computation ledger, prior
review, or judge artifact. The zero/source reviewer was independently isolated
within its narrower assigned slice. The original A4 review also began from the
released candidate and permitted files; its subsequent repair cycles are
explicitly post-verdict and are accepted only through the final independent
audit above.

## 3. Lower-closure comparison

All routes agree on the same exact disjoint allocation of the accepted lower
residual:

$$
\begin{aligned}
\mathcal D_{19}^{\rm low}={}&
\{\rho_*<\rho\leq\rho_0,\ L<K<U\}\\
&\mathbin{\dot\cup}\{\rho_0<\rho\leq\sigma,\ d<K<U\}\\
&\mathbin{\dot\cup}\{\sigma<\rho<\rho_c,\ d<K\leq\sqrt{114}\}\\
&\mathbin{\dot\cup}\{\sigma<\rho<\rho_c,\ \sqrt{114}<K<U\}.
\end{aligned}
$$

The first piece owns `rho=rho_0`, the second owns `rho=sigma`, and the
finite ledger owns `K=sqrt(114)`. The wedge reconstructs the pre-threshold
tail inequality, proves `omega_0 d>1`, obtains a one-unit floor gain, and
keeps the interface remainder strictly below `1/4`. The finite argument and
A3 independently reproduce the six complete multiplicity caps

$$45,\ 46,\ 59,\ 66,\ 69,\ 78,$$

with the moving `3z_rho` face on the lower-count side. They exclude first
channels `ell>=7`, second channels `ell>=5`, third channels `ell>=2`, and
all `n>=4` modes through the included endpoint.

Above `sqrt(114)`, the incumbent and A3 obtain the same exhaustive floor
criterion `m<=2p-1`. Its sole failure is

$$
\mathcal B=\{\sigma<\rho<\rho_c,\ K>\sqrt{114},\
\rho K\geq5/2,\ K<2/\omega_0\}.
$$

Both put a half-integer interface on the high side, put `rho K=5/2` in
`B`, and put `K=2/omega_0` in the aggregate branch. On `B` they reproduce
the complete proxy vector

$$
(6,5,5,4,4,3,3,3,2,2,1,1,1,1,0)
$$

and its multiplicity sum `395`; the incumbent, A3, and A4 each give a
strict payment. Thus both accepted lower components, including the complete
`rho=rho_0` fiber, are removed. No lower residual remains.

## 4. Zero provenance and high-staircase comparison

The incumbent source cards, A3, and the independent provenance audit agree on
the form domains, inequality directions, and preservation of radial index in

$$
q_{\ell,n}^2\geq n^2z_\rho^2+\ell(\ell+1),\qquad
q_{\ell,n}^2\geq j_{\ell+1/2,n}^2,
$$

$$
j_{p+1/2,n}^2\geq j_{\ell+1/2,n}^2
+p(p+1)-\ell(\ell+1).
$$

The independent zero audit reconstructs the positive-zero convention,
tangent-cell enumeration, ODE simplicity, exact half-integer recurrence
signs, and every strict rational wall in (19) and (27). It confirms that
Lorch is used only for qualified first-zero statements; no higher radial
zero, shell zero, angular propagation, multiplicity cap, or payment is
attributed to it.

All routes consequently agree on the nested checkpoint inventories:

| checkpoint | complete possible inventory |
|---|---|
| `k_7` | first `ell=0,...,6`; second `ell=0,1`; no `n>=3` |
| `k_8` | first `ell=0,...,7`; second `ell=0,...,3`; no `n>=3` |
| `k_9` | first `ell=0,...,8`; second `ell=0,...,4`; no `n>=3` |
| `k_10` | first `ell=0,...,9`; second `ell=0,...,5`; third `ell=0,1`; no `n>=4` |
| `k_11` | first `ell=0,...,10`; second `ell=0,...,4`; third `ell=0,1`; no `n>=4` |

Every numerical entry in the candidate's `k_8` and `k_9` matrices and its
`k_10` and `k_11` cap tables is the same full square-block sum in the
incumbents, A3, and final A4 ledger. The same incompatibilities, rational
localizations, algebraic split faces `z^2=16,68/3,34`, fixed/moving bridges,
and equality exclusions occur in all routes. In particular, the `k_11`
localizations agree: a second mode forces `rho<8/15`, a third mode forces
`rho<1/4`, `H=10` excludes all higher-radial modes, and `H=9` excludes
third modes.

The only substantive discrepancy inside the initial A3 report was its
sentence that every cap cell not displayed in its summary table had a larger
reserve. The candidate's conservative `k_9`, `H=6,h=4` cap-74 row has a
smaller positive coarse reserve. The immutable addendum corrects this exactly:
the full zero registry makes that cell empty, while the weaker retained ledger
independently pays it by

$$
\mathcal W\left(\frac7{20},\frac{207}{20}\right)
>74+\frac{727261673}{704000000}.
$$

This is the same payment already present in the authenticated incumbent
`k_9` proof. The final A4 verifier contains a connected thirteen-check path
for the printed conservative cell. Thus the report sentence is corrected
without changing the A3 theorem verdict or the frozen candidate.

The exact band union is therefore

$$
\{\rho_c\leq\rho<7/8,\ k_6<K\leq k_{11}\},
$$

with `k_6` predecessor-owned and `k_11` newly owned. Every route proves
`k_11<U` on the whole live high strip.

## 5. Optical comparison

The repaired incumbent optical route, its two adversarial audits, A3, and A4
agree on

$$
\varepsilon_0=\frac{11}{50},\qquad
C_D=\frac{1382}{3125},\qquad
c=\frac{1126}{625},\qquad q=\frac{106}{333}.
$$

They independently reconstruct the exact product deficit

$$D(a)>\frac{1382}{3125}a^2\qquad(a>\pi),$$

including the `(N,t)=(m-1,1)` convention at `a=m pi`. The inclusive low
and high screens meet at `a=c/epsilon`, and their endpoint reserves are

$$
R_L=\frac{39569}{2772225000}>0,
\qquad
R_H=\frac{14817541}{472867032960000}>0.
$$

The high screen uses the same complementary-action curvature, Stieltjes
radial deficit, exact half-integer layer count, angular ceiling, and phase
transfer in every reconstruction. No Round 16 endpoint conclusion is
extrapolated beyond its proved ratio range. The common optical face,
`epsilon=11/50`, all radial and angular equality walls, and `K=0` are owned.
Consequently

$$
\frac{39}{50}\leq\rho<1,\quad K\geq0
\quad\Longrightarrow\quad
N_D\leq\mathcal W,
$$

with equality only at `K=0` and strict comparison for `K>0`.

## 6. Final A4 repair and failure chronology

The positive computational evidence is only the final bundle authenticated in
Section 2.4. Its normal run reports

$$
587=488\text{ substantive}+65\text{ bookkeeping}+34\text{ authentication}
$$

passing checks, and the seventeen focused tests pass. The independent final
audit confirms exact expected sides at all seventeen named rational
localization faces, input sensitivity, the cap-74 wrong-wall failure gate,
strict UTF-8/final-byte hygiene, and a visibly unauthenticated skip-hash mode.

The two earlier A4 failures remain part of the chronology and supply no
positive release evidence:

1. `combined-closure-constants-adversarial-audit.md`, SHA-256
   `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd`,
   rejected the original verifier because it paid only 73 in the live
   cap-74 cell and because several labels were tautological or disconnected.
2. `combined-closure-constants-replacement-audit.md`, SHA-256
   `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31`,
   rejected the first replacement bundle because of an actual `0x08` byte,
   localization predicates that survived an expected-output mutation, an
   insufficient wrong-wall equality test, and authenticated-looking
   skip-hash output.

The second repair closes every one of those defects. The final audit at
`6322802e...` independently reruns the surviving mutations and kills them in
the repaired tests. Neither preserved FAIL is reinterpreted or overwritten.

## 7. Exact subtraction and face ledger

The authenticated starting set is

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\leq\rho_0,\ L<K<U\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U\}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6<K<U\}.
\end{aligned}
$$

The lower theorem removes the first two disjuncts. Since `k_11<U`, the
staircase removes exactly `k_6<K<=k_11` from the third disjunct and leaves
`k_11<K<U`. The optical theorem then removes exactly the ratios
`39/50<=rho<7/8`, including the `39/50` face. Therefore

$$
\boxed{
\mathcal D_{19}\setminus
\left(\mathcal D_{19}^{\rm low}
\cup\mathcal C_{20}^{\rm stair}
\cup\mathcal C_{20}^{\rm opt}\right)
=\mathcal D_{20},}
$$

where

$$
\boxed{
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
$$

The normalization is exact because `rho_c>omega_0` and
`39/50<5/6`, so neither `H_0` nor the seam branch is eligible on the
remaining interval. Face ownership agrees everywhere:

- `rho=rho_0` is removed by the first lower component; `rho=rho_c`
  remains in `D20`; `rho=39/50` is optical-owned; `rho=7/8` is inherited;
- `K=L` and `K=d` retain predecessor owners, `K=k_6` is predecessor-owned,
  `K=k_11` is staircase-owned, and `K=U` remains excluded;
- `B0` and `B1` were already absorbed by the predecessor and are not
  subtracted again.

No point is lost, duplicated as an uncovered face, or assigned to an
ineligible upper-floor branch.

## 8. Classified non-release discrepancies

The comparison records the following non-release defects without modifying
any immutable evidence.

1. The A3 comparative-reserve sentence is a mathematical statement about
   its summary, not about the theorem. It is explicitly corrected by the
   authenticated addendum and by the final A4 cap-74 path, as described in
   Section 4.
2. A3 equation (A8) omits the printed `+` immediately before `delta`, and
   (A19) prints `quad` twice without the TeX backslash. The definitions,
   surrounding prose, subsequent inequalities, incumbent formulas, and A4
   checks all use the unambiguous intended expressions. These are
   presentation-only defects.
3. The authenticated `k_10` adversarial report contains the presentation
   fragments `>left(...)` and `;qquad`; the `k_11` adversarial report has
   several superscripts printed as `^{,2}`. Their displayed rational values,
   source scopes, inventories, and conclusions are independently reproduced
   by A3, the zero audit, and A4. They are presentation-only and occur in
   excluded incumbent evidence, not in the frozen candidate.
4. The early `k_8` audit notes that an incumbent obstruction line stated the
   weaker `k_7<C_6<k_9`; the audit proves the actually needed
   `k_8<C_6<k_9`. This affected only the historical method-obstruction
   discussion, not any proved band or candidate claim.
5. Before their authenticated final hashes, the lower remainder endpoint,
   a high-note TeX sequence, a high-crosscheck control/formula defect, and the
   global-route floor provenance were repaired and independently re-audited.
   The candidate's first status-only release was likewise rejected for
   circular release prose and replaced. Those superseded bytes remain in Git
   history and are not used here.

No mathematical, provenance, face, constant, isolation, or byte discrepancy
remains in the frozen candidate plus the accepted A3/addendum, zero audit, and
final A4 bundle.

## 9. Release decision

The immutable Round 20 candidate is released to a fresh adversarial referee
who participated in neither incumbent development, A3 reconstruction, zero
provenance review, A4 development, nor this cross-comparison. That referee
must assume the candidate false and recheck every source boundary, analytic
reduction, zero enumeration, inventory, payment, strict face, optical screen,
upper-floor branch, and residual subtraction.

**Promotion is not authorized before that fresh referee returns PASS and the
remaining judge and State Patch gates succeed.**
