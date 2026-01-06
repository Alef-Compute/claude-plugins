#!/bin/bash
# setup_env.sh - Automatic environment setup for legal-assistant plugin
# Called by SessionStart hook - runs once per session

set -e

# Export CLAUDE_PLUGIN_ROOT so it persists for all bash commands
printf 'export CLAUDE_PLUGIN_ROOT=%q\n' "${CLAUDE_PLUGIN_ROOT}" >> "$CLAUDE_ENV_FILE"

# Create workspace directory using CLAUDE_PROJECT_DIR (set by Claude Code)
WORKSPACE_DIR="${CLAUDE_PROJECT_DIR}/.claude/workspace"
mkdir -p "$WORKSPACE_DIR"
printf 'export WORKSPACE_DIR=%q\n' "$WORKSPACE_DIR" >> "$CLAUDE_ENV_FILE"

# Find docx skill in common locations
DOCX_SKILL=""
for path in \
    "$HOME/.claude/plugins/marketplaces/anthropic-agent-skills/skills/docx" \
    "$HOME/.claude/plugins/marketplaces/example-skills/skills/docx"; do
    if [ -f "$path/SKILL.md" ]; then
        DOCX_SKILL="$path"
        break
    fi
done

if [ -z "$DOCX_SKILL" ]; then
    echo "Warning: Docx skill not found. Install anthropic-agent-skills for redlining support."
    exit 0  # Don't fail session start
fi

# Export docx skill path
printf 'export DOCX_SKILL=%q\n' "$DOCX_SKILL" >> "$CLAUDE_ENV_FILE"

# Ensure uv is available
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Ensure Python 3.10+
if ! uv python find 3.10 &>/dev/null 2>&1; then
    uv python install 3.10
fi

# Create venv in docx skill directory if needed
if [ ! -d "$DOCX_SKILL/.venv" ]; then
    (cd "$DOCX_SKILL" && uv venv --python 3.10)
fi

# Install dependencies (defusedxml and lxml required by docx skill)
(cd "$DOCX_SKILL" && uv pip install -q defusedxml lxml 2>/dev/null || true)

# Auto-activate venv for all bash commands
printf 'source %q 2>/dev/null || true\n' "$DOCX_SKILL/.venv/bin/activate" >> "$CLAUDE_ENV_FILE"

# Check pandoc
if ! command -v pandoc &> /dev/null; then
    echo "Warning: pandoc not found. Install with: brew install pandoc"
fi

echo "Legal assistant environment configured."
echo "  Workspace: $WORKSPACE_DIR"
echo "  Docx skill: $DOCX_SKILL"
