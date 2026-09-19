# Claims and their tier

Tier vocabulary borrowed from `readout_universe` (`Th_coqc` / `finite_diagnostic` / `Dr` / `Open` /
`fit_calibrated` / `definition`) and applied honestly here — a claim's stated strength never exceeds
what was actually checked, measured, or declared.

| Claim | Status / tier |
|---|---|
| The S1–S5 Readout Bridge equations DLEH's lens layer cites (Eq. 2–11) are the programme's own, unmodified | `Th_coqc` for every line (S1–S5), per `morrocwi/toledo`'s own closure record (`docs/READOUT_BRIDGE_CLOSURE.md`, commit `2c6585ce1917e5547584ff18f8a70dacc3b79a74`). The Coq source is split across two public repositories, not held entirely in Toledo: S1 (`IDM_ReadoutTower.v`) and S2/S4 — including `Alg_Q` (Eq. 4), the S4 exact round-trip (Eq. 5) and the NEVER clause (Eq. 6-7) — (`IDM_SignatureFunctor.v`, `IDM_BridgeRoundTrip.v`) live in `morrocwi/information-discrete-math`; S3/S5 (Eq. 8-11) live in Toledo's own `coq/canonical/PROP_BRIDGE_03_certified_radius.v`. This repository reuses, does not re-derive, and did not itself recompile the Coq (see `docs/CORRECTIONS.md` C3 for the correction history of this row). |
| Guards 1–5 (Section 7) are individually well-formed transition-relation restrictions | `definition` — stated, not measured |
| Theorem 1 (imagination noninterference): under guards 1–5 and integrity of transition metadata, no reachable authorized state descends from an imaginative artifact without a qualifying post-imagination evidence + re-verification pair | `Dr` — a paper-internal pen-and-paper proof (Section 7.2), not machine-checked, and **not yet registered in Toledo** (see `docs/CORRECTIONS.md` C3); do not cite as a Toledo theorem |
| Invariants I1–I6 | `definition` / `PROPOSAL, not yet in Toledo` (same reason as Theorem 1) |
| The reference finite-state model (this repository's `dleh_model_check.py`) has zero imagination- or lens-authorization violations, and both negative controls introduce violations | `finite_diagnostic` — executed, output in `docs/RUN_LOG.txt`; qualitative property matches the paper's Theorem 1 claim |
| The reference model's exact state/edge/violation counts equal the paper's printed Table 3 (22/44/0, 24/48/3, 24/46/1) | **Not supported** — this reconstruction gives 29/38/0, 32/46/4, 32/44/4; see `docs/CONFORMANCE.md` for why counts differ while the safety property still holds |
| DLEH reduces unauthorized-assertion rate, or improves creative-utility metrics, on any real LLM system | `Open` — the paper explicitly reports no LLM benchmark (its own "No fabricated model benchmark" box, Section 11); Section 11.4's H1–H4 are stated as preregistered hypotheses, not findings |
| Reference [20]'s citation of Toledo's closure record | **NOT FIXED in the delivered PDF.** `docs/CORRECTIONS.md` C1 correctly identified the blob-hash-as-commit error and drafted a fix, but C4 (an independent check, 2026-09-19) confirms the actual `paper/main.pdf` still carries the uncorrected citation. The LaTeX source (not held here) must be fixed before any v4 compile. |
| Section 15's code-availability claim ("the finite-state reference checker is supplied as the ancillary file `dleh_model_check.py`") | **Not supported / likely false as printed.** No original script producing the paper's Table 3 counts exists anywhere in this workspace (`docs/CORRECTIONS.md` C4, an independent, system-wide search). This repository's script is a post-hoc reconstruction, not the described ancillary artifact. |
| This repository's own prior corrections (C1–C3) were independently checked before its public push | **No.** C1–C3 were three passes inside one continuous session, ~12 minutes apart, one git identity — not independent by this workspace's own standard. `docs/CORRECTIONS.md` C4 (2026-09-19) is the first genuinely separate review pass, and it found the two items above; it did not, however, reach cross-vendor or human independence (I2, not I5). |

## What this repository is not

- Not a claim that DLEH has been run against a real generative model.
- Not a claim that the printed Table 3 counts have been independently reproduced.
- Not a Toledo registration of Theorem 1, invariants I1–I6, or any new equation — those remain
  `PROPOSAL / not yet in Toledo` until the reuse-first pipeline (Toledo lookup → Genesis
  compatibility → reuse → derive only the missing piece → mark PROPOSAL) is actually run on them.
