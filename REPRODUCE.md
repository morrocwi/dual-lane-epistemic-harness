# Reproduce

```bash
git clone https://github.com/morrocwi/dual-lane-epistemic-harness
cd dual-lane-epistemic-harness
python3 dleh_model_check.py --all
python3 -m pytest tests/ -q
```

Requires only Python 3.8+ and (for the test suite) `pytest`. No network access, no external
package, no proprietary data. The exact output this repository's claims are read from is recorded,
verbatim, in `docs/RUN_LOG.txt`.

## What "reproduce" means here

- `dleh_model_check.py --all` reproduces this repository's own reconstruction of the paper's
  finite-state conformance check. It does **not** reproduce the paper's printed Table 3 counts —
  see `docs/CONFORMANCE.md` for the disclosed gap.
- `pytest tests/` reproduces the guard-level safety property (Theorem 1's claim), which the
  reconstruction does match qualitatively even though the exact counts differ.
