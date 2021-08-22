"""
You have several buckets whose sizes are represented by the list sizes. Find the number of different ways to arrange the buckets such that the first bucket’s size is greater than the second bucket’s size.
"""

### ME: 1 ASSIST - Fully solved by CODEX ###

import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    """
    You have several buckets whose sizes are represented by the list sizes. Find the number of different ways to arrange the buckets such that the first bucket’s size is greater than the second bucket’s size.

    sizes is a list of positive integers.
    If sizes has fewer than 2 buckets, return 0.
    Some buckets may have the same size, but are nevertheless treated as unique buckets.
    """
    n = len(sizes)
    if n < 2:
        return 0
    arrangements = 0
    for permutation in itertools.permutations(sizes):
        arrangements += (permutation[0] > permutation[1])
    return arrangements

# Examples
print(count_arrangements([1, 3, 1]))
print(count_arrangements([1, 2]))


### CODEX ###

import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    """
    Codex attempt #37
    """
    if len(sizes) < 2:
        return 0
    return sum(1 for p in itertools.permutations(sizes, len(sizes))
                if p[0] > p[1])
    