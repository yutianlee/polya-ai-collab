# Round 48 clean-room reconstruction: full outer inverse-action cell

Candidate: `SHELL-general-d-d4-full-outer-action-cell-round48`
Role: clean-room reviewer
Verdict: **PASS**

The reviewer read only the candidate packet and its permitted elementary
dependencies, not the lead proof or another Round 48 route.

Let

\[
x=\xi(n),\qquad r=\xi(n-\tfrac14),\qquad y=\xi(n-1).
\]

The hypothesis \(n\le t_\mu\) puts the complete cell in the outer branch.
Define

\[
q=n-A(z)=\int_x^z h(u)\,du,qquad 0\le q\le1,
\]

and write \(z=z(q)\).  Then

\[
z(0)=x,qquad z(1/4)=r,qquad z(1)=y,
\]

and

\[
I_n:=\int_{n-1}^nF(t)\,dt=\frac13\int_0^1z(q)^3\,dq. \tag{1}
\]

Since \(z'(q)=1/h(z(q))\ge2\), and outer-branch \(h\) decreases with
\(z\), the function \(z\) is convex.  Put \(d=r-x\).  Then
\(r\ge d\ge1/2\), and

\[
z(q)\ge r-d+2q\quad(0\le q\le1/4), \tag{2}
\]

while convexity and the first-quarter secant give

\[
z(q)\ge r+4d(q-1/4)\quad(1/4\le q\le1). \tag{3}
\]

Equations (1)--(3) imply \(3I_n\ge E(r,d)\), where

\[
E(r,d)=
\frac{(r-d+1/2)^4-(r-d)^4}{8}
+\frac{(r+3d)^4-r^4}{16d}. \tag{4}
\]

Direct differentiation gives

\[
\partial_dE=
\frac{21}{8}r^2+15rd+\frac{231}{16}d^2
-\frac38r+\frac38d-\frac1{16}>0
\]

on \(r\ge d\ge1/2\).  Hence

\[
I_n\ge
Q(r):=\frac{r^3}{3}+\frac{r^2}{2}+\frac{7r}{12}+\frac5{24}. \tag{5}
\]

For \(N=\lceil r\rceil-1\ge1\), one has \(r>N\), so

\[
I_n>Q(N)=S_2(N)+\frac{5N}{12}+\frac5{24}.
\]

Moreover,

\[
\frac{5N}{12}+\frac5{24}
-\left(\frac{19N}{48}+\frac{27}{128}\right)
=\frac{8N-1}{384}>0.
\]

For \(N=0\), (5) and \(r\ge1/2\) give

\[
I_n\ge Q(1/2)=\frac23,qquad
\frac23-\frac{27}{128}=\frac{175}{384}>0.
\]

Thus the packet claim holds in every case.

The losses are exactly the two convex lower-envelope losses, the replacement
\(d\mapsto1/2\), and \(r\mapsto N\) for \(N\ge1\).  The proof separately
checks integer \(r\), \(N=0\), \(n=t_\mu\), \(n=1\),
\(\rho\downarrow0\), and integer/near-integer \(K,\mu\).  It does not apply
to an interface-straddling or truncated cell.
