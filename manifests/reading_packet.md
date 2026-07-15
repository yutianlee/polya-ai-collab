# Reading Packet

Run: `polya-main`

Current phase: post-Round-21 theorem assembly (Round 22)

## Authoritative state

Read `state/proof_obligations.yml` first. Its SHA-256 is
`a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224`.
Commit `13e9534` applies the audited Round 21 lemma patch exactly once. The
graph has 60 obligations.

The graph records:

- `CERT-round21-compact-proxy`: `certified`;
- `CERT-round21-aggregate-tail`: `certified`;
- `SHELL-exact-d20-closure`: `proved_internal`; and
- `SHELL-rho-compact-analytic-envelope`: `proved_internal`, with exact
  successor residual $\mathcal D_{21}=\varnothing$.

The all-frequency theorem is not yet promoted. `SHELL-rho-compact`,
`SHELL-rho-uniformity`, `TARGET-shell-d3`, and `POLYA-program-target` remain
`open`. `COMP-certified-bessel` remains `diagnostic_only` and is detached
from the theorem path.

The graph's top-level `round_selection` prose is preserved historical
orchestrator metadata and still describes an earlier selection cycle. It is
not the Round 22 workflow authority. Use the current obligation statuses and
`next_action` fields together with the canonical order below.

## Accepted Round 21 result

With

$$
\rho_c=\frac1{1+2\pi},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_{11}(\rho)=\sqrt{z_\rho^2+132},
$$

the historical Round 20 residual was

$$
\mathcal D_{20}=
\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\right\}.
$$

The compact theorem is strict on

$$
\frac7{51}\le\rho\le\frac{39}{50},\qquad12\le K\le200,
$$

with 10,580 exact rational certificate leaves. The aggregate finite
certificate proves 1,286 base boxes at $K=200$ only. A separate analytic
derivative, curvature, and two-integration argument gives the strict tail on

$$
\rho_c\le\rho\le\frac{39}{50},\qquad K\ge200.
$$

The exact guards

$$
\frac7{51}<\rho_c,\qquad
k_{11}(\rho)>12\quad(\rho_c\le\rho<1)
$$

give the disjoint split

$$
\mathcal D_{20}=
(\mathcal D_{20}\cap\{K\le200\})\mathbin{\dot\cup}
(\mathcal D_{20}\cap\{K>200\}),
$$

with $K=200$ compact-owned. The faces $\rho=39/50$, $K=k_{11}$, and
$K=U$ were outside the residual and are not subtracted again. Thus

$$
\boxed{\mathcal D_{21}=\varnothing.}
$$

## Mandatory positive Round 21 evidence

Read the following in lifecycle order:

1. `state/lemma_packets/SHELL-rho-compact-round21.md`
2. `rounds/polya-main/round_021/exploration/residual-mask-freeze.md`
3. `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md`
4. `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md`
5. `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md`
6. `rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room-domain-addendum.md`
7. `computations/round21_verify_exact_d20_closure.py`
8. `computations/tests/test_round21_verify_exact_d20_closure.py`
9. `rounds/polya-main/round_021/reviews/exact-d20-closure-certificates-source-exec-replacement.md`
10. `rounds/polya-main/round_021/reviews/exact-d20-closure-source-exec-cross-comparison.md`
11. `rounds/polya-main/round_021/reviews/exact-d20-closure-adversarial-referee-source-exec.md`
12. `rounds/polya-main/round_021/reviews/exact-d20-closure-source-exec-provenance-audit.md`
13. `rounds/polya-main/round_021/judge/judge-021-lemma.md`
14. `rounds/polya-main/round_021/reviews/state-patch-lemma-audit-source-exec-final.md`
15. `rounds/polya-main/round_021/reviews/state-patch-lemma-application-audit.md`

Critical current SHA-256 values are:

- scoped candidate: `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d`;
- final wrapper: `31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9`;
- final wrapper tests: `4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99`;
- domain addendum: `395238c6db9267734f818a2493ed5370bd414c5c2994ea8e4f9bc406ff6d7241`;
- final A4 report: `47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5`;
- cross-comparison: `7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a`;
- fresh referee: `d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28`;
- provenance audit: `f4670818af3a57a965f0032edd72ea875d4ad618f9cc4a5b1b78cabdc7e481da`;
- final judge: `a620175fc43591cd80fcc9f50165d7b21596b077d92fbc4450167d21a4eca9aa`;
- pre-application patch audit: `bcd67c3939892c4014026c0ebc5103033bdd33dc68f67082f7bd32ef8c0d84fa`;
  and
- post-application audit: `c81fdc03124c3bd6c2b818b93810bd64b184b06735fd8a5cd72d59f0e0e158ef`.

The original A3 report is positive for its analytic reconstruction only when
paired with the domain addendum. Its superseded loader replay is not current
source-execution evidence. Likewise, predecessor compact audits remain usable
only for unchanged finite-certificate predicates under the final scope
overlays.

The compact and aggregate producer artifacts and their original independent
audits remain required inputs, but their scope is fixed:

- `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md`
- `computations/round21_certify_compact_proxy.py`
- `computations/tests/test_round21_certify_compact_proxy.py`
- `rounds/polya-main/round_021/certification/compact-proxy-rectangle-adversarial-audit.md`
- `rounds/polya-main/round_021/certification/aggregate-tail-global.md`
- `computations/round21_verify_aggregate_tail.py`
- `computations/tests/test_round21_verify_aggregate_tail.py`
- `rounds/polya-main/round_021/certification/aggregate-tail-global-adversarial-audit.md`

## Preserved negative chronology

These failures and superseded cycles are not promotion support:

1. the initial candidate had isolation ambiguity and inconsistent aggregate
   quantification;
2. the initial aggregate route omitted its spectral bridge;
3. the first exact audit left the Machin principal branch implicit;
4. its replacement lacked required mutation and lifecycle tests;
5. the first fresh referee missed that lifecycle defect;
6. a hardened-referee transcription incorrectly described its context as
   proof-free;
7. the candidate and first judge used the false or undefined unrestricted
   guard $k_{11}(\rho)>12$ for every $\rho\ge\rho_c$;
8. that domain repair made the preceding judge and patch audit stale; and
9. the first scoped source-loader cycle could hash `.py` while executing a
   timestamp-valid adjacent `.pyc`.

The final source-execution route reads the authenticated producer source once,
hashes those exact bytes, strict-decodes and compiles them directly, and
executes them without an import loader or cache. Its isolated tests force a
conflicting timestamp-valid `.pyc` and require source behavior. The domain
guard is now restricted to $\rho_c\le\rho<1$. Preserve the failed reports in
their original evidence buckets.

## Inputs for final theorem assembly

Use the canonical ratio split

$$
0<\rho\le\rho_*,\qquad
\rho_*<\rho<\frac78,\qquad
\frac78\le\rho<1.
$$

Mandatory theorem inputs include:

- small-hole endpoint:
  `state/lemma_packets/SHELL-rho-zero-endpoint.md`;
- compact history and Round 21 closure:
  `state/lemma_packets/SHELL-rho-compact-round20.md`,
  `state/lemma_packets/SHELL-combined-closure-round20-claim.md`, and the
  positive Round 21 chain above;
- thin endpoint:
  `state/lemma_packets/SHELL-rho-one-endpoint-round16.md`;
- strict spectrum/counting:
  `state/lemma_packets/SHELL-sturm-liouville-completeness.md` and the graph
  obligations `CONV-strict-counting` and `SHELL-count-floor-identity`; and
- normalization and scaling:
  `problems/polya_conjecture.md` and the audited Round 1 responses.

Handle $K=0$ before splitting ratios:

$$
N_D(A_{\rho,1},0)=0=\frac{2}{9\pi}(1-\rho^3)0^3.
$$

For $K>0$, retain the strict convention
$N_D(\Omega,\Lambda)=\#\{j:\lambda_j<\Lambda\}$. At a phase wall the count
is the strict floor, not the ordinary integer floor.

The theorem assembly must explicitly derive

$$
L_3=\frac1{6\pi^2},\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
$$

and scale from $A_{\rho,1}$ to arbitrary
$A_{r,R}=R A_{r/R,1}$.

## Prospective non-tiling/program evidence

These artifacts have not yet promoted the program target:

- `rounds/polya-main/round_021/exploration/spherical-shell-nontiling-route.md`
- `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room.md`
- `rounds/polya-main/round_021/reviews/spherical-shell-nontiling-clean-room-addendum.md`
- `rounds/polya-main/round_021/exploration/literature-scope-note.md`

The clean-room route argues non-tiling for every bounded shell $0<r<R$ under
the stated congruent, disjoint-interior, almost-everywhere-cover convention.
It still requires a separate adversarial geometric review and program-scope
audit. The limited literature search is not a novelty certificate; make no
priority claim.

## Canonical Round 22 order

1. Freeze and hash one proof-free theorem-assembly packet.
2. Independently audit its scope and dependency whitelist.
3. Run a fresh clean-room reconstruction of counting, complete cover, seams,
   $K=0$, normalization, and arbitrary-radius scaling.
4. Run an independent theorem-assembly/provenance audit.
5. Run a different fresh adversarial theorem referee instructed to assume
   `TARGET-shell-d3` false.
6. Run an adversarial non-tiling review and a separate program-scope audit.
7. Only after all reports pass, draft and independently audit a theorem State
   Patch, apply it once, regenerate derived state, and run full validation.

## Do-not-claim rules

- Do not infer a higher theorem status merely from accepted empty
  $\mathcal D_{21}$.
- Do not broaden $k_{11}(\rho)>12$ beyond $\rho_c\le\rho<1$.
- Do not call the aggregate finite boxes an all-$K$ certificate.
- Do not double-own $K=200$ or any inherited ratio/frequency face.
- Do not omit the strict counting convention or the equality case $K=0$.
- Do not claim arbitrary shells without the explicit scaling argument.
- Do not promote a diagnostic or parallel-track artifact by prose.
- Do not call tests, displayed decimals, or agent agreement proof.
- Do not claim novelty or publication priority.
