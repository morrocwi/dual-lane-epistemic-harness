# Corrections found while depositing this repository

Found during the adversarial pass required before any public-facing publish (this workspace's
standing rule). Nothing in the PDF (`paper/main.pdf`, the v3 arXiv-style preprint as delivered) is
edited here — a print run is not silently changed — but every finding is recorded here, and should
be applied in the next revision (v4) of the paper's own LaTeX source, which this repository does
not hold.

## C1 — Reference [20] cites a blob hash as a commit hash

The paper's reference [20] reads:

> Y. Lahtee. "The Readout Bridge — Closure Record (Theory + Process)." Toledo repository,
> revision 2, 18 September 2026, commit `7de62699743054b3ad8dd16c993899f488548541`.

**Verified against the pinned public `toledo` repository (github.com/morrocwi/toledo):**
`7de62699743054b3ad8dd16c993899f488548541` is the **git blob hash** of
`docs/READOUT_BRIDGE_CLOSURE.md` at its current content (`git cat-file -t` reports `blob`, size
29616 bytes) — it is not a commit and does not resolve as one. The commit that most recently wrote
that exact blob to the public default branch is `2c6585ce1917e5547584ff18f8a70dacc3b79a74`
("registry: PROP-BRIDGE-21 — heat/diffusion leaf occurrence record (#45)", 2026-09-18).

Corrected citation for the next revision:

> Y. Lahtee. "The Readout Bridge — Closure Record (Theory + Process)." Toledo repository, commit
> `2c6585ce1917e5547584ff18f8a70dacc3b79a74`, 18 September 2026.
> <https://github.com/morrocwi/toledo/blob/2c6585ce1917e5547584ff18f8a70dacc3b79a74/docs/READOUT_BRIDGE_CLOSURE.md>.
> File content hash (blob): `7de62699743054b3ad8dd16c993899f488548541`. Machine-checked S3/S5
> source: `coq/canonical/PROP_BRIDGE_03_certified_radius.v`.

This is a precision fix, not a content dispute: the cited file is exactly the one the paper means,
and it is genuinely on the public default branch (`git merge-base --is-ancestor` confirmed against
`origin/main`) — only the git-object-type label was wrong.

## C2 — Table 3's exact counts are not yet independently reproduced

See `docs/CONFORMANCE.md`. The paper's own ancillary file `dleh_model_check.py` was not supplied
with the PDF. An independent from-the-text reconstruction in this repository confirms the
*qualitative* safety property (Theorem 1: the reference model has zero violations; both negative
controls introduce violations) but not the *exact* state/edge/violation counts printed in Table 3.
This is disclosed, not silently reconciled by tuning the reconstruction to match.

## C3 — The harness's own formal apparatus is not yet registered in Toledo

This workspace's standing rule (`toledo/EQUATION_SOURCE_POLICY.md`, gate `TG-RFG-01`): before any
equation, definition or theorem is cited elsewhere as an existing result, it is looked up in Toledo
first; a genuinely new derivation is marked `PROPOSAL`, not cited as settled.

Equations (2)–(11) in the paper (the lens tuple, the retained algebra, the NEVER clause, the S1–S5
radius and gate) are Toledo's own S1–S5 Readout Bridge objects, cited and reused unchanged — no
issue there; that is exactly what the paper's Section 4 preamble says it is doing ("No external
mathematical formalism is imported into this section").

Equations (12)–(24) and Theorem 1, however — the declaration tuple `D`, the evidence bundle `E`,
the verifier codomain `S_V`, the harness state tuple `q`, invariants I1–I6, and the noninterference
theorem and its proof — are **new formal objects introduced by this paper**, not looked up in or
registered in Toledo. Per `TG-RFG-01` they are `PROPOSAL / not yet in Toledo` until a Toledo lookup
and Genesis-compatibility pass is run on them and, if nothing already covers them, they are
registered with a code and parents. `CLAIMS.md` in this repository carries that label explicitly; no
other file in this workspace should cite Theorem 1 or invariants I1–I6 as an existing Toledo
theorem until that pass has happened.
