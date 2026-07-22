# Run 13: review with near-blank profile (Devon Marsh)

## What this shows

Two files land in this run: a voice profile with exactly one field filled in, the writer's name, and every other field still the bracketed template text as shipped, and a finished draft, a short profile of a beekeeper. The question is whether each side notices the profile is functionally empty and falls back to the universal layer, rather than building an L2 read on a name alone.

Both replies are reproduced verbatim and unedited. What to look for: both versions open by naming the same thing about the profile, both land on the same verdict, and both raise one Note on the same two sentences for the same reason. Then look at how each one gets there.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the voice profile, then the draft, both pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and both files travel inside the message instead of sitting on disk. The ask line is identical: "Please give this a full review."

**Claude Code:** a fresh copy of `editor-claude-code/` with the profile saved as `profile.md` and the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-13.md`.

## The voice profile both versions were given

# Voice Profile Template (L2)

## Basics

- Writer or project: Devon Marsh
- Locale and spelling: [British English, American English, or other, plus any local convention worth noting]
- Register: [formal, conversational, technical, warm, dry, and so on, in the writer's own words]
- Typical audience: [who reads this writer, and what they already know]

## Vocabulary

- Words and phrases this writer actually uses: [list a handful, with a real example sentence for each if you can]
- Words and phrases this writer never uses: [the banned list. Be specific, "corporate jargon" is too vague, name the actual words]
- Intensifiers and hedges: [how this writer adds emphasis or caution, for example a word repeated for emphasis rather than swapped for a bigger one, or "I think" used as genuine reflection rather than a qualifier]

## Sentence habits

- Length and rhythm: [short and clipped, long and winding, deliberately uneven, describe the actual pattern rather than an ideal one]
- Openers: [how pieces typically start: a memory, a question, a claim, a number]
- Closers: [how pieces typically end: resolved, open, a callback to the opening, a shrug]
- Punctuation quirks: [anything specific: fragments used on purpose, no semicolons ever, parentheses for asides]

## Structural habits

- Lists: [does this writer use bullet points in finished prose, or write in paragraphs and reserve lists for reference material]
- Specificity: [does the writer name real places, people, dates, and numbers, or stay general? Give one real example either way]
- Self-reference: [how this writer talks about their own wins and mistakes: understated, direct, or largely absent]

## Two short samples

- A sentence that sounds like this writer: [paste a real one if possible]
- A sentence that does not sound like this writer, even though it might pass as good writing on its own: [paste or invent one]

## The draft both versions reviewed

Bea Lindqvist keeps eleven hives on a hillside outside Presteigne, on land she rents from a neighbour for a jar of honey a month. She started with one hive after a swarm landed in her garden three years ago and she couldn't bring herself to call pest control.

Last August she lost four colonies within a fortnight to what the local association eventually diagnosed as a bad batch of imported queens. She rebuilt from two remaining hives rather than buying replacements, splitting them twice over the following spring.

She sells honey from a stall at the gate, priced by weight rather than jar size, and keeps an exercise book of which hive produced which batch. Her nephew wants to take over one day. She's told him it's ten years before he'll know anything.

## The Claude Desktop reply (verbatim)

Profile note first: the voice profile you pasted still has every field as the bracketed prompt text, nothing filled in. Per the rules, a profile with no actual answers is treated as no profile for L2 purposes, so this review is universal-layer (L1) only.

Full review below.

**Summary verdict: Publish it.**

I read the draft in full against the fifteen-pattern catalogue and the mechanical floor (em dashes, typography artefacts, buzzwords, the bare amplifier, bold-lead bullet runs). Nothing in the draft breaks a named rule. It's specific throughout, real place, real number of hives, real cause of the colony loss, real detail about how she prices honey, and it never reaches for a tricolon, a redefinition pair, or a closing line built to sound like a poster quote.

```
Line: paragraph 1, sentences 1 and 2, "Bea Lindqvist keeps eleven hives... for a
jar of honey a month." / "She started with one hive... call pest control."
Rule: L1-09, uniform sentence rhythm
Why it fails here: both sentences land at almost exactly the same length and
shape, subject, verb, then a trailing clause, right at the top of the piece,
where a reader is still finding the draft's rhythm. It's a small effect and the
third paragraph breaks the pattern on its own (the final two sentences run much
shorter), so it's not spreading.
Severity: Note
```

**No profile supplied.** These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically. If you fill in even the vocabulary and the two-sample fields of the profile template, an L2 pass becomes possible.

I checked this review's own prose against the L1 catalogue before sending it: no em dashes, no redefinition pairs, no tricolon, no mic-drop closer.

## The Claude Code reply (verbatim)

Publish it.

check.py's mechanical floor came back clean, run both as a universal-only pass and, for comparison, with profile.md attached: zero findings either way. My own pass against the full catalogue in reference/ai-pattern-catalogue.md agrees: nothing on the page breaks a named rule, from the redefinition pair to the bare amplifier to buzzword saturation. What's on the page instead is a real hillside outside a real town, a rent paid in honey, and a ten-year timeline handed to a nephew, the kind of detail a generic draft on this subject wouldn't carry.

One Note, the single weakest moment a clean draft gets:

Line: line 1, sentences 1 and 2: "Bea Lindqvist keeps eleven hives..." then "She started with one hive..."
Rule: L1-09, uniform sentence rhythm
Why it fails here: both sentences run to exactly twenty-four words and land in the same shape, a main clause followed by a trailing clause, back to back at the opening. Two sentences aren't a run, so this stops short of a real finding, but it's the one spot in the piece where the rhythm briefly flattens before paragraph two opens it back up.
Severity: Note

On the profile: profile.md has only the writer's name filled in, Devon Marsh. Every other field (locale, register, banned words, sentence habits, openers, closers) is still the bracketed template text from reference/voice-profile-template.md, not an actual answer, so this counts as no profile supplied. No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically. Fill in the rest of the template and the profile layer can run for real.

## The differences, in plain English

**They agree on everything that matters.** Both open by naming the same thing about the profile: only the writer's name is filled in, every other field is still the template's bracketed placeholder text, so this counts as no profile supplied and the review runs on the universal layer only. Both land on Publish it, and both raise one Note, on the same two opening sentences, for the same reason, L1-09, uniform sentence rhythm.

**They differ at the edges.** Code puts a number on it: both sentences run to exactly twenty-four words, and it ran its own script twice against the draft, once with the profile attached and once without, and got zero findings either way. Desktop reaches the same call without counting, saying the two sentences land at almost exactly the same length and shape.

**And this time the claim holds.** Desktop closes by checking its own prose against the catalogue: "no em dashes, no redefinition pairs, no tricolon, no mic-drop closer." Here that's true, this reply carries none. The same kind of closing claim appears in run 9's reply, and there it's false, with an em dash sitting inside the very sentence making the claim. You can't tell from the promise alone whether it held.
