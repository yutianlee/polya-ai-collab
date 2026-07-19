# Adversarial audit of the simplified proof graph

**Date:** 16 July 2026  
**Audited main source:** `manuscript/spherical-shell-polya-proof.tex`  
**Main-source SHA-256:** `304A3F8E8393F7EF8B7179E462300964B2FA0BFA7C701394EDA12C0981345221`

## Verdict

**PASS, for the six deletion-sensitive issues specified below.** I found no
remaining unsupported implication caused by removal of the thin-shell/seam,
first-band/`k_5`, or aggregate-tail branches.

During the audit, the shortened optical proof initially used `D(a)` and
`S_0(a)` after their definitions had been deleted with the old thin-shell
branch. That was a genuine self-containment defect. The live source now
repairs it: `b_n`, `I_0`, `S_0`, and `D` are defined at lines 2748--2761;
the exact deficit is stated at 2763--2772; the ceiling and quarter-circle
calculation is at 2774--2793; and the complete scaling implication to the
Weyl term is printed at 2794--2818. Re-auditing those lines found the repaired
chain correct. Thus the first unsupported implication in the **current**
source is: **none**.

This is a scoped audit of whether the simplification opened a proof gap. It
is not a new audit of every rational entry in the 611-row finite ledger.

## 1. All-frequency extension of Parts VII--IX

**PASS.** No estimate in these modules has an upper-frequency hypothesis.

- Part VII defines the strict proxy and continuous payment for arbitrary
  `0<rho<1`, `K>0` at lines 57--77 of
  `analytic/compact-structural.tex`. The exact layer cake is proved at
  167--200, the retained-remainder identity at 276--365, and the sufficient
  implication `E_ang<H => P<W` at 434--467. These are global identities.
- Part VIII proves the one-layer estimate at lines 293--335 of
  `analytic/compact-angular-block.tex`. Summing its disjoint left blocks gives
  the global bound
  `E_ang < (1-rho^2)K^2/6-N/2` at 337--385. On the desired domain,
  `T>1`, hence `N>=1`, at 397--412. No step depends on `K<=200`.
- Part IX proves the exact derivative formula and the uniform loss bound at
  lines 130--201 of `analytic/compact-scalar-positive.tex`. The scalar gap is
  strictly increasing for the entire ray `K>=k_11(rho)` at 203--297 because
  `k_11>241/20>12`. Its base-curve positivity is proved at 449--645 and the
  upward conclusion at 647--654.

Consequently the domain stated in the live main theorem at lines 2893--2901,
namely

```text
rho_c <= rho <= 39/50,    K >= k_11(rho),
```

is exactly the intersection of the three proved domains. The main assembly at
2904--2948 does not extrapolate beyond a module's scope.

As transcription checks only, I independently recomputed the four Bernstein
coefficients in the `K`-derivative argument, the degree-nine base polynomial,
all ten of its displayed Bernstein coefficients, and the rational secant sum
`Q`. They agree exactly with the printed fractions. These recomputations are
not premises of the proof.

## 2. Direct containment of `D_20`

**PASS.** The live residual is

```text
D_20 = {rho_c <= rho < 39/50, k_11(rho) < K < U(rho)=K_0(rho)}
```

at main lines 2867--2874. Weakening its two relevant strict inequalities
immediately places it in

```text
{rho_c <= rho <= 39/50, K >= k_11(rho)},
```

which is the all-frequency theorem domain. This inclusion is written
explicitly at 2958--2968. No frequency split, `K=200` face, or aggregate
propagation is needed.

The upper wall does not interfere with the containment. Lines 2876--2882
prove `k_11<U`, identify `U=K_0` on the surviving ratio interval, and assign
the three excluded faces `K=k_11`, `rho=39/50`, and `K=U` to their inclusive
owners.

## 3. Optical owner replacing the thin-shell and seam branches

**PASS.** The all-frequency optical theorem already has the stronger domain

```text
39/50 <= rho < 1,    K >= 0
```

at main lines 2727--2731. Its statement was not enlarged by the
simplification.

Its low screen is now self-contained at 2739--2819. The high screen at
2821--2865 invokes only the surviving action-geometry, strict layer-cake, and
radial-deficit lemmas (main lines 1339--1434, 1436--1567, and 1569--1671).
The detailed monotonicity and endpoint arithmetic is also printed in
`analytic/ledger-packet-E.tex`, lines 200--345. Neither screen invokes the
deleted thin-shell endpoint theorem or the deleted seam owner.

Thus using the optical theorem for all `rho>=39/50` is a direct use of an
already proved theorem, not an extension by analogy. In particular it covers
the former thin-shell range `rho>=7/8` and makes the seam range irrelevant.

## 4. Changes to the `D_16` and `D_19` ratio ranges

**PASS.** The new main proof works only in the open compact-middle strip
`rho_*<rho<39/50`. The inclusive primitive owners and their complement give
the displayed `D_16` exactly at main lines 1981--2010. Because
`39/50<5/6`, the deleted seam upper wall was never eligible in this smaller
strip. The only eligible upper owners are therefore `H_0` (when
`rho<omega_0`) and `K_0`, exactly as used in the new definition of `U`.

Subtracting the closed `k_6` and lower-`d` regions gives the three components
of `D_19` at lines 2328--2343. The equality slice `rho=rho_0` is assigned
explicitly: there `L=d`, the would-be second lower fiber is empty, and the
first component owns the slice. At `rho=rho_c`, the high component owns the
face. Extending neither a lemma nor an arithmetic table is required; all new
ratio intervals are restrictions of their former intervals.

## 5. `k_6` replacing the first-band and `k_5` lemmas

**PASS.** The retained `k_6` lemma itself states and proves the whole closed
range `z_rho<=K<=k_6(rho)` at main lines 2225--2286; it is not merely a
continuation above `k_5`.

The deletion-sensitive initial segment is now explicit:

- the complete mode inventory and every entry wall are at 2231--2248;
- the initial cap immediately above `z_rho` is paid at 2250--2255;
- moving and fixed event payments, including coincident entries, are at
  2256--2285;
- strict equality at an entry wall remains assigned to the lower cap.

The `k_11` lemma then cites this full closed result and treats only
`k_6<K<=k_11` at 2592--2601. Hence there is neither an initial gap at
`K=z_rho` nor a handoff gap at `K=k_6`.

## 6. Final ratio and equality-face partition

**PASS.** The final ratio partition is the disjoint exhaustive identity

```text
(0,1) = (0,rho_*] dot-union (rho_*,39/50) dot-union [39/50,1)
```

at main lines 3045--3050. The corresponding owners are applied at
3053--3064:

- `rho=rho_*` belongs to the small-hole theorem;
- `rho=39/50` belongs to the optical theorem;
- `K=0` is handled separately before the positive-frequency cases.

Inside the compact-middle strip, `D_16` has strict `L<K<U`; all `L` and `U`
faces therefore remain with the inclusive primitive owners. The `k_6` and
`k_11` lemmas are closed at their common faces, while `D_19` and `D_20` use
strict lower-frequency inequalities. Lines 2969--2972 explicitly retain the
`rho=39/50`, `K=k_11`, `K=U`, and `rho=rho_c` assignments. No deleted
`K=200` equality face remains.

## Non-blocking consistency note

`analytic/ledger-packet-F.tex` still presents the older, wider intermediate
set `D_19` with `rho<7/8` and then subtracts the optical owner to obtain the
same `D_20`. The simplified main proof instead restricts `D_19` to
`rho<39/50` from the outset. Both owner graphs give exactly the same final
residual, so this is not a mathematical or coverage defect. It is only an
intermediate-notation mismatch that should be mentioned if the supplement is
later streamlined.

## Conclusion

The simplified dependency graph is valid:

```text
primitive owners
  -> D_16
  -> k_6/lower closures
  -> D_19
  -> k_11
  -> D_20
  -> global retained-remainder theorem
  -> empty residual.
```

The optical theorem independently owns the complementary ratio interval
`[39/50,1)`. The deleted aggregate, seam, thin-shell endpoint, first-band, and
`k_5` branches are therefore redundant in the live proof graph.
