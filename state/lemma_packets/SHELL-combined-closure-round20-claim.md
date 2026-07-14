# Frozen Candidate Claim: Round 20 Combined Closure

Status: **FROZEN CLAIM ONLY / NOT PROVED / NOT PROMOTED**.

Round: 20.

Candidate baseline commit:
`56e8d71ad3df2da6ab47ab1fefb8d758e076c69b`.

This packet freezes only
three proposed theorem statements, their proposed constants and inventories,
the permitted input boundary, and the exact set subtraction. It contains no
Round 20 incumbent proof, zero-bound derivation, executable constant ledger,
sampled root, certificate, review conclusion, or judge decision.

The proposed high endpoint through `k_11` has a separately recorded
source-scope/adversarial pre-freeze gate. That audit is never a permitted
clean-room input and supplies none of the proposed zero bounds. The external
freeze authenticates these exact proof-free bytes and the permitted input
boundary.

## 1. Authenticated pre-candidate state

The exact accepted residual and its executable classification are fixed by
the following immutable artifacts.

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |

Only the packet and classifier above may be used for accepted set
bookkeeping. Their classification is not a spectral proof of any claim in
this packet.

## 2. Definitions and accepted residual

Retain

$$
\omega _0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
C_0=1+\frac{8\sqrt2}{15},
$$

$$
\rho_* = \frac{\omega _0}{1+2C_*},
\qquad
\rho_0=\frac1{\sqrt{337}},
\qquad
\rho_c=\frac1{1+2\pi},
\qquad
\sigma=\frac{3\omega _0}{4},
$$

$$
L(\rho)=\frac1{2\rho},
\qquad
d=\frac{\sqrt{337}}2,
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
$$

and

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{1}
$$

The inherited upper floor is the exact accepted function

$$
U(\rho)=\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega _0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\geq\frac56\right\}
\right),
\tag{2}
$$

with `K_0`, `H_0`, the `H_0=K_0` switch, and every branch face defined
exactly in the authenticated residual packet.

The strict spectral convention is

$$
N_D(A_{\rho,1},K^2)
=\#\{\lambda_j(A_{\rho,1}):\lambda_j<K^2\}.
\tag{3}
$$

The accepted live residual is

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
\tag{4}
$$

Every frequency inequality in (4) is strict. No accepted owner is to be
reconstructed or subtracted twice.

## 3. Candidate C20

An initial clean-room verdict must reconstruct or refute all three theorem
claims and the exact subtraction below.

### 3.1 Exact closure of the live lower residual

The proposed lower theorem is precisely

$$
\boxed{
(\rho,K)\in\mathcal D_{19}^{\rm low}}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K),}
\tag{5}
$$

where

$$
\boxed{
\begin{aligned}
\mathcal D_{19}^{\rm low}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}.
\end{aligned}}
\tag{6}
$$

Thus both lower components of (4), including the complete fiber at
`rho=rho_0`, are claimed. No lower residual is proposed to remain.

### 3.2 Closed high staircase through `k_11`

Conditioned on independent approval of the `k_11` zero obligations in
Section 5, the proposed closed staircase theorem is

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_{11}(\rho)}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{7}
$$

The accepted predecessor owns the closed band through `k_6`. The genuinely
new high addition is exactly

$$
\boxed{
\mathcal C_{20}^{\rm stair}
=\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K\leq k_{11}(\rho)\}.}
\tag{8}
$$

The five proposed new checkpoints are the closed upper faces `k_7`, `k_8`,
`k_9`, `k_10`, and `k_11`; the preceding face is excluded in each new
subband and owned by its predecessor.

### 3.3 All-frequency optical theorem

The proposed optical theorem is

$$
\boxed{
\frac{39}{50}\leq\rho<1,
\qquad K\geq0}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)\leq\mathcal W(\rho,K).}
\tag{9}
$$

At `K=0`, both sides in (9) are zero. For every `K>0`, the proposed
comparison is strict.

Inside the live post-staircase residual, the genuinely subtractable optical
piece is

$$
\boxed{
\mathcal C_{20}^{\rm opt}
=\left\{\frac{39}{50}\leq\rho<\frac78,
\ k_{11}(\rho)<K<U(\rho)\right\}.}
\tag{10}
$$

### 3.4 Exact proposed subtraction

A PASS must prove

$$
\rho_*<\rho_0<\sigma<\rho_c<\frac{39}{50}<\frac78,
\qquad
k_{11}(\rho)<U(\rho)
\quad(\rho_c\leq\rho<7/8),
\qquad
U(\rho)=K_0(\rho)
\quad\left(\rho_c\leq\rho<\frac{39}{50}\right),
\tag{11}
$$

with the exact face ownership below. It must then reproduce

$$
\boxed{
\mathcal D_{19}\setminus
\left(
\mathcal D_{19}^{\rm low}
\cup\mathcal C_{20}^{\rm stair}
\cup\mathcal C_{20}^{\rm opt}
\right)
=\mathcal D_{20},}
\tag{12}
$$

where

$$
\boxed{
\mathcal D_{20}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac{39}{50},
\quad k_{11}(\rho)<K<K_0(\rho)=U(\rho)
\right\}.}
\tag{13}
$$

Equations (11)--(13) are set-bookkeeping conclusions to prove from (4)--(10),
not permitted spectral inputs.

## 4. Proposed lower-route sublemmas and inventories

All statements in this section are reconstruction obligations, not supplied
lemmas.

### 4.1 Shifted-tail wedge

The proposed stronger local statement is

$$
\boxed{
0<\rho\leq\sigma,
\quad K>d,
\quad \rho K>\frac12}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{14}
$$

Its proposed discrete facts are

$$
\omega _0d>1,
\qquad
\left\lfloor\omega _0K\right\rfloor
-\left\lfloor\rho K-r-\frac12\right\rfloor\geq1
\tag{15}
$$

for every active low-interface tail, together with an interface remainder
strictly below `1/4`. The claimed consequence of (14) is all of the first
component of (6), plus

$$
\rho_0\leq\rho\leq\sigma,
\qquad d<K.
\tag{16}
$$

The corner `(rho_0,d)` is not in (16); its lower frequency face is already
owned.

### 4.2 Finite lower staircase through `sqrt(114)`

Put

$$
c_{42}=\frac{\sqrt{7073}}8,
\qquad
c_7=\sqrt{114}.
\tag{17}
$$

The proposed finite theorem is

$$
\boxed{
\rho_0<\rho<\rho_c,
\qquad d<K\leq\sqrt{114}}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{18}
$$

The proposed strict unit-ball zero obligations needed for this lower ledger
are

$$
j_{13/2,1}>10,
\qquad
j_{7/2,2}>\frac{81}{8},
\qquad
j_{3/2,3}>\frac{21}{2},
\tag{19}
$$

together with their same-radial-index angular propagation. The complete
proposed strict-count inventory is:

| frequency cell | proposed possible inventory | cap |
|---|---|---:|
| `d<K<=10`, `K<=3z_rho` | first `ell=0,...,5`; second `ell=0,1,2` | 45 |
| `d<K<=10`, `K>3z_rho` | preceding inventory plus `(0,3)` | 46 |
| `10<K<=81/8` | first `ell=0,...,6`; second `ell=0,1,2`; possible `(0,3)` | 59 |
| `81/8<K<=21/2` | preceding inventory plus `(3,2)` | 66 |
| `21/2<K<=c_42` | preceding inventory plus `(1,3)` | 69 |
| `c_42<K<=sqrt(114)` | preceding inventory plus `(4,2)` | 78 |

Every lower threshold in this table is open. The proposed exclusions are:
first modes `ell>=7`, second modes `ell>=5`, third modes `ell>=2`, and all
radial modes `n>=4` through the included face `K=sqrt(114)`.

### 4.3 Remaining lower frequencies

The proposed stronger remaining-frequency theorem is

$$
\boxed{
\sigma<\rho<\rho_c,
\qquad K>\sqrt{114}}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{20}
$$

It is proposed to split only the exact cell

$$
\mathcal B=\left\{\sigma<\rho<\rho_c,
\ K>\sqrt{114},
\ \rho K\geq\frac52,
\ K<\frac2{\omega _0}\right\}
\tag{21}
$$

from its complement. For the complement, define

$$
p=\lfloor\omega _0K\rfloor,
\qquad
m=\left\lfloor\rho K-\frac12\right\rfloor.
\tag{22}
$$

The proposed exhaustive floor assertion is that `m<=2p-1` fails only on
`mathcal B`, with half-integer interfaces assigned to the high side.

On `mathcal B`, put

$$
R=\frac{367}{20}.
\tag{23}
$$

The proposed strict-phase proxy caps are:

| `ell` | cap for the radial proxy |
|---:|---:|
| 0 | 6 |
| 1 | 5 |
| 2 | 5 |
| 3 | 4 |
| 4 | 4 |
| 5 | 3 |
| 6 | 3 |
| 7 | 3 |
| 8 | 2 |
| 9 | 2 |
| 10 | 1 |
| 11 | 1 |
| 12 | 1 |
| 13 | 1 |
| `ell>=14` | 0 |

With multiplicity `2ell+1`, the proposed total cap is exactly `395`.
Every floor wall `omega_0 K in Z`, every half-integer interface
`rho K in Z+1/2`, the face `rho K=5/2`, and the face `K=2/omega_0` is part
of the claim and must be assigned exactly.

## 5. Proposed high-staircase sublemmas and inventories

No Round 20 zero-bound card or exploration note is a permitted input. Every
zero assertion below must be reconstructed from the limited sources in
Section 7.

### 5.1 Channel comparisons and proposed zero obligations

For shell frequency `q_(ell,n)(rho)`, the reviewer must prove internally

$$
q_{\ell,n}^2\geq n^2z_\rho^2+\ell(\ell+1),
\qquad
q_{0,n}=nz_\rho,
\tag{24}
$$

$$
q_{\ell,n}^2\geq j_{\ell+1/2,n}^2,
\tag{25}
$$

and, for `p>=ell`,

$$
j_{p+1/2,n}^2
\geq j_{\ell+1/2,n}^2+p(p+1)-\ell(\ell+1).
\tag{26}
$$

The complete proposed new zero registry is

$$
\begin{gathered}
j_{3/2,2}>\frac{77}{10},
\qquad
j_{5/2,2}>9,
\qquad
j_{7/2,2}>\frac{103}{10},
\qquad
j_{11/2,2}>\frac{129}{10},\\
j_{3/2,3}>\frac{21}{2},
\qquad
j_{5/2,3}>\frac{61}{5},\\
j_{13/2,1}>10,
\qquad
j_{15/2,1}>\frac{23}{2},
\qquad
j_{17/2,1}>\frac{71}{6},\\
j_{19/2,1}>\frac{64}{5},
\qquad
j_{21/2,1}>\frac{69}{5}.
\end{gathered}
\tag{27}
$$

The bounds at radial index two or three, and the strengthenings
`j_(13/2,1)>10` and `j_(15/2,1)>23/2`, are internal reconstruction
obligations. Lorch may be used only at radial index one, through the general
strict inequalities printed in the qualified source card. Every
half-integer specialization, exact radical comparison, tangent-cell/root
enumeration, ODE simplicity step, and recurrence propagation remains to be
checked by the clean-room reviewer.

### 5.2 Nested proposed inventories

The following are the complete proposed maximal inventories at each included
checkpoint:

| included upper face | proposed possible inventory |
|---|---|
| `k_7` | first `ell=0,...,6`; second `ell=0,1`; no `n>=3` |
| `k_8` | first `ell=0,...,7`; second `ell=0,...,3`; no `n>=3` |
| `k_9` | first `ell=0,...,8`; second `ell=0,...,4`; no `n>=3` |
| `k_10` | first `ell=0,...,9`; second `ell=0,...,5`; third `ell=0,1`; no `n>=4` |
| `k_11` | first `ell=0,...,10`; second `ell=0,...,4`; third `ell=0,1`; no `n>=4` |

At `K=k_m`, the first mode in channel `ell=m` is excluded by the strict
count. No table may omit a full angular multiplicity `2ell+1`.

The proposed cap tables at the four largest checkpoints are as follows.

For `k_8`:

| first category | no second | `h=0` | `h=1` | `h=2` | `h=3` |
|---|---:|---:|---:|---:|---:|
| `H=7` | 64 | 65 | 68 | 73 | 80 |
| `H=6` | 49 | 50 | 53 | impossible | impossible |
| `H=5` | 36 | 37 | 40 | 45 | 52 |
| `H<=4` | 25 | 26 | 29 | 34 | 41 |

For `k_9`:

| first category | no second | `h=0` | `h=1` | `h=2` | `h=3` | `h=4` |
|---|---:|---:|---:|---:|---:|---:|
| `H=8` | 81 | impossible | impossible | impossible | impossible | impossible |
| `H=7` | 64 | 65 | 68 | 73 | impossible | impossible |
| `H=6` | 49 | 50 | 53 | 58 | 65 | 74 |
| `H=5` | 36 | 37 | 40 | 45 | 52 | 61 |
| `H<=4` | 25 | 26 | 29 | 34 | 41 | 50 |

For `k_10`:

| first category | radial category | cap |
|---|---|---:|
| `H=9` | no second or third | 100 |
| `H=8` | no second | 81 |
| `H=8` | `h<=3` | 97 |
| `H=7` | no second | 64 |
| `H=7` | `h<=3` | 80 |
| `H=7` | `h=4` | 89 |
| `H=7` | `h=5` | 100 |
| `H<=6` | `h<=4`, no third | 74 |
| `H<=6` | `h<=3`, third present | 69 |
| `H<=6` | `h=4`, third present | 78 |
| `H<=6` | `h=5`, no third | 85 |
| `H<=6` | `h=5`, third present | 89 |

For `k_11`:

| first category | radial category | cap |
|---|---|---:|
| `H=10` | no second or third | 121 |
| `H=9` | no second or third | 100 |
| `H=9` | second present, no third | 125 |
| `H=8` | no third | 106 |
| `H=8` | third present | 110 |
| `H<=7` | all allowed radial modes | 93 |

For the `k_7` checkpoint, the proposed cumulative first-mode caps are
`25,36,49`, and the two possible second modes add `1+3`.

### 5.3 Proposed localization and split registry

The reviewer must reconstruct every proposed incompatibility, not infer it
from a cap table. The finite registry to falsify includes

$$
\rho=\frac15,\frac3{10},\frac13,\frac38,\frac25,
\frac5{12},\frac37,\frac12,\frac{107}{200},
\frac8{15},\frac35,\frac{16}{25},\frac{13}{20},\frac23,
\tag{28}
$$

the third-mode ratios `rho=4/25,1/4`, the second-mode ratio `rho=7/20`,
and the algebraic splits

$$
z_\rho^2=16,
\qquad
z_\rho^2=\frac{68}{3},
\qquad
z_\rho^2=34.
\tag{29}
$$

In particular, the proposed `k_11` localizations are: a counted second mode
forces `rho<8/15`; a counted third mode forces `rho<1/4`; `H=10` excludes
all second and third modes; and `H=9` excludes every third mode. Equality at
each localization face must exclude the defining mode.

## 6. Proposed optical sublemmas and constants

Put

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\leq\varepsilon_0:=\frac{11}{50},
\qquad
a=\varepsilon K,
\tag{30}
$$

and freeze

$$
C_D=\frac{1382}{3125},
\qquad
c=\frac{1126}{625},
\qquad
q=\frac{106}{333}.
\tag{31}
$$

The two proposed optical pieces are both inclusive:

$$
0\leq a\leq\frac{c}{\varepsilon},
\qquad
a\geq\frac{c}{\varepsilon}.
\tag{32}
$$

For `a>pi`, write

$$
\frac a\pi=N+t,
\qquad N\geq1,
\qquad 0<t\leq1,
\tag{33}
$$

using `(N,t)=(m-1,1)` at `a=m pi`. The proposed exact product-deficit
sublemma is

$$
\boxed{D(a)>\frac{1382}{3125}a^2\qquad(a>\pi).}
\tag{34}
$$

The proposed exact endpoint reserves for the low and high screens are

$$
R_L=\frac{39569}{2772225000}>0,
\qquad
R_H=\frac{14817541}{472867032960000}>0.
\tag{35}
$$

The clean-room reviewer must reconstruct the strict product comparison on
the low piece, the complementary-action/layer-cake comparison on the high
piece, and their common ownership of `a=c/epsilon`. It may not extrapolate
the accepted Round 16 theorem beyond `epsilon=1/8`; every estimate whose
sign depends on `epsilon<=11/50` must be re-established.

## 7. Permitted inputs and source-scope boundary

Before its initial verdict, an isolated reviewer may receive only this
hash-authenticated candidate, the five residual artifacts in Section 1,
and the following hash-authenticated foundational packets or source cards:

| permitted artifact | SHA-256 | permitted scope |
|---|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum, multiplicity, strict count |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | strict phase proxies in their proved scope |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | strict multiplicity-to-tail identities and notation |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` | audited pre-threshold shifted-tail split only |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` | accepted product/action identities; no enlarged-ratio conclusion |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | quoted turning and convex-floor statements only |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` | quoted shifted-tail theorem and equality scope |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` | qualified general first-zero inequalities `(L1)-(L2)` only |
| `sources/shell_weyl_bessel.md` | `ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade` | quoted structural DLMF identities only |
| `sources/bessel_phase_enclosures.md` | `e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c` | quoted phase/DLMF identities only |

For the internal half-integer reconstructions in (27), the reviewer may
consult only the labelled primary identities DLMF 10.47.3, DLMF 10.49(i),
and DLMF 10.51.1--10.51.2. These references authorize the spherical-Bessel
identification, explicit half-integer formulas, and the standard recurrence
identities; they authorize no zero location. The exact URLs are
`https://dlmf.nist.gov/10.47.E3`, `https://dlmf.nist.gov/10.49.i`,
`https://dlmf.nist.gov/10.51.E1`, and `https://dlmf.nist.gov/10.51.E2`.

The reviewer may also use elementary one-dimensional Dirichlet
Sturm--Liouville theory, Hardy's inequality, variational min--max, extension
by zero for `H_0^1`, ODE uniqueness, exact rational arithmetic, and
independently proved rational enclosures for `pi` and displayed radicals.

The Lorch statements apply only to first positive zeros of `J_nu`. They do
not supply any higher radial zero, shell cross-product zero, angular
propagation, shell-to-ball comparison, multiplicity cap, Weyl payment, or
endpoint assignment. All such steps must be internal.

No Round 20 exploration note, Round 20 zero-bound card, Round 19 internal
zero derivation, incumbent response, source-proof note, constant ledger,
script, sampled computation, audit, repository diff, cross-review, or judge
draft is permitted before the initial verdict.

## 8. Isolation rule and mandatory falsification faces

The first reviewer must verify the released candidate hash before reading
it and must return `PASS` or `FAIL` with the first unsupported implication.
A PASS requires independent reconstruction of (5), (7), (9), (11), and
(12), not agreement with an inventory or another agent.

The initial reconstruction must explicitly test all of the following.

1. Ratio and inherited-owner faces:
   `rho=rho_*`, `rho_0`, `sigma`, `rho_c`, `39/50`, `7/8`, `1`, the
   `H_0=K_0` interface, `rho=omega_0`, `1/2`, and `5/6`, with both
   one-sided traces at every interior face.
2. Lower frequency faces: `K=L(rho)`, `d`, `3z_rho`, `10`, `81/8`,
   `21/2`, `sqrt(7073)/8`, `sqrt(114)`, `2/omega_0`, and `U(rho)`;
   include every ordering change between a moving and fixed wall.
3. High frequency faces: `K=z_rho`, every `k_m` for `m=6,...,11`, every
   rational zero wall in (27), every ratio and algebraic split in
   (28)--(29), and `K=U(rho)`.
4. Optical faces: `K=0`, `a=pi`, every `a=m pi`, every product angular
   equality, every phase-proxy integer wall, `a=c/epsilon`, and
   `epsilon=11/50`.
5. Radial indices `n=1,2,3,4` and angular indices at least
   `ell=0,...,11`, with all multiplicities, all possible cross-channel
   coincidences, and a proof that every remaining index is absent.
6. Every tangent half-period and endpoint used to reconstruct (27), the
   exact enumeration of the relevant positive zero, the positive-zero
   convention, and the strict direction at the rational wall.
7. The form domains and inequality direction in (24)--(26), including
   preservation of angular channel and radial index.
8. Every cap in Sections 4--5, every impossible cap cell, and every fixed
   or moving Weyl payment on both sides of each split. A finite inventory
   without a uniform payment is not a proof.
9. The floor cells in (21)--(22), both conventions at
   `rho K in Z+1/2`, strictness after tail aggregation, the complete
   cap-395 proxy, and all omitted angular tails.
10. All signs in (34)--(35), monotonicity in `epsilon`, the full angular
    ceiling error and radial deficit on the high optical piece, and the
    common optical face.
11. The exact containment `k_11<U`, the identity `U=K_0` on
    `rho_c<=rho<39/50`, every strict or inclusive face in (6), (8), (10),
    and (13), and the exact set subtraction with no second subtraction of
    the already absorbed boxes `B_0` and `B_1`.

## 9. Nonclaim and release conditions

No assertion is made on the proposed residual (13). In particular, this
candidate does not prove the full shell Polya conjecture.

No proposed internal zero bound is certified merely by appearing in (27),
and no numerical experiment may be called a proof. The isolated analytic
reconstruction, independent exact-constant audit, cross-comparison,
adversarial referee review, judge decision, and State Patch audit all remain
required.

Until the first two release conditions are satisfied and an external freeze
records this file's exact SHA-256, the bytes are a draft and may be corrected
without constituting a replacement frozen candidate.
