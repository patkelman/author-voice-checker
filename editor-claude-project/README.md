# editor-claude-project

The drop-in version of the editor. This folder is a self-contained Claude
project: no shell, nothing to install, nothing to run. Everything the editor
needs to work is a file inside this folder.

## Quick start

1. Create a new Claude project (or open an existing one).
2. Add every file in this folder to the project's knowledge: `identity.md`,
   `rules.md`, `examples.md`, and the four files under `reference/`.
3. Start a conversation and paste in a finished draft.
4. Ask for a review.

That's the whole setup. Claude reads `identity.md` to know who it is being
asked to act as, `rules.md` for how it decides what to flag, `examples.md`
for worked cases including each refusal in practice, and the files under
`reference/` for the pattern catalogue, the finding format, and the voice
profile template. Fill in your own profile from
`reference/voice-profile-template.md` and add it to the project if you want
voice-fidelity findings, or skip a profile entirely if you want
universal-layer findings only.

## What to expect back

A verdict, and a list of findings, each one naming a line, a rule, why it
matters for this reader, and a severity. Nothing is rewritten. Full shape:
`reference/critique-format.md`.

## The honest limit

There is no shell here, so the mechanically detectable patterns, dash
overreliance, paste artefacts, US spellings against a stated locale, and the
rest, get caught by reading rather than by a script. A language model reads
for these patterns well, but not identically on every single run: the same
draft, read twice, can catch a slip on one pass and miss the identical slip
on the next. `evidence/` at the top of this repository shows this directly,
across two independent runs of the same sixteen prompts.

If a deterministic floor for that mechanical subset matters more than the
convenience of no shell, the other version of this editor, `editor-claude-code/`,
ships the identical doctrine plus a small script that removes that variance.
This folder does not need it, and does not depend on it. What you get here is
the same judgement layer, reading carefully, run after run.
