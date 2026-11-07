#!/usr/bin/env bash
# Thai Token Optimizer v2.0 - Universal One-Line Installer (macOS / Linux)
# Usage: curl -fsSL https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.sh | bash

set -e
SKILL_URL="https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/SKILL.md"

TARGET_DIRS=(
  "$HOME/.gemini/config/skills/thai-token-optimizer"
  "$HOME/.agents/skills/thai-token-optimizer"
  "$HOME/.claude/skills/thai-token-optimizer"
)

echo "Installing Thai Token Optimizer v2.0..."

for dir in "${TARGET_DIRS[@]}"; do
  mkdir -p "$dir"
  curl -fsSL "$SKILL_URL" -o "$dir/SKILL.md"
  echo "  [OK] Installed -> $dir/SKILL.md"
done

echo ""
echo "Done! Thai Token Optimizer v2.0 is now active across Antigravity, Gemini CLI, Codex, and Claude Code."
