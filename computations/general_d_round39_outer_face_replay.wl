(* Round 39 symbolic replay: outer-B floor elimination, cap sharpening,
   and the lower-shelf j>=1 auxiliary estimate.

   This file checks algebraic identities and exact rational comparisons.
   Strict floors, one-sided endpoint ownership, and analytic monotonicity
   remain printed in the companion note. *)

ClearAll["Global`*"];

(* Exact outer-B selected-scalar rewrite. *)
gammaStart = (
  1 - J + B0 zeta + OmegaMinus + omegaB
  + (p + ap) M4 + 2 p ep + p XiHat - (p - dm)/2
);

outerRules = {
  XiHat -> Delta - M4,
  omegaB -> 1/(2 beta) - 1,
  B0 -> v - 3/4
};

gammaOuter = (
  1/(2 beta) - J + OmegaMinus + (v - 3/4) zeta
  + p Delta + ap M4 + 2 p ep - (p - dm)/2
);

gammaOuterResidual = FullSimplify[(gammaStart /. outerRules) - gammaOuter];

(* Intrinsic action coordinates on the outer-B wall. *)
actionCoordinateResiduals = FullSimplify[{
  (j + ep + h) - AxMinusAq,
  (j + u + ep) - AxMinusW,
  (lambda + ep) - AxMinusW,
  u - (v - W)
}, Assumptions -> lambda == j + u &&
                  AxMinusAq == j + ep + h &&
                  AxMinusW == j + u + ep &&
                  u == v - W];

(* Exact loss ledger after adjacent-action and elasticity projection. *)
fOuter = (
  1/(2 beta) - J + OmegaMinus + (v - 3/4) zeta
  + p R1 AxMinusAq + ap g AxMinusW + 2 p ep - (p - dm)/2
);

outerLossLedgerResidual = FullSimplify[
  (p Delta + ap M4 - p R1 AxMinusAq - ap g AxMinusW)
  - (p (Delta - R1 AxMinusAq)
     + ap (M4 - g AxMinusW))
];

(* Root-free old-level reserve after B0=v-3/4 and u=v-W. *)
omegaRFStart = (
  Pi^2/(2 K t^3 Sin[t])
  * (B0 (B0 + 1)/2 - B0 u)
);

omegaRF = (
  Pi^2/(2 K t^3 Sin[t])
  * (v - 3/4) * (W - v/2 + 1/8)
);

omegaRFResidual = FullSimplify[
  (omegaRFStart /. {B0 -> v - 3/4, u -> v - W}) - omegaRF
];

omegaRFPhase = (
  Pi (Tan[t] - t)/(2 W t^3 Tan[t])
  * (v - 3/4) * (W - v/2 + 1/8)
);

omegaRFPhaseResidual = FullSimplify[
  omegaRF - omegaRFPhase,
  Assumptions -> K == mu Sec[t] &&
                 mu == Pi W/(Tan[t] - t) &&
                 0 < t < Pi/2 && W > 0
];

(* Exact elasticity remainder and XiHat branch identity. *)
tau = g/(g + 2);
Rel = Delta - g (lambda + ep);

elasticBranchResidual = FullSimplify[
  tau (E + 2 lambda) - (g (lambda + ep) + tau Rel),
  Assumptions -> E == Delta + 2 ep
];

xiElasticResidual = FullSimplify[
  Delta - (g (lambda + ep) + tau Rel) - (1 - tau) Rel
];

xiMaxResidual = FullSimplify[
  Delta - Max[g (lambda + ep) + tau Rel, K4]
  - Min[(1 - tau) Rel, Delta - K4],
  Assumptions -> Delta == g (lambda + ep) + Rel
];

(* The q>=5 cap sharpening. *)
G[a_, z_] := (Sqrt[a^2 - z^2] - z ArcCos[z/a])/Pi;

capExactResidual = FullSimplify[
  2 Integrate[G[6, z], {z, 5, 6}]
  - (86 ArcCos[5/6] - 15 Sqrt[11])/(2 Pi)
];

u11 = 1/Sqrt[11];
capAlternatingResidual = FullSimplify[
  172 (u11 - u11^3/3 + u11^5/5) - 15 Sqrt[11]
  - 3761/(1815 Sqrt[11])
];

sqrt11Margin = FullSimplify[11 - (33/10)^2];
capPiMargin = FullSimplify[333/530 - 7522/11979];
capThresholdResiduals = FullSimplify[{
  9/10 + 1/5 - 11/10,
  2 (11/10) - 11/5,
  3 - 11/5 - 4/5
}];

(* Series majorant used in the lower-shelf j>=1 lemma. *)
cUpper = (
  8/3 + 4/(15*6) + 3/(35*6^2) + 5/(126*6^3)
  + 8/(99*6^4*(1 - 1/6))
);

cUpperResidual = FullSimplify[cUpper - 451351/166320];

piLower = 333/106;
sqrt6Lower = 2449/1000;

beckerStarkEndpoint = (
  20 cUpper^3/
  (sqrt6Lower^3 piLower (piLower^2 - 2 cUpper^2/3))
);

beckerStarkEndpointResidual = FullSimplify[
  beckerStarkEndpoint
  - 3422243005154215230806750000000/
    1959338986699645823262372838071
];

beckerStark1747Margin = FullSimplify[1747/1000 - beckerStarkEndpoint];
beckerStarkSevenFourthsMargin = FullSimplify[7/4 - 1747/1000];
sqrt6Margin = FullSimplify[6 - sqrt6Lower^2];
denominatorMargin = FullSimplify[piLower^2 - 2 cUpper^2/3];

(* Exact phase--stretch coefficient majorant.  For n >= 2, the
   odd-denominator sum S_(2 n + 2) is bounded termwise by S_6. *)
oddS6Residual = FullSimplify[
  Sum[1/q^6, {q, 1, Infinity, 2}] - Pi^6/960
];

tanCoefficientUpper = FullSimplify[
  8 4^n/Pi^(2 n + 2) * (Pi^6/960)
];

tanCoefficientUpperResidual = FullSimplify[
  tanCoefficientUpper - 4^n/(120 Pi^(2 n - 4))
];

tanMajorantCoefficient = 4^(n - 1)/(3 Pi^(2 n - 2));
tanCoefficientGapResidual = FullSimplify[
  (tanMajorantCoefficient - tanCoefficientUpper)
  - tanCoefficientUpper (10/Pi^2 - 1)
];

tanMajorant = (
  Pi^2 + (Pi^2/3 - 4) x^2
)/(Pi^2 - 4 x^2);

tanMajorantInitialCoefficientResiduals = FullSimplify[{
  SeriesCoefficient[tanMajorant, {x, 0, 0}] - 1,
  SeriesCoefficient[tanMajorant, {x, 0, 2}] - 1/3,
  SeriesCoefficient[tanMajorant, {x, 0, 2 n}]
    - tanMajorantCoefficient
}, Assumptions -> Element[n, Integers] && n >= 1];

piSquaredTenMargin = FullSimplify[10 - Pi^2];

(* Rational phase--stretch residual. *)
kPhase = 8/9 (1 - d^4);
A0Phase = 2 (1 + d)/(
  (484/49) (1 - d^2) + (484/49)^2 d^2/12
);
UPhase = 173/1000 + 61 d/250 + 11 d^2/250;

NPhase = (
  -1117641 + 1354752 d + 2145330 d^2 - 5335616 d^3
  + 27566184 d^4 - 42336000 d^5 + 12584000 d^7
);
PPhase = -NPhase;

phaseRationalResidual = FullSimplify[Together[
  kPhase A0Phase + (1 - kPhase) d/2 - UPhase
  - NPhase/(1089000 (-147 + 26 d^2))
]];

phaseDenominatorMargin = FullSimplify[147 - 26];
phasePEndpointMargins = FullSimplify[{PPhase /. d -> 0, PPhase /. d -> 1}];

(* A primitive integer Sturm chain, normalized only by positive factors,
   hence with exactly the same signs as the Euclidean Sturm chain. *)
Clear[primitivePositivePart];
primitivePositivePart[poly_] := Module[
  {coefficients, commonDenominator, integerCoefficients, commonFactor},
  coefficients = CoefficientList[poly, d];
  commonDenominator = Apply[LCM, Denominator[coefficients]];
  integerCoefficients = commonDenominator coefficients;
  commonFactor = Apply[GCD, Abs[integerCoefficients]];
  Expand[(integerCoefficients/commonFactor) . d^Range[0, Length[coefficients] - 1]]
];

phaseSturmPairs = NestWhileList[
  {#[[2]], -PolynomialRemainder[#[[1]], #[[2]], d]} &,
  {PPhase, D[PPhase, d]},
  (#[[2]] =!= 0) &
];
phaseSturmChain = primitivePositivePart /@ (First /@ phaseSturmPairs);
phaseSturmSigns0 = Sign[phaseSturmChain /. d -> 0];
phaseSturmSigns1 = Sign[phaseSturmChain /. d -> 1];

Clear[signVariations];
signVariations[signs_] := Count[
  Partition[DeleteCases[signs, 0], 2, 1],
  {left_, right_} /; left right < 0
];

phaseSturmVariations = {
  signVariations[phaseSturmSigns0],
  signVariations[phaseSturmSigns1]
};
phaseSturmRootCount = CountRoots[PPhase, {d, 0, 1}];
phaseSturmResiduals = {
  phaseSturmVariations - {3, 3},
  phaseSturmRootCount
};

(* Exact positivity ledger for the final lower-shelf residual. *)
QPhase = 108 - 241 d + 63 d^2 + 196 d^5;
QPhasePrime = 980 d^4 + 126 d - 241;
QPhaseSecond = 3920 d^3 + 126;
QCriticalQuadratic = (540 - 964 d + 189 d^2)/5;

qDerivativeResiduals = FullSimplify[{
  D[QPhase, d] - QPhasePrime,
  D[QPhasePrime, d] - QPhaseSecond,
  QPhase - QCriticalQuadratic - d QPhasePrime/5
}];

qPrimeAtSixteenTwentyFiveResidual = FullSimplify[
  (QPhasePrime /. d -> 16/25) - 316931/78125
];
qCriticalValueResidual = FullSimplify[
  (QCriticalQuadratic /. d -> 16/25) - 284/3125
];

qPositivityMargins = FullSimplify[{
  -(QPhasePrime /. d -> 0),
  QPhasePrime /. d -> 16/25,
  QPhaseSecond /. d -> 0,
  964 - 378,
  QCriticalQuadratic /. d -> 16/25
}];

finalLowerShelfResidual = FullSimplify[Together[
  6/7 + d/(1 - d) (1 - 7 kPhase/4) - d/2
  - QPhase/(126 (1 - d))
]];

allZeroChecks = {
  gammaOuterResidual,
  Sequence @@ actionCoordinateResiduals,
  outerLossLedgerResidual,
  omegaRFResidual,
  omegaRFPhaseResidual,
  elasticBranchResidual,
  xiElasticResidual,
  xiMaxResidual,
  capExactResidual,
  capAlternatingResidual,
  Sequence @@ capThresholdResiduals,
  cUpperResidual,
  beckerStarkEndpointResidual,
  oddS6Residual,
  tanCoefficientUpperResidual,
  tanCoefficientGapResidual,
  Sequence @@ tanMajorantInitialCoefficientResiduals,
  phaseRationalResidual,
  Sequence @@ Flatten[phaseSturmResiduals],
  Sequence @@ qDerivativeResiduals,
  qPrimeAtSixteenTwentyFiveResidual,
  qCriticalValueResidual,
  finalLowerShelfResidual
};

positiveChecks = {
  sqrt11Margin,
  capPiMargin,
  beckerStark1747Margin,
  beckerStarkSevenFourthsMargin,
  sqrt6Margin,
  denominatorMargin,
  piSquaredTenMargin,
  phaseDenominatorMargin,
  Sequence @@ phasePEndpointMargins,
  Sequence @@ qPositivityMargins
};

Print["gammaOuterResidual=", gammaOuterResidual];
Print["actionCoordinateResiduals=", actionCoordinateResiduals];
Print["outerLossLedgerResidual=", outerLossLedgerResidual];
Print["omegaRFResidual=", omegaRFResidual];
Print["omegaRFPhaseResidual=", omegaRFPhaseResidual];
Print["elasticBranchResidual=", elasticBranchResidual];
Print["xiElasticResidual=", xiElasticResidual];
Print["xiMaxResidual=", xiMaxResidual];
Print["capExactResidual=", capExactResidual];
Print["capAlternatingResidual=", capAlternatingResidual];
Print["sqrt11Margin=", sqrt11Margin];
Print["capPiMargin=", capPiMargin];
Print["capThresholdResiduals=", capThresholdResiduals];
Print["cUpperResidual=", cUpperResidual];
Print["beckerStarkEndpointResidual=", beckerStarkEndpointResidual];
Print["beckerStark1747Margin=", beckerStark1747Margin];
Print["beckerStarkSevenFourthsMargin=", beckerStarkSevenFourthsMargin];
Print["sqrt6Margin=", sqrt6Margin];
Print["denominatorMargin=", denominatorMargin];
Print["oddS6Residual=", oddS6Residual];
Print["tanCoefficientUpperResidual=", tanCoefficientUpperResidual];
Print["tanCoefficientGapResidual=", tanCoefficientGapResidual];
Print["tanMajorantInitialCoefficientResiduals=", tanMajorantInitialCoefficientResiduals];
Print["piSquaredTenMargin=", piSquaredTenMargin];
Print["phaseRationalResidual=", phaseRationalResidual];
Print["phaseDenominatorMargin=", phaseDenominatorMargin];
Print["phasePEndpointMargins=", phasePEndpointMargins];
Print["phaseSturmChain=", phaseSturmChain];
Print["phaseSturmSigns0=", phaseSturmSigns0];
Print["phaseSturmSigns1=", phaseSturmSigns1];
Print["phaseSturmVariations=", phaseSturmVariations];
Print["phaseSturmRootCount=", phaseSturmRootCount];
Print["qDerivativeResiduals=", qDerivativeResiduals];
Print["qPrimeAtSixteenTwentyFiveResidual=", qPrimeAtSixteenTwentyFiveResidual];
Print["qCriticalValueResidual=", qCriticalValueResidual];
Print["qPositivityMargins=", qPositivityMargins];
Print["finalLowerShelfResidual=", finalLowerShelfResidual];

round39OuterFaceReplayOK =
  And[
    And @@ (TrueQ[# == 0] & /@ allZeroChecks),
    And @@ (TrueQ[# > 0] & /@ positiveChecks)
  ];

Print["round39OuterFaceReplayOK=", round39OuterFaceReplayOK];
