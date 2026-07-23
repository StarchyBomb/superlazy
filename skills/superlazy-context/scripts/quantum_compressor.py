#!/usr/bin/env python3
"""
Superlazy Context Indexer (/sc). Mechanism adapted from supercontexter
(https://github.com/StarchyBomb/supercontexter).

Builds a compact section index (.qstate) of a file. The original text stays on
disk untouched; only the small index card enters agent context. Exact original
sections are retrieved on demand via quantum_decompressor.py — lossless by
construction, because nothing is ever thrown away.

State is stored relative to the current working directory (the project being
worked on), not next to this script — superlazy is a global plugin, so a
project-local state dir keeps one project's indexes from colliding with
another's.
"""

import sys
import os
import json
import hashlib
import re
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CHUNK = 50  # fallback chunk size (lines) for files without markdown headings
MD_EXTS = ('.md', '.markdown', '.mdx', '.txt', '.rst')
STATE_DIR = os.path.join(".superlazy-context", "compressed_states")


def estimate_tokens(text: str) -> int:
    """Rough token estimate (~4 chars/token). Same heuristic everywhere so ratios are comparable."""
    return max(1, len(text) // 4)


def split_sections(lines, is_markdown):
    """Return [(title, start, end)] with 1-indexed inclusive line ranges covering the whole file."""
    if is_markdown:
        idx = [i for i, l in enumerate(lines) if re.match(r'#{1,6} ', l)]
        if idx:
            bounds = []
            if idx[0] > 0:
                bounds.append(("(preamble)", 1, idx[0]))
            for j, i in enumerate(idx):
                end = idx[j + 1] if j + 1 < len(idx) else len(lines)
                bounds.append((lines[i].lstrip('#').strip(), i + 1, end))
            return bounds
    # Fallback: fixed-size chunks labeled by their first non-blank line
    bounds = []
    for start in range(0, len(lines), CHUNK):
        chunk = lines[start:start + CHUNK]
        title = next((l.strip() for l in chunk if l.strip()), "(blank)")[:60]
        bounds.append((title, start + 1, min(start + CHUNK, len(lines))))
    return bounds


def build_index(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    is_md = path.lower().endswith(MD_EXTS)

    sections = []
    for n, (title, start, end) in enumerate(split_sections(lines, is_md)):
        body = '\n'.join(lines[start - 1:end])
        extract = re.sub(r'\s+', ' ', body).strip()[:120]
        sections.append({
            "id": f"s{n}",
            "title": title[:80],
            "lines": [start, end],
            "tokens_est": estimate_tokens(body),
            "extract": extract,
        })

    return {
        "state_id": f"Ψ_{sha[:8]}",
        "created_at": datetime.now().isoformat(),
        "source": {
            "path": os.path.abspath(path),
            "sha256": sha,
            "total_lines": len(lines),
            "total_tokens_est": estimate_tokens(text),
        },
        "sections": sections,
    }


def index_card(qstate: dict) -> str:
    """The compact card an agent keeps in context instead of the full file."""
    src, secs = qstate["source"], qstate["sections"]
    decompressor = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_decompressor.py")
    card = [
        f"|{qstate['state_id']}⟩ {os.path.basename(src['path'])} — "
        f"{src['total_tokens_est']} tokens on disk, {len(secs)} sections (lossless, load on demand)"
    ]
    for s in secs:
        card.append(
            f"  {s['id']} L{s['lines'][0]}-{s['lines'][1]} ~{s['tokens_est']}tk  "
            f"{s['title']} — {s['extract'][:60]}"
        )
    card.append(f"retrieve: python {decompressor} {qstate['state_id']} <section-id ...>")
    return '\n'.join(card)


def save(qstate: dict, storage_dir: str) -> str:
    os.makedirs(storage_dir, exist_ok=True)
    file_path = os.path.join(storage_dir, f"{qstate['state_id']}.qstate")
    for p in (file_path, os.path.join(storage_dir, "latest.qstate")):
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(qstate, f, indent=2, ensure_ascii=False)
    return file_path


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print("Usage: python quantum_compressor.py <file> [more files...]")
        print(f"Indexes each file into {STATE_DIR}/<Ψ_hash>.qstate (relative to CWD) and prints its card.")
        sys.exit(0 if args else 1)

    for path in args:
        if not os.path.isfile(path):
            print(f"❌ Not a file: {path}")
            sys.exit(1)
        qstate = build_index(path)
        file_path = save(qstate, STATE_DIR)
        card = index_card(qstate)
        card_tokens = estimate_tokens(card)
        total = qstate["source"]["total_tokens_est"]
        print(card)
        print(f"─ card in context: ~{card_tokens} tokens; full text ({total} tokens) stays on disk, "
              f"loaded per section only when a task needs it")
        print(f"─ saved: {file_path}")


if __name__ == "__main__":
    main()
