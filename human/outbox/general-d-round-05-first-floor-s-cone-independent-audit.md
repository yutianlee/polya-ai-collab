# Independent audit: ordinary first-floor \(s\geq2\) cone

Date: 18 July 2026

## Final verdict on the revised hashes

**PASS.**  The revised proof note and unchanged directed-rounding verifier
prove the true-interface certificate on the closed universal active region

\[
 K-\mu\geq\pi
 \quad\Longleftrightarrow\quad
 3(1-\rho)\geq4\pi w.
\]

The note now explicitly assigns the complementary below-active spectral
region to the no-mode theorem and does not claim a standalone shifted-tail
certificate there.  This is exactly the scope proved by the argument.  I
found no mathematical, topological, interval-certification, strict-wall, or
grid-coverage gap in that scope.

Audited SHA-256 digests:

```text
955578A4EB5E7787CAA20A47C2254C5E1846EE688AA4D563BF4AD41AD6F427AC
  human/outbox/general-d-round-05-first-floor-s-cone.md

D5BC93C60128AB23615720244AC6AD1FA88277B5EDFB98930E8BB22BEC23AE53
  scripts/general_d_first_floor_s_cone_verify.py
```

## 1. True-interface certificate and direction

On \(A(x)=3/4\), split the continuous tail at

\[
 r< x=r+p<q=x+s+1<\mu=q+\alpha<K.
\]

The shell action is concave on \([r,\mu]\).  Hence the three chord
trapezoids give

\[
\begin{aligned}
2\int_r^xA&\geq p\bigl(A(r)+A(x)\bigr),\\
2\int_x^qA&\geq(s+1)\bigl(A(x)+A(q)\bigr),\\
2\int_q^\mu A&\geq\alpha\bigl(A(q)+A(\mu)\bigr).
\end{aligned}
\]

On \([\mu,K]\), \(A=G_K\) is convex.  Its tangent at \(\mu\) is
\(h-c(z-\mu)\); convexity and \(G_K(K)=0\) imply \(h/c\leq K-\mu\), so

\[
 2\int_\mu^KG_K(z)\,dz\geq h^2/c.
\]

Immediately after the ordinary wall, the complete strict tail count is
(1+2p).  It is smaller at the wall itself.  Therefore

\[
 \mathcal C\leq D_A(r)
\]

for the post-crossing value, and the same lower bound is wall-safe.  For
fixed \((\mu,r,p,s,\alpha)\), every action term increases with \(K\).  Also,
if \(\theta=\arccos(\mu/K)\), then

\[
 \frac{h^2}{c}=\frac{\mu^2}{\pi}
 \frac{(\tan\theta-\theta)^2}{\theta}
\]

increases with \(\theta\), because

\[
 2\theta\tan^2\theta-(\tan\theta-\theta)>0.
\]

Thus the post-crossing wall is indeed the chamber minimum.  The direction
of the certificate is correct: proving \(\mathcal C>0\) proves
\(D_A(r)>0\).

## 2. Concavity compression and scale-free reduction

With

\[
 \beta=s+1+\alpha=\mu-x,
\]

the point \(q\) divides \([x,\mu]\) in weights \(\alpha\) and \(s+1\).
Concavity gives

\[
 \beta A(q)\geq\alpha A(x)+(s+1)A(\mu).
\]

Substitution into the two middle trapezoids yields exactly

\[
 \mathcal C\geq
 p\left(a-\frac54\right)
 +\beta\left(\frac34+h\right)+\frac{h^2}{c}-1.
\]

For

\[
 \rho=\mu/K,\quad \xi=x/K,\quad \eta=r/K,
 \quad e=\rho-\xi,\quad \epsilon=1-\rho,
\]

the wall identity is (Kw=3/4).  Consequently

\[
 K=\frac3{4w},\quad
 \beta=\frac{3e}{4w},\quad
 p=\frac{3(\xi-\eta)}{4w},\quad
 h=\frac{3g(\rho)}{4w}.
\]

These substitutions and the (p)-term estimate below give

\[
 \frac{16w^2}{9}\mathcal C\geq J_2,
\]

where

\[
 J_2=w\left(\frac e3-\frac{2\epsilon}3\right)
     +e g(\rho)+\frac{g(\rho)^2}{c}-\frac{16}{9}w^2.
\]

The algebra and inequality direction agree with the code.

## 3. Independent check of the \(\eta\)-minimization

The radius-profile ratio is decreasing in the integration radius, so

\[
 a\geq\frac34
 \sqrt{\frac{1-\eta^2}{1-\xi^2}}=\frac34Q.
\]

Put \(D=(\xi-\eta)/(1-\xi)\).  The constraint \(\eta\geq0\) implies

\[
 Q\geq\frac{D+1}{\sqrt{2D+1}}.
\]

For \(D\leq2/5\), the desired global comparison follows from \(5D\leq2\).
For \(D\geq2/5\), both sides of the comparison to be squared are
nonnegative, and squaring gives

\[
 9D^4-32D^3+24D^2+12D-4>0.
\]

The script converts this polynomial exactly to Bernstein form on the six
listed rational panels.  Its conversion formula is the correct
power-to-Bernstein formula.  The tail \(D\geq4\) splits into
\(D^3(9D-32)+(24D^2+12D-4)>0\).  Therefore

\[
 (\xi-\eta)(3Q-5)\geq-2(1-\xi).
\]

For the local bound, if \(\xi\geq9/10\) and \(Q<5/3\), then
\(\eta>2/3\) and

\[
 Q^2
 =1+D\frac{\xi+\eta}{1+\xi}
 >1+\frac45D.
\]

The case \(D\leq1/5\) is immediate.  Squaring for \(D\geq1/5\) gives

\[
 \frac{36}{5}D^3-16D^2+10D-1>0.
\]

The exact Bernstein panels and the \(D\geq3\) tail in the script are
correct.  Hence

\[
 (\xi-\eta)(3Q-5)\geq-(1-\xi)
 \qquad(\xi\geq9/10).
\]

## 4. Domain reductions and analytic pieces

At fixed \(\rho\), \(w(t)\) is increasing and concave,
\(w(0)=g(\rho)>0\), and therefore \(w(t)/t\) is decreasing.  At the
physical endpoint \(\xi=0\),

\[
 \frac{w(t)}t=\frac{\epsilon^2}{\pi\rho}.
\]

This is \(>\epsilon/4\) for \(\rho\leq11/20\), which contradicts
\(e\geq4w\).  On \(11/20\leq\rho\leq39/50\), the 4096-panel directed Arb
check at \(t_0=3/\pi\) proves

\[
 w(t_0)>\frac{3\epsilon}{4\pi}.
\]

For \(t\leq t_0\), decreasing \(w/t\) contradicts \(e\geq4w\); for
\(t\geq t_0\), increasing \(w\) contradicts the active inequality.
Thus every simultaneous active, \(\beta\geq3\) point has
\(\rho>39/50\).  The second domain reduction follows directly from

\[
 w\geq\frac\epsilon\pi\sqrt{1-(\xi/\rho)^2}
 \quad\hbox{and}\quad
 w\leq\frac{3\epsilon}{4\pi}.
\]

For \(t\geq4\), the active bound gives

\[
 J_2\geq\epsilon w
 \left(\frac23-\frac4{3\pi}\right)>0.
\]

For \(\rho>49/50\) and \(t<4\), one has \(\xi>9/10\), so the local
\(J_1\) bound applies.  The three estimates

\[
 g(\rho)\geq G_0\epsilon^{3/2},\qquad
 \frac{g(\rho)}c\geq H_0\epsilon,\qquad
 w\leq B_0L(t)\epsilon^{3/2}
\]

follow from the radius integral,
\(\tan\theta/\theta-1\geq\theta^2/3\), and direct integration of the
upper square-root profile.  On \(0\leq t\leq1/2\),
\((1-2t)L(t)\leq1\); differentiating verifies it decreases from one.
On \(1/2\leq t<4\), the linear \(w\)-term is nonnegative.  The two
resulting constants in the script are therefore valid lower margins, not
numerical heuristics.

## 5. Moving boundaries, topology, and interval hulls

At fixed \(\rho\), differentiating with respect to \(e\) gives

\[
 w_e=\chi(\xi)-\chi(\xi/\rho)>0,
\qquad
 w_{ee}=\frac1{\pi\sqrt{1-\xi^2}}
 -\frac1{\pi\sqrt{\rho^2-\xi^2}}<0.
\]

Thus (F(e)=e-4w(e)) is strictly convex and (F(0)<0).  Once a positive
right endpoint is certified, its nonpositive set is one initial interval,
so the beta-entry root is unique and

\[
 e\geq4w\quad\Longleftrightarrow\quad e\geq e_\beta.
\]

At that root, substituting (w=e/4) before interval evaluation gives the
correct formula

\[
 J_b=\frac{g^2}{c}+eg-\frac{\epsilon e}{6}-\frac{e^2}{36}.
\]

Also

\[
 J_2'=w_e\left(\frac e3-\frac{2\epsilon}3-\frac{32w}{9}\right)
       +\frac w3+g.
\]

Concavity gives \(0<w_e\leq(w-g)/e\).  With \(z=g/w\in(0,1)\), the
displayed lower bound

\[
 \frac{J_2'}w\geq
 \frac13+z+(1-z)\min(0,X)
\]

is valid in both signs of (X).

The rectangle hulls in `rt_hulls` are valid.  Indeed, at fixed \(t\),
\(w\) decreases with \(\rho\): in the radius-integral representation, both
raising the lower endpoint and raising \(\xi=(1+t)\rho-t\) decrease the
integral.  At fixed \(\rho\), \(w\) increases with \(t\).  The endpoint
unions used by the code therefore enclose all values.  The same endpoint
order is correct for \(g(\rho)\) and \(c(\rho)\).

The two-stage beta bisection retains a common certainly-negative left
endpoint and a common certainly-positive right endpoint, hence encloses
every beta root on each \(\rho\)-panel.  The active function is strictly
decreasing in (t), so its analogous upper-root bisection is safe.  For
\(\rho\geq4/5\), using \(t\leq4\) deliberately overcovers the active set.
The exact split at \(\rho=4/5\) preserves physicality.  Positivity of
\(J_b\), followed by positivity of the normalized derivative on the whole
accepted interval, propagates \(J_2>0\) from the moving beta wall to the
active endpoint.

All sign decisions are Arb or exact `fmpq` decisions.  Binary floating
point is used only for reported diagnostics.

## 6. Replay results

I ran the unmodified verifier with python-flint 0.8.0 at 256, 384, and 512
bits.  All three exited with code zero and reported the same topology:

```text
rho-panels=507, rho-splits=253, empty=0, positive=254
derivative-boxes=2422, max-rho-depth=12, max-t-depth=5
```

The certified lower endpoints remained strictly positive:

| precision | smallest boundary lower endpoint | smallest derivative lower endpoint |
|---:|---:|---:|
| 256 | \(5.57124699231\times10^{-9}\) | \(0.0010973528439\) |
| 384 | \(5.57124666798\times10^{-9}\) | \(0.0010973528439\) |
| 512 | \(5.57124693441\times10^{-9}\) | \(0.0010973528439\) |

The small variation is only in printed binary-float diagnostics; every
accept/reject decision is directed-rounding.

## 7. Initial correction request (historical)

This section records why PASS was withheld from the old note hash.  Both
items were corrected before the final re-audit in Section 8.

### 7.1 Forbidden control bytes in the old hash

The old Markdown note contained two byte `0x0C` form feeds:

```text
byte 4336, line 243:  intended `\frac{4}{9}`
byte 5830, line 321:  intended `\frac{\epsilon}{4}`
```

The verifier contained no forbidden control byte.  Correcting these two
bytes and regenerating the note hash was required.

### 7.2 Active-region scope in the old hash

The proof uses the active constraint essentially in the low-\(\rho\)
exclusion, the \(u\)-lower bound, the \(t\geq4\) estimate, and the active
upper-root cutoff.  It proves

\[
 \mathcal C>0
 \quad\text{for}\quad
 \beta\geq3,\qquad K-\mu\geq\pi.
\]

The old hash did **not** justify the standalone statement for every
below-active point \(K-\mu<\pi\).  Its unqualified phrases "full continuous
... cone" and "no residual within this cone" therefore had to be restricted
to the universal active region.  Closure of the full first-floor branch
needed for the spectral theorem also had to cite the no-mode result for
\(K-\mu\leq\pi\).  No mathematical change to the active certificate was
needed.

## 8. Final re-audit of the corrected hash

Both defects are corrected in note hash
`955578A4EB5E7787CAA20A47C2254C5E1846EE688AA4D563BF4AD41AD6F427AC`.
The two intended fractions are ordinary text with no control bytes.  The
opening scope now includes \(K-\mu\geq\pi\); the conclusion restricts
\(\mathcal C>0\) to that active cone, combines the result with the no-mode
theorem below the active wall, and expressly declines a standalone
below-active shifted-tail claim.

A fresh UTF-8 scan found zero forbidden control bytes and zero U+FFFD
replacement characters in both revised artifacts.  Fresh independent
256-, 384-, and 512-bit replays exited zero with identical subdivision
topology and the positive margins recorded in Section 6.

**Final verdict: PASS.**
