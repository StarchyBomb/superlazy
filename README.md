# 🦥 superlazy

> Same code quality. Fewer tokens. Zero yapping.

![tokens saved](https://img.shields.io/badge/tokens-saved-brightgreen) ![yapping](https://img.shields.io/badge/yapping-0%25-blue) ![effort](https://img.shields.io/badge/effort-minimum%20viable-orange) ![quality](https://img.shields.io/badge/quality-suspiciously%20unchanged-purple) ![license](https://img.shields.io/badge/license-MIT-yellow)

**superlazy** is a set of 10 Claude Code skills, distilled from [obra/superpowers](https://github.com/obra/superpowers) and [anthropics/skills](https://github.com/anthropics/skills), then put on an aggressive token diet. All the discipline (TDD, root-cause debugging, verification, code review). None of the essays.

---

## The problem

You: "add a logout button"

Your AI:

> Great question! I'll now create a comprehensive plan to add the logout button. First, let me explain my approach in detail...
>
> **Step 1: Understanding the codebase** — I have carefully analyzed...
>
> **Summary of changes:** I have successfully implemented the logout button by...
>
> **Next steps you might consider:** ...
>
> *(2,847 tokens. You read: 0 of them. You just wanted the button.)*

## The superlazy way

You: "add a logout button"

Your AI:

> ✅ logout button works

That's it. That's the whole conversation. The tests ran. The diff is right there. Read it or don't — the sloth does not judge. 🦥

---

## The rules (enforced by every skill)

1. **Output ≤3 lines.** Only: blocking questions, things *you* must do yourself, and a final `✅` / `❌`.
2. **No narration.** No "I will now...", no "Here's a summary of what I did", no re-pasting code it already wrote to files. The diff *is* the summary.
3. **Lazy = minimal code, never refused work.** YAGNI, stdlib first, fewest files touched. Writing 500 lines when 5 do the trick is not "thorough", it's littering.
4. **Quality is non-negotiable.** TDD still happens. Root causes still get found. Tests still run before any `✅`. It just all happens *silently*, like a ninja. A very tired ninja.

---

## Install

### Option 1: Plugin (recommended — for people who are, correctly, lazy)

In Claude Code:

```
/plugin marketplace add StarchyBomb/superlazy
```

```
/plugin install superlazy@superlazy
```

Done. Restart Claude Code if it asks. That's the whole tutorial.

### Option 2: Manual clone (for people who like typing)

```bash
git clone https://github.com/StarchyBomb/superlazy.git
```

Then copy the folders inside `skills/` into:

- `~/.claude/skills/` — everywhere (global)
- `<your-project>/.claude/skills/` — one project only

---

## The skills

| Skill | What it silently does | Distilled from |
|---|---|---|
| `superlazy` | Core mode. Load first. The vow of silence itself. | — |
| `superlazy-tdd` | Red → green → refactor, without live-tweeting it | test-driven-development |
| `superlazy-debug` | Finds the *actual* root cause instead of duct-taping symptoms | systematic-debugging + root-cause-tracing |
| `superlazy-plan` | Plans in its head. Shows you nothing. Executes everything. | writing-plans + executing-plans |
| `superlazy-review` | Reviews the diff, deletes the fat, never says "You're absolutely right!" | requesting + receiving-code-review |
| `superlazy-verify` | No `✅` without fresh proof. "should work" is a banned phrase. | verification-before-completion |
| `superlazy-worktree` | Isolated workspace so your branch survives the experiments | using-git-worktrees |
| `superlazy-subagents` | Farms tasks out to cheap subagents, pays them in files not paragraphs | subagent-driven-development |
| `superlazy-skill-creator` | Builds skills that are themselves on a token diet | skill-creator |
| `superlazy-mcp` | Builds MCP servers without narrating the MCP spec back at you | mcp-builder |

---

## FAQ

**Q: Will it explain what it did?**
A: No. That's the point. `git diff` is right there and it never lies.

**Q: What if it needs to ask me something?**
A: Then it asks — once, batched, with actual options. Decisions are the only thing you're needed for. Sorry.

**Q: Isn't "lazy" bad?**
A: Lazy wrote 5 lines. Diligent wrote 500 lines, 3 abstractions, a config system, and 2 new bugs. Lazy's tests pass. You tell me.

**Q: But I *like* reading long explanations of my own codebase.**
A: [superpowers](https://github.com/obra/superpowers) is right there and it's excellent. Go be happy.

**Q: Does it skip tests to save tokens?**
A: 😤 No. It skips *telling you about* the tests. The tests run. Silence ≠ skipping. The sloth is lazy, not dishonest.

**Q: Why a sloth?**
A: Sloths do everything slowly, deliberately, and correctly, using the least possible energy. Also they can't type "Great question!" — their fingers are too slow. Role model.

---

## Contributing

PRs welcome. PR descriptions over 3 lines will be reviewed with deep suspicion. If your diff adds more lines than it deletes, attach a written apology.

## License

[MIT](LICENSE) — take it, it's less work for everyone.

---

*Powered by the ancient art of ขี้เกียจอย่างมีคุณภาพ (quality laziness).* 🦥
