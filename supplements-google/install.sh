#!/bin/bash
# Lexsis AI Skill Pack Installer — Supplements — Google Ads Landing Pages
# Auto-detects your AI coding platform and installs skills

set -e

PACK_DIR="$(cd "$(dirname "$0")" && pwd)"
INSTALLED=false

echo "╔══════════════════════════════════════════════════╗"
echo "║  Lexsis AI Skill Pack Installer                  ║"
echo "║  Supplements — Google Ads Landing Pages        ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Accept --target <dir> or positional arg, else walk up to find project root
TARGET_DIR=""
if [ "$1" = "--target" ] && [ -n "$2" ]; then
  TARGET_DIR="$(cd "$2" && pwd)"
  shift 2
elif [ -n "$1" ] && [ -d "$1" ]; then
  TARGET_DIR="$(cd "$1" && pwd)"
  shift
fi

if [ -z "$TARGET_DIR" ]; then
  # Find the pack's own git root (to skip only that exact repo)
  PACK_GIT_ROOT=""
  _d="$PACK_DIR"
  while [ "$_d" != "/" ]; do
    if [ -d "$_d/.git" ]; then
      PACK_GIT_ROOT="$_d"
      break
    fi
    _d="$(dirname "$_d")"
  done

  # Walk up from CWD to find project root
  SEARCH_DIR="$(pwd)"
  while [ "$SEARCH_DIR" != "/" ]; do
    if [ -d "$SEARCH_DIR/.git" ]; then
      # Skip the pack's own repo, not other ancestors
      if [ "$SEARCH_DIR" = "$PACK_GIT_ROOT" ]; then
        SEARCH_DIR="$(dirname "$SEARCH_DIR")"
        continue
      fi
      if [ -d "$SEARCH_DIR/.claude" ] || [ -f "$SEARCH_DIR/CLAUDE.md" ] || \
         [ -d "$SEARCH_DIR/.agents" ] || [ -f "$SEARCH_DIR/AGENTS.md" ] || \
         [ -d "$SEARCH_DIR/.cursor" ]; then
        TARGET_DIR="$SEARCH_DIR"
        break
      fi
      TARGET_DIR="$SEARCH_DIR"
      break
    fi
    SEARCH_DIR="$(dirname "$SEARCH_DIR")"
  done
fi

if [ -z "$TARGET_DIR" ]; then
  echo "No project root found. Specify your project directory:"
  echo ""
  echo "  $0 --target /path/to/your/project"
  echo ""
  echo "Or run from inside your project:"
  echo "  cd /path/to/your/project && <path-to>/install.sh"
  exit 1
fi

echo "  Target: $TARGET_DIR"
echo ""
cd "$TARGET_DIR"

# Detect platform
if [ -d ".claude" ] || [ -f "CLAUDE.md" ]; then
  echo "✓ Detected: Claude Code"
  mkdir -p .claude/skills .claude/commands
  cp -r "$PACK_DIR/claude/skills/"* .claude/skills/ 2>/dev/null || true
  cp -r "$PACK_DIR/claude/commands/"* .claude/commands/ 2>/dev/null || true
  echo "  → Installed 13 skills + 2 commands"
  INSTALLED=true
fi

if [ -d ".agents" ] || [ -f "AGENTS.md" ]; then
  echo "✓ Detected: OpenAI Codex"
  mkdir -p .agents/skills
  cp -r "$PACK_DIR/codex/skills/"* .agents/skills/
  if [ ! -f "AGENTS.md" ]; then
    cp "$PACK_DIR/codex/AGENTS.md" .
  else
    echo "  ⚠ AGENTS.md exists — merge manually from codex/AGENTS.md"
  fi
  echo "  → Installed 13 skills"
  INSTALLED=true
fi

if [ -d ".cursor" ]; then
  echo "✓ Detected: Cursor"
  mkdir -p .cursor/rules
  cp -r "$PACK_DIR/cursor/rules/"* .cursor/rules/
  echo "  → Installed 14 rules"
  INSTALLED=true
fi

if [ "$INSTALLED" = false ]; then
  echo "No AI coding platform detected in current directory or any parent."
  echo ""
  echo "Options:"
  echo "  1. Run from your project root:  cd /path/to/project && $0"
  echo "  2. Specify target:              $0 --target /path/to/project"
  echo ""
  echo "Manual install:"
  echo "  Claude Code: cp -r $PACK_DIR/claude/skills/* <project>/.claude/skills/"
  echo "  Codex:       cp -r $PACK_DIR/codex/skills/* <project>/.agents/skills/"
  echo "  Cursor:      cp -r $PACK_DIR/cursor/rules/* <project>/.cursor/rules/"
  echo "  GPT:         Upload gpt/knowledge.md as Custom GPT knowledge"
  exit 1
fi

echo ""
echo "━━━ MCP Server Connection ━━━"
echo ""
echo "For full tool access, add this to your .mcp.json:"
echo ""
echo '  "lexsis-ai": {'
echo '    "type": "http",'
echo '    "url": "https://mcp.trylexsis.com/mcp",'
echo '    "headers": { "Authorization": "Bearer <your-api-key>" }'
echo '  }'
echo ""
echo "Get your API key: https://trylexsis.com/settings/api-keys"
echo ""
echo "✓ Installation complete!"
