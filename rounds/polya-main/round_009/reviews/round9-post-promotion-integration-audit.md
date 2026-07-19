# Round 9 post-promotion integration audit

## Verdict

**PASS.**  The promoted Round 9 chain is internally consistent, uses the
primary constant

$$
C_{\rm lp}=\frac{125}{8},
$$

has no circular dependence on the superseded
$64\varepsilon^{-2}$ theorem, and assigns every new threshold and ratio face
without a gap.  The independently valid $C=18$ argument is retained only as
explicitly labelled fallback evidence.

This verdict was issued after correction and recheck of the notation and
typesetting findings from the first integration pass.

## 1. Sources checked

The audit read the two Round 9 theorem packets

- `state/lemma_packets/SHELL-thin-local-plateau-optimized.md`;
- `state/lemma_packets/SHELL-thin-curvature-intermediate.md`;

and the provenance-locked Round 8 compact packet
`state/lemma_packets/SHELL-rho-compact.md`.

the isolated clean-room, targeted $C=125/8$ adversarial, isolated $C=18$,
and parametric dependency reports; the optimized envelope corollary and exact
constant note; the Round 9 verifier and focused tests; the Round 9 judge; and
`state/next_round_prompts.md`.

## 2. Promoted constant ledger

All Round 9 theorem-bearing artifacts, the optimized corollary, the current
proof graph, and the next-round boundary use the same ledger:

| Quantity | Promoted value | Exact check |
| --- | --- | --- |
| high-thin constant | $C_{\rm lp}=125/8$ | clean-room and adversarial PASS |
| overlap endpoint | $\varepsilon_{\rm new}=1/15625=1/125^2$ | $1/(8C_{\rm lp})=1/125$ |
| joining frequency | $K_{\rm join}=125^5/8$ | both inclusive thresholds agree |
| thin residual ceiling | $125^5/8<2^{32}$ | exact verifier PASS |
| central residual ceiling | $180000^2<2^{35}$ | unchanged Round 8 bound |
| global analytic ceiling | $K\ge2^{35}$ | central ceiling dominates |

In particular,

$$
\frac{125^5}{8}=\frac{30517578125}{8}<2^{32},
$$

and

$$
180000^2=32400000000<34359738368=2^{35}.
$$

No occurrence of the $C=18$ endpoint $1/20736$ or its ceiling
$7739670528$ remains in the promoted packets, optimized corollary, or
next-round boundary.  The exact-arithmetic note labels its old ledger
"Fallback $C=18$"; the verifier and tests use
`C_FALLBACK`, `verify_fallback_constants`, `fallback_c18`, and
`test_round9_fallback_constant_ledger`.  Thus the executable evidence also
reflects the promotion order rather than presenting $18$ as the active
constant.

The Round 8 compact packet deliberately retains the historical
$C=64$, $\varepsilon=2^{-18}$, and $2^{42}$ envelope.  It is a hashed input
to the existing certified pilot and has SHA-256
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
Round 9 therefore does not rewrite that file.  The strengthened compact
statement is recorded in the current proof graph, optimized packet, and
envelope corollary, while the original certificate remains reproducible.

## 3. Dependency and notation audit

The optimized high-thin proof imports the unconditional Round 3 shifted-tail
decomposition and shelf ceiling

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}},
$$

but does not import the old $K\ge64\varepsilon^{-2}$ conclusion, the old
$p<8/\sqrt\varepsilon$ or $p<10/\sqrt\varepsilon$ bounds, or an old plateau
localization.  Its $t>6/7$ localization, scaled-loss bound, synthetic
$P'$ comparison, endpoint maximization, and payment margin are all rederived
under $\kappa\ge125/8$.  The aggregate-action theorem and optimized
local-plateau theorem are then combined only through their conclusions; they
are not used to prove one another.  The current compact-envelope graph
statement and Round 9 corollary depend on these two already-proved ranges,
so the promoted dependency chain is acyclic.

The dimensionful interface mesh point remains $q=x_0+n$.  The distinct
dimensionless comparison variable is now consistently written

$$
\widehat q=\frac{y^2}{\rho}(Q-1),
\qquad
\widehat q_* = \frac{41}{137500},
$$

throughout the clean-room report, targeted adversarial report, dependency
audit, and frozen optimized packet.  A search found no residual use of plain
$q$ for this dimensionless quantity in the promoted argument.

## 4. Endpoint and face ownership

The two frequency ranges are inclusive:

$$
K\le\frac1{8\varepsilon^{5/2}},
\qquad
K\ge\frac{125}{8\varepsilon^2}.
$$

At $\varepsilon=1/15625$ they meet at exactly $125^5/8$, so the joining
frequency is owned by both compatible analytic theorems and no point is
lost.  The complete thin endpoint owns

$$
1-\frac1{15625}\le\rho<1
$$

analytically.  The current closed compact planning interval includes the
face $\rho=1-1/15625$, and the Round 9 corollary and proof graph treat that
face as analytically owned rather than a numerical-certificate obligation.
The provenance-locked Round 8 packet retains its former face
$\rho=1-2^{-18}$ as historical certificate metadata.

On $1/15625\le\varepsilon\le1/100$, the true unresolved thin set has the
strict frequency inequalities $L(\varepsilon)<K<U(\varepsilon)$; the packet's
closed $\mathcal R_T$ is deliberately only an over-cover whose threshold
faces are analytically owned.  The central/thin switch $\rho=99/100$ and the
left/central switch $\rho=1/16$ are inclusive with explicit neighboring or
analytic ownership.  Since every residual is strictly below $2^{35}$, the
face $K=2^{35}$ belongs to the analytic high-energy conclusion.

The corollary now describes the *newly* removed certificate band precisely as

$$
2^{-18}<\varepsilon\le\frac1{15625};
$$

the equality $\varepsilon=2^{-18}$ was already analytically owned in Round 8.

## 5. Exact and source-hygiene checks

The independent rational verifier reproduced, without floating point,

$$
\frac{\partial H}{\partial P}
<\frac{673816}{1366875}<\frac12,
$$

the no-drop margin

$$
\frac{72581986185449}{5925464687161600}>0,
$$

and the final payment margin

$$
\frac{2428603}{653221800}>0.
$$

The following commands passed after the editorial corrections:

```text
python computations/round9_verify_thin_plateau_constants.py
python -m pytest computations/tests/test_round9_thin_plateau_constants.py -q
python -m compileall -q computations/round9_verify_thin_plateau_constants.py computations/tests/test_round9_thin_plateau_constants.py
git diff --check
```

The focused test result was `2 passed`.  A direct scan of every audited file
also passed for forbidden control characters, trailing whitespace, mixed
newline styles, and unbalanced `$$`, `\[...\]`, or `\(...\)` delimiters.
The corrected `\qquad` commands in the targeted adversarial report and judge
were re-read in place.

## Final integration conclusion

The Round 9 promotion may stand with $C=125/8$ as the sole active
local-plateau constant.  It proves the complete thin endpoint through
$\varepsilon=1/15625$ and the all-ratio analytic range $K\ge2^{35}$, while
leaving the compact residual below that ceiling and all theorem-level parent
obligations open exactly as recorded in the next-round prompts.
