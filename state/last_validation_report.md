# Last Validation Report

Date: 2026-07-14

Round: `polya-main` / round 16

## Promotion decision

- Judge: `rounds/polya-main/round_016/judge/judge-016.md`.
- Judge SHA-256:
  `6f54dfdea0b88642e5d0b1cf6a3e7fdadd4bbc870e1978112defb6cbf189aa06`.
- Decision: **PASS**. First unsupported implication: none.
- The State Patch validated against the untouched Round 15 graph, received an
  independent read-only in-memory application audit, and was applied exactly
  once. It must not be replayed against the promoted graph.
- No obligation was created or rejected. Round score: 8.

The patch strengthens `SHELL-rho-one-endpoint` and
`SHELL-rho-compact-analytic-envelope`, both already `proved_internal`.
`SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` remain
`open`; `COMP-certified-bessel` remains `diagnostic_only`.

The durable graph hashes are:

- untouched Round 15 baseline:
  `b96477f650230d847dc72db851be997752f6a50822cf47e57b13ce9d362d9bd5`;
- immediately after the one-time State Patch:
  `bfbf9c1209f598ff691d9eec62584e919723722bf7b0583bbf11c702c51128be`;
- after the Round 17 target-selection update:
  `dc2552091ff79f5ab39de896b4d97cf22ccc234f3842ee9734d54d123c5f2379`.

## Frozen artifacts and independent reviews

| Artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `rounds/polya-main/round_016/responses/thin-endpoint-incumbent.md` | `bc99a0e82bee9f55056e2122f053418b8b6f2586fad515dd115f6d29fb6878b0` |
| `rounds/polya-main/round_016/reviews/thin-endpoint-clean-room.md` | `5a4945c267c0f9d769bec6cf94ad6f7cb3d17c5af593d1837d27553cefb197d7` |
| `rounds/polya-main/round_016/exploration/thin-endpoint-constant-inventory.md` | `0aeb81f3186d7e8a3ef2d9623edc6bbfd6ab04744079dbc26bcc2b90e77df933` |
| `rounds/polya-main/round_016/reviews/thin-endpoint-adversarial-referee.md` | `185369546a0d88c5d0fdc72ae3390167e67edeb1b4cdd03074a5f1611fdec5fd` |
| `computations/round16_verify_endpoint.py` | `7be9208c5abdb233db18c15dbae87068b134121ee5efcd3825ee293f346afff5` |
| `computations/tests/test_round16_endpoint.py` | `4f372a5860ea33b19a80daadbb5ddd4382fb11be5e2f8f543a4fdd223a7d219c` |

The frozen packet audit checked 40 nontrivial identity groups. The incumbent,
strictly isolated clean-room proof, independent constant inventory, and fresh
hostile referee all returned PASS. The hostile referee then authenticated the
two editorial repairs byte-for-byte and again found no unsupported
implication. The 18-file lemma-packet manifest stayed unchanged at
`1eb2b951baf034793c9c6b6ec9efcf0857abf6b7b746ee43be343d69bbf162d3`.

## Promoted thin endpoint

Write

$$
\rho=1-\varepsilon,
\qquad
a=\varepsilon K,
\qquad
0<\varepsilon\le\frac18.
$$

The low product piece owns

$$
0\le a\le\frac{\pi}{4\varepsilon}.
$$

The min--max direction, strict radial count, zero range $0\le a\le\pi$,
radial and angular walls, and common face were independently reconstructed.
The exact deficit satisfies $D>(2/5)a^2$, and the final normalized reserve is

$$
\frac25-\left(\frac16+\frac1{32}+\frac1{576}\right)
=\frac{577}{2880}>0.
$$

The high complementary-action piece owns

$$
a\ge\frac{\pi}{4\varepsilon}.
$$

Its audit covers the exact action inverse, the actual ungridded curvature
interface, the improper $t=0$ trace, shifted-sawtooth Stieltjes directions,
strict half-integer and phase-proxy walls, and the common face. At the closed
ratio endpoint,

$$
\frac{D_{\rm rad}}{a^2}\ge\frac{21}{256},
\qquad
\frac{E}{a^2}<\frac{193}{4096},
\qquad
D_{\rm rad}-E>\frac{143}{4096}a^2>0.
$$

Both inclusive pieces own $a=\pi/(4\varepsilon)$, including the corner
$(\varepsilon,a)=(1/8,2\pi)$ and its radial wall. They use none of the
blacklisted Round 5, 6, or 11 conclusions. Their union proves

$$
\boxed{
\frac78\le\rho<1,
\qquad K\ge0,
\qquad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The face $\rho=7/8$ is included and $\rho=1$ is the excluded degenerate
limit. At $K=0$ both sides vanish; for $K>0$ the product or phase-proxy
comparison is strict before the final non-strict theorem statement.

## Four-zone integration

Let

$$
I_{16}=\left[\rho_*,\frac78\right].
$$

The accepted analytic cover now has four zones:

1. on $[\rho_*,1/16]$, a residual point can occur only for $K<64$;
2. on $[1/16,5/6]$, only for
   $K<K_0(\rho)\le K_0(5/6)<295^2=87025$;
3. on $[5/6,7/8]$, only for
   $K<54/(1-\rho)^2\le3456$;
4. on $[7/8,1)$, no residual point occurs because every frequency is covered.

All ratio, threshold, and equality faces are owned. In particular,
$K=295^2$ is covered in every ratio band. Hence

$$
\boxed{
0<\rho<1,
\qquad K\ge295^2=87025
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reduction from the Round 15 ceiling is

$$
\frac{200000}{295^2}=\frac{8000}{3481}>2.
$$

## Exact remaining boundary

The full all-frequency shell theorem is not proved. If $\mathcal A_{16}$ is
the complete accepted analytic cover with every owned face included, the
sole shell blocker is

$$
\boxed{
\mathcal D_{16}
=\bigl(I_{16}\times[0,\infty)\bigr)\setminus\mathcal A_{16}.
}
$$

This is a nonrectangular set and is not
$I_{16}\times[0,87025)$. The Round 8 certified pilot remains unchanged and
local. Any future certified extension must be an exact bounded,
face-connected subset of $\mathcal D_{16}$; the Round 16 rational ledger is
analytic finite-algebra evidence, not a Bessel-root certificate.

The positive endpoint screens at $\rho=6/7$ and $\rho=23/27$ remain
unproved. The negative screens at $\rho=17/20$ and $\rho=5/6$ are route
obstructions only, not counterexamples.

## Mechanical validation

- Standalone exact verifier: PASS, 111 finite-algebra checks.
- Focused Round 16 tests: 11 passed.
- Complete computation suite: 69 passed.
- Python compilation over `computations` and `math_collab`: PASS.
- Embedded incumbent ledger: PASS.
- Round 8 independent certificate checker: PASS; its protected packet hash
  remains
  `8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
- Pre-application patch audits: PASS in both the validator and an independent
  in-memory simulation.
- Final graph: 49 unique obligation IDs, 165 dependency edges, acyclic, with
  every dependency, permitted dependency, blocker, and implication resolved.
- Graph artifacts: 626 reference occurrences, 155 normalized paths, all
  present.
- The finite verifier explicitly reports `analytic_theorem_verified=false`.
  A separate 47-point floating diagnostic was not used as proof.
- Reading-packet regeneration and the live Round 17 handoff: PASS. A focused
  prompt audit found one missing A4 ownership assignment; after repair, the
  re-audit passed at prompt SHA-256
  `239728539661aa0f11f0a309eb677d607fd03bbbeec26bad7c983969a5bd884e`.
- UTF-8, control-character, trailing-whitespace, final-newline, Markdown
  delimiter, stale-operative-language, and Git diff checks: PASS.
- Fresh post-promotion theorem/state audit: PASS; first unsupported
  implication: none. It independently reproduced the one-time State Patch,
  graph counts, hashes, theorem boundary, and evidence-class limits.

## Authoritative next step

Round 17 must freeze the exact $\mathcal A_{16}$ membership mask and close
$\mathcal D_{16}$ by analytic or symbolic compression. At most one closed,
face-connected extension of the Round 8 pilot may be attempted as subordinate
local evidence. A fresh clean-room reconstruction and hostile referee are
mandatory for any promoted residual lemma, and fresh theorem-level reviews
remain mandatory before closing `TARGET-shell-d3`.
