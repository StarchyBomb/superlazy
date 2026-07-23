---
name: superlazy-context
description: Index-then-retrieve for large files, specs, or docs instead of pasting them whole into context. Use when a doc/spec/log would cost hundreds+ tokens to read in full, when the user says /sc (index) or /uc (retrieve), or asks to "save context on this doc" / "load only what's needed". Lossless — retrieval is verbatim, never summarized.
---

# Superlazy Context

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## When it pays off
- Large reference doc/spec/log where the current task only touches a few sections → index once, retrieve just those.
- Task will touch most of the file anyway → skip this, just Read it normally. The index has no value there — don't index reflexively.

## Silent flow
1. `python skills/superlazy-context/scripts/quantum_compressor.py <file>` → builds `.superlazy-context/compressed_states/Ψ_<hash>.qstate` in the project (CWD), prints the index card: one line per section (id, line range, token estimate, title, extract).
2. Keep only the card in context — never the full file alongside it.
3. Task needs a section → `python skills/superlazy-context/scripts/quantum_decompressor.py <state> <section-id...>` → exact original lines, sha256-verified against the live file. Source changed since indexing → refuses and demands re-index; re-run step 1, never guess from a stale card.
4. Answer only from retrieved text. Card extract alone is a navigation hint, not enough to answer from — retrieve the section.
5. First index in a project → add `.superlazy-context/` to `.gitignore` (generated state, not source).

## Honesty (state plainly when relevant)
- Input tokens only — no effect on output or thinking tokens (superlazy's own output contract already covers those).
- Deferral, not compression: nothing is summarized, so nothing can be hallucinated back. Never quote the card/file ratio as a quality claim.
- Retrieving most/all sections eventually costs slightly more than one plain Read — the win exists only when a task touches a subset.

Mechanism adapted from [supercontexter](https://github.com/StarchyBomb/supercontexter).
