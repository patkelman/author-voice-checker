#!/usr/bin/env python3
"""
check.py - the deterministic mechanical floor for the editor.

This runs before the LLM editor as a first pass, and the editor also runs it
over its own findings prose before a review goes back (see rules.md, "The
editor's own prose"). It catches the mechanically detectable subset of the
catalogue in reference/ai-pattern-catalogue.md: five L1 checks plus, when a
voice profile is supplied, an L2 profile floor (never-uses words and US
spellings against a British locale).

Every finding uses the four-part shape from reference/critique-format.md:

    Line: <location and quoted text>
    Rule: <a catalogue ID or a named profile field>
    Why it fails here: <specific to this reader and this draft>
    Severity: Blocking | Weakens | Note

Stdlib only. Importable (see the public functions below) and runnable:

    python3 check.py <draft.md> [--profile <profile.md>]
    python3 check.py --selftest

Two failures this file exists to close: a review once shipped six em dashes
while reviewing a draft for exactly that pattern, and a review once quoted a
sentence with a US spelling in it and never flagged the spelling. Both are
covered by the fixtures at the bottom of this file.
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# The finding shape (mirrors reference/critique-format.md)
# ---------------------------------------------------------------------------

SEVERITY_RANK = {"Blocking": 0, "Weakens": 1, "Note": 2}

NO_PROFILE_DISCLAIMER = (
    "No voice profile was supplied. These findings are universal-layer only, "
    "they say nothing about whether this draft sounds like you specifically."
)


@dataclass
class Finding:
    line: str
    rule: str
    why: str
    severity: str
    # Internal only, used for the "3 or more hits in one sentence" escalation.
    # Never rendered.
    cluster_key: Optional[Tuple[int, int]] = None

    def render(self) -> str:
        return (
            f"Line: {self.line}\n"
            f"Rule: {self.rule}\n"
            f"Why it fails here: {self.why}\n"
            f"Severity: {self.severity}"
        )


@dataclass
class CheckResult:
    findings: List[Finding]
    profile_supplied: bool
    deduped_buzzwords: List[str] = field(default_factory=list)
    total_words: int = 0


# ---------------------------------------------------------------------------
# Universal buzzword list (L1-11)
#
# This is the always-on, general-purpose list, kept deliberately separate
# from a writer's own profile "never uses" list. It is a defensible common
# set, not exhaustive; the seed came from the task brief and was rounded out
# with the usual corporate-deck staples. Adjust freely, but keep it general
# rather than specific to any one writer.
# ---------------------------------------------------------------------------

UNIVERSAL_BUZZWORDS = [
    "leverage",
    "synergy",
    "seamless",
    "seamlessly",
    "robust",
    "holistic",
    "cutting-edge",
    "best-in-class",
    "game-changer",
    "game changer",
    "deep dive",
    "move the needle",
    "state-of-the-art",
    "paradigm",
    "paradigm shift",
    "disruptive",
    "disruption",
    "innovative",
    "innovation",
    "streamline",
    "streamlined",
    "ecosystem",
    "elevate",
    "unlock",
    "supercharge",
    "turnkey",
    "low-hanging fruit",
    "circle back",
    "value-add",
    "bandwidth",
    "actionable",
    "empower",
    "empowering",
    "world-class",
    "next-level",
    "next level",
    "boil the ocean",
]

# ---------------------------------------------------------------------------
# US to UK spelling map (profile floor, British locale)
#
# Explicit pairs named in the task brief, plus a generated -ize/-ise and
# -yze/-yse family so the list covers common derived forms (organization,
# organizing, and so on) without hand typing every one.
# ---------------------------------------------------------------------------

EXPLICIT_US_UK_PAIRS = {
    "color": "colour",
    "colors": "colours",
    "colored": "coloured",
    "coloring": "colouring",
    "center": "centre",
    "centers": "centres",
    "centered": "centred",
    "favor": "favour",
    "favors": "favours",
    "favored": "favoured",
    "favorite": "favourite",
    "favorites": "favourites",
    "catalog": "catalogue",
    "catalogs": "catalogues",
    "cataloged": "catalogued",
    "theater": "theatre",
    "theaters": "theatres",
    "defense": "defence",
    "defenses": "defences",
    "traveler": "traveller",
    "travelers": "travellers",
    "traveled": "travelled",
    "traveling": "travelling",
    "licence": "licence",  # placeholder, deliberately not flagged; see note below
}
# "licence/license" and "program/programme" are deliberately left out: both are
# context-sensitive (a licence to practise vs. to license someone; a computer
# program vs. a stage programme), and a blind word match on either would fire
# on ordinary British usage as often as it caught a genuine US spelling. The
# placeholder key above is removed immediately below rather than shipped.
del EXPLICIT_US_UK_PAIRS["licence"]

_IZE_ROOTS = [
    "organiz",
    "optimiz",
    "recogniz",
    "realiz",
    "specializ",
    "characteriz",
    "apologiz",
    "criticiz",
    "emphasiz",
    "prioritiz",
    "summariz",
    "standardiz",
    "capitaliz",
    "minimiz",
    "maximiz",
    "utiliz",
    "customiz",
    "moderniz",
    "familiariz",
    "memoriz",
    "finaliz",
    "generaliz",
    "socializ",
    "stabiliz",
    "normaliz",
]
_IZE_SUFFIXES = ["e", "ed", "es", "ing", "ation", "ations", "er", "ers"]

_YZE_ROOTS = ["analyz", "paralyz", "catalyz"]
_YZE_SUFFIXES = ["e", "ed", "es", "ing", "er", "ers"]


def _build_derived_us_uk_pairs() -> Dict[str, str]:
    pairs = {}
    for root in _IZE_ROOTS:
        uk_root = root[:-2] + "is"  # "organiz" -> "organis"
        for suf in _IZE_SUFFIXES:
            us_form = root + suf
            uk_form = uk_root + suf
            if us_form != uk_form:
                pairs[us_form] = uk_form
    for root in _YZE_ROOTS:
        uk_root = root[:-2] + "ys"  # "analyz" -> "analys"
        for suf in _YZE_SUFFIXES:
            us_form = root + suf
            uk_form = uk_root + suf
            if us_form != uk_form:
                pairs[us_form] = uk_form
    return pairs


US_TO_UK: Dict[str, str] = {}
US_TO_UK.update(EXPLICIT_US_UK_PAIRS)
US_TO_UK.update(_build_derived_us_uk_pairs())

# ---------------------------------------------------------------------------
# Paste and typography artefact characters (L1-15)
# ---------------------------------------------------------------------------

ARTEFACT_CHAR_NAMES = {
    "‘": "curly single opening quote (U+2018)",
    "’": "curly single closing quote or apostrophe (U+2019)",
    "“": "curly double opening quote (U+201C)",
    "”": "curly double closing quote (U+201D)",
    " ": "non-breaking space (U+00A0)",
    "​": "zero-width space (U+200B)",
    "﻿": "zero-width no-break space or byte-order mark (U+FEFF)",
    "→": "rightwards arrow standing in for a word (U+2192)",
}
PASTE_ARTEFACT_RE = re.compile("[" + "".join(ARTEFACT_CHAR_NAMES.keys()) + "]")

# ---------------------------------------------------------------------------
# Dash artefacts (L1-01)
# ---------------------------------------------------------------------------

# Em dash (U+2014) or en dash (U+2013) sitting between two words, spaced or
# not. Deliberately requires a letter, digit, or closing/opening quote mark on
# each side so a plain spaced hyphen (list markers, ranges, hyphenation) is
# never a candidate: this pattern only ever matches the real dash character.
_DASH_CHARS = "\u2014\u2013"  # em dash, en dash, written as escapes so the
# characters this file hunts for never appear as literal bytes in its own
# source (the hard constraint against em dashes anywhere in this file)
_DASH_SIDE = r"[A-Za-z0-9)\"'’”]"
_DASH_SIDE_AFTER = r"[A-Za-z0-9(\"'‘“]"
EM_EN_DASH_RE = re.compile(
    r"(?:(?<=" + _DASH_SIDE + r")[" + _DASH_CHARS + r"](?=" + _DASH_SIDE_AFTER + r"))"
    r"|(?:(?<=" + _DASH_SIDE + r")\s[" + _DASH_CHARS + r"]\s(?=" + _DASH_SIDE_AFTER + r"))"
)

# The typewriter substitute: a spaced double hyphen. A single spaced hyphen
# (" - ") is explicitly never flagged; this only matches the doubled form.
ASCII_DOUBLE_HYPHEN_RE = re.compile(r"(?<=\S) -- (?=\S)")

# ---------------------------------------------------------------------------
# The bare amplifier (L1-14): "not just X, it was Y" and close variants,
# straight and curly apostrophes both handled.
# ---------------------------------------------------------------------------

BARE_AMPLIFIER_RE = re.compile(
    r"\b(?:not just|(?:was|is)n[’']t just)\b[^,.\n]{1,80},\s*(?:it was|it's|but)\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Bold-lead bullet skeleton (L1-12): a run of 3 or more consecutive
# "- **Label:** sentence" lines. One or two is ordinary and never flags.
# ---------------------------------------------------------------------------

BOLD_BULLET_RE = re.compile(r"^\s*[-*]\s+\*\*[^*\n]+:\*\*\s+\S.*$")

# ---------------------------------------------------------------------------
# Code masking: fenced blocks and inline spans are excluded from every check.
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def mask_code(lines: List[str]) -> List[str]:
    """Return a copy of lines with fenced code blocks and inline code spans
    blanked out (replaced with spaces of the same length, so offsets and
    line numbers still line up with the original text)."""
    masked = []
    in_fence = False
    for line in lines:
        if _FENCE_RE.match(line):
            masked.append(" " * len(line))
            in_fence = not in_fence
            continue
        if in_fence:
            masked.append(" " * len(line))
            continue

        def _blank(m: "re.Match") -> str:
            return " " * len(m.group(0))

        masked.append(_INLINE_CODE_RE.sub(_blank, line))
    return masked


# ---------------------------------------------------------------------------
# Paragraphs and sentences
#
# A paragraph is a maximal run of non-blank lines. Lines inside a paragraph
# are joined with a single space so a phrase that hard-wraps across two
# source lines (common in this kind of draft, see examples.md) still matches
# as one phrase, while every match can still be traced back to a real line
# number. Sentences are a plain regex approximation, used only to group
# findings for the "3 or more in one sentence" escalation, not to judge
# grammar.
# ---------------------------------------------------------------------------

_SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+")


def sentence_spans(text: str) -> List[Tuple[int, int]]:
    spans = []
    start = 0
    for m in _SENTENCE_BOUNDARY_RE.finditer(text):
        end = m.start()
        if end > start:
            spans.append((start, end))
        start = m.end()
    if start < len(text):
        spans.append((start, len(text)))
    if not spans:
        spans = [(0, len(text))]
    return spans


def _sentence_index_for_offset(spans: List[Tuple[int, int]], offset: int) -> int:
    for idx, (s, e) in enumerate(spans):
        if s <= offset < e:
            return idx
    return len(spans) - 1 if spans else 0


class Paragraph:
    def __init__(self, start_line: int, orig_lines: List[str], masked_lines: List[str]):
        self.start_line = start_line
        self.orig_lines = orig_lines
        self.masked_lines = masked_lines
        parts_m = []
        offsets = []
        pos = 0
        for i, ml in enumerate(masked_lines):
            offsets.append((pos, start_line + i))
            parts_m.append(ml)
            pos += len(ml) + 1  # +1 for the single joining space
        self.joined_masked = " ".join(parts_m)
        self.line_offsets = offsets
        self.sentence_spans = sentence_spans(self.joined_masked)

    def line_at(self, offset: int) -> int:
        line_no = self.line_offsets[0][1] if self.line_offsets else self.start_line
        for start, ln in self.line_offsets:
            if start <= offset:
                line_no = ln
            else:
                break
        return line_no


def build_paragraphs(orig_lines: List[str], masked_lines: List[str]) -> List[Paragraph]:
    paragraphs = []
    cur_orig: List[str] = []
    cur_masked: List[str] = []
    start = None
    for i, (ol, ml) in enumerate(zip(orig_lines, masked_lines), start=1):
        if ol.strip() == "":
            if cur_orig:
                paragraphs.append(Paragraph(start, cur_orig, cur_masked))
                cur_orig, cur_masked, start = [], [], None
            continue
        if start is None:
            start = i
        cur_orig.append(ol)
        cur_masked.append(ml)
    if cur_orig:
        paragraphs.append(Paragraph(start, cur_orig, cur_masked))
    return paragraphs


def _locate(para: Paragraph, p_idx: int, offset: int) -> Tuple[int, Tuple[int, int]]:
    line_no = para.line_at(offset)
    s_idx = _sentence_index_for_offset(para.sentence_spans, offset)
    return line_no, (p_idx, s_idx)


def quote_line(orig_lines: List[str], line_no: int, max_len: int = 160) -> str:
    text = orig_lines[line_no - 1].strip()
    if len(text) > max_len:
        text = text[: max_len - 3].rstrip() + "..."
    return text


_WORD_RE = re.compile(r"[A-Za-z']+")


def count_words(paragraphs: List[Paragraph]) -> int:
    return sum(len(_WORD_RE.findall(p.joined_masked)) for p in paragraphs)


def build_phrase_pattern(phrase: str) -> "re.Pattern":
    words = phrase.split()
    escaped_words = [re.escape(w) for w in words]
    body = r"\s+".join(escaped_words)
    return re.compile(r"(?<![A-Za-z0-9])" + body + r"(?![A-Za-z0-9])", re.IGNORECASE)


_UNIVERSAL_BUZZWORD_PATTERNS = {p: build_phrase_pattern(p) for p in UNIVERSAL_BUZZWORDS}

# ---------------------------------------------------------------------------
# Profile parsing (L2)
# ---------------------------------------------------------------------------


@dataclass
class ProfileData:
    never_uses: Set[str]
    british_locale: bool
    bans_em_dash: bool


def extract_field_block(text: str, field_label: str) -> str:
    pattern = re.compile(
        r"-\s+\*\*"
        + re.escape(field_label)
        + r":?\*\*\s*(.*?)(?=\n\s*[-*]\s+\*\*|\n#|\Z)",
        re.IGNORECASE | re.DOTALL,
    )
    m = pattern.search(text)
    return m.group(1).strip() if m else ""


_QUOTE_RE = re.compile(r'["“]([^"”]+)["”]')
_PAREN_RE = re.compile(r"\([^)]*\)")
_QUALIFIER_SUFFIX_RE = re.compile(r"\s+as\s+(?:a|an)\s+\w+$", re.IGNORECASE)
_TOKEN_SHAPE_RE = re.compile(r"^[A-Za-z][A-Za-z']*(?:[\s-][A-Za-z][A-Za-z']*){0,3}$")
_LEADING_STRIP_WORDS = {"the", "formal", "connectors", "connector"}


def parse_never_uses(block_text: str) -> Set[str]:
    """Pull a clean set of literal words and phrases out of a profile's own
    prose "never uses" field. The field is free text, not a clean list, so
    this is a heuristic: quoted phrases are trusted as-is (the writer went to
    the trouble of quoting them), unquoted comma or semicolon separated
    segments are cleaned of leading descriptive words (for example "the
    formal connectors moreover" becomes "moreover") and of a trailing part-of-
    speech qualifier ("underscore as a verb" becomes "underscore"), then kept
    only if what remains has the shape of a real word or short phrase rather
    than a run of descriptive prose."""
    phrases: Set[str] = set()
    if not block_text:
        return phrases

    for m in _QUOTE_RE.finditer(block_text):
        phrase = m.group(1).strip()
        phrase = phrase.rstrip("?:").strip()
        phrase = re.sub(r"\.\.\.+$", "", phrase).strip()
        phrase = phrase.rstrip(".").strip()
        if phrase:
            phrases.add(phrase.lower())

    remaining = _QUOTE_RE.sub(" ", block_text)
    remaining = _PAREN_RE.sub(" ", remaining)
    for tok in re.split(r"[;,]", remaining):
        tok = tok.strip().strip(".").strip()
        if not tok:
            continue
        words = tok.split()
        while words and words[0].lower() in _LEADING_STRIP_WORDS:
            words.pop(0)
        tok = " ".join(words).strip()
        if not tok:
            continue
        tok = _QUALIFIER_SUFFIX_RE.sub("", tok).strip()
        if _TOKEN_SHAPE_RE.match(tok):
            phrases.add(tok.lower())
    return phrases


def parse_profile(profile_text: str) -> ProfileData:
    block = extract_field_block(profile_text, "Words and phrases this writer never uses")
    never_uses = parse_never_uses(block)
    locale_block = extract_field_block(profile_text, "Locale and spelling")
    british = bool(re.search(r"british", locale_block, re.IGNORECASE)) if locale_block else False
    if not british:
        british = bool(re.search(r"british english", profile_text, re.IGNORECASE))
    bans_em_dash = bool(re.search(r"no em dash", profile_text, re.IGNORECASE))
    return ProfileData(never_uses=never_uses, british_locale=british, bans_em_dash=bans_em_dash)


# ---------------------------------------------------------------------------
# Escalation: 3 or more hits, from any check, inside one sentence, raise that
# whole cluster to Blocking (never downgrades an existing Blocking).
# ---------------------------------------------------------------------------


def apply_clustering_escalation(findings: List[Finding]) -> None:
    groups: Dict[Tuple[int, int], List[Finding]] = {}
    for f in findings:
        if f.cluster_key is None:
            continue
        groups.setdefault(f.cluster_key, []).append(f)
    for group in groups.values():
        if len(group) >= 3:
            for f in group:
                if f.severity != "Blocking":
                    f.severity = "Blocking"


# ---------------------------------------------------------------------------
# The checks
# ---------------------------------------------------------------------------


def check_dash_artefacts(
    paragraphs: List[Paragraph], orig_lines: List[str], total_words: int, profile: Optional[ProfileData]
) -> List[Finding]:
    raw_hits = []
    for p_idx, para in enumerate(paragraphs):
        for pattern in (EM_EN_DASH_RE, ASCII_DOUBLE_HYPHEN_RE):
            for m in pattern.finditer(para.joined_masked):
                line_no, key = _locate(para, p_idx, m.start())
                raw_hits.append((line_no, key))
    if not raw_hits:
        return []

    if profile is not None and profile.bans_em_dash:
        severity = "Blocking"
        why_tail = "the loaded voice profile states no em dashes, ever, so a single instance already breaks the rule."
    else:
        density = (len(raw_hits) / total_words * 100) if total_words else 0
        if density > 2:
            severity = "Blocking"
            why_tail = (
                "the draft carries about %.1f em or en dashes per hundred words, above the "
                "catalogue's density line, so the pattern reads as a habit rather than an "
                "occasional choice." % density
            )
        else:
            severity = "Weakens"
            why_tail = (
                "on its own this reads as an occasional slip rather than a habit, but a comma "
                "or a full stop would carry the same sense."
            )

    findings = []
    for line_no, key in raw_hits:
        findings.append(
            Finding(
                line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                rule="L1-01, em dash overreliance",
                why=f"this line joins clauses with a dash where other punctuation would do the same job; {why_tail}",
                severity=severity,
                cluster_key=key,
            )
        )
    return findings


def check_paste_artefacts(
    paragraphs: List[Paragraph], orig_lines: List[str], total_words: int
) -> List[Finding]:
    raw_hits = []
    for p_idx, para in enumerate(paragraphs):
        for m in PASTE_ARTEFACT_RE.finditer(para.joined_masked):
            line_no, key = _locate(para, p_idx, m.start())
            raw_hits.append((line_no, key, m.group(0)))
    if not raw_hits:
        return []
    density = (len(raw_hits) / total_words * 100) if total_words else 0
    base_severity = "Blocking" if density > 2 else "Weakens"
    findings = []
    for line_no, key, ch in raw_hits:
        name = ARTEFACT_CHAR_NAMES.get(ch, "unrecognised artefact character (U+%04X)" % ord(ch))
        findings.append(
            Finding(
                line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                rule=f"L1-15, paste and typography artefact ({name})",
                why=(
                    "this character is not one a writer types on purpose; it is the kind of "
                    "thing that survives a paste from a model or a word processor, and a "
                    "reader on the right device sees the glitch even where the writer never did."
                ),
                severity=base_severity,
                cluster_key=key,
            )
        )
    return findings


def check_buzzwords(
    paragraphs: List[Paragraph], orig_lines: List[str], total_words: int, profile: Optional[ProfileData]
) -> Tuple[List[Finding], List[str]]:
    never_uses_lower = set(profile.never_uses) if profile else set()
    raw_hits = []
    deduped: List[str] = []
    for p_idx, para in enumerate(paragraphs):
        for phrase, pattern in _UNIVERSAL_BUZZWORD_PATTERNS.items():
            for m in pattern.finditer(para.joined_masked):
                line_no, key = _locate(para, p_idx, m.start())
                if phrase.lower() in never_uses_lower:
                    deduped.append(phrase)
                    continue
                raw_hits.append((line_no, key, m.group(0), phrase))
    if not raw_hits:
        return [], deduped

    density = (len(raw_hits) / total_words * 100) if total_words else 0
    base_severity = "Blocking" if density > 3 else "Weakens"
    findings = []
    for line_no, key, matched, phrase in raw_hits:
        findings.append(
            Finding(
                line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                rule=f'L1-11, buzzword saturation ("{phrase}")',
                why=(
                    f'"{matched}" is one of the small set of words that shows up in every '
                    "corporate deck and every first AI draft; the plainer word in its place "
                    "would lose nothing."
                ),
                severity=base_severity,
                cluster_key=key,
            )
        )
    return findings, deduped


def check_bare_amplifier(paragraphs: List[Paragraph], orig_lines: List[str]) -> List[Finding]:
    raw_hits = []
    for p_idx, para in enumerate(paragraphs):
        for m in BARE_AMPLIFIER_RE.finditer(para.joined_masked):
            line_no, key = _locate(para, p_idx, m.start())
            raw_hits.append((line_no, key))
    if not raw_hits:
        return []
    base_severity = "Blocking" if len(raw_hits) >= 2 else "Weakens"
    findings = []
    for line_no, key in raw_hits:
        findings.append(
            Finding(
                line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                rule="L1-14, the bare amplifier",
                why=(
                    "this concedes a claim only to escalate it in the same breath; swapped for "
                    'a plain "X, and Y" the sentence loses nothing but the performed drama.'
                ),
                severity=base_severity,
                cluster_key=key,
            )
        )
    return findings


def check_bold_bullet_runs(orig_lines: List[str], masked_lines: List[str]) -> List[Finding]:
    findings: List[Finding] = []
    run_lines: List[int] = []

    def flush():
        if len(run_lines) >= 3:
            length = len(run_lines)
            severity = "Blocking" if length >= 6 else "Weakens"
            findings.append(
                Finding(
                    line=f"lines {run_lines[0]} to {run_lines[-1]}: {length} consecutive bold-lead bullets",
                    rule="L1-12, bold-lead bullet skeleton",
                    why=(
                        f'{length} bullets in a row all follow the same "**Label:** sentence" shape; '
                        "written as connected prose instead, the same points would have to show the "
                        "argument the formatting is currently propping up."
                    ),
                    severity=severity,
                    cluster_key=None,
                )
            )
        run_lines.clear()

    for i, ml in enumerate(masked_lines, start=1):
        if orig_lines[i - 1].strip() == "":
            continue  # a blank line between list items does not break a run
        if BOLD_BULLET_RE.match(ml):
            run_lines.append(i)
        else:
            flush()
    flush()
    return findings


def check_profile_never_uses(
    paragraphs: List[Paragraph], orig_lines: List[str], profile: ProfileData
) -> List[Finding]:
    findings = []
    patterns = {phrase: build_phrase_pattern(phrase) for phrase in profile.never_uses}
    for p_idx, para in enumerate(paragraphs):
        for phrase, pattern in patterns.items():
            for m in pattern.finditer(para.joined_masked):
                line_no, key = _locate(para, p_idx, m.start())
                findings.append(
                    Finding(
                        line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                        rule=f'profile: never-uses "{phrase}"',
                        why=f'the loaded voice profile names "{phrase}" as a word or phrase this writer never uses.',
                        severity="Weakens",
                        cluster_key=key,
                    )
                )
    return findings


def check_profile_us_spelling(paragraphs: List[Paragraph], orig_lines: List[str]) -> List[Finding]:
    findings = []
    patterns = {us: (build_phrase_pattern(us), uk) for us, uk in US_TO_UK.items()}
    for p_idx, para in enumerate(paragraphs):
        for us_form, (pattern, uk_form) in patterns.items():
            for m in pattern.finditer(para.joined_masked):
                line_no, key = _locate(para, p_idx, m.start())
                matched = m.group(0)
                findings.append(
                    Finding(
                        line=f'line {line_no}: "{quote_line(orig_lines, line_no)}"',
                        rule=f'profile: US spelling "{matched}"',
                        why=f'the profile sets a British locale; "{matched}" is the American form, "{uk_form}" is the one that fits.',
                        severity="Weakens",
                        cluster_key=key,
                    )
                )
    return findings


# ---------------------------------------------------------------------------
# Entry point for running the whole floor over a draft
# ---------------------------------------------------------------------------


def run_check(draft_text: str, profile_text: Optional[str] = None) -> CheckResult:
    orig_lines = draft_text.splitlines()
    masked_lines = mask_code(orig_lines)
    paragraphs = build_paragraphs(orig_lines, masked_lines)
    total_words = count_words(paragraphs)
    profile = parse_profile(profile_text) if profile_text else None

    findings: List[Finding] = []
    findings += check_dash_artefacts(paragraphs, orig_lines, total_words, profile)
    findings += check_paste_artefacts(paragraphs, orig_lines, total_words)
    buzz_findings, deduped = check_buzzwords(paragraphs, orig_lines, total_words, profile)
    findings += buzz_findings
    findings += check_bare_amplifier(paragraphs, orig_lines)
    findings += check_bold_bullet_runs(orig_lines, masked_lines)
    if profile is not None:
        findings += check_profile_never_uses(paragraphs, orig_lines, profile)
        if profile.british_locale:
            findings += check_profile_us_spelling(paragraphs, orig_lines)

    apply_clustering_escalation(findings)
    findings.sort(key=lambda f: SEVERITY_RANK.get(f.severity, 9))

    return CheckResult(
        findings=findings,
        profile_supplied=profile is not None,
        deduped_buzzwords=deduped,
        total_words=total_words,
    )


def format_report(result: CheckResult) -> str:
    lines: List[str] = []
    if not result.profile_supplied:
        lines.append(NO_PROFILE_DISCLAIMER)
        lines.append("")

    if not result.findings:
        lines.append("Publish it. The mechanical floor found nothing to flag.")
        return "\n".join(lines)

    blocking = [f for f in result.findings if f.severity == "Blocking"]
    weakens = [f for f in result.findings if f.severity == "Weakens"]
    notes = [f for f in result.findings if f.severity == "Note"]

    if blocking:
        verdict = "Needs another pass."
    elif weakens:
        verdict = "Publish after fixes."
    else:
        verdict = "Publish it."

    lines.append(f"Verdict: {verdict}")
    lines.append(f"{len(blocking)} Blocking, {len(weakens)} Weakens, {len(notes)} Note.")
    lines.append("")
    for f in result.findings:
        lines.append(f.render())
        lines.append("")

    if result.deduped_buzzwords:
        unique_deduped = ", ".join(sorted(set(result.deduped_buzzwords)))
        lines.append(
            "Deduplication note: the following universal buzzword-list hits also appear "
            "on the loaded profile's own never-uses list, so each is reported once as the "
            f"more specific profile finding, not twice: {unique_deduped}."
        )

    return "\n".join(lines).rstrip() + "\n"


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def check_file(draft_path: str, profile_path: Optional[str] = None) -> str:
    draft_text = read_text_file(draft_path)
    profile_text = read_text_file(profile_path) if profile_path else None
    result = run_check(draft_text, profile_text)
    return format_report(result)


# ---------------------------------------------------------------------------
# Self-test fixtures
# ---------------------------------------------------------------------------

FIXTURE_PROFILE = """# Voice Profile Fixture

## Basics
- **Writer or project:** Fixture Writer
- **Locale and spelling:** British English.

## Vocabulary
- **Words and phrases this writer never uses:** leverage, pivotal, paramount, when it comes to

## Sentence habits
- **Punctuation quirks:** no em dashes, ever.
"""

KNOWN_BAD = (
    "This update wasn’t just an upgrade, it was a total transformation of "
    "the whole platform.\n"
    "\n"
    "It changed everything\u2014nothing was the same after that.\n"
    "\n"
    "We pasted this from somewhere and it kept a curly quote around "
    "‘testing’ and a curly double quote “example”, plus a "
    "stray arrow → pointing nowhere, and a hidden gap here.\n"
    "\n"
    "The plan will leverage a seamless, best-in-class ecosystem to move the "
    "needle for every client we serve -- starting today.\n"
    "\n"
    "- **Speed:** it gets faster every release.\n"
    "- **Scale:** it grows with the whole team.\n"
    "- **Trust:** it earns confidence fast.\n"
    "\n"
    "We know this is pivotal, and when it comes to results, nothing else is "
    "paramount. The programme optimizes color choices using an American "
    "analyze pass.\n"
)

KNOWN_GOOD = (
    "Charlotte Rampling is extraordinary in this, that stillness where she "
    "gives you almost nothing and you lean right in.\n"
    "\n"
    "We watched it Tuesday night at the Plaza in Truro, a full house for a "
    "film most of the room had never heard of. The double bill worked "
    "exactly the way it always does: the safe pick got them through the "
    "door, and the strange one is the reason half of them are still "
    "talking about it.\n"
    "\n"
    "Cheers, Pat.\n"
)


def _rule_text(findings: List[Finding]) -> str:
    return " | ".join(f.rule for f in findings)


def selftest() -> bool:
    print("Running check.py selftest...")
    passed = 0
    failures: List[str] = []

    def check(condition: bool, label: str) -> None:
        nonlocal passed
        if condition:
            passed += 1
        else:
            failures.append(label)

    bad_result = run_check(KNOWN_BAD, FIXTURE_PROFILE)
    rules = _rule_text(bad_result.findings)

    check("L1-01" in rules, "known-bad: expected an L1-01 (dash) finding")
    check("L1-15" in rules, "known-bad: expected an L1-15 (paste artefact) finding")
    check("L1-11" in rules, "known-bad: expected an L1-11 (buzzword) finding")
    check("L1-14" in rules, "known-bad: expected an L1-14 (bare amplifier) finding")
    check("L1-12" in rules, "known-bad: expected an L1-12 (bold-bullet run) finding")
    check("never-uses" in rules, "known-bad: expected a profile never-uses finding")
    check("US spelling" in rules, "known-bad: expected a profile US-spelling finding")

    dash_findings = [f for f in bad_result.findings if f.rule.startswith("L1-01")]
    check(
        bool(dash_findings) and all(f.severity == "Blocking" for f in dash_findings),
        "known-bad: expected every L1-01 dash finding to be Blocking under the profile's em-dash ban",
    )

    never_uses_findings = [f for f in bad_result.findings if "never-uses" in f.rule]
    never_uses_words = {f.rule for f in never_uses_findings}
    check(
        any("pivotal" in r for r in never_uses_words),
        "known-bad: expected the newly added never-uses word 'pivotal' to be caught",
    )
    check(
        any("paramount" in r for r in never_uses_words),
        "known-bad: expected the newly added never-uses word 'paramount' to be caught",
    )
    check(
        any("when it comes to" in r for r in never_uses_words),
        "known-bad: expected the newly added never-uses phrase 'when it comes to' to be caught",
    )

    good_result_with_profile = run_check(KNOWN_GOOD, FIXTURE_PROFILE)
    check(
        not good_result_with_profile.findings,
        "known-good (with profile): expected zero findings, got: " + _rule_text(good_result_with_profile.findings),
    )

    good_result_no_profile = run_check(KNOWN_GOOD, None)
    check(
        not good_result_no_profile.findings,
        "known-good (no profile): expected zero findings, got: " + _rule_text(good_result_no_profile.findings),
    )

    total = passed + len(failures)
    print(f"{passed}/{total} checks passed.")
    if failures:
        print("FAIL")
        for f in failures:
            print(" - " + f)
        return False
    print("PASS")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Deterministic mechanical floor for the editor: catches the mechanically "
            "detectable subset of reference/ai-pattern-catalogue.md."
        )
    )
    parser.add_argument("draft", nargs="?", help="path to the draft markdown file")
    parser.add_argument("--profile", default=None, help="path to a filled voice profile markdown file")
    parser.add_argument("--selftest", action="store_true", help="run the built-in fixtures and report pass or fail")
    args = parser.parse_args(argv)

    if args.selftest:
        ok = selftest()
        sys.exit(0 if ok else 1)

    if not args.draft:
        parser.print_help()
        sys.exit(2)

    print(check_file(args.draft, args.profile))


if __name__ == "__main__":
    main()
