#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)


    def search(self, node, val):
        if node is None:
            return None
        if node.val > val:
            return self.search(node.left, val)
        elif node.val < val:
            return self.search(node.right, val)
        else:
            return node
# @lc code=end

