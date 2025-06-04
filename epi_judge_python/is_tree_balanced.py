from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(root: BinaryTreeNode) -> bool:
    if not root:
        return True

    def post_order_traversal(node):
        if not node:
            return True, 0
        left_res, left_height = post_order_traversal(node.left)
        right_res, right_height = post_order_traversal(node.right)
        if not left_res or not right_res:
            return False, -1
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

    return post_order_traversal(root)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
