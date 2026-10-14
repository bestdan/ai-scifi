"""Checks on the role agent definitions in .claude/agents/."""

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AGENTS = REPO / ".claude" / "agents"

# The model policy: creative roles run on opus, critique and reading on sonnet.
EXPECTED_MODELS = {
    "lens-ideator": "opus",
    "lens-critic": "sonnet",
    "cartographer": "opus",
    "drafter": "opus",
    "line-editor": "opus",
    "first-reader": "sonnet",
    "comprehension-grader": "sonnet",
}

# The comprehension gate's questions. They live in stage 7 only, so they reach
# the First Reader in its second turn and can't prime its read.
COMPREHENSION_QUESTIONS = [
    "What is this story about, in two sentences?",
    "What does the protagonist stand to gain or lose, and what happens if they fail?",
    "Why did the people or powers who set this situation up do it that way?",
    "What did you learn late that changed how you saw the earlier part, if anything?",
    "What happened at the end, and why?",
    "Who is each named character, in one line each?",
    "What are you still unsure about?",
    "Which words or terms didn't you know from the story itself, and where did you get their meaning, if you got it?",
    "What does the story's central change mean for people beyond its main characters?",
]


def frontmatter(path: Path) -> dict:
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(), re.DOTALL)
    assert m, f"{path} has no frontmatter"
    return dict(line.split(": ", 1) for line in m.group(1).splitlines())


class AgentDefinitions(unittest.TestCase):
    def test_every_role_exists_with_required_fields(self):
        found = {p.stem for p in AGENTS.glob("*.md")}
        self.assertEqual(found, set(EXPECTED_MODELS))
        for role, model in EXPECTED_MODELS.items():
            fm = frontmatter(AGENTS / f"{role}.md")
            for key in ("name", "description", "model", "tools"):
                self.assertIn(key, fm, f"{role} lacks {key}")
            self.assertEqual(fm["name"], role)
            self.assertEqual(fm["model"], model, f"{role} model policy")

    def test_first_reader_never_reads_the_style_guide(self):
        body = (AGENTS / "first-reader.md").read_text()
        self.assertNotIn("Read `process/style-guide.md`", body)

    def test_comprehension_grader_has_no_bash(self):
        tools = frontmatter(AGENTS / "comprehension-grader.md")["tools"]
        self.assertNotIn("Bash", tools)

    def test_comprehension_questions_live_in_stage_7_only(self):
        stage = (REPO / "process" / "stages" / "07-review.md").read_text()
        section = stage.split("## Comprehension questions", 1)[1].split("\n## ", 1)[0]
        reader_files = [
            (REPO / "personas" / "first-reader.md").read_text(),
            (AGENTS / "first-reader.md").read_text(),
        ]
        for question in COMPREHENSION_QUESTIONS:
            self.assertIn(question, section)
            for text in reader_files:
                self.assertNotIn(question, text)

    def test_grader_gate_reads_terms_and_the_lost_list(self):
        body = (AGENTS / "comprehension-grader.md").read_text()
        gate = body.split("**Gate:**", 1)[1].split("**Still unsure:**", 1)[0]
        self.assertIn("Terms is got it", gate)
        self.assertIn("Reach", gate)
        self.assertIn("lost-list", gate)
        # The count of lost-list entries no longer decides the gate
        # (dev_docs/decisions/2026-10-14-lost-list-gates-on-rows-not-count.md).
        self.assertNotIn("at most three", gate)

    def test_stage_7_splits_names_from_terms(self):
        stage = (REPO / "process" / "stages" / "07-review.md").read_text()
        self.assertIn("`names.md`: each named character", stage)
        self.assertIn("`terms.md`", stage)
        self.assertIn("Terms: stories/<slug>/reviews/draft-N/terms.md", stage)

    def test_first_reader_claims_no_experience_it_did_not_have(self):
        persona = (REPO / "personas" / "first-reader.md").read_text()
        self.assertNotIn("next day", persona)
        self.assertIn("claim no experience you didn't have", persona)

    def test_persona_files_named_by_lens_roles_exist(self):
        for name in ("cartographer", "first-reader", "line-editor"):
            self.assertTrue((REPO / "personas" / f"{name}.md").exists(), name)


if __name__ == "__main__":
    unittest.main()
