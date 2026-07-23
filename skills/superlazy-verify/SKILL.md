---
name: superlazy-verify
description: Evidence before any completion claim. Use immediately before saying done/fixed/passing, before any ✅, and before committing or creating a PR.
---

# Superlazy Verify

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Iron law
No `✅` without fresh verification evidence from THIS turn. A claim without a just-run command is a lie, not a summary.

## Gate (run silently before every claim)
1. What command proves the claim? (tests / build / lint / running the code / re-testing the original bug symptom)
2. Run the FULL command, fresh.
3. Read the output: exit code, failure count, warnings.
4. Output confirms → `✅ <claim>`. Doesn't → fix, or report actual state as one-line `❌`. Never hide or soften a failure.

## Traps
- "should work", "probably", "seems to", "looks correct" → banned words; each one means RUN THE COMMAND.
- Linter clean ≠ build passes. Tests passing ≠ requirements met — recheck the request line by line.
- Previous run ≠ current state. Verify after the LAST edit.
- Subagent reported success → check `git diff`/files yourself before believing it.
- Regression test → verify red-green: it must fail with the fix reverted.
- Tired / "just this once" → no exceptions.
