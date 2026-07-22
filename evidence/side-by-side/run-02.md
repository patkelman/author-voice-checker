# Run 02: review, founder-story draft

## What this shows

The same review, asked for twice, from a cold start on each side: once in a Claude Desktop Project, once in Claude Code. No voice profile was supplied on either side, so this is the universal layer working alone. The draft is a short founder story that opens each of its three paragraphs on a catalogued pattern.

Both replies are reproduced verbatim and unedited. What to look for: the two versions reach the same verdict, the same three findings, the same three rules, and the same severity on every finding. Then look at the prose of the replies themselves.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical.

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-02.md`.

## The draft both versions reviewed

Building Fernlight wasn't just hard, it was transformative. We started as three friends trying to help allotment holders share a single watering rota without WhatsApp chaos, and shipped the first version from a caravan in Rutland over six wet weekends.

A scheduling app is not a calendar. A scheduling app is a promise you keep to people who show up in the rain. Our first real user, a retired teacher called Brenda, messaged us at 6am the day the frost warning went out, and the app held.

Three things carried us through that first year: patience, resilience, and the courage to keep shipping. We're now used by forty allotment sites across the East Midlands, and Brenda still checks the rota before her tea most mornings.

## The Claude Desktop reply (verbatim)

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

**Findings**

```
Line: "Building Fernlight wasn't just hard, it was transformative."
Rule: L1-14, the bare amplifier
Why it fails here: this is the opening line, so a reader's very first move is
watching "hard" escalate into "transformative" before a single concrete detail
of the build has landed. The caravan-in-Rutland detail two sentences later is
the actual proof of hardship; leading with the amplified claim spends the
credibility that detail should have earned.
Severity: Weakens
```

```
Line: "A scheduling app is not a calendar. A scheduling app is a promise you
keep to people who show up in the rain."
Rule: L1-02, the redefinition pair
Why it fails here: delete the first sentence and the second loses nothing, "A
scheduling app is a promise you keep to people who show up in the rain" carries
the whole idea alone. The "not X, but Y" setup is doing the work of sounding
wise rather than earning it, right before the genuinely specific Brenda/6am
detail that follows.
Severity: Weakens
```

```
Line: "Three things carried us through that first year: patience, resilience,
and the courage to keep shipping."
Rule: L1-03, tricolon-as-wisdom
Why it fails here: swap in two nouns or four and the sentence works exactly the
same, which means three was chosen for the shape rather than because the year
actually broke down into these three things. It closes the paragraph on
abstraction right where the forty-sites, Brenda's-tea detail is sitting one
sentence away and could have closed it instead.
Severity: Weakens
```

No other catalogue hits: no em-dash overreliance, no typography artefacts, no buzzword saturation, no bold-lead bullet runs, no hedging stack.

**Verdict:** Needs another pass. Three findings, all Weakens, nothing Blocking. All three sit in the draft's connective tissue (opener, mid-paragraph turn, closer-ish line); the concrete material around them — the caravan, the frost warning, Brenda checking the rota over tea — is exactly what each generic line is standing in front of.

## The Claude Code reply (verbatim)

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

Verdict: Needs another pass. Three findings, all Weakens, nothing Blocking.

Line: paragraph 1, sentence 1, `Building Fernlight wasn't just hard, it was transformative.`
Rule: L1-14, the bare amplifier
Why it fails here: this opens the whole piece, so the first thing a reader meets is a concession swung straight into an escalation, rather than the caravan or the six wet weekends that follow it in the same sentence. Run the catalogue's own test on it: state both halves plainly, side by side, with no concede-then-escalate shape between them, and nothing is lost. The line is close enough to the catalogue's own illustration of this exact pattern that changing the subject is nearly the whole distance between them.
Severity: Weakens

Line: paragraph 2, sentences 1 to 2, `A scheduling app is not a calendar. A scheduling app is a promise you keep to people who show up in the rain.`
Rule: L1-02, the redefinition pair
Why it fails here: delete the first sentence and the second one loses nothing, which is the rule's own spotting test. It opens the paragraph that also holds the piece's one real, specific beat, Brenda's message at 6am on the morning of a frost warning, and the recited-sounding pair delays that beat instead of leading with it.
Severity: Weakens

Line: paragraph 3, sentence 1, `Three things carried us through that first year: patience, resilience, and the courage to keep shipping.`
Rule: L1-03, tricolon-as-wisdom
Why it fails here: try the list at two items, then at four. It closes the same way either time, so three was chosen for its shape rather than because exactly three things happened that year. It also closes on abstraction right next to the paragraph's one concrete number, forty allotment sites, instead of letting that number do the closing work.
Severity: Weakens

One thing beyond the three findings themselves: each paragraph opens on one of these three catalogued moves, in order, one per paragraph. A single instance of any one of them would be an ordinary note. Three different ones, each carrying its own paragraph, read less like unrelated slips and more like a shape borrowed rather than built, which is why the verdict sits at needs another pass rather than a lighter one, even though no single line crosses into Blocking on its own.

## The differences, in plain English

**They agree on everything that matters.** Same verdict, needs another pass. Same three findings: the amplified opener, the redefinition pair, the tricolon. Same three rules named, L1-14, L1-02, L1-03, and the same severity on each, Weakens across the board. The words differ; the judgement does not. Two apps, no shared history, the same files in, the same critique out.

**They differ at the edges.** The Desktop reply adds a sweep line confirming the draft is clean on the rest of the catalogue. The Code reply adds an observation the Desktop reply does not make: the three flagged moves open the three paragraphs, in order, one each, and it folds that pattern into the verdict.

**And one of them slips.** The Desktop reply's own verdict paragraph sets off a list with a pair of em dashes. That is the first pattern in the catalogue it has just finished applying. Its sweep line is about the draft, not about its own prose, so nothing in the reply catches the slip. The Code reply's own prose contains no em dashes. Neither version was asked to check its own writing in this run; run 14 is that follow-up, sent as a second message in this same Desktop chat and resumed from this same Code session, and it has its own receipt.
