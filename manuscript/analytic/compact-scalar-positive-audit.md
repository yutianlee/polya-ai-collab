# Clean-room audit of `compact-scalar-positive.tex`

Date: 2026-07-16  
Audited SHA-256: `10CD0E5D6DDE5ECD7CFA2B2C64E47368E10E44093A407C04F74E29BB71807BA1`  
Verdict: **PASS**

I reconstructed the proof from its definitions and independently replayed all
printed rational arithmetic.  The differentiation of the loss, the beta
constant, the derivative of the endpoint term, both Bernstein conversions,
the convex-secant estimate and its exact rational sum, the base-curve
substitutions, and the final domain implication are all correct.  No sampled
minimum, floating-point sign, or interval enclosure is needed.

This verdict audits the scalar note and its compatibility with the already
audited structural and angular-block notes.  It does not re-audit the external
Bessel phase theorem used earlier in the main manuscript.

## 1. Definitions and the scaled loss

On the outer branch \(z\in[\rho K,K]\), the shell action is

\[
 A_{\rho,K}(z)=G_K(z)=K G_1(z/K).
\]

Consequently the loss in the angular-block note scales exactly as

\[
 \frac12\int_{\rho K}^{K}
 \frac{z}{(1+2A_{\rho,K}(z))^2}\,dz
 =\frac{K^2}{2}\int_\rho^1
 \frac{s}{(1+2KG_1(s))^2}\,ds=\mathcal J(\rho,K).
\]

Thus the displayed definition of \(\mathcal S\) is exactly the scalar gap
from `compact-angular-block.tex`; no scaling factor or endpoint term is
missing.

Differentiating the explicit formula for \(G_1\) gives
\(G_1'(s)=-\arccos(s)/\pi\), while \(G_1(1)=0\).  Hence

\[
 G_1(s)=\frac1\pi\int_s^1\arccos u\,du.
\]

If \(u=\cos v\), then \(1-u=1-\cos v\le v^2/2\), so
\(\arccos u\ge\sqrt{2(1-u)}\).  Integration gives exactly

\[
 G_1(s)\ge \frac{2\sqrt2}{3\pi}(1-s)^{3/2}.
\]

## 2. Elementary constants

The square-root inequalities have the exact squared reserves

\[
 2-\left(\frac{140}{99}\right)^2=\frac2{9801}>0,
 \qquad
 3-\left(\frac53\right)^2=\frac29>0.
\]

The classical Archimedean lower bound \(223/71<\pi\) implies the stated
weaker lower bound because

\[
 \frac{223}{71}-\frac{157}{50}=\frac3{3550}>0.
\]

The upper bound \(\pi<22/7\) is the standard other Archimedean bound.  Thus
all three constant inequalities used in the note are valid independently of
decimal evaluation.

## 3. Derivative collapse and beta integral

Writing \(G=G_1(s)\), direct differentiation gives

\[
\begin{aligned}
 \partial_K\mathcal J
 &=K\int_\rho^1\frac{s}{(1+2KG)^2}\,ds
   -2K^2\int_\rho^1\frac{sG}{(1+2KG)^3}\,ds\\
 &=K\int_\rho^1
   \frac{s\bigl((1+2KG)-2KG\bigr)}{(1+2KG)^3}\,ds\\
 &=K\int_\rho^1\frac{s}{(1+2KG)^3}\,ds.
\end{aligned}
\]

This verifies the claimed derivative collapse.

With \(a=4\sqrt2/(3\pi)\), the turning bound and \(s\le1\) give

\[
 \int_\rho^1\frac{s\,ds}{(1+2KG_1(s))^3}
 \le \int_0^\infty\frac{dt}{(1+aKt^{3/2})^3}.
\]

Under \(u=aKt^{3/2}\), this last integral is

\[
 \frac23(aK)^{-2/3}B\!\left(\frac23,\frac73\right).
\]

The gamma identities give

\[
 B\!\left(\frac23,\frac73\right)
 =\frac{\Gamma(2/3)\Gamma(7/3)}{\Gamma(3)}
 =\frac{4\pi}{9\sqrt3},
\]

so the exact constant is \(8\pi/(27\sqrt3)\), as printed.

At \(K=12\), cubing the positive bound gives

\[
 \left[\frac{8\pi}{27\sqrt3}(12a)^{-2/3}\right]^3
 =\frac{\pi^5}{59049\sqrt3}.
\]

Using \(\pi<22/7\) and \(\sqrt3>5/3\), independent reduction gives

\[
 \frac{\pi^5}{59049\sqrt3}
 <\frac{5153632}{1654060905}.
\]

Also

\[
 \left(\frac{88}{567}\right)^3
 =\frac{681472}{182284263}
\]

and exact subtraction reproduces

\[
 \left(\frac{88}{567}\right)^3
 -\frac{5153632}{1654060905}
 =\frac{27812576}{44659644435}>0.
\]

The beta bound is decreasing in \(K\), so the strict estimate for every
\(K>12\) follows.

## 4. Monotonicity in \(K\)

Let \(y=KG_1(\rho)\).  Differentiating the \(K\)-dependent endpoint
factor independently gives

\[
 \frac{d}{dK}\left[
 K\left(\frac{y}{4(1+2y)}+\frac3{32}\right)\right]
 =\frac{y(1+y)}{2(1+2y)^2}+\frac3{32}.
\]

Since \(\theta=\arccos\rho\le\pi/2\), multiplication by
\(2\pi\rho/\theta\) gives the claimed lower bound \(3\rho/8\).  The
boundary term satisfies

\[
 -\frac{\pi\rho}{4(1-\rho)}
 >-\frac{11\rho}{14(1-\rho)}
\]

by \(\pi<22/7\).  Finally,

\[
 \frac16-\frac{88}{567}=\frac{13}{1134},
 \qquad
 12\cdot\frac{13}{1134}=\frac{26}{189}.
\]

Thus the derivative lower bound in the source reduces to positivity of

\[
 p(\rho)=(1-\rho)
 \left(\frac{26}{189}+4\rho^2+\frac{3\rho}{8}\right)
 -\frac{11\rho}{14}.
\]

Expanded in powers of \(\rho\), this is

\[
 p(\rho)=\frac{26}{189}-\frac{829}{1512}\rho
         +\frac{29}{8}\rho^2-4\rho^3.
\]

The inequality \(\rho_c>7/51\) follows from
\(\pi<22/7\), exactly as stated.  Applying the affine substitution from
\([7/51,39/50]\) to \([0,1]\), and using

\[
 b_j=\sum_{i=0}^j
 \frac{\binom ji}{\binom 3i}a_i
\]

for the power-to-Bernstein conversion, independently reproduces all four
coefficients:

| \(j\) | independently recomputed \(b_j\) |
|---:|---:|
| 0 | \(335005/2785671\) |
| 1 | \(32947387/196635600\) |
| 2 | \(281783183/578340000\) |
| 3 | \(231517/13500000\) |

They match the source and are all strictly positive.  Therefore
\(p>0\), \(\partial_K\mathcal S>0\), and reduction to
\(K=k_{11}(\rho)\) is valid, including the equality face.

## 5. The lower bound for \(K\)

Because \(\rho\ge\rho_c\),

\[
 \frac{\pi}{1-\rho}\ge\pi+\frac12
 >\frac{157}{50}+\frac12=\frac{91}{25}.
\]

The printed square identity checks exactly:

\[
 132+\left(\frac{91}{25}\right)^2
 =\frac{90781}{625}
 =\left(\frac{241}{20}\right)^2+\frac{471}{10000}.
\]

Thus \(K>241/20>12\), so there is no circularity in invoking the beta
lemma in the earlier monotonicity proposition.

The turning coefficient also checks exactly:

\[
 \frac{4(140/99)(241/20)}{3(22/7)}
 =\frac{23618}{3267}
 =\frac{36}{5}+\frac{478}{16335}.
\]

Every inequality has the correct direction: lower bounds are used for
\(\sqrt2,K\), while the upper bound is used for \(\pi\).

## 6. Convex secants and the rational loss table

After \(y=t^2\), the universal loss is

\[
 \int_0^1 2t(1-t^2)\phi(ct^3)\,dt,
 \qquad c=\frac{36}{5},\quad \phi(z)=(1+z)^{-2}.
\]

The weight \(2t(1-t^2)\) is nonnegative.  Since

\[
 \phi''(z)=\frac6{(1+z)^4}>0,
\]

the graph of \(\phi\) lies below its secant on every interval
\([z_i,z_{i+1}]\).  Because \(t\mapsto ct^3\) is increasing, the grid in
the source covers the entire integration interval with no gap or overlap.

Integrating
\(2t(1-t^2)(\alpha_i+c\beta_i t^3)\) gives exactly

\[
 F_i(t)=\alpha_i\left(t^2-\frac{t^4}{2}\right)
 +2c\beta_i\left(\frac{t^5}{5}-\frac{t^7}{7}\right).
\]

For an independent checksum, the ten rational secant contributions
\(F_i(t_{i+1})-F_i(t_i)\) are:

| \(i\) | exact contribution |
|---:|---:|
| 0 | \(7943297/141944320\) |
| 1 | \(5320920722553/221433281144320\) |
| 2 | \(7754334321247/340568373512920\) |
| 3 | \(57254963374765/2940886752269816\) |
| 4 | \(85327308715275/5577300489764864\) |
| 5 | \(6681504002615/594650274627584\) |
| 6 | \(37213394386583/4760663553085720\) |
| 7 | \(130197342943/14560372244320\) |
| 8 | \(1050600778285/324617440009184\) |
| 9 | \(911262292875/1338981210054656\) |

Their exact sum reduces to

\[
 Q=
 \frac{1305767238061446154064110434835938779253983373178558326887}
 {7706446260271137290663804190970969288616921855152043745280},
\]

matching the source.  Independent subtraction also gives exactly

\[
 \frac{17}{100}-Q=
 \frac{21643130923235926743681388145629999054466710986445549053}
 {38532231301355686453319020954854846443084609275760218726400}>0.
\]

The first comparison in the universal-loss estimate is strict because
the turning coefficient is strictly larger than \(36/5\) on a subinterval
of positive measure.  Hence the asserted strict loss bound \(<17/100\)
is justified.

## 7. Base-curve domain and endpoint payment

With \(t^2=1-\rho\), the lower endpoint calculation is

\[
 \frac{11}{50}-\left(\frac7{15}\right)^2=\frac1{450}>0.
\]

At the other end,

\[
 \left(\frac{14}{15}\right)^2-\frac{44}{51}
 =\frac{32}{3825}>0.
\]

Since \(\rho_c>7/51\), these show
\(7/15<t<14/15\) exactly as claimed.  Also

\[
 \frac7{51}-\frac1{10}=\frac{19}{510}>0,
\]

so \(C(\rho)=(100\rho^2-1)/600>0\).

The loss bound gives

\[
 \frac{1+2\rho^2}{12}-\frac{17}{200}
 =\frac{100\rho^2-1}{600}=C(\rho),
\]

with strictness inherited from the strict integral bound.

For the angular endpoint, convexity of \(\arcsin\) on
\([0,1/\sqrt2]\) puts its graph below the chord joining its endpoint
values.  Therefore

\[
 \arccos(1-t^2)=2\arcsin(t/\sqrt2)\le\frac{\pi t}{2}.
\]

The turning estimate and \(k>\pi/t^2\) give

\[
 Y=kG_1(\rho)>\frac{2\sqrt2}{3}t>\frac{14}{15}t,
\]

where the final exact reserve from the stated square-root bound is

\[
 \frac{2(140/99)}3-\frac{14}{15}=\frac{14}{1485}>0.
\]

The intermediate inequality implicit in the source is

\[
 \frac{Y}{t(1+2Y)}
 >\frac{14}{15+28t}
 >\frac{14}{15(1+2t)}.
\]

Thus the endpoint lower bound has the printed constants and direction.
Combining it with \(\pi<22/7\) produces exactly

\[
 \mathcal S(\rho,k)>C(\rho)k^2-\rho E(t)k+\frac12.
\]

Direct common-denominator expansion gives

\[
 840t^2(1+2t)E(t)=660+1005t-1414t^2.
\]

This quadratic is concave.  Its two endpoint values independently reduce
to

\[
 \left.660+1005t-1414t^2\right|_{t=7/15}
 =\frac{184739}{225},
\]

and

\[
 \left.660+1005t-1414t^2\right|_{t=14/15}
 =\frac{82406}{225}.
\]

Both are positive, so \(E(t)>0\) throughout the required interval.

## 8. Rational replacement of \(k\)

For \(x>0\), both sides of the following comparison are positive, and

\[
 \left(x+\frac{66}{x}\right)^2-(x^2+132)
 =\frac{4356}{x^2}>0.
\]

Hence \(\sqrt{x^2+132}<x+66/x\).  Taking \(x=\pi/t^2\) and applying the
two \(\pi\) bounds gives the printed upper bound

\[
 k<\frac{22}{7t^2}+\frac{3300t^2}{157}.
\]

Similarly

\[
 k^2>132+\frac{(157/50)^2}{t^4}.
\]

Since \(C>0\), \(\rho E>0\), the lower replacement for \(k^2\) and the
upper replacement for the negatively signed \(k\) both lower the right
side.  The inference \(\mathcal S>R(t)\) therefore has the correct order.

## 9. Expansion of \(H\) and the degree-nine Bernstein identity

Multiplying \(R(t)\) by \(t^4(1+2t)\) independently gives the factorized
form in the source.  Expansion with exact rational polynomial arithmetic
reproduces every power coefficient:

| power | independently recomputed coefficient |
|---:|---:|
| \(t^0\) | \(-20642567/24500000\) |
| \(t^1\) | \(-6205067/12250000\) |
| \(t^2\) | \(547983/122500\) |
| \(t^3\) | \(-1033727/367500\) |
| \(t^4\) | \(34911551/16485000\) |
| \(t^5\) | \(187093801/8242500\) |
| \(t^6\) | \(8679/1099\) |
| \(t^7\) | \(-138149/2198\) |
| \(t^8\) | \(-2101/157\) |
| \(t^9\) | \(44\) |

The substitution \(t=(7/15)(1+u)\) maps
\([7/15,14/15]\) exactly to \(u\in[0,1]\).  Using the degree-nine
conversion

\[
 d_j=\sum_{i=0}^j
 \frac{\binom ji}{\binom 9i}a_i
\]

independently reproduces all ten printed Bernstein coefficients:

| \(j\) | independently recomputed \(d_j\) |
|---:|---:|
| 0 | \(65408801807437/9463832437500000\) |
| 1 | \(299549381760793/1135659892500000\) |
| 2 | \(15904699805720773/28391497312500000\) |
| 3 | \(2765605256590021/3154610812500000\) |
| 4 | \(33203943051258761/28391497312500000\) |
| 5 | \(38636221171331747/28391497312500000\) |
| 6 | \(2538003206646073/1892766487500000\) |
| 7 | \(28758289199580211/28391497312500000\) |
| 8 | \(12920786461478803/28391497312500000\) |
| 9 | \(3428732855971679/9463832437500000\) |

Every numerator and denominator is positive.  Since the Bernstein basis is
nonnegative and sums to one, \(H(t)>0\) on the entire closed rational
interval.  The factor \(t^4(1+2t)\) is positive, so \(R(t)>0\), and hence
\(\mathcal S(\rho,k_{11}(\rho))>0\).

## 10. Final inference on the actual compact residual

The main manuscript's actual compact owner is

\[
 \mathcal C_{21}=\mathcal D_{20}\cap\{K\le200\},
\]

where

\[
 \mathcal D_{20}=
 \{\rho_c\le\rho<39/50,\ k_{11}(\rho)<K<U(\rho)\}.
\]

Therefore

\[
 \mathcal C_{21}\subset
 \{\rho_c\le\rho\le39/50,\ k_{11}(\rho)\le K\le200\}
 =\mathcal R_{\rm c}.
\]

The scalar theorem covers a closed superset: it includes the otherwise
owned faces \(K=k_{11}\) and \(\rho=39/50\), and does not need the upper
restriction \(K<U(\rho)\).

On \(\mathcal R_{\rm c}\), the monotonicity proposition and the base-curve
result give

\[
 \mathcal S(\rho,K)\ge
 \mathcal S(\rho,k_{11}(\rho))>0.
\]

Compatibility with the preceding two analytic notes is exact.  Writing

\[
 B_{\rm ang}(\rho,K)=\frac{(1-\rho^2)K^2}{6}-\frac12,
\]

the angular-block theorem gives
\(\mathcal E_{\rm ang}<B_{\rm ang}\), while the present scalar inequality
is \(\mathcal H-B_{\rm ang}>0\).  Hence

\[
 \mathcal E_{\rm ang}<B_{\rm ang}<\mathcal H.
\]

The audited structural identity then yields \(W-P>0\).  With the strict
phase-to-lattice reduction already established in the main manuscript,
\(N_D\le P<W\).  Thus this scalar proof closes the actual compact residual,
subject only to the separately stated earlier analytic dependencies; it does
not merely prove positivity on an unrelated rectangle.

**Final result: PASS. No mathematical or arithmetic gap found.**
