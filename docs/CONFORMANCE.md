# Conformance check — what was verified, and what was not

The paper's only quantitative result is a finite-state conformance check of the reference
architecture (Section 7.3, Table 3, Appendix A). Its ancillary artifact is named
`dleh_model_check.py` and described as "a small Python program with no external dependencies."
That file was **not included** with the PDF this repository was built from, and no draft of it was
found anywhere in this workspace. `dleh_model_check.py` in this repository is therefore an
**independent reconstruction from the paper's own text** (Section 7's five guards, Appendix A's
state tuple, Figure 1's control flow) — not a recovered copy of the author's original script, and
not verified to be behaviourally identical to it.

## What the reconstruction confirms (qualitatively)

Running `python3 dleh_model_check.py --all` on this reconstruction:

```
Specification         States   Edges  Violations
reference                 29      38             0
imagination-bypass        32      46             4
lens-bypass               32      44             4
```

- The reference model reaches **zero** imagination- or lens-authorization violations, matching the
  paper's qualitative claim that guards 1–5 (Section 7) are sufficient for Theorem 1.
- Both negative controls — a direct HOLD→AUTHORIZED bypass, and a direct DECLARED→AUTHORIZED bypass
  that skips the retention checkpoint — **do** introduce violations once added, in each case of the
  kind the paper says they should (imagination-shaped bypass flags at least one imagination
  violation; lens bypass flags at least one lens violation). This is the property Theorem 1 claims:
  imagination alone cannot reach the privileged authorization transition without a qualifying
  fresh-evidence/re-verification pair, and a materially changed lens cannot inherit authorization.

## What it does not confirm

The **exact counts** in Table 3 (22 states / 44 edges / 0 violations for the reference model; 24/48/3
for the imagination bypass; 24/46/1 for the lens bypass) are **not reproduced** by this
reconstruction (29/38/0, 32/46/4, 32/44/4 above). The state-space size depends on modelling choices
the paper's prose underdetermines — for example, exactly which transitions the paper's "rewrite /
translation / summarization" self-loop guard (guard 2) applies to, and whether a REFUTED state may
still enter the imagination lane. Different reasonable choices give different counts while
preserving the same qualitative safety property. Because the difference is a readout of *this*
script, not of the paper's own artifact, it is reported as an open item rather than resolved by
guessing which modelling choice the author used.

**Tier of this section: `Dr`** (a declared, reasoned reconstruction; not a reproduction of a
verified prior result — see `readout_universe`'s tier vocabulary, `main.hub`'s `claim-strength`
route). Anyone citing the 22/44/0 figures from the PDF should say so is an unreproduced claim from
the paper as printed until the author's own `dleh_model_check.py` is supplied and run, or this
reconstruction is confirmed by the author to match their intended model.

## Reproduce this reconstruction

```bash
python3 dleh_model_check.py --all          # the table above
python3 dleh_model_check.py                # reference model only, verbose
python3 dleh_model_check.py --unsafe-edge imagination
python3 dleh_model_check.py --unsafe-edge lens
python3 -m pytest tests/ -q                # guard-level unit tests (see tests/test_dleh_model_check.py)
```

No network access, no external package, no proprietary data. `python3 --version` at time of writing:
see `docs/RUN_LOG.txt`.
