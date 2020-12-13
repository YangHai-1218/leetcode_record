#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        self.ans = []
        queue = [root]
        while queue:
            current_level_size = len(queue)
            for i in range(current_level_size):
                if i == current_level_size - 1:
                    node = queue.pop(0)
                    self.ans.append(node.val)
                else:
                    node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return self.ans

    

# @lc code=end

