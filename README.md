# 🦥 superlazy

![yapping](https://img.shields.io/badge/yapping-0%25-blue) ![numbers](https://img.shields.io/badge/numbers-measured-brightgreen) ![quality](https://img.shields.io/badge/quality-suspiciously%20unchanged-purple)

Your AI writes essays about your code. You read none of them. You pay for all of them.

**superlazy** = 10 Claude Code skills. Full discipline (TDD, root-cause debugging, verification), zero narration. Distilled from [superpowers](https://github.com/obra/superpowers) + [anthropics/skills](https://github.com/anthropics/skills), then starved of tokens until only the useful parts survived.

## Measured, not imagined

One real A/B run ([full methodology + caveats](BENCHMARK.md)): identical project, 3 planted bugs + 2 feature rounds, identical prompts, Sonnet 5.

| | 😩 baseline | 🦥 superlazy |
|---|---|---|
| session cost | $0.98 * | **$0.53** |
| output tokens | 745 * | **325** |
| API time | 3m 10s | **1m 15s** |
| tests at the end | — * | **11/11 pass** |
| bug #3 (root cause far from symptom) | — * | fixed **at the source**, not patched at the crash site |
| response you read | plans, progress, summaries | `✅` per round |

\* baseline run went sideways (edited the wrong directory) — its cost/tokens are indicative, not a fair comparison yet. Rerun pending. We put the asterisk here instead of pretending; see [BENCHMARK.md](BENCHMARK.md).

## What it saves — and what it doesn't

- ✅ **Output tokens** (the narration you never read) — the only thing this can touch. Roughly half in the run above, not 400×.
- ❌ **Input/context tokens** — unchanged. If your agent re-reads the repo every turn, that's your bill's biggest line and this doesn't fix it.
- ❌ **Thinking tokens** — billed in full whether or not anything is printed. A silent model still thinks at full price.

Lazy, not dishonest.

## Install

```
/plugin marketplace add StarchyBomb/superlazy
```
```
/plugin install superlazy@superlazy
```

That's the whole tutorial. Manual people: clone and dump `skills/*` into `~/.claude/skills/`.

## What's inside

`superlazy` (the vow of silence) · `-tdd` · `-debug` · `-plan` · `-review` · `-verify` · `-worktree` · `-subagents` · `-skill-creator` · `-mcp`

Each one: output ≤3 lines — blocking questions, stuff only you can do, and a final `✅`/`❌`. Everything else is `git diff`'s job.

## FAQ

**Does it skip tests to save tokens?** No. It skips *telling you about* the tests. In the benchmark run it wrote the coupon tests first, TDD-style, then implemented.

**More questions?** That's yapping. Read the diff. 🦥

## License

[MIT](LICENSE) — take it, it's less work for everyone.
