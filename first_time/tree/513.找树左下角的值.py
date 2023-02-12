#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
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
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         queue = [root]
#         ans = 0
#         while queue:
#             size = len(queue)
#             cur_level_node = []
#             for _ in range(size):
#                 cur_node = queue.pop(0)
#                 if cur_node is not None:
#                     cur_level_node.append(cur_node.val)
#                     queue.append(cur_node.left)
#                     queue.append(cur_node.right)
#             if len(cur_level_node) > 0:
#                 ans = cur_level_node[0]
#         return ans

# DFS
class Solution:
    def __init__(self) -> None:
        self.maxdepth = -1
        self.result = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.getleftdepth(root, 0)
        return self.result
    
    def getleftdepth(self, node, depth):
        if node.left is None and node.right is None:
            if self.maxdepth < depth:
                self.maxdepth = depth
                self.result = node.val
            return 
        if node.left is not None:
            depth += 1
            self.getleftdepth(node.left, depth)
            depth -= 1
        
        if node.right is not None:
            depth += 1
            self.getleftdepth(node.right, depth)
            depth -= 1
        return 

# @lc code=end

