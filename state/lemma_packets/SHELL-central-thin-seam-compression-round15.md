# Lemma Packet: Round 15 Central--Thin Seam Extension

Prepared after the accepted Round 14 State Patch. This packet is the only
input permitted to the strictly isolated clean-room reviewer before that
reviewer returns a verdict. Every Round 15 statement below is **UNPROVED**
unless it is explicitly listed as an accepted pre-Round-15 input.

The incumbent response, exploratory calculations, executable ledger,
clean-room response, adversarial review, and judge file must not be inserted
into or used to amend this packet after its SHA-256 hash is frozen.

## Accepted boundary before Round 15

Let

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
$$

The strict shell Pólya inequality is already proved at every frequency on

$$
0<\rho\le\rho_*,
\qquad
\frac{99}{100}\le\rho<1.
\tag{A1}
$$

The following high-frequency seam theorems, including their equality
faces, are accepted only on their exact displayed domains:

$$
0<\varepsilon\le\frac18,
\qquad
K\ge\frac{32}{\varepsilon^2},
\tag{A2}
$$

$$
0<\varepsilon\le\frac1{10},
\qquad
K\ge\frac{24}{\varepsilon^2},
\tag{A3}
$$

and

$$
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}.
\tag{A4}
$$

Round 14 separately proved

$$
K_0(7/8)<550^2
\tag{A5}
$$

and consequently

$$
0<\rho<1,
\qquad
K\ge550^2.
\tag{A6}
$$

The complete all-frequency thin endpoint remains exactly
$[99/100,1)$. The full theorem remains open on the true nonrectangular
compact residual

$$
\mathcal D_{14}
=(I_{14}\times[0,\infty))\setminus\mathcal A_{14},
\qquad
I_{14}=[\rho_*,99/100],
\tag{A7}
$$

where $\mathcal A_{14}$ contains the complete accepted analytic cover and
all owned threshold faces. It is forbidden to replace $\mathcal D_{14}$ by
$I_{14}\times[0,550^2)$.

## Frozen Round 15 local claim: unproved

Put $\rho=1-\varepsilon$. The primary claim to prove or falsify is

$$
\boxed{
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{T1}
$$

Threshold equality $K=54/\varepsilon^2$ is part of the claim. The genuinely
new open-sided slab is

$$
\frac18<\varepsilon\le\frac16,
\qquad
\frac56\le\rho<\frac78.
\tag{T2}
$$

The face $\varepsilon=1/8$, equivalently $\rho=7/8$, is already owned by
(A2) and must be retained as a closed overlap face. On every overlap, use
(A4), then (A3), then (A2), before the weaker target (T1).

The logically independent endpoint target is

$$
\boxed{K_0(5/6)<295^2=87025.}
\tag{T3}
$$

Neither (T1) nor (T3) may be used to prove the other. Both are unproved.

## Exact definitions supplied to the isolated reviewer

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
\tag{D1}
$$

Write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1).
\tag{D2}
$$

For $n\ge1$, define

$$
h_j=\left\lfloor A(x_0+j)+\frac14\right\rfloor.
\tag{D3}
$$

If the first drop occurs after index $p$, let

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
\tag{D4}
$$

For the degenerate head $n=0$, use $p=m=R=0$. The wall $R=0$ belongs to
the safe branch; only $R>0$ requires a new plateau-loss cap.

Scale by

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
\tag{D5}
$$

The target domain is exactly

$$
0<y\le\frac1{\sqrt6},
\qquad
\rho=1-y^2\ge\frac56,
\qquad
\kappa\ge54.
\tag{D6}
$$

In the dangerous branch,

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{D7}
$$

Define the actual self-consistency quantities

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
a=\frac{y^2}{\rho},
\qquad
\widehat q=a(Q-1).
\tag{D8}
$$

The candidate synthetic majorant corresponding to $d>5/8$ is

$$
S_*(P,r)=P+\frac85(P-r)=\frac{13P-8r}{5},
\tag{D9}
$$

with

$$
Q_*(P,r)=1+\frac{y^2}{\kappa}
 +\frac{yS_*(P,r)}{\kappa},
\qquad
q_*(P,r)=a\bigl(Q_*(P,r)-1\bigr),
\tag{D10}
$$

and

$$
H(P,r)=\frac{2\pi^2Q_*(P,r)}{(1-q_*(P,r))^2}.
\tag{D11}
$$

Equations (D9)--(D11) are definitions, not proved comparisons. A proof must
establish $S\le S_*$, the actual-to-synthetic implication $P^2<H(P,r)$,
and positivity of every denominator on the complete path.

## Permitted proved inputs for the local claim

The isolated proof may use only the following promoted inputs.

1. `CONV-strict-counting`, the exact separated shell spectrum from
   `SHELL-sturm-liouville-completeness`, `SHELL-phase-enclosures`, the
   strict-to-ordinary-floor transfer, `SHELL-weighted-lattice-scaffold`,
   and `SHELL-high-angular-shifted-tails`, only as stated in those
   obligations.
2. With

   $$
   b_\ell=
   \left\lfloor A\!\left(\ell+\frac12\right)+\frac14\right\rfloor,
   \qquad
   \mathcal T_{r_0}=b_{r_0}+2\sum_{\ell>r_0}b_\ell,
   $$

   the audited pre-threshold low-interface decomposition

   $$
   \frac{\mathcal T_{r_0}}2
   \le
   \int_{x_0}^K A(z)\,dz+\delta-\frac M4,
   \tag{P1}
   $$

   where

   $$
   M=\lfloor K\eta\rfloor-R,
   \qquad
   \delta=\int_q^\mu G_\mu(z)\,dz,
   \qquad
   0\le\delta<\frac{2\sqrt2}{15},
   \tag{P2}
   $$

   together with the unconditional shelf estimate

   $$
   p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
   \tag{P3}
   $$
3. The exact action identity

   $$
   \eta=G_1(1-\varepsilon)
   =\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv,
   \tag{P4}
   $$

   and the elementary inequality
   $\arccos(1-v)\ge\sqrt{2v}$, provided every resulting constant is
   reconstructed on (D6).

The accepted seam theorems (A2)--(A4), the fixed-ratio theorem, and the
endpoint results may be used only for overlap ownership, (T3), and the
prospective global union. No intermediate estimate from a previous seam
proof may be extrapolated into (D6).

For (T3), the permitted fixed-ratio theorem is: with

$$
a_\rho=\frac{2\pi\rho}{1-\rho},
\qquad
\eta_\rho=G_1(\max\{\rho,1/2\}),
\qquad
C_0=1+\frac{8\sqrt2}{15},
$$

the shell theorem holds for $K\ge K_0(\rho)$, where

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
     {2\eta_\rho}
\right)^2.
\tag{P5}
$$

The already-audited monotonicity of $K_0$ on the central interval is also
permitted.

## Preliminary exact screen: navigation only

Every statement in this section is a candidate to reconstruct, not a
permitted lemma.

The proposed constants are

$$
d_0=\frac58,
\qquad
\overline q=\frac{159}{400},
\qquad
B=\frac{14}{3},
\tag{S1}
$$

with shelf factor

$$
\sqrt{2\pi\rho}<\frac{13}{5},
\qquad
p<\frac{13}{5}\sqrt{\frac K\varepsilon}.
\tag{S2}
$$

### Angular, displacement, and localization screen

The exact angular route begins with

$$
2-\left(\frac75\right)^2=\frac1{25}>0,
\qquad
\left(\frac79\right)^2-\frac35=\frac2{405}>0,
\tag{S3}
$$

and is intended to prove

$$
\cos\frac{3\pi}{16}<\frac56,
\qquad
d>\frac58
\quad(\rho\ge5/6).
\tag{S4}
$$

The radical proxy and reserve are

$$
\left(\frac{763}{5000}\right)^2-\frac{1571}{67500}
=\frac{8563}{675000000}>0.
\tag{S5}
$$

At $y^2=1/6$, $\rho=5/6$, and $\kappa=54$, the proposed displacement
proxy is

$$
\frac1{1620}+\frac{13}{5}\frac{763}{5000}
=\frac{804689}{2025000},
\tag{S6}
$$

with reserve

$$
\frac{159}{400}-\frac{804689}{2025000}
=\frac{497}{4050000}>0.
\tag{S7}
$$

If uniformly reconstructed before any outer-slope use, this gives

$$
\frac{x_0}{K}>
\frac56\left(1-\frac{159}{400}\right)
=\frac{241}{480}
=\frac12+\frac1{480}.
\tag{S8}
$$

### Complete synthetic-path screen

The endpoint bounds

$$
y<\frac{49}{120},
\qquad
\left(\frac{49}{120}\right)^2-\frac16
=\frac1{14400}>0,
\tag{S9}
$$

and

$$
6-\left(\frac{120}{49}\right)^2
=\frac6{2401}>0
\tag{S10}
$$

suggest

$$
a\le\frac15,
\qquad
\frac{\partial Q_*}{\partial P}
=\frac{13y}{5\kappa}
<\frac{637}{32400}.
\tag{S11}
$$

The proposed complete fixed-$r=B$ derivative cap is

$$
\frac{\partial H}{\partial P}
<2\left(\frac{1571}{500}\right)^2
\frac{637}{32400}
\frac{1+159/400+2/5}{(1-159/400)^3}
=\frac{2260740364246}{708624500625}
<\frac{16}{5},
\tag{S12}
$$

with exact reserve

$$
\frac{16}{5}
-\frac{2260740364246}{708624500625}
=\frac{6858037754}{708624500625}>0.
\tag{S13}
$$

The candidate lower slope is

$$
\frac d{dP}\bigl(P^2-H(P,B)\bigr)
>2B-\frac{16}{5}=\frac{92}{15}>0.
\tag{S14}
$$

At $P=r=B$, the screen gives

$$
Q_*(B,B)<\frac{10093}{9720},
\qquad
q_*(B,B)<\frac{373}{48600},
\tag{S15}
$$

and

$$
B^2-H(B,B)>
B^2-2\left(\frac{1571}{500}\right)^2
\frac{10093/9720}{(1-373/48600)^2}
=\frac{2505132463469}{2616573970125}>0.
\tag{S16}
$$

The proof must establish the entire path, not just (S16).

### Gain and payment screen

The proposed action gain is

$$
K\eta>
\frac{280000}{17281}\frac1y,
\qquad
\frac{280000}{17281}-B
=\frac{598066}{51843}>0.
\tag{S17}
$$

Using $1/y>120/49$, the proposed dangerous-branch payment reserve is

$$
\left(\frac{598066}{51843}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{80132733}{3024175}>0,
\tag{S18}
$$

and the safe-branch reserve is

$$
\left(\frac{280000}{17281}\right)\frac{120}{49}
-1-\frac{132}{175}
=\frac{114694733}{3024175}>0.
\tag{S19}
$$

The proof must derive the gain, own the full possible floor loss, and close
$R>0$ and $R\le0$ separately.

## Independent central-endpoint screen: unproved

At $\rho=5/6$,

$$
a_\rho=10\pi.
$$

The candidate exact route uses

$$
10\pi<\frac{220}{7}<36,
\qquad
36-\frac{220}{7}=\frac{32}{7}>0,
\qquad
\sqrt{a_\rho}<6,
\tag{E1}
$$

$$
\sqrt3<\frac{97}{56},
\qquad
\left(\frac{97}{56}\right)^2-3
=\frac1{3136}>0,
\tag{E2}
$$

and

$$
49-9\left(\frac{1571}{500}\right)
\left(\frac{97}{56}\right)
=\frac{517}{28000}>0,
\tag{E3}
$$

which is intended to prove $\eta_{5/6}>1/49$. Together with
$C_0<307/175$, the proposed $Y=295$ comparison is

$$
\frac1{49}(295)^2-6(295)-\frac{307}{175}
=\frac{5226}{1225}>0.
\tag{E4}
$$

A proof must derive (E1)--(E4) exactly and explain why positivity at $Y=295$
places the unique positive root of

$$
\eta_{5/6}X^2-\sqrt{a_{5/6}}X-C_0=0
$$

strictly below $295$, yielding (T3).

## Exact route obstructions: not counterexamples

The current displacement/localization majorant does not close with
$\kappa=53$. Indeed, from $\pi>333/106$,

$$
\frac{333}{14045}
-\left(\frac{3079}{20000}\right)^2
=\frac{10003031}{1123600000000}>0,
$$

so

$$
\sqrt{\frac{2\pi}{265}}>\frac{3079}{20000},
$$

and

$$
\frac1{1590}+\frac{13}{5}\frac{3079}{20000}
=\frac25+\frac{14293}{15900000}>\frac25.
\tag{O1}
$$

This is only the first obstruction in this selected route. It is not a
counterexample to the shell inequality and does not disprove a theorem with
constant $53$.

Likewise, the selected central proxies do not certify $Y=294$, because

$$
\frac1{49}(294)^2-6(294)-\frac{307}{175}
=-\frac{307}{175}<0.
\tag{O2}
$$

This does not prove $K_0(5/6)\ge294^2$ and is not a spectral
counterexample.

## Prospective seven-zone union: unproved

Only if (T1) and (T3) are proved and every shared-face and union gate passes
may the accepted envelope be refined to:

1. $[\rho_*,1/16]$: $K<64$;
2. $[1/16,5/6]$: $K<K_0(5/6)<87025$;
3. $[5/6,7/8]$: $K<54/(1-\rho)^2\le3456$;
4. $[7/8,9/10]$: $K<32/(1-\rho)^2\le3200$;
5. $[9/10,19/20]$: $K<24/(1-\rho)^2\le9600$;
6. $[19/20,24/25]$: $K<24/(1-\rho)^2\le15000$;
7. $[24/25,99/100]$: $K<20/(1-\rho)^2\le200000$.

The complete all-frequency endpoint would remain exactly $[99/100,1)$.
The prospective all-ratio high-frequency ceiling would be

$$
\boxed{K\ge200000},
\tag{G1}
$$

because the retained far-thin Round 10 zone dominates. The exact reduction
from the accepted Round 14 ceiling would be

$$
\frac{550^2}{200000}=\frac{121}{80}>1.
\tag{G2}
$$

The order $3456,3200$ in adjacent zones is intentional: (A2) is sharper at
and beyond $\rho=7/8$. These closed zones are only coarse enclosures of the
exact complement and are not a rectangular certification target.

## Required new analytic work

A proof of (T1) must, without citing any Round 15 screen as a lemma:

1. derive $d>5/8$ uniformly, including $\varepsilon=1/6$;
2. derive (S2) and dangerous localization beyond $K/2$ before using any
   outer-region slope;
3. reconstruct the ordinary-floor implication and strict self-consistency
   inequality, with every denominator, radicand, and squaring sign positive;
4. prove $\widehat q<159/400$ uniformly;
5. prove $S\le S_*$ and control the complete fixed-$r=B$ path, including
   its initial endpoint and every intermediate point;
6. prove $R<B/\sqrt\varepsilon$ and then pay the full possible floor loss
   separately for $R>0$ and $R\le0$;
7. close the no-drop, immediate-drop, degenerate-head, $R=0$, and first
   $R>0$ branches;
8. own every ordinary-floor, gain, interface, angular-cutoff, threshold,
   and strict spectral wall;
9. include threshold equality throughout (D6);
10. provide an executable exact rational or algebraic ledger reproducing
    every finite comparison.

No decimal sampling, numerical optimizer, finite sweep, or agent consensus
proves any item above.

## Mandatory branches, walls, and falsification faces

Every incumbent proof, clean-room reconstruction, exact ledger, and
adversarial review must explicitly own:

- $p=n$, $p=0$, $n=0$, $R=0$ from both sides, and the first $R>0$ branch;
- $\mu-x_0\in\mathbb Z$ and both adjacent $\beta$ cells, $q=\mu$,
  $x_0=\mu$, and the angular cutoff $\nu=K$;
- every ordinary-floor wall, coarse-proxy wall, gain wall
  $K\eta\in\mathbb Z$, denominator wall, radicand wall, and squaring wall;
- the complete fixed-$r=B$ synthetic path and every monotonicity placing a
  worst case at $y=1/\sqrt6$ or $\kappa=54$;
- $\varepsilon=1/100$, $1/25$, $1/20$, $1/10$, $1/8$, and $1/6$;
- $\kappa=20$, $24$, and $32$ only on their accepted domains, and
  $\kappa=54$ on (D6);
- the exact $\kappa=53$ route obstruction, without turning it into an
  impossibility claim;
- $\rho=\rho_*$ and $1/16$ from both adjacent analytic regimes;
- $\rho=5/6$, $7/8$, $9/10$, $19/20$, $24/25$, and $99/100$ from both
  adjacent regimes, using the sharpest accepted theorem on overlaps;
- $K=54/\varepsilon^2$, $K=64$, $1944$, $2048$, $2400$, $3200$, $3456$,
  $9600$, $12500$, $15000$, $87025$, and $200000$ wherever adjacent zones
  or sharper face theorems meet;
- $K=K_0(5/6)$, $K=294^2$, and $K=295^2$;
- exact ownership of every ratio and energy face in the prospective union
  and the unchanged endpoint (A1).

## Isolation and review protocol

- The incumbent author may use this packet and accepted repository inputs,
  but must rederive every enlarged-domain estimate.
- The constant-inventory author independently reconstructs every finite
  comparison and provides a standalone exact ledger and focused tests.
- The clean-room reviewer receives only this frozen packet before returning
  a verdict. Before that verdict, the reviewer must not inspect the
  incumbent response, incumbent ledger, exploration notes, other Round 15
  messages, adversarial report, or judge draft.
- The adversarial reviewer begins from the assumption that (T1) is false,
  audits the incumbent and clean-room proofs separately, and identifies the
  first unsupported implication, if any.
- One lead synthesizer may reconcile the artifacts only after the isolated
  verdict exists. Consensus is not verification.

## Do-not-claim rules

- Do not extrapolate any Round 14 intermediate inequality beyond
  $\varepsilon=1/8$ or below $\kappa=32$.
- Do not promote $\kappa=53$ or $Y=294$ from the present screen.
- Do not call an exact rational ledger a Bessel-root certificate.
- Do not enumerate modes, roots, or cells toward $550^2$, $295^2$, or
  $200000$ as a substitute for the analytic proof.
- Do not enlarge the complete all-frequency endpoint below $99/100$.
- Do not claim the seven-zone envelope or $K\ge200000$ unless both (T1),
  (T3), and every closed face pass all gates.
- Do not claim the full shell theorem while any point of the exact compact
  residual remains open.

## Promotion boundary

Promote (T1) and (T3) only if every domain estimate, exceptional branch,
strict wall, overlap face, denominator, radicand, squaring, synthetic-path
point, payment branch, endpoint comparison, and union face closes exactly;
a strictly isolated reconstruction passes; a fresh adversarial audit passes;
and an executable exact ledger reproduces every finite comparison.

Promotion may strengthen `SHELL-central-thin-seam-compression` and
`SHELL-rho-compact-analytic-envelope`. It must keep `SHELL-rho-compact`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` `open`, and must keep
`COMP-certified-bessel` `diagnostic_only`, until the exact compact residual
is closed and fresh theorem-level audits pass.
