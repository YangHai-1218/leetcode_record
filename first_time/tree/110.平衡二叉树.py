#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getheight(root) != -1
    
    def getheight(self, node):
        if node is None:
            return 0
        
        leftheight = self.getheight(node.left)
        rightheight = self.getheight(node.right)
        if leftheight == -1 or rightheight == -1:
            return -1
        if abs(leftheight - rightheight) > 1:
            return -1 
        else:
            return 1 + max(leftheight, rightheight)
# @lc code=end

