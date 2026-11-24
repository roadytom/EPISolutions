#include <memory>

#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;

bool HasPathSum(const unique_ptr<BinaryTreeNode<int> > &tree,
                int remaining_weight) {
    auto dfs = [&](const unique_ptr<BinaryTreeNode<int> > &node, int weight, auto &self) {
        if (node->left == nullptr && node->right == nullptr) {
            return weight == node->data;
        }
        if (node->left != nullptr) {
            bool res = self(node->left, weight - node->data, self);
            if (res) {
                return true;
            }
        }
        if (node->right != nullptr) {
            bool res = self(node->right, weight - node->data, self);
            if (res) {
                return true;
            }
        }
        return false;
    };
    return dfs(tree, remaining_weight, dfs);
}

int main(int argc, char *argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"tree", "remaining_weight"};
    return GenericTestMain(args, "path_sum.cc", "path_sum.tsv", &HasPathSum,
                           DefaultComparator{}, param_names);
}
