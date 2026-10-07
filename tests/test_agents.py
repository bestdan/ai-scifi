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
}


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

    def test_persona_files_named_by_lens_roles_exist(self):
        for name in ("cartographer", "first-reader", "line-editor"):
            self.assertTrue((REPO / "personas" / f"{name}.md").exists(), name)


if __name__ == "__main__":
    unittest.main()
