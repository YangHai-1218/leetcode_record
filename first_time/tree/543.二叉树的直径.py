#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 本质上是在求深度，求左子树的深度，右子树的深度
class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        self.ans = 0
        self._dfs(root)
        return self.ans
    def _dfs(self,node):
        if node is None:
            return 0
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        self.ans = max(self.ans, (left+right))
        return max(left, right) + 1

        
# @lc code=end

