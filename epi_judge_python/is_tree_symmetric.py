from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(root: BinaryTreeNode) -> bool:
    def is_equal(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.data == node2.data

    if not root or (root.left is None and root.right is None):
        return True
    if not is_equal(root.left, root.right):
        return False
    level = [root, root]
    while level:
        new_level = []
        for i in range(len(level) // 2):
            if not is_equal(level[i].left, level[-i - 1].right) or not is_equal(level[i].right, level[-i - 1].left):
                return False
        for node in level:
            if node.left is not None:
                new_level.append(node.left)
            if node.right is not None:
                new_level.append(node.right)
        level = new_level
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
