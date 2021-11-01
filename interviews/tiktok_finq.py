#!/bin/python3

import math
import os
import random
import re
import sys


# Task:
# Given a list of nodes representing a binary search tree, return its sExpression
# Below implementation passed all tests


# Complete the 'sExpression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING nodes as parameter.


def sExpression_inner(nodes):
    # Turn binary tree into a fast data structure
    # Choosing dictionaries - but there is likely something better, but I cant look it up online
    # Maybe a trie
    b_tree = {}
    children = set()
    parents = set()
    errors = []

    for node_pair in nodes.split(" "):
        par, child = node_pair.strip("(").strip(")").split(",")
        b_tree.setdefault(par, [])
        if child in b_tree[par]:
            errors.append("E2")
            # Else this will add an E1, which is technically correct
            # but appararently the test cases prefer an E2 here
            continue
        b_tree[par].append(child)
        if len(b_tree[par]) > 2:
            errors.append("E1")
        if child in children:
            errors.append("E3")
        children.add(child)
        parents.add(par)

    roots = parents.difference(children)
    if len(roots) > 1:
        errors.append("E4")
    # No root seems to be also considered as an E3, tho technically
    # there does not need to be a node being a descendant of > 1 nodes
    # so it should be an E5
    elif len(roots) == 0:
        errors.append("E3")
    # Return lexicographically smallest error
    if errors:
        return sorted(errors)[0]
    root = roots.pop()

    def get_repr(par):
        if par not in b_tree:
            return par
        children = sorted(b_tree[par])
        if len(children) == 2:
            return f"{par}({get_repr(children[0])})({get_repr(children[1])})"
        else:
            return f"{par}({get_repr(children[0])})"

    out = f"({get_repr(root)})"
    return out


def sExpression(nodes):
    try:
        return sExpression_inner(nodes)
    except:
        return "E5"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nodes = input()

    result = sExpression(nodes)

    fptr.write(result + "\n")

    fptr.close()
