(* General-d Round 35: exact symbolic replay for Pi/6 <= t. *)
(* The file contains only rational/symbolic identities and coefficient tests. *)
(* It performs no numerical minimization, interval subdivision, or threshold search. *)

ClearAll[
  bernstein1D, bernstein2D, e, eMax, d, x, z, ss, yy, tt, aa,
  piLower, tLower, tUpper, tMin, tStar, fl, cu, dl, d0Coarse, dlNumerator,
  k3, k5, k7, zPoly, zAtMax, zPrimeAtMax, zBar,
  sBar, cBar, cLower, aBar, rBar, uBarPoly, hBar, bBar,
  pPoly, pNorm, pxxNorm, beta, betaFloor, xCenter, qPoly, qNorm,
  gamma, gammaFloor, wUpper, sinUpper, cosLower,
  xb, aAux, uAux, uChord, cAux, du, sLarge, kLarge,
  bz, bx, hardH, dStationary, rStationary, tStationary, tZero,
  hLarge, uEnd
];

bernstein1D[poly_, var_, degree_Integer] := Table[
  Sum[
    Coefficient[poly, var, j] Binomial[k, j]/Binomial[degree, j],
    {j, 0, k}
  ],
  {k, 0, degree}
];

bernstein2D[poly_, var1_, degree1_Integer, var2_, degree2_Integer] :=
  Table[
    Sum[
      Coefficient[Coefficient[poly, var1, i], var2, j]
        Binomial[k, i]/Binomial[degree1, i]
        Binomial[l, j]/Binomial[degree2, j],
      {i, 0, k}, {j, 0, l}
    ],
    {k, 0, degree1}, {l, 0, degree2}
  ];

eMax = 3/7;
d = 1 - e;
piLower = 157/50;
tLower = 157 e/100;
tUpper = 11 e/7;
tMin = 157/300;
tStar = 471/700;

fl[tt_] := tt^3/3 + 2 tt^5/15 + 17 tt^7/315 + 62 tt^9/2835;
cu[tt_] := tt^2/2 - tt^4/24 + tt^6/720;
dl[tt_] := 8 fl[tt]/(3 cu[tt]);
d0Coarse[tt_] := 16 fl[tt]/(3 tt^2);

(* 1. Rational Taylor data and the feasible rectangle. *)

piAndPhaseChecks = {
  FullSimplify[Pi > 157/50],
  FullSimplify[Pi < 22/7],
  Together[piLower e/2 - tLower] === 0,
  Together[11 e/7 - (22/7) e/2] === 0,
  Together[3 (22/7)/14 - 33/49] === 0
};

tangentCoefficientChecks = {
  k3 = 24649/45000;
  Together[k3 - piLower^2/18] === 0,
  k5 = 607573201/1125000000;
  Together[k5 - piLower^4/180] === 0,
  k7 = 254593221134633/472500000000000;
  Together[k7 - 17 piLower^6/30240] === 0
};

zPoly = k3 e^3 + k5 e^5 + k7 e^7;
zAtMax = Together[zPoly /. e -> eMax];
zPrimeAtMax = Together[D[zPoly, e] /. e -> eMax];
zBar = Expand[zAtMax + zPrimeAtMax (e - eMax)];

zSurrogateChecks = {
  zAtMax ===
    754570373701125273/14412002500000000000,
  zPrimeAtMax ===
    122441368634735091/294122500000000000,
  Together[
    D[zPoly, {e, 2}]/e -
      (6 k3 + 20 k5 e^2 + 42 k7 e^4)
  ] === 0,
  Together[61/100 - zPrimeAtMax] ===
    56973356365264909/294122500000000000,
  Together[(100 zBar + 22 - 61 e) /. e -> eMax] ===
    157501698701125273/144120025000000000,
  Together[((zBar + 1 - e)/(2 - e) - 39/100) -
    (100 zBar + 22 - 61 e)/(100 (2 - e))] === 0
};

wUpper = 33/49;
sinUpper = wUpper - wUpper^3/6 + wUpper^5/120;
cosLower = 1 - wUpper^2/2 + wUpper^4/24 - wUpper^6/720;

zUpperChecks = {
  Together[4 cosLower - 5 sinUpper] ===
    4471174903/553651488040,
  cosLower > 0,
  Together[4 (4/5 - 33/49)/(3*3)] === 124/2205,
  Together[3/50 - 124/2205] === 83/22050
};

sBar = 29 e/20;
cBar = 7867/7000 - 4 e/5;
cLower = 1 - tUpper^2/2 + tUpper^4/24 - tUpper^6/720;
aBar = (1 + cBar + cBar^2)/3;

sinCosSurrogateChecks = {
  Together[((tLower - tLower^3/6) - sBar)/e /. e -> eMax] ===
    150321/98000000,
  Factor[D[((tLower - tLower^3/6) - sBar)/e, e]] ===
    -3869893 e/3000000,
  Together[
    D[cLower - cBar, {e, 2}] +
      (11/7)^2 (1 - (11/7)^2 e^2/2 + (11/7)^4 e^4/24)
  ] === 0,
  Together[(cLower - cBar) /. e -> 1/3] ===
    13476352907/1543790178000,
  Together[(cLower - cBar) /. e -> eMax] ===
    18311120763/27682574402000,
  Together[(sBar /. e -> eMax) - 5/8] < 0,
  Together[(cBar /. e -> 1/3)^2 - 3/4] < 0
};

sqrtTaylorIdentities = {
  Factor[(1 - aa/2 - aa^2/8)^2 - (1 - aa)] ===
    aa^3 (8 + aa)/64,
  Factor[(1 - aa/2 - aa^2/8 - aa^3/16)^2 - (1 - aa)] ===
    aa^4 (20 + 4 aa + aa^2)/256,
  Factor[(1 - aa/2)^2 - (1 - aa)] === aa^2/4
};

dlNumerator =
  113400 + 145530 tt^2 + 87075 tt^4 + 47364 tt^6 -
    3049 tt^8 + 62 tt^10;

dlDerivativeResidual = Together[
  D[dl[tt], tt] -
    128 dlNumerator/(63 (360 - 30 tt^2 + tt^4)^2)
];

d0TaylorChecks = {
  dlDerivativeResidual === 0,
  Expand[dlNumerator -
    (113400 + 145530 tt^2 + 87075 tt^4 +
      (47364 - 3049 tt^2) tt^6 + 62 tt^10)] === 0,
  47364 - 3049 > 0,
  Together[d0Coarse[tMin]] ===
    60733103449058607283/58126359375000000000,
  Together[d0Coarse[tMin] - 26/25] > 0,
  Together[26/25 - 41/40] === 3/200
};

d1UpperRectangleChecks = {
  Together[(8/3)^2 - 7] === 1/9,
  Together[(123/20)^2 - 37] === 329/400,
  Together[2/3 + (123/20 - 4)/6] === 41/40
};

feasibleRectangleChecks = And[
  And @@ piAndPhaseChecks,
  And @@ tangentCoefficientChecks,
  And @@ zSurrogateChecks,
  And @@ zUpperChecks,
  And @@ sinCosSurrogateChecks,
  And @@ sqrtTaylorIdentities,
  And @@ d0TaylorChecks,
  And @@ d1UpperRectangleChecks
];

(* 2. Boundary z=z0: one bidegree-(7,9) polynomial. *)

rBar = 2 sBar + cBar^2 (1 - x^2)/2;
uBarPoly = 1 - x^2/2 - x^4/8;
hBar = Expand[uBarPoly rBar + 1 - x^2];
bBar = Expand[2 - aBar (zBar^2 + x^2)/2];

dHatLowerChecks = {
  Together[(uBarPoly /. x -> 3/4) - 13/20] > 0,
  Together[56/181 - 3/10] > 0,
  Together[13/20 + 3/10] === 19/20,
  Together[1 - (3/50)^2 - (499/500)^2] > 0,
  Together[8/63 - 1200/9481] === 248/597303
};

pPoly = Expand[
  4 (x - zBar)^2 (x + zBar) rBar +
    ((1 - e) (1 - x) - (x - zBar)) bBar hBar
];

boundaryClearingResidual = Together[
  2 (x^2 - zBar^2) rBar/(bBar hBar) - 1/2 +
    (1 - e) (1 - x)/(2 (x - zBar)) -
    pPoly/(2 (x - zBar) bBar hBar)
];

pNorm = Expand[pPoly /. {
  e -> 1/3 + 2 ss/21,
  x -> 39/100 + 9 yy/25
}];

pxxNorm = Expand[(D[pPoly, {x, 2}] - 20) /. {
  e -> 1/3 + 2 ss/21,
  x -> 39/100 + 9 yy/25
}];

beta = bernstein2D[pxxNorm, ss, 7, yy, 7];
betaFloor = {
  {2, 6, 8, 11, 12, 13, 14, 13},
  {3, 6, 9, 11, 13, 14, 14, 14},
  {3, 6, 9, 11, 13, 15, 15, 15},
  {3, 6, 9, 12, 14, 15, 16, 16},
  {3, 7, 10, 12, 14, 16, 17, 17},
  {4, 7, 10, 13, 15, 17, 17, 18},
  {4, 7, 10, 13, 15, 17, 18, 19},
  {4, 8, 11, 14, 16, 18, 19, 19}
};

xCenter = 27/50;
qPoly = Expand[
  20 (pPoly /. x -> xCenter) -
    (D[pPoly, x] /. x -> xCenter)^2
];
qNorm = Expand[qPoly /. e -> 1/3 + 2 ss/21];
gamma = bernstein1D[qNorm, ss, 14];
gammaFloor = {51, 51, 51, 50, 48, 46, 43, 40, 36, 32, 27, 21, 15, 9, 2}/100;

bernsteinChecks = {
  {Exponent[pPoly, e], Exponent[pPoly, x]} === {7, 9},
  Count[CoefficientRules[pPoly, {e, x}], _Rule] === 76,
  {Exponent[pxxNorm, ss], Exponent[pxxNorm, yy]} === {7, 7},
  Dimensions[beta] === {8, 8},
  And @@ Flatten[MapThread[Greater, {beta, betaFloor}, 2]],
  Exponent[qPoly, e] === 14,
  Length[gamma] === 15,
  And @@ MapThread[Greater, {gamma, gammaFloor}],
  Together[
    (pPoly /. x -> xCenter) -
      (D[pPoly, x] /. x -> xCenter)^2/20 - qPoly/20
  ] === 0,
  Together[
    (pPoly /. x -> xCenter) -
      (D[pPoly, x] /. x -> xCenter)^2/40 - qPoly/20 -
      (D[pPoly, x] /. x -> xCenter)^2/40
  ] === 0
};

boundaryPolynomialChecks = And[
  And @@ dHatLowerChecks,
  boundaryClearingResidual === 0,
  And @@ bernsteinChecks
];

(* 3. The intrinsic cutoff X_b and the possible stationary root. *)

xb = 9 (1 - e)/(11 - 9 e);
aAux = 10 - 9 e;
uAux[aa_] := 2 Sqrt[aa]/(aa + 1);
uChord = 2/3 + ss/30;

xbConvexityChecks = {
  Together[1 - xb^2 - 4 (10 - 9 e)/(11 - 9 e)^2] === 0,
  FullSimplify[
    D[uAux[aa], {aa, 2}] -
      (3 aa^2 - 6 aa - 1)/(2 aa^(3/2) (aa + 1)^3),
    aa > 0
  ] === 0,
  Together[3 (43/7)^2 - 6 (43/7) - 1] > 0,
  Together[(2/3)^2 - 7/16] > 0,
  Together[(7/10)^2 - 301/625] > 0,
  Together[1/2 - (7/10)^2] === 1/100
};

cAux = 29 e/20 (1 + 7 xb/10);
du = uChord + uChord^2/(7 uChord/10 + cAux);
du = Together[du /. e -> (7 + 2 ss)/21];

duResidual = Together[
  21/20 - du -
    (119903 - 1351 ss - 71590 ss^2 + 7344 ss^3)/
      (180 (47187 + 3759 ss - 1084 ss^2))
];

duPositivityChecks = {
  duResidual === 0,
  Expand[
    119903 - 1351 ss - 71590 ss^2 + 7344 ss^3 - 46962 -
      (1351 (1 - ss) + 71590 (1 - ss^2) + 7344 ss^3)
  ] === 0,
  Expand[
    47187 + 3759 ss - 1084 ss^2 - 46103 -
      (3759 ss + 1084 (1 - ss^2))
  ] === 0,
  46962 > 0,
  46103 > 0
};

qMonotonicityResidual = Together[
  D[aa + aa^2/(7 aa/10 + cAux), aa] -
    (100 cAux^2 + 340 aa cAux + 119 aa^2)/
      (10 cAux + 7 aa)^2
];

dlCutoffChecks = {
  dlDerivativeResidual === 0,
  Together[dl[tMin] - 21/20] ===
    17290676303566582153/908989503696543937500,
  47364 - 3049 > 0
};

hardH = (1 + d) x - z - d;
dStationary = 4 z (x - z)^2/(d (1 - x) bz);
rStationary =
  2/dStationary ((x - z) (x + z)/(bz + bx) + z (x - z)/bz) - 1/2;
tStationary = d (1 - x) bz (x + z) - z (bz + bx) hardH;
tZero = d (1 - x) (x + z) - 2 z hardH;

stationaryChecks = {
  Expand[hardH - ((x - z) - d (1 - x))] === 0,
  Together[
    rStationary -
      tStationary/(2 z (x - z) (bz + bx))
  ] === 0,
  Expand[
    tStationary - bz tZero - z hardH (bz - bx)
  ] === 0,
  Expand[
    tZero -
      (2 z^2 + (3 d - (2 + 3 d) x) z + d x (1 - x))
  ] === 0,
  Factor[
    8 d x (1 - x) - ((2 + 3 d) x - 3 d)^2 +
      (x (2 + d) - d) (x (2 + 9 d) - 9 d)
  ] === 0,
  Together[
    d/(1 + d) - d/(2 + d) - d/((1 + d) (2 + d))
  ] === 0,
  Together[xb - 9 d/(2 + 9 d)] === 0
};

xbAndStationaryChecks = And[
  And @@ xbConvexityChecks,
  And @@ duPositivityChecks,
  qMonotonicityResidual === 0,
  And @@ dlCutoffChecks,
  And @@ stationaryChecks
];

(* 4. For e >= 3/7 the transported Q=1 domain is empty. *)

kLarge[tt_] :=
  -9/2 + 16 tt/3 + 3 tt^2/8 + 32 tt^3/15 - tt^4/80 +
    272 tt^5/315 + 992 tt^7/2835;

largeD0Checks = {
  Factor[16 fl[tt] - 9 cu[tt] - tt^2 kLarge[tt]] === 0,
  Expand[
    D[kLarge[tt], tt] -
      (16/3 + tt (15 - tt^2)/20 + 32 tt^2/5 +
        272 tt^4/63 + 6944 tt^6/2835)
  ] === 0,
  Together[16 fl[tStar] - 9 cu[tStar]] ===
    7448526413453072190883023/
      353094061250000000000000000,
  Together[tStar - tStar^3/6 - 3/5] ===
    15150963/686000000
};

hLarge = Expand[8 zPoly + 2 - 5 e];
largeHardChecks = {
  Together[D[hLarge, e] /. e -> 1/2] ===
    58409062334633/540000000000000,
  Together[
    (hLarge + D[hLarge, e] (1/2 - e)) /. e -> eMax
  ] === 564730015345396183/3603000625000000000,
  Factor[D[hLarge, {e, 2}] - 8 D[zPoly, {e, 2}]] === 0,
  Together[
    (zPoly + 1 - e)/(2 - e) - 3/8 -
      hLarge/(8 (2 - e))
  ] === 0
};

uEnd = Sqrt[55]/8;
largeD1Checks = {
  Together[55 - (131/18)^2] === 659/324,
  PolynomialRemainder[
    Expand[
      (3/2 - aa) (aa + 3/5) - aa^2 -
        (9 aa/10 - 131/160)
    ],
    aa^2 - 55/64,
    aa
  ] === 0,
  FullSimplify[uEnd > 131/144],
  FullSimplify[uEnd + uEnd^2/(uEnd + 3/5) < 3/2]
};

largePhaseEmptyChecks = And[
  And @@ largeD0Checks,
  And @@ largeHardChecks,
  And @@ largeD1Checks
];

round35LargephaseReplayOK = And[
  feasibleRectangleChecks,
  boundaryPolynomialChecks,
  xbAndStationaryChecks,
  largePhaseEmptyChecks
];

Print["feasibleRectangleChecks=", feasibleRectangleChecks];
Print["taylorCheckGroups=", {
  And @@ tangentCoefficientChecks,
  And @@ sinCosSurrogateChecks,
  And @@ sqrtTaylorIdentities,
  And @@ d0TaylorChecks
}];
Print["boundaryPolynomialDegree=", {Exponent[pPoly, e], Exponent[pPoly, x]}];
Print["boundaryPolynomialTermCount=", Count[CoefficientRules[pPoly, {e, x}], _Rule]];
Print["bernsteinPXXDominatesTable=", bernsteinChecks[[5]]];
Print["bernsteinPXXMinimumMargin=", Min[Flatten[beta - betaFloor]]];
Print["bernsteinQDominatesTable=", bernsteinChecks[[8]]];
Print["bernsteinQMinimumMargin=", Min[gamma - gammaFloor]];
Print["boundaryPolynomialChecks=", boundaryPolynomialChecks];
Print["xbConvexityChecks=", And @@ xbConvexityChecks];
Print["xbActionCutoffChecks=", And[And @@ duPositivityChecks, And @@ dlCutoffChecks]];
Print["stationaryChecks=", And @@ stationaryChecks];
Print["largePhaseEmptyChecks=", largePhaseEmptyChecks];
Print["round35LargephaseReplayOK=", round35LargephaseReplayOK];
