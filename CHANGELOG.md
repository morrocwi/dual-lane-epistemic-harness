# Changelog

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
