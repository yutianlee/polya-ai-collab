# Frozen Candidate Claim: Round 19 Two-Sided Staircase

Status: **FROZEN CLAIM ONLY / NOT PROVED / NOT PROMOTED**.

Round: 19.

Baseline commit:
`5814b335a108d3af25aadde312dcc9581172e9f6`.

Frozen residual packet:
`state/lemma_packets/SHELL-rho-compact-round19.md`, SHA-256
`33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50`.

Residual-mask freeze record:
`rounds/polya-main/round_019/exploration/residual-mask-freeze.md`, SHA-256
`0c64053efc91bfe057fc936a38120a68f5a0c74ba2695cbcf62cc5b8385c09e9`.

Permitted spectral packet:
`state/lemma_packets/SHELL-sturm-liouville-completeness.md`, SHA-256
`6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8`.

Permitted source cards:

- `sources/lorch_bessel_zeros.md`, SHA-256
  `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4`;
- `sources/flps_balls.md`, SHA-256
  `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38`;
- `sources/round19_bessel_zero_bounds.md`, SHA-256
  `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f`.

This file contains only the candidate statements, proposed constants,
permitted inputs, and falsification walls. It contains no Round 19
incumbent proof, crossing ledger, executable constant audit, sampled root,
certificate, review, or judge decision.

## 1. Definitions

Retain the inherited constants and upper floor from the frozen residual
packet. Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
L(\rho)=\frac1{2\rho},
$$

$$
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)},
\qquad
p_1(\rho)=\sqrt{4z_\rho^2+2},
\qquad
d=\frac{\sqrt{337}}2,
\tag{1}
$$

and

$$
\mathcal W(\rho,K)
=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{2}
$$

The spectral counting convention is strict: an eigenvalue equal to $K^2$
is not counted.

## 2. Candidate C19

Reconstruct or refute both claims below without consulting an incumbent
proof.

### High-ratio extension

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_6(\rho)
}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{3}
$$

The accepted Round 18 theorem already owns the closed subband through
$k_5$. The genuinely new high-ratio portion is exactly

$$
\boxed{
\mathcal C_{19}^{\rm H}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_5(\rho)<K\leq k_6(\rho)
\right\}.}
\tag{4}
$$

### Lower-ratio extension

$$
\boxed{
\frac1{\sqrt{337}}<\rho<\rho_c,
\qquad
L(\rho)<K\leq d
}
\quad\Longrightarrow\quad
\boxed{
N_D(A_{\rho,1},K^2)<\mathcal W(\rho,K).}
\tag{5}
$$

Because $L(\rho)<d$ exactly when $\rho>1/\sqrt{337}$, the genuinely new
lower-ratio portion can equivalently be written

$$
\boxed{
\mathcal C_{19}^{\rm L}
=\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad L(\rho)<K\leq d
\right\}.}
\tag{6}
$$

The proposed Round 19 addition is the disjoint union

$$
\boxed{\mathcal C_{19}=\mathcal C_{19}^{\rm L}
\cup\mathcal C_{19}^{\rm H}.}
\tag{7}
$$

An initial PASS must independently prove (3) and (5), prove
$\mathcal C_{19}\subset\mathcal D_{18}$, and derive the exact subtraction

$$
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\left\{(\rho,K):
\rho_*<\rho\leq\frac1{\sqrt{337}},
\quad L(\rho)<K<U(\rho)\right\}\\
&\cup
\left\{(\rho,K):
\frac1{\sqrt{337}}<\rho<\rho_c,
\quad d<K<U(\rho)\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}}
\tag{8}
$$

The inclusions require independent strict proofs of

$$
d<U(\rho)\quad(\rho_*<\rho<\rho_c),
\qquad
k_6(\rho)<U(\rho)\quad(\rho_c\leq\rho<7/8).
\tag{9}
$$

Equations (8)--(9) are bookkeeping conclusions to be proved from the
frozen predicate. They are not permitted spectral inputs.

## 3. Proposed high-ratio staircase data

The proposed first-entry thresholds are

$$
c_2=\frac{51}{10},
\quad c_3=\frac{13}{2},
\quad c_4=\frac{15}{2},
\quad c_5=\frac{17}{2},
\quad c_{1,2}=\frac{77}{10}.
\tag{10}
$$

The proposed ratio splits are

$$
r_2=\frac3{10},
\quad r_3=r_4=\frac12,
\quad r_{1,2}=\frac15,
\quad r_5=\frac{13}{25},
\tag{11}
$$

together with the inventory split $\rho=1/4$. The proposed strict-count
caps are

$$
4,9,16,25
\quad\hbox{for delayed first-mode entry},
\qquad
26,29
\quad\hbox{after the two possible second-mode entries},
\qquad
36
\quad\hbox{after first-channel entry at }\ell=5.
\tag{12}
$$

On $\rho_c\leq\rho\leq1/4$ the proposed exhaustive inventory through
$K=k_6$ consists of first modes $0\leq\ell\leq4$ and the two possible
second modes $(\ell,n)=(0,2),(1,2)$. On
$1/4\leq\rho\leq7/8$ it consists only of first modes
$0\leq\ell\leq5$. These inventories, all payments, and every equality
face are claims to be checked, not supplied facts.

## 4. Proposed lower-ratio staircase data

The proposed fixed thresholds are ordered as

$$
4<\frac{51}{10}<\frac{13}{2}<\frac{15}{2}
<\frac{77}{10}<\frac{17}{2}<9<d.
\tag{13}
$$

The proposed exhaustive strict-count caps are

| frequency range | proposed cap |
|---|---:|
| $L<K\leq4$ | $1$ |
| $4<K\leq51/10$ | $4$ |
| $51/10<K\leq13/2$, $K\leq2z_\rho$ | $9$ |
| $51/10<K\leq13/2$, $K>2z_\rho$ | $10$ |
| $13/2<K\leq15/2$, $K\leq2z_\rho$ | $16$ |
| $13/2<K\leq15/2$, $K>2z_\rho$ | $17$ |
| $15/2<K\leq77/10$ | $26$ |
| $77/10<K\leq17/2$ | $29$ |
| $17/2<K\leq9$ | $40$ |
| $9<K\leq d$ | $45$ |

The proposed inventory through $K=d$ consists of first modes
$0\leq\ell\leq5$ and possible second modes
$0\leq\ell\leq2$; all first modes with $\ell\geq6$, all second modes with
$\ell\geq3$, and all $n\geq3$ are proposed to be absent. The additional
internal zero estimate

$$
j_{5/2,2}>9
\tag{14}
$$

and any ball-channel comparison used to propagate it are reconstruction
obligations, not permitted lemmas. The source cards do not supply (14).

Every lower threshold in the table is open. At an exact spectral entry the
new mode remains excluded by strict counting. The upper face $K=d$ is
included.

## 5. Permitted inputs and provenance boundary

Before its initial verdict, a clean-room reviewer may use only:

1. this hash-authenticated candidate and the six hash-authenticated
   packets or source cards listed at its start;
2. the accepted Round 18 band and exact residual predicate stated in the
   frozen Round 19 residual packet;
3. the sourced unit-ball bounds

   $$
   j_{5/2,1}>\frac{51}{10},\quad
   j_{7/2,1}>\frac{13}{2},\quad
   j_{9/2,1}>\frac{15}{2},\quad
   j_{11/2,1}>\frac{17}{2},\quad
   j_{3/2,2}>\frac{77}{10};
   $$

4. elementary one-dimensional Dirichlet Sturm--Liouville theory, Hardy's
   inequality, the variational min--max principle, extension by zero for
   $H_0^1$, and elementary spherical-Bessel identities;
5. exact rational arithmetic and independently reconstructed elementary
   inequalities for $\pi$ and the displayed radicals.

The reviewer must internally prove every shell-to-ball fixed-channel
comparison, including form domains, preservation of the angular channel,
and the inequality direction. It must also internally prove or refute any
comparison between different ball angular channels. No source may be cited
for a shell cross-product zero, a shell multiplicity, a Weyl payment, or a
new zero outside the five statements above.

No Round 19 incumbent response or exploration proof, source-audit review,
crossing ledger, executable constant verifier, sampled root, plot,
certificate, repository diff, cross-review, or judge draft is a permitted
input before the initial verdict.

## 6. Mandatory falsification walls

The initial reconstruction must explicitly test:

- $\rho=\rho_*,1/\sqrt{337},\rho_c,1/5,1/4,3/10,1/2,
  13/25,5/6,7/8$, every active interface of $U$, and both one-sided traces
  at each interior split;
- $K=L(\rho),z_\rho,k_2,\ldots,k_6,2z_\rho,p_1(\rho),d,U(\rho)$ and every
  fixed threshold in (10) and (13), including all empty or degenerate
  subbands created by changing wall order;
- radial indices $n=1,2,3$ and angular orders $\ell=0,1,\ldots,6$, with
  full multiplicities $2\ell+1$, all remaining-mode exclusions, and all
  possible cross-order coincidences;
- the exact $\ell=0$ frequencies $nz_\rho$, the proposed $n\geq2$ and
  $n\geq3$ exclusions, and strict ownership at $K=2z_\rho$;
- the complete proof and root enumeration behind the unsourced proposal
  $j_{5/2,2}>9$, including every tangent half-period and the point $x=9$;
- the form-domain proof behind both the fixed-channel shell-to-ball
  comparison and any proposed ball angular-shift inequality;
- the scope, order, radial index, strict direction, and positive-zero
  convention behind every sourced Bessel statement;
- every Weyl-payment threshold corresponding to the caps in (12)--(13),
  on both sides of every fixed/moving split, without assuming the false
  uniform payment $\mathcal W(\rho,k_5)>25$ near $\rho_c$;
- every monotonicity, derivative sign, denominator, square root, positive
  squaring, inverse, and extremal substitution used to make a constant
  uniform;
- both comparisons in (9), every strict/inclusive face in (4), (6), and
  (8), and the exact slice $\rho=1/\sqrt{337}$ where $L=d$;
- the facts that $B_0$ and $B_1$ were already absorbed before Round 19 and
  are not subtracted again.

The reviewer must return **PASS** or **FAIL** and identify the first
unsupported implication before reading any excluded artifact. Agreement
with the candidate, a finite ledger, or agent consensus is not
verification.

## 7. Non-claim

No assertion is made for the three open components of (8). In particular,
this candidate does not prove the full shell Pólya conjecture. The first
clean-room verdict and a later exact-constant audit are still required
before any State Patch may promote (3), (5), or (8).
