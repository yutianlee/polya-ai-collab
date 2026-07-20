(* Round 46 symbolic replay for the complete-owner R45.18 attempt.

   Exact identities below support the normalization, wall calculus, and the
   one correlated action/phase reduction in the lead report.  Numerical
   fixtures are regression checks only; they do not certify the infinite
   owner or prove the remaining scalar inequality. *)

ClearAll["Global`*"];
$MaxExtraPrecision = 20000;

(* Retain the audited Round-45 coefficient and owner replay as a dependency. *)
r46ReplayDirectory = DirectoryName[$InputFileName];
Get[FileNameJoin[{r46ReplayDirectory,
   "general_d_round45_support_sign_replay.wl"}]];
r46InheritedRound45OK = TrueQ[round45SupportSignReplayOK];

(* Basic action and its exact radius antiderivative. *)
r46G[aa_, zz_] :=
  (Sqrt[aa^2 - zz^2] - zz ArcCos[zz/aa])/Pi;
r46I[aa_, zz_] := 1/(4 Pi) (
   3 zz Sqrt[aa^2 - zz^2] + aa^2 ArcSin[zz/aa] -
    2 zz^2 ArcCos[zz/aa]);

r46GzResidual = FullSimplify[
  D[r46G[aa, zz], zz] + ArcCos[zz/aa]/Pi,
  Assumptions -> aa > zz > 0];
r46GaResidual = FullSimplify[
  D[r46G[aa, zz], aa] - Sqrt[aa^2 - zz^2]/(Pi aa),
  Assumptions -> aa > zz > 0];
r46AntiderivativeResidual = FullSimplify[
  D[r46I[aa, zz], zz] - r46G[aa, zz],
  Assumptions -> aa > zz > 0];

(* Outer-angle normalization q(tan(phi)-phi)=pi v and wall derivatives. *)
r46PhiPrime = -(Tan[ph] - ph)/(qq Tan[ph]^2);
r46WallDerivativeResidual = FullSimplify[
  (Tan[ph] - ph) + qq Tan[ph]^2 r46PhiPrime,
  Assumptions -> qq > 0 && 0 < ph < Pi/2];
r46KPrimeResidual = FullSimplify[
  Sec[ph] + qq Sec[ph] Tan[ph] r46PhiPrime - ph/Sin[ph],
  Assumptions -> qq > 0 && 0 < ph < Pi/2];

(* cos(t)=(q+1)cos(phi)/q.  The second expression is the wall form
   after q(tan(phi)-phi)=pi v is imposed. *)
r46TPrimeRaw =
  (ph - qq (Tan[ph] - ph))/
   (qq (qq + 1) Tan[ph] Tan[tt]);
r46TPrimeWall =
  (ph - Pi vv)/(qq (qq + 1) Tan[ph] Tan[tt]);
r46TImplicitDerivativeResidual = FullSimplify[
  -Sin[tt] r46TPrimeRaw -
   (-Cos[ph]/qq^2 - (qq + 1) Sin[ph] r46PhiPrime/qq),
  Assumptions -> qq > 0 && 0 < tt < ph < Pi/2 &&
    Cos[tt] == (qq + 1) Cos[ph]/qq];

(* Closed cap J. *)
r46InnerAngle = ArcCos[qq/(qq + 1)];
r46JClosed = (((qq + 1)^2 + 2 qq^2) r46InnerAngle -
    3 qq Sqrt[2 qq + 1])/(2 Pi);
r46JEndpointForm = FullSimplify[
  2 ((qq + 1)^2/8 - r46I[qq + 1, qq]),
  Assumptions -> qq > 0];
r46JResidual = FullSimplify[
  r46JEndpointForm - r46JClosed,
  Assumptions -> qq > 0];

(* Fixed-q relation t(phi)=acos(cos(phi)/cos(a)). *)
r46TByPhiPrime = Sin[ph]/(Cos[al] Sin[tt]);
r46TByPhiSecond = FullSimplify[
  D[r46TByPhiPrime, ph] +
   D[r46TByPhiPrime, tt] r46TByPhiPrime,
  Assumptions -> 0 < al < ph < Pi/2 && 0 < tt < Pi/2 &&
    Cos[tt] == Cos[ph]/Cos[al]];
r46TByPhiSecondExpected =
  -Cos[ph] Sin[al]^2/(Cos[al]^3 Sin[tt]^3);
r46TByPhiSecondResidual = FullSimplify[
  r46TByPhiSecond - r46TByPhiSecondExpected,
  Assumptions -> 0 < al < ph < Pi/2 && 0 < tt < Pi/2 &&
    Cos[tt] == Cos[ph]/Cos[al]];
r46SineProductResidual = FullSimplify[
  Sin[al - ph] Sin[al + ph] - (Sin[al]^2 - Sin[ph]^2)];
r46TByPhiSecondResidualReduced = FullSimplify[
  r46TByPhiSecondResidual /.
    Sin[al - ph] Sin[al + ph] -> Sin[al]^2 - Sin[ph]^2 /.
    Sin[ph]^2 -> 1 - Cos[al]^2 Cos[tt]^2,
  Assumptions -> 0 < al < ph < Pi/2 && 0 < tt < Pi/2];

(* The normalized inverse-action quotient.  With z=mu cos(y) and
   lambda=mu/K, pi Q is the integral of this kernel. *)
r46QKernel = Sin[yy]/Sqrt[1 - ss^2 Cos[yy]^2];
r46QKernelDerivativeExpected =
  Cos[yy] (1 - ss^2)/(1 - ss^2 Cos[yy]^2)^(3/2);
r46QKernelDerivativeResidual = FullSimplify[
  D[r46QKernel, yy] - r46QKernelDerivativeExpected,
  Assumptions -> 0 < yy < Pi/2 && 0 < ss < 1];
r46AngleIntegralDerivativeResidual = FullSimplify[
  D[ArcCos[la Cos[yy]] - yy, la] +
   Cos[yy]/Sqrt[1 - la^2 Cos[yy]^2],
  Assumptions -> 0 < la < 1 && 0 < yy < Pi/2];
r46AngleIntegralEndpointResidual = FullSimplify[
  (ArcCos[la Cos[yy]] - yy) /. la -> 1,
  Assumptions -> 0 < yy < Pi/2];
r46QKernelPositive = FullSimplify[
  r46QKernelDerivativeExpected > 0,
  Assumptions -> 0 < yy < Pi/2 && 0 < ss < 1];

(* The phase/root payment after the wall substitution. *)
r46PhaseLower =
  (vv - 3/4) (Pi/(2 ph) - 1) + 9 Pi/(16 ph) - 1/10;
r46PhaseWallTerm = vv (Pi - 2 ph)/(2 ph);
r46PhaseResidual = FullSimplify[
  r46PhaseLower - r46PhaseWallTerm - 41/40];
r46PhaseResidualExpected = 3 (Pi - 2 ph)/(16 ph);
r46PhaseResidualCheck = FullSimplify[
  r46PhaseResidual - r46PhaseResidualExpected];
r46PhaseResidualPositive = FullSimplify[
  r46PhaseResidualExpected > 0,
  Assumptions -> 0 < ph < Pi/2];

(* Mandatory exact coefficient regressions. *)
r46OldCoefficientResidual = FullSimplify[
  Integrate[zz^2, {zz, -3/4, 1/4}] - 7/48];
r46TopCoefficientResidual = FullSimplify[
  2 Integrate[(3/4 - ell)^2/2, {ell, 0, 3/4}] - 9/64];
r46ReconciliationResidual = FullSimplify[
  (9/(16 be) - 1/(2 be)) - 1/(16 be)];

(* Exact normalized fixture calculation.  The returned R45.18 margin is the
   literal right-minus-left expression.  Fstrong is only a proved lower
   reduction; its sampled sign is not a theorem. *)
r46Fixture[rIn_, pIn_, mIn_, bIn_] := Module[
  {rr, pp, mm, bb, b0, qq0, mu0, xx, phi0, a0, t0, k0, beta0,
   d0, zeta0, ww, ur, ux, uq, rone, action, drop, j0, old, top,
   curv, margin, fstrong, qquot},
  rr = SetPrecision[rIn, 100]; pp = SetPrecision[pIn, 100];
  mm = SetPrecision[mIn, 100]; bb = bIn; b0 = bb - 1;
  qq0 = rr + pp + mm; mu0 = qq0 + 1; xx = rr + pp;
  phi0 = phi /. FindRoot[
     qq0 (Tan[phi] - phi) == Pi (b0 + 3/4),
     {phi, SetPrecision[1.0, 100]}, WorkingPrecision -> 100,
     AccuracyGoal -> 80, PrecisionGoal -> 80];
  a0 = ArcCos[qq0/mu0];
  t0 = ArcCos[Cos[phi0]/Cos[a0]];
  k0 = qq0 Sec[phi0]; beta0 = phi0/Pi;
  d0 = 1 - 2 t0/Pi; zeta0 = Pi/(2 t0) - 1;
  ww = mu0/Pi (Tan[t0] - t0);
  ur = Sqrt[mu0^2 - rr^2]; ux = Sqrt[mu0^2 - xx^2];
  uq = Sqrt[mu0^2 - qq0^2]; rone = (ur - ux)/(ux - uq);
  action[z_?NumericQ] := r46G[k0, z] - r46G[mu0, z];
  drop = action[xx] - action[qq0];
  j0 = r46JClosed /. qq -> qq0;
  old = Pi^2 b0/(k0 t0^3 Sin[t0]) (ww/2 - b0/4 + 1/48);
  top = 9/(64 Pi Sqrt[k0^2 - qq0^2] beta0^3);
  curv = pp^3/(6 Pi) (1/ur - 1/Sqrt[k0^2 - rr^2]);
  margin = pp rone drop + old + b0 zeta0 + 9/(16 beta0) -
    j0 + top + curv - (pp - d0 mm)/2;
  qquot = (phi0 - a0) Tan[a0]/Pi;
  fstrong = pp (ur - ux) qquot +
    qq0 (Tan[phi0] - phi0) (Pi - 2 phi0)/(2 Pi phi0) +
    d0 mm/2 - pp/2 + 41/40;
  N[<|"tuple" -> {rr, pp, mm, bb}, "q" -> qq0,
    "phi" -> phi0, "a" -> a0, "t" -> t0,
    "wallResidual" -> qq0 (Tan[phi0] - phi0) - Pi (b0 + 3/4),
    "R45.18Margin" -> margin, "Fstrong" -> fstrong,
    "marginMinusFstrong" -> margin - fstrong|>, 42]
];

r46MinimumFixture = r46Fixture[1, 3, 1, 2];
r46HalfGridFixture = r46Fixture[3/2, 3, 1, 2];
r46CFFixture = r46Fixture[1, 6, 11, 19];
r46FixtureChecks = And[
  Abs[r46MinimumFixture["wallResidual"]] < 10^-75,
  Abs[r46MinimumFixture["R45.18Margin"] -
    1.70914550684517353565515496215] < 10^-28,
  r46MinimumFixture["R45.18Margin"] >
    r46MinimumFixture["Fstrong"] > 0,
  r46HalfGridFixture["R45.18Margin"] >
    r46HalfGridFixture["Fstrong"] > 0,
  r46CFFixture["R45.18Margin"] > r46CFFixture["Fstrong"] > 0
];

round46R4518ReplayOK = And[
  r46InheritedRound45OK,
  r46GzResidual === 0,
  r46GaResidual === 0,
  r46AntiderivativeResidual === 0,
  r46WallDerivativeResidual === 0,
  r46KPrimeResidual === 0,
  r46TImplicitDerivativeResidual === 0,
  r46JResidual === 0,
  r46SineProductResidual === 0,
  r46TByPhiSecondResidualReduced === 0,
  r46QKernelDerivativeResidual === 0,
  r46AngleIntegralDerivativeResidual === 0,
  r46AngleIntegralEndpointResidual === 0,
  TrueQ[r46QKernelPositive],
  r46PhaseResidualCheck === 0,
  TrueQ[r46PhaseResidualPositive],
  r46OldCoefficientResidual === 0,
  r46TopCoefficientResidual === 0,
  r46ReconciliationResidual === 0,
  TrueQ[r46FixtureChecks]
];

Print["r46GzResidual=", r46GzResidual];
Print["r46GaResidual=", r46GaResidual];
Print["r46AntiderivativeResidual=", r46AntiderivativeResidual];
Print["r46PhiPrime=", r46PhiPrime];
Print["r46WallDerivativeResidual=", r46WallDerivativeResidual];
Print["r46KPrimeResidual=", r46KPrimeResidual];
Print["r46TPrimeRaw=", r46TPrimeRaw];
Print["r46TPrimeWall=", r46TPrimeWall];
Print["r46TImplicitDerivativeResidual=", r46TImplicitDerivativeResidual];
Print["r46JClosed=", r46JClosed];
Print["r46JResidual=", r46JResidual];
Print["r46TByPhiSecondResidual=", r46TByPhiSecondResidual];
Print["r46TByPhiSecondResidualReduced=",
  r46TByPhiSecondResidualReduced];
Print["r46QKernelDerivativeResidual=", r46QKernelDerivativeResidual];
Print["r46QKernelPositive=", r46QKernelPositive];
Print["r46PhaseResidual=", r46PhaseResidual];
Print["r46OldCoefficientResidual=", r46OldCoefficientResidual];
Print["r46TopCoefficientResidual=", r46TopCoefficientResidual];
Print["r46ReconciliationResidual=", r46ReconciliationResidual];
Print["r46MinimumFixture=", r46MinimumFixture];
Print["r46HalfGridFixture=", r46HalfGridFixture];
Print["r46CFFixture=", r46CFFixture];
Print["r46FixtureChecks=", r46FixtureChecks];
Print["round46R4518ReplayOK=", round46R4518ReplayOK];
