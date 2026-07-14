# Round 20 Combined Candidate-Claim Freeze

Status: **FROZEN / RELEASED FOR ISOLATED REVIEW**.

Candidate baseline commit:
`56e8d71ad3df2da6ab47ab1fefb8d758e076c69b`.

The `k_11` source-scope/adversarial gate is recorded at the baseline. An
independent proof-free scope audit passed before the status-only release
transition. This freeze gives no theorem or review verdict.

## Candidate and residual authentication

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `80b7ec55d71b54cd93a821cb27703b399f13d5a0dedf7bcbaaf854235a779002` |
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |

The residual packet, classifier, tests, and final residual freeze are
accepted bookkeeping only. They supply no Round 20 spectral estimate.

## Permitted clean-room inputs

If root review releases a final freeze, the first isolated reviewer may
receive only the candidate, the residual artifacts above, and these exact
foundational packets or source cards:

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/shell_weyl_bessel.md` | `ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade` |
| `sources/bessel_phase_enclosures.md` | `e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c` |

The exact DLMF identities and elementary internal tools additionally allowed
are frozen in Section 7 of the candidate. No broader source access is
implied.

## `k_11` release-gate metadata -- excluded from A3

The separate gate record is
`rounds/polya-main/round_020/exploration/high-k11-adversarial-audit.md`,
SHA-256
`515b57f7ad4c34a277c781770a7b60945fd345558ce5d4f592439e83fbd1a333`.

This hash records only that the pre-freeze release gate exists at the stated
baseline. The record, its source proof, and every artifact it reviews are
**excluded** from the first clean-room input set. It may not be used to
establish a zero bound, inventory, cap, payment, or theorem claim.

Other excluded artifacts include every Round 20 exploration proof,
`sources/round20_bessel_zero_bounds.md`,
`sources/round20_higher_radial_zero_bounds.md`,
`sources/round20_k10_zero_bounds.md`,
`sources/round20_k11_zero_bounds.md`, all incumbent responses, all constant
scripts or ledgers, all reviews, and every judge draft. Their presence in the
baseline commit does not make them permitted inputs.

## Proposed claim and exact subtraction

The candidate freezes only:

1. strict closure of both live lower components of `D_19`;
2. the closed high staircase
   `rho_c<=rho<=7/8`, `z_rho<=K<=k_11(rho)`, with genuinely new band
   `k_6(rho)<K<=k_11(rho)`;
3. the all-frequency theorem `39/50<=rho<1`, with equality only at `K=0`;
4. exact subtraction to the single proposed residual

   $$
   \left\{\rho_c\leq\rho<\frac{39}{50},
   \quad k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
   $$

All constants, zero reconstruction obligations, inventories, cap tables,
optical screens, provenance restrictions, and falsification faces are
contained in the authenticated candidate. None is proved by this draft.

## Isolation rule

After release, the first reviewer must authenticate the candidate and every
permitted file before reading them. It must not inspect an excluded artifact
until after returning an initial `PASS` or `FAIL` with the first unsupported
implication. A PASS requires independent reconstruction of all three theorem
claims, `k_11<U`, every strict face, and the exact set subtraction.

An exact-constant reviewer may begin only from the released candidate hash.
That review must distinguish analytic assumptions from finite arithmetic and
cannot replace the isolated analytic reconstruction.

## Independent gate and release rule

The independent pre-freeze scope audit is
`rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md`,
SHA-256
`819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467`.
It returned **PASS; first issue: none** on the draft claim, all hashes,
source scope, exact subtraction, face ownership, isolation boundary, and
absence of proof leakage. A separate final-byte audit must authenticate the
status-only transition before an isolated verdict is credited.

The candidate bytes named above are immutable for Round 20. Any correction
requires a replacement candidate, freeze record, and final-byte audit with
new hashes.
