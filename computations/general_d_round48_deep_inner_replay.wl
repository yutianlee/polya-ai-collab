(* Round 48 exact algebra replay for the deep-inner cell lemma. *)

ClearAll[z, mu, K, R, s, sigma, phi, n];

s[R_, z_] := z/(Pi R Sqrt[R^2 - z^2]);
sigma[z_] := (ArcSin[z/mu] - ArcSin[z/K])/Pi;
phi[u_] := 2 ArcSin[u] - u/Sqrt[1 - u^2];

shellCurvature = FullSimplify[
  2 s[R, z] - z D[s[R, z], z] ==
    z (R^2 - 2 z^2)/(Pi R (R^2 - z^2)^(3/2)),
  Assumptions -> {R > 0, 0 < z < R}
];

phiIdentity = FullSimplify[
  2 sigma[z] - z D[sigma[z], z] ==
    (phi[z/mu] - phi[z/K])/Pi,
  Assumptions -> {K > mu > 0, 0 < z < mu}
];

phiDerivative = FullSimplify[
  D[phi[u], u] == (1 - 2 u^2)/(1 - u^2)^(3/2),
  Assumptions -> {0 < u < 1}
];

squareReserve = FullSimplify[
  n^3/3 + n^2 - n (n + 1) (2 n + 1)/6 == n (3 n - 1)/6,
  Assumptions -> n >= 0
];

round48DeepInnerReplayOK = And[
  shellCurvature,
  phiIdentity,
  phiDerivative,
  squareReserve
];

Print["shellCurvature=", shellCurvature];
Print["phiIdentity=", phiIdentity];
Print["phiDerivative=", phiDerivative];
Print["squareReserve=", squareReserve];
Print["round48DeepInnerReplayOK=", round48DeepInnerReplayOK];

If[TrueQ[round48DeepInnerReplayOK], Exit[0], Exit[1]];
