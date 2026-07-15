# Round 22 fresh adversarial referee: spherical-shell theorem

Date: 2026-07-15

Role: fresh theorem referee, instructed to assume the claimed inequality is
false and to identify the first unsupported implication.

## Verdict

**PASS.**

**First unsupported implication: none.**

I reconstructed the theorem rather than adopting any prior verdict.  The
unit-shell inequality, the complete compact residual chain, the strict
threshold conventions, the Weyl normalization, and the arbitrary-radius
dilation all follow from the authenticated promoted inputs on exactly their
stated domains.  I found no circular dependency, no use of stale or negative
evidence as a positive premise, no finite-certificate extrapolation, and no
graph-status promotion.

This verdict concerns only the three-dimensional Dirichlet spectral
inequality for spherical shells and its dilation corollary.  Non-tiling,
program-target completion, novelty, and other domain classes are outside this
review.

## 1. Authentication and independent replay

I independently recomputed the six prescribed SHA-256 identities before
using their contents:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| frozen theorem packet | 8d77925828ccabd2dbe1ce066c5e07a513e991754ed8d5a0ff6aec1a41739228 | 6,568 | 244 |
| authoritative graph | a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224 | 241,363 | 4,147 |
| incumbent reconstruction | 4083d6ce3b428601b7430a72819f131b4a4fd2fcfb92b356686b5b3e84376d7b | 6,141 | 290 |
| isolated clean-room reconstruction | 9aac21bb288e3e9e9bbf5f8aff339753c75fa18013b430ce6cf9fbd3e38b5f12 | 18,000 | 655 |
| independent assembly/provenance audit | 2b0004b1a90f9b92e67432cffe1d6fed29189d0e5aab3b50f3b1743c8c695d56 | 14,726 | 361 |
| theorem cross-comparison | 6d9b9973fa635cfbaed520457a706822d2999bbc01f79cf0888b30ef9749b458 | 5,514 | 161 |

The canonical graph validator returned:

    Graph OK: D:\BaiduSyncdisk\Codex\Polya conjecture\state\proof_obligations.yml

I also independently authenticated the current final Round 21 source-execution
cycle:

| role | SHA-256 |
| --- | --- |
| scoped exact-\(\mathcal D_{20}\) packet | d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d |
| final verifier | 31130de2370fac5ef702c9bd34fce84fb0336cbc9ce02175d3419ba6344debb9 |
| final verifier tests | 4de930011f3a8a05e4e411a278c845a9da4f820666a52756b2b60883534b9b99 |
| final A4 replay report | 47cd9467a19f4f08e39b700d82b8c9d52d7272619167220431cbcaea873d43a5 |
| final source-execution comparison | 7c6dab2980f76926536def120df3bda6396e0193c2eae4d760dc3ea4b26c0d4a |
| final source-execution referee | d005e8c3c150c52ab2dfbc84b6f6ea678ef00f9402d9f8a67500f82d9d858e28 |
| final provenance/isolation audit | f4670818af3a57a965f0032edd72ea875d4ad618f9cc4a5b1b78cabdc7e481da |

Running the authenticated verifier at 384-bit higher precision reproduced:

    ROUND21_EXACT_D20_CLOSURE_A4 PASS
    authenticated_inputs=18
    exact_constants=PASS
    exact_set=PASS (243 sign rows; D20=C21 disjoint-union T21; proposed D21 empty)
    compact[256]=PASS leaves=10580 floor_comparisons=2153076
    compact[384]=PASS leaves=10580 floor_comparisons=2153076
    aggregate_base_K200[192]=PASS boxes=1286 sign_checks=14146
    aggregate_base_K200[384]=PASS boxes=1286 sign_checks=14146
    aggregate_scope=finite outward predicates at K=200 only
    analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED

The focused malicious timestamp-valid bytecode, module-state restoration, and
exact constants/faces/\(U\)-orderings/\(K=200\)-owner tests also passed:
three tests passed.

## 2. Premise graph, circularity, and status

The frozen packet permits five direct theorem inputs:

1. CONV-strict-counting;
2. SHELL-sturm-liouville-completeness;
3. SHELL-rho-zero-endpoint;
4. SHELL-rho-compact-analytic-envelope; and
5. SHELL-rho-one-endpoint.

Each has status proved_internal in the authenticated graph.  I traversed the
full transitive dependency closure of these five nodes.  It contains only
proved_internal, proved_external_dependency, and certified nodes.  It
contains no open or blocked node and does not contain TARGET-shell-d3.
Therefore the proof does not assume its conclusion.

In particular, SHELL-rho-compact-analytic-envelope is already proved and
points forward to the open node SHELL-rho-compact.  It does not depend on that
open node.  The logical direction is therefore

\[
\text{proved analytic envelope}
\longrightarrow \text{future compact/uniformity outputs},
\]

not the reverse.  The middle-range invocation is noncircular.

The graph statuses remain:

| node | status |
| --- | --- |
| SHELL-rho-compact | open |
| SHELL-rho-uniformity | open |
| TARGET-shell-d3 | open |
| POLYA-program-target | open |

The packet, incumbent, clean-room proof, A4 audit, comparison, and this report
are review artifacts, not State Patches.  None promotes any node.

## 3. Outer constants and the two theorem seams

Write

\[
\omega _0=\frac{\sqrt3}{2\pi}-\frac16,\qquad
C_*=\frac12+\frac{8\sqrt2}{15},\qquad
\rho_*=\frac{\omega_0}{1+2C_*}.
\]

The ordering is exact.  From \(3<\pi<22/7\) and
\(3\sqrt3>22/7\), one has \(3\sqrt3>\pi\), hence
\(\omega_0>0\).  Also \(\sqrt3<2\) and \(\pi>3\) give
\(\omega_0<1/6\).  Since \(C_*>0\),
\(1+2C_*>1\), and therefore

\[
0<\rho_*<\omega_0<\frac16<\frac78.
\]

Thus the ratio domain is exactly the disjoint union

\[
(0,1)
=(0,\rho_*]\mathbin{\dot\cup}
(\rho_*,7/8)\mathbin{\dot\cup}
[7/8,1).
\]

The face \(\rho=\rho_*\) is assigned to the promoted small-hole theorem.
The face \(\rho=7/8\) is assigned to the promoted thin-shell theorem.  The
compact cover may overlap those faces, but it is not the theorem-level owner
of either.  Neither \(\rho=0\) nor \(\rho=1\) is asserted to be a member of
the shell family.

## 4. Zero frequency and strict spectral walls

For every \(0<\rho<1\), the promoted Sturm--Liouville theorem gives a
positive Dirichlet spectrum with exact multiplicities.  Consequently,
under strict counting,

\[
N_D(A_{\rho,1},0)
=\#\{j:\lambda_j^D(A_{\rho,1})<0\}
=0.
\]

The Weyl-side expression

\[
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3
\]

also satisfies \(W(\rho,0)=0\).  Thus \(K=0\) is proved directly, not by
continuity from positive frequency.

If \(K_1=\sqrt{\lambda_1^D(A_{\rho,1})}\), then

\[
N_D(A_{\rho,1},K_1^2)=0<W(\rho,K_1).
\]

Every copy of the threshold eigenvalue is excluded.  If several angular
channels share an eigenvalue, their orthogonal multiplicities add in the
spectrum, but all equal-threshold copies remain excluded at the wall and
enter together only above it.

For a positive normalized radial phase \(x\), strict counting uses

\[
\#\{n\in\mathbb N:n<x\}=\lceil x\rceil-1.
\]

At an integer phase wall \(x=m\), this is \(m-1\), not the ordinary floor
\(m\).  The promoted staircase inputs use this convention at every phase and
eigenvalue wall.  No continuity argument across a counting jump is used in
the theorem assembly.

## 5. Independent reconstruction of the compact cover

Define

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
H_0(\rho)=\frac{C_*}{\omega_0-\rho}
\quad(\rho<\omega_0).
\]

Also put

\[
h(\rho)=\frac1{2\rho},\qquad
z_\rho=\frac{\pi}{1-\rho},\qquad
k_m(\rho)=\sqrt{z_\rho^2+m(m+1)}.
\]

### 5.1 Primitive complement \(\mathcal D_{16}\)

The primitive accepted cover contains, with equality included:

- the complete ratio faces \(\rho=\rho_*\) and \(\rho=7/8\);
- \(K\le h(\rho)\);
- \(K\le z_\rho\);
- \(K\ge H_0(\rho)\) when \(\rho<\omega_0\);
- \(K\ge K_0(\rho)\);
- the retained seam rays
  \(K(1-\rho)^2\ge54,32,24,20\) on their respective closed
  width domains; and
- the global face and ray \(K\ge295^2=87025\).

On the open compact ratio interval the active lower wall is

\[
L_{16}(\rho)=\max\{h(\rho),z_\rho\}.
\]

The two walls agree exactly at

\[
\rho_c=\frac1{1+2\pi},\qquad
h(\rho_c)=z_{\rho_c}=\pi+\frac12.
\]

Thus \(L_{16}=h\) below \(\rho_c\) and \(L_{16}=z\) above it, with the
equality face already covered.

Let \(\rho_{HK}\) be the unique inherited switch where
\(H_0=K_0\).  The exact upper floor is

\[
U(\rho)=
\begin{cases}
H_0(\rho),&\rho_*<\rho<\rho_{HK},\\
K_0(\rho),&\rho_{HK}\le\rho<5/6,\\
54/(1-\rho)^2,&5/6\le\rho<7/8.
\end{cases}
\]

At \(\rho_{HK}\) the first two formulas agree.  The \(H_0\) eligibility
change at \(\rho=\omega_0\) makes no gap because \(K_0\) is already the
active branch there.  The two definitions of \(\eta_\rho\), and hence
\(K_0\), meet continuously at \(\rho=1/2\).  At \(\rho=5/6\), the
\(54/(1-\rho)^2\) seam begins inclusively and is the active upper owner.
The retained \(32,24,20\) seams meet the interval only at or beyond the
thin endpoint and therefore do not create another interior residual wall.
The global \(295^2\) face is already above an accepted active upper ray in
every ratio band.

Exact subtraction therefore gives

\[
\boxed{
\mathcal D_{16}
=\{\rho_*<\rho<7/8,\ L_{16}(\rho)<K<U(\rho)\}.}
\]

Both frequency inequalities are strict because both equality faces are
accepted.

### 5.2 The complete successor chain

The Round 17 closed band \(z_\rho\le K\le k_2(\rho)\), including
\(\rho=\rho_c\), changes only the high-side lower wall:

\[
\mathcal D_{17}
=\{\rho_*<\rho<\rho_c,\ h(\rho)<K<U(\rho)\}
\cup
\{\rho_c\le\rho<7/8,\ k_2(\rho)<K<U(\rho)\}.
\]

The Round 18 genuinely new band
\(k_2(\rho)<K\le k_5(\rho)\) gives

\[
\mathcal D_{18}
=\{\rho_*<\rho<\rho_c,\ h(\rho)<K<U(\rho)\}
\cup
\{\rho_c\le\rho<7/8,\ k_5(\rho)<K<U(\rho)\}.
\]

Now set

\[
\rho_0=\frac1{\sqrt{337}},\qquad d=\frac{\sqrt{337}}2.
\]

The internal ordering is exact:

\[
\rho_*<\frac1{24}<\rho_0<\rho_c.
\]

For the first inequality, \(\sqrt3<7/4\) and \(\pi>3\) give
\(\omega_0<1/8\), while \(8\sqrt2/15>1/2\) gives
\(1+2C_*>3\), hence \(\rho_*<1/24\).  The inequality
\(1/24<\rho_0\) follows from \(\sqrt{337}<24\).  For the last,

\[
1+2\pi<\frac{51}{7}<\sqrt{337},
\]

so taking positive reciprocals gives \(\rho_0<\rho_c\).

Round 19 accepts

\[
\rho_0<\rho<\rho_c,\quad h(\rho)<K\le d,
\]

and the high band through \(k_6\).  Hence

\[
\begin{aligned}
\mathcal D_{19}={}&
\{\rho_*<\rho\le\rho_0,\ h(\rho)<K<U(\rho)\}\\
&\cup\{\rho_0<\rho<\rho_c,\ d<K<U(\rho)\}\\
&\cup\{\rho_c\le\rho<7/8,\ k_6(\rho)<K<U(\rho)\}.
\end{aligned}
\]

At \(\rho=\rho_0\), \(h(\rho_0)=d\).  The new lower fiber is empty
there, so retaining \(\rho=\rho_0\) in the first piece is necessary and
correct.

Round 20:

1. closes both low pieces of \(\mathcal D_{19}\);
2. extends the included high staircase successively through
   \(k_7,k_8,k_9,k_{10},k_{11}\); and
3. proves the all-frequency optical theorem on
   \(39/50\le\rho<1\).

Therefore

\[
\boxed{
\mathcal D_{20}
=\{\rho_c\le\rho<39/50,\
k_{11}(\rho)<K<U(\rho)=K_0(\rho)\}.}
\]

Here \(U=K_0\) because
\(\rho_{HK}<\omega_0<1/8<\rho_c\) and
\(39/50<5/6\).  The face \(K=k_{11}\) is staircase-owned, the face
\(K=U\) is high-energy-owned, and \(\rho=39/50\) is optical-owned.
The ratio face \(\rho=\rho_c\) remains only between the two strict
frequency walls.

### 5.3 Moving-wall ownership ledger

| face or interface | disposition |
| --- | --- |
| \(\rho=\rho_*\) | complete small-hole outer owner |
| \(\rho=1/16\) | coarse historical cell split only; no wall is moved |
| \(\rho=\rho_0\) | \(h=d\); empty new lower fiber, then Round 20 closure |
| \(\rho=\rho_{HK}\) | \(H_0=K_0\); the two upper values agree |
| \(\rho=\omega_0\) | \(H_0\) eligibility ends after \(K_0\) became active |
| \(\rho=\rho_c\) | \(h=z_\rho\); high staircase includes this ratio face |
| \(\rho=1/2\) | the two \(\eta_\rho\) formulas, hence \(K_0\), agree |
| \(\rho=5/6\) | the \(54/(1-\rho)^2\) seam begins inclusively |
| \(\rho=39/50\) | complete Round 20 optical owner |
| \(\rho=7/8\) | complete thin-shell outer owner |
| \(K=h(\rho)\) | included high-angular owner |
| \(K=z_\rho\) | included phase-zero owner |
| \(K=H_0,K_0,54/(1-\rho)^2\) | included inherited upper owners |
| retained \(32,24,20\) seams and \(K=295^2\) | included primitive owners; no second subtraction |
| \(K=k_2,k_5,d,k_6\) | included Round 17--19 successor faces |
| \(K=k_7,k_8,k_9,k_{10},k_{11}\) | included successive Round 20 staircase faces |
| \(K=U(\rho)\) | inherited high-energy owner, outside every residual |
| \(K=200\) | Round 21 compact subtraction owner; aggregate subtraction open there |

Every successor residual is strict beyond an included predecessor face.  No
historical \(\mathcal D_{17}\), \(\mathcal D_{18}\), or
\(\mathcal D_{19}\) is substituted for the current residual.

## 6. Exact Round 21 closure and evidence scope

The remaining ratio order is

\[
\frac7{51}<\rho_c<\frac{39}{50}<\frac78.
\]

The first inequality follows from
\(\pi<22/7\):

\[
7(1+2\pi)<51
\quad\Longrightarrow\quad
\frac7{51}<\frac1{1+2\pi}=\rho_c.
\]

Also \(\pi>3\) gives
\(\rho_c<1/7<39/50\), and
\(39/50<7/8\) follows by cross multiplication.

For the frequency guard, assume exactly
\(\rho_c\le\rho<1\).  Then

\[
z_\rho\ge z_{\rho_c}=\pi+\frac12>\frac72,
\]

and so

\[
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132
=\frac{577}{4}>144.
\]

Thus

\[
k_{11}(\rho)>12\qquad(\rho_c\le\rho<1).
\]

The upper ratio wall is essential: \(z_\rho\) is undefined at
\(\rho=1\), and the unqualified assertion is false at \(\rho=2\).
Every point of \(\mathcal D_{20}\) has
\(\rho<39/50<1\), so the guard is used only on its proved domain.

Define

\[
\mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},\qquad
\mathcal T_{21}=\mathcal D_{20}\cap\{K>200\}.
\]

Every point of \(\mathcal C_{21}\) lies in the compact theorem domain

\[
\frac7{51}\le\rho\le\frac{39}{50},\qquad
12\le K\le200.
\]

Every point of \(\mathcal T_{21}\) lies in the aggregate analytic theorem
domain

\[
\rho_c\le\rho\le\frac{39}{50},\qquad K\ge200.
\]

The split is disjoint and exhaustive by definition:

\[
\mathcal D_{20}
=\mathcal C_{21}\mathbin{\dot\cup}\mathcal T_{21}.
\]

It remains correct in all three cases
\(U(\rho)<200\), \(U(\rho)=200\), and \(U(\rho)>200\).
Where \(K=200\) belongs to \(\mathcal D_{20}\), it is subtracted only
by \(\mathcal C_{21}\).  Although both theorem domains are valid at that
face, \(\mathcal T_{21}\) is open there, so there is one subtraction owner.
Consequently,

\[
\boxed{\mathcal D_{21}=\varnothing.}
\]

The evidence boundary is preserved:

- 10,580 compact leaves own finite proxy predicates only on the closed
  rectangle \([7/51,39/50]\times[12,200]\);
- the promoted compact analytic bridge owns transfer from those predicates
  to the strict spectral inequality;
- 1,286 aggregate boxes own finite outward base predicates only at
  \(K=200\);
- the promoted derivative, curvature, and two-integration argument owns the
  universal aggregate theorem for \(K\ge200\); and
- the wrapper owns authentication, schema checks, finite replay, sign rows,
  and exact set arithmetic, not the analytic propagation.

The wrapper's explicit
analytic_K_ge_200_chain=A3_REQUIRED_NOT_CLAIMED line is therefore a correct
scope boundary, not a gap in the promoted analytic lemma.

## 7. Stale and negative chronology

The corrected scoped packet rejects the old literal
\(k_{11}(\rho)>12\) for every \(\rho\ge\rho_c\).  The current theorem uses
only the corrected domain \(\rho_c\le\rho<1\), and in fact only its
\(\mathcal D_{20}\) subdomain.

The rejected unscoped candidate beginning 415546156e, the unscoped A4 report
beginning d9def12c, the cache-vulnerable report beginning 55f4f574 and its
authoritative failure beginning d9a8fd94, the old wrapper/test cycles
4868dcc3/6716ff1b and 64854c95/c9747c8c, the intermediate repair
c501608c/d5dab951, and the superseded comparison/referee/provenance reports
e923c034, c0a5239c, and 48b259a9 are not used to authenticate current source
semantics.

Where an older clean-room artifact remains useful, it is used only for its
independent analytic reconstruction restricted to the displayed
\(\mathcal D_{20}\) ratio domain.  It is not used for the rejected
unqualified guard or for stale executable provenance.  The graph keeps the
failed and superseded cycles in negative chronology, while the current final
source-execution cycle is positive.  No negative artifact is silently
revived.

## 8. Assembly of the unit-shell inequality

For \(K>0\):

- on \(0<\rho\le\rho_*\), the promoted small-hole endpoint gives
  \(N_D(A_{\rho,1},K^2)\le W(\rho,K)\);
- on \(\rho_*<\rho<7/8\), the reconstructed accepted cover and
  \(\mathcal D_{21}=\varnothing\) give the same inequality; and
- on \(7/8\le\rho<1\), the promoted thin-shell endpoint gives the same
  inequality.

The disjoint outer partition exhausts \(0<\rho<1\).  Together with the
direct \(K=0\) check,

\[
\boxed{
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3
\quad(0<\rho<1,\ K\ge0).}
\]

No endpoint is supplied by a limit and no strict spectral count is changed
to a non-strict one.

## 9. Weyl normalization and \(\Lambda\) substitution

In three dimensions,

\[
\omega_3=\frac{4\pi}{3},\qquad
L_3=\frac{\omega_3}{(2\pi)^3}
=\frac{4\pi/3}{8\pi^3}
=\frac1{6\pi^2}.
\]

The unit-shell volume is

\[
|A_{\rho,1}|=\frac{4\pi}{3}(1-\rho^3),
\]

so

\[
L_3|A_{\rho,1}|
=\frac1{6\pi^2}\frac{4\pi}{3}(1-\rho^3)
=\frac{2}{9\pi}(1-\rho^3).
\]

For every \(\Lambda\ge0\), let \(K=\sqrt\Lambda\), the nonnegative
root.  Then \(K^2=\Lambda\) and \(K^3=\Lambda^{3/2}\).  The already proved
\(K=0\) case covers \(\Lambda=0\).  Hence

\[
N_D(A_{\rho,1},\Lambda)
\le L_3|A_{\rho,1}|\Lambda^{3/2}.
\]

This is the one-term three-dimensional Dirichlet Pólya normalization, not a
two-term Weyl estimate.

## 10. Arbitrary-radius scaling, including \(R<1\)

Let \(0<r<R\) and \(\rho=r/R\).  Since \(R>0\),

\[
A_{r,R}=R A_{\rho,1}.
\]

The unitary dilation

\[
(D_Ru)(x)=R^{-3/2}u(x/R)
\]

maps \(L^2(A_{\rho,1})\) onto \(L^2(A_{r,R})\), maps the Dirichlet form
domains onto one another, and satisfies

\[
\int_{A_{r,R}}|\nabla D_Ru|^2\,dx
=R^{-2}\int_{A_{\rho,1}}|\nabla u|^2\,dx.
\]

Therefore, with multiplicity preserved,

\[
\lambda_j^D(A_{r,R})
=R^{-2}\lambda_j^D(A_{\rho,1}).
\]

Because \(R^2>0\), strict inequalities are equivalent in the correct
direction:

\[
\lambda_j^D(A_{r,R})<\Lambda
\iff
\lambda_j^D(A_{\rho,1})<R^2\Lambda.
\]

Thus

\[
N_D(A_{r,R},\Lambda)
=N_D(A_{\rho,1},R^2\Lambda),
\]

not a count at \(R^{-2}\Lambda\).  Applying the unit-shell result,

\[
\begin{aligned}
N_D(A_{r,R},\Lambda)
&\le\frac{2}{9\pi}
\left(1-\frac{r^3}{R^3}\right)(R^2\Lambda)^{3/2}\\
&=\frac{2}{9\pi}(R^3-r^3)\Lambda^{3/2}\\
&=L_3|A_{r,R}|\Lambda^{3/2}.
\end{aligned}
\]

Here
\(|A_{r,R}|=(4\pi/3)(R^3-r^3)\), obtained by subtracting the inner
ball volume from the outer ball volume.

Only \(R>0\) was used.  The derivation is unchanged for \(R<1\) and
\(R>1\); it uses no monotonicity in \(R\).  At \(\Lambda=0\), both sides
again vanish.  The limits \(r\downarrow0\) and \(r\uparrow R\) do not add
the equality cases \(r=0\) or \(r=R\) to the stated bounded-shell class.

## 11. Final adversarial disposition

The attempted counterexample sites all close:

- \(K=0\) and the first positive eigenfrequency;
- both traces at \(\rho=\rho_*\) and \(\rho=7/8\);
- the internal faces \(\rho_0,\rho_c,39/50\);
- every lower, upper, high-frequency, and moving staircase wall;
- the three possible positions of \(U(\rho)\) relative to \(200\);
- \(K=200\) with one subtraction owner;
- shared shell eigenvalues and their full angular multiplicities;
- integer phase walls under strict counting;
- \(\Lambda=0\) under \(K=\sqrt\Lambda\);
- every \(R>0\), in particular \(R<1\); and
- the direction \(R^2\Lambda\) in the scaled count.

The cross-comparison has one presentation-only omission in its displayed
chain, where D20supset lacks the TeX backslash before superset.  The
surrounding formulas and all authenticated source statements give the
intended inclusion unambiguously; this is not a mathematical implication or
a scope discrepancy.

**Final verdict: PASS.  First unsupported implication: none.**
