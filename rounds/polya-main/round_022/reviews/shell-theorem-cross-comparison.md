# Round 22 shell-theorem cross-comparison

Date: 2026-07-15

## Verdict

**PASS. First discrepancy affecting the theorem: none.**

This comparison reconciles the incumbent, isolated clean-room proof, and
independent assembly/provenance audit before the fresh adversarial theorem
referee. It creates no theorem or graph promotion.

## Authenticated inputs

| artifact | SHA-256 |
| --- | --- |
| frozen theorem packet | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` |
| claim-scope audit | `b8c8f23adc44c4a91497f740700e171e1211bc38eac32f12926c11af5e02a0c6` |
| incumbent assembly | `4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b` |
| isolated clean-room proof | `9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12` |
| assembly/provenance audit | `2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56` |
| authoritative graph | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` |

The clean-room report explicitly did not read the incumbent, another Round 22
review, the synthesis draft, current-state prose, next-round prompts, or a
judge. The A4 auditor explicitly did not read the clean-room report before
forming its verdict. Their agreement is therefore not inherited consensus.

## Claim and outer partition

All three reconstructions prove exactly

$$
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3
\qquad(0<\rho<1,\ K\ge0)
$$

under strict counting. They use the same disjoint outer owners

$$
(0,\rho_*],\qquad(\rho_*,7/8),\qquad[7/8,1),
$$

with $\rho_*$ small-hole-owned and $7/8$ thin-shell-owned.

The incumbent proves $0<\rho_*<1/6<7/8$. The clean-room proof independently
obtains the stronger but unnecessary $0<\rho_*<1/24<7/8$. The different
upper estimates are compatible and both establish exactly the ordering the
packet requires. A4 independently validates the incumbent chain.

## Zero frequency and strict thresholds

Every report handles $K=0$ before the ratio split. Positivity of the promoted
Dirichlet spectrum gives

$$
N_D(A_{\rho,1},0)=0=W(\rho,0).
$$

For positive frequency, every report preserves
$N_D(\Omega,\Lambda)=\#\{j:\lambda_j<\Lambda\}$ with multiplicity. At an
integer phase wall the channel count is $m-1$, not the ordinary floor $m$;
at a cross-channel coincidence all equal threshold modes remain excluded and
their multiplicities enter together only above the wall. No proof uses
continuity across a spectral jump.

## Compact-middle reconstruction

The incumbent invokes the promoted complete cover
`SHELL-rho-compact-analytic-envelope` and then unpacks the final
$\mathcal D_{20}$ subtraction and its critical faces. The clean-room proof
goes further: it independently reconstructs the exact chain

$$
\mathcal D_{16}\supset\mathcal D_{17}\supset\mathcal D_{18}
\supset\mathcal D_{19}\supset\mathcal D_{20}supset
\mathcal D_{21}=\varnothing,
$$

including $\rho_0$, $\rho_c$, $39/50$, the $H_0/K_0$ switch, the seam at
$5/6$, every staircase face through $k_{11}$, and the inherited upper floor
$U$. A4 authenticates that complete predecessor union and confirms that the
incumbent's abstract $\mathcal A_{21}$ invocation is licensed by the promoted
envelope rather than by an open target or rectangular proxy. The difference
is expository depth, not mathematical scope.

All reports agree on the final cell

$$
\mathcal D_{20}
=\{\rho_c\le\rho<39/50,\ k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}
$$

and its disjoint owners

$$
\mathcal D_{20}\cap\{K\le200\},
\qquad
\mathcal D_{20}\cap\{K>200\}.
$$

The shared theorem face $K=200$ is compact subtraction-owned. The faces
$\rho=39/50$, $K=k_{11}(\rho)$, and $K=U(\rho)$ were already outside the
residual. The scoped guard is used only for $\rho_c\le\rho<1$.

## Certificate and provenance boundary

There is no evidence-role discrepancy:

- the compact computation owns 10,580 finite leaves on its closed rectangle;
- the aggregate computation owns 1,286 finite base boxes at $K=200$ only;
- promoted analytic bridges own the spectral transfers and all
  $K\ge200$ propagation; and
- the final source-execution wrapper owns authentication and finite replay.

A4 reauthenticated the final wrapper and replayed the full 384-bit proof
path. It also reran the malicious timestamp-`.pyc`, module-restoration, exact
guard, face-row, three-$U$-ordering, and unique-$K=200$ tests. Superseded
unscoped, stale-hash, and cache-vulnerable cycles remain negative evidence.

## Normalization and dilation

Every reconstruction derives

$$
L_3=\frac1{6\pi^2},\qquad
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),\qquad
L_3|A_{\rho,1}|=\frac{2}{9\pi}(1-\rho^3).
$$

With $K=\sqrt\Lambda$, all obtain $K^3=\Lambda^{3/2}$, including
$\Lambda=0$. For $\rho=r/R$, all obtain

$$
\lambda_j(A_{r,R})=R^{-2}\lambda_j(A_{\rho,1}),
\qquad
N_D(A_{r,R},\Lambda)=N_D(A_{\rho,1},R^2\Lambda),
$$

and hence

$$
N_D(A_{r,R},\Lambda)
\le L_3|A_{r,R}|\Lambda^{3/2}
$$

for every $0<r<R$ and every $R>0$, including $R<1$.

## Status and next gate

The reports agree that `SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, and `POLYA-program-target` remain open. The spectral
theorem reviews do not prove non-tiling, novelty, or another project track.

The theorem packet, two independent proof paths, exact provenance replay,
and this comparison are consistent. They are ready for a different fresh
referee instructed to assume the theorem false and identify the first
unsupported implication.

**Final verdict: PASS. First discrepancy affecting the theorem: none.**
