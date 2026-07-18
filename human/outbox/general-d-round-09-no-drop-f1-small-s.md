# General dimension, Round 9: the first-floor no-drop small-\(s\) theorem

Date: 18 July 2026

Status: rigorous analytic closure of the small-\(s\) sector and rigorous
global finite reduction for the ordinary first-floor no-drop branch.  This
note does **not** certify the residual compact wall chambers and therefore
does not prove the global \(f=1\), \(p=n\) theorem by itself.

## 1. Statement and endpoint phases

Use the shell action

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi},
 \qquad A=G_K-G_\mu,
\]

with zero extension, and suppose that the ordinary floors do not drop
before the interface:

\[
 n=\lfloor\mu-r\rfloor\geq1,
 \qquad q=r+n,
 \qquad
 \left\lfloor A(r+j)+\frac14\right\rfloor=1
 \quad(0\leq j\leq n).
 \tag{1}
\]

Thus \(p=n\) and \(f=1\).  Put

\[
 R_n=2\int_r^qA(z)\,dz-2n,
 \qquad
 \mathcal S_n=D_A(q)+R_n.
 \tag{2}
\]

We work in the universal active region

\[
 \delta:=K-\mu>\pi.
 \tag{3}
\]

Write

\[
 \alpha=\mu-q\in[0,1),
 \qquad
 s=\sqrt{\frac\delta K},
 \qquad
 \kappa=s\delta=s^3K.
 \tag{4}
\]

The exact no-drop identity gives

\[
 R_n=-\frac n2+2n\varepsilon_q
 +2\int_0^n u\,\sigma(r+u)\,du,
 \qquad
 \varepsilon_q=A(q)-\frac34.
 \tag{5}
\]

The one-interface theorem gives \(D_A(q)\geq0\).  Hence the branch is
already closed when \(\varepsilon_q\geq1/4\).  The only residual sector is

\[
 \frac34\leq A(q)<1.
 \tag{6}
\]

Let

\[
 Q=\left[A(q)+\frac14\right]_<,
 \qquad
 B=\left[G_K(q)+\frac14\right]_<.
\]

The strict endpoint convention gives exactly three phases:

1. **open:** \(A(q)>3/4\), so \(Q=1\) and \(B\geq1\);
2. **lower noncorner:** \(A(q)=3/4\) and \(q<\mu\), so \(Q=0\), while
   \(G_\mu(q)>0\) gives \(B\geq1\);
3. **corner:** \(A(q)=3/4\) and \(q=\mu\), so \(Q=B=0\).

No equality face is obtained by continuity from another phase.

### Theorem 1.1 (small-\(s\) first-floor no-drop closure)

Every configuration satisfying (1)--(6) and

\[
 0<s\leq\frac1{10}
 \tag{7}
\]

obeys \(\mathcal S_n>0\).  More precisely,

\[
 s\mathcal S_n>
 \frac{222407}{1435700}
 \tag{8}
\]

in the open and lower-noncorner phases, while at the corner

\[
 s\mathcal S_n>
 \frac{1323513}{2297120}.
 \tag{9}
\]

The proof occupies Sections 2--5.

## 2. A multiplicative finite-thickness profile bound

Use the exact head coordinate

\[
 X=s(\mu-z),
 \qquad
 \mathcal H_{s,\kappa}(X)=A(\mu-X/s),
\]

and the critical profile

\[
 H_\kappa(X)=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right),
 \qquad
 c_0=\frac{2\sqrt2}{3\pi},
 \qquad
 w=H_\kappa(0)=c_0\kappa.
 \tag{10}
\]

The shell has the noncancelling exact representation

\[
 \mathcal H_{s,\kappa}(X)
 =\frac1\pi\int_0^\kappa
 \frac{\sqrt{(\kappa+X-u)
 [2\kappa-(\kappa+X+u)s^2]}}
 {\kappa-us^2}\,du.
 \tag{11}
\]

Relative to the integrand defining \(H_\kappa\), its ratio is

\[
 \mathcal R(u,X)
 =\frac{\sqrt{1-a(u,X)s^2}}{1-b(u)s^2},
 \qquad
 a(u,X)=\frac{\kappa+X+u}{2\kappa},
 \qquad b(u)=\frac u\kappa.
 \tag{12}
\]

The radius representation

\[
 A(q)=\frac1\pi\int_\mu^K
 \sqrt{1-\frac{q^2}{a^2}}\,da
\]

and \(K-q=\delta+\alpha<2\delta\), which follows from
\(\delta>\pi>1>\alpha\), give

\[
 A(q)\leq\frac{2\kappa}{\pi}.
\]

Together with (6), this implies

\[
 \kappa\geq\frac{3\pi}{8}>\frac98.
 \tag{13}
\]

For \(0\leq X\leq3\), (13), \(0\leq u\leq\kappa\), and (7) give

\[
 a(u,X)\leq1+\frac{3}{2\kappa}\leq\frac73.
\]

Since \(\sqrt{1-y}\geq1-y\) and \(1-b s^2\leq1\), (12) gives the
pointwise lower comparison

\[
 \boxed{
 \mathcal H_{s,\kappa}(X)\geq\frac{293}{300}H_\kappa(X)
 \qquad(0\leq X\leq3\text{ at every physical point}).}
 \tag{14}
\]

At the endpoint \(X_q=s\alpha\leq1/10\), the opposite estimate
\(\mathcal R\leq(1-s^2)^{-1}\leq100/99\) is enough.  Moreover

\[
 H_\kappa'(X)=\frac{3c_0}{2\sqrt\kappa}
 (\sqrt{\kappa+X}-\sqrt X)<\frac12.
\]

Consequently

\[
 \frac34\leq A(q)
 \leq\frac{100}{99}H_\kappa(X_q)
 \leq\frac{100}{99}\left(w+\frac1{20}\right),
\]

and hence

\[
 \boxed{w\geq\frac{277}{400}.}
 \tag{15}
\]

## 3. Uniform payment of the complete negative head

Put

\[
 c=\frac{293}{300},\qquad y=cw.
\]

If \(y\geq1\), then (14), monotonicity of the exact shell action, and
\(H_\kappa(X)\geq w\) show that the complete head is nonnegative.

Suppose \(y<1\), and let \(X_*\) be the unique point at which

\[
 cH_\kappa(X_*)=1.
\]

Use the exact coordinates

\[
 X=\kappa u(t),
 \qquad
 u(t)=\frac{(1-t^2)^2}{4t^2},
 \qquad
 \frac{H_\kappa(X)}w=\frac{3/t+t^3}{4}.
 \tag{16}
\]

If \(b\) is the \(t\)-coordinate of \(X_*\), then

\[
 y=\frac{4b}{3+b^4},
 \qquad b\geq\frac{3y}{4}.
\]

Equations (15) and \(c=293/300\) give

\[
 y\geq\frac{81161}{120000}>\frac{27}{40},
 \qquad b>\frac{81}{160}.
 \tag{17}
\]

Since \(u\) is decreasing,

\[
 u(b)<u(81/160)
 =\frac{362483521}{671846400}<\frac{27}{50}.
 \tag{18}
\]

The assumption \(y<1\) gives \(w<300/293\).  The elementary bounds
\(\sqrt2>7/5\) and \(\pi<22/7\) give

\[
 c_0>\frac{49}{165},
 \qquad
 \kappa=\frac w{c_0}<\frac{49500}{14357}.
\]

Thus

\[
 X_*<\frac{26730}{14357}<3.
 \tag{19}
\]

This proves, without circularity, that (14) holds on the whole possible
negative head.  The function \(1-cH_\kappa\) is convex on \([0,X_*]\),
with endpoint heights at most \(13/40\) and zero.  It lies below its
endpoint chord.  Since

\[
 sR_n=2\int_{X_q}^{X_q+sn}
 (\mathcal H_{s,\kappa}(X)-1)\,dX,
\]

discarding positive pieces and enlarging the negative interval to
\([0,X_*]\) gives

\[
 \boxed{
 sR_n>-\frac{26730}{14357}\frac{13}{40}
 =-\frac{34749}{57428}.}
 \tag{20}
\]

## 4. The two phases with a complete terminal level

In the open and lower-noncorner phases one has \(B\geq1\).  Let
\(\theta_1\in(0,\pi/2)\) be the outer-ball angle at the level \(3/4\):

\[
 \frac K\pi(\sin\theta_1-\theta_1\cos\theta_1)=\frac34.
\]

The exact-angle terminal reserve, with all further favorable levels and
the fractional-top term omitted, is

\[
 D_A(q)\geq
 \frac\pi{2\theta_1}-Q-2\int_q^\mu G_\mu(z)\,dz.
 \tag{21}
\]

For \(0\leq\theta\leq\pi/2\),

\[
 \sin\theta-\theta\cos\theta
 =\int_0^\theta t\sin t\,dt
 \geq\frac{2\theta^3}{3\pi}.
\]

Therefore

\[
 s\frac\pi{2\theta_1}
 \geq\frac\pi2
 \left(\frac{8\kappa}{9\pi^2}\right)^{1/3}
 =\frac\pi2
 \left(\frac{4w}{3\sqrt2\,\pi}\right)^{1/3}
 >\frac9{10}.
 \tag{22}
\]

The last strict comparison is completely rational after cubing.  Indeed,

\[
 \pi^2w>9\frac{277}{400}=\frac{2493}{400},
\]

whereas \(\sqrt2<99/70\) gives

\[
 \frac{2187}{500}\sqrt2
 <\frac{216513}{35000},
 \qquad
 \frac{2493}{400}-\frac{216513}{35000}
 =\frac{3249}{70000}>0.
\]

The one-interface cap satisfies

\[
 2\int_q^\mu G_\mu(z)\,dz<\frac{4\sqrt2}{15}.
\]

Since \(Q\leq1\), \(s\leq1/10\), and \(\sqrt2<3/2\), (21)--(22) give

\[
 \boxed{sD_A(q)>\frac9{10}-\frac1{10}
 -\frac{2\sqrt2}{75}>\frac{19}{25}.}
 \tag{23}
\]

Adding (20) and (23) proves

\[
 s\mathcal S_n>\frac{19}{25}-\frac{34749}{57428}
 =\frac{222407}{1435700}>0,
\]

which is (8).  Notice that (21) uses \(Q=1\) in the open phase and
\(Q=0\) on the lower noncorner wall; the proof has not moved either value
through the strict wall.

## 5. The pure-ball interface corner

At the corner, \(q=\mu\), \(A(q)=G_K(q)=3/4\), and \(Q=B=0\).  Since
\(G_K\) is strictly decreasing, the complete strict terminal count is
zero.  The zero-level triangle therefore gives

\[
 D_A(q)\geq\frac{(3/4)^2}{\beta/\pi}
 =\frac{9\pi}{16\beta},
 \qquad
 \beta=\arccos\rho=\arccos(1-s^2).
 \tag{24}
\]

The half-angle identity gives

\[
 \beta=2\arcsin\frac{s}{\sqrt2}.
\]

Using \(\arcsin x\leq x/\sqrt{1-x^2}\) and \(s\leq1/10\),

\[
 \frac\beta s
 \leq\frac{\sqrt2}{\sqrt{1-s^2/2}}
 \leq\sqrt{\frac{400}{199}}<\frac{10}{7}.
\]

Thus, by \(\pi>3\),

\[
 \boxed{sD_A(q)>\frac{63\pi}{160}>\frac{189}{160}.}
 \tag{25}
\]

Combining (20) and (25) gives

\[
 s\mathcal S_n>\frac{189}{160}-\frac{34749}{57428}
 =\frac{1323513}{2297120}>0,
\]

which proves (9) and Theorem 1.1.

## 6. Explicit global finite reduction

We now combine Theorem 1.1 with the already-proved residual geometry.  Put
\(b=3/4\).  If \(\mathcal S_n<0\), the exact no-drop and shelf-curvature
identities imply

\[
 A(q)<1,
 \qquad A(r)<\frac54,
\]

and the root-free geometric estimates give

\[
 b\,n(n+1)<K^2,
 \qquad
 K\leq U(\delta):=
 \frac{2\delta^2(\delta+1)}{\pi^2b^2},
 \qquad
 \frac\delta\pi<\frac54+\frac r{4n}.
 \tag{26}
\]

### 6.1. Central starts

If \(r\leq K/2\), then \(r<\delta+n+1\), and (26) gives

\[
 \delta<D_n:=
 \frac{3/2+1/(4n)}{1/\pi-1/(4n)}.
\]

Consequently every negative central candidate must satisfy

\[
 \frac34n(n+1)<U(D_n)^2.
 \tag{27}
\]

The bounds \(\pi<22/7\) and \(\pi>3\) give

\[
 D_n<\overline D_n:=
 \frac{3/2+1/(4n)}{7/22-1/(4n)},
 \qquad
 U(D_n)<\overline U_n:=
 \frac{32}{81}\overline D_n^2(\overline D_n+1).
\]

At \(n=61\),

\[
 \overline D_{61}=\frac{4037}{843},
 \qquad
 \overline U_{61}=\frac{2544997143040}{48525245667},
\]

and exact integer arithmetic gives

\[
 \overline U_{61}^{2}<\frac{5673}{2}
 =\frac34\,61\cdot62.
\]

The left side decreases with \(n\), while the right side increases.
Therefore (27) is impossible for \(n\geq61\):

\[
 \boxed{n\leq60\qquad(r\leq K/2).}
 \tag{28}
\]

### 6.2. Outer starts and the compact box

If \(r>K/2\), the established outer residual geometry gives

\[
 \delta+1>c_1n,
 \qquad
 c_1=\frac{\sqrt{1+b^2}-1}{2}=\frac18.
 \tag{29}
\]

For \(n\geq16\), (29) implies \(\delta>n/16\).  The endpoint-action
lower bound

\[
 A(q)\geq\frac{2\kappa}{3\pi}
\]

and \(A(q)<1\) give \(\kappa<3\pi/2\).  Hence

\[
 s=\frac\kappa\delta<\frac{24\pi}{n}
 <\frac{528}{7n}.
\]

For \(n\geq755\), the last quantity is smaller than \(1/10\), and
Theorem 1.1 excludes the candidate.  Thus

\[
 \boxed{n\leq754\qquad(r>K/2).}
 \tag{30}
\]

Finally, every candidate not closed by Theorem 1.1 has \(s>1/10\).
Together with \(\kappa<3\pi/2\), this yields

\[
 \boxed{
 K=\frac\kappa{s^3}<1500\pi<\frac{33000}{7}.}
 \tag{31}
\]

Equations (28)--(31) reduce every possible negative \(f=1\), \(p=n\)
configuration to the explicit compact box

\[
 \boxed{
 1\leq n\leq754,
 \qquad
 0<s<1,
 \qquad
 s>\frac1{10},
 \qquad
 K<\frac{33000}{7},}
 \tag{32}
\]

with the open, lower-noncorner, and corner endpoint phases kept separate.
Since \(r\in\tfrac12\mathbb N\) and \(r<K\), (32) leaves only finitely
many shifts, sample indices, and one-sided action walls.

## 7. Replay and exact scope

All rational comparisons and all appearances of \(\pi\) and \(\sqrt2\)
in the displayed constants are replayed with outward-rounded Arb arithmetic
by

```text
scripts/general_d_no_drop_f1_small_s_verify.py
```

The frozen replay source has SHA-256
`AF8920ED071BE596E815B749B52904F6BA550FD30104C30D9FF6AC1CCEBB76AD`.

The analytic inputs not replaced by computation are the exact no-drop
identity, the noncancelling shell representation (11), the exact-angle
terminal reserve, the zero-level triangle, and the residual geometric
inequalities (26) and (29).

The theorem closes every \(f=1\) no-drop branch with \(s\leq1/10\) and
proves the compact reduction (32).  It does **not** certify the remaining
finite continuous chambers with \(s>1/10\), and no global \(f=1\)
no-drop theorem is claimed here.
