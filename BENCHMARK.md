# Benchmark — A/B test on planted bugs

Two identical copies of a small Python project, same prompts verbatim, one Claude Code session each: **A = superlazy skills on**, **B = baseline (skills off)**. Sonnet 5, 2026-07-23.

## Test project

`cart.py` + `test_cart.py` (unittest, 8 tests, 5 failing) with 3 planted bugs of increasing difficulty:

1. **Boundary** — `apply_discount` used `> 1000`; spec says "1000.00 **or more**" (`>=`)
2. **Mutable default** — `new_cart(items=[])` shared one list across all carts
3. **Root cause far from symptom** — `parse_price` swapped comma/dot European-style (`"590.00"` → `59000.0`); the failing test was downstream on `order_total`. Tests whether the fix lands at the source or gets patched at the crash site.

## Prompts (identical, both sessions)

1. `Some tests are failing. Fix cart.py so all tests pass. Do not modify test_cart.py.`
2. `Add a coupon feature to cart.py: apply_coupon(total, code) — code "SAVE50" takes 50.00 off (total can't go below 0), unknown codes raise ValueError. Cover it with tests.`
3. `Refactor cart.py: prices should be stored as integer satang (1/100 THB) internally to avoid float errors, while keeping all public function signatures and all existing tests passing.`

## Results

| | A — superlazy | B — baseline |
|---|---|---|
| Session cost | **$0.53** | $0.98 * |
| API time | 1m 15s | 3m 10s |
| Output tokens | 325 | 745 |
| Lines changed | +94 −14 | +48 −18 * |
| Final tests | **11/11 pass** | invalid * |
| Root-cause quality | all 3 bugs fixed at source (parse_price fixed at origin, not patched at `order_total`); coupon + satang refactor correct | invalid * |

\* **Baseline run invalid**: the session's edits landed outside the test folder (wrong working directory) — its `cart.py` was never modified, so $0.98 / +48 −18 cannot be attributed to completing the task. Cost and output-token gap are indicative only until the baseline is rerun correctly.

## Verified so far

- With skills on, quality did not degrade: root-cause fixes, TDD-added coupon tests, refactor kept all signatures — 11/11 green.
- Visible output stayed within the ≤3-line contract while completing 3 rounds.
- **Not yet verified**: the cost delta vs a valid baseline. Rerun pending.

## Reproduce

Recreate the two folders from the bug descriptions above (or any equivalent planted-bug project), `git init` each, run the three prompts in separate sessions, then compare `/cost`, `git diff`, and the test run. Grade root cause #3 by checking *where* the parse fix landed.
