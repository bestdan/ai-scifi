"""Tests for scripts/lint_prose.py. Run: python3 -m unittest discover -s tests"""

import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import lint_prose as L  # noqa: E402

RULES = L.load_rules(L.DEFAULT_RULES)
STORY = REPO / "stories" / "calibration-01"

# The paragraph closers the Cartographer listed in its draft-2 review
# (stories/calibration-01/reviews/draft-2/cartographer.md, note 4).
CARTOGRAPHER_CLOSERS = [
    "which was the nearest he came to saying anything",
    "because Bisi was watching her from the stove",
    "which was worse",
    "because the letter was hers",
    "They had built the term around the latest she could possibly be",
    "and she put it back in the box",
    "Oyelaran said it was very good",
    "and nobody asked her to",
]


def lint_text(text: str, waiver: str = ""):
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "final.md"
        path.write_text(text, encoding="utf-8")
        if waiver:
            (Path(d) / "lint-waivers.toml").write_text(waiver)
        return L.lint(path, RULES)


def ids(findings, severity=None):
    return [f.rule for f in findings if severity is None or f.severity == severity]


class Rules(unittest.TestCase):
    def test_banned_phrase(self):
        f, failed, _ = lint_text("It was a testament to her patience.\n")
        self.assertIn("banned-phrase", ids(f, "error"))
        self.assertTrue(failed)

    def test_plain_prose_is_clean(self):
        f, failed, _ = lint_text("She drank her tea and went out to the boat.\n")
        self.assertEqual(f, [])
        self.assertFalse(failed)

    def test_banned_name_is_whole_word_and_case_sensitive(self):
        self.assertIn("banned-name", ids(lint_text("Nova closed the hatch.\n")[0]))
        self.assertNotIn("banned-name", ids(lint_text("Novak closed the hatch.\n")[0]))
        self.assertNotIn("banned-name", ids(lint_text("A nova lit the sky.\n")[0]))

    def test_banned_ship(self):
        self.assertIn("banned-ship", ids(lint_text("They boarded the *Odyssey* at dawn.\n")[0]))
        self.assertNotIn("banned-ship", ids(lint_text("The sun rose over the horizon.\n")[0]))

    def test_em_dash_window(self):
        three = "One — two — three — four words here.\n"
        f, failed, _ = lint_text(three)
        self.assertIn("em-dash-pileup", ids(f))
        self.assertTrue(failed)
        spaced = "A — b.\n\n" + ("word " * 320) + "\n\nC — d — e.\n"
        self.assertNotIn("em-dash-pileup", ids(lint_text(spaced)[0]))

    def test_the_way_excludes_literal_uses(self):
        literal = "On the way to the surgery she cried. He knew the way home.\n"
        self.assertNotIn("the-way-simile", ids(lint_text(literal)[0]))
        simile = "He held it the way other men carry a bowl.\n"
        self.assertIn("the-way-simile", ids(lint_text(simile)[0]))

    def test_the_way_is_warn_only(self):
        text = "".join(f"She did it the way a cat {i} does.\n\n" for i in range(4))
        _, failed, summary = lint_text(text)
        self.assertFalse(failed)
        self.assertTrue(any("count the-way-simile: 4" in s for s in summary))

    def test_contrast_shape(self):
        self.assertIn("contrast-shape", ids(lint_text("It wasn't fear. It was hunger.\n")[0]))
        self.assertIn("contrast-shape",
                      ids(lint_text('"That\'s not argument. That\'s a heron."\n')[0]))

    def test_contrast_negative_from_calibration_01(self):
        text = "She had noticed it and had not done the sum. She had wanted the seat.\n"
        self.assertNotIn("contrast-shape", ids(lint_text(text)[0]))

    def test_zinger_is_warn_only(self):
        text = "She walked to the jetty in the rain and stood a long while. Then she left.\n"
        f, failed, summary = lint_text(text)
        self.assertIn("zinger-closer", ids(f, "warn"))
        self.assertFalse(failed)
        self.assertTrue(any("per 1,000 words" in s for s in summary))

    def test_zinger_skips_dialogue_and_single_sentences(self):
        self.assertNotIn("zinger-closer", ids(lint_text('"Go home. Now."\n')[0]))
        self.assertNotIn("zinger-closer", ids(lint_text("She left.\n")[0]))


class Skips(unittest.TestCase):
    def test_headings_scene_break_and_notes_are_skipped(self):
        text = ("# A testament to nothing\n\n## Nine\n\nShe drank her tea.\n\n"
                '<p align="center">·</p>\n\n## Drafter\'s notes\n\n'
                "This tapestry of notes is ignored.\n")
        f, failed, _ = lint_text(text)
        self.assertEqual(ids(f, "error"), [])
        self.assertFalse(failed)

    def test_waiver(self):
        waiver = '[[waiver]]\nrule = "banned-phrase"\nreason = "a test"\n'
        f, failed, _ = lint_text("A tapestry hung there.\n", waiver)
        self.assertEqual(ids(f, "waived"), ["banned-phrase"])
        self.assertFalse(failed)

    def test_line_numbers(self):
        f, _, _ = lint_text("Clean.\n\nStill clean.\nA tapestry here.\n")
        self.assertEqual([x.line for x in f if x.rule == "banned-phrase"], [4])


class Calibration01(unittest.TestCase):
    """The accepted final passes; the zinger rule finds the reviewer's closers."""

    def test_final_passes_strict(self):
        _, failed, summary = L.lint(STORY / "final.md", RULES)
        self.assertFalse(failed, summary)

    def test_zinger_recall_on_draft_2(self):
        f, _, _ = L.lint(STORY / "drafts" / "draft-2.md", RULES)
        flagged = [x.text for x in f if x.rule == "zinger-closer"]
        found = [c for c in CARTOGRAPHER_CLOSERS
                 if any(c in t or t in c for t in flagged)]
        self.assertGreaterEqual(len(found), 6, found)

    def test_draft_1_counts_more_similes_than_final(self):
        def count(path):
            f, _, _ = L.lint(path, RULES)
            return sum(1 for x in f if x.rule == "the-way-simile")
        self.assertGreater(count(STORY / "drafts" / "draft-1.md"), count(STORY / "final.md"))


if __name__ == "__main__":
    unittest.main()
