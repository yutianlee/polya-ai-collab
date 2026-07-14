PASS. First issue: none.

# Round 20 State-Patch Final Audit

Date: 2026-07-15

Role: independent final State Patch auditor. I did not author
`rounds/polya-main/round_020/judge/judge-020.md`, and I did not mutate or
apply `state/proof_obligations.yml`.

## Verdict

The authenticated Round 20 judge and embedded State Patch pass the final
audit. The patch parses, validates, and applies cleanly in memory; its exact
operation sets, evidence chronology, source boundary, dependency topology,
residual subtraction, face ownership, and status calibration are consistent.
It is safe to apply exactly once with Round 20 metadata, subject to the final
hash recheck stated below.

Required final hashes:

| artifact | required SHA-256 | observed SHA-256 | result |
|---|---|---|---|
| baseline `state/proof_obligations.yml` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` | PASS |
| `rounds/polya-main/round_020/judge/judge-020.md` | `3acd0b9aec2aaa52f791bd8656cf6b53327c11eed5f3c4c51fe8352bee9782fa` | `3acd0b9aec2aaa52f791bd8656cf6b53327c11eed5f3c4c51fe8352bee9782fa` | PASS |

## Evidence authentication and A4 chronology

All 26 fixed-evidence rows in the judge match their current files byte for
byte. The two created obligations contain 28 `artifact_hashes` entries,
collapsing to exactly those same 26 distinct hashes; every entry resolves to
the intended fixed artifact. The patch has 59 evidence, source-card, or
review-path occurrences collapsing to 25 distinct regular files. Every one
appears in the fixed-evidence table and is hash-correct; the remaining fixed
row is the baseline graph itself. The clean-room and adversarial-review
artifacts exist and are authenticated.

The two superseded A4 cycles are classified correctly as negative evidence,
not promotion support:

1. `combined-closure-constants-adversarial-audit.md`, SHA-256
   `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd`,
   returned **FAIL** because the original verifier paid only 73 in the live
   cap-74 cell and contained disconnected or tautological labels.
2. `combined-closure-constants-replacement-audit.md`, SHA-256
   `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31`,
   returned **FAIL** because the first replacement had an actual `0x08` byte,
   mutation-insensitive localization checks, an insufficient wrong-wall
   test, and authenticated-looking skip-hash output.

The original `combined-closure-constants.md` is not used as evidence in the
new lemma. Only the final repaired verifier at `086beb09...`, tests at
`4936f4ef...`, replacement report at `df56599f...`, and independent final
audit at `6322802e...` are positive A4 evidence. Their advertised ledger is
reproduced below: 587 checks, comprising 488 substantive checks, 65
bookkeeping identities, and 34 authentication gates, with 17 focused tests.

## Source-boundary audit

I checked the primary SIAM publisher page for Lorch's article. Its abstract
identifies (j_{\nu,1}) as the first positive zero, states
(-1<\nu<\infty), and prints the strict inequality

\[
j_{\nu,1}^{,2}>
\frac{24(\nu+1)^2}
{1-2\nu+\sqrt{(2\nu+3)(2\nu+11)}}-2(\nu^2-1).
\]

At (\nu=21/2), exact rationalization gives

\[
j_{21/2,1}^{,2}>138\sqrt3-46.
\]

The desired comparison is equivalent, on positive sides, to

\[
3450\sqrt3>5911,
\qquad
3450^2\cdot3-5911^2=767579>0.
\]

Thus the only indispensable new external numerical payload is exactly

\[
\boxed{j_{21/2,1}>69/5}.
\]

The same Lorch formula also yields the displayed order-(17/2) and
order-(19/2) bounds, but neither is indispensable. From the internally
proved (j_{15/2,1}>23/2), same-index angular min--max gives

\[
j_{17/2,1}^2>\frac{593}{4}>\left(\frac{71}{6}\right)^2,
\qquad
j_{19/2,1}^2>\frac{665}{4}>\left(\frac{64}{5}\right)^2.
\]

The NIST DLMF references supply only the spherical/ordinary identity,
explicit half-integer formulas, and recurrences. Every (n\ge2) zero,
the strengthened first-zero bounds at orders (13/2) and (15/2), root
enumeration and simplicity, fixed-channel shell-to-ball comparison, angular
propagation, multiplicity count, cap, Weyl payment, optical estimate, and
residual subtraction remains internal. No source is credited with a shell
cross-product zero. The qualified `proved_external_dependency` status of
`SRC-ROUND20-BESSEL-ZEROS` is therefore calibrated correctly.

Primary pages checked:

- [SIAM publisher abstract](https://epubs.siam.org/doi/10.1137/0524050)
- [NIST DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3)
- [NIST DLMF 10.51.1--10.51.2](https://dlmf.nist.gov/10.51.E1)

## In-memory repository-tool audit

I used the repository's `extract_state_patch`, `parse_structured_text`,
`validate_patch_against_graph`, `apply_state_patch`, and `validate_graph`
functions entirely in memory. Both public validators also passed. The live
graph retained its required baseline hash throughout.

The exact simulated operation result is:

- created: `SRC-ROUND20-BESSEL-ZEROS`, `SHELL-combined-closure`;
- updated: `CONV-strict-counting`,
  `SHELL-sturm-liouville-completeness`, `SHELL-phase-enclosures`,
  `SHELL-weighted-lattice-fractional`, `SHELL-low-interface-small-hole`,
  `SHELL-rho-one-endpoint`, `SHELL-two-sided-staircase`, `SRC-annuli`,
  `SRC-FLPS-balls`, `SRC-LORCH`,
  `SHELL-rho-compact-analytic-envelope`, `SHELL-rho-compact`,
  `SHELL-rho-uniformity`, `TARGET-shell-d3`, `POLYA-program-target`,
  `COMP-certified-bessel`;
- rejected: none;
- no change: `SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`,
  `SHELL-fixed-rho-high-energy`, `SHELL-central-thin-seam-compression`,
  `SHELL-two-sided-staircase`, `SRC-LORCH`, `SRC-FLPS-balls`, `SRC-annuli`,
  `SHELL-rho-compact-analytic-envelope`,
  `COMP-certified-bessel-pilot-round8`,
  `COMP-certified-bessel-pilot-round17`, `COMP-certified-bessel`,
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
  `POLYA-program-target`.

Eleven IDs occur in both `update` and `no_change`. For each, `no_change`
records an unchanged mathematical status or inherited result, while the
update adds reverse-edge metadata, evidence, residual bookkeeping,
falsification cases, or a next action. The five no-change-only obligations
remain byte-identical in the simulated graph. No existing status changes.

The post-patch graph has exactly 57 unique obligation IDs. It has no dangling
`dependencies`, `implies`, or `blockers`, no duplicate ID, and no duplicate
relationship, permitted-dependency, evidence, or other validated list entry.
The 12 canonical relationships introduced by this patch occur exactly once
in both dependency and implication metadata:

~~~text
CONV-strict-counting ------------------------+
SHELL-sturm-liouville-completeness ----------+
SHELL-phase-enclosures ----------------------+
SHELL-weighted-lattice-fractional -----------+
SHELL-low-interface-small-hole --------------+
SHELL-rho-one-endpoint ----------------------+--> SHELL-combined-closure
SHELL-two-sided-staircase -------------------+              |
SRC-annuli ----------------------------------+              v
SRC-FLPS-balls ------------------------------+  SHELL-rho-compact-analytic-envelope
SRC-LORCH -----------------------------------+
SRC-ROUND20-BESSEL-ZEROS --------------------+
~~~

The dependency list and permitted-dependency list of
`SHELL-combined-closure` are identical. The envelope receives the new lemma
once in both lists. The new source obligation has no dependencies. Thus the
patch introduces no impermissible dependency. The complete canonical
dependency graph, implication graph, blocker graph, and their unions are
acyclic.

With `--round-index 20`, the validator generates an ISO timestamp and sets
`last_updated_round: 20` on the two created and sixteen updated obligations.
Under the repository's Windows `validate_round` behavior, the judge reference
`rounds\polya-main\round_020\judge\judge-020.md` is appended exactly once to
the `inconclusive` evidence of each created obligation and nowhere else.
No timestamp or last-updated field is hard-coded in the patch. Revalidating
the same patch against the simulated post-patch graph fails with exactly the
two expected duplicate-create errors, one for each created ID; a second
application cannot silently succeed.

## Exact D19-to-D20 subtraction

The accepted predecessor residual is

\[
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
\]

The lower theorem removes the first two components, including the complete
(\rho=\rho_0) fiber. On the high component the staircase removes exactly
(k_6<K\le k_{11}), and the optical theorem removes all remaining
frequencies for (39/50\le\rho<7/8), including the (39/50) face.

The containment needed for this subtraction is strict. For
(\rho\ge\rho_c), one has (a_\rho\ge1) and
(0<\eta_\rho\le\omega_0<1/8), hence the positive-root formula gives
(K_0>64). On (\rho<7/8), (z_\rho<8\pi) and therefore
(k_{11}<28<64). The seam floor, whenever eligible, is at least 1944,
and the (H_0) branch is ineligible because (\rho_c>\omega_0).
Consequently (k_{11}<U) throughout the live high strip.

Moreover, on (\rho_c\le\rho<39/50), the (H_0) branch is ineligible and
(39/50<5/6) makes the seam branch ineligible. Thus (U=K_0) exactly, and
the set difference is

\[
\boxed{
\mathcal D_{20}=
\left\{\rho_c\le\rho<\frac{39}{50},\quad
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
\]

The principal post-subtraction faces are assigned consistently:

| face | owner after Round 20 |
|---|---|
| (\rho=\rho_0) | removed by the lower theorem; (L=d) there |
| (\rho=\sigma) | lower shifted-tail wedge |
| (\rho=\rho_c) | staircase through (k_{11}), residual strictly above it |
| (\rho=39/50) | optical theorem inclusively at all frequencies |
| (\rho=7/8) | inherited thin endpoint and optical theorem |
| (K=L(\rho)) | inherited predecessor; excluded from (\mathcal D_{19}) |
| (K=d) | Round 19 predecessor owner |
| (K=\sqrt{114}) | Round 20 finite lower ledger |
| (K=k_6(\rho)) | Round 19 predecessor owner |
| (K=k_7,\ldots,k_{11}) | Round 20 staircase; each upper face included |
| (K=K_0(\rho)=U(\rho)) | inherited upper owner; excluded from the residual |
| (a=c/\varepsilon) | both inclusive optical screens |
| (K=0) | optical equality face |

The final verifier also checks every internal lower threshold, moving/fixed
ordering trace, high rational-zero and algebraic split, optical integer wall,
(a=m\pi) wall, and the (\varepsilon=11/50) face. Its independent
63-cell subtraction truth table plus five explicit owner checks reproduces
the formula above. The inherited certified boxes (B_0,B_1) were already
inside the predecessor cover and are not subtracted again.

The residual is nonempty. Since
(\rho_c<1/2<39/50), (\pi<22/7), and only the (K_0) branch is eligible
at (\rho=1/2),

\[
k_{11}(1/2)^2=4\pi^2+132
<\frac{8404}{49}<196,
\]

so

\[
k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2).
\]

Hence ((1/2,30)\in\mathcal D_{20}). This witness prevents an accidental
theorem promotion.

## Status audit

The only newly promoted obligations are:

| ID | post-patch status | calibration |
|---|---|---|
| `SRC-ROUND20-BESSEL-ZEROS` | `proved_external_dependency` | qualified, narrow first-positive-zero source payload |
| `SHELL-combined-closure` | `proved_internal` | independently reconstructed and adversarially reviewed analytic lemma |

Every existing status is unchanged. In particular,
`SHELL-rho-compact-analytic-envelope` remains `proved_internal` while its
recorded cover advances from A19/D19 to A20/D20;
`SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, and
`POLYA-program-target` remain `open`; and `COMP-certified-bessel` remains
`diagnostic_only`. No Round 20 certified spectral computation or certified
subset is created. The exact constant ledger is analytic arithmetic support,
not an interval-certified eigenvalue computation.

## Reproduction results

Final-byte reruns produced:

- baseline graph validator: **PASS**;
- embedded patch validator: **PASS**;
- public Round 20 judge validator: **PASS**;
- residual-mask self-check: **PASS, 10 checks**;
- residual-focused tests: **46 passed**;
- exact combined-closure verifier: **PASS, 587 checks**
  (488 substantive, 65 bookkeeping, 34 authentication), first issue none;
- exact-verifier focused tests: **17 passed**;
- complete repository suite: **271 passed, 1 strict expected xfail,
  10 subtests passed**;
- in-memory source compilation: **PASS, 61 Python files**;
- strict UTF-8 and C0/DEL scan of the judge and all fixed evidence:
  **PASS, 27 distinct files**;
- `git diff --check`: **PASS**;
- post-patch in-memory graph validation: **PASS**.

## Application decision

**Explicit authorization: PASS.** After rechecking the two required final
hashes, apply this State Patch exactly once with the repository's canonical
Windows metadata behavior:

```text
python -m math_collab.validate_round rounds/polya-main/round_020/judge/judge-020.md --graph state/proof_obligations.yml --apply --round-index 20
```

Do not apply it if either required hash differs. This audit did not apply the
patch; at report sealing, `state/proof_obligations.yml` still had SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.
