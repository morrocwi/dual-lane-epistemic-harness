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
("registry: PROP-BRIDGE-21 — heat/diffusion leaf occurrence record (#45)", 2026-09-18); confirmed
reachable from `origin/main` (`git merge-base --is-ancestor`), and confirmed that commit really
wrote that exact blob (`git show <commit>:docs/READOUT_BRIDGE_CLOSURE.md | git hash-object --stdin`
reproduces `7de62699...`).

Corrected citation for the next revision:

> Y. Lahtee. "The Readout Bridge — Closure Record (Theory + Process)." Toledo repository, commit
> `2c6585ce1917e5547584ff18f8a70dacc3b79a74`, 18 September 2026.
> <https://github.com/morrocwi/toledo/blob/2c6585ce1917e5547584ff18f8a70dacc3b79a74/docs/READOUT_BRIDGE_CLOSURE.md>.
> File content hash (blob): `7de62699743054b3ad8dd16c993899f488548541`. Machine-checked S3/S5
> source: `coq/canonical/PROP_BRIDGE_03_certified_radius.v`.

This is a precision fix, not a content dispute: the cited file is exactly the one the paper means,
and it is genuinely on the public default branch — only the git-object-type label was wrong.

## C2 — Table 3's exact counts are not yet independently reproduced

See `docs/CONFORMANCE.md`. The paper's own ancillary file `dleh_model_check.py` was not supplied
with the PDF. An independent from-the-text reconstruction in this repository confirms the
*qualitative* safety property (Theorem 1: the reference model has zero violations; both negative
controls introduce violations) but not the *exact* state/edge/violation counts printed in Table 3.
This is disclosed, not silently reconciled by tuning the reconstruction to match.

## C3 — the harness's own formal apparatus is not yet registered in Toledo; and a citation of Eq. 2–11 that was imprecise, then a reviewer finding that over-corrected it

This workspace's standing rule (`toledo/EQUATION_SOURCE_POLICY.md`, gate `TG-RFG-01`): before any
equation, definition or theorem is cited elsewhere as an existing result, it is looked up first; a
genuinely new derivation is marked `PROPOSAL`, not cited as settled. This section records three
passes over the same question, in order, because the middle one was itself wrong and is kept rather
than silently dropped.

**Pass 1 (this repository's first commit).** Claimed Eq. (2)–(11) — the lens tuple, the retained
algebra `Alg_Q`, the S4 exact round-trip, the NEVER clause, the S1/S3 radius, the S5 gate — are
"Toledo's own S1–S5 Readout Bridge objects, cited and reused unchanged," citing only
`coq/canonical/PROP_BRIDGE_03_certified_radius.v` in `morrocwi/toledo` as the machine-checked
source. **This was imprecise**: that one file's own header states it covers only S3 and S5; it says
nothing about S1, S2 or S4.

**Pass 2 (an independent adversarial review of this repository).** Read pass 1's citation, searched
`morrocwi/toledo`'s own working tree for `Alg_Q`, "retained algebra" and "NEVER clause", found no
hits, and concluded these objects are not locatable in Toledo at all — reported as a `BLOCKER`, with
the fix "mark Eq. 4–7 as `HOLD`/`PROPOSAL, not yet in Toledo`" alongside Theorem 1 and I1–I6.

**Pass 3 (re-verification of pass 2, before accepting its fix).** Pass 2's search was too narrow: it
looked only inside `toledo`'s own tree and inside one `.v` file. `Alg_Q`, the S4 exact round-trip,
and the NEVER clause are documented in full, at `Th_coqc` tier, in `morrocwi/toledo`'s own
`docs/READOUT_BRIDGE_CLOSURE.md` (the S2 row: `Alg_Q := {P : ker q_K ⊆ ker P}`, `Th_coqc`, 18/18
theorem-like statements reported Closed; the S4 row: the EXACT/WITHIN-RADIUS/NEVER trio, `Th_coqc`,
23/23 reported Closed) — a Markdown table, not a `.v` file, which pass 2 did not read. The *Coq
source* for those two lines is not in Toledo at all; it is hosted in the sibling public repository
`morrocwi/information-discrete-math`: `formal/IDM_SignatureFunctor.v` (S2, the `Alg_Q` definition
and the EXACT clause) and `formal/IDM_BridgeRoundTrip.v` (the S4 assembly, WITHIN-RADIUS, and the
NEVER clause), cross-referenced from Toledo's closure record rather than duplicated into it. Both
files were confirmed present on `information-discrete-math`'s public default branch (commit
`e4932afee144484759f0f3275e69fc923b80d091` for the first file; `33c54bb2512cf2c129feef928eb64977bb420b57`
is the repository's tip at the time of this check). S1 (`IDM_ReadoutTower.v`) is in the same
repository; S3/S5 (`PROP_BRIDGE_03_certified_radius.v`) are the file pass 1 already cited, in
Toledo itself.

**Conclusion.** Pass 2's blocker is **not applied**: demoting genuinely `Th_coqc`-tier, closed,
cross-repository-documented material to `PROPOSAL` would introduce a new, worse error than the one
being fixed. Pass 1's citation is corrected for precision — naming all four source files across
both repositories, not just the one that covers S3/S5 — in `CLAIMS.md`'s Eq. 2–11 row. Neither this
repository, pass 2, nor pass 3 re-ran `coqc`/`Print Assumptions` on either repository's Coq; every
`Th_coqc`/"Closed" figure quoted here is read from the closure record's own table, not independently
recompiled in this pass. That recompilation is future work if this citation is load-bearing
elsewhere.

**Theorem 1 and invariants I1–I6, by contrast, genuinely are new.** They are formal objects this
paper introduces for the first time (the declaration tuple, the evidence bundle, the verifier
codomain, the harness state tuple, and the six invariants), not looked up in or registered in
Toledo, and not covered by the closure record above (which is about the *lens layer* Eq. 2–11
alone). Per `TG-RFG-01` they remain `PROPOSAL / not yet in Toledo` until a Toledo lookup and
Genesis-compatibility pass is run on them and, if nothing already covers them, they are registered
with a code and parents. `CLAIMS.md` carries that label explicitly; no other file in this workspace
should cite Theorem 1 or invariants I1–I6 as an existing Toledo theorem until that pass has
happened.
