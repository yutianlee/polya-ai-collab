# Lemma Packet: Exact Round 18 Post-Promotion Residual Mask

Status: **FROZEN RESIDUAL MAP / NO NEW THEOREM**.

Round: 18.

Primary obligations: **SHELL-rho-compact** and
**COMP-certified-bessel**.

Baseline commit:
`1caf24a0f0732038e9d162990dd3c2201daad85d`.

This packet freezes the exact accepted state after the Round 17 State Patch
and before any Round 18 candidate proof. It records accepted set arithmetic,
face ownership, and one already proved method obstruction. It does not prove
that the residual is empty, propose a new spectral threshold, or turn a mask
classification into a theorem.

## 1. Inherited constants and upper floor

Retain the frozen Round 17 definitions

$$
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
C_0=1+\frac{8\sqrt2}{15},
$$

$$
\rho_*=\frac{\omega_0}{1+2C_*},
\qquad
I_{17}=\left[\rho_*,\frac78\right].
$$

For $0<\rho<1$, let

$$
a_\rho=\frac{2\pi\rho}{1-\rho},
\qquad
\eta_\rho=G_1\!\left(\max\left\{\rho,\frac12\right\}\right),
$$

$$
K_0(\rho)=
\left(
\frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
{2\eta_\rho}
\right)^2,
\qquad
H_0(\rho)=\frac{C_*}{\omega_0-\rho}\quad(\rho<\omega_0).
$$

The exact accepted upper floor is

$$
U(\rho)=
\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right).
\tag{1}
$$

Let $\rho_{HK}$ be the unique accepted root in

$$
\frac{9407}{100000}<\rho_{HK}<\frac{94071}{1000000}
$$

of

$$
P(\rho)
=(1-\rho)\left(C_0\rho-\frac{\omega_0}{2}\right)^2
-2\pi C_*\rho(\omega_0-\rho)=0.
\tag{2}
$$

The frozen uniqueness and sign proof gives

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\le\rho<7/8.
\end{cases}
\tag{3}
$$

At $\rho_{HK}$ the first two values agree. The upper face $K=U(\rho)$
is included in old analytic coverage and excluded from every residual.

## 2. Promoted Round 17 band

Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
\tag{4}
$$

The accepted closed theorem band is

$$
\overline{\mathcal C}_{17}
=\left\{(\rho,K):
\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_2(\rho)
\right\}.
\tag{5}
$$

Its genuinely new part relative to the old mask is

$$
\mathcal C_{17}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad z_\rho<K\le k_2(\rho)
\right\}.
\tag{6}
$$

The excluded lower face $K=z_\rho$ has the old phase-zero owner; at
$\rho=\rho_c$ its point also lies on the old high-angular face. The excluded
vertical face $\rho=7/8$ has the complete Round 16 endpoint owner. The upper
face $K=k_2(\rho)$ is included and is owned by the promoted first-angular-band
theorem under strict spectral counting.

## 3. Exact analytic predicate

Let $\mathcal A_{16}$ be exactly the primitive accepted union in the frozen
Round 17 packet and executable classifier. No Round 16 branch is rewritten
or dropped here. The accepted post-promotion analytic cover is

$$
\boxed{
\mathcal A_{17}
=\mathcal A_{16}\cup\overline{\mathcal C}_{17}.
}
\tag{7}
$$

Symbolically, on rational query points with $K\ge0$,

~~~text
in_A17 =
    in_A16_frozen
    or (
        rho >= rho_c
        and rho <= 7/8
        and (1-rho)*K >= pi
        and (1-rho)^2*K^2 <= pi^2 + 6*(1-rho)^2
    )
~~~

Every displayed equality in the added disjunct is included. The executable
Round 18 classifier imports the hash-locked Round 17 implementation and
performs exactly this union; it does not reconstruct `in_A16` from prose.

The exact analytic residual is

$$
\mathcal D_{17}
=\left(I_{17}\times[0,\infty)\right)\setminus\mathcal A_{17}
=\mathcal D_{16}\setminus\mathcal C_{17}.
\tag{8}
$$

## 4. Normalized two-piece residual

Since the old lower wall is $1/(2\rho)$ below $\rho_c$, the two old lower
walls agree at $\rho_c$, and the promoted band owns through $k_2$ at and
above $\rho_c$, exact subtraction gives

$$
\boxed{
\begin{aligned}
\mathcal D_{17}
={}&\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)
\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
\tag{9}
$$

All four displayed frequency inequalities in (9) are strict. In
particular:

- $\rho=\rho_c$ belongs to the second ratio piece, never the first;
- $K=1/(2\rho)$ and $K=k_2(\rho)$ are analytically covered faces;
- $K=U(\rho)$ is an analytically covered face;
- $\rho=\rho_*$ and $\rho=7/8$ are complete old endpoint faces.

The classifier evaluates (9) independently of the union predicate and
fails if two certified decisions disagree.

## 5. Classifier and interval policy

`computations/round18_residual_mask.py` composes the accepted Round 17
classifier with (5) and separately evaluates (9). Exact rational arithmetic
owns rational faces. Comparisons with $\pi$, $\rho_*$, $\rho_c$, $H_0$,
$K_0$, $k_2$, and $\rho_{HK}$ use Arb at 128, 256, 512, 1024, and 2048
bits. A material sign not separated at the final precision returns
**indeterminate**.

A false factor may settle a conjunction without resolving irrelevant signs,
and a certified-true analytic disjunct may settle a union. An unresolved
mandatory compact-interval gate can never be overridden. Near the implicit
$H_0=K_0$ switch, both upper values are checked; membership is reported only
when the side of their minimum is certified. No ball midpoint is treated as
an exact constant.

The focused suite tests symbolic zero signs on every new face and constructs
4096-bit dyadic approximations to the $\rho_*$, $\rho_c$, $z_\rho$, $k_2$,
and $K_0$ faces. All remain indeterminate at the classifier's lower maximum
precision rather than being coerced to a Boolean answer.

## 6. Certified boxes are analytically subsumed

Retain the two independently valid closed certificates

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right],
$$

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{168}{25},\frac{673}{100}\right].
$$

First,

$$
\rho_c<\frac17<\frac{999}{2000}
<\frac{1001}{2000}<\frac78.
\tag{10}
$$

Both $z_\rho$ and $k_2(\rho)$ increase with $\rho$. Using $\pi<22/7$,
the largest lower wall on either box satisfies

$$
\max z_\rho
<\frac{44000}{6993}
=\frac{67}{10}-\frac{28531}{69930}
<\frac{67}{10}.
\tag{11}
$$

Using $\pi>157/50$, the smallest upper wall satisfies the accepted exact
reserves

$$
\min k_2^2-\left(\frac{168}{25}\right)^2
>
\left(\frac{6280}{1001}\right)^2+6
-\left(\frac{168}{25}\right)^2
=\frac{126027526}{626250625}>0,
\tag{12}
$$

and

$$
\min k_2^2-\left(\frac{673}{100}\right)^2
>
\left(\frac{6280}{1001}\right)^2+6
-\left(\frac{673}{100}\right)^2
=\frac{668749071}{10020010000}>0.
\tag{13}
$$

All square-root quantities are positive. Equations (10)--(13) control the
coordinatewise extrema and hence every closed face and corner. Therefore

$$
\boxed{B_0\subset\mathcal C_{17},\qquad
B_1\subset\mathcal C_{17}.}
\tag{14}
$$

The classifier retains both certificate labels as regression provenance but
does not subtract either box again. Thus the theorem-wise uncovered set is

$$
\boxed{\mathcal U_{17}=\mathcal D_{17}.}
\tag{15}
$$

## 7. Exact cap-9 method obstruction

Let

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
$$

The accepted Round 17 staircase paid at most $1+3=4$ states through
$K=k_2(\rho)$. Immediately above that face, the same crude min--max
bookkeeping must allow the first $\ell=2$ mode and therefore raises its cap
to $1+3+5=9$.

At $\rho_c$,

$$
z_{\rho_c}=\pi+\frac12<\frac{51}{14},
\qquad
k_2(\rho_c)^2<\frac{3777}{196}.
$$

Using $\pi>3$ and $1-\rho_c^3<1$,

$$
\mathcal W(\rho_c,k_2)
<\frac2{27}\left(\frac{3777}{196}\right)^{3/2}.
$$

All quantities are positive, and the reversible squared comparison is

$$
9^2-
\left[
\frac2{27}\left(\frac{3777}{196}\right)^{3/2}
\right]^2
=\frac{2121156829}{50824368}>0.
\tag{16}
$$

Hence

$$
\boxed{\mathcal W(\rho_c,k_2(\rho_c))<9.}
\tag{17}
$$

By continuity, replacing the cap $4$ uniformly by the crude cap $9$ cannot
continue the Round 17 payment immediately above $k_2$. This rules out only
that coarse proof mechanism. It is not a counterexample to the Pólya
inequality and does not assert that the actual strict count equals $9$.

## 8. Exact cell and face inventory

Every row below denotes a nonempty slice only when its strict frequency
interval is nonempty. A listed mechanism is a proof-design requirement, not
a granted lemma or Round 18 candidate.

| ratio cell | residual lower face | residual upper face | accepted neighboring owner | required proof-design mechanism |
|---|---|---|---|---|
| $(\rho_*,1/16]$ | $1/(2\rho)$, excluded | $H_0$, excluded | small-hole/high-angular rays | sharpen an angular entry payment without moving either face |
| $(1/16,\rho_{HK})$ | $1/(2\rho)$, excluded | $H_0$, excluded | full small-hole continuation | exact low-interface staircase |
| $\rho=\rho_{HK}$ | $1/(2\rho)$, excluded | $H_0=K_0$, excluded | shared upper owner | match both accepted upper formulas |
| $(\rho_{HK},\omega_0)$ | $1/(2\rho)$, excluded | $K_0$, excluded | fixed-ratio upper ray | ratio-dependent entry threshold |
| $\rho=\omega_0$ | $1/(2\rho)$, excluded | $K_0$, excluded | small-hole branch is open | direct fixed-ratio face argument |
| $(\omega_0,\rho_c)$ | $1/(2\rho)$, excluded | $K_0$, excluded | no small-hole input | lower-ratio angular staircase |
| $\rho=\rho_c$ | $k_2$, excluded | $K_0$, excluded | Round 17 band owns through $k_2$ | resolve the cap-9 obstruction on the shared ratio face |
| $(\rho_c,1/2)$ | $k_2$, excluded | $K_0$, excluded | Round 17 band below | sharper first $\ell=2$ entry or weighted payment |
| $\rho=1/2$ | $k_2$, excluded | $K_0$, excluded | continuous $K_0$ interface | match both $\eta_\rho$ formulas |
| $(1/2,5/6)$ | $k_2$, excluded | $K_0$, excluded | Round 17 band below | ratio-dependent next-angular staircase |
| $\rho=5/6$ | $k_2$, excluded | $1944$, excluded | seam begins inclusively | match fixed-ratio and seam faces |
| $(5/6,7/8)$ | $k_2$, excluded | $54/(1-\rho)^2$, excluded | seam above, endpoint at right | bounded seam staircase with endpoint trace |

The interfaces $\rho_{HK}$, $\omega_0$, $\rho_c$, $1/2$, and $5/6$ are
included ratio slices of the residual when their strict frequency interval
is satisfied. The two outer ratio faces are excluded. The value $1/16$ is
only a coarse bookkeeping split, not a change in the exact predicate.

## 9. Evidence classes and falsification ledger

- **Accepted analytic coverage:** exactly $\mathcal A_{17}$ in (7).
- **Accepted certified regression:** exactly the closed boxes $B_0,B_1$;
  neither changes (15).
- **Exact mask computation:** certified sign classification of rational
  parameter points and exact face truth tables; not a spectral proof.
- **Accepted method fact:** (17), with the narrow scope stated above.
- **Diagnostic only:** plots, sampled grids, and decimal switch locations.

Every later claim must test:

- $\rho=\rho_*,\rho_{HK},\omega_0,\rho_c,1/2,5/6,7/8$ and both one-sided
  traces where formulas change;
- $K=1/(2\rho)$, $K=z_\rho$, $K=k_2(\rho)$, every proposed spectral
  threshold, and $K=U(\rho)$;
- both exact ratio pieces rather than a rectangular proxy;
- strict spectral equality and accidental cross-channel coincidence;
- every closed face of $B_0$ and $B_1$, retaining their labels but never
  subtracting them from $\mathcal D_{17}$;
- an unresolved interval comparison, which must remain indeterminate;
- the difference between failure of the crude cap-9 mechanism and failure
  of the target inequality.

## 10. Frozen dependency manifest

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `3fa7413ae55f4f8c9ee6c55391d0100f19399cf875c1c43f57af46c081a3040c` |
| `state/next_round_prompts.md` | `41f9a16851eba9ea01ebb135201262e94cb114439213dfbf262fff6895fc0348` |
| `rounds/polya-main/round_017/judge/judge-017.md` | `769dc256aa97dc8da093bdead8a020033904c115ff256ae60a708a31f90dbadd` |
| `state/lemma_packets/SHELL-rho-compact-round17.md` | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| `computations/round17_residual_mask.py` | `b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b` |
| `computations/tests/test_round17_residual_mask.py` | `de43ee6b54d57b41db647f8b2c0cb2a79609069e59d0b2a50d335730a413dcc8` |
| `state/lemma_packets/SHELL-first-angular-bands-round17-claim.md` | `c23d8bd0e115214e394970746acb11fbe6355b44dbaa4efd75ab32b0009eae77` |
| `rounds/polya-main/round_017/reviews/analytic-compression-adversarial-referee.md` | `a13a05294af7957e817d3ca77440084c466c35334adaf5c1aa6cf610009c687b` |
| `rounds/polya-main/round_017/exploration/analytic-constant-audit.md` | `7fb22f516db763cc4f8fce6abf7aaa7b804fc88cd544c44589e41e3b37798be0` |
| `computations/round17_verify_candidate_c17_constants.py` | `b07f79b6f026dfe0a9e05a7198b5ac129ff4ff033eae644940eabe493a2d1469` |
| `computations/tests/test_round17_candidate_c17_constants.py` | `533620b5fadd9b7b13ff1d21ca9282bfd3d1ed778e7ecda970a3fb027ce3955c` |
| `rounds/polya-main/round_008/certification/pilot-central-box.json` | `f712c1ffb494461913665c578cc36c50d009b81cd48386afde6e49a68cddae00` |
| `rounds/polya-main/round_008/certification/pilot-central-box-check.json` | `02b12e13ad329e77035d8438ec359b6be4dd35571c384543f3890d67c132e6cc` |
| `rounds/polya-main/round_017/certification/pilot-extension-upward.json` | `858c55e832b3ca92f3b077dd7ea55f7ef6c4f7456de786c7264f178fcdf77b5b` |
| `rounds/polya-main/round_017/certification/pilot-extension-upward-check.json` | `e3bddf0b1488812e7572c318888f7f4721148b78c5e9ff98f7dabe7b19351d3f` |
| `computations/round18_residual_mask.py` | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| `computations/tests/test_round18_residual_mask.py` | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |

Reproduction commands:

~~~powershell
python computations/round18_residual_mask.py --self-check --manifest
python -m pytest computations/tests/test_round18_residual_mask.py -q
~~~

Expected focused result: **24 tests passed, 10 subtests passed**.

After this file receives its external SHA-256 freeze record, no worker may
edit it. Any correction requires a new packet and a new hash. Candidate
proof work must begin from these frozen bytes, and an isolated reviewer must
not receive an incumbent proof before returning an initial verdict.
