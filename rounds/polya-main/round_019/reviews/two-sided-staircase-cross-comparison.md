# Round 19 Two-Sided Staircase Cross-Comparison

Date: 2026-07-14.

Verdict: **PASS / RELEASE FOR FRESH ADVERSARIAL REVIEW**.

First discrepancy affecting the frozen claim: **none**.

This comparison was performed only after the isolated A3 and A4 initial
verdicts were complete. It compares their independently reconstructed
arguments with the two incumbent workstreams and the frozen candidate. It
does not replace the required fresh-referee gate.

## 1. Authenticated artifacts

| role | artifact | SHA-256 |
|---|---|---|
| frozen candidate | `state/lemma_packets/SHELL-two-sided-staircase-round19-claim.md` | `87544e727737ddf6a949284bb1ff4b01c7313fea5cff9dd874cd7f942a0ab6db` |
| candidate freeze | `rounds/polya-main/round_019/exploration/candidate-claim-freeze.md` | `7bd2bd5eb2ea898d5fa2abd34cb10a083aa04782587116915992a34c8a711eff` |
| high-ratio incumbent | `rounds/polya-main/round_019/responses/high-ratio-k6-incumbent.md` | `b9a86f1411a8e63c30b6ae5e2b3a65e167426f0b72a4447d15d4e833c5df6983` |
| lower-ratio incumbent | `rounds/polya-main/round_019/exploration/lower-ratio-route.md` | `1a4cd1eb93c286816346ead50edef0f151f8b1a287186ba3b20e37336c16b681` |
| isolated A3 reconstruction | `rounds/polya-main/round_019/reviews/two-sided-staircase-clean-room.md` | `24e487fc251f5d493cf2111a783e4a6d8c56df5d1f36089089c57200acc87e17` |
| independent A4 verifier | `computations/round19_verify_two_sided_staircase.py` | `4070c052f0e510ef207e0c42f15acb7838a5b7aebeabb7d72958e9897ca83b23` |
| A4 focused tests | `computations/tests/test_round19_verify_two_sided_staircase.py` | `1eea93d6f9d1c5efb09150e81f8c2211bd67d3338066ef1c29eb46977f43cb08` |
| A4 report | `rounds/polya-main/round_019/reviews/two-sided-staircase-constants.md` | `fbe2be74ec363341b48ee40d9efc39aa3b1db33130e656ddb00fbf3205f1d9e7` |
| zero-dependency audit | `rounds/polya-main/round_019/exploration/new-zero-dependency-audit.md` | `ab07f84c2f8bd31b7a792f69561c2bc15c8a8838ae196b7d9d0dd87d0a6de718` |

A3 and A4 each authenticated the candidate, its freeze record, and exactly
the six whitelisted dependencies before reading any excluded Round 19
artifact. Their initial verdicts were both PASS. A3 read no incumbent,
computation, source-audit review, cross-review, or judge artifact. A4 read no
incumbent, clean-room review, prior computation, cross-review, or judge
artifact.

## 2. High-ratio comparison

All three analytic routes agree on the exact closed theorem band

$$
\rho_c\leq\rho\leq\frac78,
\qquad z_\rho\leq K\leq k_6(\rho),
$$

and on the genuinely new set

$$
\rho_c\leq\rho<\frac78,
\qquad k_5(\rho)<K\leq k_6(\rho).
$$

They independently obtain the same exhaustive inventories:

- on $\rho_c\leq\rho\leq1/4$, first modes $0\leq\ell\leq4$ and only the
  possible second modes $(0,2),(1,2)$;
- on $1/4\leq\rho\leq7/8$, only first modes $0\leq\ell\leq5$.

The cumulative caps agree exactly: delayed first-mode caps
$4,9,16,25$, then radial caps $26,29$, and the $\ell=5$ cap $36$.
The incumbent and A3 both prove the fixed/moving bridges at
$3/10,1/2,1/2,1/5,13/25$ and explicitly avoid the false shortcut
$\mathcal W(\rho,k_5)>25$ near $\rho_c$. A4 independently reproduces all
finite reserves and the derivative-numerator reductions. Its executable
reports 245 exact checks overall and no failed finite obligation.

All routes assign equality consistently at $2z_\rho$, $p_1$, every fixed
zero threshold, $k_5$, and the included $k_6$ face. They prove
$k_6<U$ on the active $K_0$ and seam branches by different valid coarse
bounds. No route carries a stale one-radial-mode cap across $2z_\rho$.

## 3. Lower-ratio comparison

All routes agree on

$$
\frac1{\sqrt{337}}<\rho<\rho_c,
\qquad \frac1{2\rho}<K\leq\frac{\sqrt{337}}2.
$$

They reconstruct the same fixed-channel zero-extension comparison, the same
ball angular-shift min--max inequality, and the same complete internal proof
of $j_{5/2,2}>9$. Consequently they agree that, through the included upper
face, only first modes $0\leq\ell\leq5$ and possible second modes
$0\leq\ell\leq2$ remain; all $n\geq3$, first $\ell\geq6$, and second
$\ell\geq3$ modes are absent.

The ten strict-count caps agree exactly:

$$
1,4,9,10,16,17,26,29,40,45.
$$

The incumbent uses the uniform fixed-frequency bound
$38c^3/539$; A3 uses the independent stronger bound obtained from
$\rho_c<7/50$; A4 uses directed endpoints of its Machin enclosure. Every
route pays every cap strictly and assigns the moving $2z_\rho$ face to the
lower-count side. A4 checks 50 lower-cap cases, including all fixed faces
and three relative positions of $2z_\rho$.

All routes prove $d<U$ on both active low-ratio upper-floor branches and
agree that $\rho=1/\sqrt{337}$ has the empty candidate fiber $L=d$.

## 4. Provenance and source scope

The only new externally authenticated statements are

$$
j_{11/2,1}>\frac{17}{2},
\qquad
j_{3/2,2}>\frac{77}{10}.
$$

The first is the declared $\nu=11/2$ specialization of the published
Lorch inequality; the second is internally reconstructed from
$\tan x=x$. The shell-to-ball comparison, the ball angular shift,
$j_{5/2,2}>9$, all multiplicities, all shell exclusions, and all Weyl
payments remain internal. No route attributes a shell cross-product zero or
a new order/radial index to Lorch or DLMF.

## 5. Exact subtraction and faces

The incumbents, A3, and A4 agree on the exact post-candidate residual

$$
\begin{aligned}
\mathcal D_{19}={}&
\left\{\rho_*<\rho\leq\frac1{\sqrt{337}},
\ L(\rho)<K<U(\rho)\right\}\\
&\cup\left\{\frac1{\sqrt{337}}<\rho<\rho_c,
\ d<K<U(\rho)\right\}\\
&\cup\left\{\rho_c\leq\rho<\frac78,
\ k_6(\rho)<K<U(\rho)\right\}.
\end{aligned}
$$

A4 exhausts 63 ratio/frequency face cases and ten admissible absorbed-box
Boolean cases. Thus $B_0$ and $B_1$ remain inherited covered regression
artifacts and are not subtracted again. The faces $K=d$ and $K=k_6$ are
newly covered; $K=U$, $\rho=\rho_*$, and $\rho=7/8$ retain their inherited
owners.

## 6. Resolved non-mathematical discrepancies

Before the candidate freeze, two malformed TeX sequences in the lower
incumbent were repaired and the strengthened bytes were independently
audited. After the isolated verdicts, one missing TeX backslash in each
human-readable review was repaired. These were presentation-only changes;
the frozen candidate, verifier, tests, formulas, constants, and verdicts
were unchanged. Control-byte scans and `git diff --check` pass.

No mathematical discrepancy remains. The immutable candidate therefore
does not require replacement or a repeated A3/A4 cycle.

## 7. Release decision

The Round 19 candidate is released to a fresh referee who participated in
neither incumbent development nor clean-room reconstruction. That referee
must assume the candidate false, recheck every source boundary, spectral
inventory, payment, upper-floor comparison, equality face, and residual
subtraction, and identify the first unsupported implication. Promotion is
not authorized before that independent PASS.
