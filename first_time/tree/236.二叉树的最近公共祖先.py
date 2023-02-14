#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.find_q_or_p(root, q, p)
        return result



    
    def find_q_or_p(self, node, q, p):
        if node is None:
            return False
        if node == q or node == p:
            return node
        leftflag = self.find_q_or_p(node.left, q, p)
        rightflag = self.find_q_or_p(node.right, q, p)
    
        if leftflag and rightflag:
            return node
        elif leftflag and not rightflag:
            return leftflag
        elif not leftflag and rightflag:
            return rightflag
        else:
            return False
        
# @lc code=end

