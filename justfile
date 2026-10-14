# Repo checks and hooks. `dli check` runs the `check` recipe.

# Run every test, lint every finished story, and check the dev_docs/ layout.
check:
    python3 -m unittest discover -s tests -q
    python3 scripts/lint_prose.py --quiet stories/*/final.md
    python3 "$(scripts/agent-guidance-dir.sh)/scripts/dev-docs-layout.py" "$PWD"

# Lint story files strictly against process/prose-rules.toml.
lint +FILES:
    python3 scripts/lint_prose.py {{FILES}}

# Build a story's EPUB if it is missing, then email it to the owner's Kindle.
kindle SLUG:
    #!/bin/sh
    set -eu
    src="stories/{{SLUG}}/final.md"
    title="$(sed -n 's/^# //p' "$src" | head -n 1)"
    epub="stories/{{SLUG}}/${title:-Untitled}.epub"
    [ -f "$epub" ] || python3 scripts/make_epub.py "$src" "$epub"
    python3 scripts/send_to_kindle.py "$epub"

# Install the pre-commit shim into the shared git dir (covers every worktree).
install-hooks:
    #!/bin/sh
    set -eu
    hook="$(git rev-parse --git-common-dir)/hooks/pre-commit"
    mkdir -p "$(dirname "$hook")"
    cp scripts/hooks/pre-commit-shim "$hook"
    chmod +x "$hook"
    echo "installed $hook"
