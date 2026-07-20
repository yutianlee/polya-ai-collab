# Independent audit: General dimension, Round 39

Date: 20 July 2026

Audited artifacts:

- `human/inbox/general-d-strategy_r2.md`
- `human/outbox/general-d-round-39-outer-face-floor-elimination-and-cap-sharpening.md`
- `computations/general_d_round39_outer_face_replay.wl`
- `computations/general_d_round39_outer_face_diagnostic.py`
- the Round 39 edits in the live workflow and state documents

## Verdict

**PASS.** The complete analytic implication chain for the Round 39 claims is
sound. In particular, the note proves \(J<1/10\) on the residual \(p\geq3\)
gap, closes \(p-dm\leq11/5\), derives the exact outer-\(B\) selected-scalar
identity and its intrinsic lower bound, proves \(j\geq1\) on the simultaneous
outer-\(B\)/lower-shelf face, and closes that face by the phase--stretch
argument. The one-sided upper-\(\alpha\) outer-\(B\) endpoint and every
broader class listed in the note remain open.

This audit made four presentation-only repairs: it printed the arcsine-tail
coefficient bound, supplied the elementary \(G_{q+1}(q)<1/2\) justification,
corrected a denominator description in the rational phase proof, and completed
the loss ledger from (5.1) to (5.2), including the \((j-1)\)-reserve. It also
added an exact Mathematica replay of the cap formula. None changes a theorem
statement or proof direction.

No edit was made to `state/proof_obligations.yml`. Its SHA-256 remains

`a5b2489ab8a45a5d58b2b76b27cb42ba3fd6ff3c6b40c7dc9d9832789e9003d4`.

## 1. Residual cap and threshold

The cap proof is correct. Since \(r,m\geq1\) and \(p\geq3\), one has
\(q=r+p+m\geq5\). With \(I_a(q)=\int_q^aG_a(z)\,dz\), radius monotonicity
and \(\mu<q+1\) give

\[
 J=2I_\mu(q)<2I_{q+1}(q).
\]

The representation

\[
 I_{q+1}(q)=\frac1\pi
 \int_{0\leq u\leq w\leq1}
 \sqrt{1-\left(\frac{q+u}{q+w}\right)^2}\,dw\,du
\]

decreases pointwise with \(q\), because \((q+u)/(q+w)\) increases for
\(u\leq w\). Hence \(J<2I_6(5)\). Direct integration gives

\[
 2I_6(5)=
 \frac{86\arccos(5/6)-15\sqrt{11}}{2\pi}.
\]

Writing \(\arccos(5/6)=2\arctan(1/\sqrt{11})\), the alternating series
truncated after its positive \(z^5/5\) term gives

\[
 86\arccos(5/6)-15\sqrt{11}
 <\frac{3761}{1815\sqrt{11}}
 <\frac{7522}{11979}<\frac{333}{530}<\frac\pi5.
\]

The strict cap estimate \(J<1/10\) follows. Combining it with the audited
Round 38 estimate \(B_0\zeta>1/5\) and the nonnegative selected-scalar terms
gives

\[
 \Gamma_{\rm gap}>
 \frac{11}{10}-\frac{p-dm}{2}.
\]

Thus \(p-dm\leq11/5\) closes the selected gate. For \(p=3\), failure of this
automatic condition is exactly \(dm<4/5\), as stated.

## 2. Exact outer-face algebra and losses

On the gap-side outer wall,

\[
 v=B-\frac14,\quad B_0=v-\frac34,\quad
 \chi=h,\quad y_B=0,\quad
 \omega_B=\frac1{2\beta}-1.
\]

Substitution into the Round 38 selected normal form, together with

\[
 (p+a_p)M_4+p(\Delta-M_4)=p\Delta+a_pM_4,
\]

gives (R39.5) exactly. The action coordinates

\[
 A(x)-A(q)=j+e_p+h,
 \qquad A(x)-W=j+u+e_p=\lambda+e_p
\]

follow from the same one-sided labels. Applying the strict adjacent-action
bound to the first coordinate and the non-strict elasticity bound to the
second gives

\[
 \Gamma_{\rm OB}-F_{\rm OB}=
 p\{\Delta-R_1[A(x)-A(q)]\}
 +a_p\{M_4-g[A(x)-W]\}>0.
\]

The strictness is supplied only by the first bracket, as the note records.
The root-free substitution is also exact:

\[
 \frac{B_0(B_0+1)}2-B_0u
 =(v-\tfrac34)(W-\tfrac v2+\tfrac18),
\]

and \(K\sin t=\mu\tan t\),
\(\mu=\pi W/(\tan t-t)\) give (R39.11). This projection discards only
\(\Omega_- -\Omega_{\rm RF}\geq0\); it is not a new certificate.

Finally, if \(R_{\rm el}=\Delta-g(\lambda+e_p)\), then

\[
 \tau(E+2\lambda)=g(\lambda+e_p)+\tau R_{\rm el},
\]

so subtracting the two branches of the maximum defining \(M_4\) proves
(R39.14). No strictly positive uniform \(\widehat\Xi\)-reserve follows.

## 3. Lower-shelf floor elimination

The proof of (R39.15) is valid. With \(w=(q+1)^{-1/2}\leq1/\sqrt6\),

\[
 \pi H_{\rm ls}(q)=4\int_0^1\arcsin(w\sqrt y)\,dy.
\]

For the arcsine coefficient
\(c_n=\binom{2n}{n}/\{4^n(2n+1)\}\), \(c_n\leq1/9\) for \(n\geq4\).
This proves the printed geometric tail bound and therefore
\(\pi H_{\rm ls}<wC(w)\), with \(C\) increasing and
\(C(1/\sqrt6)=451351/166320\).

The Becker--Stark inequality follows directly from the positive partial
fractions by

\[
 \frac1{a_n-y}\leq\frac{a_1}{a_n(a_1-y)}.
\]

After substitution, every factor is monotone in the stated direction. The
endpoint denominator is positive; its exact rational lower margin is

\[
 \left(\frac{333}{106}\right)^2-
 \frac{2}{3}\left(\frac{451351}{166320}\right)^2
 =\frac{578050467307991}{116555279702400}>0.
\]

The final rational upper bound is \(<1747/1000<7/4\), proving (R39.15).

At the lower shelf, \(e_p=0\), so \(A(x)-v=j\in\mathbb Z\). The inequality
\(K>q+1\) follows because otherwise
\(v\leq G_{q+1}(q)<1/2\), while the outer label has \(v\geq7/4\). For

\[
 D(z)=G_K(z)-G_K(q)-G_{q+1}(z),
\]

one has \(D'(z)=b_{q+1}(z)-b_K(z)<0\). Since \(x\leq q-1\),

\[
 A(x)-v>D(q-1)>\beta-H_{\rm ls}(q).
\]

The outer-wall identity

\[
 v=\frac q\pi\{\tan(\pi\beta)-\pi\beta\}\geq\frac74
\]

and (R39.15) imply \(\beta>H_{\rm ls}(q)\). Thus \(j\) is a positive
integer and \(j\geq1\). No stronger analytic \(B_0\geq2\) claim is made.

## 4. Phase--stretch inequality

The stretch estimate is exact. With \(z=(m+\alpha)/p\) and \(h_r=2r/p\),

\[
 (g+1)^2=1+\frac{h_r+1}{z(z+h_r+2)}
 >1+\frac1{z(z+2)},
\]

which proves \(g>\gamma(z)\). For \(y=1+z\), differentiating

\[
 \frac{C(d,z)}{1+z}
 =\frac{3+d}{2y}-\frac d2-\frac1{\sqrt{y^2-1}}
\]

gives one critical point,
\(y^2=\ell/(\ell-1)\),
\(\ell=((3+d)/2)^{2/3}\). It is the global maximum and has value
\(\mathcal H(d)\).

The refined tangent majorant is also correct. The partial fractions give

\[
 a_n=\frac{8\,4^n}{\pi^{2n+2}}S_{2n+2}.
\]

For \(n\geq2\), \(S_{2n+2}\leq S_6=\pi^6/960\), and \(\pi^2<10\) yields

\[
 a_n<\frac{4^{n-1}}{3\pi^{2n-2}}.
\]

Coefficient comparison proves (4.6). Inverting it at \(x=\pi d/2\) gives
\(L>A_\pi-d/2\). The denominator of \(A_\pi\) is

\[
 D(\pi^2)=\pi^2(1-d^2)+\frac{\pi^4d^2}{12};
\]

\(D\) is increasing, so \(\pi<22/7\) gives \(A_\pi>A_0\) in the required
direction.

The rational majorant is sufficient. The formula for \(R''\) is correct and
decreasing, and the three printed rational comparisons prove

\[
 R(d)<U(d)=\frac{173}{1000}+\frac{61}{250}d+
 \frac{11}{250}d^2.
\]

Combining denominators gives (4.13), whose denominator is negative on
\((0,1)\). The exact Sturm sequence printed in (4.14) has three sign
variations at both endpoints and no endpoint zero; hence \(P=-N\) has no
root in \((0,1)\). Since \(P(0)>0\), the rational difference is strictly
positive. This proves \(\mathcal H(d)<k(d)L(d)\). The Sturm calculation is
one exact
polynomial check inside the analytic lemma, not a compact continuum
certificate or a chamber family.

## 5. Final lower-shelf sign

From (5.1), \(\beta<1/2\), \(J<1/7\), \(\Omega_-\geq0\),
\(\Delta\geq M_4\), \(M_4\geq g(j+u)\), \(j\geq1\), and \(u>0\) give

\[
 \Gamma_{\rm OB}>
 \frac67+B_0\zeta+(p+a_p)g-\frac{p-dm}{2}.
\]

The complete discarded reserve at this step consists of

\[
 \frac1{2\beta}-1,\quad \frac17-J,\quad \Omega_-,\quad
 p(\Delta-M_4),\quad
 (p+a_p)\{M_4-g(j+u)\},\quad
 (p+a_p)g\{(j-1)+u\}.
\]

All are nonnegative and the last is positive. Substituting
\(m=pz-\alpha\) and \(g>\gamma(z)\) gives (5.3). If \(C\leq0\), its sign is
immediate. If \(C>0\), the phase--stretch lemma gives

\[
 pC<kp(1+z)L<k\mu L=k\zeta W.
\]

The strict second inequality uses \(p(1+z)=\mu-r<\mu\). The exact count
relation \(W=B_0+3/4-u\), \(B_0\geq1\), and \(u>0\) then give

\[
 B_0-kW>1-\frac{7k}{4}.
\]

After \(\alpha<1\), the remaining lower bound has numerator

\[
 \mathcal Q(d)=108-241d+63d^2+196d^5.
\]

Its derivative is strictly increasing. At its unique critical point
\(d_*<16/25\), elimination of \(d_*^4\) gives

\[
 \mathcal Q(d_*)=
 \frac{540-964d_*+189d_*^2}{5}
 >\frac{284}{3125}>0.
\]

Thus (R39.19) is proved on the complete simultaneous one-sided endpoint.
The sign split of the single continuous expression \(C(d,z)\) introduces no
ratio, count, floor, or chamber-indexed theorem family.

## 6. Ownership, equality faces, and theorem boundary

The outer-\(B\) label is correctly one-sided: the literal strict bracket at
\(v+1/4=B\) is \(B-1\), while the gap-side limit retains \(B^+=B\). The
newest inverse displacement is \(y_B=0\) and is not counted as an old inverse
jump. The lower-shelf equality owns \(e_p=0\) only on its inherited
one-sided action face. The literal \(\alpha=0\) point remains the separate
equal-count corner, and \(\alpha\uparrow1^-\) is not relabelled as the next
chart. Round 38 excludes finite integer-\(\lambda\) walls in the positive
\(\alpha\) gap.

The loss hierarchy remains

\[
 D_A(r)\geq\mathscr S\geq\Phi_\delta^+\geq\Gamma_{\rm gap}.
\]

Only the last displayed projection reserve is identified exactly as
\(a_p\widehat\Xi\geq0\); inherited shelf, terminal, and tangent losses are
not called identities. The live state files consistently leave the selected
high-floor CST obligation, the frozen branching-backbone audit, pointwise
assembly, and the all-dimensional theorem open.

## 7. Computational and state validation

The Mathematica replay was rerun on Windows with Mathematica 15:

`wolframscript.exe -file computations/general_d_round39_outer_face_replay.wl`

It returned zero for every exact outer-face, action-coordinate, loss,
root-free, elasticity, cap, coefficient, rational, Sturm, and final-residual
check. The Sturm variation counts were `{3,3}`, the exact root count was
zero, and the run ended with

`round39OuterFaceReplayOK=True`.

Both documented diagnostics were rerun:

- `python -B computations/general_d_round39_outer_face_diagnostic.py`
- `python -B computations/general_d_round39_outer_face_diagnostic.py --high-floor-stress --skip-high-precision`

The default run reproduced 191,360 tuples, 406 feasible upper-face roots,
89 feasible lower-shelf roots, and lower-floor counts `{1: 88, 2: 1}`. The
100-decimal replay is explicitly noninterval and noncertifying. The stress
run reproduced 6,167 feasible upper and 21,121 feasible lower roots. It found
the documented negative coarse \(C_{\rm curv}\) and \(L_j\) samples, while
finding no sampled negative root-free intrinsic bound. Every output is
labelled `diagnostic_only`; no sampled minimum is used above.

The graph validator passes, the active reading-packet paths resolve, and the
Round 39 live-state edits preserve the same local theorem boundary. The
authoritative graph hash is unchanged.

## 8. Gate A/B/C conclusion

The revised strategy is followed. Gate A remains active only for one
intrinsic continuous sign on the one-sided upper-\(\alpha\) outer-\(B\)
endpoint, through \(F_{\rm OB}\) or its root-free projection while retaining
the exact cap, phase, old inverse payment, shelf excess, and elasticity
reserve. The failed coarse \(C_{\rm curv}\) and \(L_j\) reductions are not
valid owners.

If the remaining endpoint sign is certified false or requires a forbidden
ratio/count/chamber family, Gate A stops. Gate B then restores
\(\mathscr S\) with its exact shelf, terminal, cap, and inverse terms. Gate C
is activated only under the strategy's stated exact-scalar stop conditions.
No new compact certificate is authorized, and no high-floor CST or
all-dimensional theorem promotion follows from Round 39.
