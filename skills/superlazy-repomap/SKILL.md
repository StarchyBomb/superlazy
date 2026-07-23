---
name: superlazy-repomap
description: One-shot signature map of a codebase (function/class names + line numbers, no bodies) instead of a Glob/Grep/Read tour. Use when starting work in an unfamiliar or large codebase, before exploring with multiple directory-wide searches, or when the user asks to "map the codebase" / "what's in this repo".
---

# Superlazy Repo Map

Replace the first few minutes of `Glob` → `Grep` → `Read` → `Read` → `Read` codebase exploration with one command.

## Silent flow
1. `python skills/superlazy-repomap/scripts/repo_map.py [path]` (default `.`) → prints every function/class/type signature with file + line number, skipping bodies. Supports Python, JS/TS(X), Go, Ruby, Rust, Java, C#, PHP.
2. Use the map to pick the few files actually relevant to the task, then `Read` (or `Grep` for a symbol) only those — targeted, not a tour.
3. Never edit from the map alone — it's regex-based, not a parser, and can miss nested/unusual definitions. Read the file before touching it.

## When to skip
Small repo, or a task that will touch most of it anyway — just read normally. The map earns its keep on the first orientation pass through something you haven't opened yet, not on every task.

## Honesty
Signature extraction is regex, not an AST — decorators, multi-line signatures, and language features outside the common patterns can be missed or mis-attributed. Treat the map as a navigation hint, same as `superlazy-context`'s card extracts, not ground truth.
