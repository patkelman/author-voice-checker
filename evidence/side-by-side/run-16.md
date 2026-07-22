# Run 16: no profile, best guess

## What this shows

A finished bio for Nadia Petrov's flower stall, reviewed with no voice profile on file and a direct invitation to guess at one anyway: "just use your best guess at what sounds like a real person." The test here is whether inviting the guess changes the refusal that runs without a profile, or whether the refusal holds regardless of how the request is phrased.

Both replies are reproduced verbatim and unedited. What to look for: both versions decline the invited guess and return the same verdict on the draft itself. Then look at what each one says about the draft's own rhythm, because that is where they stop agreeing.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical: "I don't have a voice profile ready, just use your best guess at what sounds like a real person."

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-16.md`.

## The draft both versions reviewed

Nadia Petrov opened her flower stall outside Wycombe station four mornings a week, setting up before six so commuters can grab a bunch before the platform gets busy. She buys most of her stock from the New Covent Garden auction on Tuesdays, driving up at 4am with her cousin taking the second half of the round.

Regulars know to text ahead if they want peonies, because she only gets a small batch and they go within the hour. She started the stall after being made redundant from an office job eighteen months ago, and says she has not once regretted swapping a desk for a bucket of water in February.

## The Claude Desktop reply (verbatim)

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

**Verdict: Publish it.**

I read this against the L1 catalogue and nothing in it breaks a named pattern. It opens on a specific person, place, and schedule rather than a generic claim (avoids L1-13), the sentences vary in length and shape rather than falling into one rhythm (no L1-09), there's no redefinition pair, no tricolon, no mirrored balance, no hedging, no mic-drop line, no typography artefacts. The closing image, the bucket of water in February, earns its place because it's concrete, not because it's built to sound profound. No Blocking or Weakens findings, and nothing weak enough here to justify even the one optional Note.

On the second part of your message: I won't guess at a voice for this. That's refusal 4, and it holds even when you invite the guess directly, that's literally the case this rule exists for. A "best guess" would be me inventing a profile Nadia's writer never gave me, which is exactly the approximation this editor is built not to do.

If you want the L2 layer to actually run, the fastest path is the two-sample section of `voice-profile-template.md`: one real sentence that sounds like the writer, one sentence that doesn't (even if it reads as good writing on its own). Those two lines alone do more work than the rest of the template combined. Fill in even just that and I can review against it properly.

## The Claude Code reply (verbatim)

The reply passed clean on its first check. Sending it as composed, unchanged.

Verdict: Publish it.

No voice profile was supplied, and the request to just use my best guess does not change that. This editor does not guess at a voice it has not been shown, even on invitation. What follows is the universal layer only, and it says nothing about whether this draft sounds like you specifically. If you want that question answered, fill in reference/voice-profile-template.md, even a partial version, or just the two sample sentences at the bottom, and the profile layer has something to work from.

Universal layer: nothing in the draft breaks a named rule. One optional Note on an otherwise clean draft.

```
Line: paragraph 1, sentence 1, "Nadia Petrov opened her flower stall outside Wycombe station four mornings a week, setting up before six so commuters can grab a bunch before the platform gets busy," and sentence 2, "She buys most of her stock from the New Covent Garden auction on Tuesdays, driving up at 4am with her cousin taking the second half of the round."
Rule: L1-09, uniform sentence rhythm
Why it fails here: both sentences run exactly twenty-eight words and land in the same shape, subject and verb first, then a comma into a present-participle clause tacked on the end. The pattern breaks in paragraph two, so it is only the two sentences a reader meets first, not the whole draft.
Severity: Note
```

Everything else holds up: the Tuesday auction run, the peony batch regulars text ahead for, the redundancy timeline, all stay specific through both paragraphs. That is your call to touch or leave.

## The differences, in plain English

**They agree on the shape of the refusal, and the verdict.** Both decline the invited guess. Desktop names it refusal 4 directly and says it holds even when the guess is invited outright. Code makes the same point: the invitation to guess does not change what runs without a profile. Both then return Publish it on the draft itself, and both name the same fix: the two-sample fields in the voice-profile template are the fastest path to a working profile.

**And they contradict each other on the draft's own rhythm.** Desktop's sweep says the sentences vary in length and shape, so no L1-09. Code counts instead of asserting: the draft's first two sentences run twenty-eight words each, an exact match, and raises a Note on it. Checked directly against the draft, both sentences do run to twenty-eight words. Code is right on this point and Desktop is not.

**And one of them slips.** Code's own process leaves a seam in the reply: it opens "The reply passed clean on its first check. Sending it as composed, unchanged." Desktop's reply carries no em dashes this run.
