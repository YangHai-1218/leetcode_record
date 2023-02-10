#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def __init__(self):
#         self.traverse_path_list = []
#     def inorder(self, root):
#         if not root:
#             return
#         self.inorder(root.left)
#         self.traverse_path_list.append(root.val)
#         self.inorder(root.right) 
#     def inorderTraversal(self,root):
#         self.inorder(root)
#         return self.traverse_path_list

class Solution:
    def inorderTraversal(self,root):
        stack, ans = [], []
        cur = root
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans 

# @lc code=end

