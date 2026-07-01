# Math Problem-Solving Workflow Report: Pólya Project

This repository uses the claim-centered proof-obligation workflow adapted from `yutianlee/gauss-circle-ai-collab`.

## Current State

The first theorem target is exact Dirichlet Pólya for spherical shells in `R^3`, starting with fixed shell ratio `rho`.

No theorem has been proved by this repository. The initial state is a planning and audit graph.

## Main Tracks

- `target_conventions`: counting convention, theorem statement, and success criteria.
- `source_audit`: FLPS balls, Bessel phase enclosures, annuli, shell Weyl/Bessel, Jiang-Lin, and Mathieu references.
- `flps_reproduction`: reproduce the disk/ball/annulus machinery.
- `shell_analytic`: Bessel cross-products, shell phase enclosures, weighted lattice counts, rho-uniformity.
- `certified_computation`: interval root isolation and finite-window verification.
- `ellipse_parallel`: Mathieu-function source audit and near-circular ellipse route.
- `certificate_family`: lower-risk Jiang-Lin-style comparison family.

## Round 1 Goal

Round 1 should refine the graph and route selection:

- target theorem memo,
- formula audit,
- source-audit priorities,
- shell-route blockers,
- finite verification plan.

The expected progress is a better graph, not a proof claim.
