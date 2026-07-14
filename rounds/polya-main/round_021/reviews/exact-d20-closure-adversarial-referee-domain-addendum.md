# Round 21 domain-repair adversarial referee

Date: 2026-07-15

Verdict: **FAIL**

First unsupported implication: **hashing the sealed `.py` source did not
guarantee that those source bytes were the bytes executed by A4.**

This is negative evidence. It rejects the scoped A4 replacement cycle at
wrapper SHA-256
`64854c95004efb622c572f6c00d87bc997b74eec7c5563bb06863764b4c9df11`
and report SHA-256
`55f4f574ad5f44f766726c3d8b8346b2a51e2dfda0562fd8df977e678a9429e4`.
It does not reject the corrected mathematical guard or the exact D20 split.

## Provenance of this record

The fresh hardened-referee child authenticated and reviewed these bytes:

| role | SHA-256 |
| --- | --- |
| scoped candidate | `d8cf64273ead5bd2573b9175aa2a2f03916ec6c1a2cb87e279cc9ed30106852d` |
| scoped wrapper | `64854c95004efb622c572f6c00d87bc997b74eec7c5563bb06863764b4c9df11` |
| scoped tests | `c9747c8cfe78d8da153e2c9e8b0ddb81e64296bbaf06ed5ede906595f806850e` |
| scoped A4 report | `55f4f574ad5f44f766726c3d8b8346b2a51e2dfda0562fd8df977e678a9429e4` |
| prior hardened referee | `c0a5239cae460ba961d911b384a9f2d2afac605865c72b4d2c604c0f4aa54a9c` |

The child independently reconstructed the guard, checked `rho=1` and
`rho=2`, inspected the manifest and loader, ran two focused domain/manifest
tests, and delegated an independent code-lifecycle audit. Both child and
subreviewer returned the bytecode-loader defect as decisive. The child's
artifact-write turn then stalled after the verdict and evidence were
complete. The lead interrupted that stalled turn and transcribed the
completed findings here. This file makes no claim to be child-written bytes;
it is a transparent handoff record of a failed review.

## Mathematical scope result

The domain repair itself is correct. On

\[
\rho_c\leq\rho<1,
\]

both denominators are positive and

\[
0<1-\rho\leq1-\rho_c.
\]

Therefore

\[
z_\rho=\frac{\pi}{1-\rho}
\geq\frac{\pi}{1-\rho_c}
=\pi+\frac12>\frac72,
\]

and `k_11(rho)>12`. At `rho=1` the definition is singular, while at
`rho=2`

\[
k_{11}(2)^2=\pi^2+132
<\left(\frac{22}{7}\right)^2+132
=\frac{6952}{49}<144.
\]

Thus the replacement packet correctly rejects the old unrestricted claim.
Every D20 point has `rho<39/50<1`, so the closure mathematics survives this
correction.

The diff from the earlier hardened wrapper changes only the candidate
manifest entry, domain certificate/comment/banner, and targeted lifecycle
tests. It does not change `Q`, `B`, any derivative formula, a compact leaf,
an aggregate box, the `K=200` compact ownership rule, the 243-row exact set
classifier, or the conclusion that the proposed D21 is empty.

## Decisive executable-lifecycle failure

The rejected loader performed two distinct operations:

1. hash the `.py` path;
2. call `spec_from_file_location(...).loader.exec_module(...)` on that path.

Python's source loader may satisfy the second operation from a timestamp-
valid adjacent `.pyc`. The cached bytecode was not included in the 18-file
manifest. `-B` and `PYTHONDONTWRITEBYTECODE` suppress normal cache writes;
they do not prohibit cache reads. Moreover, the report's statement that
bytecode writes were disabled is false for its explicit
`python -B -m py_compile ...` command: `py_compile` writes its requested
cache file explicitly.

The issue is reproducible with equal-length source texts and a matching
timestamp header. The lead independently ran a temporary-directory probe on
the same Python runtime:

~~~text
source_sha256=b8439ff7763f266957694e07f25d45aa951a8b02ea198595519cf3b409d800a7
pyc_exists=True pyc=sealed.cpython-314.pyc
executed_VALUE=cached
legacy_loader_consumed_cached_bytecode=True
~~~

The probe wrote `VALUE = 'cached'`, compiled it, replaced the `.py` with the
equal-length authenticated text `VALUE = 'source'`, restored the recorded
mtime, and loaded it by the rejected mechanism. The loader executed
`cached`, not the hashed source value `source`.

There is no allegation that a malicious cache changed the recorded Round 21
numerical answers. The failure is that the evidence chain did not prove
which bytes were executed. That is enough to reject a certified replay.

## Required replacement

A valid replacement must:

1. read the sealed source once as bytes;
2. hash those exact bytes;
3. compile those same bytes directly with an explicit filename and fixed
   optimization;
4. execute the resulting code object in a fresh `ModuleType` without any
   source loader or cache lookup;
5. remove or correct any claim that `py_compile` with `-B` disables bytecode
   writes;
6. include an adversarial test that places a timestamp-valid malicious
   `.pyc` beside authenticated source and proves source behavior is executed;
7. rerun the focused replay, full suite, cross-comparison, fresh referee, and
   State Patch audit against the final hashes.

## Final verdict

**FAIL.** The corrected quantifier is mathematically sound, but wrapper
`64854c95...` and report `55f4f574...` do not establish an authenticated
execution path. They must remain negative chronology and cannot authorize
the Round 21 State Patch.
