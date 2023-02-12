#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftleaves = []
        self.getsumofleftleaves(root, leftleaves, 0)
        return sum(leftleaves) if len(leftleaves)>0 else 0
    
    def getsumofleftleaves(self, node, leftleave, leftflag):
        if node.left is None and node.right is None and leftflag:
            leftleave.append(node.val)
            return 
        
        if node.left is not None:
            self.getsumofleftleaves(node.left, leftleave, 1)
        if node.right is not None:
            self.getsumofleftleaves(node.right, leftleave, 0)
        
            

# @lc code=end

