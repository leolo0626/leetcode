#include <algorithm>

class TreeNode {
    public:
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {};
        TreeNode(): TreeNode(0, nullptr, nullptr) {};
        TreeNode(int x): TreeNode(x, nullptr, nullptr) {};

        int getHeight() {
            return std::max(_Height(left), _Height(right)) + 1;
        }
    private:
        int _Height(TreeNode* root) {
            if (root == nullptr) return -1;

            return std::max(_Height(root->left), _Height(root->right)) + 1;

        }
};

