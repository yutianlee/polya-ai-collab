# Round 21 adversarial audit: compact proxy rectangle

## Verdict

**PASS.**

**First issue:** none.

Assuming the advertised rectangle theorem false did not expose a missing
spectral channel, a strict-floor error, a reversed monotonicity, an
uncertified Arb decision, a partition defect, a digest defect, or a gap in
the prospective D20 sub-200 containment.  The frozen 256-bit computation was
reproduced exactly, all of its frozen leaves were replayed afresh at 384 bits,
and deliberate dependency, leaf, face, and count corruptions were rejected.

## 1. Authentication before inspection

The three supplied hashes were checked before their contents were read.

| artifact | observed SHA-256 | result |
|---|---|---|
| `computations/round21_certify_compact_proxy.py` | `2a43611635ffb122f2e2655fe5c0f59e0f9b0f5a0e45242c5802593acbd7e856` | exact match |
| `computations/tests/test_round21_certify_compact_proxy.py` | `29b7425c47576826e11e2843317bbf3cf96738ac05188956c1fd5b0fcfc56b36` | exact match |
| `rounds/polya-main/round_021/certification/compact-proxy-rectangle.md` | `c381c0fa5094b6702f6ee2df7721772f39b6d47aa6bee4c7860b29cd8b4b1293` | exact match |

The verifier then authenticated all three permitted packets at their embedded
digests:

| packet | observed SHA-256 |
|---|---|
| `SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |

A byte scan of the verifier, tests, and theorem report found zero C0 control
bytes other than permitted tab, LF, and CR bytes.

For the set-containment check only, I also authenticated the prospective
Round 20 frozen claim and its external freeze:

| artifact | observed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |

That candidate remains expressly **frozen but not promoted**.  It is not a
dependency of the rectangle theorem; it is used below only to check the
conditional statement that its prospective residual lies in the certified
rectangle.

## 2. Independent spectral reduction

Write

\[
 \nu_\ell=\ell+\frac12,\qquad \mu=\rho K,qquad
 A_{\rho,K}(\nu)=G_K(\nu)-G_{\rho K}(\nu).
\]

The authenticated completeness packet gives the strict phase count

\[
 N_D(A_{\rho,1},K^2)
 =\sum_{\nu_\ell<K}2\nu_\ell
   [\gamma_{\rho,K}(\nu_\ell)]_<.
\]

The sharp cutoff is legitimate: the weighted packet records that no radial
root contributes when \(K\leq\nu_\ell\), consistently with the annulus phase
bound \(\Theta<\pi\) in that range.  The code enumerates exactly

\[
 m_K=\max\left\{0,\left\lceil K-\frac12\right\rceil\right\}
\]

channels.  In particular, a channel with \(\nu_\ell=K\) is excluded.

For \(\nu<\mu\), the inner-region phase enclosure gives

\[
 \gamma_{\rho,K}(\nu)<A_{\rho,K}(\nu)+\frac14.
\]

The same statement holds at \(\nu=\mu\), where the inner \(G\)-term is
exactly zero.  For \(\mu<\nu\leq K\), the zero extension gives
\(G_{\rho K}(\nu)=0\), and the global one-sided enclosure gives the same
bound.  Therefore, throughout the active set,

\[
 [\gamma_{\rho,K}(\nu_\ell)]_<
 \leq
 \left[A_{\rho,K}(\nu_\ell)+\frac14\right]_<.
\]

This is set inclusion between positive integers strictly below the two
arguments; it never replaces a strict count by an ordinary floor.  It remains
valid when either argument is an integer.  Thus

\[
 N_D(A_{\rho,1},K^2)\leq P_{\rm coarse}(\rho,K).
\]

No unproved weighted-floor theorem from the third packet is used here.  Only
its authenticated spectral bridge and cutoff are used, and the bridge was
reconstructed above directly from the phase packet.

## 3. Independent corner monotonicity, including interfaces

For \(a>\nu\), differentiating the displayed permitted definition of \(G\)
gives

\[
 \partial_aG_a(\nu)
 =\frac1\pi\sqrt{1-\frac{\nu^2}{a^2}}\geq0.
\]

For \(a\leq\nu\), the zero extension is zero.  Its value and the right
derivative both tend to zero at \(a=\nu\), so the following monotonicities do
not skip either zero-extension interface.

At fixed \(K\), increasing \(\rho\) increases the subtracted inner term and
hence decreases \(A\).  At fixed \(\rho\), for \(\nu<K\),

\[
 \partial_K A_{\rho,K}(\nu)=
 \begin{cases}
 \dfrac{\sqrt{K^2-\nu^2}}{\pi K},&\rho K\leq\nu<K,\\[5pt]
 \dfrac{\sqrt{K^2-\nu^2}-
 \sqrt{\rho^2K^2-\nu^2}}{\pi K},&\nu<\rho K,
 \end{cases}
\]

which is positive.  At a newly active face \(K=\nu_\ell\), the formal new
summand is

\[
 2\nu_\ell[1/4]_< =0.
\]

Consequently the strict proxy itself decreases weakly with \(\rho\) and
increases weakly with \(K\), even across active-cutoff and inner-interface
faces.

Meanwhile

\[
 W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3
\]

decreases strictly with \(\rho\) and increases strictly with \(K\).  Hence on
every closed rational box

\[
 P_{\rm coarse}(\rho,K)
 \leq P_{\rm coarse}(\rho_-,K_+),\qquad
 W(\rho,K)\geq W(\rho_+,K_-).
\]

The two corners used by the verifier therefore have the correct directions.

## 4. Strict walls and Arb semantics

All geometry, channel cutoffs, \(\nu\mathrel{?}\rho K\) decisions, and
\(\nu\mathrel{?}K\) decisions are exact `Fraction` comparisons.  Arb is used
only after the branch has been fixed.

For an outward ball containing a proxy argument \(x>0\), the verifier derives
an integer \(M\) from the outward upper endpoint and then separately requires
the certain predicate

\[
 x\leq M.
\]

It follows exactly that

\[
 [x]_<\leq\max\{0,M-1\}.
\]

If \(x=M\) exactly, this returns \(M-1\).  If a ball straddles an integer,
the outward ceiling moves to the safe side and may overcount by one; it cannot
undercount.  The frozen build encountered zero wall straddles, but the
uncertain-wall branch was independently exercised and returned the safe
overestimate.

At the Weyl corner the program takes an outward lower enclosure and accepts a
leaf only when Arb says

\[
 W_{B,-}-\widehat P_B>0
\]

with certainty.  Direct checks confirmed that python-flint returns false for
`arb("0 +/- 1") > 0` and `arb("1 +/- 1") > 0`, and true only for a ball
strictly separated from zero.

An AST scan found exactly one conversion to binary floating point, at the
midpoint display used by `BoxEvaluation.subdivision_score`.  The sole proof
assignment is `passed = bool(comparison > 0)`.  A float can select a legal
split direction, but cannot accept a leaf.  Every resulting leaf is checked
by the certain Arb predicate.

## 5. Exact partition, faces, and digest

The slab sweep is sufficient, not merely an area heuristic:

1. every leaf is a nondegenerate subbox of the root;
2. on every elementary open \(\rho\)-slab, the active leaf intervals tile the
   full \(K\)-interval exactly, with any gap or overlap rejected;
3. on every rational vertical face, lower-closed/upper-open ownership (closing
   only the root upper face) again tiles the full \(K\)-interval exactly;
4. exact leaf areas sum to the exact root area.

Items 2 and 3 cover respectively all points off and on a \(\rho\)-face.  The
uniform half-open convention in \(K\) assigns horizontal faces uniquely,
including the root upper face.  Thus edges and vertices are covered as well
as interiors.

As an independent recursion invariant, every frozen leaf satisfied

\[
 |B|\,2^{\operatorname{depth}(B)}=|R|,
 \qquad
 \sum_B2^{-\operatorname{depth}(B)}=1.
\]

Removing one leaf, duplicating one leaf, or shrinking one leaf boundary was
separately rejected by exact partition validation.

I independently serialized the schema, precision, exact root, packet hashes,
and every sorted leaf endpoint, depth, and proxy integer without calling the
target serializer.  Its SHA-256 was exactly

`96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631`.

Changing one stored proxy integer changed the digest and was also rejected by
a fresh recomputation.  A one-byte mutation of a dependency packet failed the
hash gate.

## 6. Exact containment of the prospective D20 sub-200 set

The authenticated frozen Round 20 candidate defines

\[
 \mathcal D_{20}=
 \left\{\rho_c\leq\rho<\frac{39}{50},\quad
 k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\},
\]

where

\[
 \rho_c=\frac1{1+2\pi},\qquad
 z_\rho=\frac\pi{1-\rho},\qquad
 k_{11}(\rho)=\sqrt{z_\rho^2+132}.
\]

The two lower-face containments omitted from the short subset statement have
exact one-line proofs.  First, the standard strict bound \(\pi<22/7\) gives

\[
 1+2\pi<1+\frac{44}{7}=\frac{51}{7},
 \qquad
 \boxed{\frac7{51}<\rho_c}.
\]

Second, \(z_\rho\) increases with \(\rho\), and

\[
 z_{\rho_c}
 =\frac{\pi}{1-1/(1+2\pi)}
 =\pi+\frac12>\frac72
\]

by \(\pi>3\).  Therefore, for every \(\rho\geq\rho_c\),

\[
 k_{11}(\rho)^2
 =z_\rho^2+132
 >\frac{49}{4}+132
 =\frac{577}{4}>144,
 \qquad
 \boxed{k_{11}(\rho)>12}.
\]

Both rational comparisons were also certified directly by 384-bit Arb.
Thus, if \((\rho,K)\in\mathcal D_{20}\) and \(K<200\), then

\[
 \frac7{51}<\rho<\frac{39}{50},
 \qquad
 12<K<200,
\]

so it lies strictly inside the corresponding lower and upper faces of the
certified closed rectangle.  The rectangle also certifies the harmless
boundary faces \(\rho=7/51\), \(\rho=39/50\), \(K=12\), and \(K=200\).
No limiting argument or implicit reassignment of a strict face is used.

## 7. Reproduction and adversarial results

The frozen verifier was run with bytecode writes disabled.

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -B computations/round21_certify_compact_proxy.py --precision-bits 256
```

Result:

```text
ROUND21_COMPACT_PROXY PASS
precision_bits=256
leaf_boxes=10580
max_depth=15
generated_proxy_corners=16020
generated_floor_comparisons=2153076
generated_wall_straddles=0
min_gap_lower_display=0.092025556028085972
certificate_sha256=96e527b4eefaf032aeac89ddb960fc2fd4928e3b8204ccbbddbc8fddaa3be631
```

An independent higher-precision rebuild was then run:

```powershell
python -B computations/round21_certify_compact_proxy.py --precision-bits 384
```

Result:

```text
ROUND21_COMPACT_PROXY PASS
precision_bits=384
leaf_boxes=10580
max_depth=15
generated_proxy_corners=16020
generated_floor_comparisons=2153076
generated_wall_straddles=0
min_gap_lower_display=0.092025556028085972
certificate_sha256=c6deaf2c1a7e9df78760d61414c59ee48a16b0ed621266b2de40a29aea1946f6
```

The digest changes because precision is deliberately part of the canonical
bytes.  More importantly, a fresh 384-bit `Certifier` replayed every leaf of
the frozen 256-bit certificate, bypassing all construction caches.  All
10,580 leaves passed after 1,423,539 freshly recomputed strict-floor
comparisons.

Focused tests:

```powershell
python -B -m pytest -q computations/tests/test_round21_certify_compact_proxy.py
```

Result: `5 passed in 34.89s`.

The additional inline adversarial harness produced:

```text
baseline=PASS leaves=10580 depth=15
independent_digest=PASS
dyadic_tree_area_and_kraft=PASS
fresh_384_leaf_replay=PASS
missing_leaf=REJECTED
duplicate_leaf=REJECTED
shrunk_bound_gap=REJECTED
stored_proxy_count=REJECTED
digest_count_tamper=REJECTED
packet_byte_tamper=REJECTED
arb_semantics_walls_cutoffs_interfaces=PASS
float_call_sites=PASS (subdivision/display only)
proof_pass_assignment=PASS (certain Arb comparison only)
```

The cutoff check compared `active_channel_count` with a direct half-integer
enumeration at 7,200 exact rational values.  Interface checks included
\(\nu=\rho K\), \(\nu=K\), and points on both sides of the zero extension.
Exact and uncertain integer walls from 1 through 9 were also exercised.

## 8. Final assessment

The computation proves the closed-rectangle inequality

\[
 \frac7{51}\leq\rho\leq\frac{39}{50},\qquad
 12\leq K\leq200
 \quad\Longrightarrow\quad
 N_D(A_{\rho,1},K^2)
 <\frac{2}{9\pi}(1-\rho^3)K^3.
\]

The strict conclusion follows from

\[
 N_D\leq P_{\rm coarse}\leq\widehat P_B<W_{B,-}\leq W.
\]

The displayed decimal minimum is diagnostic only; the proof is the certain
Arb positivity of every leaf.  No first unsupported implication was found.
