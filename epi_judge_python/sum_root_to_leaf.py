from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    if not tree:
        return 0

    def dfs(node, upper):
        if node.left is None and node.right is None:
            return upper * 2 + node.val
        curr = upper * 2 + node.val
        return (0 if node.left is None else dfs(node.left, curr)) + (0 if node.right is None else dfs(node.right, curr))

    return dfs(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
