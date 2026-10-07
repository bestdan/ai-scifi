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
        for row in ("Premise", "Stakes", "Why", "Twist", "Ending"):
            self.assertIn(f"| {row} |", self.text, row)

    def test_ledger_rejects_never_explained(self):
        self.assertIn("not a valid ledger entry", self.text)

    def test_stakes_before_the_climax(self):
        self.assertIn("before the climax", self.text)


class Outline(unittest.TestCase):
    def test_columns(self):
        text = (TEMPLATES / "outline.md").read_text()
        for column in ("Made explicit by", "Introduces"):
            self.assertIn(column, text, column)


if __name__ == "__main__":
    unittest.main()
