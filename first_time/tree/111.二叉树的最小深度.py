#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历（BFS）
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         queue = [root]
#         level = 0
#         while queue:
#             size = len(queue)
#             cur_level_node = []
#             for _ in range(size):
#                 cur_node = queue.pop(0)
#                 if cur_node is not None:
#                     cur_level_node.append(cur_node)
#                     queue.append(cur_node.left)
#                     queue.append(cur_node.right)
#                     if cur_node.left is None and cur_node.right is None:
#                         return level + 1
            
#             if len(cur_level_node) > 0:
#                 level += 1
#         return level


# 后序遍历
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getdepth(root)

    def getdepth(self, node):
        if node is None:
            return 0 
        leftdepth = self.getdepth(node.left)
        rightdepth = self.getdepth(node.right)

        if node.left is None and node.right is not None:
            return 1 + rightdepth
        
        if node.right is None and node.left is not None:
            return 1 + leftdepth
        
        return 1 + min(leftdepth, rightdepth)



# @lc code=end

