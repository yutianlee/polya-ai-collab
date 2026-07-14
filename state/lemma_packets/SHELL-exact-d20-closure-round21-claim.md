# Frozen Candidate Claim: Round 21 Exact Closure of D20

Status: **FROZEN CLAIM ONLY / NOT PROVED / NOT PROMOTED**.

Round: 21.

Candidate baseline commit:
`a537991fd8d0418b8338388783f1a7462e0707f4`.

This packet freezes only two proposed theorem statements, two exact
containment inequalities, a disjoint subtraction, face ownership, and the
review boundary. It contains no incumbent proof, certificate leaf, route
derivation, executable logic, test implementation, audit conclusion, judge
decision, or State Patch.

The two proof-free certificate contracts are:

- `state/certificate_contracts/ROUND21-compact-proxy-contract.md`;
- `state/certificate_contracts/ROUND21-aggregate-tail-contract.md`.

Their final byte identities and this candidate's identity are fixed by the
external candidate freeze.

## 1. Authenticated accepted residual

The only accepted Round 21 starting set is authenticated by:

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round21.md` | `fa37e7f619eeca7a53969a1a0af742ac746e2579268963fde1405465ee5e3df5` |
| `rounds/polya-main/round_021/exploration/residual-mask-freeze.md` | `92a35005b1381a81ecf3b2bc953a97b1f67084cc6992fe3317e6f75f03d80fd5` |
| `rounds/polya-main/round_021/reviews/residual-mask-independent-audit.md` | `0e161d306e7d60646d71f5d42f5ed93f723c9fa07603564ece98d3255f08bf08` |

Retain

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_{11}(\rho)=\sqrt{z_\rho^2+132}.
\tag{1}
$$

The accepted live residual is exactly

$$
\boxed{
\mathcal D_{20}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac{39}{50},
\quad k_{11}(\rho)<K<K_0(\rho)=U(\rho)
\right\}.}
\tag{2}
$$

The left ratio face is included, the right ratio face is excluded, and both
frequency inequalities are strict. Equation (2) is accepted bookkeeping;
it supplies no Round 21 spectral estimate.

## 2. Candidate C21 theorem statements

Put

$$
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{3}
$$

### 2.1 Compact theorem

The proposed compact theorem is

$$
\boxed{
\frac7{51}\leq\rho\leq\frac{39}{50},
\qquad 12\leq K\leq200}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<W(\rho,K).}
\tag{4}
$$

The rectangle in (4) is a theorem domain, not the live residual.

### 2.2 Aggregate theorem

The proposed aggregate theorem is

$$
\boxed{
\rho_c\leq\rho\leq\frac{39}{50},
\qquad K\geq200}
\quad\Longrightarrow\quad
\boxed{N_D(A_{\rho,1},K^2)<W(\rho,K).}
\tag{5}
$$

The domain in (5) is also a theorem domain, not the live residual.

The analytic and finite-certificate obligations behind (4)--(5) are exactly
the predicates in the two authenticated proof-free contracts. Appearance
in a contract does not make any predicate proved.

## 3. Exact containment claims

The isolated reviewer must independently prove the exact inequalities

$$
\boxed{\frac7{51}<\rho_c}
\tag{6}
$$

and

$$
\boxed{k_{11}(\rho)>12\qquad(\rho\geq\rho_c).}
\tag{7}
$$

No decimal approximation may establish (6) or (7). Independently proved
rational enclosures for $\pi$, elementary calculus, and exact rational
arithmetic are allowed.

For every point of $\mathcal D_{20}$, equations (2), (6), and (7) propose
the exact guard relations

$$
\frac7{51}<\rho_c\leq\rho<\frac{39}{50},
\qquad
12<k_{11}(\rho)<K<K_0(\rho)=U(\rho).
\tag{8}
$$

Thus the compact theorem is claimed to cover every point of
$\mathcal D_{20}$ with $K\leq200$, and the aggregate theorem is claimed to
cover every point of $\mathcal D_{20}$ with $K>200$.

## 4. Proposed genuinely new set and disjoint subtraction

Define the proposed subtraction owners

$$
\boxed{
\mathcal C_{21}=\mathcal D_{20}\cap\{K\leq200\},
\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.}
\tag{9}
$$

The frequency face $K=200$ is assigned to $\mathcal C_{21}$. Although both
proposed theorems include that face, it is subtracted exactly once.

The required exact truth table is:

| point already known to lie in $\mathcal D_{20}$ | compact theorem applies | aggregate theorem applies | unique subtraction owner |
|---|---|---|---|
| $K<200$ | yes, by (8) | no | $\mathcal C_{21}$ |
| $K=200$ | yes | yes | $\mathcal C_{21}$ |
| $K>200$ | no | yes | $\mathcal T_{21}$ |

The candidate claims the exact disjoint union

$$
\boxed{
\mathcal D_{20}=\mathcal C_{21}\,\dot\cup\,\mathcal T_{21}}
\tag{10}
$$

and proposes, subject to every review and promotion gate below,

$$
\boxed{
\mathcal D_{21}^{\rm proposed}
:=\mathcal D_{20}\setminus
(\mathcal C_{21}\cup\mathcal T_{21})
=\varnothing.}
\tag{11}
$$

Equation (11) is a candidate conclusion only. The live repository residual
remains (2) unless and until an accepted Round 21 State Patch changes it.

## 5. Complete face ownership

| face | accepted or proposed assignment |
|---|---|
| $\rho=7/51$ | included guard face of (4), but outside $\mathcal D_{20}$ by (6) |
| $\rho=\rho_c$ | included in $\mathcal D_{20}$ when both frequency inequalities in (2) hold; proposed Round 21 owner then follows (9) |
| $\rho=39/50$ | excluded from $\mathcal D_{20}$; accepted Round 20 optical owner; not subtracted again |
| $K=12$ | included guard face of (4), but outside $\mathcal D_{20}$ by (7) and $K>k_{11}$ |
| $K=k_{11}(\rho)$ | excluded from $\mathcal D_{20}$; accepted Round 20 closed-staircase owner |
| $12<K<200$ | compact owner exactly when the point also satisfies (2) |
| $K=200$ | compact subtraction owner exactly when the point also satisfies (2); aggregate theorem overlap is not a second owner |
| $200<K<K_0(\rho)$ | aggregate owner exactly when the point also satisfies (2) |
| $K=K_0(\rho)=U(\rho)$ | excluded from $\mathcal D_{20}$; inherited upper-frequency owner |

No value or ordering of $U(\rho)$ relative to 200 is needed for (10): if
$U<200$, all residual points are compact-owned; if $U=200$, the strict upper
face excludes $K=200$; if $U>200$, the three rows of the truth table apply.

## 6. Strict A3 isolation boundary

Before returning its initial verdict, A3 may receive and read only:

1. this candidate and the two proof-free contracts;
2. the three accepted residual artifacts in Section 1;
3. the following exact foundational packets and source card:

| artifact | SHA-256 | permitted scope |
|---|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` | separated spectrum, multiplicity, strict count |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` | phase enclosure in its proved scope |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` | strict weighted count, tail identities, normalization |
| `state/lemma_packets/SHELL-low-interface-fixed-rho-high-energy.md` | `0b8346462da0bb68efca08162a6d4a62d114950650800c5cd46e4366730a1b2f` | accepted one-tail split, curvature, shelf, interface bounds |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` | only the qualified $G$, trapezoidal-floor, and interface integral statements named in the contracts |

A3 may additionally use elementary real calculus, elementary
one-dimensional summation, exact integer and rational arithmetic, and
independently proved rational enclosures for $\pi$. It must reconstruct the
compact spectral bridge and monotone-corner implication, the aggregate
summation and strict reserve implication, and every derivative identity. For
every $7/51\leq\rho\leq39/50$ and every $K\geq200$, A3 must separately
derive

$$
I_{KK}<\frac{3\rho b}{4S}<\frac{3b}{4K}
\leq\frac{3b}{800},
\qquad E_{KK}>0,
\qquad \mathcal B_{KK}>F,
$$

propagate the guards $\mu>3/2$, $K\eta_\rho>1$, and
$S>\overline R>\rho K$, and integrate from the certified $K=200$ values to
prove conditionally that the separately certified base signs, including
$F>0$, imply $\mathcal B_K>0$ and $\mathcal B>0$. The finite sign $F>0$ is
an A4 certificate predicate; it is not relabelled as an A3 analytic result.
A3 may not use a replayed $K=200$ curvature sign as the all-frequency step.
It must also reconstruct (6)--(7), all faces, and (10)--(11).

The following are expressly excluded from A3 even if their path or hash is
visible in a contract:

- `rounds/polya-main/round_021/exploration/exact-d20-closure.md`;
- every Round 21 aggregate route, certificate report, certificate audit,
  verifier, and test implementation;
- every Round 21 compact certificate report, certificate audit, verifier,
  and test implementation;
- every Round 20 proof, response, source-proof note, executable verifier,
  audit, cross-comparison, referee report, judge file, and State Patch;
- every Round 21 cross-comparison, referee report, judge draft, and State
  Patch created after this freeze.

A3 must authenticate every permitted byte before reading it. Its verdict
must identify the first unsupported implication on failure. Agent agreement,
an incumbent verdict, a decimal margin, and a sampled computation are not
mathematical verification.

## 7. Separate A4 boundary

A4 validates certificates and exact set logic; it does not replace A3's
analytic reconstruction. It must authenticate and replay the sealed targets
in both contracts, test the listed falsification mutations, use a higher
precision replay in addition to each frozen precision, and implement an
independent exact classifier for (2) and (9) on every outer and shared face.

The compact audit must cover every leaf, strict integer wall, active-channel
cutoff, zero-extension interface, monotone corner, exact coverage invariant,
and half-open owner. The aggregate audit must cover every ratio box, both
$\eta_\rho$ branches, the $\rho=1/2$ interface, all $K=200$ base signs and
guards, the base-frequency derivative consistency checks, and the precision
gate. A4 must independently check the derivative identities and verify that
the sealed executable makes no finite-box claim at $K>200$. Its replayed
$K=200$ checks of $I_{KK}$, $E_{KK}$, and $\mathcal B_{KK}$ are base
consistency only; they cannot replace A3's universally quantified analytic
derivation or the two integrations to all $K\geq200$.

No binary float or displayed decimal may reach a proof decision in either
certificate.

## 8. Review and promotion sequence

After independent A3 and A4 reviews, a cross-comparison must preserve every
discrepancy and repair chronologically. A fresh candidate referee must then
assume this claim false and reconstruct every spectral bridge, derivative,
strict wall, containment, and set face.

Only after those gates may a Round 21 lemma judge propose a State Patch. A
promotion patch must create narrowly scoped obligations
`CERT-round21-compact-proxy` and `CERT-round21-aggregate-tail`, each limited
to its stated theorem domain and authenticated evidence. The legacy
`COMP-certified-bessel` obligation remains `diagnostic_only` and is not
promoted or broadened. Any obsolete target dependency on that diagnostic
parent may be removed only in the audited State Patch that installs the two
scoped certificate obligations.

Even an accepted State Patch proving exact closure of (2) does not by itself
promote `SHELL-rho-compact`, `SHELL-rho-uniformity`, `TARGET-shell-d3`, or
`POLYA-program-target`. A separate theorem-level clean-room reconstruction,
a separate fresh adversarial theorem referee, a later theorem judge, and a
separate program-scope audit remain mandatory before the corresponding
target statuses may change.

## 9. Mandatory falsification faces and nonclaims

The initial reviewers must explicitly test:

1. both sides and equality at $\rho=7/51$, $\rho_c$, and $39/50$;
2. both sides and equality at $K=12$, $k_{11}(\rho)$, $200$, and
   $K_0(\rho)=U(\rho)$;
3. every vertex of the compact rectangle and both aggregate ratio faces at
   $K=200$;
4. the three exact $K<200$, $K=200$, and $K>200$ rows, including all three
   possible orderings of $U$ with 200;
5. exact strict-count behavior at every integer phase wall and half-integer
   active-channel wall;
6. both branches and the common value of $\eta_\rho$ at $\rho=1/2$;
7. (6)--(7), (8), the disjointness in (10), and the no-double-subtraction
   rule at $K=200$;
8. exclusion of $\rho=39/50$, $K=k_{11}$, and $K=K_0=U$ from the live
   residual;
9. the strict separation between finite $K=200$ certificate predicates and
   the universally quantified analytic curvature and integration steps for
   every $K\geq200$.

No assertion in this packet is proved merely by being frozen. The compact
and aggregate certificate domains are not themselves $\mathcal D_{20}$.
The live residual is not empty at this stage. No ellipse theorem, fallback
certificate family, higher-dimensional domain, uniform-shell theorem, full
shell theorem, or project program theorem is claimed.

Any correction to this candidate or either contract requires replacement
bytes, a replacement external freeze, and a new final-byte audit before an
isolated verdict is credited.
