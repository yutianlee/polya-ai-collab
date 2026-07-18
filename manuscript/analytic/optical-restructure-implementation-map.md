# Optical restructuring: implementation map and live-source audit

## Scope and verdict

This report audits the live main source
`manuscript/spherical-shell-polya-proof.tex`, 3,255 lines, SHA-256
`EAA6815C397BC69B2D45886E606684BF092CA20E5961FC6E1096223BFADE152D`.
It also records the pre-patch line ranges in the frozen 4,332-line source,
SHA-256
`84D079A9FD3A6001C7F00A528F7EAF40799D6850E87537BDC3819A98A9F6D982`.

The structural patch is mathematically coherent. The specialized thin-shell
low/high proofs, the thin-shell endpoint theorem, the seam owner, the
`rho_HK` locator, the uniform `295^2` ceiling, and the separate first-band and
`k_5` stages have all left the live dependency graph. The new ratio partition
is exact, the `k_6` proof now contains the base payment that the deleted first-
band proof formerly supplied, and the `k_11` proof now explicitly starts from
`k_6`. A static scan found 153 distinct labels, no duplicate labels, and no
undefined `ref` or `eqref` targets.

No further mathematical estimate is needed for this restructuring. The
remaining work is editorial reordering and removal of a few legacy words or
label prefixes.

## 1. Section 3: what must remain in the proof graph

The live Section 3 is correctly reduced to generic tools. None of the
following statements assumes `rho >= 7/8` or `epsilon <= 1/8`.

| Live lines | Block | Status and downstream use |
|---:|---|---|
| 1183--1230 | Product/action section introduction, normalized variables, strict phase input | Retain, but reword line 1186: the section is no longer a thin-shell proof. |
| 1232--1315 | Strict product majorant | Retain. It is the natural earlier source for primitive owner 2 and the optical product screen. |
| 1318--1337 | Complementary action definition | Retain. It defines the action used by all three later generic lemmas. |
| 1339--1434 | Action geometry and inverse-curvature switch | Retain. Used by the radial deficit and the optical high screen. |
| 1436--1567 | Strict phase-to-action layer cake and continuum normalization | Retain. It transfers the strict spectral count and identifies the action integral with the Weyl payment. |
| 1569--1671 | Shifted sawtooth/Stieltjes radial deficit | Retain. It is the decisive radial reserve in the optical high screen. |

The old exact product-deficit identity at frozen lines 1317--1360 was also
generic, but it need not be restored: the only surviving use is reproduced
directly in the optical proof at live lines 2754--2763. Its old universal
`D(a) > 2a^2/5` add-on at frozen lines 1340--1386 was used only by the retired
thin-shell low screen.

The following frozen blocks were specialized and were safely deleted:

| Frozen lines | Deleted block | Why redundant |
|---:|---|---|
| 1388--1484 | Inclusive thin-shell low-action proposition | The all-frequency optical product screen has the larger domain `rho >= 39/50`. |
| 1841--1967 | Inclusive thin-shell high-action proposition | The all-frequency optical action screen uses the generic geometry/layer-cake/Stieltjes lemmas directly. |
| 1969--2018 | Thin-shell endpoint theorem and dependency remark | Its full domain `rho >= 7/8` lies inside the optical theorem's domain. |

Thus the generic tools must remain somewhere in the manuscript or supplement;
the specialized assemblies do not.

## 2. Optical theorem placement

The all-frequency optical theorem is presently at live lines 2724--2824.
It proves

```
39/50 <= rho < 1,  K >= 0.
```

Its actual inputs are only the generic product comparison and the Section 3
action tools. It does not use the zero registry or finite staircase that now
precedes it. The clean final organization is therefore to place this theorem
immediately after line 1671 and before the compact-middle section.

That move should be done in this order:

1. Move the definition of `W(rho,K)` from live lines 1677--1682 to the global
   unit-shell conventions (leave `z_rho` and `k_m` in the compact section).
2. At live line 2739, cite Lemma `thin:lem-product-majorant` rather than the
   later fixed-channel formula `cm:eq-product-bound`.
3. The same cleanup is available at live lines 1756--1759 for primitive owner
   2: cite the earlier product-majorant lemma and remove the forward
   reference.
4. Move the complete optical theorem block, preserving all strict radial,
   angular, and common-screen faces.
5. Leave only the exact `D_20` subtraction, currently lines 2826--2841, after
   the `k_11` staircase.

This reordering is editorial after the two citation changes. Renaming every
legacy `thin:*` label to `tool:*` or `opt:*` is optional and has no
mathematical value; retaining the stable labels is lower risk.

## 3. Seam owner, `U(rho)`, `295^2`, and `rho_HK`

The live primitive-owner proposition, lines 1739--1979, now contains only the
five owners actually used in the middle strip. This is correct.

The exact residual setup at live lines 1981--2020 is also correct:

```
U(rho) = min({K_0(rho)} union {H_0(rho) : rho < omega_0}),
rho_* < rho < 39/50.
```

This definition automatically owns the equality face where `H_0 = K_0` and
does not require locating the switch. The following frozen material is now
mathematically unused and was safely removed:

| Frozen lines | Retired material |
|---:|---|
| 2094--2099 | Primitive seam owner, separate thin owner, and uniform `295^2` conclusion |
| 2329--2469 | Complete seam-tail proof on `rho >= 5/6` |
| 2471--2493 | Re-import of the thin endpoint and proof of the global ceiling |
| 2530--2626 | `H_0/K_0` switch equation, rational `rho_HK` locator, and Machin locator arithmetic |
| 2628--2695 | `K_0` monotonicity used only for `295^2`, the three-piece `U`, seam branch, and remaining global-ceiling arithmetic |

The deleted seam equation had one genuine downstream citation in the lower
wedge. That dependency has been repaired: live lines 2423--2425 now cite the
generic concave-head/convex-tail compensation
`eq:sc-tail-compensation` at lines 1046--1050. There is no dangling seam
lemma or equation.

On the final high residual, live lines 2825--2831 correctly establish
`U = K_0`: `omega_0 < 1/9 < 7/51 < rho_c`, so `H_0` is ineligible, and no
seam branch exists.

## 4. First bands and `k_5`: deletion audit

The deletion is valid, with the two repairs now visible in the live proof.

The two retired statements had the union of domains

```
z_rho <= K <= k_2(rho),
k_2(rho) < K <= k_5(rho).
```

The live `k_6` lemma at lines 2225--2286 covers

```
rho_c <= rho <= 39/50,
z_rho <= K <= k_6(rho),
```

and `k_6 > k_5` identically. Its proof independently lists every entry wall
through `k_5`, plus the two possible second-radial walls, at lines 2240--2247,
and gives their exact split payments at lines 2256--2282. It does not cite
either deleted lemma.

### Base-cap repair: PASS

The deleted first-band proof formerly supplied the payment immediately above
`K = z_rho`. Live lines 2250--2255 now prove

```
W(rho,z_rho)
 = (2 pi^2/9) (1+rho+rho^2)/(1-rho)^2
 > 2 pi^2/9 > 2 > 1.
```

The first strict spectral cap is 1, `W` increases with `K`, and at
`K = z_rho` the radial equality wall is excluded. This closes the only gap
that would otherwise have been created by deleting the first-band lemma.

### `k_11` base citation: PASS

The `k_11` statement at live lines 2592--2596 now has the same ratio domain as
`k_6`. Its proof begins at lines 2598--2601 by assigning the closed range
`z_rho <= K <= k_6(rho)` to the `k_6` lemma and treating only
`k_6(rho) < K <= k_11(rho)`. Hence the common face `K = k_6(rho)` has one
explicit owner and there is neither a gap nor a hidden appeal to the deleted
`k_5` stage.

The frozen blocks at lines 2891--3056, including `D_17`, `D_18`, and the
historical pilot rectangles, are therefore redundant.

## 5. Exact owner and ratio audit

The current owner sequence is:

1. `D_16`, live lines 2000--2010: complement of the primitive owners in the
   open middle strip.
2. `D_19`, live lines 2333--2343: direct subtraction of `k_6` and the lower
   `d` staircase; no intermediate `D_17` or `D_18` is needed.
3. `D_20`, live lines 2826--2841: lower closure plus `k_11`, with the optical
   owner taking the upper-ratio face.
4. All-frequency analytic middle theorem, live lines 2852--2908: owns every
   point of `D_20` without a frequency split.
5. Exact closure and compact-middle proposition, live lines 2911--2962.

The final ratio ordering and partition at live lines 3001--3012 are exact:

```
(0,1) = (0,rho_*] dot-union (rho_*,39/50) dot-union [39/50,1).
```

The applications at lines 3021--3025 match these owners exactly:

- `rho = rho_*` is small-hole owned;
- the compact theorem has both ratio endpoints open;
- `rho = 39/50` is optical owned;
- `K = 0` is handled separately at lines 3015--3019.

No ratio face is omitted or assigned twice in this final partition.

## 6. Stale-label and retired-dependency audit

Static label audit: **PASS**.

- 153 distinct labels;
- 0 duplicate definitions;
- 0 undefined `ref`/`eqref` targets.

There are no occurrences of any retired dependency label or quantity:

```
lem:thin-shell
thin:prop-low-piece
thin:prop-high-piece
cm:lem-first-bands
cm:lem-k5
cm:eq-D17
cm:eq-D18
cm:eq-seam-tail
cm:eq-U-piecewise
rho_HK
295^2
C_21, T_21, D_21
the aggregate-Q implication or aggregate-tail lemma
```

There is also no occurrence of `K=200` or an equivalent frequency cutoff.
The remaining printed number `200` appears only inside rational constants or
denominators (for example `107/200` and `11/200`), not as a domain boundary.

No retired seam, thin-shell, or `K=200` argument survives as a logical
dependency. The remaining textual occurrences should be understood as
follows:

- the `thin:*` namespace labels the now-generic Section 3 toolkit;
- lines 2970--2982 explicitly classify retired seam and aggregate material in
  the supplement as optional cross-checks;
- “aggregate-owned” at line 2560 means the averaged low-tail argument in that
  lemma, not the retired high-frequency aggregate certificate.

Four wording-only cleanups remain desirable:

| Live line | Current wording | Recommended wording |
|---:|---|---|
| 79 | “seam assignments” | “boundary assignments” |
| 1186 | “prove ... uniformly as the shell becomes thin” | “develop product and complementary-action tools valid for every shell ratio” |
| 2560 | “aggregate-owned” | “averaged-tail-owned” |
| 3183--3186 | self-contained with respect to every “seam assignment” | replace by “strict boundary assignment” |

These are not proof defects.

## 7. Safe final patch order

1. Apply only the four wording cleanups above; run the static label scan.
2. Change the two product references (live lines 1756--1759 and 2739) to the
   earlier strict product-majorant lemma.
3. Move `W` to the global unit-shell notation and relocate the optical theorem
   from lines 2724--2824 to immediately after line 1671.
4. Leave `D_20` and its face audit after `k_11`; do not move the strict owner
   subtraction with the optical theorem.
5. Optionally prune retired seam/intermediate/aggregate packets from the
   supplement. If they remain, keep the current explicit “optional
   cross-check” classification. Do not report their rows as active proof
   obligations.
6. Compile both volumes, scan the log for undefined references/citations, and
   re-run the boundary audit for `rho_*`, `rho_c`, `39/50`, `K=z_rho`,
   `K=k_6`, `K=k_11`, and `K=U`.

The current live proof is already logically simplified. Steps 1--4 improve
the exposition and dependency order; they do not strengthen any inequality.
