# Independent audit: Round 9b first-floor level-wall reduction — FINAL PASS

Date: 18 July 2026

Audited target:

```text
human/outbox/general-d-round-09-no-drop-f1-level-wall-reduction.md
```

Target SHA-256 at audit time:

```text
98DD0AF1B62EC1966A0C548BC3968E0F311D7BAF780488750B0B79C195F5EA1D
```

Dependency checked for the compact residual reduction:

```text
human/outbox/general-d-round-09-no-drop-f1-small-s.md
SHA-256 F1CEC41FD1A7807406F929E46AC2E5AE691104A9DDFBA04CF9958F0CB283A553
```

## 1. Verdict and exact scope

**FINAL PASS for the exact level-wall reduction, the normalized algebra,
and the compact certificate specification.**

This verdict does **not** certify either remaining sign assertion

\[
 P_0\geq0,
 \qquad P_1\geq0.
\]

It therefore does not prove the global \(f=1\) tail theorem or even the
remaining compact \(f=1,\ p=n\) chambers.  The target states this limitation
in its opening status paragraph, immediately after Proposition 4.1, and in
its final paragraph.  I found no closure overclaim.

The target note was not edited during this audit.

## 2. One-level tail identity

Put \(b=3/4\).  The ordinary first-floor hypothesis is

\[
 b\leq A(r)<b+1.
\]

Since \(A\) is continuous and strictly decreasing and \(A(K)=0\), whenever
\(A(r)>b\) there is a unique \(y\in(r,K)\) with \(A(y)=b\).  For every
integer \(j\geq0\), monotonicity and \(A(r)<7/4\) give

\[
 [A(r+j)+1/4]_<
 =\mathbf1_{\{r+j<y\}}.
\]

Let \(d=y-r>0\).  The positive interior indices are precisely the positive
integers \(j<d\), of which there are \(\lceil d\rceil-1\).  Hence

\[
 T_A(r)=1+2(\lceil d\rceil-1)
 =2\lceil y-r\rceil-1.
\]

This also reproduces the strict value at a positive integral wall
\(d=L\geq1\), namely \(2L-1\).  If \(A(r)=b\), then \(y=r\) in the limiting
sense, every strict bracket is zero, and the defect is automatically
nonnegative.  Thus the target's separate treatment of \(L=0\) is necessary
and correct.

The derivation depends only on the global \(3/4\)-level and not on the
interface index.  It really does cover both first-drop and no-drop
first-floor tails.

## 3. Strict wall ownership and the \(K\)-deformation

Fix \((\mu,r)\).  Since

\[
 \partial_KG_K(z)=\frac1\pi\sqrt{1-z^2/K^2}>0
 \qquad(z<K),
\]

the action and the level position \(y\) increase strictly with \(K\).
Inside a chamber with

\[
 P=\lceil y-r\rceil
\]

fixed, the tail count is fixed, the moving-endpoint term vanishes because
\(A(K)=0\), and direct differentiation gives

\[
 \partial_KD_A(r)
 =\frac2\pi\int_r^K\sqrt{1-z^2/K^2}\,dz>0.
\]

Lowering \(K\) therefore lowers the defect until the chamber's lower
level wall is reached.  Write

\[
 y-r=L=P-1\in\mathbb Z_{\geq0}.
\]

The value inherited from the open chamber retains \(2P-1=2L+1\) count
units and is exactly

\[
 \mathcal F(r;K,\mu,y)
 =2\int_r^KA(z)\,dz-2(y-r)-1.
\]

At the strict equality face, the actual count is \(2L-1\) for \(L\geq1\),
so the actual wall defect is \(\mathcal F+2\).  For \(L=0\), the actual
count is zero rather than the open-side value one, and the gain is one.

In the no-drop row, \(A(q)\geq b\) implies \(y\geq q=r+n\).  Thus an
integral level wall has \(L=y-r\geq n\geq1\), and its gain is always the
full two units.  These count conventions agree with the strict bracket at
every equality.  No count is passed through a wall by continuity.

There is also no hidden terminal boundary in the deformation.  If
\(P=1\), the lower chamber boundary is the activation wall \(A(r)=b\),
which is exactly the \(L=0\) case.  For \(P>1\), a positive integral level
is reached first.

## 4. Continuous elimination of the lattice start

At a fixed level wall \((K,\mu,y)\), relaxing the discrete start to
\(0\leq r\leq y\) can only lower the target.  Differentiating gives the
exact identity

\[
 \partial_r\mathcal F
 =-2A(r)+2=2(1-A(r)).
\]

Also

\[
 A(0)=\frac{K-\mu}{\pi}=\frac\delta\pi.
\]

If \(\delta\leq\pi\), then \(A(r)\leq A(0)\leq1\), so \(\mathcal F\)
is nondecreasing and its relaxed minimum is at \(r=0\).  The exact ball
area

\[
 2\int_0^aG_a(z)\,dz=\frac{a^2}{4}
\]

then gives

\[
 \mathcal F_0
 =\frac{K^2-\mu^2}{4}-2y-1.
\]

If \(\delta>\pi\), strict decrease of \(A\) and
\(A(y)=3/4<1<A(0)\) give a unique \(z\in(0,y)\) with \(A(z)=1\).
The derivative is negative before \(z\) and positive after \(z\), so the
relaxed minimum is at \(r=z\):

\[
 \mathcal F_1
 =J_K(z)-J_\mu(z)-2(y-z)-1.
\]

At \(\delta=\pi\), one has \(z=0\), and the two formulas coincide.  This
proves the two-case minimization and Proposition 4.1 exactly as stated.

## 5. Re-derivation of the normalized targets

Let \(g=G_1\), \(x=y/K\), and

\[
 a_\rho(t)=g(t)-\rho g(t/\rho)
 =\frac1\pi\int_\rho^1
 \left(1-\frac{t^2}{v^2}\right)_+^{1/2}\,dv.
\]

Homogeneity gives

\[
 A(Kt)=K a_\rho(t).
\]

Thus the level equation \(A(y)=b\) gives

\[
 K=\frac ba,
 \qquad y=\frac{bx}{a},
 \qquad a=a_\rho(x).
\]

Moreover

\[
 A(0)=\frac{b(1-\rho)}{\pi a}.
\]

For the lower-width target,

\[
 \mathcal F_0
 =\frac{b^2(1-\rho^2)}{4a^2}
 -\frac{2bx}{a}-1.
\]

Multiplication by \(4a^2>0\) gives exactly

\[
 P_0=b^2(1-\rho^2)-8bxa-4a^2.
\]

For the active target, put \(u=z/K\).  The unit-level equation is

\[
 K a_\rho(u)=1
 \quad\Longleftrightarrow\quad
 a_\rho(u)=\frac ab.
\]

Strict decrease of \(a_\rho\) makes this root unique, and because
\(1>b\), one has \(0\leq u<x\).  With

\[
 j_\rho(u)=2\int_u^1a_\rho(t)\,dt,
\]

homogeneity gives

\[
 J_K(z)-J_\mu(z)=K^2j_\rho(u).
\]

Hence

\[
 \mathcal F_1
 =\frac{b^2}{a^2}j_\rho(u)
 -\frac{2b}{a}(x-u)-1,
\]

and multiplication by \(a^2\) gives precisely

\[
 P_1=b^2j_\rho(u)-2ba(x-u)-a^2.
\]

I also independently checked the swapped positive representation

\[
 j_\rho(u)=\frac2\pi
 \int_{\max\{\rho,u\}}^1
 \int_u^v\sqrt{1-t^2/v^2}\,dt\,dv
\]

by changing the order in the positive radius-average formula.  No nearby
radius subtraction is required by the proposed verifier.

## 6. Geometric constraints and compact residual domain

The general first-floor condition has \(y\geq r\geq1/2\), which gives

\[
 a\leq2bx=\frac32x.
\]

For the no-drop row, \(y\geq q=r+n\geq3/2\), so

\[
 a\leq\frac{x}{2}.
\]

Since \(A(0)>A(y)=b\), division by positive quantities gives

\[
 1-\rho>\pi a.
\]

The active condition \(A(0)\geq1\) is exactly

\[
 b(1-\rho)\geq\pi a.
\]

The independently proved small-\(s\) theorem says that a remaining
negative no-drop candidate has

\[
 s>\frac1{10},
 \qquad K<\frac{33000}{7},
 \qquad 1\leq n\leq754.
\]

Since \(s^2=1-\rho\) and \(a=b/K\), these imply

\[
 \rho<\frac{99}{100},
 \qquad
 a>\frac{(3/4)7}{33000}=\frac7{44000}.
\]

Passing to the closure gives the weak inequalities in the target's domain
(31).  The lower bound on \(a\), together with \(a\leq x/2\), keeps
\(x\) away from zero; and \(a_\rho(x)\leq g(x)\) keeps \(x\) away from
one.  Thus the displayed set, interpreted with its harmless closure faces,
is genuinely compact and avoids \(\rho=1\) and \(a=0\).

The derivative minimization has already relaxed away \(r\), and hence the
integer \(n\).  Certifying \(P_1\geq0\) on this enlarged continuous domain
is therefore sufficient; a loop over \(1\leq n\leq754\) is not logically
needed.

## 7. Independent diagnostic searches

The following searches used ordinary double precision only and have no
proof status.  They were used to look for algebraic or sign counterexamples.

1. I sampled 20,000 physical \((K,\mu,r)\) triples and retained 4,797
   first-floor chambers for which the lower level wall could be isolated.
   In every retained chamber,
   \[
   D_A(r)-\mathcal F_{\rm lower\ wall}>0.
   \]
   The smallest observed difference was approximately
   \(1.2292764\times10^{-4}\), occurring extremely close to its wall.

2. On 10,000 random active normalized walls, the largest absolute error in
   the identity
   \[
   P_1=a^2\mathcal F_1
   \]
   was below \(9.5\times10^{-17}\).

3. One million random points were tested against the necessary constraints
   of the compact domain (31).  Among 396,946 feasible points, the smallest
   observed \(P_1\) was approximately
   \(4.02\times10^{-7}>0\).  This search included logarithmic bias toward
   small \(x\), the lower cutoff \(a=7/44000\), and the active boundary.

4. A separate million-point scan of the lower-width domain found no
   negative \(P_0\); the smallest observed value was about
   \(3.94\times10^{-7}\).

5. Substitution in the diagnostic example printed in the target reproduced
   \(A(q)=0.7500000066\ldots\),
   \(A(r)=1.0039940419\ldots\), and the open-side level-wall scalar
   \(1.0758944533\ldots\).

These diagnostics support the proposed certificate, but they are not a
replacement for the directed-Arb proof of \(P_1>0\).

## 8. Scope and formatting audit

- All 50 display-math openings have matching closures.
- The ordinary-floor and strict-bracket conventions are kept distinct.
- The target explicitly labels the old exact-angle expression as a failed
  lower bound, not as a counterexample to the shifted-tail inequality.
- The executable design treats a depth or box cap as failure and requests
  higher-precision replay, source hashing, and exact leaf coverage.
- The target makes no claim that the proposed verifier has already run.
- The final conclusion again calls the result an exact reduction and
  certificate plan, not a closure theorem.

Accordingly the reduction and its stated scope pass this independent audit.
The next required mathematical artifact is the directed-Arb certificate for
\(P_1>0\) on domain (31).
