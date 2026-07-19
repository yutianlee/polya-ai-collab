(* Round 33: symbolic replay for lower-Q hard-arc monotonicity. *)

ClearAll["Global`*"];

(* Exact wall factorization. *)
kappa = Sqrt[mu^2 - q^2]/Sqrt[mu^2 - c^2 q^2];
u[z_] := Sqrt[mu^2 - z^2];
v[z_] := Sqrt[mu^2 - c^2 z^2];
aa = 1 - kappa c;

factorResidual = FullSimplify[
  (u[x] - kappa v[x]) -
   aa (1 + kappa c) (q^2 - x^2)/(u[x] + kappa v[x]),
  Assumptions -> 0 < x < q < mu && 0 < c < 1
];

squareResidual = FullSimplify[
  u[x]^2 - kappa^2 v[x]^2 -
   aa (1 + kappa c) (q^2 - x^2),
  Assumptions -> 0 < x < q < mu && 0 < c < 1
];

(* Half-angle reduction of
   4 (Sin[t] - t Cos[t]) - 3 (1-Cos[t]) Sin[t]^2. *)
poly[u_] := 20 - 45 u + 32 u^2 + 7 u^4 - 2 u^6 + 3 u^8;
atanUpper[u_] := u - u^3/3 + u^5/5;

halfAngleLower = Expand[
  (1 + z^2)^2 (z - (1 - z^2) atanUpper[z]) - 3 z^4
];

halfAngleResidual = Together[
  halfAngleLower - z^3 poly[z]/15
];

polyComparisonResidual = Expand[
  poly[z] - (20 - 45 z + 30 z^2 + 7 z^4 + 3 z^8)
];

quadraticDiscriminant = Discriminant[20 - 45 z + 30 z^2, z];

(* epsilon substitutions for the second trigonometric inequality. *)
epsilonResiduals = FullSimplify[{
   1 - 2 (Pi/2 - eps)/Pi - 2 eps/Pi,
   Cos[Pi/2 - eps] - Sin[eps],
   Sin[Pi/2 - eps] - Cos[eps],
   Tan[Pi/2 - eps] - Cot[eps]
  }, Assumptions -> 0 < eps < Pi/2];

round33Residuals = {
  factorResidual,
  squareResidual,
  halfAngleResidual,
  Expand[polyComparisonResidual - 2 z^2 (1 - z^4)],
  quadraticDiscriminant + 375,
  Sequence @@ epsilonResiduals
};

round33LowerQMonotonicityReplayOK = And @@ (# === 0 & /@ round33Residuals);

Print["round33Residuals=", round33Residuals];
Print["round33LowerQMonotonicityReplayOK=", round33LowerQMonotonicityReplayOK];
