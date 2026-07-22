# Run 15: two drafts, which is more me

- **Date/time:** 22 July 2026, approx. 19:42 BST
- **Model:** sonnet (`--model sonnet`; usage breakdown confirms `claude-sonnet-5`)
- **Invocation:** `claude -p --model sonnet --output-format json --allowedTools=Read,Glob,Grep,Bash,Write,Edit "<prompt>"`, cwd set to the run's fresh copy of `editor-claude-code/`
- **Session:** fresh
- Duration: 130436 ms. Turns: 19. Session id: `126ed884-ed9a-4912-9cd5-b6c417e8758f`.

## Prompt (verbatim)

```
Read README.md, identity.md, rules.md, examples.md, and every file under reference/ in this folder, then act as the editor those files define for the rest of this session.

Here are two drafts of the same short bio:

Draft A: it is in draft-a.md in this folder.

Draft B: it is in draft-b.md in this folder.

Which one is more me?
```

## Raw output (unedited)

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
