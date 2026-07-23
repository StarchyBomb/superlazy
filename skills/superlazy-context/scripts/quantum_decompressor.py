#!/usr/bin/env python3
"""
Superlazy Context Retriever (/uc). Mechanism adapted from supercontexter
(https://github.com/StarchyBomb/supercontexter).

Loads a .qstate index and either prints its compact card (no args) or prints
the EXACT original text of the requested sections, verbatim, verified against
the source file's hash. If the source changed since indexing, it refuses and
asks for a re-index rather than serving stale line ranges.
"""

import sys
import os
import json
import hashlib

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

STATE_DIR = os.path.join(".superlazy-context", "compressed_states")


def load_qstate(state_identifier: str = "latest"):
    name = state_identifier.strip("|⟩")
    if not name.endswith(".qstate"):
        name += ".qstate"
    file_path = os.path.join(STATE_DIR, name)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    args = sys.argv[1:]
    state_id = args[0] if args else "latest"
    section_ids = args[1:]

    qstate = load_qstate(state_id)
    if not qstate:
        print(f"❌ State '{state_id}' not found in {STATE_DIR}/ — run quantum_compressor.py first")
        sys.exit(1)

    src = qstate["source"]

    if not section_ids:
        # Card mode: re-print the compact index card
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from quantum_compressor import index_card
        print(index_card(qstate))
        return

    # Section mode: verify source unchanged, then print exact original lines
    if not os.path.exists(src["path"]):
        print(f"❌ Source file missing: {src['path']}")
        sys.exit(1)
    with open(src["path"], 'r', encoding='utf-8') as f:
        text = f.read()
    if hashlib.sha256(text.encode('utf-8')).hexdigest() != src["sha256"]:
        compressor = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_compressor.py")
        print(f"❌ Source changed since indexing — re-run: python {compressor} \"{src['path']}\"")
        sys.exit(1)

    lines = text.split('\n')
    by_id = {s["id"]: s for s in qstate["sections"]}
    for sid in section_ids:
        s = by_id.get(sid)
        if not s:
            print(f"❌ Unknown section '{sid}' (valid: {', '.join(by_id)})")
            sys.exit(1)
        start, end = s["lines"]
        print(f"── {s['id']}: {s['title']} (L{start}-{end}) ──")
        print('\n'.join(lines[start - 1:end]))


if __name__ == "__main__":
    main()
