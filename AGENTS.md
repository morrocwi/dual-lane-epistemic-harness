# AGENTS.md - dual-lane-epistemic-harness

## What this repository is

The Dual-Lane Epistemic Harness (DLEH): a control architecture that separates epistemic
authorization from candidate generation for generative AI under evidence gaps. A `HOLD` state
blocks authorization but may open an explicitly labelled imagination lane (hypothesis, analogy,
counterfactual, or test proposal). The lens layer is grounded in the Toledo Readout Bridge - exact
return is licensed only in the retained algebra `Alg_Q`, approximate return is governed by the
Toledo radius and the fail-closed ACCEPT/HOLD gate. The paper's own new formal apparatus (Theorem 1,
invariants I1-I6) is `PROPOSAL / not yet in Toledo`, not an existing theorem - see
`docs/CORRECTIONS.md`. No LLM benchmark is reported (see `CLAIMS.md`).

## Read first

1. `README.md` - what this is, and what is and is not established.
2. `CLAIMS.md` - every claim, tagged with the tier its evidence earns.
3. `docs/CORRECTIONS.md` - a citation fix and a Toledo-registration gap found before deposit.
4. `docs/CONFORMANCE.md` - what the executable checker confirms, and what it does not.
5. `paper/main.pdf` - the preprint itself.

## Rules

- Do not cite Theorem 1 or invariants I1-I6 as an existing Toledo theorem; they are `PROPOSAL / not
  yet in Toledo` until the reuse-first pipeline (Toledo lookup -> Genesis compatibility -> reuse ->
  derive only the missing piece -> mark PROPOSAL) is run on them (`docs/CORRECTIONS.md` C3).
- Do not report the paper's printed Table 3 counts (22/44/0, 24/48/3, 24/46/1) as independently
  reproduced; this repository's own reconstruction gives different counts (`docs/CONFORMANCE.md`).
- A change to `dleh_model_check.py` that alters its state/edge counts must update
  `docs/RUN_LOG.txt` with a freshly executed run, not a hand-edited number.

## Programme map

This repository is one node of the Human-AI Readout Programme. Which repository answers which kind of
question, what to read first and which gate applies is kept in one place, the routing hub:
<https://github.com/morrocwi/main.hub> (start at its `AGENTS.md`, then `ROUTES.md`).
The hub holds pointers and pinned links only. It is a readout of one moment: when the hub and this
repository disagree, this repository wins.
