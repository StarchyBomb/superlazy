---
name: superlazy-tdd
description: Silent test-driven development. Use when implementing any feature or bugfix in a project that has a test setup, before writing implementation code.
---

# Superlazy TDD

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Iron law
Project has test infra → no production code without a failing test first. No test infra → run the code once to verify instead; never add a test framework uninvited.

## Silent cycle
1. **RED** — write ONE minimal test for the behavior: clear name, real code (mocks only if unavoidable), one assertion focus. Wished-for API is allowed.
2. **Verify RED** — run it. Must FAIL for the right reason (feature missing, not typo/error). Passes immediately = it tests nothing; fix the test.
3. **GREEN** — simplest code that passes. No extra features, options, or "improvements" beyond the test.
4. **Verify GREEN** — run test + suite. All pass, output clean. Test fails → fix code, not test.
5. **REFACTOR** — only if it deletes lines or duplication. Stay green.
6. Repeat per behavior. Bug fix = failing test reproducing the bug first, always.

## Cut points (lazy but honest)
- One test per behavior the request implies — not per imaginary edge case.
- Code written before its test? Delete it, restart from the test. Don't "keep as reference".
- Hard to test = design too complicated → simplify the interface, don't pile up mocks.
- Never claim tested without having run the command this session (see superlazy-verify).
