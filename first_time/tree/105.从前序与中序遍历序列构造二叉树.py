#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root =  TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # 找左子树的长度
        L = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                L = i
                break
        
        # 左子树
        root.left = self.buildTree(preorder[1:L+1], inorder[:L])
        # 右子树
        root.right = self.buildTree(preorder[L+1:], inorder[L+1:])
        return root
# @lc code=end

