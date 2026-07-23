#!/usr/bin/env python3
"""
Superlazy no-reread hook (PreToolUse on Read).

Blocks a Read of a file this session has already read in full, unchanged on
disk since (same mtime + size). Partial reads (offset/limit) always pass
through -- targeted reads are the behavior superlazy wants, not the waste
this hook exists to catch. A real edit changes mtime, so re-reading after an
Edit/Write is never blocked.
"""
import sys
import os
import json

MAX_ENTRIES = 2000


def cache_path():
    root = os.environ.get("CLAUDE_PLUGIN_DATA")
    if not root:
        root = os.path.join(os.getcwd(), ".claude", "superlazy-ultralazy")
    return os.path.join(root, "read-cache.json")


def load_cache(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def save_cache(path, cache):
    if len(cache) > MAX_ENTRIES:
        cache = dict(list(cache.items())[-MAX_ENTRIES:])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f)


def fingerprint(path):
    try:
        st = os.stat(path)
        return f"{st.st_mtime_ns}:{st.st_size}"
    except OSError:
        return None


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    if payload.get("tool_name") != "Read":
        sys.exit(0)

    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path")
    if not path or tool_input.get("offset") or tool_input.get("limit"):
        sys.exit(0)

    fp = fingerprint(path)
    if fp is None:
        sys.exit(0)

    session_id = payload.get("session_id", "unknown")
    key = f"{session_id}:{path}"

    store = cache_path()
    cache = load_cache(store)

    if cache.get(key) == fp:
        print(
            f"Already read {path} this session; unchanged on disk since (same size + "
            "mtime). Reuse what you already have instead of re-reading it in full -- "
            "if you need to confirm a specific edit landed, Read with offset/limit on "
            "just those lines instead.",
            file=sys.stderr,
        )
        sys.exit(2)

    cache[key] = fp
    save_cache(store, cache)
    sys.exit(0)


if __name__ == "__main__":
    main()
