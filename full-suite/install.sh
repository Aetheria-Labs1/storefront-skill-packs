#!/bin/bash
# Lexsis AI Skill Pack Installer — Lexsis AI — Complete Storefront Suite
# Auto-detects your AI coding platform and installs skills

set -e

PACK_DIR="$(cd "$(dirname "$0")" && pwd)"
INSTALLED=false

echo "╔══════════════════════════════════════════════════╗"
echo "║  Lexsis AI Skill Pack Installer                  ║"
echo "║  Lexsis AI — Complete Storefront Suite         ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Detect platform
if [ -d ".claude" ] || [ -f "CLAUDE.md" ]; then
  echo "✓ Detected: Claude Code"
  mkdir -p .claude/skills .claude/commands
  cp -r "$PACK_DIR/claude/skills/"* .claude/skills/ 2>/dev/null || true
  cp -r "$PACK_DIR/claude/commands/"* .claude/commands/ 2>/dev/null || true
  echo "  → Installed 23 skills + 4 commands"
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
  echo "  → Installed 23 skills"
  INSTALLED=true
fi

if [ -d ".cursor" ]; then
  echo "✓ Detected: Cursor"
  mkdir -p .cursor/rules
  cp -r "$PACK_DIR/cursor/rules/"* .cursor/rules/
  echo "  → Installed 24 rules"
  INSTALLED=true
fi

if [ "$INSTALLED" = false ]; then
  echo "No AI coding platform detected in current directory."
  echo ""
  echo "Manual install options:"
  echo "  Claude Code: cp -r claude/skills/* .claude/skills/"
  echo "  Codex:       cp -r codex/skills/* .agents/skills/"
  echo "  Cursor:      cp -r cursor/rules/* .cursor/rules/"
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
