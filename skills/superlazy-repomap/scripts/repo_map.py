#!/usr/bin/env python3
"""
Superlazy repo map -- one-shot signature index of a codebase.

Prints file path + top-level function/class/type signatures with line
numbers, skipping bodies. Regex-based, not a real parser -- a best-effort
map for deciding which few files are worth a targeted Read, not a
substitute for reading the file you're about to edit.
"""
import sys
import os
import re

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build",
    "target", "vendor", ".next", ".turbo", "coverage", ".pytest_cache",
    ".mypy_cache", "compressed_states", ".superlazy-context",
}

_JS_PATTERNS = [
    r"^\s*(export\s+)?(default\s+)?(async\s+)?function\s*\*?\s*\w+",
    r"^\s*(export\s+)?class\s+\w+",
    r"^\s*(export\s+)?const\s+\w+\s*=\s*(async\s*)?\(",
]
_TS_PATTERNS = _JS_PATTERNS + [
    r"^\s*(export\s+)?interface\s+\w+",
    r"^\s*(export\s+)?type\s+\w+\s*=",
]

PATTERNS = {
    ".py": [r"^\s*(class\s+\w+|(async\s+)?def\s+\w+)"],
    ".js": _JS_PATTERNS,
    ".jsx": _JS_PATTERNS,
    ".ts": _TS_PATTERNS,
    ".tsx": _TS_PATTERNS,
    ".go": [r"^func\s+(\(\w+\s+\*?\w+\)\s+)?\w+", r"^type\s+\w+\s+(struct|interface)"],
    ".rb": [r"^\s*(class|module)\s+\w+", r"^\s*def\s+\w+"],
    ".rs": [r"^\s*(pub\s+)?(async\s+)?fn\s+\w+", r"^\s*(pub\s+)?(struct|enum|trait)\s+\w+"],
    ".java": [r"^\s*(public|private|protected)[\w\s<>\[\],]*\b(class|interface|enum)\s+\w+"],
    ".cs": [r"^\s*(public|private|protected|internal)[\w\s<>\[\],]*\b(class|interface|enum|struct)\s+\w+"],
    ".php": [r"^\s*(class|interface|trait)\s+\w+", r"^\s*(public|private|protected|static|\s)*function\s+\w+"],
}


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def compiled_pattern(ext):
    patterns = PATTERNS.get(ext)
    if not patterns:
        return None
    return re.compile("|".join(f"(?:{p})" for p in patterns))


def scan_file(path, pattern):
    hits = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                if pattern.match(line):
                    hits.append((i, line.strip()[:100]))
    except OSError:
        return None
    return hits


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            yield os.path.join(dirpath, name)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    files_scanned = 0
    files_matched = 0
    source_tokens = 0
    lines_out = []

    for path in sorted(walk(root)):
        ext = os.path.splitext(path)[1]
        pattern = compiled_pattern(ext)
        if pattern is None:
            continue
        files_scanned += 1
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                source_tokens += estimate_tokens(f.read())
        except OSError:
            continue
        hits = scan_file(path, pattern)
        if not hits:
            continue
        files_matched += 1
        rel = os.path.relpath(path, root)
        lines_out.append(rel)
        for lineno, sig in hits:
            lines_out.append(f"  L{lineno}  {sig}")

    card = "\n".join(lines_out)
    card_tokens = estimate_tokens(card)
    print(card if card else "(no matching source files found)")
    print(
        f"─ map: ~{card_tokens} tokens across {files_matched}/{files_scanned} files "
        f"vs ~{source_tokens} tokens if those files were read in full "
        f"(regex-based, may miss nested/unusual definitions -- Read the file before editing it)"
    )


if __name__ == "__main__":
    main()
