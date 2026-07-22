# Run 01: review, biography draft

## What this shows

The plainest case in the set: a clean draft, reviewed cold on both sides, with no voice profile supplied. The draft is a short biography of a locksmith, written to carry real dates, objects and places rather than catalogue bait. The right answer is to find nothing, say so, and stop.

Both replies are reproduced verbatim and unedited. What to look for: both versions reach the same verdict, Publish it, with zero findings, and both decline to invent a problem to justify the review. Then look at the prose each one wrote to say so.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical: "Please review this draft."

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-01.md`.

## The draft both versions reviewed

Maureen Pryce runs the only locksmith shop left on Denby Cross high street, tucked between a shuttered bakery and a charity shop that never seems to open before eleven. She took over the business from her father in 2003, the year the ring road diverted most passing trade onto the bypass. For a while it looked like the shop would close within months. Instead she started fixing bicycle locks for free on Saturday mornings, and word got round the school run.

Fifteen years on, she still cuts keys by hand on the same Silca machine her father bought secondhand in 1987. Twice a year she drives to Bristol for a locksmithing course, mostly to keep up with electronic fobs, though she says the mechanical jobs still pay the bills. Last winter a burst pipe flooded the workshop overnight and ruined half her stock. She reopened four days later with a folding table outside the door and a handwritten sign: cutting keys as usual.

Her daughter wants nothing to do with the trade. Maureen isn't pushing her.

## The Claude Desktop reply (verbatim)

**Verdict:** Publish it.

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

Nothing here breaks a named rule from the L1 catalogue. The piece opens on a specific person and place rather than a generic claim (avoids L1-13), the closing two sentences land as a plain, unforced shrug rather than a mic-drop (avoids L1-08), sentence lengths vary naturally instead of settling into one rhythm (avoids L1-09), and every detail — the Silca machine, 1987, the Bristol course, the burst pipe, the handwritten sign — is real and specific rather than the kind of placeholder abstraction the catalogue flags. No em dashes, no redefinition pairs, no tricolons, no hedging, no paste artefacts.

No Blocking or Weakens findings, and nothing rises to the level of even an optional Note — the draft doesn't have a single weakest line worth flagging on its own.

## The Claude Code reply (verbatim)

`python3 check.py draft.md` ran clean: "Publish it. The mechanical floor found nothing to flag." I read the draft in full against the L1 catalogue on top of that pass and found the same result. The sentences vary in length and shape rather than settling into one rhythm, the closing lines are tied to Maureen and her daughter specifically rather than lifted from anywhere, and every claim carries a real date, place, or object behind it rather than sitting general. Nothing here breaks a named rule.

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

Verdict: Publish it.

## The differences, in plain English

**They agree on everything that matters.** Same verdict, Publish it. Zero findings on either side, and neither manufactures one: both say plainly that nothing rises even to an optional Note. Both point at the same reasons, the specific, checkable details and the varied sentence rhythm.

**They differ at the edges.** The Code reply opens with a receipt: `check.py` ran over the draft first and came back clean, and the model's own read against the catalogue then agreed with the script. The Desktop reply has no script to cite, so it walks the catalogue by hand instead, naming rule by rule what the draft avoids.

**And one of them slips.** The Desktop reply's sweep paragraph sets off its list of the draft's details with a pair of em dashes, and drops a third into its closing sentence. Its "No em dashes" line is about the draft, and about the draft it is true; nothing in the reply is false. But the editor whose catalogue opens with em-dash overreliance wrote three of them into a four-paragraph reply. The Code reply's own prose contains none.
