---
name: ultralazy
description: Maximum-savings loadout — stacks output economy, input/context economy, and tool-output economy into one skill. Use when the goal is squeezing token/credit cost as hard as possible while keeping quality unchanged or better, or when the user says "ultralazy", "save as much as possible", "minimize cost/credits", or wants every lever at once instead of loading superlazy skills piecemeal.
---

# Ultralazy — every lever, stacked

Three independent savings axes. Stack all three — none substitutes for another, and skipping one leaves real savings on the table.

## 1. Output economy
Emit ONLY: blocking question (AskUserQuestion, 2–4 concrete options, batched) / user-action item (API key, deploy — one imperative line) / final signal, max 1 line: `✅ <what works now>` or `❌ <blocker> — <what's needed>`. Never: plans, progress narration, explanations of changes, recaps, apologies, praise. Target ≤3 lines read total. Full detail: `superlazy`.

## 2. Input/context economy
- Batch independent tool calls into one turn — every extra turn re-sends the whole conversation as input.
- Targeted Grep→Read with offset/limit; never whole files or directory tours.
- Never re-read a file just written/edited; never re-run a command whose inputs haven't changed.
- Large doc/spec/log (hundreds+ tokens) where the task only needs a few sections → `superlazy-context` (`/sc` to index, `/uc` to retrieve) instead of pasting it whole. Skip it when the task touches most of the file — the index has no value there.
- Act as soon as evidence suffices — don't re-derive established facts, re-verify verified results, or re-litigate decided choices.

## 3. Tool-output economy
Verification/build/test commands can dump thousands of lines into context on every run — the same waste as pasting a whole file.
- Test suite → quiet/summary flag or grep for the pass/fail line and failing test names; pull a full stack trace only for the one failure you're about to fix.
- Build → exit code + error lines, not the full compiler log.
- Any command whose output exceeds what the current claim needs → filter to the answer before it enters context. Full detail: `superlazy-verify`.

## Honesty — what this can't touch
Skills are prompt instructions, not API calls — they cannot set request-level parameters. These real levers exist but are controlled by the harness/client, not by loading a skill:
- **Prompt cache placement/TTL** — automatic at the harness level. What a skill *can* do: keep its own text frozen (no timestamps, no per-run content) so it doesn't invalidate a cached prefix.
- **Thinking budget / effort level** — set per-request by the client. A silent model still thinks — and is billed — at full depth regardless of what any skill says.
- **Compaction / context editing** — server-side context management; runs (or doesn't) independent of skill content.
- **Batch API (50% off)** — irrelevant here; it's for async, non-interactive bulk jobs, not a live coding session.

Never claim a token-savings number for something on this list, and say so plainly if a request needs a lever this skill doesn't reach.
