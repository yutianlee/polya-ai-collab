# Round 6 review: combined thin-endpoint constants and overlap

## Verdict

| Candidate | Verdict | Scope of verdict |
|---|---|---|
| `phase-aggregate.md` | **PASS** | Its constants, rational inequalities, strict layer conventions, and range endpoints are correct, conditional only on the already-audited phase enclosure and separated spectral count that it explicitly imports. |
| `local-plateau-high-thin.md` | **PASS** | Its local-plateau constants, no-drop and immediate-drop cases, strict floor estimates, and endpoint $K=64\varepsilon^{-2}$ are correct, conditional only on the already-audited shifted-tail decomposition and spectral bridge that it explicitly imports. |
| Combined thin endpoint | **PASS** | For every $0<\varepsilon\le2^{-18}=1/262144$ and every $K\ge0$, the two proved ranges cover $K$ with no gap. Equivalently, the shell Pólya estimate holds uniformly for $1-2^{-18}\le\rho<1$ and all $K\ge0$. |

The conclusion is a genuine one-sided uniform $\rho\uparrow1$ endpoint
theorem.  It does **not** include the degenerate value $\rho=1$, and it does
not by itself settle compact $\rho$ ranges, the small-hole endpoint, or the
global shell theorem.  This review does not edit authoritative state.

## 1. Candidate A: aggregate low/intermediate range

The candidate proves, for

$$
0<\varepsilon\le\frac1{100},
$$

the aggregate range

$$
\frac{\pi}{4\varepsilon}
\le a=\varepsilon K
\le\frac1{8\varepsilon^{3/2}},
\tag{1}
$$

and combines it with the Round 5 range

$$
0\le a\le\frac{\pi}{4\varepsilon}.
\tag{2}
$$

Thus its complete consequence is

$$
\boxed{
0\le K\le L(\varepsilon)
:=\frac1{8\varepsilon^{5/2}}.
}
\tag{3}
$$

### 1.1 Strict lattice identities

The mesh count

$$
M_\varepsilon(x)
=\#\{\ell\ge0:\varepsilon(\ell+1/2)<x\}
=\max\left\{0,
\left\lceil\frac{x}{\varepsilon}-\frac12\right\rceil
\right\}
$$

is correct at and away from angular walls.  If
$x/\varepsilon=\ell+1/2$, the endpoint channel is excluded and the formula
returns exactly $\ell$.

For

$$
q_\ell=
\left[\mathcal A_{\varepsilon,a}(y_\ell)+\frac14\right]_<,
$$

strict layer cake gives

$$
\varepsilon\sum y_\ell q_\ell
=\frac{\varepsilon^2}{2}
\sum_{n-1/4<a/\pi}
M_\varepsilon(R(n-1/4))^2.
$$

The level relation is strict.  At
$\mathcal A(y_\ell)+1/4=n$, the $n$th layer is excluded, as required by
$[\cdot]_<$.  The true phase enclosure is also strict, so

$$
[\gamma]_<
\le[\mathcal A+1/4]_<
$$

even when the majorant is an integer.  No ordinary-floor substitution is
made at this step.

### 1.2 Shifted radial deficit

With

$$
t=\frac a\pi,
\qquad
N=\left\lceil t+\frac14\right\rceil-1,
\qquad
u=t-N\in\left(-\frac14,\frac34\right],
$$

the endpoint $u=3/4$ is exactly the strict radial wall
$t+1/4\in\mathbb Z$.  Direct expansion confirms

$$
\frac D{\pi^2}
=\frac{N^2}{4}
+N\left(u^2-\frac1{48}\right)
+\frac{2u^3}{3}.
\tag{4}
$$

Since $u>-1/4$ (the report harmlessly uses the weaker $u\ge-1/4$),

$$
\frac D{\pi^2}
\ge\frac{N^2}{4}-\frac N{48}-\frac1{96}
\ge\frac{N^2}{5}.
$$

The final comparison is equivalent to

$$
24N^2-10N-5\ge0,
$$

which is already strict at $N=1$ and increases thereafter.

The quarter-disk estimate

$$
\sum_{n=1}^N b_n\le\frac{a^2}{4}+\frac a4
$$

also has the correct endpoints.  For $n=1$, evenness ensures that every
value on $[-1/4,3/4]$ is at least $b(3/4)$; for $n\ge2$, monotonicity on the
successive unit intervals gives the claimed integral majorization.

### 1.3 Constants in Lemma 1

The hypotheses imply

$$
t\ge25,
\qquad
m_\varepsilon\ge\frac{99}{100},
\qquad
N\ge t-\frac34\ge\frac{24}{25}t.
$$

Consequently

$$
m_\varepsilon D
\ge
\frac{99}{100}\cdot\frac15
\left(\frac{24}{25}\right)^2a^2
=\frac{57024}{312500}a^2
>\frac9{50}a^2,
$$

because $57024-56250=774>0$ after using denominator $312500$.

At the lower endpoint,

$$
a\ge\frac\pi{4\varepsilon}>75,
$$

using $\varepsilon\le1/100$ and $\pi>3$.  Hence

$$
\varepsilon\sqrt{m_\varepsilon}\sum b_n
<\frac{19}{7500}a^2
<\frac1{300}a^2.
$$

Also $N<t+1/4<2t$ gives

$$
\frac{\varepsilon^2N}{4}
<\frac{a^2}{10000}.
$$

The final margin is valid with room to spare:

$$
\frac9{50}-\frac1{300}-\frac1{10000}
=\frac{5297}{30000}
>\frac{5000}{30000}
=\frac16.
$$

The outside factor $1/2$ therefore yields the strict margin
$I-P_{\mathcal B}>a^2/12$.

### 1.4 Outer-strip payment

There are at most $a+1$ mesh points in
$(\rho a,a)$, the endpoints are not inadvertently included, and

$$
E_{\rm out}
=\varepsilon a(a+1)
\left(\frac{a\sqrt{2\varepsilon}}\pi+1\right)
$$

obeys

$$
\frac{E_{\rm out}}{a^2}
<\frac{76}{75}
\left(\frac1{16}+\frac1{100}\right)
=\frac{2204}{30000}
<\frac{2500}{30000}
=\frac1{12}.
$$

The inequalities remain strict when
$a=1/(8\varepsilon^{3/2})$: the estimates
$a>75$ and $\sqrt2/\pi<1/2$ are strict.  Thus the upper endpoint in (1) is
included.

The interval (1) is nonempty because

$$
\frac{\pi}{4\varepsilon}
\le\frac1{8\varepsilon^{3/2}}
\iff 2\pi\sqrt\varepsilon\le1,
$$

and $2\pi\sqrt\varepsilon\le\pi/5<1$ for
$\varepsilon\le1/100$.  Its lower endpoint is included by both this proof
and Round 5, so (3) has no internal gap.

### Candidate A verdict

**PASS.**  All constants and strict endpoints close.  The proof legitimately
establishes (3), subject to its stated already-audited phase and spectral
dependencies.

## 2. Candidate B: local-plateau high-thin range

The candidate claims

$$
\boxed{
K\ge H(\varepsilon):=\frac{64}{\varepsilon^2}
}
\tag{5}
$$

for $0<\varepsilon\le1/100$.

### 2.1 Plateau bookkeeping and exceptional cases

Let $p$ be the last point in the initial constant-floor plateau, let
$m=n-p$, and set

$$
R=p-dm,
\qquad
d=1-\frac{2\arccos\rho}{\pi}.
$$

The imported audited decomposition gives

$$
M=\lfloor K\eta\rfloor-R.
\tag{6}
$$

For $R\le0$, there is no plateau loss and the later bound
$R<10/\sqrt\varepsilon$ is automatic.  For $R>0$, necessarily $p>0$.
Since

$$
\rho\ge\frac{99}{100}>\frac{\sqrt3}{2},
$$

one has $d>2/3$ and therefore

$$
m<\frac p d<\frac32p,
\qquad
u=\mu-x_0=p+m+\xi<\frac52p+1.
\tag{7}
$$

This includes the no-drop case $p=n$, for which $m=0$ and $R=p>0$.
The immediate-drop case $p=0$ necessarily has $R=-dm\le0$ and belongs to
the easy case.  If $n=0$, the stipulated $p=m=0$ also gives $R=0$ and the
purely convex tail is covered.

### 2.2 Outer-half localization

If $x_0<K/2$, then

$$
u>\left(\frac12-\varepsilon\right)K
\ge\frac{49}{100}K.
$$

Since $K>100$, (7) gives

$$
p>\frac25\left(\frac{49}{100}K-1\right)
>\frac{24}{125}K.
$$

Combining this with the audited global plateau estimate

$$
p^2<\frac{8K}{\varepsilon}
$$

would force

$$
K<\frac{125000}{576\varepsilon}
<\frac{218}{\varepsilon}.
$$

But (5) and $\varepsilon\le1/100$ imply

$$
K\ge\frac{6400}{\varepsilon},
$$

a contradiction.  Therefore $x_0\ge K/2$, including equality.

### 2.3 Local slope and quadratic bound

The exact derivative identity gives

$$
\sigma(z)
\ge\frac{\varepsilon z}{\pi\sqrt{K^2-z^2}}.
$$

Constancy of the floor through $p$ gives the strict inequality

$$
1>A(x_0)-A(x_0+p)
\ge p\sigma(x_0).
$$

Using $x_0\ge K/2$, $K-x_0=\varepsilon K+u$, (7), and
$K\ge64\varepsilon^{-2}$ yields

$$
p^2
<\frac{8\pi^2}{\varepsilon}
+\frac{5\pi^2}{16}p
+\frac{\pi^2}{8}.
\tag{8}
$$

Let $P=10/\sqrt\varepsilon$.  The associated quadratic is increasing for
$p\ge P$.  Using $\pi^2<10$ and
$1/\sqrt\varepsilon\ge10$, its value at $P$ is strictly larger than

$$
\frac{20}{\varepsilon}
-\frac{125}{4\sqrt\varepsilon}
-\frac54.
$$

Writing $x=1/\sqrt\varepsilon\ge10$, the last expression is

$$
20x^2-\frac{125}{4}x-\frac54,
$$

which is increasing on $[10,\infty)$ and equals $6745/4>0$ at $x=10$.
Thus (8) forces

$$
p<\frac{10}{\sqrt\varepsilon},
\qquad
R<\frac{10}{\sqrt\varepsilon}.
\tag{9}
$$

All inequalities remain strict at the threshold in (5).

### 2.4 Convex gain

The elementary bound

$$
\eta=G_1(1-\varepsilon)
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}
$$

has the correct direction: with
$x=\arccos(1-v)$, the inequality
$\cos x\ge1-x^2/2$ implies $x\ge\sqrt{2v}$.

Equations (5), (6), and (9) give

$$
M>
\left(\frac{128\sqrt2}{3\pi}-10\right)
\frac1{\sqrt\varepsilon}-1
>\frac{2}{3\sqrt\varepsilon}-1
\ge\frac{17}{3}.
$$

The middle strict inequality follows from $\sqrt2>1$ and $\pi<4$.
Meanwhile

$$
4\delta<\frac{8\sqrt2}{15}
<\frac{16}{15}<\frac{17}{3}.
$$

Hence $M>4\delta$ at $K=64\varepsilon^{-2}$ as well as above it.  Every
low-interface tail closes strictly; the audited convex theorem covers tails
starting at or above the interface.  The ordinary-floor coarse proxy bounds
the strict transferred phase proxy at every integer wall.

### Candidate B verdict

**PASS.**  The constant $64$, the exponent $\varepsilon^{-2}$, the no-drop
case, and all threshold endpoints are valid under the candidate's stated
audited dependencies.

## 3. Exact overlap

The low and high thresholds are

$$
L(\varepsilon)=\frac1{8\varepsilon^{5/2}},
\qquad
H(\varepsilon)=\frac{64}{\varepsilon^2}.
$$

They cover every $K\ge0$ exactly when $H\le L$.  Algebraically,

$$
\frac{64}{\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\iff
512\sqrt\varepsilon\le1
\iff
\boxed{\varepsilon\le\frac1{262144}=2^{-18}.}
\tag{10}
$$

At the endpoint $\varepsilon=2^{-18}$,

$$
L(2^{-18})=H(2^{-18})=2^{42},
$$

and in optical variables

$$
a=\varepsilon K=2^{24}.
$$

Both candidate ranges include equality, so this single joining point is not
lost.  When $0<\varepsilon<2^{-18}$, the interval
$[H(\varepsilon),L(\varepsilon)]$ is a genuine overlap.

Thus, for

$$
0<\varepsilon\le2^{-18},
$$

Candidate A covers $0\le K\le L(\varepsilon)$ and Candidate B covers
$H(\varepsilon)\le K<\infty$.  Their union is all $K\ge0$.

## 4. Exact $\rho$ and endpoint conventions

Since $\varepsilon=1-\rho$, the uniform thin neighborhood is

$$
\boxed{
1-2^{-18}\le\rho<1.
}
\tag{11}
$$

The conventions are:

1. **Lower $\rho$ endpoint included.**  At
   $\rho=1-2^{-18}=262143/262144$, the thresholds meet at $K=2^{42}$,
   and equality belongs to both ranges.
2. **Upper $\rho$ endpoint excluded.**  The shell problem assumes
   $0<\rho<1$; $\rho=1$ is a degenerate zero-width limit and is not asserted.
3. **Zero frequency included.**  At $K=0$, both the strict spectral count
   and the Weyl term are zero; Round 5 supplies this endpoint.
4. **Spectral walls remain strict.**  The eigenvalue count uses the strict
   phase count.  Candidate A preserves strict action and angular walls;
   Candidate B proves an ordinary-floor coarse bound that dominates the
   strict phase proxy, including at integer walls.
5. **Joining thresholds included.**  Candidate A includes
   $K=L(\varepsilon)$ and Candidate B includes
   $K=H(\varepsilon)$.  No open endpoint is hidden in (10).

## Combined conclusion

**PASS.**  Subject to the dependencies already marked as audited in the two
candidate reports, the combination proves

$$
\boxed{
1-2^{-18}\le\rho<1,
\quad K\ge0
\quad\Longrightarrow\quad
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

This is a uniform $\rho\uparrow1$ endpoint theorem: one fixed neighborhood
of $1$ is covered for every frequency, without an unbounded residual strip
or numerical certification.  It is eligible for the normal clean-room and
adversarial promotion process, but this constants audit alone does not alter
the proof state.
