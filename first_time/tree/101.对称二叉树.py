#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._issymmetric(root.left, root.right)
    
    def _issymmetric(self, left_node:TreeNode, right_node:TreeNode):
        if left_node is None and right_node is not None:
            return False 
        elif left_node is not None and right_node is None:
            return False 
        elif left_node is None and right_node is None:
            return True 
        elif left_node.val != right_node.val:
            return False

        flag_outer = self._issymmetric(left_node.left, right_node.right)
        flag_inner = self._issymmetric(left_node.right,right_node.left)
        if flag_inner and flag_outer:
            return True 
        else:
            return False
# @lc code=end

