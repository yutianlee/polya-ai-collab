# General dimension, Round 16: independent audit of the continuous geometric reduction and hard face

Date: 19 July 2026

Verdict: **PASS**.  No blocking mathematical, endpoint-domain, equality-wall, or diagnostic-reproducibility defect was found.  The general geometric inequality \(F(a,K)\ge 1/2\), including the unresolved sign of the action-boundary derivative (4.10), remains open exactly as stated in the audited note.

## Frozen artifacts

- Audited note: `human/outbox/general-d-round-16-continuous-geometric-reduction-and-hard-face.md`
- Audited-note SHA-256: `0c987e8dbfd6de9f6b3714e07349a11d556e331bb6491d1d12926ab240fb2dd5`
- Replayed evaluator: `computations/general_d_round16_continuous_geometric_probe.wl`
- Evaluator SHA-256: `beea443c086d31081db19e429bc4393d137825955b82f1f23ae153105a131c4b`

The audited note and evaluator were not edited during this audit.

## Continuous endpoint domain

1. **Elimination of the grid variables.**  With \(q=r+n\ge2\), \(a=q+\bar\alpha\ge2\).  Since the endpoint occurs no later than the owner activity wall,
   
   \[
   K-a\ge \frac{\pi K}{\sqrt{K^2-\kappa_{\rm owner}}}>\pi,
   \qquad
   \kappa_4=\frac34,\quad \kappa_5=2.
   \]
   It also occurs no later than the phase wall, so \(A(q)\ge3/4\).  Because \(\bar\alpha\le1\), one has \(a-1\le q\); the strict decrease of \(A\) therefore gives \(A(a-1)\ge3/4\).  The original upper action wall gives the inverse point \(z>q\ge2\).  Thus (2.1) is a valid enlargement of every original endpoint.

2. **The inverse endpoint is \(z\), not \(a\).**  The piecewise derivative
   
   \[
   A'(s)=\frac{\arccos(s/a)-\arccos(s/K)}{\pi}\quad(s<a),
   \qquad
   A'(s)=-\frac{\arccos(s/K)}{\pi}\quad(s\ge a)
   \]
   is negative on the relevant interior.  Although \(A(a)<1\) need not hold, the identity
   \(A(z)=3/4-G_a(z)\le3/4<1\), together with \(A(0)=(K-a)/\pi>1\), proves that the unique solution of \(A(x)=1\) lies in \((0,z)\).  This repairs the load-bearing endpoint issue without adding an assumption.

## Convex minimization and the scalar \(F\)

Let \(E_0(s)=2(J_K(s)-J_a(s))-s\).  Direct differentiation gives

\[
E_0'(s)=2(1-A(s)),\qquad E_0''(s)=-2A'(s)>0
\]

on the relevant interior, with compatible one-sided formulas at \(s=a\).  Hence \(x\) is the unique minimizer.  Since \(r\le q<z\), \(E_0(r)\ge E_0(x)\).  The exact identities \(n=q-r\), \(M=z-q-\eta\), and \(E_0(x)=2F(a,K)-1\) then give

\[
D_A(r)>\Omega_{\rm end}=E_0(r)+2\eta
 \ge 2F(a,K)-1+2\eta.
\]

No floor or inverse-wall convention is lost in this reduction.

## Differential calculus and Lemma 4.1

The parameter derivative

\[
P_b(s)=\partial_bJ_b(s)
=\frac{b^2\arccos(s/b)-s\sqrt{b^2-s^2}}{2\pi b}
\]

for \(s<b\), with zero extension for \(s\ge b\), is correct.  Implicit differentiation of \(G_K(z)=3/4\) gives \(z_K=\sin\theta/\theta\), and the \(x\)-derivatives cancel because \(A(x)=1\).  Consequently

\[
F_K=P_K(x)-\frac{\sin\theta}{\theta},
\qquad F_a=-P_a(x).
\]

The strict Jensen proof of Lemma 4.1 checks out.  If \(G_K(w)=1\), \(h(t)=\sin t-t\cos t\), and \(u(t)=\sin t/t\), then \(P_K(w)\) is the \(t\sin t\)-weighted mean of \(u\).  Under \(y=h(t)\), the function \(U(y)=u(h^{-1}(y))\) is strictly convex because

\[
Q(t)=3\sin^2t-t\sin(2t)-t^2,
\qquad
Q'(t)=4\cos t\,(\sin t-t\cos t)>0.
\]

Jensen and the monotonicity of \(U\) yield

\[
P_K(w)>U\!\left(\frac{h(\beta)}2\right)
>U\!\left(\frac{3h(\beta)}4\right)
=\frac{\sin\theta}{\theta}.
\]

Moreover, \(A(x)=1\) implies \(G_K(x)=1+G_a(x)\ge1\), hence \(x\le w\); since \(P_K\) decreases in its spatial argument, \(F_K>0\).  This also covers \(x\ge a\): then \(G_a(x)=P_a(x)=0\) and \(x=w\).  The reduction to \(K=\max\{a+\pi,k(a)\}\) is therefore valid.

## Boundary faces

1. **Radial face.**  On \(K=a+\pi\), one has \(x=0\) and
   
   \[
   F=\frac{K^2-a^2}{8}-z,
   \qquad
   \frac{dF}{da}=\frac\pi4-\frac{\sin\theta}{\theta}.
   \]
   The note's alternating-Taylor estimates at \(117/100\) are sign-safe.  Independently reducing the two decisive comparisons gives the positive exact margins
   
   \[
   \tan(117/100)-117/100-3\pi/8
   >\frac{8867689904954607}{779709274332548525}>0,
   \]
   
   and
   
   \[
   \frac{\sin(117/100)}{117/100}-\frac{11}{14}
   >\frac{695788735359}{560000000000000}>0.
   \]
   Thus \(z>2\) forces \(\theta<117/100\), so \(dF/da<0\), as claimed.

2. **Action face.**  With \(t=a-1\), \(\gamma=\arccos(t/K)\), and \(\phi=\arccos(t/a)\), differentiation of \(G_K(t)-G_a(t)=3/4\) gives
   
   \[
   K'(a)=\frac{\gamma+\sin\phi-\phi}{\sin\gamma}.
   \]
   Substitution into the tangential derivative produces (4.10).  The note does not claim a proof of its sign; it correctly identifies this as the remaining analytic bottleneck.

3. **Hard \(q=3\) double face.**  In the one-sided limit \(a=z=3\), \(K=3\sec\theta\), and \(\tan\theta-\theta=\pi/4\).  The radius representation makes \(t\mapsto A(\sqrt t)\) concave, so its endpoint chord gives the stated head bound.  Convexity of \(G_K\) and its tangent at \(z=3\) give \(J_K(3)\ge9\pi/(32\theta)\).  Combining these estimates reproduces (5.6).

   The rational bracketing \(107/100<\theta<108/100\) is valid: the Taylor comparisons have positive exact margins
   
   \[
   \frac{37895950228428571}{2880000000000000000},
   \qquad
   \frac{619006280090323}{239257812500000000}.
   \]
   With \(3141/1000<\pi<22/7\) and the stated cosine bound, the final exact reserve is
   
   \[
   \frac{15150166179733}{73320166719360}>\frac15>0.
   \]
   Hence this formerly suspected hard face is rigorously closed.

## Equality walls and ownership

- For \(M=[y]_<\), an integral inverse wall has \(\eta=1\); dropping \(2\eta\) is favorable.
- At the literal lower action wall, \(Q:1\to0\) and \(\chi_q:0\to1\), producing the stated two-unit gain relative to the open endpoint scalar.
- The branch and activity endpoints are used one-sidedly, so an artificial endpoint need not inherit an interior shelf label.
- The zero extension of \(G_a\) and \(P_a\) handles both \(x<a\) and \(x\ge a\).
- The hard \(q=3\) face is a one-sided \(M=0,\ B=1\) limit, not the literal \(y=0\) wall where \(B=0\).

## Diagnostic replay

Wolfram Language 15.0 replay completed successfully and printed `round16ReplayOK=True`.  The independently observed gates agree with the frozen note and evaluator:

- 3,171 seeded endpoint records;
- 0 endpoint-domain violations and 0 identity failures;
- sampled continuous-endpoint minimum \(0.354703412962\ldots\);
- sampled \(F\)-minimum \(0.674149089301\ldots\);
- minimum sampled convexity slack \(6.993069\times10^{-8}\);
- cusp value \(0.342037844059\ldots\);
- two-wall diagnostic \(F=0.627630060735\ldots\);
- hard-face diagnostic \(\Omega=0.704562259856\ldots\);
- exact hard-face reserve `15150166179733/73320166719360`.

The script explicitly labels its floating-point search as diagnostic.  The note's separate larger random search was not part of the frozen evaluator and was not independently reproduced here; it is also presented only as non-rigorous falsification evidence.  Neither numerical search is used as a proof step.

## Boundary of the PASS

This audit validates the continuous endpoint domain, the use of \(z\) rather than \(a\), the strict-convexity reduction, Lemma 4.1, the radial-face sign proof, the rational hard-face certificate, and the stated wall conventions.  It does **not** prove (4.10), prove \(F(a,K)\ge1/2\) on the entire continuous domain, close WP2, or prove the all-dimensional theorem.
