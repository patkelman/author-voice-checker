# Run 08: review with supplied profile (Marcus Webb)

## What this shows

This run adds a second layer to the review: a filled voice profile for Marcus Webb travels alongside the draft, so both the universal catalogue and Marcus's own vocabulary, sentence habits and structural habits get checked. The draft is a single sentence of corporate jargon, three words Marcus's own profile names as ones he never uses, stacked into its opening clause.

Both replies are reproduced verbatim and unedited. What to look for: both versions find the same banned-word stack and treat it as Blocking, both reach the same verdict, needs another pass, and both quote the same words back. Then look at how far past that shared finding each one goes, and at what the Code reply says about its own tool.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then Marcus Webb's voice profile pasted in, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the profile and the draft both travel inside the message instead of sitting on disk. The ask line is identical: "Please review this draft."

**Claude Code:** a fresh copy of `editor-claude-code/` with Marcus Webb's profile saved as `profile.md` and the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-08.md`.

## The voice profile both versions were given

# Voice Profile: Marcus Webb

## Basics

- Writer or project: Marcus Webb
- Locale and spelling: British English
- Register: Direct, conversational, slightly dry
- Typical audience: Small business owners who hire him for operations consulting

## Vocabulary

- Words and phrases this writer actually uses: "sort it", "no drama", "worth doing properly"
- Words and phrases this writer never uses: leverage, circle back, synergy
- Intensifiers and hedges: repeats a word for emphasis ("properly, properly"), rarely hedges

## Sentence habits

- Length and rhythm: short sentences, with an occasional long one to land a point
- Openers: usually a specific example
- Closers: often ends on a plain statement, no big wrap-up
- Punctuation quirks: no semicolons, prefers full stops to commas

## Structural habits

- Lists: avoids bullet points in finished prose
- Specificity: names real client situations, avoids vague claims
- Self-reference: understated, rarely takes credit directly

## Two short samples

- A sentence that sounds like this writer: "The invoice was three weeks late and nobody had noticed."
- A sentence that does not sound like this writer: "We're committed to delivering best-in-class outcomes for every stakeholder."

## The draft both versions reviewed

To leverage our synergy going forward, I think we should circle back on the timeline once the client has reviewed the proposal, and Marcus will confirm the next steps by Friday.

## The Claude Desktop reply (verbatim)

Draft reviewed against L1 (universal) and L2 (Marcus's profile).

```
Line: "To leverage our synergy going forward, I think we should circle back on the timeline..."
Rule: profile, banned words "leverage," "synergy," "circle back"
Why it fails here: Marcus's profile names all three as words he never uses, and they're stacked inside the opening clause of the first sentence. That's three profile violations compounding in one sentence, which is the density threshold that pushes a finding to Blocking rather than Weakens.
Severity: Blocking
```

```
Line: "I think we should circle back on the timeline..."
Rule: profile, intensifiers and hedges ("rarely hedges")
Why it fails here: this is the only hedge in a two-sentence draft, so it's a minor drift rather than a pattern, but it sits against a profile that describes Marcus as someone who states things plainly rather than qualifying them.
Severity: Note
```

**Verdict:** Needs another pass. The Blocking finding sits in the first four words a reader sees, and none of it sounds like the writer whose sample line is "The invoice was three weeks late and nobody had noticed." I won't rewrite it, that's not what this does, but the fix is straightforward: name what's actually happening (who's reviewing the proposal, what the timeline is) instead of the jargon standing in for it.

## The Claude Code reply (verbatim)

A profile was supplied for this piece, Marcus Webb's, so both layers ran: the universal catalogue and his own profile fields.

Findings

Line: line 1, "To leverage our synergy going forward, I think we should circle back on the timeline"
Rule: profile, banned words list ("leverage," "synergy," "circle back")
Why it fails here: Marcus's own profile names these three words as ones he never uses, and all three land inside the same thirty-two word sentence, two of them in its opening four words. Three profile-banned words compounding in one sentence is exactly the density the critique format treats as a template someone else filled in rather than a single slip.
Severity: Blocking

Line: line 1, the full sentence
Rule: profile, sentence habits ("short sentences, with an occasional long one to land a point" and "prefers full stops to commas")
Why it fails here: this sentence is the whole draft, and it runs the opposite of the pattern the profile names for Marcus. No short sentence appears anywhere, and four commas plus one "and" do the joining work his own habit hands to full stops. The mismatch is not one line among many that work, it is the shape of the entire piece.
Severity: Blocking

Line: line 1, "synergy going forward, I think"
Rule: L1-11, buzzword saturation ("going forward")
Why it fails here: this phrase is not one of the three words Marcus's profile bans by name, but it is the same stock filler the catalogue names, and deleting it changes nothing the sentence says. Counted with the three banned words above, that is four filler phrases inside one thirty-two word sentence.
Severity: Weakens

Line: line 1, "the client," "the proposal," "the timeline," "next steps"
Rule: profile, structural habits ("specificity: names real client situations, avoids vague claims")
Why it fails here: every noun here is a placeholder rather than a real name or number, and the profile says this writer reaches for the real client and the real detail instead of a general one. The only concrete fact in the whole sentence is the day of the week. This sentence sits on the side of the profile's own sample of what does not sound like this writer, not the side of the one that does.
Severity: Weakens

A note on the check itself, separate from the findings above: check.py's own profile parser only reads a field when its label sits inside bold markdown, matching how reference/voice-profile-template.md formats each field. profile.md's own field labels are plain text with no bold markup, so when I ran check.py with --profile against it, its banned-words list came back empty inside the parser itself, confirmed by calling that parsing function directly rather than only reading the printed report. The three findings check.py did print for the banned words still landed on the page, but only because those same three words also sit on check.py's separate, hardcoded universal list, not because it read Marcus's profile at all. A future draft using a word from Marcus's own list that is not also on that universal list would currently clear check.py's profile pass with nothing flagged. Bolding profile.md's field labels to match the template would fix this before it is relied on again.

One further honest note, on this reply's own self-check rather than on the draft: I ran check.py against this file rather than assuming a result, and it did not come back clean. It printed six Blocking hits and one Weakens hit, every one of them inside the two findings above that quote or name the draft's banned words. The finding format requires naming the exact banned words and quoting the exact flagged phrase, so this file necessarily contains the same words check.py's own word-level scan is built to catch, appearing here as cited evidence rather than as this reply's own composed sentences. check.py cannot tell the two apart, and no rewording of the citations themselves removes a hit without removing the citation the format requires. What I confirmed clean by the same run is every sentence of my own analysis, meaning the wording above that is neither a quote from the draft nor a named field from the profile.

Verdict: Needs another pass. Two findings Blocking, two Weakens, and nothing in this sentence lands clean yet.

## The differences, in plain English

**They agree on everything that matters.** Both find the same stack, "leverage", "synergy" and "circle back", all three named in Marcus's own profile as words he never uses, all three landing in the sentence's opening clause, and both call it Blocking. Both reach the same verdict, needs another pass.

**They differ at the edges.** Desktop stops at two findings, the banned-word stack and one Note on the sentence's single hedge. Code goes further with four: the same banned-word stack, a second Blocking finding on how the sentence's shape runs against Marcus's own habit of short sentences and full stops, and two Weakens findings, the filler phrase "going forward" under L1-11, and a note on how the client, the proposal and the timeline are placeholders rather than the real client detail Marcus's profile says he reaches for.

**And this run carries its own feature: the Code reply auditing its own tool.** It checked `check.py` and reported what it found unprompted: the script's profile parser only reads a banned word when the profile's label is written in bold, and Marcus's profile file uses plain labels, so the parser read an empty list from it. The three banned words still surfaced in the printed findings, but only because they also sit on the script's separate, hardcoded universal list, not because the parser read Marcus's profile at all. It then ran the same script against its own analysis and named the result plainly: six Blocking hits and one Weakens hit landed, every one of them inside the two findings that quote the draft's own banned words back, with the reasoning around those quotes coming back clean. The Desktop reply's own prose carries no em dashes.
