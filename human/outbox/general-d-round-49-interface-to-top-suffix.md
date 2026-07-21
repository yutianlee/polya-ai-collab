# General dimension, Round 49: interface-to-top suffix

Date: 21 July 2026  
Role: Prompt A, lead analytic pass  
Verdict: **INCOMPLETE — TWO SUBSTANTIVE EXACT REDUCTIONS**

Round 49 does not prove or falsify the suffix theorem
\(\mathcal R_{\mathrm{suf}}\ge0\), its quantified fallback, or literal
\(\mathrm{WT}_4\) on the complete strict-active domain. It does prove:

1. the complete strict normalization (SPLIT), (NSFX), (SSFX), (IF), and
   (TOP), including all endpoint conventions;
2. the exact row-cone block and terminal-row analogue, with no discarded
   term;
3. an exact composite Peano identity whose only nonlocal term is one
   intrinsic curvature integral; and
4. a new one-crossing theorem: \(Q=2\sigma-z\sigma'\) has exactly one zero
   in \((\mu/\sqrt2,\mu)\).

These meet two of the packet's substantive-partial-success criteria. The
first unrepaired implication is the sign of the explicit Peano boundary
ledger plus its single shallow-curvature integral. No status changes are
authorized.

## 0. Preflight and authority

| item | verified value |
|---|---|
| repository | yutianlee/polya-ai-collab |
| branch | codex/general-d-round-49-interface-to-top-suffix |
| exact base and origin/main | 828799fad8b1bb7965570d708bc842844a674de1 |
| Round 48 content commit | ddf92b23fbb313b25a6814467e9cab19faca6617 |
| state Git blob | 2b54326263cbddd9ea5fa6340802bb9e5c48af6b |
| state SHA-256 | 33d799d41dc625681a4299be532e7648e87064d7bfe4a591982201d2e244a230 |
| full-outer Round 48 cell | proved_internal |
| deep-inner Round 48 cell | proved_internal |
| scoped \(d=4\) aggregate | proposed |
| all-dimensional aggregate | proposed |
| branching backbone | derived_under_assumptions |
| \(d=3\) target | proved_internal |
| general-dimensional target | proposed |

The opening headers of state/gap_register.md, human/current_directives.md,
and state/next_round_prompts.md retain stale workflow text. The Round 49
packet expressly forbids repairing those narrative headers in this branch.
They were not used to override state/proof_obligations.yml.

The user-supplied Round 49 packet was pre-existing and untracked. It was read
in full and left unchanged. Prompt A also read every mandatory source listed
in that packet: the authoritative state and strategy files, all three Round
47 reports, the Round 48 synthesis/audit/wave ledger, both certified lemma
packets and all six certification artifacts, and both Round 48
counterexample evaluators.

The completed three-dimensional theorem is frozen. The general-dimensional
theorem remains unproved. Pointwise Gate B, R45.18, and the continuous
quarter-node route are not reopened.

## 1. Exact notation and hypotheses

For \(0<\rho<1\), \(K>0\), and \(\mu=\rho K\), let

\[
 G_R(z)=
 \frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi}
 \quad(0\le z\le R)
\]

with zero extension, and put

\[
 A(z)=G_K(z)-G_\mu(z),\qquad
 [x]_<:=\max\{0,\lceil x\rceil-1\}.
\]

The strict-active domain is

\[
 0<\rho<1,\qquad
 K^2>\frac{\pi^2}{(1-\rho)^2}+\frac34.
 \tag{ACT}
\]

The algebra below needs only \(0<\mu<K\); (ACT) supplies the intended
spectral owner. Since \(A'(z)=-\sigma(z)<0\), \(A\) has a decreasing
inverse

\[
 \xi:[0,H]\longrightarrow[0,K],\qquad
 H=A(0)=\frac{K-\mu}{\pi}.
\]

Define

\[
 F(t)=\frac{\xi(t)^3}{3},\qquad
 t_n=n-\frac14,\qquad
 N_n=\lceil\xi(t_n)\rceil-1.
\]

The exact inverse-layer ledger from Round 48 is

\[
 W_4=\int_0^H F(t)\,dt,\qquad
 P_4^<=\sum_{t_n<H}S_2(N_n),
 \quad
 S_2(N)=\frac{N(N+1)(2N+1)}6.
 \tag{1.1}
\]

Let

\[
 \tau=A(\mu)=G_K(\mu),\qquad b=\lfloor\tau\rfloor.
\]

For a complete cell,

\[
 L_n=\int_{n-1}^{n}F(t)\,dt-S_2(N_n).
 \tag{1.2}
\]

## 2. Exact outer-prefix/suffix split

Because \(0\le b\le\tau<H\), all cells \(1\le n\le b\) are complete and
wholly outer, with the endpoint \(n=\tau\) allowed by the certified packet.
Split both terms of (1.1) at \(b\):

\[
\begin{aligned}
 \mathrm{WT}_4
 &=
 \left\{\int_0^bF-\sum_{n=1}^{b}S_2(N_n)\right\}\\
 &\quad+
 \left\{\int_b^HF-
 \sum_{\substack{n\ge b+1\\n-1/4<H}}S_2(N_n)\right\}.
\end{aligned}
\]

Hence, exactly,

\[
 \boxed{
 \mathrm{WT}_4=\sum_{n=1}^{b}L_n+\mathcal R_{\mathrm{suf}},}
 \tag{SPLIT}
\]

where

\[
 \boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_b^HF(t)\,dt-
 \sum_{\substack{n\ge b+1\\n-1/4<H}}S_2(N_n).}
 \tag{2.1}
\]

There is no missing node at \(b\). Nodes with \(n\le b\) belong to the
prefix, and all nodes with \(n\ge b+1\) belong to the suffix. If
\(\tau\in\mathbb Z\), then \(b=\tau\) and the last prefix cell ends at the
interface, exactly within the Round 48 outer lemma. If \(b=0\), the prefix
is empty and \(\mathcal R_{\mathrm{suf}}=\mathrm{WT}_4\).

The certified outer reserve gives

\[
 \mathcal R_{\mathrm{out}}
 :=
 \sum_{n=1}^{b}
 \left(\frac{19N_n}{48}+\frac{27}{128}\right),
 \tag{2.2}
\]

and therefore

\[
 \mathrm{WT}_4>
 \mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}
 \quad(b\ge1).
 \tag{2.3}
\]

For \(b=0\), (2.3) becomes equality with
\(\mathcal R_{\mathrm{out}}=0\). Thus both
\(\mathcal R_{\mathrm{suf}}\ge0\) and
\(\mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}\ge0\) are sufficient
for literal \(\mathrm{WT}_4\ge0\); neither is equivalent to it.

## 3. Clipped normalization

Put

\[
 B(z)=(A(z)-b)_+,\qquad
 \widehat H=H-b,\qquad
 R=\xi(b),\qquad
 \eta(s)=\xi(b+s).
\]

Writing \(n=b+k\) in (2.1) gives

\[
 \boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^{\widehat H}\frac{\eta(s)^3}{3}\,ds
 -
 \sum_{\substack{k\ge1\\k-1/4<\widehat H}}
 S_2\!\left(\lceil\eta(k-1/4)\rceil-1\right).}
 \tag{NSFX}
\]

In this display and below, the standalone minus line is ordinary
subtraction.

Layer cake gives

\[
 \int_0^{\widehat H}\frac{\eta(s)^3}{3}\,ds
 =
 \int_0^R z^2B(z)\,dz.
 \tag{3.1}
\]

For the discrete term, use

\[
 a<\eta(k-\tfrac14)
 \iff
 k-\tfrac14<B(a).
\]

Finite exchange then yields

\[
\begin{aligned}
 \sum_{k-1/4<\widehat H}S_2(M_k)
 &=
 \sum_{1\le a<R}a^2
 \#\{k\ge1:k<B(a)+\tfrac14\}\\
 &=
 \sum_{1\le a<R}a^2[B(a)+\tfrac14]_<,
\end{aligned}
 \tag{3.2}
\]

where \(M_k=\lceil\eta(k-1/4)\rceil-1\). Thus

\[
 \boxed{
 \mathcal R_{\mathrm{suf}}
 =
 \int_0^Rz^2B(z)\,dz
 -
 \sum_{1\le a<R}a^2[B(a)+\tfrac14]_<.}
 \tag{SSFX}
\]

At the interface,

\[
 \boxed{B(\mu)=\tau-b\in[0,1).}
 \tag{IF}
\]

Consequently only the first normalized row can meet both \(z>\mu\) and
\(z<\mu\). If \(B(\mu)=0\), even that row is inner apart from its endpoint.
If \(\widehat H<1\), the first normalized row is terminal; it is not a
second interface row.

## 4. Exact terminal ownership

Write

\[
 \widehat H=q+\alpha,\qquad
 q=\lfloor\widehat H\rfloor,\qquad0\le\alpha<1.
\]

For \(1\le k\le q\), put

\[
 M_k=\lceil\eta(k-\tfrac14)\rceil-1.
\]

There are exactly \(q\) complete rows. The terminal interval
\([q,q+\alpha]\) contains a quarter node precisely when
\(q+3/4<q+\alpha\), that is, precisely when \(\alpha>3/4\). Therefore

\[
\boxed{
\begin{aligned}
 \mathcal R_{\mathrm{suf}}
 &=
 \sum_{k=1}^{q}
 \left\{\int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds-S_2(M_k)\right\}
 +T_{\mathrm{top}},\\
 T_{\mathrm{top}}
 &=
 \int_q^{q+\alpha}\frac{\eta(s)^3}{3}\,ds\\
 &\quad-
 \mathbf1_{\{\alpha>3/4\}}
 S_2\!\left(\lceil\eta(q+3/4)\rceil-1\right).
\end{aligned}}
 \tag{TOP}
\]

At \(\alpha=3/4\), strict ownership excludes the node. If
\(\widehat H<3/4\), there is no complete row and no node, so the suffix is
the strictly positive top integral.

## 5. Exact row-cone block

For a complete row define

\[
 \omega_k(z)=
 \min\{1,\max\{0,B(z)-k+1\}\}.
\]

Fubini's theorem gives

\[
 \boxed{
 \int_{k-1}^{k}\frac{\eta(s)^3}{3}\,ds
 =
 \int_0^Rz^2\omega_k(z)\,dz.}
 \tag{ROW1}
\]

For every integer \(M\ge0\),

\[
 \int_{1/2}^{M+1/2}z^2\,dz
 =
 \sum_{a=1}^{M}\int_{a-1/2}^{a+1/2}z^2\,dz
 =
 S_2(M)+\frac{M}{12}.
\]

Hence

\[
 \boxed{
 S_2(M)
 =
 \int_{1/2}^{M+1/2}z^2\,dz-\frac{M}{12}.}
 \tag{ROW2}
\]

Combining (ROW1)--(ROW2),

\[
 \boxed{
 L_k^{\mathrm{suf}}
 =
 \int_0^Rz^2
 \left(
 \omega_k(z)-
 \mathbf1_{[1/2,M_k+1/2]}(z)
 \right)dz
 +\frac{M_k}{12}.}
 \tag{ROW3}
\]

For the terminal row put

\[
 \omega_{\mathrm{top}}(z)
 =
 \min\{\alpha,\max\{0,B(z)-q\}\}.
\]

Then

\[
 T_{\mathrm{top}}
 =
 \int_0^Rz^2\omega_{\mathrm{top}}(z)\,dz
\]

when \(\alpha\le3/4\), while for \(\alpha>3/4\),

\[
\begin{aligned}
 T_{\mathrm{top}}
 &=
 \int_0^Rz^2
 \left(
 \omega_{\mathrm{top}}(z)-
 \mathbf1_{[1/2,M_{\mathrm{top}}+1/2]}(z)
 \right)dz
 +\frac{M_{\mathrm{top}}}{12},\\
 M_{\mathrm{top}}
 &=
 \lceil\eta(q+3/4)\rceil-1.
\end{aligned}
 \tag{5.1}
\]

Since

\[
 \sum_{k=1}^{q}\omega_k(z)+\omega_{\mathrm{top}}(z)=B(z),
\]

the whole block is

\[
\boxed{
\begin{aligned}
 \mathcal R_{\mathrm{suf}}
 &=
 \int_0^Rz^2\{B(z)-E(z)\}\,dz\\
 &\quad+
 \frac1{12}
 \left(
 \sum_{k=1}^{q}M_k+
 \mathbf1_{\{\alpha>3/4\}}M_{\mathrm{top}}
 \right),\\
 E(z)
 &=
 \sum_{k=1}^{q}
 \mathbf1_{[1/2,M_k+1/2]}(z)\\
 &\quad+
 \mathbf1_{\{\alpha>3/4\}}
 \mathbf1_{[1/2,M_{\mathrm{top}}+1/2]}(z).
\end{aligned}}
 \tag{RBLOCK}
\]

This formula contains the full continuous occupancy kernel, every literal
integer-row interval, every \(M/12\) correction, the unique interface-row
contribution, and the terminal contribution. No term is discarded. When
\(q=0\), the terminal row is simultaneously the first/interface row; this
is one term, not two charges.

## 6. Exact composite Peano identity

Write

\[
 \widehat F(s)=F(b+s)=\frac{\eta(s)^3}{3}.
\]

For a complete row let

\[
 c_k=k-\frac14,\qquad r_k=\eta(c_k),
\]

and define

\[
 P_k(s)=
 \begin{cases}
 \frac12(s-k+1)^2,&k-1\le s\le c_k,\\[2mm]
 \frac12(k-s)^2,&c_k\le s\le k,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Taylor's formula with integral remainder, integrated over the cell, gives

\[
 \int_{k-1}^{k}\widehat F(s)\,ds
 =
 \widehat F(c_k)-\frac14\widehat F'(c_k)
 +\int_{k-1}^{k}P_k(s)\widehat F''(s)\,ds.
 \tag{6.1}
\]

With \(\sigma=-A'\),

\[
 \widehat F'(c_k)=-\frac{r_k^2}{\sigma(r_k)}.
\]

Thus

\[
\boxed{
 L_k^{\mathrm{suf}}
 =
 C_k+
 \int_{k-1}^{k}P_k(s)\widehat F''(s)\,ds,}
 \tag{6.2}
\]

where

\[
 \boxed{
 C_k=
 \frac{r_k^3}{3}
 +\frac{r_k^2}{4\sigma(r_k)}
 -S_2(M_k).}
 \tag{6.3}
\]

No continuous \(p(r_k)\) comparison is used.

If \(\alpha>3/4\), set \(c_{\mathrm{top}}=q+3/4\) and

\[
 P_{\mathrm{top}}(s)=
 \begin{cases}
 \frac12(s-q)^2,&q\le s\le c_{\mathrm{top}},\\[2mm]
 \frac12(q+\alpha-s)^2,
   &c_{\mathrm{top}}\le s\le q+\alpha.
 \end{cases}
\]

Then

\[
\boxed{
 T_{\mathrm{top}}
 =
 C_{\mathrm{top}}+
 \int_q^{q+\alpha}
 P_{\mathrm{top}}(s)\widehat F''(s)\,ds,}
 \tag{6.4}
\]

with

\[
\boxed{
 C_{\mathrm{top}}
 =
 \alpha\widehat F(c_{\mathrm{top}})
 +\alpha\left(\frac{\alpha}{2}-\frac34\right)
 \widehat F'(c_{\mathrm{top}})
 -S_2(M_{\mathrm{top}}).}
 \tag{6.5}
\]

When \(\alpha\le3/4\), the top row has no cost and is retained as the exact
nonnegative integral \(T_{\mathrm{top}}\).

Let

\[
 P_{\mathrm{blk}}
 =
 \sum_{k=1}^{q}P_k+
 \mathbf1_{\{\alpha>3/4\}}P_{\mathrm{top}}.
\]

Summing before estimating gives

\[
\boxed{
\begin{aligned}
 \mathcal R_{\mathrm{suf}}
 &=
 \sum_{k=1}^{q}C_k
 +\mathbf1_{\{\alpha>3/4\}}C_{\mathrm{top}}\\
 &\quad+
 \mathbf1_{\{\alpha\le3/4\}}
 \int_q^{q+\alpha}\widehat F(s)\,ds
 +\int_0^{\widehat H}
 P_{\mathrm{blk}}(s)\widehat F''(s)\,ds.
\end{aligned}}
 \tag{PBLOCK}
\]

This is exact. It reduces the unproved sign to printed boundary scalars,
one harmless node-free top integral, and one intrinsic composite-curvature
integral. The interface singularity is handled by splitting the improper
integral, and \(\widehat F'\) has no interface atom. When \(b=0\), the
inverse endpoint \(s=0\) requires a separate cutoff: one has
\(\widehat F''(s)=O(s^{-4/3})\), while the first Peano kernel satisfies
\(P_1(s)=s^2/2\). Hence
\(P_1(s)\widehat F''(s)=O(s^{2/3})\) is integrable. Applying the identity on
\([\varepsilon,\widehat H]\) and sending \(\varepsilon\downarrow0\) makes
the omitted boundary terms vanish. If \(b>0\), then \(R<K\) and this
inverse-endpoint singularity is absent.

## 7. One-crossing curvature theorem

On the inner branch \(0<z<\mu\),

\[
 \sigma(z)=
 \frac{\arcsin(z/\mu)-\arcsin(z/K)}{\pi}.
\]

Define \(Q(z)=2\sigma(z)-z\sigma'(z)\).

### Theorem

There is exactly one \(z_*\in(\mu/\sqrt2,\mu)\) such that

\[
 Q(z)>0\quad(0<z<z_*),\qquad
 Q(z_*)=0,\qquad
 Q(z)<0\quad(z_*<z<\mu).
 \tag{7.1}
\]

### Proof

Put

\[
 r=\frac{\mu}{K}\in(0,1),\qquad x=\frac z\mu\in(0,1),
\]

and

\[
 \phi(u)=2\arcsin u-\frac{u}{\sqrt{1-u^2}}.
\]

Direct substitution gives

\[
 \pi Q(z)=\phi(x)-\phi(rx).
 \tag{7.2}
\]

Moreover,

\[
 \phi'(u)=\frac{1-2u^2}{(1-u^2)^{3/2}}.
 \tag{7.3}
\]

Let \(c=1/\sqrt2\). Since \(\phi\) is strictly increasing on
\([0,c]\), (7.2) is positive for \(0<x\le c\).

For \(x>c\), let \(g_r(x)=\phi(x)-\phi(rx)\). If \(rx\le c\), then

\[
 g_r'(x)=\phi'(x)-r\phi'(rx)<0.
\]

If \(rx>c\), put

\[
 h(u)=-\phi'(u)
 =\frac{2u^2-1}{(1-u^2)^{3/2}}.
\]

Then

\[
 h'(u)=\frac{u(1+2u^2)}{(1-u^2)^{5/2}}>0,
\]

and

\[
 g_r'(x)=-h(x)+rh(rx)<-h(x)+h(rx)<0.
\]

Thus \(g_r\) is strictly decreasing on \((c,1)\). It is positive at
\(c\), while \(\lim_{x\uparrow1}g_r(x)=-\infty\). The intermediate value
theorem proves the unique zero and (7.1).

At the two endpoints,

\[
 Q(z)=
 \frac1\pi
 \left[
 \left(\frac1\mu-\frac1K\right)z
 -\frac16
 \left(\frac1{\mu^3}-\frac1{K^3}\right)z^3
 +O(z^5)
 \right]
\]

as \(z\downarrow0\), whereas \(Q(z)\to-\infty\) as \(z\uparrow\mu\).
On the outer branch,

\[
 Q_{\mathrm{out}}(z)
 =
 \frac{2\arccos(z/K)}{\pi}
 +\frac{z}{\pi\sqrt{K^2-z^2}}>0.
\]

Finally,

\[
 \widehat F''(s)
 =
 \frac{zQ(z)}{\sigma(z)^3},
 \qquad z=\eta(s).
 \tag{7.4}
\]

Thus the negative curvature in (PBLOCK) is confined to one connected
shallow-inner interval adjacent to the interface. The outer piece, the
deep-inner piece, and the inverse-endpoint side are positive. This proves
localization, not the sign of the weighted Peano integral.

## 8. Regression against the rejected continuous route

The original directed Round 48 replay was rerun at 1400 Arb bits:

\[
\begin{aligned}
 K&=\frac{2485744973967441}{20000000},\\
 \mu&=\frac{1412489996090409}{10^{12}},\\
 n&=39561154.
\end{aligned}
\]

It certifies

\[
 A(\mu)=39561153.7448320909\ldots\in(n-1,n),
\]

\[
 \int_{n-1}^{n}F
 -p(\xi(n-\tfrac14))
 \in -572.69422630\pm5.18\cdot10^{-9}<0,
\]

while the literal discrete cell has \(N=1412\) and

\[
 L_n\in956715.736090048\pm8.69\cdot10^{-10}>0.
\]

The lead evaluator independently reproduces the two signs. No proposed
Round 49 statement implies the false continuous comparison: (6.3) retains
the literal \(S_2(M_k)\), and (PBLOCK) keeps the full Peano curvature term.

## 9. Attempted sign routes, in mandated order

### 9.1 Cumulative row-cone majorization

(RBLOCK) is the exact cumulative object. The needed assertion would be a
weighted cumulative dominance of \(B(z)\) over the nested literal intervals
in \(E(z)\), after retaining the positive \(M/12\) ledger. No such
whole-domain dominance was proved. Pointwise dominance is false in general
and was not assumed.

The first unsupported inequality is

\[
 \int_0^Rz^2\{B(z)-E(z)\}\,dz
 \ge
 -\frac1{12}
 \left(\sum M_k+\mathbf1_{\{\alpha>3/4\}}M_{\mathrm{top}}\right).
 \tag{9.1}
\]

Equation (9.1) is exactly (R49), not a new theorem.

### 9.2 Composite Peano plus curvature

(PBLOCK) and the one-crossing theorem reduce all curvature uncertainty to
one connected shallow interval. However, a one-sign-change statement for
\(\widehat F''\) does not by itself compare the negative shallow mass with
the explicit \(C_k\), the positive outer/interface piece, the deep reserve,
and the terminal scalar.

The first genuinely new remaining inequality is the sign of the right-hand
side of (PBLOCK), with the curvature integral restricted by (7.1). No
kernel cumulative-sign theorem was proved.

### 9.3 Abel summation

Abel summation of (RBLOCK) reproduces the same cumulative occupancy deficit.
Keeping the first interface row and terminal row avoids a false boundary
loss, but supplies no sign for the shallow cumulative term. The route ends
at the same intrinsic block, not at a distinct proof.

### 9.4 Fallback

No exact counterexample to (R49), and no proof that its sign mechanism is
impossible, was obtained. In accordance with the packet, the fallback was
evaluated but not substituted as the new analytic target. Its sign also
remains open.

## 10. Computational falsification

computations/general_d_round49_suffix_diagnostic.py implements:

- literal \(\mathrm{WT}_4\) directly and through inverse heights;
- \(\mathcal R_{\mathrm{suf}}\) in NSFX and SSFX forms;
- every complete cell and the exact terminal top;
- \(\mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}\);
- the one-crossing root; and
- the directed Round 48 regression through the frozen certified script.

In a deterministic 145-record structured/random pass:

- no class-A literal \(\mathrm{WT}_4\) negative was found;
- no class-B suffix negative was found;
- no class-C fallback negative was found;
- the two suffix forms and the two literal forms agreed to working
  precision; and
- support-collapse records made a positive suffix arbitrarily small, as
  expected, so no uniform positive margin is inferred.

The search covers active-wall approaches, \(\rho\) near zero and one,
integer and near-integer \(K,\mu\), interface-height walls, terminal
\(\widehat H\) walls, moderate frequency, and larger row counts. It is
diagnostic only:

    positive_coverage_certificate: FALSE

## 11. Endpoint and equality-face audit

| face | exact assignment |
|---|---|
| \(b=0\) | prefix empty; suffix equals literal WT4 |
| \(\tau\in\mathbb Z\) | \(b=\tau\); last prefix cell ends at interface; \(B(\mu)=0\) |
| \(0<\tau-b<1\) | only the first normalized row can straddle |
| \(\widehat H<3/4\) | no full row and no node; suffix is the positive top integral |
| \(\alpha=3/4\) | terminal node excluded by strict \(<\) |
| \(K\in\mathbb Z\) | \(a=K\) excluded; \(A(K)=0\) |
| \(\mu\in\mathbb Z\) | no action atom; split curvature at \(z=\mu\) |
| \(R\in\mathbb Z\) | \(a=R\) excluded in SSFX; inverse cutoff is \(\lceil R\rceil-1=R-1\) |
| \(R=0\) | formal clipped support, integral, and sum all vanish |
| \(\eta(c)\in\mathbb Z\) | literal \(M=\eta(c)-1\), never \(\eta(c)\) |
| \(B(a)+1/4\in\mathbb Z\) | strict bracket takes the lower value |
| activity equality | owned by the spectral no-mode theorem; not part of (ACT) |
| \(\rho\downarrow0,\rho\uparrow1\) | formulas remain exact; no limiting sign is promoted |

## 12. Dependency ledger

| input | use |
|---|---|
| strict bracket and inverse-layer identity | SPLIT, NSFX, SSFX, TOP |
| Round 48 full-outer lemma | prefix reserve and fallback only |
| Round 48 deep-inner lemma | retained positive diagnostic reserve; not spent in a false global sign |
| elementary Fubini/layer cake | SSFX and ROW1 |
| exact centered-square identity | ROW2--ROW3 |
| inverse differentiation | Peano boundary scalar and curvature |
| elementary \(\phi\)-monotonicity | new one-crossing theorem |
| Round 48 directed counterexample | regression gate only |

No pointwise \(D_A\), component-\(U\), branching-bonus, manuscript, or
finite-coverage theorem is used as a premise.

## 13. Exact loss ledger

| step | loss |
|---|---|
| SPLIT, NSFX, SSFX, IF, TOP | none |
| ROW1--ROW3 and terminal analogue | none |
| RBLOCK | none |
| PBLOCK | none |
| one-crossing theorem | none |
| prefix to \(\mathcal R_{\mathrm{out}}\) | discards the certified positive gaps \(L_n-(19N_n/48+27/128)\) |
| finite searches | diagnostic only; no analytic implication |
| attempted majorization/Abel routes | no inequality asserted |

## 14. No-double-counting ledger

1. Every inverse-height node belongs to exactly one prefix, complete suffix,
   or terminal row.
2. The interface belongs to the first normalized row only.
3. If \(q=0\), “interface row” and “terminal row” name the same row.
4. Every \(M/12\) correction corresponds to exactly one literal
   \(S_2(M)\).
5. The top node is present only for \(\alpha>3/4\).
6. The deep-inner lemma is not added to PBLOCK as a second reserve; it signs
   only cells satisfying its exact hypothesis.
7. The outer reserve is used only in the fallback, never added to the
   literal suffix theorem.

## 15. Theorem, reduction, diagnostic, and failure classification

### Proved theorem

\(Q(z)=2\sigma(z)-z\sigma'(z)\) has exactly one inner zero
\(z_*\in(\mu/\sqrt2,\mu)\), with the signs in (7.1).

### Proved exact reductions

SPLIT, NSFX, SSFX, IF, TOP, RBLOCK, and PBLOCK.

### Sufficient but unproved targets

\[
 \mathcal R_{\mathrm{suf}}\ge0,
 \qquad
 \mathcal R_{\mathrm{out}}+\mathcal R_{\mathrm{suf}}\ge0.
\]

### Diagnostics

The finite positive suffix/fallback/WT4 searches and numerical curvature
roots.

### Frozen failure

The continuous quarter-node polynomial comparison remains
interval-falsified. It is not used.

## 16. Final verdict and next exact obstruction

The correct Round 49 Prompt-A verdict is:

    INCOMPLETE — SUBSTANTIVE PARTIAL SUCCESS
    R49: not proved and not falsified
    R49-FB: not proved and not falsified
    literal WT4: not proved and not falsified
    one-crossing curvature theorem: proved
    exact composite Peano block: proved
    positive_coverage_certificate: FALSE

The first unrepaired implication is

\[
\begin{aligned}
 &\sum_{k=1}^{q}C_k
 +\mathbf1_{\{\alpha>3/4\}}C_{\mathrm{top}}
 +\mathbf1_{\{\alpha\le3/4\}}
 \int_q^{q+\alpha}\widehat F\\
 &\qquad+
 \int_0^{\widehat H}P_{\mathrm{blk}}\widehat F''\ge0,
\end{aligned}
 \tag{OPEN49}
\]

using the proved positive/negative/positive curvature localization. Signing
(OPEN49) requires a cumulative Peano-kernel payment between the first
interface row, the connected shallow-negative interval, the positive
deep-inner reserve, and the terminal row. The round stops before inventing
a count, floor, ratio, chamber, or second-certificate family.

No proof-obligation status should change. The scoped \(d=4\) aggregate
remains proposed; all broader statuses remain unchanged.

## 17. Prompt-A files

Created only:

    human/outbox/general-d-round-49-interface-to-top-suffix.md
    computations/general_d_round49_suffix_diagnostic.py
