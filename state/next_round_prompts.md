# Next Round Prompts

Generated after Round 8 in run `polya-main`.

Source synthesis: `rounds/polya-main/round_008/judge/judge-008.md`.

## Accepted boundary

Let

$$
\rho_*=
\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}},
\qquad
I_*=[\rho_*,1-2^{-18}].
$$

The shell Pólya inequality is proved for every $K\ge0$ in the two endpoint
neighborhoods

$$
0<\rho\le\rho_*
\qquad\hbox{and}\qquad
1-2^{-18}\le\rho<1.
$$

On $I_*$ it is proved uniformly for every $K\ge2^{42}$. The exact strict
count is also independently certified on

$$
B_0=
\left[\frac{999}{2000},\frac{1001}{2000}\right]
\times
\left[\frac{67}{10},\frac{168}{25}\right].
$$

The closed sets $\mathcal R_L$, $\mathcal R_C$, and $\mathcal R_T$ form a
planning envelope $\mathcal E$. The true certificate target is

$$
\mathcal D=(I_*\times[0,\infty))\setminus\mathcal A,
$$

where $\mathcal A$ is the union of all analytic ranges. `SHELL-rho-compact`
and the parent `COMP-certified-bessel` remain open.

## Round 9 primary target

Do not attempt to enumerate the current $2^{35}$ or $2^{42}$ ceilings. At
$\varepsilon=2^{-17}$, one thin residual slice already crosses more than
$2^{38}$ angular walls.

Instead, optimize the proved Round 6 local-plateau theorem. The current
statement is

$$
K\ge\frac{64}{\varepsilon^2},
\qquad 0<\varepsilon\le\frac1{100}.
$$

The Round 6 clean-room proof obtained a stronger plateau estimate than the
incumbent, but it used $64$ at intermediate steps. Introduce a parameter
$C$ in

$$
K\ge\frac{C}{\varepsilon^2}
$$

and rederive every intermediate inequality. The target is the smallest
simple explicit $C_{m opt}<64$ that is genuinely self-consistent, followed
by the exact enlarged endpoint obtained from overlap with

$$
K\le\frac1{8\varepsilon^{5/2}}.
$$

Correctness and a substantial explicit reduction come before numerical
optimality.

## For A1

Freeze a packet `SHELL-thin-local-plateau-optimized` with two outputs.

1. An explicit theorem

   $$
   0<\varepsilon\le\frac1{100},
   \qquad
   K\ge K_{\rm lp}(\varepsilon)
   \Longrightarrow\text{shell Pólya},
   $$

   where $K_{\rm lp}(\varepsilon)$ is strictly smaller than
   $64\varepsilon^{-2}$ on a nontrivial interval.
2. An exact algebraic or rational $\varepsilon_{m new}>2^{-18}$ such that

   $$
   K_{\rm lp}(\varepsilon)
   \le\frac1{8\varepsilon^{5/2}}
   \qquad(0<\varepsilon\le\varepsilon_{m new}).
   $$

List every place where the old assumption $K\ge64\varepsilon^{-2}$ entered
the proof: the dangerous-plateau location, the local slope integration, the
quadratic bound for $p$, the lower bound for $K G_1(1-\varepsilon)$, and the
final interface-loss payment. Do not import $p<8/\sqrt\varepsilon$ unless its
proof has first been made valid under the new hypothesis.

If the constant optimization cannot close self-consistently, freeze the
first failed inequality and switch to a symbolic aggregate count on one
explicit nontrivial strip of $\mathcal R_T$.

## For A2

Develop the incumbent parametric proof from the audited Round 3 tail
decomposition and the Round 6 local-slope argument.

Use

$$
M=\lfloor K\eta\rfloor+d m-p,
\qquad
\eta=G_1(1-\varepsilon),
$$

and retain the exact branch condition under which $p-dm$ can be positive.
Derive a $C$-dependent plateau bound rather than substituting $64$ at the
start. Keep the no-drop branch $p=n$, immediate-drop branch $p=0$, and
$n=0$ branch separate until the final uniform estimate.

The output must include:

- an exact formula or sufficient inequalities for $C_{m opt}$;
- all elementary bounds on $\pi$, $\sqrt2$, and $G_1$ used to rationalize it;
- a proof that every strict floor and interface endpoint is safe;
- the exact overlap equation defining $\varepsilon_{m new}$;
- a quantified reduction of $\mathcal R_T$.

No floating-point optimization may be used as proof.

## For A3

Receive only the optimized packet and reconstruct the proof independently.
Attempt to falsify it at:

- $\varepsilon=1/100$ and the proposed $\varepsilon_{m new}$;
- $K=K_{\rm lp}(\varepsilon)$;
- equality with $1/(8\varepsilon^{5/2})$;
- the branch $p=n$ with no floor drop;
- $p=0$ and $n=0$;
- the first point where the proof claims $x_0\ge K/2$;
- every use of a bound previously derived under $C=64$;
- $K\eta$ on an integer wall and the maximal interface loss.

Reject any circular argument of the form “use the $C=64$ plateau lemma to
prove the same lemma for $C<64$.” Recompute the overlap constant exactly.

## For A4

The certification task is deliberately secondary.

1. Extend $B_0$ by at least one small rational box sharing a complete face,
   or explain with a certified wall enclosure why that face must be split.
2. Emit a two-cell manifest with exact face ownership and verify its union
   and hashes independently.
3. Continue using outward-rounded Arb for the producer and a checker that
   shares no producer or Flint code for decisive low-channel identities.
4. Test tampering of coordinates, count, determinant signs, truncation, face
   ownership, and hashes.

This exercise validates the face-connected manifest format only. Do not
claim progress on the giant high-frequency families from adding low-energy
tiles.

## Promotion constraints

Promote an optimized local-plateau lemma only after:

1. the new hypothesis is used consistently in every intermediate estimate;
2. an isolated clean-room reconstruction passes;
3. an adversarial constants and wall audit passes;
4. the enlarged thin endpoint overlap is exact and includes equality.

Keep `SHELL-rho-compact`, `COMP-certified-bessel`,
`SHELL-rho-uniformity`, and `TARGET-shell-d3` open until an exact checked
cover of all of $\mathcal D$ exists. Only then begin the final theorem-level
clean-room and adversarial audit.
