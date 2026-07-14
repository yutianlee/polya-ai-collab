# Round 21 Compact-Proxy Certificate Contract

Status: **FROZEN PROOF-FREE CONTRACT / NO REVIEW VERDICT**.

Baseline commit:
`0d4ee5d77e37e9e75490ac6e0e02ab338398fa00`.

This contract fixes a theorem domain, mathematical postcondition, finite
certificate schema, exact proof predicates, authentication targets, and
falsification mutations. It contains no incumbent proof, executable code,
test implementation, certificate report prose, audit conclusion, or sampled
spectral computation.

The paths and hashes in Section 5 are sealed authentication targets for A4.
They do not authorize A3 to open an executable artifact or report.

## 1. Contracted theorem

Put

$$
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The contracted compact theorem is exactly

$$
\boxed{
\frac7{51}\leq\rho\leq\frac{39}{50},
\qquad 12\leq K\leq200}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<W(\rho,K).}
\tag{C1}
$$

All four outer faces and all four vertices of the displayed rectangle are
included. The spectral count is the strict count below $K^2$.

## 2. Mathematical certificate interface

For $a>0$ and $\nu\geq0$, define

$$
G_a(\nu)=
\begin{cases}
\displaystyle\frac1\pi\left(
\sqrt{a^2-\nu^2}-\nu\arccos\frac\nu a\right),&0\leq\nu<a,\\[4pt]
0,&\nu\geq a,
\end{cases}
\tag{C2}
$$

$$
\nu_\ell=\ell+\frac12,
\qquad
A_{\rho,K}(\nu)=G_K(\nu)-G_{\rho K}(\nu),
\tag{C3}
$$

and let

$$
[x]_<:=\#\{n\in\mathbb N:n<x\}.
\tag{C4}
$$

The analytic reconstruction must derive, rather than assume, the bridge

$$
N_D(A_{\rho,1},K^2)
=\sum_{\nu_\ell<K}2\nu_\ell
[\gamma_{\rho,K}(\nu_\ell)]_<,
\qquad
\gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+\frac14,
\tag{C5}
$$

and hence the sufficient proxy

$$
P_{\rm coarse}(\rho,K)
=\sum_{\nu_\ell<K}2\nu_\ell
\left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<.
\tag{C6}
$$

The exact proof predicates to be reconstructed and then checked are:

1. the zero extension in (C2), including $\nu=\rho K$ and $\nu=K$;
2. the strict active set $\nu_\ell<K$, with exact cardinality
   $\max\{0,\lceil K-1/2\rceil\}$;
3. $P_{\rm coarse}$ is weakly decreasing in $\rho$ and weakly increasing in
   $K$, including across both interfaces in item 1;
4. $W$ is decreasing in $\rho$ and increasing in $K$ on the contracted
   rectangle;
5. for a rational box
   $B=[\rho_-,\rho_+]\times[K_-,K_+]$,

   $$
   P_{\rm coarse}(\rho,K)
   \leq P_{\rm coarse}(\rho_-,K_+),
   \qquad
   W(\rho,K)\geq W(\rho_+,K_-);
   \tag{C7}
   $$

6. for every active channel at $(\rho_-,K_+)$, an outward Arb enclosure
   $X_\ell$ of $A_{\rho_-,K_+}(\nu_\ell)+1/4$ and an integer $M_\ell$
   satisfy the certain comparison $X_\ell\leq M_\ell$;
7. the resulting strict-wall bound is

   $$
   [A_{\rho_-,K_+}(\nu_\ell)+1/4]_<\leq M_\ell-1,
   \tag{C8}
   $$

   also when the exact argument equals the integer $M_\ell$;
8. with

   $$
   \widehat P_B
   =\sum_{\nu_\ell<K_+}2\nu_\ell(M_\ell-1),
   \tag{C9}
   $$

   and an outward lower enclosure $W_{B,-}$ of
   $W(\rho_+,K_-)$, the leaf is accepted only by the certain predicate

   $$
   W_{B,-}-\widehat P_B>0.
   \tag{C10}
   $$

No ordinary floor at an integer wall, binary float, decimal display,
midpoint sign, or sampled value is a proof predicate.

## 3. Frozen finite-certificate schema

| field | frozen value |
|---|---|
| schema | `round21-compact-proxy-v2-half-open-faces` |
| exact root | `[7/51,39/50] x [12,200]` |
| midpoint precision | `256` bits |
| minimum permitted precision | `192` bits |
| exact rational leaf boxes | `10580` |
| maximum actual depth | `15` |
| generation depth limit | `30` |
| generation box limit | `100000` |
| distinct proxy corners generated | `16020` |
| Arb/integer floor comparisons generated | `2153076` |
| generated integer-wall straddles | `0` |
| canonical certificate SHA-256 | `96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631` |

The canonical digest authenticates the ASCII schema, precision, exact root,
three dependency hashes, and every sorted leaf's four rational endpoints,
depth, and integer proxy upper bound.

Each leaf is a nondegenerate rational subrectangle of the root. Exact
rational slab tiling, exact total area, and every rational vertical face
must reproduce full coverage. Point ownership is lower-closed and
upper-open in each coordinate, except that the two root upper faces are
closed. The analytic bound is required on each closed leaf even though the
partition assigns a shared face to only one leaf.

## 4. Accepted foundational dependencies

| artifact | SHA-256 | contracted scope |
|---|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum, multiplicity, strict count |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | phase enclosure in its proved scope |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | strict weighted count and normalization |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | definition (C2) only for this contract |

The executable dependency gate contains the first three rows. The source
identity in the fourth row must be independently scoped by A3; it is not an
additional executable packet gate.

## 5. Sealed A4 authentication targets

The following rows expose byte identities only. A3 may authenticate the
strings recorded here but must not read the named files.

| role | artifact | bytes | SHA-256 |
|---|---|---:|---|
| verifier | `computations/round21_certify_compact_proxy.py` | `21493` | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` |
| tests | `computations/tests/test_round21_certify_compact_proxy.py` | `4602` | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` |
| report | `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md` | `8198` | `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` |

An existing audit file is deliberately not named here. Review conclusions
are outside this proof-free contract.

## 6. Mandatory A4 falsification mutations

A4 must reject or detect each of the following independent mutations:

1. any accepted packet hash, verifier byte, test byte, or report byte;
2. precision below 192 bits or a changed frozen precision;
3. any root endpoint, leaf endpoint, leaf depth, stored proxy upper bound,
   leaf count, schema row, or canonical digest;
4. a gap, positive-area overlap, wrong exact area, missing outer face, or
   double-owned shared face;
5. replacement of $\nu<K$ by $\nu\leq K$, especially at half-integer $K$;
6. either wrong branch at $\nu=\rho K$ or $\nu=K$;
7. replacement of (C8) by an ordinary floor rule at an exact integer wall;
8. an Arb ball straddling an integer without a certified safe upper integer;
9. reversal of either monotone corner in (C7);
10. a nonpositive or uncertain instance of (C10);
11. use of a binary float, decimal display, or midpoint comparison in any
    hash gate, branch, count, coverage, or sign decision.

## 7. Scope and nonclaims

This contract does not assert that its certificate bytes are valid and does
not prove (C1). A3 reconstructs the analytic implication; A4 independently
authenticates and replays the finite certificate and exact faces. Neither
role may infer a Round 21 subtraction, a successor residual, or a project
target from this contract alone.
