# Handoff — DLEH preprint check, v4 authoring, and project close (2026-09-19)

**Founder's request (verbatim, across two turns):**
> '/home/yaoharee-lt/Downloads/DLEH_Fail_Closed_Open_Imagination_arXiv_v3_toledo_fixed.pdf' ่เอาเข้า glosa หน่อย ตรวจ และอัพเดก่อนลงจริง /model fable
> นายตัดสินใจ ใช้สองแกน ระดับโลก adversarial camera ready ทำได้เลย
> handoff สถานะล่าสุดและปิดโครงการ

Translation of intent: bring the preprint into glosa's process, check it, and update it before real
publication; the AI was delegated the two open judgment calls under two axes — world-class rigor and
adversarial-camera-readiness; then write this handoff and close the project.

## What exists now, and where

| Artifact | Location | State |
|---|---|---|
| **v4 of the preprint — submit this one** | `paper/main_v4.pdf` / `paper/main_v4.tex` (this repo, pushed, commit `995c141`) | Content-faithful to v3, three declared fixes applied, two more mechanical fixes applied after a second check, 11 pages, clean compile, populated PDF metadata |
| v3, as originally delivered | `paper/main.pdf` (this repo) | **Superseded. Kept unedited for the record. Do not submit.** |
| Full correction history | `docs/CORRECTIONS.md` (entries C1–C5) | Public, append-only |
| Tier-honest claim table | `CLAIMS.md` | Updated to point at v4 |
| glosa problem/claim/session records | `~/ANSE.ASIA/glosa/records/{problems,claims,sessions}/...-0001*` | **Valid, schema-PASS, but NOT committed to glosa's git history** (see blocker below) |

## The three real defects found and fixed in v3 → v4

1. **Reference [20]** cited a git *blob* hash as if it were a commit hash. v4 cites the real commit
   (`2c6585ce1917e5547584ff18f8a70dacc3b79a74`) and additionally names the sibling repository
   (`information-discrete-math`) that actually holds the Coq source for `Alg_Q`, the S4 round-trip,
   and the `NEVER` clause — v3 attributed all of Eq. 2–11 to one Toledo file that covers only S3/S5.
2. **Table 3 / Section 15** printed counts (22/44/0, 24/48/3, 24/46/1) for an ancillary script that
   does not exist anywhere in this workspace. v4 reports the counts of the script that actually
   ships with the paper (`dleh_model_check.py`), re-executed for this revision: **29/38/0, 32/46/4,
   32/44/4** — this is now a claim the paper's own accompanying artifact reproduces on demand.
3. **No AI-assistance disclosure existed.** v4 adds one paragraph (Acknowledgements), naming the
   assistance by role only, no vendor name — per this workspace's standing rule and consistent with
   growing venue norms.

Two further mechanical defects were found by a *second*, separate check of the first v4 draft and
fixed immediately: empty PDF metadata (title/author/subject/keywords), and a duplicated QED mark at
the end of Theorem 1's proof. Seven DOIs that a first v4 draft had accidentally dropped from the
bibliography were also restored. Full narrative: `docs/CORRECTIONS.md` C4 (found v3 was never
actually fixed for defect 1–2, and that the companion repo's own prior "independent" review was not
genuinely independent — same session, 12 minutes apart) and C5 (v4 authored, second-checked, fixed).

## What is honestly still open — read before treating this as fully closed

- **The final, post-fix state of v4 has not itself been examined by any independent pass.** Every
  check that ran (two of them) found real problems in the draft it examined; the *last* round of
  fixes (PDF metadata, QED, DOIs) was applied and verified by this same session, not by a further
  independent agent. `CLAIMS.md` and the glosa claim card both record `independent_check.status:
  FAILED` for exactly this reason — not because v4 is known to be wrong, but because saying "PASSED"
  would overclaim what was actually checked. **A fresh, independent read of `paper/main_v4.pdf`
  before or shortly after arXiv submission is still worth doing.**
- **Independence class throughout is I2** (fresh in-session agents, same model family as the
  authoring session) — no cross-vendor AI check and no human check has occurred on any of this.
- **Open founder judgment call, not resolved here:** whether this workspace's "Core Epistemic
  Structure" disclosure block (Core Respondent / Interactional Expert / AI Model(s) Used, the
  2026-09-07 standing rule) applies to an external, arXiv-bound preprint as opposed to an internal
  document. v4 carries a shorter, standard-register AI-assistance disclosure instead, which satisfies
  the no-AI-attribution rule (role only, no vendor name) but is not literally that block's format.
  If the founder wants the literal block, it is a small addition to the Acknowledgements section of
  `paper/main_v4.tex`.
- **The companion repository (`morrocwi/dual-lane-epistemic-harness`) was already public before any
  of this session's checks ran** (created 2026-09-18T15:06 UTC). Everything found afterward was
  fixed forward (new commits, nothing rewritten in history). Whether the repository's git history
  itself should be scrubbed of the pre-fix commits is the founder's call, not made here.
- **`Th_coqc` figures throughout `CLAIMS.md`/`docs/CORRECTIONS.md`** are read from the Toledo/
  information-discrete-math closure record's own tables, not recompiled by any pass in this session
  — stated plainly in C3, not silently upgraded.

## glosa records — created, valid, but not committed

`~/ANSE.ASIA/glosa/records/sessions/bb-2026-09-19-01/BB-2026-09-19-01.yaml` (Blackbox Note, holds
the founder's verbatim lines), `records/problems/GLOSA-PC-20260919-0001.yaml`, and
`records/claims/GLOSA-CC-20260919-0001.yaml` all exist on disk and pass `./cli/glosa check`. **They
could not be committed to glosa's own git repository**: its pre-commit hook (`scripts/
check_forbidden_words.sh`) fails on **48 pre-existing hits elsewhere in the repository, none in the
three new files** — a standing debt of that repository, unrelated to this task, not fixed here (out
of scope; flagging it is the deliverable). The Blackbox Note session (`BB-2026-09-19-01`) was
**never closed** — `glosa session close` requires a human-authored retention note ("never AI-filled"
per the tool itself), which only the founder can supply. If the founder wants the session formally
closed:
```
cd ~/ANSE.ASIA/glosa
./cli/glosa session close --path records/sessions/bb-2026-09-19-01/BB-2026-09-19-01.yaml \
  --retention-note "<founder's own words>"
```

## Project status: CLOSED for now

Nothing further is queued. To resume: read this file, then `docs/CORRECTIONS.md` in full (C1–C5,
the honest account of every pass including the ones that were themselves later found wrong), then
`CLAIMS.md` for the current tier of every claim. Do not re-derive the citation/reproducibility
findings from scratch — they are already independently checked twice; the open item is a *third,
fresh* check of the current `paper/main_v4.pdf`, not a repeat of the first two.
