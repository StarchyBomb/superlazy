---
name: superlazy-mcp
description: Build MCP servers with minimal tokens. Use when creating or modifying an MCP (Model Context Protocol) server integrating any external API or service, in TypeScript or Python.
---

# Superlazy MCP Builder

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Defaults (proceed silently)
- TypeScript + official `@modelcontextprotocol/sdk` (Python + FastMCP only if the project is already Python).
- Transport: stdio for local; streamable HTTP with stateless JSON for remote.
- Docs beat memory: fetch `https://modelcontextprotocol.io/sitemap.xml`, then needed pages with `.md` suffix; SDK README from its GitHub raw. Do this before writing code, silently.

## Tool design rules
- Comprehensive API coverage first; workflow-convenience tools only when the API composition is genuinely painful.
- Names: `service_verb_noun` (`github_create_issue`). Action-oriented, consistent prefix.
- Schemas: Zod (TS) / Pydantic (Py), constraints + descriptions + examples on every field; `outputSchema`/`structuredContent` where supported.
- Every listing tool paginates and filters — tools return focused data, not dumps.
- Errors are actionable: what failed + what the agent should do next.
- Annotations on every tool: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.
- Shared infra once: API client + auth, error helper, response formatter. DRY.

## Verify before ✅
TS: `npm run build` exit 0. Py: `python -m py_compile`. Then exercise the server (MCP Inspector or direct calls) — at least one real call per tool category. Evidence per superlazy-verify.
