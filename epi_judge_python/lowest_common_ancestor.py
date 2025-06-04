import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    lca_node = None

    def dfs(node, node1, node2):
        nonlocal lca_node
        if lca_node is not None:
            return False
        if node is None:
            return False
        left = dfs(node.left, node1, node2)
        right = dfs(node.right, node1, node2)
        equal1 = node.val == node1.val
        equal2 = node.val == node2.val
        equals = [equal1, equal2, left, right]
        if equals.count(True) == 2:
            lca_node = node
            return True
        return equals.count(True) > 0

    dfs(tree, node0, node1)
    return lca_node


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
