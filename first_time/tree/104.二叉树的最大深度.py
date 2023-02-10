#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getdepth(root)
    

    def getdepth(self, node):
        if node is None:
            return 0
        
        leftdepth = self.getdepth(node.left)
        rightdepth = self.getdepth(node.right)
        depth = max(leftdepth, rightdepth) + 1
        return depth
                

# @lc code=end

