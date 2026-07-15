# Round 22 Spherical-Shell Non-Tiling: Fresh Adversarial Referee

Date: 2026-07-15

## Verdict

**PASS.**

**First unsupported implication:** none.

Starting from the assumption that the frozen claim was false, I found neither
a congruent tiling nor a failure in the rigid-motion reduction, center
separation, local-finiteness/countability chain, boundary removal, exterior
approach, fixed-neighbor extraction, boundary classification, finite-sphere
cover, coincident-sphere exclusions, or scaling. The proof works for exact and
almost-everywhere open-shell coverage and, after an explicit countability
step, for exact and almost-everywhere closed-shell coverage.

This is a geometry verdict only. It does not prove or import a spectral
theorem, make a novelty or priority claim, change the authoritative graph, or
authorize a State Patch.

## 1. Authentication and isolation

I followed the required order: I first authenticated the frozen packet, its
freeze, the Round 22 claim-scope audit, and the authoritative graph. I then
attempted the claim independently under the hypothesis that it was false. I
did not open the Round 21 incumbent route, clean-room proof, or typography
addendum until after fixing an independent provisional verdict. The mandated
scope audit was inspected at the authentication stage, but I did not use its
PASS or its comparison statements as a proof premise.

The current identities are:

| artifact | SHA-256 | bytes | physical lines |
| --- | --- | ---: | ---: |
| frozen packet | `d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f` | 4,703 | 105 |
| packet freeze | `c2067d2ec485a58b176352418a994e201415dfd410fdd324040a5019cbf97e7a` | 992 | 30 |
| Round 22 scope audit | `96dc2866392d2140ae5271dd8d419b0eeef3f9c29f357c8e6a1c8f21e13cd8a7` | 11,679 | 234 |
| authoritative graph | `a7f8c093f42522465862ea28bf57b1ee60be8b7f16804cebb300b0924ac7d224` | 241,363 | 4,147 |

The packet hash is exactly the required
`d8d0a9f59d132127033b338db95549d8e52b0252a832946670addab92baf4c8f`.
Its byte count, LF-only line count, terminal LF, strict UTF-8 encoding, and
absence of a BOM agree with the freeze. The freeze's baseline commit
`96fc9a1ec25efc45e430ed6e807b509e96cfcf3b` equaled `HEAD` when the initial
authentication was performed, and its embedded authoritative-graph hash
reproduces exactly. During this review, parallel theorem-lifecycle work moved
`HEAD` to `f4a21395b9227c42fac5ebbdd01712b21f63cefc`; rehashing afterward confirmed
that the packet, freeze, scope audit, and authoritative graph identities in
the table remained unchanged.

The canonical graph validator returned `Graph OK`. Independent parsing found
60 obligations with 60 distinct identifiers. There is no live obligation
named `SHELL-spherical-shell-nontiling`; `POLYA-program-target` remains open
with only `CONV-strict-counting` and `TARGET-shell-d3` as dependencies, and
`TARGET-shell-d3` remains open. Thus the packet, freeze, and audits have not
silently promoted the proposed geometry claim.

The worktree already contained untracked Round 22 artifacts before this
review. I did not alter them; the only file created by this review is this
report.

## 2. Independent reduction and uniform center separation

Let a putative tiling be given for some $0<r<R$. Since $R>0$, dilation by
$1/R$ gives the normalized shell

\[
T=S_{\alpha,1}=\{x:\alpha<|x|<1\},
\qquad \alpha=r/R\in(0,1).
\]

An arbitrary rigid motion has the form $x\mapsto Qx+a$, with $Q$ orthogonal.
Radial invariance gives $Q(T)=T$, including for reflections and every
orientation-reversing $Q$. Every congruent copy is therefore the translate

\[
T_a=\{x:\alpha<|x-a|<1\}.
\]

This reduction does not change the coverage convention. Two indexed copies
with the same center have the same nonempty open interior, so duplicate
indices already contradict pairwise-disjoint interiors.

For a separation argument independent of the later clean-room comparison,
fix a unit vector `e` and set

\[
c=\frac{1+\alpha}{2}e,
\qquad \varepsilon=\frac{1-\alpha}{4}.
\]

Then

\[
\frac{1+3\alpha}{4}<|x|<\frac{3+\alpha}{4}
\quad\text{for }x\in B(c,\varepsilon),
\]

so $B(c,\varepsilon)$ is contained in $T$. Consequently $T_a$ contains
$B(a+c,\varepsilon)$. Disjoint tile interiors make these balls disjoint,
hence

\[
|a-b|\geq 2\varepsilon=\frac{1-\alpha}{2}>0
\qquad(a\ne b).
\tag{2.1}
\]

Thus a bounded set contains only finitely many centers: equal small balls
about separated centers fit into one bounded enlargement. Moreover, if a
tile meets a bounded set `K`, its center lies in the bounded one-unit
enlargement of `K`. The tile family is therefore locally finite. Covering
center space by the countable family of integer-radius balls then makes the
center set, and hence the indexed family, countable. This rules out both an
initially uncountable family and infinitely many centers accumulating near a
chosen sphere; neither property was assumed from the word “tiling.”

## 3. Exact, almost-everywhere, open, and closed conventions

Each tile boundary is the union of the spheres

\[
\{x:|x-a|=\alpha\}\cup\{x:|x-a|=1\},
\]

each of which has three-dimensional Lebesgue measure zero. Countability from
Section 2 therefore implies that the union `B` of all tile boundaries is
null.

For the open-copy convention, the assumed union of the $T_a$ already covers
up to a null set; exact coverage is a special case. For closed copies, let
$K_a=\{x:\alpha\leq |x-a|\leq1\}$. If the $K_a$ cover exactly or up to a
null set $N$, then

\[
\mathbb R^3\setminus\bigcup_a T_a\subseteq N\cup B.
\]

Hence the open interiors still cover almost everywhere. This order is
essential: the boundary-only part is removed only after separation has made
the family countable. It handles exact closed-shell tilings without assuming
that their boundaries are disjoint.

## 4. Exterior approach and the fixed neighboring tile

Choose a tile $T_{a_0}$ and its outer sphere

\[
\Sigma=\{x:|x-a_0|=1\}.
\]

Fix arbitrary $p\in\Sigma$ and put $u=p-a_0$, so $|u|=1$. A radial ray
alone could lie in the null exceptional set, so it is not enough to choose
points on that ray. Instead use the positive-volume open balls

\[
U_n=B\!\left(p+\frac{2}{n}u,\frac1n\right).
\]

Every $x\in U_n$ satisfies $|x-a_0|>1$, while every point of $U_n$ is
within $3/n$ of $p$. Since the union of tile interiors has null complement,
each $U_n$ contains a point $x_n$ in some tile interior. It cannot be in
$T_{a_0}$.

The sequence $x_n$ tends to $p$. All corresponding centers are eventually
in one bounded set because $|x_n-a_n|<1$. Local finiteness leaves only
finitely many possible centers, so an infinite subsequence lies in a single
fixed tile $T_a$, with $a\ne a_0$. Therefore $p$ lies in the closure of
$T_a$.

It cannot lie in the interior of $T_a$. If a ball $B(p,\eta)$ lay in $T_a$,
then for

\[
0<t<\min\{\eta,1-\alpha\}
\]

the point $p-tu$ would lie both in $T_{a_0}$ and in $T_a$, contrary to
disjoint interiors. Thus

\[
p\in\partial T_a,\qquad a\ne a_0.
\tag{4.1}
\]

This proves the boundary conclusion rather than merely a closure conclusion,
and it explicitly excludes the possibility that the limiting point is in the
neighboring shell's interior.

## 5. Finite boundary-sphere cover and contradiction

If a neighboring boundary sphere of radius $s\in\{\alpha,1\}$ contains a
point of $\Sigma$, then its center satisfies

\[
|a-a_0|\leq 1+s\leq2.
\]

By (2.1), only finitely many centers occur in this closed ball. Since $p$ in
Section 4 was arbitrary, (4.1) produces a finite cover of $\Sigma$ by the
inner and outer boundary spheres of these finitely many neighboring tiles.

Translate $a_0$ to zero. For a neighboring center $a\ne0$ and radius
$s\in\{\alpha,1\}$, the intersection of its sphere with $\Sigma$ satisfies

\[
|x|^2=1,
\qquad
2a\mathbin\cdot x=|a|^2+1-s^2.
\]

The second equation is a genuine plane equation. Its intersection with
$\Sigma$ is empty, a tangent point, or a circle, and hence has zero
two-dimensional surface measure on $\Sigma$. Tangency therefore gives no
exception.

Nor can an identical sphere occur. An outer sphere identical to $\Sigma$
would require $a=a_0$, giving the original tile or a forbidden duplicate.
An inner sphere cannot be identical because its radius is $\alpha<1$.
Repeated spheres belonging to different neighbors can only reduce the finite
list and do not change its surface measure.

The resulting finite union has zero surface measure on $\Sigma$, whereas
$\Sigma$ has area $4\pi$. It cannot cover $\Sigma$, contradicting Section 4.
Thus the normalized tiling does not exist.

Finally, dilation by $1/R$ is an invertible linear map, preserves exact
coverage and disjointness, and sends null sets to null sets with measure
factor $R^{-3}$. This is valid whether $R<1$, $R=1$, or $R>1$. The normalized
contradiction therefore scales back to every $0<r<R$.

## 6. Mandatory falsification cases

| attempted failure or convention | determination |
| --- | --- |
| uncountable indexed family | Duplicate centers are impossible and (2.1) makes the center set countable. |
| centers accumulating near $\Sigma$ | Positive uniform separation gives finitely many centers in every bounded neighborhood. |
| coverage only through boundaries | The countable boundary union is null; closed coverage reduces to a.e. coverage by open interiors. |
| a.e. rather than exact coverage | Every positive-volume `U_n` contains an interior-covered point even if the null exceptional set is dense. |
| exact open or exact closed copies | Exact open coverage is a special case; exact closed coverage is handled by boundary removal. |
| rotations, reflections, orientation reversal | Orthogonal parts fix the radial shell, so all copies reduce to translations. |
| duplicate indexed copies | Equal centers give equal nonempty interiors and violate disjointness. |
| tangent neighboring sphere | Its intersection with $\Sigma$ is a single surface-null point. |
| coincident outer or inner sphere | Outer coincidence forces a duplicate center; inner coincidence would require $\alpha=1$. |
| limit point inside the neighbor | A small inward radial point would lie in both tile interiors. |
| $R<1$ as well as $R>1$ | The same invertible dilation works in both directions and preserves nullity. |
| $r=0$ | Excluded by the frozen scope; the inner boundary degenerates to a point, so no endpoint extension is imported. |
| $r=R$ | Excluded and essential: the separation radius vanishes. Under the closed-copy convention, the uncountable family of all radius-$R$ spheres has empty pairwise-disjoint interiors and can cover space, so the claimed closed-copy theorem must not be extended to this endpoint. |

No attempted construction using nested centers, tangencies, boundary-only
coverage, or an uncountable index set survives these checks.

## 7. Later comparison with the Round 21 materials

Only after the independent verdict above was fixed did I authenticate and
read the later comparison inputs:

| artifact | reproduced SHA-256 |
| --- | --- |
| Round 21 incumbent route | `67a622d4435f914a63190d8f0db5747aaaf7499422ac2e56adbc49b0ec7a5bca` |
| Round 21 clean-room proof | `6305b4a6d0441178fa8e81d111573bb81f4ff9b03a004b7c2175d504e69217f6` |
| typography addendum | `8f643b446d917f31596b8a7ad4effe6f6e2d18e399c93abfe7c89a3d3b6b9b55` |

All three hashes match the Round 22 scope audit.

The incumbent route uses equal tile volume to prove local finiteness, while
the frozen Round 22 packet requires an explicit contained-ball separation.
The finite-volume argument is valid (apply it to every finite subfamily),
and the clean-room proof supplies the stronger separation
`|a-b|>=1-alpha`. The independent reconstruction above supplies a different,
weaker but sufficient separation `(1-alpha)/2`.

The incumbent's phrases “approach ... through points lying just outside” and
“a finite union ... cannot cover” are terse. They do not conceal a gap: the
clean-room proof uses the positive-volume sets
$B(p,1/n)\cap\{|x|>1\}$ and explicitly uses zero surface measure for
the finite circle/point intersections. Sections 4 and 5 above independently
reconstruct the same two implications with exterior balls and surface
measure. The fixed-neighbor subsequence, boundary-versus-interior exclusion,
finite center set, tangent case, duplicate case, and scale-back all agree.

The typography addendum authenticates the immutable clean-room hash and
changes only two intended readings of the name `P` + `U+00F3` + `lya`.
Independent UTF-8 inspection found `U+00F3`, not `U+8D38`, in both the frozen
packet and clean-room report. No mathematical statement is altered.

Finally, the Round 22 scope audit correctly reports the exact theorem class,
all four coverage conventions, mandatory endpoint exclusions, graph
non-promotion, and the geometry-only/no-novelty boundary. Its PASS is
consistent with, but was not used to establish, this proof verdict.

## Final determination

**PASS. First unsupported implication: none.** The frozen claim is established
for precisely the family $0<r<R$ and the stated rigid-motion, disjoint-interior,
exact/almost-everywhere open/closed coverage conventions. No broader endpoint,
spectral, program-state, literature, novelty, or priority conclusion is part
of this verdict.
