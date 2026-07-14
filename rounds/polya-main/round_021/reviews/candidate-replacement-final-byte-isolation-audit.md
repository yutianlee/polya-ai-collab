# Round 21 Replacement Candidate Final-Byte Isolation Audit

Verdict: **PASS. First issue: none.**

The replacement bundle repairs the preserved isolation failure. The finite
outward certificate is now confined explicitly to $K=200$, while the
curvature bound and two integrations for every $K\geq200$ are separately
and unambiguously assigned to A3. These exact replacement bytes are released
to A3 and A4 only; this audit is not a theorem proof, certificate verdict,
successor-residual promotion, judge decision, or State Patch.

I used the sealed artifacts only to compare immutable identities, theorem
interfaces, schemas, constants, and the location of the finite checks. I did
not import an incumbent proof verdict, prior certificate-audit conclusion,
or displayed numerical margin.

## 1. Replacement identities and chronology

The replacement freeze reproduces all four current identities exactly:

| artifact | bytes | reproduced SHA-256 |
|---|---:|---|
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `12958` | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `7498` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `12270` | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |
| `rounds/polya-main/round_021/exploration/candidate-claim-freeze.md` | `8035` | `75afe7f0ea6ca2da4106510f6e90fb64a13a83fd83f023361d3433493d64558c` |

The replacement baseline
`a537991fd8d0418b8338388783f1a7462e0707f4` exists and is the immediate
parent of replacement commit
`868e09a1ca704bbfc354e3f54e867cd9a9b323d8`. That commit changes exactly
the candidate, aggregate contract, and external freeze. The compact contract
remains byte-identical to the first freeze and therefore correctly retains
its original historical baseline.

I also reproduced from the historical Git objects the rejected first
candidate (`11809`, `e95145eb...`), unchanged compact contract (`7498`,
`1d16d860...`), rejected aggregate contract (`9573`, `15cb8e9f...`), and
first freeze (`5522`, `37abe503...`). The preserved failure report exists at
the replacement baseline with 9,332 bytes and SHA-256
`601aa805838a683b5e440de11766eccc09a73b97112fd93d389427c84daaaf73`.
Thus the failure was preserved chronologically rather than overwritten.

The three accepted residual inputs reproduce:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |

All five A3-visible foundation/source identities also reproduce exactly:
completeness `6fde758c...`, phase enclosure `96d0d466...`, weighted lattice
`a4f56f86...`, fixed-ratio high energy `0b834646...`, and the annuli source
card `95163883...`.

## 2. The frequency split is now exact

### 2.1 Finite A4 certificate predicates

Section 3.1 of the replacement aggregate contract quantifies the finite
certificate at the **single frequency $K=200$**. Its principal signs are

$$
\mathcal B(\rho,200)>0,
\qquad
\mathcal B_K(\rho,200)>0,
\qquad
F(\rho)>0.
$$

Its guards and derivative consistency predicates are likewise labelled at
the base face:

$$
\mu_{200}=200\rho>\frac32,
\quad 200\eta_\rho>1,
\quad S(\rho,200)>\overline R(\rho,200)>200\rho,
$$

$$
I_{KK}(\rho,200)<\frac{3b}{800},
\quad E_{KK}(\rho,200)>0,
\quad \mathcal B_{KK}(\rho,200)>F(\rho).
$$

The contract additionally requires $1-\rho>0$ and outward containment of
both exact endpoints of every box. It says twice that these curvature checks
are base consistency only and cannot establish propagation above 200.

Static inspection of the authenticated verifier bytes matches this schema
exactly. The verifier fixes `K0 = 200`, calls `evaluate_at_k0` once per ratio
box, and checks precisely `1-rho`, `mu-3/2`, `K*eta-1`, `S-R`,
`R-rho*K`, `I_KK < 3b/(4K)`, `E_KK > 0`, `B_KK > F`, and the three
principal signs. Since that local `K` is exactly 200, the recorded
`I_KK` bound is exactly $3b/800$. Neither the verifier nor the replacement
schema makes a finite-box proof decision at $K>200$.

### 2.2 Universal A3 analytic predicates

Section 3.2 separately requires A3 to prove, for every

$$
\frac7{51}\leq\rho\leq\frac{39}{50},
\qquad K\geq200,
$$

the propagated guards and the exact chain

$$
I_{KK}
<\frac{3\rho b}{4S}
<\frac{3b}{4K}
\leq\frac{3b}{800},
\qquad E_{KK}>0,
$$

$$
\mathcal B_{KK}
>2\rho\eta_\rho+d_\rho\rho^2
-\frac{3(1+d_\rho)b}{4K}
\geq F(\rho).
$$

The logical dependencies are now correctly directed. $F(\rho)>0$ remains
an A4-validated base predicate; A3 must not relabel it as an analytic result.
Conditional on the separately validated base signs, A3 must perform both
integrations

$$
\mathcal B_K(\rho,K)
=\mathcal B_K(\rho,200)
+\int_{200}^{K}\mathcal B_{KK}(\rho,s)\,ds>0,
$$

$$
\mathcal B(\rho,K)
=\mathcal B(\rho,200)
+\int_{200}^{K}\mathcal B_K(\rho,s)\,ds>0
$$

for $K>200$, while the finite certificate owns $K=200$. The candidate
mirrors this division explicitly: A3 owns the universal derivation and
integrations; A4 authenticates and replays the base certificate, checks the
displayed derivative algebra independently, and verifies that no replayed
base curvature sign is promoted to an all-frequency result. This resolves
both readings that caused the first audit to fail.

## 3. Sealed-schema alignment

All sealed target identities and metadata reproduce without using their
verdict text.

The compact contract and target bytes agree on:

- theorem domain $[7/51,39/50]\times[12,200]$ and strict spectral count;
- schema `round21-compact-proxy-v2-half-open-faces`;
- frozen/minimum precision 256/192 bits;
- 10,580 exact leaves, actual depth 15, generation depth/box limits
  30/100,000;
- 16,020 distinct corners, 2,153,076 Arb/integer comparisons, and zero
  generated integer-wall straddles;
- canonical digest
  `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`;
- lower-closed/upper-open shared-face ownership with both root upper faces
  closed.

The aggregate contract and target bytes agree on:

- theorem domain $[\rho_c,39/50]\times[200,\infty)$ and strict spectral
  count;
- certified rational superset `[7/51,39/50]`, split exactly at `1/2`;
- base frequency 200 and frozen/minimum precision 192/192 bits;
- maximum exact width `1/2000`, 726 lower-branch boxes, 560 upper-branch
  boxes, and 1,286 total boxes;
- no standalone certificate digest;
- the exact route, verifier, test, and report byte sizes and SHA-256 values
  sealed in Sections 5--6.

The aggregate schema now describes only (A23), (A24a), (A24b), and
$1-\rho>0$ as finite per-box signs. It describes (A25)--(A30) as analytic
A3 obligations, so there is no remaining schema/verifier quantifier
mismatch.

## 4. Residual, faces, and proposed subtraction

The candidate, contracts, and freeze agree on the unchanged accepted set

$$
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

The compact theorem remains the closed rectangle
$[7/51,39/50]\times[12,200]$, and the aggregate theorem remains
$[\rho_c,39/50]\times[200,\infty)$. The exact inequalities
$7/51<\rho_c$ and $k_{11}(\rho)>12$ are reconstruction obligations, not
imported conclusions. Subject to those obligations, every residual point
with $K\leq200$ lies in the compact domain and every point with $K>200$ lies
in the aggregate domain.

The proposed owners

$$
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}
$$

are disjoint and exhaustive. Although both theorem domains include $K=200$,
that face is subtracted only by $\mathcal C_{21}$. The truth table remains
correct for $U<200$, $U=200$, and $U>200$; no ordering of $U$ with 200 is
assumed.

All outer and shared faces retain the correct status:

- $\rho=7/51$ and $K=12$ are included theorem guards but lie outside the
  live residual;
- $\rho=\rho_c$ is included subject to the two strict frequency bounds;
- $\rho=39/50$ is optical-owned and excluded from the residual;
- $K=k_{11}(\rho)$ and $K=K_0(\rho)=U(\rho)$ are excluded residual faces;
- $K=200$ is the unique compact subtraction face;
- the proposed successor residual is explicitly nonlive until all later
  gates pass.

## 5. Isolation, roles, and promotion scope

The A3 readable set is complete and consistent across candidate and
replacement freeze: the three frozen candidate/contract files, the three
accepted residual artifacts, the four whitelisted packets, the narrowly
scoped source card, and only the stated elementary tools. The incumbent
exploration, aggregate route, all certificate implementations and reports,
all certificate audits, the preserved failed isolation audit, Round 20 proof
materials, and later Round 21 review/judge/patch files remain excluded.
Seeing a sealed path or hash does not authorize A3 to open it.

A4 receives the sealed route and certificate targets for authentication and
replay, the exact face/subtraction obligations, and the explicit mutation
list. Its finite role cannot replace A3's analytic reconstruction. The
candidate requires cross-comparison and a fresh adversarial candidate
referee after both independent roles.

Any later promotion remains limited to narrowly scoped
`CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail` obligations.
`COMP-certified-bessel` remains `diagnostic_only` and cannot be promoted or
broadened. Even an accepted exact-D20 State Patch cannot promote
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, or
`POLYA-program-target` without the separately required theorem clean-room,
fresh theorem referee, theorem judge, and program-scope audit.

## 6. Proof-free content and hygiene

The replacement candidate and contracts contain theorem statements,
definitions, exact proposed predicates, falsification obligations, and set
bookkeeping. They contain no incumbent proof prose, code excerpt,
certificate success output, proof verdict, audit conclusion, displayed proof
margin, or leaked route proof. The new derivative inequalities and
integrations are explicitly labelled obligations that A3 must reconstruct;
they are not presented as imported results. Incumbent paths appear only in
exclusion lists or sealed A4 authentication tables.

Strict UTF-8 decoding succeeded for the four replacement release artifacts,
the preserved failed audit, the three accepted residual artifacts, and all
sealed target artifacts. None contains a BOM, forbidden C0 control, DEL
byte, replacement character, common mojibake marker, trailing whitespace,
or missing final newline. All paths are repository-contained and unique
under Windows case folding. `git diff --check` passed before this report was
created.

## Final decision

**PASS. First issue: none.** The replacement bundle authenticates correctly,
matches both sealed schemas, keeps every ratio/frequency face and review gate
exact, and cleanly separates A4's finite $K=200$ premises from A3's
universal $K\geq200$ reasoning. These exact bytes are released to A3 and A4
only. No theorem, residual, obligation, or project target is promoted by this
audit.
