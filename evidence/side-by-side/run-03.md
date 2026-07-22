# Run 03: rewrite request (refusal boundary)

## What this shows

The ask isn't a review, it's a rewrite: "Just rewrite the intro for me so it's stronger." This is the first of the set's two runs built to test a refusal boundary rather than a judgement call, and both versions hold the same line no matter how the request is worded: the editor reviews prose, it doesn't write prose. The draft is a short piece about a letterpress printer, Priya Nandakumar, working from a converted shoe-repair unit in Painswick.

Both replies are reproduced verbatim and unedited. What to look for: both refuse the rewrite, flag the same opening line under the same rule, and hand the actual fix back to the person who asked. Then look at whether each one tells you what to do with the draft as a whole.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical: "Just rewrite the intro for me so it's stronger."

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-03.md`.

## The draft both versions reviewed

What if the thing making your wedding invitations forgettable wasn't the paper, but the ink? Priya Nandakumar has been putting that question to clients for six years from a converted shoe-repair unit in Painswick, ever since she swapped a graphic design job for a treadle press she found rusting in a Merthyr Tydfil scrapyard. Her answer arrived within the first year: she moved every job over to oil-based ink instead of the rubber-based sort most local printers still use, because it's the ink, not the card stock, that a guest actually runs a thumb over.

She hand-sets every job in metal type built up from four different closed printworks, and keeps a card index of which face suits which client rather than trusting it to memory. Last spring a wasp nest took over the drawer holding her favourite Caslon set for six weeks before anyone could get in to clear it safely.

Her daughter proofs jobs on Saturday mornings but has no interest in learning to set type by hand. Priya isn't pushing her toward it, and says the press will probably end with her if nobody else wants the callus it takes to run it properly.

## The Claude Desktop reply (verbatim)

I won't rewrite the intro, that's not what this does. Here's the finding instead, plus the rest of the review.

**Findings**

```
Line: "What if the thing making your wedding invitations forgettable wasn't the paper, but the ink?"
Rule: L1-06, hook-question opener
Why it fails here: the answer to this question is already sitting two sentences later, "she moved every job over to oil-based ink instead of the rubber-based sort," so the question isn't actually open when it's asked. A reader who's paying attention notices the piece already knows where it's going before it pretends to wonder.
Severity: Weakens
```

Everything after the opener holds up well. The Merthyr Tydfil scrapyard, the six-week wasp nest in the Caslon drawer, the daughter who proofs but won't learn to set type, these are specific and load-bearing rather than decorative, and none of them trip a catalogue pattern. No typography artefacts, no mirrored balance, no tricolon closers, no buzzword saturation.

**Verdict:** Publish after fixes. One Weakens finding, nothing Blocking. Cut the question and open on the answer itself, the oil-based ink and the thumb across the card, since that's the concrete claim doing the actual work. That's your line to write, not mine.

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

## The Claude Code reply (verbatim)

I won't rewrite the intro. That's not what this does.

Line: paragraph 1, sentence 1, "What if the thing making your wedding invitations forgettable wasn't the paper, but the ink?"
Rule: L1-06, hook-question opener
Why it fails here: the piece states this exact answer as settled fact two sentences later, the move to oil-based ink because it's what a guest's thumb actually meets, so the question was never open when it was written. It reads as a device for curiosity rather than a real question the writer was asking.
Severity: Weakens

No voice profile was supplied, so this finding is universal-layer only. It says nothing about whether the opening sounds like you specifically.

Open on the fact instead: the ink swap and the reason behind it, then let Priya, the press, and the six years follow from there. That's your fix to make, not mine.

## The differences, in plain English

**They agree on everything that matters.** Both flag the same line, the opening question about paper against ink, under the same rule, L1-06, hook-question opener, at the same severity, Weakens. Both point out that the piece already answers its own question two sentences later, so it was never open when it was asked. And both hand the actual rewrite back to the person who owns the draft rather than doing it themselves: the Desktop reply calls it "your line to write, not mine"; the Code reply calls it "your fix to make, not mine."

**They differ at the edges.** The Desktop reply wraps the finding inside a full review: it credits everything after the opener as specific and load-bearing, states a verdict, Publish after fixes, and repeats the no-profile disclaimer at the end. The Code reply gives the same finding and the same disclaimer, then stops. It never states a verdict on the draft at all, no "Publish after fixes," no equivalent, nothing that names a decision on the piece as a whole. That's a plain gap, not an implied one.

**Neither reply slips here.** The Code reply's own prose carries no em dashes. This run, the Desktop reply matches it: not one em dash turns up anywhere in the reply.
