#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
using namespace std;

bool IsBalanced(const unique_ptr<BinaryTreeNode<int> > &root) {
    bool res = true;
    auto dfs = [&](const unique_ptr<BinaryTreeNode<int> > &node, auto &self) {
        if (node == nullptr) {
            return 0;
        }
        auto left = self(node->left, self);
        auto right = self(node->right, self);
        if (abs(left - right) > 1) {
            res = false;
        }
        return max(left, right) + 1;
    };
    dfs(root, dfs);
    return res;
}

int main(int argc, char *argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"tree"};
    return GenericTestMain(args, "is_tree_balanced.cc", "is_tree_balanced.tsv",
                           &IsBalanced, DefaultComparator{}, param_names);
}
