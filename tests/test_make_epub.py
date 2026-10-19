import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("make_epub", ROOT / "scripts" / "make_epub.py")
me = importlib.util.module_from_spec(spec)
spec.loader.exec_module(me)

FAKE_JPEG = b"\xff\xd8\xff\xe0fake-jpeg"


def temp_dir(test: unittest.TestCase) -> Path:
    d = tempfile.TemporaryDirectory()
    test.addCleanup(d.cleanup)
    return Path(d.name)


class BuildTest(unittest.TestCase):
    def build(self, cover):
        tmp = temp_dir(self)
        src = tmp / "final.md"
        src.write_text("# The Long Tide\n\nIt began.\n", encoding="utf-8")
        out = tmp / "out.epub"
        me.build(src, out, author="ai-scifi", cover=cover)
        z = zipfile.ZipFile(out)
        self.addCleanup(z.close)
        return z

    def test_cover_is_declared_both_ways(self):
        z = self.build(FAKE_JPEG)
        opf = z.read("OEBPS/content.opf").decode()
        self.assertIn('properties="cover-image"', opf)
        self.assertIn('<meta name="cover" content="cover-image"/>', opf)
        self.assertIn('<reference type="cover"', opf)
        self.assertIn('<spine><itemref idref="cover"/><itemref idref="story"/>', opf)
        self.assertEqual(z.read("OEBPS/cover.jpg"), FAKE_JPEG)
        self.assertIn('epub:type="cover"', z.read("OEBPS/nav.xhtml").decode())

    def test_no_cover(self):
        z = self.build(None)
        opf = z.read("OEBPS/content.opf").decode()
        self.assertNotIn("cover", opf)
        self.assertNotIn("OEBPS/cover.jpg", z.namelist())

    def test_mimetype_first_and_stored(self):
        first = self.build(FAKE_JPEG).infolist()[0]
        self.assertEqual(first.filename, "mimetype")
        self.assertEqual(first.compress_type, zipfile.ZIP_STORED)


class MainTest(unittest.TestCase):
    def test_rendered_cover_reaches_the_epub(self):
        tmp = temp_dir(self)
        src = tmp / "final.md"
        src.write_text("# The Long Tide\n\nIt began.\n", encoding="utf-8")
        out = tmp / "out.epub"
        with mock.patch.object(me, "render_cover", return_value=FAKE_JPEG) as render, \
             mock.patch("sys.argv", ["make_epub.py", str(src), str(out)]), \
             mock.patch("sys.stdout"):
            me.main()
        render.assert_called_once_with("The Long Tide", "ai-scifi")
        with zipfile.ZipFile(out) as z:
            self.assertEqual(z.read("OEBPS/cover.jpg"), FAKE_JPEG)


class RenderCoverTest(unittest.TestCase):
    def test_no_uv_builds_without_cover(self):
        with mock.patch.object(me.shutil, "which", return_value=None), \
             mock.patch("sys.stderr"):
            self.assertIsNone(me.render_cover("T", "A"))

    def test_failed_render_builds_without_cover(self):
        failed = mock.Mock(returncode=1, stderr="boom")
        with mock.patch.object(me.shutil, "which", return_value="/bin/uv"), \
             mock.patch.object(me.subprocess, "run", return_value=failed), \
             mock.patch("sys.stderr"):
            self.assertIsNone(me.render_cover("T", "A"))


if __name__ == "__main__":
    unittest.main()
