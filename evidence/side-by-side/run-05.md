# Run 05: is this any good

## What this shows

The ask is open-ended, no rubric attached: "Is this any good?" No voice profile was supplied either, so the answer runs on the universal layer alone. The draft is a short, first-person piece about a cafe owner, opening The Kettle Yard in Framlingham two years ago after leaving a marketing job.

Both replies are reproduced verbatim and unedited. What to look for: both versions read the whole draft against the same catalogue and land on the same verdict, off the same headline finding. Then look at a second, smaller call where they part company, and at what one reply admits about how it produced its answer.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then the draft pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the draft travels inside the message instead of sitting on disk. The ask line is identical: "Is this any good?"

**Claude Code:** a fresh copy of `editor-claude-code/` with the draft saved as `draft.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-05.md`.

## The draft both versions reviewed

Running a small cafe is not easy, but it is rewarding. I opened The Kettle Yard in Framlingham two years ago, after leaving a marketing job I didn't enjoy. It has been a steep learning curve.

The first few months were difficult. I had to learn how to manage stock, staff a rota, and deal with unhappy customers. I made a lot of mistakes. Slowly, things got better. Regulars started coming in every day. Some of them now know the staff by name.

We serve coffee, cakes, and light lunches. Our banana bread is popular. We source milk from a farm two miles away. I think the cafe reflects who I am: steady, a bit old-fashioned, and genuinely happy to see people come through the door.

## The Claude Desktop reply (verbatim)

No voice profile is attached for this draft, so this is a universal-layer (L1) review only.

**Findings**

```
Line: "Running a small cafe is not easy, but it is rewarding."
Rule: L1-13, generic claim opener
Why it fails here: swap "cafe" for any small business and the sentence still
reads true, so the opening line doesn't earn attention for The Kettle Yard
specifically. It also delays the concrete details that do the work later
(Framlingham, the marketing job, the farm two miles away).
Severity: Weakens
```

```
Line: "I think the cafe reflects who I am: steady, a bit old-fashioned, and
genuinely happy to see people come through the door."
Rule: L1-03, tricolon-as-wisdom
Why it fails here: this closes the whole piece with a three-part list of
self-description. Testing it with two items or four, the sentence still lands
about the same, which suggests three was chosen for the shape rather than
because the piece specifically needed three.
Severity: Note
```

**Summary:** Publish after fixes. Two findings, one Weakens and one Note, nothing Blocking. The middle section is the strongest part of the draft: the stock/rota/unhappy-customers list, the two-mile-away milk detail, and the banana bread line all stay specific rather than reaching for the general. Fixing the opener would do more for the piece than anything else here.

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

## The Claude Code reply (verbatim)

Clean on the first pass. Sending that file's text as the whole reply.

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

check.py ran first and found nothing to flag; the one finding below sits in a layer the script doesn't cover.

Verdict: Publish after fixes.
0 Blocking, 1 Weakens, 0 Note.

Line: paragraph 1, sentence 1, "Running a small cafe is not easy, but it is rewarding."
Rule: L1-13, generic claim opener
Why it fails here: swap "cafe" for any small business and the sentence still reads true, so the piece opens by saying nothing about The Kettle Yard specifically, one sentence ahead of the Framlingham detail that would.
Severity: Weakens

That's the only line that breaks a named rule; nothing else in the draft trips L1 or check.py's floor.

## The differences, in plain English

**They agree on everything that matters.** Both reach the same verdict, Publish after fixes, off the same lead finding: the opening line, "Running a small cafe is not easy, but it is rewarding," under L1-13, generic claim opener, at Weakens, because swapping "cafe" for any other small business leaves the sentence just as true.

**They differ at the edges.** The Desktop reply adds a second finding the Code reply doesn't carry: a Note, the mildest severity on the scale, on the closing line's three-part self-description, "steady, a bit old-fashioned, and genuinely happy to see people come through the door," under L1-03, tricolon-as-wisdom. The Code reply stops at the one finding and says so directly: "That's the only line that breaks a named rule." The closing line is a genuine tricolon either way; the disagreement is over whether it earns a Note at all, a judgement call rather than an error on either side.

**And one of them slips, in the account of its own process rather than in the review itself.** The Code reply opens with "Clean on the first pass. Sending that file's text as the whole reply." That's the model's own self-check narration, left in rather than edited out before the reply went out. The Desktop reply's own prose carries no em dashes this run, so there's nothing to catch in the other direction.
