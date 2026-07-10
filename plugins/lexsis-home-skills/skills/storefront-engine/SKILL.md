---
name: storefront-engine
description: Core orchestrator for Lexsis AI storefront page generation. Routes requests to the correct workflow, manages tool sequencing, and loads reference knowledge on demand. Auto-invoked by commands and agents.
allowed-tools: mcp__lexsis-ai__*
---

# Storefront Engine — Core Orchestrator

This is the routing and orchestration layer for all Lexsis AI storefront operations. It determines the correct workflow based on user input and coordinates tool calls in the optimal sequence.

## How This Works

1. **Commands** (generate, optimize, remix, experiment, cart, publish) invoke this skill automatically
2. **Agents** (cro-analyzer, page-builder) have their own orchestration logic
3. **Reference files** in `reference/` contain deep knowledge — load ONLY what you need

---



---

## Reference Files

Load these with `Read reference/{name}.md` when you need specific knowledge. Do NOT load all at once.

### Knowledge (domain expertise)
- **home-expertise.md** — **Context is everything.** Home goods buyers need to see the product in a real space before they can

### Operational (workflow procedures)

