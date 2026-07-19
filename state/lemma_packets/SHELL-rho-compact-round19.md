# Lemma Packet: Exact Round 19 Post-Round-18 Residual Mask

Status: **FROZEN RESIDUAL MAP / NO NEW THEOREM**.

Round: 19.

Primary obligations: **SHELL-rho-compact** and
**COMP-certified-bessel**.

Baseline commit:
`15e4d61db885bfff00a674fd7f37e4cffda70d0c`.

This packet freezes the accepted state after the Round 18 State Patch and
before any Round 19 proof candidate. It records exact set arithmetic, face
ownership, and the known next method walls. It does not prove a new spectral
estimate, order any Round 19 crossing globally, propose a new threshold, or
turn a mask classification into a theorem.

## 1. Authenticated inherited state

Round 19 imports the post-Round-17 analytic classifier in
`computations/round18_residual_mask.py` as an opaque base. It does not
reconstruct the older analytic union from prose. The following committed
inputs were authenticated before this packet was released.

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `24c2970516f503c765d0db280a360b37724c540e536016f9bf35fbaafb94132e` |
| `state/next_round_prompts.md` | `7d05055b4b884b052f3970bd7b08335dfe63bca25b5ac5a9db8704f6a88db2f7` |
| `rounds/polya-main/round_018/judge/judge-018.md` | `73132dfb49fd958e7f41adb43f01175f9eb4e008501d923e847c06e858782d61` |
| `state/lemma_packets/SHELL-rho-compact-round18.md` | `7c70440b5c66d1a7af1a31892676998a8fd05e959c860763ca522b9bdf1f11d9` |
| `rounds/polya-main/round_018/exploration/residual-mask-freeze.md` | `7f507b0b7fd0c625c67e1511f3433237f094809750baf888bb408667cd1cc2ff` |
| `computations/round18_residual_mask.py` | `75ede07aab5ce24b8339ea9cdf53664d4b14c3ab5ffc0a8130841945c3da52da` |
| `computations/tests/test_round18_residual_mask.py` | `ed5f39389354538e71fd843ff64267fc3514ac1219f0e9f04bc2b9410bf9c103` |
| `state/lemma_packets/SHELL-next-angular-staircase-round18-claim.md` | `354e3beae50ed837ef7da0f986da93d36d4385770c600a73dddd6d2eb16870e9` |
| `rounds/polya-main/round_018/exploration/candidate-claim-freeze.md` | `b4e4d71b569a48dd37c954bb97f90903d246e3d885fd19f51422cf2792093f6c` |

These hashes authenticate inputs only. The separate Round 19 freeze record
authenticates this packet, its executable classifier, and its tests.

## 2. Inherited constants and exact upper floor

Retain

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
I_{18}=\left[\rho_*,\frac78\right].
$$

For $0<\rho<1$, put

$$
G_1(t)=\frac{\sqrt{1-t^2}-t\arccos t}{\pi},
\qquad
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
H_0(\rho)=\frac{C_*}{\omega_0-\rho}
\quad(\rho<\omega_0).
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
$$

Then

$$
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\[2pt]
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\[2pt]
54/(1-\rho)^2,&5/6\le\rho<7/8.
\end{cases}
\tag{2}
$$

At $\rho_{HK}$ the first two values agree. The face $K=U(\rho)$ is
included in inherited analytic coverage and excluded from the residual.

## 3. Accepted Round 18 staircase and analytic predicate

Define

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\tag{3}
$$

The accepted closed Round 18 theorem band is

$$
\overline{\mathcal C}_{18}
=\left\{(\rho,K):
\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_5(\rho)
\right\}.
\tag{4}
$$

Its genuinely new part relative to the post-Round-17 analytic mask is

$$
\mathcal C_{18}
=\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_2(\rho)<K\le k_5(\rho)
\right\}.
\tag{5}
$$

Thus $K=k_2(\rho)$ retains its Round 17 owner, $K=k_5(\rho)$ is included
under the Round 18 owner, and $\rho=7/8$ retains its complete endpoint
owner. Let $\mathcal A_{17}^{\mathrm{frozen}}$ denote exactly the analytic
predicate returned by the authenticated Round 18 classifier. The accepted
post-promotion predicate is

$$
\boxed{
\mathcal A_{18}
=\mathcal A_{17}^{\mathrm{frozen}}
\cup\overline{\mathcal C}_{18}.
}
\tag{6}
$$

For rational query points with $K\ge0$, the added disjunct is evaluated as

~~~text
rho >= rho_c
and rho <= 7/8
and (1-rho)*K >= pi
and (1-rho)^2*K^2 <= pi^2 + 30*(1-rho)^2
~~~

Every equality in this disjunct is included. Irrational comparisons are
certified by precision-escalated Arb signs; they are never guessed.

## 4. Exact two-piece residual

Exact subtraction gives

$$
\mathcal D_{18}
=\left(I_{18}\times[0,\infty)\right)\setminus\mathcal A_{18}
=\mathcal D_{17}\setminus\mathcal C_{18}.
\tag{7}
$$

Its normalized form is

$$
\boxed{
\begin{aligned}
\mathcal D_{18}
={}&\left\{(\rho,K):
\rho_*<\rho<\rho_c,
\quad \frac1{2\rho}<K<U(\rho)
\right\}\\
&\cup
\left\{(\rho,K):
\rho_c\le\rho<\frac78,
\quad k_5(\rho)<K<U(\rho)
\right\}.
\end{aligned}
}
\tag{8}
$$

Every displayed frequency inequality in (8) is strict. In particular:

- $\rho=\rho_c$ belongs only to the post-$k_5$ piece;
- $K=1/(2\rho)$ below $\rho_c$ and $K=k_5(\rho)$ at or above $\rho_c$
  are covered lower faces;
- $K=U(\rho)$ is a covered upper face;
- $\rho=\rho_*$ and $\rho=7/8$ are complete covered endpoint faces.

The exact witness

$$
(\rho,K)=\left(\frac12,30\right)\in\mathcal D_{18}
$$

is retained. The residual is therefore nonempty and no theorem target is
closed by this packet.

## 5. Theorem-wise uncovered set and certified regressions

Retain the closed boxes

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times\left[\frac{67}{10},\frac{168}{25}\right],
$$

$$
B_1=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times\left[\frac{168}{25},\frac{673}{100}\right].
$$

The accepted closed-face checks give

$$
B_0\subset\mathcal C_{17}\subset\mathcal A_{18},
\qquad
B_1\subset\mathcal C_{17}\subset\mathcal A_{18}.
$$

Both certificates remain independent regression evidence. Neither is
subtracted again, so the theorem-wise uncovered set is exactly

$$
\boxed{
\mathcal U_{18}
=\left(I_{18}\times[0,\infty)\right)
\setminus\left(\mathcal A_{18}\cup B_0\cup B_1\right)
=\mathcal D_{18}.
}
\tag{9}
$$

## 6. Complete face and interface inventory

| face or interface | frozen assignment |
|---|---|
| $\rho=\rho_*$ | complete small-hole endpoint; outside $\mathcal D_{18}$ |
| $\rho=\rho_{HK}$ | included ratio slice; shared $H_0=K_0$ upper owner; implementation selects the $K_0$ branch |
| $\rho=\omega_0$ | included low-ratio slice; $H_0$ eligibility ends, while $K_0$ was already active |
| $\rho=\rho_c$ | assigned to the post-$k_5$ component; for $k_5<K<U$ it is residual, not covered |
| $\rho=1/2$ | included slice; continuous $\eta_\rho$ formula interface |
| $\rho=5/6$ | included high-ratio slice; seam owner begins inclusively |
| $\rho=7/8$ | complete thin endpoint; outside $\mathcal D_{18}$ |
| $K=1/(2\rho)$ for $\rho<\rho_c$ | inherited high-angular owner; excluded from the residual |
| $K=z_\rho$ | inherited phase-zero owner |
| $K=k_2(\rho)$ | Round 17 first-angular-band owner |
| $K=k_5(\rho)$ | Round 18 angular-staircase owner |
| $K=U(\rho)$ | active $H_0$, $K_0$, or seam owner; excluded from the residual |
| $K=295^2$ | Round 16 all-ratio high-frequency owner |
| $K=2z_\rho$ | method wall only; it does not alter $\mathcal D_{18}$ membership |
| $K=k_6(\rho)$ | method wall only; it does not alter $\mathcal D_{18}$ membership |

The historical $\rho=1/16$ division remains only an inherited bookkeeping
split. It is not an active $U$ branch or a new Round 19 predicate.

## 7. Frozen method boundary, not a candidate claim

The following facts and only these facts are carried into Round 19:

1. $K=k_5(\rho)$ is covered, and the Round 18 theorem grants nothing for
   $K>k_5(\rho)$.
2. $k_5(\rho)<U(\rho)$ on $\rho_c\le\rho<7/8$.
3. $K=2z_\rho$ is the exact $\ell=0,n=2$ radial wall. Strict counting
   excludes equality and the mode enters immediately above it.
4. $k_6(\rho)=\sqrt{z_\rho^2+42}$ is the next crude angular wall.
5. At the single accepted left face,

   $$
   k_5(\rho_c)<2z_{\rho_c}<k_6(\rho_c).
   \tag{10}
   $$

The executable inventory computes the signs of the three walls
independently. It encodes no global ordering, no crossing threshold, and no
new spectral exclusion. In particular, Round 19 may not:

- continue a one-radial-mode cap above $2z_\rho$;
- continue a stale angular cap through $k_6(\rho)$;
- extend the Round 18 staircase below $\rho_c$ or above $k_5(\rho)$;
- replace the lower-ratio component by continuity from the high-ratio one;
- import a new Bessel-zero order from the qualified Lorch source card; or
- report (10) as a counterexample.

The relative ordering of $2z_\rho$ and $k_6(\rho)$ away from $\rho_c$ is a
Round 19 question, not frozen input.

## 8. Executable predicate and tri-state policy

The classifier imports the authenticated Round 18 predicate and applies
only the union (6). It then evaluates (8) independently and raises an error
if the complement and normalized forms disagree.

The high-piece comparison $K>k_5(\rho)$ uses the sign of

$$
\pi^2+(30-K^2)(1-\rho)^2.
\tag{11}
$$

The method walls use, independently,

$$
4\pi^2-K^2(1-\rho)^2
\quad\text{and}\quad
\pi^2+(42-K^2)(1-\rho)^2.
\tag{12}
$$

Neither expression in (12) participates in residual membership.

Exact rational comparisons are used wherever possible. A material
irrational sign that remains unresolved after precision escalation returns
`indeterminate`. A false conjunction factor may suppress irrelevant
unresolved signs, and an authenticated true analytic disjunct may settle
the union. An unresolved mandatory compact-domain gate may not be
overridden.

The regression suite specifically protects:

- $\rho=\rho_*$ and $\rho=\rho_c$;
- $K=z_\rho$, $K=k_2(\rho)$, $K=k_5(\rho)$, and $K=U(\rho)$;
- the $H_0=K_0$ switch and the inclusive $\rho=5/6$ seam;
- all closed $B_0$ and $B_1$ corners;
- the distinction between indeterminate genuinely-new-$\mathcal C_{18}$
  attribution at $K=k_2$ and decisive overall staircase coverage; and
- indeterminate $2z_\rho$ or $k_6(\rho)$ wall signs without any change to
  a decisively classified $\mathcal D_{18}$ point.

## 9. Release rule

The Round 19 packet, classifier, and test bytes listed in the separate
freeze record are immutable after release. Any correction requires a
replacement packet, classifier, tests, and freeze record with new hashes.

Only after this freeze passes may an incumbent analytic worker inspect the
mask and develop a candidate. A later candidate must be frozen in a
separate proof-free claim packet before isolated reconstruction or
independent exact-constant review. Nothing in this packet is such a
candidate.
