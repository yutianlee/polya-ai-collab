# Clean-room audit of `compact-angular-block.tex`

## Verdict: PASS

I reconstructed the arguments singled out for audit and found no gap in the
one-layer estimate, the strict common-wall convention, the summation over
radial blocks, the inverse-area computation, or the conditional reduction to
the scalar inequality \(\mathcal S>0\).

This verdict is deliberately local: it verifies the deductions made in this
note.  It does **not** verify the imported structural implication
\(\mathcal E_{\rm ang}<\mathcal H\Rightarrow P<W\), and it does not prove the
still-open scalar inequality \(\mathcal S>0\).

## 1. Basic inverse and speed bound

For \(0<z<\rho K\), differentiation gives

\[
 q(z)=\frac1\pi\left(\arccos\frac zK-
                  \arccos\frac z{\rho K}\right),
\]

and for \(\rho K\le z<K\),

\[
 q(z)=\frac1\pi\arccos\frac zK.
\]

Thus \(q(z)>0\) for \(0<z<K\), while \(q(0)=0\).  Consequently
\(A'=-q\) and \(A\) is strictly decreasing on \([0,K]\), despite the
single zero derivative at the left endpoint.  Hence its decreasing inverse
\(R:[0,T]\to[0,K]\) is well defined and continuous.

Also \(q\le 1/2\): on the inner interval the first arccosine is at most
\(\pi/2\) and the second is nonnegative; on the outer interval
\(\arccos(z/K)\le\pi/2\).  This is the only quantitative fact about \(q\)
needed by the paired-block proof.

## 2. Strict common-wall handling

The definition

\[
 M(r)=\max\{0,\lceil r-1/2\rceil\}
\]

indeed gives \(M(m+1/2)=m\).  As \(t\) increases through
\(t_0=A(m+1/2)\), the decreasing function \(R(t)\) crosses the wall from
the side \(r>m+1/2\) to the side \(r<m+1/2\).  The value at the wall is
therefore the post-crossing value, so \(h=e\circ R\) is right-continuous.
An atom of the right-continuous counting function \(C\) consequently samples
the intended strict value.

The Stieltjes identity is also consistent at simultaneous jumps.  For
right-continuous bounded-variation functions, the convention used in the
note is

\[
 \int_{(0,T]} h\,dp+\int_{(0,T]}p^-\,dh=[hp]_0^T.
\]

The first integral uses the right value of \(h\), and the second uses the
left value of \(p\); this already includes the product of simultaneous jump
increments.  There is no atom of \(C\) at \(T\), because active samples obey
\(x_n<T\).  Moreover, \(p(0)=0\) and \(h(T)=e(R(T))=e(0)=0\), so the boundary
term vanishes.  At an active sample \(t=x_n=n-1/4\), all \(n-1\) earlier
samples are active, and

\[
 p(x_n^-)=C(x_n^-)-x_n=(n-1)-(n-1/4)=-3/4.
\]

Thus the common-jump formula and the stated \(-3/4\) left value are correct.

The function \(h\) is of bounded variation: \(e\) has only finitely many
walls on \([0,K]\), is smooth between them, and composition with the
monotone continuous map \(R\) preserves this finite-variation structure.

## 3. Reconstruction of the one-layer block estimate

Fix an active \(n\), so \(x_n<T\), and take
\(t\in[n-1,x_n]\).  This interval lies in \([0,T]\), since
\(0\le n-1<x_n<T\).  Put \(z=R(t)\).  Monotonicity of \(R\) gives
\(z\ge r_n=R(x_n)\), and

\[
 x_n-t=A(r_n)-A(z)=\int_{r_n}^{z}q(s)\,ds
            \le \frac{z-r_n}{2}.
\]

Therefore

\[
 R(t)=z\ge r_n+2(x_n-t).
\]

Integrating over a block of length \(3/4\) gives

\[
 \int_{n-1}^{x_n}R(t)\,dt
 \ge \frac34r_n+
     \int_{n-1}^{x_n}2(x_n-t)\,dt
 =\frac34r_n+\frac9{16},
\]

which rearranges to

\[
 r_n\le \frac43\int_{n-1}^{x_n}R(t)\,dt-\frac34.
\]

For the rounding term, the ceiling convention gives, for every \(r_n\ge0\),

\[
 m_n<r_n+\frac12.
\]

This remains strict when \(r_n\) is a half-integer, because the wall itself
uses the lower value.  Both sides are nonnegative, so squaring is legitimate:

\[
 m_n^2-r_n^2<r_n+\frac14.
\]

Hence the one-layer lemma, including its behavior at a radial--angular common
wall, is valid.

## 4. Summation over disjoint blocks

The blocks are

\[
 B_n=[n-1,n-1/4].
\]

Each \(B_n\subset[0,T]\) for active \(n\), and consecutive blocks are
separated by the unused interval \((n-1/4,n)\); hence they are pairwise
disjoint.  Combining the two one-layer estimates yields

\[
 m_n^2-r_n^2
 <\frac43\int_{B_n}R(t)\,dt-\frac12.
\]

Since the number of active samples is finite, summing preserves strictness:

\[
 \mathcal E_{\rm ang}
 <\frac43\sum_{n=1}^N\int_{B_n}R(t)\,dt-\frac N2
 \le\frac43\int_0^T R(t)\,dt-\frac N2.
\]

No endpoint overlap or omitted common-wall term occurs in this argument.

## 5. Inverse-area identity and exact area

For a continuous decreasing inverse, the subgraph identity gives

\[
 \int_0^T R(t)\,dt=\int_0^K A(z)\,dz.
\]

One direct verification is that, for fixed \(z\in(0,K)\),
\(R(t)>z\) exactly when \(0<t<A(z)\); integrating this indicator in the two
orders gives the displayed equality.  Endpoint choices have measure zero.

Scaling \(z=as\) gives

\[
 \int_0^aG_a(z)\,dz
 =\frac{a^2}{\pi}\left(
      \int_0^1\sqrt{1-s^2}\,ds-
      \int_0^1s\arccos s\,ds\right)
 =\frac{a^2}{8}.
\]

Therefore

\[
 \int_0^T R(t)\,dt
 =\int_0^K\bigl(G_K(z)-G_{\rho K}(z)\bigr)\,dz
 =\frac{(1-\rho^2)K^2}{8},
\]

and consequently

\[
 \mathcal E_{\rm ang}
 <\frac{(1-\rho^2)K^2}{6}-\frac N2.
\]

## 6. Reduction to \(\mathcal S>0\)

On the stated compact superset,

\[
 T\ge\frac{(1-\rho)k_{11}(\rho)}\pi
  =\sqrt{1+\frac{132(1-\rho)^2}{\pi^2}}>1,
\]

because \(\rho<1\).  In particular \(x_1=3/4<T\), so \(N\ge1\).  Hence

\[
 \mathcal E_{\rm ang}
 <B(\rho,K):=\frac{(1-\rho^2)K^2}{6}-\frac12.
\]

If

\[
 \mathcal S(\rho,K)=\mathcal H(\rho,K)-B(\rho,K)>0,
\]

then \(\mathcal H>B>\mathcal E_{\rm ang}\), and the imported structural
implication gives \(P<W\).  Thus the reduction to \(\mathcal S>0\) is
logically correct.

The coefficient in the expanded form is also correct:

\[
 \frac{\rho^2K^2}{4}-\frac{(1-\rho^2)K^2}{6}
 =\frac{(5\rho^2-2)K^2}{12}.
\]

Finally,

\[
 \frac{u(1+u)}{(1+2u)^2}
 =\frac14-\frac1{4(1+2u)^2}
\]

turns the integral term into

\[
 \frac{(1-\rho^2)K^2}{4}
 -\frac12\int_{\rho K}^{K}\frac{z}{(1+2A(z))^2}\,dz,
\]

and combining its quadratic contribution with
\((5\rho^2-2)K^2/12\) gives
\((1+2\rho^2)K^2/12\), as claimed in the loss form.

## 7. Scope of what remains

The common-jump identity is correct but is not needed to obtain the global
paired-block bound; the direct one-layer proof already respects the strict
wall convention pointwise.  The analytic compact closure nevertheless
remains incomplete until a separate argument proves
\(\mathcal S(\rho,K)>0\) uniformly on \(\mathcal R_{\rm c}\).  The present
note explicitly acknowledges that remaining obligation.
