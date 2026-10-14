"""Checks that the templates carry the structures the process relies on."""

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATES = REPO / "templates"


class StoryBible(unittest.TestCase):
    def setUp(self):
        self.text = (TEMPLATES / "story-bible.md").read_text()

    def test_payoff_ledger_has_graded_rows(self):
        self.assertIn("## Payoff ledger", self.text)
        for row in ("Premise", "Stakes", "Why", "Twist", "Ending", "Reach"):
            self.assertIn(f"| {row} |", self.text, row)

    def test_ledger_rejects_never_explained(self):
        self.assertIn("not a valid ledger entry", self.text)

    def test_stakes_before_the_climax(self):
        self.assertIn("before the climax", self.text)

    def test_glossary_terms_carry_a_job(self):
        self.assertIn("| Term | Meaning | Job | Clear at first use by |", self.text)

    def test_world_list_and_stated_and_shown(self):
        self.assertIn("## What the reader needs about the world", self.text)
        self.assertIn("Shown in (scene)", self.text)


class Critique(unittest.TestCase):
    def setUp(self):
        self.text = (TEMPLATES / "critique.md").read_text()

    def test_scores_table_has_no_understood_axis(self):
        scores = self.text.split("## Scores", 1)[1].split("\n## ", 1)[0]
        rows = [line for line in scores.splitlines() if line.startswith("| ")]
        self.assertTrue(rows)
        for row in rows:
            self.assertNotIn("Understood", row)

    def test_what_to_protect_is_required(self):
        section = self.text.split("## What to protect", 1)[1].split("\n## ", 1)[0]
        self.assertIn("Required", section)


class Outline(unittest.TestCase):
    def test_columns(self):
        text = (TEMPLATES / "outline.md").read_text()
        for column in ("Made explicit by", "Shown by", "Introduces", "World fact"):
            self.assertIn(column, text, column)


if __name__ == "__main__":
    unittest.main()
