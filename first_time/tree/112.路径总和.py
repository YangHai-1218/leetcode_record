#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def __init__(self) -> None:
        self.pathsum = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False 
        
        path = []
        return self.getpathsum(root, path, targetSum)
        
    
    def getpathsum(self, node, path, target):
        path.append(node.val)
        if node.left is None and node.right is None:
            if sum(path) == target:
                return True
            else:
                return False
        
        leftflag, rightflag = False, False
        if node.left is not None:
            leftflag = self.getpathsum(node.left, path, target)
            path.pop(-1)
    
        if node.right is not None:
            rightflag = self.getpathsum(node.right, path, target)
            path.pop(-1)
        if leftflag or rightflag:
            return True
        else:
            return False
        

        
# @lc code=end

