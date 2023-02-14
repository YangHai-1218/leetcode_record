#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        if p.val > q.val:
            p, q = q, p
        ans = self.find_q_or_p(root, p, q)
        return ans
    

    def find_q_or_p(self, node, p, q):
        if node is None:
            return False 
        if node == p or node == q:
            return node 
        
        if node.val > q.val:
            # p < q < node
            flag = self.find_q_or_p(node.left, p, q)
            return flag
        elif node.val < p.val:
            # node < p < q
            flag = self.find_q_or_p(node.right, p, q)
            return flag
        else:
            # p < node < q
            leftflag = self.find_q_or_p(node.left, p, q)
            rightflag = self.find_q_or_p(node.right, p, q)
            if leftflag or rightflag:
                return node
            else:
                return False
        # return node 
# @lc code=end

