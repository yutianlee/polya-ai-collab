(*
  Round 13 focused falsification of the Round 12 endpoint target (3.11).

  The construction uses an exact rational angle and rational grid/interface
  data.  The first block is an exact-rational coarse certificate based on
  alternating Taylor bounds and rational bounds for Pi.  The second block
  is a 100-digit replay of all shell quantities, including the exact defect
  and the no-drop identity (S4).
*)

ClearAll["Global`*"];

$MaxExtraPrecision = 5000;
wp = 100;
wallTol = 10^-60;

theta = 8899/100000;
q = 9998;
n = 50;
r = q - n;
alpha = 999/1000;
mu = q + alpha;
kappa = 3/4;

phi[t_] := Sin[t] - t Cos[t];
K = 3 Pi/(4 phi[theta]);
z = K Cos[theta];
y = z - q;

(* Exact-rational enclosure data. *)
piLo = 103993/33102;
piHi = 104348/33215;

phiLo = theta^3/3 - theta^5/30 + theta^7/840 - theta^9/45360;
phiHi = phiLo + theta^11/3991680;
cosLo = 1 - theta^2/2 + theta^4/24 - theta^6/720;
cosHi = cosLo + theta^8/40320;

kLo = 3 piLo/(4 phiHi);
kHi = 3 piHi/(4 phiLo);
zLo = 3 piLo cosLo/(4 phiHi);
zHi = 3 piHi cosHi/(4 phiLo);

atanLo[x_] := x - x^3/3;
atanHi[x_] := x - x^3/3 + x^5/5;

uQKLo = 8968/100000;
uQKHi = 8969/100000;
uRKLo = 13491/100000;
uRKHi = 13492/100000;
uQMuLo = 1413/100000;
uQMuHi = 1414/100000;
uRMuLo = 10138/100000;
uRMuHi = 10139/100000;

uBracketQK = And[
  kLo^2 - q^2 > uQKLo^2 q^2,
  kHi^2 - q^2 < uQKHi^2 q^2
];
uBracketRK = And[
  kLo^2 - r^2 > uRKLo^2 r^2,
  kHi^2 - r^2 < uRKHi^2 r^2
];
uBracketQMu = And[
  mu^2 - q^2 > uQMuLo^2 q^2,
  mu^2 - q^2 < uQMuHi^2 q^2
];
uBracketRMu = And[
  mu^2 - r^2 > uRMuLo^2 r^2,
  mu^2 - r^2 < uRMuHi^2 r^2
];

sigmaQHi = (atanHi[uQKHi] - atanLo[uQMuLo])/piLo;
sigmaRHi = (atanHi[uRKHi] - atanLo[uRMuLo])/piLo;

wLo = (zLo - q) theta/piHi;
betaHi = atanHi[uQKHi]/piLo;
wHi = (zHi - q) betaHi;
hOneHi = 2/(3 piLo 70); (* Sqrt[2/q] < 1/70. *)

cRN = (n + n^2/(3 (2 r + n))) (2 n/(r + 2 n));
lHi = piHi/(2 theta) + 2 (408/1000) - 1;
lambdaHi = (kHi - mu)/piLo;
psiCoarseHi = 35/2 - n/2 + (1/2) (51/4 - 3/4);

certificateGates = <|
  "PiBracket" -> TrueQ[piLo < Pi < piHi],
  "KBracket" -> TrueQ[10038 < kLo < kHi < 10039],
  "ZAndEtaCell" -> TrueQ[9998 + 407/1000 < zLo < zHi < 9998 + 408/1000],
  "UBrackets" -> And[uBracketQK, uBracketRK, uBracketQMu, uBracketRMu],
  "SlopeBounds" -> TrueQ[sigmaQHi < 25/1000 && sigmaRHi < 12/1000],
  "EndpointGapBounds" -> TrueQ[
    wLo > 11/1000 && wHi < 12/1000 && hOneHi < 31/10000
  ],
  "NoDropTrapezoid" -> TrueQ[
    762/1000 + n/2 (25/1000 + 12/1000) < 7/4
  ],
  "CoefficientBound" -> TrueQ[cRN < 1/2],
  "TerminalUpperBound" -> TrueQ[lHi < 35/2],
  "LambdaUpperBound" -> TrueQ[lambdaHi < 51/4],
  "NegativeScalarBound" -> TrueQ[psiCoarseHi == -3/2]
|>;

Print["round13CertificateGates=", certificateGates // InputForm];
Print["round13CertificatePass=", And @@ Values[certificateGates]];
Print[
  "round13RationalBounds=",
  N[<|
    "kLo" -> kLo, "kHi" -> kHi,
    "zLo" -> zLo, "zHi" -> zHi,
    "wLo" -> wLo, "wHi" -> wHi, "hOneHi" -> hOneHi,
    "sigmaRHi" -> sigmaRHi, "sigmaQHi" -> sigmaQHi,
    "C" -> cRN, "LHi" -> lHi, "lambdaHi" -> lambdaHi,
    "psiCoarseHi" -> psiCoarseHi
  |>, 30] // InputForm
];

(* High-precision shell replay. *)
strictFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, Max[0, m - 1], Max[0, Ceiling[x] - 1]]
];

ordinaryFloor[x_?NumericQ] := Module[{m = Round[x]},
  If[Abs[x - m] <= wallTol, m, Floor[x]]
];

ballAction[a_?NumericQ, x_?NumericQ] := If[
  x < a,
  (Sqrt[a^2 - x^2] - x ArcCos[x/a])/Pi,
  0
];

ballTailIntegral[a_?NumericQ, x_?NumericQ] := If[
  x < a,
  Module[{tt = ArcCos[x/a]},
    a^2/(4 Pi) (tt (1 + 2 Cos[tt]^2) - 3 Sin[tt] Cos[tt])
  ],
  0
];

shellAction[x_?NumericQ] := ballAction[N[K, wp], x] - ballAction[N[mu, wp], x];
shellTail[x_?NumericQ] :=
  ballTailIntegral[N[K, wp], x] - ballTailIntegral[N[mu, wp], x];

tailDefect[x_?NumericQ] := Module[{jmax, endpoint, doubled},
  jmax = Ceiling[N[K, wp] - x] + 1;
  endpoint = strictFloor[shellAction[x] + 1/4];
  doubled = Sum[
    strictFloor[shellAction[x + j] + 1/4],
    {j, 1, jmax}
  ];
  2 shellTail[x] - endpoint - 2 doubled
];

kN = N[K, wp];
zN = N[z, wp];
yN = N[y, wp];
muN = N[mu, wp];
qN = N[q, wp];
rN = N[r, wp];
alphaN = N[alpha, wp];

v = ballAction[kN, qN];
h = ballAction[muN, qN];
hOne = ballAction[N[q + 1, wp], qN];
aq = v - h;
eps = aq - 3/4;
B = strictFloor[v + 1/4];
Q = strictFloor[aq + 1/4];
chi = If[Abs[eps] <= wallTol, 1, 0];
beta = ArcCos[qN/kN]/Pi;
lambda = (kN - muN)/Pi;
alphaAct = kN - qN - Pi kN/Sqrt[kN^2 - kappa];

sampleActions = Table[shellAction[rN + j], {j, 0, n}];
sampleFloors = ordinaryFloor[# + 1/4] & /@ sampleActions;

sigmaAt[x_?NumericQ] := (ArcCos[x/kN] - ArcCos[x/muN])/Pi;
sigmaR = sigmaAt[rN];
sigmaQ = sigmaAt[qN];

delta = ballTailIntegral[muN, qN];
topSquare = Max[v - 1, 0]^2/beta;
lHat = Pi/(2 N[theta, wp]) + 2 yN - Q - alphaN h + topSquare;
lExactCap = Pi/(2 N[theta, wp]) + 2 yN - Q - 2 delta + topSquare;
round11R0 = -n/2 + N[cRN, wp] (lambda - 3/4);
round11Psi = Max[0, lHat] + round11R0 + chi;

exactRn = 2 (shellTail[rN] - shellTail[qN]) - 2 n;
headIntegral = exactRn + n/2 - 2 n eps;
exactDq = tailDefect[qN];
exactDr = tailDefect[rN];
s4Residual = exactDr - (exactDq + exactRn + chi);

lambdaEndpoint = (kN - qN - 1)/Pi;
lEndpoint = Pi/(2 N[theta, wp]) + 2 yN - 1 - hOne + topSquare;
endpointCoeffTerm = N[cRN, wp] * (lambdaEndpoint - 3/4);
psiEndpoint = Max[0, lEndpoint] - n/2 + endpointCoeffTerm;

replay = <|
  "theta" -> N[theta, wp], "K" -> kN, "z" -> zN,
  "q" -> qN, "yEta" -> yN, "r" -> rN, "n" -> n,
  "alpha" -> alphaN, "mu" -> muN, "rho" -> muN/kN,
  "alphaAct" -> alphaAct,
  "v" -> v, "h" -> h, "Aq" -> aq, "epsilon" -> eps,
  "B" -> B, "Q" -> Q, "chi" -> chi, "beta" -> beta,
  "C" -> N[cRN, wp], "lambda" -> lambda,
  "sigmaR" -> sigmaR, "sigmaQ" -> sigmaQ,
  "minSampleAction" -> Min[sampleActions],
  "maxSampleAction" -> Max[sampleActions],
  "sampleFloorSet" -> DeleteDuplicates[sampleFloors],
  "delta" -> delta, "twoDelta" -> 2 delta,
  "alphaH" -> alphaN h, "capSlack" -> alphaN h - 2 delta,
  "Lhat" -> lHat, "LExactCap" -> lExactCap,
  "round11R0" -> round11R0, "round11Psi" -> round11Psi,
  "headIntegral" -> headIntegral, "exactRn" -> exactRn,
  "LhatPlusExactRn" -> lHat + exactRn,
  "LExactCapPlusExactRn" -> lExactCap + exactRn,
  "exactDq" -> exactDq, "exactDr" -> exactDr,
  "s4Residual" -> s4Residual,
  "hOne" -> hOne, "endpointEpsilon" -> v - hOne - 3/4,
  "endpointLambda" -> lambdaEndpoint,
  "endpointL" -> lEndpoint, "endpointCoeffTerm" -> endpointCoeffTerm,
  "endpointPsi" -> psiEndpoint
|>;

replayGates = <|
  "ExtensionGrid" -> TrueQ[IntegerQ[r] && r >= 1],
  "CorrectN" -> TrueQ[Floor[mu - r] == n],
  "ActiveD4" -> TrueQ[
    kN^2 > Pi^2/(1 - muN/kN)^2 + kappa
  ],
  "OpenHardB1" -> TrueQ[
    B == 1 && Q == 1 && chi == 0 && 0 < eps < 1/4
  ],
  "NoDrop" -> TrueQ[Length[sampleFloors] == n + 1 && And @@ (# == 1 & /@ sampleFloors)],
  "BranchEndpointFirst" -> TrueQ[hOne < v - 3/4 && alphaAct > 1],
  "EndpointReconstruction" -> TrueQ[
    Abs[psiEndpoint - (lEndpoint - n/2 + endpointCoeffTerm)] < 10^-80
      && -1.71 < psiEndpoint < -1.70
  ],
  "NegativeEndpoint" -> TrueQ[psiEndpoint < -1],
  "NegativeActualScalar" -> TrueQ[round11Psi < -1],
  "PositiveExactDefect" -> TrueQ[exactDr > 0],
  "S4Replay" -> TrueQ[Abs[s4Residual] < 10^-80]
|>;

Print["round13Replay=", Map[N[#, 50] &, replay] // InputForm];
Print["round13ReplayGates=", replayGates // InputForm];
Print["round13ReplayPass=", And @@ Values[replayGates]];

If[!TrueQ[And @@ Values[certificateGates]] || !TrueQ[And @@ Values[replayGates]],
  Exit[2]
];
