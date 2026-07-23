---
name: superlazy-subagents
description: Silent subagent-driven plan execution. Use when executing an implementation plan with independent tasks and subagent support is available.
---

# Superlazy Subagents

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Loop (per task, no user check-ins between tasks)
1. Extract the task's text to a brief FILE. Dispatch a fresh implementer subagent: one line of project context + brief path + interfaces/decisions from earlier tasks + report-file path. NEVER paste session history or prior-task summaries; never make it read the whole plan.
2. Implementer questions → answer, re-dispatch. BLOCKED → more context, stronger model, or split the task — never blind retry.
3. Review the task: generate diff as a FILE (`git diff BASE..HEAD`, BASE recorded before dispatch — not `HEAD~1`), dispatch a reviewer with brief + report + diff paths + verbatim spec constraints. Never pre-judge findings ("don't flag X") in the prompt.
4. Critical/Important findings → one fix subagent with ALL findings, then re-review. Minor → ledger.
5. Append to ledger file (`.superlazy/progress.md`): `Task N: complete (commits X..Y)`. Ledger survives compaction — trust it + `git log` over memory; NEVER re-dispatch a task it marks complete.
6. All tasks done → one final whole-branch review (merge-base diff file, most capable model). Findings → ONE fixer for the full list. Then `✅`.

## Cost rules
- Cheapest model that fits, stated explicitly per dispatch: transcription-from-plan/1-file fixes → cheapest; multi-file integration or prose-spec implementers and reviewers → mid-tier; architecture + final review → most capable. Turn count beats token price — too-cheap models take 2-3× turns.
- Artifacts move as files (brief, report, diff), never pasted text.
- Every subagent prompt embeds the superlazy output contract: write findings to the report file, reply ≤1 line. Verbose subagent replies are billed output.
- Never dispatch implementers in parallel (conflicts). Never skip re-review after fixes.
