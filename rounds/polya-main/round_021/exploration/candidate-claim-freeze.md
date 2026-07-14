# Round 21 Exact-D20-Closure Candidate Freeze

Status: **REPLACEMENT FROZEN / NOT RELEASED TO A3 OR A4 / NO PROOF VERDICT**.

Candidate baseline commit:
`a537991fd8d0418b8338388783f1a7462e0707f4`.

This is a replacement raw-byte freeze. It authenticates one proof-free
candidate and two proof-free certificate contracts after a preserved failed
isolation gate. It supplies no theorem proof, certificate validation, review
conclusion, successor residual, judge decision, or State Patch. A new
final-byte isolation audit is required before A3 or A4 may begin.

## 1. Frozen candidate bytes

| artifact | bytes | SHA-256 |
|---|---:|---|
| `state/lemma_packets/SHELL-exact-d20-closure-round21-claim.md` | `12958` | `415546156ea8d407541ddd6477ac38caa7c2c3b956724b25a06a755453e3b8a3` |
| `state/certificate_contracts/ROUND21-compact-proxy-contract.md` | `7498` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| `state/certificate_contracts/ROUND21-aggregate-tail-contract.md` | `12270` | `06b11887e7024d07023d9b8a4be97269536c833aecd126f469b2f54336238d6d` |

These three byte sequences are the only replacement Round 21 candidate
target. The compact contract is byte-identical to the first freeze.
Any edit, including a status-only or whitespace edit, requires replacement
hashes, a replacement freeze, and a new final-byte audit.

## 2. Preserved failure and replacement chronology

The first candidate freeze was committed at
`56e94b3f47d4ce1c83cf3b1fd47c1376a36526aa` against baseline
`0d4ee5d77e37e9e75490ac6e0e02ab338398fa00`. Its raw identities were:

| artifact | bytes | SHA-256 |
|---|---:|---|
| first candidate | `11809` | `e95145eb7ceeabbb467cf04eee3585c0f327cc4dea567a7016d686014e799630` |
| unchanged compact contract | `7498` | `1d16d860f158fd8223734245d4d6a71b8af2bc3ed99f9eafddf645e6a74b61fe` |
| first aggregate contract | `9573` | `15cb8e9f5e0b513e6f1fa9f9832bebee2d8a90ae1247ed8746837adb7a501472` |
| first external freeze | `5522` | `37abe5036cad7c9fde34994b3aa0b797f85ed8f3a694a580a6ae3e1d6c8a2922` |

The preserved isolation report
`rounds/polya-main/round_021/reviews/candidate-final-byte-isolation-audit.md`,
SHA-256
`601aa805838a683b5e440de11766eccc09a73b97112fd93d389427c84daaaf73`,
was committed at `a537991fd8d0418b8338388783f1a7462e0707f4` and rejected those
bytes. Its first issue was a missing frequency quantifier: finite outward
checks evaluated at $K=200$ were grouped with predicates needed for every
$K\geq200$.

The replacement aggregate contract now separates:

1. the 1,286 finite outward ratio boxes at the single base frequency
   $K=200$, including the three principal base signs, base guards, and
   derivative consistency signs; and
2. A3's analytic obligation, universally quantified for every allowed
   ratio and every $K\geq200$, including the curvature chain, guard
   propagation, and two integrations from the separately certified base
   signs.

The replacement candidate assigns the same separation to A3 and A4. A
replayed $K=200$ check of $I_{KK}$, $E_{KK}$, or $\mathcal B_{KK}$ is now
explicitly base consistency only and cannot establish unbounded-frequency
propagation. No theorem statement, residual set, subtraction owner, face,
dependency, sealed executable identity, or compact-contract byte changed.

The failed audit remains chronological evidence and is not a permitted A3
input. These replacement bytes remain unreleased pending a new isolation
audit.

## 3. Accepted starting-set boundary

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

## 4. Frozen claims only

The replacement bytes propose, without proving:

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

## 5. Conditional isolated A3 input set

Only if a new final-byte isolation audit releases this replacement may A3
begin. Its readable inputs are limited to the three frozen candidate files
in Section 1, the three accepted residual files in Section 3, and these
foundations:

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

## 6. Explicit exclusions from A3

If released, before its initial isolated response A3 must not inspect:

- `rounds/polya-main/round_021/exploration/exact-d20-closure.md`;
- the aggregate route named only as a sealed dependency in its contract;
- either certificate verifier, test implementation, report, or adversarial
  audit;
- any Round 20 proof, executable proof ledger, source-proof note, audit,
  cross-comparison, referee report, judge file, or State Patch;
- any Round 21 cross-comparison, referee report, judge draft, or State Patch.

A3 is the analytic reconstruction role. A4 is the independent certificate
and exact-set validation role. Neither may substitute for the other. Neither
role is released by this freeze alone.

## 7. Required later gates

After a new isolation audit releases the bytes and separate A3 and A4 work
is complete, the workflow requires a cross-comparison and a fresh candidate
referee. Only a later Round 21 lemma judge may propose scoped obligations
`CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail`; an
independently audited and applied State Patch is required before the
accepted residual can change.

`COMP-certified-bessel` remains `diagnostic_only` and is not promoted by
this release. Even after exact D20 closure is accepted, separate
theorem-level clean-room and adversarial reviews, a later theorem judge, and
a separate program-scope audit are required before any of
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, or
`POLYA-program-target` may change status.

The frozen files contain the complete face and falsification lists. Decimal
displays, sampled floats, executable success, or agreement among agents do
not constitute a proof verdict.
