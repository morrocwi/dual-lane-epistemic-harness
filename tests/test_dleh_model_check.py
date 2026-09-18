"""Guard-level tests for dleh_model_check.py.

These test the SAFETY PROPERTY (Theorem 1) the paper actually claims, not the exact state/edge
counts in Table 3 — this reconstruction's counts differ from the paper's printed numbers and that
difference is disclosed in docs/CONFORMANCE.md rather than hidden by tuning the model to match.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from dleh_model_check import reachable, violations, State, START  # noqa: E402


def test_reference_model_has_zero_violations():
    states, edges = reachable(None)
    v = violations(states)
    assert v["imagination_violations"] == []
    assert v["lens_violations"] == []


def test_reference_model_reaches_authorized_without_imagination():
    states, _ = reachable(None)
    assert State("AUTHORIZED", True, False, False, False) in states


def test_reference_model_reaches_authorized_through_imagination_lane():
    # guard 5: an imagined lineage CAN authorize, but only with fresh_evidence and reverified both true
    states, _ = reachable(None)
    assert State("AUTHORIZED", True, True, True, True) in states


def test_imagination_bypass_negative_control_introduces_a_violation():
    states, _ = reachable("imagination")
    v = violations(states)
    assert len(v["imagination_violations"]) >= 1, "the injected HOLD->AUTHORIZED edge must be caught"


def test_lens_bypass_negative_control_introduces_a_violation():
    states, _ = reachable("lens")
    v = violations(states)
    assert len(v["lens_violations"]) >= 1, "the injected DECLARED->AUTHORIZED edge must be caught"


def test_no_imagined_lineage_authorizes_without_fresh_evidence():
    """Direct check of guard 5, independent of reachability: an imagined, unauthorized-evidence
    state must never appear as AUTHORIZED in the reference (non-bypass) transition relation."""
    states, edges = reachable(None)
    bad = [s for s in states if s.phase == "AUTHORIZED" and s.imagined
           and not (s.fresh_evidence and s.reverified)]
    assert bad == []


def test_refuted_is_terminal_in_the_reference_model():
    from dleh_model_check import transitions
    refuted = State("REFUTED", True, False, False, False)
    assert list(transitions(refuted, None)) == []


def test_start_state_is_unauthorized_and_uncertified():
    assert START.phase == "START"
    assert START.lens_certified is False
    assert START.imagined is False
