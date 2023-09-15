/*
 * @lc app=leetcode.cn id=337 lang=cpp
 *
 * [337] 打家劫舍 III
 */

// @lc code=start
#include <vector>
using namespace std;
// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution {
public:
    int rob(TreeNode* root) {
        vector<int>result = dfs(root);
        return max(result[0], result[1]);
    }


    vector<int> dfs(TreeNode* root){
        if (root == nullptr){
            return {0, 0};
        }
        vector<int> left = dfs(root->left);
        vector<int> right = dfs(root->right);
        // don't rob current node
        int result_0 = max(left[0], left[1]) + max(right[0], right[1]);
        // rob current node
        int result_1 = left[1] + root->val + right[1];
        return {result_1, result_0};
        

    }
};
// @lc code=end

