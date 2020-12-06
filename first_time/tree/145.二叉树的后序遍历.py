#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        self.traverse_path_list = []
        self._postorder(root)
        return self.traverse_path_list
    def _postorder(self, node):
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        self.traverse_path_list.append(node.val)
        
# @lc code=end

