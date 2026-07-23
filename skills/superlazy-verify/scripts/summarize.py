#!/usr/bin/env python3
"""
Superlazy test/build output summarizer.

Runs a command and, if its combined output is large, prints only the lines
that carry a verification verdict -- pass/fail summaries, failure/error
lines, tracebacks/panics -- instead of the full raw log. Short output is
printed as-is (filtering it would save nothing). Exit code always mirrors
the wrapped command's, so this is safe to use as the actual verify command,
not just a post-processor.

Usage: python3 summarize.py -- <command> [args...]
"""
import sys
import subprocess
import re

# Below this many characters, filtering saves nothing worth the risk of
# hiding something relevant -- just print everything.
SHORT_OUTPUT_THRESHOLD = 4000

KEEP_PATTERNS = re.compile(
    r"""
    ^\s*(FAIL|FAILED|ERROR|PASS|PASSED|OK)\b |
    \bfailed\b | \bfailure\b | \berror\b |
    ^\s*(ok|---)\s |
    \d+\s+(passed|failed|error|skipped) |
    Traceback\ \(most\ recent | ^\s*panic: | ^\s*Error: |
    ✓|✗|✔|✘
    """,
    re.IGNORECASE | re.VERBOSE,
)

CONTEXT_LINES = 2  # lines to keep around each match, for a bit of trace context


def summarize(text: str) -> str:
    lines = text.splitlines()
    keep = set()
    for i, line in enumerate(lines):
        if KEEP_PATTERNS.search(line):
            for j in range(max(0, i - CONTEXT_LINES), min(len(lines), i + CONTEXT_LINES + 1)):
                keep.add(j)

    if not keep:
        # No recognizable verdict lines -- fall back to head+tail so nothing
        # relevant near the end (usually where summaries live) is lost.
        head = lines[:20]
        tail = lines[-20:]
        omitted = max(0, len(lines) - len(head) - len(tail))
        parts = head
        if omitted:
            parts.append(f"... ({omitted} lines omitted -- no pass/fail markers matched) ...")
        parts += tail
        return "\n".join(parts)

    out = []
    prev = None
    for i in sorted(keep):
        if prev is not None and i != prev + 1:
            out.append(f"... ({i - prev - 1} lines omitted) ...")
        out.append(lines[i])
        prev = i
    return "\n".join(out)


def main():
    args = sys.argv[1:]
    if args and args[0] == "--":
        args = args[1:]
    if not args:
        print("Usage: summarize.py -- <command> [args...]", file=sys.stderr)
        sys.exit(1)

    proc = subprocess.run(args, capture_output=True, text=True)
    combined = proc.stdout + proc.stderr

    if len(combined) <= SHORT_OUTPUT_THRESHOLD:
        sys.stdout.write(combined)
    else:
        summary = summarize(combined)
        print(summary)
        print(
            f"─ summarized: {len(combined)} chars -> {len(summary)} chars "
            f"(full output not shown; re-run without this wrapper if you need it verbatim)"
        )

    sys.exit(proc.returncode)


if __name__ == "__main__":
    main()
