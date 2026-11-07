#!/usr/bin/env bash
# Thai Token Optimizer v2.1 - Dual-Mode Installer & Mode Switcher (macOS / Linux)
# Usage:
#   Interactive Menu : bash install.sh
#   Mode 1 (Skill)   : bash install.sh skill
#   Mode 2 (AlwaysOn): bash install.sh always-on
#   Disable AlwaysOn : bash install.sh disable
#   Uninstall All    : bash install.sh uninstall

set -e
MODE="${1:-menu}"
SKILL_URL="https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/SKILL.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_SKILL="$SCRIPT_DIR/SKILL.md"

SKILL_DIRS=(
  "$HOME/.gemini/config/skills/thai-token-optimizer"
  "$HOME/.agents/skills/thai-token-optimizer"
  "$HOME/.claude/skills/thai-token-optimizer"
)

GLOBAL_RULE_FILES=(
  "$HOME/.gemini/config/GEMINI.md"
  "$HOME/.claude/CLAUDE.md"
  "$HOME/.agents/AGENTS.md"
)

START_MARKER="<!-- THAI_TOKEN_OPTIMIZER_START -->"
END_MARKER="<!-- THAI_TOKEN_OPTIMIZER_END -->"

read -r -d '' RULE_BLOCK << 'EOF' || true
<!-- THAI_TOKEN_OPTIMIZER_START -->
# Thai Token Optimizer v2.1 (Always-On Golden Ratio)

When the user communicates in Thai:
1. **Backend Reasoning**: Conduct all internal thinking (`<thinking>`), planning, and technical analysis in natural English (saves ~70% reasoning tokens while keeping 100% intelligence).
2. **Direct Thai Output**: Reply in natural, direct Thai. Omit ceremonial greetings (`สวัสดีครับ/ค่ะ`) and never echo the user's question back. Use bullet points or numbered steps.
3. **Technical Terms**: Keep coding, architecture, and system terms in standard English (`Config`, `Database`, `API`, `Function`).
4. **Code & Git Hygiene**: Write all inline code comments, docstrings, logs, and Git commit messages in concise English (use Thai only for user-facing UI strings).
5. **Subagents & Memory**: Communicate with subagents and store internal scratchpads/memory in concise English; summarize to the user in Thai.
<!-- THAI_TOKEN_OPTIMIZER_END -->
EOF

install_skill_files() {
  for dir in "${SKILL_DIRS[@]}"; do
    mkdir -p "$dir"
    if [ -f "$LOCAL_SKILL" ]; then
      cp "$LOCAL_SKILL" "$dir/SKILL.md"
    else
      curl -fsSL "$SKILL_URL" -o "$dir/SKILL.md"
    fi
  done
  echo "  [OK] Installed On-Demand Skill (@thai-token-optimizer)"
}

remove_always_on_rule() {
  for file in "${GLOBAL_RULE_FILES[@]}"; do
    if [ -f "$file" ] && grep -q "$START_MARKER" "$file"; then
      sed -i.bak "/$START_MARKER/,/$END_MARKER/d" "$file"
      rm -f "$file.bak"
      echo "  [OK] Removed Always-On Rule from -> $file"
    fi
  done
}

enable_always_on_rule() {
  remove_always_on_rule
  for file in "${GLOBAL_RULE_FILES[@]}"; do
    mkdir -p "$(dirname "$file")"
    if [ -f "$file" ] && [ -s "$file" ]; then
      printf "\n\n%s\n" "$RULE_BLOCK" >> "$file"
    else
      printf "%s\n" "$RULE_BLOCK" > "$file"
    fi
    echo "  [OK] Enabled Always-On Global Rule -> $file"
  done
}

show_status() {
  local skill_installed="NOT INSTALLED"
  local always_on="INACTIVE (OFF)"
  [ -f "$HOME/.gemini/config/skills/thai-token-optimizer/SKILL.md" ] && skill_installed="INSTALLED"
  if [ -f "$HOME/.gemini/config/GEMINI.md" ] && grep -q "$START_MARKER" "$HOME/.gemini/config/GEMINI.md"; then
    always_on="ACTIVE (ON)"
  fi
  echo ""
  echo "============================================================"
  echo " THAI TOKEN OPTIMIZER - CURRENT STATUS"
  echo "============================================================"
  echo "  • On-Demand Skill (@thai-token-optimizer) : $skill_installed"
  echo "  • Always-On Global Rule (Auto every chat) : $always_on"
  echo "============================================================"
  echo ""
}

if [ "$MODE" = "menu" ]; then
  show_status
  echo "Select Mode:"
  echo "  [1] Mode 1: On-Demand Skill Only (เรียกใช้เมื่อพิมพ์ @thai-token-optimizer)"
  echo "  [2] Mode 2: Always-On Global Rule (ทำงานอัตโนมัติทุกแชทตั้งแต่วินาทีแรก)"
  echo "  [3] Disable Always-On (ยกเลิก Always-On กลับไปเป็นโหมดเรียกใช้เอง)"
  echo "  [4] Uninstall All (ถอนการติดตั้งทั้งหมด)"
  echo "  [5] Check Status Only (ดูสถานะปัจจุบัน)"
  read -r -p "Enter number (1-5): " choice
  case "$choice" in
    1) MODE="skill" ;;
    2) MODE="always-on" ;;
    3) MODE="disable" ;;
    4) MODE="uninstall" ;;
    *) MODE="status" ;;
  esac
fi

case "$MODE" in
  skill)
    install_skill_files
    remove_always_on_rule
    show_status
    ;;
  always-on)
    install_skill_files
    enable_always_on_rule
    show_status
    ;;
  disable)
    remove_always_on_rule
    show_status
    ;;
  uninstall)
    remove_always_on_rule
    for dir in "${SKILL_DIRS[@]}"; do rm -rf "$dir"; done
    show_status
    ;;
  *)
    show_status
    ;;
esac
