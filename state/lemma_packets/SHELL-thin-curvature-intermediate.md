# Lemma Packet: Complete Thin-Shell Endpoint

Obligations: SHELL-thin-curvature-intermediate and
SHELL-rho-one-endpoint.

Rounds: 5--6, strengthened in Round 9.

## Statement

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{15625}.
$$

Then, for every $K\ge0$,

$$
\boxed{
N_D(A_{\rho,1},K^2)
\le
\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{1}
$$

Equivalently, the complete all-frequency endpoint is

$$
\boxed{
1-\frac1{15625}\le\rho<1.
}
\tag{2}
$$

The lower endpoint is included.  The value $\rho=1$ is excluded as the
degenerate zero-width limit.

## Permitted proved inputs

1. The strict spectral convention and exact separated shell spectrum.
2. SHELL-thin-product-low-optical.
3. SHELL-thin-action-aggregate, which proves (1) through

   $$
   0\le K\le\frac1{8\varepsilon^{5/2}}
   \qquad
   \left(0<\varepsilon\le\frac1{100}\right).
   \tag{3}
   $$

4. SHELL-thin-local-plateau-optimized, which proves (1) throughout

   $$
   K\ge\frac{125}{8\varepsilon^2}
   \qquad
   \left(0<\varepsilon\le\frac1{100}\right).
   \tag{4}
   $$

The old Round 6 theorem with threshold $64\varepsilon^{-2}$ remains valid
historical evidence but is not used to prove the strengthened endpoint.

## Exact overlap

The inclusive ranges (3) and (4) cover every $K\ge0$ exactly when

$$
\frac{125}{8\varepsilon^2}
\le
\frac1{8\varepsilon^{5/2}}.
$$

This is equivalent to

$$
125\sqrt\varepsilon\le1,
$$

and hence to

$$
\varepsilon\le\frac1{15625}.
$$

At equality, both thresholds are

$$
K_{\rm join}=\frac{125^5}{8}<2^{32}.
$$

Both component theorems include their frequency thresholds, so no joining
point is lost.

## Dependency boundary

The optimized high theorem is a new derivation from the unconditional Round
3 shifted-tail decomposition.  It does not import the old
$K\ge64\varepsilon^{-2}$ conclusion, the old shelf bounds
$p<8/\sqrt\varepsilon$ or $p<10/\sqrt\varepsilon$, or the old plateau
localization.  Its scaled-loss proof is frozen separately in
SHELL-thin-local-plateau-optimized.md.

The aggregate-action theorem and optimized local-plateau theorem meet only
through their conclusions.  Neither is used to prove the other.

## Endpoint and wall audit

- $\varepsilon=1/15625$: both frequency ranges include the common endpoint.
- $K=0$: the strict count and Weyl term are both zero.
- $K=1/(8\varepsilon^{5/2})$: included by the aggregate theorem.
- $K=125/(8\varepsilon^2)$: included by the optimized high theorem.
- A radial spectral wall: the exact count remains strict.
- An ordinary-floor or gain wall: handled inside the optimized tail proof.
- The no-drop, immediate-drop, and degenerate-head branches: handled
  separately in the optimized packet.

## Consequence for the remaining compact interval

The thin endpoint removes every point with
$0<\varepsilon\le1/15625$ from the certificate target.  On

$$
\frac1{15625}\le\varepsilon\le\frac1{100},
$$

the only possible thin residual lies below

$$
\frac{125}{8\varepsilon^2}
\le\frac{125^5}{8}
<2^{32}.
$$

The central compact zone still has the larger ceiling below $2^{35}$.

## Promotion record

The optimized high theorem passed an isolated clean-room proof, a complete
dependency/constants audit, and a targeted adversarial reconstruction in
Round 9.  The exact overlap and all endpoint equalities passed the same
audit.  This packet proves only the complete thin endpoint; the remaining
compact residual and final shell theorem stay open.
