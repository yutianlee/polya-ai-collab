# Round 21 Aggregate-Tail Certificate Contract

Status: **FROZEN PROOF-FREE CONTRACT / NO REVIEW VERDICT**.

Baseline commit:
`a537991fd8d0418b8338388783f1a7462e0707f4`.

This contract fixes a theorem domain, mathematical postcondition, aggregate
reserve interface, outward-certificate predicates, authentication targets,
and falsification mutations. It contains no incumbent proof, executable
code, test implementation, certificate report prose, audit conclusion, or
diagnostic grid.

The paths and hashes marked sealed are authentication targets for A4. They
do not authorize A3 to open an incumbent route, executable artifact, or
report.

## 1. Contracted theorem

Put

$$
\rho_c=\frac1{1+2\pi},
\qquad
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The contracted aggregate theorem is exactly

$$
\boxed{
\rho_c\leq\rho\leq\frac{39}{50},
\qquad K\geq200}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<W(\rho,K).}
\tag{A1}
$$

Both ratio faces and the frequency face $K=200$ are included. The frequency
domain is unbounded above. The spectral count is the strict count below
$K^2$.

## 2. Exact aggregate interface

For $0\leq z\leq1$, set

$$
G_1(z)=\frac1\pi\left(\sqrt{1-z^2}-z\arccos z\right),
\qquad
\eta_\rho=G_1(\max\{\rho,1/2\}),
\qquad
d_\rho=\frac{2\arcsin\rho}{\pi}.
\tag{A2}
$$

Put

$$
\mu=\rho K,
\qquad
C=\frac{2\pi\rho K}{1-\rho},
\tag{A3}
$$

and, whenever $\mu>1/2$, write uniquely

$$
\mu-\frac12=J+\tau,
\qquad J\in\mathbb N_0,
\qquad 0\leq\tau<1.
\tag{A4}
$$

The number of low-interface tails and their starting points are

$$
R=\begin{cases}J,&\tau=0,\\J+1,&0<\tau<1,\end{cases}
\qquad x_r=r+\frac12\quad(0\leq r<R).
\tag{A5}
$$

With

$$
n_r=\lfloor\mu-x_r\rfloor,
\qquad q_r=x_r+n_r,
\tag{A6}
$$

the analytic reconstruction must establish

$$
\sum_{r=0}^{R-1}n_r=\frac{J(J+1)}2,
\qquad
\mu-q_r=\tau,
\tag{A7}
$$

and, for the accepted first-shelf length $p_r$,

$$
p_r<\sqrt{x_r^2+C}-x_r.
\tag{A8}
$$

Define

$$
\mathcal I(C,R)
=\frac12\left[
R\sqrt{R^2+C}
+C\operatorname{arsinh}\left(\frac R{\sqrt C}\right)-R^2
\right].
\tag{A9}
$$

The required strict aggregate predicates are

$$
\sum_{r=0}^{R-1}p_r<\mathcal I(C,R),
\qquad
\delta_\tau
\leq\frac{2\tau^{5/2}}{15\sqrt\mu},
\tag{A10}
$$

where $\delta_0=0$, and

$$
\begin{aligned}
\mathcal Q(\rho,K):={}&
R\lfloor K\eta_\rho\rfloor
+d_\rho\frac{J(J+1)}2
-(1+d_\rho)\mathcal I(C,R)\\
&-\frac{8R\tau^{5/2}}{15\sqrt\mu}.
\end{aligned}
\tag{A11}
$$

A3 must reconstruct, rather than assume, the implication

$$
\mathcal Q(\rho,K)\geq0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K),
\tag{A12}
$$

including $\tau=0$, every half-integer $\mu$ wall, every integer
$K\eta_\rho$ wall, all omitted high-interface tails, and the strictness
after aggregate summation.

## 3. Continuous reserve and frequency propagation

For $K\eta_\rho>1$, put

$$
b=\frac{2\pi\rho}{1-\rho},
\qquad
\overline R=\mu+\frac12,
\qquad
S=\sqrt{\overline R^2+bK},
\tag{A13}
$$

$$
\overline{\mathcal I}
=\frac12\left[
\overline R S
+bK\operatorname{arsinh}\left(\frac{\overline R}{\sqrt{bK}}\right)
-\overline R^2
\right],
\tag{A14}
$$

and define the exact continuous reserve

$$
\begin{aligned}
\mathcal B(\rho,K):={}&
\left(\mu-\frac12\right)(K\eta_\rho-1)
+\frac{d_\rho}{2}
\left(\mu-\frac32\right)\left(\mu-\frac12\right)\\
&-(1+d_\rho)\overline{\mathcal I}
-\frac{8(\mu+1/2)}{15\sqrt\mu}.
\end{aligned}
\tag{A15}
$$

The reconstruction obligation is the strict chain

$$
\mathcal B(\rho,K)\geq0
\quad\Longrightarrow\quad
\mathcal Q(\rho,K)>0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)<W(\rho,K).
\tag{A16}
$$

For fixed $\rho$ and variable $K$, A3 must derive the following frequency
identities analytically. A4 must independently check the displayed algebra
but must not treat a replay at one frequency as an all-frequency proof. With

$$
I(K)=\overline{\mathcal I},
\qquad
P=S-\overline R,
$$

one has

$$
I_K=\rho P
+\frac b2\operatorname{arsinh}
\left(\frac{\overline R}{\sqrt{bK}}\right),
\tag{A17}
$$

$$
I_{KK}
=\rho^2\left(\frac{\overline R}{S}-1\right)
+\frac{\rho b}{2S}
+\frac{b(2\rho K-1)}{8KS}.
\tag{A18}
$$

The exact first derivative of (A15) is

$$
\begin{aligned}
\mathcal B_K={}&
\rho(K\eta_\rho-1)
+(\mu-1/2)\eta_\rho
+d_\rho\rho(\mu-1)\\
&-(1+d_\rho)I_K
-\frac{2\rho(2\mu-1)}{15\mu^{3/2}}.
\end{aligned}
\tag{A19}
$$

Define

$$
E_{KK}=\frac{\rho^2(2\mu-3)}{15\mu^{5/2}},
\tag{A20}
$$

$$
\mathcal B_{KK}
=2\rho\eta_\rho+d_\rho\rho^2
-(1+d_\rho)I_{KK}+E_{KK},
\tag{A21}
$$

and

$$
F(\rho)=2\rho\eta_\rho+d_\rho\rho^2
-\frac{3(1+d_\rho)b}{800}.
\tag{A22}
$$

### 3.1 Finite base-face certificate

The finite outward boxes must prove on the rational superset
$7/51\leq\rho\leq39/50$, at the single base frequency $K=200$, that

$$
\mathcal B(\rho,200)>0,
\qquad
\mathcal B_K(\rho,200)>0,
\qquad
F(\rho)>0,
\tag{A23}
$$

together with the base guards and base consistency checks

$$
\mu_{200}:=200\rho>\frac32,
\quad 200\eta_\rho>1,
\quad S(\rho,200)>\overline R(\rho,200)>200\rho,
\tag{A24a}
$$

$$
I_{KK}(\rho,200)<\frac{3b}{800},
\quad E_{KK}(\rho,200)>0,
\quad \mathcal B_{KK}(\rho,200)>F(\rho).
\tag{A24b}
$$

The boxes also check $1-\rho>0$ and outward containment of every exact
rational endpoint. Equations (A24a)--(A24b) are consistency checks at
$K=200$ only. In particular, replaying
$I_{KK}(\rho,200)<3b/800$ or
$\mathcal B_{KK}(\rho,200)>F(\rho)$ cannot establish the unbounded-frequency
propagation below.

### 3.2 Universally quantified analytic obligation

Separately from the finite certificate, A3 must prove for every

$$
\frac7{51}\leq\rho\leq\frac{39}{50},
\qquad K\geq200,
\tag{A25}
$$

that all definitions in (A13)--(A22) are valid and that the propagated
guards

$$
1-\rho>0,
\quad \mu=\rho K>\frac32,
\quad K\eta_\rho>1,
\quad S>\overline R>\rho K
\tag{A26}
$$

hold. On the same universally quantified domain, A3 must derive

$$
I_{KK}
<\frac{3\rho b}{4S}
<\frac{3b}{4K}
\leq\frac{3b}{800},
\qquad
E_{KK}>0,
\tag{A27}
$$

and hence

$$
\mathcal B_{KK}
>2\rho\eta_\rho+d_\rho\rho^2
-\frac{3(1+d_\rho)b}{4K}
\geq F(\rho).
\tag{A28}
$$

The sign $F(\rho)>0$ is the finite predicate in (A23), not an additional
analytic conclusion and not a box check at variable $K$. Once A4 separately
validates (A23), equation (A28) supplies
$\mathcal B_{KK}(\rho,K)>F(\rho)>0$ for every $K\geq200$.

Finally A3 must derive the conditional propagation that combines the
separately validated base predicates (A23) with (A25)--(A28) by the two exact
integrations

$$
\mathcal B_K(\rho,K)
=\mathcal B_K(\rho,200)
+\int_{200}^{K}\mathcal B_{KK}(\rho,s)\,ds>0,
\tag{A29}
$$

$$
\mathcal B(\rho,K)
=\mathcal B(\rho,200)
+\int_{200}^{K}\mathcal B_K(\rho,s)\,ds>0
\tag{A30}
$$

for $K>200$, with (A23) owning $K=200$. A3 is responsible for the universal
inequalities and integration implications; A4 is responsible for the finite
premises in (A23). Equations (A26)--(A30), not the base consistency checks
(A24a)--(A24b), are the required unbounded-frequency step. No finite
frequency truncation is permitted.

## 4. Frozen outward-certificate schema

| field | frozen value |
|---|---|
| certified rational ratio superset | `[7/51,39/50]` |
| theorem ratio domain | `[rho_c,39/50]` |
| base frequency | `200` |
| midpoint precision | `192` bits |
| minimum permitted precision | `192` bits |
| maximum exact box width | `1/2000` |
| boxes on `[7/51,1/2]` | `726` |
| boxes on `[1/2,39/50]` | `560` |
| total exact rational boxes | `1286` |
| principal proof signs per box | $\mathcal B(\rho,200)>0$, $\mathcal B_K(\rho,200)>0$, $F(\rho)>0$ from (A23) |
| base guards per box | $1-\rho>0$, (A24a) |
| base consistency signs per box | (A24b), evaluated only at $K=200$ |
| all-$K\geq200$ propagation | analytic A3 obligations (A25)--(A30), not finite box predicates |
| standalone certificate digest | none emitted; identity is the exact schema plus authenticated artifact bytes |

Every rational box must be enclosed outward and must contain both exact
endpoints. The branch $\eta_\rho=G_1(1/2)$ owns the lower segment and
$\eta_\rho=G_1(\rho)$ owns the upper segment; both formulas must agree at
$\rho=1/2$. Exact consecutive endpoints must tile the entire rational
superset without a gap or overlap.

Every finite comparison in (A23)--(A24b) must be a certain Arb comparison.
The outward boxes make no proof decision at $K>200$. Binary floats and
decimal displays are excluded from hash gates, partitions, branches,
derivative decisions, signs, and theorem propagation.

## 5. Dependency identities

### A3-visible accepted foundations

| artifact | SHA-256 | contracted scope |
|---|---|---|
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` | accepted one-tail split, curvature, shelf, and interface bounds |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | strict dimension reduction and Weyl normalization |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated completeness, multiplicity, strict count |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | only the qualified trapezoidal-floor and interface integral statements |

### Sealed executable dependency

The verifier authenticates the following additional byte identity. A3 may
see this row but must not open the named file.

| artifact | bytes | SHA-256 |
|---|---:|---|
| `rounds/polya-main/round_021/exploration/aggregate-low-interface-route.md` | `8476` | `61f91d4c604afb2bb3a66d6eaddb9a8a83e01373d389c3126b84ca3cf8368da0` |

## 6. Sealed A4 authentication targets

The following rows expose byte identities only. A3 may authenticate the
strings recorded here but must not read the named files.

| role | artifact | bytes | SHA-256 |
|---|---|---:|---|
| verifier | `computations/round21_verify_aggregate_tail.py` | `12461` | `fc48425ccdfc05253c42645777fb36acbdf5fcba1cfd91483a836a1b10e9c952` |
| tests | `computations/tests/test_round21_verify_aggregate_tail.py` | `4165` | `50f10033e380b83e7cec8212c0213709676b4cca603570fb10b3974f0d89be91` |
| report | `rounds/polya-main/round_021/certification/aggregate-tail-global.md` | `7060` | `0ddd0c54942f7bd3bff3ec06271cb6bedea5a3a0b0185054f1a2ea33844eaeb6` |

An existing audit file is deliberately not named here. Review conclusions
are outside this proof-free contract.

## 7. Mandatory A4 falsification mutations

A4 must reject or detect each of the following independent mutations:

1. any foundational hash, sealed route byte, verifier byte, test byte, or
   report byte;
2. precision below 192 bits, a changed base frequency, ratio endpoint,
   split point, maximum width, or box count;
3. an outward ball that omits either exact rational endpoint;
4. a gap, overlap, reversed interval, or box crossing $\rho=1/2$ under the
   wrong $\eta_\rho$ branch;
5. disagreement of the two $\eta_\rho$ formulas at $\rho=1/2$;
6. any sign or factor change in (A15), (A17)--(A22);
7. omission of any finite predicate in (A23)--(A24b), or replacement of a
   strict certain sign by a midpoint, sample, or display decimal;
8. omission of $\tau=0$, a half-integer $\mu$ wall, or an integer
   $K\eta_\rho$ wall from the reconstruction of (A12) and (A16);
9. loss of strictness in (A10), (A12), or (A16);
10. omission or weakening of the universal quantifier in (A25), any guard
    in (A26), any inequality in (A27)--(A28), either integration in
    (A29)--(A30), or propagation only to a finite $K$ ceiling;
11. use of a binary float or decimal display in any authentication,
    partition, branch, derivative, sign, or proof decision.

## 8. Scope and nonclaims

This contract does not assert that its certificate bytes are valid and does
not prove (A1). A3 reconstructs the analytic implication, including the
universally quantified step (A25)--(A30). A4 independently authenticates and
replays the outward $K=200$ certificate, checks the derivative identities,
and confirms that its finite results are not promoted to an all-frequency
predicate. Neither role may infer a Round 21 subtraction, a successor
residual, or a project target from this contract alone.
