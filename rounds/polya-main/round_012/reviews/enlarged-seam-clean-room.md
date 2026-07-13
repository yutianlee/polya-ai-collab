# Round 12 enlarged-seam clean-room review

## Isolation boundary

I performed this reconstruction without inspecting any file under
`rounds/polya-main/round_012/` (apart from writing and verifying this review
itself), any
`computations/round12*` file, any Round 10 incumbent, clean-room, or
adversarial response, or any other agent output.  I used only
`state/lemma_packets/SHELL-central-thin-seam-compression-round12.md` and the
prior inputs it explicitly permits: the strict separated spectral count,
phase enclosure, weighted-tail scaffold and high-angular tails, the audited
Round 3 low-interface decomposition, the fixed-rho high-energy theorem, the
small-hole endpoint, and the accepted Round 10 and Round 11 theorem
statements needed only for the final union.  I inspected the corresponding
state lemma packets, not any response or review.

## Verdict

**PASS.**  The frozen local claim holds with threshold equality:

\[
0<\varepsilon\le \frac1{20},\qquad
K\ge \frac{24}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le \frac{2}{9\pi}
   \bigl(1-(1-\varepsilon)^3\bigr)K^3.
\]

An exact sufficient plateau constant is

\[
\boxed{B=5},\qquad R<\frac5{\sqrt\varepsilon}.
\]

The endpoint comparison also passes:

\[
\boxed{K_0(19/20)<3300^2}.
\]

There is therefore no failed inequality and no replacement claim is needed.

## 1. Spectral and weighted reduction

Put

\[
y=\sqrt\varepsilon,\qquad \rho=1-y^2,\qquad
\kappa=K y^4.
\]

The frozen domain is

\[
0<y\le\frac1{\sqrt{20}},\qquad \rho\ge\frac{19}{20},
\qquad \kappa\ge24.                                      \tag{1.1}
\]

Let \(\nu_\ell=\ell+1/2\), \(\mu=\rho K\), and
\(A=G_K-G_\mu\), with both \(G\)'s extended by zero past their
supports.  The strict separated spectral count and the phase enclosure give

\[
N_D(A_{\rho,1},K^2)
=\sum_{\nu_\ell<K}2\nu_\ell[\gamma(\nu_\ell)]_<,
\qquad
\gamma(\nu)<A(\nu)+\frac14.                              \tag{1.2}
\]

Consequently

\[
[\gamma(\nu)]_<\le
\left\lfloor A(\nu)+\frac14\right\rfloor.                \tag{1.3}
\]

This remains true at every wall.  If the right side's argument is an
integer \(j\), strictness in (1.2) even gives a count at most \(j-1\),
whereas the coarse upper proxy is \(j\).  If the true phase itself is an
integer, the strict count is again one less than that integer.  Thus no
ordinary floor is being substituted for the true strict count.

Define

\[
q_\ell=\left\lfloor A(\ell+\tfrac12)+\frac14\right\rfloor
\]

and, for \(x_r=r+1/2\),

\[
\mathcal T_r=q_r+2\sum_{\ell>r}q_\ell.
\]

All sums are finite because \(A=0\) past \(K\) and
\(\lfloor1/4\rfloor=0\).  The exact dimension reduction is

\[
\sum_{\ell\ge0}(2\ell+1)q_\ell=\sum_{r\ge0}\mathcal T_r. \tag{1.4}
\]

The permitted high-angular theorem proves

\[
x_r\ge\mu\quad\Longrightarrow\quad
\mathcal T_r\le2\int_{x_r}^{K}A(z)\,dz,                  \tag{1.5}
\]

including the interface equality \(x_r=\mu\).  It remains only to prove
(1.5) for \(x_r<\mu\).

For completeness, once (1.5) holds for every \(r\), set

\[
f_3(z)=\#\{r\ge0:r+1/2\le z\},\qquad
F_3(z)=\int_0^z f_3(t)\,dt.
\]

If \(z\in[m+1/2,m+3/2]\), then

\[
F_3(z)=(m+1)z-\frac{(m+1)^2}{2},
\quad
\frac{z^2}{2}-F_3(z)=\frac{(z-m-1)^2}{2}\ge0.             \tag{1.6}
\]

The formula agrees at the half-integer walls; below \(1/2\), \(F_3=0\).
Since \(A\) is decreasing, absolutely continuous, and \(A(K)=0\), (1.4),
(1.5), and integration by parts give

\[
\begin{aligned}
\sum_{\ell\ge0}(2\ell+1)q_\ell
&\le2\int_0^K f_3(z)A(z)\,dz\\
&=2\int_0^K F_3(z)(-dA(z))\\
&\le\int_0^K z^2(-dA(z))
=\int_0^K2zA(z)\,dz\\
&=\frac{2}{9\pi}(K^3-\mu^3).
                                                               \tag{1.7}
\end{aligned}
\]

Together with (1.2)--(1.3), this is exactly the desired spectral bound.

## 2. Exact elementary bounds for \(d\) and the action

Let

\[
c=\frac{\arccos\rho}{\pi},\qquad d=1-2c.
\]

The identity

\[
\cos^2\frac\pi8=\frac{2+\sqrt2}{4}
\]

and \(\sqrt2<161/100\) imply

\[
\cos^2\frac\pi8<\frac{361}{400},
\qquad \cos\frac\pi8<\frac{19}{20}.
\]

As \(\rho\ge19/20\) and arccosine is decreasing,

\[
0<\arccos\rho\le\arccos\frac{19}{20}<\frac\pi8,
\qquad
\boxed{d>\frac34}.                                        \tag{2.1}
\]

For the action, if \(t=\arccos(1-v)\), then

\[
v=1-\cos t=2\sin^2(t/2)\le\frac{t^2}{2},
\]

so \(\arccos(1-v)\ge\sqrt{2v}\).  Therefore

\[
\eta=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}
=\frac{2\sqrt2}{3\pi}y^3,                                \tag{2.2}
\]

and hence, throughout (1.1),

\[
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}
\ge\frac{16\sqrt2}{\pi y}.                               \tag{2.3}
\]

All endpoint directions in (2.1)--(2.3) are valid at
\(y=1/\sqrt{20}\) and \(\kappa=24\).

## 3. Low-interface decomposition and dangerous localization

Fix a low-interface start \(x_0=r_0+1/2<\mu\) and use the packet's
notation

\[
n=\lfloor\mu-x_0\rfloor,\quad
q=x_0+n,\quad
\beta=\mu-q\in[0,1),\quad U=n+\beta.
\]

Let \(p\) be the initial ordinary-floor plateau length,
\(m=n-p\), and

\[
R=p-dm.
\]

The audited decomposition is

\[
\frac{\mathcal T_{r_0}}2
\le\int_{x_0}^{K}A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,                                \tag{3.1}
\]

where

\[
0\le\delta<\frac{2\sqrt2}{15}.                           \tag{3.2}
\]

At \(q=\mu\), \(\delta=0\); as \(\beta\to1^-\), (3.2) remains the
strict audited bound.  The convention for \(n=0\) is \(p=m=0\).

Only \(R>0\) needs a new estimate.  In this branch \(p>dm\), so \(p>0\)
and, by (2.1),

\[
m<\frac p d<\frac{4p}{3},qquad
n=p+m<\frac{7p}{3}.                                       \tag{3.3}
\]

Using \(U<n+1\) and the unconditional shelf estimate gives

\[
\begin{aligned}
\frac UK
&<\frac73\sqrt{\frac{2\pi\rho}{\varepsilon K}}+\frac1K\\
&=\frac73 y\sqrt{\frac{2\pi\rho}{\kappa}}+\frac{y^4}{\kappa}\\
&<\frac7{3\sqrt{20}}\sqrt{\frac\pi{12}}+\frac1{9600}\\
&<\frac7{3\sqrt{60}}+\frac1{9600}
<\frac13+\frac1{9600}<\frac9{20}.                         \tag{3.4}
\end{aligned}
\]

Here only \(\rho<1\), \(\pi<4\), \(y\le1/\sqrt{20}\), and
\(\kappa\ge24\) were used; \(\sqrt{60}>7\).  Since
\(\rho-1/2\ge9/20\),

\[
\boxed{\frac{x_0}{K}=\rho-\frac UK>\frac12}.              \tag{3.5}
\]

Thus every dangerous plateau lies strictly above the outer half-radius.
Also \(K\ge24\cdot20^2=9600\), so (3.5) gives \(x_0>1\).  This will
justify every positive denominator below.

## 4. The local slope and self-consistency inequality

Scale

\[
P=py,\qquad r=Ry,\qquad S=(p+m)y=ny.                     \tag{4.1}
\]

In the branch \(R>0\),

\[
0<r\le P,qquad
r=P-d(S-P),qquad
S=P+\frac{P-r}{d}.                                        \tag{4.2}
\]

Define

\[
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q=\frac{y^2}{\rho}(Q-1).                         \tag{4.3}
\]

Since \(S=ny\) and \(\kappa=K\varepsilon^2\), these are exactly

\[
Q=1+\frac{n+1}{K\varepsilon},qquad
\widehat q=\frac{n+1}{\mu}.                              \tag{4.4}
\]

By (3.5), \(x_0>1\), whence

\[
\mu-n-1=x_0+\beta-1>0.
\]

Thus \(0<\widehat q<1\) and

\[
1-\varepsilon Q
=\rho-\frac{n+1}{K}
=\frac{\mu-n-1}{K}>0.                                    \tag{4.5}
\]

Let

\[
\sigma(z)=-A'(z)
=\frac1\pi\left(\arccos\frac zK-\arccos\frac z\mu\right),
\qquad 0<z<\mu.
\]

Because \(p\le n\), the plateau segment satisfies
\(x_0+p\le x_0+n=q\le\mu\), so this slope controls its entire length
(with the endpoint value understood by continuity if \(q=\mu\)).
It is increasing because

\[
\sigma'(z)=\frac1{\pi\sqrt{\mu^2-z^2}}
-\frac1{\pi\sqrt{K^2-z^2}}>0.                            \tag{4.6}
\]

The ordinary floors at the two ends of the initial plateau are equal.
If their common value is \(j\), both arguments lie in \([j,j+1)\), even
when one argument is exactly an integer.  Hence

\[
0\le A(x_0)-A(x_0+p)<1.                                  \tag{4.7}
\]

Since \(p>0\), (4.6)--(4.7) imply

\[
p\sigma(x_0)\le A(x_0)-A(x_0+p)<1.                       \tag{4.8}
\]

Now

\[
\begin{aligned}
\pi\sigma(x_0)
&=\int_{x_0/K}^{x_0/\mu}\frac{dt}{\sqrt{1-t^2}}\\
&\ge\frac{x_0/\mu-x_0/K}{\sqrt{1-(x_0/K)^2}}
=\frac{\varepsilon x_0/\mu}{\sqrt{1-(x_0/K)^2}}.         \tag{4.9}
\end{aligned}
\]

Because \(U=n+\beta<n+1\), (4.4)--(4.5) give

\[
\frac{x_0}{\mu}>1-\widehat q,qquad
\frac{x_0}{K}>\rho-\frac{n+1}{K}=1-\varepsilon Q>0.
\]

Therefore

\[
1-(x_0/K)^2
<1-(1-\varepsilon Q)^2
<2\varepsilon Q.                                         \tag{4.10}
\]

Substitution into (4.9) yields the strict local-slope lower bound

\[
\sigma(x_0)>
\frac{y(1-\widehat q)}{\pi\sqrt{2Q}}.                     \tag{4.11}
\]

All quantities being squared are positive by (4.5).  Combining
(4.8) and (4.11) gives the required self-consistency inequality

\[
\boxed{
P^2<\frac{2\pi^2Q}{(1-\widehat q)^2}.}                    \tag{4.12}
\]

There is no continuity assumption across an ordinary-floor wall in this
derivation.

## 5. Complete synthetic comparison and \(R<5/y\)

First obtain a global cap on the synthetic path.  From (4.2), (2.1), and
\(r>0\),

\[
S=P+\frac{P-r}{d}<\frac{7P}{3}.                           \tag{5.1}
\]

Moreover, (3.5) and \(1/K<\varepsilon/2\) imply

\[
\begin{aligned}
\widehat q=\frac{n+1}{\mu}
&\le1-\frac{x_0}{\mu}+\frac1\mu\\
&<1-\frac1{2\rho}+\frac1{\rho K}<\frac12.               \tag{5.2}
\end{aligned}
\]

The last inequality is equivalent to \(1/K<\varepsilon/2\), and
\(1/K\le\varepsilon^2/24<\varepsilon/2\).

The monotone endpoint bounds

\[
\frac{y^2}{\kappa}\le\frac1{480},qquad
\frac y\kappa\le\frac1{24\sqrt{20}}<\frac1{96}           \tag{5.3}
\]

give

\[
Q<1+\frac1{480}+\frac{7P}{288}.                           \tag{5.4}
\]

Using \(\pi^2<10\), (4.12), (5.2), and (5.4),

\[
P^2<80Q<\frac{481}{6}+\frac{35P}{18}.                     \tag{5.5}
\]

For \(P\ge10\), the difference between the left side and the last
expression equals \(7/18\) at \(P=10\), and its increment from that point
is

\[
(P-10)\left(P+10-\frac{35}{18}\right)\ge0.
\]

Thus

\[
P<10.                                                      \tag{5.6}
\]

Now suppose, for contradiction, that \(r\ge5\).  The entire possible
synthetic path is then

\[
5\le r\le P<10,qquad S=P+\frac{P-r}{d}.                  \tag{5.7}
\]

It is important that this is an interval/path comparison, not an endpoint
sample.  From (5.7), for every point on the path,

\[
S\le P+\frac{P-5}{d}
\le\frac{7P}{3}-\frac{20}{3}<\frac{50}{3}.                \tag{5.8}
\]

At the no-drop endpoint \(P=r=5\), one has \(m=0\), \(S=P=5\), and
equality holds in the non-strict part of (5.8); thus that endpoint has not
been discarded.  At all other points where \(P>5\), the use of
\(1/d<4/3\) is strict.

Using \(\sqrt{20}>22/5\),

\[
Q-1
<\frac1{480}+\frac{25}{36\sqrt{20}}
<\frac1{480}+\frac{125}{792}
=\frac{2533}{15840}<\frac4{25}.                           \tag{5.9}
\]

The last comparison is exact:
\(2533\cdot25=63325<63360=4\cdot15840\).  Also

\[
\frac{y^2}{\rho}=\frac{y^2}{1-y^2}\le\frac1{19},
\]

because this function is increasing in \(y^2\) and
\(y^2\le1/20\).  Hence on the complete path (5.7),

\[
Q<\frac{29}{25},qquad
\widehat q<\frac4{475},qquad
1-\widehat q>\frac{471}{475}.                             \tag{5.10}
\]

The exact rational estimates

\[
\pi^2<\frac{484}{49},qquad
\left(\frac{475}{471}\right)^2<\frac{41}{40}              \tag{5.11}
\]

follow respectively from \(\pi<22/7\) and

\[
40\cdot475^2=9025000<9095481=41\cdot471^2.
\]

Thus (4.12) gives, at every point of (5.7),

\[
P^2
<2\frac{484}{49}\frac{29}{25}\frac{41}{40}
=\frac{1150952}{49000}<25,                                \tag{5.12}
\]

where \(1150952<1225000\).  This contradicts \(P\ge r\ge5\).
Therefore

\[
\boxed{r<5},\qquad
\boxed{R<\frac5y=\frac5{\sqrt\varepsilon}}.              \tag{5.13}
\]

The endpoint \(P=r=B=5\), all intermediate values \(5<P<10\), and all
\(5\le r\le P\) were included.  No sampled monotonicity or numerical sign
was used.

## 6. Compensation in every branch

From (2.3), \(K\eta>1\), so \(\lfloor K\eta\rfloor\ge1\).  Explicitly,
\(\sqrt2>1\), \(\pi<4\), and \(1/y\ge\sqrt{20}>4\) make the right side of
(2.3) greater than \(16\).

### Branch \(R\le0\)

Here

\[
M=\lfloor K\eta\rfloor-R\ge\lfloor K\eta\rfloor\ge1
>\frac{8\sqrt2}{15}>4\delta.                              \tag{6.1}
\]

The inequality \(8\sqrt2/15<1\) follows, for example, from
\(\sqrt2<3/2\).  This branch includes:

- the sign wall \(R=0\);
- an immediate floor drop \(p=0\), for which \(R=-dm\le0\);
- the degenerate head \(n=0\), where \(p=m=R=0\).

### Branch \(R>0\)

The ordinary-floor inequality

\[
\lfloor x\rfloor>x-1                                     \tag{6.2}
\]

is strict even when \(x\) is an integer.  By (2.3) and (5.13),

\[
\begin{aligned}
M
&>K\eta-1-R\\
&>\frac1y\left(\frac{16\sqrt2}{\pi}-5\right)-1.          \tag{6.3}
\end{aligned}
\]

Using \(\sqrt2>7/5\), \(\pi<22/7\), \(1/y\ge\sqrt{20}>4\),

\[
\frac{16\sqrt2}{\pi}-5>\frac{117}{55},
\qquad
M>\frac{413}{55}>\frac{16}{15}>\frac{8\sqrt2}{15}>4\delta.
                                                                    \tag{6.4}
\]

This branch includes the no-drop case \(p=n>0\), for which \(m=0\) and
\(R=p\).  It also includes the very first positive branch after the sign
wall: no estimate divides by \(R\), and the proof remains valid as
\(R\downarrow0^+\).  The case \(p=1\), whenever it is the first admissible
positive branch, is therefore covered without a separate limiting step.

Combining (3.1), (6.1), and (6.4) proves, for every low-interface start,

\[
\frac{\mathcal T_{r_0}}2
<\int_{x_0}^{K}A(z)\,dz.                                  \tag{6.5}
\]

Together with the closed high-interface result (1.5), every shifted tail is
controlled.  Equations (1.2)--(1.7) prove the frozen local claim.  Since all
uses of \(\kappa\) were \(\kappa\ge24\), the threshold face
\(\kappa=24\), equivalently \(K=24/\varepsilon^2\), is included.

## 7. Exact endpoint \(K_0(19/20)<3300^2\)

At \(\rho=19/20\),

\[
a_\rho=38\pi<38\frac{22}{7}=\frac{836}{7}<121,            \tag{7.1}
\]

so \(\sqrt{a_\rho}<11\).

The action estimate (2.2) at \(\varepsilon=1/20\) gives

\[
\eta_{19/20}\ge\frac1{30\pi\sqrt{10}}.                  \tag{7.2}
\]

Since \(\sqrt{10}<19/6\) and \(\pi<22/7\),

\[
\frac1{30\pi\sqrt{10}}>\frac7{2090}
>\frac{14000}{4199283}.                                  \tag{7.3}
\]

The last comparison is the exact cross multiplication

\[
7\cdot4199283=29394981>29260000=14000\cdot2090.
\]

Also \(\sqrt2<99/70\), since \(9800<9801\), and hence

\[
C_0=1+\frac{8\sqrt2}{15}<1+\frac{132}{175}
=\frac{307}{175}.                                        \tag{7.4}
\]

Let

\[
f(X)=\eta_{19/20}X^2-\sqrt{a_{19/20}}X-C_0.
\]

Its roots have opposite signs because their product is
\(-C_0/\eta_{19/20}<0\).  Its unique positive root is precisely

\[
X_+=\frac{\sqrt{a_{19/20}}
+\sqrt{a_{19/20}+4\eta_{19/20}C_0}}
{2\eta_{19/20}},
\qquad K_0(19/20)=X_+^2.                                  \tag{7.5}
\]

For \(Y=3300\), (7.1), (7.3), and (7.4) give

\[
\begin{aligned}
f(Y)
&>\frac{14000}{4199283}Y^2-11Y-\frac{307}{175}\\
&=\frac{26027100}{4199283}-\frac{307}{175}\\
&=\frac{32985481}{7422975}>0.                             \tag{7.6}
\end{aligned}
\]

For positive \(X\), the quadratic is negative below its unique positive
root and positive above it.  Thus (7.6) implies \(X_+<3300\), proving

\[
\boxed{K_0(19/20)<3300^2}.                                \tag{7.7}
\]

The fixed-rho theorem is stated for \(K\ge K_0\), so the face
\(K=K_0(19/20)\) itself is owned.

## 8. Wall and face ledger

The proof treats the mandatory faces as follows.

1. **\(\varepsilon=1/20\).**  This is \(y=1/\sqrt{20}\); every endpoint
   bound above is non-strict in the allowed direction, while the decisive
   comparisons retain strict slack.  The new theorem owns
   \(\kappa=24\) there.
2. **\(\varepsilon=1/25\).**  Both closed theorems apply.  The retained
   Round 10 theorem owns \(\kappa=20\), while the new theorem owns
   \(\kappa=24\); on the overlap the Round 10 threshold remains sharper.
3. **\(\varepsilon=1/100\).**  The retained Round 10 theorem owns
   \(\kappa=20\), and the accepted all-frequency endpoint owns
   \(\rho=99/100\) from the other side.  The new local theorem also holds
   at its own larger threshold but is not used to weaken the accepted one.
4. **Ratio faces.**  \(\rho=19/20\) is shared by the fixed-rho central
   regime and the new seam; \(\rho=24/25\) is shared by the new and Round
   10 seams; \(\rho=99/100\) is shared by Round 10 and the accepted
   all-frequency endpoint.  Every interval is closed at the shared face.
5. **Plateau faces.**  \(n=0\), \(p=0\), and \(R=0\) lie in (6.1).
   The no-drop face \(p=n>0\) lies in the \(R>0\) proof and its synthetic
   endpoint \(P=r=5\) was explicitly retained in (5.8).  The first branch
   with \(R>0\) is covered uniformly.
6. **Ordinary-floor walls.**  Equality of plateau floors gives the strict
   loss (4.7), including when either argument is an integer.  The gain wall
   \(K\eta\in\mathbb Z\) is covered by (6.2).  Coarse proxy walls use only
   the one-sided majorization (1.3).
7. **Interface walls.**  \(x_0=\mu\) belongs to the high-angular theorem;
   \(x_0<\mu\) belongs to the low decomposition.  At \(q=\mu\),
   \(\delta=0\).  No value of the divergent inner correction at the
   interface is used.
8. **Strict spectral walls.**  At a shell eigenfrequency, the separated
   count uses \(n\pi<\Psi\), not \(n\pi\le\Psi\).  If \(\nu=K\), the
   channel is excluded by the sharp active cutoff \(\nu<K\).
9. **Monotonic endpoints.**  The bounds \(y^2/\kappa\) and \(y/\kappa\)
   are maximized by increasing \(y\) and decreasing \(\kappa\), hence at
   \(y=1/\sqrt{20}\), \(\kappa=24\).  The ratio
   \(y^2/(1-y^2)\) is increasing in \(y^2\), hence is at most \(1/19\).
   In (3.4), after replacing \(\rho\) by \(1\), the remaining factors
   \(y/\sqrt\kappa\) and \(y^4/\kappa\) have the same endpoint direction.
   The action lower bound \(\kappa/y\) is weakest at \(\kappa=24\) and
   maximal allowed \(y\).  Finally, \(\varepsilon^{-2}\) decreases as
   \(\varepsilon\) increases, so the combined seam threshold is largest at
   \(\varepsilon=1/100\).  These are algebraic monotonicities, not sampled
   claims; the monotonicity of \(K_0\) used in the central union is the
   separately permitted audited input.
10. **Energy faces.**  \(K=K_0(19/20)\) is included by the fixed-rho
    theorem.  The global statement below uses \(K\ge3300^2\), so
    \(K=3300^2\) is included as well.

## 9. Required closed global union

Use the permitted prior closed theorems only in their stated domains.

- The small-hole endpoint owns every frequency for
  \(0<\rho\le\rho_*\), where
  \[
  \rho_*=
  \frac{\frac{\sqrt3}{2\pi}-\frac16}
       {2+\frac{16\sqrt2}{15}}.
  \]
  On the closed residual strip
  \([\rho_*,1/16]\), the prior envelope leaves only \(K<64\).  Thus
  \(\rho=\rho_*\), \(\rho=1/16\), and \(K=64\) have no ownership gap.
- On \([1/16,19/20]\), the permitted monotonicity of \(K_0\) gives
  \(K_0(\rho)\le K_0(19/20)\).  Since equality \(K=K_0(\rho)\) is covered,
  every residual satisfies
  \[
  K<K_0(\rho)\le K_0(19/20)<3300^2.
  \]
- On \([19/20,24/25]\), use the new theorem with
  \(1/25\le\varepsilon\le1/20\).  On
  \([24/25,99/100]\), use the sharper retained Round 10 theorem on every
  overlap.  Across the combined closed strip one may use the coarser common
  ceiling
  \[
  \frac{24}{(1/100)^2}=240000<3300^2=10890000.
  \]
  At \(\rho=24/25\), both seam theorems own the face, with Round 10 sharper.
- The accepted all-frequency endpoint owns the closed-left interval
  \([99/100,1)\).  The face \(\rho=99/100\) is also owned from the Round 10
  side.

Thus every \(0<\rho<1\) is covered at, and above, the exact energy face
\(K=3300^2\):

\[
\boxed{0<\rho<1,\qquad K\ge3300^2.}                       \tag{9.1}
\]

This does not enlarge the all-frequency endpoint beyond
\(99/100\le\rho<1\), and it does not close the compact residual below the
new ceiling.  In particular, `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` remain outside this promotion.

## Final PASS/FAIL statement

**PASS:** the constant \(24\), all stated closed threshold faces, the exact
comparison \(K_0(19/20)<3300^2\), and the closed global union all survive
the isolated reconstruction.

**FAIL:** none.
