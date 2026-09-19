# Changelog

## [Unreleased] - 2026-09-19 (later same day)

- **v4 of the preprint authored and compiled** (`paper/main_v4.tex`, `paper/main_v4.pdf`; no LaTeX
  source for v3 existed anywhere in this workspace, so v4 is a complete, faithful re-authoring from
  v3's own delivered text, not a patch). Fixes both C4 blockers (reference [20]'s citation; Table 3/
  Section 15's counts, now the checker's real, re-executed output: 29/38/0, 32/46/4, 32/44/4) and
  adds an AI-assistance disclosure. A second, separate independent check of v4 itself found and
  this pass fixed two further defects (empty PDF metadata, a duplicated QED mark) and restored
  seven DOIs an earlier v4 draft had dropped from the bibliography; full account in
  `docs/CORRECTIONS.md` C5. `paper/main.pdf` (v3) is kept, unedited, as the historical record;
  **`paper/main_v4.pdf` is the version to submit.** `README.md`/`CLAIMS.md` updated accordingly.
  Independence class of every check so far: I2 (fresh in-session agents, same model family) — no
  cross-vendor or human check has occurred.

## [Unreleased] - 2026-09-19

- `docs/CORRECTIONS.md` C4: the first genuinely independent adversarial check of this repository
  (prior passes C1-C3 were all within one ~12-minute, single-identity session, before this
  repository's public push -- not independent by this workspace's own standard). Findings:
  (1) reference [20]'s blob-hash-as-commit error, which C1 only drafted a fix for, is **still
  present in the delivered `paper/main.pdf`** -- the fix was never applied to the actual submission
  artifact; (2) Section 15's "the finite-state reference checker is supplied as the ancillary file"
  claim is **not supported** -- no original script producing the paper's printed Table 3 counts
  exists anywhere searched. `CLAIMS.md` updated accordingly. **Verdict: NOT YET SAFE to submit** the
  preprint until both are resolved in the author's own LaTeX source. Independence class of this
  check: I2 (fresh in-session agent, same model family) -- a cross-vendor or human check is still
  stronger and has not run.

## [0.1.0] - 2026-09-18

- Initial deposit: preprint v3 (`paper/main.pdf`), an independent reconstruction of the finite-state
  conformance checker (`dleh_model_check.py`) with a guard-level test suite, and a pre-deposit
  corrections log (`docs/CORRECTIONS.md`): reference [20] cited a git blob hash as a commit hash
  (corrected pointer given); the paper's own printed Table 3 counts are not yet independently
  reproduced (disclosed in `docs/CONFORMANCE.md`); the harness's new formal apparatus (Theorem 1,
  invariants I1-I6) is marked PROPOSAL / not yet in Toledo per this workspace's TG-RFG-01 gate.
- Not yet deposited to Zenodo; no DOI assigned.
- Pre-push adversarial review round 2 found the Eq. 2-11 citation in `CLAIMS.md`/`README.md` named
  only one of four source files (S3/S5 only); the review's own proposed fix (demote to PROPOSAL)
  was independently re-checked and found wrong — `Alg_Q`, S4 and the NEVER clause are real,
  `Th_coqc`-tier, closed, documented in `toledo/docs/READOUT_BRIDGE_CLOSURE.md` with Coq source in
  `information-discrete-math`. Citation corrected to name all four files across both repositories
  instead. Full three-pass account in `docs/CORRECTIONS.md` C3. `LICENSES.md` coverage gap (a few
  untracked-by-either-bucket files, and a phantom `Makefile` reference) also fixed.
