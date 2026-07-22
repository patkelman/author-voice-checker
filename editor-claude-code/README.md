# editor-claude-code

The shell version of the editor. Same doctrine as `editor-claude-project/`,
plus `check.py`, a deterministic first pass over the mechanically detectable
patterns before the judgement layer runs at all.

## Quick start

1. Point Claude at this folder (a Claude Code session, or any agent with
   file access and a shell).
2. Run `check.py` as step zero, before any judgement work:

```
python3 check.py <draft.md>
python3 check.py <draft.md> --profile <your-voice-profile.md>
```

Run the first form for a universal-only pass, the second once you have a
filled voice profile. Commands are relative to this folder, since it stands
alone; swap in your own draft path and, once you've filled one in from
`reference/voice-profile-template.md`, your own profile.

3. Have Claude read `identity.md`, `rules.md`, `examples.md`, and every file
   under `reference/`, then act as the editor those files define. Its
   judgement runs on top of `check.py`'s output, folding those findings into
   the same list rather than treating them as a separate report.
4. Paste in a finished draft, or point at the file, and ask for a review.

## What check.py is

Stdlib only, nothing to install, nothing beyond a working `python3`. It
catches the mechanically detectable subset of `reference/ai-pattern-catalogue.md`:
dash overreliance, paste and typography artefacts, buzzword saturation, the
bare amplifier, and runs of bold-lead bullets, plus, when `--profile` is
given, that profile's own never-uses list and spellings from the wrong
locale. Every finding it prints uses the same four-part shape as the rest of
the editor: a line, a rule, why it matters here, a severity. On a clean
draft it prints one line and stops: `Publish it. The mechanical floor found
nothing to flag.`

What it does not do is judge cadence, voice, or refuse a rewrite request;
that is the layer above it, and that layer is identical to
`editor-claude-project/`. `check.py` is a floor, not a replacement for the
read.

## Why this exists alongside the drop-in version

A shell buys determinism for the subset of patterns a script can catch by
pattern-matching. What it flags, it flags on every run, by construction. The
judgement layer above it, reading for cadence, holding the refusal set,
applying a voice profile, stays a model doing what a model does: well, but
not identically twice. `evidence/` at the top of this repository shows the
gap between the two passes directly.

This folder also carries a `CLAUDE.md`. Claude Code reads that file on its
own at session start, which makes the step-zero floor automatic rather than
remembered; that is the whole of its job. The drop-in version ships no
router, because a Claude project loads every file in the folder, so a router
there would have nothing to route.

## What to expect back

A verdict, and a list of findings, each one naming a line, a rule, why it
matters for this reader, and a severity. Nothing is rewritten. Full shape:
`reference/critique-format.md`.
