---
name: superlazy-plan
description: Silent planning and execution for multi-step tasks. Use when a task spans several files/steps, or when a written plan exists and must be executed.
---

# Superlazy Plan

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Writing plans
- Default: plan is INTERNAL — head or scratchpad file. Never shown to the user.
- Write a plan document ONLY when the work spans sessions/subagents or the user asks. Save to `docs/plans/YYYY-MM-DD-<name>.md`.
- Written plans: exact file paths, real code in every code step (no "TBD"/"add validation"/"similar to Task N"), exact commands with expected output, task = smallest independently testable unit, interfaces between tasks spelled out (exact signatures). DRY, YAGNI, TDD, frequent commits.
- Self-check before use: every spec requirement has a task; no placeholders; names/types consistent across tasks. Fix inline, don't re-review.

## Executing plans
- Read the plan once, question it critically — contradictions or gaps → ONE batched blocking question before starting, not per-discovery interrupts.
- Execute every task in order without pausing to ask "continue?". Follow steps exactly; run every verification listed.
- Stop ONLY for: real blocker, genuinely ambiguous instruction, or all tasks done. Blocked → one-line question; done → `✅`.
- Independent tasks + subagent support available → prefer superlazy-subagents.
- Never start on main/master without explicit user consent (see superlazy-worktree).
