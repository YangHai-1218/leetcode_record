#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.num_sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.travsal(root)
        return root
    
    def traversal(self, node):
        if node.left is None and node.right is None:
            self.num_sum += node.val
            node.val = self.num_sum
            return
        if node.right is not None:
            self.traversal(node.right)
        self.num_sum += node.val
        node.val = self.num_sum
        if node.left is not None:
            self.traversal(node.left)



# @lc code=end

