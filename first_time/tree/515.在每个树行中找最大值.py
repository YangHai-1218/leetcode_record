#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS version
class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            current_level_size = len(queue)
            current_level_val = []
            for _ in range(current_level_size):
                current_node = queue.pop(0)
                current_level_val.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            result.append(max(current_level_val))
        return result

        
# @lc code=end

