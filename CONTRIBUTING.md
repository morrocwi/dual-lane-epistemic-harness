# Contributing

This is a small, single-author reference repository. The preferred contribution is:

- an independent reproduction (or refutation) of the finite-state conformance check in
  `docs/CONFORMANCE.md`, ideally recovering or matching the paper's own printed Table 3 counts;
- a correction to `docs/CORRECTIONS.md` if you find another citation, provenance, or Toledo-first
  gap the pre-deposit review missed;
- a test in `tests/` that exercises a guard (Section 7) this repository's reconstruction gets wrong.

Please do not propose new mathematics or a new invariant here without first running the Toledo
reuse-first pipeline (`toledo/EQUATION_SOURCE_POLICY.md`, gate `TG-RFG-01`) and marking the result
`PROPOSAL` — the same discipline `docs/CORRECTIONS.md` C3 already applies to this paper's own
formal apparatus.

Open an issue before a large change.
