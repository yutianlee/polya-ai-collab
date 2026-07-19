# Independent audit: Round 22 coarse scalar counterexample and exact-cap repair

Date: 19 July 2026  
Audited note SHA-256: `f129c6a0e62193806e355a336c6ca5b9381147bdb08ab634577bdbed0c3b29e9`  
Audited replay SHA-256: `1ff8a85499c422d54bc25adfae66518d116909df38de3fe8d72fd3e8fca1720e`  
Verdict: **PASS**

The displayed rational point is a genuine strict, dimension-active,
high-floor first-drop shell and rigorously satisfies
\(\mathcal R<-1/300\).  Keeping the correlated cap gives
\(\mathcal R_J>1/20\) and the Round 21 algebra gives
\(\Phi_\delta>\mathcal R_J\).  Thus the point falsifies only the coarse
claim \(\mathcal R\geq0\), not \(\Phi_\delta\), CST-H, the exact scalar,
or the shifted-tail theorem.

## 1. Exact phase reconstruction

For

\[
 K=\frac{261}{20},\quad \mu=\frac{699}{100},\quad
 \rho=\frac{233}{435},\quad r=1,
\]

exact rational arithmetic gives

\[
 \frac\mu K=\rho,\quad \mu-r=\frac{599}{100},\quad
 n=5,\quad q=r+n=6,\quad \alpha=\mu-q=\frac{99}{100}.
\]

The first shelf ends at \(r+p=4\), so \(p=3<n\),
\(m=n-p=2\), and \(X=\mu-r-p=299/100=m+\alpha\).  The weakest new
integer owner is \(d=4\), whose activity correction is \(3/4\).  A
256-bit directed Arb reconstruction gives

\[
 K^2-\left(\frac{\pi^2}{(1-\rho)^2}+\frac34\right)
 =123.7830682581086686440\ldots>0.
\]

For \(A(z)=G_K(z)-G_\mu(z)\), the independently recomputed strict samples
are

\[
\begin{array}{c|rrrrrr}
z&1&2&3&4&5&6\\ \hline
A(z)+1/4&
2.168351647875&2.136124226723&2.080955394142&
2.000267111380&1.889335340768&1.738646820035.
\end{array}
\]

The Arb balls lie strictly in \((2,3)\) for \(z=1,\dots,4\) and in
\((1,2)\) for \(z=5,6\).  The smallest phase reserve is

\[
 A(4)+\frac14-2
 =0.0002671113796677224460592746887\ldots>0.
\]

Consequently \(f=2\) and the asserted first drop at \(z=5\) is literal;
the point is not on an action wall.

With \(\theta=\arccos\rho\), direct evaluation of \(G_K(\mu)\) agrees
with \(K(\sin\theta-\theta\cos\theta)/\pi\), and gives

\[
 c=0.3200733626077825\ldots,\qquad
 d_\rho=0.3598532747844349\ldots,
\]

\[
 W+\frac14=1.5204910257427113\ldots,qquad
 \lambda=0.4795089742572886\ldots.
\]

Hence the literal strict count is \(B_0=1\), while
\(0<\lambda<3/4<1\).  The active top-payment branch is therefore
\(\mathcal E(\lambda)=2(3/4-\lambda)^2<1\), with value
\(0.1463307900146882767\ldots\).

## 2. Coarse scalar sign

Here \(a_p=3/5\).  Independent substitution in the two shelf payments
gives directed enclosures centered at

\[
 (s-1)\lambda=0.09918518638669317825\ldots,
\]

\[
 \frac\kappa2p(2r+p)=0.15859749644597137697\ldots.
\]

Their difference is
\(0.05941231005927819872\ldots>0\), so the curvature term is strictly the
maximum defining \(L_0\).  Substitution in Round 21 equation (4.4) then
gives, at 256 bits,

\[
 \mathcal R=
 [-0.0035802246057544553000272883575016748253
 \mathbin{+/-}3.08\,10^{-75}].
\]

More directly, the certified comparison margin is

\[
 -\frac1{300}-\mathcal R
 =[0.0002468912724211219666939550241683414920
 \mathbin{+/-}5.51\,10^{-75}]>0.
\]

This rigorously disproves \(\mathcal R\geq0\), and all phase and maximum
decisions are strict, so the failure persists on a neighborhood.

## 3. Exact cap and implication boundary

Differentiating the stated elementary primitive gives
\(I_a'(x)=-G_a(x)\), and \(I_a(a)=0\); hence the retained cap is exactly
\(J=2I_\mu(q)\).  Arb gives

\[
 J=[0.08901111693545672468110130562109603475
 \mathbin{+/-}8.06\,10^{-75}]<\frac17,
\]

and therefore

\[
 \mathcal R_J=\mathcal R+\frac17-J
 =[0.05026580131593167716172854887854514756
 \mathbin{+/-}4.67\,10^{-75}].
\]

The positive comparison reserve is

\[
 \mathcal R_J-\frac1{20}
 =[0.00026580131593167716172854887854514756
 \mathbin{+/-}4.67\,10^{-75}]>0.
\]

The exact-cap form of the Round 21 terminal argument is

\[
 L_T>\frac{B_0d_\rho}{2c}-J+\mathcal E(\lambda).
\]

Adding the already proved shelf bound gives, with no change of sign or
branch,

\[
\begin{aligned}
 \Phi_\delta
 &>(p+a_p)L_0-\frac p2+\frac{d_\rho m}{2}
   +\frac{B_0d_\rho}{2c}-J+\mathcal E(\lambda)\\
 &=\mathcal R+\frac17-J=\mathcal R_J>\frac1{20}.
\end{aligned}
\]

Thus the negative \(\mathcal R\) is entirely compatible with a positive
lower surrogate at this point.  The repaired all-domain target
\(\mathcal R_J\geq0\), and hence CST-H, remains open.

## 4. Replay audit

The frozen script was rerun with python-flint 0.8.0 at 128, 256, 512,
and 1024 bits.  Every run returned both PASS lines, all leading values
agreed, and the interval radii contracted as expected.  A separate
from-formula Arb reconstruction reproduced the activity, six shelf
samples, literal \(B_0\), branch maximum, \(\mathcal R\), \(J\), and
\(\mathcal R_J\) without importing the replay module.
