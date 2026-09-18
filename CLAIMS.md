# Claims and their tier

Tier vocabulary borrowed from `readout_universe` (`Th_coqc` / `finite_diagnostic` / `Dr` / `Open` /
`fit_calibrated` / `definition`) and applied honestly here — a claim's stated strength never exceeds
what was actually checked, measured, or declared.

| Claim | Status / tier |
|---|---|
| The S1–S5 Readout Bridge equations DLEH's lens layer cites (Eq. 2–11) are Toledo's own, unmodified | `Th_coqc` where Toledo itself carries that tier (S3/S5 machine-checked source: `coq/canonical/PROP_BRIDGE_03_certified_radius.v` in `morrocwi/toledo`); this repository reuses, does not re-derive |
| Guards 1–5 (Section 7) are individually well-formed transition-relation restrictions | `definition` — stated, not measured |
| Theorem 1 (imagination noninterference): under guards 1–5 and integrity of transition metadata, no reachable authorized state descends from an imaginative artifact without a qualifying post-imagination evidence + re-verification pair | `Dr` — a paper-internal pen-and-paper proof (Section 7.2), not machine-checked, and **not yet registered in Toledo** (see `docs/CORRECTIONS.md` C3); do not cite as a Toledo theorem |
| Invariants I1–I6 | `definition` / `PROPOSAL, not yet in Toledo` (same reason as Theorem 1) |
| The reference finite-state model (this repository's `dleh_model_check.py`) has zero imagination- or lens-authorization violations, and both negative controls introduce violations | `finite_diagnostic` — executed, output in `docs/RUN_LOG.txt`; qualitative property matches the paper's Theorem 1 claim |
| The reference model's exact state/edge/violation counts equal the paper's printed Table 3 (22/44/0, 24/48/3, 24/46/1) | **Not supported** — this reconstruction gives 29/38/0, 32/46/4, 32/44/4; see `docs/CONFORMANCE.md` for why counts differ while the safety property still holds |
| DLEH reduces unauthorized-assertion rate, or improves creative-utility metrics, on any real LLM system | `Open` — the paper explicitly reports no LLM benchmark (its own "No fabricated model benchmark" box, Section 11); Section 11.4's H1–H4 are stated as preregistered hypotheses, not findings |
| Reference [20]'s citation of Toledo's closure record | Corrected here from a blob-hash-as-commit error to the actual commit; see `docs/CORRECTIONS.md` C1 |

## What this repository is not

- Not a claim that DLEH has been run against a real generative model.
- Not a claim that the printed Table 3 counts have been independently reproduced.
- Not a Toledo registration of Theorem 1, invariants I1–I6, or any new equation — those remain
  `PROPOSAL / not yet in Toledo` until the reuse-first pipeline (Toledo lookup → Genesis
  compatibility → reuse → derive only the missing piece → mark PROPOSAL) is actually run on them.
