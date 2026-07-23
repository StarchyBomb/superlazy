---
name: superlazy-debug
description: Silent root-cause debugging. Use on any bug, test failure, build failure, or unexpected behavior, BEFORE proposing or writing any fix.
---

# Superlazy Debug

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Iron law
No fix without root cause. Symptom patches are failure — and cost more tokens later.

## Silent process
1. **Evidence first** — read the FULL error/stack trace (it often contains the answer), reproduce reliably, check recent changes (`git diff`, new deps, config).
2. **Trace to origin** — bad value deep in the stack? Trace backward: who produced it, who called that, until the source. Fix at the source, never where it crashed. Multi-component systems: log data at each boundary once, find the failing layer, then dig there.
3. **One hypothesis, one change** — state it to yourself ("X causes this because Y"), make the SMALLEST change that tests it. Never stack multiple fixes.
4. **Fix via test** — write a failing test reproducing the bug (superlazy-tdd), implement the single root-cause fix, verify test + suite green. No "while I'm here" extras.

## Stop conditions
- Fix didn't work → back to step 1 with the new evidence. Don't pile fix #2 on top.
- 3 failed fixes, or the fix keeps growing in unexpected places → the architecture is wrong, not the hypothesis. STOP; ask the user one batched blocking question with your architectural finding.
- Truly environmental/flaky after full investigation → add the appropriate retry/timeout/logging and note it in the ✅ line. (95% of "no root cause" is incomplete investigation — be sure.)
