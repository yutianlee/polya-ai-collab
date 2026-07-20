(* Round 45 localized support-sign symbolic replay.

   This file proves the new old-level aggregate algebraically and replays the
   focused endpoint fixtures at high precision.  Its numerical portion is a
   diagnostic, not directed interval arithmetic and not a positive coverage
   certificate.  Directed classification of the R45-CF counterexample is in
   general_d_round45_support_sign_diagnostic.py. *)

ClearAll["Global`*"];
$MaxExtraPrecision = 10000;

(* Ball action and the exact outer-wall derivative. *)
g[aa_, zz_] := (Sqrt[aa^2 - zz^2] - zz ArcCos[zz/aa])/Pi;
gPrimeAResidual = FullSimplify[
  D[g[aa, zz], aa] - Sqrt[aa^2 - zz^2]/(Pi aa),
  Assumptions -> aa > zz > 0
];
outerKDerivativeResidual = FullSimplify[
  D[mu Sec[tt], tt] - mu Sec[tt] Tan[tt]
];
outerWallDerivative = Sqrt[mu^2 Sec[tt]^2 - qq^2] Tan[tt]/Pi;
outerWallDerivativeResidual = FullSimplify[
  (Sqrt[aa^2 - qq^2]/(Pi aa) D[mu Sec[tt], tt] /.
      aa -> mu Sec[tt]) - outerWallDerivative,
  Assumptions -> mu Sec[tt] > qq > 0 && 0 < tt < Pi/2
];
outerWallDerivativePositive = FullSimplify[
  outerWallDerivative > 0,
  Assumptions -> mu Sec[tt] > qq > 0 && mu > 0 && 0 < tt < Pi/2
];

(* Inverse action: ell(theta)=G_K(K cos theta), Y=K cos theta-q. *)
ellOfTheta = kk/Pi (Sin[th] - th Cos[th]);
yOfTheta = kk Cos[th] - qq;
yPrimeByEll = FullSimplify[
  D[yOfTheta, th]/D[ellOfTheta, th],
  Assumptions -> kk > 0 && 0 < th < Pi/2
];
ySecondByEll = FullSimplify[
  D[yPrimeByEll, th]/D[ellOfTheta, th],
  Assumptions -> kk > 0 && 0 < th < Pi/2
];
ySecondResidual = FullSimplify[
  ySecondByEll - Pi^2/(kk Sin[th] th^3),
  Assumptions -> kk > 0 && 0 < th < Pi/2
];
denominatorDerivative = FullSimplify[D[th^3 Sin[th], th]];
denominatorDerivativePositive = FullSimplify[
  denominatorDerivative > 0,
  Assumptions -> 0 < th < Pi/2
];

(* Every old interval has theta<t because ell<=B0<W=G_K(mu).
   Strong convexity around ell_k=k-1/4 therefore gives the following
   uniform Bregman moment. *)
oldLayerMoment = Integrate[
  (ell - (k - 1/4))^2,
  {ell, k - 1, k},
  Assumptions -> Element[k, Integers]
];
oldLayerMomentResidual = FullSimplify[oldLayerMoment - 7/48];
cOld = Pi^2/(kk tt^3 Sin[tt]);
oldLayerLower = cOld oldLayerMoment;
oldLayerLowerResidual = FullSimplify[oldLayerLower - 7 cOld/48];
oldAggregateLower = b0 oldLayerLower;
oldAggregateResidual = FullSimplify[
  oldAggregateLower - 7 Pi^2 b0/(48 kk tt^3 Sin[tt])
];

(* Combine only disjoint ledger pieces: the primary u-retaining Omega bound
   and all old Bregman areas.  The top interval is not in this identity. *)
sumDelta = b0 (b0 + 1)/2 - b0 uu;
omegaPrimary = cOld sumDelta/2;
combinedOld = cOld b0 (12 b0 + 19 - 24 uu)/48;
combinedOldResidual = FullSimplify[
  omegaPrimary + oldAggregateLower - combinedOld
];
wallPositionResidual = FullSimplify[
  combinedOld - cOld b0 (ww/2 - b0/4 + 1/48),
  Assumptions -> uu == b0 + 3/4 - ww
];

(* The literal top interval is disjoint from every [k-1,k]. *)
vWall = b0 + 3/4;
cTop = 1/(Pi ukq beta^3);
topCoefficientResidual = FullSimplify[
  2 Integrate[cTop (vWall - ell)^2/2, {ell, b0, vWall}] -
   9/(64 Pi ukq beta^3),
  Assumptions -> beta > 0 && ukq > 0
];

(* Gap-side/literal reconciliation is bookkeeping, not an added reserve. *)
lPlus = omega + b0 zeta + 1/(2 beta) - jj;
lZero = omega + b0 zeta + 9/(16 beta) - jj;
reconciliationResidual = FullSimplify[lZero - lPlus - 1/(16 beta)];

(* Strict implication chain.  Adjacent action gives
     E = Delta+2 ep > R1(j+ep+h)+2 ep >= R1 h.
   CF therefore makes the S31 strict support impossible. *)
eIdentityResidual = FullSimplify[eSum - (delta + 2 ep),
  Assumptions -> eSum == delta + 2 ep];
lossIdentityResidual = FullSimplify[
  pp ((pp - dd mm)/(2 pp) - eSum) -
   ((pp - dd mm)/2 - pp eSum)
];
supportCoarseResidual = FullSimplify[
  (1/5 + 9/(16 beta) - 1/10) - 49/40,
  Assumptions -> beta == 1/2
];
actionDropIdentityResidual = FullSimplify[
  (ff - 1/4 + ep) - (bb - 1/4 - hh) - (jj0 + ep + hh),
  Assumptions -> jj0 == ff - bb
];
supportMargin30 =
  pp (eStarSymbol - eSum) -
   (omega + b0 zeta + 9/(16 beta) - jj + topSymbol + cCurvSymbol);
literalScalarSymbol =
  omega + b0 zeta + 9/(16 beta) - jj +
   rTanZero + cp - pp (eStarSymbol - eSum);
supportSlackIdentityResidual = FullSimplify[
  literalScalarSymbol -
   (-supportMargin30 + (rTanZero - topSymbol) +
     (cp - cCurvSymbol))
];

(* Shelf curvature lower bound: this is the only C_p bound combined with the
   terminal aggregate.  The hinge bound is not added. *)
shelfWeightResidual = FullSimplify[
  Integrate[ss (pp - ss), {ss, 0, pp}] - pp^3/6,
  Assumptions -> pp > 0
];

(* High-precision fixtures. *)
wp = 100;
wallTol = 10^-72;
strictFloor[x_?NumericQ] := Module[{nn = Round[x]},
  If[Abs[x - nn] < wallTol, Max[0, nn - 1], Max[0, Ceiling[x] - 1]]
];
ordinaryFloor[x_?NumericQ] := Module[{nn = Round[x]},
  If[Abs[x - nn] < wallTol, Max[0, nn], Max[0, Floor[x]]]
];
ball[aa_?NumericQ, zz_?NumericQ] := If[zz < aa, g[aa, zz], 0];
ballIntegral[aa_?NumericQ, zz_?NumericQ] := If[zz >= aa, 0,
  Module[{theta = ArcCos[zz/aa]},
    aa^2/(4 Pi) (theta (1 + 2 Cos[theta]^2) -
      3 Sin[theta] Cos[theta])]
];

fixture[rIn_, pIn_, mIn_, bIn_, gammaIn_] := Module[
  {rr, pp0, mm, qq0, mu0, b, b00, target, t0, k0, xx,
   action, cap, f0, e0, ep0, ee, del, dd0, estar, hh, ww0, uu0,
   beta0, zeta0, jj0, jmax, dq, cp, ccurv, top, ur, ux, uq,
   rone, cf, oldAngles, oldY, oldEta, omega0, capj, lzero,
   rtan0, ss0, omegaLB, oldLB, combinedLB, termSigned,
   inverseRows, activity},
  rr = SetPrecision[rIn, wp]; pp0 = SetPrecision[pIn, wp];
  mm = SetPrecision[mIn, wp]; b = bIn; b00 = b - 1;
  xx = rr + pp0; qq0 = xx + mm; mu0 = qq0 + 1;
  target = SetPrecision[b - 1/4, wp];
  t0 = tt0 /. FindRoot[
    g[mu0 Sec[tt0], qq0] == target,
    {tt0, SetPrecision[1.2, wp], SetPrecision[1.48, wp]},
    WorkingPrecision -> wp, AccuracyGoal -> 78, PrecisionGoal -> 78
  ];
  k0 = mu0 Sec[t0];
  action[z_?NumericQ] := ball[k0, z] - ball[mu0, z];
  cap[z_?NumericQ] := ballIntegral[k0, z] - ballIntegral[mu0, z];
  f0 = ordinaryFloor[action[rr] + 1/4];
  e0 = action[rr] + 1/4 - f0;
  ep0 = action[xx] + 1/4 - f0;
  ee = e0 + ep0; del = e0 - ep0;
  dd0 = 1 - 2 t0/Pi; estar = (pp0 - dd0 mm)/(2 pp0);
  hh = g[mu0, qq0]; ww0 = g[k0, mu0];
  uu0 = target - ww0; beta0 = ArcCos[qq0/k0]/Pi;
  zeta0 = Pi/(2 t0) - 1; jj0 = f0 - b;
  activity = k0^2 - Pi^2/(1 - Cos[t0])^2 - gammaIn;
  jmax = Ceiling[k0 - qq0] + 2;
  dq = 2 cap[qq0] - strictFloor[action[qq0] + 1/4] -
    2 Sum[strictFloor[action[qq0 + n] + 1/4], {n, 1, jmax}];
  cp = 2 (cap[rr] - cap[xx]) - pp0 (action[rr] + action[xx]);
  ccurv = pp0^3/(6 Pi) (1/Sqrt[mu0^2 - rr^2] -
    1/Sqrt[k0^2 - rr^2]);
  top = 9/(64 Pi Sqrt[k0^2 - qq0^2] beta0^3);
  ur = Sqrt[mu0^2 - rr^2]; ux = Sqrt[mu0^2 - xx^2];
  uq = Sqrt[mu0^2 - qq0^2]; rone = (ur - ux)/(ux - uq);
  cf = pp0 rone hh + 49/40 + top + ccurv - (pp0 - dd0 mm)/2;
  oldAngles = Table[
    aa /. FindRoot[
      k0/Pi (Sin[aa] - aa Cos[aa]) == SetPrecision[lev - 1/4, 70],
      {aa, SetPrecision[0.45, 70]}, WorkingPrecision -> 70,
      AccuracyGoal -> 55, PrecisionGoal -> 55],
    {lev, 1, b00}
  ];
  oldY = k0 Cos[#] - qq0 & /@ oldAngles;
  oldEta = (# - strictFloor[#]) & /@ oldY;
  omega0 = Total[MapThread[
    Pi/(2 #1) - Pi/(2 t0) + 2 #2 &,
    {oldAngles, oldEta}
  ]];
  capj = 2 ballIntegral[mu0, qq0];
  lzero = omega0 + b00 zeta0 + 9/(16 beta0) - capj;
  rtan0 = dq - lzero;
  ss0 = dq + cp + pp0 (ee - estar);
  omegaLB = Pi^2/(2 k0 t0^3 Sin[t0]) *
    (b00 (b00 + 1)/2 - b00 uu0);
  oldLB = 7 Pi^2 b00/(48 k0 t0^3 Sin[t0]);
  combinedLB = Pi^2 b00/(k0 t0^3 Sin[t0]) *
    (ww0/2 - b00/4 + 1/48);
  termSigned = pp0 rone (action[xx] - action[qq0]) + combinedLB + b00 zeta0 +
    9/(16 beta0) - capj + top + ccurv - (pp0 - dd0 mm)/2;
  inverseRows = MapThread[{#1, #2} &, {oldY, oldEta}];
  N[<|
    "tuple" -> {rr, pp0, mm, f0, b, jj0}, "t" -> t0, "K" -> k0,
    "shelfFloors" -> {ordinaryFloor[action[rr] + 1/4],
      ordinaryFloor[action[xx] + 1/4],
      ordinaryFloor[action[xx + 1] + 1/4]},
    "activity" -> activity, "h_u_beta" -> {hh, uu0, beta0},
    "E" -> ee, "EStar" -> estar, "Delta" -> del,
    "A(x)-A(q)" -> action[xx] - action[qq0],
    "actionDropIdentityResidual" ->
      action[xx] - action[qq0] - (jj0 + ep0 + hh),
    "adjacentSlack" -> del - rone (jj0 + ep0 + hh),
    "D_A" -> dq, "C_p" -> cp, "S" -> ss0,
    "CF_RHSMinusLHS" -> cf, "Omega" -> omega0,
    "OmegaPrimary" -> omegaLB, "Rtan0" -> rtan0,
    "oldAggregateLower" -> oldLB,
    "Rtan0MinusOldAndTop" -> rtan0 - oldLB - top,
    "combinedIdentityResidual" -> omegaLB + oldLB - combinedLB,
    "remainingTerminalSigned" -> termSigned,
    "reconciliation" -> 1/(16 beta0), "top9over64" -> top,
    "minOldInverseWallDistance" -> Min[Abs[oldY - Round[oldY]]],
    "oldInverseRows" -> inverseRows
  |>, 38]
];

round45RouteFixture = fixture[1, 6, 11, 19, 3/4];
round44MinimumFixture = fixture[1, 3, 1, 2, 3/4];
round43RejectedFixture = fixture[1, 9, 9, 3, 3/4];

fixtureChecks = And[
  round45RouteFixture["shelfFloors"] == {21, 21, 20},
  round45RouteFixture["E"] < round45RouteFixture["EStar"] < 1/2,
  round45RouteFixture["CF_RHSMinusLHS"] < -0.46,
  round45RouteFixture["S"] > 31,
  round45RouteFixture["adjacentSlack"] > 0,
  round45RouteFixture["Omega"] > round45RouteFixture["OmegaPrimary"] > 0,
  round45RouteFixture["Rtan0MinusOldAndTop"] > 0,
  Abs[round45RouteFixture["combinedIdentityResidual"]] < 10^-70,
  Abs[round44MinimumFixture["S"] -
    2.69456527890035502562933] < 10^-22,
  round43RejectedFixture["E"] > round43RejectedFixture["EStar"],
  round43RejectedFixture["S"] > 0
];

round45SupportSignReplayOK = And[
  gPrimeAResidual === 0,
  outerKDerivativeResidual === 0,
  outerWallDerivativeResidual === 0,
  TrueQ[outerWallDerivativePositive],
  ySecondResidual === 0,
  TrueQ[denominatorDerivativePositive],
  oldLayerMomentResidual === 0,
  oldLayerLowerResidual === 0,
  oldAggregateResidual === 0,
  combinedOldResidual === 0,
  wallPositionResidual === 0,
  topCoefficientResidual === 0,
  reconciliationResidual === 0,
  eIdentityResidual === 0,
  lossIdentityResidual === 0,
  supportCoarseResidual === 0,
  actionDropIdentityResidual === 0,
  supportSlackIdentityResidual === 0,
  shelfWeightResidual === 0,
  TrueQ[fixtureChecks]
];

Print["gPrimeAResidual=", gPrimeAResidual];
Print["outerKDerivativeResidual=", outerKDerivativeResidual];
Print["outerWallDerivative=", outerWallDerivative];
Print["outerWallDerivativeResidual=", outerWallDerivativeResidual];
Print["outerWallDerivativePositive=", outerWallDerivativePositive];
Print["yPrimeByEll=", yPrimeByEll];
Print["ySecondByEll=", ySecondByEll];
Print["ySecondResidual=", ySecondResidual];
Print["denominatorDerivative=", denominatorDerivative];
Print["denominatorDerivativePositive=", denominatorDerivativePositive];
Print["oldLayerMoment=", oldLayerMoment];
Print["oldLayerMomentResidual=", oldLayerMomentResidual];
Print["oldAggregateResidual=", oldAggregateResidual];
Print["combinedOldResidual=", combinedOldResidual];
Print["wallPositionResidual=", wallPositionResidual];
Print["topCoefficientResidual=", topCoefficientResidual];
Print["reconciliationResidual=", reconciliationResidual];
Print["lossIdentityResidual=", lossIdentityResidual];
Print["supportCoarseResidual=", supportCoarseResidual];
Print["actionDropIdentityResidual=", actionDropIdentityResidual];
Print["supportSlackIdentityResidual=", supportSlackIdentityResidual];
Print["shelfWeightResidual=", shelfWeightResidual];
Print["round45RouteFixture=", round45RouteFixture];
Print["round44MinimumFixture=", round44MinimumFixture];
Print["round43RejectedFixture=", round43RejectedFixture];
Print["fixtureChecks=", fixtureChecks];
Print["round45SupportSignReplayOK=", round45SupportSignReplayOK];
