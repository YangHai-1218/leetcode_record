#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        self.traversal(root, vals)
        fastpointer, slowpointer = 0, 0
        maxcount, ans = 0, []
        while fastpointer < len(vals):
            count = 0
            while fastpointer < len(vals) and vals[fastpointer] == vals[slowpointer]:
                count += 1
                fastpointer += 1
            if maxcount < count:
                ans = [vals[slowpointer], ]
                maxcount = count
            elif maxcount == count:
                ans.append(vals[slowpointer])
            slowpointer = fastpointer
        return ans
    
    def traversal(self, node, vals):
        if node is None:
            return
        
        self.traversal(node.left, vals)
        vals.append(node.val)
        self.traversal(node.right, vals)
# @lc code=end

