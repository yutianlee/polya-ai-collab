# A3 Domain-Scope Addendum for Round 21 Exact-D20 Closure

Verdict: **PASS. First issue: none.**

The replacement candidate correctly repairs the ratio domain of the
$k_{11}(\rho)>12$ guard.  The old unqualified assertion for every
$\rho\geq\rho_c$ is false and is rejected chronology.  With the necessary
upper wall $\rho<1$, the guard is exact and every use needed for
$\mathcal D_{20}$ remains valid.

## 1. Authenticated inputs and review boundary

The following supplied identities were reproduced before inspection:

| artifact | reproduced SHA-256 |
|---|---|
| state/lemma_packets/SHELL-exact-d20-closure-round21-scoped.md | d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d |
| computations/round21_verify_exact_d20_closure.py | 64854c95004efb622c572f6c00d87bc997b74eec7c5563bb06863764b4c9df11 |
| computations/tests/test_round21_verify_exact_d20_closure.py | c9747c8cfe78d8da153e2c9e8b0ddb81e64296bbaf06ed5ede906595f806850e |
| rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md | 0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc |

This addendum audits only the domain correction and its consequences.  It
does not replace the compact or aggregate certificate reviews, change an A4
predicate, or re-promote any target.

## 2. Independent exact lower and upper bounds for pi

For completeness, the two rational bounds used below can be obtained
without a displayed decimal or sampled computation.

For $0\leq x\leq1$, finite geometric division gives

$$
\frac1{1+x^2}>
1-x^2+x^4-x^6+x^8-x^{10}+x^{12}-x^{14}
$$

away from the single endpoint $x=0$.  Therefore

$$
\begin{aligned}
\frac\pi4
=\int_0^1\frac{dx}{1+x^2}
&>
1-\frac13+\frac15-\frac17+\frac19-\frac1{11}
+\frac1{13}-\frac1{15}\\
&=\frac23+\frac2{35}+\frac2{99}+\frac2{195}
>\frac34.
\end{aligned}
$$

The last comparison is exact.  Indeed,

$$
\frac2{35}+\frac2{99}+\frac2{195}
>
\frac1{18}+\frac1{50}+\frac1{98}
>\frac1{12},
$$

where the second inequality is equivalent to

$$
\frac{17}{225}>\frac{43}{588},
\qquad
17\cdot588=9996>9675=43\cdot225.
$$

Thus $\pi>3$.  In the other direction, polynomial division yields

$$
0<
\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\frac{22}{7}-\pi,
$$

so $\pi<22/7$.

## 3. Correct domain of the lower-frequency guard

Assume exactly

$$
\rho_c\leq\rho<1,
\qquad
\rho_c=\frac1{1+2\pi}.
$$

Both denominators below are positive, and

$$
0<1-\rho\leq1-\rho_c.
$$

Taking positive reciprocals reverses this order, so

$$
z_\rho=\frac{\pi}{1-\rho}
\geq\frac{\pi}{1-\rho_c}.
$$

The endpoint value simplifies exactly:

$$
1-\rho_c=\frac{2\pi}{1+2\pi},
\qquad
\frac{\pi}{1-\rho_c}
=\frac{1+2\pi}{2}
=\pi+\frac12.
$$

Since $\pi>3$,

$$
z_\rho\geq\pi+\frac12>\frac72.
$$

Consequently,

$$
\begin{aligned}
k_{11}(\rho)^2
&=z_\rho^2+132\\
&>\frac{49}{4}+132
=\frac{577}{4}
>144,
\end{aligned}
$$

and therefore

$$
\boxed{k_{11}(\rho)>12
\qquad(\rho_c\leq\rho<1).}
$$

No step compares denominators across the pole at $\rho=1$.

## 4. The omitted upper wall is essential

At $\rho=1$, the denominator $1-\rho$ vanishes.  Thus $z_\rho$ and the
displayed definition of $k_{11}(\rho)$ are undefined.  The equality point is
a genuine singularity, not an endpoint at which the old statement can be
continued by the same formula.

The exact value $\rho=2$ disproves the assertion beyond the pole:

$$
z_2=\frac{\pi}{1-2}=-\pi,
\qquad
k_{11}(2)^2=\pi^2+132.
$$

Using the exact upper bound $\pi<22/7$ gives

$$
k_{11}(2)^2
<
\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}
<\frac{7056}{49}
=144.
$$

Hence

$$
\boxed{k_{11}(2)<12.}
$$

This is an exact counterexample to the old literal quantifier
$\rho\geq\rho_c$.

## 5. Audit of the old A3 report

The immutable old report contains the scope defect in one connected
argument:

1. it says without an upper domain that
   $z_\rho=\pi/(1-\rho)$ is increasing in $\rho$;
2. it then states, “For every $\rho\geq\rho_c$,” that
   $z_\rho\geq z_{\rho_c}$ and concludes $k_{11}(\rho)>12$;
3. its displayed equation (3) and the following containment language inherit
   that unqualified quantifier.

The derivative of $z_\rho$ is positive on each component of its domain, but
the function has a pole at $\rho=1$ and values to the right of that pole
cannot be compared to $z_{\rho_c}$ in the asserted direction.  These three
occurrences are manifestations of the same missing upper wall, not separate
mathematical mechanisms.

After replacing that argument by the boxed statement on
$\rho_c\leq\rho<1$, no second substantive domain-scope error remains in the
old A3 reconstruction:

- the compact theorem is used only on
  $7/51\leq\rho\leq39/50<1$;
- the aggregate theorem is used only on
  $\rho_c\leq\rho\leq39/50<1$;
- every later invocation of equations (2)--(3) is explicitly for a point of
  the accepted residual;
- all residual face and subtraction reasoning already assumes
  $\rho<39/50$.

The old report's separately recorded typography defects and the separately
hardened Machin branch-certificate lifecycle are retained in their own
chronology.  They are not additional domain-scope errors and are not erased
by this addendum.

The old unqualified sentence is rejected chronology.  It may not be cited
as a theorem, even though its restricted use inside $\mathcal D_{20}$ was in
the valid component $\rho<1$.

## 6. Why every D20 implication survives

The accepted residual has the exact ratio condition

$$
\rho_c\leq\rho<\frac{39}{50}.
$$

Since

$$
\frac{39}{50}<1,
$$

every residual point lies in the corrected guard domain.  Therefore

$$
12<k_{11}(\rho)<K
$$

continues to hold at every point of $\mathcal D_{20}$.  The compact owner
$K\leq200$ and aggregate owner $K>200$ remain exhaustive, and the shared
theorem face $K=200$ remains uniquely compact-owned.  The cases
$U(\rho)<200$, $U(\rho)=200$, and $U(\rho)>200$ are unaffected because the
correction changes no frequency inequality or owner definition.

The included face $\rho=\rho_c$ and the excluded faces
$\rho=39/50$, $K=k_{11}(\rho)$, and $K=U(\rho)$ retain their previous
ownership.  In particular, adding $\rho<1$ to the guard does not add or
remove a point of $\mathcal D_{20}$.

## 7. Scoped wrapper and tests

The authenticated wrapper now hash-gates the scoped replacement packet
rather than the rejected old candidate and fixes

$$
\text{K11\_GUARD\_DOMAIN}=\text{rho\_c<=rho<1}.
$$

Its exact-constant check uses the positive-denominator argument above and
its CLI reports only the scoped statement.  The authenticated tests require
that exact domain string, reject the old unqualified CLI text, and check the
exact $\rho=2$ counterexample through

$$
\pi_{\rm upper}^2+132<144.
$$

Inspection found no finite-certificate change:

- the compact root, 10,580 leaves, precision gates, strict-wall schema,
  proxy corners, and canonical digest are unchanged;
- the aggregate ratio boxes, branch split, 1,286 base boxes, $K=200$
  predicate family, and precision gates are unchanged;
- the wrapper still forbids an A4 universal-frequency claim and records the
  all-$K\geq200$ chain as an A3 obligation;
- the exact face classifier, 243 sign rows, $K=200$ ownership, and all three
  $U$ orderings are unchanged.

The focused scope and branch-mutation selection was rerun:

~~~text
python -m pytest computations/tests/test_round21_verify_exact_d20_closure.py \
  -q -k "exact_constants_faces_split_and_u_orderings or machin_branch_mutation_losing"

4 passed, 8 deselected
~~~

## 8. Status and nonclaims

This correction changes no certificate sign, finite box, leaf, theorem
face, subtraction owner, obligation status, or higher target.  It does not
promote SHELL-rho-compact, SHELL-rho-uniformity, TARGET-shell-d3, or
POLYA-program-target.  It supplies no State Patch.

**PASS. First issue: none.**  The scoped replacement is mathematically
correct, the old literal unqualified assertion is rejected, and the exact
Round 21 closure argument on $\mathcal D_{20}$ is unchanged because its
ratio range already satisfies $\rho<39/50<1$.
