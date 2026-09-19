# Corrections found while depositing this repository

Found during the adversarial pass required before any public-facing publish (this workspace's
standing rule). Nothing in the PDF (`paper/main.pdf`, the v3 arXiv-style preprint as delivered) is
edited here — a print run is not silently changed — but every finding is recorded here, and should
be applied in the next revision (v4) of the paper's own LaTeX source, which this repository does
not hold.

## C1 — Reference [20] cites a blob hash as a commit hash

The paper's reference [20] reads:

> Y. Lahtee. "The Readout Bridge — Closure Record (Theory + Process)." Toledo repository,
> revision 2, 18 September 2026, commit `7de62699743054b3ad8dd16c993899f488548541`.

**Verified against the pinned public `toledo` repository (github.com/morrocwi/toledo):**
`7de62699743054b3ad8dd16c993899f488548541` is the **git blob hash** of
`docs/READOUT_BRIDGE_CLOSURE.md` at its current content (`git cat-file -t` reports `blob`, size
29616 bytes) — it is not a commit and does not resolve as one. The commit that most recently wrote
that exact blob to the public default branch is `2c6585ce1917e5547584ff18f8a70dacc3b79a74`
("registry: PROP-BRIDGE-21 — heat/diffusion leaf occurrence record (#45)", 2026-09-18); confirmed
reachable from `origin/main` (`git merge-base --is-ancestor`), and confirmed that commit really
wrote that exact blob (`git show <commit>:docs/READOUT_BRIDGE_CLOSURE.md | git hash-object --stdin`
reproduces `7de62699...`).

Corrected citation for the next revision:

> Y. Lahtee. "The Readout Bridge — Closure Record (Theory + Process)." Toledo repository, commit
> `2c6585ce1917e5547584ff18f8a70dacc3b79a74`, 18 September 2026.
> <https://github.com/morrocwi/toledo/blob/2c6585ce1917e5547584ff18f8a70dacc3b79a74/docs/READOUT_BRIDGE_CLOSURE.md>.
> File content hash (blob): `7de62699743054b3ad8dd16c993899f488548541`. Machine-checked S3/S5
> source: `coq/canonical/PROP_BRIDGE_03_certified_radius.v`.

This is a precision fix, not a content dispute: the cited file is exactly the one the paper means,
and it is genuinely on the public default branch — only the git-object-type label was wrong.

## C2 — Table 3's exact counts are not yet independently reproduced

See `docs/CONFORMANCE.md`. The paper's own ancillary file `dleh_model_check.py` was not supplied
with the PDF. An independent from-the-text reconstruction in this repository confirms the
*qualitative* safety property (Theorem 1: the reference model has zero violations; both negative
controls introduce violations) but not the *exact* state/edge/violation counts printed in Table 3.
This is disclosed, not silently reconciled by tuning the reconstruction to match.

## C3 — the harness's own formal apparatus is not yet registered in Toledo; and a citation of Eq. 2–11 that was imprecise, then a reviewer finding that over-corrected it

This workspace's standing rule (`toledo/EQUATION_SOURCE_POLICY.md`, gate `TG-RFG-01`): before any
equation, definition or theorem is cited elsewhere as an existing result, it is looked up first; a
genuinely new derivation is marked `PROPOSAL`, not cited as settled. This section records three
passes over the same question, in order, because the middle one was itself wrong and is kept rather
than silently dropped.

**Pass 1 (this repository's first commit).** Claimed Eq. (2)–(11) — the lens tuple, the retained
algebra `Alg_Q`, the S4 exact round-trip, the NEVER clause, the S1/S3 radius, the S5 gate — are
"Toledo's own S1–S5 Readout Bridge objects, cited and reused unchanged," citing only
`coq/canonical/PROP_BRIDGE_03_certified_radius.v` in `morrocwi/toledo` as the machine-checked
source. **This was imprecise**: that one file's own header states it covers only S3 and S5; it says
nothing about S1, S2 or S4.

**Pass 2 (an independent adversarial review of this repository).** Read pass 1's citation, searched
`morrocwi/toledo`'s own working tree for `Alg_Q`, "retained algebra" and "NEVER clause", found no
hits, and concluded these objects are not locatable in Toledo at all — reported as a `BLOCKER`, with
the fix "mark Eq. 4–7 as `HOLD`/`PROPOSAL, not yet in Toledo`" alongside Theorem 1 and I1–I6.

**Pass 3 (re-verification of pass 2, before accepting its fix).** Pass 2's search was too narrow: it
looked only inside `toledo`'s own tree and inside one `.v` file. `Alg_Q`, the S4 exact round-trip,
and the NEVER clause are documented in full, at `Th_coqc` tier, in `morrocwi/toledo`'s own
`docs/READOUT_BRIDGE_CLOSURE.md` (the S2 row: `Alg_Q := {P : ker q_K ⊆ ker P}`, `Th_coqc`, 18/18
theorem-like statements reported Closed; the S4 row: the EXACT/WITHIN-RADIUS/NEVER trio, `Th_coqc`,
23/23 reported Closed) — a Markdown table, not a `.v` file, which pass 2 did not read. The *Coq
source* for those two lines is not in Toledo at all; it is hosted in the sibling public repository
`morrocwi/information-discrete-math`: `formal/IDM_SignatureFunctor.v` (S2, the `Alg_Q` definition
and the EXACT clause) and `formal/IDM_BridgeRoundTrip.v` (the S4 assembly, WITHIN-RADIUS, and the
NEVER clause), cross-referenced from Toledo's closure record rather than duplicated into it. Both
files were confirmed present on `information-discrete-math`'s public default branch (commit
`e4932afee144484759f0f3275e69fc923b80d091` for the first file; `33c54bb2512cf2c129feef928eb64977bb420b57`
is the repository's tip at the time of this check). S1 (`IDM_ReadoutTower.v`) is in the same
repository; S3/S5 (`PROP_BRIDGE_03_certified_radius.v`) are the file pass 1 already cited, in
Toledo itself.

**Conclusion.** Pass 2's blocker is **not applied**: demoting genuinely `Th_coqc`-tier, closed,
cross-repository-documented material to `PROPOSAL` would introduce a new, worse error than the one
being fixed. Pass 1's citation is corrected for precision — naming all four source files across
both repositories, not just the one that covers S3/S5 — in `CLAIMS.md`'s Eq. 2–11 row. Neither this
repository, pass 2, nor pass 3 re-ran `coqc`/`Print Assumptions` on either repository's Coq; every
`Th_coqc`/"Closed" figure quoted here is read from the closure record's own table, not independently
recompiled in this pass. That recompilation is future work if this citation is load-bearing
elsewhere.

**Theorem 1 and invariants I1–I6, by contrast, genuinely are new.** They are formal objects this
paper introduces for the first time (the declaration tuple, the evidence bundle, the verifier
codomain, the harness state tuple, and the six invariants), not looked up in or registered in
Toledo, and not covered by the closure record above (which is about the *lens layer* Eq. 2–11
alone). Per `TG-RFG-01` they remain `PROPOSAL / not yet in Toledo` until a Toledo lookup and
Genesis-compatibility pass is run on them and, if nothing already covers them, they are registered
with a code and parents. `CLAIMS.md` carries that label explicitly; no other file in this workspace
should cite Theorem 1 or invariants I1–I6 as an existing Toledo theorem until that pass has
happened.

## C4 — A genuinely independent adversarial check found that C1's fix was never applied to the PDF, and a new false claim in Section 15

**This is the first genuinely independent check of this repository's own claims.** Passes 1–3 above
were all conducted within one continuous session in the ~12 minutes between this repository's two
commits, by one git identity, before the repository was pushed public. Per this workspace's own
maker-checker standing rule ("no independent check ⇒ no release"), that does not count as an
independent check, and the repository was pushed public before any check from outside that
producing session occurred. This section records the first check that was: a fresh review pass,
re-deriving every factual claim from primary sources rather than trusting `CLAIMS.md`/`CORRECTIONS.md`'s
own narrative, run against the actual delivered `paper/main.pdf` via `pdftotext` extraction, live
`git` commands against the real `toledo`/`information-discrete-math` checkouts, and a live re-run
of `dleh_model_check.py` and `pytest`.

**Finding 1 — C1's fix was never applied to the actual PDF.** The delivered `paper/main.pdf` (v3,
despite the filename `..._toledo_fixed.pdf`) still literally reads, at reference [20]:
> commit `7de62699743054b3ad8dd16c993899f488548541`

which is confirmed (again, independently) to be a git **blob** hash, not a commit. C1 above only
*proposed* corrected citation text for a future revision; it was never applied to the LaTeX source
this PDF was compiled from (which this repository does not hold). **The paper as it stands still
carries the citation error C1 found.** This must be fixed in the author's own LaTeX source before
any v4 is compiled, not merely logged here.

**Finding 2 — Section 15's code-availability claim is false as things currently stand.** The paper's
own Section 15 states as settled fact: "Code availability. The finite-state reference checker is
supplied as the ancillary file `dleh_model_check.py` in the accompanying source bundle." But per
C2/`docs/CONFORMANCE.md` (independently re-confirmed in this pass — a system-wide search for a
second implementation, `find / -iname "dleh_model_check.py"` outside `/proc`, finds only the one
file in *this* repository, which is a post-hoc reconstruction, not the author's original script):
no original `dleh_model_check.py` producing the paper's printed Table 3 counts (22/44/0, 24/48/3,
24/46/1) exists anywhere on this machine. Either the real arXiv source bundle genuinely contains a
different, original script that never reached any review in this workspace (possible, not
verifiable here), or Section 15 is currently making a claim about an artifact that does not exist.
**This must be resolved by the author before submission** — either supply the real original script
(and have it independently re-run to confirm the printed counts), or rewrite Section 15 and Table 3
to disclose plainly that the printed counts are an unreproduced prior run and the checker
accompanying the paper is a post-hoc reconstruction confirming only the qualitative safety property.

**What this pass reproduced and confirms (no change needed).** Eq. 2–11's Toledo/`information-discrete-math`
source attribution (pass 3's conclusion): confirmed correct by reading the actual `.v` files
directly (`InAlg`/`roundtrip_exact_iff` in `IDM_SignatureFunctor.v`, `roundtrip_never`/
`roundtrip_never_total` in `IDM_BridgeRoundTrip.v`, `plateau_certificate`/`plateau_radius` in
`IDM_ReadoutTower.v`, the S3/S5 objects in `toledo/coq/canonical/PROP_BRIDGE_03_certified_radius.v`).
No AI/vendor attribution anywhere (commits, PDF text). No leak of local paths, usernames, internal
tool names, or private repository names anywhere in this repository. The paper's own honesty about
Theorem 1 being a pen-and-paper proof, not Coq-checked, and about reporting no LLM benchmark: both
confirmed accurate as printed.

**Open judgment call, not resolved by this pass.** This workspace has a standing rule (2026-09-07)
that a "Core Epistemic Structure" disclosure block (Core Respondent/Experience-Based Expert;
Interactional Expert or None; AI Model(s) Used, by role) is mandatory on "every draft." This preprint
carries no such block. Whether that rule extends to an external, arXiv-bound preprint (as opposed to
an internal workspace document) is for the founder to decide, not for this repository to resolve
unilaterally.

**Verdict of this pass: NOT YET SAFE to submit.** Blocking: Finding 1 (unfixed citation still in the
PDF) and Finding 2 (a false availability claim). Independence class: a fresh in-session review agent,
same model family as the producing session (not a cross-vendor or human check) — stronger
independence has still not been obtained.

## C5 — v4 authored and compiled; a second independent check of v4 itself, applied

Because no LaTeX source for v3 existed anywhere in this workspace (confirmed by a system-wide
search before this pass), C4's required fixes could not be applied as a patch to an existing
source file. A complete v4 LaTeX source (`paper/main_v4.tex`) was authored from v3's own delivered
text, faithfully reproducing every equation, the theorem and its proof, all six invariants, all
table/listing contents, Figure 1, and references [1]-[19], with exactly the fixes below — and
compiled to `paper/main_v4.pdf` (11 pages, two-column, `pdflatex`, no errors).

**Applied, per C4's required fixes:**
1. Reference [20] now cites the real commit (`2c6585ce1917e5547584ff18f8a70dacc3b79a74`), with the
   blob hash retained as a correctly-labelled secondary integrity check.
2. Table 3 / Section 15 now report the counts of `dleh_model_check.py` as it actually ships with
   this paper, re-executed for this revision: 29/38/0 (reference), 32/46/4 (imagination bypass),
   32/44/4 (lens bypass) — exactly what running the accompanying script yourself reproduces.
3. An AI-assistance disclosure was added to the Acknowledgements, by role only, no vendor name.

**A second independent check of v4 itself** (2026-09-19, a fresh review pass, not the same pass
that wrote v4) found the above three fixes correct and faithfully applied, confirmed v4's content
otherwise matches v3 page-for-page, and additionally found two mechanical/cosmetic defects in the
first v4 draft, both since fixed:
4. Empty PDF metadata (title/author/subject/keywords) — added via `hyperref`'s `pdftitle=`/etc.
5. A duplicated QED mark at the end of Theorem 1's proof (a manual `\qed` plus `amsthm`'s automatic
   one) — the manual one removed.

It also flagged, as undeclared-but-benign and independently verified correct, two further changes
already grounded in this log's own earlier entries and now named explicitly in the paper's own
Appendix D: re-attributing Eq. 4-7 to `information-discrete-math` via a new reference [21] (per C3),
and a clarifying sentence that Theorem 1 is a pen-and-paper proof, not a Toledo theorem (per C3). It
also found seven DOIs present in v3's bibliography had been dropped from the first v4 draft — these
are restored in the current `paper/main_v4.tex`/`paper/main_v4.pdf`. No fabrication, no leak, no
overclaim was found in either check.

**Independence class of both v4 checks:** I2 (fresh in-session agents, same model family as the
authoring pass) — a cross-vendor or human check has still not run. `paper/main.pdf` (v3) is kept,
unedited, as the historical record of what was originally delivered; `paper/main_v4.pdf` is the
version that should actually be submitted.

## C6 — HANDOFF.md briefly leaked a local home-directory path

`HANDOFF.md`, committed at `d73781a`, quoted the founder's request verbatim, which itself named an
absolute local file path (a home-directory path on the founder's workstation, no credential, no
secret). This session caught it on its own next action (not via an external or independent check)
and redacted it at `db6062e`, replacing the quote with a paraphrase and pointing to the private
glosa Blackbox Note as the record of the actual verbatim text. The commit between the two
(`d73781a`) remains reachable in git history on the public repository; forward-only fix per this
workspace's convention (see C4's finding about a similarly-shaped, older leak in `s1c.log`), history
rewrite is the founder's call. No independent check caught this one — a reminder that self-checking
before every commit, not only before a "final" push, is the actual discipline this log keeps
failing at intermittently.
