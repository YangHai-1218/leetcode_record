#include <vector>
#include <iostream>



struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr){
            return root;
        }
        dfs(root);
        return root;
    }
    void dfs(TreeNode* root){
        if (root == nullptr){
            return;
        }
        else if (root->left == nullptr && root->right == nullptr){
            return;
        }else{
            TreeNode* temp = root->left;
            root->left = root->right;
            root->right = temp;
            dfs(root->left);
            dfs(root->right);
            return;
        }
    }
};


int main(){
    vector<int> nums;
    Solution test;
    TreeNode root = TreeNode(2);
    root.left = new TreeNode(3);
    root.right = nullptr;
    root.left->left = new TreeNode(1);
    TreeNode* root_ = &root;
    test.invertTree(root_);
    return 0;
}