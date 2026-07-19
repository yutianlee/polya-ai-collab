# Round 9 clean-room reconstruction: optimized thin local plateau

## Verdict

**PASS with the simple exact constant**

$$
\boxed{C_{\rm cr}=\frac{125}{8}.}
$$

More precisely, let

$$
\rho=1-\varepsilon,
\qquad
0<\varepsilon\le\frac1{100}.
$$

Using only the audited Round 3 shifted-tail decomposition and its
unconditional global plateau estimate, I independently obtain

$$
\boxed{
K\ge\frac{125}{8\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

No estimate proved under the old hypothesis
$K\ge64\varepsilon^{-2}$ is imported.  In particular, the old conclusion
$p<8/\sqrt\varepsilon$ is not used.

The key point is to estimate the actual uncompensated interface loss

$$
R=p-dm,
$$

rather than first estimating $p$ and then discarding the positive term
$dm$.  A scaled monotonicity argument shows that the largest possible $R$
occurs in the no-drop geometry $m=0$.  It gives the exact rational bound

$$
\boxed{R<\frac{361}{80\sqrt\varepsilon}.}
\tag{2}
$$

The gain $\lfloor K G_1(1-\varepsilon)\rfloor$ then pays for (2), the full
possible floor loss, and the interface remainder with a strict margin.

The new overlap endpoint is

$$
\boxed{
\varepsilon_{\rm new}
=\left(\frac1{8C_{\rm cr}}\right)^2
=\frac1{15625}.
}
\tag{3}
$$

At equality, both analytic thresholds are exactly $K=125^5/8$.

This report did not inspect any Round 9 incumbent response.

## 1. Frozen shifted-tail input

Put

$$
\mu=\rho K,
\qquad
A=G_K-G_\mu,
\qquad
c=\frac{\arccos\rho}{\pi},
\qquad
d=1-2c,
\qquad
\eta=G_1(\rho).
$$

For a low-interface shifted tail beginning at
$x_0=r+1/2<\mu$, write

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
q=x_0+n,
\qquad
\beta=\mu-q\in[0,1).
$$

Let $p$ be the last index in the initial constant ordinary-floor plateau,
with $p=n$ when there is no drop, and set

$$
m=n-p,
\qquad
U=\mu-x_0=n+\beta.
$$

The audited concave-head/convex-tail decomposition states

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^{K}A(z)\,dz
+\delta-\frac M4,
\tag{4}
$$

where

$$
0\le\delta<\frac{2\sqrt2}{15},
\qquad
M=L+dm-p,
\qquad
L=\lfloor K\eta\rfloor.
\tag{5}
$$

For $n=0$, the prescribed convention is $p=m=0$.  Independently of any
thin-shell threshold, the same audited input gives

$$
p<\sqrt{\frac{2\pi\rho K}{\varepsilon}}.
\tag{6}
$$

Define the genuine uncompensated loss

$$
R=p-dm.
\tag{7}
$$

Then $M=L-R$.  Thus the only potentially dangerous branch is $R>0$.

## 2. Exact parameterization of the old constant

Set

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2=Ky^4.
\tag{8}
$$

The hypothesis $K\ge C\varepsilon^{-2}$ is now exactly
$\kappa\ge C$.  Every former use of $64$ is retained through $\kappa$:

1. dangerous-plateau location: inverse powers of $K$ become inverse
   powers of $\kappa$;
2. local slope: the interface displacement is retained in a
   $\kappa$-dependent quantity $Q$;
3. plateau quadratic: it becomes the exact scaled inequality (25) below;
4. action gain:
   $K\eta\ge 2\sqrt2\,\kappa/(3\pi y)$;
5. final payment: the gain coefficient
   $2\sqrt2\,C/(3\pi)$ is compared directly with the scaled loss.

Only after these formulas are derived will $C=125/8$ be substituted.

## 3. A uniform bound for $d$ and the dangerous geometry

The elementary bounds

$$
3<\pi<\frac{1571}{500}<\frac{22}{7}<4
\tag{9}
$$

are sufficient below.  For completeness, the sharpened upper bound follows
from Machin's identity

$$
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}.
$$

The alternating arctangent series gives the finite rational certificate

$$
\begin{aligned}
\pi
&<16\left(
\frac15-\frac{1}{3\,5^3}+\frac{1}{5\,5^5}
-\frac{1}{7\,5^7}+\frac{1}{9\,5^9}
\right)\\
&\hspace{2cm}
-4\left(\frac1{239}-\frac{1}{3\,239^3}\right)\\
&=\frac{5277328977275528}{1679825970703125}
<\frac{1571}{500}.
\end{aligned}
$$

The last comparison has exact positive difference

$$
\frac{1571}{500}
-\frac{5277328977275528}{1679825970703125}
=\frac{2736890694763}{6719303882812500}>0.
$$

For completeness, if $a=\arctan(1/5)$ and
$b=\arctan(1/239)$, then

$$
\tan(2a)=\frac5{12},
\qquad
\tan(4a)=\frac{120}{119},
\qquad
\tan(4a-b)=1.
$$

Moreover $0<4a-b<\pi/2$, so $4a-b=\pi/4$.  This proves Machin's identity
without a decimal approximation to $\pi$.

The coarser bounds in (9) give a convenient exact estimate for $d$.  With
$u=\pi/40$, one has $3/40<u<1/10$, and

$$
\sin u>u-\frac{u^3}{6}
>\frac3{40}-\frac1{6000}
=\frac{449}{6000}
>\frac{71}{1000}.
$$

Consequently,

$$
1-\cos\frac\pi{20}
=2\sin^2\frac\pi{40}
>2\left(\frac{71}{1000}\right)^2
>\frac1{100}.
$$

Thus $\cos(\pi/20)<99/100\le\rho$, so

$$
c<\frac1{20},
\qquad
\boxed{d>\frac9{10}.}
\tag{10}
$$

Assume now that $R>0$.  Then $p>0$ and

$$
m<\frac p d<\frac{10}{9}p,
\qquad
U<1+p+m<1+\frac{19}{9}p.
\tag{11}
$$

This includes the no-drop case $p=n$, for which $m=0$.

## 4. Recomputed dangerous-plateau location for $C=125/8$

Define

$$
t=\frac{x_0}{\mu},
\qquad
w=1-t=\frac U\mu.
$$

For later use put

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
\tag{12}
$$

Since $\beta<1$,

$$
w
<\frac{1+p+m}{\rho K}
=\frac{y^4+y^3S}{\kappa\rho}
=:\widehat q.
\tag{13}
$$

In the dangerous branch, $S<19P/9$.  Equation (6) gives

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2}.
$$

Therefore, for $\kappa\ge125/8$, $y\le1/10$, and
$\rho\ge99/100$,

$$
\widehat q
<\frac{y^4}{\kappa\rho}
+\frac{19}{9}y\sqrt{\frac{2\pi}{\kappa\rho}}.
\tag{14}
$$

The first term is at most $8/1237500<1/1000$.  Moreover,

$$
\left(y\sqrt{\frac{2\pi}{\kappa\rho}}\right)^2
\le\frac{352}{86625}<\frac1{225}.
$$

It follows that

$$
\widehat q<\frac1{1000}+\frac{19}{135}<\frac17.
\tag{15}
$$

Thus

$$
\boxed{t>\frac67,}
\qquad
x_0=\rho Kt
>\frac{99}{100}\frac67K
>\frac K2.
\tag{16}
$$

This reconstructs, under $C=125/8$, the first dangerous-location claim that
previously used $C=64$.  Its only use below is to keep the exact
self-consistency denominator uniformly away from zero.

## 5. Exact local slope and the scaled plateau inequality

For $0<z<\mu$,

$$
\sigma(z):=-A'(z)
=\frac1\pi
\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
\tag{17}
$$

The function $\sigma$ is increasing.  At $x_0=\mu t$,

$$
\begin{aligned}
\sigma(x_0)
&=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}\\
&\ge
\frac{\varepsilon t}
{\pi\sqrt{1-\rho^2t^2}}.
\end{aligned}
\tag{18}
$$

Also,

$$
1-\rho t
=1-\frac{x_0}{K}
=\varepsilon+\frac UK,
$$

and hence

$$
1-\rho^2t^2
\le2\left(\varepsilon+\frac UK\right).
\tag{19}
$$

Introduce

$$
Q
=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa}.
\tag{20}
$$

Equations (13) and (20) satisfy the useful exact relation

$$
\widehat q=\frac{y^2}{\rho}(Q-1).
\tag{21}
$$

Since $U<1+p+m$,

$$
\varepsilon+\frac UK<y^2Q.
\tag{22}
$$

The plateau has the same ordinary floor at $x_0$ and $x_0+p$, so, including
at an ordinary-floor wall,

$$
A(x_0)-A(x_0+p)<1.
\tag{23}
$$

Because $\sigma$ is increasing,

$$
1>
\int_{x_0}^{x_0+p}\sigma(z)\,dz
\ge p\sigma(x_0).
\tag{24}
$$

Using $t>1-\widehat q$, (18), (19), and (22), and then squaring positive
quantities, gives the fully parameterized plateau inequality

$$
\boxed{
P^2< H(P,r)
:=\frac{2\pi^2 Q}{(1-\widehat q)^2}.
}
\tag{25}
$$

No bound obtained at $C=64$ has entered (25).

## 6. Bounding $R$, rather than $p$

From $R=p-dm$ one has

$$
P-r=dmy,
\qquad
S=P+\frac{P-r}{d}.
\tag{26}
$$

Fix $y$, $\kappa$, and $d$.  Then $H$ is decreasing in $r$.  Its derivative
with respect to $P$ is especially simple.  Put
$a=y^2/\rho$.  Since $\widehat q=a(Q-1)$,

$$
\frac{\partial H}{\partial P}
=2\pi^2\frac{\partial Q}{\partial P}
\frac{1+\widehat q+2a}{(1-\widehat q)^3}.
\tag{27}
$$

By (10), (15), and $\kappa\ge125/8$,

$$
\frac{\partial Q}{\partial P}
=\frac y\kappa\left(1+\frac1d\right)
<\frac{76}{5625},
\qquad
a\le\frac1{99}.
$$

Using $\pi<22/7$, direct rational simplification yields

$$
\frac{\partial H}{\partial P}
<
2\left(\frac{22}{7}\right)^2
\frac{76}{5625}
\frac{1+1/7+2/99}{(1-1/7)^3}
=\frac{673816}{1366875}
<\frac12.
\tag{28}
$$

Set

$$
B_*:=\frac{361}{80}.
\tag{29}
$$

Suppose for contradiction that $r\ge B_*$.  Then $P\ge r\ge B_*$, and,
because $H$ decreases in $r$,

$$
P^2-H(P,r)\ge P^2-H(P,B_*).
$$

Every intermediate $P'\in[B_*,P]$ still obeys the numerical global plateau
ceiling inherited from (6), and $S(P',B_*)<19P'/9$; hence the bound
$\widehat q<1/7$ used in (28) is valid along the whole comparison interval.
Therefore $P^2-H(P,B_*)$ is strictly increasing there, and

$$
P^2-H(P,r)
\ge B_*^2-H(B_*,B_*).
\tag{30}
$$

At $P=r=B_*$, equation (26) gives $S=B_*$ exactly: this is the no-drop
geometry $m=0$.  Both $Q$ and $\widehat q$ are largest when
$y=1/10$ and $\kappa=125/8$, where

$$
Q_*=\frac{12869}{12500},
\qquad
\widehat q_*=\frac{41}{137500}.
$$

The required endpoint check is exact:

$$
\begin{aligned}
B_*^2
&-
2\left(\frac{22}{7}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}\\
&=
\frac{72581986185449}{5925464687161600}
>0.
\end{aligned}
\tag{31}
$$

Thus (30) contradicts the strict plateau inequality (25).  We conclude

$$
r<B_*,
\qquad
\boxed{R<\frac{361}{80\sqrt\varepsilon}.}
\tag{32}
$$

Notice why the no-drop branch is safe rather than exceptional: when
$p=n$ and $p>0$, one has $m=0$, hence $P=r$ and $S=P$.  This is precisely
the endpoint geometry tested in (31).

## 7. The action gain pays the complete loss

The exact action representation and
$\arccos(1-v)\ge\sqrt{2v}$ give

$$
\eta
=\frac1\pi\int_0^\varepsilon\arccos(1-v)\,dv
\ge\frac{2\sqrt2}{3\pi}\varepsilon^{3/2}.
\tag{33}
$$

Therefore

$$
K\eta
\ge\frac{2\sqrt2\,\kappa}{3\pi y}.
\tag{34}
$$

The elementary bounds

$$
\frac{140}{99}<\sqrt2<\frac{99}{70},
\qquad
\pi<\frac{1571}{500}
$$

are exact because

$$
2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
\qquad
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0.
$$

They give,
for $\kappa\ge125/8$,

$$
\frac{2\sqrt2\,\kappa}{3\pi}
\ge\frac{125\sqrt2}{12\pi}
>\frac{2187500}{466587}.
\tag{35}
$$

On the dangerous branch, (32), (35), and
$\lfloor x\rfloor>x-1$ imply

$$
\begin{aligned}
M=L-R
&>K\eta-1-R\\
&>
\left(\frac{2187500}{466587}-\frac{361}{80}\right)
\frac1y-1\\
&=\frac{6562093}{37326960y}-1\\
&\ge\frac{2829397}{3732696}.
\end{aligned}
\tag{36}
$$

On the other hand,

$$
4\delta<\frac{8\sqrt2}{15}<\frac{132}{175}.
\tag{37}
$$

The remaining exact margin is

$$
\frac{2829397}{3732696}-\frac{132}{175}
=\frac{2428603}{653221800}>0.
$$

Thus $M>4\delta$.

If $R\le0$, then $M\ge L$ and, directly from (35),

$$
M>K\eta-1
>\frac{10\cdot2187500}{466587}-1
>1>4\delta.
$$

Thus this branch closes without any plateau argument.  Substitution in
(4) proves every low-interface shifted tail.

The already-proved high-interface shifted-tail theorem handles
$x_0\ge\mu$.  The audited multiplicity scaffold, strict phase proxy, and
exact separated spectral bridge then give (1).

## 8. Separate branch and wall audit

1. **Purely convex branch, $n=0$.**  The frozen convention is
   $p=m=0$, so $R=0$ and $M=L$.  Equation (35) closes directly; no local
   slope or division by $p$ occurs.

2. **Immediate drop, $p=0$.**  Here $R=-dm\le0$, so again $M\ge L$.
   The dangerous-plateau argument is not used.

3. **No floor drop, $p=n>0$.**  Here $m=0$ and $R=p$.  It is included
   explicitly in (25)--(32), and in fact supplies the extremal endpoint
   $P=r$ in (31).  No first-drop theorem is invoked.

4. **Other compensated branches.**  Whenever $p-dm\le0$, the convex gain
   alone closes.  When $p-dm>0$, all estimates use the exact $R$ rather
   than replacing it by a previously proved $C=64$ plateau bound.

5. **Ordinary-floor wall.**  Equality of the two plateau floors implies
   (23) strictly even when either sampled value is an integer.  A difference
   of exactly one cannot have equal ordinary floors.

6. **Interface wall, $q=\mu$.**  Then $\beta=0$ and $\delta=0$.
   The strict inequality $U<1+p+m$ remains true, so (13)--(32) remain
   valid with extra slack.

7. **Gain wall, $K\eta\in\mathbb Z$.**  Then $L=K\eta$, while the
   universal inequality $L>K\eta-1$ used in (36) is still strict.

8. **Threshold equality.**  The case
   $K=125/(8\varepsilon^2)$ is included: then $\kappa=125/8$.
   Strictness comes from the plateau relation, the
   rational inequalities, and $\lfloor x\rfloor>x-1$, not from increasing
   $K$ beyond the threshold.

9. **Strict spectral walls.**  The final step uses the already-audited
   strict phase proxy and exact spectral bridge.  This proof changes only
   the ordinary-floor tail majorant and never replaces a strict spectral
   inequality by a non-strict one.

10. **Parameter endpoint, $\varepsilon=1/100$.**  This is exactly the
    simultaneous worst endpoint used in (14), (15), and (31).  The final
    rational margins in (31) and (37) are positive there, so no limiting
    argument or open parameter interval is being used.

## 9. Exact enlarged endpoint overlap

The proved aggregate-action range ends at

$$
K\le\frac1{8\varepsilon^{5/2}},
$$

while (1) begins at $K\ge125/(8\varepsilon^2)$.  They overlap exactly when

$$
\frac{125}{8\varepsilon^2}
\le\frac1{8\varepsilon^{5/2}}
\quad\Longleftrightarrow\quad
125\sqrt\varepsilon\le1
\quad\Longleftrightarrow\quad
\varepsilon\le\frac1{125^2}.
$$

Thus (3) follows.  At
$\varepsilon=1/15625=1/125^2$,

$$
\frac{125}{8\varepsilon^2}
=\frac{125^5}{8},
$$

and

$$
\frac1{8\varepsilon^{5/2}}
=\frac{125^5}{8}.
$$

Both component ranges include equality, so there is no endpoint gap.  The
old endpoint $2^{-18}$ is enlarged by the exact factor
$262144/15625>16$ in $\varepsilon$, and the high-thin threshold is reduced
by the exact factor $512/125>4$ at every fixed $\varepsilon$.

## 10. Scope

The exact constant $125/8$ is the strongest simple constant obtained in this
clean-room reconstruction; no claim of global optimality is made.  The
proof establishes a self-consistent replacement for every use of $64$ and
an exact enlarged overlap.  It does not certify the remaining compact
region, alter the parent certification obligation, or claim the full shell
theorem before the independent Round 9 adversarial audit and state
promotion gates are complete.
