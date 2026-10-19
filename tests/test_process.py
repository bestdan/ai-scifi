"""Checks that process/PROCESS.md and the stage files agree."""

import random
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

from test_agents import COMPREHENSION_QUESTIONS

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import assign_ideation  # noqa: E402
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

    def test_reader_profile_is_read_where_it_is_aimed(self):
        self.assertTrue((REPO / "process" / "reader-profile.md").exists())
        for stage in ("01-ideate.md", "03-synthesize.md", "06-draft.md"):
            self.assertIn("process/reader-profile.md",
                          (STAGES / stage).read_text(), stage)

    def test_stage_one_assigns_and_reads_the_attractors(self):
        text = (STAGES / "01-ideate.md").read_text()
        self.assertIn("scripts/assign_ideation.py", text)
        self.assertIn("process/attractors.md", text)
        self.assertIn("process/attractors.md", (STAGES / "02-audit.md").read_text())

    def test_every_stage_one_lens_has_three_entry_points(self):
        for lens in assign_ideation.stage1_panel():
            self.assertGreaterEqual(len(assign_ideation.entry_points(lens)), 3, lens)

    def test_assignment_spreads_pulls_and_is_reproducible(self):
        lenses = assign_ideation.stage1_panel()
        draw = lambda: assign_ideation.assign(lenses, random.Random(1), Counter())
        rows = draw()
        self.assertEqual(rows, draw())
        self.assertEqual([r[0] for r in rows], lenses)
        pulls = Counter(r[2] for r in rows)
        n = len(assign_ideation.pulls())
        self.assertLessEqual(max(pulls.values()), -(-len(lenses) // n))

    def test_no_stimulus_item_goes_to_two_lenses(self):
        lenses = assign_ideation.stage1_panel()
        for seed in range(50):
            rows = assign_ideation.assign(lenses, random.Random(seed), Counter())
            items = [i for r in rows for i in r[3].split(" × ")]
            self.assertEqual(len(items), len(set(items)), f"seed {seed}")

    def test_written_rows_read_back_as_history(self):
        rows = assign_ideation.assign(["asimov", "le-guin"], random.Random(0), Counter())
        for lens, entry, *_ in rows:
            m = assign_ideation.ROW.match(assign_ideation.format_row(lens, entry, *_))
            self.assertIsNotNone(m, lens)
            self.assertEqual((m["lens"], m["entry"]), (lens, entry.split(".")[0]))

    def test_assignment_prefers_the_least_used_entry_point(self):
        used = Counter({("asimov", 1): 2, ("asimov", 2): 1})
        rows = assign_ideation.assign(["asimov"], random.Random(0), used)
        self.assertTrue(rows[0][1].startswith("3. "), rows[0][1])

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
