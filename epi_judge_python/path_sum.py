from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(root: BinaryTreeNode, remaining_weight: int) -> bool:
    if not root:
        return False

    def dfs(node, upper):
        if not node:
            return False
        if node.left is None and node.right is None:
            return (upper + node.val) == remaining_weight
        return dfs(node.left, upper + node.val) or dfs(node.right, upper + node.val)

    return dfs(root, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
