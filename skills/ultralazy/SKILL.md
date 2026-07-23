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
- Unfamiliar/large codebase, first orientation pass → `superlazy-repomap` (`python skills/superlazy-repomap/scripts/repo_map.py`) for a one-shot signature index instead of a multi-round Glob/Grep/Read tour.
- Large doc/spec/log (hundreds+ tokens) where the task only needs a few sections → `superlazy-context` (`/sc` to index, `/uc` to retrieve) instead of pasting it whole. Skip both of the above when the task will touch most of the file/repo anyway — the index has no value there.
- Act as soon as evidence suffices — don't re-derive established facts, re-verify verified results, or re-litigate decided choices.
- This plugin also ships a `PreToolUse` hook (`hooks/hooks.json` → `no_reread.py`) that blocks a full-file `Read` when this session already read that exact file and it hasn't changed on disk since — enforced automatically, not something you need to remember.

## 3. Tool-output economy
Verification/build/test commands can dump thousands of lines into context on every run — the same waste as pasting a whole file. Wrap a long-output command: `python skills/superlazy-verify/scripts/summarize.py -- <command>` — passes through short output unchanged, filters long output to pass/fail lines + failure context, exit code always intact. Full detail: `superlazy-verify`.

## Honesty — what this can't touch
Skills are prompt instructions, not API calls — they cannot set request-level parameters. These real levers exist but are controlled by the harness/client, not by loading a skill:
- **Prompt cache placement/TTL** — automatic at the harness level. What a skill *can* do: keep its own text frozen (no timestamps, no per-run content) so it doesn't invalidate a cached prefix.
- **Thinking budget / effort level** — set per-request by the client. A silent model still thinks — and is billed — at full depth regardless of what any skill says.
- **Compaction / context editing** — server-side context management; runs (or doesn't) independent of skill content.
- **Batch API (50% off)** — irrelevant here; it's for async, non-interactive bulk jobs, not a live coding session.

Never claim a token-savings number for something on this list, and say so plainly if a request needs a lever this skill doesn't reach.
