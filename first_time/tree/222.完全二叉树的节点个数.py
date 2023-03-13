#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# general solution
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         return self.getsum(root)

#     def getsum(self, node):
#         if node is None:
#             return 0
#         leftsum = self.getsum(node.left)
#         rightsum = self.getsum(node.right)
#         sum = leftsum + rightsum + 1
#         return sum

# Complete Binary Tree 
class Solution:
    def countNodes(self, root:Optional[TreeNode]) -> int:
        return self.get_tree_node_sum(root)
    
    def get_tree_node_sum(self, node):
        if node is None:
            return 0
        
        left = node.left 
        right = node.right 

        leftheight, rightheight = 0, 0
        while left:
            leftheight += 1
            left = left.left 
        while right:
            rightheight += 1
            right = right.right 
        
        if leftheight == rightheight:
            nodesum = 2**(leftheight+1) - 1
        elif leftheight > rightheight:
            left_nodesum = self.get_tree_node_sum(node.left)
            right_nodesum = self.get_tree_node_sum(node.right)
            nodesum = left_nodesum + right_nodesum + 1
        return nodesum
# @lc code=end

