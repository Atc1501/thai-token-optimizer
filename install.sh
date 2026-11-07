#!/usr/bin/env bash
# Thai Token Optimizer - Local Setup Script (macOS / Linux)
# Copies SKILL.md from the cloned folder to local skill directories.

set -e
MODE="${1:-skill}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$HOME/.gemini/config/skills/thai-token-optimizer"
mkdir -p "$HOME/.agents/skills/thai-token-optimizer"
mkdir -p "$HOME/.claude/skills/thai-token-optimizer"

cp "$SCRIPT_DIR/SKILL.md" "$HOME/.gemini/config/skills/thai-token-optimizer/SKILL.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.agents/skills/thai-token-optimizer/SKILL.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.claude/skills/thai-token-optimizer/SKILL.md"

echo "[OK] Installed SKILL.md to local skill folders."
