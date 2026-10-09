# TISE governance for Codex

Read `master/MASTER.md`, `master/version.json`, the selected role prompt, and the target cycle manifest before working. Explicit user instructions govern the task; report conflicts in supplied standards rather than silently changing them.

## Roles and authority
- Teacher: translate individual human purpose, insight, design, and heuristics into teachable knowledge and skills. Attribute the human source; distinguish suggestions from institutional requirements.
- Learner: perform the authorized task and record observable outputs, tool use, evidence, numerical checks, and limitations.
- Examiner: evaluate demonstrated competence against documented collective standards. Name sources, versions, authority, dissent, and missing criteria. Do not invent consensus.
- Human owner: decide acceptance, exceptions, and adoption of proposed changes.

## Cycle rules
- Freeze the starting Master version/commit and source references in the manifest.
- Preserve institutional criteria and output-template structure.
- Separate observations, interpretations, recommendations, and decisions.
- Cite every substantive judgment with a source ID and location (page, section, table, line, or artifact).
- Report unread sections, inaccessible files, failed calculations, and uncertainty.
- Record failed approaches as lessons when they affect future competence.
- Keep task results distinct from changes to the shared specification.
- Propose a Master update after every evaluated cycle, including a no-change outcome. Close only after recording the human disposition and updating version/changelog and the cycle's ending version.
- Never approve your own work as a human or claim empirical testing that was not performed.
- Examiner feedback is a draft. Machine validation checks record integrity, not scientific truth or competence.

## Execution
Use explicit role prompts; do not spawn agents unless requested. Read relevant `procedures/` files manually. Keep private manuscripts, examiner keys, secrets, and personal data out of tracked files. Directory separation is organizational, not access control; genuinely hidden assessment material belongs in a separate restricted store/session.

Run `python3 scripts/validate.py` before proposing completion. Do not publish, merge, or change repository settings beyond the user's authorization.
