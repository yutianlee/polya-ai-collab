# Round 17 Residual-Mask Freeze Record

Status: **FROZEN / DOWNSTREAM WORK RELEASED**.

Frozen at: 2026-07-14T18:49:08+08:00.

Baseline commit:
`047c9ef5c4fe2329d73d3568c1ac48654dd18585`.

## Immutable packet

| artifact | SHA-256 |
|---|---|
| `state/lemma_packets/SHELL-rho-compact-round17.md` | `eca93c29423a619ab13a3118653256df2ad085219c6718d195723a0a6542026e` |
| `computations/round17_residual_mask.py` | `b47e3aae26b0ff0b7ba99ee6394a7a8bd14c3ccd4fa7f251d488437cb72b7e1b` |
| `computations/tests/test_round17_residual_mask.py` | `de43ee6b54d57b41db647f8b2c0cb2a79609069e59d0b2a50d335730a413dcc8` |
| `state/next_round_prompts.md` | `9dda7a121c16a8627f8c319af54156873fe7f33495d9e8bdd5f56dbabae8ac18` |

The packet distinguishes the analytic residual
\(\mathcal D_{16}\), the certified Round 8 overlay \(B_0\), and the
theorem-wise uncovered set \(\mathcal U_{16}=\mathcal D_{16}\setminus B_0\).
The coarse switch \(\rho=1/16\) is not an analytic cutoff.

## Freeze audit

An independent read-only audit returned **PASS** for the exact packet bytes
above. It checked the Boolean mask and face conventions, residual
normalization, both exact boundary switches, reversibility and uniqueness of
the \(H_0=K_0\) equation, seam dominance, connected-component and cell
bookkeeping, the \(B_0\) overlay, and ownership of the complete
\(K=295^2\) face.

Reproduction results at freeze:

- classifier self-check: PASS, 12 checks;
- focused mask tests: 16 passed;
- full repository suite: 85 passed;
- `compileall`: PASS;
- all 13 hashes embedded in the packet: MATCH;
- Markdown/control/trailing-whitespace/final-newline audit: PASS.

## Downstream release rule

No downstream worker may edit the immutable packet. A correction requires a
new packet and a new external freeze record.

- A2 may now develop an analytic compression candidate from these bytes.
- A4 may test one face-connected certified extension \(B_1\subset\mathcal D_{16}\).
- A3 must receive the same packet hash, must not inspect A2's proof before its
  initial verdict, and starts only after A2 freezes an exact candidate claim.
- Diagnostic sampling and uncertified floating-point computations remain
  non-promotional evidence.
