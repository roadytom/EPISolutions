from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

"""
LNR
"""


def inorder_traversal(root: BinaryTreeNode) -> List[int]:
    res = []
    prev, curr, nxt = None, root, None

    while curr:
        if prev is None or curr.parent is prev:
            if curr.left:
                nxt = curr.left
            else:
                res.append(curr.val)
                nxt = curr.right or curr.parent
        elif curr.left is prev:
            res.append(curr.val)
            nxt = curr.right or curr.parent
        elif curr.right is prev:
            nxt = curr.parent

        prev, curr = curr, nxt
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
