"""Checks that process/PROCESS.md and the stage files agree."""

import re
import unittest
from pathlib import Path

from test_agents import COMPREHENSION_QUESTIONS

REPO = Path(__file__).resolve().parent.parent
PROCESS = REPO / "process" / "PROCESS.md"
STAGES = REPO / "process" / "stages"
AGENTS = REPO / ".claude" / "agents"


class ProcessLinks(unittest.TestCase):
    def test_process_links(self):
        links = re.findall(r"\]\((stages/[^)]+\.md)\)", PROCESS.read_text())
        self.assertEqual(len(links), 10, links)
        for link in links:
            self.assertTrue((REPO / "process" / link).exists(), link)

    def test_every_stage_file_is_linked(self):
        linked = set(re.findall(r"\]\(stages/([^)]+\.md)\)", PROCESS.read_text()))
        self.assertEqual({p.name for p in STAGES.glob("*.md")}, linked)

    def test_polish_sets_no_cut_quota(self):
        for path in (STAGES / "09-polish.md", REPO / "personas" / "line-editor.md"):
            self.assertIsNone(re.search(r"\d+\s*(%|percent)", path.read_text()),
                              f"{path.name} sets a cut target")

    def test_stages_use_the_length_range(self):
        for stage in STAGES.glob("*.md"):
            text = stage.read_text()
            for phrase in ("target length", "115%"):
                self.assertNotIn(phrase, text, f"{stage.name}: {phrase}")

    def test_every_gate_names_both_modes(self):
        for stage in STAGES.glob("*.md"):
            for gate in re.findall(r"^\*\*Gate:\*\*.*?(?=\n\n|\Z)",
                                   stage.read_text(), re.MULTILINE | re.DOTALL):
                gate = " ".join(gate.split())
                for mode in ("`human` mode", "`proxy` mode"):
                    self.assertIn(mode, gate, f"{stage.name} gate lacks {mode}")

    def test_stage_files_dispatch_known_roles_without_model(self):
        roles = {p.stem for p in AGENTS.glob("*.md")}
        # The debrief is an interview with the human; it dispatches no agent.
        for stage in STAGES.glob("*.md"):
            if stage.name == "10-debrief.md":
                continue
            text = stage.read_text()
            named = set(re.findall(r"`([a-z-]+)`", text)) & roles
            self.assertTrue(named, f"{stage.name} names no role")
            self.assertIn("pass `model:`", text.replace("Don't pass", "pass"),
                          f"{stage.name} lacks the no-model line")

    def test_terms_and_reach_rows_in_the_debrief_and_rubric(self):
        for path in (REPO / "templates" / "debrief.md", REPO / "process" / "rubric.md"):
            for row in ("Terms", "Reach"):
                self.assertIn(f"| Understood | {row} |", path.read_text(), path.name)

    def test_synthesis_weighs_reach_and_picks_on_the_seed(self):
        text = (STAGES / "03-synthesize.md").read_text()
        self.assertIn("**Reach:**", text)
        self.assertIn("Pick on the brief's seed", text)

    def test_debrief_checks_the_human_with_directed_questions(self):
        # The human picks from options built from the ledger rows; the open
        # comprehension questions are for the cold reader alone.
        for path in (REPO / "templates" / "debrief.md", STAGES / "10-debrief.md"):
            text = path.read_text()
            self.assertIn("ledger-rows.md", text, path.name)
            self.assertIn("can't say", text.lower(), path.name)
            for question in COMPREHENSION_QUESTIONS:
                self.assertNotIn(question, text, f"{path.name}: {question}")


if __name__ == "__main__":
    unittest.main()
