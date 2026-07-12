# Last Validation Report

Date: 2026-07-13

Round: polya-main / round 5

State patch:

- rounds/polya-main/round_005/judge/judge-005.md;
- validated before application and applied exactly once at round index 5;
- created one proved partial thin-shell lemma and one open
  radius-sensitive bottleneck;
- rejected two flat-product proof routes;
- did not promote either endpoint parent or the full shell theorem.

Validation results:

- proof-obligation graph after application: PASS;
- embedded Round 5 State Patch before application: PASS;
- isolated clean-room theorem/obstruction review: PASS;
- adversarial theorem/obstruction review: PASS;
- corrected endpoint/constants re-audit: PASS;
- Python regression suite: 15 passed;
- Python compile check: PASS;
- git diff whitespace check: PASS;
- MathJax preview generation for all Round 5 artifacts and refreshed state
  drafts: PASS.

Authoritative theorem boundary:

For every fixed $0<\rho<1$, the shell Pólya estimate is proved for
$K\ge K_0(\rho)$. In addition, with $\varepsilon=1-\rho$,

$$
0<\varepsilon\le\frac1{100},
\qquad
0\le K\le\frac{\pi}{4\varepsilon^2}
$$

is now a proved uniform thin-shell window. The radius-sensitive interval
between that window and $K_0(1-\varepsilon)$, the small-hole endpoint, and
certified finite closure remain open.
