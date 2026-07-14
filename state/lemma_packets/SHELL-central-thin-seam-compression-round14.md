# Lemma Packet: Round 14 Central--Thin Seam Extension

Obligations: `SHELL-central-thin-seam-compression`,
`SHELL-rho-compact-analytic-envelope`, and `SHELL-rho-compact`.

Round: 14.

Status: frozen candidate. Nothing in this packet asserts the Round 14 claim.
The packet becomes authoritative only after an incumbent proof, a strictly
isolated clean-room reconstruction, an adversarial review, an executable
exact ledger, and the judge gate all pass.

The clean-room reviewer may inspect only this packet and the proved inputs
listed below before issuing a separate verdict. The reviewer must not inspect
any Round 14 response, exploration, computation, test, review, ledger, judge
artifact, agent message, or incumbent proof before that verdict. The
candidate constants and reserves below are navigation aids, not proved
inputs.

## Frozen local claim

Let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac18.
$$

Prove, including threshold equality,

$$
\boxed{
K\ge\frac{32}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

The constant $32$ is a candidate, not an assumed fact. If it fails, freeze
the first exact failed inequality and report the strongest theorem actually
proved. Do not replace a failed exact sign by a decimal or sampled sign.

## Required piecewise use of proved seam theorems

The following three results are retained only on their proved domains.

Round 10:

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
\tag{2}
$$

Round 12:

$$
0<\varepsilon\le\frac1{20},
\qquad
K\ge\frac{24}{\varepsilon^2}.
\tag{3}
$$

Round 13:

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2}.
\tag{4}
$$

The genuinely new coverage sought from (1) is

$$
\frac1{10}\le\varepsilon\le\frac18,
\qquad
\frac78\le\rho\le\frac9{10}.
\tag{5}
$$

At every overlap, use the sharpest accepted theorem. In particular, the
face $\varepsilon=1/10$ is owned by Round 13 at the sharper threshold
$24/\varepsilon^2$, even if (1) is proved there at $32/\varepsilon^2$.
Likewise Round 10 remains sharper on its domain. The proposed new seam face
is

$$
\varepsilon=\frac18,
\qquad
\rho=\frac78.
\tag{6}
$$

The complete all-frequency endpoint remains exactly
$99/100\le\rho<1$. Neither (1) nor any retained high-frequency seam theorem
enlarges that endpoint.

## Definitions supplied to the isolated reviewer

For $a>0$, define

$$
G_a(z)=\frac1\pi
\left(
\sqrt{a^2-z^2}-z\arccos\frac za
\right),
\qquad 0\le z\le a,
$$

and extend $G_a$ by zero for $z\ge a$.

For a low-interface shifted tail beginning at $x_0=r_0+1/2<\mu$, put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
\qquad
\eta=G_1(\rho).
\tag{7}
$$

Write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1).
\tag{8}
$$

For $n\ge1$, define

$$
h_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor.
\tag{9}
$$

If the first drop occurs after index $p$, define $p$ by

$$
h_0=h_p>h_{p+1},
\qquad 0\le p<n;
$$

if no drop occurs, set $p=n$. Thus $p=0$ is the immediate-drop branch and
$p=n$ is the no-drop branch. Set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta,
\qquad
R=p-dm.
\tag{10}
$$

For the degenerate head $n=0$, use $p=m=0$. Only the branch $R>0$
requires a new plateau-loss payment; $R=0$ is a separate sign wall and may
not be merged into it.

Use the scaled variables

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4,
\qquad
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{11}
$$

The candidate domain is exactly

$$
0<y\le\frac1{2\sqrt2},
\qquad
\rho=1-y^2\ge\frac78,
\qquad
\kappa\ge32.
\tag{12}
$$

All divisions, square roots, and squarings in a proof must have their sign
conditions established on (12), including on the equality faces
$y=1/(2\sqrt2)$ and $\kappa=32$.

## Permitted proved inputs for the local claim

1. `CONV-strict-counting` and the exact separated shell spectrum from
   `SHELL-sturm-liouville-completeness`.
2. `SHELL-phase-enclosures`, the strict-to-ordinary-floor transfer,
   `SHELL-weighted-lattice-scaffold`, and
   `SHELL-high-angular-shifted-tails`, only as stated in those promoted
   obligations.
3. With

   $$
   b_\ell=
   \left\lfloor
   A\!\left(\ell+\frac12\right)+\frac14
   \right\rfloor,
   \qquad
   \mathcal T_{r_0}=b_{r_0}+2\sum_{\ell>r_0}b_\ell,
   $$

   the audited pre-threshold Round 3 low-interface decomposition from
   `SHELL-low-interface-fixed-rho-high-energy`

   $$
   \frac{\mathcal T_{r_0}}2
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   \tag{13}
   $$

   where

   $$
   M=\lfloor K\eta\rfloor+d(n-p)-p
   =\lfloor K\eta\rfloor-R,
   \qquad
   \delta=\int_q^\mu G_\mu(z)\,dz,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   \tag{14}
   $$

   together with the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   \tag{15}
   $$
4. The exact action identity

   $$
   \eta=G_1(1-\varepsilon)
   =\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv,
   \tag{16}
   $$

   and the elementary inequality
   $\arccos(1-v)\ge\sqrt{2v}$, provided every use and every resulting
   constant is reconstructed on (12).

The following are permitted only for the endpoint comparison and closed
global union. They are not dependencies that may be used to prove (1).

5. The promoted Round 10, Round 12, and Round 13 statements (2)--(4), only
   on their displayed domains. No intermediate inequality from an earlier
   proof may be extrapolated beyond its proved parameter range.
6. `SHELL-fixed-rho-high-energy`: with

   $$
   a_\rho=\frac{2\pi\rho}{1-\rho},
   \qquad
   \eta_\rho=G_1(\max\{\rho,1/2\}),
   \qquad
   C_0=1+\frac{8\sqrt2}{15},
   $$

   the theorem holds for $K\ge K_0(\rho)$, where

   $$
   K_0(\rho)=
   \left(
   \frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
        {2\eta_\rho}
   \right)^2.
   \tag{17}
   $$

   The already-audited monotonicity of $K_0$ on the relevant central
   interval is permitted.
7. For the prospective all-ratio corollary only, the proved small-hole
   endpoint, fixed-ratio central theorem, Round 10--13 seam theorems, and
   Round 11 all-frequency endpoint $99/100\le\rho<1$ may be assembled.
   The desired Round 14 seam, endpoint, and compact envelope are not inputs
   to (1).

## Preliminary exact screen: navigation aids only

A read-only screen suggests

$$
d_0=\frac23,
\qquad
\overline q=\frac{17}{40},
\qquad
B=\frac{14}{3}.
\tag{18}
$$

These are candidate comparison constants, not assumed bounds. In
particular, a proof must derive the precise statements in which $d_0$ and
$\overline q$ occur and prove the required strict or weak directions on the
whole closed candidate domain.

The same screen records, without proving the expressions to which they
belong,

$$
\frac1{64}>0
\quad\text{(angular reserve)},
\qquad
\frac3{1120000}>0
\quad\text{(radical reserve)},
\tag{19}
$$

$$
\frac{51}{8960}>0
\quad\text{(displacement reserve)},
\tag{20}
$$

and the candidate dangerous-plateau localization

$$
\frac{x_0}{K}>
\frac{161}{320}
=\frac12+\frac1{320}.
\tag{21}
$$

For a prospective synthetic comparison path, the screen gives the
candidate derivative cap and reserve

$$
\frac{117036972261}{23847320000}<5,
\qquad
5-\frac{117036972261}{23847320000}
=\frac{2199627739}{23847320000}>0,
\tag{22}
$$

candidate path slope $13/3$, candidate endpoint reserve

$$
\frac{49714811804}{82306584375}>0,
\tag{23}
$$

candidate dangerous-branch payment reserve

$$
\frac{98646127309}{8083619775}>0,
\tag{24}
$$

and candidate safe-branch reserve

$$
\frac{205339021309}{8083619775}>0.
\tag{25}
$$

Every formula to which (19)--(25) belongs, every monotonic reduction used
to reach it, and every strictness direction must be reconstructed. Merely
reproducing these positive fractions is not a proof.

The same architecture with $\kappa=24$ currently yields only

$$
\frac{x_0}{K}>\frac{173}{384}<\frac12.
\tag{26}
$$

This failure of the current localization route is **not a disproof** of a
possible theorem with $\kappa=24$. It identifies only the first obstruction
in this proof architecture. No reviewer may report (26) as a counterexample
to the shell inequality.

## Required new analytic work

Every Round 13 step that depended on
$\varepsilon\le1/10$ must be rederived on (12). No Round 13 intermediate
estimate is grandfathered. Independently, the incumbent and clean-room
reviewer must reconstruct:

1. a uniform bound for
   $d=1-2\arccos(1-\varepsilon)/\pi$ with all endpoint strictness, and any
   claimed use of $d_0=2/3$;
2. from $R>0$, the exact relation among $P$, $r$, and $S$, followed by a
   uniform proof of dangerous-plateau localization $x_0/K>1/2$ before any
   outer-region slope is used;
3. the local-slope inequality, including why equal ordinary-floor values
   imply the strict difference $A(x_0)-A(x_0+p)<1$ at integer walls;
4. a self-consistency inequality of the form

   $$
   P^2<
   \frac{2\pi^2Q}{(1-\widehat q)^2},
   \qquad
   Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
   \qquad
   \widehat q=\frac{y^2}{\rho}(Q-1),
   \tag{27}
   $$

   including the proof that $1-\widehat q>0$, every other denominator is
   positive, and every squaring preserves the claimed direction;
5. if $\overline q=17/40$ is used, an exact uniform derivation of
   $\widehat q<\overline q$ rather than an appeal to the screen;
6. an exact $B$ such that $R<B/\sqrt\varepsilon$, proved along the entire
   synthetic comparison path, including its derivative control and the
   no-drop endpoint $P=r=B$; endpoint positivity alone is insufficient;
7. enough action gain to prove $M>4\delta$ after the full possible floor
   loss, separately for the dangerous branch $R>0$ and safe branch
   $R\le0$;
8. the angular, radical, displacement, path, endpoint, and payment
   comparisons behind (19)--(25), with exact arithmetic and all worst-case
   endpoint reductions justified;
9. the immediate-drop branch $p=0$, degenerate head $n=0$, no-drop branch
   $p=n$, sign wall $R=0$, and first branch with $R>0$;
10. every ordinary-floor, gain, interface, threshold, and strict spectral
    wall, including threshold equality in (1).

No sampled sign, decimal approximation, numerical optimizer, or finite
parameter sweep proves any item above. An executable rational or algebraic
ledger must reproduce every finite comparison, but the ledger does not
replace the symbolic proof or the branch analysis.

## Independent exact central endpoint target

Prove from (17), without decimal evaluation,

$$
\boxed{K_0(7/8)<550^2.}
\tag{28}
$$

The preliminary screen suggests

$$
\eta_{7/8}>\frac1{76},
\qquad
\sqrt{a_{7/8}}<7,
\qquad
C_0<\frac{307}{175}.
\tag{29}
$$

These bounds remain candidates until reconstructed. A candidate exact route
is to use (16) at $\varepsilon=1/8$ and exact rational bounds for $\pi$ and
$\sqrt2$, and to note

$$
a_{7/8}=14\pi<7^2.
\tag{30}
$$

At $Y=550$, the proposed quadratic comparison is

$$
\frac1{76}Y^2-7Y-\frac{307}{175}
=\frac{427292}{3325}>0.
\tag{31}
$$

The proof must derive (29)--(31) exactly and explain why positivity at $Y$
places the unique positive root of

$$
\eta_{7/8}X^2-\sqrt{a_{7/8}}X-C_0=0
$$

strictly below $Y$, hence gives (28). The endpoint target (28) is logically
independent of the local seam claim (1); neither may be used to prove the
other.

## Required prospective closed global union

If and only if both (1) and (28) pass every gate, split the current five
finite residual zones into the following six finite zones, followed by the
unchanged all-frequency endpoint:

1. every possible residual on $[\rho_*,1/16]$ has $K<64$;
2. every possible residual on $[1/16,7/8]$ has
   $K<K_0(7/8)<550^2$;
3. on $[7/8,9/10]$, (1) leaves the coarse possible residual bound

   $$
   K<\frac{32}{(1-\rho)^2}\le3200;
   $$

4. on $[9/10,19/20]$, Round 13 leaves possible residual only below

   $$
   K<\frac{24}{(1-\rho)^2}\le9600;
   $$

5. on $[19/20,24/25]$, the retained constant-$24$ theorem leaves possible
   residual only below $15000$;
6. on $[24/25,99/100]$, Round 10 leaves possible residual only below
   $200000$;
7. every frequency on $[99/100,1)$ is already proved.

The six finite intervals are deliberately closed and overlap at their
faces. Face ownership must use the sharpest available theorem:

- $\rho=\rho_*$ and $\rho=99/100$ are owned by the adjacent complete
  all-frequency theorems;
- $\rho=7/8$ is owned by (1), if proved, including
  $K=32/(1/8)^2=2048$;
- $\rho=9/10$ is owned by Round 13 at the sharper threshold $K=2400$, not
  merely by the candidate $K=3200$ threshold;
- $\rho=19/20$ is owned at $K=9600$ by the constant-$24$ theorem;
- $\rho=24/25$ is owned by Round 10 at the sharper threshold $K=12500$;
- $\rho=1/16$ is checked from both adjacent analytic regimes.

Thus the displayed zone bounds are coarse enclosures of the exact
complement of the analytic cover; they do not supersede sharper ownership
on overlaps. Since

$$
64<3200<9600<15000<200000<550^2,
\tag{32}
$$

the prospective consequence is

$$
\boxed{
0<\rho<1,
\qquad
K\ge550^2.
}
\tag{33}
$$

The equality face $K=550^2$ must be included. The exact prospective
reduction from the Round 13 ceiling is

$$
\frac{900^2}{550^2}=\frac{324}{121}>2.
\tag{34}
$$

Neither (33) nor the six-zone envelope is an all-frequency shell theorem.
The exact compact residual below the new ceiling would remain open.

## Mandatory exceptional branches and falsification faces

The incumbent, clean-room reconstruction, ledger, and adversarial review
must explicitly test or symbolically own all of the following.

### Parameter and theorem-overlap faces

- $\varepsilon=1/100$, $1/25$, $1/20$, $1/10$, and $1/8$;
- $\kappa=20$ on the retained Round 10 domain, $\kappa=24$ on the retained
  Round 12--13 domains, and $\kappa=32$ on the whole candidate domain;
- $\rho=99/100$, $24/25$, $19/20$, $9/10$, and $7/8$, approached from
  both adjacent regimes;
- $\rho=\rho_*$ and $\rho=1/16$, approached from both adjacent regimes.

### Plateau and interface branches

- no drop $p=n$;
- immediate drop $p=0$;
- degenerate head $n=0$;
- the sign wall $R=0$ from both sides;
- the first branch with $R>0$;
- the wall $\mu-x_0\in\mathbb Z$ and both adjacent values of $\beta$;
- $q=\mu$, where $\delta=0$;
- the low/high interface $x_0=\mu$;
- the angular cutoff wall $\nu=K$.

### Discrete, analytic, and synthetic walls

- every ordinary-floor wall in (9);
- every coarse-proxy integer wall and the gain wall $K\eta\in\mathbb Z$;
- the complete synthetic $P$-comparison path, not only its endpoint;
- every denominator and squaring wall in (27);
- every monotonicity used to place a worst case at
  $y=1/(2\sqrt2)$ or $\kappa=32$;
- every gain, interface, threshold, and strict spectral wall;
- any limiting face used to infer a strict inequality on an open parameter
  interval.

### Energy and global-union faces

- $K=32/\varepsilon^2$ throughout (12);
- $K=K_0(7/8)$ and $K=550^2$;
- $K=64$, $2048$, $2400$, $3200$, $9600$, $12500$, $15000$, and
  $200000$ wherever their adjacent zones or sharper face theorems meet;
- exact ownership of every ratio and energy face in the six-zone union and
  the all-frequency endpoint.

## Do-not-claim rules

- Do not extrapolate any intermediate Round 13 estimate proved only for
  $\varepsilon\le1/10$ to the candidate domain.
- Do not use the desired Round 14 seam, endpoint bound, compact envelope, or
  $550^2$ ceiling as an input to its own proof.
- Do not let the clean-room reviewer inspect an incumbent proof, incumbent
  ledger, agent discussion, or any other Round 14 output before returning a
  separate verdict.
- Do not use the open compact, certification, uniformity, or final-target
  obligations as proved inputs.
- Do not infer a complete all-frequency endpoint beyond
  $\varepsilon=1/100$.
- Do not treat the failed $\kappa=24$ localization (26) as a disproof of a
  constant-$24$ theorem.
- Do not replace strict brackets by ordinary floors at integer walls.
- Do not use decimal signs, floating-point optimization, sampled
  monotonicity, or a finite sweep as proof.
- Do not call an exact rational ledger a Bessel-root certificate.
- Do not enumerate modes, roots, or cells toward $900^2$ or $550^2$ as a
  substitute for the analytic proof.
- Do not promote a bounded certificate-format pilot to global coverage.
- Do not claim (33) unless both the local seam (1), the independent endpoint
  (28), all shared faces, and the six-zone union have passed every gate.
- Do not claim the full shell Pólya theorem while any point of the exact
  compact residual remains open.

## Promotion boundary

Promotion may strengthen `SHELL-central-thin-seam-compression` and the
compact analytic envelope, and may lower the accepted all-ratio
high-frequency ceiling. It must leave `SHELL-rho-compact`,
`COMP-certified-bessel`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` open
until the complete compact residual is closed and fresh theorem-level audits
pass. The complete all-frequency endpoint remains exactly
$[99/100,1)$ unless a separate proof covers every frequency on a larger
interval.
