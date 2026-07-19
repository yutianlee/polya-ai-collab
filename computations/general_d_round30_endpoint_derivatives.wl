(* Symbolic replay for the Round 30 nonconstant-K endpoint reductions.

   This file checks printed identities and rational arithmetic.  It is not
   a continuum certificate for the still-open retained-E shelf scalar.
*)

ClearAll[R, z, K, mu, q, x, r, p, m, u, rr, d, t, theta, phi, psi,
  kappa, b1, b3, mm, capQ];

g[R_, z_] := (Sqrt[R^2 - z^2] - z ArcCos[z/R])/Pi;

radiusDerivativeResidual = FullSimplify[
  D[g[R, z], R] - Sqrt[1 - z^2/R^2]/Pi,
  Assumptions -> R > z > 0
];

spatialDerivativeResidual = FullSimplify[
  D[g[R, z], z] + ArcCos[z/R]/Pi,
  Assumptions -> R > z > 0
];

(* Lower-shelf transport. *)
shelfTResidual = FullSimplify[
  -Sin[t] (kappa Cos[t] - 1)/(K Sin[t])
  - (1/K - (K Cos[t]) kappa/K^2),
  Assumptions -> K > 0 && 0 < t < Pi/2
];

ratioSquared = K^2/mu^2 (mu^2 - z^2)/(K^2 - z^2);
ratioLogDerivativeResidual = FullSimplify[
  D[Log[ratioSquared], z]
  + 2 z (K^2 - mu^2)/((mu^2 - z^2) (K^2 - z^2)),
  Assumptions -> K > mu > z > 0
];

lambdaDerivativeResidual = FullSimplify[
  -(kappa Sin[t] - t)/Pi - (t - kappa Sin[t])/Pi
];

chiQ = ArcCos[q/mu];
jClosed = mu^2/(2 Pi) (chiQ (1 + 2 Cos[chiQ]^2)
   - 3 Sin[chiQ] Cos[chiQ]);
jPrimeResidual = FullSimplify[
  D[jClosed, mu]
   - mu/Pi (chiQ - Sin[chiQ] Cos[chiQ]),
  Assumptions -> mu > q > 0
];

capDerivativeAuxResidual = FullSimplify[
  D[2 Sin[u]^3/(3 Cos[u]) - u + Sin[u] Cos[u], u]
   - 2 Sin[u]^4/(3 Cos[u]^2),
  Assumptions -> 0 < u < Pi/2
];

capLogDerivativeResidual = FullSimplify[
  D[Log[(2 q + 1)^(3/2)/(q (q + 1))], q]
   + (q^2 + q + 1)/(q (q + 1) (2 q + 1)),
  Assumptions -> q > 0
];

(* Inverse-level transport. *)
inversePhi = Sin[theta] - theta Cos[theta];
thetaK = -inversePhi/(K theta Sin[theta]);
inverseYResidual = FullSimplify[
  Cos[theta] - K Sin[theta] thetaK - Sin[theta]/theta,
  Assumptions -> K > 0 && 0 < theta < Pi/2
];

(* Lower Q-wall parametrization. *)
psiPhi = Tan[phi]^2/Tan[psi]^2;
qWallKMuResidual = FullSimplify[
  (q Sec[psi] Tan[psi] psiPhi)/(q Sec[phi] Tan[phi])
   - Sin[phi]/Sin[psi],
  Assumptions -> 0 < phi < psi < Pi/2
];

qWallTResidual = FullSimplify[
  -Tan[t] (-(1/mu - kappa/K)/Tan[t])
   - (1/mu - kappa/K)
];

qWallCurvature = b1 (1/mu - 1/K) + b3 (1/mu^3 - 1/K^3);
qWallCurvatureResidual = FullSimplify[
  (D[qWallCurvature, mu]
     + D[qWallCurvature, K] kappa)
   - (b1 (-mu^-2 + kappa K^-2)
      + 3 b3 (-mu^-4 + kappa K^-4)),
  Assumptions -> K > mu > 0
];

(* Alpha=0 normalized curvature calculation. *)
qNorm = mm (u + rr + 1);
pNorm = mm rr;
rNorm = mm u;
aNorm = pNorm^2/(3 (2 rNorm + pNorm));
k1Norm = (1 - Cos[t]) pNorm (2 rNorm + pNorm)/(2 Pi qNorm);
normalizedCurvatureResidual = FullSimplify[
  (pNorm + aNorm) k1Norm
   - mm^2 (1 - Cos[t]) rr^2 (3 u + 2 rr)/
      (3 Pi (u + rr + 1)),
  Assumptions -> mm > 0 && u > 0 && rr > 0
];

curvatureCoefficient =
  (1 - Cos[t]) rr^2 (3 u + 2 rr)/(3 Pi (u + rr + 1));
mStationary = (rr - d)/(4 curvatureCoefficient);
continuousMinimumResidual = FullSimplify[
  (curvatureCoefficient mm^2 - mm (rr - d)/2 /. mm -> mStationary)
   + 3 Pi (u + rr + 1) (rr - d)^2/
      (16 (1 - Cos[t]) rr^2 (3 u + 2 rr)),
  Assumptions -> 0 < t < Pi/2 && rr > d > 0 && u > 0
];

zCritical = (1 - 2 d)/(3 d);
supremumCriticalResidual = FullSimplify[
  (1 + zCritical) (1 - d zCritical)^2
   - 4 (1 + d)^3/(27 d),
  Assumptions -> 0 < d < 1/2
];

dOfT = 1 - 2 t/Pi;
hBranch = Pi (1 + dOfT)^3/(72 dOfT (1 - Cos[t]));
hLogDerivativeResidual = FullSimplify[
  D[Log[hBranch], t]
   - (2 (1 - 2 dOfT)/(Pi dOfT (1 + dOfT)) - Cot[t/2]),
  Assumptions -> 0 < t < Pi/2
];

hRewriteResidual = FullSimplify[
  hBranch
   - (Pi - t)^3/(9 Pi (Pi - 2 t) (1 - Cos[t])),
  Assumptions -> 0 < t < Pi/2
];

symbolicResiduals = {
  radiusDerivativeResidual,
  spatialDerivativeResidual,
  shelfTResidual,
  ratioLogDerivativeResidual,
  lambdaDerivativeResidual,
  jPrimeResidual,
  capDerivativeAuxResidual,
  capLogDerivativeResidual,
  inverseYResidual,
  qWallKMuResidual,
  qWallTResidual,
  qWallCurvatureResidual,
  normalizedCurvatureResidual,
  continuousMinimumResidual,
  supremumCriticalResidual,
  hLogDerivativeResidual,
  hRewriteResidual
};

(* Exact arithmetic appearing in the printed estimates. *)
shelfMarginResidual =
  44599/51304 - 5936/35964 - 7/10;

piLower = 333/106;
piUpper = 22/7;
tProbe = 13/10;
sinLowerProbe =
  tProbe - tProbe^3/6 + tProbe^5/120 - tProbe^7/5040;
cosUpperProbe =
  1 - tProbe^2/2 + tProbe^4/24;
tanLowerResidual = sinLowerProbe/cosUpperProbe - tProbe;

tanOneLower =
  (1 - 1/6 + 1/120 - 1/5040)/(1 - 1/2 + 1/24) - 1;

hRationalUpper[t0_] :=
  (piUpper - t0)^3/
   (9 piLower (piLower - 2 t0) (t0^2/2 - t0^4/24));

hLeftUpper = hRationalUpper[4/5];
hRightUpper = hRationalUpper[13/10];

rationalSigns = {
  shelfMarginResidual == 9812441/2306371320,
  shelfMarginResidual > 0,
  tanLowerResidual == 30609129083/13809810000,
  tanLowerResidual > 11/6,
  tanOneLower == 1511/2730,
  tanOneLower > 7/13,
  hLeftUpper == 19359908900/19876504599,
  hRightUpper == 357336260800/634633671763,
  hLeftUpper < 1,
  hRightUpper < 1,
  6825/2209 > 2,
  1521/196 > 2
};

ok = And[
  And @@ (TrueQ[# == 0] & /@ symbolicResiduals),
  And @@ rationalSigns
];

Print["round30EndpointSymbolicResiduals=", symbolicResiduals];
Print["round30ShelfMarginResidual=", shelfMarginResidual];
Print["round30TanLowerResidual=", tanLowerResidual];
Print["round30TanOneLower=", tanOneLower];
Print["round30HEndpointUpperBounds=", {hLeftUpper, hRightUpper}];
Print["round30EndpointRationalSigns=", rationalSigns];
Print["round30EndpointDerivativeReplayOK=", ok];

If[! TrueQ[ok], Exit[1]];
