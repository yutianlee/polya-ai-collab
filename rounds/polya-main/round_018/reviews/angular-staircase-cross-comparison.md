# Round 18 A2/A3 Cross-Comparison

Date: 2026-07-14

Decision: **CONSISTENT / RELEASE ADVERSARIAL GATE**.

Compared byte-final artifacts:

| role | artifact | SHA-256 |
|---|---|---|
| frozen claim | `state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md` | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| A2 incumbent | `rounds/polya-main/round_018/responses/angular-staircase-incumbent.md` | `bbb1be54d3b0861442ca56b87022ef6c616fae45359914141128d871f1c42032` |
| A3 clean room | `rounds/polya-main/round_018/reviews/angular-staircase-clean-room.md` | `d94ca00eb41e4d1b33635cb8ef6a569bcfa0a70ed81549e8b4e9907483016660` |

The A3 verdict was fixed before access to A2, A4, the source-audit review,
computations, tests, certificates, Git state, or any other Round 18 review.

## Common implication chain

Both proofs independently establish:

1. the separated form lower bound
   $\lambda_{\ell,n}\ge n^2z_\rho^2+\ell(\ell+1)$;
2. the channel-preserving zero-extension comparison
   $\lambda_{\ell,1}^{\rm shell}\ge j_{\ell+1/2,1}^2$ with the correct
   min--max direction;
3. the strict Lorch consequences at $51/10$, $13/2$, and $15/2$;
4. exclusion of all $n\ge2$ and all $\ell\ge5$ through the closed
   $K=k_5$ face;
5. the exact cumulative caps $4,9,16,25$, including equality and
   cross-order multiplicity conventions;
6. strict Weyl payments using ratio splits $3/10,1/2,1/2$;
7. $k_5<U$ on every active upper-floor branch;
8. $\mathcal C_{18}\subset\mathcal D_{17}$ and the exact two-piece
   subtraction formula for $\mathcal D_{18}$.

No inequality direction, domain, cap, or face assignment conflicts between
the two reconstructions.

## Independent variance retained

- A2 differentiates a fully simplified moving-wall expression; A3
  differentiates $(1-\rho^3)(z_\rho^2+a)^{3/2}$. The two positive derivative
  criteria are algebraically equivalent on the stated range.
- A2 proves $K_0>64>26>k_5$ from the positive-root formula. A3 instead
  proves $\eta_\rho k_5<C_0<\eta_\rho K_0$ using an integral bound for
  $G_1$. Either route independently gives the required strict comparison.
- A2 and A3 use different rational lower witnesses for several moving-wall
  payments. Every displayed reserve in both files is positive; neither proof
  depends on the other's choice.
- A3 packages the delayed entries with
  $q_m=\max\{k_m,c_m\}$, while A2 lists the corresponding subcases. These
  partitions are equivalent, including empty and coincident subbands.

## Boundary comparison

Both assign $K=k_2$ to Round 17, include $K=k_3,k_4,k_5$ in the lower cap
by strict counting, include the spectral theorem at $\rho=7/8$ while leaving
that vertical face to the old endpoint owner, and make the new residual
strictly above $k_5$. Both leave the lower-ratio component unchanged and do
not subtract $B_0$ or $B_1$ again.

The common stopping point is methodological, not spectral evidence against
the conjecture: the one-radial-mode assertion cannot simply be carried to
$k_6$ at $\rho_c$ because the exact $\ell=0,n=2$ frequency $2z_{\rho_c}$
lies below $k_6(\rho_c)$.

## Release decision

The isolated and incumbent proofs agree on the exact claim and residual,
while retaining meaningful proof variance. Candidate C18 is released to a
fresh adversarial referee. This comparison does not itself promote the
lemma or modify the obligation graph.
