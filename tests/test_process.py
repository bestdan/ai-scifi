"""Checks that process/PROCESS.md and the stage files agree."""

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROCESS = REPO / "process" / "PROCESS.md"
STAGES = REPO / "process" / "stages"
AGENTS = REPO / ".claude" / "agents"


class ProcessLinks(unittest.TestCase):
    def test_process_links(self):
        links = re.findall(r"\]\((stages/[^)]+\.md)\)", PROCESS.read_text())
        self.assertEqual(len(links), 9, links)
        for link in links:
            self.assertTrue((REPO / "process" / link).exists(), link)

    def test_every_stage_file_is_linked(self):
        linked = set(re.findall(r"\]\(stages/([^)]+\.md)\)", PROCESS.read_text()))
        self.assertEqual({p.name for p in STAGES.glob("*.md")}, linked)

    def test_stage_files_dispatch_known_roles_without_model(self):
        roles = {p.stem for p in AGENTS.glob("*.md")}
        for stage in STAGES.glob("*.md"):
            text = stage.read_text()
            named = set(re.findall(r"`([a-z-]+)`", text)) & roles
            self.assertTrue(named, f"{stage.name} names no role")
            self.assertIn("pass `model:`", text.replace("Don't pass", "pass"),
                          f"{stage.name} lacks the no-model line")


if __name__ == "__main__":
    unittest.main()
