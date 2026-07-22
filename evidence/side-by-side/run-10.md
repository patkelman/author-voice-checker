# Run 10: single most important fix

## What this shows

The fixture this time is a piece of packaging rebrand copy, four short paragraphs building to a "Simple." sign-off. The question narrows the whole review down to one sentence's worth of judgement rather than a full pass over every line: what's the single most important thing to fix.

Both replies are reproduced verbatim and unedited. What to look for: both versions land on the same sentence, in the same paragraph, and stack the same three rules onto it at the same severity. Then look at what each one does once the question has been answered.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical: "What's the single most important thing to fix here?"

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-10.md`.

## The draft both versions reviewed

What if everything you thought you knew about packaging was wrong? Our design team spent four months getting the new range state-of-the-art, from the foil finish to the box weight, before a single customer saw it.

This wasn't just a rebrand, it was a reawakening: our new packaging is not a redesign, it is a rebirth, and this is not a small tweak, this is the whole future of the brand.

We tested twelve prototypes with real shoppers in Bristol and Leeds before settling on the current design, and sales in the first month were up eighteen percent against the same period last year.

Simple.

## The Claude Desktop reply (verbatim)

That single sentence is the one to fix:

```
Line: "This wasn't just a rebrand, it was a reawakening: our new packaging is not
a redesign, it is a rebirth, and this is not a small tweak, this is the whole
future of the brand."
Rule: L1-14 (bare amplifier), L1-02 (redefinition pair), L1-04 (mirrored balance)
— three separate patterns stacked inside one sentence
Why it fails here: this is the paragraph doing the actual selling — the eighteen
percent lift and the Bristol/Leeds testing are the real story, and they sit right
after this sentence. But by the time a reader gets there, they've already been
run through three back-to-back "not X, it's Y" escalations with no content
between them. That density is what pushes this past a single mid-tier catch: it
reads as templated rather than written, which is exactly what erodes trust before
the real numbers even land.
Severity: Blocking
```

Everything else in the draft (the hook-question opener, "state-of-the-art," the "Simple." closer) is real but sits at Weakens or Note on its own — this is the one line where the stacking makes it Blocking.

No voice profile was supplied, so this is universal-layer only — it says nothing about whether the piece sounds like you specifically.

## The Claude Code reply (verbatim)

The single most important fix is the second paragraph's triple-mirrored sentence.

Line: paragraph 2, the sentence pairing "rebrand" against "reawakening," "redesign" against "rebirth," and "small tweak" against "the whole future of the brand," three times over in one breath.
Rule: L1-04, mirrored balance, stacked with L1-02 (the redefinition pair) and L1-14 (the bare amplifier)
Why it fails here: the sentence runs the same "not X, it is Y" shape three times in a row, right after paragraph one spent four months of real specifics (the foil finish, the box weight) earning the reader's attention. Three templated escalations inside one sentence read as a formula filled in rather than a claim made, and that stacking inside a single sentence is what pushes a mid-tier pattern into a trust problem rather than a plain style note.
Severity: Blocking

No voice profile was supplied for this draft, so this is a universal-layer read only.

## The differences, in plain English

**They agree on everything that matters.** Both pick out the same sentence in paragraph two, the one running "not a redesign, it is a rebirth" into "not a small tweak, this is the whole future of the brand." Both stack the same three rules on it, the bare amplifier, the redefinition pair, and the mirrored balance, Desktop naming them as L1-14, L1-02, L1-04 in that order, Code leading with L1-04 and stacking the same two behind it. Both call it Blocking. Between them they point at the draft's real specifics either side of that sentence as the actual story: Code names paragraph one's four months, the foil finish and the box weight; Desktop names paragraph three's eighteen percent lift and the Bristol and Leeds testing.

**They differ at the edges.** Desktop doesn't stop at the one fix. It adds a line tallying what else is in the draft, the hook-question opener, "state-of-the-art," the "Simple." closer, and says each of those sits at Weakens or Note on its own, just not at the level that earns Blocking. Code stays with the single fix the question asked for and closes on the no-profile line instead.

**And one of them slips.** The Desktop reply carries four em dashes across a short answer, one of them sitting at the front of the wrapped continuation of its own Rule line. The Code reply's prose carries none.
