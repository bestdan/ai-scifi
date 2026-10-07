#!/bin/sh
# Print the agent-guidance plugin root, for the shared dev-docs-layout.py check.
# Order: $AGENT_GUIDANCE_DIR, the dotfiles resolver, then the installed plugin
# record. Fails (exit 1) rather than printing nothing, so a missing root fails
# `just check` instead of skipping the check.
set -eu
if [ -n "${AGENT_GUIDANCE_DIR:-}" ]; then
  echo "$AGENT_GUIDANCE_DIR"
  exit 0
fi
resolver="$HOME/src/dotfiles/agents/agent-guidance-dir.sh"
if [ -x "$resolver" ] && root="$("$resolver")" && [ -n "$root" ]; then
  echo "$root"
  exit 0
fi
record="$HOME/.claude/plugins/installed_plugins.json"
if [ -f "$record" ]; then
  root="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["plugins"]["agent-guidance@agent-guidance"][0]["installPath"])' "$record" 2>/dev/null || true)"
  if [ -n "$root" ]; then
    echo "$root"
    exit 0
  fi
fi
echo "agent-guidance-dir.sh: cannot find the agent-guidance plugin root" >&2
exit 1
