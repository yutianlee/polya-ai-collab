(* General-d Round 34: symbolic replay only. *)

ClearAll[
  K, mu, c, delta, gamma, z, s, y, t, lam, aa, u, v, b,
  r, x, q, p, m, U, V, B, Bs, Rs, sigmaKernel, phi, D0,
  zz, PP, rho, XX, QQ, cc, a2n, bn, un, vn, Ln, Nn, Dn,
  dn, S0, L0, UD
];

$Assumptions =
  K > mu > q > x > r > 0 && 0 < c < 1 && c == mu/K &&
  p > 0 && m > 0 && x == r + p && q == x + m &&
  0 < t < Pi/2 && c == Cos[t];

delta = K - mu;
activityMarginIdentityResidual = FullSimplify[
  K^2 - Pi^2/(1 - c)^2 - (delta^2 - Pi^2)/(1 - c)^2,
  $Assumptions
];

rationalGap = 49/16 - 1 - 2;
safeGapUsingPiGreater1 = 33/16 - 2;

sigmaKernel[s_, z_] := (z/mu)/Sqrt[1 - s^2 z^2/mu^2];
phi[y_, z_] := (z/mu)/Sqrt[1 - y z^2/mu^2];

kernelConvexityNumerators = FullSimplify[
  {
    D[sigmaKernel[s, z], {s, 2}],
    D[phi[y, z], {y, 2}]
  },
  mu > z > 0 && 0 < s < 1 && 0 < y < 1
];

lam = 1 - c;
aa = (1 + c + c^2)/3;
U[z_] := Sqrt[mu^2 - z^2];
V[z_] := Sqrt[mu^2 - c^2 z^2];
B[z_] := Sqrt[mu^2 - aa z^2];
Bs[z_] := Sqrt[mu^2 - s^2 z^2];
Rs = (Bs[r] - Bs[x])/(Bs[x] - Bs[q]);

adjacentActionLogDerivativeResidual = FullSimplify[
  D[Log[Rs], s] -
    mu^2/(s Bs[x]) (1/Bs[r] - 1/Bs[q]),
  mu > q > x > r > 0 && 0 < s < 1
];

quadraturePrimitiveResiduals = FullSimplify[
  {
    D[-U[z], z] - z/U[z],
    D[-V[z]/c^2, z] - z/V[z],
    D[-B[z]/aa, z] - z/B[z],
    (B[r] - B[x])/aa - p (2 r + p)/(B[r] + B[x])
  },
  $Assumptions
];

F = Tan[t] - t;
normalizedCorrelationResidual = FullSimplify[
  3 Pi/(4 F) - 2 Pi/(lam D0) -
    Pi (3 lam D0 - 8 F)/(4 F lam D0),
  0 < t < Pi/2 && D0 > 0
];

XX = zz + PP;
QQ = zz + (1 + rho) PP;
a2n = (1 + cc + cc^2)/3;
bn[y_] := Sqrt[1 - a2n y^2];
un[y_] := Sqrt[1 - y^2];
vn[y_] := Sqrt[1 - cc^2 y^2];
Ln = 1/(un[XX] + un[QQ]) + 1/(vn[XX] + vn[QQ]);
Nn = PP (XX + zz)/(bn[zz] + bn[XX]);
Dn = rho PP (XX + QQ) Ln;

transportIdentityResiduals = FullSimplify[
  {
    (2 + rho)/(XX + QQ) - 1/(XX + zz) -
      2 zz (1 + rho)/((XX + QQ) (XX + zz)),
    D[Log[Dn/Nn], PP] -
      ((2 + rho)/(XX + QQ) - 1/(XX + zz) +
       D[Ln, PP]/Ln -
       a2n XX/(bn[XX] (bn[zz] + bn[XX]))),
    (1 + cc^2)/2 - a2n - (1 - cc)^2/6
  },
  0 < zz < XX < QQ < 1 && PP > 0 && rho > 0 && 0 < cc < 1
];

dn = 1 - 2 t/Pi;
qOneResiduals = FullSimplify[
  {
    ((XX - zz) - dn (1 - XX))/(2 (XX - zz)) -
      ((1 + dn) XX - zz - dn)/(2 (XX - zz)),
    2 (XX - zz) (XX + zz)/
       ((bn[zz] + bn[XX]) D0) -
      2 (bn[zz] - bn[XX])/(a2n D0)
  },
  0 < zz < XX < 1 && 0 < cc < 1 && D0 > 0
];

S0 = Sin[t];
L0 = S0 + Cos[t]^2 D0;
UD = (Sqrt[L0^2 - S0^4] - Cos[t] L0)/(Cos[t] S0^2);
xDRootPolynomialResidual = FullSimplify[
  S0^2 UD^2 + 2 L0 UD - (L0^2 - S0^2)/Cos[t]^2,
  0 < t < Pi/2 && D0 > 0 && L0^2 > S0^4
];

round34ActivityAndQuadratureReplayOK = And[
  activityMarginIdentityResidual === 0,
  rationalGap === 1/16,
  safeGapUsingPiGreater1 === 1/16,
  adjacentActionLogDerivativeResidual === 0,
  quadraturePrimitiveResiduals === {0, 0, 0, 0},
  normalizedCorrelationResidual === 0,
  transportIdentityResiduals === {0, 0, 0},
  qOneResiduals === {0, 0},
  xDRootPolynomialResidual === 0
];

Print["activityMarginIdentityResidual=", activityMarginIdentityResidual];
Print["rationalGap=", rationalGap];
Print["safeGapUsingPiGreater1=", safeGapUsingPiGreater1];
Print["kernelConvexityNumerators=", kernelConvexityNumerators];
Print["adjacentActionLogDerivativeResidual=", adjacentActionLogDerivativeResidual];
Print["quadraturePrimitiveResiduals=", quadraturePrimitiveResiduals];
Print["normalizedCorrelationResidual=", normalizedCorrelationResidual];
Print["transportIdentityResiduals=", transportIdentityResiduals];
Print["qOneResiduals=", qOneResiduals];
Print["xDRootPolynomialResidual=", xDRootPolynomialResidual];
Print["round34ActivityAndQuadratureReplayOK=", round34ActivityAndQuadratureReplayOK];
