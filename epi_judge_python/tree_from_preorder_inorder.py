from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    preorder_idx = 0
    node_to_inorder_idx = {val: i for i, val in enumerate(inorder)}

    def build_tree(left, right):
        nonlocal preorder_idx
        if left > right:
            return None
        node_idx = node_to_inorder_idx.get(preorder[preorder_idx], -1)
        assert node_idx >= 0
        curr = BinaryTreeNode(inorder[node_idx])
        preorder_idx += 1
        curr.left = build_tree(left, node_idx - 1)
        curr.right = build_tree(node_idx + 1, right)
        return curr

    return build_tree(0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
