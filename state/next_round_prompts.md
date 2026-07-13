# Next Round Prompts

Generated after Round 10 in run polya-main.

## Accepted boundary

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The shell Pólya inequality is proved for every frequency in

$$
0<\rho\le\rho_*,
\qquad
1-\frac1{15625}\le\rho<1.
$$

Round 9 proved the sharper ultra-thin high theorem

$$
K\ge\frac{125}{8\varepsilon^2},
\qquad
0<\varepsilon\le\frac1{100}.
\tag{1}
$$

Round 10 proved the wider seam theorem

$$
K\ge\frac{20}{\varepsilon^2},
\qquad
0<\varepsilon\le\frac1{25},
\tag{2}
$$

and moved the central--thin switch to

$$
\rho_s=\frac{24}{25}.
$$

At the new switch,

$$
K_0(24/25)<6000^2=36000000.
$$

The strict shell inequality is therefore proved for every $0<\rho<1$ when

$$
K\ge\frac{125^5}{8}<2^{32}.
\tag{3}
$$

The all-frequency theorem remains open below (3).  The dominant planning
height now comes from the ultra-thin gap, not the central or enlarged seam
zones.

## Exact remaining ultra-thin gap

The aggregate-action theorem covers

$$
K\le L(\varepsilon)
:=\frac1{8\varepsilon^{5/2}},
\tag{4}
$$

while (1) covers

$$
K\ge U(\varepsilon)
:=\frac{125}{8\varepsilon^2}.
\tag{5}
$$

These overlap only for $\varepsilon\le1/15625$.  The next analytic target is
therefore

$$
\boxed{
\frac1{15625}<\varepsilon\le\frac1{100},
\qquad
L(\varepsilon)<K<U(\varepsilon).
}
\tag{6}
$$

Do not replace (6) by a rectangular sweep up to $125^5/8$.  It is a thin,
radius-sensitive region between two explicit curves.

## Round 11 primary target

Prove an exact intermediate bridge in (6), or enlarge the aggregate range,
so that the remaining ultra-thin residual has height below $6000^2$.

A concrete strong target is to prove complete all-frequency coverage through

$$
0<\varepsilon\le\frac1{1500}.
\tag{7}
$$

Indeed,

$$
U(1/1500)
=\frac{125}{8}\,1500^2
=35156250
<6000^2.
\tag{8}
$$

Thus (7), together with the accepted Round 10 seam, would lower the global
analytic ceiling to $6000^2$.

A different exact endpoint or piecewise bridge is acceptable if it proves a
strictly smaller dominant ceiling.  The output must include:

1. a closed explicit bridge domain and every switch point;
2. exact ownership of all boundary faces;
3. a derivation of the bridge that preserves the strict floor and spectral
   conventions;
4. the exact maximum residual height after the bridge;
5. a comparison with $6000^2$, $125^5/8$, and the previous $2^{35}$ ceiling;
6. a quantified reduction of the true compact residual plan.

Floating-point exploration may suggest constants but cannot certify them.

## For A1: obligation architect and lead synthesis

Freeze a packet SHELL-ultrathin-intermediate-bridge containing only the
accepted Round 6, Round 9, and Round 10 inputs and one exact Round 11 claim.

Write the present analytic cover as closed sets.  In particular, identify:

- ownership of $\varepsilon=1/15625$;
- ownership of the proposed new endpoint, preferably $\varepsilon=1/1500$;
- ownership of $\varepsilon=1/100$;
- equality at $K=L(\varepsilon)$ and $K=U(\varepsilon)$;
- the relation between the bridge and the sharper Round 9 high theorem.

Inventory which losses in the aggregate-action argument force the factor
$1/8$ in (4).  Separate genuine curvature/interface costs from proof
slack.  If the aggregate route cannot reach the target, freeze the first
exact failed inequality and pivot to a new intermediate decomposition
rather than weakening the conclusion numerically.

The final synthesis must select one proof and one exact ceiling.  Agent
agreement is not mathematical verification.

## For A2: analytic proof developer

Preferred route: retain the exact action

$$
\mathcal A_{\varepsilon,a}(y)
=\frac1\pi\int_0^1
\sqrt{a^2-\frac{y^2}{(1-\varepsilon s)^2}}_+\,ds
$$

and improve the aggregate/outer-strip accounting that currently stops at
(4).  Keep strict layer cake, half-integer angular multiplicities, and every
radial level explicit.

The response must:

- state an exact bridge theorem;
- prove every monotonicity claim on its full domain;
- retain radius dependence instead of substituting the worst endpoint too
  early;
- distinguish ordinary floors from strict spectral floors;
- handle equality at both bridge curves;
- provide an executable exact rational or algebraic constant ledger.

Fallback route: construct a separate intermediate-tail estimate that covers
part or all of (6) without claiming that the effective action is a global
pointwise majorant.  The Round 5 obstruction to the flat product majorant
remains valid and must not be ignored.

## For A3: clean-room reconstruction and adversarial audit

Receive only the frozen claim, definitions, and allowed prior lemmas.  First
reconstruct the proof without the incumbent response.  Then issue a separate
adversarial verdict.

Attempt to falsify the candidate at:

- $\varepsilon=1/15625$, the proposed bridge endpoint, and $1/100$;
- $K=L(\varepsilon)$ and $K=U(\varepsilon)$;
- every new piecewise switch;
- radial levels $n-1/4$ and half-integer angular walls;
- the inner-interface and outer whispering-gallery split;
- the first point where Jensen or a pointwise action comparison is used;
- every endpoint claimed to maximize a residual height;
- equality at the proposed new global ceiling;
- the exact comparison with $6000^2$.

Reject any use of the effective semicircle outside its proved pointwise
domain.  Reject sampled signs, unowned faces, inconsistent strict floors, or
circular use of a theorem that already assumes the desired bridge.

Report clean-room and adversarial verdicts separately.

## For A4: bounded certification pilot

Certification remains secondary.

At most one small rational cell may be added, and only if it shares a
complete face with the current certified pilot or proves that the face must
be split.  Retain outward-rounded Arb production and an independent exact
checker.  Test tampering of coordinates, signs, counts, truncation, face
ownership, and hashes.

Do not enumerate modes, roots, or cells toward $125^5/8$.  A local cell is
format validation, not a substitute for the analytic bridge.

## Promotion constraints

Promote a Round 11 bridge only if:

1. the bridge domain is explicit and nonempty;
2. every prior domain restriction is respected;
3. all switch faces and strict-count conventions are closed exactly;
4. the new dominant residual ceiling is proved symbolically;
5. an isolated clean-room reconstruction passes;
6. an independent adversarial constants-and-walls audit passes;
7. the executable ledger reproduces every finite comparison.

Keep SHELL-rho-compact, COMP-certified-bessel,
SHELL-rho-uniformity, and TARGET-shell-d3 open until the entire compact
residual is closed and fresh theorem-level audits pass.
