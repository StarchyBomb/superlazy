---
name: superlazy-skill-creator
description: Create or improve skills with minimal tokens. Use when the user wants a new skill, wants to edit/optimize an existing skill, or wants a workflow captured as a skill.
---

# Superlazy Skill Creator

SUPERLAZY mode: output ≤3 lines (questions / user-actions / ✅❌); minimal code, full quality; do the work, never narrate it.

## Structure
```
skill-name/
├── SKILL.md            # frontmatter: name, description (required)
└── references|scripts|assets/   # only if genuinely needed
```
Progressive disclosure: description always in context (~100 words) → body loads on trigger → resources load on demand. Push bulk content DOWN a level; scripts execute without being read.

## Token rules (this is the skill's whole point)
- **name**: lowercase-hyphen, ≤64 chars. **description**: third person, ≤1024 chars — carries ALL triggering info: what it does + when to use, phrased "pushy" (models undertrigger); list concrete user phrases/contexts that must trigger it, and anti-triggers ("Do NOT use for…") if adjacent skills overlap.
- Body budget ≤100 lines: every line must change model behavior. Delete rationale, motivation, examples that restate rules, tables that repeat prose. Imperative voice only.
- One rule stated once. If you write "in other words" — delete the sentence before it.
- If the skill makes the model produce user-facing output, embed the superlazy output contract line in it.

## Process
1. Missing intent (trigger phrases? output format? edge cases?) → ONE batched question.
2. Draft → self-test: run 2-3 realistic prompts against it, check it triggers and behaves.
3. Iterate on failures. `✅ <path>` when it passes.
