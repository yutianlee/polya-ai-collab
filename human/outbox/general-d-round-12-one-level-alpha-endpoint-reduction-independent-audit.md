# Independent audit: Round 12 alpha-endpoint reduction

Date: 18 July 2026

Audited source:

`human/outbox/general-d-round-12-one-level-alpha-endpoint-reduction.md`

Audited SHA-256:

`4C06CAD33A514A13C6114BE919D96BABF884AD8A91096BC0A84896E321982BB9`

Post-audit integrated source SHA-256:

`C07FB5228715C1A595878092C81387621AB0C87241AB2576FFE80753C6A29EA9`

The integrated source differs from the frozen target only by applying the two
nonblocking corrections in Section 8 and its optional owner-wall wording
refinement.  No endpoint formula or comparison was changed.

Diagnostic evaluator replayed:

`computations/general_d_round12_alpha_endpoint_probe.wl`

Evaluator SHA-256:

`D08DB0B80F837B154F32928DD70E9F86C6624B6757F98857BE4F40B99C6F9062`

## 1. Verdict

**PASS, with the two nonblocking source corrections in Section 8.**

The alpha-endpoint reduction is mathematically valid on the stated
extension-grid domain.  In particular:

1. the open-side scalar (1.8)--(1.9) is exactly the open-phase specialization
   of Round 11, equation (4.5);
2. its dependence on the interface displacement is strictly decreasing;
3. the phase, branch, and owner-dimensional activity endpoints in
   (3.1)--(3.5) are the correct first endpoints;
4. the comparison direction in (3.6) is correct even when the artificial
   endpoint crosses a shelf or no-drop wall;
5. the literal lower-action wall is strictly more favorable than the
   open-side limit;
6. the elimination formulas (3.9)--(3.10) are exact; and
7. the deterministic Mathematica replay reproduces the reported count,
   minimum, and endpoint ordering.

This verdict certifies only Proposition 1.1 and the reduction to (3.11).
It does **not** prove the endpoint sign (3.11), close the remaining
\(B=1\) sector, or prove the general-dimensional theorem.

## 2. Domain and invariant audit

The source correctly restricts the new obligations to

\[
 r\in\mathbb N,\quad r\geq1,
 \qquad\text{or}\qquad
 r\in\mathbb N_0+\frac12,\quad r\geq\frac32.
\]

The smallest new owner dimensions are \(d_{\rm own}=4\) and
\(d_{\rm own}=5\), respectively.  Proving the scalar on the corresponding
owner-active region is conservative for every higher dimension with the
same parity: the additive activity constant

\[
 \kappa_d=\frac{(d-2)^2-1}{4}
\]

increases with \(d\), so the higher-dimensional active region is a subset
of the owner-active region.  The excluded \(r=1/2\) line is owned by the
completed three-dimensional theorem, exactly as in Round 11.

For \(B=[v+1/4]_< =1\), strict counting gives

\[
 \frac34<v\leq\frac74.
\]

Consequently \(q<K\), \(\beta>0\), and the equation

\[
 \frac K\pi\Phi(\theta)=\frac34
\]

has the unique outer inverse-level angle used in the note.  Since
\(G_K(q)=v>3/4\), its crossing point \(z=K\cos\theta\) satisfies
\(z>q\).  Thus \(y=z-q>0\), and

\[
 \eta=y-[y]_<\in(0,1]
\]

has the correct literal value \(1\) when \(y\) is an integer.

With the outer data fixed and \(\mu=q+\alpha\), the open phase is

\[
 \varepsilon(\alpha)=v-h(\alpha)-\frac34>0.
\]

Therefore every original open-phase point lies strictly below the phase
endpoint \(\alpha_*\), below the branch endpoint \(1\), and, by strict
activity, below \(\alpha_{\rm act}\).  This is the exact fact needed for
the minimum endpoint in (3.5).

## 3. Open scalar and monotonicity

On the open side, the Round 11 wall table gives
\((Q,\chi_q)=(1,0)\).  Substituting

\[
 \lambda=\frac{K-q-\alpha}{\pi},
 \qquad
 2\delta\leq\alpha h
\]

into Round 11 (4.4)--(4.5) gives exactly

\[
 \Psi^{\rm op}(\alpha)
 =\max\{0,L^{\rm op}(\alpha)\}
 -\frac n2+C_{r,n}\left(\lambda(\alpha)-\frac34\right),
\]

where

\[
 C_{r,n}=
 \left(n+\frac{n^2}{3(2r+n)}\right)\frac{2n}{r+2n}>0
\]

and

\[
 L^{\rm op}(\alpha)=
 \frac\pi{2\theta}+2\eta-1-\alpha h(\alpha)
 +\frac{(v-1)_+^2}{\beta}.
\]

No term, sign, or factor from Round 11 is missing.

Direct differentiation of

\[
 G_a(q)=\frac{\sqrt{a^2-q^2}-q\arccos(q/a)}\pi
\]

with \(a=q+\alpha\) gives

\[
 h'(\alpha)
 =\frac{\sqrt{(q+\alpha)^2-q^2}}{\pi(q+\alpha)}.
\]

This is positive for \(\alpha>0\), while \(h(0)=0\).  Hence
\(\alpha h(\alpha)\) is strictly increasing on \([0,\infty)\), and
\(L^{\rm op}\) is strictly decreasing there.  Also

\[
 \frac{d}{d\alpha}
 \left[-\frac n2+C_{r,n}
 \left(\lambda(\alpha)-\frac34\right)\right]
 =-\frac{C_{r,n}}\pi<0.
\]

Since \(x\mapsto\max(0,x)\) is nondecreasing, its composition with the
decreasing \(L^{\rm op}\) is nonincreasing.  Adding the strictly decreasing
affine term proves strict decrease of \(\Psi^{\rm op}\), including through
a zero of \(L^{\rm op}\).  This argument does not differentiate the
nonsmooth maximum at its kink.

## 4. Phase and activity endpoints

The phase wall is exactly

\[
 h(\alpha_*)=v-\frac34.
\]

It has a unique positive solution because \(v>3/4\), \(h(0)=0\), and
\(h\) is strictly increasing and unbounded.  In fact the root stays inside
the shell ordering: at \(\alpha=K-q\),

\[
 h(K-q)=G_K(q)=v>v-\frac34,
\]

so \(0<\alpha_*<K-q\).  The first phase/branch endpoint is therefore
correctly \(\bar\alpha_{\rm ph}=\min\{1,\alpha_*\}\).

For the owner dimension, substitute
\(\rho=(q+\alpha)/K\) into the strict activity condition:

\[
 K^2>\frac{\pi^2}{(1-\rho)^2}+\kappa_{d_{\rm own}}.
\]

Because an active point has \(K^2>\kappa_{d_{\rm own}}\) and
\(K-q-\alpha>0\), taking positive square roots is legitimate and gives

\[
 K-q-\alpha>
 \frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}},
\]

or exactly

\[
 \alpha<\alpha_{\rm act}:=
 K-q-\frac{\pi K}{\sqrt{K^2-\kappa_{d_{\rm own}}}}.
\]

An existing active point satisfies \(0\leq\alpha<\alpha_{\rm act}\), so
every nonempty active chamber has \(\alpha_{\rm act}>0\).

Thus

\[
 \bar\alpha=
 \min\{\bar\alpha_{\rm ph},\alpha_{\rm act}\}
\]

is the first of the phase, branch, and strict activity endpoints.  Every
original open point satisfies \(\alpha<\bar\alpha\).  Strict decrease and
continuity therefore give

\[
 \Psi^{\rm op}(\alpha)>
 \Psi^{\rm op}(\bar\alpha)=\Psi_{\rm end};
\]

the source's weaker displayed \(\geq\) is valid.  If the activity wall is
first, its value is a limiting value only, which is sufficient because the
original activity inequality is strict.

The optional phase-only comparison also has the correct direction.  Since
\(\bar\alpha\leq\bar\alpha_{\rm ph}\) and \(\Psi^{\rm op}\) decreases,

\[
 \Psi_{\rm end}
 \geq\Psi^{\rm op}(\bar\alpha_{\rm ph}).
\]

## 5. Literal lower wall and other equality faces

At a literal lower-noncorner wall, \(\varepsilon=0\) and \(h>0\), so
\(\alpha=\alpha_*<1\).  Activity of that literal point gives
\(\alpha_*<\alpha_{\rm act}\), hence \(\bar\alpha=\alpha_*\).  The strict
bracket changes from \(Q=1\) to \(Q=0\), while the no-drop endpoint bonus
changes from \(\chi_q=0\) to \(\chi_q=1\).  If
\(x=L^{\rm op}(\alpha_*)\), the literal value exceeds the open limit by

\[
 \max(0,x+1)-\max(0,x)+1\geq1.
\]

Thus the claimed strict improvement is correct in every sign regime of
\(x\).

The remaining wall bookkeeping is also correct:

- \(\alpha=1\) is used only as the limit \(\alpha\uparrow1\), before the
  integer \(n\) is changed;
- the activity equality is used only as a limit;
- an integral inverse displacement has \(\eta=1\), not \(0\);
- a vertical action equality is evaluated by the literal strict bracket;
- \(v=3/4\) belongs to \(B=0\), not \(B=1\);
- ordinary shelf-floor equalities retain zero remainder;
- at \(q=\mu\), the inner cap vanishes; and
- a sample at \(K\) is absent from the strict count.

Moving the explicit scalar through an intermediate shelf or no-drop wall
does not require the endpoint to be an admissible tail.  The proof compares
two values of one algebraic function whose monotonicity is already
established; it does not reapply Round 11 at the artificial endpoint.

## 6. Variable elimination

The inverse-level relation gives

\[
 K=\frac{3\pi}{4\Phi(\theta)}.
\]

Since \(y=K\cos\theta-q\), one obtains

\[
 q=\frac{3\pi\cos\theta}{4\Phi(\theta)}-y,
 \qquad r=q-n.
\]

Finally,

\[
 \begin{aligned}
 \lambda(\alpha)
 &=\frac{K-q-\alpha}{\pi}\\
 &=\frac{3(1-\cos\theta)}{4\Phi(\theta)}
   +\frac{y-\alpha}{\pi},
 \end{aligned}
\]

which is exactly (3.10).  Once the grid identity \(q=r+n\), the first-floor
constraints, and the piecewise strict fraction of \(y\) are retained, the
remaining variables are indeed \((\theta,y,n)\).  The endpoint sign (3.11)
is therefore one scalar analytic target rather than a new ratio partition.

## 7. Mathematica replay

The supplied evaluator was replayed with Wolfram 15.0 for Windows using

```powershell
& 'C:\Program Files\Wolfram Research\Wolfram\15.0\SystemFiles\Kernel\Binaries\Windows-x86-64\wolframscript.exe' `
  -noprompt -run '<<computations/general_d_round12_alpha_endpoint_probe.wl;Quit[]'
```

It reproduced:

\[
 \#\{\text{hard extension-grid records}\}=3171,
 \qquad
 \#\{\Psi_{\rm end}<0\}=0,
\]

and

\[
 \min\Psi_{\rm end}
 =0.03954098598463273226158050782375868317\ldots.
\]

The minimizing sampled record was

\[
 r=1,\quad n=2,\quad q=3,
\]

\[
 \rho=0.4858684362777584728571\ldots,
 \qquad
 K=6.3884642054618210970572\ldots,
\]

with

\[
 \alpha_*=0.1729452229494133315763\ldots
 <\alpha_{\rm act}=0.2176014046026202632723\ldots.
\]

The phase-only and sharp endpoint values coincide at that record, and the
script printed `round12ReplayOK=True`.  The script implements the formulas
in the note literally: its root is the phase root, its activity expression
is (3.4), and its scalar retains \(2\eta\), the top square, and the full
active-width coefficient \(C_{r,n}\).

The replay is deterministic high-precision falsification evidence, not an
interval enclosure.  The source labels it accordingly, and no analytic
claim depends on the absence of a sampled negative.  The final
WolframScript configuration-file warning occurred after successful kernel
output and did not affect `round12ReplayOK=True`.

## 8. Exact nonblocking corrections

Neither item changes Proposition 1.1 or any endpoint formula.

1. **Boundary sign in (2.4).**  The displayed strict inequality
   \(-h(\alpha)-\alpha h'(\alpha)<0\) holds for \(\alpha>0\).  At
   \(\alpha=0\), both terms vanish, so the derivative is \(0\).  The text
   introduces the calculation with “For \(\alpha>0\),” and the proof of
   strict decrease remains valid because the affine term has derivative
   \(-C_{r,n}/\pi<0\) everywhere.  For maximal literalness, write
   \(L'(\alpha)\leq0\) on \([0,\infty)\), with strict inequality for
   \(\alpha>0\).

2. **Typesetting in (3.5).**  The source has
   `\bar\alpha=min\{...\}`.  This should be
   `\bar\alpha=\min\{...\}`.  The surrounding prose and the Mathematica
   implementation both use the intended minimum, so this is only a TeX
   typo.

One wording refinement is optional: (3.4) uses the **uniform
owner-dimensional** activity wall.  In an actual dimension larger than the
owner dimension, the dimension-specific wall is stronger.  The owner wall
is deliberately conservative and is sufficient for the all-dimensional
extension-grid obligation.

## 9. Final disposition

- Extension-grid and owner-dimensional scope: **PASS**.
- Open scalar specialization of Round 11: **PASS**.
- Derivative and monotonicity calculation: **PASS**.
- Phase, branch, and activity endpoints: **PASS**.
- Strict-wall and lower-noncorner ownership: **PASS**.
- Elimination to \((\theta,y,n)\): **PASS**.
- Mathematica counts and minimum: **reproduced; PASS as diagnostics**.
- Endpoint sign (3.11): **still open, exactly as the source states**.

After this audit was frozen, the two exact corrections in Section 8 and the
owner-dimensional wording refinement were applied to the integrated Round-12
source; the hashes above distinguish the frozen and corrected files.
