# Clean-Room Review: Uniform Small-Hole Endpoint

Role: isolated clean-room reviewer

Obligation: `SHELL-rho-zero-endpoint`
Verdict: **PASS**

## Scope and permitted inputs

This reconstruction uses only the lemma packet and its four permitted proved
inputs:

1. the strict spectral bridge
   \[
   N_D(A_{\rho,1},K^2)\le S_{\rho,K};
   \]
2. the exact identity (S_{\rho,K}=\sum_{r\ge0}\mathcal T_r) and the
   weighted-lattice implication from tail bounds to the cubic bound;
3. the high-angular shifted-tail theorem, including its endpoint
   (x_r=\mu);
4. the audited small-hole low-interface theorem
   \[
   0<\rho<\omega_0,\quad K(\omega_0-\rho)\ge C_*,\quad x_r<\mu
   \quad\Longrightarrow\quad
   \mathcal T_r\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz.
   \]

Here

\[
\omega_0=\frac{\sqrt3}{2\pi}-\frac16,
\qquad
C_*=\frac12+\frac{8\sqrt2}{15},
\qquad
\mu=\rho K,
\]

and every \(\mathcal T_r\) is the shifted tail formed with the ordinary
floor in the packet.

## Exact constant calculation

First, \(\omega_0>0\): equivalently \(3\sqrt3>\pi\), which follows, for
example, from \(3\sqrt3>4>\pi\). Also \(C_*>0\). Therefore

\[
D:=1+2C_*=2+\frac{16\sqrt2}{15}>1
\]

and

\[
\rho_*=\frac{\omega_0}{D}
=\frac{\frac{\sqrt3}{2\pi}-\frac16}
{2+\frac{16\sqrt2}{15}}
\]

is positive and satisfies \(\rho_*<\omega_0\). In particular, throughout
the claimed range,

\[
0<\rho\le\rho_*<\omega_0.
\tag{A}
\]

The defining identity is exactly

\[
(1+2C_*)\rho_*=\omega_0,
\]

or, equivalently,

\[
\omega_0-\rho_*=2C_*\rho_*,
\qquad
\frac{\omega_0-\rho_*}{2\rho_*}=C_*.
\tag{B}
\]

For every \(0<\rho\le\rho_*\), multiplying \(\rho\le\rho_*\) by the
positive number \(1+2C_*\) gives

\[
(1+2C_*)\rho\le\omega_0.
\]

Consequently

\[
\omega_0-\rho\ge2C_*\rho,
\qquad
\frac{\omega_0-\rho}{2\rho}\ge C_*.
\tag{C}
\]

The second inequality is an equality precisely when \(\rho=\rho_*\).

## Reconstruction of the tail bound

Fix \(0<\rho\le\rho_*\) and \(K\ge0\).

If \(K=0\), then the defining sum for \(S_{\rho,0}\) has no indices because
no positive half-integer \(\nu_\ell\) satisfies \(\nu_\ell<0\). Hence
\(S_{\rho,0}=0\), and the strict spectral bridge gives

\[
0\le N_D(A_{\rho,1},0)\le0.
\]

This is exactly the desired estimate because its right-hand side is zero.
No value at \(\rho=0\) and no limiting argument is involved.

Now assume \(K>0\) and split at the exact interface scale

\[
\mu=\rho K=\frac12.
\]

### Case 1: \(\mu\le\tfrac12\)

For every \(r\ge0\),

\[
x_r=r+\frac12\ge\frac12\ge\mu.
\]

Thus the high-angular input applies to every tail and gives

\[
\mathcal T_r\le2\int_{x_r}^{K}A_{\rho,K}(z)\,dz
\qquad(r\ge0).
\tag{D}
\]

Both equalities are harmless: when \(\mu=1/2\), the first tail has
\(x_0=\mu\), and the high-angular theorem explicitly includes that
endpoint.

### Case 2: \(\mu>\tfrac12\)

Since \(\rho>0\),

\[
K>\frac1{2\rho}.
\]

By (A), \(\omega_0-\rho>0\), so multiplication preserves strictness; using
(C),

\[
K(\omega_0-\rho)
>
\frac{\omega_0-\rho}{2\rho}
\ge C_*.
\tag{E}
\]

For any \(r\), if \(x_r\ge\mu\), the high-angular input gives (D). If
\(x_r<\mu\), then (A) and (E) supply every hypothesis of the audited
small-hole low-interface theorem, which again gives (D). Hence (D) holds
for every \(r\) in this case as well.

Notice that at \(\rho=\rho_*\), the last inequality in (E) is an equality
before multiplication by (K), by (B), but its first inequality is strict.
Thus

\[
\mu>\frac12,\quad\rho=\rho_*
\quad\Longrightarrow\quad
K(\omega_0-\rho_*)>C_*.
\]

The endpoint \(\rho=\rho_*\) is therefore fully included.

## Completion through the scaffold and strict spectral bridge

In all cases every shifted tail satisfies (D). The exact tail identity and
weighted-lattice implication therefore give

\[
S_{\rho,K}
=\sum_{r\ge0}\mathcal T_r
\le\frac{2}{9\pi}(1-\rho^3)K^3.
\]

Invoking the supplied strict spectral bridge without altering its counting
convention yields

\[
\boxed{
N_D(A_{\rho,1},K^2)
\le S_{\rho,K}
\le\frac{2}{9\pi}(1-\rho^3)K^3
}
\]

for every \(0<\rho\le\rho_*\) and \(K\ge0\).

## Falsification audit

- **\(K=0\).** The proxy sum is empty, so both sides of the desired bound
  are zero; no action function at a singular zero endpoint is needed.
- **\(\rho=\rho_*\).** Identity (B) is exact. The branch \(\mu\le1/2\) is
  handled by the high-angular theorem, while \(\mu>1/2\) makes the low-tail
  threshold strict as shown in (E).
- **\(\mu=1/2\) exactly.** Every (x_r\ge\mu), and (x_0=\mu) is included
  in the non-strict hypothesis of the high-angular theorem.
- **\(\mu>1/2\) with \(\rho=\rho_*\).** Although (C) is then sharp,
  (K>1/(2\rho_*)) forces (K(\omega_0-\rho_*)>C_*).
- **\(x_0=\mu\).** This is assigned to the high branch (x_r\ge\mu), not
  to the strict low branch.
- **\(x_0\) immediately below \(\mu\).** Then (x_0<\mu), hence
  \(\mu>1/2\), and the low-interface theorem applies with the uniform
  strict threshold (E). No positive lower bound on \(\mu-x_0\) is used.
- **\(K(\omega_0-\rho)=C_*\).** This equality cannot occur in the
  \(\mu>1/2\) branch, where (E) is strict. More directly, (C) gives
  \[
  \mu=\rho K=\frac{C_*\rho}{\omega_0-\rho}\le\frac12,
  \]
  so every tail is high-angular. At \(\rho=\rho_*\), equality gives exactly
  \(\mu=1/2\).
- **True phase on an integer wall.** The phase count remains the supplied
  strict count. The already-audited bridge (and only that bridge) compares it
  to (S_{\rho,K}), so equality at a phase wall is never silently counted as
  a strict spectral event.
- **\(A_{\rho,K}(\nu_\ell)+1/4\) on an integer wall.** The proxy and both
  tail theorems use the ordinary floor appearing in the definition. At a
  wall it takes the integer value, and no strict-floor substitution is made.
- **Ordinary proxy versus strict phase count.** They are kept distinct:
  (S_{\rho,K}) is always the coarse ordinary-floor proxy; strictness occurs
  only in the true spectral count entering the permitted bridge.
- **\(\rho\downarrow0\).** The proof assumes (\rho>0) exactly as stated,
  divides only by that positive \(\rho\), and never invokes continuity of
  shell roots or a ball limit at \(\rho=0\).

No falsification case exposes an unsupported implication. The theorem, with
the endpoint \(\rho=\rho_*\), is proved from the four permitted inputs and
requires no finite Bessel certificate.
