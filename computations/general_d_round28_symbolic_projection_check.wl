(* Round 28 exact algebra replay.  This is a diagnostic, not a proof premise. *)

ClearAll[a, delta, eP, Esum, EStar, p, g, lambda, u, r, x, mu, K];

endpointResidual = FullSimplify[
  a delta + p (Esum - EStar) - ((p + a) delta + 2 p eP - p EStar),
  Assumptions -> Esum == delta + 2 eP
];

tau = g/(g + 2);
elasticityResidual = FullSimplify[
  (1 + g/2) (delta - tau (Esum + 2 lambda)) -
    (delta - g (lambda + (Esum - delta)/2)),
  Assumptions -> g > 0
];

projectionOrderingResidual = FullSimplify[
  tau (Esum + 2 lambda) - g (lambda + eP) -
    tau (delta - g (lambda + eP)),
  Assumptions -> {g > 0, Esum == delta + 2 eP}
];

curvatureSeries = Series[(1 - u)^(-3/2), {u, 0, 3}];
curvaturePolynomialResidual = Expand[
  Integrate[z + z^3 c/6, {z, r, x}] -
    ((x^2 - r^2)/2 + c (x^4 - r^4)/24)
];

Print["round28EndpointResidual=", endpointResidual];
Print["round28ElasticityResidual=", elasticityResidual];
Print["round28ProjectionOrderingResidual=", projectionOrderingResidual];
Print["round28CurvatureSeries=", curvatureSeries];
Print["round28CurvaturePolynomialResidual=", curvaturePolynomialResidual];
projectionReplayOK = And @@ Thread[
  {endpointResidual, elasticityResidual, projectionOrderingResidual,
    curvaturePolynomialResidual} == 0
];
Print["round28ProjectionReplayOK=", projectionReplayOK];
Print["diagnosticOnly=True"];

If[! TrueQ[projectionReplayOK], Exit[1]];
