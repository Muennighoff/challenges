"""
source and target are two strings each containing file contents. Return the number of lines you would need to insert and the number of lines you would need to delete to get to target from source.
"""

### ME - ~5 ASSISTS - Fully solved by Codex ###

import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    """
    source and target are two strings each containing file contents. Return the number of lines you would need to insert and the number of lines you would need to delete to get to target from source.

    Return the answer as a tuple (inserted, deleted).
    """
    s = source.splitlines()
    t = target.splitlines()
    l = len(s) + len(t)
    ins = 0
    dels = 0
    for i in difflib.ndiff(s, t):
        if i[0] == "+":
            ins += 1
        elif i[0] == "-":
            dels += 1
    return (ins, dels)


# Examples
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))


### CODEX ###

import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    """
    Codex attempt #3
    """
    source_lines = source.splitlines()
    target_lines = target.splitlines()
    d = difflib.Differ()
    diff = d.compare(source_lines, target_lines)
    inserted = 0
    deleted = 0
    for line in diff:
        if line.startswith('+'):
            inserted += 1
        elif line.startswith('-'):
            deleted += 1
    return inserted, deleted