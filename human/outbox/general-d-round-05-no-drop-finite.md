# General dimension, Round 5: finite no-drop reductions

Date: 18 July 2026

Status: rigorous partial closure of the finite no-drop problem. This note
proves every no-drop branch with \(n=1\), and replaces the explicit
\(f=2,3\) cutoff \(n<72\,000\) by

\[
 \boxed{n<380.}
\]

The remaining chambers below that cutoff are not certified here. No
manuscript file is changed by this note.

## 1. Setup and inputs

Use the no-drop notation

\[
 \delta=K-\mu,\qquad n=\lfloor\mu-r\rfloor,\qquad
 q=r+n,\qquad \alpha=\mu-q\in[0,1),
\]

and suppose

\[
 \left\lfloor A(r+j)+\frac14\right\rfloor=f
 \qquad(0\le j\le n),\qquad f\ge2.                 \tag{1}
\]

The reduced scalar is

\[
 \mathscr S_n=D_A(q)+R_n,\qquad
 R_n=2\int_r^qA(z)\,dz-2nf.                        \tag{2}
\]

Only \(R_n<0\) needs consideration. In that residual branch the exact
no-drop identity gives

\[
 b:=f-\frac14\le A(q)<f.                           \tag{3}
\]

Since \(r\ge1/2\) and \(n\ge1\), every terminal start considered below
satisfies

\[
 q\ge\frac32.                                      \tag{4}
\]

## 2. A uniform half-unit terminal reserve

The first new observation is independent of the critical scaling.

### Proposition 2.1

Let \(q\le\mu<q+1\), \(q\ge3/2\), and suppose

\[
 A(q)\ge\frac74.
\]

Then

\[
 \boxed{D_A(q)>\frac12.}                            \tag{5}
\]

The assertion includes the lower ordinary-floor wall at \(q\).

### Proof

Put

\[
 v=G_K(q),\qquad h=G_\mu(q),\qquad
 f=\left\lfloor A(q)+\frac14\right\rfloor\ge2,
 \qquad
 Q=\left[A(q)+\frac14\right]_<,\qquad
 B=\left[v+\frac14\right]_<.
\]

If \(q=\mu\), the inner cap vanishes. Otherwise it is sharply bounded
by its endpoint chord: since \(G_\mu\) is strictly convex on
\([q,\mu]\),

\[
 2\int_q^\mu G_\mu(z)\,dz<h(\mu-q)<h.
\]

Moreover \(h\le G_{q+1}(q)\), and

\[
 \frac{d}{dq}G_{q+1}(q)
 =\frac{\sin\vartheta-\vartheta}{\pi}<0,\qquad
 \vartheta=\arccos\frac{q}{q+1}.
\]

Consequently

\[
 \boxed{
 2\int_q^\mu G_\mu(z)\,dz
 <G_{5/2}(3/2)<\frac15.}                            \tag{6}
\]

For \(1\le k\le B\), let \(\theta_k\) be the exact ball angle at
level \(k-1/4\). The fractional-top exact-angle theorem gives

\[
 D_A(q)\ge
 \frac\pi2\sum_{k=1}^{B}\frac1{\theta_k}
 -Q-2\int_q^\mu G_\mu(z)\,dz.                      \tag{7}
\]

The omitted fractional-top term is nonnegative.

First suppose \(q\ge K/2\). Every active level lies strictly to the
right of \(q\), so

\[
 \theta_k<\arccos(q/K)\le\frac\pi3,\qquad
 \frac\pi{2\theta_k}>\frac32.                       \tag{8}
\]

Away from the lower wall, \(Q=f\) and \(B\ge f\), so (6)--(8) give more
than \(f/2-1/5\ge4/5\). At the lower wall, \(Q=f-1\). If \(q<\mu\),
then \(h>0\) and \(B\ge f\), which is still stronger. If \(q=\mu\),
then the cap vanishes and \(B=Q=f-1\); pairing each count unit with its
angle term gives
\[
 D_A(q)>\frac12(f-1)\ge\frac12.
\]

It remains to treat \(q<K/2\). Let \(K_*\) be the unique solution of

\[
 G_{K_*}(3/2)=\frac74.                              \tag{9}
\]

Monotonicity of \(G_K(q)\) in \(K\), and its decrease in \(q\), imply
\(K\ge K_*\). The exact angles decrease with \(K\). Outward Arb
arithmetic at (9) proves

\[
 \theta_1<\frac{503}{500},\qquad
 \theta_2<\frac{11}{8},                             \tag{10}
\]

and hence

\[
 \boxed{
 \frac\pi2\left(\frac1{\theta_1}+\frac1{\theta_2}\right)-2
 >\frac7{10},\qquad
 \frac\pi{2\theta_1}-1>\frac12.}                    \tag{11}
\]

Away from the lower wall, \(Q=f\), \(B\ge f\ge2\), and every term with
\(k\ge3\) has \(\pi/(2\theta_k)-1>0\). Equations (6), (7), and the
first inequality in (11) therefore give

\[
 D_A(q)>\frac7{10}-\frac15=\frac12.
\]

At the lower wall with \(q=\mu\), one has \(B=Q=f-1\) and zero cap; the
second inequality in (11) applies. At the lower wall with \(q<\mu\),
one has \(B\ge f=Q+1\), so the estimate is stronger by at least one
unit. This proves (5) with every strict-wall convention retained.

### Corollary 2.2: closure of \(n=1\)

Every no-drop branch with \(f\ge2\) and \(n=1\) satisfies

\[
 \boxed{\mathscr S_1>0.}                            \tag{12}
\]

Indeed, \(A\) is concave on the inner interval \([r,q]\), and therefore

\[
 2\int_r^q A(z)\,dz\ge A(r)+A(q)\ge2f-\frac12.
\]

Thus \(R_1\ge-1/2\), while Proposition 2.1 gives \(D_A(q)>1/2\).

### Corollary 2.3: an explicit finite-chamber sector

For arbitrary \(n\ge1\), put

\[
 \varepsilon=A(q)+\frac14-f,\qquad
 \Delta=A(r)-A(q).
\]

Every no-drop branch satisfying

\[
 \boxed{
 2\varepsilon+\Delta+
 \frac{n\Delta}{3(2r+n)}
 \ge\frac12-\frac1{2n}}                             \tag{12a}
\]

has \(\mathscr S_n>0\). Indeed, the audited shelf-curvature bound gives

\[
 R_n\ge
 \frac{n^2\Delta}{3(2r+n)}
 +n\left(2\varepsilon+\Delta-\frac12\right)\ge-\frac12,
\]

and Proposition 2.1 pays the remaining half unit. Thus any interval
certificate for the residual finite chambers may discard the whole sector
(12a) before evaluating terminal angles.

## 3. A direct critical-profile remainder

We next improve the quantitative transfer for the two noncompact rows
\(f=2,3\). Assume the explicit no-drop cone from Round 4d. Put

\[
 s=\sqrt{\delta/K},\qquad
 \kappa=s\delta=s^3K,\qquad X=s(\mu-z),              \tag{13}
\]

and

\[
 \mathcal H_{s,\kappa}(X)
 :=A\left(\mu-\frac Xs\right),\qquad
 H_\kappa(X)
 :=\frac{c_0}{\sqrt\kappa}
 \left((\kappa+X)^{3/2}-X^{3/2}\right),\quad
 c_0=\frac{2\sqrt2}{3\pi}.                          \tag{14}
\]

The endpoint floors give

\[
 \frac{21}{8}\le\kappa,\qquad A(q)<f\le3.            \tag{15}
\]

Unlike the earlier two-ball subtraction estimate, the shell has the
following non-cancelling integral representation. With \(a=K-u/s\),
direct substitution in the radius derivative formula gives

\[
 \boxed{
 \mathcal H_{s,\kappa}(X)
 =\frac1\pi\int_0^\kappa
 \frac{\sqrt{(\kappa+X-u)
 [2\kappa-(\kappa+X+u)s^2]}}
 {\kappa-us^2}\,du.}                                \tag{16}
\]

The ratio of its integrand to the integrand defining \(H_\kappa\) is

\[
 \mathcal R(u,X)
 =\frac{\sqrt{1-a(u,X)s^2}}{1-b(u)s^2},\qquad
 a(u,X)=\frac{\kappa+X+u}{2\kappa},\quad
 b(u)=\frac u\kappa.                                \tag{17}
\]

### Lemma 3.1

If \(0<s\le1/10\), then, for \(0\le X\le2\) at every physical point
\(\mu-X/s\ge0\),

\[
 \boxed{
 \left|\mathcal H_{s,\kappa}(X)-H_\kappa(X)\right|
 <6s^2.}                                            \tag{18}
\]

### Proof

For \(0\le X\le2\), (15) gives

\[
 0\le b\le1,\qquad 0\le a\le1+\frac1\kappa\le\frac{29}{21}.
\]

The elementary bounds

\[
 1-y\le\sqrt{1-y}\le1,\qquad
 \frac1{1-s^2}-1\le\frac{100}{99}s^2
\]

therefore imply

\[
 |\mathcal R-1|\le\frac{29}{21}s^2.                 \tag{19}
\]

Let \(X_q=s\alpha\in[0,s)\). At \(X_q\), the sharper bound
\(a\le107/105\) and (17) give

\[
 H_\kappa(X_q)
 \le\frac{\mathcal H_{s,\kappa}(X_q)}
 {1-(107/105)s^2}
 <\frac{31}{10},                                    \tag{20}
\]

because \(\mathcal H_{s,\kappa}(X_q)=A(q)<3\). Also

\[
 0<H_\kappa'(X)<\frac12.                            \tag{21}
\]

Hence \(H_\kappa(X)<41/10\) throughout \([0,2]\). Integrating (19)
against the positive limiting integrand now gives

\[
 |\mathcal H_{s,\kappa}(X)-H_\kappa(X)|
 <\frac{29}{21}\frac{41}{10}s^2<6s^2.
\]

This proves (18).

## 4. Quantitative closure for \(s\le1/10\)

Set

\[
 \zeta=\frac s2+6s^2\le\frac{11}{100},\qquad
 w=H_\kappa(0)=c_0\kappa.                           \tag{22}
\]

Equations (18), (21), and \(A(q)\ge b\) imply

\[
 w>b-\zeta.                                         \tag{23}
\]

For \(X=\kappa u\), introduce

\[
 t=\sqrt{1+u}-\sqrt u.
\]

Then

\[
 \frac{H_\kappa(X)}w=F(t):=\frac{3/t+t^3}{4},\qquad
 H_\kappa'(X)=\frac{3c_0}{2}t.                     \tag{24}
\]

Let \(X_*\) be the point where \(H_\kappa(X_*)=f+\zeta\). In fact
\(w<f+\zeta\): otherwise (18) at \(X_q\), together with
\(H_\kappa(X_q)\ge w\), would give
\[
 A(q)>f+\zeta-6s^2=f+\frac s2,
\]
contrary to (3). Thus \(X_*>0\), and

\[
 \frac{f+\zeta}{w}
 <\frac{f+\zeta}{f-1/4-\zeta}
 \le\frac{211}{164}
 <\frac{163}{125}=F(3/5).
\]

Since \(F\) decreases, \(t_*>3/5\). Thus on \([0,X_*]\),

\[
 H_\kappa'(X)>\frac9{10}c_0.                        \tag{25}
\]

Writing \(d=f+\zeta-w\), equations (22)--(25) give

\[
 0<d<\frac14+2\zeta\le\frac{47}{100},\qquad
 X_*<\frac{10d}{9c_0}<\frac{19}{10}.                \tag{26}
\]

In particular \(X_q+X_*<2\), so Lemma 3.1 applies on the whole possible
negative head. The exact profile is increasing. Its negative part is
therefore confined to this interval, and

\[
 \begin{aligned}
 sR_n
 &\ge-2\int_0^{X_*}(f+\zeta-H_\kappa(X))\,dX\\
 &\ge-\frac{10d^2}{9c_0}.
 \end{aligned}                                      \tag{27}
\]

For the last step, \(f+\zeta-H_\kappa\) is convex with endpoint values
\(d,0\), so its integral is at most \(dX_*/2\).

The first exact terminal angle gives

\[
 sD_A(q)\ge
 \frac\pi{2\sqrt2}
 \left(\frac{b-\zeta}{3/4}\right)^{1/3}
 \left(1-\frac{3s^2}{10}\right)
 -\frac{17}{5}s.                                    \tag{28}
\]

For completeness, this step does not use the earlier restriction
\(s<10^{-3}\). If \(\theta\) is the first angle and
\(x=(3\pi(3/4)/K)^{1/3}\), the chord bound for sine gives
\(\theta<\sqrt3\,s\). The Taylor inequality
\(\sin\theta-\theta\cos\theta\ge\theta^3/3-\theta^5/30\)
then gives the factor \(1-3s^2/10\). The leading term is
\[
 \frac{\pi s}{2x}
 =\frac\pi{2\sqrt2}\left(\frac{w}{3/4}\right)^{1/3}.
\]
Finally \(Q\le3\), while the inner cap is smaller than \(2/5\), so the
discarded finite terms cost at most \(17s/5\). This proves (28) directly
for \(s\le1/10\).

All constants now close rationally. Namely,

\[
 \frac\pi{2\sqrt2}>1,\qquad c_0>\frac{49}{165},\qquad
 \frac{b-\zeta}{3/4}\ge\frac{164}{75}
 >\left(\frac{129}{100}\right)^3.
\]

Combining (27)--(28) yields

\[
 \begin{aligned}
 s\mathscr S_n
 &>
 \frac{129}{100}\frac{997}{1000}
 -\frac{17}{50}
 -\frac{10}{9}\frac{165}{49}
  \left(\frac{47}{100}\right)^2\\
 &=\frac{1758611}{14700000}>\frac1{10}.
 \end{aligned}                                      \tag{29}
\]

We have proved the following strengthened transfer.

### Theorem 4.1

Every residual no-drop candidate on the \(f=2,3\) cone with

\[
 s\le\frac1{10}
\]

satisfies

\[
 \boxed{s\mathscr S_n>\frac1{10}.}                  \tag{30}
\]

All endpoint walls are included.

## 5. The new integer cutoff

The cone gives

\[
 \delta\ge\frac{c_f}{2}n,\qquad
 c_f=\frac{\sqrt{1+(f-1/4)^2}-1}{2}.                \tag{31}
\]

On the other hand, the endpoint-action lower bound from Round 4d is

\[
 A(q)\ge\frac{2\kappa}{3\pi}.
\]

Together with (3), this gives

\[
 \kappa<\frac{3\pi f}{2},\qquad
 s=\frac\kappa\delta
 <\frac{3\pi f}{c_fn}<\frac{38}{n}
 \quad(f=2,3).                                      \tag{32}
\]

For \(f=2\), the last coefficient is

\[
 \frac{48\pi}{\sqrt{65}-4}<38;
\]

for \(f=3\), it is

\[
 \frac{72\pi}{\sqrt{137}-4}<38.
\]

The rational bounds \(\pi<22/7\), \(\sqrt{65}>8\), and
\(\sqrt{137}>11\) already prove both comparisons.

If \(n\ge380\), (32) gives \(s<1/10\), and Theorem 4.1 closes the branch.
Hence

\[
 \boxed{
 f\in\{2,3\}\text{ and }\mathscr S_n<0
 \quad\Longrightarrow\quad n<380.}                 \tag{33}
\]

This replaces the previous \(n<72\,000\) cutoff.

## 6. Exact remaining scope

Combining this note with the audited Round 4 exhaustion gives the following
rigorous state of the no-drop branch.

1. Every \(n=1\) branch is proved.
2. The central necessary box remains \(2\le f\le49\), \(n\le48\), but its
   two retained \(n=1\) pairs are removed. Thus 647 of the previously
   listed 649 necessary pairs remain before chamber certification.
3. The finite outer box for \(f\ge4\) remains
   \(4\le f\le8\), \(n\le39\). None of its 60 retained necessary pairs
   had \(n=1\).
4. The two exceptional rows \(f=2,3\) now satisfy \(2\le n\le379\).

These are discrete-pair reductions, not certifications of all continuous
\((K,\mu)\)-chambers in the boxes. The no-drop theorem is therefore still
open below the displayed cutoffs.

The outward-rounded constants, the isolated radius \(K_*\), and the
rational closure in (29) are replayed by
[general_d_no_drop_round5_verify.py](../../scripts/general_d_no_drop_round5_verify.py).
At 512-bit precision it reports PASS.
