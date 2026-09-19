# Dual-Lane Epistemic Harness (DLEH)

**Fail closed for truth; remain open for imagination.**

A control architecture for generative AI under evidence gaps: verification status and generation
class are kept independent, so a system can hold a claim in `HOLD` — not authorized here and now —
while still emitting an explicitly labelled `Imagined Proposal` artifact. Imagination alone can
never perform the privileged authorization transition; a candidate becomes eligible for
authorization only by leaving the imagination lane, acquiring admissible evidence, and passing
verification under an explicit declaration. The lens layer is grounded in Toledo's Readout Bridge
rather than an unconstrained observation map: exact return is licensed only in the retained algebra
`Alg_Q`, irreversible merging is exposed by the bridge's `NEVER` clause, and approximate return is
governed by the Toledo radius and the fail-closed `ACCEPT`/`HOLD` gate.

> A system may imagine beyond the evidence, but it may not authorize beyond the evidence.

**Author:** Yaoharee Lahtee, Open Civil Science Initiative (ORCID
[0009-0005-3861-0626](https://orcid.org/0009-0005-3861-0626)). Preprint: v3, 18 September 2026
(`paper/main.pdf`).

## What is in this repository

| Path | What it is |
|---|---|
| `paper/main_v4.pdf`, `paper/main_v4.tex` | **v4, the current, corrected, camera-ready preprint** (2026-09-19): fixes reference [20]'s blob-hash-as-commit citation, replaces Table 3/Section 15 with the counts of the checker that actually accompanies the paper, and adds an AI-assistance disclosure. Full LaTeX source is held here (v3's was not). See `docs/CORRECTIONS.md` C4/C5 and the paper's own Appendix D for the complete, itemized diff against v3. |
| `paper/main.pdf` | v3, as originally delivered -- **superseded by v4, kept for the record**; do not submit this version (see C4/C5) |
| `dleh_model_check.py` | an executable finite-state conformance checker for the reference architecture |
| `tests/` | guard-level unit tests for the checker (the safety property, not the exact Table 3 counts) |
| `docs/CONFORMANCE.md` | what the checker confirms, what it does not, and why the counts differ from the paper's Table 3 |
| `docs/CORRECTIONS.md` | citation and provenance corrections found before this deposit (a wrong reference type, and a Toledo-registration gap) |
| `docs/RUN_LOG.txt` | the actual executed output the claims above are read from |
| `CLAIMS.md` | every claim in this repository, tagged with the tier its evidence actually earns |

## Read first

1. `paper/main.pdf` — the architecture: the dual-lane control flow (Fig. 1), the epistemic object
   model (`S_V = {Certified, Matched, Refuted, Hold}`, generation classes), the transition guards
   and Theorem 1, the imagination contract, and the evaluation protocol.
2. `CLAIMS.md` — what is and is not established, and at what tier.
3. `docs/CORRECTIONS.md` — two findings from the pre-deposit review: a mislabelled citation, and
   which parts of the paper's formal apparatus are new (not yet registered in Toledo).
4. `docs/CONFORMANCE.md` — the executable check and its honest gap against Table 3.

## Reproduce

```bash
python3 dleh_model_check.py --all      # reference model + both negative controls
python3 -m pytest tests/ -q            # 8 guard-level tests
```

No network access, no external package, no proprietary data (`REPRODUCE.md` has the exact commands
and their last recorded output).

## Relation to the rest of the Human-AI Readout Programme

DLEH's lens layer is inherited from the programme's Readout Bridge closure record (S1-S5, the
retained algebra `Alg_Q`, the `NEVER` clause, the `ACCEPT`/`HOLD` certificate) — recorded in
`toledo`'s `docs/READOUT_BRIDGE_CLOSURE.md`, with the underlying Coq split across `toledo`
(S3/S5) and `information-discrete-math` (S1, S2, S4); no new mathematics is introduced there
(`docs/CORRECTIONS.md` C3 has the exact file-by-file citation and its own correction history). Its `S_V` verification vocabulary (`Certified` / `Matched` / `Refuted` / `Hold`) is a typed
analogue of `readout_universe`'s evidence-tier discipline, applied to a control architecture rather
than a claim label. Its own new formal apparatus — the declaration/state tuples, invariants I1–I6,
and Theorem 1 — is `PROPOSAL / not yet in Toledo` (see `docs/CORRECTIONS.md` C3): read them as a
paper-internal argument, not as an existing Toledo theorem, until that pass is run.

## Programme map

This repository is one node of the Human-AI Readout Programme. Which repository answers which kind
of question, what to read first and which gate applies is kept in one place, the routing hub:
<https://github.com/morrocwi/main.hub> (start at its `AGENTS.md`, then `ROUTES.md`).
The hub holds pointers and pinned links only. It is a readout of one moment: when the hub and this
repository disagree, this repository wins.

## Licence

Code (`dleh_model_check.py`, `tests/`) is MIT (`LICENSE`). The paper and documentation
(`paper/`, `docs/`, this README, `CLAIMS.md`) are CC BY 4.0 (`LICENSE-TEXT.md`). See
`LICENSES.md` for the exact split.
