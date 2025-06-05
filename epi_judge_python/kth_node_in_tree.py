import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None, size=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(root: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    def get_node_size_or_zero(node):
        return 0 if not node else node.size

    def dfs(node, k):
        if k > node.size:
            return None
        if k <= get_node_size_or_zero(node.left):
            return dfs(node.left, k)
        k -= get_node_size_or_zero(node.left)
        if k == 1:
            return node
        return dfs(node.right, k - 1)

    return dfs(root, k)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
