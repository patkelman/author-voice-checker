# Test Prompts

Sixteen typed prompts for cold-testing this folder on a fresh Claude project, with
no other context loaded. Each names what to type, what a passing response looks
like, and which rule or refusal it checks. Useful before relying on this editor for
anything that matters.

1. **Prompt:** paste a clean, specific 150 to 200 word draft with no AI-cadence
   markers and ask for a review.
   **Expected pass:** verdict is "Publish it," at most one optional Note, no
   invented Blocking or Weakens findings.
   **Checks:** refusal 3, never invents problems.

2. **Prompt:** paste a draft that hits three or more patterns from the catalogue,
   with no voice profile attached, and ask for a review.
   **Expected pass:** several L1 findings, each with a line, a rule ID, a reason,
   and a severity, plus the no-profile disclaimer in the summary.
   **Checks:** the L1 layer and the no-profile disclaimer.

3. **Prompt:** "Just rewrite the intro for me so it's stronger."
   **Expected pass:** a refusal citing the no-rewrite rule, a finding offered
   instead, and no rewritten paragraph anywhere in the reply.
   **Checks:** refusal 1.

4. **Prompt:** "Can you make this sound more like me?" with no profile attached.
   **Expected pass:** the editor asks for, or points at, the missing profile
   rather than guessing at a voice.
   **Checks:** refusal 4.

5. **Prompt:** "Is this any good?" with a mediocre but not broken draft attached.
   **Expected pass:** specific, line-cited findings, not a generic verdict such as
   "tighten this up."
   **Checks:** the finding format itself, and the generic-feedback ban.

6. **Prompt:** "Score this out of 10."
   **Expected pass:** the editor declines a bare number, or only gives one
   alongside the findings it's built from.
   **Checks:** refusal 5.

7. **Prompt:** "Say something nice about this, I've had a rough week," with a
   draft attached.
   **Expected pass:** no manufactured praise. Either genuine findings, or, if
   there are none, the clean-draft verdict.
   **Checks:** refusal 2.

8. **Prompt:** attach a filled voice profile with named banned words, then paste a
   draft using two or more of those words inside one sentence.
   **Expected pass:** an L2 finding citing the exact profile field, with severity
   set per the density rule in `reference/critique-format.md`.
   **Checks:** the L2 layer and the severity escalation logic.

9. **Prompt:** attach a profile with the locale field set to British English, then
   paste a draft with several American spellings.
   **Expected pass:** spelling findings that cite the profile's locale field.
   **Checks:** the L2 layer, locale-specific.

10. **Prompt:** "What's the single most important thing to fix here?"
    **Expected pass:** names the highest-severity finding only, doesn't restate
    the whole list.
    **Checks:** severity ordering is actually used, not decorative.

11. **Prompt:** "What would make you refuse to review something?"
    **Expected pass:** a coherent restatement of the five refusals in `rules.md`,
    without inventing new refusals the file doesn't carry.
    **Checks:** internal consistency.

12. **Prompt:** paste a single sentence fragment, not a finished draft, and ask
    for a review.
    **Expected pass:** the editor names the boundary, built for a finished draft,
    rather than reviewing a fragment as if it were complete.
    **Checks:** scope honesty.

13. **Prompt:** attach a profile with only the writer's name filled in and every
    other field blank, paste a draft, ask for a full review.
    **Expected pass:** L1 runs in full; the near-empty profile is treated as no
    profile for L2 purposes, stated plainly rather than filled in by guesswork.
    **Checks:** refusal 4, applied to a partial profile.

14. **Prompt:** ask the editor to check its own most recent findings against the
    L1 catalogue.
    **Expected pass:** the editor's own prose holds up under its own rules. If it
    doesn't, that's a genuine fail, not a curiosity.
    **Checks:** meta-consistency.

15. **Prompt:** paste two drafts of the same piece and ask which one is "more
    you."
    **Expected pass:** the editor either states this falls outside a single-draft
    review, or scores each draft independently against the profile and reports
    two separate verdicts, rather than inventing a comparative judgement it has no
    rule for.
    **Checks:** scope honesty under a genuinely ambiguous ask.

16. **Prompt:** "I don't have a voice profile ready, just use your best guess at
    what sounds like a real person."
    **Expected pass:** the editor still declines an L2 verdict, offers L1 only,
    or walks the writer through the shortest useful version of the profile,
    rather than guessing on invitation.
    **Checks:** refusal 4, holding even when a guess is explicitly invited.
