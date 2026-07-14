PASS. First issue: none.

# Round 19 State-Patch Final Audit

Date: 2026-07-14

Role: independent final State Patch auditor. I did not author the judge and
did not mutate or apply `state/proof_obligations.yml`.

## Verdict

The corrected Round 19 judge and embedded State Patch pass the final audit.
The patch validates and applies cleanly in memory, has the exact intended
operation sets and status calibration, and preserves a nonempty three-piece
residual. It is safe to apply exactly once with `--round-index 19`, subject to
one last hash check immediately before application.

Required final hashes:

| artifact | required SHA-256 | observed SHA-256 | result |
|---|---|---|---|
| baseline `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` | PASS |
| corrected `rounds/polya-main/round_019/judge/judge-019.md` | `fdf79fa03f1cd82e5ecf4db89750aa0e5d876be6430a25e488bb1c34bdabc83b` | `fdf79fa03f1cd82e5ecf4db89750aa0e5d876be6430a25e488bb1c34bdabc83b` | PASS |

## Caught-and-fixed defect

The first audit of judge hash
`3e47c1f97acce9878b7a0de43ca1dbda668ca10a00014da336e525d11f85bfc6`
caught a false equality in its nonemptiness witness: it said
`U(1/2)=K_0(1/2)=64`. From the frozen definitions,
`U(1/2)=K_0(1/2)`, but, with `a_(1/2)=2 pi` and
`0<eta_(1/2)=omega_0<1/8`, the positive-root formula gives

$$
K_0(1/2)>\frac{a_{1/2}}{\eta_{1/2}^2}>384.
$$

The judge was corrected only to `U=K_0>64` and
`k_6<10<30<64<K_0=U`. A Git-object comparison confirms those are the
only textual changes, and parsing both versions confirms that the State
Patch object is unchanged. The corrected strict chain is valid and the
final judge hash above is the object audited here.

## Evidence hashes and source scope

All 21 fixed-evidence rows in the corrected judge match their files byte for
byte. All 23 `artifact_hashes` fields across the two proposed obligations
resolve to those authenticated bytes. The patch contains 56 evidence/source/
review references collapsing to 17 distinct paths; every path is a regular
file, appears in the fixed-evidence table, and is hash-correct.

I also scanned the candidate, freezes, incumbents, reviews, source card, and
judge for every 64-hex evidence token: 128 occurrences and 30 distinct
values. Every value is the current hash of a repository artifact except the
explicitly historical test hash `58c825...` in the A4 report. Appending the
documented single terminal blank line to the current test bytes reproduces
that historical hash exactly; the final test hash is the authenticated
`1eea93...`. This is not a provenance gap.

The source boundary is correctly narrow. The SIAM publisher abstract for
[Lorch's paper](https://epubs.siam.org/doi/10.1137/0524050) identifies the
first positive zero, states `-1<nu<infinity`, and prints the strict inequality
used. At `nu=11/2`, exact specialization reduces the desired comparison to

$$
507\sqrt{77}>4264,
\qquad 507^2\cdot77-4264^2=1611077>0.
$$

Thus the only new external numerical payload is
`j_(11/2,1)>17/2`. [DLMF 10.47.3](https://dlmf.nist.gov/10.47.E3)
supplies only the positive spherical/ordinary Bessel identity, and
[DLMF 10.49(i)](https://dlmf.nist.gov/10.49.i) supplies explicit spherical
formulas. The bound `j_(3/2,2)>77/10`, the complete
`j_(5/2,2)>9` argument, shell-to-ball and ball angular-shift min--max,
multiplicities, shell exclusions, and Weyl payments remain internal. The
FLPS source is not used for a shell zero or for subtracting ball
inequalities. No source-scope overreach remains.

## In-memory repository-tool audit

I used the repository's `extract_state_patch`, `parse_structured_text`,
`validate_patch_against_graph`, `apply_state_patch`, and `validate_graph`
functions entirely in memory. The authoritative graph retained its baseline
hash throughout.

The exact simulated operation result is:

- created: `SRC-ROUND19-BESSEL-ZEROS`, `SHELL-two-sided-staircase`;
- updated: `CONV-strict-counting`,
  `SHELL-sturm-liouville-completeness`,
  `SHELL-next-angular-staircase`, `SRC-LORCH`, `SRC-FLPS-balls`,
  `SHELL-rho-compact-analytic-envelope`, `SHELL-rho-compact`,
  `SHELL-rho-uniformity`, `TARGET-shell-d3`, `POLYA-program-target`,
  `COMP-certified-bessel`;
- rejected: none;
- no change: `SHELL-rho-zero-endpoint`, `SHELL-rho-one-endpoint`,
  `SHELL-fixed-rho-high-energy`, `SHELL-central-thin-seam-compression`,
  `SHELL-thin-width-phase-zero`, `SHELL-first-angular-bands`,
  `SHELL-next-angular-staircase`, `SRC-LORCH`, `SRC-FLPS-balls`,
  `SHELL-rho-compact-analytic-envelope`,
  `COMP-certified-bessel-pilot-round8`,
  `COMP-certified-bessel-pilot-round17`, `COMP-certified-bessel`,
  `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`,
  `POLYA-program-target`.

Nine IDs occur in both `update` and `no_change`. For each, `no_change`
records the unchanged mathematical status or inherited result while the
update adds reverse-edge metadata, evidence, residual bookkeeping, or next
actions. The eight no-change-only records remain byte-identical in the
simulated graph. No existing status changes.

The post-patch graph has exactly 55 unique IDs. It has no dangling
`dependencies`, `implies`, or `blockers`, no duplicate ID, and no duplicate
relationship, permitted-dependency, evidence, or other validated list entry.
The seven new canonical edges are represented exactly once in both
dependency and implication metadata:

~~~text
CONV-strict-counting --------------------+
SHELL-sturm-liouville-completeness ------+
SHELL-next-angular-staircase ------------+
SRC-LORCH -------------------------------+--> SHELL-two-sided-staircase
SRC-FLPS-balls --------------------------+          |
SRC-ROUND19-BESSEL-ZEROS ----------------+          v
                              SHELL-rho-compact-analytic-envelope
~~~

Every applicable new dependency is also permitted. The complete canonical
dependency/implies graph, blocker graph, and their union are acyclic.

Under the exact Windows behavior of `validate_round`, the judge reference
`rounds\polya-main\round_019\judge\judge-019.md` is appended once to the
`inconclusive` evidence of each created obligation and nowhere else.
Reapplying the same patch to the simulated post-patch graph is rejected with
exactly two duplicate-create errors, one for each created ID.

## Exact D19 and status audit

Subtracting the lower addition `(L,d]` only for
`1/sqrt(337)<rho<rho_c`, and the high addition `(k_5,k_6]`, from the two
components of `D18` gives exactly

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le 1/\sqrt{337},\ L(\rho)<K<U(\rho)\}\\
&\cup\{1/\sqrt{337}<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
$$

At `rho=1/sqrt(337)`, `L=d`, so the candidate fiber is empty and the
inherited slice stays in the first component. The newly covered faces are
`K=d` and `K=k_6`; `K=L`, `K=U`, `rho=rho_*`, and `rho=7/8` retain their
inherited owners, and `rho=rho_c` belongs to the high component. The 63-case
exact face truth table and 19 mandatory frequency-face checks agree with
these assignments. `B0` and `B1` were already absorbed and are not
subtracted again.

The corrected witness is strict:

$$
k_6(1/2)^2<3994/49<100,
\qquad k_6(1/2)<10<30<64<K_0(1/2)=U(1/2).
$$

Hence `(1/2,30)` lies in the third component and `D19` is nonempty.
Accordingly `SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, and `POLYA-program-target` remain `open`, while
`COMP-certified-bessel` remains `diagnostic_only`. The only new promoted
statuses are the qualified external source obligation at
`proved_external_dependency` and the independently reviewed staircase lemma
at `proved_internal`.

## Reproduction results

Final-byte reruns produced:

- public Round 19 patch validator: **PASS**;
- frozen residual self-check: **PASS**, 13 checks;
- two-sided exact verifier: **PASS**, 245 checks, first failure `null`;
- focused residual tests: **37 passed**;
- focused staircase tests: **24 passed**;
- complete repository suite: **193 passed, 10 subtests passed**;
- in-memory source compilation: **PASS**, 50 Python files;
- `git diff --check`: **PASS**;
- post-patch in-memory graph validation: **PASS**.

## Application decision

The caught defect is repaired in the authenticated final judge, and no
further issue remains. The patch may be applied exactly once with Round 19
metadata after rechecking the two required final hashes. This audit did not
apply it; `state/proof_obligations.yml` remains at the frozen baseline hash.
