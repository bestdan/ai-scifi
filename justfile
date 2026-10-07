# Repo checks and hooks. `dli check` runs the `check` recipe.

# Run every test, lint every finished story, and check the dev_docs/ layout.
check:
    python3 -m unittest discover -s tests -q
    python3 scripts/lint_prose.py --quiet stories/*/final.md
    python3 "$(scripts/agent-guidance-dir.sh)/scripts/dev-docs-layout.py" "$PWD"

# Lint story files strictly against process/prose-rules.toml.
lint +FILES:
    python3 scripts/lint_prose.py {{FILES}}

# Install the pre-commit shim into the shared git dir (covers every worktree).
install-hooks:
    #!/bin/sh
    set -eu
    hook="$(git rev-parse --git-common-dir)/hooks/pre-commit"
    mkdir -p "$(dirname "$hook")"
    cp scripts/hooks/pre-commit-shim "$hook"
    chmod +x "$hook"
    echo "installed $hook"
