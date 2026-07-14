# Round 21 Candidate Final-Byte Isolation Audit

Verdict: **FAIL.**

First issue: the aggregate contract does not quantify (A24) consistently
with either its frozen per-box schema or its claimed all-frequency
propagation.  The exact candidate bytes are therefore **not released to A3
or A4**.

This audit used the sealed certificate artifacts only to compare theorem
interfaces, constants, schemas, byte identities, and the location of the
finite checks.  It did not import an incumbent proof verdict, audit
conclusion, or displayed numerical margin.

## 1. Frozen identities and baseline

The four supplied release artifacts reproduce exactly:

| artifact | bytes | reproduced SHA-256 |
|---|---:|---|
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `11809` | `e95145eb7ceeabbb467cf04eee3585c0f327cc4dea567a7016d686014e799630` |
| `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `7498` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `9573` | `15cb8e9f5e0b513e6f1fa9f9832bebee2d8a90ae1247ed8746837adb7a501472` |
| `rounds/polya-main/round_021/exploration/candidate-claim-freeze.md` | `5522` | `37abe5036cad7c9fde34994b3aa0b797f85ed8f3a694a580a6ae3e1d6c8a2922` |

The stated baseline
`0d4ee5d77e37e9e75490ac6e0e02ab338398fa00` exists and is a commit.  The
release commit has that commit as its immediate parent and adds exactly the
candidate, the two contracts, and the external freeze above.  All four
paths are tracked, repository-relative, distinct under Windows case
folding, and confined to the authorized candidate-release scope.

The accepted starting-set chain also reproduces exactly:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |

Every whitelisted foundation and source identity reproduces: completeness
`6fde758c...`, phase enclosure `96d0d466...`, weighted lattice
`a4f56f86...`, fixed-ratio high energy `0b834646...`, and the annuli source
card `95163883...`.  No path or hash disagreement was found.

## 2. First issue: (A24) has no consistent frequency quantifier

The aggregate contract first defines quantities depending on both
`rho` and `K`, including
`mu`, `S`, `I_KK`, `E_KK`, and `B_KK`.  It then says that the certificate
must prove (A23) and (A24) on the rational ratio superset.  Equation (A23)
explicitly evaluates the reserve and first derivative at `K=200`, whereas
(A24) leaves the frequency argument implicit:

$$
\mu>\frac32,
\quad 200\eta_\rho>1,
\quad S>\overline R>200\rho,
\quad I_{KK}<\frac{3b}{800},
\quad E_{KK}>0,
\quad \mathcal B_{KK}>F.
$$

Section 4 then labels **all of (A23)--(A24)** as the proof signs checked on
each of the 1,286 ratio boxes.  Static inspection of the authenticated
verifier bytes shows that those per-box checks call `evaluate_at_k0`, with
`K0 = 200`.  In particular, its checks of
`I_KK < 3b/(4K)`, `E_KK > 0`, and `B_KK > F` are evaluations at the single
base frequency `K=200`.  The sealed report metadata makes the same split:
the executable checks are at the base frequency, while the unbounded
frequency step is a separate analytic reduction.

Consequently neither possible reading is sound as a frozen contract:

- If (A24) means only `K=200`, then (A23)--(A24) do not imply that
  `B_K` and `B` stay positive for every `K>=200`; base positivity of
  `B_KK` supplies no such global control.
- If (A24) means every `K>=200`, then the ratio-only finite certificate does
  not certify the stated predicates, despite the schema calling them
  per-box proof signs.

The required replacement must separate the two obligations explicitly.
The finite outward boxes at `K=200` certify

$$
\mathcal B(\rho,200)>0,
\qquad
\mathcal B_K(\rho,200)>0,
\qquad
F(\rho)>0,
$$

together with any guards or derivative comparisons that are labelled
unambiguously as base-frequency checks.  Separately, A3 must analytically
derive, for every allowed `rho` and every `K>=200`,

$$
I_{KK}<\frac{3b}{4K}\leq\frac{3b}{800},
\qquad
E_{KK}>0,
\qquad
\mathcal B_{KK}>F.
$$

Those universally quantified inequalities, followed by the two integrations
from the base face, are the all-frequency propagation obligation.  A4 may
independently check the algebraic identities and replay the base certificate,
but a base-frequency interval check must not be described as the universal
analytic step.

Repairing the aggregate contract requires replacement bytes, a replacement
external freeze, and a new final-byte isolation audit before either isolated
review is credited.  The supplied files were not edited by this audit.

## 3. Alignments that passed before the first issue

The following checks found no earlier defect, but they do not cure Section
2:

- The candidate imports exactly
  $\mathcal D_{20}=\{\rho_c\leq\rho<39/50,\ k_{11}(\rho)<K<K_0(\rho)=U(\rho)\}$,
  with the accepted left/right and lower/upper face conventions.
- The candidate and compact contract agree on the closed theorem rectangle
  $[7/51,39/50]\times[12,200]$ and the strict spectral postcondition.
  The compact sealed bytes agree on schema
  `round21-compact-proxy-v2-half-open-faces`, 256-bit frozen precision,
  192-bit minimum, 10,580 leaves, actual depth 15, generation limits
  30/100,000, 16,020 corners, 2,153,076 Arb/integer comparisons, zero
  straddles, and digest
  `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`.
- The candidate and aggregate contract agree on
  $[\rho_c,39/50]\times[200,\infty)$ and the strict postcondition.  The
  sealed bytes agree on the rational superset `[7/51,39/50]`, split at
  `1/2`, base frequency 200, 192-bit frozen/minimum precision, width at most
  `1/2000`, and the exact `726 + 560 = 1286` ratio-box counts.  Its route,
  verifier, test, and report byte sizes and hashes all match the contract.
- The exact guards $7/51<\rho_c$ and $k_{11}(\rho)>12$ are correctly posed
  as reconstruction obligations.  With those guards, every point of
  $\mathcal D_{20}$ is compact-eligible for `K<=200` and aggregate-eligible
  for `K>200`.
- The sets
  $\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\}$ and
  $\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}$ are disjoint and exhaustive.
  The shared theorem face `K=200` is assigned only to the compact subtraction
  owner.  The candidate correctly handles all three possible orderings of
  `U(rho)` with 200 and does not require a value for that ordering.
- Every listed ratio and frequency face has consistent ownership:
  `rho=7/51` and `K=12` are theorem guard faces outside the live residual;
  `rho=rho_c` is inclusive; `rho=39/50`, `K=k11`, and `K=K0=U` are excluded
  from the live residual; and the proposed empty successor remains expressly
  contingent on later gates.
- The A3 whitelist and exclusions agree across candidate and freeze.  The
  contracts expose sealed executable/report identities to A3 only as hash
  strings, not as readable inputs.  A3 is assigned analytic reconstruction;
  A4 is assigned certificate authentication/replay, mutations, and exact-set
  logic.  Neither role is allowed to substitute an incumbent verdict for its
  assigned work.
- Any later patch is limited to scoped obligations
  `CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail`.
  `COMP-certified-bessel` remains `diagnostic_only`, and the candidate
  correctly reserves theorem-level clean-room, fresh theorem referee,
  theorem judge, and program-scope audit gates before any shell or program
  target can be promoted.

## 4. Isolation and byte hygiene

The candidate and contracts contain definitions, theorem predicates,
falsification obligations, and set bookkeeping, but no incumbent proof
prose, code excerpt, certificate success output, proof verdict, prior audit
conclusion, displayed proof margin, or leaked route derivation.  References
to incumbent paths occur only in the explicit exclusion lists or sealed A4
authentication tables.  The aggregate derivative formulas are presented as
reconstruction/checking obligations, not as an imported conclusion; the
failure in Section 2 is their missing quantifier and schema split, not a
proof leak.

Strict UTF-8 decoding of the four release artifacts, the three accepted
residual artifacts, and all sealed target artifacts succeeded.  None has a
BOM, forbidden C0 control, DEL byte, replacement character, common mojibake
marker, trailing whitespace, or missing final newline.  `git diff --check`
passed before this report was created.

## Final decision

**FAIL. First issue: the aggregate contract's (A24) predicates are
base-frequency certificate checks in the sealed implementation but are used
without an explicit frequency quantifier as though they supplied the
all-`K>=200` propagation.**  A corrected contract must distinguish the
finite `K=200` signs from the universally quantified analytic curvature
bound, then be refrozen and re-audited.  A3 and A4 remain unreleased on the
current bytes.
