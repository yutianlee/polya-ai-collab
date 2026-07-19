(* Round 28 symbolic replay for the branchwise Cmax derivative identities. *)

ClearAll[t, mu, h, p, ap, g, m, B, k, u, W, lam, d, z, cEl, cCur];

W = mu/Pi (Tan[t] - t);
lam = h - W;
d = 1 - 2 t/Pi;
z = Pi/(2 t) - 1;
u = 3/4 - lam;

cEl = (p + ap) g lam - p/2 + d m/2 + B z + 2 u^2 - 1/8;
cCur = (p + ap) k (1 - Cos[t]) - p/2 + d m/2 + B z + 2 u^2 - 1/8;

checks = {
  FullSimplify[
    D[cEl, t] - ((4 u - (p + ap) g) D[W, t] - m/Pi - B Pi/(2 t^2))
  ],
  FullSimplify[
    D[cEl, {t, 2}] -
      (4 D[W, t]^2 + (4 u - (p + ap) g) D[W, {t, 2}] + B Pi/t^3)
  ],
  FullSimplify[
    D[cCur, t] -
      ((p + ap) k Sin[t] - m/Pi - B Pi/(2 t^2) + 4 u D[W, t])
  ],
  FullSimplify[
    D[cCur, {t, 2}] -
      ((p + ap) k Cos[t] + B Pi/t^3 +
        4 (D[W, t]^2 + u D[W, {t, 2}]))
  ],
  FullSimplify[
    D[g lam - k (1 - Cos[t]), t] - (-g D[W, t] - k Sin[t])
  ]
};

Print["round28DerivativeResiduals=", checks];
Print["round28DerivativeReplayOK=", And @@ Thread[checks == 0]];

If[! TrueQ[And @@ Thread[checks == 0]], Exit[1]];
