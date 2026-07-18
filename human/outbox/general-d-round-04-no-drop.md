# General dimension, Round 4: the no-drop branch \(p=n\)

Date: 18 July 2026

Status: rigorous reduction, not a proof of the global shifted-tail theorem.
The no-drop scalar has an exact endpoint-wall identity and an exact weighted
slope formula which are sharper than the generic first-shelf estimate.  They
localize the unresolved part to one explicit coupling inequality.  A
certified active-region example shows that the first-shelf reserve can be
strictly negative in this branch, so the quantitative one-interface reserve
cannot be replaced by its already-proved nonnegativity.

## 1. Setup and conventions

Let

\[
 G_a(z)=\frac{\sqrt{a^2-z^2}-z\arccos(z/a)}{\pi}
 \quad (0\le z<a),
 \qquad G_a(z)=0\quad(z\ge a),
\]

and put

\[
 \mu=\rho K,
 \qquad A=G_K-G_\mu,
 \qquad
 [x]_<:=\max\{0,\lceil x\rceil-1\}.
\]

For a positive integer or half-integer shift \(s\), write

\[
 T_A(s)=[A(s)+\tfrac14]_<
 +2\sum_{j\ge1}[A(s+j)+\tfrac14]_<,
 \qquad
 D_A(s)=2\int_s^K A(z)\,dz-T_A(s).
\]

Suppose \(r<\mu\), and set

\[
 n=\lfloor\mu-r\rfloor,
 \qquad q=r+n,
 \qquad
 F_j=\left\lfloor A(r+j)+\frac14\right\rfloor
 \quad(0\le j\le n).
\]

This note treats the no-drop branch

\[
 F_0=F_1=\cdots=F_n=:m,
 \qquad p=n.
\]

Its first-shelf reserve and reduced scalar are

\[
 R_n=2\int_r^q A(z)\,dz-2nm,
 \qquad
 \mathscr S_n:=D_A(q)+R_n.
 \tag{1}
\]

The case \(n=0\) is already the proved one-interface theorem, so below
\(n\ge1\) unless stated otherwise.

## 2. Exact endpoint-wall slack

Define

\[
 \chi_q=
 \begin{cases}
 1,&A(q)+\frac14=m,\\
 0,&A(q)+\frac14>m.
 \end{cases}
 \tag{2}
\]

The upper alternative \(A(q)+1/4=m+1\) is impossible because its ordinary
floor would be \(m+1\).

### Proposition 2.1

In the no-drop branch,

\[
 \boxed{D_A(r)=D_A(q)+R_n+\chi_q.}
 \tag{3}
\]

Equivalently,

\[
 \boxed{\mathscr S_n=D_A(r)-\chi_q.}
 \tag{4}
\]

#### Proof

Put \(b_j=[A(r+j)+1/4]_<\).  The shell action is strictly decreasing on
the inner branch.  Hence \(A(r+j)+1/4=m\) cannot occur for \(j<n\): the
next sample would have ordinary floor at most \(m-1\), contradicting
no-drop.  Therefore

\[
 b_j=m\quad(0\le j<n),
 \qquad b_n=m-\chi_q.
\]

Separating the tail at \(q=r+n\) gives

\[
 T_A(r)-T_A(q)
 =b_0+2\sum_{j=1}^{n-1}b_j+b_n
 =2nm-\chi_q.
\]

Subtracting this identity from the corresponding integral decomposition
proves (3).  This computation uses the strict bracket at the wall and
therefore needs no limiting convention.

Away from the single possible lower wall at \(q\), the reduced scalar is
exactly the original tail defect.  At that wall it is a genuinely stronger
quantity by one unit.  Thus proving \(D_A(r)\ge0\) elsewhere and appealing
to continuity would not by itself prove the wall value of (1).

## 3. Exact weighted-slope formula

Let

\[
 \varepsilon=
 A(q)+\frac14-m\in[0,1),
 \qquad
 \sigma(z)=-A'(z)
 =\frac{\arccos(z/K)-\arccos(z/\mu)}{\pi}
 \quad(z<\mu).
 \tag{5}
\]

### Proposition 3.1

The head reserve has the exact representation

\[
 \boxed{
 R_n=-\frac n2+2n\varepsilon
 +2\int_0^n u\,\sigma(r+u)\,du.}
 \tag{6}
\]

#### Proof

Since \(m=A(q)+1/4-\varepsilon\),

\[
 \begin{aligned}
 R_n
 &=2\int_0^n\bigl(A(r+t)-A(q)\bigr)\,dt
   +2n\left(\varepsilon-\frac14\right)\\
 &=2\int_0^n\int_t^n\sigma(r+u)\,du\,dt
   +2n\left(\varepsilon-\frac14\right).
 \end{aligned}
\]

Reversing the order of integration proves (6).

Formula (6) is stronger than the generic bound
\(R_n\ge-n/2+2\int_0^n u\sigma(r+u)\,du\), because it retains the terminal
floor fraction \(2n\varepsilon\).

The one-interface theorem gives \(D_A(q)\ge0\).  Consequently all of the
following no-drop tails are already proved:

1. \(n=0\);
2. \(m=0\), because then \(R_n=2\int_r^qA\ge0\);
3. \(\varepsilon\ge1/4\);
4. more generally,
   \[
   2\int_0^n u\sigma(r+u)\,du
   \ge n\left(\frac12-2\varepsilon\right).
   \tag{7}
   \]

Thus a genuinely unresolved no-drop tail must satisfy

\[
 \boxed{
 n\ge1,\quad m\ge1,\quad 0\le\varepsilon<\frac14,\quad
 2\int_0^n u\sigma(r+u)\,du
 <n\left(\frac12-2\varepsilon\right).}
 \tag{8}
\]

The exact remaining payment is

\[
 \boxed{
 D_A(q)\ge
 \mathfrak h_n:=
 \frac n2-2n\varepsilon
 -2\int_0^n u\sigma(r+u)\,du>0.}
 \tag{9}
\]

This is the sharp residual for the no-drop branch produced by the
first-shelf reduction; no generic \(-n/2\) loss remains hidden in it.

## 4. Exact terminal coupling

Let

\[
 I_a(x)=\int_x^aG_a(z)\,dz,
 \qquad h=G_\mu(q),
\]

and define the strict ball defect and first-sample loss by

\[
 \begin{aligned}
 D_K(q)&=2I_K(q)-
 \left([G_K(q)+\tfrac14]_<
 +2\sum_{j\ge1}[G_K(q+j)+\tfrac14]_<\right),\\
 \lambda_q&=[G_K(q)+\tfrac14]_<-[A(q)+\tfrac14]_<.
 \end{aligned}
\]

The exact one-interface identity reads

\[
 D_A(q)=D_K(q)+\lambda_q-2I_\mu(q).
 \tag{10}
\]

In the only unresolved branch \(m\ge1\).  Integer translation of the
strict bracket and (5) then give the unambiguous exact floor formula

\[
 \boxed{
 \lambda_q=\lceil\varepsilon+h\rceil-\lceil\varepsilon\rceil.}
 \tag{11}
\]

Combining (6) and (10), the no-drop problem is exactly

\[
 \boxed{
 D_K(q)+\lambda_q-2I_\mu(q)
 \ge
 \frac n2-2n\varepsilon
 -2\int_0^n u\sigma(r+u)\,du.}
 \tag{12}
\]

There is a second exact form in which the fractional interface cap is
already combined with the inner head:

\[
 \boxed{
 \mathscr S_n
 =D_K(q)+\lambda_q
 +2\int_r^qG_K(z)\,dz
 -2I_\mu(r)-2nm.}
 \tag{13}
\]

Indeed, the \(G_\mu\)-integrals over \([r,q]\) and \([q,\mu]\) concatenate
to \(I_\mu(r)\).  Formula (13) is preferable to separately replacing
\(D_K(q)\) by a coarse integer reserve and \(I_\mu(q)\) by its universal
turning bound: those two independent weakenings destroy precisely the
coupling needed in (12).

No-drop also gives the strict action-drop constraint

\[
 A(r)-A(q)<1.
 \tag{14}
\]

In the dimension-independent spectral active region,

\[
 K>\frac{\pi}{1-\rho}
 \quad\Longleftrightarrow\quad
 K-\mu>\pi.
 \tag{15}
\]

Writing \(\alpha=\mu-q\in[0,1)\), every terminal tail in this note
therefore has the additional exact width

\[
 K-q=(K-\mu)+\alpha>\pi.
 \tag{16}
\]

Any successful estimate of the left side of (12) should retain (16); the
already-proved one-interface theorem did not need this extra width and
therefore does not quantify all of its available reserve.

## 5. Monotone two-parameter wall reduction

Fix \(r,n,q,m\), and work in an open combinatorial chamber on which all
strict tail brackets beginning at \(q\) and the no-drop floor \(m\) are
constant.  Then

\[
 \mathscr S_n(K,\mu)
 =2\bigl(I_K(r)-I_\mu(r)\bigr)-T_A(q)-2nm.
 \tag{17}
\]

The radius derivative

\[
 \partial_aG_a(z)=\frac1\pi\sqrt{1-\frac{z^2}{a^2}}
 \quad(z<a)
\]

gives

\[
 \boxed{
 \partial_K\mathscr S_n
 =\frac2\pi\int_r^K\sqrt{1-\frac{z^2}{K^2}}\,dz>0,}
 \tag{18}
\]

and

\[
 \boxed{
 \partial_\mu\mathscr S_n
 =-\frac2\pi\int_r^\mu\sqrt{1-\frac{z^2}{\mu^2}}\,dz<0.}
 \tag{19}
\]

Hence the infimum of each smooth chamber lies on its lower-\(K\),
upper-\(\mu\) boundary.  Across a sample wall, the relevant one-sided face
must be retained according to the strict-bracket convention; across a
head wall, the ordinary floor at equality must be retained.  Thus (18)--
(19) give a genuine wall reduction, not a license to ignore equality
faces.

For fixed discrete data, the candidate boundaries are:

* \(K-\mu=\pi\), the closure of the active boundary;
* \(\mu=q\) or \(\mu=q+1\);
* a head wall \(A(r+j)+1/4\in\mathbb Z\);
* a terminal wall \(A(q+j)+1/4\in\mathbb Z\).

This is finite on any compact \(K,\mu\) box.  It is not yet a global finite
certificate because (18)--(19) alone do not bound the possible
\((r,n,m)\) as \(\rho\uparrow1\).

## 6. Certified obstruction to discarding the terminal reserve

Take the exact rational parameters

\[
 K=\frac{23}{4},\qquad
 \mu=\frac{103}{40},\qquad
 \rho=\frac{103}{230},\qquad
 r=\frac12.
 \tag{20}
\]

Then

\[
 K-\mu=\frac{127}{40}>\pi,\qquad
 n=2,\qquad q=\frac52.
\]

Outward Arb interval arithmetic at 256-bit precision certifies

\[
 \begin{aligned}
 A(\tfrac12)&=1.0020569943\ldots,\\
 A(\tfrac32)&=0.9297973629\ldots,\\
 A(\tfrac52)&=0.7523237293\ldots,
 \end{aligned}
\]

and each of the three ordinary floors after adding \(1/4\) is exactly
\(1\).  Thus this is an active no-drop tail with \(m=1\), away from the
endpoint wall.  The same certified evaluation gives

\[
 \boxed{
 R_2<-0.34,\qquad
 D_A(q)>0.94,\qquad
 \mathscr S_2>0.59.}
 \tag{21}
\]

Here \(A(q+1)<3/4\), so \(T_A(q)=1\); the displayed bounds are direct
evaluations of the elementary antiderivative for \(G_a\).  They are
replayed, with exact rational inputs and outward interval arithmetic, by
[the Arb replay script](../../scripts/general_d_no_drop_example_verify.py).
Therefore (20) is a rigorous counterexample to the proposed shortcut
\(R_n\ge0\) in the no-drop branch.  It is not a counterexample to the
shifted-tail inequality: the quantitative terminal reserve more than pays
the negative head.

## 7. Numerical falsification and exact status

A floating-point falsification scan sampled 300,000 active-region
parameter triples with \(K\le1000\).  It found 39,657 cases satisfying
\(n\ge1\), \(m\ge1\), and \(p=n\).  The smallest observed value of
\(D_A(q)+R_n\) was about \(0.5989\); no negative scalar was found.  A
separate search found head reserves below \(-1.15\), again with a much
larger positive terminal reserve.  These scans are diagnostics only and
are not used in any proposition above.

The universal no-drop theorem is therefore still open.  Its exact
remaining statement is (12), restricted by (8), (14), and (16), with all
floor walls retained.  The next useful proof step is to turn the terminal
width \(K-q>\pi\) into a quantitative lower bound for the left side of
(12) which depends on the same endpoint fraction \(\varepsilon\) and
weighted inner slope appearing on the right.  A bound on \(D_A(q)\) that
depends only on its sign, or only on
\(\lfloor G_K(\max\{q,K/2\})\rfloor\), loses that correlation and cannot
close the no-drop branch.
