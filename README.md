# author-voice-checker

An editor for people who draft with AI and publish under their own name. Hand
it a finished draft and it points at the lines that have drifted into generic
machine cadence, names the rule each one breaks, and hands the draft back. It
never rewrites.

Built to Clief Notes Weekly Comp #9, "The Editor." The brief is quoted verbatim
in `docs/brief.md`.

## The problem it solves

A draft written with AI help can be competent everywhere and still not sound
like you anywhere. The tells are small and specific: em dashes arriving in
clusters, three-part lists chosen for their shape, a redefinition that sounds
wise without saying anything, American spellings in a British writer's mouth,
words you would never use sitting comfortably under your own byline.
Spell-check misses all of it, because none of it is wrong. It is just not
yours.

This editor reads a finished draft and answers one question: where has this
stopped sounding like its author? It works in two layers. The universal layer
runs against a fifteen-pattern catalogue of AI-cadence tells
(`reference/ai-pattern-catalogue.md`) and needs nothing from you. The
voice-fidelity layer runs against a profile you fill in yourself from
`reference/voice-profile-template.md`: your banned words, your locale, your
writing samples, your habits of specificity. Supply a profile and both layers
run; skip it and the universal layer runs alone, and says so plainly at the
top of every review.

What comes back is a verdict and a list of findings, each naming a line, a
rule, why it fails for this reader, and a severity. Nothing is rewritten. The
weak lines are pointed at; fixing them stays your job.

## Why the editor ships twice

This repository holds the same editor twice, as two self-contained folders.
The doctrine, who the editor is, how it critiques, what it refuses, is
identical in both. They differ in one place only: how the mechanical rules,
the dash counting, the spelling checks, the paste artefacts, get enforced.

- **`editor-claude-project/`** is the drop-in the brief describes. Add its
  files to a Claude project and Claude becomes the editor. No shell, nothing
  to install. The mechanical rules are enforced the same way everything else
  is: by the model reading them and complying.
- **`editor-claude-code/`** is the identical editor plus `check.py`, a small
  script that enforces the mechanical rules as code, running as step zero
  before any judgement work.

That one difference is the experiment this repository documents, and
`evidence/` is where it plays out. Each folder stands alone; neither needs the
other, or this top level, to work. If you just want the editor, take the
project folder. If you have a shell and want the floor, take the code folder.

## How the drop-in version works

Create a Claude project, add every file from `editor-claude-project/` to its
knowledge, paste in a finished draft, ask for a review. `identity.md` tells
Claude who it is being asked to be, `rules.md` how it decides what to flag and
the requests it refuses, `examples.md` what good findings look like with each
refusal shown in practice, and the files under `reference/` carry the pattern
catalogue, the finding format, the test prompts, and the blank profile
template. The folder's own `README.md` holds the quick start.

Everything here, the judgement calls and the mechanical checks alike, is done
by reading. A language model reads for a locale slip or a dash cluster well,
and these files tell it to on every run. What it cannot promise is to do so
identically on every run. That limit is stated inside the folder rather than
hidden, because the rest of this repository exists to show exactly where it
bites.

## How the deterministic version works

Point Claude Code, or any agent with file access and a shell, at
`editor-claude-code/`. The folder's `CLAUDE.md` binds `check.py` as step zero,
so the floor runs before any judgement without needing to be remembered. The
script is stdlib-only Python and catches the mechanically detectable subset of
the catalogue: dash overreliance, paste and typography artefacts, buzzword
saturation, the bare amplifier, runs of bold-lead bullets, and, when a profile
is supplied, that profile's never-uses list and wrong-locale spellings. Its
findings come out in the same four-part shape as everything else, and the
judgement layer, identical to the project version, folds them into one review.

What the script flags, it flags on every run, by construction. What it cannot
do is judge cadence, hold a refusal, or weigh a voice; that stays the model's
work in both versions. `check.py` is a floor, not a replacement for the read.
The folder's own `README.md` holds the quick start, including the one extra
step.

## Why the difference matters

Run both versions against the same sixteen drafts, from a cold start on each
side, and read the replies together. On judgement, they agree: the same
verdicts, the same rules cited against the same lines, sixteen times over. The
doctrine lives in the files, and it holds in either container.

The mechanical layer is another story, and the editor's own prose is where it
shows. The rules require every review to stay clean of the patterns it flags.
Across the sixteen paired runs in `evidence/side-by-side/`, the code version's
replies contain zero em dashes. The drop-in version's replies contain
forty-three, spread across eleven of the sixteen, in reviews that cite the
dash rule against other people's drafts.

The sharper detail is that the drift is invisible from inside. Two of the
drop-in replies close by declaring their own prose checked and free of dashes.
In run 13 the claim is true. In run 9 the same claim sits at the bottom of a
reply carrying eight of them, one of them inside the sentence making the
claim. Same files, same model, same self-check, different run. A reader who
got that reply would have no way to know, and that is the case in one
sentence: attention-enforced rules fail intermittently and silently, and a
rule that holds on most runs is not a floor.

The live example shows the same gap on real work. Reviewing a real film-club
post against a filled profile with a British locale, the drop-in run caught
one of the draft's three American spellings; the code version's floor caught
all three, because a script checking spellings is not simultaneously weighing
anything else.

Neither version is the lesser one. The drop-in is the editor most people
should use, and its judgement is as good as the code version's, sometimes
warmer. The code version is for the work where "usually catches it" is not
enough. Shipping both, with the receipts, is the argument that the second
thing is worth having.

## The methodology

Sixteen worked examples, and one live one.

**The sixteen.** A fixed set of test prompts, shipped with the editor in
`reference/test-prompts.md`, spanning its whole surface: clean drafts, drafts
stacking catalogued patterns, rewrite requests the editor must refuse, "score
this out of 10", missing and minimal profiles, a bare sentence fragment, and a
meta-check of the editor's own most recent findings. Every draft, writer, and
profile in them is invented for this evidence and appears nowhere in the
editor's own files. Each prompt ran through both versions from a cold start:
the drop-in version in a fresh Claude project on a clean account with no
custom instructions, one conversation per run; the code version as a fresh
copy of its folder, invoked non-interactively from the shell, one session per
run. Same model on both sides.

**The receipts.** `evidence/side-by-side/` holds one file per prompt, sixteen
in all: how each side was run, the draft both reviewed, both replies verbatim
and unedited, and a short note on what that pair shows.
`evidence/deterministic-run/` holds the code side's raw transcripts, with the
full invocation, model, and session id for each run, so any of them can be
re-run and checked. Nothing in either folder is paraphrased.

**The live example.** `live-example-pats-film-club-post.md` is a real post of
mine, run through both versions against my own filled voice profile, with both
replies verbatim and a plain-English comparison at the end. The profile itself
ships beside it as `voice-profile-pat-kelman.md`, so you can read what both
versions were checking against. The sixteen fixtures show the editor's range
on invented work; this shows it on mine.

**Where the pattern catalogue comes from.** The L1 catalogue predates this
entry. I have run its earlier form against my own drafts for the past year,
the standing check on anything I publish under my own name, and generalised it
here so it holds for any author rather than encoding how I write. For this
entry I reviewed it against current work on how AI writing gives itself away,
from peer-reviewed corpus research to the field guides that track the tells as
they move, and it grew to fifteen patterns, the newest covering the paste and
typography artefacts a model leaves in a draft. The review also kept a rule it
could have dropped: the lone em dash has weakened as a signal since early
2026, as the reading shifted to the cluster rather than the single mark, and
the rule stays, because counting em dashes per hundred words already tests the
cluster and not the mark.

## Repo map

```
author-voice-checker/
├── README.md                        this file: the whole project, explained
├── docs/
│   └── brief.md                     the competition brief, quoted verbatim
├── editor-claude-project/           the drop-in: no shell, rules enforced by reading
│   ├── README.md                    quick start for this version
│   ├── identity.md                  who the editor is, what work it reviews
│   ├── rules.md                     how it critiques, and what it refuses
│   ├── examples.md                  worked critiques, including each refusal in practice
│   └── reference/                   pattern catalogue, finding format, profile template, test prompts
├── editor-claude-code/              the same editor plus check.py, rules enforced by code
│   ├── README.md                    quick start, including the check.py step
│   ├── CLAUDE.md                    binds check.py as step zero in Claude Code
│   ├── check.py                     the mechanical floor, stdlib only
│   └── (identity, rules, examples, reference: same doctrine)
├── live-example-pats-film-club-post.md   both versions on a real post, real profile
├── voice-profile-pat-kelman.md           the filled profile the live example ran against
└── evidence/
    ├── side-by-side/                sixteen receipts, both replies verbatim
    └── deterministic-run/           the code side's raw transcripts, re-runnable
```

## Against the brief's four judging criteria

- Does the editor actually critique, rather than rewrite, summarise, or
  praise: the refusal set in either `rules.md`, each refusal shown in practice
  in `examples.md`, and held from a cold start in the receipts.
- Is the domain specific enough to be useful: `identity.md`, the writer who
  drafts with AI and still needs the finished piece to sound like them.
- Is the methodology clean, one job per file: the folder layout above, and the
  one-job header at the top of each file.
- README quality, can a stranger figure it out: this file for the entry as a
  whole, plus a self-contained quick start inside each folder.
