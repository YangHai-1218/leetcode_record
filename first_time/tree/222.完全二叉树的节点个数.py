#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.getsum(root)

    def getsum(self, node):
        if node is None:
            return 0
        leftsum = self.getsum(node.left)
        rightsum = self.getsum(node.right)
        sum = leftsum + rightsum + 1
        return sum

# @lc code=end

