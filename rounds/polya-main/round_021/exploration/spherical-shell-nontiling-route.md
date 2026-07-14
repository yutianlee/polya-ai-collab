# Round 21 exploration: spherical shells do not tile

Status: **INCUMBENT PROGRAM-SCOPE ARGUMENT / NOT INDEPENDENTLY REVIEWED**.

## Statement and convention

For \(0<r<R\), let

\[
S_{r,R}=\{x\in\mathbb R^3:r<|x|<R\}.
\]

Under the standard spectral-geometric tiling convention, a congruent tiling
has pairwise disjoint interiors and covers \(\mathbb R^3\) up to a null set
(the conclusion is therefore also valid for an everywhere-covering tiling).
Every congruent copy of a spherical shell is a translate, because rotations
leave the shell invariant.

The claim is that no \(S_{r,R}\) with \(0<r<R\) admits such a congruent
tiling of \(\mathbb R^3\).

## Proof

Scale to \(R=1\) and write \(\rho=r/R\).  Suppose, for contradiction, that
the translates

\[
T_j=c_j+S_{\rho,1}
\]

tile \(\mathbb R^3\) in the stated sense.

First, the family is locally finite.  If \(T_j\) meets a fixed ball
\(B(0,M)\), then \(|c_j|<M+1\), and the whole copy lies in \(B(0,M+2)\).
The interiors of all such copies are disjoint and each has the same positive
volume

\[
v=\frac{4\pi}{3}(1-\rho^3).
\]

Consequently there are at most

\[
\frac{|B(0,M+2)|}{v}
\]

copies meeting \(B(0,M)\).  In particular, only finitely many tile
boundaries occur near any fixed compact set, and the full family is
countable.  Its union of spherical boundaries is therefore null.

Fix one tile \(T_0\), with center \(c_0\), and its outer sphere

\[
\Sigma=\{x:|x-c_0|=1\}.
\]

For every \(x\in\Sigma\), approach \(x\) through points lying just outside
the closed outer ball of \(T_0\).  Because the uncovered set has measure
zero and the countable boundary union is also null, the approaching points
can be chosen in tile interiors.  Local
finiteness permits passage to a subsequence contained in one fixed tile
\(T_j\ne T_0\).  Hence \(x\in\overline{T_j}\).  The point \(x\) cannot be an
interior point of \(T_j\): any neighborhood of \(x\) also meets the interior
of \(T_0\), which would give an open overlap.  Thus \(x\in\partial T_j\).

Only finitely many \(T_j\) occur near \(\Sigma\), so this proves

\[
\Sigma\subseteq\bigcup_{j\in F,\,j\ne0}\partial T_j
\tag{1}
\]

for a finite set \(F\).  Each \(\partial T_j\) is the union of two spheres,
of radii \(\rho\) and \(1\), centered at \(c_j\).  Two distinct spheres in
\(\mathbb R^3\) meet in at most a circle or a point, so their intersection
has empty relative interior in \(\Sigma\).  A finite union of such
intersections cannot cover \(\Sigma\).  Equation (1) therefore forces one
boundary sphere of some \(T_j\) to coincide with \(\Sigma\).

The inner sphere cannot coincide with \(\Sigma\), because its radius is
\(\rho<1\).  Coincidence with the outer sphere forces \(c_j=c_0\), hence
\(T_j=T_0\), contradicting \(j\ne0\) and the disjoint-interior condition.
This contradiction proves the claim.

## Scope boundary

This argument proves geometric non-tiling only.  It does not prove the
spectral inequality, publication priority, or the word “first.”  Before a
program-target promotion it requires a separate clean review of local
finiteness, the almost-everywhere covering step, the finite sphere-cover
argument, and the scaling from \(S_{\rho,1}\) to \(S_{r,R}\).
