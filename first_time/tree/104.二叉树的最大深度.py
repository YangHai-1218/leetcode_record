#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         queue = [root]
#         ans = 0
#         while queue:
#             size = len(queue)
#             cur_level_node = []
#             for _ in range(size):
#                 cur_node = queue.pop(0)
#                 if cur_node is not None:
#                     cur_level_node.append(cur_node)
#                     queue.append(cur_node.left)
#                     queue.append(cur_node.right)
#             if len(cur_level_node) > 0:
#                 ans += 1
#         return ans

# DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         return self.getheight(root)
    

#     def getheight(self, node):
#         if node is None:
#             return 0
        
#         leftheight = self.getheight(node.left)
#         rightheight = self.getheight(node.right)
#         height = max(leftheight, rightheight) + 1
#         return height

# 前序遍历
class Solution:
    def __init__(self) -> None:
        self.result = 0
    
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.getdepth(root, 1)
        return self.result
    
    def getdepth(self, node:TreeNode, depth:int):
        self.result = depth if self.result < depth else self.result
        if node.left is None and node.right is None:
            return 
        if node.left is not None:
            depth += 1
            self.getdepth(node.left, depth)
            depth -= 1
        
        if node.right is not None:
            depth += 1
            self.getdepth(node.right, depth)
            depth -= 1
        return
# @lc code=end

