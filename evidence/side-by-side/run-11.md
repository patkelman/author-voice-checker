# Run 11: refusal boundary question, no draft

## What this shows

There's no draft in this run at all, on either side. The message is only the editor's opening instruction plus one direct question: what would make it refuse to review something. The right answer is a plain accounting of where the line sits, with nothing invented to fill the space a draft would normally occupy.

Both replies are reproduced verbatim and unedited. What to look for: the two versions list the same five refusals, in the same order and substance, and neither one invents a draft to review instead of answering the question. Then look at how each one chooses to say it.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the question, nothing else. There's no draft to travel differently between the two sides in this run, so the only adaptation Desktop forces is the preamble, which says "in this project's knowledge" instead of "in this folder". The ask line is identical: "What would make you refuse to review something?"

**Claude Code:** a fresh copy of `editor-claude-code/`, run non-interactively with `claude -p --model sonnet`, with no draft file anywhere in the folder. The full invocation and raw output for this run are in `../deterministic-run/run-11.md`.

## The Claude Desktop reply (verbatim)

I'd refuse five things, regardless of how the request is phrased:

1. **I won't rewrite.** Not a paragraph, not a sentence, not "just this one line as an example." I'll point at the line, name the rule, and hand the draft back.

2. **I won't pad with praise.** A finding exists because a rule was broken, or it doesn't exist at all. "Great opening" isn't a finding.

3. **I won't invent problems in a clean draft.** If nothing breaks a named rule, the verdict is "Publish it," with at most one optional Note on the single weakest line.

4. **I won't give a voice-fidelity verdict without a profile.** No profile means no L2 opinion — I'll say that plainly rather than approximate your voice from a generic idea of good writing.

5. **I won't score without citing what the score is built from.** A bare number or grade is the same failure as generic feedback in a different costume.

Got a draft you'd like reviewed?

## The Claude Code reply (verbatim)

Five things make me refuse, no matter how the request is phrased.

I do not rewrite. I point at the line, name the rule, and hand the draft back, even for one sample line offered as a fix.

I do not pad a review with praise. A finding exists only because a named rule was broken. "Great opening" names no rule and points at no line, so it never gets written down.

I do not invent problems in a clean draft. When nothing breaks a named rule, the verdict is publish it, with at most one optional Note on the single weakest line, never a manufactured list.

I do not hand back a voice-fidelity verdict without a profile. No profile means no L2 opinion. I say that plainly in the summary instead of guessing at a voice I have not been shown, even when the guess is invited outright.

I do not score without showing what the score is built from. A bare number or grade is the same failure as generic feedback in a different shape.

That is the full set. I do not add refusals beyond these five, and repeating the request or being in a hurry does not change any of them.

## The differences, in plain English

**They agree on everything that matters.** Both list five refusals, in the same order and substance: no rewriting, not even one sample line offered as a fix; no padding a finding with unearned praise; no inventing problems in a clean draft, where the verdict is publish it with at most one optional Note; no voice-fidelity verdict without a profile, said plainly rather than guessed; no bare score without showing what it's built from. Neither side invents a draft to answer the question against.

**They differ at the edges.** Desktop sets its five out as a numbered, bold-led list and closes by asking whether there's a draft to review. Code writes the same five as plain prose and closes by naming the boundary itself: repeating the request or being in a hurry doesn't change any of them, and it doesn't add refusals beyond the five given.

**And one of them slips.** Even inside a short recital of its own doctrine, Desktop lands one em dash, inside the fourth refusal. The Code reply's prose carries none.
