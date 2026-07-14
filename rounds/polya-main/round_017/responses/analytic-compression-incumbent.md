# Round 17 A2 Analytic-Compression Incumbent

Status: **EXACT CANDIDATE DERIVED / NOT PROMOTED**.

Role: A2 incumbent exploration.

Baseline commit:
`047c9ef5c4fe2329d73d3568c1ac48654dd18585`.

Frozen residual packet:
`state/lemma_packets/SHELL-rho-compact-round17.md`, SHA-256
`eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e`.

The packet hash was checked before this work began. This document does not
edit the packet, change the accepted mask, or promote a theorem. It derives
one exact candidate for a later isolated reconstruction and adversarial
audit.

## 1. Claim only

This section is intentionally proof-free so that an isolated A3 prompt can
quote the candidate without exposing the incumbent argument.

Set

$$
\rho_c=\frac1{1+2\pi},
\qquad
z_\rho=\frac{\pi}{1-\rho},
\qquad
k_1(\rho)=\sqrt{z_\rho^2+2},
\qquad
k_2(\rho)=\sqrt{z_\rho^2+6}.
\tag{C1}
$$

### Candidate lemma C17

For

$$
\boxed{
\rho_c\leq\rho\leq\frac78,
\qquad
z_\rho\leq K\leq k_2(\rho),
}
\tag{C2}
$$

the exact strict shell count satisfies the stronger strict comparison

$$
\boxed{
N_D(A_{\rho,1},K^2)
<\frac{2}{9\pi}(1-\rho^3)K^3.
}
\tag{C3}
$$

The genuinely new analytic portion would be

$$
\boxed{
\mathcal C_{17}
=\left\{(\rho,K):
\rho_c\leq\rho<\frac78,
\quad z_\rho<K\leq k_2(\rho)
\right\}.
}
\tag{C4}
$$

The lower face \(K=z_\rho\) and the right face \(\rho=7/8\) are included in
the lemma but already have analytic owners. Both upper faces
\(K=k_1(\rho)\) and \(K=k_2(\rho)\) are included. The candidate has no
sampled or decimal endpoint.

### Permitted dependencies

1. `CONV-strict-counting`, only for the convention that eigenvalues equal
   to \(K^2\) are excluded.
2. `SHELL-sturm-liouville-completeness`, for the exact orthogonal angular
   decomposition, radial operators, and multiplicities \(2\ell+1\).
3. The frozen Round 17 packet, only to identify
   \(\mathcal A_{16}\), \(\mathcal D_{16}\), their exact faces, and the
   active upper branches. It is not an input to the spectral comparison.
4. The one-dimensional Dirichlet min--max argument and all elementary
   constant inequalities are reconstructed below.

No Bessel-root certificate, phase enclosure, incumbent Round 16 endpoint
proof, sampled plot, floating-point comparison, or desired compact-ratio
conclusion is permitted as a proof input.

## 2. Why this is the selected first compression

On \(\rho\geq\rho_c\), the exact lower residual wall is the zero-count wall
\(K=z_\rho\). A direct form comparison resolves the first two possible
angular channels above this wall without Bessel functions. The resulting
band is connected, bounded, attached along its complete lower analytic
face, crosses the formula interface \(\rho=1/2\), crosses the seam interface
\(\rho=5/6\), and reaches the complete endpoint face \(\rho=7/8\).

The proof below closes this candidate completely. It also identifies the
first exact obstruction to extending the same coarse mechanism into the
third angular channel. That obstruction is a failure of the method, not a
counterexample to the shell inequality.

## 3. Radial form comparison

Write

$$
\varepsilon=1-\rho,
\qquad
z=z_\rho=\frac\pi\varepsilon.
\tag{P1}
$$

After the standard unitary transformation \(u(r)=rR(r)\), angular channel
\(\ell\) is governed on \(H^2(\rho,1)\cap H_0^1(\rho,1)\) by

$$
L_\ell=-\frac{d^2}{dr^2}+\frac{\ell(\ell+1)}{r^2}.
\tag{P2}
$$

Let \(\lambda_{\ell,n}\) be its \(n\)-th eigenvalue, in increasing order.
Since \(0<r\leq1\), one has \(r^{-2}\geq1\). The form inequality

$$
L_\ell
\geq
-\frac{d^2}{dr^2}+\ell(\ell+1)
\tag{P3}
$$

and the Dirichlet min--max principle give, for every \(\ell\geq0\) and
\(n\geq1\),

$$
\boxed{
\lambda_{\ell,n}
\geq n^2z^2+\ell(\ell+1).
}
\tag{P4}
$$

For \(\ell=0\), (P2) is exactly the Dirichlet interval Laplacian. Thus

$$
\boxed{
\lambda_{0,n}=n^2z^2,
\qquad
k_{0,n}=nz.
}
\tag{P5}
$$

In particular, \(z\) is the exact first radial eigenfrequency, not merely a
comparison threshold.

Throughout (C2), \(z>\pi>3\). If \(n\geq2\), then

$$
\lambda_{\ell,n}\geq4z^2
>z^2+6\geq K^2,
\tag{P6}
$$

because \(3z^2>27>6\). Hence no radial index \(n\geq2\) contributes anywhere
in the candidate band.

If \(\ell\geq2\), then

$$
\lambda_{\ell,1}
\geq z^2+\ell(\ell+1)
\geq z^2+6
\geq K^2.
\tag{P7}
$$

The strict counting convention excludes such an eigenvalue even when the
last inequality is equality. Consequently only
\((\ell,n)=(0,1)\) and possibly \((1,1)\) can contribute. Their angular
multiplicities are respectively \(1\) and \(3\).

## 4. Exact count caps at both internal walls

### 4.1 First band

For

$$
z\leq K\leq k_1=\sqrt{z^2+2},
\tag{P8}
$$

(P4) gives

$$
\lambda_{\ell,1}\geq z^2+2\geq K^2
\qquad(\ell\geq1).
\tag{P9}
$$

At \(K=k_1\), equality in the comparison still gives no counted
\(\ell=1\) eigenvalue because the count is strict below \(K^2\). By (P5),
the \((\ell,n)=(0,1)\) eigenvalue is excluded at \(K=z\) and included for
\(K>z\). Therefore

$$
N_D(A_{\rho,1},K^2)
=
\begin{cases}
0,&K=z,\\
1,&z<K\leq k_1.
\end{cases}
\tag{P10}
$$

### 4.2 Second band

For

$$
k_1<K\leq k_2=\sqrt{z^2+6},
\tag{P11}
$$

the two surviving channels have total multiplicity at most

$$
1+3=4.
\tag{P12}
$$

At \(K=k_2\), (P7) excludes every \(\ell=2\) eigenvalue even if its lower
bound meets \(K^2\). Thus

$$
\boxed{
N_D(A_{\rho,1},K^2)\leq4
\quad(k_1<K\leq k_2),
}
\tag{P13}
$$

including the complete upper face. Accidental coincidences cannot enlarge
this cap: the exact direct sum already assigns the full multiplicities
\(1\) and \(3\).

## 5. Weyl payment on the first band

Put

$$
W(\rho,K)=\frac{2}{9\pi}(1-\rho^3)K^3.
\tag{P14}
$$

At the lower face,

$$
W(\rho,z)
=\frac{2\pi^2}{9}
\frac{1+\rho+\rho^2}{(1-\rho)^2}.
\tag{P15}
$$

For \(\rho>0\),

$$
1+\rho+\rho^2-(1-\rho)^2=3\rho>0.
\tag{P16}
$$

Together with \(\pi>3\), this yields the uniform strict reserve

$$
\boxed{
W(\rho,z)>\frac{2\pi^2}{9}>2>1.
}
\tag{P17}
$$

Since \(W\) increases strictly with \(K>0\), (P10) and (P17) prove (C3) on
the entire first band, including \(K=z\) and \(K=k_1\).

## 6. Weyl payment on the second band

Define the value at the internal face

$$
F(\rho)
=W\!\left(\rho,k_1(\rho)\right).
\tag{P18}
$$

With \(e=1-\rho\) and \(S=1+\rho+\rho^2\), exact simplification gives

$$
F(\rho)
=\frac{2}{9\pi}
\frac{S}{e^2}
\left(\pi^2+2e^2\right)^{3/2}.
\tag{P19}
$$

Its logarithmic derivative is

$$
\frac{F'(\rho)}{F(\rho)}
=\frac{1+2\rho}{S}
+\frac2e
-\frac{6e}{\pi^2+2e^2}
=\frac{1+2\rho}{S}
+\frac{2(\pi^2-e^2)}{e(\pi^2+2e^2)}
>0.
\tag{P20}
$$

Thus \(F\) is strictly increasing on \(0<\rho<1\), so its minimum on the
candidate ratio interval is \(F(\rho_c)\).

For a fully rational lower ledger, first note the exact elementary bounds

$$
\frac{157}{50}<\pi<\frac{22}{7}.
\tag{P21}
$$

The upper bound follows, for example, from the positive integral identity

$$
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\tag{P22}
$$

For the lower bound, Machin's exact identity and the alternating arctangent
bounds \(x-x^3/3<\arctan x<x\) give

$$
\begin{aligned}
\pi
&=16\arctan\frac15-4\arctan\frac1{239}\\
&>16\left(\frac15-\frac1{3\cdot5^3}\right)-\frac4{239}
=\frac{281476}{89625}
=\frac{157}{50}+\frac{107}{179250}.
\end{aligned}
\tag{P23}
$$

For completeness, the Machin identity has a finite exact check. If
\(a=\arctan(1/5)\) and \(b=\arctan(1/239)\), two applications of the
tangent doubling formula give

$$
\tan(2a)=\frac5{12},
\qquad
\tan(4a)=\frac{120}{119}.
$$

Therefore

$$
\tan(4a-b)
=\frac{120/119-1/239}{1+120/(119\cdot239)}
=\frac{28561/28441}{28561/28441}=1.
$$

The angle \(4a-b\) lies in \((0,\pi/2)\), so it equals \(\pi/4\), proving
the identity used in (P23) without a numerical value of \(\pi\).

At \(\rho_c=1/(1+2\pi)\),

$$
\rho_c<\frac{25}{182},
\qquad
z_{\rho_c}=\pi+\frac12>\frac{91}{25},
\qquad
\frac{2}{9\pi}>\frac7{99}.
\tag{P24}
$$

Moreover,

$$
z_{\rho_c}^2+2>\frac{9531}{625},
\qquad
\sqrt{z_{\rho_c}^2+2}>\frac{488}{125},
\tag{P25}
$$

because

$$
\frac{9531}{625}-\left(\frac{488}{125}\right)^2
=\frac{131}{15625}>0.
\tag{P26}
$$

Substitution into (P18) produces the exact margin

$$
\begin{aligned}
F(\rho_c)
&>\frac7{99}
\left(1-\left(\frac{25}{182}\right)^3\right)
\frac{9531}{625}\frac{488}{125}\\
&=\frac{388430104857}{92514296875}\\
&=4+\frac{18372917357}{92514296875}>4.
\end{aligned}
\tag{P27}
$$

For the second band \(K>k_1(\rho)\). Therefore (P20), (P27), and strict
monotonicity in \(K\) give

$$
W(\rho,K)>F(\rho)\geq F(\rho_c)>4.
\tag{P28}
$$

Together with (P13), this proves (C3) on the second band, including
\(K=k_2(\rho)\). Equations (P17) and (P28) complete the candidate lemma.

## 7. Exact location inside the frozen residual

This section checks the new portion (C4) against every active primitive
branch, rather than confusing a convenient over-cover with
\(\mathcal D_{16}\).

The frozen packet proves

$$
\omega_0<\frac18<\rho_c.
\tag{P29}
$$

Hence A4 is unavailable on the candidate's ratio interval. The lower
residual wall is exactly \(L(\rho)=z_\rho\). For \(K>z_\rho\), neither A3
nor A2 applies: at \(\rho=\rho_c\) the two lower walls agree, while for
\(\rho>\rho_c\) one has \(z_\rho>1/(2\rho)\).

The candidate is uniformly below every active upper branch. Indeed,

$$
0<\eta_\rho\leq\omega_0<\frac18.
\tag{P30}
$$

Since \(a_\rho=2\rho z_\rho\) and \(C_0>0\), formula (1) of the frozen
packet gives

$$
K_0(\rho)
>\frac{a_\rho}{\eta_\rho^2}
>64a_\rho
=128\rho z_\rho.
\tag{P31}
$$

The function \(\rho z_\rho=\pi\rho/(1-\rho)\) is increasing and
\(\rho_cz_{\rho_c}=1/2\). Consequently

$$
K_0(\rho)>64.
\tag{P32}
$$

On the other hand, \(\rho\leq7/8\) gives

$$
z_\rho\leq8\pi<\frac{176}{7}<26,
\qquad
k_2(\rho)<\sqrt{26^2+6}<27.
\tag{P33}
$$

Thus \(k_2<K_0\) on the whole closed candidate band. On
\(5/6\leq\rho\leq7/8\), the still lower active seam branch satisfies

$$
\frac{54}{(1-\rho)^2}\geq1944>27>k_2(\rho).
\tag{P34}
$$

The global accepted face A10 also lies far above the candidate:

$$
k_2(\rho)<27<87025.
\tag{P35}
$$

The retained A7 branch meets the ratio interval only at \(\rho=7/8\),
whose complete vertical face is already A1; A8 and A9 do not meet
\(I_{16}\). A0 lies at \(\rho=\rho_*<\rho_c\). Therefore the only portions
of the closed lemma band already in \(\mathcal A_{16}\) are its lower face
\(K=z_\rho\) and its endpoint face \(\rho=7/8\). Equivalently,

$$
\boxed{
\overline{\mathcal C}_{17}\cap\mathcal D_{16}
=\mathcal C_{17},
}
\tag{P36}
$$

where \(\overline{\mathcal C}_{17}\) denotes the closed band (C2), and
\(\mathcal C_{17}\) is exactly (C4). This proves
\(\mathcal C_{17}\subset\mathcal D_{16}\) without a sampled inference.

## 8. Relation to the certified pilot

The candidate actually contains the complete certified Round 8 box

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right].
\tag{P37}
$$

For its lower wall, monotonicity of \(z_\rho\) and \(\pi<22/7\) give

$$
z_\rho
\leq\frac{2000\pi}{999}
<\frac{44000}{6993}
=\frac{67}{10}-\frac{28531}{69930}
<\frac{67}{10}.
\tag{P38}
$$

For its upper wall, monotonicity of \(z_\rho\) and \(\pi>157/50\) give

$$
\begin{aligned}
k_2(\rho)^2-\left(\frac{168}{25}\right)^2
&\geq
\left(\frac{2000\pi}{1001}\right)^2
+6-\left(\frac{168}{25}\right)^2\\
&>
\left(\frac{6280}{1001}\right)^2
+6-\left(\frac{168}{25}\right)^2\\
&=\frac{126027526}{626250625}>0.
\end{aligned}
\tag{P39}
$$

The ratio inclusion is immediate. Hence

$$
\boxed{B_0\subset\mathcal C_{17}.}
\tag{P40}
$$

This does not change the current evidence class: before promotion, \(B_0\)
remains `certified_only`. It says that a successful independent proof and
promotion of C17 would analytically subsume the pilot.

## 9. Exact surviving sets if the candidate were later promoted

No subtraction in this section is enacted by the incumbent. It records the
exact bookkeeping a later judge would have to apply.

Let

$$
\mathcal A_{17}^{\rm cand}
=\mathcal A_{16}\cup\overline{\mathcal C}_{17}.
\tag{P41}
$$

The resulting analytic residual would be exactly

$$
\boxed{
\mathcal D_{17}^{\rm cand}
=\mathcal D_{16}\setminus\mathcal C_{17}.
}
\tag{P42}
$$

The theorem-wise uncovered set would be

$$
\boxed{
\mathcal U_{17}^{\rm cand}
=\mathcal D_{16}\setminus(B_0\cup\mathcal C_{17})
=\mathcal U_{16}\setminus\mathcal C_{17}.
}
\tag{P43}
$$

Because \(B_0\subset\mathcal C_{17}\), (P43) simplifies, after promotion
only, to

$$
\mathcal U_{17}^{\rm cand}
=\mathcal D_{16}\setminus\mathcal C_{17}
=\mathcal D_{17}^{\rm cand}.
\tag{P44}
$$

This is exact set subtraction, not a replacement of the residual by a
rectangle.

## 10. First obstruction to this mechanism

The next product wall is

$$
K=k_2(\rho)=\sqrt{z_\rho^2+6}.
\tag{P45}
$$

Immediately above it, the form comparison permits the \((\ell,n)=(2,1)\)
channel. The coarse multiplicity cap therefore jumps from \(4\) to

$$
1+3+5=9.
\tag{P46}
$$

At the left ratio face this payment is unavailable. Indeed,
\(z_{\rho_c}=\pi+1/2<51/14<4\), so, using \(\pi>3\),

$$
\begin{aligned}
W\!\left(\rho_c,k_2(\rho_c)\right)
&=\frac{2}{9\pi}(1-\rho_c^3)
\left(z_{\rho_c}^2+6\right)^{3/2}\\
&<\frac2{27}\,22\sqrt{22}
<\frac{220}{27}
<9.
\end{aligned}
\tag{P47}
$$

Thus a uniform continuation past \(k_2\) cannot be obtained merely by
replacing the exact shell spectrum with the same channel-wise product lower
bound and paying all five new angular states at once. A continuation would
need a sharper \(\ell=2\) shell eigenvalue bound, a ratio-dependent
staircase, or a different action/tail argument. Equation (P47) is not a
failure of the target inequality and supplies no counterexample.

## 11. Face and falsification ledger

An isolated reconstruction must check all of the following.

1. \(\rho=\rho_c\), where \(1/(2\rho)=z_\rho\), is included.
2. \(\rho=7/8\) is included in the candidate lemma but excluded from the
   newly absorbed residual because A1 owns the complete face.
3. \(K=z_\rho\) is included in the lemma, has strict count zero, and is
   excluded from \(\mathcal C_{17}\) because A3 owns it.
4. At \(K=k_1(\rho)\), the \(\ell=1\) comparison eigenvalue is not counted;
   the exact count cap is \(1\), not \(4\).
5. At \(K=k_2(\rho)\), the \(\ell=2\) comparison eigenvalue is not counted;
   the count cap remains \(4\).
6. Every \(n\geq2\) mode is excluded by (P6), including all equality
   possibilities.
7. The formula interface \(\rho=1/2\) introduces no change in the spectral
   proof and is included.
8. At \(\rho=5/6\), the inclusive seam starts at \(K=1944\), while the
   candidate remains below \(27\); no face is lost.
9. A10 begins at the included face \(K=87025\), also disjoint from the
   candidate.
10. The complete closed boundary of \(B_0\) satisfies (P38)--(P40).
11. The result uses \(\mathcal D_{16}\), not the coarse four-zone over-cover
    and not \(\mathcal U_{16}\).
12. None of the proof uses a computed Bessel zero or an uncertified decimal
    constant.

## 12. Incumbent verdict

The exact candidate C17 is **ready to freeze as a claim for an isolated A3
clean-room reconstruction**. The incumbent derivation is complete and has
an explicit positive Weyl margin on both subbands. Nothing is promoted by
this file. Promotion would still require byte freezing of the claim,
strictly isolated reconstruction, adversarial review, exact state-patch
bookkeeping, and a judge decision.
