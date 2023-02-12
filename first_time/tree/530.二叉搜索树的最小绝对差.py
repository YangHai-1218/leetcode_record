#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        self.traversal(root, vals)
        ans = 100000000
        for i in range(len(vals)-1):
            if vals[i+1] - vals[i] < ans:
                ans = vals[i+1] - vals[i]
        return ans

    def traversal(self, node, vals):
        if node is None:
            return vals
        
        self.traversal(node.left, vals)
        vals.append(node.val)
        self.traversal(node.right, vals)

# @lc code=end

