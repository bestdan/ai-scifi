import importlib.util
import io
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "send_to_kindle", ROOT / "scripts" / "send_to_kindle.py")
stk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stk)


class BuildMessageTest(unittest.TestCase):
    def setUp(self):
        self.msg = stk.build_message(Path("stories/x/The Long Tide.epub"), b"PK-data",
                                     "sender@example.com", "reader@example.com")

    def test_addresses(self):
        self.assertEqual(self.msg["To"], "reader@example.com")
        self.assertEqual(self.msg["From"], "sender@example.com")

    def test_subject_names_book(self):
        self.assertIn("The Long Tide", self.msg["Subject"])

    def test_attachment(self):
        atts = list(self.msg.iter_attachments())
        self.assertEqual(len(atts), 1)
        self.assertEqual(atts[0].get_content_type(), "application/epub+zip")
        self.assertEqual(atts[0].get_filename(), "The Long Tide.epub")
        self.assertEqual(atts[0].get_content(), b"PK-data")


class OpRefTest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(stk.op_ref("KINDLE_OP_USER", {}),
                         "op://ai-scifi-dev/Gmail/username")
        self.assertEqual(stk.op_ref("KINDLE_OP_PASS", {}),
                         "op://ai-scifi-dev/Gmail/credential")
        self.assertEqual(stk.op_ref("KINDLE_OP_TO", {}),
                         "op://ai-scifi-dev/Gmail/kindle-email")

    def test_env_overrides(self):
        env = {"KINDLE_OP_USER": "op://v/i/u", "KINDLE_OP_PASS": "op://v/i/p",
               "KINDLE_OP_TO": "op://v/i/t"}
        for var, ref in env.items():
            self.assertEqual(stk.op_ref(var, env), ref)


class SmtpHostTest(unittest.TestCase):
    def test_default_is_gmail(self):
        self.assertEqual(stk.smtp_host({}), "smtp.gmail.com")

    def test_env_override(self):
        self.assertEqual(stk.smtp_host({"KINDLE_SMTP_HOST": "smtp.example.com"}),
                         "smtp.example.com")


class OpEnvTest(unittest.TestCase):
    def test_default_profile(self):
        env = stk.op_env({"PATH": "/bin"})
        self.assertEqual(env["OP_SA_PROFILE"], "ai-scifi")
        self.assertEqual(env["PATH"], "/bin")

    def test_caller_profile_wins(self):
        self.assertEqual(stk.op_env({"OP_SA_PROFILE": "other"})["OP_SA_PROFILE"], "other")

    def test_copy_not_mutation(self):
        src = {}
        stk.op_env(src)
        self.assertEqual(src, {})

    def test_op_read_passes_env(self):
        seen = {}

        def fake_run(cmd, **kw):
            seen.update(cmd=cmd, env=kw.get("env"))
            return mock.Mock(returncode=0, stdout="value\n", stderr="")

        with mock.patch.dict(stk.os.environ, {}, clear=True), \
                mock.patch.object(stk.subprocess, "run", fake_run):
            self.assertEqual(stk.op_read("op://v/i/f"), "value")
        self.assertEqual(seen["cmd"], ["op", "read", "op://v/i/f"])
        self.assertEqual(seen["env"]["OP_SA_PROFILE"], "ai-scifi")


class MainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.epub = Path(self.tmp.name) / "The Long Tide.epub"
        self.epub.write_bytes(b"PK-data")
        self.stderr = io.StringIO()
        for name, stream in (("stderr", self.stderr), ("stdout", io.StringIO())):
            patcher = mock.patch.object(stk.sys, name, stream)
            patcher.start()
            self.addCleanup(patcher.stop)

    def op_ok(self, cmd, **kw):
        return mock.Mock(returncode=0, stdout="secret-" + cmd[-1].rsplit("/", 1)[-1],
                         stderr="")

    def test_missing_file(self):
        with mock.patch.object(stk.subprocess, "run") as run:
            self.assertEqual(stk.main([str(Path(self.tmp.name) / "nope.epub")]), 1)
        run.assert_not_called()

    def test_op_read_fails(self):
        failed = mock.Mock(returncode=1, stdout="", stderr="boom")
        with mock.patch.object(stk.subprocess, "run", return_value=failed):
            self.assertEqual(stk.main([str(self.epub)]), 2)

    def test_op_missing(self):
        with mock.patch.object(stk.subprocess, "run", side_effect=FileNotFoundError):
            self.assertEqual(stk.main([str(self.epub)]), 2)

    def test_sends(self):
        smtp = mock.MagicMock()
        with mock.patch.object(stk.subprocess, "run", self.op_ok), \
                mock.patch.object(stk.smtplib, "SMTP_SSL", smtp):
            self.assertEqual(stk.main([str(self.epub)]), 0)
        server = smtp.return_value.__enter__.return_value
        server.login.assert_called_once_with("secret-username", "secret-credential")
        server.send_message.assert_called_once()

    def test_smtp_failure_hides_password(self):
        smtp = mock.MagicMock()
        smtp.return_value.__enter__.return_value.login.side_effect = \
            stk.smtplib.SMTPAuthenticationError(535, b"bad login")
        with mock.patch.object(stk.subprocess, "run", self.op_ok), \
                mock.patch.object(stk.smtplib, "SMTP_SSL", smtp):
            self.assertEqual(stk.main([str(self.epub)]), 3)
        self.assertIn("bad login", self.stderr.getvalue())
        self.assertNotIn("secret-credential", self.stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
