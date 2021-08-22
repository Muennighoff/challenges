"""
Parse the given Python source code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order.

The input will not contain any wildcard imports (from ... import *).
Ignore aliases (renamings): from x import y as z should be represented as x.y.

import os
import concurrent.futures
from os import path as renamed_path
from typing import (
    List, Tuple
)

>

['concurrent.futures', 'os', 'os.path', 'typing.List', 'typing.Tuple']
"""


### ME ~2 ASSISTS - Took CODEX output & added the for sub_name to iterate through them - Nice teamwork ###

import ast
from typing import List

def parse_imports(code: str) -> List[str]:
    """
    Parse the given Python source code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order.

    Example input:
    import os
    import concurrent.futures
    from os import path as renamed_path
    from typing import (
        List, Tuple
    )
    Example output:
    ['concurrent.futures', 'os', 'os.path', 'typing.List', 'typing.Tuple']
    """
    imports = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            # os.path -> os.path
            # renamed_path -> os.path
            for sub_name in node.names:
                imports.append(node.module + '.' + sub_name.name)
    return sorted(imports)

    

# Examples
print(parse_imports('import os'))
print(parse_imports('import os\nfrom typing import List'))


### CODEX ###

import ast
from typing import List


def parse_imports(code: str) -> List[str]:
    """
    Codex attempt #18
    """
    tree = ast.parse(code)
    ans = []
    for statement in tree.body:
        if isinstance(statement, ast.Import):
            for name in statement.names:
                ans.append(name.name)
        elif isinstance(statement, ast.ImportFrom):
            for name in statement.names:
                ans.append(statement.module + '.' + name.name)
    return sorted(ans)
