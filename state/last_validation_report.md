# Last Validation Report

Date: 2026-07-14

Round: `polya-main` / round 15

## State patch

- Source: `rounds/polya-main/round_015/judge/judge-015.md`.
- `SHELL-central-thin-seam-compression` remains `proved_internal` and is
  strengthened to

  $$
  0<\varepsilon\le\frac16,
  \qquad
  K\ge\frac{54}{\varepsilon^2},
  $$

  including threshold equality.
- The sharper retained thresholds remain authoritative:
  $K\ge32/\varepsilon^2$ on $0<\varepsilon\le1/8$,
  $K\ge24/\varepsilon^2$ on $0<\varepsilon\le1/10$, and
  $K\ge20/\varepsilon^2$ on $0<\varepsilon\le1/25$.
- `SHELL-rho-compact-analytic-envelope` remains `proved_internal`; the seam
  moves to $\rho=5/6$, the exact fixed-ratio estimate is
  $K_0(5/6)<295^2=87025$, and the complete all-ratio analytic ceiling becomes
  $K\ge200000$.
- The complete all-frequency thin endpoint remains exactly
  $99/100\le\rho<1$.
- `SHELL-rho-compact`, `SHELL-rho-uniformity`, and `TARGET-shell-d3` remain
  `open`. `COMP-certified-bessel` remains `diagnostic_only`.
- No route is newly rejected. Round score: 6.

The judge State Patch validated before application, received a fresh
independent patch audit, and was applied exactly once. It must not be replayed
or revalidated against the promoted graph. The promoted graph hash immediately
after application was
`4f8477d9499cb388d5bf0d9048e452309c2a6a5ac7d70a410f1ca340b296d40f`.

## Frozen artifacts and independent reviews

- Frozen dependency packet:
  `state/lemma_packets/SHELL-central-thin-seam-compression-round15.md`.
- Packet SHA-256:
  `c35243cb98c842692f9cfa8c98d03164a8b8b710952e5aa6161205b1951ccbe7`.
- Incumbent proof SHA-256:
  `3d9c78583f14cfa59a989b248e376d78fc2f4b580ac5f6a2c3825885faff658f`.
- Independent constant inventory SHA-256:
  `959a120a1c9e0b7107eefd152f28d96948d67c3bc91de297fe4f8d31a4a3e5e1`.
- Strictly isolated clean-room proof SHA-256:
  `824670a5a5183d30f58d663bf672b9069042e61c53157b2ea153db90f9cab2c7`.
- Adversarial referee report SHA-256:
  `2fb4b2a8fd9a174532a6ec7299c6e68800ed5d61c23b62ed403d089a64d1271d`.
- Standalone verifier SHA-256:
  `14d03a2f7d935962af72a0abc159e2f7036a6dccd9539eb7d023c7b1abb63ca7`.
- Focused tests SHA-256:
  `21032410d48161e3fdda06cdc9fafdd27d74b4d5e6eed9e28bc0dc961bb7bf3a`.

The frozen packet audit was PASS: all 24 nontrivial identities were exact,
and UTF-8, delimiter, and whitespace checks passed. The incumbent proof,
independent constant inventory, strictly isolated clean-room reconstruction,
and fresh adversarial referee audit all returned PASS. The first unsupported
implication in every review was none. The clean-room proof used a distinct
cosine-gap self-consistency route rather than copying the incumbent finite
comparison.

## Accepted Round 15 theorem and reserves

The incumbent route proves

$$
d>\frac58,
\qquad
\widehat q<\frac{159}{400},
\qquad
\frac{x_0}{K}>\frac{241}{480}
=\frac12+\frac1{480}.
$$

With $B=14/3$ and

$$
S_*(P,r)=\frac{13P-8r}{5},
$$

the complete path has derivative cap and reserve

$$
\frac{2260740364246}{708624500625}<\frac{16}{5},
\qquad
\frac{6858037754}{708624500625}>0,
$$

while the comparison slope is $92/15$. The endpoint, dangerous-payment, and
safe-payment reserves are

$$
\frac{2505132463469}{2616573970125}>0,
\qquad
\frac{80132733}{3024175}>0,
\qquad
\frac{114694733}{3024175}>0.
$$

The action-gain comparison is $280000/17281$, and the central fixed-ratio
calculation at $Y=295$ has positive margin

$$
\frac{5226}{1225}>0.
$$

Both the incumbent and isolated clean-room arguments own the no-drop,
immediate-drop, degenerate-head, and sign-wall branches; the full possible
unit floor loss; all interface, ordinary-floor, and strict spectral walls;
and the threshold face. Therefore

$$
\boxed{
0<\varepsilon\le\frac16,
\qquad
K\ge\frac{54}{\varepsilon^2}
\quad\Longrightarrow\quad
N_D(A_{1-\varepsilon,1},K^2)
\le
\frac{2}{9\pi}
\bigl(1-(1-\varepsilon)^3\bigr)K^3.
}
$$

Separately, the positive defining-quadratic margin at $Y=295$ proves

$$
\boxed{K_0(5/6)<295^2=87025.}
$$

At $\kappa=53$, the selected localization proxy misses by
$14293/15900000$. At $Y=294$, the selected central proxy equals
$-307/175$. These are route obstructions only, not counterexamples or
rejections.

## Closed seven-zone global union

The accepted finite residual zones are:

1. on $[\rho_*,1/16]$, $K<64$;
2. on $[1/16,5/6]$,
   $K<K_0(\rho)\le K_0(5/6)<87025$;
3. on $[5/6,7/8]$, $K<54/(1-\rho)^2\le3456$;
4. on $[7/8,9/10]$, $K<32/(1-\rho)^2\le3200$;
5. on $[9/10,19/20]$, $K<24/(1-\rho)^2\le9600$;
6. on $[19/20,24/25]$, $K<24/(1-\rho)^2\le15000$;
7. on $[24/25,99/100]$, $K<20/(1-\rho)^2\le200000$.

The complete endpoint owns $[99/100,1)$ for every $K$, and every shared
ratio and threshold face is owned by an accepted theorem. Consequently

$$
\boxed{
0<\rho<1,
\qquad K\ge200000
\Longrightarrow
N_D(A_{\rho,1},K^2)
\le\frac{2}{9\pi}(1-\rho^3)K^3.
}
$$

The exact reduction from the Round 14 ceiling is

$$
\frac{550^2}{200000}=\frac{121}{80}>1.
$$

## Complete thin endpoint

Round 15 does not enlarge the all-frequency endpoint. The accepted product,
aggregate, and complementary-action ranges still prove exactly

$$
\boxed{
\frac{99}{100}\le\rho<1,
\qquad K\ge0.
}
$$

The Round 15 seam theorem is high-frequency only.

## Certified pilot boundary

The Round 8 certified box

$$
\rho\in[999/2000,1001/2000],
\qquad
K\in[67/10,168/25]
$$

retains exact strict count $4$ and certified Weyl margin greater than
$14.60731553544245607556$. Round 15 changes no producer, checker,
certificate, or protected packet. The independent checker reproduces the
unchanged protected packet hash
`8b684f7f671dd96f9916d0d798566a5e1cbe787934c08744531e3f7ba086b8c7`.
This remains evidence for one local box only; the parent compact
certification remains `diagnostic_only`.

## Mechanical validation

- Frozen packet independent audit, including 24 exact nontrivial identities:
  PASS.
- Embedded incumbent exact ledger: PASS.
- Extracted strictly isolated clean-room ledger: PASS.
- Standalone Round 15 exact verifier: PASS.
- Focused Round 15 tests: 7 passed.
- Complete computation suite: 58 passed.
- Fresh adversarial branch, wall, face, and global-union audit: PASS; first
  unsupported implication: none.
- Pre-promotion graph audit: 49 obligation IDs, acyclic dependency graph, and
  all 566 evidence-reference occurrences (141 unique artifact paths) present.
- Judge State Patch pre-application validation and independent patch audit:
  PASS.
- State Patch applied exactly once: PASS.
- Round 8 independent certificate and provenance checker: PASS.
- Fresh post-promotion theorem/state audit: PASS; first unsupported
  implication: none. No accepted status, endpoint, shared face, or compact
  residual was overpromoted.
- Final durable graph audit: 49 unique obligation IDs, 170 dependency
  edges, an acyclic dependency graph, and all dependency,
  permitted-dependency, blocker, and implication references resolved. All
  596 artifact-reference occurrences (148 normalized paths) are present.
- Final durable graph SHA-256:
  `b96477f650230d847dc72db851be997752f6a50822cf47e57b13ce9d362d9bd5`.
- The Round 16 prompt audit initially found three planning-text defects: a
  falsely strict equality-face symbol, an overbroad domain for $J_r$, and an
  incomplete phase-transfer whitelist. All three were corrected; focused
  re-audit returned PASS with no unsupported implication. No Round 15
  theorem or State Patch claim was affected.
- Reading-packet regeneration, Python compilation, UTF-8/control-character,
  trailing-whitespace, final-newline, Markdown delimiter, and Git diff
  checks: PASS.

## Authoritative boundary

Both endpoint neighborhoods are proved for all frequencies, and the shell
inequality is proved for every ratio when $K\ge200000$. The full
all-frequency theorem remains open on the exact compact residual

$$
\boxed{
\mathcal D_{15}
=(I_{15}\times[0,\infty))\setminus\mathcal A,
\qquad
I_{15}=\left[\rho_*,\frac{99}{100}\right].
}
$$

Here $\mathcal A$ is the complete accepted analytic cover, including every
threshold face. The seven-zone envelope is only a planning cover of the
complement; it must not be replaced by the rectangle
$I_{15}\times[0,200000)$.

The next unproved analytic target for Round 16 is the larger all-frequency
endpoint

$$
\frac78\le\rho<1,
\qquad K\ge0.
$$

The proposed split at $a=\pi/(4\varepsilon)$, planning reserves $577/2880$
and $143/4096$, and prospective global ceiling $K\ge295^2$ remain unproved.
They are not part of the accepted Round 15 cover. Fresh theorem-level
clean-room and adversarial audits remain mandatory after the compact residual
closes.
