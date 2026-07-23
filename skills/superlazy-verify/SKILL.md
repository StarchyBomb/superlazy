---
name: superlazy-verify
description: Evidence before any completion claim. Use immediately before saying done/fixed/passing, before any ✅, and before committing or creating a PR.
---

# Superlazy Verify

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Iron law
No `✅` without fresh verification evidence from THIS turn. A claim without a just-run command is a lie, not a summary.

## Gate (run silently before every claim)
1. What command proves the claim? (tests / build / lint / running the code / re-testing the original bug symptom). Narrowest command that proves it — full suite only when the claim IS "all tests pass". UI/visual claim → screenshot or rendered-page check, not "the code looks right".
2. Run that command fresh, to completion. Command output likely to run long (full test suite, verbose build) → wrap it: `python skills/superlazy-verify/scripts/summarize.py -- <command>`. Prints everything unchanged if the output was already short; above ~4000 chars it keeps only pass/fail lines, error/failure lines, and their immediate context — exit code always passes through untouched, so this is safe to use as the actual verify command, not just a post-processor.
3. Read the (possibly summarized) output: exit code, failure count, warnings. If the summary omitted something you need (a specific stack trace) — that command's normal output still has it; re-run it unwrapped for just that one case.
4. Output confirms → `✅ <claim>`. Doesn't → fix, or report actual state as one-line `❌`. Never hide or soften a failure.

## Traps
- "should work", "probably", "seems to", "looks correct" → banned words; each one means RUN THE COMMAND.
- Linter clean ≠ build passes. Tests passing ≠ requirements met — recheck the request line by line.
- Previous run ≠ current state. Verify after the LAST edit.
- Subagent reported success → check `git diff`/files yourself before believing it.
- Regression test → verify red-green: it must fail with the fix reverted.
- Tired / "just this once" → no exceptions.
