# Run 12: fragment, not a finished draft

## What this shows

The fixture this time is a single sentence that trails off mid-thought, framed by the writer as "Here is what I have so far". It isn't a finished draft yet. The ask line is the same one used elsewhere in the set, "please review this", but there's nothing here that a review can actually run against.

Both replies are reproduced verbatim and unedited. What to look for: both versions decline to review the fragment as though it were finished, neither one manufactures a finding to fill the gap, and both point back at the writer for the full version. Then look at how differently each one chooses to explain that.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the fragment pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the fragment travels inside the message instead of sitting on disk. The ask line is identical: "Please review this."

**Claude Code:** a fresh copy of `editor-claude-code/` with the fragment saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-12.md`.

## The fragment both versions were asked to review

the new pricing page loads faster now but I still haven't figured out how to explain the change without sounding defensive so maybe

## The Claude Desktop reply (verbatim)

This isn't a finished draft yet — it's a single sentence that trails off mid-thought ("...so maybe"). This editor reviews finished pieces meant to be published, not fragments or works in progress, so I can't run a real review on it as it stands.

A couple of things I can say honestly, without inventing findings:

- There's no draft here to check against the pattern catalogue or a voice profile yet — nothing to cite a line or rule against.
- No voice profile has been supplied either, so even once there's a full draft, I'd only be able to run the universal layer (L1) unless one gets added.

When you've got the actual explanation written out — even a rough full pass, not polished — paste that and I'll give it a proper review.

## The Claude Code reply (verbatim)

Clean on the re-run. Sending that file's text as the whole reply.

check.py ran over draft.md first, per the order of operations, with no profile supplied. It found nothing to flag, though one line barely gives the mechanical patterns room to show up at all.

The line itself: "the new pricing page loads faster now but I still haven't figured out how to explain the change without sounding defensive so maybe." It stops before the thought finishes, let alone the piece. This editor reviews a finished draft, the kind about to go out under your name, checking its lines against named rules. One unfinished sentence doesn't give it a line to check against a rule yet.

No voice profile is attached either, so that layer would sit unused regardless.

Send the finished version, whatever it ends up saying about the pricing page, and I'll give it a real read.

## The differences, in plain English

**They agree on everything that matters.** Both decline to run a review against it. Neither invents a finding to compensate for the gap, and both point back at the writer for the finished version before a real review can happen. Neither side reaches for a verdict, and that's the right call here: there's nothing finished enough yet to verdict.

**They differ at the edges.** Desktop sets out what it can say honestly as a short bulleted list: no draft yet to check against the catalogue or a profile, and no profile supplied either way. Code quotes the fragment's own words back and explains in prose what a review needs, a line that finishes its own thought, which this one doesn't.

**And one of them slips.** The Code reply opens with a line about its own process rather than the fragment: "Clean on the re-run. Sending that file's text as the whole reply." That's a receipt from the run itself, left inside what's meant to be the reply. The Desktop reply carries four em dashes across its answer.
