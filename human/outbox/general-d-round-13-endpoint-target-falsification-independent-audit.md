# Independent audit: Round 13 endpoint-target falsification

Date: 18 July 2026

Audited source:

human/outbox/general-d-round-13-endpoint-target-falsification.md

Audited SHA-256:

224237C9C74467334CFED974569EC7F45FFB60481C4A0DA8823C9C3978285853

Focused evaluator replayed:

computations/general_d_round13_endpoint_counterexample.wl

Evaluator SHA-256:

467363A7011C09BE5AFFD40F84D3006C895213437316143FA2AAE4331C3CD62E

## 1. Verdict

**PASS.**

The construction is a rigorous counterexample to the proposed universal
sign of the Round 11 sufficient scalar and its Round 12 endpoint
specialization.  The analytic certificate establishes, without using a
floating-point sign:

1. the integer extension-grid and owner-dimension classification;
2. the strict active, open, hard, one-level phase;
3. all 51 ordinary first-floor values \(F_0,\ldots,F_{50}=1\);
4. the branch endpoint \(\bar\alpha=1\);
5. the strict inequality
   \(\widehat\Psi_1<-3/2<0\); and
6. by Round 12 monotonicity, a still smaller endpoint value.

The corrected endpoint reconstruction in the focused evaluator is faithful
to the Round 12 algebra and reproduces

\[
 \Psi_{\rm end}
 =-1.7076202477534487700855386069\ldots.
\]

The same literal computation reproduces the exact S4 decomposition and a
strongly positive true defect.  Thus the gate decision is correct: reject
the surrogate sign target, retain the valid monotone endpoint reduction,
and preserve the original first-floor theorem as open.

This certificate is not a counterexample to \(D_A(r)\geq0\).  At the
constructed point,

\[
 D_A(r)=39.2502753492938364914171865\ldots>0.
\]

## 2. Exact construction and Taylor enclosures

The data are

\[
 \theta=\frac{8899}{100000},\qquad
 q=9998,\qquad n=50,\qquad r=9948,
\]

\[
 \alpha=\frac{999}{1000},\qquad
 \mu=q+\alpha,
\qquad
 K=\frac{3\pi}{4\Phi(\theta)},
\]

where

\[
 \Phi(\theta)=\sin\theta-\theta\cos\theta.
\]

Since

\[
 \Phi(\theta)
 =\frac{\theta^3}{3}-\frac{\theta^5}{30}
  +\frac{\theta^7}{840}-\frac{\theta^9}{45360}
  +\frac{\theta^{11}}{3991680}-\cdots,
\]

the lower and upper alternating truncations in Section 2 have the correct
directions for \(0<\theta<1\).  Likewise,

\[
 1-\frac{\theta^2}{2}+\frac{\theta^4}{24}
 -\frac{\theta^6}{720}
 <\cos\theta
 <1-\frac{\theta^2}{2}+\frac{\theta^4}{24}
 -\frac{\theta^6}{720}+\frac{\theta^8}{40320}.
\]

Combining these bounds with

\[
 \frac{103993}{33102}<\pi<\frac{104348}{33215}
\]

gives the rational enclosures

\[
 10038.12817232145256\ldots<K
 <10038.12817522760781\ldots
\]

and

\[
 9998.40732268805396\ldots<z=K\cos\theta
 <9998.40732558368875\ldots.
\]

They imply the simpler displayed cells

\[
 10038<K<10039,
\qquad
 9998.407<z<9998.408,
\]

\[
 0.407<y=z-q<0.408.
\]

Because \(0<y<1\), its strict floor is zero and hence
\(\eta=y-[y]_< =y\).  Also

\[
 G_K(z)
 =\frac K\pi\bigl(\sin\theta-\theta\cos\theta\bigr)
 =\frac34
\]

exactly by construction.

The supplied script evaluates every displayed rational cross multiplication
and reports all exact certificate gates as true.

## 3. Terminal phase, activity, and endpoint ownership

Let

\[
 w=v-\frac34=G_K(q)-G_K(z).
\]

Since

\[
 -G_K'(s)=\frac{\arccos(s/K)}{\pi}
\]

decreases from \(\beta\) at \(q\) to \(\theta/\pi\) at \(z\), integration
over an interval of length \(y\) gives exactly

\[
 \frac{y\theta}{\pi}\leq w\leq y\beta.
\]

For positive \(x<a\),

\[
 \arccos(x/a)
 =\arctan\frac{\sqrt{a^2-x^2}}{x}.
\]

All four rational \(u\)-brackets in the evaluator have the correct
directions.  On these \(u\)-ranges, the alternating bounds

\[
 u-\frac{u^3}{3}
 <\arctan u
 <u-\frac{u^3}{3}+\frac{u^5}{5}
\]

are valid.  They give

\[
 0.0115379840\ldots<w<0.0115977938\ldots,
\qquad
 \beta<0.029.
\]

The radius derivative

\[
 \frac{\partial}{\partial a}G_a(q)
 =\frac1\pi\sqrt{1-\frac{q^2}{a^2}}
\]

and the estimate

\[
 1-\frac{q^2}{(q+t)^2}\leq\frac{2t}{q}
 \quad(0\leq t\leq1)
\]

give the quoted radius-average bound

\[
 G_{q+1}(q)
 \leq\frac2{3\pi}\sqrt{\frac2q}.
\]

Here \(\sqrt{2/q}<1/70\), so the exact rational upper bound is

\[
 G_{q+1}(q)
 <0.003031522727\ldots<0.0031.
\]

Monotonicity in the radius gives
\(h(\alpha)<G_{q+1}(q)<w\).  Therefore

\[
 0.007<\varepsilon=w-h(\alpha)<0.012<\frac14.
\]

It follows literally that

\[
 B=Q=1,\qquad\chi_q=0,\qquad v<1.
\]

Thus this is the open hard one-level phase and the top square vanishes.
The same bound at \(\alpha=1\) gives \(h(1)<w\), so the phase root satisfies
\(\alpha_*>1\).

The owner dimension is \(d_{\rm own}=4\), for which
\(\kappa_4=3/4\).  The activity endpoint is

\[
 \alpha_{\rm act}
 =K-q-\frac{\pi K}{\sqrt{K^2-3/4}}.
\]

The displayed \(K\)-cell proves this endpoint is larger than one by a wide
rational margin.  For example,

\[
 \sqrt{K^2-\frac34}>K-1,
\]

and hence, using \(K>10038\) and \(\pi<22/7\),

\[
 \frac{\pi K}{\sqrt{K^2-3/4}}
 <\frac{22}{7}\frac{10038}{10037}<4.
\]

Consequently

\[
 \alpha_{\rm act}>10038-9998-4=36>1.
\]

Since the actual \(\alpha=999/1000\) is below this strict activity endpoint,
the point is dimension-active.  The phase and activity endpoints both occur
after the branch endpoint, so

\[
 \bar\alpha=1.
\]

## 4. Complete no-drop shelf

On \([r,q]\),

\[
 \sigma(s)=-A'(s)
 =\frac{\arccos(s/K)-\arccos(s/\mu)}{\pi}.
\]

The rational arctangent brackets give the certified upper bounds

\[
 \sigma(r)<0.010528927<0.012,
\qquad
 \sigma(q)<0.023975612<0.025.
\]

As established in the earlier no-drop analysis, \(\sigma\) is increasing
and convex.  A convex function lies below its endpoint chord, so

\[
 \Delta=A(r)-A(q)
 =\int_r^q\sigma(s)\,ds
 \leq\frac n2\bigl(\sigma(r)+\sigma(q)\bigr)
 <25(0.012+0.025)=0.925.
\]

The phase bounds give

\[
 \frac34<A(q)<0.762.
\]

Since \(A\) decreases spatially,

\[
 A(q)\leq A(r+j)\leq A(r)=A(q)+\Delta
\quad(0\leq j\leq50).
\]

Therefore

\[
 \frac34<A(r+j)<0.762+0.925
 =1.687<\frac74.
\]

Every ordinary-floor argument \(A(r+j)+1/4\) is strictly between \(1\)
and \(2\).  Hence

\[
 F_0=F_1=\cdots=F_{50}=1.
\]

Also

\[
 \mu-r=50.999,
\qquad
 \lfloor\mu-r\rfloor=50=n,
\qquad
 q=r+n.
\]

Thus all first-floor no-drop chamber conditions are certified, with no
appeal to the high-precision replay.

## 5. Rigorous negative scalar bound

The coefficient in the Round 11--12 scalar is exactly

\[
 C_{9948,50}
 =\left(50+\frac{50^2}{3(2\cdot9948+50)}\right)
   \frac{100}{9948+100}
 =\frac{2339375}{4697283}
 <\frac12.
\]

The exact rational bounds give

\[
 \lambda=\frac{K-\mu}{\pi}<\frac{51}{4}.
\]

They also give \(\lambda-3/4>0\).  On the open side, \(Q=1\), \(v<1\),
and \(\eta=y\), so

\[
 L^{\rm op}(\alpha)
 =\frac{\pi}{2\theta}+2y-1-\alpha h(\alpha).
\]

Dropping the negative cap term and using \(y<0.408\) gives

\[
 L^{\rm op}(\alpha)
 <\frac{\pi_{\rm hi}}{2\theta}+2(0.408)-1
 <\frac{35}{2}.
\]

The lower sign is also strict:
\[
 L^{\rm op}(\alpha)
 >\frac{3}{2\theta}-1-G_{q+1}(q)>0.
\]

Thus the maximum with zero is exactly \(L^{\rm op}\).  Since
\(\chi_q=0\),

\[
 \begin{aligned}
 \widehat\Psi_1
 &=L^{\rm op}-\frac n2
   +C_{9948,50}\left(\lambda-\frac34\right)\\
 &<\frac{35}{2}-25
   +\frac12\left(\frac{51}{4}-\frac34\right)\\
 &=-\frac32.
 \end{aligned}
\]

Every replacement is in the correct upper-bound direction and at least one
is strict.  This proves the negative sign analytically.

## 6. Correct endpoint reconstruction

At the branch endpoint, the original integer \(n\) is held fixed and
\(\alpha=1\) is interpreted as the open-side limit.  The endpoint remains
in the open action phase because

\[
 v-G_{q+1}(q)-\frac34
 =0.0085663656954411583\ldots>0.
\]

The correct reconstructed quantities are

\[
 \lambda_{\rm end}=\frac{K-q-1}{\pi},
\]

\[
 L_{\rm end}
 =\frac{\pi}{2\theta}+2y-1-G_{q+1}(q),
\]

\[
 \Psi_{\rm end}
 =\max(0,L_{\rm end})-\frac n2
 +C_{9948,50}\left(\lambda_{\rm end}-\frac34\right).
\]

This is precisely the open-side Round 12 scalar at \(\alpha=1\); no
endpoint \(\chi_q\) or changed value of \(n\) is inserted.  The replay gives

\[
 L_{\rm end}
 =17.4630280684166286375152434\ldots,
\]

\[
 C_{9948,50}
 \left(\lambda_{\rm end}-\frac34\right)
 =5.8293516838299225923992180\ldots,
\]

and hence

\[
 \Psi_{\rm end}
 =-1.7076202477534487700855386\ldots.
\]

This is slightly smaller than the actual-point value

\[
 \widehat\Psi_1
 =-1.7074542234642107773659586\ldots,
\]

in the direction required by Round 12 strict monotonicity.  The evaluator's
endpoint-reconstruction gate now checks this formula directly and passes.

## 7. S4, exact head, and direct defect replay

The 100-digit literal replay gives

\[
 \delta
 =0.00119748715935190061890845075\ldots,
\]

\[
 2\delta
 =0.00239497431870380123781690150\ldots,
\qquad
 \alpha h
 =0.00299372217136206494693137510\ldots.
\]

Thus the cap relaxation has the stated small positive slack

\[
 \alpha h-2\delta
 =0.00059874785265826370911447361\ldots.
\]

The exact slope integral and S4 head are

\[
 2\int_0^n u\sigma(r+u)\,du
 =39.9487276527016745996221545\ldots,
\]

\[
 R_n
 =-\frac n2+2n\varepsilon
  +2\int_0^n u\sigma(r+u)\,du
 =15.8058142791134422140880431\ldots.
\]

Direct strict counting and closed-form ball integrals give

\[
 D_A(q)
 =23.4444610701803942773291434\ldots,
\]

\[
 D_A(r)
 =39.2502753492938364914171865\ldots.
\]

Since \(\chi_q=0\),

\[
 D_A(q)+R_n+\chi_q
 =39.2502753492938364914171865\ldots
 =D_A(r).
\]

The focused script reports a numerical zero residual with about \(89.42\)
digits of accuracy, stronger than the source's “more than 80” description.
The exact equality itself is the already proved S4 identity; the numerical
replay confirms that the literal counts and integral implementation follow
that identity.

The exact-head diagnostic is also reproduced:

\[
 \widehat L_1+R_n
 =33.2688498448176376217667146\ldots>0.
\]

The true defect and exact-head positivity are high-precision diagnostics,
not premises of the rational negative-scalar certificate.  Their margins
are large, and they independently confirm that the falsification concerns
the surrogate rather than the shell defect.

## 8. Strict faces, script gates, and gate decision

The replay locates the point strictly inside every relevant chamber:

\[
 0<\alpha<1,\qquad
 0<\varepsilon<\frac14,\qquad
 0<\eta<1,
\]

\[
 B=Q=1,\qquad\chi_q=0.
\]

The sampled action range is

\[
 0.7585708662641176761\ldots
 \leq A(r+j)
 \leq1.4707676500456716711\ldots,
\]

so every ordinary-floor argument is separated from both adjacent integer
walls.  Likewise \(v+1/4\), \(A(q)+1/4\), and \(y\) are separated from
their strict walls.  The endpoint \(\alpha=1\) is used only as a limit.

A fresh Wolfram 15.0 replay reports:

- every exact rational certificate gate: true;
- every chamber and activity replay gate: true;
- endpoint reconstruction: true;
- negative actual and endpoint scalar gates: true;
- positive direct defect: true;
- S4 replay: true;
- round13CertificatePass: true; and
- round13ReplayPass: true.

The final gate decision follows:

1. Round 12 Proposition 1.1 and its monotone implication remain valid.
2. The proposed universal endpoint sign target (3.11) is false.
3. The Round 11 pre-shelf scalar cannot close the extension grids
   universally.
4. The pointwise program must retain the exact correlated S4 head, as Round
   14 does, or pivot to the weighted aggregate.  A new ratio partition or
   another lossy head surrogate would not address the demonstrated failure.

## 9. Nonblocking precision notes and final disposition

No load-bearing correction is required.

Two implementation details are worth recording:

1. The displayed bound \(\beta<0.029\) is an immediate exact consequence of
   the certified \(u_{q,K}\) bracket and the same arctangent upper bound.
   The script uses that bound in \(w_{\rm hi}\), although it does not expose
   a separately named Boolean gate for \(\beta<0.029\).
2. The direct defect and S4 residual are arbitrary-precision evaluations,
   not directed interval enclosures.  The counterexample to the surrogate
   does not rely on either numerical sign: it is already proved by the
   rational bound \(\widehat\Psi_1<-3/2\).

Final disposition:

- Exact Taylor/rational certificate: **PASS**.
- Extension-grid, activity, and chamber ownership: **PASS**.
- Complete first-floor no-drop verification: **PASS**.
- Rigorous negative Round 11 scalar: **PASS**.
- Corrected Round 12 endpoint reconstruction: **PASS**.
- Exact S4 identity and numerical defect ledger: **reproduced; PASS**.
- Gate rejection of (3.11) and the universal pre-shelf scalar: **PASS**.
- Original tail inequality at this point: **positive, not falsified**.

No change was made to either primary Round-13 file.
