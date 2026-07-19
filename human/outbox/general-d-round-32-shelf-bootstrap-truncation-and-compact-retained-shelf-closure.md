# General-dimensional Round 32: shelf-bootstrap truncation and compact retained-shelf closure

Date: 19 July 2026

Status: analytic shelf strengthening proved; the finite parity-grid remainder
is closed by one compact directed-Arb certificate.  This closes only the
Round 30 included retained-\(E\) lower shelf.  It does not close the other
high-floor endpoint families, full high-floor CST, pointwise assembly, or the
all-dimensional theorem.

## 0. Statement and strict-wall conventions

Retain all Round 30--31 notation.  In particular,

\[
 \tan\theta_j-\theta_j=\frac{3\pi}{4(q+j)},\qquad
 K_j=\frac{q+j}{\cos\theta_j},\qquad j=2,3,
\]

\[
 \psi=\arccos\frac q{K_3},\qquad
 d=1-\frac{2\psi}{\pi},
\]

and let \(L_q(p,x)\) be the Round 31 lower scalar

\[
 \begin{aligned}
 L_q(p,x)={}&\frac7{10}
 +\frac23p^2(3x-p)
 \left[A+B\{x^2+(x-p)^2\}\right]\\
 &-\frac p2+\frac{d(q-x)}2,
 \end{aligned}
\tag{0.1}
\]

where

\[
 A=\frac{(q+1)^{-1}-K_2^{-1}}{2\pi},\qquad
 B=\frac{(q+1)^{-3}-K_2^{-3}}{24\pi}.
\tag{0.2}
\]

Define, only for \(q\ge35\),

\[
 y(q)=\frac\pi\psi-3,
 \qquad
 m_\sharp(q)=
 \left\lfloor\frac65y(q)\right\rfloor+1.
\tag{0.3}
\]

For the finite proof put

\[
 m_0(q)=
 \begin{cases}
 1,&3\le q<35,\\
 m_\sharp(q),&35\le q<1000.
 \end{cases}
\tag{0.4}
\]

The distinction in (0.4) is essential: formula (0.3) is not asserted below
\(q=35\).

This round proves:

1. every necessary lower-shelf point with real \(q\ge35\) satisfies the
   strict intrinsic bootstrap
   \[
    \boxed{m>\frac65\left(\frac\pi\psi-3\right)};
   \tag{0.5}
   \]
2. on the exact integer grid \(q=3,4,\ldots,999\), with \(r_0=1\), and
   the exact half-integer grid
   \(q=7/2,9/2,\ldots,1999/2\), with \(r_0=3/2\),
   \[
   L_q(p,x)>0
   \tag{0.6}
   \]
   throughout
   \[
    p\ge1,\qquad x-p\ge r_0,\qquad q-x\ge m_0(q);
   \tag{0.7}
   \]
3. together with the Round 31 real exclusion for \(q\ge1000\), the
   Round 30 retained lower-shelf scalar satisfies
   \(\mathfrak F>0\) at every necessary point on both inherited grids.

Shelf feasibility is allowed with equality.  The hard wall \(p=dm\) and
the wall \(E_{\min}=1/2-dm/(2p)\) retain their earlier automatic owner;
this note treats their strict complement.  The real endpoint \(q=1000\)
belongs to Round 31, while \(q=999.5\) is included here.

## 1. Dependencies

Only the following proved inputs are used:

- the Round 30 reduction
  \(\Psi^{L_T}_{4,E}>\mathfrak F\), its included-shelf condition
  \[
   G_{K_3}(q-m)-G_q(q-m)\ge\frac74,
  \tag{1.1}
  \]
  and the exact inherited grids;
- the Round 31 inequalities \(\mathfrak F>L_q\), strict positivity of
  \(A,B,d\), the no-interior-minimum theorem for \(L_q\), strict convexity
  of its three boundary profiles, and the real \(q\ge1000\) exclusion;
- the defining identity \(G_{K_3}(q+3)=3/4\); and
- elementary Taylor inequalities for \(\tan,\sin,\cos\), together with
  monotonicity of \(\sin u/u\) on \((0,\pi)\).

No shell-ratio threshold, owner partition, floating-point diagnostic, or
earlier fragmented certificate is a dependency.

## 2. Uniform angle bounds for \(q\ge35\)

Write \(\theta=\theta_3\), so

\[
 \tan\theta-\theta=\frac{3\pi}{4(q+3)},
 \qquad
 K_3=\frac{q+3}{\cos\theta}.
\tag{2.1}
\]

### 2.1 The bounds \(\theta<219/400\) and \(\psi<2/3\)

Since \(q\ge35\) and \(\pi<22/7\),

\[
 \frac{3\pi}{4(q+3)}\le\frac{3\pi}{152}<\frac{33}{532}.
\]

Every omitted coefficient in the Taylor series of \(\tan x-x\) is
positive on this interval.  At \(x_0=219/400\),

\[
 \frac{x_0^3}{3}+\frac{2x_0^5}{15}
 +\frac{17x_0^7}{315}-\frac{33}{532}
 =
 \frac{4764574458554919}
 {155648000000000000000}>0.
\tag{2.2}
\]

Hence

\[
 \boxed{\theta<\frac{219}{400}<\frac{11}{20}.}
\tag{2.3}
\]

Moreover,

\[
 \cos\psi=\frac{q\cos\theta}{q+3}
 >\frac{35}{38}\cos\frac{219}{400}.
\]

The alternating cosine bounds, lower through the negative sixth-order
term on the left and upper through the positive fourth-order term on the
right, give

\[
 \begin{aligned}
 &\frac{35}{38}
 \left(1-\frac{x_0^2}{2}+\frac{x_0^4}{24}
             -\frac{x_0^6}{720}\right)\\
 &\qquad-
 \left(1-\frac{(2/3)^2}{2}+\frac{(2/3)^4}{24}\right)
 =\frac{249713778018875291}
 {605159424000000000000}>0.
 \end{aligned}
\tag{2.4}
\]

Thus \(\cos\psi>\cos(2/3)\), and

\[
 \boxed{\psi<\frac23.}
\tag{2.5}
\]

### 2.2 The cubic bound \(q\psi^3<13\)

Put \(c=49/40\).  Equation (2.1) gives the exact identity

\[
 \cos\psi
 =\cos\theta-\frac4\pi
   (\sin\theta-\theta\cos\theta).
\tag{2.6}
\]

Also

\[
 \sin\theta-\theta\cos\theta
 =\int_0^\theta u\sin u\,du<\frac{\theta^3}{3}.
\tag{2.7}
\]

Since \(c\theta<1\) and \(\sin u>u-u^3/6\) on this interval,

\[
 \begin{aligned}
 \cos\theta-\cos(c\theta)
 &=\int_\theta^{c\theta}\sin u\,du\\
 &>\int_\theta^{c\theta}\left(u-\frac{u^3}{6}\right)du\\
 &=\frac{c^2-1}{2}\theta^2
  -\frac{c^4-1}{24}\theta^4.
 \end{aligned}
\tag{2.8}
\]

Using \(\pi>333/106\), (2.3), and

\[
 \frac{c^2-1}{2}
 -\frac{c^4-1}{24}\left(\frac{11}{20}\right)^2
 -\frac{424}{999}\frac{11}{20}
 =\frac{9003993307}{8183808000000}>0,
\tag{2.9}
\]

equations (2.7)--(2.9) show

\[
 \cos\theta-\cos(c\theta)
 >\frac4\pi(\sin\theta-\theta\cos\theta).
\]

By (2.6), \(\cos\psi>\cos(c\theta)\), hence

\[
 \psi<c\theta.
\tag{2.10}
\]

Finally, \(\tan\theta-\theta>\theta^3/3\), so

\[
 q\psi^3
 <c^3\frac{9\pi q}{4(q+3)}
 <c^3\frac{99}{14}
 =13-\frac{107}{128000}.
\]

Therefore

\[
 \boxed{q\psi^3<13.}
\tag{2.11}
\]

## 3. Self-improving the shelf bound

For \(0<z<q\), define

\[
 h(z)=\arccos\frac z{K_3}-\arccos\frac zq.
\tag{3.1}
\]

Direct differentiation gives

\[
 h'(z)=\frac1{\sqrt{q^2-z^2}}
       -\frac1{\sqrt{K_3^2-z^2}}>0,
\]

\[
 h''(z)=z\left\{(q^2-z^2)^{-3/2}
                -(K_3^2-z^2)^{-3/2}\right}>0.
\tag{3.2}
\]

Thus \(h\) is strictly increasing and strictly convex, with
\(h(q)=\psi\).

The elementary phase upper bound already used in Round 31 is

\[
 G_{K_3}(q-m)-G_q(q-m)
 <\frac34+\frac{(m+3)\psi}{\pi}.
\tag{3.3}
\]

Combining (3.3) with (1.1) first gives

\[
 m>y:=\frac\pi\psi-3.
\tag{3.4}
\]

Notice from (2.5) that \(y>0\); feasibility and \(m<q\) give
\(0<y<q\).

We next prove

\[
 \boxed{h(q-y)<\frac{2\psi}{3}.}
\tag{3.5}
\]

Put

\[
 \alpha=\arccos\left(1-\frac yq\right),\qquad
 \beta=\arccos\frac{q-y}{K_3}.
\]

Then \(h(q-y)=\beta-\alpha\) and
\(\cos\beta=\cos\alpha\cos\psi\).  If
\(\alpha+2\psi/3\ge\pi/2\), (3.5) is immediate because
\(\beta<\pi/2\).  Otherwise it is equivalent to

\[
 \tan\alpha>
 R:=\frac{\cos(2\psi/3)-\cos\psi}{\sin(2\psi/3)}.
\tag{3.6}
\]

The product-to-sum identity and strict decrease of \(\sin u/u\) give

\[
 \begin{aligned}
 R
 &=\frac{2\sin(5\psi/6)\sin(\psi/6)}{\sin(2\psi/3)}\\
 &<\frac\psi3\frac{\sin(5\psi/6)}{\sin(2\psi/3)}
 <\frac{5\psi}{12}.
 \end{aligned}
\tag{3.7}
\]

On the other hand,

\[
 \tan^2\alpha
 =\frac{y(2q-y)}{(q-y)^2}>\frac{2y}{q}.
\tag{3.8}
\]

The last inequality follows after clearing denominators from
\(y<q\).  Equations (2.5), (2.11), and \(\pi>333/106\) yield

\[
 q\psi^3<13
 <\frac{288}{25}\left(\frac{333}{106}-2\right)
 <\frac{288}{25}(\pi-3\psi),
\tag{3.9}
\]

where the first strict comparison has exact margin

\[
 \frac{288}{25}\left(\frac{333}{106}-2\right)-13
 =\frac{199}{1325}>0.
\]

Since \(y=(\pi-3\psi)/\psi\), (3.9) is equivalent to

\[
 \frac{2y}{q}>\left(\frac{5\psi}{12}\right)^2.
\]

Together with (3.7)--(3.8), this proves (3.5).

Now put \(x=q-m\).  By (3.4), \(x<q-y\), and hence

\[
 h(x)<\frac{2\psi}{3}.
\tag{3.10}
\]

The exact action decomposition is

\[
 \begin{aligned}
 G_{K_3}(x)-G_q(x)
 =\frac34+\frac1\pi\bigg{&
 \int_q^{q+3}\arccos\frac z{K_3}\,dz\\
 &+\int_x^q h(z)\,dz\bigg\}.
 \end{aligned}
\tag{3.11}
\]

The outer integral is strictly smaller than \(3\psi\).  Convexity of
\(h\) and the trapezoid inequality give

\[
 \int_x^q h(z)\,dz
 \le\frac m2\{h(x)+h(q)\}<\frac{5m\psi}{6}.
\tag{3.12}
\]

Consequently

\[
 G_{K_3}(q-m)-G_q(q-m)
 <\frac34+\frac\psi\pi\left(3+\frac{5m}{6}\right).
\tag{3.13}
\]

Combining (3.13) with the non-strict shelf condition (1.1) proves the
strict bootstrap (0.5).

## 4. Reduction to the shelf-truncated triangle

The variable \(m\) is an integer.  Thus (0.5) gives

\[
 m\ge m_\sharp(q),\qquad q\ge35.
\tag{4.1}
\]

For \(q<35\) we make no such assertion and retain only \(m\ge1\).  This
is exactly the piecewise boundary (0.4).

For fixed \(q\), consider the compact triangle

\[
 p\ge1,qquad r=x-p\ge r_0,qquad m=q-x\ge m_0(q).
\tag{4.2}
\]

The Round 31 Hessian calculation applies unchanged to every subtriangle:
an interior critical point of \(L_q\) is a saddle, so no interior point is
a minimum.  The three boundary edges are

\[
 p=1,qquad r=r_0,qquad m=m_0(q).
\tag{4.3}
\]

The first is immediate from (0.1): here \(x\ge1+r_0\), so every
curvature factor is positive; moreover \(A,B,d,m>0\).  Hence

\[
 L_q(1,x)>\frac7{10}-\frac12=\frac15.
\tag{4.4}
\]

Round 31 proves strict convexity of each of the other two one-variable
edge profiles.  The remaining task is therefore exactly two continuous
convex minimum checks for each of 1994 values of \(q\), not a scan of
integer \(p\)-samples.

## 5. The one compact finite certificate

The sole load-bearing numerical artifact is

```text
computations/general_d_round32_truncated_Lq_certificate.py
```

It uses python-flint Arb 0.8.0 at 192-bit precision and does the following.

1. It represents \(2q\), the parity-dependent \(r_0\), all interval
   endpoints, and every bisection midpoint exactly as integers or dyadic
   rationals.
2. For each \(q\), it encloses \(\theta_2,\theta_3\) by 100 exact dyadic
   bisections of the strictly increasing function
   \(\tan\theta-\theta\).  All transcendental evaluations are outward Arb
   balls.
3. For \(q\ge35\), it evaluates (0.3) as an Arb ball.  The call
   `unique_fmpz` succeeds only when the floor is uniquely certified, so
   every transition of \(m_\sharp\) is proved rather than guessed.
4. On each of the \(r=r_0\) and \(m=m_0(q)\) edges, it uses the proved
   strict convexity and 70 exact dyadic bisections of the derivative to
   enclose the unique stationary point, or proves that the minimum is an
   endpoint.  It then evaluates \(L_q\) on the entire root ball.
5. It checks every nontrivial edge enclosure against the rational margin
   \(1/100\).  Fixed loop bounds and a final coverage assertion prove
   finite termination and complete coverage.

The exact domain is

\[
 2q=6,7,\ldots,1999,
\]

with even \(2q\) assigned \(r_0=1\) and odd \(2q\) assigned
\(r_0=3/2\).  The replay reports

```text
qCount=1994
certifiedEdgeCount=3988
pEqualsOneAnalyticLowerBound=1/5
certifiedNontrivialEdgeMargin=1/100
round32TruncatedLqCertificateOK=True
```

Thus every edge in (4.3), and hence the whole triangle (4.2), satisfies
\(L_q>0\).  This proves (0.6).

The symbolic non-load-bearing replay

```text
computations/general_d_round32_shelf_bootstrap_replay.wl
```

checks the five rational margins in Sections 2--3, both derivatives in
(3.2), and both edge-derivative formulas used by the certificate.  On
Mathematica 15.0 it returns

```text
round32DerivativeResiduals={0,0,0,0}
round32ShelfBootstrapReplayOK=True
```

## 6. Closure of the retained lower shelf

Let a Round 30 included lower-shelf point survive the automatic sector.

- If \(q\ge1000\), Round 31 proves that the exact necessary shelf/hard
  domain is empty.
- If \(35\le q<1000\), (0.5) places the point in (4.2), and Section 5
  gives \(L_q>0\).
- If \(3\le q<35\), Section 5 covers the full untruncated triangle with
  \(m_0=1\).

Round 31 gives \(\mathfrak F>L_q\), and Round 30 gives
\(\Psi^{L_T}_{4,E}>\mathfrak F\).  Therefore

\[
 \boxed{\Psi^{L_T}_{4,E}>\mathfrak F>L_q>0}
\tag{6.1}
\]

throughout the finite retained shelf, while the real large-\(q\) part is
empty.  The Round 30 included retained-\(E\) lower shelf is closed on both
inherited grids.

## 7. Equality-face audit

1. **Shelf equality.**  Condition (1.1) is non-strict.  Both phase upper
   bounds in (3.13) are strict, so (0.5) remains strict even when the
   shelf action equals \(7/4\).
2. **Integer floor walls.**  The convention
   \(A(r+j)+1/4\in\mathbb N\) is inherited unchanged from Round 30.  This
   note starts on the included lower shelf and uses continuous lower
   bounds, so it neither deletes nor duplicates the equality wall.
3. **Hard walls.**  Equality at \(p=dm\) or
   \(E_{\min}=1/2-dm/(2p)\) has the earlier automatic owner.  The retained
   argument uses the strict hard complement.
4. **Interface and turning walls.**  Equalities \(r+j=\mu\) and
   \(r+j=K\) retain the complete one-interface and turning/zero-tail
   owners.  No continuation across either wall is used here.
5. **Integral interface \(\mu-r\in\mathbb N\).**  The included-shelf
   intersection on the \(\alpha=0\) face is covered by (6.1).  Other
   \(\alpha=0\) endpoint families remain outside this theorem.
6. **Parity and cutoff walls.**  There is no interpolation between grids.
   The certificate ends at \(q=999.5\); Round 31 includes every real
   \(q\ge1000\).  The endpoint \(q=35\) is included in the analytic
   bootstrap and in the finite certificate.
7. **Triangle boundaries.**  The literal lower radii \(r_0=1,3/2\) and
   the integer boundary \(m=m_0(q)\) are certified.  No artificial
   extension to \(r=0\) or \(r=1/2\) is made.

## 8. Loss ledger

- Equation (3.3) initially discards the variation of both phase
  integrands.  It is used only to obtain the necessary first bootstrap
  \(m>y\).
- Equations (2.2)--(2.11) replace exact angles by adverse rational bounds.
  They are used only to prove the shape estimate (3.5).
- In (3.12), convexity replaces the exact integral by its endpoint
  trapezoid and discards the strict convexity gap.  Enough remains to
  strengthen the necessary integer lower bound on \(m\).
- The finite implication \(\mathfrak F>L_q\) discards
  \(T(q)-7/10\) and the positive remainder
  \(E_{\min}-\mathcal K_{4,\min}\).  It is used only below \(q=1000\),
  after shelf feasibility has removed the spurious small-\(m\) edge.
- The certificate proves the stronger rational margin \(L_q>1/100\) on
  the two nontrivial finite edges.  No floating approximation is used as
  a premise.
- For \(q\ge1000\), the exact retained-\(E\) Round 31 implication is kept;
  the weaker scalar \(L_q\) is not extrapolated asymptotically.

No shell-ratio partition or new owner seam is introduced.

## 9. Counterexample search and scope regression

The full untruncated \(m=1\) edge of \(L_q\) is genuinely false.  For
example, high-precision evaluation gives

\[
 L_{79/2}(4,77/2)<0,
 \qquad
 L_{40}(4,39)<0.
\tag{9.1}
\]

In \((q,r,p,m)\) coordinates these are respectively
\((79/2,69/2,4,1)\) and \((40,35,4,1)\).  They are outside the
shelf-truncated domain: (0.5) forces \(m\ge3\) there.  These witnesses are
kept as scope regressions preventing any future claim that the Round 31
full-triangle \(m=1\) edge is positive.

Before certification, a floating design sweep predicted that the tight
truncated edge would occur near the upper cutoff.  The directed replay
confirms a global enclosure above \(0.0133\) at \(q=999.5,m=15\), but the
proof premise is only the printed rational margin \(1/100\), not that
decimal diagnostic.

No counterexample to the retained shelf was found.  This statement is not
used in the proof; closure is supplied by Sections 2--6.

## 10. Failure report and gate decision

The retained lower shelf is no longer a blocker.  Full high-floor CST is
still open because the Round 30 theorem did not reduce all endpoint
families to this shelf.  The live obligation remains

\[
 D_A(q)+R_p+\frac{d_\rho}{2}(n-p)\ge0
\tag{10.1}
\]

on the lower-\(Q\) hard arc, \(\alpha\)-to-one faces, small
\(\alpha=0\) phases outside the included shelf, other inverse bands,
hard-sector seams, and simultaneous inverse/outer-\(B\) endpoints not
already owned by Rounds 29--30.  No sign theorem for those faces is claimed
here.

The gate decision is to accept the single compact certificate in Section
5 as the last fallback for this compact retained-shelf remainder, then
return to analytic endpoint closure.  A second overlapping certificate or
a shell-ratio ladder is not authorized.  If the remaining endpoint family
does not yield to one correlated analytic theorem, the next route is the
weighted aggregate, not another pointwise owner partition.

The live research graph still contains a legacy certificate-backed
first-floor first-drop owner.  Before final assembly, that legacy check must
either be replaced analytically or folded together with Section 5 into one
consolidated verification artifact.  Round 32 does not authorize two
separate certificates in the final implication chain.

## 11. Reproduction

From the repository root:

```powershell
wolframscript -file computations/general_d_round32_shelf_bootstrap_replay.wl
python -B computations/general_d_round32_truncated_Lq_certificate.py
```
