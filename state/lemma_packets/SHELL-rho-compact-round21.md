# Lemma Packet: Exact Round 21 Post-Round-20 Residual Mask

Status: **FROZEN RESIDUAL MAP / NO NEW THEOREM**.

Round: 21.

Primary obligations: **SHELL-rho-compact** and
**COMP-certified-bessel**.

Baseline commit:
`e739a1cfcc5ce6647d70f2ddbc09598da4f496aa`.

This packet freezes the accepted state after application of the Round 20
State Patch and the repaired independent derived-state audit. It performs
exact set subtraction only. It does not use a Round 21 route, executable
certificate, exploratory synthesis, or proposed closure theorem. It does
not claim that the residual is empty and changes no obligation status.

## 1. Authenticated accepted state

The executable manifest authenticates the following fixed chain.

| artifact | SHA-256 |
|---|---|
| `state/proof_obligations.yml` | `313eed3a0f789e83fbd809c787590de80cb40946f307f50fd3eba53735d355bd` |
| `state/next_round_prompts.md` | `61341748ef07a6e937f752140b407a83576ae69c62061c1c28ae488acf43e4d2` |
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `e8d1ad7ab01e8140e1abb4663eb8b5ca9d708f79de31696e29486a4212443a61` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze.md` | `aa1484a886f5e6b96962464154dde488af6acdf87823fe01c62f8ec436790e87` |
| `rounds/polya-main/round_020/reviews/candidate-freeze-independent-audit.md` | `819701c2c2accf5d86f4188a920f901ef6a0658f7d515a104c67d18f505bd467` |
| `rounds/polya-main/round_020/reviews/candidate-replacement-final-byte-audit.md` | `01ad99bfeb5512ac4efc587ed79f10048bf7271f04b7f97cbf4f2400e030a43c` |
| `rounds/polya-main/round_020/reviews/combined-closure-clean-room.md` | `7f871c20d17fbd82d5b035899e3a1d7b452eadf8a9f9c1717eeb3a6538c3aadb` |
| `rounds/polya-main/round_020/reviews/combined-closure-clean-room-addendum.md` | `7f69c793bb791fdde92466f4bcd7ab8dc364a70564fa142d08b0ae0cc1b3022c` |
| `rounds/polya-main/round_020/reviews/combined-closure-zero-provenance.md` | `2ef25981cbd210c4bc0105a7e31be8f242113daf5f19980a1f39f197fa14efd8` |
| `computations/round20_verify_combined_closure.py` | `086beb09a7eddb6c936e9d47377b84d3dfb9050aaee16adef2102de2ddbe1cd5` |
| `computations/tests/test_round20_verify_combined_closure.py` | `4936f4ef3afeccd1963af492d2c80eef6c46ed852ce75d0f08d8cbcee24360cf` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-replacement.md` | `df56599ffce027c608e1ee7dd67a9aa1e5791002b392e4a32a9b3a0ed648ef95` |
| `rounds/polya-main/round_020/reviews/combined-closure-constants-final-audit.md` | `6322802e8ce528b96e6e4e170784aa5811931fde1173391f8d85de86c360e5ae` |
| `rounds/polya-main/round_020/reviews/combined-closure-cross-comparison.md` | `4b7a7810a12177002f24a16ef60a206669e07fa29e80c3018d2b85add5d1099b` |
| `rounds/polya-main/round_020/reviews/combined-closure-adversarial-referee.md` | `acea3818e562a8bc27496f1c727835f7a08e70ce60aaa28946fb8999ddf6c9cc` |
| `sources/round20_bessel_zero_bounds.md` | `2534c1cb00545e7e4c42f28878e962dd8454a56564131ec5150affd33a2b7ec3` |
| `sources/round20_higher_radial_zero_bounds.md` | `8a8dae42d890bf8f918324e8ae6cbaa7e2a821fee54c00c7f11238efaa3df2c7` |
| `sources/round20_k10_zero_bounds.md` | `a0ac0c441f01708dad404c3ad7d86ce7dcc48cbaa38b8f854aab5fa1cac11926` |
| `sources/round20_k11_zero_bounds.md` | `eee1ff26b58bb6f438cc8d970cb946817164c65b968f6adbf57b6d7a2a7db240` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| first preserved A4 failure | `4957681e290698a2e5b8068ab663a8700983bd27d4e24d6e1c2da4f489e085fd` |
| second preserved A4 failure | `52a9b81ac4e36942eee153999ab61b1365bc9c72c08f5f83b4d6c61e38adbc31` |
| `rounds/polya-main/round_020/judge/judge-020.md` | `3acd0b9aec2aaa52f791bd8656cf6b53327c11eed5f3c4c51fe8352bee9782fa` |
| `rounds/polya-main/round_020/reviews/state-patch-final-audit.md` | `9a4ef5abbdf06d54a0d3c22fc9ff3c87ab3b6f44830c378b1edc6368a23c677f` |
| preserved derived-state failure | `9c7a0dc453eea72bc571b99a11743d23ab42d1910f18e2b20c1dd0780eb752f9` |
| `rounds/polya-main/round_020/reviews/derived-state-replacement-audit.md` | `671cee8be91964efe0294eba01494cf11065ddbafdad1cc8e9885520ff3e353c` |

The graph and prompt hashes are Git-blob identities at the baseline commit.
Permanent tests authenticate those blobs instead of mutable future live
paths. All other rows are immutable committed files and are checked against
their live bytes. The two failed audits are retained as negative chronology;
only the repaired final A4 bundle and derived-state replacement PASS support
the accepted state.

## 2. Accepted Round 20 cover

Retain

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\tag{1}
$$

The imported Round 20 classifier is the opaque accepted $\mathcal A_{19}$
base. Round 20 adds exactly the following accepted theorem domains.

First, it closes both lower components

$$
\mathcal D_{19}^{\rm low}
=\{\rho_*<\rho\le\rho_0,\ L(\rho)<K<U(\rho)\}
\cup
\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}.
\tag{2}
$$

Second, it proves the closed staircase

$$
\rho_c\le\rho\le\frac78,
\qquad
z_\rho\le K\le k_{11}(\rho).
\tag{3}
$$

Third, it proves the all-frequency optical theorem

$$
\frac{39}{50}\le\rho<1,
\qquad
K\ge0.
\tag{4}
$$

Thus the genuinely new subset of the historical $\mathcal D_{19}$ is

$$
\boxed{
\begin{aligned}
\mathcal C_{20}={}&\mathcal D_{19}^{\rm low}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K\le k_{11}(\rho)\}\\
&\cup\{39/50\le\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
\end{aligned}}
\tag{5}
$$

Equation (3), rather than a reconstruction of the older staircase, is used
as the executable closed high disjunct. Equation (4) is not truncated at
$7/8$; it also classifies optical ratios outside the historical compact
interval.

## 3. Exact live upper floor

The inherited upper floor is

$$
U(\rho)=\min\left(
\{K_0(\rho)\}
\cup\{H_0(\rho):\rho<\omega_0\}
\cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge\frac56\right\}
\right).
\tag{6}
$$

On the live ratio interval, $\rho\ge\rho_c>\omega_0$, so the $H_0$
branch is ineligible. Also

$$
\rho<\frac{39}{50}<\frac56,
$$

so the seam branch is ineligible. Therefore

$$
\boxed{U(\rho)=K_0(\rho)
\quad\left(\rho_c\le\rho<\frac{39}{50}\right).}
\tag{7}
$$

The executable predicate evaluates $K_0-K$ directly and, at every decided
rational point in the live interval, independently replays the inherited
upper-floor classifier and requires it to select the `K0` branch with the
same strict side.

## 4. Exact normalized residual

Subtracting (5) from the accepted $\mathcal D_{19}$ gives exactly

$$
\boxed{
\mathcal D_{20}
=\left\{\rho_c\le\rho<\frac{39}{50},
\quad k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.}
\tag{8}
$$

This is a single ratio-frequency cell. Its left ratio face is included; its
right ratio face is excluded. Both frequency inequalities are strict.

The exact retained witness is

$$
\left(\rho,K\right)=\left(\frac12,30\right).
\tag{9}
$$

Indeed, the accepted bounds give

$$
\rho_c<\frac12<\frac{39}{50},
\qquad
k_{11}(1/2)<14<30<64<K_0(1/2)=U(1/2).
\tag{10}
$$

Hence this packet freezes a nonempty residual and closes no target.

## 5. Complete face ownership

| face or interface | frozen assignment |
|---|---|
| $\rho=\rho_c$ | included in $\mathcal D_{20}$ only strictly above $k_{11}$ |
| $\rho=39/50$ | Round 20 all-frequency optical owner; excluded from $\mathcal D_{20}$ |
| $K=k_{11}(\rho)$ | Round 20 closed staircase owner; excluded from $\mathcal D_{20}$ |
| $K=K_0(\rho)=U(\rho)$ | inherited fixed-ratio high-energy owner; excluded from $\mathcal D_{20}$ |
| $\rho=\rho_*$ | inherited complete small-hole endpoint |
| $\rho=\rho_0$ | removed with the complete Round 20 lower closure |
| $\rho=7/8$ | inherited complete thin endpoint; optical and staircase overlap it |
| $K=L(\rho)$ and $K=d$ | inherited/Round 19 lower owners, already outside $\mathcal D_{19}^{\rm low}$ |
| $K=z_\rho$ and $K=k_6(\rho)$ | predecessor staircase owners |
| $K=295^2$ | Round 16 all-ratio high-frequency owner |
| $K=0$ on optical ratios | optical equality face; the comparison is strict for $K>0$ |

The classifier preserves predecessor reasons whenever an older owner already
settles a point. Thus the complete endpoint and high-frequency owners are
not relabelled merely because the stronger optical theorem overlaps them.

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
B_0\subset\mathcal C_{17}\subset\mathcal A_{19}\subset\mathcal A_{20},
\qquad
B_1\subset\mathcal C_{17}\subset\mathcal A_{19}\subset\mathcal A_{20}.
$$

Neither box is subtracted again. Therefore

$$
\boxed{\mathcal U_{20}=\mathcal D_{20}.}
\tag{11}
$$

## 7. Executable signs and tri-state policy

For rational queries, the optical ratio sign is exact:

$$
\operatorname{sgn}\left(\rho-\frac{39}{50}\right)
=\operatorname{sgn}(50\rho-39).
\tag{12}
$$

The precision-escalated Arb policy evaluates

$$
\rho(1+2\pi)-1,
\qquad
\pi^2+\bigl(132-K^2\bigr)(1-\rho)^2,
\qquad
K_0(\rho)-K.
\tag{13}
$$

These are respectively the sides of $\rho_c$, $k_{11}$, and $K_0$.
The normalized truth table is

$$
\bigl[\rho\ge\rho_c\bigr]
\wedge
\bigl[\rho<39/50\bigr]
\wedge
\bigl[K>k_{11}(\rho)\bigr]
\wedge
\bigl[K<K_0(\rho)\bigr].
\tag{14}
$$

A false factor suppresses irrelevant unknown signs. Otherwise a material
unresolved comparison returns `indeterminate`; no midpoint or floating-point
guess is permitted. The complement classifier independently adds (2)--(4)
to opaque $\mathcal A_{19}$ and raises on every decided disagreement with
(14).

Permanent tests exhaust the strong-Kleene sign table and check the included
$\rho_c$ face, excluded $39/50$ face, excluded $k_{11}$ and $K_0=U$ faces,
the witness, both regression boxes, old endpoints, high-energy owners,
deliberate indeterminacy at all irrational walls, and baseline-byte
authentication.

## 8. Release rule

The packet, executable classifier, tests, and separate freeze record are
pre-candidate bookkeeping artifacts. An independent residual-mask auditor
must authenticate their exact bytes and reproduce the subtraction before a
Round 21 candidate can be frozen.

Any correction requires replacement packet, classifier, tests, and freeze
record hashes. This packet supplies no spectral proof and authorizes no
claim about a successor residual.
