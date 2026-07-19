# Independent audit: first-floor large-ray certificate

Date: 18 July 2026  
Audited note: `human/outbox/general-d-round-04-first-floor-large-ray.md`  
Audited verifier: `scripts/general_d_first_floor_ray_verify.py`

## Verdict

**PASS.**  I found no mathematical, interval-arithmetic, coverage, or
reproducibility error.  The stated conclusion

\[
 W>0\qquad
 (x\ge100,\ r\ge3/2,\ s\in\{0,1\})
\]

on the implicit wall \(A(x)=3/4\) follows from the displayed analytic
reductions and the exhaustive Arb branch-and-bound.  No correction to the
note or verifier is required.

This is deliberately a sector audit.  It does not enlarge the theorem to
the remaining \(s\ge2\) cone or to the finite small-\(x\) chambers.

## 1. Artifact identity and hygiene

At audit time the SHA-256 hashes were

```text
B5A0560F730FF9DF43885443F857C64D4CF0406601CBCB558F3672B52ED8519B  human/outbox/general-d-round-04-first-floor-large-ray.md
0ED04B5374BA54FD2B5018109F69CDFD6D19D712C4C4149E547F6478382544D6  scripts/general_d_first_floor_ray_verify.py
```

Both files decode as UTF-8.  The note has 9,534 bytes and 508 LF line
terminators; the verifier has 14,365 bytes and 455 LF line terminators.
Neither contains a NUL, tab, CR, or forbidden ASCII control byte.

## 2. Analytic replay

### 2.1 Wall compactification and the cone

Using

\[
 A(z)=\frac1\pi\int_\mu^K\sqrt{1-z^2/R^2}\,dR
\]

and \(R=x+u\) gives exactly

\[
 \frac{3\pi}{4}
 =\int_\beta^{\beta+\delta}
   \frac{\sqrt{u(2x+u)}}{x+u}\,du.
\]

If \(\delta\ge x-\beta\), the integration interval contains
\([x/2,x]\), because \(1\le\beta\le3\) and \(x\ge100\).  On that interval
the integrand is at least \(\sqrt5/3\), contradicting the wall identity.
Hence \(u<x\) throughout the wall integral.  Squaring verifies the two
pointwise bounds used in the note,

\[
 \sqrt{\frac{u}{2x}}
 \le \frac{\sqrt{u(2x+u)}}{x+u}
 \le \sqrt{\frac{2u}{x}}.
\]

The lower bound, together with
\((\beta+\delta)^{3/2}-\beta^{3/2}\ge\delta^{3/2}\), gives the stated
upper constant \(C\).  The upper bound and monotonicity in \(u\) give
the stated lower constant \(D\).  I independently recomputed the safety
margins at 512 bits:

```text
T_* - 100^(-1/3)              > 5.30996811627e-7
C                               = 2.923332817290565...
3571/1000 - (C+3 T_*)         > 1.33518270943e-3
D - 22/25                     > 1.82502393538e-3
583/500 - (1+(3571/1000)T_*^2)> 2.48045707344e-4
```

Thus \(22/25<\kappa<731/250\) is a valid closed enlargement of every
actual wall point.

### 2.2 The bound \(P<41\) at a possible failure

For \(f_z(R)=\sqrt{1-z^2/R^2}\), direct rationalization gives

\[
 f_r-f_x
 =\frac{x^2-r^2}{R^2(f_r+f_x)}
 \ge
 \frac{x^2-r^2}{2K\sqrt{K^2-r^2}}.
\]

The inequalities

\[
 x^2-r^2=p(2x-p)\ge px,
 \quad K-r\le(B_0+P)x^{1/3},
 \quad K+r<(C_K+1)x
\]

then reproduce (9) with the correct direction.  Dividing the necessary
failure inequality by \(\sqrt{B_0+P}\) is legitimate, and
\(P/\sqrt{B_0+P}\) is strictly increasing.  At \(P=41\), the reverse
inequality has the rigorous 512-bit margin

```text
(22/25)P - pi(583/500)sqrt((1083/500)(P+3571/1000))
    > 0.0881775052717.
```

The compact \(\Phi_r\) radicand also retains the uniform margin
\(2-41T_*^2>0.096939197424\).  Consequently every possible failure has
\(0\le P<41\).  The use of the earlier wall reduction is correct:
\(v>1/4\), and a failure requires \(p\ge1\) and
\(0<A(r)-3/4<1/2\); hence \(A(r)\ge5/4\) is indeed automatic.

### 2.3 Exact scaled profiles and concavity quadrature

Substitution of

\[
 x=t^{-3},\quad p=P/t,\quad
 R=x+(\beta t+\xi\kappa)/t
\]

reproduces, without approximation,

\[
 f_x=t\Phi_x,\qquad f_r=t\Phi_r,\qquad f_y=t\Phi_y.
\]

All factors in the three radicands are nonnegative on the certified cone,
including its \(t=0\) face.  Differentiating the radius profile gives

\[
 f_z'(R)=\frac{z^2}{R^3f_z(R)}>0,
 \qquad
 f_z''(R)=-\frac{3z^2}{R^4f_z(R)}
           -\frac{z^4}{R^6f_z(R)^3}<0.
\]

Therefore the composite trapezoid is a lower bound and the composite
midpoint rule is an upper bound on each of the two panels.  Since
\(A(z)=(\kappa/\pi)\int_0^1\Phi_z(\xi)\,d\xi\), equations (17)--(19)
have the correct normalization and orientation.  The endpoint singularity
when \(s=0,\beta=1,\xi=0\) is harmless: the profile is continuous and
concave there, and the verifier takes the rigorous semipositive square-root
hull.

### 2.4 Enclosure of every implicit wall root

For fixed \((t,\beta)\), increasing \(\kappa\) both lengthens the radius
interval and increases all noninitial radius nodes, so both quadrature
endpoint expressions are increasing.  In the code:

* an upper endpoint of the midpoint expression below \(3/4\) certifies a
  common lower bound for every root in a \((t,\beta)\)-box;
* a lower endpoint of the trapezoid expression above \(3/4\) certifies a
  common upper bound;
* if the latter test is unresolved at \(731/250\), the outer box is split.

Thus `wall_kappa_enclosure` encloses all wall-compatible roots and never
substitutes a sampled root.  Dropping the correlation between this root
interval and \((t,\beta)\) only enlarges later interval evaluations, so it
cannot create a false positive.

### 2.5 Product transition and terminal reserve

The established slope envelope gives

\[
 v-\lambda S_y\ge\frac34-\lambda S_x=H,
\]

and direct substitution gives exactly formula (20).  If \(H>0\), the
anchored terminal profile is at least \(H\) on all of \([y,\mu]\), hence

\[
 \mathcal E\ge2LH+H^2/c.
\]

Writing \(u=t^2\vartheta\) yields the exact identity

\[
 \arccos\frac1{1+u}
 =\arctan\sqrt{(1+u)^2-1}.
\]

Then \(\arctan z\le z\) proves \(c/t\le Q\), including the continuous
limit at \(t=0\).  Multiplication of (1) by \(t\) gives (24) with no lost
factor.  The verifier lowers its terms safely: the far \(P\)-endpoint is
used when the shelf defect is negative, the appropriate \(t\)-endpoint is
chosen according to the terminal bracket's sign, and
\(H_{\rm lo}^2/Q_{\rm hi}\) is used only after proving \(H_{\rm lo}>0\).

## 3. Domain and exhaustive branch dispositions

The box

\[
 0\le t\le T_*,\quad s+1\le\beta\le s+2,
 \quad0\le P\le41
\]

contains the closure of every asserted parameter point; using
\(\alpha=1\) merely closes the actual half-open chamber.  The condition

\[
 1-Pt^2-\frac32t^3\ge0
\]

is exactly \(r\ge3/2\) after multiplication by \(t^3\).  A box is accepted
only if it is rigorously outside this domain, has the quadrature lower bound
\(A(r)\ge5/4\), or has both \(H>0\) and a strictly positive lower endpoint
for the scaled certificate.  Boxes intersecting the domain boundary are
not discarded.  Binary floating point affects queue order and diagnostics
only; all acceptance tests are Arb comparisons.

## 4. Independent replays

The unmodified verifier at 384 bits reproduced the note exactly:

```text
s=0: processed=17697, invalid=4, automatic=170, positive=8675,
     max-depth=21, smallest diagnostic margin ~4.6662136e-06
s=1: processed=25367, invalid=5, automatic=140, positive=12539,
     max-depth=22, smallest diagnostic margin ~1.96594471e-06
total processed=43064
```

I then executed the same source in memory with only `ctx.prec` changed to
512 bits.  Every count and printed margin was identical.

As a stress replay, I executed it at 768 bits and tightened each common
wall-root bisection from 18 to 24 steps.  This independent enclosure
granularity also passed:

```text
s=0: processed=17695, invalid=4, automatic=170, positive=8674,
     max-depth=21, smallest diagnostic margin ~4.14820523e-06
s=1: processed=25363, invalid=5, automatic=140, positive=12537,
     max-depth=22, smallest diagnostic margin ~2.47690037e-06
total processed=43058
```

The small count change is expected from the tighter wall interval; every
leaf again received one of the three rigorous dispositions.  These
higher-precision/stress replays did not modify either audited artifact.

## 5. Final scope statement

The certificate rigorously removes the continuous large ray

\[
 r\ge3/2,\qquad s\in\{0,1\},\qquad x\ge100.
\]

It does not certify the \(s\ge2\) cone, the finite \(s=0,1, x<100\)
half-grid set, or the already bounded small-start rays.  The source note
states these residual obligations accurately.
