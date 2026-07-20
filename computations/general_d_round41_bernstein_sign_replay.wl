(* Round 41 exact Bernstein sign replay.

   This is a fixed finite rational-arithmetic audit of the rational lower
   envelopes introduced in general-d-round-41-rational-branch-elimination.md.
   It deliberately contains no Resolve/Reduce/CAD call and no numerical
   sampling.  Every verification cell is fixed below.

   Bernstein rule used here.  If P(alpha+(beta-alpha) z)=Sum[a_j z^j],
   degree n, then

     P = Sum[b_k Binomial[n,k] z^k (1-z)^(n-k)],
     b_k = Sum_{j<=k} a_j Binomial[k,j]/Binomial[n,j].

   The tensor rule is the product of the two one-variable rules.  Thus
   nonnegative Bernstein coefficients prove nonnegativity on the stated
   closed cell.  The exact Round 41 scalars are strictly above the rational
   envelopes, so nonnegativity (rather than strict positivity) is enough. *)

ClearAll["Global`*"];

(* ---------- exact rational data ---------- *)

d = 1 - s;
ellMinus = 49 s^3/(121 (1 - s^2));
ellPlus = 121 s^3/(294 (1 - s^2));
Aminus = 333 s^2/848 - 1331 s^4/16464;
tUpper = 11 s/7;
sinUpper = tUpper - tUpper^3/6 + tUpper^5/120;
Splus = 2 + sinUpper^2;

aLowerI = d (p + 2)/(2 (p + d (p + 2)));
aUpperI = 2 (p + 2) ellPlus/5;
HminusI = 2 d + 49 s^2/(121 (1 + s));
DplusI = Splus - 2 aLowerI;
cConstantI = Together[9/10 + 9 d/(16 s) - d];
cSlopeI = (2 - s)/2;
cI = cConstantI - cSlopeI p;

gII = 2 ellMinus (p + 2)/5;
hII = 1 - 4 ellPlus (p (1 + d/2) + d)/(5 d);
MminusII = 5 d/(8 ellPlus);
cII = 9/10 + 7 d/(8 s) - p (3 - s)/4 - d/2;

(* ---------- exact Bernstein transforms ---------- *)

ClearAll[
  bernstein1D, bernstein2D, signTriple, nonnegativeQ,
  positiveConstantQ
];

bernstein1D[poly_, variable_, {left_, right_}] := Module[
  {transformed, degree, powers},
  transformed = Expand[
    poly /. variable -> left + (right - left) zBernstein
  ];
  degree = Exponent[transformed, zBernstein];
  powers = CoefficientList[transformed, zBernstein];
  Table[
    Sum[
      powers[[j + 1]] Binomial[k, j]/Binomial[degree, j],
      {j, 0, k}
    ],
    {k, 0, degree}
  ]
];

bernstein2D[
  poly_, {variable1_, left1_, right1_}, {variable2_, left2_, right2_}
] := Module[
  {transformed, degree1, degree2, powers},
  transformed = Expand[
    poly /. {
      variable1 -> left1 + (right1 - left1) zBernstein1,
      variable2 -> left2 + (right2 - left2) zBernstein2
    }
  ];
  degree1 = Exponent[transformed, zBernstein1];
  degree2 = Exponent[transformed, zBernstein2];
  powers = Association[CoefficientRules[
    transformed, {zBernstein1, zBernstein2}
  ]];
  Table[
    Sum[
      Lookup[powers, Key[{i, j}], 0]
      Binomial[k, i]/Binomial[degree1, i]
      Binomial[l, j]/Binomial[degree2, j],
      {i, 0, k}, {j, 0, l}
    ],
    {k, 0, degree1}, {l, 0, degree2}
  ]
];

signTriple[list_] := With[
  {signs = Sign[Flatten[list]]},
  {Count[signs, 1], Count[signs, 0], Count[signs, -1]}
];

nonnegativeQ[list_] := Min[Sign[Flatten[list]]] >= 0;

positiveConstantQ[expression_] :=
  NumberQ[expression] && TrueQ[expression > 0];

allChecks = {};

ClearAll[record1D, recordTensor, recordCoefficientFamily];

record1D[name_, poly_, interval_] := Module[{coefficients, rowOK},
  coefficients = bernstein1D[poly, s, interval];
  rowOK = nonnegativeQ[coefficients];
  AppendTo[allChecks, rowOK];
  Print[
    name, " s=", interval,
    " degree=", Exponent[poly, s],
    " signs(+/0/-)=", signTriple[coefficients],
    " OK=", rowOK
  ];
];

recordTensor[name_, poly_, sInterval_, vInterval_] := Module[
  {coefficients, rowOK},
  coefficients = bernstein2D[
    poly, {s, sInterval[[1]], sInterval[[2]]},
    {v, vInterval[[1]], vInterval[[2]]}
  ];
  rowOK = nonnegativeQ[coefficients];
  AppendTo[allChecks, rowOK];
  Print[
    name, " cell=", {sInterval, vInterval},
    " degrees=", {Exponent[poly, s], Exponent[poly, v]},
    " signs(+/0/-)=", signTriple[coefficients],
    " OK=", rowOK
  ];
];

recordCoefficientFamily[name_, poly_, xVariable_, interval_] := Module[
  {family, coefficientTables, rowOK},
  family = CoefficientList[poly, xVariable];
  coefficientTables = bernstein1D[#, s, interval] & /@ family;
  rowOK = And @@ (nonnegativeQ /@ coefficientTables);
  AppendTo[allChecks, rowOK];
  Print[
    name, " s=", interval,
    " xDegree=", Exponent[poly, xVariable],
    " sDegrees=", (Exponent[#, s] & /@ family),
    " signs(+/0/-)=", signTriple[coefficientTables],
    " OK=", rowOK
  ];
];

(* ---------- Branch I-B: the endpoint cubic ---------- *)

(* Since aLowerI > d/(2(1+d)), DplusI is strictly below D0. *)
D0 = Together[Splus - d/(1 + d)];
d0Gap = Factor[Together[D0 - DplusI]];
Print["D0-DplusI=", d0Gap];
AppendTo[allChecks, Together[
  d0Gap - 2 d/( (1 + d) (p + d (p + 2)) )
] === 0];

E0 = Together[cConstantI + 5 HminusI/(16 ellPlus)];
C0 = cSlopeI;
KNumerator = Together[2 ellPlus Aminus/5];
Q0 = Together[4 C0^2 - 36 C0 E0 - 27 E0^2];
ZRat = Together[KNumerator^2 Q0^2 - 16 C0^6 D0];
ZDenominator = Factor[Denominator[ZRat]];
ZPolynomial = Expand[Numerator[ZRat]];

Print["IB Z denominator (positive on 0<s<1)=", ZDenominator];
AppendTo[allChecks, positiveConstantQ[Together[
  ZDenominator/((s - 1)^2 s^2 (1 + s)^2)
]]];
AppendTo[allChecks, PolynomialQ[ZPolynomial, s]];
Do[
  record1D["IB-Z", ZPolynomial, interval],
  {interval, {{0, 1/3}, {1/3, 2/3}, {2/3, 1}}}
];

(* cConstantI-67/80=(4s-3)^2/(16s), so E0>0.  Also Q0<0
   follows already from E0>=67/80 and 0<C0<1, for instance from
   Q0 < 4-27(67/80)^2 < 0.  Z>0 is the squared form of
   (KNumerator/Sqrt[D0])(-Q0)>4 C0^3. *)
cConstantLowerIdentity = Together[
  cConstantI - 67/80 - (4 s - 3)^2/(16 s)
];
AppendTo[allChecks, cConstantLowerIdentity === 0];
Print["IB cConstant lower-bound identity OK=", cConstantLowerIdentity === 0];

(* ---------- Branch I-A: translated coefficient families ---------- *)

p0IA = Together[(cConstantI + 5 HminusI/(8 ellPlus))/cSlopeI];
polyIA0 = Together[
  HminusI^2 Aminus^2 p^4 (p + 2)^2/4 - cI^4 D0
];

translatedIALowRat = Together[polyIA0 /. p -> p0IA + x];
translatedIALowDenominator = Factor[Denominator[translatedIALowRat]];
translatedIALowPolynomial = Expand[Numerator[translatedIALowRat]];
Print[
  "IA p0-chart denominator (positive on 0<s<2/3)=",
  translatedIALowDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedIALowDenominator/((s - 2)^6 s^14 (1 + s)^2)
]]];
Do[
  recordCoefficientFamily[
    "IA-p0", translatedIALowPolynomial, x, interval
  ],
  {interval, {{0, 1/3}, {1/3, 2/3}}}
];

translatedIAHighRat = Together[polyIA0 /. p -> 3 + x];
translatedIAHighDenominator = Factor[Denominator[translatedIAHighRat]];
(* Its denominator contains the single negative factor s-2. *)
translatedIAHighPolynomial = Expand[-Numerator[translatedIAHighRat]];
Print[
  "IA p=3 chart denominator (negative on 2/3<s<1)=",
  translatedIAHighDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedIAHighDenominator/((s - 2) s^4 (1 + s)^2)
]]];
recordCoefficientFamily[
  "IA-p3", translatedIAHighPolynomial, x, {2/3, 1}
];

(* ---------- Branch II domain and increasing-slope endpoint ---------- *)

(* ellMinus is increasing: ellMinus' has the displayed positive factor.
   The phase base gives ellMinus<5/24, whereas ellMinus(2/3)>5/24. *)
ellMinusDerivative = Factor[D[ellMinus, s]];
phaseCapGap = Together[ellMinus /. s -> 2/3] - 5/24;
Print["ellMinus'=", ellMinusDerivative];
Print["ellMinus(2/3)-5/24=", phaseCapGap];
AppendTo[allChecks, phaseCapGap > 0];

dGII = Together[Splus - 2 gII];
eGII = Together[cII + MminusII (1 - gII)];
pCII = Together[p /. First[Solve[cII + MminusII == 0, p]]];
polyGIIPlus = Together[
  p^4 Aminus^2 gII^2 - eGII^2 dGII
];
translatedGPlusRat = Together[polyGIIPlus /. p -> pCII + x];
translatedGPlusDenominator = Factor[Denominator[translatedGPlusRat]];
translatedGPlusPolynomial = Expand[Numerator[translatedGPlusRat]];
Print["II g-lower pC=", Factor[pCII]];
Print[
  "II g-lower denominator (positive on 0<s<2/3)=",
  translatedGPlusDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedGPlusDenominator/
   ((s - 3)^6 (s - 1)^2 s^8 (1 + s)^2)
]]];
Do[
  recordCoefficientFamily[
    "II-g-lower", translatedGPlusPolynomial, x, interval
  ],
  {interval, {{0, 1/3}, {1/3, 2/3}}}
];

(* The hard-wall lower endpoint is automatic. *)
hardEndpointIdentity = Together[
  cII + MminusII (1 - hII) - (9/10 + 7 d/(8 s))
];
AppendTo[allChecks, hardEndpointIdentity === 0];
Print["II h-lower identity OK=", hardEndpointIdentity === 0];

(* ---------- Branch II decreasing-slope endpoint at a=uP ---------- *)

uP = Together[1 - 2 ellMinus (p + 4)/5];
eU = Together[cII + MminusII (1 - uP)];
pE = Together[p /. First[Solve[eU == 0, p]]];
pX = Together[p /. First[Solve[gII == hII, p]]];
pM = Together[5/(4 ellMinus) - 3];

dHII = Together[Splus - 2 hII];
polyHU = Together[p^4 Aminus^2 uP^2 - eU^2 dHII];
polyGU = Together[p^4 Aminus^2 uP^2 - eU^2 dGII];

(* h owner and eU<0 require pE<p<=pX. *)
pHU = Together[pE + v (pX - pE)];
translatedHURat = Together[polyHU /. p -> pHU];
translatedHUDenominator = Factor[Denominator[translatedHURat]];
translatedHUPolynomial = Expand[Numerator[translatedHURat]];
Print["II h-uP pE=", Factor[pE]];
Print["II h-uP pX=", Factor[pX]];
Print[
  "II h-uP denominator (positive on 0<s<27/50)=",
  translatedHUDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedHUDenominator/
   ((s - 1)^2 s^8 (1 + s)^2
    (235 s - 29517)^6 (29047 s - 58329)^6)
]]];
Do[
  recordTensor["II-h-uP", translatedHUPolynomial, sInterval, vInterval],
  {sInterval, {{0, 1/3}, {1/3, 1/2}, {1/2, 27/50}}},
  {vInterval, {{0, 1/2}, {1/2, 1}}}
];

(* Above 27/50 the h chart is empty: pX-pE has the same sign as F,
   and -F has positive Bernstein coefficients on [27/50,2/3]. *)
pXMinusPERat = Together[pX - pE];
pXMinusPEDenominator = Factor[Denominator[pXMinusPERat]];
pXMinusPENumerator = Factor[Numerator[pXMinusPERat]];
Fcap = 26250943950 - 26459941200 s - 55931767815 s^2 +
  6811434596 s^3 + 42264512677 s^4 - 8369021640 s^5;
capFactorIdentity = Factor[pXMinusPENumerator/Fcap];
Print["II h-uP pX-pE denominator=", pXMinusPEDenominator];
Print["II h-uP numerator/Fcap=", capFactorIdentity];
AppendTo[allChecks, capFactorIdentity === 1];
AppendTo[allChecks, Together[
  pXMinusPEDenominator/
   (10 s^3 (235 s - 29517) (29047 s - 58329))
] === 1];
record1D["II-h-uP-empty-cap", -Fcap, {27/50, 2/3}];

(* g owner, eU<0 and phase give max(pX,pE)<p<pM.  It is enough to
   start at pX for s<1/2 and at pE for s>=1/2. *)
pGUX = Together[pX + v (pM - pX)];
translatedGUXRat = Together[polyGU /. p -> pGUX];
translatedGUXDenominator = Factor[Denominator[translatedGUXRat]];
translatedGUXPolynomial = Expand[Numerator[translatedGUXRat]];
Print[
  "II g-uP pX-chart denominator (positive on 0<s<1/2)=",
  translatedGUXDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedGUXDenominator/
   ((s - 1)^2 s^8 (1 + s)^2 (29047 s - 58329)^6)
]]];
Do[
  recordTensor[
    "II-g-uP-pX", translatedGUXPolynomial, sInterval, vInterval
  ],
  {sInterval, {{0, 1/3}, {1/3, 1/2}}},
  {vInterval, {{0, 1/2}, {1/2, 1}}}
];

pGUE = Together[pE + v (pM - pE)];
translatedGUERat = Together[polyGU /. p -> pGUE];
translatedGUEDenominator = Factor[Denominator[translatedGUERat]];
translatedGUEPolynomial = Expand[Numerator[translatedGUERat]];
Print[
  "II g-uP pE-chart denominator (positive on 1/2<s<2/3)=",
  translatedGUEDenominator
];
AppendTo[allChecks, positiveConstantQ[Together[
  translatedGUEDenominator/
   ((s - 1)^2 s^8 (1 + s)^2 (235 s - 29517)^6)
]]];
Do[
  recordTensor[
    "II-g-uP-pE", translatedGUEPolynomial, sInterval, vInterval
  ],
  {sInterval, {{1/2, 3/5}, {3/5, 2/3}}},
  {vInterval, {{0, 1/2}, {1/2, 1}}}
];

(* Linear identities which make the three p-walls transparent. *)
AppendTo[allChecks, Together[eU /. p -> pE] === 0];
AppendTo[allChecks, Together[(gII - hII) /. p -> pX] === 0];
AppendTo[allChecks, Together[(pM + 3) ellMinus - 5/4] === 0];
Print[
  "II wall identities OK=",
  And[
    Together[eU /. p -> pE] === 0,
    Together[(gII - hII) /. p -> pX] === 0,
    Together[(pM + 3) ellMinus - 5/4] === 0
  ]
];

round41BernsteinSignReplayOK = And @@ allChecks;
Print[
  "round41BernsteinSignReplayOK=",
  round41BernsteinSignReplayOK
];
