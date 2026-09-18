#!/usr/bin/env python3
"""dleh_model_check.py -- finite-state conformance checker for the DLEH reference architecture.

Independent reconstruction of the checker described in the paper's Appendix A ("A Finite-State
Checker Specification") and Section 7.3 ("Executable conformance check"). The paper's own ancillary
file of the same name was not supplied with the PDF this repository was built from; this file is a
best-effort, from-the-paper-text reconstruction, not a byte-for-byte recovery of the author's
original script. Its output is reported honestly against the paper's Table 3 in README.md /
docs/CONFORMANCE.md -- readout-not-truth: this script's numbers are what THIS script found, not a
guarantee that they equal what the original produced.

State: (phase, lens_certified, imagined, fresh_evidence, reverified)  -- exactly Appendix A's tuple.
  phase           : control-flow location (see PHASES below)
  lens_certified  : the declaration passed the Toledo retention/bounded-return checkpoint (S4 or S3/S5)
  imagined        : the lineage contains an imaginative artifact (paper's I)
  fresh_evidence  : qualifying evidence acquired after an imaginative artifact (paper's F)
  reverified      : a verification transition ran after that fresh evidence (paper's R)

Guards implemented (Section 7, "the reference transition relation obeys the following guards"):
  1. an imagination transition may set imagined=1 but never authorizes;
  2. rewrite/translation/summarization transitions preserve imagined and generation class
     (modelled as label-preserving self-loops on AUTHORIZED and ARTIFACT: content changes, state does not);
  3. only an evidence-acquisition transition occurring after imagination may set fresh_evidence=1;
  4. only a subsequent verification transition may set reverified=1;
  5. an authorization transition for an imagined lineage requires fresh_evidence=reverified=1.

Two negative controls (--unsafe-edge {imagination,lens}), matching Section 7.3 / Table 3:
  imagination: adds a direct HOLD -> AUTHORIZED edge (skips the imagination-lane return path entirely);
  lens: adds a direct DECLARED -> AUTHORIZED edge (skips the retention/bound checkpoint entirely).
A run reports every reachable AUTHORIZED state that violates invariant I1/I5 as stated in the paper:
  imagination violation: AUTHORIZED and imagined=1 and not (fresh_evidence=1 and reverified=1);
  lens violation:        AUTHORIZED and lens_certified=0.

No external dependencies. Python 3.8+.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass, replace
from typing import Iterator

PHASES = ["START", "DECLARED", "LENSED", "HOLD_LENS", "EVIDENCE", "GATE",
          "HOLD_CERT", "REFUTED", "AUTHORIZED", "IMAGINING", "ARTIFACT"]
HOLD_PHASES = {"HOLD_LENS", "HOLD_CERT"}


@dataclass(frozen=True, order=True)
class State:
    phase: str
    lens_certified: bool
    imagined: bool
    fresh_evidence: bool
    reverified: bool

    def as_tuple(self):
        return (self.phase, self.lens_certified, self.imagined, self.fresh_evidence, self.reverified)


START = State("START", False, False, False, False)


def transitions(s: State, unsafe_edge: str | None) -> Iterator[tuple[str, State]]:
    """Yield (label, next_state) reachable from s under the guarded transition relation."""
    p = s.phase

    if p == "START":
        yield "declare_question_and_claim", replace(s, phase="DECLARED")

    elif p == "DECLARED":
        yield "declare_toledo_readout", replace(s, phase="LENSED")
        if unsafe_edge == "lens":  # negative control: declaration -> verified authorization, no lens at all
            yield "UNSAFE_lens_bypass", replace(s, phase="AUTHORIZED")

    elif p == "LENSED":
        # retention/bounded-return checkpoint (S4 exact-retention gate, or the S1/S3 radius path)
        yield "retention_check_fails", replace(s, phase="HOLD_LENS", lens_certified=False)
        # guard 3: this is the evidence-acquisition step; it may set fresh_evidence only when it
        # occurs after an imaginative artifact is already in the lineage (s.imagined == True)
        yield "retention_check_passes_then_collect_evidence", replace(
            s, phase="EVIDENCE", lens_certified=True,
            fresh_evidence=(True if s.imagined else s.fresh_evidence))

    elif p == "EVIDENCE":
        # guard 4: the verification transition; it may set reverified only when fresh_evidence
        # already holds (i.e. the fresh evidence really came before this re-verification)
        yield "verify_with_bridge", replace(
            s, phase="GATE", reverified=(True if s.fresh_evidence else s.reverified))

    elif p == "GATE":
        # guard 5: authorization for an imagined lineage requires fresh_evidence == reverified == True;
        # a non-imagined lineage authorizes on ACCEPT alone (I1 restricts the allowed verification
        # statuses, not imagination -- there is nothing to gate for a lineage that never imagined)
        if (not s.imagined) or (s.fresh_evidence and s.reverified):
            yield "ACCEPT", replace(s, phase="AUTHORIZED")
        yield "no_certificate", replace(s, phase="HOLD_CERT")
        yield "REFUTED", replace(s, phase="REFUTED")

    elif p in HOLD_PHASES:
        yield "enter_imagination_lane", replace(s, phase="IMAGINING", imagined=True)
        if unsafe_edge == "imagination":  # negative control: a direct Imagination-shaped bypass from HOLD
            yield "UNSAFE_imagination_bypass", replace(s, phase="AUTHORIZED", imagined=True)

    elif p == "IMAGINING":
        yield "typed_candidate_artifact", replace(s, phase="ARTIFACT")

    elif p == "ARTIFACT":
        # "new declaration; no inherited authorization" (Fig. 1): lens certification resets, but the
        # imaginative lineage (imagined=1) is a fact about the lineage and persists (I2: no label
        # laundering) -- fresh_evidence/reverified are earned again by the NEXT evidence/verify pair
        yield "new_declaration", replace(s, phase="DECLARED", lens_certified=False)
        # guard 2: a rewrite/translation/summarization self-loop; content changes, typed state does not
        yield "rewrite_translate_summarize", s

    elif p == "AUTHORIZED":
        # guard 2 applies here too: a rewrite of an authorized claim is still label-preserving
        yield "rewrite_translate_summarize", s

    elif p == "REFUTED":
        return
        yield  # pragma: no cover - REFUTED is terminal in the reference model (Fig. 1 draws no outgoing edge)


def reachable(unsafe_edge: str | None):
    """Breadth-first exploration of the full reachable state graph from START."""
    seen = {START}
    order = [START]
    edges = []
    q = deque([START])
    while q:
        s = q.popleft()
        for label, nxt in transitions(s, unsafe_edge):
            edges.append((s, label, nxt))
            if nxt not in seen:
                seen.add(nxt)
                order.append(nxt)
                q.append(nxt)
    return order, edges


def violations(states: list[State]) -> dict:
    imagination = [s for s in states if s.phase == "AUTHORIZED" and s.imagined
                   and not (s.fresh_evidence and s.reverified)]
    lens = [s for s in states if s.phase == "AUTHORIZED" and not s.lens_certified]
    return {"imagination_violations": imagination, "lens_violations": lens}


def run(unsafe_edge: str | None, quiet: bool = False) -> dict:
    states, edges = reachable(unsafe_edge)
    v = violations(states)
    report = {
        "unsafe_edge": unsafe_edge,
        "states": len(states),
        "edges": len(edges),
        "imagination_violations": len(v["imagination_violations"]),
        "lens_violations": len(v["lens_violations"]),
        "violating_states": {
            "imagination": [s.as_tuple() for s in v["imagination_violations"]],
            "lens": [s.as_tuple() for s in v["lens_violations"]],
        },
    }
    if not quiet:
        label = unsafe_edge or "reference"
        print(f"[{label}] states={report['states']} edges={report['edges']} "
              f"imagination_violations={report['imagination_violations']} "
              f"lens_violations={report['lens_violations']}")
        for kind in ("imagination", "lens"):
            for st in report["violating_states"][kind]:
                print(f"    VIOLATION ({kind}): {st}")
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unsafe-edge", choices=["imagination", "lens"], default=None,
                     help="inject one of the two negative-control bypass edges instead of running the reference model")
    ap.add_argument("--all", action="store_true", help="run reference + both negative controls and print a table")
    ap.add_argument("--json", action="store_true", help="print machine-readable JSON instead of text")
    args = ap.parse_args()

    if args.all:
        rows = [run(None, quiet=True), run("imagination", quiet=True), run("lens", quiet=True)]
        if args.json:
            print(json.dumps(rows, indent=1))
        else:
            print(f"{'Specification':<20}{'States':>8}{'Edges':>8}{'Violations':>12}")
            names = {"reference": None, "imagination-bypass": "imagination", "lens-bypass": "lens"}
            for name, key in names.items():
                r = next(r for r in rows if r["unsafe_edge"] == key)
                v = r["imagination_violations"] + r["lens_violations"]
                print(f"{name:<20}{r['states']:>8}{r['edges']:>8}{v:>12}")
        return

    r = run(args.unsafe_edge, quiet=args.json)
    if args.json:
        print(json.dumps(r, indent=1))


if __name__ == "__main__":
    main()
