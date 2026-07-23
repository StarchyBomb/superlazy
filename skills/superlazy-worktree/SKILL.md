---
name: superlazy-worktree
description: Silent isolated workspace setup. Use when starting feature work that needs isolation from the current workspace, or before executing an implementation plan.
---

# Superlazy Worktree

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Silent flow
1. **Detect existing isolation**: `git rev-parse --git-dir` ≠ `--git-common-dir` (and NOT a submodule: `git rev-parse --show-superproject-working-tree` empty) → already isolated, skip creation.
2. **Consent**: no prior user preference on worktrees → one blocking question ("isolate in a worktree?"). Declined → work in place.
3. **Create**: native worktree tool (`EnterWorktree`, `/worktree`, etc.) ALWAYS beats manual git — using `git worktree add` when a native tool exists creates phantom state. No native tool → `git worktree add .worktrees/<branch> -b <branch>` (respect existing `.worktrees/`/`worktrees/`; MUST verify dir is git-ignored first — if not, add to .gitignore and commit).
4. **Setup + baseline**: install deps per manifest (package.json/Cargo.toml/pyproject/go.mod), run the test suite once. Baseline fails → one-line question (proceed vs investigate). Passes → proceed silently.

Never: nested worktrees, unignored worktree dirs, skipping baseline, starting on main/master without consent.
