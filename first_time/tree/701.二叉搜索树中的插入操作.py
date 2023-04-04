#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)
        self._insert(root, val)
        return root
    
    def _insert(self, node, val):
        if node.val < val:
            if node.right is None:
                node.right = TreeNode(val=val)
                return
            else:
                self._insert(node.right, val)
        elif node.val > val:
            if node.left is None:
                node.left = TreeNode(val=val)
                return
            else:
                self._insert(node.left, val)
# @lc code=end

