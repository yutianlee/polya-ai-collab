# Round 19 Derived-State Final Audit

Date: 2026-07-14

Role: independent post-application state auditor

## Scope and authoritative bytes

I audited the applied graph and all seven synchronized projections:

- `state/current_state.md`;
- `state/best_proof_draft.md`;
- `state/lemma_bank.md`;
- `state/gap_register.md`;
- `state/next_round_prompts.md`;
- `state/last_validation_report.md`;
- `manifests/reading_packet.md`.

The final authoritative graph is
`state/proof_obligations.yml`, SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.
The same hash occurs in every projection that carries the live graph hash,
and the obsolete intermediate hash does not occur in the audited files.

The final projection hashes are:

| artifact | SHA-256 |
|---|---|
| `state/current_state.md` | `22c816deea0a5214bda11e5dd7c7e1dfc0b70e31af7a3bae9fbec1b712f1c397` |
| `state/best_proof_draft.md` | `210ad206d233748627ee296c80fd7f6999d6969535b281759a94d93c3873997f` |
| `state/lemma_bank.md` | `69538900b76622e714dbf315448650d4ff81bb72e74970e2407e2a74ebbbf860` |
| `state/gap_register.md` | `a9eeb5e50ccbadc7d8122b3b0ff914a55c45f9526c3a2c079e752b9d20aea222` |
| `state/next_round_prompts.md` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` |
| `state/last_validation_report.md` | `d5130ef910eea2d0780af7da1c3323229241f1b99273cd7c142bdbb97c6029a9` |
| `manifests/reading_packet.md` | `6ecef9aeb7d8d809daeffeb1c8f53af638b4a19180dbb3f200b30cf63f56aa15` |

## Defects caught and repaired during the audit

The first pass found two stale prospective instructions in the otherwise
applied graph. The Round 8 and Round 17 certificate-pilot `next_action`
fields still referred to reduction or future certification inside
`D18`. Because the Round 17 wording governed “any later certificate,” it
was current routing rather than merely historical prose. Both fields now
refer explicitly to the live `D19` residual, and their touched-round
metadata was refreshed. No other live `next_action` routes work to `D18`.

The first post-application full-suite run also exposed the intended
lifecycle mismatch in the immutable pre-promotion test: that test compares
advanced live state bytes with frozen pre-promotion hashes. The lifecycle
handling now marks exactly that one assertion as a strict expected failure
and independently authenticates mutable inputs from the recorded baseline
Git objects. The original residual test remains byte-immutable at
`41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787`.
Three post-promotion lifecycle tests pass. Thus the expected failure is
explicit, narrow, strict, and does not conceal a failing check.

## Graph and status audit

The graph parser and public validator reproduce:

- 55 obligation IDs, all unique;
- no dangling or duplicate dependency, implication, or blocker edge;
- no cycle in any validated graph;
- `SRC-ROUND19-BESSEL-ZEROS` at `proved_external_dependency`;
- `SHELL-two-sided-staircase` at `proved_internal`;
- `SHELL-rho-compact`, `SHELL-rho-uniformity`,
  `TARGET-shell-d3`, and `POLYA-program-target` at `open`;
- `COMP-certified-bessel` at `diagnostic_only`.

All 20 file-backed hashes in the new staircase obligation match their
current artifacts. The two source-obligation hashes match the same source
card and source audit. The historical baseline graph hash
`24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e`
matches the committed pre-promotion graph object. The final judge and
State-Patch audit hashes are, respectively,
`fdf79fa03f1cd82e5ecf4db89750aa0e5d876be6430a25e488bb1c34bdabc83b`
and
`a4cb244e9b97fb5cceaaf82896e87320c1d828d75da09a4da0bd8c13839ca76a`.

The source boundary is consistent across the graph and all projections:
the only new external numerical payload is
$j_{11/2,1}>17/2$, together with the positive spherical/ordinary Bessel
identification. The bounds $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$, both
variational comparisons, angular shifts, spectral inventories,
multiplicities, and Weyl payments remain internal.

## Exact cover, subtraction, and faces

Every audited projection states the same Round 19 result. With

$$
\rho_0=\frac1{\sqrt{337}},\qquad
L(\rho)=\frac1{2\rho},\qquad
d=\frac{\sqrt{337}}2,
$$

the promoted bands are

$$
\rho_c\le\rho\le\frac78,\qquad z_\rho\le K\le k_6(\rho),
$$

and

$$
\rho_0<\rho<\rho_c,\qquad L(\rho)<K\le d.
$$

The genuinely new set is exactly

$$
\mathcal C_{19}
=\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}
\cup
\{\rho_c\le\rho<7/8,\ k_5(\rho)<K\le k_6(\rho)\}.
$$

The live cover is consistently recorded as

$$
\mathcal A_{19}=\mathcal A_{18}
\cup\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}
\cup\{\rho_c\le\rho\le7/8,\ z_\rho\le K\le k_6(\rho)\},
$$

and exact subtraction gives

$$
\boxed{\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

Endpoint ownership is consistent everywhere. At $\rho=\rho_0$,
$L(\rho_0)=d$, the candidate fiber is empty, and the inherited slice stays
in the first component. The faces $K=d$ and $K=k_6$ are covered;
$K=U$, $\rho=\rho_*$, and $\rho=7/8$ retain inherited owners; and
$\rho=\rho_c$ belongs to the high component. The boxes $B_0,B_1$ remain
regression evidence and are not subtracted again.

The nonemptiness witness is also stated correctly:

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2).
$$

Thus $(1/2,30)$ lies in the third component of $\mathcal D_{19}$ and no
theorem-level status may close. Every remaining `D18` occurrence in the
audited projections is labeled historical, records the predecessor
subtraction $D19=D18\setminus C19$, or expressly prohibits reusing the old
mask. None is live Round 20 routing.

## Round 20 routing

All routing projections require the exact three-piece $\mathcal D_{19}$
freeze and independent face audit before a proof-free candidate is frozen.
They separate the low, middle, and high components, preserve all strict and
inclusive faces, require narrow source cards for new external zero inputs,
and retain the A3 isolation, A4 exact-audit, cross-comparison, fresh-referee,
judge, and one-time State-Patch gates. Existing Round 20 small-hole,
lower-staircase, and high-$k_8$ notes are uniformly described as exploratory
only.

## Reproduction and hygiene

Final-byte reproduction gave:

- residual-freeze self-check: **PASS**, 13 checks;
- two-sided staircase verifier: **PASS**, 245 checks, no first failure;
- current residual-focused tests: **36 passed, 1 strict expected xfail**;
- staircase-focused tests: **24 passed**;
- full lifecycle-aware suite: **195 passed, 1 strict expected xfail,
  10 subtests passed**;
- in-memory compilation: **PASS**, 52 Python files;
- graph validation: **PASS**;
- `git diff --check`: **PASS**.

No forbidden control byte occurs in the graph, the seven audited
projections, the lifecycle tests, or any other changed/untracked text file.
The Round 20 files present in the worktree are isolated prospective
artifacts; they do not alter the applied Round 19 graph or any accepted
claim. This auditor edited no existing file and wrote only this report.

**PASS. First unsupported inconsistency: none.**
