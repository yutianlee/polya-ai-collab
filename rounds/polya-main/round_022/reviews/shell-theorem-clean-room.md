# Round 22 clean-room reconstruction: the three-dimensional shell theorem

## Verdict

**STRICT VERDICT: PASS.**

**First unsupported implication:** none.

This verdict is only for the unit-shell Pólya inequality and its
arbitrary-radius dilation corollary stated in the frozen Round 22 packet. It
does not promote a non-tiling assertion, the program target, a novelty claim,
or any other domain class.

## Isolation boundary and authentication

I performed this reconstruction without reading any file in
`rounds/polya-main/round_022/responses/`, any other Round 22 review, any
proposed judge, `state/best_proof_draft.md`, `state/current_state.md`, or
`state/next_round_prompts.md`.

The initial inputs were exactly the two prescribed live files. Their
SHA-256 digests were independently recomputed before they were read:

| input | required SHA-256 | recomputed SHA-256 |
|---|---|---|
| `state/lemma_packets/TARGET-shell-d3-round22-theorem.md` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` | `8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228` |
| `state/proof_obligations.yml` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` |

I treated only the following five graph-promoted obligations as lemmas:
`CONV-strict-counting`, `SHELL-sturm-liouville-completeness`,
`SHELL-rho-zero-endpoint`, `SHELL-rho-compact-analytic-envelope`, and
`SHELL-rho-one-endpoint`. To reconstruct the exact compact-cover set
arithmetic, I additionally read only these positive artifacts named by the
fourth obligation:

- `state/lemma_packets/SHELL-rho-compact.md`;
- `state/lemma_packets/SHELL-rho-compact-round17.md`;
- `state/lemma_packets/SHELL-rho-compact-round18.md`;
- `state/lemma_packets/SHELL-rho-compact-round19.md`;
- `state/lemma_packets/SHELL-rho-compact-round20.md`;
- `state/lemma_packets/SHELL-combined-closure-round20-claim.md`; and
- `state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md`.

The two last packets are used only to recover their exact domains and face
bookkeeping. Their historical labels do not themselves supply promotion;
the positive theorem input is the current proved status and statement of
`SHELL-rho-compact-analytic-envelope` in the authenticated graph.

## 1. Definitions and exact ordering of the outer ratio seams

Write

\[
 W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3,
 \qquad
 \omega _0=\frac{\sqrt3}{2\pi}-\frac16,
 \qquad
 C_*=\frac12+\frac{8\sqrt2}{15},
\]

and

\[
 \rho_* = \frac{\omega _0}{1+2C_*}.
\]

Here is an exact, non-decimal proof of the required ordering. Use the
elementary Archimedean bounds (3<\pi<22/7). Since

\[
 3\sqrt3>\frac{22}{7}>\pi
\]

(the first inequality follows after squaring from
(27>484/49)), we have

\[
 \omega _0=\frac{3\sqrt3-\pi}{6\pi}>0.
\]

Also (\sqrt3<7/4) and (\pi>3), so

\[
 \omega _0
 <\frac{7/4}{6}-\frac16
 =\frac18.
\]

Moreover (8\sqrt2/15>1/2) (square (16\sqrt2>15)), hence
(C_*>1) and (1+2C_*>3). Therefore

\[
 0<\rho_*<\frac{1/8}{3}=\frac1{24}<\frac78.
\tag{1}
\]

It follows directly from (1) that

\[
 (0,1)
 =(0,\rho_*]\mathbin{\dot\cup}
 (\rho_*,7/8)\mathbin{\dot\cup}
 [7/8,1).
\tag{2}
\]

The first seam belongs to the small-hole lemma and the second seam belongs
to the thin-shell lemma. Although the compact cover also contains both
vertical faces as overlaps, (2) fixes the theorem-level owners uniquely.

## 2. The zero-frequency case

For every (0<\rho<1), the promoted Sturm--Liouville completeness lemma
gives a positive Dirichlet spectrum, with eigenvalues repeated according to
their full angular multiplicities. Consequently

\[
 N_D(A_{\rho,1},0)
 =\#\{j:\lambda_j^D(A_{\rho,1})<0\}=0.
\]

Also (W(\rho,0)=0). Thus

\[
 N_D(A_{\rho,1},0)=W(\rho,0)=0.
\tag{3}
\]

This is a direct check, not a continuity argument from (K>0).

## 3. Independent reconstruction of the compact-middle cover

This section reconstructs only the implications and exact set subtraction
needed at theorem level. The spectral estimates on each accepted set are
the content of the promoted compact-envelope lemma.

### 3.1 Primitive cover and (\mathcal D_{16})

For clarity, define

\[
 G_1(s)=\frac{\sqrt{1-s^2}-s\arccos s}{\pi},\qquad
 C_0=1+\frac{8\sqrt2}{15},
\]

\[
 a_\rho=\frac{2\pi\rho}{1-\rho},\qquad
 \eta_\rho=G_1(\max\{\rho,1/2\}),
\]

\[
 K_0(\rho)=
 \left(
 \frac{\sqrt{a_\rho}+\sqrt{a_\rho+4\eta_\rho C_0}}
 {2\eta_\rho}
 \right)^2,
 \qquad
 H_0(\rho)=\frac{C_*}{\omega_0-\rho}\quad(\rho<\omega_0).
\]

On (I=[\rho_*,7/8]), the primitive accepted cover
(\mathcal A_{16}) is the union of the following exact domains:

1. the complete faces (\rho=\rho_*) and (\rho=7/8);
2. (2\rho K\le1);
3. ((1-\rho)K\le\pi);
4. (\rho<\omega_0) and (K(\omega_0-\rho)\ge C_*);
5. (K\ge K_0(\rho));
6. the retained seam branches
   \[
   \begin{array}{ll}
   0<1-\rho\le1/6,&K(1-\rho)^2\ge54,\\
   0<1-\rho\le1/8,&K(1-\rho)^2\ge32,\\
   0<1-\rho\le1/10,&K(1-\rho)^2\ge24,\\
   0<1-\rho\le1/25,&K(1-\rho)^2\ge20;
   \end{array}
   \]
7. the global high-frequency face and ray (K\ge295^2=87025).

Every displayed equality is covered. Some retained seam branches are
redundant or meet (I) only at an endpoint, but retaining them cannot
create a gap and they are not subtracted twice.

Put

\[
 h(\rho)=\frac1{2\rho},\qquad
 z_\rho=\frac{\pi}{1-\rho},\qquad
 L_{16}(\rho)=\max\{h(\rho),z_\rho\},
\]

and

\[
 U(\rho)=\min\left(
 \{K_0(\rho)\}
 \cup\{H_0(\rho):\rho<\omega_0\}
 \cup\left\{\frac{54}{(1-\rho)^2}:\rho\ge5/6\right\}
 \right).
\]

The exact complement of (\mathcal A_{16}) is

\[
 \mathcal D_{16}
 =\{\rho_*<\rho<7/8,\ L_{16}(\rho)<K<U(\rho)\}.
\tag{4}
\]

Both frequency inequalities in (4) are strict because their equality
faces are in the accepted cover. The two lower walls meet at

\[
 \rho_c=\frac1{1+2\pi},
 \qquad
 h(\rho_c)=z_{\rho_c}=\pi+\frac12.
\tag{5}
\]

Thus (L_{16}=h) on the low side and (L_{16}=z) on the high side,
with the common face covered. The upper function has its inherited exact
branches

\[
 U(\rho)=
 \begin{cases}
 H_0(\rho),&\rho_*<\rho<\rho_{HK},\\
 K_0(\rho),&\rho_{HK}\le\rho<5/6,\\
 54/(1-\rho)^2,&5/6\le\rho<7/8,
 \end{cases}
\tag{6}
\]

where (\rho_{HK}) is the inherited unique (H_0=K_0) switch. At that
switch the two values agree. The (\rho=\omega_0) eligibility change of
(H_0), the continuous (\eta_\rho) formula interface at (\rho=1/2),
and the inclusive seam start at (\rho=5/6) leave no uncovered fiber.

### 3.2 Exact residual chain through Round 20

For (m\ge0), set

\[
 k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\]

The accepted closed band through (k_2), with (\rho_c) included, gives

\[
 \begin{aligned}
 \mathcal D_{17}={}&
 \{\rho_*<\rho<\rho_c,\ h(\rho)<K<U(\rho)\}\\
 &\cup
 \{\rho_c\le\rho<7/8,\ k_2(\rho)<K<U(\rho)\}.
 \end{aligned}
\tag{7}
\]

The next accepted closed staircase through (k_5) changes only the second
lower wall:

\[
 \begin{aligned}
 \mathcal D_{18}={}&
 \{\rho_*<\rho<\rho_c,\ h(\rho)<K<U(\rho)\}\\
 &\cup
 \{\rho_c\le\rho<7/8,\ k_5(\rho)<K<U(\rho)\}.
 \end{aligned}
\tag{8}
\]

Now put

\[
 \rho_0=\frac1{\sqrt{337}},\qquad d=\frac{\sqrt{337}}2.
\]

The internal ratio ordering is exact. From (1),
(\rho_*<1/24<1/\sqrt{337}=\rho_0), since
(\sqrt{337}<24). Also

\[
 1+2\pi<\frac{51}{7}<\sqrt{337},
\]

where the last comparison follows by squaring. Hence

\[
 \rho_*<\rho_0<\rho_c.
\tag{9}
\]

The accepted lower staircase on
(\rho_0<\rho<\rho_c, h(\rho)<K\le d), together with the accepted high
staircase through (k_6), gives

\[
 \begin{aligned}
 \mathcal D_{19}={}&
 \{\rho_*<\rho\le\rho_0,\ h(\rho)<K<U(\rho)\}\\
 &\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
 &\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
 \end{aligned}
\tag{10}
\]

At (\rho=\rho_0), (h(\rho_0)=d), so the newly added lower fiber is
empty there and the whole ratio slice is correctly retained in the first
piece of (10). This is why replacing (10) by two merged open ratio cells
would be wrong.

Under the current promoted compact-envelope lemma, the accepted Round 20
addition closes both low components of (10), extends the high closed
staircase successively through (k_7,k_8,k_9,k_{10},k_{11}), and proves
the all-frequency optical theorem for (39/50\le\rho<1). Exact subtraction
therefore leaves

\[
 \boxed{
 \mathcal D_{20}
 =\{\rho_c\le\rho<39/50,\
 k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.}
\tag{11}
\]

The equality faces (K=k_{11}(\rho)) and (K=U(\rho)) are inherited
owners and are absent from (11). The face (\rho=39/50) is included in
the optical theorem and is likewise absent. The face (\rho=\rho_c)
remains in (11) only between the two strict frequency walls.

The remaining exact order needed later is

\[
 \frac7{51}<\rho_c<\frac{39}{50}<\frac78.
\tag{12}
\]

Indeed (1+2\pi<51/7) proves the first inequality, while
(\pi>3) gives (\rho_c<1/7<39/50), and
(39/50<7/8) is immediate by cross multiplication.

### 3.3 Scoped Round 21 closure and the (K=200) face

The compact theorem in the promoted envelope proves the strict target on
exactly

\[
 \frac7{51}\le\rho\le\frac{39}{50},
 \qquad 12\le K\le200.
\tag{13}
\]

Its 10,580 finite leaves have no domain outside (13). The aggregate
certificate's 1,286 boxes establish only the base predicates at (K=200);
the conclusion for

\[
 \rho_c\le\rho\le\frac{39}{50},\qquad K\ge200
\tag{14}
\]

is the separate accepted analytic aggregate implication, not a finite-box
extrapolation.

The guard (k_{11}(\rho)>12) is needed only on its proved domain
(\rho_c\le\rho<1). On that domain,

\[
 z_\rho\ge z_{\rho_c}=\pi+\frac12>\frac72,
\]

so

\[
 k_{11}(\rho)^2=z_\rho^2+132
 >\frac{49}{4}+132=\frac{577}{4}>144.
\]

Thus (k_{11}(\rho)>12). Every point of (11) satisfies the upper guard
(\rho<39/50<1), so there is no use at (\rho=1), still less at an
out-of-domain value such as (\rho=2).

Define the two subtraction owners

\[
 \mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},\qquad
 \mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

By (12), the ratio of every point of (\mathcal D_{20}) lies in both
relevant theorem ranges. By the guard, every such point has (K>12).
Hence (\mathcal C_{21}) is covered by (13), including (K=200), and
(\mathcal T_{21}) is covered by the analytic conclusion (14). The split
is disjoint and exhaustive regardless of whether, at a given ratio,
(U(\rho)<200), (U(\rho)=200), or (U(\rho)>200). Therefore

\[
 \mathcal D_{20}
 =\mathcal C_{21}\mathbin{\dot\cup}\mathcal T_{21},
 \qquad
 \boxed{\mathcal D_{21}=\varnothing.}
\tag{15}
\]

The face (K=200) is assigned only to the compact subtraction owner. The
aggregate theorem may meet that face, but it is not subtracted there a
second time.

### 3.4 Complete seam and moving-wall audit

The following ledger records the exact owners relevant to assembly:

| face | owner and consequence |
|---|---|
| (\rho=\rho_*) | complete small-hole endpoint; the compact overlap is not the outer owner |
| (\rho=\rho_0) | (h=d); the Round 19 added lower fiber is empty, and the retained first piece of (\mathcal D_{19}) is closed by the Round 20 lower theorem |
| (\rho=\rho_{HK}) | the moving upper walls (H_0=K_0) agree; their equality face is already covered |
| (\rho=\omega_0) | (H_0) eligibility ends, but (K_0) was already the active upper owner |
| (\rho=\rho_c) | (h=z_\rho); the high staircases include the ratio face, and the part surviving to (\mathcal D_{20}) is covered by Round 21 |
| (\rho=1/2) | the two formulas for (\eta_\rho), hence (K_0), meet continuously |
| (\rho=5/6) | the (54/(1-\rho)^2) seam begins inclusively and owns its equality face |
| (\rho=39/50) | the all-frequency optical theorem owns the complete face; Round 21 overcoverage does not subtract it again |
| (\rho=7/8) | complete thin-shell endpoint; the compact overlap is not the outer owner |
| (K=h(\rho)) | inclusive high-angular owner |
| (K=z_\rho) | inclusive phase-zero owner |
| (K=H_0(\rho)), (K=K_0(\rho)), and (K=54/(1-\rho)^2) | inherited high-frequency owners, all with equality included |
| retained (32,24,20) seam walls and (K=295^2) | included primitive owners; redundant coverage is never subtracted twice |
| (K=k_2,k_5,d,k_6) | respectively the Round 17, Round 18, Round 19 low/high upper owners; each successor residual is strict above the face |
| (K=k_7,k_8,k_9,k_{10},k_{11}) | successive Round 20 staircase owners; each new subband is open at its predecessor and closed at its own upper face |
| (K=U(\rho)) | inherited upper owner and excluded from every residual |
| (K=200) | compact Round 21 subtraction owner; the aggregate subtraction is open there |

Thus every inherited high-frequency wall, moving staircase wall, and named
internal ratio seam is either an included theorem face or lies in exactly
one strict residual that is later discharged. Equation (15) is the current
empty residual; no historical (\mathcal D_{18}), (\mathcal D_{19}), or
rectangular proxy has been substituted for it.

## 4. Strict counting at spectral and phase walls

All five input lemmas use

\[
 N_D(\Omega,\Lambda)=\#\{j:\lambda_j^D(\Omega)<\Lambda\}
\]

with repeated multiplicities. This convention is preserved literally in
the assembly.

Let (K_1=\sqrt{\lambda_1^D(A_{\rho,1})}>0). At the first positive
eigenfrequency,

\[
 N_D(A_{\rho,1},K_1^2)=0
 <W(\rho,K_1),
\]

because all eigenvalues are at least (\lambda_1), and those equal to it
are excluded. This separately tests the first positive wall.

More generally, if one shell eigenvalue is shared by several angular
channels, every copy at equality is excluded at the wall. Immediately
above it, the copies enter with the sum of their orthogonal angular
multiplicities, exactly as supplied by the completeness lemma. There is no
assumption that distinct angular channels cannot coincide.

At a normalized integer phase wall the strict radial count is

\[
 \#\{n\in\mathbb N:n<x\}=\lceil x\rceil-1.
\]

In particular, at (x=m\in\mathbb N) it is (m-1), not the ordinary
floor (\lfloor m\rfloor=m). Every inherited spectral, phase, angular,
and staircase equality is therefore read with the included/excluded rule
in the ledger above. No count is obtained by continuity across a jump and
no strict channel count is replaced by an ordinary floor.

## 5. The unit-shell inequality

Fix (0<\rho<1) and (K>0).

- If (0<\rho\le\rho_*), the promoted small-hole endpoint gives
  \[
  N_D(A_{\rho,1},K^2)\le W(\rho,K).
  \]
- If (\rho_*<\rho<7/8), the complete accepted compact cover together
  with (15) gives the same inequality. There is no residual point.
- If (7/8\le\rho<1), the promoted thin-shell endpoint gives the same
  inequality.

Together with (2) and the direct (K=0) check (3), these cases prove

\[
 \boxed{
 N_D(A_{\rho,1},K^2)
 \le\frac{2}{9\pi}(1-\rho^3)K^3
 \quad(0<\rho<1,\ K\ge0).}
\tag{16}
\]

Now let (\Lambda\ge0) and set (K=\sqrt\Lambda), the nonnegative square
root. Then (K^2=\Lambda) and (K^3=\Lambda^{3/2}), so (16) gives

\[
 \boxed{
 N_D(A_{\rho,1},\Lambda)
 \le\frac{2}{9\pi}(1-\rho^3)\Lambda^{3/2}.}
\tag{17}
\]

For (\Lambda=0), this substitution invokes exactly (3); it does not hide
a positive-frequency limit.

## 6. Weyl normalization

The volume of the unit ball in three dimensions is
(\omega_3=4\pi/3). Hence

\[
 L_3=\frac{\omega_3}{(2\pi)^3}
 =\frac{4\pi/3}{8\pi^3}
 =\frac1{6\pi^2}.
\tag{18}
\]

Subtracting the inner ball from the outer ball gives

\[
 |A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3).
\tag{19}
\]

Multiplying (18) and (19),

\[
 L_3|A_{\rho,1}|
 =\frac1{6\pi^2}\frac{4\pi}{3}(1-\rho^3)
 =\frac{2}{9\pi}(1-\rho^3).
\tag{20}
\]

Thus (17) is exactly the one-term three-dimensional Dirichlet Pólya
inequality, not a two-term Weyl estimate or a differently normalized
statement.

## 7. Arbitrary-radius dilation

Let (0<r<R), put (\rho=r/R\), and write

\[
 A_{r,R}=\{x:r<|x|<R\}.
\]

Since (R>0),

\[
 x\in A_{r,R}
 \iff \rho<|x/R|<1,
\]

and therefore

\[
 A_{r,R}=R A_{\rho,1}.
\tag{21}
\]

Define the unitary map

\[
 U_R:L^2(A_{r,R})\longrightarrow L^2(A_{\rho,1}),
 \qquad
 (U_Rf)(y)=R^{3/2}f(Ry).
\]

It maps the Dirichlet form domain onto the unit-shell form domain. The
chain rule gives

\[
 U_R(-\Delta_{A_{r,R}}^D)U_R^{-1}
 =R^{-2}(-\Delta_{A_{\rho,1}}^D).
\tag{22}
\]

Consequently, with multiplicity preserved,

\[
 \lambda_j^D(A_{r,R})=R^{-2}\lambda_j^D(A_{\rho,1}).
\tag{23}
\]

Because (R^2>0), the strict inequality in the counting function is
equivalent in both directions:

\[
 \begin{aligned}
 N_D(A_{r,R},\Lambda)
 &=\#\{j:R^{-2}\lambda_j^D(A_{\rho,1})<\Lambda\}\\
 &=\#\{j:\lambda_j^D(A_{\rho,1})<R^2\Lambda\}\\
 &=N_D(A_{\rho,1},R^2\Lambda).
 \end{aligned}
\tag{24}
\]

Thus the counting argument is (R^2\Lambda), not
(R^{-2}\Lambda). Applying (17) at (R^2\Lambda) and using (R>0),

\[
 \begin{aligned}
 N_D(A_{r,R},\Lambda)
 &\le\frac{2}{9\pi}
 \left(1-\frac{r^3}{R^3}\right)
 (R^2\Lambda)^{3/2}\\
 &=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}.
 \end{aligned}
\tag{25}
\]

Also

\[
 |A_{r,R}|=\frac{4\pi}{3}(R^3-r^3),
\]

so (18) turns (25) into

\[
 \boxed{
 N_D(A_{r,R},\Lambda)
 \le\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}
 =L_3|A_{r,R}|\Lambda^{3/2}
 \quad(\Lambda\ge0).}
\tag{26}
\]

Nothing in (21)--(26) distinguishes (R<1) from (R>1); only (R>0)
is used. At (\Lambda=0), positivity again makes both sides zero.

Finally, (r\downarrow0) and (r\uparrow R) may be taken as limits of
the coefficients for shells with (0<r<R), but the equality cases
(r=0) and (r=R) are not members of the stated shell family. No endpoint
theorem is inferred from either limit.

## Final falsification disposition

The direct checks above cover (K=0), the first positive eigenfrequency,
both outer ratio seams, (\rho_0,\rho_c,39/50), all inherited moving
faces, (K=200) from both sides, shared angular-channel eigenvalues,
integer phase walls, (\Lambda=0), both (R<1) and (R>1), the two open
geometric limits, and the direction of the scaled counting argument.
No mandatory falsification case produces a counterexample or an unsupported
assembly step.

**STRICT VERDICT: PASS. First unsupported implication: none.**
