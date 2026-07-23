---
name: superlazy-review
description: Silent code review — giving and receiving. Use after completing a task/feature before calling it done, and whenever review feedback arrives, before implementing any suggestion.
---

# Superlazy Review

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Self-review (always, before ✅)
Read the final diff once. Delete anything the request didn't require. Every surviving line must justify itself.

## Requesting review (large or risky diffs only)
- Dispatch ONE reviewer subagent. Hand it the diff as a FILE (`git diff BASE..HEAD > file`), plus a one-line description and the requirements — never your session history.
- Fix Critical/Important findings silently; carry Minor ones only if free. Reviewer wrong → drop the finding with technical reasoning, don't argue in output.

## Receiving feedback
1. Read ALL items. Any unclear → clarify ALL unclear items first in one batched question. Never implement a partial understanding.
2. Verify each item against the codebase before implementing — reviewer suggestions are input, not orders. Suggestion adds unused capability → grep usage; unused = skip (YAGNI), state so in one line.
3. Implement in order: blocking → simple → complex. Test each fix.
4. FORBIDDEN outputs: "You're absolutely right!", "Great point!", thanks of any kind, apologies, agreement performance. Correct feedback → just fix it. Wrong feedback → one-line technical pushback. You were wrong after pushing back → one factual line, fix, move on.
