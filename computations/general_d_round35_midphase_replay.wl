(* General-d Round 35: exact symbolic replay for Pi/8 <= t <= Pi/6. *)
(* No optimization, interval subdivision, or numerical certification is used. *)

ClearAll[
  aa, s0, x, z, p, m, gap, y, w, t, u, ux, vx, vAlt, d1,
  d1Alt, Bfun, phi, kappa, fullMomentFactor, lowResidual, uUpper,
  pPoly, pFourthCoefficients, pr, ratioR, ratioK, yy, ww, statRel,
  ratioStat, q1, q2, q1Lower, q2Lower, b1, b2, wfun
];

aa = 87/100;
s0 = 1/125;

(* 1. Exact rational bounds used at t = Pi/8 and t = Pi/6. *)

rootAndPiChecks = {
  (140/99)^2 < 2,
  (99/70)^2 > 2,
  (43/25)^2 < 3,
  FullSimplify[Pi < 22/7]
};

phaseLowerIdentities = Together[{
  140/99 - 1 - 11/28 - 59/2772,
  4 (59/2772)/(3 (22/7)) - 59/6534,
  59/6534 - 1/125
}];

a2LowerIdentity = Together[7/12 + (43/25)/6 - 87/100];

safeEndpointMargins = Together[{
  (2 - 99/70)/4 - (3/8)^2,
  (2 + 140/99)/4 - (9/10)^2
}];

safeLinearDerivativeResidual = Expand[
  D[Sin[t] + Cos[t] u, t] - (Cos[t] - u Sin[t])
];

safeLinearDerivativeLowerResidual = Expand[
  (Cos[t] - u Sin[t]) - (Cos[t] - Sin[t]) -
    (1 - u) Sin[t]
];

angleDifferenceDerivativeResidual = Expand[
  D[Cos[t] - Sin[t], t] + Sin[t] + Cos[t]
];

angleDifferenceEndpointMargin = Together[(43/25 - 1)/2];

phaseDerivativeResidual = FullSimplify[
  D[Tan[t] - t, t] - Tan[t]^2,
  0 < t < Pi/2
];

d0DerivativeRatioResidual = FullSimplify[
  D[Sin[t]/Cos[t]^2, t] - (1 + Sin[t]^2)/Cos[t]^3,
  0 < t < Pi/2
];

(* 2. The action condition forces X < 7/8. *)

ux = Sqrt[1 - x^2];
vx = Sqrt[1 - Cos[t]^2 x^2];
d1 = ux + (vx - Sin[t])/Cos[t]^2;
vAlt = Sqrt[ux^2 + Sin[t]^2 x^2];
d1Alt = ux + ux^2/(vAlt + Sin[t]);

d1RepresentationResidual = FullSimplify[
  d1 - d1Alt,
  0 < x < 1 && 0 < t < Pi/2
];

d1XDerivativeResidual = FullSimplify[
  D[d1, x] + x/ux + x/vx,
  0 < x < 1 && 0 < t < Pi/2
];

d1TDerivativeResidual = FullSimplify[
  D[d1Alt, t] +
    ux^2 Cos[t] (1 + Sin[t] x^2/vAlt)/(vAlt + Sin[t])^2,
  0 < x < 1 && 0 < t < Pi/2
];

cosPi8RationalMargin = Together[
  (2 + 140/99)/4 - (4619/5000)^2
];

d0RationalLower = Together[8 (59/2772)/(3 (381/5000))];
d0RationalGap = Together[d0RationalLower - 37/50];

uAtSevenEighthsMargin = Together[(31/64)^2 - 15/64];
vAtSevenEighthsMargin = Together[
  (158 - 49 (99/70))/256 - (47/80)^2
];
d1RationalUpper = Together[31/64 + (15/64)/(77/80)];
d1RationalGap = Together[73/100 - d1RationalUpper];

(* 3. Correlated D1 upper bound and binomial lower shelf quadrature. *)

Bfun[u_] := u (15 + 76 u)/(15 + 36 u);

BderivativeResidual = Together[
  D[Bfun[u], u] - (75 + 760 u + 912 u^2)/(3 (5 + 12 u)^2)
];

vLowerSquareResidual = TrigExpand[
  (1 - Cos[t]^2 x^2) - Cos[t]^2 (1 - x^2) - Sin[t]^2
] // FullSimplify;

BformulaResidual = Together[
  u + u^2/(3/8 + 9 u/10) - Bfun[u]
];

binomialSquareResidual = Factor[
  1 - (1 - w) (1 + w/2 + 3 w^2/8)^2 -
    w^3 (40 + 15 w + 9 w^2)/64
];

phi[y_] := y^2/2 + aa y^4/8 + aa^2 y^6/16;
kappa[y_] := 1 + aa y^2/4 + aa^2 y^4/8;

phiDerivativeResidual = Expand[
  D[phi[y], y] - y (1 + aa y^2/2 + 3 aa^2 y^4/8)
];

phiDifferenceResidual = Factor[
  phi[x] - phi[z] -
    (x - z) (x + z)/2
      (1 + aa (x^2 + z^2)/4 +
       aa^2 (x^4 + x^2 z^2 + z^4)/8)
];

fullMomentFactor =
  1 + aa (x^2 + z^2)/4 +
    aa^2 (x^4 + x^2 z^2 + z^4)/8;

kappaDiscardResidual = Expand[
  fullMomentFactor - kappa[x] -
    (aa z^2/4 + aa^2 (x^2 z^2 + z^4)/8)
];

targetUpperResidual = Together[
  1/2 - (2/3) m/(2 p) - (3 p - 2 m)/(6 p)
];

(* 4. Low-X reduction: monotonicity in z and one rational polynomial. *)

p = x - z;
m = 1 - x;
gap = 3 p - 2 m;
lowResidual = 6 kappa[x] p^2 (x + z) - Bfun[u] gap;

lowZDerivativeResidual = Together[
  D[lowResidual, z] -
    (3 Bfun[u] - 6 kappa[x] p (x + 3 z))
];

radiusQuadraticIdentity = Factor[
  4 x^2/3 - (x - z) (x + 3 z) - (x - 3 z)^2/3
];

kappaAtThreeFifths = Together[kappa[3/5]];
BAtFourFifths = Together[Bfun[4/5]];
lowZDerivativeMargin = Together[
  3 BAtFourFifths - 6 kappaAtThreeFifths (12/25)
];

uUpper = 1 - x^2/2 - x^4/8 - x^6/16 - 5 x^8/128;

sqrtUpperSquareResidual = Factor[
  uUpper^2 - (1 - x^2) -
    x^10 (896 + 224 x^2 + 80 x^4 + 25 x^6)/16384
];

uUpperAtThreeFifths = Together[uUpper /. x -> 3/5];

pPoly = Expand[
  6 (x - s0)^2 (x + s0) kappa[x] (15 + 36 uUpper) -
    (5 x - 3 s0 - 2) uUpper (15 + 76 uUpper)
];

pFourthCoefficients = CoefficientList[
  Expand[D[pPoly, {x, 4}] /. x -> 2/5 + y],
  y
];

pFourthCoefficientSigns = Sign /@ pFourthCoefficients;
pFourthAllNegative = And @@ Thread[pFourthCoefficients < 0];

pTaylorChecks = {
  Length[pFourthCoefficients] == 14,
  (D[pPoly, {x, 3}] /. x -> 3/5) > 1900,
  (D[pPoly, {x, 2}] /. x -> 253/625) > 1300,
  (pPoly /. x -> 5/9) > 7/1000,
  -7/25 < (D[pPoly, x] /. x -> 5/9) < 0
};

pThirdEndpointMargin = Together[
  (D[pPoly, {x, 3}] /. x -> 3/5) - 1900
];

pStrongConvexityMargin = Together[
  7/1000 - (7/25)^2/(2 1300)
];

(* 5. High-X calculus reduction for R. *)

ratioR = pr^2 (2 x - pr)/(3 pr - 2 (1 - x));
ratioK = pr (1 - pr) - 4 x (1 - x)/3;

ratioDerivativeResidual = Together[
  D[ratioR, pr] -
    6 pr ratioK/(3 pr - 2 (1 - x))^2
];

hardEndpointKIdentity = Factor[
  (ratioK /. pr -> 2 (1 - x)/3) -
    2 (1 - x) (-3 + 4 (1 - x))/9
];

outerEndpointDerivativeResidual = Together[
  D[x^3/(5 x - 2), x] - x^2 (10 x - 6)/(5 x - 2)^2
];

ratioStat = (1 - ww)^2 (1 + 2 yy + ww)/
  (4 (1 + 2 yy - 3 ww));
statRel = 3 ww^2 - (4 yy^2 - 1);

stationaryEquationResidual = Expand[
  (ratioK /. {x -> (1 + yy)/2, pr -> (1 - ww)/2}) -
    (-1 - 3 ww^2 + 4 yy^2)/12
];

ratioStationaryResidual = Together[
  (ratioR /. {x -> (1 + yy)/2, pr -> (1 - ww)/2}) -
    ratioStat
];

q1 = 44 - 37 yy - 125 yy^2 + 250 yy^3 +
  ww (118 - 375 yy + 125 yy^2);

q2 = 11 + 2 yy - 20 yy^2 + 40 yy^3 +
  ww (7 - 60 yy + 20 yy^2);

q1ReductionResidual = PolynomialReduce[
  125 (1 - ww)^2 (1 + 2 yy + ww) -
    108 (1 + 2 yy - 3 ww) - 4 q1/3,
  {statRel}, ww
][[2]];

q2ReductionResidual = PolynomialReduce[
  5 (1 - ww)^2 (1 + 2 yy + ww) -
    3 (1 + 2 yy - 3 ww) - q2/3,
  {statRel}, ww
][[2]];

b1 = 118 - 375 yy + 125 yy^2;
b2 = 7 - 60 yy + 20 yy^2;

q1Lower = Expand[(q1 /. ww -> 2/5)];
q2Lower = Expand[(q2 /. ww -> 3 yy/2 - 19/40)];

q1BoundChecks = {
  Together[q1Lower -
    (456 - 935 yy - 375 yy^2 + 1250 yy^3)/5] === 0,
  (q1Lower /. yy -> 3/5) === 6,
  (D[q1Lower, yy] /. yy -> 3/5) === -7,
  Expand[D[q1Lower, {yy, 2}] - (1500 yy - 150)] === 0,
  (b1 /. yy -> 1/2) === -153/4,
  Expand[D[b1, yy] - (-375 + 250 yy)] === 0,
  Together[4/25 - 11/75] === 1/75
};

wfun[yy_] := Sqrt[(4 yy^2 - 1)/3];

wConcavityResidual = FullSimplify[
  D[wfun[yy], {yy, 2}] + 4/(9 wfun[yy]^3),
  yy > 1/2
];

tangentRationalMargins = Together[{
  (13/20)^2 - 5/12,
  12/5 - (3/2)^2
}];

q2BoundChecks = {
  Together[q2Lower -
    (307 + 1640 yy - 4780 yy^2 + 2800 yy^3)/40] === 0,
  (q2Lower /. yy -> 3/4) === 59/80,
  (D[q2Lower, yy] /. yy -> 3/4) === -161/8,
  Expand[D[q2Lower, {yy, 2}] - (-239 + 420 yy)] === 0,
  (b2 /. yy -> 3/5) === -109/5,
  Expand[D[b2, yy] - (-60 + 40 yy)] === 0
};

highQuadratureConstants = Together[{
  1 + aa (3/5)^2/4,
  Bfun[4/5],
  1 + aa (4/5)^2/4,
  Bfun[3/5]
}];

highRangeMargins = Together[{
  6 (10783/10000) (27/125) - 1516/1095,
  6 (712/625) (3/20) - 303/305
}];

round35MidphaseReplayOK = And[
  And @@ rootAndPiChecks,
  phaseLowerIdentities === {0, 0, 841/816750},
  a2LowerIdentity === 0,
  safeEndpointMargins === {13/2240, 431/9900},
  safeLinearDerivativeResidual === 0,
  safeLinearDerivativeLowerResidual === 0,
  angleDifferenceDerivativeResidual === 0,
  angleDifferenceEndpointMargin === 9/25,
  phaseDerivativeResidual === 0,
  d0DerivativeRatioResidual === 0,
  d1RepresentationResidual === 0,
  d1XDerivativeResidual === 0,
  d1TDerivativeResidual === 0,
  cosPi8RationalMargin === 319061/2475000000,
  d0RationalLower === 590000/792099,
  d0RationalGap === 192337/39604950,
  uAtSevenEighthsMargin === 1/4096,
  vAtSevenEighthsMargin === 17/12800,
  d1RationalUpper === 3587/4928,
  d1RationalGap === 261/123200,
  BderivativeResidual === 0,
  vLowerSquareResidual === 0,
  BformulaResidual === 0,
  binomialSquareResidual === 0,
  phiDerivativeResidual === 0,
  phiDifferenceResidual === 0,
  kappaDiscardResidual === 0,
  targetUpperResidual === 0,
  lowZDerivativeResidual === 0,
  radiusQuadraticIdentity === 0,
  kappaAtThreeFifths === 54528089/50000000,
  BAtFourFifths === 1516/1095,
  lowZDerivativeMargin === 11550045527/11406250000,
  sqrtUpperSquareResidual === 0,
  uUpperAtThreeFifths === 8002279/10000000,
  pFourthAllNegative,
  And @@ pTaylorChecks,
  pThirdEndpointMargin === 6799998428550153647/97656250000000000,
  pStrongConvexityMargin === 5663/812500,
  ratioDerivativeResidual === 0,
  hardEndpointKIdentity === 0,
  outerEndpointDerivativeResidual === 0,
  stationaryEquationResidual === 0,
  ratioStationaryResidual === 0,
  q1ReductionResidual === 0,
  q2ReductionResidual === 0,
  And @@ q1BoundChecks,
  wConcavityResidual === 0,
  tangentRationalMargins === {7/1200, 3/20},
  And @@ q2BoundChecks,
  highQuadratureConstants === {10783/10000, 1516/1095, 712/625, 303/305},
  highRangeMargins === {1779637/136875000, 6069/190625}
];

Print["rootAndPiChecks=", rootAndPiChecks];
Print["phaseLowerIdentities=", phaseLowerIdentities];
Print["safeEndpointMargins=", safeEndpointMargins];
Print["safeLinearMonotonicityData=", {
  safeLinearDerivativeResidual, safeLinearDerivativeLowerResidual,
  angleDifferenceDerivativeResidual, angleDifferenceEndpointMargin
}];
Print["actionMonotonicityResiduals=", {
  phaseDerivativeResidual, d0DerivativeRatioResidual,
  d1RepresentationResidual, d1XDerivativeResidual, d1TDerivativeResidual
}];
Print["actionRationalMargins=", {
  cosPi8RationalMargin, d0RationalGap,
  uAtSevenEighthsMargin, vAtSevenEighthsMargin, d1RationalGap
}];
Print["quadratureResiduals=", {
  BderivativeResidual, vLowerSquareResidual, BformulaResidual,
  binomialSquareResidual, phiDerivativeResidual,
  phiDifferenceResidual, kappaDiscardResidual, targetUpperResidual
}];
Print["lowXReductionResiduals=", {
  lowZDerivativeResidual, radiusQuadraticIdentity,
  sqrtUpperSquareResidual
}];
Print["lowZDerivativeMargin=", lowZDerivativeMargin];
Print["pFourthCoefficientSigns=", pFourthCoefficientSigns];
Print["pFourthAllNegative=", pFourthAllNegative];
Print["pTaylorChecks=", pTaylorChecks];
Print["pStrongConvexityMargin=", pStrongConvexityMargin];
Print["ratioCalculusResiduals=", {
  ratioDerivativeResidual, hardEndpointKIdentity,
  outerEndpointDerivativeResidual, stationaryEquationResidual,
  ratioStationaryResidual, q1ReductionResidual, q2ReductionResidual
}];
Print["q1BoundChecks=", q1BoundChecks];
Print["q2BoundChecks=", q2BoundChecks];
Print["highRangeMargins=", highRangeMargins];
Print["round35MidphaseReplayOK=", round35MidphaseReplayOK];
