"""
Given a compressed message compressed and the prefix code tree used to encode it, decode and return the original message.

tree is a nested dictionary with characters at the leaves. For each character in compressed, traverse down one step of the tree. Once you reach a leaf of the tree, the character at that leaf is appended to the decoded message.

If the compressed message could not be decoded in full because the last step did not end at a leaf, return what was decoded so far.
"""


### ME: ~5 ASSISTS, but fully solved alone - Codex wasn't helpful here ###

from typing import Dict, Union

Tree = Dict[str, Union[str, "Tree"]]

def decompress(compressed: str, tree: Tree) -> str:
    """
    Given a compressed message and the prefix code used to encode it, decode and return the original message.

    tree is a nested dictionary with characters at the leaves. For each character in compressed, traverse down one step of the tree. Once you reach a leaf of the tree, the character at that leaf is appended to the decoded message.

    If the compressed message could not be decoded in full because the last step did not end at a leaf, return what was decoded so far.

    The keys of tree and its subdictionaries are always '0' or '1', and the leaf values are also always single characters.
    """
    def get_leaf(idx, subtree):
        if idx >= len(compressed):
            if isinstance(subtree, str):
                return subtree, idx
            return "", idx
        if compressed[idx] in subtree and isinstance(subtree, dict):
            return get_leaf(idx+1, subtree[compressed[idx]])
        else:
            return subtree, idx
    out = ""
    idx = 0
    while idx < len(compressed):
        leaf, idx = get_leaf(idx, tree)
        out += leaf

    return out
   

    

# Examples
print(decompress('110100100', {'0': 'a', '1': {'0': 'n', '1': 'b'}}))
print(decompress('0111010100', {'0': {'0': 'x', '1': 'z'}, '1': 'y'}))



### CODEX ###


from typing import Dict, Union

Tree = Dict[str, Union[str, "Tree"]]


def decompress(compressed: str, tree: Tree) -> str:
    """
    Codex attempt #44
    """
    current = tree
    decoded = ''
    for c in compressed:
        current = current[c]
        if isinstance(current, str):
            decoded += current
            current = tree
    return decoded
