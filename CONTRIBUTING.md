# Contributing

## Adding a New Vertical

1. Create the knowledge skill in the source repo:
   ```
   services/storefront-blueprint-mcp/skills/_knowledge/vertical-{name}.md
   ```

2. Follow the format of existing verticals (see `vertical-beauty.md`):
   - Section patterns specific to the industry
   - Copy tone and vocabulary
   - Product display patterns
   - Conversion tactics unique to the niche
   - Anti-patterns to avoid

3. Create a manifest in `skill-packs/manifests/`:
   ```json
   {
     "id": "vertical-{name}",
     "name": "Lexsis AI — {Name} Vertical",
     "version": "2.0.0",
     "description": "Industry-specific patterns for {name} brands.",
     "category": "vertical",
     "skills": {
       "knowledge": [{ "source": "skills/_knowledge/vertical-{name}.md", "name": "{name}-expertise" }],
       "operational": []
     },
     "commands": []
   }
   ```

4. Build and validate:
   ```bash
   cd skill-packs
   npm run build
   npm run validate
   ```

5. Copy output to this repo:
   ```bash
   cp -r dist/vertical-{name} ../storefront-skill-packs/verticals/{name}
   ```

## Adding a New Traffic Source

Same process as verticals, but:
- Source file: `skills/_knowledge/traffic-source-{platform}.md`
- Manifest category: `"traffic-source"`
- Output directory: `traffic-sources/{platform}-ads/`

## Adding New Operational Skills to Core

1. Create in `skills/_operational/{skill-name}.md`
2. Add to `manifests/core.json` under `skills.operational`
3. Add a command entry if it should have a slash command
4. Build + validate + copy `dist/core` to this repo's `core/`

## Skill Format

All skills use YAML frontmatter:

```markdown
---
name: skill-name
description: Trigger description with keywords
---

# Title

Content...
```

Constraints:
- Max 480 lines per skill (auto-chunked if larger)
- Must have `name` and `description` in frontmatter
- Operational skills should reference `vibe://skills/generation-protocol`

## Testing

After copying to this repo, verify:
```bash
# Check each platform output exists
ls core/claude/skills/
ls core/codex/skills/
ls core/cursor/rules/
ls core/gpt/

# Test installer
cd core && ./install.sh
```
