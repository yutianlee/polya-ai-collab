# Targeted adversarial referee: the clean-room constant \(C=125/8\)

## Verdict

**PASS.**  The clean-room argument proves the claimed high-thin range

$$
0<\varepsilon\le \frac1{100},\qquad
K\ge \frac{125}{8\varepsilon^2}
$$

from the unconditional Round 3 shifted-tail decomposition and global
plateau ceiling.  In particular, equations (25)--(32) are self-consistent:
the comparison path preserves every estimate used to bound its derivative,
the endpoint \(P=r=361/80\) is the genuine no-drop geometry, and the final
gain exceeds the complete interface allowance with the stated strict
rational margin.

**First unsupported implication:** none.

I did not inspect the Round 9 \(C=18\) incumbent or its constant-check
artifact.  I reconstructed the candidate from
`thin-plateau-optimized-clean-room.md`, the frozen Round 3 low-interface
packet and reviews, the weighted-tail scaffold, the source-card statements
of the FLPS floor theorems, and the already-audited pre-Round-9 thin-shell
dependencies.

During review the report used \(q=x_0+n\) for the dimensionful interface
mesh point and reused \(q\) in (13) for a dimensionless upper bound on
\(w\).  The latter has now been renamed \(\widehat q\) in the reviewed
report and frozen packet.  The two meanings were not mixed in any
inequality, so this was editorial only.

## 1. Frozen decomposition and the only dangerous branch

The Round 3 input is exactly

$$
\frac{\mathcal T_r}{2}
\le \int_{x_0}^{K}A(z)\,dz+\delta-\frac M4,
\qquad
0\le\delta<\frac{2\sqrt2}{15},
$$

$$
M=L+dm-p,\qquad L=\lfloor K\eta\rfloor,
\qquad m=n-p.
$$

Thus, with \(R=p-dm\), one has the exact identity \(M=L-R\).  If
\(R\le0\), the action gain alone closes the tail.  If \(R>0\), then
\(p>0\), and \(d>9/10\) gives

$$
m<\frac p d<\frac{10}{9}p,
\qquad
U=n+\beta=p+m+\beta<1+\frac{19}{9}p.
$$

This includes the no-drop case \(p=n>0\), where \(m=0\) and \(R=p\).
The Round 3 global estimate

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}
$$

is unconditional and was proved before any \(K\ge64\varepsilon^{-2}\)
specialization.  Its use here is therefore non-circular.

## 2. Scaled location and the bound \(\widehat q<1/7\)

Put

$$
y=\sqrt\varepsilon,\qquad \kappa=Ky^4,
\qquad P=py,\qquad \mathfrak r=Ry,
\qquad S=(p+m)y.
$$

Then

$$
P-\mathfrak r=dmy,
\qquad
S=P+\frac{P-\mathfrak r}{d}.
$$

Since \(w=U/\mu\), the strict inequality \(U<1+p+m\) gives

$$
w<\widehat q
:=\frac{y^4+y^3S}{\kappa\rho}.
$$

In the dangerous branch, the global plateau ceiling becomes

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Consequently

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac{19}{9}y\sqrt{\frac{2\pi}{\kappa\rho}}.
$$

For \(y\le1/10\), \(\rho=1-y^2\ge99/100\), and
\(\kappa\ge125/8\), the two estimates used in the clean-room report are
exact:

$$
\frac{y^4}{\kappa\rho}
\le\frac{8}{1237500}<\frac1{1000},
$$

$$
\left(y\sqrt{\frac{2\pi}{\kappa\rho}}\right)^2
\le\frac{352}{86625}<\frac1{225}.
$$

Hence

$$
\widehat q<\frac1{1000}+\frac{19}{135}<\frac17.
$$

It follows that \(t=x_0/\mu=1-w>1-\widehat q>6/7\).  No old
\(C=64\) location estimate or old \(p=O(\varepsilon^{-1/2})\) conclusion
has entered.

## 3. Reconstruction of the plateau inequality (25)

At \(x_0=\mu t\),

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
\ge \frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
$$

Also

$$
1-\rho^2t^2
\le2\left(\varepsilon+\frac UK\right),
$$

and, with

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
$$

one has the strict bound

$$
\varepsilon+\frac UK<y^2Q.
$$

Moreover

$$
\widehat q=\frac{y^2}{\rho}(Q-1).
$$

The equal ordinary floors at the ends of the initial plateau imply

$$
A(x_0)-A(x_0+p)<1
$$

even when either endpoint lies on a floor wall.  Since \(\sigma\) is
increasing and \(p>0\) in the dangerous branch,

$$
1>\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0)
>\frac{P(1-\widehat q)}{\pi\sqrt{2Q}}.
$$

Squaring positive quantities gives exactly

$$
P^2<H(P,\mathfrak r)
:=\frac{2\pi^2Q}{(1-\widehat q)^2}.
$$

All strict signs survive threshold equality.

## 4. Monotonicity in \(\mathfrak r\) and the synthetic path

For fixed \(y,\kappa,d\), write \(a=y^2/\rho\).  Then

$$
\widehat q=a(Q-1),
\qquad
Q=1+\frac{y^2}{\kappa}
+\frac y\kappa\left(P+\frac{P-\mathfrak r}{d}\right).
$$

The derivative of \(Q\mapsto Q/(1-a(Q-1))^2\) is positive, while
\(\partial Q/\partial\mathfrak r=-y/(\kappa d)<0\).  Therefore
\(H\) is strictly decreasing in \(\mathfrak r\), as claimed.

At fixed \(\mathfrak r\), direct differentiation gives

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q}{\partial P}
\frac{1+\widehat q+2a}{(1-\widehat q)^3},
$$

$$
\frac{\partial Q}{\partial P}
=\frac y\kappa\left(1+\frac1d\right)
<\frac{76}{5625}.
$$

Using \(a\le1/99\), \(\widehat q<1/7\), and \(\pi<22/7\) gives

$$
\frac{\partial H}{\partial P}
<\frac{673816}{1366875}<\frac12.
$$

The potentially delicate point is whether this derivative estimate remains
valid along the artificial segment

$$
(P',\mathfrak r)=(P',B_*),
\qquad B_*:=\frac{361}{80},
\qquad B_*\le P'\le P.
$$

It does.  The actual global ceiling gives

$$
P'\le P<\frac{\sqrt{2\pi\rho\kappa}}{y^2},
$$

while

$$
S(P',B_*)
=P'+\frac{P'-B_*}{d}
<\frac{19}{9}P'.
$$

Thus the same calculation proves \(\widehat q(P',B_*)<1/7\) at every
point of the path.  No integrality of the synthetic value of \(m\) is
needed; the path is used only to compare the smooth function \(H\).

If \(\mathfrak r\ge B_*\), then \(P\ge\mathfrak r\ge B_*\) and

$$
P^2-H(P,\mathfrak r)
\ge P^2-H(P,B_*).
$$

The derivative of the expression on the right along the path is

$$
2P'-\frac{\partial H}{\partial P}(P',B_*)
>2B_*-\frac12>0.
$$

It is therefore minimized at \(P'=B_*\).  This justifies (30) without a
hidden loss of the global ceiling or the \(\widehat q<1/7\) hypothesis.

## 5. Why the no-drop geometry is extremal

At \(P=\mathfrak r=B_*\),

$$
P-\mathfrak r=dmy=0,
$$

so \(m=0\) and \(S=B_*\).  This is exactly the no-drop geometry, not an
unattainable relaxation.

At that point

$$
Q=1+\frac{y^2+yB_*}{\kappa},
$$

which increases with \(y\) and decreases with \(\kappa\).  Also

$$
\widehat q
=\frac{y^2}{1-y^2}\frac{y^2+yB_*}{\kappa},
$$

which has the same endpoint monotonicity.  Their simultaneous maxima are
therefore at \(y=1/10\), \(\kappa=125/8\), giving

$$
Q_* = \frac{12869}{12500},
\qquad
\widehat q_* = \frac{41}{137500}.
$$

The exact endpoint calculation is correct:

$$
B_*^2
-2\left(\frac{22}{7}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=\frac{72581986185449}{5925464687161600}>0.
$$

Since the displayed expression already uses an upper bound for \(H\), it
implies \(B_*^2-H(B_*,B_*)>0\).  This contradicts (25) under the assumption
\(\mathfrak r\ge B_*\), and hence

$$
\mathfrak r<B_*,
\qquad
R<\frac{361}{80\sqrt\varepsilon}.
$$

This establishes the claimed extremality statement in the precise sense
needed by the proof.

## 6. Tight final margin

The action bound gives

$$
K\eta\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
$$

At \(\kappa=125/8\), the rational bounds in the report yield the strict
coefficient estimate

$$
\frac{2\sqrt2\,\kappa}{3\pi}
\ge\frac{125\sqrt2}{12\pi}
>\frac{2187500}{466587}.
$$

Thus, on the dangerous branch,

$$
M=L-R
>\left(\frac{2187500}{466587}-\frac{361}{80}\right)\frac1y-1.
$$

The coefficient difference is positive and \(y\le1/10\), so

$$
M>\frac{2829397}{3732696}.
$$

Meanwhile

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175},
$$

and the final exact margin is

$$
\frac{2829397}{3732696}-\frac{132}{175}
=\frac{2428603}{653221800}>0.
$$

The margin is small but genuinely strict.  It does not rely on
\(K>125/(8\varepsilon^2)\), \(\varepsilon<1/100\), or avoidance of a
gain-floor wall.

For \(R\le0\), one instead has \(M\ge L\), and the action gain is far
larger than one, so that branch closes independently of the plateau
comparison.

## 7. Exceptional branches and walls

1. **\(n=0\).**  The frozen convention gives \(p=m=R=0\) and \(M=L\).
   No slope estimate or degenerate concave theorem is used.
2. **\(p=0\).**  Then \(R=-dm\le0\), so this is an easy branch.
3. **No drop, \(p=n>0\).**  Then \(m=0\), \(R=p\), and it lies in the
   dangerous analysis.  It is exactly the endpoint geometry in the
   comparison argument.
4. **Ordinary-floor walls.**  Equal ordinary floors force a strict
   difference smaller than one even when either sampled value is integral.
5. **Interface wall \(x_0+n=\mu\).**  Here \(\beta=0\) and \(\delta=0\).
   Also \(U=p+m<1+p+m\), so the strict scaled location bound persists.
6. **Gain wall \(K\eta\in\mathbb Z\).**  The universal inequality
   \(\lfloor K\eta\rfloor>K\eta-1\) remains strict.
7. **Threshold equality.**  \(\kappa=125/8\) is used explicitly in the
   endpoint majorants, and the positive rational margins retain strictness.
8. **\(\varepsilon=1/100\).**  This is the simultaneous worst endpoint
   for the location and endpoint comparison; it was included above.
9. **Strict spectral walls.**  The new argument changes only the
   ordinary-floor shifted-tail majorant.  The already-audited strict phase
   proxy remains pointwise no larger, including when its majorant is an
   integer.

## 8. Enlarged overlap

The aggregate-action component includes

$$
0\le K\le\frac1{8\varepsilon^{5/2}},
$$

while the present high-thin component includes

$$
K\ge\frac{125}{8\varepsilon^2}.
$$

The ranges meet if and only if

$$
125\sqrt\varepsilon\le1,
$$

so the enlarged endpoint is exactly

$$
\varepsilon=\frac1{15625}=\frac1{125^2}.
$$

At equality, both thresholds are

$$
K=\frac{125^5}{8}.
$$

Both component theorems include their endpoints.  Hence there is neither a
floor-wall exception nor an open-interval gap at the new interface.

## Final referee conclusion

The constant \(C=125/8\) and the endpoint
\(\varepsilon=1/15625\) pass this targeted adversarial audit.  Promotion
retains the exact Round 3 dependency boundary.  The dimensionless quantity
in (13) has been renamed \(\widehat q\); no mathematical repair was needed.
