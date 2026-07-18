# General dimension, Round 5: complete closure of the two first-floor small starts

Date: 18 July 2026  
Scope: the ordinary first-floor first-drop branch
\(F_0=1,\ p<n\), with

\[
 r\in\left\{\frac12,1\right\},\qquad
 s=n-p-1\in\{0,1\}.
\]

Status: **proved for every \(p\geq0\)**. The finite range \(x=r+p<100\)
is certified by the stronger true-interface certificate at 384-bit
directed-rounding Arb precision and independently replayed at 512 bits.
A 768-bit, 160-root-step stress replay gives identical coverage. The ray
\(x\geq100\) is closed analytically by showing \(A(r)>5/4\) at the
first-shelf wall.

This note does not edit either manuscript. The verifier is

`scripts/general_d_first_floor_small_starts_verify.py`.

Its SHA-256 digest is

`BE36F88750456016B11E129D4EC7C4CEFB4E5CADDEE1476FDFDDBB4B45821BE7`.

## 1. Exact wall setup

Write

\[
 A(z)=G_K(z)-G_\mu(z),\qquad
 G_R(z)=\frac{\sqrt{R^2-z^2}-z\arccos(z/R)}{\pi},
\]

and put

\[
 x=r+p,\qquad q=r+n=x+s+1,\qquad
 \mu=q+\alpha,\qquad 0\leq\alpha\leq1.
 \tag{1}
\]

The actual chamber has \(0\leq\alpha<1\). Including \(\alpha=1\) gives
the closed limiting face and is conservative.

On the ordinary first shelf,

\[
 A(r+j)\geq\frac34\quad(0\leq j\leq p),
 \qquad A(x+1)<\frac34.
\]

For fixed \((\mu,r,p,s)\), every certificate term increases with \(K\).
Consequently the minimum in the post-crossing chamber is attained in the
right-hand limit at the unique wall

\[
 \boxed{A(x)=\frac34.}                            \tag{2}
\]

Existence and uniqueness follow because the left side of (2) is zero at
\(K=\mu\), tends to infinity with \(K\), and has strictly positive
\(K\)-derivative.

## 2. The stronger true-interface certificate

At the wall put

\[
 a=A(r),\qquad b=A(x)=\frac34,\qquad
 u=A(q),\qquad h=G_K(\mu),\qquad
 c=\frac1\pi\arccos\frac\mu K.
\]

The action \(A\) is concave on the inner branch. The chord inequalities on
\([r,x]\), \([x,q]\), and \([q,\mu]\) give

\[
 2\int_r^xA\geq p(a+b),\qquad
 2\int_x^qA\geq(n-p)(b+u),\qquad
 2\int_q^\mu A\geq\alpha(u+h).
\]

On \([\mu,K]\), \(A=G_K\) is convex, has value \(h\), and has slope
\(-c\) at \(\mu\). Its positive tangent triangle gives

\[
 2\int_\mu^K G_K\geq\frac{h^2}{c}.
\]

The post-crossing discrete count is \(1+2p\). At the exact strict wall
the count can only be smaller, so it is wall-safe to prove positivity of

\[
 \boxed{
 \mathcal C=
 p(a+b)+(n-p)(b+u)+\alpha(u+h)
 +\frac{h^2}{c}-(1+2p).}                          \tag{3}
\]

For fixed \(\mu\), the sampled actions in (3) increase with \(K\). The
outer term increases too. If \(\theta=\arccos(\mu/K)\), then

\[
 \frac{h^2}{c}
 =\frac{\mu^2}{\pi}
 \frac{(\tan\theta-\theta)^2}{\theta},
\qquad
 \tan\theta-\theta=\int_0^\theta\tan^2v\,dv
 <\theta\tan^2\theta.
\]

Thus (2) is the correct minimum, not a sampled surrogate.

## 3. Correlated wall panels

For fixed \(x\), write the wall root as \(K=K(\mu)\) and put

\[
 f_z(R)=\sqrt{1-\frac{z^2}{R^2}}.
\]

Implicit differentiation of

\[
 \int_\mu^{K(\mu)}f_x(R)\,dR=\frac{3\pi}{4}
\]

gives

\[
 K'(\mu)=\frac{f_x(\mu)}{f_x(K)}\in(0,1).         \tag{4}
\]

For a fixed sample \(z\),

\[
 \frac d{d\mu}A(z)
 =\frac{f_x(\mu)}{\pi}
 \left(
 \frac{f_z(K)}{f_x(K)}
 -\frac{f_z(\mu)}{f_x(\mu)}
 \right).                                         \tag{5}
\]

Since

\[
 \left(\frac{f_z(R)}{f_x(R)}\right)^2
 =\frac{R^2-z^2}{R^2-x^2},
\]

equation (5) shows that \(A(r)\) decreases and \(A(q)\) increases along
the wall. The same audited calculation shows that \(h\) and \(c\) both
decrease.

On an exact rational panel
\(\alpha_0\leq\alpha\leq\alpha_1\), the verifier isolates the two wall
roots by 110 steps of exact rational bisection:

\[
 K_i^-<K(q+\alpha_i)<K_i^+.
\]

The correlated monotonicities give

\[
 a_-\leq a,\qquad u_-\leq u,\qquad
 h_-\leq h,\qquad c_+\geq c.
\]

Since all quantities are positive, the panel certificate is

\[
 \mathcal C\geq
 p\left(a_-+\frac34\right)
 +(n-p)\left(\frac34+u_-\right)
 +\alpha_0(u_-+h_-)
 +\frac{h_-^2}{c_+}-(1+2p).                       \tag{6}
\]

Every transcendental evaluation and every sign in (6) uses Arb directed
rounding. A panel is accepted only if the lower endpoint of the resulting
Arb interval is strictly positive.

The new verifier imports the independently audited implementation

`scripts/general_d_first_floor_finite_verify.py`

and refuses to run unless its digest is exactly

`9F7C35279FD1E3FC47BF53C26A7D8681527703FE092BC3AA0831BD160609598D`.

Thus the implicit-wall isolation and correlated certificate code used here
is byte-for-byte the audited implementation.

## 4. Exact finite coverage

The finite enumeration is

\[
 r\in\left\{\frac12,1\right\},\qquad
 s\in\{0,1\},\qquad p\geq0,\qquad r+p<100.
\]

For \(r=1/2\), this is \(0\leq p\leq99\), giving 100 chambers for
each \(s\). For \(r=1\), it is \(0\leq p\leq98\), giving 99.
Therefore

\[
 199\ \text{chambers per }s,\qquad
 \boxed{398\ \text{chambers in all}.}
\]

At 384 and 512 bits, with 110 root bisections at each endpoint, the output
is identical:

```text
PASS s=0
  chambers=199, processed-panels=221, accepted-leaves=210,
  isolated-roots=409, max-depth=1

PASS s=1
  chambers=199, processed-panels=199, accepted-leaves=199,
  isolated-roots=398, max-depth=0

CERTIFIED
  chambers=398, processed-panels=420, accepted-leaves=409,
  isolated-roots=807, max-depth=1
```

Exactly eleven \(s=0\) chambers require the split
\([0,1/2]\cup[1/2,1]\):

\[
 \begin{aligned}
 &(r,p)=
 (\tfrac12,4),(\tfrac12,5),(\tfrac12,6),
 (\tfrac12,7),(\tfrac12,8),(\tfrac12,9),\\
 &(r,p)=(1,4),(1,5),(1,6),(1,7),(1,8).
 \end{aligned}
\]

Every other chamber is accepted on \([0,1]\). The smallest printed
midpoint is

\[
 0.0084055719981\ldots.
\]

This decimal is diagnostic only. The proof is the strict positive Arb
lower endpoint on every leaf. A 768-bit stress replay with 160 rational
root steps gives the same chamber, panel, leaf, and split counts.

## 5. The analytic ray \(x\geq100\)

Put

\[
 \beta=\mu-x=s+1+\alpha,\qquad
 \delta=K-\mu.
\]

Here \(1\leq\beta\leq3\). Changing variables \(R=x+v\) in the wall
equation gives

\[
 \frac{3\pi}{4}
 =\int_\beta^{\beta+\delta}
 \frac{\sqrt{v(2x+v)}}{x+v}\,dv.                  \tag{7}
\]

First,

\[
 \delta<x-\beta.                                  \tag{8}
\]

Otherwise the integration interval contains \([x/2,x]\). The integrand
is at least \(\sqrt5/3\) there, which would give

\[
 \frac{3\pi}{4}\geq\frac{x\sqrt5}{6},
\]

already false at \(x=100\).

Consequently \(v<x\) throughout (7), and

\[
 \frac{\sqrt{v(2x+v)}}{x+v}
 \geq\sqrt{\frac{v}{2x}}.
\]

Using
\((\beta+\delta)^{3/2}-\beta^{3/2}\geq\delta^{3/2}\)
gives

\[
 \delta\leq Cx^{1/3},\qquad
 C=\left(\frac{9\pi\sqrt2}{8}\right)^{2/3}
 <\frac{731}{250}.                                \tag{9}
\]

Let

\[
 T_*=\frac{53861}{250000}>100^{-1/3}.
\]

For \(t=x^{-1/3}\leq T_*\), (9) and \(\beta\leq3\) give

\[
 \begin{aligned}
 \frac Kx
 &<1+3t^3+\frac{731}{250}t^2\\
 &\leq1+3T_*^3+\frac{731}{250}T_*^2\\
 &=\frac{18214389817600143}{15625000000000000}
 <\frac65.                                        \tag{10}
 \end{aligned}
\]

Now

\[
 A(z)=\frac1\pi\int_\mu^K f_z(R)\,dR,
\qquad
 \left(\frac{f_r(R)}{f_x(R)}\right)^2
 =\frac{R^2-r^2}{R^2-x^2}.
\]

The ratio decreases with \(R\). Since \(r\leq1\), (10) implies

\[
 \begin{aligned}
 \left(\frac{f_r(R)}{f_x(R)}\right)^2
 &\geq\frac{K^2-r^2}{K^2-x^2}\\
 &>\frac{36x^2-25}{11x^2}\\
 &\geq\frac{14399}{4400}
 >\frac{25}{9}.                                   \tag{11}
 \end{aligned}
\]

Therefore \(f_r(R)>(5/3)f_x(R)\) throughout the radius integral, and

\[
 \boxed{A(r)>\frac53A(x)=\frac54.}                \tag{12}
\]

This closes the wall. With \(v=A(x+1)\), put
\(\sigma=-A'\). On the inner branch \(\sigma\) is increasing and
\(\sigma(\mu)=\arccos(\mu/K)/\pi\). Since \(x+1\leq\mu\), the
one-cell loss satisfies

\[
 \frac34-v<\frac{\arccos(\mu/K)}{\pi}<\frac12,
\]

so \(v>1/4\). The weakened wall certificate is

\[
 W=p\left(A(r)-\frac54\right)+v-\frac14+\mathcal E,
\qquad \mathcal E\geq0.
\]

Equations (12) and \(v>1/4\) give \(W>0\) for every \(p\geq0\).
Thus no interval computation is needed on \(x\geq100\).

The verifier replays all numerical comparisons above. It certifies

\[
 C=2.923332817290\ldots<2.924,
\]

\[
 1+3T_*^3+\frac{731}{250}T_*^2
 =1.165720948326\ldots<1.2,
\]

and

\[
 \frac{14399}{4400}=3.2725\ldots>\frac{25}{9}.
\]

## 6. Consequence and the earlier ten chambers

Sections 4 and 5 prove

\[
 \boxed{
 r\in\left\{\frac12,1\right\},\quad
 s=n-p-1\in\{0,1\},\quad p\geq0
 \Longrightarrow
 \text{the ordinary first-floor first-drop tail is positive}.}
\]

The ten earlier weakened-envelope failures all lie among the 398 finite
chambers. They are re-certified here directly by the stronger
true-interface certificate (3); their closure is not inferred from the old
diagnostic claim that the ten-chamber list was exhaustive.

Reproduction commands are

```text
python scripts/general_d_first_floor_small_starts_verify.py --precision 384
python scripts/general_d_first_floor_small_starts_verify.py --precision 512
python scripts/general_d_first_floor_small_starts_verify.py --precision 768 --root-steps 160
```

Combined with the audited finite and large-ray certificates for
\(r\geq3/2\), this closes the whole ordinary first-floor sector

\[
 s=n-p-1\in\{0,1\}.
\]

The cone \(s\geq2\) is separate. Its noncompact part is exhausted
qualitatively, but its compact residual set still needs an exact
certificate.
