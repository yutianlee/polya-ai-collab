# Last Validation Report

Date: 2026-07-14

Round: `polya-main` / round 14

## State patch

- Source: `rounds/polya-main/round_014/judge/judge-014.md`.
- `SHELL-central-thin-seam-compression` remains `proved_internal` and is
  strengthened to

  $$
  0<\varepsilon\le\frac18,
  \qquad
  K\ge\frac{32}{\varepsilon^2}.
  $$

- The sharper retained thresholds are $K\ge24/\varepsilon^2$ on
  $0<\varepsilon\le1/10$ and $K\ge20/\varepsilon^2$ on
  $0<\varepsilon\le1/25$.
- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`; the seam
  moves to $\rho=7/8$, the exact endpoint estimate is
  $K_0(7/8)<550^2$, and the all-ratio analytic ceiling becomes
  $K\ge550^2$.
- The complete all-frequency thin endpoint remains exactly
  $99/100\le\rho<1$.
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` remain
  `open`. `COMP-certified-bessel` remains `diagnostic_only`.
- No route is newly rejected. Round score: 6.

The judge State Patch validated before application and was applied exactly
once. It must not be replayed against the promoted graph.

## Analytic proof routes and reserves

- Frozen Round 14 dependency packet and hash: PASS.
- Incumbent full-domain proof: PASS.
- Independent finite-constant inventory: PASS.
- Strictly isolated clean-room reconstruction: PASS.
- Fresh adversarial branch, wall, face, and global-union audit: PASS; first
  unsupported implication: none.

The incumbent proof and the independent constant inventory rederive every
domain-dependent estimate on the full enlarged domain. They prove

$$
d>\frac23,
\qquad
\widehat q<\frac{17}{40},
\qquad
R<\frac{14}{3\sqrt\varepsilon}.
$$

The early exact reserves include

$$
\left(\frac78\right)^2-\frac34=\frac1{64},
\qquad
\left(\frac{67}{400}\right)^2-\frac{1571/500}{112}
=\frac3{1120000},
$$

and

$$
\frac{17}{40}-\frac{3757}{8960}
=\frac{51}{8960}>0.
$$

They imply the strict outer localization

$$
\frac{x_0}{K}>
\frac{161}{320}
=\frac12+\frac1{320}.
$$

For the incumbent's complete fixed-$r=B$ synthetic path, with $B=14/3$,
the derivative estimate has reserve

$$
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0.
$$

The no-drop endpoint, dangerous-payment, and safe-payment reserves are

$$
\frac{49714811804}{82306584375}>0,
\qquad
\frac{98646127309}{8083619775}>0,
\qquad
\frac{205339021309}{8083619775}>0.
$$

The strictly isolated clean-room proof does not reuse that finite comparison.
It first proves $P<9$ and then uses the distinct affine majorant

$$
\overline S(P)=\frac52P-7.
$$

Its endpoint and complete-path derivative reserves are

$$
\frac{3627793}{7225344}>0,
\qquad
\frac{1178207}{150528}>0,
$$

and its dangerous- and safe-payment reserves are

$$
\frac{3229}{275}>0,
\qquad
\frac{20467}{825}>0.
$$

Both architectures own the no-drop $p=n$, immediate-drop $p=0<n$,
degenerate-head $n=0$, sign wall $R=0$, and first $R>0$ branches. They also
own every ordinary-floor, coarse-proxy, gain, interface, threshold,
angular-cutoff, and strict spectral wall, with every denominator, radicand,
and squaring sign checked.

At $\varepsilon=1/8$ and $\kappa=24$, the current architecture proves only
the lower bound

$$
\frac{x_0}{K}>\frac{173}{384},
\qquad
\frac{173}{384}<\frac12.
$$

Thus this lower bound does not localize beyond $1/2$. This is the first
obstruction in that constant-$24$ proof route. It is not a counterexample and
does not disprove a possible stronger constant-$24$ theorem.

## Accepted Round 14 theorem

Including threshold equality,

$$
\boxed{
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

At $\rho=7/8$, the independent fixed-ratio calculation gives

$$
\eta_{7/8}>\frac1{76},
\qquad
\sqrt{a_{7/8}}<7,
\qquad
C_0<\frac{307}{175}.
$$

For $Y=550$, the defining quadratic therefore has exact positive margin

$$
\frac1{76}Y^2-7Y-\frac{307}{175}
=\frac{427292}{3325}>0.
$$

Its unique positive root lies below $550$, so

$$
\boxed{K_0(7/8)<550^2.}
$$

## Closed six-zone global union

The accepted analytic zones are:

1. on $[\rho_*,1/16]$, every possible residual has $K<64$;
2. on $[1/16,7/8]$, every possible residual has
   $K<K_0(\rho)\le K_0(7/8)<550^2$;
3. on $[7/8,9/10]$, every possible residual has
   $K<32/(1-\rho)^2\le3200$;
4. on $[9/10,19/20]$, every possible residual has
   $K<24/(1-\rho)^2\le9600$;
5. on $[19/20,24/25]$, every possible residual has
   $K<24/(1-\rho)^2\le15000$;
6. on $[24/25,99/100]$, every possible residual has
   $K<20/(1-\rho)^2\le200000$.

The shared faces are owned explicitly. The small-hole theorem owns
$\rho=\rho_*$, and the adjacent central theorems own $\rho=1/16$. At
$\rho=7/8$, Round 14 owns $K=2048$. At $\rho=9/10$, Round 13 owns the
sharper $K=2400$ face, and hence also the coarse $K=3200$ face. At
$\rho=19/20$, the retained constant-$24$ theorem owns $K=9600$. At
$\rho=24/25$, Round 10 owns the sharper $K=12500$ face, while the left-hand
coarse enclosure reaches $15000$. At $\rho=99/100$, the complete endpoint
owns every $K$, including $200000$. The adjacent central result owns the
$K=64$ face, and the strict $K_0(7/8)$ comparison owns $K=550^2$.

Since

$$
64<3200<9600<15000<200000<550^2,
$$

the complete high-frequency conclusion is

$$
\boxed{
0<\rho<1,
\qquad K\ge550^2
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reduction from the Round 13 ceiling is

$$
\frac{900^2}{550^2}=\frac{324}{121}>2.
$$

## Complete thin endpoint

Round 14 does not enlarge the all-frequency endpoint. The accepted product,
aggregate, and complementary-action ranges still prove exactly

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

The Round 14 seam theorem is high-frequency only.

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad
K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 14 changes no producer, checker,
certificate, or protected packet. The independent checker reproduces the
unchanged protected packet hash
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
This remains evidence for one local box only; the parent compact
certification remains `diagnostic_only`.

## Mechanical validation

- Judge State Patch validation before application: PASS.
- State Patch applied exactly once: PASS.
- Embedded incumbent exact ledger: PASS.
- Standalone exact ledger reproducing both analytic paths: PASS.
- Focused Round 14 tests: 6 passed.
- Complete computation suite: 51 passed.
- Proof graph, dependency DAG, and 530 referenced evidence paths at the
  Round 14 review gate: PASS.
- Round 8 independent certificate and provenance checker: PASS.
- Python compilation, Markdown whitespace, and diff checks at the Round 14
  review gate: PASS.

A fresh independent post-promotion state audit: PASS. It found 49 obligation
IDs, no broken dependency, permitted-dependency, blocker, or implication
references, an acyclic dependency graph, and all 566 current
artifact-reference occurrences (141 unique paths) present. The count includes
`source_card`; `evidence.positive`, `evidence.negative`, and
`evidence.inconclusive`; `clean_room_artifacts`;
`adversarial_review_artifacts`; and `certification_artifacts`. First
unsupported implication: none.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge550^2$. The full all-frequency
theorem remains open on the exact compact residual

$$
\boxed{
\mathcal D_{14}
=(I_{14}\times[0,\infty))\setminus\mathcal A,
\qquad
I_{14}=\left[\rho_*,\frac{99}{100}\right],
}
$$

below that ceiling. Here $\mathcal A$ is the complete accepted analytic
cover, including every threshold face. The six-zone envelope is a planning
cover of the complement; it must not be replaced by the rectangle
$I_{14}\times[0,550^2)$.

Round 15 may separately test

$$
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2},
\qquad
\rho_s=\frac56,
\qquad
K_0(5/6)<295^2.
$$

If all those claims and their shared faces were proved, the retained
$[24/25,99/100]$ zone would still have ceiling $200000$, so the prospective
global high-frequency ceiling would be $K\ge200000$, not $295^2$. Every
Round 15 number in this paragraph is an unproved planning target; no Round 14
estimate may be extrapolated to it. After the compact residual closes, fresh
theorem-level clean-room and adversarial audits remain mandatory before
promotion of the final target.
