# Last Validation Report

Date: 2026-07-14

Round: 19

## Promotion decision

**PASS. First unsupported implication: none.**

The Round 19 State Patch was applied exactly once. The authoritative graph is
`state/proof_obligations.yml`, SHA-256
`ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187`.
It contains 55 unique obligation IDs, no dangling or duplicate relationship,
no impermissible dependency, and no cycle in the dependency, implication,
blocker, or combined graphs.

Created obligations:

- `SRC-ROUND19-BESSEL-ZEROS`:
  `proved_external_dependency`;
- `SHELL-two-sided-staircase`: `proved_internal`.

No existing mathematical status was promoted. In particular,
`SHELL-rho-compact`, `SHELL-rho-uniformity`,
`TARGET-shell-d3`, and `POLYA-program-target` remain `open`, while
`COMP-certified-bessel` remains `diagnostic_only`.

## Promoted source boundary

The new source obligation contributes only

$$
j_{11/2,1}>\frac{17}{2}
$$

from Lorch's strict first-positive-zero inequality and the DLMF
positive spherical/ordinary Bessel identification. Exact specialization
reduces to positive sides and

$$
507^2\cdot77-4264^2=1611077>0.
$$

The bounds $j_{3/2,2}>77/10$ and $j_{5/2,2}>9$ are internal tangent-cell
arguments. Fixed-channel zero extension, shell-to-ball min--max, ball
angular shifts, every shell exclusion, multiplicity, and Weyl payment are
also internal. No source supplies a shell cross-product zero.

## Promoted analytic staircase

Let

$$
\rho_c=\frac1{1+2\pi},\qquad
\rho_0=\frac1{\sqrt{337}},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},\qquad
d=\frac{\sqrt{337}}2.
$$

Round 19 proves

$$
\rho_c\le\rho\le\frac78,\qquad
z_\rho\le K\le k_6(\rho),
$$

and

$$
\rho_0<\rho<\rho_c,\qquad
L(\rho)<K\le d.
$$

The high inventory has strict caps
$4,9,16,25,26,29,36$; the lower inventory has strict caps
$1,4,9,10,16,17,26,29,40,45$. The exact-frequency mode at
$K=2z_\rho$, every fixed threshold, all moving walls, and every ratio face
were reconstructed and audited. The genuinely new set is

$$
\mathcal C_{19}
=\{\rho_0<\rho<\rho_c,\ L(\rho)<K\le d\}
\cup
\{\rho_c\le\rho<7/8,\ k_5(\rho)<K\le k_6(\rho)\}.
$$

## Exact surviving residual

The historical $\mathcal D_{18}$ is superseded. The live cover is
$\mathcal A_{19}$, and the exact live residual is

$$
\boxed{\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}}
$$

At $\rho=\rho_0$, $L=d$, so the candidate fiber is empty and the inherited
slice remains in the first component. The faces $K=d$ and $K=k_6$ are
covered; $K=U$, $\rho=\rho_*$, and $\rho=7/8$ keep their inherited owners,
while $\rho=\rho_c$ belongs to the high component. The boxes $B_0,B_1$
remain regression evidence and are not subtracted again.

The strict witness

$$
k_6(1/2)<10<30<64<K_0(1/2)=U(1/2)
$$

puts $(1/2,30)$ in the third component, so $\mathcal D_{19}$ is nonempty
and no theorem-level target closes.

## Validation ledger

Final-byte reproduction passed:

- public Round 19 patch validator: **PASS**;
- frozen residual self-check: **PASS, 13 exact checks**;
- two-sided staircase verifier: **PASS, 245 exact checks**, first failure
  `null`;
- residual-focused tests: **37 passed**;
- staircase-focused tests: **24 passed**;
- pre-application repository suite: **193 passed, 10 subtests passed**;
- current post-application suite: **195 passed, 1 strict expected xfail,
  10 subtests passed**; the xfail is only the immutable Round 19 freeze's
  obsolete live-path comparison, while three lifecycle tests authenticate
  the recorded hashes from baseline Git objects;
- in-memory source compilation: **PASS, 52 Python files**;
- post-application graph validation: **PASS**;
- `git diff --check`: **PASS**.

The source audit, isolated A3 reconstruction, A4 exact audit,
cross-comparison, fresh adversarial referee, judge, and independent
State-Patch audit all returned PASS. The corrected judge uses the valid
nonemptiness chain $U(1/2)=K_0(1/2)>64$; it does not assert the false
equality $K_0(1/2)=64$.

## Next method boundary

Round 20 begins by freezing the exact three-piece $\mathcal D_{19}$ and
independently auditing its classifier and strict faces. No existing Round 20
exploration is promoted. Small-hole shifted-tail, lower-staircase, and
high-$k_8$ notes are prospective directions only; any candidate must be
frozen proof-free and pass isolated A3 reconstruction, independent A4 exact
audit, cross-comparison, and a fresh adversarial referee before promotion.
