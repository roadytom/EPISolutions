from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

"""
LNR
"""


def inorder_traversal(root: BinaryTreeNode) -> List[int]:
    res = []
    node = root
    DOWN, UP = 0, 1
    DIRECTION = DOWN

    while node:
        if DIRECTION == DOWN:
            node = left_most_child(node)
            DIRECTION, node = process_node(DIRECTION, UP, DOWN, node, res)
        else:
            node = lowest_left_wise_parent(node)
            if node is None:
                break
            DIRECTION, node = process_node(DIRECTION, UP, DOWN, node, res)

    return res


def process_node(DIRECTION, UP, DOWN, node, res):
    res.append(node.val)
    if node.right is not None:
        node = node.right
        DIRECTION = DOWN
    else:
        DIRECTION = UP
    return DIRECTION, node


def left_most_child(node):
    while node.left is not None:
        node = node.left
    return node


def lowest_left_wise_parent(node):
    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
