# Independent audit: Round 14 exact-head endpoint reduction

Date: 18 July 2026

Audited source:

`human/outbox/general-d-round-14-exact-head-endpoint-reduction.md`

Audited SHA-256:

`EC81BBE42152B682882509B034B37AB783FED9B46B429388B3D00CEF43900163`

Diagnostic evaluator replayed:

`computations/general_d_round14_exact_head_endpoint_probe.wl`

Evaluator SHA-256:

`4051788FDA83E7B7DF214BFB4075A5B5EE425D5A2093E4DDF27CA3119684218D`

## 1. Verdict

**PASS as an exact-head endpoint reduction.**

Every load-bearing statement in Proposition 1.1 checks:

1. the uniform bound \(L_{\rm ex}>1/12\) is valid on both new extension
   grids;
2. \(R_n=2\int_r^q(A_\alpha-1)\) is an exact identity, with no hidden
   shelf estimate;
3. S4 and the one-level fractional terminal theorem give
   \(D_{A_\alpha}(r)\geq\Xi(\alpha)\) with the exact cap;
4. both the exact head and the terminal cap move in the required direction,
   so \(\Xi\) is strictly decreasing;
5. the comparison with the first phase, branch, or activity endpoint has
   the correct strict direction;
6. the literal strict-bracket and ordinary-floor walls are owned correctly;
7. the loss ledger contains no remnant of the rejected pre-shelf surrogate;
   and
8. the supplied Mathematica replay reproduces the stated diagnostic count,
   minimum, and large-\(q\) values.

This verdict does **not** prove

\[
 \Xi_{\rm end}(\theta,y,n)\geq0.
\]

That inequality remains the selected open target, exactly as the source
states.  The seeded computation is falsification evidence only and does not
promote the first-floor branch or the general-dimensional theorem.

## 2. Scope and terminal variables

On the new grids,

\[
 r\in\mathbb N,\ r\geq1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\ r\geq\frac32,
\]

and \(n\geq1\).  Hence

\[
 q=r+n\geq2.
\]

For the strict level count \(B=[v+1/4]_< =1\), one has

\[
 \frac34<v\leq\frac74.
\]

Thus the outer action at \(q\) lies strictly above the inverse level
\(3/4\).  Since \(G_K\) decreases in its spatial argument, the inverse
point \(z\) satisfying \(G_K(z)=3/4\) obeys

\[
 z>q\geq2.
\]

In particular \(q<K\), \(0<\theta<\pi/2\), \(\beta>0\), and
\(y=z-q>0\).  The strict fraction

\[
 \eta=y-[y]_<\in(0,1]
\]

therefore has the required positive sign and takes the literal value \(1\)
at an integral inverse-spatial wall.

On the open phase, \((Q,\chi_q)=(1,0)\).  The one-level instance of T2 is
therefore exactly

\[
 L_{\rm ex}(\alpha)=
 \frac\pi{2\theta}+2\eta-1-2\delta(\alpha)
 +\frac{(v-1)_+^2}{\beta}.
\]

The adjective “exact” here correctly refers to retaining the exact cap
\(2\delta\) and the exact correlated head.  The terminal expression is
still a lower bound obtained by the audited inverse-level tangent theorem,
as the source and its loss ledger explicitly say.

## 3. Audit of the uniform bound \(L_{\rm ex}>1/12\)

Writing

\[
 \Phi(\theta)=\sin\theta-\theta\cos\theta,
\]

the inverse-level equation gives

\[
 K=\frac{3\pi}{4\Phi(\theta)},
 \qquad
 z(\theta)=\frac{3\pi\cos\theta}{4\Phi(\theta)}.
\]

Direct differentiation yields

\[
 \Phi'(\theta)=\theta\sin\theta
\]

and hence

\[
 \frac{d}{d\theta}\frac{\cos\theta}{\Phi(\theta)}
 =\frac{-\sin\theta\,\Phi(\theta)
       -\theta\sin\theta\cos\theta}{\Phi(\theta)^2}
 =-\frac{\sin^2\theta}{\Phi(\theta)^2}<0.
\]

At \(\theta_0=3\pi/8\), the condition \(z(\theta_0)<2\) reduces exactly
to

\[
 \tan\frac{3\pi}{8}=1+\sqrt2>\frac{3\pi}{4}.
\]

The rational comparisons in the note are sufficient:

\[
 1+\sqrt2>1+\frac{19}{14}=\frac{33}{14},
 \qquad
 \frac{3\pi}{4}<\frac34\frac{22}{7}=\frac{33}{14}.
\]

Since the active inverse point has \(z>2\), strict monotonicity gives

\[
 0<\theta<\frac{3\pi}{8},
 \qquad
 \frac\pi{2\theta}-1>\frac13.
\]

For

\[
 F(q)=G_{q+1}(q),
 \qquad
 \varphi=\arccos\frac{q}{q+1},
\]

direct differentiation gives

\[
 F'(q)=\frac{\sin\varphi-\varphi}{\pi}<0.
\]

All factors and signs in (2.4) are correct.  At \(q=2\),

\[
 F(2)=\frac{\sqrt5-2\arccos(2/3)}\pi.
\]

The source's exact bounds give

\[
 \sqrt5<\frac94,
 \qquad
 \cos\frac34\geq1-\frac{(3/4)^2}{2}
 =\frac{23}{32}>\frac23,
\]

so \(\arccos(2/3)>3/4\).  Therefore the numerator is less than
\(3/4\), and \(\pi>3\) proves \(F(2)<1/4\).  Since \(F\) decreases,

\[
 G_{q+1}(q)<\frac14
 \quad(q\geq2).
\]

T3 and monotonicity of the ball action in its radius give, for
\(0\leq\alpha\leq1\),

\[
 0\leq2\delta(\alpha)
 \leq\alpha G_{q+\alpha}(q)
 \leq G_{q+1}(q)<\frac14.
\]

Combining these estimates with \(2\eta>0\) and the nonnegative top square
gives precisely

\[
 L_{\rm ex}(\alpha)>\frac13-\frac14=\frac1{12}.
\]

Thus the raw T2 expression is positive and taking the maximum with the
separately proved one-interface bound \(0\) is unnecessary.

## 4. Exact head identity and S4

With \(\sigma=-A_\alpha'\), integration by parts gives

\[
 \begin{aligned}
 2\int_0^n u\sigma(r+u)\,du
 &=-2\int_0^n u\frac{d}{du}A_\alpha(r+u)\,du\\
 &=-2nA_\alpha(q)+2\int_r^qA_\alpha(s)\,ds.
 \end{aligned}
\]

Using \(A_\alpha(q)=3/4+\varepsilon\) in the exact no-drop remainder,

\[
 R_n=-\frac n2+2n\varepsilon
 +2\int_0^n u\sigma(r+u)\,du,
\]

one obtains

\[
 \begin{aligned}
 R_n
 &=-\frac n2+2n\varepsilon
   -2n\left(\frac34+\varepsilon\right)
   +2\int_r^qA_\alpha(s)\,ds\\
 &=2\int_r^q\bigl(A_\alpha(s)-1\bigr)\,ds
 =H_n(\alpha).
 \end{aligned}
\]

The constant \(-1\), factor \(2\), and cancellation of \(\varepsilon\)
are all correct.  This calculation is valid also at \(\alpha=0\): the ball
action and its first spatial derivative meet their zero extension at the
turning point, so the endpoint integration by parts creates no extra term.

In the open phase \(\chi_q=0\), exact S4 says

\[
 D_{A_\alpha}(r)=D_{A_\alpha}(q)+H_n(\alpha).
\]

T2 gives \(D_{A_\alpha}(q)\geq L_{\rm ex}(\alpha)\), and Section 3
shows that the raw lower expression is already positive.  Consequently

\[
 D_{A_\alpha}(r)
 \geq L_{\rm ex}(\alpha)+H_n(\alpha)
 =\Xi(\alpha).
\]

No curvature estimate, active-width relaxation, or pre-shelf surrogate is
used in this chain.

## 5. Monotonicity and endpoint comparison

For fixed \(s<a\), direct differentiation gives

\[
 \frac{\partial}{\partial a}G_a(s)
 =\frac{\sqrt{a^2-s^2}}{\pi a}>0.
\]

For every \(s\in[r,q)\), both radii \(q+\alpha\) lie above \(s\).
Therefore, if \(\alpha_2>\alpha_1\), then

\[
 A_{\alpha_2}(s)<A_{\alpha_1}(s)
 \quad(s\in[r,q)),
\]

and integration over an interval of length \(n>0\) proves

\[
 H_n(\alpha_2)<H_n(\alpha_1).
\]

The cap is also strictly increasing in the order sense.  On the old
interval \([q,q+\alpha_1]\), increasing the radius increases the action;
on the newly added interval, the larger ball action is nonnegative and
strictly positive away from its terminal endpoint.  This includes the case
\(\alpha_1=0\), where the new interval alone gives strict increase.  Hence

\[
 \delta(\alpha_2)>\delta(\alpha_1),
 \qquad
 L_{\rm ex}(\alpha_2)<L_{\rm ex}(\alpha_1).
\]

In particular \(\Xi=L_{\rm ex}+H_n\) is strictly decreasing on
\([0,1]\).  The source only needs the weaker observation that the terminal
part is nonincreasing because the head is already strictly decreasing.

At an original active open point,

\[
 \alpha<1,
 \qquad
 \varepsilon(\alpha)>0\Longrightarrow\alpha<\alpha_*,
 \qquad
 \text{strict activity}\Longrightarrow\alpha<\alpha_{\rm act}.
\]

Thus \(\alpha<\bar\alpha\).  Continuity and strict decrease give

\[
 \Xi(\alpha)>\Xi(\bar\alpha),
\]

even when the latter is a one-sided branch or activity-wall value.  Together
with the preceding S4 bound, this is exactly (1.11).  It is irrelevant that
the artificial motion may leave the original discrete shelf chamber: the
proof compares the explicit integral function and does not reapply S4 at
the artificial endpoint.

## 6. Literal walls and loss ledger

The wall treatment is complete and has the correct directions.

- At an ordinary-floor equality, the remainder is literally zero and the
  exact S4 identity remains valid.
- At \(q=\mu\), \(\alpha=0\) and the cap vanishes.
- A sample at \(K\) is absent under the strict bracket.
- At an integral inverse displacement, \(\eta=1\), not zero.
- At a lower noncorner action wall, \((Q,\chi_q)=(0,1)\).  Relative to the
  open-side scalar, T2 gains one unit from \(Q:1\mapsto0\), and S4 gains a
  second unit from \(\chi_q:0\mapsto1\).  The literal wall lower bound is
  therefore \(\Xi+2\), strictly more favorable.
- The branch and activity equalities are used only as limiting values.

The loss ledger is also accurate.  The only analytic terminal loss is the
nonnegative inverse-tangent gap already present in T2.  The exact head,
exact cap, fractional reserve, top square, and owner-dimensional endpoint
are retained.  The endpoint move discards the strictly positive gap
\(\Xi(\alpha)-\Xi(\bar\alpha)\), and using the open-side value at the
literal lower wall discards the two favorable unit jumps.  None of the
Round 11 pre-shelf losses survives.

## 7. Mathematica replay and large-\(q\) diagnostic

The supplied evaluator was replayed with Wolfram 15.0 for Windows.  It
reported

\[
 \#\{\text{hard extension-grid records}\}=3171,
 \qquad
 \#\{\Xi_{\rm end}<0\}=0,
\]

and the sampled minimum

\[
 \Xi_{\rm end}
 =0.13877007259120539297576415453166214848\ldots
\]

at the seeded small-grid record \(r=1,n=2,q=3\).  Its displayed split was

\[
 L_{\rm ex,end}=0.5293704887674103005\ldots,
 \qquad
 H_{n,{\rm end}}=-0.3906004161762049076\ldots.
\]

The script also printed `round14ReplayOK=True`.

The large-\(q\) record was independently recomputed from the defining ball
integrals at 110-digit working precision.  At

\[
 \theta=\frac{531}{4000},\quad q=3000,\quad n=51,\quad r=2949,
 \quad\alpha=\frac{999}{1000},
\]

the values are

\[
 \delta=0.00218584728275157868442022748792397238\ldots,
\]

\[
 L_{\rm ex}=11.31323686676273609255640989049605241663\ldots,
\]

\[
 H_n=29.90463863612766810150820977922656624471\ldots,
\]

and hence

\[
 \Xi=41.21787550289040419406461966972261866135\ldots.
\]

At its endpoint \(\bar\alpha=1\), the independent values are

\[
 L_{\rm ex,end}=11.31322591904948373463333413545661603299\ldots,
\]

\[
 H_{n,{\rm end}}=29.90055190755130856400941074776945219791\ldots,
\]

\[
 \Xi_{\rm end}=41.21377782660079229864274488322606823090\ldots.
\]

These reproduce both the rounded source values and the strict endpoint
decrease.  The same replay reproduces the rejected Round 11--12 endpoint
value \(-1.38778044667738\ldots\), the exact defect
\(45.24328925466225\ldots\), and the numerical S4 residual zero with about
58 digits of accuracy.

The seeded sweep is not interval arithmetic and covers only its generated
records.  The source explicitly states both limitations.  Its zero sampled
negative count and positive minimum are therefore diagnostic evidence, not
a proof of (1.12).  As optional diagnostic hardening, `round14ReplayOK`
could pin the displayed minimum to an expected tolerance; the present
predicate checks the record count, absence of sampled negatives, the
large-\(q\) classifications, S4 replay, and a positive Round 14 margin.
This does not affect any analytic statement.

## 8. Exact corrections and final disposition

No load-bearing correction is required.

One wording can be strengthened without changing the proof: the cap
\(\delta\) is strictly increasing on all of \([0,1]\) in the order sense,
including from \(\alpha=0\), even though its derivative at zero may vanish.
The source's weaker wording is sufficient because \(H_n\) is independently
strictly decreasing.

Final disposition:

- Extension-grid and terminal domain: **PASS**.
- Uniform bound \(L_{\rm ex}>1/12\): **PASS**.
- Exact identity \(R_n=H_n\): **PASS**.
- S4/T2 lower-bound chain: **PASS**.
- Monotonicity and endpoint comparison: **PASS**.
- Literal walls and loss ledger: **PASS**.
- Seeded Mathematica replay: **reproduced; PASS as diagnostic evidence**.
- Endpoint sign \(\Xi_{\rm end}\geq0\): **open and not promoted**.

No change was made to the audited Round-14 source.
