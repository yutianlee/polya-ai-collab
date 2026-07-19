# Round 20 adversarial audit: global high-ratio route

Status: **PASS after exact re-audit of the repaired provenance**.  The
all-frequency analytic argument through (1), its exact constants, the
prospective set subtraction, and the central-floor conclusion all pass
independent reconstruction.

Date: 2026-07-15.

Audited target:

```text
rounds/polya-main/round_020/exploration/high-global-route.md
SHA-256 bbfc40bcb7ce748b946a6fdea7728315489d7e2e7842a0ccb6789f3f34fee6c4
```

I again assumed the claimed band was false, used only the five inputs declared
in the target's provenance table, and rechecked the repaired bytes from the
beginning rather than carrying forward the previous verdict.

## 1. Provenance and byte boundary

Every declared hash matches its file byte for byte:

| declared input | independently recomputed SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-one-endpoint-round16.md` | `5886997f0f840ae1a9a8cef53ba2b44b384eb6c94f5d1fe94cee64219268df09` |
| `state/lemma_packets/SHELL-phase-enclosures.md` | `96d0d466031f2b40353a7f4a61c1650e3db45bcd9ad2a5b87091b61d6ba59abf` |
| `state/lemma_packets/SHELL-sturm-liouville-completeness.md` | `6fde758cab1c8e9bda1ed2f268640dca9a5b0536b3c635de83bbdee330d0bcb8` |
| `rounds/polya-main/round_020/exploration/high-k9-extension.md` | `d12b738945abb8e80d0ba0356411af194965e59f251ec03b7fb479ccfe884ab1` |
| `rounds/polya-main/round_020/exploration/high-k9-adversarial-audit.md` | `b31a7b4d667992a4e02ffe4e5e5999cdfe611a8b67bd58ea57cdb22a4dc7f63d` |

The target is UTF-8 without a BOM, uses LF line endings, ends in one newline,
has no trailing whitespace, and contains no disallowed control byte.  The five
declared inputs likewise contain no disallowed control byte.  No undeclared
proof or numerical zero table was used.

## 2. Scaling, split, and product deficit

Put `e=epsilon`.  From `rho=1-e` and `a=eK`, direct expansion gives

\[
 \frac{2}{9\pi}(1-\rho^3)K^3
 =\frac1{e^2}\frac{2a^3}{3\pi}
  \left(1-e+\frac{e^2}{3}\right).
\]

For `c=34/19` and `e0=7/32`,

\[
 \frac{c}{e_0}=\frac{1088}{133},\qquad
 \frac{1088}{133}-\frac{44}{7}=\frac{36}{19}>0.
\]

Since `pi<22/7`, this is strictly above `2pi`.  The inclusive pieces
`a<=c/e` and `a>=c/e` cover all nonnegative `a` and both own the face.

The product comparison is also recovered with the correct direction.  The
shell radial operator satisfies

\[
 -\partial_r^2+\frac{\ell(\ell+1)}{r^2}
 \ \geq\ -\partial_r^2+\ell(\ell+1),
\]

so the strict shell count is at most the product count.  If

\[
 b_n=(a^2-n^2\pi^2)^{1/2},\qquad
 M_n=\left\lceil
 \sqrt{(b_n/e)^2+\frac14}-\frac12
 \right\rceil,
\]

then the allowed angular indices are exactly `0,...,M_n-1`, including the
correct exclusion at an equality wall, and their multiplicity sum is
`M_n^2`.  The strict ceiling estimate, the decreasing quarter-circle sum,
and `N<a/pi` give

\[
 e^2\mathcal P_e(a)
 <S_0(a)+\frac{ea^2}{4}+\frac{e^2a}{\pi}.
\]

At `a=m pi`, `N=m-1,t=1`; hence the threshold radial mode is absent.  For
`a>pi`, exact summation gives

\[
 \frac{D(a)}{\pi^2}
 =\frac{N^2}{2}+N\left(t^2+\frac16\right)+\frac{2t^3}{3}.
\]

Subtracting `11(N+t)^2/25` reproduces (11).  Moreover

\[
 \Delta_{N+1}-\Delta_N
 =\frac{3(2N+1)}{50}
  +\left(t-\frac{11}{25}\right)^2-\frac{101}{3750}
 \geq\frac{287}{1875}>0.
\]

For `N=1`,

\[
 \Delta_1'(t)=\frac{2}{25}(25t-11)(t+1),
 \qquad
 \Delta_1(11/25)=\frac{73}{15625}>0.
\]

Thus `D(a)>11a^2/25` on every cell.  This includes the strict wall
convention and is continuous between the `(N-1,1)` and `(N,0+)`
descriptions.  No sampled zero information enters this result.

## 3. Low optical screen

The sufficient condition used in the target is deliberately stronger than
necessary: it drops the favorable `e^2 I_0/3` term.  After division by
`a^2`, `a<=c/e`, `a>pi`, and `1/pi<q=106/333` give

\[
 \frac{2ea}{3\pi}+\frac e4+\frac{e^2}{\pi a}
 <\frac{2cq}{3}+\frac e4+e^2q^2.
\]

The right side increases strictly in `e`.  Exact rational reduction at
`e=7/32` gives

\[
 \frac{11}{25}
 -\left(\frac23\frac{34}{19}\frac{106}{333}
 +\frac7{128}+\frac{49}{1024}\left(\frac{106}{333}\right)^2\right)
 =\frac{9650531}{13484102400}>0.
\]

Therefore the product count is strictly below `I_0(1-e)`, hence below the
Weyl normalization for every `K>0`.  For `0<=a<=pi`, including `a=pi`,
the strict product radial count is zero.  This closes the entire inclusive
low piece without a lost radial or angular wall.

The two rational bounds for `pi` can themselves be certified without a
decimal oracle.  For example, Machin's identity together with alternating
arctangent truncations yields strict rational enclosures stronger than
`333/106<pi<22/7`.

## 4. Phase transfer and high optical screen

For `nu=ell+1/2<=K`, the declared phase enclosure is piecewise exactly the
target action proxy:

- when `nu<=rho K`, it gives `gamma<A(y)+1/4` with the complementary
  action;
- when `rho K<nu<=K`, its permitted global one-sided estimate gives the
  outer action plus `1/4`.

Thus strict radial counting gives

\[
 q_\ell=\left[\mathcal A(y_\ell)+\frac14\right]_<,
 \qquad
 N_D\leq\frac{2P_{\mathcal A}}{e^2}.
\]

The strict bracket excludes an integer phase wall.  Channels with `nu>K`
do not contribute (the radial Poincare term together with
`ell(ell+1)=nu^2-1/4` already puts their product lower bound above `K^2`),
and the extension `A=0` gives `q_ell=0` there.

Swapping the two strict finite counts gives the exact layer-cake formula

\[
 P_{\mathcal A}=\frac{e^2}{2}
 \sum_{n-1/4<T}M_e(R(n-1/4))^2.
\]

Inverse integration gives

\[
 I=\frac12\int_0^T R(t)^2\,dt
 =\frac{a^3}{3\pi}\left(1-e+\frac{e^2}{3}\right).
\]

Direct differentiation confirms that `g=-F'` decreases before the actual
inner interface and increases after it.  Splitting the Stieltjes integral
at that ungridded interface, using `W>=0` on the decreasing part and
`-1/32<=W-t/4<=3/32` on the increasing part, gives

\[
 D_{\rm rad}\geq\frac{\rho^2a^2}{4}-\frac{\pi\rho a}{4}.
\]

The endpoint coefficient is correct because `g(T)=2pi rho a`; the full
oscillation range `4/32` costs exactly `g(T)/8=pi rho a/4`.  The improper
trace at `t=0` vanishes, and no assumption on the location of the interface
relative to a sawtooth grid point is used.

The half-integer ceiling gives, strictly,

\[
 e^2\sum M_e(R(n-1/4))^2
 <\sum F(n-1/4)+
 \left(\frac a\pi+\frac14\right)
 \left(ea+\frac{e^2}{4}\right).
\]

On `a>=c/e`, expansion with `1/a<=e/c` reproduces every coefficient:

\[
 \frac{D_{\rm rad}}{a^2}
 \geq\frac{(1-e)^2}{4}-\frac{19\pi}{136}(1-e)e,
\]

and

\[
 \frac E{a^2}\leq
 \frac e\pi+\frac{19e^3}{136\pi}
 +\frac{19e^2}{136}+\frac{361e^4}{18496}.
\]

The rational lower screen has derivative

\[
 -\frac{1-e}{2}-\frac{11}{14c}(1-2e)<0
 \qquad(0<e<1/2),
\]

while the upper screen is increasing term by term.  At `e=7/32`, exact
subtraction gives

\[
 R_{\rm high}
 =\frac{4669924235}{6458355744768}>0.
\]

Hence `D_rad>E`, including `e=7/32` and `a=c/e`, so
`P_A<I`.  Combined with the phase transfer this proves the strict Weyl
comparison for every `K>0` on the high piece.  At `K=0` both sides are
zero.  The ratio face, optical face, radial walls, half-integer walls,
phase walls, and inner-action interface all have the owners stated in the
target.

## 5. Prospective subtraction and the two-screen obstruction

Intersecting the declared prospective `k_9` residual

\[
 \{\rho_c\leq\rho<7/8,\ k_9(\rho)<K<U(\rho)\}
\]

with the new all-frequency band removes exactly

\[
 \{25/32\leq\rho<7/8,\ k_9(\rho)<K<U(\rho)\}.
\]

Thus the remaining set is exactly

\[
 \{\rho_c\leq\rho<25/32,\ k_9(\rho)<K<U(\rho)\}.
\]

The face `rho=25/32` is removed by the new theorem, `K=k_9` is owned by
the prospective staircase theorem, and `K=U` remains owned by the inherited
upper cover.  Since `25/32<5/6`, the declared `k_9` adversarial audit's
central-floor statement also supports the conclusion that this remaining
interval uses `K_0`, rather than the seam floor.

The general screens (31)--(32) are algebraically correct.  At
`e=9/41,c=206/115`, exact reduction gives

\[
 R_L=\frac{14692831}{142910046900}>0,
 \qquad
 R_H=\frac{13435547837}{496923590290624}>0.
\]

At `e=11/50`, `R_L>0` forces

\[
 c<c_{\max}=\frac{210742213}{117660000}.
\]

For fixed `e`, direct differentiation shows `R_H` is strictly increasing
in `c`.  Nevertheless,

\[
 R_H(c_{\max},11/50)
 =-\frac{4113718505834613061}
 {8555787229162000590000}<0.
\]

Therefore no constant split closes these separated screens at `11/50`.
The proposed normalized gain `1/2000` exceeds the shortfall by exactly

\[
 \frac{82087554373193617}{4277893614581000295000}>0.
\]

Continuity then permits a `c<c_max` sufficiently close to `c_max`, making
both the strict low reserve and the improved high reserve positive.  This
is correctly described as a method obstruction and next-lemma target, not
as a counterexample.

## 6. Repaired provenance and final verdict

The repaired target removes the undefined `rho_HK` chain.  It now invokes
the already declared artifact

```text
rounds/polya-main/round_020/exploration/high-k9-adversarial-audit.md
SHA-256 b31a7b4d667992a4e02ffe4e5e5999cdfe611a8b67bd58ea57cdb22a4dc7f63d
```

which explicitly records that the inherited floor on
`rho_c<=rho<5/6` is the central floor `K_0`.  The elementary strict
comparison

\[
 \frac{25}{32}<\frac56
\]

therefore places every ratio in the remaining set (29) on that declared
central branch.  This proves the repaired equation (30),

\[
 U(\rho)=K_0(\rho)
 \qquad\left(\rho_c\leq\rho<\frac{25}{32}\right),
\]

without an undeclared dependency.  The seam floor disappears because the
new all-frequency band includes the whole interval from `25/32` through the
seam and up to `7/8`.

The subsequent equation renumbering is internally consistent: the screen
definitions are now (31)--(32), the test reserves are (33), `c_max` is
(34), the obstruction is (35), and the proposed gain is (36).  Their exact
values remain those independently reduced above.

**Final verdict: PASS.**  No unsupported implication, arithmetic mismatch,
endpoint gap, strict-counting error, provenance leak, malformed byte, or
set-subtraction error remains in the repaired artifact.  This verdict is
only for the exploratory result at the audited SHA; it does not freeze or
promote the theorem.
