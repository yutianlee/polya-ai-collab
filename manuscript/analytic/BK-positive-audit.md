# Clean-room audit of BK-positive.tex

Date: 2026-07-16  
Audited file: manuscript/analytic/BK-positive.tex  
Verdict: **PASS**

No incorrect inequality, endpoint assignment, rational table entry, or
unstated numerical/certificate dependency was found. The proof establishes
\(\mathcal B_K(\rho,200)>0\) on
\([7/51,39/50]\) from the displayed analytic formulas and elementary exact
bounds.

## 1. Reconstruction of the starting formula

From the manuscript formula
\[
\mathcal B_K
=\rho(K\eta_\rho-1)+(\mu-\tfrac12)\eta_\rho
+ d_\rho\rho(\mu-1)
-(1+d_\rho)I_K
-\frac{2\rho(2\mu-1)}{15\mu^{3/2}},
\qquad \mu=\rho K,
\]
substitution of \(K=200\) and \(\mu=200\rho\) gives
\[
\rho(200\eta_\rho-1)+(200\rho-\tfrac12)\eta_\rho
=400\rho\eta_\rho-\rho-\frac{\eta_\rho}{2}.
\]
Thus the expansion on lines 84--94 is exact, including the final error term
\[
\frac{2\rho(400\rho-1)}{15(200\rho)^{3/2}}.
\]

All quantities divided by in the proof are positive because
\(7/51>1/8>0\) and \(\rho<1\).

## 2. Uniform bound for \(I_K(200)\)

The implication \(\rho>1/8\Rightarrow\overline R<204\rho\) is exact:
\[
\overline R=200\rho+\frac12<200\rho+4\rho=204\rho.
\]
Using \(200b_\rho=400\pi\rho/(1-\rho)\),
\[
u^2
=\frac{\overline R^2(1-\rho)}{400\pi\rho}
<\frac{204^2\rho(1-\rho)}{400\pi}.
\]
The standard identity
\(\rho(1-\rho)=\tfrac14-(\rho-\tfrac12)^2\leq\tfrac14\)
then gives
\[
u^2\leq\frac{41616}{1600\pi}
<\frac{41616}{4800}
=\frac{867}{100}<9,
\]
where the strict inequality uses \(\pi>3\). Hence \(0<u<3\).

The positive-term series for \(\sinh 2\) gives
\[
\sinh2>2+\frac{8}{6}=\frac{10}{3}>3>u,
\]
so monotonicity of \(\sinh\) and its inverse gives
\(\operatorname{arsinh}u<2\).

Rationalizing \(P=S-\overline R\) gives
\[
P=\frac{200b_\rho}{S+\overline R}.
\]
Since \(S>\overline R>200\rho\),
\[
P<\frac{200b_\rho}{400\rho}
=\frac{b_\rho}{2\rho}.
\]
Therefore
\[
I_K(200)
=\rho P+\frac{b_\rho}{2}\operatorname{arsinh}u
<\frac{b_\rho}{2}+b_\rho
=\frac{3b_\rho}{2}.
\]
Every inequality direction in lines 50--75 is correct.

## 3. Error-term bound

Since \(2\mu-1<2\mu\),
\[
\frac{2\rho(2\mu-1)}{15\mu^{3/2}}
<\frac{4\rho}{15\sqrt\mu}
=\frac{4\sqrt\rho}{15\sqrt{200}}.
\]
Here \(\rho<1\) and \(\sqrt{200}>14\), so
\[
\frac{4\sqrt\rho}{15\sqrt{200}}
<\frac4{15\cdot14}
=\frac2{105}<\frac1{50}.
\]
The positivity of the error follows from
\(\mu=200\rho>25\), hence \(2\mu-1>0\).
Lines 77--83 are correct.

## 4. Low branch

For \(7/51\leq\rho\leq1/2\),
\[
\eta_\rho=\frac{\sqrt3}{2\pi}-\frac16,
\qquad 0<d_\rho\leq\frac13.
\]
The square-root bounds are exact:
\[
3-\left(\frac{265}{153}\right)^2
=\frac{2}{23409}>0,
\qquad
\left(\frac{26}{15}\right)^2-3
=\frac1{225}>0.
\]
The lower comparison used for \(\eta_\rho\) is
\[
\frac{1855}{6732}-\frac{11}{40}
=\frac{37}{67320}>0.
\]
Consequently
\[
\frac{\sqrt3}{2\pi}>\frac{11}{40}
\quad\Longrightarrow\quad
\eta_\rho>\frac{11}{40}-\frac16=\frac{13}{120}.
\]
Likewise, \(\pi>78/25\) and \(\sqrt3<26/15\) give
\[
\frac{\sqrt3}{2\pi}
<\frac{26}{15}\frac{25}{156}
=\frac5{18},
\quad\Longrightarrow\quad
\eta_\rho<\frac19.
\]

In the expansion of \(\mathcal B_K\):

- \(400\rho\eta_\rho-\rho>
  (400\cdot13/120-1)\rho=(127/3)\rho\);
- \(-\eta_\rho/2>-1/18\);
- \(d_\rho\rho(200\rho-1)\geq0\);
- using \(d_\rho\leq1/3\), \(I_K<3b_\rho/2\), and
  \(4\pi<88/7\),
  \[
  -(1+d_\rho)I_K>
  -\frac{88\rho}{7(1-\rho)};
  \]
- the final error is greater than \(-1/50\).

The two constant errors combine exactly:
\[
-\frac1{18}-\frac1{50}=-\frac{17}{225}.
\]
For \(\rho\leq1/2\),
\[
\frac{127}{3}-\frac{88}{7(1-\rho)}
\geq\frac{127}{3}-\frac{176}{7}
=\frac{361}{21}>0.
\]
It is therefore valid to replace \(\rho\) by its lower endpoint \(7/51\).
The final arithmetic is
\[
\frac7{51}\frac{361}{21}-\frac{17}{225}
=\frac{2912}{1275}>0.
\]
The low-branch estimate is correct.

## 5. High-branch preliminary bounds

For \(1/2\leq\rho\leq39/50\),
\(\arcsin\rho\geq\rho\), and \(\pi<22/7\) gives
\[
d_\rho=\frac{2\arcsin\rho}{\pi}
\geq\frac{2\rho}{\pi}>\frac{7\rho}{11}.
\]
Also
\[
5-\left(\frac{53}{25}\right)^2
=\frac{316}{625}>0,
\]
so
\[
\sin\frac{3\pi}{10}
=\frac{1+\sqrt5}{4}
>\frac{1+53/25}{4}
=\frac{39}{50}.
\]
Monotonicity of \(\arcsin\) therefore yields
\(d_\rho<3/5\), including at the upper endpoint.

The identity
\[
G_1(\rho)=\frac1\pi\int_\rho^1\arccos t\,dt
\]
implies both \(0<G_1(\rho)\leq G_1(1/2)=\omega_0\) and the required
monotonicity. The pointwise bound
\(\arccos t\geq\sqrt{2(1-t)}\) is correct: putting
\(y=\arccos t\) gives
\[
\sqrt{2(1-t)}=2\sin(y/2)\leq y=\arccos t.
\]
Using \(\sqrt2>7/5\) and \(\pi<22/7\),
\[
\frac{2\sqrt2}{3\pi}>\frac{49}{165}.
\]
Thus all bounds in lines 128--155 follow from the stated analytic facts.

## 6. Slab-bound inequality directions

On a slab \(a\leq\rho\leq c\), the condition
\(s_c^2\leq1-c\) with \(s_c\geq0\) gives
\[
(1-\rho)^{3/2}
\geq(1-c)\sqrt{1-c}
\geq(1-c)s_c.
\]
Therefore \(\eta_\rho\geq\eta_c\), as used.

Each endpoint substitution in \(L(a,c)\) has the correct direction:

- \(400\rho\eta_\rho\geq400a\eta_c\);
- \(-\rho\geq-c\);
- \(-\eta_\rho/2>-1/18\);
- since
  \[
  \frac{d}{d\rho}\bigl[\rho^2(200\rho-1)\bigr]
  =2\rho(300\rho-1)>0,
  \]
  \[
  d_\rho\rho(200\rho-1)
  >\frac{7a^2}{11}(200a-1);
  \]
- \(d_\rho<3/5\), \(I_K<3b_\rho/2\), and
  \(\pi<22/7\) imply
  \[
  (1+d_\rho)I_K
  <\frac{528}{35}\frac{\rho}{1-\rho};
  \]
  because \(\rho/(1-\rho)\) is increasing,
  this is at most its \(c\)-endpoint bound;
- the final error is less than \(1/50\).

These reproduce exactly the stated expression for \(L(a,c)\).
The two monotonicity observations above are implicit rather than written out
in BK-positive.tex, but they are elementary consequences of the displayed
formulas and do not constitute a logical gap.

## 7. Independent replay of every table entry

The square-root margins and recomputed values are:

| row | \(1-c-s_c^2\) | recomputed \(\eta_c\) | recomputed \(L(a,c)\) |
|---:|---:|---:|---:|
| 1 | \(1/180\) | \(49/550\) | \(251291/17325\) |
| 2 | \(3/320\) | \(49/660\) | \(70619/5040\) |
| 3 | \(7/720\) | \(2401/39600\) | \(576451/44100\) |
| 4 | \(3/1210\) | \(147/3025\) | \(4940821/435600\) |
| 5 | \(0\) | \(49/1320\) | \(2411/315\) |
| 6 | \(21/2500\) | \(1127/37500\) | \(11101801/1386000\) |

All six values of \(L(a,c)\) match the source exactly and have positive
numerators and denominators.

The intervals meet exactly at
\[
\frac12,\ \frac{11}{20},\ \frac35,\ \frac{13}{20},\
\frac7{10},\ \frac34,\ \frac{39}{50},
\]
in strictly increasing order. Thus they tile the entire high branch with no
gap.

## 8. Dependency audit

The proof uses:

1. the analytic definitions and differentiated identities
   cm:eq-B-def, cm:eq-IK, and cm:eq-BK;
2. exact rational bounds for \(\pi\) and elementary radicals;
3. elementary monotonicity of \(\arcsin\), \(\sinh\), and rational
   functions;
4. the exact identity for \(G_1\) and the elementary
   \(\arccos\)-lower bound.

It does not use a decimal comparison, root finder, interval enclosure,
certificate output, or unlisted computed constant. Hence the claim that this
lemma is independent of the numerical and interval certificates is correct.

**Final result: PASS. No mathematical gap found.**
