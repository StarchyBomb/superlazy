# 🦥 superlazy

![yapping](https://img.shields.io/badge/yapping-0%25-blue) ![tokens](https://img.shields.io/badge/tokens-your%20money-brightgreen) ![quality](https://img.shields.io/badge/quality-suspiciously%20unchanged-purple)

Your AI writes essays about your code. You read none of them. You pay for all of them.

**superlazy** = 10 Claude Code skills. Full discipline (TDD, root-cause debugging, verification), zero narration. Distilled from [superpowers](https://github.com/obra/superpowers) + [anthropics/skills](https://github.com/anthropics/skills), then starved of tokens until only the useful parts survived.

## without vs with

Task: *"add a logout button"*

| | 😩 without | 🦥 with superlazy |
|---|---|---|
| response | "Great question! I'll create a comprehensive plan… **Step 1: Understanding the codebase**… **Summary of changes:** I have successfully… **Next steps you might consider:**…" | `✅ logout button works` |
| output tokens | ~2,800 | ~7 |
| tokens you actually read | 0 | 7 |
| useful information | in the diff | in the diff |
| tests | ran | ran (just didn't live-tweet it) |
| your wallet | 🔥🔥🔥 | 🦥 |

Same diff. Same passing tests. **~400× less reading you weren't doing anyway.**

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

**Does it skip tests to save tokens?** No. It skips *telling you about* the tests. Lazy, not dishonest.

**More questions?** That's yapping. Read the diff. 🦥

## License

[MIT](LICENSE) — take it, it's less work for everyone.
