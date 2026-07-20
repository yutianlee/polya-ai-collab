ClearAll["Global`*"];

b[a_, z_] := ArcCos[z/a]/Pi;

(* Strict midpoint kernel: Mathematica checks identities and pointwise
   derivative signs, not Hermite--Hadamard strictness. *)
dKernel = b[K, z] - b[mu, z];

dKernelPrimeResidual = FullSimplify[
  D[dKernel, z] -
    (1/Pi) (1/Sqrt[mu^2 - z^2] - 1/Sqrt[K^2 - z^2]),
  Assumptions -> K > mu > z > 0
];

dKernelSecondResidual = FullSimplify[
  D[dKernel, {z, 2}] -
    (z/Pi) ((mu^2 - z^2)^(-3/2) - (K^2 - z^2)^(-3/2)),
  Assumptions -> K > mu > z > 0
];

dKernelDerivativeSigns = FullSimplify[
  {
    K^2 - mu^2 > 0,
    (K^2 - z^2)^3 - (mu^2 - z^2)^3 > 0
  },
  Assumptions ->
    Element[{K, mu, z}, Reals] && K > mu > z > 0
];

(* Normalized angular chord and its root-free denominator slack. *)
exactAngularDenominator = 1 - (1 - rho)^2 Cos[t]^2;
rootFreeAngularDenominator = Sin[t]^2 + 2 rho;

angularDenominatorSlackResidual = FullSimplify[
  rootFreeAngularDenominator - exactAngularDenominator -
    rho (2 Sin[t]^2 + rho Cos[t]^2)
];

angularDenominatorSlackPositive = FullSimplify[
  rho (2 Sin[t]^2 + rho Cos[t]^2) > 0,
  Assumptions -> 0 < rho < 1 && 0 < t < Pi/2
];

(* Count interpolation. *)
countInterpolationResidual = FullSimplify[
  ((1 - k) + k (W - 3/4)) - (k W + 1 - 7 k/4)
];

countQuarterResidual = FullSimplify[
  (k W + 1 - 7 k/4 /. k -> 1/4) - (W/4 + 9/16)
];

(* Root-free angular function and mu monotonicity. *)
At = (1 - Cos[t])/Pi;
Cfun[rho_] := At (1 - rho)/Sqrt[Sin[t]^2 + 2 rho];

cRhoDerivativeResidual = FullSimplify[
  D[Cfun[rho], rho] +
    At (Sin[t]^2 + rho + 1)/(Sin[t]^2 + 2 rho)^(3/2),
  Assumptions -> 0 < rho < 1 && 0 < t < Pi/2
];

cRhoDerivativeNegative = FullSimplify[
  -Apos (sSq + rho + 1)/(sSq + 2 rho)^(3/2) < 0,
  Assumptions ->
    Element[{Apos, sSq, rho}, Reals] &&
    Apos > 0 && sSq >= 0 && 0 < rho < 1
];

rMu = 9/10 + 9 zeta/16 + zeta mu L0/4 +
  p^2 Cfun[N/mu] - (p - d m)/2;

rMuDerivativeResidual = FullSimplify[
  D[rMu, mu] -
    (zeta L0/4 +
      p^2 N At (Sin[t]^2 + N/mu + 1)/
        (mu^2 (Sin[t]^2 + 2 N/mu)^(3/2))),
  Assumptions ->
    mu > N > 0 && p > 0 && zeta > 0 && L0 > 0 &&
    0 < t < Pi/2
];

rMuDerivativePositive = FullSimplify[
  zeta L0/4 +
    p^2 N Apos (sSq + N/mu + 1)/
      (mu^2 (sSq + 2 N/mu)^(3/2)) > 0,
  Assumptions ->
    Element[{mu, N, p, zeta, L0, Apos, sSq}, Reals] &&
    mu > N > 0 && p > 0 && zeta > 0 && L0 > 0 &&
    Apos > 0 && sSq >= 0
];

(* Exact selected-scalar loss after the midpoint/chord payment and the
   deletion of only explicitly nonnegative reserves. *)
gammaExact = 1/(2 beta) - J + omegaMinus + B0 zeta +
  p Delta + ap M4 + 2 p ep - (p - d m)/2;

u0 = 1/(2 beta) - J + B0 zeta + p^2 deltaY - (p - d m)/2;

midpointLossResidual = FullSimplify[
  gammaExact - u0 -
    (p (Delta - p deltaY) + omegaMinus + ap M4 + 2 p ep)
];

(* Branch I: mu=p+m+2 and a=(p/2+1)/mu. *)
St = 2 + Sin[t]^2;
Lphase = zeta L0;
XI = (p + 2) (Lphase + 2 d)/8;

rI = 9/10 + 9 zeta/16 - p (1 + d)/2 - d +
  XI/a + p^2 At a/Sqrt[St - 2 a];

branchIRules = {
  mu -> (p + 2)/(2 a),
  m -> (p + 2)/(2 a) - p - 2,
  N -> ((p + 2)/(2 a)) (1 - a)
};

branchIResidual = FullSimplify[
  (rMu /. branchIRules) - rI,
  Assumptions -> 0 < a < 1/2 && p > 0 && 0 < t < Pi/2
];

fI = XI/a + p^2 At a/Sqrt[St - 2 a];

branchIFirstDerivativeResidual = FullSimplify[
  D[fI, a] -
    (-XI/a^2 + p^2 At (St - a)/(St - 2 a)^(3/2))
];

branchISecondDerivativeResidual = FullSimplify[
  D[fI, {a, 2}] -
    (2 XI/a^3 + p^2 At (2 St - a)/(St - 2 a)^(5/2))
];

branchIConvexity = FullSimplify[
  2 Xpos/a^3 + p^2 Apos (2 Spos - a)/(Spos - 2 a)^(5/2) > 0,
  Assumptions ->
    Element[{Xpos, a, p, Apos, Spos}, Reals] &&
    Xpos > 0 && 0 < a < 1/2 && p > 0 && Apos > 0 && Spos > 2
];

(* Branch II: mu0 L0=5/4 and a=1-N/mu0. *)
rII = 9/10 + 7 zeta/8 + d mu0/2 - p (2 + d)/4 - d/2 +
  p^2 At a/Sqrt[St - 2 a] - d mu0 a/2;

branchIIRules = {
  mu -> mu0,
  m -> mu0 (1 - a) - p/2 - 1,
  N -> mu0 (1 - a),
  L0 -> 5/(4 mu0)
};

branchIIResidual = FullSimplify[
  (rMu /. branchIIRules) - rII,
  Assumptions ->
    mu0 > 0 && 0 < a < 1 && p > 0 && 0 < t < Pi/2
];

fII = p^2 At a/Sqrt[St - 2 a] - d mu0 a/2;

branchIIFirstDerivativeResidual = FullSimplify[
  D[fII, a] -
    (p^2 At (St - a)/(St - 2 a)^(3/2) - d mu0/2)
];

branchIISecondDerivativeResidual = FullSimplify[
  D[fII, {a, 2}] -
    p^2 At (2 St - a)/(St - 2 a)^(5/2)
];

branchIIConvexity = FullSimplify[
  p^2 Apos (2 Spos - a)/(Spos - 2 a)^(5/2) > 0,
  Assumptions ->
    Element[{a, p, Apos, Spos}, Reals] &&
    0 < a < 1 && p > 0 && Apos > 0 && Spos > 2
];

(* Algebra behind the global upper bound for L0 used in the proposed
   rational/Sturm continuation. *)
tanMajorant[x_] :=
  x (Pi^2 + (Pi^2/3 - 4) x^2)/(Pi^2 - 4 x^2);

l0MajorantResidual = FullSimplify[
  ((tanMajorant[x] - x)/Pi /. x -> Pi s/2) -
    Pi^2 s^3/(24 (1 - s^2)),
  Assumptions -> 0 < s < 1
];

Print["dKernelPrimeResidual=", dKernelPrimeResidual];
Print["dKernelSecondResidual=", dKernelSecondResidual];
Print["dKernelDerivativeSigns=", dKernelDerivativeSigns];
Print["angularDenominatorSlackResidual=", angularDenominatorSlackResidual];
Print["angularDenominatorSlackPositive=", angularDenominatorSlackPositive];
Print["countInterpolationResidual=", countInterpolationResidual];
Print["countQuarterResidual=", countQuarterResidual];
Print["cRhoDerivativeResidual=", cRhoDerivativeResidual];
Print["cRhoDerivativeNegative=", cRhoDerivativeNegative];
Print["rMuDerivativeResidual=", rMuDerivativeResidual];
Print["rMuDerivativePositive=", rMuDerivativePositive];
Print["midpointLossResidual=", midpointLossResidual];
Print["branchIResidual=", branchIResidual];
Print["branchIFirstDerivativeResidual=", branchIFirstDerivativeResidual];
Print["branchISecondDerivativeResidual=", branchISecondDerivativeResidual];
Print["branchIConvexity=", branchIConvexity];
Print["branchIIResidual=", branchIIResidual];
Print["branchIIFirstDerivativeResidual=", branchIIFirstDerivativeResidual];
Print["branchIISecondDerivativeResidual=", branchIISecondDerivativeResidual];
Print["branchIIConvexity=", branchIIConvexity];
Print["l0MajorantResidual=", l0MajorantResidual];

round40UpperMidpointReplayOK = And[
  dKernelPrimeResidual === 0,
  dKernelSecondResidual === 0,
  dKernelDerivativeSigns === {True, True},
  angularDenominatorSlackResidual === 0,
  angularDenominatorSlackPositive === True,
  countInterpolationResidual === 0,
  countQuarterResidual === 0,
  cRhoDerivativeResidual === 0,
  cRhoDerivativeNegative === True,
  rMuDerivativeResidual === 0,
  rMuDerivativePositive === True,
  midpointLossResidual === 0,
  branchIResidual === 0,
  branchIFirstDerivativeResidual === 0,
  branchISecondDerivativeResidual === 0,
  branchIConvexity === True,
  branchIIResidual === 0,
  branchIIFirstDerivativeResidual === 0,
  branchIISecondDerivativeResidual === 0,
  branchIIConvexity === True,
  l0MajorantResidual === 0
];

Print["round40UpperMidpointReplayOK=", round40UpperMidpointReplayOK];
