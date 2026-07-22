# Comparison with a live example

## The Post

I created a real post for Pat's Film Club, recommending a "Film of the Day" that can be watched on free-to-air TV in the UK.

The post:

🎬 Pat's Pick of the Day: The Mouse That Roared (1959) ✨
Film4 | Thursday 23rd July | 1.10pm

Have you ever wondered what happens when the smallest country in the world declares war on the most powerful nation on Earth, and wins? Let that sink in.

I was just a kid, sitting at home during the school holidays, when I first discovered this hidden gem, and honestly? It changed everything. This isn't just a comedy. It's a timeless, cinematic masterpiece that continues to resonate in today's fast-paced world, and one of my all-time favorite films.

The premise is deceptively simple, yet endlessly clever. The Duchy of Grand Fenwick, a tiny, bankrupt nation, hatches an audacious plan: declare war on the United States, lose spectacularly, and reap the rewards of American aid. But here's the thing: their medieval army, armed with nothing but bows and arrows, accidentally wins. Remarkably, it's both hilarious and profound, a film brimming with warmth and humor.

Peter Sellers delivers a truly unforgettable, iconic performance, not one role but three, years before he would delve into the same trick in the legendary Dr. Strangelove. It's a masterclass in comedic genius. A testament to his extraordinary range.

I always thought of it as an Ealing comedy, and while it's technically not, it captures that spirit perfectly: the little guy triumphing over the powerful, innocence meeting intelligence in a rich tapestry of wit and wonder. Watch it and you'll quickly realize they simply don't make them like this anymore.

I haven't seen it in years, so I'll definitely be watching it myself tomorrow. And trust me, you won't want to miss this one.

At the end of the day, some films don't just entertain. They remind us who we are. 🍿

#FilmOfTheDay #ClassicCinema #PeterSellers #MustWatch #PatsFilmClub

## The Process

I then ran it through both versions of the Author Voice Checker. Both had a version of the Pat voice profile that I use daily in my second brain. I dropped it into the reference/ folder replacing the generic profile that ships with the editor. That filled profile ships in this repo as `voice-profile-pat-kelman.md`, next to this file, so you can read what both versions were checking against.

### The Claude Desktop version

The Claude Desktop instance was a clean new Claude account with no instructions of any kind in the settings.

I copied the operational files into a new Claude Project, then ran the flow in a chat.

The Prompt was simply: "Give me a critique of this text", with the post copy pasted in after it

#### The Claude Desktop Project result:

No voice profile disclaimer doesn't apply here — Pat's profile is in scope, so both layers ran.

**Verdict: Needs another pass.** Two Blocking findings, several Weakens.

---

```
Line: "Have you ever wondered what happens when the smallest country in the world
declares war on the most powerful nation on Earth, and wins? Let that sink in."
Rule: L1-06, hook-question opener (also violates the profile's stated openers
field: "Never a hook question, never a thesis statement up top.")
Why it fails here: this is the first thing a reader sees, and Pat's own profile
says he opens on an image, a place, a film, a name, or straight into the point,
never a manufactured question. "Let that sink in" doubles down on the same
manufactured-suspense move.
Severity: Weakens
```

```
Line: "This isn't just a comedy. It's a timeless, cinematic masterpiece that
continues to resonate in today's fast-paced world, and one of my all-time
favorite films."
Rule: L1-14, the bare amplifier
Why it fails here: "isn't just X, it's Y" turns up the volume rather than saying
anything specific about this film, and it arrives before a single concrete
detail about the plot or Sellers has been given.
Severity: Weakens
```

```
Line: "it's both hilarious and profound"
Rule: profile, banned word "profound"
Why it fails here: named directly on Pat's never-uses list, and it's doing the
same job the banned list exists to prevent, telling the reader how to feel
instead of showing it.
Severity: Weakens
```

```
Line: "one of my all-time favorite films"
Rule: profile, locale (British English)
Why it fails here: "favorite" is the American spelling against a profile that
specifies British English throughout.
Severity: Weakens
```

```
Line: "Peter Sellers delivers a truly unforgettable, iconic performance...years
before he would delve into the same trick in the legendary Dr. Strangelove. It's
a masterclass in comedic genius. A testament to his extraordinary range."
Rule: profile, the two-sample field
Why it fails here: Pat's own profile gives "a masterclass in tension, a
testament to the power of restraint" as the explicit example of writing that is
NOT his voice, and this stretch reproduces almost the same shape twice in three
sentences, "masterclass in," then "a testament to," stacked with "truly
unforgettable, iconic" and "legendary." That's several voice violations
compounding in one short stretch rather than a single slip.
Severity: Blocking
```

```
Line: "a rich tapestry of wit and wonder"
Rule: L1-11, buzzword saturation
Why it fails here: decorative alliteration standing in for a specific observation
about this film; swap it for plainer language and nothing about The Mouse That
Roared is lost.
Severity: Note
```

```
Line: "And trust me, you won't want to miss this one."
Rule: profile, register ("never slicker, never marketer-shaped")
Why it fails here: this is a sales close, not how Pat talks to people who already
trust his taste enough to show up. It asks the reader to trust him rather than
earning that with a specific reason.
Severity: Weakens
```

```
Line: paragraphs 2 through 4 generally, e.g. "The premise is deceptively simple,
yet endlessly clever" through "innocence meeting intelligence in a rich tapestry
of wit and wonder"
Rule: L1-09, uniform sentence rhythm (also profile, sentence habits: "mostly
short single-beat sentences with the occasional longer breath...never a flat,
uniform rhythm")
Why it fails here: sentence after sentence runs the same long, multi-clause
length with no short line to land a beat, which is the opposite of the varied,
slightly uneven rhythm the profile describes as this writer's habit.
Severity: Weakens
```

```
Line: "At the end of the day, some films don't just entertain. They remind us
who we are."
Rule: L1-14, the bare amplifier (repeated) / L1-08, mic-drop closer
Why it fails here: this is the same "don't just X, they Y" trick from the
opening, now closing the whole post, which reads as templated rather than
written when a reader hits it twice in one piece. It also lands as manufactured
profundity rather than a conclusion earned by anything specific said above it.
Severity: Blocking
```

---

The Sellers paragraph and the closing line are the two to fix before this goes out; both repeat patterns Pat's own profile calls out by name, and the repetition of the bare-amplifier trick at open and close is what pushes the close from a notice to a block. Cheers-and-sign-off aside, the rest is a voice problem more than a grammar one: the draft has real specificity to work with (the Duchy, the bows and arrows, Sellers playing three roles before Strangelove) and keeps reaching past it for stock intensity instead.

### The Claude Code version

I opened VS Code in a fresh Editor-Claude-Code folder.

In the terminal I started Claude, then gave it the prompt: "Here is a draft for your critique:" followed by the post text.

#### The Claude Code version Result:

Voice profile used: reference/voice-profile-pat-kelman.md. The draft's own sign-off, "Pat's Pick of the Day" and "#PatsFilmClub," matches this profile, so the full two-layer review runs.

Verdict: Needs another pass. 1 Blocking, 9 Weakens, 0 Note.

Line: "A testament to his extraordinary range." (the Peter Sellers paragraph)
Rule: profile, banned phrase "a testament to"
Why it fails here: your own profile names this exact phrase as the sample sentence that does not sound like you, and here it closes out the third generic-superlative beat in three sentences straight, after "truly unforgettable, iconic performance" and "a masterclass in comedic genius." Any of the three could describe any actor in any performance. Stacked together in one short paragraph, they read as a template dropped in, not a description of what Sellers actually does in this film.
Severity: Blocking

Line: "Have you ever wondered what happens when the smallest country in the world declares war on the most powerful nation on Earth, and wins?"
Rule: profile, never-uses "have you ever wondered"
Why it fails here: this exact opener is on your own never-uses list, and it is the first five words a reader meets.
Severity: Weakens

Line: same sentence
Rule: L1-06, hook-question opener
Why it fails here: the question already carries its own answer, "and wins," inside the same sentence, so it is not really being asked. Your profile's own note on openers rules this move out too: straight into the point, never a hook question.
Severity: Weakens

Line: "This isn't just a comedy. It's a timeless, cinematic masterpiece that continues to resonate in today's fast-paced world, and one of my all-time favorite films."
Rule: L1-04, mirrored balance
Why it fails here: the two sentences are built as an exact structural echo, concede then swing the other way, which reads as performed rather than said. It is also the second hook-shaped move within two paragraphs.
Severity: Weakens

Line: same sentence, "one of my all-time favorite films"
Rule: profile, US spelling "favorite"
Why it fails here: the profile sets British spelling; "favourite" is the form that fits.
Severity: Weakens

Line: "a timeless, cinematic masterpiece that continues to resonate in today's fast-paced world"
Rule: profile, specificity habit
Why it fails here: swap in any other well-regarded old comedy and the line still reads true, so it has not said anything about this film specifically yet. Your profile calls specificity, the real title, name, and detail, the strongest trust signal in this voice, and this line, along with "a masterclass in comedic genius" and "they simply don't make them like this anymore" further down, all reach for the generic label instead.
Severity: Weakens

Line: "Remarkably, it's both hilarious and profound, a film brimming with warmth and humor."
Rule: profile, never-uses "profound"
Why it fails here: "profound" is on your own banned list.
Severity: Weakens

Line: same sentence, "warmth and humor"
Rule: profile, US spelling "humor"
Why it fails here: the profile sets British spelling; "humour" is the form that fits.
Severity: Weakens

Line: "Watch it and you'll quickly realize they simply don't make them like this anymore."
Rule: profile, US spelling "realize"
Why it fails here: the profile sets British spelling; "realise" is the form that fits.
Severity: Weakens

Line: "At the end of the day, some films don't just entertain. They remind us who we are."
Rule: L1-08, mic-drop closer
Why it fails here: this closes the whole post, and it would sit on a poster with no film named in it at all. Nothing in the sentence is specific to Grand Fenwick, to Sellers, or to Thursday's screening.
Severity: Weakens

The draft is clean on em dashes and on paste artefacts; neither turned up anywhere. Handed back unrewritten, per how this editor works.

## The key differences, in plain English

**They agree on the diagnosis.** Both versions reached the same verdict, needs another pass, and both picked the same worst offender: the Peter Sellers paragraph, where three generic praise phrases stack up in three sentences and one of them ("a testament to") is the exact phrase the voice profile names as not-this-writer. Both also flagged the hook-question opener, the "isn't just a comedy" amplifier, the banned word "profound", the American spelling of "favourite", and the "At the end of the day" closer. Two separate installs, two different apps, no shared history, same rulebook in, broadly the same critique out. That is the strongest evidence in this document: the judgement lives in the files, not in the app around them.

**They differ in character.** The Desktop version behaves like an editor in the room. It weighs the findings, reads the draft as a whole ("a voice problem more than a grammar one") and ends by telling the writer which two things to fix first. It counts loosely ("several Weakens"), and it caught things the Code version missed: the "trust me" sales close, the decorative "rich tapestry" line, and the flat, same-length sentence rhythm running through the middle paragraphs. The Code version behaves like an inspector. Exact counts (1 Blocking, 9 Weakens, 0 Note), every finding tied to a named rule, and fuller mechanical coverage: it caught all three American spellings ("favorite", "humor", "realize") where Desktop caught only the first. They also weigh differently at the margin: Desktop rates the closing line Blocking because the same amplifier trick opens and closes the post; Code rates it Weakens. Same worst problem, slightly different severity at the edges.

**One of them slipped, and the slip is evidence too.** The Desktop version's own opening line contains an em dash and a tangled sentence ("No voice profile disclaimer doesn't apply here"), which breaks rules the editor itself enforces. It has been left in this document exactly as it came back, because it demonstrates the product's whole premise: prose drifts, even a machine applying the rules drifts when it is talking rather than checking, and drift gets caught by inspection, not by intention. The Code version's own prose stayed clean, and it closed by confirming its own mechanical checks.

**What that means in practice.** Run the Desktop version when you want an editor's read: priorities, feel, what to fix first. Run the Code version when you want the full inspection: every rule, every spelling, exact counts. They are the same doctrine wearing two temperaments, and the gap between them is small enough to trust the rules and large enough to be worth keeping both.