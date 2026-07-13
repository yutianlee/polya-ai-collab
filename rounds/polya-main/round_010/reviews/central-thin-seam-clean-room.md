# Round 10 clean-room reconstruction: central--thin seam

## Independence and verdict

The reviewer received only the frozen claim, definitions, and permitted
prior lemmas in
state/lemma_packets/SHELL-central-thin-seam-compression.md.  No Round 10
incumbent response, exploration note, computation, or peer output was
inspected.

**Verdict: PASS.**

The reconstruction uses constants different from the incumbent proof:

$$
\widehat q<\frac{13}{50},
\qquad
B_{\rm cr}=\frac{23}{5},
\qquad
R<\frac{23}{5\sqrt\varepsilon}.
$$

It independently proves

$$
\boxed{
0<\varepsilon\le\frac1{25},
\qquad
K\ge\frac{20}{\varepsilon^2}
\Longrightarrow
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
\tag{1}
$$

It also verifies the seam

$$
\rho_s=\frac{24}{25},
\qquad
K_0(24/25)<6000^2,
$$

and the global high-frequency ceiling $125^5/8$.

## 1. Frozen reduction

Put

$$
y=\sqrt\varepsilon,
\qquad
\kappa=K\varepsilon^2,
\qquad
\rho=1-y^2,
\qquad
\mu=\rho K.
$$

Then

$$
0<y\le\frac15,
\qquad
\kappa\ge20,
\qquad
\rho\ge\frac{24}{25}.
\tag{2}
$$

For a low shifted tail, use

$$
n=\lfloor\mu-x_0\rfloor,
\qquad
m=n-p,
\qquad
d=1-\frac2\pi\arccos\rho,
\qquad
R=p-dm.
$$

The permitted decomposition is

$$
\frac{\mathcal T_r}{2}
\le
\int_{x_0}^K A(z)\,dz+\delta-\frac M4,
\qquad
M=\lfloor K\eta\rfloor-R,
\qquad
0\le\delta<\frac{2\sqrt2}{15}.
\tag{3}
$$

It is enough to prove $M>4\delta$.

## 2. Independent elementary bounds

The proof uses

$$
3<\pi<\frac{22}{7},
\qquad
\frac75<\sqrt2<\frac32.
\tag{4}
$$

For the lower bound on $\pi$, expand the geometric series under

$$
\frac\pi4=\int_0^1\frac{dx}{1+x^2}.
$$

The eight-term lower sum is

$$
\sum_{j=0}^7\frac{(-1)^j}{2j+1}
=\frac{33976}{45045}
=\frac34+\frac{769}{180180}
>\frac34.
$$

The upper bound follows from the positive Dalzell integral

$$
\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\frac{22}{7}-\pi>0.
$$

For $0<x<1$,

$$
1-\cos x>\frac{x^2}{2}-\frac{x^4}{24}.
$$

Since $\pi/10>3/10$ and the right side is increasing there,

$$
1-\cos\frac\pi{10}
>
\frac{(3/10)^2}{2}-\frac{(3/10)^4}{24}
=\frac1{25}+\frac{373}{80000}.
$$

Therefore

$$
\arccos\frac{24}{25}<\frac\pi{10},
\qquad
\boxed{d>\frac45.}
\tag{5}
$$

## 3. Dangerous-plateau location

Assume $R>0$.  Then

$$
m<\frac pd<\frac54p,
\qquad
p+m<\frac94p.
$$

Set

$$
P=py,
\qquad
r=Ry,
\qquad
S=(p+m)y.
$$

Thus $S<9P/4$.  Define

$$
Q=1+\frac{y^2}{\kappa}+\frac{yS}{\kappa},
\qquad
\widehat q
=\frac{y^2}{\rho}(Q-1)
=\frac{y^4+y^3S}{\rho\kappa}.
$$

Writing $U=\mu-x_0$, the relation
$U<n+1=p+m+1$ gives $U/\mu<\widehat q$.
The unconditional shelf estimate gives

$$
P<\frac{\sqrt{2\pi\rho\kappa}}{y^2},
$$

and hence

$$
\widehat q
<
\frac94y\sqrt{\frac{2\pi}{\rho\kappa}}
+\frac{y^4}{\rho\kappa}.
\tag{6}
$$

The right side increases in $y$ and decreases in $\kappa$.  At the worst
endpoint,

$$
\sqrt{\frac{2\pi}{\rho\kappa}}
<
\sqrt{\frac{55}{168}}
<\frac{23}{40},
$$

because $55\cdot1600<168\cdot529$.  Consequently

$$
\widehat q
<
\frac9{20}\frac{23}{40}+\frac1{12000}
=\frac{1553}{6000}
<\frac{13}{50}.
\tag{7}
$$

If $t=x_0/\mu$, then

$$
t>1-\widehat q>\frac{37}{50},
\qquad
\frac{x_0}{K}=\rho t
>\frac{24}{25}\frac{37}{50}
=\frac{444}{625}>\frac12.
\tag{8}
$$

This localization is used only after entering $R>0$.

## 4. Local-slope inequality

For $0<z<\mu$, let

$$
\sigma(z)=-A'(z)
=\frac1\pi
\left(
\arccos\frac zK-\arccos\frac z\mu
\right).
$$

The function $\sigma$ is increasing.  Since $p>0$ in the dangerous branch
and the two plateau samples have the same ordinary floor,

$$
A(x_0)-A(x_0+p)<1.
$$

Also,

$$
\sigma(x_0)
=\frac1\pi\int_{\rho t}^{t}\frac{du}{\sqrt{1-u^2}}
>
\frac{\varepsilon t}{\pi\sqrt{1-\rho^2t^2}}.
$$

Using

$$
1-\rho t<y^2Q,
\qquad
1+\rho t<2,
\qquad
t>1-\widehat q,
$$

and squaring positive quantities yields

$$
\boxed{
P^2<
H(P,r):=
\frac{2\pi^2Q}{(1-\widehat q)^2}.
}
\tag{9}
$$

The denominator is positive by (7).

## 5. Independent scaled-loss bound

Since

$$
S=P+\frac{P-r}{d},
$$

$H$ decreases with $r$.  Choose

$$
B_{\rm cr}=\frac{23}{5}.
$$

Suppose $r\ge B_{\rm cr}$.  Then $P\ge r$ and
$H(P,r)\le H(P,B_{\rm cr})$.

On every synthetic point $P'\in[B_{\rm cr},P]$,

$$
S'=P'+\frac{P'-B_{\rm cr}}d<\frac94P'.
$$

The shelf ceiling remains valid because $P'\le P$, so (7) holds on the
complete comparison path.

Let $\alpha=y^2/\rho$.  Then

$$
\alpha\le\frac1{24},
\qquad
\frac{\partial Q}{\partial P'}<\frac9{400}.
$$

A direct rational bound gives

$$
\frac{\partial H}{\partial P'}
<
2\frac{484}{49}\frac9{400}
\left(\frac{50}{37}\right)^3\frac{481}{300}
=\frac{117975}{67081}
<\frac95,
\tag{10}
$$

with exact margin $13854/335405$.  Hence

$$
\frac d{dP'}
\bigl(P'^2-H(P',B_{\rm cr})\bigr)
>
2B_{\rm cr}-\frac95
=\frac{37}{5}>0.
$$

At $P'=B_{\rm cr}$ the worst endpoint is $y=1/5$, $\kappa=20$, with

$$
Q_*=\frac{131}{125},
\qquad
\widehat q_*=\frac1{500}.
$$

The endpoint margin is

$$
B_{\rm cr}^2
-2\left(\frac{22}{7}\right)^2
\frac{Q_*}{(1-\widehat q_*)^2}
=\frac{113954921}{305026225}>0.
\tag{11}
$$

This contradicts (9), proving

$$
\boxed{
R<\frac{23}{5\sqrt\varepsilon}.
}
\tag{12}
$$

The no-drop geometry $m=0$ has $P=r$ and is included in (11).

## 6. Payment and branches

The action representation gives

$$
K\eta>
\frac{2\sqrt2\,\kappa}{3\pi y}
>
\frac{196}{33y}.
\tag{13}
$$

If $R>0$, then

$$
M
>
\left(\frac{196}{33}-\frac{23}{5}\right)\frac1y-1
\ge\frac{188}{33}.
$$

Since

$$
4\delta<\frac{8\sqrt2}{15}<\frac45,
$$

the exact payment margin is

$$
\frac{188}{33}-\frac45
=\frac{808}{165}>0.
\tag{14}
$$

If $R\le0$, then

$$
M\ge\lfloor K\eta\rfloor
>K\eta-1
\ge\frac{947}{33},
$$

so $M-4\delta>4603/165$.

The exceptional branches are separate:

- If $p=n>0$, then $m=0$ and the dangerous proof applies.
- If $p=0<n$, then $R=-dn<0$.
- If $n=0$, then $p=m=R=0$.
- The wall $R=0$ belongs to the safe branch.

Thus (3) closes every low shifted tail.  The permitted high-tail theorem
and weighted scaffold prove (1), including $\kappa=20$.

## 7. Walls

- Equal ordinary floors imply a strict action difference smaller than one,
  including when a sample is integral.
- At a gain wall, $\lfloor x\rfloor>x-1$ remains strict.
- At the interface wall, $\delta=0$.
- The face $x_0=\mu$ is owned by the permitted high-tail theorem.
- The strict phase and spectral conventions are unchanged.
- No dangerous-branch localization is used when $R\le0$.

## 8. Central endpoint

At $\rho=24/25$,

$$
a_\rho=48\pi,
\qquad
\eta_\rho=G_1(24/25).
$$

The independent elementary bounds give

$$
\eta_\rho
>
\frac{2\sqrt2}{375\pi}
>
\frac{49}{20625},
\qquad
\sqrt{a_\rho}<13,
\qquad
C_0<\frac95.
$$

Let

$$
F(X)=\eta_\rho X^2-\sqrt{a_\rho}\,X-C_0.
$$

Its positive root is $\sqrt{K_0(24/25)}$.  At $X=6000$,

$$
F(6000)
>
\frac{49}{20625}6000^2
-13\cdot6000-\frac95
=\frac{413901}{55}>0.
$$

Therefore

$$
\boxed{
K_0(24/25)<6000^2=36000000.
}
\tag{15}
$$

## 9. Closed global union

For the corollary only, use the packet's permitted endpoint and left-zone
inputs:

- $(0,\rho_*]$ is already proved for every $K$;
- on $[\rho_*,1/16]$, the high-angular and small-hole theorems leave any
  possible residual below $64$;
- on $[1/16,24/25]$, the audited monotonicity of $K_0$ and (15) put the
  fixed-ratio threshold below $6000^2$;
- on $[24/25,99/100]$, (1) starts no higher than $200000$;
- on $[99/100,1-1/15625]$, the sharper Round 9 threshold is at most
  $125^5/8$;
- $[1-1/15625,1)$ is already proved for every $K$.

All adjacent faces are included.  At $\varepsilon=1/100$, both local
theorems apply and Round 9 is sharper.  At $\varepsilon=1/15625$, the
aggregate and Round 9 high thresholds both equal $125^5/8$.

Finally,

$$
\frac{125^5}{8}-6000^2
=\frac{30229578125}{8}>0,
$$

$$
2^{32}-\frac{125^5}{8}
=\frac{3842160243}{8}>0,
$$

and

$$
2^{35}-9\frac{125^5}{8}
=\frac{219703819}{8}>0.
$$

Hence

$$
\boxed{
0<\rho<1,
\quad
K\ge\frac{125^5}{8}
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{16}
$$

This is an isolated proof of the frozen local theorem and its seam
corollary.  It does not claim the all-frequency compact residual is closed.
