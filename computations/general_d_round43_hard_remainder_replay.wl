(* Round 43 algebra and diagnostic replay.
   This is not an interval certificate and proves no continuum sign. *)

ClearAll["Global`*"];

(* Generic rationalization used in (R43.8). *)
rationalizationResidual = Together[
   (ur - ux)/(ux - uq) -
    ((ur^2 - ux^2)/(ux^2 - uq^2)) ((ux + uq)/(ur + ux))
   ];

(* The two exact quotient identities used in Lemma 2.1. *)
q = (1 + b)/(1 + a);
qBranchOneResidual = Together[
   q - 1/a - (a b - 1)/(a (1 + a))
   ];
qBranchTwoResidual = Together[
   q^2 - b/a - (a - b) (1 - a b)/(a (1 + a)^2)
   ];

(* The strict cap comparison (R43.11). *)
capF[th_] := Sin[th] - th Cos[th] - Sin[th]^3/3;
capDerivativeResidual = TrigExpand[
   D[capF[th], th] - Sin[th] (th - Sin[th] Cos[th])
   ] // FullSimplify;
innerDerivativeResidual = FullSimplify[
   D[th - Sin[th] Cos[th], th] - 2 Sin[th]^2
   ];

(* Exact t derivative in (R43.24). *)
g[aa_, zz_] := (Sqrt[aa^2 - zz^2] - zz ArcCos[zz/aa])/Pi;
kk = mu Sec[t];
action[zz_] := g[kk, zz] - g[mu, zz];
radiusDerivativeResidual = FullSimplify[
   D[g[aa, zz], aa] - Sqrt[aa^2 - zz^2]/(Pi aa),
   Assumptions -> aa > zz > 0
   ];
kDerivativeResidual = FullSimplify[
   D[mu Sec[t], t] - mu Sec[t] Tan[t]
   ];
(* The chain rule combines these two zero residuals to give
   d A_t(z)/dt = tan(t) sqrt(K^2-z^2)/pi. *)
actionDerivativeResidual = {radiusDerivativeResidual, kDerivativeResidual};

ef = action[rr] + action[xx] + 1/2 - 2 ff;
estar = 1/2 - (1 - 2 t/Pi) mm/(2 pp);
hardDerivativeResidual = FullSimplify[
   D[ef - estar, t] -
    (Tan[t] (Sqrt[kk^2 - rr^2] + Sqrt[kk^2 - xx^2]) - mm/pp)/Pi,
   Assumptions -> 0 < t < Pi/2 && mu > xx > rr > 0 && pp > 0
   ];

(* Exact limiting coefficient in (R43.18). *)
limitCoefficient = 11 Sqrt[14]/(252 Pi (2 - Sqrt[2])) - 1/8;
limitCoefficientNegative = FullSimplify[limitCoefficient < 0];

(* High-precision finite diagnostic (R43.20)--(R43.21). *)
wp = 80;
r0 = SetPrecision[1, wp];
p0 = SetPrecision[9, wp];
m0 = SetPrecision[9, wp];
q0 = r0 + p0 + m0;
mu0 = q0 + 1;
b00 = SetPrecision[2, wp];
bOuter = b00 + 1;
theta0 = th /. FindRoot[
    q0/Pi (Tan[th] - th) == b00 + 3/4,
    {th, SetPrecision[0.95, wp]}, WorkingPrecision -> wp,
    AccuracyGoal -> 65, PrecisionGoal -> 65
    ];
t0 = ArcCos[mu0 Cos[theta0]/q0];
k0 = mu0 Sec[t0];
d0 = 1 - 2 t0/Pi;
zeta0 = Pi/(2 t0) - 1;
ball[aa_, zz_] := (Sqrt[aa^2 - zz^2] - zz ArcCos[zz/aa])/Pi;
shell[zz_] := ball[k0, zz] - ball[mu0, zz];
h0 = ball[mu0, q0];
u0 = ball[k0, q0] - ball[k0, mu0];
beta0 = ArcCos[q0/k0]/Pi;
x0 = r0 + p0;
ur0 = Sqrt[mu0^2 - r0^2];
ux0 = Sqrt[mu0^2 - x0^2];
uq0 = Sqrt[mu0^2 - q0^2];
ap0 = p0^2/(3 (2 r0 + p0));
r10 = (ur0 - ux0)/(ux0 - uq0);
hCapital0 = (p0 + ap0) r10;
t420 = 9/10 + b00 Min[zeta0, hCapital0] + hCapital0 h0 -
   (p0 - d0 m0)/2;
f0 = 4;
j0 = f0 - bOuter;
e00 = shell[r0] + 1/4 - f0;
ep0 = shell[x0] + 1/4 - f0;
e0 = e00 + ep0;
estar0 = (p0 - d0 m0)/(2 p0);
w0 = ball[k0, mu0];
lambda0 = f0 - 1/4 - w0;
stretch0 = Sqrt[(mu0^2 - r0^2)/(mu0^2 - x0^2)];
tau0 = (stretch0 - 1)/(stretch0 + 1);
elastic0 = tau0 (e0 + 2 lambda0);
quartic0 = (mu0^-1 - k0^-1) (x0^2 - r0^2)/(2 Pi) +
   (mu0^-3 - k0^-3) (x0^4 - r0^4)/(24 Pi);
m40 = Max[elastic0, quartic0];
xiHat0 = (e00 - ep0) - m40;
activity0 = k0^2 - Pi^2/(1 - Cos[t0])^2 - 3/4;
outerResidual0 = ball[k0, q0] - (bOuter - 1/4);

finiteDiagnostic = N[<|
    "theta" -> theta0,
    "t" -> t0,
    "d" -> d0,
    "zeta" -> zeta0,
    "H" -> hCapital0,
    "h" -> h0,
    "u" -> u0,
    "beta" -> beta0,
    "Ar" -> shell[r0],
    "Ax" -> shell[x0],
    "Ax1" -> shell[x0 + 1],
    "Aq" -> shell[q0],
    "floors" -> {Floor[shell[r0] + 1/4],
      Floor[shell[x0] + 1/4], Floor[shell[x0 + 1] + 1/4]},
    "j" -> j0,
    "E" -> e0,
    "EStar" -> estar0,
    "EminusEStar" -> e0 - estar0,
    "T42" -> t420,
    "activityMargin" -> activity0,
    "XiHat" -> xiHat0,
    "outerResidual" -> outerResidual0
    |>, 30];

finiteDiagnosticChecks = And[
   Abs[outerResidual0] < 10^-60,
   0 < h0 < u0 < beta0 < 1/2,
   p0 > d0 m0,
   Floor[shell[r0] + 1/4] == f0,
   Floor[shell[x0] + 1/4] == f0,
   Floor[shell[x0 + 1] + 1/4] == f0 - 1,
   activity0 > 0,
   xiHat0 > 0,
   e0 - estar0 > 0,
   t420 < 0
   ];

round43HardRemainderReplayOK = And[
   rationalizationResidual === 0,
   qBranchOneResidual === 0,
   qBranchTwoResidual === 0,
   capDerivativeResidual === 0,
   innerDerivativeResidual === 0,
   actionDerivativeResidual === {0, 0},
   hardDerivativeResidual === 0,
   TrueQ[limitCoefficientNegative],
   TrueQ[finiteDiagnosticChecks]
   ];

Print["rationalizationResidual=", rationalizationResidual];
Print["qBranchOneResidual=", qBranchOneResidual];
Print["qBranchTwoResidual=", qBranchTwoResidual];
Print["capDerivativeResidual=", capDerivativeResidual];
Print["innerDerivativeResidual=", innerDerivativeResidual];
Print["actionDerivativeResidual=", actionDerivativeResidual];
Print["hardDerivativeResidual=", hardDerivativeResidual];
Print["limitCoefficient=", N[limitCoefficient, 30]];
Print["limitCoefficientNegative=", limitCoefficientNegative];
Print["finiteDiagnostic=", finiteDiagnostic];
Print["finiteDiagnosticChecks=", finiteDiagnosticChecks];
Print["round43HardRemainderReplayOK=", round43HardRemainderReplayOK];
