from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()
