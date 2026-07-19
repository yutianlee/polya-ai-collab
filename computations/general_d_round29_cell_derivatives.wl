(* Symbolic replay for the Round 29 complete-terminal phase reduction. *)

ClearAll[theta, t, K, q, B, mu, ePrime, wPrime, tau, k4, a2, a4,
  beta, g, z, r, x, p, m, f0, b1, b3];

f = Sin[theta] - theta Cos[theta];
thetaPrime = -Tan[t] f/(theta Sin[theta]);
kPrime = K Tan[t];

yPrimeResidual = FullSimplify[
  kPrime Cos[theta] - K Sin[theta] thetaPrime
   - K Tan[t] Sin[theta]/theta,
  Assumptions -> 0 < theta < Pi/2 && 0 < t < Pi/2 && K > 0
];

inverseAngleResidual = FullSimplify[
  D[Pi/(2 theta), theta] thetaPrime
   + Pi thetaPrime/(2 theta^2)
];

v = q/Pi (Tan[theta] - theta);
vPrime = D[v, theta];
top = Pi (v - B)^2/theta;
topDerivativeResidual = FullSimplify[
  D[top, theta]
   - Pi (v - B)/theta^2 (2 theta vPrime - (v - B))
];

topGapDerivativeResidual = FullSimplify[
  D[theta vPrime - v, theta]
   - 2 q theta Sec[theta]^2 Tan[theta]/Pi
];

elasticDerivativeResidual = FullSimplify[
  tau (ePrime - 2 wPrime) - tau ePrime + 2 tau wPrime
];

k4 = (a2 (1 - Cos[t])/(2 Pi mu)
  + a4 (1 - Cos[t]^3)/(24 Pi mu^3));
k4DerivativeResidual = FullSimplify[
  D[k4, t]
   - (a2 Sin[t]/(2 Pi mu)
      + a4 Cos[t]^2 Sin[t]/(8 Pi mu^3))
];

outerWallJumpResidual = FullSimplify[
  1/(2 beta) - 9/(16 beta) + 1/(16 beta)
];

(* Fixed-K wall identities from Proposition 1A. *)
g[a_, zz_] := (Sqrt[a^2 - zz^2] - zz ArcCos[zz/a])/Pi;

fixedKActionResidual = FullSimplify[
  D[g[K, z] - g[mu, z] - g[K, mu], mu]
   - (ArcCos[mu/K] - Sqrt[1 - z^2/mu^2])/Pi,
  Assumptions -> K > mu > z > 0
];

chiQ = ArcCos[q/mu];
jClosed = mu^2/(2 Pi) (chiQ (1 + 2 Cos[chiQ]^2)
   - 3 Sin[chiQ] Cos[chiQ]);
jPrimeResidual = FullSimplify[
  D[jClosed, mu]
   - mu/Pi (chiQ - Sin[chiQ] Cos[chiQ]),
  Assumptions -> mu > q > 0
];

uFixed = Sqrt[mu^2 - r^2];
vFixed = Sqrt[mu^2 - x^2];
omegaFixed = uFixed/(uFixed + vFixed);
fixedKWeightResidual = FullSimplify[
  D[omegaFixed, mu]
   - mu (vFixed/uFixed - uFixed/vFixed)/(uFixed + vFixed)^2,
  Assumptions -> mu > x > r > 0
];

fixedKCurvature = b1 (1/mu - 1/K) + b3 (1/mu^3 - 1/K^3);
fixedKCurvatureResidual = FullSimplify[
  D[fixedKCurvature, mu]
   + b1/mu^2 + 3 b3/mu^4,
  Assumptions -> K > mu > 0 && b1 > 0 && b3 > 0
];

eFixed = g[K, r] - g[mu, r] + g[K, x] - g[mu, x]
  + 1/2 - 2 f0;
eStarFixed = 1/2 - m/(2 p) + m ArcCos[mu/K]/(p Pi);
fixedKGapResidual = FullSimplify[
  D[eFixed - eStarFixed, mu]
   - (-(Sqrt[1 - r^2/mu^2] + Sqrt[1 - x^2/mu^2])/Pi
      + m/(p Pi K Sqrt[1 - mu^2/K^2])),
  Assumptions -> K > mu > x > r > 0 && p > 0
];

primaryFaceArithmetic = FullSimplify[{
  7/4 - 1 + 5/32 - 29/32,
  29/32 - 1/9 - 229/288,
  29/32 + 14/495 - 4/5 - 2131/15840,
  2131/15840 - 1/9 - 371/15840
}];

residuals = {
  yPrimeResidual,
  inverseAngleResidual,
  topDerivativeResidual,
  topGapDerivativeResidual,
  elasticDerivativeResidual,
  k4DerivativeResidual,
  outerWallJumpResidual,
  fixedKActionResidual,
  jPrimeResidual,
  fixedKWeightResidual,
  fixedKCurvatureResidual,
  fixedKGapResidual
};

ok = And @@ (TrueQ[# == 0] & /@ Join[residuals, primaryFaceArithmetic]);

Print["round29CellDerivativeResiduals=", residuals];
Print["round29PrimaryFaceArithmetic=", primaryFaceArithmetic];
Print["round29CellDerivativeReplayOK=", ok];

If[! TrueQ[ok], Exit[1]];
