#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        path = []
        self.getpathsum(root, path, targetSum)
        return self.result
    

    def getpathsum(self, node, path, target):
        path.append(node.val)
        if node.left is None and node.right is None:
            if sum(path) == target:
                self.result.append(path.copy())
                return
        
        if node.left is not None:
            self.getpathsum(node.left, path, target)
            path.pop(-1)
        
        if node.right is not None:
            self.getpathsum(node.right, path, target)
            path.pop(-1)
        

# @lc code=end

