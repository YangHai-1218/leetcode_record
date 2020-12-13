#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._dfs(root)
        return root
    
    def _dfs(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self._dfs(node.left)
        self._dfs(node.right)
# @lc code=end

