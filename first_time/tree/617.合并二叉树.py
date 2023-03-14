#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traversal(root1, root2)
    
    def traversal(self, node_1:TreeNode, node_2:TreeNode):
        if node_1 is None and node_2 is None:
            return None 
        elif node_1 is not None and node_2 is None:
            node = TreeNode(val=node_1.val)
            node.left = self.traversal(node_1.left, None)
            node.right = self.traversal(node_1.right, None)
        elif node_1 is None and node_2 is not None:
            node = TreeNode(val=node_2.val)
            node.left = self.traversal(None, node_2.left)
            node.right = self.traversal(None, node_2.right)
        else:
            node = TreeNode(val=node_1.val+node_2.val)
            node.left = self.traversal(node_1.left, node_2.left)
            node.right = self.traversal(node_1.right, node_2.right)
        
        return node

# @lc code=end

