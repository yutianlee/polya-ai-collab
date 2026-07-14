# Round 21 Exact-D20-Closure Candidate Freeze

Status: **FROZEN / RELEASED FOR ISOLATED REVIEW / NO PROOF VERDICT**.

Candidate baseline commit:
`0d4ee5d77e37e9e75490ac6e0e02ab338398fa00`.

This is a raw-byte release record. It freezes one proof-free candidate and
two proof-free certificate contracts. It supplies no theorem proof,
certificate validation, review conclusion, successor residual, judge
decision, or State Patch.

## 1. Frozen candidate bytes

| artifact | bytes | SHA-256 |
|---|---:|---|
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `11809` | `e95145eb7ceeabbb467cf04eee3585c0f327cc4dea567a7016d686014e799630` |
| `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `7498` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `9573` | `15cb8e9f5e0b513e6f1fa9f9832bebee2d8a90ae1247ed8746837adb7a501472` |

These three byte sequences are the only Round 21 candidate release target.
Any edit, including a status-only or whitespace edit, requires replacement
hashes, a replacement freeze, and a new final-byte audit.

## 2. Accepted starting-set boundary

The candidate imports the exact accepted residual only through:

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |

That accepted residual remains

$$
\mathcal D_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

This freeze does not change it.

## 3. Frozen claims only

The released bytes propose, without proving:

1. the compact theorem on the closed rectangle
   $[7/51,39/50]\times[12,200]$;
2. the aggregate theorem on
   $[\rho_c,39/50]\times[200,\infty)$;
3. the exact inequalities $7/51<\rho_c$ and
   $k_{11}(\rho)>12$ for $\rho\geq\rho_c$;
4. the disjoint owners

   $$
   \mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
   \qquad
   \mathcal T_{21}=\mathcal D_{20}\cap\{K>200\},
   $$

   with the shared theorem face $K=200$ assigned only to
   $\mathcal C_{21}$ for subtraction;
5. an empty successor residual as a proposal contingent on all later lemma
   review, judge, State-Patch, and derived-state gates.

The larger theorem domains are not redefinitions of $\mathcal D_{20}$.
The live residual is not declared empty by this release.

## 4. Isolated A3 release set

A3 may read only the three frozen candidate files in Section 1, the three
accepted residual files in Section 2, and these foundations:

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |

Elementary calculus, elementary one-dimensional summation, exact arithmetic,
and independently established rational enclosures for $\pi$ are also
allowed. The narrower source scopes are fixed inside the candidate and
contracts.

The verifier, test, report, and aggregate-route hashes visible in the
contracts are sealed A4 authentication targets. Hash visibility does not
authorize A3 to read those files.

## 5. Explicit exclusions from A3

Before its initial isolated response, A3 must not inspect:

- `rounds/polya-main/round_021/exploration/exact-d20-closure.md`;
- the aggregate route named only as a sealed dependency in its contract;
- either certificate verifier, test implementation, report, or adversarial
  audit;
- any Round 20 proof, executable proof ledger, source-proof note, audit,
  cross-comparison, referee report, judge file, or State Patch;
- any Round 21 cross-comparison, referee report, judge draft, or State Patch.

A3 is the analytic reconstruction role. A4 is the independent certificate
and exact-set validation role. Neither may substitute for the other.

## 6. Required later gates

After separate A3 and A4 work, the release requires a cross-comparison and a
fresh candidate referee. Only a later Round 21 lemma judge may propose
scoped obligations `CERT-round21-compact-proxy` and
`CERT-round21-aggregate-tail`; an independently audited and applied State
Patch is required before the accepted residual can change.

`COMP-certified-bessel` remains `diagnostic_only` and is not promoted by
this release. Even after exact D20 closure is accepted, separate
theorem-level clean-room and adversarial reviews, a later theorem judge, and
a separate program-scope audit are required before any of
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, or
`POLYA-program-target` may change status.

The frozen files contain the complete face and falsification lists. Decimal
displays, sampled floats, executable success, or agreement among agents do
not constitute a proof verdict.
