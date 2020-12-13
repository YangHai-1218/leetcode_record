#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
            

        # 确定右子树的长度
        L, i  = 0, len(inorder)-1
        while i >= 0 and inorder[i] != postorder[-1]:
            i -= 1
            L += 1
       
        root = TreeNode(postorder[-1])
        
        # 左子树
        root.left = self.buildTree(inorder[:i], postorder[:i])
        # print(f'left tree: inorder:{inorder[:L]}, postorder:{postorder[:L]}')
        # print(f'right tree: inorder:{inorder[L+1:]}, postorder:{postorder[L:-1]}')
        # 右子树
        root.right = self.buildTree(inorder[i+1:], postorder[len(postorder)-L-1:-1])
        return root
# @lc code=end

