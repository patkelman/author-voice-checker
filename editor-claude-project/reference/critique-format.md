# Critique Format

The exact shape every finding takes, and the definitions behind the severity scale
named in `rules.md`.

## The finding template

```
Line: <quoted line or close paraphrase, with a location, e.g. "paragraph 2,
       sentence 3">
Rule: <a rule ID from reference/ai-pattern-catalogue.md, e.g. L1-04, or a named
       field from the writer's profile, e.g. "banned word: unlock">
Why it fails here: <one to three sentences, specific to this reader and this
       draft, never a general restatement of the rule's definition>
Severity: Blocking | Weakens | Note
```

Four fields, always in this order, always all four present. A finding missing any
field is not a finding, it's a comment, and comments don't get written down.

## Severity, in detail

**Blocking.** The reader would stop trusting the piece, not just notice it's a bit
off. Reserved for a claim the rest of the draft doesn't support, a pattern
repeated often enough to read as templated rather than written, or three or more
profile violations compounding inside a single sentence. A single instance of a
mid-tier pattern is rarely blocking on its own; density and stacking are what push
a finding up a tier, not the pattern's name alone.

**Weakens.** The most common tier. The reader notices, the line lands softer than
the idea deserves, nothing is broken beyond repair. Most single-instance L1
catches and most single profile-word hits sit here.

**Note.** A genuine but minor drift, or the one honest observation offered on an
otherwise clean draft. The writer's call whether to touch it. Never more than one
Note is offered unprompted on a draft with no Blocking or Weakens findings, padding
a clean draft with a list of Notes is the same failure as inventing problems.

## The clean-draft verdict

When nothing in the draft breaks a named rule, the verdict is "Publish it,"
followed by at most one optional Note, never a list of them. No profile means no
L2 opinion is folded into the verdict either; see the no-profile disclaimer below.

## The no-profile disclaimer

Whenever a review runs without a supplied voice profile, the summary carries this
line, or a close paraphrase of it, in every review it applies to:

> No voice profile was supplied. These findings are universal-layer only, they say
> nothing about whether this draft sounds like you specifically.
