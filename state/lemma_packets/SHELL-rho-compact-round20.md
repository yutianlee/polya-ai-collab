# Lemma Packet: Exact Round 20 Post-Round-19 Residual Mask

Status: **FROZEN RESIDUAL MAP / NO NEW THEOREM**.

Round: 20.

Primary obligations: **SHELL-rho-compact** and
**COMP-certified-bessel**.

Baseline commit:
`658674117632d60990ac9b9046aa0fcff9e91a62`.

This packet freezes the accepted state after application and independent
state audit of the Round 19 State Patch and before any Round 20 proof
candidate. It performs exact set subtraction only. It does not use a Round
20 exploratory proof, prove a new spectral estimate, propose a new
threshold, or change any theorem or computation status.

## 1. Authenticated committed state

Round 20 imports `computations/round19_residual_mask.py` as the opaque
accepted classifier for $\mathcal A_{18}$. The following bytes at the
baseline commit were authenticated before release.

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `ece14c8af98556a15069e01a2d1cf2c12c155ea4e547457e3572a10643ace187` |
| `state/next_round_prompts.md` | `c6e8d75717ff2286a1e29fe42f51b4922d12ef4d019cebdfa5a614f661f84159` |
| `state/lemma_packets/SHELL-rho-compact-round19.md` | `33cdf990264fae537b96b6c0e80f7dad5d0071c2f8125dccaf45abb0c005ba50` |
| `computations/round19_residual_mask.py` | `bebb432ff184e942ae46af8f6a826215484bc324230259bab9fd1e97e6f66ff6` |
| `computations/tests/test_round19_residual_mask.py` | `41629e91a777abed027827ca38a589d9271d2e7c62d9fdf52c48f17a252d7787` |
| `rounds/polya-main/round_019/reviews/residual-mask-independent-audit.md` | `9e7dedaab08425166998a5c766bdb32d3787d9f35b6c4bf4b7d6be07009c9b43` |
| `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| `sources/round19_bessel_zero_bounds.md` | `7408cd00608f2548a357247fcb61dae45ee15adc5eb2330320f8680989a2a94f` |
| `rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md` | `ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md` | `24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17` |
| `computations/round19_verify_two_sided_staircase.py` | `4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23` |
| `computations/tests/test_round19_verify_two_sided_staircase.py` | `1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md` | `fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-cross-comparison.md` | `fe46d95718e4e070bdea18ee1c2fbcfc89d5eb3c53b5346d712c72715f667365` |
| `rounds/polya-main/round_019/reviews/two-sided-staircase-adversarial-referee.md` | `6e290b70bf2bdaf9785f67fcef4a284a48b08ccce0c0951e72f0322406e58148` |
| `rounds/polya-main/round_019/judge/judge-019.md` | `fdf79fa03f1cd82e5ecf4db89750aa0e5d876be6430a25e488bb1c34bdabc83b` |
| `rounds/polya-main/round_019/reviews/state-patch-final-audit.md` | `a4cb244e9b97fb5cceaaf82896e87320c1d828d75da09a4da0bd8c13839ca76a` |
| `rounds/polya-main/round_019/reviews/derived-state-final-audit.md` | `c94de1a40cec0650ca1adcd0662f1bc1cb403f503472afab3ef3e27a48e41e93` |

The graph and prompt hashes are baseline Git-blob identities. Permanent
tests authenticate those blobs rather than mutable live paths, so a later
accepted State Patch cannot create a false regression. The separate Round
20 freeze record also records that the live paths matched these blobs at
release time.

## 2. Inherited constants and upper floor

Retain the authenticated Round 19 definitions

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
I_{19}=\left[\rho_*,\frac78\right].
$$

For $0<\rho<1$, let

$$
G_1(t)=\frac{\sqrt{1-t^2}-t\arccos t}{\pi},
\quad
a_\rho=\frac{2\pi\rho}{1-\rho},
\quad
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

The inherited exact upper floor is

$$
U(\rho)=\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right).
\tag{1}
$$

It retains its accepted $H_0$, $K_0$, and seam-$54$ branch assignments,
including the $H_0=K_0$ interface and the inclusive seam at $\rho=5/6$.
The face $K=U(\rho)$ is covered and never belongs to the residual.

## 3. The exactly accepted Round 19 addition

Define

$$
\rho_0=\frac1{\sqrt{337}},
\qquad
\rho_c=\frac1{1+2\pi},
\qquad
L(\rho)=\frac1{2\rho},
\qquad
d=\frac{\sqrt{337}}2,
$$

$$
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\tag{2}
$$

Round 20 adds to the opaque $\mathcal A_{18}$ exactly the accepted closed
Round 19 cover

$$
\mathcal P_{19}^{\rm low}
=\left\{\rho_0<\rho<\rho_c,
\quad L(\rho)<K\le d\right\},
\tag{3}
$$

$$
\overline{\mathcal P}_{19}^{\rm high}
=\left\{\rho_c\le\rho\le\frac78,
\quad z_\rho\le K\le k_6(\rho)\right\}.
\tag{4}
$$

Thus

$$
\boxed{
\mathcal A_{19}
=\mathcal A_{18}
\cup\mathcal P_{19}^{\rm low}
\cup\overline{\mathcal P}_{19}^{\rm high}.
}
\tag{5}
$$

The genuinely new subset relative to $\mathcal A_{18}$ is

$$
\mathcal C_{19}
=\left\{\rho_0<\rho<\rho_c,
L(\rho)<K\le d\right\}
\cup
\left\{\rho_c\le\rho<\frac78,
k_5(\rho)<K\le k_6(\rho)\right\}.
\tag{6}
$$

Equation (4), not a reconstruction of older bands, is used for the high
closed disjunct. This lets an independently decisive Round 19 band settle
an unresolved old $k_5$ attribution without changing any equality owner.

## 4. Exact normalized three-piece residual

Exact subtraction of (6) from the accepted $\mathcal D_{18}$ gives

$$
\boxed{
\begin{aligned}
\mathcal D_{19}={}&
\left\{\rho_*<\rho\le\rho_0,
\quad L(\rho)<K<U(\rho)\right\}\\
&\cup
\left\{\rho_0<\rho<\rho_c,
\quad d<K<U(\rho)\right\}\\
&\cup
\left\{\rho_c\le\rho<\frac78,
\quad k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}
}
\tag{7}
$$

At $\rho=\rho_0$, $L(\rho_0)=d$. The added lower fiber is empty there,
so this ratio face belongs to the first residual piece. At $\rho=\rho_c$,
the accepted high band owns all frequencies through $k_6$, and the ratio
face belongs to the third piece. Every frequency inequality displayed in
(7) is strict.

The exact witness

$$
(\rho,K)=\left(\frac12,30\right)\in\mathcal D_{19}
\tag{8}
$$

is retained. Hence this packet closes no theorem target.

## 5. Complete face ownership

| face or interface | frozen assignment |
|---|---|
| $\rho=\rho_*$ | complete small-hole endpoint; outside $\mathcal D_{19}$ |
| $\rho=\rho_0$ | first residual piece; $L=d$ and the new lower fiber is empty |
| $\rho=\rho_{HK}$ | inherited shared $H_0=K_0$ upper face; implementation selects $K_0$ |
| $\rho=\omega_0$ | inherited $H_0$ eligibility endpoint; $K_0$ is active |
| $\rho=\rho_c$ | third residual piece; accepted high owner covers through $k_6$ |
| $\rho=1/2$ | continuous inherited $K_0$ formula interface |
| $\rho=5/6$ | inherited seam-$54$ owner begins inclusively |
| $\rho=7/8$ | complete thin endpoint; outside $\mathcal D_{19}$ |
| $K=L(\rho)$ below $\rho_c$ | inherited high-angular owner; excluded from the residual |
| $K=d$ for $\rho_0<\rho<\rho_c$ | Round 19 lower staircase owner |
| $K=z_\rho$ | inherited phase-zero owner |
| $K=k_5(\rho)$ | Round 18 staircase owner |
| $K=k_6(\rho)$ at or above $\rho_c$ | Round 19 high staircase owner |
| $K=U(\rho)$ | active inherited upper-floor owner; excluded from the residual |
| $K=295^2$ | Round 16 all-ratio high-frequency owner |

## 6. B0/B1 absorption and theorem-wise uncovered set

Retain the closed regression boxes

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

The accepted relations are

$$
B_0\subset\mathcal C_{17}\subset\mathcal A_{18}\subset\mathcal A_{19},
\qquad
B_1\subset\mathcal C_{17}\subset\mathcal A_{18}\subset\mathcal A_{19}.
$$

Neither box is subtracted again. Therefore

$$
\boxed{
\mathcal U_{19}
=\left(I_{19}\times[0,\infty)\right)
\setminus\left(\mathcal A_{19}\cup B_0\cup B_1\right)
=\mathcal D_{19}.
}
\tag{9}
$$

## 7. Executable signs and tri-state policy

For rational $\rho>0$ and $K\ge0$, the new algebraic comparisons are
exact:

$$
\operatorname{sgn}(\rho-\rho_0)
=\operatorname{sgn}(337\rho^2-1),
$$

$$
\operatorname{sgn}(K-L(\rho))
=\operatorname{sgn}(2\rho K-1),
$$

$$
\operatorname{sgn}(d^2-K^2)
=\operatorname{sgn}(337-4K^2).
\tag{10}
$$

The inherited precision-escalated Arb policy evaluates

$$
\rho(1+2\pi)-1,
\qquad
(1-\rho)K-\pi,
\qquad
\pi^2+(42-K^2)(1-\rho)^2,
\tag{11}
$$

and every active upper-floor sign. A material unresolved comparison returns
`indeterminate`. A false conjunction factor suppresses irrelevant unknown
signs, and a true disjunct settles a union. An unresolved mandatory compact
gate cannot be overridden.

The classifier uses the authenticated order $\rho_0<\rho_c$. If the
$\rho_c$ side is unresolved but the middle threshold $K>d$ and the high
threshold $K>k_6(\rho)$ give the same truth value, that common value settles
residual membership. If they differ, the result remains `indeterminate`.

The executable classifier independently compares the complement of (5)
with (7) and raises on a decided disagreement. Its permanent tests include
symbolic equality truth tables, exact rational side checks, Arb
indeterminacy probes at $\rho_*$, $\rho_c$, $z_\rho$, $k_5$, $k_6$, and
$K_0$, all closed $B_0/B_1$ corners, all ratio owners, every strict or
included frequency face, and the nonempty witness (8).

## 8. Release rule

The packet, executable classifier, and tests named by the separate Round 20
freeze record are immutable after release. Any correction requires a
replacement packet, classifier, tests, and freeze record with new hashes.

Only after an independent audit of this exact mask may a Round 20 candidate
be frozen. Such a candidate must target subsets of (7) and must not cite
this set classification as a spectral proof.
