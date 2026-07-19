# Independent audit: complete first-floor small-start closure

Date: 18 July 2026  
Audited note: `human/outbox/general-d-round-05-first-floor-small-starts.md`  
Audited verifier: `scripts/general_d_first_floor_small_starts_verify.py`

## Verdict

**PASS.**  I independently checked the analytic ray, the finite enumeration,
the implicit-wall panel bounds, and the strict-wall and geometric endpoint
conventions.  I also replayed the unchanged verifier at 384 and 512 bits and
performed a stronger 1024-bit stress run with 200 exact rational root
bisections.  All three runs give identical chamber, panel, leaf, root, split,
and depth counts.

No change to the note or verifier was needed.  Their final SHA-256 digests are

```text
69369808D0E57879F818EAA1BCB2F180A9FF3BBE1193C0AE3EE1476712E855FC  human/outbox/general-d-round-05-first-floor-small-starts.md
BE36F88750456016B11E129D4EC7C4CEFB4E5CADDEE1476FDFDDBB4B45821BE7  scripts/general_d_first_floor_small_starts_verify.py
```

The imported finite-wall core is exactly the independently audited source:

```text
9F7C35279FD1E3FC47BF53C26A7D8681527703FE092BC3AA0831BD160609598D  scripts/general_d_first_floor_finite_verify.py
```

Both newly audited artifacts decode as UTF-8, contain no forbidden ASCII
control bytes, and the verifier passes `py_compile`.

## 1. Independent derivation of the analytic ray

Put

\[
 x=r+p,\qquad \beta=\mu-x=s+1+\alpha,\qquad
 \delta=K-\mu .
\]

For the asserted sector, \(x\geq100\), \(r\in\{1/2,1\}\),
\(s\in\{0,1\}\), and \(0\leq\alpha\leq1\), so
\(1\leq\beta\leq3\).  The implicit wall \(A(x)=3/4\) is exactly

\[
 \frac{3\pi}{4}
 =\int_\mu^K\sqrt{1-\frac{x^2}{R^2}}\,dR
 =\int_\beta^{\beta+\delta}
   \frac{\sqrt{v(2x+v)}}{x+v}\,dv.                 \tag{1}
\]

### 1.1 Wall thickness

Suppose \(\delta\geq x-\beta\).  Because \(\beta\leq3<x/2\), the
integration interval in (1) then contains \([x/2,x]\).  The squared
integrand is

\[
 1-\frac{x^2}{(x+v)^2},
\]

which increases with \(v\), and its value at \(v=x/2\) is \(5/9\).
Consequently the right side of (1) would be at least

\[
 \frac{x}{2}\frac{\sqrt5}{3}=\frac{x\sqrt5}{6}.
\]

At \(x=100\), this already exceeds \(3\pi/4\), and the lower bound
increases with \(x\).  Thus

\[
 \delta<x-\beta.                                  \tag{2}
\]

In particular every \(v\) in (1) is smaller than \(x\).  Direct squaring
then gives

\[
 \frac{\sqrt{v(2x+v)}}{x+v}\geq\sqrt{\frac{v}{2x}},
\]

because this inequality is equivalent to \(v^2\leq3x^2\).  Since

\[
 (\beta+\delta)^{3/2}-\beta^{3/2}\geq\delta^{3/2},
\]

equation (1) yields

\[
 \delta\leq
 \left(\frac{9\pi\sqrt2}{8}\right)^{2/3}x^{1/3}
 =Cx^{1/3}.                                       \tag{3}
\]

The directed-rounding check in the verifier proves

\[
 C=2.923332817290565\ldots<\frac{731}{250}.
\]

### 1.2 The bound \(K/x<6/5\)

Let \(t=x^{-1/3}\) and

\[
 T_*=\frac{53861}{250000}.
\]

The verifier proves with Arb that \(T_*>100^{-1/3}\).  Hence
\(t<T_*\) on the entire ray.  From \(K=x+\beta+\delta\),
\(\beta\leq3\), and (3),

\[
 \frac Kx
 <1+3T_*^3+\frac{731}{250}T_*^2
 =\frac{18214389817600143}{15625000000000000}
 =1.165720948326409\ldots<\frac65.                \tag{4}
\]

The middle comparison is exact rational arithmetic.  Thus neither a
floating-point approximation nor a sampled wall root enters (4).

### 1.3 Derivative ratio and \(A(r)>5/4\)

For \(z<x<R\), define

\[
 f_z(R)=\sqrt{1-\frac{z^2}{R^2}}.
\]

Then

\[
 \left(\frac{f_r(R)}{f_x(R)}\right)^2
 =\frac{R^2-r^2}{R^2-x^2}.
\]

This ratio decreases as \(R^2\) increases because \(r<x\).  Its minimum
on \([\mu,K]\) is therefore at \(K\).  Using \(r\leq1\) and (4),

\[
 \begin{aligned}
 \left(\frac{f_r(R)}{f_x(R)}\right)^2
 &\geq\frac{K^2-r^2}{K^2-x^2}\\
 &>\frac{36x^2-25}{11x^2}\\
 &\geq\frac{14399}{4400}
  =3.2725>\frac{25}{9}.
 \end{aligned}                                    \tag{5}
\]

The strict middle inequality follows by evaluating the decreasing rational
function at the strict upper bound \(K^2<(36/25)x^2\); the last lower bound
is attained at \(x=100\).  Hence \(f_r>(5/3)f_x\) pointwise and

\[
 A(r)=\frac1\pi\int_\mu^Kf_r(R)\,dR
 >\frac53\frac1\pi\int_\mu^Kf_x(R)\,dR
 =\frac53A(x)=\frac54.                            \tag{6}
\]

### 1.4 The first drop and positivity

Put \(v=A(x+1)\).  On the inner branch,

\[
 \sigma(z):=-A'(z)
 =\frac{\arccos(z/K)-\arccos(z/\mu)}{\pi}
\]

is strictly increasing, and

\[
 \sigma(\mu)=\frac{\arccos(\mu/K)}{\pi}<\frac12.
\]

Since \(x+1\leq\mu\), integration over the unit cell gives strictly

\[
 \frac34-v=A(x)-A(x+1)<\frac12,
 \qquad v>\frac14.                                \tag{7}
\]

Equations (6) and (7), together with the nonnegative terminal reserve,
make the previously derived weakened wall certificate

\[
 p\left(A(r)-\frac54\right)+v-\frac14+\mathcal E
\]

strictly positive, including \(p=0\).

As an independent cross-check, the stronger true-interface certificate
used in the finite computation also closes the ray directly.  At the wall
it can be rewritten as

\[
 \mathcal C=
 p\left(A(r)-\frac54\right)
 +(s+1)\left(\frac34+A(q)\right)-1
 +\alpha(A(q)+G_K(\mu))+\frac{G_K(\mu)^2}{c}.
\]

For \(s=0\), \(q=x+1\), and its second term is
\(A(x+1)-1/4>0\).  For \(s=1\), that term is
\(1/2+2A(q)>0\).  All remaining terms are nonnegative, while (6) is
strict.  This gives a second proof of wall positivity that does not use a
numerical terminal-envelope evaluation.

## 2. Audit of the finite certificate

The new verifier does not duplicate the implicit-wall implementation.  It
imports `general_d_first_floor_finite_verify.py`, hashes the resolved source
file, and exits unless that hash is the audited digest displayed above.
The imported code was therefore inspected again in the small-start domain.

For fixed \(x\), the equation

\[
 \int_\mu^{K(\mu)}f_x(R)\,dR=\frac{3\pi}{4}
\]

has one root: its left side is zero at \(K=\mu\), tends to infinity, and
has positive \(K\)-derivative.  Exact rational bisection produces strict
brackets \(K_i^-<K(\mu_i)<K_i^+\), with every endpoint sign decided by
Arb.  An undecidable sign raises an exception.

Implicit differentiation gives

\[
 K'(\mu)=\frac{f_x(\mu)}{f_x(K)}\in(0,1).
\]

For a fixed sample \(z\),

\[
 \frac d{d\mu}A(z)=\frac{f_x(\mu)}\pi
 \left(\frac{f_z(K)}{f_x(K)}-
       \frac{f_z(\mu)}{f_x(\mu)}\right).
\]

Because

\[
 \left(\frac{f_z(R)}{f_x(R)}\right)^2
 =\frac{R^2-z^2}{R^2-x^2},
\]

this proves that \(A(r)\) is nonincreasing and \(A(q)\) is increasing
along the wall.  The same direct differentiation gives that
\(h=G_K(\mu)\) and \(c=\arccos(\mu/K)/\pi\) decrease.  Therefore, on an
exact panel \(\alpha_0\leq\alpha\leq\alpha_1\), the core correctly uses

\[
 \begin{aligned}
 a_-&=G_{K_1^-}(r)-G_{\mu_1}(r),\\
 u_-&=G_{K_0^-}(q)-G_{\mu_0}(q),\\
 h_-&=G_{K_1^-}(\mu_1),\\
 c_+&=\pi^{-1}\arccos(\mu_0/K_0^+)
 \end{aligned}
\]

in the rigorous lower bound

\[
 p(a_-+3/4)+(n-p)(3/4+u_-)
 +\alpha_0(u_-+h_-)+\frac{h_-^2}{c_+}-(1+2p).
\]

All proxies are positive.  The complete Arb interval must be strictly
positive before a panel is accepted.  Binary floating point is used only
for the printed diagnostic midpoint.

## 3. Exact coverage and endpoint conventions

For \(r=1/2\), the condition \(r+p<100\) gives exactly
\(0\leq p\leq99\), or 100 chambers for each \(s\).  For \(r=1\), it
gives \(0\leq p\leq98\), or 99.  Thus the enumeration contains

\[
 2(100+99)=398
\]

and no admissible chamber is omitted.

An actual geometric chamber has \(0\leq\alpha<1\).  The verifier checks
the larger closed interval \([0,1]\).  At \(\alpha=0\), the segment
\([q,\mu]\) has zero length and its certificate term vanishes.  At
\(\alpha=1\), the same formulas are the continuous limiting face of the
half-open chamber.  The inner chord decomposition and the post-crossing
count bound remain valid, so including this endpoint is conservative.

The ordinary first-floor chamber lies on the side \(A(x)>3/4\).  For
fixed \(\mu,r,p,s\), all positive terms in the unspecialized certificate
increase with \(K\), so its minimum is the right-hand post-crossing limit
at the unique wall \(A(x)=3/4\).  At equality, the spectral bracket is
strict; its exact count can only be smaller than the paid post-crossing
count \(1+2p\).  Thus the wall calculation has the safe convention and
there is no equality gap.

## 4. Independent executions

The unchanged verifier was run in three fresh processes:

| precision | root steps | chambers | panels | leaves | roots | max depth |
|---:|---:|---:|---:|---:|---:|---:|
| 384 | 110 | 398 | 420 | 409 | 807 | 1 |
| 512 | 110 | 398 | 420 | 409 | 807 | 1 |
| 1024 | 200 | 398 | 420 | 409 | 807 | 1 |

Every run identified exactly the same eleven subdivided \(s=0\) chambers:

```text
(r,p)=(1/2,4),(1/2,5),(1/2,6),(1/2,7),(1/2,8),(1/2,9)
(r,p)=(1,4),(1,5),(1,6),(1,7),(1,8)
```

Each is resolved by the two leaves \([0,1/2]\) and \([1/2,1]\); every
other chamber is accepted on \([0,1]\).  The smallest displayed midpoint
is \(0.0084055719981\ldots\), but this number is diagnostic only.  The
proof is the strict positive lower endpoint of every accepted Arb interval.

## 5. Scope

The audit certifies the full two-small-start sector

\[
 r\in\left\{\frac12,1\right\},\qquad
 s=n-p-1\in\{0,1\},\qquad p\geq0.
\]

Together with the separately audited finite and large-ray results for
\(r\geq3/2\), it closes the entire half-grid sector \(s\in\{0,1\}\).
It does not address the residual \(s\geq2\) cone.
