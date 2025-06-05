from collections import deque
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

NOT_PROCESSED = 1
LEFT_PENDING = 0


def inorder_traversal(root: BinaryTreeNode) -> List[int]:
    if not root:
        return []
    stack = deque([(root, NOT_PROCESSED)])
    res = []
    while stack:
        curr_node, status = stack.pop()
        if status == LEFT_PENDING:
            res.append(curr_node.val)
            if curr_node.right is not None:
                stack.append((curr_node.right, NOT_PROCESSED))
        elif status == NOT_PROCESSED:
            stack.append((curr_node, LEFT_PENDING))
            if curr_node.left is not None:
                stack.append((curr_node.left, NOT_PROCESSED))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
