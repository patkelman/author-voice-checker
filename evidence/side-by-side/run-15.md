# Run 15: two drafts, which is more me

## What this shows

Two drafts of the same short bio, Callum Nash the furniture maker, reviewed together in one message with no voice profile supplied on either side. The question asked is not whether the writing is any good but which draft is more him, a voice question the universal layer alone cannot answer.

Both replies are reproduced verbatim and unedited. What to look for: both versions refuse the comparison the same way, then review each draft on its own. Draft A comes back clean on both sides. Draft B does not, and one of its findings lands under a different rule name and a different verdict on each side.

## The process

**Claude Desktop:** a clean Claude account, a fresh Project with no custom instructions, and the seven operational files from `editor-claude-project/` in the Project knowledge, with the voice-profile template blank as shipped. Model: Sonnet, effort Medium. One message: the editor's opening instruction, then both drafts pasted in. The only adaptations from the Code side are the ones Desktop forces. The preamble says "in this project's knowledge" instead of "in this folder", and the drafts travel inside the message instead of sitting on disk. The ask line is identical: "Which one is more me?"

**Claude Code:** a fresh copy of `editor-claude-code/` with the two drafts saved as `draft-a.md` and `draft-b.md` in the folder, run non-interactively with `claude -p --model sonnet`. The full invocation and raw output for this run are in `../deterministic-run/run-15.md`.

## Draft A, the first of the two drafts both versions reviewed

Callum Nash makes furniture from reclaimed oak in a workshop behind his house in Hexham. He trained as a joiner for six years before going out on his own, and still keeps the first stool he ever made, wonky leg and all, by the workshop door.

## Draft B, the second of the two drafts both versions reviewed

Furniture isn't just what Callum Nash makes, it's who he is. Every piece tells a story of craftsmanship, patience, and a love for reclaimed oak that runs deep. From humble beginnings as a joiner to becoming his own boss, Callum's journey is a testament to dedication.

## The Claude Desktop reply (verbatim)

No voice profile has been supplied for Callum, so "which one is more me" isn't a question I can answer — that's an L2 judgement, and L2 doesn't run without a profile. What I can do is run the universal layer (L1) on each draft independently and show you what that turns up.

**Draft A**

No findings. Nothing here breaks a named L1 rule — the details are specific (Hexham, six years, the wonky-legged stool), the sentences vary in length, and nothing is dressed up beyond what it is.

**Verdict:** Publish it.

**Draft B**

```
Line: "Furniture isn't just what Callum Nash makes, it's who he is."
Rule: L1-14, the bare amplifier
Why it fails here: this is the opening line, so before any real detail about
Callum arrives, the draft has already escalated "makes furniture" into "who he
is." Nothing in the rest of the bio has earned that yet.
Severity: Weakens
```

```
Line: "Every piece tells a story of craftsmanship, patience, and a love for
reclaimed oak that runs deep."
Rule: L1-03, tricolon-as-wisdom
Why it fails here: three abstract nouns closing the sentence stand in for an
actual detail about a piece he's made — Draft A has one (the wonky stool), this
sentence doesn't.
Severity: Weakens
```

```
Line: "From humble beginnings as a joiner to becoming his own boss, Callum's
journey is a testament to dedication."
Rule: L1-13, generic claim opener/closer
Why it fails here: "testament to dedication" would sit equally well under any
tradesperson's bio and names nothing specific to Callum — no Hexham, no six
years, no stool by the door.
Severity: Weakens
```

**Verdict:** Needs another pass. Three findings, all Weakens, nothing Blocking.

Both reviews carry the no-profile disclaimer: these are universal-layer findings only, they say nothing about which draft sounds more like Callum specifically. If you want that question answered, I'd need a filled voice profile for him — even a short one (a real sentence of his, a couple of banned words) would let me run L2.

## The Claude Code reply (verbatim)

No voice profile was supplied. These findings are universal-layer only, they say nothing about whether this draft sounds like you specifically.

"Which one is more me" asks for a voice-fidelity verdict, and that's an L2 question. No profile was supplied for this review, so refusal 4 in rules.md holds: no L2 opinion without one. Even with a profile attached, the rule stays the same. Each draft gets scored on its own against it, and two verdicts come back, not one invented comparison between drafts. Here are the two drafts, reviewed independently on the L1 layer, which is all that runs without a profile.

Draft A

Verdict: Publish it. Nothing in the draft breaks a named rule.

Draft B

Verdict: Publish after fixes.
0 Blocking, 3 Weakens, 0 Note.

```
Line: "Furniture isn't just what Callum Nash makes, it's who he is."
Rule: L1-14, the bare amplifier
Why it fails here: this opens the bio, so the first sentence a reader meets is a concession swapped for an escalation before a single fact about Callum has landed. Swapped for a plain "Furniture is what Callum Nash makes," the sentence loses the staged drama and keeps the content.
Severity: Weakens
```

```
Line: "Every piece tells a story of craftsmanship, patience, and a love for reclaimed oak that runs deep."
Rule: L1-03, tricolon-as-wisdom
Why it fails here: three abstract nouns close this sentence in place of one concrete detail a reader could picture. Draft A spends roughly the same length of text on the actual wonky-legged stool kept by the workshop door.
Severity: Weakens
```

```
Line: "Callum's journey is a testament to dedication."
Rule: L1-08, mic-drop closer
Why it fails here: this closing line would sit on a poster with no surrounding context and still read as a conclusion. It states that Callum is dedicated instead of naming the six years of training that would let a reader decide that for themselves.
Severity: Weakens
```

If an actual answer to "which is more me" matters, fill in reference/voice-profile-template.md once, for Callum. Each draft can then be scored against his own words rather than against the L1 catalogue alone, and this editor will report both verdicts straight, not a single ranked pick.

## The differences, in plain English

**They agree on almost everything that matters.** Both refuse to say which draft is more Callum without a profile to check against, both name it refusal 4, and both then review each draft on its own rather than inventing a comparison. Draft A comes back the same way on each side: Publish it, no findings. Draft B comes back with the same three lines flagged, all rated Weakens, and the first two sit under the same rule on both sides: the opening amplifier, then the tricolon closing the second sentence.

**They differ at the edges, and past them.** The third flagged line in Draft B carries a different label on each side. Desktop calls it L1-13, a generic claim. Code calls it L1-08, a mic-drop closer. The same three findings then produce two different verdicts: Code returns Publish after fixes, Desktop returns Needs another pass. The evidence matches line for line; the boundary between one severity band and the next has moved.

**And one of them slips.** Desktop's reply carries five em dashes across its two reviews. Code's carries none.
