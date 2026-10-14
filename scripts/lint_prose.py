#!/usr/bin/env python3
"""Lint story prose against process/prose-rules.toml.

Usage: python3 scripts/lint_prose.py [--warn-only] [--quiet] [--rules PATH] FILE...

Prints one line per finding, `path:line: [error|warn|waived] rule-id: "text"`,
then a summary of each budget's use. Exits 1 on any error or budget overrun
(unless --warn-only), else 0. --quiet prints only what makes the lint fail.

Skipped: Markdown headings, the scene-break line `<p align="center">·</p>`,
and everything after a `## Drafter's notes` heading. A story's deliberate rule
breaks go in stories/<slug>/lint-waivers.toml as [[waiver]] rule = "...",
reason = "...".
"""

import argparse
import math
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_RULES = REPO / "process" / "prose-rules.toml"
SCENE_BREAK = '<p align="center">·</p>'
NOTES_HEADING = re.compile(r"^##\s+Drafter's notes", re.IGNORECASE)
QUOTES = "\"“'‘"
SENTENCE_END = re.compile(r"(?<=[.!?])[\"”’*]*\s+")
CLAUSE_SPLIT = re.compile(r"[,;:]\s+")


@dataclass
class Paragraph:
    line: int  # 1-based line where the paragraph starts
    text: str  # line breaks folded to spaces, so offsets map 1:1
    breaks: list  # offsets of the folded line breaks

    def line_at(self, offset: int) -> int:
        return self.line + sum(1 for b in self.breaks if b < offset)


@dataclass
class Finding:
    path: str
    line: int
    severity: str
    rule: str
    text: str

    def __str__(self) -> str:
        return f'{self.path}:{self.line}: [{self.severity}] {self.rule}: "{self.text}"'


def paragraphs(source: str) -> list:
    """Split story text into prose paragraphs, dropping skipped regions."""
    out, buf, start = [], [], 0
    lines = source.splitlines()

    def flush():
        if buf:
            text = " ".join(buf)
            breaks, pos = [], 0
            for part in buf[:-1]:
                pos += len(part)
                breaks.append(pos)
                pos += 1
            out.append(Paragraph(start, text, breaks))
            buf.clear()

    for n, raw in enumerate(lines, 1):
        line = raw.strip()
        if NOTES_HEADING.match(line):
            break
        if not line or line.startswith("#") or line == SCENE_BREAK:
            flush()
            continue
        if not buf:
            start = n
        buf.append(line)
    flush()
    return out


def plain(text: str) -> str:
    return text.replace("*", "")


def is_dialogue(p: Paragraph) -> bool:
    return plain(p.text)[:1] in QUOTES


def flags(rule: dict) -> int:
    return 0 if rule.get("case_sensitive", False) else re.IGNORECASE


def pattern_hits(rule: dict, paras: list):
    pats = [re.compile(p, flags(rule)) for p in rule.get("patterns", [])]
    before = [re.compile(p, re.IGNORECASE) for p in rule.get("exclude_before", [])]
    after = [re.compile(p, re.IGNORECASE) for p in rule.get("exclude_after", [])]
    for p in paras:
        text = plain(p.text)
        for pat in pats:
            for m in pat.finditer(text):
                pre, post = text[: m.start()], text[m.end():]
                if any(b.search(pre) for b in before) or any(a.search(post) for a in after):
                    continue
                yield p.line_at(m.start()), m.group(0)


def em_dash_hits(rule: dict, paras: list):
    words, dashes = 0, []  # (word index, line)
    for p in paras:
        for m in re.finditer(r"\S+|—", p.text):
            if "—" in m.group(0):
                dashes.append((words, p.line_at(m.start())))
            words += 1
    window, cap = rule["window_words"], rule["max_in_window"]
    reported = set()
    for i, (w, _) in enumerate(dashes):
        inside = [d for d in dashes[i:] if d[0] - w < window]
        if len(inside) > cap:
            for _, line in inside[cap:]:
                if line not in reported:
                    reported.add(line)
                    yield line, f"more than {cap} em-dashes within {window} words"


def zinger_hits(rule: dict, paras: list):
    for p in paras:
        if is_dialogue(p):
            continue
        text = plain(p.text).strip()
        sentences = [s for s in SENTENCE_END.split(text) if s]
        if len(sentences) < rule["min_sentences"]:
            continue
        last_clause = CLAUSE_SPLIT.split(sentences[-1])[-1].strip()
        if len(last_clause.split()) <= rule["max_words"]:
            yield p.line_at(len(text) - 1), last_clause


def rule_hits(rule: dict, paras: list):
    if rule["id"] == "em-dash-pileup":
        return em_dash_hits(rule, paras)
    if rule["id"] == "zinger-closer":
        return zinger_hits(rule, paras)
    return pattern_hits(rule, paras)


def story_dir(path: Path) -> Path:
    return path.parent.parent if path.parent.name == "drafts" else path.parent


def waivers(path: Path) -> set:
    f = story_dir(path) / "lint-waivers.toml"
    if not f.exists():
        return set()
    return {w["rule"] for w in tomllib.loads(f.read_text()).get("waiver", [])}


def budget_allowed(rule: dict, words: int) -> int:
    """`budget` is the floor; `budget_per_1000`, if set, scales it with length."""
    per = rule.get("budget_per_1000")
    if per is None:
        return rule["budget"]
    return max(rule["budget"], math.floor(per * words / 1000))


def lint(path: Path, rules: list) -> tuple:
    """Return (findings, failed, budget summary lines) for one file."""
    paras = paragraphs(path.read_text(encoding="utf-8"))
    words = sum(len(p.text.split()) for p in paras)
    waived = waivers(path)
    findings, failed, summary = [], False, []
    for rule in rules:
        hits = list(rule_hits(rule, paras))
        sev = rule["severity"]
        if rule["id"] in waived:
            findings += [Finding(str(path), l, "waived", rule["id"], t) for l, t in hits]
            continue
        shown = "error" if sev == "error" else "warn"
        findings += [Finding(str(path), l, shown, rule["id"], t) for l, t in hits]
        if sev == "error" and hits:
            failed = True
        if sev == "budget":
            allowed = budget_allowed(rule, words)
            over = len(hits) > allowed
            failed |= over
            summary.append(f"{path}: budget {rule['id']}: {len(hits)}/{allowed}"
                           + (" OVER" if over else ""))
        if sev == "warn":
            density = 1000 * len(hits) / words if words else 0
            summary.append(f"{path}: count {rule['id']}: {len(hits)}"
                           f" ({density:.1f} per 1,000 words)")
    return findings, failed, summary


def load_rules(path: Path) -> list:
    return tomllib.loads(path.read_text())["rule"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--warn-only", action="store_true")
    ap.add_argument("--quiet", action="store_true",
                    help="print only errors and budget overruns")
    ap.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    args = ap.parse_args(argv)
    rules = load_rules(args.rules)
    any_failed = False
    for path in args.files:
        findings, failed, summary = lint(path, rules)
        over = {line.split("budget ")[1].split(":")[0] for line in summary if "OVER" in line}
        for f in sorted(findings, key=lambda f: f.line):
            if not args.quiet or f.severity == "error" or f.rule in over:
                print(f)
        for line in summary:
            if not args.quiet or "OVER" in line:
                print(line)
        any_failed |= failed
    return 0 if args.warn_only or not any_failed else 1


if __name__ == "__main__":
    sys.exit(main())
