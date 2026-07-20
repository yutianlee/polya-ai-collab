(* Round 44 exact Gate-B terminal/trapezoid replay.

   The symbolic checks below replay identities and elementary calculus only.
   The final high-precision fixture is diagnostic, not directed interval
   arithmetic and not a continuum sign certificate. *)

ClearAll["Global`*"];
$MaxExtraPrecision = 5000;

(* Ball-action and shelf calculus. *)
g[aa_, zz_] := (Sqrt[aa^2 - zz^2] - zz ArcCos[zz/aa])/Pi;

gPrimeResidual = FullSimplify[
  D[g[aa, zz], zz] + ArcCos[zz/aa]/Pi,
  Assumptions -> aa > zz > 0
];
gSecondResidual = FullSimplify[
  D[g[aa, zz], {zz, 2}] - 1/(Pi Sqrt[aa^2 - zz^2]),
  Assumptions -> aa > zz > 0
];

aAction[zz_] := g[kk, zz] - g[mu, zz];
aPrimeResidual = FullSimplify[
  D[aAction[zz], zz] -
   (ArcCos[zz/mu] - ArcCos[zz/kk])/Pi,
  Assumptions -> kk > mu > zz > 0
];
aSecondResidual = FullSimplify[
  D[aAction[zz], {zz, 2}] -
   (1/(Pi Sqrt[kk^2 - zz^2]) -
     1/(Pi Sqrt[mu^2 - zz^2])),
  Assumptions -> kk > mu > zz > 0
];
minusASecondDerivativeResidual = FullSimplify[
  D[-D[aAction[zz], {zz, 2}], zz] -
   zz/Pi ((mu^2 - zz^2)^(-3/2) -
     (kk^2 - zz^2)^(-3/2)),
  Assumptions -> kk > mu > zz > 0
];

shelfWeightResidual = FullSimplify[
  Integrate[uu (pp - uu), {uu, 0, pp}] - pp^3/6,
  Assumptions -> pp > 0
];

(* Exact hinge ledger for C_p >= a_p Delta. *)
ap = pp^2/(3 (2 rr + pp));
linearHingeResidual = FullSimplify[
  pp^3/6 - ap pp (rr + pp/2),
  Assumptions -> pp > 0 && rr > 0
];
oldHingeLossResidual = FullSimplify[
  pp^3/6 - ap pp (rr - ss + pp/2) -
   pp^3 ss/(3 (2 rr + pp)),
  Assumptions -> pp > 0 && 0 <= ss <= rr
];
interiorHingeLossResidual = FullSimplify[
  (pp ll^2/2 - ll^3/3) - ap ll^2/2 -
   (ll^2 (pp - ll)/3 + pp rr ll^2/(3 (2 rr + pp))),
  Assumptions -> pp > 0 && rr > 0 && 0 <= ll <= pp
];

(* Literal/gap-side ownership reconciliation. *)
vWall = b0 + 3/4;
bGap = b0 + 1;
newLevelResidual = FullSimplify[bGap - 1/4 - vWall];
lPlus = omegaMinus + b0 zeta + 1/(2 beta) - jj;
lZero = omegaMinus + b0 zeta + 9/(16 beta) - jj;
lDifferenceResidual = FullSimplify[lZero - lPlus - 1/(16 beta)];

remainderTailResidual = FullSimplify[
  2 Integrate[(ell - vWall)/beta, {ell, vWall, b0 + 1}] -
   1/(16 beta),
  Assumptions -> beta > 0
];

(* The top Bregman lower bound obtained from Y'' >= cTop. *)
cTop = 1/(Pi ukq beta^3);
topBregmanCoefficientResidual = FullSimplify[
  2 Integrate[cTop (vWall - ell)^2/2, {ell, b0, vWall}] -
   9/(64 Pi ukq beta^3),
  Assumptions -> beta > 0 && ukq > 0
];

(* Exact Gate-B and Round-42 loss ledgers. *)
eSum = delta + 2 ep;
eStar = (pp - dd mm)/(2 pp);
dqPlus = lPlus + rTanPlus;
dqZero = lZero + rTanZero;
sPlus = dqPlus + cp + pp (eSum - eStar);
sZero = dqZero + cp + pp (eSum - eStar);
phiPlus = lPlus + ap delta + pp (eSum - eStar);

plusLedgerResidual = FullSimplify[
  sPlus - phiPlus - (rTanPlus + cp - ap delta)
];
zeroLedgerResidual = FullSimplify[
  sZero - phiPlus -
   (1/(16 beta) + rTanZero + cp - ap delta),
  Assumptions -> rTanPlus == rTanZero + 1/(16 beta)
];
twoOwnerScalarResidual = FullSimplify[
  sPlus - sZero,
  Assumptions -> rTanPlus == rTanZero + 1/(16 beta)
];
round42EndpointResidual = FullSimplify[
  phiPlus -
   (lPlus + (pp + ap) delta + 2 pp ep - (pp - dd mm)/2)
];

(* High-precision Round-43 fixture.  It must be rejected by E < E_*.
   It also replays the two terminal decompositions and curvature reserve. *)
wp = 90;
wallTol = 10^-65;
strictFloor[x_?NumericQ] := Module[{nn = Round[x]},
  If[Abs[x - nn] < wallTol, Max[0, nn - 1], Max[0, Ceiling[x] - 1]]
];
ordinaryFloor[x_?NumericQ] := Module[{nn = Round[x]},
  If[Abs[x - nn] < wallTol, Max[0, nn], Max[0, Floor[x]]]
];
ballIntegral[aa_?NumericQ, zz_?NumericQ] := If[zz >= aa, 0,
  Module[{thh = ArcCos[zz/aa]},
   aa^2/(4 Pi) (thh (1 + 2 Cos[thh]^2) -
     3 Sin[thh] Cos[thh])]
];

r0 = SetPrecision[1, wp];
p0 = SetPrecision[9, wp];
m0 = SetPrecision[9, wp];
q0 = r0 + p0 + m0;
mu0 = q0 + 1;
bGap0 = 3;
b00 = bGap0 - 1;
theta0 = thh /. FindRoot[
   q0/Pi (Tan[thh] - thh) == bGap0 - 1/4,
   {thh, SetPrecision[0.95, wp]}, WorkingPrecision -> wp,
   AccuracyGoal -> 72, PrecisionGoal -> 72
];
t0 = ArcCos[mu0 Cos[theta0]/q0];
k0 = mu0 Sec[t0];
x0 = r0 + p0;
d0 = 1 - 2 t0/Pi;
ball0[aa_?NumericQ, zz_?NumericQ] := If[zz < aa, g[aa, zz], 0];
shell0[zz_?NumericQ] := ball0[k0, zz] - ball0[mu0, zz];
shellIntegral0[zz_] := ballIntegral[k0, zz] - ballIntegral[mu0, zz];
f0 = 4;
e00 = shell0[r0] + 1/4 - f0;
ep0 = shell0[x0] + 1/4 - f0;
eSum0 = e00 + ep0;
delta0 = e00 - ep0;
eStar0 = (p0 - d0 m0)/(2 p0);
qCount0 = strictFloor[shell0[q0] + 1/4];
jMax0 = Ceiling[k0 - q0] + 2;
dq0 = 2 shellIntegral0[q0] - qCount0 -
  2 Sum[strictFloor[shell0[q0 + ii] + 1/4], {ii, 1, jMax0}];
cp0 = 2 (shellIntegral0[r0] - shellIntegral0[x0]) -
  p0 (shell0[r0] + shell0[x0]);
ap0 = p0^2/(3 (2 r0 + p0));
curvature0 = p0^3/(6 Pi) (1/Sqrt[mu0^2 - r0^2] -
    1/Sqrt[k0^2 - r0^2]);

beta0 = ArcCos[q0/k0]/Pi;
h0 = g[mu0, q0];
j0 = 2 ballIntegral[mu0, q0];
oldAngles0 = Table[
  aa /. FindRoot[
    k0/Pi (Sin[aa] - aa Cos[aa]) ==
     SetPrecision[kkLevel - 1/4, wp],
    {aa, SetPrecision[0.5, 80]}, WorkingPrecision -> 80,
    AccuracyGoal -> 62, PrecisionGoal -> 62],
  {kkLevel, 1, b00}
];
oldY0 = k0 Cos[#] - q0 & /@ oldAngles0;
oldEta0 = (# - strictFloor[#]) & /@ oldY0;
omegaMinus0 = Total[MapThread[
   Pi/(2 #1) - Pi/(2 t0) + 2 #2 &,
   {oldAngles0, oldEta0}
]];
zeta0 = Pi/(2 t0) - 1;
lPlus0 = omegaMinus0 + b00 zeta0 + 1/(2 beta0) - j0;
lZero0 = omegaMinus0 + b00 zeta0 + 9/(16 beta0) - j0;
rTanPlus0 = dq0 - lPlus0;
rTanZero0 = dq0 - lZero0;
s0 = dq0 + cp0 + p0 (eSum0 - eStar0);
phi0 = lPlus0 + ap0 delta0 + p0 (eSum0 - eStar0);

fixture = N[<|
  "r" -> r0, "p" -> p0, "m" -> m0, "f" -> f0,
  "B" -> bGap0, "B0" -> b00, "t" -> t0,
  "shelfFloors" -> {ordinaryFloor[shell0[r0] + 1/4],
    ordinaryFloor[shell0[x0] + 1/4],
    ordinaryFloor[shell0[x0 + 1] + 1/4]},
  "E" -> eSum0, "EStar" -> eStar0,
  "hardOwnerRejected" -> (eSum0 >= eStar0),
  "Dq" -> dq0, "Cp" -> cp0, "curvatureReserve" -> curvature0,
  "apDelta" -> ap0 delta0, "LPlus" -> lPlus0, "LZero" -> lZero0,
  "RTanPlus" -> rTanPlus0, "RTanZero" -> rTanZero0,
  "remainderDifference" -> (rTanPlus0 - rTanZero0),
  "expectedDifference" -> 1/(16 beta0),
  "PhiPlus" -> phi0, "S" -> s0,
  "ledgerResidual" -> (s0 - phi0 -
    (rTanPlus0 + cp0 - ap0 delta0))
|>, 35];

fixtureChecks = And[
  ordinaryFloor[shell0[r0] + 1/4] == f0,
  ordinaryFloor[shell0[x0] + 1/4] == f0,
  ordinaryFloor[shell0[x0 + 1] + 1/4] != f0,
  eSum0 > eStar0,
  qCount0 == b00,
  cp0 > curvature0 > 0,
  rTanPlus0 > 0,
  rTanZero0 > 0,
  Abs[rTanPlus0 - rTanZero0 - 1/(16 beta0)] < 10^-60,
  Abs[s0 - phi0 - (rTanPlus0 + cp0 - ap0 delta0)] < 10^-60,
  s0 > 0
];

round44ExactGateBReplayOK = And[
  gPrimeResidual === 0,
  gSecondResidual === 0,
  aPrimeResidual === 0,
  aSecondResidual === 0,
  minusASecondDerivativeResidual === 0,
  shelfWeightResidual === 0,
  linearHingeResidual === 0,
  oldHingeLossResidual === 0,
  interiorHingeLossResidual === 0,
  newLevelResidual === 0,
  lDifferenceResidual === 0,
  remainderTailResidual === 0,
  topBregmanCoefficientResidual === 0,
  plusLedgerResidual === 0,
  zeroLedgerResidual === 0,
  twoOwnerScalarResidual === 0,
  round42EndpointResidual === 0,
  TrueQ[fixtureChecks]
];

Print["gPrimeResidual=", gPrimeResidual];
Print["gSecondResidual=", gSecondResidual];
Print["aPrimeResidual=", aPrimeResidual];
Print["aSecondResidual=", aSecondResidual];
Print["minusASecondDerivativeResidual=", minusASecondDerivativeResidual];
Print["shelfWeightResidual=", shelfWeightResidual];
Print["linearHingeResidual=", linearHingeResidual];
Print["oldHingeLossResidual=", oldHingeLossResidual];
Print["interiorHingeLossResidual=", interiorHingeLossResidual];
Print["newLevelResidual=", newLevelResidual];
Print["lDifferenceResidual=", lDifferenceResidual];
Print["remainderTailResidual=", remainderTailResidual];
Print["topBregmanCoefficientResidual=", topBregmanCoefficientResidual];
Print["plusLedgerResidual=", plusLedgerResidual];
Print["zeroLedgerResidual=", zeroLedgerResidual];
Print["twoOwnerScalarResidual=", twoOwnerScalarResidual];
Print["round42EndpointResidual=", round42EndpointResidual];
Print["round43Fixture=", fixture];
Print["round43FixtureChecks=", fixtureChecks];
Print["round44ExactGateBReplayOK=", round44ExactGateBReplayOK];
