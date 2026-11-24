#include <memory>

#include "binary_tree_node.h"
#include "test_framework/binary_tree_utils.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using namespace std;

struct result {
    BinaryTreeNode<int> *res = nullptr;
    int one_found = 0;
};

BinaryTreeNode<int> *Lca(const unique_ptr<BinaryTreeNode<int> > &tree,
                         const unique_ptr<BinaryTreeNode<int> > &node0,
                         const unique_ptr<BinaryTreeNode<int> > &node1) {
    auto dfs = [&](const unique_ptr<BinaryTreeNode<int> > &node, auto &self) {
        if (node == nullptr) {
            return result{};
        }
        bool me_equal1 = node->data == node0->data;
        bool me_equal2 = node->data == node1->data;
        auto left_res = self(node->left, self);
        auto right_res = self(node->right, self);
        if (left_res.res != nullptr) {
            return left_res;
        }
        if (right_res.res != nullptr) {
            return right_res;
        }
        int total = left_res.one_found + right_res.one_found + static_cast<int>(me_equal1) + static_cast<int>(me_equal2);
        if (total == 2) {
            return result{node.get(), 1};
        }
        return result{nullptr, total};
    };
    return dfs(tree, dfs).res;
}


int LcaWrapper(TimedExecutor &executor,
               const unique_ptr<BinaryTreeNode<int> > &tree, int key0,
               int key1) {
    const unique_ptr<BinaryTreeNode<int> > &node0 = MustFindNode(tree, key0);
    const unique_ptr<BinaryTreeNode<int> > &node1 = MustFindNode(tree, key1);

    auto result = executor.Run([&] { return Lca(tree, node0, node1); });

    if (!result) {
        throw TestFailure("Result can not be nullptr");
    }
    return result->data;
}

int main(int argc, char *argv[]) {
    vector<string> args{argv + 1, argv + argc};
    vector<string> param_names{"executor", "tree", "key0", "key1"};
    return GenericTestMain(args, "lowest_common_ancestor.cc",
                           "lowest_common_ancestor.tsv", &LcaWrapper,
                           DefaultComparator{}, param_names);
}
