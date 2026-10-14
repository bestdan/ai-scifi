#!/usr/bin/env python3
"""Email an EPUB to the owner's Kindle over SMTP (Gmail by default).

Usage: python3 scripts/send_to_kindle.py <file.epub>

The sender, the app password and the Kindle address are read from 1Password
with `op read`. Each reference can be overridden by an environment variable:
KINDLE_OP_USER, KINDLE_OP_PASS and KINDLE_OP_TO. Each `op read` runs with
OP_SA_PROFILE=ai-scifi unless the caller already set it. The password is never
printed. KINDLE_SMTP_HOST overrides the server; it must accept SSL on port 465.
"""

import argparse
import os
import smtplib
import ssl
import subprocess
import sys
from email.message import EmailMessage
from pathlib import Path

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
OP_SA_PROFILE = "ai-scifi"

DEFAULT_REFS = {
    "KINDLE_OP_USER": "op://ai-scifi-dev/Gmail/username",
    "KINDLE_OP_PASS": "op://ai-scifi-dev/Gmail/credential",
    "KINDLE_OP_TO": "op://ai-scifi-dev/Gmail/kindle-email",
}


class OpError(RuntimeError):
    pass


def op_ref(var: str, env=None) -> str:
    """Return the 1Password reference for `var`, honouring an env override."""
    env = os.environ if env is None else env
    return env.get(var) or DEFAULT_REFS[var]


def smtp_host(env=None) -> str:
    """Return the SMTP server, honouring KINDLE_SMTP_HOST."""
    env = os.environ if env is None else env
    return env.get("KINDLE_SMTP_HOST") or SMTP_HOST


def op_env(env=None) -> dict:
    """Return a copy of the environment with the ai-scifi 1Password profile set,
    unless the caller already chose one."""
    env = dict(os.environ if env is None else env)
    env.setdefault("OP_SA_PROFILE", OP_SA_PROFILE)
    return env


def op_read(ref: str) -> str:
    try:
        result = subprocess.run(["op", "read", ref], capture_output=True, text=True,
                                env=op_env())
    except FileNotFoundError as e:
        raise OpError("the `op` command was not found") from e
    if result.returncode != 0:
        # The reference names a field, not its value, so it is safe to show.
        raise OpError(f"`op read` failed for {ref}: {result.stderr.strip()}")
    return result.stdout.strip()


def build_message(epub: Path, data: bytes, sender: str, recipient: str) -> EmailMessage:
    """Build the email carrying `data` as `epub`'s attachment. Pure: no I/O."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = f"Book: {epub.stem}"
    msg.set_content(f"{epub.name}, sent from ai-scifi.\n")
    msg.add_attachment(data, maintype="application", subtype="epub+zip",
                       filename=epub.name)
    return msg


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Email an EPUB to the owner's Kindle.")
    parser.add_argument("epub", type=Path, help="the .epub file to send")
    args = parser.parse_args(argv)

    if not args.epub.is_file():
        print(f"send_to_kindle: no such file: {args.epub}", file=sys.stderr)
        return 1

    try:
        user = op_read(op_ref("KINDLE_OP_USER"))
        password = op_read(op_ref("KINDLE_OP_PASS"))
        recipient = op_read(op_ref("KINDLE_OP_TO"))
    except OpError as e:
        print(f"send_to_kindle: {e}\n"
              "Run this command unsandboxed, and run `op-sa check` to confirm "
              "the ai-scifi 1Password profile's token.", file=sys.stderr)
        return 2

    msg = build_message(args.epub, args.epub.read_bytes(), user, recipient)
    with smtplib.SMTP_SSL(smtp_host(), SMTP_PORT, context=ssl.create_default_context()) as s:
        s.login(user, password)
        s.send_message(msg)
    print(f"sent {args.epub.name} to the Kindle")
    return 0


if __name__ == "__main__":
    sys.exit(main())
