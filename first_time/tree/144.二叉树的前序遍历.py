#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# class Solution:
#     def __init__(self):
#         self.traverse_path_list = []
#     def preorderTraversal(self, root):
#         self.preorder(root)
#         return self.traverse_path_list
    
#     def preorder(self,root):
#         if not root:
#             return
#         self.traverse_path_list.append(root.val)
#         self.preorder(root.left)
#         self.preorder(root.right)


# iterate
class Solution:
    def preorderTraversal(self, root):
        stack = []
        ans = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur is not None:
                ans.append(cur.val)
            else:
                continue
            stack.append(cur.right)
            stack.append(cur.left)
        
        return ans
            

        
        
# @lc code=end

