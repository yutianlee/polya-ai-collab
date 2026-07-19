# Round 20 Candidate-Freeze Independent Audit

Verdict: **PASS**.

First issue: **none**.

This is a proof-free release-gate audit of the Round 20 draft candidate and
its draft freeze record. It checks identity, input isolation, statement
scope, face ownership, and exact proposed set subtraction. It does not
verify any proposed spectral estimate, Bessel-zero inequality, inventory,
cap, Weyl payment, or optical constant.

## 1. Exact draft bytes and baseline

The supplied bytes reproduce the requested SHA-256 identities:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-combined-closure-round20-claim.md` | `be5a9f5792495f5ede3a558f1e31e0c428efb3a34f6ef3008423693b90d59949` |
| `rounds/polya-main/round_020/exploration/candidate-claim-freeze-draft.md` | `dd9d9fdaf47315abf72cbaeaa2e312874972ae7f8dd3eee57a0280f81528e0e3` |

The declared baseline resolves exactly to
`56e8d71ad3df2da6ab47ab1fefb8d758e076c69b`. Every residual artifact,
permitted foundational input, and excluded-gate metadata path named by the
draft exists at that commit, and its baseline blob has the same SHA-256 as
the current authenticated byte stream.

The five residual identities all reproduce exactly:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round20.md` | `a62222506ed6f9197ed8338624a75382b2a1bc1245d75abcad0f85930f7328a8` |
| `computations/round20_residual_mask.py` | `5d33e0f20035a4f5e3c6d4d03d65f6949780ac4d97611ea957568c2051d545e2` |
| `computations/tests/test_round20_residual_mask.py` | `d261c89d61bced6c2630596f8bbfa66ae188257b656890c98c4654de765e0164` |
| `rounds/polya-main/round_020/exploration/residual-mask-freeze.md` | `172127510ee2a79ae8d0856cc3b8fc467189025b37f7f1938f927be1768285a7` |
| `rounds/polya-main/round_020/reviews/residual-mask-independent-audit.md` | `b111f4ef1026c05870889e194a462b726eb1fe99838364dff9d91f887bf9427f` |

The frozen residual in those bytes is exactly

$$
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\leq\rho_0,\ L(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
$$

Thus the candidate starts from the released pre-candidate mask and does not
silently import a prospective Round 20 cover.

## 2. Permitted and excluded input boundary

All ten foundational packet/source-card hashes in Section 7 reproduce
exactly:

| artifact | reproduced SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-weighted-lattice-fractional.md` | `a4f56f864b8ee6fed6dbbb51d7d23d5871193cd4b66e2d1af79990805863a47c` |
| `state/lemma_packets/SHELL-low-interface-small-hole.md` | `071335167d4f6e4c6a5b30a0a85f2274a1921a05bf5dbf990a614c920a3e931a` |
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `sources/annuli_polya.md` | `951638839f37e574acc5167e3458a0fa5e2fd38a982bdd64f299db9c9280bc57` |
| `sources/flps_balls.md` | `27ec69e8a4b49c0d44ac1077c80eea3c1264150c6d06caeb1f3763b95be62a38` |
| `sources/lorch_bessel_zeros.md` | `85f9a009811c5626e837446e2635ccbbca652ee192ccd524defc69a5952f4ce4` |
| `sources/shell_weyl_bessel.md` | `ce035399038309e0bc7a5bacf29fce4f292fc43491b82d34912bd1f6fcf98ade` |
| `sources/bessel_phase_enclosures.md` | `e1cbdef3b2461258a2ac399dc86f17400181378e38cc4bd9d1319e60c5597f9c` |

The source scopes are narrow and explicit. In particular, Lorch is limited
to the printed general first-zero inequalities; higher radial zeros,
half-integer specializations, radical comparisons, shell-to-ball and
angular propagation, tangent-cell enumeration, strict root location, and
ODE simplicity remain reconstruction obligations. The DLMF allowance is
limited to the four labelled identities/sections and authorizes identities,
not zero locations. The Round 16 endpoint packet supplies identities but no
enlarged-ratio conclusion.

The separate `k_11` gate record exists at the baseline and reproduces the
declared SHA-256
`515b57f7ad4c34a277c781770a7b60945fd345558ce5d4f592439e83fbd1a333`.
I checked only that excluded record's path and hash, not its contents. I
likewise checked only baseline path existence for the four explicitly named
Round 20 zero-bound source proofs. None of those files, no Round 20
exploration proof, incumbent response, constant ledger, script, sampled
computation, audit, cross-review, repository diff, or judge draft appears in
the permitted A3 input table. The gate record and every artifact it reviews
are expressly excluded from A3.

The candidate contains proposed statements, constants, inventories, and
falsification obligations, but no derivation, executable certificate,
sampled root, proof verdict, or review conclusion. Every potentially
proof-bearing Round 20 assertion is labelled as a proposed fact to be
reconstructed. I found no incumbent-proof or review leakage into the first
clean-room input set.

## 3. Exact three theorem claims and genuinely new cover

The candidate states exactly three theorem claims:

1. strict closure on both components of
   $\mathcal D_{19}^{\rm low}$;
2. a strict closed high staircase on
   $\rho_c\leq\rho\leq7/8$ and $z_\rho\leq K\leq k_{11}(\rho)$;
3. the all-frequency optical comparison on
   $39/50\leq\rho<1$ and $K\geq0$, with equality only at $K=0$ and a
   strict comparison for every $K>0$.

Relative to the accepted mask, the exact genuinely new proposed cover is

$$
\boxed{
\mathcal C_{20}=
\mathcal D_{19}^{\rm low}
\cup\mathcal C_{20}^{\rm stair}
\cup\mathcal C_{20}^{\rm opt},
}
$$

where

$$
\mathcal C_{20}^{\rm stair}
=\{\rho_c\leq\rho<7/8,\ k_6(\rho)<K\leq k_{11}(\rho)\},
$$

$$
\mathcal C_{20}^{\rm opt}
=\{39/50\leq\rho<7/8,\ k_{11}(\rho)<K<U(\rho)\}.
$$

This union is the one appearing in the proposed subtraction. The broader
closed staircase and optical theorem statements deliberately overlap
accepted owners; only the two displayed high pieces and the live lower
residual are new. The candidate neither reclaims the accepted band through
$k_6$ nor treats the already complete $\rho=7/8$ fiber as new.

## 4. Face ownership and exact subtraction

The proposed new pieces have the following exact ownership:

| face | assignment |
|---|---|
| $\rho=\rho_0$ | first lower component, with $L(\rho_0)=d$ |
| $\rho=\rho_c$ | high staircase side |
| $\rho=39/50$ | optical side for $K>k_{11}$ |
| $\rho=7/8$ | outside the live residual; not in the genuinely new cover |
| $K=L$ or $K=d$ | excluded from the lower residual and retained by predecessors |
| $K=k_6$ | excluded from the new staircase and retained by the predecessor |
| $K=k_{11}$ | included in the staircase; excluded from optical and residual pieces |
| $K=U$ | excluded from the accepted residual and from every new subtraction piece |
| $K=0$ in the optical theorem | included, with both sides exactly zero |
| $K>0$ in the optical theorem | proposed comparison is strict |

Subject to reconstruction of the explicitly proposed bookkeeping facts

$$
\rho_*<\rho_0<\sigma<\rho_c<39/50<7/8,
\qquad k_{11}<U,
\qquad U=K_0\ \text{on }[\rho_c,39/50),
$$

the subtraction is exhaustive and face-correct. The lower claim removes
both lower disjuncts. On
$\rho_c\leq\rho<39/50$, the staircase removes
$k_6<K\leq k_{11}$ and leaves exactly $k_{11}<K<U=K_0$. On
$39/50\leq\rho<7/8$, the staircase and optical pieces meet without a gap
at $K=k_{11}$ and remove the whole live high fiber. Hence

$$
\mathcal D_{19}\setminus\mathcal C_{20}
=\left\{\rho_c\leq\rho<\frac{39}{50},\
k_{11}(\rho)<K<K_0(\rho)=U(\rho)\right\}.
$$

No endpoint is subtracted twice, and the absorbed regression boxes
$B_0,B_1$ are not reintroduced.

## 5. Reconstruction and falsification completeness

The packet makes every route component a reconstruction obligation rather
than an allowed lemma: the shifted-tail wedge and its floor/remainder
strictness; all six finite lower cells; the exceptional floor cell and
cap-395 proxy; channel, ball, and angular comparisons with their form-domain
directions; every internal zero in the registry; all five high checkpoints,
cap cells, incompatibilities, and payments; and both optical screens,
product deficit, endpoint reserves, and common split face.

The mandatory falsification registry covers:

- every ratio endpoint, source switch, and one-sided trace used by the
  proposed cover;
- every lower fixed or moving frequency wall and every ordering change;
- $z_\rho$, $k_6$ through $k_{11}$, all rational zero walls, every listed
  rational localization, and all three algebraic splits;
- $K=0$, $a=\pi$, all $a=m\pi$ conventions, angular and phase equalities,
  the optical common face, and $\varepsilon=11/50$;
- all relevant radial/angular boundary indices, multiplicities,
  cross-channel coincidences, tangent half-periods, positive-root
  enumeration, form domains, strict directions, cap cells, Weyl payments,
  half-integer floor conventions, omitted tails, and exact subtraction.

It also requires the first unsupported implication on `FAIL`, authentication
before reading, an initial verdict before any excluded artifact is opened,
and independent reconstruction rather than agreement with a table. This is
an adequate exhaustive falsification contract for the frozen claims.

## 6. Byte and release hygiene

Both draft files decode as strict UTF-8, have LF line endings and a final
newline, and contain no BOM, replacement character, forbidden control byte,
tab, or trailing whitespace. Display-math delimiters and raw braces are
balanced. The freeze draft authenticates the candidate hash and repeats the
same permitted-input boundary; it exposes only excluded gate metadata, not
excluded proof content.

The status and release language is internally consistent: neither draft is
presented as frozen, proved, promoted, or released. A status-only
finalization may therefore freeze these claim bytes after root approval;
any substantive candidate edit requires a new candidate hash and a repeated
gate audit.

## Final decision

**PASS; first issue: none.** The two exact draft byte streams form a
coherent, proof-free candidate gate against baseline `56e8d71`. They isolate
all Round 20 proof-bearing incumbents from A3, state exactly the three
proposed theorem claims and the genuinely new cover, preserve every strict
or inclusive face including the $K=0$ convention, and subtract exactly to
$\{\rho_c\leq\rho<39/50,\ k_{11}<K<K_0=U\}$, conditional only on the
reconstruction obligations explicitly assigned to the independent
reviewers.
